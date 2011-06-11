#!/usr/bin/env python
# encoding: utf-8

name = "Functional Group Additivity Values"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = -1,
    label = "R",
    group = 
"""
1  *  R 0
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
    index = 1,
    label = "C",
    group = 
"""
1  *  C 0
""",
    thermo = 'Cs-CsCsCsCs',
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
    label = "Cbf",
    group = 
"""
1  *  Cbf 0
""",
    thermo = 'Cbf-CbCbCbf',
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
    label = "Cbf-CbCbCbf",
    group = 
"""
1  *  Cbf 0 {2,B} {3,B} {4,B}
2     Cb 0 {1,B}
3     Cb 0 {1,B}
4     Cbf 0 {1,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.01,3.68,4.2,4.61,5.2,5.7,6.2],"cal/(mol*K)","+|-",0.1),
        H298 = (4.8,"kcal/mol","+|-",0.17),
        S298 = (-5,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""Cbf-CbfCbCb STEIN and FAHR; J. PHYS. CHEM. 1985, 89, 17, 3714""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 4,
    label = "Cbf-CbCbfCbf",
    group = 
"""
1  *  Cbf 0 {2,B} {3,B} {4,B}
2     Cb 0 {1,B}
3     Cbf 0 {1,B}
4     Cbf 0 {1,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.01,3.68,4.2,4.61,5.2,5.7,6.2],"cal/(mol*K)","+|-",0.15),
        H298 = (3.7,"kcal/mol","+|-",0.3),
        S298 = (-5,"cal/(mol*K)","+|-",0.15),
    ),
    shortDesc = u"""Cbf-CbfCbfCb STEIN and FAHR; J. PHYS. CHEM. 1985, 89, 17, 3714""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 5,
    label = "Cbf-CbfCbfCbf",
    group = 
"""
1  *  Cbf 0 {2,B} {3,B} {4,B}
2     Cbf 0 {1,B}
3     Cbf 0 {1,B}
4     Cbf 0 {1,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([2,3.11,3.9,4.42,5,5.3,5.7],"cal/(mol*K)","+|-",0.15),
        H298 = (1.5,"kcal/mol","+|-",0.3),
        S298 = (1.8,"cal/(mol*K)","+|-",0.15),
    ),
    shortDesc = u"""Cbf-CbfCbfCbf STEIN and FAHR; J. PHYS. CHEM. 1985, 89, 17, 3714""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 6,
    label = "Cb",
    group = 
"""
1  *  Cb 0
""",
    thermo = 'Cb-Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 7,
    label = "Cb-H",
    group = 
"""
1  *  Cb 0 {2,S}
2     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.24,4.44,5.46,6.3,7.54,8.41,9.73],"cal/(mol*K)","+|-",0.1),
        H298 = (3.3,"kcal/mol","+|-",0.11),
        S298 = (11.53,"cal/(mol*K)","+|-",0.12),
    ),
    shortDesc = u"""Cb-H BENSON""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 8,
    label = "Cb-Os",
    group = 
"""
1  *  Cb 0 {2,S}
2     Os 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.9,5.3,6.2,6.6,6.9,6.9,7.07],"cal/(mol*K)","+|-",0.1),
        H298 = (-0.9,"kcal/mol","+|-",0.16),
        S298 = (-10.2,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""Cb-O BENSON Cp1500=3D Cp1000*(Cp1500/Cp1000: Cb/Cd)""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 9,
    label = "Cb-C",
    group = 
"""
1  *  Cb 0 {2,S}
2     C 0 {1,S}
""",
    thermo = 'Cb-Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 10,
    label = "Cb-Cs",
    group = 
"""
1  *  Cb 0 {2,S}
2     Cs 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([2.67,3.14,3.68,4.15,4.96,5.44,5.98],"cal/(mol*K)","+|-",0.07),
        H298 = (5.51,"kcal/mol","+|-",0.13),
        S298 = (-7.69,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""Cb-Cs BENSON""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 11,
    label = "Cb-Cds",
    group = 
"""
1  *  Cb 0 {2,S}
2     {Cd,CO} 0 {1,S}
""",
    thermo = 'Cb-(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 12,
    label = "Cb-(Cds-Od)",
    group = 
"""
1  *  Cb 0 {2,S}
2     CO 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.59,3.97,4.38,4.72,5.28,5.61,5.75],"cal/(mol*K)","+|-",0.1),
        H298 = (3.69,"kcal/mol","+|-",0.2),
        S298 = (-7.8,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""Enthalpy from Cb-CO, entropies and heat capacities assigned value of Cb-Cd""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 13,
    label = "Cb-(Cds-Cd)",
    group = 
"""
1  *  Cb 0 {2,S}
2     Cd 0 {1,S}
""",
    thermo = 'Cb-(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 14,
    label = "Cb-(Cds-Cds)",
    group = 
"""
1  *  Cb 0 {2,S}
2     Cd 0 {1,S} {3,D}
3     Cd 0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.59,3.97,4.38,4.72,5.28,5.61,5.75],"cal/(mol*K)","+|-",0.1),
        H298 = (5.69,"kcal/mol","+|-",0.2),
        S298 = (-7.8,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""Cb-Cd STEIN and FAHR; J. PHYS. CHEM. 1985, 89, 17, 3714""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 15,
    label = "Cb-(Cds-Cdd)",
    group = 
"""
1  *  Cb 0 {2,S}
2     Cd 0 {1,S} {3,D}
3     Cdd 0 {2,D}
""",
    thermo = 'Cb-(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 16,
    label = "Cb-(Cds-Cdd-Od)",
    group = 
"""
1  *  Cb 0 {2,S}
2     Cd 0 {1,S} {3,D}
3     Cdd 0 {2,D} {4,D}
4     Od 0 {3,D}
""",
    thermo = 'Cb-(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 17,
    label = "Cb-(Cds-Cdd-Cd)",
    group = 
"""
1  *  Cb 0 {2,S}
2     Cd 0 {1,S} {3,D}
3     Cdd 0 {2,D} {4,D}
4     C 0 {3,D}
""",
    thermo = 'Cb-(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 18,
    label = "Cb-Ct",
    group = 
"""
1  *  Cb 0 {2,S}
2     Ct 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.59,3.97,4.38,4.72,5.28,5.61,5.75],"cal/(mol*K)","+|-",0.15),
        H298 = (5.69,"kcal/mol","+|-",0.3),
        S298 = (-7.8,"cal/(mol*K)","+|-",0.15),
    ),
    shortDesc = u"""Cb-Ct STEIN and FAHR; J. PHYS. CHEM. 1985, 89, 17, 3714""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 19,
    label = "Cb-Cb",
    group = 
"""
1  *  Cb 0 {2,S}
2     Cb 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.33,4.22,4.89,5.27,5.76,5.95,6.05],"cal/(mol*K)","+|-",0.15),
        H298 = (4.96,"kcal/mol","+|-",0.3),
        S298 = (-8.64,"cal/(mol*K)","+|-",0.15),
    ),
    shortDesc = u"""Cb-Cb BENSON""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 20,
    label = "Ct",
    group = 
"""
1  *  Ct 0
""",
    thermo = 'Ct-Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 21,
    label = "Ct-H",
    group = 
"""
1  *  Ct 0 {2,S}
2     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([5.28,5.99,6.49,6.87,7.47,7.96,8.85],"cal/(mol*K)","+|-",0.07),
        H298 = (26.93,"kcal/mol","+|-",0.05),
        S298 = (24.7,"cal/(mol*K)","+|-",0.07),
    ),
    shortDesc = u"""Ct-H STEIN and FAHR; J. PHYS. CHEM. 1985, 89, 17, 3714""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 22,
    label = "Ct-Os",
    group = 
"""
1  *  Ct 0 {2,S}
2     Os 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.64,4.39,4.85,5.63,5.66,5.73,5.73],"cal/(mol*K)","+|-",0.1),
        H298 = (31.4,"kcal/mol","+|-",0.27),
        S298 = (4.91,"cal/(mol*K)","+|-",0.09),
    ),
    shortDesc = u"""Ct-O MELIUS / hc#coh !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 23,
    label = "Ct-C",
    group = 
"""
1  *  Ct 0 {2,S}
2     C 0 {1,S}
""",
    thermo = 'Ct-Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 24,
    label = "Ct-Cs",
    group = 
"""
1  *  Ct 0 {2,S}
2     Cs 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.13,3.48,3.81,4.09,4.6,4.92,6.35],"cal/(mol*K)","+|-",0.1),
        H298 = (27.55,"kcal/mol","+|-",0.27),
        S298 = (6.35,"cal/(mol*K)","+|-",0.09),
    ),
    shortDesc = u"""Ct-Cs STEIN and FAHR; J. PHYS. CHEM. 1985, 89, 17, 3714""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 25,
    label = "Ct-Cds",
    group = 
"""
1  *  Ct 0 {2,S}
2     {Cd,CO} 0 {1,S}
""",
    thermo = 'Ct-(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 26,
    label = "Ct-(Cds-Od)",
    group = 
"""
1  *  Ct 0 {2,S}
2     CO 0 {1,S}
""",
    thermo = 'Ct-Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 27,
    label = "Ct-(Cds-Cd)",
    group = 
"""
1  *  Ct 0 {2,S}
2     Cd 0 {1,S}
""",
    thermo = 'Ct-(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 28,
    label = "Ct-(Cds-Cds)",
    group = 
"""
1  *  Ct 0 {2,S}
2     Cd 0 {1,S} {3,D}
3     Cd 0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([2.57,3.54,3.5,4.92,5.34,5.5,5.8],"cal/(mol*K)","+|-",0.1),
        H298 = (28.2,"kcal/mol","+|-",0.27),
        S298 = (6.43,"cal/(mol*K)","+|-",0.09),
    ),
    shortDesc = u"""Ct-Cd STEIN and FAHR; J. PHYS. CHEM. 1985, 89, 17, 3714""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 29,
    label = "Ct-(Cds-Cdd)",
    group = 
"""
1  *  Ct 0 {2,S}
2     Cd 0 {1,S} {3,D}
3     Cdd 0 {2,D}
""",
    thermo = 'Ct-(Cds-Cdd-Cd)',
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
    label = "Ct-(Cds-Cdd-Od)",
    group = 
"""
1  *  Ct 0 {2,S}
2     Cd 0 {1,S} {3,D}
3     Cdd 0 {2,D} {4,D}
4     Od 0 {3,D}
""",
    thermo = 'Ct-(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 31,
    label = "Ct-(Cds-Cdd-Cd)",
    group = 
"""
1  *  Ct 0 {2,S}
2     Cd 0 {1,S} {3,D}
3     Cdd 0 {2,D} {4,D}
4     C 0 {3,D}
""",
    thermo = 'Ct-(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 32,
    label = "Ct-Ct",
    group = 
"""
1  *  Ct 0 {2,S}
2     Ct 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.54,4.06,4.4,4.64,5,5.23,5.57],"cal/(mol*K)","+|-",0.1),
        H298 = (25.6,"kcal/mol","+|-",0.27),
        S298 = (5.88,"cal/(mol*K)","+|-",0.09),
    ),
    shortDesc = u"""Ct-Ct STEIN and FAHR; J. PHYS. CHEM. 1985, 89, 17, 3714""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 33,
    label = "Ct-Cb",
    group = 
"""
1  *  Ct 0 {2,S}
2     Cb 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([2.57,3.54,4.5,4.92,5.34,5.5,5.8],"cal/(mol*K)","+|-",0.1),
        H298 = (24.67,"kcal/mol","+|-",0.27),
        S298 = (6.43,"cal/(mol*K)","+|-",0.09),
    ),
    shortDesc = u"""Ct-Cb STEIN and FAHR; J. PHYS. CHEM. 1985, 89, 17, 3714""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 34,
    label = "Cdd",
    group = 
"""
1  *  Cdd 0
""",
    thermo = 'Cdd-CdsCds',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 35,
    label = "Cdd-OdOd",
    group = 
"""
1  *  Cdd 0 {2,D} {3,D}
2     Od 0 {1,D}
3     Od 0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([8.91,9.86,10.65,11.31,12.32,12.99,13.93],"cal/(mol*K)"),
        H298 = (-94.05,"kcal/mol","+|-",0.03),
        S298 = (52.46,"cal/(mol*K)","+|-",0.002),
    ),
    shortDesc = u"""CHEMKIN DATABASE: S(group) = S(CO2) + Rln(2)""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 36,
    label = "Cdd-CdOd",
    group = 
"""
1  *  Cdd 0 {2,D} {3,D}
2     C 0 {1,D}
3     Od 0 {1,D}
""",
    thermo = 'Cdd-CdsOd',
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
    label = "Cdd-CdsOd",
    group = 
"""
1  *  Cdd 0 {2,D} {3,D}
2     Cd 0 {1,D}
3     Od 0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    shortDesc = u"""O=C*=C< currently treat the adjacent C as Ck""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 38,
    label = "Cdd-CddOd",
    group = 
"""
1  *  Cdd 0 {2,D} {3,D}
2     Cdd 0 {1,D}
3     Od 0 {1,D}
""",
    thermo = 'Cdd-(Cdd-Cd)Od',
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
    label = "Cdd-(Cdd-Od)Od",
    group = 
"""
1  *  Cdd 0 {2,D} {3,D}
2     Cdd 0 {1,D} {4,D}
3     Od 0 {1,D}
4     Od 0 {2,D}
""",
    thermo = 'Cdd-CdsOd',
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
    label = "Cdd-(Cdd-Cd)Od",
    group = 
"""
1  *  Cdd 0 {2,D} {3,D}
2     Cdd 0 {1,D} {4,D}
3     Od 0 {1,D}
4     C 0 {2,D}
""",
    thermo = 'Cdd-CdsOd',
    shortDesc = u"""O=C*=C= currently not defined. Assigned same value as Ca""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 41,
    label = "Cdd-CdCd",
    group = 
"""
1  *  Cdd 0 {2,D} {3,D}
2     C 0 {1,D}
3     C 0 {1,D}
""",
    thermo = 'Cdd-CdsCds',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 42,
    label = "Cdd-CddCdd",
    group = 
"""
1  *  Cdd 0 {2,D} {3,D}
2     Cdd 0 {1,D}
3     Cdd 0 {1,D}
""",
    thermo = 'Cdd-(Cdd-Cd)(Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 43,
    label = "Cdd-(Cdd-Od)(Cdd-Od)",
    group = 
"""
1  *  Cdd 0 {2,D} {3,D}
2     Cdd 0 {1,D} {4,D}
3     Cdd 0 {1,D} {5,D}
4     Od 0 {2,D}
5     Od 0 {3,D}
""",
    thermo = 'Cdd-CdsCds',
    shortDesc = u"""O=C=C*=C=O, currently not defined. Assigned same value as Ca""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 44,
    label = "Cdd-(Cdd-Od)(Cdd-Cd)",
    group = 
"""
1  *  Cdd 0 {2,D} {3,D}
2     Cdd 0 {1,D} {4,D}
3     Cdd 0 {1,D} {5,D}
4     Od 0 {2,D}
5     C 0 {3,D}
""",
    thermo = 'Cdd-(Cdd-Od)Cds',
    shortDesc = u"""O=C=C*=C=C, currently not defined. Assigned same value as Ca""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 45,
    label = "Cdd-(Cdd-Cd)(Cdd-Cd)",
    group = 
"""
1  *  Cdd 0 {2,D} {3,D}
2     Cdd 0 {1,D} {4,D}
3     Cdd 0 {1,D} {5,D}
4     C 0 {2,D}
5     C 0 {3,D}
""",
    thermo = 'Cdd-CdsCds',
    shortDesc = u"""C=C=C*=C=C, currently not defined. Assigned same value as Ca""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 46,
    label = "Cdd-CddCds",
    group = 
"""
1  *  Cdd 0 {2,D} {3,D}
2     Cdd 0 {1,D}
3     Cd 0 {1,D}
""",
    thermo = 'Cdd-(Cdd-Cd)(Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 47,
    label = "Cdd-(Cdd-Od)Cds",
    group = 
"""
1  *  Cdd 0 {2,D} {3,D}
2     Cdd 0 {1,D} {4,D}
3     Cd 0 {1,D}
4     Od 0 {2,D}
""",
    thermo = 'Cdd-CdsCds',
    shortDesc = u"""O=C=C*=C<, currently not defined. Assigned same value as Ca """,
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 48,
    label = "Cdd-(Cdd-Cd)Cds",
    group = 
"""
1  *  Cdd 0 {2,D} {3,D}
2     Cdd 0 {1,D} {4,D}
3     Cd 0 {1,D}
4     C 0 {2,D}
""",
    thermo = 'Cdd-CdsCds',
    shortDesc = u"""C=C=C*=C<, currently not defined. Assigned same value as Ca """,
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 49,
    label = "Cdd-CdsCds",
    group = 
"""
1  *  Cdd 0 {2,D} {3,D}
2     Cd 0 {1,D}
3     Cd 0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.9,4.4,4.7,5,5.3,5.5,5.7],"cal/(mol*K)","+|-",0.1),
        H298 = (34.2,"kcal/mol","+|-",0.2),
        S298 = (6,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""Benson's Ca """,
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 50,
    label = "Cds",
    group = 
"""
1  *  {Cd,CO} 0
""",
    thermo = 'Cds-CdsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 51,
    label = "Cds-OdHH",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([8.47,9.38,10.46,11.52,13.37,14.81,14.81],"cal/(mol*K)","+|-",0.06),
        H298 = (-25.95,"kcal/mol","+|-",0.11),
        S298 = (53.68,"cal/(mol*K)","+|-",0.06),
    ),
    shortDesc = u"""CO-HH BENSON !!!WARNING! Cp1500 value taken as Cp1000, S(group) = S(CH2O) + Rln(2)""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 52,
    label = "Cds-OdOsH",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Os 0 {1,S}
4     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([7.03,7.87,8.82,9.68,11.2,12.2,12.2],"cal/(mol*K)","+|-",0.15),
        H298 = (-32.1,"kcal/mol","+|-",0.3),
        S298 = (34.9,"cal/(mol*K)","+|-",0.15),
    ),
    shortDesc = u"""CO-OH BENSON !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 53,
    label = "Cds-OdOsOs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Os 0 {1,S}
4     Os 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([5.97,6.7,7.4,8.02,8.87,9.36,9.36],"cal/(mol*K)","+|-",0.15),
        H298 = (-31.45,"kcal/mol","+|-",0.3),
        S298 = (10.78,"cal/(mol*K)","+|-",0.15),
    ),
    shortDesc = u"""CO-OO BOZZELLI 8/91, S CO/C/O, Hf PEDLEY ccoc*oocc Bsn Hf-24 !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 54,
    label = "Cds-OdCH",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     C 0 {1,S}
4     H 0 {1,S}
""",
    thermo = 'Cds-OdCsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 55,
    label = "Cds-OdCsH",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([7.03,7.87,8.82,9.68,11.2,12.2,12.2],"cal/(mol*K)","+|-",0.15),
        H298 = (-29.1,"kcal/mol","+|-",0.3),
        S298 = (34.9,"cal/(mol*K)","+|-",0.15),
    ),
    shortDesc = u"""CO-CsH BENSON !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 56,
    label = "Cds-OdCdsH",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     {Cd,CO} 0 {1,S}
4     H 0 {1,S}
""",
    thermo = 'Cds-Od(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 57,
    label = "Cds-Od(Cds-Od)H",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     CO 0 {1,S}
4     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([7.45,8.77,9.82,10.7,12.14,12.9,12.9],"cal/(mol*K)","+|-",0.15),
        H298 = (-25.3,"kcal/mol","+|-",0.3),
        S298 = (33.4,"cal/(mol*K)","+|-",0.15),
    ),
    shortDesc = u"""CO-COH Hf BENSON S,Cp =3D CO/Cs/H-del(Cd/Cd/H-Cd/Cs/H) !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 58,
    label = "Cds-Od(Cds-Cd)H",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Cd 0 {1,S}
4     H 0 {1,S}
""",
    thermo = 'Cds-Od(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 59,
    label = "Cds-Od(Cds-Cds)H",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     H 0 {1,S}
5     Cd 0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([7.45,8.77,9.82,10.7,12.14,12.9,12.9],"cal/(mol*K)","+|-",0.15),
        H298 = (-30.9,"kcal/mol","+|-",0.3),
        S298 = (33.4,"cal/(mol*K)","+|-",0.15),
    ),
    shortDesc = u"""CO-CdH Hf BOZZELLI S,Cp =3D CO/C/H-del(cd syst) !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 60,
    label = "Cds-Od(Cds-Cdd)H",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     H 0 {1,S}
5     Cdd 0 {3,D}
""",
    thermo = 'Cds-Od(Cds-Cdd-Cd)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 61,
    label = "Cds-Od(Cds-Cdd-Od)H",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     H 0 {1,S}
5     Cdd 0 {3,D} {6,D}
6     Od 0 {5,D}
""",
    thermo = 'Cds-Od(Cds-Cds)H',
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
    label = "Cds-Od(Cds-Cdd-Cd)H",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     H 0 {1,S}
5     Cdd 0 {3,D} {6,D}
6     C 0 {5,D}
""",
    thermo = 'Cds-Od(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 63,
    label = "Cds-OdCtH",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Ct 0 {1,S}
4     H 0 {1,S}
""",
    thermo = 'Cds-Od(Cds-Cds)H',
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
    label = "Cds-OdCbH",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Cb 0 {1,S}
4     H 0 {1,S}
""",
    thermo = 'Cds-Od(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 65,
    label = "Cds-OdCOs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     C 0 {1,S}
4     Os 0 {1,S}
""",
    thermo = 'Cds-OdCsOs',
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
    label = "Cds-OdCsOs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Cs 0 {1,S}
4     Os 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([6.1,6.7,7.4,8.02,8.87,9.36,9.36],"cal/(mol*K)","+|-",0.15),
        H298 = (-35.1,"kcal/mol","+|-",0.3),
        S298 = (10.04,"cal/(mol*K)","+|-",0.15),
    ),
    shortDesc = u"""CO-OCs Hf BENSON S STULL !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 67,
    label = "Cds-OdCdsOs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     {Cd,CO} 0 {1,S}
4     Os 0 {1,S}
""",
    thermo = 'Cds-Od(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 68,
    label = "Cds-Od(Cds-Od)Os",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     CO 0 {1,S}
4     Os 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([5.46,6.32,7.17,7.88,9,9.77,9.77],"cal/(mol*K)","+|-",0.15),
        H298 = (-29.3,"kcal/mol","+|-",0.3),
        S298 = (14.6,"cal/(mol*K)","+|-",0.15),
    ),
    shortDesc = u"""CO-OCO Hf,S BOZZELLI Cp BENSON !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 69,
    label = "Cds-Od(Cds-Cd)Os",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Cd 0 {1,S}
4     Os 0 {1,S}
""",
    thermo = 'Cds-Od(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 70,
    label = "Cds-Od(Cds-Cds)Os",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     Os 0 {1,S}
5     Cd 0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([5.97,6.7,7.4,8.02,8.87,9.36,9.36],"cal/(mol*K)","+|-",0.15),
        H298 = (-32.1,"kcal/mol","+|-",0.3),
        S298 = (14.78,"cal/(mol*K)","+|-",0.15),
    ),
    shortDesc = u"""CO-OCd RPS + S Coreected !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 71,
    label = "Cds-Od(Cds-Cdd)Os",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     Os 0 {1,S}
5     Cdd 0 {3,D}
""",
    thermo = 'Cds-Od(Cds-Cdd-Cd)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 72,
    label = "Cds-Od(Cds-Cdd-Od)Os",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     Os 0 {1,S}
5     Cdd 0 {3,D} {6,D}
6     Od 0 {5,D}
""",
    thermo = 'Cds-Od(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 73,
    label = "Cds-Od(Cds-Cdd-Cd)Os",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     Os 0 {1,S}
5     Cdd 0 {3,D} {6,D}
6     C 0 {5,D}
""",
    thermo = 'Cds-Od(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 74,
    label = "Cds-OdCtOs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Ct 0 {1,S}
4     Os 0 {1,S}
""",
    thermo = 'Cds-Od(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 75,
    label = "Cds-OdCbOs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Cb 0 {1,S}
4     Os 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([5.97,6.7,7.4,8.02,8.87,9.36,9.36],"cal/(mol*K)","+|-",0.15),
        H298 = (-36.6,"kcal/mol","+|-",0.3),
        S298 = (14.78,"cal/(mol*K)","+|-",0.15),
    ),
    shortDesc = u"""CO-OCb RPS + S Coreected !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 76,
    label = "Cds-OdCC",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     C 0 {1,S}
4     C 0 {1,S}
""",
    thermo = 'Cds-OdCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 77,
    label = "Cds-OdCsCs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([5.59,6.32,7.09,7.76,8.89,9.61,9.61],"cal/(mol*K)","+|-",0.15),
        H298 = (-31.4,"kcal/mol","+|-",0.3),
        S298 = (15.01,"cal/(mol*K)","+|-",0.15),
    ),
    shortDesc = u"""CO-CsCs BENSON !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 78,
    label = "Cds-OdCdsCs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     {Cd,CO} 0 {1,S}
4     Cs 0 {1,S}
""",
    thermo = 'Cds-Od(Cds-Cds)Cs',
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
    label = "Cds-Od(Cds-Od)Cs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     CO 0 {1,S}
4     Cs 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([5.46,6.32,7.17,7.88,9,9.77,9.77],"cal/(mol*K)","+|-",0.15),
        H298 = (-29.1,"kcal/mol","+|-",0.3),
        S298 = (14.6,"cal/(mol*K)","+|-",0.15),
    ),
    shortDesc = u"""CO-COCs Hf,S BOZZELLI Cp BENSON !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 80,
    label = "Cds-Od(Cds-Cd)Cs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Cd 0 {1,S}
4     Cs 0 {1,S}
""",
    thermo = 'Cds-Od(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 81,
    label = "Cds-Od(Cds-Cds)Cs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     Cs 0 {1,S}
5     Cd 0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([5.46,6.32,7.17,7.88,9,9.77,9.77],"cal/(mol*K)","+|-",0.15),
        H298 = (-30.9,"kcal/mol","+|-",0.3),
        S298 = (14.6,"cal/(mol*K)","+|-",0.15),
    ),
    shortDesc = u"""CO-CdCs Hf BENSON =3D CO/Cb/C S,Cp !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 82,
    label = "Cds-Od(Cds-Cdd)Cs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     Cs 0 {1,S}
5     Cdd 0 {3,D}
""",
    thermo = 'Cds-Od(Cds-Cdd-Cd)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 83,
    label = "Cds-Od(Cds-Cdd-Od)Cs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     Cs 0 {1,S}
5     Cdd 0 {3,D} {6,D}
6     Od 0 {5,D}
""",
    thermo = 'Cds-Od(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 84,
    label = "Cds-Od(Cds-Cdd-Cd)Cs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     Cs 0 {1,S}
5     Cdd 0 {3,D} {6,D}
6     C 0 {5,D}
""",
    thermo = 'Cds-Od(Cds-Cds)Cs',
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
    label = "Cds-OdCdsCds",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     {Cd,CO} 0 {1,S}
4     {Cd,CO} 0 {1,S}
""",
    thermo = 'Cds-Od(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 86,
    label = "Cds-Od(Cds-Od)(Cds-Od)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     CO 0 {1,S}
4     CO 0 {1,S}
""",
    thermo = 'Cds-OdCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 87,
    label = "Cds-Od(Cds-Cd)(Cds-Od)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Cd 0 {1,S}
4     CO 0 {1,S}
""",
    thermo = 'Cds-Od(Cds-Cds)(Cds-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 88,
    label = "Cds-Od(Cds-Cds)(Cds-Od)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     CO 0 {1,S}
5     Cd 0 {3,D}
""",
    thermo = 'Cds-Od(Cds-Od)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 89,
    label = "Cds-Od(Cds-Cdd)(Cds-Od)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     CO 0 {1,S}
5     Cdd 0 {3,D}
""",
    thermo = 'Cds-Od(Cds-Cdd-Cd)(Cds-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 90,
    label = "Cds-Od(Cds-Cdd-Od)(Cds-Od)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     CO 0 {1,S}
5     Cdd 0 {3,D} {6,D}
6     Od 0 {5,D}
""",
    thermo = 'Cds-Od(Cds-Cdd-Od)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 91,
    label = "Cds-Od(Cds-Cdd-Cd)(Cds-Od)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     CO 0 {1,S}
5     Cdd 0 {3,D} {6,D}
6     C 0 {5,D}
""",
    thermo = 'Cds-Od(Cds-Cds)(Cds-Od)',
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
    label = "Cds-Od(Cds-Cd)(Cds-Cd)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Cd 0 {1,S}
4     Cd 0 {1,S}
""",
    thermo = 'Cds-Od(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 93,
    label = "Cds-Od(Cds-Cds)(Cds-Cds)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     Cd 0 {1,S} {6,D}
5     Cd 0 {3,D}
6     Cd 0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([5.46,6.32,7.17,7.88,9,9.77,9.77],"cal/(mol*K)","+|-",0.15),
        H298 = (-30.9,"kcal/mol","+|-",0.3),
        S298 = (14.6,"cal/(mol*K)","+|-",0.15),
    ),
    shortDesc = u"""CO-CdCd Estimate BOZZELLI !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 94,
    label = "Cds-Od(Cds-Cdd)(Cds-Cds)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     Cd 0 {1,S} {6,D}
5     Cdd 0 {3,D}
6     Cd 0 {4,D}
""",
    thermo = 'Cds-Od(Cds-Cdd-Cd)(Cds-Cds)',
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
    label = "Cds-Od(Cds-Cdd-Od)(Cds-Cds)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     Cd 0 {1,S} {6,D}
5     Cdd 0 {3,D} {7,D}
6     Cd 0 {4,D}
7     Od 0 {5,D}
""",
    thermo = 'Cds-Od(Cds-Cdd-Od)Cs',
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
    label = "Cds-Od(Cds-Cdd-Cd)(Cds-Cds)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     Cd 0 {1,S} {6,D}
5     Cdd 0 {3,D} {7,D}
6     Cd 0 {4,D}
7     C 0 {5,D}
""",
    thermo = 'Cds-Od(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 97,
    label = "Cds-Od(Cds-Cdd)(Cds-Cdd)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     Cd 0 {1,S} {6,D}
5     Cdd 0 {3,D}
6     Cdd 0 {4,D}
""",
    thermo = 'Cds-Od(Cds-Cdd-Cd)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 98,
    label = "Cds-Od(Cds-Cdd-Od)(Cds-Cdd-Od)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     Cd 0 {1,S} {6,D}
5     Cdd 0 {3,D} {7,D}
6     Cdd 0 {4,D} {8,D}
7     Od 0 {5,D}
8     Od 0 {6,D}
""",
    thermo = 'Cds-Od(Cds-Cds)(Cds-Cds)',
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
    label = "Cds-Od(Cds-Cdd-Cd)(Cds-Cdd-Od)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     Cd 0 {1,S} {6,D}
5     Cdd 0 {3,D} {7,D}
6     Cdd 0 {4,D} {8,D}
7     C 0 {5,D}
8     Od 0 {6,D}
""",
    thermo = 'Cds-Od(Cds-Cdd-Od)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 100,
    label = "Cds-Od(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     Cd 0 {1,S} {6,D}
5     Cdd 0 {3,D} {7,D}
6     Cdd 0 {4,D} {8,D}
7     C 0 {5,D}
8     C 0 {6,D}
""",
    thermo = 'Cds-Od(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 101,
    label = "Cds-OdCtCs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Ct 0 {1,S}
4     Cs 0 {1,S}
""",
    thermo = 'Cds-Od(Cds-Cds)Cs',
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
    label = "Cds-OdCtCds",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Ct 0 {1,S}
4     {Cd,CO} 0 {1,S}
""",
    thermo = 'Cds-OdCt(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 103,
    label = "Cds-OdCt(Cds-Od)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Ct 0 {1,S}
4     CO 0 {1,S}
""",
    thermo = 'Cds-Od(Cds-Cds)(Cds-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 104,
    label = "Cds-OdCt(Cds-Cd)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Ct 0 {1,S}
4     Cd 0 {1,S}
""",
    thermo = 'Cds-OdCt(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 105,
    label = "Cds-OdCt(Cds-Cds)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Ct 0 {1,S}
4     Cd 0 {1,S} {5,D}
5     Cd 0 {4,D}
""",
    thermo = 'Cds-Od(Cds-Cds)(Cds-Cds)',
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
    label = "Cds-OdCt(Cds-Cdd)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Ct 0 {1,S}
4     Cd 0 {1,S} {5,D}
5     Cdd 0 {4,D}
""",
    thermo = 'Cds-OdCt(Cds-Cdd-Cd)',
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
    label = "Cds-OdCt(Cds-Cdd-Od)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Ct 0 {1,S}
4     Cd 0 {1,S} {5,D}
5     Cdd 0 {4,D} {6,D}
6     Od 0 {5,D}
""",
    thermo = 'Cds-Od(Cds-Cdd-Od)(Cds-Cds)',
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
    label = "Cds-OdCt(Cds-Cdd-Cd)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Ct 0 {1,S}
4     Cd 0 {1,S} {5,D}
5     Cdd 0 {4,D} {6,D}
6     C 0 {5,D}
""",
    thermo = 'Cds-OdCt(Cds-Cds)',
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
    label = "Cds-OdCtCt",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Ct 0 {1,S}
4     Ct 0 {1,S}
""",
    thermo = 'Cds-Od(Cds-Cds)(Cds-Cds)',
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
    label = "Cds-OdCbCs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Cb 0 {1,S}
4     Cs 0 {1,S}
""",
    thermo = 'Cds-Od(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 111,
    label = "Cds-OdCbCds",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Cb 0 {1,S}
4     {Cd,CO} 0 {1,S}
""",
    thermo = 'Cds-OdCb(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 112,
    label = "Cds-OdCb(Cds-Od)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Cb 0 {1,S}
4     CO 0 {1,S}
""",
    thermo = 'Cds-Od(Cds-Cds)(Cds-Od)',
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
    label = "Cds-OdCb(Cds-Cd)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Cb 0 {1,S}
4     Cd 0 {1,S}
""",
    thermo = 'Cds-OdCb(Cds-Cds)',
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
    label = "Cds-OdCb(Cds-Cds)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Cb 0 {1,S}
4     Cd 0 {1,S} {5,D}
5     Cd 0 {4,D}
""",
    thermo = 'Cds-Od(Cds-Cds)(Cds-Cds)',
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
    label = "Cds-OdCb(Cds-Cdd)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Cb 0 {1,S}
4     Cd 0 {1,S} {5,D}
5     Cdd 0 {4,D}
""",
    thermo = 'Cds-OdCb(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 116,
    label = "Cds-OdCb(Cds-Cdd-Od)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Cb 0 {1,S}
4     Cd 0 {1,S} {5,D}
5     Cdd 0 {4,D} {6,D}
6     Od 0 {5,D}
""",
    thermo = 'Cds-Od(Cds-Cdd-Od)(Cds-Cds)',
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
    label = "Cds-OdCb(Cds-Cdd-Cd)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Cb 0 {1,S}
4     Cd 0 {1,S} {5,D}
5     Cdd 0 {4,D} {6,D}
6     C 0 {5,D}
""",
    thermo = 'Cds-OdCb(Cds-Cds)',
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
    label = "Cds-OdCbCt",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Cb 0 {1,S}
4     Ct 0 {1,S}
""",
    thermo = 'Cds-OdCt(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 119,
    label = "Cds-OdCbCb",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Od 0 {1,D}
3     Cb 0 {1,S}
4     Cb 0 {1,S}
""",
    thermo = 'Cds-Od(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 120,
    label = "Cds-CdHH",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    thermo = 'Cds-CdsHH',
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
    label = "Cds-CdsHH",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([5.1,6.36,7.51,8.5,10.07,11.27,13.19],"cal/(mol*K)","+|-",0.07),
        H298 = (6.26,"kcal/mol","+|-",0.19),
        S298 = (27.61,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""Cd-HH BENSON""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 122,
    label = "Cds-CddHH",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    thermo = 'Cds-(Cdd-Cd)HH',
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
    label = "Cds-(Cdd-Od)HH",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     H 0 {1,S}
4     H 0 {1,S}
5     Od 0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([12.08,13.91,15.4,16.64,18.61,20.1,22.47],"cal/(mol*K)","+|-",0.07),
        H298 = (-11.34,"kcal/mol","+|-",0.19),
        S298 = (57.47,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""{CCO/H2} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 124,
    label = "Cds-(Cdd-Cd)HH",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     H 0 {1,S}
4     H 0 {1,S}
5     C 0 {2,D}
""",
    thermo = 'Cds-CdsHH',
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
    label = "Cds-CdOsH",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3     Os 0 {1,S}
4     H 0 {1,S}
""",
    thermo = 'Cds-CdsOsH',
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
    label = "Cds-CdsOsH",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Os 0 {1,S}
4     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.75,6.46,7.64,8.35,9.1,9.56,10.46],"cal/(mol*K)","+|-",0.07),
        H298 = (2.03,"kcal/mol","+|-",0.19),
        S298 = (6.2,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""Cd-OH BOZZELLI Hf vin-oh RADOM + C/Cd/H, S&Cp LAY""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 127,
    label = "Cds-CddOsH",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D}
3     Os 0 {1,S}
4     H 0 {1,S}
""",
    thermo = 'Cds-(Cdd-Cd)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 128,
    label = "Cds-(Cdd-Od)OsH",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Os 0 {1,S}
4     H 0 {1,S}
5     Od 0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([11.29,13.67,15.1,16.1,17.36,18.25,19.75],"cal/(mol*K)","+|-",0.07),
        H298 = (2.11,"kcal/mol","+|-",0.19),
        S298 = (38.17,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""{CCO/O/H} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 129,
    label = "Cds-(Cdd-Cd)OsH",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Os 0 {1,S}
4     H 0 {1,S}
5     C 0 {2,D}
""",
    thermo = 'Cds-CdsOsH',
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
    label = "Cds-CdOsOs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3     Os 0 {1,S}
4     Os 0 {1,S}
""",
    thermo = 'Cds-CdsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 131,
    label = "Cds-CdsOsOs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Os 0 {1,S}
4     Os 0 {1,S}
""",
    thermo = 'Cds-CdsCsCs',
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
    label = "Cds-CddOsOs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D}
3     Os 0 {1,S}
4     Os 0 {1,S}
""",
    thermo = 'Cds-(Cdd-Cd)OsOs',
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
    label = "Cds-(Cdd-Od)OsOs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Os 0 {1,S}
4     Os 0 {1,S}
5     Od 0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([11.56,15.58,17.69,18.67,18.78,18.4,18.01],"cal/(mol*K)","+|-",0.07),
        H298 = (2.403,"kcal/mol","+|-",0.19),
        S298 = (13.42,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""{CCO/O2} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 134,
    label = "Cds-(Cdd-Cd)OsOs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Os 0 {1,S}
4     Os 0 {1,S}
5     C 0 {2,D}
""",
    thermo = 'Cds-CdsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 135,
    label = "Cds-CdCH",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3     C 0 {1,S}
4     H 0 {1,S}
""",
    thermo = 'Cds-CdsCsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 136,
    label = "Cds-CdsCsH",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.16,5.03,5.81,6.5,7.65,8.45,9.62],"cal/(mol*K)","+|-",0.06),
        H298 = (8.59,"kcal/mol","+|-",0.17),
        S298 = (7.97,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""Cd-CsH BENSON""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 137,
    label = "Cds-CdsCdsH",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     {Cd,CO} 0 {1,S}
4     H 0 {1,S}
""",
    thermo = 'Cds-Cds(Cds-Cds)H',
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
    label = "Cds-Cds(Cds-Od)H",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     CO 0 {1,S}
4     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.46,5.79,6.75,7.42,8.35,9.11,10.09],"cal/(mol*K)","+|-",0.1),
        H298 = (4.32,"kcal/mol","+|-",0.2),
        S298 = (6.38,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""Cd-COH BOZZELLI lit rev Jul91 S,Cp Cd/Cd/H""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 139,
    label = "Cds-Cds(Cds-Cd)H",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Cd 0 {1,S}
4     H 0 {1,S}
""",
    thermo = 'Cds-Cds(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 140,
    label = "Cds-Cds(Cds-Cds)H",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     H 0 {1,S}
5     Cd 0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.46,5.79,6.75,7.42,8.35,8.99,9.98],"cal/(mol*K)","+|-",0.1),
        H298 = (6.78,"kcal/mol","+|-",0.2),
        S298 = (6.38,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""Cd-CdH BENSON""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 141,
    label = "Cds-Cds(Cds-Cdd)H",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     H 0 {1,S}
5     Cdd 0 {3,D}
""",
    thermo = 'Cds-Cds(Cds-Cdd-Cd)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 142,
    label = "Cds-Cds(Cds-Cdd-Od)H",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     H 0 {1,S}
5     Cdd 0 {3,D} {6,D}
6     Od 0 {5,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 143,
    label = "Cds-Cds(Cds-Cdd-Cd)H",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     H 0 {1,S}
5     Cdd 0 {3,D} {6,D}
6     C 0 {5,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 144,
    label = "Cds-CdsCtH",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Ct 0 {1,S}
4     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.46,5.79,6.75,7.42,8.35,8.99,9.98],"cal/(mol*K)","+|-",0.1),
        H298 = (6.78,"kcal/mol","+|-",0.2),
        S298 = (6.38,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""Cd-CtH BENSON""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 145,
    label = "Cds-CdsCbH",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Cb 0 {1,S}
4     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.46,5.79,6.75,7.42,8.35,8.99,9.98],"cal/(mol*K)","+|-",0.1),
        H298 = (6.78,"kcal/mol","+|-",0.2),
        S298 = (6.38,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""Cd-CbH BENSON""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 146,
    label = "Cds-CddCsH",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    thermo = 'Cds-(Cdd-Cd)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 147,
    label = "Cds-(Cdd-Od)CsH",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cs 0 {1,S}
4     H 0 {1,S}
5     Od 0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([10.31,11.72,12.94,13.98,15.71,16.95,18.78],"cal/(mol*K)","+|-",0.1),
        H298 = (-4.947,"kcal/mol","+|-",0.2),
        S298 = (40.04,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""{CCO/H/C} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 148,
    label = "Cds-(Cdd-Cd)CsH",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cs 0 {1,S}
4     H 0 {1,S}
5     C 0 {2,D}
""",
    thermo = 'Cds-CdsCsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 149,
    label = "Cds-CddCdsH",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D}
3     {Cd,CO} 0 {1,S}
4     H 0 {1,S}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 150,
    label = "Cds-(Cdd-Od)(Cds-Od)H",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     CO 0 {1,S}
4     H 0 {1,S}
5     Od 0 {2,D}
""",
    thermo = 'Cds-(Cdd-Od)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 151,
    label = "Cds-(Cdd-Od)(Cds-Cd)H",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S}
4     H 0 {1,S}
5     Od 0 {2,D}
""",
    thermo = 'Cds-(Cdd-Od)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 152,
    label = "Cds-(Cdd-Od)(Cds-Cds)H",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     H 0 {1,S}
5     Od 0 {2,D}
6     Cd 0 {3,D}
""",
    thermo = 'Cds-(Cdd-Od)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 153,
    label = "Cds-(Cdd-Od)(Cds-Cdd)H",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     H 0 {1,S}
5     Od 0 {2,D}
6     Cdd 0 {3,D}
""",
    thermo = 'Cds-(Cdd-Od)(Cds-Cdd-Cd)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 154,
    label = "Cds-(Cdd-Od)(Cds-Cdd-Od)H",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     H 0 {1,S}
5     Od 0 {2,D}
6     Cdd 0 {3,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([10.55,12.41,13.82,14.91,16.51,17.62,19.24],"cal/(mol*K)","+|-",0.1),
        H298 = (-4.998,"kcal/mol","+|-",0.2),
        S298 = (39.06,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""{CCO/H/CCO} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 155,
    label = "Cds-(Cdd-Od)(Cds-Cdd-Cd)H",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     H 0 {1,S}
5     Od 0 {2,D}
6     Cdd 0 {3,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cds-(Cdd-Od)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 156,
    label = "Cds-(Cdd-Cd)(Cds-Od)H",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     CO 0 {1,S}
4     H 0 {1,S}
5     C 0 {2,D}
""",
    thermo = 'Cds-Cds(Cds-Od)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 157,
    label = "Cds-(Cdd-Cd)(Cds-Cd)H",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S}
4     H 0 {1,S}
5     C 0 {2,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 158,
    label = "Cds-(Cdd-Cd)(Cds-Cds)H",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     H 0 {1,S}
5     C 0 {2,D}
6     Cd 0 {3,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 159,
    label = "Cds-(Cdd-Cd)(Cds-Cdd)H",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     H 0 {1,S}
5     C 0 {2,D}
6     Cdd 0 {3,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cdd-Cd)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 160,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-Od)H",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     H 0 {1,S}
5     C 0 {2,D}
6     Cdd 0 {3,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cds-Cds(Cds-Cdd-Od)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 161,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-Cd)H",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     H 0 {1,S}
5     C 0 {2,D}
6     Cdd 0 {3,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 162,
    label = "Cds-CddCtH",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D}
3     Ct 0 {1,S}
4     H 0 {1,S}
""",
    thermo = 'Cds-(Cdd-Cd)CtH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 163,
    label = "Cds-(Cdd-Od)CtH",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Ct 0 {1,S}
4     H 0 {1,S}
5     Od 0 {2,D}
""",
    thermo = 'Cds-(Cdd-Od)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 164,
    label = "Cds-(Cdd-Cd)CtH",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Ct 0 {1,S}
4     H 0 {1,S}
5     C 0 {2,D}
""",
    thermo = 'Cds-CdsCtH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 165,
    label = "Cds-CddCbH",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D}
3     Cb 0 {1,S}
4     H 0 {1,S}
""",
    thermo = 'Cds-(Cdd-Cd)CbH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 166,
    label = "Cds-(Cdd-Od)CbH",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cb 0 {1,S}
4     H 0 {1,S}
5     Od 0 {2,D}
""",
    thermo = 'Cds-(Cdd-Od)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 167,
    label = "Cds-(Cdd-Cd)CbH",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cb 0 {1,S}
4     H 0 {1,S}
5     C 0 {2,D}
""",
    thermo = 'Cds-CdsCbH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 168,
    label = "Cds-CdCO",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3     C 0 {1,S}
4     O 0 {1,S}
""",
    thermo = 'Cds-CdsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 169,
    label = "Cds-CdsCsOs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Cs 0 {1,S}
4     Os 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.59,4.56,5.04,5.3,5.84,6.07,6.16],"cal/(mol*K)","+|-",0.1),
        H298 = (3.03,"kcal/mol","+|-",0.2),
        S298 = (-12.32,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""Cd-OCs BOZZELLI-RADOM vin-oh and del (ccoh-ccohc)""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 170,
    label = "Cds-CdsCdsOs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     {Cd,CO} 0 {1,S}
4     Os 0 {1,S}
""",
    thermo = 'Cds-Cds(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 171,
    label = "Cds-Cds(Cds-Od)Os",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     CO 0 {1,S}
4     Os 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.4,5.37,5.93,6.18,6.5,6.62,6.72],"cal/(mol*K)","+|-",0.1),
        H298 = (5.13,"kcal/mol","+|-",0.2),
        S298 = (-14.6,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""Cd-OCO adj BENSON for RADOM c*coh""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 172,
    label = "Cds-Cds(Cds-Cd)Os",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Cd 0 {1,S}
4     Os 0 {1,S}
""",
    thermo = 'Cds-Cds(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 173,
    label = "Cds-Cds(Cds-Cds)Os",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     Os 0 {1,S}
5     Cd 0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.4,5.37,5.93,6.18,6.5,6.62,6.72],"cal/(mol*K)","+|-",0.1),
        H298 = (1.5,"kcal/mol","+|-",0.2),
        S298 = (-14.4,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""Cd-OCd jwb need calc""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 174,
    label = "Cds-Cds(Cds-Cdd)Os",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     Os 0 {1,S}
5     Cdd 0 {3,D}
""",
    thermo = 'Cds-Cds(Cds-Cdd-Cd)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 175,
    label = "Cds-Cds(Cds-Cdd-Od)Os",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     Os 0 {1,S}
5     Cdd 0 {3,D} {6,D}
6     Od 0 {5,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 176,
    label = "Cds-Cds(Cds-Cdd-Cd)Os",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     Os 0 {1,S}
5     Cdd 0 {3,D} {6,D}
6     C 0 {5,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 177,
    label = "Cds-CdsCtOs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Ct 0 {1,S}
4     Os 0 {1,S}
""",
    thermo = 'Cds-Cds(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 178,
    label = "Cds-CdsCbOs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Cb 0 {1,S}
4     Os 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.4,5.37,5.93,6.18,6.5,6.62,6.72],"cal/(mol*K)","+|-",0.1),
        H298 = (1.5,"kcal/mol","+|-",0.2),
        S298 = (-14.4,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""Cd-OCb jwb need calc""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 179,
    label = "Cds-CddCsOs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D}
3     Cs 0 {1,S}
4     Os 0 {1,S}
""",
    thermo = 'Cds-(Cdd-Cd)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 180,
    label = "Cds-(Cdd-Od)CsOs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cs 0 {1,S}
4     Os 0 {1,S}
5     Od 0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([10.91,12.65,13.59,14.22,15,15.48,16.28],"cal/(mol*K)","+|-",0.1),
        H298 = (3.273,"kcal/mol","+|-",0.2),
        S298 = (18.58,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""{CCO/O/C} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 181,
    label = "Cds-(Cdd-Cd)CsOs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cs 0 {1,S}
4     Os 0 {1,S}
5     C 0 {2,D}
""",
    thermo = 'Cds-CdsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 182,
    label = "Cds-CddCdsOs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D}
3     {Cd,CO} 0 {1,S}
4     Os 0 {1,S}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 183,
    label = "Cds-(Cdd-Od)(Cds-Od)Os",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     CO 0 {1,S}
4     Os 0 {1,S}
5     Od 0 {2,D}
""",
    thermo = 'Cds-(Cdd-Od)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 184,
    label = "Cds-(Cdd-Od)(Cds-Cd)Os",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S}
4     Os 0 {1,S}
5     Od 0 {2,D}
""",
    thermo = 'Cds-(Cdd-Od)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 185,
    label = "Cds-(Cdd-Od)(Cds-Cds)Os",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Os 0 {1,S}
5     Od 0 {2,D}
6     Cd 0 {3,D}
""",
    thermo = 'Cds-(Cdd-Od)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 186,
    label = "Cds-(Cdd-Od)(Cds-Cdd)Os",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Os 0 {1,S}
5     Od 0 {2,D}
6     Cdd 0 {3,D}
""",
    thermo = 'Cds-(Cdd-Od)(Cds-Cdd-Cd)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 187,
    label = "Cds-(Cdd-Od)(Cds-Cdd-Od)Os",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Os 0 {1,S}
5     Od 0 {2,D}
6     Cdd 0 {3,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([11.01,12.97,14.17,14.97,15.8,16.26,16.88],"cal/(mol*K)","+|-",0.1),
        H298 = (1.607,"kcal/mol","+|-",0.2),
        S298 = (17.73,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""{CCO/O/CCO} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 188,
    label = "Cds-(Cdd-Od)(Cds-Cdd-Cd)Os",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Os 0 {1,S}
5     Od 0 {2,D}
6     Cdd 0 {3,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cds-(Cdd-Od)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 189,
    label = "Cds-(Cdd-Cd)(Cds-Cd)Os",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S}
4     Os 0 {1,S}
5     C 0 {2,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 190,
    label = "Cds-(Cdd-Cd)(Cds-Cds)Os",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Os 0 {1,S}
5     C 0 {2,D}
6     Cd 0 {3,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 191,
    label = "Cds-(Cdd-Cd)(Cds-Cdd)Os",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Os 0 {1,S}
5     C 0 {2,D}
6     Cdd 0 {3,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cdd-Cd)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 192,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-Od)Os",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Os 0 {1,S}
5     C 0 {2,D}
6     Cdd 0 {3,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cds-Cds(Cds-Cdd-Od)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 193,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-Cd)Os",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Os 0 {1,S}
5     C 0 {2,D}
6     Cdd 0 {3,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 194,
    label = "Cds-CddCtOs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D}
3     Ct 0 {1,S}
4     Os 0 {1,S}
""",
    thermo = 'Cds-(Cdd-Cd)CtOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 195,
    label = "Cds-(Cdd-Od)CtOs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Ct 0 {1,S}
4     Os 0 {1,S}
5     Od 0 {2,D}
""",
    thermo = 'Cds-(Cdd-Od)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 196,
    label = "Cds-(Cdd-Cd)CtOs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Ct 0 {1,S}
4     Os 0 {1,S}
5     C 0 {2,D}
""",
    thermo = 'Cds-CdsCtOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 197,
    label = "Cds-CddCbOs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D}
3     Cb 0 {1,S}
4     Os 0 {1,S}
""",
    thermo = 'Cds-(Cdd-Cd)CbOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 198,
    label = "Cds-(Cdd-Od)CbOs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cb 0 {1,S}
4     Os 0 {1,S}
5     Od 0 {2,D}
""",
    thermo = 'Cds-(Cdd-Od)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 199,
    label = "Cds-(Cdd-Cd)CbOs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cb 0 {1,S}
4     Os 0 {1,S}
5     C 0 {2,D}
""",
    thermo = 'Cds-CdsCbOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 200,
    label = "Cds-CdCC",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     C 0 {1,D}
3     C 0 {1,S}
4     C 0 {1,S}
""",
    thermo = 'Cds-CdsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 201,
    label = "Cds-CdsCsCs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.1,4.61,4.99,5.26,5.8,6.08,6.36],"cal/(mol*K)","+|-",0.1),
        H298 = (10.34,"kcal/mol","+|-",0.24),
        S298 = (-12.7,"cal/(mol*K)","+|-",0.12),
    ),
    shortDesc = u"""Cd-CsCs BENSON""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 202,
    label = "Cds-CdsCdsCs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     {Cd,CO} 0 {1,S}
4     Cs 0 {1,S}
""",
    thermo = 'Cds-Cds(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 203,
    label = "Cds-Cds(Cds-Od)Cs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     CO 0 {1,S}
4     Cs 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.4,5.37,5.93,6.18,6.5,6.62,6.72],"cal/(mol*K)","+|-",0.1),
        H298 = (7.5,"kcal/mol","+|-",0.24),
        S298 = (-14.6,"cal/(mol*K)","+|-",0.12),
    ),
    shortDesc = u"""Cd-COCs BENSON Hf, Cd/C/Cd =3D S,Cp""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 204,
    label = "Cds-Cds(Cds-Cd)Cs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Cd 0 {1,S}
4     Cs 0 {1,S}
""",
    thermo = 'Cds-Cds(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 205,
    label = "Cds-Cds(Cds-Cds)Cs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     Cs 0 {1,S}
5     Cd 0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.4,5.37,5.93,6.18,6.5,6.62,6.72],"cal/(mol*K)","+|-",0.1),
        H298 = (8.88,"kcal/mol","+|-",0.24),
        S298 = (-14.6,"cal/(mol*K)","+|-",0.12),
    ),
    shortDesc = u"""Cd-CdCs BENSON""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 206,
    label = "Cds-Cds(Cds-Cdd)Cs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     Cs 0 {1,S}
5     Cdd 0 {3,D}
""",
    thermo = 'Cds-Cds(Cds-Cdd-Cd)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 207,
    label = "Cds-Cds(Cds-Cdd-Od)Cs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     Cs 0 {1,S}
5     Cdd 0 {3,D} {6,D}
6     Od 0 {5,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 208,
    label = "Cds-Cds(Cds-Cdd-Cd)Cs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     Cs 0 {1,S}
5     Cdd 0 {3,D} {6,D}
6     C 0 {5,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 209,
    label = "Cds-CdsCdsCds",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     {Cd,CO} 0 {1,S}
4     {Cd,CO} 0 {1,S}
""",
    thermo = 'Cds-Cds(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 210,
    label = "Cds-Cds(Cds-Od)(Cds-Od)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     CO 0 {1,S}
4     CO 0 {1,S}
""",
    thermo = 'Cds-CdsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 211,
    label = "Cds-Cds(Cds-Od)(Cds-Cd)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     CO 0 {1,S}
4     Cd 0 {1,S}
""",
    thermo = 'Cds-Cds(Cds-Od)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 212,
    label = "Cds-Cds(Cds-Od)(Cds-Cds)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     CO 0 {1,S}
4     Cd 0 {1,S} {5,D}
5     Cd 0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.7,6.13,6.87,7.1,7.2,7.16,7.06],"cal/(mol*K)","+|-",0.1),
        H298 = (4.6,"kcal/mol","+|-",0.24),
        S298 = (-16.5,"cal/(mol*K)","+|-",0.12),
    ),
    shortDesc = u"""Cd-COCd from CD/CD2/ jwb est 6/97""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 213,
    label = "Cds-Cds(Cds-Od)(Cds-Cdd)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     CO 0 {1,S}
4     Cd 0 {1,S} {5,D}
5     Cdd 0 {4,D}
""",
    thermo = 'Cds-Cds(Cds-Od)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 214,
    label = "Cds-Cds(Cds-Od)(Cds-Cdd-Od)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     CO 0 {1,S}
4     Cd 0 {1,S} {5,D}
5     Cdd 0 {4,D} {6,D}
6     Od 0 {5,D}
""",
    thermo = 'Cds-Cds(Cds-Cdd-Od)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 215,
    label = "Cds-Cds(Cds-Od)(Cds-Cdd-Cd)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     CO 0 {1,S}
4     Cd 0 {1,S} {5,D}
5     Cdd 0 {4,D} {6,D}
6     C 0 {5,D}
""",
    thermo = 'Cds-Cds(Cds-Od)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 216,
    label = "Cds-Cds(Cds-Cd)(Cds-Cd)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Cd 0 {1,S}
4     Cd 0 {1,S}
""",
    thermo = 'Cds-Cds(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 217,
    label = "Cds-Cds(Cds-Cds)(Cds-Cds)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     Cd 0 {1,S} {6,D}
5     Cd 0 {3,D}
6     Cd 0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([1.9,2.69,3.5,4.28,5.57,6.21,7.37],"cal/(mol*K)","+|-",0.1),
        H298 = (4.6,"kcal/mol","+|-",0.24),
        S298 = (-15.67,"cal/(mol*K)","+|-",0.12),
    ),
    shortDesc = u"""Cd-CdCd Hf=3D est S,Cp mopac nov99""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 218,
    label = "Cds-Cds(Cds-Cds)(Cds-Cdd)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     Cd 0 {1,S} {6,D}
5     Cd 0 {3,D}
6     Cdd 0 {4,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 219,
    label = "Cds-Cds(Cds-Cds)(Cds-Cdd-Od)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     Cd 0 {1,S} {6,D}
5     Cd 0 {3,D}
6     Cdd 0 {4,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cds-Cds(Cds-Cdd-Od)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 220,
    label = "Cds-Cds(Cds-Cds)(Cds-Cdd-Cd)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     Cd 0 {1,S} {6,D}
5     Cd 0 {3,D}
6     Cdd 0 {4,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 221,
    label = "Cds-Cds(Cds-Cdd)(Cds-Cdd)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     Cd 0 {1,S} {6,D}
5     Cdd 0 {3,D}
6     Cdd 0 {4,D}
""",
    thermo = 'Cds-Cds(Cds-Cdd-Cd)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 222,
    label = "Cds-Cds(Cds-Cdd-Od)(Cds-Cdd-Od)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     Cd 0 {1,S} {6,D}
5     Cdd 0 {3,D} {7,D}
6     Cdd 0 {4,D} {8,D}
7     Od 0 {5,D}
8     Od 0 {6,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 223,
    label = "Cds-Cds(Cds-Cdd-Od)(Cds-Cdd-Cd)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     Cd 0 {1,S} {6,D}
5     Cdd 0 {3,D} {7,D}
6     Cdd 0 {4,D} {8,D}
7     Od 0 {5,D}
8     C 0 {6,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 224,
    label = "Cds-Cds(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     Cd 0 {1,S} {6,D}
5     Cdd 0 {3,D} {7,D}
6     Cdd 0 {4,D} {8,D}
7     C 0 {5,D}
8     C 0 {6,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 225,
    label = "Cds-CdsCtCs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Ct 0 {1,S}
4     Cs 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.5,3.88,4.88,4.18,4.86,5.4,6.01],"cal/(mol*K)","+|-",0.1),
        H298 = (8.11,"kcal/mol","+|-",0.24),
        S298 = (-13.02,"cal/(mol*K)","+|-",0.12),
    ),
    shortDesc = u"""Cd-CtCs RAMAN & GREEN JPCA 2002, 106, 11141-11149""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 226,
    label = "Cds-CdsCtCds",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Ct 0 {1,S}
4     {Cd,CO} 0 {1,S}
""",
    thermo = 'Cds-Cds(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 227,
    label = "Cds-CdsCt(Cds-Od)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Ct 0 {1,S}
4     CO 0 {1,S}
""",
    thermo = 'Cds-Cds(Cds-Od)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 228,
    label = "Cds-CdsCt(Cds-Cd)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Ct 0 {1,S}
4     Cd 0 {1,S}
""",
    thermo = 'Cds-Cds(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 229,
    label = "Cds-Cds(Cds-Cds)Ct",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     Ct 0 {1,S}
5     Cd 0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.89,5.26,5.98,6.37,6.67,6.78,6.89],"cal/(mol*K)","+|-",0.1),
        H298 = (7.54,"kcal/mol","+|-",0.24),
        S298 = (-14.65,"cal/(mol*K)","+|-",0.12),
    ),
    shortDesc = u"""Cd-CtCd RAMAN & GREEN JPCA 2002, 106, 11141-11149""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 230,
    label = "Cds-Cds(Cds-Cdd)Ct",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     Ct 0 {1,S}
5     Cdd 0 {3,D}
""",
    thermo = 'Cds-Cds(Cds-Cdd-Cd)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 231,
    label = "Cds-Cds(Cds-Cdd-Od)Ct",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     Ct 0 {1,S}
5     Cdd 0 {3,D} {6,D}
6     Od 0 {5,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 232,
    label = "Cds-Cds(Cds-Cdd-Cd)Ct",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     Ct 0 {1,S}
5     Cdd 0 {3,D} {6,D}
6     C 0 {5,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 233,
    label = "Cds-CdsCtCt",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Ct 0 {1,S}
4     Ct 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.23,4.59,5.41,5.93,6.48,6.74,7.02],"cal/(mol*K)","+|-",0.1),
        H298 = (8.81,"kcal/mol","+|-",0.24),
        S298 = (-13.51,"cal/(mol*K)","+|-",0.12),
    ),
    shortDesc = u"""Cd-CtCt RAMAN & GREEN JPCA 2002, 106, 11141-11149""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 234,
    label = "Cds-CdsCbCs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Cb 0 {1,S}
4     Cs 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.4,5.37,5.93,6.18,6.5,6.62,6.72],"cal/(mol*K)","+|-",0.1),
        H298 = (8.64,"kcal/mol","+|-",0.24),
        S298 = (-14.6,"cal/(mol*K)","+|-",0.12),
    ),
    shortDesc = u"""Cd-CbCs BENSON""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 235,
    label = "Cds-CdsCbCds",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Cb 0 {1,S}
4     {Cd,CO} 0 {1,S}
""",
    thermo = 'Cds-Cds(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 236,
    label = "Cds-CdsCb(Cds-Od)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Cb 0 {1,S}
4     CO 0 {1,S}
""",
    thermo = 'Cds-Cds(Cds-Od)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 237,
    label = "Cds-Cds(Cds-Cd)Cb",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Cd 0 {1,S}
4     Cb 0 {1,S}
""",
    thermo = 'Cds-Cds(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 238,
    label = "Cds-Cds(Cds-Cds)Cb",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     Cb 0 {1,S}
5     Cd 0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.7,6.13,6.87,7.1,7.2,7.16,7.06],"cal/(mol*K)","+|-",0.1),
        H298 = (7.18,"kcal/mol","+|-",0.24),
        S298 = (-16.5,"cal/(mol*K)","+|-",0.12),
    ),
    shortDesc = u"""Cd-CbCd BOZZELLI =3D Cd/Cs/Cb + (Cd/Cs/Cd - Cd/Cs/Cs)""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 239,
    label = "Cds-Cds(Cds-Cdd)Cb",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     Cb 0 {1,S}
5     Cdd 0 {3,D}
""",
    thermo = 'Cds-Cds(Cds-Cdd-Cd)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 240,
    label = "Cds-Cds(Cds-Cdd-Od)Cb",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     Cb 0 {1,S}
5     Cdd 0 {3,D} {6,D}
6     Od 0 {5,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 241,
    label = "Cds-Cds(Cds-Cdd-Cd)Cb",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Cd 0 {1,S} {5,D}
4     Cb 0 {1,S}
5     Cdd 0 {3,D} {6,D}
6     C 0 {5,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 242,
    label = "Cds-CdsCbCt",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Cb 0 {1,S}
4     Ct 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([2.22,3.14,4.54,4.11,5.06,5.79,6.71],"cal/(mol*K)","+|-",0.1),
        H298 = (6.7,"kcal/mol","+|-",0.24),
        S298 = (-17.04,"cal/(mol*K)","+|-",0.12),
    ),
    shortDesc = u"""Cd-CbCt Hf=3D est S,Cp mopac nov99""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 243,
    label = "Cds-CdsCbCb",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cd 0 {1,D}
3     Cb 0 {1,S}
4     Cb 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.7,6.13,6.87,7.1,7.2,7.16,7.06],"cal/(mol*K)","+|-",0.1),
        H298 = (8,"kcal/mol","+|-",0.24),
        S298 = (-16.5,"cal/(mol*K)","+|-",0.12),
    ),
    shortDesc = u"""Cd-CbCb BOZZELLI =3D Cd/Cs/Cb + (Cd/Cs/Cb - Cd/Cs/Cs)""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 244,
    label = "Cds-CddCsCs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    thermo = 'Cds-(Cdd-Cd)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 245,
    label = "Cds-(Cdd-Od)CsCs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Od 0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([9.82,10.74,11.53,13.22,13.46,14.28,15.35],"cal/(mol*K)","+|-",0.1),
        H298 = (-1.644,"kcal/mol","+|-",0.24),
        S298 = (20.02,"cal/(mol*K)","+|-",0.12),
    ),
    shortDesc = u"""{CCO/C2} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 246,
    label = "Cds-(Cdd-Cd)CsCs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     C 0 {2,D}
""",
    thermo = 'Cds-CdsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 247,
    label = "Cds-CddCdsCs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D}
3     {Cd,CO} 0 {1,S}
4     Cs 0 {1,S}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 248,
    label = "Cds-(Cdd-Od)(Cds-Od)Cs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     CO 0 {1,S}
4     Cs 0 {1,S}
5     Od 0 {2,D}
""",
    thermo = 'Cds-(Cdd-Od)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 249,
    label = "Cds-(Cdd-Od)(Cds-Cd)Cs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S}
4     Cs 0 {1,S}
5     Od 0 {2,D}
""",
    thermo = 'Cds-(Cdd-Od)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 250,
    label = "Cds-(Cdd-Od)(Cds-Cds)Cs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Cs 0 {1,S}
5     Od 0 {2,D}
6     Cd 0 {3,D}
""",
    thermo = 'Cds-(Cdd-Od)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 251,
    label = "Cds-(Cdd-Od)(Cds-Cdd)Cs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Cs 0 {1,S}
5     Od 0 {2,D}
6     Cdd 0 {3,D}
""",
    thermo = 'Cds-(Cdd-Od)(Cds-Cdd-Cd)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 252,
    label = "Cds-(Cdd-Od)(Cds-Cdd-Od)Cs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Cs 0 {1,S}
5     Od 0 {2,D}
6     Cdd 0 {3,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([10.1,11.24,12.12,12.84,14,14.75,15.72],"cal/(mol*K)","+|-",0.1),
        H298 = (-2.07,"kcal/mol","+|-",0.24),
        S298 = (19.65,"cal/(mol*K)","+|-",0.12),
    ),
    shortDesc = u"""{CCO/C/CCO} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 253,
    label = "Cds-(Cdd-Od)(Cds-Cdd-Cd)Cs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Cs 0 {1,S}
5     Od 0 {2,D}
6     Cdd 0 {3,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cds-(Cdd-Od)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 254,
    label = "Cds-(Cdd-Cd)(Cds-Cd)Cs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S}
4     Cs 0 {1,S}
5     C 0 {2,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 255,
    label = "Cds-(Cdd-Cd)(Cds-Cds)Cs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Cs 0 {1,S}
5     C 0 {2,D}
6     Cd 0 {3,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 256,
    label = "Cds-(Cdd-Cd)(Cds-Cdd)Cs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Cs 0 {1,S}
5     C 0 {2,D}
6     Cdd 0 {3,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cdd-Cd)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 257,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-Od)Cs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Cs 0 {1,S}
5     C 0 {2,D}
6     Cdd 0 {3,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cds-Cds(Cds-Cdd-Od)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 258,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-Cd)Cs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Cs 0 {1,S}
5     C 0 {2,D}
6     Cdd 0 {3,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 259,
    label = "Cds-CddCdsCds",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D}
3     {Cd,CO} 0 {1,S}
4     {Cd,CO} 0 {1,S}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 260,
    label = "Cds-(Cdd-Od)(Cds-Od)(Cds-Od)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     CO 0 {1,S}
4     CO 0 {1,S}
5     Od 0 {2,D}
""",
    thermo = 'Cds-(Cdd-Od)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 261,
    label = "Cds-(Cdd-Od)(Cds-Cd)(Cds-Od)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S}
4     CO 0 {1,S}
5     Od 0 {2,D}
""",
    thermo = 'Cds-(Cdd-Od)(Cds-Cds)(Cds-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 262,
    label = "Cds-(Cdd-Od)(Cds-Cds)(Cds-Od)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     CO 0 {1,S}
5     Od 0 {2,D}
6     Cd 0 {3,D}
""",
    thermo = 'Cds-(Cdd-Od)(Cds-Od)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 263,
    label = "Cds-(Cdd-Od)(Cds-Cdd)(Cds-Od)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     CO 0 {1,S}
5     Od 0 {2,D}
6     Cdd 0 {3,D}
""",
    thermo = 'Cds-(Cdd-Od)(Cds-Cdd-Cd)(Cds-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 264,
    label = "Cds-(Cdd-Od)(Cds-Cdd-Od)(Cds-Od)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     CO 0 {1,S}
5     Od 0 {2,D}
6     Cdd 0 {3,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cds-(Cdd-Od)(Cds-Cdd-Od)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 265,
    label = "Cds-(Cdd-Od)(Cds-Cdd-Cd)(Cds-Od)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     CO 0 {1,S}
5     Od 0 {2,D}
6     Cdd 0 {3,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cds-(Cdd-Od)(Cds-Cds)(Cds-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 266,
    label = "Cds-(Cdd-Od)(Cds-Cd)(Cds-Cd)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S}
4     Cd 0 {1,S}
5     Od 0 {2,D}
""",
    thermo = 'Cds-(Cdd-Od)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 267,
    label = "Cds-(Cdd-Od)(Cds-Cds)(Cds-Cds)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Od 0 {2,D}
6     Cd 0 {3,D}
7     Cd 0 {4,D}
""",
    thermo = 'Cds-(Cdd-Od)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 268,
    label = "Cds-(Cdd-Od)(Cds-Cdd)(Cds-Cds)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Od 0 {2,D}
6     Cdd 0 {3,D}
7     Cd 0 {4,D}
""",
    thermo = 'Cds-(Cdd-Od)(Cds-Cdd-Cd)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 269,
    label = "Cds-(Cdd-Od)(Cds-Cdd-Od)(Cds-Cds)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Od 0 {2,D}
6     Cdd 0 {3,D} {8,D}
7     Cd 0 {4,D}
8     Od 0 {6,D}
""",
    thermo = 'Cds-(Cdd-Od)(Cds-Cdd-Od)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 270,
    label = "Cds-(Cdd-Od)(Cds-Cdd-Cd)(Cds-Cds)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Od 0 {2,D}
6     Cdd 0 {3,D} {8,D}
7     Cd 0 {4,D}
8     C 0 {6,D}
""",
    thermo = 'Cds-(Cdd-Od)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 271,
    label = "Cds-(Cdd-Od)(Cds-Cdd)(Cds-Cdd)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Od 0 {2,D}
6     Cdd 0 {3,D}
7     Cdd 0 {4,D}
""",
    thermo = 'Cds-(Cdd-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 272,
    label = "Cds-(Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Od 0 {2,D}
6     Cdd 0 {3,D} {8,D}
7     Cdd 0 {4,D} {9,D}
8     Od 0 {6,D}
9     Od 0 {7,D}
""",
    thermo = 'Cds-(Cdd-Od)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 273,
    label = "Cds-(Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Od 0 {2,D}
6     Cdd 0 {3,D} {8,D}
7     Cdd 0 {4,D} {9,D}
8     Od 0 {6,D}
9     C 0 {7,D}
""",
    thermo = 'Cds-(Cdd-Od)(Cds-Cdd-Od)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 274,
    label = "Cds-(Cdd-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Od 0 {2,D}
6     Cdd 0 {3,D} {8,D}
7     Cdd 0 {4,D} {9,D}
8     C 0 {6,D}
9     C 0 {7,D}
""",
    thermo = 'Cds-(Cdd-Od)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 275,
    label = "Cds-(Cdd-Cd)(Cds-Od)(Cds-Od)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     CO 0 {1,S}
4     CO 0 {1,S}
5     C 0 {2,D}
""",
    thermo = 'Cds-Cds(Cds-Od)(Cds-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 276,
    label = "Cds-(Cdd-Cd)(Cds-Od)(Cds-Cd)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     CO 0 {1,S}
4     Cd 0 {1,S}
5     C 0 {2,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Od)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 277,
    label = "Cds-(Cdd-Cd)(Cds-Od)(Cds-Cds)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     CO 0 {1,S}
4     Cd 0 {1,S} {6,D}
5     C 0 {2,D}
6     Cd 0 {4,D}
""",
    thermo = 'Cds-Cds(Cds-Od)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 278,
    label = "Cds-(Cdd-Cd)(Cds-Od)(Cds-Cdd)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     CO 0 {1,S}
4     Cd 0 {1,S} {6,D}
5     C 0 {2,D}
6     Cdd 0 {4,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Od)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 279,
    label = "Cds-(Cdd-Cd)(Cds-Od)(Cds-Cdd-Od)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     CO 0 {1,S}
4     Cd 0 {1,S} {6,D}
5     C 0 {2,D}
6     Cdd 0 {4,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cds-Cds(Cds-Od)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 280,
    label = "Cds-(Cdd-Cd)(Cds-Od)(Cds-Cdd-Cd)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     CO 0 {1,S}
4     Cd 0 {1,S} {6,D}
5     C 0 {2,D}
6     Cdd 0 {4,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Od)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 281,
    label = "Cds-(Cdd-Cd)(Cds-Cd)(Cds-Cd)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S}
4     Cd 0 {1,S}
5     C 0 {2,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 282,
    label = "Cds-(Cdd-Cd)(Cds-Cds)(Cds-Cds)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     C 0 {2,D}
6     Cd 0 {3,D}
7     Cd 0 {4,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 283,
    label = "Cds-(Cdd-Cd)(Cds-Cdd)(Cds-Cds)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     C 0 {2,D}
6     Cdd 0 {3,D}
7     Cd 0 {4,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 284,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-Od)(Cds-Cds)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     C 0 {2,D}
6     Cdd 0 {3,D} {8,D}
7     Cd 0 {4,D}
8     Od 0 {6,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 285,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cds)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     C 0 {2,D}
6     Cdd 0 {3,D} {8,D}
7     Cd 0 {4,D}
8     C 0 {6,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 286,
    label = "Cds-(Cdd-Cd)(Cds-Cdd)(Cds-Cdd)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     C 0 {2,D}
6     Cdd 0 {3,D}
7     Cdd 0 {4,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 287,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-Od)(Cds-Cdd-Od)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     C 0 {2,D}
6     Cdd 0 {3,D} {8,D}
7     Cdd 0 {4,D} {9,D}
8     Od 0 {6,D}
9     Od 0 {7,D}
""",
    thermo = 'Cds-Cds(Cds-Cdd-Od)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 288,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-Od)(Cds-Cdd-Cd)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     C 0 {2,D}
6     Cdd 0 {3,D} {8,D}
7     Cdd 0 {4,D} {9,D}
8     Od 0 {6,D}
9     C 0 {7,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cdd-Od)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 289,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     C 0 {2,D}
6     Cdd 0 {3,D} {8,D}
7     Cdd 0 {4,D} {9,D}
8     C 0 {6,D}
9     C 0 {7,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 290,
    label = "Cds-CddCtCs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D}
3     Ct 0 {1,S}
4     Cs 0 {1,S}
""",
    thermo = 'Cds-(Cdd-Cd)CtCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 291,
    label = "Cds-(Cdd-Od)CtCs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Ct 0 {1,S}
4     Cs 0 {1,S}
5     Od 0 {2,D}
""",
    thermo = 'Cds-(Cdd-Od)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 292,
    label = "Cds-(Cdd-Cd)CtCs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Ct 0 {1,S}
4     Cs 0 {1,S}
5     C 0 {2,D}
""",
    thermo = 'Cds-CdsCtCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 293,
    label = "Cds-CddCtCds",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D}
3     Ct 0 {1,S}
4     {Cd,CO} 0 {1,S}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 294,
    label = "Cds-(Cdd-Od)(Cds-Od)Ct",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     CO 0 {1,S}
4     Ct 0 {1,S}
5     Od 0 {2,D}
""",
    thermo = 'Cds-(Cdd-Od)(Cds-Cds)(Cds-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 295,
    label = "Cds-(Cdd-Od)(Cds-Cd)Ct",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S}
4     Ct 0 {1,S}
5     Od 0 {2,D}
""",
    thermo = 'Cds-(Cdd-Od)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 296,
    label = "Cds-(Cdd-Od)(Cds-Cds)Ct",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Ct 0 {1,S}
5     Od 0 {2,D}
6     Cd 0 {3,D}
""",
    thermo = 'Cds-(Cdd-Od)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 297,
    label = "Cds-(Cdd-Od)(Cds-Cdd)Ct",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Ct 0 {1,S}
5     Od 0 {2,D}
6     Cdd 0 {3,D}
""",
    thermo = 'Cds-(Cdd-Od)(Cds-Cdd-Cd)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 298,
    label = "Cds-(Cdd-Od)(Cds-Cdd-Od)Ct",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Ct 0 {1,S}
5     Od 0 {2,D}
6     Cdd 0 {3,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cds-(Cdd-Od)(Cds-Cdd-Od)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 299,
    label = "Cds-(Cdd-Od)(Cds-Cdd-Cd)Ct",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Ct 0 {1,S}
5     Od 0 {2,D}
6     Cdd 0 {3,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cds-(Cdd-Od)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 300,
    label = "Cds-(Cdd-Cd)(Cds-Cd)Ct",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S}
4     Ct 0 {1,S}
5     C 0 {2,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 301,
    label = "Cds-(Cdd-Cd)(Cds-Cds)Ct",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Ct 0 {1,S}
5     C 0 {2,D}
6     Cd 0 {3,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 302,
    label = "Cds-(Cdd-Cd)(Cds-Cdd)Ct",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Ct 0 {1,S}
5     C 0 {2,D}
6     Cdd 0 {3,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cdd-Cd)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 303,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-Od)Ct",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Ct 0 {1,S}
5     C 0 {2,D}
6     Cdd 0 {3,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cds-Cds(Cds-Cdd-Od)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 304,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-Cd)Ct",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Ct 0 {1,S}
5     C 0 {2,D}
6     Cdd 0 {3,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 305,
    label = "Cds-CddCtCt",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D}
3     Ct 0 {1,S}
4     Ct 0 {1,S}
""",
    thermo = 'Cds-(Cdd-Cd)CtCt',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 306,
    label = "Cds-(Cdd-Od)CtCt",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Ct 0 {1,S}
4     Ct 0 {1,S}
5     Od 0 {2,D}
""",
    thermo = 'Cds-(Cdd-Od)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 307,
    label = "Cds-(Cdd-Cd)CtCt",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Ct 0 {1,S}
4     Ct 0 {1,S}
5     C 0 {2,D}
""",
    thermo = 'Cds-CdsCtCt',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 308,
    label = "Cds-CddCbCs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D}
3     Cb 0 {1,S}
4     Cs 0 {1,S}
""",
    thermo = 'Cds-(Cdd-Cd)CbCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 309,
    label = "Cds-(Cdd-Od)CbCs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cb 0 {1,S}
4     Cs 0 {1,S}
5     Od 0 {2,D}
""",
    thermo = 'Cds-(Cdd-Od)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 310,
    label = "Cds-(Cdd-Cd)CbCs",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cb 0 {1,S}
4     Cs 0 {1,S}
5     C 0 {2,D}
""",
    thermo = 'Cds-CdsCbCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 311,
    label = "Cds-CddCbCds",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D}
3     Cb 0 {1,S}
4     {Cd,CO} 0 {1,S}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 312,
    label = "Cds-(Cdd-Od)(Cds-Od)Cb",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     CO 0 {1,S}
4     Cb 0 {1,S}
5     Od 0 {2,D}
""",
    thermo = 'Cds-(Cdd-Od)(Cds-Cds)(Cds-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 313,
    label = "Cds-(Cdd-Od)(Cds-Cd)Cb",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S}
4     Cb 0 {1,S}
5     Od 0 {2,D}
""",
    thermo = 'Cds-(Cdd-Od)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 314,
    label = "Cds-(Cdd-Od)(Cds-Cds)Cb",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Cb 0 {1,S}
5     Od 0 {2,D}
6     Cd 0 {3,D}
""",
    thermo = 'Cds-(Cdd-Od)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 315,
    label = "Cds-(Cdd-Od)(Cds-Cdd)Cb",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Cb 0 {1,S}
5     Od 0 {2,D}
6     Cdd 0 {3,D}
""",
    thermo = 'Cds-(Cdd-Od)(Cds-Cdd-Cd)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 316,
    label = "Cds-(Cdd-Od)(Cds-Cdd-Od)Cb",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Cb 0 {1,S}
5     Od 0 {2,D}
6     Cdd 0 {3,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cds-(Cdd-Od)(Cds-Cdd-Od)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 317,
    label = "Cds-(Cdd-Od)(Cds-Cdd-Cd)Cb",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Cb 0 {1,S}
5     Od 0 {2,D}
6     Cdd 0 {3,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cds-(Cdd-Od)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 318,
    label = "Cds-(Cdd-Cd)(Cds-Cd)Cb",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S}
4     Cb 0 {1,S}
5     C 0 {2,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 319,
    label = "Cds-(Cdd-Cd)(Cds-Cds)Cb",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Cb 0 {1,S}
5     C 0 {2,D}
6     Cd 0 {3,D}
""",
    thermo = 'Cds-Cds(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 320,
    label = "Cds-(Cdd-Cd)(Cds-Cdd)Cb",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Cb 0 {1,S}
5     C 0 {2,D}
6     Cdd 0 {3,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cdd-Cd)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 321,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-Od)Cb",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Cb 0 {1,S}
5     C 0 {2,D}
6     Cdd 0 {3,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cds-Cds(Cds-Cdd-Od)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 322,
    label = "Cds-(Cdd-Cd)(Cds-Cdd-Cd)Cb",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cd 0 {1,S} {6,D}
4     Cb 0 {1,S}
5     C 0 {2,D}
6     Cdd 0 {3,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cds-(Cdd-Cd)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 323,
    label = "Cds-CddCbCt",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D}
3     Cb 0 {1,S}
4     Ct 0 {1,S}
""",
    thermo = 'Cds-(Cdd-Cd)CbCt',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 324,
    label = "Cds-(Cdd-Od)CbCt",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cb 0 {1,S}
4     Ct 0 {1,S}
5     Od 0 {2,D}
""",
    thermo = 'Cds-(Cdd-Od)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 325,
    label = "Cds-(Cdd-Cd)CbCt",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cb 0 {1,S}
4     Ct 0 {1,S}
5     C 0 {2,D}
""",
    thermo = 'Cds-CdsCbCt',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 326,
    label = "Cds-CddCbCb",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D}
3     Cb 0 {1,S}
4     Cb 0 {1,S}
""",
    thermo = 'Cds-(Cdd-Cd)CbCb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 327,
    label = "Cds-(Cdd-Od)CbCb",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cb 0 {1,S}
4     Cb 0 {1,S}
5     Od 0 {2,D}
""",
    thermo = 'Cds-(Cdd-Od)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 328,
    label = "Cds-(Cdd-Cd)CbCb",
    group = 
"""
1  *  C 0 {2,D} {3,S} {4,S}
2     Cdd 0 {1,D} {5,D}
3     Cb 0 {1,S}
4     Cb 0 {1,S}
5     C 0 {2,D}
""",
    thermo = 'Cds-CdsCbCb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 329,
    label = "Cs",
    group = 
"""
1  *  Cs 0
""",
    thermo = 'Cs-CsCsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 330,
    label = "Cs-HHHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([8.43,9.84,11.14,12.41,15,17.25,20.63],"cal/(mol*K)","+|-",0.06),
        H298 = (-17.9,"kcal/mol","+|-",0.1),
        S298 = (49.41,"cal/(mol*K)","+|-",0.05),
    ),
    shortDesc = u"""CHEMKIN DATABASE S(group) = S(CH4) + Rln(12)""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 331,
    label = "Cs-CHHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-CsHHH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 332,
    label = "Cs-CsHHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cs 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([6.19,7.84,9.4,10.79,13.02,14.77,17.58],"cal/(mol*K)","+|-",0.08),
        H298 = (-10.2,"kcal/mol","+|-",0.12),
        S298 = (30.41,"cal/(mol*K)","+|-",0.08),
    ),
    shortDesc = u"""Cs-CsHHH BENSON""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 333,
    label = "Cs-CdsHHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     {Cd,CO} 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)HHH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 334,
    label = "Cs-(Cds-Od)HHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([6.19,7.84,9.4,10.79,13.02,14.77,17.58],"cal/(mol*K)","+|-",0.04),
        H298 = (-10.08,"kcal/mol","+|-",0.08),
        S298 = (30.41,"cal/(mol*K)","+|-",0.04),
    ),
    shortDesc = u"""Cs-COHHH BENSON: Cp1500 =3D Cp1000*(Cp1500/Cp1000: C/Cd/H3)""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 335,
    label = "Cs-(Cds-Cd)HHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)HHH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 336,
    label = "Cs-(Cds-Cds)HHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     Cd 0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([6.19,7.84,9.4,10.79,13.02,14.77,17.58],"cal/(mol*K)","+|-",0.04),
        H298 = (-10.2,"kcal/mol","+|-",0.08),
        S298 = (30.41,"cal/(mol*K)","+|-",0.04),
    ),
    shortDesc = u"""Cs-CdHHH BENSON (Assigned Cs-CsHHH)""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 337,
    label = "Cs-(Cds-Cdd)HHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)HHH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 338,
    label = "Cs-(Cds-Cdd-Od)HHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([6.19,7.84,9.4,10.79,13.02,14.77,17.58],"cal/(mol*K)","+|-",0.04),
        H298 = (-10.08,"kcal/mol","+|-",0.08),
        S298 = (30.41,"cal/(mol*K)","+|-",0.04),
    ),
    shortDesc = u"""{CCO/C/H3} RAMAN & GREEN JPCA 2002, 106, 7937-7949, assigened same value as Cs-CsHHH""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 339,
    label = "Cs-(Cds-Cdd-Cd)HHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)HHH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 340,
    label = "Cs-CtHHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Ct 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([6.19,7.84,9.4,10.79,13.02,14.77,17.58],"cal/(mol*K)","+|-",0.08),
        H298 = (-10.2,"kcal/mol","+|-",0.15),
        S298 = (30.41,"cal/(mol*K)","+|-",0.08),
    ),
    shortDesc = u"""Cs-CtHHH BENSON (Assigned Cs-CsHHH)""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 341,
    label = "Cs-CbHHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([6.19,7.84,9.4,10.79,13.02,14.77,17.58],"cal/(mol*K)","+|-",0.1),
        H298 = (-10.2,"kcal/mol","+|-",0.18),
        S298 = (30.41,"cal/(mol*K)","+|-",0.14),
    ),
    shortDesc = u"""Cs-CbHHH BENSON (Assigned Cs-CsHHH)""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 342,
    label = "Cs-OsHHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Os 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([6.19,7.84,9.4,10.79,13.03,14.77,17.58],"cal/(mol*K)","+|-",0.1),
        H298 = (-10.1,"kcal/mol","+|-",0.2),
        S298 = (30.41,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""Cs-OHHH BENSON""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 343,
    label = "Cs-OsOsHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Os 0 {1,S}
3     Os 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([5.5,6.95,8.25,9.35,11.07,12.34,12.34],"cal/(mol*K)","+|-",0.1),
        H298 = (-15.23,"kcal/mol","+|-",0.2),
        S298 = (9.42,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""Cs-OOHH PEDLEY Hf, BOZZELLI C/C2/H2 !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 344,
    label = "Cs-OsOsOsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Os 0 {1,S}
3     Os 0 {1,S}
4     Os 0 {1,S}
5     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.54,6,7.17,8.05,9.31,10.05,10.05],"cal/(mol*K)","+|-",0.1),
        H298 = (-21.23,"kcal/mol","+|-",0.2),
        S298 = (-12.07,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""Cs-OOOH BOZZELLI del C/C2/O - C/C3/O, series !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 345,
    label = "Cs-CCHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 {1,S}
3     C 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-CsCsHH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 346,
    label = "Cs-CsCsHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cs 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([5.5,6.95,8.25,9.35,11.07,12.34,14.25],"cal/(mol*K)","+|-",0.04),
        H298 = (-4.93,"kcal/mol","+|-",0.05),
        S298 = (9.42,"cal/(mol*K)","+|-",0.13),
    ),
    shortDesc = u"""Cs-CsCsHH BENSON""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 347,
    label = "Cs-CdsCsHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     {Cd,CO} 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CsHH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 348,
    label = "Cs-(Cds-Od)CsHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([6.2,7.7,8.7,9.5,11.1,12.2,14.07],"cal/(mol*K)","+|-",0.1),
        H298 = (-5.2,"kcal/mol","+|-",0.16),
        S298 = (9.6,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""Cs-COCsHH BENSON Cp1500 =3D Cp1000*(Cp1500/Cp1000: C/C/Cd/H2)""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 349,
    label = "Cs-(Cds-Cd)CsHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CsHH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 350,
    label = "Cs-(Cds-Cds)CsHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cs 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     Cd 0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([5.12,6.86,8.32,9.49,11.22,12.48,14.36],"cal/(mol*K)","+|-",0.1),
        H298 = (-4.76,"kcal/mol","+|-",0.16),
        S298 = (9.8,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""Cs-CdCsHH BENSON""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 351,
    label = "Cs-(Cds-Cdd)CsHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cs 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CsHH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 352,
    label = "Cs-(Cds-Cdd-Od)CsHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cs 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([5.35,6.83,8.25,9.45,11.19,12.46,14.34],"cal/(mol*K)","+|-",0.1),
        H298 = (-5.723,"kcal/mol","+|-",0.16),
        S298 = (9.37,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""{C/C/H2/CCO} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 353,
    label = "Cs-(Cds-Cdd-Cd)CsHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cs 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)CsHH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 354,
    label = "Cs-CdsCdsHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     {Cd,CO} 0 {1,S}
3     {Cd,CO} 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)HH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 355,
    label = "Cs-(Cds-Od)(Cds-Od)HH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([5.03,7.44,9.16,10.49,12.17,13.57,13.57],"cal/(mol*K)","+|-",0.1),
        H298 = (-7.6,"kcal/mol","+|-",0.16),
        S298 = (5.82,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""Cs-COCOHH BENSON Hf, Mopac =3D S,Cp nov99 !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 356,
    label = "Cs-(Cds-Od)(Cds-Cd)HH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)HH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 357,
    label = "Cs-(Cds-Od)(Cds-Cds)HH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     H 0 {1,S}
5     H 0 {1,S}
6     Cd 0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.75,7.11,8.92,10.32,12.16,13.61,13.61],"cal/(mol*K)","+|-",0.1),
        H298 = (-3.8,"kcal/mol","+|-",0.16),
        S298 = (6.31,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""Cs-COCdHH BENSON Hf, Mopac =3D S,Cp nov99 !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 358,
    label = "Cs-(Cds-Od)(Cds-Cdd)HH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     H 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cdd-Cd)HH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 359,
    label = "Cs-(Cds-Od)(Cds-Cdd-Od)HH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     H 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {3,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)CsHH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 360,
    label = "Cs-(Cds-Od)(Cds-Cdd-Cd)HH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     H 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {3,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)HH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 361,
    label = "Cs-(Cds-Cd)(Cds-Cd)HH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Cd 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)HH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 362,
    label = "Cs-(Cds-Cds)(Cds-Cds)HH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     H 0 {1,S}
5     H 0 {1,S}
6     Cd 0 {2,D}
7     Cd 0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.7,6.8,8.4,9.6,11.3,12.6,14.4],"cal/(mol*K)","+|-",0.1),
        H298 = (-4.29,"kcal/mol","+|-",0.16),
        S298 = (10.2,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""Cs-CdCdHH BENSON""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 363,
    label = "Cs-(Cds-Cdd)(Cds-Cds)HH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     H 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D}
7     Cd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cds)HH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 364,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cds)HH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     H 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cd 0 {3,D}
8     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)CsHH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 365,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)HH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     H 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cd 0 {3,D}
8     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)HH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 366,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)HH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     H 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D}
7     Cdd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)HH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 367,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)HH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     H 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cdd 0 {3,D} {9,D}
8     Od 0 {6,D}
9     Od 0 {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([6.68,8.28,9.58,10.61,12.04,13.13,14.87],"cal/(mol*K)","+|-",0.1),
        H298 = (-5.301,"kcal/mol","+|-",0.16),
        S298 = (7.18,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""{C/H2/CCO2} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 368,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)HH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     H 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cdd 0 {3,D} {9,D}
8     Od 0 {6,D}
9     C 0 {7,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)(Cds-Cds)HH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 369,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)HH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     H 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cdd 0 {3,D} {9,D}
8     C 0 {6,D}
9     C 0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)HH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 370,
    label = "Cs-CtCsHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Ct 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.95,6.56,7.93,9.08,10.86,12.19,14.2],"cal/(mol*K)","+|-",0.08),
        H298 = (-4.73,"kcal/mol","+|-",0.28),
        S298 = (10.3,"cal/(mol*K)","+|-",0.07),
    ),
    shortDesc = u"""Cs-CtCsHH BENSON""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 371,
    label = "Cs-CtCdsHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Ct 0 {1,S}
3     {Cd,CO} 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CtHH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 372,
    label = "Cs-(Cds-Od)CtHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Ct 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.85,6.22,8.01,9.43,11.29,12.76,12.76],"cal/(mol*K)","+|-",0.08),
        H298 = (-5.4,"kcal/mol","+|-",0.28),
        S298 = (7.68,"cal/(mol*K)","+|-",0.07),
    ),
    shortDesc = u"""Cs-COCtHH BENSON Hf, Mopac =3D S,Cp nov99 !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 373,
    label = "Cs-(Cds-Cd)CtHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Ct 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CtHH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 374,
    label = "Cs-(Cds-Cds)CtHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Ct 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     Cd 0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.4,6.33,7.9,9.16,10.93,12.29,13.43],"cal/(mol*K)","+|-",0.08),
        H298 = (-3.49,"kcal/mol","+|-",0.28),
        S298 = (9.31,"cal/(mol*K)","+|-",0.07),
    ),
    shortDesc = u"""Cs-CtCdHH RAMAN & GREEN JPCA 2002, 106, 11141-11149""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 375,
    label = "Cs-(Cds-Cdd)CtHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Ct 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CtHH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 376,
    label = "Cs-(Cds-Cdd-Od)CtHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Ct 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)(Cds-Cds)HH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 377,
    label = "Cs-(Cds-Cdd-Cd)CtHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Ct 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)CtHH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 378,
    label = "Cs-CtCtHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Ct 0 {1,S}
3     Ct 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4,6.07,7.71,9.03,10.88,12.3,12.48],"cal/(mol*K)","+|-",0.08),
        H298 = (-0.82,"kcal/mol","+|-",0.28),
        S298 = (10.04,"cal/(mol*K)","+|-",0.07),
    ),
    shortDesc = u"""Cs-CtCtHH RAMAN & GREEN JPCA 2002, 106, 11141-11149""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 379,
    label = "Cs-CbCsHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([5.84,7.61,8.98,10.01,11.49,12.54,13.76],"cal/(mol*K)","+|-",0.1),
        H298 = (-4.86,"kcal/mol","+|-",0.2),
        S298 = (9.34,"cal/(mol*K)","+|-",0.19),
    ),
    shortDesc = u"""Cs-CbCsHH BENSON""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 380,
    label = "Cs-CbCdsHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     {Cd,CO} 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CbHH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 381,
    label = "Cs-(Cds-Od)CbHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cb 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([5.38,7.59,9.25,10.51,12.19,13.52,13.52],"cal/(mol*K)","+|-",0.1),
        H298 = (-5.4,"kcal/mol","+|-",0.2),
        S298 = (5.89,"cal/(mol*K)","+|-",0.19),
    ),
    shortDesc = u"""Cs-COCbHH BENSON Hf, Mopac =3D S,Cp nov99 !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 382,
    label = "Cs-(Cds-Cd)CbHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Cb 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CbHH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 383,
    label = "Cs-(Cds-Cds)CbHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     Cd 0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.51,6.76,8.61,10.01,11.97,13.4,15.47],"cal/(mol*K)","+|-",0.2),
        H298 = (-4.29,"kcal/mol","+|-",0.2),
        S298 = (2,"cal/(mol*K)","+|-",0.19),
    ),
    shortDesc = u"""Cs-CbCdHH Hf=Stein S,Cp=3D mopac nov99""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 384,
    label = "Cs-(Cds-Cdd)CbHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CbHH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 385,
    label = "Cs-(Cds-Cdd-Od)CbHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)(Cds-Cds)HH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 386,
    label = "Cs-(Cds-Cdd-Cd)CbHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)CbHH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 387,
    label = "Cs-CbCtHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Ct 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.28,6.43,8.16,9.5,11.36,12.74,13.7],"cal/(mol*K)","+|-",0.08),
        H298 = (-4.29,"kcal/mol","+|-",0.28),
        S298 = (9.84,"cal/(mol*K)","+|-",0.07),
    ),
    shortDesc = u"""Cs-CbCtHH Hf=Stein S,Cp=3D mopac nov99""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 388,
    label = "Cs-CbCbHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Cb 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([5.67,7.7,9.31,10.52,12.21,13.47,15.11],"cal/(mol*K)","+|-",0.2),
        H298 = (-4.29,"kcal/mol","+|-",0.2),
        S298 = (8.07,"cal/(mol*K)","+|-",0.19),
    ),
    shortDesc = u"""Cs-CbCbHH Hf=3Dbsn/Cs/Cd2/H2 S,Cp=3D mopac nov99""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 389,
    label = "Cs-CCCH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 {1,S}
3     C 0 {1,S}
4     C 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-CsCsCsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 390,
    label = "Cs-CsCsCsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cs 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.54,6,7.17,8.05,9.31,10.05,11.17],"cal/(mol*K)","+|-",0.07),
        H298 = (-1.9,"kcal/mol","+|-",0.15),
        S298 = (-12.07,"cal/(mol*K)","+|-",0.07),
    ),
    shortDesc = u"""Cs-CsCsCsH BENSON""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 391,
    label = "Cs-CdsCsCsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     {Cd,CO} 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CsCsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 392,
    label = "Cs-(Cds-Od)CsCsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.16,5.91,7.34,8.19,9.46,10.19,10.19],"cal/(mol*K)","+|-",0.13),
        H298 = (-1.7,"kcal/mol","+|-",0.27),
        S298 = (-11.7,"cal/(mol*K)","+|-",0.15),
    ),
    shortDesc = u"""Cs-COCsCsH BOZZELLI - BENSON Hf, S, -C/C2Cd/H =3D Cp !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 393,
    label = "Cs-(Cds-Cd)CsCsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CsCsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 394,
    label = "Cs-(Cds-Cds)CsCsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     H 0 {1,S}
6     Cd 0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.16,5.91,7.34,8.19,9.46,10.19,11.28],"cal/(mol*K)","+|-",0.13),
        H298 = (-1.48,"kcal/mol","+|-",0.27),
        S298 = (-11.69,"cal/(mol*K)","+|-",0.15),
    ),
    shortDesc = u"""Cs-CdCsCsH BENSON""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 395,
    label = "Cs-(Cds-Cdd)CsCsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CsCsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 396,
    label = "Cs-(Cds-Cdd-Od)CsCsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.96,6.35,7.61,8.54,9.65,10.35,11.19],"cal/(mol*K)","+|-",0.13),
        H298 = (-3.634,"kcal/mol","+|-",0.27),
        S298 = (-12.31,"cal/(mol*K)","+|-",0.15),
    ),
    shortDesc = u"""{C/C2/CCO/H} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 397,
    label = "Cs-(Cds-Cdd-Cd)CsCsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     C 0 {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.16,5.91,7.34,8.19,9.46,10.19,11.28],"cal/(mol*K)","+|-",0.13),
        H298 = (-1.48,"kcal/mol","+|-",0.27),
        S298 = (-11.69,"cal/(mol*K)","+|-",0.15),
    ),
    shortDesc = u"""Cs-CdCsCsH BENSON""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 398,
    label = "Cs-CtCsCsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Ct 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.99,5.61,6.85,7.78,9.1,9.9,11.12],"cal/(mol*K)","+|-",0.13),
        H298 = (-1.72,"kcal/mol","+|-",0.27),
        S298 = (-11.19,"cal/(mol*K)","+|-",0.15),
    ),
    shortDesc = u"""Cs-CtCsCsH BENSON""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 399,
    label = "Cs-CbCsCsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.88,6.66,7.9,8.75,9.73,10.25,10.68],"cal/(mol*K)","+|-",0.13),
        H298 = (-0.98,"kcal/mol","+|-",0.27),
        S298 = (-12.15,"cal/(mol*K)","+|-",0.15),
    ),
    shortDesc = u"""Cs-CbCsCsH BENSON""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 400,
    label = "Cs-CdsCdsCsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     {Cd,CO} 0 {1,S}
3     {Cd,CO} 0 {1,S}
4     Cs 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 401,
    label = "Cs-(Cds-Od)(Cds-Od)CsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Cs 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-CsCsCsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 402,
    label = "Cs-(Cds-Od)(Cds-Cd)CsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S}
4     Cs 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 403,
    label = "Cs-(Cds-Od)(Cds-Cds)CsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cs 0 {1,S}
5     H 0 {1,S}
6     Cd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Od)CsCsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 404,
    label = "Cs-(Cds-Od)(Cds-Cdd)CsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cs 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cdd-Cd)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 405,
    label = "Cs-(Cds-Od)(Cds-Cdd-Od)CsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cs 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {3,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)CsCsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 406,
    label = "Cs-(Cds-Od)(Cds-Cdd-Cd)CsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cs 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {3,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 407,
    label = "Cs-(Cds-Cd)(Cds-Cd)CsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Cd 0 {1,S}
4     Cs 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 408,
    label = "Cs-(Cds-Cds)(Cds-Cds)CsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cs 0 {1,S}
5     H 0 {1,S}
6     Cd 0 {2,D}
7     Cd 0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([5.28,6.54,7.67,8.48,9.45,10.18,11.24],"cal/(mol*K)","+|-",0.13),
        H298 = (-1.1,"kcal/mol","+|-",0.27),
        S298 = (-13.03,"cal/(mol*K)","+|-",0.15),
    ),
    shortDesc = u"""Cs-CdCdCsH RAMAN & GREEN JPCA 2002, 106, 11141-11149""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 409,
    label = "Cs-(Cds-Cdd)(Cds-Cds)CsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cs 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D}
7     Cd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cds)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 410,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cds)CsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cs 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cd 0 {3,D}
8     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)CsCsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 411,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cs 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cd 0 {3,D}
8     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 412,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)CsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cs 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D}
7     Cdd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 413,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cs 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cdd 0 {3,D} {9,D}
8     Od 0 {6,D}
9     Od 0 {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([6.33,7.96,9.13,9.91,10.7,11.19,11.81],"cal/(mol*K)","+|-",0.13),
        H298 = (-3.714,"kcal/mol","+|-",0.27),
        S298 = (-14.12,"cal/(mol*K)","+|-",0.15),
    ),
    shortDesc = u"""{C/C/H/CCO2} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 414,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)CsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cs 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cdd 0 {3,D} {9,D}
8     Od 0 {6,D}
9     C 0 {7,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)(Cds-Cds)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 415,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cs 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cdd 0 {3,D} {9,D}
8     C 0 {6,D}
9     C 0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 416,
    label = "Cs-CtCdsCsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Ct 0 {1,S}
3     {Cd,CO} 0 {1,S}
4     Cs 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CtCsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 417,
    label = "Cs-(Cds-Od)CtCsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Ct 0 {1,S}
4     Cs 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 418,
    label = "Cs-(Cds-Cd)CtCsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Ct 0 {1,S}
4     Cs 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CtCsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 419,
    label = "Cs-(Cds-Cds)CtCsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Ct 0 {1,S}
4     Cs 0 {1,S}
5     H 0 {1,S}
6     Cd 0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([5.55,7.21,8.39,9.17,10,10.61,10.51],"cal/(mol*K)","+|-",0.13),
        H298 = (-6.9,"kcal/mol","+|-",0.27),
        S298 = (-13.48,"cal/(mol*K)","+|-",0.15),
    ),
    shortDesc = u"""Cs-CtCdCsH RAMAN & GREEN JPCA 2002, 106, 11141-11149""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 420,
    label = "Cs-(Cds-Cdd)CtCsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Ct 0 {1,S}
4     Cs 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CtCsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 421,
    label = "Cs-(Cds-Cdd-Od)CtCsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Ct 0 {1,S}
4     Cs 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)(Cds-Cds)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 422,
    label = "Cs-(Cds-Cdd-Cd)CtCsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Ct 0 {1,S}
4     Cs 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)CtCsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 423,
    label = "Cs-CbCdsCsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     {Cd,CO} 0 {1,S}
4     Cs 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CbCsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 424,
    label = "Cs-(Cds-Od)CbCsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cb 0 {1,S}
4     Cs 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 425,
    label = "Cs-(Cds-Cd)CbCsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Cb 0 {1,S}
4     Cs 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CbCsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 426,
    label = "Cs-(Cds-Cds)CbCsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Cs 0 {1,S}
5     H 0 {1,S}
6     Cd 0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.5,6.57,8.07,8.89,9.88,10.39,10.79],"cal/(mol*K)","+|-",0.13),
        H298 = (-1.56,"kcal/mol","+|-",0.27),
        S298 = (-11.77,"cal/(mol*K)","+|-",0.15),
    ),
    shortDesc = u"""Cs-CbCdCsH BOZZELLI =3D Cs/Cs2/Cd/H + (Cs/Cs2/Cb/H - Cs/Cs3/H)""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 427,
    label = "Cs-(Cds-Cdd)CbCsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Cs 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CbCsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 428,
    label = "Cs-(Cds-Cdd-Od)CbCsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Cs 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)(Cds-Cds)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 429,
    label = "Cs-(Cds-Cdd-Cd)CbCsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Cs 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)CbCsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 430,
    label = "Cs-CtCtCsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Ct 0 {1,S}
3     Ct 0 {1,S}
4     Cs 0 {1,S}
5     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.27,5.32,6.9,8.03,9.33,10.21,9.38],"cal/(mol*K)","+|-",0.13),
        H298 = (1.72,"kcal/mol","+|-",0.27),
        S298 = (-11.61,"cal/(mol*K)","+|-",0.15),
    ),
    shortDesc = u"""Cs-CtCtCsH RAMAN & GREEN JPCA 2002, 106, 11141-11149""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 431,
    label = "Cs-CbCtCsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Ct 0 {1,S}
4     Cs 0 {1,S}
5     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.33,6.27,7.58,8.48,9.52,10.1,10.63],"cal/(mol*K)","+|-",0.13),
        H298 = (-1.55,"kcal/mol","+|-",0.27),
        S298 = (-11.65,"cal/(mol*K)","+|-",0.15),
    ),
    shortDesc = u"""Cs-CbCtCsH BOZZELLI =3D Cs/Cs2/Cb/H + (Cs/Cs2/Ct/H - Cs/Cs3/H)""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 432,
    label = "Cs-CbCbCsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Cb 0 {1,S}
4     Cs 0 {1,S}
5     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([5.22,7.32,8.63,8.45,10.15,10.45,10.89],"cal/(mol*K)","+|-",0.13),
        H298 = (-1.06,"kcal/mol","+|-",0.27),
        S298 = (-12.23,"cal/(mol*K)","+|-",0.15),
    ),
    shortDesc = u"""Cs-CbCbCsCs BOZZELLI =3D Cs/Cs2/Cb/H + (Cs/Cs2/Cb/H - Cs/Cs3/H)""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 433,
    label = "Cs-CdsCdsCdsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     {Cd,CO} 0 {1,S}
3     {Cd,CO} 0 {1,S}
4     {Cd,CO} 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 434,
    label = "Cs-(Cds-Od)(Cds-Od)(Cds-Od)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     CO 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-CsCsCsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 435,
    label = "Cs-(Cds-Od)(Cds-Od)(Cds-Cd)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Cd 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 436,
    label = "Cs-(Cds-Od)(Cds-Od)(Cds-Cds)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Cd 0 {1,S} {6,D}
5     H 0 {1,S}
6     Cd 0 {4,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Od)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 437,
    label = "Cs-(Cds-Od)(Cds-Od)(Cds-Cdd)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Cd 0 {1,S} {6,D}
5     H 0 {1,S}
6     Cdd 0 {4,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Cd)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 438,
    label = "Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Od)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Cd 0 {1,S} {6,D}
5     H 0 {1,S}
6     Cdd 0 {4,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)CsCsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 439,
    label = "Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Cd)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Cd 0 {1,S} {6,D}
5     H 0 {1,S}
6     Cdd 0 {4,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 440,
    label = "Cs-(Cds-Od)(Cds-Cd)(Cds-Cd)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S}
4     Cd 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 441,
    label = "Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     H 0 {1,S}
6     Cd 0 {3,D}
7     Cd 0 {4,D}
""",
    thermo = 'Cs-(Cds-Od)CsCsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 442,
    label = "Cs-(Cds-Od)(Cds-Cdd)(Cds-Cds)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     H 0 {1,S}
6     Cdd 0 {3,D}
7     Cd 0 {4,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 443,
    label = "Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     H 0 {1,S}
6     Cdd 0 {3,D} {8,D}
7     Cd 0 {4,D}
8     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cdd-Od)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 444,
    label = "Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cds)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     H 0 {1,S}
6     Cdd 0 {3,D} {8,D}
7     Cd 0 {4,D}
8     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 445,
    label = "Cs-(Cds-Od)(Cds-Cdd)(Cds-Cdd)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     H 0 {1,S}
6     Cdd 0 {3,D}
7     Cdd 0 {4,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 446,
    label = "Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     H 0 {1,S}
6     Cdd 0 {3,D} {8,D}
7     Cdd 0 {4,D} {9,D}
8     Od 0 {6,D}
9     Od 0 {7,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 447,
    label = "Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     H 0 {1,S}
6     Cdd 0 {3,D} {8,D}
7     Cdd 0 {4,D} {9,D}
8     Od 0 {6,D}
9     C 0 {7,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 448,
    label = "Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     H 0 {1,S}
6     Cdd 0 {3,D} {8,D}
7     Cdd 0 {4,D} {9,D}
8     C 0 {6,D}
9     C 0 {7,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 449,
    label = "Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Cd 0 {1,S}
4     Cd 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 450,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     H 0 {1,S}
6     Cd 0 {2,D}
7     Cd 0 {3,D}
8     Cd 0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.51,5.96,7.13,7.98,9.06,9.9,11.23],"cal/(mol*K)","+|-",0.13),
        H298 = (0.41,"kcal/mol","+|-",0.27),
        S298 = (-11.82,"cal/(mol*K)","+|-",0.15),
    ),
    shortDesc = u"""Cs-CdCdCdH RAMAN & GREEN JPC 2002""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 451,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     H 0 {1,S}
6     Cd 0 {2,D}
7     Cd 0 {3,D}
8     Cdd 0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 452,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     H 0 {1,S}
6     Cd 0 {2,D}
7     Cd 0 {3,D}
8     Cdd 0 {4,D} {9,D}
9     Od 0 {8,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)CsCsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 453,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     H 0 {1,S}
6     Cd 0 {2,D}
7     Cd 0 {3,D}
8     Cdd 0 {4,D} {9,D}
9     C 0 {8,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 454,
    label = "Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     H 0 {1,S}
6     Cd 0 {2,D}
7     Cdd 0 {3,D}
8     Cdd 0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 455,
    label = "Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     H 0 {1,S}
6     Cd 0 {2,D}
7     Cdd 0 {3,D} {9,D}
8     Cdd 0 {4,D} {10,D}
9     Od 0 {7,D}
10    Od 0 {8,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 456,
    label = "Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Cd)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     H 0 {1,S}
6     Cd 0 {2,D}
7     Cdd 0 {3,D} {9,D}
8     Cdd 0 {4,D} {10,D}
9     Od 0 {7,D}
10    C 0 {8,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 457,
    label = "Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     H 0 {1,S}
6     Cd 0 {2,D}
7     Cdd 0 {3,D} {9,D}
8     Cdd 0 {4,D} {10,D}
9     C 0 {7,D}
10    C 0 {8,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 458,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     H 0 {1,S}
6     Cdd 0 {2,D}
7     Cdd 0 {3,D}
8     Cdd 0 {4,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 459,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     H 0 {1,S}
6     Cdd 0 {2,D} {9,D}
7     Cdd 0 {3,D} {10,D}
8     Cdd 0 {4,D} {11,D}
9     Od 0 {6,D}
10    Od 0 {7,D}
11    Od 0 {8,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 460,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     H 0 {1,S}
6     Cdd 0 {2,D} {9,D}
7     Cdd 0 {3,D} {10,D}
8     Cdd 0 {4,D} {11,D}
9     Od 0 {6,D}
10    Od 0 {7,D}
11    C 0 {8,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 461,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     H 0 {1,S}
6     Cdd 0 {2,D} {9,D}
7     Cdd 0 {3,D} {10,D}
8     Cdd 0 {4,D} {11,D}
9     Od 0 {6,D}
10    C 0 {7,D}
11    C 0 {8,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 462,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     H 0 {1,S}
6     Cdd 0 {2,D} {9,D}
7     Cdd 0 {3,D} {10,D}
8     Cdd 0 {4,D} {11,D}
9     C 0 {6,D}
10    C 0 {7,D}
11    C 0 {8,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 463,
    label = "Cs-CtCdsCdsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Ct 0 {1,S}
3     {Cd,CO} 0 {1,S}
4     {Cd,CO} 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CtH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 464,
    label = "Cs-(Cds-Od)(Cds-Od)CtH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Ct 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 465,
    label = "Cs-(Cds-Od)(Cds-Cd)CtH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S}
4     Ct 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)CtH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 466,
    label = "Cs-(Cds-Od)(Cds-Cds)CtH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Ct 0 {1,S}
5     H 0 {1,S}
6     Cd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 467,
    label = "Cs-(Cds-Od)(Cds-Cdd)CtH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Ct 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cdd-Cd)CtH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 468,
    label = "Cs-(Cds-Od)(Cds-Cdd-Od)CtH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Ct 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {3,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 469,
    label = "Cs-(Cds-Od)(Cds-Cdd-Cd)CtH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Ct 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {3,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)CtH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 470,
    label = "Cs-(Cds-Cd)(Cds-Cd)CtH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Cd 0 {1,S}
4     Ct 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CtH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 471,
    label = "Cs-(Cds-Cds)(Cds-Cds)CtH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Ct 0 {1,S}
5     H 0 {1,S}
6     Cd 0 {2,D}
7     Cd 0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([6.68,7.85,8.62,9.16,9.81,10.42,10.49],"cal/(mol*K)","+|-",0.13),
        H298 = (1.88,"kcal/mol","+|-",0.27),
        S298 = (-13.75,"cal/(mol*K)","+|-",0.15),
    ),
    shortDesc = u"""Cs-CtCdCdH RAMAN & GREEN JPCA 2002, 106, 11141-11149""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 472,
    label = "Cs-(Cds-Cdd)(Cds-Cds)CtH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Ct 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D}
7     Cd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cds)CtH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 473,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cds)CtH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Ct 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cd 0 {3,D}
8     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 474,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CtH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Ct 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cd 0 {3,D}
8     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CtH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 475,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)CtH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Ct 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D}
7     Cdd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 476,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CtH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Ct 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cdd 0 {3,D} {9,D}
8     Od 0 {6,D}
9     Od 0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 477,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)CtH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Ct 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cdd 0 {3,D} {9,D}
8     Od 0 {6,D}
9     C 0 {7,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)(Cds-Cds)CtH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 478,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Ct 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cdd 0 {3,D} {9,D}
8     C 0 {6,D}
9     C 0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CtH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 479,
    label = "Cs-CbCdsCdsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     {Cd,CO} 0 {1,S}
4     {Cd,CO} 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CbH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 480,
    label = "Cs-(Cds-Od)(Cds-Od)CbH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Cb 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 481,
    label = "Cs-(Cds-Od)(Cds-Cd)CbH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S}
4     Cb 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)CbH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 482,
    label = "Cs-(Cds-Od)(Cds-Cds)CbH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cb 0 {1,S}
5     H 0 {1,S}
6     Cd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 483,
    label = "Cs-(Cds-Od)(Cds-Cdd)CbH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cb 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cdd-Cd)CbH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 484,
    label = "Cs-(Cds-Od)(Cds-Cdd-Od)CbH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cb 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {3,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 485,
    label = "Cs-(Cds-Od)(Cds-Cdd-Cd)CbH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cb 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {3,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)CbH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 486,
    label = "Cs-(Cds-Cd)(Cds-Cd)CbH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Cd 0 {1,S}
4     Cb 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CbH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 487,
    label = "Cs-(Cds-Cds)(Cds-Cds)CbH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cb 0 {1,S}
5     H 0 {1,S}
6     Cd 0 {2,D}
7     Cd 0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.12,6.51,8.24,9,10.03,10.53,10.89],"cal/(mol*K)","+|-",0.13),
        H298 = (-1.39,"kcal/mol","+|-",0.27),
        S298 = (-11.39,"cal/(mol*K)","+|-",0.15),
    ),
    shortDesc = u"""Cs-CbCdCdH BOZZELLI =3D Cs/Cs/Cd2/H + (Cs/Cs2/Cb/H - Cs/Cs3/H)""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 488,
    label = "Cs-(Cds-Cdd)(Cds-Cds)CbH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cb 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D}
7     Cd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cds)CbH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 489,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cds)CbH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cb 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cd 0 {3,D}
8     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 490,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CbH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cb 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cd 0 {3,D}
8     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CbH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 491,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)CbH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cb 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D}
7     Cdd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 492,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CbH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cb 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cdd 0 {3,D} {9,D}
8     Od 0 {6,D}
9     Od 0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 493,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)CbH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cb 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cdd 0 {3,D} {9,D}
8     Od 0 {6,D}
9     C 0 {7,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)(Cds-Cds)CbH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 494,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cb 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cdd 0 {3,D} {9,D}
8     C 0 {6,D}
9     C 0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CbH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 495,
    label = "Cs-CtCtCdsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Ct 0 {1,S}
3     Ct 0 {1,S}
4     {Cd,CO} 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-CtCt(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 496,
    label = "Cs-CtCt(Cds-Od)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Ct 0 {1,S}
3     Ct 0 {1,S}
4     CO 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 497,
    label = "Cs-CtCt(Cds-Cd)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Ct 0 {1,S}
3     Ct 0 {1,S}
4     Cd 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-CtCt(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 498,
    label = "Cs-CtCt(Cds-Cds)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Ct 0 {1,S}
3     Ct 0 {1,S}
4     Cd 0 {1,S} {6,D}
5     H 0 {1,S}
6     Cd 0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.58,5.68,7.11,8.12,9.27,10.13,9.44],"cal/(mol*K)","+|-",0.13),
        H298 = (4.73,"kcal/mol","+|-",0.27),
        S298 = (-11.46,"cal/(mol*K)","+|-",0.15),
    ),
    shortDesc = u"""Cs-CtCtCdH RAMAN & GREEN JPCA 2002, 106, 11141-11149""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 499,
    label = "Cs-CtCt(Cds-Cdd)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Ct 0 {1,S}
3     Ct 0 {1,S}
4     Cd 0 {1,S} {6,D}
5     H 0 {1,S}
6     Cdd 0 {4,D}
""",
    thermo = 'Cs-CtCt(Cds-Cdd-Cd)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 500,
    label = "Cs-CtCt(Cds-Cdd-Od)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Ct 0 {1,S}
3     Ct 0 {1,S}
4     Cd 0 {1,S} {6,D}
5     H 0 {1,S}
6     Cdd 0 {4,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 501,
    label = "Cs-CtCt(Cds-Cdd-Cd)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Ct 0 {1,S}
3     Ct 0 {1,S}
4     Cd 0 {1,S} {6,D}
5     H 0 {1,S}
6     Cdd 0 {4,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-CtCt(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 502,
    label = "Cs-CbCtCdsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Ct 0 {1,S}
4     {Cd,CO} 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-CbCt(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 503,
    label = "Cs-CbCt(Cds-Od)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Ct 0 {1,S}
4     CO 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)CtH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 504,
    label = "Cs-CbCt(Cds-Cd)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Ct 0 {1,S}
4     Cd 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-CbCt(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 505,
    label = "Cs-CbCt(Cds-Cds)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Ct 0 {1,S}
4     Cd 0 {1,S} {6,D}
5     H 0 {1,S}
6     Cd 0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CtH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 506,
    label = "Cs-CbCt(Cds-Cdd)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Ct 0 {1,S}
4     Cd 0 {1,S} {6,D}
5     H 0 {1,S}
6     Cdd 0 {4,D}
""",
    thermo = 'Cs-CbCt(Cds-Cdd-Cd)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 507,
    label = "Cs-CbCt(Cds-Cdd-Od)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Ct 0 {1,S}
4     Cd 0 {1,S} {6,D}
5     H 0 {1,S}
6     Cdd 0 {4,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)(Cds-Cds)CtH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 508,
    label = "Cs-CbCt(Cds-Cdd-Cd)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Ct 0 {1,S}
4     Cd 0 {1,S} {6,D}
5     H 0 {1,S}
6     Cdd 0 {4,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-CbCt(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 509,
    label = "Cs-CbCbCdsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Cb 0 {1,S}
4     {Cd,CO} 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-CbCb(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 510,
    label = "Cs-CbCb(Cds-Od)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Cb 0 {1,S}
4     CO 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = -1,
    label = "Cs-CbCb(Cds-Cd)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Cb 0 {1,S}
4     Cd 0 {1,S}
5     H 0 {1,S}
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
    index = 511,
    label = "Cs-CbCb(Cds-Cds)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Cb 0 {1,S}
4     Cd 0 {1,S} {6,D}
5     H 0 {1,S}
6     Cd 0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 512,
    label = "Cs-CbCb(Cds-Cdd)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Cb 0 {1,S}
4     Cd 0 {1,S} {6,D}
5     H 0 {1,S}
6     Cdd 0 {4,D}
""",
    thermo = 'Cs-CbCb(Cds-Cdd-Cd)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 513,
    label = "Cs-CbCb(Cds-Cdd-Od)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Cb 0 {1,S}
4     Cd 0 {1,S} {6,D}
5     H 0 {1,S}
6     Cdd 0 {4,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 514,
    label = "Cs-CbCb(Cds-Cdd-Cd)H",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Cb 0 {1,S}
4     Cd 0 {1,S} {6,D}
5     H 0 {1,S}
6     Cdd 0 {4,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-CbCb(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 515,
    label = "Cs-CtCtCtH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Ct 0 {1,S}
3     Ct 0 {1,S}
4     Ct 0 {1,S}
5     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.03,5.27,6.78,7.88,9.14,10.08,8.47],"cal/(mol*K)","+|-",0.13),
        H298 = (10.11,"kcal/mol","+|-",0.27),
        S298 = (-10.46,"cal/(mol*K)","+|-",0.15),
    ),
    shortDesc = u"""Cs-CtCtCtH RAMAN & GREEN JPCA 2002, 106, 11141-11149""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 516,
    label = "Cs-CbCtCtH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Ct 0 {1,S}
4     Ct 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-CtCt(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 517,
    label = "Cs-CbCbCtH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Cb 0 {1,S}
4     Ct 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CtH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 518,
    label = "Cs-CbCbCbH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Cb 0 {1,S}
4     Cb 0 {1,S}
5     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([5.56,7.98,9.36,10.15,10.57,10.65,9.7],"cal/(mol*K)","+|-",0.13),
        H298 = (-0.34,"kcal/mol","+|-",0.27),
        S298 = (-12.31,"cal/(mol*K)","+|-",0.15),
    ),
    shortDesc = u"""Cs-CbCbCbH BOZZELLI =3D Cs/Cs/Cb2/H + (Cs/Cs2/Cb/H - Cs/Cs3/H)""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 519,
    label = "Cs-CCCC",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 {1,S}
3     C 0 {1,S}
4     C 0 {1,S}
5     C 0 {1,S}
""",
    thermo = 'Cs-CsCsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 520,
    label = "Cs-CsCsCsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cs 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.37,6.13,7.36,8.12,8.77,8.76,8.12],"cal/(mol*K)","+|-",0.13),
        H298 = (0.5,"kcal/mol","+|-",0.27),
        S298 = (-35.1,"cal/(mol*K)","+|-",0.15),
    ),
    shortDesc = u"""Cs-CsCsCsCs BENSON""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 521,
    label = "Cs-CdsCsCsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     {Cd,CO} 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 522,
    label = "Cs-(Cds-Od)CsCsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.99,6.04,7.43,8.26,8.92,8.96,8.23],"cal/(mol*K)","+|-",0.13),
        H298 = (1.4,"kcal/mol","+|-",0.27),
        S298 = (-34.72,"cal/(mol*K)","+|-",0.15),
    ),
    shortDesc = u"""Cs-COCsCsCs Hf BENSON S,Cp =3D C/Cd/C3""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 523,
    label = "Cs-(Cds-Cd)CsCsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 524,
    label = "Cs-(Cds-Cds)CsCsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
6     Cd 0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.99,6.04,7.43,8.26,8.92,8.96,8.23],"cal/(mol*K)","+|-",0.13),
        H298 = (1.68,"kcal/mol","+|-",0.27),
        S298 = (-34.72,"cal/(mol*K)","+|-",0.15),
    ),
    shortDesc = u"""Cs-CdCsCsCs BENSON""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 525,
    label = "Cs-(Cds-Cdd)CsCsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 526,
    label = "Cs-(Cds-Cdd-Od)CsCsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.48,6.06,7.31,8.07,8.59,8.66,8.29],"cal/(mol*K)","+|-",0.13),
        H298 = (-2.896,"kcal/mol","+|-",0.27),
        S298 = (-34.87,"cal/(mol*K)","+|-",0.15),
    ),
    shortDesc = u"""{C/C3/CCO} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 527,
    label = "Cs-(Cds-Cdd-Cd)CsCsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)CsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 528,
    label = "Cs-CtCsCsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Ct 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.37,6.79,8.09,8.78,9.19,8.96,7.63],"cal/(mol*K)","+|-",0.13),
        H298 = (2.81,"kcal/mol","+|-",0.27),
        S298 = (-35.18,"cal/(mol*K)","+|-",0.15),
    ),
    shortDesc = u"""Cs-CtCsCsCs BENSON""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 529,
    label = "Cs-CbCsCsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.37,6.79,8.09,8.78,9.19,8.96,7.63],"cal/(mol*K)","+|-",0.13),
        H298 = (2.81,"kcal/mol","+|-",0.26),
        S298 = (-35.18,"cal/(mol*K)","+|-",0.13),
    ),
    shortDesc = u"""Cs-CbCsCsCs BENSON""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 530,
    label = "Cs-CdsCdsCsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     {Cd,CO} 0 {1,S}
3     {Cd,CO} 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 531,
    label = "Cs-(Cds-Od)(Cds-Od)CsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    thermo = 'Cs-CsCsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 532,
    label = "Cs-(Cds-Od)(Cds-Cd)CsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 533,
    label = "Cs-(Cds-Od)(Cds-Cds)CsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
6     Cd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Od)CsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 534,
    label = "Cs-(Cds-Od)(Cds-Cdd)CsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cdd-Cd)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 535,
    label = "Cs-(Cds-Od)(Cds-Cdd-Od)CsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {3,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)CsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 536,
    label = "Cs-(Cds-Od)(Cds-Cdd-Cd)CsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {3,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 537,
    label = "Cs-(Cds-Cd)(Cds-Cd)CsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Cd 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 538,
    label = "Cs-(Cds-Cds)(Cds-Cds)CsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
6     Cd 0 {2,D}
7     Cd 0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.99,6.04,7.43,8.26,8.92,8.96,8.23],"cal/(mol*K)","+|-",0.13),
        H298 = (1.68,"kcal/mol","+|-",0.26),
        S298 = (-34.72,"cal/(mol*K)","+|-",0.13),
    ),
    shortDesc = u"""Cs-CdCdCsCs BENSON""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 539,
    label = "Cs-(Cds-Cdd)(Cds-Cds)CsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {2,D}
7     Cd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cds)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 540,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cds)CsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cd 0 {3,D}
8     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)CsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 541,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cd 0 {3,D}
8     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 542,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)CsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {2,D}
7     Cdd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 543,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cdd 0 {3,D} {9,D}
8     Od 0 {6,D}
9     Od 0 {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([6.73,8.1,9.02,9.53,9.66,9.52,8.93],"cal/(mol*K)","+|-",0.13),
        H298 = (-2.987,"kcal/mol","+|-",0.26),
        S298 = (-36.46,"cal/(mol*K)","+|-",0.13),
    ),
    shortDesc = u"""{C/C2/CCO2} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 544,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)CsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cdd 0 {3,D} {9,D}
8     Od 0 {6,D}
9     C 0 {7,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)(Cds-Cds)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 545,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cdd 0 {3,D} {9,D}
8     C 0 {6,D}
9     C 0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 546,
    label = "Cs-CtCdsCsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Ct 0 {1,S}
3     {Cd,CO} 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CtCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 547,
    label = "Cs-(Cds-Od)CtCsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Ct 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 548,
    label = "Cs-(Cds-Cd)CtCsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Ct 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CtCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 549,
    label = "Cs-(Cds-Cds)CtCsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Ct 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
6     Cd 0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.99,6.7,8.16,8.92,9.34,9.16,7.14],"cal/(mol*K)","+|-",0.13),
        H298 = (2.99,"kcal/mol","+|-",0.26),
        S298 = (-34.8,"cal/(mol*K)","+|-",0.13),
    ),
    shortDesc = u"""Cs-CtCdCsCs BOZZELLI =3D Cs/Cs3/Cd + (Cs/Cs3/Ct - Cs/Cs4)""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 550,
    label = "Cs-(Cds-Cdd)CtCsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Ct 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CtCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 551,
    label = "Cs-(Cds-Cdd-Od)CtCsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Ct 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)(Cds-Cds)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 552,
    label = "Cs-(Cds-Cdd-Cd)CtCsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Ct 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)CtCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 553,
    label = "Cs-CbCdsCsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     {Cd,CO} 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CbCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 554,
    label = "Cs-(Cds-Od)CbCsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cb 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 555,
    label = "Cs-(Cds-Cd)CbCsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Cb 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CbCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 556,
    label = "Cs-(Cds-Cds)CbCsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
6     Cd 0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.99,6.7,8.16,8.92,9.34,9.16,7.14],"cal/(mol*K)","+|-",0.13),
        H298 = (2.99,"kcal/mol","+|-",0.26),
        S298 = (-34.8,"cal/(mol*K)","+|-",0.13),
    ),
    shortDesc = u"""Cs-CbCdCsCs BOZZELLI =3D Cs/Cs3/Cb + (Cs/Cs3/Cd - Cs/Cs4)""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 557,
    label = "Cs-(Cds-Cdd)CbCsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CbCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 558,
    label = "Cs-(Cds-Cdd-Od)CbCsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)(Cds-Cds)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 559,
    label = "Cs-(Cds-Cdd-Cd)CbCsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)CbCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 560,
    label = "Cs-CtCtCsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Ct 0 {1,S}
3     Ct 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.57,5.98,7.51,8.37,9,9.02,8.34],"cal/(mol*K)","+|-",0.13),
        H298 = (1.16,"kcal/mol","+|-",0.26),
        S298 = (-35.26,"cal/(mol*K)","+|-",0.13),
    ),
    shortDesc = u"""Cs-CtCtCsCs BOZZELLI =3D Cs/Cs3/Ct + (Cs/Cs3/Ct - Cs/Cs4)""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 561,
    label = "Cs-CbCtCsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Ct 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.57,5.98,7.51,8.37,9,9.02,8.34],"cal/(mol*K)","+|-",0.13),
        H298 = (1.16,"kcal/mol","+|-",0.26),
        S298 = (-35.26,"cal/(mol*K)","+|-",0.13),
    ),
    shortDesc = u"""Cs-CbCtCsCs BOZZELLI =3D Cs/Cs3/Cb + (Cs/Cs3/Ct - Cs/Cs4)""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 562,
    label = "Cs-CbCbCsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Cb 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.57,5.98,7.51,8.37,9,9.02,8.34],"cal/(mol*K)","+|-",0.13),
        H298 = (1.16,"kcal/mol","+|-",0.26),
        S298 = (-35.26,"cal/(mol*K)","+|-",0.13),
    ),
    shortDesc = u"""Cs-CbCbCsCs BENSON""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 563,
    label = "Cs-CdsCdsCdsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     {Cd,CO} 0 {1,S}
3     {Cd,CO} 0 {1,S}
4     {Cd,CO} 0 {1,S}
5     Cs 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 564,
    label = "Cs-(Cds-Od)(Cds-Od)(Cds-Od)Cs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     CO 0 {1,S}
5     Cs 0 {1,S}
""",
    thermo = 'Cs-CsCsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 565,
    label = "Cs-(Cds-Od)(Cds-Od)(Cds-Cd)Cs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Cd 0 {1,S}
5     Cs 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 566,
    label = "Cs-(Cds-Od)(Cds-Od)(Cds-Cds)Cs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Cd 0 {1,S} {6,D}
5     Cs 0 {1,S}
6     Cd 0 {4,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Od)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 567,
    label = "Cs-(Cds-Od)(Cds-Od)(Cds-Cdd)Cs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Cd 0 {1,S} {6,D}
5     Cs 0 {1,S}
6     Cdd 0 {4,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Cd)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 568,
    label = "Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Od)Cs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Cd 0 {1,S} {6,D}
5     Cs 0 {1,S}
6     Cdd 0 {4,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)CsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 569,
    label = "Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Cd)Cs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Cd 0 {1,S} {6,D}
5     Cs 0 {1,S}
6     Cdd 0 {4,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 570,
    label = "Cs-(Cds-Od)(Cds-Cd)(Cds-Cd)Cs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S}
4     Cd 0 {1,S}
5     Cs 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 571,
    label = "Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Cs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Cs 0 {1,S}
6     Cd 0 {3,D}
7     Cd 0 {4,D}
""",
    thermo = 'Cs-(Cds-Od)CsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 572,
    label = "Cs-(Cds-Od)(Cds-Cdd)(Cds-Cds)Cs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Cs 0 {1,S}
6     Cdd 0 {3,D}
7     Cd 0 {4,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 573,
    label = "Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)Cs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Cs 0 {1,S}
6     Cdd 0 {3,D} {8,D}
7     Cd 0 {4,D}
8     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cdd-Od)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 574,
    label = "Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cds)Cs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Cs 0 {1,S}
6     Cdd 0 {3,D} {8,D}
7     Cd 0 {4,D}
8     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 575,
    label = "Cs-(Cds-Od)(Cds-Cdd)(Cds-Cdd)Cs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Cs 0 {1,S}
6     Cdd 0 {3,D}
7     Cdd 0 {4,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 576,
    label = "Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)Cs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Cs 0 {1,S}
6     Cdd 0 {3,D} {8,D}
7     Cdd 0 {4,D} {9,D}
8     Od 0 {6,D}
9     Od 0 {7,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 577,
    label = "Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)Cs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Cs 0 {1,S}
6     Cdd 0 {3,D} {8,D}
7     Cdd 0 {4,D} {9,D}
8     Od 0 {6,D}
9     C 0 {7,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 578,
    label = "Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Cs 0 {1,S}
6     Cdd 0 {3,D} {8,D}
7     Cdd 0 {4,D} {9,D}
8     C 0 {6,D}
9     C 0 {7,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 579,
    label = "Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)Cs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Cd 0 {1,S}
4     Cd 0 {1,S}
5     Cs 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 580,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Cs 0 {1,S}
6     Cd 0 {2,D}
7     Cd 0 {3,D}
8     Cd 0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.32,5.86,7.57,8.54,9.22,9.36,8.45],"cal/(mol*K)","+|-",0.13),
        H298 = (2.54,"kcal/mol","+|-",0.26),
        S298 = (-33.96,"cal/(mol*K)","+|-",0.13),
    ),
    shortDesc = u"""Cs-CdCdCdCs BOZZELLI =3D Cs/Cs2/Cd2 + (Cs/Cs3/Cd - Cs/Cs4)""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 581,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)Cs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Cs 0 {1,S}
6     Cd 0 {2,D}
7     Cd 0 {3,D}
8     Cdd 0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 582,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Cs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Cs 0 {1,S}
6     Cd 0 {2,D}
7     Cd 0 {3,D}
8     Cdd 0 {4,D} {9,D}
9     Od 0 {8,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)CsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 583,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)Cs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Cs 0 {1,S}
6     Cd 0 {2,D}
7     Cd 0 {3,D}
8     Cdd 0 {4,D} {9,D}
9     C 0 {8,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 584,
    label = "Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)Cs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Cs 0 {1,S}
6     Cd 0 {2,D}
7     Cdd 0 {3,D}
8     Cdd 0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 585,
    label = "Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)Cs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Cs 0 {1,S}
6     Cd 0 {2,D}
7     Cdd 0 {3,D} {9,D}
8     Cdd 0 {4,D} {10,D}
9     Od 0 {7,D}
10    Od 0 {8,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 586,
    label = "Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Cd)Cs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Cs 0 {1,S}
6     Cd 0 {2,D}
7     Cdd 0 {3,D} {9,D}
8     Cdd 0 {4,D} {10,D}
9     Od 0 {7,D}
10    C 0 {8,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 587,
    label = "Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Cs 0 {1,S}
6     Cd 0 {2,D}
7     Cdd 0 {3,D} {9,D}
8     Cdd 0 {4,D} {10,D}
9     C 0 {7,D}
10    C 0 {8,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 588,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)Cs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Cs 0 {1,S}
6     Cdd 0 {2,D}
7     Cdd 0 {3,D}
8     Cdd 0 {4,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 589,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)Cs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Cs 0 {1,S}
6     Cdd 0 {2,D} {9,D}
7     Cdd 0 {3,D} {10,D}
8     Cdd 0 {4,D} {11,D}
9     Od 0 {6,D}
10    Od 0 {7,D}
11    Od 0 {8,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 590,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)Cs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Cs 0 {1,S}
6     Cdd 0 {2,D} {9,D}
7     Cdd 0 {3,D} {10,D}
8     Cdd 0 {4,D} {11,D}
9     Od 0 {6,D}
10    Od 0 {7,D}
11    C 0 {8,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 591,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Cs 0 {1,S}
6     Cdd 0 {2,D} {9,D}
7     Cdd 0 {3,D} {10,D}
8     Cdd 0 {4,D} {11,D}
9     Od 0 {6,D}
10    C 0 {7,D}
11    C 0 {8,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 592,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Cs 0 {1,S}
6     Cdd 0 {2,D} {9,D}
7     Cdd 0 {3,D} {10,D}
8     Cdd 0 {4,D} {11,D}
9     C 0 {6,D}
10    C 0 {7,D}
11    C 0 {8,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 593,
    label = "Cs-CtCdsCdsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Ct 0 {1,S}
3     {Cd,CO} 0 {1,S}
4     {Cd,CO} 0 {1,S}
5     Cs 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CtCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 594,
    label = "Cs-(Cds-Od)(Cds-Od)CtCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Ct 0 {1,S}
5     Cs 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 595,
    label = "Cs-(Cds-Od)(Cds-Cd)CtCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S}
4     Ct 0 {1,S}
5     Cs 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)CtCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 596,
    label = "Cs-(Cds-Od)(Cds-Cds)CtCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Ct 0 {1,S}
5     Cs 0 {1,S}
6     Cd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 597,
    label = "Cs-(Cds-Od)(Cds-Cdd)CtCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Ct 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cdd-Cd)CtCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 598,
    label = "Cs-(Cds-Od)(Cds-Cdd-Od)CtCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Ct 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {3,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 599,
    label = "Cs-(Cds-Od)(Cds-Cdd-Cd)CtCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Ct 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {3,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)CtCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 600,
    label = "Cs-(Cds-Cd)(Cds-Cd)CtCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Cd 0 {1,S}
4     Ct 0 {1,S}
5     Cs 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CtCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 601,
    label = "Cs-(Cds-Cds)(Cds-Cds)CtCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Ct 0 {1,S}
5     Cs 0 {1,S}
6     Cd 0 {2,D}
7     Cd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 602,
    label = "Cs-(Cds-Cdd)(Cds-Cds)CtCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Ct 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {2,D}
7     Cd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cds)CtCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 603,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cds)CtCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Ct 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cd 0 {3,D}
8     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 604,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CtCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Ct 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cd 0 {3,D}
8     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CtCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 605,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)CtCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Ct 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {2,D}
7     Cdd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 606,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CtCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Ct 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cdd 0 {3,D} {9,D}
8     Od 0 {6,D}
9     Od 0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 607,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)CtCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Ct 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cdd 0 {3,D} {9,D}
8     Od 0 {6,D}
9     C 0 {7,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)(Cds-Cds)CtCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 608,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Ct 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cdd 0 {3,D} {9,D}
8     C 0 {6,D}
9     C 0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CtCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 609,
    label = "Cs-CbCdsCdsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     {Cd,CO} 0 {1,S}
4     {Cd,CO} 0 {1,S}
5     Cs 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CbCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 610,
    label = "Cs-(Cds-Od)(Cds-Od)CbCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Cb 0 {1,S}
5     Cs 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 611,
    label = "Cs-(Cds-Od)(Cds-Cd)CbCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S}
4     Cb 0 {1,S}
5     Cs 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)CbCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 612,
    label = "Cs-(Cds-Od)(Cds-Cds)CbCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cb 0 {1,S}
5     Cs 0 {1,S}
6     Cd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 613,
    label = "Cs-(Cds-Od)(Cds-Cdd)CbCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cb 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cdd-Cd)CbCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 614,
    label = "Cs-(Cds-Od)(Cds-Cdd-Od)CbCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cb 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {3,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 615,
    label = "Cs-(Cds-Od)(Cds-Cdd-Cd)CbCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cb 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {3,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)CbCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 616,
    label = "Cs-(Cds-Cd)(Cds-Cd)CbCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Cd 0 {1,S}
4     Cb 0 {1,S}
5     Cs 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CbCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 617,
    label = "Cs-(Cds-Cds)(Cds-Cds)CbCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cb 0 {1,S}
5     Cs 0 {1,S}
6     Cd 0 {2,D}
7     Cd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 618,
    label = "Cs-(Cds-Cdd)(Cds-Cds)CbCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cb 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {2,D}
7     Cd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cds)CbCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 619,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cds)CbCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cb 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cd 0 {3,D}
8     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 620,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CbCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cb 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cd 0 {3,D}
8     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CbCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 621,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)CbCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cb 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {2,D}
7     Cdd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 622,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CbCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cb 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cdd 0 {3,D} {9,D}
8     Od 0 {6,D}
9     Od 0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 623,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)CbCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cb 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cdd 0 {3,D} {9,D}
8     Od 0 {6,D}
9     C 0 {7,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)(Cds-Cds)CbCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 624,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cb 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cdd 0 {3,D} {9,D}
8     C 0 {6,D}
9     C 0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CbCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 625,
    label = "Cs-CtCtCdsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Ct 0 {1,S}
3     Ct 0 {1,S}
4     {Cd,CO} 0 {1,S}
5     Cs 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CtCtCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 626,
    label = "Cs-(Cds-Od)CtCtCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Ct 0 {1,S}
4     Ct 0 {1,S}
5     Cs 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 627,
    label = "Cs-(Cds-Cd)CtCtCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Ct 0 {1,S}
4     Ct 0 {1,S}
5     Cs 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CtCtCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 628,
    label = "Cs-(Cds-Cds)CtCtCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Ct 0 {1,S}
4     Ct 0 {1,S}
5     Cs 0 {1,S}
6     Cd 0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.99,7.36,8.89,9.58,9.76,9.16,7.25],"cal/(mol*K)","+|-",0.13),
        H298 = (5.1,"kcal/mol","+|-",0.26),
        S298 = (-34.88,"cal/(mol*K)","+|-",0.13),
    ),
    shortDesc = u"""Cs-CtCtCdCs BOZZELLI =3D Cs/Cd2/Cs2 + (Cs/Cs3/Ct - Cs/Cs4)""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 629,
    label = "Cs-(Cds-Cdd)CtCtCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Ct 0 {1,S}
4     Ct 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CtCtCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 630,
    label = "Cs-(Cds-Cdd-Od)CtCtCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Ct 0 {1,S}
4     Ct 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 631,
    label = "Cs-(Cds-Cdd-Cd)CtCtCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Ct 0 {1,S}
4     Ct 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)CtCtCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 632,
    label = "Cs-CbCtCdsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Ct 0 {1,S}
4     {Cd,CO} 0 {1,S}
5     Cs 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CbCtCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 633,
    label = "Cs-(Cds-Od)CbCtCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cb 0 {1,S}
4     Ct 0 {1,S}
5     Cs 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)CtCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 634,
    label = "Cs-(Cds-Cd)CbCtCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Cb 0 {1,S}
4     Ct 0 {1,S}
5     Cs 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CbCtCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 635,
    label = "Cs-(Cds-Cds)CbCtCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Ct 0 {1,S}
5     Cs 0 {1,S}
6     Cd 0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.99,7.36,8.89,9.58,9.76,9.16,7.25],"cal/(mol*K)","+|-",0.13),
        H298 = (5.1,"kcal/mol","+|-",0.26),
        S298 = (-34.88,"cal/(mol*K)","+|-",0.13),
    ),
    shortDesc = u"""Cs-CbCtCdCs BOZZELLI =3D Cs/Cb/Cd/Cs2 + (Cs/Cs3/Ct - Cs/Cs4)""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 636,
    label = "Cs-(Cds-Cdd)CbCtCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Ct 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CbCtCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 637,
    label = "Cs-(Cds-Cdd-Od)CbCtCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Ct 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)(Cds-Cds)CtCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 638,
    label = "Cs-(Cds-Cdd-Cd)CbCtCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Ct 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     C 0 {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.99,7.36,8.89,9.58,9.76,9.16,7.25],"cal/(mol*K)","+|-",0.13),
        H298 = (5.1,"kcal/mol","+|-",0.26),
        S298 = (-34.88,"cal/(mol*K)","+|-",0.13),
    ),
    shortDesc = u"""Cs-CbCtCdCs BOZZELLI =3D Cs/Cb/Cd/Cs2 + (Cs/Cs3/Ct - Cs/Cs4)""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 639,
    label = "Cs-CbCbCdsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Cb 0 {1,S}
4     {Cd,CO} 0 {1,S}
5     Cs 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CbCbCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 640,
    label = "Cs-(Cds-Od)CbCbCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cb 0 {1,S}
4     Cb 0 {1,S}
5     Cs 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 641,
    label = "Cs-(Cds-Cd)CbCbCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Cb 0 {1,S}
4     Cb 0 {1,S}
5     Cs 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CbCbCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 642,
    label = "Cs-(Cds-Cds)CbCbCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Cb 0 {1,S}
5     Cs 0 {1,S}
6     Cd 0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.99,7.36,8.89,9.58,9.76,9.16,7.25],"cal/(mol*K)","+|-",0.13),
        H298 = (5.1,"kcal/mol","+|-",0.26),
        S298 = (-34.88,"cal/(mol*K)","+|-",0.13),
    ),
    shortDesc = u"""Cs-CbCbCdCs BOZZELLI =3D Cs/Cs2/Cb2 + (Cs/Cs3/Cd - Cs/Cs4)""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 643,
    label = "Cs-(Cds-Cdd)CbCbCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Cb 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CbCbCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 644,
    label = "Cs-(Cds-Cdd-Od)CbCbCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Cb 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 645,
    label = "Cs-(Cds-Cdd-Cd)CbCbCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Cb 0 {1,S}
5     Cs 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)CbCbCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 646,
    label = "Cs-CtCtCtCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Ct 0 {1,S}
3     Ct 0 {1,S}
4     Ct 0 {1,S}
5     Cs 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.37,8.11,9.55,10.1,10.03,9.36,6.65],"cal/(mol*K)","+|-",0.13),
        H298 = (6.23,"kcal/mol","+|-",0.26),
        S298 = (-35.34,"cal/(mol*K)","+|-",0.13),
    ),
    shortDesc = u"""Cs-CtCtCtCs BOZZELLI =3D Cs/Cs2/Ct2 + (Cs/Cs3/Ct - Cs/Cs4)""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 647,
    label = "Cs-CbCtCtCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Ct 0 {1,S}
4     Ct 0 {1,S}
5     Cs 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.37,8.11,9.55,10.1,10.03,9.36,6.65],"cal/(mol*K)","+|-",0.13),
        H298 = (6.23,"kcal/mol","+|-",0.26),
        S298 = (-35.34,"cal/(mol*K)","+|-",0.13),
    ),
    shortDesc = u"""Cs-CbCtCtCs BOZZELLI =3D Cs/Cs2/Cb/Ct + (Cs/Cs3/Ct - Cs/Cs4)""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 648,
    label = "Cs-CbCbCtCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Cb 0 {1,S}
4     Ct 0 {1,S}
5     Cs 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.37,8.11,9.55,10.1,10.03,9.36,6.65],"cal/(mol*K)","+|-",0.13),
        H298 = (6.43,"kcal/mol","+|-",0.26),
        S298 = (-35.34,"cal/(mol*K)","+|-",0.13),
    ),
    shortDesc = u"""Cs-CbCbCtCs BOZZELLI =3D Cs/Cs2/Cb2 + (Cs/Cs3/Ct - Cs/Cs4)""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 649,
    label = "Cs-CbCbCbCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Cb 0 {1,S}
4     Cb 0 {1,S}
5     Cs 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.37,8.11,9.55,10.1,10.03,9.36,6.65],"cal/(mol*K)","+|-",0.13),
        H298 = (6.23,"kcal/mol","+|-",0.26),
        S298 = (-35.34,"cal/(mol*K)","+|-",0.13),
    ),
    shortDesc = u"""Cs-CbCbCbCs BOZZELLI =3D Cs/Cs2/Cb2 + (Cs/Cs3/Cb - Cs/Cs4)""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 650,
    label = "Cs-CdsCdsCdsCds",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     {Cd,CO} 0 {1,S}
3     {Cd,CO} 0 {1,S}
4     {Cd,CO} 0 {1,S}
5     {Cd,CO} 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 651,
    label = "Cs-(Cds-Od)(Cds-Od)(Cds-Od)(Cds-Od)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     CO 0 {1,S}
5     CO 0 {1,S}
""",
    thermo = 'Cs-CsCsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 652,
    label = "Cs-(Cds-Od)(Cds-Od)(Cds-Od)(Cds-Cd)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     CO 0 {1,S}
5     Cd 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Od)(Cds-Od)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 653,
    label = "Cs-(Cds-Od)(Cds-Od)(Cds-Od)(Cds-Cds)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     CO 0 {1,S}
5     Cd 0 {1,S} {6,D}
6     Cd 0 {5,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Od)(Cds-Od)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 654,
    label = "Cs-(Cds-Od)(Cds-Od)(Cds-Od)(Cds-Cdd)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     CO 0 {1,S}
5     Cd 0 {1,S} {6,D}
6     Cdd 0 {5,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Od)(Cds-Od)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 655,
    label = "Cs-(Cds-Od)(Cds-Od)(Cds-Od)(Cds-Cdd-Od)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     CO 0 {1,S}
5     Cd 0 {1,S} {6,D}
6     Cdd 0 {5,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)CsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 656,
    label = "Cs-(Cds-Od)(Cds-Od)(Cds-Od)(Cds-Cdd-Cd)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     CO 0 {1,S}
5     Cd 0 {1,S} {6,D}
6     Cdd 0 {5,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Od)(Cds-Od)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 657,
    label = "Cs-(Cds-Od)(Cds-Od)(Cds-Cd)(Cds-Cd)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Cd 0 {1,S}
5     Cd 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 658,
    label = "Cs-(Cds-Od)(Cds-Od)(Cds-Cds)(Cds-Cds)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Cd 0 {1,S} {6,D}
5     Cd 0 {1,S} {7,D}
6     Cd 0 {4,D}
7     Cd 0 {5,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Od)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 659,
    label = "Cs-(Cds-Od)(Cds-Od)(Cds-Cdd)(Cds-Cds)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Cd 0 {1,S} {6,D}
5     Cd 0 {1,S} {7,D}
6     Cdd 0 {4,D}
7     Cd 0 {5,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Cd)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 660,
    label = "Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Cd 0 {1,S} {6,D}
5     Cd 0 {1,S} {7,D}
6     Cdd 0 {4,D} {8,D}
7     Cd 0 {5,D}
8     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Od)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 661,
    label = "Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Cd)(Cds-Cds)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Cd 0 {1,S} {6,D}
5     Cd 0 {1,S} {7,D}
6     Cdd 0 {4,D} {8,D}
7     Cd 0 {5,D}
8     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 662,
    label = "Cs-(Cds-Od)(Cds-Od)(Cds-Cdd)(Cds-Cdd)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Cd 0 {1,S} {6,D}
5     Cd 0 {1,S} {7,D}
6     Cdd 0 {4,D}
7     Cdd 0 {5,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 663,
    label = "Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Cd 0 {1,S} {6,D}
5     Cd 0 {1,S} {7,D}
6     Cdd 0 {4,D} {8,D}
7     Cdd 0 {5,D} {9,D}
8     Od 0 {6,D}
9     Od 0 {7,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 664,
    label = "Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Cd 0 {1,S} {6,D}
5     Cd 0 {1,S} {7,D}
6     Cdd 0 {4,D} {8,D}
7     Cdd 0 {5,D} {9,D}
8     Od 0 {6,D}
9     C 0 {7,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 665,
    label = "Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Cd 0 {1,S} {6,D}
5     Cd 0 {1,S} {7,D}
6     Cdd 0 {4,D} {8,D}
7     Cdd 0 {5,D} {9,D}
8     C 0 {6,D}
9     C 0 {7,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 666,
    label = "Cs-(Cds-Od)(Cds-Cd)(Cds-Cd)(Cds-Cd)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S}
4     Cd 0 {1,S}
5     Cd 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 667,
    label = "Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)(Cds-Cds)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Cd 0 {1,S} {8,D}
6     Cd 0 {3,D}
7     Cd 0 {4,D}
8     Cd 0 {5,D}
""",
    thermo = 'Cs-(Cds-Od)CsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 668,
    label = "Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)(Cds-Cdd)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Cd 0 {1,S} {8,D}
6     Cd 0 {3,D}
7     Cd 0 {4,D}
8     Cdd 0 {5,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 669,
    label = "Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Cd 0 {1,S} {8,D}
6     Cd 0 {3,D}
7     Cd 0 {4,D}
8     Cdd 0 {5,D} {9,D}
9     Od 0 {8,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cdd-Od)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 670,
    label = "Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Cd 0 {1,S} {8,D}
6     Cd 0 {3,D}
7     Cd 0 {4,D}
8     Cdd 0 {5,D} {9,D}
9     C 0 {8,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 671,
    label = "Cs-(Cds-Od)(Cds-Cds)(Cds-Cdd)(Cds-Cdd)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Cd 0 {1,S} {8,D}
6     Cd 0 {3,D}
7     Cdd 0 {4,D}
8     Cdd 0 {5,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 672,
    label = "Cs-(Cds-Od)(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Cd 0 {1,S} {8,D}
6     Cd 0 {3,D}
7     Cdd 0 {4,D} {9,D}
8     Cdd 0 {5,D} {10,D}
9     Od 0 {7,D}
10    Od 0 {8,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 673,
    label = "Cs-(Cds-Od)(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Cd)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Cd 0 {1,S} {8,D}
6     Cd 0 {3,D}
7     Cdd 0 {4,D} {9,D}
8     Cdd 0 {5,D} {10,D}
9     Od 0 {7,D}
10    C 0 {8,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 674,
    label = "Cs-(Cds-Od)(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Cd 0 {1,S} {8,D}
6     Cd 0 {3,D}
7     Cdd 0 {4,D} {9,D}
8     Cdd 0 {5,D} {10,D}
9     C 0 {7,D}
10    C 0 {8,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 675,
    label = "Cs-(Cds-Od)(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Cd 0 {1,S} {8,D}
6     Cdd 0 {3,D}
7     Cdd 0 {4,D}
8     Cdd 0 {5,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 676,
    label = "Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Cd 0 {1,S} {8,D}
6     Cdd 0 {3,D} {9,D}
7     Cdd 0 {4,D} {10,D}
8     Cdd 0 {5,D} {11,D}
9     Od 0 {6,D}
10    Od 0 {7,D}
11    Od 0 {8,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 677,
    label = "Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Cd 0 {1,S} {8,D}
6     Cdd 0 {3,D} {9,D}
7     Cdd 0 {4,D} {10,D}
8     Cdd 0 {5,D} {11,D}
9     Od 0 {6,D}
10    Od 0 {7,D}
11    C 0 {8,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 678,
    label = "Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Cd 0 {1,S} {8,D}
6     Cdd 0 {3,D} {9,D}
7     Cdd 0 {4,D} {10,D}
8     Cdd 0 {5,D} {11,D}
9     Od 0 {6,D}
10    C 0 {7,D}
11    C 0 {8,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 679,
    label = "Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Cd 0 {1,S} {8,D}
6     Cdd 0 {3,D} {9,D}
7     Cdd 0 {4,D} {10,D}
8     Cdd 0 {5,D} {11,D}
9     C 0 {6,D}
10    C 0 {7,D}
11    C 0 {8,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 680,
    label = "Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)(Cds-Cd)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Cd 0 {1,S}
4     Cd 0 {1,S}
5     Cd 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 681,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Cd 0 {1,S} {9,D}
6     Cd 0 {2,D}
7     Cd 0 {3,D}
8     Cd 0 {4,D}
9     Cd 0 {5,D}
""",
    thermo = 'Cs-CsCsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 682,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Cd 0 {1,S} {9,D}
6     Cd 0 {2,D}
7     Cd 0 {3,D}
8     Cd 0 {4,D}
9     Cdd 0 {5,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 683,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Cd 0 {1,S} {9,D}
6     Cd 0 {2,D}
7     Cd 0 {3,D}
8     Cd 0 {4,D}
9     Cdd 0 {5,D} {10,D}
10    Od 0 {9,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)CsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 684,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Cd 0 {1,S} {9,D}
6     Cd 0 {2,D}
7     Cd 0 {3,D}
8     Cd 0 {4,D}
9     Cdd 0 {5,D} {10,D}
10    C 0 {9,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 685,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)(Cds-Cdd)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Cd 0 {1,S} {9,D}
6     Cd 0 {2,D}
7     Cd 0 {3,D}
8     Cdd 0 {4,D}
9     Cdd 0 {5,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 686,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Cd 0 {1,S} {9,D}
6     Cd 0 {2,D}
7     Cd 0 {3,D}
8     Cdd 0 {4,D} {10,D}
9     Cdd 0 {5,D} {11,D}
10    Od 0 {8,D}
11    Od 0 {9,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 687,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Cd)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Cd 0 {1,S} {9,D}
6     Cd 0 {2,D}
7     Cd 0 {3,D}
8     Cdd 0 {4,D} {10,D}
9     Cdd 0 {5,D} {11,D}
10    Od 0 {8,D}
11    C 0 {9,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 688,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Cd 0 {1,S} {9,D}
6     Cd 0 {2,D}
7     Cd 0 {3,D}
8     Cdd 0 {4,D} {10,D}
9     Cdd 0 {5,D} {11,D}
10    C 0 {8,D}
11    C 0 {9,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 689,
    label = "Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Cd 0 {1,S} {9,D}
6     Cd 0 {2,D}
7     Cdd 0 {3,D}
8     Cdd 0 {4,D}
9     Cdd 0 {5,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 690,
    label = "Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Cd 0 {1,S} {9,D}
6     Cd 0 {2,D}
7     Cdd 0 {3,D} {10,D}
8     Cdd 0 {4,D} {11,D}
9     Cdd 0 {5,D} {12,D}
10    Od 0 {7,D}
11    Od 0 {8,D}
12    Od 0 {9,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 691,
    label = "Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Cd 0 {1,S} {9,D}
6     Cd 0 {2,D}
7     Cdd 0 {3,D} {10,D}
8     Cdd 0 {4,D} {11,D}
9     Cdd 0 {5,D} {12,D}
10    Od 0 {7,D}
11    Od 0 {8,D}
12    C 0 {9,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 692,
    label = "Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Cd 0 {1,S} {9,D}
6     Cd 0 {2,D}
7     Cdd 0 {3,D} {10,D}
8     Cdd 0 {4,D} {11,D}
9     Cdd 0 {5,D} {12,D}
10    Od 0 {7,D}
11    C 0 {8,D}
12    C 0 {9,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 693,
    label = "Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Cd 0 {1,S} {9,D}
6     Cd 0 {2,D}
7     Cdd 0 {3,D} {10,D}
8     Cdd 0 {4,D} {11,D}
9     Cdd 0 {5,D} {12,D}
10    C 0 {7,D}
11    C 0 {8,D}
12    C 0 {9,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 694,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Cd 0 {1,S} {9,D}
6     Cdd 0 {2,D}
7     Cdd 0 {3,D}
8     Cdd 0 {4,D}
9     Cdd 0 {5,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 695,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Cd 0 {1,S} {9,D}
6     Cdd 0 {2,D} {10,D}
7     Cdd 0 {3,D} {11,D}
8     Cdd 0 {4,D} {12,D}
9     Cdd 0 {5,D} {13,D}
10    Od 0 {6,D}
11    Od 0 {7,D}
12    Od 0 {8,D}
13    Od 0 {9,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 696,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Cd 0 {1,S} {9,D}
6     Cdd 0 {2,D} {10,D}
7     Cdd 0 {3,D} {11,D}
8     Cdd 0 {4,D} {12,D}
9     Cdd 0 {5,D} {13,D}
10    Od 0 {6,D}
11    Od 0 {7,D}
12    Od 0 {8,D}
13    C 0 {9,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 697,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Cd 0 {1,S} {9,D}
6     Cdd 0 {2,D} {10,D}
7     Cdd 0 {3,D} {11,D}
8     Cdd 0 {4,D} {12,D}
9     Cdd 0 {5,D} {13,D}
10    Od 0 {6,D}
11    Od 0 {7,D}
12    C 0 {8,D}
13    C 0 {9,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 698,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Cd 0 {1,S} {9,D}
6     Cdd 0 {2,D} {10,D}
7     Cdd 0 {3,D} {11,D}
8     Cdd 0 {4,D} {12,D}
9     Cdd 0 {5,D} {13,D}
10    Od 0 {6,D}
11    C 0 {7,D}
12    C 0 {8,D}
13    C 0 {9,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 699,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Cd 0 {1,S} {9,D}
6     Cdd 0 {2,D} {10,D}
7     Cdd 0 {3,D} {11,D}
8     Cdd 0 {4,D} {12,D}
9     Cdd 0 {5,D} {13,D}
10    C 0 {6,D}
11    C 0 {7,D}
12    C 0 {8,D}
13    C 0 {9,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 700,
    label = "Cs-CtCdsCdsCds",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Ct 0 {1,S}
3     {Cd,CO} 0 {1,S}
4     {Cd,CO} 0 {1,S}
5     {Cd,CO} 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 701,
    label = "Cs-(Cds-Od)(Cds-Od)(Cds-Od)Ct",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     CO 0 {1,S}
5     Ct 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Od)(Cds-Od)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 702,
    label = "Cs-(Cds-Od)(Cds-Od)(Cds-Cd)Ct",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Cd 0 {1,S}
5     Ct 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 703,
    label = "Cs-(Cds-Od)(Cds-Od)(Cds-Cds)Ct",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Cd 0 {1,S} {6,D}
5     Ct 0 {1,S}
6     Cd 0 {4,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 704,
    label = "Cs-(Cds-Od)(Cds-Od)(Cds-Cdd)Ct",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Cd 0 {1,S} {6,D}
5     Ct 0 {1,S}
6     Cdd 0 {4,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Cd)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 705,
    label = "Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Od)Ct",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Cd 0 {1,S} {6,D}
5     Ct 0 {1,S}
6     Cdd 0 {4,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 706,
    label = "Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Cd)Ct",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Cd 0 {1,S} {6,D}
5     Ct 0 {1,S}
6     Cdd 0 {4,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 707,
    label = "Cs-(Cds-Od)(Cds-Cd)(Cds-Cd)Ct",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S}
4     Cd 0 {1,S}
5     Ct 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 708,
    label = "Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Ct",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Ct 0 {1,S}
6     Cd 0 {3,D}
7     Cd 0 {4,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 709,
    label = "Cs-(Cds-Od)(Cds-Cdd)(Cds-Cds)Ct",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Ct 0 {1,S}
6     Cdd 0 {3,D}
7     Cd 0 {4,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 710,
    label = "Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)Ct",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Ct 0 {1,S}
6     Cdd 0 {3,D} {8,D}
7     Cd 0 {4,D}
8     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 711,
    label = "Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cds)Ct",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Ct 0 {1,S}
6     Cdd 0 {3,D} {8,D}
7     Cd 0 {4,D}
8     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 712,
    label = "Cs-(Cds-Od)(Cds-Cdd)(Cds-Cdd)Ct",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Ct 0 {1,S}
6     Cdd 0 {3,D}
7     Cdd 0 {4,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 713,
    label = "Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)Ct",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Ct 0 {1,S}
6     Cdd 0 {3,D} {8,D}
7     Cdd 0 {4,D} {9,D}
8     Od 0 {6,D}
9     Od 0 {7,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 714,
    label = "Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)Ct",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Ct 0 {1,S}
6     Cdd 0 {3,D} {8,D}
7     Cdd 0 {4,D} {9,D}
8     Od 0 {6,D}
9     C 0 {7,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 715,
    label = "Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Ct 0 {1,S}
6     Cdd 0 {3,D} {8,D}
7     Cdd 0 {4,D} {9,D}
8     C 0 {6,D}
9     C 0 {7,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 716,
    label = "Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)Ct",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Cd 0 {1,S}
4     Cd 0 {1,S}
5     Ct 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 717,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Ct",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Ct 0 {1,S}
6     Cd 0 {2,D}
7     Cd 0 {3,D}
8     Cd 0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 718,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)Ct",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Ct 0 {1,S}
6     Cd 0 {2,D}
7     Cd 0 {3,D}
8     Cdd 0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 719,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Ct",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Ct 0 {1,S}
6     Cd 0 {2,D}
7     Cd 0 {3,D}
8     Cdd 0 {4,D} {9,D}
9     Od 0 {8,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 720,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)Ct",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Ct 0 {1,S}
6     Cd 0 {2,D}
7     Cd 0 {3,D}
8     Cdd 0 {4,D} {9,D}
9     C 0 {8,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 721,
    label = "Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)Ct",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Ct 0 {1,S}
6     Cd 0 {2,D}
7     Cdd 0 {3,D}
8     Cdd 0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 722,
    label = "Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)Ct",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Ct 0 {1,S}
6     Cd 0 {2,D}
7     Cdd 0 {3,D} {9,D}
8     Cdd 0 {4,D} {10,D}
9     Od 0 {7,D}
10    Od 0 {8,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 723,
    label = "Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Cd)Ct",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Ct 0 {1,S}
6     Cd 0 {2,D}
7     Cdd 0 {3,D} {9,D}
8     Cdd 0 {4,D} {10,D}
9     Od 0 {7,D}
10    C 0 {8,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 724,
    label = "Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Ct 0 {1,S}
6     Cd 0 {2,D}
7     Cdd 0 {3,D} {9,D}
8     Cdd 0 {4,D} {10,D}
9     C 0 {7,D}
10    C 0 {8,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 725,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)Ct",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Ct 0 {1,S}
6     Cdd 0 {2,D}
7     Cdd 0 {3,D}
8     Cdd 0 {4,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 726,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)Ct",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Ct 0 {1,S}
6     Cdd 0 {2,D} {9,D}
7     Cdd 0 {3,D} {10,D}
8     Cdd 0 {4,D} {11,D}
9     Od 0 {6,D}
10    Od 0 {7,D}
11    Od 0 {8,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 727,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)Ct",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Ct 0 {1,S}
6     Cdd 0 {2,D} {9,D}
7     Cdd 0 {3,D} {10,D}
8     Cdd 0 {4,D} {11,D}
9     Od 0 {6,D}
10    Od 0 {7,D}
11    C 0 {8,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 728,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Ct 0 {1,S}
6     Cdd 0 {2,D} {9,D}
7     Cdd 0 {3,D} {10,D}
8     Cdd 0 {4,D} {11,D}
9     Od 0 {6,D}
10    C 0 {7,D}
11    C 0 {8,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 729,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Ct 0 {1,S}
6     Cdd 0 {2,D} {9,D}
7     Cdd 0 {3,D} {10,D}
8     Cdd 0 {4,D} {11,D}
9     C 0 {6,D}
10    C 0 {7,D}
11    C 0 {8,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 730,
    label = "Cs-CbCdsCdsCds",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     {Cd,CO} 0 {1,S}
4     {Cd,CO} 0 {1,S}
5     {Cd,CO} 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 731,
    label = "Cs-(Cds-Od)(Cds-Od)(Cds-Od)Cb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     CO 0 {1,S}
5     Cb 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Od)(Cds-Od)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 732,
    label = "Cs-(Cds-Od)(Cds-Od)(Cds-Cd)Cb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Cd 0 {1,S}
5     Cb 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 733,
    label = "Cs-(Cds-Od)(Cds-Od)(Cds-Cds)Cb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Cd 0 {1,S} {6,D}
5     Cb 0 {1,S}
6     Cd 0 {4,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 734,
    label = "Cs-(Cds-Od)(Cds-Od)(Cds-Cdd)Cb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Cd 0 {1,S} {6,D}
5     Cb 0 {1,S}
6     Cdd 0 {4,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Cd)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 735,
    label = "Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Od)Cb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Cd 0 {1,S} {6,D}
5     Cb 0 {1,S}
6     Cdd 0 {4,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 736,
    label = "Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Cd)Cb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Cd 0 {1,S} {6,D}
5     Cb 0 {1,S}
6     Cdd 0 {4,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 737,
    label = "Cs-(Cds-Od)(Cds-Cd)(Cds-Cd)Cb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S}
4     Cd 0 {1,S}
5     Cb 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 738,
    label = "Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Cb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Cb 0 {1,S}
6     Cd 0 {3,D}
7     Cd 0 {4,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 739,
    label = "Cs-(Cds-Od)(Cds-Cdd)(Cds-Cds)Cb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Cb 0 {1,S}
6     Cdd 0 {3,D}
7     Cd 0 {4,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 740,
    label = "Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)Cb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Cb 0 {1,S}
6     Cdd 0 {3,D} {8,D}
7     Cd 0 {4,D}
8     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 741,
    label = "Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cds)Cb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Cb 0 {1,S}
6     Cdd 0 {3,D} {8,D}
7     Cd 0 {4,D}
8     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 742,
    label = "Cs-(Cds-Od)(Cds-Cdd)(Cds-Cdd)Cb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Cb 0 {1,S}
6     Cdd 0 {3,D}
7     Cdd 0 {4,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 743,
    label = "Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)Cb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Cb 0 {1,S}
6     Cdd 0 {3,D} {8,D}
7     Cdd 0 {4,D} {9,D}
8     Od 0 {6,D}
9     Od 0 {7,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 744,
    label = "Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)Cb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Cb 0 {1,S}
6     Cdd 0 {3,D} {8,D}
7     Cdd 0 {4,D} {9,D}
8     Od 0 {6,D}
9     C 0 {7,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 745,
    label = "Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Cb 0 {1,S}
6     Cdd 0 {3,D} {8,D}
7     Cdd 0 {4,D} {9,D}
8     C 0 {6,D}
9     C 0 {7,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 746,
    label = "Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)Cb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Cd 0 {1,S}
4     Cd 0 {1,S}
5     Cb 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 747,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Cb 0 {1,S}
6     Cd 0 {2,D}
7     Cd 0 {3,D}
8     Cd 0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 748,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)Cb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Cb 0 {1,S}
6     Cd 0 {2,D}
7     Cd 0 {3,D}
8     Cdd 0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 749,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Cb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Cb 0 {1,S}
6     Cd 0 {2,D}
7     Cd 0 {3,D}
8     Cdd 0 {4,D} {9,D}
9     Od 0 {8,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 750,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)Cb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Cb 0 {1,S}
6     Cd 0 {2,D}
7     Cd 0 {3,D}
8     Cdd 0 {4,D} {9,D}
9     C 0 {8,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 751,
    label = "Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)Cb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Cb 0 {1,S}
6     Cd 0 {2,D}
7     Cdd 0 {3,D}
8     Cdd 0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 752,
    label = "Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)Cb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Cb 0 {1,S}
6     Cd 0 {2,D}
7     Cdd 0 {3,D} {9,D}
8     Cdd 0 {4,D} {10,D}
9     Od 0 {7,D}
10    Od 0 {8,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 753,
    label = "Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Cd)Cb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Cb 0 {1,S}
6     Cd 0 {2,D}
7     Cdd 0 {3,D} {9,D}
8     Cdd 0 {4,D} {10,D}
9     Od 0 {7,D}
10    C 0 {8,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 754,
    label = "Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Cb 0 {1,S}
6     Cd 0 {2,D}
7     Cdd 0 {3,D} {9,D}
8     Cdd 0 {4,D} {10,D}
9     C 0 {7,D}
10    C 0 {8,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 755,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)Cb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Cb 0 {1,S}
6     Cdd 0 {2,D}
7     Cdd 0 {3,D}
8     Cdd 0 {4,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 756,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)Cb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Cb 0 {1,S}
6     Cdd 0 {2,D} {9,D}
7     Cdd 0 {3,D} {10,D}
8     Cdd 0 {4,D} {11,D}
9     Od 0 {6,D}
10    Od 0 {7,D}
11    Od 0 {8,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 757,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)Cb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Cb 0 {1,S}
6     Cdd 0 {2,D} {9,D}
7     Cdd 0 {3,D} {10,D}
8     Cdd 0 {4,D} {11,D}
9     Od 0 {6,D}
10    Od 0 {7,D}
11    C 0 {8,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 758,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Cb 0 {1,S}
6     Cdd 0 {2,D} {9,D}
7     Cdd 0 {3,D} {10,D}
8     Cdd 0 {4,D} {11,D}
9     Od 0 {6,D}
10    C 0 {7,D}
11    C 0 {8,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 759,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Cb 0 {1,S}
6     Cdd 0 {2,D} {9,D}
7     Cdd 0 {3,D} {10,D}
8     Cdd 0 {4,D} {11,D}
9     C 0 {6,D}
10    C 0 {7,D}
11    C 0 {8,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 760,
    label = "Cs-CtCtCdsCds",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Ct 0 {1,S}
3     Ct 0 {1,S}
4     {Cd,CO} 0 {1,S}
5     {Cd,CO} 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CtCt',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 761,
    label = "Cs-(Cds-Od)(Cds-Od)CtCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Ct 0 {1,S}
5     Ct 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 762,
    label = "Cs-(Cds-Od)(Cds-Cd)CtCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S}
4     Ct 0 {1,S}
5     Ct 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)CtCt',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 763,
    label = "Cs-(Cds-Od)(Cds-Cds)CtCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Ct 0 {1,S}
5     Ct 0 {1,S}
6     Cd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 764,
    label = "Cs-(Cds-Od)(Cds-Cdd)CtCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Ct 0 {1,S}
5     Ct 0 {1,S}
6     Cdd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cdd-Cd)CtCt',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 765,
    label = "Cs-(Cds-Od)(Cds-Cdd-Od)CtCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Ct 0 {1,S}
5     Ct 0 {1,S}
6     Cdd 0 {3,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 766,
    label = "Cs-(Cds-Od)(Cds-Cdd-Cd)CtCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Ct 0 {1,S}
5     Ct 0 {1,S}
6     Cdd 0 {3,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)CtCt',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 767,
    label = "Cs-(Cds-Cd)(Cds-Cd)CtCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Cd 0 {1,S}
4     Ct 0 {1,S}
5     Ct 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CtCt',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 768,
    label = "Cs-(Cds-Cds)(Cds-Cds)CtCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Ct 0 {1,S}
5     Ct 0 {1,S}
6     Cd 0 {2,D}
7     Cd 0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.61,7.3,8.97,9.69,9.84,9.42,7.36],"cal/(mol*K)","+|-",0.13),
        H298 = (5.48,"kcal/mol","+|-",0.26),
        S298 = (-34.5,"cal/(mol*K)","+|-",0.13),
    ),
    shortDesc = u"""Cs-CtCtCdCd BOZZELLI =3D Cs/Cs/Cd/Ct2 + (Cs/Cs3/Cd - Cs/Cs4)""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 769,
    label = "Cs-(Cds-Cdd)(Cds-Cds)CtCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Ct 0 {1,S}
5     Ct 0 {1,S}
6     Cdd 0 {2,D}
7     Cd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cds)CtCt',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 770,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cds)CtCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Ct 0 {1,S}
5     Ct 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cd 0 {3,D}
8     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 771,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CtCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Ct 0 {1,S}
5     Ct 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cd 0 {3,D}
8     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CtCt',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 772,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)CtCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Ct 0 {1,S}
5     Ct 0 {1,S}
6     Cdd 0 {2,D}
7     Cdd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtCt',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 773,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CtCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Ct 0 {1,S}
5     Ct 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cdd 0 {3,D} {9,D}
8     Od 0 {6,D}
9     Od 0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 774,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)CtCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Ct 0 {1,S}
5     Ct 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cdd 0 {3,D} {9,D}
8     Od 0 {6,D}
9     C 0 {7,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)(Cds-Cds)CtCt',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 775,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Ct 0 {1,S}
5     Ct 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cdd 0 {3,D} {9,D}
8     C 0 {6,D}
9     C 0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CtCt',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 776,
    label = "Cs-CbCtCdsCds",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Ct 0 {1,S}
4     {Cd,CO} 0 {1,S}
5     {Cd,CO} 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CbCt',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 777,
    label = "Cs-(Cds-Od)(Cds-Od)CbCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Cb 0 {1,S}
5     Ct 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 778,
    label = "Cs-(Cds-Od)(Cds-Cd)CbCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S}
4     Cb 0 {1,S}
5     Ct 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)CbCt',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 779,
    label = "Cs-(Cds-Od)(Cds-Cds)CbCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cb 0 {1,S}
5     Ct 0 {1,S}
6     Cd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 780,
    label = "Cs-(Cds-Od)(Cds-Cdd)CbCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cb 0 {1,S}
5     Ct 0 {1,S}
6     Cdd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cdd-Cd)CbCt',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 781,
    label = "Cs-(Cds-Od)(Cds-Cdd-Od)CbCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cb 0 {1,S}
5     Ct 0 {1,S}
6     Cdd 0 {3,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 782,
    label = "Cs-(Cds-Od)(Cds-Cdd-Cd)CbCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cb 0 {1,S}
5     Ct 0 {1,S}
6     Cdd 0 {3,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)CbCt',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 783,
    label = "Cs-(Cds-Cd)(Cds-Cd)CbCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Cd 0 {1,S}
4     Cb 0 {1,S}
5     Ct 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CbCt',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 784,
    label = "Cs-(Cds-Cds)(Cds-Cds)CbCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cb 0 {1,S}
5     Ct 0 {1,S}
6     Cd 0 {2,D}
7     Cd 0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.61,7.3,8.97,9.69,9.84,9.42,7.36],"cal/(mol*K)","+|-",0.13),
        H298 = (5.48,"kcal/mol","+|-",0.26),
        S298 = (-34.5,"cal/(mol*K)","+|-",0.13),
    ),
    shortDesc = u"""Cs-CbCtCdCd BOZZELLI =3D Cs/Cs/Cb/Cd2 + (Cs/Cs3/Ct - Cs/Cs4)""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 785,
    label = "Cs-(Cds-Cdd)(Cds-Cds)CbCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cb 0 {1,S}
5     Ct 0 {1,S}
6     Cdd 0 {2,D}
7     Cd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cds)CbCt',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 786,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cds)CbCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cb 0 {1,S}
5     Ct 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cd 0 {3,D}
8     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 787,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CbCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cb 0 {1,S}
5     Ct 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cd 0 {3,D}
8     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CbCt',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 788,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)CbCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cb 0 {1,S}
5     Ct 0 {1,S}
6     Cdd 0 {2,D}
7     Cdd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbCt',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 789,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CbCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cb 0 {1,S}
5     Ct 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cdd 0 {3,D} {9,D}
8     Od 0 {6,D}
9     Od 0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 790,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)CbCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cb 0 {1,S}
5     Ct 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cdd 0 {3,D} {9,D}
8     Od 0 {6,D}
9     C 0 {7,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)(Cds-Cds)CbCt',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 791,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cb 0 {1,S}
5     Ct 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cdd 0 {3,D} {9,D}
8     C 0 {6,D}
9     C 0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CbCt',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 792,
    label = "Cs-CbCbCdsCds",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Cb 0 {1,S}
4     {Cd,CO} 0 {1,S}
5     {Cd,CO} 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CbCb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 793,
    label = "Cs-(Cds-Od)(Cds-Od)CbCb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Cb 0 {1,S}
5     Cb 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 794,
    label = "Cs-(Cds-Od)(Cds-Cd)CbCb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S}
4     Cb 0 {1,S}
5     Cb 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)CbCb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 795,
    label = "Cs-(Cds-Od)(Cds-Cds)CbCb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cb 0 {1,S}
5     Cb 0 {1,S}
6     Cd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 796,
    label = "Cs-(Cds-Od)(Cds-Cdd)CbCb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cb 0 {1,S}
5     Cb 0 {1,S}
6     Cdd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cdd-Cd)CbCb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 797,
    label = "Cs-(Cds-Od)(Cds-Cdd-Od)CbCb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cb 0 {1,S}
5     Cb 0 {1,S}
6     Cdd 0 {3,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 798,
    label = "Cs-(Cds-Od)(Cds-Cdd-Cd)CbCb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cb 0 {1,S}
5     Cb 0 {1,S}
6     Cdd 0 {3,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)CbCb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 799,
    label = "Cs-(Cds-Cd)(Cds-Cd)CbCb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Cd 0 {1,S}
4     Cb 0 {1,S}
5     Cb 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CbCb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 800,
    label = "Cs-(Cds-Cds)(Cds-Cds)CbCb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cb 0 {1,S}
5     Cb 0 {1,S}
6     Cd 0 {2,D}
7     Cd 0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.61,7.3,8.97,9.69,9.84,9.42,7.36],"cal/(mol*K)","+|-",0.13),
        H298 = (5.48,"kcal/mol","+|-",0.26),
        S298 = (-34.5,"cal/(mol*K)","+|-",0.13),
    ),
    shortDesc = u"""Cs-CbCbCdCd BOZZELLI =3D Cs/Cs/Cb2/Cd + (Cs/Cs3/Cd - Cs/Cs4)""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 801,
    label = "Cs-(Cds-Cdd)(Cds-Cds)CbCb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cb 0 {1,S}
5     Cb 0 {1,S}
6     Cdd 0 {2,D}
7     Cd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cds)CbCb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 802,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cds)CbCb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cb 0 {1,S}
5     Cb 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cd 0 {3,D}
8     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 803,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CbCb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cb 0 {1,S}
5     Cb 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cd 0 {3,D}
8     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CbCb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 804,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)CbCb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cb 0 {1,S}
5     Cb 0 {1,S}
6     Cdd 0 {2,D}
7     Cdd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbCb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 805,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CbCb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cb 0 {1,S}
5     Cb 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cdd 0 {3,D} {9,D}
8     Od 0 {6,D}
9     Od 0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 806,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)CbCb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cb 0 {1,S}
5     Cb 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cdd 0 {3,D} {9,D}
8     Od 0 {6,D}
9     C 0 {7,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)(Cds-Cds)CbCb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 807,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbCb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cb 0 {1,S}
5     Cb 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cdd 0 {3,D} {9,D}
8     C 0 {6,D}
9     C 0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CbCb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 808,
    label = "Cs-CtCtCtCds",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Ct 0 {1,S}
3     Ct 0 {1,S}
4     Ct 0 {1,S}
5     {Cd,CO} 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CtCtCt',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 809,
    label = "Cs-(Cds-Od)CtCtCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Ct 0 {1,S}
4     Ct 0 {1,S}
5     Ct 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = -1,
    label = "Cs-(Cds-Cd)CtCtCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Ct 0 {1,S}
4     Ct 0 {1,S}
5     Ct 0 {1,S}
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
    index = 810,
    label = "Cs-(Cds-Cds)CtCtCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Ct 0 {1,S}
4     Ct 0 {1,S}
5     Ct 0 {1,S}
6     Cd 0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 811,
    label = "Cs-(Cds-Cdd)CtCtCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Ct 0 {1,S}
4     Ct 0 {1,S}
5     Ct 0 {1,S}
6     Cdd 0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CtCtCt',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 812,
    label = "Cs-(Cds-Cdd-Od)CtCtCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Ct 0 {1,S}
4     Ct 0 {1,S}
5     Ct 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 813,
    label = "Cs-(Cds-Cdd-Cd)CtCtCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Ct 0 {1,S}
4     Ct 0 {1,S}
5     Ct 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)CtCtCt',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 814,
    label = "Cs-CbCtCtCds",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Ct 0 {1,S}
4     Ct 0 {1,S}
5     {Cd,CO} 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CbCtCt',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 815,
    label = "Cs-(Cds-Od)CbCtCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cb 0 {1,S}
4     Ct 0 {1,S}
5     Ct 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)CtCt',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 816,
    label = "Cs-(Cds-Cd)CbCtCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Cb 0 {1,S}
4     Ct 0 {1,S}
5     Ct 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CbCtCt',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 817,
    label = "Cs-(Cds-Cds)CbCtCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Ct 0 {1,S}
5     Ct 0 {1,S}
6     Cd 0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CtCt',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 818,
    label = "Cs-(Cds-Cdd)CbCtCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Ct 0 {1,S}
5     Ct 0 {1,S}
6     Cdd 0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CbCtCt',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 819,
    label = "Cs-(Cds-Cdd-Od)CbCtCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Ct 0 {1,S}
5     Ct 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)(Cds-Cds)CtCt',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 820,
    label = "Cs-(Cds-Cdd-Cd)CbCtCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Ct 0 {1,S}
5     Ct 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)CbCtCt',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 821,
    label = "Cs-CbCbCtCds",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Cb 0 {1,S}
4     Ct 0 {1,S}
5     {Cd,CO} 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CbCbCt',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 822,
    label = "Cs-(Cds-Od)CbCbCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cb 0 {1,S}
4     Cb 0 {1,S}
5     Ct 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 823,
    label = "Cs-(Cds-Cd)CbCbCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Cb 0 {1,S}
4     Cb 0 {1,S}
5     Ct 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CbCbCt',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 824,
    label = "Cs-(Cds-Cds)CbCbCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Cb 0 {1,S}
5     Ct 0 {1,S}
6     Cd 0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 825,
    label = "Cs-(Cds-Cdd)CbCbCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Cb 0 {1,S}
5     Ct 0 {1,S}
6     Cdd 0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CbCbCt',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 826,
    label = "Cs-(Cds-Cdd-Od)CbCbCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Cb 0 {1,S}
5     Ct 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 827,
    label = "Cs-(Cds-Cdd-Cd)CbCbCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Cb 0 {1,S}
5     Ct 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)CbCbCt',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 828,
    label = "Cs-CbCbCbCds",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Cb 0 {1,S}
4     Cb 0 {1,S}
5     {Cd,CO} 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CbCbCb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 829,
    label = "Cs-(Cds-Od)CbCbCb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cb 0 {1,S}
4     Cb 0 {1,S}
5     Cb 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 830,
    label = "Cs-(Cds-Cd)CbCbCb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Cb 0 {1,S}
4     Cb 0 {1,S}
5     Cb 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CbCbCb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 831,
    label = "Cs-(Cds-Cds)CbCbCb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Cb 0 {1,S}
5     Cb 0 {1,S}
6     Cd 0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 832,
    label = "Cs-(Cds-Cdd)CbCbCb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Cb 0 {1,S}
5     Cb 0 {1,S}
6     Cdd 0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CbCbCb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 833,
    label = "Cs-(Cds-Cdd-Od)CbCbCb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Cb 0 {1,S}
5     Cb 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 834,
    label = "Cs-(Cds-Cdd-Cd)CbCbCb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Cb 0 {1,S}
5     Cb 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)CbCbCb',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 835,
    label = "Cs-CtCtCtCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Ct 0 {1,S}
3     Ct 0 {1,S}
4     Ct 0 {1,S}
5     Ct 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 836,
    label = "Cs-CbCtCtCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Ct 0 {1,S}
4     Ct 0 {1,S}
5     Ct 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CtCtCt',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 837,
    label = "Cs-CbCbCtCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Cb 0 {1,S}
4     Ct 0 {1,S}
5     Ct 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CtCt',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 838,
    label = "Cs-CbCbCbCt",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Cb 0 {1,S}
4     Cb 0 {1,S}
5     Ct 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 839,
    label = "Cs-CbCbCbCb",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Cb 0 {1,S}
4     Cb 0 {1,S}
5     Cb 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 840,
    label = "Cs-CCCOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 {1,S}
3     C 0 {1,S}
4     C 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-CsCsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 841,
    label = "Cs-CsCsCsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cs 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.33,6.19,7.25,7.7,8.2,8.24,8.24],"cal/(mol*K)","+|-",0.2),
        H298 = (-6.6,"kcal/mol","+|-",0.4),
        S298 = (-33.56,"cal/(mol*K)","+|-",0.2),
    ),
    shortDesc = u"""Cs-OCsCsCs BENSON !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 842,
    label = "Cs-CdsCsCsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     {Cd,CO} 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 843,
    label = "Cs-(Cds-Od)CsCsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.99,6.04,7.43,8.26,8.92,8.96,8.23],"cal/(mol*K)","+|-",0.2),
        H298 = (-3.6,"kcal/mol","+|-",0.4),
        S298 = (-34.72,"cal/(mol*K)","+|-",0.2),
    ),
    shortDesc = u"""Cs-OCOCsCs Hf BENSON S,Cp =3D C/Cd/C3""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 844,
    label = "Cs-(Cds-Cd)CsCsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 845,
    label = "Cs-(Cds-Cds)CsCsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Os 0 {1,S}
6     Cd 0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.63,6.79,7.95,8.4,8.8,8.44,8.44],"cal/(mol*K)","+|-",0.2),
        H298 = (-6.6,"kcal/mol","+|-",0.4),
        S298 = (-32.56,"cal/(mol*K)","+|-",0.2),
    ),
    shortDesc = u"""Cs-OCdCsCs BOZZELLI C/C3/O - (C/C3/H - C/Cb/C2/H), Hf-1 !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 846,
    label = "Cs-(Cds-Cdd)CsCsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 847,
    label = "Cs-(Cds-Cdd-Od)CsCsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([8.39,9.66,10.03,10.07,9.64,9.26,8.74],"cal/(mol*K)","+|-",0.2),
        H298 = (-9.725,"kcal/mol","+|-",0.4),
        S298 = (-36.5,"cal/(mol*K)","+|-",0.2),
    ),
    shortDesc = u"""{C/CCO/O/C2} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 848,
    label = "Cs-(Cds-Cdd-Cd)CsCsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)CsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 849,
    label = "Cs-OsCtCsCs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Os 0 {1,S}
3     Ct 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 850,
    label = "Cs-CbCsCsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.63,6.79,7.95,8.4,8.8,8.44,8.44],"cal/(mol*K)","+|-",0.2),
        H298 = (-6.6,"kcal/mol","+|-",0.4),
        S298 = (-32.56,"cal/(mol*K)","+|-",0.2),
    ),
    shortDesc = u"""Cs-OCbCsCs BOZZELLI C/C3/O - (C/C3/H - C/Cb/C2/H), Hf-1 !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 851,
    label = "Cs-CdsCdsCsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     {Cd,CO} 0 {1,S}
3     {Cd,CO} 0 {1,S}
4     Cs 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 852,
    label = "Cs-(Cds-Od)(Cds-Od)CsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Cs 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-CsCsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 853,
    label = "Cs-(Cds-Od)(Cds-Cd)CsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S}
4     Cs 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 854,
    label = "Cs-(Cds-Od)(Cds-Cds)CsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cs 0 {1,S}
5     Os 0 {1,S}
6     Cd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Od)CsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 855,
    label = "Cs-(Cds-Od)(Cds-Cdd)CsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cs 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cdd-Cd)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 856,
    label = "Cs-(Cds-Od)(Cds-Cdd-Od)CsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cs 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {3,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)CsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 857,
    label = "Cs-(Cds-Od)(Cds-Cdd-Cd)CsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cs 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {3,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 858,
    label = "Cs-(Cds-Cd)(Cds-Cd)CsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Cd 0 {1,S}
4     Cs 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 859,
    label = "Cs-(Cds-Cds)(Cds-Cds)CsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cs 0 {1,S}
5     Os 0 {1,S}
6     Cd 0 {2,D}
7     Cd 0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.61,5.98,7.51,8.37,9,9.02,8.34],"cal/(mol*K)","+|-",0.2),
        H298 = (-8.01,"kcal/mol","+|-",0.4),
        S298 = (-34.34,"cal/(mol*K)","+|-",0.2),
    ),
    shortDesc = u"""Cs-OCdCdCs Hf jwb 697 S,Cp from C/Cd2/C2""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 860,
    label = "Cs-(Cds-Cdd)(Cds-Cds)CsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cs 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D}
7     Cd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 861,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cds)CsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cs 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cd 0 {3,D}
8     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)CsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 862,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cs 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cd 0 {3,D}
8     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 863,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)CsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cs 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D}
7     Cdd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 864,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cs 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cdd 0 {3,D} {9,D}
8     Od 0 {6,D}
9     Od 0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 865,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)CsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cs 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cdd 0 {3,D} {9,D}
8     Od 0 {6,D}
9     C 0 {7,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 866,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cs 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cdd 0 {3,D} {9,D}
8     C 0 {6,D}
9     C 0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 867,
    label = "Cs-CtCdsCsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Ct 0 {1,S}
3     {Cd,CO} 0 {1,S}
4     Cs 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CtCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 868,
    label = "Cs-(Cds-Od)CtCsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Ct 0 {1,S}
4     Cs 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 869,
    label = "Cs-(Cds-Cd)CtCsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Ct 0 {1,S}
4     Cs 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CtCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 870,
    label = "Cs-(Cds-Cds)CtCsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Ct 0 {1,S}
4     Cs 0 {1,S}
5     Os 0 {1,S}
6     Cd 0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 871,
    label = "Cs-(Cds-Cdd)CtCsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Ct 0 {1,S}
4     Cs 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CtCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 872,
    label = "Cs-(Cds-Cdd-Od)CtCsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Ct 0 {1,S}
4     Cs 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 873,
    label = "Cs-(Cds-Cdd-Cd)CtCsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Ct 0 {1,S}
4     Cs 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)CtCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 874,
    label = "Cs-CbCdsCsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     {Cd,CO} 0 {1,S}
4     Cs 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CbCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 875,
    label = "Cs-(Cds-Od)CbCsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cb 0 {1,S}
4     Cs 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 876,
    label = "Cs-(Cds-Cd)CbCsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Cb 0 {1,S}
4     Cs 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CbCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 877,
    label = "Cs-(Cds-Cds)CbCsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Cs 0 {1,S}
5     Os 0 {1,S}
6     Cd 0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 878,
    label = "Cs-(Cds-Cdd)CbCsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Cs 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CbCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 879,
    label = "Cs-(Cds-Cdd-Od)CbCsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Cs 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 880,
    label = "Cs-(Cds-Cdd-Cd)CbCsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Cs 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)CbCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 881,
    label = "Cs-CtCtCsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Ct 0 {1,S}
3     Ct 0 {1,S}
4     Cs 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 882,
    label = "Cs-CbCtCsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Ct 0 {1,S}
4     Cs 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CtCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 883,
    label = "Cs-CbCbCsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Cb 0 {1,S}
4     Cs 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 884,
    label = "Cs-CdsCdsCdsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     {Cd,CO} 0 {1,S}
3     {Cd,CO} 0 {1,S}
4     {Cd,CO} 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 885,
    label = "Cs-(Cds-Od)(Cds-Od)(Cds-Od)Os",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     CO 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-CsCsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 886,
    label = "Cs-(Cds-Od)(Cds-Od)(Cds-Cd)Os",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Cd 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 887,
    label = "Cs-(Cds-Od)(Cds-Od)(Cds-Cds)Os",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Cd 0 {1,S} {6,D}
5     Os 0 {1,S}
6     Cd 0 {4,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Od)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 888,
    label = "Cs-(Cds-Od)(Cds-Od)(Cds-Cdd)Os",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Cd 0 {1,S} {6,D}
5     Os 0 {1,S}
6     Cdd 0 {4,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Cd)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 889,
    label = "Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Od)Os",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Cd 0 {1,S} {6,D}
5     Os 0 {1,S}
6     Cdd 0 {4,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)CsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 890,
    label = "Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Cd)Os",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Cd 0 {1,S} {6,D}
5     Os 0 {1,S}
6     Cdd 0 {4,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 891,
    label = "Cs-(Cds-Od)(Cds-Cd)(Cds-Cd)Os",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S}
4     Cd 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 892,
    label = "Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Os",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Os 0 {1,S}
6     Cd 0 {3,D}
7     Cd 0 {4,D}
""",
    thermo = 'Cs-(Cds-Od)CsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 893,
    label = "Cs-(Cds-Od)(Cds-Cdd)(Cds-Cds)Os",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Os 0 {1,S}
6     Cdd 0 {3,D}
7     Cd 0 {4,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 894,
    label = "Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)Os",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Os 0 {1,S}
6     Cdd 0 {3,D} {8,D}
7     Cd 0 {4,D}
8     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cdd-Od)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 895,
    label = "Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cds)Os",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Os 0 {1,S}
6     Cdd 0 {3,D} {8,D}
7     Cd 0 {4,D}
8     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 896,
    label = "Cs-(Cds-Od)(Cds-Cdd)(Cds-Cdd)Os",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Os 0 {1,S}
6     Cdd 0 {3,D}
7     Cdd 0 {4,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 897,
    label = "Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)Os",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Os 0 {1,S}
6     Cdd 0 {3,D} {8,D}
7     Cdd 0 {4,D} {9,D}
8     Od 0 {6,D}
9     Od 0 {7,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 898,
    label = "Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)Os",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Os 0 {1,S}
6     Cdd 0 {3,D} {8,D}
7     Cdd 0 {4,D} {9,D}
8     Od 0 {6,D}
9     C 0 {7,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 899,
    label = "Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Os",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cd 0 {1,S} {7,D}
5     Os 0 {1,S}
6     Cdd 0 {3,D} {8,D}
7     Cdd 0 {4,D} {9,D}
8     C 0 {6,D}
9     C 0 {7,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 900,
    label = "Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)Os",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Cd 0 {1,S}
4     Cd 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 901,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Os",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Os 0 {1,S}
6     Cd 0 {2,D}
7     Cd 0 {3,D}
8     Cd 0 {4,D}
""",
    thermo = 'Cs-CsCsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 902,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)Os",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Os 0 {1,S}
6     Cd 0 {2,D}
7     Cd 0 {3,D}
8     Cdd 0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 903,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Os",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Os 0 {1,S}
6     Cd 0 {2,D}
7     Cd 0 {3,D}
8     Cdd 0 {4,D} {9,D}
9     Od 0 {8,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)CsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 904,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)Os",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Os 0 {1,S}
6     Cd 0 {2,D}
7     Cd 0 {3,D}
8     Cdd 0 {4,D} {9,D}
9     C 0 {8,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 905,
    label = "Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)Os",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Os 0 {1,S}
6     Cd 0 {2,D}
7     Cdd 0 {3,D}
8     Cdd 0 {4,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 906,
    label = "Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)Os",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Os 0 {1,S}
6     Cd 0 {2,D}
7     Cdd 0 {3,D} {9,D}
8     Cdd 0 {4,D} {10,D}
9     Od 0 {7,D}
10    Od 0 {8,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 907,
    label = "Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Cd)Os",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Os 0 {1,S}
6     Cd 0 {2,D}
7     Cdd 0 {3,D} {9,D}
8     Cdd 0 {4,D} {10,D}
9     Od 0 {7,D}
10    C 0 {8,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 908,
    label = "Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Os",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Os 0 {1,S}
6     Cd 0 {2,D}
7     Cdd 0 {3,D} {9,D}
8     Cdd 0 {4,D} {10,D}
9     C 0 {7,D}
10    C 0 {8,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 909,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)Os",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Os 0 {1,S}
6     Cdd 0 {2,D}
7     Cdd 0 {3,D}
8     Cdd 0 {4,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 910,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)Os",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Os 0 {1,S}
6     Cdd 0 {2,D} {9,D}
7     Cdd 0 {3,D} {10,D}
8     Cdd 0 {4,D} {11,D}
9     Od 0 {6,D}
10    Od 0 {7,D}
11    Od 0 {8,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 911,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)Os",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Os 0 {1,S}
6     Cdd 0 {2,D} {9,D}
7     Cdd 0 {3,D} {10,D}
8     Cdd 0 {4,D} {11,D}
9     Od 0 {6,D}
10    Od 0 {7,D}
11    C 0 {8,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 912,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Os",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Os 0 {1,S}
6     Cdd 0 {2,D} {9,D}
7     Cdd 0 {3,D} {10,D}
8     Cdd 0 {4,D} {11,D}
9     Od 0 {6,D}
10    C 0 {7,D}
11    C 0 {8,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 913,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Os",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cd 0 {1,S} {8,D}
5     Os 0 {1,S}
6     Cdd 0 {2,D} {9,D}
7     Cdd 0 {3,D} {10,D}
8     Cdd 0 {4,D} {11,D}
9     C 0 {6,D}
10    C 0 {7,D}
11    C 0 {8,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 914,
    label = "Cs-CtCdsCdsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Ct 0 {1,S}
3     {Cd,CO} 0 {1,S}
4     {Cd,CO} 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CtOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 915,
    label = "Cs-(Cds-Od)(Cds-Od)CtOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Ct 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 916,
    label = "Cs-(Cds-Od)(Cds-Cd)CtOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S}
4     Ct 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)CtOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 917,
    label = "Cs-(Cds-Od)(Cds-Cds)CtOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Ct 0 {1,S}
5     Os 0 {1,S}
6     Cd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 918,
    label = "Cs-(Cds-Od)(Cds-Cdd)CtOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Ct 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cdd-Cd)CtOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 919,
    label = "Cs-(Cds-Od)(Cds-Cdd-Od)CtOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Ct 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {3,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 920,
    label = "Cs-(Cds-Od)(Cds-Cdd-Cd)CtOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Ct 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {3,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)CtOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 921,
    label = "Cs-(Cds-Cd)(Cds-Cd)CtOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Cd 0 {1,S}
4     Ct 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CtOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 922,
    label = "Cs-(Cds-Cds)(Cds-Cds)CtOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Ct 0 {1,S}
5     Os 0 {1,S}
6     Cd 0 {2,D}
7     Cd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 923,
    label = "Cs-(Cds-Cdd)(Cds-Cds)CtOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Ct 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D}
7     Cd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cds)CtOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 924,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cds)CtOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Ct 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cd 0 {3,D}
8     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 925,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CtOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Ct 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cd 0 {3,D}
8     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CtOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 926,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)CtOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Ct 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D}
7     Cdd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 927,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CtOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Ct 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cdd 0 {3,D} {9,D}
8     Od 0 {6,D}
9     Od 0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 928,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)CtOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Ct 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cdd 0 {3,D} {9,D}
8     Od 0 {6,D}
9     C 0 {7,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)(Cds-Cds)CtOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 929,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Ct 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cdd 0 {3,D} {9,D}
8     C 0 {6,D}
9     C 0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CtOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 930,
    label = "Cs-CbCdsCdsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     {Cd,CO} 0 {1,S}
4     {Cd,CO} 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CbOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 931,
    label = "Cs-(Cds-Od)(Cds-Od)CbOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Cb 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 932,
    label = "Cs-(Cds-Od)(Cds-Cd)CbOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S}
4     Cb 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)CbOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 933,
    label = "Cs-(Cds-Od)(Cds-Cds)CbOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cb 0 {1,S}
5     Os 0 {1,S}
6     Cd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 934,
    label = "Cs-(Cds-Od)(Cds-Cdd)CbOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cb 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cdd-Cd)CbOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 935,
    label = "Cs-(Cds-Od)(Cds-Cdd-Od)CbOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cb 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {3,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 936,
    label = "Cs-(Cds-Od)(Cds-Cdd-Cd)CbOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Cb 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {3,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)CbOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 937,
    label = "Cs-(Cds-Cd)(Cds-Cd)CbOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Cd 0 {1,S}
4     Cb 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CbOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 938,
    label = "Cs-(Cds-Cds)(Cds-Cds)CbOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cb 0 {1,S}
5     Os 0 {1,S}
6     Cd 0 {2,D}
7     Cd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 939,
    label = "Cs-(Cds-Cdd)(Cds-Cds)CbOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cb 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D}
7     Cd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cds)CbOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 940,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cds)CbOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cb 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cd 0 {3,D}
8     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 941,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CbOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cb 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cd 0 {3,D}
8     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CbOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 942,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)CbOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cb 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D}
7     Cdd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 943,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CbOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cb 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cdd 0 {3,D} {9,D}
8     Od 0 {6,D}
9     Od 0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 944,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)CbOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cb 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cdd 0 {3,D} {9,D}
8     Od 0 {6,D}
9     C 0 {7,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)(Cds-Cds)CbOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 945,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Cb 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cdd 0 {3,D} {9,D}
8     C 0 {6,D}
9     C 0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CbOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 946,
    label = "Cs-CtCtCdsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Ct 0 {1,S}
3     Ct 0 {1,S}
4     {Cd,CO} 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CtCtOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 947,
    label = "Cs-(Cds-Od)CtCtOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Ct 0 {1,S}
4     Ct 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 948,
    label = "Cs-(Cds-Cd)CtCtOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Ct 0 {1,S}
4     Ct 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CtCtOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 949,
    label = "Cs-(Cds-Cds)CtCtOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Ct 0 {1,S}
4     Ct 0 {1,S}
5     Os 0 {1,S}
6     Cd 0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 950,
    label = "Cs-(Cds-Cdd)CtCtOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Ct 0 {1,S}
4     Ct 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CtCtOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 951,
    label = "Cs-(Cds-Cdd-Od)CtCtOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Ct 0 {1,S}
4     Ct 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 952,
    label = "Cs-(Cds-Cdd-Cd)CtCtOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Ct 0 {1,S}
4     Ct 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)CtCtOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 953,
    label = "Cs-CbCtCdsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Ct 0 {1,S}
4     {Cd,CO} 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CbCtOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 954,
    label = "Cs-(Cds-Od)CbCtOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cb 0 {1,S}
4     Ct 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)CtOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 955,
    label = "Cs-(Cds-Cd)CbCtOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Cb 0 {1,S}
4     Ct 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CbCtOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 956,
    label = "Cs-(Cds-Cds)CbCtOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Ct 0 {1,S}
5     Os 0 {1,S}
6     Cd 0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CtOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 957,
    label = "Cs-(Cds-Cdd)CbCtOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Ct 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CbCtOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 958,
    label = "Cs-(Cds-Cdd-Od)CbCtOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Ct 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)(Cds-Cds)CtOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 959,
    label = "Cs-(Cds-Cdd-Cd)CbCtOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Ct 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)CbCtOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 960,
    label = "Cs-CbCbCdsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Cb 0 {1,S}
4     {Cd,CO} 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CbCbOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 961,
    label = "Cs-(Cds-Od)CbCbOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cb 0 {1,S}
4     Cb 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 962,
    label = "Cs-(Cds-Cd)CbCbOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Cb 0 {1,S}
4     Cb 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CbCbOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 963,
    label = "Cs-(Cds-Cds)CbCbOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Cb 0 {1,S}
5     Os 0 {1,S}
6     Cd 0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 964,
    label = "Cs-(Cds-Cdd)CbCbOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Cb 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CbCbOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 965,
    label = "Cs-(Cds-Cdd-Od)CbCbOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Cb 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 966,
    label = "Cs-(Cds-Cdd-Cd)CbCbOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Cb 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)CbCbOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 967,
    label = "Cs-CtCtCtOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Ct 0 {1,S}
3     Ct 0 {1,S}
4     Ct 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 968,
    label = "Cs-CbCtCtOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Ct 0 {1,S}
4     Ct 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CtCtOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 969,
    label = "Cs-CbCbCtOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Cb 0 {1,S}
4     Ct 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)CtOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 970,
    label = "Cs-CbCbCbOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Cb 0 {1,S}
4     Cb 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 971,
    label = "Cs-CCOsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 {1,S}
3     C 0 {1,S}
4     Os 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-CsCsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 972,
    label = "Cs-CsCsOsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cs 0 {1,S}
3     Cs 0 {1,S}
4     Os 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.8,6.09,7.3,7.78,8.24,8.24,8.24],"cal/(mol*K)","+|-",0.2),
        H298 = (-9.77,"kcal/mol","+|-",0.4),
        S298 = (-33.18,"cal/(mol*K)","+|-",0.2),
    ),
    shortDesc = u"""Cs-OOCsCs BOZZELLI =3D C/C3/O - (C/C2/H2 - C/C/H2/O) !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 973,
    label = "Cs-CdsCsOsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     {Cd,CO} 0 {1,S}
3     Cs 0 {1,S}
4     Os 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 974,
    label = "Cs-(Cds-Od)CsOsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cs 0 {1,S}
4     Os 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-CsCsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 975,
    label = "Cs-(Cds-Cd)CsOsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Cs 0 {1,S}
4     Os 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 976,
    label = "Cs-(Cds-Cds)CsOsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cs 0 {1,S}
4     Os 0 {1,S}
5     Os 0 {1,S}
6     Cd 0 {2,D}
""",
    thermo = 'Cs-CsCsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 977,
    label = "Cs-(Cds-Cdd)CsOsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cs 0 {1,S}
4     Os 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 978,
    label = "Cs-(Cds-Cdd-Od)CsOsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cs 0 {1,S}
4     Os 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)CsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 979,
    label = "Cs-(Cds-Cdd-Cd)CsOsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cs 0 {1,S}
4     Os 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)CsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 980,
    label = "Cs-CdsCdsOsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     {Cd,CO} 0 {1,S}
3     {Cd,CO} 0 {1,S}
4     Os 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 981,
    label = "Cs-(Cds-Od)(Cds-Od)OsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Os 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-CsCsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 982,
    label = "Cs-(Cds-Od)(Cds-Cd)OsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S}
4     Os 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 983,
    label = "Cs-(Cds-Od)(Cds-Cds)OsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Os 0 {1,S}
5     Os 0 {1,S}
6     Cd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Od)CsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 984,
    label = "Cs-(Cds-Od)(Cds-Cdd)OsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Os 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cdd-Cd)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 985,
    label = "Cs-(Cds-Od)(Cds-Cdd-Od)OsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Os 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {3,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)CsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 986,
    label = "Cs-(Cds-Od)(Cds-Cdd-Cd)OsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Os 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {3,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 987,
    label = "Cs-(Cds-Cd)(Cds-Cd)OsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Cd 0 {1,S}
4     Os 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 988,
    label = "Cs-(Cds-Cds)(Cds-Cds)OsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Os 0 {1,S}
5     Os 0 {1,S}
6     Cd 0 {2,D}
7     Cd 0 {3,D}
""",
    thermo = 'Cs-CsCsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 989,
    label = "Cs-(Cds-Cdd)(Cds-Cds)OsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Os 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D}
7     Cd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 990,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cds)OsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Os 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cd 0 {3,D}
8     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)CsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 991,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)OsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Os 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cd 0 {3,D}
8     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 992,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)OsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Os 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D}
7     Cdd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 993,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)OsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Os 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cdd 0 {3,D} {9,D}
8     Od 0 {6,D}
9     Od 0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 994,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)OsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Os 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cdd 0 {3,D} {9,D}
8     Od 0 {6,D}
9     C 0 {7,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 995,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)OsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Os 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cdd 0 {3,D} {9,D}
8     C 0 {6,D}
9     C 0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 996,
    label = "Cs-CtCsOsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Ct 0 {1,S}
3     Cs 0 {1,S}
4     Os 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 997,
    label = "Cs-CtCdsOsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Ct 0 {1,S}
3     {Cd,CO} 0 {1,S}
4     Os 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CtOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 998,
    label = "Cs-(Cds-Od)CtOsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Ct 0 {1,S}
4     Os 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 999,
    label = "Cs-(Cds-Cd)CtOsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Ct 0 {1,S}
4     Os 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CtOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1000,
    label = "Cs-(Cds-Cds)CtOsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Ct 0 {1,S}
4     Os 0 {1,S}
5     Os 0 {1,S}
6     Cd 0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1001,
    label = "Cs-(Cds-Cdd)CtOsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Ct 0 {1,S}
4     Os 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CtOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1002,
    label = "Cs-(Cds-Cdd-Od)CtOsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Ct 0 {1,S}
4     Os 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1003,
    label = "Cs-(Cds-Cdd-Cd)CtOsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Ct 0 {1,S}
4     Os 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)CtOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1004,
    label = "Cs-CtCtOsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Ct 0 {1,S}
3     Ct 0 {1,S}
4     Os 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1005,
    label = "Cs-CbCsOsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Cs 0 {1,S}
4     Os 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1006,
    label = "Cs-CbCdsOsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     {Cd,CO} 0 {1,S}
4     Os 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CbOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1007,
    label = "Cs-(Cds-Od)CbOsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cb 0 {1,S}
4     Os 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1008,
    label = "Cs-(Cds-Cd)CbOsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Cb 0 {1,S}
4     Os 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CbOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1009,
    label = "Cs-(Cds-Cds)CbOsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Os 0 {1,S}
5     Os 0 {1,S}
6     Cd 0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1010,
    label = "Cs-(Cds-Cdd)CbOsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Os 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CbOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1011,
    label = "Cs-(Cds-Cdd-Od)CbOsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Os 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1012,
    label = "Cs-(Cds-Cdd-Cd)CbOsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Os 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)CbOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1013,
    label = "Cs-CbCtOsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Ct 0 {1,S}
4     Os 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CtOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1014,
    label = "Cs-CbCbOsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Cb 0 {1,S}
4     Os 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1015,
    label = "Cs-COsOsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 {1,S}
3     Os 0 {1,S}
4     Os 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-CsOsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1016,
    label = "Cs-CsOsOsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cs 0 {1,S}
3     Os 0 {1,S}
4     Os 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.33,6.19,7.25,7.7,8.2,8.24,8.24],"cal/(mol*K)","+|-",0.2),
        H298 = (-19,"kcal/mol","+|-",0.4),
        S298 = (-33.56,"cal/(mol*K)","+|-",0.2),
    ),
    shortDesc = u"""Cs-OOOCs BOZZELLI est !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1017,
    label = "Cs-CdsOsOsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     {Cd,CO} 0 {1,S}
3     Os 0 {1,S}
4     Os 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)OsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1018,
    label = "Cs-(Cds-Od)OsOsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Os 0 {1,S}
4     Os 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-CsOsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1019,
    label = "Cs-(Cds-Cd)OsOsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Os 0 {1,S}
4     Os 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)OsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1020,
    label = "Cs-(Cds-Cds)OsOsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Os 0 {1,S}
4     Os 0 {1,S}
5     Os 0 {1,S}
6     Cd 0 {2,D}
""",
    thermo = 'Cs-CsOsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1021,
    label = "Cs-(Cds-Cdd)OsOsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Os 0 {1,S}
4     Os 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)OsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1022,
    label = "Cs-(Cds-Cdd-Od)OsOsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Os 0 {1,S}
4     Os 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)OsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1023,
    label = "Cs-(Cds-Cdd-Cd)OsOsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Os 0 {1,S}
4     Os 0 {1,S}
5     Os 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)OsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1024,
    label = "Cs-CtOsOsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Ct 0 {1,S}
3     Os 0 {1,S}
4     Os 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)OsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1025,
    label = "Cs-CbOsOsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Os 0 {1,S}
4     Os 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)OsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1026,
    label = "Cs-OsOsOsOs",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Os 0 {1,S}
3     Os 0 {1,S}
4     Os 0 {1,S}
5     Os 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.33,6.13,7.25,7.7,8.2,8.24,8.24],"cal/(mol*K)","+|-",0.2),
        H298 = (-23,"kcal/mol","+|-",0.4),
        S298 = (-35.56,"cal/(mol*K)","+|-",0.2),
    ),
    shortDesc = u"""Cs-OOOO BOZZELLI est !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1027,
    label = "Cs-COsOsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 {1,S}
3     Os 0 {1,S}
4     Os 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-CsOsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1028,
    label = "Cs-CsOsOsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cs 0 {1,S}
3     Os 0 {1,S}
4     Os 0 {1,S}
5     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([5.25,7.1,8.81,9.55,10.31,11.05,11.05],"cal/(mol*K)","+|-",0.12),
        H298 = (-16,"kcal/mol","+|-",0.24),
        S298 = (-12.07,"cal/(mol*K)","+|-",0.12),
    ),
    shortDesc = u"""Cs-OOCsH BENSON Hf, BOZZELLI C/C3/H - C/C2/O/H !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1029,
    label = "Cs-CdsOsOsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     {Cd,CO} 0 {1,S}
3     Os 0 {1,S}
4     Os 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)OsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1030,
    label = "Cs-(Cds-Od)OsOsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Os 0 {1,S}
4     Os 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-CsOsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1031,
    label = "Cs-(Cds-Cd)OsOsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Os 0 {1,S}
4     Os 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)OsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1032,
    label = "Cs-(Cds-Cds)OsOsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Os 0 {1,S}
4     Os 0 {1,S}
5     H 0 {1,S}
6     Cd 0 {2,D}
""",
    thermo = 'Cs-CsOsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1033,
    label = "Cs-(Cds-Cdd)OsOsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Os 0 {1,S}
4     Os 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)OsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1034,
    label = "Cs-(Cds-Cdd-Od)OsOsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Os 0 {1,S}
4     Os 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)OsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1035,
    label = "Cs-(Cds-Cdd-Cd)OsOsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Os 0 {1,S}
4     Os 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)OsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1036,
    label = "Cs-CtOsOsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Ct 0 {1,S}
3     Os 0 {1,S}
4     Os 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)OsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1037,
    label = "Cs-CbOsOsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Os 0 {1,S}
4     Os 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)OsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1038,
    label = "Cs-CCOsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 {1,S}
3     C 0 {1,S}
4     Os 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-CsCsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1039,
    label = "Cs-CsCsOsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cs 0 {1,S}
3     Cs 0 {1,S}
4     Os 0 {1,S}
5     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.8,6.64,8.1,8.73,9.81,10.4,11.51],"cal/(mol*K)","+|-",0.12),
        H298 = (-7.2,"kcal/mol","+|-",0.24),
        S298 = (-11,"cal/(mol*K)","+|-",0.12),
    ),
    shortDesc = u"""Cs-OCsCs BENSON: Cp1500 =3D Cp1000*(Cp1500/Cp1000: C/C2Cd/H)""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1040,
    label = "Cs-CdsCsOsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     {Cd,CO} 0 {1,S}
3     Cs 0 {1,S}
4     Os 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1041,
    label = "Cs-(Cds-Od)CsOsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cs 0 {1,S}
4     Os 0 {1,S}
5     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.47,6.82,8.45,9.17,10.24,10.8,11.02],"cal/(mol*K)","+|-",0.12),
        H298 = (-6,"kcal/mol","+|-",0.24),
        S298 = (-11.1,"cal/(mol*K)","+|-",0.12),
    ),
    shortDesc = u"""Cs-OCOCsH BOZZELLI""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1042,
    label = "Cs-(Cds-Cd)CsOsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Cs 0 {1,S}
4     Os 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1043,
    label = "Cs-(Cds-Cds)CsOsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cs 0 {1,S}
4     Os 0 {1,S}
5     H 0 {1,S}
6     Cd 0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.47,6.82,8.45,9.17,10.24,10.8,11.02],"cal/(mol*K)","+|-",0.12),
        H298 = (-6,"kcal/mol","+|-",0.24),
        S298 = (-11.1,"cal/(mol*K)","+|-",0.12),
    ),
    shortDesc = u"""Cs-OCdCsH BOZZELLI""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1044,
    label = "Cs-(Cds-Cdd)CsOsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cs 0 {1,S}
4     Os 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1045,
    label = "Cs-(Cds-Cdd-Od)CsOsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cs 0 {1,S}
4     Os 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([7.2,8.49,9.33,9.92,10.5,10.92,11.71],"cal/(mol*K)","+|-",0.12),
        H298 = (-8.37,"kcal/mol","+|-",0.24),
        S298 = (-13.04,"cal/(mol*K)","+|-",0.12),
    ),
    shortDesc = u"""{C/CCO/O/C/H} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1046,
    label = "Cs-(Cds-Cdd-Cd)CsOsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cs 0 {1,S}
4     Os 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)CsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1047,
    label = "Cs-CdsCdsOsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     {Cd,CO} 0 {1,S}
3     {Cd,CO} 0 {1,S}
4     Os 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1048,
    label = "Cs-(Cds-Od)(Cds-Od)OsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
4     Os 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-CsCsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1049,
    label = "Cs-(Cds-Od)(Cds-Cd)OsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S}
4     Os 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1050,
    label = "Cs-(Cds-Od)(Cds-Cds)OsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Os 0 {1,S}
5     H 0 {1,S}
6     Cd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Od)CsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1051,
    label = "Cs-(Cds-Od)(Cds-Cdd)OsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Os 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cdd-Cd)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1052,
    label = "Cs-(Cds-Od)(Cds-Cdd-Od)OsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Os 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {3,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)CsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1053,
    label = "Cs-(Cds-Od)(Cds-Cdd-Cd)OsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cd 0 {1,S} {6,D}
4     Os 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {3,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1054,
    label = "Cs-(Cds-Cd)(Cds-Cd)OsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Cd 0 {1,S}
4     Os 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1055,
    label = "Cs-(Cds-Cds)(Cds-Cds)OsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Os 0 {1,S}
5     H 0 {1,S}
6     Cd 0 {2,D}
7     Cd 0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.21,6.6,8.26,9.05,10.23,10.86,11.04],"cal/(mol*K)","+|-",0.12),
        H298 = (-6.67,"kcal/mol","+|-",0.24),
        S298 = (-10.42,"cal/(mol*K)","+|-",0.12),
    ),
    shortDesc = u"""Cs-OCdCdH BOZZELLI""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1056,
    label = "Cs-(Cds-Cdd)(Cds-Cds)OsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Os 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D}
7     Cd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1057,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cds)OsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Os 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cd 0 {3,D}
8     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)CsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1058,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cds)OsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Os 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cd 0 {3,D}
8     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1059,
    label = "Cs-(Cds-Cdd)(Cds-Cdd)OsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Os 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D}
7     Cdd 0 {3,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1060,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)OsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Os 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cdd 0 {3,D} {9,D}
8     Od 0 {6,D}
9     Od 0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1061,
    label = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)OsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Os 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cdd 0 {3,D} {9,D}
8     Od 0 {6,D}
9     C 0 {7,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1062,
    label = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)OsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cd 0 {1,S} {7,D}
4     Os 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {8,D}
7     Cdd 0 {3,D} {9,D}
8     C 0 {6,D}
9     C 0 {7,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1063,
    label = "Cs-CtCsOsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Ct 0 {1,S}
3     Cs 0 {1,S}
4     Os 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1064,
    label = "Cs-CtCdsOsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Ct 0 {1,S}
3     {Cd,CO} 0 {1,S}
4     Os 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CtOsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1065,
    label = "Cs-(Cds-Od)CtOsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Ct 0 {1,S}
4     Os 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1066,
    label = "Cs-(Cds-Cd)CtOsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Ct 0 {1,S}
4     Os 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CtOsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1067,
    label = "Cs-(Cds-Cds)CtOsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Ct 0 {1,S}
4     Os 0 {1,S}
5     H 0 {1,S}
6     Cd 0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1068,
    label = "Cs-(Cds-Cdd)CtOsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Ct 0 {1,S}
4     Os 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CtOsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1069,
    label = "Cs-(Cds-Cdd-Od)CtOsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Ct 0 {1,S}
4     Os 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1070,
    label = "Cs-(Cds-Cdd-Cd)CtOsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Ct 0 {1,S}
4     Os 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)CtOsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1071,
    label = "Cs-CtCtOsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Ct 0 {1,S}
3     Ct 0 {1,S}
4     Os 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1072,
    label = "Cs-CbCsOsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Cs 0 {1,S}
4     Os 0 {1,S}
5     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.47,6.82,8.45,9.17,10.24,10.8,11.02],"cal/(mol*K)","+|-",0.12),
        H298 = (-6,"kcal/mol","+|-",0.24),
        S298 = (-11.1,"cal/(mol*K)","+|-",0.12),
    ),
    shortDesc = u"""Cs-OCbCsH BOZZELLI =3D C/Cd/C/H/O Jul 91""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1073,
    label = "Cs-CbCdsOsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     {Cd,CO} 0 {1,S}
4     Os 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CbOsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1074,
    label = "Cs-(Cds-Od)CbOsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Cb 0 {1,S}
4     Os 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Od)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1075,
    label = "Cs-(Cds-Cd)CbOsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Cb 0 {1,S}
4     Os 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CbOsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1076,
    label = "Cs-(Cds-Cds)CbOsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Os 0 {1,S}
5     H 0 {1,S}
6     Cd 0 {2,D}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1077,
    label = "Cs-(Cds-Cdd)CbOsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Os 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)CbOsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1078,
    label = "Cs-(Cds-Cdd-Od)CbOsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Os 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cdd-Od)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1079,
    label = "Cs-(Cds-Cdd-Cd)CbOsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Cb 0 {1,S}
4     Os 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)CbOsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1080,
    label = "Cs-CbCtOsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Ct 0 {1,S}
4     Os 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)CtOsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1081,
    label = "Cs-CbCbOsH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Cb 0 {1,S}
4     Os 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1082,
    label = "Cs-COsHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 {1,S}
3     Os 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-CsOsHH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1083,
    label = "Cs-CsOsHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cs 0 {1,S}
3     Os 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.99,6.85,8.3,9.43,11.11,12.33,12.33],"cal/(mol*K)","+|-",0.1),
        H298 = (-8.1,"kcal/mol","+|-",0.2),
        S298 = (9.8,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""Cs-OCsHH BENSON !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1084,
    label = "Cs-CdsOsHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     {Cd,CO} 0 {1,S}
3     Os 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)OsHH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1085,
    label = "Cs-(Cds-Od)OsHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     CO 0 {1,S}
3     Os 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([2.95,6.74,8.53,9.8,11.61,12.65,14.4],"cal/(mol*K)","+|-",0.1),
        H298 = (-5.28,"kcal/mol","+|-",0.2),
        S298 = (10.17,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""Cs-OCOHH jwl 99 cdsQ cc*ocq""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1086,
    label = "Cs-(Cds-Cd)OsHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S}
3     Os 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)OsHH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1087,
    label = "Cs-(Cds-Cds)OsHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Os 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     Cd 0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([5.12,6.86,8.32,9.49,11.22,12.48,14.4],"cal/(mol*K)","+|-",0.1),
        H298 = (-6.76,"kcal/mol","+|-",0.2),
        S298 = (9.8,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""Cs-OCdHH BOZZELLI Hf PEDLEY c*ccoh C/C/Cd/H2""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1088,
    label = "Cs-(Cds-Cdd)OsHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Os 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D}
""",
    thermo = 'Cs-(Cds-Cdd-Cd)OsHH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1089,
    label = "Cs-(Cds-Cdd-Od)OsHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Os 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     Od 0 {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([7.15,8.67,9.75,10.65,11.93,12.97,14.86],"cal/(mol*K)","+|-",0.1),
        H298 = (-8.68,"kcal/mol","+|-",0.2),
        S298 = (8.43,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""{C/CCO/O/H2} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1090,
    label = "Cs-(Cds-Cdd-Cd)OsHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cd 0 {1,S} {6,D}
3     Os 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     Cdd 0 {2,D} {7,D}
7     C 0 {6,D}
""",
    thermo = 'Cs-(Cds-Cds)OsHH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1091,
    label = "Cs-CtOsHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Ct 0 {1,S}
3     Os 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([5.12,6.86,8.32,9.49,11.22,12.48,14.4],"cal/(mol*K)","+|-",0.1),
        H298 = (-6.76,"kcal/mol","+|-",0.2),
        S298 = (9.8,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""Cs-OCtHH BOZZELLI assigned C/Cd/H2/O""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1092,
    label = "Cs-CbOsHH",
    group = 
"""
1  *  Cs 0 {2,S} {3,S} {4,S} {5,S}
2     Cb 0 {1,S}
3     Os 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    thermo = 'Cs-(Cds-Cds)OsHH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1093,
    label = "O",
    group = 
"""
1  *  O 0
""",
    thermo = 'Os-CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1094,
    label = "Od",
    group = 
"""
1  *  Od 0
""",
    thermo = 'Od-Cd',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1095,
    label = "Od-Cd",
    group = 
"""
1  *  Od 0 {2,D}
2     {Cd,CO} 0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    shortDesc = u"""In this case the C is treated as the central atom""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1096,
    label = "Od-Od",
    group = 
"""
1  *  Od 0 {2,D}
2     Od 0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.5,3.61,3.72,3.825,4.035,4.175,4.36],"cal/(mol*K)"),
        H298 = (0,"kcal/mol","+|-",0.001),
        S298 = (25.19,"cal/(mol*K)"),
    ),
    shortDesc = u"""O2 Kee et al., SAND87-8215B, 1994", we cut it half to account for adding two single Od groups, also the symmetric number is considered too. S(group) = (S(o2) + Rln(sigma))/2""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1097,
    label = "Os",
    group = 
"""
1  *  Os 0
""",
    thermo = 'Os-(Cds-Cd)(Cds-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1098,
    label = "Os-HH",
    group = 
"""
1  *  Os 0 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([8.03,8.19,8.42,8.68,9.26,9.86,11.26],"cal/(mol*K)"),
        H298 = (-57.8,"kcal/mol","+|-",0.01),
        S298 = (46.51,"cal/(mol*K)","+|-",0.002),
    ),
    shortDesc = u"""O-HH WATER. !!!Using NIST value for H2O, S(group) = S(H2O) + Rln(2)""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1099,
    label = "Os-OsH",
    group = 
"""
1  *  Os 0 {2,S} {3,S}
2     Os 0 {1,S}
3     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([5.21,5.72,6.17,6.66,7.15,7.61,8.43],"cal/(mol*K)","+|-",0.07),
        H298 = (-16.3,"kcal/mol","+|-",0.14),
        S298 = (27.83,"cal/(mol*K)","+|-",0.07),
    ),
    shortDesc = u"""O-OH SANDIA 1/2*H2O2""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1100,
    label = "Os-OsOs",
    group = 
"""
1  *  Os 0 {2,S} {3,S}
2     Os 0 {1,S}
3     Os 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([2.2,3.64,4.2,4.34,4.62,4.9,4.9],"cal/(mol*K)","+|-",0.1),
        H298 = (8.85,"kcal/mol","+|-",0.16),
        S298 = (9.4,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""O-OO LAY 1997=20 !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1101,
    label = "Os-CH",
    group = 
"""
1  *  Os 0 {2,S} {3,S}
2     C 0 {1,S}
3     H 0 {1,S}
""",
    thermo = 'Os-CsH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1102,
    label = "Os-CtH",
    group = 
"""
1  *  Os 0 {2,S} {3,S}
2     Ct 0 {1,S}
3     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.3,4.5,4.82,5.23,6.02,6.61,7.44],"cal/(mol*K)","+|-",0.1),
        H298 = (-37.9,"kcal/mol","+|-",0.16),
        S298 = (29.1,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""O-CtH BENSON (Assigned O-CsH)""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1103,
    label = "Os-CdsH",
    group = 
"""
1  *  Os 0 {2,S} {3,S}
2     {Cd,CO} 0 {1,S}
3     H 0 {1,S}
""",
    thermo = 'Os-(Cds-Cd)H',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1104,
    label = "Os-(Cds-Od)H",
    group = 
"""
1  *  Os 0 {2,S} {3,S}
2     CO 0 {1,S}
3     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.8,5,5.8,6.3,7.2,7.8,7.8],"cal/(mol*K)","+|-",0.1),
        H298 = (-58.1,"kcal/mol","+|-",0.16),
        S298 = (24.5,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""O-COH !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1105,
    label = "Os-(Cds-Cd)H",
    group = 
"""
1  *  Os 0 {2,S} {3,S}
2     Cd 0 {1,S}
3     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.3,4.5,4.82,5.23,6.02,6.61,7.44],"cal/(mol*K)","+|-",0.1),
        H298 = (-37.9,"kcal/mol","+|-",0.16),
        S298 = (29.1,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""O-CdH BENSON (Assigned O-CsH)""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1106,
    label = "Os-CsH",
    group = 
"""
1  *  Os 0 {2,S} {3,S}
2     Cs 0 {1,S}
3     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.3,4.5,4.82,5.23,6.02,6.61,7.44],"cal/(mol*K)","+|-",0.1),
        H298 = (-37.9,"kcal/mol","+|-",0.2),
        S298 = (29.07,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""O-CsH BENSON""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1107,
    label = "Os-CbH",
    group = 
"""
1  *  Os 0 {2,S} {3,S}
2     Cb 0 {1,S}
3     H 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.3,4.5,4.82,5.23,6.02,6.61,7.44],"cal/(mol*K)","+|-",0.1),
        H298 = (-37.9,"kcal/mol","+|-",0.16),
        S298 = (29.1,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""O-CbH BENSON (Assigned O-CsH)""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1108,
    label = "Os-OsC",
    group = 
"""
1  *  Os 0 {2,S} {3,S}
2     Os 0 {1,S}
3     C 0 {1,S}
""",
    thermo = 'Os-OsCs',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1109,
    label = "Os-OsCt",
    group = 
"""
1  *  Os 0 {2,S} {3,S}
2     Os 0 {1,S}
3     Ct 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.9,4.31,4.6,4.84,5.32,5.8,5.8],"cal/(mol*K)","+|-",0.15),
        H298 = (7,"kcal/mol","+|-",0.3),
        S298 = (10.8,"cal/(mol*K)","+|-",0.15),
    ),
    shortDesc = u"""O-OCb Hf JWB plot S,Cp assigned O/O/Cd !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1110,
    label = "Os-OsCds",
    group = 
"""
1  *  Os 0 {2,S} {3,S}
2     Os 0 {1,S}
3     {Cd,CO} 0 {1,S}
""",
    thermo = 'Os-Os(Cds-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1111,
    label = "Os-Os(Cds-Od)",
    group = 
"""
1  *  Os 0 {2,S} {3,S}
2     Os 0 {1,S}
3     CO 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.53,5.02,5.79,6.08,6.54,6.49,6.49],"cal/(mol*K)","+|-",0.15),
        H298 = (-23.22,"kcal/mol","+|-",0.3),
        S298 = (9.11,"cal/(mol*K)","+|-",0.15),
    ),
    shortDesc = u"""O-OCO jwl cbsQ 99 cqcho=20 !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1112,
    label = "Os-Os(Cds-Cd)",
    group = 
"""
1  *  Os 0 {2,S} {3,S}
2     Os 0 {1,S}
3     Cd 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.5,3.87,3.95,4.15,4.73,4.89,4.89],"cal/(mol*K)","+|-",0.15),
        H298 = (1.64,"kcal/mol","+|-",0.3),
        S298 = (10.12,"cal/(mol*K)","+|-",0.15),
    ),
    shortDesc = u"""O-OCd WESTMORELAND S,Cp LAY'9405 !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1113,
    label = "Os-OsCs",
    group = 
"""
1  *  Os 0 {2,S} {3,S}
2     Os 0 {1,S}
3     Cs 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.9,4.31,4.6,4.84,5.32,5.8,5.8],"cal/(mol*K)","+|-",0.15),
        H298 = (-5.4,"kcal/mol","+|-",0.3),
        S298 = (8.54,"cal/(mol*K)","+|-",0.15),
    ),
    shortDesc = u"""O-OCs LAY 1997 !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1114,
    label = "Os-OsCb",
    group = 
"""
1  *  Os 0 {2,S} {3,S}
2     Os 0 {1,S}
3     Cb 0 {1,S}
""",
    thermo = 'Os-Os(Cds-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1115,
    label = "Os-CC",
    group = 
"""
1  *  Os 0 {2,S} {3,S}
2     C 0 {1,S}
3     C 0 {1,S}
""",
    thermo = 'Os-(Cds-Cd)(Cds-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1116,
    label = "Os-CtCt",
    group = 
"""
1  *  Os 0 {2,S} {3,S}
2     Ct 0 {1,S}
3     Ct 0 {1,S}
""",
    thermo = 'Os-(Cds-Cd)(Cds-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1117,
    label = "Os-CtCds",
    group = 
"""
1  *  Os 0 {2,S} {3,S}
2     Ct 0 {1,S}
3     {Cd,CO} 0 {1,S}
""",
    thermo = 'Os-(Cds-Cd)(Cds-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1118,
    label = "Os-Ct(Cds-Od)",
    group = 
"""
1  *  Os 0 {2,S} {3,S}
2     Ct 0 {1,S}
3     CO 0 {1,S}
""",
    thermo = 'Os-(Cds-Cd)(Cds-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1119,
    label = "Os-Ct(Cds-Cd)",
    group = 
"""
1  *  Os 0 {2,S} {3,S}
2     Ct 0 {1,S}
3     Cd 0 {1,S}
""",
    thermo = 'Os-(Cds-Cd)(Cds-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1120,
    label = "Os-CtCs",
    group = 
"""
1  *  Os 0 {2,S} {3,S}
2     Ct 0 {1,S}
3     Cs 0 {1,S}
""",
    thermo = 'Os-Cs(Cds-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1121,
    label = "Os-CtCb",
    group = 
"""
1  *  Os 0 {2,S} {3,S}
2     Ct 0 {1,S}
3     Cb 0 {1,S}
""",
    thermo = 'Os-(Cds-Cd)(Cds-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1122,
    label = "Os-CdsCds",
    group = 
"""
1  *  Os 0 {2,S} {3,S}
2     {Cd,CO} 0 {1,S}
3     {Cd,CO} 0 {1,S}
""",
    thermo = 'Os-(Cds-Cd)(Cds-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1123,
    label = "Os-(Cds-Od)(Cds-Od)",
    group = 
"""
1  *  Os 0 {2,S} {3,S}
2     CO 0 {1,S}
3     CO 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.45,4.74,5.28,5.74,5.89,6.1,6.1],"cal/(mol*K)","+|-",0.1),
        H298 = (-46,"kcal/mol","+|-",0.19),
        S298 = (2.5,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""O-COCO Hf BENSON S,Cp Mopac=3D""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1124,
    label = "Os-(Cds-Od)(Cds-Cd)",
    group = 
"""
1  *  Os 0 {2,S} {3,S}
2     CO 0 {1,S}
3     Cd 0 {1,S}
""",
    thermo = 'Os-(Cds-Cd)(Cds-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1125,
    label = "Os-(Cds-Cd)(Cds-Cd)",
    group = 
"""
1  *  Os 0 {2,S} {3,S}
2     Cd 0 {1,S}
3     Cd 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.4,3.7,3.7,3.8,4.4,4.6,4.8],"cal/(mol*K)","+|-",0.1),
        H298 = (-19.61,"kcal/mol","+|-",0.19),
        S298 = (10,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""O-CdCd BOZZELLI""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1126,
    label = "Os-CdsCs",
    group = 
"""
1  *  Os 0 {2,S} {3,S}
2     {Cd,CO} 0 {1,S}
3     Cs 0 {1,S}
""",
    thermo = 'Os-Cs(Cds-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1127,
    label = "Os-Cs(Cds-Od)",
    group = 
"""
1  *  Os 0 {2,S} {3,S}
2     Cs 0 {1,S}
3     CO 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.91,4.31,4.6,4.84,5.32,5.8,5.8],"cal/(mol*K)","+|-",0.1),
        H298 = (-42.19,"kcal/mol","+|-",0.19),
        S298 = (8.4,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""O-COCs BOZZELLI Jul91 S,Cp ABaldwin O/Cs/O !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1128,
    label = "Os-Cs(Cds-Cd)",
    group = 
"""
1  *  Os 0 {2,S} {3,S}
2     Cs 0 {1,S}
3     Cd 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.91,4.31,4.6,4.84,5.32,5.8,5.8],"cal/(mol*K)","+|-",0.1),
        H298 = (-23.73,"kcal/mol","+|-",0.19),
        S298 = (9.7,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""O-CdCs Hf RADOM vin-oh S A.Baldwin O/Cs/O !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = -1,
    label = "Os-CdsCb",
    group = 
"""
1  *  Os 0 {2,S} {3,S}
2     {Cd,CO} 0 {1,S}
3     Cb 0 {1,S}
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
    index = -1,
    label = "Os-Cb(Cds-Od)",
    group = 
"""
1  *  Os 0 {2,S} {3,S}
2     Cb 0 {1,S}
3     CO 0 {1,S}
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
    index = -1,
    label = "Os-Cb(Cds-Cd)",
    group = 
"""
1  *  Os 0 {2,S} {3,S}
2     Cb 0 {1,S}
3     Cd 0 {1,S}
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
    index = 1129,
    label = "Os-CsCs",
    group = 
"""
1  *  Os 0 {2,S} {3,S}
2     Cs 0 {1,S}
3     Cs 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.4,3.7,3.7,3.8,4.4,4.6,4.6],"cal/(mol*K)","+|-",0.1),
        H298 = (-23.2,"kcal/mol","+|-",0.19),
        S298 = (8.68,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""O-CsCs BENSON !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1130,
    label = "Os-CsCb",
    group = 
"""
1  *  Os 0 {2,S} {3,S}
2     Cs 0 {1,S}
3     Cb 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([3.4,3.7,3.7,3.8,4.4,4.6,4.6],"cal/(mol*K)","+|-",0.1),
        H298 = (-22.6,"kcal/mol","+|-",0.19),
        S298 = (9.7,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""O-CbCs REID, PRAUSNITZ and SHERWOOD !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1131,
    label = "Os-CbCb",
    group = 
"""
1  *  Os 0 {2,S} {3,S}
2     Cb 0 {1,S}
3     Cb 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([1.19,-0.24,-0.72,-0.51,0.43,1.36,1.75],"cal/(mol*K)","+|-",0.1),
        H298 = (-18.77,"kcal/mol","+|-",0.19),
        S298 = (13.59,"cal/(mol*K)","+|-",0.1),
    ),
    shortDesc = u"""O-CbCb CHERN 1/97 Hf PEDLEY, Mopac""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1132,
    label = "Si",
    group = 
"""
1  *  Si 0
""",
    thermo = 'Cs-HHHH',
    shortDesc = u"""""",
    longDesc = 
u"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1133,
    label = "S",
    group = 
"""
1  *  S 0
""",
    thermo = 'Os-HH',
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
L1: R
    L2: C
        L3: Cbf
            L4: Cbf-CbCbCbf
            L4: Cbf-CbCbfCbf
            L4: Cbf-CbfCbfCbf
        L3: Cb
            L4: Cb-H
            L4: Cb-Os
            L4: Cb-C
                L5: Cb-Cs
                L5: Cb-Cds
                    L6: Cb-(Cds-Od)
                    L6: Cb-(Cds-Cd)
                        L7: Cb-(Cds-Cds)
                        L7: Cb-(Cds-Cdd)
                            L8: Cb-(Cds-Cdd-Od)
                            L8: Cb-(Cds-Cdd-Cd)
                L5: Cb-Ct
                L5: Cb-Cb
        L3: Ct
            L4: Ct-H
            L4: Ct-Os
            L4: Ct-C
                L5: Ct-Cs
                L5: Ct-Cds
                    L6: Ct-(Cds-Od)
                    L6: Ct-(Cds-Cd)
                        L7: Ct-(Cds-Cds)
                        L7: Ct-(Cds-Cdd)
                            L8: Ct-(Cds-Cdd-Od)
                            L8: Ct-(Cds-Cdd-Cd)
                L5: Ct-Ct
                L5: Ct-Cb
        L3: Cdd
            L4: Cdd-OdOd
            L4: Cdd-CdOd
                L5: Cdd-CdsOd
                L5: Cdd-CddOd
                    L6: Cdd-(Cdd-Od)Od
                    L6: Cdd-(Cdd-Cd)Od
            L4: Cdd-CdCd
                L5: Cdd-CddCdd
                    L6: Cdd-(Cdd-Od)(Cdd-Od)
                    L6: Cdd-(Cdd-Od)(Cdd-Cd)
                    L6: Cdd-(Cdd-Cd)(Cdd-Cd)
                L5: Cdd-CddCds
                    L6: Cdd-(Cdd-Od)Cds
                    L6: Cdd-(Cdd-Cd)Cds
                L5: Cdd-CdsCds
        L3: Cds
            L4: Cds-OdHH
            L4: Cds-OdOsH
            L4: Cds-OdOsOs
            L4: Cds-OdCH
                L5: Cds-OdCsH
                L5: Cds-OdCdsH
                    L6: Cds-Od(Cds-Od)H
                    L6: Cds-Od(Cds-Cd)H
                        L7: Cds-Od(Cds-Cds)H
                        L7: Cds-Od(Cds-Cdd)H
                            L8: Cds-Od(Cds-Cdd-Od)H
                            L8: Cds-Od(Cds-Cdd-Cd)H
                L5: Cds-OdCtH
                L5: Cds-OdCbH
            L4: Cds-OdCOs
                L5: Cds-OdCsOs
                L5: Cds-OdCdsOs
                    L6: Cds-Od(Cds-Od)Os
                    L6: Cds-Od(Cds-Cd)Os
                        L7: Cds-Od(Cds-Cds)Os
                        L7: Cds-Od(Cds-Cdd)Os
                            L8: Cds-Od(Cds-Cdd-Od)Os
                            L8: Cds-Od(Cds-Cdd-Cd)Os
                L5: Cds-OdCtOs
                L5: Cds-OdCbOs
            L4: Cds-OdCC
                L5: Cds-OdCsCs
                L5: Cds-OdCdsCs
                    L6: Cds-Od(Cds-Od)Cs
                    L6: Cds-Od(Cds-Cd)Cs
                        L7: Cds-Od(Cds-Cds)Cs
                        L7: Cds-Od(Cds-Cdd)Cs
                            L8: Cds-Od(Cds-Cdd-Od)Cs
                            L8: Cds-Od(Cds-Cdd-Cd)Cs
                L5: Cds-OdCdsCds
                    L6: Cds-Od(Cds-Od)(Cds-Od)
                    L6: Cds-Od(Cds-Cd)(Cds-Od)
                        L7: Cds-Od(Cds-Cds)(Cds-Od)
                        L7: Cds-Od(Cds-Cdd)(Cds-Od)
                            L8: Cds-Od(Cds-Cdd-Od)(Cds-Od)
                            L8: Cds-Od(Cds-Cdd-Cd)(Cds-Od)
                    L6: Cds-Od(Cds-Cd)(Cds-Cd)
                        L7: Cds-Od(Cds-Cds)(Cds-Cds)
                        L7: Cds-Od(Cds-Cdd)(Cds-Cds)
                            L8: Cds-Od(Cds-Cdd-Od)(Cds-Cds)
                            L8: Cds-Od(Cds-Cdd-Cd)(Cds-Cds)
                        L7: Cds-Od(Cds-Cdd)(Cds-Cdd)
                            L8: Cds-Od(Cds-Cdd-Od)(Cds-Cdd-Od)
                            L8: Cds-Od(Cds-Cdd-Cd)(Cds-Cdd-Od)
                            L8: Cds-Od(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                L5: Cds-OdCtCs
                L5: Cds-OdCtCds
                    L6: Cds-OdCt(Cds-Od)
                    L6: Cds-OdCt(Cds-Cd)
                        L7: Cds-OdCt(Cds-Cds)
                        L7: Cds-OdCt(Cds-Cdd)
                            L8: Cds-OdCt(Cds-Cdd-Od)
                            L8: Cds-OdCt(Cds-Cdd-Cd)
                L5: Cds-OdCtCt
                L5: Cds-OdCbCs
                L5: Cds-OdCbCds
                    L6: Cds-OdCb(Cds-Od)
                    L6: Cds-OdCb(Cds-Cd)
                        L7: Cds-OdCb(Cds-Cds)
                        L7: Cds-OdCb(Cds-Cdd)
                            L8: Cds-OdCb(Cds-Cdd-Od)
                            L8: Cds-OdCb(Cds-Cdd-Cd)
                L5: Cds-OdCbCt
                L5: Cds-OdCbCb
            L4: Cds-CdHH
                L5: Cds-CdsHH
                L5: Cds-CddHH
                    L6: Cds-(Cdd-Od)HH
                    L6: Cds-(Cdd-Cd)HH
            L4: Cds-CdOsH
                L5: Cds-CdsOsH
                L5: Cds-CddOsH
                    L6: Cds-(Cdd-Od)OsH
                    L6: Cds-(Cdd-Cd)OsH
            L4: Cds-CdOsOs
                L5: Cds-CdsOsOs
                L5: Cds-CddOsOs
                    L6: Cds-(Cdd-Od)OsOs
                    L6: Cds-(Cdd-Cd)OsOs
            L4: Cds-CdCH
                L5: Cds-CdsCsH
                L5: Cds-CdsCdsH
                    L6: Cds-Cds(Cds-Od)H
                    L6: Cds-Cds(Cds-Cd)H
                        L7: Cds-Cds(Cds-Cds)H
                        L7: Cds-Cds(Cds-Cdd)H
                            L8: Cds-Cds(Cds-Cdd-Od)H
                            L8: Cds-Cds(Cds-Cdd-Cd)H
                L5: Cds-CdsCtH
                L5: Cds-CdsCbH
                L5: Cds-CddCsH
                    L6: Cds-(Cdd-Od)CsH
                    L6: Cds-(Cdd-Cd)CsH
                L5: Cds-CddCdsH
                    L6: Cds-(Cdd-Od)(Cds-Od)H
                    L6: Cds-(Cdd-Od)(Cds-Cd)H
                        L7: Cds-(Cdd-Od)(Cds-Cds)H
                        L7: Cds-(Cdd-Od)(Cds-Cdd)H
                            L8: Cds-(Cdd-Od)(Cds-Cdd-Od)H
                            L8: Cds-(Cdd-Od)(Cds-Cdd-Cd)H
                    L6: Cds-(Cdd-Cd)(Cds-Od)H
                    L6: Cds-(Cdd-Cd)(Cds-Cd)H
                        L7: Cds-(Cdd-Cd)(Cds-Cds)H
                        L7: Cds-(Cdd-Cd)(Cds-Cdd)H
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Od)H
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Cd)H
                L5: Cds-CddCtH
                    L6: Cds-(Cdd-Od)CtH
                    L6: Cds-(Cdd-Cd)CtH
                L5: Cds-CddCbH
                    L6: Cds-(Cdd-Od)CbH
                    L6: Cds-(Cdd-Cd)CbH
            L4: Cds-CdCO
                L5: Cds-CdsCsOs
                L5: Cds-CdsCdsOs
                    L6: Cds-Cds(Cds-Od)Os
                    L6: Cds-Cds(Cds-Cd)Os
                        L7: Cds-Cds(Cds-Cds)Os
                        L7: Cds-Cds(Cds-Cdd)Os
                            L8: Cds-Cds(Cds-Cdd-Od)Os
                            L8: Cds-Cds(Cds-Cdd-Cd)Os
                L5: Cds-CdsCtOs
                L5: Cds-CdsCbOs
                L5: Cds-CddCsOs
                    L6: Cds-(Cdd-Od)CsOs
                    L6: Cds-(Cdd-Cd)CsOs
                L5: Cds-CddCdsOs
                    L6: Cds-(Cdd-Od)(Cds-Od)Os
                    L6: Cds-(Cdd-Od)(Cds-Cd)Os
                        L7: Cds-(Cdd-Od)(Cds-Cds)Os
                        L7: Cds-(Cdd-Od)(Cds-Cdd)Os
                            L8: Cds-(Cdd-Od)(Cds-Cdd-Od)Os
                            L8: Cds-(Cdd-Od)(Cds-Cdd-Cd)Os
                    L6: Cds-(Cdd-Cd)(Cds-Cd)Os
                        L7: Cds-(Cdd-Cd)(Cds-Cds)Os
                        L7: Cds-(Cdd-Cd)(Cds-Cdd)Os
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Od)Os
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Cd)Os
                L5: Cds-CddCtOs
                    L6: Cds-(Cdd-Od)CtOs
                    L6: Cds-(Cdd-Cd)CtOs
                L5: Cds-CddCbOs
                    L6: Cds-(Cdd-Od)CbOs
                    L6: Cds-(Cdd-Cd)CbOs
            L4: Cds-CdCC
                L5: Cds-CdsCsCs
                L5: Cds-CdsCdsCs
                    L6: Cds-Cds(Cds-Od)Cs
                    L6: Cds-Cds(Cds-Cd)Cs
                        L7: Cds-Cds(Cds-Cds)Cs
                        L7: Cds-Cds(Cds-Cdd)Cs
                            L8: Cds-Cds(Cds-Cdd-Od)Cs
                            L8: Cds-Cds(Cds-Cdd-Cd)Cs
                L5: Cds-CdsCdsCds
                    L6: Cds-Cds(Cds-Od)(Cds-Od)
                    L6: Cds-Cds(Cds-Od)(Cds-Cd)
                        L7: Cds-Cds(Cds-Od)(Cds-Cds)
                        L7: Cds-Cds(Cds-Od)(Cds-Cdd)
                            L8: Cds-Cds(Cds-Od)(Cds-Cdd-Od)
                            L8: Cds-Cds(Cds-Od)(Cds-Cdd-Cd)
                    L6: Cds-Cds(Cds-Cd)(Cds-Cd)
                        L7: Cds-Cds(Cds-Cds)(Cds-Cds)
                        L7: Cds-Cds(Cds-Cds)(Cds-Cdd)
                            L8: Cds-Cds(Cds-Cds)(Cds-Cdd-Od)
                            L8: Cds-Cds(Cds-Cds)(Cds-Cdd-Cd)
                        L7: Cds-Cds(Cds-Cdd)(Cds-Cdd)
                            L8: Cds-Cds(Cds-Cdd-Od)(Cds-Cdd-Od)
                            L8: Cds-Cds(Cds-Cdd-Od)(Cds-Cdd-Cd)
                            L8: Cds-Cds(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                L5: Cds-CdsCtCs
                L5: Cds-CdsCtCds
                    L6: Cds-CdsCt(Cds-Od)
                    L6: Cds-CdsCt(Cds-Cd)
                        L7: Cds-Cds(Cds-Cds)Ct
                        L7: Cds-Cds(Cds-Cdd)Ct
                            L8: Cds-Cds(Cds-Cdd-Od)Ct
                            L8: Cds-Cds(Cds-Cdd-Cd)Ct
                L5: Cds-CdsCtCt
                L5: Cds-CdsCbCs
                L5: Cds-CdsCbCds
                    L6: Cds-CdsCb(Cds-Od)
                    L6: Cds-Cds(Cds-Cd)Cb
                        L7: Cds-Cds(Cds-Cds)Cb
                        L7: Cds-Cds(Cds-Cdd)Cb
                            L8: Cds-Cds(Cds-Cdd-Od)Cb
                            L8: Cds-Cds(Cds-Cdd-Cd)Cb
                L5: Cds-CdsCbCt
                L5: Cds-CdsCbCb
                L5: Cds-CddCsCs
                    L6: Cds-(Cdd-Od)CsCs
                    L6: Cds-(Cdd-Cd)CsCs
                L5: Cds-CddCdsCs
                    L6: Cds-(Cdd-Od)(Cds-Od)Cs
                    L6: Cds-(Cdd-Od)(Cds-Cd)Cs
                        L7: Cds-(Cdd-Od)(Cds-Cds)Cs
                        L7: Cds-(Cdd-Od)(Cds-Cdd)Cs
                            L8: Cds-(Cdd-Od)(Cds-Cdd-Od)Cs
                            L8: Cds-(Cdd-Od)(Cds-Cdd-Cd)Cs
                    L6: Cds-(Cdd-Cd)(Cds-Cd)Cs
                        L7: Cds-(Cdd-Cd)(Cds-Cds)Cs
                        L7: Cds-(Cdd-Cd)(Cds-Cdd)Cs
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Od)Cs
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Cd)Cs
                L5: Cds-CddCdsCds
                    L6: Cds-(Cdd-Od)(Cds-Od)(Cds-Od)
                    L6: Cds-(Cdd-Od)(Cds-Cd)(Cds-Od)
                        L7: Cds-(Cdd-Od)(Cds-Cds)(Cds-Od)
                        L7: Cds-(Cdd-Od)(Cds-Cdd)(Cds-Od)
                            L8: Cds-(Cdd-Od)(Cds-Cdd-Od)(Cds-Od)
                            L8: Cds-(Cdd-Od)(Cds-Cdd-Cd)(Cds-Od)
                    L6: Cds-(Cdd-Od)(Cds-Cd)(Cds-Cd)
                        L7: Cds-(Cdd-Od)(Cds-Cds)(Cds-Cds)
                        L7: Cds-(Cdd-Od)(Cds-Cdd)(Cds-Cds)
                            L8: Cds-(Cdd-Od)(Cds-Cdd-Od)(Cds-Cds)
                            L8: Cds-(Cdd-Od)(Cds-Cdd-Cd)(Cds-Cds)
                        L7: Cds-(Cdd-Od)(Cds-Cdd)(Cds-Cdd)
                            L8: Cds-(Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)
                            L8: Cds-(Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)
                            L8: Cds-(Cdd-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                    L6: Cds-(Cdd-Cd)(Cds-Od)(Cds-Od)
                    L6: Cds-(Cdd-Cd)(Cds-Od)(Cds-Cd)
                        L7: Cds-(Cdd-Cd)(Cds-Od)(Cds-Cds)
                        L7: Cds-(Cdd-Cd)(Cds-Od)(Cds-Cdd)
                            L8: Cds-(Cdd-Cd)(Cds-Od)(Cds-Cdd-Od)
                            L8: Cds-(Cdd-Cd)(Cds-Od)(Cds-Cdd-Cd)
                    L6: Cds-(Cdd-Cd)(Cds-Cd)(Cds-Cd)
                        L7: Cds-(Cdd-Cd)(Cds-Cds)(Cds-Cds)
                        L7: Cds-(Cdd-Cd)(Cds-Cdd)(Cds-Cds)
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Od)(Cds-Cds)
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cds)
                        L7: Cds-(Cdd-Cd)(Cds-Cdd)(Cds-Cdd)
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Od)(Cds-Cdd-Od)
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Od)(Cds-Cdd-Cd)
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                L5: Cds-CddCtCs
                    L6: Cds-(Cdd-Od)CtCs
                    L6: Cds-(Cdd-Cd)CtCs
                L5: Cds-CddCtCds
                    L6: Cds-(Cdd-Od)(Cds-Od)Ct
                    L6: Cds-(Cdd-Od)(Cds-Cd)Ct
                        L7: Cds-(Cdd-Od)(Cds-Cds)Ct
                        L7: Cds-(Cdd-Od)(Cds-Cdd)Ct
                            L8: Cds-(Cdd-Od)(Cds-Cdd-Od)Ct
                            L8: Cds-(Cdd-Od)(Cds-Cdd-Cd)Ct
                    L6: Cds-(Cdd-Cd)(Cds-Cd)Ct
                        L7: Cds-(Cdd-Cd)(Cds-Cds)Ct
                        L7: Cds-(Cdd-Cd)(Cds-Cdd)Ct
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Od)Ct
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Cd)Ct
                L5: Cds-CddCtCt
                    L6: Cds-(Cdd-Od)CtCt
                    L6: Cds-(Cdd-Cd)CtCt
                L5: Cds-CddCbCs
                    L6: Cds-(Cdd-Od)CbCs
                    L6: Cds-(Cdd-Cd)CbCs
                L5: Cds-CddCbCds
                    L6: Cds-(Cdd-Od)(Cds-Od)Cb
                    L6: Cds-(Cdd-Od)(Cds-Cd)Cb
                        L7: Cds-(Cdd-Od)(Cds-Cds)Cb
                        L7: Cds-(Cdd-Od)(Cds-Cdd)Cb
                            L8: Cds-(Cdd-Od)(Cds-Cdd-Od)Cb
                            L8: Cds-(Cdd-Od)(Cds-Cdd-Cd)Cb
                    L6: Cds-(Cdd-Cd)(Cds-Cd)Cb
                        L7: Cds-(Cdd-Cd)(Cds-Cds)Cb
                        L7: Cds-(Cdd-Cd)(Cds-Cdd)Cb
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Od)Cb
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Cd)Cb
                L5: Cds-CddCbCt
                    L6: Cds-(Cdd-Od)CbCt
                    L6: Cds-(Cdd-Cd)CbCt
                L5: Cds-CddCbCb
                    L6: Cds-(Cdd-Od)CbCb
                    L6: Cds-(Cdd-Cd)CbCb
        L3: Cs
            L4: Cs-HHHH
            L4: Cs-CHHH
                L5: Cs-CsHHH
                L5: Cs-CdsHHH
                    L6: Cs-(Cds-Od)HHH
                    L6: Cs-(Cds-Cd)HHH
                        L7: Cs-(Cds-Cds)HHH
                        L7: Cs-(Cds-Cdd)HHH
                            L8: Cs-(Cds-Cdd-Od)HHH
                            L8: Cs-(Cds-Cdd-Cd)HHH
                L5: Cs-CtHHH
                L5: Cs-CbHHH
            L4: Cs-OsHHH
            L4: Cs-OsOsHH
            L4: Cs-OsOsOsH
            L4: Cs-CCHH
                L5: Cs-CsCsHH
                L5: Cs-CdsCsHH
                    L6: Cs-(Cds-Od)CsHH
                    L6: Cs-(Cds-Cd)CsHH
                        L7: Cs-(Cds-Cds)CsHH
                        L7: Cs-(Cds-Cdd)CsHH
                            L8: Cs-(Cds-Cdd-Od)CsHH
                            L8: Cs-(Cds-Cdd-Cd)CsHH
                L5: Cs-CdsCdsHH
                    L6: Cs-(Cds-Od)(Cds-Od)HH
                    L6: Cs-(Cds-Od)(Cds-Cd)HH
                        L7: Cs-(Cds-Od)(Cds-Cds)HH
                        L7: Cs-(Cds-Od)(Cds-Cdd)HH
                            L8: Cs-(Cds-Od)(Cds-Cdd-Od)HH
                            L8: Cs-(Cds-Od)(Cds-Cdd-Cd)HH
                    L6: Cs-(Cds-Cd)(Cds-Cd)HH
                        L7: Cs-(Cds-Cds)(Cds-Cds)HH
                        L7: Cs-(Cds-Cdd)(Cds-Cds)HH
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cds)HH
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)HH
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)HH
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)HH
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)HH
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)HH
                L5: Cs-CtCsHH
                L5: Cs-CtCdsHH
                    L6: Cs-(Cds-Od)CtHH
                    L6: Cs-(Cds-Cd)CtHH
                        L7: Cs-(Cds-Cds)CtHH
                        L7: Cs-(Cds-Cdd)CtHH
                            L8: Cs-(Cds-Cdd-Od)CtHH
                            L8: Cs-(Cds-Cdd-Cd)CtHH
                L5: Cs-CtCtHH
                L5: Cs-CbCsHH
                L5: Cs-CbCdsHH
                    L6: Cs-(Cds-Od)CbHH
                    L6: Cs-(Cds-Cd)CbHH
                        L7: Cs-(Cds-Cds)CbHH
                        L7: Cs-(Cds-Cdd)CbHH
                            L8: Cs-(Cds-Cdd-Od)CbHH
                            L8: Cs-(Cds-Cdd-Cd)CbHH
                L5: Cs-CbCtHH
                L5: Cs-CbCbHH
            L4: Cs-CCCH
                L5: Cs-CsCsCsH
                L5: Cs-CdsCsCsH
                    L6: Cs-(Cds-Od)CsCsH
                    L6: Cs-(Cds-Cd)CsCsH
                        L7: Cs-(Cds-Cds)CsCsH
                        L7: Cs-(Cds-Cdd)CsCsH
                            L8: Cs-(Cds-Cdd-Od)CsCsH
                            L8: Cs-(Cds-Cdd-Cd)CsCsH
                L5: Cs-CtCsCsH
                L5: Cs-CbCsCsH
                L5: Cs-CdsCdsCsH
                    L6: Cs-(Cds-Od)(Cds-Od)CsH
                    L6: Cs-(Cds-Od)(Cds-Cd)CsH
                        L7: Cs-(Cds-Od)(Cds-Cds)CsH
                        L7: Cs-(Cds-Od)(Cds-Cdd)CsH
                            L8: Cs-(Cds-Od)(Cds-Cdd-Od)CsH
                            L8: Cs-(Cds-Od)(Cds-Cdd-Cd)CsH
                    L6: Cs-(Cds-Cd)(Cds-Cd)CsH
                        L7: Cs-(Cds-Cds)(Cds-Cds)CsH
                        L7: Cs-(Cds-Cdd)(Cds-Cds)CsH
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cds)CsH
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CsH
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CsH
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CsH
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)CsH
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CsH
                L5: Cs-CtCdsCsH
                    L6: Cs-(Cds-Od)CtCsH
                    L6: Cs-(Cds-Cd)CtCsH
                        L7: Cs-(Cds-Cds)CtCsH
                        L7: Cs-(Cds-Cdd)CtCsH
                            L8: Cs-(Cds-Cdd-Od)CtCsH
                            L8: Cs-(Cds-Cdd-Cd)CtCsH
                L5: Cs-CbCdsCsH
                    L6: Cs-(Cds-Od)CbCsH
                    L6: Cs-(Cds-Cd)CbCsH
                        L7: Cs-(Cds-Cds)CbCsH
                        L7: Cs-(Cds-Cdd)CbCsH
                            L8: Cs-(Cds-Cdd-Od)CbCsH
                            L8: Cs-(Cds-Cdd-Cd)CbCsH
                L5: Cs-CtCtCsH
                L5: Cs-CbCtCsH
                L5: Cs-CbCbCsH
                L5: Cs-CdsCdsCdsH
                    L6: Cs-(Cds-Od)(Cds-Od)(Cds-Od)H
                    L6: Cs-(Cds-Od)(Cds-Od)(Cds-Cd)H
                        L7: Cs-(Cds-Od)(Cds-Od)(Cds-Cds)H
                        L7: Cs-(Cds-Od)(Cds-Od)(Cds-Cdd)H
                            L8: Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Od)H
                            L8: Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Cd)H
                    L6: Cs-(Cds-Od)(Cds-Cd)(Cds-Cd)H
                        L7: Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)H
                        L7: Cs-(Cds-Od)(Cds-Cdd)(Cds-Cds)H
                            L8: Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)H
                            L8: Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cds)H
                        L7: Cs-(Cds-Od)(Cds-Cdd)(Cds-Cdd)H
                            L8: Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)H
                            L8: Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)H
                            L8: Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H
                    L6: Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)H
                        L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)H
                        L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)H
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)H
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)H
                        L7: Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)H
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)H
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Cd)H
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)H
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)H
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)H
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H
                L5: Cs-CtCdsCdsH
                    L6: Cs-(Cds-Od)(Cds-Od)CtH
                    L6: Cs-(Cds-Od)(Cds-Cd)CtH
                        L7: Cs-(Cds-Od)(Cds-Cds)CtH
                        L7: Cs-(Cds-Od)(Cds-Cdd)CtH
                            L8: Cs-(Cds-Od)(Cds-Cdd-Od)CtH
                            L8: Cs-(Cds-Od)(Cds-Cdd-Cd)CtH
                    L6: Cs-(Cds-Cd)(Cds-Cd)CtH
                        L7: Cs-(Cds-Cds)(Cds-Cds)CtH
                        L7: Cs-(Cds-Cdd)(Cds-Cds)CtH
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cds)CtH
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CtH
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CtH
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CtH
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)CtH
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtH
                L5: Cs-CbCdsCdsH
                    L6: Cs-(Cds-Od)(Cds-Od)CbH
                    L6: Cs-(Cds-Od)(Cds-Cd)CbH
                        L7: Cs-(Cds-Od)(Cds-Cds)CbH
                        L7: Cs-(Cds-Od)(Cds-Cdd)CbH
                            L8: Cs-(Cds-Od)(Cds-Cdd-Od)CbH
                            L8: Cs-(Cds-Od)(Cds-Cdd-Cd)CbH
                    L6: Cs-(Cds-Cd)(Cds-Cd)CbH
                        L7: Cs-(Cds-Cds)(Cds-Cds)CbH
                        L7: Cs-(Cds-Cdd)(Cds-Cds)CbH
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cds)CbH
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CbH
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CbH
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CbH
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)CbH
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbH
                L5: Cs-CtCtCdsH
                    L6: Cs-CtCt(Cds-Od)H
                    L6: Cs-CtCt(Cds-Cd)H
                        L7: Cs-CtCt(Cds-Cds)H
                        L7: Cs-CtCt(Cds-Cdd)H
                            L8: Cs-CtCt(Cds-Cdd-Od)H
                            L8: Cs-CtCt(Cds-Cdd-Cd)H
                L5: Cs-CbCtCdsH
                    L6: Cs-CbCt(Cds-Od)H
                    L6: Cs-CbCt(Cds-Cd)H
                        L7: Cs-CbCt(Cds-Cds)H
                        L7: Cs-CbCt(Cds-Cdd)H
                            L8: Cs-CbCt(Cds-Cdd-Od)H
                            L8: Cs-CbCt(Cds-Cdd-Cd)H
                L5: Cs-CbCbCdsH
                    L6: Cs-CbCb(Cds-Od)H
                    L6: Cs-CbCb(Cds-Cd)H
                        L7: Cs-CbCb(Cds-Cds)H
                        L7: Cs-CbCb(Cds-Cdd)H
                            L8: Cs-CbCb(Cds-Cdd-Od)H
                            L8: Cs-CbCb(Cds-Cdd-Cd)H
                L5: Cs-CtCtCtH
                L5: Cs-CbCtCtH
                L5: Cs-CbCbCtH
                L5: Cs-CbCbCbH
            L4: Cs-CCCC
                L5: Cs-CsCsCsCs
                L5: Cs-CdsCsCsCs
                    L6: Cs-(Cds-Od)CsCsCs
                    L6: Cs-(Cds-Cd)CsCsCs
                        L7: Cs-(Cds-Cds)CsCsCs
                        L7: Cs-(Cds-Cdd)CsCsCs
                            L8: Cs-(Cds-Cdd-Od)CsCsCs
                            L8: Cs-(Cds-Cdd-Cd)CsCsCs
                L5: Cs-CtCsCsCs
                L5: Cs-CbCsCsCs
                L5: Cs-CdsCdsCsCs
                    L6: Cs-(Cds-Od)(Cds-Od)CsCs
                    L6: Cs-(Cds-Od)(Cds-Cd)CsCs
                        L7: Cs-(Cds-Od)(Cds-Cds)CsCs
                        L7: Cs-(Cds-Od)(Cds-Cdd)CsCs
                            L8: Cs-(Cds-Od)(Cds-Cdd-Od)CsCs
                            L8: Cs-(Cds-Od)(Cds-Cdd-Cd)CsCs
                    L6: Cs-(Cds-Cd)(Cds-Cd)CsCs
                        L7: Cs-(Cds-Cds)(Cds-Cds)CsCs
                        L7: Cs-(Cds-Cdd)(Cds-Cds)CsCs
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cds)CsCs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CsCs
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CsCs
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CsCs
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)CsCs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CsCs
                L5: Cs-CtCdsCsCs
                    L6: Cs-(Cds-Od)CtCsCs
                    L6: Cs-(Cds-Cd)CtCsCs
                        L7: Cs-(Cds-Cds)CtCsCs
                        L7: Cs-(Cds-Cdd)CtCsCs
                            L8: Cs-(Cds-Cdd-Od)CtCsCs
                            L8: Cs-(Cds-Cdd-Cd)CtCsCs
                L5: Cs-CbCdsCsCs
                    L6: Cs-(Cds-Od)CbCsCs
                    L6: Cs-(Cds-Cd)CbCsCs
                        L7: Cs-(Cds-Cds)CbCsCs
                        L7: Cs-(Cds-Cdd)CbCsCs
                            L8: Cs-(Cds-Cdd-Od)CbCsCs
                            L8: Cs-(Cds-Cdd-Cd)CbCsCs
                L5: Cs-CtCtCsCs
                L5: Cs-CbCtCsCs
                L5: Cs-CbCbCsCs
                L5: Cs-CdsCdsCdsCs
                    L6: Cs-(Cds-Od)(Cds-Od)(Cds-Od)Cs
                    L6: Cs-(Cds-Od)(Cds-Od)(Cds-Cd)Cs
                        L7: Cs-(Cds-Od)(Cds-Od)(Cds-Cds)Cs
                        L7: Cs-(Cds-Od)(Cds-Od)(Cds-Cdd)Cs
                            L8: Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Od)Cs
                            L8: Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Cd)Cs
                    L6: Cs-(Cds-Od)(Cds-Cd)(Cds-Cd)Cs
                        L7: Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Cs
                        L7: Cs-(Cds-Od)(Cds-Cdd)(Cds-Cds)Cs
                            L8: Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)Cs
                            L8: Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cds)Cs
                        L7: Cs-(Cds-Od)(Cds-Cdd)(Cds-Cdd)Cs
                            L8: Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)Cs
                            L8: Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)Cs
                            L8: Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs
                    L6: Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)Cs
                        L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cs
                        L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)Cs
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Cs
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)Cs
                        L7: Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)Cs
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)Cs
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Cd)Cs
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)Cs
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)Cs
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)Cs
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs
                L5: Cs-CtCdsCdsCs
                    L6: Cs-(Cds-Od)(Cds-Od)CtCs
                    L6: Cs-(Cds-Od)(Cds-Cd)CtCs
                        L7: Cs-(Cds-Od)(Cds-Cds)CtCs
                        L7: Cs-(Cds-Od)(Cds-Cdd)CtCs
                            L8: Cs-(Cds-Od)(Cds-Cdd-Od)CtCs
                            L8: Cs-(Cds-Od)(Cds-Cdd-Cd)CtCs
                    L6: Cs-(Cds-Cd)(Cds-Cd)CtCs
                        L7: Cs-(Cds-Cds)(Cds-Cds)CtCs
                        L7: Cs-(Cds-Cdd)(Cds-Cds)CtCs
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cds)CtCs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CtCs
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CtCs
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CtCs
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)CtCs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtCs
                L5: Cs-CbCdsCdsCs
                    L6: Cs-(Cds-Od)(Cds-Od)CbCs
                    L6: Cs-(Cds-Od)(Cds-Cd)CbCs
                        L7: Cs-(Cds-Od)(Cds-Cds)CbCs
                        L7: Cs-(Cds-Od)(Cds-Cdd)CbCs
                            L8: Cs-(Cds-Od)(Cds-Cdd-Od)CbCs
                            L8: Cs-(Cds-Od)(Cds-Cdd-Cd)CbCs
                    L6: Cs-(Cds-Cd)(Cds-Cd)CbCs
                        L7: Cs-(Cds-Cds)(Cds-Cds)CbCs
                        L7: Cs-(Cds-Cdd)(Cds-Cds)CbCs
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cds)CbCs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CbCs
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CbCs
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CbCs
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)CbCs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbCs
                L5: Cs-CtCtCdsCs
                    L6: Cs-(Cds-Od)CtCtCs
                    L6: Cs-(Cds-Cd)CtCtCs
                        L7: Cs-(Cds-Cds)CtCtCs
                        L7: Cs-(Cds-Cdd)CtCtCs
                            L8: Cs-(Cds-Cdd-Od)CtCtCs
                            L8: Cs-(Cds-Cdd-Cd)CtCtCs
                L5: Cs-CbCtCdsCs
                    L6: Cs-(Cds-Od)CbCtCs
                    L6: Cs-(Cds-Cd)CbCtCs
                        L7: Cs-(Cds-Cds)CbCtCs
                        L7: Cs-(Cds-Cdd)CbCtCs
                            L8: Cs-(Cds-Cdd-Od)CbCtCs
                            L8: Cs-(Cds-Cdd-Cd)CbCtCs
                L5: Cs-CbCbCdsCs
                    L6: Cs-(Cds-Od)CbCbCs
                    L6: Cs-(Cds-Cd)CbCbCs
                        L7: Cs-(Cds-Cds)CbCbCs
                        L7: Cs-(Cds-Cdd)CbCbCs
                            L8: Cs-(Cds-Cdd-Od)CbCbCs
                            L8: Cs-(Cds-Cdd-Cd)CbCbCs
                L5: Cs-CtCtCtCs
                L5: Cs-CbCtCtCs
                L5: Cs-CbCbCtCs
                L5: Cs-CbCbCbCs
                L5: Cs-CdsCdsCdsCds
                    L6: Cs-(Cds-Od)(Cds-Od)(Cds-Od)(Cds-Od)
                    L6: Cs-(Cds-Od)(Cds-Od)(Cds-Od)(Cds-Cd)
                        L7: Cs-(Cds-Od)(Cds-Od)(Cds-Od)(Cds-Cds)
                        L7: Cs-(Cds-Od)(Cds-Od)(Cds-Od)(Cds-Cdd)
                            L8: Cs-(Cds-Od)(Cds-Od)(Cds-Od)(Cds-Cdd-Od)
                            L8: Cs-(Cds-Od)(Cds-Od)(Cds-Od)(Cds-Cdd-Cd)
                    L6: Cs-(Cds-Od)(Cds-Od)(Cds-Cd)(Cds-Cd)
                        L7: Cs-(Cds-Od)(Cds-Od)(Cds-Cds)(Cds-Cds)
                        L7: Cs-(Cds-Od)(Cds-Od)(Cds-Cdd)(Cds-Cds)
                            L8: Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)
                            L8: Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Cd)(Cds-Cds)
                        L7: Cs-(Cds-Od)(Cds-Od)(Cds-Cdd)(Cds-Cdd)
                            L8: Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)
                            L8: Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                    L6: Cs-(Cds-Od)(Cds-Cd)(Cds-Cd)(Cds-Cd)
                        L7: Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)(Cds-Cds)
                        L7: Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)(Cds-Cdd)
                            L8: Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)
                            L8: Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)
                        L7: Cs-(Cds-Od)(Cds-Cds)(Cds-Cdd)(Cds-Cdd)
                            L8: Cs-(Cds-Od)(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)
                            L8: Cs-(Cds-Od)(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-Od)(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                        L7: Cs-(Cds-Od)(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)
                            L8: Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)
                            L8: Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                    L6: Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)(Cds-Cd)
                        L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)
                        L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd)
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)
                        L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)(Cds-Cdd)
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                        L7: Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                L5: Cs-CtCdsCdsCds
                    L6: Cs-(Cds-Od)(Cds-Od)(Cds-Od)Ct
                    L6: Cs-(Cds-Od)(Cds-Od)(Cds-Cd)Ct
                        L7: Cs-(Cds-Od)(Cds-Od)(Cds-Cds)Ct
                        L7: Cs-(Cds-Od)(Cds-Od)(Cds-Cdd)Ct
                            L8: Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Od)Ct
                            L8: Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Cd)Ct
                    L6: Cs-(Cds-Od)(Cds-Cd)(Cds-Cd)Ct
                        L7: Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Ct
                        L7: Cs-(Cds-Od)(Cds-Cdd)(Cds-Cds)Ct
                            L8: Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)Ct
                            L8: Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cds)Ct
                        L7: Cs-(Cds-Od)(Cds-Cdd)(Cds-Cdd)Ct
                            L8: Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)Ct
                            L8: Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)Ct
                            L8: Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct
                    L6: Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)Ct
                        L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Ct
                        L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)Ct
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Ct
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)Ct
                        L7: Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)Ct
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)Ct
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Cd)Ct
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)Ct
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)Ct
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)Ct
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct
                L5: Cs-CbCdsCdsCds
                    L6: Cs-(Cds-Od)(Cds-Od)(Cds-Od)Cb
                    L6: Cs-(Cds-Od)(Cds-Od)(Cds-Cd)Cb
                        L7: Cs-(Cds-Od)(Cds-Od)(Cds-Cds)Cb
                        L7: Cs-(Cds-Od)(Cds-Od)(Cds-Cdd)Cb
                            L8: Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Od)Cb
                            L8: Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Cd)Cb
                    L6: Cs-(Cds-Od)(Cds-Cd)(Cds-Cd)Cb
                        L7: Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Cb
                        L7: Cs-(Cds-Od)(Cds-Cdd)(Cds-Cds)Cb
                            L8: Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)Cb
                            L8: Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cds)Cb
                        L7: Cs-(Cds-Od)(Cds-Cdd)(Cds-Cdd)Cb
                            L8: Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)Cb
                            L8: Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)Cb
                            L8: Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb
                    L6: Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)Cb
                        L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cb
                        L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)Cb
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Cb
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)Cb
                        L7: Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)Cb
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)Cb
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Cd)Cb
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)Cb
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)Cb
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)Cb
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb
                L5: Cs-CtCtCdsCds
                    L6: Cs-(Cds-Od)(Cds-Od)CtCt
                    L6: Cs-(Cds-Od)(Cds-Cd)CtCt
                        L7: Cs-(Cds-Od)(Cds-Cds)CtCt
                        L7: Cs-(Cds-Od)(Cds-Cdd)CtCt
                            L8: Cs-(Cds-Od)(Cds-Cdd-Od)CtCt
                            L8: Cs-(Cds-Od)(Cds-Cdd-Cd)CtCt
                    L6: Cs-(Cds-Cd)(Cds-Cd)CtCt
                        L7: Cs-(Cds-Cds)(Cds-Cds)CtCt
                        L7: Cs-(Cds-Cdd)(Cds-Cds)CtCt
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cds)CtCt
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CtCt
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CtCt
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CtCt
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)CtCt
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtCt
                L5: Cs-CbCtCdsCds
                    L6: Cs-(Cds-Od)(Cds-Od)CbCt
                    L6: Cs-(Cds-Od)(Cds-Cd)CbCt
                        L7: Cs-(Cds-Od)(Cds-Cds)CbCt
                        L7: Cs-(Cds-Od)(Cds-Cdd)CbCt
                            L8: Cs-(Cds-Od)(Cds-Cdd-Od)CbCt
                            L8: Cs-(Cds-Od)(Cds-Cdd-Cd)CbCt
                    L6: Cs-(Cds-Cd)(Cds-Cd)CbCt
                        L7: Cs-(Cds-Cds)(Cds-Cds)CbCt
                        L7: Cs-(Cds-Cdd)(Cds-Cds)CbCt
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cds)CbCt
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CbCt
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CbCt
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CbCt
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)CbCt
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbCt
                L5: Cs-CbCbCdsCds
                    L6: Cs-(Cds-Od)(Cds-Od)CbCb
                    L6: Cs-(Cds-Od)(Cds-Cd)CbCb
                        L7: Cs-(Cds-Od)(Cds-Cds)CbCb
                        L7: Cs-(Cds-Od)(Cds-Cdd)CbCb
                            L8: Cs-(Cds-Od)(Cds-Cdd-Od)CbCb
                            L8: Cs-(Cds-Od)(Cds-Cdd-Cd)CbCb
                    L6: Cs-(Cds-Cd)(Cds-Cd)CbCb
                        L7: Cs-(Cds-Cds)(Cds-Cds)CbCb
                        L7: Cs-(Cds-Cdd)(Cds-Cds)CbCb
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cds)CbCb
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CbCb
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CbCb
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CbCb
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)CbCb
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbCb
                L5: Cs-CtCtCtCds
                    L6: Cs-(Cds-Od)CtCtCt
                    L6: Cs-(Cds-Cd)CtCtCt
                        L7: Cs-(Cds-Cds)CtCtCt
                        L7: Cs-(Cds-Cdd)CtCtCt
                            L8: Cs-(Cds-Cdd-Od)CtCtCt
                            L8: Cs-(Cds-Cdd-Cd)CtCtCt
                L5: Cs-CbCtCtCds
                    L6: Cs-(Cds-Od)CbCtCt
                    L6: Cs-(Cds-Cd)CbCtCt
                        L7: Cs-(Cds-Cds)CbCtCt
                        L7: Cs-(Cds-Cdd)CbCtCt
                            L8: Cs-(Cds-Cdd-Od)CbCtCt
                            L8: Cs-(Cds-Cdd-Cd)CbCtCt
                L5: Cs-CbCbCtCds
                    L6: Cs-(Cds-Od)CbCbCt
                    L6: Cs-(Cds-Cd)CbCbCt
                        L7: Cs-(Cds-Cds)CbCbCt
                        L7: Cs-(Cds-Cdd)CbCbCt
                            L8: Cs-(Cds-Cdd-Od)CbCbCt
                            L8: Cs-(Cds-Cdd-Cd)CbCbCt
                L5: Cs-CbCbCbCds
                    L6: Cs-(Cds-Od)CbCbCb
                    L6: Cs-(Cds-Cd)CbCbCb
                        L7: Cs-(Cds-Cds)CbCbCb
                        L7: Cs-(Cds-Cdd)CbCbCb
                            L8: Cs-(Cds-Cdd-Od)CbCbCb
                            L8: Cs-(Cds-Cdd-Cd)CbCbCb
                L5: Cs-CtCtCtCt
                L5: Cs-CbCtCtCt
                L5: Cs-CbCbCtCt
                L5: Cs-CbCbCbCt
                L5: Cs-CbCbCbCb
            L4: Cs-CCCOs
                L5: Cs-CsCsCsOs
                L5: Cs-CdsCsCsOs
                    L6: Cs-(Cds-Od)CsCsOs
                    L6: Cs-(Cds-Cd)CsCsOs
                        L7: Cs-(Cds-Cds)CsCsOs
                        L7: Cs-(Cds-Cdd)CsCsOs
                            L8: Cs-(Cds-Cdd-Od)CsCsOs
                            L8: Cs-(Cds-Cdd-Cd)CsCsOs
                L5: Cs-OsCtCsCs
                L5: Cs-CbCsCsOs
                L5: Cs-CdsCdsCsOs
                    L6: Cs-(Cds-Od)(Cds-Od)CsOs
                    L6: Cs-(Cds-Od)(Cds-Cd)CsOs
                        L7: Cs-(Cds-Od)(Cds-Cds)CsOs
                        L7: Cs-(Cds-Od)(Cds-Cdd)CsOs
                            L8: Cs-(Cds-Od)(Cds-Cdd-Od)CsOs
                            L8: Cs-(Cds-Od)(Cds-Cdd-Cd)CsOs
                    L6: Cs-(Cds-Cd)(Cds-Cd)CsOs
                        L7: Cs-(Cds-Cds)(Cds-Cds)CsOs
                        L7: Cs-(Cds-Cdd)(Cds-Cds)CsOs
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cds)CsOs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CsOs
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CsOs
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CsOs
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)CsOs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CsOs
                L5: Cs-CtCdsCsOs
                    L6: Cs-(Cds-Od)CtCsOs
                    L6: Cs-(Cds-Cd)CtCsOs
                        L7: Cs-(Cds-Cds)CtCsOs
                        L7: Cs-(Cds-Cdd)CtCsOs
                            L8: Cs-(Cds-Cdd-Od)CtCsOs
                            L8: Cs-(Cds-Cdd-Cd)CtCsOs
                L5: Cs-CbCdsCsOs
                    L6: Cs-(Cds-Od)CbCsOs
                    L6: Cs-(Cds-Cd)CbCsOs
                        L7: Cs-(Cds-Cds)CbCsOs
                        L7: Cs-(Cds-Cdd)CbCsOs
                            L8: Cs-(Cds-Cdd-Od)CbCsOs
                            L8: Cs-(Cds-Cdd-Cd)CbCsOs
                L5: Cs-CtCtCsOs
                L5: Cs-CbCtCsOs
                L5: Cs-CbCbCsOs
                L5: Cs-CdsCdsCdsOs
                    L6: Cs-(Cds-Od)(Cds-Od)(Cds-Od)Os
                    L6: Cs-(Cds-Od)(Cds-Od)(Cds-Cd)Os
                        L7: Cs-(Cds-Od)(Cds-Od)(Cds-Cds)Os
                        L7: Cs-(Cds-Od)(Cds-Od)(Cds-Cdd)Os
                            L8: Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Od)Os
                            L8: Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Cd)Os
                    L6: Cs-(Cds-Od)(Cds-Cd)(Cds-Cd)Os
                        L7: Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Os
                        L7: Cs-(Cds-Od)(Cds-Cdd)(Cds-Cds)Os
                            L8: Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)Os
                            L8: Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cds)Os
                        L7: Cs-(Cds-Od)(Cds-Cdd)(Cds-Cdd)Os
                            L8: Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)Os
                            L8: Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)Os
                            L8: Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Os
                    L6: Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)Os
                        L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Os
                        L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)Os
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Os
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)Os
                        L7: Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)Os
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)Os
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Cd)Os
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Os
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)Os
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)Os
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)Os
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Os
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Os
                L5: Cs-CtCdsCdsOs
                    L6: Cs-(Cds-Od)(Cds-Od)CtOs
                    L6: Cs-(Cds-Od)(Cds-Cd)CtOs
                        L7: Cs-(Cds-Od)(Cds-Cds)CtOs
                        L7: Cs-(Cds-Od)(Cds-Cdd)CtOs
                            L8: Cs-(Cds-Od)(Cds-Cdd-Od)CtOs
                            L8: Cs-(Cds-Od)(Cds-Cdd-Cd)CtOs
                    L6: Cs-(Cds-Cd)(Cds-Cd)CtOs
                        L7: Cs-(Cds-Cds)(Cds-Cds)CtOs
                        L7: Cs-(Cds-Cdd)(Cds-Cds)CtOs
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cds)CtOs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CtOs
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CtOs
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CtOs
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)CtOs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtOs
                L5: Cs-CbCdsCdsOs
                    L6: Cs-(Cds-Od)(Cds-Od)CbOs
                    L6: Cs-(Cds-Od)(Cds-Cd)CbOs
                        L7: Cs-(Cds-Od)(Cds-Cds)CbOs
                        L7: Cs-(Cds-Od)(Cds-Cdd)CbOs
                            L8: Cs-(Cds-Od)(Cds-Cdd-Od)CbOs
                            L8: Cs-(Cds-Od)(Cds-Cdd-Cd)CbOs
                    L6: Cs-(Cds-Cd)(Cds-Cd)CbOs
                        L7: Cs-(Cds-Cds)(Cds-Cds)CbOs
                        L7: Cs-(Cds-Cdd)(Cds-Cds)CbOs
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cds)CbOs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CbOs
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CbOs
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CbOs
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)CbOs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbOs
                L5: Cs-CtCtCdsOs
                    L6: Cs-(Cds-Od)CtCtOs
                    L6: Cs-(Cds-Cd)CtCtOs
                        L7: Cs-(Cds-Cds)CtCtOs
                        L7: Cs-(Cds-Cdd)CtCtOs
                            L8: Cs-(Cds-Cdd-Od)CtCtOs
                            L8: Cs-(Cds-Cdd-Cd)CtCtOs
                L5: Cs-CbCtCdsOs
                    L6: Cs-(Cds-Od)CbCtOs
                    L6: Cs-(Cds-Cd)CbCtOs
                        L7: Cs-(Cds-Cds)CbCtOs
                        L7: Cs-(Cds-Cdd)CbCtOs
                            L8: Cs-(Cds-Cdd-Od)CbCtOs
                            L8: Cs-(Cds-Cdd-Cd)CbCtOs
                L5: Cs-CbCbCdsOs
                    L6: Cs-(Cds-Od)CbCbOs
                    L6: Cs-(Cds-Cd)CbCbOs
                        L7: Cs-(Cds-Cds)CbCbOs
                        L7: Cs-(Cds-Cdd)CbCbOs
                            L8: Cs-(Cds-Cdd-Od)CbCbOs
                            L8: Cs-(Cds-Cdd-Cd)CbCbOs
                L5: Cs-CtCtCtOs
                L5: Cs-CbCtCtOs
                L5: Cs-CbCbCtOs
                L5: Cs-CbCbCbOs
            L4: Cs-CCOsOs
                L5: Cs-CsCsOsOs
                L5: Cs-CdsCsOsOs
                    L6: Cs-(Cds-Od)CsOsOs
                    L6: Cs-(Cds-Cd)CsOsOs
                        L7: Cs-(Cds-Cds)CsOsOs
                        L7: Cs-(Cds-Cdd)CsOsOs
                            L8: Cs-(Cds-Cdd-Od)CsOsOs
                            L8: Cs-(Cds-Cdd-Cd)CsOsOs
                L5: Cs-CdsCdsOsOs
                    L6: Cs-(Cds-Od)(Cds-Od)OsOs
                    L6: Cs-(Cds-Od)(Cds-Cd)OsOs
                        L7: Cs-(Cds-Od)(Cds-Cds)OsOs
                        L7: Cs-(Cds-Od)(Cds-Cdd)OsOs
                            L8: Cs-(Cds-Od)(Cds-Cdd-Od)OsOs
                            L8: Cs-(Cds-Od)(Cds-Cdd-Cd)OsOs
                    L6: Cs-(Cds-Cd)(Cds-Cd)OsOs
                        L7: Cs-(Cds-Cds)(Cds-Cds)OsOs
                        L7: Cs-(Cds-Cdd)(Cds-Cds)OsOs
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cds)OsOs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)OsOs
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)OsOs
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)OsOs
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)OsOs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)OsOs
                L5: Cs-CtCsOsOs
                L5: Cs-CtCdsOsOs
                    L6: Cs-(Cds-Od)CtOsOs
                    L6: Cs-(Cds-Cd)CtOsOs
                        L7: Cs-(Cds-Cds)CtOsOs
                        L7: Cs-(Cds-Cdd)CtOsOs
                            L8: Cs-(Cds-Cdd-Od)CtOsOs
                            L8: Cs-(Cds-Cdd-Cd)CtOsOs
                L5: Cs-CtCtOsOs
                L5: Cs-CbCsOsOs
                L5: Cs-CbCdsOsOs
                    L6: Cs-(Cds-Od)CbOsOs
                    L6: Cs-(Cds-Cd)CbOsOs
                        L7: Cs-(Cds-Cds)CbOsOs
                        L7: Cs-(Cds-Cdd)CbOsOs
                            L8: Cs-(Cds-Cdd-Od)CbOsOs
                            L8: Cs-(Cds-Cdd-Cd)CbOsOs
                L5: Cs-CbCtOsOs
                L5: Cs-CbCbOsOs
            L4: Cs-COsOsOs
                L5: Cs-CsOsOsOs
                L5: Cs-CdsOsOsOs
                    L6: Cs-(Cds-Od)OsOsOs
                    L6: Cs-(Cds-Cd)OsOsOs
                        L7: Cs-(Cds-Cds)OsOsOs
                        L7: Cs-(Cds-Cdd)OsOsOs
                            L8: Cs-(Cds-Cdd-Od)OsOsOs
                            L8: Cs-(Cds-Cdd-Cd)OsOsOs
                L5: Cs-CtOsOsOs
                L5: Cs-CbOsOsOs
            L4: Cs-OsOsOsOs
            L4: Cs-COsOsH
                L5: Cs-CsOsOsH
                L5: Cs-CdsOsOsH
                    L6: Cs-(Cds-Od)OsOsH
                    L6: Cs-(Cds-Cd)OsOsH
                        L7: Cs-(Cds-Cds)OsOsH
                        L7: Cs-(Cds-Cdd)OsOsH
                            L8: Cs-(Cds-Cdd-Od)OsOsH
                            L8: Cs-(Cds-Cdd-Cd)OsOsH
                L5: Cs-CtOsOsH
                L5: Cs-CbOsOsH
            L4: Cs-CCOsH
                L5: Cs-CsCsOsH
                L5: Cs-CdsCsOsH
                    L6: Cs-(Cds-Od)CsOsH
                    L6: Cs-(Cds-Cd)CsOsH
                        L7: Cs-(Cds-Cds)CsOsH
                        L7: Cs-(Cds-Cdd)CsOsH
                            L8: Cs-(Cds-Cdd-Od)CsOsH
                            L8: Cs-(Cds-Cdd-Cd)CsOsH
                L5: Cs-CdsCdsOsH
                    L6: Cs-(Cds-Od)(Cds-Od)OsH
                    L6: Cs-(Cds-Od)(Cds-Cd)OsH
                        L7: Cs-(Cds-Od)(Cds-Cds)OsH
                        L7: Cs-(Cds-Od)(Cds-Cdd)OsH
                            L8: Cs-(Cds-Od)(Cds-Cdd-Od)OsH
                            L8: Cs-(Cds-Od)(Cds-Cdd-Cd)OsH
                    L6: Cs-(Cds-Cd)(Cds-Cd)OsH
                        L7: Cs-(Cds-Cds)(Cds-Cds)OsH
                        L7: Cs-(Cds-Cdd)(Cds-Cds)OsH
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cds)OsH
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)OsH
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)OsH
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)OsH
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)OsH
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)OsH
                L5: Cs-CtCsOsH
                L5: Cs-CtCdsOsH
                    L6: Cs-(Cds-Od)CtOsH
                    L6: Cs-(Cds-Cd)CtOsH
                        L7: Cs-(Cds-Cds)CtOsH
                        L7: Cs-(Cds-Cdd)CtOsH
                            L8: Cs-(Cds-Cdd-Od)CtOsH
                            L8: Cs-(Cds-Cdd-Cd)CtOsH
                L5: Cs-CtCtOsH
                L5: Cs-CbCsOsH
                L5: Cs-CbCdsOsH
                    L6: Cs-(Cds-Od)CbOsH
                    L6: Cs-(Cds-Cd)CbOsH
                        L7: Cs-(Cds-Cds)CbOsH
                        L7: Cs-(Cds-Cdd)CbOsH
                            L8: Cs-(Cds-Cdd-Od)CbOsH
                            L8: Cs-(Cds-Cdd-Cd)CbOsH
                L5: Cs-CbCtOsH
                L5: Cs-CbCbOsH
            L4: Cs-COsHH
                L5: Cs-CsOsHH
                L5: Cs-CdsOsHH
                    L6: Cs-(Cds-Od)OsHH
                    L6: Cs-(Cds-Cd)OsHH
                        L7: Cs-(Cds-Cds)OsHH
                        L7: Cs-(Cds-Cdd)OsHH
                            L8: Cs-(Cds-Cdd-Od)OsHH
                            L8: Cs-(Cds-Cdd-Cd)OsHH
                L5: Cs-CtOsHH
                L5: Cs-CbOsHH
    L2: O
        L3: Od
            L4: Od-Cd
            L4: Od-Od
        L3: Os
            L4: Os-HH
            L4: Os-OsH
            L4: Os-OsOs
            L4: Os-CH
                L5: Os-CtH
                L5: Os-CdsH
                    L6: Os-(Cds-Od)H
                    L6: Os-(Cds-Cd)H
                L5: Os-CsH
                L5: Os-CbH
            L4: Os-OsC
                L5: Os-OsCt
                L5: Os-OsCds
                    L6: Os-Os(Cds-Od)
                    L6: Os-Os(Cds-Cd)
                L5: Os-OsCs
                L5: Os-OsCb
            L4: Os-CC
                L5: Os-CtCt
                L5: Os-CtCds
                    L6: Os-Ct(Cds-Od)
                    L6: Os-Ct(Cds-Cd)
                L5: Os-CtCs
                L5: Os-CtCb
                L5: Os-CdsCds
                    L6: Os-(Cds-Od)(Cds-Od)
                    L6: Os-(Cds-Od)(Cds-Cd)
                    L6: Os-(Cds-Cd)(Cds-Cd)
                L5: Os-CdsCs
                    L6: Os-Cs(Cds-Od)
                    L6: Os-Cs(Cds-Cd)
                L5: Os-CdsCb
                    L6: Os-Cb(Cds-Od)
                    L6: Os-Cb(Cds-Cd)
                L5: Os-CsCs
                L5: Os-CsCb
                L5: Os-CbCb
    L2: Si
    L2: S
"""
)

