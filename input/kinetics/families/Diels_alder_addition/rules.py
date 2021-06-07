#!/usr/bin/env python
# encoding: utf-8

name = "Diels_alder_addition/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(9.17508e-08,'m^3/(mol*s)'), n=3.07766, w0=(857395,'J/mol'), E0=(135956,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.12455772480097667, var=4.503087907907877, Tref=1000.0, N=19, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 19 training reactions at node Root
    Total Standard Deviation in ln(k): 4.567103260504657"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root
Total Standard Deviation in ln(k): 4.567103260504657""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root
Total Standard Deviation in ln(k): 4.567103260504657
""",
)

entry(
    index = 2,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd",
    kinetics = ArrheniusBM(A=(0.000164218,'m^3/(mol*s)'), n=2.11749, w0=(858000,'J/mol'), E0=(142431,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0614368558151701, var=3.784088113710139, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd',), comment="""BM rule fitted to 17 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd
    Total Standard Deviation in ln(k): 4.054121528473931"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd
Total Standard Deviation in ln(k): 4.054121528473931""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd
Total Standard Deviation in ln(k): 4.054121528473931
""",
)

entry(
    index = 3,
    label = "Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd",
    kinetics = ArrheniusBM(A=(1.95896e-11,'m^3/(mol*s)'), n=4.15719, w0=(852250,'J/mol'), E0=(206824,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00023424662986478353, var=0.0043250921906934775, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd',), comment="""BM rule fitted to 2 training reactions at node Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd
    Total Standard Deviation in ln(k): 0.1324308299850172"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd
Total Standard Deviation in ln(k): 0.1324308299850172""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd
Total Standard Deviation in ln(k): 0.1324308299850172
""",
)

entry(
    index = 4,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_1CdN3dN5dcS4dS6d-inRing",
    kinetics = ArrheniusBM(A=(8.11e-08,'m^3/(mol*s)'), n=3.05, w0=(858000,'J/mol'), E0=(145464,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_1CdN3dN5dcS4dS6d-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_1CdN3dN5dcS4dS6d-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_1CdN3dN5dcS4dS6d-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_1CdN3dN5dcS4dS6d-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing",
    kinetics = ArrheniusBM(A=(0.000127046,'m^3/(mol*s)'), n=2.15007, w0=(858000,'J/mol'), E0=(142104,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06358824511050899, var=3.792920539332787, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing',), comment="""BM rule fitted to 16 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing
    Total Standard Deviation in ln(k): 4.064075581202041"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing
Total Standard Deviation in ln(k): 4.064075581202041""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing
Total Standard Deviation in ln(k): 4.064075581202041
""",
)

entry(
    index = 6,
    label = "Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct",
    kinetics = ArrheniusBM(A=(1.22e-07,'m^3/(mol*s)'), n=2.98, w0=(846500,'J/mol'), E0=(212387,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct",
    kinetics = ArrheniusBM(A=(1.77e-07,'m^3/(mol*s)'), n=2.94, w0=(858000,'J/mol'), E0=(212844,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 8,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R",
    kinetics = ArrheniusBM(A=(3.26766e-09,'m^3/(mol*s)'), n=3.49827, w0=(858000,'J/mol'), E0=(131868,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.14443333294059355, var=8.305517039704704, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R',), comment="""BM rule fitted to 7 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R
    Total Standard Deviation in ln(k): 6.14040277086316"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R
Total Standard Deviation in ln(k): 6.14040277086316""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R
Total Standard Deviation in ln(k): 6.14040277086316
""",
)

entry(
    index = 9,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R",
    kinetics = ArrheniusBM(A=(0.891564,'m^3/(mol*s)'), n=0.985671, w0=(858000,'J/mol'), E0=(150184,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.007052630370330484, var=0.9912014232841642, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R',), comment="""BM rule fitted to 4 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R
    Total Standard Deviation in ln(k): 2.0136163611420597"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R
Total Standard Deviation in ln(k): 2.0136163611420597""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R
Total Standard Deviation in ln(k): 2.0136163611420597
""",
)

entry(
    index = 10,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-2CdN3dN5dcS4dS6d-R",
    kinetics = ArrheniusBM(A=(132000,'m^3/(mol*s)'), n=0, w0=(858000,'J/mol'), E0=(197826,'J/mol'), Tmin=(1000,'K'), Tmax=(1180,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-2CdN3dN5dcS4dS6d-R',), comment="""BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-2CdN3dN5dcS4dS6d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-2CdN3dN5dcS4dS6d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-2CdN3dN5dcS4dS6d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-1CdN3dN5dcS4dS6d-R",
    kinetics = ArrheniusBM(A=(0.0381414,'m^3/(mol*s)'), n=1.36206, w0=(858000,'J/mol'), E0=(137373,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.1512664848213554, var=3.20497538350606, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-1CdN3dN5dcS4dS6d-R',), comment="""BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-1CdN3dN5dcS4dS6d-R
    Total Standard Deviation in ln(k): 6.4815953127947035"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-1CdN3dN5dcS4dS6d-R
Total Standard Deviation in ln(k): 6.4815953127947035""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-1CdN3dN5dcS4dS6d-R
Total Standard Deviation in ln(k): 6.4815953127947035
""",
)

entry(
    index = 12,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R",
    kinetics = ArrheniusBM(A=(8910,'m^3/(mol*s)'), n=0, w0=(858000,'J/mol'), E0=(169755,'J/mol'), Tmin=(464,'K'), Tmax=(557,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R',), comment="""BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R",
    kinetics = ArrheniusBM(A=(3.03944e-10,'m^3/(mol*s)'), n=3.77961, w0=(858000,'J/mol'), E0=(119950,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.14910705179089842, var=13.709980217686734, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R',), comment="""BM rule fitted to 4 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R
    Total Standard Deviation in ln(k): 7.797571490148185"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R
Total Standard Deviation in ln(k): 7.797571490148185""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R
Total Standard Deviation in ln(k): 7.797571490148185
""",
)

entry(
    index = 14,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R",
    kinetics = ArrheniusBM(A=(6.76344e-05,'m^3/(mol*s)'), n=2.19153, w0=(858000,'J/mol'), E0=(149206,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.01321817248392336, var=26.283515993403185, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R',), comment="""BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
    Total Standard Deviation in ln(k): 10.310977355070442"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
Total Standard Deviation in ln(k): 10.310977355070442""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
Total Standard Deviation in ln(k): 10.310977355070442
""",
)

entry(
    index = 15,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R",
    kinetics = ArrheniusBM(A=(0.119605,'m^3/(mol*s)'), n=1.17525, w0=(858000,'J/mol'), E0=(149276,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.7763568394002489e-15, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R',), comment="""BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
    Total Standard Deviation in ln(k): 4.463208139196605e-15"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
Total Standard Deviation in ln(k): 4.463208139196605e-15""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
Total Standard Deviation in ln(k): 4.463208139196605e-15
""",
)

entry(
    index = 16,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R_Ext-2CdN3dN5dcS4dS6d-R",
    kinetics = ArrheniusBM(A=(1020,'m^3/(mol*s)'), n=0, w0=(858000,'J/mol'), E0=(143654,'J/mol'), Tmin=(492,'K'), Tmax=(606,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R_Ext-2CdN3dN5dcS4dS6d-R',), comment="""BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R_Ext-2CdN3dN5dcS4dS6d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R_Ext-2CdN3dN5dcS4dS6d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R_Ext-2CdN3dN5dcS4dS6d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-1CdN3dN5dcS4dS6d-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R",
    kinetics = ArrheniusBM(A=(1020,'m^3/(mol*s)'), n=0, w0=(858000,'J/mol'), E0=(143654,'J/mol'), Tmin=(492,'K'), Tmax=(606,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-1CdN3dN5dcS4dS6d-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R',), comment="""BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-1CdN3dN5dcS4dS6d-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-1CdN3dN5dcS4dS6d-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-1CdN3dN5dcS4dS6d-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R",
    kinetics = ArrheniusBM(A=(0.20079,'m^3/(mol*s)'), n=1.18774, w0=(858000,'J/mol'), E0=(122278,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.3988810110276873e-14, var=4.978412222288914e-60, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R',), comment="""BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
    Total Standard Deviation in ln(k): 3.514776409617305e-14"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
Total Standard Deviation in ln(k): 3.514776409617305e-14""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
Total Standard Deviation in ln(k): 3.514776409617305e-14
""",
)

entry(
    index = 19,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1020,'m^3/(mol*s)'), n=0, w0=(858000,'J/mol'), E0=(144918,'J/mol'), Tmin=(379,'K'), Tmax=(581,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1020,'m^3/(mol*s)'), n=0, w0=(858000,'J/mol'), E0=(144918,'J/mol'), Tmin=(379,'K'), Tmax=(581,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(899,'m^3/(mol*s)'), n=0, w0=(858000,'J/mol'), E0=(156378,'J/mol'), Tmin=(515,'K'), Tmax=(572,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1260,'m^3/(mol*s)'), n=0, w0=(858000,'J/mol'), E0=(127005,'J/mol'), Tmin=(352,'K'), Tmax=(423,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-6COCSCdCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

