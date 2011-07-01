#!/usr/bin/env python
# encoding: utf-8

name = "Intra_Disproportionation/rules"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 1,
    label = "Y_biCyc3;Y_rad;XH_Rrad",
    group1 = 
"""
1  *1 R!H 1 {2,{S,D,B}}
2  *2 R!H 0 {1,{S,D,B}} {3,{S,D}} {4,S}
3  *3 R!H 1 {2,{S,D}}
4  *4 H 0 {2,S}
""",
    group2 = 
"""
1  *1 R!H 1
""",
    group3 = 
"""
1  *2 R!H 0 {2,{S,D}} {3,S}
2  *3 R!H 1 {1,{S,D}}
3  *4 H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.66e+10,"s^-1"),
        n = 1,
        alpha = 0,
        E0 = (9.5,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Herbinet et al.(2006) reference Ea and Warth et al.(1998) prefactor with deltan_int=-1""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2,
    label = "Y_biCyc4;Y_rad;XH_Rrad",
    group1 = 
"""
1  *1 R!H 1 {5,{S,D,B,T}}
2  *2 R!H 0 {3,{S,D}} {4,S} {5,{S,D,B}}
3  *3 R!H 1 {2,{S,D}}
4  *4 H 0 {2,S}
5     R!H 0 {1,{S,D,B,T}} {2,{S,D,B}}
""",
    group2 = 
"""
1  *1 R!H 1
""",
    group3 = 
"""
1  *2 R!H 0 {2,{S,D}} {3,S}
2  *3 R!H 1 {1,{S,D}}
3  *4 H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.66e+10,"s^-1"),
        n = 1,
        alpha = 0,
        E0 = (16.3,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Herbinet et al.(2006) reference Ea and Warth et al.(1998) prefactor with deltan_int=-1""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 3,
    label = "Y_biCyc5;Y_rad;XH_Rrad",
    group1 = "OR{Y_biCyc5radEndo, Y_biCyc5radExo}",
    group2 = 
"""
1  *1 R!H 1
""",
    group3 = 
"""
1  *2 R!H 0 {2,{S,D}} {3,S}
2  *3 R!H 1 {1,{S,D}}
3  *4 H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.66e+10,"s^-1"),
        n = 1,
        alpha = 0,
        E0 = (7.75,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Herbinet et al.(2006) reference Ea and Warth et al.(1998) prefactor with deltan_int=-1""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 4,
    label = "Y_biCyc6;Y_rad;XH_Rrad",
    group1 = "OR{Y_biCyc6radEndo, Y_biCyc6radExo}",
    group2 = 
"""
1  *1 R!H 1
""",
    group3 = 
"""
1  *2 R!H 0 {2,{S,D}} {3,S}
2  *3 R!H 1 {1,{S,D}}
3  *4 H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.66e+10,"s^-1"),
        n = 1,
        alpha = 0,
        E0 = (3.85,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Herbinet et al.(2006) reference Ea and Warth et al.(1998) prefactor with deltan_int=-1""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 5,
    label = "Y_biCyc7;Y_rad;XH_Rrad",
    group1 = "OR{Y_biCyc7radEndo, Y_biCyc7radExo}",
    group2 = 
"""
1  *1 R!H 1
""",
    group3 = 
"""
1  *2 R!H 0 {2,{S,D}} {3,S}
2  *3 R!H 1 {1,{S,D}}
3  *4 H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.66e+10,"s^-1"),
        n = 1,
        alpha = 0,
        E0 = (7.75,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Herbinet et al.(2006) reference Ea and Warth et al.(1998) prefactor with deltan_int=-1""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

