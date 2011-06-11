#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_MultipleBond/rules"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 269,
    label = "XZ;Y_rad_birad",
    group1 = "OR{CZ, OCO, OCddO, OSi, OSiddO}",
    group2 = "OR{Y_rad, Y_birad}",
    kinetics = ArrheniusEP(
        A = (1e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (0.5,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 281,
    label = "Cd/H2;H_rad",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (1e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (1.2,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] in his reaction type 3. Based on recommendations of Allara and Shaw [146]""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
in his reaction type 3. Based on the recommendations of
[146] Allara, D.L.; Shaw, R. J Phys. Chem. Ref. Data 1980,9,523.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 282,
    label = "Cd/H/Nd;H_rad",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D}
3     H 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (1e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (2.9,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] in his reaction type 3. Based on recommendations of Allara and Shaw [146]""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
in his reaction type 3. Based on the recommendations of
[146] Allara, D.L.; Shaw, R. J Phys. Chem. Ref. Data 1980,9,523.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 283,
    label = "Cd/Nd2;H_rad",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D}
3     {Cs,O} 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (1e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (2.9,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] in his reaction type 3. Based on recommendations of Allara and Shaw [146]""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
in his reaction type 3. Based on the recommendations of
[146] Allara, D.L.; Shaw, R. J Phys. Chem. Ref. Data 1980,9,523.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 284,
    label = "Cd/H2;Cs_rad",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     R 0 {1,S}
3     R 0 {1,S}
4     R 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (8.5e+10,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (7.8,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] in his reaction type 3. Based on recommendations of Allara and Shaw [146]""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
in his reaction type 3. Based on the recommendations of
[146] Allara, D.L.; Shaw, R. J Phys. Chem. Ref. Data 1980,9,523.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 285,
    label = "Cd/H/Nd;Cs_rad",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D}
3     H 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     R 0 {1,S}
3     R 0 {1,S}
4     R 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (8.5e+10,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (10.6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] in his reaction type 3. Based on recommendations of Allara and Shaw [146]""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
in his reaction type 3. Based on the recommendations of
[146] Allara, D.L.; Shaw, R. J Phys. Chem. Ref. Data 1980,9,523.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 286,
    label = "Cd/Nd2;Cs_rad",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D}
3     {Cs,O} 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     R 0 {1,S}
3     R 0 {1,S}
4     R 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (8.5e+10,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (10.6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] in his reaction type 3. Based on recommendations of Allara and Shaw [146]""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
in his reaction type 3. Based on the recommendations of
[146] Allara, D.L.; Shaw, R. J Phys. Chem. Ref. Data 1980,9,523.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 287,
    label = "Cd/H2;O_rad/NonDe",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     {Cs,O} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (12.5,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] in his reaction type 20. Based on recommendations of Chen and Bozzelli [57]""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
in his reaction type 20. Based on the recommendations of
[146] Allara, D.L.; Shaw, R. J Phys. Chem. Ref. Data 1980,9,523.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 288,
    label = "Cd/H/Nd;O_rad/NonDe",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D}
3     H 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     {Cs,O} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (11,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] in his reaction type 20. Based on recommendations of Chen and Bozzelli [57]""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
in his reaction type 20. Based on the recommendations of
[146] Allara, D.L.; Shaw, R. J Phys. Chem. Ref. Data 1980,9,523.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 289,
    label = "Cd/Nd2;O_rad/NonDe",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D}
3     {Cs,O} 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     {Cs,O} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (7.6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] in his reaction type 20. Based on recommendations of Chen and Bozzelli [57]""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
in his reaction type 20. Based on the recommendations of
[146] Allara, D.L.; Shaw, R. J Phys. Chem. Ref. Data 1980,9,523.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 290,
    label = "Cd/H2_Cd/H2;H_rad",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (1.985e+09,"cm^3/(mol*s)","*|/",2),
        n = 1.28,
        alpha = 0,
        E0 = (1.29,"kcal/mol"),
        Tmin = (200,"K"),
        Tmax = (1100,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Baulch et al. [94] literature review.""",
    longDesc = 
u"""
[94] Baulch,D.L.; Cobos,C.J.;Cox,R.A;Frank,P.;Hayman,G.;Just,T.;Kerr,J.A.;Murells,T.;Philling,M.J.;Troe,J.;Walker,R.W.; Warnatz, J. J Phys Chem. Ref. Data 1994,23,847.
literature review. C2H4 + H --> C2H5. C.D.W. divided rate expression by 2, to get rate of addition per site 
pg.916-920: Discussion on evaluated data

H+C2H4(+m) --> C2H5(+m): "The analysis of the rxn is based on theoretical fall-off

curves and strong collision low pressure rate coefficients which were calculated
using a rxn threshold of 154.78 kJ/mol."  The rate coefficient stored in RMG
is the high-pressure limit, k_inf.
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 291,
    label = "Cd/H2_Cd/H2;C_methyl",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.655e+11,"cm^3/(mol*s)","*|/",1.3),
        n = 0,
        alpha = 0,
        E0 = (7.71,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang et al. [89] literature review.""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087. 
literature review. C2H4 + CH3 --> n-C3H7. C.D.W. divided rate expression by 2, to get rate of addition per site
pg. 1191: Discussion on evaluated data

Entry 18,16 (b)

Recommended data is from other Review paper by Kerr and Parsonage (1972)

MRH 28-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 292,
    label = "Cd/H2_Cd/H2;C_rad/H2/Cs",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1990,"cm^3/(mol*s)"),
        n = 2.44,
        alpha = 0,
        E0 = (5.37,"kcal/mol"),
        Tmin = (298,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Knyazev et al. [147]""",
    longDesc = 
u"""
[147] Knyazev,V.D.;Slagle,I.R. J Phys. Chem. 1996 100, 5318.
Pressure up to 10 atm. Excitation; thermal, analysis: mass spectrometry. C2H4 + C2H5--> n-C4H9. C.D.W. divided rate expression by 2, to get rate of addtion per site
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 293,
    label = "Cd/H2_Cd/H2;C_rad/H2/O",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.41e+10,"cm^3/(mol*s)","*|/",5),
        n = 0,
        alpha = 0,
        E0 = (6.96,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang et al. [90] literature review.""",
    longDesc = 
u"""
[90] Tsang,W.J. Phys. Chem. Ref. Data 1987,16,471.
literature review. C2H4+ CH2OH --> CH2CH2CH2OH C.D.W. divided rate expression by 2, to get rate of addition per site
pg. 502: Discussion on evaluated data

Entry 39,18 (a): No data available at the time.  Author suggests rate coefficient expression

of 8.0x10^-14 * exp(-3500/T) cm3/molecule/s noting rates of alkyl radical addition
to ethylene are similar (Kerr, J.A., Trotman-Dickenson, A.F.)
MRH 30-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 294,
    label = "Cd/H2_Cd/H2;Cd_pri_rad",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 Cd 1 {2,D} {3,S}
2     Cd 0 {1,D}
3     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (2.01,"kcal/mol"),
        Tmin = (1260,"K"),
        Tmax = (1310,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Weissman and Benson [148] Estimated values.""",
    longDesc = 
u"""
[148] Weissman and Benson. Estimated values. Activation energy is a lower limit. Pressure 1.00 atm. 
C2H4 + C2H3 --> CH2=CHCH2CH2 C.D.W. divided rate expression by 2, to get rate of addition per site
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 295,
    label = "Cd/H2_Cd/H2;O_pri_rad",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.71e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang et al. [89] literature review.""",
    longDesc = 
u"""
[89] Tsang et al. Literature Review.  
C2H4 + OH --> CH2CH2OH  C.D.W. divided rate expression by 2, to get rate of addition per site

pg. 1189: Discussion on evaluated data (in theory)

Online reference does not have pages 1188-1189; pages 1198-1199 come between
pages 1187&1190 and between 1197&1200
Following discussion is only based on table (pg. 1097) that summarizes all evaluated

data in the reference
Entry 18,6 (b)

Table states rxn is pressure-dependent: C2H4+OH(+M)=C2H4OH(+M)

Only data available in table is k=9.0x10^-12
MRH 28-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 296,
    label = "Cd/H2_Cd/H/Nd;H_rad",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     {Cs,O} 0 {2,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (1.3e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (1.56,"kcal/mol"),
        Tmin = (500,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [149] experiments and limited review.""",
    longDesc = 
u"""
[149] Tsang experiments and limited review. CH3CH=CH2 + H --> iso-C3H7
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 297,
    label = "Cd/H2_Cd/H/Nd;C_methyl",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     {Cs,O} 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (128000,"cm^3/(mol*s)"),
        n = 2.28,
        alpha = 0,
        E0 = (6.6,"kcal/mol"),
        Tmin = (298,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Knyazev et al. [150]""",
    longDesc = 
u"""
[150] Knayzev et al. Data derived from fitting to a complex mechanism. Pressure up to 10 atm. Excitation : flash photolysis, analysis : mass spectrometry
CH3CH=CH2 + CH3 --> sec-C4H9
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 298,
    label = "Cd/H2_Cd/H/Nd;C_methyl",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     {Cs,O} 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.69e+11,"cm^3/(mol*s)","*|/",1.4),
        n = 0,
        alpha = 0,
        E0 = (7.41,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [93] literature review.""",
    longDesc = 
u"""
[93] Tsang literature review. CH3CH=CH2 + CH3 --> sec-C4H9 
pg.237-239: Discussion on evaluated data

Entry 46,16(a): Recommended rate coefficient is that reported by Kerr and Parsonage (1972).

Author notes that rxn is pressure dependent and lists fall-off ratios and
collision efficiencies; these are not stored in RMG.
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 299,
    label = "Cd/H2_Cd/H/Nd;C_rad/H2/Cd",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     {Cs,O} 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.55e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (16.89,"kcal/mol"),
        Tmin = (762,"K"),
        Tmax = (811,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Barbe et al. [151] Data are estimated.""",
    longDesc = 
u"""
[151] Barbe et al. Data is estimated. Pressure 0.04-0.26 atm. CH3CH=CH2 + .CH2CH=CH2 --> CH3CH(.)CH2CH2CH=CH2
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 300,
    label = "Cd/H2_Cd/H/Nd;C_rad/Cs3",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     {Cs,O} 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     Cs 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.07e+09,"cm^3/(mol*s)","*|/",10),
        n = 0,
        alpha = 0,
        E0 = (5.88,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [93] literature review.""",
    longDesc = 
u"""
[93] Tsang literature review. CH3CH=CH2 + tert-C4H9 --> (CH3)3CCH2CH(.)CH3
pg.247: Discussion on evaluated data

Entry 46,44(terminal): Recommended rate coefficient is based on summary of data on alkyl

radical addition to olefins (Kerr and Parsonage, 1972).
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 301,
    label = "Cd/H2_Cd/H/De;C_methyl",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.155e+10,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (7.49,"kcal/mol"),
        Tmin = (743,"K"),
        Tmax = (772,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Perrin et al. [152] Data are estimated.""",
    longDesc = 
u"""
[152] Perrin et al. Data is estimated. Pressure 0.01-0.13 atm. 
CH2=CHCH=CH2 + .CH3 --> CH2CH=CHCH2CH3 C.D.W. divied rate expression by 2, to get rate of addition per site.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 302,
    label = "Cd/H2_Cd/Nd2;H_rad",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     {Cs,O} 0 {2,S}
6     {Cs,O} 0 {2,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (6.21e+12,"cm^3/(mol*s)"),
        n = 0.25,
        alpha = 0,
        E0 = (1.46,"kcal/mol"),
        Tmin = (712,"K"),
        Tmax = (779,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Knyazev et al. [153]""",
    longDesc = 
u"""
[153] Knayzev et al. Pressure ~ 0.01 atm. Excitation : thermal, analysis : GC Iso-C4H8 + CH3 --> (CH3)2CCH2CH3
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 303,
    label = "Cd/H2_Cd/Nd2;C_methyl",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     {Cs,O} 0 {2,S}
6     {Cs,O} 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.51e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (6.7,"kcal/mol"),
        Tmin = (391,"K"),
        Tmax = (449,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Seres et al. [154] Data derived from fitting a complex mechanism.""",
    longDesc = 
u"""
[303] Seres et al. Data derived from fitting to a complex mechanism. Excitation : thermal, analysis : GC Iso-C4H8 + CH3 --> (CH3)2CCH2CH3
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 304,
    label = "Cd/H/Nd_Cd/H2;H_rad",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     {Cs,O} 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (1.3e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (3.26,"kcal/mol"),
        Tmin = (500,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [149] experiments and limited review.""",
    longDesc = 
u"""
[149] Tsang experiments and limited review. CH3CH=CH2 + H --> n-C3H7
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 305,
    label = "Cd/H/Nd_Cd/H2;C_methyl",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     {Cs,O} 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (10000,"cm^3/(mol*s)"),
        n = 2.57,
        alpha = 0,
        E0 = (7.71,"kcal/mol"),
        Tmin = (298,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Knyazev et al. [147]""",
    longDesc = 
u"""
[147] Knyazev et al. Pressure up to 10 atm. Excitation : thermal, analysis : mass spectrometry. 
CH3CH=CH2 + CH3 --> iso-C4H9
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 306,
    label = "Cd/H/Nd_Cd/H2;C_methyl",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     {Cs,O} 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (9.64e+10,"cm^3/(mol*s)","*|/",3),
        n = 0,
        alpha = 0,
        E0 = (8.01,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [93] literature review.""",
    longDesc = 
u"""
[93] literature review. CH3CH=CH2 + CH3 --> iso-C4H9
pg.237-239: Discussion on evaluated data

Entry 46,16(b): Recommended rate coefficient is from reverse rate and equilibrium constant.

Author notes that rxn is pressure dependent and lists fall-off ratios and
collision efficiencies; these are not stored in RMG.
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 307,
    label = "Cd/Nd2_Cd/H2;C_methyl",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cs,O} 0 {1,S}
4     {Cs,O} 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.23e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (10.59,"kcal/mol"),
        Tmin = (560,"K"),
        Tmax = (650,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Slagle et al. [155] Data derived from detailed balance/reverse rate.""",
    longDesc = 
u"""
[155] Slagle et al. Data deriver from detailed balance/reverse rate. Pressure ~ 0.01 atm. 
Iso-C4H8 + .CH3 --> (CH3)3CCH2
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 308,
    label = "Cd/H2_Ca;H_rad",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cdd 0 {1,D} {5,D}
3     H 0 {1,S}
4     H 0 {1,S}
5     C 0 {2,D}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (1e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (1.2,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] in his reaction type 3. Based on recommendations of Allara and Shaw [146]""",
    longDesc = 
u"""
[8] Curran et al. in his reaction type 3. Based on recommendations of Allara and Shaw. [146]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 309,
    label = "Cd/H/Nd_Ca;H_rad",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cdd 0 {1,D} {5,D}
3     H 0 {1,S}
4     {Cs,O} 0 {1,S}
5     C 0 {2,D}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (1e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (2.9,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] in his reaction type 3. Based on recommendations of Allara and Shaw [146]""",
    longDesc = 
u"""
[8] Curran et al. in his reaction type 3. Based on recommendations of Allara and Shaw. [146]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 310,
    label = "Cd/Nd2_Ca;H_rad",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cdd 0 {1,D} {5,D}
3     {Cs,O} 0 {1,S}
4     {Cs,O} 0 {1,S}
5     C 0 {2,D}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (1e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (2.9,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] in his reaction type 3. Based on recommendations of Allara and Shaw [146]""",
    longDesc = 
u"""
[8] Curran et al. in his reaction type 3. Based on recommendations of Allara and Shaw. [146]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 311,
    label = "Cd/H2_Ca;Cs_rad",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cdd 0 {1,D} {5,D}
3     H 0 {1,S}
4     H 0 {1,S}
5     C 0 {2,D}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     R 0 {1,S}
3     R 0 {1,S}
4     R 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (8.5e+10,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (7.8,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] in his reaction type 3. Based on recommendations of Allara and Shaw [146]""",
    longDesc = 
u"""
[8] Curran et al. in his reaction type 3. Based on recommendations of Allara and Shaw. [146]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 312,
    label = "Cd/H/Nd_Ca;Cs_rad",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cdd 0 {1,D} {5,D}
3     H 0 {1,S}
4     {Cs,O} 0 {1,S}
5     C 0 {2,D}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     R 0 {1,S}
3     R 0 {1,S}
4     R 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (8.5e+10,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (10.6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] in his reaction type 3. Based on recommendations of Allara and Shaw [146]""",
    longDesc = 
u"""
[8] Curran et al. in his reaction type 3. Based on recommendations of Allara and Shaw. [146]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 313,
    label = "Cd/Nd2_Ca;Cs_rad",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cdd 0 {1,D} {5,D}
3     {Cs,O} 0 {1,S}
4     {Cs,O} 0 {1,S}
5     C 0 {2,D}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     R 0 {1,S}
3     R 0 {1,S}
4     R 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (8.5e+10,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (10.6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] in his reaction type 3. Based on recommendations of Allara and Shaw [146]""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 314,
    label = "Cd/H2_Ca;C_methyl",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cdd 0 {1,D} {5,D}
3     H 0 {1,S}
4     H 0 {1,S}
5     C 0 {2,D}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.75e+10,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (6.84,"kcal/mol","+|-",0.2),
        Tmin = (573,"K"),
        Tmax = (595,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Scherzer et al. [156] Data derived from fitting a complex mechanism.""",
    longDesc = 
u"""
[156] Scherzer et al. Data derived from fitting to a complex mechanism. Pressure 0.04 atm. Excitation: thermal, analysis: GC.
CH2=C=CH2 + .CH3 --> CH3CH2C=CH2
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 315,
    label = "Ca_Cd/H2;H_rad",
    group1 = 
"""
1  *1 Cdd 0 {2,D} {3,D}
2  *2 Cd 0 {1,D} {4,S} {5,S}
3     C 0 {1,D}
4     H 0 {2,S}
5     H 0 {2,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (1.2e+11,"cm^3/(mol*s)","*|/",2.5),
        n = 0.69,
        alpha = 0,
        E0 = (3,"kcal/mol"),
        Tmin = (350,"K"),
        Tmax = (1200,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang et al. [157]""",
    longDesc = 
u"""
[157] Tsang et al. Absolute Value Measured directly. Pressure 2 - 7 atm. Excitation: thermal, analysis : GC. 
CH2=C=CH2 + H --> .CH2CH=CH2
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 316,
    label = "Ca_Cd/H2;C_methyl",
    group1 = 
"""
1  *1 Cdd 0 {2,D} {3,D}
2  *2 Cd 0 {1,D} {4,S} {5,S}
3     C 0 {1,D}
4     H 0 {2,S}
5     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.58e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (4.97,"kcal/mol"),
        Tmin = (996,"K"),
        Tmax = (1180,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Tsang [158] Data is estimated.""",
    longDesc = 
u"""
[158] Tsang. Data is estimated. Pressure 1.50-5.00 atm. CH2=C=CH2 + CH3 --> CH2C(CH3)=CH2
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 317,
    label = "CO_O;H_rad",
    group1 = 
"""
1  *1 CO 0 {2,D}
2  *2 Od 0 {1,D}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (1e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (11.9,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] in his reaction type 18.""",
    longDesc = 
u"""
[8] Curran et al. In his reaction type 18.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 318,
    label = "CO_O;Cs_rad",
    group1 = 
"""
1  *1 CO 0 {2,D}
2  *2 Od 0 {1,D}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     R 0 {1,S}
3     R 0 {1,S}
4     R 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (11.9,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] in his reaction type 18.""",
    longDesc = 
u"""
[8] Curran et al. In his reaction type 18.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 319,
    label = "CO_O;CO_pri_rad",
    group1 = 
"""
1  *1 CO 0 {2,D}
2  *2 Od 0 {1,D}
""",
    group2 = 
"""
1  *3 C 1 {2,D} {3,S}
2     O 0 {1,D}
3     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.2e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (6.56,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Bozzelli et al. [144] based on CH3 addition to CO (Anastasi and Maw)""",
    longDesc = 
u"""
[144] Bozzelli et al. Based upon CH3 addition to CO (Anastasi and Maw)
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 320,
    label = "CO_O;O_rad/OneDe",
    group1 = 
"""
1  *1 CO 0 {2,D}
2  *2 Od 0 {1,D}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.3e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (7.4,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran esitmation [159] in DME oxidation modeling for ketohydroperoxide decomposition.""",
    longDesc = 
u"""
[159] Curran et al. His estimation in DME oxidation modeling for ketohydroperoxide decomposition. 
H2CO + HCO2. (formic acid radical) --> +  .OCH2OCHO (ester) (Rxn. 338, p. 234)

Verified by Greg Magoon; it is not immediately clear whether this rate constant is for high pressure limit, but based on other references to high pressure limit in the paper, I suspect that it is a high pressure limit value; also, note that CO_O group is used for H2CO...MRH and I have interpreted CO_O as referring to any carbonyl group
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 321,
    label = "CO/H2_O;C_rad/H2/Cs",
    group1 = 
"""
1  *1 CO 0 {2,D} {3,S} {4,S}
2  *2 Od 0 {1,D}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7.94e+10,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (6.7,"kcal/mol","+|-",0.47),
        Tmin = (333,"K"),
        Tmax = (363,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Knoll et al. [160] Data derived from fitting a complex mechanism.""",
    longDesc = 
u"""
[160] Knoll et al. Data derived from fitting to a complex mechanism. Pressure 0.08 atm. Excitation : direct photolysis, analysis : mass spectrometry.
N-C3H7 + C2HO --> N-C4H9O
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 322,
    label = "CO/Nd2_O;C_methyl",
    group1 = 
"""
1  *1 CO 0 {2,D} {3,S} {4,S}
2  *2 Od 0 {1,D}
3     {Cs,O} 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.16e+10,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (11.51,"kcal/mol","+|-",1.15),
        Tmin = (413,"K"),
        Tmax = (563,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Knoll et al. [161]""",
    longDesc = 
u"""
[161] Knoll et al. Absolute value measured directly. Pressure 0.28 - 1.17 atm. Excitation : thermal, analysis : mass spectrometry. 
(CH3)2CO + .CH3 --> (CH3)3CO
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 323,
    label = "Ct/H_Ct/H;H_rad",
    group1 = 
"""
1  *1 Ct 0 {2,T} {3,S}
2  *2 Ct 0 {1,T} {4,S}
3     H 0 {1,S}
4     H 0 {2,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (2.75e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (2.42,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Warnatz [134] literature review.""",
    longDesc = 
u"""
[134] Warnatz literature review. C.D.W divided rate expression by 2, to get rate of addition per site.
C2H2 + H --> C2H3
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 324,
    label = "Ct/H_Ct/H;C_methyl",
    group1 = 
"""
1  *1 Ct 0 {2,T} {3,S}
2  *2 Ct 0 {1,T} {4,S}
3     H 0 {1,S}
4     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.875e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (7.77,"kcal/mol"),
        Tmin = (370,"K"),
        Tmax = (478,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""E.W. Diau and M.C. Lin [162] RRK(M) extrapolation.""",
    longDesc = 
u"""
[162] E.W.Diau and M.C.Lin. RRK(M) extrapolation. C.D.W divided rate expression by 2, to get rate of addition per site. 
C2H2 + CH3 --> CH3CH=CH
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 325,
    label = "Ct/H_Ct/H;C_rad/H2/Cs",
    group1 = 
"""
1  *1 Ct 0 {2,T} {3,S}
2  *2 Ct 0 {1,T} {4,S}
3     H 0 {1,S}
4     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.505e+10,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (6.99,"kcal/mol"),
        Tmin = (373,"K"),
        Tmax = (473,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Kerr et al. [163] literature review.""",
    longDesc = 
u"""
[163] Kerr et al. literature review. Pressure 0.03-0.20 atm. C.D.W divided rate expression by 2, to get rate of addition per site.
C2H2 + .C2H5 --> CH3CH2CH=CH
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 326,
    label = "Ct/H_Ct/H;C_rad/H2/Cd",
    group1 = 
"""
1  *1 Ct 0 {2,T} {3,S}
2  *2 Ct 0 {1,T} {4,S}
3     H 0 {1,S}
4     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.595e+10,"cm^3/(mol*s)","*|/",10),
        n = 0,
        alpha = 0,
        E0 = (6.96,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Tsang [93] literature review.""",
    longDesc = 
u"""
[93] Tsang et al. literature review. Pressure 0.03-0.20 atm. C.D.W divided rate expression by 2, to get rate of addition per site.
C2H2 + .CH2CH=CH2 --> CHCH2CH=CH 

pg.263: Discussion on evaluated data

Entry 47,20(a): Recommended rate coefficient is estimated from the addition of alkyl

radicals to C2H2.  Author notes that this could be used as an upper limit for
cyclopentadiene formation.
MRH 31-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 327,
    label = "Ct/H_Ct/H;C_rad/H/NonDeC",
    group1 = 
"""
1  *1 Ct 0 {2,T} {3,S}
2  *2 Ct 0 {1,T} {4,S}
3     H 0 {1,S}
4     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.505e+10,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (6.9,"kcal/mol"),
        Tmin = (363,"K"),
        Tmax = (577,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Kerr et al. [163] literature review.""",
    longDesc = 
u"""
[163] Kerr et al. literature review. Pressure 0.07-0.13 atm. C.D.W divided rate expression by 2, to get rate of addition per site.
C2H2 + Iso-C3H7 --> (CH3)2CHCH=CH
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 328,
    label = "Ct/H_Ct/H;C_rad/Cs3",
    group1 = 
"""
1  *1 Ct 0 {2,T} {3,S}
2  *2 Ct 0 {1,T} {4,S}
3     H 0 {1,S}
4     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     Cs 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.505e+10,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (5.31,"kcal/mol"),
        Tmin = (373,"K"),
        Tmax = (493,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Dominguez et al. [164] Data derived from fitting a complex mechanism.""",
    longDesc = 
u"""
[164] Dominguez et al. Data derived from fitting to a complex mechanism. Pressure 0.01-0.32 atm. Excitation : direct photolysis, analysis : GC. 
C2H2 + Tert-C4H9 --> (CH3)3CCH=CH C.D.W divided rate expression by 2, to get rate of addition per site.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 329,
    label = "Ct/H_Ct/H;Cd_pri_rad",
    group1 = 
"""
1  *1 Ct 0 {2,T} {3,S}
2  *2 Ct 0 {1,T} {4,S}
3     H 0 {1,S}
4     H 0 {2,S}
""",
    group2 = 
"""
1  *3 Cd 1 {2,D} {3,S}
2     Cd 0 {1,D}
3     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (125500,"cm^3/(mol*s)"),
        n = 1.9,
        alpha = 0,
        E0 = (2.11,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Weissman et al. [121] Transition state theory.""",
    longDesc = 
u"""
[121] Weissman et al. Transition state theory. C.D.W divided rate expression by 2, to get rate of addition per site.	
C2H2 + C2H3 --> CH2=CHCH=CH.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 330,
    label = "Ct/H_Ct/H;Cd_pri_rad",
    group1 = 
"""
1  *1 Ct 0 {2,T} {3,S}
2  *2 Ct 0 {1,T} {4,S}
3     H 0 {1,S}
4     H 0 {2,S}
""",
    group2 = 
"""
1  *3 Cd 1 {2,D} {3,S}
2     Cd 0 {1,D}
3     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.155e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (4.9,"kcal/mol"),
        Tmin = (700,"K"),
        Tmax = (1300,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Duran et al. [165] Ab initio.""",
    longDesc = 
u"""
[165] Duran et al. Ab initio. C.D.W divided rate expression by 2, to get rate of addition per site.
C2H2 + C2H3 --> CH2=CHCH=CH. (Rxn. -5?)

Verified by Greg Magoon: note: NIST seems to have values (http://kinetics.nist.gov/kinetics/Detail?id=1988DUR/AMO636:5 , which agree with RMG's original values) that are slightly diferent than this paper's values (p. 637); I can't seem to figure out where the NIST values are coming from (maybe Table 3?); therefore, I have changed rateLibrary to use paper parameters of 10^8.8 (/2) and 4.9 kcal/mol (these values seem to actually be taken from other publications, however), which I am assuming to be high-pressure values; also note that values from other sources are available in the NIST Kinetics Database
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 331,
    label = "Ct/H_Ct/H;Ct_rad",
    group1 = 
"""
1  *1 Ct 0 {2,T} {3,S}
2  *2 Ct 0 {1,T} {4,S}
3     H 0 {1,S}
4     H 0 {2,S}
""",
    group2 = 
"""
1  *3 Ct 1 {2,T}
2     Ct 0 {1,T}
""",
    kinetics = ArrheniusEP(
        A = (5e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (700,"K"),
        Tmax = (1300,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Duran et al. [165] Ab initio.""",
    longDesc = 
u"""
[165] Duran et al. Ab initio. C.D.W divided rate expression by 2, to get rate of addition per site.
C2H2 + CCH --> HC(tb)CCH=CH. (Rxn. 18?) 

NIST Record: http://kinetics.nist.gov/kinetics/Detail?id=1988DUR/AMO636:4
Verified by Greg Magoon: it looks like value is taken from Rxn 18 of Table 3 (1E10), and is apparently non-pressure dependent (and non-temp dependent); based on the table, it looks like Ref. 42 in this paper may be the ultimate source of the value?
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 332,
    label = "Ct/H_Ct/H;O_pri_rad",
    group1 = 
"""
1  *1 Ct 0 {2,T} {3,S}
2  *2 Ct 0 {1,T} {4,S}
3     H 0 {1,S}
4     H 0 {2,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (6.05e+11,"cm^3/(mol*s)","*|/",10),
        n = 0,
        alpha = 0,
        E0 = (0.46,"kcal/mol"),
        Tmin = (298,"K"),
        Tmax = (1100,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Baulch et al. [95] literature review.""",
    longDesc = 
u"""
[95] Baulch et al. literature review. C.D.W divided rate expression by 2, to get rate of addition per site.
C2H2 + .OH --> HOCH=CH

pg.583-584: Discussion on evaluated data

OH+C2H2(+m) --> C2H2OH(+m): "At temperatures below ~1100K and at atmospheric pressure,

the addition channel becomes important and shows a strong pressure dependence.
The following parameters give a reasonable representation of the high temperature data
for k and are also compatible with Atkinson's analysis at low temperature ..."
RMG stores the recommended high-pressure limit rate coefficient, k_inf.

MRH 31-Aug-2009
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 333,
    label = "Ct/H_Ct/H;O_pri_rad",
    group1 = 
"""
1  *1 Ct 0 {2,T} {3,S}
2  *2 Ct 0 {1,T} {4,S}
3     H 0 {1,S}
4     H 0 {2,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7.6e+07,"cm^3/(mol*s)"),
        n = 1.7,
        alpha = 0,
        E0 = (1,"kcal/mol"),
        Tmin = (250,"K"),
        Tmax = (2500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Miller et al. [166] Transition state theory.""",
    longDesc = 
u"""
[166] Miller et al. Transition State Theory. C.D.W divided rate expression by 2, to get rate of addition per site. 
Same reaction as #332, #333 ranked as more accurate in rate library than #332, but they are both from relatively old sources from the early '90s.  

C2H2 + .OH --> HOCH=CH
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 334,
    label = "Ct/H_Ct/H;O_sec_rad",
    group1 = 
"""
1  *1 Ct 0 {2,T} {3,S}
2  *2 Ct 0 {1,T} {4,S}
3     H 0 {1,S}
4     H 0 {2,S}
""",
    group2 = 
"""
1  *3 O 1 {2,S}
2     R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.2e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (7.9,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Bozzelli et al. [144] based on CH3 addition to C2H2 (NIST)""",
    longDesc = 
u"""
[144] Bozzelli et al. Based upon CH3 addition to C2H2 (NIST)
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 335,
    label = "Cd/H2_Cd/H2;C_methyl",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (9.69e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (9,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 336,
    label = "Cd/H2_Cd/H2;C_rad/H2/Cs",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.94e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (8.2,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 337,
    label = "Cd/H2_Cd/H2;C_rad/H2/Cs",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.78e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (8,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 338,
    label = "Cd/H2_Cd/H2;C_rad/H2/Cs",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.92e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (7.6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 339,
    label = "Cd/H2_Cd/H2;C_rad/H2/Cs",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.58e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (8.3,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 340,
    label = "Cd/H2_Cd/H2;C_rad/H2/Cs",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.1e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (7.6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 341,
    label = "Cd/H2_Cd/H2;C_rad/H/NonDeC",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.73e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 342,
    label = "Cd/H2_Cd/H2;C_rad/Cs3",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     Cs 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.41e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (5.5,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 343,
    label = "Cd/H2_Cd/H2;C_rad/Cs3",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     Cs 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.05e+09,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (5.3,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 344,
    label = "Cd/H2_Cd/H2;C_rad/Cs3",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     Cs 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (8.54e+09,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (7.4,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 345,
    label = "Cd/H2_Cd/H2;C_rad/H2/Cd",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7.15e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (14.4,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 346,
    label = "Cd/H2_Cd/H2;C_rad/H2/Cd",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.44e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (14.6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 347,
    label = "Cd/H2_Cd/H2;C_rad/H/OneDeC",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.38e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (14,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 348,
    label = "Cd/H2_Cd/H2;C_rad/H/TwoDe",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.08e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (20,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 349,
    label = "Cd/H2_Cd/H2;C_rad/Cs2",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.83e+10,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (13.1,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 350,
    label = "Cd/H2_Cd/H2;C_rad/Cs",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.78e+10,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (19.3,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 351,
    label = "Cd/H2_Cd/H2;C_rad/H2/Cb",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cb 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (6.64e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (11.9,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 352,
    label = "Cd/H2_Cd/H2;C_rad/H2/Ct",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.25e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (12,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 353,
    label = "Cd/H2_Cd/H2;C_rad/H/OneDeC",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.36e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (11.4,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 354,
    label = "Cd/H2_Cd/H2;C_rad/Cs2",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7e+10,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (10.8,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 355,
    label = "Cd/H2_Cd/H2;Cd_pri_rad",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 Cd 1 {2,D} {3,S}
2     Cd 0 {1,D}
3     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.09e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (5.2,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 356,
    label = "Cd/H2_Cd/H2;Cd_rad/NonDe",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 Cd 1 {2,D} {3,S}
2     Cd 0 {1,D}
3     {Cs,O} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7.24e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (4.5,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 357,
    label = "Cd/H2_Cd/H2;Cb_rad",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 Cb 1 {2,B} {3,B}
2     {Cb,Cbf} 0 {1,B}
3     {Cb,Cbf} 0 {1,B}
""",
    kinetics = ArrheniusEP(
        A = (1.68e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (2.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 358,
    label = "Cd/H2_Cd/H2;C_methyl",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (9.69e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (9,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 359,
    label = "Cd/H2_Cd/H/Nd;C_methyl",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     {Cs,O} 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.1e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (8.5,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 360,
    label = "Cd/H2_Cd/H/Nd;C_methyl",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     {Cs,O} 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.22e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (8.4,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 361,
    label = "Cd/H2_Cd/Nd2;C_methyl",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     {Cs,O} 0 {2,S}
6     {Cs,O} 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.99e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (8,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 362,
    label = "Cd/H2_Cd/H/De;C_methyl",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7.3e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (5.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 363,
    label = "Ca_Cd/H/Nd;C_methyl",
    group1 = 
"""
1  *1 Cdd 0 {2,D} {3,D}
2  *2 Cd 0 {1,D} {4,S} {5,S}
3     C 0 {1,D}
4     H 0 {2,S}
5     {Cs,O} 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7.59e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (9.8,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 364,
    label = "Cd/H2_Cd/Nd/De;C_methyl",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     {Cs,O} 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.12e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (5.2,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 365,
    label = "Ca_Cd/Nd2;C_methyl",
    group1 = 
"""
1  *1 Cdd 0 {2,D} {3,D}
2  *2 Cd 0 {1,D} {4,S} {5,S}
3     C 0 {1,D}
4     {Cs,O} 0 {2,S}
5     {Cs,O} 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.86e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (8.8,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 366,
    label = "Ct/H_Ct/H;C_methyl",
    group1 = 
"""
1  *1 Ct 0 {2,T} {3,S}
2  *2 Ct 0 {1,T} {4,S}
3     H 0 {1,S}
4     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.06e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (9.9,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 367,
    label = "Ct/H_Ct/Nd;C_methyl",
    group1 = 
"""
1  *1 Ct 0 {2,T} {3,S}
2  *2 Ct 0 {1,T} {4,S}
3     H 0 {1,S}
4     {Cs,O} 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.32e+14,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (10.3,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 368,
    label = "Cd/H2_Ca;C_methyl",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cdd 0 {1,D} {5,D}
3     H 0 {1,S}
4     H 0 {1,S}
5     C 0 {2,D}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (9.23e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (9.4,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 369,
    label = "Cd/H2_Cd/H/De;C_methyl",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.18e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (7.4,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 370,
    label = "Cd/H2_Cd/De2;C_methyl",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.58e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (3.5,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 371,
    label = "Cd/H2_Cd/H/De;C_methyl",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.37e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (5.5,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 372,
    label = "Ct/H_Ct/De;C_methyl",
    group1 = 
"""
1  *1 Ct 0 {2,T} {3,S}
2  *2 Ct 0 {1,T} {4,S}
3     H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.19e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (7.1,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 373,
    label = "Cd/H2_Cd/Nd/De;C_methyl",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     {Cs,O} 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.32e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (5.3,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 374,
    label = "Cd/H/Nd_Cd/H2;C_methyl",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     {Cs,O} 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.36e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (10.1,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 375,
    label = "Cd/H/Nd_Cd/H2;C_methyl",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     {Cs,O} 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (6.42e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (11.1,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 376,
    label = "Cd/H/Nd_Cd/H2;C_methyl",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     {Cs,O} 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (6.24e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (11.2,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 377,
    label = "Cd/Nd2_Cd/H2;C_methyl",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cs,O} 0 {1,S}
4     {Cs,O} 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.12e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (11.2,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 378,
    label = "Cd/Nd2_Cd/H2;C_methyl",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cs,O} 0 {1,S}
4     {Cs,O} 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.51e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (12.5,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 379,
    label = "Cd/H/De_Cd/H2;C_methyl",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.43e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (10.2,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 380,
    label = "Cd/Nd/De_Cd/H2;C_methyl",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cs,O} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.92e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (11.2,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 381,
    label = "Ct/Nd_Ct/H;C_methyl",
    group1 = 
"""
1  *1 Ct 0 {2,T} {3,S}
2  *2 Ct 0 {1,T} {4,S}
3     {Cs,O} 0 {1,S}
4     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.99e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (12.1,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 382,
    label = "Cd/H/De_Cd/H2;C_methyl",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.24e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (11.1,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 383,
    label = "Cd/H/De_Cd/H2;C_methyl",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.36e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (9.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 384,
    label = "Ct/De_Ct/H;C_methyl",
    group1 = 
"""
1  *1 Ct 0 {2,T} {3,S}
2  *2 Ct 0 {1,T} {4,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.49e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (11.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 385,
    label = "Ct/De_Ct/H;C_methyl",
    group1 = 
"""
1  *1 Ct 0 {2,T} {3,S}
2  *2 Ct 0 {1,T} {4,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.71e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (11.4,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 386,
    label = "Cd/Nd/De_Cd/H2;C_methyl",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cs,O} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (6.07e+11,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (11,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 387,
    label = "Cd/H2_Cd/H2;H_rad",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (7.74e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (2.8,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 388,
    label = "Cd/H2_Cd/H/Nd;H_rad",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     {Cs,O} 0 {2,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (2.01e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (2.1,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 389,
    label = "Cd/H2_Cd/Nd2;H_rad",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     {Cs,O} 0 {2,S}
6     {Cs,O} 0 {2,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (4.94e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (1.5,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 390,
    label = "Cd/H2_Cd/H/De;H_rad",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (3.71e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (1,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 391,
    label = "Cd/H2_Cd/Nd/De;H_rad",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     {Cs,O} 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (2.13e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (0.5,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 392,
    label = "Cd/H2_Cd/H/De;H_rad",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (1.97e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (3.2,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 393,
    label = "Cd/H2_Cd/Nd/De;H_rad",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     {Cs,O} 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (1.43e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (2.5,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 394,
    label = "Ct/H_Ct/H;H_rad",
    group1 = 
"""
1  *1 Ct 0 {2,T} {3,S}
2  *2 Ct 0 {1,T} {4,S}
3     H 0 {1,S}
4     H 0 {2,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (1.16e+14,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (3.8,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 395,
    label = "Ct/H_Ct/Nd;H_rad",
    group1 = 
"""
1  *1 Ct 0 {2,T} {3,S}
2  *2 Ct 0 {1,T} {4,S}
3     H 0 {1,S}
4     {Cs,O} 0 {2,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (1.12e+14,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (3.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 396,
    label = "Cd/H2_Ca;H_rad",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cdd 0 {1,D} {5,D}
3     H 0 {1,S}
4     H 0 {1,S}
5     C 0 {2,D}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (6.68e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (2.9,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 397,
    label = "Cd/H2_Ca;H_rad",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cdd 0 {1,D} {5,D}
3     H 0 {1,S}
4     H 0 {1,S}
5     C 0 {2,D}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (2.73e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (2.6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 398,
    label = "Cd/H2_Cd/H/De;H_rad",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (1.82e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (1.4,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 399,
    label = "Cd/H2_Cd/Nd/De;H_rad",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     {Cs,O} 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (2.04e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (1,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 400,
    label = "Ct/H_Ct/De;H_rad",
    group1 = 
"""
1  *1 Ct 0 {2,T} {3,S}
2  *2 Ct 0 {1,T} {4,S}
3     H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (1.86e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (2.3,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 401,
    label = "Ct/H_Ct/De;H_rad",
    group1 = 
"""
1  *1 Ct 0 {2,T} {3,S}
2  *2 Ct 0 {1,T} {4,S}
3     H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (1.69e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (2.2,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 402,
    label = "Ct/H_Ct/De;H_rad",
    group1 = 
"""
1  *1 Ct 0 {2,T} {3,S}
2  *2 Ct 0 {1,T} {4,S}
3     H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (1.07e+14,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (2.1,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 403,
    label = "Ca_Cd/H/Nd;H_rad",
    group1 = 
"""
1  *1 Cdd 0 {2,D} {3,D}
2  *2 Cd 0 {1,D} {4,S} {5,S}
3     C 0 {1,D}
4     H 0 {2,S}
5     {Cs,O} 0 {2,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (1.28e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (3.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 404,
    label = "Ca_Cd/Nd2;H_rad",
    group1 = 
"""
1  *1 Cdd 0 {2,D} {3,D}
2  *2 Cd 0 {1,D} {4,S} {5,S}
3     C 0 {1,D}
4     {Cs,O} 0 {2,S}
5     {Cs,O} 0 {2,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (2.57e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (2.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 405,
    label = "Cd/H/Nd_Cd/H2;H_rad",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     {Cs,O} 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (1.18e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (3.8,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 406,
    label = "Cd/Nd2_Cd/H2;H_rad",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cs,O} 0 {1,S}
4     {Cs,O} 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (1.17e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (4.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 407,
    label = "Cd/H/De_Cd/H2;H_rad",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (2.85e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (4.3,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 408,
    label = "Cd/Nd/De_Cd/H2;H_rad",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cs,O} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (9.3e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (5.2,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 409,
    label = "Ct/Nd_Ct/H;H_rad",
    group1 = 
"""
1  *1 Ct 0 {2,T} {3,S}
2  *2 Ct 0 {1,T} {4,S}
3     {Cs,O} 0 {1,S}
4     H 0 {2,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (5.77e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (5.3,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 410,
    label = "Cd/H/De_Cd/H2;H_rad",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (1.67e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 411,
    label = "Cd/Nd/De_Cd/H2;H_rad",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cs,O} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (5.62e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (6.5,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 412,
    label = "Cd/H/De_Cd/H2;H_rad",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (1.33e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (4.6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 413,
    label = "Cd/Nd/De_Cd/H2;H_rad",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cs,O} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (8.2e+12,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (5.8,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 414,
    label = "Ct/De_Ct/H;H_rad",
    group1 = 
"""
1  *1 Ct 0 {2,T} {3,S}
2  *2 Ct 0 {1,T} {4,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     H 0 {2,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (2.25e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (5.4,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 415,
    label = "Ct/De_Ct/H;H_rad",
    group1 = 
"""
1  *1 Ct 0 {2,T} {3,S}
2  *2 Ct 0 {1,T} {4,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     H 0 {2,S}
""",
    group2 = 
"""
1  *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (9.99e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Mark Saeys, CBS-QB3 calculations, without hindered rotor treatment.""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 416,
    label = "Cd/H2_Cd/H2;Cd_pri_rad-Cdd/Cd",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 Cd 1 {2,D} {3,S}
2     Cdd 0 {1,D} {4,D}
3     H 0 {1,S}
4     Cd 0 {2,D}
""",
    kinetics = ArrheniusEP(
        A = (149.03,"cm^3/(mol*s)"),
        n = 3.0074,
        alpha = 0,
        E0 = (10.1708,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1600,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Sandeep CBS-QB3 calculations""",
    longDesc = 
u"""
Sandeep CBS-QB3 calculations
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

