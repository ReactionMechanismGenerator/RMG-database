#!/usr/bin/env python
# encoding: utf-8

name = "concerted_intra_H_alphaQOOH_break/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(5.15717e+07,'s^-1'), n=1.0173, w0=(726500,'J/mol'), E0=(138334,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.057860616033241975, var=5.53741756679145, Tref=1000.0, N=17, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 17 training reactions at node Root
    Total Standard Deviation in ln(k): 4.862864502636233"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root
Total Standard Deviation in ln(k): 4.862864502636233""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root
Total Standard Deviation in ln(k): 4.862864502636233
""",
)

entry(
    index = 2,
    label = "Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(92866.7,'s^-1'), n=1.91166, w0=(726500,'J/mol'), E0=(130149,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.032601008084661515, var=4.201885675538083, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 9 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 4.1913185983438"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 4.1913185983438""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 4.1913185983438
""",
)

entry(
    index = 3,
    label = "Root_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(9011.71,'s^-1'), n=2.47293, w0=(726500,'J/mol'), E0=(140939,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.008792561506656226, var=36.369715353571166, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 12.112109668120619"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 12.112109668120619""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 12.112109668120619
""",
)

entry(
    index = 4,
    label = "Root_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(2230.4,'s^-1'), n=1.92873, w0=(726500,'J/mol'), E0=(120571,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.01776337426393711, var=6.430658361200122, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 5.128387713512485"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 5.128387713512485""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 5.128387713512485
""",
)

entry(
    index = 5,
    label = "Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R_7R!H->O",
    kinetics = ArrheniusBM(A=(2.25627e+09,'s^-1'), n=0.537541, w0=(726500,'J/mol'), E0=(133091,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.002616289110682288, var=6.8206088304700385, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R_7R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R_7R!H->O
    Total Standard Deviation in ln(k): 5.242198929619051"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R_7R!H->O
Total Standard Deviation in ln(k): 5.242198929619051""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R_7R!H->O
Total Standard Deviation in ln(k): 5.242198929619051
""",
)

entry(
    index = 6,
    label = "Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R_N-7R!H->O",
    kinetics = ArrheniusBM(A=(821.577,'s^-1'), n=2.53377, w0=(726500,'J/mol'), E0=(127280,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.055271279971688736, var=5.618623893416952, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R_N-7R!H->O',), comment="""BM rule fitted to 7 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R_N-7R!H->O
    Total Standard Deviation in ln(k): 4.890823743524699"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R_N-7R!H->O
Total Standard Deviation in ln(k): 4.890823743524699""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R_N-7R!H->O
Total Standard Deviation in ln(k): 4.890823743524699
""",
)

entry(
    index = 7,
    label = "Root_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(3.25,'s^-1'), n=3.6, w0=(726500,'J/mol'), E0=(121357,'J/mol'), Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 8,
    label = "Root_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(8243.39,'s^-1'), n=1.5567, w0=(726500,'J/mol'), E0=(120389,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0036252131040513257, var=3.547708378234296, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-9R!H-R
    Total Standard Deviation in ln(k): 3.7850995384093515"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 3.7850995384093515""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 3.7850995384093515
""",
)

entry(
    index = 9,
    label = "Root_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(2745,'s^-1'), n=2.4, w0=(726500,'J/mol'), E0=(126359,'J/mol'), Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R_7R!H->O_Ext-8R!H-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(1.24e+10,'s^-1'), n=0.555, w0=(726500,'J/mol'), E0=(141556,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R_7R!H->O_Ext-8R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R_7R!H->O_Ext-8R!H-R_Ext-9R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R_7R!H->O_Ext-8R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R_7R!H->O_Ext-8R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R_N-7R!H->O_Ext-8R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1.75e+08,'s^-1'), n=1.7, w0=(726500,'J/mol'), E0=(161516,'J/mol'), Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R_N-7R!H->O_Ext-8R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R_N-7R!H->O_Ext-8R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R_N-7R!H->O_Ext-8R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R_N-7R!H->O_Ext-8R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R_N-7R!H->O_Ext-8R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(9.06435,'s^-1'), n=2.92454, w0=(726500,'J/mol'), E0=(114449,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06689999034563439, var=6.648212253453492, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R_N-7R!H->O_Ext-8R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R_N-7R!H->O_Ext-8R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 5.337124890194518"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R_N-7R!H->O_Ext-8R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 5.337124890194518""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R_N-7R!H->O_Ext-8R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 5.337124890194518
""",
)

entry(
    index = 13,
    label = "Root_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-9R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(278.5,'s^-1'), n=1.8, w0=(726500,'J/mol'), E0=(115526,'J/mol'), Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-9R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-9R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-9R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-9R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-9R!H-R_Ext-10R!H-R",
    kinetics = ArrheniusBM(A=(314,'s^-1'), n=2.2, w0=(726500,'J/mol'), E0=(119056,'J/mol'), Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-9R!H-R_Ext-10R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-9R!H-R_Ext-10R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-9R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-9R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R_N-7R!H->O_Ext-8R!H-R_Ext-6R!H-R_Ext-10R!H-R",
    kinetics = ArrheniusBM(A=(73299,'s^-1'), n=1.57992, w0=(726500,'J/mol'), E0=(122989,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.017963180843876842, var=2.31682349271065, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R_N-7R!H->O_Ext-8R!H-R_Ext-6R!H-R_Ext-10R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R_N-7R!H->O_Ext-8R!H-R_Ext-6R!H-R_Ext-10R!H-R
    Total Standard Deviation in ln(k): 3.096563984880861"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R_N-7R!H->O_Ext-8R!H-R_Ext-6R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 3.096563984880861""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R_N-7R!H->O_Ext-8R!H-R_Ext-6R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 3.096563984880861
""",
)

entry(
    index = 16,
    label = "Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R_N-7R!H->O_Ext-8R!H-R_Ext-6R!H-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(175,'s^-1'), n=3.1, w0=(726500,'J/mol'), E0=(124627,'J/mol'), Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R_N-7R!H->O_Ext-8R!H-R_Ext-6R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R_N-7R!H->O_Ext-8R!H-R_Ext-6R!H-R_Ext-9R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R_N-7R!H->O_Ext-8R!H-R_Ext-6R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R_N-7R!H->O_Ext-8R!H-R_Ext-6R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R_N-7R!H->O_Ext-8R!H-R_Ext-6R!H-R_Ext-10R!H-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(2000,'s^-1'), n=1.9, w0=(726500,'J/mol'), E0=(113702,'J/mol'), Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R_N-7R!H->O_Ext-8R!H-R_Ext-6R!H-R_Ext-10R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R_N-7R!H->O_Ext-8R!H-R_Ext-6R!H-R_Ext-10R!H-R_Ext-9R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R_N-7R!H->O_Ext-8R!H-R_Ext-6R!H-R_Ext-10R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R_N-7R!H->O_Ext-8R!H-R_Ext-6R!H-R_Ext-10R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R_N-7R!H->O_Ext-8R!H-R_Ext-6R!H-R_Ext-10R!H-R_Ext-11R!H-R",
    kinetics = ArrheniusBM(A=(254,'s^-1'), n=2.6, w0=(726500,'J/mol'), E0=(125520,'J/mol'), Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R_N-7R!H->O_Ext-8R!H-R_Ext-6R!H-R_Ext-10R!H-R_Ext-11R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R_N-7R!H->O_Ext-8R!H-R_Ext-6R!H-R_Ext-10R!H-R_Ext-11R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R_N-7R!H->O_Ext-8R!H-R_Ext-6R!H-R_Ext-10R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-6R!H-R_Ext-7R!H-R_Ext-2R!H-R_N-7R!H->O_Ext-8R!H-R_Ext-6R!H-R_Ext-10R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

