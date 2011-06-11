#!/usr/bin/env python
# encoding: utf-8

name = "1,2-Birad_to_alkene/rules"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 1,
    label = "Y_12birad",
    group1 = "OR{Y_12_00, Y_12_10, Y_12_20, Y_12_30, Y_12_40, Y_12_01, Y_12_02, Y_12_03, Y_12_04, Y_12_11, Y_12_12, Y_12_21, Y_12_22, Y_12_13, Y_12_31}",
    kinetics = ArrheniusEP(
        A = (1e+08,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
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
    index = 2,
    label = "Y_12_00",
    group1 = 
"""
1  *1 Cs 1 {2,S} {3,S} {4,S}
2  *2 Cs 1 {1,S} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (1e+08,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""see references header of 1,2-Birad_to_alkene/rateLibrary.txt""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 3,
    label = "Y_12_10",
    group1 = 
"""
1  *1 Cs 1 {2,S} {3,S} {4,S}
2  *2 Cs 1 {1,S} {5,S} {6,S}
3     {Cs,Os} 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (6.31e+07,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""see references header of 1,2-Birad_to_alkene/rateLibrary.txt""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 4,
    label = "Y_12_20",
    group1 = "OR{Y_12_20a, Y_12_20b}",
    kinetics = ArrheniusEP(
        A = (3.98e+07,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""see references header of 1,2-Birad_to_alkene/rateLibrary.txt""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 5,
    label = "Y_12_30",
    group1 = 
"""
1  *1 Cs 1 {2,S} {3,S} {4,S}
2  *2 Cs 1 {1,S} {5,S} {6,S}
3     {Cs,Os} 0 {1,S}
4     {Cs,Os} 0 {1,S}
5     {Cs,Os} 0 {2,S}
6     H 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (2.51e+07,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""see references header of 1,2-Birad_to_alkene/rateLibrary.txt""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 6,
    label = "Y_12_40",
    group1 = 
"""
1  *1 Cs 1 {2,S} {3,S} {4,S}
2  *2 Cs 1 {1,S} {5,S} {6,S}
3     {Cs,Os} 0 {1,S}
4     {Cs,Os} 0 {1,S}
5     {Cs,Os} 0 {2,S}
6     {Cs,Os} 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (1.58e+07,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""see references header of 1,2-Birad_to_alkene/rateLibrary.txt""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 7,
    label = "Y_12_01",
    group1 = 
"""
1  *1 Cs 1 {2,S} {3,S} {4,S}
2  *2 Cs 1 {1,S} {5,S} {6,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (5.01e+07,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""see references header of 1,2-Birad_to_alkene/rateLibrary.txt""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 8,
    label = "Y_12_02",
    group1 = "OR{Y_12_02a, Y_12_02b}",
    kinetics = ArrheniusEP(
        A = (2.51e+07,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""see references header of 1,2-Birad_to_alkene/rateLibrary.txt""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 9,
    label = "Y_12_03",
    group1 = 
"""
1  *1 Cs 1 {2,S} {3,S} {4,S}
2  *2 Cs 1 {1,S} {5,S} {6,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {2,S}
6     H 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (1.26e+07,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""see references header of 1,2-Birad_to_alkene/rateLibrary.txt""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 10,
    label = "Y_12_04",
    group1 = 
"""
1  *1 Cs 1 {2,S} {3,S} {4,S}
2  *2 Cs 1 {1,S} {5,S} {6,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (6.31e+06,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""see references header of 1,2-Birad_to_alkene/rateLibrary.txt""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 11,
    label = "Y_12_11",
    group1 = "OR{Y_12_11a, Y_12_11b}",
    kinetics = ArrheniusEP(
        A = (3.16e+07,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""see references header of 1,2-Birad_to_alkene/rateLibrary.txt""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 12,
    label = "Y_12_12",
    group1 = "OR{Y_12_12a, Y_12_12b}",
    kinetics = ArrheniusEP(
        A = (1.58e+07,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""see references header of 1,2-Birad_to_alkene/rateLibrary.txt""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 13,
    label = "Y_12_21",
    group1 = "OR{Y_12_21a, Y_12_21b}",
    kinetics = ArrheniusEP(
        A = (2e+07,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""see references header of 1,2-Birad_to_alkene/rateLibrary.txt""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 14,
    label = "Y_12_22",
    group1 = "OR{Y_12_22a, Y_12_22b}",
    kinetics = ArrheniusEP(
        A = (1e+07,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""see references header of 1,2-Birad_to_alkene/rateLibrary.txt""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 15,
    label = "Y_12_13",
    group1 = 
"""
1  *1 Cs 1 {2,S} {3,S} {4,S}
2  *2 Cs 1 {1,S} {5,S} {6,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {2,S}
6     {Cs,Os} 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (7.94e+06,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""see references header of 1,2-Birad_to_alkene/rateLibrary.txt""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 16,
    label = "Y_12_31",
    group1 = 
"""
1  *1 Cs 1 {2,S} {3,S} {4,S}
2  *2 Cs 1 {1,S} {5,S} {6,S}
3     {Cs,Os} 0 {1,S}
4     {Cs,Os} 0 {1,S}
5     {Cs,Os} 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (1.26e+07,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""see references header of 1,2-Birad_to_alkene/rateLibrary.txt""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

