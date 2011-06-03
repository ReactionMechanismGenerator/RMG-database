#!/usr/bin/env python
# encoding: utf-8

name = "Cyclic_Ether_Formation/rules"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 812,
    label = "RnOOH;Y_rad_intra",
    group1 = "OR{R2OOH, R3OOH, R4OOH, R5OOH}",
    group2 = 
"""
1  *1 R 1
""",
    kinetics = ArrheniusEP(
        A = (1e+11,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (10,"kcal/mol"),
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
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 813,
    label = "R2OOH_S;C_pri_rad_intra",
    group1 = 
"""
1  *1 {Cd,Cs} 1 {2,S}
2  *4 {Cd,Cs} 0 {1,S} {3,S}
3  *2 O 0 {2,S} {4,S}
4  *3 O 0 {3,S} {5,S}
5     H 0 {4,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4  *4 C 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.98e+12,"s^-1","*|/",1.2),
        n = 0,
        alpha = (1.3,"","+|-",0.3),
        E0 = (37,"kcal/mol","+|-",3),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 814,
    label = "R2OOH_S;C_sec_rad_intra",
    group1 = 
"""
1  *1 {Cd,Cs} 1 {2,S}
2  *4 {Cd,Cs} 0 {1,S} {3,S}
3  *2 O 0 {2,S} {4,S}
4  *3 O 0 {3,S} {5,S}
5     H 0 {4,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3  *4 C 0 {1,S}
4     R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.38e+12,"s^-1","*|/",1.2),
        n = 0,
        alpha = (1.3,"","+|-",0.3),
        E0 = (37,"kcal/mol","+|-",3),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 815,
    label = "R2OOH_S;C_ter_rad_intra",
    group1 = 
"""
1  *1 {Cd,Cs} 1 {2,S}
2  *4 {Cd,Cs} 0 {1,S} {3,S}
3  *2 O 0 {2,S} {4,S}
4  *3 O 0 {3,S} {5,S}
5     H 0 {4,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2  *4 C 0 {1,S}
3     R!H 0 {1,S}
4     R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.09e+12,"s^-1","*|/",1.2),
        n = 0,
        alpha = (1.3,"","+|-",0.3),
        E0 = (37,"kcal/mol","+|-",3),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 816,
    label = "R3OOH_SS;C_pri_rad_intra",
    group1 = 
"""
1  *1 {Cd,Cs} 1 {2,S}
2  *4 {Cd,Cs} 0 {1,S} {3,S}
3     {Cd,Cs,CO} 0 {2,S} {4,S}
4  *2 O 0 {3,S} {5,S}
5  *3 O 0 {4,S} {6,S}
6     H 0 {5,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4  *4 C 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.47e+11,"s^-1","*|/",1.74),
        n = 0,
        alpha = (1,"","+|-",0.1),
        E0 = (38.2,"kcal/mol","+|-",3),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 817,
    label = "R3OOH_SS;C_sec_rad_intra",
    group1 = 
"""
1  *1 {Cd,Cs} 1 {2,S}
2  *4 {Cd,Cs} 0 {1,S} {3,S}
3     {Cd,Cs,CO} 0 {2,S} {4,S}
4  *2 O 0 {3,S} {5,S}
5  *3 O 0 {4,S} {6,S}
6     H 0 {5,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3  *4 C 0 {1,S}
4     R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.04e+11,"s^-1","*|/",1.74),
        n = 0,
        alpha = (1,"","+|-",0.1),
        E0 = (38.2,"kcal/mol","+|-",3),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 818,
    label = "R3OOH_SS;C_ter_rad_intra",
    group1 = 
"""
1  *1 {Cd,Cs} 1 {2,S}
2  *4 {Cd,Cs} 0 {1,S} {3,S}
3     {Cd,Cs,CO} 0 {2,S} {4,S}
4  *2 O 0 {3,S} {5,S}
5  *3 O 0 {4,S} {6,S}
6     H 0 {5,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2  *4 C 0 {1,S}
3     R!H 0 {1,S}
4     R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.31e+11,"s^-1","*|/",1.74),
        n = 0,
        alpha = (1,"","+|-",0.1),
        E0 = (38.2,"kcal/mol","+|-",3),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 819,
    label = "R4OOH_SSS;C_pri_rad_intra",
    group1 = 
"""
1  *1 {Cd,Cs} 1 {2,S}
2  *4 {Cd,Cs} 0 {1,S} {3,S}
3     {Cd,Cs,CO} 0 {2,S} {4,S}
4     {Cd,Cs,CO} 0 {3,S} {5,S}
5  *2 O 0 {4,S} {6,S}
6  *3 O 0 {5,S} {7,S}
7     H 0 {6,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4  *4 C 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.13e+10,"s^-1","*|/",1.41),
        n = 0,
        alpha = 0,
        E0 = (14.8,"kcal/mol","+|-",2),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 820,
    label = "R4OOH_SSS;C_sec_rad_intra",
    group1 = 
"""
1  *1 {Cd,Cs} 1 {2,S}
2  *4 {Cd,Cs} 0 {1,S} {3,S}
3     {Cd,Cs,CO} 0 {2,S} {4,S}
4     {Cd,Cs,CO} 0 {3,S} {5,S}
5  *2 O 0 {4,S} {6,S}
6  *3 O 0 {5,S} {7,S}
7     H 0 {6,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3  *4 C 0 {1,S}
4     R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.63e+10,"s^-1","*|/",1.41),
        n = 0,
        alpha = 0,
        E0 = (13,"kcal/mol","+|-",2.5),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 821,
    label = "R4OOH_SSS;C_ter_rad_intra",
    group1 = 
"""
1  *1 {Cd,Cs} 1 {2,S}
2  *4 {Cd,Cs} 0 {1,S} {3,S}
3     {Cd,Cs,CO} 0 {2,S} {4,S}
4     {Cd,Cs,CO} 0 {3,S} {5,S}
5  *2 O 0 {4,S} {6,S}
6  *3 O 0 {5,S} {7,S}
7     H 0 {6,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2  *4 C 0 {1,S}
3     R!H 0 {1,S}
4     R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.57e+10,"s^-1","*|/",1.41),
        n = 0,
        alpha = 0,
        E0 = (11.5,"kcal/mol","+|-",3),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 822,
    label = "R2OOH_S;Cs_rad_intra",
    group1 = 
"""
1  *1 {Cd,Cs} 1 {2,S}
2  *4 {Cd,Cs} 0 {1,S} {3,S}
3  *2 O 0 {2,S} {4,S}
4  *3 O 0 {3,S} {5,S}
5     H 0 {4,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2  *4 C 0 {1,S}
3     R 0 {1,S}
4     R 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (6e+11,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (22,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 823,
    label = "R3OOH_SS;Cs_rad_intra",
    group1 = 
"""
1  *1 {Cd,Cs} 1 {2,S}
2  *4 {Cd,Cs} 0 {1,S} {3,S}
3     {Cd,Cs,CO} 0 {2,S} {4,S}
4  *2 O 0 {3,S} {5,S}
5  *3 O 0 {4,S} {6,S}
6     H 0 {5,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2  *4 C 0 {1,S}
3     R 0 {1,S}
4     R 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7.5e+10,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (15.25,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 824,
    label = "R4OOH_SSS;Cs_rad_intra",
    group1 = 
"""
1  *1 {Cd,Cs} 1 {2,S}
2  *4 {Cd,Cs} 0 {1,S} {3,S}
3     {Cd,Cs,CO} 0 {2,S} {4,S}
4     {Cd,Cs,CO} 0 {3,S} {5,S}
5  *2 O 0 {4,S} {6,S}
6  *3 O 0 {5,S} {7,S}
7     H 0 {6,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2  *4 C 0 {1,S}
3     R 0 {1,S}
4     R 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (9.38e+09,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 825,
    label = "R5OOH_SSSS;Cs_rad_intra",
    group1 = 
"""
1  *1 {Cd,Cs} 1 {2,S}
2  *4 {Cd,Cs} 0 {1,S} {3,S}
3     {Cd,Cs,CO} 0 {2,S} {4,S}
4     {Cd,Cs,CO} 0 {3,S} {5,S}
5     {Cd,Cs,CO} 0 {4,S} {6,S}
6  *2 O 0 {5,S} {7,S}
7  *3 O 0 {6,S} {8,S}
8     H 0 {7,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2  *4 C 0 {1,S}
3     R 0 {1,S}
4     R 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.17e+09,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (1.8,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

