#!/usr/bin/env python
# encoding: utf-8

name = "Intra_R_Add_Exocyclic/rules"
shortDesc = u""
longDesc = u"""
General comments go at the top of the file,

or in a section(s) titled 'General'

.. the ID must match those in the rateLibrary AS A STRING (ie. '2' is different from '02')
"""
entry(
    index = 1,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-5R!H-3C_N-Sp-5R!H-3C",
    kinetics = ArrheniusBM(A=(4.65626e+08,'s^-1'), n=0.824123, w0=(301000,'J/mol'), E0=(60246.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.32478894173e-06,var=1.61990102476e-42,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-5R!H-3C_N-Sp-5R!H-3C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-5R!H-3C_N-Sp-5R!H-3C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-5R!H-3C_N-Sp-5R!H-3C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-5R!H-3C_N-Sp-5R!H-3C
""",
)

entry(
    index = 2,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(3.74161e+08,'s^-1'), n=1.1957, w0=(301000,'J/mol'), E0=(65644,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-9R!H=8R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-9R!H=8R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-9R!H=8R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-9R!H=8R!H
""",
)

entry(
    index = 3,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(4.5902e-23,'s^-1'), n=10.1422, w0=(301000,'J/mol'), E0=(20073.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.50840908129,var=8.3898366711,Tref=1000.0,N=40,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R
""",
)

entry(
    index = 4,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(605933,'s^-1'), n=2.02933, w0=(173000,'J/mol'), E0=(34667.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.149845122859,var=1.82168780747,Tref=1000.0,N=4,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-8R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-8R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-8R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-8R!H-R
""",
)

entry(
    index = 5,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-5R!H-3R!H",
    kinetics = ArrheniusBM(A=(1.95263e+09,'s^-1'), n=1.04355, w0=(301000,'J/mol'), E0=(56068.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0285859942536,var=0.236632916579,Tref=1000.0,N=4,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-5R!H-3R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-5R!H-3R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-5R!H-3R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-5R!H-3R!H
""",
)

entry(
    index = 6,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_1CbCbfCdCddCtNO2dS2d->Cdd",
    kinetics = ArrheniusBM(A=(3.66412e+10,'s^-1'), n=0.667449, w0=(307000,'J/mol'), E0=(135408,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_1CbCbfCdCddCtNO2dS2d->Cdd',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_1CbCbfCdCddCtNO2dS2d->Cdd"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_1CbCbfCdCddCtNO2dS2d->Cdd""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_1CbCbfCdCddCtNO2dS2d->Cdd
""",
)

entry(
    index = 7,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(3.83124e+07,'s^-1'), n=0.839846, w0=(301000,'J/mol'), E0=(52304.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00379158771805,var=0.915880643458,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_N-Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_N-Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_N-Sp-7R!H=6R!H
""",
)

entry(
    index = 8,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.50105e+22,'s^-1'), n=-3.28285, w0=(301000,'J/mol'), E0=(114486,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.16938241956,var=14.8527201788,Tref=1000.0,N=5,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H
""",
)

entry(
    index = 9,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(4.24551e-39,'s^-1'), n=15.0285, w0=(301000,'J/mol'), E0=(12112.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.755361003618,var=0.0870358967398,Tref=1000.0,N=4,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H
""",
)

entry(
    index = 10,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(4.33644e+08,'s^-1'), n=1.05183, w0=(301000,'J/mol'), E0=(68527,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0225937550444,var=0.292576819,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H
""",
)

entry(
    index = 11,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(3.40808e+06,'s^-1'), n=1.54443, w0=(301000,'J/mol'), E0=(80753.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0295915535169,var=1.86800468636,Tref=1000.0,N=8,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R
""",
)

entry(
    index = 12,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.94935e+11,'s^-1'), n=0.562354, w0=(301000,'J/mol'), E0=(108393,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 13,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-3R!H->C",
    kinetics = ArrheniusBM(A=(9.40445e+08,'s^-1'), n=0.990105, w0=(307000,'J/mol'), E0=(106266,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-3R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-3R!H->C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-3R!H->C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-3R!H->C
""",
)

entry(
    index = 14,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.31375e+11,'s^-1'), n=0.61983, w0=(301000,'J/mol'), E0=(33763.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0110344163503,var=0.164456699419,Tref=1000.0,N=2,correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 15,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_N-1CbCbfCdCddCtNO2dS2d->Cd_4R!H-inRing",
    kinetics = ArrheniusBM(A=(2324.83,'s^-1'), n=2.55831, w0=(289500,'J/mol'), E0=(28950,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_N-1CbCbfCdCddCtNO2dS2d->Cd_4R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_N-1CbCbfCdCddCtNO2dS2d->Cd_4R!H-inRing"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_N-1CbCbfCdCddCtNO2dS2d->Cd_4R!H-inRing""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_N-1CbCbfCdCddCtNO2dS2d->Cd_4R!H-inRing
""",
)

entry(
    index = 16,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H",
    kinetics = ArrheniusBM(A=(1.39498e+09,'s^-1'), n=0.941261, w0=(301000,'J/mol'), E0=(70033.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0127810650805,var=0.293420649805,Tref=1000.0,N=4,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H
""",
)

entry(
    index = 17,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(8.39302e+09,'s^-1'), n=0.920797, w0=(301000,'J/mol'), E0=(16943.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 18,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(3.38107e+08,'s^-1'), n=0.980247, w0=(301000,'J/mol'), E0=(101127,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 19,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(1.02514e-19,'s^-1'), n=8.88363, w0=(301000,'J/mol'), E0=(26889.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.241005241734,var=18.1113458766,Tref=1000.0,N=17,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R
""",
)

entry(
    index = 20,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_N-1CbCbfCdCddCtNO2dS2d->Cd",
    kinetics = ArrheniusBM(A=(0.000159581,'s^-1'), n=4.35533, w0=(289500,'J/mol'), E0=(28950,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.218052543847,var=130.280448181,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_N-1CbCbfCdCddCtNO2dS2d->Cd',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_N-1CbCbfCdCddCtNO2dS2d->Cd"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_N-1CbCbfCdCddCtNO2dS2d->Cd""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_N-1CbCbfCdCddCtNO2dS2d->Cd
""",
)

entry(
    index = 21,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.99613e+10,'s^-1'), n=0.644903, w0=(301000,'J/mol'), E0=(128897,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0223844384399,var=0.265880214744,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-3R!H-R
""",
)

entry(
    index = 22,
    label = "Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R",
    kinetics = ArrheniusBM(A=(2.2962e+16,'s^-1'), n=-0.978559, w0=(301000,'J/mol'), E0=(36633.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0727703289576,var=0.982487184146,Tref=1000.0,N=12,correlation='Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R
""",
)

entry(
    index = 23,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.05279e+07,'s^-1'), n=1.56761, w0=(301000,'J/mol'), E0=(77145.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0123504880191,var=0.0189338227234,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 24,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2.30181e+12,'s^-1'), n=-0.0807988, w0=(301000,'J/mol'), E0=(85114.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0547487608519,var=0.824663435905,Tref=1000.0,N=12,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R
""",
)

entry(
    index = 25,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H",
    kinetics = ArrheniusBM(A=(4.64418e+06,'s^-1'), n=1.44531, w0=(301000,'J/mol'), E0=(86625.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0199384040257,var=0.278544634361,Tref=1000.0,N=4,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H
""",
)

entry(
    index = 26,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_4R!H-inRing_N-1CbCbfCdCddCtNO2dS2d->Cd",
    kinetics = ArrheniusBM(A=(8.28539e+21,'s^-1'), n=-2.75192, w0=(289500,'J/mol'), E0=(28950,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_4R!H-inRing_N-1CbCbfCdCddCtNO2dS2d->Cd',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_4R!H-inRing_N-1CbCbfCdCddCtNO2dS2d->Cd"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_4R!H-inRing_N-1CbCbfCdCddCtNO2dS2d->Cd""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_4R!H-inRing_N-1CbCbfCdCddCtNO2dS2d->Cd
""",
)

entry(
    index = 27,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(4.47363e+08,'s^-1'), n=0.760345, w0=(301000,'J/mol'), E0=(55664.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 28,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(3.82175e+33,'s^-1'), n=-6.35214, w0=(300629,'J/mol'), E0=(87428.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.607916371742,var=41.3322487407,Tref=1000.0,N=31,correlation='Root_Ext-3R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R
""",
)

entry(
    index = 29,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.50439e+08,'s^-1'), n=0.796342, w0=(301000,'J/mol'), E0=(51332,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00273979963133,var=0.904537930129,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H
""",
)

entry(
    index = 30,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H-3R!H",
    kinetics = ArrheniusBM(A=(1.43853e+08,'s^-1'), n=1.14116, w0=(301000,'J/mol'), E0=(51023.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00568475640721,var=10.5037007907,Tref=1000.0,N=8,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H-3R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H-3R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H-3R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H-3R!H
""",
)

entry(
    index = 31,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(4.055e+07,'s^-1'), n=1.20733, w0=(301000,'J/mol'), E0=(63054.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 32,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H",
    kinetics = ArrheniusBM(A=(1.47865e+06,'s^-1'), n=1.90835, w0=(301000,'J/mol'), E0=(118062,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0645286395384,var=5.58234898687,Tref=1000.0,N=8,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H
""",
)

entry(
    index = 33,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H",
    kinetics = ArrheniusBM(A=(3.39743e+09,'s^-1'), n=0.953889, w0=(301000,'J/mol'), E0=(59856.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0245997235008,var=0.292293430792,Tref=1000.0,N=4,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H
""",
)

entry(
    index = 34,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Int-6R!H-5R!H_Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(2424.11,'s^-1'), n=2.13938, w0=(301000,'J/mol'), E0=(37549.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.02277169744,var=7.67554894143,Tref=1000.0,N=10,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Int-6R!H-5R!H_Sp-6R!H-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Int-6R!H-5R!H_Sp-6R!H-5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Int-6R!H-5R!H_Sp-6R!H-5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Int-6R!H-5R!H_Sp-6R!H-5R!H
""",
)

entry(
    index = 35,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.43241e+08,'s^-1'), n=0.961238, w0=(301000,'J/mol'), E0=(53746.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R
""",
)

entry(
    index = 36,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.04295e+09,'s^-1'), n=1.13225, w0=(301000,'J/mol'), E0=(69644,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0027232184148,var=0.0913693400706,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 37,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.93485e+09,'s^-1'), n=0.949216, w0=(301000,'J/mol'), E0=(66583.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 38,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(5.90975e+07,'s^-1'), n=0.951414, w0=(301000,'J/mol'), E0=(63623,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 39,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(3.81733e+07,'s^-1'), n=0.81439, w0=(301000,'J/mol'), E0=(54101.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 40,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_Int-5R!H-3R!H_Ext-6R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(2.78294e+08,'s^-1'), n=1.08453, w0=(301000,'J/mol'), E0=(57926.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_Int-5R!H-3R!H_Ext-6R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_Int-5R!H-3R!H_Ext-6R!H-R_Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_Int-5R!H-3R!H_Ext-6R!H-R_Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_Int-5R!H-3R!H_Ext-6R!H-R_Sp-7R!H=6R!H
""",
)

entry(
    index = 41,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.313e+08,'s^-1'), n=1.22809, w0=(301000,'J/mol'), E0=(69110.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 42,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H#4R!H_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R",
    kinetics = ArrheniusBM(A=(7.40182e+22,'s^-1'), n=-3.10718, w0=(301000,'J/mol'), E0=(-16465.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H#4R!H_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H#4R!H_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H#4R!H_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H#4R!H_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R
""",
)

entry(
    index = 43,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.32429e+10,'s^-1'), n=0.806536, w0=(301000,'J/mol'), E0=(63734.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 44,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.87799e+09,'s^-1'), n=0.895423, w0=(301000,'J/mol'), E0=(134882,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0148828453056,var=0.280853625932,Tref=1000.0,N=4,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R
""",
)

entry(
    index = 45,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_6R!H-inRing_3R!H-inRing",
    kinetics = ArrheniusBM(A=(6.37204e+06,'s^-1'), n=1.33295, w0=(301000,'J/mol'), E0=(60918.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_6R!H-inRing_3R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_6R!H-inRing_3R!H-inRing"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_6R!H-inRing_3R!H-inRing""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_6R!H-inRing_3R!H-inRing
""",
)

entry(
    index = 46,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(7.19877e+09,'s^-1'), n=0.945017, w0=(301000,'J/mol'), E0=(23232.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-5R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-5R!H=4R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-5R!H=4R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-5R!H=4R!H
""",
)

entry(
    index = 47,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(8.30795e-15,'s^-1'), n=7.16537, w0=(194333,'J/mol'), E0=(2292.32,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.350107430437,var=8.73978550471,Tref=1000.0,N=6,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R
""",
)

entry(
    index = 48,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1CbCdCt->Cd_Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(4.04222e+06,'s^-1'), n=1.00513, w0=(301000,'J/mol'), E0=(212196,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=11.4764327184,var=299.250739541,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1CbCdCt->Cd_Sp-6R!H-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1CbCdCt->Cd_Sp-6R!H-5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1CbCdCt->Cd_Sp-6R!H-5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1CbCdCt->Cd_Sp-6R!H-5R!H
""",
)

entry(
    index = 49,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H",
    kinetics = ArrheniusBM(A=(4.94133e+44,'s^-1'), n=-9.70784, w0=(298700,'J/mol'), E0=(116699,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.645851718655,var=59.2650036041,Tref=1000.0,N=5,correlation='Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H
""",
)

entry(
    index = 50,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(4.09407e+10,'s^-1'), n=0.580786, w0=(301000,'J/mol'), E0=(89779.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 51,
    label = "Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(4.68272e+10,'s^-1'), n=0.733203, w0=(301000,'J/mol'), E0=(29539.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00833494554163,var=0.280535978455,Tref=1000.0,N=4,correlation='Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R
""",
)

entry(
    index = 52,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(3.02218e+17,'s^-1'), n=-1.20687, w0=(301000,'J/mol'), E0=(1875.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-5R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-5R!H=4R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-5R!H=4R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-5R!H=4R!H
""",
)

entry(
    index = 53,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_Int-5R!H-3R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(2.55183e+08,'s^-1'), n=1.02793, w0=(301000,'J/mol'), E0=(54920,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0160007123562,var=0.207410691002,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_Int-5R!H-3R!H_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_Int-5R!H-3R!H_Ext-6R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_Int-5R!H-3R!H_Ext-6R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_Int-5R!H-3R!H_Ext-6R!H-R
""",
)

entry(
    index = 54,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(2.60243e+09,'s^-1'), n=0.979075, w0=(301000,'J/mol'), E0=(55614.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 55,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_N-4R!H-inRing",
    kinetics = ArrheniusBM(A=(3.4015e+12,'s^-1'), n=-0.707238, w0=(301000,'J/mol'), E0=(64103.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=8.48684405015,var=169.729871204,Tref=1000.0,N=3,correlation='Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_N-4R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_N-4R!H-inRing"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_N-4R!H-inRing""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_N-4R!H-inRing
""",
)

entry(
    index = 56,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(9.84765e+06,'s^-1'), n=1.40256, w0=(301000,'J/mol'), E0=(62016.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00841384333474,var=0.145858903629,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Sp-7R!H=6R!H
""",
)

entry(
    index = 57,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H",
    kinetics = ArrheniusBM(A=(5.99451e+06,'s^-1'), n=1.52059, w0=(301000,'J/mol'), E0=(73517.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H
""",
)

entry(
    index = 58,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H-3R!H",
    kinetics = ArrheniusBM(A=(3.04667e-51,'s^-1'), n=18.3847, w0=(301000,'J/mol'), E0=(30100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H-3R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H-3R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H-3R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H-3R!H
""",
)

entry(
    index = 59,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(4.52799e+10,'s^-1'), n=0.675212, w0=(301000,'J/mol'), E0=(103784,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R
""",
)

entry(
    index = 60,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.49941e+12,'s^-1'), n=0.325911, w0=(301000,'J/mol'), E0=(25798.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 61,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-10R!H=9R!H",
    kinetics = ArrheniusBM(A=(1.75927e+07,'s^-1'), n=1.57122, w0=(301000,'J/mol'), E0=(81271.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-10R!H=9R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-10R!H=9R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-10R!H=9R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-10R!H=9R!H
""",
)

entry(
    index = 62,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.21077e+09,'s^-1'), n=1.04684, w0=(301000,'J/mol'), E0=(58444.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0352831499097,var=0.315546460467,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H
""",
)

entry(
    index = 63,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd",
    kinetics = ArrheniusBM(A=(8.14347e+34,'s^-1'), n=-7.01719, w0=(301000,'J/mol'), E0=(145764,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.348576608697,var=71.7454498138,Tref=1000.0,N=33,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd
""",
)

entry(
    index = 64,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.52781e+06,'s^-1'), n=1.39275, w0=(301000,'J/mol'), E0=(60090.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 65,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(8.41224e+06,'s^-1'), n=0.88548, w0=(301000,'J/mol'), E0=(52952.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R
""",
)

entry(
    index = 66,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_N-Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(1.89314e+10,'s^-1'), n=0.72951, w0=(301000,'J/mol'), E0=(25446.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00862509075044,var=0.409607504302,Tref=1000.0,N=2,correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_N-Sp-5R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_N-Sp-5R!H=4R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_N-Sp-5R!H=4R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_N-Sp-5R!H=4R!H
""",
)

entry(
    index = 67,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(3.16702e+07,'s^-1'), n=1.27543, w0=(301000,'J/mol'), E0=(67288.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0143977612424,var=0.0319906930598,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H
""",
)

entry(
    index = 68,
    label = "Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_Sp-8R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(3.40304e+09,'s^-1'), n=0.932563, w0=(301000,'J/mol'), E0=(25931.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_Sp-8R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_Sp-8R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_Sp-8R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_Sp-8R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 69,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H",
    kinetics = ArrheniusBM(A=(6.20543e+10,'s^-1'), n=0.067579, w0=(301000,'J/mol'), E0=(85489.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0488427409801,var=1.01291071112,Tref=1000.0,N=6,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H
""",
)

entry(
    index = 70,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(5.25306e+07,'s^-1'), n=1.12658, w0=(301000,'J/mol'), E0=(68313.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 71,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(2.33477e+09,'s^-1'), n=1.09691, w0=(301000,'J/mol'), E0=(73464.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-9R!H=8R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-9R!H=8R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-9R!H=8R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-9R!H=8R!H
""",
)

entry(
    index = 72,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(9.54669e+10,'s^-1'), n=0.630769, w0=(301000,'J/mol'), E0=(30510.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0160116518284,var=0.220265804049,Tref=1000.0,N=8,correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R
""",
)

entry(
    index = 73,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(4.9229e+09,'s^-1'), n=0.51563, w0=(301000,'J/mol'), E0=(91628.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R
""",
)

entry(
    index = 74,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(3.86202e+07,'s^-1'), n=1.32793, w0=(301000,'J/mol'), E0=(77544.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0201579576861,var=0.91377543496,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_N-Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_N-Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_N-Sp-7R!H=6R!H
""",
)

entry(
    index = 75,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(3.6826e+08,'s^-1'), n=1.0251, w0=(301000,'J/mol'), E0=(92009.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 76,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(8.65916e+08,'s^-1'), n=0.967732, w0=(301000,'J/mol'), E0=(95441.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 77,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H",
    kinetics = ArrheniusBM(A=(30.7804,'s^-1'), n=2.72315, w0=(301000,'J/mol'), E0=(18525.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.115086347972,var=0.914951414351,Tref=1000.0,N=12,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H
""",
)

entry(
    index = 78,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(17574.8,'s^-1'), n=1.9797, w0=(301000,'J/mol'), E0=(53460.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0537147483489,var=0.205299439259,Tref=1000.0,N=4,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H
""",
)

entry(
    index = 79,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_4R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd",
    kinetics = ArrheniusBM(A=(2.50404e+13,'s^-1'), n=-0.142489, w0=(301000,'J/mol'), E0=(42181.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_4R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_4R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_4R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_4R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd
""",
)

entry(
    index = 80,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1CbCdCt->Cd_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(7.8262e-56,'s^-1'), n=19.9076, w0=(301000,'J/mol'), E0=(2741.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.98376430314,var=75.7874949622,Tref=1000.0,N=4,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1CbCdCt->Cd_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1CbCdCt->Cd_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1CbCdCt->Cd_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1CbCdCt->Cd_Ext-3R!H-R
""",
)

entry(
    index = 81,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(7.96606e-39,'s^-1'), n=15.0081, w0=(301000,'J/mol'), E0=(12365.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.750900175699,var=0.635046696049,Tref=1000.0,N=4,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H
""",
)

entry(
    index = 82,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(9.73333e+10,'s^-1'), n=0.587475, w0=(301000,'J/mol'), E0=(29933.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0118186602151,var=0.170800438727,Tref=1000.0,N=4,correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H
""",
)

entry(
    index = 83,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(2.14342e+07,'s^-1'), n=0.982219, w0=(301000,'J/mol'), E0=(49309.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0129427526463,var=0.0260104811812,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H
""",
)

entry(
    index = 84,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(2.28154e+07,'s^-1'), n=1.27385, w0=(301000,'J/mol'), E0=(96574.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0059355392252,var=0.125659233443,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Sp-7R!H=6R!H
""",
)

entry(
    index = 85,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(7.70239e+07,'s^-1'), n=0.893138, w0=(301000,'J/mol'), E0=(64033.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0161856871855,var=0.274306687645,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-3R!H-R
""",
)

entry(
    index = 86,
    label = "Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-8R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(6.84345e+10,'s^-1'), n=0.599404, w0=(301000,'J/mol'), E0=(29478.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-8R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-8R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-8R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-8R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 87,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(9.92398e+16,'s^-1'), n=-1.03321, w0=(301000,'J/mol'), E0=(1078.27,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-5R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-5R!H=4R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-5R!H=4R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-5R!H=4R!H
""",
)

entry(
    index = 88,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-5R!H-3C_Sp-5R!H-3C",
    kinetics = ArrheniusBM(A=(8.30826e+08,'s^-1'), n=1.1618, w0=(301000,'J/mol'), E0=(40773,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00209384126442,var=10.5024968388,Tref=1000.0,N=8,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-5R!H-3C_Sp-5R!H-3C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-5R!H-3C_Sp-5R!H-3C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-5R!H-3C_Sp-5R!H-3C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-5R!H-3C_Sp-5R!H-3C
""",
)

entry(
    index = 89,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H",
    kinetics = ArrheniusBM(A=(2.38791e+12,'s^-1'), n=-0.257223, w0=(184167,'J/mol'), E0=(65523.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0869937873024,var=21.8863526817,Tref=1000.0,N=12,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H
""",
)

entry(
    index = 90,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_6R!H-inRing",
    kinetics = ArrheniusBM(A=(2.04385e+22,'s^-1'), n=-3.12264, w0=(301000,'J/mol'), E0=(93875.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.71888454525,var=55.5897148934,Tref=1000.0,N=3,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_6R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_6R!H-inRing"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_6R!H-inRing""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_6R!H-inRing
""",
)

entry(
    index = 91,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-8R!H-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(8.86025e+08,'s^-1'), n=1.22424, w0=(173000,'J/mol'), E0=(37111.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-8R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-8R!H-R_Ext-9R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-8R!H-R_Ext-9R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-8R!H-R_Ext-9R!H-R
""",
)

entry(
    index = 92,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_N-Sp-11R!H=10R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(832974,'s^-1'), n=1.706, w0=(301000,'J/mol'), E0=(76502.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_N-Sp-11R!H=10R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_N-Sp-11R!H=10R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_N-Sp-11R!H=10R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_N-Sp-11R!H=10R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 93,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.70087e+07,'s^-1'), n=1.13131, w0=(301000,'J/mol'), E0=(69369.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 94,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R_1CbCbfCdCddCtNO2dS2d->Cd",
    kinetics = ArrheniusBM(A=(2.64814e+09,'s^-1'), n=0.577107, w0=(301000,'J/mol'), E0=(92956.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R_1CbCbfCdCddCtNO2dS2d->Cd',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R_1CbCbfCdCddCtNO2dS2d->Cd"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R_1CbCbfCdCddCtNO2dS2d->Cd""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R_1CbCbfCdCddCtNO2dS2d->Cd
""",
)

entry(
    index = 95,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(1.54196e-08,'s^-1'), n=5.82156, w0=(301000,'J/mol'), E0=(42914.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.272160086837,var=6.13952343288,Tref=1000.0,N=112,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R
""",
)

entry(
    index = 96,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-8R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(3.17418e+06,'s^-1'), n=1.92887, w0=(173000,'J/mol'), E0=(52073.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-8R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-8R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-8R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-8R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R
""",
)

entry(
    index = 97,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(8.59707e-11,'s^-1'), n=6.50072, w0=(301000,'J/mol'), E0=(41141.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.303985556088,var=7.32174217794,Tref=1000.0,N=76,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R
""",
)

entry(
    index = 98,
    label = "Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.55909e+10,'s^-1'), n=0.768843, w0=(301000,'J/mol'), E0=(26056.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0165384302366,var=0.278536177751,Tref=1000.0,N=4,correlation='Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R
""",
)

entry(
    index = 99,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_N-1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing",
    kinetics = ArrheniusBM(A=(1.09539e-11,'s^-1'), n=6.15234, w0=(289500,'J/mol'), E0=(28950,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_N-1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_N-1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_N-1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_N-1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing
""",
)

entry(
    index = 100,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(3.89407e+08,'s^-1'), n=0.712299, w0=(301000,'J/mol'), E0=(52807.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0138356665767,var=0.422716881075,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R
""",
)

entry(
    index = 101,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(5.27733e+09,'s^-1'), n=0.764886, w0=(301000,'J/mol'), E0=(95782.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0116873613629,var=0.277931114678,Tref=1000.0,N=4,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R
""",
)

entry(
    index = 102,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(4.96395e+12,'s^-1'), n=-0.169564, w0=(301000,'J/mol'), E0=(82805,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0474411499893,var=8.09696841637,Tref=1000.0,N=54,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R
""",
)

entry(
    index = 103,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Sp-11R!H=10R!H",
    kinetics = ArrheniusBM(A=(2.48001e+07,'s^-1'), n=1.49366, w0=(301000,'J/mol'), E0=(85176.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Sp-11R!H=10R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Sp-11R!H=10R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Sp-11R!H=10R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Sp-11R!H=10R!H
""",
)

entry(
    index = 104,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(4.19248e+06,'s^-1'), n=1.38989, w0=(301000,'J/mol'), E0=(67535.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0047595775559,var=0.0998210737745,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H
""",
)

entry(
    index = 105,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2.74035e+07,'s^-1'), n=1.3475, w0=(301000,'J/mol'), E0=(77314.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0342149876913,var=2.80770041785,Tref=1000.0,N=4,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R
""",
)

entry(
    index = 106,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.81875e+09,'s^-1'), n=0.639476, w0=(301000,'J/mol'), E0=(130295,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R
""",
)

entry(
    index = 107,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(7.60153e+09,'s^-1'), n=0.847466, w0=(301000,'J/mol'), E0=(102456,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 108,
    label = "Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_N-Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(6.91281e+09,'s^-1'), n=0.739964, w0=(301000,'J/mol'), E0=(29283.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00662487607661,var=0.902846725076,Tref=1000.0,N=2,correlation='Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_N-Sp-5R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_N-Sp-5R!H=4R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_N-Sp-5R!H=4R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
""",
)

entry(
    index = 109,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H",
    kinetics = ArrheniusBM(A=(418471,'s^-1'), n=1.57973, w0=(301000,'J/mol'), E0=(47178.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0453119813281,var=1.3254743737,Tref=1000.0,N=6,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H
""",
)

entry(
    index = 110,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H",
    kinetics = ArrheniusBM(A=(2.34791e+11,'s^-1'), n=0.109522, w0=(301000,'J/mol'), E0=(123415,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.000750493707925,var=31.9337412423,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H
""",
)

entry(
    index = 111,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(2.9338e+08,'s^-1'), n=1.01729, w0=(301000,'J/mol'), E0=(99227.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00679543239781,var=0.898201431475,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-Sp-7R!H=6R!H
""",
)

entry(
    index = 112,
    label = "Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-7R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(2.26449e+11,'s^-1'), n=0.549513, w0=(301000,'J/mol'), E0=(32983.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-7R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-7R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-7R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-7R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 113,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_N-Sp-10R!H=9R!H",
    kinetics = ArrheniusBM(A=(5.73921e+07,'s^-1'), n=1.31387, w0=(301000,'J/mol'), E0=(72613.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0376770005177,var=0.302174379157,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_N-Sp-10R!H=9R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_N-Sp-10R!H=9R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_N-Sp-10R!H=9R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_N-Sp-10R!H=9R!H
""",
)

entry(
    index = 114,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(9.77721e+06,'s^-1'), n=1.19044, w0=(301000,'J/mol'), E0=(58332.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0228049345375,var=0.113146869666,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R
""",
)

entry(
    index = 115,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H",
    kinetics = ArrheniusBM(A=(4.90756e+07,'s^-1'), n=1.35118, w0=(301000,'J/mol'), E0=(94965.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0254824178714,var=1.22709619752,Tref=1000.0,N=12,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H
""",
)

entry(
    index = 116,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(6.72426e+10,'s^-1'), n=0.793875, w0=(301000,'J/mol'), E0=(31247.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-5R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-5R!H=4R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-5R!H=4R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-5R!H=4R!H
""",
)

entry(
    index = 117,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.52016e+09,'s^-1'), n=1.12553, w0=(301000,'J/mol'), E0=(52800.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0196429957396,var=0.207451809798,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 118,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R",
    kinetics = ArrheniusBM(A=(5.50971e+07,'s^-1'), n=1.22743, w0=(301000,'J/mol'), E0=(83424.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0019281043182,var=0.905380968993,Tref=1000.0,N=16,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R
""",
)

entry(
    index = 119,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2.93746e+10,'s^-1'), n=0.653208, w0=(301000,'J/mol'), E0=(92075,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0123512561068,var=0.0940409712741,Tref=1000.0,N=4,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R
""",
)

entry(
    index = 120,
    label = "Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(3.48702e+09,'s^-1'), n=0.861005, w0=(301000,'J/mol'), E0=(18389,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 121,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(5.65643e+10,'s^-1'), n=0.724888, w0=(301000,'J/mol'), E0=(32355.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00258215601455,var=0.383373702528,Tref=1000.0,N=2,correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_Sp-5R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_Sp-5R!H=4R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_Sp-5R!H=4R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_Sp-5R!H=4R!H
""",
)

entry(
    index = 122,
    label = "Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.13412e+18,'s^-1'), n=-1.5299, w0=(301000,'J/mol'), E0=(38725.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0925308610699,var=1.37157294376,Tref=1000.0,N=6,correlation='Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R
""",
)

entry(
    index = 123,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(6.14125e+07,'s^-1'), n=1.09578, w0=(301000,'J/mol'), E0=(72043.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 124,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H",
    kinetics = ArrheniusBM(A=(1.44919e+12,'s^-1'), n=0.188238, w0=(301000,'J/mol'), E0=(121505,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0077000434767,var=9.46923774581,Tref=1000.0,N=4,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H
""",
)

entry(
    index = 125,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-5R!H-3R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(5.65684e+09,'s^-1'), n=0.979789, w0=(301000,'J/mol'), E0=(57530.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-5R!H-3R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-5R!H-3R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-5R!H-3R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-5R!H-3R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 126,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(4.79153e+07,'s^-1'), n=0.935703, w0=(301000,'J/mol'), E0=(71044.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00170746638931,var=0.910218836972,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H
""",
)

entry(
    index = 127,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2.4196e+10,'s^-1'), n=0.700935, w0=(301000,'J/mol'), E0=(114944,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R
""",
)

entry(
    index = 128,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-10R!H=9R!H",
    kinetics = ArrheniusBM(A=(5.09553e+06,'s^-1'), n=1.59104, w0=(301000,'J/mol'), E0=(72780.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-10R!H=9R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-10R!H=9R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-10R!H=9R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-10R!H=9R!H
""",
)

entry(
    index = 129,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H",
    kinetics = ArrheniusBM(A=(8.69705e-46,'s^-1'), n=17.0867, w0=(301000,'J/mol'), E0=(-31065.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.931847979634,var=0.38756136112,Tref=1000.0,N=4,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H
""",
)

entry(
    index = 130,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(9.58823e+07,'s^-1'), n=0.928369, w0=(301000,'J/mol'), E0=(53667.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 131,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(5.03756e+09,'s^-1'), n=0.933788, w0=(301000,'J/mol'), E0=(68535.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 132,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.34876e+07,'s^-1'), n=1.26724, w0=(301000,'J/mol'), E0=(66392.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 133,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(7.74024e+22,'s^-1'), n=-3.18142, w0=(301000,'J/mol'), E0=(112384,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.195415710947,var=10.0091516301,Tref=1000.0,N=10,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H
""",
)

entry(
    index = 134,
    label = "Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.62103e+09,'s^-1'), n=0.890474, w0=(301000,'J/mol'), E0=(27785.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00288771046639,var=0.278620290958,Tref=1000.0,N=4,correlation='Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R
""",
)

entry(
    index = 135,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(9.0378e+07,'s^-1'), n=1.42002, w0=(301000,'J/mol'), E0=(22455.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 136,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(2.15559e-45,'s^-1'), n=17.0034, w0=(301000,'J/mol'), E0=(-27345.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.139492573523,var=70.7600809591,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 137,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(3.87548e-17,'s^-1'), n=7.94364, w0=(215667,'J/mol'), E0=(-939.754,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.641376619567,var=1.30085743303,Tref=1000.0,N=3,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R
""",
)

entry(
    index = 138,
    label = "Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(4.78378e+08,'s^-1'), n=1.01906, w0=(301000,'J/mol'), E0=(27963.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 139,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(1.06207e-23,'s^-1'), n=10.3565, w0=(301000,'J/mol'), E0=(-10036.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.822422477659,var=8.34895401244,Tref=1000.0,N=20,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H
""",
)

entry(
    index = 140,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(4.74032e+08,'s^-1'), n=1.165, w0=(301000,'J/mol'), E0=(48566,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H
""",
)

entry(
    index = 141,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.66854e+27,'s^-1'), n=-4.57676, w0=(292087,'J/mol'), E0=(117729,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.302358769327,var=56.9327021357,Tref=1000.0,N=276,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R
""",
)

entry(
    index = 142,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.51879e+09,'s^-1'), n=0.998461, w0=(301000,'J/mol'), E0=(110084,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.023472485103,var=0.181221076232,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R
""",
)

entry(
    index = 143,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(3.00672e+08,'s^-1'), n=0.892026, w0=(301000,'J/mol'), E0=(53272.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 144,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.17445e+14,'s^-1'), n=-0.31385, w0=(301000,'J/mol'), E0=(25781.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0235609088585,var=0.757340187171,Tref=1000.0,N=2,correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H
""",
)

entry(
    index = 145,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(1.29474e-31,'s^-1'), n=12.7006, w0=(276656,'J/mol'), E0=(28106.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.336796163828,var=140.067727749,Tref=1000.0,N=16,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H
""",
)

entry(
    index = 146,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(4.87616e+09,'s^-1'), n=0.384491, w0=(301000,'J/mol'), E0=(56198,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0206834722796,var=0.389433764374,Tref=1000.0,N=8,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R
""",
)

entry(
    index = 147,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_N-Sp-10R!H=9R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(4.20993e+07,'s^-1'), n=1.37738, w0=(301000,'J/mol'), E0=(72060.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_N-Sp-10R!H=9R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_N-Sp-10R!H=9R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_N-Sp-10R!H=9R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_N-Sp-10R!H=9R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 148,
    label = "Root_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R",
    kinetics = ArrheniusBM(A=(1.47469e+09,'s^-1'), n=0.897907, w0=(301000,'J/mol'), E0=(17683.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0085788317307,var=0.0427099832131,Tref=1000.0,N=2,correlation='Root_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R
""",
)

entry(
    index = 149,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H",
    kinetics = ArrheniusBM(A=(5.2862e+13,'s^-1'), n=-0.58297, w0=(301000,'J/mol'), E0=(91236,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0984357336127,var=0.975072093701,Tref=1000.0,N=28,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H
""",
)

entry(
    index = 150,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(2.81715e+09,'s^-1'), n=1.00588, w0=(301000,'J/mol'), E0=(115793,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 151,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing",
    kinetics = ArrheniusBM(A=(8.29899e+13,'s^-1'), n=-0.82741, w0=(301000,'J/mol'), E0=(96628.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0487602626849,var=17.4459713879,Tref=1000.0,N=10,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing
""",
)

entry(
    index = 152,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R",
    kinetics = ArrheniusBM(A=(3.03737e+17,'s^-1'), n=-1.64646, w0=(301000,'J/mol'), E0=(2422.16,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R
""",
)

entry(
    index = 153,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.66057e+07,'s^-1'), n=0.998244, w0=(301000,'J/mol'), E0=(51720.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 154,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(3.8901e+06,'s^-1'), n=1.39894, w0=(301000,'J/mol'), E0=(52323.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0157499308755,var=1.28540911459,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 155,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_Sp-10R!H=9R!H",
    kinetics = ArrheniusBM(A=(2.30785e+07,'s^-1'), n=1.30832, w0=(301000,'J/mol'), E0=(82520.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0286839546919,var=0.297475066548,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_Sp-10R!H=9R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_Sp-10R!H=9R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_Sp-10R!H=9R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_Sp-10R!H=9R!H
""",
)

entry(
    index = 156,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H",
    kinetics = ArrheniusBM(A=(3.18621e+12,'s^-1'), n=0.237566, w0=(301000,'J/mol'), E0=(23525.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0226050216685,var=0.883507842346,Tref=1000.0,N=2,correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H
""",
)

entry(
    index = 157,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2.539e+06,'s^-1'), n=1.27235, w0=(301000,'J/mol'), E0=(68621.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-3R!H-R
""",
)

entry(
    index = 158,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(1.6485e+09,'s^-1'), n=1.18282, w0=(301000,'J/mol'), E0=(55779.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-8R!H=7R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-8R!H=7R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-8R!H=7R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-8R!H=7R!H
""",
)

entry(
    index = 159,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(8.98153e+10,'s^-1'), n=0.6286, w0=(301000,'J/mol'), E0=(117812,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0119819478448,var=0.896781861693,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H
""",
)

entry(
    index = 160,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R_Int-10R!H-4R!H",
    kinetics = ArrheniusBM(A=(2020.89,'s^-1'), n=1.99107, w0=(173000,'J/mol'), E0=(51582.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R_Int-10R!H-4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R_Int-10R!H-4R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R_Int-10R!H-4R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R_Int-10R!H-4R!H
""",
)

entry(
    index = 161,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing",
    kinetics = ArrheniusBM(A=(2.15493e-05,'s^-1'), n=4.91505, w0=(301000,'J/mol'), E0=(48563.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.223689429516,var=6.92359491136,Tref=1000.0,N=168,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing
""",
)

entry(
    index = 162,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(1.41788e+09,'s^-1'), n=1.18764, w0=(301000,'J/mol'), E0=(68866.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Sp-9R!H=8R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Sp-9R!H=8R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Sp-9R!H=8R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Sp-9R!H=8R!H
""",
)

entry(
    index = 163,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(6.51062e+06,'s^-1'), n=1.46273, w0=(301000,'J/mol'), E0=(63147.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 164,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.45374e-05,'s^-1'), n=4.84791, w0=(301000,'J/mol'), E0=(-158834,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.104849552463,var=37.2271304507,Tref=1000.0,N=9,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Ext-5R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Ext-5R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Ext-5R!H-R
""",
)

entry(
    index = 165,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R_1CbCbfCdCddCtNO2dS2d->Cd_N-3R!H-inRing",
    kinetics = ArrheniusBM(A=(2.68875e+12,'s^-1'), n=-0.132778, w0=(301000,'J/mol'), E0=(6528.15,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R_1CbCbfCdCddCtNO2dS2d->Cd_N-3R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R_1CbCbfCdCddCtNO2dS2d->Cd_N-3R!H-inRing"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R_1CbCbfCdCddCtNO2dS2d->Cd_N-3R!H-inRing""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R_1CbCbfCdCddCtNO2dS2d->Cd_N-3R!H-inRing
""",
)

entry(
    index = 166,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(4.64326e+17,'s^-1'), n=-1.29869, w0=(301000,'J/mol'), E0=(13643.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.113361113531,var=0.708001102605,Tref=1000.0,N=2,correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 167,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.04489e+19,'s^-1'), n=-1.79349, w0=(301000,'J/mol'), E0=(-1452.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 168,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H",
    kinetics = ArrheniusBM(A=(1.03287e+08,'s^-1'), n=0.623759, w0=(301000,'J/mol'), E0=(55964.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00908558578876,var=0.97937239251,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H
""",
)

entry(
    index = 169,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R_N-1CbCbfCdCddCtNO2dS2d->Cd",
    kinetics = ArrheniusBM(A=(84.2695,'s^-1'), n=2.56003, w0=(173000,'J/mol'), E0=(45408,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R_N-1CbCbfCdCddCtNO2dS2d->Cd',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R_N-1CbCbfCdCddCtNO2dS2d->Cd"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R_N-1CbCbfCdCddCtNO2dS2d->Cd""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R_N-1CbCbfCdCddCtNO2dS2d->Cd
""",
)

entry(
    index = 170,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Ext-3R!H-R_N-Sp-9R!H=7R!H",
    kinetics = ArrheniusBM(A=(3.69697e+06,'s^-1'), n=1.35261, w0=(301000,'J/mol'), E0=(73790,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Ext-3R!H-R_N-Sp-9R!H=7R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Ext-3R!H-R_N-Sp-9R!H=7R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Ext-3R!H-R_N-Sp-9R!H=7R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Ext-3R!H-R_N-Sp-9R!H=7R!H
""",
)

entry(
    index = 171,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-5R!H-3R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.81448e+10,'s^-1'), n=0.816743, w0=(301000,'J/mol'), E0=(43656.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-5R!H-3R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-5R!H-3R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-5R!H-3R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-5R!H-3R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 172,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_6R!H-inRing_Ext-6R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(1.24399e+09,'s^-1'), n=0.673081, w0=(301000,'J/mol'), E0=(208763,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_6R!H-inRing_Ext-6R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_6R!H-inRing_Ext-6R!H-R_Ext-6R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_6R!H-inRing_Ext-6R!H-R_Ext-6R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_6R!H-inRing_Ext-6R!H-R_Ext-6R!H-R
""",
)

entry(
    index = 173,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(2.69191e+08,'s^-1'), n=1.11496, w0=(301000,'J/mol'), E0=(134442,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 174,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_4R!H-inRing_N-Sp-6R!H-3R!H",
    kinetics = ArrheniusBM(A=(117356,'s^-1'), n=1.93463, w0=(301000,'J/mol'), E0=(30100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_4R!H-inRing_N-Sp-6R!H-3R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_4R!H-inRing_N-Sp-6R!H-3R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_4R!H-inRing_N-Sp-6R!H-3R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_4R!H-inRing_N-Sp-6R!H-3R!H
""",
)

entry(
    index = 175,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H",
    kinetics = ArrheniusBM(A=(2.03927e+09,'s^-1'), n=0.524963, w0=(301000,'J/mol'), E0=(73829.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0305949079908,var=1.08568867803,Tref=1000.0,N=8,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H
""",
)

entry(
    index = 176,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.42183e+07,'s^-1'), n=1.33722, w0=(301000,'J/mol'), E0=(87801.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0129706526665,var=0.916187938276,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_N-Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_N-Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_N-Sp-7R!H=6R!H
""",
)

entry(
    index = 177,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(3.71041e+06,'s^-1'), n=1.1928, w0=(301000,'J/mol'), E0=(68381.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0146291288826,var=0.120203203064,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H
""",
)

entry(
    index = 178,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Sp-8R!H=3R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2.05873e+98,'s^-1'), n=-25.2701, w0=(173000,'J/mol'), E0=(253674,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=5.20248366311,var=80.5127203578,Tref=1000.0,N=3,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Sp-8R!H=3R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Sp-8R!H=3R!H_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Sp-8R!H=3R!H_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Sp-8R!H=3R!H_Ext-3R!H-R
""",
)

entry(
    index = 179,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_N-Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(2.27409e+08,'s^-1'), n=1.28666, w0=(301000,'J/mol'), E0=(61107.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_N-Sp-9R!H=8R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_N-Sp-9R!H=8R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_N-Sp-9R!H=8R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_N-Sp-9R!H=8R!H
""",
)

entry(
    index = 180,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(3.39414e+08,'s^-1'), n=1.20094, w0=(301000,'J/mol'), E0=(98972,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 181,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-11R!H=10R!H",
    kinetics = ArrheniusBM(A=(8.15116e+06,'s^-1'), n=1.45423, w0=(301000,'J/mol'), E0=(79258.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-11R!H=10R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-11R!H=10R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-11R!H=10R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-11R!H=10R!H
""",
)

entry(
    index = 182,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Sp-8R!H=3R!H",
    kinetics = ArrheniusBM(A=(4.7892e+88,'s^-1'), n=-22.4447, w0=(173000,'J/mol'), E0=(212687,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.16098903495,var=49.3323464652,Tref=1000.0,N=5,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Sp-8R!H=3R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Sp-8R!H=3R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Sp-8R!H=3R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Sp-8R!H=3R!H
""",
)

entry(
    index = 183,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(6.13896e-79,'s^-1'), n=26.6996, w0=(299562,'J/mol'), E0=(-44588.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.08768232145,var=84.8790924367,Tref=1000.0,N=8,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R
""",
)

entry(
    index = 184,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-4R!H-3C",
    kinetics = ArrheniusBM(A=(2.26631e+27,'s^-1'), n=-4.4534, w0=(295250,'J/mol'), E0=(58956.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.68275207484,var=3.97440174635,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-4R!H-3C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-4R!H-3C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-4R!H-3C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-4R!H-3C
""",
)

entry(
    index = 185,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-4R!H-3C_N-1CbCbfCdCddCtNO2dS2d->Cd",
    kinetics = ArrheniusBM(A=(9.60866e+11,'s^-1'), n=-0.0113023, w0=(289500,'J/mol'), E0=(9276.86,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-4R!H-3C_N-1CbCbfCdCddCtNO2dS2d->Cd',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-4R!H-3C_N-1CbCbfCdCddCtNO2dS2d->Cd"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-4R!H-3C_N-1CbCbfCdCddCtNO2dS2d->Cd""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-4R!H-3C_N-1CbCbfCdCddCtNO2dS2d->Cd
""",
)

entry(
    index = 186,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(2.76607e+06,'s^-1'), n=1.23765, w0=(301000,'J/mol'), E0=(69539.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 187,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H",
    kinetics = ArrheniusBM(A=(2.4927e+09,'s^-1'), n=0.656206, w0=(301000,'J/mol'), E0=(93432.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00698654424256,var=0.0395109783874,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H
""",
)

entry(
    index = 188,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.56127e+08,'s^-1'), n=1.31436, w0=(301000,'J/mol'), E0=(58476.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 189,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(5.46039e+07,'s^-1'), n=0.900423, w0=(301000,'J/mol'), E0=(72962.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 190,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1CbCdCt->Cd_N-Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(8.72043e+53,'s^-1'), n=-12.5851, w0=(301000,'J/mol'), E0=(30100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1CbCdCt->Cd_N-Sp-6R!H-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1CbCdCt->Cd_N-Sp-6R!H-5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1CbCdCt->Cd_N-Sp-6R!H-5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1CbCdCt->Cd_N-Sp-6R!H-5R!H
""",
)

entry(
    index = 191,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.16509e+08,'s^-1'), n=0.893304, w0=(301000,'J/mol'), E0=(51178.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 192,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(6.13552e+07,'s^-1'), n=0.976531, w0=(301000,'J/mol'), E0=(51838,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00898838772403,var=0.0260720334032,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H
""",
)

entry(
    index = 193,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(1.82129e+08,'s^-1'), n=1.32991, w0=(301000,'J/mol'), E0=(47836.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-8R!H=7R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-8R!H=7R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-8R!H=7R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-8R!H=7R!H
""",
)

entry(
    index = 194,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_N-Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(2.25099e+07,'s^-1'), n=1.49259, w0=(301000,'J/mol'), E0=(60299.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0156239403181,var=0.255912306384,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_N-Sp-9R!H=8R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_N-Sp-9R!H=8R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_N-Sp-9R!H=8R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_N-Sp-9R!H=8R!H
""",
)

entry(
    index = 195,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H",
    kinetics = ArrheniusBM(A=(7.4818e+11,'s^-1'), n=0.204596, w0=(301000,'J/mol'), E0=(33344.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0192954258963,var=0.469145232746,Tref=1000.0,N=2,correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H
""",
)

entry(
    index = 196,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Sp-8R!H=3R!H_Int-8R!H-2COCSCbCbfCdCtN_Ext-8R!H-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(1.31696e+35,'s^-1'), n=-6.78135, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Sp-8R!H=3R!H_Int-8R!H-2COCSCbCbfCdCtN_Ext-8R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Sp-8R!H=3R!H_Int-8R!H-2COCSCbCbfCdCtN_Ext-8R!H-R_Ext-9R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Sp-8R!H=3R!H_Int-8R!H-2COCSCbCbfCdCtN_Ext-8R!H-R_Ext-9R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Sp-8R!H=3R!H_Int-8R!H-2COCSCbCbfCdCtN_Ext-8R!H-R_Ext-9R!H-R
""",
)

entry(
    index = 197,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Sp-9R!H=7R!H",
    kinetics = ArrheniusBM(A=(1.55508e+06,'s^-1'), n=1.54337, w0=(301000,'J/mol'), E0=(82994.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Sp-9R!H=7R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Sp-9R!H=7R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Sp-9R!H=7R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Sp-9R!H=7R!H
""",
)

entry(
    index = 198,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(3.2121e+06,'s^-1'), n=1.30539, w0=(301000,'J/mol'), E0=(65857.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.014756450661,var=0.0269636052236,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Sp-7R!H=6R!H
""",
)

entry(
    index = 199,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2.33239e+08,'s^-1'), n=0.850529, w0=(301000,'J/mol'), E0=(54531.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-3R!H-R
""",
)

entry(
    index = 200,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(9.79165e-17,'s^-1'), n=8.34357, w0=(301000,'J/mol'), E0=(25285.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.453821461645,var=32.0785981744,Tref=1000.0,N=10,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H
""",
)

entry(
    index = 201,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-2COCSCbCbfCdCtN-R",
    kinetics = ArrheniusBM(A=(2.78907e+09,'s^-1'), n=0.780275, w0=(173000,'J/mol'), E0=(42706,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-2COCSCbCbfCdCtN-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-2COCSCbCbfCdCtN-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-2COCSCbCbfCdCtN-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-2COCSCbCbfCdCtN-R
""",
)

entry(
    index = 202,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.97328e+08,'s^-1'), n=1.30004, w0=(301000,'J/mol'), E0=(64859.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 203,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-4R!H-3C_1CbCbfCdCddCtNO2dS2d->Cd",
    kinetics = ArrheniusBM(A=(4.19804e-32,'s^-1'), n=13.0342, w0=(301000,'J/mol'), E0=(-48256.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-4R!H-3C_1CbCbfCdCddCtNO2dS2d->Cd',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-4R!H-3C_1CbCbfCdCddCtNO2dS2d->Cd"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-4R!H-3C_1CbCbfCdCddCtNO2dS2d->Cd""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-4R!H-3C_1CbCbfCdCddCtNO2dS2d->Cd
""",
)

entry(
    index = 204,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.88725e+06,'s^-1'), n=1.37762, w0=(301000,'J/mol'), E0=(78544.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0278133021874,var=9.16300606714,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Ext-3R!H-R
""",
)

entry(
    index = 205,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(4.70914e+09,'s^-1'), n=0.452796, w0=(301000,'J/mol'), E0=(55818.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0087754154228,var=0.415746023754,Tref=1000.0,N=4,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R
""",
)

entry(
    index = 206,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Sp-8R!H=3R!H_Ext-3R!H-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(2.66198e+36,'s^-1'), n=-7.14819, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Sp-8R!H=3R!H_Ext-3R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Sp-8R!H=3R!H_Ext-3R!H-R_Ext-9R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Sp-8R!H=3R!H_Ext-3R!H-R_Ext-9R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Sp-8R!H=3R!H_Ext-3R!H-R_Ext-9R!H-R
""",
)

entry(
    index = 207,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(4.74228e+09,'s^-1'), n=0.83475, w0=(301000,'J/mol'), E0=(97871.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00380563012328,var=0.195428296989,Tref=1000.0,N=8,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R
""",
)

entry(
    index = 208,
    label = "Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_Sp-8R!H=4R!H",
    kinetics = ArrheniusBM(A=(4.49192e+09,'s^-1'), n=0.892031, w0=(301000,'J/mol'), E0=(24706.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0217857908368,var=0.175689291474,Tref=1000.0,N=2,correlation='Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_Sp-8R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_Sp-8R!H=4R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_Sp-8R!H=4R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_Sp-8R!H=4R!H
""",
)

entry(
    index = 209,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H",
    kinetics = ArrheniusBM(A=(1.80758e-47,'s^-1'), n=17.2487, w0=(301000,'J/mol'), E0=(-35627.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.11794321149,var=72.9900294572,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H
""",
)

entry(
    index = 210,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(4.59061e+13,'s^-1'), n=-0.439145, w0=(301000,'J/mol'), E0=(92484.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0451719171818,var=14.2297803646,Tref=1000.0,N=20,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R
""",
)

entry(
    index = 211,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(4.90254e+08,'s^-1'), n=1.10533, w0=(301000,'J/mol'), E0=(63270.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0172847031443,var=0.282230163359,Tref=1000.0,N=4,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R
""",
)

entry(
    index = 212,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(7.76068e+07,'s^-1'), n=1.27765, w0=(301000,'J/mol'), E0=(68819.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 213,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(4.13606e+07,'s^-1'), n=1.25715, w0=(301000,'J/mol'), E0=(66864.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 214,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(4.26783e+09,'s^-1'), n=1.0184, w0=(301000,'J/mol'), E0=(56559.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H
""",
)

entry(
    index = 215,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(3.57826e+06,'s^-1'), n=1.41797, w0=(301000,'J/mol'), E0=(68788.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 216,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.84884e+07,'s^-1'), n=1.14497, w0=(301000,'J/mol'), E0=(67633.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00149971620472,var=0.924749013074,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_N-Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_N-Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_N-Sp-7R!H=6R!H
""",
)

entry(
    index = 217,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.13582e+10,'s^-1'), n=0.838348, w0=(301000,'J/mol'), E0=(61419,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.018877350294,var=0.882009688037,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H
""",
)

entry(
    index = 218,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.39477e+07,'s^-1'), n=1.05845, w0=(301000,'J/mol'), E0=(69752.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0090555048337,var=0.277939639894,Tref=1000.0,N=4,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R
""",
)

entry(
    index = 219,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(8.56041e+08,'s^-1'), n=1.1711, w0=(301000,'J/mol'), E0=(67410.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00454828630062,var=0.290508262288,Tref=1000.0,N=4,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H
""",
)

entry(
    index = 220,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.52806e+07,'s^-1'), n=1.33269, w0=(301000,'J/mol'), E0=(97674.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 221,
    label = "Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-8R!H=4R!H",
    kinetics = ArrheniusBM(A=(5.41839e+10,'s^-1'), n=0.645569, w0=(301000,'J/mol'), E0=(27412.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00763995500572,var=0.888739609127,Tref=1000.0,N=2,correlation='Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-8R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-8R!H=4R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-8R!H=4R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-8R!H=4R!H
""",
)

entry(
    index = 222,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R_1CbCbfCdCddCtNO2dS2d->Cd_3R!H-inRing",
    kinetics = ArrheniusBM(A=(5.59922e+18,'s^-1'), n=-1.76138, w0=(301000,'J/mol'), E0=(49790.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R_1CbCbfCdCddCtNO2dS2d->Cd_3R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R_1CbCbfCdCddCtNO2dS2d->Cd_3R!H-inRing"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R_1CbCbfCdCddCtNO2dS2d->Cd_3R!H-inRing""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R_1CbCbfCdCddCtNO2dS2d->Cd_3R!H-inRing
""",
)

entry(
    index = 223,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1365.19,'s^-1'), n=1.78173, w0=(173000,'J/mol'), E0=(51745.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R_Ext-4R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R_Ext-4R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R_Ext-4R!H-R
""",
)

entry(
    index = 224,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C",
    kinetics = ArrheniusBM(A=(4.65246e+37,'s^-1'), n=-7.5315, w0=(300042,'J/mol'), E0=(91834.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.136031326543,var=17.7731273986,Tref=1000.0,N=12,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C
""",
)

entry(
    index = 225,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H",
    kinetics = ArrheniusBM(A=(2.25415e+07,'s^-1'), n=1.49014, w0=(301000,'J/mol'), E0=(82055.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H
""",
)

entry(
    index = 226,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(8.72402e+10,'s^-1'), n=0.544204, w0=(301000,'J/mol'), E0=(104566,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-3R!H-R
""",
)

entry(
    index = 227,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(5.66592e+07,'s^-1'), n=1.13949, w0=(301000,'J/mol'), E0=(66545.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00865394733778,var=0.905927994702,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H
""",
)

entry(
    index = 228,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Sp-8R!H=3R!H_Ext-3R!H-R_Int-8R!H-2COCSCbCbfCdCtN",
    kinetics = ArrheniusBM(A=(6.4298e+32,'s^-1'), n=-5.98869, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Sp-8R!H=3R!H_Ext-3R!H-R_Int-8R!H-2COCSCbCbfCdCtN',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Sp-8R!H=3R!H_Ext-3R!H-R_Int-8R!H-2COCSCbCbfCdCtN"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Sp-8R!H=3R!H_Ext-3R!H-R_Int-8R!H-2COCSCbCbfCdCtN""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Sp-8R!H=3R!H_Ext-3R!H-R_Int-8R!H-2COCSCbCbfCdCtN
""",
)

entry(
    index = 229,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(2.57416e+06,'s^-1'), n=1.37337, w0=(301000,'J/mol'), E0=(79305.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0168462753597,var=1.41723299763,Tref=1000.0,N=4,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R
""",
)

entry(
    index = 230,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(5.93408e+06,'s^-1'), n=1.01666, w0=(301000,'J/mol'), E0=(50427.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00628998662734,var=0.0184006131269,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Sp-7R!H=6R!H
""",
)

entry(
    index = 231,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(5.38806e+07,'s^-1'), n=1.13227, w0=(301000,'J/mol'), E0=(70153.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00783644090897,var=0.915493980516,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H
""",
)

entry(
    index = 232,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H",
    kinetics = ArrheniusBM(A=(3.33364e+09,'s^-1'), n=0.860762, w0=(301000,'J/mol'), E0=(91480.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0154054442002,var=1.60732501143,Tref=1000.0,N=6,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H
""",
)

entry(
    index = 233,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1CbCdCt->Cd",
    kinetics = ArrheniusBM(A=(2.28374e-69,'s^-1'), n=23.7223, w0=(301000,'J/mol'), E0=(-20030,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.164003095881,var=158.434997805,Tref=1000.0,N=7,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1CbCdCt->Cd',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1CbCdCt->Cd"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1CbCdCt->Cd""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1CbCdCt->Cd
""",
)

entry(
    index = 234,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H",
    kinetics = ArrheniusBM(A=(7.33862e-23,'s^-1'), n=9.8433, w0=(301000,'J/mol'), E0=(24346.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.283635471647,var=32.7717308889,Tref=1000.0,N=11,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H
""",
)

entry(
    index = 235,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(8.22129e+15,'s^-1'), n=-1.19534, w0=(301000,'J/mol'), E0=(97112.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.130228411315,var=0.978124686752,Tref=1000.0,N=24,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R
""",
)

entry(
    index = 236,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2.46429e+09,'s^-1'), n=0.963789, w0=(301000,'J/mol'), E0=(55665.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0282625468553,var=0.208990193784,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R
""",
)

entry(
    index = 237,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R",
    kinetics = ArrheniusBM(A=(6.30297e+30,'s^-1'), n=-5.27279, w0=(301000,'J/mol'), E0=(63935.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.280728442429,var=3.20511796077,Tref=1000.0,N=12,correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R
""",
)

entry(
    index = 238,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_Sp-9R!H=8R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(3.29372e+07,'s^-1'), n=1.58534, w0=(301000,'J/mol'), E0=(68562.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_Sp-9R!H=8R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_Sp-9R!H=8R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_Sp-9R!H=8R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_Sp-9R!H=8R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 239,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.82107e+10,'s^-1'), n=0.642023, w0=(301000,'J/mol'), E0=(97096,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00456292909501,var=0.894848384275,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H
""",
)

entry(
    index = 240,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_Sp-11R!H=10R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.83739e+06,'s^-1'), n=1.74551, w0=(301000,'J/mol'), E0=(85627.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_Sp-11R!H=10R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_Sp-11R!H=10R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_Sp-11R!H=10R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_Sp-11R!H=10R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 241,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(305062,'s^-1'), n=1.68267, w0=(301000,'J/mol'), E0=(56355.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0391404553518,var=0.459217764594,Tref=1000.0,N=4,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H
""",
)

entry(
    index = 242,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R_1CbCbfCdCddCtNO2dS2d->Cd",
    kinetics = ArrheniusBM(A=(8.97612e+11,'s^-1'), n=0.112312, w0=(301000,'J/mol'), E0=(20249.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.527956114167,var=0.14132877534,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R_1CbCbfCdCddCtNO2dS2d->Cd',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R_1CbCbfCdCddCtNO2dS2d->Cd"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R_1CbCbfCdCddCtNO2dS2d->Cd""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R_1CbCbfCdCddCtNO2dS2d->Cd
""",
)

entry(
    index = 243,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.04492e+10,'s^-1'), n=0.864341, w0=(301000,'J/mol'), E0=(93387.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 244,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_N-Sp-9R!H=7R!H",
    kinetics = ArrheniusBM(A=(416276,'s^-1'), n=1.57243, w0=(301000,'J/mol'), E0=(74443.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_N-Sp-9R!H=7R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_N-Sp-9R!H=7R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_N-Sp-9R!H=7R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_N-Sp-9R!H=7R!H
""",
)

entry(
    index = 245,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.07107e+06,'s^-1'), n=1.60477, w0=(301000,'J/mol'), E0=(86493.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 246,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-5R!H-3R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(8.8006e+09,'s^-1'), n=0.779569, w0=(301000,'J/mol'), E0=(55768.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-5R!H-3R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-5R!H-3R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-5R!H-3R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-5R!H-3R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 247,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(5.9643e+09,'s^-1'), n=0.781488, w0=(301000,'J/mol'), E0=(73942.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 248,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Ext-3R!H-R_Sp-9R!H=7R!H",
    kinetics = ArrheniusBM(A=(1.56345e+06,'s^-1'), n=1.34051, w0=(301000,'J/mol'), E0=(83730.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Ext-3R!H-R_Sp-9R!H=7R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Ext-3R!H-R_Sp-9R!H=7R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Ext-3R!H-R_Sp-9R!H=7R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Ext-3R!H-R_Sp-9R!H=7R!H
""",
)

entry(
    index = 249,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1CbCdCt->Cd_Ext-3R!H-R_1Cd-inRing",
    kinetics = ArrheniusBM(A=(8.75886e+10,'s^-1'), n=0.456197, w0=(301000,'J/mol'), E0=(184034,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1CbCdCt->Cd_Ext-3R!H-R_1Cd-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1CbCdCt->Cd_Ext-3R!H-R_1Cd-inRing"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1CbCdCt->Cd_Ext-3R!H-R_1Cd-inRing""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1CbCdCt->Cd_Ext-3R!H-R_1Cd-inRing
""",
)

entry(
    index = 250,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1CbCdCt->Cd_Ext-3R!H-R_N-1Cd-inRing",
    kinetics = ArrheniusBM(A=(3.10438e+07,'s^-1'), n=1.38388, w0=(301000,'J/mol'), E0=(111129,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-5.21458961055,var=61.8007019385,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1CbCdCt->Cd_Ext-3R!H-R_N-1Cd-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1CbCdCt->Cd_Ext-3R!H-R_N-1Cd-inRing"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1CbCdCt->Cd_Ext-3R!H-R_N-1Cd-inRing""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1CbCdCt->Cd_Ext-3R!H-R_N-1Cd-inRing
""",
)

entry(
    index = 251,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(9.45402e+06,'s^-1'), n=1.3036, w0=(301000,'J/mol'), E0=(64694.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0182495526882,var=0.031621209156,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H
""",
)

entry(
    index = 252,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(5.3699e+11,'s^-1'), n=0.288558, w0=(301000,'J/mol'), E0=(33704.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00113744600709,var=0.300398868378,Tref=1000.0,N=4,correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R
""",
)

entry(
    index = 253,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.94897e+08,'s^-1'), n=1.10751, w0=(301000,'J/mol'), E0=(69148.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00486310490537,var=0.91244956611,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H
""",
)

entry(
    index = 254,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(0.0159876,'s^-1'), n=3.72377, w0=(301000,'J/mol'), E0=(30100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 255,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_N-Sp-11R!H=10R!H",
    kinetics = ArrheniusBM(A=(828129,'s^-1'), n=1.69919, w0=(301000,'J/mol'), E0=(75159.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0189948480144,var=0.0796322992423,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_N-Sp-11R!H=10R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_N-Sp-11R!H=10R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_N-Sp-11R!H=10R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_N-Sp-11R!H=10R!H
""",
)

entry(
    index = 256,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.62953e+08,'s^-1'), n=1.09762, w0=(301000,'J/mol'), E0=(66776.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 257,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(6.26916e+07,'s^-1'), n=1.42904, w0=(301000,'J/mol'), E0=(64261.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00936412400085,var=0.106607713333,Tref=1000.0,N=4,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H
""",
)

entry(
    index = 258,
    label = "Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(8.66219e+09,'s^-1'), n=0.692392, w0=(301000,'J/mol'), E0=(31276.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 259,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(6.29056e+09,'s^-1'), n=0.895891, w0=(301000,'J/mol'), E0=(114911,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00208867415214,var=0.180797457495,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H
""",
)

entry(
    index = 260,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H",
    kinetics = ArrheniusBM(A=(6.61966e+11,'s^-1'), n=0.302778, w0=(301000,'J/mol'), E0=(34592.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00512746197779,var=0.888109256054,Tref=1000.0,N=2,correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H
""",
)

entry(
    index = 261,
    label = "Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(3.02583e+08,'s^-1'), n=1.07046, w0=(301000,'J/mol'), E0=(26087.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00800035988506,var=0.119896622343,Tref=1000.0,N=2,correlation='Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_Sp-5R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_Sp-5R!H=4R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_Sp-5R!H=4R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_Sp-5R!H=4R!H
""",
)

entry(
    index = 262,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_N-Sp-9R!H=8R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(5.67892e+06,'s^-1'), n=1.67527, w0=(301000,'J/mol'), E0=(60852,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_N-Sp-9R!H=8R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_N-Sp-9R!H=8R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_N-Sp-9R!H=8R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_N-Sp-9R!H=8R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 263,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.71229e+09,'s^-1'), n=0.981629, w0=(301000,'J/mol'), E0=(64625.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0097411802046,var=0.898654021531,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H
""",
)

entry(
    index = 264,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd",
    kinetics = ArrheniusBM(A=(3.55177e-70,'s^-1'), n=23.9742, w0=(299722,'J/mol'), E0=(-19922.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.13304619027,var=95.2745313914,Tref=1000.0,N=9,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd
""",
)

entry(
    index = 265,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(4.06254e+07,'s^-1'), n=1.30244, w0=(301000,'J/mol'), E0=(79387.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 266,
    label = "Root_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(6.54433e+14,'s^-1'), n=-0.597846, w0=(301000,'J/mol'), E0=(34365.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0586136464877,var=1.84103045667,Tref=1000.0,N=18,correlation='Root_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 267,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(4.30759e+07,'s^-1'), n=1.24498, w0=(301000,'J/mol'), E0=(68930.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 268,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.60942e+07,'s^-1'), n=0.904994, w0=(301000,'J/mol'), E0=(55545.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R
""",
)

entry(
    index = 269,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-8R!H-R_Ext-2COCSCbCbfCdCtN-R",
    kinetics = ArrheniusBM(A=(1.78509e+09,'s^-1'), n=0.977465, w0=(173000,'J/mol'), E0=(45627.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00412639431896,var=1.54129235617,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-8R!H-R_Ext-2COCSCbCbfCdCtN-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-8R!H-R_Ext-2COCSCbCbfCdCtN-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-8R!H-R_Ext-2COCSCbCbfCdCtN-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-8R!H-R_Ext-2COCSCbCbfCdCtN-R
""",
)

entry(
    index = 270,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_6R!H-inRing_N-3R!H-inRing",
    kinetics = ArrheniusBM(A=(255050,'s^-1'), n=1.99365, w0=(301000,'J/mol'), E0=(49847.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_6R!H-inRing_N-3R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_6R!H-inRing_N-3R!H-inRing"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_6R!H-inRing_N-3R!H-inRing""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_6R!H-inRing_N-3R!H-inRing
""",
)

entry(
    index = 271,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_Sp-10R!H=9R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.70365e+07,'s^-1'), n=1.37105, w0=(301000,'J/mol'), E0=(81987.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_Sp-10R!H=9R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_Sp-10R!H=9R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_Sp-10R!H=9R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_Sp-10R!H=9R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 272,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(5.87717e+11,'s^-1'), n=0.308335, w0=(301000,'J/mol'), E0=(37038.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 273,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(8.31673e+06,'s^-1'), n=1.21837, w0=(301000,'J/mol'), E0=(59589.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 274,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-5R!H-3R!H",
    kinetics = ArrheniusBM(A=(1.46963e+09,'s^-1'), n=0.684673, w0=(301000,'J/mol'), E0=(57962.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-5R!H-3R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-5R!H-3R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-5R!H-3R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-5R!H-3R!H
""",
)

entry(
    index = 275,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.47727e+08,'s^-1'), n=0.893945, w0=(301000,'J/mol'), E0=(62920.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R
""",
)

entry(
    index = 276,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.88125e+07,'s^-1'), n=1.41861, w0=(301000,'J/mol'), E0=(84294.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00173937034587,var=0.00378539309478,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 277,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(8.49969e+08,'s^-1'), n=1.26849, w0=(301000,'J/mol'), E0=(30477.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 278,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-5R!H-3R!H",
    kinetics = ArrheniusBM(A=(3.00919e+08,'s^-1'), n=0.924129, w0=(301000,'J/mol'), E0=(57387,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-5R!H-3R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-5R!H-3R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-5R!H-3R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-5R!H-3R!H
""",
)

entry(
    index = 279,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(1.88408e+13,'s^-1'), n=-0.0350012, w0=(301000,'J/mol'), E0=(24615.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00396658302251,var=0.315435001829,Tref=1000.0,N=4,correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R
""",
)

entry(
    index = 280,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(3.59319e+07,'s^-1'), n=0.925366, w0=(301000,'J/mol'), E0=(51234.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 281,
    label = "Root",
    kinetics = ArrheniusBM(A=(7.65715e+27,'s^-1'), n=-4.75994, w0=(293622,'J/mol'), E0=(115134,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.315217236417,var=56.8410221082,Tref=1000.0,N=335,correlation='Root',), comment="""BM rule fitted to 2 training reactions at node Root"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root
""",
)

entry(
    index = 282,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H",
    kinetics = ArrheniusBM(A=(3.00581e-12,'s^-1'), n=6.70499, w0=(301000,'J/mol'), E0=(40912,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.39493856556,var=18.3965565917,Tref=1000.0,N=5,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H
""",
)

entry(
    index = 283,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H",
    kinetics = ArrheniusBM(A=(1.28538e+07,'s^-1'), n=1.4338, w0=(301000,'J/mol'), E0=(76391.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0271981691831,var=0.277583564315,Tref=1000.0,N=4,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H
""",
)

entry(
    index = 284,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(6.77931e+06,'s^-1'), n=0.892299, w0=(301000,'J/mol'), E0=(65430.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R
""",
)

entry(
    index = 285,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.36401e+08,'s^-1'), n=1.23273, w0=(301000,'J/mol'), E0=(61892.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0235720133546,var=0.172207715652,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_Sp-7R!H=6R!H
""",
)

entry(
    index = 286,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_N-1CbCdCt->Cd",
    kinetics = ArrheniusBM(A=(7.1731e-109,'s^-1'), n=36.0112, w0=(289500,'J/mol'), E0=(28950,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_N-1CbCdCt->Cd',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_N-1CbCdCt->Cd"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_N-1CbCdCt->Cd""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_N-1CbCdCt->Cd
""",
)

entry(
    index = 287,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.5067e+07,'s^-1'), n=1.31093, w0=(301000,'J/mol'), E0=(89655,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 288,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.45532e+09,'s^-1'), n=0.89415, w0=(301000,'J/mol'), E0=(94426.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0175948496798,var=0.142030011125,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H
""",
)

entry(
    index = 289,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-5R!H-3R!H",
    kinetics = ArrheniusBM(A=(7.31026e+09,'s^-1'), n=0.914704, w0=(301000,'J/mol'), E0=(42431.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0452581064073,var=0.0929360478106,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-5R!H-3R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-5R!H-3R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-5R!H-3R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-5R!H-3R!H
""",
)

entry(
    index = 290,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-5R!H-3R!H",
    kinetics = ArrheniusBM(A=(5.7645e+09,'s^-1'), n=0.813705, w0=(301000,'J/mol'), E0=(55228,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0280204143547,var=0.120569538318,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-5R!H-3R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-5R!H-3R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-5R!H-3R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-5R!H-3R!H
""",
)

entry(
    index = 291,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.40126e+08,'s^-1'), n=1.13456, w0=(301000,'J/mol'), E0=(64824.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00529165192364,var=0.899769547691,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_N-Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_N-Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_N-Sp-7R!H=6R!H
""",
)

entry(
    index = 292,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H",
    kinetics = ArrheniusBM(A=(1.07521e+07,'s^-1'), n=0.935417, w0=(301000,'J/mol'), E0=(65725.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00370612346707,var=4.09979511039,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H
""",
)

entry(
    index = 293,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.84009e+06,'s^-1'), n=1.6675, w0=(301000,'J/mol'), E0=(80145.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0156257693168,var=0.0267475772319,Tref=1000.0,N=4,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H
""",
)

entry(
    index = 294,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2.84849e+07,'s^-1'), n=1.19514, w0=(301000,'J/mol'), E0=(65868.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0134676743958,var=0.272604856316,Tref=1000.0,N=4,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R
""",
)

entry(
    index = 295,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R_N-1CbCbfCdCddCtNO2dS2d->Cd",
    kinetics = ArrheniusBM(A=(20622.1,'s^-1'), n=2.49116, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.139139067125,var=0.0,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R_N-1CbCbfCdCddCtNO2dS2d->Cd',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R_N-1CbCbfCdCddCtNO2dS2d->Cd"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R_N-1CbCbfCdCddCtNO2dS2d->Cd""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R_N-1CbCbfCdCddCtNO2dS2d->Cd
""",
)

entry(
    index = 296,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.8135e+07,'s^-1'), n=1.44328, w0=(301000,'J/mol'), E0=(82506.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00243282692732,var=0.26687963224,Tref=1000.0,N=4,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H
""",
)

entry(
    index = 297,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.51872e+08,'s^-1'), n=0.771276, w0=(301000,'J/mol'), E0=(53178.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 298,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(3.0951,'s^-1'), n=2.35066, w0=(173000,'J/mol'), E0=(45501.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R_Ext-3R!H-R
""",
)

entry(
    index = 299,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-Sp-6R!H-3R!H",
    kinetics = ArrheniusBM(A=(3.39544e+08,'s^-1'), n=0.626108, w0=(301000,'J/mol'), E0=(56872.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.000797566287008,var=1.06161833559e-37,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-Sp-6R!H-3R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-Sp-6R!H-3R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-Sp-6R!H-3R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-Sp-6R!H-3R!H
""",
)

entry(
    index = 300,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(2.05284e+32,'s^-1'), n=-5.65647, w0=(301000,'J/mol'), E0=(61484.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.277971680901,var=2.3209672731,Tref=1000.0,N=6,correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H
""",
)

entry(
    index = 301,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(463112,'s^-1'), n=1.26821, w0=(301000,'J/mol'), E0=(104923,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00243405281156,var=0.0,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 302,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(2.1725e+18,'s^-1'), n=-1.56418, w0=(301000,'J/mol'), E0=(-5894.49,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-5R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-5R!H=4R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-5R!H=4R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-5R!H=4R!H
""",
)

entry(
    index = 303,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(7.04448e+28,'s^-1'), n=-4.75923, w0=(301000,'J/mol'), E0=(65419,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.244991974093,var=2.1998139123,Tref=1000.0,N=6,correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H
""",
)

entry(
    index = 304,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R_Ext-5R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2.50137e+08,'s^-1'), n=1.0508, w0=(301000,'J/mol'), E0=(129149,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R_Ext-5R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R_Ext-5R!H-R_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R_Ext-5R!H-R_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R_Ext-5R!H-R_Ext-3R!H-R
""",
)

entry(
    index = 305,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H",
    kinetics = ArrheniusBM(A=(8.70753e+06,'s^-1'), n=1.27069, w0=(301000,'J/mol'), E0=(53233.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0292421188658,var=0.481896524866,Tref=1000.0,N=4,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H
""",
)

entry(
    index = 306,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_4R!H-inRing",
    kinetics = ArrheniusBM(A=(117356,'s^-1'), n=1.93463, w0=(301000,'J/mol'), E0=(30100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_4R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_4R!H-inRing"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_4R!H-inRing""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_4R!H-inRing
""",
)

entry(
    index = 307,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_Int-5R!H-3R!H_Ext-6R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(3.07852e+07,'s^-1'), n=1.23179, w0=(301000,'J/mol'), E0=(49950.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_Int-5R!H-3R!H_Ext-6R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_Int-5R!H-3R!H_Ext-6R!H-R_N-Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_Int-5R!H-3R!H_Ext-6R!H-R_N-Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_Int-5R!H-3R!H_Ext-6R!H-R_N-Sp-7R!H=6R!H
""",
)

entry(
    index = 308,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.38644e+08,'s^-1'), n=0.939655, w0=(301000,'J/mol'), E0=(59287.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-3R!H-R
""",
)

entry(
    index = 309,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H",
    kinetics = ArrheniusBM(A=(5.84458e-39,'s^-1'), n=15.0176, w0=(301000,'J/mol'), E0=(12246.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.789817746907,var=0.255785453159,Tref=1000.0,N=8,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H
""",
)

entry(
    index = 310,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.04191e+08,'s^-1'), n=1.11393, w0=(301000,'J/mol'), E0=(68307.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0221915810338,var=0.419655531473,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R
""",
)

entry(
    index = 311,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing",
    kinetics = ArrheniusBM(A=(9.52774e+33,'s^-1'), n=-6.75476, w0=(300343,'J/mol'), E0=(142612,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.394034291819,var=54.047942102,Tref=1000.0,N=35,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing
""",
)

entry(
    index = 312,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(1.38674e+11,'s^-1'), n=0.681013, w0=(301000,'J/mol'), E0=(36798.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-5R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-5R!H=4R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-5R!H=4R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-5R!H=4R!H
""",
)

entry(
    index = 313,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(438099,'s^-1'), n=1.61628, w0=(301000,'J/mol'), E0=(58451.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00706199856575,var=0.666888710179,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 314,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(4.58102e+07,'s^-1'), n=1.318, w0=(301000,'J/mol'), E0=(78267.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0197304130375,var=0.960174046426,Tref=1000.0,N=8,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R
""",
)

entry(
    index = 315,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.85146e+10,'s^-1'), n=0.768291, w0=(301000,'J/mol'), E0=(110964,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-3R!H-R
""",
)

entry(
    index = 316,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H",
    kinetics = ArrheniusBM(A=(1.10157e+10,'s^-1'), n=0.569954, w0=(301000,'J/mol'), E0=(79524.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0228516434295,var=0.908912307811,Tref=1000.0,N=14,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H
""",
)

entry(
    index = 317,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(3.76254e+06,'s^-1'), n=1.55616, w0=(301000,'J/mol'), E0=(75120.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0322994437009,var=0.102533986654,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_Sp-7R!H=6R!H
""",
)

entry(
    index = 318,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_Sp-11R!H=10R!H",
    kinetics = ArrheniusBM(A=(2.14064e+06,'s^-1'), n=1.71838, w0=(301000,'J/mol'), E0=(84403.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0150703755654,var=0.0932534794483,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_Sp-11R!H=10R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_Sp-11R!H=10R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_Sp-11R!H=10R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_Sp-11R!H=10R!H
""",
)

entry(
    index = 319,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(4.40321e+08,'s^-1'), n=0.787106, w0=(301000,'J/mol'), E0=(53850,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00110524003539,var=0.910509245245,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H
""",
)

entry(
    index = 320,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(3.95503e-18,'s^-1'), n=8.41003, w0=(301000,'J/mol'), E0=(26875.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.267726575563,var=14.6238107769,Tref=1000.0,N=22,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R
""",
)

entry(
    index = 321,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing",
    kinetics = ArrheniusBM(A=(4.20531e+24,'s^-1'), n=-3.99999, w0=(301000,'J/mol'), E0=(129198,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0468426161295,var=91.4781115775,Tref=1000.0,N=29,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing
""",
)

entry(
    index = 322,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(8.78718e+06,'s^-1'), n=1.30675, w0=(301000,'J/mol'), E0=(67593,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 323,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(5.14704e+08,'s^-1'), n=1.02506, w0=(301000,'J/mol'), E0=(133500,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0211510444698,var=0.158906016441,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H
""",
)

entry(
    index = 324,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H",
    kinetics = ArrheniusBM(A=(81377.1,'s^-1'), n=1.81757, w0=(301000,'J/mol'), E0=(55004.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0488293332433,var=0.286821419422,Tref=1000.0,N=8,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H
""",
)

entry(
    index = 325,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_Int-5R!H-3R!H",
    kinetics = ArrheniusBM(A=(3.30584e+10,'s^-1'), n=0.408955, w0=(301000,'J/mol'), E0=(60752.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0363112150987,var=0.108112801919,Tref=1000.0,N=3,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_Int-5R!H-3R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_Int-5R!H-3R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_Int-5R!H-3R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_Int-5R!H-3R!H
""",
)

entry(
    index = 326,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H",
    kinetics = ArrheniusBM(A=(1.83018e+08,'s^-1'), n=0.885387, w0=(301000,'J/mol'), E0=(64694.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00307550100209,var=1.31529936367,Tref=1000.0,N=4,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H
""",
)

entry(
    index = 327,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(7.77771e+07,'s^-1'), n=1.31051, w0=(301000,'J/mol'), E0=(62897,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 328,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Int-6R!H-5R!H_Sp-6R!H-5R!H_Sp-6R!H-3R!H",
    kinetics = ArrheniusBM(A=(1.0113e+08,'s^-1'), n=0.771385, w0=(301000,'J/mol'), E0=(48246.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.96372325062,var=31.6976728339,Tref=1000.0,N=8,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Int-6R!H-5R!H_Sp-6R!H-5R!H_Sp-6R!H-3R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Int-6R!H-5R!H_Sp-6R!H-5R!H_Sp-6R!H-3R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Int-6R!H-5R!H_Sp-6R!H-5R!H_Sp-6R!H-3R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Int-6R!H-5R!H_Sp-6R!H-5R!H_Sp-6R!H-3R!H
""",
)

entry(
    index = 329,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(8.80397e+06,'s^-1'), n=0.975468, w0=(301000,'J/mol'), E0=(52212.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 330,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(5.91932e+09,'s^-1'), n=0.601632, w0=(301000,'J/mol'), E0=(105618,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R
""",
)

entry(
    index = 331,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(5.28392e+08,'s^-1'), n=1.13672, w0=(301000,'J/mol'), E0=(97905.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00661623486027,var=0.12798836688,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H
""",
)

entry(
    index = 332,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(5.453e+10,'s^-1'), n=0.519916, w0=(301000,'J/mol'), E0=(90209.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0192000229982,var=0.269866003562,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R
""",
)

entry(
    index = 333,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(2.53574e+24,'s^-1'), n=-3.25419, w0=(301000,'J/mol'), E0=(-20393.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 334,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(6.91413e+18,'s^-1'), n=-1.74391, w0=(301000,'J/mol'), E0=(-5235.38,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-5R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-5R!H=4R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-5R!H=4R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-5R!H=4R!H
""",
)

entry(
    index = 335,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_3R!H-inRing",
    kinetics = ArrheniusBM(A=(3.04667e-51,'s^-1'), n=18.3847, w0=(301000,'J/mol'), E0=(30100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_3R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_3R!H-inRing"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_3R!H-inRing""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_3R!H-inRing
""",
)

entry(
    index = 336,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(7.48477e+07,'s^-1'), n=0.853974, w0=(301000,'J/mol'), E0=(50655.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00725329510983,var=0.272609309713,Tref=1000.0,N=4,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R
""",
)

entry(
    index = 337,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(3.27876e+08,'s^-1'), n=1.22848, w0=(301000,'J/mol'), E0=(63804.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0148827435207,var=0.160246570936,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Sp-7R!H=6R!H
""",
)

entry(
    index = 338,
    label = "Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-7R!H=4R!H",
    kinetics = ArrheniusBM(A=(1.8324e+11,'s^-1'), n=0.594363, w0=(301000,'J/mol'), E0=(30974.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.000760638220417,var=0.904547720478,Tref=1000.0,N=2,correlation='Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-7R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-7R!H=4R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-7R!H=4R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-7R!H=4R!H
""",
)

entry(
    index = 339,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Int-6R!H-5R!H_N-Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(4.37414e+06,'s^-1'), n=1.35134, w0=(301000,'J/mol'), E0=(111139,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-4.89968779828,var=347.792796894,Tref=1000.0,N=10,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Int-6R!H-5R!H_N-Sp-6R!H-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Int-6R!H-5R!H_N-Sp-6R!H-5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Int-6R!H-5R!H_N-Sp-6R!H-5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Int-6R!H-5R!H_N-Sp-6R!H-5R!H
""",
)

entry(
    index = 340,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.14526e+08,'s^-1'), n=1.19881, w0=(301000,'J/mol'), E0=(55541.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 341,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-5R!H-3R!H",
    kinetics = ArrheniusBM(A=(3.18293e+09,'s^-1'), n=0.718229, w0=(301000,'J/mol'), E0=(46051.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-5R!H-3R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-5R!H-3R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-5R!H-3R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-5R!H-3R!H
""",
)

entry(
    index = 342,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.63771e-39,'s^-1'), n=15.1495, w0=(301000,'J/mol'), E0=(30100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 343,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H#4R!H",
    kinetics = ArrheniusBM(A=(6.00087e+27,'s^-1'), n=-4.62153, w0=(301000,'J/mol'), E0=(46704.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.123261515209,var=10.4372252,Tref=1000.0,N=2,correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H#4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H#4R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H#4R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H#4R!H
""",
)

entry(
    index = 344,
    label = "Root_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.73889e+10,'s^-1'), n=0.541033, w0=(301000,'J/mol'), E0=(18169.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R
""",
)

entry(
    index = 345,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(3.52918e+09,'s^-1'), n=0.896526, w0=(301000,'J/mol'), E0=(30283.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 346,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(9.34899e-08,'s^-1'), n=5.59173, w0=(301000,'J/mol'), E0=(45381.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.259210051115,var=6.33146882307,Tref=1000.0,N=108,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R
""",
)

entry(
    index = 347,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(6.65174e+09,'s^-1'), n=0.769622, w0=(301000,'J/mol'), E0=(136239,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00778123955439,var=0.900548679046,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H
""",
)

entry(
    index = 348,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.06612e+11,'s^-1'), n=0.590264, w0=(301000,'J/mol'), E0=(119838,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 349,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(6.1357e+28,'s^-1'), n=-4.64691, w0=(301000,'J/mol'), E0=(61432.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.271511144948,var=2.02387366191,Tref=1000.0,N=24,correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 350,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H",
    kinetics = ArrheniusBM(A=(971502,'s^-1'), n=1.23803, w0=(301000,'J/mol'), E0=(54829.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0128827711578,var=1.37867808588,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H
""",
)

entry(
    index = 351,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(4.38763e+09,'s^-1'), n=0.968553, w0=(301000,'J/mol'), E0=(66578.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00115026482009,var=0.895491234028,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_N-Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_N-Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_N-Sp-7R!H=6R!H
""",
)

entry(
    index = 352,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(7.64112e+09,'s^-1'), n=0.734475, w0=(301000,'J/mol'), E0=(138193,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 353,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.82206e+08,'s^-1'), n=1.09281, w0=(301000,'J/mol'), E0=(70899.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 354,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R",
    kinetics = ArrheniusBM(A=(6.12084e+27,'s^-1'), n=-4.51946, w0=(237000,'J/mol'), E0=(99953.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.709412053741,var=53.8169541231,Tref=1000.0,N=6,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R
""",
)

entry(
    index = 355,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_4R!H-inRing",
    kinetics = ArrheniusBM(A=(1.88988e+23,'s^-1'), n=-3.11005, w0=(295250,'J/mol'), E0=(56034.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.172279981692,var=8.82754229708,Tref=1000.0,N=2,correlation='Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_4R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_4R!H-inRing"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_4R!H-inRing""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_4R!H-inRing
""",
)

entry(
    index = 356,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.49064e+10,'s^-1'), n=0.706646, w0=(301000,'J/mol'), E0=(128484,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 357,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(5.067e+09,'s^-1'), n=0.815026, w0=(301000,'J/mol'), E0=(71643.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00636006925108,var=0.900549198809,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H
""",
)

entry(
    index = 358,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.36919e+06,'s^-1'), n=1.56657, w0=(301000,'J/mol'), E0=(85357.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.025212547866,var=0.10856071516,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_Sp-7R!H=6R!H
""",
)

entry(
    index = 359,
    label = "Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-7R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.15894e+10,'s^-1'), n=0.882846, w0=(301000,'J/mol'), E0=(29549,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-7R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-7R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-7R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-7R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 360,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_N-Sp-11R!H=10R!H",
    kinetics = ArrheniusBM(A=(9.70942e+06,'s^-1'), n=1.47282, w0=(301000,'J/mol'), E0=(75939.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_N-Sp-11R!H=10R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_N-Sp-11R!H=10R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_N-Sp-11R!H=10R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_N-Sp-11R!H=10R!H
""",
)

entry(
    index = 361,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(6.93701e+08,'s^-1'), n=1.10555, w0=(301000,'J/mol'), E0=(110964,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 362,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R_Int-4R!H-3R!H",
    kinetics = ArrheniusBM(A=(5.68541e-15,'s^-1'), n=7.98873, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R_Int-4R!H-3R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R_Int-4R!H-3R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R_Int-4R!H-3R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R_Int-4R!H-3R!H
""",
)

entry(
    index = 363,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(6.64018e+09,'s^-1'), n=0.883275, w0=(301000,'J/mol'), E0=(100552,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00616930717628,var=0.896500256634,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H
""",
)

entry(
    index = 364,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(2.07201e+10,'s^-1'), n=0.607674, w0=(301000,'J/mol'), E0=(99014.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 365,
    label = "Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-7R!H=4R!H",
    kinetics = ArrheniusBM(A=(1.05122e+10,'s^-1'), n=0.88878, w0=(301000,'J/mol'), E0=(27992.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0133762061978,var=0.142259528183,Tref=1000.0,N=2,correlation='Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-7R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-7R!H=4R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-7R!H=4R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-7R!H=4R!H
""",
)

entry(
    index = 366,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-11R!H=10R!H",
    kinetics = ArrheniusBM(A=(2.28291e+07,'s^-1'), n=1.46487, w0=(301000,'J/mol'), E0=(88607.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-11R!H=10R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-11R!H=10R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-11R!H=10R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-11R!H=10R!H
""",
)

entry(
    index = 367,
    label = "Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(1.31838e+11,'s^-1'), n=0.602182, w0=(301000,'J/mol'), E0=(16084.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 368,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing",
    kinetics = ArrheniusBM(A=(4.29822e+73,'s^-1'), n=-18.3199, w0=(193526,'J/mol'), E0=(193575,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.996559842966,var=34.6917992375,Tref=1000.0,N=19,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing
""",
)

entry(
    index = 369,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(2.10369e-39,'s^-1'), n=15.1508, w0=(301000,'J/mol'), E0=(12392.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.03848377517,var=34.9290813568,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 370,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(6.47819e+48,'s^-1'), n=-10.9636, w0=(290080,'J/mol'), E0=(144308,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.626054807172,var=30.5704570203,Tref=1000.0,N=187,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 371,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H",
    kinetics = ArrheniusBM(A=(1.10176e+09,'s^-1'), n=1.05544, w0=(301000,'J/mol'), E0=(64553.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0106545185858,var=0.314909182121,Tref=1000.0,N=8,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H
""",
)

entry(
    index = 372,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(1.39782e+08,'s^-1'), n=1.39402, w0=(301000,'J/mol'), E0=(68044.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00779666006379,var=0.267576358578,Tref=1000.0,N=2,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_Sp-9R!H=8R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_Sp-9R!H=8R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_Sp-9R!H=8R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_Sp-9R!H=8R!H
""",
)

entry(
    index = 373,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(4.05714e+28,'s^-1'), n=-5.13657, w0=(300617,'J/mol'), E0=(126847,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.354691310379,var=42.5946220488,Tref=1000.0,N=60,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R
""",
)

entry(
    index = 374,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(3.26674e+06,'s^-1'), n=1.58092, w0=(301000,'J/mol'), E0=(76330.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 375,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(1.71791e+10,'s^-1'), n=0.813141, w0=(301000,'J/mol'), E0=(28935.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-5R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-5R!H=4R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-5R!H=4R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-5R!H=4R!H
""",
)

entry(
    index = 376,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(4.81496e+14,'s^-1'), n=-0.738851, w0=(301000,'J/mol'), E0=(89689.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0798112853483,var=9.52635925155,Tref=1000.0,N=38,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R
""",
)

entry(
    index = 377,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(9.50975e+40,'s^-1'), n=-8.67992, w0=(293037,'J/mol'), E0=(133923,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.535980038527,var=34.8857167795,Tref=1000.0,N=260,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
""",
)

entry(
    index = 378,
    label = "Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-1CbCbfCdCddCtNO2dS2d-R",
    kinetics = ArrheniusBM(A=(2.92008e+11,'s^-1'), n=0.581386, w0=(301000,'J/mol'), E0=(20862.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0,var=33.1368631905,Tref=1000.0,N=1,correlation='Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-1CbCbfCdCddCtNO2dS2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-1CbCbfCdCddCtNO2dS2d-R"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-1CbCbfCdCddCtNO2dS2d-R""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-1CbCbfCdCddCtNO2dS2d-R
""",
)

entry(
    index = 379,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(1.84211e+10,'s^-1'), n=0.497829, w0=(301000,'J/mol'), E0=(95553.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0217996214902,var=7.55015200643,Tref=1000.0,N=20,correlation='Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H
""",
)

entry(
    index = 380,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.56373e+11,'s^-1'), n=0.608116, w0=(301000,'J/mol'), E0=(31564,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0129091982856,var=0.31932859761,Tref=1000.0,N=4,correlation='Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H
""",
)

