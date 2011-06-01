#!/usr/bin/env python
# encoding: utf-8

name = "DFT_QCI_thermo"
shortDesc = ""
longDesc = """

"""

entry(
    index = -1,
    label = "CH2CHCCH2",
    molecule = 
"""
1     C     0 {2,D}
2     C     1 {1,D} {3,S}
3     C     0 {2,S} {4,D}
4     C     0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = -1,
    label = "OCCO(S)",
    molecule = 
"""
1     O     0 {2,D}
2     C     0 {1,D} {3,D}
3     C     0 {2,D} {4,D}
4     O     0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = -1,
    label = "npropoxy",
    molecule = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S}
3     C     0 {2,S} {4,S}
4     O     1 {3,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1,
    label = "CH3",
    molecule = 
"""
1     C     1
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([9.36,10.11,10.85,11.55,12.86,14.03,16.21],"cal/(mol*K)"),
        H298 = (35.25,"kcal/mol"),
        S298 = (46.44,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2,
    label = "HOOH",
    molecule = 
"""
1     O     0 {2,S}
2     O     0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([9.9,10.83,11.73,12.5,13.72,14.66,16.28],"cal/(mol*K)"),
        H298 = (-32.55,"kcal/mol"),
        S298 = (55.78,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 3,
    label = "CH2O",
    molecule = 
"""
1     C     0 {2,D}
2     O     0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([8.44,9.33,10.38,11.42,13.25,14.69,16.9],"cal/(mol*K)"),
        H298 = (-26.22,"kcal/mol"),
        S298 = (52.16,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 4,
    label = "CH3O",
    molecule = 
"""
1     C     0 {2,S}
2     O     1 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([9.87,11.64,13.32,14.81,17.21,19.04,21.89],"cal/(mol*K)"),
        H298 = (4.87,"kcal/mol"),
        S298 = (54.42,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 5,
    label = "CH2OH",
    molecule = 
"""
1     C     1 {2,S}
2     O     0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([11.45,12.96,14.32,15.46,17.23,18.59,20.93],"cal/(mol*K)"),
        H298 = (-3.84,"kcal/mol"),
        S298 = (58.19,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 6,
    label = "CH3OH",
    molecule = 
"""
1     C     0 {2,S}
2     O     0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([10.59,12.35,14.25,16.01,18.95,21.25,25.02],"cal/(mol*K)"),
        H298 = (-48.47,"kcal/mol"),
        S298 = (57.18,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 7,
    label = "HOCO",
    molecule = 
"""
1     C     1 {2,D} {3,S}
2     O     0 {1,D}
3     O     0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([11.25,12.8,13.96,14.84,16.08,16.88,17.91],"cal/(mol*K)"),
        H298 = (-44.11,"kcal/mol"),
        S298 = (60.19,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 8,
    label = "formyloxy",
    molecule = 
"""
1     C     0 {2,D} {3,S}
2     O     0 {1,D}
3     O     1 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([9.81,11.32,12.68,13.78,15.39,16.47,17.98],"cal/(mol*K)"),
        H298 = (-29.51,"kcal/mol"),
        S298 = (59.94,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 9,
    label = "CH3OO",
    molecule = 
"""
1     C     0 {2,S}
2     O     0 {1,S} {3,S}
3     O     1 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([12.08,14.18,16.24,18.05,20.9,23.01,26.26],"cal/(mol*K)"),
        H298 = (3.82,"kcal/mol"),
        S298 = (64.41,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 10,
    label = "formylperoxyl",
    molecule = 
"""
1     C     0 {2,D} {3,S}
2     O     0 {1,D}
3     O     0 {1,S} {4,S}
4     O     1 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([14.25,16.54,18.3,19.62,21.42,22.5,23.78],"cal/(mol*K)"),
        H298 = (-24.8,"kcal/mol"),
        S298 = (66.19,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 11,
    label = "OCHCH2CH2OOH",
    molecule = 
"""
1     O     0 {2,D}
2     C     0 {1,D} {3,S}
3     C     0 {2,S} {4,S}
4     C     0 {3,S} {5,S}
5     O     0 {4,S} {6,S}
6     O     0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([29.4,33.27,36.95,40.23,45.51,49.44,55.47],"cal/(mol*K)"),
        H298 = (-60.73,"kcal/mol"),
        S298 = (89.68,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 12,
    label = "CH3COCH2OOH",
    molecule = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S} {4,D}
3     C     0 {2,S} {5,S}
4     O     0 {2,D}
5     O     0 {3,S} {6,S}
6     O     0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([28.37,33.77,38.22,41.77,46.97,50.61,56.09],"cal/(mol*K)"),
        H298 = (-67.94,"kcal/mol"),
        S298 = (85.82,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 13,
    label = "cC2H3OCH2OOH",
    molecule = 
"""
1     O     0 {2,S} {3,S}
2     C     0 {1,S} {3,S}
3     C     0 {1,S} {2,S} {4,S}
4     C     0 {3,S} {5,S}
5     O     0 {4,S} {6,S}
6     O     0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([28.9,34.87,39.57,43.17,48.19,51.59,56.8],"cal/(mol*K)"),
        H298 = (-39.31,"kcal/mol"),
        S298 = (80.91,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 14,
    label = "HCO",
    molecule = 
"""
1     C     1 {2,D}
2     O     0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([8.25,8.68,9.18,9.68,10.6,11.34,12.47],"cal/(mol*K)"),
        H298 = (10.08,"kcal/mol"),
        S298 = (53.51,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 15,
    label = "formic_acid",
    molecule = 
"""
1     C     0 {2,D} {3,S}
2     O     0 {1,D}
3     O     0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([11.02,13.15,15.14,16.85,19.42,21.14,23.32],"cal/(mol*K)"),
        H298 = (-90.87,"kcal/mol"),
        S298 = (59.46,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 16,
    label = "CH3OOH",
    molecule = 
"""
1     C     0 {2,S}
2     O     0 {1,S} {3,S}
3     O     0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([14.62,17.11,19.4,21.37,24.47,26.79,30.47],"cal/(mol*K)"),
        H298 = (-30.39,"kcal/mol"),
        S298 = (67.11,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 17,
    label = "CH3CH2OCH2",
    molecule = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {4,S}
4     C     1 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([21.44,25.7,29.73,33.23,38.79,42.95,49.45],"cal/(mol*K)"),
        H298 = (-6.92,"kcal/mol"),
        S298 = (76.06,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 18,
    label = "CH2CH2OCH3",
    molecule = 
"""
1     C     1 {2,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {4,S}
4     C     0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([21.21,25.3,29.2,32.66,38.26,42.51,49.21],"cal/(mol*K)"),
        H298 = (-0.95,"kcal/mol"),
        S298 = (77.59,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 19,
    label = "CH3CHOCH3",
    molecule = 
"""
1     C     0 {2,S}
2     C     1 {1,S} {3,S}
3     O     0 {2,S} {4,S}
4     C     0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([21.48,25.8,29.73,33.09,38.46,42.58,49.16],"cal/(mol*K)"),
        H298 = (-8.27,"kcal/mol"),
        S298 = (75.54,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 20,
    label = "CH3CH2CHOH",
    molecule = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S}
3     C     1 {2,S} {4,S}
4     O     0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([21.22,25.67,29.69,33.11,38.51,42.57,49.06],"cal/(mol*K)"),
        H298 = (-17.02,"kcal/mol"),
        S298 = (78.74,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 21,
    label = "CH3CHOHCH2",
    molecule = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S} {4,S}
3     C     1 {2,S}
4     O     0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([22.67,26.97,30.74,33.91,38.93,42.77,49.05],"cal/(mol*K)"),
        H298 = (-14.14,"kcal/mol"),
        S298 = (76.56,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 22,
    label = "CH3COHCH3",
    molecule = 
"""
1     C     0 {2,S}
2     C     1 {1,S} {3,S} {4,S}
3     C     0 {2,S}
4     O     0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([21.77,26.05,29.95,33.3,38.64,42.68,49.13],"cal/(mol*K)"),
        H298 = (-22.33,"kcal/mol"),
        S298 = (74.56,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 23,
    label = "ipropoxy",
    molecule = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S} {4,S}
3     C     0 {2,S}
4     O     1 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([20.83,25.56,29.74,33.3,38.96,43.24,50],"cal/(mol*K)"),
        H298 = (-9.85,"kcal/mol"),
        S298 = (72.53,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 24,
    label = "CH2CH2CH2OH",
    molecule = 
"""
1     C     1 {2,S}
2     C     0 {1,S} {3,S}
3     C     0 {2,S} {4,S}
4     O     0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([22.04,26.17,30.07,33.41,38.68,42.66,49.06],"cal/(mol*K)"),
        H298 = (-10.97,"kcal/mol"),
        S298 = (79.48,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 25,
    label = "CH3CHCH2OH",
    molecule = 
"""
1     C     0 {2,S}
2     C     1 {1,S} {3,S}
3     C     0 {2,S} {4,S}
4     O     0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([21.04,25.11,28.98,32.38,37.87,42.05,48.76],"cal/(mol*K)"),
        H298 = (-13.23,"kcal/mol"),
        S298 = (80.42,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 26,
    label = "C3H8",
    molecule = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S}
3     C     0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([17.76,22.39,26.7,30.47,36.6,41.32,48.85],"cal/(mol*K)"),
        H298 = (-24.27,"kcal/mol"),
        S298 = (66.07,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 27,
    label = "CH2CCO",
    molecule = 
"""
1     C     0 {2,D}
2     C     0 {1,D} {3,D}
3     C     0 {2,D} {4,D}
4     O     0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([15.09,17.26,19.13,20.72,23.23,25.1,27.95],"cal/(mol*K)"),
        H298 = (33.02,"kcal/mol"),
        S298 = (66.05,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 28,
    label = "propynal",
    molecule = 
"""
1     C     0 {2,T}
2     C     0 {1,T} {3,S}
3     C     0 {2,S} {4,D}
4     O     0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([15.1,17.48,19.41,20.99,23.45,25.24,27.98],"cal/(mol*K)"),
        H298 = (33.48,"kcal/mol"),
        S298 = (65.54,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 29,
    label = "oxirane",
    molecule = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([11.43,14.85,17.98,20.59,24.54,27.39,31.72],"cal/(mol*K)"),
        H298 = (-12.07,"kcal/mol"),
        S298 = (57.94,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 30,
    label = "ethenol",
    molecule = 
"""
1     C     0 {2,D}
2     C     0 {1,D} {3,S}
3     O     0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([15.02,18.07,20.54,22.51,25.45,27.61,31.14],"cal/(mol*K)"),
        H298 = (-29.12,"kcal/mol"),
        S298 = (62.18,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 31,
    label = "CH3CHO",
    molecule = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,D}
3     O     0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([12.97,15.48,17.95,20.18,23.83,26.59,30.87],"cal/(mol*K)"),
        H298 = (-39.24,"kcal/mol"),
        S298 = (62.99,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 32,
    label = "CH3CH2O",
    molecule = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S}
3     O     1 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([15.8,18.82,21.65,24.13,28.15,31.21,36.01],"cal/(mol*K)"),
        H298 = (-2.66,"kcal/mol"),
        S298 = (66.84,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 33,
    label = "CH3OCH2",
    molecule = 
"""
1     C     1 {2,S}
2     O     0 {1,S} {3,S}
3     C     0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([15.53,18.29,21.02,23.46,27.41,30.39,35.08],"cal/(mol*K)"),
        H298 = (0.73,"kcal/mol"),
        S298 = (67.32,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 34,
    label = "CH2CH2OH",
    molecule = 
"""
1     C     1 {2,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([16.84,19.49,21.95,24.11,27.6,30.31,34.79],"cal/(mol*K)"),
        H298 = (-5.79,"kcal/mol"),
        S298 = (69.42,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 35,
    label = "CH3CHOH",
    molecule = 
"""
1     C     0 {2,S}
2     C     1 {1,S} {3,S}
3     O     0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([15.82,18.76,21.49,23.84,27.55,30.36,34.89],"cal/(mol*K)"),
        H298 = (-12.92,"kcal/mol"),
        S298 = (68.09,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 36,
    label = "C2H3O2",
    molecule = 
"""
1     C     0 {2,D}
2     C     0 {1,D} {3,S}
3     O     0 {2,S} {4,S}
4     O     1 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([16.8,20.06,22.7,24.76,27.69,29.68,32.63],"cal/(mol*K)"),
        H298 = (28.07,"kcal/mol"),
        S298 = (68.05,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 37,
    label = "CHCHOOH",
    molecule = 
"""
1     C     1 {2,D}
2     C     0 {1,D} {3,S}
3     O     0 {2,S} {4,S}
4     O     0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([18.5,21.01,23.09,24.72,27.09,28.79,31.5],"cal/(mol*K)"),
        H298 = (54.77,"kcal/mol"),
        S298 = (74.8,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 38,
    label = "OCH2CHO",
    molecule = 
"""
1     O     0 {2,D}
2     C     0 {1,D} {3,S}
3     C     0 {2,S} {4,S}
4     O     1 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([15.74,19.02,21.8,24.02,27.24,29.44,32.62],"cal/(mol*K)"),
        H298 = (-18.04,"kcal/mol"),
        S298 = (70.09,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 39,
    label = "CH2OCOH",
    molecule = 
"""
1     C     1 {2,S}
2     O     0 {1,S} {3,S}
3     C     0 {2,S} {4,D}
4     O     0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([17.17,20.16,22.87,25.13,28.42,30.56,33.29],"cal/(mol*K)"),
        H298 = (-37.47,"kcal/mol"),
        S298 = (70.12,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 40,
    label = "CH3OCO",
    molecule = 
"""
1     C     0 {2,S}
2     O     0 {1,S} {3,S}
3     C     1 {2,S} {4,D}
4     O     0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([15.26,17.74,20.19,22.37,25.81,28.27,31.76],"cal/(mol*K)"),
        H298 = (-37.83,"kcal/mol"),
        S298 = (70.5,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 41,
    label = "cC2H3O2",
    molecule = 
"""
1     O     1 {2,S}
2     C     0 {1,S} {3,S} {4,S}
3     C     0 {2,S} {4,S}
4     O     0 {2,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([15.49,18.87,21.7,23.96,27.29,29.62,33.07],"cal/(mol*K)"),
        H298 = (-8.75,"kcal/mol"),
        S298 = (66.41,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 42,
    label = "acetyloxy",
    molecule = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,D} {4,S}
3     O     0 {2,D}
4     O     1 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([14.61,17.66,20.34,22.56,25.94,28.35,31.93],"cal/(mol*K)"),
        H298 = (-44.66,"kcal/mol"),
        S298 = (67.74,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 43,
    label = "CH2COOH",
    molecule = 
"""
1     C     1 {2,S}
2     C     0 {1,S} {3,D} {4,S}
3     O     0 {2,D}
4     O     0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([16.49,19.87,22.65,24.95,28.45,30.84,33.78],"cal/(mol*K)"),
        H298 = (-55.81,"kcal/mol"),
        S298 = (67.8,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 44,
    label = "OCHOOH",
    molecule = 
"""
1     C     0 {2,D} {3,S}
2     O     0 {1,D}
3     O     0 {1,S} {4,S}
4     O     0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([17.22,19.74,21.35,22.49,24.14,25.39,27.47],"cal/(mol*K)"),
        H298 = (-68.9,"kcal/mol"),
        S298 = (67.24,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 45,
    label = "ethanol",
    molecule = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([15.67,19.24,22.57,25.46,30.09,33.6,39.27],"cal/(mol*K)"),
        H298 = (-56.24,"kcal/mol"),
        S298 = (66.77,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 46,
    label = "CH3OCH3",
    molecule = 
"""
1     C     0 {2,S}
2     O     0 {1,S} {3,S}
3     C     0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([15.77,18.92,22.07,24.95,29.76,33.49,39.39],"cal/(mol*K)"),
        H298 = (-43.93,"kcal/mol"),
        S298 = (63.86,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 47,
    label = "C2H6",
    molecule = 
"""
1     C     0 {2,S}
2     C     0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([12.57,15.51,18.42,21.06,25.49,28.96,34.59],"cal/(mol*K)"),
        H298 = (-19.5,"kcal/mol"),
        S298 = (54.73,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 48,
    label = "OCHCO",
    molecule = 
"""
1     O     0 {2,D}
2     C     0 {1,D} {3,S}
3     C     1 {2,S} {4,D}
4     O     0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([13.86,15.6,17.09,18.33,20.23,21.56,23.46],"cal/(mol*K)"),
        H298 = (-14.75,"kcal/mol"),
        S298 = (67.19,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 49,
    label = "OCCOH",
    molecule = 
"""
1     O     1 {2,S}
2     C     0 {1,S} {3,T}
3     C     0 {2,T} {4,S}
4     O     0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([14.28,16.05,17.47,18.61,20.3,21.48,23.25],"cal/(mol*K)"),
        H298 = (5.93,"kcal/mol"),
        S298 = (65.75,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 50,
    label = "C3H3",
    molecule = 
"""
1     C     0 {2,D}
2     C     0 {1,D} {3,D}
3     C     1 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([14.9,17.21,19,20.43,22.68,24.42,27.32],"cal/(mol*K)"),
        H298 = (86.21,"kcal/mol"),
        S298 = (60.63,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 51,
    label = "H2CC",
    molecule = 
"""
1     C     2S {2,D}
2     C     0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([10.53,11.5,12.36,13.11,14.38,15.42,17.18],"cal/(mol*K)"),
        H298 = (99.43,"kcal/mol"),
        S298 = (54.47,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 52,
    label = "H2CC(T)",
    molecule = 
"""
1     C     2T {2,D}
2     C     0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([9.32,10.47,11.54,12.48,14.03,15.22,17.13],"cal/(mol*K)"),
        H298 = (146.96,"kcal/mol"),
        S298 = (55.63,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 53,
    label = "C2H2",
    molecule = 
"""
1     C     0 {2,T}
2     C     0 {1,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([10.27,11.79,12.85,13.67,14.94,15.97,17.79],"cal/(mol*K)"),
        H298 = (56.1,"kcal/mol"),
        S298 = (47.73,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 54,
    label = "C2H2JJ",
    molecule = 
"""
1     C     1 {2,D}
2     C     1 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([9.63,10.9,11.97,12.88,14.32,15.44,17.25],"cal/(mol*K)"),
        H298 = (144.72,"kcal/mol"),
        S298 = (54.21,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 55,
    label = "C2H3",
    molecule = 
"""
1     C     1 {2,D}
2     C     0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([10.41,12.28,13.89,15.23,17.38,19.05,21.77],"cal/(mol*K)"),
        H298 = (72.2,"kcal/mol"),
        S298 = (55.78,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 56,
    label = "C2H4JJ",
    molecule = 
"""
1     C     1 {2,S}
2     C     1 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([13.22,15.37,17.19,18.72,21.23,23.22,26.51],"cal/(mol*K)"),
        H298 = (79.52,"kcal/mol"),
        S298 = (57.01,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 57,
    label = "C2H4",
    molecule = 
"""
1     C     0 {2,D}
2     C     0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([10.17,12.51,14.73,16.67,19.8,22.2,26.08],"cal/(mol*K)"),
        H298 = (13.55,"kcal/mol"),
        S298 = (52.25,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 58,
    label = "glyoxal",
    molecule = 
"""
1     O     0 {2,D}
2     C     0 {1,D} {3,S}
3     C     0 {2,S} {4,D}
4     O     0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([14.48,17.03,19.41,21.41,24.26,26.01,28.19],"cal/(mol*K)"),
        H298 = (-50.74,"kcal/mol"),
        S298 = (64.55,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 59,
    label = "lactone",
    molecule = 
"""
1     O     0 {2,D}
2     C     0 {1,D} {3,S} {4,S}
3     C     0 {2,S} {4,S}
4     O     0 {2,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([13.08,15.99,18.41,20.35,23.2,25.16,28.02],"cal/(mol*K)"),
        H298 = (-40.91,"kcal/mol"),
        S298 = (63.08,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 60,
    label = "hydroxyketene",
    molecule = 
"""
1     O     0 {2,S}
2     C     0 {1,S} {3,D}
3     C     0 {2,D} {4,D}
4     O     0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([15.92,18.16,19.88,21.24,23.27,24.75,27.13],"cal/(mol*K)"),
        H298 = (-35.59,"kcal/mol"),
        S298 = (66.58,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 61,
    label = "C32CH2OOH",
    molecule = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {4,S}
4     O     0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([20,24.1,27.75,30.83,35.65,39.22,44.8],"cal/(mol*K)"),
        H298 = (-37.78,"kcal/mol"),
        S298 = (75.15,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 62,
    label = "CH3OOCH3",
    molecule = 
"""
1     C     0 {2,S}
2     O     0 {1,S} {3,S}
3     O     0 {2,S} {4,S}
4     C     0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([19.47,23.3,26.88,30,35.04,38.86,44.84],"cal/(mol*K)"),
        H298 = (-28.59,"kcal/mol"),
        S298 = (72.22,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 63,
    label = "CH2CHCH2OOH",
    molecule = 
"""
1     C     0 {2,D}
2     C     0 {1,D} {3,S}
3     C     0 {2,S} {4,S}
4     O     0 {3,S} {5,S}
5     O     0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([25.13,29.03,32.69,35.84,40.8,44.47,50.25],"cal/(mol*K)"),
        H298 = (-10.19,"kcal/mol"),
        S298 = (82.03,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 64,
    label = "propen1ooh",
    molecule = 
"""
1     C     0 {2,D} {4,S}
2     C     0 {1,D} {3,S}
3     C     0 {2,S}
4     O     0 {1,S} {5,S}
5     O     0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([23.58,28.05,31.99,35.3,40.41,44.17,50.07],"cal/(mol*K)"),
        H298 = (-13.57,"kcal/mol"),
        S298 = (81.56,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 65,
    label = "propen2ooh",
    molecule = 
"""
1     C     0 {2,D}
2     C     0 {1,D} {3,S} {4,S}
3     C     0 {2,S}
4     O     0 {2,S} {5,S}
5     O     0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([24.92,29.7,33.46,36.48,41.12,44.6,50.2],"cal/(mol*K)"),
        H298 = (-18.11,"kcal/mol"),
        S298 = (78.9,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 66,
    label = "npropylooh",
    molecule = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S}
3     C     0 {2,S} {4,S}
4     O     0 {3,S} {5,S}
5     O     0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([25.71,31.19,36.07,40.2,46.68,51.49,59.01],"cal/(mol*K)"),
        H298 = (-42.14,"kcal/mol"),
        S298 = (84.19,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 67,
    label = "ipropylooh",
    molecule = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S} {4,S}
3     C     0 {2,S}
4     O     0 {2,S} {5,S}
5     O     0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([26.88,32.34,37.1,41.08,47.29,51.9,59.17],"cal/(mol*K)"),
        H298 = (-46.52,"kcal/mol"),
        S298 = (82.43,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 68,
    label = "CH2CHCO",
    molecule = 
"""
1     C     0 {2,D}
2     C     0 {1,D} {3,S}
3     C     1 {2,S} {4,D}
4     O     0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([15.61,18.59,21.17,23.32,26.65,29.05,32.71],"cal/(mol*K)"),
        H298 = (24.52,"kcal/mol"),
        S298 = (67.91,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 69,
    label = "CH2CCHO",
    molecule = 
"""
1     C     0 {2,D}
2     C     1 {1,D} {3,S}
3     C     0 {2,S} {4,D}
4     O     0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([16.31,19.12,21.61,23.72,27.02,29.41,32.99],"cal/(mol*K)"),
        H298 = (46.45,"kcal/mol"),
        S298 = (70.26,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 70,
    label = "CHCHCHO",
    molecule = 
"""
1     C     1 {2,D}
2     C     0 {1,D} {3,S}
3     C     0 {2,S} {4,D}
4     O     0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([16.24,19.74,22.69,25.03,28.29,30.37,33.17],"cal/(mol*K)"),
        H298 = (45.67,"kcal/mol"),
        S298 = (67.33,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 71,
    label = "C2H5",
    molecule = 
"""
1     C     1 {2,S}
2     C     0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([12.25,14.77,17.18,19.31,22.84,25.61,30.13],"cal/(mol*K)"),
        H298 = (29.43,"kcal/mol"),
        S298 = (59.12,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 72,
    label = "oxiranyl",
    molecule = 
"""
1     C     1 {2,S} {3,S}
2     C     0 {1,S} {3,S}
3     O     0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([11.24,14.16,16.71,18.77,21.83,23.99,27.26],"cal/(mol*K)"),
        H298 = (40.22,"kcal/mol"),
        S298 = (60.35,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 73,
    label = "CHCHOH",
    molecule = 
"""
1     C     1 {2,D}
2     C     0 {1,D} {3,S}
3     O     0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([14.65,17.72,20,21.59,23.58,24.88,27.02],"cal/(mol*K)"),
        H298 = (32.17,"kcal/mol"),
        S298 = (62.75,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 74,
    label = "CH2COH",
    molecule = 
"""
1     C     0 {2,D}
2     C     1 {1,D} {3,S}
3     O     0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([14.36,16.86,18.74,20.19,22.32,23.9,26.53],"cal/(mol*K)"),
        H298 = (28.54,"kcal/mol"),
        S298 = (64.12,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 75,
    label = "vinoxy",
    molecule = 
"""
1     C     1 {2,S}
2     C     0 {1,S} {3,D}
3     O     0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([12.72,15.28,17.49,19.32,22.13,24.19,27.35],"cal/(mol*K)"),
        H298 = (4.75,"kcal/mol"),
        S298 = (61.85,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 76,
    label = "acetyl",
    molecule = 
"""
1     C     1 {2,D} {3,S}
2     O     0 {1,D}
3     C     0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([12.06,14.11,16.08,17.82,20.67,22.81,26.16],"cal/(mol*K)"),
        H298 = (-1.95,"kcal/mol"),
        S298 = (63.74,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 77,
    label = "C2H5O2",
    molecule = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {4,S}
4     O     1 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([17.58,21.35,24.74,27.61,32.09,35.39,40.51],"cal/(mol*K)"),
        H298 = (-4.07,"kcal/mol"),
        S298 = (74.15,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 78,
    label = "CH2CH2OOH",
    molecule = 
"""
1     C     1 {2,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {4,S}
4     O     0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([19.84,23.33,26.39,28.92,32.8,35.65,40.14],"cal/(mol*K)"),
        H298 = (12.88,"kcal/mol"),
        S298 = (79.03,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 79,
    label = "allene",
    molecule = 
"""
1     C     0 {2,D}
2     C     0 {1,D} {3,D}
3     C     0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([13.97,17.02,19.63,21.79,25.18,27.73,31.82],"cal/(mol*K)"),
        H298 = (47.11,"kcal/mol"),
        S298 = (59.34,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 80,
    label = "propyne",
    molecule = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,T}
3     C     0 {2,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([14.37,17.14,19.55,21.6,24.93,27.49,31.65],"cal/(mol*K)"),
        H298 = (46.16,"kcal/mol"),
        S298 = (58.99,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 81,
    label = "cC3H4",
    molecule = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {3,D}
3     C     0 {1,S} {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([12.51,16.02,19.01,21.43,25.07,27.72,31.84],"cal/(mol*K)"),
        H298 = (69.38,"kcal/mol"),
        S298 = (58.01,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 82,
    label = "npropyl",
    molecule = 
"""
1     C     1 {2,S}
2     C     0 {1,S} {3,S}
3     C     0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([17.39,21.53,25.29,28.54,33.78,37.81,44.29],"cal/(mol*K)"),
        H298 = (25.21,"kcal/mol"),
        S298 = (69.28,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 83,
    label = "ipropyl",
    molecule = 
"""
1     C     0 {2,S}
2     C     1 {1,S} {3,S}
3     C     0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([16.37,20.25,24.07,27.48,33.07,37.34,44.11],"cal/(mol*K)"),
        H298 = (26.01,"kcal/mol"),
        S298 = (68.9,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 84,
    label = "ethynol",
    molecule = 
"""
1     C     0 {2,T}
2     C     0 {1,T} {3,S}
3     O     0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([13.44,15.17,16.46,17.47,19.01,20.21,22.29],"cal/(mol*K)"),
        H298 = (23.15,"kcal/mol"),
        S298 = (59.1,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 85,
    label = "ketene",
    molecule = 
"""
1     C     0 {2,D}
2     C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([12.31,14.11,15.57,16.77,18.67,20.12,22.44],"cal/(mol*K)"),
        H298 = (-10.78,"kcal/mol"),
        S298 = (57.63,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 86,
    label = "oxirene",
    molecule = 
"""
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {3,S}
3     O     0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([13.18,15.06,16.52,17.67,19.38,20.64,22.68],"cal/(mol*K)"),
        H298 = (65.92,"kcal/mol"),
        S298 = (60.48,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 87,
    label = "CHCHOjj",
    molecule = 
"""
1     C     1 {2,D}
2     C     0 {1,D} {3,S}
3     O     1 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([13.11,15.21,16.88,18.18,19.98,21.14,22.73],"cal/(mol*K)"),
        H298 = (39.29,"kcal/mol"),
        S298 = (62.75,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 88,
    label = "allyl",
    molecule = 
"""
1     C     0 {2,D}
2     C     0 {1,D} {3,S}
3     C     1 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([14.89,18.72,21.97,24.63,28.72,31.76,36.6],"cal/(mol*K)"),
        H298 = (42.04,"kcal/mol"),
        S298 = (61.54,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 89,
    label = "cC3H5",
    molecule = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {3,S}
3     C     1 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([13.61,17.85,21.43,24.32,28.65,31.79,36.69],"cal/(mol*K)"),
        H298 = (71.09,"kcal/mol"),
        S298 = (61.58,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 90,
    label = "propen1yl",
    molecule = 
"""
1     C     0 {2,S}
2     C     1 {1,S} {3,D}
3     C     0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([15.14,18.18,21.04,23.56,27.66,30.78,35.73],"cal/(mol*K)"),
        H298 = (61.96,"kcal/mol"),
        S298 = (65.41,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 91,
    label = "propen2yl",
    molecule = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,D}
3     C     1 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([15.28,18.48,21.36,23.85,27.84,30.89,35.74],"cal/(mol*K)"),
        H298 = (65.51,"kcal/mol"),
        S298 = (64.88,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 92,
    label = "C2H3OOH",
    molecule = 
"""
1     C     0 {2,D}
2     C     0 {1,D} {3,S}
3     O     0 {2,S} {4,S}
4     O     0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([18.38,21.58,24.39,26.69,30.1,32.51,36.24],"cal/(mol*K)"),
        H298 = (-7.9,"kcal/mol"),
        S298 = (73.04,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 93,
    label = "acetic_acid",
    molecule = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,D} {4,S}
3     O     0 {2,D}
4     O     0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([15.6,19.25,22.52,25.35,29.79,33,37.45],"cal/(mol*K)"),
        H298 = (-103.2,"kcal/mol"),
        S298 = (68.19,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 94,
    label = "methyl_formate",
    molecule = 
"""
1     C     0 {2,S}
2     O     0 {1,S} {3,S}
3     C     0 {2,S} {4,D}
4     O     0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([15.45,18.67,21.95,24.91,29.59,32.89,37.38],"cal/(mol*K)"),
        H298 = (-85.78,"kcal/mol"),
        S298 = (69,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 95,
    label = "HOOCH2CH2CH2OO",
    molecule = 
"""
1     O     0 {2,S}
2     O     0 {1,S} {3,S}
3     C     0 {2,S} {4,S}
4     C     0 {3,S} {5,S}
5     C     0 {4,S} {6,S}
6     O     0 {5,S} {7,S}
7     O     1 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([34.87,40.13,44.71,48.53,54.44,58.75,65.38],"cal/(mol*K)"),
        H298 = (-26.53,"kcal/mol"),
        S298 = (97.98,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 96,
    label = "CH3CHOOCH2OOH",
    molecule = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S} {6,S}
3     C     0 {2,S} {4,S}
4     O     0 {3,S} {5,S}
5     O     0 {4,S}
6     O     0 {2,S} {7,S}
7     O     1 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([36.16,41.94,46.34,49.78,55.07,59.08,65.5],"cal/(mol*K)"),
        H298 = (-29.64,"kcal/mol"),
        S298 = (95.85,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 97,
    label = "CH3CHOOHCH2OO",
    molecule = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S} {6,S}
3     C     0 {2,S} {4,S}
4     O     0 {3,S} {5,S}
5     O     1 {4,S}
6     O     0 {2,S} {7,S}
7     O     0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([36.52,42.43,47.25,51.04,56.52,60.37,66.33],"cal/(mol*K)"),
        H298 = (-29.54,"kcal/mol"),
        S298 = (95.57,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 98,
    label = "HOOCH2CHCH2OOH",
    molecule = 
"""
1     O     0 {2,S}
2     O     0 {1,S} {3,S}
3     C     0 {2,S} {4,S}
4     C     1 {3,S} {5,S}
5     C     0 {4,S} {6,S}
6     O     0 {5,S} {7,S}
7     O     0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([38.23,48.37,54.36,57.48,60.49,62.48,66.33],"cal/(mol*K)"),
        H298 = (-14.25,"kcal/mol"),
        S298 = (95.31,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 99,
    label = "CH2CHOOHCH2OOH",
    molecule = 
"""
1     C     1 {2,S}
2     C     0 {1,S} {3,S} {6,S}
3     C     0 {2,S} {4,S}
4     O     0 {3,S} {5,S}
5     O     0 {4,S}
6     O     0 {2,S} {7,S}
7     O     0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([35.63,41.46,46.23,50,55.51,59.4,65.34],"cal/(mol*K)"),
        H298 = (-14.47,"kcal/mol"),
        S298 = (102.1,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 100,
    label = "OHCH2CH2OO",
    molecule = 
"""
1     O     0 {2,D}
2     C     0 {1,D} {3,S}
3     C     0 {2,S} {4,S}
4     C     0 {3,S} {5,S}
5     O     0 {4,S} {6,S}
6     O     1 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([27.2,31.13,34.49,37.42,42.17,45.73,51.19],"cal/(mol*K)"),
        H298 = (-26.3,"kcal/mol"),
        S298 = (88.33,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 101,
    label = "CH3CHOOHCHO",
    molecule = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S} {4,S}
3     C     0 {2,S} {6,D}
4     O     0 {2,S} {5,S}
5     O     0 {4,S}
6     O     0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([28.66,33.76,38.09,41.61,46.84,50.5,56.01],"cal/(mol*K)"),
        H298 = (-63.38,"kcal/mol"),
        S298 = (85.49,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 102,
    label = "oxiranylmethylperoxy",
    molecule = 
"""
1     O     1 {2,S}
2     O     0 {1,S} {3,S}
3     C     0 {2,S} {4,S}
4     C     0 {3,S} {5,S} {6,S}
5     C     0 {4,S} {6,S}
6     O     0 {4,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([23.63,28.6,33.06,36.76,42.29,46.16,51.9],"cal/(mol*K)"),
        H298 = (-2.62,"kcal/mol"),
        S298 = (83.96,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 103,
    label = "HOOCH2CH2OOH",
    molecule = 
"""
1     O     1 {2,S}
2     O     0 {1,S} {3,S}
3     C     0 {2,S} {4,S}
4     C     0 {3,S} {5,S}
5     O     0 {4,S} {6,S}
6     O     0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([29.55,33.82,37.04,39.59,43.54,46.51,51.21],"cal/(mol*K)"),
        H298 = (-20.27,"kcal/mol"),
        S298 = (89.7,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 104,
    label = "CH3CHOOCHO",
    molecule = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S} {5,S}
3     C     0 {2,S} {4,D}
4     O     0 {3,D}
5     O     0 {2,S} {6,S}
6     O     1 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([25.58,30.38,34.46,37.76,42.68,46.16,51.4],"cal/(mol*K)"),
        H298 = (-27.48,"kcal/mol"),
        S298 = (85.46,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 105,
    label = "CH3COCH2OO",
    molecule = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S} {4,D}
3     C     0 {2,S} {5,S}
4     O     0 {2,D}
5     O     0 {3,S} {6,S}
6     O     1 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([25.24,29.96,34,37.3,42.29,45.86,51.26],"cal/(mol*K)"),
        H298 = (-30.79,"kcal/mol"),
        S298 = (86.93,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 106,
    label = "ketenylperoxy",
    molecule = 
"""
1     C     0 {2,D} {4,S}
2     C     0 {1,D} {3,D}
3     O     0 {2,D}
4     O     0 {1,S} {5,S}
5     O     1 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([18.67,20.75,22.36,23.61,25.41,26.65,28.44],"cal/(mol*K)"),
        H298 = (20.5,"kcal/mol"),
        S298 = (75.79,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 107,
    label = "HCCO",
    molecule = 
"""
1     C     1 {2,D}
2     C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([11.97,13.09,13.94,14.64,15.74,16.57,17.91],"cal/(mol*K)"),
        H298 = (37.64,"kcal/mol"),
        S298 = (58.8,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 108,
    label = "cCO3",
    molecule = 
"""
1     C     0 {2,D} {3,S} {4,S}
2     O     0 {1,D}
3     O     0 {1,S} {4,S}
4     O     0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([11.64,13.42,14.74,15.72,17.04,17.84,18.84],"cal/(mol*K)"),
        H298 = (-38.79,"kcal/mol"),
        S298 = (60.99,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 109,
    label = "propene",
    molecule = 
"""
1     C     0 {2,D}
2     C     0 {1,D} {3,S}
3     C     0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([15.33,19.03,22.5,25.54,30.44,34.19,40.14],"cal/(mol*K)"),
        H298 = (6.24,"kcal/mol"),
        S298 = (63.59,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 110,
    label = "cC3H6",
    molecule = 
"""
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {3,S}
3     C     0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([13.36,18.13,22.35,25.82,31.11,34.96,41],"cal/(mol*K)"),
        H298 = (14.26,"kcal/mol"),
        S298 = (59.42,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 111,
    label = "C3H6JJ",
    molecule = 
"""
1     C     1 {2,S}
2     C     1 {1,S} {3,S}
3     C     0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([17.44,20.95,24.16,26.95,31.47,34.95,40.47],"cal/(mol*K)"),
        H298 = (72.55,"kcal/mol"),
        S298 = (70.43,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 112,
    label = "acrolein",
    molecule = 
"""
1     C     0 {2,D}
2     C     0 {1,D} {3,S}
3     C     0 {2,S} {4,D}
4     O     0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([16.87,20.41,23.49,26.1,30.14,33.04,37.3],"cal/(mol*K)"),
        H298 = (-14.2,"kcal/mol"),
        S298 = (65.35,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 113,
    label = "CH3CHCO",
    molecule = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,D}
3     C     0 {2,D} {4,D}
4     O     0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([16.45,19.54,22.36,24.81,28.75,31.71,36.31],"cal/(mol*K)"),
        H298 = (-13.82,"kcal/mol"),
        S298 = (68.58,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 114,
    label = "cC3H4O",
    molecule = 
"""
1     O     0 {2,S} {3,S}
2     C     0 {1,S} {4,D}
3     C     0 {1,S} {4,S}
4     C     0 {2,D} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([14.06,18.44,22.19,25.21,29.64,32.73,37.35],"cal/(mol*K)"),
        H298 = (13.88,"kcal/mol"),
        S298 = (62.93,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 115,
    label = "C3H4OJJ",
    molecule = 
"""
1     C     0 {2,D}
2     C     0 {1,D} {3,S}
3     C     1 {2,S} {4,S}
4     O     1 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([18.77,22.18,25.08,27.48,31.17,33.88,37.99],"cal/(mol*K)"),
        H298 = (47.18,"kcal/mol"),
        S298 = (69.68,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 116,
    label = "O2",
    molecule = 
"""
1     O     1 {2,S}
2     O     1 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([7,7.15,7.37,7.59,7.97,8.24,8.58],"cal/(mol*K)"),
        H298 = (0.68,"kcal/mol"),
        S298 = (46.74,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 117,
    label = "H",
    molecule = 
"""
1     H     1
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.96,4.96,4.96,4.96,4.96,4.96,4.96],"cal/(mol*K)"),
        H298 = (52.1,"kcal/mol"),
        S298 = (27.36,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 118,
    label = "C",
    molecule = 
"""
1     C     4
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.96,4.96,4.96,4.96,4.96,4.96,4.96],"cal/(mol*K)"),
        H298 = (171.29,"kcal/mol"),
        S298 = (35.54,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 119,
    label = "O",
    molecule = 
"""
1     O     2T
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([4.96,4.96,4.96,4.96,4.96,4.96,4.96],"cal/(mol*K)"),
        H298 = (59.64,"kcal/mol"),
        S298 = (36.4,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 120,
    label = "CO",
    molecule = 
"""
1     C     2T {2,D}
2     O     0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([6.95,6.99,7.09,7.24,7.57,7.87,8.34],"cal/(mol*K)"),
        H298 = (-26.44,"kcal/mol"),
        S298 = (47.14,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 121,
    label = "CO2",
    molecule = 
"""
1     C     0 {2,D} {3,D}
2     O     0 {1,D}
3     O     0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([8.87,9.84,10.63,11.26,12.23,12.9,13.82],"cal/(mol*K)"),
        H298 = (-94.36,"kcal/mol"),
        S298 = (50.99,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 122,
    label = "OH",
    molecule = 
"""
1     O     1
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([6.95,6.95,6.95,6.97,7.07,7.23,7.72],"cal/(mol*K)"),
        H298 = (8.69,"kcal/mol"),
        S298 = (42.53,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 123,
    label = "HO2",
    molecule = 
"""
1     O     1 {2,S}
2     O     0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([8.28,8.82,9.38,9.88,10.66,11.26,12.25],"cal/(mol*K)"),
        H298 = (3.07,"kcal/mol"),
        S298 = (54.61,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 124,
    label = "H2O",
    molecule = 
"""
1     O     0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([7.99,8.15,8.37,8.63,9.17,9.73,11.01],"cal/(mol*K)"),
        H298 = (-58.46,"kcal/mol"),
        S298 = (45.02,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 125,
    label = "acetylperoxy",
    molecule = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,D} {4,S}
3     O     0 {2,D}
4     O     0 {2,S} {5,S}
5     O     1 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([19.91,23.07,25.85,28.15,31.56,33.9,37.28],"cal/(mol*K)"),
        H298 = (-36.67,"kcal/mol"),
        S298 = (76.21,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 126,
    label = "hydroperoxyl_acetyl",
    molecule = 
"""
1     C     1 {2,D} {3,S}
2     O     0 {1,D}
3     C     0 {1,S} {4,S}
4     O     0 {3,S} {5,S}
5     O     0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([22.35,25.83,28.49,30.44,33.07,34.81,37.39],"cal/(mol*K)"),
        H298 = (-17.2,"kcal/mol"),
        S298 = (79.32,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 127,
    label = "hydroperoxyl_vinoxy",
    molecule = 
"""
1     C     1 {2,S}
2     C     0 {1,S} {3,D} {4,S}
3     O     0 {2,D}
4     O     0 {2,S} {5,S}
5     O     0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([21.04,25.44,28.98,31.67,35.2,37.28,39.6],"cal/(mol*K)"),
        H298 = (-34.67,"kcal/mol"),
        S298 = (73.73,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 128,
    label = "vinoxyperoxy",
    molecule = 
"""
1     C     0 {2,D} {3,S}
2     O     0 {1,D}
3     C     0 {1,S} {4,S}
4     O     0 {3,S} {5,S}
5     O     1 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([19.79,23.22,26.1,28.39,31.7,33.97,37.29],"cal/(mol*K)"),
        H298 = (-18.09,"kcal/mol"),
        S298 = (77.55,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 129,
    label = "allyloxy",
    molecule = 
"""
1     C     0 {2,D}
2     C     0 {1,D} {3,S}
3     C     0 {2,S} {4,S}
4     O     1 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([18.45,22.37,25.85,28.76,33.26,36.56,41.63],"cal/(mol*K)"),
        H298 = (25.06,"kcal/mol"),
        S298 = (72.63,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 130,
    label = "propen1oxy",
    molecule = 
"""
1     C     0 {2,D} {4,S}
2     C     0 {1,D} {3,S}
3     C     0 {2,S}
4     O     1 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([17.66,21.3,24.73,27.71,32.46,35.99,41.38],"cal/(mol*K)"),
        H298 = (-4.44,"kcal/mol"),
        S298 = (71.94,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 131,
    label = "CH2CH2CHO",
    molecule = 
"""
1     C     1 {2,S}
2     C     0 {1,S} {3,S}
3     C     0 {2,S} {4,D}
4     O     0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([19.41,22.49,25.45,28.06,32.31,35.53,40.59],"cal/(mol*K)"),
        H298 = (7.36,"kcal/mol"),
        S298 = (75.41,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 132,
    label = "oxiranylmethyl",
    molecule = 
"""
1     C     1 {2,S}
2     C     0 {1,S} {3,S} {4,S}
3     C     0 {2,S} {4,S}
4     O     0 {2,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([17.89,22.39,26.16,29.17,33.61,36.79,41.68],"cal/(mol*K)"),
        H298 = (26.63,"kcal/mol"),
        S298 = (68.55,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 133,
    label = "CH2OCHCH2",
    molecule = 
"""
1     C     1 {2,S}
2     O     0 {1,S} {3,S}
3     C     0 {2,S} {4,D}
4     C     0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([19.07,23.06,26.47,29.24,33.39,36.38,41.02],"cal/(mol*K)"),
        H298 = (22.8,"kcal/mol"),
        S298 = (72.91,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 134,
    label = "CH3CHCHO",
    molecule = 
"""
1     C     0 {2,S}
2     C     1 {1,S} {3,S}
3     C     0 {2,S} {4,D}
4     O     0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([18.06,21.58,24.93,27.85,32.53,36.02,41.39],"cal/(mol*K)"),
        H298 = (-4.96,"kcal/mol"),
        S298 = (71.27,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 135,
    label = "CH3CH2CO",
    molecule = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S}
3     C     1 {2,S} {4,D}
4     O     0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([17.76,20.93,24.04,26.82,31.36,34.8,40.18],"cal/(mol*K)"),
        H298 = (-6.18,"kcal/mol"),
        S298 = (74.68,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 136,
    label = "propen2oxy",
    molecule = 
"""
1     C     0 {2,D}
2     C     0 {1,D} {3,S} {4,S}
3     C     0 {2,S}
4     O     1 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([17.86,21.85,25.33,28.26,32.82,36.17,41.25],"cal/(mol*K)"),
        H298 = (-6.15,"kcal/mol"),
        S298 = (72.93,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 137,
    label = "oxetanyl1",
    molecule = 
"""
1     O     0 {2,S} {3,S}
2     C     1 {1,S} {4,S}
3     C     0 {1,S} {4,S}
4     C     0 {2,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([15.35,20.12,24.34,27.8,32.98,36.65,42.16],"cal/(mol*K)"),
        H298 = (25.09,"kcal/mol"),
        S298 = (66.24,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 138,
    label = "oxetanyl2",
    molecule = 
"""
1     O     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {4,S}
4     C     1 {2,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([16.19,20.78,24.88,28.26,33.35,36.97,42.38],"cal/(mol*K)"),
        H298 = (31.23,"kcal/mol"),
        S298 = (66.78,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 139,
    label = "acetone",
    molecule = 
"""
1     O     0 {2,D}
2     C     0 {1,D} {3,S} {4,S}
3     C     0 {2,S}
4     C     0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([17.53,21.65,25.52,28.9,34.34,38.41,44.77],"cal/(mol*K)"),
        H298 = (-51.21,"kcal/mol"),
        S298 = (70.9,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 140,
    label = "propen1ol",
    molecule = 
"""
1     C     0 {2,D} {4,S}
2     C     0 {1,D} {3,S}
3     C     0 {2,S}
4     O     0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([20.67,24.56,28.02,30.98,35.68,39.25,45.02],"cal/(mol*K)"),
        H298 = (-34.7,"kcal/mol"),
        S298 = (70.85,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 141,
    label = "propen2ol",
    molecule = 
"""
1     C     0 {2,D}
2     C     0 {1,D} {3,S} {4,S}
3     C     0 {2,S}
4     O     0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([20.59,25.3,29.06,32.04,36.55,39.89,45.32],"cal/(mol*K)"),
        H298 = (-39.44,"kcal/mol"),
        S298 = (69.6,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 142,
    label = "cC3H6O",
    molecule = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S} {4,S}
3     C     0 {2,S} {4,S}
4     O     0 {2,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([17.38,22.08,26.33,29.92,35.48,39.56,45.86],"cal/(mol*K)"),
        H298 = (-21.56,"kcal/mol"),
        S298 = (67.16,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 143,
    label = "propanal",
    molecule = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S}
3     C     0 {2,S} {4,D}
4     O     0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([18.92,22.42,25.99,29.23,34.57,38.63,44.94],"cal/(mol*K)"),
        H298 = (-43.67,"kcal/mol"),
        S298 = (73.5,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 144,
    label = "propen3ol",
    molecule = 
"""
1     C     0 {2,D}
2     C     0 {1,D} {3,S}
3     C     0 {2,S} {4,S}
4     O     0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([21.54,25.01,28.2,31.01,35.6,39.14,44.92],"cal/(mol*K)"),
        H298 = (-28.93,"kcal/mol"),
        S298 = (72.64,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 145,
    label = "oxetane",
    molecule = 
"""
1     O     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S} {4,S}
4     C     0 {2,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([15.21,20.43,25.24,29.29,35.49,39.92,46.6],"cal/(mol*K)"),
        H298 = (-18.29,"kcal/mol"),
        S298 = (65.61,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 146,
    label = "npropanol",
    molecule = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S}
3     C     0 {2,S} {4,S}
4     O     0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([20.87,25.94,30.62,34.65,41.04,45.85,53.48],"cal/(mol*K)"),
        H298 = (-60.69,"kcal/mol"),
        S298 = (76.31,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 147,
    label = "ipropanol",
    molecule = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S} {4,S}
3     C     0 {2,S}
4     O     0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([21.77,26.89,31.47,35.35,41.49,46.13,53.57],"cal/(mol*K)"),
        H298 = (-64.83,"kcal/mol"),
        S298 = (74.2,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 148,
    label = "CH3CH2OCH3",
    molecule = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {4,S}
4     C     0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([22.57,26.95,31.12,34.9,41.2,46.07,53.78],"cal/(mol*K)"),
        H298 = (-51.54,"kcal/mol"),
        S298 = (73.52,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 149,
    label = "allylperoxy",
    molecule = 
"""
1     C     0 {2,D}
2     C     0 {1,D} {3,S}
3     C     0 {2,S} {4,S}
4     O     0 {3,S} {5,S}
5     O     1 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([21.15,25.43,29.2,32.34,37.16,40.67,46.07],"cal/(mol*K)"),
        H298 = (24.09,"kcal/mol"),
        S298 = (80.56,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 150,
    label = "propen1peroxy",
    molecule = 
"""
1     C     0 {2,D} {4,S}
2     C     0 {1,D} {3,S}
3     C     0 {2,S}
4     O     0 {1,S} {5,S}
5     O     1 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([22.45,26.76,30.5,33.58,38.24,41.57,46.62],"cal/(mol*K)"),
        H298 = (21.11,"kcal/mol"),
        S298 = (76.7,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 151,
    label = "propen2peroxy",
    molecule = 
"""
1     C     0 {2,D}
2     C     0 {1,D} {3,S} {4,S}
3     C     0 {2,S}
4     O     0 {2,S} {5,S}
5     O     1 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([23.08,27.64,31.33,34.26,38.62,41.76,46.64],"cal/(mol*K)"),
        H298 = (17.91,"kcal/mol"),
        S298 = (76.2,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 152,
    label = "CH3CHOCHO",
    molecule = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S} {4,S}
3     C     0 {2,S} {5,D}
4     O     1 {2,S}
5     O     0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([22.13,26.41,30.17,33.3,38.07,41.49,46.64],"cal/(mol*K)"),
        H298 = (-26.53,"kcal/mol"),
        S298 = (78.17,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 153,
    label = "OCHCH2CH2O",
    molecule = 
"""
1     O     1 {2,S}
2     C     0 {1,S} {3,S}
3     C     0 {2,S} {4,S}
4     C     0 {3,S} {5,D}
5     O     0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([20.72,24.95,28.85,32.17,37.3,40.99,46.47],"cal/(mol*K)"),
        H298 = (-25.04,"kcal/mol"),
        S298 = (82.32,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 154,
    label = "CH3COCH2O",
    molecule = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S} {4,D}
3     C     0 {2,S} {5,S}
4     O     0 {2,D}
5     O     1 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([21.08,25.77,29.92,33.34,38.35,41.79,46.82],"cal/(mol*K)"),
        H298 = (-30.7,"kcal/mol"),
        S298 = (78.33,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 155,
    label = "oxiranylmethoxy",
    molecule = 
"""
1     O     1 {2,S}
2     C     0 {1,S} {3,S}
3     C     0 {2,S} {4,S} {5,S}
4     C     0 {3,S} {5,S}
5     O     0 {3,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([19.76,24.69,29.06,32.66,38.02,41.77,47.31],"cal/(mol*K)"),
        H298 = (-2.16,"kcal/mol"),
        S298 = (75.51,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 156,
    label = "npropylperoxy",
    molecule = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S}
3     C     0 {2,S} {4,S}
4     O     0 {3,S} {5,S}
5     O     1 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([23.02,28.24,32.94,36.92,43.11,47.67,54.73],"cal/(mol*K)"),
        H298 = (-8.38,"kcal/mol"),
        S298 = (83.49,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 157,
    label = "QOOH_1",
    molecule = 
"""
1     C     1 {2,S}
2     C     0 {1,S} {3,S}
3     C     0 {2,S} {4,S}
4     O     0 {3,S} {5,S}
5     O     0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([25.27,30.39,34.78,38.41,43.99,48.1,54.53],"cal/(mol*K)"),
        H298 = (7.26,"kcal/mol"),
        S298 = (88.49,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 158,
    label = "QOOH_2",
    molecule = 
"""
1     C     0 {2,S}
2     C     1 {1,S} {3,S}
3     C     0 {2,S} {4,S}
4     O     0 {3,S} {5,S}
5     O     0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([24.29,29.11,33.52,37.27,43.13,47.45,54.15],"cal/(mol*K)"),
        H298 = (5.1,"kcal/mol"),
        S298 = (88.21,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 159,
    label = "QOOH_3",
    molecule = 
"""
1     C     1 {2,S}
2     C     0 {1,S} {3,S} {4,S}
3     C     0 {2,S}
4     O     0 {2,S} {5,S}
5     O     0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([26.48,31.26,35.42,38.88,44.22,48.17,54.42],"cal/(mol*K)"),
        H298 = (4.5,"kcal/mol"),
        S298 = (85.49,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 160,
    label = "ipropylperoxy",
    molecule = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S} {4,S}
3     C     0 {2,S}
4     O     0 {2,S} {5,S}
5     O     1 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([24.25,29.24,33.67,37.42,43.34,47.77,54.72],"cal/(mol*K)"),
        H298 = (-12.99,"kcal/mol"),
        S298 = (80.87,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 161,
    label = "OCH2OOH",
    molecule = 
"""
1     O     1 {2,S}
2     C     0 {1,S} {3,S}
3     O     0 {2,S} {4,S}
4     O     0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([19.06,21.82,23.76,25.27,27.54,29.21,31.87],"cal/(mol*K)"),
        H298 = (-21.33,"kcal/mol"),
        S298 = (72.64,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 162,
    label = "CH4",
    molecule = 
"""
1     C     0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([8.49,9.6,10.97,12.36,14.87,16.97,20.51],"cal/(mol*K)"),
        H298 = (-17.53,"kcal/mol"),
        S298 = (44.41,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 163,
    label = "CH2(S)",
    molecule = 
"""
1     C     2S
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([8.06,8.31,8.63,8.99,9.77,10.5,11.83],"cal/(mol*K)"),
        H298 = (102.52,"kcal/mol"),
        S298 = (45.14,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 164,
    label = "CH2(T)",
    molecule = 
"""
1     C     2T
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([8.3,8.66,8.98,9.28,9.87,10.47,11.69],"cal/(mol*K)"),
        H298 = (93.85,"kcal/mol"),
        S298 = (46.59,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 165,
    label = "OCCO",
    molecule = 
"""
1     O     1 {2,S}
2     C     0 {1,S} {3,T}
3     C     0 {2,T} {4,S}
4     O     1 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([14.21,15.2,15.98,16.65,17.72,18.49,19.58],"cal/(mol*K)"),
        H298 = (5.6,"kcal/mol"),
        S298 = (61.18,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 166,
    label = "CH3CHCCH",
    molecule = 
"""
1     C     0 {2,S}
2     C     1 {1,S} {3,S}
3     C     0 {2,S} {4,T}
4     C     0 {3,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([18.91,22.66,25.87,28.57,32.85,36.09,41.23],"cal/(mol*K)"),
        H298 = (79.11,"kcal/mol"),
        S298 = (71.83,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 167,
    label = "CH3CHCHCH2",
    molecule = 
"""
1     C     0 {2,S}
2     C     1 {1,S} {3,S}
3     C     0 {2,S} {4,D}
4     C     0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([19.86,24.81,29.29,33.1,39.1,43.57,50.6],"cal/(mol*K)"),
        H298 = (34.78,"kcal/mol"),
        S298 = (71.99,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 168,
    label = "CH2CCH3CH2",
    molecule = 
"""
1     C     1 {2,S}
2     C     0 {1,S} {3,S} {4,D}
3     C     0 {2,S}
4     C     0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([19.59,24.94,29.51,33.32,39.22,43.62,50.57],"cal/(mol*K)"),
        H298 = (35.2,"kcal/mol"),
        S298 = (70.24,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 169,
    label = "CH2CCCH2",
    molecule = 
"""
1     C     0 {2,D}
2     C     0 {1,D} {3,D}
3     C     0 {2,D} {4,D}
4     C     0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([17.51,21.01,23.92,26.33,30.1,32.93,37.37],"cal/(mol*K)"),
        H298 = (79.7,"kcal/mol"),
        S298 = (65.15,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 170,
    label = "CH2CHCCH",
    molecule = 
"""
1     C     0 {2,D}
2     C     0 {1,D} {3,S}
3     C     0 {2,S} {4,T}
4     C     0 {3,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([17.18,20.88,23.88,26.32,30.06,32.83,37.25],"cal/(mol*K)"),
        H298 = (71.86,"kcal/mol"),
        S298 = (66.24,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 171,
    label = "CH2CCCH",
    molecule = 
"""
1     C     0 {2,D}
2     C     1 {1,D} {3,S}
3     C     0 {2,S} {4,T}
4     C     0 {3,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([18.68,21.24,23.29,24.97,27.64,29.68,32.95],"cal/(mol*K)"),
        H298 = (121.56,"kcal/mol"),
        S298 = (70.27,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 172,
    label = "HCCCHCH",
    molecule = 
"""
1     C     0 {2,T}
2     C     0 {1,T} {3,S}
3     C     0 {2,S} {4,D}
4     C     1 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([17.24,20.41,22.8,24.66,27.47,29.56,32.87],"cal/(mol*K)"),
        H298 = (132.99,"kcal/mol"),
        S298 = (67.35,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 173,
    label = "CH3CHCCH2",
    molecule = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,D}
3     C     0 {2,D} {4,D}
4     C     0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([18.95,23.2,27.03,30.32,35.57,39.54,45.78],"cal/(mol*K)"),
        H298 = (40.97,"kcal/mol"),
        S298 = (69.71,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 174,
    label = "CH2CHCHCH2",
    molecule = 
"""
1     C     0 {2,D}
2     C     0 {1,D} {3,S}
3     C     0 {2,S} {4,D}
4     C     0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([18.48,23.96,28.66,32.35,37.56,41.12,46.59],"cal/(mol*K)"),
        H298 = (28.95,"kcal/mol"),
        S298 = (65.82,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 175,
    label = "butyne1",
    molecule = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S}
3     C     0 {2,S} {4,T}
4     C     0 {3,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([19.47,23.9,27.69,30.86,35.89,39.71,45.81],"cal/(mol*K)"),
        H298 = (42.02,"kcal/mol"),
        S298 = (69.18,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 176,
    label = "tbutyl",
    molecule = 
"""
1     C     0 {2,S}
2     C     1 {1,S} {3,S} {4,S}
3     C     0 {2,S}
4     C     0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([21.71,26.64,31.62,36.12,43.55,49.22,58.13],"cal/(mol*K)"),
        H298 = (14.3,"kcal/mol"),
        S298 = (76.21,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 177,
    label = "ibutyl",
    molecule = 
"""
1     C     1 {2,S}
2     C     0 {1,S} {3,S} {4,S}
3     C     0 {2,S}
4     C     0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([23.23,28.98,34.04,38.33,45.13,50.31,58.58],"cal/(mol*K)"),
        H298 = (19.15,"kcal/mol"),
        S298 = (76.39,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 178,
    label = "butyl_1",
    molecule = 
"""
1     C     1 {2,S}
2     C     0 {1,S} {3,S}
3     C     0 {2,S} {4,S}
4     C     0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([23.01,28.55,33.6,37.94,44.89,50.17,58.56],"cal/(mol*K)"),
        H298 = (20.65,"kcal/mol"),
        S298 = (78.53,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 179,
    label = "butyl_2",
    molecule = 
"""
1     C     0 {2,S}
2     C     1 {1,S} {3,S}
3     C     0 {2,S} {4,S}
4     C     0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([21.99,27.3,32.36,36.82,44.06,49.58,58.28],"cal/(mol*K)"),
        H298 = (18.01,"kcal/mol"),
        S298 = (78.98,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 180,
    label = "butene_1",
    molecule = 
"""
1     C     0 {2,D}
2     C     0 {1,D} {3,S}
3     C     0 {2,S} {4,S}
4     C     0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([20.82,26.08,30.86,34.96,41.53,46.49,54.36],"cal/(mol*K)"),
        H298 = (1.88,"kcal/mol"),
        S298 = (73.18,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 181,
    label = "trans_butene_2",
    molecule = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,D}
3     C     0 {2,D} {4,S}
4     C     0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([21.14,25.96,30.54,34.59,41.2,46.25,54.24],"cal/(mol*K)"),
        H298 = (-0.84,"kcal/mol"),
        S298 = (70.68,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 182,
    label = "isobutene",
    molecule = 
"""
1     C     0 {2,D}
2     C     0 {1,D} {3,S} {4,S}
3     C     0 {2,S}
4     C     0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([21.12,26.15,30.77,34.8,41.35,46.34,54.27],"cal/(mol*K)"),
        H298 = (-2.22,"kcal/mol"),
        S298 = (70.16,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 183,
    label = "nbutane",
    molecule = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S}
3     C     0 {2,S} {4,S}
4     C     0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([25.39,30.69,35.76,40.25,47.63,53.34,62.48],"cal/(mol*K)"),
        H298 = (-28.28,"kcal/mol"),
        S298 = (76.34,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 184,
    label = "ibutane",
    molecule = 
"""
1     C     0 {2,S}
2     C     0 {1,S} {3,S} {4,S}
3     C     0 {2,S}
4     C     0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([23.9,30.21,35.82,40.56,48.08,53.8,63.01],"cal/(mol*K)"),
        H298 = (-30.67,"kcal/mol"),
        S298 = (71.16,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 185,
    label = "HCCCCH",
    molecule = 
"""
1     C     0 {2,T}
2     C     0 {1,T} {3,S}
3     C     0 {2,S} {4,T}
4     C     0 {3,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([17.18,19.78,21.53,22.84,24.83,26.35,28.87],"cal/(mol*K)"),
        H298 = (113.13,"kcal/mol"),
        S298 = (59.15,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 186,
    label = "HC2",
    molecule = 
"""
1     C     1 {2,T}
2     C     0 {1,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([10.34,10.64,10.89,11.15,11.7,12.22,13.21],"cal/(mol*K)"),
        H298 = (137.14,"kcal/mol"),
        S298 = (51.64,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 187,
    label = "C2(T)",
    molecule = 
"""
1     C     1 {2,T}
2     C     1 {1,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([6.99,7.13,7.33,7.55,7.93,8.2,8.56],"cal/(mol*K)"),
        H298 = (200.8,"kcal/mol"),
        S298 = (47.81,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 188,
    label = "C2O(S)",
    molecule = 
"""
1     C     2S {2,D}
2     C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([10.25,11.02,11.64,12.16,12.94,13.46,14.15],"cal/(mol*K)"),
        H298 = (110.61,"kcal/mol"),
        S298 = (53.61,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 189,
    label = "C2O",
    molecule = 
"""
1     C     2T {2,D}
2     C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([10.34,11.1,11.7,12.21,12.97,13.48,14.16],"cal/(mol*K)"),
        H298 = (91.89,"kcal/mol"),
        S298 = (55.84,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 190,
    label = "H2",
    molecule = 
"""
1     H     0 {2,S}
2     H     0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([6.95,6.95,6.95,6.95,7,7.1,7.49],"cal/(mol*K)"),
        H298 = (-0.01,"kcal/mol"),
        S298 = (31.09,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 191,
    label = "CH",
    molecule = 
"""
1     C     3
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([6.95,6.96,6.99,7.06,7.29,7.55,8.08],"cal/(mol*K)"),
        H298 = (142.34,"kcal/mol"),
        S298 = (42.27,"cal/(mol*K)"),
    ),
    shortDesc = """""",
    longDesc = 
"""


""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

