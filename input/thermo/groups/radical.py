#!/usr/bin/env python
# encoding: utf-8

name = "Radical Corrections"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 0,
    label = "Radical",
    group = "OR{RJ, RJ2, RJ3}",
    thermo = 'RJ',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1,
    label = "RJ",
    group = 
"""
1  *  R 1
""",
    thermo = 'CJ',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2,
    label = "CJ",
    group = 
"""
1  *  C 1
""",
    thermo = 'CsJ',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 3,
    label = "CsJ",
    group = 
"""
1  *  Cs 1
""",
    thermo = 'Cs_P',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 4,
    label = "CH3",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.71,0.34,-0.33,-1.07,-2.43,-3.54,-5.43],"cal/(mol*K)"),
        H298 = (104.81,"kcal/mol","+|-",0.1),
        S298 = (0.52,"cal/(mol*K)"),
    ),
    shortDesc = u"""Calculated in relation to methane from NIST values""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 5,
    label = "Cs_P",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     C 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.77,-1.36,-1.91,-2.4,-3.16,-3.74,-4.66],"cal/(mol*K)"),
        H298 = (101.1,"kcal/mol"),
        S298 = (2.61,"cal/(mol*K)"),
    ),
    shortDesc = u"""Generic primary radical. (CHEN & BOZZELLI) #""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 6,
    label = "CsCsJ",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     Cs 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    thermo = 'Cs_P',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 11,
    label = "CJCOOH",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     Cs 0 {1,S} {5,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     O 0 {2,S} {6,S}
6     Os 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.25,-0.76,-1.34,-1.91,-2.87,-3.6,-4.69],"cal/(mol*K)"),
        H298 = (103.26,"kcal/mol"),
        S298 = (3.54,"cal/(mol*K)"),
    ),
    shortDesc = u"""WIJAYA et al.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 7,
    label = "CCJ",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     C 0 {1,S} {5,S} {6,S} {7,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
7     H 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.65,-1.21,-1.75,-2.24,-3.02,-3.63,-3.63],"cal/(mol*K)"),
        H298 = (101.1,"kcal/mol","+|-",0.2),
        S298 = (2.61,"cal/(mol*K)"),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 8,
    label = "RCCJ",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     C 0 {1,S} {5,S} {6,S} {7,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     C 0 {2,S}
6     H 0 {2,S}
7     H 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.77,-1.36,-1.91,-2.4,-3.16,-3.74,-4.66],"cal/(mol*K)"),
        H298 = (101.1,"kcal/mol","+|-",0.2),
        S298 = (2.61,"cal/(mol*K)"),
    ),
    shortDesc = u"""LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 9,
    label = "Isobutyl",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     C 0 {1,S} {5,S} {6,S} {7,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     C 0 {2,S}
6     C 0 {2,S}
7     H 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.54,-1.26,-1.92,-2.46,-3.27,-3.84,-3.84],"cal/(mol*K)"),
        H298 = (101.1,"kcal/mol"),
        S298 = (2.91,"cal/(mol*K)"),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 10,
    label = "Neopentyl",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     C 0 {1,S} {5,S} {6,S} {7,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     C 0 {2,S}
6     C 0 {2,S}
7     C 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.59,-1.32,-2.05,-2.65,-3.5,-4.06,-4.87],"cal/(mol*K)"),
        H298 = (101.1,"kcal/mol"),
        S298 = (3.03,"cal/(mol*K)"),
    ),
    shortDesc = u"""LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 12,
    label = "Benzyl_P",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     Cb 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.75,0.6,0.13,-0.42,-1.41,-2.18,-2.18],"cal/(mol*K)"),
        H298 = (88.5,"kcal/mol","+|-",0.1),
        S298 = (-4.74,"cal/(mol*K)"),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 13,
    label = "Allyl_P",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     Cd 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.62,-0.56,-0.78,-1.12,-1.84,-2.46,-3.49],"cal/(mol*K)"),
        H298 = (88.2,"kcal/mol"),
        S298 = (-2.56,"cal/(mol*K)"),
    ),
    shortDesc = u"""LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 14,
    label = "C=CC=CCJ",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     Cd 0 {1,S} {5,D}
3     H 0 {1,S}
4     H 0 {1,S}
5     C 0 {2,D} {6,S}
6     Cd 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-1.83,-1.86,-1.98,-1.99,-2.3,-2.5,-2.5],"cal/(mol*K)"),
        H298 = (80,"kcal/mol"),
        S298 = (-1.55,"cal/(mol*K)"),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 15,
    label = "CTCC=CCJ",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     Cd 0 {1,S} {5,D}
3     H 0 {1,S}
4     H 0 {1,S}
5     C 0 {2,D} {6,S}
6     Ct 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-1.09,-1.62,-2.01,-2.63,-3.07,-3.48,-3.48],"cal/(mol*K)"),
        H298 = (81,"kcal/mol"),
        S298 = (-3.55,"cal/(mol*K)"),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 17,
    label = "Propargyl",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     Ct 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.84,-1.17,-1.56,-1.95,-2.7,-3.31,-5.31],"cal/(mol*K)"),
        H298 = (89.4,"kcal/mol"),
        S298 = (-0.51,"cal/(mol*K)"),
    ),
    shortDesc = u"""LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 16,
    label = "C2JC=O",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     CO 0 {1,S} {5,D} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     O 0 {2,D}
6     C 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.32,0.19,-0.15,-0.57,-1.43,-2.22,-3.67],"cal/(mol*K)"),
        H298 = (94.4,"kcal/mol"),
        S298 = (-1.16,"cal/(mol*K)"),
    ),
    shortDesc = u"""CHEN & BOZZELLI""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 18,
    label = "Cs_S",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     C 0 {1,S}
3     C 0 {1,S}
4     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-1.5,-2.33,-3.1,-3.39,-3.75,-4.45,-5.2],"cal/(mol*K)"),
        H298 = (98.45,"kcal/mol"),
        S298 = (4.44,"cal/(mol*K)"),
    ),
    shortDesc = u"""Generic secondary radical. (CHEN & BOZZELLI) #""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 19,
    label = "(Cs)2CsJ",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     Cs 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    thermo = 'Cs_S',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 23,
    label = "CCJCOOH",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     Cs 0 {1,S} {5,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
5     O 0 {2,S} {6,S}
6     O 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.65,-1.4,-2,-2.5,-3.27,-3.84,-4.73],"cal/(mol*K)"),
        H298 = (99.98,"kcal/mol"),
        S298 = (4.79,"cal/(mol*K)"),
    ),
    shortDesc = u"""WIJAYA et al.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 20,
    label = "CCJC",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     C 0 {1,S} {5,S} {6,S} {7,S}
3     C 0 {1,S} {8,S} {9,S} {10,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
7     H 0 {2,S}
8     H 0 {3,S}
9     H 0 {3,S}
10    H 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],"cal/(mol*K)"),
        H298 = (98.45,"kcal/mol","+|-",0.2),
        S298 = (4.51,"cal/(mol*K)"),
    ),
    shortDesc = u"""LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 21,
    label = "RCCJC",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     C 0 {1,S} {5,S} {6,S} {7,S}
3     C 0 {1,S} {8,S} {9,S} {10,S}
4     H 0 {1,S}
5     C 0 {2,S}
6     H 0 {2,S}
7     H 0 {2,S}
8     H 0 {3,S}
9     H 0 {3,S}
10    H 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-1.54,-2.77,-3.49,-3.9,-4.35,-4.64,-4.64],"cal/(mol*K)"),
        H298 = (98.45,"kcal/mol"),
        S298 = (5.13,"cal/(mol*K)"),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 22,
    label = "RCCJCC",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     C 0 {1,S} {5,S} {6,S} {7,S}
3     C 0 {1,S} {8,S} {9,S} {10,S}
4     H 0 {1,S}
5     C 0 {2,S}
6     H 0 {2,S}
7     H 0 {2,S}
8     C 0 {3,S}
9     H 0 {3,S}
10    H 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-1.71,-3.14,-3.92,-4.33,-4.71,-4.92,-4.92],"cal/(mol*K)"),
        H298 = (98.45,"kcal/mol"),
        S298 = (4.9,"cal/(mol*K)"),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 24,
    label = "Benzyl_S",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     Cb 0 {1,S}
3     C 0 {1,S}
4     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.87,0.09,-0.63,-1.21,-2.07,-2.69,-2.69],"cal/(mol*K)"),
        H298 = (85.9,"kcal/mol"),
        S298 = (-5.04,"cal/(mol*K)"),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 25,
    label = "Allyl_S",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     Cd 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-1.54,-1.82,-2.08,-2.32,-2.75,-3.14,-3.85],"cal/(mol*K)"),
        H298 = (85.6,"kcal/mol"),
        S298 = (-3.81,"cal/(mol*K)"),
    ),
    shortDesc = u"""LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 27,
    label = "C=CCJC=C",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     Cd 0 {1,S}
3     Cd 0 {1,S}
4     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-2.13,-1.96,-1.88,-1.89,-2.2,-2.6,-2.6],"cal/(mol*K)"),
        H298 = (76,"kcal/mol"),
        S298 = (-4.05,"cal/(mol*K)"),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 28,
    label = "Sec_Propargyl",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     Ct 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.59,-1.2,-1.75,-2.19,-2.91,-3.49,-3.49],"cal/(mol*K)"),
        H298 = (87,"kcal/mol"),
        S298 = (-0.45,"cal/(mol*K)"),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 26,
    label = "CCJCHO",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     CO 0 {1,S} {5,D} {6,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
5     O 0 {2,D}
6     H 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-1.36,-1.57,-1.73,-1.89,-2.66,-3.11,-3.5],"cal/(mol*K)"),
        H298 = (91.9,"kcal/mol"),
        S298 = (-2.37,"cal/(mol*K)"),
    ),
    shortDesc = u"""CHEN & BOZZELLI #""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 29,
    label = "Cs_T",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     C 0 {1,S}
3     C 0 {1,S}
4     C 0 {1,S}
""",
    thermo = 'Tertalkyl',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 30,
    label = "Tertalkyl",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     Cs 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],"cal/(mol*K)"),
        H298 = (96.5,"kcal/mol"),
        S298 = (5.24,"cal/(mol*K)"),
    ),
    shortDesc = u"""LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 31,
    label = "C2CJCOOH",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     Cs 0 {1,S} {5,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     O 0 {2,S} {6,S}
6     O 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-3.54,-4.16,-4.44,-4.58,-4.74,-4.88,-5.23],"cal/(mol*K)"),
        H298 = (97.2,"kcal/mol"),
        S298 = (7.31,"cal/(mol*K)"),
    ),
    shortDesc = u"""WIJAYA et al.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 32,
    label = "Benzyl_T",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     Cb 0 {1,S}
3     C 0 {1,S}
4     C 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.27,-0.78,-1.54,-2.06,-2.74,-3.19,-3.19],"cal/(mol*K)"),
        H298 = (83.8,"kcal/mol"),
        S298 = (-5.34,"cal/(mol*K)"),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 33,
    label = "Allyl_T",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     Cd 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-1.79,-2.38,-2.74,-2.97,-3.28,-3.55,-3.55],"cal/(mol*K)"),
        H298 = (83.4,"kcal/mol"),
        S298 = (-3.69,"cal/(mol*K)"),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 35,
    label = "Tert_Propargyl",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     Ct 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.04,-1.01,-1.74,-2.41,-3.19,-3.65,-3.65],"cal/(mol*K)"),
        H298 = (84.5,"kcal/mol"),
        S298 = (1.48,"cal/(mol*K)"),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 34,
    label = "C2CJCHO",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     CO 0 {1,S} {5,D} {6,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     O 0 {2,D}
6     H 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.62,-0.2,-1.23,-1.82,-2.87,-3.47,-3.47],"cal/(mol*K)"),
        H298 = (89.8,"kcal/mol"),
        S298 = (-1.71,"cal/(mol*K)"),
    ),
    shortDesc = u"""CHEN & BOZZELLI #. Value for Cp1500 taken as equal to Cp1000""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 36,
    label = "CsJO",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     O 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    thermo = 'CsJOH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 37,
    label = "CsJOH",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.25,0.18,-0.26,-0.83,-1.95,-2.85,-4.22],"cal/(mol*K)"),
        H298 = (96.51,"kcal/mol"),
        S298 = (0.09,"cal/(mol*K)"),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 38,
    label = "CsJOC",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     C 0 {2,S}
""",
    thermo = 'CsJOCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 39,
    label = "CsJOCs",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Cs 0 {2,S}
""",
    thermo = 'CsJOCH3',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 40,
    label = "CsJOCH3",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     C 0 {2,S} {6,S} {7,S} {8,S}
6     H 0 {5,S}
7     H 0 {5,S}
8     H 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.16,-0.4,-0.82,-1.33,-2.32,-3.13,-4.37],"cal/(mol*K)"),
        H298 = (97,"kcal/mol"),
        S298 = (0.78,"cal/(mol*K)"),
    ),
    shortDesc = u"""SUMATHI & GREEN #""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 41,
    label = "CsJOCC",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     C 0 {2,S} {6,S} {7,S} {8,S}
6     C 0 {5,S}
7     H 0 {5,S}
8     H 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-1.01,-1.22,-1.4,-1.71,-3.5,-3.24,-4.42],"cal/(mol*K)"),
        H298 = (96.83,"kcal/mol"),
        S298 = (1.41,"cal/(mol*K)"),
    ),
    shortDesc = u"""Calculated from data in SUMATHI & GREEN. Values might have large error bars.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 42,
    label = "CsJOCC2",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     C 0 {2,S} {6,S} {7,S} {8,S}
6     C 0 {5,S}
7     C 0 {5,S}
8     H 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.95,0.75,0.23,-0.43,-1.71,-2.72,-4.19],"cal/(mol*K)"),
        H298 = (96.16,"kcal/mol"),
        S298 = (-0.59,"cal/(mol*K)"),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 43,
    label = "CsJOCC3",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     C 0 {2,S} {6,S} {7,S} {8,S}
6     C 0 {5,S}
7     C 0 {5,S}
8     C 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.08,-0.09,-0.52,-1.06,-2.11,-2.96,-4.27],"cal/(mol*K)"),
        H298 = (95.75,"kcal/mol"),
        S298 = (0.27,"cal/(mol*K)"),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 44,
    label = "CsJOCds",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     {Cd,CO} 0 {2,S}
""",
    thermo = 'CsJOC(O)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 45,
    label = "CsJOC(O)",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     C 0 {2,S} {6,D}
6     O 0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.91,0.89,0.42,-0.21,-1.5,-2.62,-4.43],"cal/(mol*K)"),
        H298 = (100.7,"kcal/mol"),
        S298 = (-0.18,"cal/(mol*K)"),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 46,
    label = "CsJOC(O)H",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     C 0 {2,S} {6,D} {7,S}
6     O 0 {5,D}
7     H 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.95,0.97,0.53,-0.12,-1.54,-2.76,-4.53],"cal/(mol*K)"),
        H298 = (100.88,"kcal/mol"),
        S298 = (-0.18,"cal/(mol*K)"),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 47,
    label = "CsJOC(O)C",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     C 0 {2,S} {6,D} {7,S}
6     O 0 {5,D}
7     C 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.88,0.81,0.31,-0.3,-1.45,-2.47,-4.33],"cal/(mol*K)"),
        H298 = (100.48,"kcal/mol"),
        S298 = (-0.17,"cal/(mol*K)"),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 48,
    label = "CsJOO",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     O 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.18,-0.42,-0.79,-1.2,-1.99,-2.63,-3.65],"cal/(mol*K)"),
        H298 = (98.5,"kcal/mol"),
        S298 = (-1.57,"cal/(mol*K)"),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 49,
    label = "CsJOOH",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     O 0 {2,S} {6,S}
6     H 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.06,-0.35,-0.76,-1.19,-1.99,-2.64,-3.68],"cal/(mol*K)"),
        H298 = (98.91,"kcal/mol"),
        S298 = (-1.52,"cal/(mol*K)"),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 50,
    label = "CsJOOC",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     O 0 {2,S} {6,S}
6     C 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.31,-0.48,-0.82,-1.22,-1.99,-2.62,-3.63],"cal/(mol*K)"),
        H298 = (98.34,"kcal/mol"),
        S298 = (-1.62,"cal/(mol*K)"),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 51,
    label = "CCsJO",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     O 0 {1,S}
3     C 0 {1,S}
4     H 0 {1,S}
""",
    thermo = 'CCsJOC',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 52,
    label = "CCsJOH",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3     C 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.65,-0.01,-0.75,-1.43,-2.52,-3.31,-4.47],"cal/(mol*K)"),
        H298 = (95.39,"kcal/mol"),
        S298 = (0.92,"cal/(mol*K)"),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 53,
    label = "CCsJOC",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3     C 0 {1,S}
4     H 0 {1,S}
5     C 0 {2,S}
""",
    thermo = 'CCsJOCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 54,
    label = "CCsJOCs",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3     C 0 {1,S}
4     H 0 {1,S}
5     Cs 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.82,0.53,-0.11,-0.86,-2.2,-3.18,-4.51],"cal/(mol*K)"),
        H298 = (95.41,"kcal/mol"),
        S298 = (0.33,"cal/(mol*K)"),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 55,
    label = "CCsJOCds",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3     C 0 {1,S}
4     H 0 {1,S}
5     {CO,Cd} 0 {2,S}
""",
    thermo = 'CCsJOC(O)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 56,
    label = "CCsJOC(O)",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3     C 0 {1,S}
4     H 0 {1,S}
5     C 0 {2,S} {6,D}
6     O 0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([1.16,0.78,0.05,-0.73,-2.13,-3.24,-4.9],"cal/(mol*K)"),
        H298 = (98.7,"kcal/mol"),
        S298 = (0.98,"cal/(mol*K)"),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 57,
    label = "CCsJOC(O)H",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3     C 0 {1,S}
4     H 0 {1,S}
5     C 0 {2,S} {6,D} {7,S}
6     O 0 {5,D}
7     H 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([1.2,0.88,0.16,-0.67,-2.22,-3.43,-5],"cal/(mol*K)"),
        H298 = (98.87,"kcal/mol"),
        S298 = (0.98,"cal/(mol*K)"),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = -1,
    label = "CCsJOC(O)C",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3     C 0 {1,S}
4     H 0 {1,S}
5     C 0 {2,S} {6,D} {7,S}
6     O 0 {5,D}
7     C 0 {5,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 58,
    label = "CCsJOO",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3     C 0 {1,S}
4     H 0 {1,S}
5     O 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.48,-1.15,-1.68,-2.11,-2.77,-3.26,-4.02],"cal/(mol*K)"),
        H298 = (96.9,"kcal/mol"),
        S298 = (0.76,"cal/(mol*K)"),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 59,
    label = "CCsJOOH",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3     C 0 {1,S}
4     H 0 {1,S}
5     O 0 {2,S} {6,S}
6     H 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.39,-1.08,-1.64,-2.08,-2.75,-3.26,-4.03],"cal/(mol*K)"),
        H298 = (97.19,"kcal/mol"),
        S298 = (0.77,"cal/(mol*K)"),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 60,
    label = "CCsJOOC",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3     C 0 {1,S}
4     H 0 {1,S}
5     O 0 {2,S} {6,S}
6     C 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.58,-1.21,-1.73,-2.15,-2.8,-3.27,-4.01],"cal/(mol*K)"),
        H298 = (96.64,"kcal/mol"),
        S298 = (0.74,"cal/(mol*K)"),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 61,
    label = "C2CsJO",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     O 0 {1,S}
3     C 0 {1,S}
4     C 0 {1,S}
""",
    thermo = 'C2CsJOC',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 62,
    label = "C2CsJOH",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3     C 0 {1,S}
4     C 0 {1,S}
5     H 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.31,-0.66,-1.54,-2.23,-3.17,-3.8,-4.72],"cal/(mol*K)"),
        H298 = (94.5,"kcal/mol"),
        S298 = (2.17,"cal/(mol*K)"),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 63,
    label = "C2CsJOC",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3     C 0 {1,S}
4     C 0 {1,S}
5     C 0 {2,S}
""",
    thermo = 'C2CsJOCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 64,
    label = "C2CsJOCs",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3     C 0 {1,S}
4     C 0 {1,S}
5     Cs 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.09,-1.37,-2.49,-3.26,-4.15,-4.63,-5.23],"cal/(mol*K)"),
        H298 = (95.5,"kcal/mol"),
        S298 = (3.71,"cal/(mol*K)"),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 65,
    label = "C2CsJOCds",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3     C 0 {1,S}
4     C 0 {1,S}
5     {Cd,CO} 0 {2,S}
""",
    thermo = 'C2CsJOC(O)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 66,
    label = "C2CsJOC(O)",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3     C 0 {1,S}
4     C 0 {1,S}
5     C 0 {2,S} {6,D}
6     O 0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.04,-1.34,-2.3,-2.99,-3.99,-4.77,-5.98],"cal/(mol*K)"),
        H298 = (100.1,"kcal/mol"),
        S298 = (4.77,"cal/(mol*K)"),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 67,
    label = "C2CsJOC(O)H",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3     C 0 {1,S}
4     C 0 {1,S}
5     C 0 {2,S} {6,D} {7,S}
6     O 0 {5,D}
7     H 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.03,-1.28,-2.28,-3.1,-4.35,-5.19,-6.06],"cal/(mol*K)"),
        H298 = (99.97,"kcal/mol"),
        S298 = (4.88,"cal/(mol*K)"),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 68,
    label = "C2CsJOC(O)C",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3     C 0 {1,S}
4     C 0 {1,S}
5     C 0 {2,S} {6,D} {7,S}
6     O 0 {5,D}
7     C 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.04,-1.4,-2.32,-2.89,-3.62,-4.36,-5.9],"cal/(mol*K)"),
        H298 = (100.25,"kcal/mol"),
        S298 = (4.66,"cal/(mol*K)"),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 69,
    label = "C2CsJOO",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3     C 0 {1,S}
4     C 0 {1,S}
5     O 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.89,-2.09,-2.81,-3.24,-3.69,-3.97,-4.43],"cal/(mol*K)"),
        H298 = (96.7,"kcal/mol"),
        S298 = (2.22,"cal/(mol*K)"),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 70,
    label = "C2CsJOOH",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3     C 0 {1,S}
4     C 0 {1,S}
5     O 0 {2,S} {6,S}
6     H 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-1.01,-2.17,-2.87,-3.3,-3.77,-4.05,-4.49],"cal/(mol*K)"),
        H298 = (96.74,"kcal/mol"),
        S298 = (2.37,"cal/(mol*K)"),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 71,
    label = "C2CsJOOC",
    group = 
"""
1  *  C 1 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3     C 0 {1,S}
4     C 0 {1,S}
5     O 0 {2,S} {6,S}
6     C 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.78,-2.02,-2.75,-3.18,-3.62,-3.88,-4.37],"cal/(mol*K)"),
        H298 = (96.58,"kcal/mol"),
        S298 = (2.08,"cal/(mol*K)"),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 72,
    label = "CdsJ",
    group = 
"""
1  *  {Cd,CO} 1
""",
    thermo = 'Cds_P',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 79,
    label = "CdsJO",
    group = 
"""
1  *  C 1 {2,D}
2     O 0 {1,D}
""",
    thermo = 'CCJ=O',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 80,
    label = "HCdsJO",
    group = 
"""
1  *  C 1 {2,D} {3,S}
2     O 0 {1,D}
3     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.19,-0.65,-1.19,-1.73,-2.63,-3.32,-4.42],"cal/(mol*K)"),
        H298 = (88.45,"kcal/mol"),
        S298 = (-0.01,"cal/(mol*K)"),
    ),
    shortDesc = u"""Calculated in relation to formaldehyde from NIST values""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 81,
    label = "CCJ=O",
    group = 
"""
1  *  C 1 {2,D} {3,S}
2     O 0 {1,D}
3     C 0 {1,S}
""",
    thermo = 'CsCJ=O',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 82,
    label = "CsCJ=O",
    group = 
"""
1  *  C 1 {2,D} {3,S}
2     O 0 {1,D}
3     Cs 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.83,-1.43,-1.96,-2.42,-3.16,-3.73,-4.64],"cal/(mol*K)"),
        H298 = (89,"kcal/mol"),
        S298 = (1.12,"cal/(mol*K)"),
    ),
    shortDesc = u"""CHEN & BOZZELLI #""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 83,
    label = "C=CCJ=O",
    group = 
"""
1  *  C 1 {2,D} {3,S}
2     O 0 {1,D}
3     Cd 0 {1,S} {4,D}
4     Cd 0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.19,-0.85,-1.59,-2.21,-3.21,-3.89,-4.61],"cal/(mol*K)"),
        H298 = (83,"kcal/mol"),
        S298 = (-1.39,"cal/(mol*K)"),
    ),
    shortDesc = u"""CHEN & BOZZELLI #""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 84,
    label = "(O)CJO",
    group = 
"""
1  *  C 1 {2,D} {3,S}
2     O 0 {1,D}
3     O 0 {1,S}
""",
    thermo = '(O)CJOC',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 85,
    label = "(O)CJOH",
    group = 
"""
1  *  C 1 {2,D} {3,S}
2     O 0 {1,D}
3     O 0 {1,S} {4,S}
4     H 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.02,-0.66,-1.4,-2.12,-3.41,-4.44,-5.79],"cal/(mol*K)"),
        H298 = (100.75,"kcal/mol"),
        S298 = (0.78,"cal/(mol*K)"),
    ),
    shortDesc = u"""SUMATHI & GREEN #""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 86,
    label = "(O)CJOC",
    group = 
"""
1  *  C 1 {2,D} {3,S}
2     O 0 {1,D}
3     O 0 {1,S} {4,S}
4     C 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.45,-0.27,-1.19,-2.1,-3.63,-4.69,-5.8],"cal/(mol*K)"),
        H298 = (98.99,"kcal/mol"),
        S298 = (0.72,"cal/(mol*K)"),
    ),
    shortDesc = u"""SUMATHI & GREEN (Hf assigned value of (O)CJOCH(CH3)2)""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 87,
    label = "(O)CJOCH3",
    group = 
"""
1  *  C 1 {2,D} {3,S}
2     O 0 {1,D}
3     O 0 {1,S} {4,S}
4     C 0 {3,S} {5,S} {6,S} {7,S}
5     H 0 {4,S}
6     H 0 {4,S}
7     H 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.51,-0.11,-0.94,-1.8,-3.34,-4.48,-5.79],"cal/(mol*K)"),
        H298 = (100.1,"kcal/mol"),
        S298 = (0.72,"cal/(mol*K)"),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 88,
    label = "(O)CJOCC",
    group = 
"""
1  *  C 1 {2,D} {3,S}
2     O 0 {1,D}
3     O 0 {1,S} {4,S}
4     C 0 {3,S} {5,S} {6,S} {7,S}
5     C 0 {4,S}
6     H 0 {4,S}
7     H 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.45,-0.13,-0.98,-1.86,-3.43,-4.56,-5.79],"cal/(mol*K)"),
        H298 = (99.49,"kcal/mol"),
        S298 = (0.55,"cal/(mol*K)"),
    ),
    shortDesc = u"""SUMATHI & GREEN (values from (O)CJOCH2CH3)""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 89,
    label = "(O)CJOCC2",
    group = 
"""
1  *  C 1 {2,D} {3,S}
2     O 0 {1,D}
3     O 0 {1,S} {4,S}
4     C 0 {3,S} {5,S} {6,S} {7,S}
5     C 0 {4,S}
6     C 0 {4,S}
7     H 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.74,-0.06,-1.04,-2.01,-3.6,-4.66,-5.77],"cal/(mol*K)"),
        H298 = (98.99,"kcal/mol"),
        S298 = (0.82,"cal/(mol*K)"),
    ),
    shortDesc = u"""SUMATHI & GREEN (values from (O)CJOCH(CH3)2)""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 90,
    label = "(O)CJOCC3",
    group = 
"""
1  *  C 1 {2,D} {3,S}
2     O 0 {1,D}
3     O 0 {1,S} {4,S}
4     C 0 {3,S} {5,S} {6,S} {7,S}
5     C 0 {4,S}
6     C 0 {4,S}
7     C 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.11,-0.79,-1.8,-2.73,-4.17,-5.06,-5.87],"cal/(mol*K)"),
        H298 = (97.98,"kcal/mol"),
        S298 = (0.76,"cal/(mol*K)"),
    ),
    shortDesc = u"""SUMATHI & GREEN (values from (O)CJOC(CH3)3)""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 74,
    label = "Cds_P",
    group = 
"""
1  *  C 1 {2,D} {3,S}
2     C 0 {1,D}
3     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.19,-0.75,-1.36,-1.92,-2.82,-3.49,-4.53],"cal/(mol*K)"),
        H298 = (111.2,"kcal/mol"),
        S298 = (1.39,"cal/(mol*K)"),
    ),
    shortDesc = u"""LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 75,
    label = "C=C=CJ",
    group = 
"""
1  *  C 1 {2,D} {3,S}
2     C 0 {1,D} {4,D}
3     H 0 {1,S}
4     C 0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.45,-1.05,-1.64,-2.15,-2.98,-3.6,-3.6],"cal/(mol*K)"),
        H298 = (89,"kcal/mol"),
        S298 = (1.29,"cal/(mol*K)"),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 77,
    label = "Cds_S",
    group = 
"""
1  *  C 1 {2,D} {3,S}
2     C 0 {1,D}
3     C 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],"cal/(mol*K)"),
        H298 = (109,"kcal/mol"),
        S298 = (1.81,"cal/(mol*K)"),
    ),
    shortDesc = u"""LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 78,
    label = "C=CJC=C",
    group = 
"""
1  *  C 1 {2,D} {3,S}
2     Cd 0 {1,D}
3     {Cd,CO} 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.19,-0.76,-1.51,-2.01,-2.7,-3.17,-3.17],"cal/(mol*K)"),
        H298 = (99.8,"kcal/mol"),
        S298 = (0.71,"cal/(mol*K)"),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 91,
    label = "CtJ",
    group = 
"""
1  *  C 1 {2,T}
2     C 0 {1,T}
""",
    thermo = 'Acetyl',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 92,
    label = "Acetyl",
    group = 
"""
1  *  C 1 {2,T}
2     C 0 {1,T} {3,S}
3     H 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.51,-1.56,-2.27,-2.78,-3.47,-3.97,-3.97],"cal/(mol*K)"),
        H298 = (132.7,"kcal/mol"),
        S298 = (2.11,"cal/(mol*K)"),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 93,
    label = "CbJ",
    group = 
"""
1  *  C 1 {2,B} {3,B}
2     C 0 {1,B}
3     C 0 {1,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.41,-1.18,-1.93,-2.69,-3.75,-4.48,-5.24],"cal/(mol*K)"),
        H298 = (113,"kcal/mol"),
        S298 = (1.48,"cal/(mol*K)"),
    ),
    shortDesc = u"""BDE from TSANG, S and Cp from THERM""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 94,
    label = "OJ",
    group = 
"""
1  *  O 1
""",
    thermo = 'COJ',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 95,
    label = "HOJ",
    group = 
"""
1  *  O 1 {2,S}
2     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.87,-1.1,-1.36,-1.62,-2.11,-2.53,-3.38],"cal/(mol*K)"),
        H298 = (119.22,"kcal/mol"),
        S298 = (-2.6,"cal/(mol*K)"),
    ),
    shortDesc = u"""Calculated from NIST values for H2O, OH and H""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 135,
    label = "COJ",
    group = 
"""
1  *  O 1 {2,S}
2     C 0 {1,S}
""",
    thermo = 'CsOJ',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 96,
    label = "CsOJ",
    group = 
"""
1  *  O 1 {2,S}
2     Cs 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.98,-1.3,-1.61,-1.89,-2.38,-2.8,-3.59],"cal/(mol*K)"),
        H298 = (104.06,"kcal/mol"),
        S298 = (-1.46,"cal/(mol*K)"),
    ),
    shortDesc = u"""CHEN & BOZZELLI(ROJ)""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 97,
    label = "H3COJ",
    group = 
"""
1  *  O 1 {2,S}
2     C 0 {1,S} {3,S} {4,S} {5,S}
3     H 0 {2,S}
4     H 0 {2,S}
5     H 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-1.11,-1.29,-1.62,-1.97,-2.59,-3.07,-3.84],"cal/(mol*K)"),
        H298 = (104.27,"kcal/mol"),
        S298 = (0.51,"cal/(mol*K)"),
    ),
    shortDesc = u"""Enthalpy HBI calculated from NIST values, entropy and Cp from B3LYP/6-31G* for CH3OH, CH3O and H""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 98,
    label = "CdsOJ",
    group = 
"""
1  *  O 1 {2,S}
2     {Cd,CO} 0 {1,S}
""",
    thermo = 'RC=COJ',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 99,
    label = "RC=COJ",
    group = 
"""
1  *  O 1 {2,S}
2     Cd 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-1.34,-1.99,-2.48,-2.79,-3.13,-3.33,-3.79],"cal/(mol*K)"),
        H298 = (88,"kcal/mol"),
        S298 = (-1.11,"cal/(mol*K)"),
    ),
    shortDesc = u"""CHEN & BOZZELLI""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 100,
    label = "OJC=O",
    group = 
"""
1  *  O 1 {2,S}
2     CO 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-1.31,-1.87,-2.32,-2.69,-3.28,-3.74,-4.56],"cal/(mol*K)"),
        H298 = (104,"kcal/mol"),
        S298 = (0.79,"cal/(mol*K)"),
    ),
    shortDesc = u"""CHEN & BOZZELLI""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 101,
    label = "OOJ",
    group = 
"""
1  *  O 1 {2,S}
2     O 0 {1,S}
""",
    thermo = 'ROOJ',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 102,
    label = "ROOJ",
    group = 
"""
1  *  O 1 {2,S}
2     O 0 {1,S} {3,S}
3     R!H 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-2.05,-2.84,-3.55,-4.09,-4.72,-4.97,-5.08],"cal/(mol*K)"),
        H298 = (88.2,"kcal/mol"),
        S298 = (0.22,"cal/(mol*K)"),
    ),
    shortDesc = u"""CHEN & BOZZELLI""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 104,
    label = "C(=O)OOJ",
    group = 
"""
1  *  O 1 {2,S}
2     O 0 {1,S} {3,S}
3     C 0 {2,S} {4,D}
4     O 0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-2.05,-2.84,-3.55,-4.09,-4.72,-4.97,-5.08],"cal/(mol*K)"),
        H298 = (98.33,"kcal/mol"),
        S298 = (0.22,"cal/(mol*K)"),
    ),
    shortDesc = u"""HBI for enthalpy from CHEN & BOZZELLI. Cp and S values taken from ROOJ""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 103,
    label = "C3COOJ",
    group = 
"""
1  *  O 1 {2,S}
2     O 0 {1,S} {3,S}
3     C 0 {2,S} {4,S} {5,S} {6,S}
4     C 0 {3,S}
5     C 0 {3,S}
6     C 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-2.05,-2.84,-3.55,-4.09,-4.72,-4.97,-5.08],"cal/(mol*K)"),
        H298 = (85.3,"kcal/mol"),
        S298 = (0.22,"cal/(mol*K)"),
    ),
    shortDesc = u"""CHEN & BOZZELLI""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 105,
    label = "HOOJ",
    group = 
"""
1  *  O 1 {2,S}
2     O 0 {1,S} {3,S}
3     H 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-1.99,-2.68,-3.07,-3.3,-3.55,-3.66,-3.9],"cal/(mol*K)"),
        H298 = (85.13,"kcal/mol"),
        S298 = (-0.92,"cal/(mol*K)"),
    ),
    shortDesc = u"""Calculated from NIST values for H2O2, O2H and H""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 134,
    label = "SiJ",
    group = 
"""
1  *  Si 1
""",
    thermo = 'CJ',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 137,
    label = "SJ",
    group = 
"""
1  *  S 1
""",
    thermo = 'OJ',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 106,
    label = "RJ2",
    group = 
"""
1  *  R {2S,2T}
""",
    thermo = 'CJ2',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 107,
    label = "CJ2",
    group = 
"""
1  *  C {2S,2T}
""",
    thermo = 'CsJ2',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 108,
    label = "CsJ2",
    group = 
"""
1  *  Cs {2S,2T}
""",
    thermo = 'CH2',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 109,
    label = "CH2",
    group = 
"""
1  *  C {2S,2T} {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    thermo = 'CH2_t',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 110,
    label = "CH2_t",
    group = 
"""
1  *  C 2T {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.27,-1.08,-2.14,-3.23,-5.18,-6.74,-9.47],"cal/(mol*K)"),
        H298 = (214.44,"kcal/mol"),
        S298 = (-1.73,"cal/(mol*K)"),
    ),
    shortDesc = u"""Calculated for methylene in relation to methane from NIST values""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 111,
    label = "CH2_s",
    group = 
"""
1  *  C 2S {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.27,-1.08,-2.14,-3.23,-5.18,-6.74,-9.47],"cal/(mol*K)"),
        H298 = (223.7,"kcal/mol"),
        S298 = (-1.73,"cal/(mol*K)"),
    ),
    shortDesc = u"""BDE JANOSCHEK & ROSSI. S and Cp from CH2_t.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 112,
    label = "CsJ2_P",
    group = 
"""
1  *  C {2S,2T} {2,S} {3,S}
2     C 0 {1,S}
3     H 0 {1,S}
""",
    thermo = 'CsCsJ2',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 113,
    label = "CsCsJ2",
    group = 
"""
1  *  C {2S,2T} {2,S} {3,S}
2     Cs 0 {1,S}
3     H 0 {1,S}
""",
    thermo = 'CCJ2',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 114,
    label = "CCJ2",
    group = 
"""
1  *  C {2S,2T} {2,S} {3,S}
2     Cs 0 {1,S} {4,S} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {2,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    thermo = 'CCJ2_t',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 115,
    label = "CCJ2_t",
    group = 
"""
1  *  C 2T {2,S} {3,S}
2     Cs 0 {1,S} {4,S} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {2,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.81,-1.74,-2.69,-3.61,-5.18,-6.42,-8.36],"cal/(mol*K)"),
        H298 = (211.3,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    shortDesc = u"""BDE and Cp calculated from data in KIM et al.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 116,
    label = "CCJ2_s",
    group = 
"""
1  *  C 2S {2,S} {3,S}
2     Cs 0 {1,S} {4,S} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {2,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    thermo = 'CCJ2_t',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 117,
    label = "PhCH",
    group = 
"""
1  *  C {2S,2T} {2,S} {3,S}
2     Cb 0 {1,S}
3     H 0 {1,S}
""",
    thermo = 'PhCH_t',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 118,
    label = "PhCH_t",
    group = 
"""
1  *  C 2T {2,S} {3,S}
2     Cb 0 {1,S}
3     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (195,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    shortDesc = u"""BDE from PUTSMA et al.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 119,
    label = "PhCH_s",
    group = 
"""
1  *  C 2S {2,S} {3,S}
2     Cb 0 {1,S}
3     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (205.8,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    shortDesc = u"""BDE from NGUYEN et al.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 120,
    label = "AllylJ2",
    group = 
"""
1  *  C {2S,2T} {2,S} {3,S}
2     Cd 0 {1,S}
3     H 0 {1,S}
""",
    thermo = 'AllylJ2_t',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 121,
    label = "AllylJ2_t",
    group = 
"""
1  *  C 2T {2,S} {3,S}
2     Cd 0 {1,S}
3     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (192.8,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    shortDesc = u"""BDE from PUTSMA et al.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 122,
    label = "AllylJ2_s",
    group = 
"""
1  *  C 2S {2,S} {3,S}
2     Cd 0 {1,S}
3     H 0 {1,S}
""",
    thermo = 'AllylJ2_t',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 123,
    label = "CsJ2_S",
    group = 
"""
1  *  C {2S,2T} {2,S} {3,S}
2     C 0 {1,S}
3     C 0 {1,S}
""",
    thermo = 'CsJ2_P',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 124,
    label = "CdJ2",
    group = 
"""
1  *  {Cd,CO} {2S,2T}
""",
    thermo = 'CCdJ2',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 125,
    label = "CCdJ2",
    group = 
"""
1  *  C {2S,2T} {2,D}
2     C 0 {1,D}
""",
    thermo = 'CCdJ2_s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 126,
    label = "CCdJ2_t",
    group = 
"""
1  *  C 2T {2,D}
2     C 0 {1,D}
""",
    thermo = 'CCdJ2_s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 127,
    label = "CCdJ2_s",
    group = 
"""
1  *  C 2S {2,D}
2     C 0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (190.7,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    shortDesc = u"""BDE from ERWIN et al.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 128,
    label = "CO",
    group = 
"""
1  *  C {2S,2T} {2,D}
2     O 0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-1.5,-2.38,-3.32,-4.24,-5.75,-6.88,-8.59],"cal/(mol*K)"),
        H298 = (103.73,"kcal/mol"),
        S298 = (-6.47,"cal/(mol*K)"),
    ),
    shortDesc = u"""Value for carbon monoxide calculated in relation to formaldehyde from NIST values""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 129,
    label = "Oa",
    group = 
"""
1  *  O {2S,2T}
""",
    thermo = 'Oa_t',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 130,
    label = "Oa_t",
    group = 
"""
1  *  O 2T
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-2.8,-3.05,-3.33,-3.62,-4.24,-4.86,-6.28],"cal/(mol*K)"),
        H298 = (221.55,"kcal/mol"),
        S298 = (-8.02,"cal/(mol*K)"),
    ),
    shortDesc = u"""Calculated for atomic oxygen in relation to water from NIST values""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 131,
    label = "Oa_s",
    group = 
"""
1  *  O 2S
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-2.8,-3.05,-3.33,-3.62,-4.24,-4.86,-6.28],"cal/(mol*K)"),
        H298 = (266.9,"kcal/mol"),
        S298 = (-8.02,"cal/(mol*K)"),
    ),
    shortDesc = u"""BDE from SCHALLEY et al. S and Cp values taken from Oa_t""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 135,
    label = "SiJ2",
    group = 
"""
1  *  Si {2S,2T}
""",
    thermo = 'CJ2',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 138,
    label = "Sa",
    group = 
"""
1  *  S {2S,2T}
""",
    thermo = 'Oa',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 132,
    label = "RJ3",
    group = 
"""
1  *  R 3
""",
    thermo = 'CJ3',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 133,
    label = "CJ3",
    group = 
"""
1  *  C 3
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-1.57,-2.73,-4.11,-5.5,-7.92,-9.85,-12.95],"cal/(mol*K)"),
        H298 = (316.19,"kcal/mol"),
        S298 = (-5.7,"cal/(mol*K)"),
    ),
    shortDesc = u"""Calculated for methylidyene in relation to methane from NIST values""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 136,
    label = "SiJ3",
    group = 
"""
1  *  Si 3
""",
    thermo = 'CJ3',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

tree(
"""
L1: Radical
    L2: RJ
        L3: CJ
            L4: CsJ
                L5: CH3
                L5: Cs_P
                    L6: CsCsJ
                        L7: CJCOOH
                        L7: CCJ
                        L7: RCCJ
                        L7: Isobutyl
                        L7: Neopentyl
                    L6: Benzyl_P
                    L6: Allyl_P
                        L7: C=CC=CCJ
                        L7: CTCC=CCJ
                    L6: Propargyl
                    L6: C2JC=O
                L5: Cs_S
                    L6: (Cs)2CsJ
                        L7: CCJCOOH
                        L7: CCJC
                        L7: RCCJC
                        L7: RCCJCC
                    L6: Benzyl_S
                    L6: Allyl_S
                    L6: C=CCJC=C
                    L6: Sec_Propargyl
                    L6: CCJCHO
                L5: Cs_T
                    L6: Tertalkyl
                        L7: C2CJCOOH
                    L6: Benzyl_T
                    L6: Allyl_T
                    L6: Tert_Propargyl
                    L6: C2CJCHO
                L5: CsJO
                    L6: CsJOH
                    L6: CsJOC
                        L7: CsJOCs
                            L8: CsJOCH3
                            L8: CsJOCC
                            L8: CsJOCC2
                            L8: CsJOCC3
                        L7: CsJOCds
                            L8: CsJOC(O)
                                L9: CsJOC(O)H
                                L9: CsJOC(O)C
                    L6: CsJOO
                        L7: CsJOOH
                        L7: CsJOOC
                L5: CCsJO
                    L6: CCsJOH
                    L6: CCsJOC
                        L7: CCsJOCs
                        L7: CCsJOCds
                            L8: CCsJOC(O)
                                L9: CCsJOC(O)H
                                L9: CCsJOC(O)C
                    L6: CCsJOO
                        L7: CCsJOOH
                        L7: CCsJOOC
                L5: C2CsJO
                    L6: C2CsJOH
                    L6: C2CsJOC
                        L7: C2CsJOCs
                        L7: C2CsJOCds
                            L8: C2CsJOC(O)
                                L9: C2CsJOC(O)H
                                L9: C2CsJOC(O)C
                    L6: C2CsJOO
                        L7: C2CsJOOH
                        L7: C2CsJOOC
            L4: CdsJ
                L5: CdsJO
                    L6: HCdsJO
                    L6: CCJ=O
                        L7: CsCJ=O
                        L7: C=CCJ=O
                    L6: (O)CJO
                        L7: (O)CJOH
                        L7: (O)CJOC
                            L8: (O)CJOCH3
                            L8: (O)CJOCC
                            L8: (O)CJOCC2
                            L8: (O)CJOCC3
                L5: Cds_P
                    L6: C=C=CJ
                L5: Cds_S
                    L6: C=CJC=C
            L4: CtJ
                L5: Acetyl
            L4: CbJ
        L3: OJ
            L4: HOJ
            L4: COJ
                L5: CsOJ
                    L6: H3COJ
                L5: CdsOJ
                    L6: RC=COJ
                    L6: OJC=O
            L4: OOJ
                L5: ROOJ
                    L6: C(=O)OOJ
                    L6: C3COOJ
                L5: HOOJ
        L3: SiJ
        L3: SJ
    L2: RJ2
        L3: CJ2
            L4: CsJ2
                L5: CH2
                    L6: CH2_t
                    L6: CH2_s
                L5: CsJ2_P
                    L6: CsCsJ2
                        L7: CCJ2
                            L8: CCJ2_t
                            L8: CCJ2_s
                    L6: PhCH
                        L7: PhCH_t
                        L7: PhCH_s
                    L6: AllylJ2
                        L7: AllylJ2_t
                        L7: AllylJ2_s
                L5: CsJ2_S
            L4: CdJ2
                L5: CCdJ2
                    L6: CCdJ2_t
                    L6: CCdJ2_s
                L5: CO
        L3: Oa
            L4: Oa_t
            L4: Oa_s
        L3: SiJ2
        L3: Sa
    L2: RJ3
        L3: CJ3
        L3: SiJ3
"""
)

