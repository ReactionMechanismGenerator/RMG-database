#!/usr/bin/env python
# encoding: utf-8

name = "1,3_Insertion_CO2/rules"
shortDesc = ""
longDesc = """
572 - 575 Some of the tortional motions in the alkyl part of the 
transition states are treated as free rotations as they are relatively loose TSs. 

The dictionary defines CO2 in two ways, allowing the R-R' to insert either way
around. However, there are only rates for one of these ways. The other is
presumably matching the top level node.
"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(0.000102116,'m^3/(mol*s)'), n=3.29652, w0=(820500,'J/mol'), E0=(305487,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.034441443868039615, var=7.910772835870151, Tref=1000.0, N=5, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 5 training reactions at node Root
    Total Standard Deviation in ln(k): 5.725073441582979"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root
Total Standard Deviation in ln(k): 5.725073441582979""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root
Total Standard Deviation in ln(k): 5.725073441582979
""",
)

entry(
    index = 2,
    label = "Root_2CbCdCsHNSSidSis->H",
    kinetics = ArrheniusBM(A=(0.000175732,'m^3/(mol*s)'), n=3.22799, w0=(839250,'J/mol'), E0=(304727,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.09003460388904383, var=3.8152453295400095, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_2CbCdCsHNSSidSis->H',), comment="""BM rule fitted to 4 training reactions at node Root_2CbCdCsHNSSidSis->H
    Total Standard Deviation in ln(k): 4.141997058721065"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_2CbCdCsHNSSidSis->H
Total Standard Deviation in ln(k): 4.141997058721065""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_2CbCdCsHNSSidSis->H
Total Standard Deviation in ln(k): 4.141997058721065
""",
)

entry(
    index = 3,
    label = "Root_N-2CbCdCsHNSSidSis->H",
    kinetics = ArrheniusBM(A=(7.3e-05,'m^3/(mol*s)'), n=3.13, w0=(745500,'J/mol'), E0=(457668,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2CbCdCsHNSSidSis->H',), comment="""BM rule fitted to 1 training reactions at node Root_N-2CbCdCsHNSSidSis->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2CbCdCsHNSSidSis->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2CbCdCsHNSSidSis->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 4,
    label = "Root_2CbCdCsHNSSidSis->H_1CbCdCsHNSSidSis->H",
    kinetics = ArrheniusBM(A=(1510,'m^3/(mol*s)'), n=1.23, w0=(871500,'J/mol'), E0=(307270,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2CbCdCsHNSSidSis->H_1CbCdCsHNSSidSis->H',), comment="""BM rule fitted to 1 training reactions at node Root_2CbCdCsHNSSidSis->H_1CbCdCsHNSSidSis->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2CbCdCsHNSSidSis->H_1CbCdCsHNSSidSis->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2CbCdCsHNSSidSis->H_1CbCdCsHNSSidSis->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_2CbCdCsHNSSidSis->H_N-1CbCdCsHNSSidSis->H",
    kinetics = ArrheniusBM(A=(0.00124375,'m^3/(mol*s)'), n=2.93231, w0=(828500,'J/mol'), E0=(310232,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0075186726087721435, var=1.1062410781291196, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_2CbCdCsHNSSidSis->H_N-1CbCdCsHNSSidSis->H',), comment="""BM rule fitted to 3 training reactions at node Root_2CbCdCsHNSSidSis->H_N-1CbCdCsHNSSidSis->H
    Total Standard Deviation in ln(k): 2.1274313108796026"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_2CbCdCsHNSSidSis->H_N-1CbCdCsHNSSidSis->H
Total Standard Deviation in ln(k): 2.1274313108796026""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_2CbCdCsHNSSidSis->H_N-1CbCdCsHNSSidSis->H
Total Standard Deviation in ln(k): 2.1274313108796026
""",
)

entry(
    index = 6,
    label = "Root_2CbCdCsHNSSidSis->H_N-1CbCdCsHNSSidSis->H_Ext-1Cs-R",
    kinetics = ArrheniusBM(A=(0.00469141,'m^3/(mol*s)'), n=2.69282, w0=(828500,'J/mol'), E0=(309525,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.895124125462989e-05, var=2.520758984959268, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2CbCdCsHNSSidSis->H_N-1CbCdCsHNSSidSis->H_Ext-1Cs-R',), comment="""BM rule fitted to 2 training reactions at node Root_2CbCdCsHNSSidSis->H_N-1CbCdCsHNSSidSis->H_Ext-1Cs-R
    Total Standard Deviation in ln(k): 3.1829953545126424"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2CbCdCsHNSSidSis->H_N-1CbCdCsHNSSidSis->H_Ext-1Cs-R
Total Standard Deviation in ln(k): 3.1829953545126424""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2CbCdCsHNSSidSis->H_N-1CbCdCsHNSSidSis->H_Ext-1Cs-R
Total Standard Deviation in ln(k): 3.1829953545126424
""",
)

entry(
    index = 7,
    label = "Root_2CbCdCsHNSSidSis->H_N-1CbCdCsHNSSidSis->H_Ext-1Cs-R_Ext-1Cs-R",
    kinetics = ArrheniusBM(A=(0.106,'m^3/(mol*s)'), n=2.13, w0=(828500,'J/mol'), E0=(307743,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2CbCdCsHNSSidSis->H_N-1CbCdCsHNSSidSis->H_Ext-1Cs-R_Ext-1Cs-R',), comment="""BM rule fitted to 1 training reactions at node Root_2CbCdCsHNSSidSis->H_N-1CbCdCsHNSSidSis->H_Ext-1Cs-R_Ext-1Cs-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2CbCdCsHNSSidSis->H_N-1CbCdCsHNSSidSis->H_Ext-1Cs-R_Ext-1Cs-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2CbCdCsHNSSidSis->H_N-1CbCdCsHNSSidSis->H_Ext-1Cs-R_Ext-1Cs-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

