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
    kinetics = ArrheniusBM(A=(2.65741e+15,'m^3/(mol*s)'), n=-2.45584, w0=(326786,'J/mol'), E0=(95611.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.28109324601314284, var=9.043598304113113, Tref=1000.0, N=154, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 154 training reactions at node Root
    Total Standard Deviation in ln(k): 6.735019245150295"""),
    rank = 11,
    shortDesc = """BM rule fitted to 154 training reactions at node Root
Total Standard Deviation in ln(k): 6.735019245150295""",
    longDesc = 
"""
BM rule fitted to 154 training reactions at node Root
Total Standard Deviation in ln(k): 6.735019245150295
""",
)

entry(
    index = 2,
    label = "Root_1R->H",
    kinetics = ArrheniusBM(A=(83.3665,'m^3/(mol*s)'), n=1.45277, w0=(373750,'J/mol'), E0=(79351.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.029093597245392424, var=9.006140169316618, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_1R->H',), comment="""BM rule fitted to 22 training reactions at node Root_1R->H
    Total Standard Deviation in ln(k): 6.089355941753616"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_1R->H
Total Standard Deviation in ln(k): 6.089355941753616""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_1R->H
Total Standard Deviation in ln(k): 6.089355941753616
""",
)

entry(
    index = 3,
    label = "Root_N-1R->H",
    kinetics = ArrheniusBM(A=(1.89678e+20,'m^3/(mol*s)'), n=-3.8756, w0=(318958,'J/mol'), E0=(103866,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.3562994941915823, var=8.243655543023623, Tref=1000.0, N=132, data_mean=0.0, correlation='Root_N-1R->H',), comment="""BM rule fitted to 132 training reactions at node Root_N-1R->H
    Total Standard Deviation in ln(k): 6.651173468893096"""),
    rank = 11,
    shortDesc = """BM rule fitted to 132 training reactions at node Root_N-1R->H
Total Standard Deviation in ln(k): 6.651173468893096""",
    longDesc = 
"""
BM rule fitted to 132 training reactions at node Root_N-1R->H
Total Standard Deviation in ln(k): 6.651173468893096
""",
)

entry(
    index = 4,
    label = "Root_1R->H_3R-u1",
    kinetics = ArrheniusBM(A=(3.25822e+14,'m^3/(mol*s)'), n=-2.3296, w0=(372344,'J/mol'), E0=(114127,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2725870816211051, var=6.43231030327816, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_1R->H_3R-u1',), comment="""BM rule fitted to 16 training reactions at node Root_1R->H_3R-u1
    Total Standard Deviation in ln(k): 5.769301214128376"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_1R->H_3R-u1
Total Standard Deviation in ln(k): 5.769301214128376""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_1R->H_3R-u1
Total Standard Deviation in ln(k): 5.769301214128376
""",
)

entry(
    index = 5,
    label = "Root_1R->H_N-3R-u1",
    kinetics = ArrheniusBM(A=(1.47807e-25,'m^3/(mol*s)'), n=9.53025, w0=(377500,'J/mol'), E0=(3943.55,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5471123095574091, var=1.7745713191932222, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R->H_N-3R-u1',), comment="""BM rule fitted to 6 training reactions at node Root_1R->H_N-3R-u1
    Total Standard Deviation in ln(k): 4.0452225218942335"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R->H_N-3R-u1
Total Standard Deviation in ln(k): 4.0452225218942335""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R->H_N-3R-u1
Total Standard Deviation in ln(k): 4.0452225218942335
""",
)

entry(
    index = 6,
    label = "Root_N-1R->H_3R->H",
    kinetics = ArrheniusBM(A=(315689,'m^3/(mol*s)'), n=0.723337, w0=(373750,'J/mol'), E0=(74589.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.05562077425743411, var=2.404490537602155, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_N-1R->H_3R->H',), comment="""BM rule fitted to 22 training reactions at node Root_N-1R->H_3R->H
    Total Standard Deviation in ln(k): 3.2483770507712832"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_N-1R->H_3R->H
Total Standard Deviation in ln(k): 3.2483770507712832""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_N-1R->H_3R->H
Total Standard Deviation in ln(k): 3.2483770507712832
""",
)

entry(
    index = 7,
    label = "Root_N-1R->H_N-3R->H",
    kinetics = ArrheniusBM(A=(7.30226e+22,'m^3/(mol*s)'), n=-4.68409, w0=(308000,'J/mol'), E0=(108613,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.4073596499133973, var=9.122641896623412, Tref=1000.0, N=110, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H',), comment="""BM rule fitted to 110 training reactions at node Root_N-1R->H_N-3R->H
    Total Standard Deviation in ln(k): 7.078560703750894"""),
    rank = 11,
    shortDesc = """BM rule fitted to 110 training reactions at node Root_N-1R->H_N-3R->H
Total Standard Deviation in ln(k): 7.078560703750894""",
    longDesc = 
"""
BM rule fitted to 110 training reactions at node Root_N-1R->H_N-3R->H
Total Standard Deviation in ln(k): 7.078560703750894
""",
)

entry(
    index = 8,
    label = "Root_1R->H_3R-u1_3R->C",
    kinetics = ArrheniusBM(A=(5.79265e-22,'m^3/(mol*s)'), n=8.19898, w0=(377500,'J/mol'), E0=(-2366.39,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3631089561501029, var=2.198989968047082, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_1R->H_3R-u1_3R->C',), comment="""BM rule fitted to 13 training reactions at node Root_1R->H_3R-u1_3R->C
    Total Standard Deviation in ln(k): 3.8851540563057645"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_1R->H_3R-u1_3R->C
Total Standard Deviation in ln(k): 3.8851540563057645""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_1R->H_3R-u1_3R->C
Total Standard Deviation in ln(k): 3.8851540563057645
""",
)

entry(
    index = 9,
    label = "Root_1R->H_3R-u1_N-3R->C",
    kinetics = ArrheniusBM(A=(0.00190031,'m^3/(mol*s)'), n=3.26351, w0=(350000,'J/mol'), E0=(35000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.058463059047530685, var=5.26054461750628, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_3R-u1_N-3R->C',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_3R-u1_N-3R->C
    Total Standard Deviation in ln(k): 4.744927858354638"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_3R-u1_N-3R->C
Total Standard Deviation in ln(k): 4.744927858354638""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_3R-u1_N-3R->C
Total Standard Deviation in ln(k): 4.744927858354638
""",
)

entry(
    index = 10,
    label = "Root_1R->H_N-3R-u1_Ext-3R-R_4R!H->O",
    kinetics = ArrheniusBM(A=(3.63699e-30,'m^3/(mol*s)'), n=10.9398, w0=(377500,'J/mol'), E0=(-11861.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.36190254290372315, var=8.16348795802265, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->H_N-3R-u1_Ext-3R-R_4R!H->O',), comment="""BM rule fitted to 4 training reactions at node Root_1R->H_N-3R-u1_Ext-3R-R_4R!H->O
    Total Standard Deviation in ln(k): 6.637195490588173"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->H_N-3R-u1_Ext-3R-R_4R!H->O
Total Standard Deviation in ln(k): 6.637195490588173""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->H_N-3R-u1_Ext-3R-R_4R!H->O
Total Standard Deviation in ln(k): 6.637195490588173
""",
)

entry(
    index = 11,
    label = "Root_1R->H_N-3R-u1_Ext-3R-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(1.30994e-07,'m^3/(mol*s)'), n=4.17809, w0=(377500,'J/mol'), E0=(58720.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0035184369712136666, var=2.380872797957782, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-3R-u1_Ext-3R-R_N-4R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-3R-u1_Ext-3R-R_N-4R!H->O
    Total Standard Deviation in ln(k): 3.102161977967195"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-3R-u1_Ext-3R-R_N-4R!H->O
Total Standard Deviation in ln(k): 3.102161977967195""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-3R-u1_Ext-3R-R_N-4R!H->O
Total Standard Deviation in ln(k): 3.102161977967195
""",
)

entry(
    index = 12,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.98511e-14,'m^3/(mol*s)'), n=6.39506, w0=(377500,'J/mol'), E0=(25980.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.26770150038479584, var=1.1144765834301678, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C',), comment="""BM rule fitted to 19 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 2.78899105839292"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 2.78899105839292""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 2.78899105839292
""",
)

entry(
    index = 13,
    label = "Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(19.0182,'m^3/(mol*s)'), n=2.24528, w0=(350000,'J/mol'), E0=(35000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.016482801989141843, var=2.365341270285335, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 3.124629671163786"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 3.124629671163786""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 3.124629671163786
""",
)

entry(
    index = 14,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(5.99629e+25,'m^3/(mol*s)'), n=-5.50734, w0=(317833,'J/mol'), E0=(118508,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.4536723908152644, var=9.6877624767563, Tref=1000.0, N=72, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C',), comment="""BM rule fitted to 72 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 7.37965251710853"""),
    rank = 11,
    shortDesc = """BM rule fitted to 72 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 7.37965251710853""",
    longDesc = 
"""
BM rule fitted to 72 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 7.37965251710853
""",
)

entry(
    index = 15,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.76588e+15,'m^3/(mol*s)'), n=-2.50585, w0=(289368,'J/mol'), E0=(83692,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.278929956062825, var=8.628684346753655, Tref=1000.0, N=38, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C',), comment="""BM rule fitted to 38 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 6.5896626043140145"""),
    rank = 11,
    shortDesc = """BM rule fitted to 38 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 6.5896626043140145""",
    longDesc = 
"""
BM rule fitted to 38 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 6.5896626043140145
""",
)

entry(
    index = 16,
    label = "Root_1R->H_3R-u1_3R->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(6.97329e-22,'m^3/(mol*s)'), n=8.16652, w0=(377500,'J/mol'), E0=(-933.268,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4077316637328646, var=2.6284064604640847, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_1R->H_3R-u1_3R->C_Ext-3C-R',), comment="""BM rule fitted to 12 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R
    Total Standard Deviation in ln(k): 4.274600275359183"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R
Total Standard Deviation in ln(k): 4.274600275359183""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R
Total Standard Deviation in ln(k): 4.274600275359183
""",
)

entry(
    index = 17,
    label = "Root_1R->H_3R-u1_N-3R->C_Ext-3O-R",
    kinetics = ArrheniusBM(A=(1.79393e-05,'m^3/(mol*s)'), n=3.82684, w0=(350000,'J/mol'), E0=(35000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.6260903035374364, var=8.435215208207387, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_3R-u1_N-3R->C_Ext-3O-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_3R-u1_N-3R->C_Ext-3O-R
    Total Standard Deviation in ln(k): 7.395531901247499"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_3R-u1_N-3R->C_Ext-3O-R
Total Standard Deviation in ln(k): 7.395531901247499""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_3R-u1_N-3R->C_Ext-3O-R
Total Standard Deviation in ln(k): 7.395531901247499
""",
)

entry(
    index = 18,
    label = "Root_1R->H_N-3R-u1_Ext-3R-R_4R!H->O_Ext-3R-R",
    kinetics = ArrheniusBM(A=(2.32765e-06,'m^3/(mol*s)'), n=3.86898, w0=(377500,'J/mol'), E0=(40255.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.018957639868513183, var=1.6614345713211045, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-3R-u1_Ext-3R-R_4R!H->O_Ext-3R-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-3R-u1_Ext-3R-R_4R!H->O_Ext-3R-R
    Total Standard Deviation in ln(k): 2.6316685651640563"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-3R-u1_Ext-3R-R_4R!H->O_Ext-3R-R
Total Standard Deviation in ln(k): 2.6316685651640563""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-3R-u1_Ext-3R-R_4R!H->O_Ext-3R-R
Total Standard Deviation in ln(k): 2.6316685651640563
""",
)

entry(
    index = 19,
    label = "Root_1R->H_N-3R-u1_Ext-3R-R_N-4R!H->O_Ext-3R-R",
    kinetics = ArrheniusBM(A=(4.86578e-05,'m^3/(mol*s)'), n=3.19556, w0=(377500,'J/mol'), E0=(55385.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R-u1_Ext-3R-R_N-4R!H->O_Ext-3R-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R-u1_Ext-3R-R_N-4R!H->O_Ext-3R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R-u1_Ext-3R-R_N-4R!H->O_Ext-3R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R-u1_Ext-3R-R_N-4R!H->O_Ext-3R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0",
    kinetics = ArrheniusBM(A=(2.68557e-12,'m^3/(mol*s)'), n=5.77832, w0=(377500,'J/mol'), E0=(38153.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.22663942145435448, var=0.5727403976978488, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0
    Total Standard Deviation in ln(k): 2.086621551080127"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0
Total Standard Deviation in ln(k): 2.086621551080127""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0
Total Standard Deviation in ln(k): 2.086621551080127
""",
)

entry(
    index = 21,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0",
    kinetics = ArrheniusBM(A=(1.25541e-20,'m^3/(mol*s)'), n=8.18193, w0=(377500,'J/mol'), E0=(-1835.93,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3265980070967604, var=0.9389546188488358, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0
    Total Standard Deviation in ln(k): 2.763179696878245"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0
Total Standard Deviation in ln(k): 2.763179696878245""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0
Total Standard Deviation in ln(k): 2.763179696878245
""",
)

entry(
    index = 22,
    label = "Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_Ext-1O-R",
    kinetics = ArrheniusBM(A=(1.34127,'m^3/(mol*s)'), n=2.54457, w0=(350000,'J/mol'), E0=(35000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.7022123593656946, var=1.0174030857893832, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_Ext-1O-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_Ext-1O-R
    Total Standard Deviation in ln(k): 3.786456784590486"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_Ext-1O-R
Total Standard Deviation in ln(k): 3.786456784590486""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_Ext-1O-R
Total Standard Deviation in ln(k): 3.786456784590486
""",
)

entry(
    index = 23,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(5.22271e+28,'m^3/(mol*s)'), n=-6.36289, w0=(314167,'J/mol'), E0=(118714,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.4884097485873478, var=8.039235882375902, Tref=1000.0, N=45, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R',), comment="""BM rule fitted to 45 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R
    Total Standard Deviation in ln(k): 6.911295057538507"""),
    rank = 11,
    shortDesc = """BM rule fitted to 45 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 6.911295057538507""",
    longDesc = 
"""
BM rule fitted to 45 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 6.911295057538507
""",
)

entry(
    index = 24,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1",
    kinetics = ArrheniusBM(A=(1.12874e+10,'m^3/(mol*s)'), n=-1.02118, w0=(325553,'J/mol'), E0=(99613.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.18582759822437914, var=6.846413589092204, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1',), comment="""BM rule fitted to 19 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1
    Total Standard Deviation in ln(k): 5.712423606728955"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1
Total Standard Deviation in ln(k): 5.712423606728955""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1
Total Standard Deviation in ln(k): 5.712423606728955
""",
)

entry(
    index = 25,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1",
    kinetics = ArrheniusBM(A=(7.52053e+12,'m^3/(mol*s)'), n=-1.38968, w0=(320125,'J/mol'), E0=(91328.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2802905564014563, var=5.012068561439415, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1
    Total Standard Deviation in ln(k): 5.192378281359559"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1
Total Standard Deviation in ln(k): 5.192378281359559""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1
Total Standard Deviation in ln(k): 5.192378281359559
""",
)

entry(
    index = 26,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1",
    kinetics = ArrheniusBM(A=(2.52904e+07,'m^3/(mol*s)'), n=-0.25008, w0=(290017,'J/mol'), E0=(69205.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.15779355707274736, var=6.485249654133873, Tref=1000.0, N=29, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1',), comment="""BM rule fitted to 29 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1
    Total Standard Deviation in ln(k): 5.50175531044186"""),
    rank = 11,
    shortDesc = """BM rule fitted to 29 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1
Total Standard Deviation in ln(k): 5.50175531044186""",
    longDesc = 
"""
BM rule fitted to 29 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1
Total Standard Deviation in ln(k): 5.50175531044186
""",
)

entry(
    index = 27,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1",
    kinetics = ArrheniusBM(A=(4.07288e+11,'m^3/(mol*s)'), n=-1.23691, w0=(287278,'J/mol'), E0=(59920.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1450378470060968, var=9.963617342125128, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1
    Total Standard Deviation in ln(k): 6.69240269652537"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1
Total Standard Deviation in ln(k): 6.69240269652537""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1
Total Standard Deviation in ln(k): 6.69240269652537
""",
)

entry(
    index = 28,
    label = "Root_1R->H_3R-u1_3R->C_Ext-3C-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(2.81263e-07,'m^3/(mol*s)'), n=3.71574, w0=(377500,'J/mol'), E0=(68403,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.025415814550923965, var=4.648883053789327, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R->H_3R-u1_3R->C_Ext-3C-R_4R!H->Cl',), comment="""BM rule fitted to 6 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_4R!H->Cl
    Total Standard Deviation in ln(k): 4.386321986161544"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_4R!H->Cl
Total Standard Deviation in ln(k): 4.386321986161544""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_4R!H->Cl
Total Standard Deviation in ln(k): 4.386321986161544
""",
)

entry(
    index = 29,
    label = "Root_1R->H_3R-u1_3R->C_Ext-3C-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(9.71148e-23,'m^3/(mol*s)'), n=8.49537, w0=(377500,'J/mol'), E0=(7203.66,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5198645205474097, var=1.7798951057777932, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R->H_3R-u1_3R->C_Ext-3C-R_N-4R!H->Cl',), comment="""BM rule fitted to 6 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 3.9807636478540798"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 3.9807636478540798""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 3.9807636478540798
""",
)

entry(
    index = 30,
    label = "Root_1R->H_3R-u1_N-3R->C_Ext-3O-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(0.00118512,'m^3/(mol*s)'), n=2.96558, w0=(350000,'J/mol'), E0=(35000,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R-u1_N-3R->C_Ext-3O-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_N-3R->C_Ext-3O-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_N-3R->C_Ext-3O-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_N-3R->C_Ext-3O-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "Root_1R->H_N-3R-u1_Ext-3R-R_4R!H->O_Ext-3R-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(3.42232e-09,'m^3/(mol*s)'), n=4.59791, w0=(377500,'J/mol'), E0=(35016.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R-u1_Ext-3R-R_4R!H->O_Ext-3R-R_5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R-u1_Ext-3R-R_4R!H->O_Ext-3R-R_5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R-u1_Ext-3R-R_4R!H->O_Ext-3R-R_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R-u1_Ext-3R-R_4R!H->O_Ext-3R-R_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 32,
    label = "Root_1R->H_N-3R-u1_Ext-3R-R_4R!H->O_Ext-3R-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(4.82904e-06,'m^3/(mol*s)'), n=3.79009, w0=(377500,'J/mol'), E0=(38409.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.003405159466130133, var=1.7807820673485593, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-3R-u1_Ext-3R-R_4R!H->O_Ext-3R-R_N-5R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-3R-u1_Ext-3R-R_4R!H->O_Ext-3R-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 2.6837933786161745"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-3R-u1_Ext-3R-R_4R!H->O_Ext-3R-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 2.6837933786161745""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-3R-u1_Ext-3R-R_4R!H->O_Ext-3R-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 2.6837933786161745
""",
)

entry(
    index = 33,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.63282e-13,'m^3/(mol*s)'), n=6.03682, w0=(377500,'J/mol'), E0=(34422.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2575742755888333, var=0.617967207487458, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R
    Total Standard Deviation in ln(k): 2.2231116393438284"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 2.2231116393438284""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 2.2231116393438284
""",
)

entry(
    index = 34,
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
    index = 35,
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
    index = 36,
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
    index = 37,
    label = "Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_Ext-1O-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(686.74,'m^3/(mol*s)'), n=1.69184, w0=(350000,'J/mol'), E0=(35000,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_Ext-1O-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_Ext-1O-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_Ext-1O-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_Ext-1O-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 38,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0",
    kinetics = ArrheniusBM(A=(2.83955e+16,'m^3/(mol*s)'), n=-2.761, w0=(313643,'J/mol'), E0=(95592.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.29852171789242454, var=7.1426436834029134, Tref=1000.0, N=35, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0',), comment="""BM rule fitted to 35 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0
    Total Standard Deviation in ln(k): 6.107854373560514"""),
    rank = 11,
    shortDesc = """BM rule fitted to 35 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0
Total Standard Deviation in ln(k): 6.107854373560514""",
    longDesc = 
"""
BM rule fitted to 35 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0
Total Standard Deviation in ln(k): 6.107854373560514
""",
)

entry(
    index = 39,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0",
    kinetics = ArrheniusBM(A=(3.97885e+44,'m^3/(mol*s)'), n=-10.9817, w0=(316000,'J/mol'), E0=(144082,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.7141322940934194, var=10.64610767058611, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0
    Total Standard Deviation in ln(k): 8.335426763958468"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0
Total Standard Deviation in ln(k): 8.335426763958468""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0
Total Standard Deviation in ln(k): 8.335426763958468
""",
)

entry(
    index = 40,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO",
    kinetics = ArrheniusBM(A=(6.68298e+09,'m^3/(mol*s)'), n=-0.947804, w0=(325382,'J/mol'), E0=(100437,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.15956278488190054, var=7.9289863625663894, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO',), comment="""BM rule fitted to 17 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO
    Total Standard Deviation in ln(k): 6.045935938003425"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO
Total Standard Deviation in ln(k): 6.045935938003425""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO
Total Standard Deviation in ln(k): 6.045935938003425
""",
)

entry(
    index = 41,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_N-Sp-4R!H-3CO",
    kinetics = ArrheniusBM(A=(9.68382e-07,'m^3/(mol*s)'), n=3.67709, w0=(327000,'J/mol'), E0=(51632.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.128423414068483, var=1.847793272702959, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_N-Sp-4R!H-3CO',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_N-Sp-4R!H-3CO
    Total Standard Deviation in ln(k): 3.047779653380861"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_N-Sp-4R!H-3CO
Total Standard Deviation in ln(k): 3.047779653380861""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_N-Sp-4R!H-3CO
Total Standard Deviation in ln(k): 3.047779653380861
""",
)

entry(
    index = 42,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C",
    kinetics = ArrheniusBM(A=(6.68696e+17,'m^3/(mol*s)'), n=-2.79216, w0=(327000,'J/mol'), E0=(102873,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.37014135262893855, var=6.525727053805741, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C
    Total Standard Deviation in ln(k): 6.051199920754665"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C
Total Standard Deviation in ln(k): 6.051199920754665""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C
Total Standard Deviation in ln(k): 6.051199920754665
""",
)

entry(
    index = 43,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_N-3CO->C",
    kinetics = ArrheniusBM(A=(0.000255477,'m^3/(mol*s)'), n=3.29069, w0=(299500,'J/mol'), E0=(46409,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.1508272982549048, var=0.002719354206827729, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_N-3CO->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_N-3CO->C
    Total Standard Deviation in ln(k): 2.996067652347333"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_N-3CO->C
Total Standard Deviation in ln(k): 2.996067652347333""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_N-3CO->C
Total Standard Deviation in ln(k): 2.996067652347333
""",
)

entry(
    index = 44,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C",
    kinetics = ArrheniusBM(A=(6.62937e+12,'m^3/(mol*s)'), n=-1.92871, w0=(299500,'J/mol'), E0=(85708.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2684032686381567, var=4.807017312705956, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C',), comment="""BM rule fitted to 19 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C
    Total Standard Deviation in ln(k): 5.069743927746765"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C
Total Standard Deviation in ln(k): 5.069743927746765""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C
Total Standard Deviation in ln(k): 5.069743927746765
""",
)

entry(
    index = 45,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C",
    kinetics = ArrheniusBM(A=(0.0555429,'m^3/(mol*s)'), n=2.47401, w0=(272000,'J/mol'), E0=(30063.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.030603751349406808, var=1.0310557228768036, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C
    Total Standard Deviation in ln(k): 2.1125201697409937"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C
Total Standard Deviation in ln(k): 2.1125201697409937""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C
Total Standard Deviation in ln(k): 2.1125201697409937
""",
)

entry(
    index = 46,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-3CO-R",
    kinetics = ArrheniusBM(A=(3.55662e+11,'m^3/(mol*s)'), n=-1.29676, w0=(299500,'J/mol'), E0=(9587.86,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.9976535147887824, var=17.5204291713158, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-3CO-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-3CO-R
    Total Standard Deviation in ln(k): 10.897969277941165"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-3CO-R
Total Standard Deviation in ln(k): 10.897969277941165""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-3CO-R
Total Standard Deviation in ln(k): 10.897969277941165
""",
)

entry(
    index = 47,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-1O-R",
    kinetics = ArrheniusBM(A=(0.110507,'m^3/(mol*s)'), n=2.54955, w0=(272000,'J/mol'), E0=(32710.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07656662572669266, var=1.8208793184283498, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-1O-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-1O-R
    Total Standard Deviation in ln(k): 2.8975671963302014"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-1O-R
Total Standard Deviation in ln(k): 2.8975671963302014""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-1O-R
Total Standard Deviation in ln(k): 2.8975671963302014
""",
)

entry(
    index = 48,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_1O-u0",
    kinetics = ArrheniusBM(A=(123.7,'m^3/(mol*s)'), n=1.59127, w0=(272000,'J/mol'), E0=(25987.5,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_1O-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_1O-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_1O-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_1O-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 49,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_N-1O-u0",
    kinetics = ArrheniusBM(A=(49.4221,'m^3/(mol*s)'), n=1.71189, w0=(299500,'J/mol'), E0=(29950,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_N-1O-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_N-1O-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_N-1O-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_N-1O-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 50,
    label = "Root_1R->H_3R-u1_3R->C_Ext-3C-R_4R!H->Cl_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.46205e-21,'m^3/(mol*s)'), n=8.00744, w0=(377500,'J/mol'), E0=(28207,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.07939550835360953, var=4.690480675805815, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->H_3R-u1_3R->C_Ext-3C-R_4R!H->Cl_Ext-3C-R',), comment="""BM rule fitted to 5 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_4R!H->Cl_Ext-3C-R
    Total Standard Deviation in ln(k): 4.541244719401769"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_4R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 4.541244719401769""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_4R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 4.541244719401769
""",
)

entry(
    index = 51,
    label = "Root_1R->H_3R-u1_3R->C_Ext-3C-R_N-4R!H->Cl_4BrCFINOPSSi->O",
    kinetics = ArrheniusBM(A=(8.88686e-05,'m^3/(mol*s)'), n=3.02721, w0=(377500,'J/mol'), E0=(42645.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R-u1_3R->C_Ext-3C-R_N-4R!H->Cl_4BrCFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_N-4R!H->Cl_4BrCFINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_N-4R!H->Cl_4BrCFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_N-4R!H->Cl_4BrCFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 52,
    label = "Root_1R->H_3R-u1_3R->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O",
    kinetics = ArrheniusBM(A=(1.08384e-14,'m^3/(mol*s)'), n=6.05537, w0=(377500,'J/mol'), E0=(50856.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.42585444802004124, var=1.0897109604820845, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->H_3R-u1_3R->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O',), comment="""BM rule fitted to 5 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O
    Total Standard Deviation in ln(k): 3.162713394518342"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O
Total Standard Deviation in ln(k): 3.162713394518342""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O
Total Standard Deviation in ln(k): 3.162713394518342
""",
)

entry(
    index = 53,
    label = "Root_1R->H_N-3R-u1_Ext-3R-R_4R!H->O_Ext-3R-R_N-5R!H->Cl_5BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.00165247,'m^3/(mol*s)'), n=2.72544, w0=(377500,'J/mol'), E0=(29640.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R-u1_Ext-3R-R_4R!H->O_Ext-3R-R_N-5R!H->Cl_5BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R-u1_Ext-3R-R_4R!H->O_Ext-3R-R_N-5R!H->Cl_5BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R-u1_Ext-3R-R_4R!H->O_Ext-3R-R_N-5R!H->Cl_5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R-u1_Ext-3R-R_4R!H->O_Ext-3R-R_N-5R!H->Cl_5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 54,
    label = "Root_1R->H_N-3R-u1_Ext-3R-R_4R!H->O_Ext-3R-R_N-5R!H->Cl_N-5BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.32627e-07,'m^3/(mol*s)'), n=4.44605, w0=(377500,'J/mol'), E0=(42371.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R-u1_Ext-3R-R_4R!H->O_Ext-3R-R_N-5R!H->Cl_N-5BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R-u1_Ext-3R-R_4R!H->O_Ext-3R-R_N-5R!H->Cl_N-5BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R-u1_Ext-3R-R_4R!H->O_Ext-3R-R_N-5R!H->Cl_N-5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R-u1_Ext-3R-R_4R!H->O_Ext-3R-R_N-5R!H->Cl_N-5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 55,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.17797e-12,'m^3/(mol*s)'), n=5.79755, w0=(377500,'J/mol'), E0=(32736.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3652981389217572, var=0.8299048279454785, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 2.7441303813139677"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 2.7441303813139677""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 2.7441303813139677
""",
)

entry(
    index = 56,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(0.00375102,'m^3/(mol*s)'), n=3.05715, w0=(377500,'J/mol'), E0=(64714.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.03174808013519349, var=0.39656910030912185, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H-1C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H-1C
    Total Standard Deviation in ln(k): 1.3422255534202197"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H-1C
Total Standard Deviation in ln(k): 1.3422255534202197""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H-1C
Total Standard Deviation in ln(k): 1.3422255534202197
""",
)

entry(
    index = 57,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(30.5257,'m^3/(mol*s)'), n=2.04125, w0=(377500,'J/mol'), E0=(91724.3,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 58,
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
    index = 59,
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
    index = 60,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_Sp-4R!H#1C",
    kinetics = ArrheniusBM(A=(725.803,'m^3/(mol*s)'), n=1.0218, w0=(327000,'J/mol'), E0=(54101.3,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_Sp-4R!H#1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_Sp-4R!H#1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_Sp-4R!H#1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_Sp-4R!H#1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 61,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C",
    kinetics = ArrheniusBM(A=(9.28875e+16,'m^3/(mol*s)'), n=-2.90771, w0=(313250,'J/mol'), E0=(96807.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.30727086663337616, var=7.344567170203975, Tref=1000.0, N=34, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C',), comment="""BM rule fitted to 34 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C
    Total Standard Deviation in ln(k): 6.205042206003716"""),
    rank = 11,
    shortDesc = """BM rule fitted to 34 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C
Total Standard Deviation in ln(k): 6.205042206003716""",
    longDesc = 
"""
BM rule fitted to 34 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C
Total Standard Deviation in ln(k): 6.205042206003716
""",
)

entry(
    index = 62,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_3CO->C",
    kinetics = ArrheniusBM(A=(2.09006e+21,'m^3/(mol*s)'), n=-4.10814, w0=(327000,'J/mol'), E0=(106777,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.3984396658087612, var=8.026128845913888, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_3CO->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_3CO->C
    Total Standard Deviation in ln(k): 6.68060402348377"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_3CO->C
Total Standard Deviation in ln(k): 6.68060402348377""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_3CO->C
Total Standard Deviation in ln(k): 6.68060402348377
""",
)

entry(
    index = 63,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_N-3CO->C",
    kinetics = ArrheniusBM(A=(3.51966e+14,'m^3/(mol*s)'), n=-2.13937, w0=(299500,'J/mol'), E0=(7389.03,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.6795243041270407, var=18.39783655042363, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_N-3CO->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_N-3CO->C
    Total Standard Deviation in ln(k): 10.306197387100978"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_N-3CO->C
Total Standard Deviation in ln(k): 10.306197387100978""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_N-3CO->C
Total Standard Deviation in ln(k): 10.306197387100978
""",
)

entry(
    index = 64,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C",
    kinetics = ArrheniusBM(A=(9.85811e-09,'m^3/(mol*s)'), n=4.29223, w0=(327000,'J/mol'), E0=(64581.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06244161039191973, var=5.808851492329322, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C',), comment="""BM rule fitted to 16 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C
    Total Standard Deviation in ln(k): 4.988612555526826"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C
Total Standard Deviation in ln(k): 4.988612555526826""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C
Total Standard Deviation in ln(k): 4.988612555526826
""",
)

entry(
    index = 65,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_N-3CO->C",
    kinetics = ArrheniusBM(A=(0.00010035,'m^3/(mol*s)'), n=3.57133, w0=(299500,'J/mol'), E0=(29950,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_N-3CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_N-3CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_N-3CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_N-3CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 66,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_N-Sp-4R!H-3CO_Sp-4R!H=3CO",
    kinetics = ArrheniusBM(A=(0.000142581,'m^3/(mol*s)'), n=3.33955, w0=(327000,'J/mol'), E0=(70800.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_N-Sp-4R!H-3CO_Sp-4R!H=3CO',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_N-Sp-4R!H-3CO_Sp-4R!H=3CO
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_N-Sp-4R!H-3CO_Sp-4R!H=3CO
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_N-Sp-4R!H-3CO_Sp-4R!H=3CO
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 67,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_N-Sp-4R!H-3CO_N-Sp-4R!H=3CO",
    kinetics = ArrheniusBM(A=(1565.77,'m^3/(mol*s)'), n=0.653508, w0=(327000,'J/mol'), E0=(57810,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_N-Sp-4R!H-3CO_N-Sp-4R!H=3CO',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_N-Sp-4R!H-3CO_N-Sp-4R!H=3CO
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_N-Sp-4R!H-3CO_N-Sp-4R!H=3CO
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_N-Sp-4R!H-3CO_N-Sp-4R!H=3CO
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 68,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C_Ext-3C-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(0.000402485,'m^3/(mol*s)'), n=3.52032, w0=(327000,'J/mol'), E0=(81512.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C_Ext-3C-R_4R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C_Ext-3C-R_4R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C_Ext-3C-R_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C_Ext-3C-R_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 69,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C_Ext-3C-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(1.88915e+15,'m^3/(mol*s)'), n=-2.05687, w0=(327000,'J/mol'), E0=(92104.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.35850872598344286, var=6.491775320833799, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C_Ext-3C-R_N-4R!H->Cl',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C_Ext-3C-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 6.008632687257341"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C_Ext-3C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 6.008632687257341""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C_Ext-3C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 6.008632687257341
""",
)

entry(
    index = 70,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_N-3CO->C_1C-u0",
    kinetics = ArrheniusBM(A=(10.5404,'m^3/(mol*s)'), n=2.14943, w0=(299500,'J/mol'), E0=(69107.5,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_N-3CO->C_1C-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_N-3CO->C_1C-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_N-3CO->C_1C-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_N-3CO->C_1C-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 71,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_N-3CO->C_N-1C-u0",
    kinetics = ArrheniusBM(A=(5.81832,'m^3/(mol*s)'), n=1.87825, w0=(299500,'J/mol'), E0=(29950,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_N-3CO->C_N-1C-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_N-3CO->C_N-1C-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_N-3CO->C_N-1C-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_N-3CO->C_N-1C-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 72,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0",
    kinetics = ArrheniusBM(A=(2.41947e+08,'m^3/(mol*s)'), n=-0.586754, w0=(299500,'J/mol'), E0=(70494.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2080500035969287, var=2.6388949880834622, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0
    Total Standard Deviation in ln(k): 3.7793658851743057"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0
Total Standard Deviation in ln(k): 3.7793658851743057""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0
Total Standard Deviation in ln(k): 3.7793658851743057
""",
)

entry(
    index = 73,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0",
    kinetics = ArrheniusBM(A=(5.4579e+10,'m^3/(mol*s)'), n=-1.359, w0=(299500,'J/mol'), E0=(87943.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.20366396674710358, var=7.684240057652333, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0
    Total Standard Deviation in ln(k): 6.06893673476686"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0
Total Standard Deviation in ln(k): 6.06893673476686""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0
Total Standard Deviation in ln(k): 6.06893673476686
""",
)

entry(
    index = 74,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R",
    kinetics = ArrheniusBM(A=(0.00388211,'m^3/(mol*s)'), n=2.85277, w0=(272000,'J/mol'), E0=(32134.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04589669828831547, var=1.4469474369311661, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R
    Total Standard Deviation in ln(k): 2.5267966852411075"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R
Total Standard Deviation in ln(k): 2.5267966852411075""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R
Total Standard Deviation in ln(k): 2.5267966852411075
""",
)

entry(
    index = 75,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_1O-u0",
    kinetics = ArrheniusBM(A=(106.711,'m^3/(mol*s)'), n=1.43958, w0=(272000,'J/mol'), E0=(37458,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3538790862357264, var=0.7140174652931102, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_1O-u0',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_1O-u0
    Total Standard Deviation in ln(k): 2.583135635203758"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_1O-u0
Total Standard Deviation in ln(k): 2.583135635203758""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_1O-u0
Total Standard Deviation in ln(k): 2.583135635203758
""",
)

entry(
    index = 76,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_N-1O-u0",
    kinetics = ArrheniusBM(A=(3250.38,'m^3/(mol*s)'), n=1.00954, w0=(272000,'J/mol'), E0=(28222.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_N-1O-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_N-1O-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_N-1O-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_N-1O-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 77,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-3CO-R_1O-u0",
    kinetics = ArrheniusBM(A=(9.42083e-09,'m^3/(mol*s)'), n=4.58515, w0=(299500,'J/mol'), E0=(29950,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-3CO-R_1O-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-3CO-R_1O-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-3CO-R_1O-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-3CO-R_1O-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 78,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-3CO-R_N-1O-u0",
    kinetics = ArrheniusBM(A=(1.51797e+28,'m^3/(mol*s)'), n=-6.20187, w0=(299500,'J/mol'), E0=(102831,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.46064460116188666, var=13.397136236333651, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-3CO-R_N-1O-u0',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-3CO-R_N-1O-u0
    Total Standard Deviation in ln(k): 8.495149597028348"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-3CO-R_N-1O-u0
Total Standard Deviation in ln(k): 8.495149597028348""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-3CO-R_N-1O-u0
Total Standard Deviation in ln(k): 8.495149597028348
""",
)

entry(
    index = 79,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-1O-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(0.0308162,'m^3/(mol*s)'), n=2.73613, w0=(272000,'J/mol'), E0=(27200,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.9493663578396799, var=0.920324346967258, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-1O-R_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-1O-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 4.3085558694637704"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-1O-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 4.3085558694637704""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-1O-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 4.3085558694637704
""",
)

entry(
    index = 80,
    label = "Root_1R->H_3R-u1_3R->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(1.69768e-06,'m^3/(mol*s)'), n=3.14895, w0=(377500,'J/mol'), E0=(60805,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R-u1_3R->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 81,
    label = "Root_1R->H_3R-u1_3R->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(0.0468168,'m^3/(mol*s)'), n=2.26588, w0=(377500,'J/mol'), E0=(78529.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.02660991472730535, var=3.5650555281316265, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->H_3R-u1_3R->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl',), comment="""BM rule fitted to 4 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 3.852070476570137"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 3.852070476570137""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 3.852070476570137
""",
)

entry(
    index = 82,
    label = "Root_1R->H_3R-u1_3R->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_Sp-4C-3C",
    kinetics = ArrheniusBM(A=(3.79956e-23,'m^3/(mol*s)'), n=8.56468, w0=(377500,'J/mol'), E0=(21647.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.028777355226612043, var=1.245488616695992, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->H_3R-u1_3R->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_Sp-4C-3C',), comment="""BM rule fitted to 4 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_Sp-4C-3C
    Total Standard Deviation in ln(k): 2.3096185544345365"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_Sp-4C-3C
Total Standard Deviation in ln(k): 2.3096185544345365""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_Sp-4C-3C
Total Standard Deviation in ln(k): 2.3096185544345365
""",
)

entry(
    index = 83,
    label = "Root_1R->H_3R-u1_3R->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_N-Sp-4C-3C",
    kinetics = ArrheniusBM(A=(0.0817363,'m^3/(mol*s)'), n=2.26425, w0=(377500,'J/mol'), E0=(86118.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R-u1_3R->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_N-Sp-4C-3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_N-Sp-4C-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_N-Sp-4C-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_N-Sp-4C-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 84,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.0274051,'m^3/(mol*s)'), n=2.81357, w0=(377500,'J/mol'), E0=(61953.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.05075374461238742, var=0.59062647589648, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 1.6682055191337992"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 1.6682055191337992""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 1.6682055191337992
""",
)

entry(
    index = 85,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_4R!H->O",
    kinetics = ArrheniusBM(A=(1.45326e-13,'m^3/(mol*s)'), n=6.13051, w0=(377500,'J/mol'), E0=(19577.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.15886620400003676, var=7.553162969446625, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_4R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_4R!H->O
    Total Standard Deviation in ln(k): 5.908778405987587"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_4R!H->O
Total Standard Deviation in ln(k): 5.908778405987587""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_4R!H->O
Total Standard Deviation in ln(k): 5.908778405987587
""",
)

entry(
    index = 86,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(2.64977e-08,'m^3/(mol*s)'), n=4.54941, w0=(377500,'J/mol'), E0=(49235.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.29500740776551937, var=0.7219452906301368, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_N-4R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_N-4R!H->O
    Total Standard Deviation in ln(k): 2.444595188493977"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_N-4R!H->O
Total Standard Deviation in ln(k): 2.444595188493977""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_N-4R!H->O
Total Standard Deviation in ln(k): 2.444595188493977
""",
)

entry(
    index = 87,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C",
    kinetics = ArrheniusBM(A=(22.5282,'m^3/(mol*s)'), n=1.94121, w0=(377500,'J/mol'), E0=(71325.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00062508731480322, var=0.03658460137297469, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C
    Total Standard Deviation in ln(k): 0.3850182852178551"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C
Total Standard Deviation in ln(k): 0.3850182852178551""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C
Total Standard Deviation in ln(k): 0.3850182852178551
""",
)

entry(
    index = 88,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(21.1963,'m^3/(mol*s)'), n=1.98009, w0=(377500,'J/mol'), E0=(79874.2,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 89,
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
    index = 90,
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
    index = 91,
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
    index = 92,
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
    index = 93,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C",
    kinetics = ArrheniusBM(A=(1.45386e+18,'m^3/(mol*s)'), n=-3.28285, w0=(313250,'J/mol'), E0=(100099,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.3260301248074145, var=7.777987883218455, Tref=1000.0, N=26, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C',), comment="""BM rule fitted to 26 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C
    Total Standard Deviation in ln(k): 6.410185693076269"""),
    rank = 11,
    shortDesc = """BM rule fitted to 26 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C
Total Standard Deviation in ln(k): 6.410185693076269""",
    longDesc = 
"""
BM rule fitted to 26 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C
Total Standard Deviation in ln(k): 6.410185693076269
""",
)

entry(
    index = 94,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(3.06696e+13,'m^3/(mol*s)'), n=-1.80674, w0=(313250,'J/mol'), E0=(86989.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.24881155289575135, var=7.799864758668893, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C
    Total Standard Deviation in ln(k): 6.224026485475163"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C
Total Standard Deviation in ln(k): 6.224026485475163""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C
Total Standard Deviation in ln(k): 6.224026485475163
""",
)

entry(
    index = 95,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_3CO->C_Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(1.13946e+21,'m^3/(mol*s)'), n=-4.04791, w0=(327000,'J/mol'), E0=(106860,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.37489169118768667, var=10.618664007825155, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_3CO->C_Sp-4R!H-1C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_3CO->C_Sp-4R!H-1C
    Total Standard Deviation in ln(k): 7.4746271055215985"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_3CO->C_Sp-4R!H-1C
Total Standard Deviation in ln(k): 7.4746271055215985""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_3CO->C_Sp-4R!H-1C
Total Standard Deviation in ln(k): 7.4746271055215985
""",
)

entry(
    index = 96,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_3CO->C_N-Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(0.171123,'m^3/(mol*s)'), n=2.55484, w0=(327000,'J/mol'), E0=(52803.6,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_3CO->C_N-Sp-4R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_3CO->C_N-Sp-4R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_3CO->C_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_3CO->C_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 97,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_N-3CO->C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(157.231,'m^3/(mol*s)'), n=1.7152, w0=(299500,'J/mol'), E0=(57523.1,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_N-3CO->C_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_N-3CO->C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_N-3CO->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_N-3CO->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 98,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_N-3CO->C_3O-u1",
    kinetics = ArrheniusBM(A=(0.977703,'m^3/(mol*s)'), n=2.24188, w0=(299500,'J/mol'), E0=(29950,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_N-3CO->C_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_N-3CO->C_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_N-3CO->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_N-3CO->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 99,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_N-3CO->C_N-3O-u1",
    kinetics = ArrheniusBM(A=(6.02711e+12,'m^3/(mol*s)'), n=-1.6274, w0=(299500,'J/mol'), E0=(29950,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.1436236221143194, var=4.026662798346816, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_N-3CO->C_N-3O-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_N-3CO->C_N-3O-u1
    Total Standard Deviation in ln(k): 9.408799922389525"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_N-3CO->C_N-3O-u1
Total Standard Deviation in ln(k): 9.408799922389525""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_N-3CO->C_N-3O-u1
Total Standard Deviation in ln(k): 9.408799922389525
""",
)

entry(
    index = 100,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_4R!H->O",
    kinetics = ArrheniusBM(A=(0.00024821,'m^3/(mol*s)'), n=3.22649, w0=(327000,'J/mol'), E0=(70085.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.004212251695671604, var=0.40829207818120206, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_4R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_4R!H->O
    Total Standard Deviation in ln(k): 1.2915638924059043"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_4R!H->O
Total Standard Deviation in ln(k): 1.2915638924059043""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_4R!H->O
Total Standard Deviation in ln(k): 1.2915638924059043
""",
)

entry(
    index = 101,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O",
    kinetics = ArrheniusBM(A=(1.20316e-09,'m^3/(mol*s)'), n=4.50799, w0=(327000,'J/mol'), E0=(63518.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.20275042387002915, var=6.599464473515534, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O
    Total Standard Deviation in ln(k): 5.6594718899384775"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O
Total Standard Deviation in ln(k): 5.6594718899384775""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O
Total Standard Deviation in ln(k): 5.6594718899384775
""",
)

entry(
    index = 102,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.152133,'m^3/(mol*s)'), n=2.74148, w0=(327000,'J/mol'), E0=(32854.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.1852194704518617, var=3.887251939569645, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R
    Total Standard Deviation in ln(k): 6.930497117606022"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 6.930497117606022""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 6.930497117606022
""",
)

entry(
    index = 103,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C",
    kinetics = ArrheniusBM(A=(0.000211072,'m^3/(mol*s)'), n=3.51383, w0=(327000,'J/mol'), E0=(66463.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.434397016262092e-05, var=4.624184474197434, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C
    Total Standard Deviation in ln(k): 4.311001716272808"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 4.311001716272808""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 4.311001716272808
""",
)

entry(
    index = 104,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C",
    kinetics = ArrheniusBM(A=(0.000854975,'m^3/(mol*s)'), n=3.28947, w0=(327000,'J/mol'), E0=(42838.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 105,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-1O-R",
    kinetics = ArrheniusBM(A=(0.00549393,'m^3/(mol*s)'), n=2.84052, w0=(299500,'J/mol'), E0=(29950,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-1O-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-1O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 106,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(656261,'m^3/(mol*s)'), n=0.0702041, w0=(299500,'J/mol'), E0=(68025.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.17788204649216852, var=2.5519365198240815, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-4R!H-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 3.64946034824079"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 3.64946034824079""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 3.64946034824079
""",
)

entry(
    index = 107,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.7748e+08,'m^3/(mol*s)'), n=-0.567796, w0=(299500,'J/mol'), E0=(64072.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.02409934325959359, var=4.714725724870595, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 4.413516421751511"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 4.413516421751511""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 4.413516421751511
""",
)

entry(
    index = 108,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(0.000109307,'m^3/(mol*s)'), n=3.0545, w0=(299500,'J/mol'), E0=(26145.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 109,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(1.57337e-06,'m^3/(mol*s)'), n=3.83129, w0=(299500,'J/mol'), E0=(24049.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 110,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.25359e+10,'m^3/(mol*s)'), n=-1.28264, w0=(299500,'J/mol'), E0=(86517.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2002502089021511, var=8.940981631799128, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0_Ext-3C-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0_Ext-3C-R
    Total Standard Deviation in ln(k): 6.497594660745798"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0_Ext-3C-R
Total Standard Deviation in ln(k): 6.497594660745798""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0_Ext-3C-R
Total Standard Deviation in ln(k): 6.497594660745798
""",
)

entry(
    index = 111,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(0.000153612,'m^3/(mol*s)'), n=3.32595, w0=(272000,'J/mol'), E0=(27200,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06393013539151016, var=3.8677789223461145, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R_Ext-4R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 4.103274716453381"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 4.103274716453381""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 4.103274716453381
""",
)

entry(
    index = 112,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R_4R!H->C",
    kinetics = ArrheniusBM(A=(14.9375,'m^3/(mol*s)'), n=1.73494, w0=(272000,'J/mol'), E0=(36835.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.21026825362471163, var=0.4178948848535683, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R_4R!H->C
    Total Standard Deviation in ln(k): 1.8242689719039558"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R_4R!H->C
Total Standard Deviation in ln(k): 1.8242689719039558""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R_4R!H->C
Total Standard Deviation in ln(k): 1.8242689719039558
""",
)

entry(
    index = 113,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.00123036,'m^3/(mol*s)'), n=2.89569, w0=(272000,'J/mol'), E0=(19743.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 114,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_1O-u0_Ext-1O-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(0.0898359,'m^3/(mol*s)'), n=2.42885, w0=(272000,'J/mol'), E0=(27200,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_1O-u0_Ext-1O-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_1O-u0_Ext-1O-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_1O-u0_Ext-1O-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_1O-u0_Ext-1O-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 115,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_1O-u0_Ext-1O-R_4R!H->C",
    kinetics = ArrheniusBM(A=(0.0703235,'m^3/(mol*s)'), n=2.34313, w0=(272000,'J/mol'), E0=(27346.4,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_1O-u0_Ext-1O-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_1O-u0_Ext-1O-R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_1O-u0_Ext-1O-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_1O-u0_Ext-1O-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 116,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_1O-u0_Ext-1O-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.0597365,'m^3/(mol*s)'), n=2.3895, w0=(272000,'J/mol'), E0=(29395.1,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_1O-u0_Ext-1O-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_1O-u0_Ext-1O-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_1O-u0_Ext-1O-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_1O-u0_Ext-1O-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 117,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-3CO-R_N-1O-u0_4R!H->Cl",
    kinetics = ArrheniusBM(A=(0.0728097,'m^3/(mol*s)'), n=2.4863, w0=(299500,'J/mol'), E0=(44286.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-3CO-R_N-1O-u0_4R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-3CO-R_N-1O-u0_4R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-3CO-R_N-1O-u0_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-3CO-R_N-1O-u0_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 118,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-3CO-R_N-1O-u0_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(1.00602e+11,'m^3/(mol*s)'), n=-1.20083, w0=(299500,'J/mol'), E0=(29950,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.3362374338043312, var=9.880229420684959, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-3CO-R_N-1O-u0_N-4R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-3CO-R_N-1O-u0_N-4R!H->Cl
    Total Standard Deviation in ln(k): 12.171393436569069"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-3CO-R_N-1O-u0_N-4R!H->Cl
Total Standard Deviation in ln(k): 12.171393436569069""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-3CO-R_N-1O-u0_N-4R!H->Cl
Total Standard Deviation in ln(k): 12.171393436569069
""",
)

entry(
    index = 119,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-1O-R_Ext-4R!H-R_Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(220.761,'m^3/(mol*s)'), n=1.59458, w0=(272000,'J/mol'), E0=(27200,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-1O-R_Ext-4R!H-R_Sp-5R!H=4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-1O-R_Ext-4R!H-R_Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-1O-R_Ext-4R!H-R_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-1O-R_Ext-4R!H-R_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 120,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-1O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(234.788,'m^3/(mol*s)'), n=1.5918, w0=(272000,'J/mol'), E0=(27200,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-1O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-1O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-1O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-1O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 121,
    label = "Root_1R->H_3R-u1_3R->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_5BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.47941e-05,'m^3/(mol*s)'), n=3.18409, w0=(377500,'J/mol'), E0=(73363.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.008751019579953811, var=0.016210212646957767, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_3R-u1_3R->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_5BrCFINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_5BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 0.2772290199968415"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 0.2772290199968415""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 0.2772290199968415
""",
)

entry(
    index = 122,
    label = "Root_1R->H_3R-u1_3R->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.00206404,'m^3/(mol*s)'), n=2.78833, w0=(377500,'J/mol'), E0=(72596.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0002119164358598332, var=3.403029882863948, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_3R-u1_3R->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 3.698727995796727"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 3.698727995796727""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 3.698727995796727
""",
)

entry(
    index = 123,
    label = "Root_1R->H_3R-u1_3R->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_Sp-4C-3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.78958e-24,'m^3/(mol*s)'), n=8.97966, w0=(377500,'J/mol'), E0=(20773,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.023970174077602345, var=4.918715771692648, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_3R-u1_3R->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_Sp-4C-3C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_Sp-4C-3C_Ext-3C-R
    Total Standard Deviation in ln(k): 4.506363696882636"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_Sp-4C-3C_Ext-3C-R
Total Standard Deviation in ln(k): 4.506363696882636""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_Sp-4C-3C_Ext-3C-R
Total Standard Deviation in ln(k): 4.506363696882636
""",
)

entry(
    index = 124,
    label = "Root_1R->H_3R-u1_3R->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_Sp-4C-3C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(0.00460907,'m^3/(mol*s)'), n=2.46786, w0=(377500,'J/mol'), E0=(66556.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R-u1_3R->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_Sp-4C-3C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_Sp-4C-3C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_Sp-4C-3C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_Sp-4C-3C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 125,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_Ext-1C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(0.283009,'m^3/(mol*s)'), n=2.49244, w0=(377500,'J/mol'), E0=(65783.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.013202258029997667, var=0.12026491276161314, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_Ext-1C-R_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_Ext-1C-R_4R!H->C
    Total Standard Deviation in ln(k): 0.7283982297639695"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_Ext-1C-R_4R!H->C
Total Standard Deviation in ln(k): 0.7283982297639695""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_Ext-1C-R_4R!H->C
Total Standard Deviation in ln(k): 0.7283982297639695
""",
)

entry(
    index = 126,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_Ext-1C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(185.874,'m^3/(mol*s)'), n=1.75948, w0=(377500,'J/mol'), E0=(71729.9,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_Ext-1C-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_Ext-1C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_Ext-1C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_Ext-1C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 127,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_4R!H->O_5R!H->C",
    kinetics = ArrheniusBM(A=(43.7292,'m^3/(mol*s)'), n=1.85998, w0=(377500,'J/mol'), E0=(56644.5,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_4R!H->O_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_4R!H->O_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_4R!H->O_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_4R!H->O_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 128,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_4R!H->O_N-5R!H->C",
    kinetics = ArrheniusBM(A=(52.0355,'m^3/(mol*s)'), n=1.85451, w0=(377500,'J/mol'), E0=(76275.3,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_4R!H->O_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_4R!H->O_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_4R!H->O_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_4R!H->O_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 129,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_N-4R!H->O_4CCl->Cl",
    kinetics = ArrheniusBM(A=(17.8736,'m^3/(mol*s)'), n=1.94617, w0=(377500,'J/mol'), E0=(76893.3,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_N-4R!H->O_4CCl->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_N-4R!H->O_4CCl->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_N-4R!H->O_4CCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_N-4R!H->O_4CCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 130,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_N-4R!H->O_N-4CCl->Cl",
    kinetics = ArrheniusBM(A=(1.07073e-06,'m^3/(mol*s)'), n=4.09244, w0=(377500,'J/mol'), E0=(52129.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.021218192964305292, var=1.3330683711387485, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_N-4R!H->O_N-4CCl->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_N-4R!H->O_N-4CCl->Cl
    Total Standard Deviation in ln(k): 2.3679506971142366"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_N-4R!H->O_N-4CCl->Cl
Total Standard Deviation in ln(k): 2.3679506971142366""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_N-4R!H->O_N-4CCl->Cl
Total Standard Deviation in ln(k): 2.3679506971142366
""",
)

entry(
    index = 131,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(16.8467,'m^3/(mol*s)'), n=2.0298, w0=(377500,'J/mol'), E0=(73670,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 132,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C",
    kinetics = ArrheniusBM(A=(1.60825e-05,'m^3/(mol*s)'), n=3.40139, w0=(327000,'J/mol'), E0=(65288.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.023746782292244077, var=2.5193273706961716, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C
    Total Standard Deviation in ln(k): 3.24165880960854"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C
Total Standard Deviation in ln(k): 3.24165880960854""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C
Total Standard Deviation in ln(k): 3.24165880960854
""",
)

entry(
    index = 133,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C",
    kinetics = ArrheniusBM(A=(1.06485e+15,'m^3/(mol*s)'), n=-2.26114, w0=(299500,'J/mol'), E0=(80237.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2547348881247274, var=3.0443353891954215, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C
    Total Standard Deviation in ln(k): 4.13790396689933"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C
Total Standard Deviation in ln(k): 4.13790396689933""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C
Total Standard Deviation in ln(k): 4.13790396689933
""",
)

entry(
    index = 134,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_3CO->C",
    kinetics = ArrheniusBM(A=(0.000529766,'m^3/(mol*s)'), n=3.10699, w0=(327000,'J/mol'), E0=(68601.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0013104969238321715, var=0.8017589451212953, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_3CO->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_3CO->C
    Total Standard Deviation in ln(k): 1.7983524038196275"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_3CO->C
Total Standard Deviation in ln(k): 1.7983524038196275""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_3CO->C
Total Standard Deviation in ln(k): 1.7983524038196275
""",
)

entry(
    index = 135,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_N-3CO->C",
    kinetics = ArrheniusBM(A=(0.000301781,'m^3/(mol*s)'), n=3.23474, w0=(299500,'J/mol'), E0=(28353.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06712907188497877, var=0.21618119390996673, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_N-3CO->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_N-3CO->C
    Total Standard Deviation in ln(k): 1.100773386283186"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_N-3CO->C
Total Standard Deviation in ln(k): 1.100773386283186""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_N-3CO->C
Total Standard Deviation in ln(k): 1.100773386283186
""",
)

entry(
    index = 136,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_3CO->C_Sp-4R!H-1C_4R!H->O",
    kinetics = ArrheniusBM(A=(1.39543e+19,'m^3/(mol*s)'), n=-3.47206, w0=(327000,'J/mol'), E0=(91807.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.5352246413685504, var=11.15051032067538, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_3CO->C_Sp-4R!H-1C_4R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_3CO->C_Sp-4R!H-1C_4R!H->O
    Total Standard Deviation in ln(k): 8.03907305143576"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_3CO->C_Sp-4R!H-1C_4R!H->O
Total Standard Deviation in ln(k): 8.03907305143576""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_3CO->C_Sp-4R!H-1C_4R!H->O
Total Standard Deviation in ln(k): 8.03907305143576
""",
)

entry(
    index = 137,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_3CO->C_Sp-4R!H-1C_N-4R!H->O",
    kinetics = ArrheniusBM(A=(86.872,'m^3/(mol*s)'), n=1.58191, w0=(327000,'J/mol'), E0=(83090.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.019437028169395205, var=22.281750390558173, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_3CO->C_Sp-4R!H-1C_N-4R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_3CO->C_Sp-4R!H-1C_N-4R!H->O
    Total Standard Deviation in ln(k): 9.511897801800835"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_3CO->C_Sp-4R!H-1C_N-4R!H->O
Total Standard Deviation in ln(k): 9.511897801800835""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_3CO->C_Sp-4R!H-1C_N-4R!H->O
Total Standard Deviation in ln(k): 9.511897801800835
""",
)

entry(
    index = 138,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_N-3CO->C_N-3O-u1_Ext-1C-R",
    kinetics = ArrheniusBM(A=(52.7701,'m^3/(mol*s)'), n=1.64048, w0=(299500,'J/mol'), E0=(29950,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_N-3CO->C_N-3O-u1_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_N-3CO->C_N-3O-u1_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_N-3CO->C_N-3O-u1_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_N-3CO->C_N-3O-u1_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 139,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_4R!H->O_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.000146255,'m^3/(mol*s)'), n=3.28146, w0=(327000,'J/mol'), E0=(68864.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.3972069040578369e-06, var=1.42217436415227, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_4R!H->O_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_4R!H->O_Ext-3C-R
    Total Standard Deviation in ln(k): 2.390749370307093"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_4R!H->O_Ext-3C-R
Total Standard Deviation in ln(k): 2.390749370307093""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_4R!H->O_Ext-3C-R
Total Standard Deviation in ln(k): 2.390749370307093
""",
)

entry(
    index = 140,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R",
    kinetics = ArrheniusBM(A=(8.1618e-11,'m^3/(mol*s)'), n=4.78808, w0=(327000,'J/mol'), E0=(59610.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.16523340111328927, var=9.418354335126809, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R
    Total Standard Deviation in ln(k): 6.56755842936232"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R
Total Standard Deviation in ln(k): 6.56755842936232""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R
Total Standard Deviation in ln(k): 6.56755842936232
""",
)

entry(
    index = 141,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_4CCl->C",
    kinetics = ArrheniusBM(A=(0.000260574,'m^3/(mol*s)'), n=3.15048, w0=(327000,'J/mol'), E0=(77234.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.004865731787735809, var=0.8929501064141481, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_4CCl->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_4CCl->C
    Total Standard Deviation in ln(k): 1.9066206631198352"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_4CCl->C
Total Standard Deviation in ln(k): 1.9066206631198352""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_4CCl->C
Total Standard Deviation in ln(k): 1.9066206631198352
""",
)

entry(
    index = 142,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_N-4CCl->C",
    kinetics = ArrheniusBM(A=(1.55621e-05,'m^3/(mol*s)'), n=3.2096, w0=(327000,'J/mol'), E0=(75826.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_N-4CCl->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_N-4CCl->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_N-4CCl->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_N-4CCl->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 143,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.41803e-05,'m^3/(mol*s)'), n=3.69234, w0=(327000,'J/mol'), E0=(23552.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 144,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.44905e-09,'m^3/(mol*s)'), n=5.34441, w0=(327000,'J/mol'), E0=(22954.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 145,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.22681e-05,'m^3/(mol*s)'), n=3.91521, w0=(327000,'J/mol'), E0=(59342.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_4BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 146,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(5.21196e-06,'m^3/(mol*s)'), n=3.85925, w0=(327000,'J/mol'), E0=(61730.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3CO-u1_3CO->C_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 147,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-4R!H-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.18121e+07,'m^3/(mol*s)'), n=-0.491976, w0=(299500,'J/mol'), E0=(68244.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.21629641272552838, var=3.795855785388044, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-4R!H-R_Ext-3C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-4R!H-R_Ext-3C-R
    Total Standard Deviation in ln(k): 4.449274874673261"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-4R!H-R_Ext-3C-R
Total Standard Deviation in ln(k): 4.449274874673261""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-4R!H-R_Ext-3C-R
Total Standard Deviation in ln(k): 4.449274874673261
""",
)

entry(
    index = 148,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(7.47383e-08,'m^3/(mol*s)'), n=4.03904, w0=(299500,'J/mol'), E0=(21110.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 149,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(6.87704e-06,'m^3/(mol*s)'), n=3.32501, w0=(299500,'J/mol'), E0=(35544.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.14776672778724748, var=0.14057391106349015, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R_N-4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 1.1229122673018517"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 1.1229122673018517""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 1.1229122673018517
""",
)

entry(
    index = 150,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(63141.7,'m^3/(mol*s)'), n=0.182176, w0=(299500,'J/mol'), E0=(74503.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.09660683834384302, var=13.539871730439112, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 7.619467145931699"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 7.619467145931699""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 7.619467145931699
""",
)

entry(
    index = 151,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0_Ext-3C-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(0.205248,'m^3/(mol*s)'), n=2.23631, w0=(299500,'J/mol'), E0=(68118.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0012217836043421073, var=13.990314241188614, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0_Ext-3C-R_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0_Ext-3C-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 7.5015064133577525"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0_Ext-3C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 7.5015064133577525""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0_Ext-3C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 7.5015064133577525
""",
)

entry(
    index = 152,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R_Ext-4R!H-R_Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(0.0853731,'m^3/(mol*s)'), n=2.28596, w0=(272000,'J/mol'), E0=(27200,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R_Ext-4R!H-R_Sp-5R!H=4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R_Ext-4R!H-R_Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R_Ext-4R!H-R_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R_Ext-4R!H-R_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 153,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(0.0214236,'m^3/(mol*s)'), n=2.72353, w0=(272000,'J/mol'), E0=(27200,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.7890304190584024, var=1.5320421056338418, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 4.463863134150054"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 4.463863134150054""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 4.463863134150054
""",
)

entry(
    index = 154,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R_4R!H->C_1O-u0",
    kinetics = ArrheniusBM(A=(0.000417933,'m^3/(mol*s)'), n=2.98801, w0=(272000,'J/mol'), E0=(21054.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R_4R!H->C_1O-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R_4R!H->C_1O-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R_4R!H->C_1O-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R_4R!H->C_1O-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 155,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R_4R!H->C_N-1O-u0",
    kinetics = ArrheniusBM(A=(25.2691,'m^3/(mol*s)'), n=1.65303, w0=(272000,'J/mol'), E0=(35437.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R_4R!H->C_N-1O-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R_4R!H->C_N-1O-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R_4R!H->C_N-1O-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R_4R!H->C_N-1O-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 156,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-3CO-R_N-1O-u0_N-4R!H->Cl_Ext-3CO-R",
    kinetics = ArrheniusBM(A=(3626.97,'m^3/(mol*s)'), n=0.934699, w0=(299500,'J/mol'), E0=(29950,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-3CO-R_N-1O-u0_N-4R!H->Cl_Ext-3CO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-3CO-R_N-1O-u0_N-4R!H->Cl_Ext-3CO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-3CO-R_N-1O-u0_N-4R!H->Cl_Ext-3CO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-3CO-u1_Ext-3CO-R_N-1O-u0_N-4R!H->Cl_Ext-3CO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 157,
    label = "Root_1R->H_3R-u1_3R->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.24197e-07,'m^3/(mol*s)'), n=3.47473, w0=(377500,'J/mol'), E0=(54197.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R-u1_3R->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 158,
    label = "Root_1R->H_3R-u1_3R->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.0131926,'m^3/(mol*s)'), n=2.28677, w0=(377500,'J/mol'), E0=(62877.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R-u1_3R->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_4R!H->Cl_Ext-3C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 159,
    label = "Root_1R->H_3R-u1_3R->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_Sp-4C-3C_Ext-3C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(2.12356e-06,'m^3/(mol*s)'), n=3.29547, w0=(377500,'J/mol'), E0=(61316.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R-u1_3R->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_Sp-4C-3C_Ext-3C-R_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_Sp-4C-3C_Ext-3C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_Sp-4C-3C_Ext-3C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_3R->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_Sp-4C-3C_Ext-3C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 160,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_Ext-1C-R_4R!H->C_5R!H->C",
    kinetics = ArrheniusBM(A=(58.4325,'m^3/(mol*s)'), n=1.86734, w0=(377500,'J/mol'), E0=(74737.5,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_Ext-1C-R_4R!H->C_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_Ext-1C-R_4R!H->C_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_Ext-1C-R_4R!H->C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_Ext-1C-R_4R!H->C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 161,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_Ext-1C-R_4R!H->C_N-5R!H->C",
    kinetics = ArrheniusBM(A=(93.458,'m^3/(mol*s)'), n=1.82649, w0=(377500,'J/mol'), E0=(79017.2,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_Ext-1C-R_4R!H->C_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_Ext-1C-R_4R!H->C_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_Ext-1C-R_4R!H->C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_Ext-1C-R_4R!H->C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 162,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_N-4R!H->O_N-4CCl->Cl_Ext-4C-R",
    kinetics = ArrheniusBM(A=(30.3495,'m^3/(mol*s)'), n=1.95189, w0=(377500,'J/mol'), E0=(78264.5,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_N-4R!H->O_N-4CCl->Cl_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_N-4R!H->O_N-4CCl->Cl_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_N-4R!H->O_N-4CCl->Cl_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Ext-1C-R_N-4R!H->O_N-4CCl->Cl_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 163,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_Sp-4C=1C",
    kinetics = ArrheniusBM(A=(4.90787e-05,'m^3/(mol*s)'), n=3.45028, w0=(327000,'J/mol'), E0=(64925.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.013000964180484608, var=0.03338634463104129, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_Sp-4C=1C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_Sp-4C=1C
    Total Standard Deviation in ln(k): 0.3989695403569997"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_Sp-4C=1C
Total Standard Deviation in ln(k): 0.3989695403569997""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_Sp-4C=1C
Total Standard Deviation in ln(k): 0.3989695403569997
""",
)

entry(
    index = 164,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C",
    kinetics = ArrheniusBM(A=(6.93262e-08,'m^3/(mol*s)'), n=4.04302, w0=(327000,'J/mol'), E0=(60839,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06143255375704523, var=2.3302287388512735, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C
    Total Standard Deviation in ln(k): 3.2145986394895028"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C
Total Standard Deviation in ln(k): 3.2145986394895028""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C
Total Standard Deviation in ln(k): 3.2145986394895028
""",
)

entry(
    index = 165,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C",
    kinetics = ArrheniusBM(A=(2.17974e+16,'m^3/(mol*s)'), n=-2.65597, w0=(299500,'J/mol'), E0=(80617.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2813784534603238, var=3.3110042297506896, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C
    Total Standard Deviation in ln(k): 4.354830076292993"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C
Total Standard Deviation in ln(k): 4.354830076292993""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C
Total Standard Deviation in ln(k): 4.354830076292993
""",
)

entry(
    index = 166,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_N-Sp-4C-1C",
    kinetics = ArrheniusBM(A=(58.5516,'m^3/(mol*s)'), n=1.69399, w0=(299500,'J/mol'), E0=(64762.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.006906506488055739, var=0.18040941691918894, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_N-Sp-4C-1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_N-Sp-4C-1C
    Total Standard Deviation in ln(k): 0.8688568322115681"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_N-Sp-4C-1C
Total Standard Deviation in ln(k): 0.8688568322115681""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_N-Sp-4C-1C
Total Standard Deviation in ln(k): 0.8688568322115681
""",
)

entry(
    index = 167,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_3CO->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.000180355,'m^3/(mol*s)'), n=3.19614, w0=(327000,'J/mol'), E0=(63605.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-8.435841376237718e-05, var=4.753282606147941, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_3CO->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_3CO->C_Ext-1C-R
    Total Standard Deviation in ln(k): 4.3709402294317625"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_3CO->C_Ext-1C-R
Total Standard Deviation in ln(k): 4.3709402294317625""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_3CO->C_Ext-1C-R
Total Standard Deviation in ln(k): 4.3709402294317625
""",
)

entry(
    index = 168,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_3CO->C_4ClO->O",
    kinetics = ArrheniusBM(A=(0.00435666,'m^3/(mol*s)'), n=2.88851, w0=(327000,'J/mol'), E0=(73122.8,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_3CO->C_4ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_3CO->C_4ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_3CO->C_4ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_3CO->C_4ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 169,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_3CO->C_N-4ClO->O",
    kinetics = ArrheniusBM(A=(0.00481462,'m^3/(mol*s)'), n=2.90966, w0=(327000,'J/mol'), E0=(78384.7,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_3CO->C_N-4ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_3CO->C_N-4ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_3CO->C_N-4ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_3CO->C_N-4ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 170,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_N-3CO->C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.53899e-06,'m^3/(mol*s)'), n=3.73484, w0=(299500,'J/mol'), E0=(25574.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.14947112916480124, var=0.5923858788672064, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_N-3CO->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_N-3CO->C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 1.9185321947968064"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_N-3CO->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 1.9185321947968064""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_N-3CO->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 1.9185321947968064
""",
)

entry(
    index = 171,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_3CO->C_Sp-4R!H-1C_4R!H->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3541.93,'m^3/(mol*s)'), n=1.13226, w0=(327000,'J/mol'), E0=(42355.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4922815922106995, var=0.0675906456998819, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_3CO->C_Sp-4R!H-1C_4R!H->O_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_3CO->C_Sp-4R!H-1C_4R!H->O_Ext-1C-R
    Total Standard Deviation in ln(k): 1.758083478257886"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_3CO->C_Sp-4R!H-1C_4R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 1.758083478257886""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_3CO->C_Sp-4R!H-1C_4R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 1.758083478257886
""",
)

entry(
    index = 172,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_3CO->C_Sp-4R!H-1C_N-4R!H->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.011895,'m^3/(mol*s)'), n=2.70774, w0=(327000,'J/mol'), E0=(88319.2,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_3CO->C_Sp-4R!H-1C_N-4R!H->O_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_3CO->C_Sp-4R!H-1C_N-4R!H->O_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_3CO->C_Sp-4R!H-1C_N-4R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_3CO->C_Sp-4R!H-1C_N-4R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 173,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_4R!H->O_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.19448e-05,'m^3/(mol*s)'), n=3.35979, w0=(327000,'J/mol'), E0=(61032.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_4R!H->O_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_4R!H->O_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_4R!H->O_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_4R!H->O_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 174,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_Sp-5R!H-3C",
    kinetics = ArrheniusBM(A=(2.14885e-10,'m^3/(mol*s)'), n=4.53717, w0=(327000,'J/mol'), E0=(61369.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.023909381712312647, var=4.119613499066051, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_Sp-5R!H-3C',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_Sp-5R!H-3C
    Total Standard Deviation in ln(k): 4.129050736204372"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_Sp-5R!H-3C
Total Standard Deviation in ln(k): 4.129050736204372""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_Sp-5R!H-3C
Total Standard Deviation in ln(k): 4.129050736204372
""",
)

entry(
    index = 175,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_N-Sp-5R!H-3C",
    kinetics = ArrheniusBM(A=(1.73666e-32,'m^3/(mol*s)'), n=11.6472, w0=(327000,'J/mol'), E0=(4450.14,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.017464998513887633, var=21.402209566809915, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_N-Sp-5R!H-3C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_N-Sp-5R!H-3C
    Total Standard Deviation in ln(k): 9.318292000267084"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_N-Sp-5R!H-3C
Total Standard Deviation in ln(k): 9.318292000267084""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_N-Sp-5R!H-3C
Total Standard Deviation in ln(k): 9.318292000267084
""",
)

entry(
    index = 176,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_4CCl->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(0.000264463,'m^3/(mol*s)'), n=3.15013, w0=(327000,'J/mol'), E0=(76570.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-4.036116064440243e-06, var=2.9704956582455386, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_4CCl->C_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_4CCl->C_Ext-4C-R
    Total Standard Deviation in ln(k): 3.455196292522036"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_4CCl->C_Ext-4C-R
Total Standard Deviation in ln(k): 3.455196292522036""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_4CCl->C_Ext-4C-R
Total Standard Deviation in ln(k): 3.455196292522036
""",
)

entry(
    index = 177,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-4R!H-R_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.02032e-06,'m^3/(mol*s)'), n=3.25872, w0=(299500,'J/mol'), E0=(38107.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0017978332384043748, var=4.329654512535134, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-4R!H-R_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-4R!H-R_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 4.1759342089846685"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-4R!H-R_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 4.1759342089846685""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-4R!H-R_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 4.1759342089846685
""",
)

entry(
    index = 178,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-4R!H-R_Ext-3C-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(6.25964e-08,'m^3/(mol*s)'), n=4.02374, w0=(299500,'J/mol'), E0=(23063.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-4R!H-R_Ext-3C-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-4R!H-R_Ext-3C-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-4R!H-R_Ext-3C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-4R!H-R_Ext-3C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 179,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R_N-4R!H->C_4ClO->O",
    kinetics = ArrheniusBM(A=(6.20565e-06,'m^3/(mol*s)'), n=3.17637, w0=(299500,'J/mol'), E0=(23479.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R_N-4R!H->C_4ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R_N-4R!H->C_4ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R_N-4R!H->C_4ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R_N-4R!H->C_4ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 180,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R_N-4R!H->C_N-4ClO->O",
    kinetics = ArrheniusBM(A=(1.40268e-05,'m^3/(mol*s)'), n=3.33679, w0=(299500,'J/mol'), E0=(41196.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R_N-4R!H->C_N-4ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R_N-4R!H->C_N-4ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R_N-4R!H->C_N-4ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R_N-4R!H->C_N-4ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 181,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(0.384772,'m^3/(mol*s)'), n=1.64465, w0=(299500,'J/mol'), E0=(68154.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.02391923251975329, var=9.405515034642969, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R_4R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R_4R!H->C
    Total Standard Deviation in ln(k): 6.208302733574154"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 6.208302733574154""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 6.208302733574154
""",
)

entry(
    index = 182,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(4.61982,'m^3/(mol*s)'), n=1.59815, w0=(299500,'J/mol'), E0=(48938,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 183,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(0.000430651,'m^3/(mol*s)'), n=2.78666, w0=(299500,'J/mol'), E0=(58984,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 184,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_1O-u0",
    kinetics = ArrheniusBM(A=(8.86035e-05,'m^3/(mol*s)'), n=3.31017, w0=(272000,'J/mol'), E0=(27200,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_1O-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_1O-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_1O-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_1O-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 185,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-1O-u0",
    kinetics = ArrheniusBM(A=(6.08473,'m^3/(mol*s)'), n=1.89139, w0=(272000,'J/mol'), E0=(27200,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-1O-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-1O-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-1O-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_N-3CO->C_Ext-3O-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-1O-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 186,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_Sp-4C=1C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(0.0141769,'m^3/(mol*s)'), n=2.76355, w0=(327000,'J/mol'), E0=(72170.8,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_Sp-4C=1C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_Sp-4C=1C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_Sp-4C=1C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_Sp-4C=1C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 187,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_Sp-4C=1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.00717719,'m^3/(mol*s)'), n=2.80408, w0=(327000,'J/mol'), E0=(70434.6,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_Sp-4C=1C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_Sp-4C=1C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_Sp-4C=1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_Sp-4C=1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 188,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.41162e-07,'m^3/(mol*s)'), n=3.77879, w0=(327000,'J/mol'), E0=(59363.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.052764355405467825, var=2.735633848082593, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-1C-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-1C-R
    Total Standard Deviation in ln(k): 3.4483557887118437"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-1C-R
Total Standard Deviation in ln(k): 3.4483557887118437""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-1C-R
Total Standard Deviation in ln(k): 3.4483557887118437
""",
)

entry(
    index = 189,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(0.000540685,'m^3/(mol*s)'), n=3.17235, w0=(327000,'J/mol'), E0=(74063.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.3393611685421646e-06, var=0.44730157612620847, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-4C-R
    Total Standard Deviation in ln(k): 1.3407823789970164"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-4C-R
Total Standard Deviation in ln(k): 1.3407823789970164""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-4C-R
Total Standard Deviation in ln(k): 1.3407823789970164
""",
)

entry(
    index = 190,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.30531e+17,'m^3/(mol*s)'), n=-2.95925, w0=(299500,'J/mol'), E0=(82637.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2600713415997352, var=6.313083847640051, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 5.690513052015321"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 5.690513052015321""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 5.690513052015321
""",
)

entry(
    index = 191,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_3O-u1",
    kinetics = ArrheniusBM(A=(109.001,'m^3/(mol*s)'), n=1.60095, w0=(299500,'J/mol'), E0=(38565.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06269940954337926, var=1.4403697668649784, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_3O-u1',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_3O-u1
    Total Standard Deviation in ln(k): 2.5635271465156366"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_3O-u1
Total Standard Deviation in ln(k): 2.5635271465156366""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_3O-u1
Total Standard Deviation in ln(k): 2.5635271465156366
""",
)

entry(
    index = 192,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_N-3O-u1",
    kinetics = ArrheniusBM(A=(1.17816e+08,'m^3/(mol*s)'), n=-0.0692414, w0=(299500,'J/mol'), E0=(67611.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.04773849353497379, var=6.57109927584427, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_N-3O-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_N-3O-u1
    Total Standard Deviation in ln(k): 5.258915032278341"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_N-3O-u1
Total Standard Deviation in ln(k): 5.258915032278341""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_N-3O-u1
Total Standard Deviation in ln(k): 5.258915032278341
""",
)

entry(
    index = 193,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_N-Sp-4C-1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(71.082,'m^3/(mol*s)'), n=1.78047, w0=(299500,'J/mol'), E0=(70716,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_N-Sp-4C-1C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_N-Sp-4C-1C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_N-Sp-4C-1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_N-Sp-4C-1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 194,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_3CO->C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.0117959,'m^3/(mol*s)'), n=2.7472, w0=(327000,'J/mol'), E0=(66187.2,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_3CO->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_3CO->C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_3CO->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_3CO->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 195,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_N-3CO->C_Ext-1C-R_Ext-1C-R_4ClO->O",
    kinetics = ArrheniusBM(A=(4.6039e-06,'m^3/(mol*s)'), n=3.72431, w0=(299500,'J/mol'), E0=(8896.16,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.04881028998692721, var=1.9120057645917468, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_N-3CO->C_Ext-1C-R_Ext-1C-R_4ClO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_N-3CO->C_Ext-1C-R_Ext-1C-R_4ClO->O
    Total Standard Deviation in ln(k): 2.894692293593372"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_N-3CO->C_Ext-1C-R_Ext-1C-R_4ClO->O
Total Standard Deviation in ln(k): 2.894692293593372""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_N-3CO->C_Ext-1C-R_Ext-1C-R_4ClO->O
Total Standard Deviation in ln(k): 2.894692293593372
""",
)

entry(
    index = 196,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_N-3CO->C_Ext-1C-R_Ext-1C-R_N-4ClO->O",
    kinetics = ArrheniusBM(A=(1.58515,'m^3/(mol*s)'), n=2.35936, w0=(299500,'J/mol'), E0=(50053.5,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_N-3CO->C_Ext-1C-R_Ext-1C-R_N-4ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_N-3CO->C_Ext-1C-R_Ext-1C-R_N-4ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_N-3CO->C_Ext-1C-R_Ext-1C-R_N-4ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_N-3CO->C_Ext-1C-R_Ext-1C-R_N-4ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 197,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_3CO->C_Sp-4R!H-1C_4R!H->O_Ext-1C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(0.0111464,'m^3/(mol*s)'), n=2.7136, w0=(327000,'J/mol'), E0=(23557.8,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_3CO->C_Sp-4R!H-1C_4R!H->O_Ext-1C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_3CO->C_Sp-4R!H-1C_4R!H->O_Ext-1C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_3CO->C_Sp-4R!H-1C_4R!H->O_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_3CO->C_Sp-4R!H-1C_4R!H->O_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 198,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_3CO->C_Sp-4R!H-1C_4R!H->O_Ext-1C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.0343304,'m^3/(mol*s)'), n=2.71102, w0=(327000,'J/mol'), E0=(39616.9,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_3CO->C_Sp-4R!H-1C_4R!H->O_Ext-1C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_3CO->C_Sp-4R!H-1C_4R!H->O_Ext-1C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_3CO->C_Sp-4R!H-1C_4R!H->O_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_N-1C-u0_3CO->C_Sp-4R!H-1C_4R!H->O_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 199,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_Sp-5R!H-3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(7.49201e-05,'m^3/(mol*s)'), n=2.60384, w0=(327000,'J/mol'), E0=(70755.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00010750672861105423, var=0.12129732964652548, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_Sp-5R!H-3C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_Sp-5R!H-3C_Ext-3C-R
    Total Standard Deviation in ln(k): 0.6984745625123947"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_Sp-5R!H-3C_Ext-3C-R
Total Standard Deviation in ln(k): 0.6984745625123947""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_Sp-5R!H-3C_Ext-3C-R
Total Standard Deviation in ln(k): 0.6984745625123947
""",
)

entry(
    index = 200,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_Sp-5R!H-3C_4CCl->Cl",
    kinetics = ArrheniusBM(A=(0.000111183,'m^3/(mol*s)'), n=3.16652, w0=(327000,'J/mol'), E0=(75191.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=7.183951665994539e-05, var=0.016449742049074328, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_Sp-5R!H-3C_4CCl->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_Sp-5R!H-3C_4CCl->Cl
    Total Standard Deviation in ln(k): 0.257300901543114"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_Sp-5R!H-3C_4CCl->Cl
Total Standard Deviation in ln(k): 0.257300901543114""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_Sp-5R!H-3C_4CCl->Cl
Total Standard Deviation in ln(k): 0.257300901543114
""",
)

entry(
    index = 201,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_Sp-5R!H-3C_N-4CCl->Cl",
    kinetics = ArrheniusBM(A=(5.62698e-06,'m^3/(mol*s)'), n=3.21493, w0=(327000,'J/mol'), E0=(70401.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.005705107791341785, var=4.244091596417956, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_Sp-5R!H-3C_N-4CCl->Cl',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_Sp-5R!H-3C_N-4CCl->Cl
    Total Standard Deviation in ln(k): 4.144327898216506"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_Sp-5R!H-3C_N-4CCl->Cl
Total Standard Deviation in ln(k): 4.144327898216506""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_Sp-5R!H-3C_N-4CCl->Cl
Total Standard Deviation in ln(k): 4.144327898216506
""",
)

entry(
    index = 202,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_N-Sp-5R!H-3C_4CCl->C",
    kinetics = ArrheniusBM(A=(0.000183421,'m^3/(mol*s)'), n=3.08609, w0=(327000,'J/mol'), E0=(67923.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_N-Sp-5R!H-3C_4CCl->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_N-Sp-5R!H-3C_4CCl->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_N-Sp-5R!H-3C_4CCl->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_N-Sp-5R!H-3C_4CCl->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 203,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_N-Sp-5R!H-3C_N-4CCl->C",
    kinetics = ArrheniusBM(A=(4.78552e-08,'m^3/(mol*s)'), n=4.56733, w0=(327000,'J/mol'), E0=(57012.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_N-Sp-5R!H-3C_N-4CCl->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_N-Sp-5R!H-3C_N-4CCl->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_N-Sp-5R!H-3C_N-4CCl->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_N-Sp-5R!H-3C_N-4CCl->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 204,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_4CCl->C_Ext-4C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(5.76571e-05,'m^3/(mol*s)'), n=3.24279, w0=(327000,'J/mol'), E0=(74347.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_4CCl->C_Ext-4C-R_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_4CCl->C_Ext-4C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_4CCl->C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_4CCl->C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 205,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-4R!H-R_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(4.36525e-10,'m^3/(mol*s)'), n=4.21502, w0=(299500,'J/mol'), E0=(25416.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-4R!H-R_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-4R!H-R_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-4R!H-R_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_1O-u0_Ext-3C-R_Ext-4R!H-R_Ext-3C-R_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 206,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R_4R!H->C_Ext-4C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(0.000685288,'m^3/(mol*s)'), n=2.02041, w0=(299500,'J/mol'), E0=(56243.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R_4R!H->C_Ext-4C-R_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R_4R!H->C_Ext-4C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R_4R!H->C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R_4R!H->C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 207,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R_4R!H->C_5R!H->C",
    kinetics = ArrheniusBM(A=(0.00106635,'m^3/(mol*s)'), n=2.59522, w0=(299500,'J/mol'), E0=(60401.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R_4R!H->C_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R_4R!H->C_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R_4R!H->C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R_4R!H->C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 208,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R_4R!H->C_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.000753617,'m^3/(mol*s)'), n=2.43038, w0=(299500,'J/mol'), E0=(55678.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R_4R!H->C_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R_4R!H->C_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R_4R!H->C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_3CO-u1_3CO->C_N-1O-u0_Ext-3C-R_Ext-3C-R_Ext-3C-R_4R!H->C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 209,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-1C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.44612e-07,'m^3/(mol*s)'), n=3.7257, w0=(327000,'J/mol'), E0=(57472.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0532074470433294, var=3.1661268761279766, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-1C-R_5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-1C-R_5R!H->C
    Total Standard Deviation in ln(k): 3.700835201646697"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 3.700835201646697""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 3.700835201646697
""",
)

entry(
    index = 210,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-1C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(3.26007e-09,'m^3/(mol*s)'), n=4.48991, w0=(327000,'J/mol'), E0=(57424.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05218656740273962, var=3.350691244395083, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-1C-R_N-5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-1C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 3.8007682285925393"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 3.8007682285925393""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 3.8007682285925393
""",
)

entry(
    index = 211,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-4C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(0.00283994,'m^3/(mol*s)'), n=2.94646, w0=(327000,'J/mol'), E0=(76799.7,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-4C-R_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-4C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 212,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(4.89453e+09,'m^3/(mol*s)'), n=-0.85018, w0=(299500,'J/mol'), E0=(68542.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.16834240070023365, var=2.6891432174839043, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 3.710457185757045"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 3.710457185757045""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 3.710457185757045
""",
)

entry(
    index = 213,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_Ext-1C-R_Ext-1C-R_3O-u1",
    kinetics = ArrheniusBM(A=(1.57952,'m^3/(mol*s)'), n=2.43229, w0=(299500,'J/mol'), E0=(29816.2,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_Ext-1C-R_Ext-1C-R_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_Ext-1C-R_Ext-1C-R_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_Ext-1C-R_Ext-1C-R_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_Ext-1C-R_Ext-1C-R_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 214,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_Ext-1C-R_Ext-1C-R_N-3O-u1",
    kinetics = ArrheniusBM(A=(63.0113,'m^3/(mol*s)'), n=1.7261, w0=(299500,'J/mol'), E0=(64775.3,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_Ext-1C-R_Ext-1C-R_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_Ext-1C-R_Ext-1C-R_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_Ext-1C-R_Ext-1C-R_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_Ext-1C-R_Ext-1C-R_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 215,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_3O-u1_Ext-4C-R",
    kinetics = ArrheniusBM(A=(3165.55,'m^3/(mol*s)'), n=1.12762, w0=(299500,'J/mol'), E0=(42583,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.008374178295341254, var=3.5739804111790336, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_3O-u1_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_3O-u1_Ext-4C-R
    Total Standard Deviation in ln(k): 3.8109870961232257"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_3O-u1_Ext-4C-R
Total Standard Deviation in ln(k): 3.8109870961232257""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_3O-u1_Ext-4C-R
Total Standard Deviation in ln(k): 3.8109870961232257
""",
)

entry(
    index = 216,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_N-3O-u1_Ext-4C-R",
    kinetics = ArrheniusBM(A=(48.9307,'m^3/(mol*s)'), n=1.947, w0=(299500,'J/mol'), E0=(69755.5,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_N-3O-u1_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_N-3O-u1_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_N-3O-u1_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_N-3O-u1_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 217,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_N-3CO->C_Ext-1C-R_Ext-1C-R_4ClO->O_3O-u1",
    kinetics = ArrheniusBM(A=(0.157359,'m^3/(mol*s)'), n=2.34331, w0=(299500,'J/mol'), E0=(34188.8,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_N-3CO->C_Ext-1C-R_Ext-1C-R_4ClO->O_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_N-3CO->C_Ext-1C-R_Ext-1C-R_4ClO->O_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_N-3CO->C_Ext-1C-R_Ext-1C-R_4ClO->O_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_N-3CO->C_Ext-1C-R_Ext-1C-R_4ClO->O_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 218,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_N-3CO->C_Ext-1C-R_Ext-1C-R_4ClO->O_N-3O-u1",
    kinetics = ArrheniusBM(A=(290.458,'m^3/(mol*s)'), n=1.65322, w0=(299500,'J/mol'), E0=(51387.3,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_N-3CO->C_Ext-1C-R_Ext-1C-R_4ClO->O_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_N-3CO->C_Ext-1C-R_Ext-1C-R_4ClO->O_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_N-3CO->C_Ext-1C-R_Ext-1C-R_4ClO->O_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_N-4R!H->C_N-3CO->C_Ext-1C-R_Ext-1C-R_4ClO->O_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 219,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_Sp-5R!H-3C_Ext-3C-R_Ext-4CCl-R",
    kinetics = ArrheniusBM(A=(1.55759e-07,'m^3/(mol*s)'), n=3.32068, w0=(327000,'J/mol'), E0=(59143,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_Sp-5R!H-3C_Ext-3C-R_Ext-4CCl-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_Sp-5R!H-3C_Ext-3C-R_Ext-4CCl-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_Sp-5R!H-3C_Ext-3C-R_Ext-4CCl-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_Sp-5R!H-3C_Ext-3C-R_Ext-4CCl-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 220,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_Sp-5R!H-3C_4CCl->Cl_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(3.26481e-07,'m^3/(mol*s)'), n=3.88187, w0=(327000,'J/mol'), E0=(67376.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_Sp-5R!H-3C_4CCl->Cl_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_Sp-5R!H-3C_4CCl->Cl_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_Sp-5R!H-3C_4CCl->Cl_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_Sp-5R!H-3C_4CCl->Cl_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 221,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_Sp-5R!H-3C_N-4CCl->Cl_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(5.29533e-07,'m^3/(mol*s)'), n=3.59832, w0=(327000,'J/mol'), E0=(71695.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0004062628939296235, var=14.496820689555761, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_Sp-5R!H-3C_N-4CCl->Cl_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_Sp-5R!H-3C_N-4CCl->Cl_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 7.633987554008899"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_Sp-5R!H-3C_N-4CCl->Cl_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 7.633987554008899""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_Sp-5R!H-3C_N-4CCl->Cl_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 7.633987554008899
""",
)

entry(
    index = 222,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-1C-R_5R!H->C_Ext-5C-R_Ext-5C-R",
    kinetics = ArrheniusBM(A=(7.48969e-09,'m^3/(mol*s)'), n=4.13298, w0=(327000,'J/mol'), E0=(56539.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.02774793073627493, var=5.992340363567137, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-1C-R_5R!H->C_Ext-5C-R_Ext-5C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-1C-R_5R!H->C_Ext-5C-R_Ext-5C-R
    Total Standard Deviation in ln(k): 4.977160990158553"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-1C-R_5R!H->C_Ext-5C-R_Ext-5C-R
Total Standard Deviation in ln(k): 4.977160990158553""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-1C-R_5R!H->C_Ext-5C-R_Ext-5C-R
Total Standard Deviation in ln(k): 4.977160990158553
""",
)

entry(
    index = 223,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-1C-R_N-5R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.602197,'m^3/(mol*s)'), n=1.79841, w0=(327000,'J/mol'), E0=(72113.9,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-1C-R_N-5R!H->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-1C-R_N-5R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-1C-R_N-5R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-1C-R_N-5R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 224,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-1C-R_N-5R!H->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(0.0056062,'m^3/(mol*s)'), n=2.84217, w0=(327000,'J/mol'), E0=(76231.1,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-1C-R_N-5R!H->C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-1C-R_N-5R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-1C-R_N-5R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-1C-R_N-5R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 225,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.68906e+11,'m^3/(mol*s)'), n=-1.42097, w0=(299500,'J/mol'), E0=(68353.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.5316007770156629, var=7.77830872230957, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 6.9268101819187935"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 6.9268101819187935""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 6.9268101819187935
""",
)

entry(
    index = 226,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_3O-u1_Ext-4C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(0.186883,'m^3/(mol*s)'), n=2.60235, w0=(299500,'J/mol'), E0=(41199.9,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_3O-u1_Ext-4C-R_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_3O-u1_Ext-4C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_3O-u1_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_3O-u1_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 227,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_Sp-5R!H-3C_N-4CCl->Cl_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(3.85859e-07,'m^3/(mol*s)'), n=3.30296, w0=(327000,'J/mol'), E0=(63102.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_Sp-5R!H-3C_N-4CCl->Cl_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_Sp-5R!H-3C_N-4CCl->Cl_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_Sp-5R!H-3C_N-4CCl->Cl_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3CO-u1_Ext-3CO-R_Sp-4R!H-3CO_3CO->C_N-4R!H->O_Ext-3C-R_Sp-5R!H-3C_N-4CCl->Cl_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 228,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-1C-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R",
    kinetics = ArrheniusBM(A=(0.21039,'m^3/(mol*s)'), n=1.87409, w0=(327000,'J/mol'), E0=(75354.4,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-1C-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-1C-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-1C-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-1C-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 229,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-1C-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.168083,'m^3/(mol*s)'), n=1.8024, w0=(327000,'J/mol'), E0=(72414.8,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-1C-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-1C-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-1C-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_3CO->C_N-Sp-4C=1C_Ext-1C-R_5R!H->C_Ext-5C-R_Ext-5C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 230,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(3.57521e+12,'m^3/(mol*s)'), n=-1.76616, w0=(299500,'J/mol'), E0=(72858.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.09394774172035059, var=16.293133926427753, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 8.328113493182295"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 8.328113493182295""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 8.328113493182295
""",
)

entry(
    index = 231,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_3O-u1",
    kinetics = ArrheniusBM(A=(0.211482,'m^3/(mol*s)'), n=2.3853, w0=(299500,'J/mol'), E0=(45837.1,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 232,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-3O-u1",
    kinetics = ArrheniusBM(A=(12635,'m^3/(mol*s)'), n=0.772422, w0=(299500,'J/mol'), E0=(69890.2,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_Ext-1C-R_1C-u0_N-Sp-4R!H#1C_4R!H->C_N-3CO->C_Sp-4C-1C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

