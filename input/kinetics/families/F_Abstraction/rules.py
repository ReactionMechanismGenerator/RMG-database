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
    kinetics = ArrheniusBM(A=(4.96973e+27,'m^3/(mol*s)'), n=-5.83531, w0=(417.725,'kJ/mol'), E0=(242.579,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9443379929189641, var=14.0043856029351, Tref=1000.0, N=180, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 180 training reactions at node Root
    Total Standard Deviation in ln(k): 9.874915120466401"""),
    rank = 11,
    shortDesc = """BM rule fitted to 180 training reactions at node Root
Total Standard Deviation in ln(k): 9.874915120466401""",
    longDesc = 
"""
BM rule fitted to 180 training reactions at node Root
Total Standard Deviation in ln(k): 9.874915120466401
""",
)

entry(
    index = 2,
    label = "Root_1R->O",
    kinetics = ArrheniusBM(A=(1.07917e-07,'m^3/(mol*s)'), n=4.10744, w0=(331.011,'kJ/mol'), E0=(90.5755,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.22354720646268836, var=4.392482733218183, Tref=1000.0, N=45, data_mean=0.0, correlation='Root_1R->O',), comment="""BM rule fitted to 45 training reactions at node Root_1R->O
    Total Standard Deviation in ln(k): 4.763250436447871"""),
    rank = 11,
    shortDesc = """BM rule fitted to 45 training reactions at node Root_1R->O
Total Standard Deviation in ln(k): 4.763250436447871""",
    longDesc = 
"""
BM rule fitted to 45 training reactions at node Root_1R->O
Total Standard Deviation in ln(k): 4.763250436447871
""",
)

entry(
    index = 3,
    label = "Root_1R->O_3R->O",
    kinetics = ArrheniusBM(A=(0.00675283,'m^3/(mol*s)'), n=3.13776, w0=(222,'kJ/mol'), E0=(112.622,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0410606131048033, var=0.8294787147797297, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R->O_3R->O',), comment="""BM rule fitted to 8 training reactions at node Root_1R->O_3R->O
    Total Standard Deviation in ln(k): 1.9289943166319716"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R->O_3R->O
Total Standard Deviation in ln(k): 1.9289943166319716""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R->O_3R->O
Total Standard Deviation in ln(k): 1.9289943166319716
""",
)

entry(
    index = 4,
    label = "Root_1R->O_3R->O_Ext-1O-R",
    kinetics = ArrheniusBM(A=(0.0458,'m^3/(mol*s)'), n=2.91847, w0=(222,'kJ/mol'), E0=(112.937,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7138295244705277, var=4.894562111418105, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-1O-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_3R->O_Ext-1O-R
    Total Standard Deviation in ln(k): 6.228748696352231"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_3R->O_Ext-1O-R
Total Standard Deviation in ln(k): 6.228748696352231""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_3R->O_Ext-1O-R
Total Standard Deviation in ln(k): 6.228748696352231
""",
)

entry(
    index = 5,
    label = "Root_1R->O_3R->O_Ext-1O-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(0.0487535,'m^3/(mol*s)'), n=3.06244, w0=(222,'kJ/mol'), E0=(73.0445,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-1O-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_Ext-4R!H-R
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
    index = 6,
    label = "Root_1R->O_3R->O_Ext-1O-R_4R!H->C",
    kinetics = ArrheniusBM(A=(0.00501249,'m^3/(mol*s)'), n=3.19462, w0=(222,'kJ/mol'), E0=(110.734,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.51550026966537, var=5.816205408888395, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-1O-R_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C
    Total Standard Deviation in ln(k): 8.642571186260438"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C
Total Standard Deviation in ln(k): 8.642571186260438""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C
Total Standard Deviation in ln(k): 8.642571186260438
""",
)

entry(
    index = 7,
    label = "Root_1R->O_3R->O_Ext-1O-R_4R!H->C_3O-u1",
    kinetics = ArrheniusBM(A=(0.0049864,'m^3/(mol*s)'), n=3.19625, w0=(222,'kJ/mol'), E0=(110.71,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-1O-R_4R!H->C_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C_3O-u1
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
    index = 8,
    label = "Root_1R->O_3R->O_Ext-1O-R_4R!H->C_N-3O-u1",
    kinetics = ArrheniusBM(A=(0.640932,'m^3/(mol*s)'), n=2.39839, w0=(222,'kJ/mol'), E0=(119.509,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-1O-R_4R!H->C_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C_N-3O-u1
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
    index = 9,
    label = "Root_1R->O_3R->O_Ext-1O-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.123333,'m^3/(mol*s)'), n=2.47323, w0=(222,'kJ/mol'), E0=(109.466,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-1O-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_N-4R!H->C
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
    index = 10,
    label = "Root_1R->O_3R->O_Ext-3O-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2.61665e-05,'m^3/(mol*s)'), n=4.03673, w0=(222,'kJ/mol'), E0=(69.581,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-3O-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-3O-R_Ext-4R!H-R
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
    index = 11,
    label = "Root_1R->O_3R->O_1O-u0",
    kinetics = ArrheniusBM(A=(0.000107807,'m^3/(mol*s)'), n=3.6367, w0=(222,'kJ/mol'), E0=(110.064,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_1O-u0',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_1O-u0
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
    index = 12,
    label = "Root_1R->O_3R->O_N-1O-u0",
    kinetics = ArrheniusBM(A=(0.0506398,'m^3/(mol*s)'), n=2.45715, w0=(222,'kJ/mol'), E0=(116.262,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2918622500720035, var=0.07798375555155851, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_3R->O_N-1O-u0',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_N-1O-u0
    Total Standard Deviation in ln(k): 1.2931559680615288"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_N-1O-u0
Total Standard Deviation in ln(k): 1.2931559680615288""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_N-1O-u0
Total Standard Deviation in ln(k): 1.2931559680615288
""",
)

entry(
    index = 13,
    label = "Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_4R!H->C",
    kinetics = ArrheniusBM(A=(0.446486,'m^3/(mol*s)'), n=2.22159, w0=(222,'kJ/mol'), E0=(121.217,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_4R!H->C
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
    index = 14,
    label = "Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.00111026,'m^3/(mol*s)'), n=2.89721, w0=(222,'kJ/mol'), E0=(109.23,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_N-4R!H->C
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
    index = 15,
    label = "Root_1R->O_N-3R->O",
    kinetics = ArrheniusBM(A=(162931,'m^3/(mol*s)'), n=0.544222, w0=(354.581,'kJ/mol'), E0=(141.776,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.22345273867100504, var=3.2868213936695034, Tref=1000.0, N=37, data_mean=0.0, correlation='Root_1R->O_N-3R->O',), comment="""BM rule fitted to 37 training reactions at node Root_1R->O_N-3R->O
    Total Standard Deviation in ln(k): 4.195942128015927"""),
    rank = 11,
    shortDesc = """BM rule fitted to 37 training reactions at node Root_1R->O_N-3R->O
Total Standard Deviation in ln(k): 4.195942128015927""",
    longDesc = 
"""
BM rule fitted to 37 training reactions at node Root_1R->O_N-3R->O
Total Standard Deviation in ln(k): 4.195942128015927
""",
)

entry(
    index = 16,
    label = "Root_1R->O_N-3R->O_3CClFH->C",
    kinetics = ArrheniusBM(A=(276.199,'m^3/(mol*s)'), n=1.31034, w0=(353.5,'kJ/mol'), E0=(130.862,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.15613588063722283, var=3.2240315222502165, Tref=1000.0, N=36, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C',), comment="""BM rule fitted to 36 training reactions at node Root_1R->O_N-3R->O_3CClFH->C
    Total Standard Deviation in ln(k): 3.9919209833841904"""),
    rank = 11,
    shortDesc = """BM rule fitted to 36 training reactions at node Root_1R->O_N-3R->O_3CClFH->C
Total Standard Deviation in ln(k): 3.9919209833841904""",
    longDesc = 
"""
BM rule fitted to 36 training reactions at node Root_1R->O_N-3R->O_3CClFH->C
Total Standard Deviation in ln(k): 3.9919209833841904
""",
)

entry(
    index = 17,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1",
    kinetics = ArrheniusBM(A=(3.98276,'m^3/(mol*s)'), n=1.78928, w0=(353.5,'kJ/mol'), E0=(117.123,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12403089073412163, var=4.19291258726444, Tref=1000.0, N=24, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1',), comment="""BM rule fitted to 24 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1
    Total Standard Deviation in ln(k): 4.41665177661177"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1
Total Standard Deviation in ln(k): 4.41665177661177""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1
Total Standard Deviation in ln(k): 4.41665177661177
""",
)

entry(
    index = 18,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.97763,'m^3/(mol*s)'), n=1.78894, w0=(353.5,'kJ/mol'), E0=(117.093,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12352055467232664, var=4.201615532377066, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R',), comment="""BM rule fitted to 22 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R
    Total Standard Deviation in ln(k): 4.419627569254125"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R
Total Standard Deviation in ln(k): 4.419627569254125""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R
Total Standard Deviation in ln(k): 4.419627569254125
""",
)

entry(
    index = 19,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(3.78375e-06,'m^3/(mol*s)'), n=3.40342, w0=(353.5,'kJ/mol'), E0=(97.0568,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.541536698425293, var=12.07024672352134, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl
    Total Standard Deviation in ln(k): 13.350673450512232"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl
Total Standard Deviation in ln(k): 13.350673450512232""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl
Total Standard Deviation in ln(k): 13.350673450512232
""",
)

entry(
    index = 20,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-1O-R",
    kinetics = ArrheniusBM(A=(1.34429e-06,'m^3/(mol*s)'), n=3.53038, w0=(353.5,'kJ/mol'), E0=(94.5754,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.4344593842569866, var=20.789234267912267, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-1O-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-1O-R
    Total Standard Deviation in ln(k): 17.769927173796294"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-1O-R
Total Standard Deviation in ln(k): 17.769927173796294""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-1O-R
Total Standard Deviation in ln(k): 17.769927173796294
""",
)

entry(
    index = 21,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-1O-R_5R!H->C",
    kinetics = ArrheniusBM(A=(8.19658e-06,'m^3/(mol*s)'), n=3.30549, w0=(353.5,'kJ/mol'), E0=(97.8302,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-1O-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-1O-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-1O-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-1O-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-1O-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.000113357,'m^3/(mol*s)'), n=2.96608, w0=(353.5,'kJ/mol'), E0=(145.229,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-1O-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-1O-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-1O-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-1O-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.85918e-06,'m^3/(mol*s)'), n=3.7472, w0=(353.5,'kJ/mol'), E0=(136.628,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(0.184145,'m^3/(mol*s)'), n=2.18985, w0=(353.5,'kJ/mol'), E0=(110.77,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08820292288400683, var=4.909102350649991, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl',), comment="""BM rule fitted to 18 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 4.663405494845206"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 4.663405494845206""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 4.663405494845206
""",
)

entry(
    index = 25,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(1.96983e-05,'m^3/(mol*s)'), n=3.06567, w0=(353.5,'kJ/mol'), E0=(92.6104,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3282919348092075, var=0.8962507455908166, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R',), comment="""BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 2.7227472404171533"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 2.7227472404171533""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 2.7227472404171533
""",
)

entry(
    index = 26,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C",
    kinetics = ArrheniusBM(A=(2.85655e-06,'m^3/(mol*s)'), n=3.30334, w0=(353.5,'kJ/mol'), E0=(87.7061,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6677092281828253, var=1.1802321507316156, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C
    Total Standard Deviation in ln(k): 3.8555752937254413"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 3.8555752937254413""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 3.8555752937254413
""",
)

entry(
    index = 27,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(6.82694e-06,'m^3/(mol*s)'), n=3.64173, w0=(353.5,'kJ/mol'), E0=(115.011,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C_Ext-1O-R",
    kinetics = ArrheniusBM(A=(3.91335e-06,'m^3/(mol*s)'), n=3.26013, w0=(353.5,'kJ/mol'), E0=(88.124,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3466455443082337, var=0.000464509830570196, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C_Ext-1O-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C_Ext-1O-R
    Total Standard Deviation in ln(k): 0.9141757372499842"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C_Ext-1O-R
Total Standard Deviation in ln(k): 0.9141757372499842""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C_Ext-1O-R
Total Standard Deviation in ln(k): 0.9141757372499842
""",
)

entry(
    index = 29,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C_Ext-1O-R_6R!H->C",
    kinetics = ArrheniusBM(A=(3.20903e-06,'m^3/(mol*s)'), n=3.28294, w0=(353.5,'kJ/mol'), E0=(87.4365,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C_Ext-1O-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C_Ext-1O-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C_Ext-1O-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C_Ext-1O-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 30,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C_Ext-1O-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(4.15666e-05,'m^3/(mol*s)'), n=3.33404, w0=(353.5,'kJ/mol'), E0=(133.59,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C_Ext-1O-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C_Ext-1O-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C_Ext-1O-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C_Ext-1O-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_N-Sp-4BrCFINOPSSi-3C",
    kinetics = ArrheniusBM(A=(1.71908e-05,'m^3/(mol*s)'), n=3.59799, w0=(353.5,'kJ/mol'), E0=(149.845,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_N-Sp-4BrCFINOPSSi-3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_N-Sp-4BrCFINOPSSi-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_N-Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_N-Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 32,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C",
    kinetics = ArrheniusBM(A=(0.00125927,'m^3/(mol*s)'), n=2.98925, w0=(353.5,'kJ/mol'), E0=(170.525,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C",
    kinetics = ArrheniusBM(A=(0.00208458,'m^3/(mol*s)'), n=2.80032, w0=(353.5,'kJ/mol'), E0=(101.83,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.14097594266740635, var=5.463499622854724, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C',), comment="""BM rule fitted to 12 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C
    Total Standard Deviation in ln(k): 5.040104781399489"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C
Total Standard Deviation in ln(k): 5.040104781399489""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C
Total Standard Deviation in ln(k): 5.040104781399489
""",
)

entry(
    index = 34,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0",
    kinetics = ArrheniusBM(A=(2.67762e-07,'m^3/(mol*s)'), n=3.93389, w0=(353.5,'kJ/mol'), E0=(71.8218,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.006200402315360351, var=7.302363286141221, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0',), comment="""BM rule fitted to 10 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0
    Total Standard Deviation in ln(k): 5.4329515007138545"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0
Total Standard Deviation in ln(k): 5.4329515007138545""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0
Total Standard Deviation in ln(k): 5.4329515007138545
""",
)

entry(
    index = 35,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R",
    kinetics = ArrheniusBM(A=(5.46298e-05,'m^3/(mol*s)'), n=3.30978, w0=(353.5,'kJ/mol'), E0=(60.1665,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.01834998655489695, var=14.269700153953282, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R',), comment="""BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R
    Total Standard Deviation in ln(k): 7.619043701358297"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R
Total Standard Deviation in ln(k): 7.619043701358297""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R
Total Standard Deviation in ln(k): 7.619043701358297
""",
)

entry(
    index = 36,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.000936334,'m^3/(mol*s)'), n=3.09886, w0=(353.5,'kJ/mol'), E0=(69.9735,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_Sp-4BrBrCCFFIINNOOPPSSSiSi=3C",
    kinetics = ArrheniusBM(A=(8.67316e-13,'m^3/(mol*s)'), n=5.55792, w0=(353.5,'kJ/mol'), E0=(72.2556,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.14554147039424228, var=3.371400630987773, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_Sp-4BrBrCCFFIINNOOPPSSSiSi=3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_Sp-4BrBrCCFFIINNOOPPSSSiSi=3C
    Total Standard Deviation in ln(k): 4.046651182408618"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_Sp-4BrBrCCFFIINNOOPPSSSiSi=3C
Total Standard Deviation in ln(k): 4.046651182408618""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_Sp-4BrBrCCFFIINNOOPPSSSiSi=3C
Total Standard Deviation in ln(k): 4.046651182408618
""",
)

entry(
    index = 38,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_Sp-4BrBrCCFFIINNOOPPSSSiSi=3C_Ext-1O-R",
    kinetics = ArrheniusBM(A=(0.000112955,'m^3/(mol*s)'), n=3.18792, w0=(353.5,'kJ/mol'), E0=(135.135,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_Sp-4BrBrCCFFIINNOOPPSSSiSi=3C_Ext-1O-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_Sp-4BrBrCCFFIINNOOPPSSSiSi=3C_Ext-1O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_Sp-4BrBrCCFFIINNOOPPSSSiSi=3C_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_Sp-4BrBrCCFFIINNOOPPSSSiSi=3C_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=3C",
    kinetics = ArrheniusBM(A=(3.88036e-06,'m^3/(mol*s)'), n=3.49681, w0=(353.5,'kJ/mol'), E0=(46.9331,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.809042203981164, var=5.7832687001273895, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=3C
    Total Standard Deviation in ln(k): 9.366404807314144"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=3C
Total Standard Deviation in ln(k): 9.366404807314144""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=3C
Total Standard Deviation in ln(k): 9.366404807314144
""",
)

entry(
    index = 40,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=3C_Ext-1O-R",
    kinetics = ArrheniusBM(A=(4.11983e-05,'m^3/(mol*s)'), n=3.20075, w0=(353.5,'kJ/mol'), E0=(86.8192,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=3C_Ext-1O-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=3C_Ext-1O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=3C_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=3C_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Sp-4BrCFINOPSSi-3C",
    kinetics = ArrheniusBM(A=(1.19882e-05,'m^3/(mol*s)'), n=3.2873, w0=(353.5,'kJ/mol'), E0=(92.8172,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.1068381499396294, var=2.260734454322776, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Sp-4BrCFINOPSSi-3C',), comment="""BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Sp-4BrCFINOPSSi-3C
    Total Standard Deviation in ln(k): 5.7952677032249325"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 5.7952677032249325""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 5.7952677032249325
""",
)

entry(
    index = 42,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Sp-4BrCFINOPSSi-3C_4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(8.55138e-06,'m^3/(mol*s)'), n=3.32769, w0=(353.5,'kJ/mol'), E0=(92.0775,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7886227433216854, var=0.4072789299386702, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Sp-4BrCFINOPSSi-3C_4BrCFINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Sp-4BrCFINOPSSi-3C_4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 3.2608542058752206"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Sp-4BrCFINOPSSi-3C_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 3.2608542058752206""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Sp-4BrCFINOPSSi-3C_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 3.2608542058752206
""",
)

entry(
    index = 43,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Sp-4BrCFINOPSSi-3C_4BrCFINOPSSi->C_Ext-1O-R",
    kinetics = ArrheniusBM(A=(6.07292e-05,'m^3/(mol*s)'), n=3.31932, w0=(353.5,'kJ/mol'), E0=(127.425,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Sp-4BrCFINOPSSi-3C_4BrCFINOPSSi->C_Ext-1O-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Sp-4BrCFINOPSSi-3C_4BrCFINOPSSi->C_Ext-1O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Sp-4BrCFINOPSSi-3C_4BrCFINOPSSi->C_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Sp-4BrCFINOPSSi-3C_4BrCFINOPSSi->C_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 44,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(9.78815e-05,'m^3/(mol*s)'), n=3.35062, w0=(353.5,'kJ/mol'), E0=(106.222,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 45,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_N-Sp-4BrCFINOPSSi-3C",
    kinetics = ArrheniusBM(A=(9.41439e-06,'m^3/(mol*s)'), n=3.58394, w0=(353.5,'kJ/mol'), E0=(103.023,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.1148142905507914, var=7.1521935561015795, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_N-Sp-4BrCFINOPSSi-3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_N-Sp-4BrCFINOPSSi-3C
    Total Standard Deviation in ln(k): 10.67498410313912"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_N-Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 10.67498410313912""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_N-Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 10.67498410313912
""",
)

entry(
    index = 46,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_N-Sp-4BrCFINOPSSi-3C_Ext-1O-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2.82278e-05,'m^3/(mol*s)'), n=3.44719, w0=(353.5,'kJ/mol'), E0=(105.453,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_N-Sp-4BrCFINOPSSi-3C_Ext-1O-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_N-Sp-4BrCFINOPSSi-3C_Ext-1O-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_N-Sp-4BrCFINOPSSi-3C_Ext-1O-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_N-Sp-4BrCFINOPSSi-3C_Ext-1O-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 47,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_N-Sp-4BrCFINOPSSi-3C_Ext-1O-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.000790872,'m^3/(mol*s)'), n=3.05486, w0=(353.5,'kJ/mol'), E0=(146.738,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_N-Sp-4BrCFINOPSSi-3C_Ext-1O-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_N-Sp-4BrCFINOPSSi-3C_Ext-1O-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_N-Sp-4BrCFINOPSSi-3C_Ext-1O-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_N-Sp-4BrCFINOPSSi-3C_Ext-1O-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 48,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-1O-u0",
    kinetics = ArrheniusBM(A=(0.0004321,'m^3/(mol*s)'), n=2.92722, w0=(353.5,'kJ/mol'), E0=(110.312,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.305469772945159, var=2.6237153674356675, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-1O-u0',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-1O-u0
    Total Standard Deviation in ln(k): 6.5273219908966125"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-1O-u0
Total Standard Deviation in ln(k): 6.5273219908966125""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-1O-u0
Total Standard Deviation in ln(k): 6.5273219908966125
""",
)

entry(
    index = 49,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-1O-u0_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.0885587,'m^3/(mol*s)'), n=2.37138, w0=(353.5,'kJ/mol'), E0=(143.762,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-1O-u0_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-1O-u0_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-1O-u0_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-1O-u0_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 50,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-1O-R_4R!H->C",
    kinetics = ArrheniusBM(A=(0.000476496,'m^3/(mol*s)'), n=3.27616, w0=(353.5,'kJ/mol'), E0=(124.789,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-1O-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-1O-R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-1O-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-1O-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 51,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-1O-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.000849095,'m^3/(mol*s)'), n=3.17369, w0=(353.5,'kJ/mol'), E0=(116.985,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-1O-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-1O-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-1O-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-1O-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 52,
    label = "Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1",
    kinetics = ArrheniusBM(A=(1.2872e+10,'m^3/(mol*s)'), n=-0.773833, w0=(353.5,'kJ/mol'), E0=(177.134,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7972196490543438, var=3.4097701400792344, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1',), comment="""BM rule fitted to 12 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1
    Total Standard Deviation in ln(k): 5.704920616116375"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1
Total Standard Deviation in ln(k): 5.704920616116375""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1
Total Standard Deviation in ln(k): 5.704920616116375
""",
)

entry(
    index = 53,
    label = "Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0",
    kinetics = ArrheniusBM(A=(1.25129e-06,'m^3/(mol*s)'), n=3.81647, w0=(353.5,'kJ/mol'), E0=(61.5736,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.018379550589406646, var=1.1388081239476364, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0',), comment="""BM rule fitted to 10 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0
    Total Standard Deviation in ln(k): 2.185531875257019"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0
Total Standard Deviation in ln(k): 2.185531875257019""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0
Total Standard Deviation in ln(k): 2.185531875257019
""",
)

entry(
    index = 54,
    label = "Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.00838263,'m^3/(mol*s)'), n=2.66116, w0=(353.5,'kJ/mol'), E0=(99.7018,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9756788214757182, var=10.558907788587243, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R',), comment="""BM rule fitted to 8 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R
    Total Standard Deviation in ln(k): 8.965735319983068"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R
Total Standard Deviation in ln(k): 8.965735319983068""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R
Total Standard Deviation in ln(k): 8.965735319983068
""",
)

entry(
    index = 55,
    label = "Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_Ext-1O-R",
    kinetics = ArrheniusBM(A=(18.8956,'m^3/(mol*s)'), n=1.60508, w0=(353.5,'kJ/mol'), E0=(90.0369,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2923320915469164, var=99.25880065962046, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_Ext-1O-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_Ext-1O-R
    Total Standard Deviation in ln(k): 20.707419918810718"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_Ext-1O-R
Total Standard Deviation in ln(k): 20.707419918810718""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_Ext-1O-R
Total Standard Deviation in ln(k): 20.707419918810718
""",
)

entry(
    index = 56,
    label = "Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(0.000262991,'m^3/(mol*s)'), n=3.09197, w0=(353.5,'kJ/mol'), E0=(58.5292,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.5775386942012597, var=21.447494026520534, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_Sp-4R!H-3C',), comment="""BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_Sp-4R!H-3C
    Total Standard Deviation in ln(k): 15.760444543824173"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_Sp-4R!H-3C
Total Standard Deviation in ln(k): 15.760444543824173""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_Sp-4R!H-3C
Total Standard Deviation in ln(k): 15.760444543824173
""",
)

entry(
    index = 57,
    label = "Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_Sp-4R!H-3C_4R!H->C",
    kinetics = ArrheniusBM(A=(0.000233563,'m^3/(mol*s)'), n=3.10455, w0=(353.5,'kJ/mol'), E0=(77.2281,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.727751754084225, var=14.959639222643405, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_Sp-4R!H-3C_4R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_Sp-4R!H-3C_4R!H->C
    Total Standard Deviation in ln(k): 12.094937561150282"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_Sp-4R!H-3C_4R!H->C
Total Standard Deviation in ln(k): 12.094937561150282""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_Sp-4R!H-3C_4R!H->C
Total Standard Deviation in ln(k): 12.094937561150282
""",
)

entry(
    index = 58,
    label = "Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(33.2685,'m^3/(mol*s)'), n=1.84743, w0=(353.5,'kJ/mol'), E0=(69.5384,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6803431805801812, var=124.74920786810922, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C
    Total Standard Deviation in ln(k): 24.100528599000715"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C
Total Standard Deviation in ln(k): 24.100528599000715""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C
Total Standard Deviation in ln(k): 24.100528599000715
""",
)

entry(
    index = 59,
    label = "Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_N-Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(8.02782e-05,'m^3/(mol*s)'), n=3.4195, w0=(353.5,'kJ/mol'), E0=(134.987,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_N-Sp-4R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_N-Sp-4R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 60,
    label = "Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-1O-R",
    kinetics = ArrheniusBM(A=(0.000178698,'m^3/(mol*s)'), n=3.25898, w0=(353.5,'kJ/mol'), E0=(116.028,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-1O-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-1O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 61,
    label = "Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_N-1O-u0",
    kinetics = ArrheniusBM(A=(0.00120383,'m^3/(mol*s)'), n=2.95399, w0=(353.5,'kJ/mol'), E0=(144.09,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.212597924115824, var=3.1815071461962323, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_N-1O-u0',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_N-1O-u0
    Total Standard Deviation in ln(k): 6.622530271374461"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_N-1O-u0
Total Standard Deviation in ln(k): 6.622530271374461""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_N-1O-u0
Total Standard Deviation in ln(k): 6.622530271374461
""",
)

entry(
    index = 62,
    label = "Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_N-1O-u0_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.0391196,'m^3/(mol*s)'), n=2.49957, w0=(353.5,'kJ/mol'), E0=(133.435,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_N-1O-u0_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_N-1O-u0_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_N-1O-u0_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_N-1O-u0_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 63,
    label = "Root_1R->O_N-3R->O_N-3CClFH->C",
    kinetics = ArrheniusBM(A=(1.04105,'m^3/(mol*s)'), n=2.3137, w0=(393.5,'kJ/mol'), E0=(120.296,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-3CClFH->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-3CClFH->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-3CClFH->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-3CClFH->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 64,
    label = "Root_N-1R->O",
    kinetics = ArrheniusBM(A=(2.04976e+25,'m^3/(mol*s)'), n=-5.15394, w0=(446.63,'kJ/mol'), E0=(240.931,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8929179071008335, var=12.735234451858659, Tref=1000.0, N=135, data_mean=0.0, correlation='Root_N-1R->O',), comment="""BM rule fitted to 135 training reactions at node Root_N-1R->O
    Total Standard Deviation in ln(k): 9.39770219455072"""),
    rank = 11,
    shortDesc = """BM rule fitted to 135 training reactions at node Root_N-1R->O
Total Standard Deviation in ln(k): 9.39770219455072""",
    longDesc = 
"""
BM rule fitted to 135 training reactions at node Root_N-1R->O
Total Standard Deviation in ln(k): 9.39770219455072
""",
)

entry(
    index = 65,
    label = "Root_N-1R->O_3R->O",
    kinetics = ArrheniusBM(A=(3.80551e-08,'m^3/(mol*s)'), n=4.41611, w0=(354.581,'kJ/mol'), E0=(71.8218,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1415735749628427, var=5.3808360702246185, Tref=1000.0, N=37, data_mean=0.0, correlation='Root_N-1R->O_3R->O',), comment="""BM rule fitted to 37 training reactions at node Root_N-1R->O_3R->O
    Total Standard Deviation in ln(k): 5.006022126732392"""),
    rank = 11,
    shortDesc = """BM rule fitted to 37 training reactions at node Root_N-1R->O_3R->O
Total Standard Deviation in ln(k): 5.006022126732392""",
    longDesc = 
"""
BM rule fitted to 37 training reactions at node Root_N-1R->O_3R->O
Total Standard Deviation in ln(k): 5.006022126732392
""",
)

entry(
    index = 66,
    label = "Root_N-1R->O_3R->O_Ext-3O-R",
    kinetics = ArrheniusBM(A=(4.26335e-08,'m^3/(mol*s)'), n=4.35076, w0=(356.167,'kJ/mol'), E0=(79.8808,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5019050136197111, var=2.386075406136041, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R',), comment="""BM rule fitted to 15 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R
    Total Standard Deviation in ln(k): 4.3577674277008285"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R
Total Standard Deviation in ln(k): 4.3577674277008285""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R
Total Standard Deviation in ln(k): 4.3577674277008285
""",
)

entry(
    index = 67,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C",
    kinetics = ArrheniusBM(A=(1.48072e-08,'m^3/(mol*s)'), n=4.46826, w0=(361.5,'kJ/mol'), E0=(74.1022,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.13445739142018667, var=3.8035815028286235, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C
    Total Standard Deviation in ln(k): 4.247621933066213"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C
Total Standard Deviation in ln(k): 4.247621933066213""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C
Total Standard Deviation in ln(k): 4.247621933066213
""",
)

entry(
    index = 68,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C",
    kinetics = ArrheniusBM(A=(0.00414587,'m^3/(mol*s)'), n=2.9695, w0=(353.5,'kJ/mol'), E0=(106.565,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5582301686001242, var=4.893950951569668, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C
    Total Standard Deviation in ln(k): 5.837518631023724"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C
Total Standard Deviation in ln(k): 5.837518631023724""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C
Total Standard Deviation in ln(k): 5.837518631023724
""",
)

entry(
    index = 69,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.00420594,'m^3/(mol*s)'), n=2.96721, w0=(353.5,'kJ/mol'), E0=(106.539,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.557856083311104, var=4.918947708206529, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R
    Total Standard Deviation in ln(k): 5.8478904044427225"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 5.8478904044427225""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 5.8478904044427225
""",
)

entry(
    index = 70,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_Sp-5R!H-1C",
    kinetics = ArrheniusBM(A=(8.77906e-10,'m^3/(mol*s)'), n=4.81153, w0=(353.5,'kJ/mol'), E0=(61.6807,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.19863436636952303, var=11.136254828357407, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_Sp-5R!H-1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_Sp-5R!H-1C
    Total Standard Deviation in ln(k): 7.189088281643699"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_Sp-5R!H-1C
Total Standard Deviation in ln(k): 7.189088281643699""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_Sp-5R!H-1C
Total Standard Deviation in ln(k): 7.189088281643699
""",
)

entry(
    index = 71,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C",
    kinetics = ArrheniusBM(A=(3.4028e-05,'m^3/(mol*s)'), n=3.2958, w0=(353.5,'kJ/mol'), E0=(88.8337,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 72,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_Sp-5R!H-1C_N-5R!H->C",
    kinetics = ArrheniusBM(A=(3.72654e-05,'m^3/(mol*s)'), n=3.68668, w0=(353.5,'kJ/mol'), E0=(97.9939,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_Sp-5R!H-1C_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_Sp-5R!H-1C_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_Sp-5R!H-1C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_Sp-5R!H-1C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 73,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-Sp-5R!H-1C",
    kinetics = ArrheniusBM(A=(7.11715e-05,'m^3/(mol*s)'), n=3.61421, w0=(353.5,'kJ/mol'), E0=(106.107,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-Sp-5R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-Sp-5R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-Sp-5R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-Sp-5R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 74,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_N-1BrCClFHINPSSi->C",
    kinetics = ArrheniusBM(A=(0.00559699,'m^3/(mol*s)'), n=2.68417, w0=(393.5,'kJ/mol'), E0=(120.266,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_N-1BrCClFHINPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_N-1BrCClFHINPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_N-1BrCClFHINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_N-1BrCClFHINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 75,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(5.01835e-08,'m^3/(mol*s)'), n=4.35812, w0=(353.5,'kJ/mol'), E0=(49.9882,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.49289784210241994, var=10.558994129307393, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C
    Total Standard Deviation in ln(k): 7.752744417616504"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C
Total Standard Deviation in ln(k): 7.752744417616504""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C
Total Standard Deviation in ln(k): 7.752744417616504
""",
)

entry(
    index = 76,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0",
    kinetics = ArrheniusBM(A=(3.90963e-05,'m^3/(mol*s)'), n=3.5792, w0=(353.5,'kJ/mol'), E0=(76.3721,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.7547778792799171, var=4.586286055995305, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0
    Total Standard Deviation in ln(k): 8.70225329203014"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0
Total Standard Deviation in ln(k): 8.70225329203014""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0
Total Standard Deviation in ln(k): 8.70225329203014
""",
)

entry(
    index = 77,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(4.27957e-05,'m^3/(mol*s)'), n=3.56649, w0=(353.5,'kJ/mol'), E0=(75.9533,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.018256005432997, var=6.261923581477752, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 10.087611128455896"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 10.087611128455896""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 10.087611128455896
""",
)

entry(
    index = 78,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi",
    kinetics = ArrheniusBM(A=(6.29907e-05,'m^3/(mol*s)'), n=3.67452, w0=(353.5,'kJ/mol'), E0=(139.097,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3876171256366787, var=0.06117677813487636, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi
    Total Standard Deviation in ln(k): 1.4697623445086552"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi
Total Standard Deviation in ln(k): 1.4697623445086552""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi
Total Standard Deviation in ln(k): 1.4697623445086552
""",
)

entry(
    index = 79,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(8.38302e-05,'m^3/(mol*s)'), n=3.60203, w0=(353.5,'kJ/mol'), E0=(132.965,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 80,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi",
    kinetics = ArrheniusBM(A=(0.00298854,'m^3/(mol*s)'), n=3.03657, w0=(353.5,'kJ/mol'), E0=(93.2735,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.0269741027807475, var=7.418839710711403, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi
    Total Standard Deviation in ln(k): 10.55330636157575"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi
Total Standard Deviation in ln(k): 10.55330636157575""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi
Total Standard Deviation in ln(k): 10.55330636157575
""",
)

entry(
    index = 81,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(5.69582e-06,'m^3/(mol*s)'), n=3.94767, w0=(353.5,'kJ/mol'), E0=(131.362,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 82,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(0.000489073,'m^3/(mol*s)'), n=3.26418, w0=(353.5,'kJ/mol'), E0=(86.2799,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 83,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_5R!H->C",
    kinetics = ArrheniusBM(A=(5.27349e-06,'m^3/(mol*s)'), n=3.9638, w0=(353.5,'kJ/mol'), E0=(124.929,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 84,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-5R!H->C",
    kinetics = ArrheniusBM(A=(6.65995e-06,'m^3/(mol*s)'), n=3.94804, w0=(353.5,'kJ/mol'), E0=(142.404,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 85,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_N-1BrCClFHINPSSi-u0",
    kinetics = ArrheniusBM(A=(3.19798e-06,'m^3/(mol*s)'), n=3.79061, w0=(353.5,'kJ/mol'), E0=(117.34,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.8343586838860735, var=15.827979991137536, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_N-1BrCClFHINPSSi-u0',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_N-1BrCClFHINPSSi-u0
    Total Standard Deviation in ln(k): 12.584658418049097"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_N-1BrCClFHINPSSi-u0
Total Standard Deviation in ln(k): 12.584658418049097""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_N-1BrCClFHINPSSi-u0
Total Standard Deviation in ln(k): 12.584658418049097
""",
)

entry(
    index = 86,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(1.97238e+12,'m^3/(mol*s)'), n=-1.37822, w0=(353.5,'kJ/mol'), E0=(162.229,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3417426124845085, var=80.91653487076931, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 18.89196722116006"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 18.89196722116006""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 18.89196722116006
""",
)

entry(
    index = 87,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0",
    kinetics = ArrheniusBM(A=(1.27879e+09,'m^3/(mol*s)'), n=-0.172985, w0=(353.5,'kJ/mol'), E0=(133.985,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5419981305254513, var=19.20222985649864, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0
    Total Standard Deviation in ln(k): 10.146623420546181"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0
Total Standard Deviation in ln(k): 10.146623420546181""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0
Total Standard Deviation in ln(k): 10.146623420546181
""",
)

entry(
    index = 88,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi",
    kinetics = ArrheniusBM(A=(1.72013,'m^3/(mol*s)'), n=2.4493, w0=(353.5,'kJ/mol'), E0=(172.869,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi
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
    index = 89,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi",
    kinetics = ArrheniusBM(A=(2.14517e+09,'m^3/(mol*s)'), n=-0.237488, w0=(353.5,'kJ/mol'), E0=(134.659,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5547333848356208, var=19.214123515129643, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi
    Total Standard Deviation in ln(k): 10.181341737940746"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi
Total Standard Deviation in ln(k): 10.181341737940746""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi
Total Standard Deviation in ln(k): 10.181341737940746
""",
)

entry(
    index = 90,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi",
    kinetics = ArrheniusBM(A=(7.69001e+12,'m^3/(mol*s)'), n=-1.14562, w0=(353.5,'kJ/mol'), E0=(186.49,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8368870482345636, var=3.2730959814269527, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi
    Total Standard Deviation in ln(k): 5.729637777395152"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi
Total Standard Deviation in ln(k): 5.729637777395152""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi
Total Standard Deviation in ln(k): 5.729637777395152
""",
)

entry(
    index = 91,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(0.709262,'m^3/(mol*s)'), n=2.59771, w0=(353.5,'kJ/mol'), E0=(133.981,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3994448278825658, var=0.001810456791872707, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 1.088930621581972"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 1.088930621581972""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 1.088930621581972
""",
)

entry(
    index = 92,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_3O-u1",
    kinetics = ArrheniusBM(A=(0.0379121,'m^3/(mol*s)'), n=2.90824, w0=(353.5,'kJ/mol'), E0=(123.471,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_3O-u1
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
    index = 93,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-3O-u1",
    kinetics = ArrheniusBM(A=(7.30096,'m^3/(mol*s)'), n=2.36151, w0=(353.5,'kJ/mol'), E0=(142.537,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-3O-u1
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
    index = 94,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi",
    kinetics = ArrheniusBM(A=(1.91866e+09,'m^3/(mol*s)'), n=-0.22416, w0=(353.5,'kJ/mol'), E0=(134.274,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5561655269508002, var=19.506555581096332, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi
    Total Standard Deviation in ln(k): 10.251559159888204"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi
Total Standard Deviation in ln(k): 10.251559159888204""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi
Total Standard Deviation in ln(k): 10.251559159888204
""",
)

entry(
    index = 95,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(204137,'m^3/(mol*s)'), n=1.12839, w0=(353.5,'kJ/mol'), E0=(89.7782,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.315611773296122, var=48.06414051297562, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 22.22917159254709"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 22.22917159254709""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 22.22917159254709
""",
)

entry(
    index = 96,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_4R!H->C",
    kinetics = ArrheniusBM(A=(868.266,'m^3/(mol*s)'), n=1.80878, w0=(353.5,'kJ/mol'), E0=(72.9631,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.709181372947351, var=12.715949468380543, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_4R!H->C
    Total Standard Deviation in ln(k): 11.443196573202227"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_4R!H->C
Total Standard Deviation in ln(k): 11.443196573202227""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_4R!H->C
Total Standard Deviation in ln(k): 11.443196573202227
""",
)

entry(
    index = 97,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_4R!H->C_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(174.781,'m^3/(mol*s)'), n=2.00798, w0=(353.5,'kJ/mol'), E0=(70.4627,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_4R!H->C_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_4R!H->C_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_4R!H->C_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_4R!H->C_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 98,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.0308105,'m^3/(mol*s)'), n=2.88761, w0=(353.5,'kJ/mol'), E0=(139.029,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 99,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(0.00183121,'m^3/(mol*s)'), n=3.20884, w0=(353.5,'kJ/mol'), E0=(116.38,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.21486815454720393, var=0.04166175982287194, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-4R!H-R
    Total Standard Deviation in ln(k): 0.9490604729841041"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.9490604729841041""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.9490604729841041
""",
)

entry(
    index = 100,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-4R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(0.00185843,'m^3/(mol*s)'), n=3.22261, w0=(353.5,'kJ/mol'), E0=(116.907,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-4R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-4R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 101,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1",
    kinetics = ArrheniusBM(A=(0.00455417,'m^3/(mol*s)'), n=2.86622, w0=(353.5,'kJ/mol'), E0=(95.5591,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7153323030651046, var=1.1377856582155192, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1
    Total Standard Deviation in ln(k): 3.9357088323271516"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1
Total Standard Deviation in ln(k): 3.9357088323271516""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1
Total Standard Deviation in ln(k): 3.9357088323271516
""",
)

entry(
    index = 102,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1_4R!H->Cl",
    kinetics = ArrheniusBM(A=(0.00381903,'m^3/(mol*s)'), n=3.24993, w0=(353.5,'kJ/mol'), E0=(134.971,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1_4R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1_4R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 103,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(0.00395332,'m^3/(mol*s)'), n=2.88198, w0=(353.5,'kJ/mol'), E0=(95.0284,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.600353008259089, var=4.563719678772933, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1_N-4R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1_N-4R!H->Cl
    Total Standard Deviation in ln(k): 8.30367578439722"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1_N-4R!H->Cl
Total Standard Deviation in ln(k): 8.30367578439722""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1_N-4R!H->Cl
Total Standard Deviation in ln(k): 8.30367578439722
""",
)

entry(
    index = 104,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1_N-4R!H->Cl_4CO->C",
    kinetics = ArrheniusBM(A=(0.00296033,'m^3/(mol*s)'), n=2.91633, w0=(353.5,'kJ/mol'), E0=(94.3942,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1_N-4R!H->Cl_4CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1_N-4R!H->Cl_4CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1_N-4R!H->Cl_4CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1_N-4R!H->Cl_4CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 105,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1_N-4R!H->Cl_N-4CO->C",
    kinetics = ArrheniusBM(A=(0.00678858,'m^3/(mol*s)'), n=3.1372, w0=(353.5,'kJ/mol'), E0=(107.934,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1_N-4R!H->Cl_N-4CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1_N-4R!H->Cl_N-4CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1_N-4R!H->Cl_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1_N-4R!H->Cl_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 106,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-3O-u1",
    kinetics = ArrheniusBM(A=(0.00124093,'m^3/(mol*s)'), n=3.29463, w0=(353.5,'kJ/mol'), E0=(108.493,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 107,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0",
    kinetics = ArrheniusBM(A=(4.12747e+12,'m^3/(mol*s)'), n=-1.38399, w0=(353.5,'kJ/mol'), E0=(181.994,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.2444427030870497, var=12.341693633103706, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0
    Total Standard Deviation in ln(k): 10.169524479361078"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0
Total Standard Deviation in ln(k): 10.169524479361078""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0
Total Standard Deviation in ln(k): 10.169524479361078
""",
)

entry(
    index = 108,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1",
    kinetics = ArrheniusBM(A=(0.0537303,'m^3/(mol*s)'), n=2.51468, w0=(353.5,'kJ/mol'), E0=(71.5883,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.04063663748776, var=14.360607629457062, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1
    Total Standard Deviation in ln(k): 15.236812782210666"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1
Total Standard Deviation in ln(k): 15.236812782210666""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1
Total Standard Deviation in ln(k): 15.236812782210666
""",
)

entry(
    index = 109,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(0.0611577,'m^3/(mol*s)'), n=2.49737, w0=(353.5,'kJ/mol'), E0=(51.6334,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.215850928838523, var=17.351345736798574, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 16.430740712811303"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 16.430740712811303""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 16.430740712811303
""",
)

entry(
    index = 110,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi",
    kinetics = ArrheniusBM(A=(0.0672976,'m^3/(mol*s)'), n=2.48404, w0=(353.5,'kJ/mol'), E0=(51.0325,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=4.441834136874406, var=29.003076537156954, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi
    Total Standard Deviation in ln(k): 21.956788700982226"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi
Total Standard Deviation in ln(k): 21.956788700982226""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi
Total Standard Deviation in ln(k): 21.956788700982226
""",
)

entry(
    index = 111,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->C",
    kinetics = ArrheniusBM(A=(0.0599062,'m^3/(mol*s)'), n=2.49716, w0=(353.5,'kJ/mol'), E0=(34.1366,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=4.538316137886706, var=28.369833362749432, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->C
    Total Standard Deviation in ln(k): 22.080692873008232"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->C
Total Standard Deviation in ln(k): 22.080692873008232""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->C
Total Standard Deviation in ln(k): 22.080692873008232
""",
)

entry(
    index = 112,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->C",
    kinetics = ArrheniusBM(A=(3.60039e+26,'m^3/(mol*s)'), n=-5.32572, w0=(353.5,'kJ/mol'), E0=(189.77,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.41285490692586807, var=71.88348310735326, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->C
    Total Standard Deviation in ln(k): 18.03429536844057"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->C
Total Standard Deviation in ln(k): 18.03429536844057""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->C
Total Standard Deviation in ln(k): 18.03429536844057
""",
)

entry(
    index = 113,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H-1BrCClFHINPSSi",
    kinetics = ArrheniusBM(A=(0.0387235,'m^3/(mol*s)'), n=2.8378, w0=(353.5,'kJ/mol'), E0=(137.811,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H-1BrCClFHINPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H-1BrCClFHINPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H-1BrCClFHINPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H-1BrCClFHINPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 114,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_N-3O-u1",
    kinetics = ArrheniusBM(A=(0.000311441,'m^3/(mol*s)'), n=3.31701, w0=(353.5,'kJ/mol'), E0=(142.443,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.194305989030055, var=17.390725702868696, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_N-3O-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_N-3O-u1
    Total Standard Deviation in ln(k): 16.386078560999987"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_N-3O-u1
Total Standard Deviation in ln(k): 16.386078560999987""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_N-3O-u1
Total Standard Deviation in ln(k): 16.386078560999987
""",
)

entry(
    index = 115,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_N-3O-u1_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(1.32859,'m^3/(mol*s)'), n=2.43214, w0=(353.5,'kJ/mol'), E0=(131.98,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_N-3O-u1_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_N-3O-u1_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_N-3O-u1_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_N-3O-u1_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 116,
    label = "Root_N-1R->O_N-3R->O",
    kinetics = ArrheniusBM(A=(2.74884e+12,'m^3/(mol*s)'), n=-1.49736, w0=(481.383,'kJ/mol'), E0=(213.299,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.559756750902315, var=9.511574986271984, Tref=1000.0, N=98, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O',), comment="""BM rule fitted to 98 training reactions at node Root_N-1R->O_N-3R->O
    Total Standard Deviation in ln(k): 7.589195655528512"""),
    rank = 11,
    shortDesc = """BM rule fitted to 98 training reactions at node Root_N-1R->O_N-3R->O
Total Standard Deviation in ln(k): 7.589195655528512""",
    longDesc = 
"""
BM rule fitted to 98 training reactions at node Root_N-1R->O_N-3R->O
Total Standard Deviation in ln(k): 7.589195655528512
""",
)

entry(
    index = 117,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F",
    kinetics = ArrheniusBM(A=(1.01434e+08,'m^3/(mol*s)'), n=-0.225594, w0=(330,'kJ/mol'), E0=(137.536,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.44504738936828797, var=3.960573696896842, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F
    Total Standard Deviation in ln(k): 5.107870920112682"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F
Total Standard Deviation in ln(k): 5.107870920112682""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F
Total Standard Deviation in ln(k): 5.107870920112682
""",
)

entry(
    index = 118,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(0.00111678,'m^3/(mol*s)'), n=2.91751, w0=(320,'kJ/mol'), E0=(85.3496,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.34968871769075294, var=0.1040544835549546, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_Ext-3CClFH-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 1.5252918291554425"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_Ext-3CClFH-R
Total Standard Deviation in ln(k): 1.5252918291554425""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_Ext-3CClFH-R
Total Standard Deviation in ln(k): 1.5252918291554425
""",
)

entry(
    index = 119,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_Ext-3CClFH-R_4R!H->O",
    kinetics = ArrheniusBM(A=(0.00484543,'m^3/(mol*s)'), n=2.7456, w0=(320,'kJ/mol'), E0=(87.1083,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_Ext-3CClFH-R_4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_Ext-3CClFH-R_4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_Ext-3CClFH-R_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_Ext-3CClFH-R_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 120,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_Ext-3CClFH-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(2.65e+06,'m^3/(mol*s)'), n=1.31135e-09, w0=(320,'kJ/mol'), E0=(118.336,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_Ext-3CClFH-R_N-4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_Ext-3CClFH-R_N-4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_Ext-3CClFH-R_N-4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_Ext-3CClFH-R_N-4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 121,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C",
    kinetics = ArrheniusBM(A=(4e+06,'m^3/(mol*s)'), n=8.51219e-08, w0=(320,'kJ/mol'), E0=(84.6959,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 122,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->C",
    kinetics = ArrheniusBM(A=(29364.5,'m^3/(mol*s)'), n=0.785655, w0=(360,'kJ/mol'), E0=(106.363,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->C
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
    index = 123,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F",
    kinetics = ArrheniusBM(A=(2.5022e+07,'m^3/(mol*s)'), n=-0.0531442, w0=(487.825,'kJ/mol'), E0=(201.884,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4312427228625443, var=9.19311933800675, Tref=1000.0, N=94, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F',), comment="""BM rule fitted to 94 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F
    Total Standard Deviation in ln(k): 7.161912702258527"""),
    rank = 11,
    shortDesc = """BM rule fitted to 94 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F
Total Standard Deviation in ln(k): 7.161912702258527""",
    longDesc = 
"""
BM rule fitted to 94 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F
Total Standard Deviation in ln(k): 7.161912702258527
""",
)

entry(
    index = 124,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H",
    kinetics = ArrheniusBM(A=(0.0044804,'m^3/(mol*s)'), n=3.02314, w0=(516.626,'kJ/mol'), E0=(162.419,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.47550648464061257, var=3.567916297707655, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H',), comment="""BM rule fitted to 14 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H
    Total Standard Deviation in ln(k): 4.981469717488048"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H
Total Standard Deviation in ln(k): 4.981469717488048""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H
Total Standard Deviation in ln(k): 4.981469717488048
""",
)

entry(
    index = 125,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C",
    kinetics = ArrheniusBM(A=(7.8397e-14,'m^3/(mol*s)'), n=6.12719, w0=(525,'kJ/mol'), E0=(138.588,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.28395474012164, var=1.9066537301217197, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C
    Total Standard Deviation in ln(k): 3.4816250479638544"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C
Total Standard Deviation in ln(k): 3.4816250479638544""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C
Total Standard Deviation in ln(k): 3.4816250479638544
""",
)

entry(
    index = 126,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.80295e-14,'m^3/(mol*s)'), n=6.3091, w0=(525,'kJ/mol'), E0=(137.685,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.29701287278626737, var=1.8719290494107745, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R
    Total Standard Deviation in ln(k): 3.489111122606987"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.489111122606987""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.489111122606987
""",
)

entry(
    index = 127,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F",
    kinetics = ArrheniusBM(A=(3.44515e-16,'m^3/(mol*s)'), n=6.79443, w0=(525,'kJ/mol'), E0=(136.427,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.33078718504795296, var=1.1759447643732297, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F
    Total Standard Deviation in ln(k): 3.0050780835384026"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F
Total Standard Deviation in ln(k): 3.0050780835384026""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F
Total Standard Deviation in ln(k): 3.0050780835384026
""",
)

entry(
    index = 128,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R",
    kinetics = ArrheniusBM(A=(8.5754e-12,'m^3/(mol*s)'), n=5.55841, w0=(525,'kJ/mol'), E0=(151.399,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.38425510653032846, var=1.5849298399090912, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R
    Total Standard Deviation in ln(k): 3.4893062034846456"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R
Total Standard Deviation in ln(k): 3.4893062034846456""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R
Total Standard Deviation in ln(k): 3.4893062034846456
""",
)

entry(
    index = 129,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F",
    kinetics = ArrheniusBM(A=(7.37356e-13,'m^3/(mol*s)'), n=5.82445, w0=(525,'kJ/mol'), E0=(150.78,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.40149963774568104, var=0.7309134066492422, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F
    Total Standard Deviation in ln(k): 2.722710718294716"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F
Total Standard Deviation in ln(k): 2.722710718294716""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F
Total Standard Deviation in ln(k): 2.722710718294716
""",
)

entry(
    index = 130,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.13318e-13,'m^3/(mol*s)'), n=5.82954, w0=(525,'kJ/mol'), E0=(151.113,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4404447243854116, var=2.5404741377256483, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R
    Total Standard Deviation in ln(k): 4.301965188712074"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R
Total Standard Deviation in ln(k): 4.301965188712074""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R
Total Standard Deviation in ln(k): 4.301965188712074
""",
)

entry(
    index = 131,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(1.77578e-14,'m^3/(mol*s)'), n=6.28933, w0=(525,'kJ/mol'), E0=(141.992,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 132,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(5.8332e-12,'m^3/(mol*s)'), n=5.5678, w0=(525,'kJ/mol'), E0=(158.471,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 133,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(2.61477e-11,'m^3/(mol*s)'), n=5.47859, w0=(525,'kJ/mol'), E0=(149.555,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3278872133664951, var=4.442464096628965, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F
    Total Standard Deviation in ln(k): 5.049248162379514"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F
Total Standard Deviation in ln(k): 5.049248162379514""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F
Total Standard Deviation in ln(k): 5.049248162379514
""",
)

entry(
    index = 134,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.84865e-10,'m^3/(mol*s)'), n=5.13872, w0=(525,'kJ/mol'), E0=(139.929,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 135,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(2.97102e-12,'m^3/(mol*s)'), n=5.8457, w0=(525,'kJ/mol'), E0=(158.924,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 136,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F",
    kinetics = ArrheniusBM(A=(1.57538e-15,'m^3/(mol*s)'), n=6.62238, w0=(525,'kJ/mol'), E0=(130.61,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.15717456069730484, var=3.156661768269706, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F
    Total Standard Deviation in ln(k): 3.956723135681184"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F
Total Standard Deviation in ln(k): 3.956723135681184""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F
Total Standard Deviation in ln(k): 3.956723135681184
""",
)

entry(
    index = 137,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Ext-1C-R",
    kinetics = ArrheniusBM(A=(4.82674e-21,'m^3/(mol*s)'), n=8.25103, w0=(525,'kJ/mol'), E0=(127.8,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.29068457930038594, var=7.2562105243480435, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Ext-1C-R
    Total Standard Deviation in ln(k): 6.130589154503507"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Ext-1C-R
Total Standard Deviation in ln(k): 6.130589154503507""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Ext-1C-R
Total Standard Deviation in ln(k): 6.130589154503507
""",
)

entry(
    index = 138,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.71142e-12,'m^3/(mol*s)'), n=5.47558, w0=(525,'kJ/mol'), E0=(152.666,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 139,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_4BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(5.18265e-09,'m^3/(mol*s)'), n=4.74784, w0=(525,'kJ/mol'), E0=(136.145,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_4BrCClINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_4BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 140,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-4BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(2.10446e-11,'m^3/(mol*s)'), n=5.39503, w0=(525,'kJ/mol'), E0=(135.401,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.14489781095656265, var=4.445591054253819, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-4BrCClINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-4BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 4.5909626221479565"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 4.5909626221479565""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 4.5909626221479565
""",
)

entry(
    index = 141,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-4BrCClINOPSSi->C_4ClO->O",
    kinetics = ArrheniusBM(A=(3.31829e-08,'m^3/(mol*s)'), n=4.48236, w0=(525,'kJ/mol'), E0=(137.589,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-4BrCClINOPSSi->C_4ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-4BrCClINOPSSi->C_4ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-4BrCClINOPSSi->C_4ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-4BrCClINOPSSi->C_4ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 142,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-4BrCClINOPSSi->C_N-4ClO->O",
    kinetics = ArrheniusBM(A=(3.57367e-11,'m^3/(mol*s)'), n=5.32561, w0=(525,'kJ/mol'), E0=(142.009,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-4BrCClINOPSSi->C_N-4ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-4BrCClINOPSSi->C_N-4ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-4BrCClINOPSSi->C_N-4ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-4BrCClINOPSSi->C_N-4ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 143,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->C",
    kinetics = ArrheniusBM(A=(650.29,'m^3/(mol*s)'), n=1.25799, w0=(407.77,'kJ/mol'), E0=(120.952,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 144,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H",
    kinetics = ArrheniusBM(A=(6.11389e+08,'m^3/(mol*s)'), n=-0.526977, w0=(482.785,'kJ/mol'), E0=(209.284,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3644918852903685, var=7.208857264701281, Tref=1000.0, N=80, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H',), comment="""BM rule fitted to 80 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H
    Total Standard Deviation in ln(k): 6.298385154664527"""),
    rank = 11,
    shortDesc = """BM rule fitted to 80 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H
Total Standard Deviation in ln(k): 6.298385154664527""",
    longDesc = 
"""
BM rule fitted to 80 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H
Total Standard Deviation in ln(k): 6.298385154664527
""",
)

entry(
    index = 145,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C",
    kinetics = ArrheniusBM(A=(7.8745e-10,'m^3/(mol*s)'), n=4.591, w0=(491.933,'kJ/mol'), E0=(167.976,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.08601141620493298, var=3.4900807239713676, Tref=1000.0, N=75, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C',), comment="""BM rule fitted to 75 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C
    Total Standard Deviation in ln(k): 3.961306591574779"""),
    rank = 11,
    shortDesc = """BM rule fitted to 75 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C
Total Standard Deviation in ln(k): 3.961306591574779""",
    longDesc = 
"""
BM rule fitted to 75 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C
Total Standard Deviation in ln(k): 3.961306591574779
""",
)

entry(
    index = 146,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C",
    kinetics = ArrheniusBM(A=(7.08135e-07,'m^3/(mol*s)'), n=3.83849, w0=(485,'kJ/mol'), E0=(179.209,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.011511552798783818, var=3.1739026006255564, Tref=1000.0, N=62, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C',), comment="""BM rule fitted to 62 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C
    Total Standard Deviation in ln(k): 3.6004492606027743"""),
    rank = 11,
    shortDesc = """BM rule fitted to 62 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C
Total Standard Deviation in ln(k): 3.6004492606027743""",
    longDesc = 
"""
BM rule fitted to 62 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C
Total Standard Deviation in ln(k): 3.6004492606027743
""",
)

entry(
    index = 147,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.09151e-06,'m^3/(mol*s)'), n=3.78211, w0=(485,'kJ/mol'), E0=(179.602,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04733750435694979, var=3.3257799001554456, Tref=1000.0, N=45, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R',), comment="""BM rule fitted to 45 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R
    Total Standard Deviation in ln(k): 3.7749178662136282"""),
    rank = 11,
    shortDesc = """BM rule fitted to 45 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.7749178662136282""",
    longDesc = 
"""
BM rule fitted to 45 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.7749178662136282
""",
)

entry(
    index = 148,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F",
    kinetics = ArrheniusBM(A=(2.32302e-06,'m^3/(mol*s)'), n=3.72385, w0=(485,'kJ/mol'), E0=(180.748,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04905979321646195, var=2.997139173150066, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F',), comment="""BM rule fitted to 20 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F
    Total Standard Deviation in ln(k): 3.5939128173609123"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F
Total Standard Deviation in ln(k): 3.5939128173609123""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F
Total Standard Deviation in ln(k): 3.5939128173609123
""",
)

entry(
    index = 149,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R",
    kinetics = ArrheniusBM(A=(4.049e-05,'m^3/(mol*s)'), n=3.37873, w0=(485,'kJ/mol'), E0=(186.744,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1632959862444138, var=4.208289948893707, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R
    Total Standard Deviation in ln(k): 4.522828409049108"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R
Total Standard Deviation in ln(k): 4.522828409049108""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R
Total Standard Deviation in ln(k): 4.522828409049108
""",
)

entry(
    index = 150,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F",
    kinetics = ArrheniusBM(A=(0.000180745,'m^3/(mol*s)'), n=3.23649, w0=(485,'kJ/mol'), E0=(192.71,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1486101245977482, var=5.79532703475617, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F
    Total Standard Deviation in ln(k): 5.19948835187987"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F
Total Standard Deviation in ln(k): 5.19948835187987""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F
Total Standard Deviation in ln(k): 5.19948835187987
""",
)

entry(
    index = 151,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.000156719,'m^3/(mol*s)'), n=3.21667, w0=(485,'kJ/mol'), E0=(196.016,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11105277292476928, var=5.28995906903933, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R
    Total Standard Deviation in ln(k): 4.889899907419436"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R
Total Standard Deviation in ln(k): 4.889899907419436""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R
Total Standard Deviation in ln(k): 4.889899907419436
""",
)

entry(
    index = 152,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.63605e-05,'m^3/(mol*s)'), n=3.51795, w0=(485,'kJ/mol'), E0=(196.951,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03982899793124997, var=6.097339520228167, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 5.050323386845739"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R
Total Standard Deviation in ln(k): 5.050323386845739""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R
Total Standard Deviation in ln(k): 5.050323386845739
""",
)

entry(
    index = 153,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(7.86898e-05,'m^3/(mol*s)'), n=3.34466, w0=(485,'kJ/mol'), E0=(197.61,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06673470836921505, var=11.904184412522445, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C
    Total Standard Deviation in ln(k): 7.084500537783163"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C
Total Standard Deviation in ln(k): 7.084500537783163""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C
Total Standard Deviation in ln(k): 7.084500537783163
""",
)

entry(
    index = 154,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_6R!H->C",
    kinetics = ArrheniusBM(A=(0.000351338,'m^3/(mol*s)'), n=2.76265, w0=(485,'kJ/mol'), E0=(194.788,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 155,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_N-6R!H->C",
    kinetics = ArrheniusBM(A=(2.33999e-05,'m^3/(mol*s)'), n=3.62751, w0=(485,'kJ/mol'), E0=(197.785,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.040626692649055364, var=15.212306789176688, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_N-6R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_N-6R!H->C
    Total Standard Deviation in ln(k): 7.921136781334383"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_N-6R!H->C
Total Standard Deviation in ln(k): 7.921136781334383""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_N-6R!H->C
Total Standard Deviation in ln(k): 7.921136781334383
""",
)

entry(
    index = 156,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_N-6R!H->C_Ext-7C-R_Ext-7C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(4.18684e-06,'m^3/(mol*s)'), n=3.66559, w0=(485,'kJ/mol'), E0=(196.92,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.028985101400090005, var=10.922236305026159, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_N-6R!H->C_Ext-7C-R_Ext-7C-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_N-6R!H->C_Ext-7C-R_Ext-7C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 6.6982371125215385"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_N-6R!H->C_Ext-7C-R_Ext-7C-R_Ext-3C-R
Total Standard Deviation in ln(k): 6.6982371125215385""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_N-6R!H->C_Ext-7C-R_Ext-7C-R_Ext-3C-R
Total Standard Deviation in ln(k): 6.6982371125215385
""",
)

entry(
    index = 157,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_N-6R!H->C_Ext-7C-R_Ext-7C-R_Ext-3C-R_Ext-7C-R_10R!H->C",
    kinetics = ArrheniusBM(A=(2.85326e-05,'m^3/(mol*s)'), n=3.50515, w0=(485,'kJ/mol'), E0=(193.528,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_N-6R!H->C_Ext-7C-R_Ext-7C-R_Ext-3C-R_Ext-7C-R_10R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_N-6R!H->C_Ext-7C-R_Ext-7C-R_Ext-3C-R_Ext-7C-R_10R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_N-6R!H->C_Ext-7C-R_Ext-7C-R_Ext-3C-R_Ext-7C-R_10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_N-6R!H->C_Ext-7C-R_Ext-7C-R_Ext-3C-R_Ext-7C-R_10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 158,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_N-6R!H->C_Ext-7C-R_Ext-7C-R_Ext-3C-R_Ext-7C-R_N-10R!H->C",
    kinetics = ArrheniusBM(A=(6.10895e-08,'m^3/(mol*s)'), n=4.11325, w0=(485,'kJ/mol'), E0=(197.825,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_N-6R!H->C_Ext-7C-R_Ext-7C-R_Ext-3C-R_Ext-7C-R_N-10R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_N-6R!H->C_Ext-7C-R_Ext-7C-R_Ext-3C-R_Ext-7C-R_N-10R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_N-6R!H->C_Ext-7C-R_Ext-7C-R_Ext-3C-R_Ext-7C-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_N-6R!H->C_Ext-7C-R_Ext-7C-R_Ext-3C-R_Ext-7C-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 159,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(6.50787e-07,'m^3/(mol*s)'), n=3.87488, w0=(485,'kJ/mol'), E0=(195.546,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.01936367091005961, var=0.6678765089259362, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_N-7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 1.6869963587925076"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_N-7R!H->C
Total Standard Deviation in ln(k): 1.6869963587925076""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_N-7R!H->C
Total Standard Deviation in ln(k): 1.6869963587925076
""",
)

entry(
    index = 160,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_N-7R!H->C_Ext-6R!H-R_8R!H->C",
    kinetics = ArrheniusBM(A=(3.8501e-07,'m^3/(mol*s)'), n=3.92844, w0=(485,'kJ/mol'), E0=(192.322,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_N-7R!H->C_Ext-6R!H-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_N-7R!H->C_Ext-6R!H-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_N-7R!H->C_Ext-6R!H-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_N-7R!H->C_Ext-6R!H-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 161,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_N-7R!H->C_Ext-6R!H-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(6.83125e-07,'m^3/(mol*s)'), n=3.8806, w0=(485,'kJ/mol'), E0=(198.247,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_N-7R!H->C_Ext-6R!H-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_N-7R!H->C_Ext-6R!H-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_N-7R!H->C_Ext-6R!H-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_N-7R!H->C_Ext-6R!H-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 162,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.78672e-06,'m^3/(mol*s)'), n=3.80669, w0=(485,'kJ/mol'), E0=(175.743,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 163,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(1.72454e-06,'m^3/(mol*s)'), n=3.63971, w0=(485,'kJ/mol'), E0=(170.362,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.22238140263848516, var=1.0764774624303912, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F
    Total Standard Deviation in ln(k): 2.638728685460188"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F
Total Standard Deviation in ln(k): 2.638728685460188""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F
Total Standard Deviation in ln(k): 2.638728685460188
""",
)

entry(
    index = 164,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_Ext-5BrCClINOPSSi-R",
    kinetics = ArrheniusBM(A=(1.40731e-06,'m^3/(mol*s)'), n=3.65347, w0=(485,'kJ/mol'), E0=(172.64,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.24620865212369916, var=0.021674503971195642, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_Ext-5BrCClINOPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_Ext-5BrCClINOPSSi-R
    Total Standard Deviation in ln(k): 0.9137570824578515"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_Ext-5BrCClINOPSSi-R
Total Standard Deviation in ln(k): 0.9137570824578515""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_Ext-5BrCClINOPSSi-R
Total Standard Deviation in ln(k): 0.9137570824578515
""",
)

entry(
    index = 165,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_Ext-5BrCClINOPSSi-R_6R!H->C",
    kinetics = ArrheniusBM(A=(5.66169e-06,'m^3/(mol*s)'), n=3.44838, w0=(485,'kJ/mol'), E0=(172.708,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_Ext-5BrCClINOPSSi-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_Ext-5BrCClINOPSSi-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_Ext-5BrCClINOPSSi-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_Ext-5BrCClINOPSSi-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 166,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_Ext-5BrCClINOPSSi-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(3.50479e-07,'m^3/(mol*s)'), n=3.85832, w0=(485,'kJ/mol'), E0=(172.575,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_Ext-5BrCClINOPSSi-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_Ext-5BrCClINOPSSi-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_Ext-5BrCClINOPSSi-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_Ext-5BrCClINOPSSi-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 167,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.07551e-08,'m^3/(mol*s)'), n=4.26628, w0=(485,'kJ/mol'), E0=(171.742,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.15775208188314488, var=1.3842966789088298, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R
    Total Standard Deviation in ln(k): 2.755055882272256"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R
Total Standard Deviation in ln(k): 2.755055882272256""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R
Total Standard Deviation in ln(k): 2.755055882272256
""",
)

entry(
    index = 168,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.31033e-08,'m^3/(mol*s)'), n=4.27966, w0=(485,'kJ/mol'), E0=(169.265,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1915051705106356, var=1.4977726943073988, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C
    Total Standard Deviation in ln(k): 2.9346342044127023"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 2.9346342044127023""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 2.9346342044127023
""",
)

entry(
    index = 169,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.03919e-08,'m^3/(mol*s)'), n=4.24976, w0=(485,'kJ/mol'), E0=(171.682,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.24602295488741688, var=2.944075674791113, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R
    Total Standard Deviation in ln(k): 4.05793451844353"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 4.05793451844353""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 4.05793451844353
""",
)

entry(
    index = 170,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(1.31087e-08,'m^3/(mol*s)'), n=4.12499, w0=(485,'kJ/mol'), E0=(171.629,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 171,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(8.44929e-09,'m^3/(mol*s)'), n=4.37139, w0=(485,'kJ/mol'), E0=(171.762,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 172,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(5.31049e-09,'m^3/(mol*s)'), n=4.37935, w0=(485,'kJ/mol'), E0=(166.288,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.16669961265337538, var=3.640119552359861, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R
    Total Standard Deviation in ln(k): 4.243696815739693"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 4.243696815739693""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 4.243696815739693
""",
)

entry(
    index = 173,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(1.3066e-08,'m^3/(mol*s)'), n=4.32862, w0=(485,'kJ/mol'), E0=(165.188,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 174,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(3.13797e-09,'m^3/(mol*s)'), n=4.38351, w0=(485,'kJ/mol'), E0=(167.79,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 175,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(7.13496e-08,'m^3/(mol*s)'), n=4.22227, w0=(485,'kJ/mol'), E0=(178.019,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.07298052488180977, var=9.144254022620858, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 6.245580299987413"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 6.245580299987413""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 6.245580299987413
""",
)

entry(
    index = 176,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrClFINOPSSi-3C",
    kinetics = ArrheniusBM(A=(2.5954e-07,'m^3/(mol*s)'), n=4.05671, w0=(485,'kJ/mol'), E0=(170.29,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrClFINOPSSi-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrClFINOPSSi-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrClFINOPSSi-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrClFINOPSSi-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 177,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrClFINOPSSi-3C",
    kinetics = ArrheniusBM(A=(1.87843e-08,'m^3/(mol*s)'), n=4.39321, w0=(485,'kJ/mol'), E0=(185.702,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrClFINOPSSi-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrClFINOPSSi-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrClFINOPSSi-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrClFINOPSSi-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 178,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F",
    kinetics = ArrheniusBM(A=(2.84388e-07,'m^3/(mol*s)'), n=3.89027, w0=(485,'kJ/mol'), E0=(177.603,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04435738946624992, var=4.643179823815411, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F',), comment="""BM rule fitted to 25 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F
    Total Standard Deviation in ln(k): 4.431261679541101"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F
Total Standard Deviation in ln(k): 4.431261679541101""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F
Total Standard Deviation in ln(k): 4.431261679541101
""",
)

entry(
    index = 179,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C",
    kinetics = ArrheniusBM(A=(1.76414e-06,'m^3/(mol*s)'), n=3.68184, w0=(485,'kJ/mol'), E0=(188.339,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05661268792737516, var=13.859434444901384, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C
    Total Standard Deviation in ln(k): 7.605523077989745"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C
Total Standard Deviation in ln(k): 7.605523077989745""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C
Total Standard Deviation in ln(k): 7.605523077989745
""",
)

entry(
    index = 180,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.31081e-05,'m^3/(mol*s)'), n=3.18069, w0=(485,'kJ/mol'), E0=(197.934,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04700888784542293, var=78.2636169341972, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R
    Total Standard Deviation in ln(k): 17.853347758443853"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R
Total Standard Deviation in ln(k): 17.853347758443853""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R
Total Standard Deviation in ln(k): 17.853347758443853
""",
)

entry(
    index = 181,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.24758e-05,'m^3/(mol*s)'), n=3.18211, w0=(485,'kJ/mol'), E0=(197.96,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.061299415401619595, var=79.17944444000732, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 17.992719151285804"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R_Ext-3C-R
Total Standard Deviation in ln(k): 17.992719151285804""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R_Ext-3C-R
Total Standard Deviation in ln(k): 17.992719151285804
""",
)

entry(
    index = 182,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R_Ext-3C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(1.95992e-06,'m^3/(mol*s)'), n=3.05765, w0=(485,'kJ/mol'), E0=(194.063,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R_Ext-3C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R_Ext-3C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R_Ext-3C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R_Ext-3C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 183,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R_Ext-3C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(2.47232e-06,'m^3/(mol*s)'), n=3.97637, w0=(485,'kJ/mol'), E0=(196.08,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R_Ext-3C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R_Ext-3C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R_Ext-3C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R_Ext-3C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 184,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.4494e-08,'m^3/(mol*s)'), n=4.15875, w0=(485,'kJ/mol'), E0=(182.031,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.023073450138572035, var=8.00087552305103, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-3C-R
    Total Standard Deviation in ln(k): 5.728530832154432"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-3C-R
Total Standard Deviation in ln(k): 5.728530832154432""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-3C-R
Total Standard Deviation in ln(k): 5.728530832154432
""",
)

entry(
    index = 185,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-3C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2.2091e-08,'m^3/(mol*s)'), n=4.272, w0=(485,'kJ/mol'), E0=(176.848,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-3C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-3C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 186,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-3C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.72335e-08,'m^3/(mol*s)'), n=4.18731, w0=(485,'kJ/mol'), E0=(185.981,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-3C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-3C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 187,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(5.7299e-06,'m^3/(mol*s)'), n=3.76087, w0=(485,'kJ/mol'), E0=(182.454,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 188,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(4.33733e-06,'m^3/(mol*s)'), n=3.8659, w0=(485,'kJ/mol'), E0=(180.651,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.137253727441554, var=10.35056389721595, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 14.332239336682289"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 14.332239336682289""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 14.332239336682289
""",
)

entry(
    index = 189,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C",
    kinetics = ArrheniusBM(A=(1.04035e-07,'m^3/(mol*s)'), n=4.00212, w0=(485,'kJ/mol'), E0=(170.288,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04105420917486808, var=0.11295434937841056, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C',), comment="""BM rule fitted to 17 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C
    Total Standard Deviation in ln(k): 0.7769163128608106"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C
Total Standard Deviation in ln(k): 0.7769163128608106""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C
Total Standard Deviation in ln(k): 0.7769163128608106
""",
)

entry(
    index = 190,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0",
    kinetics = ArrheniusBM(A=(8.67688e-08,'m^3/(mol*s)'), n=4.02421, w0=(485,'kJ/mol'), E0=(170.157,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03622182472569564, var=0.05143841760517488, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0
    Total Standard Deviation in ln(k): 0.5456843103614686"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0
Total Standard Deviation in ln(k): 0.5456843103614686""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0
Total Standard Deviation in ln(k): 0.5456843103614686
""",
)

entry(
    index = 191,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O",
    kinetics = ArrheniusBM(A=(6.8754e-08,'m^3/(mol*s)'), n=4.03838, w0=(485,'kJ/mol'), E0=(170.077,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.07247391028697772, var=0.1901711691979883, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O
    Total Standard Deviation in ln(k): 1.056332543236906"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O
Total Standard Deviation in ln(k): 1.056332543236906""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O
Total Standard Deviation in ln(k): 1.056332543236906
""",
)

entry(
    index = 192,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-3C-R",
    kinetics = ArrheniusBM(A=(6.72814e-08,'m^3/(mol*s)'), n=4.04013, w0=(485,'kJ/mol'), E0=(170.068,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.07804593232456486, var=0.16802021382168247, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-3C-R
    Total Standard Deviation in ln(k): 1.0178416047695489"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-3C-R
Total Standard Deviation in ln(k): 1.0178416047695489""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-3C-R
Total Standard Deviation in ln(k): 1.0178416047695489
""",
)

entry(
    index = 193,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(4.17031e-08,'m^3/(mol*s)'), n=4.09034, w0=(485,'kJ/mol'), E0=(169.935,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1431740055633906, var=0.4551542202767174, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 1.7122305761936274"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 1.7122305761936274""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 1.7122305761936274
""",
)

entry(
    index = 194,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-3C-R_Ext-3C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(4.11856e-08,'m^3/(mol*s)'), n=4.0381, w0=(485,'kJ/mol'), E0=(164.921,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-3C-R_Ext-3C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-3C-R_Ext-3C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-3C-R_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-3C-R_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 195,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-3C-R_Ext-3C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(6.32707e-08,'m^3/(mol*s)'), n=4.09227, w0=(485,'kJ/mol'), E0=(175.4,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-3C-R_Ext-3C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-3C-R_Ext-3C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-3C-R_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-3C-R_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 196,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.38922e-05,'m^3/(mol*s)'), n=3.5758, w0=(485,'kJ/mol'), E0=(168.898,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 197,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O",
    kinetics = ArrheniusBM(A=(1.00462e-07,'m^3/(mol*s)'), n=4.01706, w0=(485,'kJ/mol'), E0=(170.187,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12077137997534841, var=0.021103551809622263, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O
    Total Standard Deviation in ln(k): 0.5946747775024339"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O
Total Standard Deviation in ln(k): 0.5946747775024339""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O
Total Standard Deviation in ln(k): 0.5946747775024339
""",
)

entry(
    index = 198,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R",
    kinetics = ArrheniusBM(A=(9.9562e-08,'m^3/(mol*s)'), n=4.0173, w0=(485,'kJ/mol'), E0=(170.185,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1175287176129335, var=0.006797896954272578, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R
    Total Standard Deviation in ln(k): 0.4605874094370892"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R
Total Standard Deviation in ln(k): 0.4605874094370892""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R
Total Standard Deviation in ln(k): 0.4605874094370892
""",
)

entry(
    index = 199,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_5R!H->O",
    kinetics = ArrheniusBM(A=(9.11574e-08,'m^3/(mol*s)'), n=4.14961, w0=(485,'kJ/mol'), E0=(177.055,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 200,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(1.02759e-07,'m^3/(mol*s)'), n=3.97293, w0=(485,'kJ/mol'), E0=(167.899,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.14235073745537866, var=0.007635410199344114, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_N-5R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_N-5R!H->O
    Total Standard Deviation in ln(k): 0.5328405930575253"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_N-5R!H->O
Total Standard Deviation in ln(k): 0.5328405930575253""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_N-5R!H->O
Total Standard Deviation in ln(k): 0.5328405930575253
""",
)

entry(
    index = 201,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_N-5R!H->O_Ext-4C-R",
    kinetics = ArrheniusBM(A=(8.99897e-08,'m^3/(mol*s)'), n=3.97409, w0=(485,'kJ/mol'), E0=(167.101,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1485495104154731, var=0.0008946543607405933, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_N-5R!H->O_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_N-5R!H->O_Ext-4C-R
    Total Standard Deviation in ln(k): 0.43320315238956003"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_N-5R!H->O_Ext-4C-R
Total Standard Deviation in ln(k): 0.43320315238956003""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_N-5R!H->O_Ext-4C-R
Total Standard Deviation in ln(k): 0.43320315238956003
""",
)

entry(
    index = 202,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_N-5R!H->O_Ext-4C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(7.80562e-08,'m^3/(mol*s)'), n=3.96948, w0=(485,'kJ/mol'), E0=(165.768,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_N-5R!H->O_Ext-4C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_N-5R!H->O_Ext-4C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_N-5R!H->O_Ext-4C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_N-5R!H->O_Ext-4C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 203,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_N-5R!H->O_Ext-4C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(1.03271e-07,'m^3/(mol*s)'), n=3.97927, w0=(485,'kJ/mol'), E0=(168.429,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_N-5R!H->O_Ext-4C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_N-5R!H->O_Ext-4C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_N-5R!H->O_Ext-4C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_N-5R!H->O_Ext-4C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 204,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.21333e-05,'m^3/(mol*s)'), n=3.66599, w0=(485,'kJ/mol'), E0=(168.608,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 205,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-4C-R",
    kinetics = ArrheniusBM(A=(4.51365e-06,'m^3/(mol*s)'), n=3.78897, w0=(485,'kJ/mol'), E0=(175.374,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 206,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-1C-u0",
    kinetics = ArrheniusBM(A=(32.9374,'m^3/(mol*s)'), n=1.70228, w0=(485,'kJ/mol'), E0=(174.045,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.42054812777791145, var=12.25187189509137, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-1C-u0',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-1C-u0
    Total Standard Deviation in ln(k): 8.073762431175894"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-1C-u0
Total Standard Deviation in ln(k): 8.073762431175894""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-1C-u0
Total Standard Deviation in ln(k): 8.073762431175894
""",
)

entry(
    index = 207,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-1C-u0_4BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(5584.53,'m^3/(mol*s)'), n=0.969198, w0=(485,'kJ/mol'), E0=(175.439,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5471976191467088, var=32.594072987089795, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-1C-u0_4BrCClINOPSSi->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-1C-u0_4BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 12.820145344587809"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-1C-u0_4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 12.820145344587809""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-1C-u0_4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 12.820145344587809
""",
)

entry(
    index = 208,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-1C-u0_N-4BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.00707636,'m^3/(mol*s)'), n=2.89471, w0=(485,'kJ/mol'), E0=(171.122,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.15132977554425434, var=7.137535919274681, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-1C-u0_N-4BrCClINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-1C-u0_N-4BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 5.7361093263938985"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-1C-u0_N-4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 5.7361093263938985""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-1C-u0_N-4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 5.7361093263938985
""",
)

entry(
    index = 209,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O",
    kinetics = ArrheniusBM(A=(1.29473e-07,'m^3/(mol*s)'), n=4.33314, w0=(485,'kJ/mol'), E0=(180.081,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.0373417633816966, var=12.506196891688253, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O
    Total Standard Deviation in ln(k): 12.208514670420353"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O
Total Standard Deviation in ln(k): 12.208514670420353""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O
Total Standard Deviation in ln(k): 12.208514670420353
""",
)

entry(
    index = 210,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.03733,'m^3/(mol*s)'), n=2.44287, w0=(485,'kJ/mol'), E0=(172.342,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.046510539731673545, var=17.561199450518476, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_Ext-3C-R
    Total Standard Deviation in ln(k): 8.517920472347988"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_Ext-3C-R
Total Standard Deviation in ln(k): 8.517920472347988""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_Ext-3C-R
Total Standard Deviation in ln(k): 8.517920472347988
""",
)

entry(
    index = 211,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_3C-u1",
    kinetics = ArrheniusBM(A=(3.83004e-08,'m^3/(mol*s)'), n=4.48526, w0=(485,'kJ/mol'), E0=(179.364,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4105355365909573, var=0.08723335776142443, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_3C-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_3C-u1
    Total Standard Deviation in ln(k): 1.6236007173533158"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_3C-u1
Total Standard Deviation in ln(k): 1.6236007173533158""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_3C-u1
Total Standard Deviation in ln(k): 1.6236007173533158
""",
)

entry(
    index = 212,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_3C-u1_Sp-4O-3C",
    kinetics = ArrheniusBM(A=(9.22244e-08,'m^3/(mol*s)'), n=4.22266, w0=(485,'kJ/mol'), E0=(173.186,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_3C-u1_Sp-4O-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_3C-u1_Sp-4O-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_3C-u1_Sp-4O-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_3C-u1_Sp-4O-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 213,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_3C-u1_N-Sp-4O-3C",
    kinetics = ArrheniusBM(A=(3.80839e-08,'m^3/(mol*s)'), n=4.48675, w0=(485,'kJ/mol'), E0=(179.394,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_3C-u1_N-Sp-4O-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_3C-u1_N-Sp-4O-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_3C-u1_N-Sp-4O-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_3C-u1_N-Sp-4O-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 214,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_N-3C-u1",
    kinetics = ArrheniusBM(A=(0.000116883,'m^3/(mol*s)'), n=3.29891, w0=(485,'kJ/mol'), E0=(164.918,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.19932092372646779, var=0.8141656799581468, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_N-3C-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_N-3C-u1
    Total Standard Deviation in ln(k): 2.309701452472474"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_N-3C-u1
Total Standard Deviation in ln(k): 2.309701452472474""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_N-3C-u1
Total Standard Deviation in ln(k): 2.309701452472474
""",
)

entry(
    index = 215,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(2.37218e-08,'m^3/(mol*s)'), n=4.19176, w0=(485,'kJ/mol'), E0=(175.385,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2725448295517875, var=5.112114104232301, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O
    Total Standard Deviation in ln(k): 5.217488956790228"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O
Total Standard Deviation in ln(k): 5.217488956790228""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O
Total Standard Deviation in ln(k): 5.217488956790228
""",
)

entry(
    index = 216,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_Sp-4BrBrCCClClFFIINNPPSSSiSi=3C",
    kinetics = ArrheniusBM(A=(2.6293e-08,'m^3/(mol*s)'), n=4.39812, w0=(485,'kJ/mol'), E0=(179.717,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2777538316946297, var=0.08715771754160752, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_Sp-4BrBrCCClClFFIINNPPSSSiSi=3C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_Sp-4BrBrCCClClFFIINNPPSSSiSi=3C
    Total Standard Deviation in ln(k): 1.2897215801148425"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_Sp-4BrBrCCClClFFIINNPPSSSiSi=3C
Total Standard Deviation in ln(k): 1.2897215801148425""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_Sp-4BrBrCCClClFFIINNPPSSSiSi=3C
Total Standard Deviation in ln(k): 1.2897215801148425
""",
)

entry(
    index = 217,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.13802e-08,'m^3/(mol*s)'), n=4.49561, w0=(485,'kJ/mol'), E0=(177.749,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 218,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C",
    kinetics = ArrheniusBM(A=(2.3768e-08,'m^3/(mol*s)'), n=4.19078, w0=(485,'kJ/mol'), E0=(175.373,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2740453669517624, var=5.157959615099502, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C
    Total Standard Deviation in ln(k): 5.241538458240807"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C
Total Standard Deviation in ln(k): 5.241538458240807""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C
Total Standard Deviation in ln(k): 5.241538458240807
""",
)

entry(
    index = 219,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(1.02058e-05,'m^3/(mol*s)'), n=3.59517, w0=(485,'kJ/mol'), E0=(173.156,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2571020249191066, var=8.498307234540583, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 6.490159868964462"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C
Total Standard Deviation in ln(k): 6.490159868964462""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C
Total Standard Deviation in ln(k): 6.490159868964462
""",
)

entry(
    index = 220,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.000333719,'m^3/(mol*s)'), n=3.29572, w0=(485,'kJ/mol'), E0=(169.311,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.31237429132370714, var=34.63502170151887, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C_Ext-3C-R
    Total Standard Deviation in ln(k): 12.583031979633486"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C_Ext-3C-R
Total Standard Deviation in ln(k): 12.583031979633486""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C_Ext-3C-R
Total Standard Deviation in ln(k): 12.583031979633486
""",
)

entry(
    index = 221,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C_3C-u1",
    kinetics = ArrheniusBM(A=(1.05e-08,'m^3/(mol*s)'), n=4.48169, w0=(485,'kJ/mol'), E0=(173.038,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.28095595865846196, var=0.02692920651919652, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C_3C-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C_3C-u1
    Total Standard Deviation in ln(k): 1.0348989423555557"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C_3C-u1
Total Standard Deviation in ln(k): 1.0348989423555557""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C_3C-u1
Total Standard Deviation in ln(k): 1.0348989423555557
""",
)

entry(
    index = 222,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C_3C-u1_Ext-4C-R",
    kinetics = ArrheniusBM(A=(1.11161e-08,'m^3/(mol*s)'), n=4.4858, w0=(485,'kJ/mol'), E0=(174.256,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C_3C-u1_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C_3C-u1_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C_3C-u1_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C_3C-u1_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 223,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C_N-3C-u1",
    kinetics = ArrheniusBM(A=(2.52455e-06,'m^3/(mol*s)'), n=3.43897, w0=(485,'kJ/mol'), E0=(172.254,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C_N-3C-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C_N-3C-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C_N-3C-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C_N-3C-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 224,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_N-4BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(2.36087e-08,'m^3/(mol*s)'), n=4.19027, w0=(485,'kJ/mol'), E0=(175.44,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2826168929260327, var=5.1733135304480795, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_N-4BrCClFINPSSi->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_N-4BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 5.269846447066208"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_N-4BrCClFINPSSi->C
Total Standard Deviation in ln(k): 5.269846447066208""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_N-4BrCClFINPSSi->C
Total Standard Deviation in ln(k): 5.269846447066208
""",
)

entry(
    index = 225,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_N-4BrCClFINPSSi->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.27458e-07,'m^3/(mol*s)'), n=3.92887, w0=(485,'kJ/mol'), E0=(178.761,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.32428519464169964, var=12.582193226807838, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_N-4BrCClFINPSSi->C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_N-4BrCClFINPSSi->C_Ext-3C-R
    Total Standard Deviation in ln(k): 7.9258603737154765"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_N-4BrCClFINPSSi->C_Ext-3C-R
Total Standard Deviation in ln(k): 7.9258603737154765""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_N-4BrCClFINPSSi->C_Ext-3C-R
Total Standard Deviation in ln(k): 7.9258603737154765
""",
)

entry(
    index = 226,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_N-4BrCClFINPSSi->C_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(4.12044e-06,'m^3/(mol*s)'), n=3.28057, w0=(485,'kJ/mol'), E0=(180.908,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_N-4BrCClFINPSSi->C_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_N-4BrCClFINPSSi->C_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_N-4BrCClFINPSSi->C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_N-4BrCClFINPSSi->C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 227,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C",
    kinetics = ArrheniusBM(A=(1.66429e-16,'m^3/(mol*s)'), n=6.24272, w0=(525,'kJ/mol'), E0=(140.105,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.32514406755751285, var=5.179261680276794, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C
    Total Standard Deviation in ln(k): 5.379319238448649"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C
Total Standard Deviation in ln(k): 5.379319238448649""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C
Total Standard Deviation in ln(k): 5.379319238448649
""",
)

entry(
    index = 228,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(9.55993e-18,'m^3/(mol*s)'), n=6.58771, w0=(525,'kJ/mol'), E0=(138.185,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3712911527639925, var=5.020769751201103, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R
    Total Standard Deviation in ln(k): 5.4249171107762315"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R
Total Standard Deviation in ln(k): 5.4249171107762315""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R
Total Standard Deviation in ln(k): 5.4249171107762315
""",
)

entry(
    index = 229,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(1.08539e-15,'m^3/(mol*s)'), n=5.87859, w0=(525,'kJ/mol'), E0=(145.784,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4230103628905603, var=0.0747613929999113, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_4R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_4R!H->Cl
    Total Standard Deviation in ln(k): 1.6109853915627652"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_4R!H->Cl
Total Standard Deviation in ln(k): 1.6109853915627652""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_4R!H->Cl
Total Standard Deviation in ln(k): 1.6109853915627652
""",
)

entry(
    index = 230,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.15712e-16,'m^3/(mol*s)'), n=6.26519, w0=(525,'kJ/mol'), E0=(151.335,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 231,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(1.54823e-16,'m^3/(mol*s)'), n=6.26526, w0=(525,'kJ/mol'), E0=(140.776,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.31781845747307624, var=6.055533564411224, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 5.731789663531459"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 5.731789663531459""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 5.731789663531459
""",
)

entry(
    index = 232,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.33617e-16,'m^3/(mol*s)'), n=6.19203, w0=(525,'kJ/mol'), E0=(150.099,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.40724510089526367, var=5.198000355573465, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R
    Total Standard Deviation in ln(k): 5.59384917217177"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 5.59384917217177""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 5.59384917217177
""",
)

entry(
    index = 233,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.2063e-18,'m^3/(mol*s)'), n=6.64533, w0=(525,'kJ/mol'), E0=(149.222,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5123269305714587, var=0.4314428468336084, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 2.604049980247741"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 2.604049980247741""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 2.604049980247741
""",
)

entry(
    index = 234,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_Ext-3C-R_4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.40488e-20,'m^3/(mol*s)'), n=7.16576, w0=(525,'kJ/mol'), E0=(140.364,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_Ext-3C-R_4BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_Ext-3C-R_4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_Ext-3C-R_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_Ext-3C-R_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 235,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_Ext-3C-R_N-4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(5.16046e-17,'m^3/(mol*s)'), n=6.21158, w0=(525,'kJ/mol'), E0=(157.277,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_Ext-3C-R_N-4BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_Ext-3C-R_N-4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_Ext-3C-R_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_Ext-3C-R_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 236,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(5.21404e-19,'m^3/(mol*s)'), n=7.11375, w0=(525,'kJ/mol'), E0=(134.458,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4606984976492022, var=0.6891163442719499, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 2.8217252802809916"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 2.8217252802809916""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 2.8217252802809916
""",
)

entry(
    index = 237,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFINOPSSi->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(3.97188e-24,'m^3/(mol*s)'), n=8.75221, w0=(525,'kJ/mol'), E0=(128.14,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFINOPSSi->C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFINOPSSi->C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFINOPSSi->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFINOPSSi->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 238,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(3.92893e-16,'m^3/(mol*s)'), n=6.16724, w0=(525,'kJ/mol'), E0=(154.758,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3970616169768928, var=3.349701974648823, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 4.666746694103744"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 4.666746694103744""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 4.666746694103744
""",
)

entry(
    index = 239,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_4FO->O",
    kinetics = ArrheniusBM(A=(3.41588e-16,'m^3/(mol*s)'), n=6.33412, w0=(525,'kJ/mol'), E0=(158.017,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_4FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_4FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_4FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_4FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 240,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_N-4FO->O",
    kinetics = ArrheniusBM(A=(6.45222e-17,'m^3/(mol*s)'), n=6.24256, w0=(525,'kJ/mol'), E0=(149.427,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_N-4FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_N-4FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_N-4FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_N-4FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 241,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(4.14651e-12,'m^3/(mol*s)'), n=5.07461, w0=(525,'kJ/mol'), E0=(135.576,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_4BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 242,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(2.3435e-24,'m^3/(mol*s)'), n=8.52388, w0=(525,'kJ/mol'), E0=(108.594,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.33614716314800946, var=6.9450224743561035, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 6.127751515346931"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 6.127751515346931""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 6.127751515346931
""",
)

entry(
    index = 243,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_4FO->O",
    kinetics = ArrheniusBM(A=(1.18976e-10,'m^3/(mol*s)'), n=4.6258, w0=(525,'kJ/mol'), E0=(137.231,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_4FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_4FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_4FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_4FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 244,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_N-4FO->O",
    kinetics = ArrheniusBM(A=(9.48502e-34,'m^3/(mol*s)'), n=11.2007, w0=(525,'kJ/mol'), E0=(87.9013,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.39753805332526565, var=12.932391209827507, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_N-4FO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_N-4FO->O
    Total Standard Deviation in ln(k): 8.208194244862666"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_N-4FO->O
Total Standard Deviation in ln(k): 8.208194244862666""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_N-4FO->O
Total Standard Deviation in ln(k): 8.208194244862666
""",
)

entry(
    index = 245,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C",
    kinetics = ArrheniusBM(A=(0.878562,'m^3/(mol*s)'), n=2.10645, w0=(345.554,'kJ/mol'), E0=(87.1083,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7669067648961804, var=19.284882132302762, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C
    Total Standard Deviation in ln(k): 10.730606466217957"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C
Total Standard Deviation in ln(k): 10.730606466217957""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C
Total Standard Deviation in ln(k): 10.730606466217957
""",
)

entry(
    index = 246,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C",
    kinetics = ArrheniusBM(A=(70.1382,'m^3/(mol*s)'), n=1.97916, w0=(320,'kJ/mol'), E0=(95.6327,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.2049865575261587, var=1.6370739762218876, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C
    Total Standard Deviation in ln(k): 5.592626696024934"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C
Total Standard Deviation in ln(k): 5.592626696024934""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C
Total Standard Deviation in ln(k): 5.592626696024934
""",
)

entry(
    index = 247,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(64.8337,'m^3/(mol*s)'), n=1.99041, w0=(320,'kJ/mol'), E0=(95.6327,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.373551942715818, var=2.2544268410454205, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R
    Total Standard Deviation in ln(k): 6.461194911430702"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R
Total Standard Deviation in ln(k): 6.461194911430702""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R
Total Standard Deviation in ln(k): 6.461194911430702
""",
)

entry(
    index = 248,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_4R!H->O",
    kinetics = ArrheniusBM(A=(13.7245,'m^3/(mol*s)'), n=2.18372, w0=(320,'kJ/mol'), E0=(90.3563,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 249,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(1.01241e+11,'m^3/(mol*s)'), n=-0.712343, w0=(320,'kJ/mol'), E0=(123.579,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 250,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C",
    kinetics = ArrheniusBM(A=(27425,'m^3/(mol*s)'), n=0.648618, w0=(383.885,'kJ/mol'), E0=(122.729,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.14457842970944615, var=0.11619004637029645, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C
    Total Standard Deviation in ln(k): 1.0466096376231928"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C
Total Standard Deviation in ln(k): 1.0466096376231928""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C
Total Standard Deviation in ln(k): 1.0466096376231928
""",
)

entry(
    index = 251,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C_3ClF->F",
    kinetics = ArrheniusBM(A=(9924.64,'m^3/(mol*s)'), n=0.717092, w0=(360,'kJ/mol'), E0=(109.632,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C_3ClF->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C_3ClF->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C_3ClF->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C_3ClF->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 252,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C_N-3ClF->F",
    kinetics = ArrheniusBM(A=(1592.36,'m^3/(mol*s)'), n=1.06078, w0=(407.77,'kJ/mol'), E0=(123.454,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C_N-3ClF->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C_N-3ClF->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C_N-3ClF->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C_N-3ClF->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

