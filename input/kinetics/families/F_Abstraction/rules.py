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
    kinetics = ArrheniusBM(A=(1.02719e-06,'m^3/(mol*s)'), n=3.84148, w0=(415008,'J/mol'), E0=(11495.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3337430748393336, var=28.33116194752585, Tref=1000.0, N=133, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 133 training reactions at node Root
    Total Standard Deviation in ln(k): 11.509158855867998"""),
    rank = 11,
    shortDesc = """BM rule fitted to 133 training reactions at node Root
Total Standard Deviation in ln(k): 11.509158855867998""",
    longDesc = 
"""
BM rule fitted to 133 training reactions at node Root
Total Standard Deviation in ln(k): 11.509158855867998
""",
)

entry(
    index = 2,
    label = "Root_3R->O",
    kinetics = ArrheniusBM(A=(7.67831,'m^3/(mol*s)'), n=2.16114, w0=(330803,'J/mol'), E0=(127585,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.029445622959475587, var=8.23388710674406, Tref=1000.0, N=33, data_mean=0.0, correlation='Root_3R->O',), comment="""BM rule fitted to 33 training reactions at node Root_3R->O
    Total Standard Deviation in ln(k): 5.826521279157448"""),
    rank = 11,
    shortDesc = """BM rule fitted to 33 training reactions at node Root_3R->O
Total Standard Deviation in ln(k): 5.826521279157448""",
    longDesc = 
"""
BM rule fitted to 33 training reactions at node Root_3R->O
Total Standard Deviation in ln(k): 5.826521279157448
""",
)

entry(
    index = 3,
    label = "Root_N-3R->O",
    kinetics = ArrheniusBM(A=(0.000144148,'m^3/(mol*s)'), n=3.1307, w0=(442795,'J/mol'), E0=(-4331.02,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4307289914915006, var=28.104324660617046, Tref=1000.0, N=100, data_mean=0.0, correlation='Root_N-3R->O',), comment="""BM rule fitted to 100 training reactions at node Root_N-3R->O
    Total Standard Deviation in ln(k): 11.710038376909473"""),
    rank = 11,
    shortDesc = """BM rule fitted to 100 training reactions at node Root_N-3R->O
Total Standard Deviation in ln(k): 11.710038376909473""",
    longDesc = 
"""
BM rule fitted to 100 training reactions at node Root_N-3R->O
Total Standard Deviation in ln(k): 11.710038376909473
""",
)

entry(
    index = 4,
    label = "Root_3R->O_1R->O",
    kinetics = ArrheniusBM(A=(1.57248e+58,'m^3/(mol*s)'), n=-14.8465, w0=(222000,'J/mol'), E0=(237010,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.7953720767048976, var=9.868724280704338, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_3R->O_1R->O',), comment="""BM rule fitted to 6 training reactions at node Root_3R->O_1R->O
    Total Standard Deviation in ln(k): 8.29620247426518"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_3R->O_1R->O
Total Standard Deviation in ln(k): 8.29620247426518""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_3R->O_1R->O
Total Standard Deviation in ln(k): 8.29620247426518
""",
)

entry(
    index = 5,
    label = "Root_3R->O_N-1R->O",
    kinetics = ArrheniusBM(A=(1.48961e-13,'m^3/(mol*s)'), n=6.22486, w0=(354981,'J/mol'), E0=(35498.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1836186126144488, var=9.63859920420745, Tref=1000.0, N=27, data_mean=0.0, correlation='Root_3R->O_N-1R->O',), comment="""BM rule fitted to 27 training reactions at node Root_3R->O_N-1R->O
    Total Standard Deviation in ln(k): 6.68527255973498"""),
    rank = 11,
    shortDesc = """BM rule fitted to 27 training reactions at node Root_3R->O_N-1R->O
Total Standard Deviation in ln(k): 6.68527255973498""",
    longDesc = 
"""
BM rule fitted to 27 training reactions at node Root_3R->O_N-1R->O
Total Standard Deviation in ln(k): 6.68527255973498
""",
)

entry(
    index = 6,
    label = "Root_N-3R->O_3BrCClFHINPSSi->F",
    kinetics = ArrheniusBM(A=(99579.1,'m^3/(mol*s)'), n=0.724062, w0=(331429,'J/mol'), E0=(33142.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04379986295924776, var=1.9018195251207486, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-3R->O_3BrCClFHINPSSi->F',), comment="""BM rule fitted to 7 training reactions at node Root_N-3R->O_3BrCClFHINPSSi->F
    Total Standard Deviation in ln(k): 2.8747093419560272"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-3R->O_3BrCClFHINPSSi->F
Total Standard Deviation in ln(k): 2.8747093419560272""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-3R->O_3BrCClFHINPSSi->F
Total Standard Deviation in ln(k): 2.8747093419560272
""",
)

entry(
    index = 7,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F",
    kinetics = ArrheniusBM(A=(3.15256e-08,'m^3/(mol*s)'), n=4.26345, w0=(451178,'J/mol'), E0=(-11469.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.44750898004232315, var=27.78153838108212, Tref=1000.0, N=93, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F',), comment="""BM rule fitted to 93 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F
    Total Standard Deviation in ln(k): 11.690991194616311"""),
    rank = 11,
    shortDesc = """BM rule fitted to 93 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F
Total Standard Deviation in ln(k): 11.690991194616311""",
    longDesc = 
"""
BM rule fitted to 93 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F
Total Standard Deviation in ln(k): 11.690991194616311
""",
)

entry(
    index = 8,
    label = "Root_3R->O_1R->O_Ext-1O-R",
    kinetics = ArrheniusBM(A=(9.50684e+53,'m^3/(mol*s)'), n=-13.5934, w0=(222000,'J/mol'), E0=(225074,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.08753785633515945, var=28.008039755476897, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3R->O_1R->O_Ext-1O-R',), comment="""BM rule fitted to 3 training reactions at node Root_3R->O_1R->O_Ext-1O-R
    Total Standard Deviation in ln(k): 10.829528140188767"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3R->O_1R->O_Ext-1O-R
Total Standard Deviation in ln(k): 10.829528140188767""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3R->O_1R->O_Ext-1O-R
Total Standard Deviation in ln(k): 10.829528140188767
""",
)

entry(
    index = 9,
    label = "Root_3R->O_1R->O_1O-u0",
    kinetics = ArrheniusBM(A=(2.99935e-05,'m^3/(mol*s)'), n=4.01289, w0=(222000,'J/mol'), E0=(22200,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->O_1R->O_1O-u0',), comment="""BM rule fitted to 1 training reactions at node Root_3R->O_1R->O_1O-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->O_1R->O_1O-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->O_1R->O_1O-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_3R->O_1R->O_N-1O-u0",
    kinetics = ArrheniusBM(A=(0.329575,'m^3/(mol*s)'), n=2.30206, w0=(222000,'J/mol'), E0=(120704,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03713926538722931, var=0.10946379467839873, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->O_1R->O_N-1O-u0',), comment="""BM rule fitted to 2 training reactions at node Root_3R->O_1R->O_N-1O-u0
    Total Standard Deviation in ln(k): 0.7565876155043457"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->O_1R->O_N-1O-u0
Total Standard Deviation in ln(k): 0.7565876155043457""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->O_1R->O_N-1O-u0
Total Standard Deviation in ln(k): 0.7565876155043457
""",
)

entry(
    index = 11,
    label = "Root_3R->O_N-1R->O_Ext-3O-R",
    kinetics = ArrheniusBM(A=(7.85194e-13,'m^3/(mol*s)'), n=6.06209, w0=(357500,'J/mol'), E0=(35750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.16074316316349985, var=8.628793435899286, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_3R->O_N-1R->O_Ext-3O-R',), comment="""BM rule fitted to 10 training reactions at node Root_3R->O_N-1R->O_Ext-3O-R
    Total Standard Deviation in ln(k): 6.292748088375004"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_3R->O_N-1R->O_Ext-3O-R
Total Standard Deviation in ln(k): 6.292748088375004""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_3R->O_N-1R->O_Ext-3O-R
Total Standard Deviation in ln(k): 6.292748088375004
""",
)

entry(
    index = 12,
    label = "Root_3R->O_N-1R->O_1CClFH-u0",
    kinetics = ArrheniusBM(A=(1.26046e-20,'m^3/(mol*s)'), n=8.3455, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2995915999813187, var=8.694185717042204, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_3R->O_N-1R->O_1CClFH-u0',), comment="""BM rule fitted to 10 training reactions at node Root_3R->O_N-1R->O_1CClFH-u0
    Total Standard Deviation in ln(k): 6.663885443073088"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_3R->O_N-1R->O_1CClFH-u0
Total Standard Deviation in ln(k): 6.663885443073088""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_3R->O_N-1R->O_1CClFH-u0
Total Standard Deviation in ln(k): 6.663885443073088
""",
)

entry(
    index = 13,
    label = "Root_3R->O_N-1R->O_N-1CClFH-u0",
    kinetics = ArrheniusBM(A=(0.00017596,'m^3/(mol*s)'), n=3.42792, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05062213063070171, var=15.23029460788162, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_3R->O_N-1R->O_N-1CClFH-u0',), comment="""BM rule fitted to 7 training reactions at node Root_3R->O_N-1R->O_N-1CClFH-u0
    Total Standard Deviation in ln(k): 7.9508724117274845"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_3R->O_N-1R->O_N-1CClFH-u0
Total Standard Deviation in ln(k): 7.9508724117274845""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_3R->O_N-1R->O_N-1CClFH-u0
Total Standard Deviation in ln(k): 7.9508724117274845
""",
)

entry(
    index = 14,
    label = "Root_N-3R->O_3BrCClFHINPSSi->F_1R->C",
    kinetics = ArrheniusBM(A=(3.10961e+07,'m^3/(mol*s)'), n=-0.0368145, w0=(320000,'J/mol'), E0=(32000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.03634542142796184, var=1.5901699299407757, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->O_3BrCClFHINPSSi->F_1R->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->O_3BrCClFHINPSSi->F_1R->C
    Total Standard Deviation in ln(k): 2.6193299809935144"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->O_3BrCClFHINPSSi->F_1R->C
Total Standard Deviation in ln(k): 2.6193299809935144""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->O_3BrCClFHINPSSi->F_1R->C
Total Standard Deviation in ln(k): 2.6193299809935144
""",
)

entry(
    index = 15,
    label = "Root_N-3R->O_3BrCClFHINPSSi->F_N-1R->C",
    kinetics = ArrheniusBM(A=(0.0577854,'m^3/(mol*s)'), n=2.62625, w0=(360000,'J/mol'), E0=(36000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.3854301666465253, var=0.9609060278365511, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_3BrCClFHINPSSi->F_N-1R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_3BrCClFHINPSSi->F_N-1R->C
    Total Standard Deviation in ln(k): 2.933575389249798"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_3BrCClFHINPSSi->F_N-1R->C
Total Standard Deviation in ln(k): 2.933575389249798""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_3BrCClFHINPSSi->F_N-1R->C
Total Standard Deviation in ln(k): 2.933575389249798
""",
)

entry(
    index = 16,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O",
    kinetics = ArrheniusBM(A=(1.26567e-17,'m^3/(mol*s)'), n=7.12681, w0=(355167,'J/mol'), E0=(35516.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.21668081676615528, var=10.522747283182838, Tref=1000.0, N=24, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O',), comment="""BM rule fitted to 24 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O
    Total Standard Deviation in ln(k): 7.047541042652431"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O
Total Standard Deviation in ln(k): 7.047541042652431""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O
Total Standard Deviation in ln(k): 7.047541042652431
""",
)

entry(
    index = 17,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O",
    kinetics = ArrheniusBM(A=(7.03279e-07,'m^3/(mol*s)'), n=3.80319, w0=(484573,'J/mol'), E0=(-11771.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.24764870831551716, var=29.448384555504756, Tref=1000.0, N=69, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O',), comment="""BM rule fitted to 69 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O
    Total Standard Deviation in ln(k): 11.501201636727302"""),
    rank = 11,
    shortDesc = """BM rule fitted to 69 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O
Total Standard Deviation in ln(k): 11.501201636727302""",
    longDesc = 
"""
BM rule fitted to 69 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O
Total Standard Deviation in ln(k): 11.501201636727302
""",
)

entry(
    index = 18,
    label = "Root_3R->O_1R->O_Ext-1O-R_3O-u1",
    kinetics = ArrheniusBM(A=(0.0487535,'m^3/(mol*s)'), n=3.06244, w0=(222000,'J/mol'), E0=(22200,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->O_1R->O_Ext-1O-R_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_3R->O_1R->O_Ext-1O-R_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->O_1R->O_Ext-1O-R_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->O_1R->O_Ext-1O-R_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_3R->O_1R->O_Ext-1O-R_N-3O-u1",
    kinetics = ArrheniusBM(A=(6.52723,'m^3/(mol*s)'), n=1.98959, w0=(222000,'J/mol'), E0=(118211,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.02935573976520705, var=0.14075700629316643, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->O_1R->O_Ext-1O-R_N-3O-u1',), comment="""BM rule fitted to 2 training reactions at node Root_3R->O_1R->O_Ext-1O-R_N-3O-u1
    Total Standard Deviation in ln(k): 0.8258865615642318"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->O_1R->O_Ext-1O-R_N-3O-u1
Total Standard Deviation in ln(k): 0.8258865615642318""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->O_1R->O_Ext-1O-R_N-3O-u1
Total Standard Deviation in ln(k): 0.8258865615642318
""",
)

entry(
    index = 20,
    label = "Root_3R->O_1R->O_N-1O-u0_Ext-3O-R_4R!H->C",
    kinetics = ArrheniusBM(A=(0.0552802,'m^3/(mol*s)'), n=2.52847, w0=(222000,'J/mol'), E0=(119820,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->O_1R->O_N-1O-u0_Ext-3O-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->O_1R->O_N-1O-u0_Ext-3O-R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->O_1R->O_N-1O-u0_Ext-3O-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->O_1R->O_N-1O-u0_Ext-3O-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_3R->O_1R->O_N-1O-u0_Ext-3O-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.00111026,'m^3/(mol*s)'), n=2.89721, w0=(222000,'J/mol'), E0=(106112,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->O_1R->O_N-1O-u0_Ext-3O-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->O_1R->O_N-1O-u0_Ext-3O-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->O_1R->O_N-1O-u0_Ext-3O-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->O_1R->O_N-1O-u0_Ext-3O-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_3R->O_N-1R->O_Ext-3O-R_4R!H->C",
    kinetics = ArrheniusBM(A=(2.91727e-06,'m^3/(mol*s)'), n=4.17871, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->O_N-1R->O_Ext-3O-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_Ext-3O-R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_Ext-3O-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_Ext-3O-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(4.80145e-12,'m^3/(mol*s)'), n=5.81504, w0=(357944,'J/mol'), E0=(35794.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.14511091670000018, var=9.845226373886705, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C',), comment="""BM rule fitted to 9 training reactions at node Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C
    Total Standard Deviation in ln(k): 6.654878337176112"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C
Total Standard Deviation in ln(k): 6.654878337176112""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C
Total Standard Deviation in ln(k): 6.654878337176112
""",
)

entry(
    index = 24,
    label = "Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_Sp-4R!H#1CCCClClClFFFHHH",
    kinetics = ArrheniusBM(A=(1.72013,'m^3/(mol*s)'), n=2.4493, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_Sp-4R!H#1CCCClClClFFFHHH',), comment="""BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_Sp-4R!H#1CCCClClClFFFHHH
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_Sp-4R!H#1CCCClClClFFFHHH
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_Sp-4R!H#1CCCClClClFFFHHH
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH",
    kinetics = ArrheniusBM(A=(4.45037e-19,'m^3/(mol*s)'), n=7.88825, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.27555972221121855, var=7.938709169533117, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH',), comment="""BM rule fitted to 9 training reactions at node Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH
    Total Standard Deviation in ln(k): 6.340845534440389"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH
Total Standard Deviation in ln(k): 6.340845534440389""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH
Total Standard Deviation in ln(k): 6.340845534440389
""",
)

entry(
    index = 26,
    label = "Root_3R->O_N-1R->O_N-1CClFH-u0_Ext-1CClFH-R",
    kinetics = ArrheniusBM(A=(0.00797733,'m^3/(mol*s)'), n=2.9371, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.026030962479877167, var=17.411905898531455, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_3R->O_N-1R->O_N-1CClFH-u0_Ext-1CClFH-R',), comment="""BM rule fitted to 6 training reactions at node Root_3R->O_N-1R->O_N-1CClFH-u0_Ext-1CClFH-R
    Total Standard Deviation in ln(k): 8.43067793694655"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_3R->O_N-1R->O_N-1CClFH-u0_Ext-1CClFH-R
Total Standard Deviation in ln(k): 8.43067793694655""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_3R->O_N-1R->O_N-1CClFH-u0_Ext-1CClFH-R
Total Standard Deviation in ln(k): 8.43067793694655
""",
)

entry(
    index = 27,
    label = "Root_N-3R->O_3BrCClFHINPSSi->F_1R->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(9.06896e+07,'m^3/(mol*s)'), n=-0.190202, w0=(320000,'J/mol'), E0=(32000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.02529143280371619, var=2.4048304245064247, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->O_3BrCClFHINPSSi->F_1R->C_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->O_3BrCClFHINPSSi->F_1R->C_Ext-1C-R
    Total Standard Deviation in ln(k): 3.17239237752867"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->O_3BrCClFHINPSSi->F_1R->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.17239237752867""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->O_3BrCClFHINPSSi->F_1R->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.17239237752867
""",
)

entry(
    index = 28,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C",
    kinetics = ArrheniusBM(A=(1.49314e-18,'m^3/(mol*s)'), n=7.37098, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.22764485899194145, var=5.732180675583465, Tref=1000.0, N=23, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C',), comment="""BM rule fitted to 23 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C
    Total Standard Deviation in ln(k): 5.371703302065065"""),
    rank = 11,
    shortDesc = """BM rule fitted to 23 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C
Total Standard Deviation in ln(k): 5.371703302065065""",
    longDesc = 
"""
BM rule fitted to 23 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C
Total Standard Deviation in ln(k): 5.371703302065065
""",
)

entry(
    index = 29,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_N-3CClH->C",
    kinetics = ArrheniusBM(A=(188.681,'m^3/(mol*s)'), n=2.15358, w0=(393500,'J/mol'), E0=(39350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_N-3CClH->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_N-3CClH->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_N-3CClH->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_N-3CClH->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 30,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_1CClFH->F",
    kinetics = ArrheniusBM(A=(3258.2,'m^3/(mol*s)'), n=0.941778, w0=(331429,'J/mol'), E0=(33142.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0299143331907759, var=2.8893453770197914, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_1CClFH->F',), comment="""BM rule fitted to 7 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_1CClFH->F
    Total Standard Deviation in ln(k): 3.482825266877825"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_1CClFH->F
Total Standard Deviation in ln(k): 3.482825266877825""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_1CClFH->F
Total Standard Deviation in ln(k): 3.482825266877825
""",
)

entry(
    index = 31,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F",
    kinetics = ArrheniusBM(A=(0.000184974,'m^3/(mol*s)'), n=3.09602, w0=(501864,'J/mol'), E0=(-7003.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.33284146888393973, var=34.35464248379759, Tref=1000.0, N=62, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F',), comment="""BM rule fitted to 62 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F
    Total Standard Deviation in ln(k): 12.586605423681734"""),
    rank = 11,
    shortDesc = """BM rule fitted to 62 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F
Total Standard Deviation in ln(k): 12.586605423681734""",
    longDesc = 
"""
BM rule fitted to 62 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F
Total Standard Deviation in ln(k): 12.586605423681734
""",
)

entry(
    index = 32,
    label = "Root_3R->O_1R->O_Ext-1O-R_N-3O-u1_4R!H->C",
    kinetics = ArrheniusBM(A=(0.640932,'m^3/(mol*s)'), n=2.39839, w0=(222000,'J/mol'), E0=(123802,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->O_1R->O_Ext-1O-R_N-3O-u1_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->O_1R->O_Ext-1O-R_N-3O-u1_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->O_1R->O_Ext-1O-R_N-3O-u1_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->O_1R->O_Ext-1O-R_N-3O-u1_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_3R->O_1R->O_Ext-1O-R_N-3O-u1_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.0839177,'m^3/(mol*s)'), n=2.53937, w0=(222000,'J/mol'), E0=(112434,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->O_1R->O_Ext-1O-R_N-3O-u1_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->O_1R->O_Ext-1O-R_N-3O-u1_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->O_1R->O_Ext-1O-R_N-3O-u1_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->O_1R->O_Ext-1O-R_N-3O-u1_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0",
    kinetics = ArrheniusBM(A=(1.86187e-15,'m^3/(mol*s)'), n=6.90398, w0=(359214,'J/mol'), E0=(35921.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.20189508283118154, var=8.382431336148349, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0',), comment="""BM rule fitted to 7 training reactions at node Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0
    Total Standard Deviation in ln(k): 6.311469037254658"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0
Total Standard Deviation in ln(k): 6.311469037254658""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0
Total Standard Deviation in ln(k): 6.311469037254658
""",
)

entry(
    index = 35,
    label = "Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_N-1CClFH-u0",
    kinetics = ArrheniusBM(A=(4.18172,'m^3/(mol*s)'), n=2.00376, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.9227449579611222, var=45.348163327937655, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_N-1CClFH-u0',), comment="""BM rule fitted to 2 training reactions at node Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_N-1CClFH-u0
    Total Standard Deviation in ln(k): 18.331112975057057"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_N-1CClFH-u0
Total Standard Deviation in ln(k): 18.331112975057057""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_N-1CClFH-u0
Total Standard Deviation in ln(k): 18.331112975057057
""",
)

entry(
    index = 36,
    label = "Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_Sp-4R!H=1CCClClFFHH",
    kinetics = ArrheniusBM(A=(3.61646e-23,'m^3/(mol*s)'), n=9.15458, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3554320204658105, var=31.87299821333461, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_Sp-4R!H=1CCClClFFHH',), comment="""BM rule fitted to 3 training reactions at node Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_Sp-4R!H=1CCClClFFHH
    Total Standard Deviation in ln(k): 12.21101293653521"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_Sp-4R!H=1CCClClFFHH
Total Standard Deviation in ln(k): 12.21101293653521""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_Sp-4R!H=1CCClClFFHH
Total Standard Deviation in ln(k): 12.21101293653521
""",
)

entry(
    index = 37,
    label = "Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_N-Sp-4R!H=1CCClClFFHH",
    kinetics = ArrheniusBM(A=(4.93688e-17,'m^3/(mol*s)'), n=7.25509, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2356235707682487, var=6.083619708854371, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_N-Sp-4R!H=1CCClClFFHH',), comment="""BM rule fitted to 6 training reactions at node Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_N-Sp-4R!H=1CCClClFFHH
    Total Standard Deviation in ln(k): 5.536697057720324"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_N-Sp-4R!H=1CCClClFFHH
Total Standard Deviation in ln(k): 5.536697057720324""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_N-Sp-4R!H=1CCClClFFHH
Total Standard Deviation in ln(k): 5.536697057720324
""",
)

entry(
    index = 38,
    label = "Root_3R->O_N-1R->O_N-1CClFH-u0_Ext-1CClFH-R_Sp-4R!H-1CClFH",
    kinetics = ArrheniusBM(A=(0.525855,'m^3/(mol*s)'), n=2.39904, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.002420137268149058, var=21.285115513415498, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_3R->O_N-1R->O_N-1CClFH-u0_Ext-1CClFH-R_Sp-4R!H-1CClFH',), comment="""BM rule fitted to 5 training reactions at node Root_3R->O_N-1R->O_N-1CClFH-u0_Ext-1CClFH-R_Sp-4R!H-1CClFH
    Total Standard Deviation in ln(k): 9.255085340023976"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_3R->O_N-1R->O_N-1CClFH-u0_Ext-1CClFH-R_Sp-4R!H-1CClFH
Total Standard Deviation in ln(k): 9.255085340023976""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_3R->O_N-1R->O_N-1CClFH-u0_Ext-1CClFH-R_Sp-4R!H-1CClFH
Total Standard Deviation in ln(k): 9.255085340023976
""",
)

entry(
    index = 39,
    label = "Root_3R->O_N-1R->O_N-1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H-1CClFH",
    kinetics = ArrheniusBM(A=(0.0387235,'m^3/(mol*s)'), n=2.8378, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->O_N-1R->O_N-1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H-1CClFH',), comment="""BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_N-1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H-1CClFH
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_N-1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H-1CClFH
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_N-1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H-1CClFH
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 40,
    label = "Root_N-3R->O_3BrCClFHINPSSi->F_1R->C_Ext-1C-R_4R!H->O",
    kinetics = ArrheniusBM(A=(1.7749e+09,'m^3/(mol*s)'), n=-0.624012, w0=(320000,'J/mol'), E0=(32000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.5540822016511767, var=0.9609060278363374, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_3BrCClFHINPSSi->F_1R->C_Ext-1C-R_4R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_3BrCClFHINPSSi->F_1R->C_Ext-1C-R_4R!H->O
    Total Standard Deviation in ln(k): 3.3573242209195575"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_3BrCClFHINPSSi->F_1R->C_Ext-1C-R_4R!H->O
Total Standard Deviation in ln(k): 3.3573242209195575""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_3BrCClFHINPSSi->F_1R->C_Ext-1C-R_4R!H->O
Total Standard Deviation in ln(k): 3.3573242209195575
""",
)

entry(
    index = 41,
    label = "Root_N-3R->O_3BrCClFHINPSSi->F_1R->C_Ext-1C-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(4.63385e+06,'m^3/(mol*s)'), n=0.243607, w0=(320000,'J/mol'), E0=(32000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.1224165581362937, var=26.32685640378136, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_3BrCClFHINPSSi->F_1R->C_Ext-1C-R_N-4R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_3BrCClFHINPSSi->F_1R->C_Ext-1C-R_N-4R!H->O
    Total Standard Deviation in ln(k): 13.106378283351617"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_3BrCClFHINPSSi->F_1R->C_Ext-1C-R_N-4R!H->O
Total Standard Deviation in ln(k): 13.106378283351617""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_3BrCClFHINPSSi->F_1R->C_Ext-1C-R_N-4R!H->O
Total Standard Deviation in ln(k): 13.106378283351617
""",
)

entry(
    index = 42,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1",
    kinetics = ArrheniusBM(A=(1.23752e-20,'m^3/(mol*s)'), n=7.98469, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.26342053295880474, var=6.629635477137876, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1',), comment="""BM rule fitted to 17 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1
    Total Standard Deviation in ln(k): 5.823668254970071"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1
Total Standard Deviation in ln(k): 5.823668254970071""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1
Total Standard Deviation in ln(k): 5.823668254970071
""",
)

entry(
    index = 43,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_N-3C-u1",
    kinetics = ArrheniusBM(A=(1.17984e-12,'m^3/(mol*s)'), n=5.63212, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.12628044882821055, var=1.1460446740542933, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_N-3C-u1',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_N-3C-u1
    Total Standard Deviation in ln(k): 2.4634261463902623"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_N-3C-u1
Total Standard Deviation in ln(k): 2.4634261463902623""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_N-3C-u1
Total Standard Deviation in ln(k): 2.4634261463902623
""",
)

entry(
    index = 44,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_1CClFH->F_3CClH->C",
    kinetics = ArrheniusBM(A=(48339.6,'m^3/(mol*s)'), n=0.436192, w0=(320000,'J/mol'), E0=(32000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.02408438344513273, var=0.5019752739533132, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_1CClFH->F_3CClH->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_1CClFH->F_3CClH->C
    Total Standard Deviation in ln(k): 1.4808726067825593"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_1CClFH->F_3CClH->C
Total Standard Deviation in ln(k): 1.4808726067825593""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_1CClFH->F_3CClH->C
Total Standard Deviation in ln(k): 1.4808726067825593
""",
)

entry(
    index = 45,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_1CClFH->F_N-3CClH->C",
    kinetics = ArrheniusBM(A=(3.84296,'m^3/(mol*s)'), n=2.20574, w0=(360000,'J/mol'), E0=(36000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.6692812243519491, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_1CClFH->F_N-3CClH->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_1CClFH->F_N-3CClH->C
    Total Standard Deviation in ln(k): 3.6467690015748317"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_1CClFH->F_N-3CClH->C
Total Standard Deviation in ln(k): 3.6467690015748317""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_1CClFH->F_N-3CClH->C
Total Standard Deviation in ln(k): 3.6467690015748317
""",
)

entry(
    index = 46,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H",
    kinetics = ArrheniusBM(A=(0.000749662,'m^3/(mol*s)'), n=3.10502, w0=(517673,'J/mol'), E0=(10685.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.2290148368986173, var=57.513314807902084, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H',), comment="""BM rule fitted to 16 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H
    Total Standard Deviation in ln(k): 23.3165189556349"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H
Total Standard Deviation in ln(k): 23.3165189556349""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H
Total Standard Deviation in ln(k): 23.3165189556349
""",
)

entry(
    index = 47,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H",
    kinetics = ArrheniusBM(A=(4.13446e-10,'m^3/(mol*s)'), n=4.76537, w0=(496365,'J/mol'), E0=(11904.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.8889405811488532, var=76.96515175977228, Tref=1000.0, N=46, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H',), comment="""BM rule fitted to 46 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H
    Total Standard Deviation in ln(k): 19.82101678009418"""),
    rank = 11,
    shortDesc = """BM rule fitted to 46 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H
Total Standard Deviation in ln(k): 19.82101678009418""",
    longDesc = 
"""
BM rule fitted to 46 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H
Total Standard Deviation in ln(k): 19.82101678009418
""",
)

entry(
    index = 48,
    label = "Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0_1CClFH->C",
    kinetics = ArrheniusBM(A=(7.91545e-18,'m^3/(mol*s)'), n=7.56836, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2371644558372289, var=2.0922689553448754, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0_1CClFH->C',), comment="""BM rule fitted to 6 training reactions at node Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0_1CClFH->C
    Total Standard Deviation in ln(k): 3.4956752317636206"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0_1CClFH->C
Total Standard Deviation in ln(k): 3.4956752317636206""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0_1CClFH->C
Total Standard Deviation in ln(k): 3.4956752317636206
""",
)

entry(
    index = 49,
    label = "Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0_N-1CClFH->C",
    kinetics = ArrheniusBM(A=(0.0192658,'m^3/(mol*s)'), n=3.05869, w0=(393500,'J/mol'), E0=(39350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0_N-1CClFH->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0_N-1CClFH->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0_N-1CClFH->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0_N-1CClFH->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 50,
    label = "Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_N-1CClFH-u0_Ext-1CClFH-R_Ext-1CClFH-R",
    kinetics = ArrheniusBM(A=(0.000115787,'m^3/(mol*s)'), n=3.43806, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_N-1CClFH-u0_Ext-1CClFH-R_Ext-1CClFH-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_N-1CClFH-u0_Ext-1CClFH-R_Ext-1CClFH-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_N-1CClFH-u0_Ext-1CClFH-R_Ext-1CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_N-1CClFH-u0_Ext-1CClFH-R_Ext-1CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 51,
    label = "Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_Sp-4R!H=1CCClClFFHH_Ext-1CClFH-R",
    kinetics = ArrheniusBM(A=(7.11294e-15,'m^3/(mol*s)'), n=6.71706, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.5134766165460327, var=0.690220448585621, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_Sp-4R!H=1CCClClFFHH_Ext-1CClFH-R',), comment="""BM rule fitted to 2 training reactions at node Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_Sp-4R!H=1CCClClFFHH_Ext-1CClFH-R
    Total Standard Deviation in ln(k): 10.493354714095197"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_Sp-4R!H=1CCClClFFHH_Ext-1CClFH-R
Total Standard Deviation in ln(k): 10.493354714095197""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_Sp-4R!H=1CCClClFFHH_Ext-1CClFH-R
Total Standard Deviation in ln(k): 10.493354714095197
""",
)

entry(
    index = 52,
    label = "Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_N-Sp-4R!H=1CCClClFFHH_Ext-1CClFH-R",
    kinetics = ArrheniusBM(A=(5.23275e-18,'m^3/(mol*s)'), n=7.56477, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.688102149872853, var=29.172611800688376, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_N-Sp-4R!H=1CCClClFFHH_Ext-1CClFH-R',), comment="""BM rule fitted to 2 training reactions at node Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_N-Sp-4R!H=1CCClClFFHH_Ext-1CClFH-R
    Total Standard Deviation in ln(k): 22.607061343265773"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_N-Sp-4R!H=1CCClClFFHH_Ext-1CClFH-R
Total Standard Deviation in ln(k): 22.607061343265773""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_N-Sp-4R!H=1CCClClFFHH_Ext-1CClFH-R
Total Standard Deviation in ln(k): 22.607061343265773
""",
)

entry(
    index = 53,
    label = "Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_N-Sp-4R!H=1CCClClFFHH_4R!H->Cl",
    kinetics = ArrheniusBM(A=(0.00381903,'m^3/(mol*s)'), n=3.24993, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_N-Sp-4R!H=1CCClClFFHH_4R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_N-Sp-4R!H=1CCClClFFHH_4R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_N-Sp-4R!H=1CCClClFFHH_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_N-Sp-4R!H=1CCClClFFHH_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 54,
    label = "Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_N-Sp-4R!H=1CCClClFFHH_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(2.26272e-14,'m^3/(mol*s)'), n=6.42856, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1980139044022901, var=3.0656399567510455, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_N-Sp-4R!H=1CCClClFFHH_N-4R!H->Cl',), comment="""BM rule fitted to 3 training reactions at node Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_N-Sp-4R!H=1CCClClFFHH_N-4R!H->Cl
    Total Standard Deviation in ln(k): 4.0076068065297195"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_N-Sp-4R!H=1CCClClFFHH_N-4R!H->Cl
Total Standard Deviation in ln(k): 4.0076068065297195""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_N-Sp-4R!H=1CCClClFFHH_N-4R!H->Cl
Total Standard Deviation in ln(k): 4.0076068065297195
""",
)

entry(
    index = 55,
    label = "Root_3R->O_N-1R->O_N-1CClFH-u0_Ext-1CClFH-R_Sp-4R!H-1CClFH_4R!H->C",
    kinetics = ArrheniusBM(A=(2.54569,'m^3/(mol*s)'), n=2.22407, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.23703399793422275, var=30.374551110529616, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->O_N-1R->O_N-1CClFH-u0_Ext-1CClFH-R_Sp-4R!H-1CClFH_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_3R->O_N-1R->O_N-1CClFH-u0_Ext-1CClFH-R_Sp-4R!H-1CClFH_4R!H->C
    Total Standard Deviation in ln(k): 11.644281688004938"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->O_N-1R->O_N-1CClFH-u0_Ext-1CClFH-R_Sp-4R!H-1CClFH_4R!H->C
Total Standard Deviation in ln(k): 11.644281688004938""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->O_N-1R->O_N-1CClFH-u0_Ext-1CClFH-R_Sp-4R!H-1CClFH_4R!H->C
Total Standard Deviation in ln(k): 11.644281688004938
""",
)

entry(
    index = 56,
    label = "Root_3R->O_N-1R->O_N-1CClFH-u0_Ext-1CClFH-R_Sp-4R!H-1CClFH_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.183755,'m^3/(mol*s)'), n=2.51569, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.01910788558130034, var=37.3303580558227, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3R->O_N-1R->O_N-1CClFH-u0_Ext-1CClFH-R_Sp-4R!H-1CClFH_N-4R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_3R->O_N-1R->O_N-1CClFH-u0_Ext-1CClFH-R_Sp-4R!H-1CClFH_N-4R!H->C
    Total Standard Deviation in ln(k): 12.296655310086123"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3R->O_N-1R->O_N-1CClFH-u0_Ext-1CClFH-R_Sp-4R!H-1CClFH_N-4R!H->C
Total Standard Deviation in ln(k): 12.296655310086123""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3R->O_N-1R->O_N-1CClFH-u0_Ext-1CClFH-R_Sp-4R!H-1CClFH_N-4R!H->C
Total Standard Deviation in ln(k): 12.296655310086123
""",
)

entry(
    index = 57,
    label = "Root_N-3R->O_3BrCClFHINPSSi->F_1R->C_Ext-1C-R_N-4R!H->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(9.84714e+10,'m^3/(mol*s)'), n=-0.706626, w0=(320000,'J/mol'), E0=(32000,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_3BrCClFHINPSSi->F_1R->C_Ext-1C-R_N-4R!H->O_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_3BrCClFHINPSSi->F_1R->C_Ext-1C-R_N-4R!H->O_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_3BrCClFHINPSSi->F_1R->C_Ext-1C-R_N-4R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_3BrCClFHINPSSi->F_1R->C_Ext-1C-R_N-4R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 58,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.54344e-21,'m^3/(mol*s)'), n=8.16405, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.27340489627663167, var=6.445441291377109, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R',), comment="""BM rule fitted to 15 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R
    Total Standard Deviation in ln(k): 5.776543062872674"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R
Total Standard Deviation in ln(k): 5.776543062872674""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R
Total Standard Deviation in ln(k): 5.776543062872674
""",
)

entry(
    index = 59,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-1O-R_4R!H->C",
    kinetics = ArrheniusBM(A=(0.000476496,'m^3/(mol*s)'), n=3.27616, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-1O-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-1O-R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-1O-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-1O-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 60,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-1O-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.000849095,'m^3/(mol*s)'), n=3.17369, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-1O-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-1O-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-1O-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-1O-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 61,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_N-3C-u1_Ext-1O-R",
    kinetics = ArrheniusBM(A=(7.91658e-06,'m^3/(mol*s)'), n=3.24946, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_N-3C-u1_Ext-1O-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_N-3C-u1_Ext-1O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_N-3C-u1_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_N-3C-u1_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 62,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_N-3C-u1_1O-u0",
    kinetics = ArrheniusBM(A=(4.59424e-13,'m^3/(mol*s)'), n=5.85065, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1253559220713916, var=0.07230117984200256, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_N-3C-u1_1O-u0',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_N-3C-u1_1O-u0
    Total Standard Deviation in ln(k): 0.8540154117892048"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_N-3C-u1_1O-u0
Total Standard Deviation in ln(k): 0.8540154117892048""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_N-3C-u1_1O-u0
Total Standard Deviation in ln(k): 0.8540154117892048
""",
)

entry(
    index = 63,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_N-3C-u1_N-1O-u0",
    kinetics = ArrheniusBM(A=(0.0391196,'m^3/(mol*s)'), n=2.49957, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_N-3C-u1_N-1O-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_N-3C-u1_N-1O-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_N-3C-u1_N-1O-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_N-3C-u1_N-1O-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 64,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_1CClFH->F_3CClH->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(58716.8,'m^3/(mol*s)'), n=0.378639, w0=(320000,'J/mol'), E0=(32000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.020906567161643637, var=0.2608617441749449, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_1CClFH->F_3CClH->C_Ext-3C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_1CClFH->F_3CClH->C_Ext-3C-R
    Total Standard Deviation in ln(k): 1.0764400103544418"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_1CClFH->F_3CClH->C_Ext-3C-R
Total Standard Deviation in ln(k): 1.0764400103544418""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_1CClFH->F_3CClH->C_Ext-3C-R
Total Standard Deviation in ln(k): 1.0764400103544418
""",
)

entry(
    index = 65,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C",
    kinetics = ArrheniusBM(A=(7.55426e-40,'m^3/(mol*s)'), n=13.5653, w0=(525000,'J/mol'), E0=(-106816,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.582583920531897, var=58.5757439181079, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C',), comment="""BM rule fitted to 15 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C
    Total Standard Deviation in ln(k): 21.83210254626826"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C
Total Standard Deviation in ln(k): 21.83210254626826""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C
Total Standard Deviation in ln(k): 21.83210254626826
""",
)

entry(
    index = 66,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_N-1CClH->C",
    kinetics = ArrheniusBM(A=(6.9e+06,'m^3/(mol*s)'), n=0, w0=(407770,'J/mol'), E0=(40777,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_N-1CClH->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_N-1CClH->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_N-1CClH->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_N-1CClH->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 67,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R",
    kinetics = ArrheniusBM(A=(1.34175e-07,'m^3/(mol*s)'), n=3.44784, w0=(502143,'J/mol'), E0=(14844,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4882909895250913, var=147.12979749355748, Tref=1000.0, N=28, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R',), comment="""BM rule fitted to 28 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R
    Total Standard Deviation in ln(k): 25.543711345893268"""),
    rank = 11,
    shortDesc = """BM rule fitted to 28 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R
Total Standard Deviation in ln(k): 25.543711345893268""",
    longDesc = 
"""
BM rule fitted to 28 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R
Total Standard Deviation in ln(k): 25.543711345893268
""",
)

entry(
    index = 68,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C",
    kinetics = ArrheniusBM(A=(4.60106,'m^3/(mol*s)'), n=1.89483, w0=(492059,'J/mol'), E0=(-54271.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-15.820257477047122, var=893.3254493768096, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C',), comment="""BM rule fitted to 17 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C
    Total Standard Deviation in ln(k): 99.66801619152649"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C
Total Standard Deviation in ln(k): 99.66801619152649""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C
Total Standard Deviation in ln(k): 99.66801619152649
""",
)

entry(
    index = 69,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_N-3CCl->C",
    kinetics = ArrheniusBM(A=(1.6896e+07,'m^3/(mol*s)'), n=-0.197208, w0=(407770,'J/mol'), E0=(40777,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_N-3CCl->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_N-3CCl->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_N-3CCl->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_N-3CCl->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 70,
    label = "Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0_1CClFH->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.22263e-18,'m^3/(mol*s)'), n=7.78745, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.24774887608839782, var=1.4437131529589833, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0_1CClFH->C_Ext-1C-R',), comment="""BM rule fitted to 5 training reactions at node Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0_1CClFH->C_Ext-1C-R
    Total Standard Deviation in ln(k): 3.031266329285076"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0_1CClFH->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.031266329285076""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0_1CClFH->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.031266329285076
""",
)

entry(
    index = 71,
    label = "Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_Sp-4R!H=1CCClClFFHH_Ext-1CClFH-R_3O-u1",
    kinetics = ArrheniusBM(A=(0.0379121,'m^3/(mol*s)'), n=2.90824, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_Sp-4R!H=1CCClClFFHH_Ext-1CClFH-R_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_Sp-4R!H=1CCClClFFHH_Ext-1CClFH-R_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_Sp-4R!H=1CCClClFFHH_Ext-1CClFH-R_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_Sp-4R!H=1CCClClFFHH_Ext-1CClFH-R_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 72,
    label = "Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_Sp-4R!H=1CCClClFFHH_Ext-1CClFH-R_N-3O-u1",
    kinetics = ArrheniusBM(A=(7.30096,'m^3/(mol*s)'), n=2.36151, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_Sp-4R!H=1CCClClFFHH_Ext-1CClFH-R_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_Sp-4R!H=1CCClClFFHH_Ext-1CClFH-R_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_Sp-4R!H=1CCClClFFHH_Ext-1CClFH-R_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_Sp-4R!H=1CCClClFFHH_Ext-1CClFH-R_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 73,
    label = "Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_N-Sp-4R!H=1CCClClFFHH_Ext-1CClFH-R_Ext-1CClFH-R",
    kinetics = ArrheniusBM(A=(0.0308105,'m^3/(mol*s)'), n=2.88761, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_N-Sp-4R!H=1CCClClFFHH_Ext-1CClFH-R_Ext-1CClFH-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_N-Sp-4R!H=1CCClClFFHH_Ext-1CClFH-R_Ext-1CClFH-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_N-Sp-4R!H=1CCClClFFHH_Ext-1CClFH-R_Ext-1CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_N-Sp-4R!H=1CCClClFFHH_Ext-1CClFH-R_Ext-1CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 74,
    label = "Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_N-Sp-4R!H=1CCClClFFHH_N-4R!H->Cl_4CO->C",
    kinetics = ArrheniusBM(A=(2.82154e-16,'m^3/(mol*s)'), n=6.96308, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.3271961102935776, var=0.10106532836810057, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_N-Sp-4R!H=1CCClClFFHH_N-4R!H->Cl_4CO->C',), comment="""BM rule fitted to 2 training reactions at node Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_N-Sp-4R!H=1CCClClFFHH_N-4R!H->Cl_4CO->C
    Total Standard Deviation in ln(k): 8.997110010818872"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_N-Sp-4R!H=1CCClClFFHH_N-4R!H->Cl_4CO->C
Total Standard Deviation in ln(k): 8.997110010818872""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_N-Sp-4R!H=1CCClClFFHH_N-4R!H->Cl_4CO->C
Total Standard Deviation in ln(k): 8.997110010818872
""",
)

entry(
    index = 75,
    label = "Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_N-Sp-4R!H=1CCClClFFHH_N-4R!H->Cl_N-4CO->C",
    kinetics = ArrheniusBM(A=(0.00678858,'m^3/(mol*s)'), n=3.1372, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_N-Sp-4R!H=1CCClClFFHH_N-4R!H->Cl_N-4CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_N-Sp-4R!H=1CCClClFFHH_N-4R!H->Cl_N-4CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_N-Sp-4R!H=1CCClClFFHH_N-4R!H->Cl_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_N-Sp-4R!H=1CCClClFFHH_N-4R!H->Cl_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 76,
    label = "Root_3R->O_N-1R->O_N-1CClFH-u0_Ext-1CClFH-R_Sp-4R!H-1CClFH_4R!H->C_Ext-1CClFH-R",
    kinetics = ArrheniusBM(A=(0.0952393,'m^3/(mol*s)'), n=2.75763, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->O_N-1R->O_N-1CClFH-u0_Ext-1CClFH-R_Sp-4R!H-1CClFH_4R!H->C_Ext-1CClFH-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_N-1CClFH-u0_Ext-1CClFH-R_Sp-4R!H-1CClFH_4R!H->C_Ext-1CClFH-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_N-1CClFH-u0_Ext-1CClFH-R_Sp-4R!H-1CClFH_4R!H->C_Ext-1CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_N-1CClFH-u0_Ext-1CClFH-R_Sp-4R!H-1CClFH_4R!H->C_Ext-1CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 77,
    label = "Root_3R->O_N-1R->O_N-1CClFH-u0_Ext-1CClFH-R_Sp-4R!H-1CClFH_N-4R!H->C_Ext-1CClFH-R",
    kinetics = ArrheniusBM(A=(0.0446012,'m^3/(mol*s)'), n=2.65475, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->O_N-1R->O_N-1CClFH-u0_Ext-1CClFH-R_Sp-4R!H-1CClFH_N-4R!H->C_Ext-1CClFH-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_N-1CClFH-u0_Ext-1CClFH-R_Sp-4R!H-1CClFH_N-4R!H->C_Ext-1CClFH-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_N-1CClFH-u0_Ext-1CClFH-R_Sp-4R!H-1CClFH_N-4R!H->C_Ext-1CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_N-1CClFH-u0_Ext-1CClFH-R_Sp-4R!H-1CClFH_N-4R!H->C_Ext-1CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 78,
    label = "Root_3R->O_N-1R->O_N-1CClFH-u0_Ext-1CClFH-R_Sp-4R!H-1CClFH_N-4R!H->C_3O-u1",
    kinetics = ArrheniusBM(A=(0.00474579,'m^3/(mol*s)'), n=2.96408, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->O_N-1R->O_N-1CClFH-u0_Ext-1CClFH-R_Sp-4R!H-1CClFH_N-4R!H->C_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_N-1CClFH-u0_Ext-1CClFH-R_Sp-4R!H-1CClFH_N-4R!H->C_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_N-1CClFH-u0_Ext-1CClFH-R_Sp-4R!H-1CClFH_N-4R!H->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_N-1CClFH-u0_Ext-1CClFH-R_Sp-4R!H-1CClFH_N-4R!H->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 79,
    label = "Root_3R->O_N-1R->O_N-1CClFH-u0_Ext-1CClFH-R_Sp-4R!H-1CClFH_N-4R!H->C_N-3O-u1",
    kinetics = ArrheniusBM(A=(1.32859,'m^3/(mol*s)'), n=2.43214, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->O_N-1R->O_N-1CClFH-u0_Ext-1CClFH-R_Sp-4R!H-1CClFH_N-4R!H->C_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_N-1CClFH-u0_Ext-1CClFH-R_Sp-4R!H-1CClFH_N-4R!H->C_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_N-1CClFH-u0_Ext-1CClFH-R_Sp-4R!H-1CClFH_N-4R!H->C_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_N-1CClFH-u0_Ext-1CClFH-R_Sp-4R!H-1CClFH_N-4R!H->C_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 80,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(5.49046e-26,'m^3/(mol*s)'), n=9.38964, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3327689673506645, var=0.07407895714845698, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_4R!H->Cl',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_4R!H->Cl
    Total Standard Deviation in ln(k): 1.3817406955698213"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_4R!H->Cl
Total Standard Deviation in ln(k): 1.3817406955698213""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_4R!H->Cl
Total Standard Deviation in ln(k): 1.3817406955698213
""",
)

entry(
    index = 81,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(3.73143e-20,'m^3/(mol*s)'), n=7.85765, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.25856387840757156, var=6.508701079485093, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl',), comment="""BM rule fitted to 12 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 5.764169405687612"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 5.764169405687612""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 5.764169405687612
""",
)

entry(
    index = 82,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_N-3C-u1_1O-u0_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.01503e-12,'m^3/(mol*s)'), n=5.56578, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.10630467437085643, var=0.00036971752178976405, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_N-3C-u1_1O-u0_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_N-3C-u1_1O-u0_Ext-3C-R
    Total Standard Deviation in ln(k): 0.3056442980200545"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_N-3C-u1_1O-u0_Ext-3C-R
Total Standard Deviation in ln(k): 0.3056442980200545""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_N-3C-u1_1O-u0_Ext-3C-R
Total Standard Deviation in ln(k): 0.3056442980200545
""",
)

entry(
    index = 83,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_1CClFH->F_3CClH->C_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(21476.1,'m^3/(mol*s)'), n=0.504852, w0=(320000,'J/mol'), E0=(32000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.027875404831498134, var=0.2711846437048365, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_1CClFH->F_3CClH->C_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_1CClFH->F_3CClH->C_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 1.1140123528522476"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_1CClFH->F_3CClH->C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 1.1140123528522476""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_1CClFH->F_3CClH->C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 1.1140123528522476
""",
)

entry(
    index = 84,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.41536e-21,'m^3/(mol*s)'), n=8.15746, w0=(525000,'J/mol'), E0=(-17571.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.8254236001486828, var=104.69013871967294, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C_Ext-1C-R',), comment="""BM rule fitted to 12 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C_Ext-1C-R
    Total Standard Deviation in ln(k): 22.586016927546723"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C_Ext-1C-R
Total Standard Deviation in ln(k): 22.586016927546723""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C_Ext-1C-R
Total Standard Deviation in ln(k): 22.586016927546723
""",
)

entry(
    index = 85,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R",
    kinetics = ArrheniusBM(A=(2.60186e+14,'m^3/(mol*s)'), n=-2.09663, w0=(485000,'J/mol'), E0=(76903.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.11730654659896363, var=42.68086405786051, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R
    Total Standard Deviation in ln(k): 13.391793245144212"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R
Total Standard Deviation in ln(k): 13.391793245144212""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R
Total Standard Deviation in ln(k): 13.391793245144212
""",
)

entry(
    index = 86,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_4R!H->O",
    kinetics = ArrheniusBM(A=(6.4714e+16,'m^3/(mol*s)'), n=-2.50087, w0=(501000,'J/mol'), E0=(155292,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.30284748024693664, var=209.44111291199104, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_4R!H->O',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_4R!H->O
    Total Standard Deviation in ln(k): 29.773610663172413"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_4R!H->O
Total Standard Deviation in ln(k): 29.773610663172413""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_4R!H->O
Total Standard Deviation in ln(k): 29.773610663172413
""",
)

entry(
    index = 87,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(5.38915e-08,'m^3/(mol*s)'), n=3.57489, w0=(508529,'J/mol'), E0=(14786,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.6889393615697106, var=160.70139371540114, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O',), comment="""BM rule fitted to 17 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O
    Total Standard Deviation in ln(k): 27.144639762315624"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O
Total Standard Deviation in ln(k): 27.144639762315624""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O
Total Standard Deviation in ln(k): 27.144639762315624
""",
)

entry(
    index = 88,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0",
    kinetics = ArrheniusBM(A=(195.704,'m^3/(mol*s)'), n=1.41574, w0=(495909,'J/mol'), E0=(-13009.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-17.195896706649886, var=698.1580686134637, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0',), comment="""BM rule fitted to 11 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0
    Total Standard Deviation in ln(k): 96.17624596004318"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0
Total Standard Deviation in ln(k): 96.17624596004318""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0
Total Standard Deviation in ln(k): 96.17624596004318
""",
)

entry(
    index = 89,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_N-1CClH-u0",
    kinetics = ArrheniusBM(A=(58946.9,'m^3/(mol*s)'), n=0.623319, w0=(485000,'J/mol'), E0=(174045,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.19750296686777583, var=9.812746336080703, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_N-1CClH-u0',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_N-1CClH-u0
    Total Standard Deviation in ln(k): 6.776132065439107"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_N-1CClH-u0
Total Standard Deviation in ln(k): 6.776132065439107""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_N-1CClH-u0
Total Standard Deviation in ln(k): 6.776132065439107
""",
)

entry(
    index = 90,
    label = "Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0_1CClFH->C_Ext-1C-R_Sp-5R!H=1C",
    kinetics = ArrheniusBM(A=(1.88247e-15,'m^3/(mol*s)'), n=6.87072, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.9194619642740138, var=0.016304834531196837, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0_1CClFH->C_Ext-1C-R_Sp-5R!H=1C',), comment="""BM rule fitted to 2 training reactions at node Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0_1CClFH->C_Ext-1C-R_Sp-5R!H=1C
    Total Standard Deviation in ln(k): 5.078754149174308"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0_1CClFH->C_Ext-1C-R_Sp-5R!H=1C
Total Standard Deviation in ln(k): 5.078754149174308""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0_1CClFH->C_Ext-1C-R_Sp-5R!H=1C
Total Standard Deviation in ln(k): 5.078754149174308
""",
)

entry(
    index = 91,
    label = "Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0_1CClFH->C_Ext-1C-R_N-Sp-5R!H=1C",
    kinetics = ArrheniusBM(A=(9.16936e-21,'m^3/(mol*s)'), n=8.3986, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2843292027330782, var=0.5249940210955626, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0_1CClFH->C_Ext-1C-R_N-Sp-5R!H=1C',), comment="""BM rule fitted to 3 training reactions at node Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0_1CClFH->C_Ext-1C-R_N-Sp-5R!H=1C
    Total Standard Deviation in ln(k): 2.1669552746506127"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0_1CClFH->C_Ext-1C-R_N-Sp-5R!H=1C
Total Standard Deviation in ln(k): 2.1669552746506127""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0_1CClFH->C_Ext-1C-R_N-Sp-5R!H=1C
Total Standard Deviation in ln(k): 2.1669552746506127
""",
)

entry(
    index = 92,
    label = "Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_N-Sp-4R!H=1CCClClFFHH_N-4R!H->Cl_4CO->C_Ext-4C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(0.00185843,'m^3/(mol*s)'), n=3.22261, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_N-Sp-4R!H=1CCClClFFHH_N-4R!H->Cl_4CO->C_Ext-4C-R_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_N-Sp-4R!H=1CCClClFFHH_N-4R!H->Cl_4CO->C_Ext-4C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_N-Sp-4R!H=1CCClClFFHH_N-4R!H->Cl_4CO->C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_1CClFH-u0_Ext-1CClFH-R_N-Sp-4R!H#1CCCClClClFFFHHH_N-Sp-4R!H=1CCClClFFHH_N-4R!H->Cl_4CO->C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 93,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-1O-R",
    kinetics = ArrheniusBM(A=(7.71299e-05,'m^3/(mol*s)'), n=3.03221, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-1O-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-1O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 94,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.85918e-06,'m^3/(mol*s)'), n=3.7472, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 95,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C",
    kinetics = ArrheniusBM(A=(1.83428e-16,'m^3/(mol*s)'), n=6.73282, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1967931058979272, var=1.7109262296773071, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C',), comment="""BM rule fitted to 9 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C
    Total Standard Deviation in ln(k): 3.1166962095868267"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 3.1166962095868267""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 3.1166962095868267
""",
)

entry(
    index = 96,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C",
    kinetics = ArrheniusBM(A=(3.14125e-31,'m^3/(mol*s)'), n=11.2321, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4438761924032385, var=38.160093905598075, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C
    Total Standard Deviation in ln(k): 13.49928858510209"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 13.49928858510209""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 13.49928858510209
""",
)

entry(
    index = 97,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_N-3C-u1_1O-u0_Ext-3C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(1.29788e-13,'m^3/(mol*s)'), n=6.01822, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.9784640933125033, var=0.19498774102889238, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_N-3C-u1_1O-u0_Ext-3C-R_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_N-3C-u1_1O-u0_Ext-3C-R_4R!H->C
    Total Standard Deviation in ln(k): 5.856254522758884"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_N-3C-u1_1O-u0_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 5.856254522758884""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_N-3C-u1_1O-u0_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 5.856254522758884
""",
)

entry(
    index = 98,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_N-3C-u1_1O-u0_Ext-3C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(4.33685e-06,'m^3/(mol*s)'), n=3.64876, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_N-3C-u1_1O-u0_Ext-3C-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_N-3C-u1_1O-u0_Ext-3C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_N-3C-u1_1O-u0_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_N-3C-u1_1O-u0_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 99,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_1CClFH->F_3CClH->C_Ext-3C-R_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.65e+06,'m^3/(mol*s)'), n=0, w0=(320000,'J/mol'), E0=(32000,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_1CClFH->F_3CClH->C_Ext-3C-R_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_1CClFH->F_3CClH->C_Ext-3C-R_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_1CClFH->F_3CClH->C_Ext-3C-R_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_1CClFH->F_3CClH->C_Ext-3C-R_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 100,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F",
    kinetics = ArrheniusBM(A=(2.91115e+09,'m^3/(mol*s)'), n=-0.676426, w0=(525000,'J/mol'), E0=(49582.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-13.86024690715722, var=434.85092546119574, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F',), comment="""BM rule fitted to 9 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F
    Total Standard Deviation in ln(k): 76.62964095788975"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F
Total Standard Deviation in ln(k): 76.62964095788975""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F
Total Standard Deviation in ln(k): 76.62964095788975
""",
)

entry(
    index = 101,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F",
    kinetics = ArrheniusBM(A=(336.304,'m^3/(mol*s)'), n=1.15115, w0=(525000,'J/mol'), E0=(84119.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=5.978953462185943, var=93.8329754017231, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F
    Total Standard Deviation in ln(k): 34.44184810871877"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F
Total Standard Deviation in ln(k): 34.44184810871877""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F
Total Standard Deviation in ln(k): 34.44184810871877
""",
)

entry(
    index = 102,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_4R!H->O",
    kinetics = ArrheniusBM(A=(7.96663e+13,'m^3/(mol*s)'), n=-1.00675, w0=(485000,'J/mol'), E0=(74457.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.023071886767473508, var=23.247341832380833, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_4R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_4R!H->O
    Total Standard Deviation in ln(k): 9.723899442841727"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_4R!H->O
Total Standard Deviation in ln(k): 9.723899442841727""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_4R!H->O
Total Standard Deviation in ln(k): 9.723899442841727
""",
)

entry(
    index = 103,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(1.22202e+07,'m^3/(mol*s)'), n=-0.399937, w0=(485000,'J/mol'), E0=(62485.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.004842522460019282, var=4.350712371945208, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_N-4R!H->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_N-4R!H->O
    Total Standard Deviation in ln(k): 4.193716002523654"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_N-4R!H->O
Total Standard Deviation in ln(k): 4.193716002523654""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_N-4R!H->O
Total Standard Deviation in ln(k): 4.193716002523654
""",
)

entry(
    index = 104,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_4R!H->O_1CClH->C",
    kinetics = ArrheniusBM(A=(0.000123671,'m^3/(mol*s)'), n=3.41898, w0=(485000,'J/mol'), E0=(170605,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.032366727905742416, var=6.9934785353169815, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_4R!H->O_1CClH->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_4R!H->O_1CClH->C
    Total Standard Deviation in ln(k): 5.382882602914498"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_4R!H->O_1CClH->C
Total Standard Deviation in ln(k): 5.382882602914498""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_4R!H->O_1CClH->C
Total Standard Deviation in ln(k): 5.382882602914498
""",
)

entry(
    index = 105,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_4R!H->O_N-1CClH->C",
    kinetics = ArrheniusBM(A=(15905.3,'m^3/(mol*s)'), n=1.57595, w0=(525000,'J/mol'), E0=(38511.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.13578562943061823, var=6.859546164325131e-29, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_4R!H->O_N-1CClH->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_4R!H->O_N-1CClH->C
    Total Standard Deviation in ln(k): 0.3411699231925247"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_4R!H->O_N-1CClH->C
Total Standard Deviation in ln(k): 0.3411699231925247""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_4R!H->O_N-1CClH->C
Total Standard Deviation in ln(k): 0.3411699231925247
""",
)

entry(
    index = 106,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C",
    kinetics = ArrheniusBM(A=(0.000198317,'m^3/(mol*s)'), n=3.08906, w0=(495000,'J/mol'), E0=(168330,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.003570420763224793, var=2.8019762697078003, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C',), comment="""BM rule fitted to 8 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C
    Total Standard Deviation in ln(k): 3.364717946936259"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C
Total Standard Deviation in ln(k): 3.364717946936259""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C
Total Standard Deviation in ln(k): 3.364717946936259
""",
)

entry(
    index = 107,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_N-4CClF->C",
    kinetics = ArrheniusBM(A=(2.44462e-14,'m^3/(mol*s)'), n=5.70734, w0=(520556,'J/mol'), E0=(4990.03,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.8721874926725696, var=157.33685027005458, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_N-4CClF->C',), comment="""BM rule fitted to 9 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_N-4CClF->C
    Total Standard Deviation in ln(k): 27.337617170507382"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_N-4CClF->C
Total Standard Deviation in ln(k): 27.337617170507382""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_N-4CClF->C
Total Standard Deviation in ln(k): 27.337617170507382
""",
)

entry(
    index = 108,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C",
    kinetics = ArrheniusBM(A=(137.758,'m^3/(mol*s)'), n=1.53099, w0=(485000,'J/mol'), E0=(171204,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.13331229021227967, var=31.118482184439817, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C',), comment="""BM rule fitted to 8 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C
    Total Standard Deviation in ln(k): 11.51815809130589"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C
Total Standard Deviation in ln(k): 11.51815809130589""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C
Total Standard Deviation in ln(k): 11.51815809130589
""",
)

entry(
    index = 109,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_N-1CClH->C",
    kinetics = ArrheniusBM(A=(193374,'m^3/(mol*s)'), n=0.529316, w0=(525000,'J/mol'), E0=(-17668,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-20.176979688366018, var=699.1718253055901, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_N-1CClH->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_N-1CClH->C
    Total Standard Deviation in ln(k): 103.70484800290072"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_N-1CClH->C
Total Standard Deviation in ln(k): 103.70484800290072""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_N-1CClH->C
Total Standard Deviation in ln(k): 103.70484800290072
""",
)

entry(
    index = 110,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_N-1CClH-u0_Ext-1CClH-R_Sp-4R!H-1CClH",
    kinetics = ArrheniusBM(A=(4.04135e+06,'m^3/(mol*s)'), n=0.131404, w0=(485000,'J/mol'), E0=(180336,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.18293333524098893, var=13.136792961221664, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_N-1CClH-u0_Ext-1CClH-R_Sp-4R!H-1CClH',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_N-1CClH-u0_Ext-1CClH-R_Sp-4R!H-1CClH
    Total Standard Deviation in ln(k): 7.725736456967689"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_N-1CClH-u0_Ext-1CClH-R_Sp-4R!H-1CClH
Total Standard Deviation in ln(k): 7.725736456967689""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_N-1CClH-u0_Ext-1CClH-R_Sp-4R!H-1CClH
Total Standard Deviation in ln(k): 7.725736456967689
""",
)

entry(
    index = 111,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_N-1CClH-u0_Ext-1CClH-R_N-Sp-4R!H-1CClH",
    kinetics = ArrheniusBM(A=(1.28573e-06,'m^3/(mol*s)'), n=3.56699, w0=(485000,'J/mol'), E0=(48500,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_N-1CClH-u0_Ext-1CClH-R_N-Sp-4R!H-1CClH',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_N-1CClH-u0_Ext-1CClH-R_N-Sp-4R!H-1CClH
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_N-1CClH-u0_Ext-1CClH-R_N-Sp-4R!H-1CClH
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_N-1CClH-u0_Ext-1CClH-R_N-Sp-4R!H-1CClH
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 112,
    label = "Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0_1CClFH->C_Ext-1C-R_Sp-5R!H=1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(8.38302e-05,'m^3/(mol*s)'), n=3.60203, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0_1CClFH->C_Ext-1C-R_Sp-5R!H=1C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0_1CClFH->C_Ext-1C-R_Sp-5R!H=1C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0_1CClFH->C_Ext-1C-R_Sp-5R!H=1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0_1CClFH->C_Ext-1C-R_Sp-5R!H=1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 113,
    label = "Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0_1CClFH->C_Ext-1C-R_N-Sp-5R!H=1C_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(5.69582e-06,'m^3/(mol*s)'), n=3.94767, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0_1CClFH->C_Ext-1C-R_N-Sp-5R!H=1C_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0_1CClFH->C_Ext-1C-R_N-Sp-5R!H=1C_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0_1CClFH->C_Ext-1C-R_N-Sp-5R!H=1C_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0_1CClFH->C_Ext-1C-R_N-Sp-5R!H=1C_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 114,
    label = "Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0_1CClFH->C_Ext-1C-R_N-Sp-5R!H=1C_5R!H->C",
    kinetics = ArrheniusBM(A=(5.27349e-06,'m^3/(mol*s)'), n=3.9638, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0_1CClFH->C_Ext-1C-R_N-Sp-5R!H=1C_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0_1CClFH->C_Ext-1C-R_N-Sp-5R!H=1C_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0_1CClFH->C_Ext-1C-R_N-Sp-5R!H=1C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0_1CClFH->C_Ext-1C-R_N-Sp-5R!H=1C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 115,
    label = "Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0_1CClFH->C_Ext-1C-R_N-Sp-5R!H=1C_N-5R!H->C",
    kinetics = ArrheniusBM(A=(6.65995e-06,'m^3/(mol*s)'), n=3.94804, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0_1CClFH->C_Ext-1C-R_N-Sp-5R!H=1C_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0_1CClFH->C_Ext-1C-R_N-Sp-5R!H=1C_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0_1CClFH->C_Ext-1C-R_N-Sp-5R!H=1C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->O_N-1R->O_Ext-3O-R_N-4R!H->C_1CClFH-u0_1CClFH->C_Ext-1C-R_N-Sp-5R!H=1C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 116,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(3.67795e-18,'m^3/(mol*s)'), n=7.1915, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.21267445005356395, var=0.06812177183619142, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 1.0575967341270556"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 1.0575967341270556""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 1.0575967341270556
""",
)

entry(
    index = 117,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0",
    kinetics = ArrheniusBM(A=(5.88373e-15,'m^3/(mol*s)'), n=6.32934, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1653662947494982, var=2.3062508460953035, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0
    Total Standard Deviation in ln(k): 3.459953121777019"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0
Total Standard Deviation in ln(k): 3.459953121777019""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0
Total Standard Deviation in ln(k): 3.459953121777019
""",
)

entry(
    index = 118,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-1O-u0",
    kinetics = ArrheniusBM(A=(3.99453,'m^3/(mol*s)'), n=1.8271, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-1O-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-1O-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-1O-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_N-1O-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 119,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Ext-1O-R",
    kinetics = ArrheniusBM(A=(0.000687695,'m^3/(mol*s)'), n=3.26448, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Ext-1O-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Ext-1O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 120,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(6.05211e-05,'m^3/(mol*s)'), n=3.35051, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 121,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_N-3C-u1_1O-u0_Ext-3C-R_4R!H->C_Sp-4C-3C",
    kinetics = ArrheniusBM(A=(1.1077e-05,'m^3/(mol*s)'), n=3.63411, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_N-3C-u1_1O-u0_Ext-3C-R_4R!H->C_Sp-4C-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_N-3C-u1_1O-u0_Ext-3C-R_4R!H->C_Sp-4C-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_N-3C-u1_1O-u0_Ext-3C-R_4R!H->C_Sp-4C-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_N-3C-u1_1O-u0_Ext-3C-R_4R!H->C_Sp-4C-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 122,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_N-3C-u1_1O-u0_Ext-3C-R_4R!H->C_N-Sp-4C-3C",
    kinetics = ArrheniusBM(A=(2.02262e-05,'m^3/(mol*s)'), n=3.63862, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_N-3C-u1_1O-u0_Ext-3C-R_4R!H->C_N-Sp-4C-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_N-3C-u1_1O-u0_Ext-3C-R_4R!H->C_N-Sp-4C-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_N-3C-u1_1O-u0_Ext-3C-R_4R!H->C_N-Sp-4C-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_N-3C-u1_1O-u0_Ext-3C-R_4R!H->C_N-Sp-4C-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 123,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R",
    kinetics = ArrheniusBM(A=(405577,'m^3/(mol*s)'), n=0.646054, w0=(525000,'J/mol'), E0=(172804,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.022705243406140687, var=17.73184255051114, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R
    Total Standard Deviation in ln(k): 8.498826264557575"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R
Total Standard Deviation in ln(k): 8.498826264557575""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R
Total Standard Deviation in ln(k): 8.498826264557575
""",
)

entry(
    index = 124,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_4BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.07142e+07,'m^3/(mol*s)'), n=0.021022, w0=(525000,'J/mol'), E0=(37025,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.0539125955565538e-15, var=4.8816931486372335e-29, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_4BrCClINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_4BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 1.9167490859651512e-14"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 1.9167490859651512e-14""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 1.9167490859651512e-14
""",
)

entry(
    index = 125,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-4BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(4e+06,'m^3/(mol*s)'), n=0, w0=(525000,'J/mol'), E0=(98263.8,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-4BrCClINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-4BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 126,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_4R!H->O_5R!H->C",
    kinetics = ArrheniusBM(A=(1.08192e+09,'m^3/(mol*s)'), n=0.294345, w0=(485000,'J/mol'), E0=(70701.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_4R!H->O_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_4R!H->O_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_4R!H->O_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_4R!H->O_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 127,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_4R!H->O_N-5R!H->C",
    kinetics = ArrheniusBM(A=(3.37525e+08,'m^3/(mol*s)'), n=0.655991, w0=(485000,'J/mol'), E0=(52964.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_4R!H->O_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_4R!H->O_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_4R!H->O_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_4R!H->O_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 128,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_N-4R!H->O_4CClF->C",
    kinetics = ArrheniusBM(A=(55.5923,'m^3/(mol*s)'), n=1.12408, w0=(485000,'J/mol'), E0=(56238.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.014134232086567567, var=11.956670811070923, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_N-4R!H->O_4CClF->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_N-4R!H->O_4CClF->C
    Total Standard Deviation in ln(k): 6.967570154580985"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_N-4R!H->O_4CClF->C
Total Standard Deviation in ln(k): 6.967570154580985""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_N-4R!H->O_4CClF->C
Total Standard Deviation in ln(k): 6.967570154580985
""",
)

entry(
    index = 129,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_N-4R!H->O_N-4CClF->C",
    kinetics = ArrheniusBM(A=(2.22346e+08,'m^3/(mol*s)'), n=-0.717576, w0=(485000,'J/mol'), E0=(60309.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.007906154924774152, var=1.9232340592402049, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_N-4R!H->O_N-4CClF->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_N-4R!H->O_N-4CClF->C
    Total Standard Deviation in ln(k): 2.8000456413419967"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_N-4R!H->O_N-4CClF->C
Total Standard Deviation in ln(k): 2.8000456413419967""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_N-4R!H->O_N-4CClF->C
Total Standard Deviation in ln(k): 2.8000456413419967
""",
)

entry(
    index = 130,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_4R!H->O_1CClH->C_Ext-3CCl-R",
    kinetics = ArrheniusBM(A=(5.52227e-09,'m^3/(mol*s)'), n=4.65502, w0=(485000,'J/mol'), E0=(143244,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_4R!H->O_1CClH->C_Ext-3CCl-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_4R!H->O_1CClH->C_Ext-3CCl-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_4R!H->O_1CClH->C_Ext-3CCl-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_4R!H->O_1CClH->C_Ext-3CCl-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 131,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_4R!H->O_1CClH->C_3CCl-u1",
    kinetics = ArrheniusBM(A=(1.16395e-07,'m^3/(mol*s)'), n=4.1592, w0=(485000,'J/mol'), E0=(169776,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_4R!H->O_1CClH->C_3CCl-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_4R!H->O_1CClH->C_3CCl-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_4R!H->O_1CClH->C_3CCl-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_4R!H->O_1CClH->C_3CCl-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 132,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_4R!H->O_1CClH->C_N-3CCl-u1",
    kinetics = ArrheniusBM(A=(4.70357e-08,'m^3/(mol*s)'), n=4.531, w0=(485000,'J/mol'), E0=(170055,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_4R!H->O_1CClH->C_N-3CCl-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_4R!H->O_1CClH->C_N-3CCl-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_4R!H->O_1CClH->C_N-3CCl-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_4R!H->O_1CClH->C_N-3CCl-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 133,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C_Sp-4C=3CCClCl",
    kinetics = ArrheniusBM(A=(7.90804e-06,'m^3/(mol*s)'), n=3.70635, w0=(485000,'J/mol'), E0=(180473,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=8.615050681197804e-05, var=3.638739124228993, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C_Sp-4C=3CCClCl',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C_Sp-4C=3CCClCl
    Total Standard Deviation in ln(k): 3.8243447156158"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C_Sp-4C=3CCClCl
Total Standard Deviation in ln(k): 3.8243447156158""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C_Sp-4C=3CCClCl
Total Standard Deviation in ln(k): 3.8243447156158
""",
)

entry(
    index = 134,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C_N-Sp-4C=3CCClCl",
    kinetics = ArrheniusBM(A=(0.00207878,'m^3/(mol*s)'), n=2.71969, w0=(498333,'J/mol'), E0=(165443,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.013497457094648288, var=3.9529038597949686, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C_N-Sp-4C=3CCClCl',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C_N-Sp-4C=3CCClCl
    Total Standard Deviation in ln(k): 4.019709652391487"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C_N-Sp-4C=3CCClCl
Total Standard Deviation in ln(k): 4.019709652391487""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C_N-Sp-4C=3CCClCl
Total Standard Deviation in ln(k): 4.019709652391487
""",
)

entry(
    index = 135,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_N-4CClF->C_1CClH->C",
    kinetics = ArrheniusBM(A=(8.06448e-06,'m^3/(mol*s)'), n=3.27326, w0=(485000,'J/mol'), E0=(53822.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_N-4CClF->C_1CClH->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_N-4CClF->C_1CClH->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_N-4CClF->C_1CClH->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_N-4CClF->C_1CClH->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 136,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_N-4CClF->C_N-1CClH->C",
    kinetics = ArrheniusBM(A=(2.4756e-14,'m^3/(mol*s)'), n=5.70551, w0=(525000,'J/mol'), E0=(5610.96,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.8402569293125832, var=160.68866778340083, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_N-4CClF->C_N-1CClH->C',), comment="""BM rule fitted to 8 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_N-4CClF->C_N-1CClH->C
    Total Standard Deviation in ln(k): 27.523828384187837"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_N-4CClF->C_N-1CClH->C
Total Standard Deviation in ln(k): 27.523828384187837""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_N-4CClF->C_N-1CClH->C
Total Standard Deviation in ln(k): 27.523828384187837
""",
)

entry(
    index = 137,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_4R!H->F",
    kinetics = ArrheniusBM(A=(0.0964,'m^3/(mol*s)'), n=2.41, w0=(485000,'J/mol'), E0=(62127.1,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_4R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_4R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_4R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_4R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 138,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F",
    kinetics = ArrheniusBM(A=(2.47826e-06,'m^3/(mol*s)'), n=3.83361, w0=(485000,'J/mol'), E0=(169871,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.015922366724326387, var=2.7000041963494104, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F',), comment="""BM rule fitted to 7 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F
    Total Standard Deviation in ln(k): 3.3341243775376195"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F
Total Standard Deviation in ln(k): 3.3341243775376195""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F
Total Standard Deviation in ln(k): 3.3341243775376195
""",
)

entry(
    index = 139,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_N-1CClH-u0_Ext-1CClH-R_Sp-4R!H-1CClH_4R!H->C",
    kinetics = ArrheniusBM(A=(6.51763e+08,'m^3/(mol*s)'), n=-0.623975, w0=(485000,'J/mol'), E0=(180751,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1882547913414259, var=34.79542300696017, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_N-1CClH-u0_Ext-1CClH-R_Sp-4R!H-1CClH_4R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_N-1CClH-u0_Ext-1CClH-R_Sp-4R!H-1CClH_4R!H->C
    Total Standard Deviation in ln(k): 12.298462159390047"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_N-1CClH-u0_Ext-1CClH-R_Sp-4R!H-1CClH_4R!H->C
Total Standard Deviation in ln(k): 12.298462159390047""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_N-1CClH-u0_Ext-1CClH-R_Sp-4R!H-1CClH_4R!H->C
Total Standard Deviation in ln(k): 12.298462159390047
""",
)

entry(
    index = 140,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_N-1CClH-u0_Ext-1CClH-R_Sp-4R!H-1CClH_N-4R!H->C",
    kinetics = ArrheniusBM(A=(573.41,'m^3/(mol*s)'), n=1.42307, w0=(485000,'J/mol'), E0=(178584,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.074635836811602, var=10.568480468737494, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_N-1CClH-u0_Ext-1CClH-R_Sp-4R!H-1CClH_N-4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_N-1CClH-u0_Ext-1CClH-R_Sp-4R!H-1CClH_N-4R!H->C
    Total Standard Deviation in ln(k): 6.704760469525989"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_N-1CClH-u0_Ext-1CClH-R_Sp-4R!H-1CClH_N-4R!H->C
Total Standard Deviation in ln(k): 6.704760469525989""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_N-1CClH-u0_Ext-1CClH-R_Sp-4R!H-1CClH_N-4R!H->C
Total Standard Deviation in ln(k): 6.704760469525989
""",
)

entry(
    index = 141,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Ext-1O-R",
    kinetics = ArrheniusBM(A=(8.66494e-05,'m^3/(mol*s)'), n=3.25251, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Ext-1O-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Ext-1O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 142,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(7.78646e-05,'m^3/(mol*s)'), n=3.27081, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 143,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-1O-R",
    kinetics = ArrheniusBM(A=(3.47363e-17,'m^3/(mol*s)'), n=6.91941, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.1369389069937657, var=0.2544942313608796, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-1O-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-1O-R
    Total Standard Deviation in ln(k): 8.893093197725634"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-1O-R
Total Standard Deviation in ln(k): 8.893093197725634""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-1O-R
Total Standard Deviation in ln(k): 8.893093197725634
""",
)

entry(
    index = 144,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-3C-R",
    kinetics = ArrheniusBM(A=(7.21673e-14,'m^3/(mol*s)'), n=6.05636, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.129617103770459, var=4.312988567682566, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-3C-R
    Total Standard Deviation in ln(k): 9.514177618192498"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-3C-R
Total Standard Deviation in ln(k): 9.514177618192498""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-3C-R
Total Standard Deviation in ln(k): 9.514177618192498
""",
)

entry(
    index = 145,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2.129e+08,'m^3/(mol*s)'), n=-0.13362, w0=(525000,'J/mol'), E0=(142759,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.887379141862768e-15, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->C
    Total Standard Deviation in ln(k): 4.742158647896402e-15"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 4.742158647896402e-15""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 4.742158647896402e-15
""",
)

entry(
    index = 146,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(608.453,'m^3/(mol*s)'), n=1.46892, w0=(525000,'J/mol'), E0=(184814,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.004830601962949611, var=0.764728194177801, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 1.765252735082743"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 1.765252735082743""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 1.765252735082743
""",
)

entry(
    index = 147,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_N-4R!H->O_4CClF->C_5R!H->C",
    kinetics = ArrheniusBM(A=(300000,'m^3/(mol*s)'), n=0, w0=(485000,'J/mol'), E0=(73025.1,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_N-4R!H->O_4CClF->C_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_N-4R!H->O_4CClF->C_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_N-4R!H->O_4CClF->C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_N-4R!H->O_4CClF->C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 148,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_N-4R!H->O_4CClF->C_N-5R!H->C",
    kinetics = ArrheniusBM(A=(23397.8,'m^3/(mol*s)'), n=0.361646, w0=(485000,'J/mol'), E0=(52041.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_N-4R!H->O_4CClF->C_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_N-4R!H->O_4CClF->C_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_N-4R!H->O_4CClF->C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_N-4R!H->O_4CClF->C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 149,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_N-4R!H->O_N-4CClF->C_5R!H->O",
    kinetics = ArrheniusBM(A=(2e+06,'m^3/(mol*s)'), n=0, w0=(485000,'J/mol'), E0=(58651.2,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_N-4R!H->O_N-4CClF->C_5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_N-4R!H->O_N-4CClF->C_5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_N-4R!H->O_N-4CClF->C_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_N-4R!H->O_N-4CClF->C_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 150,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_N-4R!H->O_N-4CClF->C_N-5R!H->O",
    kinetics = ArrheniusBM(A=(500000,'m^3/(mol*s)'), n=0, w0=(485000,'J/mol'), E0=(55194,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_N-4R!H->O_N-4CClF->C_N-5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_N-4R!H->O_N-4CClF->C_N-5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_N-4R!H->O_N-4CClF->C_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_Ext-1CClH-R_N-4R!H->O_N-4CClF->C_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 151,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C_Sp-4C=3CCClCl_Ext-3CCl-R",
    kinetics = ArrheniusBM(A=(9.71972e-07,'m^3/(mol*s)'), n=3.8373, w0=(485000,'J/mol'), E0=(176147,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C_Sp-4C=3CCClCl_Ext-3CCl-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C_Sp-4C=3CCClCl_Ext-3CCl-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C_Sp-4C=3CCClCl_Ext-3CCl-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C_Sp-4C=3CCClCl_Ext-3CCl-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 152,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C_N-Sp-4C=3CCClCl_1CClH->C",
    kinetics = ArrheniusBM(A=(4.08559e-07,'m^3/(mol*s)'), n=3.94371, w0=(485000,'J/mol'), E0=(173053,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0001555860252563714, var=1.3020608493179398, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C_N-Sp-4C=3CCClCl_1CClH->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C_N-Sp-4C=3CCClCl_1CClH->C
    Total Standard Deviation in ln(k): 2.2879516349861477"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C_N-Sp-4C=3CCClCl_1CClH->C
Total Standard Deviation in ln(k): 2.2879516349861477""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C_N-Sp-4C=3CCClCl_1CClH->C
Total Standard Deviation in ln(k): 2.2879516349861477
""",
)

entry(
    index = 153,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C_N-Sp-4C=3CCClCl_N-1CClH->C",
    kinetics = ArrheniusBM(A=(38.0863,'m^3/(mol*s)'), n=1.20386, w0=(525000,'J/mol'), E0=(143756,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.7763568394002532e-15, var=5.546678239835258e-30, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C_N-Sp-4C=3CCClCl_N-1CClH->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C_N-Sp-4C=3CCClCl_N-1CClH->C
    Total Standard Deviation in ln(k): 9.184637279209668e-15"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C_N-Sp-4C=3CCClCl_N-1CClH->C
Total Standard Deviation in ln(k): 9.184637279209668e-15""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C_N-Sp-4C=3CCClCl_N-1CClH->C
Total Standard Deviation in ln(k): 9.184637279209668e-15
""",
)

entry(
    index = 154,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_N-4CClF->C_N-1CClH->C_Ext-3CCl-R",
    kinetics = ArrheniusBM(A=(1.47186e+09,'m^3/(mol*s)'), n=-1.25457, w0=(525000,'J/mol'), E0=(115431,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-9.331772358267001, var=197.07327113511053, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_N-4CClF->C_N-1CClH->C_Ext-3CCl-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_N-4CClF->C_N-1CClH->C_Ext-3CCl-R
    Total Standard Deviation in ln(k): 51.58969411540508"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_N-4CClF->C_N-1CClH->C_Ext-3CCl-R
Total Standard Deviation in ln(k): 51.58969411540508""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_N-4CClF->C_N-1CClH->C_Ext-3CCl-R
Total Standard Deviation in ln(k): 51.58969411540508
""",
)

entry(
    index = 155,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C",
    kinetics = ArrheniusBM(A=(2.44017e-07,'m^3/(mol*s)'), n=4.16404, w0=(485000,'J/mol'), E0=(175728,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00025522771122145544, var=1.4648823670544793, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C
    Total Standard Deviation in ln(k): 2.427018747899486"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C
Total Standard Deviation in ln(k): 2.427018747899486""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C
Total Standard Deviation in ln(k): 2.427018747899486
""",
)

entry(
    index = 156,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C",
    kinetics = ArrheniusBM(A=(3.69575e-05,'m^3/(mol*s)'), n=3.47371, w0=(485000,'J/mol'), E0=(169119,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03340575014571195, var=3.9657942102968873, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C
    Total Standard Deviation in ln(k): 4.076224006022539"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C
Total Standard Deviation in ln(k): 4.076224006022539""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C
Total Standard Deviation in ln(k): 4.076224006022539
""",
)

entry(
    index = 157,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_N-1CClH-u0_Ext-1CClH-R_Sp-4R!H-1CClH_4R!H->C_Ext-1CClH-R",
    kinetics = ArrheniusBM(A=(0.00316659,'m^3/(mol*s)'), n=2.90754, w0=(485000,'J/mol'), E0=(148767,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.016744412032128522, var=3.4091025726652537, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_N-1CClH-u0_Ext-1CClH-R_Sp-4R!H-1CClH_4R!H->C_Ext-1CClH-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_N-1CClH-u0_Ext-1CClH-R_Sp-4R!H-1CClH_4R!H->C_Ext-1CClH-R
    Total Standard Deviation in ln(k): 3.743565164412682"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_N-1CClH-u0_Ext-1CClH-R_Sp-4R!H-1CClH_4R!H->C_Ext-1CClH-R
Total Standard Deviation in ln(k): 3.743565164412682""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_N-1CClH-u0_Ext-1CClH-R_Sp-4R!H-1CClH_4R!H->C_Ext-1CClH-R
Total Standard Deviation in ln(k): 3.743565164412682
""",
)

entry(
    index = 158,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_N-1CClH-u0_Ext-1CClH-R_Sp-4R!H-1CClH_N-4R!H->C_Ext-1CClH-R",
    kinetics = ArrheniusBM(A=(1.71639e-05,'m^3/(mol*s)'), n=3.56319, w0=(485000,'J/mol'), E0=(147593,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_N-1CClH-u0_Ext-1CClH-R_Sp-4R!H-1CClH_N-4R!H->C_Ext-1CClH-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_N-1CClH-u0_Ext-1CClH-R_Sp-4R!H-1CClH_N-4R!H->C_Ext-1CClH-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_N-1CClH-u0_Ext-1CClH-R_Sp-4R!H-1CClH_N-4R!H->C_Ext-1CClH-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_N-1CClH-u0_Ext-1CClH-R_Sp-4R!H-1CClH_N-4R!H->C_Ext-1CClH-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 159,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-1O-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.00346669,'m^3/(mol*s)'), n=2.70977, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-1O-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-1O-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-1O-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-1O-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 160,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-3C-R_Sp-5R!H-3C",
    kinetics = ArrheniusBM(A=(1.83515e-06,'m^3/(mol*s)'), n=3.99398, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-3C-R_Sp-5R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-3C-R_Sp-5R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-3C-R_Sp-5R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-3C-R_Sp-5R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 161,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-3C-R_N-Sp-5R!H-3C",
    kinetics = ArrheniusBM(A=(0.000643764,'m^3/(mol*s)'), n=2.99108, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-3C-R_N-Sp-5R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-3C-R_N-Sp-5R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-3C-R_N-Sp-5R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_1R->O_3CClH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-3C_1O-u0_Ext-3C-R_N-Sp-5R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 162,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2623.05,'m^3/(mol*s)'), n=1.33443, w0=(525000,'J/mol'), E0=(184478,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.831867990631525e-15, var=5.798743950956662e-29, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 1.9868637612922088e-14"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 1.9868637612922088e-14""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_3CClH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 1.9868637612922088e-14
""",
)

entry(
    index = 163,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C_N-Sp-4C=3CCClCl_1CClH->C_Ext-3CCl-R",
    kinetics = ArrheniusBM(A=(6.04602e-10,'m^3/(mol*s)'), n=4.8068, w0=(485000,'J/mol'), E0=(160768,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C_N-Sp-4C=3CCClCl_1CClH->C_Ext-3CCl-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C_N-Sp-4C=3CCClCl_1CClH->C_Ext-3CCl-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C_N-Sp-4C=3CCClCl_1CClH->C_Ext-3CCl-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C_N-Sp-4C=3CCClCl_1CClH->C_Ext-3CCl-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 164,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C_N-Sp-4C=3CCClCl_1CClH->C_3CCl-u1",
    kinetics = ArrheniusBM(A=(3.85526e-07,'m^3/(mol*s)'), n=4.0341, w0=(485000,'J/mol'), E0=(176832,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=5.862582240052549e-06, var=0.07405109848287114, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C_N-Sp-4C=3CCClCl_1CClH->C_3CCl-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C_N-Sp-4C=3CCClCl_1CClH->C_3CCl-u1
    Total Standard Deviation in ln(k): 0.5455498847550282"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C_N-Sp-4C=3CCClCl_1CClH->C_3CCl-u1
Total Standard Deviation in ln(k): 0.5455498847550282""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C_N-Sp-4C=3CCClCl_1CClH->C_3CCl-u1
Total Standard Deviation in ln(k): 0.5455498847550282
""",
)

entry(
    index = 165,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C_N-Sp-4C=3CCClCl_1CClH->C_N-3CCl-u1",
    kinetics = ArrheniusBM(A=(2.18882e-06,'m^3/(mol*s)'), n=3.44185, w0=(485000,'J/mol'), E0=(167585,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C_N-Sp-4C=3CCClCl_1CClH->C_N-3CCl-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C_N-Sp-4C=3CCClCl_1CClH->C_N-3CCl-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C_N-Sp-4C=3CCClCl_1CClH->C_N-3CCl-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C_N-Sp-4C=3CCClCl_1CClH->C_N-3CCl-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 166,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_N-4CClF->C_N-1CClH->C_Ext-3CCl-R_Ext-3CCl-R",
    kinetics = ArrheniusBM(A=(1.10533e+06,'m^3/(mol*s)'), n=-0.331017, w0=(525000,'J/mol'), E0=(107399,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-9.23361578773873, var=189.80926122941955, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_N-4CClF->C_N-1CClH->C_Ext-3CCl-R_Ext-3CCl-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_N-4CClF->C_N-1CClH->C_Ext-3CCl-R_Ext-3CCl-R
    Total Standard Deviation in ln(k): 50.81953182071582"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_N-4CClF->C_N-1CClH->C_Ext-3CCl-R_Ext-3CCl-R
Total Standard Deviation in ln(k): 50.81953182071582""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_N-4CClF->C_N-1CClH->C_Ext-3CCl-R_Ext-3CCl-R
Total Standard Deviation in ln(k): 50.81953182071582
""",
)

entry(
    index = 167,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.5027e-05,'m^3/(mol*s)'), n=3.59925, w0=(485000,'J/mol'), E0=(178250,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 168,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(8.8015e-05,'m^3/(mol*s)'), n=3.36358, w0=(485000,'J/mol'), E0=(168745,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.038815891780034736, var=5.7831647601714185, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 4.9185566791636735"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 4.9185566791636735""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 4.9185566791636735
""",
)

entry(
    index = 169,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(5.29538e-06,'m^3/(mol*s)'), n=3.74, w0=(485000,'J/mol'), E0=(173354,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 170,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_N-1CClH-u0_Ext-1CClH-R_Sp-4R!H-1CClH_4R!H->C_Ext-1CClH-R_5R!H->C",
    kinetics = ArrheniusBM(A=(4.47723e-05,'m^3/(mol*s)'), n=3.46134, w0=(485000,'J/mol'), E0=(150992,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_N-1CClH-u0_Ext-1CClH-R_Sp-4R!H-1CClH_4R!H->C_Ext-1CClH-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_N-1CClH-u0_Ext-1CClH-R_Sp-4R!H-1CClH_4R!H->C_Ext-1CClH-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_N-1CClH-u0_Ext-1CClH-R_Sp-4R!H-1CClH_4R!H->C_Ext-1CClH-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_N-1CClH-u0_Ext-1CClH-R_Sp-4R!H-1CClH_4R!H->C_Ext-1CClH-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 171,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_N-1CClH-u0_Ext-1CClH-R_Sp-4R!H-1CClH_4R!H->C_Ext-1CClH-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(3.5032e-05,'m^3/(mol*s)'), n=3.5135, w0=(485000,'J/mol'), E0=(140694,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_N-1CClH-u0_Ext-1CClH-R_Sp-4R!H-1CClH_4R!H->C_Ext-1CClH-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_N-1CClH-u0_Ext-1CClH-R_Sp-4R!H-1CClH_4R!H->C_Ext-1CClH-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_N-1CClH-u0_Ext-1CClH-R_Sp-4R!H-1CClH_4R!H->C_Ext-1CClH-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_N-1CClH-u0_Ext-1CClH-R_Sp-4R!H-1CClH_4R!H->C_Ext-1CClH-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 172,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C_N-Sp-4C=3CCClCl_1CClH->C_3CCl-u1_Ext-4C-R",
    kinetics = ArrheniusBM(A=(6.44863e-08,'m^3/(mol*s)'), n=4.22412, w0=(485000,'J/mol'), E0=(172116,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C_N-Sp-4C=3CCClCl_1CClH->C_3CCl-u1_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C_N-Sp-4C=3CCClCl_1CClH->C_3CCl-u1_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C_N-Sp-4C=3CCClCl_1CClH->C_3CCl-u1_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_4CClF->C_N-Sp-4C=3CCClCl_1CClH->C_3CCl-u1_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 173,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_N-4CClF->C_N-1CClH->C_Ext-3CCl-R_Ext-3CCl-R_4ClF->F",
    kinetics = ArrheniusBM(A=(0.0015362,'m^3/(mol*s)'), n=2.50956, w0=(525000,'J/mol'), E0=(184399,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.552713678800665e-15, var=6.310887241768139e-28, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_N-4CClF->C_N-1CClH->C_Ext-3CCl-R_Ext-3CCl-R_4ClF->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_N-4CClF->C_N-1CClH->C_Ext-3CCl-R_Ext-3CCl-R_4ClF->F
    Total Standard Deviation in ln(k): 5.928832710519964e-14"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_N-4CClF->C_N-1CClH->C_Ext-3CCl-R_Ext-3CCl-R_4ClF->F
Total Standard Deviation in ln(k): 5.928832710519964e-14""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_N-4CClF->C_N-1CClH->C_Ext-3CCl-R_Ext-3CCl-R_4ClF->F
Total Standard Deviation in ln(k): 5.928832710519964e-14
""",
)

entry(
    index = 174,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_N-4CClF->C_N-1CClH->C_Ext-3CCl-R_Ext-3CCl-R_N-4ClF->F",
    kinetics = ArrheniusBM(A=(60.0213,'m^3/(mol*s)'), n=0.789613, w0=(525000,'J/mol'), E0=(87114.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_N-4CClF->C_N-1CClH->C_Ext-3CCl-R_Ext-3CCl-R_N-4ClF->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_N-4CClF->C_N-1CClH->C_Ext-3CCl-R_Ext-3CCl-R_N-4ClF->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_N-4CClF->C_N-1CClH->C_Ext-3CCl-R_Ext-3CCl-R_N-4ClF->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_Ext-3CCl-R_N-4R!H->O_N-4CClF->C_N-1CClH->C_Ext-3CCl-R_Ext-3CCl-R_N-4ClF->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 175,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(8.20609e-05,'m^3/(mol*s)'), n=3.38243, w0=(485000,'J/mol'), E0=(158962,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.012264147187268556, var=12.879310944920245, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C_Ext-1C-R
    Total Standard Deviation in ln(k): 7.225358948516927"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 7.225358948516927""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 7.225358948516927
""",
)

entry(
    index = 176,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(4.51365e-06,'m^3/(mol*s)'), n=3.78897, w0=(485000,'J/mol'), E0=(175679,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 177,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C_Ext-1C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.21333e-05,'m^3/(mol*s)'), n=3.66599, w0=(485000,'J/mol'), E0=(170288,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C_Ext-1C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C_Ext-1C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 178,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C_Ext-1C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(3.38922e-05,'m^3/(mol*s)'), n=3.5758, w0=(485000,'J/mol'), E0=(152436,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C_Ext-1C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C_Ext-1C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->F_N-1R->O_N-1CClFH->F_N-3CClH->H_3CCl->C_1CClH-u0_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

