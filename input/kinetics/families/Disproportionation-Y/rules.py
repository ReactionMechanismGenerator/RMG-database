#!/usr/bin/env python
# encoding: utf-8

name = "Disproportionation-Y/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(3.23373e+10,'m^3/(mol*s)'), n=-1.11374, w0=(639114,'J/mol'), E0=(71751.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.037517728311943145, var=5.119388619038298, Tref=1000.0, N=22, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 22 training reactions at node Root
    Total Standard Deviation in ln(k): 4.630192463143264"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root
Total Standard Deviation in ln(k): 4.630192463143264""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root
Total Standard Deviation in ln(k): 4.630192463143264
""",
)

entry(
    index = 2,
    label = "Root_4R->H",
    kinetics = ArrheniusBM(A=(2.54169e+09,'m^3/(mol*s)'), n=-0.745194, w0=(653600,'J/mol'), E0=(56608.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.08862005332600933, var=1.0602797998021696, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_4R->H',), comment="""BM rule fitted to 20 training reactions at node Root_4R->H
    Total Standard Deviation in ln(k): 2.2869369303528115"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_4R->H
Total Standard Deviation in ln(k): 2.2869369303528115""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_4R->H
Total Standard Deviation in ln(k): 2.2869369303528115
""",
)

entry(
    index = 3,
    label = "Root_N-4R->H",
    kinetics = ArrheniusBM(A=(6.16793e+22,'m^3/(mol*s)'), n=-5.14204, w0=(494250,'J/mol'), E0=(77648.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.07116578166380688, var=128.40059898869487, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->H
    Total Standard Deviation in ln(k): 22.895261166764133"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->H
Total Standard Deviation in ln(k): 22.895261166764133""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->H
Total Standard Deviation in ln(k): 22.895261166764133
""",
)

entry(
    index = 4,
    label = "Root_4R->H_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(4.36138e+09,'m^3/(mol*s)'), n=-0.902433, w0=(649864,'J/mol'), E0=(41813.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.08630237420930674, var=0.8328036276570125, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_4R->H_Ext-2R!H-R',), comment="""BM rule fitted to 11 training reactions at node Root_4R->H_Ext-2R!H-R
    Total Standard Deviation in ln(k): 2.0463227793051826"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_4R->H_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.0463227793051826""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_4R->H_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.0463227793051826
""",
)

entry(
    index = 5,
    label = "Root_4R->H_Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(2.08509e+09,'m^3/(mol*s)'), n=-0.556928, w0=(671500,'J/mol'), E0=(67150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.038334311443416605, var=0.5015770793411518, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_4R->H_Sp-2R!H-1R!H',), comment="""BM rule fitted to 5 training reactions at node Root_4R->H_Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 1.516112980431913"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_4R->H_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.516112980431913""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_4R->H_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.516112980431913
""",
)

entry(
    index = 6,
    label = "Root_4R->H_N-Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(7.37471e+08,'m^3/(mol*s)'), n=-0.548118, w0=(641500,'J/mol'), E0=(64150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06539578995210048, var=0.3779534857901618, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R->H_N-Sp-2R!H-1R!H',), comment="""BM rule fitted to 4 training reactions at node Root_4R->H_N-Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 1.396780491423361"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R->H_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.396780491423361""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R->H_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.396780491423361
""",
)

entry(
    index = 7,
    label = "Root_N-4R->H_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(6e+07,'m^3/(mol*s)'), n=0, w0=(540500,'J/mol'), E0=(54105.9,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->H_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->H_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->H_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->H_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 8,
    label = "Root_4R->H_Ext-2R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(3.00811e+09,'m^3/(mol*s)'), n=-0.942415, w0=(653000,'J/mol'), E0=(59151.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.08379358354329436, var=1.3053296642527137, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R->H_Ext-2R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_4R->H_Ext-2R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 2.5009670102947603"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R->H_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.5009670102947603""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R->H_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.5009670102947603
""",
)

entry(
    index = 9,
    label = "Root_4R->H_Ext-2R!H-R_Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(6.12822e+10,'m^3/(mol*s)'), n=-1.27483, w0=(653000,'J/mol'), E0=(65300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.10436566153268591, var=0.43218337890608616, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R->H_Ext-2R!H-R_Sp-2R!H-1R!H',), comment="""BM rule fitted to 4 training reactions at node Root_4R->H_Ext-2R!H-R_Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 1.580151261682526"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R->H_Ext-2R!H-R_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.580151261682526""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R->H_Ext-2R!H-R_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.580151261682526
""",
)

entry(
    index = 10,
    label = "Root_4R->H_Ext-2R!H-R_N-Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(2.11082e+08,'m^3/(mol*s)'), n=-0.352588, w0=(641500,'J/mol'), E0=(64150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06556305828151585, var=0.5832464150564071, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_4R->H_Ext-2R!H-R_N-Sp-2R!H-1R!H',), comment="""BM rule fitted to 3 training reactions at node Root_4R->H_Ext-2R!H-R_N-Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 1.6957589325434401"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_4R->H_Ext-2R!H-R_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.6957589325434401""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_4R->H_Ext-2R!H-R_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.6957589325434401
""",
)

entry(
    index = 11,
    label = "Root_4R->H_Sp-2R!H-1R!H_2R!H->C",
    kinetics = ArrheniusBM(A=(4.45559e+09,'m^3/(mol*s)'), n=-0.69616, w0=(653000,'J/mol'), E0=(65300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04791788904805767, var=0.3109331404557689, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R->H_Sp-2R!H-1R!H_2R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H->C
    Total Standard Deviation in ln(k): 1.2382646335822984"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H->C
Total Standard Deviation in ln(k): 1.2382646335822984""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H->C
Total Standard Deviation in ln(k): 1.2382646335822984
""",
)

entry(
    index = 12,
    label = "Root_4R->H_Sp-2R!H-1R!H_N-2R!H->C",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=0, w0=(745500,'J/mol'), E0=(74550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->H_Sp-2R!H-1R!H_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R->H_Sp-2R!H-1R!H_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->H_Sp-2R!H-1R!H_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->H_Sp-2R!H-1R!H_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "Root_4R->H_N-Sp-2R!H-1R!H_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(1.67536e+08,'m^3/(mol*s)'), n=-0.352589, w0=(641500,'J/mol'), E0=(64150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06556305488210509, var=0.485146560097461, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_4R->H_N-Sp-2R!H-1R!H_Ext-1R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_4R->H_N-Sp-2R!H-1R!H_Ext-1R!H-R
    Total Standard Deviation in ln(k): 1.5610786515608777"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_4R->H_N-Sp-2R!H-1R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 1.5610786515608777""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_4R->H_N-Sp-2R!H-1R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 1.5610786515608777
""",
)

entry(
    index = 14,
    label = "Root_4R->H_Ext-2R!H-R_Ext-2R!H-R_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(6.82563e+08,'m^3/(mol*s)'), n=-0.630496, w0=(653000,'J/mol'), E0=(50929.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.685783535021827, var=1.6157159588823224, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->H_Ext-2R!H-R_Ext-2R!H-R_Ext-1R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_4R->H_Ext-2R!H-R_Ext-2R!H-R_Ext-1R!H-R
    Total Standard Deviation in ln(k): 6.783872141701826"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->H_Ext-2R!H-R_Ext-2R!H-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 6.783872141701826""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->H_Ext-2R!H-R_Ext-2R!H-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 6.783872141701826
""",
)

entry(
    index = 15,
    label = "Root_4R->H_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(1.4799e+10,'m^3/(mol*s)'), n=-1.08354, w0=(653000,'J/mol'), E0=(65300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.11373181040474326, var=0.7070026847525505, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_4R->H_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_4R->H_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R
    Total Standard Deviation in ln(k): 1.9714087678440078"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_4R->H_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 1.9714087678440078""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_4R->H_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 1.9714087678440078
""",
)

entry(
    index = 16,
    label = "Root_4R->H_Ext-2R!H-R_N-Sp-2R!H-1R!H_5R!H->C",
    kinetics = ArrheniusBM(A=(3e+07,'m^3/(mol*s)'), n=0, w0=(641500,'J/mol'), E0=(64150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->H_Ext-2R!H-R_N-Sp-2R!H-1R!H_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R->H_Ext-2R!H-R_N-Sp-2R!H-1R!H_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->H_Ext-2R!H-R_N-Sp-2R!H-1R!H_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->H_Ext-2R!H-R_N-Sp-2R!H-1R!H_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_4R->H_Ext-2R!H-R_N-Sp-2R!H-1R!H_N-5R!H->C",
    kinetics = ArrheniusBM(A=(6.29006e+10,'m^3/(mol*s)'), n=-1.1347, w0=(641500,'J/mol'), E0=(64150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.9762447934156254, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->H_Ext-2R!H-R_N-Sp-2R!H-1R!H_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_4R->H_Ext-2R!H-R_N-Sp-2R!H-1R!H_N-5R!H->C
    Total Standard Deviation in ln(k): 2.452876365365893"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->H_Ext-2R!H-R_N-Sp-2R!H-1R!H_N-5R!H->C
Total Standard Deviation in ln(k): 2.452876365365893""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->H_Ext-2R!H-R_N-Sp-2R!H-1R!H_N-5R!H->C
Total Standard Deviation in ln(k): 2.452876365365893
""",
)

entry(
    index = 18,
    label = "Root_4R->H_Sp-2R!H-1R!H_2R!H->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(2.12927e+09,'m^3/(mol*s)'), n=-0.570904, w0=(653000,'J/mol'), E0=(65300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04460070932531281, var=0.3792944565490591, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_4R->H_Sp-2R!H-1R!H_2R!H->C_Ext-1R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 1.3467159966844713"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 1.3467159966844713""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 1.3467159966844713
""",
)

entry(
    index = 19,
    label = "Root_4R->H_N-Sp-2R!H-1R!H_Ext-1R!H-R_5R!H->C",
    kinetics = ArrheniusBM(A=(3e+07,'m^3/(mol*s)'), n=0, w0=(641500,'J/mol'), E0=(64150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->H_N-Sp-2R!H-1R!H_Ext-1R!H-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R->H_N-Sp-2R!H-1R!H_Ext-1R!H-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->H_N-Sp-2R!H-1R!H_Ext-1R!H-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->H_N-Sp-2R!H-1R!H_Ext-1R!H-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_4R->H_N-Sp-2R!H-1R!H_Ext-1R!H-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(4.44775e+10,'m^3/(mol*s)'), n=-1.1347, w0=(641500,'J/mol'), E0=(64150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.9762447934156255, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->H_N-Sp-2R!H-1R!H_Ext-1R!H-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_4R->H_N-Sp-2R!H-1R!H_Ext-1R!H-R_N-5R!H->C
    Total Standard Deviation in ln(k): 4.418034250478541"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->H_N-Sp-2R!H-1R!H_Ext-1R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 4.418034250478541""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->H_N-Sp-2R!H-1R!H_Ext-1R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 4.418034250478541
""",
)

entry(
    index = 21,
    label = "Root_4R->H_Ext-2R!H-R_Ext-2R!H-R_Ext-1R!H-R_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(1.41e+15,'m^3/(mol*s)'), n=-2.4, w0=(653000,'J/mol'), E0=(65300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->H_Ext-2R!H-R_Ext-2R!H-R_Ext-1R!H-R_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R->H_Ext-2R!H-R_Ext-2R!H-R_Ext-1R!H-R_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->H_Ext-2R!H-R_Ext-2R!H-R_Ext-1R!H-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->H_Ext-2R!H-R_Ext-2R!H-R_Ext-1R!H-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_4R->H_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(8.21893e+09,'m^3/(mol*s)'), n=-1.0104, w0=(653000,'J/mol'), E0=(65300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.1261001299902147, var=2.4138979216251633, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->H_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_Ext-1R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_4R->H_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_Ext-1R!H-R
    Total Standard Deviation in ln(k): 8.456661681503595"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->H_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 8.456661681503595""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->H_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 8.456661681503595
""",
)

entry(
    index = 23,
    label = "Root_4R->H_Ext-2R!H-R_N-Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(5.98e+14,'m^3/(mol*s)'), n=-2.31, w0=(641500,'J/mol'), E0=(64150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->H_Ext-2R!H-R_N-Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R->H_Ext-2R!H-R_N-Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->H_Ext-2R!H-R_N-Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->H_Ext-2R!H-R_N-Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_4R->H_Sp-2R!H-1R!H_2R!H->C_Ext-1R!H-R_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(1.12e+15,'m^3/(mol*s)'), n=-2.27, w0=(653000,'J/mol'), E0=(65300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->H_Sp-2R!H-1R!H_2R!H->C_Ext-1R!H-R_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H->C_Ext-1R!H-R_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H->C_Ext-1R!H-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->H_Sp-2R!H-1R!H_2R!H->C_Ext-1R!H-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

