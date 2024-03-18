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
    kinetics = ArrheniusBM(A=(1.1975e+32,'m^3/(mol*s)'), n=-7.07496, w0=(409.075,'kJ/mol'), E0=(250.271,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.0322469017760625, var=14.87532888732254, Tref=1000.0, N=234, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 234 training reactions at node Root
    Total Standard Deviation in ln(k): 10.325557270474627"""),
    rank = 11,
    shortDesc = """BM rule fitted to 234 training reactions at node Root
Total Standard Deviation in ln(k): 10.325557270474627""",
    longDesc = 
"""
BM rule fitted to 234 training reactions at node Root
Total Standard Deviation in ln(k): 10.325557270474627
""",
)

entry(
    index = 2,
    label = "Root_1R->O",
    kinetics = ArrheniusBM(A=(1.91927e-08,'m^3/(mol*s)'), n=4.30256, w0=(337.688,'kJ/mol'), E0=(90.7442,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.23149780005575135, var=5.678387695980674, Tref=1000.0, N=64, data_mean=0.0, correlation='Root_1R->O',), comment="""BM rule fitted to 64 training reactions at node Root_1R->O
    Total Standard Deviation in ln(k): 5.35880971340848"""),
    rank = 11,
    shortDesc = """BM rule fitted to 64 training reactions at node Root_1R->O
Total Standard Deviation in ln(k): 5.35880971340848""",
    longDesc = 
"""
BM rule fitted to 64 training reactions at node Root_1R->O
Total Standard Deviation in ln(k): 5.35880971340848
""",
)

entry(
    index = 3,
    label = "Root_N-1R->O",
    kinetics = ArrheniusBM(A=(1.27165e+33,'m^3/(mol*s)'), n=-7.36304, w0=(435.95,'kJ/mol'), E0=(257.483,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.0645789966290355, var=14.546346062150658, Tref=1000.0, N=170, data_mean=0.0, correlation='Root_N-1R->O',), comment="""BM rule fitted to 170 training reactions at node Root_N-1R->O
    Total Standard Deviation in ln(k): 10.320815497634985"""),
    rank = 11,
    shortDesc = """BM rule fitted to 170 training reactions at node Root_N-1R->O
Total Standard Deviation in ln(k): 10.320815497634985""",
    longDesc = 
"""
BM rule fitted to 170 training reactions at node Root_N-1R->O
Total Standard Deviation in ln(k): 10.320815497634985
""",
)

entry(
    index = 4,
    label = "Root_1R->O_3R->O",
    kinetics = ArrheniusBM(A=(0.00306105,'m^3/(mol*s)'), n=3.2533, w0=(222,'kJ/mol'), E0=(115.57,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03768902570593624, var=0.6026654143860766, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R->O_3R->O',), comment="""BM rule fitted to 8 training reactions at node Root_1R->O_3R->O
    Total Standard Deviation in ln(k): 1.651002517968561"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R->O_3R->O
Total Standard Deviation in ln(k): 1.651002517968561""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R->O_3R->O
Total Standard Deviation in ln(k): 1.651002517968561
""",
)

entry(
    index = 5,
    label = "Root_1R->O_N-3R->O",
    kinetics = ArrheniusBM(A=(53209.4,'m^3/(mol*s)'), n=0.673456, w0=(354.214,'kJ/mol'), E0=(142.827,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.21122012198858867, var=4.906279148229817, Tref=1000.0, N=56, data_mean=0.0, correlation='Root_1R->O_N-3R->O',), comment="""BM rule fitted to 56 training reactions at node Root_1R->O_N-3R->O
    Total Standard Deviation in ln(k): 4.9712165244829585"""),
    rank = 11,
    shortDesc = """BM rule fitted to 56 training reactions at node Root_1R->O_N-3R->O
Total Standard Deviation in ln(k): 4.9712165244829585""",
    longDesc = 
"""
BM rule fitted to 56 training reactions at node Root_1R->O_N-3R->O
Total Standard Deviation in ln(k): 4.9712165244829585
""",
)

entry(
    index = 6,
    label = "Root_N-1R->O_3R->O",
    kinetics = ArrheniusBM(A=(1.70438e-09,'m^3/(mol*s)'), n=4.8865, w0=(354.214,'kJ/mol'), E0=(71.2531,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2551979728165072, var=5.3185056924973235, Tref=1000.0, N=56, data_mean=0.0, correlation='Root_N-1R->O_3R->O',), comment="""BM rule fitted to 56 training reactions at node Root_N-1R->O_3R->O
    Total Standard Deviation in ln(k): 5.264498045962209"""),
    rank = 11,
    shortDesc = """BM rule fitted to 56 training reactions at node Root_N-1R->O_3R->O
Total Standard Deviation in ln(k): 5.264498045962209""",
    longDesc = 
"""
BM rule fitted to 56 training reactions at node Root_N-1R->O_3R->O
Total Standard Deviation in ln(k): 5.264498045962209
""",
)

entry(
    index = 7,
    label = "Root_N-1R->O_N-3R->O",
    kinetics = ArrheniusBM(A=(5.53613e+19,'m^3/(mol*s)'), n=-3.59955, w0=(476.101,'kJ/mol'), E0=(229.025,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7368934635915846, var=11.006434409459201, Tref=1000.0, N=114, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O',), comment="""BM rule fitted to 114 training reactions at node Root_N-1R->O_N-3R->O
    Total Standard Deviation in ln(k): 8.502389526622727"""),
    rank = 11,
    shortDesc = """BM rule fitted to 114 training reactions at node Root_N-1R->O_N-3R->O
Total Standard Deviation in ln(k): 8.502389526622727""",
    longDesc = 
"""
BM rule fitted to 114 training reactions at node Root_N-1R->O_N-3R->O
Total Standard Deviation in ln(k): 8.502389526622727
""",
)

entry(
    index = 8,
    label = "Root_1R->O_3R->O_Ext-1O-R",
    kinetics = ArrheniusBM(A=(0.053912,'m^3/(mol*s)'), n=2.89879, w0=(222,'kJ/mol'), E0=(116.194,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.160247080347969, var=5.664716473986595, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-1O-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_3R->O_Ext-1O-R
    Total Standard Deviation in ln(k): 7.686596438632637"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_3R->O_Ext-1O-R
Total Standard Deviation in ln(k): 7.686596438632637""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_3R->O_Ext-1O-R
Total Standard Deviation in ln(k): 7.686596438632637
""",
)

entry(
    index = 9,
    label = "Root_1R->O_3R->O_Ext-3O-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(3.88038e-05,'m^3/(mol*s)'), n=3.96851, w0=(222,'kJ/mol'), E0=(70.7103,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-3O-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-3O-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-3O-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-3O-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_1R->O_3R->O_1O-u0",
    kinetics = ArrheniusBM(A=(1.72685e-05,'m^3/(mol*s)'), n=3.8992, w0=(222,'kJ/mol'), E0=(112.651,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_1O-u0',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_1O-u0
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
    index = 11,
    label = "Root_1R->O_3R->O_N-1O-u0",
    kinetics = ArrheniusBM(A=(1.30966,'m^3/(mol*s)'), n=2.01045, w0=(222,'kJ/mol'), E0=(121.615,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2372268767621959, var=1.2145918791894776, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_3R->O_N-1O-u0',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_N-1O-u0
    Total Standard Deviation in ln(k): 2.8054363706525454"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_N-1O-u0
Total Standard Deviation in ln(k): 2.8054363706525454""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_N-1O-u0
Total Standard Deviation in ln(k): 2.8054363706525454
""",
)

entry(
    index = 12,
    label = "Root_1R->O_N-3R->O_1O-u0",
    kinetics = ArrheniusBM(A=(104.059,'m^3/(mol*s)'), n=1.46253, w0=(354.37,'kJ/mol'), E0=(125.762,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.15156985425016342, var=3.1507974072221425, Tref=1000.0, N=46, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0',), comment="""BM rule fitted to 46 training reactions at node Root_1R->O_N-3R->O_1O-u0
    Total Standard Deviation in ln(k): 3.939330901356086"""),
    rank = 11,
    shortDesc = """BM rule fitted to 46 training reactions at node Root_1R->O_N-3R->O_1O-u0
Total Standard Deviation in ln(k): 3.939330901356086""",
    longDesc = 
"""
BM rule fitted to 46 training reactions at node Root_1R->O_N-3R->O_1O-u0
Total Standard Deviation in ln(k): 3.939330901356086
""",
)

entry(
    index = 13,
    label = "Root_1R->O_N-3R->O_N-1O-u0",
    kinetics = ArrheniusBM(A=(1.37673e-18,'m^3/(mol*s)'), n=7.09598, w0=(353.5,'kJ/mol'), E0=(55.0346,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.759844288928569, var=9.429543487304173, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0',), comment="""BM rule fitted to 10 training reactions at node Root_1R->O_N-3R->O_N-1O-u0
    Total Standard Deviation in ln(k): 8.06520912332037"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_1R->O_N-3R->O_N-1O-u0
Total Standard Deviation in ln(k): 8.06520912332037""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_1R->O_N-3R->O_N-1O-u0
Total Standard Deviation in ln(k): 8.06520912332037
""",
)

entry(
    index = 14,
    label = "Root_N-1R->O_3R->O_Ext-3O-R",
    kinetics = ArrheniusBM(A=(9.10117e-09,'m^3/(mol*s)'), n=4.58799, w0=(355.318,'kJ/mol'), E0=(66.4471,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.49547621290396426, var=2.3948910231711906, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R',), comment="""BM rule fitted to 22 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R
    Total Standard Deviation in ln(k): 4.34732993593143"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R
Total Standard Deviation in ln(k): 4.34732993593143""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R
Total Standard Deviation in ln(k): 4.34732993593143
""",
)

entry(
    index = 15,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0",
    kinetics = ArrheniusBM(A=(0.875028,'m^3/(mol*s)'), n=2.53077, w0=(353.5,'kJ/mol'), E0=(115.01,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09541207989331034, var=11.637685235419637, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0',), comment="""BM rule fitted to 25 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0
    Total Standard Deviation in ln(k): 7.07869245190145"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0
Total Standard Deviation in ln(k): 7.07869245190145""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0
Total Standard Deviation in ln(k): 7.07869245190145
""",
)

entry(
    index = 16,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0",
    kinetics = ArrheniusBM(A=(2.99799e+09,'m^3/(mol*s)'), n=-0.390634, w0=(353.5,'kJ/mol'), E0=(172.336,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8794998731885698, var=7.899353733928562, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0
    Total Standard Deviation in ln(k): 7.8442647781207"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0
Total Standard Deviation in ln(k): 7.8442647781207""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0
Total Standard Deviation in ln(k): 7.8442647781207
""",
)

entry(
    index = 17,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F",
    kinetics = ArrheniusBM(A=(0.225872,'m^3/(mol*s)'), n=2.32186, w0=(326.667,'kJ/mol'), E0=(102.035,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18066910911741735, var=1.3866870769790212, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F
    Total Standard Deviation in ln(k): 2.8146719659718227"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F
Total Standard Deviation in ln(k): 2.8146719659718227""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F
Total Standard Deviation in ln(k): 2.8146719659718227
""",
)

entry(
    index = 18,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F",
    kinetics = ArrheniusBM(A=(5.14048e+13,'m^3/(mol*s)'), n=-1.872, w0=(484.403,'kJ/mol'), E0=(215.658,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5818918190838651, var=10.817018102077043, Tref=1000.0, N=108, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F',), comment="""BM rule fitted to 108 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F
    Total Standard Deviation in ln(k): 8.055460149219499"""),
    rank = 11,
    shortDesc = """BM rule fitted to 108 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F
Total Standard Deviation in ln(k): 8.055460149219499""",
    longDesc = 
"""
BM rule fitted to 108 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F
Total Standard Deviation in ln(k): 8.055460149219499
""",
)

entry(
    index = 19,
    label = "Root_1R->O_3R->O_Ext-1O-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(0.0487535,'m^3/(mol*s)'), n=3.06244, w0=(222,'kJ/mol'), E0=(73.6796,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-1O-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_1R->O_3R->O_Ext-1O-R_4R!H->C",
    kinetics = ArrheniusBM(A=(0.00499702,'m^3/(mol*s)'), n=3.195, w0=(222,'kJ/mol'), E0=(113.815,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.3671264958245537, var=5.1591057048308535, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-1O-R_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C
    Total Standard Deviation in ln(k): 7.988479259716138"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C
Total Standard Deviation in ln(k): 7.988479259716138""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C
Total Standard Deviation in ln(k): 7.988479259716138
""",
)

entry(
    index = 21,
    label = "Root_1R->O_3R->O_Ext-1O-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.00330356,'m^3/(mol*s)'), n=3.04576, w0=(222,'kJ/mol'), E0=(108.998,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-1O-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_4R!H->C",
    kinetics = ArrheniusBM(A=(1.72407,'m^3/(mol*s)'), n=1.96958, w0=(222,'kJ/mol'), E0=(124.836,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_4R!H->C
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
    index = 23,
    label = "Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.00111026,'m^3/(mol*s)'), n=2.89721, w0=(222,'kJ/mol'), E0=(110.649,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_N-4R!H->C
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
    index = 24,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1",
    kinetics = ArrheniusBM(A=(378.719,'m^3/(mol*s)'), n=1.2828, w0=(354.611,'kJ/mol'), E0=(126.334,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12205593838248062, var=4.076228515042114, Tref=1000.0, N=36, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1',), comment="""BM rule fitted to 36 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1
    Total Standard Deviation in ln(k): 4.354167558287331"""),
    rank = 11,
    shortDesc = """BM rule fitted to 36 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1
Total Standard Deviation in ln(k): 4.354167558287331""",
    longDesc = 
"""
BM rule fitted to 36 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1
Total Standard Deviation in ln(k): 4.354167558287331
""",
)

entry(
    index = 25,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1",
    kinetics = ArrheniusBM(A=(1.18901e-06,'m^3/(mol*s)'), n=3.82331, w0=(353.5,'kJ/mol'), E0=(67.7625,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.021250959501089135, var=1.1604385387028968, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1',), comment="""BM rule fitted to 10 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1
    Total Standard Deviation in ln(k): 2.2129682262825647"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1
Total Standard Deviation in ln(k): 2.2129682262825647""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1
Total Standard Deviation in ln(k): 2.2129682262825647
""",
)

entry(
    index = 26,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(5.97256e-18,'m^3/(mol*s)'), n=6.84928, w0=(353.5,'kJ/mol'), E0=(21.5433,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.7837322265028825, var=27.083511192271114, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R',), comment="""BM rule fitted to 8 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 14.914745641066652"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R
Total Standard Deviation in ln(k): 14.914745641066652""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R
Total Standard Deviation in ln(k): 14.914745641066652
""",
)

entry(
    index = 27,
    label = "Root_1R->O_N-3R->O_N-1O-u0_3CClFH-u1",
    kinetics = ArrheniusBM(A=(0.00154,'m^3/(mol*s)'), n=2.64, w0=(353.5,'kJ/mol'), E0=(109.169,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_3CClFH-u1',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_3CClFH-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_3CClFH-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_3CClFH-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_1R->O_N-3R->O_N-1O-u0_N-3CClFH-u1",
    kinetics = ArrheniusBM(A=(0.000996795,'m^3/(mol*s)'), n=2.97758, w0=(353.5,'kJ/mol'), E0=(143.141,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_N-3CClFH-u1',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_N-3CClFH-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_N-3CClFH-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_N-3CClFH-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 29,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0",
    kinetics = ArrheniusBM(A=(2.13788e-08,'m^3/(mol*s)'), n=4.49069, w0=(355.605,'kJ/mol'), E0=(64.8116,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3051123717852611, var=2.9605875549158713, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0',), comment="""BM rule fitted to 19 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0
    Total Standard Deviation in ln(k): 4.216032942368238"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0
Total Standard Deviation in ln(k): 4.216032942368238""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0
Total Standard Deviation in ln(k): 4.216032942368238
""",
)

entry(
    index = 30,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-1BrCClFHINPSSi-u0",
    kinetics = ArrheniusBM(A=(2.81472e-06,'m^3/(mol*s)'), n=3.81984, w0=(353.5,'kJ/mol'), E0=(116.193,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.1712716753008154, var=11.928027392316274, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-1BrCClFHINPSSi-u0',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-1BrCClFHINPSSi-u0
    Total Standard Deviation in ln(k): 9.866642463251583"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-1BrCClFHINPSSi-u0
Total Standard Deviation in ln(k): 9.866642463251583""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-1BrCClFHINPSSi-u0
Total Standard Deviation in ln(k): 9.866642463251583
""",
)

entry(
    index = 31,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(0.661648,'m^3/(mol*s)'), n=2.5628, w0=(353.5,'kJ/mol'), E0=(114.207,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1131438807490842, var=12.809769490350542, Tref=1000.0, N=23, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 23 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 7.459375961727456"""),
    rank = 11,
    shortDesc = """BM rule fitted to 23 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 7.459375961727456""",
    longDesc = 
"""
BM rule fitted to 23 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 7.459375961727456
""",
)

entry(
    index = 32,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_3O-u1",
    kinetics = ArrheniusBM(A=(0.00127734,'m^3/(mol*s)'), n=3.49913, w0=(353.5,'kJ/mol'), E0=(103.497,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_N-3O-u1",
    kinetics = ArrheniusBM(A=(1.57299e-06,'m^3/(mol*s)'), n=4.1009, w0=(353.5,'kJ/mol'), E0=(103.461,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(0.0235004,'m^3/(mol*s)'), n=2.67239, w0=(353.5,'kJ/mol'), E0=(85.7434,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.444913085487056, var=10.100201699675287, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 12.514209062863104"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 12.514209062863104""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 12.514209062863104
""",
)

entry(
    index = 35,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1",
    kinetics = ArrheniusBM(A=(0.00226498,'m^3/(mol*s)'), n=3.15133, w0=(353.5,'kJ/mol'), E0=(127.522,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 36,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_N-3O-u1",
    kinetics = ArrheniusBM(A=(5.80629e-06,'m^3/(mol*s)'), n=3.94733, w0=(353.5,'kJ/mol'), E0=(138.855,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C",
    kinetics = ArrheniusBM(A=(0.0782216,'m^3/(mol*s)'), n=2.39589, w0=(320,'kJ/mol'), E0=(92.8758,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04818887122543718, var=0.6726922640656996, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C
    Total Standard Deviation in ln(k): 1.7653175539723212"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C
Total Standard Deviation in ln(k): 1.7653175539723212""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C
Total Standard Deviation in ln(k): 1.7653175539723212
""",
)

entry(
    index = 38,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->C",
    kinetics = ArrheniusBM(A=(29364.5,'m^3/(mol*s)'), n=0.785655, w0=(360,'kJ/mol'), E0=(105.704,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->F",
    kinetics = ArrheniusBM(A=(1.48732,'m^3/(mol*s)'), n=2.24745, w0=(326.667,'kJ/mol'), E0=(32.6856,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6726399932929283, var=17.20948979911223, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->F',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->F
    Total Standard Deviation in ln(k): 10.006557801535218"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->F
Total Standard Deviation in ln(k): 10.006557801535218""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->F
Total Standard Deviation in ln(k): 10.006557801535218
""",
)

entry(
    index = 40,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F",
    kinetics = ArrheniusBM(A=(29.5277,'m^3/(mol*s)'), n=1.62227, w0=(493.682,'kJ/mol'), E0=(187.371,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2651050543512581, var=8.35773314623803, Tref=1000.0, N=102, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F',), comment="""BM rule fitted to 102 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F
    Total Standard Deviation in ln(k): 6.461730946047483"""),
    rank = 11,
    shortDesc = """BM rule fitted to 102 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F
Total Standard Deviation in ln(k): 6.461730946047483""",
    longDesc = 
"""
BM rule fitted to 102 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F
Total Standard Deviation in ln(k): 6.461730946047483
""",
)

entry(
    index = 41,
    label = "Root_1R->O_3R->O_Ext-1O-R_4R!H->C_3O-u1",
    kinetics = ArrheniusBM(A=(0.0049864,'m^3/(mol*s)'), n=3.19625, w0=(222,'kJ/mol'), E0=(113.797,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-1O-R_4R!H->C_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_1R->O_3R->O_Ext-1O-R_4R!H->C_N-3O-u1",
    kinetics = ArrheniusBM(A=(0.640932,'m^3/(mol*s)'), n=2.39839, w0=(222,'kJ/mol'), E0=(122.152,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-1O-R_4R!H->C_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 43,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(0.0527449,'m^3/(mol*s)'), n=2.34087, w0=(353.5,'kJ/mol'), E0=(109.273,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08240087327858411, var=3.879425739009372, Tref=1000.0, N=31, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R',), comment="""BM rule fitted to 31 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 4.155615273666526"""),
    rank = 11,
    shortDesc = """BM rule fitted to 31 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R
Total Standard Deviation in ln(k): 4.155615273666526""",
    longDesc = 
"""
BM rule fitted to 31 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R
Total Standard Deviation in ln(k): 4.155615273666526
""",
)

entry(
    index = 44,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C",
    kinetics = ArrheniusBM(A=(5.15234e-10,'m^3/(mol*s)'), n=4.89163, w0=(353.5,'kJ/mol'), E0=(59.3084,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11885735049688435, var=4.585344978605982, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C
    Total Standard Deviation in ln(k): 4.591459706531456"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C
Total Standard Deviation in ln(k): 4.591459706531456""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C
Total Standard Deviation in ln(k): 4.591459706531456
""",
)

entry(
    index = 45,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->C",
    kinetics = ArrheniusBM(A=(1.04105,'m^3/(mol*s)'), n=2.3137, w0=(393.5,'kJ/mol'), E0=(121.184,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(0.000245593,'m^3/(mol*s)'), n=3.10149, w0=(353.5,'kJ/mol'), E0=(62.672,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.183070665051795, var=15.116406908742166, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R',), comment="""BM rule fitted to 8 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 13.279476810748406"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R
Total Standard Deviation in ln(k): 13.279476810748406""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R
Total Standard Deviation in ln(k): 13.279476810748406
""",
)

entry(
    index = 47,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-1O-R",
    kinetics = ArrheniusBM(A=(0.000178698,'m^3/(mol*s)'), n=3.25898, w0=(353.5,'kJ/mol'), E0=(114.913,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-1O-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-1O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 48,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH",
    kinetics = ArrheniusBM(A=(3.92577e-15,'m^3/(mol*s)'), n=6.0378, w0=(353.5,'kJ/mol'), E0=(47.6909,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.536016221907208, var=10.673457503104192, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH',), comment="""BM rule fitted to 7 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH
    Total Standard Deviation in ln(k): 10.408858438046696"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH
Total Standard Deviation in ln(k): 10.408858438046696""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH
Total Standard Deviation in ln(k): 10.408858438046696
""",
)

entry(
    index = 49,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_N-Sp-4R!H-3CClFH",
    kinetics = ArrheniusBM(A=(0.00171,'m^3/(mol*s)'), n=2.75, w0=(353.5,'kJ/mol'), E0=(228.746,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_N-Sp-4R!H-3CClFH',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_N-Sp-4R!H-3CClFH
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_N-Sp-4R!H-3CClFH
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_N-Sp-4R!H-3CClFH
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 50,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C",
    kinetics = ArrheniusBM(A=(8.28352,'m^3/(mol*s)'), n=2.0705, w0=(353.5,'kJ/mol'), E0=(121.428,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.14622528691466438, var=1.43137498279478, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C',), comment="""BM rule fitted to 18 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C
    Total Standard Deviation in ln(k): 2.765866959709696"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C
Total Standard Deviation in ln(k): 2.765866959709696""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C
Total Standard Deviation in ln(k): 2.765866959709696
""",
)

entry(
    index = 51,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_N-1BrCClFHINPSSi->C",
    kinetics = ArrheniusBM(A=(0.000345832,'m^3/(mol*s)'), n=3.07623, w0=(393.5,'kJ/mol'), E0=(119.902,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_N-1BrCClFHINPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_N-1BrCClFHINPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_N-1BrCClFHINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_N-1BrCClFHINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 52,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(9.76107e+14,'m^3/(mol*s)'), n=-2.15023, w0=(353.5,'kJ/mol'), E0=(179.903,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.28557476142198046, var=91.69606931051206, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 19.91447962577011"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 19.91447962577011""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 19.91447962577011
""",
)

entry(
    index = 53,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi",
    kinetics = ArrheniusBM(A=(1.72013,'m^3/(mol*s)'), n=2.4493, w0=(353.5,'kJ/mol'), E0=(175.233,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi
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
    index = 54,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi",
    kinetics = ArrheniusBM(A=(0.893779,'m^3/(mol*s)'), n=2.52538, w0=(353.5,'kJ/mol'), E0=(114.665,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11607207289645985, var=12.803409109755234, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi',), comment="""BM rule fitted to 22 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi
    Total Standard Deviation in ln(k): 7.464951697527306"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi
Total Standard Deviation in ln(k): 7.464951697527306""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi
Total Standard Deviation in ln(k): 7.464951697527306
""",
)

entry(
    index = 55,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi",
    kinetics = ArrheniusBM(A=(0.0261731,'m^3/(mol*s)'), n=2.65783, w0=(353.5,'kJ/mol'), E0=(85.7434,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.472097495493643, var=16.14965698319457, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi
    Total Standard Deviation in ln(k): 16.780218900562463"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi
Total Standard Deviation in ln(k): 16.780218900562463""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi
Total Standard Deviation in ln(k): 16.780218900562463
""",
)

entry(
    index = 56,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H-1BrCClFHINPSSi",
    kinetics = ArrheniusBM(A=(0.0387235,'m^3/(mol*s)'), n=2.8378, w0=(353.5,'kJ/mol'), E0=(143.208,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H-1BrCClFHINPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H-1BrCClFHINPSSi
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
    index = 57,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.0108084,'m^3/(mol*s)'), n=2.63211, w0=(320,'kJ/mol'), E0=(83.0209,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.38367603811109313, var=1.3832635132527058, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R
    Total Standard Deviation in ln(k): 3.3218236471716764"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R
Total Standard Deviation in ln(k): 3.3218236471716764""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R
Total Standard Deviation in ln(k): 3.3218236471716764
""",
)

entry(
    index = 58,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->F_1CClH->C",
    kinetics = ArrheniusBM(A=(3.00113e+09,'m^3/(mol*s)'), n=-0.1616, w0=(320,'kJ/mol'), E0=(137.69,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6975612345784726, var=2.0774207414964425, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->F_1CClH->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->F_1CClH->C
    Total Standard Deviation in ln(k): 4.642143280483522"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->F_1CClH->C
Total Standard Deviation in ln(k): 4.642143280483522""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->F_1CClH->C
Total Standard Deviation in ln(k): 4.642143280483522
""",
)

entry(
    index = 59,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->F_N-1CClH->C",
    kinetics = ArrheniusBM(A=(1365.62,'m^3/(mol*s)'), n=0.97718, w0=(360,'kJ/mol'), E0=(107.46,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->F_N-1CClH->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->F_N-1CClH->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->F_N-1CClH->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->F_N-1CClH->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 60,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H",
    kinetics = ArrheniusBM(A=(0.0523259,'m^3/(mol*s)'), n=2.69179, w0=(516.626,'kJ/mol'), E0=(159.38,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.46337231346705193, var=4.404673011537254, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H',), comment="""BM rule fitted to 14 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H
    Total Standard Deviation in ln(k): 5.371652271291064"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H
Total Standard Deviation in ln(k): 5.371652271291064""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H
Total Standard Deviation in ln(k): 5.371652271291064
""",
)

entry(
    index = 61,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H",
    kinetics = ArrheniusBM(A=(0.0160864,'m^3/(mol*s)'), n=2.48754, w0=(490.031,'kJ/mol'), E0=(184.297,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07243131170897807, var=4.911461384111603, Tref=1000.0, N=88, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H',), comment="""BM rule fitted to 88 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H
    Total Standard Deviation in ln(k): 4.62484543788691"""),
    rank = 11,
    shortDesc = """BM rule fitted to 88 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H
Total Standard Deviation in ln(k): 4.62484543788691""",
    longDesc = 
"""
BM rule fitted to 88 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H
Total Standard Deviation in ln(k): 4.62484543788691
""",
)

entry(
    index = 62,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(5.89739e-06,'m^3/(mol*s)'), n=3.34803, w0=(353.5,'kJ/mol'), E0=(99.0058,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.8654383088615774, var=15.298175858458903, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl
    Total Standard Deviation in ln(k): 15.040690514926796"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl
Total Standard Deviation in ln(k): 15.040690514926796""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl
Total Standard Deviation in ln(k): 15.040690514926796
""",
)

entry(
    index = 63,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(0.000264819,'m^3/(mol*s)'), n=3.01826, w0=(353.5,'kJ/mol'), E0=(96.5551,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0443910038622758, var=4.580376471892987, Tref=1000.0, N=27, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl',), comment="""BM rule fitted to 27 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 4.402031932156766"""),
    rank = 11,
    shortDesc = """BM rule fitted to 27 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 4.402031932156766""",
    longDesc = 
"""
BM rule fitted to 27 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 4.402031932156766
""",
)

entry(
    index = 64,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R",
    kinetics = ArrheniusBM(A=(0.040025,'m^3/(mol*s)'), n=2.50006, w0=(353.5,'kJ/mol'), E0=(108.196,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1263403561200987, var=0.09019034707082725, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R
    Total Standard Deviation in ln(k): 0.919494260417605"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R
Total Standard Deviation in ln(k): 0.919494260417605""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R
Total Standard Deviation in ln(k): 0.919494260417605
""",
)

entry(
    index = 65,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(0.000340767,'m^3/(mol*s)'), n=3.06, w0=(353.5,'kJ/mol'), E0=(73.6425,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=5.91127940619075, var=69.36738602575939, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 31.549314988912286"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 31.549314988912286""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 31.549314988912286
""",
)

entry(
    index = 66,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-1O-R",
    kinetics = ArrheniusBM(A=(1.85866e-05,'m^3/(mol*s)'), n=3.19173, w0=(353.5,'kJ/mol'), E0=(113.846,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-1O-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-1O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 67,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C",
    kinetics = ArrheniusBM(A=(9.97946e-13,'m^3/(mol*s)'), n=5.64084, w0=(353.5,'kJ/mol'), E0=(76.2913,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.30434017465797997, var=2.7049866552525774, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C
    Total Standard Deviation in ln(k): 4.061830240247385"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C
Total Standard Deviation in ln(k): 4.061830240247385""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C
Total Standard Deviation in ln(k): 4.061830240247385
""",
)

entry(
    index = 68,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(1.07293e-05,'m^3/(mol*s)'), n=3.59914, w0=(353.5,'kJ/mol'), E0=(106.801,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 69,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O",
    kinetics = ArrheniusBM(A=(0.000484074,'m^3/(mol*s)'), n=2.91294, w0=(353.5,'kJ/mol'), E0=(110.151,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.8008208526366516, var=0.8869888793603722, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O
    Total Standard Deviation in ln(k): 3.900173935744253"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O
Total Standard Deviation in ln(k): 3.900173935744253""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O
Total Standard Deviation in ln(k): 3.900173935744253
""",
)

entry(
    index = 70,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O",
    kinetics = ArrheniusBM(A=(1.1486e-10,'m^3/(mol*s)'), n=4.67579, w0=(353.5,'kJ/mol'), E0=(116.648,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18966329920532646, var=1.6710359937267594, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O',), comment="""BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O
    Total Standard Deviation in ln(k): 3.0680330674033436"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O
Total Standard Deviation in ln(k): 3.0680330674033436""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O
Total Standard Deviation in ln(k): 3.0680330674033436
""",
)

entry(
    index = 71,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_4R!H->C",
    kinetics = ArrheniusBM(A=(0.000635818,'m^3/(mol*s)'), n=3.24928, w0=(353.5,'kJ/mol'), E0=(107.269,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7853855271379451, var=4.633895826089613, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_4R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_4R!H->C
    Total Standard Deviation in ln(k): 6.288820549228972"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_4R!H->C
Total Standard Deviation in ln(k): 6.288820549228972""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_4R!H->C
Total Standard Deviation in ln(k): 6.288820549228972
""",
)

entry(
    index = 72,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(4.48831,'m^3/(mol*s)'), n=2.147, w0=(353.5,'kJ/mol'), E0=(114.984,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.054447482843778434, var=0.3545605216991095, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C',), comment="""BM rule fitted to 14 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C
    Total Standard Deviation in ln(k): 1.330521918191035"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C
Total Standard Deviation in ln(k): 1.330521918191035""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C
Total Standard Deviation in ln(k): 1.330521918191035
""",
)

entry(
    index = 73,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(354736,'m^3/(mol*s)'), n=0.720119, w0=(353.5,'kJ/mol'), E0=(91.4106,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 74,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F",
    kinetics = ArrheniusBM(A=(2951.78,'m^3/(mol*s)'), n=1.56698, w0=(353.5,'kJ/mol'), E0=(145.313,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.24680212978546387, var=1.9656333009757083, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F
    Total Standard Deviation in ln(k): 3.430765381053054"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F
Total Standard Deviation in ln(k): 3.430765381053054""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F
Total Standard Deviation in ln(k): 3.430765381053054
""",
)

entry(
    index = 75,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F",
    kinetics = ArrheniusBM(A=(29467.4,'m^3/(mol*s)'), n=1.21194, w0=(353.5,'kJ/mol'), E0=(125.535,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06252418558900218, var=23.877431695835654, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F',), comment="""BM rule fitted to 14 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F
    Total Standard Deviation in ln(k): 9.953141476784701"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F
Total Standard Deviation in ln(k): 9.953141476784701""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F
Total Standard Deviation in ln(k): 9.953141476784701
""",
)

entry(
    index = 76,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O",
    kinetics = ArrheniusBM(A=(0.0371909,'m^3/(mol*s)'), n=2.60707, w0=(353.5,'kJ/mol'), E0=(96.5492,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.221747880371906, var=14.80789706567018, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O
    Total Standard Deviation in ln(k): 15.809271081671426"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O
Total Standard Deviation in ln(k): 15.809271081671426""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O
Total Standard Deviation in ln(k): 15.809271081671426
""",
)

entry(
    index = 77,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->O",
    kinetics = ArrheniusBM(A=(1.95805e+20,'m^3/(mol*s)'), n=-3.41724, w0=(353.5,'kJ/mol'), E0=(173.275,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3501671031459575, var=69.16912336717945, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->O
    Total Standard Deviation in ln(k): 17.55279284866854"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->O
Total Standard Deviation in ln(k): 17.55279284866854""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->O
Total Standard Deviation in ln(k): 17.55279284866854
""",
)

entry(
    index = 78,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.0815946,'m^3/(mol*s)'), n=2.37871, w0=(320,'kJ/mol'), E0=(92.8758,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03551235230664396, var=0.348983181696394, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 1.2735202231307345"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 1.2735202231307345""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 1.2735202231307345
""",
)

entry(
    index = 79,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->F_1CClH->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(59837,'m^3/(mol*s)'), n=1.19288, w0=(320,'kJ/mol'), E0=(111.469,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.0476742663608252, var=3.773344480265319, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->F_1CClH->C_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->F_1CClH->C_Ext-1C-R
    Total Standard Deviation in ln(k): 6.526565018260485"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->F_1CClH->C_Ext-1C-R
Total Standard Deviation in ln(k): 6.526565018260485""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->F_1CClH->C_Ext-1C-R
Total Standard Deviation in ln(k): 6.526565018260485
""",
)

entry(
    index = 80,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C",
    kinetics = ArrheniusBM(A=(1.4281e-16,'m^3/(mol*s)'), n=6.89419, w0=(525,'kJ/mol'), E0=(126.81,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.26333986996410924, var=1.7443482339537688, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C
    Total Standard Deviation in ln(k): 3.309387282722058"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C
Total Standard Deviation in ln(k): 3.309387282722058""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C
Total Standard Deviation in ln(k): 3.309387282722058
""",
)

entry(
    index = 81,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_N-1CClH->C",
    kinetics = ArrheniusBM(A=(650.29,'m^3/(mol*s)'), n=1.25799, w0=(407.77,'kJ/mol'), E0=(120.836,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_N-1CClH->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_N-1CClH->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_N-1CClH->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_N-1CClH->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 82,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1",
    kinetics = ArrheniusBM(A=(0.0155023,'m^3/(mol*s)'), n=2.4919, w0=(490.4,'kJ/mol'), E0=(184.27,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07196907439090044, var=4.8958854986901, Tref=1000.0, N=82, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1',), comment="""BM rule fitted to 82 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1
    Total Standard Deviation in ln(k): 4.616633550786232"""),
    rank = 11,
    shortDesc = """BM rule fitted to 82 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1
Total Standard Deviation in ln(k): 4.616633550786232""",
    longDesc = 
"""
BM rule fitted to 82 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1
Total Standard Deviation in ln(k): 4.616633550786232
""",
)

entry(
    index = 83,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1",
    kinetics = ArrheniusBM(A=(1.81911e-05,'m^3/(mol*s)'), n=3.64993, w0=(485,'kJ/mol'), E0=(159.215,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04751116821897129, var=12.86647698666389, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1
    Total Standard Deviation in ln(k): 7.310333804463108"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1
Total Standard Deviation in ln(k): 7.310333804463108""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1
Total Standard Deviation in ln(k): 7.310333804463108
""",
)

entry(
    index = 84,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R",
    kinetics = ArrheniusBM(A=(1.41898e-06,'m^3/(mol*s)'), n=3.52361, w0=(353.5,'kJ/mol'), E0=(95.7533,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.705400020897315, var=25.4564433034689, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R
    Total Standard Deviation in ln(k): 19.424816583247015"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R
Total Standard Deviation in ln(k): 19.424816583247015""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R
Total Standard Deviation in ln(k): 19.424816583247015
""",
)

entry(
    index = 85,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(2.40529e-06,'m^3/(mol*s)'), n=3.70283, w0=(353.5,'kJ/mol'), E0=(138.874,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-3CClFH-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-3CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-3CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 86,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(1.9965e-05,'m^3/(mol*s)'), n=3.06368, w0=(353.5,'kJ/mol'), E0=(93.4586,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.10951814676230599, var=0.8144639060757135, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R',), comment="""BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 2.084397600200855"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 2.084397600200855""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 2.084397600200855
""",
)

entry(
    index = 87,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi",
    kinetics = ArrheniusBM(A=(0.00502134,'m^3/(mol*s)'), n=2.89121, w0=(353.5,'kJ/mol'), E0=(173.92,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 88,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi",
    kinetics = ArrheniusBM(A=(1.24392e-07,'m^3/(mol*s)'), n=4.02029, w0=(353.5,'kJ/mol'), E0=(65.9796,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.19752774973835366, var=4.0298390155139385, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi',), comment="""BM rule fitted to 21 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi
    Total Standard Deviation in ln(k): 4.520698077501679"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi
Total Standard Deviation in ln(k): 4.520698077501679""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi
Total Standard Deviation in ln(k): 4.520698077501679
""",
)

entry(
    index = 89,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_4R!H->C",
    kinetics = ArrheniusBM(A=(0.000476496,'m^3/(mol*s)'), n=3.27616, w0=(353.5,'kJ/mol'), E0=(125.819,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 90,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.0281256,'m^3/(mol*s)'), n=2.53702, w0=(353.5,'kJ/mol'), E0=(106.61,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.34576941237773406, var=0.18043928384878202, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_N-4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_N-4R!H->C
    Total Standard Deviation in ln(k): 1.7203416492834527"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_N-4R!H->C
Total Standard Deviation in ln(k): 1.7203416492834527""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_N-4R!H->C
Total Standard Deviation in ln(k): 1.7203416492834527
""",
)

entry(
    index = 91,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C",
    kinetics = ArrheniusBM(A=(0.000290035,'m^3/(mol*s)'), n=3.07816, w0=(353.5,'kJ/mol'), E0=(80.7316,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=5.42585721184051, var=60.29990426503073, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C
    Total Standard Deviation in ln(k): 29.200178965666076"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C
Total Standard Deviation in ln(k): 29.200178965666076""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C
Total Standard Deviation in ln(k): 29.200178965666076
""",
)

entry(
    index = 92,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(2.47592e+10,'m^3/(mol*s)'), n=-0.535493, w0=(353.5,'kJ/mol'), E0=(52.3754,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 93,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C_Sp-4C-3CClFH",
    kinetics = ArrheniusBM(A=(3.03844e-05,'m^3/(mol*s)'), n=3.46112, w0=(353.5,'kJ/mol'), E0=(113.457,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C_Sp-4C-3CClFH',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C_Sp-4C-3CClFH
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C_Sp-4C-3CClFH
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C_Sp-4C-3CClFH
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 94,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C_N-Sp-4C-3CClFH",
    kinetics = ArrheniusBM(A=(9.84034e-05,'m^3/(mol*s)'), n=3.38442, w0=(353.5,'kJ/mol'), E0=(140.646,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C_N-Sp-4C-3CClFH',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C_N-Sp-4C-3CClFH
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C_N-Sp-4C-3CClFH
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C_N-Sp-4C-3CClFH
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 95,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O_3CClFH-u1",
    kinetics = ArrheniusBM(A=(0.000576508,'m^3/(mol*s)'), n=2.8908, w0=(353.5,'kJ/mol'), E0=(110.367,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O_3CClFH-u1',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O_3CClFH-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O_3CClFH-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O_3CClFH-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 96,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O_N-3CClFH-u1",
    kinetics = ArrheniusBM(A=(2.33307,'m^3/(mol*s)'), n=1.93544, w0=(353.5,'kJ/mol'), E0=(141.17,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O_N-3CClFH-u1',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O_N-3CClFH-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O_N-3CClFH-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O_N-3CClFH-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 97,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_4CF->F",
    kinetics = ArrheniusBM(A=(8.90879e-11,'m^3/(mol*s)'), n=4.70709, w0=(353.5,'kJ/mol'), E0=(116.298,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17388835585505416, var=1.7003450236386057, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_4CF->F',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_4CF->F
    Total Standard Deviation in ln(k): 3.0510253984843776"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_4CF->F
Total Standard Deviation in ln(k): 3.0510253984843776""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_4CF->F
Total Standard Deviation in ln(k): 3.0510253984843776
""",
)

entry(
    index = 98,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->F",
    kinetics = ArrheniusBM(A=(124.581,'m^3/(mol*s)'), n=1.2682, w0=(353.5,'kJ/mol'), E0=(149.553,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->F',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 99,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_4R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.000645275,'m^3/(mol*s)'), n=3.24695, w0=(353.5,'kJ/mol'), E0=(107.244,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7850264791316793, var=4.658032934219402, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_4R!H->C_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_4R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 6.299143116378881"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 6.299143116378881""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 6.299143116378881
""",
)

entry(
    index = 100,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.0474431,'m^3/(mol*s)'), n=2.71862, w0=(353.5,'kJ/mol'), E0=(103.523,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.08896806343444627, var=0.3785331031062749, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 1.4569519849493786"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 1.4569519849493786""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 1.4569519849493786
""",
)

entry(
    index = 101,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_4FO->F",
    kinetics = ArrheniusBM(A=(0.00762111,'m^3/(mol*s)'), n=2.86357, w0=(353.5,'kJ/mol'), E0=(106.35,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_4FO->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_4FO->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_4FO->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_4FO->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 102,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_N-4FO->F",
    kinetics = ArrheniusBM(A=(2.91478e-07,'m^3/(mol*s)'), n=4.48603, w0=(353.5,'kJ/mol'), E0=(111.506,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_N-4FO->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_N-4FO->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_N-4FO->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_N-4FO->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 103,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(1.56428e+06,'m^3/(mol*s)'), n=0.792213, w0=(353.5,'kJ/mol'), E0=(157.747,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.39883970844672484, var=2.2979472870590048, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 4.041084072070477"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 4.041084072070477""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 4.041084072070477
""",
)

entry(
    index = 104,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_3O-u1",
    kinetics = ArrheniusBM(A=(0.150831,'m^3/(mol*s)'), n=2.7069, w0=(353.5,'kJ/mol'), E0=(105.444,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 105,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_N-3O-u1",
    kinetics = ArrheniusBM(A=(5.86794e-05,'m^3/(mol*s)'), n=3.82866, w0=(353.5,'kJ/mol'), E0=(124.919,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 106,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi",
    kinetics = ArrheniusBM(A=(8.68966e+09,'m^3/(mol*s)'), n=-0.366497, w0=(353.5,'kJ/mol'), E0=(208.911,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.30877144873132584, var=173.12600183956022, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi
    Total Standard Deviation in ln(k): 27.15358143047648"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 27.15358143047648""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 27.15358143047648
""",
)

entry(
    index = 107,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi",
    kinetics = ArrheniusBM(A=(4.59372e+08,'m^3/(mol*s)'), n=0.0118863, w0=(353.5,'kJ/mol'), E0=(132.743,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4750676185683855, var=17.464590627665405, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi
    Total Standard Deviation in ln(k): 9.571556952695122"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 9.571556952695122""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 9.571556952695122
""",
)

entry(
    index = 108,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(0.0305183,'m^3/(mol*s)'), n=2.6347, w0=(353.5,'kJ/mol'), E0=(91.254,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=5.3942370373753, var=58.909468306530705, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 28.940203043314867"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 28.940203043314867""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 28.940203043314867
""",
)

entry(
    index = 109,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_3O-u1",
    kinetics = ArrheniusBM(A=(0.00474579,'m^3/(mol*s)'), n=2.96408, w0=(353.5,'kJ/mol'), E0=(109.07,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 110,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_N-3O-u1",
    kinetics = ArrheniusBM(A=(1.32859,'m^3/(mol*s)'), n=2.43214, w0=(353.5,'kJ/mol'), E0=(137.126,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 111,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->O_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(2.23847e+07,'m^3/(mol*s)'), n=0.359183, w0=(353.5,'kJ/mol'), E0=(82.2933,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->O_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->O_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->O_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->O_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 112,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R_4R!H->O",
    kinetics = ArrheniusBM(A=(0.00484609,'m^3/(mol*s)'), n=2.74562, w0=(320,'kJ/mol'), E0=(86.8099,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R_4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R_4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 113,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(0.367477,'m^3/(mol*s)'), n=2.16709, w0=(320,'kJ/mol'), E0=(90.85,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.14134114997090105, var=1.9469810745700107, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R_N-4R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R_N-4R!H->O
    Total Standard Deviation in ln(k): 3.152420846849181"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R_N-4R!H->O
Total Standard Deviation in ln(k): 3.152420846849181""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R_N-4R!H->O
Total Standard Deviation in ln(k): 3.152420846849181
""",
)

entry(
    index = 114,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->F_1CClH->C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(4.6364e+06,'m^3/(mol*s)'), n=0.643003, w0=(320,'kJ/mol'), E0=(123.528,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.3407708968887784, var=3.3731727788117047, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->F_1CClH->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->F_1CClH->C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 7.050707501519996"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->F_1CClH->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 7.050707501519996""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->F_1CClH->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 7.050707501519996
""",
)

entry(
    index = 115,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.22657e-17,'m^3/(mol*s)'), n=6.97948, w0=(525,'kJ/mol'), E0=(126.297,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2610430704552387, var=1.7207225930956775, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R
    Total Standard Deviation in ln(k): 3.2856247357268074"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.2856247357268074""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.2856247357268074
""",
)

entry(
    index = 116,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C",
    kinetics = ArrheniusBM(A=(1.04239e-06,'m^3/(mol*s)'), n=3.76371, w0=(485,'kJ/mol'), E0=(179.665,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.007412696986269543, var=3.2119615290120844, Tref=1000.0, N=68, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C',), comment="""BM rule fitted to 68 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C
    Total Standard Deviation in ln(k): 3.6115002719605664"""),
    rank = 11,
    shortDesc = """BM rule fitted to 68 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C
Total Standard Deviation in ln(k): 3.6115002719605664""",
    longDesc = 
"""
BM rule fitted to 68 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C
Total Standard Deviation in ln(k): 3.6115002719605664
""",
)

entry(
    index = 117,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C",
    kinetics = ArrheniusBM(A=(2.24072e+06,'m^3/(mol*s)'), n=-0.0769205, w0=(516.626,'kJ/mol'), E0=(187.279,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03837702426697858, var=15.717101098793703, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C',), comment="""BM rule fitted to 14 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C
    Total Standard Deviation in ln(k): 8.044156659192115"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C
Total Standard Deviation in ln(k): 8.044156659192115""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C
Total Standard Deviation in ln(k): 8.044156659192115
""",
)

entry(
    index = 118,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1_Ext-3CCl-R_Ext-3CCl-R",
    kinetics = ArrheniusBM(A=(2.24206e-07,'m^3/(mol*s)'), n=4.41751, w0=(485,'kJ/mol'), E0=(146.158,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.05122312627766323, var=0.10807146951858823, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1_Ext-3CCl-R_Ext-3CCl-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1_Ext-3CCl-R_Ext-3CCl-R
    Total Standard Deviation in ln(k): 0.787742450179583"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1_Ext-3CCl-R_Ext-3CCl-R
Total Standard Deviation in ln(k): 0.787742450179583""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1_Ext-3CCl-R_Ext-3CCl-R
Total Standard Deviation in ln(k): 0.787742450179583
""",
)

entry(
    index = 119,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1_Ext-3CCl-R_Sp-4R!H-3CCl",
    kinetics = ArrheniusBM(A=(2.19995e-06,'m^3/(mol*s)'), n=3.79688, w0=(485,'kJ/mol'), E0=(176.429,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3545102319141808, var=33.37437654867942, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1_Ext-3CCl-R_Sp-4R!H-3CCl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1_Ext-3CCl-R_Sp-4R!H-3CCl
    Total Standard Deviation in ln(k): 12.472196123677417"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1_Ext-3CCl-R_Sp-4R!H-3CCl
Total Standard Deviation in ln(k): 12.472196123677417""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1_Ext-3CCl-R_Sp-4R!H-3CCl
Total Standard Deviation in ln(k): 12.472196123677417
""",
)

entry(
    index = 120,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1_Ext-3CCl-R_N-Sp-4R!H-3CCl",
    kinetics = ArrheniusBM(A=(1.71492e-09,'m^3/(mol*s)'), n=4.37345, w0=(485,'kJ/mol'), E0=(128.047,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1_Ext-3CCl-R_N-Sp-4R!H-3CCl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1_Ext-3CCl-R_N-Sp-4R!H-3CCl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1_Ext-3CCl-R_N-Sp-4R!H-3CCl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1_Ext-3CCl-R_N-Sp-4R!H-3CCl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 121,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R_5R!H->C",
    kinetics = ArrheniusBM(A=(8.19658e-06,'m^3/(mol*s)'), n=3.30549, w0=(353.5,'kJ/mol'), E0=(98.8969,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 122,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(9.46969e-05,'m^3/(mol*s)'), n=2.97971, w0=(353.5,'kJ/mol'), E0=(149.359,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 123,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi",
    kinetics = ArrheniusBM(A=(1.9354e-06,'m^3/(mol*s)'), n=3.35153, w0=(353.5,'kJ/mol'), E0=(87.5501,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08060587025515112, var=0.26954735424019977, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi
    Total Standard Deviation in ln(k): 1.2433446692820127"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi
Total Standard Deviation in ln(k): 1.2433446692820127""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi
Total Standard Deviation in ln(k): 1.2433446692820127
""",
)

entry(
    index = 124,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi",
    kinetics = ArrheniusBM(A=(2.22405e-05,'m^3/(mol*s)'), n=3.55361, w0=(353.5,'kJ/mol'), E0=(151.807,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 125,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi",
    kinetics = ArrheniusBM(A=(2.53764e-08,'m^3/(mol*s)'), n=4.20712, w0=(353.5,'kJ/mol'), E0=(71.2531,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.31156794738602406, var=5.749860370571932, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi',), comment="""BM rule fitted to 16 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi
    Total Standard Deviation in ln(k): 5.589961510975441"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi
Total Standard Deviation in ln(k): 5.589961510975441""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi
Total Standard Deviation in ln(k): 5.589961510975441
""",
)

entry(
    index = 126,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi",
    kinetics = ArrheniusBM(A=(1.57353e-06,'m^3/(mol*s)'), n=3.77675, w0=(353.5,'kJ/mol'), E0=(91.2355,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3096871457026521, var=0.7634027499262561, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi',), comment="""BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi
    Total Standard Deviation in ln(k): 2.529704021817279"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi
Total Standard Deviation in ln(k): 2.529704021817279""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi
Total Standard Deviation in ln(k): 2.529704021817279
""",
)

entry(
    index = 127,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_N-4R!H->C_4BrClFINOPSSi->F",
    kinetics = ArrheniusBM(A=(0.01745,'m^3/(mol*s)'), n=2.59, w0=(353.5,'kJ/mol'), E0=(105.176,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_N-4R!H->C_4BrClFINOPSSi->F',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_N-4R!H->C_4BrClFINOPSSi->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_N-4R!H->C_4BrClFINOPSSi->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_N-4R!H->C_4BrClFINOPSSi->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 128,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_N-4R!H->C_N-4BrClFINOPSSi->F",
    kinetics = ArrheniusBM(A=(0.000849095,'m^3/(mol*s)'), n=3.17369, w0=(353.5,'kJ/mol'), E0=(115.83,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_N-4R!H->C_N-4BrClFINOPSSi->F',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_N-4R!H->C_N-4BrClFINOPSSi->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_N-4R!H->C_N-4BrClFINOPSSi->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->C_Ext-1O-R_N-4R!H->C_N-4BrClFINOPSSi->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 129,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_5R!H->C",
    kinetics = ArrheniusBM(A=(5.31199e+07,'m^3/(mol*s)'), n=0.114184, w0=(353.5,'kJ/mol'), E0=(73.8142,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2208263570551893, var=1.9761977631219036, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_5R!H->C
    Total Standard Deviation in ln(k): 3.3730425624361167"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_5R!H->C
Total Standard Deviation in ln(k): 3.3730425624361167""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_5R!H->C
Total Standard Deviation in ln(k): 3.3730425624361167
""",
)

entry(
    index = 130,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.0002226,'m^3/(mol*s)'), n=3.1084, w0=(353.5,'kJ/mol'), E0=(94.5663,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 131,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_4CF->F_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(2.36549e-06,'m^3/(mol*s)'), n=3.4429, w0=(353.5,'kJ/mol'), E0=(138.531,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.057717188173985995, var=1.4725290034972491, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_4CF->F_Ext-3CClFH-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_4CF->F_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 2.5777200944218834"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_4CF->F_Ext-3CClFH-R
Total Standard Deviation in ln(k): 2.5777200944218834""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_4CF->F_Ext-3CClFH-R
Total Standard Deviation in ln(k): 2.5777200944218834
""",
)

entry(
    index = 132,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_4R!H->C_Ext-1C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(23683.8,'m^3/(mol*s)'), n=1.01364, w0=(353.5,'kJ/mol'), E0=(138.828,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5311374402950297, var=7.859704199276205, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_4R!H->C_Ext-1C-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_4R!H->C_Ext-1C-R_5R!H->C
    Total Standard Deviation in ln(k): 6.954823846704389"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_4R!H->C_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 6.954823846704389""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_4R!H->C_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 6.954823846704389
""",
)

entry(
    index = 133,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_4R!H->C_Ext-1C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(4.6139e-06,'m^3/(mol*s)'), n=3.99356, w0=(353.5,'kJ/mol'), E0=(98.0064,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_4R!H->C_Ext-1C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_4R!H->C_Ext-1C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_4R!H->C_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_4R!H->C_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 134,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_Sp-5R!H=1C",
    kinetics = ArrheniusBM(A=(6.05875e-06,'m^3/(mol*s)'), n=3.78969, w0=(353.5,'kJ/mol'), E0=(75.1179,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.25813018408344474, var=0.6254283369202852, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_Sp-5R!H=1C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_Sp-5R!H=1C
    Total Standard Deviation in ln(k): 2.233993537009855"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_Sp-5R!H=1C
Total Standard Deviation in ln(k): 2.233993537009855""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_Sp-5R!H=1C
Total Standard Deviation in ln(k): 2.233993537009855
""",
)

entry(
    index = 135,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_N-Sp-5R!H=1C",
    kinetics = ArrheniusBM(A=(1.17707,'m^3/(mol*s)'), n=2.33364, w0=(353.5,'kJ/mol'), E0=(110.144,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.15090881084269162, var=0.41210042852399287, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_N-Sp-5R!H=1C',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_N-Sp-5R!H=1C
    Total Standard Deviation in ln(k): 1.6661085268717226"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_N-Sp-5R!H=1C
Total Standard Deviation in ln(k): 1.6661085268717226""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_N-Sp-5R!H=1C
Total Standard Deviation in ln(k): 1.6661085268717226
""",
)

entry(
    index = 136,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_5R!H->O",
    kinetics = ArrheniusBM(A=(143.594,'m^3/(mol*s)'), n=1.91558, w0=(353.5,'kJ/mol'), E0=(148.846,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.22786649808903706, var=6.287439671009029, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_5R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_5R!H->O
    Total Standard Deviation in ln(k): 5.599355493828799"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_5R!H->O
Total Standard Deviation in ln(k): 5.599355493828799""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_5R!H->O
Total Standard Deviation in ln(k): 5.599355493828799
""",
)

entry(
    index = 137,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(7293.09,'m^3/(mol*s)'), n=1.47687, w0=(353.5,'kJ/mol'), E0=(146.268,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3365081680268378, var=3.1312204306572937, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O
    Total Standard Deviation in ln(k): 4.392927713275807"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O
Total Standard Deviation in ln(k): 4.392927713275807""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O
Total Standard Deviation in ln(k): 4.392927713275807
""",
)

entry(
    index = 138,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-4CClO-R",
    kinetics = ArrheniusBM(A=(0.000377996,'m^3/(mol*s)'), n=3.50982, w0=(353.5,'kJ/mol'), E0=(152.625,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-4CClO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-4CClO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-4CClO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-4CClO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 139,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(0.454433,'m^3/(mol*s)'), n=2.6531, w0=(353.5,'kJ/mol'), E0=(135.1,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.001894442906887018, var=0.07687488622111935, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 0.560599184503651"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 0.560599184503651""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 0.560599184503651
""",
)

entry(
    index = 140,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1",
    kinetics = ArrheniusBM(A=(0.293027,'m^3/(mol*s)'), n=2.5626, w0=(353.5,'kJ/mol'), E0=(108.124,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 141,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_N-3O-u1",
    kinetics = ArrheniusBM(A=(9.83389e-05,'m^3/(mol*s)'), n=3.69437, w0=(353.5,'kJ/mol'), E0=(224.944,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 142,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(198486,'m^3/(mol*s)'), n=1.14409, w0=(353.5,'kJ/mol'), E0=(89.6195,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.669021281514281, var=54.48941672835009, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 24.016988743122784"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 24.016988743122784""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 24.016988743122784
""",
)

entry(
    index = 143,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1",
    kinetics = ArrheniusBM(A=(0.00168156,'m^3/(mol*s)'), n=3.00925, w0=(353.5,'kJ/mol'), E0=(94.0774,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0216538156505004, var=0.38767117408136725, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1
    Total Standard Deviation in ln(k): 1.3026196949485842"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1
Total Standard Deviation in ln(k): 1.3026196949485842""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1
Total Standard Deviation in ln(k): 1.3026196949485842
""",
)

entry(
    index = 144,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_N-3O-u1",
    kinetics = ArrheniusBM(A=(4.25251e-05,'m^3/(mol*s)'), n=3.86124, w0=(353.5,'kJ/mol'), E0=(105.743,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 145,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_Ext-1BrCClFHINPSSi-R_5R!H->C",
    kinetics = ArrheniusBM(A=(0.0258927,'m^3/(mol*s)'), n=2.65481, w0=(353.5,'kJ/mol'), E0=(91.7276,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_Ext-1BrCClFHINPSSi-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_Ext-1BrCClFHINPSSi-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_Ext-1BrCClFHINPSSi-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_Ext-1BrCClFHINPSSi-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 146,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_Ext-1BrCClFHINPSSi-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(2.98958e+12,'m^3/(mol*s)'), n=-1.30667, w0=(353.5,'kJ/mol'), E0=(71.1161,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_Ext-1BrCClFHINPSSi-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_Ext-1BrCClFHINPSSi-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_Ext-1BrCClFHINPSSi-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_Ext-1BrCClFHINPSSi-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 147,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R_N-4R!H->O_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.145146,'m^3/(mol*s)'), n=2.24269, w0=(320,'kJ/mol'), E0=(93.0242,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R_N-4R!H->O_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R_N-4R!H->O_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R_N-4R!H->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C_Ext-3C-R_Ext-3C-R_N-4R!H->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 148,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->F_1CClH->C_Ext-1C-R_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(337.847,'m^3/(mol*s)'), n=1.89564, w0=(320,'kJ/mol'), E0=(88.1337,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->F_1CClH->C_Ext-1C-R_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->F_1CClH->C_Ext-1C-R_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->F_1CClH->C_Ext-1C-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->F_1CClH->C_Ext-1C-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 149,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->F_1CClH->C_Ext-1C-R_Ext-1C-R_4R!H->O",
    kinetics = ArrheniusBM(A=(3.62281,'m^3/(mol*s)'), n=2.36756, w0=(320,'kJ/mol'), E0=(88.3061,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->F_1CClH->C_Ext-1C-R_Ext-1C-R_4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->F_1CClH->C_Ext-1C-R_Ext-1C-R_4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->F_1CClH->C_Ext-1C-R_Ext-1C-R_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->F_1CClH->C_Ext-1C-R_Ext-1C-R_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 150,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->F_1CClH->C_Ext-1C-R_Ext-1C-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(331.421,'m^3/(mol*s)'), n=1.92127, w0=(320,'kJ/mol'), E0=(80.5534,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->F_1CClH->C_Ext-1C-R_Ext-1C-R_N-4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->F_1CClH->C_Ext-1C-R_Ext-1C-R_N-4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->F_1CClH->C_Ext-1C-R_Ext-1C-R_N-4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->F_1CClH->C_Ext-1C-R_Ext-1C-R_N-4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 151,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F",
    kinetics = ArrheniusBM(A=(4.99909e-20,'m^3/(mol*s)'), n=7.84487, w0=(525,'kJ/mol'), E0=(118.039,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.31834942678035844, var=1.1268158352807045, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F
    Total Standard Deviation in ln(k): 2.9279309303883942"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F
Total Standard Deviation in ln(k): 2.9279309303883942""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F
Total Standard Deviation in ln(k): 2.9279309303883942
""",
)

entry(
    index = 152,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F",
    kinetics = ArrheniusBM(A=(1.86351e-15,'m^3/(mol*s)'), n=6.60208, w0=(525,'kJ/mol'), E0=(130.188,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.18791149516056707, var=2.9243880961799387, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F
    Total Standard Deviation in ln(k): 3.9004052894360886"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F
Total Standard Deviation in ln(k): 3.9004052894360886""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F
Total Standard Deviation in ln(k): 3.9004052894360886
""",
)

entry(
    index = 153,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(9.42402e-07,'m^3/(mol*s)'), n=3.77581, w0=(485,'kJ/mol'), E0=(179.648,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.014576587959134218, var=3.2820665453679188, Tref=1000.0, N=56, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R',), comment="""BM rule fitted to 56 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R
    Total Standard Deviation in ln(k): 3.668497818205738"""),
    rank = 11,
    shortDesc = """BM rule fitted to 56 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.668497818205738""",
    longDesc = 
"""
BM rule fitted to 56 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.668497818205738
""",
)

entry(
    index = 154,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_Sp-4R!H=3CCClCl",
    kinetics = ArrheniusBM(A=(4.97708e-05,'m^3/(mol*s)'), n=3.41316, w0=(485,'kJ/mol'), E0=(181.191,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2740281621639529, var=0.960841089372717, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_Sp-4R!H=3CCClCl',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_Sp-4R!H=3CCClCl
    Total Standard Deviation in ln(k): 2.653604451122851"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_Sp-4R!H=3CCClCl
Total Standard Deviation in ln(k): 2.653604451122851""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_Sp-4R!H=3CCClCl
Total Standard Deviation in ln(k): 2.653604451122851
""",
)

entry(
    index = 155,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl",
    kinetics = ArrheniusBM(A=(1.04396e-05,'m^3/(mol*s)'), n=3.41775, w0=(485,'kJ/mol'), E0=(178.695,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.23338911014725236, var=0.33630971388662706, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl
    Total Standard Deviation in ln(k): 1.7489950995253618"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl
Total Standard Deviation in ln(k): 1.7489950995253618""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl
Total Standard Deviation in ln(k): 1.7489950995253618
""",
)

entry(
    index = 156,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_3CCl->Cl",
    kinetics = ArrheniusBM(A=(794.677,'m^3/(mol*s)'), n=1.14596, w0=(407.77,'kJ/mol'), E0=(123.402,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_3CCl->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_3CCl->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_3CCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_3CCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 157,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl",
    kinetics = ArrheniusBM(A=(1.96701e-20,'m^3/(mol*s)'), n=7.36202, w0=(525,'kJ/mol'), E0=(126.058,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.48467556409445955, var=4.80578081768734, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl
    Total Standard Deviation in ln(k): 5.6125763153650885"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl
Total Standard Deviation in ln(k): 5.6125763153650885""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl
Total Standard Deviation in ln(k): 5.6125763153650885
""",
)

entry(
    index = 158,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1_Ext-3CCl-R_Ext-3CCl-R_4R!H->O",
    kinetics = ArrheniusBM(A=(7.83906e-10,'m^3/(mol*s)'), n=5.14485, w0=(485,'kJ/mol'), E0=(139.646,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06543906391629187, var=0.010784333405798029, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1_Ext-3CCl-R_Ext-3CCl-R_4R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1_Ext-3CCl-R_Ext-3CCl-R_4R!H->O
    Total Standard Deviation in ln(k): 0.3726067755457056"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1_Ext-3CCl-R_Ext-3CCl-R_4R!H->O
Total Standard Deviation in ln(k): 0.3726067755457056""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1_Ext-3CCl-R_Ext-3CCl-R_4R!H->O
Total Standard Deviation in ln(k): 0.3726067755457056
""",
)

entry(
    index = 159,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1_Ext-3CCl-R_Ext-3CCl-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(8.68377e-05,'m^3/(mol*s)'), n=3.62888, w0=(485,'kJ/mol'), E0=(152.865,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1_Ext-3CCl-R_Ext-3CCl-R_N-4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1_Ext-3CCl-R_Ext-3CCl-R_N-4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1_Ext-3CCl-R_Ext-3CCl-R_N-4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1_Ext-3CCl-R_Ext-3CCl-R_N-4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 160,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1_Ext-3CCl-R_Sp-4R!H-3CCl_4R!H->C",
    kinetics = ArrheniusBM(A=(2.08267e-06,'m^3/(mol*s)'), n=3.44277, w0=(485,'kJ/mol'), E0=(172.692,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1_Ext-3CCl-R_Sp-4R!H-3CCl_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1_Ext-3CCl-R_Sp-4R!H-3CCl_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1_Ext-3CCl-R_Sp-4R!H-3CCl_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1_Ext-3CCl-R_Sp-4R!H-3CCl_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 161,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1_Ext-3CCl-R_Sp-4R!H-3CCl_N-4R!H->C",
    kinetics = ArrheniusBM(A=(4.03653e-08,'m^3/(mol*s)'), n=4.6553, w0=(485,'kJ/mol'), E0=(175.804,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1_Ext-3CCl-R_Sp-4R!H-3CCl_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1_Ext-3CCl-R_Sp-4R!H-3CCl_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1_Ext-3CCl-R_Sp-4R!H-3CCl_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1_Ext-3CCl-R_Sp-4R!H-3CCl_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 162,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-4BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(8.83229e-06,'m^3/(mol*s)'), n=3.59735, w0=(353.5,'kJ/mol'), E0=(117.975,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-4BrCFINOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-4BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 163,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-1O-R",
    kinetics = ArrheniusBM(A=(2.62839e-06,'m^3/(mol*s)'), n=3.30957, w0=(353.5,'kJ/mol'), E0=(87.9188,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7680594107793325, var=0.506894661214793, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-1O-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-1O-R
    Total Standard Deviation in ln(k): 3.3570994278276993"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-1O-R
Total Standard Deviation in ln(k): 3.3570994278276993""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-1O-R
Total Standard Deviation in ln(k): 3.3570994278276993
""",
)

entry(
    index = 164,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.5017e-06,'m^3/(mol*s)'), n=3.68796, w0=(353.5,'kJ/mol'), E0=(71.2531,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.41255200745776727, var=13.999320422827976, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C',), comment="""BM rule fitted to 7 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 8.537412586813376"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 8.537412586813376""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 8.537412586813376
""",
)

entry(
    index = 165,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.000653036,'m^3/(mol*s)'), n=2.92536, w0=(353.5,'kJ/mol'), E0=(109.903,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0272736281605613, var=0.4206990194107873, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C',), comment="""BM rule fitted to 9 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 1.3688242390199368"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 1.3688242390199368""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 1.3688242390199368
""",
)

entry(
    index = 166,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.07246e-05,'m^3/(mol*s)'), n=3.56773, w0=(353.5,'kJ/mol'), E0=(105.004,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.0442219949691744, var=7.113647583797912, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 10.483149718850274"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 10.483149718850274""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 10.483149718850274
""",
)

entry(
    index = 167,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(7.08191e-06,'m^3/(mol*s)'), n=3.53568, w0=(353.5,'kJ/mol'), E0=(71.9608,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.22879857032810358, var=1.8815384174228167, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C',), comment="""BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 3.3247494635322137"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 3.3247494635322137""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 3.3247494635322137
""",
)

entry(
    index = 168,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_5R!H->C_Ext-1O-R",
    kinetics = ArrheniusBM(A=(1.1312e+08,'m^3/(mol*s)'), n=-0.0669897, w0=(353.5,'kJ/mol'), E0=(81.6653,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_5R!H->C_Ext-1O-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_5R!H->C_Ext-1O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_5R!H->C_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_5R!H->C_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 169,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_4CF->F_Ext-3CClFH-R_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(0.000214,'m^3/(mol*s)'), n=2.82, w0=(353.5,'kJ/mol'), E0=(150.59,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_4CF->F_Ext-3CClFH-R_Ext-3CClFH-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_4CF->F_Ext-3CClFH-R_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_4CF->F_Ext-3CClFH-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_4CF->F_Ext-3CClFH-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 170,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_4CF->F_Ext-3CClFH-R_5R!H->F",
    kinetics = ArrheniusBM(A=(0.000591,'m^3/(mol*s)'), n=2.76, w0=(353.5,'kJ/mol'), E0=(139.294,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_4CF->F_Ext-3CClFH-R_5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_4CF->F_Ext-3CClFH-R_5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_4CF->F_Ext-3CClFH-R_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_4CF->F_Ext-3CClFH-R_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 171,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_4CF->F_Ext-3CClFH-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(0.000778,'m^3/(mol*s)'), n=2.78, w0=(353.5,'kJ/mol'), E0=(150.855,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_4CF->F_Ext-3CClFH-R_N-5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_4CF->F_Ext-3CClFH-R_N-5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_4CF->F_Ext-3CClFH-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_4CF->F_Ext-3CClFH-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 172,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_4R!H->C_Ext-1C-R_5R!H->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(1.37515e-06,'m^3/(mol*s)'), n=3.75034, w0=(353.5,'kJ/mol'), E0=(86.9747,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_4R!H->C_Ext-1C-R_5R!H->C_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_4R!H->C_Ext-1C-R_5R!H->C_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_4R!H->C_Ext-1C-R_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_4R!H->C_Ext-1C-R_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 173,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_Sp-5R!H=1C_5R!H->C",
    kinetics = ArrheniusBM(A=(4.61853e-05,'m^3/(mol*s)'), n=3.71313, w0=(353.5,'kJ/mol'), E0=(141.91,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5338166302884035, var=0.018703501560795355, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_Sp-5R!H=1C_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_Sp-5R!H=1C_5R!H->C
    Total Standard Deviation in ln(k): 1.6154168788837857"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_Sp-5R!H=1C_5R!H->C
Total Standard Deviation in ln(k): 1.6154168788837857""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_Sp-5R!H=1C_5R!H->C
Total Standard Deviation in ln(k): 1.6154168788837857
""",
)

entry(
    index = 174,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_Sp-5R!H=1C_N-5R!H->C",
    kinetics = ArrheniusBM(A=(8.94345e-06,'m^3/(mol*s)'), n=3.73749, w0=(353.5,'kJ/mol'), E0=(81.2931,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.15322818487298656, var=0.6815218607347818, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_Sp-5R!H=1C_N-5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_Sp-5R!H=1C_N-5R!H->C
    Total Standard Deviation in ln(k): 2.039991197179844"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_Sp-5R!H=1C_N-5R!H->C
Total Standard Deviation in ln(k): 2.039991197179844""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_Sp-5R!H=1C_N-5R!H->C
Total Standard Deviation in ln(k): 2.039991197179844
""",
)

entry(
    index = 175,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_N-Sp-5R!H=1C_4FO->F",
    kinetics = ArrheniusBM(A=(0.51368,'m^3/(mol*s)'), n=2.50464, w0=(353.5,'kJ/mol'), E0=(110.869,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.028192741787463914, var=0.3463742622302057, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_N-Sp-5R!H=1C_4FO->F',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_N-Sp-5R!H=1C_4FO->F
    Total Standard Deviation in ln(k): 1.250694183200232"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_N-Sp-5R!H=1C_4FO->F
Total Standard Deviation in ln(k): 1.250694183200232""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_N-Sp-5R!H=1C_4FO->F
Total Standard Deviation in ln(k): 1.250694183200232
""",
)

entry(
    index = 176,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_N-Sp-5R!H=1C_N-4FO->F",
    kinetics = ArrheniusBM(A=(0.00523765,'m^3/(mol*s)'), n=2.97537, w0=(353.5,'kJ/mol'), E0=(94.6013,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.625692345683569, var=12.437155803732226, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_N-Sp-5R!H=1C_N-4FO->F',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_N-Sp-5R!H=1C_N-4FO->F
    Total Standard Deviation in ln(k): 13.667186230998006"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_N-Sp-5R!H=1C_N-4FO->F
Total Standard Deviation in ln(k): 13.667186230998006""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_N-Sp-5R!H=1C_N-4FO->F
Total Standard Deviation in ln(k): 13.667186230998006
""",
)

entry(
    index = 177,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_5R!H->O_3O-u1",
    kinetics = ArrheniusBM(A=(4.84958,'m^3/(mol*s)'), n=2.26492, w0=(353.5,'kJ/mol'), E0=(126.301,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_5R!H->O_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_5R!H->O_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_5R!H->O_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_5R!H->O_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 178,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_5R!H->O_N-3O-u1",
    kinetics = ArrheniusBM(A=(0.00160312,'m^3/(mol*s)'), n=3.40668, w0=(353.5,'kJ/mol'), E0=(147.531,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_5R!H->O_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_5R!H->O_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_5R!H->O_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_5R!H->O_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 179,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(608569,'m^3/(mol*s)'), n=0.929655, w0=(353.5,'kJ/mol'), E0=(153.48,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3910721621197293, var=18.817356533764162, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 9.678929071543935"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 9.678929071543935""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 9.678929071543935
""",
)

entry(
    index = 180,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_3O-u1",
    kinetics = ArrheniusBM(A=(4.39416,'m^3/(mol*s)'), n=2.31879, w0=(353.5,'kJ/mol'), E0=(117.73,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 181,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_N-3O-u1",
    kinetics = ArrheniusBM(A=(0.00157708,'m^3/(mol*s)'), n=3.46056, w0=(353.5,'kJ/mol'), E0=(135.202,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 182,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_3O-u1",
    kinetics = ArrheniusBM(A=(0.0379121,'m^3/(mol*s)'), n=2.90824, w0=(353.5,'kJ/mol'), E0=(126.106,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 183,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-3O-u1",
    kinetics = ArrheniusBM(A=(7.30096,'m^3/(mol*s)'), n=2.36151, w0=(353.5,'kJ/mol'), E0=(143.793,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 184,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_4CClO->C",
    kinetics = ArrheniusBM(A=(737.893,'m^3/(mol*s)'), n=1.8413, w0=(353.5,'kJ/mol'), E0=(72.5651,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.069608233712642, var=16.36662688363046, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_4CClO->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_4CClO->C
    Total Standard Deviation in ln(k): 13.310314361186922"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_4CClO->C
Total Standard Deviation in ln(k): 13.310314361186922""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_4CClO->C
Total Standard Deviation in ln(k): 13.310314361186922
""",
)

entry(
    index = 185,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-4CClO->C",
    kinetics = ArrheniusBM(A=(0.0308105,'m^3/(mol*s)'), n=2.88761, w0=(353.5,'kJ/mol'), E0=(141.13,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-4CClO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-4CClO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-4CClO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-4CClO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 186,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_4CClO->Cl",
    kinetics = ArrheniusBM(A=(0.00381903,'m^3/(mol*s)'), n=3.24993, w0=(353.5,'kJ/mol'), E0=(137.265,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_4CClO->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_4CClO->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_4CClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_4CClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 187,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl",
    kinetics = ArrheniusBM(A=(0.00139606,'m^3/(mol*s)'), n=3.03068, w0=(353.5,'kJ/mol'), E0=(93.4452,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.24036167192443, var=0.3747267519497552, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl
    Total Standard Deviation in ln(k): 1.831120950945008"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl
Total Standard Deviation in ln(k): 1.831120950945008""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl
Total Standard Deviation in ln(k): 1.831120950945008
""",
)

entry(
    index = 188,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6.24816e-11,'m^3/(mol*s)'), n=5.26333, w0=(525,'kJ/mol'), E0=(144.391,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.31900200383844896, var=2.270533501249724, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R
    Total Standard Deviation in ln(k): 3.8223054352599286"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R
Total Standard Deviation in ln(k): 3.8223054352599286""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R
Total Standard Deviation in ln(k): 3.8223054352599286
""",
)

entry(
    index = 189,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C",
    kinetics = ArrheniusBM(A=(2.96435e-18,'m^3/(mol*s)'), n=7.56751, w0=(525,'kJ/mol'), E0=(130.195,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4349754859510323, var=0.04448227865617492, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C
    Total Standard Deviation in ln(k): 1.5157183443960391"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C
Total Standard Deviation in ln(k): 1.5157183443960391""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C
Total Standard Deviation in ln(k): 1.5157183443960391
""",
)

entry(
    index = 190,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C",
    kinetics = ArrheniusBM(A=(3.87435e-14,'m^3/(mol*s)'), n=6.17703, w0=(525,'kJ/mol'), E0=(131.492,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.15174787894526534, var=4.6611662935599245, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C
    Total Standard Deviation in ln(k): 4.709445854301914"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C
Total Standard Deviation in ln(k): 4.709445854301914""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C
Total Standard Deviation in ln(k): 4.709445854301914
""",
)

entry(
    index = 191,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0",
    kinetics = ArrheniusBM(A=(8.64116e-07,'m^3/(mol*s)'), n=3.78655, w0=(485,'kJ/mol'), E0=(179.584,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.013163617278834092, var=3.2673803958764562, Tref=1000.0, N=50, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0',), comment="""BM rule fitted to 50 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0
    Total Standard Deviation in ln(k): 3.656812821602809"""),
    rank = 11,
    shortDesc = """BM rule fitted to 50 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0
Total Standard Deviation in ln(k): 3.656812821602809""",
    longDesc = 
"""
BM rule fitted to 50 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0
Total Standard Deviation in ln(k): 3.656812821602809
""",
)

entry(
    index = 192,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_N-1C-u0",
    kinetics = ArrheniusBM(A=(226.686,'m^3/(mol*s)'), n=1.41927, w0=(485,'kJ/mol'), E0=(172.862,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.476202477337676, var=9.700063949958636, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_N-1C-u0',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_N-1C-u0
    Total Standard Deviation in ln(k): 7.440221133894459"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_N-1C-u0
Total Standard Deviation in ln(k): 7.440221133894459""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_N-1C-u0
Total Standard Deviation in ln(k): 7.440221133894459
""",
)

entry(
    index = 193,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_Sp-4R!H=3CCClCl_Ext-3CCl-R",
    kinetics = ArrheniusBM(A=(6.8148e-05,'m^3/(mol*s)'), n=3.38383, w0=(485,'kJ/mol'), E0=(179.393,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.2149616755423855, var=2.1237975861441836, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_Sp-4R!H=3CCClCl_Ext-3CCl-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_Sp-4R!H=3CCClCl_Ext-3CCl-R
    Total Standard Deviation in ln(k): 5.974219057081788"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_Sp-4R!H=3CCClCl_Ext-3CCl-R
Total Standard Deviation in ln(k): 5.974219057081788""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_Sp-4R!H=3CCClCl_Ext-3CCl-R
Total Standard Deviation in ln(k): 5.974219057081788
""",
)

entry(
    index = 194,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_Sp-4R!H=3CCClCl_4R!H->C",
    kinetics = ArrheniusBM(A=(3.70857e-08,'m^3/(mol*s)'), n=4.36701, w0=(485,'kJ/mol'), E0=(179.598,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_Sp-4R!H=3CCClCl_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_Sp-4R!H=3CCClCl_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_Sp-4R!H=3CCClCl_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_Sp-4R!H=3CCClCl_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 195,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_Sp-4R!H=3CCClCl_N-4R!H->C",
    kinetics = ArrheniusBM(A=(3.95e-05,'m^3/(mol*s)'), n=3.43, w0=(485,'kJ/mol'), E0=(182.949,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_Sp-4R!H=3CCClCl_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_Sp-4R!H=3CCClCl_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_Sp-4R!H=3CCClCl_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_Sp-4R!H=3CCClCl_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 196,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_Ext-3CCl-R",
    kinetics = ArrheniusBM(A=(1.48449e-05,'m^3/(mol*s)'), n=3.39528, w0=(485,'kJ/mol'), E0=(181.012,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2840078072331988, var=0.783376808139735, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_Ext-3CCl-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_Ext-3CCl-R
    Total Standard Deviation in ln(k): 2.487949931258856"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_Ext-3CCl-R
Total Standard Deviation in ln(k): 2.487949931258856""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_Ext-3CCl-R
Total Standard Deviation in ln(k): 2.487949931258856
""",
)

entry(
    index = 197,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_4R!H->C",
    kinetics = ArrheniusBM(A=(2.26291e-08,'m^3/(mol*s)'), n=4.37484, w0=(485,'kJ/mol'), E0=(173.742,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.24436438432485788, var=0.014235358056973308, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_4R!H->C
    Total Standard Deviation in ln(k): 0.8531698562866517"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_4R!H->C
Total Standard Deviation in ln(k): 0.8531698562866517""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_4R!H->C
Total Standard Deviation in ln(k): 0.8531698562866517
""",
)

entry(
    index = 198,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_N-4R!H->C",
    kinetics = ArrheniusBM(A=(1.972e-05,'m^3/(mol*s)'), n=3.28397, w0=(485,'kJ/mol'), E0=(175.447,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.1309384567838423, var=3.7654530018551067, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_N-4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_N-4R!H->C
    Total Standard Deviation in ln(k): 6.731697260808422"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_N-4R!H->C
Total Standard Deviation in ln(k): 6.731697260808422""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_N-4R!H->C
Total Standard Deviation in ln(k): 6.731697260808422
""",
)

entry(
    index = 199,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R",
    kinetics = ArrheniusBM(A=(6.88515e-21,'m^3/(mol*s)'), n=7.49121, w0=(525,'kJ/mol'), E0=(125.251,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5045851005295108, var=4.772387119355364, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R
    Total Standard Deviation in ln(k): 5.647304696345808"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 5.647304696345808""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 5.647304696345808
""",
)

entry(
    index = 200,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1_Ext-3CCl-R_Ext-3CCl-R_4R!H->O_5R!H->C",
    kinetics = ArrheniusBM(A=(1.10332e-07,'m^3/(mol*s)'), n=4.39237, w0=(485,'kJ/mol'), E0=(138.074,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1_Ext-3CCl-R_Ext-3CCl-R_4R!H->O_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1_Ext-3CCl-R_Ext-3CCl-R_4R!H->O_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1_Ext-3CCl-R_Ext-3CCl-R_4R!H->O_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1_Ext-3CCl-R_Ext-3CCl-R_4R!H->O_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 201,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1_Ext-3CCl-R_Ext-3CCl-R_4R!H->O_N-5R!H->C",
    kinetics = ArrheniusBM(A=(4.88042e-12,'m^3/(mol*s)'), n=5.91377, w0=(485,'kJ/mol'), E0=(141.07,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1_Ext-3CCl-R_Ext-3CCl-R_4R!H->O_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1_Ext-3CCl-R_Ext-3CCl-R_4R!H->O_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1_Ext-3CCl-R_Ext-3CCl-R_4R!H->O_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_N-3CCl-u1_Ext-3CCl-R_Ext-3CCl-R_4R!H->O_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 202,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-1O-R_6R!H->C",
    kinetics = ArrheniusBM(A=(3.20903e-06,'m^3/(mol*s)'), n=3.28294, w0=(353.5,'kJ/mol'), E0=(88.1477,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-1O-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-1O-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-1O-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-1O-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 203,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-1O-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(0.000106385,'m^3/(mol*s)'), n=3.20001, w0=(353.5,'kJ/mol'), E0=(140.681,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-1O-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-1O-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-1O-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-1O-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 204,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(5.43645e-05,'m^3/(mol*s)'), n=3.30995, w0=(353.5,'kJ/mol'), E0=(55.5613,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.022278827196986203, var=14.297730926031129, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R',), comment="""BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 7.636349484692201"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R
Total Standard Deviation in ln(k): 7.636349484692201""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R
Total Standard Deviation in ln(k): 7.636349484692201
""",
)

entry(
    index = 205,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-1O-R",
    kinetics = ArrheniusBM(A=(0.000106567,'m^3/(mol*s)'), n=3.23582, w0=(353.5,'kJ/mol'), E0=(135.421,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-1O-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-1O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 206,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R",
    kinetics = ArrheniusBM(A=(5.62416e-08,'m^3/(mol*s)'), n=4.11181, w0=(353.5,'kJ/mol'), E0=(79.7488,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.07479334404006228, var=0.9564606426372354, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R
    Total Standard Deviation in ln(k): 2.148529941192914"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R
Total Standard Deviation in ln(k): 2.148529941192914""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R
Total Standard Deviation in ln(k): 2.148529941192914
""",
)

entry(
    index = 207,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F",
    kinetics = ArrheniusBM(A=(0.0008528,'m^3/(mol*s)'), n=2.86905, w0=(353.5,'kJ/mol'), E0=(110.115,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06865434019811986, var=0.3243580807999663, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F
    Total Standard Deviation in ln(k): 1.3142439522625955"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F
Total Standard Deviation in ln(k): 1.3142439522625955""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F
Total Standard Deviation in ln(k): 1.3142439522625955
""",
)

entry(
    index = 208,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_N-4FO->F",
    kinetics = ArrheniusBM(A=(0.000118485,'m^3/(mol*s)'), n=3.29853, w0=(353.5,'kJ/mol'), E0=(109.065,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_N-4FO->F',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_N-4FO->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_N-4FO->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_N-4FO->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 209,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-1O-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2.82278e-05,'m^3/(mol*s)'), n=3.44719, w0=(353.5,'kJ/mol'), E0=(107.142,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-1O-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-1O-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-1O-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-1O-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 210,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-1O-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.000485841,'m^3/(mol*s)'), n=3.11646, w0=(353.5,'kJ/mol'), E0=(147.641,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-1O-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-1O-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-1O-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-1O-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 211,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R",
    kinetics = ArrheniusBM(A=(0.000246125,'m^3/(mol*s)'), n=3.06199, w0=(353.5,'kJ/mol'), E0=(76.9034,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.14857082303703534, var=3.5988775584450927, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R
    Total Standard Deviation in ln(k): 4.176417869642315"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R
Total Standard Deviation in ln(k): 4.176417869642315""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R
Total Standard Deviation in ln(k): 4.176417869642315
""",
)

entry(
    index = 212,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_Sp-5R!H=1C_5R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(8.38302e-05,'m^3/(mol*s)'), n=3.60203, w0=(353.5,'kJ/mol'), E0=(138.734,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_Sp-5R!H=1C_5R!H->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_Sp-5R!H=1C_5R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_Sp-5R!H=1C_5R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_Sp-5R!H=1C_5R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 213,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_Sp-5R!H=1C_N-5R!H->C_4FO->F",
    kinetics = ArrheniusBM(A=(0.196785,'m^3/(mol*s)'), n=2.53703, w0=(353.5,'kJ/mol'), E0=(112.17,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.014132649901079262, var=1.8886909247224426, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_Sp-5R!H=1C_N-5R!H->C_4FO->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_Sp-5R!H=1C_N-5R!H->C_4FO->F
    Total Standard Deviation in ln(k): 2.7906096108725"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_Sp-5R!H=1C_N-5R!H->C_4FO->F
Total Standard Deviation in ln(k): 2.7906096108725""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_Sp-5R!H=1C_N-5R!H->C_4FO->F
Total Standard Deviation in ln(k): 2.7906096108725
""",
)

entry(
    index = 214,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_Sp-5R!H=1C_N-5R!H->C_N-4FO->F",
    kinetics = ArrheniusBM(A=(0.000215818,'m^3/(mol*s)'), n=3.25392, w0=(353.5,'kJ/mol'), E0=(87.4802,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_Sp-5R!H=1C_N-5R!H->C_N-4FO->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_Sp-5R!H=1C_N-5R!H->C_N-4FO->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_Sp-5R!H=1C_N-5R!H->C_N-4FO->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_Sp-5R!H=1C_N-5R!H->C_N-4FO->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 215,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_N-Sp-5R!H=1C_4FO->F_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.244874,'m^3/(mol*s)'), n=2.61206, w0=(353.5,'kJ/mol'), E0=(110.803,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.14565900478907443, var=0.7887472760890899, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_N-Sp-5R!H=1C_4FO->F_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_N-Sp-5R!H=1C_4FO->F_Ext-1C-R
    Total Standard Deviation in ln(k): 2.1464115893864313"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_N-Sp-5R!H=1C_4FO->F_Ext-1C-R
Total Standard Deviation in ln(k): 2.1464115893864313""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_N-Sp-5R!H=1C_4FO->F_Ext-1C-R
Total Standard Deviation in ln(k): 2.1464115893864313
""",
)

entry(
    index = 216,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_N-Sp-5R!H=1C_N-4FO->F_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.000541723,'m^3/(mol*s)'), n=3.2573, w0=(353.5,'kJ/mol'), E0=(85.3443,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_N-Sp-5R!H=1C_N-4FO->F_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_N-Sp-5R!H=1C_N-4FO->F_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_N-Sp-5R!H=1C_N-4FO->F_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_N-Sp-5R!H=1C_N-4FO->F_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 217,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_N-Sp-5R!H=1C_N-4FO->F_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(5.69582e-06,'m^3/(mol*s)'), n=3.94767, w0=(353.5,'kJ/mol'), E0=(138.068,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_N-Sp-5R!H=1C_N-4FO->F_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_N-Sp-5R!H=1C_N-4FO->F_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_N-Sp-5R!H=1C_N-4FO->F_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_N-Sp-5R!H=1C_N-4FO->F_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 218,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_N-Sp-5R!H=1C_N-4FO->F_5R!H->Cl",
    kinetics = ArrheniusBM(A=(6.65995e-06,'m^3/(mol*s)'), n=3.94804, w0=(353.5,'kJ/mol'), E0=(146.969,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_N-Sp-5R!H=1C_N-4FO->F_5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_N-Sp-5R!H=1C_N-4FO->F_5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_N-Sp-5R!H=1C_N-4FO->F_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_N-Sp-5R!H=1C_N-4FO->F_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 219,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_N-Sp-5R!H=1C_N-4FO->F_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(5.27349e-06,'m^3/(mol*s)'), n=3.9638, w0=(353.5,'kJ/mol'), E0=(132.925,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_N-Sp-5R!H=1C_N-4FO->F_N-5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_N-Sp-5R!H=1C_N-4FO->F_N-5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_N-Sp-5R!H=1C_N-4FO->F_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_N-Sp-5R!H=1C_N-4FO->F_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 220,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_Ext-1BrCClFHINPSSi-R_3O-u1",
    kinetics = ArrheniusBM(A=(34.915,'m^3/(mol*s)'), n=2.08375, w0=(353.5,'kJ/mol'), E0=(106.274,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_Ext-1BrCClFHINPSSi-R_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_Ext-1BrCClFHINPSSi-R_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_Ext-1BrCClFHINPSSi-R_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_Ext-1BrCClFHINPSSi-R_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 221,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_Ext-1BrCClFHINPSSi-R_N-3O-u1",
    kinetics = ArrheniusBM(A=(0.00549685,'m^3/(mol*s)'), n=3.29552, w0=(353.5,'kJ/mol'), E0=(147.196,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_Ext-1BrCClFHINPSSi-R_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_Ext-1BrCClFHINPSSi-R_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_Ext-1BrCClFHINPSSi-R_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_Ext-1BrCClFHINPSSi-R_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 222,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_4CClO->C_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(147.866,'m^3/(mol*s)'), n=2.04113, w0=(353.5,'kJ/mol'), E0=(69.632,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_4CClO->C_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_4CClO->C_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_4CClO->C_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_4CClO->C_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 223,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_Ext-4CO-R",
    kinetics = ArrheniusBM(A=(0.00211236,'m^3/(mol*s)'), n=3.19107, w0=(353.5,'kJ/mol'), E0=(120.015,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.14649321907291848, var=0.08544573799067014, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_Ext-4CO-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_Ext-4CO-R
    Total Standard Deviation in ln(k): 0.9540795891838858"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_Ext-4CO-R
Total Standard Deviation in ln(k): 0.9540795891838858""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_Ext-4CO-R
Total Standard Deviation in ln(k): 0.9540795891838858
""",
)

entry(
    index = 224,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_4CO->C",
    kinetics = ArrheniusBM(A=(0.00108931,'m^3/(mol*s)'), n=3.05784, w0=(353.5,'kJ/mol'), E0=(92.5778,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_4CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_4CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_4CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_4CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 225,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_N-4CO->C",
    kinetics = ArrheniusBM(A=(0.00678858,'m^3/(mol*s)'), n=3.1372, w0=(353.5,'kJ/mol'), E0=(110.664,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_N-4CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_N-4CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 226,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F",
    kinetics = ArrheniusBM(A=(1.5949e-12,'m^3/(mol*s)'), n=5.70937, w0=(525,'kJ/mol'), E0=(144.472,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.21166727828255652, var=0.4565258990841588, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F
    Total Standard Deviation in ln(k): 1.8863606741295094"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F
Total Standard Deviation in ln(k): 1.8863606741295094""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F
Total Standard Deviation in ln(k): 1.8863606741295094
""",
)

entry(
    index = 227,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(5.8602e-10,'m^3/(mol*s)'), n=4.99659, w0=(525,'kJ/mol'), E0=(142.2,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.9020005043715235, var=6.104076113325933, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F
    Total Standard Deviation in ln(k): 7.2193173192128635"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F
Total Standard Deviation in ln(k): 7.2193173192128635""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F
Total Standard Deviation in ln(k): 7.2193173192128635
""",
)

entry(
    index = 228,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.80067e-20,'m^3/(mol*s)'), n=8.17077, w0=(525,'kJ/mol'), E0=(126.077,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 229,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(5.18265e-09,'m^3/(mol*s)'), n=4.74784, w0=(525,'kJ/mol'), E0=(136.667,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 230,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(4.4871e-15,'m^3/(mol*s)'), n=6.43208, w0=(525,'kJ/mol'), E0=(131.746,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.14164862423309704, var=6.363823580874183, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 5.413170071534778"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 5.413170071534778""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 5.413170071534778
""",
)

entry(
    index = 231,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.4072e-05,'m^3/(mol*s)'), n=3.45455, w0=(485,'kJ/mol'), E0=(188.572,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0985724558137202, var=6.0960489654238526, Tref=1000.0, N=24, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R',), comment="""BM rule fitted to 24 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R
    Total Standard Deviation in ln(k): 5.197396105233193"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 5.197396105233193""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 5.197396105233193
""",
)

entry(
    index = 232,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(7.98998e-08,'m^3/(mol*s)'), n=4.06507, w0=(485,'kJ/mol'), E0=(170.994,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0628102702633848, var=0.5772292955492786, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C',), comment="""BM rule fitted to 21 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C
    Total Standard Deviation in ln(k): 1.680924405925733"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C
Total Standard Deviation in ln(k): 1.680924405925733""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C
Total Standard Deviation in ln(k): 1.680924405925733
""",
)

entry(
    index = 233,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(6.93639e-07,'m^3/(mol*s)'), n=3.84128, w0=(485,'kJ/mol'), E0=(181.27,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17614469304775013, var=1.308476701639213, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C
    Total Standard Deviation in ln(k): 2.7357643269006675"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 2.7357643269006675""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 2.7357643269006675
""",
)

entry(
    index = 234,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(86.3197,'m^3/(mol*s)'), n=1.5824, w0=(485,'kJ/mol'), E0=(174.861,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4039562151170453, var=13.200382787736764, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C
    Total Standard Deviation in ln(k): 8.298635212481031"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C
Total Standard Deviation in ln(k): 8.298635212481031""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C
Total Standard Deviation in ln(k): 8.298635212481031
""",
)

entry(
    index = 235,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_N-1C-u0_N-Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(1.28573e-06,'m^3/(mol*s)'), n=3.56699, w0=(485,'kJ/mol'), E0=(129.946,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_N-1C-u0_N-Sp-4R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_N-1C-u0_N-Sp-4R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_N-1C-u0_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_N-1C-u0_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 236,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_Sp-4R!H=3CCClCl_Ext-3CCl-R_4R!H->C",
    kinetics = ArrheniusBM(A=(4.362e-07,'m^3/(mol*s)'), n=3.96684, w0=(485,'kJ/mol'), E0=(178.635,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_Sp-4R!H=3CCClCl_Ext-3CCl-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_Sp-4R!H=3CCClCl_Ext-3CCl-R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_Sp-4R!H=3CCClCl_Ext-3CCl-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_Sp-4R!H=3CCClCl_Ext-3CCl-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 237,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_Sp-4R!H=3CCClCl_Ext-3CCl-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(8.35e-05,'m^3/(mol*s)'), n=3.36, w0=(485,'kJ/mol'), E0=(179.463,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_Sp-4R!H=3CCClCl_Ext-3CCl-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_Sp-4R!H=3CCClCl_Ext-3CCl-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_Sp-4R!H=3CCClCl_Ext-3CCl-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_Sp-4R!H=3CCClCl_Ext-3CCl-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 238,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_Ext-3CCl-R_Ext-3CCl-R",
    kinetics = ArrheniusBM(A=(3.34e-05,'m^3/(mol*s)'), n=3.35, w0=(485,'kJ/mol'), E0=(183.315,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_Ext-3CCl-R_Ext-3CCl-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_Ext-3CCl-R_Ext-3CCl-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_Ext-3CCl-R_Ext-3CCl-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_Ext-3CCl-R_Ext-3CCl-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 239,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_Ext-3CCl-R_4R!H->C",
    kinetics = ArrheniusBM(A=(6.36303e-10,'m^3/(mol*s)'), n=4.82658, w0=(485,'kJ/mol'), E0=(166.608,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4745848157928954, var=0.005426392301841526, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_Ext-3CCl-R_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_Ext-3CCl-R_4R!H->C
    Total Standard Deviation in ln(k): 1.34010106579823"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_Ext-3CCl-R_4R!H->C
Total Standard Deviation in ln(k): 1.34010106579823""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_Ext-3CCl-R_4R!H->C
Total Standard Deviation in ln(k): 1.34010106579823
""",
)

entry(
    index = 240,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_Ext-3CCl-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(1.35e-05,'m^3/(mol*s)'), n=3.34, w0=(485,'kJ/mol'), E0=(179.728,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_Ext-3CCl-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_Ext-3CCl-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_Ext-3CCl-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_Ext-3CCl-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 241,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_4R!H->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(2.894e-08,'m^3/(mol*s)'), n=4.35365, w0=(485,'kJ/mol'), E0=(174.899,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_4R!H->C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_4R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 242,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_N-4R!H->C_4FO->F",
    kinetics = ArrheniusBM(A=(2.43e-05,'m^3/(mol*s)'), n=3.25, w0=(485,'kJ/mol'), E0=(175.575,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_N-4R!H->C_4FO->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_N-4R!H->C_4FO->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_N-4R!H->C_4FO->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_N-4R!H->C_4FO->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 243,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_N-4R!H->C_N-4FO->F",
    kinetics = ArrheniusBM(A=(7.33269e-08,'m^3/(mol*s)'), n=4.23045, w0=(485,'kJ/mol'), E0=(172.474,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_N-4R!H->C_N-4FO->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_N-4R!H->C_N-4FO->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_N-4R!H->C_N-4FO->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_N-4R!H->C_N-4FO->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 244,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(5.41648e-16,'m^3/(mol*s)'), n=5.96378, w0=(525,'kJ/mol'), E0=(145.654,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4805865621710167, var=0.07428163186732142, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_4R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_4R!H->Cl
    Total Standard Deviation in ln(k): 1.7538875906560576"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_4R!H->Cl
Total Standard Deviation in ln(k): 1.7538875906560576""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_4R!H->Cl
Total Standard Deviation in ln(k): 1.7538875906560576
""",
)

entry(
    index = 245,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(7.45019e-18,'m^3/(mol*s)'), n=6.65942, w0=(525,'kJ/mol'), E0=(130.663,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4035344065425317, var=5.1833895123470635, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 5.578097615842104"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 5.578097615842104""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 5.578097615842104
""",
)

entry(
    index = 246,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(0.000936334,'m^3/(mol*s)'), n=3.09886, w0=(353.5,'kJ/mol'), E0=(69.4048,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_Ext-3CClFH-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 247,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_Sp-5R!H-3CClFH",
    kinetics = ArrheniusBM(A=(3.84196e-06,'m^3/(mol*s)'), n=3.49798, w0=(353.5,'kJ/mol'), E0=(56.4557,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.5473357703331074, var=3.8825174269449745, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_Sp-5R!H-3CClFH',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_Sp-5R!H-3CClFH
    Total Standard Deviation in ln(k): 7.837929306881209"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_Sp-5R!H-3CClFH
Total Standard Deviation in ln(k): 7.837929306881209""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_Sp-5R!H-3CClFH
Total Standard Deviation in ln(k): 7.837929306881209
""",
)

entry(
    index = 248,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_N-Sp-5R!H-3CClFH",
    kinetics = ArrheniusBM(A=(8.83137e-13,'m^3/(mol*s)'), n=5.47481, w0=(353.5,'kJ/mol'), E0=(67.1992,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.10006927796601872, var=4.863381034621694, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_N-Sp-5R!H-3CClFH',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_N-Sp-5R!H-3CClFH
    Total Standard Deviation in ln(k): 4.672487587007515"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_N-Sp-5R!H-3CClFH
Total Standard Deviation in ln(k): 4.672487587007515""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_N-Sp-5R!H-3CClFH
Total Standard Deviation in ln(k): 4.672487587007515
""",
)

entry(
    index = 249,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(0.00021361,'m^3/(mol*s)'), n=3.08911, w0=(353.5,'kJ/mol'), E0=(112.188,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.014776873834088355, var=1.0648126974945902, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 2.105809178149278"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 2.105809178149278""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 2.105809178149278
""",
)

entry(
    index = 250,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(0.296927,'m^3/(mol*s)'), n=2.14524, w0=(353.5,'kJ/mol'), E0=(124.445,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00660417109202603, var=0.2118707644900309, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F_Ext-3CClFH-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 0.9393613537134735"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F_Ext-3CClFH-R
Total Standard Deviation in ln(k): 0.9393613537134735""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F_Ext-3CClFH-R
Total Standard Deviation in ln(k): 0.9393613537134735
""",
)

entry(
    index = 251,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_5R!H->O",
    kinetics = ArrheniusBM(A=(0.002697,'m^3/(mol*s)'), n=2.63489, w0=(353.5,'kJ/mol'), E0=(82.3497,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 252,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(0.02065,'m^3/(mol*s)'), n=2.64, w0=(353.5,'kJ/mol'), E0=(100.057,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_N-5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_N-5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 253,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_Sp-5R!H=1C_N-5R!H->C_4FO->F_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6.74008,'m^3/(mol*s)'), n=2.11936, w0=(353.5,'kJ/mol'), E0=(129.161,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_Sp-5R!H=1C_N-5R!H->C_4FO->F_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_Sp-5R!H=1C_N-5R!H->C_4FO->F_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_Sp-5R!H=1C_N-5R!H->C_4FO->F_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_Sp-5R!H=1C_N-5R!H->C_4FO->F_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 254,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_N-Sp-5R!H=1C_4FO->F_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(48.5444,'m^3/(mol*s)'), n=1.9582, w0=(353.5,'kJ/mol'), E0=(129.541,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_N-Sp-5R!H=1C_4FO->F_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_N-Sp-5R!H=1C_4FO->F_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_N-Sp-5R!H=1C_4FO->F_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_1BrCClFHINPSSi-u0_1BrCClFHINPSSi->C_N-4R!H->C_Ext-1C-R_N-Sp-5R!H=1C_4FO->F_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 255,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_Ext-4CO-R_Ext-4CO-R",
    kinetics = ArrheniusBM(A=(0.00185843,'m^3/(mol*s)'), n=3.22261, w0=(353.5,'kJ/mol'), E0=(119.68,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_Ext-4CO-R_Ext-4CO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_Ext-4CO-R_Ext-4CO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_Ext-4CO-R_Ext-4CO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_Ext-4CO-R_Ext-4CO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 256,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.67208e-13,'m^3/(mol*s)'), n=5.94049, w0=(525,'kJ/mol'), E0=(142.943,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.15516744737374857, var=1.5065365233189214, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R
    Total Standard Deviation in ln(k): 2.850500831981296"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R
Total Standard Deviation in ln(k): 2.850500831981296""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R
Total Standard Deviation in ln(k): 2.850500831981296
""",
)

entry(
    index = 257,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.84864e-10,'m^3/(mol*s)'), n=5.13872, w0=(525,'kJ/mol'), E0=(138.713,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 258,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(6.15e-07,'m^3/(mol*s)'), n=4.14, w0=(525,'kJ/mol'), E0=(163.675,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 259,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.71142e-12,'m^3/(mol*s)'), n=5.47558, w0=(525,'kJ/mol'), E0=(152.495,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 260,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C_4ClO->Cl",
    kinetics = ArrheniusBM(A=(3.57367e-11,'m^3/(mol*s)'), n=5.32561, w0=(525,'kJ/mol'), E0=(141.836,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C_4ClO->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C_4ClO->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C_4ClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C_4ClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 261,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C_N-4ClO->Cl",
    kinetics = ArrheniusBM(A=(3.31829e-08,'m^3/(mol*s)'), n=4.48236, w0=(525,'kJ/mol'), E0=(137.247,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C_N-4ClO->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C_N-4ClO->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C_N-4ClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C_N-4ClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 262,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(2.00179e-06,'m^3/(mol*s)'), n=3.59463, w0=(485,'kJ/mol'), E0=(184.963,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07127630849995228, var=7.212345980836135, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C
    Total Standard Deviation in ln(k): 5.56296488743793"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C
Total Standard Deviation in ln(k): 5.56296488743793""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C
Total Standard Deviation in ln(k): 5.56296488743793
""",
)

entry(
    index = 263,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.000112375,'m^3/(mol*s)'), n=3.34717, w0=(485,'kJ/mol'), E0=(193.047,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11649476807305856, var=6.542463448122908, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 5.420459851507813"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C
Total Standard Deviation in ln(k): 5.420459851507813""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C
Total Standard Deviation in ln(k): 5.420459851507813
""",
)

entry(
    index = 264,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F",
    kinetics = ArrheniusBM(A=(8.0722e-08,'m^3/(mol*s)'), n=4.09577, w0=(485,'kJ/mol'), E0=(171.561,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.16555178975853388, var=1.197265706866839, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F
    Total Standard Deviation in ln(k): 2.6095331250902634"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F
Total Standard Deviation in ln(k): 2.6095331250902634""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F
Total Standard Deviation in ln(k): 2.6095331250902634
""",
)

entry(
    index = 265,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F",
    kinetics = ArrheniusBM(A=(8.39474e-08,'m^3/(mol*s)'), n=4.02792, w0=(485,'kJ/mol'), E0=(170.508,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.028020092662087215, var=0.06812965528928436, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F
    Total Standard Deviation in ln(k): 0.59367133755393"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F
Total Standard Deviation in ln(k): 0.59367133755393""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F
Total Standard Deviation in ln(k): 0.59367133755393
""",
)

entry(
    index = 266,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_4R!H->C",
    kinetics = ArrheniusBM(A=(5.7299e-06,'m^3/(mol*s)'), n=3.76087, w0=(485,'kJ/mol'), E0=(180.492,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 267,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(6.7827e-07,'m^3/(mol*s)'), n=3.84344, w0=(485,'kJ/mol'), E0=(181.257,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18844180021896278, var=1.32438726038431, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C
    Total Standard Deviation in ln(k): 2.78056159374933"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C
Total Standard Deviation in ln(k): 2.78056159374933""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C
Total Standard Deviation in ln(k): 2.78056159374933
""",
)

entry(
    index = 268,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C",
    kinetics = ArrheniusBM(A=(18908.5,'m^3/(mol*s)'), n=0.81744, w0=(485,'kJ/mol'), E0=(176.149,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.513238060813226, var=34.9716148721854, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C
    Total Standard Deviation in ln(k): 13.144905231046868"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C
Total Standard Deviation in ln(k): 13.144905231046868""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C
Total Standard Deviation in ln(k): 13.144905231046868
""",
)

entry(
    index = 269,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.0158687,'m^3/(mol*s)'), n=2.79423, w0=(485,'kJ/mol'), E0=(172.35,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1575084340451707, var=8.568385324107215, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C
    Total Standard Deviation in ln(k): 6.263971138772223"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C
Total Standard Deviation in ln(k): 6.263971138772223""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C
Total Standard Deviation in ln(k): 6.263971138772223
""",
)

entry(
    index = 270,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_Ext-3CCl-R_4R!H->C_5R!H->C",
    kinetics = ArrheniusBM(A=(3.19591e-10,'m^3/(mol*s)'), n=4.92231, w0=(485,'kJ/mol'), E0=(166.297,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_Ext-3CCl-R_4R!H->C_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_Ext-3CCl-R_4R!H->C_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_Ext-3CCl-R_4R!H->C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_Ext-3CCl-R_4R!H->C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 271,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_Ext-3CCl-R_4R!H->C_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.29256e-09,'m^3/(mol*s)'), n=4.72835, w0=(485,'kJ/mol'), E0=(166.942,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_Ext-3CCl-R_4R!H->C_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_Ext-3CCl-R_4R!H->C_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_Ext-3CCl-R_4R!H->C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-3CCl-R_N-Sp-4R!H=3CCClCl_Ext-3CCl-R_4R!H->C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 272,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_4R!H->Cl_Ext-3C-R",
    kinetics = ArrheniusBM(A=(5.77469e-17,'m^3/(mol*s)'), n=6.35038, w0=(525,'kJ/mol'), E0=(151.207,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_4R!H->Cl_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_4R!H->Cl_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_4R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_4R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 273,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_Ext-3C-R",
    kinetics = ArrheniusBM(A=(4.19021e-17,'m^3/(mol*s)'), n=6.40104, w0=(525,'kJ/mol'), E0=(141.602,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5477830059097045, var=7.5875009089488445, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_Ext-3C-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_Ext-3C-R
    Total Standard Deviation in ln(k): 6.898465918081849"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 6.898465918081849""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 6.898465918081849
""",
)

entry(
    index = 274,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(4.34682e-12,'m^3/(mol*s)'), n=5.06266, w0=(525,'kJ/mol'), E0=(136.494,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_4BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 275,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(7.11402e-27,'m^3/(mol*s)'), n=9.28823, w0=(525,'kJ/mol'), E0=(97.2268,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.46172144012136523, var=0.5381798913485838, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 2.630792709852956"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 2.630792709852956""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 2.630792709852956
""",
)

entry(
    index = 276,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_Sp-5R!H-3CClFH_Ext-1O-R",
    kinetics = ArrheniusBM(A=(4.11983e-05,'m^3/(mol*s)'), n=3.20075, w0=(353.5,'kJ/mol'), E0=(86.0782,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_Sp-5R!H-3CClFH_Ext-1O-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_Sp-5R!H-3CClFH_Ext-1O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_Sp-5R!H-3CClFH_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_Sp-5R!H-3CClFH_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 277,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_N-Sp-5R!H-3CClFH_Ext-1O-R",
    kinetics = ArrheniusBM(A=(0.00425626,'m^3/(mol*s)'), n=2.65728, w0=(353.5,'kJ/mol'), E0=(143.351,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_N-Sp-5R!H-3CClFH_Ext-1O-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_N-Sp-5R!H-3CClFH_Ext-1O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_N-Sp-5R!H-3CClFH_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_N-Sp-5R!H-3CClFH_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 278,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(0.00442,'m^3/(mol*s)'), n=2.67, w0=(353.5,'kJ/mol'), E0=(124.691,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R_Ext-3CClFH-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 279,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R_6R!H->F",
    kinetics = ArrheniusBM(A=(0.00705,'m^3/(mol*s)'), n=2.66, w0=(353.5,'kJ/mol'), E0=(109.371,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R_6R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R_6R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R_6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R_6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 280,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R_N-6R!H->F",
    kinetics = ArrheniusBM(A=(0.00765,'m^3/(mol*s)'), n=2.68, w0=(353.5,'kJ/mol'), E0=(125.319,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R_N-6R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R_N-6R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R_N-6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R_N-6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 281,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F_Ext-3CClFH-R_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(0.00175,'m^3/(mol*s)'), n=2.74, w0=(353.5,'kJ/mol'), E0=(102.532,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F_Ext-3CClFH-R_Ext-3CClFH-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F_Ext-3CClFH-R_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F_Ext-3CClFH-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F_Ext-3CClFH-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 282,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F_Ext-3CClFH-R_5R!H->F",
    kinetics = ArrheniusBM(A=(0.00212,'m^3/(mol*s)'), n=2.75, w0=(353.5,'kJ/mol'), E0=(115.497,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F_Ext-3CClFH-R_5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F_Ext-3CClFH-R_5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F_Ext-3CClFH-R_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F_Ext-3CClFH-R_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 283,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F_Ext-3CClFH-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(0.00303,'m^3/(mol*s)'), n=2.77, w0=(353.5,'kJ/mol'), E0=(124.009,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F_Ext-3CClFH-R_N-5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F_Ext-3CClFH-R_N-5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F_Ext-3CClFH-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->F_Ext-3CClFH-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 284,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(1.77578e-14,'m^3/(mol*s)'), n=6.28933, w0=(525,'kJ/mol'), E0=(139.417,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 285,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(6.45e-07,'m^3/(mol*s)'), n=4.04, w0=(525,'kJ/mol'), E0=(162.45,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 286,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(2.58883e-06,'m^3/(mol*s)'), n=3.55742, w0=(485,'kJ/mol'), E0=(187.883,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.058908738351432434, var=7.3507010348261606, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 5.58328498982993"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 5.58328498982993""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 5.58328498982993
""",
)

entry(
    index = 287,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Sp-4C=1C",
    kinetics = ArrheniusBM(A=(2.5027e-05,'m^3/(mol*s)'), n=3.59925, w0=(485,'kJ/mol'), E0=(178.513,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Sp-4C=1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Sp-4C=1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Sp-4C=1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Sp-4C=1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 288,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C",
    kinetics = ArrheniusBM(A=(1.59331e-06,'m^3/(mol*s)'), n=3.65749, w0=(485,'kJ/mol'), E0=(166.464,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.181595671093109, var=7.03809268974634, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C
    Total Standard Deviation in ln(k): 10.799838807848376"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C
Total Standard Deviation in ln(k): 10.799838807848376""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C
Total Standard Deviation in ln(k): 10.799838807848376
""",
)

entry(
    index = 289,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O",
    kinetics = ArrheniusBM(A=(0.161782,'m^3/(mol*s)'), n=2.43248, w0=(485,'kJ/mol'), E0=(190.562,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2894535009314283, var=26.574338000377352, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O
    Total Standard Deviation in ln(k): 11.06174028820509"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O
Total Standard Deviation in ln(k): 11.06174028820509""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O
Total Standard Deviation in ln(k): 11.06174028820509
""",
)

entry(
    index = 290,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O",
    kinetics = ArrheniusBM(A=(7.52259e-05,'m^3/(mol*s)'), n=3.39773, w0=(485,'kJ/mol'), E0=(193.259,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09250277953740067, var=6.906895070230772, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O
    Total Standard Deviation in ln(k): 5.501057755436018"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O
Total Standard Deviation in ln(k): 5.501057755436018""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O
Total Standard Deviation in ln(k): 5.501057755436018
""",
)

entry(
    index = 291,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R",
    kinetics = ArrheniusBM(A=(6.17544e-08,'m^3/(mol*s)'), n=4.12767, w0=(485,'kJ/mol'), E0=(171.42,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17797988810844184, var=1.217229011632701, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R
    Total Standard Deviation in ln(k): 2.6589718118389447"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R
Total Standard Deviation in ln(k): 2.6589718118389447""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R
Total Standard Deviation in ln(k): 2.6589718118389447
""",
)

entry(
    index = 292,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R",
    kinetics = ArrheniusBM(A=(8.34353e-08,'m^3/(mol*s)'), n=4.02818, w0=(485,'kJ/mol'), E0=(170.502,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.026983944685405336, var=0.06263505290286348, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R
    Total Standard Deviation in ln(k): 0.5695238237214809"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R
Total Standard Deviation in ln(k): 0.5695238237214809""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R
Total Standard Deviation in ln(k): 0.5695238237214809
""",
)

entry(
    index = 293,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_4CO->C",
    kinetics = ArrheniusBM(A=(3.39606e-06,'m^3/(mol*s)'), n=3.8002, w0=(485,'kJ/mol'), E0=(174.472,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.24993611629262544, var=0.04764147309766436, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_4CO->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_4CO->C
    Total Standard Deviation in ln(k): 1.0655522483929907"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_4CO->C
Total Standard Deviation in ln(k): 1.0655522483929907""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_4CO->C
Total Standard Deviation in ln(k): 1.0655522483929907
""",
)

entry(
    index = 294,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_N-4CO->C",
    kinetics = ArrheniusBM(A=(5.29538e-06,'m^3/(mol*s)'), n=3.74, w0=(485,'kJ/mol'), E0=(173.466,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_N-4CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_N-4CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 295,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3CCl-R",
    kinetics = ArrheniusBM(A=(2.22395e-07,'m^3/(mol*s)'), n=3.97282, w0=(485,'kJ/mol'), E0=(180.817,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7406508044333014, var=2.8104200778925885, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3CCl-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3CCl-R
    Total Standard Deviation in ln(k): 5.221731209747573"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3CCl-R
Total Standard Deviation in ln(k): 5.221731209747573""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3CCl-R
Total Standard Deviation in ln(k): 5.221731209747573
""",
)

entry(
    index = 296,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.009208,'m^3/(mol*s)'), n=2.80941, w0=(485,'kJ/mol'), E0=(151.694,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.332656919811769, var=4.25485772067976, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 4.9710498891419785"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 4.9710498891419785""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 4.9710498891419785
""",
)

entry(
    index = 297,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.71639e-05,'m^3/(mol*s)'), n=3.56319, w0=(485,'kJ/mol'), E0=(152.498,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 298,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.05337e-19,'m^3/(mol*s)'), n=6.82518, w0=(525,'kJ/mol'), E0=(141.34,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7108375931197274, var=0.11413692146565324, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 2.463306934597187"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 2.463306934597187""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 2.463306934597187
""",
)

entry(
    index = 299,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.90827e-19,'m^3/(mol*s)'), n=7.22478, w0=(525,'kJ/mol'), E0=(132.114,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5082260822702707, var=0.5588172313796241, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 2.7755711971598522"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 2.7755711971598522""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 2.7755711971598522
""",
)

entry(
    index = 300,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(4.62502e-11,'m^3/(mol*s)'), n=4.57588, w0=(525,'kJ/mol'), E0=(159.198,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.43851301354750166, var=0.4877635602995544, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 2.501899905040801"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 2.501899905040801""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 2.501899905040801
""",
)

entry(
    index = 301,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_4FO->F",
    kinetics = ArrheniusBM(A=(2.67939e-44,'m^3/(mol*s)'), n=14.2981, w0=(525,'kJ/mol'), E0=(51.7829,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_4FO->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_4FO->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_4FO->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_4FO->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 302,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_N-4FO->F",
    kinetics = ArrheniusBM(A=(1.56246e-10,'m^3/(mol*s)'), n=4.59091, w0=(525,'kJ/mol'), E0=(139.657,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6830217334835639, var=0.5281442775779198, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_N-4FO->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_N-4FO->F
    Total Standard Deviation in ln(k): 3.173046868794559"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_N-4FO->F
Total Standard Deviation in ln(k): 3.173046868794559""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_N-4FO->F
Total Standard Deviation in ln(k): 3.173046868794559
""",
)

entry(
    index = 303,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_7R!H->C",
    kinetics = ArrheniusBM(A=(1.68723e-05,'m^3/(mol*s)'), n=2.95314, w0=(485,'kJ/mol'), E0=(193.721,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0030046029818384134, var=14.743691214756458, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_7R!H->C
    Total Standard Deviation in ln(k): 7.705233678445662"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_7R!H->C
Total Standard Deviation in ln(k): 7.705233678445662""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_7R!H->C
Total Standard Deviation in ln(k): 7.705233678445662
""",
)

entry(
    index = 304,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(8.96824e-07,'m^3/(mol*s)'), n=3.83775, w0=(485,'kJ/mol'), E0=(185.213,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07754259444220443, var=1.754056388859614, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_N-7R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_N-7R!H->C
    Total Standard Deviation in ln(k): 2.849917691374449"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_N-7R!H->C
Total Standard Deviation in ln(k): 2.849917691374449""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_N-7R!H->C
Total Standard Deviation in ln(k): 2.849917691374449
""",
)

entry(
    index = 305,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_Ext-3CCl-R",
    kinetics = ArrheniusBM(A=(1.5333e-06,'m^3/(mol*s)'), n=3.65941, w0=(485,'kJ/mol'), E0=(166.429,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_Ext-3CCl-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_Ext-3CCl-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_Ext-3CCl-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_Ext-3CCl-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 306,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_5R!H->C",
    kinetics = ArrheniusBM(A=(1.21333e-05,'m^3/(mol*s)'), n=3.66599, w0=(485,'kJ/mol'), E0=(168.262,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 307,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_N-5R!H->C",
    kinetics = ArrheniusBM(A=(3.38922e-05,'m^3/(mol*s)'), n=3.5758, w0=(485,'kJ/mol'), E0=(168.916,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 308,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O_Ext-3CCl-R",
    kinetics = ArrheniusBM(A=(0.00331206,'m^3/(mol*s)'), n=2.81802, w0=(485,'kJ/mol'), E0=(196.029,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O_Ext-3CCl-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O_Ext-3CCl-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O_Ext-3CCl-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O_Ext-3CCl-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 309,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R",
    kinetics = ArrheniusBM(A=(2.13872e-05,'m^3/(mol*s)'), n=3.55176, w0=(485,'kJ/mol'), E0=(193.142,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.027783525579027298, var=7.287454963942901, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R
    Total Standard Deviation in ln(k): 5.481647642096425"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R
Total Standard Deviation in ln(k): 5.481647642096425""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R
Total Standard Deviation in ln(k): 5.481647642096425
""",
)

entry(
    index = 310,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.839925,'m^3/(mol*s)'), n=2.36463, w0=(485,'kJ/mol'), E0=(184.976,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 311,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2.73445e-08,'m^3/(mol*s)'), n=4.20668, w0=(485,'kJ/mol'), E0=(169.253,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1699640488159558, var=1.181990833198972, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_5R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_5R!H->C
    Total Standard Deviation in ln(k): 2.6065813329923846"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_5R!H->C
Total Standard Deviation in ln(k): 2.6065813329923846""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_5R!H->C
Total Standard Deviation in ln(k): 2.6065813329923846
""",
)

entry(
    index = 312,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(7.84573e-07,'m^3/(mol*s)'), n=3.87954, w0=(485,'kJ/mol'), E0=(178.087,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.9426494161731698, var=6.57708312571278, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_N-5R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_N-5R!H->C
    Total Standard Deviation in ln(k): 7.509774259468916"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_N-5R!H->C
Total Standard Deviation in ln(k): 7.509774259468916""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_N-5R!H->C
Total Standard Deviation in ln(k): 7.509774259468916
""",
)

entry(
    index = 313,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_4CO->C",
    kinetics = ArrheniusBM(A=(1.00712e-07,'m^3/(mol*s)'), n=4.01588, w0=(485,'kJ/mol'), E0=(170.299,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.10014952334378734, var=0.022957014575159668, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_4CO->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_4CO->C
    Total Standard Deviation in ln(k): 0.5553808545883934"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_4CO->C
Total Standard Deviation in ln(k): 0.5553808545883934""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_4CO->C
Total Standard Deviation in ln(k): 0.5553808545883934
""",
)

entry(
    index = 314,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_N-4CO->C",
    kinetics = ArrheniusBM(A=(6.28297e-08,'m^3/(mol*s)'), n=4.04865, w0=(485,'kJ/mol'), E0=(170.739,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.07071074998058823, var=0.23643663099245127, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_N-4CO->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_N-4CO->C
    Total Standard Deviation in ln(k): 1.1524626199576522"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_N-4CO->C
Total Standard Deviation in ln(k): 1.1524626199576522""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_N-4CO->C
Total Standard Deviation in ln(k): 1.1524626199576522
""",
)

entry(
    index = 315,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_4CO->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(4.51365e-06,'m^3/(mol*s)'), n=3.78897, w0=(485,'kJ/mol'), E0=(175.572,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_4CO->C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_4CO->C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_4CO->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_4CO->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 316,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3CCl-R_Ext-3CCl-R",
    kinetics = ArrheniusBM(A=(3.63e-05,'m^3/(mol*s)'), n=3.37, w0=(485,'kJ/mol'), E0=(197.415,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3CCl-R_Ext-3CCl-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3CCl-R_Ext-3CCl-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3CCl-R_Ext-3CCl-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3CCl-R_Ext-3CCl-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 317,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3CCl-R_5R!H->F",
    kinetics = ArrheniusBM(A=(2.58576e-05,'m^3/(mol*s)'), n=3.2457, w0=(485,'kJ/mol'), E0=(186.26,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3CCl-R_5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3CCl-R_5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3CCl-R_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3CCl-R_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 318,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3CCl-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(3.56033e-08,'m^3/(mol*s)'), n=4.21745, w0=(485,'kJ/mol'), E0=(177.011,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3CCl-R_N-5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3CCl-R_N-5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3CCl-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->C_Ext-3CCl-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 319,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(4.47723e-05,'m^3/(mol*s)'), n=3.46134, w0=(485,'kJ/mol'), E0=(152.048,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 320,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(3.5032e-05,'m^3/(mol*s)'), n=3.5135, w0=(485,'kJ/mol'), E0=(138.997,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 321,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_Ext-3C-R_4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.25051e-20,'m^3/(mol*s)'), n=7.1754, w0=(525,'kJ/mol'), E0=(137.943,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_Ext-3C-R_4BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_Ext-3C-R_4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_Ext-3C-R_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_Ext-3C-R_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 322,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_Ext-3C-R_N-4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(3.10106e-12,'m^3/(mol*s)'), n=4.75583, w0=(525,'kJ/mol'), E0=(161.43,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_Ext-3C-R_N-4BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_Ext-3C-R_N-4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_Ext-3C-R_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_Ext-3C-R_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 323,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFINOPSSi->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(1.46161e-24,'m^3/(mol*s)'), n=8.84783, w0=(525,'kJ/mol'), E0=(125.212,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFINOPSSi->C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFINOPSSi->C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFINOPSSi->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFINOPSSi->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 324,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_4FO->O",
    kinetics = ArrheniusBM(A=(3.68586e-11,'m^3/(mol*s)'), n=4.70466, w0=(525,'kJ/mol'), E0=(162.823,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_4FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_4FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_4FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_4FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 325,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_N-4FO->O",
    kinetics = ArrheniusBM(A=(2.96186e-11,'m^3/(mol*s)'), n=4.53079, w0=(525,'kJ/mol'), E0=(154.874,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_N-4FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_N-4FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_N-4FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_N-4FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 326,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_N-4FO->F_Sp-4O-3C",
    kinetics = ArrheniusBM(A=(5.55553e-11,'m^3/(mol*s)'), n=4.70327, w0=(525,'kJ/mol'), E0=(136.865,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_N-4FO->F_Sp-4O-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_N-4FO->F_Sp-4O-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_N-4FO->F_Sp-4O-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_N-4FO->F_Sp-4O-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 327,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_N-4FO->F_N-Sp-4O-3C",
    kinetics = ArrheniusBM(A=(1.47529e-08,'m^3/(mol*s)'), n=4.12698, w0=(525,'kJ/mol'), E0=(154.869,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_N-4FO->F_N-Sp-4O-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_N-4FO->F_N-Sp-4O-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_N-4FO->F_N-Sp-4O-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_N-1CClH->C_N-3CCl->Cl_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_N-4FO->F_N-Sp-4O-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 328,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_7R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.000145249,'m^3/(mol*s)'), n=2.84864, w0=(485,'kJ/mol'), E0=(194.031,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_7R!H->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_7R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_7R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_7R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 329,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_N-7R!H->C_5R!H->F",
    kinetics = ArrheniusBM(A=(4.86925e-07,'m^3/(mol*s)'), n=3.84755, w0=(485,'kJ/mol'), E0=(182.435,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0960091925402666, var=2.0878679097954644, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_N-7R!H->C_5R!H->F',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_N-7R!H->C_5R!H->F
    Total Standard Deviation in ln(k): 3.1379623414440583"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_N-7R!H->C_5R!H->F
Total Standard Deviation in ln(k): 3.1379623414440583""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_N-7R!H->C_5R!H->F
Total Standard Deviation in ln(k): 3.1379623414440583
""",
)

entry(
    index = 330,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_N-7R!H->C_N-5R!H->F",
    kinetics = ArrheniusBM(A=(2.47232e-06,'m^3/(mol*s)'), n=3.97637, w0=(485,'kJ/mol'), E0=(194.828,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_N-7R!H->C_N-5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_N-7R!H->C_N-5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_N-7R!H->C_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_N-7R!H->C_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 331,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_6R!H->O",
    kinetics = ArrheniusBM(A=(1.50054e-05,'m^3/(mol*s)'), n=3.79284, w0=(485,'kJ/mol'), E0=(187.083,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.005088736941093816, var=2.1376794914896005, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_6R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_6R!H->O
    Total Standard Deviation in ln(k): 2.943869906153487"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_6R!H->O
Total Standard Deviation in ln(k): 2.943869906153487""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_6R!H->O
Total Standard Deviation in ln(k): 2.943869906153487
""",
)

entry(
    index = 332,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_N-6R!H->O",
    kinetics = ArrheniusBM(A=(7.70504e-06,'m^3/(mol*s)'), n=3.51763, w0=(485,'kJ/mol'), E0=(196.685,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04959390361496888, var=1.7912645786841095, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_N-6R!H->O',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_N-6R!H->O
    Total Standard Deviation in ln(k): 2.8077077928577854"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_N-6R!H->O
Total Standard Deviation in ln(k): 2.8077077928577854""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_N-6R!H->O
Total Standard Deviation in ln(k): 2.8077077928577854
""",
)

entry(
    index = 333,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_5R!H->C_Ext-3CCl-R",
    kinetics = ArrheniusBM(A=(1.6394e-08,'m^3/(mol*s)'), n=4.20067, w0=(485,'kJ/mol'), E0=(170.79,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.22661832906730353, var=4.962422799104255, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_5R!H->C_Ext-3CCl-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_5R!H->C_Ext-3CCl-R
    Total Standard Deviation in ln(k): 5.035240106288148"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_5R!H->C_Ext-3CCl-R
Total Standard Deviation in ln(k): 5.035240106288148""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_5R!H->C_Ext-3CCl-R
Total Standard Deviation in ln(k): 5.035240106288148
""",
)

entry(
    index = 334,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_5R!H->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(1.43184e-08,'m^3/(mol*s)'), n=4.29567, w0=(485,'kJ/mol'), E0=(166.374,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1435250581045639, var=0.3600922451326483, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_5R!H->C_Ext-5C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_5R!H->C_Ext-5C-R
    Total Standard Deviation in ln(k): 1.5636108663242876"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 1.5636108663242876""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 1.5636108663242876
""",
)

entry(
    index = 335,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_N-5R!H->C_Sp-5BrBrCClClClFFIINNOOPPSSSiSi=3BrBrCCClClClClFFIINNOOPPSSSiSi",
    kinetics = ArrheniusBM(A=(5.94508e-05,'m^3/(mol*s)'), n=3.37621, w0=(485,'kJ/mol'), E0=(190.622,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.14501143760179874, var=0.535319801453646, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_N-5R!H->C_Sp-5BrBrCClClClFFIINNOOPPSSSiSi=3BrBrCCClClClClFFIINNOOPPSSSiSi',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_N-5R!H->C_Sp-5BrBrCClClClFFIINNOOPPSSSiSi=3BrBrCCClClClClFFIINNOOPPSSSiSi
    Total Standard Deviation in ln(k): 1.8311258333110374"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_N-5R!H->C_Sp-5BrBrCClClClFFIINNOOPPSSSiSi=3BrBrCCClClClClFFIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 1.8311258333110374""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_N-5R!H->C_Sp-5BrBrCClClClFFIINNOOPPSSSiSi=3BrBrCCClClClClFFIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 1.8311258333110374
""",
)

entry(
    index = 336,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_N-5R!H->C_N-Sp-5BrBrCClClClFFIINNOOPPSSSiSi=3BrBrCCClClClClFFIINNOOPPSSSiSi",
    kinetics = ArrheniusBM(A=(2.46703e-07,'m^3/(mol*s)'), n=4.01498, w0=(485,'kJ/mol'), E0=(174.93,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.847640735516106, var=15.359050616724181, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_N-5R!H->C_N-Sp-5BrBrCClClClFFIINNOOPPSSSiSi=3BrBrCCClClClClFFIINNOOPPSSSiSi',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_N-5R!H->C_N-Sp-5BrBrCClClClFFIINNOOPPSSSiSi=3BrBrCCClClClClFFIINNOOPPSSSiSi
    Total Standard Deviation in ln(k): 12.498995403011742"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_N-5R!H->C_N-Sp-5BrBrCClClClFFIINNOOPPSSSiSi=3BrBrCCClClClClFFIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 12.498995403011742""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_N-5R!H->C_N-Sp-5BrBrCClClClFFIINNOOPPSSSiSi=3BrBrCCClClClClFFIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 12.498995403011742
""",
)

entry(
    index = 337,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_4CO->C_5R!H->F",
    kinetics = ArrheniusBM(A=(1.04194e-07,'m^3/(mol*s)'), n=3.9712, w0=(485,'kJ/mol'), E0=(168.055,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12341804144031279, var=0.03795975742173232, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_4CO->C_5R!H->F',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_4CO->C_5R!H->F
    Total Standard Deviation in ln(k): 0.7006834081722779"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_4CO->C_5R!H->F
Total Standard Deviation in ln(k): 0.7006834081722779""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_4CO->C_5R!H->F
Total Standard Deviation in ln(k): 0.7006834081722779
""",
)

entry(
    index = 338,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_4CO->C_N-5R!H->F",
    kinetics = ArrheniusBM(A=(9.11574e-08,'m^3/(mol*s)'), n=4.14961, w0=(485,'kJ/mol'), E0=(177.038,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_4CO->C_N-5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_4CO->C_N-5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_4CO->C_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_4CO->C_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 339,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_N-4CO->C_Ext-3CCl-R",
    kinetics = ArrheniusBM(A=(4.02769e-08,'m^3/(mol*s)'), n=4.09467, w0=(485,'kJ/mol'), E0=(170.981,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1344579195349335, var=0.5134742245781766, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_N-4CO->C_Ext-3CCl-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_N-4CO->C_Ext-3CCl-R
    Total Standard Deviation in ln(k): 1.7743693047131563"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_N-4CO->C_Ext-3CCl-R
Total Standard Deviation in ln(k): 1.7743693047131563""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_N-4CO->C_Ext-3CCl-R
Total Standard Deviation in ln(k): 1.7743693047131563
""",
)

entry(
    index = 340,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_N-7R!H->C_5R!H->F_Sp-6R!H=4C",
    kinetics = ArrheniusBM(A=(3.8501e-07,'m^3/(mol*s)'), n=3.92844, w0=(485,'kJ/mol'), E0=(191.208,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_N-7R!H->C_5R!H->F_Sp-6R!H=4C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_N-7R!H->C_5R!H->F_Sp-6R!H=4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_N-7R!H->C_5R!H->F_Sp-6R!H=4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_N-7R!H->C_5R!H->F_Sp-6R!H=4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 341,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_N-7R!H->C_5R!H->F_N-Sp-6R!H=4C",
    kinetics = ArrheniusBM(A=(9.19499e-07,'m^3/(mol*s)'), n=3.75122, w0=(485,'kJ/mol'), E0=(180.122,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.16931566407085466, var=3.515915180339681, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_N-7R!H->C_5R!H->F_N-Sp-6R!H=4C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_N-7R!H->C_5R!H->F_N-Sp-6R!H=4C
    Total Standard Deviation in ln(k): 4.1844496375519515"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_N-7R!H->C_5R!H->F_N-Sp-6R!H=4C
Total Standard Deviation in ln(k): 4.1844496375519515""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_N-7R!H->C_5R!H->F_N-Sp-6R!H=4C
Total Standard Deviation in ln(k): 4.1844496375519515
""",
)

entry(
    index = 342,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_6R!H->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.68364e-05,'m^3/(mol*s)'), n=3.9376, w0=(485,'kJ/mol'), E0=(195.002,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_6R!H->O_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_6R!H->O_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_6R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_6R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 343,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_6R!H->O_Sp-6O-3CCl",
    kinetics = ArrheniusBM(A=(2.28891e-06,'m^3/(mol*s)'), n=3.82239, w0=(485,'kJ/mol'), E0=(176.853,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_6R!H->O_Sp-6O-3CCl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_6R!H->O_Sp-6O-3CCl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_6R!H->O_Sp-6O-3CCl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_6R!H->O_Sp-6O-3CCl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 344,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_6R!H->O_N-Sp-6O-3CCl",
    kinetics = ArrheniusBM(A=(0.00168439,'m^3/(mol*s)'), n=3.12619, w0=(485,'kJ/mol'), E0=(197.881,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_6R!H->O_N-Sp-6O-3CCl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_6R!H->O_N-Sp-6O-3CCl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_6R!H->O_N-Sp-6O-3CCl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_6R!H->O_N-Sp-6O-3CCl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 345,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_N-6R!H->O_6BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(1.43033e-06,'m^3/(mol*s)'), n=3.73989, w0=(485,'kJ/mol'), E0=(195.288,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.029338637895178165, var=3.7318857833729817, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_N-6R!H->O_6BrCClFINPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_N-6R!H->O_6BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 3.9464803168381426"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_N-6R!H->O_6BrCClFINPSSi->C
Total Standard Deviation in ln(k): 3.9464803168381426""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_N-6R!H->O_6BrCClFINPSSi->C
Total Standard Deviation in ln(k): 3.9464803168381426
""",
)

entry(
    index = 346,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_N-6R!H->O_N-6BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(0.00139189,'m^3/(mol*s)'), n=2.83127, w0=(485,'kJ/mol'), E0=(200.974,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.13039190977957113, var=3.2232542925893632, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_N-6R!H->O_N-6BrCClFINPSSi->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_N-6R!H->O_N-6BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 3.9268037262861055"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_N-6R!H->O_N-6BrCClFINPSSi->C
Total Standard Deviation in ln(k): 3.9268037262861055""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_N-6R!H->O_N-6BrCClFINPSSi->C
Total Standard Deviation in ln(k): 3.9268037262861055
""",
)

entry(
    index = 347,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_5R!H->C_Ext-3CCl-R_Ext-5C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(1.31087e-08,'m^3/(mol*s)'), n=4.12499, w0=(485,'kJ/mol'), E0=(171.382,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_5R!H->C_Ext-3CCl-R_Ext-5C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_5R!H->C_Ext-3CCl-R_Ext-5C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_5R!H->C_Ext-3CCl-R_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_5R!H->C_Ext-3CCl-R_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 348,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_5R!H->C_Ext-3CCl-R_Ext-5C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(2.14559e-08,'m^3/(mol*s)'), n=4.27069, w0=(485,'kJ/mol'), E0=(170.247,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_5R!H->C_Ext-3CCl-R_Ext-5C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_5R!H->C_Ext-3CCl-R_Ext-5C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_5R!H->C_Ext-3CCl-R_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_5R!H->C_Ext-3CCl-R_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 349,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_5R!H->C_Ext-5C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(3.45985e-08,'m^3/(mol*s)'), n=4.20193, w0=(485,'kJ/mol'), E0=(166.436,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_5R!H->C_Ext-5C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_5R!H->C_Ext-5C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_5R!H->C_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_5R!H->C_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 350,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_5R!H->C_Ext-5C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(6.21207e-09,'m^3/(mol*s)'), n=4.38354, w0=(485,'kJ/mol'), E0=(166.362,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_5R!H->C_Ext-5C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_5R!H->C_Ext-5C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_5R!H->C_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_5R!H->C_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 351,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_N-5R!H->C_Sp-5BrBrCClClClFFIINNOOPPSSSiSi=3BrBrCCClClClClFFIINNOOPPSSSiSi_Ext-3CCl-R",
    kinetics = ArrheniusBM(A=(0.0001135,'m^3/(mol*s)'), n=3.32, w0=(485,'kJ/mol'), E0=(195.165,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_N-5R!H->C_Sp-5BrBrCClClClFFIINNOOPPSSSiSi=3BrBrCCClClClClFFIINNOOPPSSSiSi_Ext-3CCl-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_N-5R!H->C_Sp-5BrBrCClClClFFIINNOOPPSSSiSi=3BrBrCCClClClClFFIINNOOPPSSSiSi_Ext-3CCl-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_N-5R!H->C_Sp-5BrBrCClClClFFIINNOOPPSSSiSi=3BrBrCCClClClClFFIINNOOPPSSSiSi_Ext-3CCl-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_N-5R!H->C_Sp-5BrBrCClClClFFIINNOOPPSSSiSi=3BrBrCCClClClClFFIINNOOPPSSSiSi_Ext-3CCl-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 352,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_N-5R!H->C_N-Sp-5BrBrCClClClFFIINNOOPPSSSiSi=3BrBrCCClClClClFFIINNOOPPSSSiSi_Ext-3CCl-R",
    kinetics = ArrheniusBM(A=(3.05889e-05,'m^3/(mol*s)'), n=3.30617, w0=(485,'kJ/mol'), E0=(194.249,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.21443168705568316, var=0.0840085163809187, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_N-5R!H->C_N-Sp-5BrBrCClClClFFIINNOOPPSSSiSi=3BrBrCCClClClClFFIINNOOPPSSSiSi_Ext-3CCl-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_N-5R!H->C_N-Sp-5BrBrCClClClFFIINNOOPPSSSiSi=3BrBrCCClClClClFFIINNOOPPSSSiSi_Ext-3CCl-R
    Total Standard Deviation in ln(k): 1.1198299618386542"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_N-5R!H->C_N-Sp-5BrBrCClClClFFIINNOOPPSSSiSi=3BrBrCCClClClClFFIINNOOPPSSSiSi_Ext-3CCl-R
Total Standard Deviation in ln(k): 1.1198299618386542""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_N-5R!H->C_N-Sp-5BrBrCClClClFFIINNOOPPSSSiSi=3BrBrCCClClClClFFIINNOOPPSSSiSi_Ext-3CCl-R
Total Standard Deviation in ln(k): 1.1198299618386542
""",
)

entry(
    index = 353,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_4CO->C_5R!H->F_Ext-4C-R",
    kinetics = ArrheniusBM(A=(9.11391e-08,'m^3/(mol*s)'), n=3.97251, w0=(485,'kJ/mol'), E0=(166.8,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12852274226468113, var=0.13186923682206217, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_4CO->C_5R!H->F_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_4CO->C_5R!H->F_Ext-4C-R
    Total Standard Deviation in ln(k): 1.05091703170753"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_4CO->C_5R!H->F_Ext-4C-R
Total Standard Deviation in ln(k): 1.05091703170753""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_4CO->C_5R!H->F_Ext-4C-R
Total Standard Deviation in ln(k): 1.05091703170753
""",
)

entry(
    index = 354,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_N-4CO->C_Ext-3CCl-R_5R!H->C",
    kinetics = ArrheniusBM(A=(4.11856e-08,'m^3/(mol*s)'), n=4.0381, w0=(485,'kJ/mol'), E0=(165.871,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_N-4CO->C_Ext-3CCl-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_N-4CO->C_Ext-3CCl-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_N-4CO->C_Ext-3CCl-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_N-4CO->C_Ext-3CCl-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 355,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_N-4CO->C_Ext-3CCl-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(6.32707e-08,'m^3/(mol*s)'), n=4.09227, w0=(485,'kJ/mol'), E0=(176.621,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_N-4CO->C_Ext-3CCl-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_N-4CO->C_Ext-3CCl-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_N-4CO->C_Ext-3CCl-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_N-4CO->C_Ext-3CCl-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 356,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_N-7R!H->C_5R!H->F_N-Sp-6R!H=4C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6.83125e-07,'m^3/(mol*s)'), n=3.8806, w0=(485,'kJ/mol'), E0=(197.6,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_N-7R!H->C_5R!H->F_N-Sp-6R!H=4C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_N-7R!H->C_5R!H->F_N-Sp-6R!H=4C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_N-7R!H->C_5R!H->F_N-Sp-6R!H=4C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_N-7R!H->C_5R!H->F_N-Sp-6R!H=4C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 357,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_N-7R!H->C_5R!H->F_N-Sp-6R!H=4C_6R!H->F",
    kinetics = ArrheniusBM(A=(3.50479e-07,'m^3/(mol*s)'), n=3.85832, w0=(485,'kJ/mol'), E0=(171.028,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_N-7R!H->C_5R!H->F_N-Sp-6R!H=4C_6R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_N-7R!H->C_5R!H->F_N-Sp-6R!H=4C_6R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_N-7R!H->C_5R!H->F_N-Sp-6R!H=4C_6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_N-7R!H->C_5R!H->F_N-Sp-6R!H=4C_6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 358,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_N-7R!H->C_5R!H->F_N-Sp-6R!H=4C_N-6R!H->F",
    kinetics = ArrheniusBM(A=(6.55056e-06,'m^3/(mol*s)'), n=3.42741, w0=(485,'kJ/mol'), E0=(172.504,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_N-7R!H->C_5R!H->F_N-Sp-6R!H=4C_N-6R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_N-7R!H->C_5R!H->F_N-Sp-6R!H=4C_N-6R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_N-7R!H->C_5R!H->F_N-Sp-6R!H=4C_N-6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3CCl-R_N-7R!H->C_5R!H->F_N-Sp-6R!H=4C_N-6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 359,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(5.76532e-06,'m^3/(mol*s)'), n=3.58647, w0=(485,'kJ/mol'), E0=(192.053,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 360,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(1.00057e-07,'m^3/(mol*s)'), n=4.05084, w0=(485,'kJ/mol'), E0=(197.154,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 361,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_N-6R!H->O_N-6BrCClFINPSSi->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.00676358,'m^3/(mol*s)'), n=2.69434, w0=(485,'kJ/mol'), E0=(203.157,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1920396451478112, var=11.520881032749676, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_N-6R!H->O_N-6BrCClFINPSSi->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_N-6R!H->O_N-6BrCClFINPSSi->C_Ext-1C-R
    Total Standard Deviation in ln(k): 7.287068342570407"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_N-6R!H->O_N-6BrCClFINPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 7.287068342570407""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_N-6R!H->O_N-6BrCClFINPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 7.287068342570407
""",
)

entry(
    index = 362,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_N-6R!H->O_N-6BrCClFINPSSi->C_Ext-3CCl-R",
    kinetics = ArrheniusBM(A=(2.96e-05,'m^3/(mol*s)'), n=3.23, w0=(485,'kJ/mol'), E0=(204.744,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_N-6R!H->O_N-6BrCClFINPSSi->C_Ext-3CCl-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_N-6R!H->O_N-6BrCClFINPSSi->C_Ext-3CCl-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_N-6R!H->O_N-6BrCClFINPSSi->C_Ext-3CCl-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_N-6R!H->O_N-6BrCClFINPSSi->C_Ext-3CCl-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 363,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_N-5R!H->C_N-Sp-5BrBrCClClClFFIINNOOPPSSSiSi=3BrBrCCClClClClFFIINNOOPPSSSiSi_Ext-3CCl-R_Ext-3CCl-R",
    kinetics = ArrheniusBM(A=(4.915e-05,'m^3/(mol*s)'), n=3.31, w0=(485,'kJ/mol'), E0=(197.747,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_N-5R!H->C_N-Sp-5BrBrCClClClFFIINNOOPPSSSiSi=3BrBrCCClClClClFFIINNOOPPSSSiSi_Ext-3CCl-R_Ext-3CCl-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_N-5R!H->C_N-Sp-5BrBrCClClClFFIINNOOPPSSSiSi=3BrBrCCClClClClFFIINNOOPPSSSiSi_Ext-3CCl-R_Ext-3CCl-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_N-5R!H->C_N-Sp-5BrBrCClClClFFIINNOOPPSSSiSi=3BrBrCCClClClClFFIINNOOPPSSSiSi_Ext-3CCl-R_Ext-3CCl-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3CCl-R_N-5R!H->C_N-Sp-5BrBrCClClClFFIINNOOPPSSSiSi=3BrBrCCClClClClFFIINNOOPPSSSiSi_Ext-3CCl-R_Ext-3CCl-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 364,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_4CO->C_5R!H->F_Ext-4C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(7.80562e-08,'m^3/(mol*s)'), n=3.96948, w0=(485,'kJ/mol'), E0=(166.513,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_4CO->C_5R!H->F_Ext-4C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_4CO->C_5R!H->F_Ext-4C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_4CO->C_5R!H->F_Ext-4C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_4CO->C_5R!H->F_Ext-4C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 365,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_4CO->C_5R!H->F_Ext-4C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(1.03271e-07,'m^3/(mol*s)'), n=3.97927, w0=(485,'kJ/mol'), E0=(167.054,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_4CO->C_5R!H->F_Ext-4C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_4CO->C_5R!H->F_Ext-4C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_4CO->C_5R!H->F_Ext-4C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3CCl-R_4CO->C_5R!H->F_Ext-4C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 366,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_N-6R!H->O_N-6BrCClFINPSSi->C_Ext-1C-R_Ext-3CCl-R",
    kinetics = ArrheniusBM(A=(0.000284922,'m^3/(mol*s)'), n=3.00496, w0=(485,'kJ/mol'), E0=(205.158,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_N-6R!H->O_N-6BrCClFINPSSi->C_Ext-1C-R_Ext-3CCl-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_N-6R!H->O_N-6BrCClFINPSSi->C_Ext-1C-R_Ext-3CCl-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_N-6R!H->O_N-6BrCClFINPSSi->C_Ext-1C-R_Ext-3CCl-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->F_N-3CClH->H_3CCl-u1_1CClH->C_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3CCl-R_N-6R!H->O_N-6BrCClFINPSSi->C_Ext-1C-R_Ext-3CCl-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

