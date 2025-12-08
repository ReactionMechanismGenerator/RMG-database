#!/usr/bin/env python
# encoding: utf-8

name = "1,2_Insertion_carbene/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(4.30005e+53,'m^3/(mol*s)'), n=-13.5694, w0=(581.04,'kJ/mol'), E0=(337.012,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.5233267459670397, var=98.00751797024216, Tref=1000.0, N=63, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 63 training reactions at node Root
    Total Standard Deviation in ln(k): 23.674080096564104"""),
    rank = 11,
    shortDesc = """BM rule fitted to 63 training reactions at node Root
Total Standard Deviation in ln(k): 23.674080096564104""",
    longDesc = 
"""
BM rule fitted to 63 training reactions at node Root
Total Standard Deviation in ln(k): 23.674080096564104
""",
)

entry(
    index = 2,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H",
    kinetics = ArrheniusBM(A=(1.47559e+25,'m^3/(mol*s)'), n=-5.39954, w0=(604.163,'kJ/mol'), E0=(204.605,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6013619775147557, var=9.016657063212783, Tref=1000.0, N=46, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H',), comment="""BM rule fitted to 46 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
    Total Standard Deviation in ln(k): 7.5307279017446"""),
    rank = 11,
    shortDesc = """BM rule fitted to 46 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 7.5307279017446""",
    longDesc = 
"""
BM rule fitted to 46 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 7.5307279017446
""",
)

entry(
    index = 3,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H",
    kinetics = ArrheniusBM(A=(1.07751e+08,'m^3/(mol*s)'), n=-0.562555, w0=(518.471,'kJ/mol'), E0=(370.115,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6189277179997523, var=35.95234309915544, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H',), comment="""BM rule fitted to 17 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
    Total Standard Deviation in ln(k): 13.57554097482504"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 13.57554097482504""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 13.57554097482504
""",
)

entry(
    index = 4,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R",
    kinetics = ArrheniusBM(A=(1.67081e+07,'m^3/(mol*s)'), n=-0.25099, w0=(584,'kJ/mol'), E0=(109.795,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05783420753682775, var=0.11014630303709819, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R',), comment="""BM rule fitted to 12 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R
    Total Standard Deviation in ln(k): 0.8106495025147907"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R
Total Standard Deviation in ln(k): 0.8106495025147907""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R
Total Standard Deviation in ln(k): 0.8106495025147907
""",
)

entry(
    index = 5,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s",
    kinetics = ArrheniusBM(A=(396.492,'m^3/(mol*s)'), n=1.28632, w0=(529,'kJ/mol'), E0=(73.8371,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3399281796983404, var=2.6054747464730257, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s',), comment="""BM rule fitted to 7 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s
    Total Standard Deviation in ln(k): 4.09003062839241"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s
Total Standard Deviation in ln(k): 4.09003062839241""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s
Total Standard Deviation in ln(k): 4.09003062839241
""",
)

entry(
    index = 6,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s",
    kinetics = ArrheniusBM(A=(2.53375e+19,'m^3/(mol*s)'), n=-3.80026, w0=(632.611,'kJ/mol'), E0=(213.534,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6101362338219153, var=23.976613655258173, Tref=1000.0, N=27, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s',), comment="""BM rule fitted to 27 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s
    Total Standard Deviation in ln(k): 11.349375444939106"""),
    rank = 11,
    shortDesc = """BM rule fitted to 27 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s
Total Standard Deviation in ln(k): 11.349375444939106""",
    longDesc = 
"""
BM rule fitted to 27 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s
Total Standard Deviation in ln(k): 11.349375444939106
""",
)

entry(
    index = 7,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs",
    kinetics = ArrheniusBM(A=(149.329,'m^3/(mol*s)'), n=1.15044, w0=(558.965,'kJ/mol'), E0=(360.634,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.02444579981017453, var=27.257607940150287, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs',), comment="""BM rule fitted to 10 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs
    Total Standard Deviation in ln(k): 10.527906711693689"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs
Total Standard Deviation in ln(k): 10.527906711693689""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs
Total Standard Deviation in ln(k): 10.527906711693689
""",
)

entry(
    index = 8,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs",
    kinetics = ArrheniusBM(A=(0.0284828,'m^3/(mol*s)'), n=1.92223, w0=(481,'kJ/mol'), E0=(274.257,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4205111057330172, var=172.01008088991162, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs',), comment="""BM rule fitted to 7 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs
    Total Standard Deviation in ln(k): 27.34918509141041"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs
Total Standard Deviation in ln(k): 27.34918509141041""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs
Total Standard Deviation in ln(k): 27.34918509141041
""",
)

entry(
    index = 9,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs",
    kinetics = ArrheniusBM(A=(1.13979e+06,'m^3/(mol*s)'), n=0.0863482, w0=(584,'kJ/mol'), E0=(109.454,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.028930789527083983, var=0.07206278047358167, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs',), comment="""BM rule fitted to 3 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs
    Total Standard Deviation in ln(k): 0.6108517669800518"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs
Total Standard Deviation in ln(k): 0.6108517669800518""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs
Total Standard Deviation in ln(k): 0.6108517669800518
""",
)

entry(
    index = 10,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs",
    kinetics = ArrheniusBM(A=(4.08908e+07,'m^3/(mol*s)'), n=-0.363436, w0=(584,'kJ/mol'), E0=(109.908,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06746868073200103, var=0.08249864241260736, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs',), comment="""BM rule fitted to 9 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs
    Total Standard Deviation in ln(k): 0.7453308726894404"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs
Total Standard Deviation in ln(k): 0.7453308726894404""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs
Total Standard Deviation in ln(k): 0.7453308726894404
""",
)

entry(
    index = 11,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_3Br1sCCl1sF1sHI1s->F1s",
    kinetics = Arrhenius(A=(214000,'m^3/(mol*s)'), n=0, Ea=(39.999,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_3Br1sCCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_3Br1sCCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(2.28047e+06,'m^3/(mol*s)'), n=0.110072, w0=(529,'kJ/mol'), E0=(66.8802,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1228852807500813, var=1.6630932046347704, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 6 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 2.8940828089895545"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 2.8940828089895545""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 2.8940828089895545
""",
)

entry(
    index = 13,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H",
    kinetics = ArrheniusBM(A=(0.00894059,'m^3/(mol*s)'), n=2.5125, w0=(621.938,'kJ/mol'), E0=(100.559,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.23244784692196094, var=12.899207574774826, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H',), comment="""BM rule fitted to 8 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H
    Total Standard Deviation in ln(k): 7.7841394335065806"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 7.7841394335065806""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 7.7841394335065806
""",
)

entry(
    index = 14,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H",
    kinetics = ArrheniusBM(A=(2.74024e+08,'m^3/(mol*s)'), n=-0.727258, w0=(637.105,'kJ/mol'), E0=(191.951,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2929637864645238, var=23.484033945739345, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H',), comment="""BM rule fitted to 19 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H
    Total Standard Deviation in ln(k): 10.451101865837275"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 10.451101865837275""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 10.451101865837275
""",
)

entry(
    index = 15,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H",
    kinetics = ArrheniusBM(A=(7.88149e-13,'m^3/(mol*s)'), n=5.26076, w0=(530.8,'kJ/mol'), E0=(296.217,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3459676098171128, var=44.29986627532601, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H',), comment="""BM rule fitted to 5 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H
    Total Standard Deviation in ln(k): 14.212410090385184"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 14.212410090385184""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 14.212410090385184
""",
)

entry(
    index = 16,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H",
    kinetics = ArrheniusBM(A=(0.0013635,'m^3/(mol*s)'), n=2.58942, w0=(616.793,'kJ/mol'), E0=(351.109,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.561374114612063, var=45.216344220470596, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H',), comment="""BM rule fitted to 5 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H
    Total Standard Deviation in ln(k): 19.91607336892996"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 19.91607336892996""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 19.91607336892996
""",
)

entry(
    index = 17,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O",
    kinetics = ArrheniusBM(A=(1.15378e+28,'m^3/(mol*s)'), n=-6.55063, w0=(531,'kJ/mol'), E0=(379.899,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.590729050620465, var=52.21530137929554, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O
    Total Standard Deviation in ln(k): 15.97049077888919"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O
Total Standard Deviation in ln(k): 15.97049077888919""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O
Total Standard Deviation in ln(k): 15.97049077888919
""",
)

entry(
    index = 18,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O",
    kinetics = ArrheniusBM(A=(2.84494e+11,'m^3/(mol*s)'), n=-1.89521, w0=(443.5,'kJ/mol'), E0=(137.781,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4540615412450565, var=34.02892237583595, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O
    Total Standard Deviation in ln(k): 12.83534277500452"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O
Total Standard Deviation in ln(k): 12.83534277500452""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O
Total Standard Deviation in ln(k): 12.83534277500452
""",
)

entry(
    index = 19,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Sp-7R!H=6R!H",
    kinetics = Arrhenius(A=(6.23333e+06,'m^3/(mol*s)'), n=-0.146, Ea=(0.0118826,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(490108,'m^3/(mol*s)'), n=0.201831, w0=(584,'kJ/mol'), E0=(107.984,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.47428387515166337, var=0.06288991772562831, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.6944127300954466"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.6944127300954466""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.6944127300954466
""",
)

entry(
    index = 21,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(9.16873e+07,'m^3/(mol*s)'), n=-0.471498, w0=(584,'kJ/mol'), E0=(108.904,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07514140315329598, var=0.030917555371422278, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R
    Total Standard Deviation in ln(k): 0.5412978538803993"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R
Total Standard Deviation in ln(k): 0.5412978538803993""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R
Total Standard Deviation in ln(k): 0.5412978538803993
""",
)

entry(
    index = 22,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-4Br1sCbCdCl1sCtF1sHO-R",
    kinetics = Arrhenius(A=(2.13e+07,'m^3/(mol*s)'), n=-0.274, Ea=(-2.87022,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-4Br1sCbCdCl1sCtF1sHO-R',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-4Br1sCbCdCl1sCtF1sHO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-4Br1sCbCdCl1sCtF1sHO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-4Br1sCbCdCl1sCtF1sHO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->Ct",
    kinetics = Arrhenius(A=(33.15,'m^3/(mol*s)'), n=1.475, Ea=(-6.90778,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->Ct",
    kinetics = Arrhenius(A=(1.325e+06,'m^3/(mol*s)'), n=0.0073, Ea=(-4.40994,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->H",
    kinetics = Arrhenius(A=(1e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->H',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 26,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H",
    kinetics = ArrheniusBM(A=(1.6968e+06,'m^3/(mol*s)'), n=0.132086, w0=(529,'kJ/mol'), E0=(63.6229,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.14746229953200704, var=1.9511959451670937, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H',), comment="""BM rule fitted to 5 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H
    Total Standard Deviation in ln(k): 3.1708268049501607"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 3.1708268049501607""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 3.1708268049501607
""",
)

entry(
    index = 27,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->H",
    kinetics = Arrhenius(A=(2.33736e+17,'m^3/(mol*s)'), n=-4.54388, Ea=(39.3742,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->H',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H",
    kinetics = ArrheniusBM(A=(463.76,'m^3/(mol*s)'), n=1.17969, w0=(627.5,'kJ/mol'), E0=(125.905,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07066939929040657, var=10.775860019109354, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H',), comment="""BM rule fitted to 7 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H
    Total Standard Deviation in ln(k): 6.758425974856338"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 6.758425974856338""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 6.758425974856338
""",
)

entry(
    index = 29,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C",
    kinetics = ArrheniusBM(A=(6.46741e-12,'m^3/(mol*s)'), n=4.8544, w0=(665.278,'kJ/mol'), E0=(68.466,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2750952906735081, var=15.963039561628669, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C',), comment="""BM rule fitted to 9 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C
    Total Standard Deviation in ln(k): 8.700867166291564"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C
Total Standard Deviation in ln(k): 8.700867166291564""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C
Total Standard Deviation in ln(k): 8.700867166291564
""",
)

entry(
    index = 30,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C",
    kinetics = ArrheniusBM(A=(2.74022e-08,'m^3/(mol*s)'), n=3.90302, w0=(611.75,'kJ/mol'), E0=(176.233,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0518846730424038, var=15.81229105749227, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C',), comment="""BM rule fitted to 10 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C
    Total Standard Deviation in ln(k): 8.102126695562415"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C
Total Standard Deviation in ln(k): 8.102126695562415""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C
Total Standard Deviation in ln(k): 8.102126695562415
""",
)

entry(
    index = 31,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs",
    kinetics = ArrheniusBM(A=(3.27433e+09,'m^3/(mol*s)'), n=-1.00793, w0=(577.983,'kJ/mol'), E0=(403.727,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=11.004081363264657, var=510.03437470682996, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs',), comment="""BM rule fitted to 2 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs
    Total Standard Deviation in ln(k): 72.92326361762518"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs
Total Standard Deviation in ln(k): 72.92326361762518""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs
Total Standard Deviation in ln(k): 72.92326361762518
""",
)

entry(
    index = 32,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs",
    kinetics = ArrheniusBM(A=(3.32355e-13,'m^3/(mol*s)'), n=5.41799, w0=(538.667,'kJ/mol'), E0=(263.22,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.29531828142893024, var=10.482611697361952, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs',), comment="""BM rule fitted to 3 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs
    Total Standard Deviation in ln(k): 7.232708755047147"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs
Total Standard Deviation in ln(k): 7.232708755047147""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs
Total Standard Deviation in ln(k): 7.232708755047147
""",
)

entry(
    index = 33,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs",
    kinetics = Arrhenius(A=(2.22791e-07,'m^3/(mol*s)'), n=3.59921, Ea=(320.496,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs',), comment="""BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs",
    kinetics = ArrheniusBM(A=(7.32435e-06,'m^3/(mol*s)'), n=3.24373, w0=(576.289,'kJ/mol'), E0=(339.967,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2008800543015702, var=6.487576677063239, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs',), comment="""BM rule fitted to 4 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs
    Total Standard Deviation in ln(k): 5.610928693285066"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs
Total Standard Deviation in ln(k): 5.610928693285066""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs
Total Standard Deviation in ln(k): 5.610928693285066
""",
)

entry(
    index = 35,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(2.25815e+07,'m^3/(mol*s)'), n=-0.647497, w0=(531,'kJ/mol'), E0=(341.875,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=8.438505347300241, var=310.4176015602939, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 2 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 56.52304443307441"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 56.52304443307441""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 56.52304443307441
""",
)

entry(
    index = 36,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O_N-2Br1sCl1sF1sHI1s->F1s",
    kinetics = Arrhenius(A=(1.26474e-05,'m^3/(mol*s)'), n=2.95311, Ea=(59.8071,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O_N-2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O_N-2Br1sCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O_N-2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O_N-2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->Cl1s",
    kinetics = ArrheniusBM(A=(1.55937e+21,'m^3/(mol*s)'), n=-4.1602, w0=(473.5,'kJ/mol'), E0=(191.487,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=4.503809742819507, var=53.833815132058966, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->Cl1s',), comment="""BM rule fitted to 2 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->Cl1s
    Total Standard Deviation in ln(k): 26.025153003555154"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->Cl1s
Total Standard Deviation in ln(k): 26.025153003555154""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->Cl1s
Total Standard Deviation in ln(k): 26.025153003555154
""",
)

entry(
    index = 38,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_N-2Br1sCl1sF1sHI1s->Cl1s",
    kinetics = ArrheniusBM(A=(2.18345,'m^3/(mol*s)'), n=0.764042, w0=(413.5,'kJ/mol'), E0=(18.2016,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.790053776114707, var=13.222171864649557, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_N-2Br1sCl1sF1sHI1s->Cl1s',), comment="""BM rule fitted to 2 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_N-2Br1sCl1sF1sHI1s->Cl1s
    Total Standard Deviation in ln(k): 9.27473846583569"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_N-2Br1sCl1sF1sHI1s->Cl1s
Total Standard Deviation in ln(k): 9.27473846583569""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_N-2Br1sCl1sF1sHI1s->Cl1s
Total Standard Deviation in ln(k): 9.27473846583569
""",
)

entry(
    index = 39,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R",
    kinetics = Arrhenius(A=(4933.33,'m^3/(mol*s)'), n=0.797, Ea=(-4.91202,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 40,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Sp-6R!H-4Br1sCbCdCl1sCtF1sHO",
    kinetics = Arrhenius(A=(36700,'m^3/(mol*s)'), n=0.498, Ea=(-7.35547,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Sp-6R!H-4Br1sCbCdCl1sCtF1sHO',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Sp-6R!H-4Br1sCbCdCl1sCtF1sHO
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Sp-6R!H-4Br1sCbCdCl1sCtF1sHO
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_Sp-6R!H-4Br1sCbCdCl1sCtF1sHO
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO",
    kinetics = ArrheniusBM(A=(1.10825e+08,'m^3/(mol*s)'), n=-0.494291, w0=(584,'kJ/mol'), E0=(108.923,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07395629059949477, var=0.029136335316146046, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO',), comment="""BM rule fitted to 5 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO
    Total Standard Deviation in ln(k): 0.5280154505842135"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO
Total Standard Deviation in ln(k): 0.5280154505842135""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO
Total Standard Deviation in ln(k): 0.5280154505842135
""",
)

entry(
    index = 42,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R",
    kinetics = ArrheniusBM(A=(216154,'m^3/(mol*s)'), n=0.41647, w0=(529,'kJ/mol'), E0=(66.7368,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12186484989945345, var=2.914903945292179, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R',), comment="""BM rule fitted to 4 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R
    Total Standard Deviation in ln(k): 3.72889528571959"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R
Total Standard Deviation in ln(k): 3.72889528571959""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R
Total Standard Deviation in ln(k): 3.72889528571959
""",
)

entry(
    index = 43,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(1015.46,'m^3/(mol*s)'), n=0.966596, w0=(638.875,'kJ/mol'), E0=(136.758,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11904686342549113, var=11.577371977767495, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s',), comment="""BM rule fitted to 4 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s
    Total Standard Deviation in ln(k): 7.1203315645943075"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s
Total Standard Deviation in ln(k): 7.1203315645943075""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s
Total Standard Deviation in ln(k): 7.1203315645943075
""",
)

entry(
    index = 44,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(1.26572,'m^3/(mol*s)'), n=2.06839, w0=(612.333,'kJ/mol'), E0=(44.6025,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4485521228400918, var=7.396541472899672, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s',), comment="""BM rule fitted to 3 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s
    Total Standard Deviation in ln(k): 6.579209851795327"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s
Total Standard Deviation in ln(k): 6.579209851795327""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s
Total Standard Deviation in ln(k): 6.579209851795327
""",
)

entry(
    index = 45,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs",
    kinetics = ArrheniusBM(A=(0.00743795,'m^3/(mol*s)'), n=2.17675, w0=(584,'kJ/mol'), E0=(172.195,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.023331098161077896, var=3.374095881581692, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs',), comment="""BM rule fitted to 3 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs
    Total Standard Deviation in ln(k): 3.741061018523575"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs
Total Standard Deviation in ln(k): 3.741061018523575""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs
Total Standard Deviation in ln(k): 3.741061018523575
""",
)

entry(
    index = 46,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs",
    kinetics = ArrheniusBM(A=(1.02129e-05,'m^3/(mol*s)'), n=3.11928, w0=(705.917,'kJ/mol'), E0=(64.7805,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17238204106895547, var=2.5279296375530644, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs',), comment="""BM rule fitted to 6 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs
    Total Standard Deviation in ln(k): 3.6205420775848647"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs
Total Standard Deviation in ln(k): 3.6205420775848647""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs
Total Standard Deviation in ln(k): 3.6205420775848647
""",
)

entry(
    index = 47,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cl1s",
    kinetics = ArrheniusBM(A=(1.3079e+13,'m^3/(mol*s)'), n=-2.4865, w0=(583,'kJ/mol'), E0=(113.481,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.9802769474520832, var=6.746761737390621, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cl1s',), comment="""BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cl1s
    Total Standard Deviation in ln(k): 7.670212411644807"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cl1s
Total Standard Deviation in ln(k): 7.670212411644807""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cl1s
Total Standard Deviation in ln(k): 7.670212411644807
""",
)

entry(
    index = 48,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s",
    kinetics = ArrheniusBM(A=(5.97796e-07,'m^3/(mol*s)'), n=3.52893, w0=(618.938,'kJ/mol'), E0=(182.551,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.034815813240342545, var=14.085152584943291, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s',), comment="""BM rule fitted to 8 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s
    Total Standard Deviation in ln(k): 7.611286012341976"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s
Total Standard Deviation in ln(k): 7.611286012341976""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s
Total Standard Deviation in ln(k): 7.611286012341976
""",
)

entry(
    index = 49,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_3Br1sCCl1sF1sHI1s->H",
    kinetics = Arrhenius(A=(0.000166864,'m^3/(mol*s)'), n=2.82973, Ea=(154.574,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_3Br1sCCl1sF1sHI1s->H',), comment="""BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_3Br1sCCl1sF1sHI1s->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_3Br1sCCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_3Br1sCCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 50,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-3Br1sCCl1sF1sHI1s->H",
    kinetics = Arrhenius(A=(5.7066e-06,'m^3/(mol*s)'), n=3.19155, Ea=(216.984,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-3Br1sCCl1sF1sHI1s->H',), comment="""BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-3Br1sCCl1sF1sHI1s->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-3Br1sCCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-3Br1sCCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 51,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_5Br1sCl1sF1s->Br1s",
    kinetics = Arrhenius(A=(3.01249e-05,'m^3/(mol*s)'), n=3.17037, Ea=(120.81,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_5Br1sCl1sF1s->Br1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_5Br1sCl1sF1s->Br1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_5Br1sCl1sF1s->Br1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_5Br1sCl1sF1s->Br1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 52,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Br1s",
    kinetics = ArrheniusBM(A=(7.00651e-11,'m^3/(mol*s)'), n=4.73603, w0=(579,'kJ/mol'), E0=(277.591,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=6.981466752822914, var=192.7601605666135, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Br1s',), comment="""BM rule fitted to 2 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Br1s
    Total Standard Deviation in ln(k): 45.37473325427515"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Br1s
Total Standard Deviation in ln(k): 45.37473325427515""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Br1s
Total Standard Deviation in ln(k): 45.37473325427515
""",
)

entry(
    index = 53,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_Ext-4Cs-R",
    kinetics = Arrhenius(A=(1.33582e-06,'m^3/(mol*s)'), n=3.3552, Ea=(272.197,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_Ext-4Cs-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_Ext-4Cs-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_Ext-4Cs-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_Ext-4Cs-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 54,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_5Br1sCl1sF1s->Cl1s",
    kinetics = Arrhenius(A=(3.42311e-06,'m^3/(mol*s)'), n=3.42841, Ea=(214.884,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_5Br1sCl1sF1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_5Br1sCl1sF1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_5Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_5Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 55,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Cl1s",
    kinetics = ArrheniusBM(A=(2.54272e-08,'m^3/(mol*s)'), n=3.94901, w0=(558,'kJ/mol'), E0=(332.159,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.3381213615549306, var=17.352834998219944, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Cl1s',), comment="""BM rule fitted to 2 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Cl1s
    Total Standard Deviation in ln(k): 14.225748403311506"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 14.225748403311506""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 14.225748403311506
""",
)

entry(
    index = 56,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->F1s_3Br1sCCl1sF1sHI1s->H",
    kinetics = Arrhenius(A=(2.12553e-07,'m^3/(mol*s)'), n=3.34134, Ea=(111.339,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->F1s_3Br1sCCl1sF1sHI1s->H',), comment="""BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->F1s_3Br1sCCl1sF1sHI1s->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->F1s_3Br1sCCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->F1s_3Br1sCCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 57,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->F1s_N-3Br1sCCl1sF1sHI1s->H",
    kinetics = Arrhenius(A=(1.40908e-07,'m^3/(mol*s)'), n=3.45227, Ea=(176.699,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->F1s_N-3Br1sCCl1sF1sHI1s->H',), comment="""BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->F1s_N-3Br1sCCl1sF1sHI1s->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->F1s_N-3Br1sCCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->F1s_N-3Br1sCCl1sF1sHI1s->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 58,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->Cl1s_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cl1s",
    kinetics = Arrhenius(A=(3e+07,'m^3/(mol*s)'), n=0, Ea=(25.104,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->Cl1s_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->Cl1s_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->Cl1s_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->Cl1s_5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 59,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->Cl1s_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cl1s",
    kinetics = Arrhenius(A=(739000,'m^3/(mol*s)'), n=0, Ea=(49.7896,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->Cl1s_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->Cl1s_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->Cl1s_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_2Br1sCl1sF1sHI1s->Cl1s_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 60,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_N-2Br1sCl1sF1sHI1s->Cl1s_4Br1sCbCdCl1sCtF1sH->Cl1s",
    kinetics = Arrhenius(A=(321,'m^3/(mol*s)'), n=0, Ea=(8.82824,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_N-2Br1sCl1sF1sHI1s->Cl1s_4Br1sCbCdCl1sCtF1sH->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_N-2Br1sCl1sF1sHI1s->Cl1s_4Br1sCbCdCl1sCtF1sH->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_N-2Br1sCl1sF1sHI1s->Cl1s_4Br1sCbCdCl1sCtF1sH->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_N-2Br1sCl1sF1sHI1s->Cl1s_4Br1sCbCdCl1sCtF1sH->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 61,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_N-2Br1sCl1sF1sHI1s->Cl1s_N-4Br1sCbCdCl1sCtF1sH->Cl1s",
    kinetics = Arrhenius(A=(3200,'m^3/(mol*s)'), n=0, Ea=(4.30952,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_N-2Br1sCl1sF1sHI1s->Cl1s_N-4Br1sCbCdCl1sCtF1sH->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_N-2Br1sCl1sF1sHI1s->Cl1s_N-4Br1sCbCdCl1sCtF1sH->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_N-2Br1sCl1sF1sHI1s->Cl1s_N-4Br1sCbCdCl1sCtF1sH->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-4Br1sCbCdCl1sCtF1sHO->O_N-2Br1sCl1sF1sHI1s->Cl1s_N-4Br1sCbCdCl1sCtF1sH->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 62,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_Sp-7R!H=6R!H",
    kinetics = Arrhenius(A=(70000,'m^3/(mol*s)'), n=0.465, Ea=(-7.28853,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_Sp-7R!H=6R!H',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 63,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.27295e+08,'m^3/(mol*s)'), n=-0.522177, w0=(584,'kJ/mol'), E0=(109.449,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0723630864830317, var=0.01117157508829927, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 4 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 0.39370862147891594"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.39370862147891594""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.39370862147891594
""",
)

entry(
    index = 64,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R_Ext-3Br1sCCl1sH-R",
    kinetics = ArrheniusBM(A=(380.996,'m^3/(mol*s)'), n=1.18611, w0=(529,'kJ/mol'), E0=(74.7001,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7102492569695187, var=0.8256572923853683, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R_Ext-3Br1sCCl1sH-R',), comment="""BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R_Ext-3Br1sCCl1sH-R
    Total Standard Deviation in ln(k): 3.6061621558257553"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R_Ext-3Br1sCCl1sH-R
Total Standard Deviation in ln(k): 3.6061621558257553""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R_Ext-3Br1sCCl1sH-R
Total Standard Deviation in ln(k): 3.6061621558257553
""",
)

entry(
    index = 65,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R_6R!H->C",
    kinetics = Arrhenius(A=(3.92494,'m^3/(mol*s)'), n=1.71005, Ea=(-27.1019,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 66,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R_N-6R!H->C",
    kinetics = Arrhenius(A=(264.856,'m^3/(mol*s)'), n=1.35424, Ea=(-5.31624,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 67,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_4CbCdCl1sCsCtF1sHO->Cs",
    kinetics = Arrhenius(A=(2.79958e-05,'m^3/(mol*s)'), n=3.10993, Ea=(26.3876,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_4CbCdCl1sCsCtF1sHO->Cs',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_4CbCdCl1sCsCtF1sHO->Cs
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_4CbCdCl1sCsCtF1sHO->Cs
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_4CbCdCl1sCsCtF1sHO->Cs
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 68,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs",
    kinetics = ArrheniusBM(A=(165413,'m^3/(mol*s)'), n=0.340384, w0=(657.167,'kJ/mol'), E0=(134.388,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18341100062289362, var=8.915352774860462, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs',), comment="""BM rule fitted to 3 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs
    Total Standard Deviation in ln(k): 6.446687532806618"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs
Total Standard Deviation in ln(k): 6.446687532806618""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs
Total Standard Deviation in ln(k): 6.446687532806618
""",
)

entry(
    index = 69,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s_4CbCdCl1sCsCtF1sHO->Cl1s",
    kinetics = Arrhenius(A=(1e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s_4CbCdCl1sCsCtF1sHO->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s_4CbCdCl1sCsCtF1sHO->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s_4CbCdCl1sCsCtF1sHO->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s_4CbCdCl1sCsCtF1sHO->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 70,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cl1s",
    kinetics = ArrheniusBM(A=(7.59917,'m^3/(mol*s)'), n=1.89141, w0=(627,'kJ/mol'), E0=(126.772,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.0394544596457838, var=0.3638912372950381, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cl1s',), comment="""BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cl1s
    Total Standard Deviation in ln(k): 3.8210189462416184"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cl1s
Total Standard Deviation in ln(k): 3.8210189462416184""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cl1s
Total Standard Deviation in ln(k): 3.8210189462416184
""",
)

entry(
    index = 71,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs_2Br1sCl1sF1s->F1s",
    kinetics = Arrhenius(A=(3.33872e-07,'m^3/(mol*s)'), n=3.38172, Ea=(55.0573,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs_2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs_2Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 72,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(5.00807e-06,'m^3/(mol*s)'), n=3.10588, w0=(584,'kJ/mol'), E0=(155.269,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=4.554751041316875, var=0.20403171106326037, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 12.349634312037445"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 12.349634312037445""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 12.349634312037445
""",
)

entry(
    index = 73,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.44246e-08,'m^3/(mol*s)'), n=3.90274, w0=(730.5,'kJ/mol'), E0=(68.9596,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3126567050200818, var=8.370718462765254, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_Ext-3C-R
    Total Standard Deviation in ln(k): 6.585708016680295"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_Ext-3C-R
Total Standard Deviation in ln(k): 6.585708016680295""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_Ext-3C-R
Total Standard Deviation in ln(k): 6.585708016680295
""",
)

entry(
    index = 74,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_2Br1sCl1sF1s->Cl1s",
    kinetics = Arrhenius(A=(112.911,'m^3/(mol*s)'), n=1.11181, Ea=(14.3945,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_2Br1sCl1sF1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_2Br1sCl1sF1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_2Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_2Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 75,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->Cl1s",
    kinetics = ArrheniusBM(A=(17.8899,'m^3/(mol*s)'), n=1.2765, w0=(656.75,'kJ/mol'), E0=(94.5563,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5513237759929538, var=0.29465366767184964, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->Cl1s',), comment="""BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->Cl1s
    Total Standard Deviation in ln(k): 2.4734461256439864"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 2.4734461256439864""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 2.4734461256439864
""",
)

entry(
    index = 76,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->Cl1s",
    kinetics = Arrhenius(A=(0.109762,'m^3/(mol*s)'), n=1.4247, Ea=(-23.1333,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 77,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->Cl1s",
    kinetics = Arrhenius(A=(1.9521,'m^3/(mol*s)'), n=1.31015, Ea=(25.7214,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 78,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(1.37306e-13,'m^3/(mol*s)'), n=5.46154, w0=(638.875,'kJ/mol'), E0=(180.908,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06377445459910688, var=26.455849515686403, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 4 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 10.471642329618119"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 10.471642329618119""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 10.471642329618119
""",
)

entry(
    index = 79,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(1.55283e-16,'m^3/(mol*s)'), n=6.2448, w0=(599,'kJ/mol'), E0=(134.525,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.41275689388512043, var=3.2482144216748603, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 4 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 4.650172238457119"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 4.650172238457119""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 4.650172238457119
""",
)

entry(
    index = 80,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Br1s_5Cl1sF1s->Cl1s",
    kinetics = Arrhenius(A=(1.78425e-05,'m^3/(mol*s)'), n=3.22746, Ea=(130.179,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Br1s_5Cl1sF1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Br1s_5Cl1sF1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Br1s_5Cl1sF1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Br1s_5Cl1sF1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 81,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Br1s_N-5Cl1sF1s->Cl1s",
    kinetics = Arrhenius(A=(4.96165e-06,'m^3/(mol*s)'), n=3.30609, Ea=(133.548,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Br1s_N-5Cl1sF1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Br1s_N-5Cl1sF1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Br1s_N-5Cl1sF1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Br1s_N-5Cl1sF1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 82,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Cl1s_5Br1sF1s->F1s",
    kinetics = Arrhenius(A=(6.158e-07,'m^3/(mol*s)'), n=3.54561, Ea=(195.225,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Cl1s_5Br1sF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Cl1s_5Br1sF1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Cl1s_5Br1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Cl1s_5Br1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 83,
    label = "Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Cl1s_N-5Br1sF1s->F1s",
    kinetics = Arrhenius(A=(7.43831e-06,'m^3/(mol*s)'), n=3.35156, Ea=(209.26,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Cl1s_N-5Br1sF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Cl1s_N-5Br1sF1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Cl1s_N-5Br1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_N-2Br1sCl1sF1sHI1s->H_N-5Br1sCbCdCl1sCsCtF1sI1sNSSidSis->Cs_N-5Br1sCl1sF1s->Cl1s_N-5Br1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 84,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(5.40342e+08,'m^3/(mol*s)'), n=-0.740623, w0=(584,'kJ/mol'), E0=(109.227,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7870344623206381, var=0.09796882358847878, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_Ext-7R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_Ext-7R!H-R
    Total Standard Deviation in ln(k): 2.6049550376933337"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 2.6049550376933337""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 2.6049550376933337
""",
)

entry(
    index = 85,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_4Br1sCbCdCl1sCtF1sHO->Ct",
    kinetics = Arrhenius(A=(203,'m^3/(mol*s)'), n=1.249, Ea=(-9.26338,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_4Br1sCbCdCl1sCtF1sHO->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_4Br1sCbCdCl1sCtF1sHO->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_4Br1sCbCdCl1sCtF1sHO->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_4Br1sCbCdCl1sCtF1sHO->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 86,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_N-4Br1sCbCdCl1sCtF1sHO->Ct",
    kinetics = Arrhenius(A=(1.985e+07,'m^3/(mol*s)'), n=-0.324, Ea=(-3.91204,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_N-4Br1sCbCdCl1sCtF1sHO->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_N-4Br1sCbCdCl1sCtF1sHO->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_N-4Br1sCbCdCl1sCtF1sHO->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_N-4Br1sCbCdCl1sCtF1sHO->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 87,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R_Ext-3Br1sCCl1sH-R_Ext-3Br1sCCl1sH-R",
    kinetics = Arrhenius(A=(0.971461,'m^3/(mol*s)'), n=1.9253, Ea=(-2.06442,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R_Ext-3Br1sCCl1sH-R_Ext-3Br1sCCl1sH-R',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R_Ext-3Br1sCCl1sH-R_Ext-3Br1sCCl1sH-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R_Ext-3Br1sCCl1sH-R_Ext-3Br1sCCl1sH-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-3Br1sCCl1sF1sHI1s->F1s_N-2Br1sCl1sF1sHI1s->H_Ext-3Br1sCCl1sH-R_Ext-3Br1sCCl1sH-R_Ext-3Br1sCCl1sH-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 88,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs_4Cl1sF1sHO->O",
    kinetics = Arrhenius(A=(4.67448e-06,'m^3/(mol*s)'), n=3.15288, Ea=(2.84581,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs_4Cl1sF1sHO->O',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs_4Cl1sF1sHO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs_4Cl1sF1sHO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs_4Cl1sF1sHO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 89,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs_N-4Cl1sF1sHO->O",
    kinetics = ArrheniusBM(A=(3.55814,'m^3/(mol*s)'), n=1.78259, w0=(678.75,'kJ/mol'), E0=(108.812,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5157032220446471, var=5.303397096358326, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs_N-4Cl1sF1sHO->O',), comment="""BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs_N-4Cl1sF1sHO->O
    Total Standard Deviation in ln(k): 5.912462339866296"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs_N-4Cl1sF1sHO->O
Total Standard Deviation in ln(k): 5.912462339866296""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs_N-4Cl1sF1sHO->O
Total Standard Deviation in ln(k): 5.912462339866296
""",
)

entry(
    index = 90,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cl1s_3Br1sCCl1s->Cl1s",
    kinetics = Arrhenius(A=(1.39739,'m^3/(mol*s)'), n=2.08325, Ea=(9.93074,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cl1s_3Br1sCCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cl1s_3Br1sCCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cl1s_3Br1sCCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cl1s_3Br1sCCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 91,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-3Br1sCCl1s->Cl1s",
    kinetics = Arrhenius(A=(1.50896,'m^3/(mol*s)'), n=2.11145, Ea=(7.35429,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-3Br1sCCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-3Br1sCCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-3Br1sCCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_N-3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-3Br1sCCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 92,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Cl1s",
    kinetics = Arrhenius(A=(2.24049e-06,'m^3/(mol*s)'), n=3.20888, Ea=(40.549,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 93,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Cl1s",
    kinetics = Arrhenius(A=(2.9253e-06,'m^3/(mol*s)'), n=3.16987, Ea=(35.1917,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 94,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.13331,'m^3/(mol*s)'), n=1.51168, w0=(730.5,'kJ/mol'), E0=(133.165,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.027348021081210358, var=0.0027343189908051193, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 0.1735426536054152"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 0.1735426536054152""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 0.1735426536054152
""",
)

entry(
    index = 95,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->Cl1s_4Cl1sF1sHO->Cl1s",
    kinetics = Arrhenius(A=(2.57491,'m^3/(mol*s)'), n=1.58614, Ea=(10.1384,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->Cl1s_4Cl1sF1sHO->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->Cl1s_4Cl1sF1sHO->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->Cl1s_4Cl1sF1sHO->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->Cl1s_4Cl1sF1sHO->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 96,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->Cl1s_N-4Cl1sF1sHO->Cl1s",
    kinetics = Arrhenius(A=(11.2646,'m^3/(mol*s)'), n=1.26561, Ea=(1.63685,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->Cl1s_N-4Cl1sF1sHO->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->Cl1s_N-4Cl1sF1sHO->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->Cl1s_N-4Cl1sF1sHO->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_N-2Br1sCl1sF1s->Cl1s_N-4Cl1sF1sHO->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 97,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_4CsF1sHO->F1s",
    kinetics = Arrhenius(A=(3.98081e-09,'m^3/(mol*s)'), n=4.16158, Ea=(55.7474,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_4CsF1sHO->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_4CsF1sHO->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_4CsF1sHO->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_4CsF1sHO->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 98,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s",
    kinetics = ArrheniusBM(A=(1.52384e-10,'m^3/(mol*s)'), n=4.59619, w0=(608.333,'kJ/mol'), E0=(205.159,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.014635730876962901, var=14.560499963457204, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s',), comment="""BM rule fitted to 3 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s
    Total Standard Deviation in ln(k): 7.686486043395319"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s
Total Standard Deviation in ln(k): 7.686486043395319""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s
Total Standard Deviation in ln(k): 7.686486043395319
""",
)

entry(
    index = 99,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_4CsF1sHO->Cs",
    kinetics = ArrheniusBM(A=(1.61505e-06,'m^3/(mol*s)'), n=3.40296, w0=(584,'kJ/mol'), E0=(180.376,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.15483021363048757, var=1.0188775063905142, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_4CsF1sHO->Cs',), comment="""BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_4CsF1sHO->Cs
    Total Standard Deviation in ln(k): 2.412589446362772"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_4CsF1sHO->Cs
Total Standard Deviation in ln(k): 2.412589446362772""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_4CsF1sHO->Cs
Total Standard Deviation in ln(k): 2.412589446362772
""",
)

entry(
    index = 100,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_N-4CsF1sHO->Cs",
    kinetics = ArrheniusBM(A=(2.63835e-09,'m^3/(mol*s)'), n=4.14506, w0=(614,'kJ/mol'), E0=(143.299,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.23722374380764366, var=0.04400924715156273, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_N-4CsF1sHO->Cs',), comment="""BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_N-4CsF1sHO->Cs
    Total Standard Deviation in ln(k): 1.0166005209018925"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_N-4CsF1sHO->Cs
Total Standard Deviation in ln(k): 1.0166005209018925""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_N-4CsF1sHO->Cs
Total Standard Deviation in ln(k): 1.0166005209018925
""",
)

entry(
    index = 101,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_Ext-7R!H-R_4Br1sCbCdCl1sCtF1sHO->Cb",
    kinetics = Arrhenius(A=(1.08e+07,'m^3/(mol*s)'), n=-0.272, Ea=(-5.33042,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_Ext-7R!H-R_4Br1sCbCdCl1sCtF1sHO->Cb',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_Ext-7R!H-R_4Br1sCbCdCl1sCtF1sHO->Cb
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_Ext-7R!H-R_4Br1sCbCdCl1sCtF1sHO->Cb
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_Ext-7R!H-R_4Br1sCbCdCl1sCtF1sHO->Cb
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 102,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_Ext-7R!H-R_N-4Br1sCbCdCl1sCtF1sHO->Cb",
    kinetics = Arrhenius(A=(131500,'m^3/(mol*s)'), n=0.313, Ea=(-7.75714,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_Ext-7R!H-R_N-4Br1sCbCdCl1sCtF1sHO->Cb',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_Ext-7R!H-R_N-4Br1sCbCdCl1sCtF1sHO->Cb
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_Ext-7R!H-R_N-4Br1sCbCdCl1sCtF1sHO->Cb
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis-R_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cs_Ext-6R!H-R_N-Sp-6R!H-4Br1sCbCdCl1sCtF1sHO_N-Sp-7R!H=6R!H_Ext-7R!H-R_N-4Br1sCbCdCl1sCtF1sHO->Cb
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 103,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs_N-4Cl1sF1sHO->O_4Cl1sF1sH->H",
    kinetics = Arrhenius(A=(2.13948,'m^3/(mol*s)'), n=1.96174, Ea=(10.3842,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs_N-4Cl1sF1sHO->O_4Cl1sF1sH->H',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs_N-4Cl1sF1sHO->O_4Cl1sF1sH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs_N-4Cl1sF1sHO->O_4Cl1sF1sH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs_N-4Cl1sF1sHO->O_4Cl1sF1sH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 104,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs_N-4Cl1sF1sHO->O_N-4Cl1sF1sH->H",
    kinetics = Arrhenius(A=(0.00948844,'m^3/(mol*s)'), n=2.40423, Ea=(-1.8086,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs_N-4Cl1sF1sHO->O_N-4Cl1sF1sH->H',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs_N-4Cl1sF1sHO->O_N-4Cl1sF1sH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs_N-4Cl1sF1sHO->O_N-4Cl1sF1sH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->H_3Br1sCCl1sF1s->F1s_N-4CbCdCl1sCsCtF1sHO->Cs_N-4Cl1sF1sHO->O_N-4Cl1sF1sH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 105,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_Ext-3C-R_Ext-3C-R_Ext-3C-R",
    kinetics = Arrhenius(A=(6.46471,'m^3/(mol*s)'), n=1.46279, Ea=(27.8967,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_Ext-3C-R_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_Ext-3C-R_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_Ext-3C-R_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cs_Ext-3C-R_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 106,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s_4CsHO->Cs",
    kinetics = Arrhenius(A=(6.68018e-11,'m^3/(mol*s)'), n=4.72997, Ea=(129.265,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s_4CsHO->Cs',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s_4CsHO->Cs
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s_4CsHO->Cs
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s_4CsHO->Cs
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 107,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s_N-4CsHO->Cs",
    kinetics = ArrheniusBM(A=(1.00619e-13,'m^3/(mol*s)'), n=5.49179, w0=(620.5,'kJ/mol'), E0=(183.471,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.020117520822944164, var=15.933120176435315, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s_N-4CsHO->Cs',), comment="""BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s_N-4CsHO->Cs
    Total Standard Deviation in ln(k): 8.052709752900228"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s_N-4CsHO->Cs
Total Standard Deviation in ln(k): 8.052709752900228""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s_N-4CsHO->Cs
Total Standard Deviation in ln(k): 8.052709752900228
""",
)

entry(
    index = 108,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_4CsF1sHO->Cs_2Br1sCl1s->Cl1s",
    kinetics = Arrhenius(A=(3.3398e-07,'m^3/(mol*s)'), n=3.60759, Ea=(71.667,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_4CsF1sHO->Cs_2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_4CsF1sHO->Cs_2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_4CsF1sHO->Cs_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_4CsF1sHO->Cs_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 109,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_4CsF1sHO->Cs_N-2Br1sCl1s->Cl1s",
    kinetics = Arrhenius(A=(5.49685e-07,'m^3/(mol*s)'), n=3.52855, Ea=(62.1777,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_4CsF1sHO->Cs_N-2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_4CsF1sHO->Cs_N-2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_4CsF1sHO->Cs_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_4CsF1sHO->Cs_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 110,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_N-4CsF1sHO->Cs_2Br1sCl1s->Cl1s",
    kinetics = Arrhenius(A=(2.23355e-09,'m^3/(mol*s)'), n=4.16722, Ea=(48.7822,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_N-4CsF1sHO->Cs_2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_N-4CsF1sHO->Cs_2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_N-4CsF1sHO->Cs_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_N-4CsF1sHO->Cs_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 111,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_N-4CsF1sHO->Cs_N-2Br1sCl1s->Cl1s",
    kinetics = Arrhenius(A=(1.67626e-09,'m^3/(mol*s)'), n=4.20006, Ea=(44.8276,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_N-4CsF1sHO->Cs_N-2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_N-4CsF1sHO->Cs_N-2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_N-4CsF1sHO->Cs_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_N-2Br1sCl1sF1s->F1s_N-4CsF1sHO->Cs_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 112,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s_N-4CsHO->Cs_4HO->H",
    kinetics = Arrhenius(A=(3.26413e-09,'m^3/(mol*s)'), n=4.30786, Ea=(109.478,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s_N-4CsHO->Cs_4HO->H',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s_N-4CsHO->Cs_4HO->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s_N-4CsHO->Cs_4HO->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s_N-4CsHO->Cs_4HO->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 113,
    label = "Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s_N-4CsHO->Cs_N-4HO->H",
    kinetics = Arrhenius(A=(1.76395e-12,'m^3/(mol*s)'), n=5.02686, Ea=(72.5674,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s_N-4CsHO->Cs_N-4HO->H',), comment="""BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s_N-4CsHO->Cs_N-4HO->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s_N-4CsHO->Cs_N-4HO->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-2Br1sCl1sF1sHI1s->H_N-3Br1sCCl1sF1sHI1s->C_N-4CbCdCl1sCsCtF1sHO->Cl1s_2Br1sCl1sF1s->F1s_N-4CsF1sHO->F1s_N-4CsHO->Cs_N-4HO->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

