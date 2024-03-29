#!/usr/bin/env python
# encoding: utf-8

name = "Li_Addition_MultipleBond/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(3.38862e+22,'m^3/(mol*s)'), n=-3.83488, w0=(331025,'J/mol'), E0=(69762.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2739971381142295, var=18.397651058247572, Tref=1000.0, N=4, data_mean=0.0, correlation='Root',), solute=SoluteData(S=-2.526374294614294,B=0.8015972337092023,E=0.7939796321505602,L=-7.347532148984288,A=3.5839299275543293,comment=''), comment="""BM rule fitted to 4 training reactions at node Root
    Total Standard Deviation in ln(k): 9.287241561557916"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root
Total Standard Deviation in ln(k): 9.287241561557916""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root
Total Standard Deviation in ln(k): 9.287241561557916
""",
)

entry(
    index = 2,
    label = "Root_1R!H->C",
    kinetics = Arrhenius(A=(105.399,'m^3/(mol*s)'), n=1.74038, Ea=(37.7145,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 3,
    label = "Root_N-1R!H->C",
    kinetics = ArrheniusBM(A=(2.88896e+17,'m^3/(mol*s)'), n=-2.28234, w0=(362933,'J/mol'), E0=(48674.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3169889639215061, var=6.766509193272011, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H->C',), solute=SoluteData(S=-2.526374294614294,B=0.8015972337092023,E=0.7939796321505602,L=-7.347532148984288,A=3.5839299275543293,comment=''), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H->C
    Total Standard Deviation in ln(k): 6.011274743737681"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H->C
Total Standard Deviation in ln(k): 6.011274743737681""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H->C
Total Standard Deviation in ln(k): 6.011274743737681
""",
)

entry(
    index = 4,
    label = "Root_N-1R!H->C_1BrClFILiNOPSSi->O",
    kinetics = ArrheniusBM(A=(7.22249e+18,'m^3/(mol*s)'), n=-2.68647, w0=(391300,'J/mol'), E0=(48434.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.180092557367769, var=46.07331062123734, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFILiNOPSSi->O',), solute=SoluteData(S=-2.8589187219655385,B=2.5382122694909937,E=-5.179331723749835,L=-7.842845726943329,A=3.3935425114208373,comment=''), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFILiNOPSSi->O
    Total Standard Deviation in ln(k): 19.085224653395613"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFILiNOPSSi->O
Total Standard Deviation in ln(k): 19.085224653395613""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFILiNOPSSi->O
Total Standard Deviation in ln(k): 19.085224653395613
""",
)

entry(
    index = 5,
    label = "Root_N-1R!H->C_N-1BrClFILiNOPSSi->O",
    kinetics = Arrhenius(A=(12900,'m^3/(mol*s)'), n=1.54986, Ea=(-0.322199,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFILiNOPSSi->O',), solute=SoluteData(S=-1.8612854399118046,B=-2.67163283785438,E=12.74060234395135,L=-6.356904993066203,A=3.9647047598213128,comment=''), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFILiNOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFILiNOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFILiNOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 6,
    label = "Root_N-1R!H->C_1BrClFILiNOPSSi->O_2R!H-inRing",
    kinetics = Arrhenius(A=(286.34,'m^3/(mol*s)'), n=1.60471, Ea=(-29.5903,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFILiNOPSSi->O_2R!H-inRing',), solute=SoluteData(S=-4.381373385806166,B=2.8115182826673752,E=-5.285110205702292,L=-10.646126189503287,A=3.0115609547759967,comment=''), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFILiNOPSSi->O_2R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFILiNOPSSi->O_2R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFILiNOPSSi->O_2R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "Root_N-1R!H->C_1BrClFILiNOPSSi->O_N-2R!H-inRing",
    kinetics = Arrhenius(A=(792975,'m^3/(mol*s)'), n=1.43477, Ea=(-1.88935,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFILiNOPSSi->O_N-2R!H-inRing',), solute=SoluteData(S=-1.3364640581249116,B=2.2649062563146116,E=-5.073553241797377,L=-5.039565264383372,A=3.7755240680656774,comment=''), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFILiNOPSSi->O_N-2R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFILiNOPSSi->O_N-2R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFILiNOPSSi->O_N-2R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

