#!/usr/bin/env python
# encoding: utf-8

name = "Br_Abstraction/rules"
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
    kinetics = ArrheniusBM(A=(6.43559e+07,'m^3/(mol*s)'), n=-0.156922, w0=(288.01,'kJ/mol'), E0=(61.6133,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.16118635182028776, var=9.994861125437609, Tref=1000.0, N=200, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 200 training reactions at node Root
    Total Standard Deviation in ln(k): 6.7428906719939405"""),
    rank = 11,
    shortDesc = """BM rule fitted to 200 training reactions at node Root
Total Standard Deviation in ln(k): 6.7428906719939405""",
    longDesc = 
"""
BM rule fitted to 200 training reactions at node Root
Total Standard Deviation in ln(k): 6.7428906719939405
""",
)

entry(
    index = 2,
    label = "Root_1R->H",
    kinetics = ArrheniusBM(A=(3386.46,'m^3/(mol*s)'), n=0.944666, w0=(318.097,'kJ/mol'), E0=(59.1439,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5503919267812694, var=3.480057901773251, Tref=1000.0, N=38, data_mean=0.0, correlation='Root_1R->H',), comment="""BM rule fitted to 38 training reactions at node Root_1R->H
    Total Standard Deviation in ln(k): 5.122710193934974"""),
    rank = 11,
    shortDesc = """BM rule fitted to 38 training reactions at node Root_1R->H
Total Standard Deviation in ln(k): 5.122710193934974""",
    longDesc = 
"""
BM rule fitted to 38 training reactions at node Root_1R->H
Total Standard Deviation in ln(k): 5.122710193934974
""",
)

entry(
    index = 3,
    label = "Root_1R->H_3R->C",
    kinetics = ArrheniusBM(A=(2.23878e-10,'m^3/(mol*s)'), n=4.67771, w0=(323.5,'kJ/mol'), E0=(0.193436,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.2260281451463118, var=0.9071756895127708, Tref=1000.0, N=31, data_mean=0.0, correlation='Root_1R->H_3R->C',), comment="""BM rule fitted to 31 training reactions at node Root_1R->H_3R->C
    Total Standard Deviation in ln(k): 4.989898107653222"""),
    rank = 11,
    shortDesc = """BM rule fitted to 31 training reactions at node Root_1R->H_3R->C
Total Standard Deviation in ln(k): 4.989898107653222""",
    longDesc = 
"""
BM rule fitted to 31 training reactions at node Root_1R->H_3R->C
Total Standard Deviation in ln(k): 4.989898107653222
""",
)

entry(
    index = 4,
    label = "Root_1R->H_3R->C_3C-u1",
    kinetics = ArrheniusBM(A=(3.45311e-10,'m^3/(mol*s)'), n=4.58593, w0=(323.5,'kJ/mol'), E0=(13.1441,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.2663341396512773, var=0.7929275046285716, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1',), comment="""BM rule fitted to 25 training reactions at node Root_1R->H_3R->C_3C-u1
    Total Standard Deviation in ln(k): 4.966890026846542"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_1R->H_3R->C_3C-u1
Total Standard Deviation in ln(k): 4.966890026846542""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_1R->H_3R->C_3C-u1
Total Standard Deviation in ln(k): 4.966890026846542
""",
)

entry(
    index = 5,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.04155e-10,'m^3/(mol*s)'), n=4.59588, w0=(323.5,'kJ/mol'), E0=(12.4803,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.298726004402836, var=0.8126025989525971, Tref=1000.0, N=23, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R',), comment="""BM rule fitted to 23 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R
    Total Standard Deviation in ln(k): 5.070288532343017"""),
    rank = 11,
    shortDesc = """BM rule fitted to 23 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R
Total Standard Deviation in ln(k): 5.070288532343017""",
    longDesc = 
"""
BM rule fitted to 23 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R
Total Standard Deviation in ln(k): 5.070288532343017
""",
)

entry(
    index = 6,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_Sp-4R!H=3C",
    kinetics = ArrheniusBM(A=(9.83308e-06,'m^3/(mol*s)'), n=3.53062, w0=(323.5,'kJ/mol'), E0=(39.6535,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6545797850109607, var=0.6239755520051671, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_Sp-4R!H=3C',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_Sp-4R!H=3C
    Total Standard Deviation in ln(k): 3.228255627866072"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_Sp-4R!H=3C
Total Standard Deviation in ln(k): 3.228255627866072""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_Sp-4R!H=3C
Total Standard Deviation in ln(k): 3.228255627866072
""",
)

entry(
    index = 7,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.42001e-07,'m^3/(mol*s)'), n=3.98305, w0=(323.5,'kJ/mol'), E0=(39.8777,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7687874385928474, var=1.1173949680539925, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R
    Total Standard Deviation in ln(k): 4.050770125916972"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R
Total Standard Deviation in ln(k): 4.050770125916972""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R
Total Standard Deviation in ln(k): 4.050770125916972
""",
)

entry(
    index = 8,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(6.71691e-14,'m^3/(mol*s)'), n=6.161, w0=(323.5,'kJ/mol'), E0=(33.773,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 9,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C",
    kinetics = ArrheniusBM(A=(1.24649e-08,'m^3/(mol*s)'), n=4.09983, w0=(323.5,'kJ/mol'), E0=(26.6213,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.1255894406083837, var=1.0813026725236283, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C',), comment="""BM rule fitted to 20 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C
    Total Standard Deviation in ln(k): 4.9127520645118095"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C
Total Standard Deviation in ln(k): 4.9127520645118095""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C
Total Standard Deviation in ln(k): 4.9127520645118095
""",
)

entry(
    index = 10,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br",
    kinetics = ArrheniusBM(A=(0.00759771,'m^3/(mol*s)'), n=2.37782, w0=(323.5,'kJ/mol'), E0=(49.4471,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7095752825022102, var=0.2701047296001838, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br
    Total Standard Deviation in ln(k): 2.824745381331985"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br
Total Standard Deviation in ln(k): 2.824745381331985""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br
Total Standard Deviation in ln(k): 2.824745381331985
""",
)

entry(
    index = 11,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.00114784,'m^3/(mol*s)'), n=2.63117, w0=(323.5,'kJ/mol'), E0=(47.4281,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.8325170106585299, var=0.5684410224924069, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R
    Total Standard Deviation in ln(k): 3.603221853037736"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R
Total Standard Deviation in ln(k): 3.603221853037736""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R
Total Standard Deviation in ln(k): 3.603221853037736
""",
)

entry(
    index = 12,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.00198848,'m^3/(mol*s)'), n=2.53388, w0=(323.5,'kJ/mol'), E0=(49.2158,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br",
    kinetics = ArrheniusBM(A=(4.81985e-06,'m^3/(mol*s)'), n=3.36991, w0=(323.5,'kJ/mol'), E0=(37.0653,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.0280890328583094, var=1.2094765192806365, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br',), comment="""BM rule fitted to 17 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br
    Total Standard Deviation in ln(k): 4.787869788788029"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br
Total Standard Deviation in ln(k): 4.787869788788029""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br
Total Standard Deviation in ln(k): 4.787869788788029
""",
)

entry(
    index = 14,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClF->Cl",
    kinetics = ArrheniusBM(A=(0.00328889,'m^3/(mol*s)'), n=2.58868, w0=(323.5,'kJ/mol'), E0=(47.9555,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7290756964313243, var=6.447853774887535, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClF->Cl',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClF->Cl
    Total Standard Deviation in ln(k): 6.9223969817628435"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClF->Cl
Total Standard Deviation in ln(k): 6.9223969817628435""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClF->Cl
Total Standard Deviation in ln(k): 6.9223969817628435
""",
)

entry(
    index = 15,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClF->Cl_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.0183772,'m^3/(mol*s)'), n=2.48777, w0=(323.5,'kJ/mol'), E0=(49.4109,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.8303824706236708, var=1.2144909747653172, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClF->Cl_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClF->Cl_Ext-3C-R
    Total Standard Deviation in ln(k): 4.295685282342983"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClF->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 4.295685282342983""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClF->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 4.295685282342983
""",
)

entry(
    index = 16,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClF->Cl_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.0063045,'m^3/(mol*s)'), n=2.56274, w0=(323.5,'kJ/mol'), E0=(48.0337,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClF->Cl_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClF->Cl_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClF->Cl_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClF->Cl_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl",
    kinetics = ArrheniusBM(A=(3.29732e-09,'m^3/(mol*s)'), n=4.26904, w0=(323.5,'kJ/mol'), E0=(23.8543,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.173119419353875, var=0.7994201868215671, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl',), comment="""BM rule fitted to 14 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl
    Total Standard Deviation in ln(k): 4.739975890127031"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl
Total Standard Deviation in ln(k): 4.739975890127031""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl
Total Standard Deviation in ln(k): 4.739975890127031
""",
)

entry(
    index = 18,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R",
    kinetics = ArrheniusBM(A=(7.3812e-07,'m^3/(mol*s)'), n=3.52927, w0=(323.5,'kJ/mol'), E0=(33.3916,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.1374945083689458, var=0.7766342913159477, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R',), comment="""BM rule fitted to 8 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R
    Total Standard Deviation in ln(k): 4.624736416508559"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R
Total Standard Deviation in ln(k): 4.624736416508559""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R
Total Standard Deviation in ln(k): 4.624736416508559
""",
)

entry(
    index = 19,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(0.00101353,'m^3/(mol*s)'), n=2.63217, w0=(323.5,'kJ/mol'), E0=(46.6266,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.8115135714486373, var=0.1761901516924456, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_5R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_5R!H->Cl
    Total Standard Deviation in ln(k): 2.8804665844639548"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_5R!H->Cl
Total Standard Deviation in ln(k): 2.8804665844639548""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_5R!H->Cl
Total Standard Deviation in ln(k): 2.8804665844639548
""",
)

entry(
    index = 20,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_5R!H->Cl_Ext-4CF-R",
    kinetics = ArrheniusBM(A=(0.012647,'m^3/(mol*s)'), n=2.30939, w0=(323.5,'kJ/mol'), E0=(50.6518,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_5R!H->Cl_Ext-4CF-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_5R!H->Cl_Ext-4CF-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_5R!H->Cl_Ext-4CF-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_5R!H->Cl_Ext-4CF-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(5.69893e-06,'m^3/(mol*s)'), n=3.2743, w0=(323.5,'kJ/mol'), E0=(35.765,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.1486742588044867, var=1.0978121308689917, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl',), comment="""BM rule fitted to 6 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 4.986608084620623"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 4.986608084620623""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 4.986608084620623
""",
)

entry(
    index = 22,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_5BrCFINOPSSi->F",
    kinetics = ArrheniusBM(A=(0.000285184,'m^3/(mol*s)'), n=2.79633, w0=(323.5,'kJ/mol'), E0=(43.9995,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.0572948147686656, var=0.96256021380983, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_5BrCFINOPSSi->F',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_5BrCFINOPSSi->F
    Total Standard Deviation in ln(k): 4.623368288450273"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_5BrCFINOPSSi->F
Total Standard Deviation in ln(k): 4.623368288450273""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_5BrCFINOPSSi->F
Total Standard Deviation in ln(k): 4.623368288450273
""",
)

entry(
    index = 23,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_5BrCFINOPSSi->F_Ext-4CF-R",
    kinetics = ArrheniusBM(A=(0.0454822,'m^3/(mol*s)'), n=2.13705, w0=(323.5,'kJ/mol'), E0=(51.7141,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_5BrCFINOPSSi->F_Ext-4CF-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_5BrCFINOPSSi->F_Ext-4CF-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_5BrCFINOPSSi->F_Ext-4CF-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_5BrCFINOPSSi->F_Ext-4CF-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_5BrCFINOPSSi->F_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.17187e-08,'m^3/(mol*s)'), n=3.99558, w0=(323.5,'kJ/mol'), E0=(32.2386,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_5BrCFINOPSSi->F_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_5BrCFINOPSSi->F_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_5BrCFINOPSSi->F_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_5BrCFINOPSSi->F_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_N-5BrCFINOPSSi->F",
    kinetics = ArrheniusBM(A=(0.000109753,'m^3/(mol*s)'), n=2.89733, w0=(323.5,'kJ/mol'), E0=(37.2892,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.038089464470325, var=2.719173199512671, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_N-5BrCFINOPSSi->F',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_N-5BrCFINOPSSi->F
    Total Standard Deviation in ln(k): 5.914056229773974"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_N-5BrCFINOPSSi->F
Total Standard Deviation in ln(k): 5.914056229773974""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_N-5BrCFINOPSSi->F
Total Standard Deviation in ln(k): 5.914056229773974
""",
)

entry(
    index = 26,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_N-5BrCFINOPSSi->F_Ext-4CF-R",
    kinetics = ArrheniusBM(A=(0.0276483,'m^3/(mol*s)'), n=2.38592, w0=(323.5,'kJ/mol'), E0=(47.342,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_N-5BrCFINOPSSi->F_Ext-4CF-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_N-5BrCFINOPSSi->F_Ext-4CF-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_N-5BrCFINOPSSi->F_Ext-4CF-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_N-5BrCFINOPSSi->F_Ext-4CF-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_N-5BrCFINOPSSi->F_Ext-3C-R",
    kinetics = ArrheniusBM(A=(5.30094e-09,'m^3/(mol*s)'), n=4.17923, w0=(323.5,'kJ/mol'), E0=(21.9347,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_N-5BrCFINOPSSi->F_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_N-5BrCFINOPSSi->F_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_N-5BrCFINOPSSi->F_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_N-5BrCFINOPSSi->F_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F",
    kinetics = ArrheniusBM(A=(0.00508534,'m^3/(mol*s)'), n=2.57039, w0=(323.5,'kJ/mol'), E0=(47.6696,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.8166704513430073, var=0.26313477728732426, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F',), comment="""BM rule fitted to 5 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F
    Total Standard Deviation in ln(k): 3.0802980310419965"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F
Total Standard Deviation in ln(k): 3.0802980310419965""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F
Total Standard Deviation in ln(k): 3.0802980310419965
""",
)

entry(
    index = 29,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.0019165,'m^3/(mol*s)'), n=2.69915, w0=(323.5,'kJ/mol'), E0=(46.7312,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.9106705059639078, var=0.3240936789862426, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R
    Total Standard Deviation in ln(k): 3.4293970150427446"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R
Total Standard Deviation in ln(k): 3.4293970150427446""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R
Total Standard Deviation in ln(k): 3.4293970150427446
""",
)

entry(
    index = 30,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.00144735,'m^3/(mol*s)'), n=2.7504, w0=(323.5,'kJ/mol'), E0=(46.1058,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.9740494617978175, var=0.19853612435620657, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 3.340618137659127"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 3.340618137659127""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 3.340618137659127
""",
)

entry(
    index = 31,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R_5R!H->F",
    kinetics = ArrheniusBM(A=(0.00335574,'m^3/(mol*s)'), n=2.6774, w0=(323.5,'kJ/mol'), E0=(47.3371,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.8938104045929507, var=0.025176786775953978, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R_5R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R_5R!H->F
    Total Standard Deviation in ln(k): 2.5638500034293936"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R_5R!H->F
Total Standard Deviation in ln(k): 2.5638500034293936""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R_5R!H->F
Total Standard Deviation in ln(k): 2.5638500034293936
""",
)

entry(
    index = 32,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R_5R!H->F_6R!H->C",
    kinetics = ArrheniusBM(A=(0.00138706,'m^3/(mol*s)'), n=2.76619, w0=(323.5,'kJ/mol'), E0=(45.3665,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R_5R!H->F_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R_5R!H->F_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R_5R!H->F_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R_5R!H->F_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R_5R!H->F_N-6R!H->C",
    kinetics = ArrheniusBM(A=(0.00946276,'m^3/(mol*s)'), n=2.56954, w0=(323.5,'kJ/mol'), E0=(49.4591,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R_5R!H->F_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R_5R!H->F_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R_5R!H->F_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R_5R!H->F_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(4.66724e-05,'m^3/(mol*s)'), n=3.11447, w0=(323.5,'kJ/mol'), E0=(41.3265,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R_N-5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R_N-5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 35,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_N-4CF->F",
    kinetics = ArrheniusBM(A=(0.0560766,'m^3/(mol*s)'), n=2.37231, w0=(323.5,'kJ/mol'), E0=(46.0729,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_N-4CF->F',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_N-4CF->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_N-4CF->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_N-4CF->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 36,
    label = "Root_1R->H_3R->C_N-3C-u1",
    kinetics = ArrheniusBM(A=(1.4481e-10,'m^3/(mol*s)'), n=4.88339, w0=(323.5,'kJ/mol'), E0=(3.49396,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.1804332694116488, var=2.6930321208150803, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R->H_3R->C_N-3C-u1',), comment="""BM rule fitted to 6 training reactions at node Root_1R->H_3R->C_N-3C-u1
    Total Standard Deviation in ln(k): 6.255775306637816"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R->H_3R->C_N-3C-u1
Total Standard Deviation in ln(k): 6.255775306637816""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R->H_3R->C_N-3C-u1
Total Standard Deviation in ln(k): 6.255775306637816
""",
)

entry(
    index = 37,
    label = "Root_1R->H_3R->C_N-3C-u1_Ext-3C-R",
    kinetics = ArrheniusBM(A=(6.58773e-14,'m^3/(mol*s)'), n=5.82225, w0=(323.5,'kJ/mol'), E0=(-15.1793,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4142299178620902, var=2.348218497787689, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->H_3R->C_N-3C-u1_Ext-3C-R',), comment="""BM rule fitted to 5 training reactions at node Root_1R->H_3R->C_N-3C-u1_Ext-3C-R
    Total Standard Deviation in ln(k): 4.112814271509468"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->H_3R->C_N-3C-u1_Ext-3C-R
Total Standard Deviation in ln(k): 4.112814271509468""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->H_3R->C_N-3C-u1_Ext-3C-R
Total Standard Deviation in ln(k): 4.112814271509468
""",
)

entry(
    index = 38,
    label = "Root_1R->H_3R->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(2.74323e-15,'m^3/(mol*s)'), n=6.27488, w0=(323.5,'kJ/mol'), E0=(-17.0451,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.3151496590004055, var=7.793275177776979, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->H_3R->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C',), comment="""BM rule fitted to 4 training reactions at node Root_1R->H_3R->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C
    Total Standard Deviation in ln(k): 8.900902403335651"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->H_3R->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C
Total Standard Deviation in ln(k): 8.900902403335651""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->H_3R->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C
Total Standard Deviation in ln(k): 8.900902403335651
""",
)

entry(
    index = 39,
    label = "Root_1R->H_3R->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_4R!H->C",
    kinetics = ArrheniusBM(A=(6.4819e-10,'m^3/(mol*s)'), n=4.67096, w0=(323.5,'kJ/mol'), E0=(3.62173,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.47715252679712533, var=1.7417805761685443, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_3R->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_3R->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_4R!H->C
    Total Standard Deviation in ln(k): 3.844655584347964"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_3R->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_4R!H->C
Total Standard Deviation in ln(k): 3.844655584347964""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_3R->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_4R!H->C
Total Standard Deviation in ln(k): 3.844655584347964
""",
)

entry(
    index = 40,
    label = "Root_1R->H_3R->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(1.16097e-20,'m^3/(mol*s)'), n=7.87879, w0=(323.5,'kJ/mol'), E0=(-36.9381,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.611127522405062, var=38.4973985943333, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_3R->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_3R->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C
    Total Standard Deviation in ln(k): 13.974130061830248"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_3R->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C
Total Standard Deviation in ln(k): 13.974130061830248""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_3R->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C
Total Standard Deviation in ln(k): 13.974130061830248
""",
)

entry(
    index = 41,
    label = "Root_1R->H_3R->C_N-3C-u1_Ext-3C-R_N-Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(0.416835,'m^3/(mol*s)'), n=1.92612, w0=(323.5,'kJ/mol'), E0=(25.3446,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R->C_N-3C-u1_Ext-3C-R_N-Sp-4R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_N-3C-u1_Ext-3C-R_N-Sp-4R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_N-3C-u1_Ext-3C-R_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_N-3C-u1_Ext-3C-R_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_1R->H_N-3R->C",
    kinetics = ArrheniusBM(A=(14.1491,'m^3/(mol*s)'), n=1.84181, w0=(294.167,'kJ/mol'), E0=(21.8109,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6875541963847694, var=1.3067189816709899, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R->H_N-3R->C',), comment="""BM rule fitted to 7 training reactions at node Root_1R->H_N-3R->C
    Total Standard Deviation in ln(k): 4.019172051384877"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R->H_N-3R->C
Total Standard Deviation in ln(k): 4.019172051384877""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R->H_N-3R->C
Total Standard Deviation in ln(k): 4.019172051384877
""",
)

entry(
    index = 43,
    label = "Root_1R->H_N-3R->C_Ext-3BrClHO-R",
    kinetics = ArrheniusBM(A=(7.97811,'m^3/(mol*s)'), n=1.89323, w0=(298.55,'kJ/mol'), E0=(57.4032,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7222461975439702, var=3.100513572073411, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-3R->C_Ext-3BrClHO-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-3R->C_Ext-3BrClHO-R
    Total Standard Deviation in ln(k): 5.344681642749019"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-3R->C_Ext-3BrClHO-R
Total Standard Deviation in ln(k): 5.344681642749019""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-3R->C_Ext-3BrClHO-R
Total Standard Deviation in ln(k): 5.344681642749019
""",
)

entry(
    index = 44,
    label = "Root_1R->H_N-3R->C_Ext-3BrClHO-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1477.96,'m^3/(mol*s)'), n=1.20107, w0=(298.55,'kJ/mol'), E0=(76.4935,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.188211054393341, var=3.093550680807603, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-3R->C_Ext-3BrClHO-R_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->C_Ext-3BrClHO-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 6.511481695911503"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->C_Ext-3BrClHO-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 6.511481695911503""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->C_Ext-3BrClHO-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 6.511481695911503
""",
)

entry(
    index = 45,
    label = "Root_1R->H_N-3R->C_Ext-3BrClHO-R_Ext-4R!H-R_Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(1.49307,'m^3/(mol*s)'), n=1.95214, w0=(298.55,'kJ/mol'), E0=(52.3445,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->C_Ext-3BrClHO-R_Ext-4R!H-R_Sp-5R!H-4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_Ext-3BrClHO-R_Ext-4R!H-R_Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_Ext-3BrClHO-R_Ext-4R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_Ext-3BrClHO-R_Ext-4R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "Root_1R->H_N-3R->C_Ext-3BrClHO-R_Ext-4R!H-R_N-Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(0.214535,'m^3/(mol*s)'), n=2.40797, w0=(298.55,'kJ/mol'), E0=(61.5074,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->C_Ext-3BrClHO-R_Ext-4R!H-R_N-Sp-5R!H-4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_Ext-3BrClHO-R_Ext-4R!H-R_N-Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_Ext-3BrClHO-R_Ext-4R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_Ext-3BrClHO-R_Ext-4R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 47,
    label = "Root_1R->H_N-3R->C_3BrClHO-u1",
    kinetics = ArrheniusBM(A=(7.25323e+06,'m^3/(mol*s)'), n=0.191604, w0=(288.323,'kJ/mol'), E0=(57.5181,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.36933008988063826, var=2.778950055393995, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-3R->C_3BrClHO-u1',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-3R->C_3BrClHO-u1
    Total Standard Deviation in ln(k): 4.269895136390198"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-3R->C_3BrClHO-u1
Total Standard Deviation in ln(k): 4.269895136390198""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-3R->C_3BrClHO-u1
Total Standard Deviation in ln(k): 4.269895136390198
""",
)

entry(
    index = 48,
    label = "Root_1R->H_N-3R->C_3BrClHO-u1_3BrClHO->Br",
    kinetics = ArrheniusBM(A=(32771.6,'m^3/(mol*s)'), n=1.02226, w0=(276,'kJ/mol'), E0=(51.6139,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->C_3BrClHO-u1_3BrClHO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_3BrClHO-u1_3BrClHO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_3BrClHO-u1_3BrClHO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_3BrClHO-u1_3BrClHO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 49,
    label = "Root_1R->H_N-3R->C_3BrClHO-u1_N-3BrClHO->Br",
    kinetics = ArrheniusBM(A=(6.71177e+06,'m^3/(mol*s)'), n=0.200853, w0=(294.485,'kJ/mol'), E0=(57.4215,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3868248730619273, var=2.8763125523613398, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-3R->C_3BrClHO-u1_N-3BrClHO->Br',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->C_3BrClHO-u1_N-3BrClHO->Br
    Total Standard Deviation in ln(k): 4.371891342845465"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->C_3BrClHO-u1_N-3BrClHO->Br
Total Standard Deviation in ln(k): 4.371891342845465""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->C_3BrClHO-u1_N-3BrClHO->Br
Total Standard Deviation in ln(k): 4.371891342845465
""",
)

entry(
    index = 50,
    label = "Root_1R->H_N-3R->C_3BrClHO-u1_N-3BrClHO->Br_3ClO->O",
    kinetics = ArrheniusBM(A=(342.08,'m^3/(mol*s)'), n=1.58841, w0=(298.55,'kJ/mol'), E0=(43.8668,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->C_3BrClHO-u1_N-3BrClHO->Br_3ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_3BrClHO-u1_N-3BrClHO->Br_3ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_3BrClHO-u1_N-3BrClHO->Br_3ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_3BrClHO-u1_N-3BrClHO->Br_3ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 51,
    label = "Root_1R->H_N-3R->C_3BrClHO-u1_N-3BrClHO->Br_N-3ClO->O",
    kinetics = ArrheniusBM(A=(833562,'m^3/(mol*s)'), n=0.302768, w0=(290.42,'kJ/mol'), E0=(45.4088,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->C_3BrClHO-u1_N-3BrClHO->Br_N-3ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_3BrClHO-u1_N-3BrClHO->Br_N-3ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_3BrClHO-u1_N-3BrClHO->Br_N-3ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_3BrClHO-u1_N-3BrClHO->Br_N-3ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 52,
    label = "Root_1R->H_N-3R->C_N-3BrClHO-u1",
    kinetics = ArrheniusBM(A=(104.591,'m^3/(mol*s)'), n=1.68113, w0=(298.55,'kJ/mol'), E0=(39.6517,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->C_N-3BrClHO-u1',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_N-3BrClHO-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_N-3BrClHO-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_N-3BrClHO-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 53,
    label = "Root_N-1R->H",
    kinetics = ArrheniusBM(A=(3.1629e+12,'m^3/(mol*s)'), n=-1.46914, w0=(280.953,'kJ/mol'), E0=(71.4975,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4391197785891208, var=11.032102199271982, Tref=1000.0, N=162, data_mean=0.0, correlation='Root_N-1R->H',), comment="""BM rule fitted to 162 training reactions at node Root_N-1R->H
    Total Standard Deviation in ln(k): 7.761965107186772"""),
    rank = 11,
    shortDesc = """BM rule fitted to 162 training reactions at node Root_N-1R->H
Total Standard Deviation in ln(k): 7.761965107186772""",
    longDesc = 
"""
BM rule fitted to 162 training reactions at node Root_N-1R->H
Total Standard Deviation in ln(k): 7.761965107186772
""",
)

entry(
    index = 54,
    label = "Root_N-1R->H_3R->H",
    kinetics = ArrheniusBM(A=(1586.93,'m^3/(mol*s)'), n=1.51877, w0=(318.097,'kJ/mol'), E0=(45.8122,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.26347296149367216, var=0.7566116793688372, Tref=1000.0, N=38, data_mean=0.0, correlation='Root_N-1R->H_3R->H',), comment="""BM rule fitted to 38 training reactions at node Root_N-1R->H_3R->H
    Total Standard Deviation in ln(k): 2.405779663620572"""),
    rank = 11,
    shortDesc = """BM rule fitted to 38 training reactions at node Root_N-1R->H_3R->H
Total Standard Deviation in ln(k): 2.405779663620572""",
    longDesc = 
"""
BM rule fitted to 38 training reactions at node Root_N-1R->H_3R->H
Total Standard Deviation in ln(k): 2.405779663620572
""",
)

entry(
    index = 55,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.0129965,'m^3/(mol*s)'), n=2.97057, w0=(323.5,'kJ/mol'), E0=(29.7602,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09448409884389038, var=0.6922595534478609, Tref=1000.0, N=31, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C',), comment="""BM rule fitted to 31 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 1.9053796507983611"""),
    rank = 11,
    shortDesc = """BM rule fitted to 31 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 1.9053796507983611""",
    longDesc = 
"""
BM rule fitted to 31 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 1.9053796507983611
""",
)

entry(
    index = 56,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0",
    kinetics = ArrheniusBM(A=(0.000303475,'m^3/(mol*s)'), n=3.47146, w0=(323.5,'kJ/mol'), E0=(25.4076,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.044520384490985755, var=0.4550411714808703, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0',), comment="""BM rule fitted to 25 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0
    Total Standard Deviation in ln(k): 1.4641891829734894"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0
Total Standard Deviation in ln(k): 1.4641891829734894""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0
Total Standard Deviation in ln(k): 1.4641891829734894
""",
)

entry(
    index = 57,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.000290869,'m^3/(mol*s)'), n=3.47544, w0=(323.5,'kJ/mol'), E0=(24.7463,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04801716527319303, var=0.471133358705018, Tref=1000.0, N=23, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R',), comment="""BM rule fitted to 23 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R
    Total Standard Deviation in ln(k): 1.4966793592526886"""),
    rank = 11,
    shortDesc = """BM rule fitted to 23 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 1.4966793592526886""",
    longDesc = 
"""
BM rule fitted to 23 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 1.4966793592526886
""",
)

entry(
    index = 58,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C",
    kinetics = ArrheniusBM(A=(72.2329,'m^3/(mol*s)'), n=1.97455, w0=(323.5,'kJ/mol'), E0=(41.7854,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.36536960387529444, var=0.6239338455029545, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C
    Total Standard Deviation in ln(k): 2.501543957102505"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C
Total Standard Deviation in ln(k): 2.501543957102505""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C
Total Standard Deviation in ln(k): 2.501543957102505
""",
)

entry(
    index = 59,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(134.986,'m^3/(mol*s)'), n=1.87045, w0=(323.5,'kJ/mol'), E0=(42.7807,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.42724889559531704, var=0.6419994985002245, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_Ext-1C-R
    Total Standard Deviation in ln(k): 2.6797810861119156"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_Ext-1C-R
Total Standard Deviation in ln(k): 2.6797810861119156""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_Ext-1C-R
Total Standard Deviation in ln(k): 2.6797810861119156
""",
)

entry(
    index = 60,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_Ext-1C-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(890.982,'m^3/(mol*s)'), n=1.65484, w0=(323.5,'kJ/mol'), E0=(48.4541,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_Ext-1C-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_Ext-1C-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_Ext-1C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_Ext-1C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 61,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C",
    kinetics = ArrheniusBM(A=(0.000318475,'m^3/(mol*s)'), n=3.45426, w0=(323.5,'kJ/mol'), E0=(23.2289,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09187343940246825, var=0.509354311114861, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C',), comment="""BM rule fitted to 20 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C
    Total Standard Deviation in ln(k): 1.6615984218640032"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C
Total Standard Deviation in ln(k): 1.6615984218640032""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C
Total Standard Deviation in ln(k): 1.6615984218640032
""",
)

entry(
    index = 62,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.00031629,'m^3/(mol*s)'), n=3.46679, w0=(323.5,'kJ/mol'), E0=(14.5507,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17096317402076094, var=0.2943689491310361, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R',), comment="""BM rule fitted to 14 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R
    Total Standard Deviation in ln(k): 1.517240334998934"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R
Total Standard Deviation in ln(k): 1.517240334998934""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R
Total Standard Deviation in ln(k): 1.517240334998934
""",
)

entry(
    index = 63,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F",
    kinetics = ArrheniusBM(A=(0.0998388,'m^3/(mol*s)'), n=2.7508, w0=(323.5,'kJ/mol'), E0=(36.7881,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.033838942503948, var=0.2698683453046594, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F
    Total Standard Deviation in ln(k): 1.1264593711228748"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F
Total Standard Deviation in ln(k): 1.1264593711228748""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F
Total Standard Deviation in ln(k): 1.1264593711228748
""",
)

entry(
    index = 64,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_5R!H->Cl",
    kinetics = ArrheniusBM(A=(828.619,'m^3/(mol*s)'), n=1.64975, w0=(323.5,'kJ/mol'), E0=(50.637,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.25824678262697653, var=0.029506747071255984, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_5R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_5R!H->Cl
    Total Standard Deviation in ln(k): 0.9932251935985921"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_5R!H->Cl
Total Standard Deviation in ln(k): 0.9932251935985921""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_5R!H->Cl
Total Standard Deviation in ln(k): 0.9932251935985921
""",
)

entry(
    index = 65,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_5R!H->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(943.579,'m^3/(mol*s)'), n=1.62342, w0=(323.5,'kJ/mol'), E0=(49.287,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_5R!H->Cl_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_5R!H->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_5R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_5R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 66,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(8.9289e-05,'m^3/(mol*s)'), n=3.61987, w0=(323.5,'kJ/mol'), E0=(16.9934,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17113916976176682, var=0.18473778158664939, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl
    Total Standard Deviation in ln(k): 1.2916557689946904"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl
Total Standard Deviation in ln(k): 1.2916557689946904""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl
Total Standard Deviation in ln(k): 1.2916557689946904
""",
)

entry(
    index = 67,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C",
    kinetics = ArrheniusBM(A=(0.000189987,'m^3/(mol*s)'), n=3.53761, w0=(323.5,'kJ/mol'), E0=(10.783,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17647321685042552, var=0.09224334753538165, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C
    Total Standard Deviation in ln(k): 1.0522699593844373"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C
Total Standard Deviation in ln(k): 1.0522699593844373""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C
Total Standard Deviation in ln(k): 1.0522699593844373
""",
)

entry(
    index = 68,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(11.1825,'m^3/(mol*s)'), n=2.14797, w0=(323.5,'kJ/mol'), E0=(43.7972,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.18098631932139003, var=0.06526655934873365, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R
    Total Standard Deviation in ln(k): 0.9668955946163034"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R
Total Standard Deviation in ln(k): 0.9668955946163034""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R
Total Standard Deviation in ln(k): 0.9668955946163034
""",
)

entry(
    index = 69,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(741.601,'m^3/(mol*s)'), n=1.63349, w0=(323.5,'kJ/mol'), E0=(52.3283,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2083020493037463, var=0.02909400748016003, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 0.86531895529907"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_Ext-1C-R
Total Standard Deviation in ln(k): 0.86531895529907""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_Ext-1C-R
Total Standard Deviation in ln(k): 0.86531895529907
""",
)

entry(
    index = 70,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_Ext-1C-R_6R!H->Br",
    kinetics = ArrheniusBM(A=(659.135,'m^3/(mol*s)'), n=1.65584, w0=(323.5,'kJ/mol'), E0=(52.1817,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_Ext-1C-R_6R!H->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_Ext-1C-R_6R!H->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_Ext-1C-R_6R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_Ext-1C-R_6R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 71,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_Ext-1C-R_N-6R!H->Br",
    kinetics = ArrheniusBM(A=(590.348,'m^3/(mol*s)'), n=1.65419, w0=(323.5,'kJ/mol'), E0=(52.0148,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_Ext-1C-R_N-6R!H->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_Ext-1C-R_N-6R!H->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_Ext-1C-R_N-6R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_Ext-1C-R_N-6R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 72,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_6R!H->F",
    kinetics = ArrheniusBM(A=(384.224,'m^3/(mol*s)'), n=1.70269, w0=(323.5,'kJ/mol'), E0=(44.972,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_6R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_6R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 73,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_N-6R!H->F",
    kinetics = ArrheniusBM(A=(401.227,'m^3/(mol*s)'), n=1.6928, w0=(323.5,'kJ/mol'), E0=(47.0803,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_N-6R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_N-6R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_N-6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_N-6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 74,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-1C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(874.403,'m^3/(mol*s)'), n=1.67238, w0=(323.5,'kJ/mol'), E0=(44.3198,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-1C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-1C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 75,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-1C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(898.897,'m^3/(mol*s)'), n=1.67337, w0=(323.5,'kJ/mol'), E0=(47.1774,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-1C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-1C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 76,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C",
    kinetics = ArrheniusBM(A=(2.92878,'m^3/(mol*s)'), n=2.30847, w0=(323.5,'kJ/mol'), E0=(43.5143,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.19642718735610937, var=0.4079552543226393, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C
    Total Standard Deviation in ln(k): 1.7739875054796288"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C
Total Standard Deviation in ln(k): 1.7739875054796288""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C
Total Standard Deviation in ln(k): 1.7739875054796288
""",
)

entry(
    index = 77,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(4.97995e-05,'m^3/(mol*s)'), n=3.69989, w0=(323.5,'kJ/mol'), E0=(18.0903,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3036302398105292, var=2.2752221819037985, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_Ext-1C-R
    Total Standard Deviation in ln(k): 3.7868002919544663"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.7868002919544663""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.7868002919544663
""",
)

entry(
    index = 78,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_Ext-1C-R_5BrF->Br",
    kinetics = ArrheniusBM(A=(579.05,'m^3/(mol*s)'), n=1.60333, w0=(323.5,'kJ/mol'), E0=(50.4739,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_Ext-1C-R_5BrF->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_Ext-1C-R_5BrF->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_Ext-1C-R_5BrF->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_Ext-1C-R_5BrF->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 79,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_Ext-1C-R_N-5BrF->Br",
    kinetics = ArrheniusBM(A=(1349.13,'m^3/(mol*s)'), n=1.64247, w0=(323.5,'kJ/mol'), E0=(50.6966,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_Ext-1C-R_N-5BrF->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_Ext-1C-R_N-5BrF->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_Ext-1C-R_N-5BrF->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_Ext-1C-R_N-5BrF->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 80,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_5BrF->Br",
    kinetics = ArrheniusBM(A=(455.069,'m^3/(mol*s)'), n=1.66953, w0=(323.5,'kJ/mol'), E0=(50.3346,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_5BrF->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_5BrF->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_5BrF->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_5BrF->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 81,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_N-5BrF->Br",
    kinetics = ArrheniusBM(A=(353.002,'m^3/(mol*s)'), n=1.6735, w0=(323.5,'kJ/mol'), E0=(51.0443,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_N-5BrF->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_N-5BrF->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_N-5BrF->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_N-5BrF->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 82,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-4R!H->F",
    kinetics = ArrheniusBM(A=(656.056,'m^3/(mol*s)'), n=1.65652, w0=(323.5,'kJ/mol'), E0=(34.17,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.46257225116661277, var=0.46957433762863793, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-4R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-4R!H->F
    Total Standard Deviation in ln(k): 2.5359964593490076"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-4R!H->F
Total Standard Deviation in ln(k): 2.5359964593490076""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-4R!H->F
Total Standard Deviation in ln(k): 2.5359964593490076
""",
)

entry(
    index = 83,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-4R!H->F_Ext-5R!H-R_6R!H->F",
    kinetics = ArrheniusBM(A=(544.736,'m^3/(mol*s)'), n=1.68578, w0=(323.5,'kJ/mol'), E0=(37.2823,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-4R!H->F_Ext-5R!H-R_6R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-4R!H->F_Ext-5R!H-R_6R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-4R!H->F_Ext-5R!H-R_6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-4R!H->F_Ext-5R!H-R_6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 84,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-4R!H->F_Ext-5R!H-R_N-6R!H->F",
    kinetics = ArrheniusBM(A=(684.364,'m^3/(mol*s)'), n=1.64514, w0=(323.5,'kJ/mol'), E0=(30.6475,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-4R!H->F_Ext-5R!H-R_N-6R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-4R!H->F_Ext-5R!H-R_N-6R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-4R!H->F_Ext-5R!H-R_N-6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-4R!H->F_Ext-5R!H-R_N-6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 85,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(247.051,'m^3/(mol*s)'), n=1.6473, w0=(323.5,'kJ/mol'), E0=(44.05,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2674695990644603, var=11.047891544188142, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 7.335446535082747"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R
Total Standard Deviation in ln(k): 7.335446535082747""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R
Total Standard Deviation in ln(k): 7.335446535082747
""",
)

entry(
    index = 86,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(650.121,'m^3/(mol*s)'), n=1.74726, w0=(323.5,'kJ/mol'), E0=(48.3078,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 87,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F",
    kinetics = ArrheniusBM(A=(349.197,'m^3/(mol*s)'), n=1.7256, w0=(323.5,'kJ/mol'), E0=(51.8131,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 88,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F",
    kinetics = ArrheniusBM(A=(1.93642e-05,'m^3/(mol*s)'), n=3.84839, w0=(323.5,'kJ/mol'), E0=(17.1028,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3301063494560454, var=0.3407507701637398, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F
    Total Standard Deviation in ln(k): 1.9996542150302936"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F
Total Standard Deviation in ln(k): 1.9996542150302936""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F
Total Standard Deviation in ln(k): 1.9996542150302936
""",
)

entry(
    index = 89,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_4BrCCl->Cl",
    kinetics = ArrheniusBM(A=(371.066,'m^3/(mol*s)'), n=1.71693, w0=(323.5,'kJ/mol'), E0=(54.1921,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_4BrCCl->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_4BrCCl->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_4BrCCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_4BrCCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 90,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_N-4BrCCl->Cl",
    kinetics = ArrheniusBM(A=(1.97983e-05,'m^3/(mol*s)'), n=3.8681, w0=(323.5,'kJ/mol'), E0=(17.1588,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1751193851205436, var=1.2271067861179352, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_N-4BrCCl->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_N-4BrCCl->Cl
    Total Standard Deviation in ln(k): 2.6607407723647953"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_N-4BrCCl->Cl
Total Standard Deviation in ln(k): 2.6607407723647953""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_N-4BrCCl->Cl
Total Standard Deviation in ln(k): 2.6607407723647953
""",
)

entry(
    index = 91,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_N-4BrCCl->Cl_4BrC->Br",
    kinetics = ArrheniusBM(A=(539.35,'m^3/(mol*s)'), n=1.7149, w0=(323.5,'kJ/mol'), E0=(52.3118,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_N-4BrCCl->Cl_4BrC->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_N-4BrCCl->Cl_4BrC->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_N-4BrCCl->Cl_4BrC->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_N-4BrCCl->Cl_4BrC->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 92,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_N-4BrCCl->Cl_N-4BrC->Br",
    kinetics = ArrheniusBM(A=(506.769,'m^3/(mol*s)'), n=1.76845, w0=(323.5,'kJ/mol'), E0=(46.9141,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_N-4BrCCl->Cl_N-4BrC->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_N-4BrCCl->Cl_N-4BrC->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_N-4BrCCl->Cl_N-4BrC->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_N-4BrCCl->Cl_N-4BrC->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 93,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0",
    kinetics = ArrheniusBM(A=(44.973,'m^3/(mol*s)'), n=1.82297, w0=(323.5,'kJ/mol'), E0=(31.9078,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.15485088832030697, var=2.593726157346707, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0
    Total Standard Deviation in ln(k): 3.6177083265043546"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0
Total Standard Deviation in ln(k): 3.6177083265043546""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0
Total Standard Deviation in ln(k): 3.6177083265043546
""",
)

entry(
    index = 94,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.65556,'m^3/(mol*s)'), n=2.05058, w0=(323.5,'kJ/mol'), E0=(27.4116,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0953946632281141, var=2.0283738612514406, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R
    Total Standard Deviation in ln(k): 3.094848643068825"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 3.094848643068825""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 3.094848643068825
""",
)

entry(
    index = 95,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(4.15552e-08,'m^3/(mol*s)'), n=4.4399, w0=(323.5,'kJ/mol'), E0=(0.391193,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2876209225991324, var=1.302661546771392, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C
    Total Standard Deviation in ln(k): 3.0107539649099047"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C
Total Standard Deviation in ln(k): 3.0107539649099047""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C
Total Standard Deviation in ln(k): 3.0107539649099047
""",
)

entry(
    index = 96,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C",
    kinetics = ArrheniusBM(A=(3.04739e-08,'m^3/(mol*s)'), n=4.46176, w0=(323.5,'kJ/mol'), E0=(0.315788,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2335801824795302, var=7.264710502746058, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C
    Total Standard Deviation in ln(k): 5.990272776973767"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C
Total Standard Deviation in ln(k): 5.990272776973767""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C
Total Standard Deviation in ln(k): 5.990272776973767
""",
)

entry(
    index = 97,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(4.00122,'m^3/(mol*s)'), n=2.16923, w0=(323.5,'kJ/mol'), E0=(30.8635,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.38430482972079294, var=10.477681059877924, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C
    Total Standard Deviation in ln(k): 7.454766372935232"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C
Total Standard Deviation in ln(k): 7.454766372935232""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C
Total Standard Deviation in ln(k): 7.454766372935232
""",
)

entry(
    index = 98,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_N-Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(2625.75,'m^3/(mol*s)'), n=1.23946, w0=(323.5,'kJ/mol'), E0=(26.3133,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_N-Sp-4R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_N-Sp-4R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 99,
    label = "Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(185596,'m^3/(mol*s)'), n=0.927587, w0=(294.167,'kJ/mol'), E0=(53.8056,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.235313774409862, var=1.2590668543122734, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 2.8407167477252018"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 2.8407167477252018""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 2.8407167477252018
""",
)

entry(
    index = 100,
    label = "Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl",
    kinetics = ArrheniusBM(A=(381135,'m^3/(mol*s)'), n=0.513067, w0=(290.42,'kJ/mol'), E0=(39.8411,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 101,
    label = "Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl",
    kinetics = ArrheniusBM(A=(4579.14,'m^3/(mol*s)'), n=1.45323, w0=(294.792,'kJ/mol'), E0=(46.556,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.20064636664349816, var=0.682244739527598, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl
    Total Standard Deviation in ln(k): 2.1600098378906187"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl
Total Standard Deviation in ln(k): 2.1600098378906187""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl
Total Standard Deviation in ln(k): 2.1600098378906187
""",
)

entry(
    index = 102,
    label = "Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0",
    kinetics = ArrheniusBM(A=(908.229,'m^3/(mol*s)'), n=1.69116, w0=(294.04,'kJ/mol'), E0=(32.7716,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.035253335475806204, var=0.16271859560187563, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0
    Total Standard Deviation in ln(k): 0.8972541354562763"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0
Total Standard Deviation in ln(k): 0.8972541354562763""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0
Total Standard Deviation in ln(k): 0.8972541354562763
""",
)

entry(
    index = 103,
    label = "Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_1BrO->Br",
    kinetics = ArrheniusBM(A=(114000,'m^3/(mol*s)'), n=1, w0=(276,'kJ/mol'), E0=(47.5991,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_1BrO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_1BrO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_1BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_1BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 104,
    label = "Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br",
    kinetics = ArrheniusBM(A=(904.631,'m^3/(mol*s)'), n=1.69177, w0=(298.55,'kJ/mol'), E0=(33.932,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04598567697655498, var=0.17902876681910643, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br
    Total Standard Deviation in ln(k): 0.9637812205043058"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br
Total Standard Deviation in ln(k): 0.9637812205043058""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br
Total Standard Deviation in ln(k): 0.9637812205043058
""",
)

entry(
    index = 105,
    label = "Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br_Ext-1O-R",
    kinetics = ArrheniusBM(A=(795.463,'m^3/(mol*s)'), n=1.69349, w0=(298.55,'kJ/mol'), E0=(42.5979,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.10606040464386511, var=0.18459446535967378, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br_Ext-1O-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br_Ext-1O-R
    Total Standard Deviation in ln(k): 1.1278069896429856"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br_Ext-1O-R
Total Standard Deviation in ln(k): 1.1278069896429856""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br_Ext-1O-R
Total Standard Deviation in ln(k): 1.1278069896429856
""",
)

entry(
    index = 106,
    label = "Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br_Ext-1O-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(675.746,'m^3/(mol*s)'), n=1.70325, w0=(298.55,'kJ/mol'), E0=(39.3245,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4643189208425385, var=1.4399756945988365, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br_Ext-1O-R_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br_Ext-1O-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 3.5722922447112433"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br_Ext-1O-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 3.5722922447112433""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br_Ext-1O-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 3.5722922447112433
""",
)

entry(
    index = 107,
    label = "Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br_Ext-1O-R_Ext-4R!H-R_Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(2137.95,'m^3/(mol*s)'), n=1.58633, w0=(298.55,'kJ/mol'), E0=(51.6296,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br_Ext-1O-R_Ext-4R!H-R_Sp-5R!H-4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br_Ext-1O-R_Ext-4R!H-R_Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br_Ext-1O-R_Ext-4R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br_Ext-1O-R_Ext-4R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 108,
    label = "Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br_Ext-1O-R_Ext-4R!H-R_N-Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(1865.29,'m^3/(mol*s)'), n=1.5505, w0=(298.55,'kJ/mol'), E0=(69.321,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br_Ext-1O-R_Ext-4R!H-R_N-Sp-5R!H-4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br_Ext-1O-R_Ext-4R!H-R_N-Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br_Ext-1O-R_Ext-4R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br_Ext-1O-R_Ext-4R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 109,
    label = "Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0",
    kinetics = ArrheniusBM(A=(23904.8,'m^3/(mol*s)'), n=1.10058, w0=(298.55,'kJ/mol'), E0=(43.2762,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 110,
    label = "Root_N-1R->H_N-3R->H",
    kinetics = ArrheniusBM(A=(8.6308e+08,'m^3/(mol*s)'), n=-0.558341, w0=(269.571,'kJ/mol'), E0=(62.1293,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2905298168786524, var=13.01260748236256, Tref=1000.0, N=124, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H',), comment="""BM rule fitted to 124 training reactions at node Root_N-1R->H_N-3R->H
    Total Standard Deviation in ln(k): 7.961653645172024"""),
    rank = 11,
    shortDesc = """BM rule fitted to 124 training reactions at node Root_N-1R->H_N-3R->H
Total Standard Deviation in ln(k): 7.961653645172024""",
    longDesc = 
"""
BM rule fitted to 124 training reactions at node Root_N-1R->H_N-3R->H
Total Standard Deviation in ln(k): 7.961653645172024
""",
)

entry(
    index = 111,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(3.56609e+09,'m^3/(mol*s)'), n=-0.746808, w0=(279.113,'kJ/mol'), E0=(69.9261,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3555232498357281, var=7.64753695247773, Tref=1000.0, N=96, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C',), comment="""BM rule fitted to 96 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 6.437205051509255"""),
    rank = 11,
    shortDesc = """BM rule fitted to 96 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 6.437205051509255""",
    longDesc = 
"""
BM rule fitted to 96 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 6.437205051509255
""",
)

entry(
    index = 112,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1",
    kinetics = ArrheniusBM(A=(1.27223e+07,'m^3/(mol*s)'), n=-0.0699347, w0=(279.712,'kJ/mol'), E0=(64.9598,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.29214818951422045, var=6.410377959810965, Tref=1000.0, N=88, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1',), comment="""BM rule fitted to 88 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1
    Total Standard Deviation in ln(k): 5.80977413245842"""),
    rank = 11,
    shortDesc = """BM rule fitted to 88 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1
Total Standard Deviation in ln(k): 5.80977413245842""",
    longDesc = 
"""
BM rule fitted to 88 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1
Total Standard Deviation in ln(k): 5.80977413245842
""",
)

entry(
    index = 113,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C",
    kinetics = ArrheniusBM(A=(41178.4,'m^3/(mol*s)'), n=0.623757, w0=(285,'kJ/mol'), E0=(59.4658,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.22271957422891273, var=5.510011081575291, Tref=1000.0, N=76, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C',), comment="""BM rule fitted to 76 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C
    Total Standard Deviation in ln(k): 5.26539432143077"""),
    rank = 11,
    shortDesc = """BM rule fitted to 76 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C
Total Standard Deviation in ln(k): 5.26539432143077""",
    longDesc = 
"""
BM rule fitted to 76 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C
Total Standard Deviation in ln(k): 5.26539432143077
""",
)

entry(
    index = 114,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.204674,'m^3/(mol*s)'), n=2.06813, w0=(285,'kJ/mol'), E0=(47.3422,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.014422164036486522, var=4.649715387058696, Tref=1000.0, N=56, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R',), comment="""BM rule fitted to 56 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R
    Total Standard Deviation in ln(k): 4.3590866769920416"""),
    rank = 11,
    shortDesc = """BM rule fitted to 56 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R
Total Standard Deviation in ln(k): 4.3590866769920416""",
    longDesc = 
"""
BM rule fitted to 56 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R
Total Standard Deviation in ln(k): 4.3590866769920416
""",
)

entry(
    index = 115,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C",
    kinetics = ArrheniusBM(A=(1.06979e-16,'m^3/(mol*s)'), n=6.70875, w0=(285,'kJ/mol'), E0=(-8.19309,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3039617715624239, var=6.239062638386861, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C
    Total Standard Deviation in ln(k): 5.771173514889917"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C
Total Standard Deviation in ln(k): 5.771173514889917""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C
Total Standard Deviation in ln(k): 5.771173514889917
""",
)

entry(
    index = 116,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(0.000113191,'m^3/(mol*s)'), n=3.35911, w0=(285,'kJ/mol'), E0=(53.2652,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.13669033296711564, var=5.813706754943242, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 5.177185983970883"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-4R!H-R
Total Standard Deviation in ln(k): 5.177185983970883""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-4R!H-R
Total Standard Deviation in ln(k): 5.177185983970883
""",
)

entry(
    index = 117,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-4R!H-R_Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(0.000423303,'m^3/(mol*s)'), n=3.19649, w0=(285,'kJ/mol'), E0=(47.2037,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-4R!H-R_Sp-5R!H-4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-4R!H-R_Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-4R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-4R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 118,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-4R!H-R_N-Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(0.000626686,'m^3/(mol*s)'), n=3.14466, w0=(285,'kJ/mol'), E0=(62.6922,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-4R!H-R_N-Sp-5R!H-4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-4R!H-R_N-Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-4R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-4R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 119,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.83859e-12,'m^3/(mol*s)'), n=5.3436, w0=(285,'kJ/mol'), E0=(4.75456,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.22842702507804474, var=13.617019473487016, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R
    Total Standard Deviation in ln(k): 7.971659450057285"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R
Total Standard Deviation in ln(k): 7.971659450057285""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R
Total Standard Deviation in ln(k): 7.971659450057285
""",
)

entry(
    index = 120,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(0.0026651,'m^3/(mol*s)'), n=3.02759, w0=(285,'kJ/mol'), E0=(36.2941,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 121,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.000323684,'m^3/(mol*s)'), n=2.67488, w0=(285,'kJ/mol'), E0=(38.5775,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.07618010463556793, var=25.082452301952227, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 10.231598580717034"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_Ext-1C-R
Total Standard Deviation in ln(k): 10.231598580717034""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_Ext-1C-R
Total Standard Deviation in ln(k): 10.231598580717034
""",
)

entry(
    index = 122,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.00301022,'m^3/(mol*s)'), n=2.08084, w0=(285,'kJ/mol'), E0=(37.3238,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 123,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.00304471,'m^3/(mol*s)'), n=2.97709, w0=(285,'kJ/mol'), E0=(36.0726,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 124,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C",
    kinetics = ArrheniusBM(A=(0.00825622,'m^3/(mol*s)'), n=2.42392, w0=(285,'kJ/mol'), E0=(43.5215,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.05074466069838507, var=4.160631910363266, Tref=1000.0, N=48, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C',), comment="""BM rule fitted to 48 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C
    Total Standard Deviation in ln(k): 4.2166830004328135"""),
    rank = 11,
    shortDesc = """BM rule fitted to 48 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C
Total Standard Deviation in ln(k): 4.2166830004328135""",
    longDesc = 
"""
BM rule fitted to 48 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C
Total Standard Deviation in ln(k): 4.2166830004328135
""",
)

entry(
    index = 125,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br",
    kinetics = ArrheniusBM(A=(0.000576867,'m^3/(mol*s)'), n=2.58853, w0=(285,'kJ/mol'), E0=(40.736,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09028494436167352, var=5.0053452007969135, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br
    Total Standard Deviation in ln(k): 4.711965969705408"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br
Total Standard Deviation in ln(k): 4.711965969705408""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br
Total Standard Deviation in ln(k): 4.711965969705408
""",
)

entry(
    index = 126,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.00104192,'m^3/(mol*s)'), n=2.4822, w0=(285,'kJ/mol'), E0=(40.3523,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.184761708062462, var=7.715769042700143, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R
    Total Standard Deviation in ln(k): 6.03283278319661"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R
Total Standard Deviation in ln(k): 6.03283278319661""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R
Total Standard Deviation in ln(k): 6.03283278319661
""",
)

entry(
    index = 127,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.05699e-06,'m^3/(mol*s)'), n=3.53644, w0=(285,'kJ/mol'), E0=(32.4846,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1923795851987931, var=0.4884220170208299, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 1.884418925559909"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 1.884418925559909""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 1.884418925559909
""",
)

entry(
    index = 128,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.00011293,'m^3/(mol*s)'), n=3.02471, w0=(285,'kJ/mol'), E0=(33.1671,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0046382544112912325, var=0.14749366805386255, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 0.7815704951280834"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R_Ext-1C-R
Total Standard Deviation in ln(k): 0.7815704951280834""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R_Ext-1C-R
Total Standard Deviation in ln(k): 0.7815704951280834
""",
)

entry(
    index = 129,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R_Ext-1C-R_7R!H->Cl",
    kinetics = ArrheniusBM(A=(4.43199e-05,'m^3/(mol*s)'), n=3.11015, w0=(285,'kJ/mol'), E0=(31.4635,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R_Ext-1C-R_7R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R_Ext-1C-R_7R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R_Ext-1C-R_7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R_Ext-1C-R_7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 130,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R_Ext-1C-R_N-7R!H->Cl",
    kinetics = ArrheniusBM(A=(6.82116e-05,'m^3/(mol*s)'), n=3.11838, w0=(285,'kJ/mol'), E0=(33.3346,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R_Ext-1C-R_N-7R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R_Ext-1C-R_N-7R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R_Ext-1C-R_N-7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R_Ext-1C-R_N-7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 131,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.000640323,'m^3/(mol*s)'), n=2.17818, w0=(285,'kJ/mol'), E0=(40.9351,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1926142048073511, var=0.18373038768678374, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 1.343260577970662"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-1C-R
Total Standard Deviation in ln(k): 1.343260577970662""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-1C-R
Total Standard Deviation in ln(k): 1.343260577970662
""",
)

entry(
    index = 132,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-1C-R_6R!H->Cl",
    kinetics = ArrheniusBM(A=(0.000746917,'m^3/(mol*s)'), n=2.18514, w0=(285,'kJ/mol'), E0=(43.9027,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-1C-R_6R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-1C-R_6R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-1C-R_6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-1C-R_6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 133,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-1C-R_N-6R!H->Cl",
    kinetics = ArrheniusBM(A=(0.000258195,'m^3/(mol*s)'), n=2.26509, w0=(285,'kJ/mol'), E0=(37.1184,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-1C-R_N-6R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-1C-R_N-6R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-1C-R_N-6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-1C-R_N-6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 134,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-1C-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(0.000205056,'m^3/(mol*s)'), n=2.81796, w0=(285,'kJ/mol'), E0=(43.2327,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-1C-R_5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-1C-R_5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-1C-R_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-1C-R_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 135,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-1C-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(0.000313942,'m^3/(mol*s)'), n=2.76015, w0=(285,'kJ/mol'), E0=(42.5695,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-1C-R_N-5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-1C-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-1C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-1C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 136,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br",
    kinetics = ArrheniusBM(A=(0.0120844,'m^3/(mol*s)'), n=2.40982, w0=(285,'kJ/mol'), E0=(43.9154,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04506013643035528, var=3.9900055525961884, Tref=1000.0, N=40, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br',), comment="""BM rule fitted to 40 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br
    Total Standard Deviation in ln(k): 4.117674390321688"""),
    rank = 11,
    shortDesc = """BM rule fitted to 40 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br
Total Standard Deviation in ln(k): 4.117674390321688""",
    longDesc = 
"""
BM rule fitted to 40 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br
Total Standard Deviation in ln(k): 4.117674390321688
""",
)

entry(
    index = 137,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.00221595,'m^3/(mol*s)'), n=2.70391, w0=(285,'kJ/mol'), E0=(41.5753,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.13078281576751133, var=3.0905046006381633, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R',), comment="""BM rule fitted to 25 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R
    Total Standard Deviation in ln(k): 3.8528904374856414"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R
Total Standard Deviation in ln(k): 3.8528904374856414""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R
Total Standard Deviation in ln(k): 3.8528904374856414
""",
)

entry(
    index = 138,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_4CClFO->O",
    kinetics = ArrheniusBM(A=(1.2265e-06,'m^3/(mol*s)'), n=3.76713, w0=(285,'kJ/mol'), E0=(36.9947,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_4CClFO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_4CClFO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_4CClFO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_4CClFO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 139,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O",
    kinetics = ArrheniusBM(A=(0.00327856,'m^3/(mol*s)'), n=2.64975, w0=(285,'kJ/mol'), E0=(41.8544,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11679549557654674, var=3.2112854530815946, Tref=1000.0, N=24, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O',), comment="""BM rule fitted to 24 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O
    Total Standard Deviation in ln(k): 3.8859532776357"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O
Total Standard Deviation in ln(k): 3.8859532776357""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O
Total Standard Deviation in ln(k): 3.8859532776357
""",
)

entry(
    index = 140,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.0248588,'m^3/(mol*s)'), n=2.33446, w0=(285,'kJ/mol'), E0=(41.977,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.030170738243272266, var=3.7236931534025635, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R',), comment="""BM rule fitted to 19 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R
    Total Standard Deviation in ln(k): 3.944317734015101"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R
Total Standard Deviation in ln(k): 3.944317734015101""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R
Total Standard Deviation in ln(k): 3.944317734015101
""",
)

entry(
    index = 141,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(1.3581,'m^3/(mol*s)'), n=2.00184, w0=(285,'kJ/mol'), E0=(44.7039,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.008332823594901463, var=1.0867320114472125, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 2.110801679026811"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 2.110801679026811""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 2.110801679026811
""",
)

entry(
    index = 142,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_7R!H->Br",
    kinetics = ArrheniusBM(A=(0.000381437,'m^3/(mol*s)'), n=3.1179, w0=(285,'kJ/mol'), E0=(39.7149,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_7R!H->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_7R!H->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_7R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_7R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 143,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br",
    kinetics = ArrheniusBM(A=(8.70309,'m^3/(mol*s)'), n=1.74607, w0=(285,'kJ/mol'), E0=(45.7457,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.024910187569321122, var=1.6039132868367632, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br
    Total Standard Deviation in ln(k): 2.6014991464720563"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br
Total Standard Deviation in ln(k): 2.6014991464720563""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br
Total Standard Deviation in ln(k): 2.6014991464720563
""",
)

entry(
    index = 144,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br_7CClFINOPSSi->Cl",
    kinetics = ArrheniusBM(A=(0.000661896,'m^3/(mol*s)'), n=3.04672, w0=(285,'kJ/mol'), E0=(40.4365,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.055339376828988, var=1.9151043117170548, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br_7CClFINOPSSi->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br_7CClFINOPSSi->Cl
    Total Standard Deviation in ln(k): 2.9133422841487726"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br_7CClFINOPSSi->Cl
Total Standard Deviation in ln(k): 2.9133422841487726""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br_7CClFINOPSSi->Cl
Total Standard Deviation in ln(k): 2.9133422841487726
""",
)

entry(
    index = 145,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br_7CClFINOPSSi->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.000586117,'m^3/(mol*s)'), n=3.12075, w0=(285,'kJ/mol'), E0=(40.001,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br_7CClFINOPSSi->Cl_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br_7CClFINOPSSi->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br_7CClFINOPSSi->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br_7CClFINOPSSi->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 146,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br_N-7CClFINOPSSi->Cl",
    kinetics = ArrheniusBM(A=(148016,'m^3/(mol*s)'), n=0.4134, w0=(285,'kJ/mol'), E0=(51.3962,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.02688097021999166, var=8.408480422887102, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br_N-7CClFINOPSSi->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br_N-7CClFINOPSSi->Cl
    Total Standard Deviation in ln(k): 5.880746594216569"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br_N-7CClFINOPSSi->Cl
Total Standard Deviation in ln(k): 5.880746594216569""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br_N-7CClFINOPSSi->Cl
Total Standard Deviation in ln(k): 5.880746594216569
""",
)

entry(
    index = 147,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br_N-7CClFINOPSSi->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.47957e+08,'m^3/(mol*s)'), n=-0.551496, w0=(285,'kJ/mol'), E0=(49.5363,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br_N-7CClFINOPSSi->Cl_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br_N-7CClFINOPSSi->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br_N-7CClFINOPSSi->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br_N-7CClFINOPSSi->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 148,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br",
    kinetics = ArrheniusBM(A=(0.000123642,'m^3/(mol*s)'), n=3.12707, w0=(285,'kJ/mol'), E0=(37.7617,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.08820969906517935, var=0.4847375858848096, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br
    Total Standard Deviation in ln(k): 1.6173910893407242"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br
Total Standard Deviation in ln(k): 1.6173910893407242""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br
Total Standard Deviation in ln(k): 1.6173910893407242
""",
)

entry(
    index = 149,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.000211037,'m^3/(mol*s)'), n=3.03539, w0=(285,'kJ/mol'), E0=(33.0559,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.002138859588203227, var=0.11257589852128522, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_Ext-1C-R
    Total Standard Deviation in ln(k): 0.6780093887227377"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_Ext-1C-R
Total Standard Deviation in ln(k): 0.6780093887227377""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_Ext-1C-R
Total Standard Deviation in ln(k): 0.6780093887227377
""",
)

entry(
    index = 150,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_Ext-1C-R_4CClF->Cl",
    kinetics = ArrheniusBM(A=(8.62315e-05,'m^3/(mol*s)'), n=3.11892, w0=(285,'kJ/mol'), E0=(31.4714,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_Ext-1C-R_4CClF->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_Ext-1C-R_4CClF->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_Ext-1C-R_4CClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_Ext-1C-R_4CClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 151,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_Ext-1C-R_N-4CClF->Cl",
    kinetics = ArrheniusBM(A=(0.000139321,'m^3/(mol*s)'), n=3.1149, w0=(285,'kJ/mol'), E0=(33.2432,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_Ext-1C-R_N-4CClF->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_Ext-1C-R_N-4CClF->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_Ext-1C-R_N-4CClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_Ext-1C-R_N-4CClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 152,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_4CClF->Cl",
    kinetics = ArrheniusBM(A=(8.64676e-05,'m^3/(mol*s)'), n=3.24132, w0=(285,'kJ/mol'), E0=(42.8094,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_4CClF->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_4CClF->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_4CClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_4CClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 153,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_N-4CClF->Cl",
    kinetics = ArrheniusBM(A=(6.23785e-05,'m^3/(mol*s)'), n=3.19274, w0=(285,'kJ/mol'), E0=(42.0948,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_N-4CClF->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_N-4CClF->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_N-4CClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_N-4CClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 154,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br",
    kinetics = ArrheniusBM(A=(0.22441,'m^3/(mol*s)'), n=1.92501, w0=(285,'kJ/mol'), E0=(44.5759,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.007535248510732998, var=5.039986522665189, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br
    Total Standard Deviation in ln(k): 4.519545854217711"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br
Total Standard Deviation in ln(k): 4.519545854217711""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br
Total Standard Deviation in ln(k): 4.519545854217711
""",
)

entry(
    index = 155,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_Sp-6CCFF=1C",
    kinetics = ArrheniusBM(A=(0.0107137,'m^3/(mol*s)'), n=2.39107, w0=(285,'kJ/mol'), E0=(39.8079,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1312460803063958, var=57.73773294430883, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_Sp-6CCFF=1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_Sp-6CCFF=1C
    Total Standard Deviation in ln(k): 15.56281351362553"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_Sp-6CCFF=1C
Total Standard Deviation in ln(k): 15.56281351362553""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_Sp-6CCFF=1C
Total Standard Deviation in ln(k): 15.56281351362553
""",
)

entry(
    index = 156,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_Sp-6CCFF=1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.00774663,'m^3/(mol*s)'), n=2.01884, w0=(285,'kJ/mol'), E0=(37.4737,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_Sp-6CCFF=1C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_Sp-6CCFF=1C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_Sp-6CCFF=1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_Sp-6CCFF=1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 157,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C",
    kinetics = ArrheniusBM(A=(0.0045249,'m^3/(mol*s)'), n=2.38889, w0=(285,'kJ/mol'), E0=(40.6719,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.023053196350276205, var=3.4656448210005717, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C
    Total Standard Deviation in ln(k): 3.7899860241589596"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C
Total Standard Deviation in ln(k): 3.7899860241589596""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C
Total Standard Deviation in ln(k): 3.7899860241589596
""",
)

entry(
    index = 158,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.011887,'m^3/(mol*s)'), n=2.38814, w0=(285,'kJ/mol'), E0=(41.3384,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12304881103459353, var=3.3384100593195876, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R
    Total Standard Deviation in ln(k): 3.972082772791382"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R
Total Standard Deviation in ln(k): 3.972082772791382""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R
Total Standard Deviation in ln(k): 3.972082772791382
""",
)

entry(
    index = 159,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.00196709,'m^3/(mol*s)'), n=2.79477, w0=(285,'kJ/mol'), E0=(39.8944,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1827466684519542, var=0.6355484962096422, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 2.0573632593307467"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 2.0573632593307467""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 2.0573632593307467
""",
)

entry(
    index = 160,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_9R!H->Cl",
    kinetics = ArrheniusBM(A=(0.00179019,'m^3/(mol*s)'), n=2.84887, w0=(285,'kJ/mol'), E0=(39.9705,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_9R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_9R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_9R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_9R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 161,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_N-9R!H->Cl",
    kinetics = ArrheniusBM(A=(0.00375254,'m^3/(mol*s)'), n=2.67203, w0=(285,'kJ/mol'), E0=(40.4176,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_N-9R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_N-9R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_N-9R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_N-9R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 162,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_4CClF->C",
    kinetics = ArrheniusBM(A=(2.90405e-05,'m^3/(mol*s)'), n=2.92564, w0=(285,'kJ/mol'), E0=(36.4179,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_4CClF->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_4CClF->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_4CClF->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_4CClF->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 163,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_N-4CClF->C",
    kinetics = ArrheniusBM(A=(0.00414474,'m^3/(mol*s)'), n=2.36454, w0=(285,'kJ/mol'), E0=(37.6683,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_N-4CClF->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_N-4CClF->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_N-4CClF->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_N-4CClF->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 164,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.00371455,'m^3/(mol*s)'), n=2.04407, w0=(285,'kJ/mol'), E0=(33.1151,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 165,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_4CClF->C",
    kinetics = ArrheniusBM(A=(2.97295e-05,'m^3/(mol*s)'), n=2.87869, w0=(285,'kJ/mol'), E0=(37.5627,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3178544011032928, var=23.446483983117474, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_4CClF->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_4CClF->C
    Total Standard Deviation in ln(k): 10.505871047733615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_4CClF->C
Total Standard Deviation in ln(k): 10.505871047733615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_4CClF->C
Total Standard Deviation in ln(k): 10.505871047733615
""",
)

entry(
    index = 166,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_4CClF->C_Ext-4C-R_7R!H->Cl",
    kinetics = ArrheniusBM(A=(6.12147e-07,'m^3/(mol*s)'), n=3.64776, w0=(285,'kJ/mol'), E0=(35.4361,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_4CClF->C_Ext-4C-R_7R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_4CClF->C_Ext-4C-R_7R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_4CClF->C_Ext-4C-R_7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_4CClF->C_Ext-4C-R_7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 167,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_4CClF->C_Ext-4C-R_N-7R!H->Cl",
    kinetics = ArrheniusBM(A=(2.44738e-05,'m^3/(mol*s)'), n=2.61697, w0=(285,'kJ/mol'), E0=(35.3134,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_4CClF->C_Ext-4C-R_N-7R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_4CClF->C_Ext-4C-R_N-7R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_4CClF->C_Ext-4C-R_N-7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_4CClF->C_Ext-4C-R_N-7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 168,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_N-4CClF->C",
    kinetics = ArrheniusBM(A=(0.000224002,'m^3/(mol*s)'), n=2.92557, w0=(285,'kJ/mol'), E0=(41.7299,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_N-4CClF->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_N-4CClF->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_N-4CClF->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_N-4CClF->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 169,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_4CClF->C",
    kinetics = ArrheniusBM(A=(1.06992e-06,'m^3/(mol*s)'), n=3.86337, w0=(285,'kJ/mol'), E0=(44.4749,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4566349583673352, var=0.5124058146789137, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_4CClF->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_4CClF->C
    Total Standard Deviation in ln(k): 2.582364040563395"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_4CClF->C
Total Standard Deviation in ln(k): 2.582364040563395""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_4CClF->C
Total Standard Deviation in ln(k): 2.582364040563395
""",
)

entry(
    index = 170,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_4CClF->C_5R!H->C",
    kinetics = ArrheniusBM(A=(1.4648e-07,'m^3/(mol*s)'), n=4.08332, w0=(285,'kJ/mol'), E0=(42.9847,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_4CClF->C_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_4CClF->C_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_4CClF->C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_4CClF->C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 171,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_4CClF->C_N-5R!H->C",
    kinetics = ArrheniusBM(A=(8.04004e-06,'m^3/(mol*s)'), n=3.63988, w0=(285,'kJ/mol'), E0=(45.9951,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_4CClF->C_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_4CClF->C_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_4CClF->C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_4CClF->C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 172,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_N-4CClF->C",
    kinetics = ArrheniusBM(A=(0.000118744,'m^3/(mol*s)'), n=3.31983, w0=(285,'kJ/mol'), E0=(43.8066,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3955531718061656, var=0.8661692112516568, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_N-4CClF->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_N-4CClF->C
    Total Standard Deviation in ln(k): 2.8596232853121446"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_N-4CClF->C
Total Standard Deviation in ln(k): 2.8596232853121446""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_N-4CClF->C
Total Standard Deviation in ln(k): 2.8596232853121446
""",
)

entry(
    index = 173,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_N-4CClF->C_4ClF->Cl",
    kinetics = ArrheniusBM(A=(9.90858e-06,'m^3/(mol*s)'), n=3.62496, w0=(285,'kJ/mol'), E0=(35.1941,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_N-4CClF->C_4ClF->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_N-4CClF->C_4ClF->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_N-4CClF->C_4ClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_N-4CClF->C_4ClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 174,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_N-4CClF->C_N-4ClF->Cl",
    kinetics = ArrheniusBM(A=(2.74246e-05,'m^3/(mol*s)'), n=3.50414, w0=(285,'kJ/mol'), E0=(45.1217,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.37816610777607695, var=0.0008358245930592769, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_N-4CClF->C_N-4ClF->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_N-4CClF->C_N-4ClF->Cl
    Total Standard Deviation in ln(k): 1.0081242563009198"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_N-4CClF->C_N-4ClF->Cl
Total Standard Deviation in ln(k): 1.0081242563009198""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_N-4CClF->C_N-4ClF->Cl
Total Standard Deviation in ln(k): 1.0081242563009198
""",
)

entry(
    index = 175,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_N-4CClF->C_N-4ClF->Cl_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.39721e-05,'m^3/(mol*s)'), n=3.56605, w0=(285,'kJ/mol'), E0=(43.1736,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_N-4CClF->C_N-4ClF->Cl_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_N-4CClF->C_N-4ClF->Cl_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_N-4CClF->C_N-4ClF->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_N-4CClF->C_N-4ClF->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 176,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClFO->Cl",
    kinetics = ArrheniusBM(A=(0.204931,'m^3/(mol*s)'), n=1.67313, w0=(285,'kJ/mol'), E0=(53.3169,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.02342475176696992, var=33.107608552258554, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClFO->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClFO->Cl
    Total Standard Deviation in ln(k): 11.593943713793967"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClFO->Cl
Total Standard Deviation in ln(k): 11.593943713793967""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClFO->Cl
Total Standard Deviation in ln(k): 11.593943713793967
""",
)

entry(
    index = 177,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClFO->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.00552521,'m^3/(mol*s)'), n=1.74736, w0=(285,'kJ/mol'), E0=(44.282,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClFO->Cl_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClFO->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClFO->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClFO->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 178,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl",
    kinetics = ArrheniusBM(A=(0.0352395,'m^3/(mol*s)'), n=2.17613, w0=(285,'kJ/mol'), E0=(45.0574,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07273416809833437, var=2.526421209233436, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl
    Total Standard Deviation in ln(k): 3.369219420376576"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl
Total Standard Deviation in ln(k): 3.369219420376576""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl
Total Standard Deviation in ln(k): 3.369219420376576
""",
)

entry(
    index = 179,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C",
    kinetics = ArrheniusBM(A=(0.000349834,'m^3/(mol*s)'), n=2.81042, w0=(285,'kJ/mol'), E0=(41.9539,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06268300425940322, var=1.1219372981818108, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C
    Total Standard Deviation in ln(k): 2.2809412852009485"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C
Total Standard Deviation in ln(k): 2.2809412852009485""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C
Total Standard Deviation in ln(k): 2.2809412852009485
""",
)

entry(
    index = 180,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.000613934,'m^3/(mol*s)'), n=2.72329, w0=(285,'kJ/mol'), E0=(39.9664,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.01678794480903829, var=1.7756854489619565, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R
    Total Standard Deviation in ln(k): 2.7135874440890833"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R
Total Standard Deviation in ln(k): 2.7135874440890833""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R
Total Standard Deviation in ln(k): 2.7135874440890833
""",
)

entry(
    index = 181,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.000567875,'m^3/(mol*s)'), n=2.68112, w0=(285,'kJ/mol'), E0=(38.3418,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04880724091117948, var=2.209719063547789, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 3.10269477489895"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 3.10269477489895""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 3.10269477489895
""",
)

entry(
    index = 182,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.0586022,'m^3/(mol*s)'), n=1.72086, w0=(285,'kJ/mol'), E0=(33.4548,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 183,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(6.42243e-05,'m^3/(mol*s)'), n=3.07851, w0=(285,'kJ/mol'), E0=(39.2241,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0032154503405871252, var=3.233295680005579, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 3.6128667865175603"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R_Ext-4C-R
Total Standard Deviation in ln(k): 3.6128667865175603""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R_Ext-4C-R
Total Standard Deviation in ln(k): 3.6128667865175603
""",
)

entry(
    index = 184,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R_Ext-4C-R_7R!H->Cl",
    kinetics = ArrheniusBM(A=(1.87452e-05,'m^3/(mol*s)'), n=3.32701, w0=(285,'kJ/mol'), E0=(38.0418,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R_Ext-4C-R_7R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R_Ext-4C-R_7R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R_Ext-4C-R_7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R_Ext-4C-R_7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 185,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R_Ext-4C-R_N-7R!H->Cl",
    kinetics = ArrheniusBM(A=(0.000212992,'m^3/(mol*s)'), n=2.83406, w0=(285,'kJ/mol'), E0=(40.3713,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R_Ext-4C-R_N-7R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R_Ext-4C-R_N-7R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R_Ext-4C-R_N-7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R_Ext-4C-R_N-7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 186,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(5.46688e-05,'m^3/(mol*s)'), n=3.05096, w0=(285,'kJ/mol'), E0=(45.9336,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 187,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C",
    kinetics = ArrheniusBM(A=(7.71982,'m^3/(mol*s)'), n=1.4351, w0=(285,'kJ/mol'), E0=(48.7282,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.21999314607321863, var=5.727502866005908, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C
    Total Standard Deviation in ln(k): 5.350519056045076"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C
Total Standard Deviation in ln(k): 5.350519056045076""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C
Total Standard Deviation in ln(k): 5.350519056045076
""",
)

entry(
    index = 188,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(12.9813,'m^3/(mol*s)'), n=1.38381, w0=(285,'kJ/mol'), E0=(48.6776,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.28707938547167533, var=7.6129632396800435, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R
    Total Standard Deviation in ln(k): 6.252689582844891"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R
Total Standard Deviation in ln(k): 6.252689582844891""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R
Total Standard Deviation in ln(k): 6.252689582844891
""",
)

entry(
    index = 189,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(8.70123,'m^3/(mol*s)'), n=1.53925, w0=(285,'kJ/mol'), E0=(49.0693,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.29866778652004544, var=6.794986111044045, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C
    Total Standard Deviation in ln(k): 5.976203423309462"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 5.976203423309462""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 5.976203423309462
""",
)

entry(
    index = 190,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_Sp-5C=1C",
    kinetics = ArrheniusBM(A=(0.00373505,'m^3/(mol*s)'), n=2.70426, w0=(285,'kJ/mol'), E0=(41.4482,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_Sp-5C=1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_Sp-5C=1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_Sp-5C=1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_Sp-5C=1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 191,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_N-Sp-5C=1C",
    kinetics = ArrheniusBM(A=(0.00944884,'m^3/(mol*s)'), n=2.32179, w0=(285,'kJ/mol'), E0=(41.3708,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.23757717925267988, var=10.605778574686477, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_N-Sp-5C=1C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_N-Sp-5C=1C
    Total Standard Deviation in ln(k): 7.125650954375748"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_N-Sp-5C=1C
Total Standard Deviation in ln(k): 7.125650954375748""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_N-Sp-5C=1C
Total Standard Deviation in ln(k): 7.125650954375748
""",
)

entry(
    index = 192,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_N-Sp-5C=1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.0191164,'m^3/(mol*s)'), n=2.12005, w0=(285,'kJ/mol'), E0=(39.1089,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.27397906341089767, var=32.71151533337036, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_N-Sp-5C=1C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_N-Sp-5C=1C_Ext-1C-R
    Total Standard Deviation in ln(k): 12.154267723133678"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_N-Sp-5C=1C_Ext-1C-R
Total Standard Deviation in ln(k): 12.154267723133678""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_N-Sp-5C=1C_Ext-1C-R
Total Standard Deviation in ln(k): 12.154267723133678
""",
)

entry(
    index = 193,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_N-Sp-5C=1C_Ext-1C-R_Ext-5C-R_7R!H->Cl",
    kinetics = ArrheniusBM(A=(0.000536535,'m^3/(mol*s)'), n=2.88999, w0=(285,'kJ/mol'), E0=(37.0669,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_N-Sp-5C=1C_Ext-1C-R_Ext-5C-R_7R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_N-Sp-5C=1C_Ext-1C-R_Ext-5C-R_7R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_N-Sp-5C=1C_Ext-1C-R_Ext-5C-R_7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_N-Sp-5C=1C_Ext-1C-R_Ext-5C-R_7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 194,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_N-Sp-5C=1C_Ext-1C-R_Ext-5C-R_N-7R!H->Cl",
    kinetics = ArrheniusBM(A=(0.00816439,'m^3/(mol*s)'), n=1.90059, w0=(285,'kJ/mol'), E0=(36.4057,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_N-Sp-5C=1C_Ext-1C-R_Ext-5C-R_N-7R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_N-Sp-5C=1C_Ext-1C-R_Ext-5C-R_N-7R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_N-Sp-5C=1C_Ext-1C-R_Ext-5C-R_N-7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_N-Sp-5C=1C_Ext-1C-R_Ext-5C-R_N-7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 195,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.0089246,'m^3/(mol*s)'), n=1.86732, w0=(285,'kJ/mol'), E0=(37.5254,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 196,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6.77285e+13,'m^3/(mol*s)'), n=-1.78439, w0=(285,'kJ/mol'), E0=(74.8399,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7804770843392129, var=5.921315615982575, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 6.839270629016249"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 6.839270629016249""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 6.839270629016249
""",
)

entry(
    index = 197,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(0.033938,'m^3/(mol*s)'), n=2.67089, w0=(285,'kJ/mol'), E0=(36.3693,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_4R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_4R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 198,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(4.7386e+14,'m^3/(mol*s)'), n=-2.03362, w0=(285,'kJ/mol'), E0=(77.0051,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8025620987049087, var=6.619989429781166, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 7.1745387507383205"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 7.1745387507383205""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 7.1745387507383205
""",
)

entry(
    index = 199,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.00215829,'m^3/(mol*s)'), n=2.92579, w0=(285,'kJ/mol'), E0=(40.1293,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.36690102366962635, var=1.3922593660243823, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 3.287329793323395"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 3.287329793323395""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 3.287329793323395
""",
)

entry(
    index = 200,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_Ext-1C-R_4BrCFO->Br",
    kinetics = ArrheniusBM(A=(0.00880775,'m^3/(mol*s)'), n=2.67281, w0=(285,'kJ/mol'), E0=(40.6255,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_Ext-1C-R_4BrCFO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_Ext-1C-R_4BrCFO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_Ext-1C-R_4BrCFO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_Ext-1C-R_4BrCFO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 201,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_Ext-1C-R_N-4BrCFO->Br",
    kinetics = ArrheniusBM(A=(0.0455873,'m^3/(mol*s)'), n=2.62423, w0=(285,'kJ/mol'), E0=(44.4152,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_Ext-1C-R_N-4BrCFO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_Ext-1C-R_N-4BrCFO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_Ext-1C-R_N-4BrCFO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_Ext-1C-R_N-4BrCFO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 202,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_4BrCFO->Br",
    kinetics = ArrheniusBM(A=(0.484658,'m^3/(mol*s)'), n=1.73772, w0=(285,'kJ/mol'), E0=(41.4287,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_4BrCFO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_4BrCFO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_4BrCFO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_4BrCFO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 203,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br",
    kinetics = ArrheniusBM(A=(1.80523e+16,'m^3/(mol*s)'), n=-2.40914, w0=(285,'kJ/mol'), E0=(78.9849,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8604649204861572, var=6.307127274132294, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br
    Total Standard Deviation in ln(k): 7.196662763390724"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br
Total Standard Deviation in ln(k): 7.196662763390724""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br
Total Standard Deviation in ln(k): 7.196662763390724
""",
)

entry(
    index = 204,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_Sp-4CCFFOO=1C",
    kinetics = ArrheniusBM(A=(0.0713601,'m^3/(mol*s)'), n=2.71607, w0=(285,'kJ/mol'), E0=(38.8018,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_Sp-4CCFFOO=1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_Sp-4CCFFOO=1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_Sp-4CCFFOO=1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_Sp-4CCFFOO=1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 205,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C",
    kinetics = ArrheniusBM(A=(6.87199e+17,'m^3/(mol*s)'), n=-2.88516, w0=(285,'kJ/mol'), E0=(82.3196,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9019201004542027, var=7.8270827057571655, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C
    Total Standard Deviation in ln(k): 7.874762974470703"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C
Total Standard Deviation in ln(k): 7.874762974470703""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C
Total Standard Deviation in ln(k): 7.874762974470703
""",
)

entry(
    index = 206,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_4CFO->O",
    kinetics = ArrheniusBM(A=(8.10742e+20,'m^3/(mol*s)'), n=-3.77304, w0=(285,'kJ/mol'), E0=(76.5451,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.2861909031179795, var=34.10055956035574, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_4CFO->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_4CFO->O
    Total Standard Deviation in ln(k): 17.45098593667848"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_4CFO->O
Total Standard Deviation in ln(k): 17.45098593667848""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_4CFO->O
Total Standard Deviation in ln(k): 17.45098593667848
""",
)

entry(
    index = 207,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O",
    kinetics = ArrheniusBM(A=(0.0152409,'m^3/(mol*s)'), n=2.75378, w0=(285,'kJ/mol'), E0=(46.8372,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.39483513040703044, var=0.14632690268041218, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O
    Total Standard Deviation in ln(k): 1.7589133533111987"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O
Total Standard Deviation in ln(k): 1.7589133533111987""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O
Total Standard Deviation in ln(k): 1.7589133533111987
""",
)

entry(
    index = 208,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O_4CF->C",
    kinetics = ArrheniusBM(A=(0.0112489,'m^3/(mol*s)'), n=2.77506, w0=(285,'kJ/mol'), E0=(46.2588,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4412448109051552, var=0.22116849323104967, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O_4CF->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O_4CF->C
    Total Standard Deviation in ln(k): 2.051453230945435"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O_4CF->C
Total Standard Deviation in ln(k): 2.051453230945435""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O_4CF->C
Total Standard Deviation in ln(k): 2.051453230945435
""",
)

entry(
    index = 209,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O_4CF->C_5R!H->C",
    kinetics = ArrheniusBM(A=(0.0105062,'m^3/(mol*s)'), n=2.7954, w0=(285,'kJ/mol'), E0=(45.119,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O_4CF->C_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O_4CF->C_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O_4CF->C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O_4CF->C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 210,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O_4CF->C_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.0117903,'m^3/(mol*s)'), n=2.75736, w0=(285,'kJ/mol'), E0=(47.3756,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O_4CF->C_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O_4CF->C_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O_4CF->C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O_4CF->C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 211,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O_N-4CF->C",
    kinetics = ArrheniusBM(A=(0.0270554,'m^3/(mol*s)'), n=2.71539, w0=(285,'kJ/mol'), E0=(47.9587,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O_N-4CF->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O_N-4CF->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O_N-4CF->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O_N-4CF->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 212,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(0.00556838,'m^3/(mol*s)'), n=2.8146, w0=(285,'kJ/mol'), E0=(49.8074,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_4R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_4R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 213,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(3249.78,'m^3/(mol*s)'), n=1.11861, w0=(285,'kJ/mol'), E0=(58.9168,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3962824453399733, var=5.396655372608918, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 5.6528249474900845"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 5.6528249474900845""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 5.6528249474900845
""",
)

entry(
    index = 214,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C",
    kinetics = ArrheniusBM(A=(224051,'m^3/(mol*s)'), n=0.457342, w0=(285,'kJ/mol'), E0=(59.3043,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4938143733724141, var=7.569175376096465, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C
    Total Standard Deviation in ln(k): 6.756193714201841"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C
Total Standard Deviation in ln(k): 6.756193714201841""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C
Total Standard Deviation in ln(k): 6.756193714201841
""",
)

entry(
    index = 215,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_1C-u0",
    kinetics = ArrheniusBM(A=(0.0395434,'m^3/(mol*s)'), n=2.22957, w0=(285,'kJ/mol'), E0=(46.5897,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2337312426871424, var=1.37691642063271, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_1C-u0',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_1C-u0
    Total Standard Deviation in ln(k): 2.93966230710976"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_1C-u0
Total Standard Deviation in ln(k): 2.93966230710976""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_1C-u0
Total Standard Deviation in ln(k): 2.93966230710976
""",
)

entry(
    index = 216,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_1C-u0_4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.0210091,'m^3/(mol*s)'), n=2.40951, w0=(285,'kJ/mol'), E0=(47.7277,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.26594978376560396, var=0.0002309660710468903, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_1C-u0_4BrCFINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_1C-u0_4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 0.6986826346238111"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_1C-u0_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 0.6986826346238111""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_1C-u0_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 0.6986826346238111
""",
)

entry(
    index = 217,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_1C-u0_4BrCFINOPSSi->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(0.0211921,'m^3/(mol*s)'), n=2.3961, w0=(285,'kJ/mol'), E0=(46.9597,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_1C-u0_4BrCFINOPSSi->C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_1C-u0_4BrCFINOPSSi->C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_1C-u0_4BrCFINOPSSi->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_1C-u0_4BrCFINOPSSi->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 218,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_1C-u0_N-4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.2494,'m^3/(mol*s)'), n=1.79792, w0=(285,'kJ/mol'), E0=(44.9287,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_1C-u0_N-4BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_1C-u0_N-4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_1C-u0_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_1C-u0_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 219,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_N-1C-u0",
    kinetics = ArrheniusBM(A=(0.0340168,'m^3/(mol*s)'), n=2.655, w0=(285,'kJ/mol'), E0=(35.2069,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.48952855871062717, var=1.2722365252845313, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_N-1C-u0',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_N-1C-u0
    Total Standard Deviation in ln(k): 3.4911813670168574"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_N-1C-u0
Total Standard Deviation in ln(k): 3.4911813670168574""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_N-1C-u0
Total Standard Deviation in ln(k): 3.4911813670168574
""",
)

entry(
    index = 220,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_N-1C-u0_4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.0291245,'m^3/(mol*s)'), n=2.69164, w0=(285,'kJ/mol'), E0=(32.9874,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_N-1C-u0_4BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_N-1C-u0_4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_N-1C-u0_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_N-1C-u0_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 221,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_N-1C-u0_N-4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.0169924,'m^3/(mol*s)'), n=2.72405, w0=(285,'kJ/mol'), E0=(36.3918,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_N-1C-u0_N-4BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_N-1C-u0_N-4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_N-1C-u0_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_N-1C-u0_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 222,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-1C",
    kinetics = ArrheniusBM(A=(1.37382e-05,'m^3/(mol*s)'), n=3.74204, w0=(285,'kJ/mol'), E0=(44.4255,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.027916317733348076, var=8.027715917489672, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-1C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-1C
    Total Standard Deviation in ln(k): 5.750202336350368"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-1C
Total Standard Deviation in ln(k): 5.750202336350368""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-1C
Total Standard Deviation in ln(k): 5.750202336350368
""",
)

entry(
    index = 223,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-1C_Ext-4BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(0.000978778,'m^3/(mol*s)'), n=3.14895, w0=(285,'kJ/mol'), E0=(52.9088,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11528347022699377, var=11.735046105920542, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-1C_Ext-4BrCFINOPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-1C_Ext-4BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 7.157168368499517"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-1C_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 7.157168368499517""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-1C_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 7.157168368499517
""",
)

entry(
    index = 224,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-1C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi",
    kinetics = ArrheniusBM(A=(0.0104139,'m^3/(mol*s)'), n=2.90017, w0=(285,'kJ/mol'), E0=(47.5449,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-1C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-1C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-1C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-1C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 225,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-1C_Ext-4BrCFINOPSSi-R_N-Sp-5R!H-4BrCFINOPSSi",
    kinetics = ArrheniusBM(A=(0.00684122,'m^3/(mol*s)'), n=2.86155, w0=(285,'kJ/mol'), E0=(63.0829,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-1C_Ext-4BrCFINOPSSi-R_N-Sp-5R!H-4BrCFINOPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-1C_Ext-4BrCFINOPSSi-R_N-Sp-5R!H-4BrCFINOPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-1C_Ext-4BrCFINOPSSi-R_N-Sp-5R!H-4BrCFINOPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-1C_Ext-4BrCFINOPSSi-R_N-Sp-5R!H-4BrCFINOPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 226,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C",
    kinetics = ArrheniusBM(A=(3.81151e+14,'m^3/(mol*s)'), n=-1.84158, w0=(246.218,'kJ/mol'), E0=(70.3204,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5597117925445113, var=12.336023647217177, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C
    Total Standard Deviation in ln(k): 8.447477082104752"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C
Total Standard Deviation in ln(k): 8.447477082104752""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C
Total Standard Deviation in ln(k): 8.447477082104752
""",
)

entry(
    index = 227,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0",
    kinetics = ArrheniusBM(A=(3.0034e+14,'m^3/(mol*s)'), n=-1.81032, w0=(247.011,'kJ/mol'), E0=(70.1742,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5561793243864988, var=12.379179603655746, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0
    Total Standard Deviation in ln(k): 8.45090707775242"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0
Total Standard Deviation in ln(k): 8.45090707775242""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0
Total Standard Deviation in ln(k): 8.45090707775242
""",
)

entry(
    index = 228,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.7211e+15,'m^3/(mol*s)'), n=-2.10967, w0=(246.619,'kJ/mol'), E0=(72.9321,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.640186694512548, var=16.79648916746522, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R
    Total Standard Deviation in ln(k): 9.824619309213999"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 9.824619309213999""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 9.824619309213999
""",
)

entry(
    index = 229,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(1.41491e+15,'m^3/(mol*s)'), n=-2.08491, w0=(246.003,'kJ/mol'), E0=(72.7611,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6377376716038478, var=16.999504965923755, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C
    Total Standard Deviation in ln(k): 9.867970085750475"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C
Total Standard Deviation in ln(k): 9.867970085750475""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C
Total Standard Deviation in ln(k): 9.867970085750475
""",
)

entry(
    index = 230,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->Cl",
    kinetics = ArrheniusBM(A=(2.66025e+11,'m^3/(mol*s)'), n=-1.00751, w0=(244.71,'kJ/mol'), E0=(76.428,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4963403205786405, var=7.063294072897563, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->Cl
    Total Standard Deviation in ln(k): 6.575042279141968"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->Cl
Total Standard Deviation in ln(k): 6.575042279141968""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->Cl
Total Standard Deviation in ln(k): 6.575042279141968
""",
)

entry(
    index = 231,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->Cl_3BrClO->Br",
    kinetics = ArrheniusBM(A=(8.1e+07,'m^3/(mol*s)'), n=4.57457e-08, w0=(237.5,'kJ/mol'), E0=(58.7611,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->Cl_3BrClO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->Cl_3BrClO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->Cl_3BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->Cl_3BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 232,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->Cl_N-3BrClO->Br",
    kinetics = ArrheniusBM(A=(8.1e+07,'m^3/(mol*s)'), n=5.42152e-08, w0=(251.92,'kJ/mol'), E0=(75.0929,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->Cl_N-3BrClO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->Cl_N-3BrClO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->Cl_N-3BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->Cl_N-3BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 233,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(9.91483e+10,'m^3/(mol*s)'), n=-0.91402, w0=(246.52,'kJ/mol'), E0=(30.9525,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.20811405009937375, var=1.255128763363552, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl
    Total Standard Deviation in ln(k): 2.768855037432941"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl
Total Standard Deviation in ln(k): 2.768855037432941""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl
Total Standard Deviation in ln(k): 2.768855037432941
""",
)

entry(
    index = 234,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_4BrCF->Br",
    kinetics = ArrheniusBM(A=(9.62687e+10,'m^3/(mol*s)'), n=-0.908295, w0=(237.5,'kJ/mol'), E0=(30.9845,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_4BrCF->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_4BrCF->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_4BrCF->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_4BrCF->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 235,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br",
    kinetics = ArrheniusBM(A=(5.1419e+14,'m^3/(mol*s)'), n=-2.0792, w0=(248.775,'kJ/mol'), E0=(39.75,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5696669876968484, var=5.8533859808280155, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br
    Total Standard Deviation in ln(k): 6.281534405169761"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br
Total Standard Deviation in ln(k): 6.281534405169761""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br
Total Standard Deviation in ln(k): 6.281534405169761
""",
)

entry(
    index = 236,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_Ext-1C-R",
    kinetics = ArrheniusBM(A=(5.02027e+10,'m^3/(mol*s)'), n=-1.02645, w0=(248.775,'kJ/mol'), E0=(32.7166,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4265254232671609, var=0.30398645772842897, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_Ext-1C-R
    Total Standard Deviation in ln(k): 2.1769819395142678"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_Ext-1C-R
Total Standard Deviation in ln(k): 2.1769819395142678""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_Ext-1C-R
Total Standard Deviation in ln(k): 2.1769819395142678
""",
)

entry(
    index = 237,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_Ext-1C-R_3BrClO->Br",
    kinetics = ArrheniusBM(A=(2.47962e+10,'m^3/(mol*s)'), n=-0.904814, w0=(237.5,'kJ/mol'), E0=(33.4782,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_Ext-1C-R_3BrClO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_Ext-1C-R_3BrClO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_Ext-1C-R_3BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_Ext-1C-R_3BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 238,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_Ext-1C-R_N-3BrClO->Br",
    kinetics = ArrheniusBM(A=(6.2848e+08,'m^3/(mol*s)'), n=-0.515236, w0=(260.05,'kJ/mol'), E0=(7.0959,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_Ext-1C-R_N-3BrClO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_Ext-1C-R_N-3BrClO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_Ext-1C-R_N-3BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_Ext-1C-R_N-3BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 239,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_3BrClO->Br",
    kinetics = ArrheniusBM(A=(6.40068e+10,'m^3/(mol*s)'), n=-0.723925, w0=(237.5,'kJ/mol'), E0=(25.6391,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_3BrClO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_3BrClO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_3BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_3BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 240,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_N-3BrClO->Br",
    kinetics = ArrheniusBM(A=(3.348e+16,'m^3/(mol*s)'), n=-2.64273, w0=(260.05,'kJ/mol'), E0=(-3.5843,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_N-3BrClO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_N-3BrClO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_N-3BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_N-3BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 241,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(4.25793e+18,'m^3/(mol*s)'), n=-3.19555, w0=(248.775,'kJ/mol'), E0=(64.3096,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.27803754491902527, var=17.869612490067993, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C
    Total Standard Deviation in ln(k): 9.173096021400873"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 9.173096021400873""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 9.173096021400873
""",
)

entry(
    index = 242,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_3BrClO->Br",
    kinetics = ArrheniusBM(A=(1.18385e+10,'m^3/(mol*s)'), n=-0.457979, w0=(237.5,'kJ/mol'), E0=(31.2272,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_3BrClO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_3BrClO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_3BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_3BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 243,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_N-3BrClO->Br",
    kinetics = ArrheniusBM(A=(2.59369e+13,'m^3/(mol*s)'), n=-1.98749, w0=(260.05,'kJ/mol'), E0=(21.1726,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_N-3BrClO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_N-3BrClO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_N-3BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_N-3BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 244,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_3BrClO->Br",
    kinetics = ArrheniusBM(A=(1.03104e+08,'m^3/(mol*s)'), n=-0.000954103, w0=(237.5,'kJ/mol'), E0=(23.7193,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_3BrClO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_3BrClO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_3BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_3BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 245,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_N-3BrClO->Br",
    kinetics = ArrheniusBM(A=(7.22697,'m^3/(mol*s)'), n=2.3407, w0=(260.05,'kJ/mol'), E0=(10.5535,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_N-3BrClO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_N-3BrClO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_N-3BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_N-3BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 246,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_N-1C-u0",
    kinetics = ArrheniusBM(A=(1.12562e+45,'m^3/(mol*s)'), n=-11.848, w0=(237.5,'kJ/mol'), E0=(6.54161,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_N-1C-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_N-1C-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_N-1C-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_N-1C-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 247,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1",
    kinetics = ArrheniusBM(A=(1.33201e+16,'m^3/(mol*s)'), n=-2.30486, w0=(272.525,'kJ/mol'), E0=(70.9958,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4716498872885413, var=10.36235049569795, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1
    Total Standard Deviation in ln(k): 7.638413466497605"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1
Total Standard Deviation in ln(k): 7.638413466497605""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1
Total Standard Deviation in ln(k): 7.638413466497605
""",
)

entry(
    index = 248,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_3BrCClO->C",
    kinetics = ArrheniusBM(A=(0.0121066,'m^3/(mol*s)'), n=3.06941, w0=(285,'kJ/mol'), E0=(8.17066,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.0380488558738787, var=16.529552910258243, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_3BrCClO->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_3BrCClO->C
    Total Standard Deviation in ln(k): 10.758724720294069"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_3BrCClO->C
Total Standard Deviation in ln(k): 10.758724720294069""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_3BrCClO->C
Total Standard Deviation in ln(k): 10.758724720294069
""",
)

entry(
    index = 249,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_3BrCClO->C_Ext-3C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(53.4567,'m^3/(mol*s)'), n=1.95515, w0=(285,'kJ/mol'), E0=(4.21632,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8885719586171996, var=36.892930172937085, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_3BrCClO->C_Ext-3C-R_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_3BrCClO->C_Ext-3C-R_4R!H->C
    Total Standard Deviation in ln(k): 14.409263644983783"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_3BrCClO->C_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 14.409263644983783""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_3BrCClO->C_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 14.409263644983783
""",
)

entry(
    index = 250,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(3.12241e+14,'m^3/(mol*s)'), n=-1.56279, w0=(285,'kJ/mol'), E0=(78.9979,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8719483630552657, var=99.25162554994235, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 22.163020305985853"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 22.163020305985853""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 22.163020305985853
""",
)

entry(
    index = 251,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C",
    kinetics = ArrheniusBM(A=(2.55902e+08,'m^3/(mol*s)'), n=-0.502127, w0=(260.05,'kJ/mol'), E0=(44.0553,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9820330314860344, var=11.385172333096587, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C
    Total Standard Deviation in ln(k): 9.231780939439208"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C
Total Standard Deviation in ln(k): 9.231780939439208""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C
Total Standard Deviation in ln(k): 9.231780939439208
""",
)

entry(
    index = 252,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.30815e+08,'m^3/(mol*s)'), n=-0.48954, w0=(260.05,'kJ/mol'), E0=(44.0003,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9227635461645857, var=11.591998430904013, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C_Ext-1C-R
    Total Standard Deviation in ln(k): 9.144027701151593"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C_Ext-1C-R
Total Standard Deviation in ln(k): 9.144027701151593""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C_Ext-1C-R
Total Standard Deviation in ln(k): 9.144027701151593
""",
)

entry(
    index = 253,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(344.157,'m^3/(mol*s)'), n=1.02974, w0=(260.05,'kJ/mol'), E0=(25.989,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=5.343167377397428, var=42.19961664089164, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 26.4480497096621"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 26.4480497096621""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 26.4480497096621
""",
)

entry(
    index = 254,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C_Ext-1C-R_Ext-1C-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(43.7346,'m^3/(mol*s)'), n=1.28523, w0=(260.05,'kJ/mol'), E0=(23.4176,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C_Ext-1C-R_Ext-1C-R_4R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C_Ext-1C-R_Ext-1C-R_4R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C_Ext-1C-R_Ext-1C-R_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C_Ext-1C-R_Ext-1C-R_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 255,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(1.62441e+09,'m^3/(mol*s)'), n=-0.646505, w0=(260.05,'kJ/mol'), E0=(15.3018,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 256,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(59.3516,'m^3/(mol*s)'), n=1.55074, w0=(236.855,'kJ/mol'), E0=(1.2761,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.08714169881633037, var=13.85528350124452, Tref=1000.0, N=28, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C',), comment="""BM rule fitted to 28 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 7.681111414013017"""),
    rank = 11,
    shortDesc = """BM rule fitted to 28 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 7.681111414013017""",
    longDesc = 
"""
BM rule fitted to 28 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 7.681111414013017
""",
)

entry(
    index = 257,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R",
    kinetics = ArrheniusBM(A=(5.23448e+09,'m^3/(mol*s)'), n=-1.1124, w0=(249.977,'kJ/mol'), E0=(62.9475,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0111818188144321, var=5.846210419351629, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R
    Total Standard Deviation in ln(k): 4.875331532802805"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R
Total Standard Deviation in ln(k): 4.875331532802805""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R
Total Standard Deviation in ln(k): 4.875331532802805
""",
)

entry(
    index = 258,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(1.28669e+06,'m^3/(mol*s)'), n=-0.0844531, w0=(249.823,'kJ/mol'), E0=(63.1861,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2510323365258838, var=3.418354804226335, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl
    Total Standard Deviation in ln(k): 4.337247775418355"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl
Total Standard Deviation in ln(k): 4.337247775418355""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl
Total Standard Deviation in ln(k): 4.337247775418355
""",
)

entry(
    index = 259,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl_1BrClO->Br",
    kinetics = ArrheniusBM(A=(1882.63,'m^3/(mol*s)'), n=0.917064, w0=(237.5,'kJ/mol'), E0=(55.9763,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl_1BrClO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl_1BrClO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl_1BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl_1BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 260,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl_N-1BrClO->Br",
    kinetics = ArrheniusBM(A=(0.16235,'m^3/(mol*s)'), n=1.79755, w0=(255.985,'kJ/mol'), E0=(44.882,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3656217827241419, var=0.5826532239546593, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl_N-1BrClO->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl_N-1BrClO->Br
    Total Standard Deviation in ln(k): 2.448896561288501"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl_N-1BrClO->Br
Total Standard Deviation in ln(k): 2.448896561288501""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl_N-1BrClO->Br
Total Standard Deviation in ln(k): 2.448896561288501
""",
)

entry(
    index = 261,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl_N-1BrClO->Br_1ClO->O",
    kinetics = ArrheniusBM(A=(0.0667867,'m^3/(mol*s)'), n=1.64401, w0=(260.05,'kJ/mol'), E0=(24.0373,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl_N-1BrClO->Br_1ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl_N-1BrClO->Br_1ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl_N-1BrClO->Br_1ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl_N-1BrClO->Br_1ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 262,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl_N-1BrClO->Br_N-1ClO->O",
    kinetics = ArrheniusBM(A=(247.456,'m^3/(mol*s)'), n=1.14962, w0=(251.92,'kJ/mol'), E0=(72.0616,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl_N-1BrClO->Br_N-1ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl_N-1BrClO->Br_N-1ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl_N-1BrClO->Br_N-1ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl_N-1BrClO->Br_N-1ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 263,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(76.5728,'m^3/(mol*s)'), n=1.14151, w0=(250.028,'kJ/mol'), E0=(4.47462,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.022715131247957144, var=12.4206240207046, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 7.1223421223897425"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 7.1223421223897425""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 7.1223421223897425
""",
)

entry(
    index = 264,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0",
    kinetics = ArrheniusBM(A=(99305.6,'m^3/(mol*s)'), n=0.306675, w0=(247.164,'kJ/mol'), E0=(18.2029,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.58603702819343, var=6.197247303779576, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0
    Total Standard Deviation in ln(k): 8.975659495835629"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0
Total Standard Deviation in ln(k): 8.975659495835629""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0
Total Standard Deviation in ln(k): 8.975659495835629
""",
)

entry(
    index = 265,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R",
    kinetics = ArrheniusBM(A=(498010,'m^3/(mol*s)'), n=0.103666, w0=(245.017,'kJ/mol'), E0=(25.0973,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.23220217998716491, var=0.10631107360748877, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R
    Total Standard Deviation in ln(k): 1.2370740315873336"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R
Total Standard Deviation in ln(k): 1.2370740315873336""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R
Total Standard Deviation in ln(k): 1.2370740315873336
""",
)

entry(
    index = 266,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R_4BrCFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(1.15e+06,'m^3/(mol*s)'), n=-5.53109e-08, w0=(237.5,'kJ/mol'), E0=(26.8401,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R_4BrCFINOPSSi->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R_4BrCFINOPSSi->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R_4BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R_4BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 267,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R_N-4BrCFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(243227,'m^3/(mol*s)'), n=0.146702, w0=(248.775,'kJ/mol'), E0=(19.5122,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.13003563456222947, var=0.6890225861009108, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R_N-4BrCFINOPSSi->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R_N-4BrCFINOPSSi->Br
    Total Standard Deviation in ln(k): 1.9908008513258892"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R_N-4BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 1.9908008513258892""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R_N-4BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 1.9908008513258892
""",
)

entry(
    index = 268,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R_N-4BrCFINOPSSi->Br_1BrClO->Br",
    kinetics = ArrheniusBM(A=(605000,'m^3/(mol*s)'), n=8.05121e-09, w0=(237.5,'kJ/mol'), E0=(27.6304,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R_N-4BrCFINOPSSi->Br_1BrClO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R_N-4BrCFINOPSSi->Br_1BrClO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R_N-4BrCFINOPSSi->Br_1BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R_N-4BrCFINOPSSi->Br_1BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 269,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R_N-4BrCFINOPSSi->Br_N-1BrClO->Br",
    kinetics = ArrheniusBM(A=(249985,'m^3/(mol*s)'), n=0.176609, w0=(260.05,'kJ/mol'), E0=(13.6696,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R_N-4BrCFINOPSSi->Br_N-1BrClO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R_N-4BrCFINOPSSi->Br_N-1BrClO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R_N-4BrCFINOPSSi->Br_N-1BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R_N-4BrCFINOPSSi->Br_N-1BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 270,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_1BrClO->Br",
    kinetics = ArrheniusBM(A=(4.18273e+08,'m^3/(mol*s)'), n=-0.468288, w0=(237.5,'kJ/mol'), E0=(32.1677,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1566065503372975, var=0.022123763318405463, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_1BrClO->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_1BrClO->Br
    Total Standard Deviation in ln(k): 0.6916692744031697"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_1BrClO->Br
Total Standard Deviation in ln(k): 0.6916692744031697""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_1BrClO->Br
Total Standard Deviation in ln(k): 0.6916692744031697
""",
)

entry(
    index = 271,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_1BrClO->Br_Sp-4BrCFINOPSSi-3BrBrCCClFINOOPSSi",
    kinetics = ArrheniusBM(A=(1.93937e+08,'m^3/(mol*s)'), n=-0.399054, w0=(237.5,'kJ/mol'), E0=(22.3546,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_1BrClO->Br_Sp-4BrCFINOPSSi-3BrBrCCClFINOOPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_1BrClO->Br_Sp-4BrCFINOPSSi-3BrBrCCClFINOOPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_1BrClO->Br_Sp-4BrCFINOPSSi-3BrBrCCClFINOOPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_1BrClO->Br_Sp-4BrCFINOPSSi-3BrBrCCClFINOOPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 272,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_1BrClO->Br_N-Sp-4BrCFINOPSSi-3BrBrCCClFINOOPSSi",
    kinetics = ArrheniusBM(A=(1.12393e+08,'m^3/(mol*s)'), n=-0.278364, w0=(237.5,'kJ/mol'), E0=(33.4898,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_1BrClO->Br_N-Sp-4BrCFINOPSSi-3BrBrCCClFINOOPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_1BrClO->Br_N-Sp-4BrCFINOPSSi-3BrBrCCClFINOOPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_1BrClO->Br_N-Sp-4BrCFINOPSSi-3BrBrCCClFINOOPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_1BrClO->Br_N-Sp-4BrCFINOPSSi-3BrBrCCClFINOOPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 273,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_N-1BrClO->Br",
    kinetics = ArrheniusBM(A=(7.53927e+12,'m^3/(mol*s)'), n=-1.97967, w0=(260.05,'kJ/mol'), E0=(5.2511,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.23329868308901133, var=12.147033397099303, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_N-1BrClO->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_N-1BrClO->Br
    Total Standard Deviation in ln(k): 7.573199458376113"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_N-1BrClO->Br
Total Standard Deviation in ln(k): 7.573199458376113""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_N-1BrClO->Br
Total Standard Deviation in ln(k): 7.573199458376113
""",
)

entry(
    index = 274,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_N-1BrClO->Br_Sp-4BrCFINOPSSi-3BrBrCCClFINOOPSSi",
    kinetics = ArrheniusBM(A=(1.53024e+14,'m^3/(mol*s)'), n=-2.23466, w0=(260.05,'kJ/mol'), E0=(2.6005,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_N-1BrClO->Br_Sp-4BrCFINOPSSi-3BrBrCCClFINOOPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_N-1BrClO->Br_Sp-4BrCFINOPSSi-3BrBrCCClFINOOPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_N-1BrClO->Br_Sp-4BrCFINOPSSi-3BrBrCCClFINOOPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_N-1BrClO->Br_Sp-4BrCFINOPSSi-3BrBrCCClFINOOPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 275,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_N-1BrClO->Br_N-Sp-4BrCFINOPSSi-3BrBrCCClFINOOPSSi",
    kinetics = ArrheniusBM(A=(3.71448e+11,'m^3/(mol*s)'), n=-1.72467, w0=(260.05,'kJ/mol'), E0=(13.3499,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_N-1BrClO->Br_N-Sp-4BrCFINOPSSi-3BrBrCCClFINOOPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_N-1BrClO->Br_N-Sp-4BrCFINOPSSi-3BrBrCCClFINOOPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_N-1BrClO->Br_N-Sp-4BrCFINOPSSi-3BrBrCCClFINOOPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_N-1BrClO->Br_N-Sp-4BrCFINOPSSi-3BrBrCCClFINOOPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 276,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_N-1BrClO-u0",
    kinetics = ArrheniusBM(A=(0.0492229,'m^3/(mol*s)'), n=1.99753, w0=(260.05,'kJ/mol'), E0=(12.3355,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.8806184498345653, var=6.9248612539565215, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_N-1BrClO-u0',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_N-1BrClO-u0
    Total Standard Deviation in ln(k): 10.000658624978575"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_N-1BrClO-u0
Total Standard Deviation in ln(k): 10.000658624978575""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_N-1BrClO-u0
Total Standard Deviation in ln(k): 10.000658624978575
""",
)

entry(
    index = 277,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_N-1BrClO-u0_Ext-3BrCClO-R",
    kinetics = ArrheniusBM(A=(1.79213e+06,'m^3/(mol*s)'), n=-0.253483, w0=(260.05,'kJ/mol'), E0=(10.3625,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_N-1BrClO-u0_Ext-3BrCClO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_N-1BrClO-u0_Ext-3BrCClO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_N-1BrClO-u0_Ext-3BrCClO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_N-1BrClO-u0_Ext-3BrCClO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 278,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0",
    kinetics = ArrheniusBM(A=(677207,'m^3/(mol*s)'), n=0.545506, w0=(224.796,'kJ/mol'), E0=(9.60204,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0860027509627596, var=3.4083400239492696, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0
    Total Standard Deviation in ln(k): 3.9171670928036404"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0
Total Standard Deviation in ln(k): 3.9171670928036404""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0
Total Standard Deviation in ln(k): 3.9171670928036404
""",
)

entry(
    index = 279,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br",
    kinetics = ArrheniusBM(A=(3355.72,'m^3/(mol*s)'), n=1.29508, w0=(220.904,'kJ/mol'), E0=(2.20904,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03569651346497102, var=12.475566987533986, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br
    Total Standard Deviation in ln(k): 7.170568121703802"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br
Total Standard Deviation in ln(k): 7.170568121703802""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br
Total Standard Deviation in ln(k): 7.170568121703802
""",
)

entry(
    index = 280,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_3BrCClO->O",
    kinetics = ArrheniusBM(A=(10.0753,'m^3/(mol*s)'), n=1.93706, w0=(212.55,'kJ/mol'), E0=(1.4522,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.344969477292565, var=0.35414155135832764, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_3BrCClO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_3BrCClO->O
    Total Standard Deviation in ln(k): 2.059771183926704"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_3BrCClO->O
Total Standard Deviation in ln(k): 2.059771183926704""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_3BrCClO->O
Total Standard Deviation in ln(k): 2.059771183926704
""",
)

entry(
    index = 281,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_3BrCClO->O_3O-u1",
    kinetics = ArrheniusBM(A=(88.3416,'m^3/(mol*s)'), n=1.63658, w0=(212.55,'kJ/mol'), E0=(2.35382,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_3BrCClO->O_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_3BrCClO->O_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_3BrCClO->O_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_3BrCClO->O_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 282,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_3BrCClO->O_N-3O-u1",
    kinetics = ArrheniusBM(A=(19965.9,'m^3/(mol*s)'), n=1.02274, w0=(212.55,'kJ/mol'), E0=(24.6631,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_3BrCClO->O_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_3BrCClO->O_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_3BrCClO->O_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_3BrCClO->O_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 283,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O",
    kinetics = ArrheniusBM(A=(3.31041e+08,'m^3/(mol*s)'), n=0.0241013, w0=(226.473,'kJ/mol'), E0=(2.26473,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.9411590342588882, var=6.162799249274468, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O
    Total Standard Deviation in ln(k): 7.341473194528425"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O
Total Standard Deviation in ln(k): 7.341473194528425""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O
Total Standard Deviation in ln(k): 7.341473194528425
""",
)

entry(
    index = 284,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O_3BrCCl-u1",
    kinetics = ArrheniusBM(A=(2.1769e+08,'m^3/(mol*s)'), n=0.0832384, w0=(220.96,'kJ/mol'), E0=(2.31866,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-5.500517280501082, var=48.912378764422165, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O_3BrCCl-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O_3BrCCl-u1
    Total Standard Deviation in ln(k): 27.8409881501905"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O_3BrCCl-u1
Total Standard Deviation in ln(k): 27.8409881501905""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O_3BrCCl-u1
Total Standard Deviation in ln(k): 27.8409881501905
""",
)

entry(
    index = 285,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O_3BrCCl-u1_3BrCCl->C",
    kinetics = ArrheniusBM(A=(2.78087e+07,'m^3/(mol*s)'), n=-0.189794, w0=(237.5,'kJ/mol'), E0=(23.7001,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O_3BrCCl-u1_3BrCCl->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O_3BrCCl-u1_3BrCCl->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O_3BrCCl-u1_3BrCCl->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O_3BrCCl-u1_3BrCCl->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 286,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O_3BrCCl-u1_N-3BrCCl->C",
    kinetics = ArrheniusBM(A=(2.81493e+09,'m^3/(mol*s)'), n=-0.232559, w0=(204.42,'kJ/mol'), E0=(11.3183,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O_3BrCCl-u1_N-3BrCCl->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O_3BrCCl-u1_N-3BrCCl->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O_3BrCCl-u1_N-3BrCCl->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O_3BrCCl-u1_N-3BrCCl->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 287,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O_N-3BrCCl-u1",
    kinetics = ArrheniusBM(A=(2.41219e+44,'m^3/(mol*s)'), n=-11.6259, w0=(237.5,'kJ/mol'), E0=(2.375,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O_N-3BrCCl-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O_N-3BrCCl-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O_N-3BrCCl-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O_N-3BrCCl-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 288,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br",
    kinetics = ArrheniusBM(A=(1.17038e+07,'m^3/(mol*s)'), n=0.152564, w0=(227.576,'kJ/mol'), E0=(11.2849,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.20803853506074263, var=3.326114430074154, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br
    Total Standard Deviation in ln(k): 4.178873167352673"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br
Total Standard Deviation in ln(k): 4.178873167352673""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br
Total Standard Deviation in ln(k): 4.178873167352673
""",
)

entry(
    index = 289,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1",
    kinetics = ArrheniusBM(A=(3.72289e+07,'m^3/(mol*s)'), n=-0.0251648, w0=(226.192,'kJ/mol'), E0=(11.492,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3214024148413374, var=5.236393739973473, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1
    Total Standard Deviation in ln(k): 5.395012696742996"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1
Total Standard Deviation in ln(k): 5.395012696742996""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1
Total Standard Deviation in ln(k): 5.395012696742996
""",
)

entry(
    index = 290,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_3BrCClO->O",
    kinetics = ArrheniusBM(A=(2.18739e+08,'m^3/(mol*s)'), n=-0.68298, w0=(226.97,'kJ/mol'), E0=(-8.25945,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_3BrCClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_3BrCClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_3BrCClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_3BrCClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 291,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O",
    kinetics = ArrheniusBM(A=(609769,'m^3/(mol*s)'), n=0.595881, w0=(225.998,'kJ/mol'), E0=(8.65768,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3767214803692408, var=6.01359307153392, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O
    Total Standard Deviation in ln(k): 5.862673731518171"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O
Total Standard Deviation in ln(k): 5.862673731518171""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O
Total Standard Deviation in ln(k): 5.862673731518171
""",
)

entry(
    index = 292,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O",
    kinetics = ArrheniusBM(A=(84518,'m^3/(mol*s)'), n=0.774569, w0=(233.19,'kJ/mol'), E0=(8.19603,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2936072625424158, var=0.5333824925416483, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O
    Total Standard Deviation in ln(k): 2.2018256599179655"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O
Total Standard Deviation in ln(k): 2.2018256599179655""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O
Total Standard Deviation in ln(k): 2.2018256599179655
""",
)

entry(
    index = 293,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O_3BrCCl->Br",
    kinetics = ArrheniusBM(A=(133.262,'m^3/(mol*s)'), n=1.71978, w0=(212.55,'kJ/mol'), E0=(-2.77863,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O_3BrCCl->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O_3BrCCl->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O_3BrCCl->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O_3BrCCl->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 294,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O_N-3BrCCl->Br",
    kinetics = ArrheniusBM(A=(1.81444e+06,'m^3/(mol*s)'), n=0.321827, w0=(243.51,'kJ/mol'), E0=(9.69703,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7615087915196876, var=0.011739853077446044, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O_N-3BrCCl->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O_N-3BrCCl->Br
    Total Standard Deviation in ln(k): 2.130552925790406"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O_N-3BrCCl->Br
Total Standard Deviation in ln(k): 2.130552925790406""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O_N-3BrCCl->Br
Total Standard Deviation in ln(k): 2.130552925790406
""",
)

entry(
    index = 295,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O_N-3BrCCl->Br_3CCl->C",
    kinetics = ArrheniusBM(A=(2.94036,'m^3/(mol*s)'), n=2.23507, w0=(260.05,'kJ/mol'), E0=(16.2271,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O_N-3BrCCl->Br_3CCl->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O_N-3BrCCl->Br_3CCl->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O_N-3BrCCl->Br_3CCl->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O_N-3BrCCl->Br_3CCl->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 296,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O_N-3BrCCl->Br_N-3CCl->C",
    kinetics = ArrheniusBM(A=(2.01522e+07,'m^3/(mol*s)'), n=-0.231972, w0=(226.97,'kJ/mol'), E0=(-4.69625,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O_N-3BrCCl->Br_N-3CCl->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O_N-3BrCCl->Br_N-3CCl->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O_N-3BrCCl->Br_N-3CCl->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O_N-3BrCCl->Br_N-3CCl->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 297,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_N-1ClO->O",
    kinetics = ArrheniusBM(A=(3.7e+08,'m^3/(mol*s)'), n=1.5752e-07, w0=(204.42,'kJ/mol'), E0=(10.6728,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_N-1ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_N-1ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_N-1ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_N-1ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 298,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_N-3BrCClO-u1",
    kinetics = ArrheniusBM(A=(1.55045e+08,'m^3/(mol*s)'), n=-0.0846249, w0=(231.035,'kJ/mol'), E0=(17.2001,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.009826493203659071, var=2.947461971396475, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_N-3BrCClO-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_N-3BrCClO-u1
    Total Standard Deviation in ln(k): 3.466453736767797"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_N-3BrCClO-u1
Total Standard Deviation in ln(k): 3.466453736767797""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_N-3BrCClO-u1
Total Standard Deviation in ln(k): 3.466453736767797
""",
)

entry(
    index = 299,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_N-3BrCClO-u1_1ClO->O",
    kinetics = ArrheniusBM(A=(7.2e+07,'m^3/(mol*s)'), n=-2.74108e-08, w0=(235.1,'kJ/mol'), E0=(10.4768,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_N-3BrCClO-u1_1ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_N-3BrCClO-u1_1ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_N-3BrCClO-u1_1ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_N-3BrCClO-u1_1ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 300,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_N-3BrCClO-u1_N-1ClO->O",
    kinetics = ArrheniusBM(A=(22611.5,'m^3/(mol*s)'), n=1.0253, w0=(226.97,'kJ/mol'), E0=(12.7573,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_N-3BrCClO-u1_N-1ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_N-3BrCClO-u1_N-1ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_N-3BrCClO-u1_N-1ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_N-3BrCClO-u1_N-1ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 301,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0",
    kinetics = ArrheniusBM(A=(2439.08,'m^3/(mol*s)'), n=1.21253, w0=(233.668,'kJ/mol'), E0=(2.38918,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04973758122968413, var=0.8451732775787261, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0
    Total Standard Deviation in ln(k): 1.967988032833394"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0
Total Standard Deviation in ln(k): 1.967988032833394""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0
Total Standard Deviation in ln(k): 1.967988032833394
""",
)

entry(
    index = 302,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_3BrCClO->Br",
    kinetics = ArrheniusBM(A=(1.31182e+06,'m^3/(mol*s)'), n=0.464452, w0=(212.55,'kJ/mol'), E0=(27.9816,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_3BrCClO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_3BrCClO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_3BrCClO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_3BrCClO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 303,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br",
    kinetics = ArrheniusBM(A=(572691,'m^3/(mol*s)'), n=0.516193, w0=(240.707,'kJ/mol'), E0=(8.10252,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.033259621294171295, var=0.0435933174427777, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br
    Total Standard Deviation in ln(k): 0.5021357805730207"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br
Total Standard Deviation in ln(k): 0.5021357805730207""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br
Total Standard Deviation in ln(k): 0.5021357805730207
""",
)

entry(
    index = 304,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br_3CClO->Cl",
    kinetics = ArrheniusBM(A=(1.13026e+07,'m^3/(mol*s)'), n=0.234452, w0=(226.97,'kJ/mol'), E0=(16.3172,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br_3CClO->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br_3CClO->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br_3CClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br_3CClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 305,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br_N-3CClO->Cl",
    kinetics = ArrheniusBM(A=(1.4471e+07,'m^3/(mol*s)'), n=0.0254194, w0=(247.575,'kJ/mol'), E0=(6.51295,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.2094973024729323, var=12.338711457678789, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br_N-3CClO->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br_N-3CClO->Cl
    Total Standard Deviation in ln(k): 12.593433839132429"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br_N-3CClO->Cl
Total Standard Deviation in ln(k): 12.593433839132429""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br_N-3CClO->Cl
Total Standard Deviation in ln(k): 12.593433839132429
""",
)

entry(
    index = 306,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br_N-3CClO->Cl_3CO->C",
    kinetics = ArrheniusBM(A=(8.30513e+10,'m^3/(mol*s)'), n=-1.51237, w0=(260.05,'kJ/mol'), E0=(8.61773,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br_N-3CClO->Cl_3CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br_N-3CClO->Cl_3CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br_N-3CClO->Cl_3CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br_N-3CClO->Cl_3CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 307,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br_N-3CClO->Cl_N-3CO->C",
    kinetics = ArrheniusBM(A=(1.61447e+09,'m^3/(mol*s)'), n=-0.558876, w0=(235.1,'kJ/mol'), E0=(13.0785,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br_N-3CClO->Cl_N-3CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br_N-3CClO->Cl_N-3CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br_N-3CClO->Cl_N-3CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br_N-3CClO->Cl_N-3CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

