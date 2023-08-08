#!/usr/bin/env python
# encoding: utf-8

name = "Br_Abstraction/rules"
shortDesc = ""
longDesc = """
General comments go at the top of the file,

or in a section(s) titled 'General'

.. the ID must match those in the rateLibrary AS A STRING (ie. '2' is different from '02')


.. [MRHCBSQB3RRHO] M.R. Harper (mrharper_at_mit_dot_edu or michael.harper.jr_at_gmail_dot_com)
The geometries of all reactants, products, and the transition state were optimized using the CBS-QB3 calculations.  The zero-point
energy is that computed by the CBS-QB3 calculations.  The frequencies were computed with B3LYP/CBSB7.
In computing k(T), an asymmetric tunneling correction was employed, the calculated frequencies were scaled by 0.99, and the
temperatures used were: 300, 331, 370, 419, 482, 568, 692, 885, 1227, 2000 (evenly spaced on inverse temperature scale).

.. [Tsang1990] W. Tsang; "Chemical kinetic database for combustion chemistry. Part IV. Isobutane" J. Phys. Chem. Ref. Data 19 (1990) 1-68

.. [Tsang1991] W. Tsang; "Chemical kinetic database for combustion chemistry. Part V. Propene" J. Phys. Chem. Ref. Data 20 (1991) 221-273
"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(2.27679e+10,'m^3/(mol*s)'), n=-0.983935, w0=(287334,'J/mol'), E0=(64487.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.17581410179615745, var=9.52795296508157, Tref=1000.0, N=192, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 192 training reactions at node Root
    Total Standard Deviation in ln(k): 6.629836399734354"""),
    rank = 11,
    shortDesc = """BM rule fitted to 192 training reactions at node Root
Total Standard Deviation in ln(k): 6.629836399734354""",
    longDesc = 
"""
BM rule fitted to 192 training reactions at node Root
Total Standard Deviation in ln(k): 6.629836399734354
""",
)

entry(
    index = 2,
    label = "Root_1R->H",
    kinetics = ArrheniusBM(A=(1.98363e+06,'m^3/(mol*s)'), n=0.181283, w0=(317796,'J/mol'), E0=(66363.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.09337125855213854, var=2.656566859659815, Tref=1000.0, N=36, data_mean=0.0, correlation='Root_1R->H',), comment="""BM rule fitted to 36 training reactions at node Root_1R->H
    Total Standard Deviation in ln(k): 3.5021144574155345"""),
    rank = 11,
    shortDesc = """BM rule fitted to 36 training reactions at node Root_1R->H
Total Standard Deviation in ln(k): 3.5021144574155345""",
    longDesc = 
"""
BM rule fitted to 36 training reactions at node Root_1R->H
Total Standard Deviation in ln(k): 3.5021144574155345
""",
)

entry(
    index = 3,
    label = "Root_N-1R->H",
    kinetics = ArrheniusBM(A=(3.07227e+16,'m^3/(mol*s)'), n=-2.78777, w0=(280304,'J/mol'), E0=(74942.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.27934103688608586, var=10.553971667687781, Tref=1000.0, N=156, data_mean=0.0, correlation='Root_N-1R->H',), comment="""BM rule fitted to 156 training reactions at node Root_N-1R->H
    Total Standard Deviation in ln(k): 7.214620057187144"""),
    rank = 11,
    shortDesc = """BM rule fitted to 156 training reactions at node Root_N-1R->H
Total Standard Deviation in ln(k): 7.214620057187144""",
    longDesc = 
"""
BM rule fitted to 156 training reactions at node Root_N-1R->H
Total Standard Deviation in ln(k): 7.214620057187144
""",
)

entry(
    index = 4,
    label = "Root_1R->H_3R->C",
    kinetics = ArrheniusBM(A=(2.44308e-12,'m^3/(mol*s)'), n=5.46251, w0=(323500,'J/mol'), E0=(15051.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2168405384925515, var=0.920959263470726, Tref=1000.0, N=29, data_mean=0.0, correlation='Root_1R->H_3R->C',), comment="""BM rule fitted to 29 training reactions at node Root_1R->H_3R->C
    Total Standard Deviation in ln(k): 2.4687020175151537"""),
    rank = 11,
    shortDesc = """BM rule fitted to 29 training reactions at node Root_1R->H_3R->C
Total Standard Deviation in ln(k): 2.4687020175151537""",
    longDesc = 
"""
BM rule fitted to 29 training reactions at node Root_1R->H_3R->C
Total Standard Deviation in ln(k): 2.4687020175151537
""",
)

entry(
    index = 5,
    label = "Root_1R->H_N-3R->C",
    kinetics = ArrheniusBM(A=(1.05603,'m^3/(mol*s)'), n=2.32493, w0=(294167,'J/mol'), E0=(29416.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04682963148057531, var=0.8343115742894281, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R->H_N-3R->C',), comment="""BM rule fitted to 7 training reactions at node Root_1R->H_N-3R->C
    Total Standard Deviation in ln(k): 1.9488005948115545"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R->H_N-3R->C
Total Standard Deviation in ln(k): 1.9488005948115545""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R->H_N-3R->C
Total Standard Deviation in ln(k): 1.9488005948115545
""",
)

entry(
    index = 6,
    label = "Root_N-1R->H_3R->H",
    kinetics = ArrheniusBM(A=(355631,'m^3/(mol*s)'), n=0.777051, w0=(317796,'J/mol'), E0=(52184.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.05885087003189327, var=0.6078015438566834, Tref=1000.0, N=36, data_mean=0.0, correlation='Root_N-1R->H_3R->H',), comment="""BM rule fitted to 36 training reactions at node Root_N-1R->H_3R->H
    Total Standard Deviation in ln(k): 1.7107906108043205"""),
    rank = 11,
    shortDesc = """BM rule fitted to 36 training reactions at node Root_N-1R->H_3R->H
Total Standard Deviation in ln(k): 1.7107906108043205""",
    longDesc = 
"""
BM rule fitted to 36 training reactions at node Root_N-1R->H_3R->H
Total Standard Deviation in ln(k): 1.7107906108043205
""",
)

entry(
    index = 7,
    label = "Root_N-1R->H_N-3R->H",
    kinetics = ArrheniusBM(A=(2.34827e+07,'m^3/(mol*s)'), n=-0.204194, w0=(269056,'J/mol'), E0=(55003.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1433139282765473, var=12.3709890338907, Tref=1000.0, N=120, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H',), comment="""BM rule fitted to 120 training reactions at node Root_N-1R->H_N-3R->H
    Total Standard Deviation in ln(k): 7.411223018027715"""),
    rank = 11,
    shortDesc = """BM rule fitted to 120 training reactions at node Root_N-1R->H_N-3R->H
Total Standard Deviation in ln(k): 7.411223018027715""",
    longDesc = 
"""
BM rule fitted to 120 training reactions at node Root_N-1R->H_N-3R->H
Total Standard Deviation in ln(k): 7.411223018027715
""",
)

entry(
    index = 8,
    label = "Root_1R->H_3R->C_3C-u1",
    kinetics = ArrheniusBM(A=(7.24651e-12,'m^3/(mol*s)'), n=5.30712, w0=(323500,'J/mol'), E0=(22065.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.20246964340952164, var=0.8811436270150597, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1',), comment="""BM rule fitted to 25 training reactions at node Root_1R->H_3R->C_3C-u1
    Total Standard Deviation in ln(k): 2.3905474972887477"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_1R->H_3R->C_3C-u1
Total Standard Deviation in ln(k): 2.3905474972887477""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_1R->H_3R->C_3C-u1
Total Standard Deviation in ln(k): 2.3905474972887477
""",
)

entry(
    index = 9,
    label = "Root_1R->H_3R->C_N-3C-u1",
    kinetics = ArrheniusBM(A=(0.525082,'m^3/(mol*s)'), n=2.16219, w0=(323500,'J/mol'), E0=(39837.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.002363559055877691, var=1.787066878887757, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->H_3R->C_N-3C-u1',), comment="""BM rule fitted to 4 training reactions at node Root_1R->H_3R->C_N-3C-u1
    Total Standard Deviation in ln(k): 2.685892915431505"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->H_3R->C_N-3C-u1
Total Standard Deviation in ln(k): 2.685892915431505""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->H_3R->C_N-3C-u1
Total Standard Deviation in ln(k): 2.685892915431505
""",
)

entry(
    index = 10,
    label = "Root_1R->H_N-3R->C_Ext-3BrClHO-R",
    kinetics = ArrheniusBM(A=(0.0107059,'m^3/(mol*s)'), n=2.94962, w0=(298550,'J/mol'), E0=(29855,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05088746898130236, var=1.783656615851116, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-3R->C_Ext-3BrClHO-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-3R->C_Ext-3BrClHO-R
    Total Standard Deviation in ln(k): 2.8052539851153004"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-3R->C_Ext-3BrClHO-R
Total Standard Deviation in ln(k): 2.8052539851153004""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-3R->C_Ext-3BrClHO-R
Total Standard Deviation in ln(k): 2.8052539851153004
""",
)

entry(
    index = 11,
    label = "Root_1R->H_N-3R->C_3BrClHO-u1",
    kinetics = ArrheniusBM(A=(383.832,'m^3/(mol*s)'), n=1.50809, w0=(288323,'J/mol'), E0=(28832.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.03967429217952225, var=3.4391785705942346, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-3R->C_3BrClHO-u1',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-3R->C_3BrClHO-u1
    Total Standard Deviation in ln(k): 3.8174698495568773"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-3R->C_3BrClHO-u1
Total Standard Deviation in ln(k): 3.8174698495568773""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-3R->C_3BrClHO-u1
Total Standard Deviation in ln(k): 3.8174698495568773
""",
)

entry(
    index = 12,
    label = "Root_1R->H_N-3R->C_N-3BrClHO-u1",
    kinetics = ArrheniusBM(A=(104.591,'m^3/(mol*s)'), n=1.68113, w0=(298550,'J/mol'), E0=(29855,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->C_N-3BrClHO-u1',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_N-3BrClHO-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_N-3BrClHO-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_N-3BrClHO-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.09407,'m^3/(mol*s)'), n=2.40586, w0=(323500,'J/mol'), E0=(38748.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0159328180068142, var=0.5856688571123184, Tref=1000.0, N=29, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C',), comment="""BM rule fitted to 29 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 1.574236009056873"""),
    rank = 11,
    shortDesc = """BM rule fitted to 29 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 1.574236009056873""",
    longDesc = 
"""
BM rule fitted to 29 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 1.574236009056873
""",
)

entry(
    index = 14,
    label = "Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(1691.93,'m^3/(mol*s)'), n=1.51832, w0=(294167,'J/mol'), E0=(29416.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.011245487822828325, var=1.348216547327026, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 2.3560075708137993"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 2.3560075708137993""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 2.3560075708137993
""",
)

entry(
    index = 15,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(9.90849e+07,'m^3/(mol*s)'), n=-0.419281, w0=(278857,'J/mol'), E0=(62408.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.17413570880241505, var=6.2158299118174245, Tref=1000.0, N=92, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C',), comment="""BM rule fitted to 92 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 5.4356454280361515"""),
    rank = 11,
    shortDesc = """BM rule fitted to 92 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 5.4356454280361515""",
    longDesc = 
"""
BM rule fitted to 92 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 5.4356454280361515
""",
)

entry(
    index = 16,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(7.61275e-14,'m^3/(mol*s)'), n=6.00952, w0=(236855,'J/mol'), E0=(-41225.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.8167411992965796, var=12.557082135346782, Tref=1000.0, N=28, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C',), comment="""BM rule fitted to 28 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 14.181213089590988"""),
    rank = 11,
    shortDesc = """BM rule fitted to 28 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 14.181213089590988""",
    longDesc = 
"""
BM rule fitted to 28 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 14.181213089590988
""",
)

entry(
    index = 17,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R",
    kinetics = ArrheniusBM(A=(7.69536e-12,'m^3/(mol*s)'), n=5.29465, w0=(323500,'J/mol'), E0=(22195.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.20736354858000752, var=0.9138844272716529, Tref=1000.0, N=23, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R',), comment="""BM rule fitted to 23 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R
    Total Standard Deviation in ln(k): 2.437486600293049"""),
    rank = 11,
    shortDesc = """BM rule fitted to 23 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R
Total Standard Deviation in ln(k): 2.437486600293049""",
    longDesc = 
"""
BM rule fitted to 23 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R
Total Standard Deviation in ln(k): 2.437486600293049
""",
)

entry(
    index = 18,
    label = "Root_1R->H_3R->C_N-3C-u1_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.63424,'m^3/(mol*s)'), n=1.95806, w0=(323500,'J/mol'), E0=(38998.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.007086042747752114, var=2.859741556579387, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_3R->C_N-3C-u1_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_3R->C_N-3C-u1_Ext-3C-R
    Total Standard Deviation in ln(k): 3.407965588979388"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_3R->C_N-3C-u1_Ext-3C-R
Total Standard Deviation in ln(k): 3.407965588979388""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_3R->C_N-3C-u1_Ext-3C-R
Total Standard Deviation in ln(k): 3.407965588979388
""",
)

entry(
    index = 19,
    label = "Root_1R->H_N-3R->C_Ext-3BrClHO-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(0.00073902,'m^3/(mol*s)'), n=3.38055, w0=(298550,'J/mol'), E0=(29855,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.5200745748538014, var=4.49275642323657, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-3R->C_Ext-3BrClHO-R_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->C_Ext-3BrClHO-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 8.068544036863248"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->C_Ext-3BrClHO-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 8.068544036863248""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->C_Ext-3BrClHO-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 8.068544036863248
""",
)

entry(
    index = 20,
    label = "Root_1R->H_N-3R->C_3BrClHO-u1_3BrClHO->Br",
    kinetics = ArrheniusBM(A=(32771.6,'m^3/(mol*s)'), n=1.02226, w0=(276000,'J/mol'), E0=(27600,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->C_3BrClHO-u1_3BrClHO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_3BrClHO-u1_3BrClHO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_3BrClHO-u1_3BrClHO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_3BrClHO-u1_3BrClHO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_1R->H_N-3R->C_3BrClHO-u1_N-3BrClHO->Br",
    kinetics = ArrheniusBM(A=(383.342,'m^3/(mol*s)'), n=1.50784, w0=(294485,'J/mol'), E0=(29448.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.14113569273627924, var=2.8628671744052863, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-3R->C_3BrClHO-u1_N-3BrClHO->Br',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->C_3BrClHO-u1_N-3BrClHO->Br
    Total Standard Deviation in ln(k): 3.7466259248254445"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->C_3BrClHO-u1_N-3BrClHO->Br
Total Standard Deviation in ln(k): 3.7466259248254445""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->C_3BrClHO-u1_N-3BrClHO->Br
Total Standard Deviation in ln(k): 3.7466259248254445
""",
)

entry(
    index = 22,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0",
    kinetics = ArrheniusBM(A=(7.54353e-05,'m^3/(mol*s)'), n=3.68707, w0=(323500,'J/mol'), E0=(28161.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.09493398414988284, var=0.4658594684837088, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0',), comment="""BM rule fitted to 25 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0
    Total Standard Deviation in ln(k): 1.6068374468667326"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0
Total Standard Deviation in ln(k): 1.6068374468667326""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0
Total Standard Deviation in ln(k): 1.6068374468667326
""",
)

entry(
    index = 23,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0",
    kinetics = ArrheniusBM(A=(348506,'m^3/(mol*s)'), n=0.564412, w0=(323500,'J/mol'), E0=(43173.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.05347247452109321, var=1.1096892032489478, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0
    Total Standard Deviation in ln(k): 2.246176700885173"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0
Total Standard Deviation in ln(k): 2.246176700885173""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0
Total Standard Deviation in ln(k): 2.246176700885173
""",
)

entry(
    index = 24,
    label = "Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl",
    kinetics = ArrheniusBM(A=(381135,'m^3/(mol*s)'), n=0.513067, w0=(290420,'J/mol'), E0=(29042,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl",
    kinetics = ArrheniusBM(A=(717.402,'m^3/(mol*s)'), n=1.69038, w0=(294792,'J/mol'), E0=(29479.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.011966567967005319, var=0.5437046947403953, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl
    Total Standard Deviation in ln(k): 1.508284905576342"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl
Total Standard Deviation in ln(k): 1.508284905576342""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl
Total Standard Deviation in ln(k): 1.508284905576342
""",
)

entry(
    index = 26,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1",
    kinetics = ArrheniusBM(A=(2.53445e+07,'m^3/(mol*s)'), n=-0.253756, w0=(279589,'J/mol'), E0=(61855.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.16557750971200746, var=6.002483268947115, Tref=1000.0, N=86, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1',), comment="""BM rule fitted to 86 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1
    Total Standard Deviation in ln(k): 5.327617988190518"""),
    rank = 11,
    shortDesc = """BM rule fitted to 86 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1
Total Standard Deviation in ln(k): 5.327617988190518""",
    longDesc = 
"""
BM rule fitted to 86 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1
Total Standard Deviation in ln(k): 5.327617988190518
""",
)

entry(
    index = 27,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1",
    kinetics = ArrheniusBM(A=(16595.1,'m^3/(mol*s)'), n=0.87482, w0=(268367,'J/mol'), E0=(40366.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.08960954255872788, var=4.284275912478388, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1
    Total Standard Deviation in ln(k): 4.374648998270802"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1
Total Standard Deviation in ln(k): 4.374648998270802""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1
Total Standard Deviation in ln(k): 4.374648998270802
""",
)

entry(
    index = 28,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R",
    kinetics = ArrheniusBM(A=(3.10414e+13,'m^3/(mol*s)'), n=-2.25222, w0=(249977,'J/mol'), E0=(68103.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.196219976748108, var=5.740478112062978, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R
    Total Standard Deviation in ln(k): 5.296218904760553"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R
Total Standard Deviation in ln(k): 5.296218904760553""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R
Total Standard Deviation in ln(k): 5.296218904760553
""",
)

entry(
    index = 29,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0",
    kinetics = ArrheniusBM(A=(35276.1,'m^3/(mol*s)'), n=0.921099, w0=(224796,'J/mol'), E0=(346.711,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.19144893363828902, var=3.9803541878109097, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0
    Total Standard Deviation in ln(k): 4.480639344515025"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0
Total Standard Deviation in ln(k): 4.480639344515025""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0
Total Standard Deviation in ln(k): 4.480639344515025
""",
)

entry(
    index = 30,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0",
    kinetics = ArrheniusBM(A=(307.077,'m^3/(mol*s)'), n=1.52374, w0=(233668,'J/mol'), E0=(-11963.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.2617814855995082, var=0.06101486711366018, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0
    Total Standard Deviation in ln(k): 3.6654986134776366"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0
Total Standard Deviation in ln(k): 3.6654986134776366""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0
Total Standard Deviation in ln(k): 3.6654986134776366
""",
)

entry(
    index = 31,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_Sp-4R!H=3C",
    kinetics = ArrheniusBM(A=(0.0195966,'m^3/(mol*s)'), n=2.54608, w0=(323500,'J/mol'), E0=(43872.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.24691058483428616, var=1.1379847334504785, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_Sp-4R!H=3C',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_Sp-4R!H=3C
    Total Standard Deviation in ln(k): 2.7589569078610543"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_Sp-4R!H=3C
Total Standard Deviation in ln(k): 2.7589569078610543""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_Sp-4R!H=3C
Total Standard Deviation in ln(k): 2.7589569078610543
""",
)

entry(
    index = 32,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C",
    kinetics = ArrheniusBM(A=(1.90529e-10,'m^3/(mol*s)'), n=4.86128, w0=(323500,'J/mol'), E0=(28747.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1241928360149794, var=1.0669263403957938, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C',), comment="""BM rule fitted to 20 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C
    Total Standard Deviation in ln(k): 2.382775794362689"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C
Total Standard Deviation in ln(k): 2.382775794362689""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C
Total Standard Deviation in ln(k): 2.382775794362689
""",
)

entry(
    index = 33,
    label = "Root_1R->H_3R->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(8.45714e-05,'m^3/(mol*s)'), n=3.29977, w0=(323500,'J/mol'), E0=(34787.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0014948508078482965, var=10.208671995990533, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_3R->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_3R->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C
    Total Standard Deviation in ln(k): 6.409087457700756"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_3R->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C
Total Standard Deviation in ln(k): 6.409087457700756""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_3R->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C
Total Standard Deviation in ln(k): 6.409087457700756
""",
)

entry(
    index = 34,
    label = "Root_1R->H_3R->C_N-3C-u1_Ext-3C-R_N-Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(0.416835,'m^3/(mol*s)'), n=1.92612, w0=(323500,'J/mol'), E0=(22788.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R->C_N-3C-u1_Ext-3C-R_N-Sp-4R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_N-3C-u1_Ext-3C-R_N-Sp-4R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_N-3C-u1_Ext-3C-R_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_N-3C-u1_Ext-3C-R_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 35,
    label = "Root_1R->H_N-3R->C_Ext-3BrClHO-R_Ext-4R!H-R_Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(0.00672713,'m^3/(mol*s)'), n=2.9623, w0=(298550,'J/mol'), E0=(29855,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->C_Ext-3BrClHO-R_Ext-4R!H-R_Sp-5R!H-4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_Ext-3BrClHO-R_Ext-4R!H-R_Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_Ext-3BrClHO-R_Ext-4R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_Ext-3BrClHO-R_Ext-4R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 36,
    label = "Root_1R->H_N-3R->C_Ext-3BrClHO-R_Ext-4R!H-R_N-Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(0.00527246,'m^3/(mol*s)'), n=2.77027, w0=(298550,'J/mol'), E0=(29855,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->C_Ext-3BrClHO-R_Ext-4R!H-R_N-Sp-5R!H-4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_Ext-3BrClHO-R_Ext-4R!H-R_N-Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_Ext-3BrClHO-R_Ext-4R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_Ext-3BrClHO-R_Ext-4R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "Root_1R->H_N-3R->C_3BrClHO-u1_N-3BrClHO->Br_3ClO->O",
    kinetics = ArrheniusBM(A=(342.08,'m^3/(mol*s)'), n=1.58841, w0=(298550,'J/mol'), E0=(29855,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->C_3BrClHO-u1_N-3BrClHO->Br_3ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_3BrClHO-u1_N-3BrClHO->Br_3ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_3BrClHO-u1_N-3BrClHO->Br_3ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_3BrClHO-u1_N-3BrClHO->Br_3ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 38,
    label = "Root_1R->H_N-3R->C_3BrClHO-u1_N-3BrClHO->Br_N-3ClO->O",
    kinetics = ArrheniusBM(A=(833562,'m^3/(mol*s)'), n=0.302768, w0=(290420,'J/mol'), E0=(29042,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->C_3BrClHO-u1_N-3BrClHO->Br_N-3ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_3BrClHO-u1_N-3BrClHO->Br_N-3ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_3BrClHO-u1_N-3BrClHO->Br_N-3ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_3BrClHO-u1_N-3BrClHO->Br_N-3ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R",
    kinetics = ArrheniusBM(A=(5.98185e-05,'m^3/(mol*s)'), n=3.7171, w0=(323500,'J/mol'), E0=(27412.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.09503423841138321, var=0.4794748553909954, Tref=1000.0, N=23, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R',), comment="""BM rule fitted to 23 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R
    Total Standard Deviation in ln(k): 1.6269407139760421"""),
    rank = 11,
    shortDesc = """BM rule fitted to 23 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 1.6269407139760421""",
    longDesc = 
"""
BM rule fitted to 23 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 1.6269407139760421
""",
)

entry(
    index = 40,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R",
    kinetics = ArrheniusBM(A=(362469,'m^3/(mol*s)'), n=0.554197, w0=(323500,'J/mol'), E0=(40473.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.04493300396746833, var=1.0760876977534932, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R
    Total Standard Deviation in ln(k): 2.192501849681162"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 2.192501849681162""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 2.192501849681162
""",
)

entry(
    index = 41,
    label = "Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0",
    kinetics = ArrheniusBM(A=(737.867,'m^3/(mol*s)'), n=1.72171, w0=(294040,'J/mol'), E0=(29404,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.008649563693288011, var=0.13155772483290154, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0
    Total Standard Deviation in ln(k): 0.7488677679254814"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0
Total Standard Deviation in ln(k): 0.7488677679254814""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0
Total Standard Deviation in ln(k): 0.7488677679254814
""",
)

entry(
    index = 42,
    label = "Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0",
    kinetics = ArrheniusBM(A=(23904.8,'m^3/(mol*s)'), n=1.10058, w0=(298550,'J/mol'), E0=(29855,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 43,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C",
    kinetics = ArrheniusBM(A=(55.1372,'m^3/(mol*s)'), n=1.39812, w0=(285000,'J/mol'), E0=(50792.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.08358098256272123, var=4.966659359094866, Tref=1000.0, N=74, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C',), comment="""BM rule fitted to 74 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C
    Total Standard Deviation in ln(k): 4.677755691508327"""),
    rank = 11,
    shortDesc = """BM rule fitted to 74 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C
Total Standard Deviation in ln(k): 4.677755691508327""",
    longDesc = 
"""
BM rule fitted to 74 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C
Total Standard Deviation in ln(k): 4.677755691508327
""",
)

entry(
    index = 44,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C",
    kinetics = ArrheniusBM(A=(4.01638e+21,'m^3/(mol*s)'), n=-4.05309, w0=(246218,'J/mol'), E0=(80834.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.26572566520420327, var=12.18927708870539, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C
    Total Standard Deviation in ln(k): 7.666813112794716"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C
Total Standard Deviation in ln(k): 7.666813112794716""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C
Total Standard Deviation in ln(k): 7.666813112794716
""",
)

entry(
    index = 45,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_3BrCClO->C",
    kinetics = ArrheniusBM(A=(0.555662,'m^3/(mol*s)'), n=2.48693, w0=(285000,'J/mol'), E0=(41340,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0012288671781378285, var=13.37403770670558, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_3BrCClO->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_3BrCClO->C
    Total Standard Deviation in ln(k): 7.334510326021607"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_3BrCClO->C
Total Standard Deviation in ln(k): 7.334510326021607""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_3BrCClO->C
Total Standard Deviation in ln(k): 7.334510326021607
""",
)

entry(
    index = 46,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C",
    kinetics = ArrheniusBM(A=(1.4758e+12,'m^3/(mol*s)'), n=-1.75948, w0=(260050,'J/mol'), E0=(47335.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.6700956026344866, var=42.03770148326072, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C
    Total Standard Deviation in ln(k): 19.70678105700364"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C
Total Standard Deviation in ln(k): 19.70678105700364""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C
Total Standard Deviation in ln(k): 19.70678105700364
""",
)

entry(
    index = 47,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(4.64102e+07,'m^3/(mol*s)'), n=-0.533698, w0=(249823,'J/mol'), E0=(65231.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.46359052552323654, var=6.657351645622095, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl
    Total Standard Deviation in ln(k): 6.337386530018609"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl
Total Standard Deviation in ln(k): 6.337386530018609""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl
Total Standard Deviation in ln(k): 6.337386530018609
""",
)

entry(
    index = 48,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(4.97603e+11,'m^3/(mol*s)'), n=-1.72437, w0=(250028,'J/mol'), E0=(48891.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.15120509859928608, var=11.59711189530224, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 7.206943909624679"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 7.206943909624679""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 7.206943909624679
""",
)

entry(
    index = 49,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br",
    kinetics = ArrheniusBM(A=(3.55155e-06,'m^3/(mol*s)'), n=4.1153, w0=(220904,'J/mol'), E0=(-6220.33,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.0927997363071065, var=12.654593299652086, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br
    Total Standard Deviation in ln(k): 9.877231247260353"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br
Total Standard Deviation in ln(k): 9.877231247260353""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br
Total Standard Deviation in ln(k): 9.877231247260353
""",
)

entry(
    index = 50,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br",
    kinetics = ArrheniusBM(A=(129991,'m^3/(mol*s)'), n=0.717255, w0=(227576,'J/mol'), E0=(254.497,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.415469328364077, var=4.347313118139047, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br
    Total Standard Deviation in ln(k): 5.22380778394193"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br
Total Standard Deviation in ln(k): 5.22380778394193""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br
Total Standard Deviation in ln(k): 5.22380778394193
""",
)

entry(
    index = 51,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_3BrCClO->Br",
    kinetics = ArrheniusBM(A=(1.31182e+06,'m^3/(mol*s)'), n=0.464452, w0=(212550,'J/mol'), E0=(27071,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_3BrCClO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_3BrCClO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_3BrCClO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_3BrCClO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 52,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br",
    kinetics = ArrheniusBM(A=(700891,'m^3/(mol*s)'), n=0.517973, w0=(240707,'J/mol'), E0=(9897.51,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03516771471883505, var=0.04880254434115809, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br
    Total Standard Deviation in ln(k): 0.5312330905404677"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br
Total Standard Deviation in ln(k): 0.5312330905404677""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br
Total Standard Deviation in ln(k): 0.5312330905404677
""",
)

entry(
    index = 53,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.357862,'m^3/(mol*s)'), n=2.13837, w0=(323500,'J/mol'), E0=(47755.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07083056985365817, var=3.3941268767153168, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R
    Total Standard Deviation in ln(k): 3.8713210209240025"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R
Total Standard Deviation in ln(k): 3.8713210209240025""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R
Total Standard Deviation in ln(k): 3.8713210209240025
""",
)

entry(
    index = 54,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br",
    kinetics = ArrheniusBM(A=(0.0576983,'m^3/(mol*s)'), n=2.2512, w0=(323500,'J/mol'), E0=(54197.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0009542453689490317, var=0.32383258835637285, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br
    Total Standard Deviation in ln(k): 1.1432179657011137"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br
Total Standard Deviation in ln(k): 1.1432179657011137""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br
Total Standard Deviation in ln(k): 1.1432179657011137
""",
)

entry(
    index = 55,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br",
    kinetics = ArrheniusBM(A=(7.05179e-07,'m^3/(mol*s)'), n=3.80178, w0=(323500,'J/mol'), E0=(39370,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.08968102916198635, var=1.2212126541242254, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br',), comment="""BM rule fitted to 17 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br
    Total Standard Deviation in ln(k): 2.440731697779462"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br
Total Standard Deviation in ln(k): 2.440731697779462""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br
Total Standard Deviation in ln(k): 2.440731697779462
""",
)

entry(
    index = 56,
    label = "Root_1R->H_3R->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_4R!H->C",
    kinetics = ArrheniusBM(A=(0.279393,'m^3/(mol*s)'), n=2.26429, w0=(323500,'J/mol'), E0=(32680.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 57,
    label = "Root_1R->H_3R->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.00111222,'m^3/(mol*s)'), n=2.71464, w0=(323500,'J/mol'), E0=(31265.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 58,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C",
    kinetics = ArrheniusBM(A=(0.000284597,'m^3/(mol*s)'), n=3.57186, w0=(323500,'J/mol'), E0=(31115.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.052706171398782066, var=0.6768029790199216, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C
    Total Standard Deviation in ln(k): 1.781683746731074"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C
Total Standard Deviation in ln(k): 1.781683746731074""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C
Total Standard Deviation in ln(k): 1.781683746731074
""",
)

entry(
    index = 59,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C",
    kinetics = ArrheniusBM(A=(0.020476,'m^3/(mol*s)'), n=2.94461, w0=(323500,'J/mol'), E0=(35366.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05276087665434829, var=0.5667047141516738, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C',), comment="""BM rule fitted to 20 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C
    Total Standard Deviation in ln(k): 1.6417254208494476"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C
Total Standard Deviation in ln(k): 1.6417254208494476""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C
Total Standard Deviation in ln(k): 1.6417254208494476
""",
)

entry(
    index = 60,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(8.8432,'m^3/(mol*s)'), n=1.95158, w0=(323500,'J/mol'), E0=(35525.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0017892275663359885, var=0.720192675491597, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C
    Total Standard Deviation in ln(k): 1.7057972605154506"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C
Total Standard Deviation in ln(k): 1.7057972605154506""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C
Total Standard Deviation in ln(k): 1.7057972605154506
""",
)

entry(
    index = 61,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_N-Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(2625.75,'m^3/(mol*s)'), n=1.23946, w0=(323500,'J/mol'), E0=(33096,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_N-Sp-4R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_N-Sp-4R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 62,
    label = "Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_1BrO->Br",
    kinetics = ArrheniusBM(A=(114000,'m^3/(mol*s)'), n=1, w0=(276000,'J/mol'), E0=(27600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_1BrO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_1BrO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_1BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_1BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 63,
    label = "Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br",
    kinetics = ArrheniusBM(A=(735.084,'m^3/(mol*s)'), n=1.72229, w0=(298550,'J/mol'), E0=(29855,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.008565162027852038, var=0.13189636077551997, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br
    Total Standard Deviation in ln(k): 0.7495909425588086"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br
Total Standard Deviation in ln(k): 0.7495909425588086""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br
Total Standard Deviation in ln(k): 0.7495909425588086
""",
)

entry(
    index = 64,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(28.2562,'m^3/(mol*s)'), n=1.42268, w0=(285000,'J/mol'), E0=(50220.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.08067881360144924, var=4.8570338413153875, Tref=1000.0, N=56, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R',), comment="""BM rule fitted to 56 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R
    Total Standard Deviation in ln(k): 4.620881926892344"""),
    rank = 11,
    shortDesc = """BM rule fitted to 56 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R
Total Standard Deviation in ln(k): 4.620881926892344""",
    longDesc = 
"""
BM rule fitted to 56 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R
Total Standard Deviation in ln(k): 4.620881926892344
""",
)

entry(
    index = 65,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.582081,'m^3/(mol*s)'), n=2.17547, w0=(285000,'J/mol'), E0=(43195.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.04465045860144299, var=3.2721405473992915, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 3.7385641871062325"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 3.7385641871062325""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 3.7385641871062325
""",
)

entry(
    index = 66,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(0.00556838,'m^3/(mol*s)'), n=2.8146, w0=(285000,'J/mol'), E0=(50539.3,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_4R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_4R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 67,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(1889.57,'m^3/(mol*s)'), n=1.12836, w0=(285000,'J/mol'), E0=(56929.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.10253575557584768, var=5.504581283361724, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 4.961105710324198"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 4.961105710324198""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 4.961105710324198
""",
)

entry(
    index = 68,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0",
    kinetics = ArrheniusBM(A=(2.45326e+21,'m^3/(mol*s)'), n=-3.98825, w0=(247011,'J/mol'), E0=(80495.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.26069237129727857, var=12.236336008745411, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0
    Total Standard Deviation in ln(k): 7.667664396703013"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0
Total Standard Deviation in ln(k): 7.667664396703013""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0
Total Standard Deviation in ln(k): 7.667664396703013
""",
)

entry(
    index = 69,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_N-1C-u0",
    kinetics = ArrheniusBM(A=(5000,'m^3/(mol*s)'), n=0, w0=(237500,'J/mol'), E0=(23750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_N-1C-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_N-1C-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_N-1C-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_N-1C-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 70,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_3BrCClO->C_Ext-3C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(0.0016727,'m^3/(mol*s)'), n=3.33083, w0=(285000,'J/mol'), E0=(30341.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_3BrCClO->C_Ext-3C-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_3BrCClO->C_Ext-3C-R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_3BrCClO->C_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_3BrCClO->C_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 71,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(5.11215e-06,'m^3/(mol*s)'), n=3.81141, w0=(285000,'J/mol'), E0=(31398.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 72,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.16584e+12,'m^3/(mol*s)'), n=-1.7298, w0=(260050,'J/mol'), E0=(47165,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.3668391974360073, var=11.785445881836885, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C_Ext-1C-R
    Total Standard Deviation in ln(k): 7.803949457259909"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C_Ext-1C-R
Total Standard Deviation in ln(k): 7.803949457259909""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C_Ext-1C-R
Total Standard Deviation in ln(k): 7.803949457259909
""",
)

entry(
    index = 73,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl_1BrClO->Br",
    kinetics = ArrheniusBM(A=(1882.63,'m^3/(mol*s)'), n=0.917064, w0=(237500,'J/mol'), E0=(54196.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl_1BrClO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl_1BrClO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl_1BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl_1BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 74,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl_N-1BrClO->Br",
    kinetics = ArrheniusBM(A=(9.13509e-14,'m^3/(mol*s)'), n=5.4332, w0=(255985,'J/mol'), E0=(10488.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.11073282746786067, var=0.4453131224195067, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl_N-1BrClO->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl_N-1BrClO->Br
    Total Standard Deviation in ln(k): 1.6160187005149582"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl_N-1BrClO->Br
Total Standard Deviation in ln(k): 1.6160187005149582""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl_N-1BrClO->Br
Total Standard Deviation in ln(k): 1.6160187005149582
""",
)

entry(
    index = 75,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0",
    kinetics = ArrheniusBM(A=(1.53002e+09,'m^3/(mol*s)'), n=-0.891737, w0=(247164,'J/mol'), E0=(37123.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.0125723570816976, var=2.9936415972819717, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0
    Total Standard Deviation in ln(k): 6.012772992076272"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0
Total Standard Deviation in ln(k): 6.012772992076272""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0
Total Standard Deviation in ln(k): 6.012772992076272
""",
)

entry(
    index = 76,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_N-1BrClO-u0",
    kinetics = ArrheniusBM(A=(0.0824085,'m^3/(mol*s)'), n=1.92177, w0=(260050,'J/mol'), E0=(6959.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.2049749100137457, var=5.770142754214172, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_N-1BrClO-u0',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_N-1BrClO-u0
    Total Standard Deviation in ln(k): 7.843173626476478"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_N-1BrClO-u0
Total Standard Deviation in ln(k): 7.843173626476478""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_N-1BrClO-u0
Total Standard Deviation in ln(k): 7.843173626476478
""",
)

entry(
    index = 77,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_3BrCClO->O",
    kinetics = ArrheniusBM(A=(4.47316,'m^3/(mol*s)'), n=2.05644, w0=(212550,'J/mol'), E0=(-3666.49,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5047708693731049, var=0.1921437508241951, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_3BrCClO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_3BrCClO->O
    Total Standard Deviation in ln(k): 2.1470281950306687"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_3BrCClO->O
Total Standard Deviation in ln(k): 2.1470281950306687""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_3BrCClO->O
Total Standard Deviation in ln(k): 2.1470281950306687
""",
)

entry(
    index = 78,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O",
    kinetics = ArrheniusBM(A=(3.48325e+08,'m^3/(mol*s)'), n=0.0231767, w0=(226473,'J/mol'), E0=(7565.15,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.6403525102388543, var=15.540248852695646, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O
    Total Standard Deviation in ln(k): 14.536942204544106"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O
Total Standard Deviation in ln(k): 14.536942204544106""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O
Total Standard Deviation in ln(k): 14.536942204544106
""",
)

entry(
    index = 79,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1",
    kinetics = ArrheniusBM(A=(646045,'m^3/(mol*s)'), n=0.47614, w0=(226192,'J/mol'), E0=(-3.05516,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.6631468621526736, var=6.864472903571605, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1
    Total Standard Deviation in ln(k): 6.918631940480145"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1
Total Standard Deviation in ln(k): 6.918631940480145""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1
Total Standard Deviation in ln(k): 6.918631940480145
""",
)

entry(
    index = 80,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_N-3BrCClO-u1",
    kinetics = ArrheniusBM(A=(6.9409e+09,'m^3/(mol*s)'), n=-0.593728, w0=(231035,'J/mol'), E0=(19653.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.010692155221322053, var=2.874192945020624, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_N-3BrCClO-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_N-3BrCClO-u1
    Total Standard Deviation in ln(k): 3.4255812820836598"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_N-3BrCClO-u1
Total Standard Deviation in ln(k): 3.4255812820836598""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_N-3BrCClO-u1
Total Standard Deviation in ln(k): 3.4255812820836598
""",
)

entry(
    index = 81,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br_3CClO->Cl",
    kinetics = ArrheniusBM(A=(1.13026e+07,'m^3/(mol*s)'), n=0.234452, w0=(226970,'J/mol'), E0=(16550.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br_3CClO->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br_3CClO->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br_3CClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br_3CClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 82,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br_N-3CClO->Cl",
    kinetics = ArrheniusBM(A=(678423,'m^3/(mol*s)'), n=0.465326, w0=(247575,'J/mol'), E0=(4209.08,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.8791561812784865, var=21.885036233336137, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br_N-3CClO->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br_N-3CClO->Cl
    Total Standard Deviation in ln(k): 19.125064005269433"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br_N-3CClO->Cl
Total Standard Deviation in ln(k): 19.125064005269433""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br_N-3CClO->Cl
Total Standard Deviation in ln(k): 19.125064005269433
""",
)

entry(
    index = 83,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(6.71691e-14,'m^3/(mol*s)'), n=6.161, w0=(323500,'J/mol'), E0=(24118.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 84,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.00230167,'m^3/(mol*s)'), n=2.69491, w0=(323500,'J/mol'), E0=(50840.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0065737383112800625, var=0.3522095422000362, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R
    Total Standard Deviation in ln(k): 1.206271957081028"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R
Total Standard Deviation in ln(k): 1.206271957081028""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R
Total Standard Deviation in ln(k): 1.206271957081028
""",
)

entry(
    index = 85,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClF->Cl",
    kinetics = ArrheniusBM(A=(4.58628,'m^3/(mol*s)'), n=1.79617, w0=(323500,'J/mol'), E0=(58728.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.017387621510314116, var=6.6994888411298685, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClF->Cl',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClF->Cl
    Total Standard Deviation in ln(k): 5.232617628180455"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClF->Cl
Total Standard Deviation in ln(k): 5.232617628180455""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClF->Cl
Total Standard Deviation in ln(k): 5.232617628180455
""",
)

entry(
    index = 86,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl",
    kinetics = ArrheniusBM(A=(5.50817e-11,'m^3/(mol*s)'), n=5.03329, w0=(323500,'J/mol'), E0=(26817.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.08717089154463062, var=0.8349360734507447, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl',), comment="""BM rule fitted to 14 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl
    Total Standard Deviation in ln(k): 2.050845738596351"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl
Total Standard Deviation in ln(k): 2.050845738596351""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl
Total Standard Deviation in ln(k): 2.050845738596351
""",
)

entry(
    index = 87,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.30985e-05,'m^3/(mol*s)'), n=3.84372, w0=(323500,'J/mol'), E0=(30370.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.02277208720285725, var=1.2420742785481371, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_Ext-1C-R
    Total Standard Deviation in ln(k): 2.291461190746548"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_Ext-1C-R
Total Standard Deviation in ln(k): 2.291461190746548""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_Ext-1C-R
Total Standard Deviation in ln(k): 2.291461190746548
""",
)

entry(
    index = 88,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.56677e-05,'m^3/(mol*s)'), n=3.90861, w0=(323500,'J/mol'), E0=(6540.14,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.12394839338767152, var=0.29416462714798913, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R',), comment="""BM rule fitted to 14 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R
    Total Standard Deviation in ln(k): 1.3987351980799212"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R
Total Standard Deviation in ln(k): 1.3987351980799212""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R
Total Standard Deviation in ln(k): 1.3987351980799212
""",
)

entry(
    index = 89,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2.53152e-07,'m^3/(mol*s)'), n=4.31499, w0=(323500,'J/mol'), E0=(11612.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00012692656988021894, var=11.986960897707982, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 6.9411509288476525"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R
Total Standard Deviation in ln(k): 6.9411509288476525""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R
Total Standard Deviation in ln(k): 6.9411509288476525
""",
)

entry(
    index = 90,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F",
    kinetics = ArrheniusBM(A=(349.197,'m^3/(mol*s)'), n=1.7256, w0=(323500,'J/mol'), E0=(53622,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 91,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F",
    kinetics = ArrheniusBM(A=(5.71694e-07,'m^3/(mol*s)'), n=4.3663, w0=(323500,'J/mol'), E0=(16374.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.30374349461677336, var=0.4227319381518444, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F
    Total Standard Deviation in ln(k): 2.0666100335518305"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F
Total Standard Deviation in ln(k): 2.0666100335518305""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F
Total Standard Deviation in ln(k): 2.0666100335518305
""",
)

entry(
    index = 92,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C",
    kinetics = ArrheniusBM(A=(197.056,'m^3/(mol*s)'), n=1.64084, w0=(323500,'J/mol'), E0=(41284.7,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 93,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(149.752,'m^3/(mol*s)'), n=1.64303, w0=(323500,'J/mol'), E0=(44257.2,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 94,
    label = "Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br_Ext-1O-R",
    kinetics = ArrheniusBM(A=(644.68,'m^3/(mol*s)'), n=1.72439, w0=(298550,'J/mol'), E0=(29855,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.008673604970408515, var=0.06670459070419386, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br_Ext-1O-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br_Ext-1O-R
    Total Standard Deviation in ln(k): 0.5395605545088691"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br_Ext-1O-R
Total Standard Deviation in ln(k): 0.5395605545088691""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br_Ext-1O-R
Total Standard Deviation in ln(k): 0.5395605545088691
""",
)

entry(
    index = 95,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C",
    kinetics = ArrheniusBM(A=(1.2078e-15,'m^3/(mol*s)'), n=6.49287, w0=(285000,'J/mol'), E0=(6555.94,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.19621783641570767, var=6.44831867616914, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C
    Total Standard Deviation in ln(k): 5.58374165281985"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C
Total Standard Deviation in ln(k): 5.58374165281985""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C
Total Standard Deviation in ln(k): 5.58374165281985
""",
)

entry(
    index = 96,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C",
    kinetics = ArrheniusBM(A=(1.19327,'m^3/(mol*s)'), n=1.79405, w0=(285000,'J/mol'), E0=(47075.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07104421400305445, var=4.487077826022761, Tref=1000.0, N=48, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C',), comment="""BM rule fitted to 48 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C
    Total Standard Deviation in ln(k): 4.42507797033194"""),
    rank = 11,
    shortDesc = """BM rule fitted to 48 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C
Total Standard Deviation in ln(k): 4.42507797033194""",
    longDesc = 
"""
BM rule fitted to 48 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C
Total Standard Deviation in ln(k): 4.42507797033194
""",
)

entry(
    index = 97,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(0.033938,'m^3/(mol*s)'), n=2.67089, w0=(285000,'J/mol'), E0=(39102.6,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_4R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_4R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 98,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(0.318649,'m^3/(mol*s)'), n=2.24128, w0=(285000,'J/mol'), E0=(43144.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0365041016444612, var=3.640963651745853, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 3.917015858991078"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 3.917015858991078""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 3.917015858991078
""",
)

entry(
    index = 99,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C",
    kinetics = ArrheniusBM(A=(1.88438e+06,'m^3/(mol*s)'), n=0.0901955, w0=(285000,'J/mol'), E0=(58211.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1391900715111477, var=7.386769681432762, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C
    Total Standard Deviation in ln(k): 5.798315546899704"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C
Total Standard Deviation in ln(k): 5.798315546899704""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C
Total Standard Deviation in ln(k): 5.798315546899704
""",
)

entry(
    index = 100,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-1C",
    kinetics = ArrheniusBM(A=(4.50439e-28,'m^3/(mol*s)'), n=10.4274, w0=(285000,'J/mol'), E0=(-14681.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.02495475530272098, var=8.213378835972103, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-1C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-1C
    Total Standard Deviation in ln(k): 5.808069258568899"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-1C
Total Standard Deviation in ln(k): 5.808069258568899""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-1C
Total Standard Deviation in ln(k): 5.808069258568899
""",
)

entry(
    index = 101,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.39083e+20,'m^3/(mol*s)'), n=-3.69696, w0=(246619,'J/mol'), E0=(79492.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.22730729586425127, var=16.748386063895385, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R
    Total Standard Deviation in ln(k): 8.775460479755308"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 8.775460479755308""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 8.775460479755308
""",
)

entry(
    index = 102,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_3BrClO->Br",
    kinetics = ArrheniusBM(A=(7.04501e+07,'m^3/(mol*s)'), n=0.0380005, w0=(237500,'J/mol'), E0=(23750,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_3BrClO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_3BrClO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_3BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_3BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 103,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_N-3BrClO->Br",
    kinetics = ArrheniusBM(A=(0.145829,'m^3/(mol*s)'), n=2.81794, w0=(260050,'J/mol'), E0=(19495.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_N-3BrClO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_N-3BrClO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_N-3BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_N-3BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 104,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(615.671,'m^3/(mol*s)'), n=0.853454, w0=(260050,'J/mol'), E0=(24963.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.522675652395081, var=38.84722307206231, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 23.858527341017908"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 23.858527341017908""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 23.858527341017908
""",
)

entry(
    index = 105,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl_N-1BrClO->Br_1ClO->O",
    kinetics = ArrheniusBM(A=(0.0667867,'m^3/(mol*s)'), n=1.64401, w0=(260050,'J/mol'), E0=(21929.5,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl_N-1BrClO->Br_1ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl_N-1BrClO->Br_1ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl_N-1BrClO->Br_1ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl_N-1BrClO->Br_1ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 106,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl_N-1BrClO->Br_N-1ClO->O",
    kinetics = ArrheniusBM(A=(247.456,'m^3/(mol*s)'), n=1.14962, w0=(251920,'J/mol'), E0=(69327.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl_N-1BrClO->Br_N-1ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl_N-1BrClO->Br_N-1ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl_N-1BrClO->Br_N-1ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_4R!H->Cl_N-1BrClO->Br_N-1ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 107,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R",
    kinetics = ArrheniusBM(A=(144410,'m^3/(mol*s)'), n=0.280295, w0=(245017,'J/mol'), E0=(23517.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.19250701493587524, var=0.2254084579534079, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R
    Total Standard Deviation in ln(k): 1.435478061943111"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R
Total Standard Deviation in ln(k): 1.435478061943111""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R
Total Standard Deviation in ln(k): 1.435478061943111
""",
)

entry(
    index = 108,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_1BrClO->Br",
    kinetics = ArrheniusBM(A=(6.14681e+08,'m^3/(mol*s)'), n=-0.527905, w0=(237500,'J/mol'), E0=(30474.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.35024040011199753, var=0.2620792632022212, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_1BrClO->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_1BrClO->Br
    Total Standard Deviation in ln(k): 1.9062986186992787"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_1BrClO->Br
Total Standard Deviation in ln(k): 1.9062986186992787""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_1BrClO->Br
Total Standard Deviation in ln(k): 1.9062986186992787
""",
)

entry(
    index = 109,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_N-1BrClO->Br",
    kinetics = ArrheniusBM(A=(3.56665e+14,'m^3/(mol*s)'), n=-2.54977, w0=(260050,'J/mol'), E0=(-10277.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.620107419366252, var=8.027161994609964, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_N-1BrClO->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_N-1BrClO->Br
    Total Standard Deviation in ln(k): 12.26304933608979"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_N-1BrClO->Br
Total Standard Deviation in ln(k): 12.26304933608979""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_N-1BrClO->Br
Total Standard Deviation in ln(k): 12.26304933608979
""",
)

entry(
    index = 110,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_N-1BrClO-u0_Ext-3BrCClO-R",
    kinetics = ArrheniusBM(A=(14427.7,'m^3/(mol*s)'), n=0.346526, w0=(260050,'J/mol'), E0=(13273,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_N-1BrClO-u0_Ext-3BrCClO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_N-1BrClO-u0_Ext-3BrCClO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_N-1BrClO-u0_Ext-3BrCClO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_N-1BrClO-u0_Ext-3BrCClO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 111,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_3BrCClO->O_3O-u1",
    kinetics = ArrheniusBM(A=(12.8629,'m^3/(mol*s)'), n=1.87634, w0=(212550,'J/mol'), E0=(4529.77,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_3BrCClO->O_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_3BrCClO->O_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_3BrCClO->O_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_3BrCClO->O_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 112,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_3BrCClO->O_N-3O-u1",
    kinetics = ArrheniusBM(A=(19965.9,'m^3/(mol*s)'), n=1.02274, w0=(212550,'J/mol'), E0=(25084.9,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_3BrCClO->O_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_3BrCClO->O_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_3BrCClO->O_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_3BrCClO->O_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 113,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O_3BrCCl-u1",
    kinetics = ArrheniusBM(A=(1.28903e+08,'m^3/(mol*s)'), n=0.160282, w0=(220960,'J/mol'), E0=(768.032,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-5.71921841333791, var=51.110668855379124, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O_3BrCCl-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O_3BrCCl-u1
    Total Standard Deviation in ln(k): 28.702092595172754"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O_3BrCCl-u1
Total Standard Deviation in ln(k): 28.702092595172754""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O_3BrCCl-u1
Total Standard Deviation in ln(k): 28.702092595172754
""",
)

entry(
    index = 114,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O_N-3BrCCl-u1",
    kinetics = ArrheniusBM(A=(194.627,'m^3/(mol*s)'), n=0.434377, w0=(237500,'J/mol'), E0=(23750,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O_N-3BrCCl-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O_N-3BrCCl-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O_N-3BrCCl-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O_N-3BrCCl-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 115,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_3BrCClO->O",
    kinetics = ArrheniusBM(A=(904000,'m^3/(mol*s)'), n=0, w0=(226970,'J/mol'), E0=(-1668.73,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_3BrCClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_3BrCClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_3BrCClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_3BrCClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 116,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O",
    kinetics = ArrheniusBM(A=(50759,'m^3/(mol*s)'), n=0.889702, w0=(225998,'J/mol'), E0=(-6163.55,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.0230540124727385, var=8.398990562586768, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O
    Total Standard Deviation in ln(k): 8.380412601015154"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O
Total Standard Deviation in ln(k): 8.380412601015154""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O
Total Standard Deviation in ln(k): 8.380412601015154
""",
)

entry(
    index = 117,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_N-3BrCClO-u1_1ClO->O",
    kinetics = ArrheniusBM(A=(7.2e+07,'m^3/(mol*s)'), n=0, w0=(235100,'J/mol'), E0=(10605.2,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_N-3BrCClO-u1_1ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_N-3BrCClO-u1_1ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_N-3BrCClO-u1_1ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_N-3BrCClO-u1_1ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 118,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_N-3BrCClO-u1_N-1ClO->O",
    kinetics = ArrheniusBM(A=(22611.5,'m^3/(mol*s)'), n=1.0253, w0=(226970,'J/mol'), E0=(12604.8,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_N-3BrCClO-u1_N-1ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_N-3BrCClO-u1_N-1ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_N-3BrCClO-u1_N-1ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_N-3BrCClO-u1_N-1ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 119,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br_N-3CClO->Cl_3CO->C",
    kinetics = ArrheniusBM(A=(5.64233e+07,'m^3/(mol*s)'), n=-0.596289, w0=(260050,'J/mol'), E0=(15576.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br_N-3CClO->Cl_3CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br_N-3CClO->Cl_3CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br_N-3CClO->Cl_3CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br_N-3CClO->Cl_3CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 120,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br_N-3CClO->Cl_N-3CO->C",
    kinetics = ArrheniusBM(A=(1.61447e+09,'m^3/(mol*s)'), n=-0.558876, w0=(235100,'J/mol'), E0=(12790.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br_N-3CClO->Cl_N-3CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br_N-3CClO->Cl_N-3CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br_N-3CClO->Cl_N-3CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_N-1BrClO-u0_N-3BrCClO->Br_N-3CClO->Cl_N-3CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 121,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.00198848,'m^3/(mol*s)'), n=2.53388, w0=(323500,'J/mol'), E0=(37460.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 122,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClF->Cl_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.0361728,'m^3/(mol*s)'), n=2.54721, w0=(323500,'J/mol'), E0=(52406.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.005254922146764159, var=0.9204273018118259, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClF->Cl_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClF->Cl_Ext-3C-R
    Total Standard Deviation in ln(k): 1.9365241538059839"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClF->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 1.9365241538059839""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClF->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 1.9365241538059839
""",
)

entry(
    index = 123,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R",
    kinetics = ArrheniusBM(A=(3.65465e-07,'m^3/(mol*s)'), n=3.82051, w0=(323500,'J/mol'), E0=(37649.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.035742871319919815, var=0.8994584981929977, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R',), comment="""BM rule fitted to 8 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R
    Total Standard Deviation in ln(k): 1.991092663803135"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R
Total Standard Deviation in ln(k): 1.991092663803135""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R
Total Standard Deviation in ln(k): 1.991092663803135
""",
)

entry(
    index = 124,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F",
    kinetics = ArrheniusBM(A=(0.0850035,'m^3/(mol*s)'), n=2.35365, w0=(323500,'J/mol'), E0=(52746.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0005624965051950025, var=0.29388832008971977, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F',), comment="""BM rule fitted to 5 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F
    Total Standard Deviation in ln(k): 1.0882096113382063"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F
Total Standard Deviation in ln(k): 1.0882096113382063""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F
Total Standard Deviation in ln(k): 1.0882096113382063
""",
)

entry(
    index = 125,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_N-4CF->F",
    kinetics = ArrheniusBM(A=(0.0899429,'m^3/(mol*s)'), n=2.31578, w0=(323500,'J/mol'), E0=(40860.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_N-4CF->F',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_N-4CF->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_N-4CF->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_N-4CF->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 126,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_Ext-1C-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(890.982,'m^3/(mol*s)'), n=1.65484, w0=(323500,'J/mol'), E0=(52880.9,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_Ext-1C-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_Ext-1C-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_Ext-1C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_Sp-4R!H=1C_Ext-1C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 127,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F",
    kinetics = ArrheniusBM(A=(0.00766895,'m^3/(mol*s)'), n=3.08147, w0=(323500,'J/mol'), E0=(35283.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06727665948070745, var=0.2523966573023917, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F
    Total Standard Deviation in ln(k): 1.176197574262323"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F
Total Standard Deviation in ln(k): 1.176197574262323""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F
Total Standard Deviation in ln(k): 1.176197574262323
""",
)

entry(
    index = 128,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-4R!H->F",
    kinetics = ArrheniusBM(A=(56.2048,'m^3/(mol*s)'), n=1.91323, w0=(323500,'J/mol'), E0=(30949.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0019614854279453534, var=0.5666788516450608, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-4R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-4R!H->F
    Total Standard Deviation in ln(k): 1.5140543225685406"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-4R!H->F
Total Standard Deviation in ln(k): 1.5140543225685406""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-4R!H->F
Total Standard Deviation in ln(k): 1.5140543225685406
""",
)

entry(
    index = 129,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(650.121,'m^3/(mol*s)'), n=1.74726, w0=(323500,'J/mol'), E0=(50950.1,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 130,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_4BrCCl->Cl",
    kinetics = ArrheniusBM(A=(371.066,'m^3/(mol*s)'), n=1.71693, w0=(323500,'J/mol'), E0=(55780.9,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_4BrCCl->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_4BrCCl->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_4BrCCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_4BrCCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 131,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_N-4BrCCl->Cl",
    kinetics = ArrheniusBM(A=(9.29276e-07,'m^3/(mol*s)'), n=4.32239, w0=(323500,'J/mol'), E0=(21306.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.01566014487253595, var=0.9177851917572412, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_N-4BrCCl->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_N-4BrCCl->Cl
    Total Standard Deviation in ln(k): 1.9599054748893912"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_N-4BrCCl->Cl
Total Standard Deviation in ln(k): 1.9599054748893912""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_N-4BrCCl->Cl
Total Standard Deviation in ln(k): 1.9599054748893912
""",
)

entry(
    index = 132,
    label = "Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br_Ext-1O-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(541.102,'m^3/(mol*s)'), n=1.73592, w0=(298550,'J/mol'), E0=(29855,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.13795724490983916, var=0.12127301348872485, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br_Ext-1O-R_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br_Ext-1O-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 1.0447607014804807"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br_Ext-1O-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 1.0447607014804807""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br_Ext-1O-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 1.0447607014804807
""",
)

entry(
    index = 133,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2.43789e-20,'m^3/(mol*s)'), n=7.94839, w0=(285000,'J/mol'), E0=(-1705.08,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.020370586976262036, var=12.583874895779013, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 7.162731030077497"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-4R!H-R
Total Standard Deviation in ln(k): 7.162731030077497""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-4R!H-R
Total Standard Deviation in ln(k): 7.162731030077497
""",
)

entry(
    index = 134,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(6.80487e-14,'m^3/(mol*s)'), n=5.82527, w0=(285000,'J/mol'), E0=(2506.04,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.7095254310172734, var=33.21364856902875, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R
    Total Standard Deviation in ln(k): 15.848835619576569"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R
Total Standard Deviation in ln(k): 15.848835619576569""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R
Total Standard Deviation in ln(k): 15.848835619576569
""",
)

entry(
    index = 135,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.00304471,'m^3/(mol*s)'), n=2.97709, w0=(285000,'J/mol'), E0=(38041.3,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 136,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br",
    kinetics = ArrheniusBM(A=(0.0145517,'m^3/(mol*s)'), n=2.17835, w0=(285000,'J/mol'), E0=(43186.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.024892792328615028, var=4.9646607510947645, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br
    Total Standard Deviation in ln(k): 4.529398913783842"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br
Total Standard Deviation in ln(k): 4.529398913783842""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br
Total Standard Deviation in ln(k): 4.529398913783842
""",
)

entry(
    index = 137,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br",
    kinetics = ArrheniusBM(A=(2.21185,'m^3/(mol*s)'), n=1.7511, w0=(285000,'J/mol'), E0=(47617.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07773011893767734, var=4.334979188452902, Tref=1000.0, N=40, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br',), comment="""BM rule fitted to 40 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br
    Total Standard Deviation in ln(k): 4.369283094790619"""),
    rank = 11,
    shortDesc = """BM rule fitted to 40 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br
Total Standard Deviation in ln(k): 4.369283094790619""",
    longDesc = 
"""
BM rule fitted to 40 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br
Total Standard Deviation in ln(k): 4.369283094790619
""",
)

entry(
    index = 138,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.37382e-07,'m^3/(mol*s)'), n=4.06437, w0=(285000,'J/mol'), E0=(32610.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.006726150674765597, var=1.344750883402891, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 2.341658719958271"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 2.341658719958271""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 2.341658719958271
""",
)

entry(
    index = 139,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_4BrCFO->Br",
    kinetics = ArrheniusBM(A=(0.484658,'m^3/(mol*s)'), n=1.73772, w0=(285000,'J/mol'), E0=(43563.3,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_4BrCFO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_4BrCFO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_4BrCFO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_4BrCFO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 140,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br",
    kinetics = ArrheniusBM(A=(163.947,'m^3/(mol*s)'), n=1.53192, w0=(285000,'J/mol'), E0=(48271.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.08497921417846573, var=2.6959492924957718, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br
    Total Standard Deviation in ln(k): 3.5051595386598393"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br
Total Standard Deviation in ln(k): 3.5051595386598393""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br
Total Standard Deviation in ln(k): 3.5051595386598393
""",
)

entry(
    index = 141,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_1C-u0",
    kinetics = ArrheniusBM(A=(0.000775546,'m^3/(mol*s)'), n=2.71448, w0=(285000,'J/mol'), E0=(42844.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.011226134731481817, var=2.0918372342884335, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_1C-u0',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_1C-u0
    Total Standard Deviation in ln(k): 2.927691820084005"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_1C-u0
Total Standard Deviation in ln(k): 2.927691820084005""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_1C-u0
Total Standard Deviation in ln(k): 2.927691820084005
""",
)

entry(
    index = 142,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_N-1C-u0",
    kinetics = ArrheniusBM(A=(0.00247873,'m^3/(mol*s)'), n=2.9317, w0=(285000,'J/mol'), E0=(32823.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0038694193895180626, var=1.6021249676700775, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_N-1C-u0',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_N-1C-u0
    Total Standard Deviation in ln(k): 2.547217092215782"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_N-1C-u0
Total Standard Deviation in ln(k): 2.547217092215782""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_N-1C-u0
Total Standard Deviation in ln(k): 2.547217092215782
""",
)

entry(
    index = 143,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-1C_Ext-4BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(3.44925e-20,'m^3/(mol*s)'), n=8.05735, w0=(285000,'J/mol'), E0=(4725.57,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.022972667232871787, var=16.20754213057048, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-1C_Ext-4BrCFINOPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-1C_Ext-4BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 8.128501382576301"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-1C_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 8.128501382576301""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-1C_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 8.128501382576301
""",
)

entry(
    index = 144,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(9.22241e+19,'m^3/(mol*s)'), n=-3.64403, w0=(246003,'J/mol'), E0=(79158.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.47763607570776156, var=19.936170164188464, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C
    Total Standard Deviation in ln(k): 10.151220452705022"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C
Total Standard Deviation in ln(k): 10.151220452705022""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C
Total Standard Deviation in ln(k): 10.151220452705022
""",
)

entry(
    index = 145,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(5.33096e+13,'m^3/(mol*s)'), n=-1.90062, w0=(248775,'J/mol'), E0=(24877.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.9646971416581305, var=31.886971574602665, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C
    Total Standard Deviation in ln(k): 13.744310493015316"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 13.744310493015316""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 13.744310493015316
""",
)

entry(
    index = 146,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C_Ext-1C-R_Ext-1C-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(43.7346,'m^3/(mol*s)'), n=1.28523, w0=(260050,'J/mol'), E0=(28612,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C_Ext-1C-R_Ext-1C-R_4R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C_Ext-1C-R_Ext-1C-R_4R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C_Ext-1C-R_Ext-1C-R_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C_Ext-1C-R_Ext-1C-R_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 147,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(9e+06,'m^3/(mol*s)'), n=0, w0=(260050,'J/mol'), E0=(16433.5,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_N-3BrCClO-u1_N-3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 148,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R_4BrCFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(1.15e+06,'m^3/(mol*s)'), n=0, w0=(237500,'J/mol'), E0=(25499.6,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R_4BrCFINOPSSi->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R_4BrCFINOPSSi->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R_4BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R_4BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 149,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R_N-4BrCFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(404904,'m^3/(mol*s)'), n=0.0717696, w0=(248775,'J/mol'), E0=(4810.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.501833267386881, var=0.03703918853040752, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R_N-4BrCFINOPSSi->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R_N-4BrCFINOPSSi->Br
    Total Standard Deviation in ln(k): 1.6467102578214547"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R_N-4BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 1.6467102578214547""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R_N-4BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 1.6467102578214547
""",
)

entry(
    index = 150,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_1BrClO->Br_Sp-4BrCFINOPSSi-3BrBrCCClFINOOPSSi",
    kinetics = ArrheniusBM(A=(7.85e+06,'m^3/(mol*s)'), n=0, w0=(237500,'J/mol'), E0=(23750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_1BrClO->Br_Sp-4BrCFINOPSSi-3BrBrCCClFINOOPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_1BrClO->Br_Sp-4BrCFINOPSSi-3BrBrCCClFINOOPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_1BrClO->Br_Sp-4BrCFINOPSSi-3BrBrCCClFINOOPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_1BrClO->Br_Sp-4BrCFINOPSSi-3BrBrCCClFINOOPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 151,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_1BrClO->Br_N-Sp-4BrCFINOPSSi-3BrBrCCClFINOOPSSi",
    kinetics = ArrheniusBM(A=(1.2e+07,'m^3/(mol*s)'), n=0, w0=(237500,'J/mol'), E0=(23750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_1BrClO->Br_N-Sp-4BrCFINOPSSi-3BrBrCCClFINOOPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_1BrClO->Br_N-Sp-4BrCFINOPSSi-3BrBrCCClFINOOPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_1BrClO->Br_N-Sp-4BrCFINOPSSi-3BrBrCCClFINOOPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_1BrClO->Br_N-Sp-4BrCFINOPSSi-3BrBrCCClFINOOPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 152,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_N-1BrClO->Br_Sp-4BrCFINOPSSi-3BrBrCCClFINOOPSSi",
    kinetics = ArrheniusBM(A=(36181.1,'m^3/(mol*s)'), n=0.525658, w0=(260050,'J/mol'), E0=(18554,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_N-1BrClO->Br_Sp-4BrCFINOPSSi-3BrBrCCClFINOOPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_N-1BrClO->Br_Sp-4BrCFINOPSSi-3BrBrCCClFINOOPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_N-1BrClO->Br_Sp-4BrCFINOPSSi-3BrBrCCClFINOOPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_N-1BrClO->Br_Sp-4BrCFINOPSSi-3BrBrCCClFINOOPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 153,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_N-1BrClO->Br_N-Sp-4BrCFINOPSSi-3BrBrCCClFINOOPSSi",
    kinetics = ArrheniusBM(A=(15049.5,'m^3/(mol*s)'), n=0.392587, w0=(260050,'J/mol'), E0=(26005,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_N-1BrClO->Br_N-Sp-4BrCFINOPSSi-3BrBrCCClFINOOPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_N-1BrClO->Br_N-Sp-4BrCFINOPSSi-3BrBrCCClFINOOPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_N-1BrClO->Br_N-Sp-4BrCFINOPSSi-3BrBrCCClFINOOPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_N-1BrClO->Br_N-Sp-4BrCFINOPSSi-3BrBrCCClFINOOPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 154,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O_3BrCCl-u1_3BrCCl->C",
    kinetics = ArrheniusBM(A=(6.05e+06,'m^3/(mol*s)'), n=0, w0=(237500,'J/mol'), E0=(23750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O_3BrCCl-u1_3BrCCl->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O_3BrCCl-u1_3BrCCl->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O_3BrCCl-u1_3BrCCl->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O_3BrCCl-u1_3BrCCl->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 155,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O_3BrCCl-u1_N-3BrCCl->C",
    kinetics = ArrheniusBM(A=(2.81493e+09,'m^3/(mol*s)'), n=-0.232559, w0=(204420,'J/mol'), E0=(11817.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O_3BrCCl-u1_N-3BrCCl->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O_3BrCCl-u1_N-3BrCCl->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O_3BrCCl-u1_N-3BrCCl->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_1BrClO->Br_N-3BrCClO->O_3BrCCl-u1_N-3BrCCl->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 156,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O",
    kinetics = ArrheniusBM(A=(30989.6,'m^3/(mol*s)'), n=0.875321, w0=(233190,'J/mol'), E0=(-678.428,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1934490555273065, var=0.7887783426216745, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O
    Total Standard Deviation in ln(k): 2.266522156551422"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O
Total Standard Deviation in ln(k): 2.266522156551422""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O
Total Standard Deviation in ln(k): 2.266522156551422
""",
)

entry(
    index = 157,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_N-1ClO->O",
    kinetics = ArrheniusBM(A=(3.7e+08,'m^3/(mol*s)'), n=0, w0=(204420,'J/mol'), E0=(8527.98,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_N-1ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_N-1ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_N-1ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_N-1ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 158,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClF->Cl_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.0063045,'m^3/(mol*s)'), n=2.56274, w0=(323500,'J/mol'), E0=(35930.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClF->Cl_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClF->Cl_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClF->Cl_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClF->Cl_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 159,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(0.000417549,'m^3/(mol*s)'), n=2.90659, w0=(323500,'J/mol'), E0=(49024.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.010034378026869378, var=0.3511158422147603, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_5R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_5R!H->Cl
    Total Standard Deviation in ln(k): 1.2131183498695897"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_5R!H->Cl
Total Standard Deviation in ln(k): 1.2131183498695897""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_5R!H->Cl
Total Standard Deviation in ln(k): 1.2131183498695897
""",
)

entry(
    index = 160,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(0.000130154,'m^3/(mol*s)'), n=3.058, w0=(323500,'J/mol'), E0=(43130.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.005291862584370542, var=1.2788026732044613, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl',), comment="""BM rule fitted to 6 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 2.28033391436092"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 2.28033391436092""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 2.28033391436092
""",
)

entry(
    index = 161,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.031369,'m^3/(mol*s)'), n=2.49657, w0=(323500,'J/mol'), E0=(51768,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.007264055775639266, var=0.3369529740647633, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R
    Total Standard Deviation in ln(k): 1.1819530096833968"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R
Total Standard Deviation in ln(k): 1.1819530096833968""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R
Total Standard Deviation in ln(k): 1.1819530096833968
""",
)

entry(
    index = 162,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_5R!H->Cl",
    kinetics = ArrheniusBM(A=(417.629,'m^3/(mol*s)'), n=1.69481, w0=(323500,'J/mol'), E0=(49291.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0010162657125841888, var=0.02084998831756513, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_5R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_5R!H->Cl
    Total Standard Deviation in ln(k): 0.29202765478224135"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_5R!H->Cl
Total Standard Deviation in ln(k): 0.29202765478224135""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_5R!H->Cl
Total Standard Deviation in ln(k): 0.29202765478224135
""",
)

entry(
    index = 163,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(9.7492e-06,'m^3/(mol*s)'), n=3.95534, w0=(323500,'J/mol'), E0=(24359.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.10788263752010444, var=0.2560632236934628, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl
    Total Standard Deviation in ln(k): 1.2855117801883134"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl
Total Standard Deviation in ln(k): 1.2855117801883134""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl
Total Standard Deviation in ln(k): 1.2855117801883134
""",
)

entry(
    index = 164,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-4R!H->F_Ext-5R!H-R_6R!H->F",
    kinetics = ArrheniusBM(A=(544.736,'m^3/(mol*s)'), n=1.68578, w0=(323500,'J/mol'), E0=(43199.7,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-4R!H->F_Ext-5R!H-R_6R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-4R!H->F_Ext-5R!H-R_6R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-4R!H->F_Ext-5R!H-R_6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-4R!H->F_Ext-5R!H-R_6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 165,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-4R!H->F_Ext-5R!H-R_N-6R!H->F",
    kinetics = ArrheniusBM(A=(684.364,'m^3/(mol*s)'), n=1.64514, w0=(323500,'J/mol'), E0=(36348.8,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-4R!H->F_Ext-5R!H-R_N-6R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-4R!H->F_Ext-5R!H-R_N-6R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-4R!H->F_Ext-5R!H-R_N-6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-4R!H->F_Ext-5R!H-R_N-6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 166,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_N-4BrCCl->Cl_4BrC->Br",
    kinetics = ArrheniusBM(A=(539.35,'m^3/(mol*s)'), n=1.7149, w0=(323500,'J/mol'), E0=(53918.5,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_N-4BrCCl->Cl_4BrC->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_N-4BrCCl->Cl_4BrC->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_N-4BrCCl->Cl_4BrC->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_N-4BrCCl->Cl_4BrC->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 167,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_N-4BrCCl->Cl_N-4BrC->Br",
    kinetics = ArrheniusBM(A=(506.769,'m^3/(mol*s)'), n=1.76845, w0=(323500,'J/mol'), E0=(50173.4,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_N-4BrCCl->Cl_N-4BrC->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_N-4BrCCl->Cl_N-4BrC->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_N-4BrCCl->Cl_N-4BrC->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->F_N-4BrCCl->Cl_N-4BrC->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 168,
    label = "Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br_Ext-1O-R_Ext-4R!H-R_Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(2137.95,'m^3/(mol*s)'), n=1.58633, w0=(298550,'J/mol'), E0=(29855,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br_Ext-1O-R_Ext-4R!H-R_Sp-5R!H-4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br_Ext-1O-R_Ext-4R!H-R_Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br_Ext-1O-R_Ext-4R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br_Ext-1O-R_Ext-4R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 169,
    label = "Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br_Ext-1O-R_Ext-4R!H-R_N-Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(1823.35,'m^3/(mol*s)'), n=1.55333, w0=(298550,'J/mol'), E0=(29855,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br_Ext-1O-R_Ext-4R!H-R_N-Sp-5R!H-4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br_Ext-1O-R_Ext-4R!H-R_N-Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br_Ext-1O-R_Ext-4R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-1BrO->Br_Ext-1O-R_Ext-4R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 170,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-4R!H-R_Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(0.000423303,'m^3/(mol*s)'), n=3.19649, w0=(285000,'J/mol'), E0=(47494.2,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-4R!H-R_Sp-5R!H-4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-4R!H-R_Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-4R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-4R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 171,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-4R!H-R_N-Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(0.00204522,'m^3/(mol*s)'), n=2.89817, w0=(285000,'J/mol'), E0=(65338.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-4R!H-R_N-Sp-5R!H-4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-4R!H-R_N-Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-4R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-4R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 172,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(0.0026651,'m^3/(mol*s)'), n=3.02759, w0=(285000,'J/mol'), E0=(35679,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 173,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(5.87465e-14,'m^3/(mol*s)'), n=5.55444, w0=(285000,'J/mol'), E0=(10334,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0016388859543622427, var=25.925937131661048, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 10.211731388202468"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_Ext-1C-R
Total Standard Deviation in ln(k): 10.211731388202468""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_Ext-1C-R
Total Standard Deviation in ln(k): 10.211731388202468
""",
)

entry(
    index = 174,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.114556,'m^3/(mol*s)'), n=1.8901, w0=(285000,'J/mol'), E0=(43815.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03077343477304079, var=7.62711397360311, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R
    Total Standard Deviation in ln(k): 5.613843176305182"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R
Total Standard Deviation in ln(k): 5.613843176305182""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R
Total Standard Deviation in ln(k): 5.613843176305182
""",
)

entry(
    index = 175,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-1C-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(0.000205056,'m^3/(mol*s)'), n=2.81796, w0=(285000,'J/mol'), E0=(44774.4,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-1C-R_5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-1C-R_5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-1C-R_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-1C-R_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 176,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-1C-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(0.000313942,'m^3/(mol*s)'), n=2.76015, w0=(285000,'J/mol'), E0=(44322.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-1C-R_N-5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-1C-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-1C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-1C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 177,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.977504,'m^3/(mol*s)'), n=1.94986, w0=(285000,'J/mol'), E0=(46204.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.08176437823042886, var=3.4454774624256657, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R',), comment="""BM rule fitted to 25 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R
    Total Standard Deviation in ln(k): 3.926626859015883"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R
Total Standard Deviation in ln(k): 3.926626859015883""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R
Total Standard Deviation in ln(k): 3.926626859015883
""",
)

entry(
    index = 178,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClFO->Cl",
    kinetics = ArrheniusBM(A=(21.7395,'m^3/(mol*s)'), n=1.04442, w0=(285000,'J/mol'), E0=(56419.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0025523409375730203, var=35.00276400810121, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClFO->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClFO->Cl
    Total Standard Deviation in ln(k): 11.867053878286942"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClFO->Cl
Total Standard Deviation in ln(k): 11.867053878286942""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClFO->Cl
Total Standard Deviation in ln(k): 11.867053878286942
""",
)

entry(
    index = 179,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl",
    kinetics = ArrheniusBM(A=(0.105865,'m^3/(mol*s)'), n=2.02415, w0=(285000,'J/mol'), E0=(45177.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.034165230998233674, var=2.7422982184916584, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl
    Total Standard Deviation in ln(k): 3.4056607080905006"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl
Total Standard Deviation in ln(k): 3.4056607080905006""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl
Total Standard Deviation in ln(k): 3.4056607080905006
""",
)

entry(
    index = 180,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_Ext-1C-R_4BrCFO->Br",
    kinetics = ArrheniusBM(A=(0.00880775,'m^3/(mol*s)'), n=2.67281, w0=(285000,'J/mol'), E0=(43351,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_Ext-1C-R_4BrCFO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_Ext-1C-R_4BrCFO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_Ext-1C-R_4BrCFO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_Ext-1C-R_4BrCFO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 181,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_Ext-1C-R_N-4BrCFO->Br",
    kinetics = ArrheniusBM(A=(0.0455873,'m^3/(mol*s)'), n=2.62423, w0=(285000,'J/mol'), E0=(47481.8,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_Ext-1C-R_N-4BrCFO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_Ext-1C-R_N-4BrCFO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_Ext-1C-R_N-4BrCFO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_Ext-1C-R_N-4BrCFO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 182,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_Sp-4CCFFOO=1C",
    kinetics = ArrheniusBM(A=(0.0713601,'m^3/(mol*s)'), n=2.71607, w0=(285000,'J/mol'), E0=(40112,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_Sp-4CCFFOO=1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_Sp-4CCFFOO=1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_Sp-4CCFFOO=1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_Sp-4CCFFOO=1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 183,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C",
    kinetics = ArrheniusBM(A=(0.398038,'m^3/(mol*s)'), n=2.25735, w0=(285000,'J/mol'), E0=(43242.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.04896491050341593, var=2.492198984344499, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C
    Total Standard Deviation in ln(k): 3.28784254776136"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C
Total Standard Deviation in ln(k): 3.28784254776136""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C
Total Standard Deviation in ln(k): 3.28784254776136
""",
)

entry(
    index = 184,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_1C-u0_4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.000774648,'m^3/(mol*s)'), n=2.8154, w0=(285000,'J/mol'), E0=(43955.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-5.252632270871114e-05, var=0.03856942825963039, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_1C-u0_4BrCFINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_1C-u0_4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 0.3938439195140297"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_1C-u0_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 0.3938439195140297""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_1C-u0_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 0.3938439195140297
""",
)

entry(
    index = 185,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_1C-u0_N-4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.2494,'m^3/(mol*s)'), n=1.79792, w0=(285000,'J/mol'), E0=(47302.9,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_1C-u0_N-4BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_1C-u0_N-4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_1C-u0_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_1C-u0_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 186,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_N-1C-u0_4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.0291245,'m^3/(mol*s)'), n=2.69164, w0=(285000,'J/mol'), E0=(36210.7,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_N-1C-u0_4BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_N-1C-u0_4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_N-1C-u0_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_N-1C-u0_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 187,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_N-1C-u0_N-4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.0169924,'m^3/(mol*s)'), n=2.72405, w0=(285000,'J/mol'), E0=(41346.9,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_N-1C-u0_N-4BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_N-1C-u0_N-4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_N-1C-u0_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_N-1C-u0_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 188,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-1C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi",
    kinetics = ArrheniusBM(A=(0.000390629,'m^3/(mol*s)'), n=3.36664, w0=(285000,'J/mol'), E0=(46000.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-1C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-1C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-1C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-1C_Ext-4BrCFINOPSSi-R_Sp-5R!H-4BrCFINOPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 189,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-1C_Ext-4BrCFINOPSSi-R_N-Sp-5R!H-4BrCFINOPSSi",
    kinetics = ArrheniusBM(A=(0.00684122,'m^3/(mol*s)'), n=2.86155, w0=(285000,'J/mol'), E0=(65621,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-1C_Ext-4BrCFINOPSSi-R_N-Sp-5R!H-4BrCFINOPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-1C_Ext-4BrCFINOPSSi-R_N-Sp-5R!H-4BrCFINOPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-1C_Ext-4BrCFINOPSSi-R_N-Sp-5R!H-4BrCFINOPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_N-Sp-4BrCFINOPSSi-1C_Ext-4BrCFINOPSSi-R_N-Sp-5R!H-4BrCFINOPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 190,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->Cl",
    kinetics = ArrheniusBM(A=(3.0767e+14,'m^3/(mol*s)'), n=-2.02659, w0=(244710,'J/mol'), E0=(80239.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.041884815588575645, var=7.141425269666211, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->Cl
    Total Standard Deviation in ln(k): 5.4625810417858265"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->Cl
Total Standard Deviation in ln(k): 5.4625810417858265""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->Cl
Total Standard Deviation in ln(k): 5.4625810417858265
""",
)

entry(
    index = 191,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(3.51561e+11,'m^3/(mol*s)'), n=-1.17675, w0=(246520,'J/mol'), E0=(30196.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.28143826918630704, var=1.2621831333721885, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl
    Total Standard Deviation in ln(k): 2.9593895235454375"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl
Total Standard Deviation in ln(k): 2.9593895235454375""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl
Total Standard Deviation in ln(k): 2.9593895235454375
""",
)

entry(
    index = 192,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_3BrClO->Br",
    kinetics = ArrheniusBM(A=(7.0092e+09,'m^3/(mol*s)'), n=-0.392, w0=(237500,'J/mol'), E0=(23750,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_3BrClO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_3BrClO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_3BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_3BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 193,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_N-3BrClO->Br",
    kinetics = ArrheniusBM(A=(3e+06,'m^3/(mol*s)'), n=0, w0=(260050,'J/mol'), E0=(26005,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_N-3BrClO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_N-3BrClO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_N-3BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_N-Sp-4R!H-1C_N-3BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 194,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R_N-4BrCFINOPSSi->Br_1BrClO->Br",
    kinetics = ArrheniusBM(A=(605000,'m^3/(mol*s)'), n=0, w0=(237500,'J/mol'), E0=(26474.9,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R_N-4BrCFINOPSSi->Br_1BrClO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R_N-4BrCFINOPSSi->Br_1BrClO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R_N-4BrCFINOPSSi->Br_1BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R_N-4BrCFINOPSSi->Br_1BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 195,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R_N-4BrCFINOPSSi->Br_N-1BrClO->Br",
    kinetics = ArrheniusBM(A=(714.922,'m^3/(mol*s)'), n=0.905401, w0=(260050,'J/mol'), E0=(17266.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R_N-4BrCFINOPSSi->Br_N-1BrClO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R_N-4BrCFINOPSSi->Br_N-1BrClO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R_N-4BrCFINOPSSi->Br_N-1BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_Ext-3BrCClO-R_N-4R!H->Cl_1BrClO-u0_Ext-3BrCClO-R_N-4BrCFINOPSSi->Br_N-1BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 196,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O_3BrCCl->Br",
    kinetics = ArrheniusBM(A=(37.6899,'m^3/(mol*s)'), n=1.87693, w0=(212550,'J/mol'), E0=(4521.27,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O_3BrCCl->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O_3BrCCl->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O_3BrCCl->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O_3BrCCl->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 197,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O_N-3BrCCl->Br",
    kinetics = ArrheniusBM(A=(3538.14,'m^3/(mol*s)'), n=1.14062, w0=(243510,'J/mol'), E0=(-1475.35,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.546019180092731, var=0.17558448032670193, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O_N-3BrCCl->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O_N-3BrCCl->Br
    Total Standard Deviation in ln(k): 4.724510468930931"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O_N-3BrCCl->Br
Total Standard Deviation in ln(k): 4.724510468930931""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O_N-3BrCCl->Br
Total Standard Deviation in ln(k): 4.724510468930931
""",
)

entry(
    index = 198,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_5R!H->Cl_Ext-4CF-R",
    kinetics = ArrheniusBM(A=(0.012647,'m^3/(mol*s)'), n=2.30939, w0=(323500,'J/mol'), E0=(42990.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_5R!H->Cl_Ext-4CF-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_5R!H->Cl_Ext-4CF-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_5R!H->Cl_Ext-4CF-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_5R!H->Cl_Ext-4CF-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 199,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_5BrCFINOPSSi->F",
    kinetics = ArrheniusBM(A=(8.97509e-12,'m^3/(mol*s)'), n=5.2402, w0=(323500,'J/mol'), E0=(22816.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.01873065651327944, var=1.1057890732951303, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_5BrCFINOPSSi->F',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_5BrCFINOPSSi->F
    Total Standard Deviation in ln(k): 2.1551713109638597"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_5BrCFINOPSSi->F
Total Standard Deviation in ln(k): 2.1551713109638597""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_5BrCFINOPSSi->F
Total Standard Deviation in ln(k): 2.1551713109638597
""",
)

entry(
    index = 200,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_N-5BrCFINOPSSi->F",
    kinetics = ArrheniusBM(A=(35.8296,'m^3/(mol*s)'), n=1.41913, w0=(323500,'J/mol'), E0=(53566.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1632313431309324, var=4.501994380734046, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_N-5BrCFINOPSSi->F',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_N-5BrCFINOPSSi->F
    Total Standard Deviation in ln(k): 4.663756587532718"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_N-5BrCFINOPSSi->F
Total Standard Deviation in ln(k): 4.663756587532718""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_N-5BrCFINOPSSi->F
Total Standard Deviation in ln(k): 4.663756587532718
""",
)

entry(
    index = 201,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.011833,'m^3/(mol*s)'), n=2.64514, w0=(323500,'J/mol'), E0=(50404.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.012695615969692844, var=0.14425589723506763, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 0.7933176515010197"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 0.7933176515010197""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 0.7933176515010197
""",
)

entry(
    index = 202,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_5R!H->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(943.579,'m^3/(mol*s)'), n=1.62342, w0=(323500,'J/mol'), E0=(52336.7,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_5R!H->Cl_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_5R!H->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_5R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_5R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 203,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C",
    kinetics = ArrheniusBM(A=(8.54244e-06,'m^3/(mol*s)'), n=3.99367, w0=(323500,'J/mol'), E0=(15690.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.12933878647251654, var=0.09112359252169241, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C
    Total Standard Deviation in ln(k): 0.9301348795478352"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C
Total Standard Deviation in ln(k): 0.9301348795478352""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C
Total Standard Deviation in ln(k): 0.9301348795478352
""",
)

entry(
    index = 204,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C",
    kinetics = ArrheniusBM(A=(0.12216,'m^3/(mol*s)'), n=2.69824, w0=(323500,'J/mol'), E0=(40539.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.010768866808436323, var=0.5313449675193981, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C
    Total Standard Deviation in ln(k): 1.4883772760692606"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C
Total Standard Deviation in ln(k): 1.4883772760692606""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C
Total Standard Deviation in ln(k): 1.4883772760692606
""",
)

entry(
    index = 205,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.00301022,'m^3/(mol*s)'), n=2.08084, w0=(285000,'J/mol'), E0=(38417.5,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 206,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(6.32929e-07,'m^3/(mol*s)'), n=3.71277, w0=(285000,'J/mol'), E0=(31603.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.025780928165611994, var=0.37201815371016694, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 1.2875300993267618"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 1.2875300993267618""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 1.2875300993267618
""",
)

entry(
    index = 207,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.0144958,'m^3/(mol*s)'), n=1.79772, w0=(285000,'J/mol'), E0=(43345.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.006598701824353219, var=0.19139735168650115, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 0.8936308617923329"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-1C-R
Total Standard Deviation in ln(k): 0.8936308617923329""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-1C-R
Total Standard Deviation in ln(k): 0.8936308617923329
""",
)

entry(
    index = 208,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_4CClFO->O",
    kinetics = ArrheniusBM(A=(4.68481e-07,'m^3/(mol*s)'), n=3.98461, w0=(285000,'J/mol'), E0=(13071.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_4CClFO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_4CClFO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_4CClFO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_4CClFO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 209,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O",
    kinetics = ArrheniusBM(A=(0.793726,'m^3/(mol*s)'), n=1.9672, w0=(285000,'J/mol'), E0=(46654.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.08003454306675684, var=3.04788688608911, Tref=1000.0, N=24, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O',), comment="""BM rule fitted to 24 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O
    Total Standard Deviation in ln(k): 3.7009980729347847"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O
Total Standard Deviation in ln(k): 3.7009980729347847""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O
Total Standard Deviation in ln(k): 3.7009980729347847
""",
)

entry(
    index = 210,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClFO->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.00552521,'m^3/(mol*s)'), n=1.74736, w0=(285000,'J/mol'), E0=(45937.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClFO->Cl_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClFO->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClFO->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_4CClFO->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 211,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C",
    kinetics = ArrheniusBM(A=(0.000477666,'m^3/(mol*s)'), n=2.77689, w0=(285000,'J/mol'), E0=(41296.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0002257121853738823, var=1.0844980119831775, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C
    Total Standard Deviation in ln(k): 2.088282875312407"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C
Total Standard Deviation in ln(k): 2.088282875312407""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C
Total Standard Deviation in ln(k): 2.088282875312407
""",
)

entry(
    index = 212,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C",
    kinetics = ArrheniusBM(A=(119.365,'m^3/(mol*s)'), n=1.05254, w0=(285000,'J/mol'), E0=(50404.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06541409890968033, var=6.338402591677906, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C
    Total Standard Deviation in ln(k): 5.211515023531625"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C
Total Standard Deviation in ln(k): 5.211515023531625""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C
Total Standard Deviation in ln(k): 5.211515023531625
""",
)

entry(
    index = 213,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_4CFO->O",
    kinetics = ArrheniusBM(A=(0.00808906,'m^3/(mol*s)'), n=2.74525, w0=(285000,'J/mol'), E0=(24580.1,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_4CFO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_4CFO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_4CFO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_4CFO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 214,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O",
    kinetics = ArrheniusBM(A=(0.000236861,'m^3/(mol*s)'), n=3.23973, w0=(285000,'J/mol'), E0=(43114.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0033080269062343124, var=0.15624262746826664, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O
    Total Standard Deviation in ln(k): 0.8007340485455938"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O
Total Standard Deviation in ln(k): 0.8007340485455938""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O
Total Standard Deviation in ln(k): 0.8007340485455938
""",
)

entry(
    index = 215,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_1C-u0_4BrCFINOPSSi->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(0.00740299,'m^3/(mol*s)'), n=2.54444, w0=(285000,'J/mol'), E0=(46548.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_1C-u0_4BrCFINOPSSi->C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_1C-u0_4BrCFINOPSSi->C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_1C-u0_4BrCFINOPSSi->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_N-4R!H->Cl_Sp-4BrCFINOPSSi-1C_1C-u0_4BrCFINOPSSi->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 216,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->Cl_3BrClO->Br",
    kinetics = ArrheniusBM(A=(8.1e+07,'m^3/(mol*s)'), n=0, w0=(237500,'J/mol'), E0=(62615.9,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->Cl_3BrClO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->Cl_3BrClO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->Cl_3BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->Cl_3BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 217,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->Cl_N-3BrClO->Br",
    kinetics = ArrheniusBM(A=(8.1e+07,'m^3/(mol*s)'), n=0, w0=(251920,'J/mol'), E0=(79217.1,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->Cl_N-3BrClO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->Cl_N-3BrClO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->Cl_N-3BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->Cl_N-3BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 218,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_4BrCF->Br",
    kinetics = ArrheniusBM(A=(9.62687e+10,'m^3/(mol*s)'), n=-0.908295, w0=(237500,'J/mol'), E0=(36569.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_4BrCF->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_4BrCF->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_4BrCF->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_4BrCF->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 219,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br",
    kinetics = ArrheniusBM(A=(2.04328e+17,'m^3/(mol*s)'), n=-2.97377, w0=(248775,'J/mol'), E0=(42761.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.13504911324859117, var=5.841329224901494, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br
    Total Standard Deviation in ln(k): 5.184531909071357"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br
Total Standard Deviation in ln(k): 5.184531909071357""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br
Total Standard Deviation in ln(k): 5.184531909071357
""",
)

entry(
    index = 220,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O_N-3BrCCl->Br_3CCl->C",
    kinetics = ArrheniusBM(A=(0.036695,'m^3/(mol*s)'), n=2.78053, w0=(260050,'J/mol'), E0=(19485.4,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O_N-3BrCCl->Br_3CCl->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O_N-3BrCCl->Br_3CCl->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O_N-3BrCCl->Br_3CCl->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O_N-3BrCCl->Br_3CCl->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 221,
    label = "Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O_N-3BrCCl->Br_N-3CCl->C",
    kinetics = ArrheniusBM(A=(2.01522e+07,'m^3/(mol*s)'), n=-0.231972, w0=(226970,'J/mol'), E0=(-1645.85,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O_N-3BrCCl->Br_N-3CCl->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O_N-3BrCCl->Br_N-3CCl->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O_N-3BrCCl->Br_N-3CCl->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_N-1BrCClFINOPSSi->C_1BrClO-u0_N-1BrClO->Br_3BrCClO-u1_N-3BrCClO->O_1ClO->O_N-3BrCCl->Br_N-3CCl->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 222,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_5BrCFINOPSSi->F_Ext-4CF-R",
    kinetics = ArrheniusBM(A=(0.0454822,'m^3/(mol*s)'), n=2.13705, w0=(323500,'J/mol'), E0=(44942.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_5BrCFINOPSSi->F_Ext-4CF-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_5BrCFINOPSSi->F_Ext-4CF-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_5BrCFINOPSSi->F_Ext-4CF-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_5BrCFINOPSSi->F_Ext-4CF-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 223,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_5BrCFINOPSSi->F_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.17187e-08,'m^3/(mol*s)'), n=3.99558, w0=(323500,'J/mol'), E0=(20391.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_5BrCFINOPSSi->F_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_5BrCFINOPSSi->F_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_5BrCFINOPSSi->F_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_5BrCFINOPSSi->F_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 224,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_N-5BrCFINOPSSi->F_Ext-4CF-R",
    kinetics = ArrheniusBM(A=(0.315343,'m^3/(mol*s)'), n=2.015, w0=(323500,'J/mol'), E0=(44975.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_N-5BrCFINOPSSi->F_Ext-4CF-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_N-5BrCFINOPSSi->F_Ext-4CF-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_N-5BrCFINOPSSi->F_Ext-4CF-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_N-5BrCFINOPSSi->F_Ext-4CF-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 225,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_N-5BrCFINOPSSi->F_Ext-3C-R",
    kinetics = ArrheniusBM(A=(5.30094e-09,'m^3/(mol*s)'), n=4.17923, w0=(323500,'J/mol'), E0=(20582.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_N-5BrCFINOPSSi->F_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_N-5BrCFINOPSSi->F_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_N-5BrCFINOPSSi->F_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_Ext-4CF-R_N-5R!H->Cl_N-5BrCFINOPSSi->F_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 226,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R_5R!H->F",
    kinetics = ArrheniusBM(A=(0.0397032,'m^3/(mol*s)'), n=2.51385, w0=(323500,'J/mol'), E0=(51969.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.005782572228181063, var=0.0032741965040595632, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R_5R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R_5R!H->F
    Total Standard Deviation in ln(k): 0.12924121010462356"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R_5R!H->F
Total Standard Deviation in ln(k): 0.12924121010462356""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R_5R!H->F
Total Standard Deviation in ln(k): 0.12924121010462356
""",
)

entry(
    index = 227,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(4.66724e-05,'m^3/(mol*s)'), n=3.11447, w0=(323500,'J/mol'), E0=(23964.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R_N-5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R_N-5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 228,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(0.927,'m^3/(mol*s)'), n=2.44362, w0=(323500,'J/mol'), E0=(41073.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04912247210470259, var=0.05873039802134528, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R
    Total Standard Deviation in ln(k): 0.6092579196340154"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R
Total Standard Deviation in ln(k): 0.6092579196340154""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R
Total Standard Deviation in ln(k): 0.6092579196340154
""",
)

entry(
    index = 229,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-1C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(874.403,'m^3/(mol*s)'), n=1.67238, w0=(323500,'J/mol'), E0=(48499.7,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-1C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-1C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 230,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-1C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(898.897,'m^3/(mol*s)'), n=1.67337, w0=(323500,'J/mol'), E0=(50700.6,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-1C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-1C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 231,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.56625e-06,'m^3/(mol*s)'), n=4.2085, w0=(323500,'J/mol'), E0=(17687.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.002293917155819721, var=2.289759174481826, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_Ext-1C-R
    Total Standard Deviation in ln(k): 3.0393187504038814"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.0393187504038814""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.0393187504038814
""",
)

entry(
    index = 232,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_5BrF->Br",
    kinetics = ArrheniusBM(A=(455.07,'m^3/(mol*s)'), n=1.66953, w0=(323500,'J/mol'), E0=(52930.5,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_5BrF->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_5BrF->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_5BrF->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_5BrF->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 233,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_N-5BrF->Br",
    kinetics = ArrheniusBM(A=(353.002,'m^3/(mol*s)'), n=1.6735, w0=(323500,'J/mol'), E0=(53825.1,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_N-5BrF->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_N-5BrF->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_N-5BrF->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_N-5BrF->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 234,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.000180709,'m^3/(mol*s)'), n=2.96193, w0=(285000,'J/mol'), E0=(33455.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0028082580359234167, var=0.15366932740888917, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 0.7929256974382358"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R_Ext-1C-R
Total Standard Deviation in ln(k): 0.7929256974382358""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R_Ext-1C-R
Total Standard Deviation in ln(k): 0.7929256974382358
""",
)

entry(
    index = 235,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-1C-R_6R!H->Cl",
    kinetics = ArrheniusBM(A=(0.000746917,'m^3/(mol*s)'), n=2.18514, w0=(285000,'J/mol'), E0=(42277.3,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-1C-R_6R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-1C-R_6R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-1C-R_6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-1C-R_6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 236,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-1C-R_N-6R!H->Cl",
    kinetics = ArrheniusBM(A=(0.000258195,'m^3/(mol*s)'), n=2.26509, w0=(285000,'J/mol'), E0=(35410,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-1C-R_N-6R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-1C-R_N-6R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-1C-R_N-6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-1C-R_N-6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 237,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(5.07487,'m^3/(mol*s)'), n=1.66708, w0=(285000,'J/mol'), E0=(46664.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.09847682045636451, var=3.5506626931928364, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R',), comment="""BM rule fitted to 19 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R
    Total Standard Deviation in ln(k): 4.024992040103632"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R
Total Standard Deviation in ln(k): 4.024992040103632""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R
Total Standard Deviation in ln(k): 4.024992040103632
""",
)

entry(
    index = 238,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_4CClF->C",
    kinetics = ArrheniusBM(A=(8.81075e-05,'m^3/(mol*s)'), n=3.34357, w0=(285000,'J/mol'), E0=(47936.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0006795599920784333, var=0.39052057730436157, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_4CClF->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_4CClF->C
    Total Standard Deviation in ln(k): 1.2544993774709725"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_4CClF->C
Total Standard Deviation in ln(k): 1.2544993774709725""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_4CClF->C
Total Standard Deviation in ln(k): 1.2544993774709725
""",
)

entry(
    index = 239,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_N-4CClF->C",
    kinetics = ArrheniusBM(A=(0.143922,'m^3/(mol*s)'), n=2.44048, w0=(285000,'J/mol'), E0=(49271.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.027948136458935763, var=0.9181193096521969, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_N-4CClF->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_N-4CClF->C
    Total Standard Deviation in ln(k): 1.9911293815490745"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_N-4CClF->C
Total Standard Deviation in ln(k): 1.9911293815490745""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_N-4CClF->C
Total Standard Deviation in ln(k): 1.9911293815490745
""",
)

entry(
    index = 240,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.000330294,'m^3/(mol*s)'), n=2.80103, w0=(285000,'J/mol'), E0=(38778.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0027563624524001777, var=1.7774069629778333, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R
    Total Standard Deviation in ln(k): 2.679626852915243"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R
Total Standard Deviation in ln(k): 2.679626852915243""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R
Total Standard Deviation in ln(k): 2.679626852915243
""",
)

entry(
    index = 241,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(5.46688e-05,'m^3/(mol*s)'), n=3.05096, w0=(285000,'J/mol'), E0=(42425.4,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 242,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(214.018,'m^3/(mol*s)'), n=0.986263, w0=(285000,'J/mol'), E0=(50189.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.05981998444868818, var=8.370678624296, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R
    Total Standard Deviation in ln(k): 5.950426072326196"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R
Total Standard Deviation in ln(k): 5.950426072326196""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R
Total Standard Deviation in ln(k): 5.950426072326196
""",
)

entry(
    index = 243,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O_4CF->C",
    kinetics = ArrheniusBM(A=(0.000105146,'m^3/(mol*s)'), n=3.31908, w0=(285000,'J/mol'), E0=(41967.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0001228506120685026, var=0.18068500119284198, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O_4CF->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O_4CF->C
    Total Standard Deviation in ln(k): 0.8524625795464832"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O_4CF->C
Total Standard Deviation in ln(k): 0.8524625795464832""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O_4CF->C
Total Standard Deviation in ln(k): 0.8524625795464832
""",
)

entry(
    index = 244,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O_N-4CF->C",
    kinetics = ArrheniusBM(A=(0.0270554,'m^3/(mol*s)'), n=2.71539, w0=(285000,'J/mol'), E0=(50311.5,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O_N-4CF->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O_N-4CF->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O_N-4CF->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O_N-4CF->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 245,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_Ext-1C-R",
    kinetics = ArrheniusBM(A=(5.14736e+11,'m^3/(mol*s)'), n=-1.43733, w0=(248775,'J/mol'), E0=(32987.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.16852641275786082, var=0.283368096851936, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_Ext-1C-R
    Total Standard Deviation in ln(k): 1.4906003920342725"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_Ext-1C-R
Total Standard Deviation in ln(k): 1.4906003920342725""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_Ext-1C-R
Total Standard Deviation in ln(k): 1.4906003920342725
""",
)

entry(
    index = 246,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_3BrClO->Br",
    kinetics = ArrheniusBM(A=(1.27147e+10,'m^3/(mol*s)'), n=-0.525071, w0=(237500,'J/mol'), E0=(23750,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_3BrClO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_3BrClO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_3BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_3BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 247,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_N-3BrClO->Br",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(260050,'J/mol'), E0=(18537.6,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_N-3BrClO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_N-3BrClO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_N-3BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_N-3BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 248,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R_5R!H->F_6R!H->C",
    kinetics = ArrheniusBM(A=(0.00138706,'m^3/(mol*s)'), n=2.76619, w0=(323500,'J/mol'), E0=(34165.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R_5R!H->F_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R_5R!H->F_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R_5R!H->F_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R_5R!H->F_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 249,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R_5R!H->F_N-6R!H->C",
    kinetics = ArrheniusBM(A=(0.00946276,'m^3/(mol*s)'), n=2.56954, w0=(323500,'J/mol'), E0=(40522,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R_5R!H->F_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R_5R!H->F_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R_5R!H->F_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClF->Cl_4CF->F_Ext-3C-R_Ext-3C-R_5R!H->F_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 250,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(964.854,'m^3/(mol*s)'), n=1.55787, w0=(323500,'J/mol'), E0=(51737.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=6.003155483946566e-05, var=0.035260980847982175, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 0.3765981306520775"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_Ext-1C-R
Total Standard Deviation in ln(k): 0.3765981306520775""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_Ext-1C-R
Total Standard Deviation in ln(k): 0.3765981306520775
""",
)

entry(
    index = 251,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_6R!H->F",
    kinetics = ArrheniusBM(A=(384.224,'m^3/(mol*s)'), n=1.70269, w0=(323500,'J/mol'), E0=(48256.9,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_6R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_6R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 252,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_N-6R!H->F",
    kinetics = ArrheniusBM(A=(401.227,'m^3/(mol*s)'), n=1.6928, w0=(323500,'J/mol'), E0=(50270.9,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_N-6R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_N-6R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_N-6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_N-6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 253,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_Ext-1C-R_5BrF->Br",
    kinetics = ArrheniusBM(A=(579.05,'m^3/(mol*s)'), n=1.60333, w0=(323500,'J/mol'), E0=(53510.2,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_Ext-1C-R_5BrF->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_Ext-1C-R_5BrF->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_Ext-1C-R_5BrF->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_Ext-1C-R_5BrF->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 254,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_Ext-1C-R_N-5BrF->Br",
    kinetics = ArrheniusBM(A=(1349.13,'m^3/(mol*s)'), n=1.64247, w0=(323500,'J/mol'), E0=(53987.7,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_Ext-1C-R_N-5BrF->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_Ext-1C-R_N-5BrF->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_Ext-1C-R_N-5BrF->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_N-5BrCF->C_Ext-1C-R_N-5BrF->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 255,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R_Ext-1C-R_7R!H->Cl",
    kinetics = ArrheniusBM(A=(4.43199e-05,'m^3/(mol*s)'), n=3.11015, w0=(285000,'J/mol'), E0=(31496,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R_Ext-1C-R_7R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R_Ext-1C-R_7R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R_Ext-1C-R_7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R_Ext-1C-R_7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 256,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R_Ext-1C-R_N-7R!H->Cl",
    kinetics = ArrheniusBM(A=(6.82116e-05,'m^3/(mol*s)'), n=3.11838, w0=(285000,'J/mol'), E0=(33272.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R_Ext-1C-R_N-7R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R_Ext-1C-R_N-7R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R_Ext-1C-R_N-7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->Br_Ext-3C-R_Ext-3C-R_Ext-1C-R_N-7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 257,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(480.556,'m^3/(mol*s)'), n=1.29214, w0=(285000,'J/mol'), E0=(50945.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.20624779850418581, var=1.1914187422027946, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 2.7064215811898378"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 2.7064215811898378""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 2.7064215811898378
""",
)

entry(
    index = 258,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br",
    kinetics = ArrheniusBM(A=(0.000773894,'m^3/(mol*s)'), n=2.90011, w0=(285000,'J/mol'), E0=(39193.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.006620139126459195, var=0.4414694101957124, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br
    Total Standard Deviation in ln(k): 1.348642939626891"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br
Total Standard Deviation in ln(k): 1.348642939626891""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br
Total Standard Deviation in ln(k): 1.348642939626891
""",
)

entry(
    index = 259,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br",
    kinetics = ArrheniusBM(A=(77.9113,'m^3/(mol*s)'), n=1.16951, w0=(285000,'J/mol'), E0=(48855.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.057171631873927896, var=4.879243160035557, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br
    Total Standard Deviation in ln(k): 4.571908421191888"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br
Total Standard Deviation in ln(k): 4.571908421191888""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br
Total Standard Deviation in ln(k): 4.571908421191888
""",
)

entry(
    index = 260,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_4CClF->C_5R!H->C",
    kinetics = ArrheniusBM(A=(1.15283e-07,'m^3/(mol*s)'), n=4.09835, w0=(285000,'J/mol'), E0=(37946.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_4CClF->C_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_4CClF->C_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_4CClF->C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_4CClF->C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 261,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_4CClF->C_N-5R!H->C",
    kinetics = ArrheniusBM(A=(7.45313e-06,'m^3/(mol*s)'), n=3.64088, w0=(285000,'J/mol'), E0=(42669.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_4CClF->C_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_4CClF->C_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_4CClF->C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_4CClF->C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 262,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_N-4CClF->C_4ClF->Cl",
    kinetics = ArrheniusBM(A=(9.18527e-06,'m^3/(mol*s)'), n=3.62595, w0=(285000,'J/mol'), E0=(30670.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_N-4CClF->C_4ClF->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_N-4CClF->C_4ClF->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_N-4CClF->C_4ClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_N-4CClF->C_4ClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 263,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_N-4CClF->C_N-4ClF->Cl",
    kinetics = ArrheniusBM(A=(0.00170737,'m^3/(mol*s)'), n=3.00893, w0=(285000,'J/mol'), E0=(48298.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.4954693600540294e-05, var=0.009081974526389201, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_N-4CClF->C_N-4ClF->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_N-4CClF->C_N-4ClF->Cl
    Total Standard Deviation in ln(k): 0.1911629898092292"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_N-4CClF->C_N-4ClF->Cl
Total Standard Deviation in ln(k): 0.1911629898092292""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_N-4CClF->C_N-4ClF->Cl
Total Standard Deviation in ln(k): 0.1911629898092292
""",
)

entry(
    index = 264,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.000200112,'m^3/(mol*s)'), n=2.8105, w0=(285000,'J/mol'), E0=(36982.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0026457385905469433, var=2.1221917761527136, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 2.927094409013472"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 2.927094409013472""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 2.927094409013472
""",
)

entry(
    index = 265,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(185.755,'m^3/(mol*s)'), n=1.11189, w0=(285000,'J/mol'), E0=(50914.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06786545315396314, var=7.550125354714639, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C
    Total Standard Deviation in ln(k): 5.679025305484025"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 5.679025305484025""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 5.679025305484025
""",
)

entry(
    index = 266,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.0089246,'m^3/(mol*s)'), n=1.86732, w0=(285000,'J/mol'), E0=(38831,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 267,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O_4CF->C_5R!H->C",
    kinetics = ArrheniusBM(A=(0.0105062,'m^3/(mol*s)'), n=2.7954, w0=(285000,'J/mol'), E0=(48899.3,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O_4CF->C_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O_4CF->C_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O_4CF->C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O_4CF->C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 268,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O_4CF->C_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.0117903,'m^3/(mol*s)'), n=2.75736, w0=(285000,'J/mol'), E0=(50173.8,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O_4CF->C_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O_4CF->C_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O_4CF->C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-1C-R_Ext-1C-R_N-4R!H->Cl_N-4BrCFO->Br_N-Sp-4CCFFOO=1C_N-4CFO->O_4CF->C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 269,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_Ext-1C-R_3BrClO->Br",
    kinetics = ArrheniusBM(A=(2.47962e+10,'m^3/(mol*s)'), n=-0.904814, w0=(237500,'J/mol'), E0=(40176.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_Ext-1C-R_3BrClO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_Ext-1C-R_3BrClO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_Ext-1C-R_3BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_Ext-1C-R_3BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 270,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_Ext-1C-R_N-3BrClO->Br",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(260050,'J/mol'), E0=(22978,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_Ext-1C-R_N-3BrClO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_Ext-1C-R_N-3BrClO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_Ext-1C-R_N-3BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_N-3BrCClO->C_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Cl_N-4BrCF->Br_Ext-1C-R_N-3BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 271,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_Ext-1C-R_6R!H->Br",
    kinetics = ArrheniusBM(A=(659.135,'m^3/(mol*s)'), n=1.65584, w0=(323500,'J/mol'), E0=(54255.4,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_Ext-1C-R_6R!H->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_Ext-1C-R_6R!H->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_Ext-1C-R_6R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_Ext-1C-R_6R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 272,
    label = "Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_Ext-1C-R_N-6R!H->Br",
    kinetics = ArrheniusBM(A=(590.348,'m^3/(mol*s)'), n=1.65419, w0=(323500,'J/mol'), E0=(54373,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_Ext-1C-R_N-6R!H->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_Ext-1C-R_N-6R!H->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_Ext-1C-R_N-6R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_3R->H_1BrCClFINOPSSi->C_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_4R!H->F_N-5R!H->Cl_5BrCF->C_Ext-5C-R_Ext-1C-R_N-6R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 273,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_7R!H->Br",
    kinetics = ArrheniusBM(A=(0.000381437,'m^3/(mol*s)'), n=3.1179, w0=(285000,'J/mol'), E0=(38337.1,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_7R!H->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_7R!H->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_7R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_7R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 274,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br",
    kinetics = ArrheniusBM(A=(4759.01,'m^3/(mol*s)'), n=0.986845, w0=(285000,'J/mol'), E0=(52682.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2445648264977929, var=1.8075161306801444, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br
    Total Standard Deviation in ln(k): 3.3097284412909818"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br
Total Standard Deviation in ln(k): 3.3097284412909818""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br
Total Standard Deviation in ln(k): 3.3097284412909818
""",
)

entry(
    index = 275,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.00030578,'m^3/(mol*s)'), n=2.98502, w0=(285000,'J/mol'), E0=(33258.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.002923684157833714, var=0.10836170129093096, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_Ext-1C-R
    Total Standard Deviation in ln(k): 0.6672714199074092"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_Ext-1C-R
Total Standard Deviation in ln(k): 0.6672714199074092""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_Ext-1C-R
Total Standard Deviation in ln(k): 0.6672714199074092
""",
)

entry(
    index = 276,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_4CClF->Cl",
    kinetics = ArrheniusBM(A=(8.64676e-05,'m^3/(mol*s)'), n=3.24132, w0=(285000,'J/mol'), E0=(41193.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_4CClF->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_4CClF->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_4CClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_4CClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 277,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_N-4CClF->Cl",
    kinetics = ArrheniusBM(A=(6.23785e-05,'m^3/(mol*s)'), n=3.19274, w0=(285000,'J/mol'), E0=(40642.6,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_N-4CClF->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_N-4CClF->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_N-4CClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_N-4CClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 278,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_Sp-6CCFF=1C",
    kinetics = ArrheniusBM(A=(7.71163,'m^3/(mol*s)'), n=1.60255, w0=(285000,'J/mol'), E0=(47223.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0010547291293545415, var=52.36559508300653, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_Sp-6CCFF=1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_Sp-6CCFF=1C
    Total Standard Deviation in ln(k): 14.509730241192196"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_Sp-6CCFF=1C
Total Standard Deviation in ln(k): 14.509730241192196""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_Sp-6CCFF=1C
Total Standard Deviation in ln(k): 14.509730241192196
""",
)

entry(
    index = 279,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C",
    kinetics = ArrheniusBM(A=(0.00746841,'m^3/(mol*s)'), n=2.32272, w0=(285000,'J/mol'), E0=(40495.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.022353407240007513, var=3.3719093137906873, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C
    Total Standard Deviation in ln(k): 3.737411120832148"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C
Total Standard Deviation in ln(k): 3.737411120832148""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C
Total Standard Deviation in ln(k): 3.737411120832148
""",
)

entry(
    index = 280,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_N-4CClF->C_N-4ClF->Cl_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.29521e-05,'m^3/(mol*s)'), n=3.56704, w0=(285000,'J/mol'), E0=(39483.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_N-4CClF->C_N-4ClF->Cl_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_N-4CClF->C_N-4ClF->Cl_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_N-4CClF->C_N-4ClF->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_N-4CClF->C_N-4ClF->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 281,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.0586022,'m^3/(mol*s)'), n=1.72086, w0=(285000,'J/mol'), E0=(33512.9,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 282,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(2.8472e-05,'m^3/(mol*s)'), n=3.18744, w0=(285000,'J/mol'), E0=(38752.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-8.400365728336307e-06, var=3.3182018065670245, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 3.6518329023890828"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R_Ext-4C-R
Total Standard Deviation in ln(k): 3.6518329023890828""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R_Ext-4C-R
Total Standard Deviation in ln(k): 3.6518329023890828
""",
)

entry(
    index = 283,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_Sp-5C=1C",
    kinetics = ArrheniusBM(A=(8.28059e-05,'m^3/(mol*s)'), n=3.24854, w0=(285000,'J/mol'), E0=(40150.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_Sp-5C=1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_Sp-5C=1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_Sp-5C=1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_Sp-5C=1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 284,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_N-Sp-5C=1C",
    kinetics = ArrheniusBM(A=(0.00277396,'m^3/(mol*s)'), n=2.44531, w0=(285000,'J/mol'), E0=(39818.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.012674661724953615, var=11.03129223350531, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_N-Sp-5C=1C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_N-Sp-5C=1C
    Total Standard Deviation in ln(k): 6.690250524190503"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_N-Sp-5C=1C
Total Standard Deviation in ln(k): 6.690250524190503""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_N-Sp-5C=1C
Total Standard Deviation in ln(k): 6.690250524190503
""",
)

entry(
    index = 285,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br_7CClFINOPSSi->Cl",
    kinetics = ArrheniusBM(A=(0.00597426,'m^3/(mol*s)'), n=2.75967, w0=(285000,'J/mol'), E0=(41773.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00014759201242752488, var=2.1953149130367566, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br_7CClFINOPSSi->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br_7CClFINOPSSi->Cl
    Total Standard Deviation in ln(k): 2.970705633055776"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br_7CClFINOPSSi->Cl
Total Standard Deviation in ln(k): 2.970705633055776""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br_7CClFINOPSSi->Cl
Total Standard Deviation in ln(k): 2.970705633055776
""",
)

entry(
    index = 286,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br_N-7CClFINOPSSi->Cl",
    kinetics = ArrheniusBM(A=(5.74384e+07,'m^3/(mol*s)'), n=-0.251198, w0=(285000,'J/mol'), E0=(59834.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.02095154746235566, var=7.8620747611145045, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br_N-7CClFINOPSSi->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br_N-7CClFINOPSSi->Cl
    Total Standard Deviation in ln(k): 5.673797249440488"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br_N-7CClFINOPSSi->Cl
Total Standard Deviation in ln(k): 5.673797249440488""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br_N-7CClFINOPSSi->Cl
Total Standard Deviation in ln(k): 5.673797249440488
""",
)

entry(
    index = 287,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_Ext-1C-R_4CClF->Cl",
    kinetics = ArrheniusBM(A=(8.62315e-05,'m^3/(mol*s)'), n=3.11892, w0=(285000,'J/mol'), E0=(31439.8,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_Ext-1C-R_4CClF->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_Ext-1C-R_4CClF->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_Ext-1C-R_4CClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_Ext-1C-R_4CClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 288,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_Ext-1C-R_N-4CClF->Cl",
    kinetics = ArrheniusBM(A=(0.000139321,'m^3/(mol*s)'), n=3.1149, w0=(285000,'J/mol'), E0=(33287,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_Ext-1C-R_N-4CClF->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_Ext-1C-R_N-4CClF->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_Ext-1C-R_N-4CClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_6R!H->Br_Ext-1C-R_N-4CClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 289,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_Sp-6CCFF=1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.000171743,'m^3/(mol*s)'), n=2.56312, w0=(285000,'J/mol'), E0=(33928,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_Sp-6CCFF=1C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_Sp-6CCFF=1C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_Sp-6CCFF=1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_Sp-6CCFF=1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 290,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.00792627,'m^3/(mol*s)'), n=2.4227, w0=(285000,'J/mol'), E0=(40890.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.02121621391788451, var=3.2715474241597717, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R
    Total Standard Deviation in ln(k): 3.6793554935499233"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R
Total Standard Deviation in ln(k): 3.6793554935499233""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R
Total Standard Deviation in ln(k): 3.6793554935499233
""",
)

entry(
    index = 291,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.00231591,'m^3/(mol*s)'), n=2.1006, w0=(285000,'J/mol'), E0=(30324.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 292,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_4CClF->C",
    kinetics = ArrheniusBM(A=(0.00702378,'m^3/(mol*s)'), n=2.21204, w0=(285000,'J/mol'), E0=(42046.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=9.86779071375884e-06, var=23.58170199429774, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_4CClF->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_4CClF->C
    Total Standard Deviation in ln(k): 9.735217726183082"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_4CClF->C
Total Standard Deviation in ln(k): 9.735217726183082""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_4CClF->C
Total Standard Deviation in ln(k): 9.735217726183082
""",
)

entry(
    index = 293,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_N-4CClF->C",
    kinetics = ArrheniusBM(A=(0.000139659,'m^3/(mol*s)'), n=2.9821, w0=(285000,'J/mol'), E0=(39718.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_N-4CClF->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_N-4CClF->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_N-4CClF->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_N-4CClF->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 294,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R_Ext-4C-R_7R!H->Cl",
    kinetics = ArrheniusBM(A=(1.87452e-05,'m^3/(mol*s)'), n=3.32701, w0=(285000,'J/mol'), E0=(37930.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R_Ext-4C-R_7R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R_Ext-4C-R_7R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R_Ext-4C-R_7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R_Ext-4C-R_7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 295,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R_Ext-4C-R_N-7R!H->Cl",
    kinetics = ArrheniusBM(A=(0.000212992,'m^3/(mol*s)'), n=2.83406, w0=(285000,'J/mol'), E0=(40536.1,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R_Ext-4C-R_N-7R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R_Ext-4C-R_N-7R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R_Ext-4C-R_N-7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_4CFO->C_Ext-1C-R_Ext-1C-R_Ext-4C-R_N-7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 296,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_N-Sp-5C=1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.072651,'m^3/(mol*s)'), n=1.9038, w0=(285000,'J/mol'), E0=(39928.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00023943045587580702, var=32.85180916654862, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_N-Sp-5C=1C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_N-Sp-5C=1C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.491040943413894"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_N-Sp-5C=1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.491040943413894""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_N-Sp-5C=1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.491040943413894
""",
)

entry(
    index = 297,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br_7CClFINOPSSi->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.000586117,'m^3/(mol*s)'), n=3.12075, w0=(285000,'J/mol'), E0=(38966.7,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br_7CClFINOPSSi->Cl_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br_7CClFINOPSSi->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br_7CClFINOPSSi->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br_7CClFINOPSSi->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 298,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br_N-7CClFINOPSSi->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.47957e+08,'m^3/(mol*s)'), n=-0.551496, w0=(285000,'J/mol'), E0=(50497.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br_N-7CClFINOPSSi->Cl_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br_N-7CClFINOPSSi->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br_N-7CClFINOPSSi->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_Ext-6R!H-R_N-7R!H->Br_N-7CClFINOPSSi->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 299,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.000108817,'m^3/(mol*s)'), n=3.14996, w0=(285000,'J/mol'), E0=(37743.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0001416082260973505, var=0.7037461277521883, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 1.6821195936774374"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 1.6821195936774374""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 1.6821195936774374
""",
)

entry(
    index = 300,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_4CClF->C",
    kinetics = ArrheniusBM(A=(2.90405e-05,'m^3/(mol*s)'), n=2.92564, w0=(285000,'J/mol'), E0=(35175,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_4CClF->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_4CClF->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_4CClF->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_4CClF->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 301,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_N-4CClF->C",
    kinetics = ArrheniusBM(A=(0.00488192,'m^3/(mol*s)'), n=2.35051, w0=(285000,'J/mol'), E0=(40003.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_N-4CClF->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_N-4CClF->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_N-4CClF->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_N-4CClF->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 302,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_4CClF->C_Ext-4C-R_7R!H->Cl",
    kinetics = ArrheniusBM(A=(6.12147e-07,'m^3/(mol*s)'), n=3.64776, w0=(285000,'J/mol'), E0=(32701.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_4CClF->C_Ext-4C-R_7R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_4CClF->C_Ext-4C-R_7R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_4CClF->C_Ext-4C-R_7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_4CClF->C_Ext-4C-R_7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 303,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_4CClF->C_Ext-4C-R_N-7R!H->Cl",
    kinetics = ArrheniusBM(A=(2.44738e-05,'m^3/(mol*s)'), n=2.61697, w0=(285000,'J/mol'), E0=(32715.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_4CClF->C_Ext-4C-R_N-7R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_4CClF->C_Ext-4C-R_N-7R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_4CClF->C_Ext-4C-R_N-7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_4CClF->C_Ext-4C-R_N-7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 304,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_N-Sp-5C=1C_Ext-1C-R_Ext-5C-R_7R!H->Cl",
    kinetics = ArrheniusBM(A=(0.000536535,'m^3/(mol*s)'), n=2.88999, w0=(285000,'J/mol'), E0=(39281.2,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_N-Sp-5C=1C_Ext-1C-R_Ext-5C-R_7R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_N-Sp-5C=1C_Ext-1C-R_Ext-5C-R_7R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_N-Sp-5C=1C_Ext-1C-R_Ext-5C-R_7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_N-Sp-5C=1C_Ext-1C-R_Ext-5C-R_7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 305,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_N-Sp-5C=1C_Ext-1C-R_Ext-5C-R_N-7R!H->Cl",
    kinetics = ArrheniusBM(A=(0.00816439,'m^3/(mol*s)'), n=1.90059, w0=(285000,'J/mol'), E0=(38785.3,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_N-Sp-5C=1C_Ext-1C-R_Ext-5C-R_N-7R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_N-Sp-5C=1C_Ext-1C-R_Ext-5C-R_N-7R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_N-Sp-5C=1C_Ext-1C-R_Ext-5C-R_N-7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_N-4CClFO->Cl_N-4CFO->C_Ext-1C-R_5R!H->C_N-Sp-5C=1C_Ext-1C-R_Ext-5C-R_N-7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 306,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_9R!H->Cl",
    kinetics = ArrheniusBM(A=(0.00179019,'m^3/(mol*s)'), n=2.84887, w0=(285000,'J/mol'), E0=(41260.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_9R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_9R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_9R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_9R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 307,
    label = "Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_N-9R!H->Cl",
    kinetics = ArrheniusBM(A=(0.00375254,'m^3/(mol*s)'), n=2.67203, w0=(285000,'J/mol'), E0=(42197.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_N-9R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_N-9R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_N-9R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-3R->H_1BrCClFINOPSSi->C_3BrCClO-u1_3BrCClO->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->Br_Ext-3C-R_N-4CClFO->O_Ext-1C-R_N-6R!H->Br_N-Sp-6CCFF=1C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R_N-9R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

