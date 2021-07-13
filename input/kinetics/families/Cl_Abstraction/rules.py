#!/usr/bin/env python
# encoding: utf-8

name = "Cl_Abstraction/rules"
shortDesc = ""
longDesc = """
General comments go at the top of the file,

or in a section(s) titled 'General'

.. the ID must match those in the rateLibrary AS A STRING (ie. '2' is different from '02')


.. [MRHCBSQB3RRHO] M.R. Harper (mrharper_at_mit_dot_edu or michael.harper.jr_at_gmail_dot_com)
The geometries of all reactants, products, and the transition state were optimized using the CBS-QB3 calculations.  The zero-point
energy is that computed by the CBS-QB3 calculations.  The frequencies were computed with B3LYP/CBSB7.
In computing k(T), an asymmetric tunneling correction was employed, the calculated frequencies were scaled by 0.99, and the
temperatures used were: 300, 331, 370, 419, 482, 568, 692, 885, 1227, 2000 (evenly spaced on inverse temperature scale).

.. [Tsang1990] W. Tsang; "Chemical kinetic database for combustion chemistry. Part IV. Isobutane" J. Phys. Chem. Ref. Data 19 (1990) 1-68

.. [Tsang1991] W. Tsang; "Chemical kinetic database for combustion chemistry. Part V. Propene" J. Phys. Chem. Ref. Data 20 (1991) 221-273
"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(1.43925e+09,'m^3/(mol*s)'), n=-0.813567, w0=(325033,'J/mol'), E0=(68607.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.10605851595914033, var=18.44356937483735, Tref=1000.0, N=394, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 394 training reactions at node Root
    Total Standard Deviation in ln(k): 8.87600932879668"""),
    rank = 11,
    shortDesc = """BM rule fitted to 394 training reactions at node Root
Total Standard Deviation in ln(k): 8.87600932879668""",
    longDesc = 
"""
BM rule fitted to 394 training reactions at node Root
Total Standard Deviation in ln(k): 8.87600932879668
""",
)

entry(
    index = 2,
    label = "Root_1R->H",
    kinetics = ArrheniusBM(A=(3.69815e+15,'m^3/(mol*s)'), n=-2.89183, w0=(372872,'J/mol'), E0=(105028,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.22774223624323925, var=10.731494749812493, Tref=1000.0, N=65, data_mean=0.0, correlation='Root_1R->H',), comment="""BM rule fitted to 65 training reactions at node Root_1R->H
    Total Standard Deviation in ln(k): 7.139520340051507"""),
    rank = 11,
    shortDesc = """BM rule fitted to 65 training reactions at node Root_1R->H
Total Standard Deviation in ln(k): 7.139520340051507""",
    longDesc = 
"""
BM rule fitted to 65 training reactions at node Root_1R->H
Total Standard Deviation in ln(k): 7.139520340051507
""",
)

entry(
    index = 3,
    label = "Root_N-1R->H",
    kinetics = ArrheniusBM(A=(3.21011e+13,'m^3/(mol*s)'), n=-2.06424, w0=(315581,'J/mol'), E0=(74219.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.17306006590457826, var=16.88281608403024, Tref=1000.0, N=329, data_mean=0.0, correlation='Root_N-1R->H',), comment="""BM rule fitted to 329 training reactions at node Root_N-1R->H
    Total Standard Deviation in ln(k): 8.67202093482144"""),
    rank = 11,
    shortDesc = """BM rule fitted to 329 training reactions at node Root_N-1R->H
Total Standard Deviation in ln(k): 8.67202093482144""",
    longDesc = 
"""
BM rule fitted to 329 training reactions at node Root_N-1R->H
Total Standard Deviation in ln(k): 8.67202093482144
""",
)

entry(
    index = 4,
    label = "Root_1R->H_3R->O",
    kinetics = ArrheniusBM(A=(0.00387886,'m^3/(mol*s)'), n=3.02543, w0=(350000,'J/mol'), E0=(35000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.08361486753058357, var=4.1865036263408895, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R->H_3R->O',), comment="""BM rule fitted to 6 training reactions at node Root_1R->H_3R->O
    Total Standard Deviation in ln(k): 4.311965475046433"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R->H_3R->O
Total Standard Deviation in ln(k): 4.311965475046433""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R->H_3R->O
Total Standard Deviation in ln(k): 4.311965475046433
""",
)

entry(
    index = 5,
    label = "Root_1R->H_N-3R->O",
    kinetics = ArrheniusBM(A=(2193.96,'m^3/(mol*s)'), n=0.669077, w0=(375198,'J/mol'), E0=(77300.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.007002813405458301, var=10.765081894051965, Tref=1000.0, N=59, data_mean=0.0, correlation='Root_1R->H_N-3R->O',), comment="""BM rule fitted to 59 training reactions at node Root_1R->H_N-3R->O
    Total Standard Deviation in ln(k): 6.595167731327816"""),
    rank = 11,
    shortDesc = """BM rule fitted to 59 training reactions at node Root_1R->H_N-3R->O
Total Standard Deviation in ln(k): 6.595167731327816""",
    longDesc = 
"""
BM rule fitted to 59 training reactions at node Root_1R->H_N-3R->O
Total Standard Deviation in ln(k): 6.595167731327816
""",
)

entry(
    index = 6,
    label = "Root_N-1R->H_3R->H",
    kinetics = ArrheniusBM(A=(1.15744e+09,'m^3/(mol*s)'), n=-0.517992, w0=(373140,'J/mol'), E0=(77687.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07009072635127325, var=4.921338295966679, Tref=1000.0, N=69, data_mean=0.0, correlation='Root_N-1R->H_3R->H',), comment="""BM rule fitted to 69 training reactions at node Root_N-1R->H_3R->H
    Total Standard Deviation in ln(k): 4.623429602697268"""),
    rank = 11,
    shortDesc = """BM rule fitted to 69 training reactions at node Root_N-1R->H_3R->H
Total Standard Deviation in ln(k): 4.623429602697268""",
    longDesc = 
"""
BM rule fitted to 69 training reactions at node Root_N-1R->H_3R->H
Total Standard Deviation in ln(k): 4.623429602697268
""",
)

entry(
    index = 7,
    label = "Root_N-1R->H_N-3R->H",
    kinetics = ArrheniusBM(A=(3.19605e+14,'m^3/(mol*s)'), n=-2.42163, w0=(300306,'J/mol'), E0=(72953.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1962458974385311, var=20.17541547015201, Tref=1000.0, N=260, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H',), comment="""BM rule fitted to 260 training reactions at node Root_N-1R->H_N-3R->H
    Total Standard Deviation in ln(k): 9.497759086267452"""),
    rank = 11,
    shortDesc = """BM rule fitted to 260 training reactions at node Root_N-1R->H_N-3R->H
Total Standard Deviation in ln(k): 9.497759086267452""",
    longDesc = 
"""
BM rule fitted to 260 training reactions at node Root_N-1R->H_N-3R->H
Total Standard Deviation in ln(k): 9.497759086267452
""",
)

entry(
    index = 8,
    label = "Root_1R->H_3R->O_Ext-3O-R",
    kinetics = ArrheniusBM(A=(1.79393e-05,'m^3/(mol*s)'), n=3.82684, w0=(350000,'J/mol'), E0=(35000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.6260903035374364, var=8.435215208207387, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_3R->O_Ext-3O-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_3R->O_Ext-3O-R
    Total Standard Deviation in ln(k): 7.395531901247499"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_3R->O_Ext-3O-R
Total Standard Deviation in ln(k): 7.395531901247499""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_3R->O_Ext-3O-R
Total Standard Deviation in ln(k): 7.395531901247499
""",
)

entry(
    index = 9,
    label = "Root_1R->H_3R->O_3O-u1",
    kinetics = ArrheniusBM(A=(0.000500647,'m^3/(mol*s)'), n=3.31619, w0=(350000,'J/mol'), E0=(35000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.09630791755504133, var=14.983567501557328, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_3R->O_3O-u1',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_3R->O_3O-u1
    Total Standard Deviation in ln(k): 8.002031197281925"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_3R->O_3O-u1
Total Standard Deviation in ln(k): 8.002031197281925""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_3R->O_3O-u1
Total Standard Deviation in ln(k): 8.002031197281925
""",
)

entry(
    index = 10,
    label = "Root_1R->H_3R->O_N-3O-u1",
    kinetics = ArrheniusBM(A=(37484.4,'m^3/(mol*s)'), n=0.582358, w0=(350000,'J/mol'), E0=(35000,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R->O_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R->O_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R->O_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R->O_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1",
    kinetics = ArrheniusBM(A=(2.41208e+07,'m^3/(mol*s)'), n=-0.545215, w0=(375075,'J/mol'), E0=(87054,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.08049693589224978, var=10.2910306849045, Tref=1000.0, N=56, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1',), comment="""BM rule fitted to 56 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1
    Total Standard Deviation in ln(k): 6.633370834303112"""),
    rank = 11,
    shortDesc = """BM rule fitted to 56 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1
Total Standard Deviation in ln(k): 6.633370834303112""",
    longDesc = 
"""
BM rule fitted to 56 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1
Total Standard Deviation in ln(k): 6.633370834303112
""",
)

entry(
    index = 12,
    label = "Root_1R->H_N-3R->O_N-3BrCClFH-u1",
    kinetics = ArrheniusBM(A=(0.000402938,'m^3/(mol*s)'), n=2.98496, w0=(377500,'J/mol'), E0=(51822.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.019289044531561227, var=3.3292098135641837, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-3R->O_N-3BrCClFH-u1',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-3R->O_N-3BrCClFH-u1
    Total Standard Deviation in ln(k): 3.7063290891513314"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-3R->O_N-3BrCClFH-u1
Total Standard Deviation in ln(k): 3.7063290891513314""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-3R->O_N-3BrCClFH-u1
Total Standard Deviation in ln(k): 3.7063290891513314
""",
)

entry(
    index = 13,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.7155e-08,'m^3/(mol*s)'), n=4.44799, w0=(377500,'J/mol'), E0=(36838.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.19534217145575014, var=4.73576852296705, Tref=1000.0, N=60, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C',), comment="""BM rule fitted to 60 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 4.853478062360042"""),
    rank = 11,
    shortDesc = """BM rule fitted to 60 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 4.853478062360042""",
    longDesc = 
"""
BM rule fitted to 60 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 4.853478062360042
""",
)

entry(
    index = 14,
    label = "Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(280.966,'m^3/(mol*s)'), n=1.66499, w0=(344077,'J/mol'), E0=(34407.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0440775975999143, var=2.583623122194221, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 3.3330892784719355"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 3.3330892784719355""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 3.3330892784719355
""",
)

entry(
    index = 15,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(2.0197e+24,'m^3/(mol*s)'), n=-5.2915, w0=(313851,'J/mol'), E0=(100605,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.354791064877922, var=18.830636722397905, Tref=1000.0, N=158, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C',), comment="""BM rule fitted to 158 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 9.59083867684477"""),
    rank = 11,
    shortDesc = """BM rule fitted to 158 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 9.59083867684477""",
    longDesc = 
"""
BM rule fitted to 158 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 9.59083867684477
""",
)

entry(
    index = 16,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.172157,'m^3/(mol*s)'), n=2.03089, w0=(279324,'J/mol'), E0=(112.873,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.12780601733171976, var=20.74110294178891, Tref=1000.0, N=102, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C',), comment="""BM rule fitted to 102 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 9.451165537647167"""),
    rank = 11,
    shortDesc = """BM rule fitted to 102 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 9.451165537647167""",
    longDesc = 
"""
BM rule fitted to 102 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 9.451165537647167
""",
)

entry(
    index = 17,
    label = "Root_1R->H_3R->O_Ext-3O-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(0.00118512,'m^3/(mol*s)'), n=2.96558, w0=(350000,'J/mol'), E0=(35000,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R->O_Ext-3O-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R->O_Ext-3O-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R->O_Ext-3O-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R->O_Ext-3O-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C",
    kinetics = ArrheniusBM(A=(1.49907e-16,'m^3/(mol*s)'), n=6.32648, w0=(377500,'J/mol'), E0=(29992.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2661598351128361, var=7.475307111928749, Tref=1000.0, N=53, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C',), comment="""BM rule fitted to 53 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C
    Total Standard Deviation in ln(k): 6.1498910565668945"""),
    rank = 11,
    shortDesc = """BM rule fitted to 53 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C
Total Standard Deviation in ln(k): 6.1498910565668945""",
    longDesc = 
"""
BM rule fitted to 53 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C
Total Standard Deviation in ln(k): 6.1498910565668945
""",
)

entry(
    index = 19,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_N-3BrCClFH->C",
    kinetics = ArrheniusBM(A=(73287,'m^3/(mol*s)'), n=0.736388, w0=(332230,'J/mol'), E0=(33223,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0696316217747085, var=2.8855487410586758, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_N-3BrCClFH->C',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_N-3BrCClFH->C
    Total Standard Deviation in ln(k): 3.580377856983489"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_N-3BrCClFH->C
Total Standard Deviation in ln(k): 3.580377856983489""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_N-3BrCClFH->C
Total Standard Deviation in ln(k): 3.580377856983489
""",
)

entry(
    index = 20,
    label = "Root_1R->H_N-3R->O_N-3BrCClFH-u1_Ext-3BrCClFH-R",
    kinetics = ArrheniusBM(A=(0.00180769,'m^3/(mol*s)'), n=2.92944, w0=(377500,'J/mol'), E0=(66574.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.3849888924453412e-05, var=2.972861947826329, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-3R->O_N-3BrCClFH-u1_Ext-3BrCClFH-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->O_N-3BrCClFH-u1_Ext-3BrCClFH-R
    Total Standard Deviation in ln(k): 3.456596872704742"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->O_N-3BrCClFH-u1_Ext-3BrCClFH-R
Total Standard Deviation in ln(k): 3.456596872704742""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->O_N-3BrCClFH-u1_Ext-3BrCClFH-R
Total Standard Deviation in ln(k): 3.456596872704742
""",
)

entry(
    index = 21,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0",
    kinetics = ArrheniusBM(A=(0.000111116,'m^3/(mol*s)'), n=3.3088, w0=(377500,'J/mol'), E0=(48548,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.12862526796432114, var=5.059960469910624, Tref=1000.0, N=53, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0',), comment="""BM rule fitted to 53 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0
    Total Standard Deviation in ln(k): 4.8327014952231675"""),
    rank = 11,
    shortDesc = """BM rule fitted to 53 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0
Total Standard Deviation in ln(k): 4.8327014952231675""",
    longDesc = 
"""
BM rule fitted to 53 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0
Total Standard Deviation in ln(k): 4.8327014952231675
""",
)

entry(
    index = 22,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0",
    kinetics = ArrheniusBM(A=(3.26898e-18,'m^3/(mol*s)'), n=7.34094, w0=(377500,'J/mol'), E0=(-4076.57,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3361854162256975, var=1.1902891964007432, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0
    Total Standard Deviation in ln(k): 3.031860475393479"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0
Total Standard Deviation in ln(k): 3.031860475393479""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0
Total Standard Deviation in ln(k): 3.031860475393479
""",
)

entry(
    index = 23,
    label = "Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_Ext-1BrClFO-R",
    kinetics = ArrheniusBM(A=(1.34127,'m^3/(mol*s)'), n=2.54457, w0=(350000,'J/mol'), E0=(35000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.7022123593656946, var=1.0174030857893832, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_Ext-1BrClFO-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_Ext-1BrClFO-R
    Total Standard Deviation in ln(k): 3.786456784590486"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_Ext-1BrClFO-R
Total Standard Deviation in ln(k): 3.786456784590486""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_Ext-1BrClFO-R
Total Standard Deviation in ln(k): 3.786456784590486
""",
)

entry(
    index = 24,
    label = "Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_1BrClFO->O",
    kinetics = ArrheniusBM(A=(8.82928,'m^3/(mol*s)'), n=2.11953, w0=(350000,'J/mol'), E0=(35000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05626692271938685, var=8.479938391034016, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_1BrClFO->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_1BrClFO->O
    Total Standard Deviation in ln(k): 5.979229635883354"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_1BrClFO->O
Total Standard Deviation in ln(k): 5.979229635883354""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_1BrClFO->O
Total Standard Deviation in ln(k): 5.979229635883354
""",
)

entry(
    index = 25,
    label = "Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClFO->O",
    kinetics = ArrheniusBM(A=(999343,'m^3/(mol*s)'), n=0.472541, w0=(332230,'J/mol'), E0=(33223,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0260914155751895, var=0.6085246273576697, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClFO->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClFO->O
    Total Standard Deviation in ln(k): 1.6294098296529749"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClFO->O
Total Standard Deviation in ln(k): 1.6294098296529749""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClFO->O
Total Standard Deviation in ln(k): 1.6294098296529749
""",
)

entry(
    index = 26,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClFO->Br",
    kinetics = ArrheniusBM(A=(0.00281823,'m^3/(mol*s)'), n=1.23493, w0=(272920,'J/mol'), E0=(-1.57098e+06,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.5363609968987084, var=1671.7426966600656, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClFO->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClFO->Br
    Total Standard Deviation in ln(k): 85.82770678347114"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClFO->Br
Total Standard Deviation in ln(k): 85.82770678347114""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClFO->Br
Total Standard Deviation in ln(k): 85.82770678347114
""",
)

entry(
    index = 27,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br",
    kinetics = ArrheniusBM(A=(7.20603e+26,'m^3/(mol*s)'), n=-6.02769, w0=(314376,'J/mol'), E0=(105907,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.3965582969512766, var=14.767576665931806, Tref=1000.0, N=156, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br',), comment="""BM rule fitted to 156 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br
    Total Standard Deviation in ln(k): 8.700294831584497"""),
    rank = 11,
    shortDesc = """BM rule fitted to 156 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br
Total Standard Deviation in ln(k): 8.700294831584497""",
    longDesc = 
"""
BM rule fitted to 156 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br
Total Standard Deviation in ln(k): 8.700294831584497
""",
)

entry(
    index = 28,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O",
    kinetics = ArrheniusBM(A=(753.723,'m^3/(mol*s)'), n=1.19199, w0=(267012,'J/mol'), E0=(25097.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.009982177181012793, var=3.083805665060243, Tref=1000.0, N=31, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O',), comment="""BM rule fitted to 31 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O
    Total Standard Deviation in ln(k): 3.545549571106947"""),
    rank = 11,
    shortDesc = """BM rule fitted to 31 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O
Total Standard Deviation in ln(k): 3.545549571106947""",
    longDesc = 
"""
BM rule fitted to 31 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O
Total Standard Deviation in ln(k): 3.545549571106947
""",
)

entry(
    index = 29,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O",
    kinetics = ArrheniusBM(A=(25.3482,'m^3/(mol*s)'), n=1.29797, w0=(284700,'J/mol'), E0=(24342.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0698969180623387, var=28.27867552079607, Tref=1000.0, N=71, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O',), comment="""BM rule fitted to 71 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O
    Total Standard Deviation in ln(k): 10.836340025147756"""),
    rank = 11,
    shortDesc = """BM rule fitted to 71 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O
Total Standard Deviation in ln(k): 10.836340025147756""",
    longDesc = 
"""
BM rule fitted to 71 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O
Total Standard Deviation in ln(k): 10.836340025147756
""",
)

entry(
    index = 30,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.93604e-16,'m^3/(mol*s)'), n=6.27411, w0=(377500,'J/mol'), E0=(30577.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.26126359383889286, var=7.589293234212873, Tref=1000.0, N=50, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R',), comment="""BM rule fitted to 50 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R
    Total Standard Deviation in ln(k): 6.179220079786713"""),
    rank = 11,
    shortDesc = """BM rule fitted to 50 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R
Total Standard Deviation in ln(k): 6.179220079786713""",
    longDesc = 
"""
BM rule fitted to 50 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R
Total Standard Deviation in ln(k): 6.179220079786713
""",
)

entry(
    index = 31,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_N-3BrCClFH->C_3BrClF->Br",
    kinetics = ArrheniusBM(A=(5.82871e+07,'m^3/(mol*s)'), n=-0.000344372, w0=(323420,'J/mol'), E0=(32342,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_N-3BrCClFH->C_3BrClF->Br',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_N-3BrCClFH->C_3BrClF->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_N-3BrCClFH->C_3BrClF->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_N-3BrCClFH->C_3BrClF->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 32,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_N-3BrCClFH->C_N-3BrClF->Br",
    kinetics = ArrheniusBM(A=(110983,'m^3/(mol*s)'), n=0.583786, w0=(336635,'J/mol'), E0=(33663.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.11518828570550879, var=0.7209792918186334, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_N-3BrCClFH->C_N-3BrClF->Br',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_N-3BrCClFH->C_N-3BrClF->Br
    Total Standard Deviation in ln(k): 1.991648370302813"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_N-3BrCClFH->C_N-3BrClF->Br
Total Standard Deviation in ln(k): 1.991648370302813""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_N-3BrCClFH->C_N-3BrClF->Br
Total Standard Deviation in ln(k): 1.991648370302813
""",
)

entry(
    index = 33,
    label = "Root_1R->H_N-3R->O_N-3BrCClFH-u1_Ext-3BrCClFH-R_4R!H->C",
    kinetics = ArrheniusBM(A=(0.00118183,'m^3/(mol*s)'), n=2.92126, w0=(377500,'J/mol'), E0=(57174.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->O_N-3BrCClFH-u1_Ext-3BrCClFH-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_N-3BrCClFH-u1_Ext-3BrCClFH-R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_N-3BrCClFH-u1_Ext-3BrCClFH-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_N-3BrCClFH-u1_Ext-3BrCClFH-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Root_1R->H_N-3R->O_N-3BrCClFH-u1_Ext-3BrCClFH-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.000796126,'m^3/(mol*s)'), n=2.83903, w0=(377500,'J/mol'), E0=(59376.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->O_N-3BrCClFH-u1_Ext-3BrCClFH-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_N-3BrCClFH-u1_Ext-3BrCClFH-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_N-3BrCClFH-u1_Ext-3BrCClFH-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_N-3BrCClFH-u1_Ext-3BrCClFH-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 35,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.000444928,'m^3/(mol*s)'), n=3.119, w0=(377500,'J/mol'), E0=(49991.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.11964734670218177, var=5.260102670656977, Tref=1000.0, N=50, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R',), comment="""BM rule fitted to 50 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R
    Total Standard Deviation in ln(k): 4.898464076059647"""),
    rank = 11,
    shortDesc = """BM rule fitted to 50 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 4.898464076059647""",
    longDesc = 
"""
BM rule fitted to 50 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 4.898464076059647
""",
)

entry(
    index = 36,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.25541e-20,'m^3/(mol*s)'), n=8.18193, w0=(377500,'J/mol'), E0=(-1835.93,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3265980070967604, var=0.9389546188488358, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R
    Total Standard Deviation in ln(k): 2.763179696878245"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 2.763179696878245""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 2.763179696878245
""",
)

entry(
    index = 37,
    label = "Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_Ext-1BrClFO-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(686.74,'m^3/(mol*s)'), n=1.69184, w0=(350000,'J/mol'), E0=(35000,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_Ext-1BrClFO-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_Ext-1BrClFO-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_Ext-1BrClFO-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_Ext-1BrClFO-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 38,
    label = "Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_1BrClFO->O_1O-u0",
    kinetics = ArrheniusBM(A=(0.0897719,'m^3/(mol*s)'), n=2.82604, w0=(350000,'J/mol'), E0=(35000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.07502255009929547, var=14.98356773290693, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_1BrClFO->O_1O-u0',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_1BrClFO->O_1O-u0
    Total Standard Deviation in ln(k): 7.948550434437251"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_1BrClFO->O_1O-u0
Total Standard Deviation in ln(k): 7.948550434437251""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_1BrClFO->O_1O-u0
Total Standard Deviation in ln(k): 7.948550434437251
""",
)

entry(
    index = 39,
    label = "Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_1BrClFO->O_N-1O-u0",
    kinetics = ArrheniusBM(A=(8.4e+06,'m^3/(mol*s)'), n=0, w0=(350000,'J/mol'), E0=(35000,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_1BrClFO->O_N-1O-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_1BrClFO->O_N-1O-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_1BrClFO->O_N-1O-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_1BrClFO->O_N-1O-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 40,
    label = "Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClFO->O_1BrClF->Br",
    kinetics = ArrheniusBM(A=(8.59e+07,'m^3/(mol*s)'), n=0, w0=(323420,'J/mol'), E0=(32342,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClFO->O_1BrClF->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClFO->O_1BrClF->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClFO->O_1BrClF->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClFO->O_1BrClF->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClFO->O_N-1BrClF->Br",
    kinetics = ArrheniusBM(A=(1.70663e+06,'m^3/(mol*s)'), n=0.354406, w0=(336635,'J/mol'), E0=(33663.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2943830949217219, var=0.7999612370642049, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClFO->O_N-1BrClF->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClFO->O_N-1BrClF->Br
    Total Standard Deviation in ln(k): 2.532702139952888"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClFO->O_N-1BrClF->Br
Total Standard Deviation in ln(k): 2.532702139952888""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClFO->O_N-1BrClF->Br
Total Standard Deviation in ln(k): 2.532702139952888
""",
)

entry(
    index = 42,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClFO->Br_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.9e+08,'m^3/(mol*s)'), n=0, w0=(272920,'J/mol'), E0=(27292,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClFO->Br_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClFO->Br_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClFO->Br_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClFO->Br_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 43,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R",
    kinetics = ArrheniusBM(A=(1.59355e+07,'m^3/(mol*s)'), n=-0.411256, w0=(326563,'J/mol'), E0=(76315.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07788325678124591, var=7.7728086804121395, Tref=1000.0, N=63, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R',), comment="""BM rule fitted to 63 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R
    Total Standard Deviation in ln(k): 5.784839319040918"""),
    rank = 11,
    shortDesc = """BM rule fitted to 63 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R
Total Standard Deviation in ln(k): 5.784839319040918""",
    longDesc = 
"""
BM rule fitted to 63 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R
Total Standard Deviation in ln(k): 5.784839319040918
""",
)

entry(
    index = 44,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0",
    kinetics = ArrheniusBM(A=(1.13356e+27,'m^3/(mol*s)'), n=-5.97577, w0=(304995,'J/mol'), E0=(97399.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.3867870614904246, var=12.203868849591482, Tref=1000.0, N=82, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0',), comment="""BM rule fitted to 82 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0
    Total Standard Deviation in ln(k): 7.975175563417214"""),
    rank = 11,
    shortDesc = """BM rule fitted to 82 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0
Total Standard Deviation in ln(k): 7.975175563417214""",
    longDesc = 
"""
BM rule fitted to 82 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0
Total Standard Deviation in ln(k): 7.975175563417214
""",
)

entry(
    index = 45,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0",
    kinetics = ArrheniusBM(A=(7.62155e+41,'m^3/(mol*s)'), n=-10.1922, w0=(314500,'J/mol'), E0=(139113,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.6694316528385513, var=10.089367636890998, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0
    Total Standard Deviation in ln(k): 8.049782455674196"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0
Total Standard Deviation in ln(k): 8.049782455674196""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0
Total Standard Deviation in ln(k): 8.049782455674196
""",
)

entry(
    index = 46,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R",
    kinetics = ArrheniusBM(A=(9428.29,'m^3/(mol*s)'), n=0.979293, w0=(270222,'J/mol'), E0=(53349.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.09127628940892372, var=5.536834158029212, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R
    Total Standard Deviation in ln(k): 4.946574963027846"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R
Total Standard Deviation in ln(k): 4.946574963027846""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R
Total Standard Deviation in ln(k): 4.946574963027846
""",
)

entry(
    index = 47,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0",
    kinetics = ArrheniusBM(A=(364.228,'m^3/(mol*s)'), n=1.24016, w0=(264704,'J/mol'), E0=(18446.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00398780886031901, var=2.545777375757235, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0',), comment="""BM rule fitted to 19 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0
    Total Standard Deviation in ln(k): 3.2086731484426556"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0
Total Standard Deviation in ln(k): 3.2086731484426556""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0
Total Standard Deviation in ln(k): 3.2086731484426556
""",
)

entry(
    index = 48,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_N-1BrClFO-u0",
    kinetics = ArrheniusBM(A=(405.06,'m^3/(mol*s)'), n=1.2113, w0=(272000,'J/mol'), E0=(26626.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0014744770912550604, var=0.4453592543749315, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_N-1BrClFO-u0',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_N-1BrClFO-u0
    Total Standard Deviation in ln(k): 1.3415695245139632"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_N-1BrClFO-u0
Total Standard Deviation in ln(k): 1.3415695245139632""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_N-1BrClFO-u0
Total Standard Deviation in ln(k): 1.3415695245139632
""",
)

entry(
    index = 49,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_1BrClFO->Br",
    kinetics = ArrheniusBM(A=(9.20189e-07,'m^3/(mol*s)'), n=2.49472, w0=(258420,'J/mol'), E0=(-17195.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.21565797812489, var=620.1679414123168, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_1BrClFO->Br',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_1BrClFO->Br
    Total Standard Deviation in ln(k): 52.978678098690516"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_1BrClFO->Br
Total Standard Deviation in ln(k): 52.978678098690516""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_1BrClFO->Br
Total Standard Deviation in ln(k): 52.978678098690516
""",
)

entry(
    index = 50,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br",
    kinetics = ArrheniusBM(A=(2.25522e+11,'m^3/(mol*s)'), n=-1.57963, w0=(285859,'J/mol'), E0=(53683.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.12677703481621838, var=13.875693129474286, Tref=1000.0, N=68, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br',), comment="""BM rule fitted to 68 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br
    Total Standard Deviation in ln(k): 7.786191759721522"""),
    rank = 11,
    shortDesc = """BM rule fitted to 68 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br
Total Standard Deviation in ln(k): 7.786191759721522""",
    longDesc = 
"""
BM rule fitted to 68 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br
Total Standard Deviation in ln(k): 7.786191759721522
""",
)

entry(
    index = 51,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(2.90511e-14,'m^3/(mol*s)'), n=5.48106, w0=(377500,'J/mol'), E0=(36043.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1616115377204448, var=6.013929974173905, Tref=1000.0, N=24, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl',), comment="""BM rule fitted to 24 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl
    Total Standard Deviation in ln(k): 5.322334196408053"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl
Total Standard Deviation in ln(k): 5.322334196408053""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl
Total Standard Deviation in ln(k): 5.322334196408053
""",
)

entry(
    index = 52,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(0.0139386,'m^3/(mol*s)'), n=2.28024, w0=(377500,'J/mol'), E0=(66776.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04018507836026131, var=9.539390765679677, Tref=1000.0, N=26, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl',), comment="""BM rule fitted to 26 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 6.292773082782009"""),
    rank = 11,
    shortDesc = """BM rule fitted to 26 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 6.292773082782009""",
    longDesc = 
"""
BM rule fitted to 26 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 6.292773082782009
""",
)

entry(
    index = 53,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_N-3BrCClFH->C_N-3BrClF->Br_3ClF->F",
    kinetics = ArrheniusBM(A=(1.86246e+07,'m^3/(mol*s)'), n=-0.196688, w0=(339270,'J/mol'), E0=(33927,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_N-3BrCClFH->C_N-3BrClF->Br_3ClF->F',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_N-3BrCClFH->C_N-3BrClF->Br_3ClF->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_N-3BrCClFH->C_N-3BrClF->Br_3ClF->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_N-3BrCClFH->C_N-3BrClF->Br_3ClF->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 54,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_N-3BrCClFH->C_N-3BrClF->Br_N-3ClF->F",
    kinetics = ArrheniusBM(A=(3.58875e+07,'m^3/(mol*s)'), n=-0.164171, w0=(334000,'J/mol'), E0=(33400,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_N-3BrCClFH->C_N-3BrClF->Br_N-3ClF->F',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_N-3BrCClFH->C_N-3BrClF->Br_N-3ClF->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_N-3BrCClFH->C_N-3BrClF->Br_N-3ClF->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_N-3BrCClFH->C_N-3BrClF->Br_N-3ClF->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 55,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C",
    kinetics = ArrheniusBM(A=(2.5907e+09,'m^3/(mol*s)'), n=-0.810196, w0=(377500,'J/mol'), E0=(76267.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07397224685800342, var=8.03386529555096, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C
    Total Standard Deviation in ln(k): 5.8680958503162"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C
Total Standard Deviation in ln(k): 5.8680958503162""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C
Total Standard Deviation in ln(k): 5.8680958503162
""",
)

entry(
    index = 56,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C",
    kinetics = ArrheniusBM(A=(6.21406e-11,'m^3/(mol*s)'), n=5.22271, w0=(377500,'J/mol'), E0=(28297.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.24692752722915787, var=3.971868155135798, Tref=1000.0, N=38, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C',), comment="""BM rule fitted to 38 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C
    Total Standard Deviation in ln(k): 4.615766976044839"""),
    rank = 11,
    shortDesc = """BM rule fitted to 38 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C
Total Standard Deviation in ln(k): 4.615766976044839""",
    longDesc = 
"""
BM rule fitted to 38 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C
Total Standard Deviation in ln(k): 4.615766976044839
""",
)

entry(
    index = 57,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.26162e-17,'m^3/(mol*s)'), n=7.24459, w0=(377500,'J/mol'), E0=(5968.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.5701002496100095, var=4.156874659324315, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 5.519749758383643"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 5.519749758383643""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 5.519749758383643
""",
)

entry(
    index = 58,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(50.0158,'m^3/(mol*s)'), n=1.87664, w0=(377500,'J/mol'), E0=(69121.7,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 59,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(46.4852,'m^3/(mol*s)'), n=1.87563, w0=(377500,'J/mol'), E0=(70843.6,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 60,
    label = "Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClFO->O_N-1BrClF->Br_1ClF->F",
    kinetics = ArrheniusBM(A=(1.7e+07,'m^3/(mol*s)'), n=0, w0=(339270,'J/mol'), E0=(33927,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClFO->O_N-1BrClF->Br_1ClF->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClFO->O_N-1BrClF->Br_1ClF->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClFO->O_N-1BrClF->Br_1ClF->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClFO->O_N-1BrClF->Br_1ClF->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 61,
    label = "Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClFO->O_N-1BrClF->Br_N-1ClF->F",
    kinetics = ArrheniusBM(A=(4.295e+07,'m^3/(mol*s)'), n=0, w0=(334000,'J/mol'), E0=(33400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClFO->O_N-1BrClF->Br_N-1ClF->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClFO->O_N-1BrClF->Br_N-1ClF->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClFO->O_N-1BrClF->Br_N-1ClF->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClFO->O_N-1BrClF->Br_N-1ClF->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 62,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(5.75395e-06,'m^3/(mol*s)'), n=3.09898, w0=(327000,'J/mol'), E0=(51367.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.21694674621645255, var=6.411095723978784, Tref=1000.0, N=29, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl',), comment="""BM rule fitted to 29 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl
    Total Standard Deviation in ln(k): 5.6211099371306705"""),
    rank = 11,
    shortDesc = """BM rule fitted to 29 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl
Total Standard Deviation in ln(k): 5.6211099371306705""",
    longDesc = 
"""
BM rule fitted to 29 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl
Total Standard Deviation in ln(k): 5.6211099371306705
""",
)

entry(
    index = 63,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(5.68637e+10,'m^3/(mol*s)'), n=-1.31755, w0=(326191,'J/mol'), E0=(82673.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.12769416426492586, var=7.080575520905949, Tref=1000.0, N=34, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl',), comment="""BM rule fitted to 34 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 5.655309510135193"""),
    rank = 11,
    shortDesc = """BM rule fitted to 34 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 5.655309510135193""",
    longDesc = 
"""
BM rule fitted to 34 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 5.655309510135193
""",
)

entry(
    index = 64,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R",
    kinetics = ArrheniusBM(A=(8.6586e+26,'m^3/(mol*s)'), n=-5.95084, w0=(305609,'J/mol'), E0=(97010.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.3874078380330987, var=12.558320439978212, Tref=1000.0, N=79, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R',), comment="""BM rule fitted to 79 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R
    Total Standard Deviation in ln(k): 8.077710690256563"""),
    rank = 11,
    shortDesc = """BM rule fitted to 79 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 8.077710690256563""",
    longDesc = 
"""
BM rule fitted to 79 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 8.077710690256563
""",
)

entry(
    index = 65,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_3CClFO->O",
    kinetics = ArrheniusBM(A=(10.5404,'m^3/(mol*s)'), n=2.14943, w0=(299500,'J/mol'), E0=(69107.5,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_3CClFO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_3CClFO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_3CClFO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_3CClFO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 66,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_N-3CClFO->O",
    kinetics = ArrheniusBM(A=(7.50584e+10,'m^3/(mol*s)'), n=-1.0283, w0=(283500,'J/mol'), E0=(48808.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.330063467427867e-15, var=0.19952571495078422, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_N-3CClFO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_N-3CClFO->O
    Total Standard Deviation in ln(k): 0.8954811065402019"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_N-3CClFO->O
Total Standard Deviation in ln(k): 0.8954811065402019""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_N-3CClFO->O
Total Standard Deviation in ln(k): 0.8954811065402019
""",
)

entry(
    index = 67,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_3CClFO->C",
    kinetics = ArrheniusBM(A=(2.09006e+21,'m^3/(mol*s)'), n=-4.10814, w0=(327000,'J/mol'), E0=(106777,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.3984396658087612, var=8.026128845913888, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_3CClFO->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_3CClFO->C
    Total Standard Deviation in ln(k): 6.68060402348377"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_3CClFO->C
Total Standard Deviation in ln(k): 6.68060402348377""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_3CClFO->C
Total Standard Deviation in ln(k): 6.68060402348377
""",
)

entry(
    index = 68,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_N-3CClFO->C",
    kinetics = ArrheniusBM(A=(1.78753e+42,'m^3/(mol*s)'), n=-10.3158, w0=(299500,'J/mol'), E0=(125533,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.8139111089222729, var=15.814800700673798, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_N-3CClFO->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_N-3CClFO->C
    Total Standard Deviation in ln(k): 10.01739857463312"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_N-3CClFO->C
Total Standard Deviation in ln(k): 10.01739857463312""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_N-3CClFO->C
Total Standard Deviation in ln(k): 10.01739857463312
""",
)

entry(
    index = 69,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_4R!H->O",
    kinetics = ArrheniusBM(A=(1.49643e+06,'m^3/(mol*s)'), n=0.37083, w0=(266667,'J/mol'), E0=(26666.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05149343949476097, var=19.136771886014984, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_4R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_4R!H->O
    Total Standard Deviation in ln(k): 8.899213623522808"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_4R!H->O
Total Standard Deviation in ln(k): 8.899213623522808""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_4R!H->O
Total Standard Deviation in ln(k): 8.899213623522808
""",
)

entry(
    index = 70,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(0.00388211,'m^3/(mol*s)'), n=2.85277, w0=(272000,'J/mol'), E0=(32134.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04589669828831547, var=1.4469474369311661, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O
    Total Standard Deviation in ln(k): 2.5267966852411075"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O
Total Standard Deviation in ln(k): 2.5267966852411075""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O
Total Standard Deviation in ln(k): 2.5267966852411075
""",
)

entry(
    index = 71,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_1BrClFO->F",
    kinetics = ArrheniusBM(A=(2.08327e+15,'m^3/(mol*s)'), n=-2.70406, w0=(261270,'J/mol'), E0=(45238.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.20101143674631483, var=65.21747732091801, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_1BrClFO->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_1BrClFO->F
    Total Standard Deviation in ln(k): 16.694760798983896"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_1BrClFO->F
Total Standard Deviation in ln(k): 16.694760798983896""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_1BrClFO->F
Total Standard Deviation in ln(k): 16.694760798983896
""",
)

entry(
    index = 72,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F",
    kinetics = ArrheniusBM(A=(53.7105,'m^3/(mol*s)'), n=1.50696, w0=(265108,'J/mol'), E0=(15071.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.024908445415280887, var=1.4014817984960566, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F',), comment="""BM rule fitted to 17 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F
    Total Standard Deviation in ln(k): 2.4358735473729602"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F
Total Standard Deviation in ln(k): 2.4358735473729602""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F
Total Standard Deviation in ln(k): 2.4358735473729602
""",
)

entry(
    index = 73,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_1BrClFO->Br_3BrCClF->C",
    kinetics = ArrheniusBM(A=(9.46237e-07,'m^3/(mol*s)'), n=1.82842, w0=(272920,'J/mol'), E0=(-20203.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.1412920824242747, var=1532.5751428575854, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_1BrClFO->Br_3BrCClF->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_1BrClFO->Br_3BrCClF->C
    Total Standard Deviation in ln(k): 81.3491734126974"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_1BrClFO->Br_3BrCClF->C
Total Standard Deviation in ln(k): 81.3491734126974""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_1BrClFO->Br_3BrCClF->C
Total Standard Deviation in ln(k): 81.3491734126974
""",
)

entry(
    index = 74,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_1BrClFO->Br_N-3BrCClF->C",
    kinetics = ArrheniusBM(A=(8.7e+06,'m^3/(mol*s)'), n=0, w0=(229420,'J/mol'), E0=(6670.89,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_1BrClFO->Br_N-3BrCClF->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_1BrClFO->Br_N-3BrCClF->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_1BrClFO->Br_N-3BrCClF->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_1BrClFO->Br_N-3BrCClF->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 75,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0",
    kinetics = ArrheniusBM(A=(8456.36,'m^3/(mol*s)'), n=0.6253, w0=(284229,'J/mol'), E0=(26949.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05662156793134671, var=15.214587388149534, Tref=1000.0, N=49, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0',), comment="""BM rule fitted to 49 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0
    Total Standard Deviation in ln(k): 7.961910997205746"""),
    rank = 11,
    shortDesc = """BM rule fitted to 49 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0
Total Standard Deviation in ln(k): 7.961910997205746""",
    longDesc = 
"""
BM rule fitted to 49 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0
Total Standard Deviation in ln(k): 7.961910997205746
""",
)

entry(
    index = 76,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0",
    kinetics = ArrheniusBM(A=(2.21865e+13,'m^3/(mol*s)'), n=-2.23185, w0=(290063,'J/mol'), E0=(67127.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.16535174583102832, var=13.419193362735472, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0',), comment="""BM rule fitted to 19 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0
    Total Standard Deviation in ln(k): 7.759245724217835"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0
Total Standard Deviation in ln(k): 7.759245724217835""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0
Total Standard Deviation in ln(k): 7.759245724217835
""",
)

entry(
    index = 77,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.34198e-14,'m^3/(mol*s)'), n=5.46341, w0=(377500,'J/mol'), E0=(35251.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1804115585117187, var=6.797979744448016, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R',), comment="""BM rule fitted to 21 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R
    Total Standard Deviation in ln(k): 5.6802282439464795"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 5.6802282439464795""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 5.6802282439464795
""",
)

entry(
    index = 78,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C",
    kinetics = ArrheniusBM(A=(823037,'m^3/(mol*s)'), n=-0.45359, w0=(377500,'J/mol'), E0=(55468.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 79,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C",
    kinetics = ArrheniusBM(A=(0.0286357,'m^3/(mol*s)'), n=2.20419, w0=(377500,'J/mol'), E0=(68608.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.029955383612472603, var=9.936241796352265, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C',), comment="""BM rule fitted to 25 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C
    Total Standard Deviation in ln(k): 6.39455156715808"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C
Total Standard Deviation in ln(k): 6.39455156715808""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C
Total Standard Deviation in ln(k): 6.39455156715808
""",
)

entry(
    index = 80,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C",
    kinetics = ArrheniusBM(A=(123.645,'m^3/(mol*s)'), n=1.29759, w0=(377500,'J/mol'), E0=(61557,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.48104404972789094, var=13.425150317275554, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C
    Total Standard Deviation in ln(k): 8.554072288585735"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C
Total Standard Deviation in ln(k): 8.554072288585735""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C
Total Standard Deviation in ln(k): 8.554072288585735
""",
)

entry(
    index = 81,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(5.0567e+10,'m^3/(mol*s)'), n=-1.07381, w0=(377500,'J/mol'), E0=(77038.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.08306123261095291, var=4.744624423151358, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_N-4R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_N-4R!H->C
    Total Standard Deviation in ln(k): 4.575442346625547"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_N-4R!H->C
Total Standard Deviation in ln(k): 4.575442346625547""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_N-4R!H->C
Total Standard Deviation in ln(k): 4.575442346625547
""",
)

entry(
    index = 82,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F",
    kinetics = ArrheniusBM(A=(2.27609e+08,'m^3/(mol*s)'), n=-0.336794, w0=(377500,'J/mol'), E0=(87892.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.016757454008488566, var=17.28831596108248, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F
    Total Standard Deviation in ln(k): 8.377636383636345"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F
Total Standard Deviation in ln(k): 8.377636383636345""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F
Total Standard Deviation in ln(k): 8.377636383636345
""",
)

entry(
    index = 83,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F",
    kinetics = ArrheniusBM(A=(1.1276e-10,'m^3/(mol*s)'), n=5.16816, w0=(377500,'J/mol'), E0=(23389.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.23309112250619993, var=1.4409769407702624, Tref=1000.0, N=31, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F',), comment="""BM rule fitted to 31 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F
    Total Standard Deviation in ln(k): 2.992154085974135"""),
    rank = 11,
    shortDesc = """BM rule fitted to 31 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F
Total Standard Deviation in ln(k): 2.992154085974135""",
    longDesc = 
"""
BM rule fitted to 31 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F
Total Standard Deviation in ln(k): 2.992154085974135
""",
)

entry(
    index = 84,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Ext-1C-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(2.4575e-21,'m^3/(mol*s)'), n=8.34648, w0=(377500,'J/mol'), E0=(2887.79,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06924398405310164, var=14.213536654906394, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Ext-1C-R_4R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Ext-1C-R_4R!H->Cl
    Total Standard Deviation in ln(k): 7.732000373106373"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Ext-1C-R_4R!H->Cl
Total Standard Deviation in ln(k): 7.732000373106373""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Ext-1C-R_4R!H->Cl
Total Standard Deviation in ln(k): 7.732000373106373
""",
)

entry(
    index = 85,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Ext-1C-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(882.183,'m^3/(mol*s)'), n=1.42825, w0=(377500,'J/mol'), E0=(45417.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0022107214661341293, var=0.2475890620304536, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Ext-1C-R_N-4R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Ext-1C-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 1.0030771140320058"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Ext-1C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 1.0030771140320058""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Ext-1C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 1.0030771140320058
""",
)

entry(
    index = 86,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(8.16443e+06,'m^3/(mol*s)'), n=-0.631568, w0=(327000,'J/mol'), E0=(70174.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00014504756242999777, var=3.894052879547799, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 3.9563792784995084"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 3.9563792784995084""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 3.9563792784995084
""",
)

entry(
    index = 87,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R",
    kinetics = ArrheniusBM(A=(9.39076e-28,'m^3/(mol*s)'), n=9.73356, w0=(327000,'J/mol'), E0=(-7165.12,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4556377784173475, var=6.2290552600627125, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R',), comment="""BM rule fitted to 14 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R
    Total Standard Deviation in ln(k): 6.148251453909567"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R
Total Standard Deviation in ln(k): 6.148251453909567""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R
Total Standard Deviation in ln(k): 6.148251453909567
""",
)

entry(
    index = 88,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(0.000468906,'m^3/(mol*s)'), n=2.77279, w0=(327000,'J/mol'), E0=(69382.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.007450415050835228, var=5.356006145246326, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 4.658287404710733"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 4.658287404710733""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 4.658287404710733
""",
)

entry(
    index = 89,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C",
    kinetics = ArrheniusBM(A=(110.442,'m^3/(mol*s)'), n=1.25087, w0=(327000,'J/mol'), E0=(60406.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.07029504948634763, var=6.587260413533573, Tref=1000.0, N=27, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C',), comment="""BM rule fitted to 27 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C
    Total Standard Deviation in ln(k): 5.321905374319842"""),
    rank = 11,
    shortDesc = """BM rule fitted to 27 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C
Total Standard Deviation in ln(k): 5.321905374319842""",
    longDesc = 
"""
BM rule fitted to 27 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C
Total Standard Deviation in ln(k): 5.321905374319842
""",
)

entry(
    index = 90,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_N-3CClFO->C",
    kinetics = ArrheniusBM(A=(0.00010035,'m^3/(mol*s)'), n=3.57133, w0=(299500,'J/mol'), E0=(29950,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_N-3CClFO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_N-3CClFO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_N-3CClFO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_N-3CClFO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 91,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(5.86057e+24,'m^3/(mol*s)'), n=-5.35677, w0=(304456,'J/mol'), E0=(88483.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.34759734517753194, var=12.953012745959933, Tref=1000.0, N=50, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl',), comment="""BM rule fitted to 50 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl
    Total Standard Deviation in ln(k): 8.088460681021626"""),
    rank = 11,
    shortDesc = """BM rule fitted to 50 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl
Total Standard Deviation in ln(k): 8.088460681021626""",
    longDesc = 
"""
BM rule fitted to 50 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl
Total Standard Deviation in ln(k): 8.088460681021626
""",
)

entry(
    index = 92,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(3.83681e+30,'m^3/(mol*s)'), n=-6.94734, w0=(307596,'J/mol'), E0=(111676,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.45276568821571955, var=13.094080918362193, Tref=1000.0, N=29, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl',), comment="""BM rule fitted to 29 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 8.391885325257078"""),
    rank = 11,
    shortDesc = """BM rule fitted to 29 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 8.391885325257078""",
    longDesc = 
"""
BM rule fitted to 29 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 8.391885325257078
""",
)

entry(
    index = 93,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_3CClFO->C_Ext-1C-R_Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(1.13946e+21,'m^3/(mol*s)'), n=-4.04791, w0=(327000,'J/mol'), E0=(106860,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.37489169118768667, var=10.618664007825155, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_3CClFO->C_Ext-1C-R_Sp-4R!H-1C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_3CClFO->C_Ext-1C-R_Sp-4R!H-1C
    Total Standard Deviation in ln(k): 7.4746271055215985"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_3CClFO->C_Ext-1C-R_Sp-4R!H-1C
Total Standard Deviation in ln(k): 7.4746271055215985""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_3CClFO->C_Ext-1C-R_Sp-4R!H-1C
Total Standard Deviation in ln(k): 7.4746271055215985
""",
)

entry(
    index = 94,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_3CClFO->C_Ext-1C-R_N-Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(0.171123,'m^3/(mol*s)'), n=2.55484, w0=(327000,'J/mol'), E0=(52803.6,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_3CClFO->C_Ext-1C-R_N-Sp-4R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_3CClFO->C_Ext-1C-R_N-Sp-4R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_3CClFO->C_Ext-1C-R_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_3CClFO->C_Ext-1C-R_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 95,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_N-3CClFO->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.51966e+14,'m^3/(mol*s)'), n=-2.13937, w0=(299500,'J/mol'), E0=(7389.03,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.6795243041270407, var=18.39783655042363, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_N-3CClFO->C_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_N-3CClFO->C_Ext-1C-R
    Total Standard Deviation in ln(k): 10.306197387100978"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_N-3CClFO->C_Ext-1C-R
Total Standard Deviation in ln(k): 10.306197387100978""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_N-3CClFO->C_Ext-1C-R
Total Standard Deviation in ln(k): 10.306197387100978
""",
)

entry(
    index = 96,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_4R!H->O_1BrClFO-u0",
    kinetics = ArrheniusBM(A=(5.42459e+07,'m^3/(mol*s)'), n=0.0480137, w0=(264000,'J/mol'), E0=(26400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2455966319345321, var=23.541474785982114, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_4R!H->O_1BrClFO-u0',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_4R!H->O_1BrClFO-u0
    Total Standard Deviation in ln(k): 10.343962889079577"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_4R!H->O_1BrClFO-u0
Total Standard Deviation in ln(k): 10.343962889079577""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_4R!H->O_1BrClFO-u0
Total Standard Deviation in ln(k): 10.343962889079577
""",
)

entry(
    index = 97,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_4R!H->O_N-1BrClFO-u0",
    kinetics = ArrheniusBM(A=(6.84623e+07,'m^3/(mol*s)'), n=-0.410194, w0=(272000,'J/mol'), E0=(27200,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_4R!H->O_N-1BrClFO-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_4R!H->O_N-1BrClFO-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_4R!H->O_N-1BrClFO-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_4R!H->O_N-1BrClFO-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 98,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O_Ext-4BrCClFINPSSi-R",
    kinetics = ArrheniusBM(A=(0.000153612,'m^3/(mol*s)'), n=3.32595, w0=(272000,'J/mol'), E0=(27200,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06393013539151016, var=3.8677789223461145, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O_Ext-4BrCClFINPSSi-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O_Ext-4BrCClFINPSSi-R
    Total Standard Deviation in ln(k): 4.103274716453381"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O_Ext-4BrCClFINPSSi-R
Total Standard Deviation in ln(k): 4.103274716453381""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O_Ext-4BrCClFINPSSi-R
Total Standard Deviation in ln(k): 4.103274716453381
""",
)

entry(
    index = 99,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O_4BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(14.9375,'m^3/(mol*s)'), n=1.73494, w0=(272000,'J/mol'), E0=(36835.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.21026825362471163, var=0.4178948848535683, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O_4BrCClFINPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O_4BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 1.8242689719039558"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O_4BrCClFINPSSi->C
Total Standard Deviation in ln(k): 1.8242689719039558""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O_4BrCClFINPSSi->C
Total Standard Deviation in ln(k): 1.8242689719039558
""",
)

entry(
    index = 100,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O_N-4BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(0.00123036,'m^3/(mol*s)'), n=2.89569, w0=(272000,'J/mol'), E0=(19743.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O_N-4BrCClFINPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O_N-4BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O_N-4BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O_N-4BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 101,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_1BrClFO->F_3O-u1",
    kinetics = ArrheniusBM(A=(770603,'m^3/(mol*s)'), n=0.19732, w0=(261270,'J/mol'), E0=(6019.92,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_1BrClFO->F_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_1BrClFO->F_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_1BrClFO->F_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_1BrClFO->F_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 102,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_1BrClFO->F_N-3O-u1",
    kinetics = ArrheniusBM(A=(500000,'m^3/(mol*s)'), n=0, w0=(261270,'J/mol'), E0=(40550.4,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_1BrClFO->F_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_1BrClFO->F_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_1BrClFO->F_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_1BrClFO->F_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 103,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_1BrClO->Cl",
    kinetics = ArrheniusBM(A=(100.484,'m^3/(mol*s)'), n=1.27365, w0=(256000,'J/mol'), E0=(433.129,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.03821208298272079, var=1.2326126643078588, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_1BrClO->Cl',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_1BrClO->Cl
    Total Standard Deviation in ln(k): 2.321729099718136"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_1BrClO->Cl
Total Standard Deviation in ln(k): 2.321729099718136""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_1BrClO->Cl
Total Standard Deviation in ln(k): 2.321729099718136
""",
)

entry(
    index = 104,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl",
    kinetics = ArrheniusBM(A=(5.83133,'m^3/(mol*s)'), n=1.83994, w0=(267911,'J/mol'), E0=(17593.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.02737425615541584, var=1.5911187956102155, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl
    Total Standard Deviation in ln(k): 2.5975434929411394"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl
Total Standard Deviation in ln(k): 2.5975434929411394""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl
Total Standard Deviation in ln(k): 2.5975434929411394
""",
)

entry(
    index = 105,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_1BrClFO->Br_3BrCClF->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1968.51,'m^3/(mol*s)'), n=0.908851, w0=(272920,'J/mol'), E0=(27292,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_1BrClFO->Br_3BrCClF->C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_1BrClFO->Br_3BrCClF->C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_1BrClFO->Br_3BrCClF->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_1BrClFO->Br_3BrCClF->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 106,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R",
    kinetics = ArrheniusBM(A=(2.74515e+19,'m^3/(mol*s)'), n=-4.03071, w0=(291213,'J/mol'), E0=(74519.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2955667982030343, var=6.657022525536846, Tref=1000.0, N=38, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R',), comment="""BM rule fitted to 38 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R
    Total Standard Deviation in ln(k): 5.915088500489784"""),
    rank = 11,
    shortDesc = """BM rule fitted to 38 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R
Total Standard Deviation in ln(k): 5.915088500489784""",
    longDesc = 
"""
BM rule fitted to 38 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R
Total Standard Deviation in ln(k): 5.915088500489784
""",
)

entry(
    index = 107,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_3BrCClF->C",
    kinetics = ArrheniusBM(A=(7.82607,'m^3/(mol*s)'), n=1.72648, w0=(288833,'J/mol'), E0=(16447.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.14443867296820748, var=0.338273074773904, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_3BrCClF->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_3BrCClF->C
    Total Standard Deviation in ln(k): 1.528890175069824"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_3BrCClF->C
Total Standard Deviation in ln(k): 1.528890175069824""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_3BrCClF->C
Total Standard Deviation in ln(k): 1.528890175069824
""",
)

entry(
    index = 108,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C",
    kinetics = ArrheniusBM(A=(7.5813e+12,'m^3/(mol*s)'), n=-1.62732, w0=(249331,'J/mol'), E0=(22541.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.10286379935271425, var=3.887674943543769, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C
    Total Standard Deviation in ln(k): 4.211225556227606"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C
Total Standard Deviation in ln(k): 4.211225556227606""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C
Total Standard Deviation in ln(k): 4.211225556227606
""",
)

entry(
    index = 109,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1",
    kinetics = ArrheniusBM(A=(4334.15,'m^3/(mol*s)'), n=0.573738, w0=(288952,'J/mol'), E0=(44090.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0061808206836900925, var=14.968346924096888, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1',), comment="""BM rule fitted to 17 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1
    Total Standard Deviation in ln(k): 7.771638803727038"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1
Total Standard Deviation in ln(k): 7.771638803727038""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1
Total Standard Deviation in ln(k): 7.771638803727038
""",
)

entry(
    index = 110,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_N-3BrCClF-u1",
    kinetics = ArrheniusBM(A=(0.172496,'m^3/(mol*s)'), n=2.38833, w0=(299500,'J/mol'), E0=(29950,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.3222723629768012, var=0.811624612398152, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_N-3BrCClF-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_N-3BrCClF-u1
    Total Standard Deviation in ln(k): 2.615799617096273"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_N-3BrCClF-u1
Total Standard Deviation in ln(k): 2.615799617096273""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_N-3BrCClF-u1
Total Standard Deviation in ln(k): 2.615799617096273
""",
)

entry(
    index = 111,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(1.00042e-13,'m^3/(mol*s)'), n=5.1956, w0=(377500,'J/mol'), E0=(-9062.12,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.23062320779638043, var=1.896647565230179, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl',), comment="""BM rule fitted to 9 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl
    Total Standard Deviation in ln(k): 3.340352953910886"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl
Total Standard Deviation in ln(k): 3.340352953910886""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl
Total Standard Deviation in ln(k): 3.340352953910886
""",
)

entry(
    index = 112,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(1.81599e+08,'m^3/(mol*s)'), n=-0.890841, w0=(377500,'J/mol'), E0=(89993.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.13822719298816089, var=7.878473041231882, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl',), comment="""BM rule fitted to 12 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 5.974318768904033"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 5.974318768904033""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 5.974318768904033
""",
)

entry(
    index = 113,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(2.50189e-14,'m^3/(mol*s)'), n=5.71822, w0=(377500,'J/mol'), E0=(47490.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2292001092309166, var=14.878882229263493, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R',), comment="""BM rule fitted to 11 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 8.308775193256901"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 8.308775193256901""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 8.308775193256901
""",
)

entry(
    index = 114,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_4BrCFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(1110.76,'m^3/(mol*s)'), n=0.908507, w0=(377500,'J/mol'), E0=(98353.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_4BrCFINOPSSi->Br',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_4BrCFINOPSSi->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_4BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_4BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 115,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(4.02421e+10,'m^3/(mol*s)'), n=-1.35519, w0=(377500,'J/mol'), E0=(87407.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.15694925755177874, var=7.2921976976428615, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br',), comment="""BM rule fitted to 13 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br
    Total Standard Deviation in ln(k): 5.807945404879668"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 5.807945404879668""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 5.807945404879668
""",
)

entry(
    index = 116,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(5.29649e-38,'m^3/(mol*s)'), n=12.7904, w0=(377500,'J/mol'), E0=(-20637.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.347632557405025, var=33.37237304328049, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 17.479693532439395"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 17.479693532439395""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 17.479693532439395
""",
)

entry(
    index = 117,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(1.3076e+07,'m^3/(mol*s)'), n=-0.101081, w0=(377500,'J/mol'), E0=(79172.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.09464690228688659, var=10.493612523838511, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C_Ext-4C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 6.731914204486714"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 6.731914204486714""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 6.731914204486714
""",
)

entry(
    index = 118,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_N-4R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.38812e+17,'m^3/(mol*s)'), n=-3.07858, w0=(377500,'J/mol'), E0=(90145.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.010861323946090667, var=7.423365314706921, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_N-4R!H->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_N-4R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 5.489361575739411"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_N-4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 5.489361575739411""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_N-4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 5.489361575739411
""",
)

entry(
    index = 119,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.80207e+07,'m^3/(mol*s)'), n=-0.105819, w0=(377500,'J/mol'), E0=(94413.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.27821043997144973, var=14.324989666921656, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R
    Total Standard Deviation in ln(k): 8.286616318156316"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R
Total Standard Deviation in ln(k): 8.286616318156316""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R
Total Standard Deviation in ln(k): 8.286616318156316
""",
)

entry(
    index = 120,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C",
    kinetics = ArrheniusBM(A=(1.40769e-10,'m^3/(mol*s)'), n=5.13766, w0=(377500,'J/mol'), E0=(22333.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.22846920999470594, var=1.4672823742208287, Tref=1000.0, N=30, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C',), comment="""BM rule fitted to 30 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C
    Total Standard Deviation in ln(k): 3.0024075419440868"""),
    rank = 11,
    shortDesc = """BM rule fitted to 30 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C
Total Standard Deviation in ln(k): 3.0024075419440868""",
    longDesc = 
"""
BM rule fitted to 30 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C
Total Standard Deviation in ln(k): 3.0024075419440868
""",
)

entry(
    index = 121,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_N-Sp-4BrCClO-1C",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(377500,'J/mol'), E0=(54877.5,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_N-Sp-4BrCClO-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_N-Sp-4BrCClO-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_N-Sp-4BrCClO-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_N-Sp-4BrCClO-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 122,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Ext-1C-R_4R!H->Cl_5R!H->C",
    kinetics = ArrheniusBM(A=(23.5467,'m^3/(mol*s)'), n=1.8421, w0=(377500,'J/mol'), E0=(70516.5,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Ext-1C-R_4R!H->Cl_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Ext-1C-R_4R!H->Cl_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Ext-1C-R_4R!H->Cl_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Ext-1C-R_4R!H->Cl_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 123,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Ext-1C-R_4R!H->Cl_N-5R!H->C",
    kinetics = ArrheniusBM(A=(36.3215,'m^3/(mol*s)'), n=1.83646, w0=(377500,'J/mol'), E0=(51038.8,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Ext-1C-R_4R!H->Cl_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Ext-1C-R_4R!H->Cl_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Ext-1C-R_4R!H->Cl_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Ext-1C-R_4R!H->Cl_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 124,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_4CO->C",
    kinetics = ArrheniusBM(A=(34.0466,'m^3/(mol*s)'), n=1.832, w0=(377500,'J/mol'), E0=(40068.1,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_4CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_4CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_4CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_4CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 125,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4CO->C",
    kinetics = ArrheniusBM(A=(82.3604,'m^3/(mol*s)'), n=1.89796, w0=(377500,'J/mol'), E0=(54231.8,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 126,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_5R!H->Br",
    kinetics = ArrheniusBM(A=(190000,'m^3/(mol*s)'), n=0, w0=(327000,'J/mol'), E0=(44132.4,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_5R!H->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_5R!H->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_5R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_5R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 127,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br",
    kinetics = ArrheniusBM(A=(3.39155e+10,'m^3/(mol*s)'), n=-1.71326, w0=(327000,'J/mol'), E0=(79836.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.08036426153610884, var=2.485353260578186, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br
    Total Standard Deviation in ln(k): 3.3623857471717353"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br
Total Standard Deviation in ln(k): 3.3623857471717353""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br
Total Standard Deviation in ln(k): 3.3623857471717353
""",
)

entry(
    index = 128,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R",
    kinetics = ArrheniusBM(A=(1.60861e-24,'m^3/(mol*s)'), n=8.48148, w0=(327000,'J/mol'), E0=(1363.89,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.037730654435693, var=19.091036956906233, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R
    Total Standard Deviation in ln(k): 13.879273618517212"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R
Total Standard Deviation in ln(k): 13.879273618517212""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R
Total Standard Deviation in ln(k): 13.879273618517212
""",
)

entry(
    index = 129,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Sp-5R!H-3CClFO",
    kinetics = ArrheniusBM(A=(1.37748,'m^3/(mol*s)'), n=1.9862, w0=(327000,'J/mol'), E0=(77057.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0298585448195696, var=2.498804733445619, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Sp-5R!H-3CClFO',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Sp-5R!H-3CClFO
    Total Standard Deviation in ln(k): 3.244028111011072"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Sp-5R!H-3CClFO
Total Standard Deviation in ln(k): 3.244028111011072""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Sp-5R!H-3CClFO
Total Standard Deviation in ln(k): 3.244028111011072
""",
)

entry(
    index = 130,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_N-Sp-5R!H-3CClFO",
    kinetics = ArrheniusBM(A=(0.0181681,'m^3/(mol*s)'), n=2.73798, w0=(327000,'J/mol'), E0=(65050.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0067194163353994215, var=4.173326487825017, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_N-Sp-5R!H-3CClFO',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_N-Sp-5R!H-3CClFO
    Total Standard Deviation in ln(k): 4.112300347888221"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_N-Sp-5R!H-3CClFO
Total Standard Deviation in ln(k): 4.112300347888221""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_N-Sp-5R!H-3CClFO
Total Standard Deviation in ln(k): 4.112300347888221
""",
)

entry(
    index = 131,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-3CClFO-R",
    kinetics = ArrheniusBM(A=(0.00669369,'m^3/(mol*s)'), n=2.27982, w0=(327000,'J/mol'), E0=(67886.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.001435242633319624, var=8.203411902057832, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-3CClFO-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-3CClFO-R
    Total Standard Deviation in ln(k): 5.745487945317708"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-3CClFO-R
Total Standard Deviation in ln(k): 5.745487945317708""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-3CClFO-R
Total Standard Deviation in ln(k): 5.745487945317708
""",
)

entry(
    index = 132,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(5.76571e-05,'m^3/(mol*s)'), n=3.24279, w0=(327000,'J/mol'), E0=(74347.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 133,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C",
    kinetics = ArrheniusBM(A=(7.20383e-20,'m^3/(mol*s)'), n=7.46605, w0=(327000,'J/mol'), E0=(10896.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.33903742858241803, var=4.615311646559138, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C',), comment="""BM rule fitted to 22 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C
    Total Standard Deviation in ln(k): 5.158680612237643"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 5.158680612237643""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 5.158680612237643
""",
)

entry(
    index = 134,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_N-Sp-4BrCFINOPSSi-3C",
    kinetics = ArrheniusBM(A=(4.31181e-09,'m^3/(mol*s)'), n=4.51138, w0=(327000,'J/mol'), E0=(23229.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5203014658373865, var=19.2097186312958, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_N-Sp-4BrCFINOPSSi-3C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_N-Sp-4BrCFINOPSSi-3C
    Total Standard Deviation in ln(k): 10.093822038700425"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_N-Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 10.093822038700425""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_N-Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 10.093822038700425
""",
)

entry(
    index = 135,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O",
    kinetics = ArrheniusBM(A=(9.72151e+18,'m^3/(mol*s)'), n=-3.64654, w0=(299500,'J/mol'), E0=(68514.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2672813145824368, var=6.819894145331023, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O',), comment="""BM rule fitted to 21 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O
    Total Standard Deviation in ln(k): 5.90691212086068"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O
Total Standard Deviation in ln(k): 5.90691212086068""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O
Total Standard Deviation in ln(k): 5.90691212086068
""",
)

entry(
    index = 136,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O",
    kinetics = ArrheniusBM(A=(1.40314e+26,'m^3/(mol*s)'), n=-5.76876, w0=(308045,'J/mol'), E0=(96525,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.3537161621821146, var=17.759453273349035, Tref=1000.0, N=29, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O',), comment="""BM rule fitted to 29 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O
    Total Standard Deviation in ln(k): 9.337081891843106"""),
    rank = 11,
    shortDesc = """BM rule fitted to 29 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O
Total Standard Deviation in ln(k): 9.337081891843106""",
    longDesc = 
"""
BM rule fitted to 29 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O
Total Standard Deviation in ln(k): 9.337081891843106
""",
)

entry(
    index = 137,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C",
    kinetics = ArrheniusBM(A=(725.803,'m^3/(mol*s)'), n=1.0218, w0=(327000,'J/mol'), E0=(54101.3,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 138,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C",
    kinetics = ArrheniusBM(A=(7.95168e+31,'m^3/(mol*s)'), n=-7.33004, w0=(306902,'J/mol'), E0=(114116,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.472101567624727, var=13.326400681389075, Tref=1000.0, N=28, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C',), comment="""BM rule fitted to 28 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C
    Total Standard Deviation in ln(k): 8.504539007342133"""),
    rank = 11,
    shortDesc = """BM rule fitted to 28 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C
Total Standard Deviation in ln(k): 8.504539007342133""",
    longDesc = 
"""
BM rule fitted to 28 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C
Total Standard Deviation in ln(k): 8.504539007342133
""",
)

entry(
    index = 139,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_3CClFO->C_Ext-1C-R_Sp-4R!H-1C_4R!H->O",
    kinetics = ArrheniusBM(A=(1.39543e+19,'m^3/(mol*s)'), n=-3.47206, w0=(327000,'J/mol'), E0=(91807.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.5352246413685504, var=11.15051032067538, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_3CClFO->C_Ext-1C-R_Sp-4R!H-1C_4R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_3CClFO->C_Ext-1C-R_Sp-4R!H-1C_4R!H->O
    Total Standard Deviation in ln(k): 8.03907305143576"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_3CClFO->C_Ext-1C-R_Sp-4R!H-1C_4R!H->O
Total Standard Deviation in ln(k): 8.03907305143576""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_3CClFO->C_Ext-1C-R_Sp-4R!H-1C_4R!H->O
Total Standard Deviation in ln(k): 8.03907305143576
""",
)

entry(
    index = 140,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_3CClFO->C_Ext-1C-R_Sp-4R!H-1C_N-4R!H->O",
    kinetics = ArrheniusBM(A=(86.872,'m^3/(mol*s)'), n=1.58191, w0=(327000,'J/mol'), E0=(83090.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.019437028169395205, var=22.281750390558173, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_3CClFO->C_Ext-1C-R_Sp-4R!H-1C_N-4R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_3CClFO->C_Ext-1C-R_Sp-4R!H-1C_N-4R!H->O
    Total Standard Deviation in ln(k): 9.511897801800835"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_3CClFO->C_Ext-1C-R_Sp-4R!H-1C_N-4R!H->O
Total Standard Deviation in ln(k): 9.511897801800835""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_3CClFO->C_Ext-1C-R_Sp-4R!H-1C_N-4R!H->O
Total Standard Deviation in ln(k): 9.511897801800835
""",
)

entry(
    index = 141,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_N-3CClFO->C_Ext-1C-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(157.231,'m^3/(mol*s)'), n=1.7152, w0=(299500,'J/mol'), E0=(57523.1,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_N-3CClFO->C_Ext-1C-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_N-3CClFO->C_Ext-1C-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_N-3CClFO->C_Ext-1C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_N-3CClFO->C_Ext-1C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 142,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_N-3CClFO->C_Ext-1C-R_3ClFO-u1",
    kinetics = ArrheniusBM(A=(0.977703,'m^3/(mol*s)'), n=2.24188, w0=(299500,'J/mol'), E0=(29950,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_N-3CClFO->C_Ext-1C-R_3ClFO-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_N-3CClFO->C_Ext-1C-R_3ClFO-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_N-3CClFO->C_Ext-1C-R_3ClFO-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_N-3CClFO->C_Ext-1C-R_3ClFO-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 143,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_N-3CClFO->C_Ext-1C-R_N-3ClFO-u1",
    kinetics = ArrheniusBM(A=(6.02711e+12,'m^3/(mol*s)'), n=-1.6274, w0=(299500,'J/mol'), E0=(29950,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.1436236221143194, var=4.026662798346816, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_N-3CClFO->C_Ext-1C-R_N-3ClFO-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_N-3CClFO->C_Ext-1C-R_N-3ClFO-u1
    Total Standard Deviation in ln(k): 9.408799922389525"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_N-3CClFO->C_Ext-1C-R_N-3ClFO-u1
Total Standard Deviation in ln(k): 9.408799922389525""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_N-3CClFO->C_Ext-1C-R_N-3ClFO-u1
Total Standard Deviation in ln(k): 9.408799922389525
""",
)

entry(
    index = 144,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_4R!H->O_1BrClFO-u0_1BrClFO->O",
    kinetics = ArrheniusBM(A=(3.47397e+06,'m^3/(mol*s)'), n=0.171533, w0=(272000,'J/mol'), E0=(27200,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_4R!H->O_1BrClFO-u0_1BrClFO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_4R!H->O_1BrClFO-u0_1BrClFO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_4R!H->O_1BrClFO-u0_1BrClFO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_4R!H->O_1BrClFO-u0_1BrClFO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 145,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_4R!H->O_1BrClFO-u0_N-1BrClFO->O",
    kinetics = ArrheniusBM(A=(3.1688e+07,'m^3/(mol*s)'), n=0.336335, w0=(256000,'J/mol'), E0=(25600,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_4R!H->O_1BrClFO-u0_N-1BrClFO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_4R!H->O_1BrClFO-u0_N-1BrClFO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_4R!H->O_1BrClFO-u0_N-1BrClFO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_4R!H->O_1BrClFO-u0_N-1BrClFO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 146,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi",
    kinetics = ArrheniusBM(A=(0.0853731,'m^3/(mol*s)'), n=2.28596, w0=(272000,'J/mol'), E0=(27200,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 147,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi",
    kinetics = ArrheniusBM(A=(0.0214236,'m^3/(mol*s)'), n=2.72353, w0=(272000,'J/mol'), E0=(27200,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.7890304190584024, var=1.5320421056338418, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi
    Total Standard Deviation in ln(k): 4.463863134150054"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi
Total Standard Deviation in ln(k): 4.463863134150054""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi
Total Standard Deviation in ln(k): 4.463863134150054
""",
)

entry(
    index = 148,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O_4BrCClFINPSSi->C_1BrClFO-u0",
    kinetics = ArrheniusBM(A=(0.000417933,'m^3/(mol*s)'), n=2.98801, w0=(272000,'J/mol'), E0=(21054.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O_4BrCClFINPSSi->C_1BrClFO-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O_4BrCClFINPSSi->C_1BrClFO-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O_4BrCClFINPSSi->C_1BrClFO-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O_4BrCClFINPSSi->C_1BrClFO-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 149,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O_4BrCClFINPSSi->C_N-1BrClFO-u0",
    kinetics = ArrheniusBM(A=(25.2691,'m^3/(mol*s)'), n=1.65303, w0=(272000,'J/mol'), E0=(35437.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O_4BrCClFINPSSi->C_N-1BrClFO-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O_4BrCClFINPSSi->C_N-1BrClFO-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O_4BrCClFINPSSi->C_N-1BrClFO-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O_4BrCClFINPSSi->C_N-1BrClFO-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 150,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_1BrClO->Cl_3O-u1",
    kinetics = ArrheniusBM(A=(8499.14,'m^3/(mol*s)'), n=0.730146, w0=(256000,'J/mol'), E0=(1475.47,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.26275138250443636, var=0.9043599506947635, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_1BrClO->Cl_3O-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_1BrClO->Cl_3O-u1
    Total Standard Deviation in ln(k): 2.5666391445849746"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_1BrClO->Cl_3O-u1
Total Standard Deviation in ln(k): 2.5666391445849746""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_1BrClO->Cl_3O-u1
Total Standard Deviation in ln(k): 2.5666391445849746
""",
)

entry(
    index = 151,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_1BrClO->Cl_N-3O-u1",
    kinetics = ArrheniusBM(A=(1.4223e+06,'m^3/(mol*s)'), n=0.0240137, w0=(256000,'J/mol'), E0=(21399,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.2212663242000096e-15, var=0.18300674264565733, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_1BrClO->Cl_N-3O-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_1BrClO->Cl_N-3O-u1
    Total Standard Deviation in ln(k): 0.8576113794309276"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_1BrClO->Cl_N-3O-u1
Total Standard Deviation in ln(k): 0.8576113794309276""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_1BrClO->Cl_N-3O-u1
Total Standard Deviation in ln(k): 0.8576113794309276
""",
)

entry(
    index = 152,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_3O-u1",
    kinetics = ArrheniusBM(A=(170.503,'m^3/(mol*s)'), n=1.29323, w0=(266684,'J/mol'), E0=(18772.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2522289953642745, var=3.5751154810753474, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_3O-u1',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_3O-u1
    Total Standard Deviation in ln(k): 4.424289423306565"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_3O-u1
Total Standard Deviation in ln(k): 4.424289423306565""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_3O-u1
Total Standard Deviation in ln(k): 4.424289423306565
""",
)

entry(
    index = 153,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_N-3O-u1",
    kinetics = ArrheniusBM(A=(0.983982,'m^3/(mol*s)'), n=2.13912, w0=(268678,'J/mol'), E0=(17677.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0039699020441198085, var=1.9545058077711839, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_N-3O-u1',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_N-3O-u1
    Total Standard Deviation in ln(k): 2.812667261781953"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_N-3O-u1
Total Standard Deviation in ln(k): 2.812667261781953""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_N-3O-u1
Total Standard Deviation in ln(k): 2.812667261781953
""",
)

entry(
    index = 154,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2.10552e+26,'m^3/(mol*s)'), n=-6.10353, w0=(293100,'J/mol'), E0=(100898,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.44008810152278366, var=13.37717509859112, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 8.438031601174622"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 8.438031601174622""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 8.438031601174622
""",
)

entry(
    index = 155,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(1.67502e+15,'m^3/(mol*s)'), n=-2.85507, w0=(291911,'J/mol'), E0=(57346.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2178602768228565, var=3.293205131638785, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl',), comment="""BM rule fitted to 19 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl
    Total Standard Deviation in ln(k): 4.185418510789204"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl
Total Standard Deviation in ln(k): 4.185418510789204""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl
Total Standard Deviation in ln(k): 4.185418510789204
""",
)

entry(
    index = 156,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(3535.96,'m^3/(mol*s)'), n=0.819108, w0=(287641,'J/mol'), E0=(6605.45,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0046806056767311624, var=7.077485090321053, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 5.345065932732235"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 5.345065932732235""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 5.345065932732235
""",
)

entry(
    index = 157,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_3BrCClF->C_1ClFO->O",
    kinetics = ArrheniusBM(A=(0.00549393,'m^3/(mol*s)'), n=2.84052, w0=(299500,'J/mol'), E0=(29950,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_3BrCClF->C_1ClFO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_3BrCClF->C_1ClFO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_3BrCClF->C_1ClFO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_3BrCClF->C_1ClFO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 158,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_3BrCClF->C_N-1ClFO->O",
    kinetics = ArrheniusBM(A=(687986,'m^3/(mol*s)'), n=0.180673, w0=(283500,'J/mol'), E0=(38914.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.81172952430381e-17, var=0.19952571495072416, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_3BrCClF->C_N-1ClFO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_3BrCClF->C_N-1ClFO->O
    Total Standard Deviation in ln(k): 0.8954811065400564"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_3BrCClF->C_N-1ClFO->O
Total Standard Deviation in ln(k): 0.8954811065400564""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_3BrCClF->C_N-1ClFO->O
Total Standard Deviation in ln(k): 0.8954811065400564
""",
)

entry(
    index = 159,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_3BrClF->Br",
    kinetics = ArrheniusBM(A=(3.51884e+13,'m^3/(mol*s)'), n=-1.91815, w0=(237420,'J/mol'), E0=(22663.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.15132587543639395, var=4.3057798820038915, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_3BrClF->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_3BrClF->Br
    Total Standard Deviation in ln(k): 4.540115870995364"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_3BrClF->Br
Total Standard Deviation in ln(k): 4.540115870995364""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_3BrClF->Br
Total Standard Deviation in ln(k): 4.540115870995364
""",
)

entry(
    index = 160,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_N-3BrClF->Br",
    kinetics = ArrheniusBM(A=(1.76212e+12,'m^3/(mol*s)'), n=-1.40873, w0=(253302,'J/mol'), E0=(21457.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.20819619923831897, var=5.793444919006491, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_N-3BrClF->Br',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_N-3BrClF->Br
    Total Standard Deviation in ln(k): 5.34841837158755"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_N-3BrClF->Br
Total Standard Deviation in ln(k): 5.34841837158755""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_N-3BrClF->Br
Total Standard Deviation in ln(k): 5.34841837158755
""",
)

entry(
    index = 161,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R",
    kinetics = ArrheniusBM(A=(7.03209e+15,'m^3/(mol*s)'), n=-3.11532, w0=(299500,'J/mol'), E0=(77983.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.25272363930847636, var=8.516600066923209, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R
    Total Standard Deviation in ln(k): 6.485445389898733"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R
Total Standard Deviation in ln(k): 6.485445389898733""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R
Total Standard Deviation in ln(k): 6.485445389898733
""",
)

entry(
    index = 162,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_3BrCClF->F",
    kinetics = ArrheniusBM(A=(1.22754e+08,'m^3/(mol*s)'), n=-0.779046, w0=(261270,'J/mol'), E0=(44210.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_3BrCClF->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_3BrCClF->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_3BrCClF->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_3BrCClF->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 163,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_N-3BrCClF->F",
    kinetics = ArrheniusBM(A=(0.0332264,'m^3/(mol*s)'), n=2.37175, w0=(264230,'J/mol'), E0=(-15733.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.1837857443867037, var=6.016662017866487, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_N-3BrCClF->F',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_N-3BrCClF->F
    Total Standard Deviation in ln(k): 12.916853296185003"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_N-3BrCClF->F
Total Standard Deviation in ln(k): 12.916853296185003""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_N-3BrCClF->F
Total Standard Deviation in ln(k): 12.916853296185003
""",
)

entry(
    index = 164,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_N-3BrCClF-u1_Ext-3BrCClF-R",
    kinetics = ArrheniusBM(A=(0.254715,'m^3/(mol*s)'), n=2.28881, w0=(299500,'J/mol'), E0=(29950,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_N-3BrCClF-u1_Ext-3BrCClF-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_N-3BrCClF-u1_Ext-3BrCClF-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_N-3BrCClF-u1_Ext-3BrCClF-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_N-3BrCClF-u1_Ext-3BrCClF-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 165,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R",
    kinetics = ArrheniusBM(A=(8.23731e-14,'m^3/(mol*s)'), n=5.23721, w0=(377500,'J/mol'), E0=(-24321.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.23018252732438768, var=2.1204008071863845, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R',), comment="""BM rule fitted to 8 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R
    Total Standard Deviation in ln(k): 3.497562305259632"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 3.497562305259632""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 3.497562305259632
""",
)

entry(
    index = 166,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C",
    kinetics = ArrheniusBM(A=(2.14215,'m^3/(mol*s)'), n=1.56773, w0=(377500,'J/mol'), E0=(76070.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.014231643629638507, var=3.863934639803852, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C',), comment="""BM rule fitted to 8 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C
    Total Standard Deviation in ln(k): 3.9764442995119227"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 3.9764442995119227""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 3.9764442995119227
""",
)

entry(
    index = 167,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C",
    kinetics = ArrheniusBM(A=(5.71668e+13,'m^3/(mol*s)'), n=-2.73675, w0=(377500,'J/mol'), E0=(94279.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06610517962890695, var=29.154769848176354, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C',), comment="""BM rule fitted to 4 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C
    Total Standard Deviation in ln(k): 10.990691950839237"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 10.990691950839237""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 10.990691950839237
""",
)

entry(
    index = 168,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_5R!H->F",
    kinetics = ArrheniusBM(A=(2.70503e-42,'m^3/(mol*s)'), n=14.163, w0=(377500,'J/mol'), E0=(-26564,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.6147725168667681, var=281.70224220879584, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_5R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_5R!H->F
    Total Standard Deviation in ln(k): 35.192103391688136"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_5R!H->F
Total Standard Deviation in ln(k): 35.192103391688136""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_5R!H->F
Total Standard Deviation in ln(k): 35.192103391688136
""",
)

entry(
    index = 169,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(5154.55,'m^3/(mol*s)'), n=0.558651, w0=(377500,'J/mol'), E0=(79691.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.09919969928834332, var=3.268718542005419, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F',), comment="""BM rule fitted to 9 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F
    Total Standard Deviation in ln(k): 3.8737258517254403"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F
Total Standard Deviation in ln(k): 3.8737258517254403""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F
Total Standard Deviation in ln(k): 3.8737258517254403
""",
)

entry(
    index = 170,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_Sp-4CCFFOO=3C",
    kinetics = ArrheniusBM(A=(4.019e+14,'m^3/(mol*s)'), n=-2.70352, w0=(377500,'J/mol'), E0=(97285.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2119162703149814, var=11.957780945004497, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_Sp-4CCFFOO=3C',), comment="""BM rule fitted to 4 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_Sp-4CCFFOO=3C
    Total Standard Deviation in ln(k): 7.464831749951217"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_Sp-4CCFFOO=3C
Total Standard Deviation in ln(k): 7.464831749951217""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_Sp-4CCFFOO=3C
Total Standard Deviation in ln(k): 7.464831749951217
""",
)

entry(
    index = 171,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_N-Sp-4CCFFOO=3C",
    kinetics = ArrheniusBM(A=(2.01209e+06,'m^3/(mol*s)'), n=-0.00825365, w0=(377500,'J/mol'), E0=(77507.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07391693671384797, var=7.315169214801215, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_N-Sp-4CCFFOO=3C',), comment="""BM rule fitted to 9 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_N-Sp-4CCFFOO=3C
    Total Standard Deviation in ln(k): 5.607841605617218"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_N-Sp-4CCFFOO=3C
Total Standard Deviation in ln(k): 5.607841605617218""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_N-Sp-4CCFFOO=3C
Total Standard Deviation in ln(k): 5.607841605617218
""",
)

entry(
    index = 172,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C_Ext-1C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(1.21764e-19,'m^3/(mol*s)'), n=7.53777, w0=(377500,'J/mol'), E0=(-4621.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.828611780953135, var=9.58647310895691, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C_Ext-1C-R_Ext-4C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C_Ext-1C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 13.31413156679966"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C_Ext-1C-R_Ext-4C-R
Total Standard Deviation in ln(k): 13.31413156679966""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C_Ext-1C-R_Ext-4C-R
Total Standard Deviation in ln(k): 13.31413156679966
""",
)

entry(
    index = 173,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C_Ext-4C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(1.2e+06,'m^3/(mol*s)'), n=0, w0=(377500,'J/mol'), E0=(82843.8,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C_Ext-4C-R_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C_Ext-4C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 174,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C_Ext-4C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(30.5257,'m^3/(mol*s)'), n=2.04125, w0=(377500,'J/mol'), E0=(93315.7,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C_Ext-4C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C_Ext-4C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 175,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(2.5e+06,'m^3/(mol*s)'), n=0, w0=(377500,'J/mol'), E0=(57404.7,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 176,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_N-4R!H->C_Ext-1C-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(2.5e+07,'m^3/(mol*s)'), n=0, w0=(377500,'J/mol'), E0=(72095,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_N-4R!H->C_Ext-1C-R_5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_N-4R!H->C_Ext-1C-R_5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_N-4R!H->C_Ext-1C-R_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_N-4R!H->C_Ext-1C-R_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 177,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_N-4R!H->C_Ext-1C-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(3e+06,'m^3/(mol*s)'), n=0, w0=(377500,'J/mol'), E0=(70255.5,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_N-4R!H->C_Ext-1C-R_N-5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_N-4R!H->C_Ext-1C-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_N-4R!H->C_Ext-1C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_N-4R!H->C_Ext-1C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 178,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(5e+08,'m^3/(mol*s)'), n=0, w0=(377500,'J/mol'), E0=(170610,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 179,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(2.27569e+06,'m^3/(mol*s)'), n=0.186753, w0=(377500,'J/mol'), E0=(77317.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3049750542439436, var=4.049781753751407, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R_N-5R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 4.800611793800034"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 4.800611793800034""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 4.800611793800034
""",
)

entry(
    index = 180,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C",
    kinetics = ArrheniusBM(A=(2.27623e-10,'m^3/(mol*s)'), n=5.09592, w0=(377500,'J/mol'), E0=(24102.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.24059633816583487, var=1.1970644072055805, Tref=1000.0, N=23, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C',), comment="""BM rule fitted to 23 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C
    Total Standard Deviation in ln(k): 2.7979028531847914"""),
    rank = 11,
    shortDesc = """BM rule fitted to 23 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C
Total Standard Deviation in ln(k): 2.7979028531847914""",
    longDesc = 
"""
BM rule fitted to 23 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C
Total Standard Deviation in ln(k): 2.7979028531847914
""",
)

entry(
    index = 181,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_N-4BrCClO->C",
    kinetics = ArrheniusBM(A=(9.66369e-11,'m^3/(mol*s)'), n=5.11235, w0=(377500,'J/mol'), E0=(-12125.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.22403445795229843, var=3.0055752382552794, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_N-4BrCClO->C',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_N-4BrCClO->C
    Total Standard Deviation in ln(k): 4.038428646334748"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_N-4BrCClO->C
Total Standard Deviation in ln(k): 4.038428646334748""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_N-4BrCClO->C
Total Standard Deviation in ln(k): 4.038428646334748
""",
)

entry(
    index = 182,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_5CClFINOPSSi->Cl",
    kinetics = ArrheniusBM(A=(5426.36,'m^3/(mol*s)'), n=0.206923, w0=(327000,'J/mol'), E0=(54411.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.5745685336101335e-15, var=19.67711727356854, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_5CClFINOPSSi->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_5CClFINOPSSi->Cl
    Total Standard Deviation in ln(k): 8.89278364556498"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_5CClFINOPSSi->Cl
Total Standard Deviation in ln(k): 8.89278364556498""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_5CClFINOPSSi->Cl
Total Standard Deviation in ln(k): 8.89278364556498
""",
)

entry(
    index = 183,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl",
    kinetics = ArrheniusBM(A=(1.40536e+13,'m^3/(mol*s)'), n=-2.46929, w0=(327000,'J/mol'), E0=(87794.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.12513426049413934, var=2.1816268350866364, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl
    Total Standard Deviation in ln(k): 3.2754677941306607"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl
Total Standard Deviation in ln(k): 3.2754677941306607""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl
Total Standard Deviation in ln(k): 3.2754677941306607
""",
)

entry(
    index = 184,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_5R!H->C",
    kinetics = ArrheniusBM(A=(0.00381671,'m^3/(mol*s)'), n=1.95816, w0=(327000,'J/mol'), E0=(67694.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.01661708277638799, var=3.8631878016647714, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_5R!H->C
    Total Standard Deviation in ln(k): 3.9820570102759514"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_5R!H->C
Total Standard Deviation in ln(k): 3.9820570102759514""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_5R!H->C
Total Standard Deviation in ln(k): 3.9820570102759514
""",
)

entry(
    index = 185,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(8.00655e-23,'m^3/(mol*s)'), n=8.12555, w0=(327000,'J/mol'), E0=(-4458.34,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4096819885548672, var=2.696583683498456, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_N-5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_N-5R!H->C
    Total Standard Deviation in ln(k): 4.321382915149009"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_N-5R!H->C
Total Standard Deviation in ln(k): 4.321382915149009""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_N-5R!H->C
Total Standard Deviation in ln(k): 4.321382915149009
""",
)

entry(
    index = 186,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Sp-5R!H-3CClFO_5R!H->O",
    kinetics = ArrheniusBM(A=(9.74342e-08,'m^3/(mol*s)'), n=4.2645, w0=(327000,'J/mol'), E0=(60940.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Sp-5R!H-3CClFO_5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Sp-5R!H-3CClFO_5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Sp-5R!H-3CClFO_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Sp-5R!H-3CClFO_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 187,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Sp-5R!H-3CClFO_N-5R!H->O",
    kinetics = ArrheniusBM(A=(51.9241,'m^3/(mol*s)'), n=1.43659, w0=(327000,'J/mol'), E0=(78985.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03139387996478252, var=2.6000454443648677, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Sp-5R!H-3CClFO_N-5R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Sp-5R!H-3CClFO_N-5R!H->O
    Total Standard Deviation in ln(k): 3.3114455275907706"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Sp-5R!H-3CClFO_N-5R!H->O
Total Standard Deviation in ln(k): 3.3114455275907706""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Sp-5R!H-3CClFO_N-5R!H->O
Total Standard Deviation in ln(k): 3.3114455275907706
""",
)

entry(
    index = 188,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_N-Sp-5R!H-3CClFO_5R!H->C",
    kinetics = ArrheniusBM(A=(4.78552e-08,'m^3/(mol*s)'), n=4.56733, w0=(327000,'J/mol'), E0=(57012.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_N-Sp-5R!H-3CClFO_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_N-Sp-5R!H-3CClFO_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_N-Sp-5R!H-3CClFO_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_N-Sp-5R!H-3CClFO_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 189,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_N-Sp-5R!H-3CClFO_N-5R!H->C",
    kinetics = ArrheniusBM(A=(4138.58,'m^3/(mol*s)'), n=0.816913, w0=(327000,'J/mol'), E0=(63082.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_N-Sp-5R!H-3CClFO_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_N-Sp-5R!H-3CClFO_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_N-Sp-5R!H-3CClFO_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_N-Sp-5R!H-3CClFO_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 190,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-3CClFO-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.88448e+06,'m^3/(mol*s)'), n=-0.28595, w0=(327000,'J/mol'), E0=(59446,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-3CClFO-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-3CClFO-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-3CClFO-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-3CClFO-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 191,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-3CClFO-R_Ext-4BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(5.29533e-07,'m^3/(mol*s)'), n=3.59832, w0=(327000,'J/mol'), E0=(71695.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0004062628939296235, var=14.496820689555761, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-3CClFO-R_Ext-4BrCFINOPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-3CClFO-R_Ext-4BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 7.633987554008899"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-3CClFO-R_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 7.633987554008899""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-3CClFO-R_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 7.633987554008899
""",
)

entry(
    index = 192,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1",
    kinetics = ArrheniusBM(A=(3.86085e-20,'m^3/(mol*s)'), n=7.48873, w0=(327000,'J/mol'), E0=(6568.07,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3770115919145117, var=4.220065096308573, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1',), comment="""BM rule fitted to 20 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1
    Total Standard Deviation in ln(k): 5.065551884798474"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1
Total Standard Deviation in ln(k): 5.065551884798474""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1
Total Standard Deviation in ln(k): 5.065551884798474
""",
)

entry(
    index = 193,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_N-3C-u1",
    kinetics = ArrheniusBM(A=(0.000211072,'m^3/(mol*s)'), n=3.51383, w0=(327000,'J/mol'), E0=(66463.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.434397016262092e-05, var=4.624184474197434, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_N-3C-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_N-3C-u1
    Total Standard Deviation in ln(k): 4.311001716272808"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_N-3C-u1
Total Standard Deviation in ln(k): 4.311001716272808""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_N-3C-u1
Total Standard Deviation in ln(k): 4.311001716272808
""",
)

entry(
    index = 194,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_N-Sp-4BrCFINOPSSi-3C_3C-u1",
    kinetics = ArrheniusBM(A=(3.36762e-13,'m^3/(mol*s)'), n=5.6414, w0=(327000,'J/mol'), E0=(-2846.82,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.2101293874171102, var=15.431367107869557, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_N-Sp-4BrCFINOPSSi-3C_3C-u1',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_N-Sp-4BrCFINOPSSi-3C_3C-u1
    Total Standard Deviation in ln(k): 10.915682560196254"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_N-Sp-4BrCFINOPSSi-3C_3C-u1
Total Standard Deviation in ln(k): 10.915682560196254""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_N-Sp-4BrCFINOPSSi-3C_3C-u1
Total Standard Deviation in ln(k): 10.915682560196254
""",
)

entry(
    index = 195,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_N-Sp-4BrCFINOPSSi-3C_N-3C-u1",
    kinetics = ArrheniusBM(A=(0.000854975,'m^3/(mol*s)'), n=3.28947, w0=(327000,'J/mol'), E0=(42838.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_N-Sp-4BrCFINOPSSi-3C_N-3C-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_N-Sp-4BrCFINOPSSi-3C_N-3C-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_N-Sp-4BrCFINOPSSi-3C_N-3C-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_N-Sp-4BrCFINOPSSi-3C_N-3C-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 196,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.38248e+16,'m^3/(mol*s)'), n=-2.73444, w0=(299500,'J/mol'), E0=(78132.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.24902106231210822, var=4.390924828939613, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C
    Total Standard Deviation in ln(k): 4.8265099364490744"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 4.8265099364490744""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 4.8265099364490744
""",
)

entry(
    index = 197,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(8.56225e+22,'m^3/(mol*s)'), n=-4.88923, w0=(299500,'J/mol'), E0=(59602.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.22936460790545274, var=7.399698044953812, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 6.029650726471307"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 6.029650726471307""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 6.029650726471307
""",
)

entry(
    index = 198,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C",
    kinetics = ArrheniusBM(A=(5.32392e-23,'m^3/(mol*s)'), n=8.42878, w0=(327000,'J/mol'), E0=(9618.13,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.37749051126744754, var=2.4117244157922397, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C',), comment="""BM rule fitted to 16 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C
    Total Standard Deviation in ln(k): 4.061767602000908"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C
Total Standard Deviation in ln(k): 4.061767602000908""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C
Total Standard Deviation in ln(k): 4.061767602000908
""",
)

entry(
    index = 199,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C",
    kinetics = ArrheniusBM(A=(1.02572e+28,'m^3/(mol*s)'), n=-6.1436, w0=(284716,'J/mol'), E0=(76622.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.27507041045751107, var=3.887768893645592, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C
    Total Standard Deviation in ln(k): 4.643953244983023"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C
Total Standard Deviation in ln(k): 4.643953244983023""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C
Total Standard Deviation in ln(k): 4.643953244983023
""",
)

entry(
    index = 200,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C",
    kinetics = ArrheniusBM(A=(1.48557e+21,'m^3/(mol*s)'), n=-4.12536, w0=(303333,'J/mol'), E0=(91395,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.24130553464454163, var=8.074822143166752, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C
    Total Standard Deviation in ln(k): 6.3029969245556705"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C
Total Standard Deviation in ln(k): 6.3029969245556705""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C
Total Standard Deviation in ln(k): 6.3029969245556705
""",
)

entry(
    index = 201,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C",
    kinetics = ArrheniusBM(A=(5.56316e+35,'m^3/(mol*s)'), n=-8.48295, w0=(308593,'J/mol'), E0=(121881,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.5485777701674205, var=17.58787118325883, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C',), comment="""BM rule fitted to 19 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C
    Total Standard Deviation in ln(k): 9.785773218110258"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C
Total Standard Deviation in ln(k): 9.785773218110258""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C
Total Standard Deviation in ln(k): 9.785773218110258
""",
)

entry(
    index = 202,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_3CClFO->C_Ext-1C-R_Sp-4R!H-1C_4R!H->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3541.93,'m^3/(mol*s)'), n=1.13226, w0=(327000,'J/mol'), E0=(42355.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4922815922106995, var=0.0675906456998819, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_3CClFO->C_Ext-1C-R_Sp-4R!H-1C_4R!H->O_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_3CClFO->C_Ext-1C-R_Sp-4R!H-1C_4R!H->O_Ext-1C-R
    Total Standard Deviation in ln(k): 1.758083478257886"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_3CClFO->C_Ext-1C-R_Sp-4R!H-1C_4R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 1.758083478257886""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_3CClFO->C_Ext-1C-R_Sp-4R!H-1C_4R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 1.758083478257886
""",
)

entry(
    index = 203,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_3CClFO->C_Ext-1C-R_Sp-4R!H-1C_N-4R!H->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.011895,'m^3/(mol*s)'), n=2.70774, w0=(327000,'J/mol'), E0=(88319.2,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_3CClFO->C_Ext-1C-R_Sp-4R!H-1C_N-4R!H->O_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_3CClFO->C_Ext-1C-R_Sp-4R!H-1C_N-4R!H->O_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_3CClFO->C_Ext-1C-R_Sp-4R!H-1C_N-4R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_3CClFO->C_Ext-1C-R_Sp-4R!H-1C_N-4R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 204,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_N-3CClFO->C_Ext-1C-R_N-3ClFO-u1_Ext-1C-R",
    kinetics = ArrheniusBM(A=(52.7701,'m^3/(mol*s)'), n=1.64048, w0=(299500,'J/mol'), E0=(29950,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_N-3CClFO->C_Ext-1C-R_N-3ClFO-u1_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_N-3CClFO->C_Ext-1C-R_N-3ClFO-u1_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_N-3CClFO->C_Ext-1C-R_N-3ClFO-u1_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_N-3CClFO->C_Ext-1C-R_N-3ClFO-u1_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 205,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_1BrClFO-u0",
    kinetics = ArrheniusBM(A=(8.86035e-05,'m^3/(mol*s)'), n=3.31017, w0=(272000,'J/mol'), E0=(27200,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_1BrClFO-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_1BrClFO-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_1BrClFO-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_1BrClFO-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 206,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-1BrClFO-u0",
    kinetics = ArrheniusBM(A=(6.08473,'m^3/(mol*s)'), n=1.89139, w0=(272000,'J/mol'), E0=(27200,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-1BrClFO-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-1BrClFO-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-1BrClFO-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_Ext-3O-R_N-4R!H->O_Ext-4BrCClFINPSSi-R_N-Sp-5R!H=4BrBrCCClClFFIINNPPSSSiSi_N-1BrClFO-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 207,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_3O-u1_1BrO->Br",
    kinetics = ArrheniusBM(A=(904000,'m^3/(mol*s)'), n=0, w0=(245420,'J/mol'), E0=(4224.36,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_3O-u1_1BrO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_3O-u1_1BrO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_3O-u1_1BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_3O-u1_1BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 208,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_3O-u1_N-1BrO->Br",
    kinetics = ArrheniusBM(A=(1246.54,'m^3/(mol*s)'), n=1.07989, w0=(272000,'J/mol'), E0=(37454.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.022654515080099313, var=0.13536078329125176, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_3O-u1_N-1BrO->Br',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_3O-u1_N-1BrO->Br
    Total Standard Deviation in ln(k): 0.7944911893012605"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_3O-u1_N-1BrO->Br
Total Standard Deviation in ln(k): 0.7944911893012605""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_3O-u1_N-1BrO->Br
Total Standard Deviation in ln(k): 0.7944911893012605
""",
)

entry(
    index = 209,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_N-3O-u1_1BrO->Br",
    kinetics = ArrheniusBM(A=(1.26e+07,'m^3/(mol*s)'), n=0, w0=(245420,'J/mol'), E0=(11383.3,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_N-3O-u1_1BrO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_N-3O-u1_1BrO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_N-3O-u1_1BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_N-3O-u1_1BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 210,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_N-3O-u1_N-1BrO->Br",
    kinetics = ArrheniusBM(A=(0.275042,'m^3/(mol*s)'), n=2.30738, w0=(272000,'J/mol'), E0=(20648.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04775776928289103, var=1.5422892446387602, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_N-3O-u1_N-1BrO->Br',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_N-3O-u1_N-1BrO->Br
    Total Standard Deviation in ln(k): 2.609653607586987"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_N-3O-u1_N-1BrO->Br
Total Standard Deviation in ln(k): 2.609653607586987""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_N-3O-u1_N-1BrO->Br
Total Standard Deviation in ln(k): 2.609653607586987
""",
)

entry(
    index = 211,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_1ClFO->O",
    kinetics = ArrheniusBM(A=(5.46781e+11,'m^3/(mol*s)'), n=-1.79685, w0=(299500,'J/mol'), E0=(82490.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2655129192754972, var=6.565719490207164, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_1ClFO->O',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_1ClFO->O
    Total Standard Deviation in ln(k): 5.803982878093955"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_1ClFO->O
Total Standard Deviation in ln(k): 5.803982878093955""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_1ClFO->O
Total Standard Deviation in ln(k): 5.803982878093955
""",
)

entry(
    index = 212,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_N-1ClFO->O",
    kinetics = ArrheniusBM(A=(7.36132e+39,'m^3/(mol*s)'), n=-10.1047, w0=(283500,'J/mol'), E0=(110394,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.5596046912645656, var=22.028875719413676, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_N-1ClFO->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_N-1ClFO->O
    Total Standard Deviation in ln(k): 10.815251814981645"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_N-1ClFO->O
Total Standard Deviation in ln(k): 10.815251814981645""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_N-1ClFO->O
Total Standard Deviation in ln(k): 10.815251814981645
""",
)

entry(
    index = 213,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_1ClFO->F",
    kinetics = ArrheniusBM(A=(3.47386e+17,'m^3/(mol*s)'), n=-3.79151, w0=(288770,'J/mol'), E0=(55145.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.05749138200302929, var=6.078319481301948, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_1ClFO->F',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_1ClFO->F
    Total Standard Deviation in ln(k): 5.086974300768586"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_1ClFO->F
Total Standard Deviation in ln(k): 5.086974300768586""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_1ClFO->F
Total Standard Deviation in ln(k): 5.086974300768586
""",
)

entry(
    index = 214,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F",
    kinetics = ArrheniusBM(A=(2.13555e+13,'m^3/(mol*s)'), n=-2.24922, w0=(292500,'J/mol'), E0=(54333.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.17718229439793673, var=3.6228802136482594, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F',), comment="""BM rule fitted to 16 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F
    Total Standard Deviation in ln(k): 4.2609673504425025"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F
Total Standard Deviation in ln(k): 4.2609673504425025""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F
Total Standard Deviation in ln(k): 4.2609673504425025
""",
)

entry(
    index = 215,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R",
    kinetics = ArrheniusBM(A=(4.8568,'m^3/(mol*s)'), n=1.64333, w0=(289712,'J/mol'), E0=(293.152,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05262168113568221, var=7.769308738225285, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R
    Total Standard Deviation in ln(k): 5.720109539235581"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R
Total Standard Deviation in ln(k): 5.720109539235581""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R
Total Standard Deviation in ln(k): 5.720109539235581
""",
)

entry(
    index = 216,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Sp-4BrCFO-3BrBrCCClFFO",
    kinetics = ArrheniusBM(A=(30526.1,'m^3/(mol*s)'), n=0.654316, w0=(283500,'J/mol'), E0=(23918.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Sp-4BrCFO-3BrBrCCClFFO',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Sp-4BrCFO-3BrBrCCClFFO
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Sp-4BrCFO-3BrBrCCClFFO
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Sp-4BrCFO-3BrBrCCClFFO
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 217,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_N-Sp-4BrCFO-3BrBrCCClFFO",
    kinetics = ArrheniusBM(A=(5.51149e+07,'m^3/(mol*s)'), n=-0.40526, w0=(283500,'J/mol'), E0=(37242.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.14675907080018452, var=0.34946980756160567, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_N-Sp-4BrCFO-3BrBrCCClFFO',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_N-Sp-4BrCFO-3BrBrCCClFFO
    Total Standard Deviation in ln(k): 1.5538599990962576"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_N-Sp-4BrCFO-3BrBrCCClFFO
Total Standard Deviation in ln(k): 1.5538599990962576""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_N-Sp-4BrCFO-3BrBrCCClFFO
Total Standard Deviation in ln(k): 1.5538599990962576
""",
)

entry(
    index = 218,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_3BrClF->Br_1ClFO->O",
    kinetics = ArrheniusBM(A=(5.23133e+06,'m^3/(mol*s)'), n=-0.000975817, w0=(245420,'J/mol'), E0=(4185.89,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_3BrClF->Br_1ClFO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_3BrClF->Br_1ClFO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_3BrClF->Br_1ClFO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_3BrClF->Br_1ClFO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 219,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_3BrClF->Br_N-1ClFO->O",
    kinetics = ArrheniusBM(A=(7.0651e+06,'m^3/(mol*s)'), n=0.163827, w0=(229420,'J/mol'), E0=(6668.79,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_3BrClF->Br_N-1ClFO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_3BrClF->Br_N-1ClFO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_3BrClF->Br_N-1ClFO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_3BrClF->Br_N-1ClFO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 220,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_N-3BrClF->Br_1ClFO->Cl",
    kinetics = ArrheniusBM(A=(2.75e+08,'m^3/(mol*s)'), n=0, w0=(245270,'J/mol'), E0=(11908.2,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_N-3BrClF->Br_1ClFO->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_N-3BrClF->Br_1ClFO->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_N-3BrClF->Br_1ClFO->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_N-3BrClF->Br_1ClFO->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 221,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_N-3BrClF->Br_N-1ClFO->Cl",
    kinetics = ArrheniusBM(A=(4.61796e+13,'m^3/(mol*s)'), n=-1.88486, w0=(254908,'J/mol'), E0=(25507.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.29084537810169764, var=5.721329963796209, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_N-3BrClF->Br_N-1ClFO->Cl',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_N-3BrClF->Br_N-1ClFO->Cl
    Total Standard Deviation in ln(k): 5.5259536068836175"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_N-3BrClF->Br_N-1ClFO->Cl
Total Standard Deviation in ln(k): 5.5259536068836175""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_N-3BrClF->Br_N-1ClFO->Cl
Total Standard Deviation in ln(k): 5.5259536068836175
""",
)

entry(
    index = 222,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_4R!H->F",
    kinetics = ArrheniusBM(A=(1.18119e+12,'m^3/(mol*s)'), n=-2.10081, w0=(299500,'J/mol'), E0=(25317.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.8871030306023553, var=0.3320283513066128, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_4R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_4R!H->F
    Total Standard Deviation in ln(k): 5.896631369266527"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_4R!H->F
Total Standard Deviation in ln(k): 5.896631369266527""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_4R!H->F
Total Standard Deviation in ln(k): 5.896631369266527
""",
)

entry(
    index = 223,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F",
    kinetics = ArrheniusBM(A=(1.12458e+09,'m^3/(mol*s)'), n=-1.09474, w0=(299500,'J/mol'), E0=(70265.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.15210589099965532, var=6.765428918965776, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F
    Total Standard Deviation in ln(k): 5.596579375988314"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F
Total Standard Deviation in ln(k): 5.596579375988314""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F
Total Standard Deviation in ln(k): 5.596579375988314
""",
)

entry(
    index = 224,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_N-3BrCClF->F_3BrCCl->Br",
    kinetics = ArrheniusBM(A=(1.91593e+09,'m^3/(mol*s)'), n=-0.582702, w0=(245420,'J/mol'), E0=(17249.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_N-3BrCClF->F_3BrCCl->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_N-3BrCClF->F_3BrCCl->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_N-3BrCClF->F_3BrCCl->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_N-3BrCClF->F_3BrCCl->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 225,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_N-3BrCClF->F_N-3BrCCl->Br",
    kinetics = ArrheniusBM(A=(2.18374e-05,'m^3/(mol*s)'), n=3.23485, w0=(270500,'J/mol'), E0=(-12845.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.094346729924015, var=2.5269568210931395, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_N-3BrCClF->F_N-3BrCCl->Br',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_N-3BrCClF->F_N-3BrCCl->Br
    Total Standard Deviation in ln(k): 8.448985722285393"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_N-3BrCClF->F_N-3BrCCl->Br
Total Standard Deviation in ln(k): 8.448985722285393""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_N-3BrCClF->F_N-3BrCCl->Br
Total Standard Deviation in ln(k): 8.448985722285393
""",
)

entry(
    index = 226,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_6R!H->F",
    kinetics = ArrheniusBM(A=(20.0567,'m^3/(mol*s)'), n=0.936757, w0=(377500,'J/mol'), E0=(53302.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_6R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_6R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 227,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F",
    kinetics = ArrheniusBM(A=(2.61523e-14,'m^3/(mol*s)'), n=5.36203, w0=(377500,'J/mol'), E0=(-10583.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.23320287094445957, var=1.5624404947235055, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F',), comment="""BM rule fitted to 7 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F
    Total Standard Deviation in ln(k): 3.0918079910318186"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F
Total Standard Deviation in ln(k): 3.0918079910318186""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F
Total Standard Deviation in ln(k): 3.0918079910318186
""",
)

entry(
    index = 228,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->O",
    kinetics = ArrheniusBM(A=(0.00206404,'m^3/(mol*s)'), n=2.78833, w0=(377500,'J/mol'), E0=(72596.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0002119164358598332, var=3.403029882863948, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->O',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->O
    Total Standard Deviation in ln(k): 3.698727995796727"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->O
Total Standard Deviation in ln(k): 3.698727995796727""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->O
Total Standard Deviation in ln(k): 3.698727995796727
""",
)

entry(
    index = 229,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->O",
    kinetics = ArrheniusBM(A=(0.440651,'m^3/(mol*s)'), n=1.66279, w0=(377500,'J/mol'), E0=(73336.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.007406637063760949, var=3.0478214808454065, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->O',), comment="""BM rule fitted to 6 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->O
    Total Standard Deviation in ln(k): 3.518478344235328"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->O
Total Standard Deviation in ln(k): 3.518478344235328""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->O
Total Standard Deviation in ln(k): 3.518478344235328
""",
)

entry(
    index = 230,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(10.8005,'m^3/(mol*s)'), n=0.927525, w0=(377500,'J/mol'), E0=(66908.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.01771508020151891, var=48.64075906975436, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 14.02611952559976"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 14.02611952559976""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 14.02611952559976
""",
)

entry(
    index = 231,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(415.506,'m^3/(mol*s)'), n=0.731615, w0=(377500,'J/mol'), E0=(60721,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 232,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_5R!H->F_Sp-4BrCFINOPSSi-3C",
    kinetics = ArrheniusBM(A=(5310.27,'m^3/(mol*s)'), n=0.584739, w0=(377500,'J/mol'), E0=(162496,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_5R!H->F_Sp-4BrCFINOPSSi-3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_5R!H->F_Sp-4BrCFINOPSSi-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_5R!H->F_Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_5R!H->F_Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 233,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_5R!H->F_N-Sp-4BrCFINOPSSi-3C",
    kinetics = ArrheniusBM(A=(2.04513e-05,'m^3/(mol*s)'), n=3.11027, w0=(377500,'J/mol'), E0=(41819.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_5R!H->F_N-Sp-4BrCFINOPSSi-3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_5R!H->F_N-Sp-4BrCFINOPSSi-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_5R!H->F_N-Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_5R!H->F_N-Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 234,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi",
    kinetics = ArrheniusBM(A=(5.80782e+08,'m^3/(mol*s)'), n=-0.971858, w0=(377500,'J/mol'), E0=(87664.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1411092345705402, var=3.4129106724501947, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi',), comment="""BM rule fitted to 8 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi
    Total Standard Deviation in ln(k): 4.058106371944206"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 4.058106371944206""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 4.058106371944206
""",
)

entry(
    index = 235,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_N-Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi",
    kinetics = ArrheniusBM(A=(0.287756,'m^3/(mol*s)'), n=2.01677, w0=(377500,'J/mol'), E0=(90165.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_N-Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_N-Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_N-Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_N-Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 236,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_Sp-4CCFFOO=3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(223.904,'m^3/(mol*s)'), n=0.665992, w0=(377500,'J/mol'), E0=(60874.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_Sp-4CCFFOO=3C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_Sp-4CCFFOO=3C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_Sp-4CCFFOO=3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_Sp-4CCFFOO=3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 237,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_Sp-4CCFFOO=3C_4CFO->C",
    kinetics = ArrheniusBM(A=(727.239,'m^3/(mol*s)'), n=0.376238, w0=(377500,'J/mol'), E0=(74431.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_Sp-4CCFFOO=3C_4CFO->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_Sp-4CCFFOO=3C_4CFO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_Sp-4CCFFOO=3C_4CFO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_Sp-4CCFFOO=3C_4CFO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 238,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_Sp-4CCFFOO=3C_N-4CFO->C",
    kinetics = ArrheniusBM(A=(3.68944,'m^3/(mol*s)'), n=1.67555, w0=(377500,'J/mol'), E0=(64685.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=8.997534477772192e-16, var=21.093872457788333, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_Sp-4CCFFOO=3C_N-4CFO->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_Sp-4CCFFOO=3C_N-4CFO->C
    Total Standard Deviation in ln(k): 9.207360493132587"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_Sp-4CCFFOO=3C_N-4CFO->C
Total Standard Deviation in ln(k): 9.207360493132587""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_Sp-4CCFFOO=3C_N-4CFO->C
Total Standard Deviation in ln(k): 9.207360493132587
""",
)

entry(
    index = 239,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_N-Sp-4CCFFOO=3C_4CFO->O",
    kinetics = ArrheniusBM(A=(8.88686e-05,'m^3/(mol*s)'), n=3.02721, w0=(377500,'J/mol'), E0=(42645.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_N-Sp-4CCFFOO=3C_4CFO->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_N-Sp-4CCFFOO=3C_4CFO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_N-Sp-4CCFFOO=3C_4CFO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_N-Sp-4CCFFOO=3C_4CFO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 240,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_N-Sp-4CCFFOO=3C_N-4CFO->O",
    kinetics = ArrheniusBM(A=(7.00114e+08,'m^3/(mol*s)'), n=-0.775919, w0=(377500,'J/mol'), E0=(83419.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.11916753143529758, var=8.135570985346636, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_N-Sp-4CCFFOO=3C_N-4CFO->O',), comment="""BM rule fitted to 8 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_N-Sp-4CCFFOO=3C_N-4CFO->O
    Total Standard Deviation in ln(k): 6.0175061996270625"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_N-Sp-4CCFFOO=3C_N-4CFO->O
Total Standard Deviation in ln(k): 6.0175061996270625""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_N-Sp-4CCFFOO=3C_N-4CFO->O
Total Standard Deviation in ln(k): 6.0175061996270625
""",
)

entry(
    index = 241,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C_Ext-1C-R_Ext-4C-R_5R!H->F",
    kinetics = ArrheniusBM(A=(0.4,'m^3/(mol*s)'), n=2.5, w0=(377500,'J/mol'), E0=(50026.6,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C_Ext-1C-R_Ext-4C-R_5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C_Ext-1C-R_Ext-4C-R_5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C_Ext-1C-R_Ext-4C-R_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C_Ext-1C-R_Ext-4C-R_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 242,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C_Ext-1C-R_Ext-4C-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(2.10518e+06,'m^3/(mol*s)'), n=-0.208522, w0=(377500,'J/mol'), E0=(76036.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0022770762577922097, var=43.43214470243579, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C_Ext-1C-R_Ext-4C-R_N-5R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C_Ext-1C-R_Ext-4C-R_N-5R!H->F
    Total Standard Deviation in ln(k): 13.217540659589995"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C_Ext-1C-R_Ext-4C-R_N-5R!H->F
Total Standard Deviation in ln(k): 13.217540659589995""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C_Ext-1C-R_Ext-4C-R_N-5R!H->F
Total Standard Deviation in ln(k): 13.217540659589995
""",
)

entry(
    index = 243,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->F",
    kinetics = ArrheniusBM(A=(8.1712e-17,'m^3/(mol*s)'), n=6.89639, w0=(377500,'J/mol'), E0=(7452.14,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3526924675606849, var=1.468831498085182, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->F',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->F
    Total Standard Deviation in ln(k): 3.3158078476908783"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->F
Total Standard Deviation in ln(k): 3.3158078476908783""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->F
Total Standard Deviation in ln(k): 3.3158078476908783
""",
)

entry(
    index = 244,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(377500,'J/mol'), E0=(68072.1,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 245,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(8.45512e-11,'m^3/(mol*s)'), n=5.20956, w0=(377500,'J/mol'), E0=(23363.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.24090203970778482, var=1.2576604837963699, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R
    Total Standard Deviation in ln(k): 2.8535009382744274"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R
Total Standard Deviation in ln(k): 2.8535009382744274""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R
Total Standard Deviation in ln(k): 2.8535009382744274
""",
)

entry(
    index = 246,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.06805e-11,'m^3/(mol*s)'), n=5.50814, w0=(377500,'J/mol'), E0=(24181.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.18961189118709348, var=1.330134483533562, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-1C-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-1C-R
    Total Standard Deviation in ln(k): 2.788501948621743"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-1C-R
Total Standard Deviation in ln(k): 2.788501948621743""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-1C-R
Total Standard Deviation in ln(k): 2.788501948621743
""",
)

entry(
    index = 247,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_N-4BrCClO->C_4ClO->O",
    kinetics = ArrheniusBM(A=(72.5748,'m^3/(mol*s)'), n=1.78727, w0=(377500,'J/mol'), E0=(69608.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00016374826442201187, var=2.3387465599204367, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_N-4BrCClO->C_4ClO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_N-4BrCClO->C_4ClO->O
    Total Standard Deviation in ln(k): 3.0662449621730365"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_N-4BrCClO->C_4ClO->O
Total Standard Deviation in ln(k): 3.0662449621730365""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_N-4BrCClO->C_4ClO->O
Total Standard Deviation in ln(k): 3.0662449621730365
""",
)

entry(
    index = 248,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_N-4BrCClO->C_N-4ClO->O",
    kinetics = ArrheniusBM(A=(8.33246e-10,'m^3/(mol*s)'), n=4.73903, w0=(377500,'J/mol'), E0=(-11633.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.22003296211978093, var=3.690773408437578, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_N-4BrCClO->C_N-4ClO->O',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_N-4BrCClO->C_N-4ClO->O
    Total Standard Deviation in ln(k): 4.404220520025395"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_N-4BrCClO->C_N-4ClO->O
Total Standard Deviation in ln(k): 4.404220520025395""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_N-4BrCClO->C_N-4ClO->O
Total Standard Deviation in ln(k): 4.404220520025395
""",
)

entry(
    index = 249,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_5CClFINOPSSi->Cl_Ext-3CClFO-R_6R!H->C",
    kinetics = ArrheniusBM(A=(210.143,'m^3/(mol*s)'), n=0.420053, w0=(327000,'J/mol'), E0=(52664.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_5CClFINOPSSi->Cl_Ext-3CClFO-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_5CClFINOPSSi->Cl_Ext-3CClFO-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_5CClFINOPSSi->Cl_Ext-3CClFO-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_5CClFINOPSSi->Cl_Ext-3CClFO-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 250,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_5CClFINOPSSi->Cl_Ext-3CClFO-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(135500,'m^3/(mol*s)'), n=0, w0=(327000,'J/mol'), E0=(56247.4,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_5CClFINOPSSi->Cl_Ext-3CClFO-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_5CClFINOPSSi->Cl_Ext-3CClFO-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_5CClFINOPSSi->Cl_Ext-3CClFO-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_5CClFINOPSSi->Cl_Ext-3CClFO-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 251,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C",
    kinetics = ArrheniusBM(A=(1.58684e+08,'m^3/(mol*s)'), n=-1.03701, w0=(327000,'J/mol'), E0=(77475.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0579275137676553, var=1.7780124447213934, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C
    Total Standard Deviation in ln(k): 2.8187030312699717"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C
Total Standard Deviation in ln(k): 2.8187030312699717""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C
Total Standard Deviation in ln(k): 2.8187030312699717
""",
)

entry(
    index = 252,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_N-Sp-5CF-1C",
    kinetics = ArrheniusBM(A=(3210.17,'m^3/(mol*s)'), n=0.601824, w0=(327000,'J/mol'), E0=(60212.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_N-Sp-5CF-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_N-Sp-5CF-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_N-Sp-5CF-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_N-Sp-5CF-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 253,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_5R!H->C_6R!H->C",
    kinetics = ArrheniusBM(A=(1.55759e-07,'m^3/(mol*s)'), n=3.32068, w0=(327000,'J/mol'), E0=(59143,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_5R!H->C_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_5R!H->C_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_5R!H->C_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_5R!H->C_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 254,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_5R!H->C_N-6R!H->C",
    kinetics = ArrheniusBM(A=(0.0486986,'m^3/(mol*s)'), n=1.57639, w0=(327000,'J/mol'), E0=(67703.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.015255539187826348, var=7.167565146167526, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_5R!H->C_N-6R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_5R!H->C_N-6R!H->C
    Total Standard Deviation in ln(k): 5.40546914141694"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_5R!H->C_N-6R!H->C
Total Standard Deviation in ln(k): 5.40546914141694""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_5R!H->C_N-6R!H->C
Total Standard Deviation in ln(k): 5.40546914141694
""",
)

entry(
    index = 255,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_N-5R!H->C_5ClFO->Cl",
    kinetics = ArrheniusBM(A=(24679.7,'m^3/(mol*s)'), n=0.0266534, w0=(327000,'J/mol'), E0=(70436.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.020116140353135255, var=0.4636674324812988, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_N-5R!H->C_5ClFO->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_N-5R!H->C_5ClFO->Cl
    Total Standard Deviation in ln(k): 1.4156299244412311"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_N-5R!H->C_5ClFO->Cl
Total Standard Deviation in ln(k): 1.4156299244412311""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_N-5R!H->C_5ClFO->Cl
Total Standard Deviation in ln(k): 1.4156299244412311
""",
)

entry(
    index = 256,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_N-5R!H->C_N-5ClFO->Cl",
    kinetics = ArrheniusBM(A=(1.19684,'m^3/(mol*s)'), n=1.77109, w0=(327000,'J/mol'), E0=(60519.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.008645500198563782, var=0.0010437054277527627, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_N-5R!H->C_N-5ClFO->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_N-5R!H->C_N-5ClFO->Cl
    Total Standard Deviation in ln(k): 0.08648819601519707"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_N-5R!H->C_N-5ClFO->Cl
Total Standard Deviation in ln(k): 0.08648819601519707""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_N-5R!H->C_N-5ClFO->Cl
Total Standard Deviation in ln(k): 0.08648819601519707
""",
)

entry(
    index = 257,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Sp-5R!H-3CClFO_N-5R!H->O_5CCl->C",
    kinetics = ArrheniusBM(A=(0.000111183,'m^3/(mol*s)'), n=3.16652, w0=(327000,'J/mol'), E0=(75191.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=7.183951665994539e-05, var=0.016449742049074328, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Sp-5R!H-3CClFO_N-5R!H->O_5CCl->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Sp-5R!H-3CClFO_N-5R!H->O_5CCl->C
    Total Standard Deviation in ln(k): 0.257300901543114"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Sp-5R!H-3CClFO_N-5R!H->O_5CCl->C
Total Standard Deviation in ln(k): 0.257300901543114""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Sp-5R!H-3CClFO_N-5R!H->O_5CCl->C
Total Standard Deviation in ln(k): 0.257300901543114
""",
)

entry(
    index = 258,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Sp-5R!H-3CClFO_N-5R!H->O_N-5CCl->C",
    kinetics = ArrheniusBM(A=(3943.23,'m^3/(mol*s)'), n=0.729364, w0=(327000,'J/mol'), E0=(64248.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Sp-5R!H-3CClFO_N-5R!H->O_N-5CCl->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Sp-5R!H-3CClFO_N-5R!H->O_N-5CCl->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Sp-5R!H-3CClFO_N-5R!H->O_N-5CCl->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Sp-5R!H-3CClFO_N-5R!H->O_N-5CCl->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 259,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-3CClFO-R_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(3.85859e-07,'m^3/(mol*s)'), n=3.30296, w0=(327000,'J/mol'), E0=(63102.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-3CClFO-R_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-3CClFO-R_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-3CClFO-R_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-3CClFO-R_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 260,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.4138e-17,'m^3/(mol*s)'), n=6.67321, w0=(327000,'J/mol'), E0=(-989.332,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4758010814261643, var=2.9108593005802277, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R',), comment="""BM rule fitted to 15 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R
    Total Standard Deviation in ln(k): 4.615806849129586"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R
Total Standard Deviation in ln(k): 4.615806849129586""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R
Total Standard Deviation in ln(k): 4.615806849129586
""",
)

entry(
    index = 261,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.020834,'m^3/(mol*s)'), n=2.53385, w0=(327000,'J/mol'), E0=(77596.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.008497846063110827, var=0.5026463770185007, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_4BrCFINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 1.4426595918898018"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 1.4426595918898018""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 1.4426595918898018
""",
)

entry(
    index = 262,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_N-4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(3318.37,'m^3/(mol*s)'), n=0.806435, w0=(327000,'J/mol'), E0=(68097.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.012738461081291636, var=2.0627715516337455, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_N-4BrCFINOPSSi->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_N-4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 2.9112772697858142"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 2.9112772697858142""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 2.9112772697858142
""",
)

entry(
    index = 263,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_N-3C-u1_4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.22681e-05,'m^3/(mol*s)'), n=3.91521, w0=(327000,'J/mol'), E0=(59342.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_N-3C-u1_4BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_N-3C-u1_4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_N-3C-u1_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_N-3C-u1_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 264,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_N-3C-u1_N-4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(5.21196e-06,'m^3/(mol*s)'), n=3.85925, w0=(327000,'J/mol'), E0=(61730.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_N-3C-u1_N-4BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_N-3C-u1_N-4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_N-3C-u1_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_N-3C-u1_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 265,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_N-Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.875e+06,'m^3/(mol*s)'), n=0, w0=(327000,'J/mol'), E0=(66587.6,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_N-Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_N-Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_N-Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_N-Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 266,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_N-Sp-4BrCFINOPSSi-3C_3C-u1_4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(9.68382e-07,'m^3/(mol*s)'), n=3.67709, w0=(327000,'J/mol'), E0=(51632.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.128423414068483, var=1.847793272702959, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_N-Sp-4BrCFINOPSSi-3C_3C-u1_4BrCFINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_N-Sp-4BrCFINOPSSi-3C_3C-u1_4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 3.047779653380861"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_N-Sp-4BrCFINOPSSi-3C_3C-u1_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 3.047779653380861""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_N-Sp-4BrCFINOPSSi-3C_3C-u1_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 3.047779653380861
""",
)

entry(
    index = 267,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_N-Sp-4BrCFINOPSSi-3C_3C-u1_N-4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(423328,'m^3/(mol*s)'), n=0.468098, w0=(327000,'J/mol'), E0=(35320.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_N-Sp-4BrCFINOPSSi-3C_3C-u1_N-4BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_N-Sp-4BrCFINOPSSi-3C_3C-u1_N-4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_N-Sp-4BrCFINOPSSi-3C_3C-u1_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_N-Sp-4BrCFINOPSSi-3C_3C-u1_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 268,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.25183e+15,'m^3/(mol*s)'), n=-2.70935, w0=(299500,'J/mol'), E0=(76339,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.20858557597707988, var=6.154949359005549, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 5.49766577580012"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 5.49766577580012""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 5.49766577580012
""",
)

entry(
    index = 269,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(1.74019e+08,'m^3/(mol*s)'), n=-0.308868, w0=(299500,'J/mol'), E0=(66063.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.15969779456574232, var=4.168577371559353, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-5C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-5C-R
    Total Standard Deviation in ln(k): 4.49433724001282"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 4.49433724001282""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 4.49433724001282
""",
)

entry(
    index = 270,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(0.0134262,'m^3/(mol*s)'), n=2.60238, w0=(299500,'J/mol'), E0=(13431.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1510848664779744, var=0.2205000765659587, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->O',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 1.320982401806987"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->O
Total Standard Deviation in ln(k): 1.320982401806987""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->O
Total Standard Deviation in ln(k): 1.320982401806987
""",
)

entry(
    index = 271,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(9.15457e+40,'m^3/(mol*s)'), n=-10.4089, w0=(299500,'J/mol'), E0=(75595.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.507801644682754, var=10.128031630335636, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->O',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 7.6558664177314215"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->O
Total Standard Deviation in ln(k): 7.6558664177314215""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->O
Total Standard Deviation in ln(k): 7.6558664177314215
""",
)

entry(
    index = 272,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.18693e-23,'m^3/(mol*s)'), n=8.49652, w0=(327000,'J/mol'), E0=(10620.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.38232304411456103, var=2.6071857093715076, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R',), comment="""BM rule fitted to 14 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R
    Total Standard Deviation in ln(k): 4.197612702149682"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R
Total Standard Deviation in ln(k): 4.197612702149682""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R
Total Standard Deviation in ln(k): 4.197612702149682
""",
)

entry(
    index = 273,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6.3003e+28,'m^3/(mol*s)'), n=-6.42379, w0=(284937,'J/mol'), E0=(77456.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.21790252741773875, var=4.947176618658688, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R
    Total Standard Deviation in ln(k): 5.00647556046096"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R
Total Standard Deviation in ln(k): 5.00647556046096""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R
Total Standard Deviation in ln(k): 5.00647556046096
""",
)

entry(
    index = 274,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_3CClFO->C",
    kinetics = ArrheniusBM(A=(1.08502e-22,'m^3/(mol*s)'), n=8.64631, w0=(327000,'J/mol'), E0=(-26010.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.4159734270573328, var=49.62002445919826, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_3CClFO->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_3CClFO->C
    Total Standard Deviation in ln(k): 20.191936064266727"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_3CClFO->C
Total Standard Deviation in ln(k): 20.191936064266727""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_3CClFO->C
Total Standard Deviation in ln(k): 20.191936064266727
""",
)

entry(
    index = 275,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C",
    kinetics = ArrheniusBM(A=(8.94249e+19,'m^3/(mol*s)'), n=-3.78695, w0=(291500,'J/mol'), E0=(82631,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.4811402480317912, var=9.91942267861543, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C
    Total Standard Deviation in ln(k): 7.5228312730755125"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C
Total Standard Deviation in ln(k): 7.5228312730755125""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C
Total Standard Deviation in ln(k): 7.5228312730755125
""",
)

entry(
    index = 276,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_4BrCFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(3.96117e+28,'m^3/(mol*s)'), n=-6.49239, w0=(302375,'J/mol'), E0=(83596.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.46969874115636984, var=17.487718650974628, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_4BrCFINOPSSi->Br',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_4BrCFINOPSSi->Br
    Total Standard Deviation in ln(k): 9.56361283502309"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_4BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 9.56361283502309""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_4BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 9.56361283502309
""",
)

entry(
    index = 277,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(1.74674e+36,'m^3/(mol*s)'), n=-8.59807, w0=(310251,'J/mol'), E0=(128948,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.5710001311557296, var=19.658379183409753, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br',), comment="""BM rule fitted to 15 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br
    Total Standard Deviation in ln(k): 10.323222131342906"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 10.323222131342906""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 10.323222131342906
""",
)

entry(
    index = 278,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_3CClFO->C_Ext-1C-R_Sp-4R!H-1C_4R!H->O_Ext-1C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(0.0111464,'m^3/(mol*s)'), n=2.7136, w0=(327000,'J/mol'), E0=(23557.8,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_3CClFO->C_Ext-1C-R_Sp-4R!H-1C_4R!H->O_Ext-1C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_3CClFO->C_Ext-1C-R_Sp-4R!H-1C_4R!H->O_Ext-1C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_3CClFO->C_Ext-1C-R_Sp-4R!H-1C_4R!H->O_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_3CClFO->C_Ext-1C-R_Sp-4R!H-1C_4R!H->O_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 279,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_3CClFO->C_Ext-1C-R_Sp-4R!H-1C_4R!H->O_Ext-1C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.0343304,'m^3/(mol*s)'), n=2.71102, w0=(327000,'J/mol'), E0=(39616.9,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_3CClFO->C_Ext-1C-R_Sp-4R!H-1C_4R!H->O_Ext-1C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_3CClFO->C_Ext-1C-R_Sp-4R!H-1C_4R!H->O_Ext-1C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_3CClFO->C_Ext-1C-R_Sp-4R!H-1C_4R!H->O_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_N-1C-u0_3CClFO->C_Ext-1C-R_Sp-4R!H-1C_4R!H->O_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 280,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_3O-u1_N-1BrO->Br_Ext-1O-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(0.0898359,'m^3/(mol*s)'), n=2.42885, w0=(272000,'J/mol'), E0=(27200,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_3O-u1_N-1BrO->Br_Ext-1O-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_3O-u1_N-1BrO->Br_Ext-1O-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_3O-u1_N-1BrO->Br_Ext-1O-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_3O-u1_N-1BrO->Br_Ext-1O-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 281,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_3O-u1_N-1BrO->Br_Ext-1O-R_4R!H->C",
    kinetics = ArrheniusBM(A=(0.0703235,'m^3/(mol*s)'), n=2.34313, w0=(272000,'J/mol'), E0=(27346.4,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_3O-u1_N-1BrO->Br_Ext-1O-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_3O-u1_N-1BrO->Br_Ext-1O-R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_3O-u1_N-1BrO->Br_Ext-1O-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_3O-u1_N-1BrO->Br_Ext-1O-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 282,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_3O-u1_N-1BrO->Br_Ext-1O-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(24235.8,'m^3/(mol*s)'), n=0.643885, w0=(272000,'J/mol'), E0=(40061.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06397030255359418, var=1.5641811761623856, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_3O-u1_N-1BrO->Br_Ext-1O-R_N-4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_3O-u1_N-1BrO->Br_Ext-1O-R_N-4R!H->C
    Total Standard Deviation in ln(k): 2.6679960128384854"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_3O-u1_N-1BrO->Br_Ext-1O-R_N-4R!H->C
Total Standard Deviation in ln(k): 2.6679960128384854""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_3O-u1_N-1BrO->Br_Ext-1O-R_N-4R!H->C
Total Standard Deviation in ln(k): 2.6679960128384854
""",
)

entry(
    index = 283,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_N-3O-u1_N-1BrO->Br_Ext-1O-R",
    kinetics = ArrheniusBM(A=(0.162524,'m^3/(mol*s)'), n=2.39091, w0=(272000,'J/mol'), E0=(25597.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.08034137144210812, var=2.9959507748148555, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_N-3O-u1_N-1BrO->Br_Ext-1O-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_N-3O-u1_N-1BrO->Br_Ext-1O-R
    Total Standard Deviation in ln(k): 3.6718216046806083"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_N-3O-u1_N-1BrO->Br_Ext-1O-R
Total Standard Deviation in ln(k): 3.6718216046806083""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_N-3O-u1_N-1BrO->Br_Ext-1O-R
Total Standard Deviation in ln(k): 3.6718216046806083
""",
)

entry(
    index = 284,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_1ClFO->O_5R!H->F",
    kinetics = ArrheniusBM(A=(0.218097,'m^3/(mol*s)'), n=1.28932, w0=(299500,'J/mol'), E0=(53971.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_1ClFO->O_5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_1ClFO->O_5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_1ClFO->O_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_1ClFO->O_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 285,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_1ClFO->O_N-5R!H->F",
    kinetics = ArrheniusBM(A=(3.00329e+07,'m^3/(mol*s)'), n=-0.438434, w0=(299500,'J/mol'), E0=(72546,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.20720451475523072, var=2.6555726842046816, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_1ClFO->O_N-5R!H->F',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_1ClFO->O_N-5R!H->F
    Total Standard Deviation in ln(k): 3.7875162008010155"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_1ClFO->O_N-5R!H->F
Total Standard Deviation in ln(k): 3.7875162008010155""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_1ClFO->O_N-5R!H->F
Total Standard Deviation in ln(k): 3.7875162008010155
""",
)

entry(
    index = 286,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_N-1ClFO->O_Sp-4R!H-3BrCClF",
    kinetics = ArrheniusBM(A=(5.972e+29,'m^3/(mol*s)'), n=-7.17263, w0=(283500,'J/mol'), E0=(94500.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06306915444830848, var=34.41533342633492, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_N-1ClFO->O_Sp-4R!H-3BrCClF',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_N-1ClFO->O_Sp-4R!H-3BrCClF
    Total Standard Deviation in ln(k): 11.919160021560801"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_N-1ClFO->O_Sp-4R!H-3BrCClF
Total Standard Deviation in ln(k): 11.919160021560801""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_N-1ClFO->O_Sp-4R!H-3BrCClF
Total Standard Deviation in ln(k): 11.919160021560801
""",
)

entry(
    index = 287,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_N-1ClFO->O_N-Sp-4R!H-3BrCClF",
    kinetics = ArrheniusBM(A=(455.559,'m^3/(mol*s)'), n=0.98537, w0=(283500,'J/mol'), E0=(28350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_N-1ClFO->O_N-Sp-4R!H-3BrCClF',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_N-1ClFO->O_N-Sp-4R!H-3BrCClF
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_N-1ClFO->O_N-Sp-4R!H-3BrCClF
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_N-1ClFO->O_N-Sp-4R!H-3BrCClF
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 288,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_1ClFO->F_Ext-3BrCClF-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(55624.1,'m^3/(mol*s)'), n=-0.110059, w0=(288770,'J/mol'), E0=(28156.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.14097564936898727, var=0.08717774874113246, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_1ClFO->F_Ext-3BrCClF-R_5R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_1ClFO->F_Ext-3BrCClF-R_5R!H->Cl
    Total Standard Deviation in ln(k): 0.9461258128122229"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_1ClFO->F_Ext-3BrCClF-R_5R!H->Cl
Total Standard Deviation in ln(k): 0.9461258128122229""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_1ClFO->F_Ext-3BrCClF-R_5R!H->Cl
Total Standard Deviation in ln(k): 0.9461258128122229
""",
)

entry(
    index = 289,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_1ClFO->F_Ext-3BrCClF-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(24.7268,'m^3/(mol*s)'), n=1.11035, w0=(288770,'J/mol'), E0=(17369.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_1ClFO->F_Ext-3BrCClF-R_N-5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_1ClFO->F_Ext-3BrCClF-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_1ClFO->F_Ext-3BrCClF-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_1ClFO->F_Ext-3BrCClF-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 290,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O",
    kinetics = ArrheniusBM(A=(9.77895e+16,'m^3/(mol*s)'), n=-3.36287, w0=(299500,'J/mol'), E0=(58168.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2581110395722446, var=6.664969141361914, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O
    Total Standard Deviation in ln(k): 5.824064864919236"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O
Total Standard Deviation in ln(k): 5.824064864919236""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O
Total Standard Deviation in ln(k): 5.824064864919236
""",
)

entry(
    index = 291,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_N-1ClO->O",
    kinetics = ArrheniusBM(A=(1678.97,'m^3/(mol*s)'), n=0.769961, w0=(283500,'J/mol'), E0=(35402.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.044875033772721465, var=1.1607988384649661, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_N-1ClO->O',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_N-1ClO->O
    Total Standard Deviation in ln(k): 2.272660429372085"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_N-1ClO->O
Total Standard Deviation in ln(k): 2.272660429372085""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_N-1ClO->O
Total Standard Deviation in ln(k): 2.272660429372085
""",
)

entry(
    index = 292,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R_Ext-3BrCClF-R",
    kinetics = ArrheniusBM(A=(1.33915e+13,'m^3/(mol*s)'), n=-1.99653, w0=(288818,'J/mol'), E0=(58079,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.716666782840959, var=3.896772044871818, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R_Ext-3BrCClF-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R_Ext-3BrCClF-R
    Total Standard Deviation in ln(k): 8.270628935334221"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R_Ext-3BrCClF-R
Total Standard Deviation in ln(k): 8.270628935334221""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R_Ext-3BrCClF-R
Total Standard Deviation in ln(k): 8.270628935334221
""",
)

entry(
    index = 293,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R_1ClFO->O",
    kinetics = ArrheniusBM(A=(2e+06,'m^3/(mol*s)'), n=0, w0=(299500,'J/mol'), E0=(29950,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R_1ClFO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R_1ClFO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R_1ClFO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R_1ClFO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 294,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R_N-1ClFO->O",
    kinetics = ArrheniusBM(A=(1.5e+06,'m^3/(mol*s)'), n=0, w0=(283500,'J/mol'), E0=(28350,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R_N-1ClFO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R_N-1ClFO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R_N-1ClFO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R_N-1ClFO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 295,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_N-Sp-4BrCFO-3BrBrCCClFFO_4BrCFO->C",
    kinetics = ArrheniusBM(A=(2.625e+06,'m^3/(mol*s)'), n=0, w0=(283500,'J/mol'), E0=(28350,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_N-Sp-4BrCFO-3BrBrCCClFFO_4BrCFO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_N-Sp-4BrCFO-3BrBrCCClFFO_4BrCFO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_N-Sp-4BrCFO-3BrBrCCClFFO_4BrCFO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_N-Sp-4BrCFO-3BrBrCCClFFO_4BrCFO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 296,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_N-Sp-4BrCFO-3BrBrCCClFFO_N-4BrCFO->C",
    kinetics = ArrheniusBM(A=(1.9e+06,'m^3/(mol*s)'), n=0, w0=(283500,'J/mol'), E0=(26530,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_N-Sp-4BrCFO-3BrBrCCClFFO_N-4BrCFO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_N-Sp-4BrCFO-3BrBrCCClFFO_N-4BrCFO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_N-Sp-4BrCFO-3BrBrCCClFFO_N-4BrCFO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_N-Sp-4BrCFO-3BrBrCCClFFO_N-4BrCFO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 297,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_N-3BrClF->Br_N-1ClFO->Cl_Ext-1FO-R",
    kinetics = ArrheniusBM(A=(1.3e+08,'m^3/(mol*s)'), n=0, w0=(256000,'J/mol'), E0=(25600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_N-3BrClF->Br_N-1ClFO->Cl_Ext-1FO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_N-3BrClF->Br_N-1ClFO->Cl_Ext-1FO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_N-3BrClF->Br_N-1ClFO->Cl_Ext-1FO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_N-3BrClF->Br_N-1ClFO->Cl_Ext-1FO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 298,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_N-3BrClF->Br_N-1ClFO->Cl_1FO->O",
    kinetics = ArrheniusBM(A=(1.90603e+10,'m^3/(mol*s)'), n=-1.07798, w0=(257757,'J/mol'), E0=(15242.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.14471903139257522, var=1.1012985232171526, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_N-3BrClF->Br_N-1ClFO->Cl_1FO->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_N-3BrClF->Br_N-1ClFO->Cl_1FO->O
    Total Standard Deviation in ln(k): 2.467440202682148"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_N-3BrClF->Br_N-1ClFO->Cl_1FO->O
Total Standard Deviation in ln(k): 2.467440202682148""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_N-3BrClF->Br_N-1ClFO->Cl_1FO->O
Total Standard Deviation in ln(k): 2.467440202682148
""",
)

entry(
    index = 299,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_N-3BrClF->Br_N-1ClFO->Cl_N-1FO->O",
    kinetics = ArrheniusBM(A=(2.09737e+08,'m^3/(mol*s)'), n=0.0325169, w0=(245270,'J/mol'), E0=(11646.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_N-3BrClF->Br_N-1ClFO->Cl_N-1FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_N-3BrClF->Br_N-1ClFO->Cl_N-1FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_N-3BrClF->Br_N-1ClFO->Cl_N-1FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_N-3BrClF->Br_N-1ClFO->Cl_N-1FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 300,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R",
    kinetics = ArrheniusBM(A=(5513.92,'m^3/(mol*s)'), n=0.326148, w0=(299500,'J/mol'), E0=(15653.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 301,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R",
    kinetics = ArrheniusBM(A=(3.60565,'m^3/(mol*s)'), n=1.20385, w0=(299500,'J/mol'), E0=(49159,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.24727775331562046, var=10.508444266229489, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R
    Total Standard Deviation in ln(k): 7.119996592396043"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R
Total Standard Deviation in ln(k): 7.119996592396043""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R
Total Standard Deviation in ln(k): 7.119996592396043
""",
)

entry(
    index = 302,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_4BrCClINOPSSi->Cl",
    kinetics = ArrheniusBM(A=(5.95358e-10,'m^3/(mol*s)'), n=4.55569, w0=(299500,'J/mol'), E0=(18474.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1052797351177451, var=0.012557858128170313, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_4BrCClINOPSSi->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_4BrCClINOPSSi->Cl
    Total Standard Deviation in ln(k): 0.48917626819480414"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_4BrCClINOPSSi->Cl
Total Standard Deviation in ln(k): 0.48917626819480414""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_4BrCClINOPSSi->Cl
Total Standard Deviation in ln(k): 0.48917626819480414
""",
)

entry(
    index = 303,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_N-4BrCClINOPSSi->Cl",
    kinetics = ArrheniusBM(A=(596880,'m^3/(mol*s)'), n=0.194919, w0=(299500,'J/mol'), E0=(74423.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06670427970414879, var=14.665826065401646, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_N-4BrCClINOPSSi->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_N-4BrCClINOPSSi->Cl
    Total Standard Deviation in ln(k): 7.844929502930761"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_N-4BrCClINOPSSi->Cl
Total Standard Deviation in ln(k): 7.844929502930761""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_N-4BrCClINOPSSi->Cl
Total Standard Deviation in ln(k): 7.844929502930761
""",
)

entry(
    index = 304,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_N-3BrCClF->F_N-3BrCCl->Br_3CCl->C",
    kinetics = ArrheniusBM(A=(90.1146,'m^3/(mol*s)'), n=1.48177, w0=(299500,'J/mol'), E0=(72259.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_N-3BrCClF->F_N-3BrCCl->Br_3CCl->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_N-3BrCClF->F_N-3BrCCl->Br_3CCl->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_N-3BrCClF->F_N-3BrCCl->Br_3CCl->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_N-3BrCClF->F_N-3BrCCl->Br_3CCl->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 305,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_N-3BrCClF->F_N-3BrCCl->Br_N-3CCl->C",
    kinetics = ArrheniusBM(A=(4.1257e+08,'m^3/(mol*s)'), n=-0.785566, w0=(256000,'J/mol'), E0=(24979.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=7.310496763189906e-16, var=0.1830067426456429, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_N-3BrCClF->F_N-3BrCCl->Br_N-3CCl->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_N-3BrCClF->F_N-3BrCCl->Br_N-3CCl->C
    Total Standard Deviation in ln(k): 0.85761137943089"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_N-3BrCClF->F_N-3BrCCl->Br_N-3CCl->C
Total Standard Deviation in ln(k): 0.85761137943089""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_N-3BrCClF->F_N-3BrCCl->Br_N-3CCl->C
Total Standard Deviation in ln(k): 0.85761137943089
""",
)

entry(
    index = 306,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.11342e-14,'m^3/(mol*s)'), n=5.52327, w0=(377500,'J/mol'), E0=(2146.49,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2368282303737004, var=1.1440933320499662, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C',), comment="""BM rule fitted to 6 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 2.7393565244588594"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C
Total Standard Deviation in ln(k): 2.7393565244588594""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C
Total Standard Deviation in ln(k): 2.7393565244588594
""",
)

entry(
    index = 307,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_N-6BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.311275,'m^3/(mol*s)'), n=0.978062, w0=(377500,'J/mol'), E0=(37750,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_N-6BrCClINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_N-6BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_N-6BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_N-6BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 308,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->O_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.0131926,'m^3/(mol*s)'), n=2.28677, w0=(377500,'J/mol'), E0=(62877.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->O_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->O_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 309,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->O_5CF->C",
    kinetics = ArrheniusBM(A=(3.1478e-06,'m^3/(mol*s)'), n=3.23663, w0=(377500,'J/mol'), E0=(60412,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1391895558473104, var=2.7022360556062677, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->O_5CF->C',), comment="""BM rule fitted to 5 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->O_5CF->C
    Total Standard Deviation in ln(k): 3.6452021328637314"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->O_5CF->C
Total Standard Deviation in ln(k): 3.6452021328637314""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->O_5CF->C
Total Standard Deviation in ln(k): 3.6452021328637314
""",
)

entry(
    index = 310,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->O_N-5CF->C",
    kinetics = ArrheniusBM(A=(8.57271,'m^3/(mol*s)'), n=0.913662, w0=(377500,'J/mol'), E0=(70310.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->O_N-5CF->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->O_N-5CF->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->O_N-5CF->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->O_N-5CF->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 311,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(75.7389,'m^3/(mol*s)'), n=0.567841, w0=(377500,'J/mol'), E0=(79302.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.002960605136392612, var=80.5499143950141, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R
    Total Standard Deviation in ln(k): 17.99985666231482"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R
Total Standard Deviation in ln(k): 17.99985666231482""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R
Total Standard Deviation in ln(k): 17.99985666231482
""",
)

entry(
    index = 312,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.12356e-06,'m^3/(mol*s)'), n=3.29547, w0=(377500,'J/mol'), E0=(61316.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 313,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi_Sp-4BrCFINOPSSi-3C",
    kinetics = ArrheniusBM(A=(155.295,'m^3/(mol*s)'), n=1.08686, w0=(377500,'J/mol'), E0=(71945.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.011658288912141934, var=0.43750855971363606, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi_Sp-4BrCFINOPSSi-3C',), comment="""BM rule fitted to 5 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi_Sp-4BrCFINOPSSi-3C
    Total Standard Deviation in ln(k): 1.3553127696801648"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi_Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 1.3553127696801648""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi_Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 1.3553127696801648
""",
)

entry(
    index = 314,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi_N-Sp-4BrCFINOPSSi-3C",
    kinetics = ArrheniusBM(A=(131.111,'m^3/(mol*s)'), n=0.623064, w0=(377500,'J/mol'), E0=(68285.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.001814113051895433, var=19.584724860832623, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi_N-Sp-4BrCFINOPSSi-3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi_N-Sp-4BrCFINOPSSi-3C
    Total Standard Deviation in ln(k): 8.876439457653666"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi_N-Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 8.876439457653666""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi_N-Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 8.876439457653666
""",
)

entry(
    index = 315,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_N-Sp-4CCFFOO=3C_N-4CFO->O_Ext-3C-R",
    kinetics = ArrheniusBM(A=(283.628,'m^3/(mol*s)'), n=1.07155, w0=(377500,'J/mol'), E0=(74624.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03543298314827721, var=6.106849372232294, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_N-Sp-4CCFFOO=3C_N-4CFO->O_Ext-3C-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_N-Sp-4CCFFOO=3C_N-4CFO->O_Ext-3C-R
    Total Standard Deviation in ln(k): 5.043137004006911"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_N-Sp-4CCFFOO=3C_N-4CFO->O_Ext-3C-R
Total Standard Deviation in ln(k): 5.043137004006911""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_N-Sp-4CCFFOO=3C_N-4CFO->O_Ext-3C-R
Total Standard Deviation in ln(k): 5.043137004006911
""",
)

entry(
    index = 316,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_N-Sp-4CCFFOO=3C_N-4CFO->O_4CF->C",
    kinetics = ArrheniusBM(A=(1.11449,'m^3/(mol*s)'), n=1.85194, w0=(377500,'J/mol'), E0=(69827.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.010349809717648813, var=4.099603986082469, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_N-Sp-4CCFFOO=3C_N-4CFO->O_4CF->C',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_N-Sp-4CCFFOO=3C_N-4CFO->O_4CF->C
    Total Standard Deviation in ln(k): 4.085087649161569"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_N-Sp-4CCFFOO=3C_N-4CFO->O_4CF->C
Total Standard Deviation in ln(k): 4.085087649161569""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_N-Sp-4CCFFOO=3C_N-4CFO->O_4CF->C
Total Standard Deviation in ln(k): 4.085087649161569
""",
)

entry(
    index = 317,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_N-Sp-4CCFFOO=3C_N-4CFO->O_N-4CF->C",
    kinetics = ArrheniusBM(A=(127137,'m^3/(mol*s)'), n=0.344475, w0=(377500,'J/mol'), E0=(23657.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_N-Sp-4CCFFOO=3C_N-4CFO->O_N-4CF->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_N-Sp-4CCFFOO=3C_N-4CFO->O_N-4CF->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_N-Sp-4CCFFOO=3C_N-4CFO->O_N-4CF->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_N-Sp-4CCFFOO=3C_N-4CFO->O_N-4CF->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 318,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C_Ext-1C-R_Ext-4C-R_N-5R!H->F_Ext-4C-R",
    kinetics = ArrheniusBM(A=(300000,'m^3/(mol*s)'), n=0, w0=(377500,'J/mol'), E0=(91977.5,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C_Ext-1C-R_Ext-4C-R_N-5R!H->F_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C_Ext-1C-R_Ext-4C-R_N-5R!H->F_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C_Ext-1C-R_Ext-4C-R_N-5R!H->F_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_4R!H->C_Ext-1C-R_Ext-4C-R_N-5R!H->F_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 319,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->F_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.11321e-16,'m^3/(mol*s)'), n=6.79409, w0=(377500,'J/mol'), E0=(6971.23,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3767466585149717, var=2.0341600407461917, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->F_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->F_Ext-1C-R
    Total Standard Deviation in ln(k): 3.8058326521015973"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->F_Ext-1C-R
Total Standard Deviation in ln(k): 3.8058326521015973""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->F_Ext-1C-R
Total Standard Deviation in ln(k): 3.8058326521015973
""",
)

entry(
    index = 320,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(3.53142e-08,'m^3/(mol*s)'), n=4.3809, w0=(377500,'J/mol'), E0=(19103.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2311143200586872, var=1.239088907399723, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_5R!H->Cl',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_5R!H->Cl
    Total Standard Deviation in ln(k): 2.8122474774490347"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_5R!H->Cl
Total Standard Deviation in ln(k): 2.8122474774490347""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_5R!H->Cl
Total Standard Deviation in ln(k): 2.8122474774490347
""",
)

entry(
    index = 321,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(1.96782e-11,'m^3/(mol*s)'), n=5.31067, w0=(377500,'J/mol'), E0=(29820.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.18081449385362605, var=1.9311290745775522, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_N-5R!H->Cl',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 3.240189281853766"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 3.240189281853766""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 3.240189281853766
""",
)

entry(
    index = 322,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-1C-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(0.000187287,'m^3/(mol*s)'), n=3.3772, w0=(377500,'J/mol'), E0=(52779.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.14461331002318453, var=0.4139862045664977, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-1C-R_5R!H->Cl',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-1C-R_5R!H->Cl
    Total Standard Deviation in ln(k): 1.6532318519835962"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-1C-R_5R!H->Cl
Total Standard Deviation in ln(k): 1.6532318519835962""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-1C-R_5R!H->Cl
Total Standard Deviation in ln(k): 1.6532318519835962
""",
)

entry(
    index = 323,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-1C-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(2305.74,'m^3/(mol*s)'), n=1.3445, w0=(377500,'J/mol'), E0=(59071.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.22732408925703998, var=6.961080989995246, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-1C-R_N-5R!H->Cl',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-1C-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 5.860431131189627"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-1C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 5.860431131189627""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-1C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 5.860431131189627
""",
)

entry(
    index = 324,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_N-4BrCClO->C_4ClO->O_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(185.874,'m^3/(mol*s)'), n=1.75948, w0=(377500,'J/mol'), E0=(71729.9,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_N-4BrCClO->C_4ClO->O_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_N-4BrCClO->C_4ClO->O_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_N-4BrCClO->C_4ClO->O_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_N-4BrCClO->C_4ClO->O_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 325,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_N-4BrCClO->C_N-4ClO->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.97302e-06,'m^3/(mol*s)'), n=3.3926, w0=(377500,'J/mol'), E0=(20075.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.5219233026892134, var=0.001049586313955792, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_N-4BrCClO->C_N-4ClO->O_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_N-4BrCClO->C_N-4ClO->O_Ext-1C-R
    Total Standard Deviation in ln(k): 3.8888759391173497"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_N-4BrCClO->C_N-4ClO->O_Ext-1C-R
Total Standard Deviation in ln(k): 3.8888759391173497""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_N-4BrCClO->C_N-4ClO->O_Ext-1C-R
Total Standard Deviation in ln(k): 3.8888759391173497
""",
)

entry(
    index = 326,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_5CF->C",
    kinetics = ArrheniusBM(A=(95380,'m^3/(mol*s)'), n=0.0123277, w0=(327000,'J/mol'), E0=(71681.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0011627826594900522, var=0.35984360878986205, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_5CF->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_5CF->C
    Total Standard Deviation in ln(k): 1.205501313405628"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_5CF->C
Total Standard Deviation in ln(k): 1.205501313405628""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_5CF->C
Total Standard Deviation in ln(k): 1.205501313405628
""",
)

entry(
    index = 327,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C",
    kinetics = ArrheniusBM(A=(1.72248e+08,'m^3/(mol*s)'), n=-1.07541, w0=(327000,'J/mol'), E0=(77232.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.056884056507211615, var=2.370377361337601, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C
    Total Standard Deviation in ln(k): 3.229420880840031"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C
Total Standard Deviation in ln(k): 3.229420880840031""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C
Total Standard Deviation in ln(k): 3.229420880840031
""",
)

entry(
    index = 328,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_5R!H->C_N-6R!H->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(1.46105,'m^3/(mol*s)'), n=1.05347, w0=(327000,'J/mol'), E0=(66427.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-7.411655188782661e-05, var=23.891333057511883, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_5R!H->C_N-6R!H->C_Ext-5C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_5R!H->C_N-6R!H->C_Ext-5C-R
    Total Standard Deviation in ln(k): 9.799082953294391"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_5R!H->C_N-6R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 9.799082953294391""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_5R!H->C_N-6R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 9.799082953294391
""",
)

entry(
    index = 329,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_N-5R!H->C_5ClFO->Cl_6R!H->F",
    kinetics = ArrheniusBM(A=(3.50476,'m^3/(mol*s)'), n=1.02205, w0=(327000,'J/mol'), E0=(55374.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_N-5R!H->C_5ClFO->Cl_6R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_N-5R!H->C_5ClFO->Cl_6R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_N-5R!H->C_5ClFO->Cl_6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_N-5R!H->C_5ClFO->Cl_6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 330,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_N-5R!H->C_5ClFO->Cl_N-6R!H->F",
    kinetics = ArrheniusBM(A=(8.56692,'m^3/(mol*s)'), n=1.06336, w0=(327000,'J/mol'), E0=(61561.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_N-5R!H->C_5ClFO->Cl_N-6R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_N-5R!H->C_5ClFO->Cl_N-6R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_N-5R!H->C_5ClFO->Cl_N-6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_N-5R!H->C_5ClFO->Cl_N-6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 331,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_N-5R!H->C_N-5ClFO->Cl_5FO->O",
    kinetics = ArrheniusBM(A=(2.19448e-05,'m^3/(mol*s)'), n=3.35979, w0=(327000,'J/mol'), E0=(61032.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_N-5R!H->C_N-5ClFO->Cl_5FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_N-5R!H->C_N-5ClFO->Cl_5FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_N-5R!H->C_N-5ClFO->Cl_5FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_N-5R!H->C_N-5ClFO->Cl_5FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 332,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_N-5R!H->C_N-5ClFO->Cl_N-5FO->O",
    kinetics = ArrheniusBM(A=(56.6252,'m^3/(mol*s)'), n=0.99896, w0=(327000,'J/mol'), E0=(48198.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_N-5R!H->C_N-5ClFO->Cl_N-5FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_N-5R!H->C_N-5ClFO->Cl_N-5FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_N-5R!H->C_N-5ClFO->Cl_N-5FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_N-5R!H->C_N-5ClFO->Cl_N-5FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 333,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Sp-5R!H-3CClFO_N-5R!H->O_5CCl->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(3.26481e-07,'m^3/(mol*s)'), n=3.88187, w0=(327000,'J/mol'), E0=(67376.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Sp-5R!H-3CClFO_N-5R!H->O_5CCl->C_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Sp-5R!H-3CClFO_N-5R!H->O_5CCl->C_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Sp-5R!H-3CClFO_N-5R!H->O_5CCl->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Sp-5R!H-3CClFO_N-5R!H->O_5CCl->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 334,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6.80202e-20,'m^3/(mol*s)'), n=7.38302, w0=(327000,'J/mol'), E0=(-9935.15,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.6003007141274336, var=2.1510465394337923, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 14 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 4.4485272343794575"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 4.4485272343794575""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 4.4485272343794575
""",
)

entry(
    index = 335,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_4BrCFINOPSSi->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.000183421,'m^3/(mol*s)'), n=3.08609, w0=(327000,'J/mol'), E0=(67923.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_4BrCFINOPSSi->C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_4BrCFINOPSSi->C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_4BrCFINOPSSi->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_4BrCFINOPSSi->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 336,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_N-4BrCFINOPSSi->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(7.82049e+06,'m^3/(mol*s)'), n=-0.360206, w0=(327000,'J/mol'), E0=(65965.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.007919056535651111, var=7.340789768403433, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_N-4BrCFINOPSSi->C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_N-4BrCFINOPSSi->C_Ext-3C-R
    Total Standard Deviation in ln(k): 5.451504669120441"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_N-4BrCFINOPSSi->C_Ext-3C-R
Total Standard Deviation in ln(k): 5.451504669120441""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_N-4BrCFINOPSSi->C_Ext-3C-R
Total Standard Deviation in ln(k): 5.451504669120441
""",
)

entry(
    index = 337,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_N-Sp-4BrCFINOPSSi-3C_3C-u1_4BrCFINOPSSi->C_Sp-4C=3C",
    kinetics = ArrheniusBM(A=(0.000142581,'m^3/(mol*s)'), n=3.33955, w0=(327000,'J/mol'), E0=(70800.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_N-Sp-4BrCFINOPSSi-3C_3C-u1_4BrCFINOPSSi->C_Sp-4C=3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_N-Sp-4BrCFINOPSSi-3C_3C-u1_4BrCFINOPSSi->C_Sp-4C=3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_N-Sp-4BrCFINOPSSi-3C_3C-u1_4BrCFINOPSSi->C_Sp-4C=3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_N-Sp-4BrCFINOPSSi-3C_3C-u1_4BrCFINOPSSi->C_Sp-4C=3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 338,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_N-Sp-4BrCFINOPSSi-3C_3C-u1_4BrCFINOPSSi->C_N-Sp-4C=3C",
    kinetics = ArrheniusBM(A=(1565.77,'m^3/(mol*s)'), n=0.653508, w0=(327000,'J/mol'), E0=(57810,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_N-Sp-4BrCFINOPSSi-3C_3C-u1_4BrCFINOPSSi->C_N-Sp-4C=3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_N-Sp-4BrCFINOPSSi-3C_3C-u1_4BrCFINOPSSi->C_N-Sp-4C=3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_N-Sp-4BrCFINOPSSi-3C_3C-u1_4BrCFINOPSSi->C_N-Sp-4C=3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_N-Sp-4BrCFINOPSSi-3C_3C-u1_4BrCFINOPSSi->C_N-Sp-4C=3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 339,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(4.89453e+09,'m^3/(mol*s)'), n=-0.85018, w0=(299500,'J/mol'), E0=(68542.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.16834240070023365, var=2.6891432174839043, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R_Ext-6R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 3.710457185757045"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 3.710457185757045""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 3.710457185757045
""",
)

entry(
    index = 340,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R_3O-u1",
    kinetics = ArrheniusBM(A=(1.42893e+28,'m^3/(mol*s)'), n=-6.3203, w0=(299500,'J/mol'), E0=(98981.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.333529716998769, var=109.16028746792871, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R_3O-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R_3O-u1
    Total Standard Deviation in ln(k): 21.78344649134883"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R_3O-u1
Total Standard Deviation in ln(k): 21.78344649134883""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R_3O-u1
Total Standard Deviation in ln(k): 21.78344649134883
""",
)

entry(
    index = 341,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R_N-3O-u1",
    kinetics = ArrheniusBM(A=(1.92415e-09,'m^3/(mol*s)'), n=4.39204, w0=(299500,'J/mol'), E0=(9026.96,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04695322233784124, var=0.7019975659481158, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R_N-3O-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R_N-3O-u1
    Total Standard Deviation in ln(k): 1.7976461191588329"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R_N-3O-u1
Total Standard Deviation in ln(k): 1.7976461191588329""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R_N-3O-u1
Total Standard Deviation in ln(k): 1.7976461191588329
""",
)

entry(
    index = 342,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-5C-R_3O-u1",
    kinetics = ArrheniusBM(A=(0.057352,'m^3/(mol*s)'), n=2.53406, w0=(299500,'J/mol'), E0=(37077.3,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-5C-R_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-5C-R_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-5C-R_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-5C-R_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 343,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-5C-R_N-3O-u1",
    kinetics = ArrheniusBM(A=(71.082,'m^3/(mol*s)'), n=1.78047, w0=(299500,'J/mol'), E0=(70716,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-5C-R_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-5C-R_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-5C-R_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-5C-R_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 344,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->O_3O-u1",
    kinetics = ArrheniusBM(A=(123.539,'m^3/(mol*s)'), n=1.39966, w0=(299500,'J/mol'), E0=(34301.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.11638642559514523, var=0.07617808970076764, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->O_3O-u1',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->O_3O-u1
    Total Standard Deviation in ln(k): 0.845742675626788"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->O_3O-u1
Total Standard Deviation in ln(k): 0.845742675626788""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->O_3O-u1
Total Standard Deviation in ln(k): 0.845742675626788
""",
)

entry(
    index = 345,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->O_N-3O-u1",
    kinetics = ArrheniusBM(A=(19458.6,'m^3/(mol*s)'), n=0.885377, w0=(299500,'J/mol'), E0=(40073.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.010998035635065394, var=0.16470362621903395, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->O_N-3O-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->O_N-3O-u1
    Total Standard Deviation in ln(k): 0.8412288154299133"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->O_N-3O-u1
Total Standard Deviation in ln(k): 0.8412288154299133""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->O_N-3O-u1
Total Standard Deviation in ln(k): 0.8412288154299133
""",
)

entry(
    index = 346,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->O_5ClF->F",
    kinetics = ArrheniusBM(A=(3.28945e+42,'m^3/(mol*s)'), n=-11.0493, w0=(299500,'J/mol'), E0=(46272.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.304230504669441, var=80.97606372350121, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->O_5ClF->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->O_5ClF->F
    Total Standard Deviation in ln(k): 23.829473497697535"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->O_5ClF->F
Total Standard Deviation in ln(k): 23.829473497697535""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->O_5ClF->F
Total Standard Deviation in ln(k): 23.829473497697535
""",
)

entry(
    index = 347,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->O_N-5ClF->F",
    kinetics = ArrheniusBM(A=(6.28443e+15,'m^3/(mol*s)'), n=-2.8666, w0=(299500,'J/mol'), E0=(41246.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.04958548742509155, var=7.659319777563204, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->O_N-5ClF->F',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->O_N-5ClF->F
    Total Standard Deviation in ln(k): 5.672786425376503"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->O_N-5ClF->F
Total Standard Deviation in ln(k): 5.672786425376503""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->O_N-5ClF->F
Total Standard Deviation in ln(k): 5.672786425376503
""",
)

entry(
    index = 348,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2.91987e-26,'m^3/(mol*s)'), n=9.38276, w0=(327000,'J/mol'), E0=(7456.96,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5151261788163088, var=2.10335677914548, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C
    Total Standard Deviation in ln(k): 4.2017449644481255"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 4.2017449644481255""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 4.2017449644481255
""",
)

entry(
    index = 349,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.60005e-19,'m^3/(mol*s)'), n=7.41101, w0=(327000,'J/mol'), E0=(15025.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.18584249793824897, var=3.951562273965686, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 4.452060961143319"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 4.452060961143319""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 4.452060961143319
""",
)

entry(
    index = 350,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(635049,'m^3/(mol*s)'), n=0.297593, w0=(285006,'J/mol'), E0=(26551.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.054990220667167314, var=2.5450921468170655, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl
    Total Standard Deviation in ln(k): 3.3363894033006605"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl
Total Standard Deviation in ln(k): 3.3363894033006605""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl
Total Standard Deviation in ln(k): 3.3363894033006605
""",
)

entry(
    index = 351,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(5.25004e+35,'m^3/(mol*s)'), n=-8.37711, w0=(284818,'J/mol'), E0=(91073.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.139611945991563, var=17.73138791348363, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_N-5R!H->Cl',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 8.792453475667912"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 8.792453475667912""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 8.792453475667912
""",
)

entry(
    index = 352,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_3CClFO->C_4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.000141709,'m^3/(mol*s)'), n=3.34347, w0=(327000,'J/mol'), E0=(67808.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0010803452893020033, var=0.09744382221526766, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_3CClFO->C_4BrCFINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_3CClFO->C_4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 0.6285123978481912"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_3CClFO->C_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 0.6285123978481912""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_3CClFO->C_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 0.6285123978481912
""",
)

entry(
    index = 353,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_3CClFO->C_N-4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.5e+07,'m^3/(mol*s)'), n=0, w0=(327000,'J/mol'), E0=(39288.5,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_3CClFO->C_N-4BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_3CClFO->C_N-4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_3CClFO->C_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_3CClFO->C_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 354,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C_3ClFO-u1",
    kinetics = ArrheniusBM(A=(1.40065e+23,'m^3/(mol*s)'), n=-4.6755, w0=(289900,'J/mol'), E0=(97097.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.6632233347279575, var=11.061342298214134, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C_3ClFO-u1',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C_3ClFO-u1
    Total Standard Deviation in ln(k): 8.333857756963768"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C_3ClFO-u1
Total Standard Deviation in ln(k): 8.333857756963768""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C_3ClFO-u1
Total Standard Deviation in ln(k): 8.333857756963768
""",
)

entry(
    index = 355,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C_N-3ClFO-u1",
    kinetics = ArrheniusBM(A=(3e+06,'m^3/(mol*s)'), n=0, w0=(299500,'J/mol'), E0=(21956.6,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C_N-3ClFO-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C_N-3ClFO-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C_N-3ClFO-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C_N-3ClFO-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 356,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_4BrCFINOPSSi->Br_3CClFO->Cl",
    kinetics = ArrheniusBM(A=(1.9e+08,'m^3/(mol*s)'), n=0, w0=(283500,'J/mol'), E0=(81655.6,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_4BrCFINOPSSi->Br_3CClFO->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_4BrCFINOPSSi->Br_3CClFO->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_4BrCFINOPSSi->Br_3CClFO->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_4BrCFINOPSSi->Br_3CClFO->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 357,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_4BrCFINOPSSi->Br_N-3CClFO->Cl",
    kinetics = ArrheniusBM(A=(2.2914e+37,'m^3/(mol*s)'), n=-9.21342, w0=(308667,'J/mol'), E0=(90330.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.5923752115075438, var=28.382536086887917, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_4BrCFINOPSSi->Br_N-3CClFO->Cl',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_4BrCFINOPSSi->Br_N-3CClFO->Cl
    Total Standard Deviation in ln(k): 12.168658704325521"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_4BrCFINOPSSi->Br_N-3CClFO->Cl
Total Standard Deviation in ln(k): 12.168658704325521""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_4BrCFINOPSSi->Br_N-3CClFO->Cl
Total Standard Deviation in ln(k): 12.168658704325521
""",
)

entry(
    index = 358,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.73266e+34,'m^3/(mol*s)'), n=-8.07511, w0=(308752,'J/mol'), E0=(123053,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.5324846704418418, var=19.371510837995057, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R
    Total Standard Deviation in ln(k): 10.161357426142974"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R
Total Standard Deviation in ln(k): 10.161357426142974""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R
Total Standard Deviation in ln(k): 10.161357426142974
""",
)

entry(
    index = 359,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_3CClFO->C",
    kinetics = ArrheniusBM(A=(0.000328721,'m^3/(mol*s)'), n=3.19942, w0=(327000,'J/mol'), E0=(73069.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00270886685695681, var=0.6124908689661955, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_3CClFO->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_3CClFO->C
    Total Standard Deviation in ln(k): 1.575747871735938"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_3CClFO->C
Total Standard Deviation in ln(k): 1.575747871735938""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_3CClFO->C
Total Standard Deviation in ln(k): 1.575747871735938
""",
)

entry(
    index = 360,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_N-3CClFO->C",
    kinetics = ArrheniusBM(A=(3.72742e+17,'m^3/(mol*s)'), n=-2.93697, w0=(283500,'J/mol'), E0=(2590.95,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.609868534487436, var=0.03692914219224229, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_N-3CClFO->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_N-3CClFO->C
    Total Standard Deviation in ln(k): 4.4301448855615995"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_N-3CClFO->C
Total Standard Deviation in ln(k): 4.4301448855615995""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_N-3CClFO->C
Total Standard Deviation in ln(k): 4.4301448855615995
""",
)

entry(
    index = 361,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_3O-u1_N-1BrO->Br_Ext-1O-R_N-4R!H->C_4BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(2e+06,'m^3/(mol*s)'), n=0, w0=(272000,'J/mol'), E0=(27200,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_3O-u1_N-1BrO->Br_Ext-1O-R_N-4R!H->C_4BrClFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_3O-u1_N-1BrO->Br_Ext-1O-R_N-4R!H->C_4BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_3O-u1_N-1BrO->Br_Ext-1O-R_N-4R!H->C_4BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_3O-u1_N-1BrO->Br_Ext-1O-R_N-4R!H->C_4BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 362,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_3O-u1_N-1BrO->Br_Ext-1O-R_N-4R!H->C_N-4BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(0.0597365,'m^3/(mol*s)'), n=2.3895, w0=(272000,'J/mol'), E0=(29395.1,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_3O-u1_N-1BrO->Br_Ext-1O-R_N-4R!H->C_N-4BrClFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_3O-u1_N-1BrO->Br_Ext-1O-R_N-4R!H->C_N-4BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_3O-u1_N-1BrO->Br_Ext-1O-R_N-4R!H->C_N-4BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_3O-u1_N-1BrO->Br_Ext-1O-R_N-4R!H->C_N-4BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 363,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_N-3O-u1_N-1BrO->Br_Ext-1O-R_4R!H->C",
    kinetics = ArrheniusBM(A=(0.110507,'m^3/(mol*s)'), n=2.54955, w0=(272000,'J/mol'), E0=(32710.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07656662572669266, var=1.8208793184283498, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_N-3O-u1_N-1BrO->Br_Ext-1O-R_4R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_N-3O-u1_N-1BrO->Br_Ext-1O-R_4R!H->C
    Total Standard Deviation in ln(k): 2.8975671963302014"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_N-3O-u1_N-1BrO->Br_Ext-1O-R_4R!H->C
Total Standard Deviation in ln(k): 2.8975671963302014""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_N-3O-u1_N-1BrO->Br_Ext-1O-R_4R!H->C
Total Standard Deviation in ln(k): 2.8975671963302014
""",
)

entry(
    index = 364,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_N-3O-u1_N-1BrO->Br_Ext-1O-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(1.5e+06,'m^3/(mol*s)'), n=0, w0=(272000,'J/mol'), E0=(27200,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_N-3O-u1_N-1BrO->Br_Ext-1O-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_N-3O-u1_N-1BrO->Br_Ext-1O-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_N-3O-u1_N-1BrO->Br_Ext-1O-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_N-3O-u1_N-1BrO->Br_Ext-1O-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 365,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_1ClFO->O_N-5R!H->F_Ext-3BrCClF-R",
    kinetics = ArrheniusBM(A=(3.18121e+07,'m^3/(mol*s)'), n=-0.491976, w0=(299500,'J/mol'), E0=(68244.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.21629641272552838, var=3.795855785388044, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_1ClFO->O_N-5R!H->F_Ext-3BrCClF-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_1ClFO->O_N-5R!H->F_Ext-3BrCClF-R
    Total Standard Deviation in ln(k): 4.449274874673261"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_1ClFO->O_N-5R!H->F_Ext-3BrCClF-R
Total Standard Deviation in ln(k): 4.449274874673261""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_1ClFO->O_N-5R!H->F_Ext-3BrCClF-R
Total Standard Deviation in ln(k): 4.449274874673261
""",
)

entry(
    index = 366,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_N-1ClFO->O_Sp-4R!H-3BrCClF_Ext-3BrCClF-R",
    kinetics = ArrheniusBM(A=(227.702,'m^3/(mol*s)'), n=0.812121, w0=(283500,'J/mol'), E0=(43230.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0011593949134833107, var=42.17190048174953, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_N-1ClFO->O_Sp-4R!H-3BrCClF_Ext-3BrCClF-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_N-1ClFO->O_Sp-4R!H-3BrCClF_Ext-3BrCClF-R
    Total Standard Deviation in ln(k): 13.021641727496226"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_N-1ClFO->O_Sp-4R!H-3BrCClF_Ext-3BrCClF-R
Total Standard Deviation in ln(k): 13.021641727496226""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_N-1ClFO->O_Sp-4R!H-3BrCClF_Ext-3BrCClF-R
Total Standard Deviation in ln(k): 13.021641727496226
""",
)

entry(
    index = 367,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_1ClFO->F_Ext-3BrCClF-R_5R!H->Cl_Ext-3BrCClF-R_6R!H->Cl",
    kinetics = ArrheniusBM(A=(2.3677,'m^3/(mol*s)'), n=1.17475, w0=(288770,'J/mol'), E0=(18555.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_1ClFO->F_Ext-3BrCClF-R_5R!H->Cl_Ext-3BrCClF-R_6R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_1ClFO->F_Ext-3BrCClF-R_5R!H->Cl_Ext-3BrCClF-R_6R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_1ClFO->F_Ext-3BrCClF-R_5R!H->Cl_Ext-3BrCClF-R_6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_1ClFO->F_Ext-3BrCClF-R_5R!H->Cl_Ext-3BrCClF-R_6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 368,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_1ClFO->F_Ext-3BrCClF-R_5R!H->Cl_Ext-3BrCClF-R_N-6R!H->Cl",
    kinetics = ArrheniusBM(A=(1.75749,'m^3/(mol*s)'), n=1.13344, w0=(288770,'J/mol'), E0=(12087.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_1ClFO->F_Ext-3BrCClF-R_5R!H->Cl_Ext-3BrCClF-R_N-6R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_1ClFO->F_Ext-3BrCClF-R_5R!H->Cl_Ext-3BrCClF-R_N-6R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_1ClFO->F_Ext-3BrCClF-R_5R!H->Cl_Ext-3BrCClF-R_N-6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_1ClFO->F_Ext-3BrCClF-R_5R!H->Cl_Ext-3BrCClF-R_N-6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 369,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_5R!H->F",
    kinetics = ArrheniusBM(A=(2.10975e+32,'m^3/(mol*s)'), n=-8.40691, w0=(299500,'J/mol'), E0=(11074.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-7.751089999242703, var=9.796202993666792, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_5R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_5R!H->F
    Total Standard Deviation in ln(k): 25.74969807593661"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_5R!H->F
Total Standard Deviation in ln(k): 25.74969807593661""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_5R!H->F
Total Standard Deviation in ln(k): 25.74969807593661
""",
)

entry(
    index = 370,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(3909.39,'m^3/(mol*s)'), n=0.727444, w0=(299500,'J/mol'), E0=(43659.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.09178259082134593, var=2.4130054164351145, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F
    Total Standard Deviation in ln(k): 3.344735218548227"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F
Total Standard Deviation in ln(k): 3.344735218548227""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F
Total Standard Deviation in ln(k): 3.344735218548227
""",
)

entry(
    index = 371,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_N-1ClO->O_Ext-3BrCClF-R",
    kinetics = ArrheniusBM(A=(0.629376,'m^3/(mol*s)'), n=1.78262, w0=(283500,'J/mol'), E0=(27011,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2478109154148313, var=1.1670342552695678, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_N-1ClO->O_Ext-3BrCClF-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_N-1ClO->O_Ext-3BrCClF-R
    Total Standard Deviation in ln(k): 2.788342958365024"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_N-1ClO->O_Ext-3BrCClF-R
Total Standard Deviation in ln(k): 2.788342958365024""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_N-1ClO->O_Ext-3BrCClF-R
Total Standard Deviation in ln(k): 2.788342958365024
""",
)

entry(
    index = 372,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R_Ext-3BrCClF-R_1ClFO->Cl",
    kinetics = ArrheniusBM(A=(8.86124e+14,'m^3/(mol*s)'), n=-2.35726, w0=(283500,'J/mol'), E0=(90678.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.8693838208947646, var=19.67050991415716, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R_Ext-3BrCClF-R_1ClFO->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R_Ext-3BrCClF-R_1ClFO->Cl
    Total Standard Deviation in ln(k): 11.075671930304635"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R_Ext-3BrCClF-R_1ClFO->Cl
Total Standard Deviation in ln(k): 11.075671930304635""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R_Ext-3BrCClF-R_1ClFO->Cl
Total Standard Deviation in ln(k): 11.075671930304635
""",
)

entry(
    index = 373,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R_Ext-3BrCClF-R_N-1ClFO->Cl",
    kinetics = ArrheniusBM(A=(5.80357e+15,'m^3/(mol*s)'), n=-2.97426, w0=(294135,'J/mol'), E0=(-8911.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.290895095126207, var=0.6611342121643728, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R_Ext-3BrCClF-R_N-1ClFO->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R_Ext-3BrCClF-R_N-1ClFO->Cl
    Total Standard Deviation in ln(k): 9.898633940324014"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R_Ext-3BrCClF-R_N-1ClFO->Cl
Total Standard Deviation in ln(k): 9.898633940324014""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R_Ext-3BrCClF-R_N-1ClFO->Cl
Total Standard Deviation in ln(k): 9.898633940324014
""",
)

entry(
    index = 374,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_N-3BrClF->Br_N-1ClFO->Cl_1FO->O_3ClF->F",
    kinetics = ArrheniusBM(A=(7.2e+06,'m^3/(mol*s)'), n=0, w0=(261270,'J/mol'), E0=(6019.14,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_N-3BrClF->Br_N-1ClFO->Cl_1FO->O_3ClF->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_N-3BrClF->Br_N-1ClFO->Cl_1FO->O_3ClF->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_N-3BrClF->Br_N-1ClFO->Cl_1FO->O_3ClF->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_N-3BrClF->Br_N-1ClFO->Cl_1FO->O_3ClF->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 375,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_N-3BrClF->Br_N-1ClFO->Cl_1FO->O_N-3ClF->F",
    kinetics = ArrheniusBM(A=(95506.5,'m^3/(mol*s)'), n=0.473217, w0=(256000,'J/mol'), E0=(1995.04,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.16458173119139988, var=1.0888799341665543, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_N-3BrClF->Br_N-1ClFO->Cl_1FO->O_N-3ClF->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_N-3BrClF->Br_N-1ClFO->Cl_1FO->O_N-3ClF->F
    Total Standard Deviation in ln(k): 2.5054511605236214"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_N-3BrClF->Br_N-1ClFO->Cl_1FO->O_N-3ClF->F
Total Standard Deviation in ln(k): 2.5054511605236214""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_N-3BrCClF->C_N-3BrClF->Br_N-1ClFO->Cl_1FO->O_N-3ClF->F
Total Standard Deviation in ln(k): 2.5054511605236214
""",
)

entry(
    index = 376,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_4BrCClINOPSSi->O",
    kinetics = ArrheniusBM(A=(4.61982,'m^3/(mol*s)'), n=1.59815, w0=(299500,'J/mol'), E0=(48938,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_4BrCClINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_4BrCClINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_4BrCClINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_4BrCClINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 377,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_N-4BrCClINOPSSi->O",
    kinetics = ArrheniusBM(A=(1.31901e-13,'m^3/(mol*s)'), n=4.91785, w0=(299500,'J/mol'), E0=(-5116.06,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4730159422220372, var=5.854124617861466, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_N-4BrCClINOPSSi->O',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_N-4BrCClINOPSSi->O
    Total Standard Deviation in ln(k): 6.03899859601261"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_N-4BrCClINOPSSi->O
Total Standard Deviation in ln(k): 6.03899859601261""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_N-4BrCClINOPSSi->O
Total Standard Deviation in ln(k): 6.03899859601261
""",
)

entry(
    index = 378,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_4BrCClINOPSSi->Cl_Ext-3BrCClF-R_5R!H->C",
    kinetics = ArrheniusBM(A=(0.00205139,'m^3/(mol*s)'), n=2.91659, w0=(299500,'J/mol'), E0=(57268.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_4BrCClINOPSSi->Cl_Ext-3BrCClF-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_4BrCClINOPSSi->Cl_Ext-3BrCClF-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_4BrCClINOPSSi->Cl_Ext-3BrCClF-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_4BrCClINOPSSi->Cl_Ext-3BrCClF-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 379,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_4BrCClINOPSSi->Cl_Ext-3BrCClF-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(37244.9,'m^3/(mol*s)'), n=0.149257, w0=(299500,'J/mol'), E0=(35150.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_4BrCClINOPSSi->Cl_Ext-3BrCClF-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_4BrCClINOPSSi->Cl_Ext-3BrCClF-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_4BrCClINOPSSi->Cl_Ext-3BrCClF-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_4BrCClINOPSSi->Cl_Ext-3BrCClF-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 380,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_N-4BrCClINOPSSi->Cl_Ext-4CO-R",
    kinetics = ArrheniusBM(A=(0.000430651,'m^3/(mol*s)'), n=2.78666, w0=(299500,'J/mol'), E0=(58984,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_N-4BrCClINOPSSi->Cl_Ext-4CO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_N-4BrCClINOPSSi->Cl_Ext-4CO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_N-4BrCClINOPSSi->Cl_Ext-4CO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_N-4BrCClINOPSSi->Cl_Ext-4CO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 381,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C_Ext-6C-R",
    kinetics = ArrheniusBM(A=(2.00161e-12,'m^3/(mol*s)'), n=4.75486, w0=(377500,'J/mol'), E0=(24619,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2061227234603807, var=2.146600970621064, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C_Ext-6C-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C_Ext-6C-R
    Total Standard Deviation in ln(k): 3.455090410049128"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C_Ext-6C-R
Total Standard Deviation in ln(k): 3.455090410049128""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C_Ext-6C-R
Total Standard Deviation in ln(k): 3.455090410049128
""",
)

entry(
    index = 382,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->O_5CF->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(4.90176e-06,'m^3/(mol*s)'), n=3.11083, w0=(377500,'J/mol'), E0=(59315.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.019918687470238047, var=5.660341859628158, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->O_5CF->C_Ext-5C-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->O_5CF->C_Ext-5C-R
    Total Standard Deviation in ln(k): 4.819606993522996"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->O_5CF->C_Ext-5C-R
Total Standard Deviation in ln(k): 4.819606993522996""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->O_5CF->C_Ext-5C-R
Total Standard Deviation in ln(k): 4.819606993522996
""",
)

entry(
    index = 383,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->O_5CF->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.24197e-07,'m^3/(mol*s)'), n=3.47473, w0=(377500,'J/mol'), E0=(54197.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->O_5CF->C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->O_5CF->C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->O_5CF->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->O_5CF->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 384,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R",
    kinetics = ArrheniusBM(A=(0.725045,'m^3/(mol*s)'), n=0.821199, w0=(377500,'J/mol'), E0=(81745.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 385,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(45.927,'m^3/(mol*s)'), n=1.27853, w0=(377500,'J/mol'), E0=(68096.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00019387291237111165, var=0.13205268767072018, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 0.728988888777895"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 0.728988888777895""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 0.728988888777895
""",
)

entry(
    index = 386,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi_Sp-4BrCFINOPSSi-3C_5BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.00460907,'m^3/(mol*s)'), n=2.46786, w0=(377500,'J/mol'), E0=(66556.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi_Sp-4BrCFINOPSSi-3C_5BrCClINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi_Sp-4BrCFINOPSSi-3C_5BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi_Sp-4BrCFINOPSSi-3C_5BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi_Sp-4BrCFINOPSSi-3C_5BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 387,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi_Sp-4BrCFINOPSSi-3C_N-5BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(105.403,'m^3/(mol*s)'), n=1.02966, w0=(377500,'J/mol'), E0=(68561.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.743272305068362e-15, var=0.4118215425457979, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi_Sp-4BrCFINOPSSi-3C_N-5BrCClINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi_Sp-4BrCFINOPSSi-3C_N-5BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 1.2865051228513575"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi_Sp-4BrCFINOPSSi-3C_N-5BrCClINOPSSi->C
Total Standard Deviation in ln(k): 1.2865051228513575""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi_Sp-4BrCFINOPSSi-3C_N-5BrCClINOPSSi->C
Total Standard Deviation in ln(k): 1.2865051228513575
""",
)

entry(
    index = 388,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi_N-Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(223.135,'m^3/(mol*s)'), n=0.451611, w0=(377500,'J/mol'), E0=(76040.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi_N-Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi_N-Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi_N-Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi_N-Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 389,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_N-Sp-4CCFFOO=3C_N-4CFO->O_Ext-3C-R_4CF->C",
    kinetics = ArrheniusBM(A=(0.344305,'m^3/(mol*s)'), n=2.09545, w0=(377500,'J/mol'), E0=(67803,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=8.997534477772192e-16, var=16.282486288094255, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_N-Sp-4CCFFOO=3C_N-4CFO->O_Ext-3C-R_4CF->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_N-Sp-4CCFFOO=3C_N-4CFO->O_Ext-3C-R_4CF->C
    Total Standard Deviation in ln(k): 8.089419358167142"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_N-Sp-4CCFFOO=3C_N-4CFO->O_Ext-3C-R_4CF->C
Total Standard Deviation in ln(k): 8.089419358167142""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_N-Sp-4CCFFOO=3C_N-4CFO->O_Ext-3C-R_4CF->C
Total Standard Deviation in ln(k): 8.089419358167142
""",
)

entry(
    index = 390,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_N-Sp-4CCFFOO=3C_N-4CFO->O_Ext-3C-R_N-4CF->C",
    kinetics = ArrheniusBM(A=(15.0263,'m^3/(mol*s)'), n=1.2903, w0=(377500,'J/mol'), E0=(72320.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.005998997841474389, var=3.9512308049560576, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_N-Sp-4CCFFOO=3C_N-4CFO->O_Ext-3C-R_N-4CF->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_N-Sp-4CCFFOO=3C_N-4CFO->O_Ext-3C-R_N-4CF->C
    Total Standard Deviation in ln(k): 4.000025724975527"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_N-Sp-4CCFFOO=3C_N-4CFO->O_Ext-3C-R_N-4CF->C
Total Standard Deviation in ln(k): 4.000025724975527""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_N-Sp-4CCFFOO=3C_N-4CFO->O_Ext-3C-R_N-4CF->C
Total Standard Deviation in ln(k): 4.000025724975527
""",
)

entry(
    index = 391,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->F_Ext-1C-R_6R!H->Cl",
    kinetics = ArrheniusBM(A=(2.5e+06,'m^3/(mol*s)'), n=0, w0=(377500,'J/mol'), E0=(82359.9,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->F_Ext-1C-R_6R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->F_Ext-1C-R_6R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->F_Ext-1C-R_6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->F_Ext-1C-R_6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 392,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->F_Ext-1C-R_N-6R!H->Cl",
    kinetics = ArrheniusBM(A=(0.203436,'m^3/(mol*s)'), n=2.31689, w0=(377500,'J/mol'), E0=(67279.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.10548746838489194, var=0.8130276953949701, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->F_Ext-1C-R_N-6R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->F_Ext-1C-R_N-6R!H->Cl
    Total Standard Deviation in ln(k): 2.0726743854781327"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->F_Ext-1C-R_N-6R!H->Cl
Total Standard Deviation in ln(k): 2.0726743854781327""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->F_Ext-1C-R_N-6R!H->Cl
Total Standard Deviation in ln(k): 2.0726743854781327
""",
)

entry(
    index = 393,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_5R!H->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.9091,'m^3/(mol*s)'), n=1.95961, w0=(377500,'J/mol'), E0=(55555.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.15555708409255045, var=2.135310785284623, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_5R!H->Cl_Ext-1C-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_5R!H->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 3.3203067013220267"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_5R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 3.3203067013220267""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_5R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 3.3203067013220267
""",
)

entry(
    index = 394,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_5R!H->Cl_Ext-4C-R",
    kinetics = ArrheniusBM(A=(2.08288e+08,'m^3/(mol*s)'), n=-0.159444, w0=(377500,'J/mol'), E0=(68541.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00031093622434279986, var=0.01841489794949468, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_5R!H->Cl_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_5R!H->Cl_Ext-4C-R
    Total Standard Deviation in ln(k): 0.2728268101580565"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_5R!H->Cl_Ext-4C-R
Total Standard Deviation in ln(k): 0.2728268101580565""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_5R!H->Cl_Ext-4C-R
Total Standard Deviation in ln(k): 0.2728268101580565
""",
)

entry(
    index = 395,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_N-5R!H->Cl_Ext-4C-R",
    kinetics = ArrheniusBM(A=(1e+06,'m^3/(mol*s)'), n=0, w0=(377500,'J/mol'), E0=(68663.2,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_N-5R!H->Cl_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_N-5R!H->Cl_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_N-5R!H->Cl_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_N-5R!H->Cl_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 396,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_N-5R!H->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(17.8736,'m^3/(mol*s)'), n=1.94617, w0=(377500,'J/mol'), E0=(76893.3,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_N-5R!H->Cl_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_N-5R!H->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_N-5R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_N-5R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 397,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-1C-R_5R!H->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.81352,'m^3/(mol*s)'), n=2.14168, w0=(377500,'J/mol'), E0=(66287,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.056789502117612675, var=0.20722286937706325, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-1C-R_5R!H->Cl_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-1C-R_5R!H->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 1.0552774546986878"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-1C-R_5R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 1.0552774546986878""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-1C-R_5R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 1.0552774546986878
""",
)

entry(
    index = 398,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(18942.8,'m^3/(mol*s)'), n=1.11114, w0=(377500,'J/mol'), E0=(63198.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-4.498767238886096e-16, var=16.28248628809398, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 8.089419358167072"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 8.089419358167072""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 8.089419358167072
""",
)

entry(
    index = 399,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(43.7292,'m^3/(mol*s)'), n=1.85998, w0=(377500,'J/mol'), E0=(56644.5,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 400,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_N-4BrCClO->C_N-4ClO->O_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(300000,'m^3/(mol*s)'), n=0, w0=(377500,'J/mol'), E0=(37750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_N-4BrCClO->C_N-4ClO->O_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_N-4BrCClO->C_N-4ClO->O_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_N-4BrCClO->C_N-4ClO->O_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_N-4BrCClO->C_N-4ClO->O_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 401,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_5CF->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(623828,'m^3/(mol*s)'), n=-0.252248, w0=(327000,'J/mol'), E0=(73988.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_5CF->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_5CF->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_5CF->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_5CF->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 402,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C_Ext-3CClFO-R",
    kinetics = ArrheniusBM(A=(463855,'m^3/(mol*s)'), n=-0.258071, w0=(327000,'J/mol'), E0=(71990.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.011058911992283206, var=1.3213830926387578, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C_Ext-3CClFO-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C_Ext-3CClFO-R
    Total Standard Deviation in ln(k): 2.3322578212045912"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C_Ext-3CClFO-R
Total Standard Deviation in ln(k): 2.3322578212045912""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C_Ext-3CClFO-R
Total Standard Deviation in ln(k): 2.3322578212045912
""",
)

entry(
    index = 403,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_5R!H->C_N-6R!H->C_Ext-5C-R_7R!H->Cl",
    kinetics = ArrheniusBM(A=(0.00443575,'m^3/(mol*s)'), n=1.48341, w0=(327000,'J/mol'), E0=(56558.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_5R!H->C_N-6R!H->C_Ext-5C-R_7R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_5R!H->C_N-6R!H->C_Ext-5C-R_7R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_5R!H->C_N-6R!H->C_Ext-5C-R_7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_5R!H->C_N-6R!H->C_Ext-5C-R_7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 404,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_5R!H->C_N-6R!H->C_Ext-5C-R_N-7R!H->Cl",
    kinetics = ArrheniusBM(A=(0.266114,'m^3/(mol*s)'), n=1.37524, w0=(327000,'J/mol'), E0=(55569.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_5R!H->C_N-6R!H->C_Ext-5C-R_N-7R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_5R!H->C_N-6R!H->C_Ext-5C-R_N-7R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_5R!H->C_N-6R!H->C_Ext-5C-R_N-7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-3CClFO-R_Ext-3CClFO-R_5R!H->C_N-6R!H->C_Ext-5C-R_N-7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 405,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(0.971493,'m^3/(mol*s)'), n=1.60662, w0=(327000,'J/mol'), E0=(54966.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.09993456458810462, var=2.9336181132776584, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl
    Total Standard Deviation in ln(k): 3.6847636464726823"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl
Total Standard Deviation in ln(k): 3.6847636464726823""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl
Total Standard Deviation in ln(k): 3.6847636464726823
""",
)

entry(
    index = 406,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(49132.4,'m^3/(mol*s)'), n=0.534804, w0=(327000,'J/mol'), E0=(50661.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.03559456983627841, var=1.126225608691662, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_N-5R!H->Cl',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 2.2169341795111452"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 2.2169341795111452""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 2.2169341795111452
""",
)

entry(
    index = 407,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_N-4BrCFINOPSSi->C_Ext-3C-R_4BrFO->Br",
    kinetics = ArrheniusBM(A=(232.18,'m^3/(mol*s)'), n=0.993804, w0=(327000,'J/mol'), E0=(49144.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_N-4BrCFINOPSSi->C_Ext-3C-R_4BrFO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_N-4BrCFINOPSSi->C_Ext-3C-R_4BrFO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_N-4BrCFINOPSSi->C_Ext-3C-R_4BrFO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_N-4BrCFINOPSSi->C_Ext-3C-R_4BrFO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 408,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_N-4BrCFINOPSSi->C_Ext-3C-R_N-4BrFO->Br",
    kinetics = ArrheniusBM(A=(190000,'m^3/(mol*s)'), n=0, w0=(327000,'J/mol'), E0=(63841.4,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_N-4BrCFINOPSSi->C_Ext-3C-R_N-4BrFO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_N-4BrCFINOPSSi->C_Ext-3C-R_N-4BrFO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_N-4BrCFINOPSSi->C_Ext-3C-R_N-4BrFO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_N-4BrCFINOPSSi->C_Ext-3C-R_N-4BrFO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 409,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R_Ext-6R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(2.68906e+11,'m^3/(mol*s)'), n=-1.42097, w0=(299500,'J/mol'), E0=(68353.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.5316007770156629, var=7.77830872230957, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R_Ext-6R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R_Ext-6R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 6.9268101819187935"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R_Ext-6R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 6.9268101819187935""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R_Ext-6R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 6.9268101819187935
""",
)

entry(
    index = 410,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R_3O-u1_Ext-5C-R",
    kinetics = ArrheniusBM(A=(666667,'m^3/(mol*s)'), n=0, w0=(299500,'J/mol'), E0=(65458.4,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R_3O-u1_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R_3O-u1_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R_3O-u1_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R_3O-u1_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 411,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R_N-3O-u1_Ext-5C-R_Ext-5C-R",
    kinetics = ArrheniusBM(A=(666667,'m^3/(mol*s)'), n=0, w0=(299500,'J/mol'), E0=(36924.7,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R_N-3O-u1_Ext-5C-R_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R_N-3O-u1_Ext-5C-R_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R_N-3O-u1_Ext-5C-R_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R_N-3O-u1_Ext-5C-R_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 412,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->O_3O-u1_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.157359,'m^3/(mol*s)'), n=2.34331, w0=(299500,'J/mol'), E0=(34188.8,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->O_3O-u1_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->O_3O-u1_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->O_3O-u1_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->O_3O-u1_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 413,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->O_3O-u1_Sp-5O-1C",
    kinetics = ArrheniusBM(A=(0.176621,'m^3/(mol*s)'), n=2.47253, w0=(299500,'J/mol'), E0=(43850.5,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->O_3O-u1_Sp-5O-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->O_3O-u1_Sp-5O-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->O_3O-u1_Sp-5O-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->O_3O-u1_Sp-5O-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 414,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->O_3O-u1_N-Sp-5O-1C",
    kinetics = ArrheniusBM(A=(5e+06,'m^3/(mol*s)'), n=0, w0=(299500,'J/mol'), E0=(45136.1,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->O_3O-u1_N-Sp-5O-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->O_3O-u1_N-Sp-5O-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->O_3O-u1_N-Sp-5O-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->O_3O-u1_N-Sp-5O-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 415,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->O_N-3O-u1_Ext-1C-R",
    kinetics = ArrheniusBM(A=(290.458,'m^3/(mol*s)'), n=1.65322, w0=(299500,'J/mol'), E0=(51387.3,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->O_N-3O-u1_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->O_N-3O-u1_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->O_N-3O-u1_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->O_N-3O-u1_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 416,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->O_5ClF->F_Ext-1C-R_6R!H->Cl",
    kinetics = ArrheniusBM(A=(200000,'m^3/(mol*s)'), n=0, w0=(299500,'J/mol'), E0=(-20023.7,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->O_5ClF->F_Ext-1C-R_6R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->O_5ClF->F_Ext-1C-R_6R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->O_5ClF->F_Ext-1C-R_6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->O_5ClF->F_Ext-1C-R_6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 417,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->O_5ClF->F_Ext-1C-R_N-6R!H->Cl",
    kinetics = ArrheniusBM(A=(301500,'m^3/(mol*s)'), n=0, w0=(299500,'J/mol'), E0=(-26903.8,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->O_5ClF->F_Ext-1C-R_N-6R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->O_5ClF->F_Ext-1C-R_N-6R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->O_5ClF->F_Ext-1C-R_N-6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->O_5ClF->F_Ext-1C-R_N-6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 418,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->O_N-5ClF->F_3O-u1",
    kinetics = ArrheniusBM(A=(1.50111e+09,'m^3/(mol*s)'), n=-0.69405, w0=(299500,'J/mol'), E0=(34329.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.249383619443048e-15, var=13.590011051830386, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->O_N-5ClF->F_3O-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->O_N-5ClF->F_3O-u1
    Total Standard Deviation in ln(k): 7.390382123060883"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->O_N-5ClF->F_3O-u1
Total Standard Deviation in ln(k): 7.390382123060883""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->O_N-5ClF->F_3O-u1
Total Standard Deviation in ln(k): 7.390382123060883
""",
)

entry(
    index = 419,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->O_N-5ClF->F_N-3O-u1",
    kinetics = ArrheniusBM(A=(75000,'m^3/(mol*s)'), n=0, w0=(299500,'J/mol'), E0=(4498.3,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->O_N-5ClF->F_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->O_N-5ClF->F_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->O_N-5ClF->F_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->O_N-5ClF->F_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 420,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3428.4,'m^3/(mol*s)'), n=0.490734, w0=(327000,'J/mol'), E0=(69158.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.04147513457240349, var=1.613719140779142, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 2.650868866844599"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 2.650868866844599""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 2.650868866844599
""",
)

entry(
    index = 421,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C_Sp-5C-1C",
    kinetics = ArrheniusBM(A=(0.00013286,'m^3/(mol*s)'), n=3.28053, w0=(327000,'J/mol'), E0=(70037.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.7870288922727993e-05, var=0.005404304799094452, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C_Sp-5C-1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C_Sp-5C-1C
    Total Standard Deviation in ln(k): 0.14744607401411086"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C_Sp-5C-1C
Total Standard Deviation in ln(k): 0.14744607401411086""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C_Sp-5C-1C
Total Standard Deviation in ln(k): 0.14744607401411086
""",
)

entry(
    index = 422,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C_N-Sp-5C-1C",
    kinetics = ArrheniusBM(A=(0.0141769,'m^3/(mol*s)'), n=2.76355, w0=(327000,'J/mol'), E0=(72170.8,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C_N-Sp-5C-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C_N-Sp-5C-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C_N-Sp-5C-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C_N-Sp-5C-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 423,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C",
    kinetics = ArrheniusBM(A=(3.81825e-19,'m^3/(mol*s)'), n=7.26603, w0=(327000,'J/mol'), E0=(16794.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.19227920924141023, var=4.022669462453007, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C
    Total Standard Deviation in ln(k): 4.503929260404748"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C
Total Standard Deviation in ln(k): 4.503929260404748""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C
Total Standard Deviation in ln(k): 4.503929260404748
""",
)

entry(
    index = 424,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_N-Sp-5BrClFINOPSSi-1C",
    kinetics = ArrheniusBM(A=(9.5e+06,'m^3/(mol*s)'), n=0, w0=(327000,'J/mol'), E0=(70135.7,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_N-Sp-5BrClFINOPSSi-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_N-Sp-5BrClFINOPSSi-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_N-Sp-5BrClFINOPSSi-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_N-Sp-5BrClFINOPSSi-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 425,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6.84025e+09,'m^3/(mol*s)'), n=-0.906082, w0=(285257,'J/mol'), E0=(34501.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1552956695081282, var=2.884763027965569, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 3.7951504906546223"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 3.7951504906546223""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 3.7951504906546223
""",
)

entry(
    index = 426,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_N-5R!H->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(5.34251e+09,'m^3/(mol*s)'), n=-0.911806, w0=(286135,'J/mol'), E0=(-17715.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4845119214808093, var=0.6842606789232818, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_N-5R!H->Cl_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_N-5R!H->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 2.8756845094799095"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_N-5R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 2.8756845094799095""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_N-5R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 2.8756845094799095
""",
)

entry(
    index = 427,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.575e+08,'m^3/(mol*s)'), n=0, w0=(283500,'J/mol'), E0=(28350,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 428,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.6e+08,'m^3/(mol*s)'), n=0, w0=(283500,'J/mol'), E0=(54802.7,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 429,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_3CClFO->C_4BrCFINOPSSi->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.00717719,'m^3/(mol*s)'), n=2.80408, w0=(327000,'J/mol'), E0=(70434.6,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_3CClFO->C_4BrCFINOPSSi->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_3CClFO->C_4BrCFINOPSSi->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_3CClFO->C_4BrCFINOPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_3CClFO->C_4BrCFINOPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 430,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C_3ClFO-u1_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.00191607,'m^3/(mol*s)'), n=2.86987, w0=(291500,'J/mol'), E0=(-27882.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.747804554012546, var=1.9363394764708726, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C_3ClFO-u1_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C_3ClFO-u1_Ext-1C-R
    Total Standard Deviation in ln(k): 12.206231643202159"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C_3ClFO-u1_Ext-1C-R
Total Standard Deviation in ln(k): 12.206231643202159""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C_3ClFO-u1_Ext-1C-R
Total Standard Deviation in ln(k): 12.206231643202159
""",
)

entry(
    index = 431,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C_3ClFO-u1_4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.72691e+36,'m^3/(mol*s)'), n=-8.44925, w0=(291500,'J/mol'), E0=(131645,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.3009601976563725, var=61.86687707008711, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C_3ClFO-u1_4BrCFINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C_3ClFO-u1_4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 19.037088237315132"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C_3ClFO-u1_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 19.037088237315132""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C_3ClFO-u1_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 19.037088237315132
""",
)

entry(
    index = 432,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C_3ClFO-u1_N-4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.47448e+09,'m^3/(mol*s)'), n=-0.546971, w0=(283500,'J/mol'), E0=(37589,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C_3ClFO-u1_N-4BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C_3ClFO-u1_N-4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C_3ClFO-u1_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C_3ClFO-u1_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 433,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_4BrCFINOPSSi->Br_N-3CClFO->Cl_3CFO->C",
    kinetics = ArrheniusBM(A=(1.26e+06,'m^3/(mol*s)'), n=0, w0=(327000,'J/mol'), E0=(57627.8,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_4BrCFINOPSSi->Br_N-3CClFO->Cl_3CFO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_4BrCFINOPSSi->Br_N-3CClFO->Cl_3CFO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_4BrCFINOPSSi->Br_N-3CClFO->Cl_3CFO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_4BrCFINOPSSi->Br_N-3CClFO->Cl_3CFO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 434,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_4BrCFINOPSSi->Br_N-3CClFO->Cl_N-3CFO->C",
    kinetics = ArrheniusBM(A=(6.07546e+24,'m^3/(mol*s)'), n=-5.47668, w0=(299500,'J/mol'), E0=(44809.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.207882010466994, var=1.414745191794855, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_4BrCFINOPSSi->Br_N-3CClFO->Cl_N-3CFO->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_4BrCFINOPSSi->Br_N-3CClFO->Cl_N-3CFO->C
    Total Standard Deviation in ln(k): 7.931935516654148"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_4BrCFINOPSSi->Br_N-3CClFO->Cl_N-3CFO->C
Total Standard Deviation in ln(k): 7.931935516654148""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_4BrCFINOPSSi->Br_N-3CClFO->Cl_N-3CFO->C
Total Standard Deviation in ln(k): 7.931935516654148
""",
)

entry(
    index = 435,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_3CClFO->F",
    kinetics = ArrheniusBM(A=(3.15e+07,'m^3/(mol*s)'), n=0, w0=(288770,'J/mol'), E0=(23052.9,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_3CClFO->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_3CClFO->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_3CClFO->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_3CClFO->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 436,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F",
    kinetics = ArrheniusBM(A=(1.18855e+30,'m^3/(mol*s)'), n=-6.85646, w0=(311250,'J/mol'), E0=(119730,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.4684301200962865, var=15.949816831298314, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F
    Total Standard Deviation in ln(k): 9.183315039406551"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F
Total Standard Deviation in ln(k): 9.183315039406551""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F
Total Standard Deviation in ln(k): 9.183315039406551
""",
)

entry(
    index = 437,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_3CClFO->C_4CFO->C",
    kinetics = ArrheniusBM(A=(0.00026643,'m^3/(mol*s)'), n=3.22769, w0=(327000,'J/mol'), E0=(74142.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.004169354070088563, var=0.8869135175636432, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_3CClFO->C_4CFO->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_3CClFO->C_4CFO->C
    Total Standard Deviation in ln(k): 1.8984567946985005"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_3CClFO->C_4CFO->C
Total Standard Deviation in ln(k): 1.8984567946985005""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_3CClFO->C_4CFO->C
Total Standard Deviation in ln(k): 1.8984567946985005
""",
)

entry(
    index = 438,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_3CClFO->C_N-4CFO->C",
    kinetics = ArrheniusBM(A=(0.00435666,'m^3/(mol*s)'), n=2.88851, w0=(327000,'J/mol'), E0=(73122.8,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_3CClFO->C_N-4CFO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_3CClFO->C_N-4CFO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_3CClFO->C_N-4CFO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_3CClFO->C_N-4CFO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 439,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_N-3CClFO->C_Ext-4CFO-R",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=0, w0=(283500,'J/mol'), E0=(23236.1,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_N-3CClFO->C_Ext-4CFO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_N-3CClFO->C_Ext-4CFO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_N-3CClFO->C_Ext-4CFO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_N-3CClFO->C_Ext-4CFO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 440,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_N-3O-u1_N-1BrO->Br_Ext-1O-R_4R!H->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(0.0308162,'m^3/(mol*s)'), n=2.73613, w0=(272000,'J/mol'), E0=(27200,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.9493663578396799, var=0.920324346967258, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_N-3O-u1_N-1BrO->Br_Ext-1O-R_4R!H->C_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_N-3O-u1_N-1BrO->Br_Ext-1O-R_4R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 4.3085558694637704"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_N-3O-u1_N-1BrO->Br_Ext-1O-R_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 4.3085558694637704""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_N-3O-u1_N-1BrO->Br_Ext-1O-R_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 4.3085558694637704
""",
)

entry(
    index = 441,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_1ClFO->O_N-5R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R",
    kinetics = ArrheniusBM(A=(2.02032e-06,'m^3/(mol*s)'), n=3.25872, w0=(299500,'J/mol'), E0=(38107.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0017978332384043748, var=4.329654512535134, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_1ClFO->O_N-5R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_1ClFO->O_N-5R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R
    Total Standard Deviation in ln(k): 4.1759342089846685"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_1ClFO->O_N-5R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R
Total Standard Deviation in ln(k): 4.1759342089846685""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_1ClFO->O_N-5R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R
Total Standard Deviation in ln(k): 4.1759342089846685
""",
)

entry(
    index = 442,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_1ClFO->O_N-5R!H->F_Ext-3BrCClF-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(6.25964e-08,'m^3/(mol*s)'), n=4.02374, w0=(299500,'J/mol'), E0=(23063.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_1ClFO->O_N-5R!H->F_Ext-3BrCClF-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_1ClFO->O_N-5R!H->F_Ext-3BrCClF-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_1ClFO->O_N-5R!H->F_Ext-3BrCClF-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_1ClFO->O_N-5R!H->F_Ext-3BrCClF-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 443,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_N-1ClFO->O_Sp-4R!H-3BrCClF_Ext-3BrCClF-R_5R!H->F",
    kinetics = ArrheniusBM(A=(630000,'m^3/(mol*s)'), n=0, w0=(283500,'J/mol'), E0=(43458.3,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_N-1ClFO->O_Sp-4R!H-3BrCClF_Ext-3BrCClF-R_5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_N-1ClFO->O_Sp-4R!H-3BrCClF_Ext-3BrCClF-R_5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_N-1ClFO->O_Sp-4R!H-3BrCClF_Ext-3BrCClF-R_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_N-1ClFO->O_Sp-4R!H-3BrCClF_Ext-3BrCClF-R_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 444,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_N-1ClFO->O_Sp-4R!H-3BrCClF_Ext-3BrCClF-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(0.0423683,'m^3/(mol*s)'), n=1.56229, w0=(283500,'J/mol'), E0=(33175.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_N-1ClFO->O_Sp-4R!H-3BrCClF_Ext-3BrCClF-R_N-5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_N-1ClFO->O_Sp-4R!H-3BrCClF_Ext-3BrCClF-R_N-5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_N-1ClFO->O_Sp-4R!H-3BrCClF_Ext-3BrCClF-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_N-1ClFO->O_Sp-4R!H-3BrCClF_Ext-3BrCClF-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 445,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_5R!H->F_Ext-3BrCClF-R_6R!H->Cl",
    kinetics = ArrheniusBM(A=(3.421,'m^3/(mol*s)'), n=0.936125, w0=(299500,'J/mol'), E0=(-20042.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_5R!H->F_Ext-3BrCClF-R_6R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_5R!H->F_Ext-3BrCClF-R_6R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_5R!H->F_Ext-3BrCClF-R_6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_5R!H->F_Ext-3BrCClF-R_6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 446,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_5R!H->F_Ext-3BrCClF-R_N-6R!H->Cl",
    kinetics = ArrheniusBM(A=(8.81719,'m^3/(mol*s)'), n=0.91303, w0=(299500,'J/mol'), E0=(-26845.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_5R!H->F_Ext-3BrCClF-R_N-6R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_5R!H->F_Ext-3BrCClF-R_N-6R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_5R!H->F_Ext-3BrCClF-R_N-6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_5R!H->F_Ext-3BrCClF-R_N-6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 447,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F_5BrCClINOPSSi->Cl",
    kinetics = ArrheniusBM(A=(0.00111862,'m^3/(mol*s)'), n=2.47098, w0=(299500,'J/mol'), E0=(-6622.36,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.439310500891337, var=15.668394289742418, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F_5BrCClINOPSSi->Cl',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F_5BrCClINOPSSi->Cl
    Total Standard Deviation in ln(k): 14.06432838843979"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F_5BrCClINOPSSi->Cl
Total Standard Deviation in ln(k): 14.06432838843979""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F_5BrCClINOPSSi->Cl
Total Standard Deviation in ln(k): 14.06432838843979
""",
)

entry(
    index = 448,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F_N-5BrCClINOPSSi->Cl",
    kinetics = ArrheniusBM(A=(5.31143,'m^3/(mol*s)'), n=1.68882, w0=(299500,'J/mol'), E0=(41140.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.12307201892259666, var=2.1214003892381674, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F_N-5BrCClINOPSSi->Cl',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F_N-5BrCClINOPSSi->Cl
    Total Standard Deviation in ln(k): 3.2291284198640557"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F_N-5BrCClINOPSSi->Cl
Total Standard Deviation in ln(k): 3.2291284198640557""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F_N-5BrCClINOPSSi->Cl
Total Standard Deviation in ln(k): 3.2291284198640557
""",
)

entry(
    index = 449,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_N-1ClO->O_Ext-3BrCClF-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(0.00502776,'m^3/(mol*s)'), n=2.31491, w0=(283500,'J/mol'), E0=(-969.137,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.5953511635575963, var=18.888040288824254, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_N-1ClO->O_Ext-3BrCClF-R_5R!H->Cl',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_N-1ClO->O_Ext-3BrCClF-R_5R!H->Cl
    Total Standard Deviation in ln(k): 15.2336362634724"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_N-1ClO->O_Ext-3BrCClF-R_5R!H->Cl
Total Standard Deviation in ln(k): 15.2336362634724""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_N-1ClO->O_Ext-3BrCClF-R_5R!H->Cl
Total Standard Deviation in ln(k): 15.2336362634724
""",
)

entry(
    index = 450,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_N-1ClO->O_Ext-3BrCClF-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(0.0235853,'m^3/(mol*s)'), n=2.28238, w0=(283500,'J/mol'), E0=(22987.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03594039195680618, var=0.8922572147249155, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_N-1ClO->O_Ext-3BrCClF-R_N-5R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_N-1ClO->O_Ext-3BrCClF-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 1.9839625706228285"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_N-1ClO->O_Ext-3BrCClF-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 1.9839625706228285""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_N-1ClO->O_Ext-3BrCClF-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 1.9839625706228285
""",
)

entry(
    index = 451,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R_Ext-3BrCClF-R_1ClFO->Cl_4BrCFO->Br",
    kinetics = ArrheniusBM(A=(1598.59,'m^3/(mol*s)'), n=1.07268, w0=(283500,'J/mol'), E0=(71845,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R_Ext-3BrCClF-R_1ClFO->Cl_4BrCFO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R_Ext-3BrCClF-R_1ClFO->Cl_4BrCFO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R_Ext-3BrCClF-R_1ClFO->Cl_4BrCFO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R_Ext-3BrCClF-R_1ClFO->Cl_4BrCFO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 452,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R_Ext-3BrCClF-R_1ClFO->Cl_N-4BrCFO->Br",
    kinetics = ArrheniusBM(A=(1922.29,'m^3/(mol*s)'), n=1.03486, w0=(283500,'J/mol'), E0=(28350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R_Ext-3BrCClF-R_1ClFO->Cl_N-4BrCFO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R_Ext-3BrCClF-R_1ClFO->Cl_N-4BrCFO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R_Ext-3BrCClF-R_1ClFO->Cl_N-4BrCFO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R_Ext-3BrCClF-R_1ClFO->Cl_N-4BrCFO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 453,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R_Ext-3BrCClF-R_N-1ClFO->Cl_1FO->O",
    kinetics = ArrheniusBM(A=(209.844,'m^3/(mol*s)'), n=0.907875, w0=(299500,'J/mol'), E0=(22308.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R_Ext-3BrCClF-R_N-1ClFO->Cl_1FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R_Ext-3BrCClF-R_N-1ClFO->Cl_1FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R_Ext-3BrCClF-R_N-1ClFO->Cl_1FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R_Ext-3BrCClF-R_N-1ClFO->Cl_1FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 454,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R_Ext-3BrCClF-R_N-1ClFO->Cl_N-1FO->O",
    kinetics = ArrheniusBM(A=(243.063,'m^3/(mol*s)'), n=1.06738, w0=(288770,'J/mol'), E0=(23045.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R_Ext-3BrCClF-R_N-1ClFO->Cl_N-1FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R_Ext-3BrCClF-R_N-1ClFO->Cl_N-1FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R_Ext-3BrCClF-R_N-1ClFO->Cl_N-1FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_N-4R!H->Cl_Ext-3BrCClF-R_Ext-3BrCClF-R_N-1ClFO->Cl_N-1FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 455,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_N-4BrCClINOPSSi->O_4CCl->C",
    kinetics = ArrheniusBM(A=(0.000785201,'m^3/(mol*s)'), n=2.30876, w0=(299500,'J/mol'), E0=(52708.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.24744740339616736, var=6.757090681600176, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_N-4BrCClINOPSSi->O_4CCl->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_N-4BrCClINOPSSi->O_4CCl->C
    Total Standard Deviation in ln(k): 5.832916606915056"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_N-4BrCClINOPSSi->O_4CCl->C
Total Standard Deviation in ln(k): 5.832916606915056""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_N-4BrCClINOPSSi->O_4CCl->C
Total Standard Deviation in ln(k): 5.832916606915056
""",
)

entry(
    index = 456,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_N-4BrCClINOPSSi->O_N-4CCl->C",
    kinetics = ArrheniusBM(A=(17.4387,'m^3/(mol*s)'), n=0.395704, w0=(299500,'J/mol'), E0=(4536.49,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_N-4BrCClINOPSSi->O_N-4CCl->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_N-4BrCClINOPSSi->O_N-4CCl->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_N-4BrCClINOPSSi->O_N-4CCl->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_N-4BrCClINOPSSi->O_N-4CCl->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 457,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C_Ext-6C-R_Ext-6C-R",
    kinetics = ArrheniusBM(A=(3.60001e-11,'m^3/(mol*s)'), n=4.26558, w0=(377500,'J/mol'), E0=(27821.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1436206686835173, var=0.46028208338840637, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C_Ext-6C-R_Ext-6C-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C_Ext-6C-R_Ext-6C-R
    Total Standard Deviation in ln(k): 1.720950263883745"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C_Ext-6C-R_Ext-6C-R
Total Standard Deviation in ln(k): 1.720950263883745""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C_Ext-6C-R_Ext-6C-R
Total Standard Deviation in ln(k): 1.720950263883745
""",
)

entry(
    index = 458,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->O_5CF->C_Ext-5C-R_Ext-5C-R",
    kinetics = ArrheniusBM(A=(2.83327,'m^3/(mol*s)'), n=0.843456, w0=(377500,'J/mol'), E0=(47771.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->O_5CF->C_Ext-5C-R_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->O_5CF->C_Ext-5C-R_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->O_5CF->C_Ext-5C-R_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->O_5CF->C_Ext-5C-R_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 459,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->O_5CF->C_Ext-5C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(3.97108e-05,'m^3/(mol*s)'), n=2.90057, w0=(377500,'J/mol'), E0=(64016,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->O_5CF->C_Ext-5C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->O_5CF->C_Ext-5C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->O_5CF->C_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->O_5CF->C_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 460,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->O_5CF->C_Ext-5C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(543.729,'m^3/(mol*s)'), n=0.762756, w0=(377500,'J/mol'), E0=(67707.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->O_5CF->C_Ext-5C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->O_5CF->C_Ext-5C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->O_5CF->C_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->O_5CF->C_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 461,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(499.498,'m^3/(mol*s)'), n=0.845669, w0=(377500,'J/mol'), E0=(60923.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_Ext-4BrCFINOPSSi-R_N-5R!H->F_Sp-5BrCClINOPSSi-4BrBrCCClFIINNOOPPSSSiSi_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 462,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_N-Sp-4CCFFOO=3C_N-4CFO->O_Ext-3C-R_N-4CF->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(28.7425,'m^3/(mol*s)'), n=0.870689, w0=(377500,'J/mol'), E0=(58215.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_N-Sp-4CCFFOO=3C_N-4CFO->O_Ext-3C-R_N-4CF->C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_N-Sp-4CCFFOO=3C_N-4CFO->O_Ext-3C-R_N-4CF->C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_N-Sp-4CCFFOO=3C_N-4CFO->O_Ext-3C-R_N-4CF->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-4BrCFINOPSSi->Br_N-Sp-4CCFFOO=3C_N-4CFO->O_Ext-3C-R_N-4CF->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 463,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->F_Ext-1C-R_N-6R!H->Cl_6BrCFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(1.58e+08,'m^3/(mol*s)'), n=0, w0=(377500,'J/mol'), E0=(109745,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->F_Ext-1C-R_N-6R!H->Cl_6BrCFINOPSSi->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->F_Ext-1C-R_N-6R!H->Cl_6BrCFINOPSSi->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->F_Ext-1C-R_N-6R!H->Cl_6BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->F_Ext-1C-R_N-6R!H->Cl_6BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 464,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->F_Ext-1C-R_N-6R!H->Cl_N-6BrCFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(3.4e+06,'m^3/(mol*s)'), n=0, w0=(377500,'J/mol'), E0=(69541,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->F_Ext-1C-R_N-6R!H->Cl_N-6BrCFINOPSSi->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->F_Ext-1C-R_N-6R!H->Cl_N-6BrCFINOPSSi->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->F_Ext-1C-R_N-6R!H->Cl_N-6BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->F_Ext-1C-R_N-6R!H->Cl_N-6BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 465,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_5R!H->Cl_Ext-1C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(11779.2,'m^3/(mol*s)'), n=0.750302, w0=(377500,'J/mol'), E0=(63146.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.17169218613807086, var=3.3846749487308014, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_5R!H->Cl_Ext-1C-R_Ext-4C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_5R!H->Cl_Ext-1C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 4.1195959748109034"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_5R!H->Cl_Ext-1C-R_Ext-4C-R
Total Standard Deviation in ln(k): 4.1195959748109034""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_5R!H->Cl_Ext-1C-R_Ext-4C-R
Total Standard Deviation in ln(k): 4.1195959748109034
""",
)

entry(
    index = 466,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_5R!H->Cl_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.33333e+07,'m^3/(mol*s)'), n=0, w0=(377500,'J/mol'), E0=(86837.2,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_5R!H->Cl_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_5R!H->Cl_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_5R!H->Cl_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_5R!H->Cl_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 467,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_5R!H->Cl_Ext-4C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=0, w0=(377500,'J/mol'), E0=(72521,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_5R!H->Cl_Ext-4C-R_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_5R!H->Cl_Ext-4C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_5R!H->Cl_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_5R!H->Cl_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 468,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(58.4325,'m^3/(mol*s)'), n=1.86734, w0=(377500,'J/mol'), E0=(74737.5,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 469,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(15651.6,'m^3/(mol*s)'), n=1.00983, w0=(377500,'J/mol'), E0=(75641.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-5.651576343850658e-15, var=0.3039306537166053, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 1.1052085640068323"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 1.1052085640068323""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 1.1052085640068323
""",
)

entry(
    index = 470,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C_Ext-3CClFO-R_6R!H->F",
    kinetics = ArrheniusBM(A=(2.12106e+06,'m^3/(mol*s)'), n=-0.408328, w0=(327000,'J/mol'), E0=(71254.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0014515685703786107, var=0.7703953870628389, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C_Ext-3CClFO-R_6R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C_Ext-3CClFO-R_6R!H->F
    Total Standard Deviation in ln(k): 1.7632466424305102"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C_Ext-3CClFO-R_6R!H->F
Total Standard Deviation in ln(k): 1.7632466424305102""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C_Ext-3CClFO-R_6R!H->F
Total Standard Deviation in ln(k): 1.7632466424305102
""",
)

entry(
    index = 471,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C_Ext-3CClFO-R_N-6R!H->F",
    kinetics = ArrheniusBM(A=(1.10609e+08,'m^3/(mol*s)'), n=-0.983094, w0=(327000,'J/mol'), E0=(78155.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.051754454791236165, var=1.9814254359813397, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C_Ext-3CClFO-R_N-6R!H->F',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C_Ext-3CClFO-R_N-6R!H->F
    Total Standard Deviation in ln(k): 2.951963847856913"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C_Ext-3CClFO-R_N-6R!H->F
Total Standard Deviation in ln(k): 2.951963847856913""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C_Ext-3CClFO-R_N-6R!H->F
Total Standard Deviation in ln(k): 2.951963847856913
""",
)

entry(
    index = 472,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.00237852,'m^3/(mol*s)'), n=2.40102, w0=(327000,'J/mol'), E0=(48854.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.15980303660531373, var=2.939315719541326, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 3.8385197251169694"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 3.8385197251169694""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 3.8385197251169694
""",
)

entry(
    index = 473,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_N-5R!H->Cl_4BrCFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(4.15803e+06,'m^3/(mol*s)'), n=0.0378171, w0=(327000,'J/mol'), E0=(61029.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_N-5R!H->Cl_4BrCFINOPSSi->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_N-5R!H->Cl_4BrCFINOPSSi->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_N-5R!H->Cl_4BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_N-5R!H->Cl_4BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 474,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_N-5R!H->Cl_N-4BrCFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(23471.8,'m^3/(mol*s)'), n=0.611057, w0=(327000,'J/mol'), E0=(48394.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.03793678665591556, var=1.6631090108296722, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_N-5R!H->Cl_N-4BrCFINOPSSi->Br',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_N-5R!H->Cl_N-4BrCFINOPSSi->Br
    Total Standard Deviation in ln(k): 2.680656667178491"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_N-5R!H->Cl_N-4BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 2.680656667178491""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_N-5R!H->Cl_N-4BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 2.680656667178491
""",
)

entry(
    index = 475,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(3.57521e+12,'m^3/(mol*s)'), n=-1.76616, w0=(299500,'J/mol'), E0=(72858.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.09394774172035059, var=16.293133926427753, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 8.328113493182295"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 8.328113493182295""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 8.328113493182295
""",
)

entry(
    index = 476,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C_Ext-1C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(0.168083,'m^3/(mol*s)'), n=1.8024, w0=(327000,'J/mol'), E0=(72414.8,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C_Ext-1C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C_Ext-1C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 477,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C_Ext-1C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(1184.5,'m^3/(mol*s)'), n=0.637954, w0=(327000,'J/mol'), E0=(65492.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.017676028313309066, var=0.9452640719203018, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C_Ext-1C-R_N-6R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C_Ext-1C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 1.9935096342763239"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 1.9935096342763239""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 1.9935096342763239
""",
)

entry(
    index = 478,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C_Sp-5C-1C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(0.0056062,'m^3/(mol*s)'), n=2.84217, w0=(327000,'J/mol'), E0=(76231.1,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C_Sp-5C-1C_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C_Sp-5C-1C_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C_Sp-5C-1C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C_Sp-5C-1C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 479,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C_5BrClFINOPSSi->F",
    kinetics = ArrheniusBM(A=(2.6533e-21,'m^3/(mol*s)'), n=7.59901, w0=(327000,'J/mol'), E0=(-8725.52,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0119815596409625, var=19.739775533812924, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C_5BrClFINOPSSi->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C_5BrClFINOPSSi->F
    Total Standard Deviation in ln(k): 8.937035552608881"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C_5BrClFINOPSSi->F
Total Standard Deviation in ln(k): 8.937035552608881""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C_5BrClFINOPSSi->F
Total Standard Deviation in ln(k): 8.937035552608881
""",
)

entry(
    index = 480,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C_N-5BrClFINOPSSi->F",
    kinetics = ArrheniusBM(A=(2.58859e-20,'m^3/(mol*s)'), n=7.748, w0=(327000,'J/mol'), E0=(20109.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0005441907117536237, var=4.7457957728726505, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C_N-5BrClFINOPSSi->F',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C_N-5BrClFINOPSSi->F
    Total Standard Deviation in ln(k): 4.368652092004725"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C_N-5BrClFINOPSSi->F
Total Standard Deviation in ln(k): 4.368652092004725""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C_N-5BrClFINOPSSi->F
Total Standard Deviation in ln(k): 4.368652092004725
""",
)

entry(
    index = 481,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->F",
    kinetics = ArrheniusBM(A=(4.22031e+14,'m^3/(mol*s)'), n=-2.42449, w0=(286135,'J/mol'), E0=(43575.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1544155828171472, var=6.107069694862513, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->F
    Total Standard Deviation in ln(k): 5.342177625715762"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->F
Total Standard Deviation in ln(k): 5.342177625715762""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->F
Total Standard Deviation in ln(k): 5.342177625715762
""",
)

entry(
    index = 482,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F",
    kinetics = ArrheniusBM(A=(8.6798e+11,'m^3/(mol*s)'), n=-1.46927, w0=(284818,'J/mol'), E0=(40573.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.21800346249738004, var=4.282671766684793, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F
    Total Standard Deviation in ln(k): 4.696469873373527"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F
Total Standard Deviation in ln(k): 4.696469873373527""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F
Total Standard Deviation in ln(k): 4.696469873373527
""",
)

entry(
    index = 483,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_N-5R!H->Cl_Ext-1C-R_3ClF->F",
    kinetics = ArrheniusBM(A=(7.9e+06,'m^3/(mol*s)'), n=0, w0=(288770,'J/mol'), E0=(17371.6,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_N-5R!H->Cl_Ext-1C-R_3ClF->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_N-5R!H->Cl_Ext-1C-R_3ClF->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_N-5R!H->Cl_Ext-1C-R_3ClF->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_N-5R!H->Cl_Ext-1C-R_3ClF->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 484,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_N-5R!H->Cl_Ext-1C-R_N-3ClF->F",
    kinetics = ArrheniusBM(A=(9.45439e+10,'m^3/(mol*s)'), n=-1.07783, w0=(283500,'J/mol'), E0=(50360,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_N-5R!H->Cl_Ext-1C-R_N-3ClF->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_N-5R!H->Cl_Ext-1C-R_N-3ClF->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_N-5R!H->Cl_Ext-1C-R_N-3ClF->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_N-5R!H->Cl_Ext-1C-R_N-3ClF->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 485,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C_3ClFO-u1_Ext-1C-R_3ClFO->O",
    kinetics = ArrheniusBM(A=(3.14214e+09,'m^3/(mol*s)'), n=-0.665361, w0=(299500,'J/mol'), E0=(29950,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C_3ClFO-u1_Ext-1C-R_3ClFO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C_3ClFO-u1_Ext-1C-R_3ClFO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C_3ClFO-u1_Ext-1C-R_3ClFO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C_3ClFO-u1_Ext-1C-R_3ClFO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 486,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C_3ClFO-u1_Ext-1C-R_N-3ClFO->O",
    kinetics = ArrheniusBM(A=(1.67931e+10,'m^3/(mol*s)'), n=-0.830163, w0=(283500,'J/mol'), E0=(28350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C_3ClFO-u1_Ext-1C-R_N-3ClFO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C_3ClFO-u1_Ext-1C-R_N-3ClFO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C_3ClFO-u1_Ext-1C-R_N-3ClFO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C_3ClFO-u1_Ext-1C-R_N-3ClFO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 487,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C_3ClFO-u1_4BrCFINOPSSi->C_3ClFO->O",
    kinetics = ArrheniusBM(A=(0.0318289,'m^3/(mol*s)'), n=2.73518, w0=(299500,'J/mol'), E0=(66623.9,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C_3ClFO-u1_4BrCFINOPSSi->C_3ClFO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C_3ClFO-u1_4BrCFINOPSSi->C_3ClFO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C_3ClFO-u1_4BrCFINOPSSi->C_3ClFO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C_3ClFO-u1_4BrCFINOPSSi->C_3ClFO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 488,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C_3ClFO-u1_4BrCFINOPSSi->C_N-3ClFO->O",
    kinetics = ArrheniusBM(A=(3.61921e+09,'m^3/(mol*s)'), n=-0.540409, w0=(283500,'J/mol'), E0=(28350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C_3ClFO-u1_4BrCFINOPSSi->C_N-3ClFO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C_3ClFO-u1_4BrCFINOPSSi->C_N-3ClFO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C_3ClFO-u1_4BrCFINOPSSi->C_N-3ClFO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3CClFO->C_3ClFO-u1_4BrCFINOPSSi->C_N-3ClFO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 489,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_4BrCFINOPSSi->Br_N-3CClFO->Cl_N-3CFO->C_3O-u1",
    kinetics = ArrheniusBM(A=(3.5e+06,'m^3/(mol*s)'), n=0, w0=(299500,'J/mol'), E0=(22320.3,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_4BrCFINOPSSi->Br_N-3CClFO->Cl_N-3CFO->C_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_4BrCFINOPSSi->Br_N-3CClFO->Cl_N-3CFO->C_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_4BrCFINOPSSi->Br_N-3CClFO->Cl_N-3CFO->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_4BrCFINOPSSi->Br_N-3CClFO->Cl_N-3CFO->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 490,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_4BrCFINOPSSi->Br_N-3CClFO->Cl_N-3CFO->C_N-3O-u1",
    kinetics = ArrheniusBM(A=(3.5e+06,'m^3/(mol*s)'), n=0, w0=(299500,'J/mol'), E0=(15635.3,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_4BrCFINOPSSi->Br_N-3CClFO->Cl_N-3CFO->C_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_4BrCFINOPSSi->Br_N-3CClFO->Cl_N-3CFO->C_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_4BrCFINOPSSi->Br_N-3CClFO->Cl_N-3CFO->C_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_4BrCFINOPSSi->Br_N-3CClFO->Cl_N-3CFO->C_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 491,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_3CClO->Cl",
    kinetics = ArrheniusBM(A=(1.9e+08,'m^3/(mol*s)'), n=0, w0=(283500,'J/mol'), E0=(28350,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_3CClO->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_3CClO->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_3CClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_3CClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 492,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_N-3CClO->Cl",
    kinetics = ArrheniusBM(A=(3.61227e+24,'m^3/(mol*s)'), n=-5.2741, w0=(315214,'J/mol'), E0=(110286,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.39356681997342136, var=15.268275344568444, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_N-3CClO->Cl',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_N-3CClO->Cl
    Total Standard Deviation in ln(k): 8.822291612317736"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_N-3CClO->Cl
Total Standard Deviation in ln(k): 8.822291612317736""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_N-3CClO->Cl
Total Standard Deviation in ln(k): 8.822291612317736
""",
)

entry(
    index = 493,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_3CClFO->C_4CFO->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(0.000540685,'m^3/(mol*s)'), n=3.17235, w0=(327000,'J/mol'), E0=(74063.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.3393611685421646e-06, var=0.44730157612620847, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_3CClFO->C_4CFO->C_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_3CClFO->C_4CFO->C_Ext-4C-R
    Total Standard Deviation in ln(k): 1.3407823789970164"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_3CClFO->C_4CFO->C_Ext-4C-R
Total Standard Deviation in ln(k): 1.3407823789970164""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_3CClFO->C_4CFO->C_Ext-4C-R
Total Standard Deviation in ln(k): 1.3407823789970164
""",
)

entry(
    index = 494,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_N-3O-u1_N-1BrO->Br_Ext-1O-R_4R!H->C_Ext-4C-R_Sp-5R!H=4C",
    kinetics = ArrheniusBM(A=(220.761,'m^3/(mol*s)'), n=1.59458, w0=(272000,'J/mol'), E0=(27200,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_N-3O-u1_N-1BrO->Br_Ext-1O-R_4R!H->C_Ext-4C-R_Sp-5R!H=4C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_N-3O-u1_N-1BrO->Br_Ext-1O-R_4R!H->C_Ext-4C-R_Sp-5R!H=4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_N-3O-u1_N-1BrO->Br_Ext-1O-R_4R!H->C_Ext-4C-R_Sp-5R!H=4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_N-3O-u1_N-1BrO->Br_Ext-1O-R_4R!H->C_Ext-4C-R_Sp-5R!H=4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 495,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_N-3O-u1_N-1BrO->Br_Ext-1O-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C",
    kinetics = ArrheniusBM(A=(234.788,'m^3/(mol*s)'), n=1.5918, w0=(272000,'J/mol'), E0=(27200,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_N-3O-u1_N-1BrO->Br_Ext-1O-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_N-3O-u1_N-1BrO->Br_Ext-1O-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_N-3O-u1_N-1BrO->Br_Ext-1O-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3BrCClFO->O_1BrClFO-u0_N-1BrClFO->F_N-1BrClO->Cl_N-3O-u1_N-1BrO->Br_Ext-1O-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 496,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_1ClFO->O_N-5R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_Ext-4R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(4.36525e-10,'m^3/(mol*s)'), n=4.21502, w0=(299500,'J/mol'), E0=(25416.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_1ClFO->O_N-5R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_Ext-4R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_1ClFO->O_N-5R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_Ext-4R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_1ClFO->O_N-5R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_Ext-4R!H-R_1ClFO->O_N-5R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 497,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F_5BrCClINOPSSi->Cl_Ext-3BrCClF-R_6R!H->O",
    kinetics = ArrheniusBM(A=(6.20565e-06,'m^3/(mol*s)'), n=3.17637, w0=(299500,'J/mol'), E0=(23479.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F_5BrCClINOPSSi->Cl_Ext-3BrCClF-R_6R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F_5BrCClINOPSSi->Cl_Ext-3BrCClF-R_6R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F_5BrCClINOPSSi->Cl_Ext-3BrCClF-R_6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F_5BrCClINOPSSi->Cl_Ext-3BrCClF-R_6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 498,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F_5BrCClINOPSSi->Cl_Ext-3BrCClF-R_N-6R!H->O",
    kinetics = ArrheniusBM(A=(2.45869e+06,'m^3/(mol*s)'), n=-0.272498, w0=(299500,'J/mol'), E0=(38011.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.124691809721524e-15, var=13.59001105182999, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F_5BrCClINOPSSi->Cl_Ext-3BrCClF-R_N-6R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F_5BrCClINOPSSi->Cl_Ext-3BrCClF-R_N-6R!H->O
    Total Standard Deviation in ln(k): 7.390382123060773"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F_5BrCClINOPSSi->Cl_Ext-3BrCClF-R_N-6R!H->O
Total Standard Deviation in ln(k): 7.390382123060773""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F_5BrCClINOPSSi->Cl_Ext-3BrCClF-R_N-6R!H->O
Total Standard Deviation in ln(k): 7.390382123060773
""",
)

entry(
    index = 499,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_Sp-5CO-3BrCCClFO",
    kinetics = ArrheniusBM(A=(0.00011084,'m^3/(mol*s)'), n=3.14673, w0=(299500,'J/mol'), E0=(20029.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.027324712080111443, var=0.8469398038275362, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_Sp-5CO-3BrCCClFO',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_Sp-5CO-3BrCCClFO
    Total Standard Deviation in ln(k): 1.913599365365919"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_Sp-5CO-3BrCCClFO
Total Standard Deviation in ln(k): 1.913599365365919""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_Sp-5CO-3BrCCClFO
Total Standard Deviation in ln(k): 1.913599365365919
""",
)

entry(
    index = 500,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_N-Sp-5CO-3BrCCClFO",
    kinetics = ArrheniusBM(A=(708.716,'m^3/(mol*s)'), n=0.730984, w0=(299500,'J/mol'), E0=(36927.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_N-Sp-5CO-3BrCCClFO',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_N-Sp-5CO-3BrCCClFO
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_N-Sp-5CO-3BrCCClFO
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_N-Sp-5CO-3BrCCClFO
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 501,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_N-1ClO->O_Ext-3BrCClF-R_5R!H->Cl_Ext-3BrCClF-R",
    kinetics = ArrheniusBM(A=(0.311776,'m^3/(mol*s)'), n=1.78291, w0=(283500,'J/mol'), E0=(12743.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.12329673634702638, var=1.1276264636741187, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_N-1ClO->O_Ext-3BrCClF-R_5R!H->Cl_Ext-3BrCClF-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_N-1ClO->O_Ext-3BrCClF-R_5R!H->Cl_Ext-3BrCClF-R
    Total Standard Deviation in ln(k): 2.4386141157095866"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_N-1ClO->O_Ext-3BrCClF-R_5R!H->Cl_Ext-3BrCClF-R
Total Standard Deviation in ln(k): 2.4386141157095866""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_N-1ClO->O_Ext-3BrCClF-R_5R!H->Cl_Ext-3BrCClF-R
Total Standard Deviation in ln(k): 2.4386141157095866
""",
)

entry(
    index = 502,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_N-1ClO->O_Ext-3BrCClF-R_N-5R!H->Cl_Ext-3BrCClF-R",
    kinetics = ArrheniusBM(A=(388000,'m^3/(mol*s)'), n=0, w0=(283500,'J/mol'), E0=(38472.7,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_N-1ClO->O_Ext-3BrCClF-R_N-5R!H->Cl_Ext-3BrCClF-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_N-1ClO->O_Ext-3BrCClF-R_N-5R!H->Cl_Ext-3BrCClF-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_N-1ClO->O_Ext-3BrCClF-R_N-5R!H->Cl_Ext-3BrCClF-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_N-1ClO->O_Ext-3BrCClF-R_N-5R!H->Cl_Ext-3BrCClF-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 503,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_N-4BrCClINOPSSi->O_4CCl->C_Ext-4C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(2.61942e-37,'m^3/(mol*s)'), n=12.0358, w0=(299500,'J/mol'), E0=(-13261.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.062384973801084445, var=20.983957787767434, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_N-4BrCClINOPSSi->O_4CCl->C_Ext-4C-R_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_N-4BrCClINOPSSi->O_4CCl->C_Ext-4C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 9.340086749678047"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_N-4BrCClINOPSSi->O_4CCl->C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 9.340086749678047""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_N-4BrCClINOPSSi->O_4CCl->C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 9.340086749678047
""",
)

entry(
    index = 504,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_N-4BrCClINOPSSi->O_4CCl->C_5R!H->C",
    kinetics = ArrheniusBM(A=(0.00106635,'m^3/(mol*s)'), n=2.59522, w0=(299500,'J/mol'), E0=(60401.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_N-4BrCClINOPSSi->O_4CCl->C_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_N-4BrCClINOPSSi->O_4CCl->C_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_N-4BrCClINOPSSi->O_4CCl->C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_N-4BrCClINOPSSi->O_4CCl->C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 505,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_N-4BrCClINOPSSi->O_4CCl->C_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.000753617,'m^3/(mol*s)'), n=2.43038, w0=(299500,'J/mol'), E0=(55678.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_N-4BrCClINOPSSi->O_4CCl->C_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_N-4BrCClINOPSSi->O_4CCl->C_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_N-4BrCClINOPSSi->O_4CCl->C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_N-4BrCClINOPSSi->O_4CCl->C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 506,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C_Ext-6C-R_Ext-6C-R_Ext-6C-R",
    kinetics = ArrheniusBM(A=(0.0210238,'m^3/(mol*s)'), n=1.59222, w0=(377500,'J/mol'), E0=(66751.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00017083974618084378, var=0.0005111090110197106, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C_Ext-6C-R_Ext-6C-R_Ext-6C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C_Ext-6C-R_Ext-6C-R_Ext-6C-R
    Total Standard Deviation in ln(k): 0.04575173522636573"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C_Ext-6C-R_Ext-6C-R_Ext-6C-R
Total Standard Deviation in ln(k): 0.04575173522636573""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C_Ext-6C-R_Ext-6C-R_Ext-6C-R
Total Standard Deviation in ln(k): 0.04575173522636573
""",
)

entry(
    index = 507,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_5R!H->Cl_Ext-1C-R_Ext-4C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(2.60485e+07,'m^3/(mol*s)'), n=-0.0256506, w0=(377500,'J/mol'), E0=(77118.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.049302615044287006, var=0.05080206269995769, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_5R!H->Cl_Ext-1C-R_Ext-4C-R_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_5R!H->Cl_Ext-1C-R_Ext-4C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 0.5757294295493273"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_5R!H->Cl_Ext-1C-R_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 0.5757294295493273""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_5R!H->Cl_Ext-1C-R_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 0.5757294295493273
""",
)

entry(
    index = 508,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_5R!H->Cl_Ext-1C-R_Ext-4C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.2e+06,'m^3/(mol*s)'), n=0, w0=(377500,'J/mol'), E0=(69816,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_5R!H->Cl_Ext-1C-R_Ext-4C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_5R!H->Cl_Ext-1C-R_Ext-4C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_5R!H->Cl_Ext-1C-R_Ext-4C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_5R!H->Cl_Ext-1C-R_Ext-4C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 509,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C_Ext-3CClFO-R_6R!H->F_Ext-3CClFO-R_7R!H->Cl",
    kinetics = ArrheniusBM(A=(67300.9,'m^3/(mol*s)'), n=0.0660671, w0=(327000,'J/mol'), E0=(67326.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C_Ext-3CClFO-R_6R!H->F_Ext-3CClFO-R_7R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C_Ext-3CClFO-R_6R!H->F_Ext-3CClFO-R_7R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C_Ext-3CClFO-R_6R!H->F_Ext-3CClFO-R_7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C_Ext-3CClFO-R_6R!H->F_Ext-3CClFO-R_7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 510,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C_Ext-3CClFO-R_6R!H->F_Ext-3CClFO-R_N-7R!H->Cl",
    kinetics = ArrheniusBM(A=(47458.9,'m^3/(mol*s)'), n=0.0429724, w0=(327000,'J/mol'), E0=(68277.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C_Ext-3CClFO-R_6R!H->F_Ext-3CClFO-R_N-7R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C_Ext-3CClFO-R_6R!H->F_Ext-3CClFO-R_N-7R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C_Ext-3CClFO-R_6R!H->F_Ext-3CClFO-R_N-7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C_Ext-3CClFO-R_6R!H->F_Ext-3CClFO-R_N-7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 511,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C_Ext-3CClFO-R_N-6R!H->F_6BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(120180,'m^3/(mol*s)'), n=-0.0941862, w0=(327000,'J/mol'), E0=(76576.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.02907383120058163, var=3.3624259516464883, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C_Ext-3CClFO-R_N-6R!H->F_6BrCClINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C_Ext-3CClFO-R_N-6R!H->F_6BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 3.749116282446281"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C_Ext-3CClFO-R_N-6R!H->F_6BrCClINOPSSi->C
Total Standard Deviation in ln(k): 3.749116282446281""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C_Ext-3CClFO-R_N-6R!H->F_6BrCClINOPSSi->C
Total Standard Deviation in ln(k): 3.749116282446281
""",
)

entry(
    index = 512,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C_Ext-3CClFO-R_N-6R!H->F_N-6BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(2.39515e+10,'m^3/(mol*s)'), n=-1.68621, w0=(327000,'J/mol'), E0=(78402.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.014999276780830816, var=6.6502966869444124, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C_Ext-3CClFO-R_N-6R!H->F_N-6BrCClINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C_Ext-3CClFO-R_N-6R!H->F_N-6BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 5.207531355030813"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C_Ext-3CClFO-R_N-6R!H->F_N-6BrCClINOPSSi->C
Total Standard Deviation in ln(k): 5.207531355030813""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C_Ext-3CClFO-R_N-6R!H->F_N-6BrCClINOPSSi->C
Total Standard Deviation in ln(k): 5.207531355030813
""",
)

entry(
    index = 513,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl",
    kinetics = ArrheniusBM(A=(2.6061e+06,'m^3/(mol*s)'), n=-0.252865, w0=(327000,'J/mol'), E0=(71911.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.015580019959500434, var=0.35544478409945907, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl
    Total Standard Deviation in ln(k): 1.2343525977402119"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl
Total Standard Deviation in ln(k): 1.2343525977402119""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl
Total Standard Deviation in ln(k): 1.2343525977402119
""",
)

entry(
    index = 514,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl",
    kinetics = ArrheniusBM(A=(9.50868e-20,'m^3/(mol*s)'), n=7.192, w0=(327000,'J/mol'), E0=(-1808.66,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.021505126897219052, var=33.43623967789457, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl
    Total Standard Deviation in ln(k): 11.646228680755353"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl
Total Standard Deviation in ln(k): 11.646228680755353""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl
Total Standard Deviation in ln(k): 11.646228680755353
""",
)

entry(
    index = 515,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_N-5R!H->Cl_N-4BrCFINOPSSi->Br_5BrCFO->C",
    kinetics = ArrheniusBM(A=(1.5e+06,'m^3/(mol*s)'), n=0, w0=(327000,'J/mol'), E0=(57043.5,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_N-5R!H->Cl_N-4BrCFINOPSSi->Br_5BrCFO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_N-5R!H->Cl_N-4BrCFINOPSSi->Br_5BrCFO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_N-5R!H->Cl_N-4BrCFINOPSSi->Br_5BrCFO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_N-5R!H->Cl_N-4BrCFINOPSSi->Br_5BrCFO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 516,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_N-5R!H->Cl_N-4BrCFINOPSSi->Br_N-5BrCFO->C",
    kinetics = ArrheniusBM(A=(6206.25,'m^3/(mol*s)'), n=0.804774, w0=(327000,'J/mol'), E0=(45370,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.03405438142603017, var=1.3208429237086072, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_N-5R!H->Cl_N-4BrCFINOPSSi->Br_N-5BrCFO->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_N-5R!H->Cl_N-4BrCFINOPSSi->Br_N-5BrCFO->C
    Total Standard Deviation in ln(k): 2.3895643113323284"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_N-5R!H->Cl_N-4BrCFINOPSSi->Br_N-5BrCFO->C
Total Standard Deviation in ln(k): 2.3895643113323284""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_N-5R!H->Cl_N-4BrCFINOPSSi->Br_N-5BrCFO->C
Total Standard Deviation in ln(k): 2.3895643113323284
""",
)

entry(
    index = 517,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_3O-u1",
    kinetics = ArrheniusBM(A=(0.211482,'m^3/(mol*s)'), n=2.3853, w0=(299500,'J/mol'), E0=(45837.1,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 518,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-3O-u1",
    kinetics = ArrheniusBM(A=(12635,'m^3/(mol*s)'), n=0.772422, w0=(299500,'J/mol'), E0=(69890.2,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_3CClFO->O_Ext-1C-R_5R!H->C_Ext-1C-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 519,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C_Ext-1C-R_N-6R!H->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(7759.99,'m^3/(mol*s)'), n=0.333879, w0=(327000,'J/mol'), E0=(62293.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00010050920102062203, var=2.627719107866215, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C_Ext-1C-R_N-6R!H->C_Ext-5C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C_Ext-1C-R_N-6R!H->C_Ext-5C-R
    Total Standard Deviation in ln(k): 3.2499763948461613"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C_Ext-1C-R_N-6R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 3.2499763948461613""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C_Ext-1C-R_N-6R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 3.2499763948461613
""",
)

entry(
    index = 520,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C_5BrClFINOPSSi->F_Ext-1C-R_6R!H->Cl",
    kinetics = ArrheniusBM(A=(66666.7,'m^3/(mol*s)'), n=0, w0=(327000,'J/mol'), E0=(64303.9,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C_5BrClFINOPSSi->F_Ext-1C-R_6R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C_5BrClFINOPSSi->F_Ext-1C-R_6R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C_5BrClFINOPSSi->F_Ext-1C-R_6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C_5BrClFINOPSSi->F_Ext-1C-R_6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 521,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C_5BrClFINOPSSi->F_Ext-1C-R_N-6R!H->Cl",
    kinetics = ArrheniusBM(A=(630000,'m^3/(mol*s)'), n=0, w0=(327000,'J/mol'), E0=(56704.6,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C_5BrClFINOPSSi->F_Ext-1C-R_N-6R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C_5BrClFINOPSSi->F_Ext-1C-R_N-6R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C_5BrClFINOPSSi->F_Ext-1C-R_N-6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C_5BrClFINOPSSi->F_Ext-1C-R_N-6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 522,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C_N-5BrClFINOPSSi->F_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.59902e-21,'m^3/(mol*s)'), n=8.04061, w0=(327000,'J/mol'), E0=(10348.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.01623558718234365, var=12.094830893907567, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C_N-5BrClFINOPSSi->F_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C_N-5BrClFINOPSSi->F_Ext-1C-R
    Total Standard Deviation in ln(k): 7.012785086568307"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C_N-5BrClFINOPSSi->F_Ext-1C-R
Total Standard Deviation in ln(k): 7.012785086568307""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C_N-5BrClFINOPSSi->F_Ext-1C-R
Total Standard Deviation in ln(k): 7.012785086568307
""",
)

entry(
    index = 523,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C_N-5BrClFINOPSSi->F_5ClO->O",
    kinetics = ArrheniusBM(A=(0.00355875,'m^3/(mol*s)'), n=2.81981, w0=(327000,'J/mol'), E0=(73300.2,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C_N-5BrClFINOPSSi->F_5ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C_N-5BrClFINOPSSi->F_5ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C_N-5BrClFINOPSSi->F_5ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C_N-5BrClFINOPSSi->F_5ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 524,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C_N-5BrClFINOPSSi->F_N-5ClO->O",
    kinetics = ArrheniusBM(A=(8e+06,'m^3/(mol*s)'), n=0, w0=(327000,'J/mol'), E0=(70560.6,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C_N-5BrClFINOPSSi->F_N-5ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C_N-5BrClFINOPSSi->F_N-5ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C_N-5BrClFINOPSSi->F_N-5ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C_N-5BrClFINOPSSi->F_N-5ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 525,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->F_3ClF->F",
    kinetics = ArrheniusBM(A=(960000,'m^3/(mol*s)'), n=0, w0=(288770,'J/mol'), E0=(21294,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->F_3ClF->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->F_3ClF->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->F_3ClF->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->F_3ClF->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 526,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->F_N-3ClF->F",
    kinetics = ArrheniusBM(A=(1.73306e+11,'m^3/(mol*s)'), n=-1.10093, w0=(283500,'J/mol'), E0=(49631.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->F_N-3ClF->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->F_N-3ClF->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->F_N-3ClF->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->F_N-3ClF->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 527,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_3ClF->F",
    kinetics = ArrheniusBM(A=(2.5e+06,'m^3/(mol*s)'), n=0, w0=(288770,'J/mol'), E0=(29079.4,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_3ClF->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_3ClF->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_3ClF->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_3ClF->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 528,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-3ClF->F",
    kinetics = ArrheniusBM(A=(98.6766,'m^3/(mol*s)'), n=1.48749, w0=(283500,'J/mol'), E0=(4659.85,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.08499520833324213, var=4.357628469075198, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-3ClF->F',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-3ClF->F
    Total Standard Deviation in ln(k): 4.398426934136067"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-3ClF->F
Total Standard Deviation in ln(k): 4.398426934136067""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-3ClF->F
Total Standard Deviation in ln(k): 4.398426934136067
""",
)

entry(
    index = 529,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_N-3CClO->Cl_Ext-4CFO-R",
    kinetics = ArrheniusBM(A=(9.55337e+22,'m^3/(mol*s)'), n=-4.80658, w0=(316000,'J/mol'), E0=(111625,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.3643899767227345, var=19.472593223300745, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_N-3CClO->Cl_Ext-4CFO-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_N-3CClO->Cl_Ext-4CFO-R
    Total Standard Deviation in ln(k): 9.761999813144847"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_N-3CClO->Cl_Ext-4CFO-R
Total Standard Deviation in ln(k): 9.761999813144847""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_N-3CClO->Cl_Ext-4CFO-R
Total Standard Deviation in ln(k): 9.761999813144847
""",
)

entry(
    index = 530,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_N-3CClO->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(8.57465e+08,'m^3/(mol*s)'), n=-0.955987, w0=(327000,'J/mol'), E0=(71912.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_N-3CClO->Cl_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_N-3CClO->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_N-3CClO->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_N-3CClO->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 531,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_3CClFO->C_4CFO->C_Ext-4C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(0.00283994,'m^3/(mol*s)'), n=2.94646, w0=(327000,'J/mol'), E0=(76799.7,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_3CClFO->C_4CFO->C_Ext-4C-R_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_3CClFO->C_4CFO->C_Ext-4C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_3CClFO->C_4CFO->C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_3CClFO->C_4CFO->C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 532,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_Sp-5CO-3BrCCClFO_5CO->C",
    kinetics = ArrheniusBM(A=(0.00122456,'m^3/(mol*s)'), n=2.76919, w0=(299500,'J/mol'), E0=(12380.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.7002253211393805, var=0.15813103416887234, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_Sp-5CO-3BrCCClFO_5CO->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_Sp-5CO-3BrCCClFO_5CO->C
    Total Standard Deviation in ln(k): 2.556556900188728"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_Sp-5CO-3BrCCClFO_5CO->C
Total Standard Deviation in ln(k): 2.556556900188728""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_Sp-5CO-3BrCCClFO_5CO->C
Total Standard Deviation in ln(k): 2.556556900188728
""",
)

entry(
    index = 533,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_Sp-5CO-3BrCCClFO_N-5CO->C",
    kinetics = ArrheniusBM(A=(1.57337e-06,'m^3/(mol*s)'), n=3.83129, w0=(299500,'J/mol'), E0=(24049.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_Sp-5CO-3BrCCClFO_N-5CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_Sp-5CO-3BrCCClFO_N-5CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_Sp-5CO-3BrCCClFO_N-5CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_Sp-5CO-3BrCCClFO_N-5CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 534,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_N-1ClO->O_Ext-3BrCClF-R_5R!H->Cl_Ext-3BrCClF-R_6R!H->Cl",
    kinetics = ArrheniusBM(A=(240000,'m^3/(mol*s)'), n=0, w0=(283500,'J/mol'), E0=(25945.7,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_N-1ClO->O_Ext-3BrCClF-R_5R!H->Cl_Ext-3BrCClF-R_6R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_N-1ClO->O_Ext-3BrCClF-R_5R!H->Cl_Ext-3BrCClF-R_6R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_N-1ClO->O_Ext-3BrCClF-R_5R!H->Cl_Ext-3BrCClF-R_6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_N-1ClO->O_Ext-3BrCClF-R_5R!H->Cl_Ext-3BrCClF-R_6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 535,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_N-1ClO->O_Ext-3BrCClF-R_5R!H->Cl_Ext-3BrCClF-R_N-6R!H->Cl",
    kinetics = ArrheniusBM(A=(416000,'m^3/(mol*s)'), n=0, w0=(283500,'J/mol'), E0=(38989.1,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_N-1ClO->O_Ext-3BrCClF-R_5R!H->Cl_Ext-3BrCClF-R_N-6R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_N-1ClO->O_Ext-3BrCClF-R_5R!H->Cl_Ext-3BrCClF-R_N-6R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_N-1ClO->O_Ext-3BrCClF-R_5R!H->Cl_Ext-3BrCClF-R_N-6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_N-1ClO->O_Ext-3BrCClF-R_5R!H->Cl_Ext-3BrCClF-R_N-6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 536,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_N-4BrCClINOPSSi->O_4CCl->C_Ext-4C-R_Ext-4C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(0.000685288,'m^3/(mol*s)'), n=2.02041, w0=(299500,'J/mol'), E0=(56243.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_N-4BrCClINOPSSi->O_4CCl->C_Ext-4C-R_Ext-4C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_N-4BrCClINOPSSi->O_4CCl->C_Ext-4C-R_Ext-4C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_N-4BrCClINOPSSi->O_4CCl->C_Ext-4C-R_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_N-4BrCClINOPSSi->O_4CCl->C_Ext-4C-R_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 537,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_N-4BrCClINOPSSi->O_4CCl->C_Ext-4C-R_Ext-4C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(5.73079,'m^3/(mol*s)'), n=0.707589, w0=(299500,'J/mol'), E0=(27798.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_N-4BrCClINOPSSi->O_4CCl->C_Ext-4C-R_Ext-4C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_N-4BrCClINOPSSi->O_4CCl->C_Ext-4C-R_Ext-4C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_N-4BrCClINOPSSi->O_4CCl->C_Ext-4C-R_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_N-1ClFO-u0_3BrCClF-u1_Ext-3BrCClF-R_N-4R!H->F_Ext-3BrCClF-R_Ext-3BrCClF-R_N-4BrCClINOPSSi->O_4CCl->C_Ext-4C-R_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 538,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C_Ext-6C-R_Ext-6C-R_Ext-6C-R_7R!H->F",
    kinetics = ArrheniusBM(A=(0.0383598,'m^3/(mol*s)'), n=1.28995, w0=(377500,'J/mol'), E0=(45709.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C_Ext-6C-R_Ext-6C-R_Ext-6C-R_7R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C_Ext-6C-R_Ext-6C-R_Ext-6C-R_7R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C_Ext-6C-R_Ext-6C-R_Ext-6C-R_7R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C_Ext-6C-R_Ext-6C-R_Ext-6C-R_7R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 539,
    label = "Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C_Ext-6C-R_Ext-6C-R_Ext-6C-R_N-7R!H->F",
    kinetics = ArrheniusBM(A=(0.0193099,'m^3/(mol*s)'), n=1.39812, w0=(377500,'J/mol'), E0=(46572.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C_Ext-6C-R_Ext-6C-R_Ext-6C-R_N-7R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C_Ext-6C-R_Ext-6C-R_Ext-6C-R_N-7R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C_Ext-6C-R_Ext-6C-R_Ext-6C-R_N-7R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->O_3BrCClFH-u1_3BrCClFH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C_Ext-6C-R_Ext-6C-R_Ext-6C-R_N-7R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 540,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_5R!H->Cl_Ext-1C-R_Ext-4C-R_Ext-4C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.2e+07,'m^3/(mol*s)'), n=0, w0=(377500,'J/mol'), E0=(70531,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_5R!H->Cl_Ext-1C-R_Ext-4C-R_Ext-4C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_5R!H->Cl_Ext-1C-R_Ext-4C-R_Ext-4C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_5R!H->Cl_Ext-1C-R_Ext-4C-R_Ext-4C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_Sp-4BrCClO-1C_4BrCClO->C_Ext-4C-R_5R!H->Cl_Ext-1C-R_Ext-4C-R_Ext-4C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 541,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C_Ext-3CClFO-R_N-6R!H->F_6BrCClINOPSSi->C_Ext-6C-R",
    kinetics = ArrheniusBM(A=(9544.18,'m^3/(mol*s)'), n=0.419258, w0=(327000,'J/mol'), E0=(80103.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C_Ext-3CClFO-R_N-6R!H->F_6BrCClINOPSSi->C_Ext-6C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C_Ext-3CClFO-R_N-6R!H->F_6BrCClINOPSSi->C_Ext-6C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C_Ext-3CClFO-R_N-6R!H->F_6BrCClINOPSSi->C_Ext-6C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C_Ext-3CClFO-R_N-6R!H->F_6BrCClINOPSSi->C_Ext-6C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 542,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C_Ext-3CClFO-R_N-6R!H->F_N-6BrCClINOPSSi->C_Ext-3CClFO-R",
    kinetics = ArrheniusBM(A=(44185.5,'m^3/(mol*s)'), n=0.107373, w0=(327000,'J/mol'), E0=(63960.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C_Ext-3CClFO-R_N-6R!H->F_N-6BrCClINOPSSi->C_Ext-3CClFO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C_Ext-3CClFO-R_N-6R!H->F_N-6BrCClINOPSSi->C_Ext-3CClFO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C_Ext-3CClFO-R_N-6R!H->F_N-6BrCClINOPSSi->C_Ext-3CClFO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_4R!H->Cl_Ext-1C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl_Sp-5CF-1C_N-5CF->C_Ext-3CClFO-R_N-6R!H->F_N-6BrCClINOPSSi->C_Ext-3CClFO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 543,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_7R!H->F",
    kinetics = ArrheniusBM(A=(283667,'m^3/(mol*s)'), n=0, w0=(327000,'J/mol'), E0=(67906,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_7R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_7R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_7R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_7R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 544,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_N-7R!H->F",
    kinetics = ArrheniusBM(A=(5.15337e+06,'m^3/(mol*s)'), n=-0.333628, w0=(327000,'J/mol'), E0=(72984.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.020352596589214362, var=0.47498745839543227, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_N-7R!H->F',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_N-7R!H->F
    Total Standard Deviation in ln(k): 1.432787238975486"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_N-7R!H->F
Total Standard Deviation in ln(k): 1.432787238975486""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_N-7R!H->F
Total Standard Deviation in ln(k): 1.432787238975486
""",
)

entry(
    index = 545,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl_4BrCFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(389528,'m^3/(mol*s)'), n=-0.00515532, w0=(327000,'J/mol'), E0=(44169.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl_4BrCFINOPSSi->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl_4BrCFINOPSSi->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl_4BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl_4BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 546,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl_N-4BrCFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(117000,'m^3/(mol*s)'), n=0, w0=(327000,'J/mol'), E0=(68642.3,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl_N-4BrCFINOPSSi->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl_N-4BrCFINOPSSi->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl_N-4BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl_N-4BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 547,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_N-5R!H->Cl_N-4BrCFINOPSSi->Br_N-5BrCFO->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(575.991,'m^3/(mol*s)'), n=1.13644, w0=(327000,'J/mol'), E0=(45304.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.014855022588442054, var=4.51902017884977, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_N-5R!H->Cl_N-4BrCFINOPSSi->Br_N-5BrCFO->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_N-5R!H->Cl_N-4BrCFINOPSSi->Br_N-5BrCFO->C_Ext-1C-R
    Total Standard Deviation in ln(k): 4.298987429813492"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_N-5R!H->Cl_N-4BrCFINOPSSi->Br_N-5BrCFO->C_Ext-1C-R
Total Standard Deviation in ln(k): 4.298987429813492""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_N-5R!H->Cl_N-4BrCFINOPSSi->Br_N-5BrCFO->C_Ext-1C-R
Total Standard Deviation in ln(k): 4.298987429813492
""",
)

entry(
    index = 548,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C_Ext-1C-R_N-6R!H->C_Ext-5C-R_7R!H->Cl",
    kinetics = ArrheniusBM(A=(105167,'m^3/(mol*s)'), n=0, w0=(327000,'J/mol'), E0=(70015.4,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C_Ext-1C-R_N-6R!H->C_Ext-5C-R_7R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C_Ext-1C-R_N-6R!H->C_Ext-5C-R_7R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C_Ext-1C-R_N-6R!H->C_Ext-5C-R_7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C_Ext-1C-R_N-6R!H->C_Ext-5C-R_7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 549,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C_Ext-1C-R_N-6R!H->C_Ext-5C-R_N-7R!H->Cl",
    kinetics = ArrheniusBM(A=(264667,'m^3/(mol*s)'), n=0, w0=(327000,'J/mol'), E0=(68049.6,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C_Ext-1C-R_N-6R!H->C_Ext-5C-R_N-7R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C_Ext-1C-R_N-6R!H->C_Ext-5C-R_N-7R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C_Ext-1C-R_N-6R!H->C_Ext-5C-R_N-7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_5R!H->C_Ext-1C-R_N-6R!H->C_Ext-5C-R_N-7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 550,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C_N-5BrClFINOPSSi->F_Ext-1C-R_5ClO->O",
    kinetics = ArrheniusBM(A=(0.0117959,'m^3/(mol*s)'), n=2.7472, w0=(327000,'J/mol'), E0=(66187.2,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C_N-5BrClFINOPSSi->F_Ext-1C-R_5ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C_N-5BrClFINOPSSi->F_Ext-1C-R_5ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C_N-5BrClFINOPSSi->F_Ext-1C-R_5ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C_N-5BrClFINOPSSi->F_Ext-1C-R_5ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 551,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C_N-5BrClFINOPSSi->F_Ext-1C-R_N-5ClO->O",
    kinetics = ArrheniusBM(A=(315000,'m^3/(mol*s)'), n=0, w0=(327000,'J/mol'), E0=(71229.2,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C_N-5BrClFINOPSSi->F_Ext-1C-R_N-5ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C_N-5BrClFINOPSSi->F_Ext-1C-R_N-5ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C_N-5BrClFINOPSSi->F_Ext-1C-R_N-5ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_3CClF->C_Ext-1C-R_N-5R!H->C_Sp-5BrClFINOPSSi-1C_N-5BrClFINOPSSi->F_Ext-1C-R_N-5ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 552,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-3ClF->F_6BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(6.85367e+10,'m^3/(mol*s)'), n=-1.03492, w0=(283500,'J/mol'), E0=(45143.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0005612384116816376, var=10.37828553507008, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-3ClF->F_6BrCClINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-3ClF->F_6BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 6.459733673212557"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-3ClF->F_6BrCClINOPSSi->C
Total Standard Deviation in ln(k): 6.459733673212557""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-3ClF->F_6BrCClINOPSSi->C
Total Standard Deviation in ln(k): 6.459733673212557
""",
)

entry(
    index = 553,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-3ClF->F_N-6BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.93272e+11,'m^3/(mol*s)'), n=-1.14223, w0=(283500,'J/mol'), E0=(36553.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-3ClF->F_N-6BrCClINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-3ClF->F_N-6BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-3ClF->F_N-6BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-3ClF->F_N-6BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 554,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_N-3CClO->Cl_Ext-4CFO-R_3CO->C",
    kinetics = ArrheniusBM(A=(0.000193888,'m^3/(mol*s)'), n=2.86662, w0=(327000,'J/mol'), E0=(64503.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00563682575007647, var=4.143579817895739, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_N-3CClO->Cl_Ext-4CFO-R_3CO->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_N-3CClO->Cl_Ext-4CFO-R_3CO->C
    Total Standard Deviation in ln(k): 4.09495849471426"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_N-3CClO->Cl_Ext-4CFO-R_3CO->C
Total Standard Deviation in ln(k): 4.09495849471426""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_N-3CClO->Cl_Ext-4CFO-R_3CO->C
Total Standard Deviation in ln(k): 4.09495849471426
""",
)

entry(
    index = 555,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_N-3CClO->Cl_Ext-4CFO-R_N-3CO->C",
    kinetics = ArrheniusBM(A=(3.50249e+11,'m^3/(mol*s)'), n=-1.11421, w0=(299500,'J/mol'), E0=(74375.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.18183132879976788, var=6.837966964004557, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_N-3CClO->Cl_Ext-4CFO-R_N-3CO->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_N-3CClO->Cl_Ext-4CFO-R_N-3CO->C
    Total Standard Deviation in ln(k): 5.699145952677338"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_N-3CClO->Cl_Ext-4CFO-R_N-3CO->C
Total Standard Deviation in ln(k): 5.699145952677338""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_N-3CClO->Cl_Ext-4CFO-R_N-3CO->C
Total Standard Deviation in ln(k): 5.699145952677338
""",
)

entry(
    index = 556,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_Sp-5CO-3BrCCClFO_5CO->C_Ext-3BrCClF-R",
    kinetics = ArrheniusBM(A=(7.47383e-08,'m^3/(mol*s)'), n=4.03904, w0=(299500,'J/mol'), E0=(21110.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_Sp-5CO-3BrCCClFO_5CO->C_Ext-3BrCClF-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_Sp-5CO-3BrCCClFO_5CO->C_Ext-3BrCClF-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_Sp-5CO-3BrCCClFO_5CO->C_Ext-3BrCClF-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3BrCClFO->O_N-1BrClFO->Br_1ClFO-u0_Ext-3BrCClF-R_4R!H->Cl_N-1ClFO->F_1ClO->O_Ext-3BrCClF-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_Sp-5CO-3BrCCClFO_5CO->C_Ext-3BrCClF-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 557,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_N-7R!H->F_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.47947e+07,'m^3/(mol*s)'), n=-0.480125, w0=(327000,'J/mol'), E0=(74234.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.024832817385073626, var=0.5909097545429439, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_N-7R!H->F_Ext-3C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_N-7R!H->F_Ext-3C-R
    Total Standard Deviation in ln(k): 1.6034469914053209"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_N-7R!H->F_Ext-3C-R
Total Standard Deviation in ln(k): 1.6034469914053209""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_N-7R!H->F_Ext-3C-R
Total Standard Deviation in ln(k): 1.6034469914053209
""",
)

entry(
    index = 558,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_N-5R!H->Cl_N-4BrCFINOPSSi->Br_N-5BrCFO->C_Ext-1C-R_5BrFO->Br",
    kinetics = ArrheniusBM(A=(5e+06,'m^3/(mol*s)'), n=0, w0=(327000,'J/mol'), E0=(61358.3,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_N-5R!H->Cl_N-4BrCFINOPSSi->Br_N-5BrCFO->C_Ext-1C-R_5BrFO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_N-5R!H->Cl_N-4BrCFINOPSSi->Br_N-5BrCFO->C_Ext-1C-R_5BrFO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_N-5R!H->Cl_N-4BrCFINOPSSi->Br_N-5BrCFO->C_Ext-1C-R_5BrFO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_N-5R!H->Cl_N-4BrCFINOPSSi->Br_N-5BrCFO->C_Ext-1C-R_5BrFO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 559,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_N-5R!H->Cl_N-4BrCFINOPSSi->Br_N-5BrCFO->C_Ext-1C-R_N-5BrFO->Br",
    kinetics = ArrheniusBM(A=(1.76573e+07,'m^3/(mol*s)'), n=-0.204697, w0=(327000,'J/mol'), E0=(47470.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_N-5R!H->Cl_N-4BrCFINOPSSi->Br_N-5BrCFO->C_Ext-1C-R_N-5BrFO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_N-5R!H->Cl_N-4BrCFINOPSSi->Br_N-5BrCFO->C_Ext-1C-R_N-5BrFO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_N-5R!H->Cl_N-4BrCFINOPSSi->Br_N-5BrCFO->C_Ext-1C-R_N-5BrFO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_N-5R!H->Cl_N-4BrCFINOPSSi->Br_N-5BrCFO->C_Ext-1C-R_N-5BrFO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 560,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-3ClF->F_6BrCClINOPSSi->C_Ext-6C-R_7R!H->Cl",
    kinetics = ArrheniusBM(A=(2.2e+07,'m^3/(mol*s)'), n=0, w0=(283500,'J/mol'), E0=(47431.1,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-3ClF->F_6BrCClINOPSSi->C_Ext-6C-R_7R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-3ClF->F_6BrCClINOPSSi->C_Ext-6C-R_7R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-3ClF->F_6BrCClINOPSSi->C_Ext-6C-R_7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-3ClF->F_6BrCClINOPSSi->C_Ext-6C-R_7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 561,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-3ClF->F_6BrCClINOPSSi->C_Ext-6C-R_N-7R!H->Cl",
    kinetics = ArrheniusBM(A=(1.37228e+13,'m^3/(mol*s)'), n=-1.45412, w0=(283500,'J/mol'), E0=(56341.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-3ClF->F_6BrCClINOPSSi->C_Ext-6C-R_N-7R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-3ClF->F_6BrCClINOPSSi->C_Ext-6C-R_N-7R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-3ClF->F_6BrCClINOPSSi->C_Ext-6C-R_N-7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_4R!H->Cl_N-3CClFO->O_N-3CClF->C_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-3ClF->F_6BrCClINOPSSi->C_Ext-6C-R_N-7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 562,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_N-3CClO->Cl_Ext-4CFO-R_3CO->C_Ext-4CFO-R",
    kinetics = ArrheniusBM(A=(4.24293e-05,'m^3/(mol*s)'), n=3.13493, w0=(327000,'J/mol'), E0=(66034.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0004017641776887628, var=14.112966075722639, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_N-3CClO->Cl_Ext-4CFO-R_3CO->C_Ext-4CFO-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_N-3CClO->Cl_Ext-4CFO-R_3CO->C_Ext-4CFO-R
    Total Standard Deviation in ln(k): 7.532243398836198"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_N-3CClO->Cl_Ext-4CFO-R_3CO->C_Ext-4CFO-R
Total Standard Deviation in ln(k): 7.532243398836198""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_N-3CClO->Cl_Ext-4CFO-R_3CO->C_Ext-4CFO-R
Total Standard Deviation in ln(k): 7.532243398836198
""",
)

entry(
    index = 563,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_N-3CClO->Cl_Ext-4CFO-R_N-3CO->C_3O-u1",
    kinetics = ArrheniusBM(A=(0.186883,'m^3/(mol*s)'), n=2.60235, w0=(299500,'J/mol'), E0=(41199.9,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_N-3CClO->Cl_Ext-4CFO-R_N-3CO->C_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_N-3CClO->Cl_Ext-4CFO-R_N-3CO->C_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_N-3CClO->Cl_Ext-4CFO-R_N-3CO->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_N-3CClO->Cl_Ext-4CFO-R_N-3CO->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 564,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_N-3CClO->Cl_Ext-4CFO-R_N-3CO->C_N-3O-u1",
    kinetics = ArrheniusBM(A=(48.9307,'m^3/(mol*s)'), n=1.947, w0=(299500,'J/mol'), E0=(69755.5,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_N-3CClO->Cl_Ext-4CFO-R_N-3CO->C_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_N-3CClO->Cl_Ext-4CFO-R_N-3CO->C_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_N-3CClO->Cl_Ext-4CFO-R_N-3CO->C_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_N-3CClO->Cl_Ext-4CFO-R_N-3CO->C_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 565,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_N-7R!H->F_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(5.24678e+07,'m^3/(mol*s)'), n=-0.63187, w0=(327000,'J/mol'), E0=(74727.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.029674732665606704, var=0.7744113131902334, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_N-7R!H->F_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_N-7R!H->F_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 1.8387393842076851"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_N-7R!H->F_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 1.8387393842076851""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_N-7R!H->F_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 1.8387393842076851
""",
)

entry(
    index = 566,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_N-3CClO->Cl_Ext-4CFO-R_3CO->C_Ext-4CFO-R_Ext-4CFO-R",
    kinetics = ArrheniusBM(A=(0.21039,'m^3/(mol*s)'), n=1.87409, w0=(327000,'J/mol'), E0=(75354.4,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_N-3CClO->Cl_Ext-4CFO-R_3CO->C_Ext-4CFO-R_Ext-4CFO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_N-3CClO->Cl_Ext-4CFO-R_3CO->C_Ext-4CFO-R_Ext-4CFO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_N-3CClO->Cl_Ext-4CFO-R_3CO->C_Ext-4CFO-R_Ext-4CFO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_1C-u0_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->Br_Ext-1C-R_N-3CClFO->F_N-3CClO->Cl_Ext-4CFO-R_3CO->C_Ext-4CFO-R_Ext-4CFO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 567,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_N-7R!H->F_Ext-3C-R_Ext-3C-R_7CCl->C",
    kinetics = ArrheniusBM(A=(3.42833e+06,'m^3/(mol*s)'), n=-0.276479, w0=(327000,'J/mol'), E0=(74721.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.02582194022418881, var=1.2872060053735992, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_N-7R!H->F_Ext-3C-R_Ext-3C-R_7CCl->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_N-7R!H->F_Ext-3C-R_Ext-3C-R_7CCl->C
    Total Standard Deviation in ln(k): 2.3393534634248816"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_N-7R!H->F_Ext-3C-R_Ext-3C-R_7CCl->C
Total Standard Deviation in ln(k): 2.3393534634248816""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_N-7R!H->F_Ext-3C-R_Ext-3C-R_7CCl->C
Total Standard Deviation in ln(k): 2.3393534634248816
""",
)

entry(
    index = 568,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_N-7R!H->F_Ext-3C-R_Ext-3C-R_N-7CCl->C",
    kinetics = ArrheniusBM(A=(360000,'m^3/(mol*s)'), n=0, w0=(327000,'J/mol'), E0=(64966.7,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_N-7R!H->F_Ext-3C-R_Ext-3C-R_N-7CCl->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_N-7R!H->F_Ext-3C-R_Ext-3C-R_N-7CCl->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_N-7R!H->F_Ext-3C-R_Ext-3C-R_N-7CCl->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_N-7R!H->F_Ext-3C-R_Ext-3C-R_N-7CCl->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 569,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_N-7R!H->F_Ext-3C-R_Ext-3C-R_7CCl->C_Ext-7C-R",
    kinetics = ArrheniusBM(A=(2.10333e+06,'m^3/(mol*s)'), n=0, w0=(327000,'J/mol'), E0=(83849.7,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_N-7R!H->F_Ext-3C-R_Ext-3C-R_7CCl->C_Ext-7C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_N-7R!H->F_Ext-3C-R_Ext-3C-R_7CCl->C_Ext-7C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_N-7R!H->F_Ext-3C-R_Ext-3C-R_7CCl->C_Ext-7C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClFO->Br_Ext-3CClFO-R_N-4R!H->Cl_3CClFO->C_Sp-4BrCFINOPSSi-3C_3C-u1_Ext-1C-R_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_N-7R!H->F_Ext-3C-R_Ext-3C-R_7CCl->C_Ext-7C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

