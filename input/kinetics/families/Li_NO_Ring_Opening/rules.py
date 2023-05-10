#!/usr/bin/env python
# encoding: utf-8

name = "Li_NO_Ring_Opening/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(1227.49,'m^3/(mol*s)'), n=1.78231, w0=(340580,'J/mol'), E0=(61995.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03079975817713572, var=13.049803001179814, Tref=1000.0, N=5, data_mean=0.0, correlation='Root',), solute=SoluteData(S=0.33752849960684006,B=-0.08726885649250123,E=0.37833778894270276,L=1.1498227049138072,A=0.073872744373486,comment=''), comment="""BM rule fitted to 5 training reactions at node Root
    Total Standard Deviation in ln(k): 7.319393776850598"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root
Total Standard Deviation in ln(k): 7.319393776850598""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root
Total Standard Deviation in ln(k): 7.319393776850598
""",
)

entry(
    index = 2,
    label = "Root_1NO->O",
    kinetics = ArrheniusBM(A=(721.913,'m^3/(mol*s)'), n=1.85814, w0=(349800,'J/mol'), E0=(61620.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4375477450633406, var=24.504133425532565, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1NO->O',), solute=SoluteData(S=0.4590453878469358,B=-0.1677500099666882,E=0.6946943283413284,L=0.8027664740150602,A=0.3404928856360022,comment=''), comment="""BM rule fitted to 4 training reactions at node Root_1NO->O
    Total Standard Deviation in ln(k): 11.023135587423338"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1NO->O
Total Standard Deviation in ln(k): 11.023135587423338""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1NO->O
Total Standard Deviation in ln(k): 11.023135587423338
""",
)

entry(
    index = 3,
    label = "Root_N-1NO->O",
    kinetics = Arrhenius(A=(0.600821,'m^3/(mol*s)'), n=2.69163, Ea=(75.1245,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1NO->O',), solute=SoluteData(S=-0.148539053353543,B=0.2346557574042466,E=-0.8870883686517999,L=2.5380476285087967,A=-0.9926078206765788,comment=''), comment="""BM rule fitted to 1 training reactions at node Root_N-1NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 4,
    label = "Root_1NO->O_Ext-2R-R",
    kinetics = ArrheniusBM(A=(0.0811241,'m^3/(mol*s)'), n=3.0165, w0=(349800,'J/mol'), E0=(55933.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5578666757241915, var=40.08131913969709, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1NO->O_Ext-2R-R',), solute=SoluteData(S=0.5933552756886175,B=-0.23163482172950375,E=0.6191898079346778,L=1.126493496999618,A=0.10351697123780944,comment=''), comment="""BM rule fitted to 3 training reactions at node Root_1NO->O_Ext-2R-R
    Total Standard Deviation in ln(k): 14.09361454656864"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1NO->O_Ext-2R-R
Total Standard Deviation in ln(k): 14.09361454656864""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1NO->O_Ext-2R-R
Total Standard Deviation in ln(k): 14.09361454656864
""",
)

entry(
    index = 5,
    label = "Root_1NO->O_Ext-2R-R_Ext-5R!H-R_Ext-6R!H-R",
    kinetics = Arrhenius(A=(1235,'m^3/(mol*s)'), n=1.47788, Ea=(57.5452,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1NO->O_Ext-2R-R_Ext-5R!H-R_Ext-6R!H-R',), solute=SoluteData(S=0.6720034234692184,B=-0.5272433935924955,E=-0.04058233196442157,L=0.016250546098216745,A=-0.03472246433194898,comment=''), comment="""BM rule fitted to 1 training reactions at node Root_1NO->O_Ext-2R-R_Ext-5R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1NO->O_Ext-2R-R_Ext-5R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1NO->O_Ext-2R-R_Ext-5R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 6,
    label = "Root_1NO->O_Ext-2R-R_Ext-5R!H-R_Ext-3R-R",
    kinetics = Arrhenius(A=(32.0115,'m^3/(mol*s)'), n=2.08453, Ea=(2.45304,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1NO->O_Ext-2R-R_Ext-5R!H-R_Ext-3R-R',), solute=SoluteData(S=0.48393279894068975,B=0.3604817411402965,E=2.468332514419877,L=4.280078451074511,A=0.2780568400693335,comment=''), comment="""BM rule fitted to 1 training reactions at node Root_1NO->O_Ext-2R-R_Ext-5R!H-R_Ext-3R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1NO->O_Ext-2R-R_Ext-5R!H-R_Ext-3R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1NO->O_Ext-2R-R_Ext-5R!H-R_Ext-3R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

