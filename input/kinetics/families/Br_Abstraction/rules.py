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
    kinetics = ArrheniusBM(A=(1.62083e-10,'m^3/(mol*s)'), n=4.88687, w0=(281984,'J/mol'), E0=(5398.72,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2046846484373866, var=30.8158985087252, Tref=1000.0, N=149, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 149 training reactions at node Root
    Total Standard Deviation in ln(k): 11.642982314020609"""),
    rank = 11,
    shortDesc = """BM rule fitted to 149 training reactions at node Root
Total Standard Deviation in ln(k): 11.642982314020609""",
    longDesc = 
"""
BM rule fitted to 149 training reactions at node Root
Total Standard Deviation in ln(k): 11.642982314020609
""",
)

entry(
    index = 2,
    label = "Root_1R->H",
    kinetics = ArrheniusBM(A=(370.912,'m^3/(mol*s)'), n=1.27907, w0=(316562,'J/mol'), E0=(72206.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.627031681764817, var=29.954570791063006, Tref=1000.0, N=26, data_mean=0.0, correlation='Root_1R->H',), comment="""BM rule fitted to 26 training reactions at node Root_1R->H
    Total Standard Deviation in ln(k): 12.547525736465438"""),
    rank = 11,
    shortDesc = """BM rule fitted to 26 training reactions at node Root_1R->H
Total Standard Deviation in ln(k): 12.547525736465438""",
    longDesc = 
"""
BM rule fitted to 26 training reactions at node Root_1R->H
Total Standard Deviation in ln(k): 12.547525736465438
""",
)

entry(
    index = 3,
    label = "Root_N-1R->H",
    kinetics = ArrheniusBM(A=(4.54044e-09,'m^3/(mol*s)'), n=4.44183, w0=(274675,'J/mol'), E0=(6451.98,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1805632642095759, var=33.95876340124483, Tref=1000.0, N=123, data_mean=0.0, correlation='Root_N-1R->H',), comment="""BM rule fitted to 123 training reactions at node Root_N-1R->H
    Total Standard Deviation in ln(k): 12.136099429124762"""),
    rank = 11,
    shortDesc = """BM rule fitted to 123 training reactions at node Root_N-1R->H
Total Standard Deviation in ln(k): 12.136099429124762""",
    longDesc = 
"""
BM rule fitted to 123 training reactions at node Root_N-1R->H
Total Standard Deviation in ln(k): 12.136099429124762
""",
)

entry(
    index = 4,
    label = "Root_1R->H_3R-u1",
    kinetics = ArrheniusBM(A=(2.43865e+17,'m^3/(mol*s)'), n=-3.13378, w0=(315728,'J/mol'), E0=(114668,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.23498972977277127, var=25.897550452912885, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_1R->H_3R-u1',), comment="""BM rule fitted to 20 training reactions at node Root_1R->H_3R-u1
    Total Standard Deviation in ln(k): 10.792450279584811"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_1R->H_3R-u1
Total Standard Deviation in ln(k): 10.792450279584811""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_1R->H_3R-u1
Total Standard Deviation in ln(k): 10.792450279584811
""",
)

entry(
    index = 5,
    label = "Root_1R->H_N-3R-u1",
    kinetics = ArrheniusBM(A=(0.136512,'m^3/(mol*s)'), n=2.33444, w0=(319342,'J/mol'), E0=(37903,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.013438175404486552, var=1.9935749867617472, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R->H_N-3R-u1',), comment="""BM rule fitted to 6 training reactions at node Root_1R->H_N-3R-u1
    Total Standard Deviation in ln(k): 2.86433020539804"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R->H_N-3R-u1
Total Standard Deviation in ln(k): 2.86433020539804""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R->H_N-3R-u1
Total Standard Deviation in ln(k): 2.86433020539804
""",
)

entry(
    index = 6,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(2.57726e-07,'m^3/(mol*s)'), n=3.96484, w0=(286593,'J/mol'), E0=(26472.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.13403332517388938, var=21.81911502000373, Tref=1000.0, N=85, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C',), comment="""BM rule fitted to 85 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 9.701072252562742"""),
    rank = 11,
    shortDesc = """BM rule fitted to 85 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 9.701072252562742""",
    longDesc = 
"""
BM rule fitted to 85 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 9.701072252562742
""",
)

entry(
    index = 7,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(4.41609e-10,'m^3/(mol*s)'), n=4.58065, w0=(248017,'J/mol'), E0=(-19421.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.5770164595475216, var=72.00120071959894, Tref=1000.0, N=38, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C',), comment="""BM rule fitted to 38 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 20.973235966522893"""),
    rank = 11,
    shortDesc = """BM rule fitted to 38 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 20.973235966522893""",
    longDesc = 
"""
BM rule fitted to 38 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 20.973235966522893
""",
)

entry(
    index = 8,
    label = "Root_1R->H_3R-u1_3R->O",
    kinetics = ArrheniusBM(A=(0.028327,'m^3/(mol*s)'), n=2.84123, w0=(298550,'J/mol'), E0=(29855,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.060564280426098765, var=3.1193288635452796, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_3R-u1_3R->O',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_3R-u1_3R->O
    Total Standard Deviation in ln(k): 3.6928588433946965"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_3R-u1_3R->O
Total Standard Deviation in ln(k): 3.6928588433946965""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_3R-u1_3R->O
Total Standard Deviation in ln(k): 3.6928588433946965
""",
)

entry(
    index = 9,
    label = "Root_1R->H_3R-u1_N-3R->O",
    kinetics = ArrheniusBM(A=(3.23097e+06,'m^3/(mol*s)'), n=0.0227834, w0=(318760,'J/mol'), E0=(90213.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.16468898595063702, var=34.6310908780265, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_1R->H_3R-u1_N-3R->O',), comment="""BM rule fitted to 17 training reactions at node Root_1R->H_3R-u1_N-3R->O
    Total Standard Deviation in ln(k): 12.211293850744084"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_1R->H_3R-u1_N-3R->O
Total Standard Deviation in ln(k): 12.211293850744084""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_1R->H_3R-u1_N-3R->O
Total Standard Deviation in ln(k): 12.211293850744084
""",
)

entry(
    index = 10,
    label = "Root_1R->H_N-3R-u1_3R->C",
    kinetics = ArrheniusBM(A=(0.251209,'m^3/(mol*s)'), n=2.25649, w0=(323500,'J/mol'), E0=(38488.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.006688757734172009, var=2.0051322091049806, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->H_N-3R-u1_3R->C',), comment="""BM rule fitted to 5 training reactions at node Root_1R->H_N-3R-u1_3R->C
    Total Standard Deviation in ln(k): 2.855564740442996"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->H_N-3R-u1_3R->C
Total Standard Deviation in ln(k): 2.855564740442996""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->H_N-3R-u1_3R->C
Total Standard Deviation in ln(k): 2.855564740442996
""",
)

entry(
    index = 11,
    label = "Root_1R->H_N-3R-u1_N-3R->C",
    kinetics = ArrheniusBM(A=(4375.31,'m^3/(mol*s)'), n=0.580548, w0=(298550,'J/mol'), E0=(29855,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R-u1_N-3R->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R-u1_N-3R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R-u1_N-3R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R-u1_N-3R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_3R->Cl",
    kinetics = ArrheniusBM(A=(1.16655e-12,'m^3/(mol*s)'), n=3.89159, w0=(251920,'J/mol'), E0=(-85024.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.18926981139848992, var=1200.4840418456631, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_3R->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->Cl
    Total Standard Deviation in ln(k): 69.9356172393764"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->Cl
Total Standard Deviation in ln(k): 69.9356172393764""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->Cl
Total Standard Deviation in ln(k): 69.9356172393764
""",
)

entry(
    index = 13,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl",
    kinetics = ArrheniusBM(A=(0.00111807,'m^3/(mol*s)'), n=2.94985, w0=(287428,'J/mol'), E0=(35245.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06736919256719999, var=10.632525485546847, Tref=1000.0, N=83, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl',), comment="""BM rule fitted to 83 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl
    Total Standard Deviation in ln(k): 6.706219967146111"""),
    rank = 11,
    shortDesc = """BM rule fitted to 83 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl
Total Standard Deviation in ln(k): 6.706219967146111""",
    longDesc = 
"""
BM rule fitted to 83 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl
Total Standard Deviation in ln(k): 6.706219967146111
""",
)

entry(
    index = 14,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl",
    kinetics = ArrheniusBM(A=(0.0303934,'m^3/(mol*s)'), n=1.92891, w0=(242103,'J/mol'), E0=(-6903.08,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.15368815656203197, var=231.13323810370105, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl
    Total Standard Deviation in ln(k): 30.86427231178154"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl
Total Standard Deviation in ln(k): 30.86427231178154""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl
Total Standard Deviation in ln(k): 30.86427231178154
""",
)

entry(
    index = 15,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl",
    kinetics = ArrheniusBM(A=(0.0127013,'m^3/(mol*s)'), n=2.59583, w0=(249125,'J/mol'), E0=(-10781.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.9008243832826895, var=23.052162321303825, Tref=1000.0, N=32, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl',), comment="""BM rule fitted to 32 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl
    Total Standard Deviation in ln(k): 11.888645699693612"""),
    rank = 11,
    shortDesc = """BM rule fitted to 32 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl
Total Standard Deviation in ln(k): 11.888645699693612""",
    longDesc = 
"""
BM rule fitted to 32 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl
Total Standard Deviation in ln(k): 11.888645699693612
""",
)

entry(
    index = 16,
    label = "Root_1R->H_3R-u1_3R->O_Ext-3O-R",
    kinetics = ArrheniusBM(A=(0.02722,'m^3/(mol*s)'), n=2.84724, w0=(298550,'J/mol'), E0=(29855,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.2325603151022477, var=5.2097791213440425, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_3R-u1_3R->O_Ext-3O-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_3R-u1_3R->O_Ext-3O-R
    Total Standard Deviation in ln(k): 7.672681114320994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_3R-u1_3R->O_Ext-3O-R
Total Standard Deviation in ln(k): 7.672681114320994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_3R-u1_3R->O_Ext-3O-R
Total Standard Deviation in ln(k): 7.672681114320994
""",
)

entry(
    index = 17,
    label = "Root_1R->H_3R-u1_N-3R->O_3BrCCl->C",
    kinetics = ArrheniusBM(A=(9.30105e-23,'m^3/(mol*s)'), n=8.47975, w0=(323500,'J/mol'), E0=(-10613,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.7175371536862905, var=66.12259798877442, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_1R->H_3R-u1_N-3R->O_3BrCCl->C',), comment="""BM rule fitted to 15 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C
    Total Standard Deviation in ln(k): 20.61708422319487"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C
Total Standard Deviation in ln(k): 20.61708422319487""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C
Total Standard Deviation in ln(k): 20.61708422319487
""",
)

entry(
    index = 18,
    label = "Root_1R->H_3R-u1_N-3R->O_N-3BrCCl->C",
    kinetics = ArrheniusBM(A=(63024,'m^3/(mol*s)'), n=0.872381, w0=(283210,'J/mol'), E0=(28321,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.30046023529256427, var=0.05582180620399102, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_3R-u1_N-3R->O_N-3BrCCl->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_3R-u1_N-3R->O_N-3BrCCl->C
    Total Standard Deviation in ln(k): 1.2285767303830044"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_3R-u1_N-3R->O_N-3BrCCl->C
Total Standard Deviation in ln(k): 1.2285767303830044""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_3R-u1_N-3R->O_N-3BrCCl->C
Total Standard Deviation in ln(k): 1.2285767303830044
""",
)

entry(
    index = 19,
    label = "Root_1R->H_N-3R-u1_3R->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.63424,'m^3/(mol*s)'), n=1.95806, w0=(323500,'J/mol'), E0=(38998.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.007086042747752114, var=2.859741556579387, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-3R-u1_3R->C_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-3R-u1_3R->C_Ext-3C-R
    Total Standard Deviation in ln(k): 3.407965588979388"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-3R-u1_3R->C_Ext-3C-R
Total Standard Deviation in ln(k): 3.407965588979388""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-3R-u1_3R->C_Ext-3C-R
Total Standard Deviation in ln(k): 3.407965588979388
""",
)

entry(
    index = 20,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_3R->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(8.1e+07,'m^3/(mol*s)'), n=0, w0=(251920,'J/mol'), E0=(79217.1,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_3R->Cl_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H",
    kinetics = ArrheniusBM(A=(1.12302e-14,'m^3/(mol*s)'), n=6.51327, w0=(323500,'J/mol'), E0=(-2598.84,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.0684765916653363, var=26.6946233386778, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H',), comment="""BM rule fitted to 21 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H
    Total Standard Deviation in ln(k): 15.555009972470472"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H
Total Standard Deviation in ln(k): 15.555009972470472""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H
Total Standard Deviation in ln(k): 15.555009972470472
""",
)

entry(
    index = 22,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H",
    kinetics = ArrheniusBM(A=(3.03987e+08,'m^3/(mol*s)'), n=-0.541098, w0=(275210,'J/mol'), E0=(55938.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.11492915567471972, var=8.492339961185106, Tref=1000.0, N=62, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H',), comment="""BM rule fitted to 62 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H
    Total Standard Deviation in ln(k): 6.130889436252776"""),
    rank = 11,
    shortDesc = """BM rule fitted to 62 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H
Total Standard Deviation in ln(k): 6.130889436252776""",
    longDesc = 
"""
BM rule fitted to 62 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H
Total Standard Deviation in ln(k): 6.130889436252776
""",
)

entry(
    index = 23,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl_3R->C",
    kinetics = ArrheniusBM(A=(6.33499e-50,'m^3/(mol*s)'), n=14.6717, w0=(251920,'J/mol'), E0=(-178924,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1814422429167134, var=1133.0604159007603, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl_3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl_3R->C
    Total Standard Deviation in ln(k): 67.9371978749665"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl_3R->C
Total Standard Deviation in ln(k): 67.9371978749665""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl_3R->C
Total Standard Deviation in ln(k): 67.9371978749665
""",
)

entry(
    index = 24,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl_N-3R->C",
    kinetics = ArrheniusBM(A=(2.32048e+10,'m^3/(mol*s)'), n=-0.867719, w0=(237195,'J/mol'), E0=(14623.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.5060170488424585, var=7.128157331514332, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl_N-3R->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl_N-3R->C
    Total Standard Deviation in ln(k): 6.623763458058837"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl_N-3R->C
Total Standard Deviation in ln(k): 6.623763458058837""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl_N-3R->C
Total Standard Deviation in ln(k): 6.623763458058837
""",
)

entry(
    index = 25,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R",
    kinetics = ArrheniusBM(A=(1.59574e-31,'m^3/(mol*s)'), n=10.908, w0=(251996,'J/mol'), E0=(-32673.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.1157716702282117, var=31.913883992944683, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R',), comment="""BM rule fitted to 14 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R
    Total Standard Deviation in ln(k): 19.153796552474986"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R
Total Standard Deviation in ln(k): 19.153796552474986""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R
Total Standard Deviation in ln(k): 19.153796552474986
""",
)

entry(
    index = 26,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0",
    kinetics = ArrheniusBM(A=(1.02508e+08,'m^3/(mol*s)'), n=0.00321688, w0=(246988,'J/mol'), E0=(12557,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0940725145039093, var=2.674863615592639, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0
    Total Standard Deviation in ln(k): 3.5151093835552203"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0
Total Standard Deviation in ln(k): 3.5151093835552203""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0
Total Standard Deviation in ln(k): 3.5151093835552203
""",
)

entry(
    index = 27,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0",
    kinetics = ArrheniusBM(A=(1.16416e+07,'m^3/(mol*s)'), n=0.0508927, w0=(246644,'J/mol'), E0=(2678.94,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04396557513634543, var=0.06978821169239435, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0
    Total Standard Deviation in ln(k): 0.6400663275538472"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0
Total Standard Deviation in ln(k): 0.6400663275538472""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0
Total Standard Deviation in ln(k): 0.6400663275538472
""",
)

entry(
    index = 28,
    label = "Root_1R->H_3R-u1_3R->O_Ext-3O-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(0.00532831,'m^3/(mol*s)'), n=2.77064, w0=(298550,'J/mol'), E0=(29855,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R-u1_3R->O_Ext-3O-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_3R->O_Ext-3O-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_3R->O_Ext-3O-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_3R->O_Ext-3O-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 29,
    label = "Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(7.22363e-24,'m^3/(mol*s)'), n=8.78967, w0=(323500,'J/mol'), E0=(-6317.39,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.194632642615857, var=30.25896264065602, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R',), comment="""BM rule fitted to 13 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R
    Total Standard Deviation in ln(k): 19.054391416248"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R
Total Standard Deviation in ln(k): 19.054391416248""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R
Total Standard Deviation in ln(k): 19.054391416248
""",
)

entry(
    index = 30,
    label = "Root_1R->H_3R-u1_N-3R->O_N-3BrCCl->C_3BrCl->Br",
    kinetics = ArrheniusBM(A=(32771.6,'m^3/(mol*s)'), n=1.02226, w0=(276000,'J/mol'), E0=(27600,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R-u1_N-3R->O_N-3BrCCl->C_3BrCl->Br',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_N-3R->O_N-3BrCCl->C_3BrCl->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_N-3R->O_N-3BrCCl->C_3BrCl->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_N-3R->O_N-3BrCCl->C_3BrCl->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "Root_1R->H_3R-u1_N-3R->O_N-3BrCCl->C_N-3BrCl->Br",
    kinetics = ArrheniusBM(A=(1.87868e+08,'m^3/(mol*s)'), n=-0.210299, w0=(290420,'J/mol'), E0=(29042,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R-u1_N-3R->O_N-3BrCCl->C_N-3BrCl->Br',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_N-3R->O_N-3BrCCl->C_N-3BrCl->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_N-3R->O_N-3BrCCl->C_N-3BrCl->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_N-3R->O_N-3BrCCl->C_N-3BrCl->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 32,
    label = "Root_1R->H_N-3R-u1_3R->C_Ext-3C-R_Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(8.45714e-05,'m^3/(mol*s)'), n=3.29977, w0=(323500,'J/mol'), E0=(34787.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0014948508078482965, var=10.208671995990533, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-3R-u1_3R->C_Ext-3C-R_Sp-4R!H-3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-3R-u1_3R->C_Ext-3C-R_Sp-4R!H-3C
    Total Standard Deviation in ln(k): 6.409087457700756"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-3R-u1_3R->C_Ext-3C-R_Sp-4R!H-3C
Total Standard Deviation in ln(k): 6.409087457700756""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-3R-u1_3R->C_Ext-3C-R_Sp-4R!H-3C
Total Standard Deviation in ln(k): 6.409087457700756
""",
)

entry(
    index = 33,
    label = "Root_1R->H_N-3R-u1_3R->C_Ext-3C-R_N-Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(0.416835,'m^3/(mol*s)'), n=1.92612, w0=(323500,'J/mol'), E0=(22788.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R-u1_3R->C_Ext-3C-R_N-Sp-4R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R-u1_3R->C_Ext-3C-R_N-Sp-4R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R-u1_3R->C_Ext-3C-R_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R-u1_3R->C_Ext-3C-R_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.42906e-15,'m^3/(mol*s)'), n=6.66501, w0=(323500,'J/mol'), E0=(-4889.15,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.883360245752303, var=9.880092780747576, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R',), comment="""BM rule fitted to 17 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R
    Total Standard Deviation in ln(k): 8.52090466693944"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R
Total Standard Deviation in ln(k): 8.52090466693944""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R
Total Standard Deviation in ln(k): 8.52090466693944
""",
)

entry(
    index = 35,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_1C-u0",
    kinetics = ArrheniusBM(A=(1110.39,'m^3/(mol*s)'), n=1.58156, w0=(323500,'J/mol'), E0=(52438,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4168931069501357, var=0.35476654140791564, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_1C-u0',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_1C-u0
    Total Standard Deviation in ln(k): 2.2415360742502544"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_1C-u0
Total Standard Deviation in ln(k): 2.2415360742502544""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_1C-u0
Total Standard Deviation in ln(k): 2.2415360742502544
""",
)

entry(
    index = 36,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_N-1C-u0",
    kinetics = ArrheniusBM(A=(159.46,'m^3/(mol*s)'), n=1.56503, w0=(323500,'J/mol'), E0=(41594.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.552499098455533, var=13.299166400648918, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_N-1C-u0',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_N-1C-u0
    Total Standard Deviation in ln(k): 13.724186639918862"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_N-1C-u0
Total Standard Deviation in ln(k): 13.724186639918862""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_N-1C-u0
Total Standard Deviation in ln(k): 13.724186639918862
""",
)

entry(
    index = 37,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R",
    kinetics = ArrheniusBM(A=(1.66392e-12,'m^3/(mol*s)'), n=5.40354, w0=(284168,'J/mol'), E0=(16815.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.08354419882058846, var=6.981268357275188, Tref=1000.0, N=30, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R',), comment="""BM rule fitted to 30 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R
    Total Standard Deviation in ln(k): 5.506839095307012"""),
    rank = 11,
    shortDesc = """BM rule fitted to 30 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R
Total Standard Deviation in ln(k): 5.506839095307012""",
    longDesc = 
"""
BM rule fitted to 30 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R
Total Standard Deviation in ln(k): 5.506839095307012
""",
)

entry(
    index = 38,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br",
    kinetics = ArrheniusBM(A=(3.84511e+10,'m^3/(mol*s)'), n=-0.881741, w0=(237500,'J/mol'), E0=(46500.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07951122150648926, var=23.038298704781962, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br
    Total Standard Deviation in ln(k): 9.82215002774575"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br
Total Standard Deviation in ln(k): 9.82215002774575""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br
Total Standard Deviation in ln(k): 9.82215002774575
""",
)

entry(
    index = 39,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br",
    kinetics = ArrheniusBM(A=(8.64218e+20,'m^3/(mol*s)'), n=-4.20011, w0=(275020,'J/mol'), E0=(76215,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.3341007843870509, var=8.007251946077336, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br',), comment="""BM rule fitted to 25 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br
    Total Standard Deviation in ln(k): 6.512265716046835"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br
Total Standard Deviation in ln(k): 6.512265716046835""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br
Total Standard Deviation in ln(k): 6.512265716046835
""",
)

entry(
    index = 40,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl_3R->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(247.456,'m^3/(mol*s)'), n=1.14962, w0=(251920,'J/mol'), E0=(69327.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl_3R->C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl_3R->C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl_3R->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl_3R->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl_N-3R->C_3BrClHO->O",
    kinetics = ArrheniusBM(A=(1.87879e+11,'m^3/(mol*s)'), n=-1.38743, w0=(226970,'J/mol'), E0=(11162.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4276526398966118, var=9.741433979709994, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl_N-3R->C_3BrClHO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl_N-3R->C_3BrClHO->O
    Total Standard Deviation in ln(k): 7.331536971976397"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl_N-3R->C_3BrClHO->O
Total Standard Deviation in ln(k): 7.331536971976397""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl_N-3R->C_3BrClHO->O
Total Standard Deviation in ln(k): 7.331536971976397
""",
)

entry(
    index = 42,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl_N-3R->C_N-3BrClHO->O",
    kinetics = ArrheniusBM(A=(3.23525e+06,'m^3/(mol*s)'), n=0.526301, w0=(247420,'J/mol'), E0=(-5212.67,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.744614264300018, var=15.609515254169375, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl_N-3R->C_N-3BrClHO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl_N-3R->C_N-3BrClHO->O
    Total Standard Deviation in ln(k): 9.791373685446224"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl_N-3R->C_N-3BrClHO->O
Total Standard Deviation in ln(k): 9.791373685446224""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl_N-3R->C_N-3BrClHO->O
Total Standard Deviation in ln(k): 9.791373685446224
""",
)

entry(
    index = 43,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-1BrO-R",
    kinetics = ArrheniusBM(A=(0.0113539,'m^3/(mol*s)'), n=2.68093, w0=(260050,'J/mol'), E0=(26005,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-1BrO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-1BrO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-1BrO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-1BrO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 44,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R",
    kinetics = ArrheniusBM(A=(44868.6,'m^3/(mol*s)'), n=0.284662, w0=(251594,'J/mol'), E0=(29258.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.02250601402637283, var=3.366426498412813, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R
    Total Standard Deviation in ln(k): 3.7348004341269587"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R
Total Standard Deviation in ln(k): 3.7348004341269587""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R
Total Standard Deviation in ln(k): 3.7348004341269587
""",
)

entry(
    index = 45,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_1BrO-u0",
    kinetics = ArrheniusBM(A=(3.0425e+11,'m^3/(mol*s)'), n=-1.48571, w0=(248775,'J/mol'), E0=(-544.045,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0947089065041228, var=1.4474141053851577, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_1BrO-u0',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_1BrO-u0
    Total Standard Deviation in ln(k): 2.649829267264275"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_1BrO-u0
Total Standard Deviation in ln(k): 2.649829267264275""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_1BrO-u0
Total Standard Deviation in ln(k): 2.649829267264275
""",
)

entry(
    index = 46,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_N-1BrO-u0",
    kinetics = ArrheniusBM(A=(811294,'m^3/(mol*s)'), n=-0.0332179, w0=(260050,'J/mol'), E0=(14584.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_N-1BrO-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_N-1BrO-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_N-1BrO-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_N-1BrO-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 47,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_3R->Br",
    kinetics = ArrheniusBM(A=(1.62623e+09,'m^3/(mol*s)'), n=-0.659413, w0=(212550,'J/mol'), E0=(4542.98,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_3R->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_3R->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_3R->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_3R->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 48,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br",
    kinetics = ArrheniusBM(A=(1.00976e+08,'m^3/(mol*s)'), n=0.00547275, w0=(249858,'J/mol'), E0=(12548,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.09461843689313316, var=2.680183054915517, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br
    Total Standard Deviation in ln(k): 3.519739611994286"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br
Total Standard Deviation in ln(k): 3.519739611994286""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br
Total Standard Deviation in ln(k): 3.519739611994286
""",
)

entry(
    index = 49,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0_3R->Br",
    kinetics = ArrheniusBM(A=(3.48226e+08,'m^3/(mol*s)'), n=-0.558288, w0=(212550,'J/mol'), E0=(13124.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0_3R->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0_3R->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0_3R->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0_3R->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 50,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0_N-3R->Br",
    kinetics = ArrheniusBM(A=(1.16463e+07,'m^3/(mol*s)'), n=0.051631, w0=(255168,'J/mol'), E0=(3211.48,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0415163123607323, var=0.0650123273127719, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0_N-3R->Br',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0_N-3R->Br
    Total Standard Deviation in ln(k): 0.6154699704513077"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0_N-3R->Br
Total Standard Deviation in ln(k): 0.6154699704513077""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0_N-3R->Br
Total Standard Deviation in ln(k): 0.6154699704513077
""",
)

entry(
    index = 51,
    label = "Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F",
    kinetics = ArrheniusBM(A=(3.52722e-33,'m^3/(mol*s)'), n=11.5707, w0=(323500,'J/mol'), E0=(-9682.49,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.955563821134698, var=113.88784796956026, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F',), comment="""BM rule fitted to 6 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F
    Total Standard Deviation in ln(k): 26.307658773959194"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F
Total Standard Deviation in ln(k): 26.307658773959194""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F
Total Standard Deviation in ln(k): 26.307658773959194
""",
)

entry(
    index = 52,
    label = "Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_N-4R!H->F",
    kinetics = ArrheniusBM(A=(6.77187e-13,'m^3/(mol*s)'), n=5.53548, w0=(323500,'J/mol'), E0=(19543.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06570589444219498, var=4.065238852118525, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_N-4R!H->F',), comment="""BM rule fitted to 7 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_N-4R!H->F
    Total Standard Deviation in ln(k): 4.207124753615432"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_N-4R!H->F
Total Standard Deviation in ln(k): 4.207124753615432""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_N-4R!H->F
Total Standard Deviation in ln(k): 4.207124753615432
""",
)

entry(
    index = 53,
    label = "Root_1R->H_N-3R-u1_3R->C_Ext-3C-R_Sp-4R!H-3C_4R!H->C",
    kinetics = ArrheniusBM(A=(0.279393,'m^3/(mol*s)'), n=2.26429, w0=(323500,'J/mol'), E0=(32680.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R-u1_3R->C_Ext-3C-R_Sp-4R!H-3C_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R-u1_3R->C_Ext-3C-R_Sp-4R!H-3C_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R-u1_3R->C_Ext-3C-R_Sp-4R!H-3C_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R-u1_3R->C_Ext-3C-R_Sp-4R!H-3C_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 54,
    label = "Root_1R->H_N-3R-u1_3R->C_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.00111222,'m^3/(mol*s)'), n=2.71464, w0=(323500,'J/mol'), E0=(31265.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R-u1_3R->C_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R-u1_3R->C_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R-u1_3R->C_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R-u1_3R->C_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 55,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2.43186e-30,'m^3/(mol*s)'), n=11.2397, w0=(323500,'J/mol'), E0=(557.815,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.281322578745599, var=90.0391364085781, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_Ext-4R!H-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 24.754687784800655"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 24.754687784800655""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 24.754687784800655
""",
)

entry(
    index = 56,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0",
    kinetics = ArrheniusBM(A=(2.79651e-09,'m^3/(mol*s)'), n=4.95392, w0=(323500,'J/mol'), E0=(-3420.09,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.22172477219175732, var=1.7420402621503253, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0
    Total Standard Deviation in ln(k): 3.2030745317299054"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0
Total Standard Deviation in ln(k): 3.2030745317299054""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0
Total Standard Deviation in ln(k): 3.2030745317299054
""",
)

entry(
    index = 57,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_N-1C-u0",
    kinetics = ArrheniusBM(A=(3.98282e-06,'m^3/(mol*s)'), n=3.84125, w0=(323500,'J/mol'), E0=(13658.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2779741605534091, var=1.8474209462856896, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_N-1C-u0',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_N-1C-u0
    Total Standard Deviation in ln(k): 3.4232607322727504"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_N-1C-u0
Total Standard Deviation in ln(k): 3.4232607322727504""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_N-1C-u0
Total Standard Deviation in ln(k): 3.4232607322727504
""",
)

entry(
    index = 58,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C",
    kinetics = ArrheniusBM(A=(557.264,'m^3/(mol*s)'), n=1.08139, w0=(285000,'J/mol'), E0=(46037,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.007248054526332242, var=6.403181854720068, Tref=1000.0, N=29, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C',), comment="""BM rule fitted to 29 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C
    Total Standard Deviation in ln(k): 5.091094911716732"""),
    rank = 11,
    shortDesc = """BM rule fitted to 29 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C
Total Standard Deviation in ln(k): 5.091094911716732""",
    longDesc = 
"""
BM rule fitted to 29 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C
Total Standard Deviation in ln(k): 5.091094911716732
""",
)

entry(
    index = 59,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_N-3BrCO->C",
    kinetics = ArrheniusBM(A=(0.000210828,'m^3/(mol*s)'), n=3.57193, w0=(260050,'J/mol'), E0=(26005,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_N-3BrCO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_N-3BrCO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_N-3BrCO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_N-3BrCO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 60,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_1C-u0",
    kinetics = ArrheniusBM(A=(4.0719e+08,'m^3/(mol*s)'), n=-0.297691, w0=(237500,'J/mol'), E0=(41761.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.030336428523838346, var=23.290722512570433, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_1C-u0',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_1C-u0
    Total Standard Deviation in ln(k): 9.751166406620165"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_1C-u0
Total Standard Deviation in ln(k): 9.751166406620165""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_1C-u0
Total Standard Deviation in ln(k): 9.751166406620165
""",
)

entry(
    index = 61,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_N-1C-u0",
    kinetics = ArrheniusBM(A=(5000,'m^3/(mol*s)'), n=0, w0=(237500,'J/mol'), E0=(23750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_N-1C-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_N-1C-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_N-1C-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_N-1C-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 62,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1",
    kinetics = ArrheniusBM(A=(1.86784e+21,'m^3/(mol*s)'), n=-4.28879, w0=(277871,'J/mol'), E0=(78771.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.3459339430771889, var=8.246120186725971, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1',), comment="""BM rule fitted to 21 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1
    Total Standard Deviation in ln(k): 6.6259897475586"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1
Total Standard Deviation in ln(k): 6.6259897475586""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1
Total Standard Deviation in ln(k): 6.6259897475586
""",
)

entry(
    index = 63,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_N-3CO-u1",
    kinetics = ArrheniusBM(A=(6.0325e+09,'m^3/(mol*s)'), n=-1.06022, w0=(260050,'J/mol'), E0=(25372,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.515121754479738, var=12.363742709402118, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_N-3CO-u1',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_N-3CO-u1
    Total Standard Deviation in ln(k): 13.368473754760297"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_N-3CO-u1
Total Standard Deviation in ln(k): 13.368473754760297""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_N-3CO-u1
Total Standard Deviation in ln(k): 13.368473754760297
""",
)

entry(
    index = 64,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl_N-3R->C_3BrClHO->O_3O-u1",
    kinetics = ArrheniusBM(A=(904000,'m^3/(mol*s)'), n=0, w0=(226970,'J/mol'), E0=(-1668.73,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl_N-3R->C_3BrClHO->O_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl_N-3R->C_3BrClHO->O_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl_N-3R->C_3BrClHO->O_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl_N-3R->C_3BrClHO->O_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 65,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl_N-3R->C_3BrClHO->O_N-3O-u1",
    kinetics = ArrheniusBM(A=(1.26e+07,'m^3/(mol*s)'), n=0, w0=(226970,'J/mol'), E0=(2816,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl_N-3R->C_3BrClHO->O_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl_N-3R->C_3BrClHO->O_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl_N-3R->C_3BrClHO->O_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl_N-3R->C_3BrClHO->O_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 66,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl_N-3R->C_N-3BrClHO->O_3BrH->Br",
    kinetics = ArrheniusBM(A=(3.7e+08,'m^3/(mol*s)'), n=0, w0=(204420,'J/mol'), E0=(8527.98,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl_N-3R->C_N-3BrClHO->O_3BrH->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl_N-3R->C_N-3BrClHO->O_3BrH->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl_N-3R->C_N-3BrClHO->O_3BrH->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl_N-3R->C_N-3BrClHO->O_3BrH->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 67,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl_N-3R->C_N-3BrClHO->O_N-3BrH->Br",
    kinetics = ArrheniusBM(A=(8.59e+07,'m^3/(mol*s)'), n=0, w0=(290420,'J/mol'), E0=(29042,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl_N-3R->C_N-3BrClHO->O_N-3BrH->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl_N-3R->C_N-3BrClHO->O_N-3BrH->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl_N-3R->C_N-3BrClHO->O_N-3BrH->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrClO->Cl_N-3R->C_N-3BrClHO->O_N-3BrH->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 68,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(0.522786,'m^3/(mol*s)'), n=1.72912, w0=(252533,'J/mol'), E0=(2155.08,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.422749766087777, var=19.80812332583467, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_4R!H->Cl',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_4R!H->Cl
    Total Standard Deviation in ln(k): 15.009648635074402"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_4R!H->Cl
Total Standard Deviation in ln(k): 15.009648635074402""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_4R!H->Cl
Total Standard Deviation in ln(k): 15.009648635074402
""",
)

entry(
    index = 69,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(3.04368e+15,'m^3/(mol*s)'), n=-2.9292, w0=(251030,'J/mol'), E0=(51907.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.10304073136485785, var=13.242450054606739, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_N-4R!H->Cl',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 7.554162804780947"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 7.554162804780947""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 7.554162804780947
""",
)

entry(
    index = 70,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_1BrO-u0_1BrO->Br",
    kinetics = ArrheniusBM(A=(6.14681e+08,'m^3/(mol*s)'), n=-0.527905, w0=(237500,'J/mol'), E0=(30474.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.35024040011199753, var=0.2620792632022212, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_1BrO-u0_1BrO->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_1BrO-u0_1BrO->Br
    Total Standard Deviation in ln(k): 1.9062986186992787"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_1BrO-u0_1BrO->Br
Total Standard Deviation in ln(k): 1.9062986186992787""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_1BrO-u0_1BrO->Br
Total Standard Deviation in ln(k): 1.9062986186992787
""",
)

entry(
    index = 71,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_1BrO-u0_N-1BrO->Br",
    kinetics = ArrheniusBM(A=(3.56665e+14,'m^3/(mol*s)'), n=-2.54977, w0=(260050,'J/mol'), E0=(-10277.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.620107419366252, var=8.027161994609964, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_1BrO-u0_N-1BrO->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_1BrO-u0_N-1BrO->Br
    Total Standard Deviation in ln(k): 12.26304933608979"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_1BrO-u0_N-1BrO->Br
Total Standard Deviation in ln(k): 12.26304933608979""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_1BrO-u0_N-1BrO->Br
Total Standard Deviation in ln(k): 12.26304933608979
""",
)

entry(
    index = 72,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_3CClHO->O",
    kinetics = ArrheniusBM(A=(1.32876e+06,'m^3/(mol*s)'), n=0.508568, w0=(220067,'J/mol'), E0=(3971.92,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.0671279395699083, var=9.73034019267967, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_3CClHO->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_3CClHO->O
    Total Standard Deviation in ln(k): 11.447257797353947"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_3CClHO->O
Total Standard Deviation in ln(k): 11.447257797353947""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_3CClHO->O
Total Standard Deviation in ln(k): 11.447257797353947
""",
)

entry(
    index = 73,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O",
    kinetics = ArrheniusBM(A=(4.98087e+07,'m^3/(mol*s)'), n=0.111651, w0=(259788,'J/mol'), E0=(12169.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1831029895412737, var=5.625127441800049, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O
    Total Standard Deviation in ln(k): 5.214758336109713"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O
Total Standard Deviation in ln(k): 5.214758336109713""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O
Total Standard Deviation in ln(k): 5.214758336109713
""",
)

entry(
    index = 74,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0_N-3R->Br_3CClHO->H",
    kinetics = ArrheniusBM(A=(1e+06,'m^3/(mol*s)'), n=0, w0=(298550,'J/mol'), E0=(29855,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0_N-3R->Br_3CClHO->H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0_N-3R->Br_3CClHO->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0_N-3R->Br_3CClHO->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0_N-3R->Br_3CClHO->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 75,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0_N-3R->Br_N-3CClHO->H",
    kinetics = ArrheniusBM(A=(1.18259e+07,'m^3/(mol*s)'), n=0.0506899, w0=(240707,'J/mol'), E0=(3315.05,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06193774761210188, var=0.021855931918031344, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0_N-3R->Br_N-3CClHO->H',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0_N-3R->Br_N-3CClHO->H
    Total Standard Deviation in ln(k): 0.4519975408126643"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0_N-3R->Br_N-3CClHO->H
Total Standard Deviation in ln(k): 0.4519975408126643""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0_N-3R->Br_N-3CClHO->H
Total Standard Deviation in ln(k): 0.4519975408126643
""",
)

entry(
    index = 76,
    label = "Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F_Ext-3C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(8183.69,'m^3/(mol*s)'), n=0.822108, w0=(323500,'J/mol'), E0=(168788,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00023163511234437686, var=2.0783412293122656, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F_Ext-3C-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F_Ext-3C-R_5R!H->C
    Total Standard Deviation in ln(k): 2.8906989403758696"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 2.8906989403758696""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 2.8906989403758696
""",
)

entry(
    index = 77,
    label = "Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F_Ext-3C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(4.57001e-16,'m^3/(mol*s)'), n=6.4701, w0=(323500,'J/mol'), E0=(4487.78,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4349417078002769, var=2.388906783740137, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F_Ext-3C-R_N-5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F_Ext-3C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 4.191354681987134"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 4.191354681987134""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 4.191354681987134
""",
)

entry(
    index = 78,
    label = "Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_N-4R!H->F_4BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(14.9548,'m^3/(mol*s)'), n=1.56664, w0=(323500,'J/mol'), E0=(53694.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0018218150470407654, var=4.059038505777299, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_N-4R!H->F_4BrCClINOPSSi->C',), comment="""BM rule fitted to 6 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_N-4R!H->F_4BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 4.043528337605101"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_N-4R!H->F_4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 4.043528337605101""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_N-4R!H->F_4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 4.043528337605101
""",
)

entry(
    index = 79,
    label = "Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_N-4R!H->F_N-4BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.0666301,'m^3/(mol*s)'), n=1.98796, w0=(323500,'J/mol'), E0=(49060.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_N-4R!H->F_N-4BrCClINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_N-4R!H->F_N-4BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_N-4R!H->F_N-4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_N-4R!H->F_N-4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 80,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_Ext-4R!H-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.77268e+08,'m^3/(mol*s)'), n=0.00925515, w0=(323500,'J/mol'), E0=(166790,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0269421956282239, var=1.9075430022643527, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_Ext-4R!H-R_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_Ext-4R!H-R_Ext-1C-R
    Total Standard Deviation in ln(k): 2.836510354545944"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_Ext-4R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 2.836510354545944""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_Ext-4R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 2.836510354545944
""",
)

entry(
    index = 81,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_Ext-4R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(650.121,'m^3/(mol*s)'), n=1.74726, w0=(323500,'J/mol'), E0=(50950.1,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_Ext-4R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_Ext-4R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 82,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_4R!H->Br",
    kinetics = ArrheniusBM(A=(7.9e+07,'m^3/(mol*s)'), n=0, w0=(323500,'J/mol'), E0=(82145.2,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_4R!H->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_4R!H->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_4R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_4R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 83,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_N-4R!H->Br",
    kinetics = ArrheniusBM(A=(1.28554e-08,'m^3/(mol*s)'), n=4.78149, w0=(323500,'J/mol'), E0=(-3194.27,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2598555334579625, var=1.9688175514768538, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_N-4R!H->Br',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_N-4R!H->Br
    Total Standard Deviation in ln(k): 3.4658385367471904"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_N-4R!H->Br
Total Standard Deviation in ln(k): 3.4658385367471904""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_N-4R!H->Br
Total Standard Deviation in ln(k): 3.4658385367471904
""",
)

entry(
    index = 84,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(4.92797e-10,'m^3/(mol*s)'), n=5.05694, w0=(323500,'J/mol'), E0=(-5462.78,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4146126939604183, var=2.1672192650295634, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C
    Total Standard Deviation in ln(k): 3.99300685255122"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C
Total Standard Deviation in ln(k): 3.99300685255122""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C
Total Standard Deviation in ln(k): 3.99300685255122
""",
)

entry(
    index = 85,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_N-1C-u0_N-Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(2625.75,'m^3/(mol*s)'), n=1.23946, w0=(323500,'J/mol'), E0=(33096,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_N-1C-u0_N-Sp-4R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_N-1C-u0_N-Sp-4R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_N-1C-u0_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_N-1C-u0_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 86,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F",
    kinetics = ArrheniusBM(A=(4314.73,'m^3/(mol*s)'), n=0.678601, w0=(285000,'J/mol'), E0=(42037.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.035185093060151204, var=5.548613709006941, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F',), comment="""BM rule fitted to 16 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F
    Total Standard Deviation in ln(k): 4.810657577134911"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F
Total Standard Deviation in ln(k): 4.810657577134911""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F
Total Standard Deviation in ln(k): 4.810657577134911
""",
)

entry(
    index = 87,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F",
    kinetics = ArrheniusBM(A=(0.239887,'m^3/(mol*s)'), n=2.28602, w0=(285000,'J/mol'), E0=(47848.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.04404576376952747, var=10.669414708636308, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F
    Total Standard Deviation in ln(k): 6.6589484439370485"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F
Total Standard Deviation in ln(k): 6.6589484439370485""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F
Total Standard Deviation in ln(k): 6.6589484439370485
""",
)

entry(
    index = 88,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_1C-u0_Ext-1C-R",
    kinetics = ArrheniusBM(A=(317.034,'m^3/(mol*s)'), n=1.47429, w0=(237500,'J/mol'), E0=(11059.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.025488002906318283, var=23.568530387070464, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_1C-u0_Ext-1C-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_1C-u0_Ext-1C-R
    Total Standard Deviation in ln(k): 9.79651395546459"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 9.79651395546459""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 9.79651395546459
""",
)

entry(
    index = 89,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0",
    kinetics = ArrheniusBM(A=(4.10067e+09,'m^3/(mol*s)'), n=-0.920209, w0=(276194,'J/mol'), E0=(57542.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.15390334292066807, var=7.34960592968302, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0',), comment="""BM rule fitted to 17 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0
    Total Standard Deviation in ln(k): 5.821560013084513"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0
Total Standard Deviation in ln(k): 5.821560013084513""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0
Total Standard Deviation in ln(k): 5.821560013084513
""",
)

entry(
    index = 90,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_N-1C-u0",
    kinetics = ArrheniusBM(A=(2.40279e+25,'m^3/(mol*s)'), n=-5.31366, w0=(285000,'J/mol'), E0=(79643.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.44309165403282924, var=7.090544534240762, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_N-1C-u0',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_N-1C-u0
    Total Standard Deviation in ln(k): 6.451519495892753"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_N-1C-u0
Total Standard Deviation in ln(k): 6.451519495892753""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_N-1C-u0
Total Standard Deviation in ln(k): 6.451519495892753
""",
)

entry(
    index = 91,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_N-3CO-u1_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.29951e+08,'m^3/(mol*s)'), n=-0.792618, w0=(260050,'J/mol'), E0=(23084.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.0498607650858904, var=15.155216902911233, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_N-3CO-u1_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_N-3CO-u1_Ext-1C-R
    Total Standard Deviation in ln(k): 15.467340642280385"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_N-3CO-u1_Ext-1C-R
Total Standard Deviation in ln(k): 15.467340642280385""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_N-3CO-u1_Ext-1C-R
Total Standard Deviation in ln(k): 15.467340642280385
""",
)

entry(
    index = 92,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_4R!H->Cl_1BrO-u0",
    kinetics = ArrheniusBM(A=(1.35321e-36,'m^3/(mol*s)'), n=12.4574, w0=(248775,'J/mol'), E0=(-51960.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.8387830801904048, var=5.421813014350684, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_4R!H->Cl_1BrO-u0',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_4R!H->Cl_1BrO-u0
    Total Standard Deviation in ln(k): 6.775478085131367"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_4R!H->Cl_1BrO-u0
Total Standard Deviation in ln(k): 6.775478085131367""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_4R!H->Cl_1BrO-u0
Total Standard Deviation in ln(k): 6.775478085131367
""",
)

entry(
    index = 93,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_4R!H->Cl_N-1BrO-u0",
    kinetics = ArrheniusBM(A=(4810.33,'m^3/(mol*s)'), n=0.358775, w0=(260050,'J/mol'), E0=(16812.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_4R!H->Cl_N-1BrO-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_4R!H->Cl_N-1BrO-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_4R!H->Cl_N-1BrO-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_4R!H->Cl_N-1BrO-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 94,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_N-4R!H->Cl_4BrCF->Br",
    kinetics = ArrheniusBM(A=(3.18502e+15,'m^3/(mol*s)'), n=-2.93547, w0=(248775,'J/mol'), E0=(51972.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.33227235803229394, var=17.785567083617504, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_N-4R!H->Cl_4BrCF->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_N-4R!H->Cl_4BrCF->Br
    Total Standard Deviation in ln(k): 9.289412004411622"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_N-4R!H->Cl_4BrCF->Br
Total Standard Deviation in ln(k): 9.289412004411622""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_N-4R!H->Cl_4BrCF->Br
Total Standard Deviation in ln(k): 9.289412004411622
""",
)

entry(
    index = 95,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_N-4R!H->Cl_N-4BrCF->Br",
    kinetics = ArrheniusBM(A=(2.63961e+06,'m^3/(mol*s)'), n=-0.182222, w0=(252533,'J/mol'), E0=(19940,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.27049586198572784, var=1.016314332492233, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_N-4R!H->Cl_N-4BrCF->Br',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_N-4R!H->Cl_N-4BrCF->Br
    Total Standard Deviation in ln(k): 2.700659720562218"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_N-4R!H->Cl_N-4BrCF->Br
Total Standard Deviation in ln(k): 2.700659720562218""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_N-4R!H->Cl_N-4BrCF->Br
Total Standard Deviation in ln(k): 2.700659720562218
""",
)

entry(
    index = 96,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_1BrO-u0_1BrO->Br_Sp-4R!H-3R",
    kinetics = ArrheniusBM(A=(7.85e+06,'m^3/(mol*s)'), n=0, w0=(237500,'J/mol'), E0=(23750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_1BrO-u0_1BrO->Br_Sp-4R!H-3R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_1BrO-u0_1BrO->Br_Sp-4R!H-3R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_1BrO-u0_1BrO->Br_Sp-4R!H-3R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_1BrO-u0_1BrO->Br_Sp-4R!H-3R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 97,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_1BrO-u0_1BrO->Br_N-Sp-4R!H-3R",
    kinetics = ArrheniusBM(A=(1.2e+07,'m^3/(mol*s)'), n=0, w0=(237500,'J/mol'), E0=(23750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_1BrO-u0_1BrO->Br_N-Sp-4R!H-3R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_1BrO-u0_1BrO->Br_N-Sp-4R!H-3R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_1BrO-u0_1BrO->Br_N-Sp-4R!H-3R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_1BrO-u0_1BrO->Br_N-Sp-4R!H-3R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 98,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_1BrO-u0_N-1BrO->Br_Sp-4R!H-3R",
    kinetics = ArrheniusBM(A=(36181.1,'m^3/(mol*s)'), n=0.525658, w0=(260050,'J/mol'), E0=(18554,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_1BrO-u0_N-1BrO->Br_Sp-4R!H-3R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_1BrO-u0_N-1BrO->Br_Sp-4R!H-3R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_1BrO-u0_N-1BrO->Br_Sp-4R!H-3R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_1BrO-u0_N-1BrO->Br_Sp-4R!H-3R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 99,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_1BrO-u0_N-1BrO->Br_N-Sp-4R!H-3R",
    kinetics = ArrheniusBM(A=(15049.5,'m^3/(mol*s)'), n=0.392587, w0=(260050,'J/mol'), E0=(26005,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_1BrO-u0_N-1BrO->Br_N-Sp-4R!H-3R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_1BrO-u0_N-1BrO->Br_N-Sp-4R!H-3R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_1BrO-u0_N-1BrO->Br_N-Sp-4R!H-3R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_1BrO-u0_N-1BrO->Br_N-Sp-4R!H-3R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 100,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_3CClHO->O_1BrO->Br",
    kinetics = ArrheniusBM(A=(6.55098e+07,'m^3/(mol*s)'), n=-0.354233, w0=(212550,'J/mol'), E0=(-4137.68,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.14028945735713552, var=0.07386226843174754, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_3CClHO->O_1BrO->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_3CClHO->O_1BrO->Br
    Total Standard Deviation in ln(k): 0.8973252280263948"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_3CClHO->O_1BrO->Br
Total Standard Deviation in ln(k): 0.8973252280263948""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_3CClHO->O_1BrO->Br
Total Standard Deviation in ln(k): 0.8973252280263948
""",
)

entry(
    index = 101,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_3CClHO->O_N-1BrO->Br",
    kinetics = ArrheniusBM(A=(7.2e+07,'m^3/(mol*s)'), n=0, w0=(235100,'J/mol'), E0=(10605.2,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_3CClHO->O_N-1BrO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_3CClHO->O_N-1BrO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_3CClHO->O_N-1BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_3CClHO->O_N-1BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 102,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1",
    kinetics = ArrheniusBM(A=(4.25573e+07,'m^3/(mol*s)'), n=0.133465, w0=(262574,'J/mol'), E0=(12120.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1791618795821122, var=5.618477454815291, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1
    Total Standard Deviation in ln(k): 5.202044731491255"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1
Total Standard Deviation in ln(k): 5.202044731491255""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1
Total Standard Deviation in ln(k): 5.202044731491255
""",
)

entry(
    index = 103,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_N-3CClH-u1",
    kinetics = ArrheniusBM(A=(194.627,'m^3/(mol*s)'), n=0.434377, w0=(237500,'J/mol'), E0=(23750,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_N-3CClH-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_N-3CClH-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_N-3CClH-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_N-3CClH-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 104,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0_N-3R->Br_N-3CClHO->H_3CClO->Cl",
    kinetics = ArrheniusBM(A=(6.29827e+09,'m^3/(mol*s)'), n=-0.790848, w0=(226970,'J/mol'), E0=(8508.22,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0_N-3R->Br_N-3CClHO->H_3CClO->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0_N-3R->Br_N-3CClHO->H_3CClO->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0_N-3R->Br_N-3CClHO->H_3CClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0_N-3R->Br_N-3CClHO->H_3CClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 105,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0_N-3R->Br_N-3CClHO->H_N-3CClO->Cl",
    kinetics = ArrheniusBM(A=(678423,'m^3/(mol*s)'), n=0.465326, w0=(247575,'J/mol'), E0=(4209.08,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.8791561812784865, var=21.885036233336137, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0_N-3R->Br_N-3CClHO->H_N-3CClO->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0_N-3R->Br_N-3CClHO->H_N-3CClO->Cl
    Total Standard Deviation in ln(k): 19.125064005269433"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0_N-3R->Br_N-3CClHO->H_N-3CClO->Cl
Total Standard Deviation in ln(k): 19.125064005269433""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0_N-3R->Br_N-3CClHO->H_N-3CClO->Cl
Total Standard Deviation in ln(k): 19.125064005269433
""",
)

entry(
    index = 106,
    label = "Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_6R!H->Cl",
    kinetics = ArrheniusBM(A=(21423,'m^3/(mol*s)'), n=0.655198, w0=(323500,'J/mol'), E0=(162660,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_6R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_6R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 107,
    label = "Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_N-6R!H->Cl",
    kinetics = ArrheniusBM(A=(34501.4,'m^3/(mol*s)'), n=0.481205, w0=(323500,'J/mol'), E0=(165195,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_N-6R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_N-6R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_N-6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_N-6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 108,
    label = "Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F_Ext-3C-R_N-5R!H->C_5BrClFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(271.29,'m^3/(mol*s)'), n=0.930555, w0=(323500,'J/mol'), E0=(69820.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F_Ext-3C-R_N-5R!H->C_5BrClFINOPSSi->Br',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F_Ext-3C-R_N-5R!H->C_5BrClFINOPSSi->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F_Ext-3C-R_N-5R!H->C_5BrClFINOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F_Ext-3C-R_N-5R!H->C_5BrClFINOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 109,
    label = "Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F_Ext-3C-R_N-5R!H->C_N-5BrClFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(4.1976e-15,'m^3/(mol*s)'), n=6.22802, w0=(323500,'J/mol'), E0=(13046.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.09070744057682063, var=1.5731088435864324, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F_Ext-3C-R_N-5R!H->C_N-5BrClFINOPSSi->Br',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F_Ext-3C-R_N-5R!H->C_N-5BrClFINOPSSi->Br
    Total Standard Deviation in ln(k): 2.7423197658628324"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F_Ext-3C-R_N-5R!H->C_N-5BrClFINOPSSi->Br
Total Standard Deviation in ln(k): 2.7423197658628324""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F_Ext-3C-R_N-5R!H->C_N-5BrClFINOPSSi->Br
Total Standard Deviation in ln(k): 2.7423197658628324
""",
)

entry(
    index = 110,
    label = "Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_N-4R!H->F_4BrCClINOPSSi->C_Sp-4C=3C",
    kinetics = ArrheniusBM(A=(4478.47,'m^3/(mol*s)'), n=0.974603, w0=(323500,'J/mol'), E0=(64748.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.017686131927548882, var=0.006433665541479198, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_N-4R!H->F_4BrCClINOPSSi->C_Sp-4C=3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_N-4R!H->F_4BrCClINOPSSi->C_Sp-4C=3C
    Total Standard Deviation in ln(k): 0.2052375859131282"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_N-4R!H->F_4BrCClINOPSSi->C_Sp-4C=3C
Total Standard Deviation in ln(k): 0.2052375859131282""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_N-4R!H->F_4BrCClINOPSSi->C_Sp-4C=3C
Total Standard Deviation in ln(k): 0.2052375859131282
""",
)

entry(
    index = 111,
    label = "Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_N-4R!H->F_4BrCClINOPSSi->C_N-Sp-4C=3C",
    kinetics = ArrheniusBM(A=(15.4495,'m^3/(mol*s)'), n=1.56199, w0=(323500,'J/mol'), E0=(53705.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0037981947199020867, var=4.086339118900511, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_N-4R!H->F_4BrCClINOPSSi->C_N-Sp-4C=3C',), comment="""BM rule fitted to 4 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_N-4R!H->F_4BrCClINOPSSi->C_N-Sp-4C=3C
    Total Standard Deviation in ln(k): 4.0620541063384765"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_N-4R!H->F_4BrCClINOPSSi->C_N-Sp-4C=3C
Total Standard Deviation in ln(k): 4.0620541063384765""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_N-4R!H->F_4BrCClINOPSSi->C_N-Sp-4C=3C
Total Standard Deviation in ln(k): 4.0620541063384765
""",
)

entry(
    index = 112,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_Ext-4R!H-R_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(9.10921e+08,'m^3/(mol*s)'), n=-0.104144, w0=(323500,'J/mol'), E0=(167839,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-8.212183991944255e-05, var=1.2895194608912057, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_Ext-4R!H-R_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_Ext-4R!H-R_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 2.276723556427068"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_Ext-4R!H-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 2.276723556427068""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_Ext-4R!H-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 2.276723556427068
""",
)

entry(
    index = 113,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_N-4R!H->Br_Sp-4CClFO-1C",
    kinetics = ArrheniusBM(A=(1.31654e-08,'m^3/(mol*s)'), n=4.77837, w0=(323500,'J/mol'), E0=(9348.51,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.26363590249463076, var=1.9632033360096317, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_N-4R!H->Br_Sp-4CClFO-1C',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_N-4R!H->Br_Sp-4CClFO-1C
    Total Standard Deviation in ln(k): 3.4713234513827493"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_N-4R!H->Br_Sp-4CClFO-1C
Total Standard Deviation in ln(k): 3.4713234513827493""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_N-4R!H->Br_Sp-4CClFO-1C
Total Standard Deviation in ln(k): 3.4713234513827493
""",
)

entry(
    index = 114,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_N-4R!H->Br_N-Sp-4CClFO-1C",
    kinetics = ArrheniusBM(A=(3e+08,'m^3/(mol*s)'), n=0, w0=(323500,'J/mol'), E0=(65544.2,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_N-4R!H->Br_N-Sp-4CClFO-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_N-4R!H->Br_N-Sp-4CClFO-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_N-4R!H->Br_N-Sp-4CClFO-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_N-4R!H->Br_N-Sp-4CClFO-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 115,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(379.761,'m^3/(mol*s)'), n=1.67816, w0=(323500,'J/mol'), E0=(33799.7,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 116,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C",
    kinetics = ArrheniusBM(A=(197.056,'m^3/(mol*s)'), n=1.64084, w0=(323500,'J/mol'), E0=(41284.7,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 117,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(149.752,'m^3/(mol*s)'), n=1.64303, w0=(323500,'J/mol'), E0=(44257.2,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 118,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R",
    kinetics = ArrheniusBM(A=(4.68285e+06,'m^3/(mol*s)'), n=-0.166593, w0=(285000,'J/mol'), E0=(47200.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.007313060876220849, var=4.9263356540811625, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R
    Total Standard Deviation in ln(k): 4.4679542119148925"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R
Total Standard Deviation in ln(k): 4.4679542119148925""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R
Total Standard Deviation in ln(k): 4.4679542119148925
""",
)

entry(
    index = 119,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-3C-R_5R!H->Br",
    kinetics = ArrheniusBM(A=(73.0295,'m^3/(mol*s)'), n=0.946296, w0=(285000,'J/mol'), E0=(48051.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-3C-R_5R!H->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-3C-R_5R!H->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-3C-R_5R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-3C-R_5R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 120,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-3C-R_N-5R!H->Br",
    kinetics = ArrheniusBM(A=(5187.03,'m^3/(mol*s)'), n=0.339242, w0=(285000,'J/mol'), E0=(40241.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.6437996832837445, var=5.59651690660517, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-3C-R_N-5R!H->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-3C-R_N-5R!H->Br
    Total Standard Deviation in ln(k): 8.872743432929736"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-3C-R_N-5R!H->Br
Total Standard Deviation in ln(k): 8.872743432929736""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-3C-R_N-5R!H->Br
Total Standard Deviation in ln(k): 8.872743432929736
""",
)

entry(
    index = 121,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_4BrCClO->Cl",
    kinetics = ArrheniusBM(A=(4.05024e-05,'m^3/(mol*s)'), n=3.10137, w0=(285000,'J/mol'), E0=(48070.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_4BrCClO->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_4BrCClO->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_4BrCClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_4BrCClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 122,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl",
    kinetics = ArrheniusBM(A=(0.00583005,'m^3/(mol*s)'), n=2.80279, w0=(285000,'J/mol'), E0=(43085.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.08639510974763989, var=11.312379296105428, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl
    Total Standard Deviation in ln(k): 6.959775178919852"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl
Total Standard Deviation in ln(k): 6.959775178919852""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl
Total Standard Deviation in ln(k): 6.959775178919852
""",
)

entry(
    index = 123,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_1C-u0_Ext-1C-R_Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(301.161,'m^3/(mol*s)'), n=1.48029, w0=(237500,'J/mol'), E0=(4971.77,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0024214454611250617, var=23.66946923334349, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_1C-u0_Ext-1C-R_Sp-4R!H-1C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_1C-u0_Ext-1C-R_Sp-4R!H-1C
    Total Standard Deviation in ln(k): 9.75937653944994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_1C-u0_Ext-1C-R_Sp-4R!H-1C
Total Standard Deviation in ln(k): 9.75937653944994""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_1C-u0_Ext-1C-R_Sp-4R!H-1C
Total Standard Deviation in ln(k): 9.75937653944994
""",
)

entry(
    index = 124,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_1C-u0_Ext-1C-R_N-Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(7.0092e+09,'m^3/(mol*s)'), n=-0.392, w0=(237500,'J/mol'), E0=(23750,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_1C-u0_Ext-1C-R_N-Sp-4R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_1C-u0_Ext-1C-R_N-Sp-4R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_1C-u0_Ext-1C-R_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_1C-u0_Ext-1C-R_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 125,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C",
    kinetics = ArrheniusBM(A=(0.00999654,'m^3/(mol*s)'), n=2.53877, w0=(285000,'J/mol'), E0=(40732.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00839183604230005, var=6.235335808630295, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C
    Total Standard Deviation in ln(k): 5.027039692089164"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C
Total Standard Deviation in ln(k): 5.027039692089164""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C
Total Standard Deviation in ln(k): 5.027039692089164
""",
)

entry(
    index = 126,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_N-3CO->C",
    kinetics = ArrheniusBM(A=(4.92843e+11,'m^3/(mol*s)'), n=-1.65601, w0=(260050,'J/mol'), E0=(28899.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.15273429410097944, var=3.572853359510573, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_N-3CO->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_N-3CO->C
    Total Standard Deviation in ln(k): 4.1731033296258175"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_N-3CO->C
Total Standard Deviation in ln(k): 4.1731033296258175""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_N-3CO->C
Total Standard Deviation in ln(k): 4.1731033296258175
""",
)

entry(
    index = 127,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_N-1C-u0_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.72205e+13,'m^3/(mol*s)'), n=-1.72311, w0=(285000,'J/mol'), E0=(30937.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.9033957811730633, var=0.032230573830243005, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_N-1C-u0_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_N-1C-u0_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 7.654871866621272"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_N-1C-u0_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 7.654871866621272""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_N-1C-u0_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 7.654871866621272
""",
)

entry(
    index = 128,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_N-1C-u0_Ext-1C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(0.0291245,'m^3/(mol*s)'), n=2.69164, w0=(285000,'J/mol'), E0=(36210.7,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_N-1C-u0_Ext-1C-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_N-1C-u0_Ext-1C-R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_N-1C-u0_Ext-1C-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_N-1C-u0_Ext-1C-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 129,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_N-1C-u0_Ext-1C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.0169924,'m^3/(mol*s)'), n=2.72405, w0=(285000,'J/mol'), E0=(41346.9,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_N-1C-u0_Ext-1C-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_N-1C-u0_Ext-1C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_N-1C-u0_Ext-1C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_N-1C-u0_Ext-1C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 130,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_N-3CO-u1_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(5.74605e+07,'m^3/(mol*s)'), n=-0.471535, w0=(260050,'J/mol'), E0=(20123.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.9307833028032546, var=7.727576628603477, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_N-3CO-u1_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_N-3CO-u1_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 10.424080957928155"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_N-3CO-u1_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 10.424080957928155""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_N-3CO-u1_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 10.424080957928155
""",
)

entry(
    index = 131,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_4R!H->Cl_1BrO-u0_1BrO->Br",
    kinetics = ArrheniusBM(A=(1882.63,'m^3/(mol*s)'), n=0.917064, w0=(237500,'J/mol'), E0=(54196.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_4R!H->Cl_1BrO-u0_1BrO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_4R!H->Cl_1BrO-u0_1BrO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_4R!H->Cl_1BrO-u0_1BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_4R!H->Cl_1BrO-u0_1BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 132,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_4R!H->Cl_1BrO-u0_N-1BrO->Br",
    kinetics = ArrheniusBM(A=(214.525,'m^3/(mol*s)'), n=0.917651, w0=(260050,'J/mol'), E0=(12955.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_4R!H->Cl_1BrO-u0_N-1BrO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_4R!H->Cl_1BrO-u0_N-1BrO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_4R!H->Cl_1BrO-u0_N-1BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_4R!H->Cl_1BrO-u0_N-1BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 133,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_N-4R!H->Cl_4BrCF->Br_1BrO->Br",
    kinetics = ArrheniusBM(A=(1.15e+06,'m^3/(mol*s)'), n=0, w0=(237500,'J/mol'), E0=(25499.6,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_N-4R!H->Cl_4BrCF->Br_1BrO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_N-4R!H->Cl_4BrCF->Br_1BrO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_N-4R!H->Cl_4BrCF->Br_1BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_N-4R!H->Cl_4BrCF->Br_1BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 134,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_N-4R!H->Cl_4BrCF->Br_N-1BrO->Br",
    kinetics = ArrheniusBM(A=(55.3041,'m^3/(mol*s)'), n=0.908883, w0=(260050,'J/mol'), E0=(12616.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_N-4R!H->Cl_4BrCF->Br_N-1BrO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_N-4R!H->Cl_4BrCF->Br_N-1BrO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_N-4R!H->Cl_4BrCF->Br_N-1BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_N-4R!H->Cl_4BrCF->Br_N-1BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 135,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_N-4R!H->Cl_N-4BrCF->Br_1BrO-u0",
    kinetics = ArrheniusBM(A=(4.70779e+06,'m^3/(mol*s)'), n=-0.247245, w0=(248775,'J/mol'), E0=(-2989.85,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.6462620335978734, var=0.1104653596575432, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_N-4R!H->Cl_N-4BrCF->Br_1BrO-u0',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_N-4R!H->Cl_N-4BrCF->Br_1BrO-u0
    Total Standard Deviation in ln(k): 2.290074309067887"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_N-4R!H->Cl_N-4BrCF->Br_1BrO-u0
Total Standard Deviation in ln(k): 2.290074309067887""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_N-4R!H->Cl_N-4BrCF->Br_1BrO-u0
Total Standard Deviation in ln(k): 2.290074309067887
""",
)

entry(
    index = 136,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_N-4R!H->Cl_N-4BrCF->Br_N-1BrO-u0",
    kinetics = ArrheniusBM(A=(16163.4,'m^3/(mol*s)'), n=0.323494, w0=(260050,'J/mol'), E0=(14274.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_N-4R!H->Cl_N-4BrCF->Br_N-1BrO-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_N-4R!H->Cl_N-4BrCF->Br_N-1BrO-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_N-4R!H->Cl_N-4BrCF->Br_N-1BrO-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_N-4R!H->Cl_N-4BrCF->Br_N-1BrO-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 137,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_3CClHO->O_1BrO->Br_3O-u1",
    kinetics = ArrheniusBM(A=(5.55e+08,'m^3/(mol*s)'), n=-0.66, w0=(212550,'J/mol'), E0=(4523.67,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_3CClHO->O_1BrO->Br_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_3CClHO->O_1BrO->Br_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_3CClHO->O_1BrO->Br_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_3CClHO->O_1BrO->Br_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 138,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_3CClHO->O_1BrO->Br_N-3O-u1",
    kinetics = ArrheniusBM(A=(5.3e+06,'m^3/(mol*s)'), n=0, w0=(212550,'J/mol'), E0=(8723.87,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_3CClHO->O_1BrO->Br_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_3CClHO->O_1BrO->Br_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_3CClHO->O_1BrO->Br_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_3CClHO->O_1BrO->Br_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 139,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_3CClH->H",
    kinetics = ArrheniusBM(A=(1351.55,'m^3/(mol*s)'), n=1.62054, w0=(292912,'J/mol'), E0=(29291.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.006954391262830947, var=0.22462875505850005, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_3CClH->H',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_3CClH->H
    Total Standard Deviation in ln(k): 0.9676178574617904"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_3CClH->H
Total Standard Deviation in ln(k): 0.9676178574617904""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_3CClH->H
Total Standard Deviation in ln(k): 0.9676178574617904
""",
)

entry(
    index = 140,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_N-3CClH->H",
    kinetics = ArrheniusBM(A=(2.53938e+18,'m^3/(mol*s)'), n=-3.2115, w0=(232235,'J/mol'), E0=(25698.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.15641619058286377, var=29.34931973788548, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_N-3CClH->H',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_N-3CClH->H
    Total Standard Deviation in ln(k): 11.253660281342048"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_N-3CClH->H
Total Standard Deviation in ln(k): 11.253660281342048""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_N-3CClH->H
Total Standard Deviation in ln(k): 11.253660281342048
""",
)

entry(
    index = 141,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0_N-3R->Br_N-3CClHO->H_N-3CClO->Cl_3CO->C",
    kinetics = ArrheniusBM(A=(5.64233e+07,'m^3/(mol*s)'), n=-0.596289, w0=(260050,'J/mol'), E0=(15576.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0_N-3R->Br_N-3CClHO->H_N-3CClO->Cl_3CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0_N-3R->Br_N-3CClHO->H_N-3CClO->Cl_3CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0_N-3R->Br_N-3CClHO->H_N-3CClO->Cl_3CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0_N-3R->Br_N-3CClHO->H_N-3CClO->Cl_3CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 142,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0_N-3R->Br_N-3CClHO->H_N-3CClO->Cl_N-3CO->C",
    kinetics = ArrheniusBM(A=(1.61447e+09,'m^3/(mol*s)'), n=-0.558876, w0=(235100,'J/mol'), E0=(12790.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0_N-3R->Br_N-3CClHO->H_N-3CClO->Cl_N-3CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0_N-3R->Br_N-3CClHO->H_N-3CClO->Cl_N-3CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0_N-3R->Br_N-3CClHO->H_N-3CClO->Cl_N-3CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_N-1BrO-u0_N-3R->Br_N-3CClHO->H_N-3CClO->Cl_N-3CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 143,
    label = "Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F_Ext-3C-R_N-5R!H->C_N-5BrClFINOPSSi->Br_5ClF->Cl",
    kinetics = ArrheniusBM(A=(1055.67,'m^3/(mol*s)'), n=0.939323, w0=(323500,'J/mol'), E0=(69260.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F_Ext-3C-R_N-5R!H->C_N-5BrClFINOPSSi->Br_5ClF->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F_Ext-3C-R_N-5R!H->C_N-5BrClFINOPSSi->Br_5ClF->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F_Ext-3C-R_N-5R!H->C_N-5BrClFINOPSSi->Br_5ClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F_Ext-3C-R_N-5R!H->C_N-5BrClFINOPSSi->Br_5ClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 144,
    label = "Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F_Ext-3C-R_N-5R!H->C_N-5BrClFINOPSSi->Br_N-5ClF->Cl",
    kinetics = ArrheniusBM(A=(0.020179,'m^3/(mol*s)'), n=2.37805, w0=(323500,'J/mol'), E0=(51557.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.7602096917111854, var=1.282401671043499, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F_Ext-3C-R_N-5R!H->C_N-5BrClFINOPSSi->Br_N-5ClF->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F_Ext-3C-R_N-5R!H->C_N-5BrClFINOPSSi->Br_N-5ClF->Cl
    Total Standard Deviation in ln(k): 4.180300256601981"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F_Ext-3C-R_N-5R!H->C_N-5BrClFINOPSSi->Br_N-5ClF->Cl
Total Standard Deviation in ln(k): 4.180300256601981""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F_Ext-3C-R_N-5R!H->C_N-5BrClFINOPSSi->Br_N-5ClF->Cl
Total Standard Deviation in ln(k): 4.180300256601981
""",
)

entry(
    index = 145,
    label = "Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_N-4R!H->F_4BrCClINOPSSi->C_Sp-4C=3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.28415e-07,'m^3/(mol*s)'), n=4.24484, w0=(323500,'J/mol'), E0=(47185.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_N-4R!H->F_4BrCClINOPSSi->C_Sp-4C=3C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_N-4R!H->F_4BrCClINOPSSi->C_Sp-4C=3C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_N-4R!H->F_4BrCClINOPSSi->C_Sp-4C=3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_N-4R!H->F_4BrCClINOPSSi->C_Sp-4C=3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 146,
    label = "Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_N-4R!H->F_4BrCClINOPSSi->C_N-Sp-4C=3C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(0.00446386,'m^3/(mol*s)'), n=2.50706, w0=(323500,'J/mol'), E0=(44546.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.002369357643453439, var=4.8899952222988965, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_N-4R!H->F_4BrCClINOPSSi->C_N-Sp-4C=3C_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_N-4R!H->F_4BrCClINOPSSi->C_N-Sp-4C=3C_Ext-4C-R
    Total Standard Deviation in ln(k): 4.439090711452324"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_N-4R!H->F_4BrCClINOPSSi->C_N-Sp-4C=3C_Ext-4C-R
Total Standard Deviation in ln(k): 4.439090711452324""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_N-4R!H->F_4BrCClINOPSSi->C_N-Sp-4C=3C_Ext-4C-R
Total Standard Deviation in ln(k): 4.439090711452324
""",
)

entry(
    index = 147,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_Ext-4R!H-R_Ext-1C-R_Ext-1C-R_5R!H->Br",
    kinetics = ArrheniusBM(A=(5e+08,'m^3/(mol*s)'), n=0, w0=(323500,'J/mol'), E0=(172381,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_Ext-4R!H-R_Ext-1C-R_Ext-1C-R_5R!H->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_Ext-4R!H-R_Ext-1C-R_Ext-1C-R_5R!H->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_Ext-4R!H-R_Ext-1C-R_Ext-1C-R_5R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_Ext-4R!H-R_Ext-1C-R_Ext-1C-R_5R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 148,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_Ext-4R!H-R_Ext-1C-R_Ext-1C-R_N-5R!H->Br",
    kinetics = ArrheniusBM(A=(1e+09,'m^3/(mol*s)'), n=0, w0=(323500,'J/mol'), E0=(171436,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_Ext-4R!H-R_Ext-1C-R_Ext-1C-R_N-5R!H->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_Ext-4R!H-R_Ext-1C-R_Ext-1C-R_N-5R!H->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_Ext-4R!H-R_Ext-1C-R_Ext-1C-R_N-5R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_Ext-4R!H-R_Ext-1C-R_Ext-1C-R_N-5R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 149,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_N-4R!H->Br_Sp-4CClFO-1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.05389e-09,'m^3/(mol*s)'), n=5.02905, w0=(323500,'J/mol'), E0=(8987.67,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.08757357177092147, var=1.3904003504673823, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_N-4R!H->Br_Sp-4CClFO-1C_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_N-4R!H->Br_Sp-4CClFO-1C_Ext-1C-R
    Total Standard Deviation in ln(k): 2.5839222506334107"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_N-4R!H->Br_Sp-4CClFO-1C_Ext-1C-R
Total Standard Deviation in ln(k): 2.5839222506334107""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_N-4R!H->Br_Sp-4CClFO-1C_Ext-1C-R
Total Standard Deviation in ln(k): 2.5839222506334107
""",
)

entry(
    index = 150,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_N-4R!H->Br_Sp-4CClFO-1C_4CClFO->C",
    kinetics = ArrheniusBM(A=(416.64,'m^3/(mol*s)'), n=1.75119, w0=(323500,'J/mol'), E0=(48282.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.10056140288087342, var=0.020642194789598986, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_N-4R!H->Br_Sp-4CClFO-1C_4CClFO->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_N-4R!H->Br_Sp-4CClFO-1C_4CClFO->C
    Total Standard Deviation in ln(k): 0.540694985061601"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_N-4R!H->Br_Sp-4CClFO-1C_4CClFO->C
Total Standard Deviation in ln(k): 0.540694985061601""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_N-4R!H->Br_Sp-4CClFO-1C_4CClFO->C
Total Standard Deviation in ln(k): 0.540694985061601
""",
)

entry(
    index = 151,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_N-4R!H->Br_Sp-4CClFO-1C_N-4CClFO->C",
    kinetics = ArrheniusBM(A=(371.066,'m^3/(mol*s)'), n=1.71693, w0=(323500,'J/mol'), E0=(55780.9,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_N-4R!H->Br_Sp-4CClFO-1C_N-4CClFO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_N-4R!H->Br_Sp-4CClFO-1C_N-4CClFO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_N-4R!H->Br_Sp-4CClFO-1C_N-4CClFO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_N-4R!H->Br_Sp-4CClFO-1C_N-4CClFO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 152,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(547429,'m^3/(mol*s)'), n=0.0256044, w0=(285000,'J/mol'), E0=(56022.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0002494641382711485, var=2.117772947611213, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_6R!H->C
    Total Standard Deviation in ln(k): 2.9180315568045647"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_6R!H->C
Total Standard Deviation in ln(k): 2.9180315568045647""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_6R!H->C
Total Standard Deviation in ln(k): 2.9180315568045647
""",
)

entry(
    index = 153,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(1.14616e+07,'m^3/(mol*s)'), n=-0.260625, w0=(285000,'J/mol'), E0=(45320.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.013772051614507598, var=5.006394062555299, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 4.520192420627709"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C
Total Standard Deviation in ln(k): 4.520192420627709""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C
Total Standard Deviation in ln(k): 4.520192420627709
""",
)

entry(
    index = 154,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-3C-R_N-5R!H->Br_5CClFINOPSSi->Cl",
    kinetics = ArrheniusBM(A=(27.0649,'m^3/(mol*s)'), n=0.955064, w0=(285000,'J/mol'), E0=(31639.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-3C-R_N-5R!H->Br_5CClFINOPSSi->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-3C-R_N-5R!H->Br_5CClFINOPSSi->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-3C-R_N-5R!H->Br_5CClFINOPSSi->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-3C-R_N-5R!H->Br_5CClFINOPSSi->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 155,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-3C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl",
    kinetics = ArrheniusBM(A=(8.8168e-05,'m^3/(mol*s)'), n=2.96978, w0=(285000,'J/mol'), E0=(28287.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-3C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-3C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-3C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-3C-R_N-5R!H->Br_N-5CClFINOPSSi->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 156,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.09344e+20,'m^3/(mol*s)'), n=-3.95459, w0=(285000,'J/mol'), E0=(51552.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1947993986133369, var=10.992844849589671, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 7.13623696251936"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 7.13623696251936""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 7.13623696251936
""",
)

entry(
    index = 157,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Ext-4BrCO-R",
    kinetics = ArrheniusBM(A=(0.00204522,'m^3/(mol*s)'), n=2.89817, w0=(285000,'J/mol'), E0=(65338.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Ext-4BrCO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Ext-4BrCO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Ext-4BrCO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Ext-4BrCO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 158,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C",
    kinetics = ArrheniusBM(A=(2.5186e+06,'m^3/(mol*s)'), n=0.259244, w0=(285000,'J/mol'), E0=(57603.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1462307266021346, var=10.238703902589506, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C
    Total Standard Deviation in ln(k): 6.782160131382683"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C
Total Standard Deviation in ln(k): 6.782160131382683""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C
Total Standard Deviation in ln(k): 6.782160131382683
""",
)

entry(
    index = 159,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_N-Sp-4BrCO-3C",
    kinetics = ArrheniusBM(A=(199360,'m^3/(mol*s)'), n=0.43, w0=(285000,'J/mol'), E0=(13954.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_N-Sp-4BrCO-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_N-Sp-4BrCO-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_N-Sp-4BrCO-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_N-Sp-4BrCO-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 160,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->Br",
    kinetics = ArrheniusBM(A=(9.62687e+10,'m^3/(mol*s)'), n=-0.908295, w0=(237500,'J/mol'), E0=(36569.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 161,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Br",
    kinetics = ArrheniusBM(A=(1.41327e+09,'m^3/(mol*s)'), n=-0.450516, w0=(237500,'J/mol'), E0=(59884.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.140731266546097, var=19.619247366976207, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Br',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Br
    Total Standard Deviation in ln(k): 16.77098187970486"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Br
Total Standard Deviation in ln(k): 16.77098187970486""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Br
Total Standard Deviation in ln(k): 16.77098187970486
""",
)

entry(
    index = 162,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(4.13691e-16,'m^3/(mol*s)'), n=6.74351, w0=(285000,'J/mol'), E0=(11893.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.22246476218627947, var=13.224758945600287, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_4R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_4R!H->C
    Total Standard Deviation in ln(k): 7.849348538644379"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_4R!H->C
Total Standard Deviation in ln(k): 7.849348538644379""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_4R!H->C
Total Standard Deviation in ln(k): 7.849348538644379
""",
)

entry(
    index = 163,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(191.019,'m^3/(mol*s)'), n=1.0315, w0=(285000,'J/mol'), E0=(47076.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0236953927280496, var=2.191363859876865, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_N-4R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 3.027196803927249"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_N-4R!H->C
Total Standard Deviation in ln(k): 3.027196803927249""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_N-4R!H->C
Total Standard Deviation in ln(k): 3.027196803927249
""",
)

entry(
    index = 164,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_N-3CO->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.06998e+11,'m^3/(mol*s)'), n=-1.46221, w0=(260050,'J/mol'), E0=(27100.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.12762720018091006, var=3.544069048158676, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_N-3CO->C_Ext-1C-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_N-3CO->C_Ext-1C-R
    Total Standard Deviation in ln(k): 4.094725068964159"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_N-3CO->C_Ext-1C-R
Total Standard Deviation in ln(k): 4.094725068964159""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_N-3CO->C_Ext-1C-R
Total Standard Deviation in ln(k): 4.094725068964159
""",
)

entry(
    index = 165,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_N-1C-u0_Ext-1C-R_Ext-1C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(0.0244505,'m^3/(mol*s)'), n=2.62586, w0=(285000,'J/mol'), E0=(22089.6,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_N-1C-u0_Ext-1C-R_Ext-1C-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_N-1C-u0_Ext-1C-R_Ext-1C-R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_N-1C-u0_Ext-1C-R_Ext-1C-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_N-1C-u0_Ext-1C-R_Ext-1C-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 166,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_N-1C-u0_Ext-1C-R_Ext-1C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.0741868,'m^3/(mol*s)'), n=2.6667, w0=(285000,'J/mol'), E0=(21687.6,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_N-1C-u0_Ext-1C-R_Ext-1C-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_N-1C-u0_Ext-1C-R_Ext-1C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_N-1C-u0_Ext-1C-R_Ext-1C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_N-1C-u0_Ext-1C-R_Ext-1C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 167,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_N-3CO-u1_Ext-1C-R_Ext-1C-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(3.15e+06,'m^3/(mol*s)'), n=0, w0=(260050,'J/mol'), E0=(24078.9,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_N-3CO-u1_Ext-1C-R_Ext-1C-R_4R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_N-3CO-u1_Ext-1C-R_Ext-1C-R_4R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_N-3CO-u1_Ext-1C-R_Ext-1C-R_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_N-3CO-u1_Ext-1C-R_Ext-1C-R_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 168,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_N-3CO-u1_Ext-1C-R_Ext-1C-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(9e+06,'m^3/(mol*s)'), n=0, w0=(260050,'J/mol'), E0=(14285.2,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_N-3CO-u1_Ext-1C-R_Ext-1C-R_N-4R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_N-3CO-u1_Ext-1C-R_Ext-1C-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_N-3CO-u1_Ext-1C-R_Ext-1C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_N-3CO-u1_Ext-1C-R_Ext-1C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 169,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_N-4R!H->Cl_N-4BrCF->Br_1BrO-u0_1BrO->Br",
    kinetics = ArrheniusBM(A=(605000,'m^3/(mol*s)'), n=0, w0=(237500,'J/mol'), E0=(23750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_N-4R!H->Cl_N-4BrCF->Br_1BrO-u0_1BrO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_N-4R!H->Cl_N-4BrCF->Br_1BrO-u0_1BrO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_N-4R!H->Cl_N-4BrCF->Br_1BrO-u0_1BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_N-4R!H->Cl_N-4BrCF->Br_1BrO-u0_1BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 170,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_N-4R!H->Cl_N-4BrCF->Br_1BrO-u0_N-1BrO->Br",
    kinetics = ArrheniusBM(A=(800.927,'m^3/(mol*s)'), n=0.88237, w0=(260050,'J/mol'), E0=(18237.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_N-4R!H->Cl_N-4BrCF->Br_1BrO-u0_N-1BrO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_N-4R!H->Cl_N-4BrCF->Br_1BrO-u0_N-1BrO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_N-4R!H->Cl_N-4BrCF->Br_1BrO-u0_N-1BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_Ext-3R-R_Ext-3R-R_N-4R!H->Cl_N-4BrCF->Br_1BrO-u0_N-1BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 171,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_3CClH->H_Ext-1BrO-R",
    kinetics = ArrheniusBM(A=(1309.58,'m^3/(mol*s)'), n=1.62557, w0=(298550,'J/mol'), E0=(29855,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.05630419466203027, var=0.3152507178383666, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_3CClH->H_Ext-1BrO-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_3CClH->H_Ext-1BrO-R
    Total Standard Deviation in ln(k): 1.2670702803684868"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_3CClH->H_Ext-1BrO-R
Total Standard Deviation in ln(k): 1.2670702803684868""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_3CClH->H_Ext-1BrO-R
Total Standard Deviation in ln(k): 1.2670702803684868
""",
)

entry(
    index = 172,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_3CClH->H_1BrO->Br",
    kinetics = ArrheniusBM(A=(114000,'m^3/(mol*s)'), n=1, w0=(276000,'J/mol'), E0=(27600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_3CClH->H_1BrO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_3CClH->H_1BrO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_3CClH->H_1BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_3CClH->H_1BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 173,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_3CClH->H_N-1BrO->Br",
    kinetics = ArrheniusBM(A=(3e+07,'m^3/(mol*s)'), n=0, w0=(298550,'J/mol'), E0=(29855,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_3CClH->H_N-1BrO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_3CClH->H_N-1BrO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_3CClH->H_N-1BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_3CClH->H_N-1BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 174,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_N-3CClH->H_1BrO->Br",
    kinetics = ArrheniusBM(A=(1.28903e+08,'m^3/(mol*s)'), n=0.160282, w0=(220960,'J/mol'), E0=(768.032,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-5.71921841333791, var=51.110668855379124, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_N-3CClH->H_1BrO->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_N-3CClH->H_1BrO->Br
    Total Standard Deviation in ln(k): 28.702092595172754"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_N-3CClH->H_1BrO->Br
Total Standard Deviation in ln(k): 28.702092595172754""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_N-3CClH->H_1BrO->Br
Total Standard Deviation in ln(k): 28.702092595172754
""",
)

entry(
    index = 175,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_N-3CClH->H_N-1BrO->Br",
    kinetics = ArrheniusBM(A=(3.55879e+11,'m^3/(mol*s)'), n=-1.5018, w0=(243510,'J/mol'), E0=(5917.44,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.2631937375164712, var=0.24607249240667117, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_N-3CClH->H_N-1BrO->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_N-3CClH->H_N-1BrO->Br
    Total Standard Deviation in ln(k): 9.193441997459777"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_N-3CClH->H_N-1BrO->Br
Total Standard Deviation in ln(k): 9.193441997459777""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_N-3CClH->H_N-1BrO->Br
Total Standard Deviation in ln(k): 9.193441997459777
""",
)

entry(
    index = 176,
    label = "Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F_Ext-3C-R_N-5R!H->C_N-5BrClFINOPSSi->Br_N-5ClF->Cl_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.000157155,'m^3/(mol*s)'), n=2.91404, w0=(323500,'J/mol'), E0=(28843,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F_Ext-3C-R_N-5R!H->C_N-5BrClFINOPSSi->Br_N-5ClF->Cl_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F_Ext-3C-R_N-5R!H->C_N-5BrClFINOPSSi->Br_N-5ClF->Cl_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F_Ext-3C-R_N-5R!H->C_N-5BrClFINOPSSi->Br_N-5ClF->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_4R!H->F_Ext-3C-R_N-5R!H->C_N-5BrClFINOPSSi->Br_N-5ClF->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 177,
    label = "Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_N-4R!H->F_4BrCClINOPSSi->C_N-Sp-4C=3C_Ext-4C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(0.315343,'m^3/(mol*s)'), n=2.015, w0=(323500,'J/mol'), E0=(44975.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_N-4R!H->F_4BrCClINOPSSi->C_N-Sp-4C=3C_Ext-4C-R_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_N-4R!H->F_4BrCClINOPSSi->C_N-Sp-4C=3C_Ext-4C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_N-4R!H->F_4BrCClINOPSSi->C_N-Sp-4C=3C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R-u1_N-3R->O_3BrCCl->C_Ext-3C-R_N-4R!H->F_4BrCClINOPSSi->C_N-Sp-4C=3C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 178,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_N-4R!H->Br_Sp-4CClFO-1C_Ext-1C-R_4CClFO->Cl",
    kinetics = ArrheniusBM(A=(1.58e+08,'m^3/(mol*s)'), n=0, w0=(323500,'J/mol'), E0=(81624.5,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_N-4R!H->Br_Sp-4CClFO-1C_Ext-1C-R_4CClFO->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_N-4R!H->Br_Sp-4CClFO-1C_Ext-1C-R_4CClFO->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_N-4R!H->Br_Sp-4CClFO-1C_Ext-1C-R_4CClFO->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_N-4R!H->Br_Sp-4CClFO-1C_Ext-1C-R_4CClFO->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 179,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_N-4R!H->Br_Sp-4CClFO-1C_Ext-1C-R_N-4CClFO->Cl",
    kinetics = ArrheniusBM(A=(91.9835,'m^3/(mol*s)'), n=1.70556, w0=(323500,'J/mol'), E0=(48212.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.9762786510383236, var=1.9925448608029321, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_N-4R!H->Br_Sp-4CClFO-1C_Ext-1C-R_N-4CClFO->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_N-4R!H->Br_Sp-4CClFO-1C_Ext-1C-R_N-4CClFO->Cl
    Total Standard Deviation in ln(k): 5.282795976661633"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_N-4R!H->Br_Sp-4CClFO-1C_Ext-1C-R_N-4CClFO->Cl
Total Standard Deviation in ln(k): 5.282795976661633""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_N-4R!H->Br_Sp-4CClFO-1C_Ext-1C-R_N-4CClFO->Cl
Total Standard Deviation in ln(k): 5.282795976661633
""",
)

entry(
    index = 180,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_6R!H->C_Ext-6C-R_7R!H->Cl",
    kinetics = ArrheniusBM(A=(8.17904e+06,'m^3/(mol*s)'), n=-0.248845, w0=(285000,'J/mol'), E0=(58424.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_6R!H->C_Ext-6C-R_7R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_6R!H->C_Ext-6C-R_7R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_6R!H->C_Ext-6C-R_7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_6R!H->C_Ext-6C-R_7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 181,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_6R!H->C_Ext-6C-R_N-7R!H->Cl",
    kinetics = ArrheniusBM(A=(1.31723e+07,'m^3/(mol*s)'), n=-0.422837, w0=(285000,'J/mol'), E0=(60969.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_6R!H->C_Ext-6C-R_N-7R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_6R!H->C_Ext-6C-R_N-7R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_6R!H->C_Ext-6C-R_N-7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_6R!H->C_Ext-6C-R_N-7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 182,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_6BrClFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(296.375,'m^3/(mol*s)'), n=0.948866, w0=(285000,'J/mol'), E0=(37779.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.030158223700273847, var=1.4044126320858221, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_6BrClFINOPSSi->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_6BrClFINOPSSi->Br
    Total Standard Deviation in ln(k): 2.4515442070056723"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_6BrClFINOPSSi->Br
Total Standard Deviation in ln(k): 2.4515442070056723""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_6BrClFINOPSSi->Br
Total Standard Deviation in ln(k): 2.4515442070056723
""",
)

entry(
    index = 183,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(5.01667e+07,'m^3/(mol*s)'), n=-0.401555, w0=(285000,'J/mol'), E0=(46003.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.02219720306696606, var=6.41284827163895, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br
    Total Standard Deviation in ln(k): 5.132483223805107"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br
Total Standard Deviation in ln(k): 5.132483223805107""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br
Total Standard Deviation in ln(k): 5.132483223805107
""",
)

entry(
    index = 184,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Ext-1C-R_Sp-4BrBrCCOO=3C",
    kinetics = ArrheniusBM(A=(1.06124e+08,'m^3/(mol*s)'), n=-0.284023, w0=(285000,'J/mol'), E0=(20956.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4825685360649426, var=0.8188613098559411, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Ext-1C-R_Sp-4BrBrCCOO=3C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Ext-1C-R_Sp-4BrBrCCOO=3C
    Total Standard Deviation in ln(k): 3.0265876936278273"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Ext-1C-R_Sp-4BrBrCCOO=3C
Total Standard Deviation in ln(k): 3.0265876936278273""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Ext-1C-R_Sp-4BrBrCCOO=3C
Total Standard Deviation in ln(k): 3.0265876936278273
""",
)

entry(
    index = 185,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Ext-1C-R_N-Sp-4BrBrCCOO=3C",
    kinetics = ArrheniusBM(A=(2.2587e+07,'m^3/(mol*s)'), n=-0.356712, w0=(285000,'J/mol'), E0=(35724.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Ext-1C-R_N-Sp-4BrBrCCOO=3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Ext-1C-R_N-Sp-4BrBrCCOO=3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Ext-1C-R_N-Sp-4BrBrCCOO=3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Ext-1C-R_N-Sp-4BrBrCCOO=3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 186,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C_3C-u1",
    kinetics = ArrheniusBM(A=(9711.02,'m^3/(mol*s)'), n=0.840447, w0=(285000,'J/mol'), E0=(53557.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1011385398188406, var=11.697533464705973, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C_3C-u1',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C_3C-u1
    Total Standard Deviation in ln(k): 7.110643097942282"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C_3C-u1
Total Standard Deviation in ln(k): 7.110643097942282""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C_3C-u1
Total Standard Deviation in ln(k): 7.110643097942282
""",
)

entry(
    index = 187,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C_N-3C-u1",
    kinetics = ArrheniusBM(A=(0.555662,'m^3/(mol*s)'), n=2.48693, w0=(285000,'J/mol'), E0=(41340,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0012288671781378285, var=13.37403770670558, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C_N-3C-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C_N-3C-u1
    Total Standard Deviation in ln(k): 7.334510326021607"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C_N-3C-u1
Total Standard Deviation in ln(k): 7.334510326021607""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C_N-3C-u1
Total Standard Deviation in ln(k): 7.334510326021607
""",
)

entry(
    index = 188,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Br_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.8349e+08,'m^3/(mol*s)'), n=-0.245613, w0=(237500,'J/mol'), E0=(58421.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.1599624390130727, var=11.095624400227553, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Br_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Br_Ext-1C-R
    Total Standard Deviation in ln(k): 14.617395739349835"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Br_Ext-1C-R
Total Standard Deviation in ln(k): 14.617395739349835""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Br_Ext-1C-R
Total Standard Deviation in ln(k): 14.617395739349835
""",
)

entry(
    index = 189,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_4R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.000149886,'m^3/(mol*s)'), n=3.33856, w0=(285000,'J/mol'), E0=(24310.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0550525557927264, var=0.09694733431833993, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_4R!H->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_4R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 0.7625246733983523"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 0.7625246733983523""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 0.7625246733983523
""",
)

entry(
    index = 190,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_4R!H->C_Sp-4C-1C",
    kinetics = ArrheniusBM(A=(0.000210316,'m^3/(mol*s)'), n=3.19938, w0=(285000,'J/mol'), E0=(47148.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.844872009599926, var=47.9134940114136, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_4R!H->C_Sp-4C-1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_4R!H->C_Sp-4C-1C
    Total Standard Deviation in ln(k): 26.049736020083678"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_4R!H->C_Sp-4C-1C
Total Standard Deviation in ln(k): 26.049736020083678""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_4R!H->C_Sp-4C-1C
Total Standard Deviation in ln(k): 26.049736020083678
""",
)

entry(
    index = 191,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_4R!H->C_N-Sp-4C-1C",
    kinetics = ArrheniusBM(A=(0.00310561,'m^3/(mol*s)'), n=2.96044, w0=(285000,'J/mol'), E0=(64461.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=5.951345885437872, var=77.07981759076687, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_4R!H->C_N-Sp-4C-1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_4R!H->C_N-Sp-4C-1C
    Total Standard Deviation in ln(k): 32.553724508054785"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_4R!H->C_N-Sp-4C-1C
Total Standard Deviation in ln(k): 32.553724508054785""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_4R!H->C_N-Sp-4C-1C
Total Standard Deviation in ln(k): 32.553724508054785
""",
)

entry(
    index = 192,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_N-4R!H->C_4BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(0.2494,'m^3/(mol*s)'), n=1.79792, w0=(285000,'J/mol'), E0=(46194.6,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_N-4R!H->C_4BrClFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_N-4R!H->C_4BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_N-4R!H->C_4BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_N-4R!H->C_4BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 193,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_N-4R!H->C_N-4BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(1.62378,'m^3/(mol*s)'), n=1.68039, w0=(285000,'J/mol'), E0=(41574,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.017540713297959292, var=1.9723799846239651, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_N-4R!H->C_N-4BrClFINOPSSi->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_N-4R!H->C_N-4BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 2.859551081668901"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_N-4R!H->C_N-4BrClFINOPSSi->O
Total Standard Deviation in ln(k): 2.859551081668901""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_N-4R!H->C_N-4BrClFINOPSSi->O
Total Standard Deviation in ln(k): 2.859551081668901
""",
)

entry(
    index = 194,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_N-3CO->C_Ext-1C-R_Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(2.00176e+10,'m^3/(mol*s)'), n=-1.24938, w0=(260050,'J/mol'), E0=(24964.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.10723471314629561, var=3.622216643860209, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_N-3CO->C_Ext-1C-R_Sp-4R!H-1C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_N-3CO->C_Ext-1C-R_Sp-4R!H-1C
    Total Standard Deviation in ln(k): 4.084870191592366"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_N-3CO->C_Ext-1C-R_Sp-4R!H-1C
Total Standard Deviation in ln(k): 4.084870191592366""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_N-3CO->C_Ext-1C-R_Sp-4R!H-1C
Total Standard Deviation in ln(k): 4.084870191592366
""",
)

entry(
    index = 195,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_N-3CO->C_Ext-1C-R_N-Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(3e+06,'m^3/(mol*s)'), n=0, w0=(260050,'J/mol'), E0=(26005,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_N-3CO->C_Ext-1C-R_N-Sp-4R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_N-3CO->C_Ext-1C-R_N-Sp-4R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_N-3CO->C_Ext-1C-R_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_N-3CO->C_Ext-1C-R_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 196,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_3CClH->H_Ext-1BrO-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1823.35,'m^3/(mol*s)'), n=1.55333, w0=(298550,'J/mol'), E0=(29855,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_3CClH->H_Ext-1BrO-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_3CClH->H_Ext-1BrO-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_3CClH->H_Ext-1BrO-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_3CClH->H_Ext-1BrO-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 197,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_N-3CClH->H_1BrO->Br_3CCl->C",
    kinetics = ArrheniusBM(A=(6.05e+06,'m^3/(mol*s)'), n=0, w0=(237500,'J/mol'), E0=(23750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_N-3CClH->H_1BrO->Br_3CCl->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_N-3CClH->H_1BrO->Br_3CCl->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_N-3CClH->H_1BrO->Br_3CCl->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_N-3CClH->H_1BrO->Br_3CCl->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 198,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_N-3CClH->H_1BrO->Br_N-3CCl->C",
    kinetics = ArrheniusBM(A=(2.81493e+09,'m^3/(mol*s)'), n=-0.232559, w0=(204420,'J/mol'), E0=(11817.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_N-3CClH->H_1BrO->Br_N-3CCl->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_N-3CClH->H_1BrO->Br_N-3CCl->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_N-3CClH->H_1BrO->Br_N-3CCl->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_N-3CClH->H_1BrO->Br_N-3CCl->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 199,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_N-3CClH->H_N-1BrO->Br_3CCl->C",
    kinetics = ArrheniusBM(A=(2.5163e+06,'m^3/(mol*s)'), n=-0.0374132, w0=(260050,'J/mol'), E0=(19503.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_N-3CClH->H_N-1BrO->Br_3CCl->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_N-3CClH->H_N-1BrO->Br_3CCl->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_N-3CClH->H_N-1BrO->Br_3CCl->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_N-3CClH->H_N-1BrO->Br_3CCl->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 200,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_N-3CClH->H_N-1BrO->Br_N-3CCl->C",
    kinetics = ArrheniusBM(A=(2.01522e+07,'m^3/(mol*s)'), n=-0.231972, w0=(226970,'J/mol'), E0=(-1645.85,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_N-3CClH->H_N-1BrO->Br_N-3CCl->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_N-3CClH->H_N-1BrO->Br_N-3CCl->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_N-3CClH->H_N-1BrO->Br_N-3CCl->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrClO->Cl_1BrO-u0_N-3R->Br_N-3CClHO->O_3CClH-u1_N-3CClH->H_N-1BrO->Br_N-3CCl->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 201,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_N-4R!H->Br_Sp-4CClFO-1C_Ext-1C-R_N-4CClFO->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(20,'m^3/(mol*s)'), n=2.01, w0=(323500,'J/mol'), E0=(43961.8,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_N-4R!H->Br_Sp-4CClFO-1C_Ext-1C-R_N-4CClFO->Cl_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_N-4R!H->Br_Sp-4CClFO-1C_Ext-1C-R_N-4CClFO->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_N-4R!H->Br_Sp-4CClFO-1C_Ext-1C-R_N-4CClFO->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_3BrCHO->H_Ext-1C-R_1C-u0_N-4R!H->Br_Sp-4CClFO-1C_Ext-1C-R_N-4CClFO->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 202,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_6BrClFINOPSSi->Br_5R!H->Cl",
    kinetics = ArrheniusBM(A=(190000,'m^3/(mol*s)'), n=0, w0=(285000,'J/mol'), E0=(33146.8,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_6BrClFINOPSSi->Br_5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_6BrClFINOPSSi->Br_5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_6BrClFINOPSSi->Br_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_6BrClFINOPSSi->Br_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 203,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_6BrClFINOPSSi->Br_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(983310,'m^3/(mol*s)'), n=0.0265125, w0=(285000,'J/mol'), E0=(55557.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_6BrClFINOPSSi->Br_N-5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_6BrClFINOPSSi->Br_N-5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_6BrClFINOPSSi->Br_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_6BrClFINOPSSi->Br_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 204,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_5R!H->Cl",
    kinetics = ArrheniusBM(A=(4.5e+06,'m^3/(mol*s)'), n=0, w0=(285000,'J/mol'), E0=(27289,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 205,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(8.99516e+06,'m^3/(mol*s)'), n=-0.199178, w0=(285000,'J/mol'), E0=(47716.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.01077840622221685, var=5.596237015184066, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl
    Total Standard Deviation in ln(k): 4.76955630349453"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl
Total Standard Deviation in ln(k): 4.76955630349453""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl
Total Standard Deviation in ln(k): 4.76955630349453
""",
)

entry(
    index = 206,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Ext-1C-R_Sp-4BrBrCCOO=3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.000544749,'m^3/(mol*s)'), n=3.34079, w0=(285000,'J/mol'), E0=(8153.36,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Ext-1C-R_Sp-4BrBrCCOO=3C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Ext-1C-R_Sp-4BrBrCCOO=3C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Ext-1C-R_Sp-4BrBrCCOO=3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Ext-1C-R_Sp-4BrBrCCOO=3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 207,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C_3C-u1_4BrCO->C",
    kinetics = ArrheniusBM(A=(88.2817,'m^3/(mol*s)'), n=1.57598, w0=(285000,'J/mol'), E0=(48272.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.6615732560133369, var=13.901923111760915, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C_3C-u1_4BrCO->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C_3C-u1_4BrCO->C
    Total Standard Deviation in ln(k): 9.136955785631626"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C_3C-u1_4BrCO->C
Total Standard Deviation in ln(k): 9.136955785631626""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C_3C-u1_4BrCO->C
Total Standard Deviation in ln(k): 9.136955785631626
""",
)

entry(
    index = 208,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C_3C-u1_N-4BrCO->C",
    kinetics = ArrheniusBM(A=(0.00466139,'m^3/(mol*s)'), n=2.28217, w0=(285000,'J/mol'), E0=(42042.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C_3C-u1_N-4BrCO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C_3C-u1_N-4BrCO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C_3C-u1_N-4BrCO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C_3C-u1_N-4BrCO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 209,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C_N-3C-u1_4BrCO->C",
    kinetics = ArrheniusBM(A=(0.0016727,'m^3/(mol*s)'), n=3.33083, w0=(285000,'J/mol'), E0=(30341.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C_N-3C-u1_4BrCO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C_N-3C-u1_4BrCO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C_N-3C-u1_4BrCO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C_N-3C-u1_4BrCO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 210,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C_N-3C-u1_N-4BrCO->C",
    kinetics = ArrheniusBM(A=(5.11215e-06,'m^3/(mol*s)'), n=3.81141, w0=(285000,'J/mol'), E0=(31398.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C_N-3C-u1_N-4BrCO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C_N-3C-u1_N-4BrCO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C_N-3C-u1_N-4BrCO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C_N-3C-u1_N-4BrCO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 211,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Br_Ext-1C-R_4CClF->Cl",
    kinetics = ArrheniusBM(A=(8.1e+07,'m^3/(mol*s)'), n=0, w0=(237500,'J/mol'), E0=(62615.9,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Br_Ext-1C-R_4CClF->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Br_Ext-1C-R_4CClF->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Br_Ext-1C-R_4CClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Br_Ext-1C-R_4CClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 212,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Br_Ext-1C-R_N-4CClF->Cl",
    kinetics = ArrheniusBM(A=(2.21335e+10,'m^3/(mol*s)'), n=-0.881783, w0=(237500,'J/mol'), E0=(23750,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Br_Ext-1C-R_N-4CClF->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Br_Ext-1C-R_N-4CClF->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Br_Ext-1C-R_N-4CClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_3BrCO->Br_1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->Br_Ext-1C-R_N-4CClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 213,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_4R!H->C_Ext-1C-R_Sp-4C=1C",
    kinetics = ArrheniusBM(A=(0.0713601,'m^3/(mol*s)'), n=2.71607, w0=(285000,'J/mol'), E0=(40112,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_4R!H->C_Ext-1C-R_Sp-4C=1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_4R!H->C_Ext-1C-R_Sp-4C=1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_4R!H->C_Ext-1C-R_Sp-4C=1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_4R!H->C_Ext-1C-R_Sp-4C=1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 214,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_4R!H->C_Ext-1C-R_N-Sp-4C=1C",
    kinetics = ArrheniusBM(A=(0.00808906,'m^3/(mol*s)'), n=2.74525, w0=(285000,'J/mol'), E0=(24580.1,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_4R!H->C_Ext-1C-R_N-Sp-4C=1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_4R!H->C_Ext-1C-R_N-Sp-4C=1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_4R!H->C_Ext-1C-R_N-Sp-4C=1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_4R!H->C_Ext-1C-R_N-Sp-4C=1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 215,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_4R!H->C_N-Sp-4C-1C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(0.00684122,'m^3/(mol*s)'), n=2.86155, w0=(285000,'J/mol'), E0=(65621,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_4R!H->C_N-Sp-4C-1C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_4R!H->C_N-Sp-4C-1C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_4R!H->C_N-Sp-4C-1C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_4R!H->C_N-Sp-4C-1C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 216,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_N-4R!H->C_N-4BrClFINOPSSi->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2765.11,'m^3/(mol*s)'), n=0.529263, w0=(285000,'J/mol'), E0=(41656.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.004051022901272474, var=0.1262580589853697, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_N-4R!H->C_N-4BrClFINOPSSi->O_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_N-4R!H->C_N-4BrClFINOPSSi->O_Ext-1C-R
    Total Standard Deviation in ln(k): 0.7225171565016609"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_N-4R!H->C_N-4BrClFINOPSSi->O_Ext-1C-R
Total Standard Deviation in ln(k): 0.7225171565016609""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_N-4R!H->C_N-4BrClFINOPSSi->O_Ext-1C-R
Total Standard Deviation in ln(k): 0.7225171565016609
""",
)

entry(
    index = 217,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_N-3CO->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(4.46955e+09,'m^3/(mol*s)'), n=-1.06011, w0=(260050,'J/mol'), E0=(22916.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.08904227460712978, var=3.722414873856955, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_N-3CO->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_N-3CO->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R
    Total Standard Deviation in ln(k): 4.0915721134426875"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_N-3CO->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 4.0915721134426875""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_N-3CO->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 4.0915721134426875
""",
)

entry(
    index = 218,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_Sp-5BrBrCCFF=1C",
    kinetics = ArrheniusBM(A=(1.35427e+10,'m^3/(mol*s)'), n=-0.860688, w0=(285000,'J/mol'), E0=(29855.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.18253676189438572, var=1.2339546971339515, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_Sp-5BrBrCCFF=1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_Sp-5BrBrCCFF=1C
    Total Standard Deviation in ln(k): 2.685565240458092"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_Sp-5BrBrCCFF=1C
Total Standard Deviation in ln(k): 2.685565240458092""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_Sp-5BrBrCCFF=1C
Total Standard Deviation in ln(k): 2.685565240458092
""",
)

entry(
    index = 219,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_N-Sp-5BrBrCCFF=1C",
    kinetics = ArrheniusBM(A=(6.18011e+06,'m^3/(mol*s)'), n=-0.151552, w0=(285000,'J/mol'), E0=(47428.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.004216011391249321, var=5.574723153445219, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_N-Sp-5BrBrCCFF=1C',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_N-Sp-5BrBrCCFF=1C
    Total Standard Deviation in ln(k): 4.7439432431885376"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_N-Sp-5BrBrCCFF=1C
Total Standard Deviation in ln(k): 4.7439432431885376""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_N-Sp-5BrBrCCFF=1C
Total Standard Deviation in ln(k): 4.7439432431885376
""",
)

entry(
    index = 220,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C_3C-u1_4BrCO->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.33708e-11,'m^3/(mol*s)'), n=5.36122, w0=(285000,'J/mol'), E0=(-1846.41,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1710217051851192, var=2.846816501450424, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C_3C-u1_4BrCO->C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C_3C-u1_4BrCO->C_Ext-3C-R
    Total Standard Deviation in ln(k): 3.8121943762452886"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C_3C-u1_4BrCO->C_Ext-3C-R
Total Standard Deviation in ln(k): 3.8121943762452886""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C_3C-u1_4BrCO->C_Ext-3C-R
Total Standard Deviation in ln(k): 3.8121943762452886
""",
)

entry(
    index = 221,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_N-4R!H->C_N-4BrClFINOPSSi->O_Ext-1C-R_4BrClF->Br",
    kinetics = ArrheniusBM(A=(525000,'m^3/(mol*s)'), n=0, w0=(285000,'J/mol'), E0=(56226.1,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_N-4R!H->C_N-4BrClFINOPSSi->O_Ext-1C-R_4BrClF->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_N-4R!H->C_N-4BrClFINOPSSi->O_Ext-1C-R_4BrClF->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_N-4R!H->C_N-4BrClFINOPSSi->O_Ext-1C-R_4BrClF->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_N-4R!H->C_N-4BrClFINOPSSi->O_Ext-1C-R_4BrClF->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 222,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_N-4R!H->C_N-4BrClFINOPSSi->O_Ext-1C-R_N-4BrClF->Br",
    kinetics = ArrheniusBM(A=(1423.77,'m^3/(mol*s)'), n=0.511016, w0=(285000,'J/mol'), E0=(33764,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.8097316446742169, var=6.752236675016292, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_N-4R!H->C_N-4BrClFINOPSSi->O_Ext-1C-R_N-4BrClF->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_N-4R!H->C_N-4BrClFINOPSSi->O_Ext-1C-R_N-4BrClF->Br
    Total Standard Deviation in ln(k): 9.756381811845758"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_N-4R!H->C_N-4BrClFINOPSSi->O_Ext-1C-R_N-4BrClF->Br
Total Standard Deviation in ln(k): 9.756381811845758""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_N-4R!H->C_N-4BrClFINOPSSi->O_Ext-1C-R_N-4BrClF->Br
Total Standard Deviation in ln(k): 9.756381811845758
""",
)

entry(
    index = 223,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_N-3CO->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(3.15e+06,'m^3/(mol*s)'), n=0, w0=(260050,'J/mol'), E0=(12950.8,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_N-3CO->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_4R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_N-3CO->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_4R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_N-3CO->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_N-3CO->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 224,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_N-3CO->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(7.47688e+07,'m^3/(mol*s)'), n=-0.579909, w0=(260050,'J/mol'), E0=(21822.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.286637805163859, var=11.097030364400412, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_N-3CO->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_N-4R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_N-3CO->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 12.423535809131273"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_N-3CO->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 12.423535809131273""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_N-3CO->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 12.423535809131273
""",
)

entry(
    index = 225,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_Sp-5BrBrCCFF=1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(285000,'J/mol'), E0=(19101.1,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_Sp-5BrBrCCFF=1C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_Sp-5BrBrCCFF=1C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_Sp-5BrBrCCFF=1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_Sp-5BrBrCCFF=1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 226,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_N-Sp-5BrBrCCFF=1C_Ext-5BrCF-R",
    kinetics = ArrheniusBM(A=(1.19739e+07,'m^3/(mol*s)'), n=-0.209077, w0=(285000,'J/mol'), E0=(59250.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00010567658566274231, var=1.3141291266138428, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_N-Sp-5BrBrCCFF=1C_Ext-5BrCF-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_N-Sp-5BrBrCCFF=1C_Ext-5BrCF-R
    Total Standard Deviation in ln(k): 2.298403022119452"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_N-Sp-5BrBrCCFF=1C_Ext-5BrCF-R
Total Standard Deviation in ln(k): 2.298403022119452""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_N-Sp-5BrBrCCFF=1C_Ext-5BrCF-R
Total Standard Deviation in ln(k): 2.298403022119452
""",
)

entry(
    index = 227,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_N-Sp-5BrBrCCFF=1C_5BrCF->Br",
    kinetics = ArrheniusBM(A=(168.912,'m^3/(mol*s)'), n=1.10649, w0=(285000,'J/mol'), E0=(36596.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.030493072284775935, var=1.830747768929601, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_N-Sp-5BrBrCCFF=1C_5BrCF->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_N-Sp-5BrBrCCFF=1C_5BrCF->Br
    Total Standard Deviation in ln(k): 2.7891251239794403"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_N-Sp-5BrBrCCFF=1C_5BrCF->Br
Total Standard Deviation in ln(k): 2.7891251239794403""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_N-Sp-5BrBrCCFF=1C_5BrCF->Br
Total Standard Deviation in ln(k): 2.7891251239794403
""",
)

entry(
    index = 228,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_N-Sp-5BrBrCCFF=1C_N-5BrCF->Br",
    kinetics = ArrheniusBM(A=(1.00704e+07,'m^3/(mol*s)'), n=-0.0883209, w0=(285000,'J/mol'), E0=(28027.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.233591473066516, var=10.313558517300883, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_N-Sp-5BrBrCCFF=1C_N-5BrCF->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_N-Sp-5BrBrCCFF=1C_N-5BrCF->Br
    Total Standard Deviation in ln(k): 12.050191352740402"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_N-Sp-5BrBrCCFF=1C_N-5BrCF->Br
Total Standard Deviation in ln(k): 12.050191352740402""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_N-Sp-5BrBrCCFF=1C_N-5BrCF->Br
Total Standard Deviation in ln(k): 12.050191352740402
""",
)

entry(
    index = 229,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C_3C-u1_4BrCO->C_Ext-3C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(0.00230719,'m^3/(mol*s)'), n=2.96161, w0=(285000,'J/mol'), E0=(37850.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C_3C-u1_4BrCO->C_Ext-3C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C_3C-u1_4BrCO->C_Ext-3C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C_3C-u1_4BrCO->C_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C_3C-u1_4BrCO->C_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 230,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C_3C-u1_4BrCO->C_Ext-3C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(4.68481e-07,'m^3/(mol*s)'), n=3.98461, w0=(285000,'J/mol'), E0=(13071.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C_3C-u1_4BrCO->C_Ext-3C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C_3C-u1_4BrCO->C_Ext-3C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C_3C-u1_4BrCO->C_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_N-4R!H->F_N-4BrCClO->Cl_Sp-4BrCO-3C_3C-u1_4BrCO->C_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 231,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_N-4R!H->C_N-4BrClFINOPSSi->O_Ext-1C-R_N-4BrClF->Br_4ClF->Cl",
    kinetics = ArrheniusBM(A=(100000,'m^3/(mol*s)'), n=0, w0=(285000,'J/mol'), E0=(40049.9,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_N-4R!H->C_N-4BrClFINOPSSi->O_Ext-1C-R_N-4BrClF->Br_4ClF->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_N-4R!H->C_N-4BrClFINOPSSi->O_Ext-1C-R_N-4BrClF->Br_4ClF->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_N-4R!H->C_N-4BrClFINOPSSi->O_Ext-1C-R_N-4BrClF->Br_4ClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_N-4R!H->C_N-4BrClFINOPSSi->O_Ext-1C-R_N-4BrClF->Br_4ClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 232,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_N-4R!H->C_N-4BrClFINOPSSi->O_Ext-1C-R_N-4BrClF->Br_N-4ClF->Cl",
    kinetics = ArrheniusBM(A=(0.277,'m^3/(mol*s)'), n=2.05, w0=(285000,'J/mol'), E0=(36034.4,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_N-4R!H->C_N-4BrClFINOPSSi->O_Ext-1C-R_N-4BrClF->Br_N-4ClF->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_N-4R!H->C_N-4BrClFINOPSSi->O_Ext-1C-R_N-4BrClF->Br_N-4ClF->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_N-4R!H->C_N-4BrClFINOPSSi->O_Ext-1C-R_N-4BrClF->Br_N-4ClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_3CO->C_Ext-1C-R_N-4R!H->C_N-4BrClFINOPSSi->O_Ext-1C-R_N-4BrClF->Br_N-4ClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 233,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_N-3CO->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_N-4R!H->Cl_4BrCF->Br",
    kinetics = ArrheniusBM(A=(1.58e+06,'m^3/(mol*s)'), n=0, w0=(260050,'J/mol'), E0=(24424.8,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_N-3CO->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_N-4R!H->Cl_4BrCF->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_N-3CO->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_N-4R!H->Cl_4BrCF->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_N-3CO->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_N-4R!H->Cl_4BrCF->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_N-3CO->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_N-4R!H->Cl_4BrCF->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 234,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_N-3CO->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_N-4R!H->Cl_N-4BrCF->Br",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(260050,'J/mol'), E0=(18242.2,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_N-3CO->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_N-4R!H->Cl_N-4BrCF->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_N-3CO->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_N-4R!H->Cl_N-4BrCF->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_N-3CO->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_N-4R!H->Cl_N-4BrCF->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_N-3BrCO->Br_3CO-u1_1C-u0_N-3CO->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R_N-4R!H->Cl_N-4BrCF->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 235,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_N-Sp-5BrBrCCFF=1C_Ext-5BrCF-R_7R!H->Cl",
    kinetics = ArrheniusBM(A=(3e+06,'m^3/(mol*s)'), n=0, w0=(285000,'J/mol'), E0=(56374.6,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_N-Sp-5BrBrCCFF=1C_Ext-5BrCF-R_7R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_N-Sp-5BrBrCCFF=1C_Ext-5BrCF-R_7R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_N-Sp-5BrBrCCFF=1C_Ext-5BrCF-R_7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_N-Sp-5BrBrCCFF=1C_Ext-5BrCF-R_7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 236,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_N-Sp-5BrBrCCFF=1C_Ext-5BrCF-R_N-7R!H->Cl",
    kinetics = ArrheniusBM(A=(1.5e+06,'m^3/(mol*s)'), n=0, w0=(285000,'J/mol'), E0=(57359.3,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_N-Sp-5BrBrCCFF=1C_Ext-5BrCF-R_N-7R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_N-Sp-5BrBrCCFF=1C_Ext-5BrCF-R_N-7R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_N-Sp-5BrBrCCFF=1C_Ext-5BrCF-R_N-7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_N-Sp-5BrBrCCFF=1C_Ext-5BrCF-R_N-7R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 237,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_N-Sp-5BrBrCCFF=1C_5BrCF->Br_6ClF->Cl",
    kinetics = ArrheniusBM(A=(369675,'m^3/(mol*s)'), n=0.00876838, w0=(285000,'J/mol'), E0=(33090.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_N-Sp-5BrBrCCFF=1C_5BrCF->Br_6ClF->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_N-Sp-5BrBrCCFF=1C_5BrCF->Br_6ClF->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_N-Sp-5BrBrCCFF=1C_5BrCF->Br_6ClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_N-Sp-5BrBrCCFF=1C_5BrCF->Br_6ClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 238,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_N-Sp-5BrBrCCFF=1C_5BrCF->Br_N-6ClF->Cl",
    kinetics = ArrheniusBM(A=(2.25e+06,'m^3/(mol*s)'), n=0, w0=(285000,'J/mol'), E0=(55813.6,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_N-Sp-5BrBrCCFF=1C_5BrCF->Br_N-6ClF->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_N-Sp-5BrBrCCFF=1C_5BrCF->Br_N-6ClF->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_N-Sp-5BrBrCCFF=1C_5BrCF->Br_N-6ClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_N-Sp-5BrBrCCFF=1C_5BrCF->Br_N-6ClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 239,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_N-Sp-5BrBrCCFF=1C_N-5BrCF->Br_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.82637e+06,'m^3/(mol*s)'), n=0.0352809, w0=(285000,'J/mol'), E0=(26964.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_N-Sp-5BrBrCCFF=1C_N-5BrCF->Br_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_N-Sp-5BrBrCCFF=1C_N-5BrCF->Br_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_N-Sp-5BrBrCCFF=1C_N-5BrCF->Br_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->Cl_N-3BrCHO->H_Ext-3BrCO-R_3BrCO->C_4R!H->F_Ext-1C-R_Ext-3C-R_N-6R!H->C_N-6BrClFINOPSSi->Br_N-5R!H->Cl_N-Sp-5BrBrCCFF=1C_N-5BrCF->Br_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

