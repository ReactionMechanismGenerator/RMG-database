#!/usr/bin/env python
# encoding: utf-8

name = "HO2_Elimination_from_PeroxyRadical/rules"
shortDesc = ""
longDesc = """
General comments go at the top of the file,

or in a section(s) titled 'General'

.. the ID must match those in the rateLibrary AS A STRING (ie. '2' is different from '02')
"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(1.78412e+13,'s^-1'), n=-0.108123, w0=(756.562,'kJ/mol'), E0=(87.6069,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5180601460176953, var=2.4339146265247202, Tref=1000.0, N=16, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 16 training reactions at node Root
    Total Standard Deviation in ln(k): 4.429247533700703"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root
Total Standard Deviation in ln(k): 4.429247533700703""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root
Total Standard Deviation in ln(k): 4.429247533700703
""",
)

entry(
    index = 2,
    label = "Root_Ext-2CNOSSi-R",
    kinetics = ArrheniusBM(A=(3.42884e+12,'s^-1'), n=0.0693686, w0=(742,'kJ/mol'), E0=(88.9502,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5315153241198234, var=2.9215946783220317, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_Ext-2CNOSSi-R',), comment="""BM rule fitted to 7 training reactions at node Root_Ext-2CNOSSi-R
    Total Standard Deviation in ln(k): 4.7620937370612335"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_Ext-2CNOSSi-R
Total Standard Deviation in ln(k): 4.7620937370612335""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_Ext-2CNOSSi-R
Total Standard Deviation in ln(k): 4.7620937370612335
""",
)

entry(
    index = 3,
    label = "Root_Ext-1CNSSi-R",
    kinetics = ArrheniusBM(A=(1.03664e+13,'s^-1'), n=-0.00508037, w0=(761.417,'kJ/mol'), E0=(79.7907,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.37102717427159054, var=3.226735978979628, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-1CNSSi-R',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-1CNSSi-R
    Total Standard Deviation in ln(k): 4.533358298537413"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-1CNSSi-R
Total Standard Deviation in ln(k): 4.533358298537413""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-1CNSSi-R
Total Standard Deviation in ln(k): 4.533358298537413
""",
)

entry(
    index = 4,
    label = "Root_2CNOSSi->C",
    kinetics = ArrheniusBM(A=(1.90486e+07,'s^-1'), n=1.66868, w0=(742,'kJ/mol'), E0=(74.97,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.645653760605861, var=5.093536649750057, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2CNOSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_2CNOSSi->C
    Total Standard Deviation in ln(k): 8.659267965262588"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2CNOSSi->C
Total Standard Deviation in ln(k): 8.659267965262588""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2CNOSSi->C
Total Standard Deviation in ln(k): 8.659267965262588
""",
)

entry(
    index = 5,
    label = "Root_N-2CNOSSi->C",
    kinetics = Arrhenius(A=(6.38e+12,'s^-1'), n=0, Ea=(123.219,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2CNOSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-2CNOSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2CNOSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2CNOSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 6,
    label = "Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi",
    kinetics = ArrheniusBM(A=(5.10918e+12,'s^-1'), n=0.0187431, w0=(742,'kJ/mol'), E0=(89.2223,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5410234914268949, var=2.921587891372611, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi
    Total Standard Deviation in ln(k): 4.785979624586256"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi
Total Standard Deviation in ln(k): 4.785979624586256""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi
Total Standard Deviation in ln(k): 4.785979624586256
""",
)

entry(
    index = 7,
    label = "Root_Ext-2CNOSSi-R_N-Sp-6R!H-2CNOSSi",
    kinetics = Arrhenius(A=(3.63e+09,'s^-1'), n=1.11, Ea=(178.657,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2CNOSSi-R_N-Sp-6R!H-2CNOSSi',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2CNOSSi-R_N-Sp-6R!H-2CNOSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2CNOSSi-R_N-Sp-6R!H-2CNOSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2CNOSSi-R_N-Sp-6R!H-2CNOSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 8,
    label = "Root_Ext-1CNSSi-R_6R!H->C",
    kinetics = ArrheniusBM(A=(1.02257e+13,'s^-1'), n=-0.00376839, w0=(765.3,'kJ/mol'), E0=(79.7812,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.36493129676317776, var=3.3282243211161475, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-1CNSSi-R_6R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-1CNSSi-R_6R!H->C
    Total Standard Deviation in ln(k): 4.574235529655648"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-1CNSSi-R_6R!H->C
Total Standard Deviation in ln(k): 4.574235529655648""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-1CNSSi-R_6R!H->C
Total Standard Deviation in ln(k): 4.574235529655648
""",
)

entry(
    index = 9,
    label = "Root_Ext-1CNSSi-R_N-6R!H->C",
    kinetics = Arrhenius(A=(8.66667e+08,'s^-1'), n=1.2, Ea=(142.674,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1CNSSi-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1CNSSi-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1CNSSi-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1CNSSi-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi_Ext-2CNOSSi-R",
    kinetics = ArrheniusBM(A=(3.90825e+14,'s^-1'), n=-0.462115, w0=(742,'kJ/mol'), E0=(95.6739,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5692208182410083, var=10.898111239664464, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi_Ext-2CNOSSi-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi_Ext-2CNOSSi-R
    Total Standard Deviation in ln(k): 8.048292128412134"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi_Ext-2CNOSSi-R
Total Standard Deviation in ln(k): 8.048292128412134""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi_Ext-2CNOSSi-R
Total Standard Deviation in ln(k): 8.048292128412134
""",
)

entry(
    index = 11,
    label = "Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi_Ext-1CNSSi-R",
    kinetics = ArrheniusBM(A=(4.5004e+12,'s^-1'), n=-0.0540427, w0=(742,'kJ/mol'), E0=(83.8869,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6455429291903173, var=1.8028066113531251, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi_Ext-1CNSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi_Ext-1CNSSi-R
    Total Standard Deviation in ln(k): 4.313697565290574"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi_Ext-1CNSSi-R
Total Standard Deviation in ln(k): 4.313697565290574""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi_Ext-1CNSSi-R
Total Standard Deviation in ln(k): 4.313697565290574
""",
)

entry(
    index = 12,
    label = "Root_Ext-1CNSSi-R_6R!H->C_Ext-1CNSSi-R",
    kinetics = Arrhenius(A=(7.48e+09,'s^-1'), n=1.08, Ea=(124.265,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-1CNSSi-R_6R!H->C_Ext-1CNSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-1CNSSi-R_6R!H->C_Ext-1CNSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-1CNSSi-R_6R!H->C_Ext-1CNSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-1CNSSi-R_6R!H->C_Ext-1CNSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "Root_Ext-1CNSSi-R_6R!H->C_Ext-6C-R",
    kinetics = ArrheniusBM(A=(825300,'s^-1'), n=1.829, w0=(742,'kJ/mol'), E0=(61.9225,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08973995196239858, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-1CNSSi-R_6R!H->C_Ext-6C-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1CNSSi-R_6R!H->C_Ext-6C-R
    Total Standard Deviation in ln(k): 0.22547726623718234"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1CNSSi-R_6R!H->C_Ext-6C-R
Total Standard Deviation in ln(k): 0.22547726623718234""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1CNSSi-R_6R!H->C_Ext-6C-R
Total Standard Deviation in ln(k): 0.22547726623718234
""",
)

entry(
    index = 14,
    label = "Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi_Ext-2CNOSSi-R_Ext-1CNSSi-R",
    kinetics = ArrheniusBM(A=(8.58698e+16,'s^-1'), n=-1.11567, w0=(742,'kJ/mol'), E0=(96.5958,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5862151225609914, var=25.59049467959897, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi_Ext-2CNOSSi-R_Ext-1CNSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi_Ext-2CNOSSi-R_Ext-1CNSSi-R
    Total Standard Deviation in ln(k): 11.614265361156251"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi_Ext-2CNOSSi-R_Ext-1CNSSi-R
Total Standard Deviation in ln(k): 11.614265361156251""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2CNOSSi-R_Sp-6R!H-2CNOSSi_Ext-2CNOSSi-R_Ext-1CNSSi-R
Total Standard Deviation in ln(k): 11.614265361156251
""",
)

