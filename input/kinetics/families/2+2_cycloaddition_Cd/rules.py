#!/usr/bin/env python
# encoding: utf-8

name = "2+2_cycloaddition_Cd/rules"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 586,
    label = "db;doublebond",
    group1 = "OR{db_2H, db_HNd, db_HDe, db_Nd2, db_NdDe, db_De2}",
    group2 = "OR{mb_db, mb_CO, mb_OC, mb_CCO, mb_COC}",
    kinetics = ArrheniusEP(
        A = (6.92e+10,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (43.72,"kcal/mol"),
        Tmin = (723,"K"),
        Tmax = (786,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Quick et al. [107]""",
    longDesc = 
u"""
[107] Quick, L. M. *Int. J. Chem. Kinet.* 1972, 4, 61. 

C2H4 + C2H4 --> cyclobutane, absolute value measured directly using thermal excitation technique 
and mass spectrometry. Pressure  0.40 - 1.73 bar.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 6000,
    label = "db_2H;mb_OC",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    group2 = 
"""
1  *3 Od 0 {2,D}
2  *4 CO 0 {1,D}
""",
    kinetics = ArrheniusEP(
        A = (2.33e+06,"cm^3/(mol*s)","*|/",5),
        n = 1.65,
        alpha = 0,
        E0 = (54.15,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 0,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

