#!/usr/bin/env python
# encoding: utf-8

name = "DFT_QCI_thermo"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 1,
    label = "H2",
    molecule = 
"""
1 H 0 0 {2,S}
2 H 0 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.948,6.948,6.949,6.954,6.995,7.095,7.493],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (31.095,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2,
    label = "CH",
    molecule = 
"""
1 C 3Q 0 {2,S}
2 H 0  0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.948,6.956,6.99,7.06,7.285,7.55,8.079],'cal/(mol*K)'),
        H298 = (142.315,'kcal/mol'),
        S298 = (43.643,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 3,
    label = "CH2(S)",
    molecule = 
"""
1 C 2S 0 {2,S} {3,S}
2 H 0  0 {1,S}
3 H 0  0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.063,8.31,8.633,8.995,9.765,10.497,11.831],'cal/(mol*K)'),
        H298 = (102.462,'kcal/mol'),
        S298 = (45.144,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 4,
    label = "CH2(T)",
    molecule = 
"""
1 C 2T 0 {2,S} {3,S}
2 H 0  0 {1,S}
3 H 0  0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.296,8.655,8.981,9.279,9.87,10.466,11.687],'cal/(mol*K)'),
        H298 = (93.79,'kcal/mol'),
        S298 = (46.586,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 5,
    label = "CH3",
    molecule = 
"""
1 C 1 0 {2,S} {3,S} {4,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.36,10.115,10.854,11.553,12.856,14.029,16.21],'cal/(mol*K)'),
        H298 = (35.163,'kcal/mol'),
        S298 = (46.435,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 6,
    label = "CH4",
    molecule = 
"""
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.492,9.605,10.975,12.356,14.873,16.97,20.511],'cal/(mol*K)'),
        H298 = (-17.645,'kcal/mol'),
        S298 = (44.41,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 7,
    label = "OH",
    molecule = 
"""
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.948,6.948,6.953,6.971,7.066,7.234,7.723],'cal/(mol*K)'),
        H298 = (8.911,'kcal/mol'),
        S298 = (43.903,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 8,
    label = "H2O",
    molecule = 
"""
1 O 0 2 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.998,8.16,8.392,8.649,9.189,9.749,11.025],'cal/(mol*K)'),
        H298 = (-58.023,'kcal/mol'),
        S298 = (45.035,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 9,
    label = "CO",
    molecule = 
"""
1 C 2T 0 {2,D}
2 O 0  2 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.954,6.995,7.094,7.24,7.575,7.872,8.342],'cal/(mol*K)'),
        H298 = (-26.323,'kcal/mol'),
        S298 = (47.136,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 10,
    label = "HCO",
    molecule = 
"""
1 C 1 0 {2,D} {3,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.254,8.683,9.176,9.68,10.604,11.341,12.468],'cal/(mol*K)'),
        H298 = (10.166,'kcal/mol'),
        S298 = (53.514,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 11,
    label = "CH2O",
    molecule = 
"""
1 C 0 0 {2,D} {3,S} {4,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.443,9.326,10.378,11.422,13.254,14.685,16.902],'cal/(mol*K)'),
        H298 = (-26.159,'kcal/mol'),
        S298 = (52.16,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 12,
    label = "HCOH(S)",
    molecule = 
"""
1 C 2S 0 {2,S} {3,S}
2 O 0  2 {1,S} {4,S}
3 H 0  0 {1,S}
4 H 0  0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.69,9.849,11.134,12.347,14.347,15.799,17.849],'cal/(mol*K)'),
        H298 = (26.108,'kcal/mol'),
        S298 = (53.701,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 13,
    label = "HCOH(T)",
    molecule = 
"""
1 C 2T 0 {2,S} {3,S}
2 O 0  2 {1,S} {4,S}
3 H 0  0 {1,S}
4 H 0  0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.197,11.246,12.177,12.943,14.111,14.992,16.475],'cal/(mol*K)'),
        H298 = (51.83,'kcal/mol'),
        S298 = (58.324,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 14,
    label = "CH3O",
    molecule = 
"""
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 2 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.872,11.64,13.325,14.806,17.21,19.036,21.889],'cal/(mol*K)'),
        H298 = (4.884,'kcal/mol'),
        S298 = (54.422,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 15,
    label = "CH2OH",
    molecule = 
"""
1 C 1 0 {2,S} {3,S} {4,S}
2 O 0 2 {1,S} {5,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.448,12.958,14.318,15.456,17.227,18.589,20.925],'cal/(mol*K)'),
        H298 = (-3.59,'kcal/mol'),
        S298 = (58.19,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 16,
    label = "CH3OH",
    molecule = 
"""
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 2 {1,S} {6,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.587,12.352,14.254,16.013,18.952,21.247,25.018],'cal/(mol*K)'),
        H298 = (-48.24,'kcal/mol'),
        S298 = (57.185,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 17,
    label = "O2",
    molecule = 
"""
1 O 1 2 {2,S}
2 O 1 2 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7,7.151,7.369,7.596,7.977,8.239,8.58],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (48.924,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 18,
    label = "HO2",
    molecule = 
"""
1 O 1 2 {2,S}
2 O 0 2 {1,S} {3,S}
3 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.285,8.816,9.377,9.875,10.664,11.259,12.253],'cal/(mol*K)'),
        H298 = (2.733,'kcal/mol'),
        S298 = (54.609,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 19,
    label = "HOOH",
    molecule = 
"""
1 O 0 2 {2,S} {3,S}
2 O 0 2 {1,S} {4,S}
3 H 0 0 {1,S}
4 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.897,10.831,11.728,12.501,13.72,14.66,16.279],'cal/(mol*K)'),
        H298 = (-32.097,'kcal/mol'),
        S298 = (55.779,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 20,
    label = "CO2",
    molecule = 
"""
1 C 0 0 {2,D} {3,D}
2 O 0 2 {1,D}
3 O 0 2 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.869,9.845,10.626,11.264,12.229,12.898,13.822],'cal/(mol*K)'),
        H298 = (-94.125,'kcal/mol'),
        S298 = (50.992,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 21,
    label = "HOCO",
    molecule = 
"""
1 C 1 0 {2,D} {3,S}
2 O 0 2 {1,D}
3 O 0 2 {1,S} {4,S}
4 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.253,12.802,13.956,14.837,16.078,16.88,17.908],'cal/(mol*K)'),
        H298 = (-43.681,'kcal/mol'),
        S298 = (60.193,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 22,
    label = "formyloxy",
    molecule = 
"""
1 C 0 0 {2,D} {3,S} {4,S}
2 O 0 2 {1,D}
3 O 1 2 {1,S}
4 H 0 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.24,13.41,14.377,15.196,16.462,17.336,18.524],'cal/(mol*K)'),
        H298 = (-30.207,'kcal/mol'),
        S298 = (60.345,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 23,
    label = "formic_acid",
    molecule = 
"""
1 C 0 0 {2,D} {3,S} {4,S}
2 O 0 2 {1,D}
3 O 0 2 {1,S} {5,S}
4 H 0 0 {1,S}
5 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.017,13.147,15.139,16.849,19.423,21.14,23.318],'cal/(mol*K)'),
        H298 = (-90.466,'kcal/mol'),
        S298 = (59.464,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 24,
    label = "CH3OO",
    molecule = 
"""
1 C 0 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 2 {1,S} {3,S}
3 O 1 2 {2,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.076,14.177,16.239,18.046,20.904,23.012,26.263],'cal/(mol*K)'),
        H298 = (3.263,'kcal/mol'),
        S298 = (64.41,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 25,
    label = "HOCH2O",
    molecule = 
"""
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 2 {1,S} {6,S}
3 O 1 2 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.221,15.915,18.157,19.91,22.422,24.168,26.843],'cal/(mol*K)'),
        H298 = (-40.555,'kcal/mol'),
        S298 = (64.473,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 26,
    label = "CH3OOH",
    molecule = 
"""
1 C 0 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 2 {1,S} {3,S}
3 O 0 2 {2,S} {7,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.618,17.113,19.403,21.368,24.47,26.791,30.466],'cal/(mol*K)'),
        H298 = (-30.726,'kcal/mol'),
        S298 = (67.106,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 27,
    label = "cCO3",
    molecule = 
"""
1 C 0 0 {2,D} {3,S} {4,S}
2 O 0 2 {1,D}
3 O 0 2 {1,S} {4,S}
4 O 0 2 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.641,13.42,14.737,15.718,17.036,17.843,18.839],'cal/(mol*K)'),
        H298 = (-39.061,'kcal/mol'),
        S298 = (60.992,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 28,
    label = "formylperoxy",
    molecule = 
"""
1 C 0 0 {2,D} {3,S} {5,S}
2 O 0 2 {1,D}
3 O 0 2 {1,S} {4,S}
4 O 1 2 {3,S}
5 H 0 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.255,16.544,18.298,19.623,21.416,22.504,23.781],'cal/(mol*K)'),
        H298 = (-25.183,'kcal/mol'),
        S298 = (66.189,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 29,
    label = "OCHOOH",
    molecule = 
"""
1 C 0 0 {2,D} {3,S} {5,S}
2 O 0 2 {1,D}
3 O 0 2 {1,S} {4,S}
4 O 0 2 {3,S} {6,S}
5 H 0 0 {1,S}
6 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([17.217,19.74,21.349,22.485,24.14,25.387,27.466],'cal/(mol*K)'),
        H298 = (-69.069,'kcal/mol'),
        S298 = (67.243,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 30,
    label = "HOOCH2O",
    molecule = 
"""
1 O 1 2 {2,S}
2 C 0 0 {1,S} {3,S} {5,S} {6,S}
3 O 0 2 {2,S} {4,S}
4 O 0 2 {3,S} {7,S}
5 H 0 0 {2,S}
6 H 0 0 {2,S}
7 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([19.059,21.82,23.763,25.265,27.536,29.213,31.87],'cal/(mol*K)'),
        H298 = (-21.543,'kcal/mol'),
        S298 = (72.641,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 31,
    label = "HOCH2OO",
    molecule = 
"""
1 C 0 0 {2,S} {3,S} {5,S} {6,S}
2 O 0 2 {1,S} {7,S}
3 O 0 2 {1,S} {4,S}
4 O 1 2 {3,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([17.716,20.358,22.565,24.339,26.928,28.737,31.532],'cal/(mol*K)'),
        H298 = (-39.477,'kcal/mol'),
        S298 = (72.46,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 32,
    label = "HOOCH2OH",
    molecule = 
"""
1 O 0 2 {2,S} {5,S}
2 C 0 0 {1,S} {3,S} {6,S} {7,S}
3 O 0 2 {2,S} {4,S}
4 O 0 2 {3,S} {8,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {2,S}
8 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([19.912,23.176,25.963,28.132,31.112,33.1,36.163],'cal/(mol*K)'),
        H298 = (-75.31,'kcal/mol'),
        S298 = (72.773,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 33,
    label = "C2(T)",
    molecule = 
"""
1 C 1 0 {2,T}
2 C 1 0 {1,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.99,7.126,7.332,7.553,7.934,8.203,8.559],'cal/(mol*K)'),
        H298 = (199.39,'kcal/mol'),
        S298 = (47.814,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 34,
    label = "HC2",
    molecule = 
"""
1 C 1 0 {2,T}
2 C 0 0 {1,T} {3,S}
3 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.34,10.641,10.891,11.15,11.697,12.221,13.212],'cal/(mol*K)'),
        H298 = (135.7,'kcal/mol'),
        S298 = (51.641,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 35,
    label = "C2H2",
    molecule = 
"""
1 C 0 0 {2,T} {3,S}
2 C 0 0 {1,T} {4,S}
3 H 0 0 {1,S}
4 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.273,11.786,12.854,13.669,14.942,15.966,17.787],'cal/(mol*K)'),
        H298 = (54.64,'kcal/mol'),
        S298 = (47.728,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 36,
    label = "C2H2(T)",
    molecule = 
"""
1 C 1 0 {2,D} {3,S}
2 C 1 0 {1,D} {4,S}
3 H 0 0 {1,S}
4 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.634,10.896,11.974,12.877,14.323,15.44,17.247],'cal/(mol*K)'),
        H298 = (143.701,'kcal/mol'),
        S298 = (54.212,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 37,
    label = "H2CC(S)",
    molecule = 
"""
1 C 2S 0 {2,D}
2 C 0  0 {1,D} {3,S} {4,S}
3 H 0  0 {2,S}
4 H 0  0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.526,11.5,12.355,13.107,14.382,15.421,17.18],'cal/(mol*K)'),
        H298 = (98.417,'kcal/mol'),
        S298 = (53.097,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 38,
    label = "H2CC(T)",
    molecule = 
"""
1 C 2T 0 {2,D}
2 C 0  0 {1,D} {3,S} {4,S}
3 H 0  0 {2,S}
4 H 0  0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.32,10.467,11.539,12.482,14.029,15.223,17.135],'cal/(mol*K)'),
        H298 = (145.946,'kcal/mol'),
        S298 = (55.633,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 39,
    label = "C2H3",
    molecule = 
"""
1 C 1 0 {2,D} {3,S}
2 C 0 0 {1,D} {4,S} {5,S}
3 H 0 0 {1,S}
4 H 0 0 {2,S}
5 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.415,12.276,13.886,15.235,17.385,19.047,21.768],'cal/(mol*K)'),
        H298 = (71.151,'kcal/mol'),
        S298 = (55.777,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 40,
    label = "CCH3",
    molecule = 
"""
1 C 1 0 {2,T}
2 C 0 0 {1,T} {3,S}
3 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.461,12.226,13.853,15.263,17.545,19.284,22.02],'cal/(mol*K)'),
        H298 = (120.39,'kcal/mol'),
        S298 = (56.468,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("Thu Feb  6 13:58:32 2014","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> updated this entry by importing the old RMG database."""),
    ],
)

entry(
    index = 41,
    label = "C2H4",
    molecule = 
"""
1 C 0 0 {2,D} {3,S} {4,S}
2 C 0 0 {1,D} {5,S} {6,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
6 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.17,12.505,14.733,16.674,19.803,22.2,26.076],'cal/(mol*K)'),
        H298 = (12.476,'kcal/mol'),
        S298 = (52.254,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 42,
    label = "C2H4(T)",
    molecule = 
"""
1 C 1 0 {2,S} {3,S} {4,S}
2 C 1 0 {1,S} {5,S} {6,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
6 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.222,15.372,17.192,18.725,21.229,23.224,26.514],'cal/(mol*K)'),
        H298 = (79.052,'kcal/mol'),
        S298 = (57.013,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 43,
    label = "CHCH3(S)",
    molecule = 
"""
1 C 2S 0 {2,S} {3,S}
2 C 0  0 {1,S} {4,S} {5,S} {6,S}
3 H 0  0 {1,S}
4 H 0  0 {2,S}
5 H 0  0 {2,S}
6 H 0  0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.521,13.507,15.431,17.15,20.007,22.231,25.785],'cal/(mol*K)'),
        H298 = (87.469,'kcal/mol'),
        S298 = (57.911,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 44,
    label = "CHCH3(T)",
    molecule = 
"""
1 C 2T 0 {2,S} {3,S}
2 C 0  0 {1,S} {4,S} {5,S} {6,S}
3 H 0  0 {1,S}
4 H 0  0 {2,S}
5 H 0  0 {2,S}
6 H 0  0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.007,13.097,15.099,16.86,19.742,21.977,25.583],'cal/(mol*K)'),
        H298 = (84.827,'kcal/mol'),
        S298 = (59.111,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 45,
    label = "C2H5",
    molecule = 
"""
1 C 1 0 {2,S} {3,S} {4,S}
2 C 0 0 {1,S} {5,S} {6,S} {7,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
6 H 0 0 {2,S}
7 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.251,14.774,17.181,19.314,22.843,25.611,30.127],'cal/(mol*K)'),
        H298 = (28.934,'kcal/mol'),
        S298 = (59.122,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 46,
    label = "C2H6",
    molecule = 
"""
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {2,S}
8 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.565,15.512,18.421,21.059,25.487,28.964,34.591],'cal/(mol*K)'),
        H298 = (-20.028,'kcal/mol'),
        S298 = (54.726,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 47,
    label = "C2O(S)",
    molecule = 
"""
1 C 2S 0 {2,D}
2 C 0  0 {1,D} {3,D}
3 O 0  2 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.245,11.021,11.645,12.161,12.939,13.461,14.149],'cal/(mol*K)'),
        H298 = (110.367,'kcal/mol'),
        S298 = (53.61,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 48,
    label = "C2O(T)",
    molecule = 
"""
1 C 2T 0 {2,D}
2 C 0  0 {1,D} {3,D}
3 O 0  2 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.343,11.096,11.703,12.208,12.97,13.483,14.16],'cal/(mol*K)'),
        H298 = (91.049,'kcal/mol'),
        S298 = (55.836,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 49,
    label = "HCCO",
    molecule = 
"""
1 C 1 0 {2,D} {4,S}
2 C 0 0 {1,D} {3,D}
3 O 0 2 {2,D}
4 H 0 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.97,13.092,13.942,14.635,15.735,16.572,17.909],'cal/(mol*K)'),
        H298 = (42.404,'kcal/mol'),
        S298 = (58.805,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 50,
    label = "ethynol",
    molecule = 
"""
1 C 0 0 {2,T} {4,S}
2 C 0 0 {1,T} {3,S}
3 O 0 2 {2,S} {5,S}
4 H 0 0 {1,S}
5 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.438,15.172,16.461,17.467,19.01,20.208,22.286],'cal/(mol*K)'),
        H298 = (22.03,'kcal/mol'),
        S298 = (59.097,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 51,
    label = "ketene",
    molecule = 
"""
1 C 0 0 {2,D} {4,S} {5,S}
2 C 0 0 {1,D} {3,D}
3 O 0 2 {2,D}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.306,14.108,15.568,16.77,18.67,20.117,22.439],'cal/(mol*K)'),
        H298 = (-11.679,'kcal/mol'),
        S298 = (57.631,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 52,
    label = "ketene(T)",
    molecule = 
"""
1 C 1 0 {2,D} {4,S}
2 C 0 0 {1,D} {3,S} {5,S}
3 O 1 2 {2,S}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.107,15.207,16.88,18.179,19.979,21.136,22.731],'cal/(mol*K)'),
        H298 = (38.991,'kcal/mol'),
        S298 = (62.753,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("Thu Feb  6 13:58:32 2014","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> updated this entry by importing the old RMG database."""),
    ],
)

entry(
    index = 53,
    label = "oxirene",
    molecule = 
"""
1 C 0 0 {2,D} {3,S} {4,S}
2 C 0 0 {1,D} {3,S} {5,S}
3 O 0 2 {1,S} {2,S}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.179,15.057,16.524,17.671,19.382,20.642,22.684],'cal/(mol*K)'),
        H298 = (65.089,'kcal/mol'),
        S298 = (60.479,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 54,
    label = "oxiranyl",
    molecule = 
"""
1 C 1 0 {2,S} {3,S} {4,S}
2 C 0 0 {1,S} {3,S} {5,S} {6,S}
3 O 0 2 {1,S} {2,S}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
6 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.243,14.159,16.706,18.77,21.828,23.989,27.256],'cal/(mol*K)'),
        H298 = (39.967,'kcal/mol'),
        S298 = (60.352,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 55,
    label = "CHCHOH",
    molecule = 
"""
1 C 1 0 {2,D} {4,S}
2 C 0 0 {1,D} {3,S} {5,S}
3 O 0 2 {2,S} {6,S}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
6 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.653,17.718,19.999,21.591,23.584,24.881,27.021],'cal/(mol*K)'),
        H298 = (31.463,'kcal/mol'),
        S298 = (62.748,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 56,
    label = "CH2COH",
    molecule = 
"""
1 C 0 0 {2,D} {4,S} {5,S}
2 C 1 0 {1,D} {3,S}
3 O 0 2 {2,S} {6,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.363,16.856,18.744,20.19,22.32,23.901,26.535],'cal/(mol*K)'),
        H298 = (27.838,'kcal/mol'),
        S298 = (64.116,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 57,
    label = "vinoxy",
    molecule = 
"""
1 C 1 0 {2,S} {4,S} {5,S}
2 C 0 0 {1,S} {3,D} {6,S}
3 O 0 2 {2,D}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.72,15.276,17.486,19.318,22.133,24.186,27.351],'cal/(mol*K)'),
        H298 = (4.427,'kcal/mol'),
        S298 = (61.853,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 58,
    label = "acetyl",
    molecule = 
"""
1 C 1 0 {2,D} {3,S}
2 O 0 2 {1,D}
3 C 0 0 {1,S} {4,S} {5,S} {6,S}
4 H 0 0 {3,S}
5 H 0 0 {3,S}
6 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.064,14.111,16.078,17.824,20.667,22.815,26.158],'cal/(mol*K)'),
        H298 = (-2.271,'kcal/mol'),
        S298 = (63.738,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 59,
    label = "oxirane",
    molecule = 
"""
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 0 {1,S} {3,S} {6,S} {7,S}
3 O 0 2 {1,S} {2,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.426,14.853,17.98,20.587,24.544,27.388,31.722],'cal/(mol*K)'),
        H298 = (-12.356,'kcal/mol'),
        S298 = (57.942,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 60,
    label = "ethenol",
    molecule = 
"""
1 C 0 0 {2,D} {4,S} {5,S}
2 C 0 0 {1,D} {3,S} {6,S}
3 O 0 2 {2,S} {7,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([15.024,18.066,20.543,22.511,25.445,27.605,31.144],'cal/(mol*K)'),
        H298 = (-29.857,'kcal/mol'),
        S298 = (62.176,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 61,
    label = "CH3CHO",
    molecule = 
"""
1 C 0 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 0 {1,S} {3,D} {7,S}
3 O 0 2 {2,D}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.966,15.477,17.954,20.181,23.829,26.589,30.869],'cal/(mol*K)'),
        H298 = (-39.589,'kcal/mol'),
        S298 = (62.986,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 62,
    label = "CH3CH2O",
    molecule = 
"""
1 C 0 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 0 {1,S} {3,S} {7,S} {8,S}
3 O 1 2 {2,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {2,S}
8 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([15.802,18.824,21.653,24.132,28.151,31.206,36.006],'cal/(mol*K)'),
        H298 = (-3.059,'kcal/mol'),
        S298 = (66.844,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 63,
    label = "CH3OCH2",
    molecule = 
"""
1 C 1 0 {2,S} {4,S} {5,S}
2 O 0 2 {1,S} {3,S}
3 C 0 0 {2,S} {6,S} {7,S} {8,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {3,S}
7 H 0 0 {3,S}
8 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([15.533,18.29,21.024,23.462,27.406,30.387,35.08],'cal/(mol*K)'),
        H298 = (0.773,'kcal/mol'),
        S298 = (67.315,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 64,
    label = "CH2CH2OH",
    molecule = 
"""
1 C 1 0 {2,S} {4,S} {5,S}
2 C 0 0 {1,S} {3,S} {6,S} {7,S}
3 O 0 2 {2,S} {8,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {2,S}
8 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([16.841,19.488,21.955,24.106,27.598,30.309,34.795],'cal/(mol*K)'),
        H298 = (-5.946,'kcal/mol'),
        S298 = (69.419,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 65,
    label = "CH3CHOH",
    molecule = 
"""
1 C 0 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 0 {1,S} {3,S} {7,S}
3 O 0 2 {2,S} {8,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {2,S}
8 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([15.825,18.764,21.494,23.839,27.553,30.36,34.892],'cal/(mol*K)'),
        H298 = (-13.048,'kcal/mol'),
        S298 = (68.089,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 66,
    label = "ethanol",
    molecule = 
"""
1 C 0 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 0 {1,S} {3,S} {7,S} {8,S}
3 O 0 2 {2,S} {9,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {2,S}
8 H 0 0 {2,S}
9 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([15.674,19.241,22.574,25.462,30.088,33.605,39.265],'cal/(mol*K)'),
        H298 = (-56.422,'kcal/mol'),
        S298 = (66.773,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 67,
    label = "DME",
    molecule = 
"""
1 C 0 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 2 {1,S} {3,S}
3 C 0 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {3,S}
8 H 0 0 {3,S}
9 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([15.775,18.915,22.066,24.947,29.763,33.488,39.389],'cal/(mol*K)'),
        H298 = (-43.917,'kcal/mol'),
        S298 = (63.856,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 68,
    label = "OCCO(T)",
    molecule = 
"""
1 O 1 2 {2,S}
2 C 0 0 {1,S} {3,T}
3 C 0 0 {2,T} {4,S}
4 O 1 2 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.208,15.201,15.983,16.649,17.719,18.49,19.579],'cal/(mol*K)'),
        H298 = (4.834,'kcal/mol'),
        S298 = (61.184,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 69,
    label = "OCHCO",
    molecule = 
"""
1 O 0 2 {2,D}
2 C 0 0 {1,D} {3,S} {5,S}
3 C 1 0 {2,S} {4,D}
4 O 0 2 {3,D}
5 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.857,15.602,17.092,18.334,20.23,21.559,23.46],'cal/(mol*K)'),
        H298 = (-14.899,'kcal/mol'),
        S298 = (67.191,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 70,
    label = "OCCOH",
    molecule = 
"""
1 O 1 2 {2,S}
2 C 0 0 {1,S} {3,T}
3 C 0 0 {2,T} {4,S}
4 O 0 2 {3,S} {5,S}
5 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.276,16.054,17.471,18.612,20.304,21.483,23.249],'cal/(mol*K)'),
        H298 = (5.313,'kcal/mol'),
        S298 = (65.745,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 71,
    label = "glyoxal",
    molecule = 
"""
1 O 0 2 {2,D}
2 C 0 0 {1,D} {3,S} {5,S}
3 C 0 0 {2,S} {4,D} {6,S}
4 O 0 2 {3,D}
5 H 0 0 {2,S}
6 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.478,17.028,19.406,21.413,24.263,26.01,28.192],'cal/(mol*K)'),
        H298 = (-50.919,'kcal/mol'),
        S298 = (64.554,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 72,
    label = "oxiranone",
    molecule = 
"""
1 O 0 2 {2,D}
2 C 0 0 {1,D} {3,S} {4,S}
3 C 0 0 {2,S} {4,S} {5,S} {6,S}
4 O 0 2 {2,S} {3,S}
5 H 0 0 {3,S}
6 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.081,15.993,18.414,20.353,23.198,25.16,28.016],'cal/(mol*K)'),
        H298 = (-41.023,'kcal/mol'),
        S298 = (63.082,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 73,
    label = "hydroxyketene",
    molecule = 
"""
1 O 0 2 {2,S} {5,S}
2 C 0 0 {1,S} {3,D} {6,S}
3 C 0 0 {2,D} {4,D}
4 O 0 2 {3,D}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([15.92,18.159,19.881,21.236,23.268,24.755,27.132],'cal/(mol*K)'),
        H298 = (-36.154,'kcal/mol'),
        S298 = (66.577,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 74,
    label = "ethynediol",
    molecule = 
"""
1 C 0 0 {2,T} {4,S}
2 C 0 0 {1,T} {3,S}
3 O 0 2 {2,S} {5,S}
4 O 0 2 {1,S} {6,S}
5 H 0 0 {3,S}
6 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([17.316,18.995,20.349,21.46,23.198,24.538,26.841],'cal/(mol*K)'),
        H298 = (-5.13,'kcal/mol'),
        S298 = (67.354,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 75,
    label = "CH2CHOO",
    molecule = 
"""
1 C 0 0 {2,D} {5,S} {6,S}
2 C 0 0 {1,D} {3,S} {7,S}
3 O 0 2 {2,S} {4,S}
4 O 1 2 {3,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([16.796,20.057,22.697,24.76,27.694,29.683,32.629],'cal/(mol*K)'),
        H298 = (27.516,'kcal/mol'),
        S298 = (68.05,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 76,
    label = "CHCHOOH",
    molecule = 
"""
1 C 1 0 {2,D} {5,S}
2 C 0 0 {1,D} {3,S} {6,S}
3 O 0 2 {2,S} {4,S}
4 O 0 2 {3,S} {7,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.5,21.013,23.088,24.719,27.092,28.788,31.504],'cal/(mol*K)'),
        H298 = (53.494,'kcal/mol'),
        S298 = (74.802,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 77,
    label = "OCH2CHO",
    molecule = 
"""
1 O 0 2 {2,D}
2 C 0 0 {1,D} {3,S} {5,S}
3 C 0 0 {2,S} {4,S} {6,S} {7,S}
4 O 1 2 {3,S}
5 H 0 0 {2,S}
6 H 0 0 {3,S}
7 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([15.735,19.025,21.803,24.021,27.241,29.443,32.623],'cal/(mol*K)'),
        H298 = (-18.263,'kcal/mol'),
        S298 = (70.091,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 78,
    label = "CH2OCHO",
    molecule = 
"""
1 C 1 0 {2,S} {5,S} {6,S}
2 O 0 2 {1,S} {3,S}
3 C 0 0 {2,S} {4,D} {7,S}
4 O 0 2 {3,D}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([17.173,20.159,22.873,25.133,28.423,30.563,33.294],'cal/(mol*K)'),
        H298 = (-37.259,'kcal/mol'),
        S298 = (70.119,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 79,
    label = "CH3OCO",
    molecule = 
"""
1 C 0 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 2 {1,S} {3,S}
3 C 1 0 {2,S} {4,D}
4 O 0 2 {3,D}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([15.263,17.744,20.194,22.368,25.812,28.271,31.762],'cal/(mol*K)'),
        H298 = (-37.616,'kcal/mol'),
        S298 = (70.503,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 80,
    label = "cC2H3O2",
    molecule = 
"""
1 O 1 2 {2,S}
2 C 0 0 {1,S} {3,S} {4,S} {5,S}
3 C 0 0 {2,S} {4,S} {6,S} {7,S}
4 O 0 2 {2,S} {3,S}
5 H 0 0 {2,S}
6 H 0 0 {3,S}
7 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([15.486,18.872,21.696,23.961,27.294,29.62,33.074],'cal/(mol*K)'),
        H298 = (-8.906,'kcal/mol'),
        S298 = (67.786,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 81,
    label = "acetyloxy",
    molecule = 
"""
1 C 0 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 0 {1,S} {3,D} {4,S}
3 O 0 2 {2,D}
4 O 1 2 {2,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.611,17.659,20.335,22.562,25.943,28.347,31.931],'cal/(mol*K)'),
        H298 = (-44.885,'kcal/mol'),
        S298 = (67.738,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 82,
    label = "CH2COOH",
    molecule = 
"""
1 C 1 0 {2,S} {5,S} {6,S}
2 C 0 0 {1,S} {3,D} {4,S}
3 O 0 2 {2,D}
4 O 0 2 {2,S} {7,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([16.495,19.865,22.653,24.954,28.451,30.839,33.784],'cal/(mol*K)'),
        H298 = (-55.793,'kcal/mol'),
        S298 = (67.8,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 83,
    label = "CH2CHOOH",
    molecule = 
"""
1 C 0 0 {2,D} {5,S} {6,S}
2 C 0 0 {1,D} {3,S} {7,S}
3 O 0 2 {2,S} {4,S}
4 O 0 2 {3,S} {8,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {2,S}
8 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.382,21.576,24.393,26.691,30.095,32.505,36.237],'cal/(mol*K)'),
        H298 = (-9.2,'kcal/mol'),
        S298 = (73.038,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 84,
    label = "acetic_acid",
    molecule = 
"""
1 C 0 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 0 {1,S} {3,D} {4,S}
3 O 0 2 {2,D}
4 O 0 2 {2,S} {8,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {1,S}
8 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([15.539,19.209,22.499,25.328,29.785,32.989,37.443],'cal/(mol*K)'),
        H298 = (-103.256,'kcal/mol'),
        S298 = (68.232,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 85,
    label = "methyl_formate",
    molecule = 
"""
1 C 0 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 2 {1,S} {3,S}
3 C 0 0 {2,S} {4,D} {8,S}
4 O 0 2 {3,D}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {1,S}
8 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([15.451,18.667,21.952,24.911,29.595,32.888,37.375],'cal/(mol*K)'),
        H298 = (-85.596,'kcal/mol'),
        S298 = (69.003,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 86,
    label = "HOCHCHOH",
    molecule = 
"""
1 O 0 2 {2,S} {5,S}
2 C 0 0 {1,S} {3,D} {6,S}
3 C 0 0 {2,D} {4,S} {7,S}
4 O 0 2 {3,S} {8,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {3,S}
8 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([17.079,21.406,25.07,27.861,31.436,33.559,36.617],'cal/(mol*K)'),
        H298 = (-68.797,'kcal/mol'),
        S298 = (68.764,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 87,
    label = "HOCH2CHO",
    molecule = 
"""
1 O 0 2 {2,S} {5,S}
2 C 0 0 {1,S} {3,S} {6,S} {7,S}
3 C 0 0 {2,S} {4,D} {8,S}
4 O 0 2 {3,D}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {2,S}
8 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([17.667,21.961,25.631,28.398,31.96,34.133,37.211],'cal/(mol*K)'),
        H298 = (-76.04,'kcal/mol'),
        S298 = (68.745,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 88,
    label = "CH3CH2OO",
    molecule = 
"""
1 C 0 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 0 {1,S} {3,S} {8,S} {9,S}
3 O 0 2 {2,S} {4,S}
4 O 1 2 {3,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {1,S}
8 H 0 0 {2,S}
9 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([17.576,21.349,24.744,27.614,32.088,35.388,40.506],'cal/(mol*K)'),
        H298 = (-5.033,'kcal/mol'),
        S298 = (74.152,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 89,
    label = "CH2CH2OOH",
    molecule = 
"""
1 C 1 0 {2,S} {5,S} {6,S}
2 C 0 0 {1,S} {3,S} {7,S} {8,S}
3 O 0 2 {2,S} {4,S}
4 O 0 2 {3,S} {9,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {2,S}
8 H 0 0 {2,S}
9 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([19.841,23.332,26.389,28.922,32.8,35.647,40.14],'cal/(mol*K)'),
        H298 = (12.161,'kcal/mol'),
        S298 = (79.034,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 90,
    label = "HOCH2CHOH",
    molecule = 
"""
1 C 0 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 2 {1,S} {3,S}
3 C 0 0 {2,S} {4,S} {8,S} {9,S}
4 O 1 2 {3,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {1,S}
8 H 0 0 {3,S}
9 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([21.752,25.836,29.029,31.399,34.651,36.913,40.601],'cal/(mol*K)'),
        H298 = (-50.001,'kcal/mol'),
        S298 = (75.152,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 91,
    label = "HOCH2CH2O",
    molecule = 
"""
1 O 0 2 {2,S} {5,S}
2 C 0 0 {1,S} {3,S} {6,S} {7,S}
3 C 0 0 {2,S} {4,S} {8,S} {9,S}
4 O 1 2 {3,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {2,S}
8 H 0 0 {3,S}
9 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.941,25.839,29.129,31.403,34.627,37.067,41.184],'cal/(mol*K)'),
        H298 = (-39.262,'kcal/mol'),
        S298 = (71.449,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 92,
    label = "CH3OCHOH",
    molecule = 
"""
1 C 0 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 2 {1,S} {3,S}
3 C 1 0 {2,S} {4,S} {8,S}
4 O 0 2 {3,S} {9,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {1,S}
8 H 0 0 {3,S}
9 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.939,24.674,27.531,29.733,33.069,35.628,39.922],'cal/(mol*K)'),
        H298 = (-43.809,'kcal/mol'),
        S298 = (73.603,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 93,
    label = "HOCH2OCH2",
    molecule = 
"""
1 O 0 2 {2,S} {5,S}
2 C 0 0 {1,S} {3,S} {6,S} {7,S}
3 O 0 2 {2,S} {4,S}
4 C 1 0 {3,S} {8,S} {9,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {2,S}
8 H 0 0 {4,S}
9 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([22.78,26.011,28.451,30.43,33.556,35.993,40.114],'cal/(mol*K)'),
        H298 = (-42.696,'kcal/mol'),
        S298 = (74.398,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 94,
    label = "CH3OCH2O",
    molecule = 
"""
1 C 0 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 2 {1,S} {3,S}
3 C 0 0 {2,S} {4,S} {8,S} {9,S}
4 O 1 2 {3,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {1,S}
8 H 0 0 {3,S}
9 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([17.428,21.195,24.672,27.637,32.257,35.63,40.75],'cal/(mol*K)'),
        H298 = (-35.159,'kcal/mol'),
        S298 = (74.159,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 95,
    label = "CH3CH2OOH",
    molecule = 
"""
1  C 0 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 0 {1,S} {3,S} {8,S} {9,S}
3  O 0 2 {2,S} {4,S}
4  O 0 2 {3,S} {10,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {2,S}
10 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20,24.099,27.75,30.835,35.65,39.218,44.799],'cal/(mol*K)'),
        H298 = (-38.534,'kcal/mol'),
        S298 = (75.154,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 96,
    label = "CH3OOCH3",
    molecule = 
"""
1  C 0 0 {2,S} {5,S} {6,S} {7,S}
2  O 0 2 {1,S} {3,S}
3  O 0 2 {2,S} {4,S}
4  C 0 0 {3,S} {8,S} {9,S} {10,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {4,S}
9  H 0 0 {4,S}
10 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([19.474,23.302,26.877,30.001,35.042,38.862,44.844],'cal/(mol*K)'),
        H298 = (-29.144,'kcal/mol'),
        S298 = (72.224,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 97,
    label = "ketenylperoxy",
    molecule = 
"""
1 C 0 0 {2,D} {4,S} {6,S}
2 C 0 0 {1,D} {3,D}
3 O 0 2 {2,D}
4 O 0 2 {1,S} {5,S}
5 O 1 2 {4,S}
6 H 0 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.667,20.748,22.358,23.607,25.41,26.646,28.437],'cal/(mol*K)'),
        H298 = (19.158,'kcal/mol'),
        S298 = (75.792,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 98,
    label = "acetylperoxy",
    molecule = 
"""
1 C 0 0 {2,S} {6,S} {7,S} {8,S}
2 C 0 0 {1,S} {3,D} {4,S}
3 O 0 2 {2,D}
4 O 0 2 {2,S} {5,S}
5 O 1 2 {4,S}
6 H 0 0 {1,S}
7 H 0 0 {1,S}
8 H 0 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([19.907,23.071,25.848,28.147,31.557,33.9,37.28],'cal/(mol*K)'),
        H298 = (-37.465,'kcal/mol'),
        S298 = (76.208,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 99,
    label = "vinoxyperoxy",
    molecule = 
"""
1 C 0 0 {2,D} {3,S} {6,S}
2 O 0 2 {1,D}
3 C 0 0 {1,S} {4,S} {7,S} {8,S}
4 O 0 2 {3,S} {5,S}
5 O 1 2 {4,S}
6 H 0 0 {1,S}
7 H 0 0 {3,S}
8 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([19.793,23.218,26.099,28.389,31.698,33.966,37.286],'cal/(mol*K)'),
        H298 = (-18.878,'kcal/mol'),
        S298 = (77.552,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 100,
    label = "hoo_acetyl",
    molecule = 
"""
1 C 1 0 {2,D} {3,S}
2 O 0 2 {1,D}
3 C 0 0 {1,S} {4,S} {6,S} {7,S}
4 O 0 2 {3,S} {5,S}
5 O 0 2 {4,S} {8,S}
6 H 0 0 {3,S}
7 H 0 0 {3,S}
8 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([22.346,25.828,28.486,30.44,33.07,34.813,37.392],'cal/(mol*K)'),
        H298 = (-17.755,'kcal/mol'),
        S298 = (79.317,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 101,
    label = "hoo_vinoxy",
    molecule = 
"""
1 C 1 0 {2,S} {6,S} {7,S}
2 C 0 0 {1,S} {3,D} {4,S}
3 O 0 2 {2,D}
4 O 0 2 {2,S} {5,S}
5 O 0 2 {4,S} {8,S}
6 H 0 0 {1,S}
7 H 0 0 {1,S}
8 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([21.044,25.439,28.985,31.674,35.203,37.276,39.598],'cal/(mol*K)'),
        H298 = (-35.219,'kcal/mol'),
        S298 = (73.727,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 102,
    label = "CH3OOCH2O",
    molecule = 
"""
1  C 0 0 {2,S} {6,S} {7,S} {8,S}
2  O 0 2 {1,S} {3,S}
3  O 0 2 {2,S} {4,S}
4  C 0 0 {3,S} {5,S} {9,S} {10,S}
5  O 1 2 {4,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {1,S}
9  H 0 0 {4,S}
10 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([22.724,26.951,30.525,33.478,38.037,41.374,46.433],'cal/(mol*K)'),
        H298 = (-29.253,'kcal/mol'),
        S298 = (81.274,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 103,
    label = "HOOCH2CH2OO",
    molecule = 
"""
1  O 1 2 {2,S}
2  O 0 2 {1,S} {3,S}
3  C 0 0 {2,S} {4,S} {7,S} {8,S}
4  C 0 0 {3,S} {5,S} {9,S} {10,S}
5  O 0 2 {4,S} {6,S}
6  O 0 2 {5,S} {11,S}
7  H 0 0 {3,S}
8  H 0 0 {3,S}
9  H 0 0 {4,S}
10 H 0 0 {4,S}
11 H 0 0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.552,33.824,37.039,39.593,43.544,46.512,51.215],'cal/(mol*K)'),
        H298 = (-21.46,'kcal/mol'),
        S298 = (89.696,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 104,
    label = "H2CCC(S)",
    molecule = 
"""
1 C 0  0 {2,D} {4,S} {5,S}
2 C 0  0 {1,D} {3,D}
3 C 2S 0 {2,D}
4 H 0  0 {1,S}
5 H 0  0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.446,13.958,15.368,16.606,18.613,20.132,22.506],'cal/(mol*K)'),
        H298 = (132.136,'kcal/mol'),
        S298 = (58.667,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 105,
    label = "HCCCH(S)",
    molecule = 
"""
1 C 1 0 {2,T}
2 C 0 0 {1,T} {3,S}
3 C 1 0 {2,S} {4,S} {5,S}
4 H 0 0 {3,S}
5 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.124,15.722,16.994,18.026,19.636,20.861,22.85],'cal/(mol*K)'),
        H298 = (142.727,'kcal/mol'),
        S298 = (59.457,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("Thu Feb  6 13:58:32 2014","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> updated this entry by importing the old RMG database."""),
    ],
)

entry(
    index = 106,
    label = "HCCCH(T)",
    molecule = 
"""
1 C 0  0 {2,T} {4,S}
2 C 0  0 {1,T} {3,S}
3 C 2T 0 {2,S} {5,S}
4 H 0  0 {1,S}
5 H 0  0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([16.803,17.706,18.466,19.13,20.259,21.205,22.91],'cal/(mol*K)'),
        H298 = (130.529,'kcal/mol'),
        S298 = (63.781,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("Thu Feb  6 13:58:32 2014","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> updated this entry by importing the old RMG database."""),
    ],
)

entry(
    index = 107,
    label = "C3H3",
    molecule = 
"""
1 C 0 0 {2,D} {4,S} {5,S}
2 C 0 0 {1,D} {3,D}
3 C 1 0 {2,D} {6,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.902,17.212,18.998,20.432,22.682,24.423,27.317],'cal/(mol*K)'),
        H298 = (84.199,'kcal/mol'),
        S298 = (60.623,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 108,
    label = "allene",
    molecule = 
"""
1 C 0 0 {2,D} {4,S} {5,S}
2 C 0 0 {1,D} {3,D}
3 C 0 0 {2,D} {6,S} {7,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {3,S}
7 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.967,17.02,19.626,21.787,25.176,27.734,31.818],'cal/(mol*K)'),
        H298 = (45.072,'kcal/mol'),
        S298 = (59.336,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 109,
    label = "propyne",
    molecule = 
"""
1 C 0 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 0 {1,S} {3,T}
3 C 0 0 {2,T} {7,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.368,17.141,19.547,21.601,24.925,27.494,31.649],'cal/(mol*K)'),
        H298 = (44.284,'kcal/mol'),
        S298 = (58.986,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 110,
    label = "cC3H4",
    molecule = 
"""
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 0 {1,S} {3,D} {6,S}
3 C 0 0 {1,S} {2,D} {7,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.508,16.018,19.007,21.428,25.074,27.721,31.841],'cal/(mol*K)'),
        H298 = (67.589,'kcal/mol'),
        S298 = (58.015,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 111,
    label = "allyl",
    molecule = 
"""
1 C 0 0 {2,D} {4,S} {5,S}
2 C 0 0 {1,D} {3,S} {6,S}
3 C 1 0 {2,S} {7,S} {8,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {3,S}
8 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.885,18.725,21.975,24.634,28.721,31.759,36.602],'cal/(mol*K)'),
        H298 = (40.585,'kcal/mol'),
        S298 = (61.54,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 112,
    label = "cC3H5",
    molecule = 
"""
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 0 {1,S} {3,S} {6,S} {7,S}
3 C 1 0 {1,S} {2,S} {8,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {2,S}
8 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.614,17.846,21.434,24.32,28.647,31.786,36.685],'cal/(mol*K)'),
        H298 = (69.882,'kcal/mol'),
        S298 = (61.584,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 113,
    label = "propen2yl",
    molecule = 
"""
1 C 0 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 0 {1,S} {3,D}
3 C 0 0 {2,D} {7,S} {8,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {3,S}
8 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([15.139,18.179,21.042,23.559,27.655,30.784,35.731],'cal/(mol*K)'),
        H298 = (60.498,'kcal/mol'),
        S298 = (65.408,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 114,
    label = "propen1yl",
    molecule = 
"""
1 C 0 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 0 {1,S} {3,D} {7,S}
3 C 1 0 {2,D} {8,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {2,S}
8 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([15.279,18.478,21.363,23.847,27.842,30.889,35.745],'cal/(mol*K)'),
        H298 = (64.052,'kcal/mol'),
        S298 = (64.876,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 115,
    label = "cC3H6",
    molecule = 
"""
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 0 {1,S} {3,S} {6,S} {7,S}
3 C 0 0 {1,S} {2,S} {8,S} {9,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {2,S}
8 H 0 0 {3,S}
9 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.356,18.125,22.345,25.821,31.105,34.964,40.997],'cal/(mol*K)'),
        H298 = (13.022,'kcal/mol'),
        S298 = (56.668,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 116,
    label = "C3H6",
    molecule = 
"""
1 C 0 0 {2,D} {4,S} {5,S}
2 C 0 0 {1,D} {3,S} {6,S}
3 C 0 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {3,S}
8 H 0 0 {3,S}
9 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([15.382,19.098,22.571,25.602,30.502,34.236,40.173],'cal/(mol*K)'),
        H298 = (4.607,'kcal/mol'),
        S298 = (63.63,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 117,
    label = "C3H6(T)",
    molecule = 
"""
1 C 1 0 {2,S} {4,S} {5,S}
2 C 1 0 {1,S} {3,S} {6,S}
3 C 0 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {3,S}
8 H 0 0 {3,S}
9 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([17.326,20.881,24.12,26.919,31.453,34.939,40.466],'cal/(mol*K)'),
        H298 = (71.616,'kcal/mol'),
        S298 = (70.488,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 118,
    label = "npropyl",
    molecule = 
"""
1  C 1 0 {2,S} {4,S} {5,S}
2  C 0 0 {1,S} {3,S} {6,S} {7,S}
3  C 0 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 0 {1,S}
5  H 0 0 {1,S}
6  H 0 0 {2,S}
7  H 0 0 {2,S}
8  H 0 0 {3,S}
9  H 0 0 {3,S}
10 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([17.348,21.505,25.276,28.526,33.776,37.81,44.287],'cal/(mol*K)'),
        H298 = (24.271,'kcal/mol'),
        S298 = (69.303,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 119,
    label = "ipropyl",
    molecule = 
"""
1  C 0 0 {2,S} {4,S} {5,S} {6,S}
2  C 1 0 {1,S} {3,S} {7,S}
3  C 0 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 0 {1,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {2,S}
8  H 0 0 {3,S}
9  H 0 0 {3,S}
10 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([16.369,20.253,24.072,27.481,33.066,37.343,44.108],'cal/(mol*K)'),
        H298 = (21.249,'kcal/mol'),
        S298 = (68.901,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 120,
    label = "C3H8",
    molecule = 
"""
1  C 0 0 {2,S} {4,S} {5,S} {6,S}
2  C 0 0 {1,S} {3,S} {7,S} {8,S}
3  C 0 0 {2,S} {9,S} {10,S} {11,S}
4  H 0 0 {1,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {2,S}
8  H 0 0 {2,S}
9  H 0 0 {3,S}
10 H 0 0 {3,S}
11 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([17.757,22.393,26.702,30.469,36.602,41.318,48.85],'cal/(mol*K)'),
        H298 = (-25.203,'kcal/mol'),
        S298 = (66.066,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 121,
    label = "HCCCO",
    molecule = 
"""
1 C 0 0 {2,T} {5,S}
2 C 0 0 {1,T} {3,S}
3 C 1 0 {2,S} {4,D}
4 O 0 2 {3,D}
5 H 0 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([15.566,17.096,18.236,19.163,20.623,21.714,23.411],'cal/(mol*K)'),
        H298 = (69.086,'kcal/mol'),
        S298 = (66.418,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 122,
    label = "propynal",
    molecule = 
"""
1 C 0 0 {2,T} {5,S}
2 C 0 0 {1,T} {3,S}
3 C 0 0 {2,S} {4,D} {6,S}
4 O 0 2 {3,D}
5 H 0 0 {1,S}
6 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([15.1,17.478,19.409,20.994,23.447,25.241,27.984],'cal/(mol*K)'),
        H298 = (31.776,'kcal/mol'),
        S298 = (65.537,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 123,
    label = "CH2CCO",
    molecule = 
"""
1 C 0 0 {2,D} {5,S} {6,S}
2 C 0 0 {1,D} {3,D}
3 C 0 0 {2,D} {4,D}
4 O 0 2 {3,D}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([15.092,17.264,19.13,20.716,23.234,25.101,27.947],'cal/(mol*K)'),
        H298 = (31.16,'kcal/mol'),
        S298 = (66.052,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 124,
    label = "CH2CHCO",
    molecule = 
"""
1 C 0 0 {2,D} {5,S} {6,S}
2 C 0 0 {1,D} {3,S} {7,S}
3 C 1 0 {2,S} {4,D}
4 O 0 2 {3,D}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([15.612,18.585,21.167,23.324,26.646,29.052,32.709],'cal/(mol*K)'),
        H298 = (23.236,'kcal/mol'),
        S298 = (67.913,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 125,
    label = "CH2CCHO",
    molecule = 
"""
1 C 0 0 {2,D} {5,S} {6,S}
2 C 1 0 {1,D} {3,S}
3 C 0 0 {2,S} {4,D} {7,S}
4 O 0 2 {3,D}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([16.308,19.124,21.611,23.723,27.02,29.411,32.991],'cal/(mol*K)'),
        H298 = (45.164,'kcal/mol'),
        S298 = (70.258,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 126,
    label = "CHCHCHO",
    molecule = 
"""
1 C 1 0 {2,D} {5,S}
2 C 0 0 {1,D} {3,S} {6,S}
3 C 0 0 {2,S} {4,D} {7,S}
4 O 0 2 {3,D}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([16.24,19.738,22.686,25.026,28.292,30.371,33.172],'cal/(mol*K)'),
        H298 = (44.384,'kcal/mol'),
        S298 = (67.331,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 127,
    label = "acrolein",
    molecule = 
"""
1 C 0 0 {2,D} {5,S} {6,S}
2 C 0 0 {1,D} {3,S} {7,S}
3 C 0 0 {2,S} {4,D} {8,S}
4 O 0 2 {3,D}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {2,S}
8 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([16.875,20.407,23.492,26.098,30.139,33.039,37.305],'cal/(mol*K)'),
        H298 = (-15.511,'kcal/mol'),
        S298 = (65.35,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 128,
    label = "acrolein(T)",
    molecule = 
"""
1 C 0 0 {2,D} {5,S} {6,S}
2 C 0 0 {1,D} {3,S} {7,S}
3 C 1 0 {2,S} {4,S} {8,S}
4 O 1 2 {3,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {2,S}
8 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.774,22.181,25.079,27.475,31.172,33.882,37.991],'cal/(mol*K)'),
        H298 = (45.847,'kcal/mol'),
        S298 = (69.681,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 129,
    label = "methylketene",
    molecule = 
"""
1 C 0 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 0 {1,S} {3,D} {8,S}
3 C 0 0 {2,D} {4,D}
4 O 0 2 {3,D}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {1,S}
8 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([16.455,19.542,22.364,24.815,28.752,31.711,36.314],'cal/(mol*K)'),
        H298 = (-15.137,'kcal/mol'),
        S298 = (68.576,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 130,
    label = "oxetene",
    molecule = 
"""
1 O 0 2 {2,S} {3,S}
2 C 0 0 {1,S} {4,D} {5,S}
3 C 0 0 {1,S} {4,S} {6,S} {7,S}
4 C 0 0 {2,D} {3,S} {8,S}
5 H 0 0 {2,S}
6 H 0 0 {3,S}
7 H 0 0 {3,S}
8 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.061,18.436,22.192,25.213,29.643,32.733,37.351],'cal/(mol*K)'),
        H298 = (12.636,'kcal/mol'),
        S298 = (62.927,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 131,
    label = "allyloxy",
    molecule = 
"""
1 C 0 0 {2,D} {5,S} {6,S}
2 C 0 0 {1,D} {3,S} {7,S}
3 C 0 0 {2,S} {4,S} {8,S} {9,S}
4 O 1 2 {3,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {2,S}
8 H 0 0 {3,S}
9 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.451,22.366,25.849,28.762,33.265,36.562,41.635],'cal/(mol*K)'),
        H298 = (23.695,'kcal/mol'),
        S298 = (72.632,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 132,
    label = "propen2oxy",
    molecule = 
"""
1 C 0 0 {2,D} {5,S} {6,S}
2 C 0 0 {1,D} {3,S} {4,S}
3 C 0 0 {2,S} {7,S} {8,S} {9,S}
4 O 1 2 {2,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {3,S}
8 H 0 0 {3,S}
9 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([17.861,21.848,25.33,28.259,32.823,36.173,41.247],'cal/(mol*K)'),
        H298 = (-6.892,'kcal/mol'),
        S298 = (72.934,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 133,
    label = "CH2CH2CHO",
    molecule = 
"""
1 C 1 0 {2,S} {5,S} {6,S}
2 C 0 0 {1,S} {3,S} {7,S} {8,S}
3 C 0 0 {2,S} {4,D} {9,S}
4 O 0 2 {3,D}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {2,S}
8 H 0 0 {2,S}
9 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([19.408,22.494,25.45,28.064,32.311,35.534,40.591],'cal/(mol*K)'),
        H298 = (6.623,'kcal/mol'),
        S298 = (75.408,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 134,
    label = "oxiranylmethyl",
    molecule = 
"""
1 C 1 0 {2,S} {5,S} {6,S}
2 C 0 0 {1,S} {3,S} {4,S} {7,S}
3 C 0 0 {2,S} {4,S} {8,S} {9,S}
4 O 0 2 {2,S} {3,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {2,S}
8 H 0 0 {3,S}
9 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([17.893,22.389,26.157,29.167,33.614,36.786,41.683],'cal/(mol*K)'),
        H298 = (25.964,'kcal/mol'),
        S298 = (69.926,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 135,
    label = "CH2OCHCH2",
    molecule = 
"""
1 C 1 0 {2,S} {5,S} {6,S}
2 O 0 2 {1,S} {3,S}
3 C 0 0 {2,S} {4,D} {7,S}
4 C 0 0 {3,D} {8,S} {9,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {3,S}
8 H 0 0 {4,S}
9 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([19.071,23.063,26.469,29.237,33.387,36.377,41.022],'cal/(mol*K)'),
        H298 = (22.086,'kcal/mol'),
        S298 = (72.905,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 136,
    label = "CH3CHCHO",
    molecule = 
"""
1 C 0 0 {2,S} {5,S} {6,S} {7,S}
2 C 1 0 {1,S} {3,S} {8,S}
3 C 0 0 {2,S} {4,D} {9,S}
4 O 0 2 {3,D}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {1,S}
8 H 0 0 {2,S}
9 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.055,21.584,24.93,27.854,32.529,36.02,41.385],'cal/(mol*K)'),
        H298 = (-5.7,'kcal/mol'),
        S298 = (71.271,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 137,
    label = "CH3CH2CO",
    molecule = 
"""
1 C 0 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 0 {1,S} {3,S} {8,S} {9,S}
3 C 1 0 {2,S} {4,D}
4 O 0 2 {3,D}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {1,S}
8 H 0 0 {2,S}
9 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([17.762,20.928,24.041,26.823,31.363,34.804,40.182],'cal/(mol*K)'),
        H298 = (-6.919,'kcal/mol'),
        S298 = (74.679,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 138,
    label = "oxetanyl2",
    molecule = 
"""
1 O 0 2 {2,S} {3,S}
2 C 1 0 {1,S} {4,S} {5,S}
3 C 0 0 {1,S} {4,S} {6,S} {7,S}
4 C 0 0 {2,S} {3,S} {8,S} {9,S}
5 H 0 0 {2,S}
6 H 0 0 {3,S}
7 H 0 0 {3,S}
8 H 0 0 {4,S}
9 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([15.345,20.118,24.337,27.798,32.981,36.653,42.164],'cal/(mol*K)'),
        H298 = (24.42,'kcal/mol'),
        S298 = (67.616,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 139,
    label = "oxetanyl3",
    molecule = 
"""
1 O 0 2 {2,S} {3,S}
2 C 0 0 {1,S} {4,S} {5,S} {6,S}
3 C 0 0 {1,S} {4,S} {7,S} {8,S}
4 C 1 0 {2,S} {3,S} {9,S}
5 H 0 0 {2,S}
6 H 0 0 {2,S}
7 H 0 0 {3,S}
8 H 0 0 {3,S}
9 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([16.188,20.783,24.882,28.263,33.353,36.969,42.379],'cal/(mol*K)'),
        H298 = (30.557,'kcal/mol'),
        S298 = (66.777,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 140,
    label = "hydroxyl1allyl",
    molecule = 
"""
1 C 1 0 {2,S} {5,S} {6,S}
2 C 0 0 {1,S} {3,D} {7,S}
3 C 0 0 {2,D} {4,S} {8,S}
4 O 0 2 {3,S} {9,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {2,S}
8 H 0 0 {3,S}
9 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([19.347,23.577,27.069,29.849,33.947,36.892,41.563],'cal/(mol*K)'),
        H298 = (-2.209,'kcal/mol'),
        S298 = (70.175,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 141,
    label = "hydroxyl2allyl",
    molecule = 
"""
1 C 1 0 {2,S} {5,S} {6,S}
2 C 0 0 {1,S} {3,D} {4,S}
3 C 0 0 {2,D} {7,S} {8,S}
4 O 0 2 {2,S} {9,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {3,S}
8 H 0 0 {3,S}
9 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([19.737,24.218,27.654,30.297,34.159,36.969,41.531],'cal/(mol*K)'),
        H298 = (-1.576,'kcal/mol'),
        S298 = (69.254,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 142,
    label = "acetone",
    molecule = 
"""
1  O 0 2 {2,D}
2  C 0 0 {1,D} {3,S} {4,S}
3  C 0 0 {2,S} {5,S} {6,S} {7,S}
4  C 0 0 {2,S} {8,S} {9,S} {10,S}
5  H 0 0 {3,S}
6  H 0 0 {3,S}
7  H 0 0 {3,S}
8  H 0 0 {4,S}
9  H 0 0 {4,S}
10 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([17.532,21.653,25.522,28.904,34.336,38.414,44.767],'cal/(mol*K)'),
        H298 = (-51.977,'kcal/mol'),
        S298 = (70.899,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 143,
    label = "propanal",
    molecule = 
"""
1  C 0 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 0 {2,S} {4,D} {10,S}
4  O 0 2 {3,D}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {2,S}
10 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.919,22.416,25.987,29.231,34.574,38.63,44.939],'cal/(mol*K)'),
        H298 = (-45.041,'kcal/mol'),
        S298 = (73.497,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 144,
    label = "propen1ol",
    molecule = 
"""
1  C 0 0 {2,D} {4,S} {5,S}
2  C 0 0 {1,D} {3,S} {6,S}
3  C 0 0 {2,S} {7,S} {8,S} {9,S}
4  O 0 2 {1,S} {10,S}
5  H 0 0 {1,S}
6  H 0 0 {2,S}
7  H 0 0 {3,S}
8  H 0 0 {3,S}
9  H 0 0 {3,S}
10 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.671,24.561,28.022,30.977,35.68,39.253,45.019],'cal/(mol*K)'),
        H298 = (-35.849,'kcal/mol'),
        S298 = (70.849,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 145,
    label = "propen2ol",
    molecule = 
"""
1  C 0 0 {2,D} {5,S} {6,S}
2  C 0 0 {1,D} {3,S} {4,S}
3  C 0 0 {2,S} {7,S} {8,S} {9,S}
4  O 0 2 {2,S} {10,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {3,S}
8  H 0 0 {3,S}
9  H 0 0 {3,S}
10 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.595,25.298,29.058,32.045,36.547,39.89,45.318],'cal/(mol*K)'),
        H298 = (-40.585,'kcal/mol'),
        S298 = (69.602,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 146,
    label = "cC3H6O",
    molecule = 
"""
1  C 0 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 0 {1,S} {3,S} {4,S} {8,S}
3  C 0 0 {2,S} {4,S} {9,S} {10,S}
4  O 0 2 {2,S} {3,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {3,S}
10 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([17.377,22.084,26.33,29.916,35.483,39.565,45.86],'cal/(mol*K)'),
        H298 = (-22.254,'kcal/mol'),
        S298 = (68.534,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 147,
    label = "oxetane",
    molecule = 
"""
1  O 0 2 {2,S} {3,S}
2  C 0 0 {1,S} {4,S} {5,S} {6,S}
3  C 0 0 {1,S} {4,S} {7,S} {8,S}
4  C 0 0 {2,S} {3,S} {9,S} {10,S}
5  H 0 0 {2,S}
6  H 0 0 {2,S}
7  H 0 0 {3,S}
8  H 0 0 {3,S}
9  H 0 0 {4,S}
10 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([15.214,20.428,25.24,29.292,35.485,39.924,46.599],'cal/(mol*K)'),
        H298 = (-18.984,'kcal/mol'),
        S298 = (65.615,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 148,
    label = "propen3ol",
    molecule = 
"""
1  C 0 0 {2,D} {5,S} {6,S}
2  C 0 0 {1,D} {3,S} {7,S}
3  C 0 0 {2,S} {4,S} {8,S} {9,S}
4  O 0 2 {3,S} {10,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {2,S}
8  H 0 0 {3,S}
9  H 0 0 {3,S}
10 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([21.542,25.014,28.203,31.012,35.6,39.144,44.922],'cal/(mol*K)'),
        H298 = (-30.08,'kcal/mol'),
        S298 = (72.639,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 149,
    label = "cyclopropanol",
    molecule = 
"""
1  C 0 0 {2,S} {3,S} {4,S} {5,S}
2  C 0 0 {1,S} {3,S} {6,S} {7,S}
3  C 0 0 {1,S} {2,S} {8,S} {9,S}
4  O 0 2 {1,S} {10,S}
5  H 0 0 {1,S}
6  H 0 0 {2,S}
7  H 0 0 {2,S}
8  H 0 0 {3,S}
9  H 0 0 {3,S}
10 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.046,23.137,27.432,30.893,36.073,39.831,45.769],'cal/(mol*K)'),
        H298 = (-24.243,'kcal/mol'),
        S298 = (68.026,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 150,
    label = "npropoxy",
    molecule = 
"""
1  C 0 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 0 {2,S} {4,S} {10,S} {11,S}
4  O 1 2 {3,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {2,S}
10 H 0 0 {3,S}
11 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.762,25.478,29.707,33.323,39.081,43.409,50.173],'cal/(mol*K)'),
        H298 = (-8.073,'kcal/mol'),
        S298 = (75.655,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 151,
    label = "ipropoxy",
    molecule = 
"""
1  C 0 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 0 {1,S} {3,S} {4,S} {8,S}
3  C 0 0 {2,S} {9,S} {10,S} {11,S}
4  O 1 2 {2,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {3,S}
10 H 0 0 {3,S}
11 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.827,25.556,29.742,33.303,38.965,43.242,50],'cal/(mol*K)'),
        H298 = (-10.664,'kcal/mol'),
        S298 = (72.525,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 152,
    label = "CH2CH2CH2OH",
    molecule = 
"""
1  C 1 0 {2,S} {5,S} {6,S}
2  C 0 0 {1,S} {3,S} {7,S} {8,S}
3  C 0 0 {2,S} {4,S} {9,S} {10,S}
4  O 0 2 {3,S} {11,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {2,S}
8  H 0 0 {2,S}
9  H 0 0 {3,S}
10 H 0 0 {3,S}
11 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([22.039,26.168,30.066,33.408,38.68,42.656,49.055],'cal/(mol*K)'),
        H298 = (-11.538,'kcal/mol'),
        S298 = (79.475,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 153,
    label = "CH3CH2CHOH",
    molecule = 
"""
1  C 0 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 0 {1,S} {3,S} {8,S} {9,S}
3  C 1 0 {2,S} {4,S} {10,S}
4  O 0 2 {3,S} {11,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {2,S}
10 H 0 0 {3,S}
11 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([21.219,25.668,29.69,33.112,38.509,42.571,49.06],'cal/(mol*K)'),
        H298 = (-17.59,'kcal/mol'),
        S298 = (78.735,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 154,
    label = "CH3CHCH2OH",
    molecule = 
"""
1  C 0 0 {2,S} {5,S} {6,S} {7,S}
2  C 1 0 {1,S} {3,S} {8,S}
3  C 0 0 {2,S} {4,S} {9,S} {10,S}
4  O 0 2 {3,S} {11,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {3,S}
10 H 0 0 {3,S}
11 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([21.043,25.107,28.976,32.376,37.867,42.053,48.757],'cal/(mol*K)'),
        H298 = (-13.795,'kcal/mol'),
        S298 = (80.42,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 155,
    label = "CH3CHOHCH2",
    molecule = 
"""
1  C 0 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 0 {1,S} {3,S} {4,S} {8,S}
3  C 1 0 {2,S} {9,S} {10,S}
4  O 0 2 {2,S} {11,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {3,S}
10 H 0 0 {3,S}
11 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([22.674,26.974,30.742,33.915,38.934,42.771,49.052],'cal/(mol*K)'),
        H298 = (-14.714,'kcal/mol'),
        S298 = (77.935,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 156,
    label = "CH3COHCH3",
    molecule = 
"""
1  C 0 0 {2,S} {5,S} {6,S} {7,S}
2  C 1 0 {1,S} {3,S} {4,S}
3  C 0 0 {2,S} {8,S} {9,S} {10,S}
4  O 0 2 {2,S} {11,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {3,S}
9  H 0 0 {3,S}
10 H 0 0 {3,S}
11 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([21.775,26.053,29.947,33.298,38.637,42.675,49.128],'cal/(mol*K)'),
        H298 = (-22.896,'kcal/mol'),
        S298 = (74.562,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 157,
    label = "CH3CH2OCH2",
    molecule = 
"""
1  C 0 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 0 {1,S} {3,S} {8,S} {9,S}
3  O 0 2 {2,S} {4,S}
4  C 1 0 {3,S} {10,S} {11,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {2,S}
10 H 0 0 {4,S}
11 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([21.441,25.698,29.733,33.234,38.792,42.947,49.453],'cal/(mol*K)'),
        H298 = (-7.287,'kcal/mol'),
        S298 = (76.058,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 158,
    label = "CH2CH2OCH3",
    molecule = 
"""
1  C 1 0 {2,S} {5,S} {6,S}
2  C 0 0 {1,S} {3,S} {7,S} {8,S}
3  O 0 2 {2,S} {4,S}
4  C 0 0 {3,S} {9,S} {10,S} {11,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {2,S}
8  H 0 0 {2,S}
9  H 0 0 {4,S}
10 H 0 0 {4,S}
11 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([21.214,25.297,29.205,32.656,38.258,42.512,49.206],'cal/(mol*K)'),
        H298 = (-1.319,'kcal/mol'),
        S298 = (77.592,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 159,
    label = "CH3CHOCH3",
    molecule = 
"""
1  C 0 0 {2,S} {5,S} {6,S} {7,S}
2  C 1 0 {1,S} {3,S} {8,S}
3  O 0 2 {2,S} {4,S}
4  C 0 0 {3,S} {9,S} {10,S} {11,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {4,S}
10 H 0 0 {4,S}
11 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([21.477,25.803,29.729,33.086,38.465,42.577,49.155],'cal/(mol*K)'),
        H298 = (-8.641,'kcal/mol'),
        S298 = (75.541,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 160,
    label = "npropanol",
    molecule = 
"""
1  C 0 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 0 {2,S} {4,S} {10,S} {11,S}
4  O 0 2 {3,S} {12,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {2,S}
10 H 0 0 {3,S}
11 H 0 0 {3,S}
12 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.866,25.943,30.623,34.65,41.045,45.854,53.483],'cal/(mol*K)'),
        H298 = (-61.284,'kcal/mol'),
        S298 = (76.307,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 161,
    label = "ipropanol",
    molecule = 
"""
1  C 0 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 0 {1,S} {3,S} {4,S} {8,S}
3  C 0 0 {2,S} {9,S} {10,S} {11,S}
4  O 0 2 {2,S} {12,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {3,S}
10 H 0 0 {3,S}
11 H 0 0 {3,S}
12 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([21.77,26.888,31.47,35.354,41.489,46.126,53.569],'cal/(mol*K)'),
        H298 = (-65.424,'kcal/mol'),
        S298 = (74.202,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 162,
    label = "EME",
    molecule = 
"""
1  C 0 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 0 {1,S} {3,S} {8,S} {9,S}
3  O 0 2 {2,S} {4,S}
4  C 0 0 {3,S} {10,S} {11,S} {12,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {2,S}
10 H 0 0 {4,S}
11 H 0 0 {4,S}
12 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([22.572,26.948,31.119,34.897,41.198,46.07,53.781],'cal/(mol*K)'),
        H298 = (-51.942,'kcal/mol'),
        S298 = (73.519,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 163,
    label = "allylperoxy",
    molecule = 
"""
1  C 0 0 {2,D} {6,S} {7,S}
2  C 0 0 {1,D} {3,S} {8,S}
3  C 0 0 {2,S} {4,S} {9,S} {10,S}
4  O 0 2 {3,S} {5,S}
5  O 1 2 {4,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {3,S}
10 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([21.146,25.434,29.199,32.34,37.164,40.674,46.074],'cal/(mol*K)'),
        H298 = (21.2,'kcal/mol'),
        S298 = (80.556,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 164,
    label = "propen1peroxy",
    molecule = 
"""
1  C 0 0 {2,D} {4,S} {6,S}
2  C 0 0 {1,D} {3,S} {7,S}
3  C 0 0 {2,S} {8,S} {9,S} {10,S}
4  O 0 2 {1,S} {5,S}
5  O 1 2 {4,S}
6  H 0 0 {1,S}
7  H 0 0 {2,S}
8  H 0 0 {3,S}
9  H 0 0 {3,S}
10 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([22.446,26.758,30.497,33.584,38.244,41.571,46.621],'cal/(mol*K)'),
        H298 = (19.177,'kcal/mol'),
        S298 = (76.696,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 165,
    label = "propen2peroxy",
    molecule = 
"""
1  C 0 0 {2,D} {6,S} {7,S}
2  C 0 0 {1,D} {3,S} {4,S}
3  C 0 0 {2,S} {8,S} {9,S} {10,S}
4  O 0 2 {2,S} {5,S}
5  O 1 2 {4,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {3,S}
9  H 0 0 {3,S}
10 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.081,27.645,31.326,34.258,38.62,41.761,46.637],'cal/(mol*K)'),
        H298 = (15.984,'kcal/mol'),
        S298 = (76.198,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 166,
    label = "OCHCH2CH2O",
    molecule = 
"""
1  O 1 2 {2,S}
2  C 0 0 {1,S} {3,S} {6,S} {7,S}
3  C 0 0 {2,S} {4,S} {8,S} {9,S}
4  C 0 0 {3,S} {5,D} {10,S}
5  O 0 2 {4,D}
6  H 0 0 {2,S}
7  H 0 0 {2,S}
8  H 0 0 {3,S}
9  H 0 0 {3,S}
10 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.717,24.95,28.848,32.167,37.303,40.995,46.475],'cal/(mol*K)'),
        H298 = (-25.676,'kcal/mol'),
        S298 = (82.319,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 167,
    label = "CH3CHOCHO",
    molecule = 
"""
1  C 0 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 0 {1,S} {3,S} {4,S} {9,S}
3  C 0 0 {2,S} {5,D} {10,S}
4  O 1 2 {2,S}
5  O 0 2 {3,D}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {1,S}
9  H 0 0 {2,S}
10 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([22.135,26.412,30.173,33.3,38.066,41.488,46.644],'cal/(mol*K)'),
        H298 = (-27.168,'kcal/mol'),
        S298 = (79.542,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 168,
    label = "CH3COCH2O",
    molecule = 
"""
1  C 0 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 0 {1,S} {3,S} {4,D}
3  C 0 0 {2,S} {5,S} {9,S} {10,S}
4  O 0 2 {2,D}
5  O 1 2 {3,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {1,S}
9  H 0 0 {3,S}
10 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([21.085,25.767,29.923,33.337,38.348,41.786,46.818],'cal/(mol*K)'),
        H298 = (-31.345,'kcal/mol'),
        S298 = (78.328,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 169,
    label = "oxiranylmethoxy",
    molecule = 
"""
1  O 1 2 {2,S}
2  C 0 0 {1,S} {3,S} {6,S} {7,S}
3  C 0 0 {2,S} {4,S} {5,S} {8,S}
4  C 0 0 {3,S} {5,S} {9,S} {10,S}
5  O 0 2 {3,S} {4,S}
6  H 0 0 {2,S}
7  H 0 0 {2,S}
8  H 0 0 {3,S}
9  H 0 0 {4,S}
10 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([19.761,24.69,29.063,32.657,38.018,41.772,47.306],'cal/(mol*K)'),
        H298 = (-2.738,'kcal/mol'),
        S298 = (76.885,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 170,
    label = "CH2CHCH2OOH",
    molecule = 
"""
1  C 0 0 {2,D} {6,S} {7,S}
2  C 0 0 {1,D} {3,S} {8,S}
3  C 0 0 {2,S} {4,S} {9,S} {10,S}
4  O 0 2 {3,S} {5,S}
5  O 0 2 {4,S} {11,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {3,S}
10 H 0 0 {3,S}
11 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.135,29.031,32.69,35.843,40.796,44.469,50.249],'cal/(mol*K)'),
        H298 = (-11.901,'kcal/mol'),
        S298 = (82.028,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 171,
    label = "propen1ooh",
    molecule = 
"""
1  C 0 0 {2,D} {4,S} {6,S}
2  C 0 0 {1,D} {3,S} {7,S}
3  C 0 0 {2,S} {8,S} {9,S} {10,S}
4  O 0 2 {1,S} {5,S}
5  O 0 2 {4,S} {11,S}
6  H 0 0 {1,S}
7  H 0 0 {2,S}
8  H 0 0 {3,S}
9  H 0 0 {3,S}
10 H 0 0 {3,S}
11 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.578,28.046,31.992,35.298,40.409,44.17,50.069],'cal/(mol*K)'),
        H298 = (-15.283,'kcal/mol'),
        S298 = (81.557,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 172,
    label = "propen2ooh",
    molecule = 
"""
1  C 0 0 {2,D} {6,S} {7,S}
2  C 0 0 {1,D} {3,S} {4,S}
3  C 0 0 {2,S} {8,S} {9,S} {10,S}
4  O 0 2 {2,S} {5,S}
5  O 0 2 {4,S} {11,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {3,S}
9  H 0 0 {3,S}
10 H 0 0 {3,S}
11 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([24.922,29.698,33.46,36.482,41.122,44.595,50.198],'cal/(mol*K)'),
        H298 = (-19.819,'kcal/mol'),
        S298 = (78.901,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 173,
    label = "npropylperoxy",
    molecule = 
"""
1  C 0 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 2 {3,S} {5,S}
5  O 1 2 {4,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {1,S}
9  H 0 0 {2,S}
10 H 0 0 {2,S}
11 H 0 0 {3,S}
12 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.015,28.238,32.94,36.915,43.109,47.671,54.73],'cal/(mol*K)'),
        H298 = (-9.762,'kcal/mol'),
        S298 = (83.486,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 174,
    label = "ipropylperoxy",
    molecule = 
"""
1  C 0 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 0 {1,S} {3,S} {4,S} {9,S}
3  C 0 0 {2,S} {10,S} {11,S} {12,S}
4  O 0 2 {2,S} {5,S}
5  O 1 2 {4,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {1,S}
9  H 0 0 {2,S}
10 H 0 0 {3,S}
11 H 0 0 {3,S}
12 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([24.247,29.244,33.669,37.422,43.342,47.771,54.724],'cal/(mol*K)'),
        H298 = (-14.373,'kcal/mol'),
        S298 = (80.87,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 175,
    label = "QOOH_1",
    molecule = 
"""
1  C 1 0 {2,S} {6,S} {7,S}
2  C 0 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 0 {2,S} {4,S} {10,S} {11,S}
4  O 0 2 {3,S} {5,S}
5  O 0 2 {4,S} {12,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {2,S}
10 H 0 0 {3,S}
11 H 0 0 {3,S}
12 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.248,30.372,34.765,38.398,43.989,48.101,54.526],'cal/(mol*K)'),
        H298 = (6.809,'kcal/mol'),
        S298 = (88.506,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 176,
    label = "QOOH_2",
    molecule = 
"""
1  C 0 0 {2,S} {6,S} {7,S} {8,S}
2  C 1 0 {1,S} {3,S} {9,S}
3  C 0 0 {2,S} {4,S} {10,S} {11,S}
4  O 0 2 {3,S} {5,S}
5  O 0 2 {4,S} {12,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {1,S}
9  H 0 0 {2,S}
10 H 0 0 {3,S}
11 H 0 0 {3,S}
12 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([24.23,29.075,33.496,37.257,43.123,47.442,54.148],'cal/(mol*K)'),
        H298 = (4.644,'kcal/mol'),
        S298 = (88.239,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 177,
    label = "QOOH_3",
    molecule = 
"""
1  C 1 0 {2,S} {6,S} {7,S}
2  C 0 0 {1,S} {3,S} {4,S} {8,S}
3  C 0 0 {2,S} {9,S} {10,S} {11,S}
4  O 0 2 {2,S} {5,S}
5  O 0 2 {4,S} {12,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {3,S}
10 H 0 0 {3,S}
11 H 0 0 {3,S}
12 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([26.485,31.256,35.42,38.884,44.223,48.167,54.418],'cal/(mol*K)'),
        H298 = (4.077,'kcal/mol'),
        S298 = (86.863,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 178,
    label = "npropylooh",
    molecule = 
"""
1  C 0 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 2 {3,S} {5,S}
5  O 0 2 {4,S} {13,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {1,S}
9  H 0 0 {2,S}
10 H 0 0 {2,S}
11 H 0 0 {3,S}
12 H 0 0 {3,S}
13 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.706,31.192,36.068,40.199,46.678,51.491,59.007],'cal/(mol*K)'),
        H298 = (-43.306,'kcal/mol'),
        S298 = (84.192,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 179,
    label = "ipropylooh",
    molecule = 
"""
1  C 0 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 0 {1,S} {3,S} {4,S} {9,S}
3  C 0 0 {2,S} {10,S} {11,S} {12,S}
4  O 0 2 {2,S} {5,S}
5  O 0 2 {4,S} {13,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {1,S}
9  H 0 0 {2,S}
10 H 0 0 {3,S}
11 H 0 0 {3,S}
12 H 0 0 {3,S}
13 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([26.878,32.342,37.095,41.079,47.288,51.904,59.171],'cal/(mol*K)'),
        H298 = (-47.686,'kcal/mol'),
        S298 = (82.43,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 180,
    label = "CH3CHOOCHO",
    molecule = 
"""
1  C 0 0 {2,S} {7,S} {8,S} {9,S}
2  C 0 0 {1,S} {3,S} {5,S} {10,S}
3  C 0 0 {2,S} {4,D} {11,S}
4  O 0 2 {3,D}
5  O 0 2 {2,S} {6,S}
6  O 1 2 {5,S}
7  H 0 0 {1,S}
8  H 0 0 {1,S}
9  H 0 0 {1,S}
10 H 0 0 {2,S}
11 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.578,30.377,34.459,37.764,42.677,46.156,51.402],'cal/(mol*K)'),
        H298 = (-28.683,'kcal/mol'),
        S298 = (86.84,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 181,
    label = "OCHCH2CH2OO",
    molecule = 
"""
1  O 0 2 {2,D}
2  C 0 0 {1,D} {3,S} {7,S}
3  C 0 0 {2,S} {4,S} {8,S} {9,S}
4  C 0 0 {3,S} {5,S} {10,S} {11,S}
5  O 0 2 {4,S} {6,S}
6  O 1 2 {5,S}
7  H 0 0 {2,S}
8  H 0 0 {3,S}
9  H 0 0 {3,S}
10 H 0 0 {4,S}
11 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.204,31.13,34.486,37.418,42.17,45.728,51.188],'cal/(mol*K)'),
        H298 = (-27.501,'kcal/mol'),
        S298 = (88.332,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 182,
    label = "CH3COCH2OO",
    molecule = 
"""
1  C 0 0 {2,S} {7,S} {8,S} {9,S}
2  C 0 0 {1,S} {3,S} {4,D}
3  C 0 0 {2,S} {5,S} {10,S} {11,S}
4  O 0 2 {2,D}
5  O 0 2 {3,S} {6,S}
6  O 1 2 {5,S}
7  H 0 0 {1,S}
8  H 0 0 {1,S}
9  H 0 0 {1,S}
10 H 0 0 {3,S}
11 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.238,29.958,33.996,37.299,42.286,45.858,51.258],'cal/(mol*K)'),
        H298 = (-31.999,'kcal/mol'),
        S298 = (86.932,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 183,
    label = "oxiranylmoo",
    molecule = 
"""
1  O 1 2 {2,S}
2  O 0 2 {1,S} {3,S}
3  C 0 0 {2,S} {4,S} {7,S} {8,S}
4  C 0 0 {3,S} {5,S} {6,S} {9,S}
5  C 0 0 {4,S} {6,S} {10,S} {11,S}
6  O 0 2 {4,S} {5,S}
7  H 0 0 {3,S}
8  H 0 0 {3,S}
9  H 0 0 {4,S}
10 H 0 0 {5,S}
11 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.625,28.595,33.065,36.764,42.289,46.16,51.895],'cal/(mol*K)'),
        H298 = (-3.756,'kcal/mol'),
        S298 = (85.336,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 184,
    label = "CH3CHOOHCHO",
    molecule = 
"""
1  C 0 0 {2,S} {7,S} {8,S} {9,S}
2  C 0 0 {1,S} {3,S} {4,S} {10,S}
3  C 0 0 {2,S} {6,D} {11,S}
4  O 0 2 {2,S} {5,S}
5  O 0 2 {4,S} {12,S}
6  O 0 2 {3,D}
7  H 0 0 {1,S}
8  H 0 0 {1,S}
9  H 0 0 {1,S}
10 H 0 0 {2,S}
11 H 0 0 {3,S}
12 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([28.656,33.764,38.091,41.614,46.838,50.504,56.009],'cal/(mol*K)'),
        H298 = (-64.046,'kcal/mol'),
        S298 = (86.869,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 185,
    label = "OCHCH2CH2OOH",
    molecule = 
"""
1  O 0 2 {2,D}
2  C 0 0 {1,D} {3,S} {7,S}
3  C 0 0 {2,S} {4,S} {8,S} {9,S}
4  C 0 0 {3,S} {5,S} {10,S} {11,S}
5  O 0 2 {4,S} {6,S}
6  O 0 2 {5,S} {12,S}
7  H 0 0 {2,S}
8  H 0 0 {3,S}
9  H 0 0 {3,S}
10 H 0 0 {4,S}
11 H 0 0 {4,S}
12 H 0 0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.398,33.269,36.951,40.23,45.513,49.441,55.469],'cal/(mol*K)'),
        H298 = (-61.721,'kcal/mol'),
        S298 = (89.678,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 186,
    label = "CH3COCH2OOH",
    molecule = 
"""
1  C 0 0 {2,S} {7,S} {8,S} {9,S}
2  C 0 0 {1,S} {3,S} {4,D}
3  C 0 0 {2,S} {5,S} {10,S} {11,S}
4  O 0 2 {2,D}
5  O 0 2 {3,S} {6,S}
6  O 0 2 {5,S} {12,S}
7  H 0 0 {1,S}
8  H 0 0 {1,S}
9  H 0 0 {1,S}
10 H 0 0 {3,S}
11 H 0 0 {3,S}
12 H 0 0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([28.339,33.752,38.208,41.764,46.966,50.605,56.094],'cal/(mol*K)'),
        H298 = (-68.961,'kcal/mol'),
        S298 = (85.834,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 187,
    label = "cC2H3OCH2OOH",
    molecule = 
"""
1  O 0 2 {2,S} {3,S}
2  C 0 0 {1,S} {3,S} {7,S} {8,S}
3  C 0 0 {1,S} {2,S} {4,S} {9,S}
4  C 0 0 {3,S} {5,S} {10,S} {11,S}
5  O 0 2 {4,S} {6,S}
6  O 0 2 {5,S} {12,S}
7  H 0 0 {2,S}
8  H 0 0 {2,S}
9  H 0 0 {3,S}
10 H 0 0 {4,S}
11 H 0 0 {4,S}
12 H 0 0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([28.904,34.868,39.572,43.175,48.19,51.591,56.799],'cal/(mol*K)'),
        H298 = (-40.231,'kcal/mol'),
        S298 = (82.285,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 188,
    label = "HOOCH2CH2CH2OO",
    molecule = 
"""
1  O 0 2 {2,S} {8,S}
2  O 0 2 {1,S} {3,S}
3  C 0 0 {2,S} {4,S} {9,S} {10,S}
4  C 0 0 {3,S} {5,S} {11,S} {12,S}
5  C 0 0 {4,S} {6,S} {13,S} {14,S}
6  O 0 2 {5,S} {7,S}
7  O 1 2 {6,S}
8  H 0 0 {1,S}
9  H 0 0 {3,S}
10 H 0 0 {3,S}
11 H 0 0 {4,S}
12 H 0 0 {4,S}
13 H 0 0 {5,S}
14 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([34.868,40.135,44.707,48.533,54.436,58.745,65.38],'cal/(mol*K)'),
        H298 = (-28.14,'kcal/mol'),
        S298 = (97.982,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 189,
    label = "CH3CHOOCH2OOH",
    molecule = 
"""
1  C 0 0 {2,S} {8,S} {9,S} {10,S}
2  C 0 0 {1,S} {3,S} {6,S} {11,S}
3  C 0 0 {2,S} {4,S} {12,S} {13,S}
4  O 0 2 {3,S} {5,S}
5  O 0 2 {4,S} {14,S}
6  O 0 2 {2,S} {7,S}
7  O 1 2 {6,S}
8  H 0 0 {1,S}
9  H 0 0 {1,S}
10 H 0 0 {1,S}
11 H 0 0 {2,S}
12 H 0 0 {3,S}
13 H 0 0 {3,S}
14 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([36.165,41.945,46.337,49.781,55.071,59.075,65.505],'cal/(mol*K)'),
        H298 = (-31.242,'kcal/mol'),
        S298 = (97.229,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 190,
    label = "CH3CHOOHCH2OO",
    molecule = 
"""
1  C 0 0 {2,S} {8,S} {9,S} {10,S}
2  C 0 0 {1,S} {3,S} {6,S} {11,S}
3  C 0 0 {2,S} {4,S} {12,S} {13,S}
4  O 0 2 {3,S} {5,S}
5  O 1 2 {4,S}
6  O 0 2 {2,S} {7,S}
7  O 0 2 {6,S} {14,S}
8  H 0 0 {1,S}
9  H 0 0 {1,S}
10 H 0 0 {1,S}
11 H 0 0 {2,S}
12 H 0 0 {3,S}
13 H 0 0 {3,S}
14 H 0 0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([36.515,42.429,47.245,51.041,56.519,60.371,66.327],'cal/(mol*K)'),
        H298 = (-31.149,'kcal/mol'),
        S298 = (96.95,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 191,
    label = "HOOCH2CHCH2OOH",
    molecule = 
"""
1  O 0 2 {2,S} {8,S}
2  O 0 2 {1,S} {3,S}
3  C 0 0 {2,S} {4,S} {9,S} {10,S}
4  C 1 0 {3,S} {5,S} {11,S}
5  C 0 0 {4,S} {6,S} {12,S} {13,S}
6  O 0 2 {5,S} {7,S}
7  O 0 2 {6,S} {14,S}
8  H 0 0 {1,S}
9  H 0 0 {3,S}
10 H 0 0 {3,S}
11 H 0 0 {4,S}
12 H 0 0 {5,S}
13 H 0 0 {5,S}
14 H 0 0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([38.231,48.369,54.363,57.483,60.489,62.478,66.333],'cal/(mol*K)'),
        H298 = (-15.611,'kcal/mol'),
        S298 = (95.309,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 192,
    label = "CH2CHOOHCH2OOH",
    molecule = 
"""
1  C 1 0 {2,S} {8,S} {9,S}
2  C 0 0 {1,S} {3,S} {6,S} {10,S}
3  C 0 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 2 {3,S} {5,S}
5  O 0 2 {4,S} {13,S}
6  O 0 2 {2,S} {7,S}
7  O 0 2 {6,S} {14,S}
8  H 0 0 {1,S}
9  H 0 0 {1,S}
10 H 0 0 {2,S}
11 H 0 0 {3,S}
12 H 0 0 {3,S}
13 H 0 0 {5,S}
14 H 0 0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([35.627,41.461,46.23,49.999,55.508,59.397,65.337],'cal/(mol*K)'),
        H298 = (-15.837,'kcal/mol'),
        S298 = (103.475,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 193,
    label = "HCCCCH",
    molecule = 
"""
1 C 0 0 {2,T} {5,S}
2 C 0 0 {1,T} {3,S}
3 C 0 0 {2,S} {4,T}
4 C 0 0 {3,T} {6,S}
5 H 0 0 {1,S}
6 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([17.017,19.654,21.44,22.778,24.797,26.331,28.861],'cal/(mol*K)'),
        H298 = (109.864,'kcal/mol'),
        S298 = (58.912,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 194,
    label = "HCCCHCH",
    molecule = 
"""
1 C 0 0 {2,T} {5,S}
2 C 0 0 {1,T} {3,S}
3 C 0 0 {2,S} {4,D} {6,S}
4 C 1 0 {3,D} {7,S}
5 H 0 0 {1,S}
6 H 0 0 {3,S}
7 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([17.244,20.414,22.801,24.664,27.474,29.555,32.868],'cal/(mol*K)'),
        H298 = (130.181,'kcal/mol'),
        S298 = (67.346,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 195,
    label = "CH2CCCH",
    molecule = 
"""
1 C 0 0 {2,D} {5,S} {6,S}
2 C 1 0 {1,D} {3,S}
3 C 0 0 {2,S} {4,T}
4 C 0 0 {3,T} {7,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.68,21.245,23.288,24.972,27.641,29.676,32.946],'cal/(mol*K)'),
        H298 = (118.749,'kcal/mol'),
        S298 = (70.267,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 196,
    label = "CH2CHCCH",
    molecule = 
"""
1 C 0 0 {2,D} {5,S} {6,S}
2 C 0 0 {1,D} {3,S} {7,S}
3 C 0 0 {2,S} {4,T}
4 C 0 0 {3,T} {8,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {2,S}
8 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([17.179,20.88,23.885,26.319,30.057,32.835,37.245],'cal/(mol*K)'),
        H298 = (69.023,'kcal/mol'),
        S298 = (66.235,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 197,
    label = "butatriene123",
    molecule = 
"""
1 C 0 0 {2,D} {5,S} {6,S}
2 C 0 0 {1,D} {3,D}
3 C 0 0 {2,D} {4,D}
4 C 0 0 {3,D} {7,S} {8,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {4,S}
8 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([17.514,21.007,23.923,26.334,30.104,32.926,37.371],'cal/(mol*K)'),
        H298 = (76.698,'kcal/mol'),
        S298 = (65.154,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 198,
    label = "CH3CHCCH",
    molecule = 
"""
1 C 0 0 {2,S} {5,S} {6,S} {7,S}
2 C 1 0 {1,S} {3,S} {8,S}
3 C 0 0 {2,S} {4,T}
4 C 0 0 {3,T} {9,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {1,S}
8 H 0 0 {2,S}
9 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.796,22.592,25.825,28.541,32.837,36.079,41.229],'cal/(mol*K)'),
        H298 = (76.796,'kcal/mol'),
        S298 = (71.892,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 199,
    label = "CH2CHCCH2",
    molecule = 
"""
1 C 0 0 {2,D} {5,S} {6,S}
2 C 1 0 {1,D} {3,S}
3 C 0 0 {2,S} {4,D} {7,S}
4 C 0 0 {3,D} {8,S} {9,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {3,S}
8 H 0 0 {4,S}
9 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.791,23.052,26.587,29.469,33.895,37.167,42.307],'cal/(mol*K)'),
        H298 = (76.211,'kcal/mol'),
        S298 = (69.58,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 200,
    label = "CH2CHCHCH",
    molecule = 
"""
1 C 0 0 {2,D} {5,S} {6,S}
2 C 0 0 {1,D} {3,S} {7,S}
3 C 0 0 {2,S} {4,D} {8,S}
4 C 1 0 {3,D} {9,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {2,S}
8 H 0 0 {3,S}
9 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.727,23.697,27.655,30.652,34.828,37.701,42.137],'cal/(mol*K)'),
        H298 = (86.372,'kcal/mol'),
        S298 = (68.326,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 201,
    label = "butyne1",
    molecule = 
"""
1  C 0 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 0 {2,S} {4,T}
4  C 0 0 {3,T} {10,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {2,S}
10 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([19.467,23.9,27.686,30.861,35.893,39.713,45.811],'cal/(mol*K)'),
        H298 = (40.086,'kcal/mol'),
        S298 = (69.18,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 202,
    label = "CH3CHCCH2",
    molecule = 
"""
1  C 0 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 0 {1,S} {3,D} {8,S}
3  C 0 0 {2,D} {4,D}
4  C 0 0 {3,D} {9,S} {10,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {4,S}
10 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.949,23.2,27.031,30.319,35.571,39.537,45.785],'cal/(mol*K)'),
        H298 = (38.522,'kcal/mol'),
        S298 = (69.709,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 203,
    label = "butadiene13",
    molecule = 
"""
1  C 0 0 {2,D} {5,S} {6,S}
2  C 0 0 {1,D} {3,S} {7,S}
3  C 0 0 {2,S} {4,D} {8,S}
4  C 0 0 {3,D} {9,S} {10,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {2,S}
8  H 0 0 {3,S}
9  H 0 0 {4,S}
10 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.482,23.965,28.661,32.35,37.557,41.123,46.59],'cal/(mol*K)'),
        H298 = (26.497,'kcal/mol'),
        S298 = (65.819,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 204,
    label = "m1_allyl",
    molecule = 
"""
1  C 0 0 {2,S} {5,S} {6,S} {7,S}
2  C 1 0 {1,S} {3,S} {8,S}
3  C 0 0 {2,S} {4,D} {9,S}
4  C 0 0 {3,D} {10,S} {11,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {3,S}
10 H 0 0 {4,S}
11 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([19.86,24.811,29.29,33.101,39.099,43.575,50.602],'cal/(mol*K)'),
        H298 = (32.909,'kcal/mol'),
        S298 = (71.99,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 205,
    label = "m2_allyl",
    molecule = 
"""
1  C 1 0 {2,S} {5,S} {6,S}
2  C 0 0 {1,S} {3,S} {4,D}
3  C 0 0 {2,S} {7,S} {8,S} {9,S}
4  C 0 0 {2,D} {10,S} {11,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {3,S}
8  H 0 0 {3,S}
9  H 0 0 {3,S}
10 H 0 0 {4,S}
11 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([19.588,24.938,29.515,33.315,39.222,43.621,50.574],'cal/(mol*K)'),
        H298 = (33.333,'kcal/mol'),
        S298 = (70.246,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 206,
    label = "buten1yl1",
    molecule = 
"""
1  C 1 0 {2,D} {5,S}
2  C 0 0 {1,D} {3,S} {6,S}
3  C 0 0 {2,S} {4,S} {7,S} {8,S}
4  C 0 0 {3,S} {9,S} {10,S} {11,S}
5  H 0 0 {1,S}
6  H 0 0 {2,S}
7  H 0 0 {3,S}
8  H 0 0 {3,S}
9  H 0 0 {4,S}
10 H 0 0 {4,S}
11 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.575,25.356,29.574,33.154,38.837,43.129,49.921],'cal/(mol*K)'),
        H298 = (59.278,'kcal/mol'),
        S298 = (74.497,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 207,
    label = "buten3yl1",
    molecule = 
"""
1  C 0 0 {2,D} {5,S} {6,S}
2  C 0 0 {1,D} {3,S} {7,S}
3  C 0 0 {2,S} {4,S} {8,S} {9,S}
4  C 1 0 {3,S} {10,S} {11,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {2,S}
8  H 0 0 {3,S}
9  H 0 0 {3,S}
10 H 0 0 {4,S}
11 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.739,25.338,29.497,33.052,38.708,42.987,49.792],'cal/(mol*K)'),
        H298 = (49.793,'kcal/mol'),
        S298 = (75.467,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 208,
    label = "buten22yl",
    molecule = 
"""
1  C 0 0 {2,S} {5,S} {6,S} {7,S}
2  C 1 0 {1,S} {3,D}
3  C 0 0 {2,D} {4,S} {8,S}
4  C 0 0 {3,S} {9,S} {10,S} {11,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {3,S}
9  H 0 0 {4,S}
10 H 0 0 {4,S}
11 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.309,24.46,28.515,32.141,38.08,42.605,49.702],'cal/(mol*K)'),
        H298 = (53.827,'kcal/mol'),
        S298 = (74.383,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 209,
    label = "butene1",
    molecule = 
"""
1  C 0 0 {2,D} {5,S} {6,S}
2  C 0 0 {1,D} {3,S} {7,S}
3  C 0 0 {2,S} {4,S} {8,S} {9,S}
4  C 0 0 {3,S} {10,S} {11,S} {12,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {2,S}
8  H 0 0 {3,S}
9  H 0 0 {3,S}
10 H 0 0 {4,S}
11 H 0 0 {4,S}
12 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.824,26.078,30.855,34.962,41.526,46.493,54.356],'cal/(mol*K)'),
        H298 = (-0.014,'kcal/mol'),
        S298 = (73.182,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 210,
    label = "butene2c",
    molecule = 
"""
1  C 0 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 0 {1,S} {3,D} {8,S}
3  C 0 0 {2,D} {4,S} {9,S}
4  C 0 0 {3,S} {10,S} {11,S} {12,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {3,S}
10 H 0 0 {4,S}
11 H 0 0 {4,S}
12 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.325,25.281,30.029,34.222,41.021,46.172,54.247],'cal/(mol*K)'),
        H298 = (-1.534,'kcal/mol'),
        S298 = (73.277,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 211,
    label = "butene2t",
    molecule = 
"""
1  C 0 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 0 {1,S} {3,D} {8,S}
3  C 0 0 {2,D} {4,S} {9,S}
4  C 0 0 {3,S} {10,S} {11,S} {12,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {3,S}
10 H 0 0 {4,S}
11 H 0 0 {4,S}
12 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([21.142,25.958,30.537,34.592,41.204,46.25,54.235],'cal/(mol*K)'),
        H298 = (-2.738,'kcal/mol'),
        S298 = (70.677,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 212,
    label = "isobutene",
    molecule = 
"""
1  C 0 0 {2,D} {5,S} {6,S}
2  C 0 0 {1,D} {3,S} {4,S}
3  C 0 0 {2,S} {7,S} {8,S} {9,S}
4  C 0 0 {2,S} {10,S} {11,S} {12,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {3,S}
8  H 0 0 {3,S}
9  H 0 0 {3,S}
10 H 0 0 {4,S}
11 H 0 0 {4,S}
12 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([21.121,26.147,30.767,34.802,41.347,46.344,54.274],'cal/(mol*K)'),
        H298 = (-4.119,'kcal/mol'),
        S298 = (70.164,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 213,
    label = "butyl_1",
    molecule = 
"""
1  C 1 0 {2,S} {5,S} {6,S}
2  C 0 0 {1,S} {3,S} {7,S} {8,S}
3  C 0 0 {2,S} {4,S} {9,S} {10,S}
4  C 0 0 {3,S} {11,S} {12,S} {13,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {2,S}
8  H 0 0 {2,S}
9  H 0 0 {3,S}
10 H 0 0 {3,S}
11 H 0 0 {4,S}
12 H 0 0 {4,S}
13 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.005,28.544,33.594,37.935,44.885,50.167,58.559],'cal/(mol*K)'),
        H298 = (19.318,'kcal/mol'),
        S298 = (78.54,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 214,
    label = "butyl_2",
    molecule = 
"""
1  C 0 0 {2,S} {5,S} {6,S} {7,S}
2  C 1 0 {1,S} {3,S} {8,S}
3  C 0 0 {2,S} {4,S} {9,S} {10,S}
4  C 0 0 {3,S} {11,S} {12,S} {13,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {3,S}
10 H 0 0 {3,S}
11 H 0 0 {4,S}
12 H 0 0 {4,S}
13 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([21.878,27.229,32.315,36.787,44.042,49.565,58.276],'cal/(mol*K)'),
        H298 = (16.616,'kcal/mol'),
        S298 = (79.048,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 215,
    label = "ibutyl",
    molecule = 
"""
1  C 1 0 {2,S} {5,S} {6,S}
2  C 0 0 {1,S} {3,S} {4,S} {7,S}
3  C 0 0 {2,S} {8,S} {9,S} {10,S}
4  C 0 0 {2,S} {11,S} {12,S} {13,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {2,S}
8  H 0 0 {3,S}
9  H 0 0 {3,S}
10 H 0 0 {3,S}
11 H 0 0 {4,S}
12 H 0 0 {4,S}
13 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.139,28.925,34.009,38.302,45.116,50.296,58.581],'cal/(mol*K)'),
        H298 = (17.766,'kcal/mol'),
        S298 = (76.44,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 216,
    label = "tbutyl",
    molecule = 
"""
1  C 0 0 {2,S} {5,S} {6,S} {7,S}
2  C 1 0 {1,S} {3,S} {4,S}
3  C 0 0 {2,S} {8,S} {9,S} {10,S}
4  C 0 0 {2,S} {11,S} {12,S} {13,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {3,S}
9  H 0 0 {3,S}
10 H 0 0 {3,S}
11 H 0 0 {4,S}
12 H 0 0 {4,S}
13 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([21.711,26.638,31.617,36.121,43.546,49.221,58.128],'cal/(mol*K)'),
        H298 = (12.98,'kcal/mol'),
        S298 = (76.215,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 217,
    label = "nbutane",
    molecule = 
"""
1  C 0 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 0 {2,S} {4,S} {10,S} {11,S}
4  C 0 0 {3,S} {12,S} {13,S} {14,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {2,S}
10 H 0 0 {3,S}
11 H 0 0 {3,S}
12 H 0 0 {4,S}
13 H 0 0 {4,S}
14 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.971,29.745,35.176,39.946,47.715,53.665,63.113],'cal/(mol*K)'),
        H298 = (-30.036,'kcal/mol'),
        S298 = (73.694,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 218,
    label = "ibutane",
    molecule = 
"""
1  C 0 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 0 {1,S} {3,S} {4,S} {8,S}
3  C 0 0 {2,S} {9,S} {10,S} {11,S}
4  C 0 0 {2,S} {12,S} {13,S} {14,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {3,S}
10 H 0 0 {3,S}
11 H 0 0 {3,S}
12 H 0 0 {4,S}
13 H 0 0 {4,S}
14 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.899,30.207,35.819,40.565,48.083,53.802,63.009],'cal/(mol*K)'),
        H298 = (-32.025,'kcal/mol'),
        S298 = (71.156,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

