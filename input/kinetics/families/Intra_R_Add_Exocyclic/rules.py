#!/usr/bin/env python
# encoding: utf-8

name = "Intra_R_Add_Exocyclic/rules"
shortDesc = ""
longDesc = """
General comments go at the top of the file,

or in a section(s) titled 'General'

.. the ID must match those in the rateLibrary AS A STRING (ie. '2' is different from '02')
"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(0.00236757,'s^-1'), n=4.06678, w0=(298536,'J/mol'), E0=(33139.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2590740457753217, var=31.25908666079392, Tref=1000.0, N=374, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 374 training reactions at node Root
    Total Standard Deviation in ln(k): 11.859378789575507"""),
    rank = 11,
    shortDesc = """BM rule fitted to 374 training reactions at node Root
Total Standard Deviation in ln(k): 11.859378789575507""",
    longDesc = 
"""
BM rule fitted to 374 training reactions at node Root
Total Standard Deviation in ln(k): 11.859378789575507
""",
)

entry(
    index = 2,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(15.0359,'s^-1'), n=2.95378, w0=(298055,'J/mol'), E0=(49288.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.16566985214994603, var=29.88646097300466, Tref=1000.0, N=309, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R',), comment="""BM rule fitted to 309 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.375844077281805"""),
    rank = 11,
    shortDesc = """BM rule fitted to 309 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.375844077281805""",
    longDesc = 
"""
BM rule fitted to 309 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.375844077281805
""",
)

entry(
    index = 3,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(28369.2,'s^-1'), n=2.19471, w0=(300629,'J/mol'), E0=(-5975.21,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.744728002539553, var=42.615331796011496, Tref=1000.0, N=31, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 31 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 19.98329621237887"""),
    rank = 11,
    shortDesc = """BM rule fitted to 31 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 19.98329621237887""",
    longDesc = 
"""
BM rule fitted to 31 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 19.98329621237887
""",
)

entry(
    index = 4,
    label = "Root_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(8.75789e+08,'s^-1'), n=0.974372, w0=(301000,'J/mol'), E0=(23585.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.21168631147271214, var=1.6061326827803675, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 20 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 3.072541876475581"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 3.072541876475581""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 3.072541876475581
""",
)

entry(
    index = 5,
    label = "Root_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R",
    kinetics = ArrheniusBM(A=(1.03499e+11,'s^-1'), n=0.401583, w0=(301000,'J/mol'), E0=(31759.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.041898202322309105, var=1.6198625782520386, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R
    Total Standard Deviation in ln(k): 2.6567748203682866"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R
Total Standard Deviation in ln(k): 2.6567748203682866""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R
Total Standard Deviation in ln(k): 2.6567748203682866
""",
)

entry(
    index = 6,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(8.43839e-22,'s^-1'), n=9.48875, w0=(292233,'J/mol'), E0=(26922.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6922242234571211, var=130.8884485559219, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H',), comment="""BM rule fitted to 15 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 24.674727114986407"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 24.674727114986407""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 24.674727114986407
""",
)

entry(
    index = 7,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(1.45397e+10,'s^-1'), n=0.355126, w0=(298352,'J/mol'), E0=(66658.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09787741744447599, var=16.53644654772196, Tref=1000.0, N=294, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H',), comment="""BM rule fitted to 294 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 8.398184340870088"""),
    rank = 11,
    shortDesc = """BM rule fitted to 294 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 8.398184340870088""",
    longDesc = 
"""
BM rule fitted to 294 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 8.398184340870088
""",
)

entry(
    index = 8,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(9.44682e+22,'s^-1'), n=-2.83224, w0=(301000,'J/mol'), E0=(53732.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.296039633544568, var=2.095688256618284, Tref=1000.0, N=24, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 24 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 3.645971340604814"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 3.645971340604814""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 3.645971340604814
""",
)

entry(
    index = 9,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H#4R!H",
    kinetics = ArrheniusBM(A=(2.20876e+23,'s^-1'), n=-3.21146, w0=(301000,'J/mol'), E0=(41189.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.554225271598829, var=2.416923504474888, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H#4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H#4R!H
    Total Standard Deviation in ln(k): 9.53430436633193"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H#4R!H
Total Standard Deviation in ln(k): 9.53430436633193""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H#4R!H
Total Standard Deviation in ln(k): 9.53430436633193
""",
)

entry(
    index = 10,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H",
    kinetics = ArrheniusBM(A=(3.63185e+18,'s^-1'), n=-1.92567, w0=(298700,'J/mol'), E0=(74983.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.21440539630920238, var=34.792021002659354, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H
    Total Standard Deviation in ln(k): 12.363589085765115"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H
Total Standard Deviation in ln(k): 12.363589085765115""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H
Total Standard Deviation in ln(k): 12.363589085765115
""",
)

entry(
    index = 11,
    label = "Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R",
    kinetics = ArrheniusBM(A=(3.81806e+14,'s^-1'), n=-0.425082, w0=(301000,'J/mol'), E0=(34195.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07392732318713054, var=0.9737517633784474, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R',), comment="""BM rule fitted to 12 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R
    Total Standard Deviation in ln(k): 2.1639967862167615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R
Total Standard Deviation in ln(k): 2.1639967862167615""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R
Total Standard Deviation in ln(k): 2.1639967862167615
""",
)

entry(
    index = 12,
    label = "Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.09095e+09,'s^-1'), n=0.945416, w0=(301000,'J/mol'), E0=(27519.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.005570283581313703, var=0.27146221678471316, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 1.0585034815239267"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 1.0585034815239267""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 1.0585034815239267
""",
)

entry(
    index = 13,
    label = "Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.64477e+07,'s^-1'), n=1.43279, w0=(301000,'J/mol'), E0=(18863.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.4137206761135945, var=4.541200809277449, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 7.824171175430521"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 7.824171175430521""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 7.824171175430521
""",
)

entry(
    index = 14,
    label = "Root_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Int-4R!H-1COCSCbCbfCdCtN",
    kinetics = ArrheniusBM(A=(8.52e+08,'s^-1'), n=0.89, w0=(301000,'J/mol'), E0=(27513.8,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Int-4R!H-1COCSCbCbfCdCtN',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Int-4R!H-1COCSCbCbfCdCtN
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Int-4R!H-1COCSCbCbfCdCtN
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Int-4R!H-1COCSCbCbfCdCtN
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2.8565e+08,'s^-1'), n=1.2092, w0=(301000,'J/mol'), E0=(21841,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3984913043232801, var=0.1674976106506139, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 1.8217017721514084"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.8217017721514084""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.8217017721514084
""",
)

entry(
    index = 16,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-1COCSCbCbfCdCtN-R",
    kinetics = ArrheniusBM(A=(3.39214e+22,'s^-1'), n=-2.95414, w0=(280000,'J/mol'), E0=(93287.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3719667540891202, var=36.23116161373032, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-1COCSCbCbfCdCtN-R',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-1COCSCbCbfCdCtN-R
    Total Standard Deviation in ln(k): 13.001556653341163"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-1COCSCbCbfCdCtN-R
Total Standard Deviation in ln(k): 13.001556653341163""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-1COCSCbCbfCdCtN-R
Total Standard Deviation in ln(k): 13.001556653341163
""",
)

entry(
    index = 17,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_2CbCbfCdCddCtNO2dS2d->Cdd",
    kinetics = ArrheniusBM(A=(9.291e+11,'s^-1'), n=0.234, w0=(307000,'J/mol'), E0=(90907.6,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_2CbCbfCdCddCtNO2dS2d->Cdd',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_2CbCbfCdCddCtNO2dS2d->Cdd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_2CbCbfCdCddCtNO2dS2d->Cdd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_2CbCbfCdCddCtNO2dS2d->Cdd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2CbCbfCdCddCtNO2dS2d->Cdd",
    kinetics = ArrheniusBM(A=(7.2102e-52,'s^-1'), n=18.0028, w0=(299562,'J/mol'), E0=(-4094.83,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.603457831412561, var=132.8700652633857, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2CbCbfCdCddCtNO2dS2d->Cdd',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2CbCbfCdCddCtNO2dS2d->Cdd
    Total Standard Deviation in ln(k): 24.624662268141762"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2CbCbfCdCddCtNO2dS2d->Cdd
Total Standard Deviation in ln(k): 24.624662268141762""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2CbCbfCdCddCtNO2dS2d->Cdd
Total Standard Deviation in ln(k): 24.624662268141762
""",
)

entry(
    index = 19,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(4.37702e+15,'s^-1'), n=-1.11051, w0=(297154,'J/mol'), E0=(78465.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.20223955199262356, var=13.05077311781442, Tref=1000.0, N=195, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 195 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 7.750416206470323"""),
    rank = 11,
    shortDesc = """BM rule fitted to 195 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 7.750416206470323""",
    longDesc = 
"""
BM rule fitted to 195 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 7.750416206470323
""",
)

entry(
    index = 20,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(6.74834e+10,'s^-1'), n=0.0202481, w0=(300712,'J/mol'), E0=(75427.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.15459148765109906, var=16.93023611095705, Tref=1000.0, N=80, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R',), comment="""BM rule fitted to 80 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 8.637177574966323"""),
    rank = 11,
    shortDesc = """BM rule fitted to 80 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 8.637177574966323""",
    longDesc = 
"""
BM rule fitted to 80 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 8.637177574966323
""",
)

entry(
    index = 21,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C",
    kinetics = ArrheniusBM(A=(6.7637e+08,'s^-1'), n=0.879505, w0=(300361,'J/mol'), E0=(45357.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04050976610814811, var=8.747908141098238, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C',), comment="""BM rule fitted to 18 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C
    Total Standard Deviation in ln(k): 6.031160768829516"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C
Total Standard Deviation in ln(k): 6.031160768829516""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C
Total Standard Deviation in ln(k): 6.031160768829516
""",
)

entry(
    index = 22,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-3R!H->C",
    kinetics = ArrheniusBM(A=(2.724e+10,'s^-1'), n=0.478, w0=(307000,'J/mol'), E0=(104963,'J/mol'), Tmin=(600,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-3R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-3R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-3R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-3R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R",
    kinetics = ArrheniusBM(A=(1.08817e+25,'s^-1'), n=-3.46668, w0=(301000,'J/mol'), E0=(56380.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3054354734534962, var=3.303981180346053, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R',), comment="""BM rule fitted to 12 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R
    Total Standard Deviation in ln(k): 4.411404026984196"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R
Total Standard Deviation in ln(k): 4.411404026984196""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R
Total Standard Deviation in ln(k): 4.411404026984196
""",
)

entry(
    index = 24,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(1.53216e+10,'s^-1'), n=0.8714, w0=(301000,'J/mol'), E0=(29269.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.01732282090885951, var=0.2024514008161267, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 0.9455472001055875"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 0.9455472001055875""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 0.9455472001055875
""",
)

entry(
    index = 25,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(2.28449e+16,'s^-1'), n=-0.867374, w0=(301000,'J/mol'), E0=(5403.85,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7041072017956109, var=1.1015468397837935, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 3.8731752860438666"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 3.8731752860438666""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 3.8731752860438666
""",
)

entry(
    index = 26,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(5.72e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(18364.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Sp-5R!H=4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_N-Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(1.97e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(17058.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_N-Sp-5R!H=4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_N-Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H#4R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R",
    kinetics = ArrheniusBM(A=(1.98e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(22004,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H#4R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H#4R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H#4R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H#4R!H_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 29,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_4R!H-inRing",
    kinetics = ArrheniusBM(A=(9.66972e+11,'s^-1'), n=0.212297, w0=(295250,'J/mol'), E0=(51891.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03016851959504495, var=0.15307859246949268, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_4R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_4R!H-inRing
    Total Standard Deviation in ln(k): 0.8601581002074907"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_4R!H-inRing
Total Standard Deviation in ln(k): 0.8601581002074907""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_4R!H-inRing
Total Standard Deviation in ln(k): 0.8601581002074907
""",
)

entry(
    index = 30,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_N-4R!H-inRing",
    kinetics = ArrheniusBM(A=(1.04952e+10,'s^-1'), n=0.0451934, w0=(301000,'J/mol'), E0=(59742.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=8.607670857836702, var=173.42050493396246, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_N-4R!H-inRing',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_N-4R!H-inRing
    Total Standard Deviation in ln(k): 48.02751344800922"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_N-4R!H-inRing
Total Standard Deviation in ln(k): 48.02751344800922""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_N-4R!H-inRing
Total Standard Deviation in ln(k): 48.02751344800922
""",
)

entry(
    index = 31,
    label = "Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(7.41431e+15,'s^-1'), n=-0.846851, w0=(301000,'J/mol'), E0=(35915.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09883978669442112, var=1.3698797335449475, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-3R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 2.59472042464498"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.59472042464498""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.59472042464498
""",
)

entry(
    index = 32,
    label = "Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(6.18098e+10,'s^-1'), n=0.700128, w0=(301000,'J/mol'), E0=(29799.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.008598119718277845, var=0.27378997040802405, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 1.0705798108757838"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 1.0705798108757838""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 1.0705798108757838
""",
)

entry(
    index = 33,
    label = "Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(4.53e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(22334.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(9.07985e+08,'s^-1'), n=0.931559, w0=(301000,'J/mol'), E0=(26984.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.00442396459325276, var=0.21471553090034456, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_Sp-5R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 0.940057745666803"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 0.940057745666803""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 0.940057745666803
""",
)

entry(
    index = 35,
    label = "Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_N-Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(1.22728e+09,'s^-1'), n=0.96751, w0=(301000,'J/mol'), E0=(27985.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=4.2759607491297814e-05, var=0.8943487563765848, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_N-Sp-5R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 1.8959856812295448"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 1.8959856812295448""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 1.8959856812295448
""",
)

entry(
    index = 36,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-1COCSCbCbfCdCtN-R_Int-4R!H-3R!H",
    kinetics = ArrheniusBM(A=(5.925e+10,'s^-1'), n=0.586, w0=(259000,'J/mol'), E0=(25900,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-1COCSCbCbfCdCtN-R_Int-4R!H-3R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-1COCSCbCbfCdCtN-R_Int-4R!H-3R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-1COCSCbCbfCdCtN-R_Int-4R!H-3R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-1COCSCbCbfCdCtN-R_Int-4R!H-3R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-1COCSCbCbfCdCtN-R_Ext-5R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(4.36e+10,'s^-1'), n=0.44, w0=(301000,'J/mol'), E0=(131415,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-1COCSCbCbfCdCtN-R_Ext-5R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-1COCSCbCbfCdCtN-R_Ext-5R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-1COCSCbCbfCdCtN-R_Ext-5R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-1COCSCbCbfCdCtN-R_Ext-5R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 38,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-1COCSCbCbfCdCtN-R_3R!H-inRing",
    kinetics = ArrheniusBM(A=(8.15385e+14,'s^-1'), n=-0.537569, w0=(301000,'J/mol'), E0=(46122.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-1COCSCbCbfCdCtN-R_3R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-1COCSCbCbfCdCtN-R_3R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-1COCSCbCbfCdCtN-R_3R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-1COCSCbCbfCdCtN-R_3R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-1COCSCbCbfCdCtN-R_N-3R!H-inRing",
    kinetics = ArrheniusBM(A=(1.98168e-18,'s^-1'), n=8.47399, w0=(273000,'J/mol'), E0=(-81631,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.6956643137416205, var=4.463545190931781, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-1COCSCbCbfCdCtN-R_N-3R!H-inRing',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-1COCSCbCbfCdCtN-R_N-3R!H-inRing
    Total Standard Deviation in ln(k): 13.52101335468863"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-1COCSCbCbfCdCtN-R_N-3R!H-inRing
Total Standard Deviation in ln(k): 13.52101335468863""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-1COCSCbCbfCdCtN-R_N-3R!H-inRing
Total Standard Deviation in ln(k): 13.52101335468863
""",
)

entry(
    index = 40,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.8787e-60,'s^-1'), n=20.5891, w0=(299357,'J/mol'), E0=(-7105.82,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.24972203796037998, var=136.11282912115115, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R',), comment="""BM rule fitted to 7 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R
    Total Standard Deviation in ln(k): 24.01616581554136"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R
Total Standard Deviation in ln(k): 24.01616581554136""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R
Total Standard Deviation in ln(k): 24.01616581554136
""",
)

entry(
    index = 41,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing",
    kinetics = ArrheniusBM(A=(5.41822e+22,'s^-1'), n=-3.08776, w0=(261526,'J/mol'), E0=(88908.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.38602323746248324, var=15.147371757937837, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing',), comment="""BM rule fitted to 19 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing
    Total Standard Deviation in ln(k): 8.772261287008215"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing
Total Standard Deviation in ln(k): 8.772261287008215""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing
Total Standard Deviation in ln(k): 8.772261287008215
""",
)

entry(
    index = 42,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing",
    kinetics = ArrheniusBM(A=(1.73214e-09,'s^-1'), n=5.77835, w0=(301000,'J/mol'), E0=(15007.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.40779506976337565, var=4.285594677558484, Tref=1000.0, N=176, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing',), comment="""BM rule fitted to 176 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing
    Total Standard Deviation in ln(k): 5.17474871217456"""),
    rank = 11,
    shortDesc = """BM rule fitted to 176 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing
Total Standard Deviation in ln(k): 5.17474871217456""",
    longDesc = 
"""
BM rule fitted to 176 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing
Total Standard Deviation in ln(k): 5.17474871217456
""",
)

entry(
    index = 43,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.28547e-05,'s^-1'), n=4.36508, w0=(301000,'J/mol'), E0=(-10358.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4991338847183328, var=8.204042565093385, Tref=1000.0, N=27, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 27 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 6.996207754384147"""),
    rank = 11,
    shortDesc = """BM rule fitted to 27 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.996207754384147""",
    longDesc = 
"""
BM rule fitted to 27 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.996207754384147
""",
)

entry(
    index = 44,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(3.7183e+20,'s^-1'), n=-2.75676, w0=(300617,'J/mol'), E0=(102527,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.43487423451057294, var=26.675250004655492, Tref=1000.0, N=30, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H',), comment="""BM rule fitted to 30 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H
    Total Standard Deviation in ln(k): 11.4467222122624"""),
    rank = 11,
    shortDesc = """BM rule fitted to 30 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H
Total Standard Deviation in ln(k): 11.4467222122624""",
    longDesc = 
"""
BM rule fitted to 30 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H
Total Standard Deviation in ln(k): 11.4467222122624
""",
)

entry(
    index = 45,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_1COCSCbCbfCdCtN->Ct",
    kinetics = ArrheniusBM(A=(2.05e+09,'s^-1'), n=0.155, w0=(289500,'J/mol'), E0=(28950,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_1COCSCbCbfCdCtN->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_1COCSCbCbfCdCtN->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_1COCSCbCbfCdCtN->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_1COCSCbCbfCdCtN->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct",
    kinetics = ArrheniusBM(A=(0.00236303,'s^-1'), n=3.93761, w0=(301000,'J/mol'), E0=(41157.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09019380290262172, var=17.492790642686646, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct',), comment="""BM rule fitted to 22 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct
    Total Standard Deviation in ln(k): 8.611298486357892"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct
Total Standard Deviation in ln(k): 8.611298486357892""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct
Total Standard Deviation in ln(k): 8.611298486357892
""",
)

entry(
    index = 47,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.49661e+11,'s^-1'), n=0.160565, w0=(298125,'J/mol'), E0=(57042.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06526749664576621, var=3.461458407068705, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Ext-5R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Ext-5R!H-R
    Total Standard Deviation in ln(k): 3.893797303629088"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 3.893797303629088""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 3.893797303629088
""",
)

entry(
    index = 48,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Ext-1COCSCbCbfCdCtN-R",
    kinetics = ArrheniusBM(A=(6.48e+06,'s^-1'), n=1.25, w0=(301000,'J/mol'), E0=(51111.8,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Ext-1COCSCbCbfCdCtN-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Ext-1COCSCbCbfCdCtN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Ext-1COCSCbCbfCdCtN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Ext-1COCSCbCbfCdCtN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 49,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-4R!H-3C",
    kinetics = ArrheniusBM(A=(1.67082e+07,'s^-1'), n=1.41523, w0=(301000,'J/mol'), E0=(12870.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.004861188433814168, var=0.05005056033725098, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-4R!H-3C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-4R!H-3C
    Total Standard Deviation in ln(k): 0.46071302304878453"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-4R!H-3C
Total Standard Deviation in ln(k): 0.46071302304878453""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-4R!H-3C
Total Standard Deviation in ln(k): 0.46071302304878453
""",
)

entry(
    index = 50,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-5R!H-3C_Sp-5R!H-3C",
    kinetics = ArrheniusBM(A=(11224.9,'s^-1'), n=2.24934, w0=(301000,'J/mol'), E0=(43613,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.189245678739991, var=42.296570890020966, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-5R!H-3C_Sp-5R!H-3C',), comment="""BM rule fitted to 9 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-5R!H-3C_Sp-5R!H-3C
    Total Standard Deviation in ln(k): 21.051137837581226"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-5R!H-3C_Sp-5R!H-3C
Total Standard Deviation in ln(k): 21.051137837581226""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-5R!H-3C_Sp-5R!H-3C
Total Standard Deviation in ln(k): 21.051137837581226
""",
)

entry(
    index = 51,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-5R!H-3C_N-Sp-5R!H-3C",
    kinetics = ArrheniusBM(A=(1.96901e+08,'s^-1'), n=0.937279, w0=(301000,'J/mol'), E0=(59606.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-7.771561172376099e-16, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-5R!H-3C_N-Sp-5R!H-3C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-5R!H-3C_N-Sp-5R!H-3C
    Total Standard Deviation in ln(k): 1.9526535608985173e-15"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-5R!H-3C_N-Sp-5R!H-3C
Total Standard Deviation in ln(k): 1.9526535608985173e-15""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-5R!H-3C_N-Sp-5R!H-3C
Total Standard Deviation in ln(k): 1.9526535608985173e-15
""",
)

entry(
    index = 52,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(1.92263e+23,'s^-1'), n=-3.01978, w0=(301000,'J/mol'), E0=(57939.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2640499078874141, var=2.3179934699662277, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Sp-5R!H=4R!H',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 3.7156427209533556"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 3.7156427209533556""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 3.7156427209533556
""",
)

entry(
    index = 53,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(3.47676e+26,'s^-1'), n=-3.84234, w0=(301000,'J/mol'), E0=(54135.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3084092502715923, var=2.465936435974042, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 3.922993328945506"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 3.922993328945506""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 3.922993328945506
""",
)

entry(
    index = 54,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(4.3656e+10,'s^-1'), n=0.699341, w0=(301000,'J/mol'), E0=(29667.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.01710710428220226, var=0.19609616413197326, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 0.9307344272406816"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.9307344272406816""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.9307344272406816
""",
)

entry(
    index = 55,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(5.21569e+09,'s^-1'), n=1.04737, w0=(301000,'J/mol'), E0=(28844.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.009121788620217107, var=0.286009487861094, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.0950484771209643"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.0950484771209643""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.0950484771209643
""",
)

entry(
    index = 56,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(9.58e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(17329.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Sp-5R!H=4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 57,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-2CbCbfCdCddCtNO2dS2d-R_N-Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(3.31e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(15951.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-2CbCbfCdCddCtNO2dS2d-R_N-Sp-5R!H=4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-2CbCbfCdCddCtNO2dS2d-R_N-Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-2CbCbfCdCddCtNO2dS2d-R_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-2CbCbfCdCddCtNO2dS2d-R_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 58,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_4R!H-inRing_1COCSCbCbfCdCtN->Ct",
    kinetics = ArrheniusBM(A=(8.443e+10,'s^-1'), n=0.474, w0=(289500,'J/mol'), E0=(43573.7,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_4R!H-inRing_1COCSCbCbfCdCtN->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_4R!H-inRing_1COCSCbCbfCdCtN->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_4R!H-inRing_1COCSCbCbfCdCtN->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_4R!H-inRing_1COCSCbCbfCdCtN->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 59,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_4R!H-inRing_N-1COCSCbCbfCdCtN->Ct",
    kinetics = ArrheniusBM(A=(1.126e+14,'s^-1'), n=-0.355, w0=(301000,'J/mol'), E0=(61561.2,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_4R!H-inRing_N-1COCSCbCbfCdCtN->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_4R!H-inRing_N-1COCSCbCbfCdCtN->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_4R!H-inRing_N-1COCSCbCbfCdCtN->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_4R!H-inRing_N-1COCSCbCbfCdCtN->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 60,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R",
    kinetics = ArrheniusBM(A=(7.99e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(21615.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 61,
    label = "Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(5.12473e+10,'s^-1'), n=0.616823, w0=(301000,'J/mol'), E0=(27026.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.013526110093322474, var=0.2726630257431694, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 1.0808006283595655"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 1.0808006283595655""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 1.0808006283595655
""",
)

entry(
    index = 62,
    label = "Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.42e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(11360.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 63,
    label = "Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-7R!H=4R!H",
    kinetics = ArrheniusBM(A=(6.51216e+10,'s^-1'), n=0.655902, w0=(301000,'J/mol'), E0=(29465,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.003505909519626159, var=0.23862443778973919, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-7R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-7R!H=4R!H
    Total Standard Deviation in ln(k): 0.9881058729600023"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-7R!H=4R!H
Total Standard Deviation in ln(k): 0.9881058729600023""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-7R!H=4R!H
Total Standard Deviation in ln(k): 0.9881058729600023
""",
)

entry(
    index = 64,
    label = "Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-7R!H=4R!H",
    kinetics = ArrheniusBM(A=(5.57365e+10,'s^-1'), n=0.750742, w0=(301000,'J/mol'), E0=(30079.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.327358272774688e-05, var=0.8958621509142529, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-7R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-7R!H=4R!H
    Total Standard Deviation in ln(k): 1.8975652477858749"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-7R!H=4R!H
Total Standard Deviation in ln(k): 1.8975652477858749""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-7R!H=4R!H
Total Standard Deviation in ln(k): 1.8975652477858749
""",
)

entry(
    index = 65,
    label = "Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(2.8e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(34655,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 66,
    label = "Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(2.95e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(32974.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 67,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-1COCSCbCbfCdCtN-R_N-3R!H-inRing_1COCSCbCbfCdCtN->Cb",
    kinetics = ArrheniusBM(A=(2.84704e+10,'s^-1'), n=0.407843, w0=(259000,'J/mol'), E0=(65064.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.776356839400252e-15, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-1COCSCbCbfCdCtN-R_N-3R!H-inRing_1COCSCbCbfCdCtN->Cb',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-1COCSCbCbfCdCtN-R_N-3R!H-inRing_1COCSCbCbfCdCtN->Cb
    Total Standard Deviation in ln(k): 4.463208139196613e-15"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-1COCSCbCbfCdCtN-R_N-3R!H-inRing_1COCSCbCbfCdCtN->Cb
Total Standard Deviation in ln(k): 4.463208139196613e-15""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-1COCSCbCbfCdCtN-R_N-3R!H-inRing_1COCSCbCbfCdCtN->Cb
Total Standard Deviation in ln(k): 4.463208139196613e-15
""",
)

entry(
    index = 68,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-1COCSCbCbfCdCtN-R_N-3R!H-inRing_N-1COCSCbCbfCdCtN->Cb",
    kinetics = ArrheniusBM(A=(6.32e+10,'s^-1'), n=0.35, w0=(301000,'J/mol'), E0=(11247.7,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-1COCSCbCbfCdCtN-R_N-3R!H-inRing_N-1COCSCbCbfCdCtN->Cb',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-1COCSCbCbfCdCtN-R_N-3R!H-inRing_N-1COCSCbCbfCdCtN->Cb
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-1COCSCbCbfCdCtN-R_N-3R!H-inRing_N-1COCSCbCbfCdCtN->Cb
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-1COCSCbCbfCdCtN-R_N-3R!H-inRing_N-1COCSCbCbfCdCtN->Cb
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 69,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1COCSCbCbfCdCtN->Ct",
    kinetics = ArrheniusBM(A=(2.992e+11,'s^-1'), n=0.67, w0=(289500,'J/mol'), E0=(28950,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1COCSCbCbfCdCtN->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1COCSCbCbfCdCtN->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1COCSCbCbfCdCtN->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1COCSCbCbfCdCtN->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 70,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_N-1COCSCbCbfCdCtN->Ct",
    kinetics = ArrheniusBM(A=(1.63198e+11,'s^-1'), n=0.128023, w0=(301000,'J/mol'), E0=(167590,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.18032971475273862, var=179.6250226055613, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_N-1COCSCbCbfCdCtN->Ct',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_N-1COCSCbCbfCdCtN->Ct
    Total Standard Deviation in ln(k): 27.32140325396198"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_N-1COCSCbCbfCdCtN->Ct
Total Standard Deviation in ln(k): 27.32140325396198""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_N-1COCSCbCbfCdCtN->Ct
Total Standard Deviation in ln(k): 27.32140325396198
""",
)

entry(
    index = 71,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=3R!H",
    kinetics = ArrheniusBM(A=(1.09612e+22,'s^-1'), n=-2.61991, w0=(259000,'J/mol'), E0=(84702.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.29187948897521554, var=6.797718319207352, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=3R!H',), comment="""BM rule fitted to 7 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=3R!H
    Total Standard Deviation in ln(k): 5.960197915739436"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=3R!H
Total Standard Deviation in ln(k): 5.960197915739436""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=3R!H
Total Standard Deviation in ln(k): 5.960197915739436
""",
)

entry(
    index = 72,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H",
    kinetics = ArrheniusBM(A=(2.27644e+07,'s^-1'), n=1.1612, w0=(263000,'J/mol'), E0=(51217.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.013390514907153197, var=17.603474814811708, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H',), comment="""BM rule fitted to 12 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H
    Total Standard Deviation in ln(k): 8.444810255932683"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H
Total Standard Deviation in ln(k): 8.444810255932683""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H
Total Standard Deviation in ln(k): 8.444810255932683
""",
)

entry(
    index = 73,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(1.50153e+07,'s^-1'), n=1.45289, w0=(301000,'J/mol'), E0=(82795.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.778105967465095e-05, var=3.6558319590830006, Tref=1000.0, N=114, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R',), comment="""BM rule fitted to 114 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R
    Total Standard Deviation in ln(k): 3.8331693819777373"""),
    rank = 11,
    shortDesc = """BM rule fitted to 114 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R
Total Standard Deviation in ln(k): 3.8331693819777373""",
    longDesc = 
"""
BM rule fitted to 114 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R
Total Standard Deviation in ln(k): 3.8331693819777373
""",
)

entry(
    index = 74,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(0.000117072,'s^-1'), n=4.16685, w0=(301000,'J/mol'), E0=(18485.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.15477672378691787, var=5.648072914637428, Tref=1000.0, N=58, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R',), comment="""BM rule fitted to 58 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R
    Total Standard Deviation in ln(k): 5.153274401103107"""),
    rank = 11,
    shortDesc = """BM rule fitted to 58 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R
Total Standard Deviation in ln(k): 5.153274401103107""",
    longDesc = 
"""
BM rule fitted to 58 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R
Total Standard Deviation in ln(k): 5.153274401103107
""",
)

entry(
    index = 75,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(34212.8,'s^-1'), n=1.96906, w0=(301000,'J/mol'), E0=(43009.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.2531813912948866, var=3.5683821790906824, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 6.935673987813629"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 6.935673987813629""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 6.935673987813629
""",
)

entry(
    index = 76,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(0.000583799,'s^-1'), n=3.74871, w0=(301000,'J/mol'), E0=(33508.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.14855376257090772, var=3.491590808518556, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 19 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 4.119258311842052"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 4.119258311842052""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 4.119258311842052
""",
)

entry(
    index = 77,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-5R!H-3R!H",
    kinetics = ArrheniusBM(A=(4080,'s^-1'), n=2.33335, w0=(301000,'J/mol'), E0=(34944.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.1150155255466325, var=2.824914554736722, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-5R!H-3R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-5R!H-3R!H
    Total Standard Deviation in ln(k): 6.171001445011375"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-5R!H-3R!H
Total Standard Deviation in ln(k): 6.171001445011375""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-5R!H-3R!H
Total Standard Deviation in ln(k): 6.171001445011375
""",
)

entry(
    index = 78,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H",
    kinetics = ArrheniusBM(A=(4450.01,'s^-1'), n=1.96955, w0=(301000,'J/mol'), E0=(38869.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.038260646958770496, var=0.10122153796907708, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H
    Total Standard Deviation in ln(k): 0.7339454086534604"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H
Total Standard Deviation in ln(k): 0.7339454086534604""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H
Total Standard Deviation in ln(k): 0.7339454086534604
""",
)

entry(
    index = 79,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H",
    kinetics = ArrheniusBM(A=(2.74933e+09,'s^-1'), n=0.644301, w0=(301000,'J/mol'), E0=(93065.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0004304852593907077, var=0.12894932491034397, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H
    Total Standard Deviation in ln(k): 0.7209722594368648"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H
Total Standard Deviation in ln(k): 0.7209722594368648""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H
Total Standard Deviation in ln(k): 0.7209722594368648
""",
)

entry(
    index = 80,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(2.38562e+15,'s^-1'), n=-1.31378, w0=(300425,'J/mol'), E0=(72632.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.24719545912758212, var=1.9485551152845841, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H',), comment="""BM rule fitted to 20 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 3.419516957568994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 3.419516957568994""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 3.419516957568994
""",
)

entry(
    index = 81,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_N-Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(1.82212e+06,'s^-1'), n=1.46647, w0=(301000,'J/mol'), E0=(110493,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-4.902578058927746, var=347.79453759449495, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_N-Sp-6R!H-5R!H',), comment="""BM rule fitted to 10 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_N-Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 49.7048416127322"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 49.7048416127322""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 49.7048416127322
""",
)

entry(
    index = 82,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_5R!H-inRing",
    kinetics = ArrheniusBM(A=(4.61445e+16,'s^-1'), n=-1.37143, w0=(301000,'J/mol'), E0=(96887.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.205030561419664, var=16.71751517049963, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_5R!H-inRing',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_5R!H-inRing
    Total Standard Deviation in ln(k): 11.224486929482978"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_5R!H-inRing
Total Standard Deviation in ln(k): 11.224486929482978""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_5R!H-inRing
Total Standard Deviation in ln(k): 11.224486929482978
""",
)

entry(
    index = 83,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing",
    kinetics = ArrheniusBM(A=(4.16484e-13,'s^-1'), n=6.67908, w0=(301000,'J/mol'), E0=(-3608.78,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.6186150558715222, var=5.769188710693211, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing',), comment="""BM rule fitted to 18 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing
    Total Standard Deviation in ln(k): 8.882072349994527"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing
Total Standard Deviation in ln(k): 8.882072349994527""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing
Total Standard Deviation in ln(k): 8.882072349994527
""",
)

entry(
    index = 84,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Ext-5R!H-R_1COCSCbCbfCdCtN->Ct",
    kinetics = ArrheniusBM(A=(1.881e+08,'s^-1'), n=1.062, w0=(289500,'J/mol'), E0=(53416.1,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Ext-5R!H-R_1COCSCbCbfCdCtN->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Ext-5R!H-R_1COCSCbCbfCdCtN->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Ext-5R!H-R_1COCSCbCbfCdCtN->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Ext-5R!H-R_1COCSCbCbfCdCtN->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 85,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Ext-5R!H-R_N-1COCSCbCbfCdCtN->Ct",
    kinetics = ArrheniusBM(A=(2.34536e+12,'s^-1'), n=-0.117788, w0=(301000,'J/mol'), E0=(58319.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.029710527431266655, var=6.3899030077378205, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Ext-5R!H-R_N-1COCSCbCbfCdCtN->Ct',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Ext-5R!H-R_N-1COCSCbCbfCdCtN->Ct
    Total Standard Deviation in ln(k): 5.142270511175955"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Ext-5R!H-R_N-1COCSCbCbfCdCtN->Ct
Total Standard Deviation in ln(k): 5.142270511175955""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Ext-5R!H-R_N-1COCSCbCbfCdCtN->Ct
Total Standard Deviation in ln(k): 5.142270511175955
""",
)

entry(
    index = 86,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-4R!H-3C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.85e+09,'s^-1'), n=0.75, w0=(301000,'J/mol'), E0=(14686.4,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-4R!H-3C_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-4R!H-3C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-4R!H-3C_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-4R!H-3C_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 87,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(1.45779e+12,'s^-1'), n=0.165319, w0=(301000,'J/mol'), E0=(34792.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.002824999359713774, var=0.3054684672867636, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R
    Total Standard Deviation in ln(k): 1.1150990647750283"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 1.1150990647750283""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 1.1150990647750283
""",
)

entry(
    index = 88,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.41e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(20651.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 89,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(1.05736e+14,'s^-1'), n=-0.253437, w0=(301000,'J/mol'), E0=(26567.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00938354665276722, var=0.32125941092383564, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R
    Total Standard Deviation in ln(k): 1.159855589109769"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 1.159855589109769""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 1.159855589109769
""",
)

entry(
    index = 90,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(3.48e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(20956.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 91,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(1.05731e+10,'s^-1'), n=0.94173, w0=(301000,'J/mol'), E0=(31241.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.008711706330767389, var=0.5260663532288169, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_Sp-5R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 1.4759317167895907"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 1.4759317167895907""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 1.4759317167895907
""",
)

entry(
    index = 92,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_N-Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(5.34661e+10,'s^-1'), n=0.608246, w0=(301000,'J/mol'), E0=(26719.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.011819111914780262, var=0.5425275801653988, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_N-Sp-5R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_N-Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 1.506313383088425"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 1.506313383088425""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 1.506313383088425
""",
)

entry(
    index = 93,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(9.49154e+09,'s^-1'), n=0.958426, w0=(301000,'J/mol'), E0=(31729.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.00935209196786196, var=0.053141540759598455, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 0.48563825098692154"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 0.48563825098692154""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 0.48563825098692154
""",
)

entry(
    index = 94,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(7.17e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(38069.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-5R!H=4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 95,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(2.48e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(30177.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-5R!H=4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 96,
    label = "Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_Sp-8R!H=4R!H",
    kinetics = ArrheniusBM(A=(7.51765e+10,'s^-1'), n=0.530146, w0=(301000,'J/mol'), E0=(26955.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0016245569548618628, var=0.28702562969298234, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_Sp-8R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_Sp-8R!H=4R!H
    Total Standard Deviation in ln(k): 1.0781140674105063"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_Sp-8R!H=4R!H
Total Standard Deviation in ln(k): 1.0781140674105063""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_Sp-8R!H=4R!H
Total Standard Deviation in ln(k): 1.0781140674105063
""",
)

entry(
    index = 97,
    label = "Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-8R!H=4R!H",
    kinetics = ArrheniusBM(A=(3.12987e+10,'s^-1'), n=0.717174, w0=(301000,'J/mol'), E0=(26979.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.7523741974928294e-05, var=0.8797090670508095, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-8R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-8R!H=4R!H
    Total Standard Deviation in ln(k): 1.8803413342365833"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-8R!H=4R!H
Total Standard Deviation in ln(k): 1.8803413342365833""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-8R!H=4R!H
Total Standard Deviation in ln(k): 1.8803413342365833
""",
)

entry(
    index = 98,
    label = "Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-7R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.87e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(33146.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-7R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-7R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-7R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-7R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 99,
    label = "Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-7R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.97e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(31429.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-7R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-7R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-7R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-7R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 100,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_N-1COCSCbCbfCdCtN->Ct_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(4.25811e+09,'s^-1'), n=0.804888, w0=(301000,'J/mol'), E0=(137780,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.039996627692727424, var=43.50804165884098, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_N-1COCSCbCbfCdCtN->Ct_Ext-3R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_N-1COCSCbCbfCdCtN->Ct_Ext-3R!H-R
    Total Standard Deviation in ln(k): 13.323852081372122"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_N-1COCSCbCbfCdCtN->Ct_Ext-3R!H-R
Total Standard Deviation in ln(k): 13.323852081372122""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_N-1COCSCbCbfCdCtN->Ct_Ext-3R!H-R
Total Standard Deviation in ln(k): 13.323852081372122
""",
)

entry(
    index = 101,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_N-1COCSCbCbfCdCtN->Ct_Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(2.23514e+06,'s^-1'), n=1.08303, w0=(301000,'J/mol'), E0=(211756,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=11.476385067684125, var=299.26347221058796, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_N-1COCSCbCbfCdCtN->Ct_Sp-6R!H-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_N-1COCSCbCbfCdCtN->Ct_Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 63.51551813726193"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_N-1COCSCbCbfCdCtN->Ct_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 63.51551813726193""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_N-1COCSCbCbfCdCtN->Ct_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 63.51551813726193
""",
)

entry(
    index = 102,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_N-1COCSCbCbfCdCtN->Ct_N-Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(1e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(30100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_N-1COCSCbCbfCdCtN->Ct_N-Sp-6R!H-5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_N-1COCSCbCbfCdCtN->Ct_N-Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_N-1COCSCbCbfCdCtN->Ct_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_N-1COCSCbCbfCdCtN->Ct_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 103,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=3R!H_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(3.44163e+11,'s^-1'), n=0.436872, w0=(259000,'J/mol'), E0=(54069.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0006592123094507639, var=0.9216470842205743, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=3R!H_Ext-7R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=3R!H_Ext-7R!H-R
    Total Standard Deviation in ln(k): 1.926251148187319"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=3R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 1.926251148187319""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=3R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 1.926251148187319
""",
)

entry(
    index = 104,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=3R!H_Ext-1COCSCbCbfCdCtN-R",
    kinetics = ArrheniusBM(A=(1.241e+10,'s^-1'), n=0.754, w0=(259000,'J/mol'), E0=(64365.8,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=3R!H_Ext-1COCSCbCbfCdCtN-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=3R!H_Ext-1COCSCbCbfCdCtN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=3R!H_Ext-1COCSCbCbfCdCtN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=3R!H_Ext-1COCSCbCbfCdCtN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 105,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=3R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(0.000188337,'s^-1'), n=4.8063, w0=(259000,'J/mol'), E0=(-38513.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.01747228448123726, var=32.570319773942586, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=3R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=3R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.48500598456916"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=3R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.48500598456916""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=3R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.48500598456916
""",
)

entry(
    index = 106,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(136.678,'s^-1'), n=2.3108, w0=(273000,'J/mol'), E0=(51856.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04608533243177885, var=16.571846345922523, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 8.27677463784878"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 8.27677463784878""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 8.27677463784878
""",
)

entry(
    index = 107,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-1COCSCbCbfCdCtN-R",
    kinetics = ArrheniusBM(A=(272635,'s^-1'), n=1.67471, w0=(259000,'J/mol'), E0=(43832.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.040461491432170635, var=12.682089580794338, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-1COCSCbCbfCdCtN-R',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-1COCSCbCbfCdCtN-R
    Total Standard Deviation in ln(k): 7.240908873736085"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-1COCSCbCbfCdCtN-R
Total Standard Deviation in ln(k): 7.240908873736085""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-1COCSCbCbfCdCtN-R
Total Standard Deviation in ln(k): 7.240908873736085
""",
)

entry(
    index = 108,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_3R!H->C",
    kinetics = ArrheniusBM(A=(5.59275e+10,'s^-1'), n=0.569537, w0=(259000,'J/mol'), E0=(42921.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00957208299639109, var=18.110427446516187, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_3R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_3R!H->C
    Total Standard Deviation in ln(k): 8.555470795325917"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_3R!H->C
Total Standard Deviation in ln(k): 8.555470795325917""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_3R!H->C
Total Standard Deviation in ln(k): 8.555470795325917
""",
)

entry(
    index = 109,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_N-3R!H->C",
    kinetics = ArrheniusBM(A=(7.785e+11,'s^-1'), n=0.342, w0=(265000,'J/mol'), E0=(67814,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_N-3R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_N-3R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_N-3R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_N-3R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 110,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(3.94321e+07,'s^-1'), n=1.33443, w0=(301000,'J/mol'), E0=(84384.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.01085723132261828, var=3.6542178881686977, Tref=1000.0, N=110, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 110 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 3.8595327947914146"""),
    rank = 11,
    shortDesc = """BM rule fitted to 110 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 3.8595327947914146""",
    longDesc = 
"""
BM rule fitted to 110 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 3.8595327947914146
""",
)

entry(
    index = 111,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(3.01823e+07,'s^-1'), n=1.2623, w0=(301000,'J/mol'), E0=(62964,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0013944264516755733, var=0.24460264796958056, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 0.9949918219926736"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.9949918219926736""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.9949918219926736
""",
)

entry(
    index = 112,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(2.49925e+07,'s^-1'), n=1.36128, w0=(301000,'J/mol'), E0=(63543.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.2526545083375107e-05, var=0.8906410654621427, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.8919757774506523"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.8919757774506523""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.8919757774506523
""",
)

entry(
    index = 113,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(4.03867e-06,'s^-1'), n=4.55866, w0=(301000,'J/mol'), E0=(18630.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.18907303441602075, var=8.653806828609616, Tref=1000.0, N=40, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 40 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 6.3724579060600215"""),
    rank = 11,
    shortDesc = """BM rule fitted to 40 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 6.3724579060600215""",
    longDesc = 
"""
BM rule fitted to 40 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 6.3724579060600215
""",
)

entry(
    index = 114,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-5R!H-3R!H",
    kinetics = ArrheniusBM(A=(2.46249e+10,'s^-1'), n=0.708757, w0=(301000,'J/mol'), E0=(57879.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.02208049489238226, var=0.23680677867493966, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-5R!H-3R!H',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-5R!H-3R!H
    Total Standard Deviation in ln(k): 1.0310387863099693"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-5R!H-3R!H
Total Standard Deviation in ln(k): 1.0310387863099693""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-5R!H-3R!H
Total Standard Deviation in ln(k): 1.0310387863099693
""",
)

entry(
    index = 115,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H",
    kinetics = ArrheniusBM(A=(33734.7,'s^-1'), n=1.71681, w0=(301000,'J/mol'), E0=(39995.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.033428926400403215, var=0.3215380154278646, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H
    Total Standard Deviation in ln(k): 1.2207637145971184"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H
Total Standard Deviation in ln(k): 1.2207637145971184""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H
Total Standard Deviation in ln(k): 1.2207637145971184
""",
)

entry(
    index = 116,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H",
    kinetics = ArrheniusBM(A=(1.06532e+10,'s^-1'), n=0.707813, w0=(301000,'J/mol'), E0=(92005.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.012744301144928596, var=1.7144564401085987, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H
    Total Standard Deviation in ln(k): 2.6569659110341903"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H
Total Standard Deviation in ln(k): 2.6569659110341903""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H
Total Standard Deviation in ln(k): 2.6569659110341903
""",
)

entry(
    index = 117,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H",
    kinetics = ArrheniusBM(A=(31.587,'s^-1'), n=2.35402, w0=(301000,'J/mol'), E0=(45970.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06557906480861644, var=0.5491565296222776, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H
    Total Standard Deviation in ln(k): 1.6503823790917889"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H
Total Standard Deviation in ln(k): 1.6503823790917889""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H
Total Standard Deviation in ln(k): 1.6503823790917889
""",
)

entry(
    index = 118,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H",
    kinetics = ArrheniusBM(A=(2.67738e-14,'s^-1'), n=7.10102, w0=(301000,'J/mol'), E0=(28498.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.284210598514262, var=26.50386747339659, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H',), comment="""BM rule fitted to 11 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H
    Total Standard Deviation in ln(k): 11.034855460615764"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H
Total Standard Deviation in ln(k): 11.034855460615764""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H
Total Standard Deviation in ln(k): 11.034855460615764
""",
)

entry(
    index = 119,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2980.82,'s^-1'), n=2.00426, w0=(301000,'J/mol'), E0=(37890.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.3563565371368287, var=4.180143749525445, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 7.506692022533614"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 7.506692022533614""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 7.506692022533614
""",
)

entry(
    index = 120,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(3.55e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(90392.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 121,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_4R!H-inRing",
    kinetics = ArrheniusBM(A=(196017,'s^-1'), n=1.88276, w0=(295250,'J/mol'), E0=(29525,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.5358242832497362, var=1.316646002880678, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_4R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_4R!H-inRing
    Total Standard Deviation in ln(k): 6.159192178949002"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_4R!H-inRing
Total Standard Deviation in ln(k): 6.159192178949002""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_4R!H-inRing
Total Standard Deviation in ln(k): 6.159192178949002
""",
)

entry(
    index = 122,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing",
    kinetics = ArrheniusBM(A=(2.13915e+06,'s^-1'), n=1.21071, w0=(301000,'J/mol'), E0=(46833.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05054860687268546, var=1.026585065710262, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing',), comment="""BM rule fitted to 18 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing
    Total Standard Deviation in ln(k): 2.1582148402878314"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing
Total Standard Deviation in ln(k): 2.1582148402878314""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing
Total Standard Deviation in ln(k): 2.1582148402878314
""",
)

entry(
    index = 123,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_5R!H-inRing_Ext-6R!H-R_Int-7R!H-5R!H",
    kinetics = ArrheniusBM(A=(3.36398e+07,'s^-1'), n=1.17244, w0=(301000,'J/mol'), E0=(203515,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.006255368295709824, var=1.6069781634296842, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_5R!H-inRing_Ext-6R!H-R_Int-7R!H-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_5R!H-inRing_Ext-6R!H-R_Int-7R!H-5R!H
    Total Standard Deviation in ln(k): 2.557052353101604"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_5R!H-inRing_Ext-6R!H-R_Int-7R!H-5R!H
Total Standard Deviation in ln(k): 2.557052353101604""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_5R!H-inRing_Ext-6R!H-R_Int-7R!H-5R!H
Total Standard Deviation in ln(k): 2.557052353101604
""",
)

entry(
    index = 124,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_5R!H-inRing_3R!H-inRing",
    kinetics = ArrheniusBM(A=(5.932e+07,'s^-1'), n=1.035, w0=(301000,'J/mol'), E0=(74396.4,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_5R!H-inRing_3R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_5R!H-inRing_3R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_5R!H-inRing_3R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_5R!H-inRing_3R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 125,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_5R!H-inRing_N-3R!H-inRing",
    kinetics = ArrheniusBM(A=(4.713e+10,'s^-1'), n=0.481, w0=(301000,'J/mol'), E0=(71883.2,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_5R!H-inRing_N-3R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_5R!H-inRing_N-3R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_5R!H-inRing_N-3R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_5R!H-inRing_N-3R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 126,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(91003.3,'s^-1'), n=1.6133, w0=(301000,'J/mol'), E0=(71798.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2723001377466633, var=6.473560135443784, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-5R!H-R',), comment="""BM rule fitted to 12 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-5R!H-R
    Total Standard Deviation in ln(k): 5.784857126616284"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-5R!H-R
Total Standard Deviation in ln(k): 5.784857126616284""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-5R!H-R
Total Standard Deviation in ln(k): 5.784857126616284
""",
)

entry(
    index = 127,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(1.89621e+08,'s^-1'), n=1.03751, w0=(301000,'J/mol'), E0=(52588.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.00765228749611785, var=0.25415231167941665, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-6R!H-R
    Total Standard Deviation in ln(k): 1.029884395657012"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-6R!H-R
Total Standard Deviation in ln(k): 1.029884395657012""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-6R!H-R
Total Standard Deviation in ln(k): 1.029884395657012
""",
)

entry(
    index = 128,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Int-5R!H-3R!H",
    kinetics = ArrheniusBM(A=(46917.2,'s^-1'), n=1.97474, w0=(301000,'J/mol'), E0=(42590.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.29276097790952393, var=0.19474659156015695, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Int-5R!H-3R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Int-5R!H-3R!H
    Total Standard Deviation in ln(k): 1.6202719839591258"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Int-5R!H-3R!H
Total Standard Deviation in ln(k): 1.6202719839591258""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Int-5R!H-3R!H
Total Standard Deviation in ln(k): 1.6202719839591258
""",
)

entry(
    index = 129,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2.6e+07,'s^-1'), n=1.13, w0=(301000,'J/mol'), E0=(47188.9,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 130,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Ext-5R!H-R_N-1COCSCbCbfCdCtN->Ct_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(6.7433e+12,'s^-1'), n=-0.176659, w0=(301000,'J/mol'), E0=(59230.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06733986544384683, var=13.197688841272665, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Ext-5R!H-R_N-1COCSCbCbfCdCtN->Ct_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Ext-5R!H-R_N-1COCSCbCbfCdCtN->Ct_Ext-5R!H-R
    Total Standard Deviation in ln(k): 7.4521222226834"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Ext-5R!H-R_N-1COCSCbCbfCdCtN->Ct_Ext-5R!H-R
Total Standard Deviation in ln(k): 7.4521222226834""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Ext-5R!H-R_N-1COCSCbCbfCdCtN->Ct_Ext-5R!H-R
Total Standard Deviation in ln(k): 7.4521222226834
""",
)

entry(
    index = 131,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H",
    kinetics = ArrheniusBM(A=(6.54886e+12,'s^-1'), n=-0.0661714, w0=(301000,'J/mol'), E0=(35581.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.02642234269757723, var=0.7420036436692553, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H
    Total Standard Deviation in ln(k): 1.7932592413801394"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H
Total Standard Deviation in ln(k): 1.7932592413801394""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H
Total Standard Deviation in ln(k): 1.7932592413801394
""",
)

entry(
    index = 132,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H",
    kinetics = ArrheniusBM(A=(2.53072e+11,'s^-1'), n=0.428141, w0=(301000,'J/mol'), E0=(33722.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0001320083482108111, var=0.8720616725206921, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H
    Total Standard Deviation in ln(k): 1.8724383430518639"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H
Total Standard Deviation in ln(k): 1.8724383430518639""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H
Total Standard Deviation in ln(k): 1.8724383430518639
""",
)

entry(
    index = 133,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H",
    kinetics = ArrheniusBM(A=(9.15065e+14,'s^-1'), n=-0.568565, w0=(301000,'J/mol'), E0=(28183.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2684916712269394, var=0.376767885019329, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H
    Total Standard Deviation in ln(k): 1.905137067817143"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H
Total Standard Deviation in ln(k): 1.905137067817143""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H
Total Standard Deviation in ln(k): 1.905137067817143
""",
)

entry(
    index = 134,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H",
    kinetics = ArrheniusBM(A=(4.88921e+12,'s^-1'), n=0.177787, w0=(301000,'J/mol'), E0=(23733.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06085811911567928, var=0.7130579319742886, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H
    Total Standard Deviation in ln(k): 1.8457634299772712"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H
Total Standard Deviation in ln(k): 1.8457634299772712""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H
Total Standard Deviation in ln(k): 1.8457634299772712
""",
)

entry(
    index = 135,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(3.97e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(41400.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 136,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.37e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(33518.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 137,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(4.18e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(39168.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Sp-5R!H=4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 138,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(1.44e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(31236,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-Sp-5R!H=4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 139,
    label = "Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_Sp-8R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(5.88e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(27110.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_Sp-8R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_Sp-8R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_Sp-8R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_Sp-8R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 140,
    label = "Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-8R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(6.19e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(25322.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-8R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-8R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-8R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-8R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 141,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_N-1COCSCbCbfCdCtN->Ct_Ext-3R!H-R_1Cd-inRing",
    kinetics = ArrheniusBM(A=(6.69e+11,'s^-1'), n=0.22, w0=(301000,'J/mol'), E0=(166035,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_N-1COCSCbCbfCdCtN->Ct_Ext-3R!H-R_1Cd-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_N-1COCSCbCbfCdCtN->Ct_Ext-3R!H-R_1Cd-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_N-1COCSCbCbfCdCtN->Ct_Ext-3R!H-R_1Cd-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_N-1COCSCbCbfCdCtN->Ct_Ext-3R!H-R_1Cd-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 142,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_N-1COCSCbCbfCdCtN->Ct_Ext-3R!H-R_N-1Cd-inRing",
    kinetics = ArrheniusBM(A=(2.27101e+07,'s^-1'), n=1.42496, w0=(301000,'J/mol'), E0=(110897,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-5.215402716989285, var=61.8043701559801, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_N-1COCSCbCbfCdCtN->Ct_Ext-3R!H-R_N-1Cd-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_N-1COCSCbCbfCdCtN->Ct_Ext-3R!H-R_N-1Cd-inRing
    Total Standard Deviation in ln(k): 28.86440319929974"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_N-1COCSCbCbfCdCtN->Ct_Ext-3R!H-R_N-1Cd-inRing
Total Standard Deviation in ln(k): 28.86440319929974""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_N-1COCSCbCbfCdCtN->Ct_Ext-3R!H-R_N-1Cd-inRing
Total Standard Deviation in ln(k): 28.86440319929974
""",
)

entry(
    index = 143,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=3R!H_Ext-7R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(9.423e+09,'s^-1'), n=0.834, w0=(259000,'J/mol'), E0=(48878.6,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=3R!H_Ext-7R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=3R!H_Ext-7R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=3R!H_Ext-7R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=3R!H_Ext-7R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 144,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=3R!H_Ext-3R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(3.233e+11,'s^-1'), n=0.39, w0=(259000,'J/mol'), E0=(92284.7,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=3R!H_Ext-3R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=3R!H_Ext-3R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=3R!H_Ext-3R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=3R!H_Ext-3R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 145,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R_1COCSCbCbfCdCtN->Cb",
    kinetics = ArrheniusBM(A=(2.28032e-10,'s^-1'), n=5.56493, w0=(259000,'J/mol'), E0=(5689.66,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0060518631342186225, var=51.55205822785766, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R_1COCSCbCbfCdCtN->Cb',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R_1COCSCbCbfCdCtN->Cb
    Total Standard Deviation in ln(k): 14.409155828604547"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R_1COCSCbCbfCdCtN->Cb
Total Standard Deviation in ln(k): 14.409155828604547""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R_1COCSCbCbfCdCtN->Cb
Total Standard Deviation in ln(k): 14.409155828604547
""",
)

entry(
    index = 146,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R_N-1COCSCbCbfCdCtN->Cb",
    kinetics = ArrheniusBM(A=(1.19e+11,'s^-1'), n=0.08, w0=(301000,'J/mol'), E0=(87554.3,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R_N-1COCSCbCbfCdCtN->Cb',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R_N-1COCSCbCbfCdCtN->Cb
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R_N-1COCSCbCbfCdCtN->Cb
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R_N-1COCSCbCbfCdCtN->Cb
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 147,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-1COCSCbCbfCdCtN-R_Ext-6R!H-R_Int-9R!H-5R!H_Int-9R!H-7R!H",
    kinetics = ArrheniusBM(A=(231677,'s^-1'), n=1.30099, w0=(259000,'J/mol'), E0=(53318.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-1COCSCbCbfCdCtN-R_Ext-6R!H-R_Int-9R!H-5R!H_Int-9R!H-7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-1COCSCbCbfCdCtN-R_Ext-6R!H-R_Int-9R!H-5R!H_Int-9R!H-7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-1COCSCbCbfCdCtN-R_Ext-6R!H-R_Int-9R!H-5R!H_Int-9R!H-7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-1COCSCbCbfCdCtN-R_Ext-6R!H-R_Int-9R!H-5R!H_Int-9R!H-7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 148,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.12951e+06,'s^-1'), n=1.40297, w0=(259000,'J/mol'), E0=(49301.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 149,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-1COCSCbCbfCdCtN-R_Int-7R!H-5R!H",
    kinetics = ArrheniusBM(A=(905.58,'s^-1'), n=2.15236, w0=(259000,'J/mol'), E0=(45992.7,'J/mol'), Tmin=(500,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-1COCSCbCbfCdCtN-R_Int-7R!H-5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-1COCSCbCbfCdCtN-R_Int-7R!H-5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-1COCSCbCbfCdCtN-R_Int-7R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-1COCSCbCbfCdCtN-R_Int-7R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 150,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-1COCSCbCbfCdCtN-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(4.80432e+06,'s^-1'), n=1.55545, w0=(259000,'J/mol'), E0=(38378.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00029827683003114575, var=0.9571087745642144, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-1COCSCbCbfCdCtN-R_Ext-7R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-1COCSCbCbfCdCtN-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 1.962020581679106"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-1COCSCbCbfCdCtN-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 1.962020581679106""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-1COCSCbCbfCdCtN-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 1.962020581679106
""",
)

entry(
    index = 151,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_3R!H->C_Int-7R!H-1COCSCbCbfCdCtN_Ext-7R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(2.93867e+07,'s^-1'), n=1.59576, w0=(259000,'J/mol'), E0=(25609.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_3R!H->C_Int-7R!H-1COCSCbCbfCdCtN_Ext-7R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_3R!H->C_Int-7R!H-1COCSCbCbfCdCtN_Ext-7R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_3R!H->C_Int-7R!H-1COCSCbCbfCdCtN_Ext-7R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_3R!H->C_Int-7R!H-1COCSCbCbfCdCtN_Ext-7R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 152,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1.10695e+08,'s^-1'), n=1.15372, w0=(301000,'J/mol'), E0=(79652.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.014286490403265148, var=4.966992684455259, Tref=1000.0, N=76, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 76 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 4.503798846012626"""),
    rank = 11,
    shortDesc = """BM rule fitted to 76 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 4.503798846012626""",
    longDesc = 
"""
BM rule fitted to 76 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 4.503798846012626
""",
)

entry(
    index = 153,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H",
    kinetics = ArrheniusBM(A=(2.26515e+09,'s^-1'), n=0.964509, w0=(301000,'J/mol'), E0=(65154.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.009228365525366728, var=0.3109978543026534, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H
    Total Standard Deviation in ln(k): 1.1411710991585706"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H
Total Standard Deviation in ln(k): 1.1411710991585706""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H
Total Standard Deviation in ln(k): 1.1411710991585706
""",
)

entry(
    index = 154,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H",
    kinetics = ArrheniusBM(A=(888.269,'s^-1'), n=2.22879, w0=(301000,'J/mol'), E0=(18248.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.14088617644121207, var=0.9963574171791729, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H',), comment="""BM rule fitted to 12 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H
    Total Standard Deviation in ln(k): 2.3550659075349603"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H
Total Standard Deviation in ln(k): 2.3550659075349603""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H
Total Standard Deviation in ln(k): 2.3550659075349603
""",
)

entry(
    index = 155,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H",
    kinetics = ArrheniusBM(A=(1.87912e+10,'s^-1'), n=0.6664, w0=(301000,'J/mol'), E0=(104361,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.013090627536269694, var=0.2565739351087866, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H',), comment="""BM rule fitted to 14 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H
    Total Standard Deviation in ln(k): 1.0483520438075122"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H
Total Standard Deviation in ln(k): 1.0483520438075122""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H
Total Standard Deviation in ln(k): 1.0483520438075122
""",
)

entry(
    index = 156,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.11e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(72264.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 157,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.17e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(70529.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 158,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H",
    kinetics = ArrheniusBM(A=(0.000120299,'s^-1'), n=3.96336, w0=(301000,'J/mol'), E0=(-1823.84,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12797232381928222, var=1.90692966141716, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H',), comment="""BM rule fitted to 16 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H
    Total Standard Deviation in ln(k): 3.089909726982329"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H
Total Standard Deviation in ln(k): 3.089909726982329""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H
Total Standard Deviation in ln(k): 3.089909726982329
""",
)

entry(
    index = 159,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(7.75021e+17,'s^-1'), n=-1.63987, w0=(301000,'J/mol'), E0=(98005.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.19722937199130583, var=7.91120734310125, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 20 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 6.134243185428128"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.134243185428128""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.134243185428128
""",
)

entry(
    index = 160,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.45044e+09,'s^-1'), n=1.12351, w0=(301000,'J/mol'), E0=(52286.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.006570588214302276, var=0.1492437062799305, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 0.7909797337858375"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 0.7909797337858375""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 0.7909797337858375
""",
)

entry(
    index = 161,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(2.26e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(62960.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 162,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(7.81e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(55842.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 163,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(4.74772e+10,'s^-1'), n=0.574276, w0=(301000,'J/mol'), E0=(57844.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0005540984563063583, var=0.20264207511403293, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 0.9038394064750148"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 0.9038394064750148""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 0.9038394064750148
""",
)

entry(
    index = 164,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-5R!H-3R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.79e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(61099.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-5R!H-3R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-5R!H-3R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-5R!H-3R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-5R!H-3R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 165,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(3.03779e+09,'s^-1'), n=0.514048, w0=(301000,'J/mol'), E0=(55653.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.011941076661397146, var=0.414592130657874, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 1.3208281470912193"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.3208281470912193""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.3208281470912193
""",
)

entry(
    index = 166,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(96935.7,'s^-1'), n=1.57359, w0=(301000,'J/mol'), E0=(40218.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.012412163774521385, var=0.00035005677044125876, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 0.06869454176500632"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 0.06869454176500632""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 0.06869454176500632
""",
)

entry(
    index = 167,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(9.52922e+10,'s^-1'), n=0.499551, w0=(301000,'J/mol'), E0=(92509.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.008552511411544476, var=0.12153796152601967, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 0.720385379534774"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 0.720385379534774""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 0.720385379534774
""",
)

entry(
    index = 168,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(2.98e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(100889,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 169,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(1.2544e+07,'s^-1'), n=1.16176, w0=(301000,'J/mol'), E0=(80308.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.010334419008899372, var=1.4184838986700232, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R
    Total Standard Deviation in ln(k): 2.413607793656036"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 2.413607793656036""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 2.413607793656036
""",
)

entry(
    index = 170,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(17.8177,'s^-1'), n=2.38355, w0=(301000,'J/mol'), E0=(40649.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.2347748574941748, var=3.4643283087411767, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 6.833803884591368"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.833803884591368""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.833803884591368
""",
)

entry(
    index = 171,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_3R!H-inRing",
    kinetics = ArrheniusBM(A=(1e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(30100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_3R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_3R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_3R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_3R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 172,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing",
    kinetics = ArrheniusBM(A=(6.01713e+16,'s^-1'), n=-1.6161, w0=(301000,'J/mol'), E0=(99656.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.20400127411110786, var=9.489425255733714, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing',), comment="""BM rule fitted to 10 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing
    Total Standard Deviation in ln(k): 6.688134526591891"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing
Total Standard Deviation in ln(k): 6.688134526591891""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing
Total Standard Deviation in ln(k): 6.688134526591891
""",
)

entry(
    index = 173,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_4R!H-inRing_1COCSCbCbfCdCtN->Ct",
    kinetics = ArrheniusBM(A=(1.42e+11,'s^-1'), n=0.258, w0=(289500,'J/mol'), E0=(28950,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_4R!H-inRing_1COCSCbCbfCdCtN->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_4R!H-inRing_1COCSCbCbfCdCtN->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_4R!H-inRing_1COCSCbCbfCdCtN->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_4R!H-inRing_1COCSCbCbfCdCtN->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 174,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_4R!H-inRing_N-1COCSCbCbfCdCtN->Ct",
    kinetics = ArrheniusBM(A=(6.311e+09,'s^-1'), n=0.537, w0=(301000,'J/mol'), E0=(30100,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_4R!H-inRing_N-1COCSCbCbfCdCtN->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_4R!H-inRing_N-1COCSCbCbfCdCtN->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_4R!H-inRing_N-1COCSCbCbfCdCtN->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_4R!H-inRing_N-1COCSCbCbfCdCtN->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 175,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing_Ext-1COCSCbCbfCdCtN-R",
    kinetics = ArrheniusBM(A=(184000,'s^-1'), n=1.4, w0=(301000,'J/mol'), E0=(52693.1,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing_Ext-1COCSCbCbfCdCtN-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing_Ext-1COCSCbCbfCdCtN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing_Ext-1COCSCbCbfCdCtN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing_Ext-1COCSCbCbfCdCtN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 176,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(40683.1,'s^-1'), n=1.71232, w0=(301000,'J/mol'), E0=(41686.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0018539796123168322, var=0.015978837537474706, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing_Ext-4R!H-R
    Total Standard Deviation in ln(k): 0.25807164268015687"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.25807164268015687""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.25807164268015687
""",
)

entry(
    index = 177,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(72220.9,'s^-1'), n=1.6363, w0=(301000,'J/mol'), E0=(39718.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0017952159058182728, var=0.0036340586183760135, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing_Ext-5R!H-R
    Total Standard Deviation in ln(k): 0.12536234549921912"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.12536234549921912""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.12536234549921912
""",
)

entry(
    index = 178,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(60370.2,'s^-1'), n=1.63267, w0=(301000,'J/mol'), E0=(38671.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0013317020727281878, var=0.6679269765401225, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing_Ext-6R!H-R
    Total Standard Deviation in ln(k): 1.6417518034055345"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing_Ext-6R!H-R
Total Standard Deviation in ln(k): 1.6417518034055345""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing_Ext-6R!H-R
Total Standard Deviation in ln(k): 1.6417518034055345
""",
)

entry(
    index = 179,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing_Sp-6R!H-3R!H",
    kinetics = ArrheniusBM(A=(465716,'s^-1'), n=1.42934, w0=(301000,'J/mol'), E0=(44693.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3292219847419922, var=4.161322094198857, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing_Sp-6R!H-3R!H',), comment="""BM rule fitted to 9 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing_Sp-6R!H-3R!H
    Total Standard Deviation in ln(k): 4.916713921181709"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing_Sp-6R!H-3R!H
Total Standard Deviation in ln(k): 4.916713921181709""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing_Sp-6R!H-3R!H
Total Standard Deviation in ln(k): 4.916713921181709
""",
)

entry(
    index = 180,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing_N-Sp-6R!H-3R!H",
    kinetics = ArrheniusBM(A=(2.46301e+08,'s^-1'), n=0.668371, w0=(301000,'J/mol'), E0=(56547.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.0128758627126295, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing_N-Sp-6R!H-3R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing_N-Sp-6R!H-3R!H
    Total Standard Deviation in ln(k): 5.057477041991532"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing_N-Sp-6R!H-3R!H
Total Standard Deviation in ln(k): 5.057477041991532""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing_N-Sp-6R!H-3R!H
Total Standard Deviation in ln(k): 5.057477041991532
""",
)

entry(
    index = 181,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_5R!H-inRing_Ext-6R!H-R_Int-7R!H-5R!H_4R!H-inRing",
    kinetics = ArrheniusBM(A=(1e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(211407,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_5R!H-inRing_Ext-6R!H-R_Int-7R!H-5R!H_4R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_5R!H-inRing_Ext-6R!H-R_Int-7R!H-5R!H_4R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_5R!H-inRing_Ext-6R!H-R_Int-7R!H-5R!H_4R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_5R!H-inRing_Ext-6R!H-R_Int-7R!H-5R!H_4R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 182,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_5R!H-inRing_Ext-6R!H-R_Int-7R!H-5R!H_N-4R!H-inRing",
    kinetics = ArrheniusBM(A=(1e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(219004,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_5R!H-inRing_Ext-6R!H-R_Int-7R!H-5R!H_N-4R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_5R!H-inRing_Ext-6R!H-R_Int-7R!H-5R!H_N-4R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_5R!H-inRing_Ext-6R!H-R_Int-7R!H-5R!H_N-4R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_5R!H-inRing_Ext-6R!H-R_Int-7R!H-5R!H_N-4R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 183,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-5R!H-R_Sp-6R!H-3R!H",
    kinetics = ArrheniusBM(A=(4.2722e+06,'s^-1'), n=1.13308, w0=(301000,'J/mol'), E0=(75574.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06954861879510306, var=6.248140281064059, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-5R!H-R_Sp-6R!H-3R!H',), comment="""BM rule fitted to 11 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-5R!H-R_Sp-6R!H-3R!H
    Total Standard Deviation in ln(k): 5.185837262606732"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-5R!H-R_Sp-6R!H-3R!H
Total Standard Deviation in ln(k): 5.185837262606732""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-5R!H-R_Sp-6R!H-3R!H
Total Standard Deviation in ln(k): 5.185837262606732
""",
)

entry(
    index = 184,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-5R!H-R_N-Sp-6R!H-3R!H",
    kinetics = ArrheniusBM(A=(1e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(30100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-5R!H-R_N-Sp-6R!H-3R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-5R!H-R_N-Sp-6R!H-3R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-5R!H-R_N-Sp-6R!H-3R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-5R!H-R_N-Sp-6R!H-3R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 185,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-6R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(2.15e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(63021.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-6R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-6R!H-R_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-6R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-6R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 186,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-6R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(7.43e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(56583.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-6R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-6R!H-R_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-6R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-6R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 187,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Ext-5R!H-R_N-1COCSCbCbfCdCtN->Ct_Ext-5R!H-R_Int-4R!H-3C",
    kinetics = ArrheniusBM(A=(2.54e+10,'s^-1'), n=0.69, w0=(301000,'J/mol'), E0=(53221.8,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Ext-5R!H-R_N-1COCSCbCbfCdCtN->Ct_Ext-5R!H-R_Int-4R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Ext-5R!H-R_N-1COCSCbCbfCdCtN->Ct_Ext-5R!H-R_Int-4R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Ext-5R!H-R_N-1COCSCbCbfCdCtN->Ct_Ext-5R!H-R_Int-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Ext-5R!H-R_N-1COCSCbCbfCdCtN->Ct_Ext-5R!H-R_Int-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 188,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(5.82e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(33559.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 189,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(6.13e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(30801.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 190,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.44e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(19820.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 191,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.52e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(12471.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-1COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 192,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R_1COCSCbCbfCdCtN->Cb_Int-7R!H-4R!H",
    kinetics = ArrheniusBM(A=(2.27635e+06,'s^-1'), n=1.20282, w0=(259000,'J/mol'), E0=(50810.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R_1COCSCbCbfCdCtN->Cb_Int-7R!H-4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R_1COCSCbCbfCdCtN->Cb_Int-7R!H-4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R_1COCSCbCbfCdCtN->Cb_Int-7R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R_1COCSCbCbfCdCtN->Cb_Int-7R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 193,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-1COCSCbCbfCdCtN-R_Ext-7R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(966131,'s^-1'), n=1.86605, w0=(259000,'J/mol'), E0=(46209.4,'J/mol'), Tmin=(500,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-1COCSCbCbfCdCtN-R_Ext-7R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-1COCSCbCbfCdCtN-R_Ext-7R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-1COCSCbCbfCdCtN-R_Ext-7R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=3R!H_Ext-1COCSCbCbfCdCtN-R_Ext-7R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 194,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H",
    kinetics = ArrheniusBM(A=(1.16542e+11,'s^-1'), n=0.228711, w0=(301000,'J/mol'), E0=(86602.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08772502303586381, var=0.9858687739525692, Tref=1000.0, N=28, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H',), comment="""BM rule fitted to 28 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H
    Total Standard Deviation in ln(k): 2.2109346280589226"""),
    rank = 11,
    shortDesc = """BM rule fitted to 28 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H
Total Standard Deviation in ln(k): 2.2109346280589226""",
    longDesc = 
"""
BM rule fitted to 28 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H
Total Standard Deviation in ln(k): 2.2109346280589226
""",
)

entry(
    index = 195,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.00502e+09,'s^-1'), n=0.875771, w0=(301000,'J/mol'), E0=(85999.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0006708612126859182, var=6.295563914310492, Tref=1000.0, N=40, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 40 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 5.031758814927284"""),
    rank = 11,
    shortDesc = """BM rule fitted to 40 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 5.031758814927284""",
    longDesc = 
"""
BM rule fitted to 40 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 5.031758814927284
""",
)

entry(
    index = 196,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.85282e+08,'s^-1'), n=1.28823, w0=(301000,'J/mol'), E0=(64836.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.003960691824752335, var=0.1470703760042366, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 0.7787624910327837"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.7787624910327837""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.7787624910327837
""",
)

entry(
    index = 197,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.10988e+08,'s^-1'), n=1.43139, w0=(301000,'J/mol'), E0=(65458.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0012836583595059803, var=0.2854252215584198, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.0742590382067003"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.0742590382067003""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.0742590382067003
""",
)

entry(
    index = 198,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.9276e+09,'s^-1'), n=0.929295, w0=(301000,'J/mol'), E0=(64356.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.013750472370697037, var=0.276395061932914, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 1.0885040729930324"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.0885040729930324""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.0885040729930324
""",
)

entry(
    index = 199,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(2.29622e+09,'s^-1'), n=0.979983, w0=(301000,'J/mol'), E0=(65373.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0011442113882921517, var=0.26227892729126606, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.029563382412674"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.029563382412674""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.029563382412674
""",
)

entry(
    index = 200,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.60156e+09,'s^-1'), n=1.10104, w0=(301000,'J/mol'), E0=(65830.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.0204473452922223e-05, var=0.8862713147752092, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.8873230147889108"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.8873230147889108""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.8873230147889108
""",
)

entry(
    index = 201,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.39424e+09,'s^-1'), n=0.556198, w0=(301000,'J/mol'), E0=(55375.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.022331382814247853, var=0.38539456585251236, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 1.3006516476437238"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.3006516476437238""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.3006516476437238
""",
)

entry(
    index = 202,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(9.19391e+06,'s^-1'), n=0.961477, w0=(301000,'J/mol'), E0=(50887.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0061682323683784745, var=0.05077367337677354, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 0.46722531308767884"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.46722531308767884""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.46722531308767884
""",
)

entry(
    index = 203,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.53278e+07,'s^-1'), n=0.961764, w0=(301000,'J/mol'), E0=(51469.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=8.882097112640255e-05, var=0.9103453622999381, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.9129814078275085"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.9129814078275085""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.9129814078275085
""",
)

entry(
    index = 204,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_2CbCbfCdCddCtNO2dS2d-inRing",
    kinetics = ArrheniusBM(A=(4.39374e+10,'s^-1'), n=0.57269, w0=(301000,'J/mol'), E0=(106019,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.7763568394002489e-15, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_2CbCbfCdCddCtNO2dS2d-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_2CbCbfCdCddCtNO2dS2d-inRing
    Total Standard Deviation in ln(k): 4.463208139196605e-15"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_2CbCbfCdCddCtNO2dS2d-inRing
Total Standard Deviation in ln(k): 4.463208139196605e-15""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_2CbCbfCdCddCtNO2dS2d-inRing
Total Standard Deviation in ln(k): 4.463208139196605e-15
""",
)

entry(
    index = 205,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing",
    kinetics = ArrheniusBM(A=(1.78856e+08,'s^-1'), n=1.18231, w0=(301000,'J/mol'), E0=(95602.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0255455889986089, var=1.2964183065836339, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing',), comment="""BM rule fitted to 12 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing
    Total Standard Deviation in ln(k): 2.3467836040130066"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing
Total Standard Deviation in ln(k): 2.3467836040130066""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing
Total Standard Deviation in ln(k): 2.3467836040130066
""",
)

entry(
    index = 206,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(0.000314825,'s^-1'), n=3.83369, w0=(301000,'J/mol'), E0=(794.878,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.909844897386684, var=19.665850404104983, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 16.20140541695909"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 16.20140541695909""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 16.20140541695909
""",
)

entry(
    index = 207,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.08711e+11,'s^-1'), n=0.293932, w0=(301000,'J/mol'), E0=(83012.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04102646390331378, var=1.0173884201862333, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 2.125171116356609"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.125171116356609""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.125171116356609
""",
)

entry(
    index = 208,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(9.99368e+15,'s^-1'), n=-1.1132, w0=(301000,'J/mol'), E0=(93630.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.15039983067986365, var=5.0135273809529, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H',), comment="""BM rule fitted to 10 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 4.866672787213734"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 4.866672787213734""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 4.866672787213734
""",
)

entry(
    index = 209,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(4.28528e+19,'s^-1'), n=-2.12452, w0=(301000,'J/mol'), E0=(101999,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.22728620082431011, var=13.80079185091669, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H',), comment="""BM rule fitted to 10 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 8.018544797263525"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 8.018544797263525""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 8.018544797263525
""",
)

entry(
    index = 210,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(3.79e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(65186.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 211,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_N-Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(1.31e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(58117.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_N-Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_N-Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 212,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(5.62e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(55941,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 213,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(7.03913e+08,'s^-1'), n=0.635277, w0=(301000,'J/mol'), E0=(53325.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0004578765828920934, var=0.4109969623386361, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 1.286366952284899"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.286366952284899""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.286366952284899
""",
)

entry(
    index = 214,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(5.89e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(58432.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 215,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(5.2642e+11,'s^-1'), n=0.221845, w0=(301000,'J/mol'), E0=(91880.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-9.536571581324116e-06, var=0.26426699795692804, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 1.0305962370601296"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.0305962370601296""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.0305962370601296
""",
)

entry(
    index = 216,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.99e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(98457,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 217,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(5.57636e+07,'s^-1'), n=0.932712, w0=(301000,'J/mol'), E0=(81061.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0003943183632176365, var=9.201227445488232, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 6.082058927089304"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.082058927089304""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.082058927089304
""",
)

entry(
    index = 218,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Sp-9R!H=7R!H",
    kinetics = ArrheniusBM(A=(2.42e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(86735.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Sp-9R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Sp-9R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Sp-9R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Sp-9R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 219,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_N-Sp-9R!H=7R!H",
    kinetics = ArrheniusBM(A=(8.36e+09,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(78507.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_N-Sp-9R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_N-Sp-9R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_N-Sp-9R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_N-Sp-9R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 220,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H",
    kinetics = ArrheniusBM(A=(5.48609e+14,'s^-1'), n=-1.04543, w0=(301000,'J/mol'), E0=(94918.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12712956119120697, var=7.608112959369094, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H
    Total Standard Deviation in ln(k): 5.849043276618438"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H
Total Standard Deviation in ln(k): 5.849043276618438""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H
Total Standard Deviation in ln(k): 5.849043276618438
""",
)

entry(
    index = 221,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H",
    kinetics = ArrheniusBM(A=(4.59239e+18,'s^-1'), n=-2.14165, w0=(301000,'J/mol'), E0=(103988,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.19781149873198342, var=20.814060710798255, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H
    Total Standard Deviation in ln(k): 9.643102284089762"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H
Total Standard Deviation in ln(k): 9.643102284089762""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H
Total Standard Deviation in ln(k): 9.643102284089762
""",
)

entry(
    index = 222,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing_Ext-4R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.18e+07,'s^-1'), n=0.99, w0=(301000,'J/mol'), E0=(48077.9,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing_Ext-4R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing_Ext-4R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 223,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(3.37e+07,'s^-1'), n=0.85, w0=(301000,'J/mol'), E0=(46777.4,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 224,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing_Ext-6R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(7.05e+06,'s^-1'), n=1.03, w0=(301000,'J/mol'), E0=(41988,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing_Ext-6R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing_Ext-6R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing_Ext-6R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-4R!H-inRing_Ext-6R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 225,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-5R!H-R_Sp-6R!H-3R!H_Int-7R!H-6R!H_Sp-7R!H-6R!H",
    kinetics = ArrheniusBM(A=(51315.8,'s^-1'), n=1.49196, w0=(301000,'J/mol'), E0=(60389.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6204738967727678, var=15.621556329688683, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-5R!H-R_Sp-6R!H-3R!H_Int-7R!H-6R!H_Sp-7R!H-6R!H',), comment="""BM rule fitted to 10 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-5R!H-R_Sp-6R!H-3R!H_Int-7R!H-6R!H_Sp-7R!H-6R!H
    Total Standard Deviation in ln(k): 9.482517529356283"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-5R!H-R_Sp-6R!H-3R!H_Int-7R!H-6R!H_Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 9.482517529356283""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-5R!H-R_Sp-6R!H-3R!H_Int-7R!H-6R!H_Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 9.482517529356283
""",
)

entry(
    index = 226,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-5R!H-R_Sp-6R!H-3R!H_Int-7R!H-6R!H_N-Sp-7R!H-6R!H",
    kinetics = ArrheniusBM(A=(2.5578e+10,'s^-1'), n=0.210583, w0=(301000,'J/mol'), E0=(92746.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-5R!H-R_Sp-6R!H-3R!H_Int-7R!H-6R!H_N-Sp-7R!H-6R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-5R!H-R_Sp-6R!H-3R!H_Int-7R!H-6R!H_N-Sp-7R!H-6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-5R!H-R_Sp-6R!H-3R!H_Int-7R!H-6R!H_N-Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-5R!H-R_Sp-6R!H-3R!H_Int-7R!H-6R!H_N-Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 227,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(3.79177e+12,'s^-1'), n=-0.171413, w0=(301000,'J/mol'), E0=(91657.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12311189548306858, var=1.00420243423803, Tref=1000.0, N=24, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R',), comment="""BM rule fitted to 24 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 2.318269415326708"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.318269415326708""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.318269415326708
""",
)

entry(
    index = 228,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(8.95438e+06,'s^-1'), n=1.17401, w0=(301000,'J/mol'), E0=(66906.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.858281319607548, var=0.030521375809949142, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 7.531845951268982"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 7.531845951268982""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 7.531845951268982
""",
)

entry(
    index = 229,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.19475e+07,'s^-1'), n=1.20316, w0=(301000,'J/mol'), E0=(67261.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.7828044883667897, var=0.7583875753606414, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 8.73780365723938"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 8.73780365723938""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 8.73780365723938
""",
)

entry(
    index = 230,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(8.21232e+10,'s^-1'), n=0.315129, w0=(301000,'J/mol'), E0=(91818.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.062149106928244276, var=3.688075685114382, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H',), comment="""BM rule fitted to 20 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 4.006119603140224"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 4.006119603140224""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 4.006119603140224
""",
)

entry(
    index = 231,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(569693,'s^-1'), n=1.81847, w0=(301000,'J/mol'), E0=(76707.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09845475601048409, var=9.760634499236819, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H',), comment="""BM rule fitted to 20 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 6.510569930009723"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 6.510569930009723""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 6.510569930009723
""",
)

entry(
    index = 232,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(9.46112e+07,'s^-1'), n=1.43714, w0=(301000,'J/mol'), E0=(67007.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.001785034913054568, var=0.4113520585173574, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_Sp-9R!H=8R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 1.2902566064892482"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 1.2902566064892482""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 1.2902566064892482
""",
)

entry(
    index = 233,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_N-Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(2.6145e+08,'s^-1'), n=1.18012, w0=(301000,'J/mol'), E0=(62325,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0016304613083146817, var=0.39541936686895485, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_N-Sp-9R!H=8R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_N-Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 1.264721758516651"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 1.264721758516651""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 1.264721758516651
""",
)

entry(
    index = 234,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.93409e+08,'s^-1'), n=1.34583, w0=(301000,'J/mol'), E0=(67977.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0021035441095094915, var=0.07140553614019061, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 0.5409868720150801"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 0.5409868720150801""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 0.5409868720150801
""",
)

entry(
    index = 235,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(2.84e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(76269.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Sp-9R!H=8R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 236,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_N-Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(9.8e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(68951.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_N-Sp-9R!H=8R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_N-Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 237,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(2.50086e+09,'s^-1'), n=0.858133, w0=(301000,'J/mol'), E0=(64184,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0009099447885058112, var=0.27849951000157613, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.0602461939868872"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.0602461939868872""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.0602461939868872
""",
)

entry(
    index = 238,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.43917e+09,'s^-1'), n=1.00442, w0=(301000,'J/mol'), E0=(64494.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=8.171684915377137e-06, var=0.8893913685504728, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.890637035307336"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.890637035307336""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.890637035307336
""",
)

entry(
    index = 239,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(7.41e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(70621.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 240,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(7.81e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(68863.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 241,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(9.50689e+07,'s^-1'), n=0.824298, w0=(301000,'J/mol'), E0=(50919.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.007199515990337169, var=0.2652579815407888, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 1.0505919924673437"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.0505919924673437""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.0505919924673437
""",
)

entry(
    index = 242,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.39707e+08,'s^-1'), n=0.871081, w0=(301000,'J/mol'), E0=(52662.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.006076656226940486, var=0.059162380386821777, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 0.5028860706020695"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.5028860706020695""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.5028860706020695
""",
)

entry(
    index = 243,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(2.21125e+08,'s^-1'), n=0.878781, w0=(301000,'J/mol'), E0=(53251.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=8.50512200629795e-05, var=0.9050939833988869, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.9074470296389483"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.9074470296389483""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.9074470296389483
""",
)

entry(
    index = 244,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(3.65e+09,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(60423.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 245,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(3.84e+09,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(58905.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 246,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(5.9875e+09,'s^-1'), n=0.809338, w0=(301000,'J/mol'), E0=(97761.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.002885553689669155, var=0.21378044776099492, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R
    Total Standard Deviation in ln(k): 0.9341674192711222"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R
Total Standard Deviation in ln(k): 0.9341674192711222""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R
Total Standard Deviation in ln(k): 0.9341674192711222
""",
)

entry(
    index = 247,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(5.24776e+07,'s^-1'), n=1.17062, w0=(301000,'J/mol'), E0=(97304,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0015495595210675772, var=0.21284924432544747, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 0.9287896734223493"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.9287896734223493""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.9287896734223493
""",
)

entry(
    index = 248,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(4.88511e+07,'s^-1'), n=1.25321, w0=(301000,'J/mol'), E0=(97882.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.4402099292639156e-05, var=0.8893022089370891, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.8905579220764255"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.8905579220764255""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.8905579220764255
""",
)

entry(
    index = 249,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.06748e+11,'s^-1'), n=0.350699, w0=(301000,'J/mol'), E0=(82607.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.053947705316459996, var=1.0604811587654506, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 2.200016483044289"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.200016483044289""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.200016483044289
""",
)

entry(
    index = 250,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(7.33327e+08,'s^-1'), n=0.925304, w0=(301000,'J/mol'), E0=(80407.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.01497252773101592, var=1.4169784389227, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R
    Total Standard Deviation in ln(k): 2.4239939754428583"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 2.4239939754428583""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 2.4239939754428583
""",
)

entry(
    index = 251,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(3.77e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(67023.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 252,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-5R!H-3R!H",
    kinetics = ArrheniusBM(A=(2.84411e+11,'s^-1'), n=0.30016, w0=(301000,'J/mol'), E0=(58502,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.002538541922622625, var=0.11550273728440234, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-5R!H-3R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-5R!H-3R!H
    Total Standard Deviation in ln(k): 0.6877013679258529"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-5R!H-3R!H
Total Standard Deviation in ln(k): 0.6877013679258529""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-5R!H-3R!H
Total Standard Deviation in ln(k): 0.6877013679258529
""",
)

entry(
    index = 253,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H",
    kinetics = ArrheniusBM(A=(1.38708e+08,'s^-1'), n=0.914909, w0=(301000,'J/mol'), E0=(64133,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0011183573557213436, var=1.287079440166476, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H
    Total Standard Deviation in ln(k): 2.2771723375499673"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H
Total Standard Deviation in ln(k): 2.2771723375499673""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H
Total Standard Deviation in ln(k): 2.2771723375499673
""",
)

entry(
    index = 254,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H",
    kinetics = ArrheniusBM(A=(3.47159e+10,'s^-1'), n=0.620895, w0=(301000,'J/mol'), E0=(100949,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.015289796014867374, var=2.191531773804009, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H
    Total Standard Deviation in ln(k): 3.006190910970594"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H
Total Standard Deviation in ln(k): 3.006190910970594""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H
Total Standard Deviation in ln(k): 3.006190910970594
""",
)

entry(
    index = 255,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-5R!H-3R!H",
    kinetics = ArrheniusBM(A=(4.61649e+12,'s^-1'), n=0.0654112, w0=(301000,'J/mol'), E0=(48388.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.005313620952029411, var=0.08526797681987967, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-5R!H-3R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-5R!H-3R!H
    Total Standard Deviation in ln(k): 0.5987471003422999"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-5R!H-3R!H
Total Standard Deviation in ln(k): 0.5987471003422999""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-5R!H-3R!H
Total Standard Deviation in ln(k): 0.5987471003422999
""",
)

entry(
    index = 256,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H",
    kinetics = ArrheniusBM(A=(1.70454e+08,'s^-1'), n=0.879585, w0=(301000,'J/mol'), E0=(55432.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.01952996430041272, var=0.48632946803394245, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H
    Total Standard Deviation in ln(k): 1.4471189045588257"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H
Total Standard Deviation in ln(k): 1.4471189045588257""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H
Total Standard Deviation in ln(k): 1.4471189045588257
""",
)

entry(
    index = 257,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H",
    kinetics = ArrheniusBM(A=(8.50003e+10,'s^-1'), n=0.537253, w0=(301000,'J/mol'), E0=(114762,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.01360508089563144, var=5.2382889380130875, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H
    Total Standard Deviation in ln(k): 4.622482653059286"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H
Total Standard Deviation in ln(k): 4.622482653059286""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H
Total Standard Deviation in ln(k): 4.622482653059286
""",
)

entry(
    index = 258,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.85e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(54245.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 259,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(6.25e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(91018.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 260,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Ext-3R!H-R_Sp-9R!H=7R!H",
    kinetics = ArrheniusBM(A=(3.56e+09,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(82883.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Ext-3R!H-R_Sp-9R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Ext-3R!H-R_Sp-9R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Ext-3R!H-R_Sp-9R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Ext-3R!H-R_Sp-9R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 261,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Ext-3R!H-R_N-Sp-9R!H=7R!H",
    kinetics = ArrheniusBM(A=(8.8e+09,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(72540.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Ext-3R!H-R_N-Sp-9R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Ext-3R!H-R_N-Sp-9R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Ext-3R!H-R_N-Sp-9R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Ext-3R!H-R_N-Sp-9R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 262,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-5R!H-3R!H",
    kinetics = ArrheniusBM(A=(3.16e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(55728.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-5R!H-3R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-5R!H-3R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-5R!H-3R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-5R!H-3R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 263,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H",
    kinetics = ArrheniusBM(A=(2.98006e+06,'s^-1'), n=1.09636, w0=(301000,'J/mol'), E0=(64383.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0006442206325263416, var=3.9688317525041095, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H
    Total Standard Deviation in ln(k): 3.9954372307047827"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H
Total Standard Deviation in ln(k): 3.9954372307047827""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H
Total Standard Deviation in ln(k): 3.9954372307047827
""",
)

entry(
    index = 264,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H",
    kinetics = ArrheniusBM(A=(1.08041e+09,'s^-1'), n=0.759592, w0=(301000,'J/mol'), E0=(101591,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.719523279923105e-05, var=7.157638165295278, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H
    Total Standard Deviation in ln(k): 5.363514101268714"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H
Total Standard Deviation in ln(k): 5.363514101268714""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H
Total Standard Deviation in ln(k): 5.363514101268714
""",
)

entry(
    index = 265,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-5R!H-3R!H",
    kinetics = ArrheniusBM(A=(7.82e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(42274.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-5R!H-3R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-5R!H-3R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-5R!H-3R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-5R!H-3R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 266,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H",
    kinetics = ArrheniusBM(A=(5.83511e+06,'s^-1'), n=1.00242, w0=(301000,'J/mol'), E0=(56159.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0030249117350975127, var=1.4208938706557543, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H
    Total Standard Deviation in ln(k): 2.397269611467009"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H
Total Standard Deviation in ln(k): 2.397269611467009""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H
Total Standard Deviation in ln(k): 2.397269611467009
""",
)

entry(
    index = 267,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H",
    kinetics = ArrheniusBM(A=(4.58084e+09,'s^-1'), n=0.604425, w0=(301000,'J/mol'), E0=(115972,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0007680916864333964, var=17.773376435306666, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H
    Total Standard Deviation in ln(k): 8.453588738812668"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H
Total Standard Deviation in ln(k): 8.453588738812668""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H
Total Standard Deviation in ln(k): 8.453588738812668
""",
)

entry(
    index = 268,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-5R!H-R_Sp-6R!H-3R!H_Int-7R!H-6R!H_Sp-7R!H-6R!H_Ext-1Cd-R",
    kinetics = ArrheniusBM(A=(24600,'s^-1'), n=1.32, w0=(301000,'J/mol'), E0=(58646.4,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-5R!H-R_Sp-6R!H-3R!H_Int-7R!H-6R!H_Sp-7R!H-6R!H_Ext-1Cd-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-5R!H-R_Sp-6R!H-3R!H_Int-7R!H-6R!H_Sp-7R!H-6R!H_Ext-1Cd-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-5R!H-R_Sp-6R!H-3R!H_Int-7R!H-6R!H_Sp-7R!H-6R!H_Ext-1Cd-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-1COCSCbCbfCdCtN->Ct_N-5R!H-inRing_Ext-5R!H-R_Sp-6R!H-3R!H_Int-7R!H-6R!H_Sp-7R!H-6R!H_Ext-1Cd-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 269,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R",
    kinetics = ArrheniusBM(A=(1.11449e+08,'s^-1'), n=1.13616, w0=(301000,'J/mol'), E0=(83927.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0017421644805980278, var=0.8993123767271904, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R',), comment="""BM rule fitted to 16 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R
    Total Standard Deviation in ln(k): 1.9055093091964967"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 1.9055093091964967""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 1.9055093091964967
""",
)

entry(
    index = 270,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(7.92793e+07,'s^-1'), n=1.06329, w0=(301000,'J/mol'), E0=(66904.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09065527762665071, var=0.3918379949521838, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 1.4826803817626448"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.4826803817626448""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.4826803817626448
""",
)

entry(
    index = 271,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.50896e+08,'s^-1'), n=1.07425, w0=(301000,'J/mol'), E0=(68837.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.617130642308806, var=4.172426419855754, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 8.158118053220699"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 8.158118053220699""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 8.158118053220699
""",
)

entry(
    index = 272,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.87143e+08,'s^-1'), n=1.11371, w0=(301000,'J/mol'), E0=(69162.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.8935090526494047, var=0.7479513311358108, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 9.003901931573196"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 9.003901931573196""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 9.003901931573196
""",
)

entry(
    index = 273,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.25e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(30100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 274,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.31e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(30100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 275,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H",
    kinetics = ArrheniusBM(A=(7.76238e+09,'s^-1'), n=0.720911, w0=(301000,'J/mol'), E0=(71440.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.007859345131137327, var=0.29201132213759073, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H
    Total Standard Deviation in ln(k): 1.1030672820901808"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H
Total Standard Deviation in ln(k): 1.1030672820901808""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H
Total Standard Deviation in ln(k): 1.1030672820901808
""",
)

entry(
    index = 276,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H",
    kinetics = ArrheniusBM(A=(1.46182e+08,'s^-1'), n=0.872576, w0=(301000,'J/mol'), E0=(71756.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.027723865286707065, var=1.069341247060535, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H
    Total Standard Deviation in ln(k): 2.1427335951519124"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H
Total Standard Deviation in ln(k): 2.1427335951519124""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H
Total Standard Deviation in ln(k): 2.1427335951519124
""",
)

entry(
    index = 277,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H",
    kinetics = ArrheniusBM(A=(2.64262e+09,'s^-1'), n=0.916648, w0=(301000,'J/mol'), E0=(109646,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.004161567290766595, var=1.5626397472725044, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H
    Total Standard Deviation in ln(k): 2.5164871059638063"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H
Total Standard Deviation in ln(k): 2.5164871059638063""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H
Total Standard Deviation in ln(k): 2.5164871059638063
""",
)

entry(
    index = 278,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H",
    kinetics = ArrheniusBM(A=(9.83334e+10,'s^-1'), n=0.516815, w0=(301000,'J/mol'), E0=(62536.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.014136938914754553, var=0.29156076050454705, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H
    Total Standard Deviation in ln(k): 1.1180040485930351"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H
Total Standard Deviation in ln(k): 1.1180040485930351""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H
Total Standard Deviation in ln(k): 1.1180040485930351
""",
)

entry(
    index = 279,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H",
    kinetics = ArrheniusBM(A=(3.81256e+06,'s^-1'), n=1.31385, w0=(301000,'J/mol'), E0=(58008.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03745730986658431, var=0.288409179357186, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H
    Total Standard Deviation in ln(k): 1.1707315768721904"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H
Total Standard Deviation in ln(k): 1.1707315768721904""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H
Total Standard Deviation in ln(k): 1.1707315768721904
""",
)

entry(
    index = 280,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H",
    kinetics = ArrheniusBM(A=(1.29743e+06,'s^-1'), n=1.88498, w0=(301000,'J/mol'), E0=(111668,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.10597266846243782, var=2.6733361095371064, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H
    Total Standard Deviation in ln(k): 3.544072954712169"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H
Total Standard Deviation in ln(k): 3.544072954712169""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H
Total Standard Deviation in ln(k): 3.544072954712169
""",
)

entry(
    index = 281,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_Sp-9R!H=8R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.57e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(79326.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_Sp-9R!H=8R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_Sp-9R!H=8R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_Sp-9R!H=8R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_Sp-9R!H=8R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 282,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_N-Sp-9R!H=8R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(5.42e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(71976.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_N-Sp-9R!H=8R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_N-Sp-9R!H=8R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_N-Sp-9R!H=8R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_N-Sp-9R!H=8R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 283,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(1.65e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(77298.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Sp-9R!H=8R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 284,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(5.71e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(69980.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-Sp-9R!H=8R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 285,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(2.32e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(66041.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 286,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(2.45e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(64261.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 287,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(7.10982e+07,'s^-1'), n=0.827664, w0=(301000,'J/mol'), E0=(50519.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.006628096165220683, var=0.055879889834976666, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 0.4905513815850393"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.4905513815850393""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.4905513815850393
""",
)

entry(
    index = 288,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.07733e+08,'s^-1'), n=0.84137, w0=(301000,'J/mol'), E0=(51078.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=9.372642703870917e-05, var=0.8994028476387768, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.9014631296685194"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.9014631296685194""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.9014631296685194
""",
)

entry(
    index = 289,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(2.44e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(59817.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 290,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(2.57e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(58299.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 291,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.81201e+10,'s^-1'), n=0.606214, w0=(301000,'J/mol'), E0=(96764.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.008639217752073287, var=0.2712907275995352, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 1.065884398981816"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.065884398981816""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.065884398981816
""",
)

entry(
    index = 292,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.11616e+09,'s^-1'), n=1.04653, w0=(301000,'J/mol'), E0=(97785.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0014286204878767837, var=0.21735111994079787, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 0.9382156541797062"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.9382156541797062""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.9382156541797062
""",
)

entry(
    index = 293,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(9.38343e+08,'s^-1'), n=1.14235, w0=(301000,'J/mol'), E0=(98301.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.3090081934036536e-05, var=0.8874136788859341, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.8885461943478408"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.8885461943478408""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.8885461943478408
""",
)

entry(
    index = 294,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.23e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(108227,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 295,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.3e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(106544,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 296,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-10R!H-R",
    kinetics = ArrheniusBM(A=(3.24857e+08,'s^-1'), n=1.0807, w0=(301000,'J/mol'), E0=(79246.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.00916236261566594, var=1.421927151496731, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-10R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-10R!H-R
    Total Standard Deviation in ln(k): 2.4135590739170953"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 2.4135590739170953""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 2.4135590739170953
""",
)

entry(
    index = 297,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(6.32e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(67583,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 298,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(3.54818e+09,'s^-1'), n=0.684731, w0=(301000,'J/mol'), E0=(81200.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0003955008382185443, var=9.196857932392323, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 6.080617826538562"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.080617826538562""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.080617826538562
""",
)

entry(
    index = 299,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H",
    kinetics = ArrheniusBM(A=(2.54e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(86097.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 300,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H",
    kinetics = ArrheniusBM(A=(8.78e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(77867.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 301,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-5R!H-3R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(5.57e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(57603.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-5R!H-3R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-5R!H-3R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-5R!H-3R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-5R!H-3R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 302,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(4.68806e+08,'s^-1'), n=0.655683, w0=(301000,'J/mol'), E0=(65363,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.022352492846357e-05, var=0.2685331100674202, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 1.0389081472953778"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.0389081472953778""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.0389081472953778
""",
)

entry(
    index = 303,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.25e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(72736.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 304,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(5.32493e+10,'s^-1'), n=0.457866, w0=(301000,'J/mol'), E0=(103018,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00025257209401540663, var=0.21182172977174196, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 0.9232957747926"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 0.9232957747926""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 0.9232957747926
""",
)

entry(
    index = 305,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(4.22e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(107958,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 306,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-5R!H-3R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.38e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(44740.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-5R!H-3R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-5R!H-3R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-5R!H-3R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-5R!H-3R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 307,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(7.6404e+07,'s^-1'), n=1.00724, w0=(301000,'J/mol'), E0=(54520.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.00433535032553191, var=1.3453127771217215, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 2.336137324399147"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 2.336137324399147""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 2.336137324399147
""",
)

entry(
    index = 308,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2.7e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(56996.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 309,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(2.79049e+10,'s^-1'), n=0.703566, w0=(301000,'J/mol'), E0=(113567,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.005229229681639835, var=17.188885655746706, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 8.32466635506853"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 8.32466635506853""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 8.32466635506853
""",
)

entry(
    index = 310,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(9.14e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(104658,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 311,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.04e+09,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(68008,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 312,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(3.52e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(106809,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 313,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2.57e+09,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(57641.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 314,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(8.7e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(105313,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 315,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(9.39737e+07,'s^-1'), n=1.11223, w0=(301000,'J/mol'), E0=(83385.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.01977467317985484, var=1.865312630486377, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 2.787681080497892"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.787681080497892""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.787681080497892
""",
)

entry(
    index = 316,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(8.37988e+06,'s^-1'), n=1.46712, w0=(301000,'J/mol'), E0=(81071.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.012254835381840929, var=0.0438298123309946, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 0.4504937744772678"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.4504937744772678""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.4504937744772678
""",
)

entry(
    index = 317,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(9.7958e+06,'s^-1'), n=1.51781, w0=(301000,'J/mol'), E0=(81675.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.003943505338016459, var=0.26588919391311044, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.0436388117175908"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.0436388117175908""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.0436388117175908
""",
)

entry(
    index = 318,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(6.92367e+07,'s^-1'), n=1.04664, w0=(301000,'J/mol'), E0=(66680.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.4925162221107378, var=3.5077320291177814, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 7.504697107358476"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 7.504697107358476""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 7.504697107358476
""",
)

entry(
    index = 319,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(7.86506e+07,'s^-1'), n=1.09755, w0=(301000,'J/mol'), E0=(66921.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=7.009100361534949e-05, var=0.9010269015666957, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.903119495700503"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.903119495700503""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.903119495700503
""",
)

entry(
    index = 320,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(8.34e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(30100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 321,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(8.79e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(30100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 322,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.37067e+10,'s^-1'), n=0.608329, w0=(301000,'J/mol'), E0=(71355.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0030876277936222785, var=0.4586707173014343, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.3654693592160811"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.3654693592160811""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.3654693592160811
""",
)

entry(
    index = 323,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(4.31333e+09,'s^-1'), n=0.835853, w0=(301000,'J/mol'), E0=(71505,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.055225837881176e-05, var=0.8884441047129247, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.8896610548317974"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.8896610548317974""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.8896610548317974
""",
)

entry(
    index = 324,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(3.01001e+07,'s^-1'), n=0.960546, w0=(301000,'J/mol'), E0=(70385.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.007515431790619978, var=0.2706683011681045, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 1.0618622918136504"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.0618622918136504""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.0618622918136504
""",
)

entry(
    index = 325,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(2.70902e+06,'s^-1'), n=1.4406, w0=(301000,'J/mol'), E0=(66622.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.002335360012522922, var=0.1792391491342366, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 0.8546053072484454"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.8546053072484454""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.8546053072484454
""",
)

entry(
    index = 326,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(2.78519e+06,'s^-1'), n=1.50985, w0=(301000,'J/mol'), E0=(67238.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.3906901605553218e-05, var=0.907081489862618, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.9093863103581328"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.9093863103581328""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.9093863103581328
""",
)

entry(
    index = 327,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.98707e+09,'s^-1'), n=0.841553, w0=(301000,'J/mol'), E0=(111012,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.008643128607831863, var=0.2796782061625515, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 1.081912747197264"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.081912747197264""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.081912747197264
""",
)

entry(
    index = 328,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(4.15903e+09,'s^-1'), n=0.931907, w0=(301000,'J/mol'), E0=(107967,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.00010568628826578016, var=0.3096862221937616, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.1158897566730914"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.1158897566730914""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.1158897566730914
""",
)

entry(
    index = 329,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(2.80557e+09,'s^-1'), n=1.05866, w0=(301000,'J/mol'), E0=(108530,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.085942975583725e-06, var=0.8854340407176501, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.886408413921495"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.886408413921495""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.886408413921495
""",
)

entry(
    index = 330,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.86114e+11,'s^-1'), n=0.395679, w0=(301000,'J/mol'), E0=(62519.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.004503469261866372, var=0.4934313270120711, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.419534732770541"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.419534732770541""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.419534732770541
""",
)

entry(
    index = 331,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(5.10234e+10,'s^-1'), n=0.640204, w0=(301000,'J/mol'), E0=(62533.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.7851083942415053e-05, var=0.8700046154270793, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.8699673343515257"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.8699673343515257""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.8699673343515257
""",
)

entry(
    index = 332,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(3.26151e+06,'s^-1'), n=1.29785, w0=(301000,'J/mol'), E0=(57585.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03898163884566308, var=0.24277547873917868, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.0857219294070133"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.0857219294070133""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.0857219294070133
""",
)

entry(
    index = 333,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(4.22676e+06,'s^-1'), n=1.33647, w0=(301000,'J/mol'), E0=(58373.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.030403564239537842, var=0.45986330479700616, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.4358663090266566"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.4358663090266566""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.4358663090266566
""",
)

entry(
    index = 334,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.56192e+06,'s^-1'), n=1.82433, w0=(301000,'J/mol'), E0=(111483,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.102595535175024, var=4.059153341643385, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 4.296785772810131"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 4.296785772810131""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 4.296785772810131
""",
)

entry(
    index = 335,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.07169e+06,'s^-1'), n=1.94634, w0=(301000,'J/mol'), E0=(111846,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09799921353187929, var=4.224461562913216, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 4.3666604166164875"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 4.3666604166164875""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 4.3666604166164875
""",
)

entry(
    index = 336,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(7.65e+09,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(55650.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 337,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(8.06e+09,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(54131.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 338,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(2.06032e+10,'s^-1'), n=0.552706, w0=(301000,'J/mol'), E0=(96525,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0012691947758164594, var=0.2324833106962551, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 0.969802484761105"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.969802484761105""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.969802484761105
""",
)

entry(
    index = 339,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.58218e+10,'s^-1'), n=0.660626, w0=(301000,'J/mol'), E0=(96996.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.1417269561738198e-05, var=0.8858049272061354, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.8868294150796763"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.8868294150796763""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.8868294150796763
""",
)

entry(
    index = 340,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(8.25e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(106134,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 341,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(8.69e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(104437,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 342,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.24812e+09,'s^-1'), n=0.868412, w0=(301000,'J/mol'), E0=(79836.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0004983903804592809, var=9.200844737381237, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 6.082193947839984"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.082193947839984""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.082193947839984
""",
)

entry(
    index = 343,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H",
    kinetics = ArrheniusBM(A=(4.26e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(87106.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 344,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H",
    kinetics = ArrheniusBM(A=(1.47e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(78833.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 345,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_Sp-10R!H=9R!H",
    kinetics = ArrheniusBM(A=(3.74e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(82244,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_Sp-10R!H=9R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_Sp-10R!H=9R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 346,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_N-Sp-10R!H=9R!H",
    kinetics = ArrheniusBM(A=(9.24e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(71901,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_N-Sp-10R!H=9R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_N-Sp-10R!H=9R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_N-Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_N-Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 347,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.83e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(68626,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 348,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(6.19e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(107760,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 349,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(4.53e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(58275,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 350,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.53e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(106163,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 351,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H",
    kinetics = ArrheniusBM(A=(4.76006e+07,'s^-1'), n=1.1429, w0=(301000,'J/mol'), E0=(88475.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.013339900589089359, var=0.27095436672861684, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H
    Total Standard Deviation in ln(k): 1.0770476451301756"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 1.0770476451301756""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 1.0770476451301756
""",
)

entry(
    index = 352,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H",
    kinetics = ArrheniusBM(A=(3.71471e+08,'s^-1'), n=0.995327, w0=(301000,'J/mol'), E0=(79063.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0174362203292323, var=0.2700782456349628, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H
    Total Standard Deviation in ln(k): 1.085651431119483"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 1.085651431119483""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 1.085651431119483
""",
)

entry(
    index = 353,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_Sp-11R!H=10R!H",
    kinetics = ArrheniusBM(A=(5.6373e+06,'s^-1'), n=1.58478, w0=(301000,'J/mol'), E0=(84603.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0023022807903855173, var=0.16352594002320128, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_Sp-11R!H=10R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_Sp-11R!H=10R!H
    Total Standard Deviation in ln(k): 0.8164662262426715"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 0.8164662262426715""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 0.8164662262426715
""",
)

entry(
    index = 354,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_N-Sp-11R!H=10R!H",
    kinetics = ArrheniusBM(A=(1.09592e+07,'s^-1'), n=1.36506, w0=(301000,'J/mol'), E0=(77311.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.002902767303773757, var=0.14365025671620152, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_N-Sp-11R!H=10R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_N-Sp-11R!H=10R!H
    Total Standard Deviation in ln(k): 0.7671124610015203"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_N-Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 0.7671124610015203""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_N-Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 0.7671124610015203
""",
)

entry(
    index = 355,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.08325e+07,'s^-1'), n=1.48446, w0=(301000,'J/mol'), E0=(83501,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.005469175823717592, var=0.0022147313604411367, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 0.1080863497998224"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 0.1080863497998224""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 0.1080863497998224
""",
)

entry(
    index = 356,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Sp-11R!H=10R!H",
    kinetics = ArrheniusBM(A=(3.19e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(90487.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Sp-11R!H=10R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Sp-11R!H=10R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 357,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_N-Sp-11R!H=10R!H",
    kinetics = ArrheniusBM(A=(1.1e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(81381.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_N-Sp-11R!H=10R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_N-Sp-11R!H=10R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_N-Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_N-Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 358,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(2.62e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(30100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 359,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(2.76e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(67511.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 360,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(2.3e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(73899.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 361,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(2.43e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(71800.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 362,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(3.22094e+07,'s^-1'), n=0.91507, w0=(301000,'J/mol'), E0=(70114.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0019585629726090797, var=0.20486804952555723, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 0.9123112569426"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.9123112569426""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.9123112569426
""",
)

entry(
    index = 363,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(2.76348e+07,'s^-1'), n=1.00824, w0=(301000,'J/mol'), E0=(70638,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.9237866958192016e-05, var=0.9015424868757916, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.9035360969473445"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.9035360969473445""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.9035360969473445
""",
)

entry(
    index = 364,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(5.16e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(79568.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 365,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(5.44e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(77967.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 366,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(2.48742e+09,'s^-1'), n=0.774406, w0=(301000,'J/mol'), E0=(110749,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.3550410155275e-05, var=0.3223210820729283, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.1382140014737567"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.1382140014737567""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.1382140014737567
""",
)

entry(
    index = 367,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.59265e+09,'s^-1'), n=0.908286, w0=(301000,'J/mol'), E0=(111278,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=8.049473537573448e-08, var=0.8869413213547774, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.888010825813487"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.888010825813487""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.888010825813487
""",
)

entry(
    index = 368,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.75e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(118353,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 369,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.84e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(116509,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 370,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(5.7e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(63112.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 371,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(6.01e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(60899.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 372,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2.42547e+08,'s^-1'), n=0.774458, w0=(301000,'J/mol'), E0=(60866.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0024536402012063844, var=0.19510916919030544, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 0.891679735485539"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 0.891679735485539""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 0.891679735485539
""",
)

entry(
    index = 373,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.78e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(70652,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 374,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(5.65297e+06,'s^-1'), n=1.2792, w0=(301000,'J/mol'), E0=(60396.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.009941611089130638, var=0.7189757867974458, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 1.7248427084349112"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 1.7248427084349112""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 1.7248427084349112
""",
)

entry(
    index = 375,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(3.39e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(63160.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 376,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(3.87983e+10,'s^-1'), n=0.58032, w0=(301000,'J/mol'), E0=(112613,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.00035770901024972414, var=0.29186446398988997, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 1.0839465045217023"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.0839465045217023""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.0839465045217023
""",
)

entry(
    index = 377,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(6.03e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(137689,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 378,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.91832e+06,'s^-1'), n=1.85395, w0=(301000,'J/mol'), E0=(114197,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03421372723188449, var=13.839466047202976, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 7.543865871446508"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 7.543865871446508""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 7.543865871446508
""",
)

entry(
    index = 379,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.15e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(113185,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 380,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(2.59e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(99243.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 381,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(2.73e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(97525.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-2CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 382,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H",
    kinetics = ArrheniusBM(A=(6.26e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(83355.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 383,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H",
    kinetics = ArrheniusBM(A=(1.55e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(73006,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 384,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(5.3888e+07,'s^-1'), n=1.09049, w0=(301000,'J/mol'), E0=(88290.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0020182003068943384, var=0.18289294178347487, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 0.8624155445959526"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.8624155445959526""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.8624155445959526
""",
)

entry(
    index = 385,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(4.04643e+07,'s^-1'), n=1.20007, w0=(301000,'J/mol'), E0=(88618.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.0394514281470798e-05, var=0.9082383871948086, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.9105946805222207"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.9105946805222207""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.9105946805222207
""",
)

entry(
    index = 386,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(3.88014e+08,'s^-1'), n=0.953541, w0=(301000,'J/mol'), E0=(78823,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.002416028026535949, var=0.1734881108439877, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 0.8410807524563302"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.8410807524563302""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.8410807524563302
""",
)

entry(
    index = 387,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(3.38245e+08,'s^-1'), n=1.04334, w0=(301000,'J/mol'), E0=(79248,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.495444613003415e-05, var=0.906041652794281, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.90829424606997"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.90829424606997""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.90829424606997
""",
)

entry(
    index = 388,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_Sp-11R!H=10R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.77e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(93233.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_Sp-11R!H=10R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_Sp-11R!H=10R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_Sp-11R!H=10R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_Sp-11R!H=10R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 389,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_N-Sp-11R!H=10R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(6.09e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(84125,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_N-Sp-11R!H=10R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_N-Sp-11R!H=10R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_N-Sp-11R!H=10R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_N-Sp-11R!H=10R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 390,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Sp-11R!H=10R!H",
    kinetics = ArrheniusBM(A=(1.86e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(91607.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Sp-11R!H=10R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Sp-11R!H=10R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 391,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-Sp-11R!H=10R!H",
    kinetics = ArrheniusBM(A=(6.42e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(82532.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-Sp-11R!H=10R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-Sp-11R!H=10R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 392,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(7.58e+09,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(76401,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 393,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(7.99e+09,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(74763,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 394,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(2.56e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(118434,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 395,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(2.7e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(116573,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 396,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.88e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(65914.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 397,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.98e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(64292.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 398,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(6.34e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(116038,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 399,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(6.68e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(114225,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 400,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(2.59e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(90244.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 401,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(2.73e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(88634.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 402,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(6.41e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(79663.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 403,
    label = "Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(6.76e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(78069.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2CbCbfCdCddCtNO2dS2d-R_N-1COCSCbCbfCdCtN-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_N-Sp-7R!H=6R!H_Ext-2CbCbfCdCddCtNO2dS2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

