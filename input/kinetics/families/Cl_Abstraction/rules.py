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
    kinetics = ArrheniusBM(A=(3.8818e+08,'m^3/(mol*s)'), n=-0.452812, w0=(331.857,'kJ/mol'), E0=(83.4605,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2406029078311829, var=9.487340514870478, Tref=1000.0, N=476, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 476 training reactions at node Root
    Total Standard Deviation in ln(k): 6.779420034888771"""),
    rank = 11,
    shortDesc = """BM rule fitted to 476 training reactions at node Root
Total Standard Deviation in ln(k): 6.779420034888771""",
    longDesc = 
"""
BM rule fitted to 476 training reactions at node Root
Total Standard Deviation in ln(k): 6.779420034888771
""",
)

entry(
    index = 2,
    label = "Root_3R->H",
    kinetics = ArrheniusBM(A=(324.429,'m^3/(mol*s)'), n=1.65695, w0=(375.737,'kJ/mol'), E0=(65.0871,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3072552990164269, var=1.41541293709976, Tref=1000.0, N=78, data_mean=0.0, correlation='Root_3R->H',), comment="""BM rule fitted to 78 training reactions at node Root_3R->H
    Total Standard Deviation in ln(k): 3.157054179906825"""),
    rank = 11,
    shortDesc = """BM rule fitted to 78 training reactions at node Root_3R->H
Total Standard Deviation in ln(k): 3.157054179906825""",
    longDesc = 
"""
BM rule fitted to 78 training reactions at node Root_3R->H
Total Standard Deviation in ln(k): 3.157054179906825
""",
)

entry(
    index = 3,
    label = "Root_3R->H_1R->C",
    kinetics = ArrheniusBM(A=(1.8926e-05,'m^3/(mol*s)'), n=3.72123, w0=(377.5,'kJ/mol'), E0=(43.8133,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06153363521668375, var=1.1674350364516553, Tref=1000.0, N=73, data_mean=0.0, correlation='Root_3R->H_1R->C',), comment="""BM rule fitted to 73 training reactions at node Root_3R->H_1R->C
    Total Standard Deviation in ln(k): 2.3206814302846337"""),
    rank = 11,
    shortDesc = """BM rule fitted to 73 training reactions at node Root_3R->H_1R->C
Total Standard Deviation in ln(k): 2.3206814302846337""",
    longDesc = 
"""
BM rule fitted to 73 training reactions at node Root_3R->H_1R->C
Total Standard Deviation in ln(k): 2.3206814302846337
""",
)

entry(
    index = 4,
    label = "Root_3R->H_1R->C_1C-u0",
    kinetics = ArrheniusBM(A=(3.75885e-06,'m^3/(mol*s)'), n=3.92997, w0=(377.5,'kJ/mol'), E0=(41.3104,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.010171341599995703, var=0.9090141464466714, Tref=1000.0, N=65, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0',), comment="""BM rule fitted to 65 training reactions at node Root_3R->H_1R->C_1C-u0
    Total Standard Deviation in ln(k): 1.9369153306639395"""),
    rank = 11,
    shortDesc = """BM rule fitted to 65 training reactions at node Root_3R->H_1R->C_1C-u0
Total Standard Deviation in ln(k): 1.9369153306639395""",
    longDesc = 
"""
BM rule fitted to 65 training reactions at node Root_3R->H_1R->C_1C-u0
Total Standard Deviation in ln(k): 1.9369153306639395
""",
)

entry(
    index = 5,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.28851e-06,'m^3/(mol*s)'), n=3.94591, w0=(377.5,'kJ/mol'), E0=(40.985,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.008958494581522685, var=0.9207973187100628, Tref=1000.0, N=64, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R',), comment="""BM rule fitted to 64 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R
    Total Standard Deviation in ln(k): 1.9462161661790647"""),
    rank = 11,
    shortDesc = """BM rule fitted to 64 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 1.9462161661790647""",
    longDesc = 
"""
BM rule fitted to 64 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 1.9462161661790647
""",
)

entry(
    index = 6,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(0.000798217,'m^3/(mol*s)'), n=3.24871, w0=(377.5,'kJ/mol'), E0=(48.194,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.117392811345718, var=0.7677049847729723, Tref=1000.0, N=56, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C',), comment="""BM rule fitted to 56 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C
    Total Standard Deviation in ln(k): 2.051481142416793"""),
    rank = 11,
    shortDesc = """BM rule fitted to 56 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C
Total Standard Deviation in ln(k): 2.051481142416793""",
    longDesc = 
"""
BM rule fitted to 56 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C
Total Standard Deviation in ln(k): 2.051481142416793
""",
)

entry(
    index = 7,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C",
    kinetics = ArrheniusBM(A=(7.68092e-07,'m^3/(mol*s)'), n=4.11481, w0=(377.5,'kJ/mol'), E0=(36.1858,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.029630927091921774, var=0.8612399648374393, Tref=1000.0, N=35, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C',), comment="""BM rule fitted to 35 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C
    Total Standard Deviation in ln(k): 1.9349041661131878"""),
    rank = 11,
    shortDesc = """BM rule fitted to 35 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C
Total Standard Deviation in ln(k): 1.9349041661131878""",
    longDesc = 
"""
BM rule fitted to 35 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C
Total Standard Deviation in ln(k): 1.9349041661131878
""",
)

entry(
    index = 8,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.07874e-07,'m^3/(mol*s)'), n=4.21779, w0=(377.5,'kJ/mol'), E0=(32.1905,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.07764779844235388, var=0.952938858826725, Tref=1000.0, N=26, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R',), comment="""BM rule fitted to 26 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 2.1520890328072366"""),
    rank = 11,
    shortDesc = """BM rule fitted to 26 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 2.1520890328072366""",
    longDesc = 
"""
BM rule fitted to 26 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 2.1520890328072366
""",
)

entry(
    index = 9,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(8.54231e-07,'m^3/(mol*s)'), n=4.09238, w0=(377.5,'kJ/mol'), E0=(25.0585,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1945060516172328, var=0.7962255093201512, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 15 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 2.2775632352632815"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 2.2775632352632815""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 2.2775632352632815
""",
)

entry(
    index = 10,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(76300,'m^3/(mol*s)'), n=0.975209, w0=(377.5,'kJ/mol'), E0=(57.2803,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.548414718571427, var=2.261768437179915, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 4.3928829878149"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 4.3928829878149""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 4.3928829878149
""",
)

entry(
    index = 11,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_7R!H->C",
    kinetics = ArrheniusBM(A=(64.768,'m^3/(mol*s)'), n=1.81809, w0=(377.5,'kJ/mol'), E0=(54.2366,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(23769.7,'m^3/(mol*s)'), n=1.13885, w0=(377.5,'kJ/mol'), E0=(52.7723,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.40713066901509964, var=3.2061454026843297, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_N-7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_N-7R!H->C
    Total Standard Deviation in ln(k): 4.612562373643468"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 4.612562373643468""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 4.612562373643468
""",
)

entry(
    index = 13,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_N-7R!H->C_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(209.185,'m^3/(mol*s)'), n=1.80526, w0=(377.5,'kJ/mol'), E0=(45.3766,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_N-7R!H->C_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_N-7R!H->C_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_N-7R!H->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_N-7R!H->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_5R!H->F",
    kinetics = ArrheniusBM(A=(2.57956,'m^3/(mol*s)'), n=2.23999, w0=(377.5,'kJ/mol'), E0=(54.0084,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.32762508586335115, var=0.24892010259715072, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_5R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_5R!H->F
    Total Standard Deviation in ln(k): 1.8233788952486925"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_5R!H->F
Total Standard Deviation in ln(k): 1.8233788952486925""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_5R!H->F
Total Standard Deviation in ln(k): 1.8233788952486925
""",
)

entry(
    index = 15,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_5R!H->F_Ext-4C-R",
    kinetics = ArrheniusBM(A=(65.426,'m^3/(mol*s)'), n=1.83086, w0=(377.5,'kJ/mol'), E0=(59.9111,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_5R!H->F_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_5R!H->F_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_5R!H->F_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_5R!H->F_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(3.23983e-07,'m^3/(mol*s)'), n=4.20605, w0=(377.5,'kJ/mol'), E0=(17.9473,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2162952616596391, var=0.6316451759696616, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F',), comment="""BM rule fitted to 10 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F
    Total Standard Deviation in ln(k): 2.136740848656815"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F
Total Standard Deviation in ln(k): 2.136740848656815""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F
Total Standard Deviation in ln(k): 2.136740848656815
""",
)

entry(
    index = 17,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->O",
    kinetics = ArrheniusBM(A=(0.624479,'m^3/(mol*s)'), n=2.40957, w0=(377.5,'kJ/mol'), E0=(44.6542,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.31670101270122164, var=0.17895919769356108, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->O',), comment="""BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->O
    Total Standard Deviation in ln(k): 1.6438056807737946"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->O
Total Standard Deviation in ln(k): 1.6438056807737946""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->O
Total Standard Deviation in ln(k): 1.6438056807737946
""",
)

entry(
    index = 18,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->O_6R!H->C",
    kinetics = ArrheniusBM(A=(107.671,'m^3/(mol*s)'), n=1.76176, w0=(377.5,'kJ/mol'), E0=(49.448,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->O_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->O_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->O_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->O_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->O_N-6R!H->C",
    kinetics = ArrheniusBM(A=(117.661,'m^3/(mol*s)'), n=1.76471, w0=(377.5,'kJ/mol'), E0=(54.223,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->O_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->O_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->O_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->O_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O",
    kinetics = ArrheniusBM(A=(0.0217584,'m^3/(mol*s)'), n=2.82195, w0=(377.5,'kJ/mol'), E0=(57.0319,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2183689687248578, var=0.7786312076453775, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O',), comment="""BM rule fitted to 8 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O
    Total Standard Deviation in ln(k): 2.317645627318183"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O
Total Standard Deviation in ln(k): 2.317645627318183""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O
Total Standard Deviation in ln(k): 2.317645627318183
""",
)

entry(
    index = 21,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_5CCl->C",
    kinetics = ArrheniusBM(A=(58.4325,'m^3/(mol*s)'), n=1.86734, w0=(377.5,'kJ/mol'), E0=(70.0764,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_5CCl->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_5CCl->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_5CCl->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_5CCl->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C",
    kinetics = ArrheniusBM(A=(5.32657e-07,'m^3/(mol*s)'), n=4.13914, w0=(377.5,'kJ/mol'), E0=(28.2406,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.20143640593389378, var=0.5890972821345056, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C',), comment="""BM rule fitted to 7 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C
    Total Standard Deviation in ln(k): 2.04480938255431"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C
Total Standard Deviation in ln(k): 2.04480938255431""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C
Total Standard Deviation in ln(k): 2.04480938255431
""",
)

entry(
    index = 23,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(2.88938,'m^3/(mol*s)'), n=2.20077, w0=(377.5,'kJ/mol'), E0=(65.7265,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.22694998537874672, var=0.5204852738460685, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R',), comment="""BM rule fitted to 6 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R
    Total Standard Deviation in ln(k): 2.0165355066561204"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R
Total Standard Deviation in ln(k): 2.0165355066561204""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R
Total Standard Deviation in ln(k): 2.0165355066561204
""",
)

entry(
    index = 24,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(14.4896,'m^3/(mol*s)'), n=2.01167, w0=(377.5,'kJ/mol'), E0=(70.9142,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2730863994931993, var=0.30399280637316123, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R',), comment="""BM rule fitted to 5 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 1.7914682960877815"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 1.7914682960877815""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 1.7914682960877815
""",
)

entry(
    index = 25,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_7R!H->F",
    kinetics = ArrheniusBM(A=(2.49121,'m^3/(mol*s)'), n=2.20599, w0=(377.5,'kJ/mol'), E0=(62.8358,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2506179937365303, var=1.3556002588495772, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_7R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_7R!H->F
    Total Standard Deviation in ln(k): 2.9638114687139936"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_7R!H->F
Total Standard Deviation in ln(k): 2.9638114687139936""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_7R!H->F
Total Standard Deviation in ln(k): 2.9638114687139936
""",
)

entry(
    index = 26,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_7R!H->F_8R!H->C",
    kinetics = ArrheniusBM(A=(46.947,'m^3/(mol*s)'), n=1.75719, w0=(377.5,'kJ/mol'), E0=(55.3865,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_7R!H->F_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_7R!H->F_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_7R!H->F_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_7R!H->F_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_7R!H->F_N-8R!H->C",
    kinetics = ArrheniusBM(A=(131.082,'m^3/(mol*s)'), n=1.7963, w0=(377.5,'kJ/mol'), E0=(79.2477,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_7R!H->F_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_7R!H->F_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_7R!H->F_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_7R!H->F_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_N-7R!H->F",
    kinetics = ArrheniusBM(A=(94.8048,'m^3/(mol*s)'), n=1.79444, w0=(377.5,'kJ/mol'), E0=(77.032,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3146319062891615, var=0.07356115419209124, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_N-7R!H->F',), comment="""BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_N-7R!H->F
    Total Standard Deviation in ln(k): 1.334259875314625"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_N-7R!H->F
Total Standard Deviation in ln(k): 1.334259875314625""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_N-7R!H->F
Total Standard Deviation in ln(k): 1.334259875314625
""",
)

entry(
    index = 29,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_N-7R!H->F_7CCl->C",
    kinetics = ArrheniusBM(A=(81.3833,'m^3/(mol*s)'), n=1.79753, w0=(377.5,'kJ/mol'), E0=(77.7444,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_N-7R!H->F_7CCl->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_N-7R!H->F_7CCl->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_N-7R!H->F_7CCl->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_N-7R!H->F_7CCl->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 30,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_N-7R!H->F_N-7CCl->C",
    kinetics = ArrheniusBM(A=(114.913,'m^3/(mol*s)'), n=1.77846, w0=(377.5,'kJ/mol'), E0=(76.8296,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3329899550414647, var=0.08368708760374793, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_N-7R!H->F_N-7CCl->C',), comment="""BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_N-7R!H->F_N-7CCl->C
    Total Standard Deviation in ln(k): 1.4166023879736023"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_N-7R!H->F_N-7CCl->C
Total Standard Deviation in ln(k): 1.4166023879736023""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_N-7R!H->F_N-7CCl->C
Total Standard Deviation in ln(k): 1.4166023879736023
""",
)

entry(
    index = 31,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_N-7R!H->F_N-7CCl->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(134.809,'m^3/(mol*s)'), n=1.77494, w0=(377.5,'kJ/mol'), E0=(77.0456,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_N-7R!H->F_N-7CCl->C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_N-7R!H->F_N-7CCl->C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_N-7R!H->F_N-7CCl->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->O_N-5CCl->C_Ext-4C-R_Ext-4C-R_N-7R!H->F_N-7CCl->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 32,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(1740.6,'m^3/(mol*s)'), n=1.39113, w0=(377.5,'kJ/mol'), E0=(70.1458,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3198519715525826, var=1.6097658899727378, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl',), comment="""BM rule fitted to 5 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl
    Total Standard Deviation in ln(k): 3.347186869393644"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl
Total Standard Deviation in ln(k): 3.347186869393644""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl
Total Standard Deviation in ln(k): 3.347186869393644
""",
)

entry(
    index = 33,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R",
    kinetics = ArrheniusBM(A=(11326.4,'m^3/(mol*s)'), n=1.13998, w0=(377.5,'kJ/mol'), E0=(73.5721,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.35653366949045323, var=1.737143867395948, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R',), comment="""BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R
    Total Standard Deviation in ln(k): 3.5380691814728364"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R
Total Standard Deviation in ln(k): 3.5380691814728364""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R
Total Standard Deviation in ln(k): 3.5380691814728364
""",
)

entry(
    index = 34,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(18.1398,'m^3/(mol*s)'), n=1.9317, w0=(377.5,'kJ/mol'), E0=(72.9778,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3011723212497701, var=0.00010015117539178098, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R_6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R_6R!H->C
    Total Standard Deviation in ln(k): 0.7767768733811989"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R_6R!H->C
Total Standard Deviation in ln(k): 0.7767768733811989""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R_6R!H->C
Total Standard Deviation in ln(k): 0.7767768733811989
""",
)

entry(
    index = 35,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R_6R!H->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(18.9529,'m^3/(mol*s)'), n=1.91362, w0=(377.5,'kJ/mol'), E0=(72.3512,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R_6R!H->C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R_6R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R_6R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R_6R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 36,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(105.032,'m^3/(mol*s)'), n=1.7316, w0=(377.5,'kJ/mol'), E0=(59.8545,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2352097775278261, var=0.2936591510671025, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R_N-6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 1.6773518289528593"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R_N-6R!H->C
Total Standard Deviation in ln(k): 1.6773518289528593""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R_N-6R!H->C
Total Standard Deviation in ln(k): 1.6773518289528593
""",
)

entry(
    index = 37,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R_N-6R!H->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(36.5503,'m^3/(mol*s)'), n=1.87317, w0=(377.5,'kJ/mol'), E0=(57.1063,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R_N-6R!H->C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R_N-6R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R_N-6R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->Cl_Ext-4C-R_N-6R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 38,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(3.46661e-11,'m^3/(mol*s)'), n=5.3722, w0=(377.5,'kJ/mol'), E0=(21.4695,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0631962955883278, var=1.1814925550432194, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl',), comment="""BM rule fitted to 6 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 2.3378611972214327"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 2.3378611972214327""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 2.3378611972214327
""",
)

entry(
    index = 39,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C",
    kinetics = ArrheniusBM(A=(2.84152e-11,'m^3/(mol*s)'), n=5.39726, w0=(377.5,'kJ/mol'), E0=(17.7125,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0029269335592070123, var=1.8568362843455533, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C',), comment="""BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C
    Total Standard Deviation in ln(k): 2.7391219978343577"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C
Total Standard Deviation in ln(k): 2.7391219978343577""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C
Total Standard Deviation in ln(k): 2.7391219978343577
""",
)

entry(
    index = 40,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C_5CFO->C",
    kinetics = ArrheniusBM(A=(4.30856e-11,'m^3/(mol*s)'), n=5.36062, w0=(377.5,'kJ/mol'), E0=(14.9718,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.15813902881131384, var=3.3651584909989496, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C_5CFO->C',), comment="""BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C_5CFO->C
    Total Standard Deviation in ln(k): 4.074894107837656"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C_5CFO->C
Total Standard Deviation in ln(k): 4.074894107837656""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C_5CFO->C
Total Standard Deviation in ln(k): 4.074894107837656
""",
)

entry(
    index = 41,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C_5CFO->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(9.45261e-12,'m^3/(mol*s)'), n=5.55172, w0=(377.5,'kJ/mol'), E0=(5.02272,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3606929559212123, var=7.797089842776355, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C_5CFO->C_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C_5CFO->C_Ext-4C-R
    Total Standard Deviation in ln(k): 6.504139509463156"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C_5CFO->C_Ext-4C-R
Total Standard Deviation in ln(k): 6.504139509463156""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C_5CFO->C_Ext-4C-R
Total Standard Deviation in ln(k): 6.504139509463156
""",
)

entry(
    index = 42,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C_5CFO->C_Ext-4C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(30.3495,'m^3/(mol*s)'), n=1.95189, w0=(377.5,'kJ/mol'), E0=(74.2065,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C_5CFO->C_Ext-4C-R_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C_5CFO->C_Ext-4C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C_5CFO->C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C_5CFO->C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 43,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C_N-5CFO->C",
    kinetics = ArrheniusBM(A=(43.7292,'m^3/(mol*s)'), n=1.85998, w0=(377.5,'kJ/mol'), E0=(65.0469,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C_N-5CFO->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C_N-5CFO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C_N-5CFO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_Sp-5CFO-1C_N-5CFO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 44,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_N-Sp-5CFO-1C",
    kinetics = ArrheniusBM(A=(0.0219218,'m^3/(mol*s)'), n=2.84996, w0=(377.5,'kJ/mol'), E0=(49.3751,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3509448291920086, var=0.6878191117392113, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_N-Sp-5CFO-1C',), comment="""BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_N-Sp-5CFO-1C
    Total Standard Deviation in ln(k): 2.54439517122495"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_N-Sp-5CFO-1C
Total Standard Deviation in ln(k): 2.54439517122495""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_N-Sp-5CFO-1C
Total Standard Deviation in ln(k): 2.54439517122495
""",
)

entry(
    index = 45,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_N-Sp-5CFO-1C_5CFO->C",
    kinetics = ArrheniusBM(A=(45.5028,'m^3/(mol*s)'), n=1.93983, w0=(377.5,'kJ/mol'), E0=(57.9734,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_N-Sp-5CFO-1C_5CFO->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_N-Sp-5CFO-1C_5CFO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_N-Sp-5CFO-1C_5CFO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_N-Sp-5CFO-1C_5CFO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_N-Sp-5CFO-1C_N-5CFO->C",
    kinetics = ArrheniusBM(A=(68.8575,'m^3/(mol*s)'), n=1.80771, w0=(377.5,'kJ/mol'), E0=(59.1156,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_N-Sp-5CFO-1C_N-5CFO->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_N-Sp-5CFO-1C_N-5CFO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_N-Sp-5CFO-1C_N-5CFO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->Cl_N-Sp-5CFO-1C_N-5CFO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 47,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(0.000123059,'m^3/(mol*s)'), n=3.51531, w0=(377.5,'kJ/mol'), E0=(47.6848,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1338953470694557, var=1.12808033962407, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R',), comment="""BM rule fitted to 8 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 2.465672179427275"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 2.465672179427275""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 2.465672179427275
""",
)

entry(
    index = 48,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2.04962e-06,'m^3/(mol*s)'), n=4.02268, w0=(377.5,'kJ/mol'), E0=(45.1858,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1961450496075064, var=2.595726923419656, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C
    Total Standard Deviation in ln(k): 3.7227075240077716"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 3.7227075240077716""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 3.7227075240077716
""",
)

entry(
    index = 49,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C_Sp-5C-4C",
    kinetics = ArrheniusBM(A=(1.34152,'m^3/(mol*s)'), n=2.35829, w0=(377.5,'kJ/mol'), E0=(61.241,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2392492890249638, var=4.250055235487042, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C_Sp-5C-4C',), comment="""BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C_Sp-5C-4C
    Total Standard Deviation in ln(k): 4.734022961128598"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C_Sp-5C-4C
Total Standard Deviation in ln(k): 4.734022961128598""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C_Sp-5C-4C
Total Standard Deviation in ln(k): 4.734022961128598
""",
)

entry(
    index = 50,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C_Sp-5C-4C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(0.0201286,'m^3/(mol*s)'), n=2.88764, w0=(377.5,'kJ/mol'), E0=(52.6102,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.27127770748759755, var=11.312145116802764, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C_Sp-5C-4C_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C_Sp-5C-4C_Ext-4C-R
    Total Standard Deviation in ln(k): 7.424234527753133"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C_Sp-5C-4C_Ext-4C-R
Total Standard Deviation in ln(k): 7.424234527753133""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C_Sp-5C-4C_Ext-4C-R
Total Standard Deviation in ln(k): 7.424234527753133
""",
)

entry(
    index = 51,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(14.0202,'m^3/(mol*s)'), n=1.96824, w0=(377.5,'kJ/mol'), E0=(64.7938,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C_Sp-5C-4C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 52,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C_N-Sp-5C-4C",
    kinetics = ArrheniusBM(A=(43.2043,'m^3/(mol*s)'), n=1.91844, w0=(377.5,'kJ/mol'), E0=(74.5888,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C_N-Sp-5C-4C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C_N-Sp-5C-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C_N-Sp-5C-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_5R!H->C_N-Sp-5C-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 53,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(67.426,'m^3/(mol*s)'), n=1.87326, w0=(377.5,'kJ/mol'), E0=(61.4543,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2848241365299478, var=0.42960569809988525, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 2.0296283701384414"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 2.0296283701384414""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 2.0296283701384414
""",
)

entry(
    index = 54,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(57.1916,'m^3/(mol*s)'), n=1.89941, w0=(377.5,'kJ/mol'), E0=(58.5224,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.27751844588963204, var=0.9289435039664459, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 2.6294805817055322"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 2.6294805817055322""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 2.6294805817055322
""",
)

entry(
    index = 55,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(34.7298,'m^3/(mol*s)'), n=1.98737, w0=(377.5,'kJ/mol'), E0=(56.315,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 56,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C_5BrClFINOPSSi->F",
    kinetics = ArrheniusBM(A=(21.2149,'m^3/(mol*s)'), n=2.00716, w0=(377.5,'kJ/mol'), E0=(64.4355,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C_5BrClFINOPSSi->F',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C_5BrClFINOPSSi->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C_5BrClFINOPSSi->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C_5BrClFINOPSSi->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 57,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C_N-5BrClFINOPSSi->F",
    kinetics = ArrheniusBM(A=(28.5031,'m^3/(mol*s)'), n=1.97907, w0=(377.5,'kJ/mol'), E0=(61.3786,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C_N-5BrClFINOPSSi->F',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C_N-5BrClFINOPSSi->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C_N-5BrClFINOPSSi->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R_N-5R!H->C_N-5BrClFINOPSSi->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 58,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(6.04738,'m^3/(mol*s)'), n=2.13423, w0=(377.5,'kJ/mol'), E0=(60.9337,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.23296921159839126, var=0.5969982171627074, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C',), comment="""BM rule fitted to 21 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C
    Total Standard Deviation in ln(k): 2.1343215610281585"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C
Total Standard Deviation in ln(k): 2.1343215610281585""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C
Total Standard Deviation in ln(k): 2.1343215610281585
""",
)

entry(
    index = 59,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl",
    kinetics = ArrheniusBM(A=(1.10065,'m^3/(mol*s)'), n=2.34562, w0=(377.5,'kJ/mol'), E0=(56.2528,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.19108460837767144, var=0.6764118408868596, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl',), comment="""BM rule fitted to 14 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl
    Total Standard Deviation in ln(k): 2.1288916236234887"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl
Total Standard Deviation in ln(k): 2.1288916236234887""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl
Total Standard Deviation in ln(k): 2.1288916236234887
""",
)

entry(
    index = 60,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.84628,'m^3/(mol*s)'), n=2.28096, w0=(377.5,'kJ/mol'), E0=(56.4287,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.20767318122214976, var=0.7105321876327274, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R',), comment="""BM rule fitted to 13 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 2.211644681631511"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 2.211644681631511""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 2.211644681631511
""",
)

entry(
    index = 61,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(2900.89,'m^3/(mol*s)'), n=1.38212, w0=(377.5,'kJ/mol'), E0=(65.1067,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.24709391496755967, var=0.23015218609245378, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_5R!H->Cl',), comment="""BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_5R!H->Cl
    Total Standard Deviation in ln(k): 1.5825941789666835"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_5R!H->Cl
Total Standard Deviation in ln(k): 1.5825941789666835""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_5R!H->Cl
Total Standard Deviation in ln(k): 1.5825941789666835
""",
)

entry(
    index = 62,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1307.66,'m^3/(mol*s)'), n=1.48313, w0=(377.5,'kJ/mol'), E0=(62.238,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.23990289343606502, var=0.0918047260615839, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 1.2101916785187972"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 1.2101916785187972""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 1.2101916785187972
""",
)

entry(
    index = 63,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl",
    kinetics = ArrheniusBM(A=(179.007,'m^3/(mol*s)'), n=1.73491, w0=(377.5,'kJ/mol'), E0=(58.5179,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 64,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl",
    kinetics = ArrheniusBM(A=(120.578,'m^3/(mol*s)'), n=1.77539, w0=(377.5,'kJ/mol'), E0=(59.4028,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 65,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(9.02061e-06,'m^3/(mol*s)'), n=3.79757, w0=(377.5,'kJ/mol'), E0=(41.0721,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06605471591054306, var=0.7743806558454761, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl',), comment="""BM rule fitted to 10 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 1.9301114568230497"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 1.9301114568230497""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 1.9301114568230497
""",
)

entry(
    index = 66,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(212.326,'m^3/(mol*s)'), n=1.6665, w0=(377.5,'kJ/mol'), E0=(58.0124,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.34229530228558047, var=1.412572983162815, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C',), comment="""BM rule fitted to 5 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 3.2427004410805753"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 3.2427004410805753""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 3.2427004410805753
""",
)

entry(
    index = 67,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(302.582,'m^3/(mol*s)'), n=1.60363, w0=(377.5,'kJ/mol'), E0=(57.1888,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.34186584228000405, var=2.149747685655175, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R',), comment="""BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R
    Total Standard Deviation in ln(k): 3.798305559378503"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R
Total Standard Deviation in ln(k): 3.798305559378503""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R
Total Standard Deviation in ln(k): 3.798305559378503
""",
)

entry(
    index = 68,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R",
    kinetics = ArrheniusBM(A=(183.986,'m^3/(mol*s)'), n=1.77285, w0=(377.5,'kJ/mol'), E0=(56.8752,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3222175853065505, var=6.5136130954371705, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R',), comment="""BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R
    Total Standard Deviation in ln(k): 5.926032899935359"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R
Total Standard Deviation in ln(k): 5.926032899935359""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R
Total Standard Deviation in ln(k): 5.926032899935359
""",
)

entry(
    index = 69,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(41.157,'m^3/(mol*s)'), n=1.86255, w0=(377.5,'kJ/mol'), E0=(57.4087,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 70,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(163.845,'m^3/(mol*s)'), n=1.8839, w0=(377.5,'kJ/mol'), E0=(54.4923,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 71,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(24.8273,'m^3/(mol*s)'), n=1.88378, w0=(377.5,'kJ/mol'), E0=(58.5286,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 72,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(17440.8,'m^3/(mol*s)'), n=0.915521, w0=(377.5,'kJ/mol'), E0=(57.1047,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 73,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(4.60693,'m^3/(mol*s)'), n=2.18106, w0=(377.5,'kJ/mol'), E0=(63.1102,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2497255497440884, var=0.5011957097798698, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C',), comment="""BM rule fitted to 5 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 2.0467068780377606"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 2.0467068780377606""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 2.0467068780377606
""",
)

entry(
    index = 74,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.80928,'m^3/(mol*s)'), n=2.22816, w0=(377.5,'kJ/mol'), E0=(60.5169,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2537892144591133, var=0.5468567014103751, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Ext-1C-R
    Total Standard Deviation in ln(k): 2.1201581225925965"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 2.1201581225925965""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 2.1201581225925965
""",
)

entry(
    index = 75,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Ext-1C-R_5FO->O",
    kinetics = ArrheniusBM(A=(185.874,'m^3/(mol*s)'), n=1.75948, w0=(377.5,'kJ/mol'), E0=(69.4855,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Ext-1C-R_5FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Ext-1C-R_5FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Ext-1C-R_5FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Ext-1C-R_5FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 76,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Ext-1C-R_N-5FO->O",
    kinetics = ArrheniusBM(A=(84.18,'m^3/(mol*s)'), n=1.82792, w0=(377.5,'kJ/mol'), E0=(60.5485,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Ext-1C-R_N-5FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Ext-1C-R_N-5FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Ext-1C-R_N-5FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Ext-1C-R_N-5FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 77,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C",
    kinetics = ArrheniusBM(A=(4.2966,'m^3/(mol*s)'), n=2.17487, w0=(377.5,'kJ/mol'), E0=(64.7641,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.32813388838578084, var=2.3032276154566196, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C',), comment="""BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C
    Total Standard Deviation in ln(k): 3.8669208014171277"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C
Total Standard Deviation in ln(k): 3.8669208014171277""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C
Total Standard Deviation in ln(k): 3.8669208014171277
""",
)

entry(
    index = 78,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_5FO->O",
    kinetics = ArrheniusBM(A=(52.0355,'m^3/(mol*s)'), n=1.85451, w0=(377.5,'kJ/mol'), E0=(72.1297,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_5FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_5FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_5FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_5FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 79,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_N-5FO->O",
    kinetics = ArrheniusBM(A=(40.2856,'m^3/(mol*s)'), n=1.90639, w0=(377.5,'kJ/mol'), E0=(63.2876,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_N-5FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_N-5FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_N-5FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_N-5FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 80,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_N-Sp-5FO-1C",
    kinetics = ArrheniusBM(A=(67.2815,'m^3/(mol*s)'), n=1.83026, w0=(377.5,'kJ/mol'), E0=(67.7675,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_N-Sp-5FO-1C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_N-Sp-5FO-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_N-Sp-5FO-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_4BrClFO->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_N-Sp-5FO-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 81,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl",
    kinetics = ArrheniusBM(A=(1.18709,'m^3/(mol*s)'), n=2.33804, w0=(377.5,'kJ/mol'), E0=(63.7096,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.22374231782283832, var=0.2108076454393995, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl',), comment="""BM rule fitted to 7 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl
    Total Standard Deviation in ln(k): 1.4826165559006175"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl
Total Standard Deviation in ln(k): 1.4826165559006175""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl
Total Standard Deviation in ln(k): 1.4826165559006175
""",
)

entry(
    index = 82,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_4BrFO->O",
    kinetics = ArrheniusBM(A=(28.207,'m^3/(mol*s)'), n=1.91432, w0=(377.5,'kJ/mol'), E0=(60.9389,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_4BrFO->O',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_4BrFO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_4BrFO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_4BrFO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 83,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O",
    kinetics = ArrheniusBM(A=(0.756588,'m^3/(mol*s)'), n=2.39901, w0=(377.5,'kJ/mol'), E0=(64.2621,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2288426979434886, var=0.1663094860786253, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O',), comment="""BM rule fitted to 6 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O
    Total Standard Deviation in ln(k): 1.3925338693676457"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O
Total Standard Deviation in ln(k): 1.3925338693676457""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O
Total Standard Deviation in ln(k): 1.3925338693676457
""",
)

entry(
    index = 84,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_4BrF->Br",
    kinetics = ArrheniusBM(A=(22.8943,'m^3/(mol*s)'), n=1.98539, w0=(377.5,'kJ/mol'), E0=(72.2861,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2556636615189453, var=0.40459050363563204, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_4BrF->Br',), comment="""BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_4BrF->Br
    Total Standard Deviation in ln(k): 1.9175314517818993"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_4BrF->Br
Total Standard Deviation in ln(k): 1.9175314517818993""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_4BrF->Br
Total Standard Deviation in ln(k): 1.9175314517818993
""",
)

entry(
    index = 85,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_4BrF->Br_Ext-1C-R",
    kinetics = ArrheniusBM(A=(71.139,'m^3/(mol*s)'), n=1.83301, w0=(377.5,'kJ/mol'), E0=(70.4116,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_4BrF->Br_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_4BrF->Br_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_4BrF->Br_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_4BrF->Br_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 86,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br",
    kinetics = ArrheniusBM(A=(20.6469,'m^3/(mol*s)'), n=1.98223, w0=(377.5,'kJ/mol'), E0=(66.3166,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.28929266080326765, var=0.12899178459488977, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br',), comment="""BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br
    Total Standard Deviation in ln(k): 1.4468751310485113"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br
Total Standard Deviation in ln(k): 1.4468751310485113""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br
Total Standard Deviation in ln(k): 1.4468751310485113
""",
)

entry(
    index = 87,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br_Ext-1C-R",
    kinetics = ArrheniusBM(A=(27.678,'m^3/(mol*s)'), n=1.94701, w0=(377.5,'kJ/mol'), E0=(66.1996,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3264295656670953, var=0.2343046538674139, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br_Ext-1C-R
    Total Standard Deviation in ln(k): 1.7905673228507488"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br_Ext-1C-R
Total Standard Deviation in ln(k): 1.7905673228507488""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br_Ext-1C-R
Total Standard Deviation in ln(k): 1.7905673228507488
""",
)

entry(
    index = 88,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(73.4575,'m^3/(mol*s)'), n=1.82774, w0=(377.5,'kJ/mol'), E0=(64.0942,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 89,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br_Ext-1C-R_5R!H->O",
    kinetics = ArrheniusBM(A=(52.0663,'m^3/(mol*s)'), n=1.89167, w0=(377.5,'kJ/mol'), E0=(71.1751,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br_Ext-1C-R_5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br_Ext-1C-R_5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br_Ext-1C-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br_Ext-1C-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 90,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br_Ext-1C-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(34.4569,'m^3/(mol*s)'), n=1.89428, w0=(377.5,'kJ/mol'), E0=(65.4658,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br_Ext-1C-R_N-5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br_Ext-1C-R_N-5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br_Ext-1C-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C_N-4BrClFO->Cl_N-4BrFO->O_N-4BrF->Br_Ext-1C-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 91,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(2.39651e-14,'m^3/(mol*s)'), n=6.37242, w0=(377.5,'kJ/mol'), E0=(20.7241,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0252052905086953, var=2.7010150214527795, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C',), comment="""BM rule fitted to 8 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C
    Total Standard Deviation in ln(k): 3.3580648734658163"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 3.3580648734658163""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 3.3580648734658163
""",
)

entry(
    index = 92,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C",
    kinetics = ArrheniusBM(A=(2.88599e-12,'m^3/(mol*s)'), n=5.70893, w0=(377.5,'kJ/mol'), E0=(27.4415,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1000755743252786, var=1.4362013247992034, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C',), comment="""BM rule fitted to 7 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C
    Total Standard Deviation in ln(k): 2.653953106888688"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C
Total Standard Deviation in ln(k): 2.653953106888688""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C
Total Standard Deviation in ln(k): 2.653953106888688
""",
)

entry(
    index = 93,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C",
    kinetics = ArrheniusBM(A=(2.75037e-12,'m^3/(mol*s)'), n=5.72477, w0=(377.5,'kJ/mol'), E0=(27.7449,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.23205909743532752, var=2.1891787499194835, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C
    Total Standard Deviation in ln(k): 3.5492437355112543"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C
Total Standard Deviation in ln(k): 3.5492437355112543""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C
Total Standard Deviation in ln(k): 3.5492437355112543
""",
)

entry(
    index = 94,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_5R!H->F",
    kinetics = ArrheniusBM(A=(23993.5,'m^3/(mol*s)'), n=0.953042, w0=(377.5,'kJ/mol'), E0=(64.7432,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 95,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(1.96069e-13,'m^3/(mol*s)'), n=6.0943, w0=(377.5,'kJ/mol'), E0=(24.8463,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3393380537055749, var=2.605995550680641, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F',), comment="""BM rule fitted to 5 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F
    Total Standard Deviation in ln(k): 4.08887129703256"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F
Total Standard Deviation in ln(k): 4.08887129703256""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F
Total Standard Deviation in ln(k): 4.08887129703256
""",
)

entry(
    index = 96,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C",
    kinetics = ArrheniusBM(A=(57.3259,'m^3/(mol*s)'), n=1.9463, w0=(377.5,'kJ/mol'), E0=(61.8464,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.26709769222689106, var=0.9244166911742336, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C',), comment="""BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C
    Total Standard Deviation in ln(k): 2.5985841595818595"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C
Total Standard Deviation in ln(k): 2.5985841595818595""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C
Total Standard Deviation in ln(k): 2.5985841595818595
""",
)

entry(
    index = 97,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_5BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(53.4862,'m^3/(mol*s)'), n=1.91684, w0=(377.5,'kJ/mol'), E0=(62.7585,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.23345985449748885, var=0.20411813389032354, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_5BrCClINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_5BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 1.4923105284236908"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_5BrCClINOPSSi->C
Total Standard Deviation in ln(k): 1.4923105284236908""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_5BrCClINOPSSi->C
Total Standard Deviation in ln(k): 1.4923105284236908
""",
)

entry(
    index = 98,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_5BrCClINOPSSi->C_Ext-4C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(74.2968,'m^3/(mol*s)'), n=1.88465, w0=(377.5,'kJ/mol'), E0=(62.3679,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_5BrCClINOPSSi->C_Ext-4C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_5BrCClINOPSSi->C_Ext-4C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_5BrCClINOPSSi->C_Ext-4C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_5BrCClINOPSSi->C_Ext-4C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 99,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_5BrCClINOPSSi->C_Ext-4C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(57.7168,'m^3/(mol*s)'), n=1.89866, w0=(377.5,'kJ/mol'), E0=(63.5957,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_5BrCClINOPSSi->C_Ext-4C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_5BrCClINOPSSi->C_Ext-4C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_5BrCClINOPSSi->C_Ext-4C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_5BrCClINOPSSi->C_Ext-4C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 100,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_N-5BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(60.0054,'m^3/(mol*s)'), n=1.97871, w0=(377.5,'kJ/mol'), E0=(60.9075,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.30403209069386183, var=4.04037422921823, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_N-5BrCClINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_N-5BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 4.793553984059097"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_N-5BrCClINOPSSi->C
Total Standard Deviation in ln(k): 4.793553984059097""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_N-5BrCClINOPSSi->C
Total Standard Deviation in ln(k): 4.793553984059097
""",
)

entry(
    index = 101,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_N-5BrCClINOPSSi->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(126.882,'m^3/(mol*s)'), n=1.93859, w0=(377.5,'kJ/mol'), E0=(58.8144,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_N-5BrCClINOPSSi->C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_N-5BrCClINOPSSi->C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_N-5BrCClINOPSSi->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_Sp-5BrCClINOPSSi-4C_N-5BrCClINOPSSi->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 102,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_N-Sp-5BrCClINOPSSi-4C",
    kinetics = ArrheniusBM(A=(30.5257,'m^3/(mol*s)'), n=2.04125, w0=(377.5,'kJ/mol'), E0=(90.202,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_N-Sp-5BrCClINOPSSi-4C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_N-Sp-5BrCClINOPSSi-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_N-Sp-5BrCClINOPSSi-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_4R!H->C_Ext-4C-R_N-5R!H->F_N-Sp-5BrCClINOPSSi-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 103,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(24.0657,'m^3/(mol*s)'), n=1.94769, w0=(377.5,'kJ/mol'), E0=(66.4621,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_Sp-4R!H=1C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 104,
    label = "Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_N-Sp-4R!H=1C",
    kinetics = ArrheniusBM(A=(0.00424845,'m^3/(mol*s)'), n=3.63506, w0=(377.5,'kJ/mol'), E0=(56.9157,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_N-Sp-4R!H=1C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_N-Sp-4R!H=1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_N-Sp-4R!H=1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_N-Sp-4R!H=1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 105,
    label = "Root_3R->H_1R->C_N-1C-u0",
    kinetics = ArrheniusBM(A=(2.30375e-17,'m^3/(mol*s)'), n=7.07338, w0=(377.5,'kJ/mol'), E0=(4.27017,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1271009841950513, var=2.322796766278457, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_3R->H_1R->C_N-1C-u0',), comment="""BM rule fitted to 8 training reactions at node Root_3R->H_1R->C_N-1C-u0
    Total Standard Deviation in ln(k): 3.37471066374245"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_3R->H_1R->C_N-1C-u0
Total Standard Deviation in ln(k): 3.37471066374245""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_3R->H_1R->C_N-1C-u0
Total Standard Deviation in ln(k): 3.37471066374245
""",
)

entry(
    index = 106,
    label = "Root_3R->H_1R->C_N-1C-u0_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.43121e-16,'m^3/(mol*s)'), n=6.85865, w0=(377.5,'kJ/mol'), E0=(5.62902,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2394770852933179, var=2.055676078404911, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_3R->H_1R->C_N-1C-u0_Ext-1C-R',), comment="""BM rule fitted to 7 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R
    Total Standard Deviation in ln(k): 3.47601601509616"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 3.47601601509616""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 3.47601601509616
""",
)

entry(
    index = 107,
    label = "Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O",
    kinetics = ArrheniusBM(A=(3.57195,'m^3/(mol*s)'), n=2.18024, w0=(377.5,'kJ/mol'), E0=(48.1417,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.36887145755025913, var=3.0772055601041464, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O',), comment="""BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O
    Total Standard Deviation in ln(k): 4.443512077596634"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O
Total Standard Deviation in ln(k): 4.443512077596634""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O
Total Standard Deviation in ln(k): 4.443512077596634
""",
)

entry(
    index = 108,
    label = "Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(358.916,'m^3/(mol*s)'), n=1.60172, w0=(377.5,'kJ/mol'), E0=(47.9534,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.39325833118785725, var=0.8269102670824383, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R
    Total Standard Deviation in ln(k): 2.811084214531041"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 2.811084214531041""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 2.811084214531041
""",
)

entry(
    index = 109,
    label = "Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(36.3214,'m^3/(mol*s)'), n=1.83646, w0=(377.5,'kJ/mol'), E0=(48.2445,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R_5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R_5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 110,
    label = "Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(183.661,'m^3/(mol*s)'), n=1.71023, w0=(377.5,'kJ/mol'), E0=(45.8384,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.40249109614608936, var=0.5568489316027914, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R_N-5R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 2.507263807640092"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 2.507263807640092""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 2.507263807640092
""",
)

entry(
    index = 111,
    label = "Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(34.0466,'m^3/(mol*s)'), n=1.832, w0=(377.5,'kJ/mol'), E0=(35.2329,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 112,
    label = "Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(82.3604,'m^3/(mol*s)'), n=1.89796, w0=(377.5,'kJ/mol'), E0=(53.5639,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_4R!H->O_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 113,
    label = "Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(1.5387e-16,'m^3/(mol*s)'), n=6.82348, w0=(377.5,'kJ/mol'), E0=(18.7676,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3963142756183935, var=2.6383616134684145, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_N-4R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_N-4R!H->O
    Total Standard Deviation in ln(k): 4.252062562182656"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_N-4R!H->O
Total Standard Deviation in ln(k): 4.252062562182656""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_N-4R!H->O
Total Standard Deviation in ln(k): 4.252062562182656
""",
)

entry(
    index = 114,
    label = "Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_N-4R!H->O_Ext-4BrCClFINPSSi-R",
    kinetics = ArrheniusBM(A=(23.5466,'m^3/(mol*s)'), n=1.8421, w0=(377.5,'kJ/mol'), E0=(65.7601,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_N-4R!H->O_Ext-4BrCClFINPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_N-4R!H->O_Ext-4BrCClFINPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_N-4R!H->O_Ext-4BrCClFINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_N-4R!H->O_Ext-4BrCClFINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 115,
    label = "Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_N-4R!H->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(42.4593,'m^3/(mol*s)'), n=1.81356, w0=(377.5,'kJ/mol'), E0=(81.7579,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_N-4R!H->O_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_N-4R!H->O_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_N-4R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_1R->C_N-1C-u0_Ext-1C-R_N-4R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 116,
    label = "Root_3R->H_N-1R->C",
    kinetics = ArrheniusBM(A=(1186.89,'m^3/(mol*s)'), n=1.61789, w0=(350,'kJ/mol'), E0=(63.7949,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5036957819591996, var=3.592561360036192, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_3R->H_N-1R->C',), comment="""BM rule fitted to 5 training reactions at node Root_3R->H_N-1R->C
    Total Standard Deviation in ln(k): 5.065352839664528"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_3R->H_N-1R->C
Total Standard Deviation in ln(k): 5.065352839664528""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_3R->H_N-1R->C
Total Standard Deviation in ln(k): 5.065352839664528
""",
)

entry(
    index = 117,
    label = "Root_3R->H_N-1R->C_1BrClFHO-u0",
    kinetics = ArrheniusBM(A=(84.2393,'m^3/(mol*s)'), n=1.99904, w0=(350,'kJ/mol'), E0=(41.5049,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03149390873228127, var=0.4298160499359183, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_3R->H_N-1R->C_1BrClFHO-u0',), comment="""BM rule fitted to 4 training reactions at node Root_3R->H_N-1R->C_1BrClFHO-u0
    Total Standard Deviation in ln(k): 1.393441911261586"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_3R->H_N-1R->C_1BrClFHO-u0
Total Standard Deviation in ln(k): 1.393441911261586""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_3R->H_N-1R->C_1BrClFHO-u0
Total Standard Deviation in ln(k): 1.393441911261586
""",
)

entry(
    index = 118,
    label = "Root_3R->H_N-1R->C_1BrClFHO-u0_Ext-1BrClFHO-R",
    kinetics = ArrheniusBM(A=(36.2707,'m^3/(mol*s)'), n=2.10136, w0=(350,'kJ/mol'), E0=(42.0277,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0015464718316186169, var=0.7044475996462057, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3R->H_N-1R->C_1BrClFHO-u0_Ext-1BrClFHO-R',), comment="""BM rule fitted to 3 training reactions at node Root_3R->H_N-1R->C_1BrClFHO-u0_Ext-1BrClFHO-R
    Total Standard Deviation in ln(k): 1.6864873574654329"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3R->H_N-1R->C_1BrClFHO-u0_Ext-1BrClFHO-R
Total Standard Deviation in ln(k): 1.6864873574654329""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3R->H_N-1R->C_1BrClFHO-u0_Ext-1BrClFHO-R
Total Standard Deviation in ln(k): 1.6864873574654329
""",
)

entry(
    index = 119,
    label = "Root_3R->H_N-1R->C_1BrClFHO-u0_Ext-1BrClFHO-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(127.005,'m^3/(mol*s)'), n=1.91628, w0=(350,'kJ/mol'), E0=(40.0647,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6418005097333057, var=5.44534466252004, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->H_N-1R->C_1BrClFHO-u0_Ext-1BrClFHO-R_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_3R->H_N-1R->C_1BrClFHO-u0_Ext-1BrClFHO-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 6.290665980570672"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->H_N-1R->C_1BrClFHO-u0_Ext-1BrClFHO-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 6.290665980570672""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->H_N-1R->C_1BrClFHO-u0_Ext-1BrClFHO-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 6.290665980570672
""",
)

entry(
    index = 120,
    label = "Root_3R->H_N-1R->C_1BrClFHO-u0_Ext-1BrClFHO-R_Ext-4R!H-R_Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(2761.89,'m^3/(mol*s)'), n=1.54753, w0=(350,'kJ/mol'), E0=(55.4059,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_N-1R->C_1BrClFHO-u0_Ext-1BrClFHO-R_Ext-4R!H-R_Sp-5R!H-4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_N-1R->C_1BrClFHO-u0_Ext-1BrClFHO-R_Ext-4R!H-R_Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_N-1R->C_1BrClFHO-u0_Ext-1BrClFHO-R_Ext-4R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_N-1R->C_1BrClFHO-u0_Ext-1BrClFHO-R_Ext-4R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 121,
    label = "Root_3R->H_N-1R->C_1BrClFHO-u0_Ext-1BrClFHO-R_Ext-4R!H-R_N-Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(686.74,'m^3/(mol*s)'), n=1.69184, w0=(350,'kJ/mol'), E0=(90.2703,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_N-1R->C_1BrClFHO-u0_Ext-1BrClFHO-R_Ext-4R!H-R_N-Sp-5R!H-4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_N-1R->C_1BrClFHO-u0_Ext-1BrClFHO-R_Ext-4R!H-R_N-Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_N-1R->C_1BrClFHO-u0_Ext-1BrClFHO-R_Ext-4R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_N-1R->C_1BrClFHO-u0_Ext-1BrClFHO-R_Ext-4R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 122,
    label = "Root_3R->H_N-1R->C_N-1BrClFHO-u0",
    kinetics = ArrheniusBM(A=(5996.23,'m^3/(mol*s)'), n=1.20842, w0=(350,'kJ/mol'), E0=(67.1609,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_N-1R->C_N-1BrClFHO-u0',), comment="""BM rule fitted to 1 training reactions at node Root_3R->H_N-1R->C_N-1BrClFHO-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->H_N-1R->C_N-1BrClFHO-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->H_N-1R->C_N-1BrClFHO-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 123,
    label = "Root_N-3R->H",
    kinetics = ArrheniusBM(A=(3.7634e+07,'m^3/(mol*s)'), n=-0.234634, w0=(323.258,'kJ/mol'), E0=(81.0599,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.15924234251966932, var=9.737500677133058, Tref=1000.0, N=398, data_mean=0.0, correlation='Root_N-3R->H',), comment="""BM rule fitted to 398 training reactions at node Root_N-3R->H
    Total Standard Deviation in ln(k): 6.6558759100459755"""),
    rank = 11,
    shortDesc = """BM rule fitted to 398 training reactions at node Root_N-3R->H
Total Standard Deviation in ln(k): 6.6558759100459755""",
    longDesc = 
"""
BM rule fitted to 398 training reactions at node Root_N-3R->H
Total Standard Deviation in ln(k): 6.6558759100459755
""",
)

entry(
    index = 124,
    label = "Root_N-3R->H_1R->H",
    kinetics = ArrheniusBM(A=(0.66111,'m^3/(mol*s)'), n=1.84399, w0=(375.737,'kJ/mol'), E0=(69.9049,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.625593259901317, var=3.8307551619805063, Tref=1000.0, N=78, data_mean=0.0, correlation='Root_N-3R->H_1R->H',), comment="""BM rule fitted to 78 training reactions at node Root_N-3R->H_1R->H
    Total Standard Deviation in ln(k): 5.495573013096975"""),
    rank = 11,
    shortDesc = """BM rule fitted to 78 training reactions at node Root_N-3R->H_1R->H
Total Standard Deviation in ln(k): 5.495573013096975""",
    longDesc = 
"""
BM rule fitted to 78 training reactions at node Root_N-3R->H_1R->H
Total Standard Deviation in ln(k): 5.495573013096975
""",
)

entry(
    index = 125,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(4.54483e-16,'m^3/(mol*s)'), n=6.16015, w0=(377.5,'kJ/mol'), E0=(-16.6148,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.3033046520116665, var=1.305635355405709, Tref=1000.0, N=73, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C',), comment="""BM rule fitted to 73 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 5.565333351009197"""),
    rank = 11,
    shortDesc = """BM rule fitted to 73 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 5.565333351009197""",
    longDesc = 
"""
BM rule fitted to 73 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 5.565333351009197
""",
)

entry(
    index = 126,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1",
    kinetics = ArrheniusBM(A=(1.53833e-14,'m^3/(mol*s)'), n=5.67724, w0=(377.5,'kJ/mol'), E0=(22.6764,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.2471289139486947, var=1.1444376215982333, Tref=1000.0, N=65, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1',), comment="""BM rule fitted to 65 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1
    Total Standard Deviation in ln(k): 5.278123070178778"""),
    rank = 11,
    shortDesc = """BM rule fitted to 65 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1
Total Standard Deviation in ln(k): 5.278123070178778""",
    longDesc = 
"""
BM rule fitted to 65 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1
Total Standard Deviation in ln(k): 5.278123070178778
""",
)

entry(
    index = 127,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.53021e-14,'m^3/(mol*s)'), n=5.67476, w0=(377.5,'kJ/mol'), E0=(22.6953,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.2561367027783432, var=1.1524625762645666, Tref=1000.0, N=64, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R',), comment="""BM rule fitted to 64 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R
    Total Standard Deviation in ln(k): 5.308261802549391"""),
    rank = 11,
    shortDesc = """BM rule fitted to 64 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R
Total Standard Deviation in ln(k): 5.308261802549391""",
    longDesc = 
"""
BM rule fitted to 64 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R
Total Standard Deviation in ln(k): 5.308261802549391
""",
)

entry(
    index = 128,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(2.68662e-13,'m^3/(mol*s)'), n=5.24475, w0=(377.5,'kJ/mol'), E0=(26.1497,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.2877532680286625, var=1.4702317105310077, Tref=1000.0, N=28, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl',), comment="""BM rule fitted to 28 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl
    Total Standard Deviation in ln(k): 5.666364638320716"""),
    rank = 11,
    shortDesc = """BM rule fitted to 28 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl
Total Standard Deviation in ln(k): 5.666364638320716""",
    longDesc = 
"""
BM rule fitted to 28 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl
Total Standard Deviation in ln(k): 5.666364638320716
""",
)

entry(
    index = 129,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.91208e-13,'m^3/(mol*s)'), n=5.24164, w0=(377.5,'kJ/mol'), E0=(26.3832,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.3018795530833995, var=1.3667477423359082, Tref=1000.0, N=27, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R',), comment="""BM rule fitted to 27 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R
    Total Standard Deviation in ln(k): 5.6147495770516755"""),
    rank = 11,
    shortDesc = """BM rule fitted to 27 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 5.6147495770516755""",
    longDesc = 
"""
BM rule fitted to 27 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 5.6147495770516755
""",
)

entry(
    index = 130,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(3.76634e-12,'m^3/(mol*s)'), n=4.82531, w0=(377.5,'kJ/mol'), E0=(-3.85399,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.4109049778014187, var=2.498192180654313, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl',), comment="""BM rule fitted to 10 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl
    Total Standard Deviation in ln(k): 6.713605576738383"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl
Total Standard Deviation in ln(k): 6.713605576738383""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl
Total Standard Deviation in ln(k): 6.713605576738383
""",
)

entry(
    index = 131,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.72773e-12,'m^3/(mol*s)'), n=4.85341, w0=(377.5,'kJ/mol'), E0=(-7.45528,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.3799308063629505, var=3.1887950365197986, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R
    Total Standard Deviation in ln(k): 7.047057857441339"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 7.047057857441339""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 7.047057857441339
""",
)

entry(
    index = 132,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_6R!H->F",
    kinetics = ArrheniusBM(A=(0.000241839,'m^3/(mol*s)'), n=2.71215, w0=(377.5,'kJ/mol'), E0=(57.8815,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_6R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_6R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 133,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F",
    kinetics = ArrheniusBM(A=(5.18022e-06,'m^3/(mol*s)'), n=3.03754, w0=(377.5,'kJ/mol'), E0=(63.4293,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.0940832248724288, var=3.406632669750059, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F',), comment="""BM rule fitted to 8 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F
    Total Standard Deviation in ln(k): 6.449105490237005"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F
Total Standard Deviation in ln(k): 6.449105490237005""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F
Total Standard Deviation in ln(k): 6.449105490237005
""",
)

entry(
    index = 134,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R",
    kinetics = ArrheniusBM(A=(8.55076e-09,'m^3/(mol*s)'), n=3.8185, w0=(377.5,'kJ/mol'), E0=(56.9887,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.2768975237332107, var=3.1996689236642095, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R
    Total Standard Deviation in ln(k): 6.794278843181372"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R
Total Standard Deviation in ln(k): 6.794278843181372""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R
Total Standard Deviation in ln(k): 6.794278843181372
""",
)

entry(
    index = 135,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R",
    kinetics = ArrheniusBM(A=(6.84359e-07,'m^3/(mol*s)'), n=3.26681, w0=(377.5,'kJ/mol'), E0=(67.1487,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.0377705637351111, var=2.924007828377328, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R
    Total Standard Deviation in ln(k): 6.035506680748168"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R
Total Standard Deviation in ln(k): 6.035506680748168""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R
Total Standard Deviation in ln(k): 6.035506680748168
""",
)

entry(
    index = 136,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_7R!H->C",
    kinetics = ArrheniusBM(A=(1.19416e-05,'m^3/(mol*s)'), n=2.93744, w0=(377.5,'kJ/mol'), E0=(63.1208,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.9720890801355242, var=0.08029255176105139, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_7R!H->C
    Total Standard Deviation in ln(k): 3.0104954111582467"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_7R!H->C
Total Standard Deviation in ln(k): 3.0104954111582467""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_7R!H->C
Total Standard Deviation in ln(k): 3.0104954111582467
""",
)

entry(
    index = 137,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_7R!H->C_8R!H->F",
    kinetics = ArrheniusBM(A=(5.75008e-06,'m^3/(mol*s)'), n=2.92375, w0=(377.5,'kJ/mol'), E0=(51.8515,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_7R!H->C_8R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_7R!H->C_8R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_7R!H->C_8R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_7R!H->C_8R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 138,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_7R!H->C_N-8R!H->F",
    kinetics = ArrheniusBM(A=(0.000248607,'m^3/(mol*s)'), n=2.66431, w0=(377.5,'kJ/mol'), E0=(76.5707,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_7R!H->C_N-8R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_7R!H->C_N-8R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_7R!H->C_N-8R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_7R!H->C_N-8R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 139,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(2.87604e-06,'m^3/(mol*s)'), n=3.07055, w0=(377.5,'kJ/mol'), E0=(74.3578,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.0252636039784269, var=5.5726345406040565, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_N-7R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_N-7R!H->C
    Total Standard Deviation in ln(k): 7.3085026796413"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_N-7R!H->C
Total Standard Deviation in ln(k): 7.3085026796413""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_N-7R!H->C
Total Standard Deviation in ln(k): 7.3085026796413
""",
)

entry(
    index = 140,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_N-7R!H->C_Ext-6BrCClINOPSSi-R",
    kinetics = ArrheniusBM(A=(1.35152e-06,'m^3/(mol*s)'), n=3.09757, w0=(377.5,'kJ/mol'), E0=(75.2704,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.066141420890183, var=10.397861632572551, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_N-7R!H->C_Ext-6BrCClINOPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_N-7R!H->C_Ext-6BrCClINOPSSi-R
    Total Standard Deviation in ln(k): 9.143158969445587"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_N-7R!H->C_Ext-6BrCClINOPSSi-R
Total Standard Deviation in ln(k): 9.143158969445587""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_N-7R!H->C_Ext-6BrCClINOPSSi-R
Total Standard Deviation in ln(k): 9.143158969445587
""",
)

entry(
    index = 141,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_N-7R!H->C_Ext-6BrCClINOPSSi-R_7ClF->F",
    kinetics = ArrheniusBM(A=(5.0283e-06,'m^3/(mol*s)'), n=3.08625, w0=(377.5,'kJ/mol'), E0=(76.1339,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_N-7R!H->C_Ext-6BrCClINOPSSi-R_7ClF->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_N-7R!H->C_Ext-6BrCClINOPSSi-R_7ClF->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_N-7R!H->C_Ext-6BrCClINOPSSi-R_7ClF->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_N-7R!H->C_Ext-6BrCClINOPSSi-R_7ClF->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 142,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_N-7R!H->C_Ext-6BrCClINOPSSi-R_N-7ClF->F",
    kinetics = ArrheniusBM(A=(2.16928e-07,'m^3/(mol*s)'), n=3.17306, w0=(377.5,'kJ/mol'), E0=(73.7073,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_N-7R!H->C_Ext-6BrCClINOPSSi-R_N-7ClF->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_N-7R!H->C_Ext-6BrCClINOPSSi-R_N-7ClF->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_N-7R!H->C_Ext-6BrCClINOPSSi-R_N-7ClF->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_Ext-6BrCClINOPSSi-R_Ext-6BrCClINOPSSi-R_N-7R!H->C_Ext-6BrCClINOPSSi-R_N-7ClF->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 143,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(2.47693e-06,'m^3/(mol*s)'), n=3.10583, w0=(377.5,'kJ/mol'), E0=(55.0109,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 144,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_N-6BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.000185734,'m^3/(mol*s)'), n=2.71297, w0=(377.5,'kJ/mol'), E0=(56.6127,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_N-6BrCClINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_N-6BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_N-6BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_N-6BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 145,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(1.24318e-09,'m^3/(mol*s)'), n=4.25904, w0=(377.5,'kJ/mol'), E0=(44.3335,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.9826555816973266, var=0.9513057804531725, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl',), comment="""BM rule fitted to 17 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 4.4243003382746515"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 4.4243003382746515""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 4.4243003382746515
""",
)

entry(
    index = 146,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C",
    kinetics = ArrheniusBM(A=(0.000371684,'m^3/(mol*s)'), n=2.70005, w0=(377.5,'kJ/mol'), E0=(63.9651,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7910111619951474, var=1.3754235622575262, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C',), comment="""BM rule fitted to 11 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C
    Total Standard Deviation in ln(k): 4.3385875238820875"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 4.3385875238820875""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 4.3385875238820875
""",
)

entry(
    index = 147,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(0.0222899,'m^3/(mol*s)'), n=2.10769, w0=(377.5,'kJ/mol'), E0=(70.186,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6511673342739458, var=0.980104128170539, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 3.6207907361913843"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R
Total Standard Deviation in ln(k): 3.6207907361913843""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R
Total Standard Deviation in ln(k): 3.6207907361913843
""",
)

entry(
    index = 148,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_Ext-5BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(0.0170575,'m^3/(mol*s)'), n=2.13501, w0=(377.5,'kJ/mol'), E0=(68.4744,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6475347856133409, var=1.2164392062794156, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_Ext-5BrCFINOPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_Ext-5BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 3.838040305579684"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_Ext-5BrCFINOPSSi-R
Total Standard Deviation in ln(k): 3.838040305579684""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_Ext-5BrCFINOPSSi-R
Total Standard Deviation in ln(k): 3.838040305579684
""",
)

entry(
    index = 149,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_Ext-5BrCFINOPSSi-R_6R!H->C",
    kinetics = ArrheniusBM(A=(0.00141887,'m^3/(mol*s)'), n=2.48484, w0=(377.5,'kJ/mol'), E0=(71.641,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_Ext-5BrCFINOPSSi-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_Ext-5BrCFINOPSSi-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_Ext-5BrCFINOPSSi-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_Ext-5BrCFINOPSSi-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 150,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_Ext-5BrCFINOPSSi-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(0.000115063,'m^3/(mol*s)'), n=2.71663, w0=(377.5,'kJ/mol'), E0=(54.8747,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_Ext-5BrCFINOPSSi-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_Ext-5BrCFINOPSSi-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_Ext-5BrCFINOPSSi-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_Ext-5BrCFINOPSSi-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 151,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_6R!H->C",
    kinetics = ArrheniusBM(A=(3.97108e-05,'m^3/(mol*s)'), n=2.90057, w0=(377.5,'kJ/mol'), E0=(71.7295,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 152,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(0.00033355,'m^3/(mol*s)'), n=2.63731, w0=(377.5,'kJ/mol'), E0=(57.7118,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_Ext-5BrCFINOPSSi-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 153,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->F",
    kinetics = ArrheniusBM(A=(0.00118562,'m^3/(mol*s)'), n=2.60866, w0=(377.5,'kJ/mol'), E0=(61.2627,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7490226852990982, var=0.47552299868572234, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->F
    Total Standard Deviation in ln(k): 3.264395281656225"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->F
Total Standard Deviation in ln(k): 3.264395281656225""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->F
Total Standard Deviation in ln(k): 3.264395281656225
""",
)

entry(
    index = 154,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->F_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.00028866,'m^3/(mol*s)'), n=2.74158, w0=(377.5,'kJ/mol'), E0=(59.1849,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->F_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->F_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->F_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->F_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 155,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F",
    kinetics = ArrheniusBM(A=(0.00109656,'m^3/(mol*s)'), n=2.61062, w0=(377.5,'kJ/mol'), E0=(66.1671,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.8522866200766248, var=2.236966882092403, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F
    Total Standard Deviation in ln(k): 5.139804319580604"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F
Total Standard Deviation in ln(k): 5.139804319580604""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F
Total Standard Deviation in ln(k): 5.139804319580604
""",
)

entry(
    index = 156,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.00282804,'m^3/(mol*s)'), n=2.43673, w0=(377.5,'kJ/mol'), E0=(67.2191,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.8828782220355884, var=4.870532024454879, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R
    Total Standard Deviation in ln(k): 6.6425933406616835"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R
Total Standard Deviation in ln(k): 6.6425933406616835""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R
Total Standard Deviation in ln(k): 6.6425933406616835
""",
)

entry(
    index = 157,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R_5CO->O",
    kinetics = ArrheniusBM(A=(2.60273e-05,'m^3/(mol*s)'), n=3.06563, w0=(377.5,'kJ/mol'), E0=(55.5629,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.8085861580455086, var=2.6363211636944035, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R_5CO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R_5CO->O
    Total Standard Deviation in ln(k): 5.286662145720866"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R_5CO->O
Total Standard Deviation in ln(k): 5.286662145720866""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R_5CO->O
Total Standard Deviation in ln(k): 5.286662145720866
""",
)

entry(
    index = 158,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R_5CO->O_6R!H->C",
    kinetics = ArrheniusBM(A=(6.12995e-05,'m^3/(mol*s)'), n=2.9629, w0=(377.5,'kJ/mol'), E0=(51.4477,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R_5CO->O_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R_5CO->O_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R_5CO->O_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R_5CO->O_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 159,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R_5CO->O_N-6R!H->C",
    kinetics = ArrheniusBM(A=(0.0131926,'m^3/(mol*s)'), n=2.28677, w0=(377.5,'kJ/mol'), E0=(68.8153,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R_5CO->O_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R_5CO->O_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R_5CO->O_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R_5CO->O_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 160,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R_N-5CO->O",
    kinetics = ArrheniusBM(A=(3.24197e-07,'m^3/(mol*s)'), n=3.47473, w0=(377.5,'kJ/mol'), E0=(66.4933,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R_N-5CO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R_N-5CO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R_N-5CO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_Ext-3C-R_N-5CO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 161,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_5CO->C",
    kinetics = ArrheniusBM(A=(0.00296538,'m^3/(mol*s)'), n=2.42542, w0=(377.5,'kJ/mol'), E0=(60.6732,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_5CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_5CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_5CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_5CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 162,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_N-5CO->C",
    kinetics = ArrheniusBM(A=(5.4353e-05,'m^3/(mol*s)'), n=3.2139, w0=(377.5,'kJ/mol'), E0=(69.4873,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_N-5CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_N-5CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_N-5CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->F_N-5CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 163,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C",
    kinetics = ArrheniusBM(A=(6.22375e-08,'m^3/(mol*s)'), n=3.75402, w0=(377.5,'kJ/mol'), E0=(45.3803,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7300963942570904, var=0.2834779941975115, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C
    Total Standard Deviation in ln(k): 2.901787162259514"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 2.901787162259514""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 2.901787162259514
""",
)

entry(
    index = 164,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.00359695,'m^3/(mol*s)'), n=2.38431, w0=(377.5,'kJ/mol'), E0=(56.9016,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6149676163342318, var=0.1506266941051072, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 2.323195579086853"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 2.323195579086853""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 2.323195579086853
""",
)

entry(
    index = 165,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(0.0045684,'m^3/(mol*s)'), n=2.33135, w0=(377.5,'kJ/mol'), E0=(55.9998,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6172171859468926, var=0.21745062367464152, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R
    Total Standard Deviation in ln(k): 2.48563701737014"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R
Total Standard Deviation in ln(k): 2.48563701737014""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R
Total Standard Deviation in ln(k): 2.48563701737014
""",
)

entry(
    index = 166,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R",
    kinetics = ArrheniusBM(A=(0.00164872,'m^3/(mol*s)'), n=2.48346, w0=(377.5,'kJ/mol'), E0=(55.4232,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5892185214819646, var=1.1901431754153382, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R
    Total Standard Deviation in ln(k): 3.667487884445032"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R
Total Standard Deviation in ln(k): 3.667487884445032""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R
Total Standard Deviation in ln(k): 3.667487884445032
""",
)

entry(
    index = 167,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(0.0035867,'m^3/(mol*s)'), n=2.3426, w0=(377.5,'kJ/mol'), E0=(56.7047,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 168,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(0.000395983,'m^3/(mol*s)'), n=2.7051, w0=(377.5,'kJ/mol'), E0=(53.3865,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 169,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(0.000869642,'m^3/(mol*s)'), n=2.59617, w0=(377.5,'kJ/mol'), E0=(57.6208,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 170,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(0.312416,'m^3/(mol*s)'), n=1.69659, w0=(377.5,'kJ/mol'), E0=(56.1257,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_5BrCFINOPSSi->C_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 171,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.00111823,'m^3/(mol*s)'), n=2.56187, w0=(377.5,'kJ/mol'), E0=(66.4419,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3C_N-5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 172,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(3.05918e-11,'m^3/(mol*s)'), n=4.78616, w0=(377.5,'kJ/mol'), E0=(39.7671,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.9815347990532445, var=1.0899074781672338, Tref=1000.0, N=36, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl',), comment="""BM rule fitted to 36 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 4.559083872993737"""),
    rank = 11,
    shortDesc = """BM rule fitted to 36 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 4.559083872993737""",
    longDesc = 
"""
BM rule fitted to 36 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 4.559083872993737
""",
)

entry(
    index = 173,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C",
    kinetics = ArrheniusBM(A=(1.76228e-06,'m^3/(mol*s)'), n=3.39677, w0=(377.5,'kJ/mol'), E0=(54.1696,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.8993297460079297, var=1.2415870559521356, Tref=1000.0, N=28, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C',), comment="""BM rule fitted to 28 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C
    Total Standard Deviation in ln(k): 4.493429117334684"""),
    rank = 11,
    shortDesc = """BM rule fitted to 28 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 4.493429117334684""",
    longDesc = 
"""
BM rule fitted to 28 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 4.493429117334684
""",
)

entry(
    index = 174,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(0.00127445,'m^3/(mol*s)'), n=2.53116, w0=(377.5,'kJ/mol'), E0=(62.3756,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.9176550699298026, var=1.8067767597339555, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R',), comment="""BM rule fitted to 14 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 5.000358651472218"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 5.000358651472218""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 5.000358651472218
""",
)

entry(
    index = 175,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi",
    kinetics = ArrheniusBM(A=(8.21371e-15,'m^3/(mol*s)'), n=5.71849, w0=(377.5,'kJ/mol'), E0=(12.0793,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.2633034367046156, var=1.2400700520703902, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi',), comment="""BM rule fitted to 13 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi
    Total Standard Deviation in ln(k): 5.406570798781686"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi
Total Standard Deviation in ln(k): 5.406570798781686""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi
Total Standard Deviation in ln(k): 5.406570798781686
""",
)

entry(
    index = 176,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl",
    kinetics = ArrheniusBM(A=(3.37248e-07,'m^3/(mol*s)'), n=3.48551, w0=(377.5,'kJ/mol'), E0=(51.3951,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.0030967832680822, var=1.02376616290026, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl',), comment="""BM rule fitted to 9 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl
    Total Standard Deviation in ln(k): 4.548761299597697"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl
Total Standard Deviation in ln(k): 4.548761299597697""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl
Total Standard Deviation in ln(k): 4.548761299597697
""",
)

entry(
    index = 177,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.26142e-09,'m^3/(mol*s)'), n=4.02301, w0=(377.5,'kJ/mol'), E0=(45.629,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.3989053942318856, var=1.5230964924623742, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R
    Total Standard Deviation in ln(k): 5.988957323080046"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 5.988957323080046""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 5.988957323080046
""",
)

entry(
    index = 178,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.31417e-07,'m^3/(mol*s)'), n=3.42833, w0=(377.5,'kJ/mol'), E0=(47.5181,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.2573730456458136, var=1.1960403194763065, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 5.351679776328824"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 5.351679776328824""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 5.351679776328824
""",
)

entry(
    index = 179,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R_Ext-4BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(3.10754e-06,'m^3/(mol*s)'), n=3.12379, w0=(377.5,'kJ/mol'), E0=(52.0346,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.148138976138127, var=0.5592306990446144, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R_Ext-4BrCFINOPSSi-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R_Ext-4BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 4.383946849335255"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 4.383946849335255""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 4.383946849335255
""",
)

entry(
    index = 180,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R_Ext-4BrCFINOPSSi-R_8R!H->C",
    kinetics = ArrheniusBM(A=(2.96843e-08,'m^3/(mol*s)'), n=3.73603, w0=(377.5,'kJ/mol'), E0=(49.4925,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R_Ext-4BrCFINOPSSi-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R_Ext-4BrCFINOPSSi-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R_Ext-4BrCFINOPSSi-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R_Ext-4BrCFINOPSSi-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 181,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R_Ext-4BrCFINOPSSi-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(1.02403e-05,'m^3/(mol*s)'), n=2.95864, w0=(377.5,'kJ/mol'), E0=(51.8366,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.0437897175102202, var=1.2520337920614315, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R_Ext-4BrCFINOPSSi-R_N-8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R_Ext-4BrCFINOPSSi-R_N-8R!H->C
    Total Standard Deviation in ln(k): 4.865771829476588"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R_Ext-4BrCFINOPSSi-R_N-8R!H->C
Total Standard Deviation in ln(k): 4.865771829476588""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R_Ext-4BrCFINOPSSi-R_N-8R!H->C
Total Standard Deviation in ln(k): 4.865771829476588
""",
)

entry(
    index = 182,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R_Ext-4BrCFINOPSSi-R_N-8R!H->C_Ext-4BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(0.000694859,'m^3/(mol*s)'), n=2.4156, w0=(377.5,'kJ/mol'), E0=(58.4618,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R_Ext-4BrCFINOPSSi-R_N-8R!H->C_Ext-4BrCFINOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R_Ext-4BrCFINOPSSi-R_N-8R!H->C_Ext-4BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R_Ext-4BrCFINOPSSi-R_N-8R!H->C_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-3C-R_Ext-3C-R_Ext-4BrCFINOPSSi-R_N-8R!H->C_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 183,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-4BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(0.00285305,'m^3/(mol*s)'), n=2.41283, w0=(377.5,'kJ/mol'), E0=(61.8636,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6521167723706013, var=1.8527619017489518, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-4BrCFINOPSSi-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-4BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 4.367253494937644"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 4.367253494937644""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 4.367253494937644
""",
)

entry(
    index = 184,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-4BrCFINOPSSi-R_6R!H->C",
    kinetics = ArrheniusBM(A=(0.000166848,'m^3/(mol*s)'), n=2.71783, w0=(377.5,'kJ/mol'), E0=(63.3264,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-4BrCFINOPSSi-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-4BrCFINOPSSi-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-4BrCFINOPSSi-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-4BrCFINOPSSi-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 185,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-4BrCFINOPSSi-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(0.00041919,'m^3/(mol*s)'), n=2.6756, w0=(377.5,'kJ/mol'), E0=(56.9724,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7058325342874846, var=2.071098785200921, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-4BrCFINOPSSi-R_N-6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-4BrCFINOPSSi-R_N-6R!H->C
    Total Standard Deviation in ln(k): 4.658525497686495"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-4BrCFINOPSSi-R_N-6R!H->C
Total Standard Deviation in ln(k): 4.658525497686495""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-4BrCFINOPSSi-R_N-6R!H->C
Total Standard Deviation in ln(k): 4.658525497686495
""",
)

entry(
    index = 186,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-4BrCFINOPSSi-R_N-6R!H->C_Ext-4BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(0.000173475,'m^3/(mol*s)'), n=2.83304, w0=(377.5,'kJ/mol'), E0=(54.1185,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-4BrCFINOPSSi-R_N-6R!H->C_Ext-4BrCFINOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-4BrCFINOPSSi-R_N-6R!H->C_Ext-4BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-4BrCFINOPSSi-R_N-6R!H->C_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_5R!H->Cl_Ext-4BrCFINOPSSi-R_N-6R!H->C_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 187,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(2.92513e-05,'m^3/(mol*s)'), n=3.09797, w0=(377.5,'kJ/mol'), E0=(58.125,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6991189116902325, var=1.6993325727959425, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl
    Total Standard Deviation in ln(k): 4.369921772197586"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl
Total Standard Deviation in ln(k): 4.369921772197586""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl
Total Standard Deviation in ln(k): 4.369921772197586
""",
)

entry(
    index = 188,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl_Ext-4BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(0.00471725,'m^3/(mol*s)'), n=2.56078, w0=(377.5,'kJ/mol'), E0=(57.3256,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl_Ext-4BrCFINOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl_Ext-4BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 189,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.62215e-05,'m^3/(mol*s)'), n=3.14181, w0=(377.5,'kJ/mol'), E0=(55.7903,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 190,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl_5CF->C",
    kinetics = ArrheniusBM(A=(0.00150441,'m^3/(mol*s)'), n=2.61552, w0=(377.5,'kJ/mol'), E0=(70.0304,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl_5CF->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl_5CF->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl_5CF->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl_5CF->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 191,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl_N-5CF->C",
    kinetics = ArrheniusBM(A=(0.000850733,'m^3/(mol*s)'), n=2.60501, w0=(377.5,'kJ/mol'), E0=(63.4061,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl_N-5CF->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl_N-5CF->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl_N-5CF->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi_N-5R!H->Cl_N-5CF->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 192,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_N-Sp-5R!H-4BrCFINOPSSi",
    kinetics = ArrheniusBM(A=(0.504308,'m^3/(mol*s)'), n=2.03378, w0=(377.5,'kJ/mol'), E0=(75.5444,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_N-Sp-5R!H-4BrCFINOPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_N-Sp-5R!H-4BrCFINOPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_N-Sp-5R!H-4BrCFINOPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_N-Sp-5R!H-4BrCFINOPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 193,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_4BrCFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(0.000926024,'m^3/(mol*s)'), n=2.61462, w0=(377.5,'kJ/mol'), E0=(70.8774,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5864975485222702, var=2.276890877267597, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_4BrCFINOPSSi->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_4BrCFINOPSSi->Br
    Total Standard Deviation in ln(k): 4.498630869286715"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_4BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 4.498630869286715""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_4BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 4.498630869286715
""",
)

entry(
    index = 194,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_4BrCFINOPSSi->Br_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.000500117,'m^3/(mol*s)'), n=2.74152, w0=(377.5,'kJ/mol'), E0=(69.1178,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_4BrCFINOPSSi->Br_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_4BrCFINOPSSi->Br_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_4BrCFINOPSSi->Br_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_4BrCFINOPSSi->Br_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 195,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(0.000174949,'m^3/(mol*s)'), n=2.87922, w0=(377.5,'kJ/mol'), E0=(58.414,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7291921845369882, var=0.5092608104025962, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br',), comment="""BM rule fitted to 12 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br
    Total Standard Deviation in ln(k): 3.2627704752556896"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 3.2627704752556896""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 3.2627704752556896
""",
)

entry(
    index = 196,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F",
    kinetics = ArrheniusBM(A=(0.00067317,'m^3/(mol*s)'), n=2.69382, w0=(377.5,'kJ/mol'), E0=(63.4762,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6848138968080264, var=0.05375919075440844, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F
    Total Standard Deviation in ln(k): 2.185456373724017"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F
Total Standard Deviation in ln(k): 2.185456373724017""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F
Total Standard Deviation in ln(k): 2.185456373724017
""",
)

entry(
    index = 197,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.000320443,'m^3/(mol*s)'), n=2.79082, w0=(377.5,'kJ/mol'), E0=(62.6631,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7594507312924307, var=0.01400043979083455, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R
    Total Standard Deviation in ln(k): 2.145374845482359"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R
Total Standard Deviation in ln(k): 2.145374845482359""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R
Total Standard Deviation in ln(k): 2.145374845482359
""",
)

entry(
    index = 198,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R_5R!H->F",
    kinetics = ArrheniusBM(A=(0.000968703,'m^3/(mol*s)'), n=2.64771, w0=(377.5,'kJ/mol'), E0=(63.5751,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6837324222670912, var=0.04301272446389267, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R_5R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R_5R!H->F
    Total Standard Deviation in ln(k): 2.1336928761189213"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R_5R!H->F
Total Standard Deviation in ln(k): 2.1336928761189213""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R_5R!H->F
Total Standard Deviation in ln(k): 2.1336928761189213
""",
)

entry(
    index = 199,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R_5R!H->F_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.000554304,'m^3/(mol*s)'), n=2.72146, w0=(377.5,'kJ/mol'), E0=(62.7267,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R_5R!H->F_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R_5R!H->F_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R_5R!H->F_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R_5R!H->F_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 200,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(0.000107653,'m^3/(mol*s)'), n=2.93201, w0=(377.5,'kJ/mol'), E0=(61.7583,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.8375592370061683, var=0.0018342838237614624, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R_N-5R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R_N-5R!H->F
    Total Standard Deviation in ln(k): 2.1902800695887295"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R_N-5R!H->F
Total Standard Deviation in ln(k): 2.1902800695887295""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R_N-5R!H->F
Total Standard Deviation in ln(k): 2.1902800695887295
""",
)

entry(
    index = 201,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R_N-5R!H->F_Ext-3C-R",
    kinetics = ArrheniusBM(A=(4.04932e-06,'m^3/(mol*s)'), n=3.26105, w0=(377.5,'kJ/mol'), E0=(53.1912,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R_N-5R!H->F_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R_N-5R!H->F_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R_N-5R!H->F_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_4CFO->F_Ext-3C-R_N-5R!H->F_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 202,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F",
    kinetics = ArrheniusBM(A=(0.000159219,'m^3/(mol*s)'), n=2.90362, w0=(377.5,'kJ/mol'), E0=(55.8054,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7462327670841784, var=0.530900979327811, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F',), comment="""BM rule fitted to 7 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F
    Total Standard Deviation in ln(k): 3.33566586101622"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F
Total Standard Deviation in ln(k): 3.33566586101622""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F
Total Standard Deviation in ln(k): 3.33566586101622
""",
)

entry(
    index = 203,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.28884e-05,'m^3/(mol*s)'), n=3.20885, w0=(377.5,'kJ/mol'), E0=(52.7212,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.8610044626554989, var=0.9659515124619527, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R
    Total Standard Deviation in ln(k): 4.1336382097617665"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R
Total Standard Deviation in ln(k): 4.1336382097617665""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R
Total Standard Deviation in ln(k): 4.1336382097617665
""",
)

entry(
    index = 204,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(5.41344e-07,'m^3/(mol*s)'), n=3.59064, w0=(377.5,'kJ/mol'), E0=(49.138,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.9657143811730287, var=1.5734263031504556, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C
    Total Standard Deviation in ln(k): 4.94108336314704"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 4.94108336314704""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 4.94108336314704
""",
)

entry(
    index = 205,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_4CO->C",
    kinetics = ArrheniusBM(A=(0.000396221,'m^3/(mol*s)'), n=2.78156, w0=(377.5,'kJ/mol'), E0=(54.7524,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.8308086929813021, var=0.9275085414446818, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_4CO->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_4CO->C
    Total Standard Deviation in ln(k): 4.018164147571618"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_4CO->C
Total Standard Deviation in ln(k): 4.018164147571618""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_4CO->C
Total Standard Deviation in ln(k): 4.018164147571618
""",
)

entry(
    index = 206,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_4CO->C_Sp-5C-3C",
    kinetics = ArrheniusBM(A=(5.94642e-05,'m^3/(mol*s)'), n=3.01136, w0=(377.5,'kJ/mol'), E0=(51.739,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.981442082067932, var=2.2534368589916305, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_4CO->C_Sp-5C-3C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_4CO->C_Sp-5C-3C
    Total Standard Deviation in ln(k): 5.475333283219138"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_4CO->C_Sp-5C-3C
Total Standard Deviation in ln(k): 5.475333283219138""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_4CO->C_Sp-5C-3C
Total Standard Deviation in ln(k): 5.475333283219138
""",
)

entry(
    index = 207,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_4CO->C_Sp-5C-3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(5.12514e-05,'m^3/(mol*s)'), n=3.03612, w0=(377.5,'kJ/mol'), E0=(46.7947,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_4CO->C_Sp-5C-3C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_4CO->C_Sp-5C-3C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_4CO->C_Sp-5C-3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_4CO->C_Sp-5C-3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 208,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_4CO->C_N-Sp-5C-3C",
    kinetics = ArrheniusBM(A=(0.000983575,'m^3/(mol*s)'), n=2.68082, w0=(377.5,'kJ/mol'), E0=(56.9831,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_4CO->C_N-Sp-5C-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_4CO->C_N-Sp-5C-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_4CO->C_N-Sp-5C-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_4CO->C_N-Sp-5C-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 209,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_N-4CO->C",
    kinetics = ArrheniusBM(A=(0.000215677,'m^3/(mol*s)'), n=2.81072, w0=(377.5,'kJ/mol'), E0=(63.4783,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_N-4CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_N-4CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_5R!H->C_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 210,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.00247943,'m^3/(mol*s)'), n=2.60505, w0=(377.5,'kJ/mol'), E0=(58.1004,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 211,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_4CO->C",
    kinetics = ArrheniusBM(A=(0.00370217,'m^3/(mol*s)'), n=2.54095, w0=(377.5,'kJ/mol'), E0=(61.6406,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_4CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_4CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_4CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_4CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 212,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_N-4CO->C",
    kinetics = ArrheniusBM(A=(0.0293722,'m^3/(mol*s)'), n=2.26344, w0=(377.5,'kJ/mol'), E0=(60.4598,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_N-4CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_N-4CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->Br_N-4CFO->F_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 213,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C",
    kinetics = ArrheniusBM(A=(1.05821e-12,'m^3/(mol*s)'), n=5.29384, w0=(377.5,'kJ/mol'), E0=(36.5342,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5309914736408321, var=1.610666827147807, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C',), comment="""BM rule fitted to 8 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C
    Total Standard Deviation in ln(k): 3.8783998021171904"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 3.8783998021171904""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 3.8783998021171904
""",
)

entry(
    index = 214,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C",
    kinetics = ArrheniusBM(A=(2.44364e-10,'m^3/(mol*s)'), n=4.57432, w0=(377.5,'kJ/mol'), E0=(43.2299,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5381520374702685, var=1.220561648715197, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C',), comment="""BM rule fitted to 7 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C
    Total Standard Deviation in ln(k): 3.5669527031101564"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C
Total Standard Deviation in ln(k): 3.5669527031101564""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C
Total Standard Deviation in ln(k): 3.5669527031101564
""",
)

entry(
    index = 215,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.51575e-11,'m^3/(mol*s)'), n=4.90867, w0=(377.5,'kJ/mol'), E0=(39.7911,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4818810452381022, var=1.3296704660475434, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 3.5224432352238044"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 3.5224432352238044""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 3.5224432352238044
""",
)

entry(
    index = 216,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C",
    kinetics = ArrheniusBM(A=(0.0841599,'m^3/(mol*s)'), n=2.08797, w0=(377.5,'kJ/mol'), E0=(62.2572,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3976827895245833, var=0.9988116974030249, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C
    Total Standard Deviation in ln(k): 3.0027465961380693"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C
Total Standard Deviation in ln(k): 3.0027465961380693""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C
Total Standard Deviation in ln(k): 3.0027465961380693
""",
)

entry(
    index = 217,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(0.0451542,'m^3/(mol*s)'), n=2.22559, w0=(377.5,'kJ/mol'), E0=(61.3128,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.37722678632135304, var=1.3387541688444908, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R
    Total Standard Deviation in ln(k): 3.2673755916197744"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R
Total Standard Deviation in ln(k): 3.2673755916197744""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R
Total Standard Deviation in ln(k): 3.2673755916197744
""",
)

entry(
    index = 218,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(0.0698615,'m^3/(mol*s)'), n=2.12937, w0=(377.5,'kJ/mol'), E0=(62.8572,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.33648245853362835, var=0.23540736584333805, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R_5R!H->C
    Total Standard Deviation in ln(k): 1.8181066546827762"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 1.8181066546827762""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 1.8181066546827762
""",
)

entry(
    index = 219,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R_5R!H->C_6R!H->C",
    kinetics = ArrheniusBM(A=(0.201337,'m^3/(mol*s)'), n=2.00328, w0=(377.5,'kJ/mol'), E0=(62.8126,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R_5R!H->C_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R_5R!H->C_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R_5R!H->C_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R_5R!H->C_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 220,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R_5R!H->C_N-6R!H->C",
    kinetics = ArrheniusBM(A=(0.0395088,'m^3/(mol*s)'), n=2.19468, w0=(377.5,'kJ/mol'), E0=(63.4385,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R_5R!H->C_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R_5R!H->C_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R_5R!H->C_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R_5R!H->C_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 221,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.0235932,'m^3/(mol*s)'), n=2.3902, w0=(377.5,'kJ/mol'), E0=(58.4656,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 222,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_5R!H->F",
    kinetics = ArrheniusBM(A=(9.05162,'m^3/(mol*s)'), n=1.36072, w0=(377.5,'kJ/mol'), E0=(64.31,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 223,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_N-5R!H->F",
    kinetics = ArrheniusBM(A=(0.00498304,'m^3/(mol*s)'), n=2.40441, w0=(377.5,'kJ/mol'), E0=(63.0156,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_N-5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_N-5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_Sp-5R!H-4C_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 224,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_N-Sp-5R!H-4C",
    kinetics = ArrheniusBM(A=(0.0817363,'m^3/(mol*s)'), n=2.26425, w0=(377.5,'kJ/mol'), E0=(89.8765,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_N-Sp-5R!H-4C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_N-Sp-5R!H-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_N-Sp-5R!H-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_4BrCFINOPSSi->C_Ext-4C-R_N-Sp-5R!H-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 225,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_N-4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.0175518,'m^3/(mol*s)'), n=2.3929, w0=(377.5,'kJ/mol'), E0=(65.9155,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_N-4BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_N-4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Sp-4BrCFINOPSSi=3C_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 226,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_N-Sp-4BrCFINOPSSi=3C",
    kinetics = ArrheniusBM(A=(9.64471e-05,'m^3/(mol*s)'), n=3.30977, w0=(377.5,'kJ/mol'), E0=(58.4639,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_N-Sp-4BrCFINOPSSi=3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_N-Sp-4BrCFINOPSSi=3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_N-Sp-4BrCFINOPSSi=3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_N-Sp-4BrCFINOPSSi=3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 227,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_N-3C-u1",
    kinetics = ArrheniusBM(A=(2.19763e-23,'m^3/(mol*s)'), n=8.61918, w0=(377.5,'kJ/mol'), E0=(-19.1051,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.4646594003355289, var=2.0481925644424193, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_N-3C-u1',), comment="""BM rule fitted to 8 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_N-3C-u1
    Total Standard Deviation in ln(k): 6.549126920814744"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_N-3C-u1
Total Standard Deviation in ln(k): 6.549126920814744""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_N-3C-u1
Total Standard Deviation in ln(k): 6.549126920814744
""",
)

entry(
    index = 228,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_N-3C-u1_Ext-3C-R",
    kinetics = ArrheniusBM(A=(4.53707e-21,'m^3/(mol*s)'), n=7.94556, w0=(377.5,'kJ/mol'), E0=(4.12617,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.4877204262337034, var=2.6987477803635986, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_N-3C-u1_Ext-3C-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_N-3C-u1_Ext-3C-R
    Total Standard Deviation in ln(k): 7.031342922382065"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_N-3C-u1_Ext-3C-R
Total Standard Deviation in ln(k): 7.031342922382065""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_N-3C-u1_Ext-3C-R
Total Standard Deviation in ln(k): 7.031342922382065
""",
)

entry(
    index = 229,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_N-3C-u1_Ext-3C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(1.16363e-16,'m^3/(mol*s)'), n=6.61381, w0=(377.5,'kJ/mol'), E0=(22.6002,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.9578676511373394, var=4.792596739886361, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_N-3C-u1_Ext-3C-R_4R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_N-3C-u1_Ext-3C-R_4R!H->C
    Total Standard Deviation in ln(k): 9.308031532285082"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_N-3C-u1_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 9.308031532285082""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_N-3C-u1_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 9.308031532285082
""",
)

entry(
    index = 230,
    label = "Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_N-3C-u1_Ext-3C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(2.8158e-27,'m^3/(mol*s)'), n=9.80675, w0=(377.5,'kJ/mol'), E0=(-27.6069,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.8751418348943519, var=13.264581734405644, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_N-3C-u1_Ext-3C-R_N-4R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_N-3C-u1_Ext-3C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 9.500208953089656"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_N-3C-u1_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 9.500208953089656""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_3BrCClFINOPSSi->C_N-3C-u1_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 9.500208953089656
""",
)

entry(
    index = 231,
    label = "Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.0676658,'m^3/(mol*s)'), n=2.53916, w0=(350,'kJ/mol'), E0=(36.6887,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7666587199812803, var=1.3254651311333112, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 4.234306562190847"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 4.234306562190847""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 4.234306562190847
""",
)

entry(
    index = 232,
    label = "Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_Ext-3BrClFO-R",
    kinetics = ArrheniusBM(A=(0.0226172,'m^3/(mol*s)'), n=2.64755, w0=(350,'kJ/mol'), E0=(55.5384,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7275143801457727, var=1.423564898523257, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_Ext-3BrClFO-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_Ext-3BrClFO-R
    Total Standard Deviation in ln(k): 4.219839931166794"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_Ext-3BrClFO-R
Total Standard Deviation in ln(k): 4.219839931166794""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_Ext-3BrClFO-R
Total Standard Deviation in ln(k): 4.219839931166794
""",
)

entry(
    index = 233,
    label = "Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_Ext-3BrClFO-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(0.185375,'m^3/(mol*s)'), n=2.32354, w0=(350,'kJ/mol'), E0=(65.4899,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.6098302482326579, var=0.010256831792420026, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_Ext-3BrClFO-R_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_Ext-3BrClFO-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 4.247831204166285"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_Ext-3BrClFO-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 4.247831204166285""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_Ext-3BrClFO-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 4.247831204166285
""",
)

entry(
    index = 234,
    label = "Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_Ext-3BrClFO-R_Ext-4R!H-R_Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(1.83471,'m^3/(mol*s)'), n=1.92781, w0=(350,'kJ/mol'), E0=(50.9181,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_Ext-3BrClFO-R_Ext-4R!H-R_Sp-5R!H-4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_Ext-3BrClFO-R_Ext-4R!H-R_Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_Ext-3BrClFO-R_Ext-4R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_Ext-3BrClFO-R_Ext-4R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 235,
    label = "Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_Ext-3BrClFO-R_Ext-4R!H-R_N-Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(0.0382272,'m^3/(mol*s)'), n=2.6305, w0=(350,'kJ/mol'), E0=(88.6369,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_Ext-3BrClFO-R_Ext-4R!H-R_N-Sp-5R!H-4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_Ext-3BrClFO-R_Ext-4R!H-R_N-Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_Ext-3BrClFO-R_Ext-4R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_Ext-3BrClFO-R_Ext-4R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 236,
    label = "Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_3BrClFO-u1",
    kinetics = ArrheniusBM(A=(188.748,'m^3/(mol*s)'), n=1.64016, w0=(350,'kJ/mol'), E0=(51.9294,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_3BrClFO-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_3BrClFO-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_3BrClFO-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_3BrClFO-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 237,
    label = "Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_N-3BrClFO-u1",
    kinetics = ArrheniusBM(A=(26.7577,'m^3/(mol*s)'), n=1.79078, w0=(350,'kJ/mol'), E0=(64.6189,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_N-3BrClFO-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_N-3BrClFO-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_N-3BrClFO-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_1R->H_N-3BrCClFINOPSSi->C_N-3BrClFO-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 238,
    label = "Root_N-3R->H_N-1R->H",
    kinetics = ArrheniusBM(A=(1.19864e+12,'m^3/(mol*s)'), n=-1.48989, w0=(310.466,'kJ/mol'), E0=(90.3531,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4076157101792493, var=10.367202692733693, Tref=1000.0, N=320, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H',), comment="""BM rule fitted to 320 training reactions at node Root_N-3R->H_N-1R->H
    Total Standard Deviation in ln(k): 7.479034299388339"""),
    rank = 11,
    shortDesc = """BM rule fitted to 320 training reactions at node Root_N-3R->H_N-1R->H
Total Standard Deviation in ln(k): 7.479034299388339""",
    longDesc = 
"""
BM rule fitted to 320 training reactions at node Root_N-3R->H_N-1R->H
Total Standard Deviation in ln(k): 7.479034299388339
""",
)

entry(
    index = 239,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C",
    kinetics = ArrheniusBM(A=(2.49786e+12,'m^3/(mol*s)'), n=-1.54851, w0=(319.262,'kJ/mol'), E0=(95.4442,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.505483868990105, var=9.93805113587131, Tref=1000.0, N=230, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C',), comment="""BM rule fitted to 230 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C
    Total Standard Deviation in ln(k): 7.589922085485658"""),
    rank = 11,
    shortDesc = """BM rule fitted to 230 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C
Total Standard Deviation in ln(k): 7.589922085485658""",
    longDesc = 
"""
BM rule fitted to 230 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C
Total Standard Deviation in ln(k): 7.589922085485658
""",
)

entry(
    index = 240,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0",
    kinetics = ArrheniusBM(A=(6.52322e+09,'m^3/(mol*s)'), n=-0.819537, w0=(319.524,'kJ/mol'), E0=(89.4839,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4243363456136127, var=9.596764611745396, Tref=1000.0, N=216, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0',), comment="""BM rule fitted to 216 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0
    Total Standard Deviation in ln(k): 7.276569399794586"""),
    rank = 11,
    shortDesc = """BM rule fitted to 216 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0
Total Standard Deviation in ln(k): 7.276569399794586""",
    longDesc = 
"""
BM rule fitted to 216 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0
Total Standard Deviation in ln(k): 7.276569399794586
""",
)

entry(
    index = 241,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(681.703,'m^3/(mol*s)'), n=1.03596, w0=(326.767,'kJ/mol'), E0=(78.8587,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.014989880519170853, var=6.704871164019452, Tref=1000.0, N=118, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R',), comment="""BM rule fitted to 118 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R
    Total Standard Deviation in ln(k): 5.228677110102691"""),
    rank = 11,
    shortDesc = """BM rule fitted to 118 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 5.228677110102691""",
    longDesc = 
"""
BM rule fitted to 118 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 5.228677110102691
""",
)

entry(
    index = 242,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(0.000388477,'m^3/(mol*s)'), n=2.73292, w0=(327,'kJ/mol'), E0=(64.0994,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.23237106199395813, var=6.214375893369738, Tref=1000.0, N=51, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl',), comment="""BM rule fitted to 51 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl
    Total Standard Deviation in ln(k): 5.581380792166963"""),
    rank = 11,
    shortDesc = """BM rule fitted to 51 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl
Total Standard Deviation in ln(k): 5.581380792166963""",
    longDesc = 
"""
BM rule fitted to 51 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl
Total Standard Deviation in ln(k): 5.581380792166963
""",
)

entry(
    index = 243,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(2.29367e-05,'m^3/(mol*s)'), n=3.13347, w0=(327,'kJ/mol'), E0=(61.1799,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3289460841529283, var=4.9300421846720965, Tref=1000.0, N=44, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R',), comment="""BM rule fitted to 44 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R
    Total Standard Deviation in ln(k): 5.277750983083284"""),
    rank = 11,
    shortDesc = """BM rule fitted to 44 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 5.277750983083284""",
    longDesc = 
"""
BM rule fitted to 44 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 5.277750983083284
""",
)

entry(
    index = 244,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(0.0989742,'m^3/(mol*s)'), n=1.97911, w0=(327,'kJ/mol'), E0=(67.5801,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.19139477269589977, var=4.978728359536289, Tref=1000.0, N=23, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl',), comment="""BM rule fitted to 23 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl
    Total Standard Deviation in ln(k): 4.954069646078162"""),
    rank = 11,
    shortDesc = """BM rule fitted to 23 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl
Total Standard Deviation in ln(k): 4.954069646078162""",
    longDesc = 
"""
BM rule fitted to 23 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl
Total Standard Deviation in ln(k): 4.954069646078162
""",
)

entry(
    index = 245,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(0.105505,'m^3/(mol*s)'), n=1.96371, w0=(327,'kJ/mol'), E0=(67.935,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2104682899280889, var=5.168026621304137, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R',), comment="""BM rule fitted to 20 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R
    Total Standard Deviation in ln(k): 5.086238016097419"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 5.086238016097419""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 5.086238016097419
""",
)

entry(
    index = 246,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F",
    kinetics = ArrheniusBM(A=(6.03403e-06,'m^3/(mol*s)'), n=3.44652, w0=(327,'kJ/mol'), E0=(54.5328,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2837924980655133, var=1.1307892871443057, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F
    Total Standard Deviation in ln(k): 2.8448532232770063"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F
Total Standard Deviation in ln(k): 2.8448532232770063""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F
Total Standard Deviation in ln(k): 2.8448532232770063
""",
)

entry(
    index = 247,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.69273e-05,'m^3/(mol*s)'), n=3.21598, w0=(327,'kJ/mol'), E0=(56.0476,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1924895810000576, var=0.584765439115621, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F_Ext-1C-R
    Total Standard Deviation in ln(k): 2.01666222382158"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F_Ext-1C-R
Total Standard Deviation in ln(k): 2.01666222382158""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F_Ext-1C-R
Total Standard Deviation in ln(k): 2.01666222382158
""",
)

entry(
    index = 248,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(8.14379e-05,'m^3/(mol*s)'), n=3.22757, w0=(327,'kJ/mol'), E0=(60.6536,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 249,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F_Ext-1C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(4.02496e-06,'m^3/(mol*s)'), n=3.23501, w0=(327,'kJ/mol'), E0=(44.6302,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F_Ext-1C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F_Ext-1C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F_Ext-1C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F_Ext-1C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 250,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F_Ext-1C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(2.97135e-06,'m^3/(mol*s)'), n=3.55842, w0=(327,'kJ/mol'), E0=(59.4815,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F_Ext-1C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F_Ext-1C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F_Ext-1C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->F_Ext-1C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 251,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F",
    kinetics = ArrheniusBM(A=(9.49751,'m^3/(mol*s)'), n=1.33696, w0=(327,'kJ/mol'), E0=(73.6142,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1663953036825486, var=4.840290997816313, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F',), comment="""BM rule fitted to 16 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F
    Total Standard Deviation in ln(k): 4.82862840563614"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F
Total Standard Deviation in ln(k): 4.82862840563614""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F
Total Standard Deviation in ln(k): 4.82862840563614
""",
)

entry(
    index = 252,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl",
    kinetics = ArrheniusBM(A=(1689.71,'m^3/(mol*s)'), n=0.804851, w0=(327,'kJ/mol'), E0=(72.9536,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.008621768634224227, var=9.42893146868963, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl
    Total Standard Deviation in ln(k): 6.177515573124972"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl
Total Standard Deviation in ln(k): 6.177515573124972""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl
Total Standard Deviation in ln(k): 6.177515573124972
""",
)

entry(
    index = 253,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(432671,'m^3/(mol*s)'), n=0.0218824, w0=(327,'kJ/mol'), E0=(78.5741,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11001041652158022, var=9.787896882944041, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 6.548345006049886"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 6.548345006049886""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 6.548345006049886
""",
)

entry(
    index = 254,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.61987e+06,'m^3/(mol*s)'), n=-0.27797, w0=(327,'kJ/mol'), E0=(79.9833,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.26314046949734043, var=29.76193812430002, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.597889565216812"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.597889565216812""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.597889565216812
""",
)

entry(
    index = 255,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R_7R!H->F",
    kinetics = ArrheniusBM(A=(0.0013649,'m^3/(mol*s)'), n=2.67622, w0=(327,'kJ/mol'), E0=(47.2083,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R_7R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R_7R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R_7R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R_7R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 256,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R_N-7R!H->F",
    kinetics = ArrheniusBM(A=(0.110345,'m^3/(mol*s)'), n=1.80649, w0=(327,'kJ/mol'), E0=(66.9561,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R_N-7R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R_N-7R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R_N-7R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R_N-7R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 257,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_Sp-7R!H-1C",
    kinetics = ArrheniusBM(A=(5.8589e-05,'m^3/(mol*s)'), n=2.29206, w0=(327,'kJ/mol'), E0=(40.7264,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_Sp-7R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_Sp-7R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_Sp-7R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_Sp-7R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 258,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_N-Sp-7R!H-1C",
    kinetics = ArrheniusBM(A=(2.37346e-06,'m^3/(mol*s)'), n=3.69132, w0=(327,'kJ/mol'), E0=(62.068,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_N-Sp-7R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_N-Sp-7R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_N-Sp-7R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_6BrCClINOPSSi->Cl_Ext-1C-R_N-Sp-7R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 259,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl",
    kinetics = ArrheniusBM(A=(0.000113396,'m^3/(mol*s)'), n=2.69629, w0=(327,'kJ/mol'), E0=(64.0077,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3551262118744188, var=2.9438038486887055, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl',), comment="""BM rule fitted to 11 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl
    Total Standard Deviation in ln(k): 4.3319045036750925"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl
Total Standard Deviation in ln(k): 4.3319045036750925""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl
Total Standard Deviation in ln(k): 4.3319045036750925
""",
)

entry(
    index = 260,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.0323412,'m^3/(mol*s)'), n=2.02154, w0=(327,'kJ/mol'), E0=(68.8531,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06480524689450456, var=5.673055003193311, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 4.937740511994033"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 4.937740511994033""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 4.937740511994033
""",
)

entry(
    index = 261,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-6CO-R",
    kinetics = ArrheniusBM(A=(8.69384,'m^3/(mol*s)'), n=1.2223, w0=(327,'kJ/mol'), E0=(75.5558,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05866349367239268, var=10.4485014218227, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-6CO-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-6CO-R
    Total Standard Deviation in ln(k): 6.627529801190854"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-6CO-R
Total Standard Deviation in ln(k): 6.627529801190854""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-6CO-R
Total Standard Deviation in ln(k): 6.627529801190854
""",
)

entry(
    index = 262,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-6CO-R_8R!H->F",
    kinetics = ArrheniusBM(A=(8.17278e-07,'m^3/(mol*s)'), n=3.58113, w0=(327,'kJ/mol'), E0=(65.6713,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-6CO-R_8R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-6CO-R_8R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-6CO-R_8R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-6CO-R_8R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 263,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-6CO-R_N-8R!H->F",
    kinetics = ArrheniusBM(A=(1.16993,'m^3/(mol*s)'), n=1.2991, w0=(327,'kJ/mol'), E0=(69.3607,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0029930070290520253, var=26.24237548084292, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-6CO-R_N-8R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-6CO-R_N-8R!H->F
    Total Standard Deviation in ln(k): 10.277239151233395"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-6CO-R_N-8R!H->F
Total Standard Deviation in ln(k): 10.277239151233395""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-6CO-R_N-8R!H->F
Total Standard Deviation in ln(k): 10.277239151233395
""",
)

entry(
    index = 264,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-6CO-R_N-8R!H->F_Ext-6CO-R",
    kinetics = ArrheniusBM(A=(0.00017113,'m^3/(mol*s)'), n=2.22654, w0=(327,'kJ/mol'), E0=(65.5044,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-6CO-R_N-8R!H->F_Ext-6CO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-6CO-R_N-8R!H->F_Ext-6CO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-6CO-R_N-8R!H->F_Ext-6CO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-6CO-R_N-8R!H->F_Ext-6CO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 265,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(4.07553e-07,'m^3/(mol*s)'), n=3.64601, w0=(327,'kJ/mol'), E0=(57.6983,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 266,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C",
    kinetics = ArrheniusBM(A=(2.85672e-07,'m^3/(mol*s)'), n=3.4484, w0=(327,'kJ/mol'), E0=(61.0469,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6407190611527247, var=3.5033995001941394, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C
    Total Standard Deviation in ln(k): 5.362183762047712"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C
Total Standard Deviation in ln(k): 5.362183762047712""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C
Total Standard Deviation in ln(k): 5.362183762047712
""",
)

entry(
    index = 267,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R",
    kinetics = ArrheniusBM(A=(3.8202e-09,'m^3/(mol*s)'), n=4.0436, w0=(327,'kJ/mol'), E0=(55.0246,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6953685382864305, var=2.1884234896610373, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R
    Total Standard Deviation in ln(k): 4.712826102039405"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R
Total Standard Deviation in ln(k): 4.712826102039405""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R
Total Standard Deviation in ln(k): 4.712826102039405
""",
)

entry(
    index = 268,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R_7R!H->Cl",
    kinetics = ArrheniusBM(A=(9.61229e-09,'m^3/(mol*s)'), n=3.76774, w0=(327,'kJ/mol'), E0=(53.5181,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6560985622455391, var=2.3560865457481412, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R_7R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R_7R!H->Cl
    Total Standard Deviation in ln(k): 4.725666780577516"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R_7R!H->Cl
Total Standard Deviation in ln(k): 4.725666780577516""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R_7R!H->Cl
Total Standard Deviation in ln(k): 4.725666780577516
""",
)

entry(
    index = 269,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R_7R!H->Cl_Ext-6C-R",
    kinetics = ArrheniusBM(A=(4.64511e-10,'m^3/(mol*s)'), n=4.2575, w0=(327,'kJ/mol'), E0=(61.8108,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R_7R!H->Cl_Ext-6C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R_7R!H->Cl_Ext-6C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R_7R!H->Cl_Ext-6C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R_7R!H->Cl_Ext-6C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 270,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R_N-7R!H->Cl",
    kinetics = ArrheniusBM(A=(3.19529e-08,'m^3/(mol*s)'), n=3.94036, w0=(327,'kJ/mol'), E0=(59.9165,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7050469983542766, var=0.7706094078551056, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R_N-7R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R_N-7R!H->Cl
    Total Standard Deviation in ln(k): 3.5313187525085117"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R_N-7R!H->Cl
Total Standard Deviation in ln(k): 3.5313187525085117""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R_N-7R!H->Cl
Total Standard Deviation in ln(k): 3.5313187525085117
""",
)

entry(
    index = 271,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R_N-7R!H->Cl_Ext-6C-R",
    kinetics = ArrheniusBM(A=(1.81644e-08,'m^3/(mol*s)'), n=4.14193, w0=(327,'kJ/mol'), E0=(64.777,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R_N-7R!H->Cl_Ext-6C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R_N-7R!H->Cl_Ext-6C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R_N-7R!H->Cl_Ext-6C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C_Ext-6C-R_N-7R!H->Cl_Ext-6C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 272,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_N-6CO->C",
    kinetics = ArrheniusBM(A=(2.86786e-05,'m^3/(mol*s)'), n=2.68616, w0=(327,'kJ/mol'), E0=(51.0185,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_N-6CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_N-6CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_N-6CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_N-6CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 273,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(339.013,'m^3/(mol*s)'), n=0.91188, w0=(327,'kJ/mol'), E0=(71.5199,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03754168625935206, var=42.74003680138772, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 13.200454754907495"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 13.200454754907495""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 13.200454754907495
""",
)

entry(
    index = 274,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.00021109,'m^3/(mol*s)'), n=3.01699, w0=(327,'kJ/mol'), E0=(54.6981,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_5R!H->Cl_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 275,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(6.08063e-07,'m^3/(mol*s)'), n=3.70882, w0=(327,'kJ/mol'), E0=(60.3645,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4092327372539239, var=5.003615279472892, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl',), comment="""BM rule fitted to 21 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 5.512567204983788"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 5.512567204983788""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 5.512567204983788
""",
)

entry(
    index = 276,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi",
    kinetics = ArrheniusBM(A=(5.17708e-07,'m^3/(mol*s)'), n=3.68025, w0=(327,'kJ/mol'), E0=(59.9463,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.39876681134245934, var=4.9224015321516745, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi',), comment="""BM rule fitted to 18 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi
    Total Standard Deviation in ln(k): 5.449729299197225"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 5.449729299197225""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 5.449729299197225
""",
)

entry(
    index = 277,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(2.13448e-07,'m^3/(mol*s)'), n=3.67614, w0=(327,'kJ/mol'), E0=(55.7962,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.41156722767597165, var=6.630689006487045, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R',), comment="""BM rule fitted to 12 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R
    Total Standard Deviation in ln(k): 6.196306251716257"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 6.196306251716257""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 6.196306251716257
""",
)

entry(
    index = 278,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_Ext-5BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(1.68025e-07,'m^3/(mol*s)'), n=3.31968, w0=(327,'kJ/mol'), E0=(65.4921,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_Ext-5BrCFINOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_Ext-5BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_Ext-5BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_Ext-5BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 279,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_5BrCFINOPSSi->O",
    kinetics = ArrheniusBM(A=(1.83193e-06,'m^3/(mol*s)'), n=3.64737, w0=(327,'kJ/mol'), E0=(62.5908,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4373659392636773, var=1.1194708618345255, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_5BrCFINOPSSi->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_5BrCFINOPSSi->O
    Total Standard Deviation in ln(k): 3.2200203473559563"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_5BrCFINOPSSi->O
Total Standard Deviation in ln(k): 3.2200203473559563""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_5BrCFINOPSSi->O
Total Standard Deviation in ln(k): 3.2200203473559563
""",
)

entry(
    index = 280,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_5BrCFINOPSSi->O_6R!H->C",
    kinetics = ArrheniusBM(A=(6.13084e-08,'m^3/(mol*s)'), n=4.04025, w0=(327,'kJ/mol'), E0=(60.6277,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_5BrCFINOPSSi->O_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_5BrCFINOPSSi->O_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_5BrCFINOPSSi->O_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_5BrCFINOPSSi->O_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 281,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_5BrCFINOPSSi->O_N-6R!H->C",
    kinetics = ArrheniusBM(A=(2.36729e-05,'m^3/(mol*s)'), n=3.35879, w0=(327,'kJ/mol'), E0=(63.6553,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_5BrCFINOPSSi->O_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_5BrCFINOPSSi->O_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_5BrCFINOPSSi->O_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_5BrCFINOPSSi->O_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 282,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O",
    kinetics = ArrheniusBM(A=(5.97744e-06,'m^3/(mol*s)'), n=3.25135, w0=(327,'kJ/mol'), E0=(57.3044,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3253068137668299, var=7.203547581859649, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O',), comment="""BM rule fitted to 9 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O
    Total Standard Deviation in ln(k): 6.197947567985292"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O
Total Standard Deviation in ln(k): 6.197947567985292""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O
Total Standard Deviation in ln(k): 6.197947567985292
""",
)

entry(
    index = 283,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F",
    kinetics = ArrheniusBM(A=(1.26475e-05,'m^3/(mol*s)'), n=3.19208, w0=(327,'kJ/mol'), E0=(56.7921,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.27000268144675865, var=6.832513097118184, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F',), comment="""BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F
    Total Standard Deviation in ln(k): 5.91859101162738"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F
Total Standard Deviation in ln(k): 5.91859101162738""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F
Total Standard Deviation in ln(k): 5.91859101162738
""",
)

entry(
    index = 284,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.46874e-05,'m^3/(mol*s)'), n=2.98067, w0=(327,'kJ/mol'), E0=(56.8714,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.19141530621034533, var=8.236154071246672, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R
    Total Standard Deviation in ln(k): 6.2342721258254805"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R
Total Standard Deviation in ln(k): 6.2342721258254805""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R
Total Standard Deviation in ln(k): 6.2342721258254805
""",
)

entry(
    index = 285,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.000327626,'m^3/(mol*s)'), n=3.00816, w0=(327,'kJ/mol'), E0=(57.3529,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.005821990480834724, var=4.3707258080189275, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 4.205783581310472"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 4.205783581310472""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 4.205783581310472
""",
)

entry(
    index = 286,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_Ext-1C-R_7R!H->Br",
    kinetics = ArrheniusBM(A=(4.48911e-05,'m^3/(mol*s)'), n=3.19144, w0=(327,'kJ/mol'), E0=(57.6119,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_Ext-1C-R_7R!H->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_Ext-1C-R_7R!H->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_Ext-1C-R_7R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_Ext-1C-R_7R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 287,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_Ext-1C-R_N-7R!H->Br",
    kinetics = ArrheniusBM(A=(0.000113941,'m^3/(mol*s)'), n=3.20363, w0=(327,'kJ/mol'), E0=(53.8029,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_Ext-1C-R_N-7R!H->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_Ext-1C-R_N-7R!H->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_Ext-1C-R_N-7R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_Ext-1C-R_N-7R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 288,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_7R!H->Br",
    kinetics = ArrheniusBM(A=(5.12823e-06,'m^3/(mol*s)'), n=3.42232, w0=(327,'kJ/mol'), E0=(65.1727,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_7R!H->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_7R!H->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_7R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_7R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 289,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br",
    kinetics = ArrheniusBM(A=(2.63443e-05,'m^3/(mol*s)'), n=2.74238, w0=(327,'kJ/mol'), E0=(54.3984,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.28796504839758613, var=11.599364947218016, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br
    Total Standard Deviation in ln(k): 7.5512250092883395"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br
Total Standard Deviation in ln(k): 7.5512250092883395""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br
Total Standard Deviation in ln(k): 7.5512250092883395
""",
)

entry(
    index = 290,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br_6R!H->C",
    kinetics = ArrheniusBM(A=(1.8714e-07,'m^3/(mol*s)'), n=3.7897, w0=(327,'kJ/mol'), E0=(52.2732,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 291,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br_N-6R!H->C",
    kinetics = ArrheniusBM(A=(0.000109305,'m^3/(mol*s)'), n=2.34946, w0=(327,'kJ/mol'), E0=(54.3289,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.24333587676193436, var=0.003884290190083349, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br_N-6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br_N-6R!H->C
    Total Standard Deviation in ln(k): 0.7363399324363427"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br_N-6R!H->C
Total Standard Deviation in ln(k): 0.7363399324363427""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br_N-6R!H->C
Total Standard Deviation in ln(k): 0.7363399324363427
""",
)

entry(
    index = 292,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br_N-6R!H->C_7CF->C",
    kinetics = ArrheniusBM(A=(0.000181891,'m^3/(mol*s)'), n=2.18883, w0=(327,'kJ/mol'), E0=(48.8442,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br_N-6R!H->C_7CF->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br_N-6R!H->C_7CF->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br_N-6R!H->C_7CF->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br_N-6R!H->C_7CF->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 293,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br_N-6R!H->C_N-7CF->C",
    kinetics = ArrheniusBM(A=(6.47964e-05,'m^3/(mol*s)'), n=2.51178, w0=(327,'kJ/mol'), E0=(59.7909,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br_N-6R!H->C_N-7CF->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br_N-6R!H->C_N-7CF->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br_N-6R!H->C_N-7CF->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_Ext-1C-R_N-7R!H->Br_N-6R!H->C_N-7CF->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 294,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_6R!H->C",
    kinetics = ArrheniusBM(A=(4.44292e-07,'m^3/(mol*s)'), n=3.98555, w0=(327,'kJ/mol'), E0=(56.4543,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 295,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_N-6R!H->C",
    kinetics = ArrheniusBM(A=(5.96633e-07,'m^3/(mol*s)'), n=3.71051, w0=(327,'kJ/mol'), E0=(56.2791,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_5CF->F_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 296,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_N-5CF->F",
    kinetics = ArrheniusBM(A=(9.18426e-08,'m^3/(mol*s)'), n=3.49906, w0=(327,'kJ/mol'), E0=(63.3623,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_N-5CF->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_N-5CF->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_N-5CF->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-3BrCClFINOPSSi-R_N-5BrCFINOPSSi->O_N-5CF->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 297,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6.18612e-06,'m^3/(mol*s)'), n=3.39168, w0=(327,'kJ/mol'), E0=(58.0734,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.22389280612221907, var=0.5503650895053545, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-1C-R
    Total Standard Deviation in ln(k): 2.049789434035394"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-1C-R
Total Standard Deviation in ln(k): 2.049789434035394""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-1C-R
Total Standard Deviation in ln(k): 2.049789434035394
""",
)

entry(
    index = 298,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-1C-R_Ext-5BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(6.70266e-07,'m^3/(mol*s)'), n=3.70279, w0=(327,'kJ/mol'), E0=(55.6126,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-1C-R_Ext-5BrCFINOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-1C-R_Ext-5BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-1C-R_Ext-5BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_Ext-1C-R_Ext-5BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 299,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_5BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(5.95401e-06,'m^3/(mol*s)'), n=3.69212, w0=(327,'kJ/mol'), E0=(75.5601,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3801414558597131, var=6.6119543686555735, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_5BrCFINOPSSi->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_5BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 6.110049089880831"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 6.110049089880831""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 6.110049089880831
""",
)

entry(
    index = 300,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_5BrCFINOPSSi->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(3.5219e-07,'m^3/(mol*s)'), n=3.88087, w0=(327,'kJ/mol'), E0=(71.3039,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_5BrCFINOPSSi->C_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_5BrCFINOPSSi->C_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_5BrCFINOPSSi->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_5BrCFINOPSSi->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 301,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-5BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.05107e-07,'m^3/(mol*s)'), n=4.2635, w0=(327,'kJ/mol'), E0=(66.5673,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-5BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-5BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 302,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi",
    kinetics = ArrheniusBM(A=(1.05487e-07,'m^3/(mol*s)'), n=4.21828, w0=(327,'kJ/mol'), E0=(59.9484,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.49742720173349747, var=3.4685462261495235, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi
    Total Standard Deviation in ln(k): 4.983442407356837"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 4.983442407356837""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 4.983442407356837
""",
)

entry(
    index = 303,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_5BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.19067e-07,'m^3/(mol*s)'), n=4.28135, w0=(327,'kJ/mol'), E0=(61.1284,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5120348907560373, var=7.463252313576021, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_5BrCFINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_5BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 6.763246302377868"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 6.763246302377868""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 6.763246302377868
""",
)

entry(
    index = 304,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_5BrCFINOPSSi->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(5.16237e-08,'m^3/(mol*s)'), n=4.56633, w0=(327,'kJ/mol'), E0=(63.1935,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_5BrCFINOPSSi->C_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_5BrCFINOPSSi->C_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_5BrCFINOPSSi->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_5BrCFINOPSSi->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 305,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-5BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(4.23604e-06,'m^3/(mol*s)'), n=3.60249, w0=(327,'kJ/mol'), E0=(61.8405,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-5BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-5BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-3BrCClFINOPSSi-R_N-5R!H->Cl_N-Sp-5BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 306,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(103.348,'m^3/(mol*s)'), n=0.814439, w0=(327,'kJ/mol'), E0=(74.8686,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.31694563762874695, var=14.180392373659329, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 8.345548990018859"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 8.345548990018859""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 8.345548990018859
""",
)

entry(
    index = 307,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_5R!H->F",
    kinetics = ArrheniusBM(A=(0.00138208,'m^3/(mol*s)'), n=2.70635, w0=(327,'kJ/mol'), E0=(59.775,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 308,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(886.449,'m^3/(mol*s)'), n=0.447918, w0=(327,'kJ/mol'), E0=(77.7835,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2931988065691029, var=13.260045345558652, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F
    Total Standard Deviation in ln(k): 8.036791927868956"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F
Total Standard Deviation in ln(k): 8.036791927868956""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F
Total Standard Deviation in ln(k): 8.036791927868956
""",
)

entry(
    index = 309,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->Cl",
    kinetics = ArrheniusBM(A=(3.00115e-05,'m^3/(mol*s)'), n=2.67815, w0=(327,'kJ/mol'), E0=(56.2724,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.16395212079425261, var=17.63843159862718, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->Cl
    Total Standard Deviation in ln(k): 8.831453005724747"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->Cl
Total Standard Deviation in ln(k): 8.831453005724747""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->Cl
Total Standard Deviation in ln(k): 8.831453005724747
""",
)

entry(
    index = 310,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->Cl_Ext-1C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(5.07841e-05,'m^3/(mol*s)'), n=2.8807, w0=(327,'kJ/mol'), E0=(59.7545,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->Cl_Ext-1C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->Cl_Ext-1C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->Cl_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->Cl_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 311,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->Cl_Ext-1C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(0.00171439,'m^3/(mol*s)'), n=1.9068, w0=(327,'kJ/mol'), E0=(57.691,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->Cl_Ext-1C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->Cl_Ext-1C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->Cl_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->Cl_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 312,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->Cl",
    kinetics = ArrheniusBM(A=(1.03613e+07,'m^3/(mol*s)'), n=-0.777467, w0=(327,'kJ/mol'), E0=(90.0539,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.33416279119718334, var=29.51893773375132, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->Cl',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->Cl
    Total Standard Deviation in ln(k): 11.73159796099847"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->Cl
Total Standard Deviation in ln(k): 11.73159796099847""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->Cl
Total Standard Deviation in ln(k): 11.73159796099847
""",
)

entry(
    index = 313,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_Sp-5BrC-1C",
    kinetics = ArrheniusBM(A=(0.0284234,'m^3/(mol*s)'), n=1.36627, w0=(327,'kJ/mol'), E0=(67.5052,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.23832714189856924, var=2.3453459392659277, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_Sp-5BrC-1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_Sp-5BrC-1C
    Total Standard Deviation in ln(k): 3.6689679234029113"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_Sp-5BrC-1C
Total Standard Deviation in ln(k): 3.6689679234029113""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_Sp-5BrC-1C
Total Standard Deviation in ln(k): 3.6689679234029113
""",
)

entry(
    index = 314,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_Sp-5BrC-1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.0839921,'m^3/(mol*s)'), n=1.12937, w0=(327,'kJ/mol'), E0=(57.529,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_Sp-5BrC-1C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_Sp-5BrC-1C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_Sp-5BrC-1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_Sp-5BrC-1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 315,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_N-Sp-5BrC-1C",
    kinetics = ArrheniusBM(A=(6.62337e-05,'m^3/(mol*s)'), n=3.0485, w0=(327,'kJ/mol'), E0=(63.7888,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_N-Sp-5BrC-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_N-Sp-5BrC-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_N-Sp-5BrC-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_4R!H->Cl_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->Cl_N-Sp-5BrC-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 316,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(484885,'m^3/(mol*s)'), n=0.288905, w0=(326.59,'kJ/mol'), E0=(85.3367,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1459339938311444, var=6.681289516511121, Tref=1000.0, N=67, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl',), comment="""BM rule fitted to 67 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 5.5485457426255484"""),
    rank = 11,
    shortDesc = """BM rule fitted to 67 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 5.5485457426255484""",
    longDesc = 
"""
BM rule fitted to 67 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 5.5485457426255484
""",
)

entry(
    index = 317,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1",
    kinetics = ArrheniusBM(A=(90.0427,'m^3/(mol*s)'), n=1.30426, w0=(326.549,'kJ/mol'), E0=(76.3861,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04946413762411095, var=4.765523725364202, Tref=1000.0, N=61, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1',), comment="""BM rule fitted to 61 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1
    Total Standard Deviation in ln(k): 4.50063437158314"""),
    rank = 11,
    shortDesc = """BM rule fitted to 61 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1
Total Standard Deviation in ln(k): 4.50063437158314""",
    longDesc = 
"""
BM rule fitted to 61 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1
Total Standard Deviation in ln(k): 4.50063437158314
""",
)

entry(
    index = 318,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi",
    kinetics = ArrheniusBM(A=(17.2009,'m^3/(mol*s)'), n=1.49224, w0=(326.5,'kJ/mol'), E0=(74.5777,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.02574785269452865, var=4.851988688227253, Tref=1000.0, N=55, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi',), comment="""BM rule fitted to 55 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi
    Total Standard Deviation in ln(k): 4.4805691945512685"""),
    rank = 11,
    shortDesc = """BM rule fitted to 55 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 4.4805691945512685""",
    longDesc = 
"""
BM rule fitted to 55 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 4.4805691945512685
""",
)

entry(
    index = 319,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F",
    kinetics = ArrheniusBM(A=(0.0437704,'m^3/(mol*s)'), n=2.32835, w0=(327,'kJ/mol'), E0=(65.6506,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07483488222036268, var=3.6299290320151987, Tref=1000.0, N=29, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F',), comment="""BM rule fitted to 29 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F
    Total Standard Deviation in ln(k): 4.007523316098835"""),
    rank = 11,
    shortDesc = """BM rule fitted to 29 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F
Total Standard Deviation in ln(k): 4.007523316098835""",
    longDesc = 
"""
BM rule fitted to 29 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F
Total Standard Deviation in ln(k): 4.007523316098835
""",
)

entry(
    index = 320,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.173631,'m^3/(mol*s)'), n=2.13343, w0=(327,'kJ/mol'), E0=(66.5917,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.13397517068028633, var=3.794436440724575, Tref=1000.0, N=26, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R',), comment="""BM rule fitted to 26 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R
    Total Standard Deviation in ln(k): 4.241707284256231"""),
    rank = 11,
    shortDesc = """BM rule fitted to 26 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R
Total Standard Deviation in ln(k): 4.241707284256231""",
    longDesc = 
"""
BM rule fitted to 26 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R
Total Standard Deviation in ln(k): 4.241707284256231
""",
)

entry(
    index = 321,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(0.0058422,'m^3/(mol*s)'), n=2.62731, w0=(327,'kJ/mol'), E0=(59.9691,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1214629614343445, var=2.7549260493723766, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl',), comment="""BM rule fitted to 14 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl
    Total Standard Deviation in ln(k): 3.6326365682139006"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl
Total Standard Deviation in ln(k): 3.6326365682139006""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl
Total Standard Deviation in ln(k): 3.6326365682139006
""",
)

entry(
    index = 322,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(1.0537e-05,'m^3/(mol*s)'), n=3.48098, w0=(327,'kJ/mol'), E0=(53.7822,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.051704143459487956, var=1.5991884456339824, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R
    Total Standard Deviation in ln(k): 2.665078297489345"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 2.665078297489345""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 2.665078297489345
""",
)

entry(
    index = 323,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->Br",
    kinetics = ArrheniusBM(A=(9.20334e-05,'m^3/(mol*s)'), n=3.18628, w0=(327,'kJ/mol'), E0=(57.6279,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_6R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 324,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br",
    kinetics = ArrheniusBM(A=(2.24329e-06,'m^3/(mol*s)'), n=3.67659, w0=(327,'kJ/mol'), E0=(51.8348,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.07577241556703265, var=1.8324587267190775, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br',), comment="""BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br
    Total Standard Deviation in ln(k): 2.904159534012147"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br
Total Standard Deviation in ln(k): 2.904159534012147""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br
Total Standard Deviation in ln(k): 2.904159534012147
""",
)

entry(
    index = 325,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(22.4051,'m^3/(mol*s)'), n=1.40381, w0=(327,'kJ/mol'), E0=(63.4913,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04892586636372716, var=17.314438203026047, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C
    Total Standard Deviation in ln(k): 8.46475656062923"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C
Total Standard Deviation in ln(k): 8.46475656062923""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C
Total Standard Deviation in ln(k): 8.46475656062923
""",
)

entry(
    index = 326,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C_Ext-3BrCClFINOPSSi-R_Ext-1C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(6.69523e-06,'m^3/(mol*s)'), n=3.1208, w0=(327,'kJ/mol'), E0=(49.7125,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C_Ext-3BrCClFINOPSSi-R_Ext-1C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C_Ext-3BrCClFINOPSSi-R_Ext-1C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C_Ext-3BrCClFINOPSSi-R_Ext-1C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C_Ext-3BrCClFINOPSSi-R_Ext-1C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 327,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C_Ext-3BrCClFINOPSSi-R_Ext-1C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(9.80672e-05,'m^3/(mol*s)'), n=3.09159, w0=(327,'kJ/mol'), E0=(45.7667,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C_Ext-3BrCClFINOPSSi-R_Ext-1C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C_Ext-3BrCClFINOPSSi-R_Ext-1C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C_Ext-3BrCClFINOPSSi-R_Ext-1C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C_Ext-3BrCClFINOPSSi-R_Ext-1C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 328,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(6.60787e-08,'m^3/(mol*s)'), n=4.20431, w0=(327,'kJ/mol'), E0=(50.0769,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.10426054408096201, var=0.7841914305754356, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C
    Total Standard Deviation in ln(k): 2.0372459694055873"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C
Total Standard Deviation in ln(k): 2.0372459694055873""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C
Total Standard Deviation in ln(k): 2.0372459694055873
""",
)

entry(
    index = 329,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(4.07354e-08,'m^3/(mol*s)'), n=4.25023, w0=(327,'kJ/mol'), E0=(49.3377,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.07129860478036713, var=0.9002192678815326, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R
    Total Standard Deviation in ln(k): 2.0812325697440563"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 2.0812325697440563""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 2.0812325697440563
""",
)

entry(
    index = 330,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl",
    kinetics = ArrheniusBM(A=(1.92308e-06,'m^3/(mol*s)'), n=3.76581, w0=(327,'kJ/mol'), E0=(55.0728,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.006645744005414854, var=0.9081207715002358, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl
    Total Standard Deviation in ln(k): 1.9271175768285327"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl
Total Standard Deviation in ln(k): 1.9271175768285327""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl
Total Standard Deviation in ln(k): 1.9271175768285327
""",
)

entry(
    index = 331,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.16099e-06,'m^3/(mol*s)'), n=3.83799, w0=(327,'kJ/mol'), E0=(56.2457,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03390666736334659, var=1.3682738794552087, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 2.430196198022822"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 2.430196198022822""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 2.430196198022822
""",
)

entry(
    index = 332,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl_Ext-1C-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(0.00016077,'m^3/(mol*s)'), n=3.1849, w0=(327,'kJ/mol'), E0=(67.0167,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl_Ext-1C-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl_Ext-1C-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl_Ext-1C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl_Ext-1C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 333,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl_Ext-1C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(0.0001693,'m^3/(mol*s)'), n=3.21727, w0=(327,'kJ/mol'), E0=(58.7533,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl_Ext-1C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl_Ext-1C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl_Ext-1C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl_Ext-1C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 334,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl_Ext-1C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(0.000306394,'m^3/(mol*s)'), n=3.18453, w0=(327,'kJ/mol'), E0=(60.5486,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl_Ext-1C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl_Ext-1C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl_Ext-1C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_7R!H->Cl_Ext-1C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 335,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_N-7R!H->Cl",
    kinetics = ArrheniusBM(A=(0.000250735,'m^3/(mol*s)'), n=3.18369, w0=(327,'kJ/mol'), E0=(53.7024,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_N-7R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_N-7R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_N-7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C_Ext-1C-R_N-7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 336,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl",
    kinetics = ArrheniusBM(A=(0.00116047,'m^3/(mol*s)'), n=2.87695, w0=(327,'kJ/mol'), E0=(56.0073,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.28587153058236664, var=0.10638298856496625, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl
    Total Standard Deviation in ln(k): 1.3721426925973033"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl
Total Standard Deviation in ln(k): 1.3721426925973033""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl
Total Standard Deviation in ln(k): 1.3721426925973033
""",
)

entry(
    index = 337,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_Ext-1C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(0.000570337,'m^3/(mol*s)'), n=2.91943, w0=(327,'kJ/mol'), E0=(51.1905,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_Ext-1C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_Ext-1C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_Ext-1C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_Ext-1C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 338,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_Ext-1C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(0.00164798,'m^3/(mol*s)'), n=2.87921, w0=(327,'kJ/mol'), E0=(60.3788,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_Ext-1C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_Ext-1C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_Ext-1C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->Cl_Ext-1C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 339,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl",
    kinetics = ArrheniusBM(A=(0.00292119,'m^3/(mol*s)'), n=2.47866, w0=(327,'kJ/mol'), E0=(58.1591,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2822321397191193, var=11.707986016907288, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl
    Total Standard Deviation in ln(k): 7.568714848183587"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl
Total Standard Deviation in ln(k): 7.568714848183587""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl
Total Standard Deviation in ln(k): 7.568714848183587
""",
)

entry(
    index = 340,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl_6BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.000302452,'m^3/(mol*s)'), n=2.94956, w0=(327,'kJ/mol'), E0=(55.5206,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2809829152551233, var=0.8898153742801957, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl_6BrCFINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl_6BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 2.5970543373697628"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl_6BrCFINOPSSi->C
Total Standard Deviation in ln(k): 2.5970543373697628""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl_6BrCFINOPSSi->C
Total Standard Deviation in ln(k): 2.5970543373697628
""",
)

entry(
    index = 341,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl_6BrCFINOPSSi->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.000243865,'m^3/(mol*s)'), n=2.90704, w0=(327,'kJ/mol'), E0=(53.8922,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl_6BrCFINOPSSi->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl_6BrCFINOPSSi->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl_6BrCFINOPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl_6BrCFINOPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 342,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl_N-6BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.0210198,'m^3/(mol*s)'), n=1.85566, w0=(327,'kJ/mol'), E0=(60.6698,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl_N-6BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl_N-6BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl_N-6BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->Cl_N-6BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 343,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(0.00266595,'m^3/(mol*s)'), n=2.56931, w0=(327,'kJ/mol'), E0=(65.4115,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05130091348385007, var=4.001102073538313, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl',), comment="""BM rule fitted to 12 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 4.13891922566585"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 4.13891922566585""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 4.13891922566585
""",
)

entry(
    index = 344,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(0.000113077,'m^3/(mol*s)'), n=3.17042, w0=(327,'kJ/mol'), E0=(62.7216,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.10256139900568542, var=1.8217388439869158, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->Br',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->Br
    Total Standard Deviation in ln(k): 2.96351909862929"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 2.96351909862929""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 2.96351909862929
""",
)

entry(
    index = 345,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->Br_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.000463548,'m^3/(mol*s)'), n=3.00555, w0=(327,'kJ/mol'), E0=(61.0403,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.24091837443447006, var=2.718379826495783, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->Br_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->Br_Ext-1C-R
    Total Standard Deviation in ln(k): 3.9106314920492955"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->Br_Ext-1C-R
Total Standard Deviation in ln(k): 3.9106314920492955""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->Br_Ext-1C-R
Total Standard Deviation in ln(k): 3.9106314920492955
""",
)

entry(
    index = 346,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->Br_Ext-1C-R_Ext-3BrCClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(0.0001815,'m^3/(mol*s)'), n=3.18568, w0=(327,'kJ/mol'), E0=(59.7319,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->Br_Ext-1C-R_Ext-3BrCClFINOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->Br_Ext-1C-R_Ext-3BrCClFINOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->Br_Ext-1C-R_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->Br_Ext-1C-R_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 347,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(0.00244741,'m^3/(mol*s)'), n=2.51066, w0=(327,'kJ/mol'), E0=(65.0815,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.02080857759060292, var=4.586385714061141, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br',), comment="""BM rule fitted to 9 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br
    Total Standard Deviation in ln(k): 4.345593149018728"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 4.345593149018728""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 4.345593149018728
""",
)

entry(
    index = 348,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_Ext-5CFO-R",
    kinetics = ArrheniusBM(A=(0.000171298,'m^3/(mol*s)'), n=3.19295, w0=(327,'kJ/mol'), E0=(65.9496,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_Ext-5CFO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_Ext-5CFO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_Ext-5CFO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_Ext-5CFO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 349,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CFO->O",
    kinetics = ArrheniusBM(A=(0.00289119,'m^3/(mol*s)'), n=2.26603, w0=(327,'kJ/mol'), E0=(71.5532,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CFO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CFO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CFO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CFO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 350,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O",
    kinetics = ArrheniusBM(A=(0.00190676,'m^3/(mol*s)'), n=2.52351, w0=(327,'kJ/mol'), E0=(63.3823,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0507937322781478, var=4.473499728569895, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O',), comment="""BM rule fitted to 7 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O
    Total Standard Deviation in ln(k): 4.367767332436508"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O
Total Standard Deviation in ln(k): 4.367767332436508""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O
Total Standard Deviation in ln(k): 4.367767332436508
""",
)

entry(
    index = 351,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(0.00113909,'m^3/(mol*s)'), n=2.6132, w0=(327,'kJ/mol'), E0=(65.0225,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06643126573811964, var=6.242912481968694, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R
    Total Standard Deviation in ln(k): 5.175907896182195"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 5.175907896182195""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 5.175907896182195
""",
)

entry(
    index = 352,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_6R!H->Br",
    kinetics = ArrheniusBM(A=(0.000169094,'m^3/(mol*s)'), n=3.20047, w0=(327,'kJ/mol'), E0=(59.8486,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_6R!H->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_6R!H->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_6R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_6R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 353,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br",
    kinetics = ArrheniusBM(A=(0.000189035,'m^3/(mol*s)'), n=2.7492, w0=(327,'kJ/mol'), E0=(63.8704,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.10503034008838728, var=3.9217648860701244, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br
    Total Standard Deviation in ln(k): 4.233961688395636"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br
Total Standard Deviation in ln(k): 4.233961688395636""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br
Total Standard Deviation in ln(k): 4.233961688395636
""",
)

entry(
    index = 354,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(3.38381e-05,'m^3/(mol*s)'), n=2.98964, w0=(327,'kJ/mol'), E0=(61.0559,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.16918748334924372, var=6.087897097272554, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C
    Total Standard Deviation in ln(k): 5.371510209211474"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C
Total Standard Deviation in ln(k): 5.371510209211474""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C
Total Standard Deviation in ln(k): 5.371510209211474
""",
)

entry(
    index = 355,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C_Ext-3BrCClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(8.80861e-05,'m^3/(mol*s)'), n=2.76058, w0=(327,'kJ/mol'), E0=(61.3988,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.14869480890608802, var=11.077292793476966, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C_Ext-3BrCClFINOPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C_Ext-3BrCClFINOPSSi-R
    Total Standard Deviation in ln(k): 7.045878040434148"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 7.045878040434148""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 7.045878040434148
""",
)

entry(
    index = 356,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C_Ext-3BrCClFINOPSSi-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.000241094,'m^3/(mol*s)'), n=2.88397, w0=(327,'kJ/mol'), E0=(65.9685,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C_Ext-3BrCClFINOPSSi-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C_Ext-3BrCClFINOPSSi-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C_Ext-3BrCClFINOPSSi-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_6CClFINOPSSi->C_Ext-3BrCClFINOPSSi-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 357,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.0200628,'m^3/(mol*s)'), n=2.08964, w0=(327,'kJ/mol'), E0=(71.7688,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-3BrCClFINOPSSi-R_N-6R!H->Br_N-6CClFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 358,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.0148734,'m^3/(mol*s)'), n=1.93367, w0=(327,'kJ/mol'), E0=(55.333,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CFO->O_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 359,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-3BrCClFINOPSSi-R_5R!H->Br",
    kinetics = ArrheniusBM(A=(1.55016e-06,'m^3/(mol*s)'), n=3.70765, w0=(327,'kJ/mol'), E0=(60.7022,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-3BrCClFINOPSSi-R_5R!H->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-3BrCClFINOPSSi-R_5R!H->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-3BrCClFINOPSSi-R_5R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-3BrCClFINOPSSi-R_5R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 360,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-3BrCClFINOPSSi-R_N-5R!H->Br",
    kinetics = ArrheniusBM(A=(2.86253e-05,'m^3/(mol*s)'), n=3.49359, w0=(327,'kJ/mol'), E0=(61.8935,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3604895888584518, var=4.7773852221737245, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-3BrCClFINOPSSi-R_N-5R!H->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-3BrCClFINOPSSi-R_N-5R!H->Br
    Total Standard Deviation in ln(k): 5.287548390271309"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-3BrCClFINOPSSi-R_N-5R!H->Br
Total Standard Deviation in ln(k): 5.287548390271309""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-3BrCClFINOPSSi-R_N-5R!H->Br
Total Standard Deviation in ln(k): 5.287548390271309
""",
)

entry(
    index = 361,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-3BrCClFINOPSSi-R_N-5R!H->Br_Ext-3BrCClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(2.91371e-05,'m^3/(mol*s)'), n=3.55919, w0=(327,'kJ/mol'), E0=(59.5742,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-3BrCClFINOPSSi-R_N-5R!H->Br_Ext-3BrCClFINOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-3BrCClFINOPSSi-R_N-5R!H->Br_Ext-3BrCClFINOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-3BrCClFINOPSSi-R_N-5R!H->Br_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->F_Ext-3BrCClFINOPSSi-R_N-5R!H->Br_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 362,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F",
    kinetics = ArrheniusBM(A=(3831.65,'m^3/(mol*s)'), n=0.716064, w0=(325.942,'kJ/mol'), E0=(83.1887,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.057395005676930885, var=5.16524719335484, Tref=1000.0, N=26, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F',), comment="""BM rule fitted to 26 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F
    Total Standard Deviation in ln(k): 4.700406090457389"""),
    rank = 11,
    shortDesc = """BM rule fitted to 26 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F
Total Standard Deviation in ln(k): 4.700406090457389""",
    longDesc = 
"""
BM rule fitted to 26 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F
Total Standard Deviation in ln(k): 4.700406090457389
""",
)

entry(
    index = 363,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.00012332,'m^3/(mol*s)'), n=2.83695, w0=(327,'kJ/mol'), E0=(64.9169,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2327813422701447, var=3.618100292830344, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C',), comment="""BM rule fitted to 25 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 4.398145402485485"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 4.398145402485485""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 4.398145402485485
""",
)

entry(
    index = 364,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.0775929,'m^3/(mol*s)'), n=1.78747, w0=(327,'kJ/mol'), E0=(62.7378,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05743515449925945, var=5.223448996425793, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R',), comment="""BM rule fitted to 11 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R
    Total Standard Deviation in ln(k): 4.726104588317167"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 4.726104588317167""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 4.726104588317167
""",
)

entry(
    index = 365,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.0670923,'m^3/(mol*s)'), n=1.88425, w0=(327,'kJ/mol'), E0=(57.5021,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.24855384430607694, var=4.065978546401393, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 4.666909432408856"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 4.666909432408856""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 4.666909432408856
""",
)

entry(
    index = 366,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.00436905,'m^3/(mol*s)'), n=2.22929, w0=(327,'kJ/mol'), E0=(51.5289,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.24590351320160977, var=5.966751843350412, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 5.514801492448601"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 5.514801492448601""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 5.514801492448601
""",
)

entry(
    index = 367,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C",
    kinetics = ArrheniusBM(A=(0.0511571,'m^3/(mol*s)'), n=1.81831, w0=(327,'kJ/mol'), E0=(48.6319,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6976210790274141, var=14.963630754846362, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C
    Total Standard Deviation in ln(k): 9.507703906199705"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C
Total Standard Deviation in ln(k): 9.507703906199705""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C
Total Standard Deviation in ln(k): 9.507703906199705
""",
)

entry(
    index = 368,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C_5R!H->F",
    kinetics = ArrheniusBM(A=(153.473,'m^3/(mol*s)'), n=0.90913, w0=(327,'kJ/mol'), E0=(59.6855,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.14981805003780188, var=36.8111757966334, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C_5R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C_5R!H->F
    Total Standard Deviation in ln(k): 12.539598870559296"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C_5R!H->F
Total Standard Deviation in ln(k): 12.539598870559296""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C_5R!H->F
Total Standard Deviation in ln(k): 12.539598870559296
""",
)

entry(
    index = 369,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C_5R!H->F_6R!H->F",
    kinetics = ArrheniusBM(A=(0.00843525,'m^3/(mol*s)'), n=1.82185, w0=(327,'kJ/mol'), E0=(49.2454,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C_5R!H->F_6R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C_5R!H->F_6R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C_5R!H->F_6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C_5R!H->F_6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 370,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C_5R!H->F_N-6R!H->F",
    kinetics = ArrheniusBM(A=(0.000319131,'m^3/(mol*s)'), n=2.84493, w0=(327,'kJ/mol'), E0=(45.047,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C_5R!H->F_N-6R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C_5R!H->F_N-6R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C_5R!H->F_N-6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C_5R!H->F_N-6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 371,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C_N-5R!H->F",
    kinetics = ArrheniusBM(A=(0.00897965,'m^3/(mol*s)'), n=1.86068, w0=(327,'kJ/mol'), E0=(41.2724,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C_N-5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C_N-5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_4BrCO->C_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 372,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_N-4BrCO->C",
    kinetics = ArrheniusBM(A=(0.000909656,'m^3/(mol*s)'), n=2.73905, w0=(327,'kJ/mol'), E0=(66.0122,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_N-4BrCO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_N-4BrCO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_N-4BrCO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R_N-4BrCO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 373,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_4BrCO->C",
    kinetics = ArrheniusBM(A=(0.00177736,'m^3/(mol*s)'), n=1.98145, w0=(327,'kJ/mol'), E0=(48.7509,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_4BrCO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_4BrCO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_4BrCO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_4BrCO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 374,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_N-4BrCO->C",
    kinetics = ArrheniusBM(A=(0.00038912,'m^3/(mol*s)'), n=2.85908, w0=(327,'kJ/mol'), E0=(68.4042,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_N-4BrCO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_N-4BrCO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_N-4BrCO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-1C-R_N-4BrCO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 375,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.17428e-06,'m^3/(mol*s)'), n=3.0585, w0=(327,'kJ/mol'), E0=(53.5948,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4104478841303087, var=10.92057473426591, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 7.656182343175322"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-3C-R
Total Standard Deviation in ln(k): 7.656182343175322""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-3C-R
Total Standard Deviation in ln(k): 7.656182343175322
""",
)

entry(
    index = 376,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-3C-R_Ext-4BrCO-R",
    kinetics = ArrheniusBM(A=(2.9359e-06,'m^3/(mol*s)'), n=2.62195, w0=(327,'kJ/mol'), E0=(47.6691,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-3C-R_Ext-4BrCO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-3C-R_Ext-4BrCO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-3C-R_Ext-4BrCO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-3C-R_Ext-4BrCO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 377,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(4.54685e-09,'m^3/(mol*s)'), n=4.29667, w0=(327,'kJ/mol'), E0=(58.3991,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 378,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_4BrCO->C",
    kinetics = ArrheniusBM(A=(0.00102069,'m^3/(mol*s)'), n=2.41392, w0=(327,'kJ/mol'), E0=(64.5003,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_4BrCO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_4BrCO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_4BrCO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_4BrCO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 379,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_N-4BrCO->C",
    kinetics = ArrheniusBM(A=(0.00204844,'m^3/(mol*s)'), n=2.00995, w0=(327,'kJ/mol'), E0=(73.9775,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_N-4BrCO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_N-4BrCO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_N-4BrCO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-1C-R_N-4BrCO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 380,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R",
    kinetics = ArrheniusBM(A=(1.25111e-06,'m^3/(mol*s)'), n=3.53759, w0=(327,'kJ/mol'), E0=(67.8019,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5051931448737018, var=3.011830786426104, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R',), comment="""BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R
    Total Standard Deviation in ln(k): 4.748472461858173"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R
Total Standard Deviation in ln(k): 4.748472461858173""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R
Total Standard Deviation in ln(k): 4.748472461858173
""",
)

entry(
    index = 381,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C",
    kinetics = ArrheniusBM(A=(7.16571e-06,'m^3/(mol*s)'), n=3.43765, w0=(327,'kJ/mol'), E0=(68.6712,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.44404450015095204, var=0.6762410857856621, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C
    Total Standard Deviation in ln(k): 2.764261116987659"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C
Total Standard Deviation in ln(k): 2.764261116987659""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C
Total Standard Deviation in ln(k): 2.764261116987659
""",
)

entry(
    index = 382,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C_Ext-4BrCO-R",
    kinetics = ArrheniusBM(A=(7.02045e-06,'m^3/(mol*s)'), n=3.41341, w0=(327,'kJ/mol'), E0=(68.0484,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4720267468101776, var=0.24932802449970956, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C_Ext-4BrCO-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C_Ext-4BrCO-R
    Total Standard Deviation in ln(k): 2.187016350663417"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C_Ext-4BrCO-R
Total Standard Deviation in ln(k): 2.187016350663417""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C_Ext-4BrCO-R
Total Standard Deviation in ln(k): 2.187016350663417
""",
)

entry(
    index = 383,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C_Ext-4BrCO-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(9.36524e-06,'m^3/(mol*s)'), n=3.29362, w0=(327,'kJ/mol'), E0=(65.4622,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5726525613225978, var=0.2373746448541737, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C_Ext-4BrCO-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C_Ext-4BrCO-R_Ext-3C-R
    Total Standard Deviation in ln(k): 2.41555469037182"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C_Ext-4BrCO-R_Ext-3C-R
Total Standard Deviation in ln(k): 2.41555469037182""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C_Ext-4BrCO-R_Ext-3C-R
Total Standard Deviation in ln(k): 2.41555469037182
""",
)

entry(
    index = 384,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C_Ext-4BrCO-R_Ext-3C-R_Ext-4BrCO-R",
    kinetics = ArrheniusBM(A=(9.26597e-06,'m^3/(mol*s)'), n=3.28359, w0=(327,'kJ/mol'), E0=(66.0345,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C_Ext-4BrCO-R_Ext-3C-R_Ext-4BrCO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C_Ext-4BrCO-R_Ext-3C-R_Ext-4BrCO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C_Ext-4BrCO-R_Ext-3C-R_Ext-4BrCO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C_Ext-4BrCO-R_Ext-3C-R_Ext-4BrCO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 385,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(6.98204e-06,'m^3/(mol*s)'), n=3.27477, w0=(327,'kJ/mol'), E0=(65.6499,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_5R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 386,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(9.02647e-08,'m^3/(mol*s)'), n=3.66936, w0=(327,'kJ/mol'), E0=(66.6523,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6034266307990408, var=4.1569257614547155, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_N-5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_N-5R!H->C
    Total Standard Deviation in ln(k): 5.603509508047966"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_N-5R!H->C
Total Standard Deviation in ln(k): 5.603509508047966""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_N-5R!H->C
Total Standard Deviation in ln(k): 5.603509508047966
""",
)

entry(
    index = 387,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_N-5R!H->C_Ext-4BrCO-R",
    kinetics = ArrheniusBM(A=(1.89638e-08,'m^3/(mol*s)'), n=3.94208, w0=(327,'kJ/mol'), E0=(68.4417,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6242678919200633, var=14.259078368477818, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_N-5R!H->C_Ext-4BrCO-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_N-5R!H->C_Ext-4BrCO-R
    Total Standard Deviation in ln(k): 9.138631480191481"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_N-5R!H->C_Ext-4BrCO-R
Total Standard Deviation in ln(k): 9.138631480191481""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_N-5R!H->C_Ext-4BrCO-R
Total Standard Deviation in ln(k): 9.138631480191481
""",
)

entry(
    index = 388,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_N-5R!H->C_Ext-4BrCO-R_Ext-4BrCO-R",
    kinetics = ArrheniusBM(A=(4.16244e-07,'m^3/(mol*s)'), n=3.30197, w0=(327,'kJ/mol'), E0=(68.2775,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_N-5R!H->C_Ext-4BrCO-R_Ext-4BrCO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_N-5R!H->C_Ext-4BrCO-R_Ext-4BrCO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_N-5R!H->C_Ext-4BrCO-R_Ext-4BrCO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_Ext-4BrCO-R_N-5R!H->C_Ext-4BrCO-R_Ext-4BrCO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 389,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_4BrCO->Br",
    kinetics = ArrheniusBM(A=(5.16897e-05,'m^3/(mol*s)'), n=3.22055, w0=(327,'kJ/mol'), E0=(75.0651,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_4BrCO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_4BrCO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_4BrCO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_4BrCO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 390,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br",
    kinetics = ArrheniusBM(A=(2.44573e-05,'m^3/(mol*s)'), n=3.32082, w0=(327,'kJ/mol'), E0=(68.4285,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3988578912800571, var=1.0055130843922244, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br
    Total Standard Deviation in ln(k): 3.0124091243642828"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br
Total Standard Deviation in ln(k): 3.0124091243642828""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br
Total Standard Deviation in ln(k): 3.0124091243642828
""",
)

entry(
    index = 391,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C",
    kinetics = ArrheniusBM(A=(4.63091e-05,'m^3/(mol*s)'), n=3.18955, w0=(327,'kJ/mol'), E0=(68.8629,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.44319010002380604, var=0.5738921140784249, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C
    Total Standard Deviation in ln(k): 2.6322434020435557"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C
Total Standard Deviation in ln(k): 2.6322434020435557""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C
Total Standard Deviation in ln(k): 2.6322434020435557
""",
)

entry(
    index = 392,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.000127696,'m^3/(mol*s)'), n=3.0088, w0=(327,'kJ/mol'), E0=(67.2966,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5089338681359885, var=1.1756968598115154, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C_Ext-3C-R
    Total Standard Deviation in ln(k): 3.4524536537927086"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C_Ext-3C-R
Total Standard Deviation in ln(k): 3.4524536537927086""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C_Ext-3C-R
Total Standard Deviation in ln(k): 3.4524536537927086
""",
)

entry(
    index = 393,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C_Ext-3C-R_Sp-5R!H-3C",
    kinetics = ArrheniusBM(A=(2.95423e-06,'m^3/(mol*s)'), n=3.37691, w0=(327,'kJ/mol'), E0=(61.1319,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6520097639383396, var=1.0000867819602604, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C_Ext-3C-R_Sp-5R!H-3C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C_Ext-3C-R_Sp-5R!H-3C
    Total Standard Deviation in ln(k): 3.643037550209151"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C_Ext-3C-R_Sp-5R!H-3C
Total Standard Deviation in ln(k): 3.643037550209151""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C_Ext-3C-R_Sp-5R!H-3C
Total Standard Deviation in ln(k): 3.643037550209151
""",
)

entry(
    index = 394,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C_Ext-3C-R_Sp-5R!H-3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(9.46418e-07,'m^3/(mol*s)'), n=3.44684, w0=(327,'kJ/mol'), E0=(59.1061,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C_Ext-3C-R_Sp-5R!H-3C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C_Ext-3C-R_Sp-5R!H-3C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C_Ext-3C-R_Sp-5R!H-3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C_Ext-3C-R_Sp-5R!H-3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 395,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C_Ext-3C-R_N-Sp-5R!H-3C",
    kinetics = ArrheniusBM(A=(4.38666e-06,'m^3/(mol*s)'), n=3.62937, w0=(327,'kJ/mol'), E0=(67.9674,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C_Ext-3C-R_N-Sp-5R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C_Ext-3C-R_N-Sp-5R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C_Ext-3C-R_N-Sp-5R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_4CO->C_Ext-3C-R_N-Sp-5R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 396,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_N-4CO->C",
    kinetics = ArrheniusBM(A=(0.000128276,'m^3/(mol*s)'), n=3.32193, w0=(327,'kJ/mol'), E0=(71.2084,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_N-4CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_N-4CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_3BrCClFINOPSSi->C_N-4BrCO->Br_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 397,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_N-3BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.000874326,'m^3/(mol*s)'), n=3.26345, w0=(299.5,'kJ/mol'), E0=(48.566,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_N-3BrCClFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_N-3BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_N-3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->F_N-3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 398,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi",
    kinetics = ArrheniusBM(A=(1.49335,'m^3/(mol*s)'), n=1.97929, w0=(327,'kJ/mol'), E0=(71.8369,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0016543644631412812, var=5.367881547016808, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi
    Total Standard Deviation in ln(k): 4.648865068617931"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 4.648865068617931""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 4.648865068617931
""",
)

entry(
    index = 399,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(7456.3,'m^3/(mol*s)'), n=0.85624, w0=(327,'kJ/mol'), E0=(80.2491,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.16016389125737263, var=5.89153418015773, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 5.268411592325855"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 5.268411592325855""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 5.268411592325855
""",
)

entry(
    index = 400,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi",
    kinetics = ArrheniusBM(A=(240036,'m^3/(mol*s)'), n=0.529364, w0=(327,'kJ/mol'), E0=(88.6803,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.17505921148046455, var=8.121930162518323, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi
    Total Standard Deviation in ln(k): 6.1531418157356175"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi
Total Standard Deviation in ln(k): 6.1531418157356175""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi
Total Standard Deviation in ln(k): 6.1531418157356175
""",
)

entry(
    index = 401,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.13079e+08,'m^3/(mol*s)'), n=-0.295164, w0=(327,'kJ/mol'), E0=(92.8726,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2789169505989404, var=14.953150320325935, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi_Ext-1C-R
    Total Standard Deviation in ln(k): 8.452967269812186"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi_Ext-1C-R
Total Standard Deviation in ln(k): 8.452967269812186""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi_Ext-1C-R
Total Standard Deviation in ln(k): 8.452967269812186
""",
)

entry(
    index = 402,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi_Ext-1C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(0.00423821,'m^3/(mol*s)'), n=2.23356, w0=(327,'kJ/mol'), E0=(64.9183,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi_Ext-1C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi_Ext-1C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 403,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi_Ext-1C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.429484,'m^3/(mol*s)'), n=2.34667, w0=(327,'kJ/mol'), E0=(71.1674,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0468296525000834, var=0.6855466720236403, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi_Ext-1C-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi_Ext-1C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 1.7775378981041114"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 1.7775378981041114""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 1.7775378981041114
""",
)

entry(
    index = 404,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi_Ext-1C-R_N-5R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.00151048,'m^3/(mol*s)'), n=3.07958, w0=(327,'kJ/mol'), E0=(63.1353,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi_Ext-1C-R_N-5R!H->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi_Ext-1C-R_N-5R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi_Ext-1C-R_N-5R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Sp-4C=3BrCClFINOPSSi_Ext-1C-R_N-5R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 405,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_N-Sp-4C=3BrCClFINOPSSi",
    kinetics = ArrheniusBM(A=(465.895,'m^3/(mol*s)'), n=0.780808, w0=(327,'kJ/mol'), E0=(55.4867,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_N-Sp-4C=3BrCClFINOPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_N-Sp-4C=3BrCClFINOPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_N-Sp-4C=3BrCClFINOPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_N-Sp-4C=3BrCClFINOPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 406,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.000216764,'m^3/(mol*s)'), n=3.39606, w0=(327,'kJ/mol'), E0=(69.0838,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 407,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1",
    kinetics = ArrheniusBM(A=(1.07372e+07,'m^3/(mol*s)'), n=0.449219, w0=(327,'kJ/mol'), E0=(84.75,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12379713313505768, var=9.552269375313532, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1
    Total Standard Deviation in ln(k): 6.507031821682254"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1
Total Standard Deviation in ln(k): 6.507031821682254""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1
Total Standard Deviation in ln(k): 6.507031821682254
""",
)

entry(
    index = 408,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi",
    kinetics = ArrheniusBM(A=(1.66661e+07,'m^3/(mol*s)'), n=0.403472, w0=(327,'kJ/mol'), E0=(86.3405,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11282756987713188, var=13.207125729688357, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi
    Total Standard Deviation in ln(k): 7.569016267545527"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 7.569016267545527""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 7.569016267545527
""",
)

entry(
    index = 409,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.39282e+06,'m^3/(mol*s)'), n=0.635935, w0=(327,'kJ/mol'), E0=(83.0936,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6710046567735851, var=33.20862647082057, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 13.23861342566751"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 13.23861342566751""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 13.23861342566751
""",
)

entry(
    index = 410,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Ext-3BrCClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(4.72341e+09,'m^3/(mol*s)'), n=-0.435693, w0=(327,'kJ/mol'), E0=(88.5721,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5083417333916375, var=90.42338247658445, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Ext-3BrCClFINOPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Ext-3BrCClFINOPSSi-R
    Total Standard Deviation in ln(k): 20.34050898997589"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 20.34050898997589""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_4BrCFINOPSSi->C_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 20.34050898997589
""",
)

entry(
    index = 411,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.13797e+09,'m^3/(mol*s)'), n=-0.00749939, w0=(327,'kJ/mol'), E0=(91.7183,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6531083028950267, var=77.00768444391267, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 19.233332320772167"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 19.233332320772167""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 19.233332320772167
""",
)

entry(
    index = 412,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi",
    kinetics = ArrheniusBM(A=(0.000922302,'m^3/(mol*s)'), n=3.28847, w0=(327,'kJ/mol'), E0=(44.7128,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_Ext-3BrCClFINOPSSi-R_N-4R!H->Cl_N-3BrCClFINOPSSi-u1_N-Sp-4BrCFINOPSSi-3BrBrCCClFFIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 413,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(6.65786e+07,'m^3/(mol*s)'), n=-0.0116872, w0=(299.5,'kJ/mol'), E0=(67.1519,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6619252918922767, var=2.8497698853017295, Tref=1000.0, N=50, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O',), comment="""BM rule fitted to 50 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O
    Total Standard Deviation in ln(k): 5.047374574346249"""),
    rank = 11,
    shortDesc = """BM rule fitted to 50 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O
Total Standard Deviation in ln(k): 5.047374574346249""",
    longDesc = 
"""
BM rule fitted to 50 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O
Total Standard Deviation in ln(k): 5.047374574346249
""",
)

entry(
    index = 414,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.63926e+07,'m^3/(mol*s)'), n=0.0903534, w0=(299.5,'kJ/mol'), E0=(65.6069,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6767165662941109, var=2.7219496933071468, Tref=1000.0, N=48, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R',), comment="""BM rule fitted to 48 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R
    Total Standard Deviation in ln(k): 5.007771432113451"""),
    rank = 11,
    shortDesc = """BM rule fitted to 48 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R
Total Standard Deviation in ln(k): 5.007771432113451""",
    longDesc = 
"""
BM rule fitted to 48 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R
Total Standard Deviation in ln(k): 5.007771432113451
""",
)

entry(
    index = 415,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(6.33349e+08,'m^3/(mol*s)'), n=-0.300829, w0=(299.5,'kJ/mol'), E0=(67.2792,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7465121211773315, var=2.8522063864987635, Tref=1000.0, N=33, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl',), comment="""BM rule fitted to 33 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl
    Total Standard Deviation in ln(k): 5.2613507211952495"""),
    rank = 11,
    shortDesc = """BM rule fitted to 33 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl
Total Standard Deviation in ln(k): 5.2613507211952495""",
    longDesc = 
"""
BM rule fitted to 33 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl
Total Standard Deviation in ln(k): 5.2613507211952495
""",
)

entry(
    index = 416,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.53358e+09,'m^3/(mol*s)'), n=-0.462964, w0=(299.5,'kJ/mol'), E0=(67.7258,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8128141776787615, var=3.1797833676888128, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 21 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 5.617079659126022"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 5.617079659126022""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 5.617079659126022
""",
)

entry(
    index = 417,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F",
    kinetics = ArrheniusBM(A=(0.586849,'m^3/(mol*s)'), n=2.33295, w0=(299.5,'kJ/mol'), E0=(17.6101,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5687317283421407, var=0.7157769047563731, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F
    Total Standard Deviation in ln(k): 3.1250522276350585"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F
Total Standard Deviation in ln(k): 3.1250522276350585""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F
Total Standard Deviation in ln(k): 3.1250522276350585
""",
)

entry(
    index = 418,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F_6R!H->Cl",
    kinetics = ArrheniusBM(A=(1.74981,'m^3/(mol*s)'), n=2.26956, w0=(299.5,'kJ/mol'), E0=(30.7019,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F_6R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F_6R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F_6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F_6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 419,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F_N-6R!H->Cl",
    kinetics = ArrheniusBM(A=(80.7343,'m^3/(mol*s)'), n=1.68395, w0=(299.5,'kJ/mol'), E0=(35.6394,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7480435768597896, var=1.3589656727653516, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F_N-6R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F_N-6R!H->Cl
    Total Standard Deviation in ln(k): 4.216520036938794"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F_N-6R!H->Cl
Total Standard Deviation in ln(k): 4.216520036938794""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F_N-6R!H->Cl
Total Standard Deviation in ln(k): 4.216520036938794
""",
)

entry(
    index = 420,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F_N-6R!H->Cl_6CFO->C",
    kinetics = ArrheniusBM(A=(3.56063,'m^3/(mol*s)'), n=2.01448, w0=(299.5,'kJ/mol'), E0=(26.0893,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F_N-6R!H->Cl_6CFO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F_N-6R!H->Cl_6CFO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F_N-6R!H->Cl_6CFO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F_N-6R!H->Cl_6CFO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 421,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F_N-6R!H->Cl_N-6CFO->C",
    kinetics = ArrheniusBM(A=(2.18952,'m^3/(mol*s)'), n=2.19068, w0=(299.5,'kJ/mol'), E0=(24.772,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F_N-6R!H->Cl_N-6CFO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F_N-6R!H->Cl_N-6CFO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F_N-6R!H->Cl_N-6CFO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_5R!H->F_N-6R!H->Cl_N-6CFO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 422,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(6.18667e+08,'m^3/(mol*s)'), n=-0.29342, w0=(299.5,'kJ/mol'), E0=(67.1745,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8020953971027528, var=3.53218842198869, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F',), comment="""BM rule fitted to 18 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F
    Total Standard Deviation in ln(k): 5.783037672695255"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F
Total Standard Deviation in ln(k): 5.783037672695255""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F
Total Standard Deviation in ln(k): 5.783037672695255
""",
)

entry(
    index = 423,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R",
    kinetics = ArrheniusBM(A=(311932,'m^3/(mol*s)'), n=0.606853, w0=(299.5,'kJ/mol'), E0=(61.562,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7791907623334885, var=3.0948133866027008, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R',), comment="""BM rule fitted to 10 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R
    Total Standard Deviation in ln(k): 5.484512062031866"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R
Total Standard Deviation in ln(k): 5.484512062031866""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R
Total Standard Deviation in ln(k): 5.484512062031866
""",
)

entry(
    index = 424,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl",
    kinetics = ArrheniusBM(A=(9.77223e+06,'m^3/(mol*s)'), n=0.130469, w0=(299.5,'kJ/mol'), E0=(66.7379,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9344303097916957, var=2.755442164439803, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl
    Total Standard Deviation in ln(k): 5.675579769060044"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl
Total Standard Deviation in ln(k): 5.675579769060044""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl
Total Standard Deviation in ln(k): 5.675579769060044
""",
)

entry(
    index = 425,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl_Ext-5CClO-R",
    kinetics = ArrheniusBM(A=(1.98922e+08,'m^3/(mol*s)'), n=-0.295296, w0=(299.5,'kJ/mol'), E0=(66.1768,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.1131811268549248, var=5.845739551942597, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl_Ext-5CClO-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl_Ext-5CClO-R
    Total Standard Deviation in ln(k): 7.643978807524511"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl_Ext-5CClO-R
Total Standard Deviation in ln(k): 7.643978807524511""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl_Ext-5CClO-R
Total Standard Deviation in ln(k): 7.643978807524511
""",
)

entry(
    index = 426,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl_Ext-5CClO-R_Ext-5CClO-R",
    kinetics = ArrheniusBM(A=(4.31182e+09,'m^3/(mol*s)'), n=-0.690684, w0=(299.5,'kJ/mol'), E0=(71.5167,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.1002887319180636, var=18.826951444555757, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl_Ext-5CClO-R_Ext-5CClO-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl_Ext-5CClO-R_Ext-5CClO-R
    Total Standard Deviation in ln(k): 11.46309708647137"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl_Ext-5CClO-R_Ext-5CClO-R
Total Standard Deviation in ln(k): 11.46309708647137""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl_Ext-5CClO-R_Ext-5CClO-R
Total Standard Deviation in ln(k): 11.46309708647137
""",
)

entry(
    index = 427,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl_Ext-5CClO-R_Ext-5CClO-R_3O-u1",
    kinetics = ArrheniusBM(A=(0.211482,'m^3/(mol*s)'), n=2.3853, w0=(299.5,'kJ/mol'), E0=(35.055,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl_Ext-5CClO-R_Ext-5CClO-R_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl_Ext-5CClO-R_Ext-5CClO-R_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl_Ext-5CClO-R_Ext-5CClO-R_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl_Ext-5CClO-R_Ext-5CClO-R_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 428,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl_Ext-5CClO-R_Ext-5CClO-R_N-3O-u1",
    kinetics = ArrheniusBM(A=(12634.9,'m^3/(mol*s)'), n=0.772422, w0=(299.5,'kJ/mol'), E0=(62.7941,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl_Ext-5CClO-R_Ext-5CClO-R_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl_Ext-5CClO-R_Ext-5CClO-R_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl_Ext-5CClO-R_Ext-5CClO-R_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_7R!H->Cl_Ext-5CClO-R_Ext-5CClO-R_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 429,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl",
    kinetics = ArrheniusBM(A=(1.16917e+06,'m^3/(mol*s)'), n=0.474297, w0=(299.5,'kJ/mol'), E0=(62.2677,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.71009902022175, var=4.54576650284829, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl
    Total Standard Deviation in ln(k): 6.058424603445274"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl
Total Standard Deviation in ln(k): 6.058424603445274""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl
Total Standard Deviation in ln(k): 6.058424603445274
""",
)

entry(
    index = 430,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_6R!H->C",
    kinetics = ArrheniusBM(A=(94.1969,'m^3/(mol*s)'), n=1.7043, w0=(299.5,'kJ/mol'), E0=(40.0119,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7704537649084743, var=0.0025939631176078062, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_6R!H->C
    Total Standard Deviation in ln(k): 2.0379165701910584"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_6R!H->C
Total Standard Deviation in ln(k): 2.0379165701910584""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_6R!H->C
Total Standard Deviation in ln(k): 2.0379165701910584
""",
)

entry(
    index = 431,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_6R!H->C_Ext-5CClO-R_Ext-5CClO-R",
    kinetics = ArrheniusBM(A=(101.399,'m^3/(mol*s)'), n=1.7102, w0=(299.5,'kJ/mol'), E0=(40.8947,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_6R!H->C_Ext-5CClO-R_Ext-5CClO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_6R!H->C_Ext-5CClO-R_Ext-5CClO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_6R!H->C_Ext-5CClO-R_Ext-5CClO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_6R!H->C_Ext-5CClO-R_Ext-5CClO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 432,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C",
    kinetics = ArrheniusBM(A=(568002,'m^3/(mol*s)'), n=0.535599, w0=(299.5,'kJ/mol'), E0=(66.9335,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.629986308771963, var=5.0244562229539795, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C
    Total Standard Deviation in ln(k): 6.0765537592100065"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C
Total Standard Deviation in ln(k): 6.0765537592100065""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C
Total Standard Deviation in ln(k): 6.0765537592100065
""",
)

entry(
    index = 433,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_3O-u1",
    kinetics = ArrheniusBM(A=(36.3899,'m^3/(mol*s)'), n=1.93252, w0=(299.5,'kJ/mol'), E0=(50.2509,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 434,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_N-3O-u1",
    kinetics = ArrheniusBM(A=(1691.84,'m^3/(mol*s)'), n=1.19417, w0=(299.5,'kJ/mol'), E0=(62.2826,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5559742852017904, var=3.713553423312238, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_N-3O-u1',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_N-3O-u1
    Total Standard Deviation in ln(k): 5.26016154522043"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_N-3O-u1
Total Standard Deviation in ln(k): 5.26016154522043""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_N-3O-u1
Total Standard Deviation in ln(k): 5.26016154522043
""",
)

entry(
    index = 435,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_N-3O-u1_7BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(2.51973,'m^3/(mol*s)'), n=2.10185, w0=(299.5,'kJ/mol'), E0=(54.2627,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5061970520133109, var=0.02411429484484604, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_N-3O-u1_7BrCFINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_N-3O-u1_7BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 1.583162750605948"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_N-3O-u1_7BrCFINOPSSi->C
Total Standard Deviation in ln(k): 1.583162750605948""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_N-3O-u1_7BrCFINOPSSi->C
Total Standard Deviation in ln(k): 1.583162750605948
""",
)

entry(
    index = 436,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_N-3O-u1_7BrCFINOPSSi->C_Ext-5CClO-R",
    kinetics = ArrheniusBM(A=(0.128823,'m^3/(mol*s)'), n=2.44703, w0=(299.5,'kJ/mol'), E0=(49.0419,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_N-3O-u1_7BrCFINOPSSi->C_Ext-5CClO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_N-3O-u1_7BrCFINOPSSi->C_Ext-5CClO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_N-3O-u1_7BrCFINOPSSi->C_Ext-5CClO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_N-3O-u1_7BrCFINOPSSi->C_Ext-5CClO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 437,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_N-3O-u1_N-7BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(1036.11,'m^3/(mol*s)'), n=1.05979, w0=(299.5,'kJ/mol'), E0=(63.2231,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_N-3O-u1_N-7BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_N-3O-u1_N-7BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_N-3O-u1_N-7BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_Ext-5CClO-R_N-7R!H->Cl_N-6R!H->C_N-3O-u1_N-7BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 438,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C",
    kinetics = ArrheniusBM(A=(1.45119e+13,'m^3/(mol*s)'), n=-1.47238, w0=(299.5,'kJ/mol'), E0=(72.979,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9427751313710645, var=5.6976284167061975, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C
    Total Standard Deviation in ln(k): 7.154025331662652"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C
Total Standard Deviation in ln(k): 7.154025331662652""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C
Total Standard Deviation in ln(k): 7.154025331662652
""",
)

entry(
    index = 439,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_6R!H->C",
    kinetics = ArrheniusBM(A=(7.77045e+10,'m^3/(mol*s)'), n=-0.684996, w0=(299.5,'kJ/mol'), E0=(63.5919,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.5725695453905977, var=16.92448033556847, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_6R!H->C
    Total Standard Deviation in ln(k): 12.198534229164757"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_6R!H->C
Total Standard Deviation in ln(k): 12.198534229164757""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_6R!H->C
Total Standard Deviation in ln(k): 12.198534229164757
""",
)

entry(
    index = 440,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_6R!H->C_3O-u1",
    kinetics = ArrheniusBM(A=(1731.37,'m^3/(mol*s)'), n=1.56133, w0=(299.5,'kJ/mol'), E0=(-11.3361,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_6R!H->C_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_6R!H->C_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_6R!H->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_6R!H->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 441,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_6R!H->C_N-3O-u1",
    kinetics = ArrheniusBM(A=(398.23,'m^3/(mol*s)'), n=1.63639, w0=(299.5,'kJ/mol'), E0=(47.1468,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_6R!H->C_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_6R!H->C_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_6R!H->C_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_6R!H->C_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 442,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_N-6R!H->C",
    kinetics = ArrheniusBM(A=(585529,'m^3/(mol*s)'), n=0.509531, w0=(299.5,'kJ/mol'), E0=(56.7062,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6849632434374909, var=4.800202000537862, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_N-6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_N-6R!H->C
    Total Standard Deviation in ln(k): 6.113260086833194"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_N-6R!H->C
Total Standard Deviation in ln(k): 6.113260086833194""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_N-6R!H->C
Total Standard Deviation in ln(k): 6.113260086833194
""",
)

entry(
    index = 443,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_N-6R!H->C_6ClO->O",
    kinetics = ArrheniusBM(A=(4.69543,'m^3/(mol*s)'), n=2.03929, w0=(299.5,'kJ/mol'), E0=(39.6583,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_N-6R!H->C_6ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_N-6R!H->C_6ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_N-6R!H->C_6ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_N-6R!H->C_6ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 444,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_N-6R!H->C_N-6ClO->O",
    kinetics = ArrheniusBM(A=(6674.28,'m^3/(mol*s)'), n=0.996546, w0=(299.5,'kJ/mol'), E0=(54.1845,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_N-6R!H->C_N-6ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_N-6R!H->C_N-6ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_N-6R!H->C_N-6ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_5CClO->C_N-6R!H->C_N-6ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 445,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C",
    kinetics = ArrheniusBM(A=(7.82975e+06,'m^3/(mol*s)'), n=0.288307, w0=(299.5,'kJ/mol'), E0=(60.5164,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9502847154053109, var=10.164254102671496, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C
    Total Standard Deviation in ln(k): 8.779031612538775"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C
Total Standard Deviation in ln(k): 8.779031612538775""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C
Total Standard Deviation in ln(k): 8.779031612538775
""",
)

entry(
    index = 446,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_3O-u1",
    kinetics = ArrheniusBM(A=(5.47178e-05,'m^3/(mol*s)'), n=3.51961, w0=(299.5,'kJ/mol'), E0=(9.35005,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5987021156435502, var=7.8088741983006535, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_3O-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_3O-u1
    Total Standard Deviation in ln(k): 7.106381131547527"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_3O-u1
Total Standard Deviation in ln(k): 7.106381131547527""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_3O-u1
Total Standard Deviation in ln(k): 7.106381131547527
""",
)

entry(
    index = 447,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_3O-u1_5ClO->O",
    kinetics = ArrheniusBM(A=(0.157359,'m^3/(mol*s)'), n=2.34331, w0=(299.5,'kJ/mol'), E0=(28.0811,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_3O-u1_5ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_3O-u1_5ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_3O-u1_5ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_3O-u1_5ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 448,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_3O-u1_N-5ClO->O",
    kinetics = ArrheniusBM(A=(4.54705,'m^3/(mol*s)'), n=2.29539, w0=(299.5,'kJ/mol'), E0=(39.0368,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_3O-u1_N-5ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_3O-u1_N-5ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_3O-u1_N-5ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_3O-u1_N-5ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 449,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_N-3O-u1",
    kinetics = ArrheniusBM(A=(5.56074e+08,'m^3/(mol*s)'), n=-0.277201, w0=(299.5,'kJ/mol'), E0=(71.1798,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3916721853964625, var=21.12653886861374, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_N-3O-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_N-3O-u1
    Total Standard Deviation in ln(k): 10.198588058678457"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_N-3O-u1
Total Standard Deviation in ln(k): 10.198588058678457""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_N-3O-u1
Total Standard Deviation in ln(k): 10.198588058678457
""",
)

entry(
    index = 450,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_N-3O-u1_5ClO->O",
    kinetics = ArrheniusBM(A=(290.458,'m^3/(mol*s)'), n=1.65322, w0=(299.5,'kJ/mol'), E0=(49.0121,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_N-3O-u1_5ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_N-3O-u1_5ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_N-3O-u1_5ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_N-3O-u1_5ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 451,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_N-3O-u1_N-5ClO->O",
    kinetics = ArrheniusBM(A=(244.231,'m^3/(mol*s)'), n=1.41374, w0=(299.5,'kJ/mol'), E0=(60.5888,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_N-3O-u1_N-5ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_N-3O-u1_N-5ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_N-3O-u1_N-5ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_Ext-1C-R_N-5R!H->F_N-5CClO->C_N-3O-u1_N-5ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 452,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(7.41788e+10,'m^3/(mol*s)'), n=-0.920896, w0=(299.5,'kJ/mol'), E0=(75.3913,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6985940795707578, var=3.9122746919581557, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C
    Total Standard Deviation in ln(k): 5.720521419578762"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 5.720521419578762""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 5.720521419578762
""",
)

entry(
    index = 453,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_Sp-5C-1C",
    kinetics = ArrheniusBM(A=(1.36715e+10,'m^3/(mol*s)'), n=-0.776489, w0=(299.5,'kJ/mol'), E0=(68.5775,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9242793684352515, var=10.25656360672962, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_Sp-5C-1C',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_Sp-5C-1C
    Total Standard Deviation in ln(k): 8.74264850398006"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_Sp-5C-1C
Total Standard Deviation in ln(k): 8.74264850398006""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_Sp-5C-1C
Total Standard Deviation in ln(k): 8.74264850398006
""",
)

entry(
    index = 454,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_Sp-5C-1C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(9.10115e+09,'m^3/(mol*s)'), n=-0.834243, w0=(299.5,'kJ/mol'), E0=(68.6446,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.873917836177602, var=17.373868261261002, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_Sp-5C-1C_Ext-5C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_Sp-5C-1C_Ext-5C-R
    Total Standard Deviation in ln(k): 10.551904681404517"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_Sp-5C-1C_Ext-5C-R
Total Standard Deviation in ln(k): 10.551904681404517""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_Sp-5C-1C_Ext-5C-R
Total Standard Deviation in ln(k): 10.551904681404517
""",
)

entry(
    index = 455,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_Sp-5C-1C_Ext-5C-R_3O-u1",
    kinetics = ArrheniusBM(A=(0.057352,'m^3/(mol*s)'), n=2.53406, w0=(299.5,'kJ/mol'), E0=(25.2986,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_Sp-5C-1C_Ext-5C-R_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_Sp-5C-1C_Ext-5C-R_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_Sp-5C-1C_Ext-5C-R_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_Sp-5C-1C_Ext-5C-R_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 456,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_Sp-5C-1C_Ext-5C-R_N-3O-u1",
    kinetics = ArrheniusBM(A=(215.121,'m^3/(mol*s)'), n=1.19164, w0=(299.5,'kJ/mol'), E0=(49.1875,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_Sp-5C-1C_Ext-5C-R_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_Sp-5C-1C_Ext-5C-R_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_Sp-5C-1C_Ext-5C-R_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_Sp-5C-1C_Ext-5C-R_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 457,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_N-Sp-5C-1C",
    kinetics = ArrheniusBM(A=(6.09578e+11,'m^3/(mol*s)'), n=-1.11696, w0=(299.5,'kJ/mol'), E0=(82.991,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3913258853229997, var=9.688881981674491, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_N-Sp-5C-1C',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_N-Sp-5C-1C
    Total Standard Deviation in ln(k): 7.223363525281837"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_N-Sp-5C-1C
Total Standard Deviation in ln(k): 7.223363525281837""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_N-Sp-5C-1C
Total Standard Deviation in ln(k): 7.223363525281837
""",
)

entry(
    index = 458,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_N-Sp-5C-1C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(71.082,'m^3/(mol*s)'), n=1.78047, w0=(299.5,'kJ/mol'), E0=(62.9922,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_N-Sp-5C-1C_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_N-Sp-5C-1C_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_N-Sp-5C-1C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_N-Sp-5C-1C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 459,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_N-Sp-5C-1C_3O-u1",
    kinetics = ArrheniusBM(A=(2.78211,'m^3/(mol*s)'), n=2.35512, w0=(299.5,'kJ/mol'), E0=(32.5454,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_N-Sp-5C-1C_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_N-Sp-5C-1C_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_N-Sp-5C-1C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_N-Sp-5C-1C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 460,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_N-Sp-5C-1C_N-3O-u1",
    kinetics = ArrheniusBM(A=(40.6724,'m^3/(mol*s)'), n=1.5243, w0=(299.5,'kJ/mol'), E0=(45.298,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_N-Sp-5C-1C_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_N-Sp-5C-1C_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_N-Sp-5C-1C_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->C_N-Sp-5C-1C_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 461,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(2.52225e+09,'m^3/(mol*s)'), n=-0.481706, w0=(299.5,'kJ/mol'), E0=(70.8927,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6517501315881978, var=3.833237990656589, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 5.5625651347211855"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 5.5625651347211855""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 5.5625651347211855
""",
)

entry(
    index = 462,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->F",
    kinetics = ArrheniusBM(A=(0.187594,'m^3/(mol*s)'), n=2.42669, w0=(299.5,'kJ/mol'), E0=(36.6677,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 463,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F",
    kinetics = ArrheniusBM(A=(1.5724e+10,'m^3/(mol*s)'), n=-0.710702, w0=(299.5,'kJ/mol'), E0=(73.2117,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6651727060532027, var=5.135165064173458, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F
    Total Standard Deviation in ln(k): 6.2141988379125666"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F
Total Standard Deviation in ln(k): 6.2141988379125666""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F
Total Standard Deviation in ln(k): 6.2141988379125666
""",
)

entry(
    index = 464,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1",
    kinetics = ArrheniusBM(A=(0.00146245,'m^3/(mol*s)'), n=3.12609, w0=(299.5,'kJ/mol'), E0=(21.9592,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6827319733529622, var=0.519999630815042, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1
    Total Standard Deviation in ln(k): 3.1610414780970713"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1
Total Standard Deviation in ln(k): 3.1610414780970713""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1
Total Standard Deviation in ln(k): 3.1610414780970713
""",
)

entry(
    index = 465,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1_5ClO->O",
    kinetics = ArrheniusBM(A=(0.00543344,'m^3/(mol*s)'), n=2.94383, w0=(299.5,'kJ/mol'), E0=(6.58228,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6461447167857034, var=1.4620930302901531, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1_5ClO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1_5ClO->O
    Total Standard Deviation in ln(k): 4.047545481821978"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1_5ClO->O
Total Standard Deviation in ln(k): 4.047545481821978""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1_5ClO->O
Total Standard Deviation in ln(k): 4.047545481821978
""",
)

entry(
    index = 466,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1_5ClO->O_Sp-5O-1C",
    kinetics = ArrheniusBM(A=(0.176621,'m^3/(mol*s)'), n=2.47253, w0=(299.5,'kJ/mol'), E0=(33.4675,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1_5ClO->O_Sp-5O-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1_5ClO->O_Sp-5O-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1_5ClO->O_Sp-5O-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1_5ClO->O_Sp-5O-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 467,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1_5ClO->O_N-Sp-5O-1C",
    kinetics = ArrheniusBM(A=(0.722892,'m^3/(mol*s)'), n=2.37337, w0=(299.5,'kJ/mol'), E0=(34.5908,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1_5ClO->O_N-Sp-5O-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1_5ClO->O_N-Sp-5O-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1_5ClO->O_N-Sp-5O-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1_5ClO->O_N-Sp-5O-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 468,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1_N-5ClO->O",
    kinetics = ArrheniusBM(A=(0.446215,'m^3/(mol*s)'), n=2.42573, w0=(299.5,'kJ/mol'), E0=(34.8346,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1_N-5ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1_N-5ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1_N-5ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_3O-u1_N-5ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 469,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_N-3O-u1",
    kinetics = ArrheniusBM(A=(940.006,'m^3/(mol*s)'), n=1.21749, w0=(299.5,'kJ/mol'), E0=(63.2529,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.32083809985135014, var=2.777310655401938, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_N-3O-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_N-3O-u1
    Total Standard Deviation in ln(k): 4.147070059218163"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_N-3O-u1
Total Standard Deviation in ln(k): 4.147070059218163""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_N-3O-u1
Total Standard Deviation in ln(k): 4.147070059218163
""",
)

entry(
    index = 470,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_N-3O-u1_5ClO->O",
    kinetics = ArrheniusBM(A=(208.569,'m^3/(mol*s)'), n=1.5036, w0=(299.5,'kJ/mol'), E0=(62.3866,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_N-3O-u1_5ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_N-3O-u1_5ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_N-3O-u1_5ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_N-3O-u1_5ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 471,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_N-3O-u1_N-5ClO->O",
    kinetics = ArrheniusBM(A=(33.1951,'m^3/(mol*s)'), n=1.53476, w0=(299.5,'kJ/mol'), E0=(58.7069,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_N-3O-u1_N-5ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_N-3O-u1_N-5ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_N-3O-u1_N-5ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->F_N-3O-u1_N-5ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 472,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(3.19344e+07,'m^3/(mol*s)'), n=0.05728, w0=(299.5,'kJ/mol'), E0=(70.5696,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5961471610823028, var=2.5461422239195026, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl',), comment="""BM rule fitted to 15 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 4.696739916191951"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 4.696739916191951""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 4.696739916191951
""",
)

entry(
    index = 473,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C",
    kinetics = ArrheniusBM(A=(6.90488e+08,'m^3/(mol*s)'), n=-0.29046, w0=(299.5,'kJ/mol'), E0=(81.9176,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.48687213989410666, var=4.341822172535553, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C
    Total Standard Deviation in ln(k): 5.400571243616051"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C
Total Standard Deviation in ln(k): 5.400571243616051""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C
Total Standard Deviation in ln(k): 5.400571243616051
""",
)

entry(
    index = 474,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_3O-u1",
    kinetics = ArrheniusBM(A=(7.69795e+10,'m^3/(mol*s)'), n=-0.781775, w0=(299.5,'kJ/mol'), E0=(86.5993,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5399798940853445, var=16.697123782491353, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_3O-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_3O-u1
    Total Standard Deviation in ln(k): 9.54850477287158"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_3O-u1
Total Standard Deviation in ln(k): 9.54850477287158""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_3O-u1
Total Standard Deviation in ln(k): 9.54850477287158
""",
)

entry(
    index = 475,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_3O-u1_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.13444,'m^3/(mol*s)'), n=2.35273, w0=(299.5,'kJ/mol'), E0=(40.1409,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_3O-u1_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_3O-u1_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_3O-u1_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_3O-u1_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 476,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3O-u1",
    kinetics = ArrheniusBM(A=(7.15716e+09,'m^3/(mol*s)'), n=-0.676681, w0=(299.5,'kJ/mol'), E0=(85.6669,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5069983430382397, var=12.90078535766782, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3O-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3O-u1
    Total Standard Deviation in ln(k): 8.474405131815077"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3O-u1
Total Standard Deviation in ln(k): 8.474405131815077""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3O-u1
Total Standard Deviation in ln(k): 8.474405131815077
""",
)

entry(
    index = 477,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3O-u1_Ext-1C-R",
    kinetics = ArrheniusBM(A=(50.2678,'m^3/(mol*s)'), n=1.51875, w0=(299.5,'kJ/mol'), E0=(63.8677,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3O-u1_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3O-u1_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3O-u1_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-3O-u1_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 478,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C",
    kinetics = ArrheniusBM(A=(4.36804e+07,'m^3/(mol*s)'), n=0.00567964, w0=(299.5,'kJ/mol'), E0=(68.2277,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6506672427306956, var=2.7437112184116166, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C',), comment="""BM rule fitted to 11 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C
    Total Standard Deviation in ln(k): 4.95551591426435"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C
Total Standard Deviation in ln(k): 4.95551591426435""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C
Total Standard Deviation in ln(k): 4.95551591426435
""",
)

entry(
    index = 479,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(5.5511e+08,'m^3/(mol*s)'), n=-0.255625, w0=(299.5,'kJ/mol'), E0=(69.1281,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8544204818645897, var=4.297260332739199, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R
    Total Standard Deviation in ln(k): 6.302567742611591"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R
Total Standard Deviation in ln(k): 6.302567742611591""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R
Total Standard Deviation in ln(k): 6.302567742611591
""",
)

entry(
    index = 480,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.11536e+06,'m^3/(mol*s)'), n=0.63546, w0=(299.5,'kJ/mol'), E0=(60.4738,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8845027802427224, var=1.3209423409764705, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 4.526456040664232"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 4.526456040664232""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 4.526456040664232
""",
)

entry(
    index = 481,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C_3O-u1",
    kinetics = ArrheniusBM(A=(0.671582,'m^3/(mol*s)'), n=2.44318, w0=(299.5,'kJ/mol'), E0=(16.8125,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 482,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C_N-3O-u1",
    kinetics = ArrheniusBM(A=(49186.3,'m^3/(mol*s)'), n=1.01535, w0=(299.5,'kJ/mol'), E0=(58.3376,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.836560445980245, var=1.8523174573160006, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C_N-3O-u1',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C_N-3O-u1
    Total Standard Deviation in ln(k): 4.830352499460802"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C_N-3O-u1
Total Standard Deviation in ln(k): 4.830352499460802""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C_N-3O-u1
Total Standard Deviation in ln(k): 4.830352499460802
""",
)

entry(
    index = 483,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C_N-3O-u1_Ext-1C-R",
    kinetics = ArrheniusBM(A=(26.7714,'m^3/(mol*s)'), n=1.82744, w0=(299.5,'kJ/mol'), E0=(36.6659,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C_N-3O-u1_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C_N-3O-u1_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C_N-3O-u1_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C_N-3O-u1_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 484,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C_N-3O-u1_Ext-4C-R",
    kinetics = ArrheniusBM(A=(48.9307,'m^3/(mol*s)'), n=1.947, w0=(299.5,'kJ/mol'), E0=(63.2204,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C_N-3O-u1_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C_N-3O-u1_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C_N-3O-u1_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_4BrCFINOPSSi->C_N-3O-u1_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 485,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_N-4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.19735e+10,'m^3/(mol*s)'), n=-0.874524, w0=(299.5,'kJ/mol'), E0=(74.6831,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6799593649508333, var=19.82194648401196, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_N-4BrCFINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_N-4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 10.633890977530923"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 10.633890977530923""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 10.633890977530923
""",
)

entry(
    index = 486,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_N-4BrCFINOPSSi->C_3O-u1",
    kinetics = ArrheniusBM(A=(0.558006,'m^3/(mol*s)'), n=2.23525, w0=(299.5,'kJ/mol'), E0=(37.6334,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_N-4BrCFINOPSSi->C_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_N-4BrCFINOPSSi->C_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_N-4BrCFINOPSSi->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_N-4BrCFINOPSSi->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 487,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_N-4BrCFINOPSSi->C_N-3O-u1",
    kinetics = ArrheniusBM(A=(34.7818,'m^3/(mol*s)'), n=1.42177, w0=(299.5,'kJ/mol'), E0=(55.3509,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_N-4BrCFINOPSSi->C_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_N-4BrCFINOPSSi->C_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_N-4BrCFINOPSSi->C_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-1C-R_N-4BrCFINOPSSi->C_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 488,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-4BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(230747,'m^3/(mol*s)'), n=0.617371, w0=(299.5,'kJ/mol'), E0=(60.826,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4915454707497373, var=6.345279126883097, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-4BrCFINOPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-4BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 6.284933951901126"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 6.284933951901126""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 6.284933951901126
""",
)

entry(
    index = 489,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-4BrCFINOPSSi-R_3O-u1",
    kinetics = ArrheniusBM(A=(0.316045,'m^3/(mol*s)'), n=2.33519, w0=(299.5,'kJ/mol'), E0=(30.8454,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-4BrCFINOPSSi-R_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-4BrCFINOPSSi-R_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-4BrCFINOPSSi-R_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-4BrCFINOPSSi-R_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 490,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-4BrCFINOPSSi-R_N-3O-u1",
    kinetics = ArrheniusBM(A=(0.0877805,'m^3/(mol*s)'), n=2.41884, w0=(299.5,'kJ/mol'), E0=(46.173,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-4BrCFINOPSSi-R_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-4BrCFINOPSSi-R_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-4BrCFINOPSSi-R_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_Ext-4BrCFINOPSSi-R_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 491,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.0961606,'m^3/(mol*s)'), n=2.45743, w0=(299.5,'kJ/mol'), E0=(49.4284,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_4BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 492,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.11085e+07,'m^3/(mol*s)'), n=0.0660297, w0=(299.5,'kJ/mol'), E0=(70.7063,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1039335839408819, var=16.869547896515282, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 8.495098868453654"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 8.495098868453654""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 8.495098868453654
""",
)

entry(
    index = 493,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->C_3O-u1",
    kinetics = ArrheniusBM(A=(0.0415779,'m^3/(mol*s)'), n=2.65327, w0=(299.5,'kJ/mol'), E0=(44.0733,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->C_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->C_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 494,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->C_N-3O-u1",
    kinetics = ArrheniusBM(A=(0.00435304,'m^3/(mol*s)'), n=2.58838, w0=(299.5,'kJ/mol'), E0=(46.115,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->C_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->C_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->C_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=1C_N-4BrCFINOPSSi->C_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 495,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_3O-u1",
    kinetics = ArrheniusBM(A=(0.104392,'m^3/(mol*s)'), n=2.92687, w0=(299.5,'kJ/mol'), E0=(33.8378,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 496,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_N-3O-u1",
    kinetics = ArrheniusBM(A=(10.5404,'m^3/(mol*s)'), n=2.14943, w0=(299.5,'kJ/mol'), E0=(69.675,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_3BrCClFINOPSSi->O_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 497,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(81678.3,'m^3/(mol*s)'), n=0.693333, w0=(322.579,'kJ/mol'), E0=(76.9173,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5447242644194065, var=7.039466687342751, Tref=1000.0, N=48, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O',), comment="""BM rule fitted to 48 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O
    Total Standard Deviation in ln(k): 6.687615695865357"""),
    rank = 11,
    shortDesc = """BM rule fitted to 48 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O
Total Standard Deviation in ln(k): 6.687615695865357""",
    longDesc = 
"""
BM rule fitted to 48 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O
Total Standard Deviation in ln(k): 6.687615695865357
""",
)

entry(
    index = 498,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_3CClF->F",
    kinetics = ArrheniusBM(A=(1430.74,'m^3/(mol*s)'), n=1.46983, w0=(288.77,'kJ/mol'), E0=(17.7251,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_3CClF->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_3CClF->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_3CClF->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_3CClF->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 499,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F",
    kinetics = ArrheniusBM(A=(87979.8,'m^3/(mol*s)'), n=0.678272, w0=(323.298,'kJ/mol'), E0=(78.1266,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5464023501332972, var=5.637661397806192, Tref=1000.0, N=47, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F',), comment="""BM rule fitted to 47 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F
    Total Standard Deviation in ln(k): 6.132865084147238"""),
    rank = 11,
    shortDesc = """BM rule fitted to 47 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F
Total Standard Deviation in ln(k): 6.132865084147238""",
    longDesc = 
"""
BM rule fitted to 47 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F
Total Standard Deviation in ln(k): 6.132865084147238
""",
)

entry(
    index = 500,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R",
    kinetics = ArrheniusBM(A=(126828,'m^3/(mol*s)'), n=0.632351, w0=(323.217,'kJ/mol'), E0=(78.2647,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5631654369039731, var=5.755688937231928, Tref=1000.0, N=46, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R',), comment="""BM rule fitted to 46 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R
    Total Standard Deviation in ln(k): 6.224551854746981"""),
    rank = 11,
    shortDesc = """BM rule fitted to 46 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R
Total Standard Deviation in ln(k): 6.224551854746981""",
    longDesc = 
"""
BM rule fitted to 46 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R
Total Standard Deviation in ln(k): 6.224551854746981
""",
)

entry(
    index = 501,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(7456.47,'m^3/(mol*s)'), n=0.968475, w0=(321.78,'kJ/mol'), E0=(71.6176,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5367524010153673, var=7.659890854831162, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl',), comment="""BM rule fitted to 25 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl
    Total Standard Deviation in ln(k): 6.897030729156332"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl
Total Standard Deviation in ln(k): 6.897030729156332""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl
Total Standard Deviation in ln(k): 6.897030729156332
""",
)

entry(
    index = 502,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(11697.6,'m^3/(mol*s)'), n=0.906805, w0=(321.562,'kJ/mol'), E0=(71.5325,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5524602564148487, var=8.012077947142831, Tref=1000.0, N=24, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R',), comment="""BM rule fitted to 24 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 7.062616862053271"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 7.062616862053271""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 7.062616862053271
""",
)

entry(
    index = 503,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(2.34173e+06,'m^3/(mol*s)'), n=0.226418, w0=(316.125,'kJ/mol'), E0=(68.4143,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5720212149748917, var=13.10327459104541, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl',), comment="""BM rule fitted to 12 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl
    Total Standard Deviation in ln(k): 8.694068584593932"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl
Total Standard Deviation in ln(k): 8.694068584593932""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl
Total Standard Deviation in ln(k): 8.694068584593932
""",
)

entry(
    index = 504,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(8.18824e+06,'m^3/(mol*s)'), n=0.0608693, w0=(315.136,'kJ/mol'), E0=(68.4453,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5931893668614321, var=14.54369289367868, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R',), comment="""BM rule fitted to 11 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 9.13572211885295"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 9.13572211885295""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 9.13572211885295
""",
)

entry(
    index = 505,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->F",
    kinetics = ArrheniusBM(A=(2.44893e+14,'m^3/(mol*s)'), n=-1.68563, w0=(305.25,'kJ/mol'), E0=(77.8405,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6286649657296021, var=87.5872712319382, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->F
    Total Standard Deviation in ln(k): 20.341489187401013"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->F
Total Standard Deviation in ln(k): 20.341489187401013""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->F
Total Standard Deviation in ln(k): 20.341489187401013
""",
)

entry(
    index = 506,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->F_3CCl->C",
    kinetics = ArrheniusBM(A=(0.0228759,'m^3/(mol*s)'), n=2.75, w0=(327,'kJ/mol'), E0=(54.6342,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->F_3CCl->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->F_3CCl->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->F_3CCl->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->F_3CCl->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 507,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->F_N-3CCl->C",
    kinetics = ArrheniusBM(A=(8392.38,'m^3/(mol*s)'), n=1.46983, w0=(283.5,'kJ/mol'), E0=(28.2271,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->F_N-3CCl->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->F_N-3CCl->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->F_N-3CCl->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_6R!H->F_N-3CCl->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 508,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F",
    kinetics = ArrheniusBM(A=(1830.25,'m^3/(mol*s)'), n=1.01897, w0=(317.333,'kJ/mol'), E0=(61.2678,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.49257550097802566, var=9.788750664824684, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F',), comment="""BM rule fitted to 9 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F
    Total Standard Deviation in ln(k): 7.509837350537778"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F
Total Standard Deviation in ln(k): 7.509837350537778""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F
Total Standard Deviation in ln(k): 7.509837350537778
""",
)

entry(
    index = 509,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_6BrCClINOPSSi->Cl",
    kinetics = ArrheniusBM(A=(1.5463e-06,'m^3/(mol*s)'), n=3.83136, w0=(305.25,'kJ/mol'), E0=(9.89539,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.23842130783882798, var=9.682831764422724, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_6BrCClINOPSSi->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_6BrCClINOPSSi->Cl
    Total Standard Deviation in ln(k): 6.83723254176537"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_6BrCClINOPSSi->Cl
Total Standard Deviation in ln(k): 6.83723254176537""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_6BrCClINOPSSi->Cl
Total Standard Deviation in ln(k): 6.83723254176537
""",
)

entry(
    index = 510,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_6BrCClINOPSSi->Cl_3CCl->C",
    kinetics = ArrheniusBM(A=(0.0287047,'m^3/(mol*s)'), n=2.77954, w0=(327,'kJ/mol'), E0=(52.6899,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_6BrCClINOPSSi->Cl_3CCl->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_6BrCClINOPSSi->Cl_3CCl->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_6BrCClINOPSSi->Cl_3CCl->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_6BrCClINOPSSi->Cl_3CCl->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 511,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_6BrCClINOPSSi->Cl_N-3CCl->C",
    kinetics = ArrheniusBM(A=(212391,'m^3/(mol*s)'), n=0.469006, w0=(283.5,'kJ/mol'), E0=(29.0904,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_6BrCClINOPSSi->Cl_N-3CCl->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_6BrCClINOPSSi->Cl_N-3CCl->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_6BrCClINOPSSi->Cl_N-3CCl->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_6BrCClINOPSSi->Cl_N-3CCl->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 512,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl",
    kinetics = ArrheniusBM(A=(193.653,'m^3/(mol*s)'), n=1.23766, w0=(320.786,'kJ/mol'), E0=(63.3768,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4877576724575427, var=6.740053833010311, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl',), comment="""BM rule fitted to 7 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl
    Total Standard Deviation in ln(k): 6.43013754504343"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl
Total Standard Deviation in ln(k): 6.43013754504343""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl
Total Standard Deviation in ln(k): 6.43013754504343
""",
)

entry(
    index = 513,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R",
    kinetics = ArrheniusBM(A=(19.3468,'m^3/(mol*s)'), n=1.61853, w0=(318.3,'kJ/mol'), E0=(59.23,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.46635580469945387, var=6.880919969428898, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R
    Total Standard Deviation in ln(k): 6.430470617706964"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R
Total Standard Deviation in ln(k): 6.430470617706964""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R
Total Standard Deviation in ln(k): 6.430470617706964
""",
)

entry(
    index = 514,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C",
    kinetics = ArrheniusBM(A=(0.0938456,'m^3/(mol*s)'), n=2.29843, w0=(327,'kJ/mol'), E0=(61.5047,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.40675169216592416, var=2.029598165523891, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C
    Total Standard Deviation in ln(k): 3.8780142786372425"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C
Total Standard Deviation in ln(k): 3.8780142786372425""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C
Total Standard Deviation in ln(k): 3.8780142786372425
""",
)

entry(
    index = 515,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_Ext-6CO-R",
    kinetics = ArrheniusBM(A=(0.0131534,'m^3/(mol*s)'), n=2.77065, w0=(327,'kJ/mol'), E0=(66.2049,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.41879006532127905, var=0.0404166830511143, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_Ext-6CO-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_Ext-6CO-R
    Total Standard Deviation in ln(k): 1.4552662978535011"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_Ext-6CO-R
Total Standard Deviation in ln(k): 1.4552662978535011""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_Ext-6CO-R
Total Standard Deviation in ln(k): 1.4552662978535011
""",
)

entry(
    index = 516,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_Ext-6CO-R_7R!H->F",
    kinetics = ArrheniusBM(A=(0.0167469,'m^3/(mol*s)'), n=2.76768, w0=(327,'kJ/mol'), E0=(67.5973,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_Ext-6CO-R_7R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_Ext-6CO-R_7R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_Ext-6CO-R_7R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_Ext-6CO-R_7R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 517,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_Ext-6CO-R_N-7R!H->F",
    kinetics = ArrheniusBM(A=(0.0102091,'m^3/(mol*s)'), n=2.77509, w0=(327,'kJ/mol'), E0=(64.7972,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_Ext-6CO-R_N-7R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_Ext-6CO-R_N-7R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_Ext-6CO-R_N-7R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_Ext-6CO-R_N-7R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 518,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_7R!H->C",
    kinetics = ArrheniusBM(A=(0.00133416,'m^3/(mol*s)'), n=2.78212, w0=(327,'kJ/mol'), E0=(54.1157,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 519,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_N-7R!H->C",
    kinetics = ArrheniusBM(A=(0.208167,'m^3/(mol*s)'), n=1.78944, w0=(327,'kJ/mol'), E0=(51.3384,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_3CCl->C_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 520,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_N-3CCl->C",
    kinetics = ArrheniusBM(A=(1.71214e+06,'m^3/(mol*s)'), n=0.133752, w0=(283.5,'kJ/mol'), E0=(38.2833,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_N-3CCl->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_N-3CCl->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_N-3CCl->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_Ext-6CO-R_N-3CCl->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 521,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C",
    kinetics = ArrheniusBM(A=(0.602197,'m^3/(mol*s)'), n=1.79841, w0=(327,'kJ/mol'), E0=(68.2397,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_6CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 522,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_N-6CO->C",
    kinetics = ArrheniusBM(A=(0.21934,'m^3/(mol*s)'), n=1.76817, w0=(327,'kJ/mol'), E0=(52.2986,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_N-6CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_N-6CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_N-6CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_5R!H->Cl_Ext-1C-R_N-6R!H->F_N-6BrCClINOPSSi->Cl_N-6CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 523,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(0.00269788,'m^3/(mol*s)'), n=2.82941, w0=(327,'kJ/mol'), E0=(63.8103,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.406934140565805, var=2.948343106823439, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl',), comment="""BM rule fitted to 12 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 4.464726059089124"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 4.464726059089124""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 4.464726059089124
""",
)

entry(
    index = 524,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.00113213,'m^3/(mol*s)'), n=2.91006, w0=(327,'kJ/mol'), E0=(63.5156,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.427004733774016, var=4.3931835353227005, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C',), comment="""BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 5.274785412158763"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 5.274785412158763""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 5.274785412158763
""",
)

entry(
    index = 525,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(9.27378e-05,'m^3/(mol*s)'), n=3.07065, w0=(327,'kJ/mol'), E0=(57.2404,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4254862951485422, var=10.750432183590208, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R
    Total Standard Deviation in ln(k): 7.6421566823565605"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 7.6421566823565605""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 7.6421566823565605
""",
)

entry(
    index = 526,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(0.018601,'m^3/(mol*s)'), n=2.15643, w0=(327,'kJ/mol'), E0=(64.3949,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.553790851545538, var=4.008010777497536, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_6R!H->C
    Total Standard Deviation in ln(k): 5.404917318685679"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 5.404917318685679""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 5.404917318685679
""",
)

entry(
    index = 527,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_6R!H->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(0.168083,'m^3/(mol*s)'), n=1.8024, w0=(327,'kJ/mol'), E0=(68.2519,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_6R!H->C_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_6R!H->C_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_6R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_6R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 528,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(0.00446736,'m^3/(mol*s)'), n=2.84309, w0=(327,'kJ/mol'), E0=(60.0223,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4567555409143319, var=8.331293979910841, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_N-6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 6.934090501527358"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 6.934090501527358""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 6.934090501527358
""",
)

entry(
    index = 529,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_N-6R!H->C_6BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(0.00416182,'m^3/(mol*s)'), n=2.75776, w0=(327,'kJ/mol'), E0=(62.9722,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_N-6R!H->C_6BrClFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_N-6R!H->C_6BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_N-6R!H->C_6BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_N-6R!H->C_6BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 530,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_N-6R!H->C_N-6BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(0.0184071,'m^3/(mol*s)'), n=2.76105, w0=(327,'kJ/mol'), E0=(58.5254,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_N-6R!H->C_N-6BrClFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_N-6R!H->C_N-6BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_N-6R!H->C_N-6BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R_N-6R!H->C_N-6BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 531,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(0.00539879,'m^3/(mol*s)'), n=2.86527, w0=(327,'kJ/mol'), E0=(69.4087,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5262427687359987, var=2.045381680363714, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R
    Total Standard Deviation in ln(k): 4.189326789588217"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R
Total Standard Deviation in ln(k): 4.189326789588217""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R
Total Standard Deviation in ln(k): 4.189326789588217
""",
)

entry(
    index = 532,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_Sp-5C-1C",
    kinetics = ArrheniusBM(A=(0.0056062,'m^3/(mol*s)'), n=2.84217, w0=(327,'kJ/mol'), E0=(73.1711,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_Sp-5C-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_Sp-5C-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_Sp-5C-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_Sp-5C-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 533,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_N-Sp-5C-1C",
    kinetics = ArrheniusBM(A=(0.0141769,'m^3/(mol*s)'), n=2.76355, w0=(327,'kJ/mol'), E0=(66.7329,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_N-Sp-5C-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_N-Sp-5C-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_N-Sp-5C-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R_N-Sp-5C-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 534,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Sp-5C-1C",
    kinetics = ArrheniusBM(A=(0.00472731,'m^3/(mol*s)'), n=2.8542, w0=(327,'kJ/mol'), E0=(73.0828,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Sp-5C-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Sp-5C-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Sp-5C-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Sp-5C-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 535,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_N-Sp-5C-1C",
    kinetics = ArrheniusBM(A=(0.0351245,'m^3/(mol*s)'), n=2.66451, w0=(327,'kJ/mol'), E0=(64.9314,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_N-Sp-5C-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_N-Sp-5C-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_N-Sp-5C-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_5BrCFINOPSSi->C_N-Sp-5C-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 536,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.00998293,'m^3/(mol*s)'), n=2.72141, w0=(327,'kJ/mol'), E0=(63.9385,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3616109244300033, var=0.9457673997761912, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 2.858186516825833"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 2.858186516825833""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 2.858186516825833
""",
)

entry(
    index = 537,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C",
    kinetics = ArrheniusBM(A=(0.00638277,'m^3/(mol*s)'), n=2.75958, w0=(327,'kJ/mol'), E0=(63.6855,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.37904084491358475, var=1.390577818302298, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C
    Total Standard Deviation in ln(k): 3.316402938742185"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C
Total Standard Deviation in ln(k): 3.316402938742185""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C
Total Standard Deviation in ln(k): 3.316402938742185
""",
)

entry(
    index = 538,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.00896417,'m^3/(mol*s)'), n=2.72355, w0=(327,'kJ/mol'), E0=(61.0513,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3073583091199936, var=0.05405634822057568, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_Ext-1C-R
    Total Standard Deviation in ln(k): 1.2383583870386454"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_Ext-1C-R
Total Standard Deviation in ln(k): 1.2383583870386454""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_Ext-1C-R
Total Standard Deviation in ln(k): 1.2383583870386454
""",
)

entry(
    index = 539,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_Ext-1C-R_5FO->O",
    kinetics = ArrheniusBM(A=(0.0117958,'m^3/(mol*s)'), n=2.7472, w0=(327,'kJ/mol'), E0=(64.4082,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_Ext-1C-R_5FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_Ext-1C-R_5FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_Ext-1C-R_5FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_Ext-1C-R_5FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 540,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_Ext-1C-R_N-5FO->O",
    kinetics = ArrheniusBM(A=(0.00615345,'m^3/(mol*s)'), n=2.71255, w0=(327,'kJ/mol'), E0=(57.6127,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_Ext-1C-R_N-5FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_Ext-1C-R_N-5FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_Ext-1C-R_N-5FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Sp-5FO-1C_Ext-1C-R_N-5FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 541,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_N-Sp-5FO-1C",
    kinetics = ArrheniusBM(A=(0.0090139,'m^3/(mol*s)'), n=2.78658, w0=(327,'kJ/mol'), E0=(63.1361,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_N-Sp-5FO-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_N-Sp-5FO-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_N-Sp-5FO-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_4R!H->Cl_Ext-1C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_N-Sp-5FO-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 542,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(1.29938e+06,'m^3/(mol*s)'), n=0.362445, w0=(324.929,'kJ/mol'), E0=(85.0221,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5700782131168316, var=4.194504145568811, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl',), comment="""BM rule fitted to 21 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 5.538152715425382"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 5.538152715425382""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 5.538152715425382
""",
)

entry(
    index = 543,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C",
    kinetics = ArrheniusBM(A=(725.803,'m^3/(mol*s)'), n=1.0218, w0=(327,'kJ/mol'), E0=(53.6626,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 544,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C",
    kinetics = ArrheniusBM(A=(750202,'m^3/(mol*s)'), n=0.444428, w0=(324.825,'kJ/mol'), E0=(85.3214,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5861628612104686, var=4.469721248236337, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C',), comment="""BM rule fitted to 20 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C
    Total Standard Deviation in ln(k): 5.711124829131921"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C
Total Standard Deviation in ln(k): 5.711124829131921""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C
Total Standard Deviation in ln(k): 5.711124829131921
""",
)

entry(
    index = 545,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.291839,'m^3/(mol*s)'), n=2.20908, w0=(327,'kJ/mol'), E0=(71.1358,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.48781788117053365, var=1.4715785193528592, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C',), comment="""BM rule fitted to 13 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 3.657589848162542"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 3.657589848162542""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 3.657589848162542
""",
)

entry(
    index = 546,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_Sp-4C=1C",
    kinetics = ArrheniusBM(A=(0.0084201,'m^3/(mol*s)'), n=2.83508, w0=(327,'kJ/mol'), E0=(71.6904,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3209668851146146, var=0.11174125365987567, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_Sp-4C=1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_Sp-4C=1C
    Total Standard Deviation in ln(k): 1.476586710150149"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_Sp-4C=1C
Total Standard Deviation in ln(k): 1.476586710150149""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_Sp-4C=1C
Total Standard Deviation in ln(k): 1.476586710150149
""",
)

entry(
    index = 547,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_Sp-4C=1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.00717719,'m^3/(mol*s)'), n=2.80408, w0=(327,'kJ/mol'), E0=(69.1391,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_Sp-4C=1C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_Sp-4C=1C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_Sp-4C=1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_Sp-4C=1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 548,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C",
    kinetics = ArrheniusBM(A=(0.109606,'m^3/(mol*s)'), n=2.29733, w0=(327,'kJ/mol'), E0=(69.2983,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4991498227146935, var=1.6010532598277762, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C',), comment="""BM rule fitted to 11 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C
    Total Standard Deviation in ln(k): 3.79079137220463"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C
Total Standard Deviation in ln(k): 3.79079137220463""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C
Total Standard Deviation in ln(k): 3.79079137220463
""",
)

entry(
    index = 549,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(0.0700804,'m^3/(mol*s)'), n=2.35734, w0=(327,'kJ/mol'), E0=(69.7758,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.48649003834888416, var=2.36219749130288, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R',), comment="""BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R
    Total Standard Deviation in ln(k): 4.303502740849482"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R
Total Standard Deviation in ln(k): 4.303502740849482""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R
Total Standard Deviation in ln(k): 4.303502740849482
""",
)

entry(
    index = 550,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(0.115806,'m^3/(mol*s)'), n=2.39936, w0=(327,'kJ/mol'), E0=(70.2342,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4637961184448076, var=0.519052059902285, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C
    Total Standard Deviation in ln(k): 2.6096336338462236"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 2.6096336338462236""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 2.6096336338462236
""",
)

entry(
    index = 551,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(0.170253,'m^3/(mol*s)'), n=2.36486, w0=(327,'kJ/mol'), E0=(69.3579,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4995632027167773, var=0.5386804132987032, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C_Ext-4C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 2.7265562466463757"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 2.7265562466463757""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 2.7265562466463757
""",
)

entry(
    index = 552,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C_Ext-4C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.03354,'m^3/(mol*s)'), n=2.10434, w0=(327,'kJ/mol'), E0=(66.4655,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6101842157162864, var=0.06360067258694051, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C_Ext-4C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C_Ext-4C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 2.038703793028195"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C_Ext-4C-R_Ext-1C-R
Total Standard Deviation in ln(k): 2.038703793028195""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C_Ext-4C-R_Ext-1C-R
Total Standard Deviation in ln(k): 2.038703793028195
""",
)

entry(
    index = 553,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C_Ext-4C-R_Ext-1C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(0.0560356,'m^3/(mol*s)'), n=2.48678, w0=(327,'kJ/mol'), E0=(65.0993,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C_Ext-4C-R_Ext-1C-R_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C_Ext-4C-R_Ext-1C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C_Ext-4C-R_Ext-1C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C_Ext-4C-R_Ext-1C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 554,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.727634,'m^3/(mol*s)'), n=1.97706, w0=(327,'kJ/mol'), E0=(67.7967,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_5R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 555,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.0372743,'m^3/(mol*s)'), n=2.2617, w0=(327,'kJ/mol'), E0=(69.2319,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5272173391068671, var=4.215055823942805, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_N-5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 5.4405083039214555"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 5.4405083039214555""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 5.4405083039214555
""",
)

entry(
    index = 556,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_N-5R!H->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(0.0132465,'m^3/(mol*s)'), n=2.47066, w0=(327,'kJ/mol'), E0=(71.2684,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5444421483579307, var=14.484281741882423, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_N-5R!H->C_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_N-5R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 8.997610128289072"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_N-5R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 8.997610128289072""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_N-5R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 8.997610128289072
""",
)

entry(
    index = 557,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(0.21039,'m^3/(mol*s)'), n=1.87409, w0=(327,'kJ/mol'), E0=(71.2622,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-4C-R_N-5R!H->C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 558,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(5.45881,'m^3/(mol*s)'), n=1.72833, w0=(327,'kJ/mol'), E0=(64.1868,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6668251766443749, var=0.4874012594220295, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-1C-R
    Total Standard Deviation in ln(k): 3.0750284733801854"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-1C-R
Total Standard Deviation in ln(k): 3.0750284733801854""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-1C-R
Total Standard Deviation in ln(k): 3.0750284733801854
""",
)

entry(
    index = 559,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(32.2266,'m^3/(mol*s)'), n=1.4911, w0=(327,'kJ/mol'), E0=(62.7471,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_4BrCFINOPSSi->C_N-Sp-4C=1C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 560,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(3.48116e+11,'m^3/(mol*s)'), n=-1.04557, w0=(320.786,'kJ/mol'), E0=(96.3549,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5561321037705129, var=9.3306365504243, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C',), comment="""BM rule fitted to 7 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 7.520998787403335"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 7.520998787403335""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 7.520998787403335
""",
)

entry(
    index = 561,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C",
    kinetics = ArrheniusBM(A=(0.00732469,'m^3/(mol*s)'), n=2.83145, w0=(327,'kJ/mol'), E0=(67.0508,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.273748444817242, var=1.5509305540597231, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C
    Total Standard Deviation in ln(k): 3.1844343024533375"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C
Total Standard Deviation in ln(k): 3.1844343024533375""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C
Total Standard Deviation in ln(k): 3.1844343024533375
""",
)

entry(
    index = 562,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.0197756,'m^3/(mol*s)'), n=2.69586, w0=(327,'kJ/mol'), E0=(62.4235,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3790307505357223, var=2.790161373972543, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Ext-1C-R
    Total Standard Deviation in ln(k): 4.301003164837129"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Ext-1C-R
Total Standard Deviation in ln(k): 4.301003164837129""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Ext-1C-R
Total Standard Deviation in ln(k): 4.301003164837129
""",
)

entry(
    index = 563,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.0174418,'m^3/(mol*s)'), n=2.72596, w0=(327,'kJ/mol'), E0=(60.84,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.40694941113664906, var=8.354594070392489, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 6.8170353100515495"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 6.8170353100515495""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 6.8170353100515495
""",
)

entry(
    index = 564,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Ext-1C-R_Ext-1C-R_4BrFO->Br",
    kinetics = ArrheniusBM(A=(0.00779837,'m^3/(mol*s)'), n=2.71484, w0=(327,'kJ/mol'), E0=(62.0205,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Ext-1C-R_Ext-1C-R_4BrFO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Ext-1C-R_Ext-1C-R_4BrFO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Ext-1C-R_Ext-1C-R_4BrFO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Ext-1C-R_Ext-1C-R_4BrFO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 565,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Ext-1C-R_Ext-1C-R_N-4BrFO->Br",
    kinetics = ArrheniusBM(A=(0.13656,'m^3/(mol*s)'), n=2.58117, w0=(327,'kJ/mol'), E0=(61.0047,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Ext-1C-R_Ext-1C-R_N-4BrFO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Ext-1C-R_Ext-1C-R_N-4BrFO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Ext-1C-R_Ext-1C-R_N-4BrFO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Ext-1C-R_Ext-1C-R_N-4BrFO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 566,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Sp-4BrFO-1C",
    kinetics = ArrheniusBM(A=(0.00252818,'m^3/(mol*s)'), n=2.9418, w0=(327,'kJ/mol'), E0=(73.2931,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1498645969993785, var=0.9009307548383979, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Sp-4BrFO-1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Sp-4BrFO-1C
    Total Standard Deviation in ln(k): 2.279386068920475"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Sp-4BrFO-1C
Total Standard Deviation in ln(k): 2.279386068920475""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Sp-4BrFO-1C
Total Standard Deviation in ln(k): 2.279386068920475
""",
)

entry(
    index = 567,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Sp-4BrFO-1C_4BrFO->O",
    kinetics = ArrheniusBM(A=(0.00435666,'m^3/(mol*s)'), n=2.88851, w0=(327,'kJ/mol'), E0=(71.8059,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Sp-4BrFO-1C_4BrFO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Sp-4BrFO-1C_4BrFO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Sp-4BrFO-1C_4BrFO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Sp-4BrFO-1C_4BrFO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 568,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Sp-4BrFO-1C_N-4BrFO->O",
    kinetics = ArrheniusBM(A=(0.00300542,'m^3/(mol*s)'), n=2.90586, w0=(327,'kJ/mol'), E0=(75.5573,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Sp-4BrFO-1C_N-4BrFO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Sp-4BrFO-1C_N-4BrFO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Sp-4BrFO-1C_N-4BrFO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_Sp-4BrFO-1C_N-4BrFO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 569,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_N-Sp-4BrFO-1C",
    kinetics = ArrheniusBM(A=(0.0105112,'m^3/(mol*s)'), n=2.86655, w0=(327,'kJ/mol'), E0=(69.7521,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_N-Sp-4BrFO-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_N-Sp-4BrFO-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_N-Sp-4BrFO-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_3CCl->C_N-Sp-4BrFO-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 570,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_N-3CCl->C",
    kinetics = ArrheniusBM(A=(1130.32,'m^3/(mol*s)'), n=1.6362, w0=(283.5,'kJ/mol'), E0=(35.6344,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_N-3CCl->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_N-3CCl->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_N-3CCl->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_1C-u0_N-3BrCClFINOPSSi->O_N-3CClF->F_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#1C_N-4BrCFINOPSSi->C_N-3CCl->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 571,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0",
    kinetics = ArrheniusBM(A=(5.26481e+25,'m^3/(mol*s)'), n=-5.19439, w0=(315.214,'kJ/mol'), E0=(122.068,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.0247727405454432, var=13.938876701231193, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0',), comment="""BM rule fitted to 14 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0
    Total Standard Deviation in ln(k): 10.059445215282057"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0
Total Standard Deviation in ln(k): 10.059445215282057""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0
Total Standard Deviation in ln(k): 10.059445215282057
""",
)

entry(
    index = 572,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R",
    kinetics = ArrheniusBM(A=(8.81746e+27,'m^3/(mol*s)'), n=-5.76298, w0=(317,'kJ/mol'), E0=(124.723,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.1022530618571327, var=12.563778849089344, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R',), comment="""BM rule fitted to 11 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R
    Total Standard Deviation in ln(k): 9.875347978624365"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 9.875347978624365""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 9.875347978624365
""",
)

entry(
    index = 573,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(6.36534e+11,'m^3/(mol*s)'), n=-1.14551, w0=(327,'kJ/mol'), E0=(95.9307,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7235196411097009, var=8.661118763863497, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C',), comment="""BM rule fitted to 7 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 7.71777952048597"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 7.71777952048597""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 7.71777952048597
""",
)

entry(
    index = 574,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(1.39587e+10,'m^3/(mol*s)'), n=-0.686648, w0=(327,'kJ/mol'), E0=(93.0034,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6639069358398655, var=10.441835163482438, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C
    Total Standard Deviation in ln(k): 8.146174439351991"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C
Total Standard Deviation in ln(k): 8.146174439351991""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C
Total Standard Deviation in ln(k): 8.146174439351991
""",
)

entry(
    index = 575,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_4R!H->O",
    kinetics = ArrheniusBM(A=(3.88279e+11,'m^3/(mol*s)'), n=-1.08656, w0=(327,'kJ/mol'), E0=(81.1083,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8566447784126505, var=10.493198559347489, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_4R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_4R!H->O
    Total Standard Deviation in ln(k): 8.646353637536201"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_4R!H->O
Total Standard Deviation in ln(k): 8.646353637536201""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_4R!H->O
Total Standard Deviation in ln(k): 8.646353637536201
""",
)

entry(
    index = 576,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_4R!H->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3409.25,'m^3/(mol*s)'), n=1.21062, w0=(327,'kJ/mol'), E0=(45.3737,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5161522691026467, var=2.329664483611597, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_4R!H->O_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_4R!H->O_Ext-1C-R
    Total Standard Deviation in ln(k): 4.356739951772849"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_4R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 4.356739951772849""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_4R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 4.356739951772849
""",
)

entry(
    index = 577,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_4R!H->O_Ext-1C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(6386.97,'m^3/(mol*s)'), n=1.06381, w0=(327,'kJ/mol'), E0=(19.4601,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_4R!H->O_Ext-1C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_4R!H->O_Ext-1C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_4R!H->O_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_4R!H->O_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 578,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_4R!H->O_Ext-1C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.0343304,'m^3/(mol*s)'), n=2.71102, w0=(327,'kJ/mol'), E0=(41.4246,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_4R!H->O_Ext-1C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_4R!H->O_Ext-1C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_4R!H->O_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_4R!H->O_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 579,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_N-4R!H->O",
    kinetics = ArrheniusBM(A=(0.0029073,'m^3/(mol*s)'), n=2.93284, w0=(327,'kJ/mol'), E0=(75.9187,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9252912942817241, var=11.564801302400848, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_N-4R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_N-4R!H->O
    Total Standard Deviation in ln(k): 9.142367105468631"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_N-4R!H->O
Total Standard Deviation in ln(k): 9.142367105468631""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_N-4R!H->O
Total Standard Deviation in ln(k): 9.142367105468631
""",
)

entry(
    index = 580,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_N-4R!H->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.0146577,'m^3/(mol*s)'), n=2.68594, w0=(327,'kJ/mol'), E0=(84.4248,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2623534998053151, var=0.45833181103501913, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_N-4R!H->O_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_N-4R!H->O_Ext-1C-R
    Total Standard Deviation in ln(k): 2.016389457165503"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_N-4R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 2.016389457165503""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_Sp-4R!H-1C_N-4R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 2.016389457165503
""",
)

entry(
    index = 581,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_N-Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(0.171123,'m^3/(mol*s)'), n=2.55484, w0=(327,'kJ/mol'), E0=(46.499,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_N-Sp-4R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_N-Sp-4R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_3BrCClFINOPSSi->C_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 582,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(6.05133e+27,'m^3/(mol*s)'), n=-5.70336, w0=(299.5,'kJ/mol'), E0=(99.5126,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.0081260609803866, var=13.791603779397537, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 9.977974450542987"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 9.977974450542987""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 9.977974450542987
""",
)

entry(
    index = 583,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(157.231,'m^3/(mol*s)'), n=1.7152, w0=(299.5,'kJ/mol'), E0=(48.1681,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 584,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C_3O-u1",
    kinetics = ArrheniusBM(A=(6.64531e+26,'m^3/(mol*s)'), n=-5.44595, w0=(299.5,'kJ/mol'), E0=(-50.8493,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 585,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C_N-3O-u1",
    kinetics = ArrheniusBM(A=(1.30895e+17,'m^3/(mol*s)'), n=-2.683, w0=(299.5,'kJ/mol'), E0=(70.5002,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6392766547354837, var=25.68076122806406, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C_N-3O-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C_N-3O-u1
    Total Standard Deviation in ln(k): 11.765456100965302"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C_N-3O-u1
Total Standard Deviation in ln(k): 11.765456100965302""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C_N-3O-u1
Total Standard Deviation in ln(k): 11.765456100965302
""",
)

entry(
    index = 586,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C_N-3O-u1_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.04579e+17,'m^3/(mol*s)'), n=-2.74234, w0=(299.5,'kJ/mol'), E0=(2.63076,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C_N-3O-u1_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C_N-3O-u1_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C_N-3O-u1_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_Ext-1C-R_N-3BrCClFINOPSSi->C_N-3O-u1_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 587,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_3BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.164051,'m^3/(mol*s)'), n=1.82992, w0=(327,'kJ/mol'), E0=(76.3746,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_3BrCClFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_3BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 588,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_N-3BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.121158,'m^3/(mol*s)'), n=2.34554, w0=(299.5,'kJ/mol'), E0=(39.8957,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.43132246679206304, var=0.028484641302594885, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_N-3BrCClFINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_N-3BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 1.4220718195722521"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_N-3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 1.4220718195722521""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_N-3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 1.4220718195722521
""",
)

entry(
    index = 589,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_N-3BrCClFINOPSSi->C_3O-u1",
    kinetics = ArrheniusBM(A=(0.241972,'m^3/(mol*s)'), n=2.245, w0=(299.5,'kJ/mol'), E0=(37.7343,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_N-3BrCClFINOPSSi->C_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_N-3BrCClFINOPSSi->C_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_N-3BrCClFINOPSSi->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_N-3BrCClFINOPSSi->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 590,
    label = "Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_N-3BrCClFINOPSSi->C_N-3O-u1",
    kinetics = ArrheniusBM(A=(5.81832,'m^3/(mol*s)'), n=1.87825, w0=(299.5,'kJ/mol'), E0=(49.87,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_N-3BrCClFINOPSSi->C_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_N-3BrCClFINOPSSi->C_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_N-3BrCClFINOPSSi->C_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_1BrCClFO->C_N-1C-u0_N-3BrCClFINOPSSi->C_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 591,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C",
    kinetics = ArrheniusBM(A=(7.66883e+07,'m^3/(mol*s)'), n=-0.371934, w0=(287.987,'kJ/mol'), E0=(67.0844,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06881624814975101, var=10.66572616573068, Tref=1000.0, N=90, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C',), comment="""BM rule fitted to 90 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C
    Total Standard Deviation in ln(k): 6.72005383497381"""),
    rank = 11,
    shortDesc = """BM rule fitted to 90 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C
Total Standard Deviation in ln(k): 6.72005383497381""",
    longDesc = 
"""
BM rule fitted to 90 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C
Total Standard Deviation in ln(k): 6.72005383497381
""",
)

entry(
    index = 592,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(5.28706e+12,'m^3/(mol*s)'), n=-1.85469, w0=(293.883,'kJ/mol'), E0=(84.5585,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.13003086769965233, var=7.546744098647174, Tref=1000.0, N=67, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R',), comment="""BM rule fitted to 67 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R
    Total Standard Deviation in ln(k): 5.833986208014332"""),
    rank = 11,
    shortDesc = """BM rule fitted to 67 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 5.833986208014332""",
    longDesc = 
"""
BM rule fitted to 67 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R
Total Standard Deviation in ln(k): 5.833986208014332
""",
)

entry(
    index = 593,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(9.45903e+14,'m^3/(mol*s)'), n=-2.53593, w0=(298.189,'kJ/mol'), E0=(91.7426,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.20532667627653628, var=7.286231096720982, Tref=1000.0, N=57, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C',), comment="""BM rule fitted to 57 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 5.927281504694647"""),
    rank = 11,
    shortDesc = """BM rule fitted to 57 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 5.927281504694647""",
    longDesc = 
"""
BM rule fitted to 57 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 5.927281504694647
""",
)

entry(
    index = 594,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0",
    kinetics = ArrheniusBM(A=(3.23939e+12,'m^3/(mol*s)'), n=-1.69683, w0=(296.831,'kJ/mol'), E0=(80.2833,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.061201483021668945, var=5.431289838460677, Tref=1000.0, N=28, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0',), comment="""BM rule fitted to 28 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0
    Total Standard Deviation in ln(k): 4.8258332976981775"""),
    rank = 11,
    shortDesc = """BM rule fitted to 28 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0
Total Standard Deviation in ln(k): 4.8258332976981775""",
    longDesc = 
"""
BM rule fitted to 28 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0
Total Standard Deviation in ln(k): 4.8258332976981775
""",
)

entry(
    index = 595,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2492.88,'m^3/(mol*s)'), n=0.761868, w0=(297.5,'kJ/mol'), E0=(63.302,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03774001310086868, var=1.5796038733241262, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R',), comment="""BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R
    Total Standard Deviation in ln(k): 2.614421164134275"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R
Total Standard Deviation in ln(k): 2.614421164134275""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R
Total Standard Deviation in ln(k): 2.614421164134275
""",
)

entry(
    index = 596,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O",
    kinetics = ArrheniusBM(A=(46.7029,'m^3/(mol*s)'), n=1.32302, w0=(299.5,'kJ/mol'), E0=(61.0927,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.049167018119429064, var=1.6606055487230003, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O',), comment="""BM rule fitted to 7 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O
    Total Standard Deviation in ln(k): 2.7069267539527813"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O
Total Standard Deviation in ln(k): 2.7069267539527813""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O
Total Standard Deviation in ln(k): 2.7069267539527813
""",
)

entry(
    index = 597,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(643.862,'m^3/(mol*s)'), n=0.95372, w0=(299.5,'kJ/mol'), E0=(61.94,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.041400960948550135, var=2.07985007828286, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C
    Total Standard Deviation in ln(k): 2.9951883610569796"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C
Total Standard Deviation in ln(k): 2.9951883610569796""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C
Total Standard Deviation in ln(k): 2.9951883610569796
""",
)

entry(
    index = 598,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(34.9134,'m^3/(mol*s)'), n=1.30185, w0=(299.5,'kJ/mol'), E0=(60.6417,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.41671740037164623, var=6.0279068579134645, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 5.969013305349788"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R
Total Standard Deviation in ln(k): 5.969013305349788""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R
Total Standard Deviation in ln(k): 5.969013305349788
""",
)

entry(
    index = 599,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(9.78257e-12,'m^3/(mol*s)'), n=4.82636, w0=(299.5,'kJ/mol'), E0=(15.2348,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.267044371671865, var=1.7912631481937884, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 3.354064681447858"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 3.354064681447858""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 3.354064681447858
""",
)

entry(
    index = 600,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R_Ext-3C-R_Ext-3C-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(8.44362e-13,'m^3/(mol*s)'), n=5.13133, w0=(299.5,'kJ/mol'), E0=(10.459,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1764956242105077, var=5.10127433376767, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R_Ext-3C-R_Ext-3C-R_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R_Ext-3C-R_Ext-3C-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 4.971351153918079"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R_Ext-3C-R_Ext-3C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 4.971351153918079""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R_Ext-3C-R_Ext-3C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 4.971351153918079
""",
)

entry(
    index = 601,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_5R!H->F",
    kinetics = ArrheniusBM(A=(1.19048e-05,'m^3/(mol*s)'), n=3.22184, w0=(299.5,'kJ/mol'), E0=(46.6573,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 602,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(4.36525e-10,'m^3/(mol*s)'), n=4.21502, w0=(299.5,'kJ/mol'), E0=(28.4956,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_N-5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_N-5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-4R!H-R_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 603,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(8.68508e-06,'m^3/(mol*s)'), n=3.2292, w0=(299.5,'kJ/mol'), E0=(22.918,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_Sp-4R!H-3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 604,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_N-Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(0.000726835,'m^3/(mol*s)'), n=2.95754, w0=(299.5,'kJ/mol'), E0=(61.7838,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_N-Sp-4R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_N-Sp-4R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_1BrClFO->O_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 605,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_N-1BrClFO->O",
    kinetics = ArrheniusBM(A=(0.0786025,'m^3/(mol*s)'), n=1.58787, w0=(283.5,'kJ/mol'), E0=(33.4266,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_N-1BrClFO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_N-1BrClFO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_N-1BrClFO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Ext-4R!H-R_N-1BrClFO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 606,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C",
    kinetics = ArrheniusBM(A=(4.17149,'m^3/(mol*s)'), n=1.92026, w0=(295.5,'kJ/mol'), E0=(48.2623,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.27885594011309645, var=2.675953159730106, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C
    Total Standard Deviation in ln(k): 3.980057040334211"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C
Total Standard Deviation in ln(k): 3.980057040334211""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C
Total Standard Deviation in ln(k): 3.980057040334211
""",
)

entry(
    index = 607,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O",
    kinetics = ArrheniusBM(A=(41.2787,'m^3/(mol*s)'), n=1.60495, w0=(299.5,'kJ/mol'), E0=(54.6576,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11462550523827662, var=0.3660984145213899, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O
    Total Standard Deviation in ln(k): 1.5009901313391427"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O
Total Standard Deviation in ln(k): 1.5009901313391427""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O
Total Standard Deviation in ln(k): 1.5009901313391427
""",
)

entry(
    index = 608,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O_4R!H->C",
    kinetics = ArrheniusBM(A=(0.00248496,'m^3/(mol*s)'), n=2.86331, w0=(299.5,'kJ/mol'), E0=(33.4519,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 609,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O_N-4R!H->C",
    kinetics = ArrheniusBM(A=(34.0017,'m^3/(mol*s)'), n=1.6045, w0=(299.5,'kJ/mol'), E0=(53.2542,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.14868071999765536, var=2.2507677694550163, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O_N-4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O_N-4R!H->C
    Total Standard Deviation in ln(k): 3.381185278685439"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O_N-4R!H->C
Total Standard Deviation in ln(k): 3.381185278685439""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O_N-4R!H->C
Total Standard Deviation in ln(k): 3.381185278685439
""",
)

entry(
    index = 610,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O_N-4R!H->C_Ext-3C-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(0.000102465,'m^3/(mol*s)'), n=3.10435, w0=(299.5,'kJ/mol'), E0=(31.5394,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O_N-4R!H->C_Ext-3C-R_5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O_N-4R!H->C_Ext-3C-R_5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O_N-4R!H->C_Ext-3C-R_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O_N-4R!H->C_Ext-3C-R_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 611,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O_N-4R!H->C_Ext-3C-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(0.000506611,'m^3/(mol*s)'), n=3.06943, w0=(299.5,'kJ/mol'), E0=(36.2404,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O_N-4R!H->C_Ext-3C-R_N-5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O_N-4R!H->C_Ext-3C-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O_N-4R!H->C_Ext-3C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_1BrClFO->O_N-4R!H->C_Ext-3C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 612,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_N-1BrClFO->O",
    kinetics = ArrheniusBM(A=(0.0683409,'m^3/(mol*s)'), n=2.52216, w0=(283.5,'kJ/mol'), E0=(26.7122,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_N-1BrClFO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_N-1BrClFO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_N-1BrClFO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_Sp-4R!H=3C_N-1BrClFO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 613,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C",
    kinetics = ArrheniusBM(A=(3.96166e+15,'m^3/(mol*s)'), n=-2.55776, w0=(296.829,'kJ/mol'), E0=(83.608,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0940264334624489, var=9.546518256491732, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C',), comment="""BM rule fitted to 16 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C
    Total Standard Deviation in ln(k): 6.430365585128296"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C
Total Standard Deviation in ln(k): 6.430365585128296""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C
Total Standard Deviation in ln(k): 6.430365585128296
""",
)

entry(
    index = 614,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_1BrClFO->Cl",
    kinetics = ArrheniusBM(A=(1.67522e+10,'m^3/(mol*s)'), n=-1.1642, w0=(283.5,'kJ/mol'), E0=(57.6596,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12388939469586184, var=35.48403950074823, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_1BrClFO->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_1BrClFO->Cl
    Total Standard Deviation in ln(k): 12.253182259005412"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_1BrClFO->Cl
Total Standard Deviation in ln(k): 12.253182259005412""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_1BrClFO->Cl
Total Standard Deviation in ln(k): 12.253182259005412
""",
)

entry(
    index = 615,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_1BrClFO->Cl_4R!H->F",
    kinetics = ArrheniusBM(A=(0.0201448,'m^3/(mol*s)'), n=2.57076, w0=(283.5,'kJ/mol'), E0=(23.0383,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_1BrClFO->Cl_4R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_1BrClFO->Cl_4R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_1BrClFO->Cl_4R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_1BrClFO->Cl_4R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 616,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_1BrClFO->Cl_N-4R!H->F",
    kinetics = ArrheniusBM(A=(0.263742,'m^3/(mol*s)'), n=1.61124, w0=(283.5,'kJ/mol'), E0=(25.5927,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_1BrClFO->Cl_N-4R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_1BrClFO->Cl_N-4R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_1BrClFO->Cl_N-4R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_1BrClFO->Cl_N-4R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 617,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl",
    kinetics = ArrheniusBM(A=(1.58008e+16,'m^3/(mol*s)'), n=-2.70902, w0=(298.734,'kJ/mol'), E0=(87.0341,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08298090780761387, var=10.836997817991593, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl',), comment="""BM rule fitted to 14 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl
    Total Standard Deviation in ln(k): 6.808001568854193"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl
Total Standard Deviation in ln(k): 6.808001568854193""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl
Total Standard Deviation in ln(k): 6.808001568854193
""",
)

entry(
    index = 618,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F",
    kinetics = ArrheniusBM(A=(2.38605e-05,'m^3/(mol*s)'), n=3.21315, w0=(299.5,'kJ/mol'), E0=(24.0578,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.05089319530459262, var=0.20573048067578348, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F
    Total Standard Deviation in ln(k): 1.0371705048380597"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F
Total Standard Deviation in ln(k): 1.0371705048380597""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F
Total Standard Deviation in ln(k): 1.0371705048380597
""",
)

entry(
    index = 619,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(0.000182721,'m^3/(mol*s)'), n=2.96683, w0=(299.5,'kJ/mol'), E0=(29.6553,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.028081120691753295, var=0.07882583548288191, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl
    Total Standard Deviation in ln(k): 0.6334037785310471"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl
Total Standard Deviation in ln(k): 0.6334037785310471""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl
Total Standard Deviation in ln(k): 0.6334037785310471
""",
)

entry(
    index = 620,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.000468708,'m^3/(mol*s)'), n=2.83774, w0=(299.5,'kJ/mol'), E0=(30.083,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0056025792467066324, var=0.18570890280655866, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R
    Total Standard Deviation in ln(k): 0.8779964808034161"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 0.8779964808034161""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 0.8779964808034161
""",
)

entry(
    index = 621,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R_6R!H->F",
    kinetics = ArrheniusBM(A=(0.000361617,'m^3/(mol*s)'), n=2.88829, w0=(299.5,'kJ/mol'), E0=(23.8867,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R_6R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R_6R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R_6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R_6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 622,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F",
    kinetics = ArrheniusBM(A=(3.71283e-05,'m^3/(mol*s)'), n=3.14411, w0=(299.5,'kJ/mol'), E0=(23.0959,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.02565938238436312, var=0.011180835519648491, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F
    Total Standard Deviation in ln(k): 0.27645043462074254"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F
Total Standard Deviation in ln(k): 0.27645043462074254""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F
Total Standard Deviation in ln(k): 0.27645043462074254
""",
)

entry(
    index = 623,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.000229474,'m^3/(mol*s)'), n=2.8827, w0=(299.5,'kJ/mol'), E0=(23.0659,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_6BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 624,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_N-6BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(2.99305e-05,'m^3/(mol*s)'), n=3.20569, w0=(299.5,'kJ/mol'), E0=(27.3151,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_N-6BrCClINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_N-6BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_N-6BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->F_N-6BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 625,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(3.34555e-05,'m^3/(mol*s)'), n=3.14313, w0=(299.5,'kJ/mol'), E0=(34.2166,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_N-5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_4R!H->F_Ext-3C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 626,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F",
    kinetics = ArrheniusBM(A=(2.34009e+21,'m^3/(mol*s)'), n=-4.16639, w0=(298.308,'kJ/mol'), E0=(97.5819,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.025831034822746273, var=17.54372396267059, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F',), comment="""BM rule fitted to 9 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F
    Total Standard Deviation in ln(k): 8.46178084864952"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F
Total Standard Deviation in ln(k): 8.46178084864952""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F
Total Standard Deviation in ln(k): 8.46178084864952
""",
)

entry(
    index = 627,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_4BrCClO->C",
    kinetics = ArrheniusBM(A=(0.000432682,'m^3/(mol*s)'), n=2.92215, w0=(299.5,'kJ/mol'), E0=(19.5913,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.025862488516359944, var=2.16044899202608, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_4BrCClO->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_4BrCClO->C
    Total Standard Deviation in ln(k): 3.011634140120933"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_4BrCClO->C
Total Standard Deviation in ln(k): 3.011634140120933""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_4BrCClO->C
Total Standard Deviation in ln(k): 3.011634140120933
""",
)

entry(
    index = 628,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_4BrCClO->C_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.00290261,'m^3/(mol*s)'), n=2.72416, w0=(299.5,'kJ/mol'), E0=(13.872,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_4BrCClO->C_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_4BrCClO->C_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_4BrCClO->C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_4BrCClO->C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 629,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C",
    kinetics = ArrheniusBM(A=(5.67642e+24,'m^3/(mol*s)'), n=-5.13681, w0=(297.967,'kJ/mol'), E0=(104.767,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.16556248424213246, var=27.184796538711517, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C',), comment="""BM rule fitted to 7 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C
    Total Standard Deviation in ln(k): 10.868482691239276"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C
Total Standard Deviation in ln(k): 10.868482691239276""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C
Total Standard Deviation in ln(k): 10.868482691239276
""",
)

entry(
    index = 630,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_4BrClO->O",
    kinetics = ArrheniusBM(A=(13646.4,'m^3/(mol*s)'), n=0.741772, w0=(299.5,'kJ/mol'), E0=(58.7859,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09764253340944089, var=18.99453308236256, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_4BrClO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_4BrClO->O
    Total Standard Deviation in ln(k): 8.982513352721941"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_4BrClO->O
Total Standard Deviation in ln(k): 8.982513352721941""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_4BrClO->O
Total Standard Deviation in ln(k): 8.982513352721941
""",
)

entry(
    index = 631,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_4BrClO->O_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(6.20565e-06,'m^3/(mol*s)'), n=3.17637, w0=(299.5,'kJ/mol'), E0=(24.8738,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_4BrClO->O_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_4BrClO->O_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_4BrClO->O_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_4BrClO->O_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 632,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O",
    kinetics = ArrheniusBM(A=(8.85524e+28,'m^3/(mol*s)'), n=-6.32657, w0=(297.354,'kJ/mol'), E0=(112.204,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.44994312531219244, var=42.40884390042175, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O
    Total Standard Deviation in ln(k): 14.185760767945816"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O
Total Standard Deviation in ln(k): 14.185760767945816""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O
Total Standard Deviation in ln(k): 14.185760767945816
""",
)

entry(
    index = 633,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O_1FO->O",
    kinetics = ArrheniusBM(A=(4.23015e+32,'m^3/(mol*s)'), n=-7.34461, w0=(299.5,'kJ/mol'), E0=(126.254,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12466635039419462, var=61.82607719063019, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O_1FO->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O_1FO->O
    Total Standard Deviation in ln(k): 16.07637575828881"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O_1FO->O
Total Standard Deviation in ln(k): 16.07637575828881""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O_1FO->O
Total Standard Deviation in ln(k): 16.07637575828881
""",
)

entry(
    index = 634,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O_1FO->O_Ext-3C-R",
    kinetics = ArrheniusBM(A=(61.8219,'m^3/(mol*s)'), n=1.547, w0=(299.5,'kJ/mol'), E0=(8.7966,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2761533716883881, var=100.65204053031188, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O_1FO->O_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O_1FO->O_Ext-3C-R
    Total Standard Deviation in ln(k): 20.80645569785425"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O_1FO->O_Ext-3C-R
Total Standard Deviation in ln(k): 20.80645569785425""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O_1FO->O_Ext-3C-R
Total Standard Deviation in ln(k): 20.80645569785425
""",
)

entry(
    index = 635,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O_1FO->O_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(4.02363e-05,'m^3/(mol*s)'), n=3.27282, w0=(299.5,'kJ/mol'), E0=(36.8314,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O_1FO->O_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O_1FO->O_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O_1FO->O_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O_1FO->O_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 636,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O_N-1FO->O",
    kinetics = ArrheniusBM(A=(0.00135502,'m^3/(mol*s)'), n=2.64458, w0=(288.77,'kJ/mol'), E0=(14.1264,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O_N-1FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O_N-1FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O_N-1FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_1BrClFO-u0_N-Sp-4R!H=3C_N-1BrClFO->Cl_N-4R!H->F_N-4BrCClO->C_N-4BrClO->O_N-1FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 637,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0",
    kinetics = ArrheniusBM(A=(2.83682e+14,'m^3/(mol*s)'), n=-2.51424, w0=(299.5,'kJ/mol'), E0=(94.8892,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12590628069136064, var=6.348460548714553, Tref=1000.0, N=29, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0',), comment="""BM rule fitted to 29 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0
    Total Standard Deviation in ln(k): 5.367508329406724"""),
    rank = 11,
    shortDesc = """BM rule fitted to 29 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0
Total Standard Deviation in ln(k): 5.367508329406724""",
    longDesc = 
"""
BM rule fitted to 29 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0
Total Standard Deviation in ln(k): 5.367508329406724
""",
)

entry(
    index = 638,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1",
    kinetics = ArrheniusBM(A=(278528,'m^3/(mol*s)'), n=0.0175857, w0=(299.5,'kJ/mol'), E0=(73.3341,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09625806635824079, var=3.707068727511735, Tref=1000.0, N=26, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1',), comment="""BM rule fitted to 26 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1
    Total Standard Deviation in ln(k): 4.1017211528055295"""),
    rank = 11,
    shortDesc = """BM rule fitted to 26 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1
Total Standard Deviation in ln(k): 4.1017211528055295""",
    longDesc = 
"""
BM rule fitted to 26 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1
Total Standard Deviation in ln(k): 4.1017211528055295
""",
)

entry(
    index = 639,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl",
    kinetics = ArrheniusBM(A=(4410.4,'m^3/(mol*s)'), n=0.49332, w0=(299.5,'kJ/mol'), E0=(68.5624,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.19030879727095043, var=4.594237030248893, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl',), comment="""BM rule fitted to 17 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl
    Total Standard Deviation in ln(k): 4.775146330548346"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl
Total Standard Deviation in ln(k): 4.775146330548346""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl
Total Standard Deviation in ln(k): 4.775146330548346
""",
)

entry(
    index = 640,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(0.0885627,'m^3/(mol*s)'), n=1.70837, w0=(299.5,'kJ/mol'), E0=(60.2271,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.30826726509533314, var=2.2875219149715322, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl
    Total Standard Deviation in ln(k): 3.8066136435009783"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl
Total Standard Deviation in ln(k): 3.8066136435009783""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl
Total Standard Deviation in ln(k): 3.8066136435009783
""",
)

entry(
    index = 641,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.0984745,'m^3/(mol*s)'), n=1.70617, w0=(299.5,'kJ/mol'), E0=(60.5674,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.32932391982438813, var=3.0592836879115284, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R
    Total Standard Deviation in ln(k): 4.333890692323977"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 4.333890692323977""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 4.333890692323977
""",
)

entry(
    index = 642,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(0.234631,'m^3/(mol*s)'), n=1.6298, w0=(299.5,'kJ/mol'), E0=(63.0449,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3047420310533887, var=8.674633303959412, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_Ext-6R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 6.670175679003066"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 6.670175679003066""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 6.670175679003066
""",
)

entry(
    index = 643,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_Ext-6R!H-R_7R!H->C",
    kinetics = ArrheniusBM(A=(5.60342e-05,'m^3/(mol*s)'), n=2.80226, w0=(299.5,'kJ/mol'), E0=(52.2979,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3256562996986553, var=4.26704461931162, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_Ext-6R!H-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_Ext-6R!H-R_7R!H->C
    Total Standard Deviation in ln(k): 4.95937828323101"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_Ext-6R!H-R_7R!H->C
Total Standard Deviation in ln(k): 4.95937828323101""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_Ext-6R!H-R_7R!H->C
Total Standard Deviation in ln(k): 4.95937828323101
""",
)

entry(
    index = 644,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_Ext-6R!H-R_7R!H->C_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(0.000148664,'m^3/(mol*s)'), n=2.72935, w0=(299.5,'kJ/mol'), E0=(49.6869,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_Ext-6R!H-R_7R!H->C_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_Ext-6R!H-R_7R!H->C_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_Ext-6R!H-R_7R!H->C_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_Ext-6R!H-R_7R!H->C_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 645,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_Ext-6R!H-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(0.00890658,'m^3/(mol*s)'), n=1.76738, w0=(299.5,'kJ/mol'), E0=(62.2717,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_Ext-6R!H-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_Ext-6R!H-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_Ext-6R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_Ext-6R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 646,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(0.027169,'m^3/(mol*s)'), n=1.73665, w0=(299.5,'kJ/mol'), E0=(53.4699,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 647,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(0.0567875,'m^3/(mol*s)'), n=1.80944, w0=(299.5,'kJ/mol'), E0=(60.9599,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_5R!H->Cl_Ext-3C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 648,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(15.8796,'m^3/(mol*s)'), n=1.26479, w0=(299.5,'kJ/mol'), E0=(60.0106,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.23621738488104926, var=5.007989026142697, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl',), comment="""BM rule fitted to 11 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 5.07981475767414"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 5.07981475767414""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 5.07981475767414
""",
)

entry(
    index = 649,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(809.106,'m^3/(mol*s)'), n=0.734667, w0=(299.5,'kJ/mol'), E0=(67.4562,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.29271903261677024, var=8.944312760987572, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 6.731044957303672"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R
Total Standard Deviation in ln(k): 6.731044957303672""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R
Total Standard Deviation in ln(k): 6.731044957303672
""",
)

entry(
    index = 650,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C",
    kinetics = ArrheniusBM(A=(0.00453613,'m^3/(mol*s)'), n=2.12352, w0=(299.5,'kJ/mol'), E0=(51.972,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2439180066479592, var=8.836815907673301, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C
    Total Standard Deviation in ln(k): 6.57229165104596"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 6.57229165104596""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 6.57229165104596
""",
)

entry(
    index = 651,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_6R!H->C",
    kinetics = ArrheniusBM(A=(5.66845e-11,'m^3/(mol*s)'), n=4.40349, w0=(299.5,'kJ/mol'), E0=(10.0632,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.013275139454150008, var=2.58520818354354, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_6R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_6R!H->C
    Total Standard Deviation in ln(k): 3.2566844746034316"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_6R!H->C
Total Standard Deviation in ln(k): 3.2566844746034316""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_6R!H->C
Total Standard Deviation in ln(k): 3.2566844746034316
""",
)

entry(
    index = 652,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_6R!H->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.000140688,'m^3/(mol*s)'), n=2.66229, w0=(299.5,'kJ/mol'), E0=(38.4052,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3773197575506914, var=0.002543402745941579, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_6R!H->C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_6R!H->C_Ext-3C-R
    Total Standard Deviation in ln(k): 1.0491427116922123"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_6R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 1.0491427116922123""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_6R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 1.0491427116922123
""",
)

entry(
    index = 653,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_6R!H->C_Ext-3C-R_Ext-5BrCFINOPSSi-R_Ext-5BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(0.000151446,'m^3/(mol*s)'), n=2.66819, w0=(299.5,'kJ/mol'), E0=(39.2969,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_6R!H->C_Ext-3C-R_Ext-5BrCFINOPSSi-R_Ext-5BrCFINOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_6R!H->C_Ext-3C-R_Ext-5BrCFINOPSSi-R_Ext-5BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_6R!H->C_Ext-3C-R_Ext-5BrCFINOPSSi-R_Ext-5BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_6R!H->C_Ext-3C-R_Ext-5BrCFINOPSSi-R_Ext-5BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 654,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_N-6R!H->C",
    kinetics = ArrheniusBM(A=(0.174138,'m^3/(mol*s)'), n=1.64625, w0=(299.5,'kJ/mol'), E0=(68.3341,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.474843510785093, var=31.991518218954337, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_N-6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_N-6R!H->C
    Total Standard Deviation in ln(k): 12.532065258694836"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_N-6R!H->C
Total Standard Deviation in ln(k): 12.532065258694836""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_N-6R!H->C
Total Standard Deviation in ln(k): 12.532065258694836
""",
)

entry(
    index = 655,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_N-6R!H->C_Ext-5BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(0.000685288,'m^3/(mol*s)'), n=2.02041, w0=(299.5,'kJ/mol'), E0=(60.9353,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_N-6R!H->C_Ext-5BrCFINOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_N-6R!H->C_Ext-5BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_N-6R!H->C_Ext-5BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_Sp-5BrCFINOPSSi-3C_N-6R!H->C_Ext-5BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 656,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_N-Sp-5BrCFINOPSSi-3C",
    kinetics = ArrheniusBM(A=(0.00205139,'m^3/(mol*s)'), n=2.91659, w0=(299.5,'kJ/mol'), E0=(60.9744,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_N-Sp-5BrCFINOPSSi-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_N-Sp-5BrCFINOPSSi-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_N-Sp-5BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-5BrCFINOPSSi-R_N-Sp-5BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 657,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R",
    kinetics = ArrheniusBM(A=(7.44899e-05,'m^3/(mol*s)'), n=2.92396, w0=(299.5,'kJ/mol'), E0=(38.6298,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2817461696210709, var=0.6995800279417627, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R
    Total Standard Deviation in ln(k): 2.3846834253176956"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 2.3846834253176956""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 2.3846834253176956
""",
)

entry(
    index = 658,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R_5BrCFINOPSSi->O",
    kinetics = ArrheniusBM(A=(0.0125162,'m^3/(mol*s)'), n=2.29978, w0=(299.5,'kJ/mol'), E0=(43.0082,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18994344585724204, var=0.4600262193396319, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R_5BrCFINOPSSi->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R_5BrCFINOPSSi->O
    Total Standard Deviation in ln(k): 1.8369610704807378"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R_5BrCFINOPSSi->O
Total Standard Deviation in ln(k): 1.8369610704807378""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R_5BrCFINOPSSi->O
Total Standard Deviation in ln(k): 1.8369610704807378
""",
)

entry(
    index = 659,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R_5BrCFINOPSSi->O_6R!H->C",
    kinetics = ArrheniusBM(A=(0.00054819,'m^3/(mol*s)'), n=2.65512, w0=(299.5,'kJ/mol'), E0=(38.9677,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R_5BrCFINOPSSi->O_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R_5BrCFINOPSSi->O_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R_5BrCFINOPSSi->O_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R_5BrCFINOPSSi->O_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 660,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R_5BrCFINOPSSi->O_N-6R!H->C",
    kinetics = ArrheniusBM(A=(4.61982,'m^3/(mol*s)'), n=1.59815, w0=(299.5,'kJ/mol'), E0=(50.1338,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R_5BrCFINOPSSi->O_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R_5BrCFINOPSSi->O_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R_5BrCFINOPSSi->O_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R_5BrCFINOPSSi->O_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 661,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R_N-5BrCFINOPSSi->O",
    kinetics = ArrheniusBM(A=(0.000495128,'m^3/(mol*s)'), n=2.66142, w0=(299.5,'kJ/mol'), E0=(45.3557,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R_N-5BrCFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R_N-5BrCFINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R_N-5BrCFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_Ext-3C-R_N-5BrCFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 662,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_5BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.210425,'m^3/(mol*s)'), n=1.63892, w0=(299.5,'kJ/mol'), E0=(46.319,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_5BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_5BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 663,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.776813,'m^3/(mol*s)'), n=1.65286, w0=(299.5,'kJ/mol'), E0=(62.8975,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 664,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(80105,'m^3/(mol*s)'), n=0.248402, w0=(299.5,'kJ/mol'), E0=(72.0677,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.01833227964526745, var=2.982206897535867, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl',), comment="""BM rule fitted to 9 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl
    Total Standard Deviation in ln(k): 3.5080515263536"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl
Total Standard Deviation in ln(k): 3.5080515263536""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl
Total Standard Deviation in ln(k): 3.5080515263536
""",
)

entry(
    index = 665,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C",
    kinetics = ArrheniusBM(A=(13.893,'m^3/(mol*s)'), n=1.43821, w0=(299.5,'kJ/mol'), E0=(60.556,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11315095062481396, var=1.4138184177615591, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C
    Total Standard Deviation in ln(k): 2.668011003017915"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C
Total Standard Deviation in ln(k): 2.668011003017915""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C
Total Standard Deviation in ln(k): 2.668011003017915
""",
)

entry(
    index = 666,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(0.00861799,'m^3/(mol*s)'), n=2.31906, w0=(299.5,'kJ/mol'), E0=(57.9225,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17825512019873363, var=0.23466641337535726, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Ext-4C-R
    Total Standard Deviation in ln(k): 1.4190185610309238"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Ext-4C-R
Total Standard Deviation in ln(k): 1.4190185610309238""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Ext-4C-R
Total Standard Deviation in ln(k): 1.4190185610309238
""",
)

entry(
    index = 667,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Ext-4C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.000430651,'m^3/(mol*s)'), n=2.78666, w0=(299.5,'kJ/mol'), E0=(62.295,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Ext-4C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Ext-4C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Ext-4C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Ext-4C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 668,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Sp-4C-3C",
    kinetics = ArrheniusBM(A=(0.0247267,'m^3/(mol*s)'), n=2.22873, w0=(299.5,'kJ/mol'), E0=(47.3043,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17677307780058454, var=2.397239101935136, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Sp-4C-3C',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Sp-4C-3C
    Total Standard Deviation in ln(k): 3.548088803736505"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Sp-4C-3C
Total Standard Deviation in ln(k): 3.548088803736505""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Sp-4C-3C
Total Standard Deviation in ln(k): 3.548088803736505
""",
)

entry(
    index = 669,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Sp-4C-3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.00436923,'m^3/(mol*s)'), n=2.47085, w0=(299.5,'kJ/mol'), E0=(41.6908,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.21444140842164053, var=2.6102295710096346, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Sp-4C-3C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Sp-4C-3C_Ext-3C-R
    Total Standard Deviation in ln(k): 3.7776885787052934"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Sp-4C-3C_Ext-3C-R
Total Standard Deviation in ln(k): 3.7776885787052934""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Sp-4C-3C_Ext-3C-R
Total Standard Deviation in ln(k): 3.7776885787052934
""",
)

entry(
    index = 670,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Sp-4C-3C_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.000447245,'m^3/(mol*s)'), n=2.63852, w0=(299.5,'kJ/mol'), E0=(35.2326,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Sp-4C-3C_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Sp-4C-3C_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Sp-4C-3C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_Sp-4C-3C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 671,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_N-Sp-4C-3C",
    kinetics = ArrheniusBM(A=(0.00285547,'m^3/(mol*s)'), n=2.56268, w0=(299.5,'kJ/mol'), E0=(48.0832,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_N-Sp-4C-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_N-Sp-4C-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_N-Sp-4C-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_4BrCFO->C_N-Sp-4C-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 672,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_N-4BrCFO->C",
    kinetics = ArrheniusBM(A=(4.39905,'m^3/(mol*s)'), n=1.24451, w0=(299.5,'kJ/mol'), E0=(61.9944,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.13451216915785605, var=0.8356866734432951, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_N-4BrCFO->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_N-4BrCFO->C
    Total Standard Deviation in ln(k): 2.1706168836735036"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_N-4BrCFO->C
Total Standard Deviation in ln(k): 2.1706168836735036""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_N-4BrCFO->C
Total Standard Deviation in ln(k): 2.1706168836735036
""",
)

entry(
    index = 673,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_N-4BrCFO->C_4BrFO->O",
    kinetics = ArrheniusBM(A=(0.589857,'m^3/(mol*s)'), n=1.65372, w0=(299.5,'kJ/mol'), E0=(64.4935,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_N-4BrCFO->C_4BrFO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_N-4BrCFO->C_4BrFO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_N-4BrCFO->C_4BrFO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_N-4BrCFO->C_4BrFO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 674,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_N-4BrCFO->C_N-4BrFO->O",
    kinetics = ArrheniusBM(A=(0.00782324,'m^3/(mol*s)'), n=1.95281, w0=(299.5,'kJ/mol'), E0=(52.1056,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1366819415789349, var=0.25664486196267866, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_N-4BrCFO->C_N-4BrFO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_N-4BrCFO->C_N-4BrFO->O
    Total Standard Deviation in ln(k): 1.3590233300566865"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_N-4BrCFO->C_N-4BrFO->O
Total Standard Deviation in ln(k): 1.3590233300566865""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_N-4BrCFO->C_N-4BrFO->O
Total Standard Deviation in ln(k): 1.3590233300566865
""",
)

entry(
    index = 675,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_N-4BrCFO->C_N-4BrFO->O_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.0547955,'m^3/(mol*s)'), n=1.74792, w0=(299.5,'kJ/mol'), E0=(55.8502,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_N-4BrCFO->C_N-4BrFO->O_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_N-4BrCFO->C_N-4BrFO->O_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_N-4BrCFO->C_N-4BrFO->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_3C-u1_N-4R!H->Cl_N-4BrCFO->C_N-4BrFO->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 676,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_N-3C-u1",
    kinetics = ArrheniusBM(A=(32697.6,'m^3/(mol*s)'), n=0.75861, w0=(299.5,'kJ/mol'), E0=(25.1069,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3754533374258913, var=9.695185503213164, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_N-3C-u1',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_N-3C-u1
    Total Standard Deviation in ln(k): 7.185512315816049"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_N-3C-u1
Total Standard Deviation in ln(k): 7.185512315816049""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_N-1BrClFO-u0_N-3C-u1
Total Standard Deviation in ln(k): 7.185512315816049
""",
)

entry(
    index = 677,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.224744,'m^3/(mol*s)'), n=2.18071, w0=(269.342,'kJ/mol'), E0=(31.1285,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4905993532545772, var=0.7773850464450843, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C',), comment="""BM rule fitted to 10 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 3.000225418575029"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 3.000225418575029""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 3.000225418575029
""",
)

entry(
    index = 678,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(0.0199658,'m^3/(mol*s)'), n=2.45102, w0=(272,'kJ/mol'), E0=(5.35318,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.9167029906025199, var=1.096842446223129, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 4.402837827289003"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 4.402837827289003""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 4.402837827289003
""",
)

entry(
    index = 679,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(1512.69,'m^3/(mol*s)'), n=0.821119, w0=(272,'kJ/mol'), E0=(23.5476,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6453381654092957, var=2.233054471172977, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_Sp-5R!H-4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 4.617210126184595"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 4.617210126184595""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 4.617210126184595
""",
)

entry(
    index = 680,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_Sp-5R!H-4R!H_1BrClFO-u0",
    kinetics = ArrheniusBM(A=(0.0483302,'m^3/(mol*s)'), n=2.06003, w0=(272,'kJ/mol'), E0=(1.48162,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_Sp-5R!H-4R!H_1BrClFO-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_Sp-5R!H-4R!H_1BrClFO-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_Sp-5R!H-4R!H_1BrClFO-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_Sp-5R!H-4R!H_1BrClFO-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 681,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_Sp-5R!H-4R!H_N-1BrClFO-u0",
    kinetics = ArrheniusBM(A=(25.9488,'m^3/(mol*s)'), n=1.37612, w0=(272,'kJ/mol'), E0=(18.8126,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_Sp-5R!H-4R!H_N-1BrClFO-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_Sp-5R!H-4R!H_N-1BrClFO-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_Sp-5R!H-4R!H_N-1BrClFO-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_Sp-5R!H-4R!H_N-1BrClFO-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 682,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(717.254,'m^3/(mol*s)'), n=1.30041, w0=(272,'kJ/mol'), E0=(74.5508,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.35221910682086516, var=0.25165639362137593, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 1.890655317170107"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 1.890655317170107""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 1.890655317170107
""",
)

entry(
    index = 683,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(2.7538,'m^3/(mol*s)'), n=1.95088, w0=(272,'kJ/mol'), E0=(65.6743,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-5R!H=4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 684,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(0.116843,'m^3/(mol*s)'), n=2.40658, w0=(272,'kJ/mol'), E0=(52.8436,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.8088605316747004, var=0.11845617635557605, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-5R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 2.722291848388196"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 2.722291848388196""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 2.722291848388196
""",
)

entry(
    index = 685,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-5R!H=4R!H_1BrClFO-u0",
    kinetics = ArrheniusBM(A=(0.00730549,'m^3/(mol*s)'), n=2.76801, w0=(272,'kJ/mol'), E0=(38.4514,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-5R!H=4R!H_1BrClFO-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-5R!H=4R!H_1BrClFO-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-5R!H=4R!H_1BrClFO-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-5R!H=4R!H_1BrClFO-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 686,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-5R!H=4R!H_N-1BrClFO-u0",
    kinetics = ArrheniusBM(A=(5.30835,'m^3/(mol*s)'), n=1.91524, w0=(272,'kJ/mol'), E0=(62.684,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-5R!H=4R!H_N-1BrClFO-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-5R!H=4R!H_N-1BrClFO-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-5R!H=4R!H_N-1BrClFO-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-5R!H=4R!H_N-1BrClFO-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 687,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_4R!H->C",
    kinetics = ArrheniusBM(A=(1.23504,'m^3/(mol*s)'), n=1.96419, w0=(272,'kJ/mol'), E0=(31.4286,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.38004813691876954, var=0.1331811840283738, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_4R!H->C
    Total Standard Deviation in ln(k): 1.6865027817663514"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_4R!H->C
Total Standard Deviation in ln(k): 1.6865027817663514""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_4R!H->C
Total Standard Deviation in ln(k): 1.6865027817663514
""",
)

entry(
    index = 688,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_4R!H->C_1BrClFO-u0",
    kinetics = ArrheniusBM(A=(0.00337555,'m^3/(mol*s)'), n=2.68113, w0=(272,'kJ/mol'), E0=(23.8303,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_4R!H->C_1BrClFO-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_4R!H->C_1BrClFO-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_4R!H->C_1BrClFO-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_4R!H->C_1BrClFO-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 689,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_4R!H->C_N-1BrClFO-u0",
    kinetics = ArrheniusBM(A=(204.093,'m^3/(mol*s)'), n=1.34615, w0=(272,'kJ/mol'), E0=(38.9583,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_4R!H->C_N-1BrClFO-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_4R!H->C_N-1BrClFO-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_4R!H->C_N-1BrClFO-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_4R!H->C_N-1BrClFO-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 690,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(1.82157e-05,'m^3/(mol*s)'), n=3.40746, w0=(263.14,'kJ/mol'), E0=(8.41962,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5773589129294956, var=1.1405462773939998, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C
    Total Standard Deviation in ln(k): 3.5916346501421192"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C
Total Standard Deviation in ln(k): 3.5916346501421192""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C
Total Standard Deviation in ln(k): 3.5916346501421192
""",
)

entry(
    index = 691,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C_4ClO->O",
    kinetics = ArrheniusBM(A=(6.32748e-06,'m^3/(mol*s)'), n=3.53281, w0=(258.71,'kJ/mol'), E0=(15.5151,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6909966160507658, var=3.9561909001928433, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C_4ClO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C_4ClO->O
    Total Standard Deviation in ln(k): 5.723625697507296"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C_4ClO->O
Total Standard Deviation in ln(k): 5.723625697507296""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C_4ClO->O
Total Standard Deviation in ln(k): 5.723625697507296
""",
)

entry(
    index = 692,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C_4ClO->O_1BrClFO->O",
    kinetics = ArrheniusBM(A=(1.89325e-05,'m^3/(mol*s)'), n=3.38382, w0=(272,'kJ/mol'), E0=(37.5921,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C_4ClO->O_1BrClFO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C_4ClO->O_1BrClFO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C_4ClO->O_1BrClFO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C_4ClO->O_1BrClFO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 693,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C_4ClO->O_N-1BrClFO->O",
    kinetics = ArrheniusBM(A=(0.00908931,'m^3/(mol*s)'), n=2.64082, w0=(245.42,'kJ/mol'), E0=(30.8892,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C_4ClO->O_N-1BrClFO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C_4ClO->O_N-1BrClFO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C_4ClO->O_N-1BrClFO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C_4ClO->O_N-1BrClFO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 694,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C_N-4ClO->O",
    kinetics = ArrheniusBM(A=(0.00123036,'m^3/(mol*s)'), n=2.89569, w0=(272,'kJ/mol'), E0=(27.0101,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C_N-4ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C_N-4ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C_N-4ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_Ext-3BrCClFINOPSSi-R_N-3BrCClFINOPSSi->C_N-4R!H->C_N-4ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 695,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1",
    kinetics = ArrheniusBM(A=(0.000457003,'m^3/(mol*s)'), n=3.08165, w0=(269.156,'kJ/mol'), E0=(7.90331,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.13066049254889042, var=2.9071209498534136, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1',), comment="""BM rule fitted to 14 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1
    Total Standard Deviation in ln(k): 3.7464224101464527"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1
Total Standard Deviation in ln(k): 3.7464224101464527""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1
Total Standard Deviation in ln(k): 3.7464224101464527
""",
)

entry(
    index = 696,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0",
    kinetics = ArrheniusBM(A=(0.0121443,'m^3/(mol*s)'), n=2.68276, w0=(269.526,'kJ/mol'), E0=(17.2588,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.025793320265256013, var=2.4268269194737986, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0',), comment="""BM rule fitted to 10 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0
    Total Standard Deviation in ln(k): 3.187839028323095"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0
Total Standard Deviation in ln(k): 3.187839028323095""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0
Total Standard Deviation in ln(k): 3.187839028323095
""",
)

entry(
    index = 697,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_3BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.00102068,'m^3/(mol*s)'), n=3.15929, w0=(299.5,'kJ/mol'), E0=(0.0695393,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18824435061559772, var=12.508943138294745, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_3BrCClFINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_3BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 7.563319630698585"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 7.563319630698585""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 7.563319630698585
""",
)

entry(
    index = 698,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_3BrCClFINOPSSi->C_Ext-1BrClFO-R",
    kinetics = ArrheniusBM(A=(0.00549393,'m^3/(mol*s)'), n=2.84052, w0=(299.5,'kJ/mol'), E0=(48.0944,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_3BrCClFINOPSSi->C_Ext-1BrClFO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_3BrCClFINOPSSi->C_Ext-1BrClFO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_3BrCClFINOPSSi->C_Ext-1BrClFO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_3BrCClFINOPSSi->C_Ext-1BrClFO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 699,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.00394725,'m^3/(mol*s)'), n=2.7805, w0=(262.033,'kJ/mol'), E0=(12.9502,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0531671349412505, var=2.5406890711494983, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C',), comment="""BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 3.3290410837915485"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 3.3290410837915485""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 3.3290410837915485
""",
)

entry(
    index = 700,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R",
    kinetics = ArrheniusBM(A=(0.068553,'m^3/(mol*s)'), n=2.37581, w0=(267.57,'kJ/mol'), E0=(18.0876,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.005774442206094593, var=3.275590353876276, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R
    Total Standard Deviation in ln(k): 3.642796888787234"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R
Total Standard Deviation in ln(k): 3.642796888787234""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R
Total Standard Deviation in ln(k): 3.642796888787234
""",
)

entry(
    index = 701,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O",
    kinetics = ArrheniusBM(A=(0.0181845,'m^3/(mol*s)'), n=2.51252, w0=(272,'kJ/mol'), E0=(14.4416,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1295159349359336, var=3.912327246186039, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O
    Total Standard Deviation in ln(k): 4.290703467973239"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O
Total Standard Deviation in ln(k): 4.290703467973239""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O
Total Standard Deviation in ln(k): 4.290703467973239
""",
)

entry(
    index = 702,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(151.351,'m^3/(mol*s)'), n=1.41346, w0=(272,'kJ/mol'), E0=(19.2251,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.9608509848699642, var=1.5863375183402106, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_Ext-4R!H-R
    Total Standard Deviation in ln(k): 7.451722924515038"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_Ext-4R!H-R
Total Standard Deviation in ln(k): 7.451722924515038""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_Ext-4R!H-R
Total Standard Deviation in ln(k): 7.451722924515038
""",
)

entry(
    index = 703,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_Ext-4R!H-R_Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(4.43941,'m^3/(mol*s)'), n=1.76166, w0=(272,'kJ/mol'), E0=(1.39272,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_Ext-4R!H-R_Sp-5R!H-4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_Ext-4R!H-R_Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_Ext-4R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_Ext-4R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 704,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_Ext-4R!H-R_N-Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(1.4941,'m^3/(mol*s)'), n=2.07904, w0=(272,'kJ/mol'), E0=(46.1346,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_Ext-4R!H-R_N-Sp-5R!H-4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_Ext-4R!H-R_N-Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_Ext-4R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_Ext-4R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 705,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_4R!H->Cl",
    kinetics = ArrheniusBM(A=(0.0597365,'m^3/(mol*s)'), n=2.3895, w0=(272,'kJ/mol'), E0=(28.4542,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_4R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_4R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 706,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(7.0942e-06,'m^3/(mol*s)'), n=3.45254, w0=(272,'kJ/mol'), E0=(9.50222,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4670151349553045, var=7.474347444498696, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_N-4R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_N-4R!H->Cl
    Total Standard Deviation in ln(k): 6.654200772374844"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_N-4R!H->Cl
Total Standard Deviation in ln(k): 6.654200772374844""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_N-4R!H->Cl
Total Standard Deviation in ln(k): 6.654200772374844
""",
)

entry(
    index = 707,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_N-4R!H->Cl_4CO->C",
    kinetics = ArrheniusBM(A=(0.0703235,'m^3/(mol*s)'), n=2.34313, w0=(272,'kJ/mol'), E0=(24.1416,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_N-4R!H->Cl_4CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_N-4R!H->Cl_4CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_N-4R!H->Cl_4CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_N-4R!H->Cl_4CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 708,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_N-4R!H->Cl_N-4CO->C",
    kinetics = ArrheniusBM(A=(0.0290111,'m^3/(mol*s)'), n=2.3822, w0=(272,'kJ/mol'), E0=(40.8088,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_N-4R!H->Cl_N-4CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_N-4R!H->Cl_N-4CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_N-4R!H->Cl_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_3BrClO->O_N-4R!H->Cl_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 709,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_N-3BrClO->O",
    kinetics = ArrheniusBM(A=(80.5994,'m^3/(mol*s)'), n=1.63822, w0=(245.42,'kJ/mol'), E0=(35.2843,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_N-3BrClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_N-3BrClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_N-3BrClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_Ext-1BrClFO-R_N-3BrClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 710,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_1BrClFO->O",
    kinetics = ArrheniusBM(A=(49.219,'m^3/(mol*s)'), n=1.86416, w0=(245.42,'kJ/mol'), E0=(28.1333,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_1BrClFO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_1BrClFO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_1BrClFO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_1BrClFO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 711,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_N-1BrClFO->O",
    kinetics = ArrheniusBM(A=(8.50529,'m^3/(mol*s)'), n=1.86514, w0=(245.42,'kJ/mol'), E0=(27.3857,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_N-1BrClFO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_N-1BrClFO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_N-1BrClFO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_1BrClFO-u0_N-3BrCClFINOPSSi->C_N-1BrClFO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 712,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0",
    kinetics = ArrheniusBM(A=(9.11766e-05,'m^3/(mol*s)'), n=3.25915, w0=(268.23,'kJ/mol'), E0=(2.08301,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2654947387831439, var=7.788100361311907, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0
    Total Standard Deviation in ln(k): 6.261720105209482"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0
Total Standard Deviation in ln(k): 6.261720105209482""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0
Total Standard Deviation in ln(k): 6.261720105209482
""",
)

entry(
    index = 713,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_3BrCClFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(1.3609e+06,'m^3/(mol*s)'), n=0.498188, w0=(245.42,'kJ/mol'), E0=(46.1405,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_3BrCClFINOPSSi->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_3BrCClFINOPSSi->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_3BrCClFINOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_3BrCClFINOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 714,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(0.000128554,'m^3/(mol*s)'), n=3.16506, w0=(275.833,'kJ/mol'), E0=(4.57928,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.21719781774309602, var=13.483914914631317, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br
    Total Standard Deviation in ln(k): 7.90720069551793"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br
Total Standard Deviation in ln(k): 7.90720069551793""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br
Total Standard Deviation in ln(k): 7.90720069551793
""",
)

entry(
    index = 715,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br_3CClO->Cl",
    kinetics = ArrheniusBM(A=(1.50923e+06,'m^3/(mol*s)'), n=0.331641, w0=(256,'kJ/mol'), E0=(25.5497,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br_3CClO->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br_3CClO->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br_3CClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br_3CClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 716,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br_N-3CClO->Cl",
    kinetics = ArrheniusBM(A=(2.59015e-06,'m^3/(mol*s)'), n=3.62508, w0=(285.75,'kJ/mol'), E0=(6.26909,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.9940632303698039, var=64.85312634483438, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br_N-3CClO->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br_N-3CClO->Cl
    Total Standard Deviation in ln(k): 18.642066326110125"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br_N-3CClO->Cl
Total Standard Deviation in ln(k): 18.642066326110125""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br_N-3CClO->Cl
Total Standard Deviation in ln(k): 18.642066326110125
""",
)

entry(
    index = 717,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br_N-3CClO->Cl_3CO->C",
    kinetics = ArrheniusBM(A=(83.5364,'m^3/(mol*s)'), n=1.48277, w0=(299.5,'kJ/mol'), E0=(71.6278,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br_N-3CClO->Cl_3CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br_N-3CClO->Cl_3CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br_N-3CClO->Cl_3CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br_N-3CClO->Cl_3CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 718,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br_N-3CClO->Cl_N-3CO->C",
    kinetics = ArrheniusBM(A=(3523.39,'m^3/(mol*s)'), n=0.999173, w0=(272,'kJ/mol'), E0=(16.8442,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br_N-3CClO->Cl_N-3CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br_N-3CClO->Cl_N-3CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br_N-3CClO->Cl_N-3CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_3BrCClFINOPSSi-u1_N-1BrClFO-u0_N-3BrCClFINOPSSi->Br_N-3CClO->Cl_N-3CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 719,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1",
    kinetics = ArrheniusBM(A=(0.072914,'m^3/(mol*s)'), n=2.56158, w0=(273.38,'kJ/mol'), E0=(9.07456,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17059233194272588, var=1.1456758531408489, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1',), comment="""BM rule fitted to 9 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1
    Total Standard Deviation in ln(k): 2.5744171724122804"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1
Total Standard Deviation in ln(k): 2.5744171724122804""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1
Total Standard Deviation in ln(k): 2.5744171724122804
""",
)

entry(
    index = 720,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_1BrClFO->Br",
    kinetics = ArrheniusBM(A=(8949.92,'m^3/(mol*s)'), n=1.08089, w0=(245.42,'kJ/mol'), E0=(42.899,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_1BrClFO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_1BrClFO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_1BrClFO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_1BrClFO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 721,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br",
    kinetics = ArrheniusBM(A=(0.348277,'m^3/(mol*s)'), n=2.36983, w0=(276.875,'kJ/mol'), E0=(11.355,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.020732688923790994, var=0.6856280462375826, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br',), comment="""BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br
    Total Standard Deviation in ln(k): 1.7120661483340962"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br
Total Standard Deviation in ln(k): 1.7120661483340962""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br
Total Standard Deviation in ln(k): 1.7120661483340962
""",
)

entry(
    index = 722,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0",
    kinetics = ArrheniusBM(A=(0.635249,'m^3/(mol*s)'), n=2.30095, w0=(273.643,'kJ/mol'), E0=(12.5792,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.004750096094866444, var=0.7883221384137206, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0',), comment="""BM rule fitted to 7 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0
    Total Standard Deviation in ln(k): 1.7918892102750057"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0
Total Standard Deviation in ln(k): 1.7918892102750057""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0
Total Standard Deviation in ln(k): 1.7918892102750057
""",
)

entry(
    index = 723,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_3BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.221635,'m^3/(mol*s)'), n=2.53078, w0=(299.5,'kJ/mol'), E0=(37.4654,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_3BrCClFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_3BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 724,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.562779,'m^3/(mol*s)'), n=2.29956, w0=(269.333,'kJ/mol'), E0=(11.2407,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03520984233815562, var=0.8714983533367342, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 1.9599688512558078"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 1.9599688512558078""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 1.9599688512558078
""",
)

entry(
    index = 725,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O",
    kinetics = ArrheniusBM(A=(0.402836,'m^3/(mol*s)'), n=2.34729, w0=(272,'kJ/mol'), E0=(7.45893,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2103366556413032, var=1.1568838775993893, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O
    Total Standard Deviation in ln(k): 2.6847477695313136"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O
Total Standard Deviation in ln(k): 2.6847477695313136""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O
Total Standard Deviation in ln(k): 2.6847477695313136
""",
)

entry(
    index = 726,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R",
    kinetics = ArrheniusBM(A=(0.427653,'m^3/(mol*s)'), n=2.35078, w0=(272,'kJ/mol'), E0=(19.4629,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09283476352927283, var=2.475874757079821, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R
    Total Standard Deviation in ln(k): 3.387686305098207"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R
Total Standard Deviation in ln(k): 3.387686305098207""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R
Total Standard Deviation in ln(k): 3.387686305098207
""",
)

entry(
    index = 727,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.53031,'m^3/(mol*s)'), n=2.19957, w0=(272,'kJ/mol'), E0=(3.80416,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.282960222810669, var=8.257559341124429, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 8.984318720355718"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 8.984318720355718""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 8.984318720355718
""",
)

entry(
    index = 728,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R_Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(220.761,'m^3/(mol*s)'), n=1.59458, w0=(272,'kJ/mol'), E0=(64.1767,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R_Sp-5R!H=4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R_Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 729,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(78.1584,'m^3/(mol*s)'), n=1.70333, w0=(272,'kJ/mol'), E0=(16.3514,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.0174669886314587, var=7.5380643838169705, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 10.573120074889856"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 10.573120074889856""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 10.573120074889856
""",
)

entry(
    index = 730,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(177.245,'m^3/(mol*s)'), n=1.57612, w0=(272,'kJ/mol'), E0=(13.8028,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-5R!H-4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 731,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(234.788,'m^3/(mol*s)'), n=1.5918, w0=(272,'kJ/mol'), E0=(61.4167,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-5R!H-4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_1ClO->O_Ext-1O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 732,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_N-1ClO->O",
    kinetics = ArrheniusBM(A=(8060.2,'m^3/(mol*s)'), n=1.07817, w0=(256,'kJ/mol'), E0=(22.1188,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_N-1ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_N-1ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_N-1ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_1ClO-u0_N-3BrCClFINOPSSi->C_N-1ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 733,
    label = "Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_N-1ClO-u0",
    kinetics = ArrheniusBM(A=(49.4221,'m^3/(mol*s)'), n=1.71189, w0=(299.5,'kJ/mol'), E0=(51.8349,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_N-1ClO-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_N-1ClO-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_N-1ClO-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->H_N-1R->H_N-1BrCClFO->C_N-3BrCClFINOPSSi-u1_N-1BrClFO->Br_N-1ClO-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

