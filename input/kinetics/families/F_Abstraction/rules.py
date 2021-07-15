#!/usr/bin/env python
# encoding: utf-8

name = "F_Abstraction/rules"
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
    kinetics = ArrheniusBM(A=(8.78467e+28,'m^3/(mol*s)'), n=-6.38448, w0=(410841,'J/mol'), E0=(205137,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.4887935728354616, var=22.80004405709894, Tref=1000.0, N=132, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 132 training reactions at node Root
    Total Standard Deviation in ln(k): 10.800612597165474"""),
    rank = 11,
    shortDesc = """BM rule fitted to 132 training reactions at node Root
Total Standard Deviation in ln(k): 10.800612597165474""",
    longDesc = 
"""
BM rule fitted to 132 training reactions at node Root
Total Standard Deviation in ln(k): 10.800612597165474
""",
)

entry(
    index = 2,
    label = "Root_1R->O",
    kinetics = ArrheniusBM(A=(0.00546156,'m^3/(mol*s)'), n=2.85856, w0=(330803,'J/mol'), E0=(118159,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.01847775776966147, var=14.542108210780928, Tref=1000.0, N=33, data_mean=0.0, correlation='Root_1R->O',), comment="""BM rule fitted to 33 training reactions at node Root_1R->O
    Total Standard Deviation in ln(k): 7.691306573373309"""),
    rank = 11,
    shortDesc = """BM rule fitted to 33 training reactions at node Root_1R->O
Total Standard Deviation in ln(k): 7.691306573373309""",
    longDesc = 
"""
BM rule fitted to 33 training reactions at node Root_1R->O
Total Standard Deviation in ln(k): 7.691306573373309
""",
)

entry(
    index = 3,
    label = "Root_N-1R->O",
    kinetics = ArrheniusBM(A=(8.04071e+36,'m^3/(mol*s)'), n=-8.74359, w0=(437520,'J/mol'), E0=(223213,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.6040793280768137, var=25.261291199878976, Tref=1000.0, N=99, data_mean=0.0, correlation='Root_N-1R->O',), comment="""BM rule fitted to 99 training reactions at node Root_N-1R->O
    Total Standard Deviation in ln(k): 11.593708447982996"""),
    rank = 11,
    shortDesc = """BM rule fitted to 99 training reactions at node Root_N-1R->O
Total Standard Deviation in ln(k): 11.593708447982996""",
    longDesc = 
"""
BM rule fitted to 99 training reactions at node Root_N-1R->O
Total Standard Deviation in ln(k): 11.593708447982996
""",
)

entry(
    index = 4,
    label = "Root_1R->O_3R->O",
    kinetics = ArrheniusBM(A=(1.57248e+58,'m^3/(mol*s)'), n=-14.8465, w0=(222000,'J/mol'), E0=(237010,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.7953720767048976, var=9.868724280704338, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R->O_3R->O',), comment="""BM rule fitted to 6 training reactions at node Root_1R->O_3R->O
    Total Standard Deviation in ln(k): 8.29620247426518"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R->O_3R->O
Total Standard Deviation in ln(k): 8.29620247426518""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R->O_3R->O
Total Standard Deviation in ln(k): 8.29620247426518
""",
)

entry(
    index = 5,
    label = "Root_1R->O_N-3R->O",
    kinetics = ArrheniusBM(A=(9.8225e-14,'m^3/(mol*s)'), n=5.99395, w0=(354981,'J/mol'), E0=(35498.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.15516074885255043, var=16.149763058025595, Tref=1000.0, N=27, data_mean=0.0, correlation='Root_1R->O_N-3R->O',), comment="""BM rule fitted to 27 training reactions at node Root_1R->O_N-3R->O
    Total Standard Deviation in ln(k): 8.446233432326483"""),
    rank = 11,
    shortDesc = """BM rule fitted to 27 training reactions at node Root_1R->O_N-3R->O
Total Standard Deviation in ln(k): 8.446233432326483""",
    longDesc = 
"""
BM rule fitted to 27 training reactions at node Root_1R->O_N-3R->O
Total Standard Deviation in ln(k): 8.446233432326483
""",
)

entry(
    index = 6,
    label = "Root_N-1R->O_3R->O",
    kinetics = ArrheniusBM(A=(6.15784e-13,'m^3/(mol*s)'), n=6.04834, w0=(354981,'J/mol'), E0=(35498.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1745085862731796, var=8.471305790924811, Tref=1000.0, N=27, data_mean=0.0, correlation='Root_N-1R->O_3R->O',), comment="""BM rule fitted to 27 training reactions at node Root_N-1R->O_3R->O
    Total Standard Deviation in ln(k): 6.273347009888863"""),
    rank = 11,
    shortDesc = """BM rule fitted to 27 training reactions at node Root_N-1R->O_3R->O
Total Standard Deviation in ln(k): 6.273347009888863""",
    longDesc = 
"""
BM rule fitted to 27 training reactions at node Root_N-1R->O_3R->O
Total Standard Deviation in ln(k): 6.273347009888863
""",
)

entry(
    index = 7,
    label = "Root_N-1R->O_N-3R->O",
    kinetics = ArrheniusBM(A=(3.14522e+34,'m^3/(mol*s)'), n=-8.13683, w0=(468472,'J/mol'), E0=(215568,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.5495326535589553, var=32.748389657870675, Tref=1000.0, N=72, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O',), comment="""BM rule fitted to 72 training reactions at node Root_N-1R->O_N-3R->O
    Total Standard Deviation in ln(k): 12.853074109491555"""),
    rank = 11,
    shortDesc = """BM rule fitted to 72 training reactions at node Root_N-1R->O_N-3R->O
Total Standard Deviation in ln(k): 12.853074109491555""",
    longDesc = 
"""
BM rule fitted to 72 training reactions at node Root_N-1R->O_N-3R->O
Total Standard Deviation in ln(k): 12.853074109491555
""",
)

entry(
    index = 8,
    label = "Root_1R->O_3R->O_Ext-1O-R",
    kinetics = ArrheniusBM(A=(9.50684e+53,'m^3/(mol*s)'), n=-13.5934, w0=(222000,'J/mol'), E0=(225074,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.08753785633515945, var=28.008039755476897, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-1O-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->O_3R->O_Ext-1O-R
    Total Standard Deviation in ln(k): 10.829528140188767"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->O_3R->O_Ext-1O-R
Total Standard Deviation in ln(k): 10.829528140188767""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->O_3R->O_Ext-1O-R
Total Standard Deviation in ln(k): 10.829528140188767
""",
)

entry(
    index = 9,
    label = "Root_1R->O_3R->O_1O-u0",
    kinetics = ArrheniusBM(A=(2.99935e-05,'m^3/(mol*s)'), n=4.01289, w0=(222000,'J/mol'), E0=(22200,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_1O-u0',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_1O-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_1O-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_1O-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_1R->O_3R->O_N-1O-u0",
    kinetics = ArrheniusBM(A=(0.329575,'m^3/(mol*s)'), n=2.30206, w0=(222000,'J/mol'), E0=(120704,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03713926538722931, var=0.10946379467839873, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_3R->O_N-1O-u0',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_N-1O-u0
    Total Standard Deviation in ln(k): 0.7565876155043457"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_N-1O-u0
Total Standard Deviation in ln(k): 0.7565876155043457""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_N-1O-u0
Total Standard Deviation in ln(k): 0.7565876155043457
""",
)

entry(
    index = 11,
    label = "Root_1R->O_N-3R->O_3CFH->C",
    kinetics = ArrheniusBM(A=(2.09273e-14,'m^3/(mol*s)'), n=6.16638, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1624935529159007, var=13.168511404316224, Tref=1000.0, N=26, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CFH->C',), comment="""BM rule fitted to 26 training reactions at node Root_1R->O_N-3R->O_3CFH->C
    Total Standard Deviation in ln(k): 7.683146841680539"""),
    rank = 11,
    shortDesc = """BM rule fitted to 26 training reactions at node Root_1R->O_N-3R->O_3CFH->C
Total Standard Deviation in ln(k): 7.683146841680539""",
    longDesc = 
"""
BM rule fitted to 26 training reactions at node Root_1R->O_N-3R->O_3CFH->C
Total Standard Deviation in ln(k): 7.683146841680539
""",
)

entry(
    index = 12,
    label = "Root_1R->O_N-3R->O_N-3CFH->C",
    kinetics = ArrheniusBM(A=(188.681,'m^3/(mol*s)'), n=2.15358, w0=(393500,'J/mol'), E0=(39350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-3CFH->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-3CFH->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-3CFH->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-3CFH->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "Root_N-1R->O_3R->O_Ext-3O-R",
    kinetics = ArrheniusBM(A=(2.04599e-12,'m^3/(mol*s)'), n=5.95128, w0=(357500,'J/mol'), E0=(35750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.15636523448813933, var=7.948211212813177, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R
    Total Standard Deviation in ln(k): 6.044741293489853"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R
Total Standard Deviation in ln(k): 6.044741293489853""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R
Total Standard Deviation in ln(k): 6.044741293489853
""",
)

entry(
    index = 14,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0",
    kinetics = ArrheniusBM(A=(2.21956e-19,'m^3/(mol*s)'), n=7.9755, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2788693585598425, var=6.43973158053964, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0
    Total Standard Deviation in ln(k): 5.7880180522067635"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0
Total Standard Deviation in ln(k): 5.7880180522067635""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0
Total Standard Deviation in ln(k): 5.7880180522067635
""",
)

entry(
    index = 15,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0",
    kinetics = ArrheniusBM(A=(0.000177411,'m^3/(mol*s)'), n=3.4339, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05134086265292892, var=14.958473479399446, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0
    Total Standard Deviation in ln(k): 7.882547775402072"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0
Total Standard Deviation in ln(k): 7.882547775402072""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0
Total Standard Deviation in ln(k): 7.882547775402072
""",
)

entry(
    index = 16,
    label = "Root_N-1R->O_N-3R->O_3CFH->F",
    kinetics = ArrheniusBM(A=(97385.7,'m^3/(mol*s)'), n=0.73315, w0=(331429,'J/mol'), E0=(33142.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04543208822892779, var=1.9573248697977497, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_3CFH->F',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_3CFH->F
    Total Standard Deviation in ln(k): 2.9188640986166017"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_3CFH->F
Total Standard Deviation in ln(k): 2.9188640986166017""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_3CFH->F
Total Standard Deviation in ln(k): 2.9188640986166017
""",
)

entry(
    index = 17,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F",
    kinetics = ArrheniusBM(A=(9.2666e+22,'m^3/(mol*s)'), n=-4.74688, w0=(483231,'J/mol'), E0=(192934,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.37212390103520143, var=34.96715900087185, Tref=1000.0, N=65, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F',), comment="""BM rule fitted to 65 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F
    Total Standard Deviation in ln(k): 12.789591747363197"""),
    rank = 11,
    shortDesc = """BM rule fitted to 65 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F
Total Standard Deviation in ln(k): 12.789591747363197""",
    longDesc = 
"""
BM rule fitted to 65 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F
Total Standard Deviation in ln(k): 12.789591747363197
""",
)

entry(
    index = 18,
    label = "Root_1R->O_3R->O_Ext-1O-R_3O-u1",
    kinetics = ArrheniusBM(A=(0.0487535,'m^3/(mol*s)'), n=3.06244, w0=(222000,'J/mol'), E0=(22200,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-1O-R_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_1R->O_3R->O_Ext-1O-R_N-3O-u1",
    kinetics = ArrheniusBM(A=(6.52723,'m^3/(mol*s)'), n=1.98959, w0=(222000,'J/mol'), E0=(118211,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.02935573976520705, var=0.14075700629316643, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-1O-R_N-3O-u1',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_Ext-1O-R_N-3O-u1
    Total Standard Deviation in ln(k): 0.8258865615642318"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_Ext-1O-R_N-3O-u1
Total Standard Deviation in ln(k): 0.8258865615642318""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_Ext-1O-R_N-3O-u1
Total Standard Deviation in ln(k): 0.8258865615642318
""",
)

entry(
    index = 20,
    label = "Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_4R!H->C",
    kinetics = ArrheniusBM(A=(0.0552802,'m^3/(mol*s)'), n=2.52847, w0=(222000,'J/mol'), E0=(119820,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.00111026,'m^3/(mol*s)'), n=2.89721, w0=(222000,'J/mol'), E0=(106112,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_1R->O_N-3R->O_3CFH->C_3C-u1",
    kinetics = ArrheniusBM(A=(1.24823e-19,'m^3/(mol*s)'), n=7.67739, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.24722111772064775, var=4.931576187700041, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CFH->C_3C-u1',), comment="""BM rule fitted to 17 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1
    Total Standard Deviation in ln(k): 5.073104330523289"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1
Total Standard Deviation in ln(k): 5.073104330523289""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1
Total Standard Deviation in ln(k): 5.073104330523289
""",
)

entry(
    index = 23,
    label = "Root_1R->O_N-3R->O_3CFH->C_N-3C-u1",
    kinetics = ArrheniusBM(A=(0.000154549,'m^3/(mol*s)'), n=3.31223, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0024525976788391177, var=19.525205422314997, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CFH->C_N-3C-u1',), comment="""BM rule fitted to 9 training reactions at node Root_1R->O_N-3R->O_3CFH->C_N-3C-u1
    Total Standard Deviation in ln(k): 8.864552277854601"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1R->O_N-3R->O_3CFH->C_N-3C-u1
Total Standard Deviation in ln(k): 8.864552277854601""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1R->O_N-3R->O_3CFH->C_N-3C-u1
Total Standard Deviation in ln(k): 8.864552277854601
""",
)

entry(
    index = 24,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C",
    kinetics = ArrheniusBM(A=(1.42819e-06,'m^3/(mol*s)'), n=4.29373, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(1.47722e-11,'m^3/(mol*s)'), n=5.6801, w0=(357944,'J/mol'), E0=(35794.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.13954016191919755, var=9.063544844171751, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C
    Total Standard Deviation in ln(k): 6.386003071910343"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C
Total Standard Deviation in ln(k): 6.386003071910343""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C
Total Standard Deviation in ln(k): 6.386003071910343
""",
)

entry(
    index = 26,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi",
    kinetics = ArrheniusBM(A=(1.72013,'m^3/(mol*s)'), n=2.4493, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi",
    kinetics = ArrheniusBM(A=(1.00581e-18,'m^3/(mol*s)'), n=7.78025, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2691554807570094, var=7.0999581494971755, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi
    Total Standard Deviation in ln(k): 6.018036350970901"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi
Total Standard Deviation in ln(k): 6.018036350970901""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi
Total Standard Deviation in ln(k): 6.018036350970901
""",
)

entry(
    index = 28,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(0.00939528,'m^3/(mol*s)'), n=2.92328, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.026294303046248396, var=16.885074199594314, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 8.303813590284808"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 8.303813590284808""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 8.303813590284808
""",
)

entry(
    index = 29,
    label = "Root_N-1R->O_N-3R->O_3CFH->F_1BrCClFHINPSSi->H",
    kinetics = ArrheniusBM(A=(0.0577854,'m^3/(mol*s)'), n=2.62625, w0=(360000,'J/mol'), E0=(36000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.3854301666465253, var=0.9609060278365511, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_3CFH->F_1BrCClFHINPSSi->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_3CFH->F_1BrCClFHINPSSi->H
    Total Standard Deviation in ln(k): 2.933575389249798"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_3CFH->F_1BrCClFHINPSSi->H
Total Standard Deviation in ln(k): 2.933575389249798""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_3CFH->F_1BrCClFHINPSSi->H
Total Standard Deviation in ln(k): 2.933575389249798
""",
)

entry(
    index = 30,
    label = "Root_N-1R->O_N-3R->O_3CFH->F_N-1BrCClFHINPSSi->H",
    kinetics = ArrheniusBM(A=(3.01413e+07,'m^3/(mol*s)'), n=-0.0240909, w0=(320000,'J/mol'), E0=(32000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0386306418606146, var=1.5732727919425211, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_3CFH->F_N-1BrCClFHINPSSi->H',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_3CFH->F_N-1BrCClFHINPSSi->H
    Total Standard Deviation in ln(k): 2.6116045596714987"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_3CFH->F_N-1BrCClFHINPSSi->H
Total Standard Deviation in ln(k): 2.6116045596714987""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_3CFH->F_N-1BrCClFHINPSSi->H
Total Standard Deviation in ln(k): 2.6116045596714987
""",
)

entry(
    index = 31,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_1BrCClFHINPSSi->F",
    kinetics = ArrheniusBM(A=(3258.2,'m^3/(mol*s)'), n=0.941778, w0=(331429,'J/mol'), E0=(33142.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0299143331907759, var=2.8893453770197914, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_1BrCClFHINPSSi->F',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_1BrCClFHINPSSi->F
    Total Standard Deviation in ln(k): 3.482825266877825"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_1BrCClFHINPSSi->F
Total Standard Deviation in ln(k): 3.482825266877825""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_1BrCClFHINPSSi->F
Total Standard Deviation in ln(k): 3.482825266877825
""",
)

entry(
    index = 32,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F",
    kinetics = ArrheniusBM(A=(11.0527,'m^3/(mol*s)'), n=1.73736, w0=(501552,'J/mol'), E0=(149963,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03761997933070907, var=38.555754927633984, Tref=1000.0, N=58, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F',), comment="""BM rule fitted to 58 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F
    Total Standard Deviation in ln(k): 12.542580325369455"""),
    rank = 11,
    shortDesc = """BM rule fitted to 58 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F
Total Standard Deviation in ln(k): 12.542580325369455""",
    longDesc = 
"""
BM rule fitted to 58 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F
Total Standard Deviation in ln(k): 12.542580325369455
""",
)

entry(
    index = 33,
    label = "Root_1R->O_3R->O_Ext-1O-R_N-3O-u1_4R!H->C",
    kinetics = ArrheniusBM(A=(0.640932,'m^3/(mol*s)'), n=2.39839, w0=(222000,'J/mol'), E0=(123802,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-1O-R_N-3O-u1_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_N-3O-u1_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_N-3O-u1_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_N-3O-u1_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Root_1R->O_3R->O_Ext-1O-R_N-3O-u1_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.0839177,'m^3/(mol*s)'), n=2.53937, w0=(222000,'J/mol'), E0=(112434,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-1O-R_N-3O-u1_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_N-3O-u1_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_N-3O-u1_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_N-3O-u1_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 35,
    label = "Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.49137e-20,'m^3/(mol*s)'), n=7.81578, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.25504555942845647, var=4.626033160428342, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R',), comment="""BM rule fitted to 15 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R
    Total Standard Deviation in ln(k): 4.952645311352376"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R
Total Standard Deviation in ln(k): 4.952645311352376""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R
Total Standard Deviation in ln(k): 4.952645311352376
""",
)

entry(
    index = 36,
    label = "Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-1O-R_4R!H->C",
    kinetics = ArrheniusBM(A=(0.000476496,'m^3/(mol*s)'), n=3.27616, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-1O-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-1O-R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-1O-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-1O-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-1O-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.000849095,'m^3/(mol*s)'), n=3.17369, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-1O-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-1O-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-1O-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-1O-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 38,
    label = "Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0",
    kinetics = ArrheniusBM(A=(0.00462438,'m^3/(mol*s)'), n=2.88898, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.026219391307740456, var=20.34067741353229, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0',), comment="""BM rule fitted to 8 training reactions at node Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0
    Total Standard Deviation in ln(k): 9.107361398467269"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0
Total Standard Deviation in ln(k): 9.107361398467269""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0
Total Standard Deviation in ln(k): 9.107361398467269
""",
)

entry(
    index = 39,
    label = "Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_N-1O-u0",
    kinetics = ArrheniusBM(A=(0.0391196,'m^3/(mol*s)'), n=2.49957, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_N-1O-u0',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_N-1O-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_N-1O-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_N-1O-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 40,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C",
    kinetics = ArrheniusBM(A=(7.55574e-13,'m^3/(mol*s)'), n=6.0254, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.15819783577559415, var=6.314678996638406, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C
    Total Standard Deviation in ln(k): 5.435185796085838"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C
Total Standard Deviation in ln(k): 5.435185796085838""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C
Total Standard Deviation in ln(k): 5.435185796085838
""",
)

entry(
    index = 41,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_N-1BrCClFHINPSSi->C",
    kinetics = ArrheniusBM(A=(0.0192658,'m^3/(mol*s)'), n=3.05869, w0=(393500,'J/mol'), E0=(39350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_N-1BrCClFHINPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_N-1BrCClFHINPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_N-1BrCClFHINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_N-1BrCClFHINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi",
    kinetics = ArrheniusBM(A=(4.17491e-22,'m^3/(mol*s)'), n=8.83058, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3362193007036281, var=26.408898740619986, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi
    Total Standard Deviation in ln(k): 11.147023312568622"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi
Total Standard Deviation in ln(k): 11.147023312568622""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi
Total Standard Deviation in ln(k): 11.147023312568622
""",
)

entry(
    index = 43,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi",
    kinetics = ArrheniusBM(A=(4.93688e-17,'m^3/(mol*s)'), n=7.25509, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2356235707682487, var=6.083619708854371, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi
    Total Standard Deviation in ln(k): 5.536697057720324"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi
Total Standard Deviation in ln(k): 5.536697057720324""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi
Total Standard Deviation in ln(k): 5.536697057720324
""",
)

entry(
    index = 44,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi",
    kinetics = ArrheniusBM(A=(0.532224,'m^3/(mol*s)'), n=2.40066, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0028685516197031035, var=21.020464677530406, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi
    Total Standard Deviation in ln(k): 9.198532898208695"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi
Total Standard Deviation in ln(k): 9.198532898208695""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi
Total Standard Deviation in ln(k): 9.198532898208695
""",
)

entry(
    index = 45,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H-1BrCClFHINPSSi",
    kinetics = ArrheniusBM(A=(0.0387235,'m^3/(mol*s)'), n=2.8378, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H-1BrCClFHINPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H-1BrCClFHINPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H-1BrCClFHINPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H-1BrCClFHINPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "Root_N-1R->O_N-3R->O_3CFH->F_N-1BrCClFHINPSSi->H_Ext-1CF-R",
    kinetics = ArrheniusBM(A=(9.97654e+07,'m^3/(mol*s)'), n=-0.200889, w0=(320000,'J/mol'), E0=(32000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0265584834573785, var=2.3657766429344305, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_3CFH->F_N-1BrCClFHINPSSi->H_Ext-1CF-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_3CFH->F_N-1BrCClFHINPSSi->H_Ext-1CF-R
    Total Standard Deviation in ln(k): 3.150229194194175"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_3CFH->F_N-1BrCClFHINPSSi->H_Ext-1CF-R
Total Standard Deviation in ln(k): 3.150229194194175""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_3CFH->F_N-1BrCClFHINPSSi->H_Ext-1CF-R
Total Standard Deviation in ln(k): 3.150229194194175
""",
)

entry(
    index = 47,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_1BrCClFHINPSSi->F_3CH->C",
    kinetics = ArrheniusBM(A=(48339.6,'m^3/(mol*s)'), n=0.436192, w0=(320000,'J/mol'), E0=(32000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.02408438344513273, var=0.5019752739533132, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_1BrCClFHINPSSi->F_3CH->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_1BrCClFHINPSSi->F_3CH->C
    Total Standard Deviation in ln(k): 1.4808726067825593"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_1BrCClFHINPSSi->F_3CH->C
Total Standard Deviation in ln(k): 1.4808726067825593""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_1BrCClFHINPSSi->F_3CH->C
Total Standard Deviation in ln(k): 1.4808726067825593
""",
)

entry(
    index = 48,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_1BrCClFHINPSSi->F_N-3CH->C",
    kinetics = ArrheniusBM(A=(3.84296,'m^3/(mol*s)'), n=2.20574, w0=(360000,'J/mol'), E0=(36000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.6692812243519491, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_1BrCClFHINPSSi->F_N-3CH->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_1BrCClFHINPSSi->F_N-3CH->C
    Total Standard Deviation in ln(k): 3.6467690015748317"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_1BrCClFHINPSSi->F_N-3CH->C
Total Standard Deviation in ln(k): 3.6467690015748317""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_1BrCClFHINPSSi->F_N-3CH->C
Total Standard Deviation in ln(k): 3.6467690015748317
""",
)

entry(
    index = 49,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C",
    kinetics = ArrheniusBM(A=(0.00201846,'m^3/(mol*s)'), n=2.92936, w0=(495435,'J/mol'), E0=(140657,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.013273464069812071, var=35.17687532448327, Tref=1000.0, N=46, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C',), comment="""BM rule fitted to 46 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C
    Total Standard Deviation in ln(k): 11.923453477632396"""),
    rank = 11,
    shortDesc = """BM rule fitted to 46 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C
Total Standard Deviation in ln(k): 11.923453477632396""",
    longDesc = 
"""
BM rule fitted to 46 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C
Total Standard Deviation in ln(k): 11.923453477632396
""",
)

entry(
    index = 50,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_N-1CH->C",
    kinetics = ArrheniusBM(A=(5.74191e+09,'m^3/(mol*s)'), n=-1.17425, w0=(525000,'J/mol'), E0=(173669,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.15328163565144917, var=51.25100260613659, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_N-1CH->C',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_N-1CH->C
    Total Standard Deviation in ln(k): 14.736989177506622"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_N-1CH->C
Total Standard Deviation in ln(k): 14.736989177506622""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_N-1CH->C
Total Standard Deviation in ln(k): 14.736989177506622
""",
)

entry(
    index = 51,
    label = "Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(5.49046e-26,'m^3/(mol*s)'), n=9.38964, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3327689673506645, var=0.07407895714845698, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_4R!H->Cl',), comment="""BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_4R!H->Cl
    Total Standard Deviation in ln(k): 1.3817406955698213"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_4R!H->Cl
Total Standard Deviation in ln(k): 1.3817406955698213""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_4R!H->Cl
Total Standard Deviation in ln(k): 1.3817406955698213
""",
)

entry(
    index = 52,
    label = "Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(9.85923e-19,'m^3/(mol*s)'), n=7.42231, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2356147074001311, var=3.7329384146101683, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl',), comment="""BM rule fitted to 12 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 4.465308044127896"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 4.465308044127896""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 4.465308044127896
""",
)

entry(
    index = 53,
    label = "Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.297177,'m^3/(mol*s)'), n=2.33269, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.05689406089570303, var=23.671972508903306, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R',), comment="""BM rule fitted to 7 training reactions at node Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R
    Total Standard Deviation in ln(k): 9.896758146301446"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R
Total Standard Deviation in ln(k): 9.896758146301446""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R
Total Standard Deviation in ln(k): 9.896758146301446
""",
)

entry(
    index = 54,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.10562e-12,'m^3/(mol*s)'), n=5.94627, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.15356899515662342, var=7.323710128631917, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R
    Total Standard Deviation in ln(k): 5.811136813440013"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 5.811136813440013""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 5.811136813440013
""",
)

entry(
    index = 55,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(7.11294e-15,'m^3/(mol*s)'), n=6.71706, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.5134766165460327, var=0.690220448585621, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 10.493354714095197"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 10.493354714095197""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 10.493354714095197
""",
)

entry(
    index = 56,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(5.23275e-18,'m^3/(mol*s)'), n=7.56477, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.688102149872853, var=29.172611800688376, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 22.607061343265773"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 22.607061343265773""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 22.607061343265773
""",
)

entry(
    index = 57,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_4R!H->Cl",
    kinetics = ArrheniusBM(A=(0.00381903,'m^3/(mol*s)'), n=3.24993, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_4R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_4R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 58,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(2.26272e-14,'m^3/(mol*s)'), n=6.42856, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1980139044022901, var=3.0656399567510455, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-4R!H->Cl',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-4R!H->Cl
    Total Standard Deviation in ln(k): 4.0076068065297195"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-4R!H->Cl
Total Standard Deviation in ln(k): 4.0076068065297195""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-4R!H->Cl
Total Standard Deviation in ln(k): 4.0076068065297195
""",
)

entry(
    index = 59,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->C",
    kinetics = ArrheniusBM(A=(2.62347,'m^3/(mol*s)'), n=2.22813, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2963153646008864, var=29.457481448673217, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->C
    Total Standard Deviation in ln(k): 11.625159847610592"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->C
Total Standard Deviation in ln(k): 11.625159847610592""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->C
Total Standard Deviation in ln(k): 11.625159847610592
""",
)

entry(
    index = 60,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.183755,'m^3/(mol*s)'), n=2.51569, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.01910788558130034, var=37.3303580558227, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->C
    Total Standard Deviation in ln(k): 12.296655310086123"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->C
Total Standard Deviation in ln(k): 12.296655310086123""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->C
Total Standard Deviation in ln(k): 12.296655310086123
""",
)

entry(
    index = 61,
    label = "Root_N-1R->O_N-3R->O_3CFH->F_N-1BrCClFHINPSSi->H_Ext-1CF-R_4R!H->O",
    kinetics = ArrheniusBM(A=(1.99295e+09,'m^3/(mol*s)'), n=-0.632959, w0=(320000,'J/mol'), E0=(32000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.5551482553889073, var=0.960906027836823, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_3CFH->F_N-1BrCClFHINPSSi->H_Ext-1CF-R_4R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_3CFH->F_N-1BrCClFHINPSSi->H_Ext-1CF-R_4R!H->O
    Total Standard Deviation in ln(k): 3.360002747899277"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_3CFH->F_N-1BrCClFHINPSSi->H_Ext-1CF-R_4R!H->O
Total Standard Deviation in ln(k): 3.360002747899277""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_3CFH->F_N-1BrCClFHINPSSi->H_Ext-1CF-R_4R!H->O
Total Standard Deviation in ln(k): 3.360002747899277
""",
)

entry(
    index = 62,
    label = "Root_N-1R->O_N-3R->O_3CFH->F_N-1BrCClFHINPSSi->H_Ext-1CF-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(4.9942e+06,'m^3/(mol*s)'), n=0.231181, w0=(320000,'J/mol'), E0=(32000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.127722950403335, var=26.079836360346846, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_3CFH->F_N-1BrCClFHINPSSi->H_Ext-1CF-R_N-4R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_3CFH->F_N-1BrCClFHINPSSi->H_Ext-1CF-R_N-4R!H->O
    Total Standard Deviation in ln(k): 13.071340267074275"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_3CFH->F_N-1BrCClFHINPSSi->H_Ext-1CF-R_N-4R!H->O
Total Standard Deviation in ln(k): 13.071340267074275""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_3CFH->F_N-1BrCClFHINPSSi->H_Ext-1CF-R_N-4R!H->O
Total Standard Deviation in ln(k): 13.071340267074275
""",
)

entry(
    index = 63,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_1BrCClFHINPSSi->F_3CH->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(58716.8,'m^3/(mol*s)'), n=0.378639, w0=(320000,'J/mol'), E0=(32000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.020906567161643637, var=0.2608617441749449, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_1BrCClFHINPSSi->F_3CH->C_Ext-3C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_1BrCClFHINPSSi->F_3CH->C_Ext-3C-R
    Total Standard Deviation in ln(k): 1.0764400103544418"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_1BrCClFHINPSSi->F_3CH->C_Ext-3C-R
Total Standard Deviation in ln(k): 1.0764400103544418""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_1BrCClFHINPSSi->F_3CH->C_Ext-3C-R
Total Standard Deviation in ln(k): 1.0764400103544418
""",
)

entry(
    index = 64,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0",
    kinetics = ArrheniusBM(A=(4.04966,'m^3/(mol*s)'), n=1.96977, w0=(497000,'J/mol'), E0=(144851,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.02895214053930591, var=38.35616850804335, Tref=1000.0, N=40, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0',), comment="""BM rule fitted to 40 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0
    Total Standard Deviation in ln(k): 12.488540933766275"""),
    rank = 11,
    shortDesc = """BM rule fitted to 40 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0
Total Standard Deviation in ln(k): 12.488540933766275""",
    longDesc = 
"""
BM rule fitted to 40 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0
Total Standard Deviation in ln(k): 12.488540933766275
""",
)

entry(
    index = 65,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_N-1C-u0",
    kinetics = ArrheniusBM(A=(1.64218e+07,'m^3/(mol*s)'), n=-0.105107, w0=(485000,'J/mol'), E0=(180272,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.22124444763326373, var=9.408359297958176, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_N-1C-u0',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_N-1C-u0
    Total Standard Deviation in ln(k): 6.705024281171459"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_N-1C-u0
Total Standard Deviation in ln(k): 6.705024281171459""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_N-1C-u0
Total Standard Deviation in ln(k): 6.705024281171459
""",
)

entry(
    index = 66,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_N-1CH->C_Ext-3CH-R",
    kinetics = ArrheniusBM(A=(1.7505e+12,'m^3/(mol*s)'), n=-1.96257, w0=(525000,'J/mol'), E0=(174961,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.19784793536423737, var=64.97819327940041, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_N-1CH->C_Ext-3CH-R',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_N-1CH->C_Ext-3CH-R
    Total Standard Deviation in ln(k): 16.657084854313343"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_N-1CH->C_Ext-3CH-R
Total Standard Deviation in ln(k): 16.657084854313343""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_N-1CH->C_Ext-3CH-R
Total Standard Deviation in ln(k): 16.657084854313343
""",
)

entry(
    index = 67,
    label = "Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-1O-R",
    kinetics = ArrheniusBM(A=(7.71299e-05,'m^3/(mol*s)'), n=3.03221, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-1O-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-1O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 68,
    label = "Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.85918e-06,'m^3/(mol*s)'), n=3.7472, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 69,
    label = "Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C",
    kinetics = ArrheniusBM(A=(5.74886e-16,'m^3/(mol*s)'), n=6.58226, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.18999525896923575, var=1.5650398247745507, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C',), comment="""BM rule fitted to 9 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C
    Total Standard Deviation in ln(k): 2.985329712631087"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 2.985329712631087""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 2.985329712631087
""",
)

entry(
    index = 70,
    label = "Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C",
    kinetics = ArrheniusBM(A=(4.97311e-27,'m^3/(mol*s)'), n=9.94247, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.37247305393162494, var=17.15182280551588, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C',), comment="""BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C
    Total Standard Deviation in ln(k): 9.238423995876666"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 9.238423995876666""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 9.238423995876666
""",
)

entry(
    index = 71,
    label = "Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.23084e+12,'m^3/(mol*s)'), n=-1.21549, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.24576662242553837, var=1.8464043534076287, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 3.3415874602362727"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 3.3415874602362727""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 3.3415874602362727
""",
)

entry(
    index = 72,
    label = "Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R_Ext-1O-R",
    kinetics = ArrheniusBM(A=(7.91658e-06,'m^3/(mol*s)'), n=3.24946, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R_Ext-1O-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R_Ext-1O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 73,
    label = "Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R_Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(8.18801e-11,'m^3/(mol*s)'), n=5.08894, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.2509046752593258, var=0.3198106349141868, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R_Sp-4R!H-3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R_Sp-4R!H-3C
    Total Standard Deviation in ln(k): 4.276690389631595"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R_Sp-4R!H-3C
Total Standard Deviation in ln(k): 4.276690389631595""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R_Sp-4R!H-3C
Total Standard Deviation in ln(k): 4.276690389631595
""",
)

entry(
    index = 74,
    label = "Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R_N-Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(8.02782e-05,'m^3/(mol*s)'), n=3.4195, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R_N-Sp-4R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R_N-Sp-4R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 75,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_5R!H->O",
    kinetics = ArrheniusBM(A=(3.55718e-06,'m^3/(mol*s)'), n=3.53988, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 76,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(1.56111e-13,'m^3/(mol*s)'), n=6.27134, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1742732561936205, var=8.193773201737132, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-5R!H->O',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-5R!H->O
    Total Standard Deviation in ln(k): 6.1763800720655535"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-5R!H->O
Total Standard Deviation in ln(k): 6.1763800720655535""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-5R!H->O
Total Standard Deviation in ln(k): 6.1763800720655535
""",
)

entry(
    index = 77,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_3O-u1",
    kinetics = ArrheniusBM(A=(0.0379121,'m^3/(mol*s)'), n=2.90824, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 78,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-3O-u1",
    kinetics = ArrheniusBM(A=(7.30096,'m^3/(mol*s)'), n=2.36151, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 79,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(0.0308105,'m^3/(mol*s)'), n=2.88761, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 80,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-4R!H->Cl_4CO->C",
    kinetics = ArrheniusBM(A=(2.82154e-16,'m^3/(mol*s)'), n=6.96308, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.3271961102935776, var=0.10106532836810057, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-4R!H->Cl_4CO->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-4R!H->Cl_4CO->C
    Total Standard Deviation in ln(k): 8.997110010818872"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-4R!H->Cl_4CO->C
Total Standard Deviation in ln(k): 8.997110010818872""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-4R!H->Cl_4CO->C
Total Standard Deviation in ln(k): 8.997110010818872
""",
)

entry(
    index = 81,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-4R!H->Cl_N-4CO->C",
    kinetics = ArrheniusBM(A=(0.00678858,'m^3/(mol*s)'), n=3.1372, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-4R!H->Cl_N-4CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-4R!H->Cl_N-4CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-4R!H->Cl_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-4R!H->Cl_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 82,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->C_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(0.0952393,'m^3/(mol*s)'), n=2.75763, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->C_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->C_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->C_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->C_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 83,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->C_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(0.0446012,'m^3/(mol*s)'), n=2.65475, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->C_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->C_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->C_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->C_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 84,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->C_3O-u1",
    kinetics = ArrheniusBM(A=(0.00474579,'m^3/(mol*s)'), n=2.96408, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->C_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->C_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 85,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->C_N-3O-u1",
    kinetics = ArrheniusBM(A=(1.32859,'m^3/(mol*s)'), n=2.43214, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->C_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->C_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->C_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->C_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 86,
    label = "Root_N-1R->O_N-3R->O_3CFH->F_N-1BrCClFHINPSSi->H_Ext-1CF-R_N-4R!H->O_Ext-1CF-R",
    kinetics = ArrheniusBM(A=(1.01241e+11,'m^3/(mol*s)'), n=-0.712343, w0=(320000,'J/mol'), E0=(32000,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_3CFH->F_N-1BrCClFHINPSSi->H_Ext-1CF-R_N-4R!H->O_Ext-1CF-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_3CFH->F_N-1BrCClFHINPSSi->H_Ext-1CF-R_N-4R!H->O_Ext-1CF-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_3CFH->F_N-1BrCClFHINPSSi->H_Ext-1CF-R_N-4R!H->O_Ext-1CF-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_3CFH->F_N-1BrCClFHINPSSi->H_Ext-1CF-R_N-4R!H->O_Ext-1CF-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 87,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_1BrCClFHINPSSi->F_3CH->C_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(21476.1,'m^3/(mol*s)'), n=0.504852, w0=(320000,'J/mol'), E0=(32000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.027875404831498134, var=0.2711846437048365, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_1BrCClFHINPSSi->F_3CH->C_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_1BrCClFHINPSSi->F_3CH->C_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 1.1140123528522476"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_1BrCClFHINPSSi->F_3CH->C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 1.1140123528522476""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_1BrCClFHINPSSi->F_3CH->C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 1.1140123528522476
""",
)

entry(
    index = 88,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C",
    kinetics = ArrheniusBM(A=(3.3258e-06,'m^3/(mol*s)'), n=3.71016, w0=(485000,'J/mol'), E0=(132537,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.020272401382813592, var=40.0996508285819, Tref=1000.0, N=28, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C',), comment="""BM rule fitted to 28 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C
    Total Standard Deviation in ln(k): 12.745777240055112"""),
    rank = 11,
    shortDesc = """BM rule fitted to 28 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C
Total Standard Deviation in ln(k): 12.745777240055112""",
    longDesc = 
"""
BM rule fitted to 28 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C
Total Standard Deviation in ln(k): 12.745777240055112
""",
)

entry(
    index = 89,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_N-3CH->C",
    kinetics = ArrheniusBM(A=(1.53963e+13,'m^3/(mol*s)'), n=-1.61469, w0=(525000,'J/mol'), E0=(170028,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.12572316523688595, var=42.35463494623351, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_N-3CH->C',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_N-3CH->C
    Total Standard Deviation in ln(k): 13.36279117083685"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_N-3CH->C
Total Standard Deviation in ln(k): 13.36279117083685""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_N-3CH->C
Total Standard Deviation in ln(k): 13.36279117083685
""",
)

entry(
    index = 90,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(521134,'m^3/(mol*s)'), n=0.387983, w0=(485000,'J/mol'), E0=(180404,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.17241509234118216, var=12.78679497461014, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C
    Total Standard Deviation in ln(k): 7.601861395628112"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C
Total Standard Deviation in ln(k): 7.601861395628112""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C
Total Standard Deviation in ln(k): 7.601861395628112
""",
)

entry(
    index = 91,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_N-1C-u0_Ext-1C-R_N-Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(1.28573e-06,'m^3/(mol*s)'), n=3.56699, w0=(485000,'J/mol'), E0=(48500,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_N-1C-u0_Ext-1C-R_N-Sp-4R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_N-1C-u0_Ext-1C-R_N-Sp-4R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_N-1C-u0_Ext-1C-R_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_N-1C-u0_Ext-1C-R_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 92,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_N-1CH->C_Ext-3CH-R_4R!H->O",
    kinetics = ArrheniusBM(A=(274.502,'m^3/(mol*s)'), n=1.01742, w0=(525000,'J/mol'), E0=(42270.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.7208456881690469e-15, var=2.0639189730426997e-28, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_N-1CH->C_Ext-3CH-R_4R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_N-1CH->C_Ext-3CH-R_4R!H->O
    Total Standard Deviation in ln(k): 3.312445063892648e-14"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_N-1CH->C_Ext-3CH-R_4R!H->O
Total Standard Deviation in ln(k): 3.312445063892648e-14""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_N-1CH->C_Ext-3CH-R_4R!H->O
Total Standard Deviation in ln(k): 3.312445063892648e-14
""",
)

entry(
    index = 93,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_N-1CH->C_Ext-3CH-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(2.47222,'m^3/(mol*s)'), n=1.52616, w0=(525000,'J/mol'), E0=(177287,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.01728024655805243, var=7.185118885179754, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_N-1CH->C_Ext-3CH-R_N-4R!H->O',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_N-1CH->C_Ext-3CH-R_N-4R!H->O
    Total Standard Deviation in ln(k): 5.417124527402398"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_N-1CH->C_Ext-3CH-R_N-4R!H->O
Total Standard Deviation in ln(k): 5.417124527402398""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_N-1CH->C_Ext-3CH-R_N-4R!H->O
Total Standard Deviation in ln(k): 5.417124527402398
""",
)

entry(
    index = 94,
    label = "Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(3.67795e-18,'m^3/(mol*s)'), n=7.1915, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.21267445005356395, var=0.06812177183619142, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 1.0575967341270556"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 1.0575967341270556""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 1.0575967341270556
""",
)

entry(
    index = 95,
    label = "Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0",
    kinetics = ArrheniusBM(A=(4.59897e-14,'m^3/(mol*s)'), n=6.05833, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.15313016968629564, var=1.4687863274669513, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0',), comment="""BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0
    Total Standard Deviation in ln(k): 2.8143576795194476"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0
Total Standard Deviation in ln(k): 2.8143576795194476""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0
Total Standard Deviation in ln(k): 2.8143576795194476
""",
)

entry(
    index = 96,
    label = "Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-1O-u0",
    kinetics = ArrheniusBM(A=(3.99453,'m^3/(mol*s)'), n=1.8271, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-1O-u0',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-1O-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-1O-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-1O-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 97,
    label = "Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Ext-1O-R",
    kinetics = ArrheniusBM(A=(0.000493877,'m^3/(mol*s)'), n=3.13091, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Ext-1O-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Ext-1O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 98,
    label = "Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(1.71908e-05,'m^3/(mol*s)'), n=3.59799, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 99,
    label = "Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R_Ext-3C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(3.37562e+10,'m^3/(mol*s)'), n=-0.767873, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.7086826882892017, var=1.6400841424518575, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R_Ext-3C-R_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R_Ext-3C-R_4R!H->C
    Total Standard Deviation in ln(k): 9.373114809379146"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 9.373114809379146""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 9.373114809379146
""",
)

entry(
    index = 100,
    label = "Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R_Ext-3C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(1.23555e-08,'m^3/(mol*s)'), n=4.72058, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R_Ext-3C-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R_Ext-3C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 101,
    label = "Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R_Sp-4R!H-3C_4R!H->C",
    kinetics = ArrheniusBM(A=(2.41917e-05,'m^3/(mol*s)'), n=3.5172, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R_Sp-4R!H-3C_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R_Sp-4R!H-3C_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R_Sp-4R!H-3C_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R_Sp-4R!H-3C_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 102,
    label = "Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(4.33685e-06,'m^3/(mol*s)'), n=3.64876, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 103,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-5R!H->O_Sp-5BrBrCCClClFFIINNPPSSSiSi=1C",
    kinetics = ArrheniusBM(A=(4.21084e-15,'m^3/(mol*s)'), n=6.77562, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.7740884642740191, var=0.00606822146475164, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-5R!H->O_Sp-5BrBrCCClClFFIINNPPSSSiSi=1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-5R!H->O_Sp-5BrBrCCClClFFIINNPPSSSiSi=1C
    Total Standard Deviation in ln(k): 4.613675140764854"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-5R!H->O_Sp-5BrBrCCClClFFIINNPPSSSiSi=1C
Total Standard Deviation in ln(k): 4.613675140764854""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-5R!H->O_Sp-5BrBrCCClClFFIINNPPSSSiSi=1C
Total Standard Deviation in ln(k): 4.613675140764854
""",
)

entry(
    index = 104,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-5R!H->O_N-Sp-5BrBrCCClClFFIINNPPSSSiSi=1C",
    kinetics = ArrheniusBM(A=(9.50536e-13,'m^3/(mol*s)'), n=6.01921, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1663458129650766, var=17.006586613290324, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-5R!H->O_N-Sp-5BrBrCCClClFFIINNPPSSSiSi=1C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-5R!H->O_N-Sp-5BrBrCCClClFFIINNPPSSSiSi=1C
    Total Standard Deviation in ln(k): 8.685289894823784"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-5R!H->O_N-Sp-5BrBrCCClClFFIINNPPSSSiSi=1C
Total Standard Deviation in ln(k): 8.685289894823784""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-5R!H->O_N-Sp-5BrBrCCClClFFIINNPPSSSiSi=1C
Total Standard Deviation in ln(k): 8.685289894823784
""",
)

entry(
    index = 105,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-4R!H->Cl_4CO->C_Ext-4C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(0.00185843,'m^3/(mol*s)'), n=3.22261, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-4R!H->Cl_4CO->C_Ext-4C-R_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-4R!H->Cl_4CO->C_Ext-4C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-4R!H->Cl_4CO->C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-4R!H->Cl_4CO->C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 106,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_1BrCClFHINPSSi->F_3CH->C_Ext-3C-R_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.65e+06,'m^3/(mol*s)'), n=0, w0=(320000,'J/mol'), E0=(32000,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_1BrCClFHINPSSi->F_3CH->C_Ext-3C-R_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_1BrCClFHINPSSi->F_3CH->C_Ext-3C-R_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_1BrCClFHINPSSi->F_3CH->C_Ext-3C-R_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_1BrCClFHINPSSi->F_3CH->C_Ext-3C-R_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 107,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(6.43855e-18,'m^3/(mol*s)'), n=7.14341, w0=(485000,'J/mol'), E0=(97786.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.18402182569569125, var=45.42554561848692, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R',), comment="""BM rule fitted to 20 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R
    Total Standard Deviation in ln(k): 13.97397528838754"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R
Total Standard Deviation in ln(k): 13.97397528838754""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R
Total Standard Deviation in ln(k): 13.97397528838754
""",
)

entry(
    index = 108,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_4R!H->F",
    kinetics = ArrheniusBM(A=(0.0964,'m^3/(mol*s)'), n=2.41, w0=(485000,'J/mol'), E0=(68083,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_4R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_4R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_4R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_4R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 109,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F",
    kinetics = ArrheniusBM(A=(1.18407e-06,'m^3/(mol*s)'), n=3.92451, w0=(485000,'J/mol'), E0=(170274,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.013333982321667718, var=2.341218942635411, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F
    Total Standard Deviation in ln(k): 3.1009560822152067"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F
Total Standard Deviation in ln(k): 3.1009560822152067""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F
Total Standard Deviation in ln(k): 3.1009560822152067
""",
)

entry(
    index = 110,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_N-3CH->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.37379e+17,'m^3/(mol*s)'), n=-2.8111, w0=(525000,'J/mol'), E0=(173393,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1929525742478792, var=52.55608857552154, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_N-3CH->C_Ext-1C-R',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_N-3CH->C_Ext-1C-R
    Total Standard Deviation in ln(k): 15.018248318902437"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_N-3CH->C_Ext-1C-R
Total Standard Deviation in ln(k): 15.018248318902437""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_N-3CH->C_Ext-1C-R
Total Standard Deviation in ln(k): 15.018248318902437
""",
)

entry(
    index = 111,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C",
    kinetics = ArrheniusBM(A=(5.75131e+07,'m^3/(mol*s)'), n=-0.317486, w0=(485000,'J/mol'), E0=(180460,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.17592987804682242, var=33.89054175610318, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C
    Total Standard Deviation in ln(k): 12.112717121817955"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C
Total Standard Deviation in ln(k): 12.112717121817955""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C
Total Standard Deviation in ln(k): 12.112717121817955
""",
)

entry(
    index = 112,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(156.901,'m^3/(mol*s)'), n=1.58124, w0=(485000,'J/mol'), E0=(179363,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06875736121202176, var=10.147090870361966, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C
    Total Standard Deviation in ln(k): 6.5587402794106735"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C
Total Standard Deviation in ln(k): 6.5587402794106735""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C
Total Standard Deviation in ln(k): 6.5587402794106735
""",
)

entry(
    index = 113,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_N-1CH->C_Ext-3CH-R_N-4R!H->O_4BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(38.9593,'m^3/(mol*s)'), n=1.15314, w0=(525000,'J/mol'), E0=(149167,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=7.105427357600158e-15, var=3.266278578067554e-27, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_N-1CH->C_Ext-3CH-R_N-4R!H->O_4BrCClFINPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_N-1CH->C_Ext-3CH-R_N-4R!H->O_4BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 1.3242617968776676e-13"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_N-1CH->C_Ext-3CH-R_N-4R!H->O_4BrCClFINPSSi->C
Total Standard Deviation in ln(k): 1.3242617968776676e-13""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_N-1CH->C_Ext-3CH-R_N-4R!H->O_4BrCClFINPSSi->C
Total Standard Deviation in ln(k): 1.3242617968776676e-13
""",
)

entry(
    index = 114,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_N-1CH->C_Ext-3CH-R_N-4R!H->O_N-4BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(0.203357,'m^3/(mol*s)'), n=1.85344, w0=(525000,'J/mol'), E0=(185246,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.014134804715025585, var=1.3806567324099637, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_N-1CH->C_Ext-3CH-R_N-4R!H->O_N-4BrCClFINPSSi->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_N-1CH->C_Ext-3CH-R_N-4R!H->O_N-4BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 2.39110537073851"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_N-1CH->C_Ext-3CH-R_N-4R!H->O_N-4BrCClFINPSSi->C
Total Standard Deviation in ln(k): 2.39110537073851""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_N-1CH->C_Ext-3CH-R_N-4R!H->O_N-4BrCClFINPSSi->C
Total Standard Deviation in ln(k): 2.39110537073851
""",
)

entry(
    index = 115,
    label = "Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Ext-1O-R",
    kinetics = ArrheniusBM(A=(8.66494e-05,'m^3/(mol*s)'), n=3.25251, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Ext-1O-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Ext-1O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 116,
    label = "Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(7.78646e-05,'m^3/(mol*s)'), n=3.27081, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 117,
    label = "Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-1O-R",
    kinetics = ArrheniusBM(A=(5.93338e-15,'m^3/(mol*s)'), n=6.24187, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.6767481435309115, var=0.003599597201544746, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-1O-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-1O-R
    Total Standard Deviation in ln(k): 6.8457752233214215"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-1O-R
Total Standard Deviation in ln(k): 6.8457752233214215""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-1O-R
Total Standard Deviation in ln(k): 6.8457752233214215
""",
)

entry(
    index = 118,
    label = "Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-3C-R",
    kinetics = ArrheniusBM(A=(7.21673e-14,'m^3/(mol*s)'), n=6.05636, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.129617103770459, var=4.312988567682566, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-3C-R
    Total Standard Deviation in ln(k): 9.514177618192498"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-3C-R
Total Standard Deviation in ln(k): 9.514177618192498""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-3C-R
Total Standard Deviation in ln(k): 9.514177618192498
""",
)

entry(
    index = 119,
    label = "Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R_Ext-3C-R_4R!H->C_Ext-1O-R",
    kinetics = ArrheniusBM(A=(0.53284,'m^3/(mol*s)'), n=2.34576, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R_Ext-3C-R_4R!H->C_Ext-1O-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R_Ext-3C-R_4R!H->C_Ext-1O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R_Ext-3C-R_4R!H->C_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_N-3C-u1_1O-u0_Ext-3C-R_Ext-3C-R_4R!H->C_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 120,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-5R!H->O_Sp-5BrBrCCClClFFIINNPPSSSiSi=1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(8.38302e-05,'m^3/(mol*s)'), n=3.60203, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-5R!H->O_Sp-5BrBrCCClClFFIINNPPSSSiSi=1C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-5R!H->O_Sp-5BrBrCCClClFFIINNPPSSSiSi=1C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-5R!H->O_Sp-5BrBrCCClClFFIINNPPSSSiSi=1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-5R!H->O_Sp-5BrBrCCClClFFIINNPPSSSiSi=1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 121,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-5R!H->O_N-Sp-5BrBrCCClClFFIINNPPSSSiSi=1C_1C-u0",
    kinetics = ArrheniusBM(A=(1.86752e-19,'m^3/(mol*s)'), n=8.02172, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.267331334783395, var=0.5211829382440627, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-5R!H->O_N-Sp-5BrBrCCClClFFIINNPPSSSiSi=1C_1C-u0',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-5R!H->O_N-Sp-5BrBrCCClClFFIINNPPSSSiSi=1C_1C-u0
    Total Standard Deviation in ln(k): 2.118965183763332"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-5R!H->O_N-Sp-5BrBrCCClClFFIINNPPSSSiSi=1C_1C-u0
Total Standard Deviation in ln(k): 2.118965183763332""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-5R!H->O_N-Sp-5BrBrCCClClFFIINNPPSSSiSi=1C_1C-u0
Total Standard Deviation in ln(k): 2.118965183763332
""",
)

entry(
    index = 122,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-5R!H->O_N-Sp-5BrBrCCClClFFIINNPPSSSiSi=1C_N-1C-u0",
    kinetics = ArrheniusBM(A=(0.000115787,'m^3/(mol*s)'), n=3.43806, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-5R!H->O_N-Sp-5BrBrCCClClFFIINNPPSSSiSi=1C_N-1C-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-5R!H->O_N-Sp-5BrBrCCClClFFIINNPPSSSiSi=1C_N-1C-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-5R!H->O_N-Sp-5BrBrCCClClFFIINNPPSSSiSi=1C_N-1C-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-5R!H->O_N-Sp-5BrBrCCClClFFIINNPPSSSiSi=1C_N-1C-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 123,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.74497e+11,'m^3/(mol*s)'), n=-1.50288, w0=(485000,'J/mol'), E0=(74096.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07685340693933024, var=4.9255733332096066, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 4.642334413317349"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R
Total Standard Deviation in ln(k): 4.642334413317349""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R
Total Standard Deviation in ln(k): 4.642334413317349
""",
)

entry(
    index = 124,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_4R!H->F",
    kinetics = ArrheniusBM(A=(3.84009e-06,'m^3/(mol*s)'), n=3.394, w0=(485000,'J/mol'), E0=(58912.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_4R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_4R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_4R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_4R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 125,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F",
    kinetics = ArrheniusBM(A=(101015,'m^3/(mol*s)'), n=0.719189, w0=(485000,'J/mol'), E0=(188127,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.18703354518789098, var=7.562110945463186, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F
    Total Standard Deviation in ln(k): 5.982813182309724"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F
Total Standard Deviation in ln(k): 5.982813182309724""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F
Total Standard Deviation in ln(k): 5.982813182309724
""",
)

entry(
    index = 126,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C",
    kinetics = ArrheniusBM(A=(1.98065e-07,'m^3/(mol*s)'), n=4.18767, w0=(485000,'J/mol'), E0=(176965,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=5.5894666507659404e-05, var=0.9693719512841332, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C
    Total Standard Deviation in ln(k): 1.9739362095107178"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C
Total Standard Deviation in ln(k): 1.9739362095107178""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C
Total Standard Deviation in ln(k): 1.9739362095107178
""",
)

entry(
    index = 127,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C",
    kinetics = ArrheniusBM(A=(1.39778e-05,'m^3/(mol*s)'), n=3.5943, w0=(485000,'J/mol'), E0=(169170,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.029564212116525136, var=3.3298013412750778, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C
    Total Standard Deviation in ln(k): 3.732471039896878"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C
Total Standard Deviation in ln(k): 3.732471039896878""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C
Total Standard Deviation in ln(k): 3.732471039896878
""",
)

entry(
    index = 128,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_N-3CH->C_Ext-1C-R_4R!H->O",
    kinetics = ArrheniusBM(A=(2.97193e+07,'m^3/(mol*s)'), n=-0.0923208, w0=(525000,'J/mol'), E0=(42282.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.7755575615628514e-16, var=1.6029900113123836e-29, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_N-3CH->C_Ext-1C-R_4R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_N-3CH->C_Ext-1C-R_4R!H->O
    Total Standard Deviation in ln(k): 8.723805809771637e-15"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_N-3CH->C_Ext-1C-R_4R!H->O
Total Standard Deviation in ln(k): 8.723805809771637e-15""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_N-3CH->C_Ext-1C-R_4R!H->O
Total Standard Deviation in ln(k): 8.723805809771637e-15
""",
)

entry(
    index = 129,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_N-3CH->C_Ext-1C-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(4.41365e+06,'m^3/(mol*s)'), n=0.331565, w0=(525000,'J/mol'), E0=(178183,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.030153810444676105, var=9.792245825238517, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_N-3CH->C_Ext-1C-R_N-4R!H->O',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_N-3CH->C_Ext-1C-R_N-4R!H->O
    Total Standard Deviation in ln(k): 6.349093480788056"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_N-3CH->C_Ext-1C-R_N-4R!H->O
Total Standard Deviation in ln(k): 6.349093480788056""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_N-3CH->C_Ext-1C-R_N-4R!H->O
Total Standard Deviation in ln(k): 6.349093480788056
""",
)

entry(
    index = 130,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.00145226,'m^3/(mol*s)'), n=2.99928, w0=(485000,'J/mol'), E0=(150111,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.01523902092730193, var=3.2682109819200096, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 3.662487961470511"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.662487961470511""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.662487961470511
""",
)

entry(
    index = 131,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.71639e-05,'m^3/(mol*s)'), n=3.56319, w0=(485000,'J/mol'), E0=(150385,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 132,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_N-1CH->C_Ext-3CH-R_N-4R!H->O_N-4BrCClFINPSSi->C_Ext-3CH-R",
    kinetics = ArrheniusBM(A=(0.000648872,'m^3/(mol*s)'), n=2.5954, w0=(525000,'J/mol'), E0=(185402,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.008011585092201273, var=0.07418139365724122, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_N-1CH->C_Ext-3CH-R_N-4R!H->O_N-4BrCClFINPSSi->C_Ext-3CH-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_N-1CH->C_Ext-3CH-R_N-4R!H->O_N-4BrCClFINPSSi->C_Ext-3CH-R
    Total Standard Deviation in ln(k): 0.5661444974015927"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_N-1CH->C_Ext-3CH-R_N-4R!H->O_N-4BrCClFINPSSi->C_Ext-3CH-R
Total Standard Deviation in ln(k): 0.5661444974015927""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_N-1CH->C_Ext-3CH-R_N-4R!H->O_N-4BrCClFINPSSi->C_Ext-3CH-R
Total Standard Deviation in ln(k): 0.5661444974015927
""",
)

entry(
    index = 133,
    label = "Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-1O-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.00346669,'m^3/(mol*s)'), n=2.70977, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-1O-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-1O-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-1O-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-1O-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 134,
    label = "Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-3C-R_Sp-5R!H-3C",
    kinetics = ArrheniusBM(A=(1.83515e-06,'m^3/(mol*s)'), n=3.99398, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-3C-R_Sp-5R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-3C-R_Sp-5R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-3C-R_Sp-5R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-3C-R_Sp-5R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 135,
    label = "Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-3C-R_N-Sp-5R!H-3C",
    kinetics = ArrheniusBM(A=(0.000643764,'m^3/(mol*s)'), n=2.99108, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-3C-R_N-Sp-5R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-3C-R_N-Sp-5R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-3C-R_N-Sp-5R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-3C-R_N-Sp-5R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 136,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-5R!H->O_N-Sp-5BrBrCCClClFFIINNPPSSSiSi=1C_1C-u0_Ext-5BrCClFINPSSi-R",
    kinetics = ArrheniusBM(A=(5.69582e-06,'m^3/(mol*s)'), n=3.94767, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-5R!H->O_N-Sp-5BrBrCCClClFFIINNPPSSSiSi=1C_1C-u0_Ext-5BrCClFINPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-5R!H->O_N-Sp-5BrBrCCClClFFIINNPPSSSiSi=1C_1C-u0_Ext-5BrCClFINPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-5R!H->O_N-Sp-5BrBrCCClClFFIINNPPSSSiSi=1C_1C-u0_Ext-5BrCClFINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-5R!H->O_N-Sp-5BrBrCCClClFFIINNPPSSSiSi=1C_1C-u0_Ext-5BrCClFINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 137,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-5R!H->O_N-Sp-5BrBrCCClClFFIINNPPSSSiSi=1C_1C-u0_5BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(5.27349e-06,'m^3/(mol*s)'), n=3.9638, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-5R!H->O_N-Sp-5BrBrCCClClFFIINNPPSSSiSi=1C_1C-u0_5BrCClFINPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-5R!H->O_N-Sp-5BrBrCCClClFFIINNPPSSSiSi=1C_1C-u0_5BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-5R!H->O_N-Sp-5BrBrCCClClFFIINNPPSSSiSi=1C_1C-u0_5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-5R!H->O_N-Sp-5BrBrCCClClFFIINNPPSSSiSi=1C_1C-u0_5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 138,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-5R!H->O_N-Sp-5BrBrCCClClFFIINNPPSSSiSi=1C_1C-u0_N-5BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(6.65995e-06,'m^3/(mol*s)'), n=3.94804, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-5R!H->O_N-Sp-5BrBrCCClClFFIINNPPSSSiSi=1C_1C-u0_N-5BrCClFINPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-5R!H->O_N-Sp-5BrBrCCClClFFIINNPPSSSiSi=1C_1C-u0_N-5BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-5R!H->O_N-Sp-5BrBrCCClClFFIINNPPSSSiSi=1C_1C-u0_N-5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-5R!H->O_N-Sp-5BrBrCCClClFFIINNPPSSSiSi=1C_1C-u0_N-5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 139,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(1.18087e+12,'m^3/(mol*s)'), n=-1.72333, w0=(485000,'J/mol'), E0=(77787.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07248463590892681, var=9.888819399217423, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R_4R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R_4R!H->C
    Total Standard Deviation in ln(k): 6.486311015718294"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R_4R!H->C
Total Standard Deviation in ln(k): 6.486311015718294""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R_4R!H->C
Total Standard Deviation in ln(k): 6.486311015718294
""",
)

entry(
    index = 140,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(6.99631e+08,'m^3/(mol*s)'), n=-0.844408, w0=(485000,'J/mol'), E0=(65124.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.003991012989907948, var=2.765856103509407, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R_N-4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 3.3440751506986266"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R_N-4R!H->C
Total Standard Deviation in ln(k): 3.3440751506986266""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R_N-4R!H->C
Total Standard Deviation in ln(k): 3.3440751506986266
""",
)

entry(
    index = 141,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_3C-u1",
    kinetics = ArrheniusBM(A=(4.57438e-06,'m^3/(mol*s)'), n=3.74673, w0=(485000,'J/mol'), E0=(175267,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0169091122407432, var=3.1489191766923104, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_3C-u1',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_3C-u1
    Total Standard Deviation in ln(k): 3.5999265361008708"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_3C-u1
Total Standard Deviation in ln(k): 3.5999265361008708""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_3C-u1
Total Standard Deviation in ln(k): 3.5999265361008708
""",
)

entry(
    index = 142,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1",
    kinetics = ArrheniusBM(A=(5.87084,'m^3/(mol*s)'), n=2.00334, w0=(485000,'J/mol'), E0=(169005,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.18676736288242687, var=12.231274908733644, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1
    Total Standard Deviation in ln(k): 7.4804727583775845"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1
Total Standard Deviation in ln(k): 7.4804727583775845""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1
Total Standard Deviation in ln(k): 7.4804727583775845
""",
)

entry(
    index = 143,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.5027e-05,'m^3/(mol*s)'), n=3.59925, w0=(485000,'J/mol'), E0=(180542,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 144,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(2.64593e-05,'m^3/(mol*s)'), n=3.51437, w0=(485000,'J/mol'), E0=(168388,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03353608159788866, var=4.7021217407257225, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 4.431404484864095"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 4.431404484864095""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 4.431404484864095
""",
)

entry(
    index = 145,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(5.29538e-06,'m^3/(mol*s)'), n=3.74, w0=(485000,'J/mol'), E0=(175524,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 146,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_N-3CH->C_Ext-1C-R_N-4R!H->O_4BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(3.49783e+08,'m^3/(mol*s)'), n=-0.190181, w0=(525000,'J/mol'), E0=(148797,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-7.216449660063544e-15, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_N-3CH->C_Ext-1C-R_N-4R!H->O_4BrCClFINPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_N-3CH->C_Ext-1C-R_N-4R!H->O_4BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 1.8131783065486293e-14"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_N-3CH->C_Ext-1C-R_N-4R!H->O_4BrCClFINPSSi->C
Total Standard Deviation in ln(k): 1.8131783065486293e-14""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_N-3CH->C_Ext-1C-R_N-4R!H->O_4BrCClFINPSSi->C
Total Standard Deviation in ln(k): 1.8131783065486293e-14
""",
)

entry(
    index = 147,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_N-3CH->C_Ext-1C-R_N-4R!H->O_N-4BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(172909,'m^3/(mol*s)'), n=0.734537, w0=(525000,'J/mol'), E0=(186381,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.02355627985006888, var=0.9829368301626673, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_N-3CH->C_Ext-1C-R_N-4R!H->O_N-4BrCClFINPSSi->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_N-3CH->C_Ext-1C-R_N-4R!H->O_N-4BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 2.0467445531762056"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_N-3CH->C_Ext-1C-R_N-4R!H->O_N-4BrCClFINPSSi->C
Total Standard Deviation in ln(k): 2.0467445531762056""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_N-3CH->C_Ext-1C-R_N-4R!H->O_N-4BrCClFINPSSi->C
Total Standard Deviation in ln(k): 2.0467445531762056
""",
)

entry(
    index = 148,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(4.47723e-05,'m^3/(mol*s)'), n=3.46134, w0=(485000,'J/mol'), E0=(153463,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 149,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(3.5032e-05,'m^3/(mol*s)'), n=3.5135, w0=(485000,'J/mol'), E0=(143442,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 150,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_N-1CH->C_Ext-3CH-R_N-4R!H->O_N-4BrCClFINPSSi->C_Ext-3CH-R_Ext-3CH-R",
    kinetics = ArrheniusBM(A=(0.0010964,'m^3/(mol*s)'), n=2.5574, w0=(525000,'J/mol'), E0=(186114,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.9428902930941035e-14, var=2.4460851037674356e-27, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_N-1CH->C_Ext-3CH-R_N-4R!H->O_N-4BrCClFINPSSi->C_Ext-3CH-R_Ext-3CH-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_N-1CH->C_Ext-3CH-R_N-4R!H->O_N-4BrCClFINPSSi->C_Ext-3CH-R_Ext-3CH-R
    Total Standard Deviation in ln(k): 1.479663509627408e-13"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_N-1CH->C_Ext-3CH-R_N-4R!H->O_N-4BrCClFINPSSi->C_Ext-3CH-R_Ext-3CH-R
Total Standard Deviation in ln(k): 1.479663509627408e-13""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_N-1CH->C_Ext-3CH-R_N-4R!H->O_N-4BrCClFINPSSi->C_Ext-3CH-R_Ext-3CH-R
Total Standard Deviation in ln(k): 1.479663509627408e-13
""",
)

entry(
    index = 151,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R_4R!H->C_5R!H->O",
    kinetics = ArrheniusBM(A=(300000,'m^3/(mol*s)'), n=0, w0=(485000,'J/mol'), E0=(71601.2,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R_4R!H->C_5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R_4R!H->C_5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R_4R!H->C_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R_4R!H->C_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 152,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R_4R!H->C_N-5R!H->O",
    kinetics = ArrheniusBM(A=(4.65238e+12,'m^3/(mol*s)'), n=-1.82985, w0=(485000,'J/mol'), E0=(76201.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06446505530931997, var=9.531089354840619, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R_4R!H->C_N-5R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R_4R!H->C_N-5R!H->O
    Total Standard Deviation in ln(k): 6.35108333340074"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R_4R!H->C_N-5R!H->O
Total Standard Deviation in ln(k): 6.35108333340074""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R_4R!H->C_N-5R!H->O
Total Standard Deviation in ln(k): 6.35108333340074
""",
)

entry(
    index = 153,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R_N-4R!H->C_5R!H->O",
    kinetics = ArrheniusBM(A=(2e+06,'m^3/(mol*s)'), n=0, w0=(485000,'J/mol'), E0=(60327.1,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R_N-4R!H->C_5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R_N-4R!H->C_5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R_N-4R!H->C_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R_N-4R!H->C_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 154,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R_N-4R!H->C_N-5R!H->O",
    kinetics = ArrheniusBM(A=(500000,'m^3/(mol*s)'), n=0, w0=(485000,'J/mol'), E0=(58526.8,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R_N-4R!H->C_N-5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R_N-4R!H->C_N-5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R_N-4R!H->C_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R_N-4R!H->C_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 155,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_3C-u1_4CO->O",
    kinetics = ArrheniusBM(A=(0.000336201,'m^3/(mol*s)'), n=3.25307, w0=(485000,'J/mol'), E0=(169444,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.01478493898391874, var=24.848703892903735, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_3C-u1_4CO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_3C-u1_4CO->O
    Total Standard Deviation in ln(k): 10.030446584775426"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_3C-u1_4CO->O
Total Standard Deviation in ln(k): 10.030446584775426""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_3C-u1_4CO->O
Total Standard Deviation in ln(k): 10.030446584775426
""",
)

entry(
    index = 156,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_3C-u1_N-4CO->O",
    kinetics = ArrheniusBM(A=(2.52196e-07,'m^3/(mol*s)'), n=4.09544, w0=(485000,'J/mol'), E0=(176540,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0043179176979719425, var=0.3364138793521485, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_3C-u1_N-4CO->O',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_3C-u1_N-4CO->O
    Total Standard Deviation in ln(k): 1.1736193706558342"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_3C-u1_N-4CO->O
Total Standard Deviation in ln(k): 1.1736193706558342""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_3C-u1_N-4CO->O
Total Standard Deviation in ln(k): 1.1736193706558342
""",
)

entry(
    index = 157,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.02801e-06,'m^3/(mol*s)'), n=4.1278, w0=(485000,'J/mol'), E0=(147613,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03722150037496022, var=0.14117931941902592, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1_Ext-3C-R
    Total Standard Deviation in ln(k): 0.8467772392611741"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1_Ext-3C-R
Total Standard Deviation in ln(k): 0.8467772392611741""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1_Ext-3C-R
Total Standard Deviation in ln(k): 0.8467772392611741
""",
)

entry(
    index = 158,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1_Sp-4CO-3C",
    kinetics = ArrheniusBM(A=(0.000235004,'m^3/(mol*s)'), n=3.19486, w0=(485000,'J/mol'), E0=(179003,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0005189499870718598, var=24.018014794453205, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1_Sp-4CO-3C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1_Sp-4CO-3C
    Total Standard Deviation in ln(k): 9.826145181724515"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1_Sp-4CO-3C
Total Standard Deviation in ln(k): 9.826145181724515""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1_Sp-4CO-3C
Total Standard Deviation in ln(k): 9.826145181724515
""",
)

entry(
    index = 159,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1_N-Sp-4CO-3C",
    kinetics = ArrheniusBM(A=(1.97404e-09,'m^3/(mol*s)'), n=4.3496, w0=(485000,'J/mol'), E0=(48500,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1_N-Sp-4CO-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1_N-Sp-4CO-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1_N-Sp-4CO-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1_N-Sp-4CO-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 160,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.11671e-05,'m^3/(mol*s)'), n=3.49958, w0=(485000,'J/mol'), E0=(159893,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.010610137368484684, var=12.617966593133893, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C_Ext-1C-R
    Total Standard Deviation in ln(k): 7.147833923938062"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 7.147833923938062""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 7.147833923938062
""",
)

entry(
    index = 161,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(4.51365e-06,'m^3/(mol*s)'), n=3.78897, w0=(485000,'J/mol'), E0=(177779,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 162,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_N-3CH->C_Ext-1C-R_N-4R!H->O_N-4BrCClFINPSSi->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(985.256,'m^3/(mol*s)'), n=1.40729, w0=(525000,'J/mol'), E0=(186064,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.007294082459230069, var=0.4417967943835712, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_N-3CH->C_Ext-1C-R_N-4R!H->O_N-4BrCClFINPSSi->C_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_N-3CH->C_Ext-1C-R_N-4R!H->O_N-4BrCClFINPSSi->C_Ext-1C-R
    Total Standard Deviation in ln(k): 1.3508300677744975"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_N-3CH->C_Ext-1C-R_N-4R!H->O_N-4BrCClFINPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 1.3508300677744975""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_N-3CH->C_Ext-1C-R_N-4R!H->O_N-4BrCClFINPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 1.3508300677744975
""",
)

entry(
    index = 163,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R_4R!H->C_N-5R!H->O_Ext-4C-R_Ext-4C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(44713.3,'m^3/(mol*s)'), n=0.232655, w0=(485000,'J/mol'), E0=(56538.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R_4R!H->C_N-5R!H->O_Ext-4C-R_Ext-4C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R_4R!H->C_N-5R!H->O_Ext-4C-R_Ext-4C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R_4R!H->C_N-5R!H->O_Ext-4C-R_Ext-4C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R_4R!H->C_N-5R!H->O_Ext-4C-R_Ext-4C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 164,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R_4R!H->C_N-5R!H->O_5CF->C",
    kinetics = ArrheniusBM(A=(5.37784e+07,'m^3/(mol*s)'), n=-0.294997, w0=(485000,'J/mol'), E0=(74183.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R_4R!H->C_N-5R!H->O_5CF->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R_4R!H->C_N-5R!H->O_5CF->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R_4R!H->C_N-5R!H->O_5CF->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R_4R!H->C_N-5R!H->O_5CF->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 165,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R_4R!H->C_N-5R!H->O_N-5CF->C",
    kinetics = ArrheniusBM(A=(3.20615e+07,'m^3/(mol*s)'), n=-0.0623422, w0=(485000,'J/mol'), E0=(60947.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R_4R!H->C_N-5R!H->O_N-5CF->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R_4R!H->C_N-5R!H->O_N-5CF->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R_4R!H->C_N-5R!H->O_N-5CF->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_Ext-1C-R_4R!H->C_N-5R!H->O_N-5CF->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 166,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_3C-u1_4CO->O_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.70352e-09,'m^3/(mol*s)'), n=4.77004, w0=(485000,'J/mol'), E0=(144580,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_3C-u1_4CO->O_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_3C-u1_4CO->O_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_3C-u1_4CO->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_3C-u1_4CO->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 167,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_3C-u1_N-4CO->O_Sp-4C=3C",
    kinetics = ArrheniusBM(A=(4.7621e-06,'m^3/(mol*s)'), n=3.70949, w0=(485000,'J/mol'), E0=(182151,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.4311660551369507e-05, var=0.026872770462439747, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_3C-u1_N-4CO->O_Sp-4C=3C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_3C-u1_N-4CO->O_Sp-4C=3C
    Total Standard Deviation in ln(k): 0.3286956277293367"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_3C-u1_N-4CO->O_Sp-4C=3C
Total Standard Deviation in ln(k): 0.3286956277293367""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_3C-u1_N-4CO->O_Sp-4C=3C
Total Standard Deviation in ln(k): 0.3286956277293367
""",
)

entry(
    index = 168,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_3C-u1_N-4CO->O_N-Sp-4C=3C",
    kinetics = ArrheniusBM(A=(2.5414e-07,'m^3/(mol*s)'), n=4.10045, w0=(485000,'J/mol'), E0=(174571,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.005312506283599704, var=0.34888895989869806, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_3C-u1_N-4CO->O_N-Sp-4C=3C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_3C-u1_N-4CO->O_N-Sp-4C=3C
    Total Standard Deviation in ln(k): 1.1974813288596242"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_3C-u1_N-4CO->O_N-Sp-4C=3C
Total Standard Deviation in ln(k): 1.1974813288596242""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_3C-u1_N-4CO->O_N-Sp-4C=3C
Total Standard Deviation in ln(k): 1.1974813288596242
""",
)

entry(
    index = 169,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1_Ext-3C-R_4CO->O",
    kinetics = ArrheniusBM(A=(1.15755e-09,'m^3/(mol*s)'), n=5.09587, w0=(485000,'J/mol'), E0=(139936,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0045355772669015875, var=0.1695294605612366, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1_Ext-3C-R_4CO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1_Ext-3C-R_4CO->O
    Total Standard Deviation in ln(k): 0.8368246500030938"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1_Ext-3C-R_4CO->O
Total Standard Deviation in ln(k): 0.8368246500030938""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1_Ext-3C-R_4CO->O
Total Standard Deviation in ln(k): 0.8368246500030938
""",
)

entry(
    index = 170,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1_Ext-3C-R_N-4CO->O",
    kinetics = ArrheniusBM(A=(9.47301e-05,'m^3/(mol*s)'), n=3.61437, w0=(485000,'J/mol'), E0=(152301,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1_Ext-3C-R_N-4CO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1_Ext-3C-R_N-4CO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1_Ext-3C-R_N-4CO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1_Ext-3C-R_N-4CO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 171,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1_Sp-4CO-3C_4CO->C",
    kinetics = ArrheniusBM(A=(2.34026e-06,'m^3/(mol*s)'), n=3.43997, w0=(485000,'J/mol'), E0=(169290,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1_Sp-4CO-3C_4CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1_Sp-4CO-3C_4CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1_Sp-4CO-3C_4CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1_Sp-4CO-3C_4CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 172,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1_Sp-4CO-3C_N-4CO->C",
    kinetics = ArrheniusBM(A=(2.30271e-08,'m^3/(mol*s)'), n=4.64603, w0=(485000,'J/mol'), E0=(171336,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1_Sp-4CO-3C_N-4CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1_Sp-4CO-3C_N-4CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1_Sp-4CO-3C_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1_Sp-4CO-3C_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 173,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C_Ext-1C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.21333e-05,'m^3/(mol*s)'), n=3.66599, w0=(485000,'J/mol'), E0=(172409,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C_Ext-1C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C_Ext-1C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 174,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C_Ext-1C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(3.38922e-05,'m^3/(mol*s)'), n=3.5758, w0=(485000,'J/mol'), E0=(154793,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C_Ext-1C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C_Ext-1C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 175,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_N-3CH->C_Ext-1C-R_N-4R!H->O_N-4BrCClFINPSSi->C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3407.11,'m^3/(mol*s)'), n=1.29978, w0=(525000,'J/mol'), E0=(186590,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.426636586643339e-14, var=9.940263703367236e-29, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_N-3CH->C_Ext-1C-R_N-4R!H->O_N-4BrCClFINPSSi->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_N-3CH->C_Ext-1C-R_N-4R!H->O_N-4BrCClFINPSSi->C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 5.5832523727311933e-14"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_N-3CH->C_Ext-1C-R_N-4R!H->O_N-4BrCClFINPSSi->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 5.5832523727311933e-14""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_N-3CH->C_Ext-1C-R_N-4R!H->O_N-4BrCClFINPSSi->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 5.5832523727311933e-14
""",
)

entry(
    index = 176,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_3C-u1_N-4CO->O_Sp-4C=3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(4.75844e-07,'m^3/(mol*s)'), n=3.95233, w0=(485000,'J/mol'), E0=(177409,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_3C-u1_N-4CO->O_Sp-4C=3C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_3C-u1_N-4CO->O_Sp-4C=3C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_3C-u1_N-4CO->O_Sp-4C=3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_3C-u1_N-4CO->O_Sp-4C=3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 177,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_3C-u1_N-4CO->O_N-Sp-4C=3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.95993e-10,'m^3/(mol*s)'), n=4.92183, w0=(485000,'J/mol'), E0=(161867,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_3C-u1_N-4CO->O_N-Sp-4C=3C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_3C-u1_N-4CO->O_N-Sp-4C=3C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_3C-u1_N-4CO->O_N-Sp-4C=3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_3C-u1_N-4CO->O_N-Sp-4C=3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 178,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_3C-u1_N-4CO->O_N-Sp-4C=3C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(3.15703e-08,'m^3/(mol*s)'), n=4.33914, w0=(485000,'J/mol'), E0=(173191,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_3C-u1_N-4CO->O_N-Sp-4C=3C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_3C-u1_N-4CO->O_N-Sp-4C=3C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_3C-u1_N-4CO->O_N-Sp-4C=3C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_3C-u1_N-4CO->O_N-Sp-4C=3C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 179,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1_Ext-3C-R_4CO->O_5R!H->C",
    kinetics = ArrheniusBM(A=(1.2036e-07,'m^3/(mol*s)'), n=4.37786, w0=(485000,'J/mol'), E0=(135943,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1_Ext-3C-R_4CO->O_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1_Ext-3C-R_4CO->O_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1_Ext-3C-R_4CO->O_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1_Ext-3C-R_4CO->O_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 180,
    label = "Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1_Ext-3C-R_4CO->O_N-5R!H->C",
    kinetics = ArrheniusBM(A=(5.32399e-12,'m^3/(mol*s)'), n=5.89926, w0=(485000,'J/mol'), E0=(142781,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1_Ext-3C-R_4CO->O_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1_Ext-3C-R_4CO->O_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1_Ext-3C-R_4CO->O_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-3CFH->F_N-1BrCClFHINPSSi->F_1CH->C_1C-u0_3CH->C_Ext-3C-R_N-4R!H->F_N-3C-u1_Ext-3C-R_4CO->O_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

