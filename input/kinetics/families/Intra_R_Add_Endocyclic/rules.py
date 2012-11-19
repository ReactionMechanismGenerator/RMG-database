#!/usr/bin/env python
# encoding: utf-8

name = "Intra_R_Add_Endocyclic/rules"
shortDesc = u""
longDesc = u"""

"""
recommended = True

entry(
    index = 809,
    label = "Rn;multiplebond_intra;radadd_intra",
    group1 = "OR{R3, R4, R5, R6}",
    group2 = 
"""
1 *2 {Cd,Ct,CO}    0 {2,{D,T}}
2 *3 {Cd,Ct,Od,Sd} 0 {1,{D,T}}
""",
    group3 = 
"""
1 *1 R!H 1
""",
    kinetics = ArrheniusEP(
        A = (100000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 0,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 810,
    label = "R5_SS_D;doublebond_intra_pri_2H;radadd_intra_cs2H",
    group1 = 
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3 *5 R!H 0 {2,S} {4,S}
4 *2 Cd  0 {3,S} {5,D}
5 *3 Cd  0 {4,D}
""",
    group2 = 
"""
1 *2 Cd 0 {2,D} {3,S}
2 *3 Cd 0 {1,D} {4,S} {5,S}
3    H  0 {1,S}
4    H  0 {2,S}
5    H  0 {2,S}
""",
    group3 = 
"""
1 *1 Cs 1 {2,S} {3,S}
2    H  0 {1,S}
3    H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (122000000.0, 's^-1'),
        n = 1.05,
        alpha = 0,
        E0 = (15.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 811,
    label = "R6_SSS_D;doublebond_intra_pri_2H;radadd_intra_cs2H",
    group1 = 
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3    R!H 0 {2,S} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 Cd  0 {4,S} {6,D}
6 *3 Cd  0 {5,D}
""",
    group2 = 
"""
1 *2 Cd 0 {2,D} {3,S}
2 *3 Cd 0 {1,D} {4,S} {5,S}
3    H  0 {1,S}
4    H  0 {2,S}
5    H  0 {2,S}
""",
    group3 = 
"""
1 *1 Cs 1 {2,S} {3,S}
2    H  0 {1,S}
3    H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (100000000.0, 's^-1'),
        n = 0.855,
        alpha = 0,
        E0 = (5.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 812,
    label = "R5_SD_D;doublebond_intra_pri_2H;radadd_intra_cs2H",
    group1 = 
"""
1 *1 R!H 1 {2,S}
2 *4 Cd  0 {1,S} {3,D}
3 *5 Cd  0 {2,D} {4,S}
4 *2 Cd  0 {3,S} {5,D}
5 *3 Cd  0 {4,D}
""",
    group2 = 
"""
1 *2 Cd 0 {2,D} {3,S}
2 *3 Cd 0 {1,D} {4,S} {5,S}
3    H  0 {1,S}
4    H  0 {2,S}
5    H  0 {2,S}
""",
    group3 = 
"""
1 *1 Cs 1 {2,S} {3,S}
2    H  0 {1,S}
3    H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (10500000.0, 's^-1'),
        n = 1.192,
        alpha = 0,
        E0 = (34.9116, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1600, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 813,
    label = "R3_D;doublebond_intra_pri_HDe;radadd_intra_cs2H",
    group1 = 
"""
1 *1 R!H 1 {2,S}
2 *2 Cd  0 {1,S} {3,D}
3 *3 Cd  0 {2,D}
""",
    group2 = 
"""
1 *2 Cd            0 {2,D} {3,S}
2 *3 Cd            0 {1,D} {4,S} {5,S}
3    H             0 {1,S}
4    H             0 {2,S}
5    {Cd,Ct,Cb,CO} 0 {2,S}
""",
    group3 = 
"""
1 *1 Cs 1 {2,S} {3,S}
2    H  0 {1,S}
3    H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (105000000.0, 's^-1'),
        n = 1.192,
        alpha = 0,
        E0 = (54, 'kcal/mol'),
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
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 814,
    label = "R3_T;triplebond_intra_H;radadd_intra_cs2H",
    group1 = 
"""
1 *1 R!H 1 {2,S}
2 *2 Ct  0 {1,S} {3,T}
3 *3 Ct  0 {2,T}
""",
    group2 = 
"""
1 *2 Ct 0 {2,T}
2 *3 Ct 0 {1,T} {3,S}
3    H  0 {2,S}
""",
    group3 = 
"""
1 *1 Cs 1 {2,S} {3,S}
2    H  0 {1,S}
3    H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (105000000.0, 's^-1'),
        n = 1.192,
        alpha = 0,
        E0 = (54, 'kcal/mol'),
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
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 816,
    label = "R5_DS_allenic_D;doublebond_intra_secDe_2H;radadd_intra_cdsingleH",
    group1 = 
"""
1 *1 Cd  1 {2,D}
2 *4 Cd  0 {1,D} {3,S}
3 *5 R!H 0 {2,S} {4,D}
4 *2 Cd  0 {3,D} {5,D}
5 *3 Cd  0 {4,D}
""",
    group2 = 
"""
1 *2 Cd            0 {2,D} {3,S}
2 *3 Cd            0 {1,D} {4,S} {5,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    H             0 {2,S}
5    H             0 {2,S}
""",
    group3 = 
"""
1 *1 Cd 1 {2,S}
2    H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (282000000000.0, 's^-1'),
        n = 0.12,
        alpha = 0,
        E0 = (14.82, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (3000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""RRHO, CBS-QB3 treatment of H2C=C=CH-CH=CH. cyclization by gmagoon""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

