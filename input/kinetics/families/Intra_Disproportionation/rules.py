#!/usr/bin/env python
# encoding: utf-8

name = "Intra_Disproportionation/rules"
shortDesc = u""
longDesc = u"""

"""
recommended = True

entry(
    index = 1,
    label = "R3;Y_rad;XH_Rrad",
    group1 = "OR{R3radEndo, R3radExo}",
    group2 = 
"""
1 *1 R!H 1
""",
    group3 = 
"""
1 *3 R!H 1 {2,S}
2 *2 R!H 0 {1,S} {3,S}
3 *4 H   0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (162000000000.0, 's^-1'),
        n = -0.305,
        alpha = 0,
        E0 = (2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Herbinet et al.(2006) reference Ea and Warth et al.(1998) prefactor with deltan_int=-1""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Feb 10 21:39:02 2014","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> added this entry by importing the old RMG database."""),
    ],
)

entry(
    index = 2,
    label = "R4;Y_rad;XH_Rrad",
    group1 = "OR{R4radEndo, R4radExo}",
    group2 = 
"""
1 *1 R!H 1
""",
    group3 = 
"""
1 *3 R!H 1 {2,S}
2 *2 R!H 0 {1,S} {3,S}
3 *4 H   0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (776000000.0, 's^-1'),
        n = 0.311,
        alpha = 0,
        E0 = (2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Herbinet et al.(2006) reference Ea and Warth et al.(1998) prefactor with deltan_int=-1""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Feb 10 21:39:02 2014","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> added this entry by importing the old RMG database."""),
    ],
)

entry(
    index = 3,
    label = "R5;Y_rad;XH_Rrad",
    group1 = "OR{R5radEndo, R5radExo}",
    group2 = 
"""
1 *1 R!H 1
""",
    group3 = 
"""
1 *3 R!H 1 {2,S}
2 *2 R!H 0 {1,S} {3,S}
3 *4 H   0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (3210000000.0, 's^-1'),
        n = 0.137,
        alpha = 0,
        E0 = (2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Herbinet et al.(2006) reference Ea and Warth et al.(1998) prefactor with deltan_int=-1""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Feb 10 21:39:02 2014","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> added this entry by importing the old RMG database."""),
    ],
)

entry(
    index = 4,
    label = "R6;Y_rad;XH_Rrad",
    group1 = "OR{R6radEndo, R6radExo}",
    group2 = 
"""
1 *1 R!H 1
""",
    group3 = 
"""
1 *3 R!H 1 {2,S}
2 *2 R!H 0 {1,S} {3,S}
3 *4 H   0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (3210000000.0, 's^-1'),
        n = 0.137,
        alpha = 0,
        E0 = (2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Herbinet et al.(2006) reference Ea and Warth et al.(1998) prefactor with deltan_int=-1""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Feb 10 21:39:02 2014","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> added this entry by importing the old RMG database."""),
    ],
)

entry(
    index = 5,
    label = "R7;Y_rad;XH_Rrad",
    group1 = "OR{R7radEndo, R7radExo}",
    group2 = 
"""
1 *1 R!H 1
""",
    group3 = 
"""
1 *3 R!H 1 {2,S}
2 *2 R!H 0 {1,S} {3,S}
3 *4 H   0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (3210000000.0, 's^-1'),
        n = 0.137,
        alpha = 0,
        E0 = (2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Herbinet et al.(2006) reference Ea and Warth et al.(1998) prefactor with deltan_int=-1""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Feb 10 21:39:02 2014","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> added this entry by importing the old RMG database."""),
    ],
)

