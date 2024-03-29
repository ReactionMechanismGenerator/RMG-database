#!/usr/bin/env python
# encoding: utf-8

name = "Cation_NO_Ring_Opening/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusChargeTransfer(A=(58120,'m^3/(mol*s)'), n=1.21832, Ea=(50.6022,'kJ/mol'), V0=(0,'V'), alpha=0.125, electrons=1, T0=(1,'K'), uncertainty=RateUncertainty(mu=-1.5745685336101335e-15, var=45.176682218361336, Tref=1000.0, N=4, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 4 training reactions at node Root
    Total Standard Deviation in ln(k): 13.474546453398474"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root
Total Standard Deviation in ln(k): 13.474546453398474""",
    longDesc =
"""
BM rule fitted to 4 training reactions at node Root
Total Standard Deviation in ln(k): 13.474546453398474
""",
)

entry(
    index = 2,
    label = "Root_Ext-2R-R",
    kinetics = ArrheniusChargeTransfer(A=(295357,'m^3/(mol*s)'), n=1.03263, Ea=(67.486,'kJ/mol'), V0=(0,'V'), alpha=0.166667, electrons=1, T0=(1,'K'), uncertainty=RateUncertainty(mu=-8.997534477772192e-16, var=47.31059998036416, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-2R-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-2R-R
    Total Standard Deviation in ln(k): 13.789109401274187"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-2R-R
Total Standard Deviation in ln(k): 13.789109401274187""",
    longDesc =
"""
BM rule fitted to 3 training reactions at node Root_Ext-2R-R
Total Standard Deviation in ln(k): 13.789109401274187
""",
)

entry(
    index = 3,
    label = "Root_Ext-2R-R_Ext-5R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusChargeTransfer(A=(1674.36,'m^3/(mol*s)'), n=1.43292, Ea=(69.2534,'kJ/mol'), V0=(0,'V'), alpha=0.25, electrons=1, T0=(1,'K'), uncertainty=RateUncertainty(mu=-1.124691809721524e-16, var=3.4421337695732377, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R-R_Ext-5R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R-R_Ext-5R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 3.719382654880908"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R-R_Ext-5R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 3.719382654880908""",
    longDesc =
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R-R_Ext-5R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 3.719382654880908
""",
)

entry(
    index = 4,
    label = "Root_Ext-2R-R_Ext-5R!H-R_Ext-6R!H-R_1NO->O",
    kinetics = ArrheniusChargeTransferBM(A=(714805,'m^3/(mol*s)'), n=0.521642, w0=(349800,'J/mol'), E0=(34980,'J/mol'), V0=(0,'V'), alpha=0.5, electrons=0, Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R-R_Ext-5R!H-R_Ext-6R!H-R_1NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R-R_Ext-5R!H-R_Ext-6R!H-R_1NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R-R_Ext-5R!H-R_Ext-6R!H-R_1NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc =
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R-R_Ext-5R!H-R_Ext-6R!H-R_1NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_Ext-2R-R_Ext-5R!H-R_Ext-6R!H-R_N-1NO->O",
    kinetics = ArrheniusChargeTransferBM(A=(3.92201,'m^3/(mol*s)'), n=2.34419, w0=(303700,'J/mol'), E0=(30370,'J/mol'), V0=(0,'V'), alpha=0.5, electrons=0, Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R-R_Ext-5R!H-R_Ext-6R!H-R_N-1NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R-R_Ext-5R!H-R_Ext-6R!H-R_N-1NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R-R_Ext-5R!H-R_Ext-6R!H-R_N-1NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc =
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R-R_Ext-5R!H-R_Ext-6R!H-R_N-1NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)
