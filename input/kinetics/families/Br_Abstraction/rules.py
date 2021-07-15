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
    kinetics = ArrheniusBM(A=(3641.86,'m^3/(mol*s)'), n=1.15013, w0=(286523,'J/mol'), E0=(51784.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06941792876817682, var=9.439271592884126, Tref=1000.0, N=104, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 104 training reactions at node Root
    Total Standard Deviation in ln(k): 6.333644190389708"""),
    rank = 11,
    shortDesc = """BM rule fitted to 104 training reactions at node Root
Total Standard Deviation in ln(k): 6.333644190389708""",
    longDesc = 
"""
BM rule fitted to 104 training reactions at node Root
Total Standard Deviation in ln(k): 6.333644190389708
""",
)

entry(
    index = 2,
    label = "Root_1R->H",
    kinetics = ArrheniusBM(A=(33.9831,'m^3/(mol*s)'), n=1.64326, w0=(316486,'J/mol'), E0=(50708.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.28025767281628633, var=7.659761769979992, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_1R->H',), comment="""BM rule fitted to 21 training reactions at node Root_1R->H
    Total Standard Deviation in ln(k): 6.2525248618730345"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_1R->H
Total Standard Deviation in ln(k): 6.2525248618730345""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_1R->H
Total Standard Deviation in ln(k): 6.2525248618730345
""",
)

entry(
    index = 3,
    label = "Root_N-1R->H",
    kinetics = ArrheniusBM(A=(1.11576e+06,'m^3/(mol*s)'), n=0.454266, w0=(278942,'J/mol'), E0=(56407,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.09429053985732985, var=10.908499635488736, Tref=1000.0, N=83, data_mean=0.0, correlation='Root_N-1R->H',), comment="""BM rule fitted to 83 training reactions at node Root_N-1R->H
    Total Standard Deviation in ln(k): 6.858153497596138"""),
    rank = 11,
    shortDesc = """BM rule fitted to 83 training reactions at node Root_N-1R->H
Total Standard Deviation in ln(k): 6.858153497596138""",
    longDesc = 
"""
BM rule fitted to 83 training reactions at node Root_N-1R->H
Total Standard Deviation in ln(k): 6.858153497596138
""",
)

entry(
    index = 4,
    label = "Root_1R->H_3R->C",
    kinetics = ArrheniusBM(A=(1.21379e-16,'m^3/(mol*s)'), n=6.79619, w0=(323500,'J/mol'), E0=(-24479,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.9522047950906147, var=19.167477174691584, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_1R->H_3R->C',), comment="""BM rule fitted to 16 training reactions at node Root_1R->H_3R->C
    Total Standard Deviation in ln(k): 18.70702878017282"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_1R->H_3R->C
Total Standard Deviation in ln(k): 18.70702878017282""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_1R->H_3R->C
Total Standard Deviation in ln(k): 18.70702878017282
""",
)

entry(
    index = 5,
    label = "Root_1R->H_N-3R->C",
    kinetics = ArrheniusBM(A=(0.0300208,'m^3/(mol*s)'), n=2.83224, w0=(294040,'J/mol'), E0=(29404,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06439687131480729, var=3.1025923240295956, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->H_N-3R->C',), comment="""BM rule fitted to 5 training reactions at node Root_1R->H_N-3R->C
    Total Standard Deviation in ln(k): 3.6929770391205907"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->H_N-3R->C
Total Standard Deviation in ln(k): 3.6929770391205907""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->H_N-3R->C
Total Standard Deviation in ln(k): 3.6929770391205907
""",
)

entry(
    index = 6,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(5.66711e+09,'m^3/(mol*s)'), n=-0.657053, w0=(287933,'J/mol'), E0=(62136.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.18763251013457058, var=9.369703271062747, Tref=1000.0, N=61, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C',), comment="""BM rule fitted to 61 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 6.60792673398543"""),
    rank = 11,
    shortDesc = """BM rule fitted to 61 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 6.60792673398543""",
    longDesc = 
"""
BM rule fitted to 61 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 6.60792673398543
""",
)

entry(
    index = 7,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C",
    kinetics = ArrheniusBM(A=(3.97788e-08,'m^3/(mol*s)'), n=4.59722, w0=(254014,'J/mol'), E0=(-1914.63,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.26882676921344945, var=77.48427425268802, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C',), comment="""BM rule fitted to 22 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C
    Total Standard Deviation in ln(k): 18.322155180771844"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 18.322155180771844""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C
Total Standard Deviation in ln(k): 18.322155180771844
""",
)

entry(
    index = 8,
    label = "Root_1R->H_3R->C_3C-u1",
    kinetics = ArrheniusBM(A=(2.39281e-12,'m^3/(mol*s)'), n=5.3906, w0=(323500,'J/mol'), E0=(3750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.021428799404749913, var=3.503759133984028, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1',), comment="""BM rule fitted to 10 training reactions at node Root_1R->H_3R->C_3C-u1
    Total Standard Deviation in ln(k): 3.8063706682765073"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_1R->H_3R->C_3C-u1
Total Standard Deviation in ln(k): 3.8063706682765073""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_1R->H_3R->C_3C-u1
Total Standard Deviation in ln(k): 3.8063706682765073
""",
)

entry(
    index = 9,
    label = "Root_1R->H_3R->C_N-3C-u1",
    kinetics = ArrheniusBM(A=(3.78271e-13,'m^3/(mol*s)'), n=5.84088, w0=(323500,'J/mol'), E0=(1300.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4412204251320279, var=2.9448563798723586, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R->H_3R->C_N-3C-u1',), comment="""BM rule fitted to 6 training reactions at node Root_1R->H_3R->C_N-3C-u1
    Total Standard Deviation in ln(k): 4.548836471760612"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R->H_3R->C_N-3C-u1
Total Standard Deviation in ln(k): 4.548836471760612""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R->H_3R->C_N-3C-u1
Total Standard Deviation in ln(k): 4.548836471760612
""",
)

entry(
    index = 10,
    label = "Root_1R->H_N-3R->C_Ext-3BrHO-R",
    kinetics = ArrheniusBM(A=(0.02722,'m^3/(mol*s)'), n=2.84724, w0=(298550,'J/mol'), E0=(29855,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.2325603151022477, var=5.2097791213440425, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-3R->C_Ext-3BrHO-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->C_Ext-3BrHO-R
    Total Standard Deviation in ln(k): 7.672681114320994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->C_Ext-3BrHO-R
Total Standard Deviation in ln(k): 7.672681114320994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->C_Ext-3BrHO-R
Total Standard Deviation in ln(k): 7.672681114320994
""",
)

entry(
    index = 11,
    label = "Root_1R->H_N-3R->C_3BrHO-u1",
    kinetics = ArrheniusBM(A=(10474.4,'m^3/(mol*s)'), n=1.0453, w0=(287275,'J/mol'), E0=(28727.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2753520931965579, var=10.676287333689414, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-3R->C_3BrHO-u1',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->C_3BrHO-u1
    Total Standard Deviation in ln(k): 7.242228799834179"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->C_3BrHO-u1
Total Standard Deviation in ln(k): 7.242228799834179""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-3R->C_3BrHO-u1
Total Standard Deviation in ln(k): 7.242228799834179
""",
)

entry(
    index = 12,
    label = "Root_1R->H_N-3R->C_N-3BrHO-u1",
    kinetics = ArrheniusBM(A=(4375.31,'m^3/(mol*s)'), n=0.580548, w0=(298550,'J/mol'), E0=(29855,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->C_N-3BrHO-u1',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_N-3BrHO-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_N-3BrHO-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_N-3BrHO-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_3R->H",
    kinetics = ArrheniusBM(A=(0.0447273,'m^3/(mol*s)'), n=2.7341, w0=(323500,'J/mol'), E0=(31850.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06303502755114296, var=1.2352186279237474, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_3R->H',), comment="""BM rule fitted to 16 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H
    Total Standard Deviation in ln(k): 2.3864498487793133"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H
Total Standard Deviation in ln(k): 2.3864498487793133""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H
Total Standard Deviation in ln(k): 2.3864498487793133
""",
)

entry(
    index = 14,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H",
    kinetics = ArrheniusBM(A=(1.15233e+11,'m^3/(mol*s)'), n=-1.09051, w0=(275287,'J/mol'), E0=(67304.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.23958505809312297, var=12.653447924284183, Tref=1000.0, N=45, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H',), comment="""BM rule fitted to 45 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H
    Total Standard Deviation in ln(k): 7.733153028587053"""),
    rank = 11,
    shortDesc = """BM rule fitted to 45 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H
Total Standard Deviation in ln(k): 7.733153028587053""",
    longDesc = 
"""
BM rule fitted to 45 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H
Total Standard Deviation in ln(k): 7.733153028587053
""",
)

entry(
    index = 15,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0",
    kinetics = ArrheniusBM(A=(2.959e-08,'m^3/(mol*s)'), n=4.64071, w0=(252768,'J/mol'), E0=(-2451.77,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.24152087740527578, var=81.91855719511985, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0',), comment="""BM rule fitted to 17 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0
    Total Standard Deviation in ln(k): 18.751467215017122"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0
Total Standard Deviation in ln(k): 18.751467215017122""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0
Total Standard Deviation in ln(k): 18.751467215017122
""",
)

entry(
    index = 16,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrO-u0",
    kinetics = ArrheniusBM(A=(1.1799e+08,'m^3/(mol*s)'), n=-0.638678, w0=(258250,'J/mol'), E0=(8098.88,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.9029654357561454, var=4.681195006334862, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrO-u0',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrO-u0
    Total Standard Deviation in ln(k): 6.606216109772695"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrO-u0
Total Standard Deviation in ln(k): 6.606216109772695""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrO-u0
Total Standard Deviation in ln(k): 6.606216109772695
""",
)

entry(
    index = 17,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.48031e-12,'m^3/(mol*s)'), n=5.34818, w0=(323500,'J/mol'), E0=(19543.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07893269652893749, var=4.062952290441803, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R',), comment="""BM rule fitted to 8 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R
    Total Standard Deviation in ln(k): 4.239221009777108"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R
Total Standard Deviation in ln(k): 4.239221009777108""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R
Total Standard Deviation in ln(k): 4.239221009777108
""",
)

entry(
    index = 18,
    label = "Root_1R->H_3R->C_N-3C-u1_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.11452e-12,'m^3/(mol*s)'), n=5.58476, w0=(323500,'J/mol'), E0=(-1324.26,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5383289232720325, var=4.86347601177787, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->H_3R->C_N-3C-u1_Ext-3C-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->H_3R->C_N-3C-u1_Ext-3C-R
    Total Standard Deviation in ln(k): 5.773685643999156"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->H_3R->C_N-3C-u1_Ext-3C-R
Total Standard Deviation in ln(k): 5.773685643999156""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->H_3R->C_N-3C-u1_Ext-3C-R
Total Standard Deviation in ln(k): 5.773685643999156
""",
)

entry(
    index = 19,
    label = "Root_1R->H_N-3R->C_Ext-3BrHO-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(0.00532831,'m^3/(mol*s)'), n=2.77064, w0=(298550,'J/mol'), E0=(29855,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->C_Ext-3BrHO-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_Ext-3BrHO-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_Ext-3BrHO-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_Ext-3BrHO-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_1R->H_N-3R->C_3BrHO-u1_3BrHO->Br",
    kinetics = ArrheniusBM(A=(32771.6,'m^3/(mol*s)'), n=1.02226, w0=(276000,'J/mol'), E0=(27600,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->C_3BrHO-u1_3BrHO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_3BrHO-u1_3BrHO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_3BrHO-u1_3BrHO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_3BrHO-u1_3BrHO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_1R->H_N-3R->C_3BrHO-u1_N-3BrHO->Br",
    kinetics = ArrheniusBM(A=(2.94325e+06,'m^3/(mol*s)'), n=0.0216725, w0=(298550,'J/mol'), E0=(29855,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-3R->C_3BrHO-u1_N-3BrHO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_3BrHO-u1_N-3BrHO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_3BrHO-u1_N-3BrHO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-3R->C_3BrHO-u1_N-3BrHO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0",
    kinetics = ArrheniusBM(A=(1.1486,'m^3/(mol*s)'), n=2.40599, w0=(323500,'J/mol'), E0=(42362.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.005910038215410101, var=1.431865786755239, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0
    Total Standard Deviation in ln(k): 2.413727253294168"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0
Total Standard Deviation in ln(k): 2.413727253294168""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0
Total Standard Deviation in ln(k): 2.413727253294168
""",
)

entry(
    index = 23,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_N-1C-u0",
    kinetics = ArrheniusBM(A=(0.0250039,'m^3/(mol*s)'), n=2.7119, w0=(323500,'J/mol'), E0=(25680.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1996470102010613, var=1.8919201021035779, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_N-1C-u0',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_N-1C-u0
    Total Standard Deviation in ln(k): 3.2590803459656073"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_N-1C-u0
Total Standard Deviation in ln(k): 3.2590803459656073""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_N-1C-u0
Total Standard Deviation in ln(k): 3.2590803459656073
""",
)

entry(
    index = 24,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R",
    kinetics = ArrheniusBM(A=(34.7124,'m^3/(mol*s)'), n=1.77334, w0=(283752,'J/mol'), E0=(51286.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.12052598392718872, var=21.95167596132344, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R',), comment="""BM rule fitted to 20 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R
    Total Standard Deviation in ln(k): 9.695537317640456"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R
Total Standard Deviation in ln(k): 9.695537317640456""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R
Total Standard Deviation in ln(k): 9.695537317640456
""",
)

entry(
    index = 25,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_3BrCO->Br",
    kinetics = ArrheniusBM(A=(1.5389e+31,'m^3/(mol*s)'), n=-7.15133, w0=(237500,'J/mol'), E0=(68544.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.7922908921257092, var=41.65581510980468, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_3BrCO->Br',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_3BrCO->Br
    Total Standard Deviation in ln(k): 19.954630336334098"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_3BrCO->Br
Total Standard Deviation in ln(k): 19.954630336334098""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_3BrCO->Br
Total Standard Deviation in ln(k): 19.954630336334098
""",
)

entry(
    index = 26,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br",
    kinetics = ArrheniusBM(A=(1.26031e+21,'m^3/(mol*s)'), n=-4.1121, w0=(276268,'J/mol'), E0=(83343.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.36944202599197734, var=8.75222757257289, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br',), comment="""BM rule fitted to 20 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br
    Total Standard Deviation in ln(k): 6.859087419214285"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br
Total Standard Deviation in ln(k): 6.859087419214285""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br
Total Standard Deviation in ln(k): 6.859087419214285
""",
)

entry(
    index = 27,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R",
    kinetics = ArrheniusBM(A=(8.55192e-30,'m^3/(mol*s)'), n=10.7701, w0=(250386,'J/mol'), E0=(10115.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=7.703299584817925, var=126.40098043477992, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R
    Total Standard Deviation in ln(k): 41.893897822517765"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R
Total Standard Deviation in ln(k): 41.893897822517765""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R
Total Standard Deviation in ln(k): 41.893897822517765
""",
)

entry(
    index = 28,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_3R->O",
    kinetics = ArrheniusBM(A=(6.55098e+07,'m^3/(mol*s)'), n=-0.354233, w0=(212550,'J/mol'), E0=(-4137.68,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.14028945735713552, var=0.07386226843174754, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_3R->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_3R->O
    Total Standard Deviation in ln(k): 0.8973252280263948"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_3R->O
Total Standard Deviation in ln(k): 0.8973252280263948""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_3R->O
Total Standard Deviation in ln(k): 0.8973252280263948
""",
)

entry(
    index = 29,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O",
    kinetics = ArrheniusBM(A=(2186.05,'m^3/(mol*s)'), n=1.55089, w0=(264906,'J/mol'), E0=(19507,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.008851399794162208, var=0.28773210831891893, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O
    Total Standard Deviation in ln(k): 1.0975929514282303"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O
Total Standard Deviation in ln(k): 1.0975929514282303""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O
Total Standard Deviation in ln(k): 1.0975929514282303
""",
)

entry(
    index = 30,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrO-u0_3R->Br",
    kinetics = ArrheniusBM(A=(3.48226e+08,'m^3/(mol*s)'), n=-0.558288, w0=(212550,'J/mol'), E0=(13124.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrO-u0_3R->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrO-u0_3R->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrO-u0_3R->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrO-u0_3R->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrO-u0_N-3R->Br",
    kinetics = ArrheniusBM(A=(5.1331e+08,'m^3/(mol*s)'), n=-0.875041, w0=(269675,'J/mol'), E0=(21176.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.36665426589522254, var=1.806477459471323, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrO-u0_N-3R->Br',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrO-u0_N-3R->Br
    Total Standard Deviation in ln(k): 3.6157113178332505"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrO-u0_N-3R->Br
Total Standard Deviation in ln(k): 3.6157113178332505""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrO-u0_N-3R->Br
Total Standard Deviation in ln(k): 3.6157113178332505
""",
)

entry(
    index = 32,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(0.078788,'m^3/(mol*s)'), n=1.96376, w0=(323500,'J/mol'), E0=(49274.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_4R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_4R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(14.6313,'m^3/(mol*s)'), n=1.56959, w0=(323500,'J/mol'), E0=(53679.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.002119825765990429, var=4.036098048483923, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-4R!H->Cl',), comment="""BM rule fitted to 7 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 4.032847472013547"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 4.032847472013547""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 4.032847472013547
""",
)

entry(
    index = 34,
    label = "Root_1R->H_3R->C_N-3C-u1_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(9.60134e-09,'m^3/(mol*s)'), n=4.763, w0=(323500,'J/mol'), E0=(16711.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R->C_N-3C-u1_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_N-3C-u1_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_N-3C-u1_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_N-3C-u1_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 35,
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
    index = 36,
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
    index = 37,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.524433,'m^3/(mol*s)'), n=2.49244, w0=(323500,'J/mol'), E0=(40679.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.02379587517552979, var=2.253343019089903, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0_Ext-1C-R',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0_Ext-1C-R
    Total Standard Deviation in ln(k): 3.0691243738841116"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 3.0691243738841116""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 3.0691243738841116
""",
)

entry(
    index = 38,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_N-1C-u0_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.98282e-06,'m^3/(mol*s)'), n=3.84125, w0=(323500,'J/mol'), E0=(13658.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2779741605534091, var=1.8474209462856896, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_N-1C-u0_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_N-1C-u0_Ext-1C-R
    Total Standard Deviation in ln(k): 3.4232607322727504"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_N-1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 3.4232607322727504""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_N-1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 3.4232607322727504
""",
)

entry(
    index = 39,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_3BrCO->O",
    kinetics = ArrheniusBM(A=(0.000210828,'m^3/(mol*s)'), n=3.57193, w0=(260050,'J/mol'), E0=(26005,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_3BrCO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_3BrCO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_3BrCO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_3BrCO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 40,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O",
    kinetics = ArrheniusBM(A=(1.0161e+24,'m^3/(mol*s)'), n=-4.89192, w0=(285000,'J/mol'), E0=(93005.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.43158434799223294, var=16.145649800435297, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O',), comment="""BM rule fitted to 19 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O
    Total Standard Deviation in ln(k): 9.139739064550286"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O
Total Standard Deviation in ln(k): 9.139739064550286""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O
Total Standard Deviation in ln(k): 9.139739064550286
""",
)

entry(
    index = 41,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_3BrCO->Br_1C-u0",
    kinetics = ArrheniusBM(A=(5.44329e+18,'m^3/(mol*s)'), n=-3.21804, w0=(237500,'J/mol'), E0=(57087.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.300434693363986, var=40.29087132777154, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_3BrCO->Br_1C-u0',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_3BrCO->Br_1C-u0
    Total Standard Deviation in ln(k): 21.01762355710426"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_3BrCO->Br_1C-u0
Total Standard Deviation in ln(k): 21.01762355710426""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_3BrCO->Br_1C-u0
Total Standard Deviation in ln(k): 21.01762355710426
""",
)

entry(
    index = 42,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_3BrCO->Br_N-1C-u0",
    kinetics = ArrheniusBM(A=(5000,'m^3/(mol*s)'), n=0, w0=(237500,'J/mol'), E0=(23750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_3BrCO->Br_N-1C-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_3BrCO->Br_N-1C-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_3BrCO->Br_N-1C-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_3BrCO->Br_N-1C-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 43,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0",
    kinetics = ArrheniusBM(A=(1.50843,'m^3/(mol*s)'), n=2.02721, w0=(274084,'J/mol'), E0=(48178.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06523034992535032, var=7.592615369359121, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0',), comment="""BM rule fitted to 16 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0
    Total Standard Deviation in ln(k): 5.687882878416081"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0
Total Standard Deviation in ln(k): 5.687882878416081""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0
Total Standard Deviation in ln(k): 5.687882878416081
""",
)

entry(
    index = 44,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_N-1C-u0",
    kinetics = ArrheniusBM(A=(2.40279e+25,'m^3/(mol*s)'), n=-5.31366, w0=(285000,'J/mol'), E0=(79643.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.44309165403282924, var=7.090544534240762, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_N-1C-u0',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_N-1C-u0
    Total Standard Deviation in ln(k): 6.451519495892753"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_N-1C-u0
Total Standard Deviation in ln(k): 6.451519495892753""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_N-1C-u0
Total Standard Deviation in ln(k): 6.451519495892753
""",
)

entry(
    index = 45,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_Ext-1BrO-R",
    kinetics = ArrheniusBM(A=(0.00322504,'m^3/(mol*s)'), n=2.9284, w0=(260050,'J/mol'), E0=(26005,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_Ext-1BrO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_Ext-1BrO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_Ext-1BrO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_Ext-1BrO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_Ext-3R-R",
    kinetics = ArrheniusBM(A=(404904,'m^3/(mol*s)'), n=0.0717696, w0=(248775,'J/mol'), E0=(4810.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.501833267386881, var=0.03703918853040752, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_Ext-3R-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_Ext-3R-R
    Total Standard Deviation in ln(k): 1.6467102578214547"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_Ext-3R-R
Total Standard Deviation in ln(k): 1.6467102578214547""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_Ext-3R-R
Total Standard Deviation in ln(k): 1.6467102578214547
""",
)

entry(
    index = 47,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_1BrO->Br",
    kinetics = ArrheniusBM(A=(6.14681e+08,'m^3/(mol*s)'), n=-0.527905, w0=(237500,'J/mol'), E0=(30474.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.35024040011199753, var=0.2620792632022212, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_1BrO->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_1BrO->Br
    Total Standard Deviation in ln(k): 1.9062986186992787"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_1BrO->Br
Total Standard Deviation in ln(k): 1.9062986186992787""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_1BrO->Br
Total Standard Deviation in ln(k): 1.9062986186992787
""",
)

entry(
    index = 48,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_N-1BrO->Br",
    kinetics = ArrheniusBM(A=(3.56665e+14,'m^3/(mol*s)'), n=-2.54977, w0=(260050,'J/mol'), E0=(-10277.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.620107419366252, var=8.027161994609964, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_N-1BrO->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_N-1BrO->Br
    Total Standard Deviation in ln(k): 12.26304933608979"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_N-1BrO->Br
Total Standard Deviation in ln(k): 12.26304933608979""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_N-1BrO->Br
Total Standard Deviation in ln(k): 12.26304933608979
""",
)

entry(
    index = 49,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_3R->O_3O-u1",
    kinetics = ArrheniusBM(A=(5.55e+08,'m^3/(mol*s)'), n=-0.66, w0=(212550,'J/mol'), E0=(4523.67,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_3R->O_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_3R->O_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_3R->O_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_3R->O_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 50,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_3R->O_N-3O-u1",
    kinetics = ArrheniusBM(A=(5.3e+06,'m^3/(mol*s)'), n=0, w0=(212550,'J/mol'), E0=(8723.87,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_3R->O_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_3R->O_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_3R->O_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_3R->O_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 51,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_3BrCH->Br",
    kinetics = ArrheniusBM(A=(1.62623e+09,'m^3/(mol*s)'), n=-0.659413, w0=(212550,'J/mol'), E0=(4542.98,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_3BrCH->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_3BrCH->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_3BrCH->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_3BrCH->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 52,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br",
    kinetics = ArrheniusBM(A=(2043.57,'m^3/(mol*s)'), n=1.56114, w0=(272386,'J/mol'), E0=(35567.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0010821625097404578, var=0.28066061534160086, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br
    Total Standard Deviation in ln(k): 1.064775757290886"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br
Total Standard Deviation in ln(k): 1.064775757290886""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br
Total Standard Deviation in ln(k): 1.064775757290886
""",
)

entry(
    index = 53,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrO-u0_N-3R->Br_Ext-3CHO-R",
    kinetics = ArrheniusBM(A=(2.31488e+11,'m^3/(mol*s)'), n=-1.6853, w0=(260050,'J/mol'), E0=(30912,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.6649700656316035, var=4.1322449448537455, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrO-u0_N-3R->Br_Ext-3CHO-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrO-u0_N-3R->Br_Ext-3CHO-R
    Total Standard Deviation in ln(k): 5.745989290370929"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrO-u0_N-3R->Br_Ext-3CHO-R
Total Standard Deviation in ln(k): 5.745989290370929""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrO-u0_N-3R->Br_Ext-3CHO-R
Total Standard Deviation in ln(k): 5.745989290370929
""",
)

entry(
    index = 54,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrO-u0_N-3R->Br_3CHO->C",
    kinetics = ArrheniusBM(A=(5.64233e+07,'m^3/(mol*s)'), n=-0.596289, w0=(260050,'J/mol'), E0=(15576.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrO-u0_N-3R->Br_3CHO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrO-u0_N-3R->Br_3CHO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrO-u0_N-3R->Br_3CHO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrO-u0_N-3R->Br_3CHO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 55,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrO-u0_N-3R->Br_N-3CHO->C",
    kinetics = ArrheniusBM(A=(1e+06,'m^3/(mol*s)'), n=0, w0=(298550,'J/mol'), E0=(29855,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrO-u0_N-3R->Br_N-3CHO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrO-u0_N-3R->Br_N-3CHO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrO-u0_N-3R->Br_N-3CHO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrO-u0_N-3R->Br_N-3CHO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 56,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=3C",
    kinetics = ArrheniusBM(A=(3031.4,'m^3/(mol*s)'), n=1.04901, w0=(323500,'J/mol'), E0=(65422.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.027175033457041274, var=0.06963930819597611, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=3C
    Total Standard Deviation in ln(k): 0.597313745086431"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=3C
Total Standard Deviation in ln(k): 0.597313745086431""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=3C
Total Standard Deviation in ln(k): 0.597313745086431
""",
)

entry(
    index = 57,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=3C",
    kinetics = ArrheniusBM(A=(15.2631,'m^3/(mol*s)'), n=1.5636, w0=(323500,'J/mol'), E0=(53695.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.004147308692882553, var=4.062837855042181, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=3C',), comment="""BM rule fitted to 5 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=3C
    Total Standard Deviation in ln(k): 4.051261117754709"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=3C
Total Standard Deviation in ln(k): 4.051261117754709""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=3C
Total Standard Deviation in ln(k): 4.051261117754709
""",
)

entry(
    index = 58,
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
    index = 59,
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
    index = 60,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0_Ext-1C-R_Sp-4R!H=1C",
    kinetics = ArrheniusBM(A=(3101.16,'m^3/(mol*s)'), n=1.48308, w0=(323500,'J/mol'), E0=(56972.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.009622695723297159, var=1.4932494029440815, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0_Ext-1C-R_Sp-4R!H=1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0_Ext-1C-R_Sp-4R!H=1C
    Total Standard Deviation in ln(k): 2.4739355129976532"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0_Ext-1C-R_Sp-4R!H=1C
Total Standard Deviation in ln(k): 2.4739355129976532""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0_Ext-1C-R_Sp-4R!H=1C
Total Standard Deviation in ln(k): 2.4739355129976532
""",
)

entry(
    index = 61,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0_Ext-1C-R_N-Sp-4R!H=1C",
    kinetics = ArrheniusBM(A=(0.442907,'m^3/(mol*s)'), n=2.51403, w0=(323500,'J/mol'), E0=(40466.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.025454755193513753, var=2.2789675287757154, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0_Ext-1C-R_N-Sp-4R!H=1C',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0_Ext-1C-R_N-Sp-4R!H=1C
    Total Standard Deviation in ln(k): 3.0903547882854188"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0_Ext-1C-R_N-Sp-4R!H=1C
Total Standard Deviation in ln(k): 3.0903547882854188""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0_Ext-1C-R_N-Sp-4R!H=1C
Total Standard Deviation in ln(k): 3.0903547882854188
""",
)

entry(
    index = 62,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_N-1C-u0_Ext-1C-R_Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(4.92797e-10,'m^3/(mol*s)'), n=5.05694, w0=(323500,'J/mol'), E0=(-5462.78,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4146126939604183, var=2.1672192650295634, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_N-1C-u0_Ext-1C-R_Sp-4R!H-1C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_N-1C-u0_Ext-1C-R_Sp-4R!H-1C
    Total Standard Deviation in ln(k): 3.99300685255122"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_N-1C-u0_Ext-1C-R_Sp-4R!H-1C
Total Standard Deviation in ln(k): 3.99300685255122""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_N-1C-u0_Ext-1C-R_Sp-4R!H-1C
Total Standard Deviation in ln(k): 3.99300685255122
""",
)

entry(
    index = 63,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_N-1C-u0_Ext-1C-R_N-Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(2625.75,'m^3/(mol*s)'), n=1.23946, w0=(323500,'J/mol'), E0=(33096,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_N-1C-u0_Ext-1C-R_N-Sp-4R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_N-1C-u0_Ext-1C-R_N-Sp-4R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_N-1C-u0_Ext-1C-R_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_N-1C-u0_Ext-1C-R_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 64,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1",
    kinetics = ArrheniusBM(A=(0.0560495,'m^3/(mol*s)'), n=2.38609, w0=(285000,'J/mol'), E0=(48481.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03457687290715065, var=7.952258800734053, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1',), comment="""BM rule fitted to 15 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1
    Total Standard Deviation in ln(k): 5.7401792939161025"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1
Total Standard Deviation in ln(k): 5.7401792939161025""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1
Total Standard Deviation in ln(k): 5.7401792939161025
""",
)

entry(
    index = 65,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_N-3BrC-u1",
    kinetics = ArrheniusBM(A=(6.29689e+24,'m^3/(mol*s)'), n=-4.84804, w0=(285000,'J/mol'), E0=(82562.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.47932563146551777, var=9.598182212950416, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_N-3BrC-u1',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_N-3BrC-u1
    Total Standard Deviation in ln(k): 7.415192106999519"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_N-3BrC-u1
Total Standard Deviation in ln(k): 7.415192106999519""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_N-3BrC-u1
Total Standard Deviation in ln(k): 7.415192106999519
""",
)

entry(
    index = 66,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_3BrCO->Br_1C-u0_Ext-1C-R",
    kinetics = ArrheniusBM(A=(9.05584e+10,'m^3/(mol*s)'), n=-0.94803, w0=(237500,'J/mol'), E0=(-35179.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.862747501434782, var=38.77831150089627, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_3BrCO->Br_1C-u0_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_3BrCO->Br_1C-u0_Ext-1C-R
    Total Standard Deviation in ln(k): 22.189328953599475"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_3BrCO->Br_1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 22.189328953599475""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_3BrCO->Br_1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 22.189328953599475
""",
)

entry(
    index = 67,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1",
    kinetics = ArrheniusBM(A=(0.654647,'m^3/(mol*s)'), n=2.13443, w0=(277323,'J/mol'), E0=(47536.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0564616140369068, var=7.553205547404734, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1
    Total Standard Deviation in ln(k): 5.651495970373906"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1
Total Standard Deviation in ln(k): 5.651495970373906""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1
Total Standard Deviation in ln(k): 5.651495970373906
""",
)

entry(
    index = 68,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_N-3CO-u1",
    kinetics = ArrheniusBM(A=(5.67642e+14,'m^3/(mol*s)'), n=-2.33379, w0=(260050,'J/mol'), E0=(29844.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.17156176802326226, var=1.0572447409880583, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_N-3CO-u1',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_N-3CO-u1
    Total Standard Deviation in ln(k): 2.4923765819901305"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_N-3CO-u1
Total Standard Deviation in ln(k): 2.4923765819901305""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_N-3CO-u1
Total Standard Deviation in ln(k): 2.4923765819901305
""",
)

entry(
    index = 69,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_N-1C-u0_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.72205e+13,'m^3/(mol*s)'), n=-1.72311, w0=(285000,'J/mol'), E0=(30937.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.9033957811730633, var=0.032230573830243005, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_N-1C-u0_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_N-1C-u0_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 7.654871866621272"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_N-1C-u0_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 7.654871866621272""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_N-1C-u0_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 7.654871866621272
""",
)

entry(
    index = 70,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_N-1C-u0_Ext-1C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(0.0291245,'m^3/(mol*s)'), n=2.69164, w0=(285000,'J/mol'), E0=(36210.7,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_N-1C-u0_Ext-1C-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_N-1C-u0_Ext-1C-R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_N-1C-u0_Ext-1C-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_N-1C-u0_Ext-1C-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 71,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_N-1C-u0_Ext-1C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.0169924,'m^3/(mol*s)'), n=2.72405, w0=(285000,'J/mol'), E0=(41346.9,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_N-1C-u0_Ext-1C-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_N-1C-u0_Ext-1C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_N-1C-u0_Ext-1C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_N-1C-u0_Ext-1C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 72,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_Ext-3R-R_1BrO->Br",
    kinetics = ArrheniusBM(A=(605000,'m^3/(mol*s)'), n=0, w0=(237500,'J/mol'), E0=(26474.9,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_Ext-3R-R_1BrO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_Ext-3R-R_1BrO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_Ext-3R-R_1BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_Ext-3R-R_1BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 73,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_Ext-3R-R_N-1BrO->Br",
    kinetics = ArrheniusBM(A=(714.922,'m^3/(mol*s)'), n=0.905401, w0=(260050,'J/mol'), E0=(17266.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_Ext-3R-R_N-1BrO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_Ext-3R-R_N-1BrO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_Ext-3R-R_N-1BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_Ext-3R-R_N-1BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 74,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_1BrO->Br_Sp-4R!H-3R",
    kinetics = ArrheniusBM(A=(7.85e+06,'m^3/(mol*s)'), n=0, w0=(237500,'J/mol'), E0=(23750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_1BrO->Br_Sp-4R!H-3R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_1BrO->Br_Sp-4R!H-3R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_1BrO->Br_Sp-4R!H-3R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_1BrO->Br_Sp-4R!H-3R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 75,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_1BrO->Br_N-Sp-4R!H-3R",
    kinetics = ArrheniusBM(A=(1.2e+07,'m^3/(mol*s)'), n=0, w0=(237500,'J/mol'), E0=(23750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_1BrO->Br_N-Sp-4R!H-3R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_1BrO->Br_N-Sp-4R!H-3R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_1BrO->Br_N-Sp-4R!H-3R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_1BrO->Br_N-Sp-4R!H-3R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 76,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_N-1BrO->Br_Sp-4R!H-3R",
    kinetics = ArrheniusBM(A=(36181.1,'m^3/(mol*s)'), n=0.525658, w0=(260050,'J/mol'), E0=(18554,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_N-1BrO->Br_Sp-4R!H-3R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_N-1BrO->Br_Sp-4R!H-3R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_N-1BrO->Br_Sp-4R!H-3R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_N-1BrO->Br_Sp-4R!H-3R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 77,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_N-1BrO->Br_N-Sp-4R!H-3R",
    kinetics = ArrheniusBM(A=(15049.5,'m^3/(mol*s)'), n=0.392587, w0=(260050,'J/mol'), E0=(26005,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_N-1BrO->Br_N-Sp-4R!H-3R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_N-1BrO->Br_N-Sp-4R!H-3R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_N-1BrO->Br_N-Sp-4R!H-3R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_Ext-3R-R_N-1BrO->Br_N-Sp-4R!H-3R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 78,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_3CH-u1",
    kinetics = ArrheniusBM(A=(1599.05,'m^3/(mol*s)'), n=1.59584, w0=(278200,'J/mol'), E0=(39348.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.007099861095785292, var=0.26475779085756607, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_3CH-u1',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_3CH-u1
    Total Standard Deviation in ln(k): 1.049367660956376"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_3CH-u1
Total Standard Deviation in ln(k): 1.049367660956376""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_3CH-u1
Total Standard Deviation in ln(k): 1.049367660956376
""",
)

entry(
    index = 79,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_N-3CH-u1",
    kinetics = ArrheniusBM(A=(194.627,'m^3/(mol*s)'), n=0.434377, w0=(237500,'J/mol'), E0=(23750,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_N-3CH-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_N-3CH-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_N-3CH-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_N-3CH-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 80,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrO-u0_N-3R->Br_Ext-3CHO-R_Ext-3CHO-R",
    kinetics = ArrheniusBM(A=(14427.7,'m^3/(mol*s)'), n=0.346526, w0=(260050,'J/mol'), E0=(13273,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrO-u0_N-3R->Br_Ext-3CHO-R_Ext-3CHO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrO-u0_N-3R->Br_Ext-3CHO-R_Ext-3CHO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrO-u0_N-3R->Br_Ext-3CHO-R_Ext-3CHO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_N-1BrO-u0_N-3R->Br_Ext-3CHO-R_Ext-3CHO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 81,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.26163e-08,'m^3/(mol*s)'), n=4.50616, w0=(323500,'J/mol'), E0=(46576.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=3C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=3C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrBrCCFFIINNOOPPSSSiSi=3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 82,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.000140279,'m^3/(mol*s)'), n=2.93707, w0=(323500,'J/mol'), E0=(29605.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=3C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=3C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 83,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=3C_Ext-4BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(0.00446386,'m^3/(mol*s)'), n=2.50706, w0=(323500,'J/mol'), E0=(44546.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.002369357643453439, var=4.8899952222988965, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=3C_Ext-4BrCFINOPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=3C_Ext-4BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 4.439090711452324"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=3C_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 4.439090711452324""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=3C_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 4.439090711452324
""",
)

entry(
    index = 84,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0_Ext-1C-R_Sp-4R!H=1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3e+08,'m^3/(mol*s)'), n=0, w0=(323500,'J/mol'), E0=(72923.7,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0_Ext-1C-R_Sp-4R!H=1C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0_Ext-1C-R_Sp-4R!H=1C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0_Ext-1C-R_Sp-4R!H=1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0_Ext-1C-R_Sp-4R!H=1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 85,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2.30963,'m^3/(mol*s)'), n=2.22053, w0=(323500,'J/mol'), E0=(39600.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0005452558867692863, var=11.080192570090098, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 6.674516248090655"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R
Total Standard Deviation in ln(k): 6.674516248090655""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R
Total Standard Deviation in ln(k): 6.674516248090655
""",
)

entry(
    index = 86,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->C",
    kinetics = ArrheniusBM(A=(416.64,'m^3/(mol*s)'), n=1.75119, w0=(323500,'J/mol'), E0=(48282.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.10056140288087342, var=0.020642194789598986, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->C
    Total Standard Deviation in ln(k): 0.540694985061601"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->C
Total Standard Deviation in ln(k): 0.540694985061601""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_4R!H->C
Total Standard Deviation in ln(k): 0.540694985061601
""",
)

entry(
    index = 87,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(589.737,'m^3/(mol*s)'), n=1.62414, w0=(323500,'J/mol'), E0=(53829.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.04709975495970357, var=0.015864758780953222, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->C
    Total Standard Deviation in ln(k): 0.37084826953301403"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->C
Total Standard Deviation in ln(k): 0.37084826953301403""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->C
Total Standard Deviation in ln(k): 0.37084826953301403
""",
)

entry(
    index = 88,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(379.761,'m^3/(mol*s)'), n=1.67816, w0=(323500,'J/mol'), E0=(33799.7,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 89,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C",
    kinetics = ArrheniusBM(A=(197.056,'m^3/(mol*s)'), n=1.64084, w0=(323500,'J/mol'), E0=(41284.7,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 90,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(149.752,'m^3/(mol*s)'), n=1.64303, w0=(323500,'J/mol'), E0=(44257.2,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_N-1C-u0_Ext-1C-R_Sp-4R!H-1C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 91,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C",
    kinetics = ArrheniusBM(A=(3.09281e-17,'m^3/(mol*s)'), n=7.04013, w0=(285000,'J/mol'), E0=(11705.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.22791499898342404, var=6.891868351476702, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C
    Total Standard Deviation in ln(k): 5.835555087067116"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C
Total Standard Deviation in ln(k): 5.835555087067116""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C
Total Standard Deviation in ln(k): 5.835555087067116
""",
)

entry(
    index = 92,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.0189487,'m^3/(mol*s)'), n=2.2286, w0=(285000,'J/mol'), E0=(49348,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07783696773675657, var=0.8093799884091178, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_N-4R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_N-4R!H->C
    Total Standard Deviation in ln(k): 1.9991411753887938"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_N-4R!H->C
Total Standard Deviation in ln(k): 1.9991411753887938""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_N-4R!H->C
Total Standard Deviation in ln(k): 1.9991411753887938
""",
)

entry(
    index = 93,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_N-3BrC-u1_Ext-3BrC-R",
    kinetics = ArrheniusBM(A=(6.81642e+09,'m^3/(mol*s)'), n=-0.384812, w0=(285000,'J/mol'), E0=(10060.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-4.224791795219166, var=2.745708217015127, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_N-3BrC-u1_Ext-3BrC-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_N-3BrC-u1_Ext-3BrC-R
    Total Standard Deviation in ln(k): 13.936936607002513"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_N-3BrC-u1_Ext-3BrC-R
Total Standard Deviation in ln(k): 13.936936607002513""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_N-3BrC-u1_Ext-3BrC-R
Total Standard Deviation in ln(k): 13.936936607002513
""",
)

entry(
    index = 94,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_N-3BrC-u1_4R!H->C",
    kinetics = ArrheniusBM(A=(0.0016727,'m^3/(mol*s)'), n=3.33083, w0=(285000,'J/mol'), E0=(30341.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_N-3BrC-u1_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_N-3BrC-u1_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_N-3BrC-u1_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_N-3BrC-u1_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 95,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_N-3BrC-u1_N-4R!H->C",
    kinetics = ArrheniusBM(A=(5.11215e-06,'m^3/(mol*s)'), n=3.81141, w0=(285000,'J/mol'), E0=(31398.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_N-3BrC-u1_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_N-3BrC-u1_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_N-3BrC-u1_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_N-3BrC-u1_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 96,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_3BrCO->Br_1C-u0_Ext-1C-R_Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(6.17067e+10,'m^3/(mol*s)'), n=-0.977887, w0=(237500,'J/mol'), E0=(20947.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.10249654351863134, var=16.137870525755368, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_3BrCO->Br_1C-u0_Ext-1C-R_Sp-4R!H-1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_3BrCO->Br_1C-u0_Ext-1C-R_Sp-4R!H-1C
    Total Standard Deviation in ln(k): 8.310944440337074"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_3BrCO->Br_1C-u0_Ext-1C-R_Sp-4R!H-1C
Total Standard Deviation in ln(k): 8.310944440337074""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_3BrCO->Br_1C-u0_Ext-1C-R_Sp-4R!H-1C
Total Standard Deviation in ln(k): 8.310944440337074
""",
)

entry(
    index = 97,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_3BrCO->Br_1C-u0_Ext-1C-R_N-Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(7.0092e+09,'m^3/(mol*s)'), n=-0.392, w0=(237500,'J/mol'), E0=(23750,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_3BrCO->Br_1C-u0_Ext-1C-R_N-Sp-4R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_3BrCO->Br_1C-u0_Ext-1C-R_N-Sp-4R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_3BrCO->Br_1C-u0_Ext-1C-R_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_3BrCO->Br_1C-u0_Ext-1C-R_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 98,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C",
    kinetics = ArrheniusBM(A=(0.0406861,'m^3/(mol*s)'), n=2.49114, w0=(285000,'J/mol'), E0=(45172.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.05074452052252661, var=7.714017129843122, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C
    Total Standard Deviation in ln(k): 5.695473952154746"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C
Total Standard Deviation in ln(k): 5.695473952154746""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C
Total Standard Deviation in ln(k): 5.695473952154746
""",
)

entry(
    index = 99,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_N-3CO->C",
    kinetics = ArrheniusBM(A=(9.70803e+15,'m^3/(mol*s)'), n=-2.72939, w0=(260050,'J/mol'), E0=(12554.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.15162387217802184, var=4.830882796507803, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_N-3CO->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_N-3CO->C
    Total Standard Deviation in ln(k): 4.7872257202216"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_N-3CO->C
Total Standard Deviation in ln(k): 4.7872257202216""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_N-3CO->C
Total Standard Deviation in ln(k): 4.7872257202216
""",
)

entry(
    index = 100,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_N-3CO-u1_Ext-1C-R",
    kinetics = ArrheniusBM(A=(5.73534e+13,'m^3/(mol*s)'), n=-2.04678, w0=(260050,'J/mol'), E0=(28382.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.17791686282955063, var=2.133483104549346, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_N-3CO-u1_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_N-3CO-u1_Ext-1C-R
    Total Standard Deviation in ln(k): 3.3752330724117763"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_N-3CO-u1_Ext-1C-R
Total Standard Deviation in ln(k): 3.3752330724117763""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_N-3CO-u1_Ext-1C-R
Total Standard Deviation in ln(k): 3.3752330724117763
""",
)

entry(
    index = 101,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_N-1C-u0_Ext-1C-R_Ext-1C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(0.0244505,'m^3/(mol*s)'), n=2.62586, w0=(285000,'J/mol'), E0=(22089.6,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_N-1C-u0_Ext-1C-R_Ext-1C-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_N-1C-u0_Ext-1C-R_Ext-1C-R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_N-1C-u0_Ext-1C-R_Ext-1C-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_N-1C-u0_Ext-1C-R_Ext-1C-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 102,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_N-1C-u0_Ext-1C-R_Ext-1C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.0741868,'m^3/(mol*s)'), n=2.6667, w0=(285000,'J/mol'), E0=(21687.6,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_N-1C-u0_Ext-1C-R_Ext-1C-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_N-1C-u0_Ext-1C-R_Ext-1C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_N-1C-u0_Ext-1C-R_Ext-1C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_N-1C-u0_Ext-1C-R_Ext-1C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 103,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_3CH-u1_3CH->C",
    kinetics = ArrheniusBM(A=(3.18672e-33,'m^3/(mol*s)'), n=11.5496, w0=(248775,'J/mol'), E0=(-28447.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.7937728146942329, var=0.4265297382842621, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_3CH-u1_3CH->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_3CH-u1_3CH->C
    Total Standard Deviation in ln(k): 5.816244199096479"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_3CH-u1_3CH->C
Total Standard Deviation in ln(k): 5.816244199096479""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_3CH-u1_3CH->C
Total Standard Deviation in ln(k): 5.816244199096479
""",
)

entry(
    index = 104,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_3CH-u1_N-3CH->C",
    kinetics = ArrheniusBM(A=(1351.55,'m^3/(mol*s)'), n=1.62054, w0=(292912,'J/mol'), E0=(29291.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.006954391262830947, var=0.22462875505850005, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_3CH-u1_N-3CH->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_3CH-u1_N-3CH->C
    Total Standard Deviation in ln(k): 0.9676178574617904"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_3CH-u1_N-3CH->C
Total Standard Deviation in ln(k): 0.9676178574617904""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_3CH-u1_N-3CH->C
Total Standard Deviation in ln(k): 0.9676178574617904
""",
)

entry(
    index = 105,
    label = "Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=3C_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(0.315343,'m^3/(mol*s)'), n=2.015, w0=(323500,'J/mol'), E0=(44975.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=3C_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=3C_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=3C_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_3R->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=3C_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 106,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(650.121,'m^3/(mol*s)'), n=1.74726, w0=(323500,'J/mol'), E0=(50950.1,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 107,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(20,'m^3/(mol*s)'), n=2.01, w0=(323500,'J/mol'), E0=(45391.5,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_3R->H_1C-u0_Ext-1C-R_N-Sp-4R!H=1C_N-4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 108,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.6133e+20,'m^3/(mol*s)'), n=-4.19698, w0=(285000,'J/mol'), E0=(51681.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.26177186979103667, var=11.765593738400979, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 7.534162313222643"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 7.534162313222643""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 7.534162313222643
""",
)

entry(
    index = 109,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(0.000580939,'m^3/(mol*s)'), n=3.14565, w0=(285000,'J/mol'), E0=(61278,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 110,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_Sp-4C-3BrC",
    kinetics = ArrheniusBM(A=(88.2817,'m^3/(mol*s)'), n=1.57598, w0=(285000,'J/mol'), E0=(48272.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.6615732560133369, var=13.901923111760915, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_Sp-4C-3BrC',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_Sp-4C-3BrC
    Total Standard Deviation in ln(k): 9.136955785631626"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_Sp-4C-3BrC
Total Standard Deviation in ln(k): 9.136955785631626""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_Sp-4C-3BrC
Total Standard Deviation in ln(k): 9.136955785631626
""",
)

entry(
    index = 111,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_N-Sp-4C-3BrC",
    kinetics = ArrheniusBM(A=(199360,'m^3/(mol*s)'), n=0.43, w0=(285000,'J/mol'), E0=(13954.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_N-Sp-4C-3BrC',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_N-Sp-4C-3BrC
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_N-Sp-4C-3BrC
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_N-Sp-4C-3BrC
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 112,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_N-4R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.4672e+20,'m^3/(mol*s)'), n=-3.95507, w0=(285000,'J/mol'), E0=(53266.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.5478732376713488, var=8.64553765638748, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_N-4R!H->C_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_N-4R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 7.271147641481283"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_N-4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 7.271147641481283""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_N-4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 7.271147641481283
""",
)

entry(
    index = 113,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_N-4R!H->C_Ext-3BrC-R",
    kinetics = ArrheniusBM(A=(7.87004e-05,'m^3/(mol*s)'), n=2.99281, w0=(285000,'J/mol'), E0=(30132.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_N-4R!H->C_Ext-3BrC-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_N-4R!H->C_Ext-3BrC-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_N-4R!H->C_Ext-3BrC-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_N-4R!H->C_Ext-3BrC-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 114,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_N-4R!H->C_4ClFO->O",
    kinetics = ArrheniusBM(A=(0.00466139,'m^3/(mol*s)'), n=2.28217, w0=(285000,'J/mol'), E0=(42042.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_N-4R!H->C_4ClFO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_N-4R!H->C_4ClFO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_N-4R!H->C_4ClFO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_N-4R!H->C_4ClFO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 115,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_N-4R!H->C_N-4ClFO->O",
    kinetics = ArrheniusBM(A=(4.78928e-05,'m^3/(mol*s)'), n=3.07717, w0=(285000,'J/mol'), E0=(48212.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_N-4R!H->C_N-4ClFO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_N-4R!H->C_N-4ClFO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_N-4R!H->C_N-4ClFO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_N-4R!H->C_N-4ClFO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 116,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_N-3BrC-u1_Ext-3BrC-R_4R!H->C",
    kinetics = ArrheniusBM(A=(2.26825e-05,'m^3/(mol*s)'), n=3.63549, w0=(285000,'J/mol'), E0=(22104.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_N-3BrC-u1_Ext-3BrC-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_N-3BrC-u1_Ext-3BrC-R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_N-3BrC-u1_Ext-3BrC-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_N-3BrC-u1_Ext-3BrC-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 117,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_N-3BrC-u1_Ext-3BrC-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(7.59768e-11,'m^3/(mol*s)'), n=5.76728, w0=(285000,'J/mol'), E0=(21705.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_N-3BrC-u1_Ext-3BrC-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_N-3BrC-u1_Ext-3BrC-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_N-3BrC-u1_Ext-3BrC-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_N-3BrC-u1_Ext-3BrC-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 118,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_3BrCO->Br_1C-u0_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.47962e+10,'m^3/(mol*s)'), n=-0.904814, w0=(237500,'J/mol'), E0=(40176.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_3BrCO->Br_1C-u0_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_3BrCO->Br_1C-u0_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_3BrCO->Br_1C-u0_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_3BrCO->Br_1C-u0_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 119,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(1.10422e-15,'m^3/(mol*s)'), n=6.60336, w0=(285000,'J/mol'), E0=(11981.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.3003257929896403, var=11.630247168153922, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_4R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_4R!H->C
    Total Standard Deviation in ln(k): 7.591365163196117"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_4R!H->C
Total Standard Deviation in ln(k): 7.591365163196117""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_4R!H->C
Total Standard Deviation in ln(k): 7.591365163196117
""",
)

entry(
    index = 120,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(8.60743,'m^3/(mol*s)'), n=1.5908, w0=(285000,'J/mol'), E0=(52070.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0014657358142244124, var=14.566901020932242, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_N-4R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 7.655076894405451"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_N-4R!H->C
Total Standard Deviation in ln(k): 7.655076894405451""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_N-4R!H->C
Total Standard Deviation in ln(k): 7.655076894405451
""",
)

entry(
    index = 121,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_N-3CO->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.36984e+14,'m^3/(mol*s)'), n=-2.31423, w0=(260050,'J/mol'), E0=(22556.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.3868159133422941, var=6.7048020287619075, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_N-3CO->C_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_N-3CO->C_Ext-1C-R
    Total Standard Deviation in ln(k): 6.162886610619992"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_N-3CO->C_Ext-1C-R
Total Standard Deviation in ln(k): 6.162886610619992""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_N-3CO->C_Ext-1C-R
Total Standard Deviation in ln(k): 6.162886610619992
""",
)

entry(
    index = 122,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_N-3CO-u1_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(9e+06,'m^3/(mol*s)'), n=0, w0=(260050,'J/mol'), E0=(16433.5,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_N-3CO-u1_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_N-3CO-u1_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_N-3CO-u1_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_N-3CO-u1_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 123,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_3CH-u1_3CH->C_1BrO->Br",
    kinetics = ArrheniusBM(A=(6.05e+06,'m^3/(mol*s)'), n=0, w0=(237500,'J/mol'), E0=(23750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_3CH-u1_3CH->C_1BrO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_3CH-u1_3CH->C_1BrO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_3CH-u1_3CH->C_1BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_3CH-u1_3CH->C_1BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 124,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_3CH-u1_3CH->C_N-1BrO->Br",
    kinetics = ArrheniusBM(A=(2.5163e+06,'m^3/(mol*s)'), n=-0.0374132, w0=(260050,'J/mol'), E0=(19503.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_3CH-u1_3CH->C_N-1BrO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_3CH-u1_3CH->C_N-1BrO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_3CH-u1_3CH->C_N-1BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_3CH-u1_3CH->C_N-1BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 125,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_3CH-u1_N-3CH->C_Ext-1BrO-R",
    kinetics = ArrheniusBM(A=(1309.58,'m^3/(mol*s)'), n=1.62557, w0=(298550,'J/mol'), E0=(29855,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.05630419466203027, var=0.3152507178383666, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_3CH-u1_N-3CH->C_Ext-1BrO-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_3CH-u1_N-3CH->C_Ext-1BrO-R
    Total Standard Deviation in ln(k): 1.2670702803684868"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_3CH-u1_N-3CH->C_Ext-1BrO-R
Total Standard Deviation in ln(k): 1.2670702803684868""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_3CH-u1_N-3CH->C_Ext-1BrO-R
Total Standard Deviation in ln(k): 1.2670702803684868
""",
)

entry(
    index = 126,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_3CH-u1_N-3CH->C_1BrO->Br",
    kinetics = ArrheniusBM(A=(114000,'m^3/(mol*s)'), n=1, w0=(276000,'J/mol'), E0=(27600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_3CH-u1_N-3CH->C_1BrO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_3CH-u1_N-3CH->C_1BrO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_3CH-u1_N-3CH->C_1BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_3CH-u1_N-3CH->C_1BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 127,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_3CH-u1_N-3CH->C_N-1BrO->Br",
    kinetics = ArrheniusBM(A=(3e+07,'m^3/(mol*s)'), n=0, w0=(298550,'J/mol'), E0=(29855,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_3CH-u1_N-3CH->C_N-1BrO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_3CH-u1_N-3CH->C_N-1BrO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_3CH-u1_N-3CH->C_N-1BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_3CH-u1_N-3CH->C_N-1BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 128,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_Ext-1C-R_Sp-4C=3BrBrCC",
    kinetics = ArrheniusBM(A=(4.19028e+07,'m^3/(mol*s)'), n=-0.141367, w0=(285000,'J/mol'), E0=(17856.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.8717020469262368, var=0.6884750486105978, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_Ext-1C-R_Sp-4C=3BrBrCC',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_Ext-1C-R_Sp-4C=3BrBrCC
    Total Standard Deviation in ln(k): 3.853622981344778"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_Ext-1C-R_Sp-4C=3BrBrCC
Total Standard Deviation in ln(k): 3.853622981344778""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_Ext-1C-R_Sp-4C=3BrBrCC
Total Standard Deviation in ln(k): 3.853622981344778
""",
)

entry(
    index = 129,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_Ext-1C-R_N-Sp-4C=3BrBrCC",
    kinetics = ArrheniusBM(A=(2.53042e+07,'m^3/(mol*s)'), n=-0.379744, w0=(285000,'J/mol'), E0=(33653.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_Ext-1C-R_N-Sp-4C=3BrBrCC',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_Ext-1C-R_N-Sp-4C=3BrBrCC
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_Ext-1C-R_N-Sp-4C=3BrBrCC
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_Ext-1C-R_N-Sp-4C=3BrBrCC
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 130,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_Sp-4C-3BrC_Ext-3BrC-R",
    kinetics = ArrheniusBM(A=(1.33708e-11,'m^3/(mol*s)'), n=5.36122, w0=(285000,'J/mol'), E0=(-1846.41,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1710217051851192, var=2.846816501450424, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_Sp-4C-3BrC_Ext-3BrC-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_Sp-4C-3BrC_Ext-3BrC-R
    Total Standard Deviation in ln(k): 3.8121943762452886"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_Sp-4C-3BrC_Ext-3BrC-R
Total Standard Deviation in ln(k): 3.8121943762452886""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_Sp-4C-3BrC_Ext-3BrC-R
Total Standard Deviation in ln(k): 3.8121943762452886
""",
)

entry(
    index = 131,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_N-4R!H->C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(285000,'J/mol'), E0=(19506.1,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_N-4R!H->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_N-4R!H->C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_N-4R!H->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_N-4R!H->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 132,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_N-4R!H->C_Ext-1C-R_Sp-5R!H-1C",
    kinetics = ArrheniusBM(A=(1e+06,'m^3/(mol*s)'), n=0, w0=(285000,'J/mol'), E0=(30464.4,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_N-4R!H->C_Ext-1C-R_Sp-5R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_N-4R!H->C_Ext-1C-R_Sp-5R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_N-4R!H->C_Ext-1C-R_Sp-5R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_N-4R!H->C_Ext-1C-R_Sp-5R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 133,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_N-4R!H->C_Ext-1C-R_N-Sp-5R!H-1C",
    kinetics = ArrheniusBM(A=(2e+06,'m^3/(mol*s)'), n=0, w0=(285000,'J/mol'), E0=(12337.3,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_N-4R!H->C_Ext-1C-R_N-Sp-5R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_N-4R!H->C_Ext-1C-R_N-Sp-5R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_N-4R!H->C_Ext-1C-R_N-Sp-5R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_N-4R!H->C_Ext-1C-R_N-Sp-5R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 134,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_4R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.000149886,'m^3/(mol*s)'), n=3.33856, w0=(285000,'J/mol'), E0=(24310.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0550525557927264, var=0.09694733431833993, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_4R!H->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_4R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 0.7625246733983523"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 0.7625246733983523""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 0.7625246733983523
""",
)

entry(
    index = 135,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_4R!H->C_Sp-4C-1C",
    kinetics = ArrheniusBM(A=(0.000210316,'m^3/(mol*s)'), n=3.19938, w0=(285000,'J/mol'), E0=(47148.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.844872009599926, var=47.9134940114136, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_4R!H->C_Sp-4C-1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_4R!H->C_Sp-4C-1C
    Total Standard Deviation in ln(k): 26.049736020083678"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_4R!H->C_Sp-4C-1C
Total Standard Deviation in ln(k): 26.049736020083678""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_4R!H->C_Sp-4C-1C
Total Standard Deviation in ln(k): 26.049736020083678
""",
)

entry(
    index = 136,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_4R!H->C_N-Sp-4C-1C",
    kinetics = ArrheniusBM(A=(0.0027578,'m^3/(mol*s)'), n=2.96417, w0=(285000,'J/mol'), E0=(61782.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=5.866080928170888, var=73.32726907885305, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_4R!H->C_N-Sp-4C-1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_4R!H->C_N-Sp-4C-1C
    Total Standard Deviation in ln(k): 31.905712512663456"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_4R!H->C_N-Sp-4C-1C
Total Standard Deviation in ln(k): 31.905712512663456""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_4R!H->C_N-Sp-4C-1C
Total Standard Deviation in ln(k): 31.905712512663456
""",
)

entry(
    index = 137,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_N-4R!H->C_4BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(0.2494,'m^3/(mol*s)'), n=1.79792, w0=(285000,'J/mol'), E0=(46194.6,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_N-4R!H->C_4BrClFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_N-4R!H->C_4BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_N-4R!H->C_4BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_N-4R!H->C_4BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 138,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_N-4R!H->C_N-4BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(0.001655,'m^3/(mol*s)'), n=2.95855, w0=(285000,'J/mol'), E0=(48628.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07552110482532208, var=0.016378413885094627, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_N-4R!H->C_N-4BrClFINOPSSi->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_N-4R!H->C_N-4BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 0.44631386099303993"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_N-4R!H->C_N-4BrClFINOPSSi->O
Total Standard Deviation in ln(k): 0.44631386099303993""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_N-4R!H->C_N-4BrClFINOPSSi->O
Total Standard Deviation in ln(k): 0.44631386099303993
""",
)

entry(
    index = 139,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_N-3CO->C_Ext-1C-R_Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(1.21171e+18,'m^3/(mol*s)'), n=-3.29495, w0=(260050,'J/mol'), E0=(38505.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.9997402495321025, var=6.797480512557644, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_N-3CO->C_Ext-1C-R_Sp-4R!H-1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_N-3CO->C_Ext-1C-R_Sp-4R!H-1C
    Total Standard Deviation in ln(k): 7.738651113520571"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_N-3CO->C_Ext-1C-R_Sp-4R!H-1C
Total Standard Deviation in ln(k): 7.738651113520571""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_N-3CO->C_Ext-1C-R_Sp-4R!H-1C
Total Standard Deviation in ln(k): 7.738651113520571
""",
)

entry(
    index = 140,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_N-3CO->C_Ext-1C-R_N-Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(3e+06,'m^3/(mol*s)'), n=0, w0=(260050,'J/mol'), E0=(26005,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_N-3CO->C_Ext-1C-R_N-Sp-4R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_N-3CO->C_Ext-1C-R_N-Sp-4R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_N-3CO->C_Ext-1C-R_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_N-3CO->C_Ext-1C-R_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 141,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_3CH-u1_N-3CH->C_Ext-1BrO-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1823.35,'m^3/(mol*s)'), n=1.55333, w0=(298550,'J/mol'), E0=(29855,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_3CH-u1_N-3CH->C_Ext-1BrO-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_3CH-u1_N-3CH->C_Ext-1BrO-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_3CH-u1_N-3CH->C_Ext-1BrO-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->C_1BrO-u0_N-3R->O_N-3BrCH->Br_3CH-u1_N-3CH->C_Ext-1BrO-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 142,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_Ext-1C-R_Sp-4C=3BrBrCC_Ext-3BrC-R",
    kinetics = ArrheniusBM(A=(0.000107482,'m^3/(mol*s)'), n=3.57909, w0=(285000,'J/mol'), E0=(8040.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_Ext-1C-R_Sp-4C=3BrBrCC_Ext-3BrC-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_Ext-1C-R_Sp-4C=3BrBrCC_Ext-3BrC-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_Ext-1C-R_Sp-4C=3BrBrCC_Ext-3BrC-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_Ext-1C-R_Sp-4C=3BrBrCC_Ext-3BrC-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 143,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_Sp-4C-3BrC_Ext-3BrC-R_5R!H->C",
    kinetics = ArrheniusBM(A=(0.00230719,'m^3/(mol*s)'), n=2.96161, w0=(285000,'J/mol'), E0=(37850.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_Sp-4C-3BrC_Ext-3BrC-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_Sp-4C-3BrC_Ext-3BrC-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_Sp-4C-3BrC_Ext-3BrC-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_Sp-4C-3BrC_Ext-3BrC-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 144,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_Sp-4C-3BrC_Ext-3BrC-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(4.68481e-07,'m^3/(mol*s)'), n=3.98461, w0=(285000,'J/mol'), E0=(13071.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_Sp-4C-3BrC_Ext-3BrC-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_Sp-4C-3BrC_Ext-3BrC-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_Sp-4C-3BrC_Ext-3BrC-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_Ext-3BrCO-R_N-3BrCO->O_3BrC-u1_4R!H->C_Sp-4C-3BrC_Ext-3BrC-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 145,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_4R!H->C_Ext-1C-R_Sp-4C=1C",
    kinetics = ArrheniusBM(A=(0.0713601,'m^3/(mol*s)'), n=2.71607, w0=(285000,'J/mol'), E0=(40112,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_4R!H->C_Ext-1C-R_Sp-4C=1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_4R!H->C_Ext-1C-R_Sp-4C=1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_4R!H->C_Ext-1C-R_Sp-4C=1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_4R!H->C_Ext-1C-R_Sp-4C=1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 146,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_4R!H->C_Ext-1C-R_N-Sp-4C=1C",
    kinetics = ArrheniusBM(A=(0.00808906,'m^3/(mol*s)'), n=2.74525, w0=(285000,'J/mol'), E0=(24580.1,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_4R!H->C_Ext-1C-R_N-Sp-4C=1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_4R!H->C_Ext-1C-R_N-Sp-4C=1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_4R!H->C_Ext-1C-R_N-Sp-4C=1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_4R!H->C_Ext-1C-R_N-Sp-4C=1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 147,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_4R!H->C_N-Sp-4C-1C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(0.00684122,'m^3/(mol*s)'), n=2.86155, w0=(285000,'J/mol'), E0=(63747.8,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_4R!H->C_N-Sp-4C-1C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_4R!H->C_N-Sp-4C-1C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_4R!H->C_N-Sp-4C-1C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_4R!H->C_N-Sp-4C-1C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 148,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_N-4R!H->C_N-4BrClFINOPSSi->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.277,'m^3/(mol*s)'), n=2.05, w0=(285000,'J/mol'), E0=(38148.5,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_N-4R!H->C_N-4BrClFINOPSSi->O_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_N-4R!H->C_N-4BrClFINOPSSi->O_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_N-4R!H->C_N-4BrClFINOPSSi->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_3CO->C_Ext-1C-R_N-4R!H->C_N-4BrClFINOPSSi->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 149,
    label = "Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_N-3CO->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(260050,'J/mol'), E0=(22978,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_N-3CO->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_N-3CO->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_N-3CO->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->C_N-3R->H_N-3BrCO->Br_1C-u0_3CO-u1_N-3CO->C_Ext-1C-R_Sp-4R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

