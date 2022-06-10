#!/usr/bin/env python
# encoding: utf-8

name = "Diels_alder_addition/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(9.33101e-05,'m^3/(mol*s)'), n=2.25664, w0=(862143,'J/mol'), E0=(156345,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1147967005954929, var=4.101568337638634, Tref=1000.0, N=21, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 21 training reactions at node Root
    Total Standard Deviation in ln(k): 4.348489374620653"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root
Total Standard Deviation in ln(k): 4.348489374620653""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root
Total Standard Deviation in ln(k): 4.348489374620653
""",
)

entry(
    index = 2,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd",
    kinetics = ArrheniusBM(A=(1.78049e-06,'m^3/(mol*s)'), n=2.77654, w0=(858000,'J/mol'), E0=(149854,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.053516820163873775, var=3.6255907632588267, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd',), comment="""BM rule fitted to 18 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd
    Total Standard Deviation in ln(k): 3.9516772499747743"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd
Total Standard Deviation in ln(k): 3.9516772499747743""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd
Total Standard Deviation in ln(k): 3.9516772499747743
""",
)

entry(
    index = 3,
    label = "Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd",
    kinetics = ArrheniusBM(A=(4.03757e-13,'m^3/(mol*s)'), n=4.52954, w0=(887000,'J/mol'), E0=(143100,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-6.0855622054326055, var=71.1568223758254, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd',), comment="""BM rule fitted to 3 training reactions at node Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd
    Total Standard Deviation in ln(k): 32.20120048283609"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd
Total Standard Deviation in ln(k): 32.20120048283609""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd
Total Standard Deviation in ln(k): 32.20120048283609
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
    kinetics = ArrheniusBM(A=(1.73957e-06,'m^3/(mol*s)'), n=2.77944, w0=(858000,'J/mol'), E0=(149813,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05377849566294846, var=3.6383400603390044, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing',), comment="""BM rule fitted to 17 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing
    Total Standard Deviation in ln(k): 3.9590404018616376"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing
Total Standard Deviation in ln(k): 3.9590404018616376""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing
Total Standard Deviation in ln(k): 3.9590404018616376
""",
)

entry(
    index = 6,
    label = "Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct",
    kinetics = ArrheniusBM(A=(1.22e-07,'m^3/(mol*s)'), n=2.98, w0=(846500,'J/mol'), E0=(211218,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct
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
    kinetics = ArrheniusBM(A=(1.75475e-11,'m^3/(mol*s)'), n=4.0597, w0=(907250,'J/mol'), E0=(146666,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-6.193484162227714, var=73.27695532230449, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct',), comment="""BM rule fitted to 2 training reactions at node Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct
    Total Standard Deviation in ln(k): 32.72244315846819"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct
Total Standard Deviation in ln(k): 32.72244315846819""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct
Total Standard Deviation in ln(k): 32.72244315846819
""",
)

entry(
    index = 8,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R",
    kinetics = ArrheniusBM(A=(5.38143e-07,'m^3/(mol*s)'), n=2.90426, w0=(858000,'J/mol'), E0=(147287,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.22625272160794474, var=7.109026128865732, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R',), comment="""BM rule fitted to 8 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R
    Total Standard Deviation in ln(k): 5.913650604377937"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R
Total Standard Deviation in ln(k): 5.913650604377937""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R
Total Standard Deviation in ln(k): 5.913650604377937
""",
)

entry(
    index = 9,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-1CdN3dN5dcS4dS6d-R",
    kinetics = ArrheniusBM(A=(0.446605,'m^3/(mol*s)'), n=1.06441, w0=(858000,'J/mol'), E0=(139969,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.2479418310823012, var=3.746729545052508, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-1CdN3dN5dcS4dS6d-R',), comment="""BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-1CdN3dN5dcS4dS6d-R
    Total Standard Deviation in ln(k): 7.015991799694358"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-1CdN3dN5dcS4dS6d-R
Total Standard Deviation in ln(k): 7.015991799694358""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-1CdN3dN5dcS4dS6d-R
Total Standard Deviation in ln(k): 7.015991799694358
""",
)

entry(
    index = 10,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-2CdN3dN5dcS4dS6d-R",
    kinetics = ArrheniusBM(A=(0.446605,'m^3/(mol*s)'), n=1.06441, w0=(858000,'J/mol'), E0=(139969,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.2479418310823012, var=3.746729545052508, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-2CdN3dN5dcS4dS6d-R',), comment="""BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-2CdN3dN5dcS4dS6d-R
    Total Standard Deviation in ln(k): 7.015991799694358"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-2CdN3dN5dcS4dS6d-R
Total Standard Deviation in ln(k): 7.015991799694358""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-2CdN3dN5dcS4dS6d-R
Total Standard Deviation in ln(k): 7.015991799694358
""",
)

entry(
    index = 11,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R",
    kinetics = ArrheniusBM(A=(2.15883,'m^3/(mol*s)'), n=0.926526, w0=(858000,'J/mol'), E0=(155877,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.018010594753247997, var=0.625832289615524, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R',), comment="""BM rule fitted to 3 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R
    Total Standard Deviation in ln(k): 1.6311899018279374"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R
Total Standard Deviation in ln(k): 1.6311899018279374""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R
Total Standard Deviation in ln(k): 1.6311899018279374
""",
)

entry(
    index = 12,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R",
    kinetics = ArrheniusBM(A=(8910,'m^3/(mol*s)'), n=0, w0=(858000,'J/mol'), E0=(167318,'J/mol'), Tmin=(464,'K'), Tmax=(557,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R',), comment="""BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct_5COCdd->Cdd",
    kinetics = ArrheniusBM(A=(1.77e-07,'m^3/(mol*s)'), n=2.94, w0=(858000,'J/mol'), E0=(211660,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct_5COCdd->Cdd',), comment="""BM rule fitted to 1 training reactions at node Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct_5COCdd->Cdd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct_5COCdd->Cdd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct_5COCdd->Cdd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct_N-5COCdd->Cdd",
    kinetics = ArrheniusBM(A=(2.74773e-08,'m^3/(mol*s)'), n=3.0576, w0=(956500,'J/mol'), E0=(149441,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct_N-5COCdd->Cdd',), comment="""BM rule fitted to 1 training reactions at node Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct_N-5COCdd->Cdd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct_N-5COCdd->Cdd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-5COCSCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Ct_N-5COCdd->Cdd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R",
    kinetics = ArrheniusBM(A=(0.000165533,'m^3/(mol*s)'), n=2.05774, w0=(858000,'J/mol'), E0=(131083,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.10166403055099561, var=13.658259824244146, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R',), comment="""BM rule fitted to 4 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R
    Total Standard Deviation in ln(k): 7.664353323599815"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R
Total Standard Deviation in ln(k): 7.664353323599815""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R
Total Standard Deviation in ln(k): 7.664353323599815
""",
)

entry(
    index = 16,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R",
    kinetics = ArrheniusBM(A=(0.0106931,'m^3/(mol*s)'), n=1.53489, w0=(858000,'J/mol'), E0=(153249,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.01820808251533475, var=28.348068215283774, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R',), comment="""BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
    Total Standard Deviation in ln(k): 10.719540669073005"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
Total Standard Deviation in ln(k): 10.719540669073005""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
Total Standard Deviation in ln(k): 10.719540669073005
""",
)

entry(
    index = 17,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-4Cd-R",
    kinetics = ArrheniusBM(A=(4570,'m^3/(mol*s)'), n=0, w0=(858000,'J/mol'), E0=(176716,'J/mol'), Tmin=(450,'K'), Tmax=(592,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-4Cd-R',), comment="""BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-4Cd-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-4Cd-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-4Cd-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-1CdN3dN5dcS4dS6d-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R",
    kinetics = ArrheniusBM(A=(1020,'m^3/(mol*s)'), n=0, w0=(858000,'J/mol'), E0=(142478,'J/mol'), Tmin=(492,'K'), Tmax=(606,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-1CdN3dN5dcS4dS6d-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R',), comment="""BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-1CdN3dN5dcS4dS6d-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-1CdN3dN5dcS4dS6d-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-1CdN3dN5dcS4dS6d-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-2CdN3dN5dcS4dS6d-R_Ext-5Cd-R",
    kinetics = ArrheniusBM(A=(1020,'m^3/(mol*s)'), n=0, w0=(858000,'J/mol'), E0=(142478,'J/mol'), Tmin=(492,'K'), Tmax=(606,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-2CdN3dN5dcS4dS6d-R_Ext-5Cd-R',), comment="""BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-2CdN3dN5dcS4dS6d-R_Ext-5Cd-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-2CdN3dN5dcS4dS6d-R_Ext-5Cd-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-2CdN3dN5dcS4dS6d-R_Ext-5Cd-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R",
    kinetics = ArrheniusBM(A=(0.562362,'m^3/(mol*s)'), n=0.999299, w0=(858000,'J/mol'), E0=(151136,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-8.770761894538775e-15, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R',), comment="""BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
    Total Standard Deviation in ln(k): 2.203709018728335e-14"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
Total Standard Deviation in ln(k): 2.203709018728335e-14""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
Total Standard Deviation in ln(k): 2.203709018728335e-14
""",
)

entry(
    index = 21,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R",
    kinetics = ArrheniusBM(A=(0.492357,'m^3/(mol*s)'), n=1.06989, w0=(858000,'J/mol'), E0=(122997,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.3988810110276873e-14, var=4.978412222288914e-60, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R',), comment="""BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
    Total Standard Deviation in ln(k): 3.514776409617305e-14"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
Total Standard Deviation in ln(k): 3.514776409617305e-14""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R
Total Standard Deviation in ln(k): 3.514776409617305e-14
""",
)

entry(
    index = 22,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1020,'m^3/(mol*s)'), n=0, w0=(858000,'J/mol'), E0=(143715,'J/mol'), Tmin=(379,'K'), Tmax=(581,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-8R!H-R
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
    index = 23,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1020,'m^3/(mol*s)'), n=0, w0=(858000,'J/mol'), E0=(143715,'J/mol'), Tmin=(379,'K'), Tmax=(581,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(899,'m^3/(mol*s)'), n=0, w0=(858000,'J/mol'), E0=(155169,'J/mol'), Tmin=(515,'K'), Tmax=(572,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-5Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1260,'m^3/(mol*s)'), n=0, w0=(858000,'J/mol'), E0=(127005,'J/mol'), Tmin=(352,'K'), Tmax=(423,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt->Cd_N-1CdN3dN5dcS4dS6d-inRing_Ext-3Cd-R_Ext-5Cd-R_Ext-6COCSCdCddCtN3dN3tN5dcN5tcO2dS2dS4dS4tS6dS6tS6tdS6tt-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

