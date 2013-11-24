#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_MultipleBond/rules"
shortDesc = u""
longDesc = u"""

"""
recommended = True

entry(
    index = 269,
    label = "XZ;Y_rad_birad_trirad_quadrad",
    group1 = "OR{CZ, SZ, OCO, OCddO, OSi, OSiddO, Od_N, N_R}",
    group2 = "OR{Y_rad, Y_birad, Y_1centertrirad, Y_2centerbirad, Y_1centerbirad, Y_1centerquadrad}",
    kinetics = ArrheniusEP(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 281,
    label = "Cd/H2;H_rad",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D}
3    H  0 {1,S}
4    H  0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (1.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 282,
    label = "Cd/H/NonDe;H_rad",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D}
3    H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (2.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 283,
    label = "Cd/NonDe2;H_rad",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D}
3    {Cs,O,S} 0 {1,S}
4    {Cs,O,S} 0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (2.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 284,
    label = "Cd/H2;Cs_rad",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D}
3    H  0 {1,S}
4    H  0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    R 0 {1,S}
3    R 0 {1,S}
4    R 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (85000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (7.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 285,
    label = "Cd/H/NonDe;Cs_rad",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D}
3    H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    R 0 {1,S}
3    R 0 {1,S}
4    R 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (85000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (10.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 286,
    label = "Cd/NonDe2;Cs_rad",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D}
3    {Cs,O,S} 0 {1,S}
4    {Cs,O,S} 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    R 0 {1,S}
3    R 0 {1,S}
4    R 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (85000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (10.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 287,
    label = "Cd/H2;O_rad/NonDe",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D}
3    H  0 {1,S}
4    H  0 {1,S}
""",
    group2 = 
"""
1 *3 O        1 {2,S}
2    {Cs,O,S} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (12.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 288,
    label = "Cd/H/NonDe;O_rad/NonDe",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D}
3    H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
""",
    group2 = 
"""
1 *3 O        1 {2,S}
2    {Cs,O,S} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 289,
    label = "Cd/NonDe2;O_rad/NonDe",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D}
3    {Cs,O,S} 0 {1,S}
4    {Cs,O,S} 0 {1,S}
""",
    group2 = 
"""
1 *3 O        1 {2,S}
2    {Cs,O,S} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (7.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 290,
    label = "Cd/H2_Cd/H2;H_rad",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (1985000000.0, 'cm^3/(mol*s)', '*|/', 2),
        n = 1.28,
        alpha = 0,
        E0 = (1.29, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (1100, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 291,
    label = "Cd/H2_Cd/H2;C_methyl",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (165500000000.0, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        alpha = 0,
        E0 = (7.71, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 292,
    label = "Cd/H2_Cd/H2;C_rad/H2/Cs",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1990, 'cm^3/(mol*s)'),
        n = 2.44,
        alpha = 0,
        E0 = (5.37, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 293,
    label = "Cd/H2_Cd/H2;C_rad/H2/O",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (24100000000.0, 'cm^3/(mol*s)', '*|/', 5),
        n = 0,
        alpha = 0,
        E0 = (6.96, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 294,
    label = "Cd/H2_Cd/H2;Cd_pri_rad",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    group2 = 
"""
1 *3 Cd 1 {2,D} {3,S}
2    Cd 0 {1,D}
3    H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (2.01, 'kcal/mol'),
        Tmin = (1260, 'K'),
        Tmax = (1310, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 295,
    label = "Cd/H2_Cd/H2;O_pri_rad",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2710000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 296,
    label = "Cd/H2_Cd/H/NonDe;H_rad",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    H        0 {1,S}
4    H        0 {1,S}
5    H        0 {2,S}
6    {Cs,O,S} 0 {2,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (13000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (1.56, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 297,
    label = "Cd/H2_Cd/H/NonDe;C_methyl",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    H        0 {1,S}
4    H        0 {1,S}
5    H        0 {2,S}
6    {Cs,O,S} 0 {2,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (128000, 'cm^3/(mol*s)'),
        n = 2.28,
        alpha = 0,
        E0 = (6.6, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 298,
    label = "Cd/H2_Cd/H/NonDe;C_methyl",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    H        0 {1,S}
4    H        0 {1,S}
5    H        0 {2,S}
6    {Cs,O,S} 0 {2,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (169000000000.0, 'cm^3/(mol*s)', '*|/', 1.4),
        n = 0,
        alpha = 0,
        E0 = (7.41, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 299,
    label = "Cd/H2_Cd/H/NonDe;C_rad/H2/Cd",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    H        0 {1,S}
4    H        0 {1,S}
5    H        0 {2,S}
6    {Cs,O,S} 0 {2,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (355000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (16.89, 'kcal/mol'),
        Tmin = (762, 'K'),
        Tmax = (811, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 300,
    label = "Cd/H2_Cd/H/NonDe;C_rad/Cs3",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    H        0 {1,S}
4    H        0 {1,S}
5    H        0 {2,S}
6    {Cs,O,S} 0 {2,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3070000000.0, 'cm^3/(mol*s)', '*|/', 10),
        n = 0,
        alpha = 0,
        E0 = (5.88, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 301,
    label = "Cd/H2_Cd/H/OneDe;C_methyl",
    group1 = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    H                0 {1,S}
4    H                0 {1,S}
5    H                0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (31550000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (7.49, 'kcal/mol'),
        Tmin = (743, 'K'),
        Tmax = (772, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 302,
    label = "Cd/H2_Cd/NonDe2;H_rad",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    H        0 {1,S}
4    H        0 {1,S}
5    {Cs,O,S} 0 {2,S}
6    {Cs,O,S} 0 {2,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (6210000000000.0, 'cm^3/(mol*s)'),
        n = 0.25,
        alpha = 0,
        E0 = (1.46, 'kcal/mol'),
        Tmin = (712, 'K'),
        Tmax = (779, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 303,
    label = "Cd/H2_Cd/NonDe2;C_methyl",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    H        0 {1,S}
4    H        0 {1,S}
5    {Cs,O,S} 0 {2,S}
6    {Cs,O,S} 0 {2,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (251000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (6.7, 'kcal/mol'),
        Tmin = (391, 'K'),
        Tmax = (449, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 304,
    label = "Cd/H/NonDe_Cd/H2;H_rad",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    H        0 {2,S}
6    H        0 {2,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (13000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (3.26, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 305,
    label = "Cd/H/NonDe_Cd/H2;C_methyl",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    H        0 {2,S}
6    H        0 {2,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (10000, 'cm^3/(mol*s)'),
        n = 2.57,
        alpha = 0,
        E0 = (7.71, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 306,
    label = "Cd/H/NonDe_Cd/H2;C_methyl",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    H        0 {2,S}
6    H        0 {2,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (96400000000.0, 'cm^3/(mol*s)', '*|/', 3),
        n = 0,
        alpha = 0,
        E0 = (8.01, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 307,
    label = "Cd/NonDe2_Cd/H2;C_methyl",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    {Cs,O,S} 0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    H        0 {2,S}
6    H        0 {2,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (223000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (10.59, 'kcal/mol'),
        Tmin = (560, 'K'),
        Tmax = (650, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 308,
    label = "Cd/H2_Ca;H_rad",
    group1 = 
"""
1 *1 Cd  0 {2,D} {3,S} {4,S}
2 *2 Cdd 0 {1,D} {5,D}
3    H   0 {1,S}
4    H   0 {1,S}
5    C   0 {2,D}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (1.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 309,
    label = "Cd/H/NonDe_Ca;H_rad",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cdd      0 {1,D} {5,D}
3    H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    C        0 {2,D}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (2.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 310,
    label = "Cd/NonDe2_Ca;H_rad",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cdd      0 {1,D} {5,D}
3    {Cs,O,S} 0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    C        0 {2,D}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (2.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 311,
    label = "Cd/H2_Ca;Cs_rad",
    group1 = 
"""
1 *1 Cd  0 {2,D} {3,S} {4,S}
2 *2 Cdd 0 {1,D} {5,D}
3    H   0 {1,S}
4    H   0 {1,S}
5    C   0 {2,D}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    R 0 {1,S}
3    R 0 {1,S}
4    R 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (85000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (7.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 312,
    label = "Cd/H/NonDe_Ca;Cs_rad",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cdd      0 {1,D} {5,D}
3    H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    C        0 {2,D}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    R 0 {1,S}
3    R 0 {1,S}
4    R 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (85000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (10.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 313,
    label = "Cd/NonDe2_Ca;Cs_rad",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cdd      0 {1,D} {5,D}
3    {Cs,O,S} 0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    C        0 {2,D}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    R 0 {1,S}
3    R 0 {1,S}
4    R 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (85000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (10.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran et al. [8] in his reaction type 3. Based on recommendations of Allara and Shaw [146]""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 314,
    label = "Cd/H2_Ca;C_methyl",
    group1 = 
"""
1 *1 Cd  0 {2,D} {3,S} {4,S}
2 *2 Cdd 0 {1,D} {5,D}
3    H   0 {1,S}
4    H   0 {1,S}
5    C   0 {2,D}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (57500000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (6.84, 'kcal/mol', '+|-', 0.2),
        Tmin = (573, 'K'),
        Tmax = (595, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 315,
    label = "Ca_Cd/H2;H_rad",
    group1 = 
"""
1 *1 Cdd 0 {2,D} {3,D}
2 *2 Cd  0 {1,D} {4,S} {5,S}
3    C   0 {1,D}
4    H   0 {2,S}
5    H   0 {2,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (120000000000.0, 'cm^3/(mol*s)', '*|/', 2.5),
        n = 0.69,
        alpha = 0,
        E0 = (3, 'kcal/mol'),
        Tmin = (350, 'K'),
        Tmax = (1200, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 316,
    label = "Ca_Cd/H2;C_methyl",
    group1 = 
"""
1 *1 Cdd 0 {2,D} {3,D}
2 *2 Cd  0 {1,D} {4,S} {5,S}
3    C   0 {1,D}
4    H   0 {2,S}
5    H   0 {2,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (158000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (4.97, 'kcal/mol'),
        Tmin = (996, 'K'),
        Tmax = (1180, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 317,
    label = "CO_O;H_rad",
    group1 = 
"""
1 *1 CO 0 {2,D}
2 *2 Od 0 {1,D}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (11.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 318,
    label = "CO_O;Cs_rad",
    group1 = 
"""
1 *1 CO 0 {2,D}
2 *2 Od 0 {1,D}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    R 0 {1,S}
3    R 0 {1,S}
4    R 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (11.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 319,
    label = "CO_O;CO_pri_rad",
    group1 = 
"""
1 *1 CO 0 {2,D}
2 *2 Od 0 {1,D}
""",
    group2 = 
"""
1 *3 C 1 {2,D} {3,S}
2    O 0 {1,D}
3    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (520000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (6.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 320,
    label = "CO_O;O_rad/OneDe",
    group1 = 
"""
1 *1 CO 0 {2,D}
2 *2 Od 0 {1,D}
""",
    group2 = 
"""
1 *3 O                1 {2,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (130000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (7.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 321,
    label = "CO/H2_O;C_rad/H2/Cs",
    group1 = 
"""
1 *1 CO 0 {2,D} {3,S} {4,S}
2 *2 Od 0 {1,D}
3    H  0 {1,S}
4    H  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (79400000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (6.7, 'kcal/mol', '+|-', 0.47),
        Tmin = (333, 'K'),
        Tmax = (363, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 322,
    label = "CO/NonDe2_O;C_methyl",
    group1 = 
"""
1 *1 CO       0 {2,D} {3,S} {4,S}
2 *2 Od       0 {1,D}
3    {Cs,O,S} 0 {1,S}
4    {Cs,O,S} 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (31600000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (11.51, 'kcal/mol', '+|-', 1.15),
        Tmin = (413, 'K'),
        Tmax = (563, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 323,
    label = "Ct/H_Ct/H;H_rad",
    group1 = 
"""
1 *1 Ct 0 {2,T} {3,S}
2 *2 Ct 0 {1,T} {4,S}
3    H  0 {1,S}
4    H  0 {2,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (2750000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (2.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 324,
    label = "Ct/H_Ct/H;C_methyl",
    group1 = 
"""
1 *1 Ct 0 {2,T} {3,S}
2 *2 Ct 0 {1,T} {4,S}
3    H  0 {1,S}
4    H  0 {2,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (187500000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (7.77, 'kcal/mol'),
        Tmin = (370, 'K'),
        Tmax = (478, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 325,
    label = "Ct/H_Ct/H;C_rad/H2/Cs",
    group1 = 
"""
1 *1 Ct 0 {2,T} {3,S}
2 *2 Ct 0 {1,T} {4,S}
3    H  0 {1,S}
4    H  0 {2,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (25050000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (6.99, 'kcal/mol'),
        Tmin = (373, 'K'),
        Tmax = (473, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 326,
    label = "Ct/H_Ct/H;C_rad/H2/Cd",
    group1 = 
"""
1 *1 Ct 0 {2,T} {3,S}
2 *2 Ct 0 {1,T} {4,S}
3    H  0 {1,S}
4    H  0 {2,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (15950000000.0, 'cm^3/(mol*s)', '*|/', 10),
        n = 0,
        alpha = 0,
        E0 = (6.96, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 327,
    label = "Ct/H_Ct/H;C_rad/H/NonDeC",
    group1 = 
"""
1 *1 Ct 0 {2,T} {3,S}
2 *2 Ct 0 {1,T} {4,S}
3    H  0 {1,S}
4    H  0 {2,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (25050000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (6.9, 'kcal/mol'),
        Tmin = (363, 'K'),
        Tmax = (577, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 328,
    label = "Ct/H_Ct/H;C_rad/Cs3",
    group1 = 
"""
1 *1 Ct 0 {2,T} {3,S}
2 *2 Ct 0 {1,T} {4,S}
3    H  0 {1,S}
4    H  0 {2,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (25050000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (5.31, 'kcal/mol'),
        Tmin = (373, 'K'),
        Tmax = (493, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 329,
    label = "Ct/H_Ct/H;Cd_pri_rad",
    group1 = 
"""
1 *1 Ct 0 {2,T} {3,S}
2 *2 Ct 0 {1,T} {4,S}
3    H  0 {1,S}
4    H  0 {2,S}
""",
    group2 = 
"""
1 *3 Cd 1 {2,D} {3,S}
2    Cd 0 {1,D}
3    H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (125500, 'cm^3/(mol*s)'),
        n = 1.9,
        alpha = 0,
        E0 = (2.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 330,
    label = "Ct/H_Ct/H;Cd_pri_rad",
    group1 = 
"""
1 *1 Ct 0 {2,T} {3,S}
2 *2 Ct 0 {1,T} {4,S}
3    H  0 {1,S}
4    H  0 {2,S}
""",
    group2 = 
"""
1 *3 Cd 1 {2,D} {3,S}
2    Cd 0 {1,D}
3    H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (315500000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (4.9, 'kcal/mol'),
        Tmin = (700, 'K'),
        Tmax = (1300, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Duran et al. [165] Ab initio.""",
    longDesc = 
u"""
[165] Duran et al. Ab initio. C.D.W divided rate expression by 2, to get rate of addition per site.
C2H2 + C2H3 --> CH2=CHCH=CH. (Rxn. -5?)

Verified by Greg Magoon: note: NIST seems to have values (http://kinetics.nist.gov/kinetics/OneDetail?id=1988DUR/AMO636:5 , which agree with RMG's original values) that are slightly diferent than this paper's values (p. 637); I can't seem to figure out where the NIST values are coming from (maybe Table 3?); therefore, I have changed rateLibrary to use paper parameters of 10^8.8 (/2) and 4.9 kcal/mol (these values seem to actually be taken from other publications, however), which I am assuming to be high-pressure values; also note that values from other sources are available in the NIST Kinetics Database
""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 331,
    label = "Ct/H_Ct/H;Ct_rad/Ct",
    group1 = 
"""
1 *1 Ct 0 {2,T} {3,S}
2 *2 Ct 0 {1,T} {4,S}
3    H  0 {1,S}
4    H  0 {2,S}
""",
    group2 = 
"""
1 *3 Ct 1 {2,T}
2    Ct 0 {1,T}
""",
    kinetics = ArrheniusEP(
        A = (5000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (700, 'K'),
        Tmax = (1300, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Duran et al. [165] Ab initio.""",
    longDesc = 
u"""
[165] Duran et al. Ab initio. C.D.W divided rate expression by 2, to get rate of addition per site.
C2H2 + CCH --> HC(tb)CCH=CH. (Rxn. 18?) 

NIST Record: http://kinetics.nist.gov/kinetics/OneDetail?id=1988DUR/AMO636:4
Verified by Greg Magoon: it looks like value is taken from Rxn 18 of Table 3 (1E10), and is apparently non-pressure dependent (and non-temp dependent); based on the table, it looks like Ref. 42 in this paper may be the ultimate source of the value?
""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 332,
    label = "Ct/H_Ct/H;O_pri_rad",
    group1 = 
"""
1 *1 Ct 0 {2,T} {3,S}
2 *2 Ct 0 {1,T} {4,S}
3    H  0 {1,S}
4    H  0 {2,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (605000000000.0, 'cm^3/(mol*s)', '*|/', 10),
        n = 0,
        alpha = 0,
        E0 = (0.46, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (1100, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 333,
    label = "Ct/H_Ct/H;O_pri_rad",
    group1 = 
"""
1 *1 Ct 0 {2,T} {3,S}
2 *2 Ct 0 {1,T} {4,S}
3    H  0 {1,S}
4    H  0 {2,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (76000000.0, 'cm^3/(mol*s)'),
        n = 1.7,
        alpha = 0,
        E0 = (1, 'kcal/mol'),
        Tmin = (250, 'K'),
        Tmax = (2500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 334,
    label = "Ct/H_Ct/H;O_sec_rad",
    group1 = 
"""
1 *1 Ct 0 {2,T} {3,S}
2 *2 Ct 0 {1,T} {4,S}
3    H  0 {1,S}
4    H  0 {2,S}
""",
    group2 = 
"""
1 *3 O   1 {2,S}
2    R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (520000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (7.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 335,
    label = "Cd/H2_Cd/H2;C_methyl",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (9690000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 336,
    label = "Cd/H2_Cd/H2;C_rad/H2/Cs",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (294000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (8.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 337,
    label = "Cd/H2_Cd/H2;C_rad/H2/Cs",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (378000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 338,
    label = "Cd/H2_Cd/H2;C_rad/H2/Cs",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (292000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (7.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 339,
    label = "Cd/H2_Cd/H2;C_rad/H2/Cs",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (258000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (8.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 340,
    label = "Cd/H2_Cd/H2;C_rad/H2/Cs",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (110000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (7.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 341,
    label = "Cd/H2_Cd/H2;C_rad/H/NonDeC",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (173000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 342,
    label = "Cd/H2_Cd/H2;C_rad/Cs3",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (241000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (5.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 343,
    label = "Cd/H2_Cd/H2;C_rad/Cs3",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2050000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (5.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 344,
    label = "Cd/H2_Cd/H2;C_rad/Cs3",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (8540000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (7.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 345,
    label = "Cd/H2_Cd/H2;C_rad/H2/Cd",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (715000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (14.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 346,
    label = "Cd/H2_Cd/H2;C_rad/H2/Cd",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (544000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (14.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 347,
    label = "Cd/H2_Cd/H2;C_rad/H/OneDeC",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    group2 = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    Cs               0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (238000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 348,
    label = "Cd/H2_Cd/H2;C_rad/H/TwoDe",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    group2 = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1080000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (20, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 349,
    label = "Cd/H2_Cd/H2;C_rad/Cs2",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    group2 = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
3    Cs               0 {1,S}
4    Cs               0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (38300000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (13.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 350,
    label = "Cd/H2_Cd/H2;C_rad/Cs",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    group2 = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    Cs               0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (37800000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (19.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 351,
    label = "Cd/H2_Cd/H2;C_rad/H2/Cb",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cb 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (664000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (11.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 352,
    label = "Cd/H2_Cd/H2;C_rad/H2/Ct",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1250000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 353,
    label = "Cd/H2_Cd/H2;C_rad/H/OneDeC",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    group2 = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    Cs               0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (136000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (11.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 354,
    label = "Cd/H2_Cd/H2;C_rad/Cs2",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    group2 = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
3    Cs               0 {1,S}
4    Cs               0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (70000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (10.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 355,
    label = "Cd/H2_Cd/H2;Cd_pri_rad",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    group2 = 
"""
1 *3 Cd 1 {2,D} {3,S}
2    Cd 0 {1,D}
3    H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (20900000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (5.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 356,
    label = "Cd/H2_Cd/H2;Cd_rad/NonDe",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    group2 = 
"""
1 *3 Cd       1 {2,D} {3,S}
2    Cd       0 {1,D}
3    {Cs,O,S} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7240000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (4.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 357,
    label = "Cd/H2_Cd/H2;Cb_rad",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    group2 = 
"""
1 *3 Cb       1 {2,B} {3,B}
2    {Cb,Cbf} 0 {1,B}
3    {Cb,Cbf} 0 {1,B}
""",
    kinetics = ArrheniusEP(
        A = (16800000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (2.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 358,
    label = "Cd/H2_Cd/H2;C_methyl",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (9690000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 359,
    label = "Cd/H2_Cd/H/NonDe;C_methyl",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    H        0 {1,S}
4    H        0 {1,S}
5    H        0 {2,S}
6    {Cs,O,S} 0 {2,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (8.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 360,
    label = "Cd/H2_Cd/H/NonDe;C_methyl",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    H        0 {1,S}
4    H        0 {1,S}
5    H        0 {2,S}
6    {Cs,O,S} 0 {2,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2220000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (8.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 361,
    label = "Cd/H2_Cd/NonDe2;C_methyl",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    H        0 {1,S}
4    H        0 {1,S}
5    {Cs,O,S} 0 {2,S}
6    {Cs,O,S} 0 {2,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3990000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 362,
    label = "Cd/H2_Cd/H/OneDe;C_methyl",
    group1 = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    H                0 {1,S}
4    H                0 {1,S}
5    H                0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (5.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 363,
    label = "Ca_Cd/H/NonDe;C_methyl",
    group1 = 
"""
1 *1 Cdd      0 {2,D} {3,D}
2 *2 Cd       0 {1,D} {4,S} {5,S}
3    C        0 {1,D}
4    H        0 {2,S}
5    {Cs,O,S} 0 {2,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7590000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (9.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 364,
    label = "Cd/H2_Cd/NonDe/OneDe;C_methyl",
    group1 = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    H                0 {1,S}
4    H                0 {1,S}
5    {Cs,O,S}         0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4120000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (5.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 365,
    label = "Ca_Cd/NonDe2;C_methyl",
    group1 = 
"""
1 *1 Cdd      0 {2,D} {3,D}
2 *2 Cd       0 {1,D} {4,S} {5,S}
3    C        0 {1,D}
4    {Cs,O,S} 0 {2,S}
5    {Cs,O,S} 0 {2,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (18600000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (8.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 366,
    label = "Ct/H_Ct/H;C_methyl",
    group1 = 
"""
1 *1 Ct 0 {2,T} {3,S}
2 *2 Ct 0 {1,T} {4,S}
3    H  0 {1,S}
4    H  0 {2,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (40600000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (9.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 367,
    label = "Ct/H_Ct/NonDe;C_methyl",
    group1 = 
"""
1 *1 Ct       0 {2,T} {3,S}
2 *2 Ct       0 {1,T} {4,S}
3    H        0 {1,S}
4    {Cs,O,S} 0 {2,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (132000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (10.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 368,
    label = "Cd/H2_Ca;C_methyl",
    group1 = 
"""
1 *1 Cd  0 {2,D} {3,S} {4,S}
2 *2 Cdd 0 {1,D} {5,D}
3    H   0 {1,S}
4    H   0 {1,S}
5    C   0 {2,D}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (9230000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (9.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 369,
    label = "Cd/H2_Cd/H/OneDe;C_methyl",
    group1 = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    H                0 {1,S}
4    H                0 {1,S}
5    H                0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (418000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (7.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 370,
    label = "Cd/H2_Cd/TwoDe;C_methyl",
    group1 = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    H                0 {1,S}
4    H                0 {1,S}
5    {Cd,Ct,Cb,CO,CS} 0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5580000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (3.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 371,
    label = "Cd/H2_Cd/H/OneDe;C_methyl",
    group1 = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    H                0 {1,S}
4    H                0 {1,S}
5    H                0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4370000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (5.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 372,
    label = "Ct/H_Ct/OneDe;C_methyl",
    group1 = 
"""
1 *1 Ct               0 {2,T} {3,S}
2 *2 Ct               0 {1,T} {4,S}
3    H                0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (11900000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (7.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 373,
    label = "Cd/H2_Cd/NonDe/OneDe;C_methyl",
    group1 = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    H                0 {1,S}
4    H                0 {1,S}
5    {Cs,O,S}         0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4320000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (5.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 374,
    label = "Cd/H/NonDe_Cd/H2;C_methyl",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    H        0 {2,S}
6    H        0 {2,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1360000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (10.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 375,
    label = "Cd/H/NonDe_Cd/H2;C_methyl",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    H        0 {2,S}
6    H        0 {2,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (642000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (11.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 376,
    label = "Cd/H/NonDe_Cd/H2;C_methyl",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    H        0 {2,S}
6    H        0 {2,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (624000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (11.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 377,
    label = "Cd/NonDe2_Cd/H2;C_methyl",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    {Cs,O,S} 0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    H        0 {2,S}
6    H        0 {2,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1120000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (11.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 378,
    label = "Cd/NonDe2_Cd/H2;C_methyl",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    {Cs,O,S} 0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    H        0 {2,S}
6    H        0 {2,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (151000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (12.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 379,
    label = "Cd/H/OneDe_Cd/H2;C_methyl",
    group1 = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    H                0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    H                0 {2,S}
6    H                0 {2,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2430000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (10.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 380,
    label = "Cd/NonDe/OneDe_Cd/H2;C_methyl",
    group1 = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    {Cs,O,S}         0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    H                0 {2,S}
6    H                0 {2,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (592000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (11.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 381,
    label = "Ct/NonDe_Ct/H;C_methyl",
    group1 = 
"""
1 *1 Ct       0 {2,T} {3,S}
2 *2 Ct       0 {1,T} {4,S}
3    {Cs,O,S} 0 {1,S}
4    H        0 {2,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (19900000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (12.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 382,
    label = "Cd/H/OneDe_Cd/H2;C_methyl",
    group1 = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    H                0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    H                0 {2,S}
6    H                0 {2,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (124000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (11.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 383,
    label = "Cd/H/OneDe_Cd/H2;C_methyl",
    group1 = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    H                0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    H                0 {2,S}
6    H                0 {2,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1360000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (9.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 384,
    label = "Ct/OneDe_Ct/H;C_methyl",
    group1 = 
"""
1 *1 Ct               0 {2,T} {3,S}
2 *2 Ct               0 {1,T} {4,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    H                0 {2,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4490000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (11.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 385,
    label = "Ct/OneDe_Ct/H;C_methyl",
    group1 = 
"""
1 *1 Ct               0 {2,T} {3,S}
2 *2 Ct               0 {1,T} {4,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    H                0 {2,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (17100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (11.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 386,
    label = "Cd/NonDe/OneDe_Cd/H2;C_methyl",
    group1 = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    {Cs,O,S}         0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    H                0 {2,S}
6    H                0 {2,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (607000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 387,
    label = "Cd/H2_Cd/H2;H_rad",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (77400000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (2.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 388,
    label = "Cd/H2_Cd/H/NonDe;H_rad",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    H        0 {1,S}
4    H        0 {1,S}
5    H        0 {2,S}
6    {Cs,O,S} 0 {2,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (20100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (2.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 389,
    label = "Cd/H2_Cd/NonDe2;H_rad",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    H        0 {1,S}
4    H        0 {1,S}
5    {Cs,O,S} 0 {2,S}
6    {Cs,O,S} 0 {2,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (49400000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (1.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 390,
    label = "Cd/H2_Cd/H/OneDe;H_rad",
    group1 = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    H                0 {1,S}
4    H                0 {1,S}
5    H                0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (37100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 391,
    label = "Cd/H2_Cd/NonDe/OneDe;H_rad",
    group1 = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    H                0 {1,S}
4    H                0 {1,S}
5    {Cs,O,S}         0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (21300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 392,
    label = "Cd/H2_Cd/H/OneDe;H_rad",
    group1 = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    H                0 {1,S}
4    H                0 {1,S}
5    H                0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (1970000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (3.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 393,
    label = "Cd/H2_Cd/NonDe/OneDe;H_rad",
    group1 = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    H                0 {1,S}
4    H                0 {1,S}
5    {Cs,O,S}         0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (14300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (2.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 394,
    label = "Ct/H_Ct/H;H_rad",
    group1 = 
"""
1 *1 Ct 0 {2,T} {3,S}
2 *2 Ct 0 {1,T} {4,S}
3    H  0 {1,S}
4    H  0 {2,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (116000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (3.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 395,
    label = "Ct/H_Ct/NonDe;H_rad",
    group1 = 
"""
1 *1 Ct       0 {2,T} {3,S}
2 *2 Ct       0 {1,T} {4,S}
3    H        0 {1,S}
4    {Cs,O,S} 0 {2,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (112000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (3.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 396,
    label = "Cd/H2_Ca;H_rad",
    group1 = 
"""
1 *1 Cd  0 {2,D} {3,S} {4,S}
2 *2 Cdd 0 {1,D} {5,D}
3    H   0 {1,S}
4    H   0 {1,S}
5    C   0 {2,D}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (66800000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (2.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 397,
    label = "Cd/H2_Ca;H_rad",
    group1 = 
"""
1 *1 Cd  0 {2,D} {3,S} {4,S}
2 *2 Cdd 0 {1,D} {5,D}
3    H   0 {1,S}
4    H   0 {1,S}
5    C   0 {2,D}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (27300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (2.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 398,
    label = "Cd/H2_Cd/H/OneDe;H_rad",
    group1 = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    H                0 {1,S}
4    H                0 {1,S}
5    H                0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (18200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (1.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 399,
    label = "Cd/H2_Cd/NonDe/OneDe;H_rad",
    group1 = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    H                0 {1,S}
4    H                0 {1,S}
5    {Cs,O,S}         0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (20400000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 400,
    label = "Ct/H_Ct/OneDe;H_rad",
    group1 = 
"""
1 *1 Ct               0 {2,T} {3,S}
2 *2 Ct               0 {1,T} {4,S}
3    H                0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (18600000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (2.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 401,
    label = "Ct/H_Ct/OneDe;H_rad",
    group1 = 
"""
1 *1 Ct               0 {2,T} {3,S}
2 *2 Ct               0 {1,T} {4,S}
3    H                0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (16900000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (2.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 402,
    label = "Ct/H_Ct/OneDe;H_rad",
    group1 = 
"""
1 *1 Ct               0 {2,T} {3,S}
2 *2 Ct               0 {1,T} {4,S}
3    H                0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (107000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (2.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 403,
    label = "Ca_Cd/H/NonDe;H_rad",
    group1 = 
"""
1 *1 Cdd      0 {2,D} {3,D}
2 *2 Cd       0 {1,D} {4,S} {5,S}
3    C        0 {1,D}
4    H        0 {2,S}
5    {Cs,O,S} 0 {2,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (12800000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (3.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 404,
    label = "Ca_Cd/NonDe2;H_rad",
    group1 = 
"""
1 *1 Cdd      0 {2,D} {3,D}
2 *2 Cd       0 {1,D} {4,S} {5,S}
3    C        0 {1,D}
4    {Cs,O,S} 0 {2,S}
5    {Cs,O,S} 0 {2,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (25700000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (2.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 405,
    label = "Cd/H/NonDe_Cd/H2;H_rad",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    H        0 {2,S}
6    H        0 {2,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (11800000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (3.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 406,
    label = "Cd/NonDe2_Cd/H2;H_rad",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    {Cs,O,S} 0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    H        0 {2,S}
6    H        0 {2,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (11700000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (4.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 407,
    label = "Cd/H/OneDe_Cd/H2;H_rad",
    group1 = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    H                0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    H                0 {2,S}
6    H                0 {2,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (28500000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (4.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 408,
    label = "Cd/NonDe/OneDe_Cd/H2;H_rad",
    group1 = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    {Cs,O,S}         0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    H                0 {2,S}
6    H                0 {2,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (9300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (5.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 409,
    label = "Ct/NonDe_Ct/H;H_rad",
    group1 = 
"""
1 *1 Ct       0 {2,T} {3,S}
2 *2 Ct       0 {1,T} {4,S}
3    {Cs,O,S} 0 {1,S}
4    H        0 {2,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (57700000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (5.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 410,
    label = "Cd/H/OneDe_Cd/H2;H_rad",
    group1 = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    H                0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    H                0 {2,S}
6    H                0 {2,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (1670000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 411,
    label = "Cd/NonDe/OneDe_Cd/H2;H_rad",
    group1 = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    {Cs,O,S}         0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    H                0 {2,S}
6    H                0 {2,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (5620000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (6.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 412,
    label = "Cd/H/OneDe_Cd/H2;H_rad",
    group1 = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    H                0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    H                0 {2,S}
6    H                0 {2,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (13300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (4.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 413,
    label = "Cd/NonDe/OneDe_Cd/H2;H_rad",
    group1 = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    {Cs,O,S}         0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    H                0 {2,S}
6    H                0 {2,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (8200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (5.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 414,
    label = "Ct/OneDe_Ct/H;H_rad",
    group1 = 
"""
1 *1 Ct               0 {2,T} {3,S}
2 *2 Ct               0 {1,T} {4,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    H                0 {2,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (22500000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (5.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 415,
    label = "Ct/OneDe_Ct/H;H_rad",
    group1 = 
"""
1 *1 Ct               0 {2,T} {3,S}
2 *2 Ct               0 {1,T} {4,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    H                0 {2,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (99900000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 416,
    label = "Cd/H2_Cd/H2;Cd_pri_rad-Cdd/Cd",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    group2 = 
"""
1 *3 Cd  1 {2,D} {3,S}
2    Cdd 0 {1,D} {4,D}
3    H   0 {1,S}
4    Cd  0 {2,D}
""",
    kinetics = ArrheniusEP(
        A = (149.03, 'cm^3/(mol*s)'),
        n = 3.0074,
        alpha = 0,
        E0 = (10.1708, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1600, 'K'),
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
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 417,
    label = "CO/H/NonDe_O;O_rad/NonDeO",
    group1 = 
"""
1 *1 CO       0 {2,D} {3,S} {4,S}
2 *2 Od       0 {1,D}
3    H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.04245, 'cm^3/(mol*s)'),
        n = 3.486,
        alpha = 0,
        E0 = (22.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1600, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 418,
    label = "CO/NonDe2_O;O_rad/NonDeO",
    group1 = 
"""
1 *1 CO       0 {2,D} {3,S} {4,S}
2 *2 Od       0 {1,D}
3    {Cs,O,S} 0 {1,S}
4    {Cs,O,S} 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.04245, 'cm^3/(mol*s)'),
        n = 3.486,
        alpha = 0,
        E0 = (22.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1600, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 419,
    label = "CO/H2_O;O_rad/NonDeO",
    group1 = 
"""
1 *1 CO 0 {2,D} {3,S} {4,S}
2 *2 Od 0 {1,D}
3    H  0 {1,S}
4    H  0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.04245, 'cm^3/(mol*s)'),
        n = 3.486,
        alpha = 0,
        E0 = (22.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1600, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 420,
    label = "CO/NonDe2_O;O_rad/NonDeO",
    group1 = 
"""
1 *1 CO       0 {2,D} {3,S} {4,S}
2 *2 Od       0 {1,D}
3    {Cs,O,S} 0 {1,S}
4    {Cs,O,S} 0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.04245, 'cm^3/(mol*s)'),
        n = 3.486,
        alpha = 0,
        E0 = (22.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1600, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 421,
    label = "Cd/H2_Cd/H2;O_rad/NonDeO",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (35.6, 'cm^3/(mol*s)'),
        n = 3.22,
        alpha = 0,
        E0 = (11.1, 'kcal/mol'),
        Tmin = (400, 'K'),
        Tmax = (1100, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""pp, CBS-QB3 calculations, with hindered rotor treatment.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 422,
    label = "Cd/H2_Cd/H/NonDe;O_rad/NonDeO",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    H        0 {1,S}
4    H        0 {1,S}
5    H        0 {2,S}
6    {Cs,O,S} 0 {2,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (791, 'cm^3/(mol*s)'),
        n = 2.78,
        alpha = 0,
        E0 = (9.5, 'kcal/mol'),
        Tmin = (400, 'K'),
        Tmax = (1100, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""ps, CBS-QB3 calculations, with hindered rotor treatment.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 423,
    label = "Cd/H2_Cd/NonDe2;O_rad/NonDeO",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    H        0 {1,S}
4    H        0 {1,S}
5    {Cs,O,S} 0 {2,S}
6    {Cs,O,S} 0 {2,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1350, 'cm^3/(mol*s)'),
        n = 2.67,
        alpha = 0,
        E0 = (7.9, 'kcal/mol'),
        Tmin = (400, 'K'),
        Tmax = (1100, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""pt, CBS-QB3 calculations, with hindered rotor treatment.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 424,
    label = "Cd/H/NonDe_Cd/H2;O_rad/NonDeO",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    H        0 {2,S}
6    H        0 {2,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (10.6, 'cm^3/(mol*s)'),
        n = 3.29,
        alpha = 0,
        E0 = (9.1, 'kcal/mol'),
        Tmin = (400, 'K'),
        Tmax = (1100, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""sp, CBS-QB3 calculations, with hindered rotor treatment.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 425,
    label = "Cd/H/NonDe_Cd/H/NonDe;O_rad/NonDeO",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    H        0 {2,S}
6    {Cs,O,S} 0 {2,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (46.2, 'cm^3/(mol*s)'),
        n = 3.09,
        alpha = 0,
        E0 = (7.2, 'kcal/mol'),
        Tmin = (400, 'K'),
        Tmax = (1100, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""ss , CBS-QB3 calculations, with hindered rotor treatment.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 426,
    label = "Cd/H/NonDe_Cd/NonDe2;O_rad/NonDeO",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    {Cs,O,S} 0 {2,S}
6    {Cs,O,S} 0 {2,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (186, 'cm^3/(mol*s)'),
        n = 2.95,
        alpha = 0,
        E0 = (5.4, 'kcal/mol'),
        Tmin = (400, 'K'),
        Tmax = (1100, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""st, CBS-QB3 calculations, with hindered rotor treatment.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 427,
    label = "Cd/NonDe2_Cd/H2;O_rad/NonDeO",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    {Cs,O,S} 0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    H        0 {2,S}
6    H        0 {2,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.337, 'cm^3/(mol*s)'),
        n = 3.67,
        alpha = 0,
        E0 = (7.2, 'kcal/mol'),
        Tmin = (400, 'K'),
        Tmax = (1100, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""tp, CBS-QB3 calculations, with hindered rotor treatment.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 428,
    label = "Cd/NonDe2_Cd/H/NonDe;O_rad/NonDeO",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    {Cs,O,S} 0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    H        0 {2,S}
6    {Cs,O,S} 0 {2,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.172, 'cm^3/(mol*s)'),
        n = 3.7,
        alpha = 0,
        E0 = (4.7, 'kcal/mol'),
        Tmin = (400, 'K'),
        Tmax = (1100, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""ts, CBS-QB3 calculations, with hindered rotor treatment.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 429,
    label = "Cd/NonDe2_Cd/NonDe2;O_rad/NonDeO",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    {Cs,O,S} 0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    {Cs,O,S} 0 {2,S}
6    {Cs,O,S} 0 {2,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.69, 'cm^3/(mol*s)'),
        n = 3.44,
        alpha = 0,
        E0 = (2.7, 'kcal/mol'),
        Tmin = (400, 'K'),
        Tmax = (1100, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""tt, CBS-QB3 calculations, with hindered rotor treatment.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 421,
    label = "Cd/H2_Cd/H2;O_rad/NonDeO",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (35.6, 'cm^3/(mol*s)'),
        n = 3.22,
        alpha = 0,
        E0 = (11.1, 'kcal/mol'),
        Tmin = (400, 'K'),
        Tmax = (1100, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""pp, CBS-QB3 calculations, with hindered rotor treatment.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 422,
    label = "Cd/H2_Cd/H/NonDe;O_rad/NonDeO",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    H        0 {1,S}
4    H        0 {1,S}
5    H        0 {2,S}
6    {Cs,O,S} 0 {2,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (791, 'cm^3/(mol*s)'),
        n = 2.78,
        alpha = 0,
        E0 = (9.5, 'kcal/mol'),
        Tmin = (400, 'K'),
        Tmax = (1100, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""ps, CBS-QB3 calculations, with hindered rotor treatment.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 423,
    label = "Cd/H2_Cd/NonDe2;O_rad/NonDeO",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    H        0 {1,S}
4    H        0 {1,S}
5    {Cs,O,S} 0 {2,S}
6    {Cs,O,S} 0 {2,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1350, 'cm^3/(mol*s)'),
        n = 2.67,
        alpha = 0,
        E0 = (7.9, 'kcal/mol'),
        Tmin = (400, 'K'),
        Tmax = (1100, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""pt, CBS-QB3 calculations, with hindered rotor treatment.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 424,
    label = "Cd/H/NonDe_Cd/H2;O_rad/NonDeO",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    H        0 {2,S}
6    H        0 {2,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (10.6, 'cm^3/(mol*s)'),
        n = 3.29,
        alpha = 0,
        E0 = (9.1, 'kcal/mol'),
        Tmin = (400, 'K'),
        Tmax = (1100, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""sp, CBS-QB3 calculations, with hindered rotor treatment.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 425,
    label = "Cd/H/NonDe_Cd/H/NonDe;O_rad/NonDeO",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    H        0 {2,S}
6    {Cs,O,S} 0 {2,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (46.2, 'cm^3/(mol*s)'),
        n = 3.09,
        alpha = 0,
        E0 = (7.2, 'kcal/mol'),
        Tmin = (400, 'K'),
        Tmax = (1100, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""ss , CBS-QB3 calculations, with hindered rotor treatment.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 426,
    label = "Cd/H/NonDe_Cd/NonDe2;O_rad/NonDeO",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    {Cs,O,S} 0 {2,S}
6    {Cs,O,S} 0 {2,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (186, 'cm^3/(mol*s)'),
        n = 2.95,
        alpha = 0,
        E0 = (5.4, 'kcal/mol'),
        Tmin = (400, 'K'),
        Tmax = (1100, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""st, CBS-QB3 calculations, with hindered rotor treatment.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 427,
    label = "Cd/NonDe2_Cd/H2;O_rad/NonDeO",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    {Cs,O,S} 0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    H        0 {2,S}
6    H        0 {2,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.337, 'cm^3/(mol*s)'),
        n = 3.67,
        alpha = 0,
        E0 = (7.2, 'kcal/mol'),
        Tmin = (400, 'K'),
        Tmax = (1100, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""tp, CBS-QB3 calculations, with hindered rotor treatment.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 428,
    label = "Cd/NonDe2_Cd/H/NonDe;O_rad/NonDeO",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    {Cs,O,S} 0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    H        0 {2,S}
6    {Cs,O,S} 0 {2,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.172, 'cm^3/(mol*s)'),
        n = 3.7,
        alpha = 0,
        E0 = (4.7, 'kcal/mol'),
        Tmin = (400, 'K'),
        Tmax = (1100, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""ts, CBS-QB3 calculations, with hindered rotor treatment.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 429,
    label = "Cd/NonDe2_Cd/NonDe2;O_rad/NonDeO",
    group1 = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    {Cs,O,S} 0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    {Cs,O,S} 0 {2,S}
6    {Cs,O,S} 0 {2,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.69, 'cm^3/(mol*s)'),
        n = 3.44,
        alpha = 0,
        E0 = (2.7, 'kcal/mol'),
        Tmin = (400, 'K'),
        Tmax = (1100, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""tt, CBS-QB3 calculations, with hindered rotor treatment.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2498,
    label = "CS/H2_S;H_rad",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Sd 0 {1,D}
3    H  0 {1,S}
4    H  0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (462000000.0, 'cm^3/(mol*s)'),
        n = 1.7,
        alpha = 0,
        E0 = (0.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2499,
    label = "CS/H2_S;C_methyl",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Sd 0 {1,D}
3    H  0 {1,S}
4    H  0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (11500, 'cm^3/(mol*s)'),
        n = 2.8,
        alpha = 0,
        E0 = (-0.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2500,
    label = "CS/H2_S;C_rad/H2/Cs",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Sd 0 {1,D}
3    H  0 {1,S}
4    H  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (557, 'cm^3/(mol*s)'),
        n = 2.9,
        alpha = 0,
        E0 = (-2.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2501,
    label = "CS/H2_S;C_rad/H/NonDeC",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Sd 0 {1,D}
3    H  0 {1,S}
4    H  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (178, 'cm^3/(mol*s)'),
        n = 2.9,
        alpha = 0,
        E0 = (-4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2502,
    label = "CS/H2_S;C_rad/Cs3",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Sd 0 {1,D}
3    H  0 {1,S}
4    H  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (120, 'cm^3/(mol*s)'),
        n = 3,
        alpha = 0,
        E0 = (-5.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2511,
    label = "CS/H2_S;S_pri_rad",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Sd 0 {1,D}
3    H  0 {1,S}
4    H  0 {1,S}
""",
    group2 = 
"""
1 *3 Ss 1 {2,S}
2    H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (29200, 'cm^3/(mol*s)'),
        n = 2.5,
        alpha = 0,
        E0 = (-1.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2512,
    label = "CS/H2_S;S_rad/NonDeC",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Sd 0 {1,D}
3    H  0 {1,S}
4    H  0 {1,S}
""",
    group2 = 
"""
1 *3 Ss 1 {2,S}
2    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (858, 'cm^3/(mol*s)'),
        n = 2.9,
        alpha = 0,
        E0 = (-0.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2516,
    label = "CS/H2_S;S_rad/NonDeS",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Sd 0 {1,D}
3    H  0 {1,S}
4    H  0 {1,S}
""",
    group2 = 
"""
1 *3 Ss 1 {2,S}
2    Ss 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (31.9, 'cm^3/(mol*s)'),
        n = 3,
        alpha = 0,
        E0 = (3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2517,
    label = "CS/H/OneDe_S;C_methyl",
    group1 = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Sd               0 {1,D}
3    H                0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1, 'cm^3/(mol*s)'),
        n = 2.8,
        alpha = 0,
        E0 = (1.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2518,
    label = "CS/TwoDe_S;C_methyl",
    group1 = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Sd               0 {1,D}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1, 'cm^3/(mol*s)'),
        n = 2.7,
        alpha = 0,
        E0 = (2.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2519,
    label = "CS/H/Os_S;H_rad",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Sd 0 {1,D}
3    H  0 {1,S}
4    O  0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (645000000.0, 'cm^3/(mol*s)'),
        n = 1.4,
        alpha = 0,
        E0 = (2.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""CAC CBS-QB3 1DHR""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2520,
    label = "CS/H/Os_S;C_methyl",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Sd 0 {1,D}
3    H  0 {1,S}
4    O  0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (172000, 'cm^3/(mol*s)'),
        n = 1.68,
        alpha = 0,
        E0 = (5.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""CAC CBS-QB3 1DHR""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2521,
    label = "Sd_Cds/H2;H_rad",
    group1 = 
"""
1 *1 Sd 0 {2,D}
2 *2 Cd 0 {1,D} {3,S} {4,S}
3    H  0 {2,S}
4    H  0 {2,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (950000000.0, 'cm^3/(mol*s)'),
        n = 1.7,
        alpha = 0,
        E0 = (-0.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2522,
    label = "Sd_Cds/H2;C_methyl",
    group1 = 
"""
1 *1 Sd 0 {2,D}
2 *2 Cd 0 {1,D} {3,S} {4,S}
3    H  0 {2,S}
4    H  0 {2,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3760, 'cm^3/(mol*s)'),
        n = 2.9,
        alpha = 0,
        E0 = (1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2523,
    label = "Sd_Cds/H2;C_rad/H2/Cs",
    group1 = 
"""
1 *1 Sd 0 {2,D}
2 *2 Cd 0 {1,D} {3,S} {4,S}
3    H  0 {2,S}
4    H  0 {2,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (169, 'cm^3/(mol*s)'),
        n = 3,
        alpha = 0,
        E0 = (-1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2524,
    label = "Sd_Cds/H2;C_rad/H/NonDeC",
    group1 = 
"""
1 *1 Sd 0 {2,D}
2 *2 Cd 0 {1,D} {3,S} {4,S}
3    H  0 {2,S}
4    H  0 {2,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (64.4, 'cm^3/(mol*s)'),
        n = 3,
        alpha = 0,
        E0 = (-2.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2525,
    label = "Sd_Cds/H2;C_rad/Cs3",
    group1 = 
"""
1 *1 Sd 0 {2,D}
2 *2 Cd 0 {1,D} {3,S} {4,S}
3    H  0 {2,S}
4    H  0 {2,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (36.2, 'cm^3/(mol*s)'),
        n = 3.1,
        alpha = 0,
        E0 = (-3.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2526,
    label = "Sd_Cds/H/NonDe;C_rad/H2/Cs",
    group1 = 
"""
1 *1 Sd       0 {2,D}
2 *2 Cd       0 {1,D} {3,S} {4,S}
3    {Cs,O,S} 0 {2,S}
4    H        0 {2,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (169, 'cm^3/(mol*s)'),
        n = 3,
        alpha = 0,
        E0 = (-1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""based on 2523""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2534,
    label = "Sd_Cds/H2;S_pri_rad",
    group1 = 
"""
1 *1 Sd 0 {2,D}
2 *2 Cd 0 {1,D} {3,S} {4,S}
3    H  0 {2,S}
4    H  0 {2,S}
""",
    group2 = 
"""
1 *3 Ss 1 {2,S}
2    H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (14400, 'cm^3/(mol*s)'),
        n = 2.6,
        alpha = 0,
        E0 = (-6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2535,
    label = "Sd_Cds/H2;S_rad/NonDeC",
    group1 = 
"""
1 *1 Sd 0 {2,D}
2 *2 Cd 0 {1,D} {3,S} {4,S}
3    H  0 {2,S}
4    H  0 {2,S}
""",
    group2 = 
"""
1 *3 Ss 1 {2,S}
2    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (382, 'cm^3/(mol*s)'),
        n = 3,
        alpha = 0,
        E0 = (-3.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2539,
    label = "Sd_Cds/H2;S_rad/NonDeS",
    group1 = 
"""
1 *1 Sd 0 {2,D}
2 *2 Cd 0 {1,D} {3,S} {4,S}
3    H  0 {2,S}
4    H  0 {2,S}
""",
    group2 = 
"""
1 *3 Ss 1 {2,S}
2    Ss 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (13.4, 'cm^3/(mol*s)'),
        n = 3.3,
        alpha = 0,
        E0 = (1.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2540,
    label = "Sd_Cds/H/NonDe;C_methyl",
    group1 = 
"""
1 *1 Sd       0 {2,D}
2 *2 Cd       0 {1,D} {3,S} {4,S}
3    {Cs,O,S} 0 {2,S}
4    H        0 {2,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5360, 'cm^3/(mol*s)'),
        n = 2.8,
        alpha = 0,
        E0 = (1.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2541,
    label = "Sd_Cds/NonDe2;C_methyl",
    group1 = 
"""
1 *1 Sd       0 {2,D}
2 *2 Cd       0 {1,D} {3,S} {4,S}
3    {Cs,O,S} 0 {2,S}
4    {Cs,O,S} 0 {2,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5290, 'cm^3/(mol*s)'),
        n = 2.7,
        alpha = 0,
        E0 = (2.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2542,
    label = "Sd_Cds/H/Cd;C_methyl",
    group1 = 
"""
1 *1 Sd 0 {2,D}
2 *2 Cd 0 {1,D} {3,S} {4,S}
3    Cd 0 {2,S} {5,D}
4    H  0 {2,S}
5    C  0 {3,D}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1650, 'cm^3/(mol*s)'),
        n = 3.2,
        alpha = 0,
        E0 = (1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2543,
    label = "Sd_Cds/NonDe/Cd;C_methyl",
    group1 = 
"""
1 *1 Sd       0 {2,D}
2 *2 Cd       0 {1,D} {3,S} {4,S}
3    Cd       0 {2,S} {5,D}
4    {Cs,O,S} 0 {2,S}
5    C        0 {3,D}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1680, 'cm^3/(mol*s)'),
        n = 3.1,
        alpha = 0,
        E0 = (1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2544,
    label = "Cd/H2_Cd/H2;S_pri_rad",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    group2 = 
"""
1 *3 Ss 1 {2,S}
2    H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4980, 'cm^3/(mol*s)'),
        n = 2.7,
        alpha = 0,
        E0 = (-0.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2545,
    label = "Cd/H2_Cd/H2;S_rad/NonDeC",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    group2 = 
"""
1 *3 Ss 1 {2,S}
2    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (73.9, 'cm^3/(mol*s)'),
        n = 3.1,
        alpha = 0,
        E0 = (1.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2549,
    label = "Cd/H2_Cd/H2;S_rad/NonDeS",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    group2 = 
"""
1 *3 Ss 1 {2,S}
2    Ss 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.21, 'cm^3/(mol*s)'),
        n = 3.3,
        alpha = 0,
        E0 = (7.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""Aäron Vandeputte GAVs""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2601,
    label = "CS/H/Cs_S;H_rad",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Sd 0 {1,D}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (1700000000.0, 'cm^3/(mol*s)'),
        n = 1.36,
        alpha = 0,
        E0 = (1.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""CAC calc CBS-QB3 1dhr""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2602,
    label = "CS/H/Cs_S;C_rad/H/CsS",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Sd 0 {1,D}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.52, 'cm^3/(mol*s)'),
        n = 3.09,
        alpha = 0,
        E0 = (-1.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""CAC calc CBS-QB3 1dhr""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2603,
    label = "CS/H/Os_S;H_rad",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Sd 0 {1,D}
3    H  0 {1,S}
4    O  0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (645000000.0, 'cm^3/(mol*s)'),
        n = 1.4,
        alpha = 0,
        E0 = (2.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""CAC calc CBS-QB3 1dhr""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2604,
    label = "CS/H/Os_S;C_methyl",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Sd 0 {1,D}
3    H  0 {1,S}
4    O  0 {1,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (172000, 'cm^3/(mol*s)'),
        n = 1.68,
        alpha = 0,
        E0 = (5.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""CAC calc CBS-QB3 1dhr""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2605,
    label = "CS/H/Os_S;C_rad/H2/Cs",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Sd 0 {1,D}
3    H  0 {1,S}
4    O  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (774, 'cm^3/(mol*s)'),
        n = 2.56,
        alpha = 0,
        E0 = (3.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""CAC calc CBS-QB3 1dhr""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2606,
    label = "Sd_Cds/H/NonDe;Cs_rad",
    group1 = 
"""
1 *1 Sd       0 {2,D}
2 *2 Cd       0 {1,D} {3,S} {4,S}
3    {Cs,O,S} 0 {2,S}
4    H        0 {2,S}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    R 0 {1,S}
3    R 0 {1,S}
4    R 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3910000.0, 'cm^3/(mol*s)'),
        n = 1.66,
        alpha = 0,
        E0 = (-0.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""CAC calc CBS-QB3 1dhr""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2607,
    label = "CS_O;H_rad",
    group1 = 
"""
1 *1 Cdd 0 {2,D} {3,D}
2 *2 Sd  0 {1,D}
3    Od  0 {1,D}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (567000000.0, 'cm^3/(mol*s)'),
        n = 1.75,
        alpha = 0,
        E0 = (8.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""CAC calc CBS-QB3 1dhr""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2608,
    label = "CS_O;Cs_rad",
    group1 = 
"""
1 *1 Cdd 0 {2,D} {3,D}
2 *2 Sd  0 {1,D}
3    Od  0 {1,D}
""",
    group2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    R 0 {1,S}
3    R 0 {1,S}
4    R 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (603000, 'cm^3/(mol*s)'),
        n = 1.83,
        alpha = 0,
        E0 = (11.84, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""CAC calc CBS-QB3 1dhr""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2609,
    label = "CS/H/Cs_S;C_rad/H2/Cs",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Sd 0 {1,D}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1800, 'cm^3/(mol*s)'),
        n = 2.47,
        alpha = 0,
        E0 = (0.61, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""CAC calc CBS-QB3 1dhr""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2610,
    label = "CS/H/Cs_S;C_rad/H/NonDeC",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Sd 0 {1,D}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (17.9, 'cm^3/(mol*s)'),
        n = 2.9,
        alpha = 0,
        E0 = (-1.43, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""CAC calc CBS-QB3 1dhr""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2611,
    label = "CS/H/Cs_S;S_pri_rad",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Sd 0 {1,D}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 Ss 1 {2,S}
2    H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (11800000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (-1.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (700, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""AA calcs""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2612,
    label = "CS/H/Cs_S;S_pri_rad",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Sd 0 {1,D}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    group2 = 
"""
1 *3 Ss 1 {2,S}
2    H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (246000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (2.93, 'kcal/mol'),
        Tmin = (701, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""AA calcs""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2613,
    label = "CS/H/Ss_S;C_rad/H/NonDeC",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Sd 0 {1,D}
3    H  0 {1,S}
4    S  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (195000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (4.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""AA calcs""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2614,
    label = "CS/CsSs_S;H_rad",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Sd 0 {1,D}
3    Cs 0 {1,S}
4    S  0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (16200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (4.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""AA calcs""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2615,
    label = "CS2;H_rad",
    group1 = 
"""
1 *1 Cdd 0 {2,D} {3,D}
2 *2 Sd  0 {1,D}
3    Sd  0 {1,D}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (387000000.0, 'cm^3/(mol*s)'),
        n = 1.89,
        alpha = 0,
        E0 = (7.72, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""CAC calc CBS-QB3 1dhr""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2616,
    label = "CS2;C_rad/H2/Cs",
    group1 = 
"""
1 *1 Cdd 0 {2,D} {3,D}
2 *2 Sd  0 {1,D}
3    Sd  0 {1,D}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (359, 'cm^3/(mol*s)'),
        n = 2.94,
        alpha = 0,
        E0 = (8.96, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""CAC calc CBS-QB3 1dhr""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2617,
    label = "Sd_Cds/CsO;H_rad",
    group1 = 
"""
1 *1 Sd 0 {2,D}
2 *2 Cd 0 {1,D} {3,S} {4,S}
3    Cs 0 {2,S}
4    O  0 {2,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (554000000.0, 'cm^3/(mol*s)'),
        n = 1.24,
        alpha = 0,
        E0 = (-0.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""CAC calc CBS-QB3 1dhr""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2618,
    label = "Cd/H/Os_Cd/H/Cs;S_pri_rad",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    O  0 {1,S}
5    H  0 {2,S}
6    Cs 0 {2,S}
""",
    group2 = 
"""
1 *3 Ss 1 {2,S}
2    H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (21000, 'cm^3/(mol*s)'),
        n = 2.39,
        alpha = 0,
        E0 = (-5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""CAC calc CBS-QB3 1dhr""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 3000,
    label = "CS/H/Os_S;C_rad/H2/Cs",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Sd 0 {1,D}
3    H  0 {1,S}
4    O  0 {1,S}
""",
    group2 = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (774, 'cm^3/(mol*s)'),
        n = 2.56,
        alpha = 0,
        E0 = (3.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""CAC CBS-QB3 1dHR""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 3001,
    label = "CS_O;H_rad",
    group1 = 
"""
1 *1 Cdd 0 {2,D} {3,D}
2 *2 Sd  0 {1,D}
3    Od  0 {1,D}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (567000000.0, 'cm^3/(mol*s)'),
        n = 1.75,
        alpha = 0,
        E0 = (8.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""CAC CBS-QB3""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 3002,
    label = "N3t_N3t-CH2_triplet",
    group1 = 
"""
1 *1 N3t 0 {2,T}
2 *2 N3t 0 {1,T}
""",
    group2 = 
"""
1 *3 C 2T {2,S} {3,S}
2    H 0  {1,S}
3    H 0  {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.6e+32, 'cm^3/(mol*s)'),
        n = -7.07,
        alpha = 0,
        E0 = (19.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 1,
    shortDesc = u"Added by Beat Buesser",
    longDesc = 
u"""
Added by Beat Buesser, value for reaction: CH2 + N2 = CH2NN (B&D #22a) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",
""",
    history = [
        (""),
    ],
)

entry(
    index = 3003,
    label = "N3t_N3t-CH_quartet",
    group1 = 
"""
1 *1 N3t 0 {2,T}
2 *2 N3t 0 {1,T}
""",
    group2 = 
"""
1 *3 Cs 3 {2,S}
2    H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.6e+28, 'cm^3/(mol*s)'),
        n = -5.84,
        alpha = 0,
        E0 = (2.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 1,
    shortDesc = u"Added by Beat Buesser",
    longDesc = 
u"""
Added by Beat Buesser, value for reaction: CH + N2 = HCNN (B&D #24a) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",
""",
    history = [
        (""),
    ],
)

entry(
    index = 3004,
    label = "N3d/H_N3d/H-H_rad",
    group1 = 
"""
1 *1 N3d 0 {2,D} {3,S}
2 *2 N3d 0 {1,D} {4,S}
3    H   0 {1,S}
4    H   0 {2,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (9.91e+34, 'cm^3/(mol*s)'),
        n = -7.67,
        alpha = 0,
        E0 = (12.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 1,
    shortDesc = u"Added by Beat Buesser",
    longDesc = 
u"""
Added by Beat Buesser, value for reaction: N2H2 + H = N2H3 (B&D #31a) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",
""",
    history = [
        (""),
    ],
)

entry(
    index = 3005,
    label = "Ct/H_N3t-O_pri_rad",
    group1 = 
"""
1 *1 Ct  0 {2,T} {3,S}
2 *2 N3t 0 {1,T}
3    H   0 {1,S}
""",
    group2 = 
"""
1 *3 O 1 {2,S}
2    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.8e+30, 'cm^3/(mol*s)'),
        n = -6.37,
        alpha = 0,
        E0 = (5.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 1,
    shortDesc = u"Added by Beat Buesser",
    longDesc = 
u"""
Added by Beat Buesser, value for reaction: HCN + OH = NCHOH (B&D #42b4) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",
""",
    history = [
        (""),
    ],
)

entry(
    index = 3006,
    label = "Ct/H_N3t-H_rad",
    group1 = 
"""
1 *1 Ct  0 {2,T} {3,S}
2 *2 N3t 0 {1,T}
3    H   0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (7.24e+29, 'cm^3/(mol*s)'),
        n = -6.87,
        alpha = 0,
        E0 = (7.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 1,
    shortDesc = u"Added by Beat Buesser",
    longDesc = 
u"""
Added by Beat Buesser, value for reaction: HCN + H = H2CN (B&D #45a) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",
""",
    history = [
        (""),
    ],
)

entry(
    index = 3007,
    label = "N3t_Ct/H-H_rad",
    group1 = 
"""
1 *1 N3t 0 {2,T}
2 *2 Ct  0 {1,T} {3,S}
3    H   0 {2,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (7.24e+29, 'cm^3/(mol*s)'),
        n = -6.87,
        alpha = 0,
        E0 = (7.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 1,
    shortDesc = u"Added by Beat Buesser",
    longDesc = 
u"""
Added by Beat Buesser, value for reaction: HCN + H = HCNH (B&D #46) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",
""",
    history = [
        (""),
    ],
)

entry(
    index = 3008,
    label = "Cds/H2_N3d-H_rad",
    group1 = 
"""
1 *1 Cd  0 {2,D} {3,S} {4,S}
2 *2 N3d 0 {1,D}
3    H   0 {1,S}
4    H   0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (7.32e+29, 'cm^3/(mol*s)'),
        n = -6.51,
        alpha = 0,
        E0 = (8.31, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 1,
    shortDesc = u"Added by Beat Buesser",
    longDesc = 
u"""
Added by Beat Buesser, value for reaction: H2CNH + H = CH3NH (B&D #49a) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",
""",
    history = [
        (""),
    ],
)

entry(
    index = 3009,
    label = "N3d/H_Cds/H2-H_rad",
    group1 = 
"""
1 *1 N3d 0 {2,D} {5,S}
2 *2 Cd  0 {1,D} {3,S} {4,S}
3    H   0 {2,S}
4    H   0 {2,S}
5    H   0 {1,S}
""",
    group2 = 
"""
1 *3 H 1
""",
    kinetics = ArrheniusEP(
        A = (9.86e+36, 'cm^3/(mol*s)'),
        n = -8.41,
        alpha = 0,
        E0 = (12.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 1,
    shortDesc = u"Added by Beat Buesser",
    longDesc = 
u"""
Added by Beat Buesser, value for reaction: H2CNH + H = CH2NH2 (B&D #50) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",
""",
    history = [
        (""),
    ],
)

entry(
    index = 3010,
    label = "N3t_Ct/H-O_atom_triplet",
    group1 = 
"""
1 *1 N3t 0 {2,T}
2 *2 Ct  0 {1,T} {3,S}
3    H   0 {2,S}
""",
    group2 = 
"""
1 *3 O 2T
""",
    kinetics = ArrheniusEP(
        A = (9.99e+25, 'cm^3/(mol*s)'),
        n = -5.73,
        alpha = 0,
        E0 = (11.80, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 1,
    shortDesc = u"Added by Beat Buesser",
    longDesc = 
u"""
Added by Beat Buesser, value for reaction: HCN + O = HCNO (B&D #54) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",
""",
    history = [
        (""),
    ],
)

