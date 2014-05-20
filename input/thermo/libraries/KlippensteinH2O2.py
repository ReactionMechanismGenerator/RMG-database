#!/usr/bin/env python
# encoding: utf-8

name = "KlippensteinH2O2"
shortDesc = u""
longDesc = u"""

"""
entry(
    index        = 1,
    label        = "H",
    multiplicity = 2,
    molecule = 
"""
1 H U1 L0 E0 
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.97,4.97,4.97,4.97,4.97,4.97,4.97],'cal/(mol*K)'),
        H298 = (52.1,'kcal/mol'),
        S298 = (27.4,'cal/(mol*K)'),
    ),
    shortDesc = u"""Neither TRange included 298K!""",
    longDesc = 
u"""

""",
)

entry(
    index        = 2,
    label        = "H2",
    multiplicity = 1,
    molecule = 
"""
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.9,6.96,7,7.02,7.07,7.21,7.73],'cal/(mol*K)'),
        H298 = (-0.00045,'kcal/mol'),
        S298 = (31.2,'cal/(mol*K)'),
    ),
    shortDesc = u"""Neither TRange included 298K!""",
    longDesc = 
u"""

""",
)

entry(
    index        = 3,
    label        = "O_(T)",
    multiplicity = 3,
    molecule = 
"""
1 O U2 L2 E0 
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.23,5.14,5.08,5.05,5.02,5,4.98],'cal/(mol*K)'),
        H298 = (59.6,'kcal/mol'),
        S298 = (38.5,'cal/(mol*K)'),
    ),
    shortDesc = u"""Neither TRange included 298K!""",
    longDesc = 
u"""

""",
)

entry(
    index        = 4,
    label        = "OH",
    multiplicity = 2,
    molecule = 
"""
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.16,7.08,7.05,7.06,7.15,7.33,7.87],'cal/(mol*K)'),
        H298 = (8.9,'kcal/mol'),
        S298 = (43.9,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 5,
    label        = "H2O",
    multiplicity = 1,
    molecule = 
"""
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8,8.23,8.44,8.67,9.22,9.87,11.3],'cal/(mol*K)'),
        H298 = (-57.8,'kcal/mol'),
        S298 = (45.1,'cal/(mol*K)'),
    ),
    shortDesc = u"""Neither TRange included 298K!""",
    longDesc = 
u"""

""",
)

entry(
    index        = 6,
    label        = "O2_(T)",
    multiplicity = 3,
    molecule = 
"""
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.01,7.22,7.44,7.65,8.07,8.35,8.72],'cal/(mol*K)'),
        H298 = (-0.00125,'kcal/mol'),
        S298 = (49,'cal/(mol*K)'),
    ),
    shortDesc = u"""Neither TRange included 298K!""",
    longDesc = 
u"""

""",
)

entry(
    index        = 7,
    label        = "HO2",
    multiplicity = 2,
    molecule = 
"""
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.35,8.89,9.46,9.99,10.8,11.4,12.5],'cal/(mol*K)'),
        H298 = (3,'kcal/mol'),
        S298 = (54.7,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 8,
    label        = "H2O2",
    multiplicity = 1,
    molecule = 
"""
1 O U0 L2 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.4,11.4,12.3,13.1,14.3,15.2,16.8],'cal/(mol*K)'),
        H298 = (-32.5,'kcal/mol'),
        S298 = (55.6,'cal/(mol*K)'),
    ),
    shortDesc = u"""Neither TRange included 298K!""",
    longDesc = 
u"""

""",
)

entry(
    index        = 9,
    label        = "CO",
    multiplicity = 1,
    molecule = 
"""
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.95,7.03,7.14,7.27,7.61,7.95,8.41],'cal/(mol*K)'),
        H298 = (-26.4,'kcal/mol'),
        S298 = (47.2,'cal/(mol*K)'),
    ),
    shortDesc = u"""Neither TRange included 298K!""",
    longDesc = 
u"""

""",
)

entry(
    index        = 10,
    label        = "CO2",
    multiplicity = 1,
    molecule = 
"""
1 C U0 L0 E0  {2,D} {3,D}
2 O U0 L2 E0  {1,D}
3 O U0 L2 E0  {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.91,9.86,10.7,11.3,12.3,13,13.9],'cal/(mol*K)'),
        H298 = (-94.1,'kcal/mol'),
        S298 = (51.1,'cal/(mol*K)'),
    ),
    shortDesc = u"""Neither TRange included 298K!""",
    longDesc = 
u"""

""",
)

