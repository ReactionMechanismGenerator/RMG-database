#!/usr/bin/env python
# encoding: utf-8

name = "Functional Group Additivity Values"
shortDesc = u""
longDesc = u"""

"""
entry(
    index        = -1,
    label        = "R",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * R U0
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1,
    label        = "C",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U0
""",
    thermo = u'Cs-CsCsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 2,
    label        = "Cbf",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cbf U0
""",
    thermo = u'Cbf-CbCbCbf',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 3,
    label        = "Cbf-CbCbCbf",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cbf U0 {2,B} {3,B} {4,B}
2   Cb  U0 {1,B}
3   Cb  U0 {1,B}
4   Cbf U0 {1,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.01,3.68,4.2,4.61,5.2,5.7,6.2],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (4.8,'kcal/mol','+|-',0.17),
        S298 = (-5,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cbf-CbfCbCb STEIN and FAHR; J. PHYS. CHEM. 1985, 89, 17, 3714""",
    longDesc = 
u"""

""",
)

entry(
    index        = 4,
    label        = "Cbf-CbCbfCbf",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cbf U0 {2,B} {3,B} {4,B}
2   Cb  U0 {1,B}
3   Cbf U0 {1,B}
4   Cbf U0 {1,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.01,3.68,4.2,4.61,5.2,5.7,6.2],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (3.7,'kcal/mol','+|-',0.3),
        S298 = (-5,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cbf-CbfCbfCb STEIN and FAHR; J. PHYS. CHEM. 1985, 89, 17, 3714""",
    longDesc = 
u"""

""",
)

entry(
    index        = 5,
    label        = "Cbf-CbfCbfCbf",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cbf U0 {2,B} {3,B} {4,B}
2   Cbf U0 {1,B}
3   Cbf U0 {1,B}
4   Cbf U0 {1,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2,3.11,3.9,4.42,5,5.3,5.7],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (1.5,'kcal/mol','+|-',0.3),
        S298 = (1.8,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cbf-CbfCbfCbf STEIN and FAHR; J. PHYS. CHEM. 1985, 89, 17, 3714""",
    longDesc = 
u"""

""",
)

entry(
    index        = 6,
    label        = "Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cb U0
""",
    thermo = u'Cb-Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 7,
    label        = "Cb-H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cb U0 {2,S}
2   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.24,4.44,5.46,6.3,7.54,8.41,9.73],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (3.3,'kcal/mol','+|-',0.11),
        S298 = (11.53,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = u"""Cb-H BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index        = 8,
    label        = "Cb-Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cb U0 {2,S}
2   Os U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.9,5.3,6.2,6.6,6.9,6.9,7.07],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-0.9,'kcal/mol','+|-',0.16),
        S298 = (-10.2,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cb-O BENSON Cp1500=3D Cp1000*(Cp1500/Cp1000: Cb/Cd)""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1197,
    label        = "Cb-Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cb U0 {2,S}
2   Ss U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.46,3.24,3.92,4.49,5.27,5.75,6.3],'cal/(mol*K)'),
        H298 = (5.83,'kcal/mol'),
        S298 = (-7.94,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 9,
    label        = "Cb-C",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cb U0 {2,S}
2   C  U0 {1,S}
""",
    thermo = u'Cb-Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 10,
    label        = "Cb-Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cb U0 {2,S}
2   Cs U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.67,3.14,3.68,4.15,4.96,5.44,5.98],'cal/(mol*K)','+|-',[0.07,0.07,0.07,0.07,0.07,0.07,0.07]),
        H298 = (5.51,'kcal/mol','+|-',0.13),
        S298 = (-7.69,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cb-Cs BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index        = 11,
    label        = "Cb-Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cb      U0 {2,S}
2   {Cd,CO} U0 {1,S}
""",
    thermo = u'Cb-(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 12,
    label        = "Cb-(Cds-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cb U0 {2,S}
2   CO U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.59,3.97,4.38,4.72,5.28,5.61,5.75],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (3.69,'kcal/mol','+|-',0.2),
        S298 = (-7.8,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Enthalpy from Cb-CO, entropies and heat capacities assigned value of Cb-Cd""",
    longDesc = 
u"""

""",
)

entry(
    index        = 13,
    label        = "Cb-(Cds-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cb U0 {2,S}
2   Cd U0 {1,S}
""",
    thermo = u'Cb-(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 14,
    label        = "Cb-(Cds-Cds)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cb U0 {2,S}
2   Cd U0 {1,S} {3,D}
3   Cd U0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.59,3.97,4.38,4.72,5.28,5.61,5.75],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (5.69,'kcal/mol','+|-',0.2),
        S298 = (-7.8,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cb-Cd STEIN and FAHR; J. PHYS. CHEM. 1985, 89, 17, 3714""",
    longDesc = 
u"""

""",
)

entry(
    index        = 15,
    label        = "Cb-(Cds-Cdd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cb  U0 {2,S}
2   Cd  U0 {1,S} {3,D}
3   Cdd U0 {2,D}
""",
    thermo = u'Cb-(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 16,
    label        = "Cb-(Cds-Cdd-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cb  U0 {2,S}
2   Cd  U0 {1,S} {3,D}
3   Cdd U0 {2,D} {4,D}
4   Od  U0 {3,D}
""",
    thermo = u'Cb-(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cb-(Cds-Cdd-Sd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cb  U0 {2,S}
2   Cd  U0 {1,S} {3,D}
3   Cdd U0 {2,D} {4,D}
4   Sd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 17,
    label        = "Cb-(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cb  U0 {2,S}
2   Cd  U0 {1,S} {3,D}
3   Cdd U0 {2,D} {4,D}
4   C   U0 {3,D}
""",
    thermo = u'Cb-(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1198,
    label        = "Cb-C=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cb U0 {2,S}
2   Cd U0 {1,S} {3,D}
3   Sd U0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.46,3.24,3.92,4.49,5.27,5.75,6.3],'cal/(mol*K)'),
        H298 = (5.83,'kcal/mol'),
        S298 = (-7.94,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 18,
    label        = "Cb-Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cb U0 {2,S}
2   Ct U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.59,3.97,4.38,4.72,5.28,5.61,5.75],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (5.69,'kcal/mol','+|-',0.3),
        S298 = (-7.8,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cb-Ct STEIN and FAHR; J. PHYS. CHEM. 1985, 89, 17, 3714""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1839,
    label        = "Cb-(CtN3t)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cb  U0 {2,S}
2   Ct  U0 {1,S} {3,T}
3   N3t U0 {2,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.8,11.2,12.3,13.1,14.2,14.9,16.65],'cal/(mol*K)'),
        H298 = (35.8,'kcal/mol'),
        S298 = (20.5,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 19,
    label        = "Cb-Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cb U0 {2,S}
2   Cb U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.33,4.22,4.89,5.27,5.76,5.95,6.05],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (4.96,'kcal/mol','+|-',0.3),
        S298 = (-8.64,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cb-Cb BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1821,
    label        = "Cb-CbCbN3s",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cb  U0 {2,B} {3,B} {4,S}
2   Cb  U0 {1,B}
3   Cb  U0 {1,B}
4   N3s U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.95,5.21,5.94,6.32,6.53,6.56,6.635],'cal/(mol*K)'),
        H298 = (-0.5,'kcal/mol'),
        S298 = (-9.69,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 20,
    label        = "Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ct U0
""",
    thermo = u'Ct-CtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1849,
    label        = "Ct-CtN3s",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ct  U0 {2,T} {3,S}
2   Ct  U0 {1,T}
3   N3s U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1853,
    label        = "Ct-N3tN3s",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ct  U0 {2,T} {3,S}
2   N3t U0 {1,T}
3   N3s U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 21,
    label        = "Ct-CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ct U0 {2,T} {3,S}
2   Ct U0 {1,T}
3   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.28,5.99,6.49,6.87,7.47,7.96,8.85],'cal/(mol*K)','+|-',[0.07,0.07,0.07,0.07,0.07,0.07,0.07]),
        H298 = (26.93,'kcal/mol','+|-',0.05),
        S298 = (24.7,'cal/(mol*K)','+|-',0.07),
    ),
    shortDesc = u"""Ct-H STEIN and FAHR; J. PHYS. CHEM. 1985, 89, 17, 3714""",
    longDesc = 
u"""

""",
)

entry(
    index        = 22,
    label        = "Ct-CtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ct U0 {2,T} {3,S}
2   Ct U0 {1,T}
3   Os U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.64,4.39,4.85,5.63,5.66,5.73,5.73],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (31.4,'kcal/mol','+|-',0.27),
        S298 = (4.91,'cal/(mol*K)','+|-',0.09),
    ),
    shortDesc = u"""Ct-O MELIUS / hc#coh !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1852,
    label        = "Ct-N3tOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ct  U0 {2,T} {3,S}
2   N3t U0 {1,T}
3   Os  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1195,
    label        = "Ct-CtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ct U0 {2,T} {3,S}
2   Ct U0 {1,T}
3   Ss U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.29,3.67,4,4.29,4.74,5.05,5.49],'cal/(mol*K)'),
        H298 = (27.63,'kcal/mol'),
        S298 = (6.32,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1942,
    label        = "Ct-N3tC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ct  U0 {2,T} {3,S}
2   N3t U0 {1,T}
3   C   U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1850,
    label        = "Ct-N3tCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ct  U0 {2,T} {3,S}
2   N3t U0 {1,T}
3   Cs  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1851,
    label        = "Ct-N3tCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ct  U0 {2,T} {3,S}
2   N3t U0 {1,T}
3   Cd  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 23,
    label        = "Ct-CtC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ct U0 {2,T} {3,S}
2   Ct U0 {1,T}
3   C  U0 {1,S}
""",
    thermo = u'Ct-CtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 24,
    label        = "Ct-CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ct U0 {2,T} {3,S}
2   Ct U0 {1,T}
3   Cs U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.13,3.48,3.81,4.09,4.6,4.92,6.35],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (27.55,'kcal/mol','+|-',0.27),
        S298 = (6.35,'cal/(mol*K)','+|-',0.09),
    ),
    shortDesc = u"""Ct-Cs STEIN and FAHR; J. PHYS. CHEM. 1985, 89, 17, 3714""",
    longDesc = 
u"""

""",
)

entry(
    index        = 25,
    label        = "Ct-CtCds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ct      U0 {2,T} {3,S}
2   Ct      U0 {1,T}
3   {Cd,CO} U0 {1,S}
""",
    thermo = u'Ct-Ct(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 26,
    label        = "Ct-Ct(Cds-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ct U0 {2,T} {3,S}
2   Ct U0 {1,T}
3   CO U0 {1,S}
""",
    thermo = u'Ct-CtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 27,
    label        = "Ct-Ct(Cds-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ct U0 {2,T} {3,S}
2   Ct U0 {1,T}
3   Cd U0 {1,S}
""",
    thermo = u'Ct-Ct(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 28,
    label        = "Ct-Ct(Cds-Cds)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ct U0 {2,T} {3,S}
2   Ct U0 {1,T}
3   Cd U0 {1,S} {4,D}
4   Cd U0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.57,3.54,3.5,4.92,5.34,5.5,5.8],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (28.2,'kcal/mol','+|-',0.27),
        S298 = (6.43,'cal/(mol*K)','+|-',0.09),
    ),
    shortDesc = u"""Ct-Cd STEIN and FAHR; J. PHYS. CHEM. 1985, 89, 17, 3714""",
    longDesc = 
u"""

""",
)

entry(
    index        = 29,
    label        = "Ct-Ct(Cds-Cdd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ct  U0 {2,T} {3,S}
2   Ct  U0 {1,T}
3   Cd  U0 {1,S} {4,D}
4   Cdd U0 {3,D}
""",
    thermo = u'Ct-Ct(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 30,
    label        = "Ct-Ct(Cds-Cdd-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ct  U0 {2,T} {3,S}
2 * Ct  U0 {1,T}
3   Cd  U0 {1,S} {4,D}
4   Cdd U0 {3,D} {5,D}
5   Od  U0 {4,D}
""",
    thermo = u'Ct-Ct(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Ct-Ct(Cds-Cdd-Sd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ct  U0 {2,T} {3,S}
2   Ct  U0 {1,T}
3   Cd  U0 {1,S} {4,D}
4   Cdd U0 {3,D} {5,D}
5   Sd  U0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 31,
    label        = "Ct-Ct(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ct  U0 {2,T} {3,S}
2   Ct  U0 {1,T}
3   Cd  U0 {1,S} {4,D}
4   Cdd U0 {3,D} {5,D}
5   C   U0 {4,D}
""",
    thermo = u'Ct-Ct(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1196,
    label        = "Ct-CtC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ct U0 {2,T} {3,S}
2   Ct U0 {1,T}
3   Cd U0 {1,S} {4,D}
4   Sd U0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.29,3.67,4,4.29,4.74,5.05,5.49],'cal/(mol*K)'),
        H298 = (27.63,'kcal/mol'),
        S298 = (6.32,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 32,
    label        = "Ct-CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ct U0 {2,T} {3,S}
2   Ct U0 {1,T}
3   Ct U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.54,4.06,4.4,4.64,5,5.23,5.57],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (25.6,'kcal/mol','+|-',0.27),
        S298 = (5.88,'cal/(mol*K)','+|-',0.09),
    ),
    shortDesc = u"""Ct-Ct STEIN and FAHR; J. PHYS. CHEM. 1985, 89, 17, 3714""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1840,
    label        = "Ct-Ct(CtN3t)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ct  U0 {2,T} {3,S}
2   Ct  U0 {1,T}
3   Ct  U0 {1,S} {4,T}
4   N3t U0 {3,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.3,11.3,12.1,12.7,13.6,14.3,15.3],'cal/(mol*K)'),
        H298 = (63.8,'kcal/mol'),
        S298 = (35.4,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 33,
    label        = "Ct-CtCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ct U0 {2,T} {3,S}
2   Ct U0 {1,T}
3   Cb U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.57,3.54,4.5,4.92,5.34,5.5,5.8],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (24.67,'kcal/mol','+|-',0.27),
        S298 = (6.43,'cal/(mol*K)','+|-',0.09),
    ),
    shortDesc = u"""Ct-Cb STEIN and FAHR; J. PHYS. CHEM. 1985, 89, 17, 3714""",
    longDesc = 
u"""

""",
)

entry(
    index        = 34,
    label        = "Cdd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cdd U0
""",
    thermo = u'Cdd-CdsCds',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1854,
    label        = "Cdd-N3dCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cdd U0 {2,D} {3,D}
2   N3d U0 {1,D}
3   Cd  U0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.5,5.1,5.6,6,6.5,6.9,7.4],'cal/(mol*K)','+|-',[1.1,1.1,1.1,1.1,1.1,1.1,1.1]),
        H298 = (25.9,'kcal/mol','+|-',1.5),
        S298 = (19.7,'cal/(mol*K)','+|-',1.4),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 35,
    label        = "Cdd-OdOd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cdd U0 {2,D} {3,D}
2   Od  U0 {1,D}
3   Od  U0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.91,9.86,10.65,11.31,12.32,12.99,13.93],'cal/(mol*K)'),
        H298 = (-94.05,'kcal/mol','+|-',0.03),
        S298 = (52.46,'cal/(mol*K)','+|-',0.002),
    ),
    shortDesc = u"""CHEMKIN DATABASE: S(group) = S(CO2) + Rln(2)""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1199,
    label        = "Cdd-SdSd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cdd U0 {2,D} {3,D}
2   Sd  U0 {1,D}
3   Sd  U0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.91,11.83,12.49,12.98,13.63,14.01,14.47],'cal/(mol*K)'),
        H298 = (24.5,'kcal/mol'),
        S298 = (58.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
u"""

""",
)

entry(
    index        = 36,
    label        = "Cdd-CdOd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cdd U0 {2,D} {3,D}
2   C   U0 {1,D}
3   Od  U0 {1,D}
""",
    thermo = u'Cdd-CdsOd',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 37,
    label        = "Cdd-CdsOd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cdd U0 {2,D} {3,D}
2   Cd  U0 {1,D}
3   Od  U0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""O=C*=C< currently treat the adjacent C as Ck""",
    longDesc = 
u"""

""",
)

entry(
    index        = 38,
    label        = "Cdd-CddOd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cdd U0 {2,D} {3,D}
2   Cdd U0 {1,D}
3   Od  U0 {1,D}
""",
    thermo = u'Cdd-(Cdd-Cd)Od',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 40,
    label        = "Cdd-(Cdd-Od)Od",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cdd U0 {2,D} {3,D}
2   Cdd U0 {1,D} {4,D}
3   Od  U0 {1,D}
4   Od  U0 {2,D}
""",
    thermo = u'Cdd-CdsOd',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 39,
    label        = "Cdd-(Cdd-Cd)Od",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cdd U0 {2,D} {3,D}
2   Cdd U0 {1,D} {4,D}
3   Od  U0 {1,D}
4   C   U0 {2,D}
""",
    thermo = u'Cdd-CdsOd',
    shortDesc = u"""O=C*=C= currently not defined. Assigned same value as Ca""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1200,
    label        = "Cdd-CdSd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cdd U0 {2,D} {3,D}
2   C   U0 {1,D}
3   Sd  U0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.88,8.48,8.8,8.99,9.23,9.37,9.58],'cal/(mol*K)'),
        H298 = (40.33,'kcal/mol'),
        S298 = (34.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cdd-CdsSd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cdd U0 {2,D} {3,D}
2   Cd  U0 {1,D}
3   Sd  U0 {1,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cdd-CddSd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cdd U0 {2,D} {3,D}
2   Cdd U0 {1,D}
3   Sd  U0 {1,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cdd-(Cdd-Sd)Sd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cdd U0 {2,D} {3,D}
2   Cdd U0 {1,D} {4,D}
3   Sd  U0 {1,D}
4   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cdd-(Cdd-Cd)Sd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cdd U0 {2,D} {3,D}
2   Cdd U0 {1,D} {4,D}
3   Sd  U0 {1,D}
4   C   U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 41,
    label        = "Cdd-CdCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cdd U0 {2,D} {3,D}
2   C   U0 {1,D}
3   C   U0 {1,D}
""",
    thermo = u'Cdd-CdsCds',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 42,
    label        = "Cdd-CddCdd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cdd U0 {2,D} {3,D}
2   Cdd U0 {1,D}
3   Cdd U0 {1,D}
""",
    thermo = u'Cdd-(Cdd-Cd)(Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 43,
    label        = "Cdd-(Cdd-Od)(Cdd-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cdd U0 {2,D} {3,D}
2   Cdd U0 {1,D} {4,D}
3   Cdd U0 {1,D} {5,D}
4   Od  U0 {2,D}
5   Od  U0 {3,D}
""",
    thermo = u'Cdd-CdsCds',
    shortDesc = u"""O=C=C*=C=O, currently not defined. Assigned same value as Ca""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cdd-(Cdd-Sd)(Cdd-Sd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cdd U0 {2,D} {3,D}
2   Cdd U0 {1,D} {4,D}
3   Cdd U0 {1,D} {5,D}
4   Sd  U0 {2,D}
5   Sd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 44,
    label        = "Cdd-(Cdd-Od)(Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cdd U0 {2,D} {3,D}
2   Cdd U0 {1,D} {4,D}
3   Cdd U0 {1,D} {5,D}
4   Od  U0 {2,D}
5   C   U0 {3,D}
""",
    thermo = u'Cdd-(Cdd-Od)Cds',
    shortDesc = u"""O=C=C*=C=C, currently not defined. Assigned same value as Ca""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cdd-(Cdd-Sd)(Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cdd U0 {2,D} {3,D}
2   Cdd U0 {1,D} {4,D}
3   Cdd U0 {1,D} {5,D}
4   Sd  U0 {2,D}
5   C   U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 45,
    label        = "Cdd-(Cdd-Cd)(Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cdd U0 {2,D} {3,D}
2   Cdd U0 {1,D} {4,D}
3   Cdd U0 {1,D} {5,D}
4   C   U0 {2,D}
5   C   U0 {3,D}
""",
    thermo = u'Cdd-CdsCds',
    shortDesc = u"""C=C=C*=C=C, currently not defined. Assigned same value as Ca""",
    longDesc = 
u"""

""",
)

entry(
    index        = 46,
    label        = "Cdd-CddCds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cdd U0 {2,D} {3,D}
2   Cdd U0 {1,D}
3   Cd  U0 {1,D}
""",
    thermo = u'Cdd-(Cdd-Cd)(Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 47,
    label        = "Cdd-(Cdd-Od)Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cdd U0 {2,D} {3,D}
2   Cdd U0 {1,D} {4,D}
3   Cd  U0 {1,D}
4   Od  U0 {2,D}
""",
    thermo = u'Cdd-CdsCds',
    shortDesc = u"""O=C=C*=C<, currently not defined. Assigned same value as Ca """,
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cdd-(Cdd-Sd)Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cdd U0 {2,D} {3,D}
2   Cdd U0 {1,D} {4,D}
3   Cd  U0 {1,D}
4   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 48,
    label        = "Cdd-(Cdd-Cd)Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cdd U0 {2,D} {3,D}
2   Cdd U0 {1,D} {4,D}
3   Cd  U0 {1,D}
4   C   U0 {2,D}
""",
    thermo = u'Cdd-CdsCds',
    shortDesc = u"""C=C=C*=C<, currently not defined. Assigned same value as Ca """,
    longDesc = 
u"""

""",
)

entry(
    index        = 49,
    label        = "Cdd-CdsCds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cdd U0 {2,D} {3,D}
2   Cd  U0 {1,D}
3   Cd  U0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.9,4.4,4.7,5,5.3,5.5,5.7],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (34.2,'kcal/mol','+|-',0.2),
        S298 = (6,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Benson's Ca """,
    longDesc = 
u"""

""",
)

entry(
    index        = 50,
    label        = "Cds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * {Cd,CO} U0
""",
    thermo = u'Cds-CdsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1823,
    label        = "Cds-OdN3sH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * {Cd,CO} U0 {2,D} {3,S} {4,S}
2   Od      U0 {1,D}
3   N3s     U0 {1,S}
4   H       U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.03,7.87,8.82,9.68,11.16,12.2,14.8],'cal/(mol*K)'),
        H298 = (-29.6,'kcal/mol'),
        S298 = (34.93,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1824,
    label        = "Cds-OdN3sCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * {Cd,CO} U0 {2,D} {3,S} {4,S}
2   Od      U0 {1,D}
3   N3s     U0 {1,S}
4   Cs      U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.37,6.17,7.07,7.66,9.62,11.19,15.115],'cal/(mol*K)'),
        H298 = (-32.8,'kcal/mol'),
        S298 = (16.2,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1855,
    label        = "Cd-N3dCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cd  U0 {2,D} {3,S} {4,S}
2   N3d U0 {1,D}
3   Cs  U0 {1,S}
4   Cs  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.5,4.2,5,5.6,6.6,7.2,7.9],'cal/(mol*K)','+|-',[0.9,0.9,0.9,0.9,0.9,0.9,0.9]),
        H298 = (5.7,'kcal/mol','+|-',1.2),
        S298 = (2,'cal/(mol*K)','+|-',1.1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1856,
    label        = "Cd-N3dCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cd  U0 {2,D} {3,S} {4,S}
2   N3d U0 {1,D}
3   Cs  U0 {1,S}
4   H   U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.5,6.3,7.2,8,9.3,10.2,11.6],'cal/(mol*K)','+|-',[0.9,0.9,0.9,0.9,0.9,0.9,0.9]),
        H298 = (3.3,'kcal/mol','+|-',1.3),
        S298 = (21.2,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1857,
    label        = "Cd-N3dHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cd  U0 {2,D} {3,S} {4,S}
2   N3d U0 {1,D}
3   H   U0 {1,S}
4   H   U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.2,7.4,8.7,9.8,11.5,12.9,15],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (4.4,'kcal/mol','+|-',1.4),
        S298 = (40.8,'cal/(mol*K)','+|-',1.3),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 51,
    label        = "Cds-OdHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Od U0 {1,D}
3   H  U0 {1,S}
4   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.47,9.38,10.46,11.52,13.37,14.81,14.81],'cal/(mol*K)','+|-',[0.06,0.06,0.06,0.06,0.06,0.06,0.06]),
        H298 = (-25.95,'kcal/mol','+|-',0.11),
        S298 = (53.68,'cal/(mol*K)','+|-',0.06),
    ),
    shortDesc = u"""CO-HH BENSON !!!WARNING! Cp1500 value taken as Cp1000, S(group) = S(CH2O) + Rln(2)""",
    longDesc = 
u"""

""",
)

entry(
    index        = 52,
    label        = "Cds-OdOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Od U0 {1,D}
3   Os U0 {1,S}
4   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.03,7.87,8.82,9.68,11.2,12.2,12.2],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (-32.1,'kcal/mol','+|-',0.3),
        S298 = (34.9,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""CO-OH BENSON !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1453,
    label        = "CO-SsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Od U0 {1,D}
3   Ss U0 {1,S}
4   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.26,4.48,4.61,4.7,4.89,4.95,4.98],'cal/(mol*K)'),
        H298 = (-1.13,'kcal/mol'),
        S298 = (26.69,'cal/(mol*K)'),
    ),
    shortDesc = u"""CAC 1d-HR calc""",
    longDesc = 
u"""

""",
)

entry(
    index        = 53,
    label        = "Cds-OdOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Od U0 {1,D}
3   Os U0 {1,S}
4   Os U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.97,6.7,7.4,8.02,8.87,9.36,9.36],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (-31.45,'kcal/mol','+|-',0.3),
        S298 = (10.78,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""CO-OO BOZZELLI 8/91, S CO/C/O, Hf PEDLEY ccoc*oocc Bsn Hf-24 !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1454,
    label        = "CO-CsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Od U0 {1,D}
3   Ss U0 {1,S}
4   Cs U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.82,6.45,7,7.45,8.05,8.43,8.84],'cal/(mol*K)'),
        H298 = (-9.43,'kcal/mol'),
        S298 = (18.05,'cal/(mol*K)'),
    ),
    shortDesc = u"""CAC 1d-HR calc""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1183,
    label        = "C=S-HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Sd U0 {1,D}
3   H  U0 {1,S}
4   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.08,10.34,11.51,12.5,14.07,15.25,17.14],'cal/(mol*K)'),
        H298 = (27.71,'kcal/mol'),
        S298 = (56.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1189,
    label        = "C=S-SsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Sd U0 {1,D}
3   Ss U0 {1,S}
4   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.38,9.78,10.83,11.66,12.86,13.71,14.87],'cal/(mol*K)'),
        H298 = (21.55,'kcal/mol'),
        S298 = (34.41,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1455,
    label        = "CS-OsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Sd U0 {1,D}
3   Os U0 {1,S}
4   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.6,5.45,6.2,6.84,7.78,8.44,9.34],'cal/(mol*K)'),
        H298 = (-7.85,'kcal/mol'),
        S298 = (27.65,'cal/(mol*K)'),
    ),
    shortDesc = u"""CAC 1d-HR calc""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-SsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Sd U0 {1,D}
3   Ss U0 {1,S}
4   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 54,
    label        = "Cds-OdCH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Od U0 {1,D}
3   C  U0 {1,S}
4   H  U0 {1,S}
""",
    thermo = u'Cds-OdCsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 55,
    label        = "Cds-OdCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Od U0 {1,D}
3   Cs U0 {1,S}
4   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.03,7.87,8.82,9.68,11.2,12.2,12.2],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (-29.1,'kcal/mol','+|-',0.3),
        S298 = (34.9,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""CO-CsH BENSON !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index        = 56,
    label        = "Cds-OdCdsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C       U0 {2,D} {3,S} {4,S}
2   Od      U0 {1,D}
3   {Cd,CO} U0 {1,S}
4   H       U0 {1,S}
""",
    thermo = u'Cds-Od(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 57,
    label        = "Cds-Od(Cds-Od)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Od U0 {1,D}
3   CO U0 {1,S}
4   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.45,8.77,9.82,10.7,12.14,12.9,12.9],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (-25.3,'kcal/mol','+|-',0.3),
        S298 = (33.4,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""CO-COH Hf BENSON S,Cp =3D CO/Cs/H-del(Cd/Cd/H-Cd/Cs/H) !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index        = 58,
    label        = "Cds-Od(Cds-Cd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Od U0 {1,D}
3   Cd U0 {1,S}
4   H  U0 {1,S}
""",
    thermo = u'Cds-Od(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 59,
    label        = "Cds-Od(Cds-Cds)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Od U0 {1,D}
3   Cd U0 {1,S} {5,D}
4   H  U0 {1,S}
5   Cd U0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.45,8.77,9.82,10.7,12.14,12.9,12.9],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (-30.9,'kcal/mol','+|-',0.3),
        S298 = (33.4,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""CO-CdH Hf BOZZELLI S,Cp =3D CO/C/H-del(cd syst) !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index        = 60,
    label        = "Cds-Od(Cds-Cdd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Od  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   H   U0 {1,S}
5   Cdd U0 {3,D}
""",
    thermo = u'Cds-Od(Cds-Cdd-Cd)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 61,
    label        = "Cds-Od(Cds-Cdd-Od)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Od  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   H   U0 {1,S}
5   Cdd U0 {3,D} {6,D}
6   Od  U0 {5,D}
""",
    thermo = u'Cds-Od(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 62,
    label        = "Cds-Od(Cds-Cdd-Cd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Od  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   H   U0 {1,S}
5   Cdd U0 {3,D} {6,D}
6   C   U0 {5,D}
""",
    thermo = u'Cds-Od(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 63,
    label        = "Cds-OdCtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Od U0 {1,D}
3   Ct U0 {1,S}
4   H  U0 {1,S}
""",
    thermo = u'Cds-Od(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 64,
    label        = "Cds-OdCbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Od U0 {1,D}
3   Cb U0 {1,S}
4   H  U0 {1,S}
""",
    thermo = u'Cds-Od(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-CH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Sd U0 {1,D}
3   C  U0 {1,S}
4   H  U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1184,
    label        = "C=S-CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Sd U0 {1,D}
3   Cs U0 {1,S}
4   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.11,9.03,9.88,10.61,11.74,12.55,13.82],'cal/(mol*K)'),
        H298 = (27.32,'kcal/mol'),
        S298 = (37.56,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1185,
    label        = "C=S-CdsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Sd U0 {1,D}
3   Cd U0 {1,S}
4   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.59,9.38,10.81,11.85,13.18,13.95,14.81],'cal/(mol*K)'),
        H298 = (24.05,'kcal/mol'),
        S298 = (34.35,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-(Cds-Cd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Sd U0 {1,D}
3   Cd U0 {1,S}
4   H  U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-(Cds-Cds)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Sd U0 {1,D}
3   Cd U0 {1,S} {5,D}
4   H  U0 {1,S}
5   Cd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-(Cds-Cdd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Sd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   H   U0 {1,S}
5   Cdd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-(Cds-Cdd-Sd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Sd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   H   U0 {1,S}
5   Cdd U0 {3,D} {6,D}
6   Sd  U0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-(Cds-Cdd-Cd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Sd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   H   U0 {1,S}
5   Cdd U0 {3,D} {6,D}
6   C   U0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1188,
    label        = "C=S-C=SH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Sd U0 {1,D}
3   Cd U0 {1,S} {5,D}
4   H  U0 {1,S}
5   Sd U0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.79,9.18,10.41,11.42,12.82,13.63,14.54],'cal/(mol*K)'),
        H298 = (26.96,'kcal/mol'),
        S298 = (35.65,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1186,
    label        = "C=S-CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Sd U0 {1,D}
3   Ct U0 {1,S}
4   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.46,8.91,10.01,10.83,11.98,12.74,13.87],'cal/(mol*K)'),
        H298 = (30.83,'kcal/mol'),
        S298 = (37.16,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1187,
    label        = "C=S-CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Sd U0 {1,D}
3   Cb U0 {1,S}
4   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.45,9.84,10.94,11.78,12.97,13.76,14.77],'cal/(mol*K)'),
        H298 = (24.71,'kcal/mol'),
        S298 = (34.15,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 65,
    label        = "Cds-OdCOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Od U0 {1,D}
3   C  U0 {1,S}
4   Os U0 {1,S}
""",
    thermo = u'Cds-OdCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 66,
    label        = "Cds-OdCsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Od U0 {1,D}
3   Cs U0 {1,S}
4   Os U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.1,6.7,7.4,8.02,8.87,9.36,9.36],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (-35.1,'kcal/mol','+|-',0.3),
        S298 = (10.04,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""CO-OCs Hf BENSON S STULL !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index        = 67,
    label        = "Cds-OdCdsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C       U0 {2,D} {3,S} {4,S}
2   Od      U0 {1,D}
3   {Cd,CO} U0 {1,S}
4   Os      U0 {1,S}
""",
    thermo = u'Cds-Od(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 68,
    label        = "Cds-Od(Cds-Od)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Od U0 {1,D}
3   CO U0 {1,S}
4   Os U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.46,6.32,7.17,7.88,9,9.77,9.77],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (-29.3,'kcal/mol','+|-',0.3),
        S298 = (14.6,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""CO-OCO Hf,S BOZZELLI Cp BENSON !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index        = 69,
    label        = "Cds-Od(Cds-Cd)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Od U0 {1,D}
3   Cd U0 {1,S}
4   Os U0 {1,S}
""",
    thermo = u'Cds-Od(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 70,
    label        = "Cds-Od(Cds-Cds)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Od U0 {1,D}
3   Cd U0 {1,S} {5,D}
4   Os U0 {1,S}
5   Cd U0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.97,6.7,7.4,8.02,8.87,9.36,9.36],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (-32.1,'kcal/mol','+|-',0.3),
        S298 = (14.78,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""CO-OCd RPS + S Coreected !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index        = 71,
    label        = "Cds-Od(Cds-Cdd)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Od  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Os  U0 {1,S}
5   Cdd U0 {3,D}
""",
    thermo = u'Cds-Od(Cds-Cdd-Cd)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 72,
    label        = "Cds-Od(Cds-Cdd-Od)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Od  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Os  U0 {1,S}
5   Cdd U0 {3,D} {6,D}
6   Od  U0 {5,D}
""",
    thermo = u'Cds-Od(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 73,
    label        = "Cds-Od(Cds-Cdd-Cd)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Od  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Os  U0 {1,S}
5   Cdd U0 {3,D} {6,D}
6   C   U0 {5,D}
""",
    thermo = u'Cds-Od(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 74,
    label        = "Cds-OdCtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Od U0 {1,D}
3   Ct U0 {1,S}
4   Os U0 {1,S}
""",
    thermo = u'Cds-Od(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 75,
    label        = "Cds-OdCbOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Od U0 {1,D}
3   Cb U0 {1,S}
4   Os U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.97,6.7,7.4,8.02,8.87,9.36,9.36],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (-36.6,'kcal/mol','+|-',0.3),
        S298 = (14.78,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""CO-OCb RPS + S Coreected !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1205,
    label        = "C=S-CSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Sd U0 {1,D}
3   C  U0 {1,S}
4   Ss U0 {1,S}
""",
    thermo = u'C=S-CsSs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1206,
    label        = "C=S-CsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Sd U0 {1,D}
3   Cs U0 {1,S}
4   Ss U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.4,8.38,9.16,9.8,10.72,11.25,11.66],'cal/(mol*K)'),
        H298 = (21.35,'kcal/mol'),
        S298 = (14.52,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-CdsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Sd U0 {1,D}
3   Cd U0 {1,S}
4   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-(Cds-Cd)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Sd U0 {1,D}
3   Cd U0 {1,S}
4   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-(Cds-Cds)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Sd U0 {1,D}
3   Cd U0 {1,S} {5,D}
4   Ss U0 {1,S}
5   Cd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-(Cds-Cdd)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Sd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Ss  U0 {1,S}
5   Cdd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-(Cds-Cdd-Sd)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Sd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Ss  U0 {1,S}
5   Cdd U0 {3,D} {6,D}
6   Sd  U0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-(Cds-Cdd-Cd)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Sd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Ss  U0 {1,S}
5   Cdd U0 {3,D} {6,D}
6   C   U0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-C=SSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Sd U0 {1,D}
3   Cd U0 {1,S} {5,D}
4   Ss U0 {1,S}
5   Sd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-CtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Sd U0 {1,D}
3   Ct U0 {1,S}
4   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-CbSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Sd U0 {1,D}
3   Cb U0 {1,S}
4   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 76,
    label        = "Cds-OdCC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Od U0 {1,D}
3   C  U0 {1,S}
4   C  U0 {1,S}
""",
    thermo = u'Cds-OdCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 77,
    label        = "Cds-OdCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Od U0 {1,D}
3   Cs U0 {1,S}
4   Cs U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.59,6.32,7.09,7.76,8.89,9.61,9.61],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (-31.4,'kcal/mol','+|-',0.3),
        S298 = (15.01,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""CO-CsCs BENSON !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index        = 78,
    label        = "Cds-OdCdsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C       U0 {2,D} {3,S} {4,S}
2   Od      U0 {1,D}
3   {Cd,CO} U0 {1,S}
4   Cs      U0 {1,S}
""",
    thermo = u'Cds-Od(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 79,
    label        = "Cds-Od(Cds-Od)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Od U0 {1,D}
3   CO U0 {1,S}
4   Cs U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.46,6.32,7.17,7.88,9,9.77,9.77],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (-29.1,'kcal/mol','+|-',0.3),
        S298 = (14.6,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""CO-COCs Hf,S BOZZELLI Cp BENSON !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index        = 80,
    label        = "Cds-Od(Cds-Cd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Od U0 {1,D}
3   Cd U0 {1,S}
4   Cs U0 {1,S}
""",
    thermo = u'Cds-Od(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 81,
    label        = "Cds-Od(Cds-Cds)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Od U0 {1,D}
3   Cd U0 {1,S} {5,D}
4   Cs U0 {1,S}
5   Cd U0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.46,6.32,7.17,7.88,9,9.77,9.77],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (-30.9,'kcal/mol','+|-',0.3),
        S298 = (14.6,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""CO-CdCs Hf BENSON =3D CO/Cb/C S,Cp !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index        = 82,
    label        = "Cds-Od(Cds-Cdd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Od  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Cs  U0 {1,S}
5   Cdd U0 {3,D}
""",
    thermo = u'Cds-Od(Cds-Cdd-Cd)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 83,
    label        = "Cds-Od(Cds-Cdd-Od)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Od  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Cs  U0 {1,S}
5   Cdd U0 {3,D} {6,D}
6   Od  U0 {5,D}
""",
    thermo = u'Cds-Od(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 84,
    label        = "Cds-Od(Cds-Cdd-Cd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Od  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Cs  U0 {1,S}
5   Cdd U0 {3,D} {6,D}
6   C   U0 {5,D}
""",
    thermo = u'Cds-Od(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 85,
    label        = "Cds-OdCdsCds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C       U0 {2,D} {3,S} {4,S}
2   Od      U0 {1,D}
3   {Cd,CO} U0 {1,S}
4   {Cd,CO} U0 {1,S}
""",
    thermo = u'Cds-Od(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 86,
    label        = "Cds-Od(Cds-Od)(Cds-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Od U0 {1,D}
3   CO U0 {1,S}
4   CO U0 {1,S}
""",
    thermo = u'Cds-OdCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 87,
    label        = "Cds-Od(Cds-Cd)(Cds-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Od U0 {1,D}
3   Cd U0 {1,S}
4   CO U0 {1,S}
""",
    thermo = u'Cds-Od(Cds-Cds)(Cds-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 88,
    label        = "Cds-Od(Cds-Cds)(Cds-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Od U0 {1,D}
3   Cd U0 {1,S} {5,D}
4   CO U0 {1,S}
5   Cd U0 {3,D}
""",
    thermo = u'Cds-Od(Cds-Od)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 89,
    label        = "Cds-Od(Cds-Cdd)(Cds-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Od  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   CO  U0 {1,S}
5   Cdd U0 {3,D}
""",
    thermo = u'Cds-Od(Cds-Cdd-Cd)(Cds-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 90,
    label        = "Cds-Od(Cds-Cdd-Od)(Cds-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Od  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   CO  U0 {1,S}
5   Cdd U0 {3,D} {6,D}
6   Od  U0 {5,D}
""",
    thermo = u'Cds-Od(Cds-Cdd-Od)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 91,
    label        = "Cds-Od(Cds-Cdd-Cd)(Cds-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Od  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   CO  U0 {1,S}
5   Cdd U0 {3,D} {6,D}
6   C   U0 {5,D}
""",
    thermo = u'Cds-Od(Cds-Cds)(Cds-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 92,
    label        = "Cds-Od(Cds-Cd)(Cds-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Od U0 {1,D}
3   Cd U0 {1,S}
4   Cd U0 {1,S}
""",
    thermo = u'Cds-Od(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 93,
    label        = "Cds-Od(Cds-Cds)(Cds-Cds)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Od U0 {1,D}
3   Cd U0 {1,S} {5,D}
4   Cd U0 {1,S} {6,D}
5   Cd U0 {3,D}
6   Cd U0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.46,6.32,7.17,7.88,9,9.77,9.77],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (-30.9,'kcal/mol','+|-',0.3),
        S298 = (14.6,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""CO-CdCd Estimate BOZZELLI !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index        = 94,
    label        = "Cds-Od(Cds-Cdd)(Cds-Cds)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Od  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Cd  U0 {1,S} {6,D}
5   Cdd U0 {3,D}
6   Cd  U0 {4,D}
""",
    thermo = u'Cds-Od(Cds-Cdd-Cd)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 95,
    label        = "Cds-Od(Cds-Cdd-Od)(Cds-Cds)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Od  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Cd  U0 {1,S} {6,D}
5   Cdd U0 {3,D} {7,D}
6   Cd  U0 {4,D}
7   Od  U0 {5,D}
""",
    thermo = u'Cds-Od(Cds-Cdd-Od)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 96,
    label        = "Cds-Od(Cds-Cdd-Cd)(Cds-Cds)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Od  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Cd  U0 {1,S} {6,D}
5   Cdd U0 {3,D} {7,D}
6   Cd  U0 {4,D}
7   C   U0 {5,D}
""",
    thermo = u'Cds-Od(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 97,
    label        = "Cds-Od(Cds-Cdd)(Cds-Cdd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Od  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Cd  U0 {1,S} {6,D}
5   Cdd U0 {3,D}
6   Cdd U0 {4,D}
""",
    thermo = u'Cds-Od(Cds-Cdd-Cd)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 98,
    label        = "Cds-Od(Cds-Cdd-Od)(Cds-Cdd-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Od  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Cd  U0 {1,S} {6,D}
5   Cdd U0 {3,D} {7,D}
6   Cdd U0 {4,D} {8,D}
7   Od  U0 {5,D}
8   Od  U0 {6,D}
""",
    thermo = u'Cds-Od(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 99,
    label        = "Cds-Od(Cds-Cdd-Cd)(Cds-Cdd-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Od  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Cd  U0 {1,S} {6,D}
5   Cdd U0 {3,D} {7,D}
6   Cdd U0 {4,D} {8,D}
7   C   U0 {5,D}
8   Od  U0 {6,D}
""",
    thermo = u'Cds-Od(Cds-Cdd-Od)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 100,
    label        = "Cds-Od(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Od  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Cd  U0 {1,S} {6,D}
5   Cdd U0 {3,D} {7,D}
6   Cdd U0 {4,D} {8,D}
7   C   U0 {5,D}
8   C   U0 {6,D}
""",
    thermo = u'Cds-Od(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 101,
    label        = "Cds-OdCtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Od U0 {1,D}
3   Ct U0 {1,S}
4   Cs U0 {1,S}
""",
    thermo = u'Cds-Od(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 102,
    label        = "Cds-OdCtCds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C       U0 {2,D} {3,S} {4,S}
2   Od      U0 {1,D}
3   Ct      U0 {1,S}
4   {Cd,CO} U0 {1,S}
""",
    thermo = u'Cds-OdCt(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 103,
    label        = "Cds-OdCt(Cds-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Od U0 {1,D}
3   Ct U0 {1,S}
4   CO U0 {1,S}
""",
    thermo = u'Cds-Od(Cds-Cds)(Cds-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 104,
    label        = "Cds-OdCt(Cds-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Od U0 {1,D}
3   Ct U0 {1,S}
4   Cd U0 {1,S}
""",
    thermo = u'Cds-OdCt(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 105,
    label        = "Cds-OdCt(Cds-Cds)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Od U0 {1,D}
3   Ct U0 {1,S}
4   Cd U0 {1,S} {5,D}
5   Cd U0 {4,D}
""",
    thermo = u'Cds-Od(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 106,
    label        = "Cds-OdCt(Cds-Cdd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Od  U0 {1,D}
3   Ct  U0 {1,S}
4   Cd  U0 {1,S} {5,D}
5   Cdd U0 {4,D}
""",
    thermo = u'Cds-OdCt(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 107,
    label        = "Cds-OdCt(Cds-Cdd-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Od  U0 {1,D}
3   Ct  U0 {1,S}
4   Cd  U0 {1,S} {5,D}
5   Cdd U0 {4,D} {6,D}
6   Od  U0 {5,D}
""",
    thermo = u'Cds-Od(Cds-Cdd-Od)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 108,
    label        = "Cds-OdCt(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Od  U0 {1,D}
3   Ct  U0 {1,S}
4   Cd  U0 {1,S} {5,D}
5   Cdd U0 {4,D} {6,D}
6   C   U0 {5,D}
""",
    thermo = u'Cds-OdCt(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 109,
    label        = "Cds-OdCtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Od U0 {1,D}
3   Ct U0 {1,S}
4   Ct U0 {1,S}
""",
    thermo = u'Cds-Od(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 110,
    label        = "Cds-OdCbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Od U0 {1,D}
3   Cb U0 {1,S}
4   Cs U0 {1,S}
""",
    thermo = u'Cds-Od(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 111,
    label        = "Cds-OdCbCds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C       U0 {2,D} {3,S} {4,S}
2   Od      U0 {1,D}
3   Cb      U0 {1,S}
4   {Cd,CO} U0 {1,S}
""",
    thermo = u'Cds-OdCb(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 112,
    label        = "Cds-OdCb(Cds-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Od U0 {1,D}
3   Cb U0 {1,S}
4   CO U0 {1,S}
""",
    thermo = u'Cds-Od(Cds-Cds)(Cds-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 113,
    label        = "Cds-OdCb(Cds-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Od U0 {1,D}
3   Cb U0 {1,S}
4   Cd U0 {1,S}
""",
    thermo = u'Cds-OdCb(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 114,
    label        = "Cds-OdCb(Cds-Cds)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Od U0 {1,D}
3   Cb U0 {1,S}
4   Cd U0 {1,S} {5,D}
5   Cd U0 {4,D}
""",
    thermo = u'Cds-Od(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 115,
    label        = "Cds-OdCb(Cds-Cdd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Od  U0 {1,D}
3   Cb  U0 {1,S}
4   Cd  U0 {1,S} {5,D}
5   Cdd U0 {4,D}
""",
    thermo = u'Cds-OdCb(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 116,
    label        = "Cds-OdCb(Cds-Cdd-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Od  U0 {1,D}
3   Cb  U0 {1,S}
4   Cd  U0 {1,S} {5,D}
5   Cdd U0 {4,D} {6,D}
6   Od  U0 {5,D}
""",
    thermo = u'Cds-Od(Cds-Cdd-Od)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 117,
    label        = "Cds-OdCb(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Od  U0 {1,D}
3   Cb  U0 {1,S}
4   Cd  U0 {1,S} {5,D}
5   Cdd U0 {4,D} {6,D}
6   C   U0 {5,D}
""",
    thermo = u'Cds-OdCb(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 118,
    label        = "Cds-OdCbCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Od U0 {1,D}
3   Cb U0 {1,S}
4   Ct U0 {1,S}
""",
    thermo = u'Cds-OdCt(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 119,
    label        = "Cds-OdCbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Od U0 {1,D}
3   Cb U0 {1,S}
4   Cb U0 {1,S}
""",
    thermo = u'Cds-Od(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-CC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Sd U0 {1,D}
3   C  U0 {1,S}
4   C  U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1190,
    label        = "C=S-CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Sd U0 {1,D}
3   Cs U0 {1,S}
4   Cs U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.7,7.44,8.14,8.72,9.52,9.98,10.51],'cal/(mol*K)'),
        H298 = (27.2,'kcal/mol'),
        S298 = (18,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1191,
    label        = "C=S-CdsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Sd U0 {1,D}
3   Cd U0 {1,S}
4   Cs U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.79,9.21,10.13,10.71,11.25,11.42,11.35],'cal/(mol*K)'),
        H298 = (26.19,'kcal/mol'),
        S298 = (13.44,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-(Cds-Cd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Sd U0 {1,D}
3   Cd U0 {1,S}
4   Cs U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-(Cds-Cds)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Sd U0 {1,D}
3   Cd U0 {1,S} {5,D}
4   Cs U0 {1,S}
5   Cd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-(Cds-Cdd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Sd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Cs  U0 {1,S}
5   Cdd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-(Cds-Cdd-Sd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Sd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Cs  U0 {1,S}
5   Cdd U0 {3,D} {6,D}
6   Sd  U0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-(Cds-Cdd-Cd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Sd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Cs  U0 {1,S}
5   Cdd U0 {3,D} {6,D}
6   C   U0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1194,
    label        = "C=S-C=SCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Sd U0 {1,D}
3   Cd U0 {1,S} {5,D}
4   Cs U0 {1,S}
5   Sd U0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.93,7.93,8.76,9.37,10.11,10.45,10.71],'cal/(mol*K)'),
        H298 = (27.48,'kcal/mol'),
        S298 = (16.58,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-CdsCds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Sd U0 {1,D}
3   Cd U0 {1,S}
4   Cd U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-(Cds-Cd)(Cds-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Sd U0 {1,D}
3   Cd U0 {1,S}
4   Cd U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-(Cds-Cds)(Cds-Cds)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Sd U0 {1,D}
3   Cd U0 {1,S} {5,D}
4   Cd U0 {1,S} {6,D}
5   Cd U0 {3,D}
6   Cd U0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-(Cds-Cdd)(Cds-Cds)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Sd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Cd  U0 {1,S} {6,D}
5   Cdd U0 {3,D}
6   Cd  U0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-(Cds-Cdd-Sd)(Cds-Cds)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Sd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Cd  U0 {1,S} {6,D}
5   Cdd U0 {3,D} {7,D}
6   Cd  U0 {4,D}
7   Sd  U0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-(Cds-Cdd-Cd)(Cds-Cds)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Sd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Cd  U0 {1,S} {6,D}
5   Cdd U0 {3,D} {7,D}
6   Cd  U0 {4,D}
7   C   U0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-(Cds-Cdd)(Cds-Cdd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Sd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Cd  U0 {1,S} {6,D}
5   Cdd U0 {3,D}
6   Cdd U0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-(Cds-Cdd-Sd)(Cds-Cdd-Sd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Sd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Cd  U0 {1,S} {6,D}
5   Cdd U0 {3,D} {7,D}
6   Cdd U0 {4,D} {8,D}
7   Sd  U0 {5,D}
8   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-(Cds-Cdd-Cd)(Cds-Cdd-Sd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Sd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Cd  U0 {1,S} {6,D}
5   Cdd U0 {3,D} {7,D}
6   Cdd U0 {4,D} {8,D}
7   C   U0 {5,D}
8   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Sd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Cd  U0 {1,S} {6,D}
5   Cdd U0 {3,D} {7,D}
6   Cdd U0 {4,D} {8,D}
7   C   U0 {5,D}
8   C   U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-(Cds-Cd)C=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Sd U0 {1,D}
3   Cd U0 {1,S}
4   Cd U0 {1,S} {5,D}
5   Sd U0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-(Cds-Cds)C=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Sd U0 {1,D}
3   Cd U0 {1,S} {5,D}
4   Cd U0 {1,S} {6,D}
5   Cd U0 {3,D}
6   Sd U0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-(Cds-Cdd)C=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Sd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Cd  U0 {1,S} {6,D}
5   Cdd U0 {3,D}
6   Sd  U0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-(Cds-Cdd-Sd)C=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Sd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Cd  U0 {1,S} {7,D}
5   Cdd U0 {3,D} {6,D}
6   Sd  U0 {5,D}
7   Sd  U0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-(Cds-Cdd-Cd)C=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Sd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Cd  U0 {1,S} {7,D}
5   Cdd U0 {3,D} {6,D}
6   C   U0 {5,D}
7   Sd  U0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-C=SC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Sd U0 {1,D}
3   Cd U0 {1,S} {5,D}
4   Cd U0 {1,S} {6,D}
5   Sd U0 {3,D}
6   Sd U0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1192,
    label        = "C=S-CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Sd U0 {1,D}
3   Ct U0 {1,S}
4   Cs U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.87,7.88,8.6,9.13,9.8,10.17,10.59],'cal/(mol*K)'),
        H298 = (30.12,'kcal/mol'),
        S298 = (17.46,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-CtCds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Sd U0 {1,D}
3   Ct U0 {1,S}
4   Cd U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-Ct(Cds-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Sd U0 {1,D}
3   Ct U0 {1,S}
4   Cd U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-Ct(Cds-Cds)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Sd U0 {1,D}
3   Ct U0 {1,S}
4   Cd U0 {1,S} {5,D}
5   Cd U0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-Ct(Cds-Cdd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Sd  U0 {1,D}
3   Ct  U0 {1,S}
4   Cd  U0 {1,S} {5,D}
5   Cdd U0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-Ct(Cds-Cdd-Sd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Sd  U0 {1,D}
3   Ct  U0 {1,S}
4   Cd  U0 {1,S} {5,D}
5   Cdd U0 {4,D} {6,D}
6   Sd  U0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-Ct(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Sd  U0 {1,D}
3   Ct  U0 {1,S}
4   Cd  U0 {1,S} {5,D}
5   Cdd U0 {4,D} {6,D}
6   C   U0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-CtC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Sd U0 {1,D}
3   Ct U0 {1,S}
4   Cd U0 {1,S} {5,D}
5   Sd U0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Sd U0 {1,D}
3   Ct U0 {1,S}
4   Ct U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1193,
    label        = "C=S-CbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Sd U0 {1,D}
3   Cb U0 {1,S}
4   Cs U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.02,9.02,9.75,10.23,10.75,10.96,11.04],'cal/(mol*K)'),
        H298 = (26.6,'kcal/mol'),
        S298 = (14.55,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-CbCds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Sd U0 {1,D}
3   Cb U0 {1,S}
4   Cd U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-Cb(Cds-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Sd U0 {1,D}
3   Cb U0 {1,S}
4   Cd U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-Cb(Cds-Cds)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Sd U0 {1,D}
3   Cb U0 {1,S}
4   Cd U0 {1,S} {5,D}
5   Cd U0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-Cb(Cds-Cdd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Sd  U0 {1,D}
3   Cb  U0 {1,S}
4   Cd  U0 {1,S} {5,D}
5   Cdd U0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-Cb(Cds-Cdd-Sd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Sd  U0 {1,D}
3   Cb  U0 {1,S}
4   Cd  U0 {1,S} {5,D}
5   Cdd U0 {4,D} {6,D}
6   Sd  U0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-Cb(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Sd  U0 {1,D}
3   Cb  U0 {1,S}
4   Cd  U0 {1,S} {5,D}
5   Cdd U0 {4,D} {6,D}
6   C   U0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-CbC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Sd U0 {1,D}
3   Cb U0 {1,S}
4   Cd U0 {1,S} {5,D}
5   Sd U0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-CbCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Sd U0 {1,D}
3   Cb U0 {1,S}
4   Ct U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=S-CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Sd U0 {1,D}
3   Cb U0 {1,S}
4   Cb U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1456,
    label        = "CS-CsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Sd U0 {1,D}
3   Os U0 {1,S}
4   Cs U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.56,4.06,4.48,4.82,5.35,5.7,6.03],'cal/(mol*K)'),
        H298 = (-11.19,'kcal/mol'),
        S298 = (6.94,'cal/(mol*K)'),
    ),
    shortDesc = u"""CAC 1d-HR calc""",
    longDesc = 
u"""

""",
)

entry(
    index        = 120,
    label        = "Cds-CdHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U0 {2,D} {3,S} {4,S}
2   C U0 {1,D}
3   H U0 {1,S}
4   H U0 {1,S}
""",
    thermo = u'Cds-CdsHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 121,
    label        = "Cds-CdsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   H  U0 {1,S}
4   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.1,6.36,7.51,8.5,10.07,11.27,13.19],'cal/(mol*K)','+|-',[0.07,0.07,0.07,0.07,0.07,0.07,0.07]),
        H298 = (6.26,'kcal/mol','+|-',0.19),
        S298 = (27.61,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cd-HH BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index        = 122,
    label        = "Cds-CddHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D}
3   H   U0 {1,S}
4   H   U0 {1,S}
""",
    thermo = u'Cds-(Cdd-Cd)HH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 123,
    label        = "Cds-(Cdd-Od)HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   H   U0 {1,S}
4   H   U0 {1,S}
5   Od  U0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.08,13.91,15.4,16.64,18.61,20.1,22.47],'cal/(mol*K)','+|-',[0.07,0.07,0.07,0.07,0.07,0.07,0.07]),
        H298 = (-11.34,'kcal/mol','+|-',0.19),
        S298 = (57.47,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""{CCO/H2} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   H   U0 {1,S}
4   H   U0 {1,S}
5   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 124,
    label        = "Cds-(Cdd-Cd)HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   H   U0 {1,S}
4   H   U0 {1,S}
5   C   U0 {2,D}
""",
    thermo = u'Cds-CdsHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 125,
    label        = "Cds-CdOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   C  U0 {1,D}
3   Os U0 {1,S}
4   H  U0 {1,S}
""",
    thermo = u'Cds-CdsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 126,
    label        = "Cds-CdsOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   Os U0 {1,S}
4   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.75,6.46,7.64,8.35,9.1,9.56,10.46],'cal/(mol*K)','+|-',[0.07,0.07,0.07,0.07,0.07,0.07,0.07]),
        H298 = (2.03,'kcal/mol','+|-',0.19),
        S298 = (6.2,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cd-OH BOZZELLI Hf vin-oh RADOM + C/Cd/H, S&Cp LAY""",
    longDesc = 
u"""

""",
)

entry(
    index        = 127,
    label        = "Cds-CddOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D}
3   Os  U0 {1,S}
4   H   U0 {1,S}
""",
    thermo = u'Cds-(Cdd-Cd)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 128,
    label        = "Cds-(Cdd-Od)OsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Os  U0 {1,S}
4   H   U0 {1,S}
5   Od  U0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.29,13.67,15.1,16.1,17.36,18.25,19.75],'cal/(mol*K)','+|-',[0.07,0.07,0.07,0.07,0.07,0.07,0.07]),
        H298 = (2.11,'kcal/mol','+|-',0.19),
        S298 = (38.17,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""{CCO/O/H} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""

""",
)

entry(
    index        = 129,
    label        = "Cds-(Cdd-Cd)OsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Os  U0 {1,S}
4   H   U0 {1,S}
5   C   U0 {2,D}
""",
    thermo = u'Cds-CdsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-CdSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   C  U0 {1,D}
3   Ss U0 {1,S}
4   H  U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1180,
    label        = "Cds-CdsSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   Ss U0 {1,S}
4   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.41,5.2,5.98,6.68,7.8,8.62,9.84],'cal/(mol*K)'),
        H298 = (8.87,'kcal/mol'),
        S298 = (7.87,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-CddSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D}
3   Ss  U0 {1,S}
4   H   U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)SsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Ss  U0 {1,S}
4   H   U0 {1,S}
5   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Cd)SsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Ss  U0 {1,S}
4   H   U0 {1,S}
5   C   U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 130,
    label        = "Cds-CdOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   C  U0 {1,D}
3   Os U0 {1,S}
4   Os U0 {1,S}
""",
    thermo = u'Cds-CdsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 131,
    label        = "Cds-CdsOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   Os U0 {1,S}
4   Os U0 {1,S}
""",
    thermo = u'Cds-CdsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 132,
    label        = "Cds-CddOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D}
3   Os  U0 {1,S}
4   Os  U0 {1,S}
""",
    thermo = u'Cds-(Cdd-Cd)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 133,
    label        = "Cds-(Cdd-Od)OsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Os  U0 {1,S}
4   Os  U0 {1,S}
5   Od  U0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.56,15.58,17.69,18.67,18.78,18.4,18.01],'cal/(mol*K)','+|-',[0.07,0.07,0.07,0.07,0.07,0.07,0.07]),
        H298 = (2.403,'kcal/mol','+|-',0.19),
        S298 = (13.42,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""{CCO/O2} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""

""",
)

entry(
    index        = 134,
    label        = "Cds-(Cdd-Cd)OsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Os  U0 {1,S}
4   Os  U0 {1,S}
5   C   U0 {2,D}
""",
    thermo = u'Cds-CdsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-CdSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   C  U0 {1,D}
3   Ss U0 {1,S}
4   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-CdsSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   Ss U0 {1,S}
4   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-CddSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D}
3   Ss  U0 {1,S}
4   Ss  U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)SsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Ss  U0 {1,S}
4   Ss  U0 {1,S}
5   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Cd)SsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Ss  U0 {1,S}
4   Ss  U0 {1,S}
5   C   U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 135,
    label        = "Cds-CdCH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U0 {2,D} {3,S} {4,S}
2   C U0 {1,D}
3   C U0 {1,S}
4   H U0 {1,S}
""",
    thermo = u'Cds-CdsCsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 136,
    label        = "Cds-CdsCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   Cs U0 {1,S}
4   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.16,5.03,5.81,6.5,7.65,8.45,9.62],'cal/(mol*K)','+|-',[0.06,0.06,0.06,0.06,0.06,0.06,0.06]),
        H298 = (8.59,'kcal/mol','+|-',0.17),
        S298 = (7.97,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cd-CsH BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index        = 137,
    label        = "Cds-CdsCdsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C       U0 {2,D} {3,S} {4,S}
2   Cd      U0 {1,D}
3   {Cd,CO} U0 {1,S}
4   H       U0 {1,S}
""",
    thermo = u'Cds-Cds(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 138,
    label        = "Cds-Cds(Cds-Od)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   CO U0 {1,S}
4   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.46,5.79,6.75,7.42,8.35,9.11,10.09],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (4.32,'kcal/mol','+|-',0.2),
        S298 = (6.38,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cd-COH BOZZELLI lit rev Jul91 S,Cp Cd/Cd/H""",
    longDesc = 
u"""

""",
)

entry(
    index        = 139,
    label        = "Cds-Cds(Cds-Cd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   Cd U0 {1,S}
4   H  U0 {1,S}
""",
    thermo = u'Cds-Cds(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 140,
    label        = "Cds-Cds(Cds-Cds)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   Cd U0 {1,S} {5,D}
4   H  U0 {1,S}
5   Cd U0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.46,5.79,6.75,7.42,8.35,8.99,9.98],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (6.78,'kcal/mol','+|-',0.2),
        S298 = (6.38,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cd-CdH BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index        = 141,
    label        = "Cds-Cds(Cds-Cdd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   H   U0 {1,S}
5   Cdd U0 {3,D}
""",
    thermo = u'Cds-Cds(Cds-Cdd-Cd)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 142,
    label        = "Cds-Cds(Cds-Cdd-Od)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   H   U0 {1,S}
5   Cdd U0 {3,D} {6,D}
6   Od  U0 {5,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-Cds(Cds-Cdd-Sd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   H   U0 {1,S}
5   Cdd U0 {3,D} {6,D}
6   Sd  U0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 143,
    label        = "Cds-Cds(Cds-Cdd-Cd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   H   U0 {1,S}
5   Cdd U0 {3,D} {6,D}
6   C   U0 {5,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1182,
    label        = "Cds-CdsC=SH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   Cd U0 {1,S} {5,D}
4   H  U0 {1,S}
5   Sd U0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.41,5.2,5.98,6.68,7.8,8.62,9.84],'cal/(mol*K)'),
        H298 = (8.87,'kcal/mol'),
        S298 = (7.87,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 144,
    label        = "Cds-CdsCtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   Ct U0 {1,S}
4   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.46,5.79,6.75,7.42,8.35,8.99,9.98],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (6.78,'kcal/mol','+|-',0.2),
        S298 = (6.38,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cd-CtH BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1836,
    label        = "Cds-CdsH(CtN3t)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cd  U0 {2,D} {3,S} {4,S}
2   Cd  U0 {1,D}
3   H   U0 {1,S}
4   Ct  U0 {1,S} {5,T}
5   N3t U0 {4,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.3,12,13.4,14.6,16.3,17.5,19.4],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (38.5,'kcal/mol','+|-',1.3),
        S298 = (37.6,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 145,
    label        = "Cds-CdsCbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   Cb U0 {1,S}
4   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.46,5.79,6.75,7.42,8.35,8.99,9.98],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (6.78,'kcal/mol','+|-',0.2),
        S298 = (6.38,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cd-CbH BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index        = 146,
    label        = "Cds-CddCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D}
3   Cs  U0 {1,S}
4   H   U0 {1,S}
""",
    thermo = u'Cds-(Cdd-Cd)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 147,
    label        = "Cds-(Cdd-Od)CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cs  U0 {1,S}
4   H   U0 {1,S}
5   Od  U0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.31,11.72,12.94,13.98,15.71,16.95,18.78],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-4.947,'kcal/mol','+|-',0.2),
        S298 = (40.04,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""{CCO/H/C} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cs  U0 {1,S}
4   H   U0 {1,S}
5   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 148,
    label        = "Cds-(Cdd-Cd)CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cs  U0 {1,S}
4   H   U0 {1,S}
5   C   U0 {2,D}
""",
    thermo = u'Cds-CdsCsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 149,
    label        = "Cds-CddCdsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C       U0 {2,D} {3,S} {4,S}
2   Cdd     U0 {1,D}
3   {Cd,CO} U0 {1,S}
4   H       U0 {1,S}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 150,
    label        = "Cds-(Cdd-Od)(Cds-Od)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   CO  U0 {1,S}
4   H   U0 {1,S}
5   Od  U0 {2,D}
""",
    thermo = u'Cds-(Cdd-Od)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 151,
    label        = "Cds-(Cdd-Od)(Cds-Cd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S}
4   H   U0 {1,S}
5   Od  U0 {2,D}
""",
    thermo = u'Cds-(Cdd-Od)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 152,
    label        = "Cds-(Cdd-Od)(Cds-Cds)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   H   U0 {1,S}
5   Od  U0 {2,D}
6   Cd  U0 {3,D}
""",
    thermo = u'Cds-(Cdd-Od)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 153,
    label        = "Cds-(Cdd-Od)(Cds-Cdd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   H   U0 {1,S}
5   Od  U0 {2,D}
6   Cdd U0 {3,D}
""",
    thermo = u'Cds-(Cdd-Od)(Cds-Cdd-Cd)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 154,
    label        = "Cds-(Cdd-Od)(Cds-Cdd-Od)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   H   U0 {1,S}
5   Od  U0 {2,D}
6   Cdd U0 {3,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.55,12.41,13.82,14.91,16.51,17.62,19.24],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-4.998,'kcal/mol','+|-',0.2),
        S298 = (39.06,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""{CCO/H/CCO} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""

""",
)

entry(
    index        = 155,
    label        = "Cds-(Cdd-Od)(Cds-Cdd-Cd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   H   U0 {1,S}
5   Od  U0 {2,D}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cds-(Cdd-Od)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)(Cds-Cd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S}
4   H   U0 {1,S}
5   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)(Cds-Cds)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   H   U0 {1,S}
5   Sd  U0 {2,D}
6   Cd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)(Cds-Cdd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   H   U0 {1,S}
5   Sd  U0 {2,D}
6   Cdd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)(Cds-Cdd-Sd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   H   U0 {1,S}
5   Sd  U0 {2,D}
6   Cdd U0 {3,D} {7,D}
7   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)(Cds-Cdd-Cd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   H   U0 {1,S}
5   Sd  U0 {2,D}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 156,
    label        = "Cds-(Cdd-Cd)(Cds-Od)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   CO  U0 {1,S}
4   H   U0 {1,S}
5   C   U0 {2,D}
""",
    thermo = u'Cds-Cds(Cds-Od)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 157,
    label        = "Cds-(Cdd-Cd)(Cds-Cd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S}
4   H   U0 {1,S}
5   C   U0 {2,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 158,
    label        = "Cds-(Cdd-Cd)(Cds-Cds)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   H   U0 {1,S}
5   C   U0 {2,D}
6   Cd  U0 {3,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 159,
    label        = "Cds-(Cdd-Cd)(Cds-Cdd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   H   U0 {1,S}
5   C   U0 {2,D}
6   Cdd U0 {3,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cdd-Cd)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 160,
    label        = "Cds-(Cdd-Cd)(Cds-Cdd-Od)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   H   U0 {1,S}
5   C   U0 {2,D}
6   Cdd U0 {3,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cds-Cds(Cds-Cdd-Od)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Cd)(Cds-Cdd-Sd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   H   U0 {1,S}
5   C   U0 {2,D}
6   Cdd U0 {3,D} {7,D}
7   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 161,
    label        = "Cds-(Cdd-Cd)(Cds-Cdd-Cd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   H   U0 {1,S}
5   C   U0 {2,D}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)C=SH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   H   U0 {1,S}
5   Sd  U0 {2,D}
6   Sd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Cd)C=SH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   H   U0 {1,S}
5   C   U0 {2,D}
6   Sd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 162,
    label        = "Cds-CddCtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D}
3   Ct  U0 {1,S}
4   H   U0 {1,S}
""",
    thermo = u'Cds-(Cdd-Cd)CtH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 163,
    label        = "Cds-(Cdd-Od)CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Ct  U0 {1,S}
4   H   U0 {1,S}
5   Od  U0 {2,D}
""",
    thermo = u'Cds-(Cdd-Od)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Ct  U0 {1,S}
4   H   U0 {1,S}
5   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 164,
    label        = "Cds-(Cdd-Cd)CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Ct  U0 {1,S}
4   H   U0 {1,S}
5   C   U0 {2,D}
""",
    thermo = u'Cds-CdsCtH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 165,
    label        = "Cds-CddCbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D}
3   Cb  U0 {1,S}
4   H   U0 {1,S}
""",
    thermo = u'Cds-(Cdd-Cd)CbH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 166,
    label        = "Cds-(Cdd-Od)CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cb  U0 {1,S}
4   H   U0 {1,S}
5   Od  U0 {2,D}
""",
    thermo = u'Cds-(Cdd-Od)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cb  U0 {1,S}
4   H   U0 {1,S}
5   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 167,
    label        = "Cds-(Cdd-Cd)CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cb  U0 {1,S}
4   H   U0 {1,S}
5   C   U0 {2,D}
""",
    thermo = u'Cds-CdsCbH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 168,
    label        = "Cds-CdCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U0 {2,D} {3,S} {4,S}
2   C U0 {1,D}
3   C U0 {1,S}
4   O U0 {1,S}
""",
    thermo = u'Cds-CdsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 169,
    label        = "Cds-CdsCsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   Cs U0 {1,S}
4   Os U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.59,4.56,5.04,5.3,5.84,6.07,6.16],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (3.03,'kcal/mol','+|-',0.2),
        S298 = (-12.32,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cd-OCs BOZZELLI-RADOM vin-oh and del (ccoh-ccohc)""",
    longDesc = 
u"""

""",
)

entry(
    index        = 170,
    label        = "Cds-CdsCdsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C       U0 {2,D} {3,S} {4,S}
2   Cd      U0 {1,D}
3   {Cd,CO} U0 {1,S}
4   Os      U0 {1,S}
""",
    thermo = u'Cds-Cds(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 171,
    label        = "Cds-Cds(Cds-Od)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   CO U0 {1,S}
4   Os U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.4,5.37,5.93,6.18,6.5,6.62,6.72],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (5.13,'kcal/mol','+|-',0.2),
        S298 = (-14.6,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cd-OCO adj BENSON for RADOM c*coh""",
    longDesc = 
u"""

""",
)

entry(
    index        = 172,
    label        = "Cds-Cds(Cds-Cd)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   Cd U0 {1,S}
4   Os U0 {1,S}
""",
    thermo = u'Cds-Cds(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 173,
    label        = "Cds-Cds(Cds-Cds)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   Cd U0 {1,S} {5,D}
4   Os U0 {1,S}
5   Cd U0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.4,5.37,5.93,6.18,6.5,6.62,6.72],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (1.5,'kcal/mol','+|-',0.2),
        S298 = (-14.4,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cd-OCd jwb need calc""",
    longDesc = 
u"""

""",
)

entry(
    index        = 174,
    label        = "Cds-Cds(Cds-Cdd)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Os  U0 {1,S}
5   Cdd U0 {3,D}
""",
    thermo = u'Cds-Cds(Cds-Cdd-Cd)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 175,
    label        = "Cds-Cds(Cds-Cdd-Od)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Os  U0 {1,S}
5   Cdd U0 {3,D} {6,D}
6   Od  U0 {5,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 176,
    label        = "Cds-Cds(Cds-Cdd-Cd)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Os  U0 {1,S}
5   Cdd U0 {3,D} {6,D}
6   C   U0 {5,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 177,
    label        = "Cds-CdsCtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   Ct U0 {1,S}
4   Os U0 {1,S}
""",
    thermo = u'Cds-Cds(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 178,
    label        = "Cds-CdsCbOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   Cb U0 {1,S}
4   Os U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.4,5.37,5.93,6.18,6.5,6.62,6.72],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (1.5,'kcal/mol','+|-',0.2),
        S298 = (-14.4,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cd-OCb jwb need calc""",
    longDesc = 
u"""

""",
)

entry(
    index        = 179,
    label        = "Cds-CddCsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D}
3   Cs  U0 {1,S}
4   Os  U0 {1,S}
""",
    thermo = u'Cds-(Cdd-Cd)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 180,
    label        = "Cds-(Cdd-Od)CsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cs  U0 {1,S}
4   Os  U0 {1,S}
5   Od  U0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.91,12.65,13.59,14.22,15,15.48,16.28],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (3.273,'kcal/mol','+|-',0.2),
        S298 = (18.58,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""{CCO/O/C} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""

""",
)

entry(
    index        = 181,
    label        = "Cds-(Cdd-Cd)CsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cs  U0 {1,S}
4   Os  U0 {1,S}
5   C   U0 {2,D}
""",
    thermo = u'Cds-CdsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 182,
    label        = "Cds-CddCdsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C       U0 {2,D} {3,S} {4,S}
2   Cdd     U0 {1,D}
3   {Cd,CO} U0 {1,S}
4   Os      U0 {1,S}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 183,
    label        = "Cds-(Cdd-Od)(Cds-Od)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   CO  U0 {1,S}
4   Os  U0 {1,S}
5   Od  U0 {2,D}
""",
    thermo = u'Cds-(Cdd-Od)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 184,
    label        = "Cds-(Cdd-Od)(Cds-Cd)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S}
4   Os  U0 {1,S}
5   Od  U0 {2,D}
""",
    thermo = u'Cds-(Cdd-Od)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 185,
    label        = "Cds-(Cdd-Od)(Cds-Cds)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Os  U0 {1,S}
5   Od  U0 {2,D}
6   Cd  U0 {3,D}
""",
    thermo = u'Cds-(Cdd-Od)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 186,
    label        = "Cds-(Cdd-Od)(Cds-Cdd)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Os  U0 {1,S}
5   Od  U0 {2,D}
6   Cdd U0 {3,D}
""",
    thermo = u'Cds-(Cdd-Od)(Cds-Cdd-Cd)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 187,
    label        = "Cds-(Cdd-Od)(Cds-Cdd-Od)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Os  U0 {1,S}
5   Od  U0 {2,D}
6   Cdd U0 {3,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.01,12.97,14.17,14.97,15.8,16.26,16.88],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (1.607,'kcal/mol','+|-',0.2),
        S298 = (17.73,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""{CCO/O/CCO} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""

""",
)

entry(
    index        = 188,
    label        = "Cds-(Cdd-Od)(Cds-Cdd-Cd)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Os  U0 {1,S}
5   Od  U0 {2,D}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cds-(Cdd-Od)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 189,
    label        = "Cds-(Cdd-Cd)(Cds-Cd)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S}
4   Os  U0 {1,S}
5   C   U0 {2,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 190,
    label        = "Cds-(Cdd-Cd)(Cds-Cds)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Os  U0 {1,S}
5   C   U0 {2,D}
6   Cd  U0 {3,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 191,
    label        = "Cds-(Cdd-Cd)(Cds-Cdd)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Os  U0 {1,S}
5   C   U0 {2,D}
6   Cdd U0 {3,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cdd-Cd)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 192,
    label        = "Cds-(Cdd-Cd)(Cds-Cdd-Od)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Os  U0 {1,S}
5   C   U0 {2,D}
6   Cdd U0 {3,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cds-Cds(Cds-Cdd-Od)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 193,
    label        = "Cds-(Cdd-Cd)(Cds-Cdd-Cd)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Os  U0 {1,S}
5   C   U0 {2,D}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 194,
    label        = "Cds-CddCtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D}
3   Ct  U0 {1,S}
4   Os  U0 {1,S}
""",
    thermo = u'Cds-(Cdd-Cd)CtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 195,
    label        = "Cds-(Cdd-Od)CtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Ct  U0 {1,S}
4   Os  U0 {1,S}
5   Od  U0 {2,D}
""",
    thermo = u'Cds-(Cdd-Od)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 196,
    label        = "Cds-(Cdd-Cd)CtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Ct  U0 {1,S}
4   Os  U0 {1,S}
5   C   U0 {2,D}
""",
    thermo = u'Cds-CdsCtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 197,
    label        = "Cds-CddCbOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D}
3   Cb  U0 {1,S}
4   Os  U0 {1,S}
""",
    thermo = u'Cds-(Cdd-Cd)CbOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 198,
    label        = "Cds-(Cdd-Od)CbOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cb  U0 {1,S}
4   Os  U0 {1,S}
5   Od  U0 {2,D}
""",
    thermo = u'Cds-(Cdd-Od)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 199,
    label        = "Cds-(Cdd-Cd)CbOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cb  U0 {1,S}
4   Os  U0 {1,S}
5   C   U0 {2,D}
""",
    thermo = u'Cds-CdsCbOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-CdCS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U0 {2,D} {3,S} {4,S}
2   C U0 {1,D}
3   C U0 {1,S}
4   S U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1181,
    label        = "Cds-CdsCsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   Cs U0 {1,S}
4   Ss U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.23,4.63,4.97,5.29,5.83,6.17,6.53],'cal/(mol*K)'),
        H298 = (10.63,'kcal/mol'),
        S298 = (-12.76,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-CdsCdsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   Cd U0 {1,S}
4   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-Cds(Cds-Cd)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   Cd U0 {1,S}
4   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-Cds(Cds-Cds)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   Cd U0 {1,S} {5,D}
4   Ss U0 {1,S}
5   Cd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-Cds(Cds-Cdd)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Ss  U0 {1,S}
5   Cdd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-Cds(Cds-Cdd-Sd)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Ss  U0 {1,S}
5   Cdd U0 {3,D} {6,D}
6   Sd  U0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-Cds(Cds-Cdd-Cd)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Ss  U0 {1,S}
5   Cdd U0 {3,D} {6,D}
6   C   U0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-CdsC=SSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   Cd U0 {1,S} {5,D}
4   Ss U0 {1,S}
5   Sd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-CdsCtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   Ct U0 {1,S}
4   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-CdsCbSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   Cb U0 {1,S}
4   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-CddCsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D}
3   Cs  U0 {1,S}
4   Ss  U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)CsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cs  U0 {1,S}
4   Ss  U0 {1,S}
5   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Cd)CsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cs  U0 {1,S}
4   Ss  U0 {1,S}
5   C   U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-CddCdsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D}
3   Cd  U0 {1,S}
4   Ss  U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)(Cds-Cd)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S}
4   Ss  U0 {1,S}
5   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)(Cds-Cds)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Ss  U0 {1,S}
5   Sd  U0 {2,D}
6   Cd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)(Cds-Cdd)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Ss  U0 {1,S}
5   Sd  U0 {2,D}
6   Cdd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)(Cds-Cdd-Sd)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Ss  U0 {1,S}
5   Sd  U0 {2,D}
6   Cdd U0 {3,D} {7,D}
7   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)(Cds-Cdd-Cd)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Ss  U0 {1,S}
5   Sd  U0 {2,D}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Cd)(Cds-Cd)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S}
4   Ss  U0 {1,S}
5   C   U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Cd)(Cds-Cds)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Ss  U0 {1,S}
5   C   U0 {2,D}
6   Cd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Cd)(Cds-Cdd)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Ss  U0 {1,S}
5   C   U0 {2,D}
6   Cdd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Cd)(Cds-Cdd-Sd)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Ss  U0 {1,S}
5   C   U0 {2,D}
6   Cdd U0 {3,D} {7,D}
7   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Cd)(Cds-Cdd-Cd)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Ss  U0 {1,S}
5   C   U0 {2,D}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)C=SSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Ss  U0 {1,S}
5   Sd  U0 {2,D}
6   Sd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-CddCtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D}
3   Ct  U0 {1,S}
4   Ss  U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)CtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Ct  U0 {1,S}
4   Ss  U0 {1,S}
5   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Cd)CtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Ct  U0 {1,S}
4   Ss  U0 {1,S}
5   C   U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-CddCbSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D}
3   Cb  U0 {1,S}
4   Ss  U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)CbSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cb  U0 {1,S}
4   Ss  U0 {1,S}
5   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Cd)CbSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cb  U0 {1,S}
4   Ss  U0 {1,S}
5   C   U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 200,
    label        = "Cds-CdCC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U0 {2,D} {3,S} {4,S}
2   C U0 {1,D}
3   C U0 {1,S}
4   C U0 {1,S}
""",
    thermo = u'Cds-CdsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 201,
    label        = "Cds-CdsCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   Cs U0 {1,S}
4   Cs U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.1,4.61,4.99,5.26,5.8,6.08,6.36],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (10.34,'kcal/mol','+|-',0.24),
        S298 = (-12.7,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = u"""Cd-CsCs BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index        = 202,
    label        = "Cds-CdsCdsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C       U0 {2,D} {3,S} {4,S}
2   Cd      U0 {1,D}
3   {Cd,CO} U0 {1,S}
4   Cs      U0 {1,S}
""",
    thermo = u'Cds-Cds(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 203,
    label        = "Cds-Cds(Cds-Od)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   CO U0 {1,S}
4   Cs U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.4,5.37,5.93,6.18,6.5,6.62,6.72],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (7.5,'kcal/mol','+|-',0.24),
        S298 = (-14.6,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = u"""Cd-COCs BENSON Hf, Cd/C/Cd =3D S,Cp""",
    longDesc = 
u"""

""",
)

entry(
    index        = 204,
    label        = "Cds-Cds(Cds-Cd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   Cd U0 {1,S}
4   Cs U0 {1,S}
""",
    thermo = u'Cds-Cds(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 205,
    label        = "Cds-Cds(Cds-Cds)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   Cd U0 {1,S} {5,D}
4   Cs U0 {1,S}
5   Cd U0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.4,5.37,5.93,6.18,6.5,6.62,6.72],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (8.88,'kcal/mol','+|-',0.24),
        S298 = (-14.6,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = u"""Cd-CdCs BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index        = 206,
    label        = "Cds-Cds(Cds-Cdd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Cs  U0 {1,S}
5   Cdd U0 {3,D}
""",
    thermo = u'Cds-Cds(Cds-Cdd-Cd)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 207,
    label        = "Cds-Cds(Cds-Cdd-Od)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Cs  U0 {1,S}
5   Cdd U0 {3,D} {6,D}
6   Od  U0 {5,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-Cds(Cds-Cdd-Sd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Cs  U0 {1,S}
5   Cdd U0 {3,D} {6,D}
6   Sd  U0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 208,
    label        = "Cds-Cds(Cds-Cdd-Cd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Cs  U0 {1,S}
5   Cdd U0 {3,D} {6,D}
6   C   U0 {5,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1204,
    label        = "Cds-CdsC=SCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   Cd U0 {1,S} {5,D}
4   Cs U0 {1,S}
5   Sd U0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.44,4.73,4.94,5.14,5.48,5.75,6.24],'cal/(mol*K)'),
        H298 = (10.34,'kcal/mol'),
        S298 = (-11.67,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 209,
    label        = "Cds-CdsCdsCds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C       U0 {2,D} {3,S} {4,S}
2   Cd      U0 {1,D}
3   {Cd,CO} U0 {1,S}
4   {Cd,CO} U0 {1,S}
""",
    thermo = u'Cds-Cds(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 210,
    label        = "Cds-Cds(Cds-Od)(Cds-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   CO U0 {1,S}
4   CO U0 {1,S}
""",
    thermo = u'Cds-CdsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 211,
    label        = "Cds-Cds(Cds-Od)(Cds-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   CO U0 {1,S}
4   Cd U0 {1,S}
""",
    thermo = u'Cds-Cds(Cds-Od)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 212,
    label        = "Cds-Cds(Cds-Od)(Cds-Cds)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   CO U0 {1,S}
4   Cd U0 {1,S} {5,D}
5   Cd U0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.7,6.13,6.87,7.1,7.2,7.16,7.06],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (4.6,'kcal/mol','+|-',0.24),
        S298 = (-16.5,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = u"""Cd-COCd from CD/CD2/ jwb est 6/97""",
    longDesc = 
u"""

""",
)

entry(
    index        = 213,
    label        = "Cds-Cds(Cds-Od)(Cds-Cdd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cd  U0 {1,D}
3   CO  U0 {1,S}
4   Cd  U0 {1,S} {5,D}
5   Cdd U0 {4,D}
""",
    thermo = u'Cds-Cds(Cds-Od)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 214,
    label        = "Cds-Cds(Cds-Od)(Cds-Cdd-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cd  U0 {1,D}
3   CO  U0 {1,S}
4   Cd  U0 {1,S} {5,D}
5   Cdd U0 {4,D} {6,D}
6   Od  U0 {5,D}
""",
    thermo = u'Cds-Cds(Cds-Cdd-Od)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 215,
    label        = "Cds-Cds(Cds-Od)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cd  U0 {1,D}
3   CO  U0 {1,S}
4   Cd  U0 {1,S} {5,D}
5   Cdd U0 {4,D} {6,D}
6   C   U0 {5,D}
""",
    thermo = u'Cds-Cds(Cds-Od)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 216,
    label        = "Cds-Cds(Cds-Cd)(Cds-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   Cd U0 {1,S}
4   Cd U0 {1,S}
""",
    thermo = u'Cds-Cds(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 217,
    label        = "Cds-Cds(Cds-Cds)(Cds-Cds)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   Cd U0 {1,S} {5,D}
4   Cd U0 {1,S} {6,D}
5   Cd U0 {3,D}
6   Cd U0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.9,2.69,3.5,4.28,5.57,6.21,7.37],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (4.6,'kcal/mol','+|-',0.24),
        S298 = (-15.67,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = u"""Cd-CdCd Hf=3D est S,Cp mopac nov99""",
    longDesc = 
u"""

""",
)

entry(
    index        = 218,
    label        = "Cds-Cds(Cds-Cds)(Cds-Cdd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Cd  U0 {1,S} {6,D}
5   Cd  U0 {3,D}
6   Cdd U0 {4,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 219,
    label        = "Cds-Cds(Cds-Cds)(Cds-Cdd-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Cd  U0 {1,S} {6,D}
5   Cd  U0 {3,D}
6   Cdd U0 {4,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cds-Cds(Cds-Cdd-Od)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-Cds(Cds-Cds)(Cds-Cdd-Sd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Cd  U0 {1,S} {6,D}
5   Cd  U0 {3,D}
6   Cdd U0 {4,D} {7,D}
7   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 220,
    label        = "Cds-Cds(Cds-Cds)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Cd  U0 {1,S} {6,D}
5   Cd  U0 {3,D}
6   Cdd U0 {4,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 221,
    label        = "Cds-Cds(Cds-Cdd)(Cds-Cdd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Cd  U0 {1,S} {6,D}
5   Cdd U0 {3,D}
6   Cdd U0 {4,D}
""",
    thermo = u'Cds-Cds(Cds-Cdd-Cd)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 222,
    label        = "Cds-Cds(Cds-Cdd-Od)(Cds-Cdd-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Cd  U0 {1,S} {6,D}
5   Cdd U0 {3,D} {7,D}
6   Cdd U0 {4,D} {8,D}
7   Od  U0 {5,D}
8   Od  U0 {6,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 223,
    label        = "Cds-Cds(Cds-Cdd-Od)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Cd  U0 {1,S} {6,D}
5   Cdd U0 {3,D} {7,D}
6   Cdd U0 {4,D} {8,D}
7   Od  U0 {5,D}
8   C   U0 {6,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-Cds(Cds-Cdd-Sd)(Cds-Cdd-Sd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Cd  U0 {1,S} {6,D}
5   Cdd U0 {3,D} {7,D}
6   Cdd U0 {4,D} {8,D}
7   Sd  U0 {5,D}
8   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-Cds(Cds-Cdd-Sd)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Cd  U0 {1,S} {6,D}
5   Cdd U0 {3,D} {7,D}
6   Cdd U0 {4,D} {8,D}
7   Sd  U0 {5,D}
8   C   U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 224,
    label        = "Cds-Cds(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Cd  U0 {1,S} {6,D}
5   Cdd U0 {3,D} {7,D}
6   Cdd U0 {4,D} {8,D}
7   C   U0 {5,D}
8   C   U0 {6,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-CdsC=S(Cds-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   Cd U0 {1,S} {5,D}
4   Cd U0 {1,S}
5   Sd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-CdsC=S(Cds-Cds)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   Cd U0 {1,S} {6,D}
4   Cd U0 {1,S} {5,D}
5   Cd U0 {4,D}
6   Sd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-CdsC=S(Cds-Cdd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cd  U0 {1,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {5,D}
5   Cdd U0 {4,D}
6   Sd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-CdsC=S(Cds-Cdd-Sd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cd  U0 {1,D}
3   Cd  U0 {1,S} {7,D}
4   Cd  U0 {1,S} {5,D}
5   Cdd U0 {4,D} {6,D}
6   Sd  U0 {5,D}
7   Sd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-CdsC=S(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cd  U0 {1,D}
3   Cd  U0 {1,S} {7,D}
4   Cd  U0 {1,S} {5,D}
5   Cdd U0 {4,D} {6,D}
6   C   U0 {5,D}
7   Sd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-CdsC=SC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   Cd U0 {1,S} {5,D}
4   Cd U0 {1,S} {6,D}
5   Sd U0 {3,D}
6   Sd U0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 225,
    label        = "Cds-CdsCtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   Ct U0 {1,S}
4   Cs U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.5,3.88,4.88,4.18,4.86,5.4,6.01],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (8.11,'kcal/mol','+|-',0.24),
        S298 = (-13.02,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = u"""Cd-CtCs RAMAN & GREEN JPCA 2002, 106, 11141-11149""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1858,
    label        = "Cd-CdCs(CtN3t)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cd  U0 {2,D} {5,S} {6,S}
2   Cd  U0 {1,D} {3,S} {4,S}
3   R   U0 {2,S}
4   R   U0 {2,S}
5   Cs  U0 {1,S}
6   Ct  U0 {1,S} {7,T}
7   N3t U0 {6,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.2,10.6,11.7,12.5,13.8,14.7,15.9],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (40.2,'kcal/mol','+|-',1.3),
        S298 = (17.9,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 226,
    label        = "Cds-CdsCtCds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C       U0 {2,D} {3,S} {4,S}
2   Cd      U0 {1,D}
3   Ct      U0 {1,S}
4   {Cd,CO} U0 {1,S}
""",
    thermo = u'Cds-Cds(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 227,
    label        = "Cds-CdsCt(Cds-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   Ct U0 {1,S}
4   CO U0 {1,S}
""",
    thermo = u'Cds-Cds(Cds-Od)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 228,
    label        = "Cds-CdsCt(Cds-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   Ct U0 {1,S}
4   Cd U0 {1,S}
""",
    thermo = u'Cds-Cds(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 229,
    label        = "Cds-Cds(Cds-Cds)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   Cd U0 {1,S} {5,D}
4   Ct U0 {1,S}
5   Cd U0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.89,5.26,5.98,6.37,6.67,6.78,6.89],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (7.54,'kcal/mol','+|-',0.24),
        S298 = (-14.65,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = u"""Cd-CtCd RAMAN & GREEN JPCA 2002, 106, 11141-11149""",
    longDesc = 
u"""

""",
)

entry(
    index        = 230,
    label        = "Cds-Cds(Cds-Cdd)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Ct  U0 {1,S}
5   Cdd U0 {3,D}
""",
    thermo = u'Cds-Cds(Cds-Cdd-Cd)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 231,
    label        = "Cds-Cds(Cds-Cdd-Od)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Ct  U0 {1,S}
5   Cdd U0 {3,D} {6,D}
6   Od  U0 {5,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-Cds(Cds-Cdd-Sd)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Ct  U0 {1,S}
5   Cdd U0 {3,D} {6,D}
6   Sd  U0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 232,
    label        = "Cds-Cds(Cds-Cdd-Cd)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Ct  U0 {1,S}
5   Cdd U0 {3,D} {6,D}
6   C   U0 {5,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-CdsCtC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   Ct U0 {1,S}
4   Cd U0 {1,S} {5,D}
5   Sd U0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 233,
    label        = "Cds-CdsCtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   Ct U0 {1,S}
4   Ct U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.23,4.59,5.41,5.93,6.48,6.74,7.02],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (8.81,'kcal/mol','+|-',0.24),
        S298 = (-13.51,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = u"""Cd-CtCt RAMAN & GREEN JPCA 2002, 106, 11141-11149""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1837,
    label        = "Cds-Cd(CtN3t)(CtN3t)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cd  U0 {2,S} {4,S} {6,D}
2   Ct  U0 {1,S} {3,T}
3   N3t U0 {2,T}
4   Ct  U0 {1,S} {5,T}
5   N3t U0 {4,T}
6   Cd  U0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (84.1,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 234,
    label        = "Cds-CdsCbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   Cb U0 {1,S}
4   Cs U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.4,5.37,5.93,6.18,6.5,6.62,6.72],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (8.64,'kcal/mol','+|-',0.24),
        S298 = (-14.6,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = u"""Cd-CbCs BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index        = 235,
    label        = "Cds-CdsCbCds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C       U0 {2,D} {3,S} {4,S}
2   Cd      U0 {1,D}
3   Cb      U0 {1,S}
4   {Cd,CO} U0 {1,S}
""",
    thermo = u'Cds-Cds(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 236,
    label        = "Cds-CdsCb(Cds-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   Cb U0 {1,S}
4   CO U0 {1,S}
""",
    thermo = u'Cds-Cds(Cds-Od)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 237,
    label        = "Cds-Cds(Cds-Cd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   Cd U0 {1,S}
4   Cb U0 {1,S}
""",
    thermo = u'Cds-Cds(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 238,
    label        = "Cds-Cds(Cds-Cds)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   Cd U0 {1,S} {5,D}
4   Cb U0 {1,S}
5   Cd U0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.7,6.13,6.87,7.1,7.2,7.16,7.06],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (7.18,'kcal/mol','+|-',0.24),
        S298 = (-16.5,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = u"""Cd-CbCd BOZZELLI =3D Cd/Cs/Cb + (Cd/Cs/Cd - Cd/Cs/Cs)""",
    longDesc = 
u"""

""",
)

entry(
    index        = 239,
    label        = "Cds-Cds(Cds-Cdd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Cb  U0 {1,S}
5   Cdd U0 {3,D}
""",
    thermo = u'Cds-Cds(Cds-Cdd-Cd)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 240,
    label        = "Cds-Cds(Cds-Cdd-Od)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Cb  U0 {1,S}
5   Cdd U0 {3,D} {6,D}
6   Od  U0 {5,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-Cds(Cds-Cdd-Sd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Cb  U0 {1,S}
5   Cdd U0 {3,D} {6,D}
6   Sd  U0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 241,
    label        = "Cds-Cds(Cds-Cdd-Cd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cd  U0 {1,D}
3   Cd  U0 {1,S} {5,D}
4   Cb  U0 {1,S}
5   Cdd U0 {3,D} {6,D}
6   C   U0 {5,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-CdsCbC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   Cb U0 {1,S}
4   Cd U0 {1,S} {5,D}
5   Sd U0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 242,
    label        = "Cds-CdsCbCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   Cb U0 {1,S}
4   Ct U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.22,3.14,4.54,4.11,5.06,5.79,6.71],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (6.7,'kcal/mol','+|-',0.24),
        S298 = (-17.04,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = u"""Cd-CbCt Hf=3D est S,Cp mopac nov99""",
    longDesc = 
u"""

""",
)

entry(
    index        = 243,
    label        = "Cds-CdsCbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U0 {2,D} {3,S} {4,S}
2   Cd U0 {1,D}
3   Cb U0 {1,S}
4   Cb U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.7,6.13,6.87,7.1,7.2,7.16,7.06],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (8,'kcal/mol','+|-',0.24),
        S298 = (-16.5,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = u"""Cd-CbCb BOZZELLI =3D Cd/Cs/Cb + (Cd/Cs/Cb - Cd/Cs/Cs)""",
    longDesc = 
u"""

""",
)

entry(
    index        = 244,
    label        = "Cds-CddCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D}
3   Cs  U0 {1,S}
4   Cs  U0 {1,S}
""",
    thermo = u'Cds-(Cdd-Cd)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 245,
    label        = "Cds-(Cdd-Od)CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cs  U0 {1,S}
4   Cs  U0 {1,S}
5   Od  U0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.82,10.74,11.53,13.22,13.46,14.28,15.35],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-1.644,'kcal/mol','+|-',0.24),
        S298 = (20.02,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = u"""{CCO/C2} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cs  U0 {1,S}
4   Cs  U0 {1,S}
5   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 246,
    label        = "Cds-(Cdd-Cd)CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cs  U0 {1,S}
4   Cs  U0 {1,S}
5   C   U0 {2,D}
""",
    thermo = u'Cds-CdsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 247,
    label        = "Cds-CddCdsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C       U0 {2,D} {3,S} {4,S}
2   Cdd     U0 {1,D}
3   {Cd,CO} U0 {1,S}
4   Cs      U0 {1,S}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 248,
    label        = "Cds-(Cdd-Od)(Cds-Od)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   CO  U0 {1,S}
4   Cs  U0 {1,S}
5   Od  U0 {2,D}
""",
    thermo = u'Cds-(Cdd-Od)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 249,
    label        = "Cds-(Cdd-Od)(Cds-Cd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S}
4   Cs  U0 {1,S}
5   Od  U0 {2,D}
""",
    thermo = u'Cds-(Cdd-Od)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 250,
    label        = "Cds-(Cdd-Od)(Cds-Cds)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cs  U0 {1,S}
5   Od  U0 {2,D}
6   Cd  U0 {3,D}
""",
    thermo = u'Cds-(Cdd-Od)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 251,
    label        = "Cds-(Cdd-Od)(Cds-Cdd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cs  U0 {1,S}
5   Od  U0 {2,D}
6   Cdd U0 {3,D}
""",
    thermo = u'Cds-(Cdd-Od)(Cds-Cdd-Cd)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 252,
    label        = "Cds-(Cdd-Od)(Cds-Cdd-Od)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cs  U0 {1,S}
5   Od  U0 {2,D}
6   Cdd U0 {3,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.1,11.24,12.12,12.84,14,14.75,15.72],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-2.07,'kcal/mol','+|-',0.24),
        S298 = (19.65,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = u"""{CCO/C/CCO} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""

""",
)

entry(
    index        = 253,
    label        = "Cds-(Cdd-Od)(Cds-Cdd-Cd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cs  U0 {1,S}
5   Od  U0 {2,D}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cds-(Cdd-Od)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)(Cds-Cd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S}
4   Cs  U0 {1,S}
5   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)(Cds-Cds)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cs  U0 {1,S}
5   Sd  U0 {2,D}
6   Cd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)(Cds-Cdd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cs  U0 {1,S}
5   Sd  U0 {2,D}
6   Cdd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)(Cds-Cdd-Sd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cs  U0 {1,S}
5   Sd  U0 {2,D}
6   Cdd U0 {3,D} {7,D}
7   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)(Cds-Cdd-Cd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cs  U0 {1,S}
5   Sd  U0 {2,D}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 254,
    label        = "Cds-(Cdd-Cd)(Cds-Cd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S}
4   Cs  U0 {1,S}
5   C   U0 {2,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 255,
    label        = "Cds-(Cdd-Cd)(Cds-Cds)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cs  U0 {1,S}
5   C   U0 {2,D}
6   Cd  U0 {3,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 256,
    label        = "Cds-(Cdd-Cd)(Cds-Cdd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cs  U0 {1,S}
5   C   U0 {2,D}
6   Cdd U0 {3,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cdd-Cd)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 257,
    label        = "Cds-(Cdd-Cd)(Cds-Cdd-Od)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cs  U0 {1,S}
5   C   U0 {2,D}
6   Cdd U0 {3,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cds-Cds(Cds-Cdd-Od)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Cd)(Cds-Cdd-Sd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cs  U0 {1,S}
5   C   U0 {2,D}
6   Cdd U0 {3,D} {7,D}
7   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 258,
    label        = "Cds-(Cdd-Cd)(Cds-Cdd-Cd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cs  U0 {1,S}
5   C   U0 {2,D}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)C=SCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cs  U0 {1,S}
5   Sd  U0 {2,D}
6   Sd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 259,
    label        = "Cds-CddCdsCds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C       U0 {2,D} {3,S} {4,S}
2   Cdd     U0 {1,D}
3   {Cd,CO} U0 {1,S}
4   {Cd,CO} U0 {1,S}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 260,
    label        = "Cds-(Cdd-Od)(Cds-Od)(Cds-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   CO  U0 {1,S}
4   CO  U0 {1,S}
5   Od  U0 {2,D}
""",
    thermo = u'Cds-(Cdd-Od)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 261,
    label        = "Cds-(Cdd-Od)(Cds-Cd)(Cds-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S}
4   CO  U0 {1,S}
5   Od  U0 {2,D}
""",
    thermo = u'Cds-(Cdd-Od)(Cds-Cds)(Cds-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 262,
    label        = "Cds-(Cdd-Od)(Cds-Cds)(Cds-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   CO  U0 {1,S}
5   Od  U0 {2,D}
6   Cd  U0 {3,D}
""",
    thermo = u'Cds-(Cdd-Od)(Cds-Od)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 263,
    label        = "Cds-(Cdd-Od)(Cds-Cdd)(Cds-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   CO  U0 {1,S}
5   Od  U0 {2,D}
6   Cdd U0 {3,D}
""",
    thermo = u'Cds-(Cdd-Od)(Cds-Cdd-Cd)(Cds-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 264,
    label        = "Cds-(Cdd-Od)(Cds-Cdd-Od)(Cds-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   CO  U0 {1,S}
5   Od  U0 {2,D}
6   Cdd U0 {3,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cds-(Cdd-Od)(Cds-Cdd-Od)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 265,
    label        = "Cds-(Cdd-Od)(Cds-Cdd-Cd)(Cds-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   CO  U0 {1,S}
5   Od  U0 {2,D}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cds-(Cdd-Od)(Cds-Cds)(Cds-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 266,
    label        = "Cds-(Cdd-Od)(Cds-Cd)(Cds-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S}
4   Cd  U0 {1,S}
5   Od  U0 {2,D}
""",
    thermo = u'Cds-(Cdd-Od)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 267,
    label        = "Cds-(Cdd-Od)(Cds-Cds)(Cds-Cds)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Od  U0 {2,D}
6   Cd  U0 {3,D}
7   Cd  U0 {4,D}
""",
    thermo = u'Cds-(Cdd-Od)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 268,
    label        = "Cds-(Cdd-Od)(Cds-Cdd)(Cds-Cds)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Od  U0 {2,D}
6   Cdd U0 {3,D}
7   Cd  U0 {4,D}
""",
    thermo = u'Cds-(Cdd-Od)(Cds-Cdd-Cd)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 269,
    label        = "Cds-(Cdd-Od)(Cds-Cdd-Od)(Cds-Cds)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Od  U0 {2,D}
6   Cdd U0 {3,D} {8,D}
7   Cd  U0 {4,D}
8   Od  U0 {6,D}
""",
    thermo = u'Cds-(Cdd-Od)(Cds-Cdd-Od)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 270,
    label        = "Cds-(Cdd-Od)(Cds-Cdd-Cd)(Cds-Cds)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Od  U0 {2,D}
6   Cdd U0 {3,D} {8,D}
7   Cd  U0 {4,D}
8   C   U0 {6,D}
""",
    thermo = u'Cds-(Cdd-Od)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 271,
    label        = "Cds-(Cdd-Od)(Cds-Cdd)(Cds-Cdd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Od  U0 {2,D}
6   Cdd U0 {3,D}
7   Cdd U0 {4,D}
""",
    thermo = u'Cds-(Cdd-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 272,
    label        = "Cds-(Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Od  U0 {2,D}
6   Cdd U0 {3,D} {8,D}
7   Cdd U0 {4,D} {9,D}
8   Od  U0 {6,D}
9   Od  U0 {7,D}
""",
    thermo = u'Cds-(Cdd-Od)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 273,
    label        = "Cds-(Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Od  U0 {2,D}
6   Cdd U0 {3,D} {8,D}
7   Cdd U0 {4,D} {9,D}
8   Od  U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = u'Cds-(Cdd-Od)(Cds-Cdd-Od)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 274,
    label        = "Cds-(Cdd-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Od  U0 {2,D}
6   Cdd U0 {3,D} {8,D}
7   Cdd U0 {4,D} {9,D}
8   C   U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = u'Cds-(Cdd-Od)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 275,
    label        = "Cds-(Cdd-Cd)(Cds-Od)(Cds-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   CO  U0 {1,S}
4   CO  U0 {1,S}
5   C   U0 {2,D}
""",
    thermo = u'Cds-Cds(Cds-Od)(Cds-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 276,
    label        = "Cds-(Cdd-Cd)(Cds-Od)(Cds-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   CO  U0 {1,S}
4   Cd  U0 {1,S}
5   C   U0 {2,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Od)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 277,
    label        = "Cds-(Cdd-Cd)(Cds-Od)(Cds-Cds)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   CO  U0 {1,S}
4   Cd  U0 {1,S} {6,D}
5   C   U0 {2,D}
6   Cd  U0 {4,D}
""",
    thermo = u'Cds-Cds(Cds-Od)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 278,
    label        = "Cds-(Cdd-Cd)(Cds-Od)(Cds-Cdd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   CO  U0 {1,S}
4   Cd  U0 {1,S} {6,D}
5   C   U0 {2,D}
6   Cdd U0 {4,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Od)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 279,
    label        = "Cds-(Cdd-Cd)(Cds-Od)(Cds-Cdd-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   CO  U0 {1,S}
4   Cd  U0 {1,S} {6,D}
5   C   U0 {2,D}
6   Cdd U0 {4,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cds-Cds(Cds-Od)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 280,
    label        = "Cds-(Cdd-Cd)(Cds-Od)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   CO  U0 {1,S}
4   Cd  U0 {1,S} {6,D}
5   C   U0 {2,D}
6   Cdd U0 {4,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Od)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)(Cds-Cd)(Cds-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S}
4   Cd  U0 {1,S}
5   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)(Cds-Cds)(Cds-Cds)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Sd  U0 {2,D}
6   Cd  U0 {3,D}
7   Cd  U0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)(Cds-Cdd)(Cds-Cds)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Sd  U0 {2,D}
6   Cdd U0 {3,D}
7   Cd  U0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)(Cds-Cdd-Sd)(Cds-Cds)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Sd  U0 {2,D}
6   Cdd U0 {3,D} {8,D}
7   Cd  U0 {4,D}
8   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)(Cds-Cdd-Cd)(Cds-Cds)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Sd  U0 {2,D}
6   Cdd U0 {3,D} {8,D}
7   Cd  U0 {4,D}
8   C   U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)(Cds-Cdd)(Cds-Cdd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Sd  U0 {2,D}
6   Cdd U0 {3,D}
7   Cdd U0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)(Cds-Cdd-Sd)(Cds-Cdd-Sd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Sd  U0 {2,D}
6   Cdd U0 {3,D} {8,D}
7   Cdd U0 {4,D} {9,D}
8   Sd  U0 {6,D}
9   Sd  U0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)(Cds-Cdd-Sd)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Sd  U0 {2,D}
6   Cdd U0 {3,D} {8,D}
7   Cdd U0 {4,D} {9,D}
8   Sd  U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Sd  U0 {2,D}
6   Cdd U0 {3,D} {8,D}
7   Cdd U0 {4,D} {9,D}
8   C   U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 281,
    label        = "Cds-(Cdd-Cd)(Cds-Cd)(Cds-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S}
4   Cd  U0 {1,S}
5   C   U0 {2,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 282,
    label        = "Cds-(Cdd-Cd)(Cds-Cds)(Cds-Cds)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   C   U0 {2,D}
6   Cd  U0 {3,D}
7   Cd  U0 {4,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 283,
    label        = "Cds-(Cdd-Cd)(Cds-Cdd)(Cds-Cds)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   C   U0 {2,D}
6   Cdd U0 {3,D}
7   Cd  U0 {4,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 284,
    label        = "Cds-(Cdd-Cd)(Cds-Cdd-Od)(Cds-Cds)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   C   U0 {2,D}
6   Cdd U0 {3,D} {8,D}
7   Cd  U0 {4,D}
8   Od  U0 {6,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Cd)(Cds-Cdd-Sd)(Cds-Cds)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   C   U0 {2,D}
6   Cdd U0 {3,D} {8,D}
7   Cd  U0 {4,D}
8   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 285,
    label        = "Cds-(Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cds)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   C   U0 {2,D}
6   Cdd U0 {3,D} {8,D}
7   Cd  U0 {4,D}
8   C   U0 {6,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 286,
    label        = "Cds-(Cdd-Cd)(Cds-Cdd)(Cds-Cdd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   C   U0 {2,D}
6   Cdd U0 {3,D}
7   Cdd U0 {4,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 287,
    label        = "Cds-(Cdd-Cd)(Cds-Cdd-Od)(Cds-Cdd-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   C   U0 {2,D}
6   Cdd U0 {3,D} {8,D}
7   Cdd U0 {4,D} {9,D}
8   Od  U0 {6,D}
9   Od  U0 {7,D}
""",
    thermo = u'Cds-Cds(Cds-Cdd-Od)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 288,
    label        = "Cds-(Cdd-Cd)(Cds-Cdd-Od)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   C   U0 {2,D}
6   Cdd U0 {3,D} {8,D}
7   Cdd U0 {4,D} {9,D}
8   Od  U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cdd-Od)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Cd)(Cds-Cdd-Sd)(Cds-Cdd-Sd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   C   U0 {2,D}
6   Cdd U0 {3,D} {8,D}
7   Cdd U0 {4,D} {9,D}
8   Sd  U0 {6,D}
9   Sd  U0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Cd)(Cds-Cdd-Sd)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   C   U0 {2,D}
6   Cdd U0 {3,D} {8,D}
7   Cdd U0 {4,D} {9,D}
8   Sd  U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 289,
    label        = "Cds-(Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   C   U0 {2,D}
6   Cdd U0 {3,D} {8,D}
7   Cdd U0 {4,D} {9,D}
8   C   U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)(Cds-Cd)C=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S}
4   Cd  U0 {1,S} {6,D}
5   Sd  U0 {2,D}
6   Sd  U0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)(Cds-Cds)C=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Sd  U0 {2,D}
6   Cd  U0 {3,D}
7   Sd  U0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)(Cds-Cdd)C=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Sd  U0 {2,D}
6   Cdd U0 {3,D}
7   Sd  U0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)(Cds-Cdd-Sd)C=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {8,D}
5   Sd  U0 {2,D}
6   Cdd U0 {3,D} {7,D}
7   Sd  U0 {6,D}
8   Sd  U0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)(Cds-Cdd-Cd)C=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {8,D}
5   Sd  U0 {2,D}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
8   Sd  U0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Cd)C=S(Cds-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S}
5   C   U0 {2,D}
6   Sd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Cd)C=S(Cds-Cds)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {7,D}
4   Cd  U0 {1,S} {6,D}
5   C   U0 {2,D}
6   Cd  U0 {4,D}
7   Sd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Cd)C=S(Cds-Cdd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {7,D}
4   Cd  U0 {1,S} {6,D}
5   C   U0 {2,D}
6   Cdd U0 {4,D}
7   Sd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Cd)C=S(Cds-Cdd-Sd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {8,D}
4   Cd  U0 {1,S} {6,D}
5   C   U0 {2,D}
6   Cdd U0 {4,D} {7,D}
7   Sd  U0 {6,D}
8   Sd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Cd)C=S(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {8,D}
4   Cd  U0 {1,S} {6,D}
5   C   U0 {2,D}
6   Cdd U0 {4,D} {7,D}
7   C   U0 {6,D}
8   Sd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)C=SC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Sd  U0 {2,D}
6   Sd  U0 {3,D}
7   Sd  U0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Cd)C=SC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   C   U0 {2,D}
6   Sd  U0 {3,D}
7   Sd  U0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 290,
    label        = "Cds-CddCtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D}
3   Ct  U0 {1,S}
4   Cs  U0 {1,S}
""",
    thermo = u'Cds-(Cdd-Cd)CtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 291,
    label        = "Cds-(Cdd-Od)CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Ct  U0 {1,S}
4   Cs  U0 {1,S}
5   Od  U0 {2,D}
""",
    thermo = u'Cds-(Cdd-Od)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Ct  U0 {1,S}
4   Cs  U0 {1,S}
5   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 292,
    label        = "Cds-(Cdd-Cd)CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Ct  U0 {1,S}
4   Cs  U0 {1,S}
5   C   U0 {2,D}
""",
    thermo = u'Cds-CdsCtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 293,
    label        = "Cds-CddCtCds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C       U0 {2,D} {3,S} {4,S}
2   Cdd     U0 {1,D}
3   Ct      U0 {1,S}
4   {Cd,CO} U0 {1,S}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 294,
    label        = "Cds-(Cdd-Od)(Cds-Od)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   CO  U0 {1,S}
4   Ct  U0 {1,S}
5   Od  U0 {2,D}
""",
    thermo = u'Cds-(Cdd-Od)(Cds-Cds)(Cds-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 295,
    label        = "Cds-(Cdd-Od)(Cds-Cd)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S}
4   Ct  U0 {1,S}
5   Od  U0 {2,D}
""",
    thermo = u'Cds-(Cdd-Od)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 296,
    label        = "Cds-(Cdd-Od)(Cds-Cds)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Ct  U0 {1,S}
5   Od  U0 {2,D}
6   Cd  U0 {3,D}
""",
    thermo = u'Cds-(Cdd-Od)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 297,
    label        = "Cds-(Cdd-Od)(Cds-Cdd)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Ct  U0 {1,S}
5   Od  U0 {2,D}
6   Cdd U0 {3,D}
""",
    thermo = u'Cds-(Cdd-Od)(Cds-Cdd-Cd)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 298,
    label        = "Cds-(Cdd-Od)(Cds-Cdd-Od)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Ct  U0 {1,S}
5   Od  U0 {2,D}
6   Cdd U0 {3,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cds-(Cdd-Od)(Cds-Cdd-Od)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 299,
    label        = "Cds-(Cdd-Od)(Cds-Cdd-Cd)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Ct  U0 {1,S}
5   Od  U0 {2,D}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cds-(Cdd-Od)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)(Cds-Cd)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S}
4   Ct  U0 {1,S}
5   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)(Cds-Cds)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Ct  U0 {1,S}
5   Sd  U0 {2,D}
6   Cd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)(Cds-Cdd)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Ct  U0 {1,S}
5   Sd  U0 {2,D}
6   Cdd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)(Cds-Cdd-Sd)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Ct  U0 {1,S}
5   Sd  U0 {2,D}
6   Cdd U0 {3,D} {7,D}
7   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)(Cds-Cdd-Cd)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Ct  U0 {1,S}
5   Sd  U0 {2,D}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 300,
    label        = "Cds-(Cdd-Cd)(Cds-Cd)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S}
4   Ct  U0 {1,S}
5   C   U0 {2,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 301,
    label        = "Cds-(Cdd-Cd)(Cds-Cds)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Ct  U0 {1,S}
5   C   U0 {2,D}
6   Cd  U0 {3,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 302,
    label        = "Cds-(Cdd-Cd)(Cds-Cdd)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Ct  U0 {1,S}
5   C   U0 {2,D}
6   Cdd U0 {3,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cdd-Cd)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 303,
    label        = "Cds-(Cdd-Cd)(Cds-Cdd-Od)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Ct  U0 {1,S}
5   C   U0 {2,D}
6   Cdd U0 {3,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cds-Cds(Cds-Cdd-Od)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Cd)(Cds-Cdd-Sd)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Ct  U0 {1,S}
5   C   U0 {2,D}
6   Cdd U0 {3,D} {7,D}
7   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 304,
    label        = "Cds-(Cdd-Cd)(Cds-Cdd-Cd)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Ct  U0 {1,S}
5   C   U0 {2,D}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)C=SCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Ct  U0 {1,S}
5   Sd  U0 {2,D}
6   Sd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 305,
    label        = "Cds-CddCtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D}
3   Ct  U0 {1,S}
4   Ct  U0 {1,S}
""",
    thermo = u'Cds-(Cdd-Cd)CtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 306,
    label        = "Cds-(Cdd-Od)CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Ct  U0 {1,S}
4   Ct  U0 {1,S}
5   Od  U0 {2,D}
""",
    thermo = u'Cds-(Cdd-Od)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Ct  U0 {1,S}
4   Ct  U0 {1,S}
5   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 307,
    label        = "Cds-(Cdd-Cd)CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Ct  U0 {1,S}
4   Ct  U0 {1,S}
5   C   U0 {2,D}
""",
    thermo = u'Cds-CdsCtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 308,
    label        = "Cds-CddCbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D}
3   Cb  U0 {1,S}
4   Cs  U0 {1,S}
""",
    thermo = u'Cds-(Cdd-Cd)CbCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 309,
    label        = "Cds-(Cdd-Od)CbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cb  U0 {1,S}
4   Cs  U0 {1,S}
5   Od  U0 {2,D}
""",
    thermo = u'Cds-(Cdd-Od)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)CbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cb  U0 {1,S}
4   Cs  U0 {1,S}
5   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 310,
    label        = "Cds-(Cdd-Cd)CbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cb  U0 {1,S}
4   Cs  U0 {1,S}
5   C   U0 {2,D}
""",
    thermo = u'Cds-CdsCbCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 311,
    label        = "Cds-CddCbCds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C       U0 {2,D} {3,S} {4,S}
2   Cdd     U0 {1,D}
3   Cb      U0 {1,S}
4   {Cd,CO} U0 {1,S}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 312,
    label        = "Cds-(Cdd-Od)(Cds-Od)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   CO  U0 {1,S}
4   Cb  U0 {1,S}
5   Od  U0 {2,D}
""",
    thermo = u'Cds-(Cdd-Od)(Cds-Cds)(Cds-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 313,
    label        = "Cds-(Cdd-Od)(Cds-Cd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S}
4   Cb  U0 {1,S}
5   Od  U0 {2,D}
""",
    thermo = u'Cds-(Cdd-Od)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 314,
    label        = "Cds-(Cdd-Od)(Cds-Cds)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cb  U0 {1,S}
5   Od  U0 {2,D}
6   Cd  U0 {3,D}
""",
    thermo = u'Cds-(Cdd-Od)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 315,
    label        = "Cds-(Cdd-Od)(Cds-Cdd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cb  U0 {1,S}
5   Od  U0 {2,D}
6   Cdd U0 {3,D}
""",
    thermo = u'Cds-(Cdd-Od)(Cds-Cdd-Cd)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 316,
    label        = "Cds-(Cdd-Od)(Cds-Cdd-Od)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cb  U0 {1,S}
5   Od  U0 {2,D}
6   Cdd U0 {3,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cds-(Cdd-Od)(Cds-Cdd-Od)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 317,
    label        = "Cds-(Cdd-Od)(Cds-Cdd-Cd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cb  U0 {1,S}
5   Od  U0 {2,D}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cds-(Cdd-Od)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)(Cds-Cd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S}
4   Cb  U0 {1,S}
5   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)(Cds-Cds)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cb  U0 {1,S}
5   Sd  U0 {2,D}
6   Cd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)(Cds-Cdd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cb  U0 {1,S}
5   Sd  U0 {2,D}
6   Cdd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)(Cds-Cdd-Sd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cb  U0 {1,S}
5   Sd  U0 {2,D}
6   Cdd U0 {3,D} {7,D}
7   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)(Cds-Cdd-Cd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cb  U0 {1,S}
5   Sd  U0 {2,D}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 318,
    label        = "Cds-(Cdd-Cd)(Cds-Cd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S}
4   Cb  U0 {1,S}
5   C   U0 {2,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 319,
    label        = "Cds-(Cdd-Cd)(Cds-Cds)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cb  U0 {1,S}
5   C   U0 {2,D}
6   Cd  U0 {3,D}
""",
    thermo = u'Cds-Cds(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 320,
    label        = "Cds-(Cdd-Cd)(Cds-Cdd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cb  U0 {1,S}
5   C   U0 {2,D}
6   Cdd U0 {3,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cdd-Cd)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 321,
    label        = "Cds-(Cdd-Cd)(Cds-Cdd-Od)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cb  U0 {1,S}
5   C   U0 {2,D}
6   Cdd U0 {3,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cds-Cds(Cds-Cdd-Od)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Cd)(Cds-Cdd-Sd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cb  U0 {1,S}
5   C   U0 {2,D}
6   Cdd U0 {3,D} {7,D}
7   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 322,
    label        = "Cds-(Cdd-Cd)(Cds-Cdd-Cd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cb  U0 {1,S}
5   C   U0 {2,D}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cds-(Cdd-Cd)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)C=SCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cd  U0 {1,S} {6,D}
4   Cb  U0 {1,S}
5   Sd  U0 {2,D}
6   Sd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 323,
    label        = "Cds-CddCbCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D}
3   Cb  U0 {1,S}
4   Ct  U0 {1,S}
""",
    thermo = u'Cds-(Cdd-Cd)CbCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 324,
    label        = "Cds-(Cdd-Od)CbCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cb  U0 {1,S}
4   Ct  U0 {1,S}
5   Od  U0 {2,D}
""",
    thermo = u'Cds-(Cdd-Od)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)CbCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cb  U0 {1,S}
4   Ct  U0 {1,S}
5   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 325,
    label        = "Cds-(Cdd-Cd)CbCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cb  U0 {1,S}
4   Ct  U0 {1,S}
5   C   U0 {2,D}
""",
    thermo = u'Cds-CdsCbCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 326,
    label        = "Cds-CddCbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D}
3   Cb  U0 {1,S}
4   Cb  U0 {1,S}
""",
    thermo = u'Cds-(Cdd-Cd)CbCb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 327,
    label        = "Cds-(Cdd-Od)CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cb  U0 {1,S}
4   Cb  U0 {1,S}
5   Od  U0 {2,D}
""",
    thermo = u'Cds-(Cdd-Od)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cds-(Cdd-Sd)CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cb  U0 {1,S}
4   Cb  U0 {1,S}
5   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 328,
    label        = "Cds-(Cdd-Cd)CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C   U0 {2,D} {3,S} {4,S}
2   Cdd U0 {1,D} {5,D}
3   Cb  U0 {1,S}
4   Cb  U0 {1,S}
5   C   U0 {2,D}
""",
    thermo = u'Cds-CdsCbCb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1923,
    label        = "Cds-CNH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cd U0 {2,D} {3,S} {4,S}
2   C  U0 {1,D}
3   N  U0 {1,S}
4   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1860,
    label        = "Cd-CdHN3s",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cd  U0 {2,D} {5,S} {6,S}
2   Cd  U0 {1,D} {3,S} {4,S}
3   R   U0 {2,S}
4   R   U0 {2,S}
5   H   U0 {1,S}
6   N3s U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.7,6,7,7.7,8.8,9.5,10.6],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (2.2,'kcal/mol','+|-',1.4),
        S298 = (7.1,'cal/(mol*K)','+|-',1.3),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1838,
    label        = "Cd-CdH(N5dOdOs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cd  U0 {2,D} {5,S} {8,S}
2   Cd  U0 {1,D} {3,S} {4,S}
3   R   U0 {2,S}
4   R   U0 {2,S}
5   N5d U0 {1,S} {6,D} {7,S}
6   Od  U0 {5,D}
7   Os  U0 {5,S}
8   H   U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.7,15.4,17.6,19.3,21.7,23.1,25],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (2,'kcal/mol','+|-',1.3),
        S298 = (44.3,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1924,
    label        = "Cds-CCN",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cd U0 {2,D} {3,S} {4,S}
2   C  U0 {1,D}
3   C  U0 {1,S}
4   N  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1859,
    label        = "Cd-CdCsN3s",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cd  U0 {2,D} {5,S} {6,S}
2   Cd  U0 {1,D} {3,S} {4,S}
3   R   U0 {2,S}
4   R   U0 {2,S}
5   Cs  U0 {1,S}
6   N3s U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.8,5,5.9,6.4,6.9,7.1,7.2],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (3.5,'kcal/mol','+|-',1.4),
        S298 = (-14.1,'cal/(mol*K)','+|-',1.3),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1861,
    label        = "Cd-CdCs(N5dOdOs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cd  U0 {2,D} {5,S} {8,S}
2   Cd  U0 {1,D} {3,S} {4,S}
3   R   U0 {2,S}
4   R   U0 {2,S}
5   N5d U0 {1,S} {6,D} {7,S}
6   Od  U0 {5,D}
7   Os  U0 {5,S}
8   Cs  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.1,14.3,16.1,17.5,19.3,20.3,21.4],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (2.3,'kcal/mol','+|-',1.3),
        S298 = (24,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 329,
    label        = "Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0
""",
    thermo = u'Cs-CsCsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1919,
    label        = "Cs-NHHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   N  U0 {1,S}
3   H  U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1800,
    label        = "Cs-N3sHHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   N3s U0 {1,S}
3   H   U0 {1,S}
4   H   U0 {1,S}
5   H   U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.19,7.84,9.4,10.79,13.02,14.77,17.58],'cal/(mol*K)'),
        H298 = (-10.08,'kcal/mol'),
        S298 = (30.41,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1920,
    label        = "Cs-N3dHHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   N3d U0 {1,S}
3   H   U0 {1,S}
4   H   U0 {1,S}
5   H   U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1870,
    label        = "Cs-(N3dCd)HHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs       U0 {2,S} {4,S} {5,S} {6,S}
2   N3d      U0 {1,S} {3,D}
3   {Cd,Cdd} U0 {2,D}
4   H        U0 {1,S}
5   H        U0 {1,S}
6   H        U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6,7.7,9.3,10.7,13.1,14.8,17.7],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-5.7,'kcal/mol','+|-',1.3),
        S298 = (30.4,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1801,
    label        = "Cs-(N3dN3d)HHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {4,S} {5,S} {6,S}
2   N3d U0 {1,S} {3,D}
3   N3d U0 {2,D}
4   H   U0 {1,S}
5   H   U0 {1,S}
6   H   U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6,7.8,9.4,10.8,13.1,14.8,17.6],'cal/(mol*K)','+|-',[0.6,0.6,0.6,0.6,0.6,0.6,0.6]),
        H298 = (-9,'kcal/mol','+|-',0.8),
        S298 = (30.2,'cal/(mol*K)','+|-',0.8),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1921,
    label        = "Cs-NCsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   N  U0 {1,S}
3   Cs U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1802,
    label        = "Cs-N3sCsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   N3s U0 {1,S}
3   Cs  U0 {1,S}
4   H   U0 {1,S}
5   H   U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.25,6.9,8.28,9.39,11.09,12.34,14.8],'cal/(mol*K)'),
        H298 = (-6.6,'kcal/mol'),
        S298 = (9.8,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1925,
    label        = "Cs-N3dCHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   N3d U0 {1,S}
3   C   U0 {1,S}
4   H   U0 {1,S}
5   H   U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1805,
    label        = "Cs-(N3dN3d)CsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {4,S} {5,S} {6,S}
2   N3d U0 {1,S} {3,D}
3   N3d U0 {2,D}
4   Cs  U0 {1,S}
5   H   U0 {1,S}
6   H   U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.3,6.9,8.3,9.4,11.1,12.3,14.2],'cal/(mol*K)','+|-',[0.6,0.6,0.6,0.6,0.6,0.6,0.6]),
        H298 = (-5.5,'kcal/mol','+|-',0.8),
        S298 = (9.4,'cal/(mol*K)','+|-',0.8),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1869,
    label        = "Cs-(N3dOd)CHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {4,S} {5,S} {6,S}
2   N3d U0 {1,S} {3,D}
3   Od  U0 {2,D}
4   C   U0 {1,S}
5   H   U0 {1,S}
6   H   U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.8,13.6,15.2,16.7,18.9,20.5,23],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (21.4,'kcal/mol','+|-',1.3),
        S298 = (44.3,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1871,
    label        = "Cs-(N3dCd)CsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {4,S} {5,S} {6,S}
2   N3d U0 {1,S} {3,D}
3   Cd  U0 {2,D}
4   Cs  U0 {1,S}
5   H   U0 {1,S}
6   H   U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.3,7.2,8.7,9.8,11.6,12.8,14.7],'cal/(mol*K)','+|-',[1.2,1.2,1.2,1.2,1.2,1.2,1.2]),
        H298 = (-2.9,'kcal/mol','+|-',1.7),
        S298 = (8.6,'cal/(mol*K)','+|-',1.6),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1926,
    label        = "Cs-N5dCsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   N5d U0 {1,S}
3   Cs  U0 {1,S}
4   H   U0 {1,S}
5   H   U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1841,
    label        = "Cs-(N5dOdOs)CsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {5,S} {6,S} {7,S}
2   N5d U0 {1,S} {3,D} {4,S}
3   Od  U0 {2,D}
4   Os  U0 {2,S}
5   Cs  U0 {1,S}
6   H   U0 {1,S}
7   H   U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.9,15.8,18.3,20.3,23.3,25.4,28.3],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-14.8,'kcal/mol','+|-',1.3),
        S298 = (48.9,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1927,
    label        = "Cs-NCsCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   N  U0 {1,S}
3   Cs U0 {1,S}
4   Cs U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1803,
    label        = "Cs-N3sCsCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   N3s U0 {1,S}
3   Cs  U0 {1,S}
4   Cs  U0 {1,S}
5   H   U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.67,6.32,7.64,8.39,9.56,10.23,11.905],'cal/(mol*K)'),
        H298 = (-5.2,'kcal/mol'),
        S298 = (-11.7,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1928,
    label        = "Cs-N3dCsCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   N3d U0 {1,S}
3   Cs  U0 {1,S}
4   Cs  U0 {1,S}
5   H   U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1806,
    label        = "Cs-(N3dN3d)CsCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {4,S} {5,S} {6,S}
2   N3d U0 {1,S} {3,S}
3   N3d U0 {2,S}
4   Cs  U0 {1,S}
5   Cs  U0 {1,S}
6   H   U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (-3.3,'kcal/mol'),
        S298 = (-11.7,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1868,
    label        = "Cs-(N3dOd)CsCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {4,S} {5,S} {6,S}
2   N3d U0 {1,S} {3,D}
3   Od  U0 {2,D}
4   Cs  U0 {1,S}
5   Cs  U0 {1,S}
6   H   U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.2,12.7,14,15.1,16.8,17.9,19.5],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (23.4,'kcal/mol','+|-',1.3),
        S298 = (23.1,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1929,
    label        = "Cs-N5dCsCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   N5d U0 {1,S}
3   Cs  U0 {1,S}
4   Cs  U0 {1,S}
5   H   U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1842,
    label        = "Cs-(N5dOdOs)CsCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {5,S} {6,S} {7,S}
2   N5d U0 {1,S} {3,D} {4,S}
3   Od  U0 {2,D}
4   Os  U0 {2,S}
5   Cs  U0 {1,S}
6   Cs  U0 {1,S}
7   H   U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.6,16.1,18.1,19.6,21.8,23.2,25.1],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-13.9,'kcal/mol','+|-',1.3),
        S298 = (27.5,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1930,
    label        = "Cs-NCsCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   N  U0 {1,S}
3   Cs U0 {1,S}
4   Cs U0 {1,S}
5   Cs U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1804,
    label        = "Cs-N3sCsCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   N3s U0 {1,S}
3   Cs  U0 {1,S}
4   Cs  U0 {1,S}
5   Cs  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.35,6.16,7.31,7.91,8.49,8.5,8.525],'cal/(mol*K)'),
        H298 = (-3.2,'kcal/mol'),
        S298 = (-34.1,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1931,
    label        = "Cs-N3dCsCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   N3d U0 {1,S}
3   Cs  U0 {1,S}
4   Cs  U0 {1,S}
5   Cs  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1807,
    label        = "Cs-(N3dN3d)CsCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {4,S} {5,S} {6,S}
2   N3d U0 {1,S} {3,S}
3   N3d U0 {2,S}
4   Cs  U0 {1,S}
5   Cs  U0 {1,S}
6   Cs  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (-1.9,'kcal/mol'),
        S298 = (-34.7,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1867,
    label        = "Cs-(N3dOd)CsCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {4,S} {5,S} {6,S}
2   N3d U0 {1,S} {3,D}
3   Od  U0 {2,D}
4   Cs  U0 {1,S}
5   Cs  U0 {1,S}
6   Cs  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.2,13.3,14,14.5,15.3,15.7,16.2],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (24.1,'kcal/mol','+|-',1.3),
        S298 = (1.2,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1932,
    label        = "Cs-N5dCsCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   N5d U0 {1,S}
3   Cs  U0 {1,S}
4   Cs  U0 {1,S}
5   Cs  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1843,
    label        = "Cs-(N5dOdOs)CsCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {5,S} {6,S} {7,S}
2   N5d U0 {1,S} {3,D} {4,S}
3   Od  U0 {2,D}
4   Os  U0 {2,S}
5   Cs  U0 {1,S}
6   Cs  U0 {1,S}
7   Cs  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.5,16,17.8,18.9,20.3,21.1,21.9],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-12.7,'kcal/mol','+|-',1.3),
        S298 = (5.2,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1933,
    label        = "Cs-NNCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   N  U0 {1,S}
3   N  U0 {1,S}
4   Cs U0 {1,S}
5   Cs U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1934,
    label        = "Cs-N5dN5dCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   N5d U0 {1,S}
3   N5d U0 {1,S}
4   Cs  U0 {1,S}
5   Cs  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1846,
    label        = "Cs-(N5dOdOs)(N5dOdOs)CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {5,S} {8,S} {9,S}
2   N5d U0 {1,S} {3,D} {4,S}
3   Od  U0 {2,D}
4   Os  U0 {2,S}
5   N5d U0 {1,S} {6,D} {7,S}
6   Od  U0 {5,D}
7   Os  U0 {5,S}
8   Cs  U0 {1,S}
9   H   U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (-14.9,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 330,
    label        = "Cs-HHHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   H  U0 {1,S}
3   H  U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.43,9.84,11.14,12.41,15,17.25,20.63],'cal/(mol*K)','+|-',[0.06,0.06,0.06,0.06,0.06,0.06,0.06]),
        H298 = (-17.9,'kcal/mol','+|-',0.1),
        S298 = (49.41,'cal/(mol*K)','+|-',0.05),
    ),
    shortDesc = u"""CHEMKIN DATABASE S(group) = S(CH4) + Rln(12)""",
    longDesc = 
u"""

""",
)

entry(
    index        = 331,
    label        = "Cs-CHHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   C  U0 {1,S}
3   H  U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-CsHHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 332,
    label        = "Cs-CsHHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cs U0 {1,S}
3   H  U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.19,7.84,9.4,10.79,13.02,14.77,17.58],'cal/(mol*K)','+|-',[0.08,0.08,0.08,0.08,0.08,0.08,0.08]),
        H298 = (-10.2,'kcal/mol','+|-',0.12),
        S298 = (30.41,'cal/(mol*K)','+|-',0.08),
    ),
    shortDesc = u"""Cs-CsHHH BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index        = 333,
    label        = "Cs-CdsHHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   {Cd,CO} U0 {1,S}
3   H       U0 {1,S}
4   H       U0 {1,S}
5   H       U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)HHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 334,
    label        = "Cs-(Cds-Od)HHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   H  U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.19,7.84,9.4,10.79,13.02,14.77,17.58],'cal/(mol*K)','+|-',[0.04,0.04,0.04,0.04,0.04,0.04,0.04]),
        H298 = (-10.08,'kcal/mol','+|-',0.08),
        S298 = (30.41,'cal/(mol*K)','+|-',0.04),
    ),
    shortDesc = u"""Cs-COHHH BENSON: Cp1500 =3D Cp1000*(Cp1500/Cp1000: C/Cd/H3)""",
    longDesc = 
u"""

""",
)

entry(
    index        = 335,
    label        = "Cs-(Cds-Cd)HHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   H  U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)HHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1862,
    label        = "Cs-(CdN3d)HHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   H   U0 {1,S}
3   H   U0 {1,S}
4   H   U0 {1,S}
5   Cd  U0 {1,S} {6,D}
6   N3d U0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.2,7.8,9.4,10.8,13,14.8,17.6],'cal/(mol*K)'),
        H298 = (-10.2,'kcal/mol'),
        S298 = (30.4,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 336,
    label        = "Cs-(Cds-Cds)HHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   H  U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.19,7.84,9.4,10.79,13.02,14.77,17.58],'cal/(mol*K)','+|-',[0.04,0.04,0.04,0.04,0.04,0.04,0.04]),
        H298 = (-10.2,'kcal/mol','+|-',0.08),
        S298 = (30.41,'cal/(mol*K)','+|-',0.04),
    ),
    shortDesc = u"""Cs-CdHHH BENSON (Assigned Cs-CsHHH)""",
    longDesc = 
u"""

""",
)

entry(
    index        = 337,
    label        = "Cs-(Cds-Cdd)HHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   H   U0 {1,S}
4   H   U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)HHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 338,
    label        = "Cs-(Cds-Cdd-Od)HHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   H   U0 {1,S}
4   H   U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.19,7.84,9.4,10.79,13.02,14.77,17.58],'cal/(mol*K)','+|-',[0.04,0.04,0.04,0.04,0.04,0.04,0.04]),
        H298 = (-10.08,'kcal/mol','+|-',0.08),
        S298 = (30.41,'cal/(mol*K)','+|-',0.04),
    ),
    shortDesc = u"""{CCO/C/H3} RAMAN & GREEN JPCA 2002, 106, 7937-7949, assigened same value as Cs-CsHHH""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)HHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   H   U0 {1,S}
4   H   U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 339,
    label        = "Cs-(Cds-Cdd-Cd)HHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   H   U0 {1,S}
4   H   U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)HHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1176,
    label        = "Cs-C=SHHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   H  U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.96,7.6,9.13,10.49,12.72,14.46,17.28],'cal/(mol*K)'),
        H298 = (-10.25,'kcal/mol'),
        S298 = (30.4,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 340,
    label        = "Cs-CtHHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Ct U0 {1,S}
3   H  U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.19,7.84,9.4,10.79,13.02,14.77,17.58],'cal/(mol*K)','+|-',[0.08,0.08,0.08,0.08,0.08,0.08,0.08]),
        H298 = (-10.2,'kcal/mol','+|-',0.15),
        S298 = (30.41,'cal/(mol*K)','+|-',0.08),
    ),
    shortDesc = u"""Cs-CtHHH BENSON (Assigned Cs-CsHHH)""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1863,
    label        = "Cs-(CtN3t)HHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {4,S} {5,S} {6,S}
2   Ct  U0 {1,S} {3,T}
3   N3t U0 {2,T}
4   H   U0 {1,S}
5   H   U0 {1,S}
6   H   U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.5,14.6,16.6,18.3,21.1,23.4,26.9],'cal/(mol*K)','+|-',[1.3,1.3,1.3,1.3,1.3,1.3,1.3]),
        H298 = (17.7,'kcal/mol','+|-',1.9),
        S298 = (60.2,'cal/(mol*K)','+|-',1.7),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 341,
    label        = "Cs-CbHHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   H  U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.19,7.84,9.4,10.79,13.02,14.77,17.58],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-10.2,'kcal/mol','+|-',0.18),
        S298 = (30.41,'cal/(mol*K)','+|-',0.14),
    ),
    shortDesc = u"""Cs-CbHHH BENSON (Assigned Cs-CsHHH)""",
    longDesc = 
u"""

""",
)

entry(
    index        = 342,
    label        = "Cs-OsHHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Os U0 {1,S}
3   H  U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.19,7.84,9.4,10.79,13.03,14.77,17.58],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-10.1,'kcal/mol','+|-',0.2),
        S298 = (30.41,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cs-OHHH BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index        = 343,
    label        = "Cs-OsOsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Os U0 {1,S}
3   Os U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.5,6.95,8.25,9.35,11.07,12.34,12.34],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-15.23,'kcal/mol','+|-',0.2),
        S298 = (9.42,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cs-OOHH PEDLEY Hf, BOZZELLI C/C2/H2 !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index        = 344,
    label        = "Cs-OsOsOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Os U0 {1,S}
3   Os U0 {1,S}
4   Os U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.54,6,7.17,8.05,9.31,10.05,10.05],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-21.23,'kcal/mol','+|-',0.2),
        S298 = (-12.07,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cs-OOOH BOZZELLI del C/C2/O - C/C3/O, series !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1451,
    label        = "Cs-OsSsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Os U0 {1,S}
3   Ss U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.55,8.91,8.5,7.79,6.37,5.31,3.93],'cal/(mol*K)'),
        H298 = (-9.05,'kcal/mol'),
        S298 = (6.82,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 1DHR CAC""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1459,
    label        = "Cs-OsOsSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Os U0 {1,S}
3   Os U0 {1,S}
4   Ss U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.29,8.57,9.99,10.79,11.56,11.96,12.58],'cal/(mol*K)'),
        H298 = (-18.46,'kcal/mol'),
        S298 = (-14.64,'cal/(mol*K)'),
    ),
    shortDesc = u"""CAC calc 1D-HR""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1162,
    label        = "Cs-SsHHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Ss U0 {1,S}
3   H  U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.96,7.6,9.13,10.49,12.72,14.46,17.28],'cal/(mol*K)'),
        H298 = (-10.25,'kcal/mol'),
        S298 = (30.4,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1167,
    label        = "Cs-SsSsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Ss U0 {1,S}
3   Ss U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.37,9.7,10.52,11.13,12.16,13.01,14.43],'cal/(mol*K)'),
        H298 = (-6.21,'kcal/mol'),
        S298 = (6.14,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1201,
    label        = "Cs-SsSsSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Ss U0 {1,S}
3   Ss U0 {1,S}
4   Ss U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.84,9.14,10.24,10.73,11.12,11.33,11.57],'cal/(mol*K)'),
        H298 = (-2.78,'kcal/mol'),
        S298 = (-15.38,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 345,
    label        = "Cs-CCHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   C  U0 {1,S}
3   C  U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-CsCsHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 346,
    label        = "Cs-CsCsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cs U0 {1,S}
3   Cs U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.5,6.95,8.25,9.35,11.07,12.34,14.25],'cal/(mol*K)','+|-',[0.04,0.04,0.04,0.04,0.04,0.04,0.04]),
        H298 = (-4.93,'kcal/mol','+|-',0.05),
        S298 = (9.42,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = u"""Cs-CsCsHH BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index        = 347,
    label        = "Cs-CdsCsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   {Cd,CO} U0 {1,S}
3   Cs      U0 {1,S}
4   H       U0 {1,S}
5   H       U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CsHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 348,
    label        = "Cs-(Cds-Od)CsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cs U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.2,7.7,8.7,9.5,11.1,12.2,14.07],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-5.2,'kcal/mol','+|-',0.16),
        S298 = (9.6,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cs-COCsHH BENSON Cp1500 =3D Cp1000*(Cp1500/Cp1000: C/C/Cd/H2)""",
    longDesc = 
u"""

""",
)

entry(
    index        = 349,
    label        = "Cs-(Cds-Cd)CsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cs U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CsHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 350,
    label        = "Cs-(Cds-Cds)CsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cs U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.12,6.86,8.32,9.49,11.22,12.48,14.36],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-4.76,'kcal/mol','+|-',0.16),
        S298 = (9.8,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cs-CdCsHH BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index        = 351,
    label        = "Cs-(Cds-Cdd)CsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cs  U0 {1,S}
4   H   U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CsHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 352,
    label        = "Cs-(Cds-Cdd-Od)CsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cs  U0 {1,S}
4   H   U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.35,6.83,8.25,9.45,11.19,12.46,14.34],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-5.723,'kcal/mol','+|-',0.16),
        S298 = (9.37,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""{C/C/H2/CCO} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)CsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cs  U0 {1,S}
4   H   U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 353,
    label        = "Cs-(Cds-Cdd-Cd)CsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cs  U0 {1,S}
4   H   U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)CsHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1864,
    label        = "Cs-(CdN3d)CsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {5,S} {6,S} {7,S}
2   Cd  U0 {1,S} {3,D} {4,S}
3   N3d U0 {2,D}
4   R   U0 {2,S}
5   Cs  U0 {1,S}
6   H   U0 {1,S}
7   H   U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.5,6.9,8.1,9.2,10.9,12.2,14.1],'cal/(mol*K)','+|-',[1.2,1.2,1.2,1.2,1.2,1.2,1.2]),
        H298 = (-5.1,'kcal/mol','+|-',1.7),
        S298 = (10.1,'cal/(mol*K)','+|-',1.6),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1177,
    label        = "Cs-C=SCsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cs U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.23,6.82,8.16,9.27,10.96,12.2,14.13],'cal/(mol*K)'),
        H298 = (-4.89,'kcal/mol'),
        S298 = (9.83,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 354,
    label        = "Cs-CdsCdsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   {Cd,CO} U0 {1,S}
3   {Cd,CO} U0 {1,S}
4   H       U0 {1,S}
5   H       U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)HH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 355,
    label        = "Cs-(Cds-Od)(Cds-Od)HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   CO U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.03,7.44,9.16,10.49,12.17,13.57,13.57],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-7.6,'kcal/mol','+|-',0.16),
        S298 = (5.82,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cs-COCOHH BENSON Hf, Mopac =3D S,Cp nov99 !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index        = 356,
    label        = "Cs-(Cds-Od)(Cds-Cd)HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cd U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)HH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 357,
    label        = "Cs-(Cds-Od)(Cds-Cds)HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cd U0 {1,S} {6,D}
4   H  U0 {1,S}
5   H  U0 {1,S}
6   Cd U0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.75,7.11,8.92,10.32,12.16,13.61,13.61],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-3.8,'kcal/mol','+|-',0.16),
        S298 = (6.31,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cs-COCdHH BENSON Hf, Mopac =3D S,Cp nov99 !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index        = 358,
    label        = "Cs-(Cds-Od)(Cds-Cdd)HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   H   U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cdd-Cd)HH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 359,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Od)HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   H   U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)CsHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 360,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Cd)HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   H   U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)HH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 361,
    label        = "Cs-(Cds-Cd)(Cds-Cd)HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cd U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)HH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 362,
    label        = "Cs-(Cds-Cds)(Cds-Cds)HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   H  U0 {1,S}
5   H  U0 {1,S}
6   Cd U0 {2,D}
7   Cd U0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.7,6.8,8.4,9.6,11.3,12.6,14.4],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-4.29,'kcal/mol','+|-',0.16),
        S298 = (10.2,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cs-CdCdHH BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index        = 363,
    label        = "Cs-(Cds-Cdd)(Cds-Cds)HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   H   U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D}
7   Cd  U0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cds)HH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 364,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cds)HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   H   U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)CsHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cds)HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   H   U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 365,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cds)HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   H   U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)HH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 366,
    label        = "Cs-(Cds-Cdd)(Cds-Cdd)HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   H   U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D}
7   Cdd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)HH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 367,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   H   U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Od  U0 {6,D}
9   Od  U0 {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.68,8.28,9.58,10.61,12.04,13.13,14.87],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-5.301,'kcal/mol','+|-',0.16),
        S298 = (7.18,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""{C/H2/CCO2} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""

""",
)

entry(
    index        = 368,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   H   U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Od  U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)(Cds-Cds)HH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   H   U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Sd  U0 {6,D}
9   Sd  U0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Cd)HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   H   U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Sd  U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 369,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   H   U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   C   U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)HH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cd)HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cds)HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {7,D}
3   Cd U0 {1,S} {6,D}
4   H  U0 {1,S}
5   H  U0 {1,S}
6   Cd U0 {3,D}
7   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd)HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {7,D}
3   Cd  U0 {1,S} {6,D}
4   H   U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {3,D}
7   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Sd)HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {6,D}
4   H   U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   Sd  U0 {6,D}
8   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Cd)HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {6,D}
4   H   U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
8   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=SHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   H  U0 {1,S}
5   H  U0 {1,S}
6   Sd U0 {2,D}
7   Sd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 370,
    label        = "Cs-CtCsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Ct U0 {1,S}
3   Cs U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.95,6.56,7.93,9.08,10.86,12.19,14.2],'cal/(mol*K)','+|-',[0.08,0.08,0.08,0.08,0.08,0.08,0.08]),
        H298 = (-4.73,'kcal/mol','+|-',0.28),
        S298 = (10.3,'cal/(mol*K)','+|-',0.07),
    ),
    shortDesc = u"""Cs-CtCsHH BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1832,
    label        = "Cs-(CtN3t)CsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {4,S} {5,S} {6,S}
2   Ct  U0 {1,S} {3,T}
3   N3t U0 {2,T}
4   Cs  U0 {1,S}
5   H   U0 {1,S}
6   H   U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.3,13.5,15.3,16.8,19.2,20.9,23.5],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (22.9,'kcal/mol','+|-',1.3),
        S298 = (39.8,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 371,
    label        = "Cs-CtCdsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   Ct      U0 {1,S}
3   {Cd,CO} U0 {1,S}
4   H       U0 {1,S}
5   H       U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CtHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 372,
    label        = "Cs-(Cds-Od)CtHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Ct U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.85,6.22,8.01,9.43,11.29,12.76,12.76],'cal/(mol*K)','+|-',[0.08,0.08,0.08,0.08,0.08,0.08,0.08]),
        H298 = (-5.4,'kcal/mol','+|-',0.28),
        S298 = (7.68,'cal/(mol*K)','+|-',0.07),
    ),
    shortDesc = u"""Cs-COCtHH BENSON Hf, Mopac =3D S,Cp nov99 !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index        = 373,
    label        = "Cs-(Cds-Cd)CtHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Ct U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CtHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 374,
    label        = "Cs-(Cds-Cds)CtHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Ct U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.4,6.33,7.9,9.16,10.93,12.29,13.43],'cal/(mol*K)','+|-',[0.08,0.08,0.08,0.08,0.08,0.08,0.08]),
        H298 = (-3.49,'kcal/mol','+|-',0.28),
        S298 = (9.31,'cal/(mol*K)','+|-',0.07),
    ),
    shortDesc = u"""Cs-CtCdHH RAMAN & GREEN JPCA 2002, 106, 11141-11149""",
    longDesc = 
u"""

""",
)

entry(
    index        = 375,
    label        = "Cs-(Cds-Cdd)CtHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ct  U0 {1,S}
4   H   U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CtHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 376,
    label        = "Cs-(Cds-Cdd-Od)CtHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ct  U0 {1,S}
4   H   U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)(Cds-Cds)HH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)CtHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ct  U0 {1,S}
4   H   U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 377,
    label        = "Cs-(Cds-Cdd-Cd)CtHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ct  U0 {1,S}
4   H   U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)CtHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SCtHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Ct U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 378,
    label        = "Cs-CtCtHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Ct U0 {1,S}
3   Ct U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4,6.07,7.71,9.03,10.88,12.3,12.48],'cal/(mol*K)','+|-',[0.08,0.08,0.08,0.08,0.08,0.08,0.08]),
        H298 = (-0.82,'kcal/mol','+|-',0.28),
        S298 = (10.04,'cal/(mol*K)','+|-',0.07),
    ),
    shortDesc = u"""Cs-CtCtHH RAMAN & GREEN JPCA 2002, 106, 11141-11149""",
    longDesc = 
u"""

""",
)

entry(
    index        = 379,
    label        = "Cs-CbCsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Cs U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.84,7.61,8.98,10.01,11.49,12.54,13.76],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-4.86,'kcal/mol','+|-',0.2),
        S298 = (9.34,'cal/(mol*K)','+|-',0.19),
    ),
    shortDesc = u"""Cs-CbCsHH BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index        = 380,
    label        = "Cs-CbCdsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   Cb      U0 {1,S}
3   {Cd,CO} U0 {1,S}
4   H       U0 {1,S}
5   H       U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CbHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 381,
    label        = "Cs-(Cds-Od)CbHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cb U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.38,7.59,9.25,10.51,12.19,13.52,13.52],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-5.4,'kcal/mol','+|-',0.2),
        S298 = (5.89,'cal/(mol*K)','+|-',0.19),
    ),
    shortDesc = u"""Cs-COCbHH BENSON Hf, Mopac =3D S,Cp nov99 !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index        = 382,
    label        = "Cs-(Cds-Cd)CbHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cb U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CbHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 383,
    label        = "Cs-(Cds-Cds)CbHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cb U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.51,6.76,8.61,10.01,11.97,13.4,15.47],'cal/(mol*K)','+|-',[0.2,0.2,0.2,0.2,0.2,0.2,0.2]),
        H298 = (-4.29,'kcal/mol','+|-',0.2),
        S298 = (2,'cal/(mol*K)','+|-',0.19),
    ),
    shortDesc = u"""Cs-CbCdHH Hf=Stein S,Cp=3D mopac nov99""",
    longDesc = 
u"""

""",
)

entry(
    index        = 384,
    label        = "Cs-(Cds-Cdd)CbHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   H   U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CbHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 385,
    label        = "Cs-(Cds-Cdd-Od)CbHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   H   U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)(Cds-Cds)HH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)CbHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   H   U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 386,
    label        = "Cs-(Cds-Cdd-Cd)CbHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   H   U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)CbHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SCbHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cb U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 387,
    label        = "Cs-CbCtHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Ct U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.28,6.43,8.16,9.5,11.36,12.74,13.7],'cal/(mol*K)','+|-',[0.08,0.08,0.08,0.08,0.08,0.08,0.08]),
        H298 = (-4.29,'kcal/mol','+|-',0.28),
        S298 = (9.84,'cal/(mol*K)','+|-',0.07),
    ),
    shortDesc = u"""Cs-CbCtHH Hf=Stein S,Cp=3D mopac nov99""",
    longDesc = 
u"""

""",
)

entry(
    index        = 388,
    label        = "Cs-CbCbHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Cb U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.67,7.7,9.31,10.52,12.21,13.47,15.11],'cal/(mol*K)','+|-',[0.2,0.2,0.2,0.2,0.2,0.2,0.2]),
        H298 = (-4.29,'kcal/mol','+|-',0.2),
        S298 = (8.07,'cal/(mol*K)','+|-',0.19),
    ),
    shortDesc = u"""Cs-CbCbHH Hf=3Dbsn/Cs/Cd2/H2 S,Cp=3D mopac nov99""",
    longDesc = 
u"""

""",
)

entry(
    index        = 389,
    label        = "Cs-CCCH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   C  U0 {1,S}
3   C  U0 {1,S}
4   C  U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-CsCsCsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 390,
    label        = "Cs-CsCsCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cs U0 {1,S}
3   Cs U0 {1,S}
4   Cs U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.54,6,7.17,8.05,9.31,10.05,11.17],'cal/(mol*K)','+|-',[0.07,0.07,0.07,0.07,0.07,0.07,0.07]),
        H298 = (-1.9,'kcal/mol','+|-',0.15),
        S298 = (-12.07,'cal/(mol*K)','+|-',0.07),
    ),
    shortDesc = u"""Cs-CsCsCsH BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index        = 391,
    label        = "Cs-CdsCsCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   {Cd,CO} U0 {1,S}
3   Cs      U0 {1,S}
4   Cs      U0 {1,S}
5   H       U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CsCsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 392,
    label        = "Cs-(Cds-Od)CsCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cs U0 {1,S}
4   Cs U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.16,5.91,7.34,8.19,9.46,10.19,10.19],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (-1.7,'kcal/mol','+|-',0.27),
        S298 = (-11.7,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cs-COCsCsH BOZZELLI - BENSON Hf, S, -C/C2Cd/H =3D Cp !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index        = 393,
    label        = "Cs-(Cds-Cd)CsCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cs U0 {1,S}
4   Cs U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CsCsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 394,
    label        = "Cs-(Cds-Cds)CsCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cs U0 {1,S}
4   Cs U0 {1,S}
5   H  U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.16,5.91,7.34,8.19,9.46,10.19,11.28],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (-1.48,'kcal/mol','+|-',0.27),
        S298 = (-11.69,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cs-CdCsCsH BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index        = 395,
    label        = "Cs-(Cds-Cdd)CsCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cs  U0 {1,S}
4   Cs  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CsCsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 396,
    label        = "Cs-(Cds-Cdd-Od)CsCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cs  U0 {1,S}
4   Cs  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.96,6.35,7.61,8.54,9.65,10.35,11.19],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (-3.634,'kcal/mol','+|-',0.27),
        S298 = (-12.31,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""{C/C2/CCO/H} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)CsCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cs  U0 {1,S}
4   Cs  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 397,
    label        = "Cs-(Cds-Cdd-Cd)CsCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cs  U0 {1,S}
4   Cs  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.16,5.91,7.34,8.19,9.46,10.19,11.28],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (-1.48,'kcal/mol','+|-',0.27),
        S298 = (-11.69,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cs-CdCsCsH BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1865,
    label        = "Cs-(CdN3d)CsCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {5,S} {6,S} {7,S}
2   Cd  U0 {1,S} {3,D} {4,S}
3   N3d U0 {2,D}
4   R   U0 {2,S}
5   Cs  U0 {1,S}
6   Cs  U0 {1,S}
7   H   U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5,6.5,7.5,8.2,9.3,9.9,10.9],'cal/(mol*K)','+|-',[1.2,1.2,1.2,1.2,1.2,1.2,1.2]),
        H298 = (-1.6,'kcal/mol','+|-',1.7),
        S298 = (-11.2,'cal/(mol*K)','+|-',1.6),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1178,
    label        = "Cs-C=SCsCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cs U0 {1,S}
4   Cs U0 {1,S}
5   H  U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.78,6.25,7.44,8.35,9.57,10.31,11.2],'cal/(mol*K)'),
        H298 = (-0.78,'kcal/mol'),
        S298 = (-11.46,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 398,
    label        = "Cs-CtCsCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Ct U0 {1,S}
3   Cs U0 {1,S}
4   Cs U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.99,5.61,6.85,7.78,9.1,9.9,11.12],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (-1.72,'kcal/mol','+|-',0.27),
        S298 = (-11.19,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cs-CtCsCsH BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1833,
    label        = "Cs-(CtN3t)CsCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {4,S} {5,S} {6,S}
2   Ct  U0 {1,S} {3,T}
3   N3t U0 {2,T}
4   Cs  U0 {1,S}
5   Cs  U0 {1,S}
6   H   U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11,12.7,14.1,15.4,17.3,18.6,21.85],'cal/(mol*K)'),
        H298 = (25.8,'kcal/mol'),
        S298 = (19.8,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 399,
    label        = "Cs-CbCsCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Cs U0 {1,S}
4   Cs U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.88,6.66,7.9,8.75,9.73,10.25,10.68],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (-0.98,'kcal/mol','+|-',0.27),
        S298 = (-12.15,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cs-CbCsCsH BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index        = 400,
    label        = "Cs-CdsCdsCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   {Cd,CO} U0 {1,S}
3   {Cd,CO} U0 {1,S}
4   Cs      U0 {1,S}
5   H       U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 401,
    label        = "Cs-(Cds-Od)(Cds-Od)CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   CO U0 {1,S}
4   Cs U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-CsCsCsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 402,
    label        = "Cs-(Cds-Od)(Cds-Cd)CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cd U0 {1,S}
4   Cs U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 403,
    label        = "Cs-(Cds-Od)(Cds-Cds)CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cd U0 {1,S} {6,D}
4   Cs U0 {1,S}
5   H  U0 {1,S}
6   Cd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Od)CsCsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 404,
    label        = "Cs-(Cds-Od)(Cds-Cdd)CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cs  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cdd-Cd)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 405,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Od)CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cs  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)CsCsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 406,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Cd)CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cs  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 407,
    label        = "Cs-(Cds-Cd)(Cds-Cd)CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cd U0 {1,S}
4   Cs U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 408,
    label        = "Cs-(Cds-Cds)(Cds-Cds)CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Cs U0 {1,S}
5   H  U0 {1,S}
6   Cd U0 {2,D}
7   Cd U0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.28,6.54,7.67,8.48,9.45,10.18,11.24],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (-1.1,'kcal/mol','+|-',0.27),
        S298 = (-13.03,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cs-CdCdCsH RAMAN & GREEN JPCA 2002, 106, 11141-11149""",
    longDesc = 
u"""

""",
)

entry(
    index        = 409,
    label        = "Cs-(Cds-Cdd)(Cds-Cds)CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cs  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D}
7   Cd  U0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cds)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 410,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cds)CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cs  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)CsCsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cds)CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cs  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 411,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cs  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 412,
    label        = "Cs-(Cds-Cdd)(Cds-Cdd)CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cs  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D}
7   Cdd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 413,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cs  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Od  U0 {6,D}
9   Od  U0 {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.33,7.96,9.13,9.91,10.7,11.19,11.81],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (-3.714,'kcal/mol','+|-',0.27),
        S298 = (-14.12,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""{C/C/H/CCO2} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""

""",
)

entry(
    index        = 414,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cs  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Od  U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)(Cds-Cds)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cs  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Sd  U0 {6,D}
9   Sd  U0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Cd)CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cs  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Sd  U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 415,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cs  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   C   U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cd)CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S}
4   Cs U0 {1,S}
5   H  U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cds)CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {7,D}
3   Cd U0 {1,S} {6,D}
4   Cs U0 {1,S}
5   H  U0 {1,S}
6   Cd U0 {3,D}
7   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd)CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {7,D}
3   Cd  U0 {1,S} {6,D}
4   Cs  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {3,D}
7   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Sd)CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {6,D}
4   Cs  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   Sd  U0 {6,D}
8   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Cd)CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {6,D}
4   Cs  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
8   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=SCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Cs U0 {1,S}
5   H  U0 {1,S}
6   Sd U0 {2,D}
7   Sd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 416,
    label        = "Cs-CtCdsCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   Ct      U0 {1,S}
3   {Cd,CO} U0 {1,S}
4   Cs      U0 {1,S}
5   H       U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CtCsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 417,
    label        = "Cs-(Cds-Od)CtCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Ct U0 {1,S}
4   Cs U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 418,
    label        = "Cs-(Cds-Cd)CtCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Ct U0 {1,S}
4   Cs U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CtCsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 419,
    label        = "Cs-(Cds-Cds)CtCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Ct U0 {1,S}
4   Cs U0 {1,S}
5   H  U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.55,7.21,8.39,9.17,10,10.61,10.51],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (-6.9,'kcal/mol','+|-',0.27),
        S298 = (-13.48,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cs-CtCdCsH RAMAN & GREEN JPCA 2002, 106, 11141-11149""",
    longDesc = 
u"""

""",
)

entry(
    index        = 420,
    label        = "Cs-(Cds-Cdd)CtCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ct  U0 {1,S}
4   Cs  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CtCsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 421,
    label        = "Cs-(Cds-Cdd-Od)CtCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ct  U0 {1,S}
4   Cs  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)(Cds-Cds)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)CtCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ct  U0 {1,S}
4   Cs  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 422,
    label        = "Cs-(Cds-Cdd-Cd)CtCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ct  U0 {1,S}
4   Cs  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)CtCsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SCtCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Ct U0 {1,S}
4   Cs U0 {1,S}
5   H  U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 423,
    label        = "Cs-CbCdsCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   Cb      U0 {1,S}
3   {Cd,CO} U0 {1,S}
4   Cs      U0 {1,S}
5   H       U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CbCsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 424,
    label        = "Cs-(Cds-Od)CbCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cb U0 {1,S}
4   Cs U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 425,
    label        = "Cs-(Cds-Cd)CbCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cb U0 {1,S}
4   Cs U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CbCsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 426,
    label        = "Cs-(Cds-Cds)CbCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cb U0 {1,S}
4   Cs U0 {1,S}
5   H  U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.5,6.57,8.07,8.89,9.88,10.39,10.79],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (-1.56,'kcal/mol','+|-',0.27),
        S298 = (-11.77,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cs-CbCdCsH BOZZELLI =3D Cs/Cs2/Cd/H + (Cs/Cs2/Cb/H - Cs/Cs3/H)""",
    longDesc = 
u"""

""",
)

entry(
    index        = 427,
    label        = "Cs-(Cds-Cdd)CbCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Cs  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CbCsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 428,
    label        = "Cs-(Cds-Cdd-Od)CbCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Cs  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)(Cds-Cds)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 429,
    label        = "Cs-(Cds-Cdd-Cd)CbCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Cs  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)CbCsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 430,
    label        = "Cs-CtCtCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Ct U0 {1,S}
3   Ct U0 {1,S}
4   Cs U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.27,5.32,6.9,8.03,9.33,10.21,9.38],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (1.72,'kcal/mol','+|-',0.27),
        S298 = (-11.61,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cs-CtCtCsH RAMAN & GREEN JPCA 2002, 106, 11141-11149""",
    longDesc = 
u"""

""",
)

entry(
    index        = 431,
    label        = "Cs-CbCtCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Ct U0 {1,S}
4   Cs U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.33,6.27,7.58,8.48,9.52,10.1,10.63],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (-1.55,'kcal/mol','+|-',0.27),
        S298 = (-11.65,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cs-CbCtCsH BOZZELLI =3D Cs/Cs2/Cb/H + (Cs/Cs2/Ct/H - Cs/Cs3/H)""",
    longDesc = 
u"""

""",
)

entry(
    index        = 432,
    label        = "Cs-CbCbCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Cb U0 {1,S}
4   Cs U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.22,7.32,8.63,8.45,10.15,10.45,10.89],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (-1.06,'kcal/mol','+|-',0.27),
        S298 = (-12.23,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cs-CbCbCsCs BOZZELLI =3D Cs/Cs2/Cb/H + (Cs/Cs2/Cb/H - Cs/Cs3/H)""",
    longDesc = 
u"""

""",
)

entry(
    index        = 433,
    label        = "Cs-CdsCdsCdsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   {Cd,CO} U0 {1,S}
3   {Cd,CO} U0 {1,S}
4   {Cd,CO} U0 {1,S}
5   H       U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 434,
    label        = "Cs-(Cds-Od)(Cds-Od)(Cds-Od)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   CO U0 {1,S}
4   CO U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-CsCsCsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 435,
    label        = "Cs-(Cds-Od)(Cds-Od)(Cds-Cd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   CO U0 {1,S}
4   Cd U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 436,
    label        = "Cs-(Cds-Od)(Cds-Od)(Cds-Cds)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   CO U0 {1,S}
4   Cd U0 {1,S} {6,D}
5   H  U0 {1,S}
6   Cd U0 {4,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Od)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 437,
    label        = "Cs-(Cds-Od)(Cds-Od)(Cds-Cdd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   CO  U0 {1,S}
4   Cd  U0 {1,S} {6,D}
5   H   U0 {1,S}
6   Cdd U0 {4,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Cd)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 438,
    label        = "Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Od)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   CO  U0 {1,S}
4   Cd  U0 {1,S} {6,D}
5   H   U0 {1,S}
6   Cdd U0 {4,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)CsCsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 439,
    label        = "Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Cd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   CO  U0 {1,S}
4   Cd  U0 {1,S} {6,D}
5   H   U0 {1,S}
6   Cdd U0 {4,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 440,
    label        = "Cs-(Cds-Od)(Cds-Cd)(Cds-Cd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cd U0 {1,S}
4   Cd U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 441,
    label        = "Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cd U0 {1,S} {6,D}
4   Cd U0 {1,S} {7,D}
5   H  U0 {1,S}
6   Cd U0 {3,D}
7   Cd U0 {4,D}
""",
    thermo = u'Cs-(Cds-Od)CsCsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 442,
    label        = "Cs-(Cds-Od)(Cds-Cdd)(Cds-Cds)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   H   U0 {1,S}
6   Cdd U0 {3,D}
7   Cd  U0 {4,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 443,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   H   U0 {1,S}
6   Cdd U0 {3,D} {8,D}
7   Cd  U0 {4,D}
8   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cdd-Od)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 444,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cds)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   H   U0 {1,S}
6   Cdd U0 {3,D} {8,D}
7   Cd  U0 {4,D}
8   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 445,
    label        = "Cs-(Cds-Od)(Cds-Cdd)(Cds-Cdd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   H   U0 {1,S}
6   Cdd U0 {3,D}
7   Cdd U0 {4,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 446,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   H   U0 {1,S}
6   Cdd U0 {3,D} {8,D}
7   Cdd U0 {4,D} {9,D}
8   Od  U0 {6,D}
9   Od  U0 {7,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 447,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   H   U0 {1,S}
6   Cdd U0 {3,D} {8,D}
7   Cdd U0 {4,D} {9,D}
8   Od  U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 448,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   H   U0 {1,S}
6   Cdd U0 {3,D} {8,D}
7   Cdd U0 {4,D} {9,D}
8   C   U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 449,
    label        = "Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cd U0 {1,S}
4   Cd U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 450,
    label        = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Cd U0 {1,S} {8,D}
5   H  U0 {1,S}
6   Cd U0 {2,D}
7   Cd U0 {3,D}
8   Cd U0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.51,5.96,7.13,7.98,9.06,9.9,11.23],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (0.41,'kcal/mol','+|-',0.27),
        S298 = (-11.82,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cs-CdCdCdH RAMAN & GREEN JPC 2002""",
    longDesc = 
u"""

""",
)

entry(
    index        = 451,
    label        = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cd  U0 {1,S} {8,D}
5   H   U0 {1,S}
6   Cd  U0 {2,D}
7   Cd  U0 {3,D}
8   Cdd U0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 452,
    label        = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cd  U0 {1,S} {8,D}
5   H   U0 {1,S}
6   Cd  U0 {2,D}
7   Cd  U0 {3,D}
8   Cdd U0 {4,D} {9,D}
9   Od  U0 {8,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)CsCsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Sd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cd  U0 {1,S} {8,D}
5   H   U0 {1,S}
6   Cd  U0 {2,D}
7   Cd  U0 {3,D}
8   Cdd U0 {4,D} {9,D}
9   Sd  U0 {8,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 453,
    label        = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cd  U0 {1,S} {8,D}
5   H   U0 {1,S}
6   Cd  U0 {2,D}
7   Cd  U0 {3,D}
8   Cdd U0 {4,D} {9,D}
9   C   U0 {8,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 454,
    label        = "Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cd  U0 {1,S} {8,D}
5   H   U0 {1,S}
6   Cd  U0 {2,D}
7   Cdd U0 {3,D}
8   Cdd U0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 455,
    label        = "Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    H   U0 {1,S}
6    Cd  U0 {2,D}
7    Cdd U0 {3,D} {9,D}
8    Cdd U0 {4,D} {10,D}
9    Od  U0 {7,D}
10   Od  U0 {8,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 456,
    label        = "Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Cd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    H   U0 {1,S}
6    Cd  U0 {2,D}
7    Cdd U0 {3,D} {9,D}
8    Cdd U0 {4,D} {10,D}
9    Od  U0 {7,D}
10   C   U0 {8,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cds)(Cds-Cdd-Sd)(Cds-Cdd-Sd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    H   U0 {1,S}
6    Cd  U0 {2,D}
7    Cdd U0 {3,D} {9,D}
8    Cdd U0 {4,D} {10,D}
9    Sd  U0 {7,D}
10   Sd  U0 {8,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cds)(Cds-Cdd-Sd)(Cds-Cdd-Cd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    H   U0 {1,S}
6    Cd  U0 {2,D}
7    Cdd U0 {3,D} {9,D}
8    Cdd U0 {4,D} {10,D}
9    Sd  U0 {7,D}
10   C   U0 {8,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 457,
    label        = "Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    H   U0 {1,S}
6    Cd  U0 {2,D}
7    Cdd U0 {3,D} {9,D}
8    Cdd U0 {4,D} {10,D}
9    C   U0 {7,D}
10   C   U0 {8,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 458,
    label        = "Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cd  U0 {1,S} {8,D}
5   H   U0 {1,S}
6   Cdd U0 {2,D}
7   Cdd U0 {3,D}
8   Cdd U0 {4,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 459,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    H   U0 {1,S}
6    Cdd U0 {2,D} {9,D}
7    Cdd U0 {3,D} {10,D}
8    Cdd U0 {4,D} {11,D}
9    Od  U0 {6,D}
10   Od  U0 {7,D}
11   Od  U0 {8,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 460,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    H   U0 {1,S}
6    Cdd U0 {2,D} {9,D}
7    Cdd U0 {3,D} {10,D}
8    Cdd U0 {4,D} {11,D}
9    Od  U0 {6,D}
10   Od  U0 {7,D}
11   C   U0 {8,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 461,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    H   U0 {1,S}
6    Cdd U0 {2,D} {9,D}
7    Cdd U0 {3,D} {10,D}
8    Cdd U0 {4,D} {11,D}
9    Od  U0 {6,D}
10   C   U0 {7,D}
11   C   U0 {8,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)(Cds-Cdd-Sd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    H   U0 {1,S}
6    Cdd U0 {2,D} {9,D}
7    Cdd U0 {3,D} {10,D}
8    Cdd U0 {4,D} {11,D}
9    Sd  U0 {6,D}
10   Sd  U0 {7,D}
11   Sd  U0 {8,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)(Cds-Cdd-Cd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    H   U0 {1,S}
6    Cdd U0 {2,D} {9,D}
7    Cdd U0 {3,D} {10,D}
8    Cdd U0 {4,D} {11,D}
9    Sd  U0 {6,D}
10   Sd  U0 {7,D}
11   C   U0 {8,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    H   U0 {1,S}
6    Cdd U0 {2,D} {9,D}
7    Cdd U0 {3,D} {10,D}
8    Cdd U0 {4,D} {11,D}
9    Sd  U0 {6,D}
10   C   U0 {7,D}
11   C   U0 {8,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 462,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    H   U0 {1,S}
6    Cdd U0 {2,D} {9,D}
7    Cdd U0 {3,D} {10,D}
8    Cdd U0 {4,D} {11,D}
9    C   U0 {6,D}
10   C   U0 {7,D}
11   C   U0 {8,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cd)(Cds-Cd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S}
4   Cd U0 {1,S}
5   H  U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cds)(Cds-Cds)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {8,D}
3   Cd U0 {1,S} {6,D}
4   Cd U0 {1,S} {7,D}
5   H  U0 {1,S}
6   Cd U0 {3,D}
7   Cd U0 {4,D}
8   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd)(Cds-Cds)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   H   U0 {1,S}
6   Cdd U0 {3,D}
7   Cd  U0 {4,D}
8   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Sd)(Cds-Cds)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {9,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   H   U0 {1,S}
6   Cdd U0 {3,D} {8,D}
7   Cd  U0 {4,D}
8   Sd  U0 {6,D}
9   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Cd)(Cds-Cds)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {9,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   H   U0 {1,S}
6   Cdd U0 {3,D} {8,D}
7   Cd  U0 {4,D}
8   C   U0 {6,D}
9   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd)(Cds-Cdd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   H   U0 {1,S}
6   Cdd U0 {3,D}
7   Cdd U0 {4,D}
8   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Sd)(Cds-Cdd-Sd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {10,D}
3    Cd  U0 {1,S} {6,D}
4    Cd  U0 {1,S} {7,D}
5    H   U0 {1,S}
6    Cdd U0 {3,D} {8,D}
7    Cdd U0 {4,D} {9,D}
8    Sd  U0 {6,D}
9    Sd  U0 {7,D}
10   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Sd)(Cds-Cdd-Cd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {10,D}
3    Cd  U0 {1,S} {6,D}
4    Cd  U0 {1,S} {7,D}
5    H   U0 {1,S}
6    Cdd U0 {3,D} {8,D}
7    Cdd U0 {4,D} {9,D}
8    Sd  U0 {6,D}
9    C   U0 {7,D}
10   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Cd)(Cds-Cdd-Cd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {10,D}
3    Cd  U0 {1,S} {6,D}
4    Cd  U0 {1,S} {7,D}
5    H   U0 {1,S}
6    Cdd U0 {3,D} {8,D}
7    Cdd U0 {4,D} {9,D}
8    C   U0 {6,D}
9    C   U0 {7,D}
10   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=S(Cds-Cd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Cd U0 {1,S}
5   H  U0 {1,S}
6   Sd U0 {2,D}
7   Sd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=S(Cds-Cds)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {7,D}
3   Cd U0 {1,S} {8,D}
4   Cd U0 {1,S} {6,D}
5   H  U0 {1,S}
6   Cd U0 {4,D}
7   Sd U0 {2,D}
8   Sd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=S(Cds-Cdd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {7,D}
3   Cd  U0 {1,S} {8,D}
4   Cd  U0 {1,S} {6,D}
5   H   U0 {1,S}
6   Cdd U0 {4,D}
7   Sd  U0 {2,D}
8   Sd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=S(Cds-Cdd-Sd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {9,D}
4   Cd  U0 {1,S} {6,D}
5   H   U0 {1,S}
6   Cdd U0 {4,D} {7,D}
7   Sd  U0 {6,D}
8   Sd  U0 {2,D}
9   Sd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=S(Cds-Cdd-Cd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {9,D}
4   Cd  U0 {1,S} {6,D}
5   H   U0 {1,S}
6   Cdd U0 {4,D} {7,D}
7   C   U0 {6,D}
8   Sd  U0 {2,D}
9   Sd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=SC=SH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Cd U0 {1,S} {8,D}
5   H  U0 {1,S}
6   Sd U0 {2,D}
7   Sd U0 {3,D}
8   Sd U0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 463,
    label        = "Cs-CtCdsCdsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   Ct      U0 {1,S}
3   {Cd,CO} U0 {1,S}
4   {Cd,CO} U0 {1,S}
5   H       U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CtH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 464,
    label        = "Cs-(Cds-Od)(Cds-Od)CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   CO U0 {1,S}
4   Ct U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 465,
    label        = "Cs-(Cds-Od)(Cds-Cd)CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cd U0 {1,S}
4   Ct U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)CtH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 466,
    label        = "Cs-(Cds-Od)(Cds-Cds)CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cd U0 {1,S} {6,D}
4   Ct U0 {1,S}
5   H  U0 {1,S}
6   Cd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 467,
    label        = "Cs-(Cds-Od)(Cds-Cdd)CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Ct  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cdd-Cd)CtH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 468,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Od)CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Ct  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 469,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Cd)CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Ct  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)CtH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 470,
    label        = "Cs-(Cds-Cd)(Cds-Cd)CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cd U0 {1,S}
4   Ct U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CtH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 471,
    label        = "Cs-(Cds-Cds)(Cds-Cds)CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Ct U0 {1,S}
5   H  U0 {1,S}
6   Cd U0 {2,D}
7   Cd U0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.68,7.85,8.62,9.16,9.81,10.42,10.49],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (1.88,'kcal/mol','+|-',0.27),
        S298 = (-13.75,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cs-CtCdCdH RAMAN & GREEN JPCA 2002, 106, 11141-11149""",
    longDesc = 
u"""

""",
)

entry(
    index        = 472,
    label        = "Cs-(Cds-Cdd)(Cds-Cds)CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ct  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D}
7   Cd  U0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cds)CtH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 473,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cds)CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ct  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cds)CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ct  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 474,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ct  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CtH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 475,
    label        = "Cs-(Cds-Cdd)(Cds-Cdd)CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ct  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D}
7   Cdd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 476,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ct  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Od  U0 {6,D}
9   Od  U0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 477,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ct  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Od  U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)(Cds-Cds)CtH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ct  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Sd  U0 {6,D}
9   Sd  U0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Cd)CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ct  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Sd  U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 478,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ct  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   C   U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CtH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cd)CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S}
4   Ct U0 {1,S}
5   H  U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cds)CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {7,D}
3   Cd U0 {1,S} {6,D}
4   Ct U0 {1,S}
5   H  U0 {1,S}
6   Cd U0 {3,D}
7   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd)CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {7,D}
3   Cd  U0 {1,S} {6,D}
4   Ct  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {3,D}
7   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Sd)CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {6,D}
4   Ct  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   Sd  U0 {6,D}
8   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Cd)CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {6,D}
4   Ct  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
8   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=SCtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Ct U0 {1,S}
5   H  U0 {1,S}
6   Sd U0 {2,D}
7   Sd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 479,
    label        = "Cs-CbCdsCdsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   Cb      U0 {1,S}
3   {Cd,CO} U0 {1,S}
4   {Cd,CO} U0 {1,S}
5   H       U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CbH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 480,
    label        = "Cs-(Cds-Od)(Cds-Od)CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   CO U0 {1,S}
4   Cb U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 481,
    label        = "Cs-(Cds-Od)(Cds-Cd)CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cd U0 {1,S}
4   Cb U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)CbH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 482,
    label        = "Cs-(Cds-Od)(Cds-Cds)CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cd U0 {1,S} {6,D}
4   Cb U0 {1,S}
5   H  U0 {1,S}
6   Cd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 483,
    label        = "Cs-(Cds-Od)(Cds-Cdd)CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cb  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cdd-Cd)CbH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 484,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Od)CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cb  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 485,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Cd)CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cb  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)CbH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 486,
    label        = "Cs-(Cds-Cd)(Cds-Cd)CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cd U0 {1,S}
4   Cb U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CbH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 487,
    label        = "Cs-(Cds-Cds)(Cds-Cds)CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Cb U0 {1,S}
5   H  U0 {1,S}
6   Cd U0 {2,D}
7   Cd U0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.12,6.51,8.24,9,10.03,10.53,10.89],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (-1.39,'kcal/mol','+|-',0.27),
        S298 = (-11.39,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cs-CbCdCdH BOZZELLI =3D Cs/Cs/Cd2/H + (Cs/Cs2/Cb/H - Cs/Cs3/H)""",
    longDesc = 
u"""

""",
)

entry(
    index        = 488,
    label        = "Cs-(Cds-Cdd)(Cds-Cds)CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D}
7   Cd  U0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cds)CbH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 489,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cds)CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cds)CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 490,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CbH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 491,
    label        = "Cs-(Cds-Cdd)(Cds-Cdd)CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D}
7   Cdd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 492,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Od  U0 {6,D}
9   Od  U0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 493,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Od  U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)(Cds-Cds)CbH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Sd  U0 {6,D}
9   Sd  U0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Cd)CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Sd  U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 494,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   C   U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CbH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cd)CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S}
4   Cb U0 {1,S}
5   H  U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cds)CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {7,D}
3   Cd U0 {1,S} {6,D}
4   Cb U0 {1,S}
5   H  U0 {1,S}
6   Cd U0 {3,D}
7   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd)CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {7,D}
3   Cd  U0 {1,S} {6,D}
4   Cb  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {3,D}
7   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Sd)CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {6,D}
4   Cb  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   Sd  U0 {6,D}
8   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Cd)CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {6,D}
4   Cb  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
8   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=SCbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Cb U0 {1,S}
5   H  U0 {1,S}
6   Sd U0 {2,D}
7   Sd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 495,
    label        = "Cs-CtCtCdsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   Ct      U0 {1,S}
3   Ct      U0 {1,S}
4   {Cd,CO} U0 {1,S}
5   H       U0 {1,S}
""",
    thermo = u'Cs-CtCt(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 496,
    label        = "Cs-CtCt(Cds-Od)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Ct U0 {1,S}
3   Ct U0 {1,S}
4   CO U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 497,
    label        = "Cs-CtCt(Cds-Cd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Ct U0 {1,S}
3   Ct U0 {1,S}
4   Cd U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-CtCt(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 498,
    label        = "Cs-CtCt(Cds-Cds)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Ct U0 {1,S}
3   Ct U0 {1,S}
4   Cd U0 {1,S} {6,D}
5   H  U0 {1,S}
6   Cd U0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.58,5.68,7.11,8.12,9.27,10.13,9.44],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (4.73,'kcal/mol','+|-',0.27),
        S298 = (-11.46,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cs-CtCtCdH RAMAN & GREEN JPCA 2002, 106, 11141-11149""",
    longDesc = 
u"""

""",
)

entry(
    index        = 499,
    label        = "Cs-CtCt(Cds-Cdd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Ct  U0 {1,S}
3   Ct  U0 {1,S}
4   Cd  U0 {1,S} {6,D}
5   H   U0 {1,S}
6   Cdd U0 {4,D}
""",
    thermo = u'Cs-CtCt(Cds-Cdd-Cd)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 500,
    label        = "Cs-CtCt(Cds-Cdd-Od)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Ct  U0 {1,S}
3   Ct  U0 {1,S}
4   Cd  U0 {1,S} {6,D}
5   H   U0 {1,S}
6   Cdd U0 {4,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CtCt(Cds-Cdd-Sd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Ct  U0 {1,S}
3   Ct  U0 {1,S}
4   Cd  U0 {1,S} {6,D}
5   H   U0 {1,S}
6   Cdd U0 {4,D} {7,D}
7   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 501,
    label        = "Cs-CtCt(Cds-Cdd-Cd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Ct  U0 {1,S}
3   Ct  U0 {1,S}
4   Cd  U0 {1,S} {6,D}
5   H   U0 {1,S}
6   Cdd U0 {4,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-CtCt(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CtCtC=SH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Ct U0 {1,S}
3   Ct U0 {1,S}
4   Cd U0 {1,S} {6,D}
5   H  U0 {1,S}
6   Sd U0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 502,
    label        = "Cs-CbCtCdsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   Cb      U0 {1,S}
3   Ct      U0 {1,S}
4   {Cd,CO} U0 {1,S}
5   H       U0 {1,S}
""",
    thermo = u'Cs-CbCt(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 503,
    label        = "Cs-CbCt(Cds-Od)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Ct U0 {1,S}
4   CO U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)CtH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 504,
    label        = "Cs-CbCt(Cds-Cd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Ct U0 {1,S}
4   Cd U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-CbCt(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 505,
    label        = "Cs-CbCt(Cds-Cds)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Ct U0 {1,S}
4   Cd U0 {1,S} {6,D}
5   H  U0 {1,S}
6   Cd U0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CtH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 506,
    label        = "Cs-CbCt(Cds-Cdd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cb  U0 {1,S}
3   Ct  U0 {1,S}
4   Cd  U0 {1,S} {6,D}
5   H   U0 {1,S}
6   Cdd U0 {4,D}
""",
    thermo = u'Cs-CbCt(Cds-Cdd-Cd)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 507,
    label        = "Cs-CbCt(Cds-Cdd-Od)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cb  U0 {1,S}
3   Ct  U0 {1,S}
4   Cd  U0 {1,S} {6,D}
5   H   U0 {1,S}
6   Cdd U0 {4,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)(Cds-Cds)CtH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CbCt(Cds-Cdd-Sd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cb  U0 {1,S}
3   Ct  U0 {1,S}
4   Cd  U0 {1,S} {6,D}
5   H   U0 {1,S}
6   Cdd U0 {4,D} {7,D}
7   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 508,
    label        = "Cs-CbCt(Cds-Cdd-Cd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cb  U0 {1,S}
3   Ct  U0 {1,S}
4   Cd  U0 {1,S} {6,D}
5   H   U0 {1,S}
6   Cdd U0 {4,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-CbCt(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CbCtC=SH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Ct U0 {1,S}
4   Cd U0 {1,S} {6,D}
5   H  U0 {1,S}
6   Sd U0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 509,
    label        = "Cs-CbCbCdsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   Cb      U0 {1,S}
3   Cb      U0 {1,S}
4   {Cd,CO} U0 {1,S}
5   H       U0 {1,S}
""",
    thermo = u'Cs-CbCb(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 510,
    label        = "Cs-CbCb(Cds-Od)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Cb U0 {1,S}
4   CO U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CbCb(Cds-Cd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Cb U0 {1,S}
4   Cd U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 511,
    label        = "Cs-CbCb(Cds-Cds)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Cb U0 {1,S}
4   Cd U0 {1,S} {6,D}
5   H  U0 {1,S}
6   Cd U0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 512,
    label        = "Cs-CbCb(Cds-Cdd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cb  U0 {1,S}
3   Cb  U0 {1,S}
4   Cd  U0 {1,S} {6,D}
5   H   U0 {1,S}
6   Cdd U0 {4,D}
""",
    thermo = u'Cs-CbCb(Cds-Cdd-Cd)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 513,
    label        = "Cs-CbCb(Cds-Cdd-Od)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cb  U0 {1,S}
3   Cb  U0 {1,S}
4   Cd  U0 {1,S} {6,D}
5   H   U0 {1,S}
6   Cdd U0 {4,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CbCb(Cds-Cdd-Sd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cb  U0 {1,S}
3   Cb  U0 {1,S}
4   Cd  U0 {1,S} {6,D}
5   H   U0 {1,S}
6   Cdd U0 {4,D} {7,D}
7   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 514,
    label        = "Cs-CbCb(Cds-Cdd-Cd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cb  U0 {1,S}
3   Cb  U0 {1,S}
4   Cd  U0 {1,S} {6,D}
5   H   U0 {1,S}
6   Cdd U0 {4,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-CbCb(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CbCbC=SH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Cb U0 {1,S}
4   Cd U0 {1,S} {6,D}
5   H  U0 {1,S}
6   Sd U0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 515,
    label        = "Cs-CtCtCtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Ct U0 {1,S}
3   Ct U0 {1,S}
4   Ct U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.03,5.27,6.78,7.88,9.14,10.08,8.47],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (10.11,'kcal/mol','+|-',0.27),
        S298 = (-10.46,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cs-CtCtCtH RAMAN & GREEN JPCA 2002, 106, 11141-11149""",
    longDesc = 
u"""

""",
)

entry(
    index        = 516,
    label        = "Cs-CbCtCtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Ct U0 {1,S}
4   Ct U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-CtCt(Cds-Cds)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 517,
    label        = "Cs-CbCbCtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Cb U0 {1,S}
4   Ct U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CtH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 518,
    label        = "Cs-CbCbCbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Cb U0 {1,S}
4   Cb U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.56,7.98,9.36,10.15,10.57,10.65,9.7],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (-0.34,'kcal/mol','+|-',0.27),
        S298 = (-12.31,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cs-CbCbCbH BOZZELLI =3D Cs/Cs/Cb2/H + (Cs/Cs2/Cb/H - Cs/Cs3/H)""",
    longDesc = 
u"""

""",
)

entry(
    index        = 519,
    label        = "Cs-CCCC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   C  U0 {1,S}
3   C  U0 {1,S}
4   C  U0 {1,S}
5   C  U0 {1,S}
""",
    thermo = u'Cs-CsCsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 520,
    label        = "Cs-CsCsCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cs U0 {1,S}
3   Cs U0 {1,S}
4   Cs U0 {1,S}
5   Cs U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.37,6.13,7.36,8.12,8.77,8.76,8.12],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (0.5,'kcal/mol','+|-',0.27),
        S298 = (-35.1,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cs-CsCsCsCs BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index        = 521,
    label        = "Cs-CdsCsCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   {Cd,CO} U0 {1,S}
3   Cs      U0 {1,S}
4   Cs      U0 {1,S}
5   Cs      U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 522,
    label        = "Cs-(Cds-Od)CsCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cs U0 {1,S}
4   Cs U0 {1,S}
5   Cs U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.99,6.04,7.43,8.26,8.92,8.96,8.23],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (1.4,'kcal/mol','+|-',0.27),
        S298 = (-34.72,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cs-COCsCsCs Hf BENSON S,Cp =3D C/Cd/C3""",
    longDesc = 
u"""

""",
)

entry(
    index        = 523,
    label        = "Cs-(Cds-Cd)CsCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cs U0 {1,S}
4   Cs U0 {1,S}
5   Cs U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 524,
    label        = "Cs-(Cds-Cds)CsCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cs U0 {1,S}
4   Cs U0 {1,S}
5   Cs U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.99,6.04,7.43,8.26,8.92,8.96,8.23],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (1.68,'kcal/mol','+|-',0.27),
        S298 = (-34.72,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cs-CdCsCsCs BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index        = 525,
    label        = "Cs-(Cds-Cdd)CsCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cs  U0 {1,S}
4   Cs  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 526,
    label        = "Cs-(Cds-Cdd-Od)CsCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cs  U0 {1,S}
4   Cs  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.48,6.06,7.31,8.07,8.59,8.66,8.29],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (-2.896,'kcal/mol','+|-',0.27),
        S298 = (-34.87,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""{C/C3/CCO} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)CsCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cs  U0 {1,S}
4   Cs  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 527,
    label        = "Cs-(Cds-Cdd-Cd)CsCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cs  U0 {1,S}
4   Cs  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)CsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1866,
    label        = "Cs-(CdN3d)CsCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {5,S} {6,S} {7,S}
2   Cd  U0 {1,S} {3,D} {4,S}
3   N3d U0 {2,D}
4   R   U0 {2,S}
5   Cs  U0 {1,S}
6   Cs  U0 {1,S}
7   Cs  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.3,6.6,7.3,7.5,7.8,7.8,7.7],'cal/(mol*K)','+|-',[1.2,1.2,1.2,1.2,1.2,1.2,1.2]),
        H298 = (0.6,'kcal/mol','+|-',1.7),
        S298 = (-33.5,'cal/(mol*K)','+|-',1.6),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1179,
    label        = "Cs-C=SCsCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cs U0 {1,S}
4   Cs U0 {1,S}
5   Cs U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.14,6.63,7.51,7.98,8.33,8.38,8.24],'cal/(mol*K)'),
        H298 = (1.36,'kcal/mol'),
        S298 = (-33.92,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 528,
    label        = "Cs-CtCsCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Ct U0 {1,S}
3   Cs U0 {1,S}
4   Cs U0 {1,S}
5   Cs U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.37,6.79,8.09,8.78,9.19,8.96,7.63],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (2.81,'kcal/mol','+|-',0.27),
        S298 = (-35.18,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""Cs-CtCsCsCs BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1834,
    label        = "Cs-(CtN3t)CsCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {4,S} {5,S} {6,S}
2   Ct  U0 {1,S} {3,T}
3   N3t U0 {2,T}
4   Cs  U0 {1,S}
5   Cs  U0 {1,S}
6   Cs  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.4,13.4,14.6,15.3,16.3,16.7,17.2],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (28.3,'kcal/mol','+|-',1.3),
        S298 = (-3,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 529,
    label        = "Cs-CbCsCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Cs U0 {1,S}
4   Cs U0 {1,S}
5   Cs U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.37,6.79,8.09,8.78,9.19,8.96,7.63],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (2.81,'kcal/mol','+|-',0.26),
        S298 = (-35.18,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = u"""Cs-CbCsCsCs BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index        = 530,
    label        = "Cs-CdsCdsCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   {Cd,CO} U0 {1,S}
3   {Cd,CO} U0 {1,S}
4   Cs      U0 {1,S}
5   Cs      U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 531,
    label        = "Cs-(Cds-Od)(Cds-Od)CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   CO U0 {1,S}
4   Cs U0 {1,S}
5   Cs U0 {1,S}
""",
    thermo = u'Cs-CsCsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 532,
    label        = "Cs-(Cds-Od)(Cds-Cd)CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cd U0 {1,S}
4   Cs U0 {1,S}
5   Cs U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 533,
    label        = "Cs-(Cds-Od)(Cds-Cds)CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cd U0 {1,S} {6,D}
4   Cs U0 {1,S}
5   Cs U0 {1,S}
6   Cd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Od)CsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 534,
    label        = "Cs-(Cds-Od)(Cds-Cdd)CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cs  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cdd-Cd)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 535,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Od)CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cs  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)CsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 536,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Cd)CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cs  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 537,
    label        = "Cs-(Cds-Cd)(Cds-Cd)CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cd U0 {1,S}
4   Cs U0 {1,S}
5   Cs U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 538,
    label        = "Cs-(Cds-Cds)(Cds-Cds)CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Cs U0 {1,S}
5   Cs U0 {1,S}
6   Cd U0 {2,D}
7   Cd U0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.99,6.04,7.43,8.26,8.92,8.96,8.23],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (1.68,'kcal/mol','+|-',0.26),
        S298 = (-34.72,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = u"""Cs-CdCdCsCs BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index        = 539,
    label        = "Cs-(Cds-Cdd)(Cds-Cds)CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cs  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D}
7   Cd  U0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cds)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 540,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cds)CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cs  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)CsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cds)CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cs  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 541,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cs  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 542,
    label        = "Cs-(Cds-Cdd)(Cds-Cdd)CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cs  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D}
7   Cdd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 543,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cs  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Od  U0 {6,D}
9   Od  U0 {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.73,8.1,9.02,9.53,9.66,9.52,8.93],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (-2.987,'kcal/mol','+|-',0.26),
        S298 = (-36.46,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = u"""{C/C2/CCO2} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""

""",
)

entry(
    index        = 544,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cs  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Od  U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)(Cds-Cds)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cs  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Sd  U0 {6,D}
9   Sd  U0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Cd)CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cs  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Sd  U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 545,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cs  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   C   U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cd)CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S}
4   Cs U0 {1,S}
5   Cs U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cds)CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {7,D}
3   Cd U0 {1,S} {6,D}
4   Cs U0 {1,S}
5   Cs U0 {1,S}
6   Cd U0 {3,D}
7   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd)CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {7,D}
3   Cd  U0 {1,S} {6,D}
4   Cs  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {3,D}
7   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Sd)CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {6,D}
4   Cs  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   Sd  U0 {6,D}
8   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Cd)CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {6,D}
4   Cs  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
8   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=SCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Cs U0 {1,S}
5   Cs U0 {1,S}
6   Sd U0 {2,D}
7   Sd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 546,
    label        = "Cs-CtCdsCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   Ct      U0 {1,S}
3   {Cd,CO} U0 {1,S}
4   Cs      U0 {1,S}
5   Cs      U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CtCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 547,
    label        = "Cs-(Cds-Od)CtCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Ct U0 {1,S}
4   Cs U0 {1,S}
5   Cs U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 548,
    label        = "Cs-(Cds-Cd)CtCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Ct U0 {1,S}
4   Cs U0 {1,S}
5   Cs U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CtCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 549,
    label        = "Cs-(Cds-Cds)CtCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Ct U0 {1,S}
4   Cs U0 {1,S}
5   Cs U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.99,6.7,8.16,8.92,9.34,9.16,7.14],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (2.99,'kcal/mol','+|-',0.26),
        S298 = (-34.8,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = u"""Cs-CtCdCsCs BOZZELLI =3D Cs/Cs3/Cd + (Cs/Cs3/Ct - Cs/Cs4)""",
    longDesc = 
u"""

""",
)

entry(
    index        = 550,
    label        = "Cs-(Cds-Cdd)CtCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ct  U0 {1,S}
4   Cs  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CtCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 551,
    label        = "Cs-(Cds-Cdd-Od)CtCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ct  U0 {1,S}
4   Cs  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)(Cds-Cds)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)CtCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ct  U0 {1,S}
4   Cs  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 552,
    label        = "Cs-(Cds-Cdd-Cd)CtCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ct  U0 {1,S}
4   Cs  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)CtCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SCtCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Ct U0 {1,S}
4   Cs U0 {1,S}
5   Cs U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 553,
    label        = "Cs-CbCdsCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   Cb      U0 {1,S}
3   {Cd,CO} U0 {1,S}
4   Cs      U0 {1,S}
5   Cs      U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CbCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 554,
    label        = "Cs-(Cds-Od)CbCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cb U0 {1,S}
4   Cs U0 {1,S}
5   Cs U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 555,
    label        = "Cs-(Cds-Cd)CbCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cb U0 {1,S}
4   Cs U0 {1,S}
5   Cs U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CbCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 556,
    label        = "Cs-(Cds-Cds)CbCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cb U0 {1,S}
4   Cs U0 {1,S}
5   Cs U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.99,6.7,8.16,8.92,9.34,9.16,7.14],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (2.99,'kcal/mol','+|-',0.26),
        S298 = (-34.8,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = u"""Cs-CbCdCsCs BOZZELLI =3D Cs/Cs3/Cb + (Cs/Cs3/Cd - Cs/Cs4)""",
    longDesc = 
u"""

""",
)

entry(
    index        = 557,
    label        = "Cs-(Cds-Cdd)CbCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Cs  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CbCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 558,
    label        = "Cs-(Cds-Cdd-Od)CbCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Cs  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)(Cds-Cds)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)CbCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Cs  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 559,
    label        = "Cs-(Cds-Cdd-Cd)CbCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Cs  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)CbCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SCbCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cb U0 {1,S}
4   Cs U0 {1,S}
5   Cs U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 560,
    label        = "Cs-CtCtCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Ct U0 {1,S}
3   Ct U0 {1,S}
4   Cs U0 {1,S}
5   Cs U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.57,5.98,7.51,8.37,9,9.02,8.34],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (1.16,'kcal/mol','+|-',0.26),
        S298 = (-35.26,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = u"""Cs-CtCtCsCs BOZZELLI =3D Cs/Cs3/Ct + (Cs/Cs3/Ct - Cs/Cs4)""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1835,
    label        = "Cs-(CtN3t)(CtN3t)CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {4,S} {6,S} {7,S}
2   Ct  U0 {1,S} {3,T}
3   N3t U0 {2,T}
4   Ct  U0 {1,S} {5,T}
5   N3t U0 {4,T}
6   Cs  U0 {1,S}
7   Cs  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (28.4,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 561,
    label        = "Cs-CbCtCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Ct U0 {1,S}
4   Cs U0 {1,S}
5   Cs U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.57,5.98,7.51,8.37,9,9.02,8.34],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (1.16,'kcal/mol','+|-',0.26),
        S298 = (-35.26,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = u"""Cs-CbCtCsCs BOZZELLI =3D Cs/Cs3/Cb + (Cs/Cs3/Ct - Cs/Cs4)""",
    longDesc = 
u"""

""",
)

entry(
    index        = 562,
    label        = "Cs-CbCbCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Cb U0 {1,S}
4   Cs U0 {1,S}
5   Cs U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.57,5.98,7.51,8.37,9,9.02,8.34],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (1.16,'kcal/mol','+|-',0.26),
        S298 = (-35.26,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = u"""Cs-CbCbCsCs BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index        = 563,
    label        = "Cs-CdsCdsCdsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   {Cd,CO} U0 {1,S}
3   {Cd,CO} U0 {1,S}
4   {Cd,CO} U0 {1,S}
5   Cs      U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 564,
    label        = "Cs-(Cds-Od)(Cds-Od)(Cds-Od)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   CO U0 {1,S}
4   CO U0 {1,S}
5   Cs U0 {1,S}
""",
    thermo = u'Cs-CsCsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 565,
    label        = "Cs-(Cds-Od)(Cds-Od)(Cds-Cd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   CO U0 {1,S}
4   Cd U0 {1,S}
5   Cs U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 566,
    label        = "Cs-(Cds-Od)(Cds-Od)(Cds-Cds)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   CO U0 {1,S}
4   Cd U0 {1,S} {6,D}
5   Cs U0 {1,S}
6   Cd U0 {4,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Od)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 567,
    label        = "Cs-(Cds-Od)(Cds-Od)(Cds-Cdd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   CO  U0 {1,S}
4   Cd  U0 {1,S} {6,D}
5   Cs  U0 {1,S}
6   Cdd U0 {4,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Cd)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 568,
    label        = "Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Od)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   CO  U0 {1,S}
4   Cd  U0 {1,S} {6,D}
5   Cs  U0 {1,S}
6   Cdd U0 {4,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)CsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 569,
    label        = "Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Cd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   CO  U0 {1,S}
4   Cd  U0 {1,S} {6,D}
5   Cs  U0 {1,S}
6   Cdd U0 {4,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 570,
    label        = "Cs-(Cds-Od)(Cds-Cd)(Cds-Cd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cd U0 {1,S}
4   Cd U0 {1,S}
5   Cs U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 571,
    label        = "Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cd U0 {1,S} {6,D}
4   Cd U0 {1,S} {7,D}
5   Cs U0 {1,S}
6   Cd U0 {3,D}
7   Cd U0 {4,D}
""",
    thermo = u'Cs-(Cds-Od)CsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 572,
    label        = "Cs-(Cds-Od)(Cds-Cdd)(Cds-Cds)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Cs  U0 {1,S}
6   Cdd U0 {3,D}
7   Cd  U0 {4,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 573,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Cs  U0 {1,S}
6   Cdd U0 {3,D} {8,D}
7   Cd  U0 {4,D}
8   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cdd-Od)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 574,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cds)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Cs  U0 {1,S}
6   Cdd U0 {3,D} {8,D}
7   Cd  U0 {4,D}
8   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 575,
    label        = "Cs-(Cds-Od)(Cds-Cdd)(Cds-Cdd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Cs  U0 {1,S}
6   Cdd U0 {3,D}
7   Cdd U0 {4,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 576,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Cs  U0 {1,S}
6   Cdd U0 {3,D} {8,D}
7   Cdd U0 {4,D} {9,D}
8   Od  U0 {6,D}
9   Od  U0 {7,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 577,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Cs  U0 {1,S}
6   Cdd U0 {3,D} {8,D}
7   Cdd U0 {4,D} {9,D}
8   Od  U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 578,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Cs  U0 {1,S}
6   Cdd U0 {3,D} {8,D}
7   Cdd U0 {4,D} {9,D}
8   C   U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 579,
    label        = "Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cd U0 {1,S}
4   Cd U0 {1,S}
5   Cs U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 580,
    label        = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Cd U0 {1,S} {8,D}
5   Cs U0 {1,S}
6   Cd U0 {2,D}
7   Cd U0 {3,D}
8   Cd U0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.32,5.86,7.57,8.54,9.22,9.36,8.45],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (2.54,'kcal/mol','+|-',0.26),
        S298 = (-33.96,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = u"""Cs-CdCdCdCs BOZZELLI =3D Cs/Cs2/Cd2 + (Cs/Cs3/Cd - Cs/Cs4)""",
    longDesc = 
u"""

""",
)

entry(
    index        = 581,
    label        = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cd  U0 {1,S} {8,D}
5   Cs  U0 {1,S}
6   Cd  U0 {2,D}
7   Cd  U0 {3,D}
8   Cdd U0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 582,
    label        = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cd  U0 {1,S} {8,D}
5   Cs  U0 {1,S}
6   Cd  U0 {2,D}
7   Cd  U0 {3,D}
8   Cdd U0 {4,D} {9,D}
9   Od  U0 {8,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)CsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Sd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cd  U0 {1,S} {8,D}
5   Cs  U0 {1,S}
6   Cd  U0 {2,D}
7   Cd  U0 {3,D}
8   Cdd U0 {4,D} {9,D}
9   Sd  U0 {8,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 583,
    label        = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cd  U0 {1,S} {8,D}
5   Cs  U0 {1,S}
6   Cd  U0 {2,D}
7   Cd  U0 {3,D}
8   Cdd U0 {4,D} {9,D}
9   C   U0 {8,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 584,
    label        = "Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cd  U0 {1,S} {8,D}
5   Cs  U0 {1,S}
6   Cd  U0 {2,D}
7   Cdd U0 {3,D}
8   Cdd U0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 585,
    label        = "Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cs  U0 {1,S}
6    Cd  U0 {2,D}
7    Cdd U0 {3,D} {9,D}
8    Cdd U0 {4,D} {10,D}
9    Od  U0 {7,D}
10   Od  U0 {8,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 586,
    label        = "Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Cd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cs  U0 {1,S}
6    Cd  U0 {2,D}
7    Cdd U0 {3,D} {9,D}
8    Cdd U0 {4,D} {10,D}
9    Od  U0 {7,D}
10   C   U0 {8,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cds)(Cds-Cdd-Sd)(Cds-Cdd-Sd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cs  U0 {1,S}
6    Cd  U0 {2,D}
7    Cdd U0 {3,D} {9,D}
8    Cdd U0 {4,D} {10,D}
9    Sd  U0 {7,D}
10   Sd  U0 {8,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cds)(Cds-Cdd-Sd)(Cds-Cdd-Cd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cs  U0 {1,S}
6    Cd  U0 {2,D}
7    Cdd U0 {3,D} {9,D}
8    Cdd U0 {4,D} {10,D}
9    Sd  U0 {7,D}
10   C   U0 {8,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 587,
    label        = "Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cs  U0 {1,S}
6    Cd  U0 {2,D}
7    Cdd U0 {3,D} {9,D}
8    Cdd U0 {4,D} {10,D}
9    C   U0 {7,D}
10   C   U0 {8,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 588,
    label        = "Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cd  U0 {1,S} {8,D}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D}
7   Cdd U0 {3,D}
8   Cdd U0 {4,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 589,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cs  U0 {1,S}
6    Cdd U0 {2,D} {9,D}
7    Cdd U0 {3,D} {10,D}
8    Cdd U0 {4,D} {11,D}
9    Od  U0 {6,D}
10   Od  U0 {7,D}
11   Od  U0 {8,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 590,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cs  U0 {1,S}
6    Cdd U0 {2,D} {9,D}
7    Cdd U0 {3,D} {10,D}
8    Cdd U0 {4,D} {11,D}
9    Od  U0 {6,D}
10   Od  U0 {7,D}
11   C   U0 {8,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 591,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cs  U0 {1,S}
6    Cdd U0 {2,D} {9,D}
7    Cdd U0 {3,D} {10,D}
8    Cdd U0 {4,D} {11,D}
9    Od  U0 {6,D}
10   C   U0 {7,D}
11   C   U0 {8,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)(Cds-Cdd-Sd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cs  U0 {1,S}
6    Cdd U0 {2,D} {9,D}
7    Cdd U0 {3,D} {10,D}
8    Cdd U0 {4,D} {11,D}
9    Sd  U0 {6,D}
10   Sd  U0 {7,D}
11   Sd  U0 {8,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)(Cds-Cdd-Cd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cs  U0 {1,S}
6    Cdd U0 {2,D} {9,D}
7    Cdd U0 {3,D} {10,D}
8    Cdd U0 {4,D} {11,D}
9    Sd  U0 {6,D}
10   Sd  U0 {7,D}
11   C   U0 {8,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cs  U0 {1,S}
6    Cdd U0 {2,D} {9,D}
7    Cdd U0 {3,D} {10,D}
8    Cdd U0 {4,D} {11,D}
9    Sd  U0 {6,D}
10   C   U0 {7,D}
11   C   U0 {8,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 592,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cs  U0 {1,S}
6    Cdd U0 {2,D} {9,D}
7    Cdd U0 {3,D} {10,D}
8    Cdd U0 {4,D} {11,D}
9    C   U0 {6,D}
10   C   U0 {7,D}
11   C   U0 {8,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cd)(Cds-Cd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S}
4   Cd U0 {1,S}
5   Cs U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cds)(Cds-Cds)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {8,D}
3   Cd U0 {1,S} {6,D}
4   Cd U0 {1,S} {7,D}
5   Cs U0 {1,S}
6   Cd U0 {3,D}
7   Cd U0 {4,D}
8   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd)(Cds-Cds)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Cs  U0 {1,S}
6   Cdd U0 {3,D}
7   Cd  U0 {4,D}
8   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Sd)(Cds-Cds)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {9,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Cs  U0 {1,S}
6   Cdd U0 {3,D} {8,D}
7   Cd  U0 {4,D}
8   Sd  U0 {6,D}
9   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Cd)(Cds-Cds)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {9,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Cs  U0 {1,S}
6   Cdd U0 {3,D} {8,D}
7   Cd  U0 {4,D}
8   C   U0 {6,D}
9   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd)(Cds-Cdd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Cs  U0 {1,S}
6   Cdd U0 {3,D}
7   Cdd U0 {4,D}
8   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Sd)(Cds-Cdd-Sd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {10,D}
3    Cd  U0 {1,S} {6,D}
4    Cd  U0 {1,S} {7,D}
5    Cs  U0 {1,S}
6    Cdd U0 {3,D} {8,D}
7    Cdd U0 {4,D} {9,D}
8    Sd  U0 {6,D}
9    Sd  U0 {7,D}
10   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Sd)(Cds-Cdd-Cd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {10,D}
3    Cd  U0 {1,S} {6,D}
4    Cd  U0 {1,S} {7,D}
5    Cs  U0 {1,S}
6    Cdd U0 {3,D} {8,D}
7    Cdd U0 {4,D} {9,D}
8    Sd  U0 {6,D}
9    C   U0 {7,D}
10   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {10,D}
3    Cd  U0 {1,S} {6,D}
4    Cd  U0 {1,S} {7,D}
5    Cs  U0 {1,S}
6    Cdd U0 {3,D} {8,D}
7    Cdd U0 {4,D} {9,D}
8    C   U0 {6,D}
9    C   U0 {7,D}
10   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=S(Cds-Cd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Cd U0 {1,S}
5   Cs U0 {1,S}
6   Sd U0 {2,D}
7   Sd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=S(Cds-Cds)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {7,D}
3   Cd U0 {1,S} {8,D}
4   Cd U0 {1,S} {6,D}
5   Cs U0 {1,S}
6   Cd U0 {4,D}
7   Sd U0 {2,D}
8   Sd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=S(Cds-Cdd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {7,D}
3   Cd  U0 {1,S} {8,D}
4   Cd  U0 {1,S} {6,D}
5   Cs  U0 {1,S}
6   Cdd U0 {4,D}
7   Sd  U0 {2,D}
8   Sd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=S(Cds-Cdd-Sd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {9,D}
4   Cd  U0 {1,S} {6,D}
5   Cs  U0 {1,S}
6   Cdd U0 {4,D} {7,D}
7   Sd  U0 {6,D}
8   Sd  U0 {2,D}
9   Sd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=S(Cds-Cdd-Cd)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {9,D}
4   Cd  U0 {1,S} {6,D}
5   Cs  U0 {1,S}
6   Cdd U0 {4,D} {7,D}
7   C   U0 {6,D}
8   Sd  U0 {2,D}
9   Sd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=SC=SCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Cd U0 {1,S} {8,D}
5   Cs U0 {1,S}
6   Sd U0 {2,D}
7   Sd U0 {3,D}
8   Sd U0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 593,
    label        = "Cs-CtCdsCdsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   Ct      U0 {1,S}
3   {Cd,CO} U0 {1,S}
4   {Cd,CO} U0 {1,S}
5   Cs      U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 594,
    label        = "Cs-(Cds-Od)(Cds-Od)CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   CO U0 {1,S}
4   Ct U0 {1,S}
5   Cs U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 595,
    label        = "Cs-(Cds-Od)(Cds-Cd)CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cd U0 {1,S}
4   Ct U0 {1,S}
5   Cs U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)CtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 596,
    label        = "Cs-(Cds-Od)(Cds-Cds)CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cd U0 {1,S} {6,D}
4   Ct U0 {1,S}
5   Cs U0 {1,S}
6   Cd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 597,
    label        = "Cs-(Cds-Od)(Cds-Cdd)CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Ct  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cdd-Cd)CtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 598,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Od)CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Ct  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 599,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Cd)CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Ct  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)CtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 600,
    label        = "Cs-(Cds-Cd)(Cds-Cd)CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cd U0 {1,S}
4   Ct U0 {1,S}
5   Cs U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 601,
    label        = "Cs-(Cds-Cds)(Cds-Cds)CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Ct U0 {1,S}
5   Cs U0 {1,S}
6   Cd U0 {2,D}
7   Cd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 602,
    label        = "Cs-(Cds-Cdd)(Cds-Cds)CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ct  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D}
7   Cd  U0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cds)CtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 603,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cds)CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ct  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cds)CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ct  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 604,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ct  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 605,
    label        = "Cs-(Cds-Cdd)(Cds-Cdd)CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ct  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D}
7   Cdd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 606,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ct  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Od  U0 {6,D}
9   Od  U0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 607,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ct  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Od  U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)(Cds-Cds)CtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ct  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Sd  U0 {6,D}
9   Sd  U0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Cd)CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ct  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Sd  U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 608,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ct  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   C   U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cd)CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S}
4   Ct U0 {1,S}
5   Cs U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cds)CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {7,D}
3   Cd U0 {1,S} {6,D}
4   Ct U0 {1,S}
5   Cs U0 {1,S}
6   Cd U0 {3,D}
7   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd)CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {7,D}
3   Cd  U0 {1,S} {6,D}
4   Ct  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {3,D}
7   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Sd)CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {6,D}
4   Ct  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   Sd  U0 {6,D}
8   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Cd)CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {6,D}
4   Ct  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
8   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=SCtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Ct U0 {1,S}
5   Cs U0 {1,S}
6   Sd U0 {2,D}
7   Sd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 609,
    label        = "Cs-CbCdsCdsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   Cb      U0 {1,S}
3   {Cd,CO} U0 {1,S}
4   {Cd,CO} U0 {1,S}
5   Cs      U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CbCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 610,
    label        = "Cs-(Cds-Od)(Cds-Od)CbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   CO U0 {1,S}
4   Cb U0 {1,S}
5   Cs U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 611,
    label        = "Cs-(Cds-Od)(Cds-Cd)CbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cd U0 {1,S}
4   Cb U0 {1,S}
5   Cs U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)CbCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 612,
    label        = "Cs-(Cds-Od)(Cds-Cds)CbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cd U0 {1,S} {6,D}
4   Cb U0 {1,S}
5   Cs U0 {1,S}
6   Cd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 613,
    label        = "Cs-(Cds-Od)(Cds-Cdd)CbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cb  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cdd-Cd)CbCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 614,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Od)CbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cb  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 615,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Cd)CbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cb  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)CbCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 616,
    label        = "Cs-(Cds-Cd)(Cds-Cd)CbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cd U0 {1,S}
4   Cb U0 {1,S}
5   Cs U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CbCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 617,
    label        = "Cs-(Cds-Cds)(Cds-Cds)CbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Cb U0 {1,S}
5   Cs U0 {1,S}
6   Cd U0 {2,D}
7   Cd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 618,
    label        = "Cs-(Cds-Cdd)(Cds-Cds)CbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D}
7   Cd  U0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cds)CbCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 619,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cds)CbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cds)CbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 620,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CbCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 621,
    label        = "Cs-(Cds-Cdd)(Cds-Cdd)CbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D}
7   Cdd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 622,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Od  U0 {6,D}
9   Od  U0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 623,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)CbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Od  U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)(Cds-Cds)CbCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)CbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Sd  U0 {6,D}
9   Sd  U0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Cd)CbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Sd  U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 624,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   C   U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CbCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cd)CbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S}
4   Cb U0 {1,S}
5   Cs U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cds)CbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {7,D}
3   Cd U0 {1,S} {6,D}
4   Cb U0 {1,S}
5   Cs U0 {1,S}
6   Cd U0 {3,D}
7   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd)CbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {7,D}
3   Cd  U0 {1,S} {6,D}
4   Cb  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {3,D}
7   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Sd)CbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {6,D}
4   Cb  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   Sd  U0 {6,D}
8   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Cd)CbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {6,D}
4   Cb  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
8   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=SCbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Cb U0 {1,S}
5   Cs U0 {1,S}
6   Sd U0 {2,D}
7   Sd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 625,
    label        = "Cs-CtCtCdsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   Ct      U0 {1,S}
3   Ct      U0 {1,S}
4   {Cd,CO} U0 {1,S}
5   Cs      U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CtCtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 626,
    label        = "Cs-(Cds-Od)CtCtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Ct U0 {1,S}
4   Ct U0 {1,S}
5   Cs U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 627,
    label        = "Cs-(Cds-Cd)CtCtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Ct U0 {1,S}
4   Ct U0 {1,S}
5   Cs U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CtCtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 628,
    label        = "Cs-(Cds-Cds)CtCtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Ct U0 {1,S}
4   Ct U0 {1,S}
5   Cs U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.99,7.36,8.89,9.58,9.76,9.16,7.25],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (5.1,'kcal/mol','+|-',0.26),
        S298 = (-34.88,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = u"""Cs-CtCtCdCs BOZZELLI =3D Cs/Cd2/Cs2 + (Cs/Cs3/Ct - Cs/Cs4)""",
    longDesc = 
u"""

""",
)

entry(
    index        = 629,
    label        = "Cs-(Cds-Cdd)CtCtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ct  U0 {1,S}
4   Ct  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CtCtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 630,
    label        = "Cs-(Cds-Cdd-Od)CtCtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ct  U0 {1,S}
4   Ct  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)CtCtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ct  U0 {1,S}
4   Ct  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 631,
    label        = "Cs-(Cds-Cdd-Cd)CtCtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ct  U0 {1,S}
4   Ct  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)CtCtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SCtCtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Ct U0 {1,S}
4   Ct U0 {1,S}
5   Cs U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 632,
    label        = "Cs-CbCtCdsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   Cb      U0 {1,S}
3   Ct      U0 {1,S}
4   {Cd,CO} U0 {1,S}
5   Cs      U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CbCtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 633,
    label        = "Cs-(Cds-Od)CbCtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cb U0 {1,S}
4   Ct U0 {1,S}
5   Cs U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)CtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 634,
    label        = "Cs-(Cds-Cd)CbCtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cb U0 {1,S}
4   Ct U0 {1,S}
5   Cs U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CbCtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 635,
    label        = "Cs-(Cds-Cds)CbCtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cb U0 {1,S}
4   Ct U0 {1,S}
5   Cs U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.99,7.36,8.89,9.58,9.76,9.16,7.25],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (5.1,'kcal/mol','+|-',0.26),
        S298 = (-34.88,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = u"""Cs-CbCtCdCs BOZZELLI =3D Cs/Cb/Cd/Cs2 + (Cs/Cs3/Ct - Cs/Cs4)""",
    longDesc = 
u"""

""",
)

entry(
    index        = 636,
    label        = "Cs-(Cds-Cdd)CbCtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Ct  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CbCtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 637,
    label        = "Cs-(Cds-Cdd-Od)CbCtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Ct  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)(Cds-Cds)CtCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)CbCtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Ct  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 638,
    label        = "Cs-(Cds-Cdd-Cd)CbCtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Ct  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.99,7.36,8.89,9.58,9.76,9.16,7.25],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (5.1,'kcal/mol','+|-',0.26),
        S298 = (-34.88,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = u"""Cs-CbCtCdCs BOZZELLI =3D Cs/Cb/Cd/Cs2 + (Cs/Cs3/Ct - Cs/Cs4)""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SCbCtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cb U0 {1,S}
4   Ct U0 {1,S}
5   Cs U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 639,
    label        = "Cs-CbCbCdsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   Cb      U0 {1,S}
3   Cb      U0 {1,S}
4   {Cd,CO} U0 {1,S}
5   Cs      U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CbCbCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 640,
    label        = "Cs-(Cds-Od)CbCbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cb U0 {1,S}
4   Cb U0 {1,S}
5   Cs U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 641,
    label        = "Cs-(Cds-Cd)CbCbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cb U0 {1,S}
4   Cb U0 {1,S}
5   Cs U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CbCbCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 642,
    label        = "Cs-(Cds-Cds)CbCbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cb U0 {1,S}
4   Cb U0 {1,S}
5   Cs U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.99,7.36,8.89,9.58,9.76,9.16,7.25],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (5.1,'kcal/mol','+|-',0.26),
        S298 = (-34.88,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = u"""Cs-CbCbCdCs BOZZELLI =3D Cs/Cs2/Cb2 + (Cs/Cs3/Cd - Cs/Cs4)""",
    longDesc = 
u"""

""",
)

entry(
    index        = 643,
    label        = "Cs-(Cds-Cdd)CbCbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Cb  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CbCbCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 644,
    label        = "Cs-(Cds-Cdd-Od)CbCbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Cb  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)CbCbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Cb  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 645,
    label        = "Cs-(Cds-Cdd-Cd)CbCbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Cb  U0 {1,S}
5   Cs  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)CbCbCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SCbCbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cb U0 {1,S}
4   Cb U0 {1,S}
5   Cs U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 646,
    label        = "Cs-CtCtCtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Ct U0 {1,S}
3   Ct U0 {1,S}
4   Ct U0 {1,S}
5   Cs U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.37,8.11,9.55,10.1,10.03,9.36,6.65],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (6.23,'kcal/mol','+|-',0.26),
        S298 = (-35.34,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = u"""Cs-CtCtCtCs BOZZELLI =3D Cs/Cs2/Ct2 + (Cs/Cs3/Ct - Cs/Cs4)""",
    longDesc = 
u"""

""",
)

entry(
    index        = 647,
    label        = "Cs-CbCtCtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Ct U0 {1,S}
4   Ct U0 {1,S}
5   Cs U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.37,8.11,9.55,10.1,10.03,9.36,6.65],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (6.23,'kcal/mol','+|-',0.26),
        S298 = (-35.34,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = u"""Cs-CbCtCtCs BOZZELLI =3D Cs/Cs2/Cb/Ct + (Cs/Cs3/Ct - Cs/Cs4)""",
    longDesc = 
u"""

""",
)

entry(
    index        = 648,
    label        = "Cs-CbCbCtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Cb U0 {1,S}
4   Ct U0 {1,S}
5   Cs U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.37,8.11,9.55,10.1,10.03,9.36,6.65],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (6.43,'kcal/mol','+|-',0.26),
        S298 = (-35.34,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = u"""Cs-CbCbCtCs BOZZELLI =3D Cs/Cs2/Cb2 + (Cs/Cs3/Ct - Cs/Cs4)""",
    longDesc = 
u"""

""",
)

entry(
    index        = 649,
    label        = "Cs-CbCbCbCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Cb U0 {1,S}
4   Cb U0 {1,S}
5   Cs U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.37,8.11,9.55,10.1,10.03,9.36,6.65],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (6.23,'kcal/mol','+|-',0.26),
        S298 = (-35.34,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = u"""Cs-CbCbCbCs BOZZELLI =3D Cs/Cs2/Cb2 + (Cs/Cs3/Cb - Cs/Cs4)""",
    longDesc = 
u"""

""",
)

entry(
    index        = 650,
    label        = "Cs-CdsCdsCdsCds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   {Cd,CO} U0 {1,S}
3   {Cd,CO} U0 {1,S}
4   {Cd,CO} U0 {1,S}
5   {Cd,CO} U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 651,
    label        = "Cs-(Cds-Od)(Cds-Od)(Cds-Od)(Cds-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   CO U0 {1,S}
4   CO U0 {1,S}
5   CO U0 {1,S}
""",
    thermo = u'Cs-CsCsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 652,
    label        = "Cs-(Cds-Od)(Cds-Od)(Cds-Od)(Cds-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   CO U0 {1,S}
4   CO U0 {1,S}
5   Cd U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Od)(Cds-Od)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 653,
    label        = "Cs-(Cds-Od)(Cds-Od)(Cds-Od)(Cds-Cds)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   CO U0 {1,S}
4   CO U0 {1,S}
5   Cd U0 {1,S} {6,D}
6   Cd U0 {5,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Od)(Cds-Od)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 654,
    label        = "Cs-(Cds-Od)(Cds-Od)(Cds-Od)(Cds-Cdd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   CO  U0 {1,S}
4   CO  U0 {1,S}
5   Cd  U0 {1,S} {6,D}
6   Cdd U0 {5,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Od)(Cds-Od)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 655,
    label        = "Cs-(Cds-Od)(Cds-Od)(Cds-Od)(Cds-Cdd-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   CO  U0 {1,S}
4   CO  U0 {1,S}
5   Cd  U0 {1,S} {6,D}
6   Cdd U0 {5,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)CsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 656,
    label        = "Cs-(Cds-Od)(Cds-Od)(Cds-Od)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   CO  U0 {1,S}
4   CO  U0 {1,S}
5   Cd  U0 {1,S} {6,D}
6   Cdd U0 {5,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Od)(Cds-Od)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 657,
    label        = "Cs-(Cds-Od)(Cds-Od)(Cds-Cd)(Cds-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   CO U0 {1,S}
4   Cd U0 {1,S}
5   Cd U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 658,
    label        = "Cs-(Cds-Od)(Cds-Od)(Cds-Cds)(Cds-Cds)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   CO U0 {1,S}
4   Cd U0 {1,S} {6,D}
5   Cd U0 {1,S} {7,D}
6   Cd U0 {4,D}
7   Cd U0 {5,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Od)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 659,
    label        = "Cs-(Cds-Od)(Cds-Od)(Cds-Cdd)(Cds-Cds)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   CO  U0 {1,S}
4   Cd  U0 {1,S} {6,D}
5   Cd  U0 {1,S} {7,D}
6   Cdd U0 {4,D}
7   Cd  U0 {5,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Cd)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 660,
    label        = "Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   CO  U0 {1,S}
4   Cd  U0 {1,S} {6,D}
5   Cd  U0 {1,S} {7,D}
6   Cdd U0 {4,D} {8,D}
7   Cd  U0 {5,D}
8   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Od)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 661,
    label        = "Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Cd)(Cds-Cds)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   CO  U0 {1,S}
4   Cd  U0 {1,S} {6,D}
5   Cd  U0 {1,S} {7,D}
6   Cdd U0 {4,D} {8,D}
7   Cd  U0 {5,D}
8   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 662,
    label        = "Cs-(Cds-Od)(Cds-Od)(Cds-Cdd)(Cds-Cdd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   CO  U0 {1,S}
4   Cd  U0 {1,S} {6,D}
5   Cd  U0 {1,S} {7,D}
6   Cdd U0 {4,D}
7   Cdd U0 {5,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 663,
    label        = "Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   CO  U0 {1,S}
4   Cd  U0 {1,S} {6,D}
5   Cd  U0 {1,S} {7,D}
6   Cdd U0 {4,D} {8,D}
7   Cdd U0 {5,D} {9,D}
8   Od  U0 {6,D}
9   Od  U0 {7,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 664,
    label        = "Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   CO  U0 {1,S}
4   Cd  U0 {1,S} {6,D}
5   Cd  U0 {1,S} {7,D}
6   Cdd U0 {4,D} {8,D}
7   Cdd U0 {5,D} {9,D}
8   Od  U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 665,
    label        = "Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   CO  U0 {1,S}
4   Cd  U0 {1,S} {6,D}
5   Cd  U0 {1,S} {7,D}
6   Cdd U0 {4,D} {8,D}
7   Cdd U0 {5,D} {9,D}
8   C   U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 666,
    label        = "Cs-(Cds-Od)(Cds-Cd)(Cds-Cd)(Cds-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cd U0 {1,S}
4   Cd U0 {1,S}
5   Cd U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 667,
    label        = "Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)(Cds-Cds)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cd U0 {1,S} {6,D}
4   Cd U0 {1,S} {7,D}
5   Cd U0 {1,S} {8,D}
6   Cd U0 {3,D}
7   Cd U0 {4,D}
8   Cd U0 {5,D}
""",
    thermo = u'Cs-(Cds-Od)CsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 668,
    label        = "Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)(Cds-Cdd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Cd  U0 {1,S} {8,D}
6   Cd  U0 {3,D}
7   Cd  U0 {4,D}
8   Cdd U0 {5,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 669,
    label        = "Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Cd  U0 {1,S} {8,D}
6   Cd  U0 {3,D}
7   Cd  U0 {4,D}
8   Cdd U0 {5,D} {9,D}
9   Od  U0 {8,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cdd-Od)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 670,
    label        = "Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Cd  U0 {1,S} {8,D}
6   Cd  U0 {3,D}
7   Cd  U0 {4,D}
8   Cdd U0 {5,D} {9,D}
9   C   U0 {8,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 671,
    label        = "Cs-(Cds-Od)(Cds-Cds)(Cds-Cdd)(Cds-Cdd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Cd  U0 {1,S} {8,D}
6   Cd  U0 {3,D}
7   Cdd U0 {4,D}
8   Cdd U0 {5,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 672,
    label        = "Cs-(Cds-Od)(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    CO  U0 {1,S}
3    Cd  U0 {1,S} {6,D}
4    Cd  U0 {1,S} {7,D}
5    Cd  U0 {1,S} {8,D}
6    Cd  U0 {3,D}
7    Cdd U0 {4,D} {9,D}
8    Cdd U0 {5,D} {10,D}
9    Od  U0 {7,D}
10   Od  U0 {8,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 673,
    label        = "Cs-(Cds-Od)(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    CO  U0 {1,S}
3    Cd  U0 {1,S} {6,D}
4    Cd  U0 {1,S} {7,D}
5    Cd  U0 {1,S} {8,D}
6    Cd  U0 {3,D}
7    Cdd U0 {4,D} {9,D}
8    Cdd U0 {5,D} {10,D}
9    Od  U0 {7,D}
10   C   U0 {8,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 674,
    label        = "Cs-(Cds-Od)(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    CO  U0 {1,S}
3    Cd  U0 {1,S} {6,D}
4    Cd  U0 {1,S} {7,D}
5    Cd  U0 {1,S} {8,D}
6    Cd  U0 {3,D}
7    Cdd U0 {4,D} {9,D}
8    Cdd U0 {5,D} {10,D}
9    C   U0 {7,D}
10   C   U0 {8,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 675,
    label        = "Cs-(Cds-Od)(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Cd  U0 {1,S} {8,D}
6   Cdd U0 {3,D}
7   Cdd U0 {4,D}
8   Cdd U0 {5,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 676,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    CO  U0 {1,S}
3    Cd  U0 {1,S} {6,D}
4    Cd  U0 {1,S} {7,D}
5    Cd  U0 {1,S} {8,D}
6    Cdd U0 {3,D} {9,D}
7    Cdd U0 {4,D} {10,D}
8    Cdd U0 {5,D} {11,D}
9    Od  U0 {6,D}
10   Od  U0 {7,D}
11   Od  U0 {8,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 677,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    CO  U0 {1,S}
3    Cd  U0 {1,S} {6,D}
4    Cd  U0 {1,S} {7,D}
5    Cd  U0 {1,S} {8,D}
6    Cdd U0 {3,D} {9,D}
7    Cdd U0 {4,D} {10,D}
8    Cdd U0 {5,D} {11,D}
9    Od  U0 {6,D}
10   Od  U0 {7,D}
11   C   U0 {8,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 678,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    CO  U0 {1,S}
3    Cd  U0 {1,S} {6,D}
4    Cd  U0 {1,S} {7,D}
5    Cd  U0 {1,S} {8,D}
6    Cdd U0 {3,D} {9,D}
7    Cdd U0 {4,D} {10,D}
8    Cdd U0 {5,D} {11,D}
9    Od  U0 {6,D}
10   C   U0 {7,D}
11   C   U0 {8,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 679,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    CO  U0 {1,S}
3    Cd  U0 {1,S} {6,D}
4    Cd  U0 {1,S} {7,D}
5    Cd  U0 {1,S} {8,D}
6    Cdd U0 {3,D} {9,D}
7    Cdd U0 {4,D} {10,D}
8    Cdd U0 {5,D} {11,D}
9    C   U0 {6,D}
10   C   U0 {7,D}
11   C   U0 {8,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 680,
    label        = "Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)(Cds-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cd U0 {1,S}
4   Cd U0 {1,S}
5   Cd U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 681,
    label        = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Cd U0 {1,S} {8,D}
5   Cd U0 {1,S} {9,D}
6   Cd U0 {2,D}
7   Cd U0 {3,D}
8   Cd U0 {4,D}
9   Cd U0 {5,D}
""",
    thermo = u'Cs-CsCsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 682,
    label        = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cd  U0 {1,S} {8,D}
5   Cd  U0 {1,S} {9,D}
6   Cd  U0 {2,D}
7   Cd  U0 {3,D}
8   Cd  U0 {4,D}
9   Cdd U0 {5,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 683,
    label        = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cd  U0 {1,S} {9,D}
6    Cd  U0 {2,D}
7    Cd  U0 {3,D}
8    Cd  U0 {4,D}
9    Cdd U0 {5,D} {10,D}
10   Od  U0 {9,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)CsCsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Sd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cd  U0 {1,S} {9,D}
6    Cd  U0 {2,D}
7    Cd  U0 {3,D}
8    Cd  U0 {4,D}
9    Cdd U0 {5,D} {10,D}
10   Sd  U0 {9,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 684,
    label        = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cd  U0 {1,S} {9,D}
6    Cd  U0 {2,D}
7    Cd  U0 {3,D}
8    Cd  U0 {4,D}
9    Cdd U0 {5,D} {10,D}
10   C   U0 {9,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 685,
    label        = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)(Cds-Cdd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cd  U0 {1,S} {8,D}
5   Cd  U0 {1,S} {9,D}
6   Cd  U0 {2,D}
7   Cd  U0 {3,D}
8   Cdd U0 {4,D}
9   Cdd U0 {5,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 686,
    label        = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cd  U0 {1,S} {9,D}
6    Cd  U0 {2,D}
7    Cd  U0 {3,D}
8    Cdd U0 {4,D} {10,D}
9    Cdd U0 {5,D} {11,D}
10   Od  U0 {8,D}
11   Od  U0 {9,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 687,
    label        = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cd  U0 {1,S} {9,D}
6    Cd  U0 {2,D}
7    Cd  U0 {3,D}
8    Cdd U0 {4,D} {10,D}
9    Cdd U0 {5,D} {11,D}
10   Od  U0 {8,D}
11   C   U0 {9,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Sd)(Cds-Cdd-Sd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cd  U0 {1,S} {9,D}
6    Cd  U0 {2,D}
7    Cd  U0 {3,D}
8    Cdd U0 {4,D} {10,D}
9    Cdd U0 {5,D} {11,D}
10   Sd  U0 {8,D}
11   Sd  U0 {9,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Sd)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cd  U0 {1,S} {9,D}
6    Cd  U0 {2,D}
7    Cd  U0 {3,D}
8    Cdd U0 {4,D} {10,D}
9    Cdd U0 {5,D} {11,D}
10   Sd  U0 {8,D}
11   C   U0 {9,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 688,
    label        = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cd  U0 {1,S} {9,D}
6    Cd  U0 {2,D}
7    Cd  U0 {3,D}
8    Cdd U0 {4,D} {10,D}
9    Cdd U0 {5,D} {11,D}
10   C   U0 {8,D}
11   C   U0 {9,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 689,
    label        = "Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cd  U0 {1,S} {8,D}
5   Cd  U0 {1,S} {9,D}
6   Cd  U0 {2,D}
7   Cdd U0 {3,D}
8   Cdd U0 {4,D}
9   Cdd U0 {5,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 690,
    label        = "Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cd  U0 {1,S} {9,D}
6    Cd  U0 {2,D}
7    Cdd U0 {3,D} {10,D}
8    Cdd U0 {4,D} {11,D}
9    Cdd U0 {5,D} {12,D}
10   Od  U0 {7,D}
11   Od  U0 {8,D}
12   Od  U0 {9,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)Cs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 691,
    label        = "Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cd  U0 {1,S} {9,D}
6    Cd  U0 {2,D}
7    Cdd U0 {3,D} {10,D}
8    Cdd U0 {4,D} {11,D}
9    Cdd U0 {5,D} {12,D}
10   Od  U0 {7,D}
11   Od  U0 {8,D}
12   C   U0 {9,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 692,
    label        = "Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cd  U0 {1,S} {9,D}
6    Cd  U0 {2,D}
7    Cdd U0 {3,D} {10,D}
8    Cdd U0 {4,D} {11,D}
9    Cdd U0 {5,D} {12,D}
10   Od  U0 {7,D}
11   C   U0 {8,D}
12   C   U0 {9,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cds)(Cds-Cdd-Sd)(Cds-Cdd-Sd)(Cds-Cdd-Sd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cd  U0 {1,S} {9,D}
6    Cd  U0 {2,D}
7    Cdd U0 {3,D} {10,D}
8    Cdd U0 {4,D} {11,D}
9    Cdd U0 {5,D} {12,D}
10   Sd  U0 {7,D}
11   Sd  U0 {8,D}
12   Sd  U0 {9,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cds)(Cds-Cdd-Sd)(Cds-Cdd-Sd)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cd  U0 {1,S} {9,D}
6    Cd  U0 {2,D}
7    Cdd U0 {3,D} {10,D}
8    Cdd U0 {4,D} {11,D}
9    Cdd U0 {5,D} {12,D}
10   Sd  U0 {7,D}
11   Sd  U0 {8,D}
12   C   U0 {9,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cds)(Cds-Cdd-Sd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cd  U0 {1,S} {9,D}
6    Cd  U0 {2,D}
7    Cdd U0 {3,D} {10,D}
8    Cdd U0 {4,D} {11,D}
9    Cdd U0 {5,D} {12,D}
10   Sd  U0 {7,D}
11   C   U0 {8,D}
12   C   U0 {9,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 693,
    label        = "Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cd  U0 {1,S} {9,D}
6    Cd  U0 {2,D}
7    Cdd U0 {3,D} {10,D}
8    Cdd U0 {4,D} {11,D}
9    Cdd U0 {5,D} {12,D}
10   C   U0 {7,D}
11   C   U0 {8,D}
12   C   U0 {9,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 694,
    label        = "Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cd  U0 {1,S} {8,D}
5   Cd  U0 {1,S} {9,D}
6   Cdd U0 {2,D}
7   Cdd U0 {3,D}
8   Cdd U0 {4,D}
9   Cdd U0 {5,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 695,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cd  U0 {1,S} {9,D}
6    Cdd U0 {2,D} {10,D}
7    Cdd U0 {3,D} {11,D}
8    Cdd U0 {4,D} {12,D}
9    Cdd U0 {5,D} {13,D}
10   Od  U0 {6,D}
11   Od  U0 {7,D}
12   Od  U0 {8,D}
13   Od  U0 {9,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 696,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cd  U0 {1,S} {9,D}
6    Cdd U0 {2,D} {10,D}
7    Cdd U0 {3,D} {11,D}
8    Cdd U0 {4,D} {12,D}
9    Cdd U0 {5,D} {13,D}
10   Od  U0 {6,D}
11   Od  U0 {7,D}
12   Od  U0 {8,D}
13   C   U0 {9,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 697,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cd  U0 {1,S} {9,D}
6    Cdd U0 {2,D} {10,D}
7    Cdd U0 {3,D} {11,D}
8    Cdd U0 {4,D} {12,D}
9    Cdd U0 {5,D} {13,D}
10   Od  U0 {6,D}
11   Od  U0 {7,D}
12   C   U0 {8,D}
13   C   U0 {9,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 698,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cd  U0 {1,S} {9,D}
6    Cdd U0 {2,D} {10,D}
7    Cdd U0 {3,D} {11,D}
8    Cdd U0 {4,D} {12,D}
9    Cdd U0 {5,D} {13,D}
10   Od  U0 {6,D}
11   C   U0 {7,D}
12   C   U0 {8,D}
13   C   U0 {9,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)(Cds-Cdd-Sd)(Cds-Cdd-Sd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cd  U0 {1,S} {9,D}
6    Cdd U0 {2,D} {10,D}
7    Cdd U0 {3,D} {11,D}
8    Cdd U0 {4,D} {12,D}
9    Cdd U0 {5,D} {13,D}
10   Sd  U0 {6,D}
11   Sd  U0 {7,D}
12   Sd  U0 {8,D}
13   Sd  U0 {9,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)(Cds-Cdd-Sd)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cd  U0 {1,S} {9,D}
6    Cdd U0 {2,D} {10,D}
7    Cdd U0 {3,D} {11,D}
8    Cdd U0 {4,D} {12,D}
9    Cdd U0 {5,D} {13,D}
10   Sd  U0 {6,D}
11   Sd  U0 {7,D}
12   Sd  U0 {8,D}
13   C   U0 {9,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cd  U0 {1,S} {9,D}
6    Cdd U0 {2,D} {10,D}
7    Cdd U0 {3,D} {11,D}
8    Cdd U0 {4,D} {12,D}
9    Cdd U0 {5,D} {13,D}
10   Sd  U0 {6,D}
11   Sd  U0 {7,D}
12   C   U0 {8,D}
13   C   U0 {9,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cd  U0 {1,S} {9,D}
6    Cdd U0 {2,D} {10,D}
7    Cdd U0 {3,D} {11,D}
8    Cdd U0 {4,D} {12,D}
9    Cdd U0 {5,D} {13,D}
10   Sd  U0 {6,D}
11   C   U0 {7,D}
12   C   U0 {8,D}
13   C   U0 {9,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 699,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cd  U0 {1,S} {9,D}
6    Cdd U0 {2,D} {10,D}
7    Cdd U0 {3,D} {11,D}
8    Cdd U0 {4,D} {12,D}
9    Cdd U0 {5,D} {13,D}
10   C   U0 {6,D}
11   C   U0 {7,D}
12   C   U0 {8,D}
13   C   U0 {9,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cd)(Cds-Cd)(Cds-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S}
4   Cd U0 {1,S}
5   Cd U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cds)(Cds-Cds)(Cds-Cds)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {9,D}
3   Cd U0 {1,S} {6,D}
4   Cd U0 {1,S} {7,D}
5   Cd U0 {1,S} {8,D}
6   Cd U0 {3,D}
7   Cd U0 {4,D}
8   Cd U0 {5,D}
9   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cds)(Cds-Cds)(Cds-Cdd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {9,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Cd  U0 {1,S} {8,D}
6   Cd  U0 {3,D}
7   Cd  U0 {4,D}
8   Cdd U0 {5,D}
9   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cds)(Cds-Cds)(Cds-Cdd-Sd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {10,D}
3    Cd  U0 {1,S} {6,D}
4    Cd  U0 {1,S} {7,D}
5    Cd  U0 {1,S} {8,D}
6    Cd  U0 {3,D}
7    Cd  U0 {4,D}
8    Cdd U0 {5,D} {9,D}
9    Sd  U0 {8,D}
10   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {10,D}
3    Cd  U0 {1,S} {6,D}
4    Cd  U0 {1,S} {7,D}
5    Cd  U0 {1,S} {8,D}
6    Cd  U0 {3,D}
7    Cd  U0 {4,D}
8    Cdd U0 {5,D} {9,D}
9    C   U0 {8,D}
10   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cds)(Cds-Cdd)(Cds-Cdd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {9,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Cd  U0 {1,S} {8,D}
6   Cd  U0 {3,D}
7   Cdd U0 {4,D}
8   Cdd U0 {5,D}
9   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cds)(Cds-Cdd-Sd)(Cds-Cdd-Sd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {11,D}
3    Cd  U0 {1,S} {6,D}
4    Cd  U0 {1,S} {7,D}
5    Cd  U0 {1,S} {8,D}
6    Cd  U0 {3,D}
7    Cdd U0 {4,D} {9,D}
8    Cdd U0 {5,D} {10,D}
9    Sd  U0 {7,D}
10   Sd  U0 {8,D}
11   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cds)(Cds-Cdd-Sd)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {11,D}
3    Cd  U0 {1,S} {6,D}
4    Cd  U0 {1,S} {7,D}
5    Cd  U0 {1,S} {8,D}
6    Cd  U0 {3,D}
7    Cdd U0 {4,D} {9,D}
8    Cdd U0 {5,D} {10,D}
9    Sd  U0 {7,D}
10   C   U0 {8,D}
11   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {11,D}
3    Cd  U0 {1,S} {6,D}
4    Cd  U0 {1,S} {7,D}
5    Cd  U0 {1,S} {8,D}
6    Cd  U0 {3,D}
7    Cdd U0 {4,D} {9,D}
8    Cdd U0 {5,D} {10,D}
9    C   U0 {7,D}
10   C   U0 {8,D}
11   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {9,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Cd  U0 {1,S} {8,D}
6   Cdd U0 {3,D}
7   Cdd U0 {4,D}
8   Cdd U0 {5,D}
9   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Sd)(Cds-Cdd-Sd)(Cds-Cdd-Sd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {12,D}
3    Cd  U0 {1,S} {6,D}
4    Cd  U0 {1,S} {7,D}
5    Cd  U0 {1,S} {8,D}
6    Cdd U0 {3,D} {9,D}
7    Cdd U0 {4,D} {10,D}
8    Cdd U0 {5,D} {11,D}
9    Sd  U0 {6,D}
10   Sd  U0 {7,D}
11   Sd  U0 {8,D}
12   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Sd)(Cds-Cdd-Sd)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {12,D}
3    Cd  U0 {1,S} {6,D}
4    Cd  U0 {1,S} {7,D}
5    Cd  U0 {1,S} {8,D}
6    Cdd U0 {3,D} {9,D}
7    Cdd U0 {4,D} {10,D}
8    Cdd U0 {5,D} {11,D}
9    Sd  U0 {6,D}
10   Sd  U0 {7,D}
11   C   U0 {8,D}
12   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Sd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {12,D}
3    Cd  U0 {1,S} {6,D}
4    Cd  U0 {1,S} {7,D}
5    Cd  U0 {1,S} {8,D}
6    Cdd U0 {3,D} {9,D}
7    Cdd U0 {4,D} {10,D}
8    Cdd U0 {5,D} {11,D}
9    Sd  U0 {6,D}
10   C   U0 {7,D}
11   C   U0 {8,D}
12   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {12,D}
3    Cd  U0 {1,S} {6,D}
4    Cd  U0 {1,S} {7,D}
5    Cd  U0 {1,S} {8,D}
6    Cdd U0 {3,D} {9,D}
7    Cdd U0 {4,D} {10,D}
8    Cdd U0 {5,D} {11,D}
9    C   U0 {6,D}
10   C   U0 {7,D}
11   C   U0 {8,D}
12   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=S(Cds-Cd)(Cds-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Cd U0 {1,S}
5   Cd U0 {1,S}
6   Sd U0 {2,D}
7   Sd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=S(Cds-Cds)(Cds-Cds)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {8,D}
3   Cd U0 {1,S} {9,D}
4   Cd U0 {1,S} {6,D}
5   Cd U0 {1,S} {7,D}
6   Cd U0 {4,D}
7   Cd U0 {5,D}
8   Sd U0 {2,D}
9   Sd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=S(Cds-Cdd)(Cds-Cds)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {9,D}
4   Cd  U0 {1,S} {6,D}
5   Cd  U0 {1,S} {7,D}
6   Cdd U0 {4,D}
7   Cd  U0 {5,D}
8   Sd  U0 {2,D}
9   Sd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=S(Cds-Cdd-Sd)(Cds-Cds)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {9,D}
3    Cd  U0 {1,S} {10,D}
4    Cd  U0 {1,S} {6,D}
5    Cd  U0 {1,S} {7,D}
6    Cdd U0 {4,D} {8,D}
7    Cd  U0 {5,D}
8    Sd  U0 {6,D}
9    Sd  U0 {2,D}
10   Sd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=S(Cds-Cdd-Cd)(Cds-Cds)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {9,D}
3    Cd  U0 {1,S} {10,D}
4    Cd  U0 {1,S} {6,D}
5    Cd  U0 {1,S} {7,D}
6    Cdd U0 {4,D} {8,D}
7    Cd  U0 {5,D}
8    C   U0 {6,D}
9    Sd  U0 {2,D}
10   Sd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=S(Cds-Cdd)(Cds-Cdd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {9,D}
4   Cd  U0 {1,S} {6,D}
5   Cd  U0 {1,S} {7,D}
6   Cdd U0 {4,D}
7   Cdd U0 {5,D}
8   Sd  U0 {2,D}
9   Sd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=S(Cds-Cdd-Sd)(Cds-Cdd-Sd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {10,D}
3    Cd  U0 {1,S} {11,D}
4    Cd  U0 {1,S} {6,D}
5    Cd  U0 {1,S} {7,D}
6    Cdd U0 {4,D} {8,D}
7    Cdd U0 {5,D} {9,D}
8    Sd  U0 {6,D}
9    Sd  U0 {7,D}
10   Sd  U0 {2,D}
11   Sd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=S(Cds-Cdd-Sd)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {10,D}
3    Cd  U0 {1,S} {11,D}
4    Cd  U0 {1,S} {6,D}
5    Cd  U0 {1,S} {7,D}
6    Cdd U0 {4,D} {8,D}
7    Cdd U0 {5,D} {9,D}
8    Sd  U0 {6,D}
9    C   U0 {7,D}
10   Sd  U0 {2,D}
11   Sd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=S(Cds-Cdd-Cd)(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {10,D}
3    Cd  U0 {1,S} {11,D}
4    Cd  U0 {1,S} {6,D}
5    Cd  U0 {1,S} {7,D}
6    Cdd U0 {4,D} {8,D}
7    Cdd U0 {5,D} {9,D}
8    C   U0 {6,D}
9    C   U0 {7,D}
10   Sd  U0 {2,D}
11   Sd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=SC=S(Cds-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Cd U0 {1,S} {8,D}
5   Cd U0 {1,S}
6   Sd U0 {2,D}
7   Sd U0 {3,D}
8   Sd U0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=SC=S(Cds-Cds)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {7,D}
3   Cd U0 {1,S} {8,D}
4   Cd U0 {1,S} {9,D}
5   Cd U0 {1,S} {6,D}
6   Cd U0 {5,D}
7   Sd U0 {2,D}
8   Sd U0 {3,D}
9   Sd U0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=SC=S(Cds-Cdd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {7,D}
3   Cd  U0 {1,S} {8,D}
4   Cd  U0 {1,S} {9,D}
5   Cd  U0 {1,S} {6,D}
6   Cdd U0 {5,D}
7   Sd  U0 {2,D}
8   Sd  U0 {3,D}
9   Sd  U0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=SC=S(Cds-Cdd-Sd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {8,D}
3    Cd  U0 {1,S} {9,D}
4    Cd  U0 {1,S} {10,D}
5    Cd  U0 {1,S} {6,D}
6    Cdd U0 {5,D} {7,D}
7    Sd  U0 {6,D}
8    Sd  U0 {2,D}
9    Sd  U0 {3,D}
10   Sd  U0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=SC=S(Cds-Cdd-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {8,D}
3    Cd  U0 {1,S} {9,D}
4    Cd  U0 {1,S} {10,D}
5    Cd  U0 {1,S} {6,D}
6    Cdd U0 {5,D} {7,D}
7    C   U0 {6,D}
8    Sd  U0 {2,D}
9    Sd  U0 {3,D}
10   Sd  U0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=SC=SC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Cd U0 {1,S} {8,D}
5   Cd U0 {1,S} {9,D}
6   Sd U0 {2,D}
7   Sd U0 {3,D}
8   Sd U0 {4,D}
9   Sd U0 {5,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 700,
    label        = "Cs-CtCdsCdsCds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   Ct      U0 {1,S}
3   {Cd,CO} U0 {1,S}
4   {Cd,CO} U0 {1,S}
5   {Cd,CO} U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 701,
    label        = "Cs-(Cds-Od)(Cds-Od)(Cds-Od)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   CO U0 {1,S}
4   CO U0 {1,S}
5   Ct U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Od)(Cds-Od)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 702,
    label        = "Cs-(Cds-Od)(Cds-Od)(Cds-Cd)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   CO U0 {1,S}
4   Cd U0 {1,S}
5   Ct U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 703,
    label        = "Cs-(Cds-Od)(Cds-Od)(Cds-Cds)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   CO U0 {1,S}
4   Cd U0 {1,S} {6,D}
5   Ct U0 {1,S}
6   Cd U0 {4,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 704,
    label        = "Cs-(Cds-Od)(Cds-Od)(Cds-Cdd)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   CO  U0 {1,S}
4   Cd  U0 {1,S} {6,D}
5   Ct  U0 {1,S}
6   Cdd U0 {4,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Cd)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 705,
    label        = "Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Od)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   CO  U0 {1,S}
4   Cd  U0 {1,S} {6,D}
5   Ct  U0 {1,S}
6   Cdd U0 {4,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 706,
    label        = "Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Cd)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   CO  U0 {1,S}
4   Cd  U0 {1,S} {6,D}
5   Ct  U0 {1,S}
6   Cdd U0 {4,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 707,
    label        = "Cs-(Cds-Od)(Cds-Cd)(Cds-Cd)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cd U0 {1,S}
4   Cd U0 {1,S}
5   Ct U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 708,
    label        = "Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cd U0 {1,S} {6,D}
4   Cd U0 {1,S} {7,D}
5   Ct U0 {1,S}
6   Cd U0 {3,D}
7   Cd U0 {4,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 709,
    label        = "Cs-(Cds-Od)(Cds-Cdd)(Cds-Cds)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Ct  U0 {1,S}
6   Cdd U0 {3,D}
7   Cd  U0 {4,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 710,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Ct  U0 {1,S}
6   Cdd U0 {3,D} {8,D}
7   Cd  U0 {4,D}
8   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 711,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cds)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Ct  U0 {1,S}
6   Cdd U0 {3,D} {8,D}
7   Cd  U0 {4,D}
8   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 712,
    label        = "Cs-(Cds-Od)(Cds-Cdd)(Cds-Cdd)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Ct  U0 {1,S}
6   Cdd U0 {3,D}
7   Cdd U0 {4,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 713,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Ct  U0 {1,S}
6   Cdd U0 {3,D} {8,D}
7   Cdd U0 {4,D} {9,D}
8   Od  U0 {6,D}
9   Od  U0 {7,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 714,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Ct  U0 {1,S}
6   Cdd U0 {3,D} {8,D}
7   Cdd U0 {4,D} {9,D}
8   Od  U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 715,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Ct  U0 {1,S}
6   Cdd U0 {3,D} {8,D}
7   Cdd U0 {4,D} {9,D}
8   C   U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 716,
    label        = "Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cd U0 {1,S}
4   Cd U0 {1,S}
5   Ct U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 717,
    label        = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Cd U0 {1,S} {8,D}
5   Ct U0 {1,S}
6   Cd U0 {2,D}
7   Cd U0 {3,D}
8   Cd U0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 718,
    label        = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cd  U0 {1,S} {8,D}
5   Ct  U0 {1,S}
6   Cd  U0 {2,D}
7   Cd  U0 {3,D}
8   Cdd U0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 719,
    label        = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cd  U0 {1,S} {8,D}
5   Ct  U0 {1,S}
6   Cd  U0 {2,D}
7   Cd  U0 {3,D}
8   Cdd U0 {4,D} {9,D}
9   Od  U0 {8,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Sd)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cd  U0 {1,S} {8,D}
5   Ct  U0 {1,S}
6   Cd  U0 {2,D}
7   Cd  U0 {3,D}
8   Cdd U0 {4,D} {9,D}
9   Sd  U0 {8,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 720,
    label        = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cd  U0 {1,S} {8,D}
5   Ct  U0 {1,S}
6   Cd  U0 {2,D}
7   Cd  U0 {3,D}
8   Cdd U0 {4,D} {9,D}
9   C   U0 {8,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 721,
    label        = "Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cd  U0 {1,S} {8,D}
5   Ct  U0 {1,S}
6   Cd  U0 {2,D}
7   Cdd U0 {3,D}
8   Cdd U0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 722,
    label        = "Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Ct  U0 {1,S}
6    Cd  U0 {2,D}
7    Cdd U0 {3,D} {9,D}
8    Cdd U0 {4,D} {10,D}
9    Od  U0 {7,D}
10   Od  U0 {8,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 723,
    label        = "Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Cd)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Ct  U0 {1,S}
6    Cd  U0 {2,D}
7    Cdd U0 {3,D} {9,D}
8    Cdd U0 {4,D} {10,D}
9    Od  U0 {7,D}
10   C   U0 {8,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cds)(Cds-Cdd-Sd)(Cds-Cdd-Sd)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Ct  U0 {1,S}
6    Cd  U0 {2,D}
7    Cdd U0 {3,D} {9,D}
8    Cdd U0 {4,D} {10,D}
9    Sd  U0 {7,D}
10   Sd  U0 {8,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cds)(Cds-Cdd-Sd)(Cds-Cdd-Cd)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Ct  U0 {1,S}
6    Cd  U0 {2,D}
7    Cdd U0 {3,D} {9,D}
8    Cdd U0 {4,D} {10,D}
9    Sd  U0 {7,D}
10   C   U0 {8,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 724,
    label        = "Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Ct  U0 {1,S}
6    Cd  U0 {2,D}
7    Cdd U0 {3,D} {9,D}
8    Cdd U0 {4,D} {10,D}
9    C   U0 {7,D}
10   C   U0 {8,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 725,
    label        = "Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cd  U0 {1,S} {8,D}
5   Ct  U0 {1,S}
6   Cdd U0 {2,D}
7   Cdd U0 {3,D}
8   Cdd U0 {4,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 726,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Ct  U0 {1,S}
6    Cdd U0 {2,D} {9,D}
7    Cdd U0 {3,D} {10,D}
8    Cdd U0 {4,D} {11,D}
9    Od  U0 {6,D}
10   Od  U0 {7,D}
11   Od  U0 {8,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 727,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Ct  U0 {1,S}
6    Cdd U0 {2,D} {9,D}
7    Cdd U0 {3,D} {10,D}
8    Cdd U0 {4,D} {11,D}
9    Od  U0 {6,D}
10   Od  U0 {7,D}
11   C   U0 {8,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 728,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Ct  U0 {1,S}
6    Cdd U0 {2,D} {9,D}
7    Cdd U0 {3,D} {10,D}
8    Cdd U0 {4,D} {11,D}
9    Od  U0 {6,D}
10   C   U0 {7,D}
11   C   U0 {8,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)(Cds-Cdd-Sd)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Ct  U0 {1,S}
6    Cdd U0 {2,D} {9,D}
7    Cdd U0 {3,D} {10,D}
8    Cdd U0 {4,D} {11,D}
9    Sd  U0 {6,D}
10   Sd  U0 {7,D}
11   Sd  U0 {8,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)(Cds-Cdd-Cd)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Ct  U0 {1,S}
6    Cdd U0 {2,D} {9,D}
7    Cdd U0 {3,D} {10,D}
8    Cdd U0 {4,D} {11,D}
9    Sd  U0 {6,D}
10   Sd  U0 {7,D}
11   C   U0 {8,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Ct  U0 {1,S}
6    Cdd U0 {2,D} {9,D}
7    Cdd U0 {3,D} {10,D}
8    Cdd U0 {4,D} {11,D}
9    Sd  U0 {6,D}
10   C   U0 {7,D}
11   C   U0 {8,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 729,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Ct  U0 {1,S}
6    Cdd U0 {2,D} {9,D}
7    Cdd U0 {3,D} {10,D}
8    Cdd U0 {4,D} {11,D}
9    C   U0 {6,D}
10   C   U0 {7,D}
11   C   U0 {8,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cd)(Cds-Cd)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S}
4   Cd U0 {1,S}
5   Ct U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cds)(Cds-Cds)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {8,D}
3   Cd U0 {1,S} {6,D}
4   Cd U0 {1,S} {7,D}
5   Ct U0 {1,S}
6   Cd U0 {3,D}
7   Cd U0 {4,D}
8   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd)(Cds-Cds)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Ct  U0 {1,S}
6   Cdd U0 {3,D}
7   Cd  U0 {4,D}
8   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Sd)(Cds-Cds)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {9,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Ct  U0 {1,S}
6   Cdd U0 {3,D} {8,D}
7   Cd  U0 {4,D}
8   Sd  U0 {6,D}
9   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Cd)(Cds-Cds)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {9,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Ct  U0 {1,S}
6   Cdd U0 {3,D} {8,D}
7   Cd  U0 {4,D}
8   C   U0 {6,D}
9   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd)(Cds-Cdd)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Ct  U0 {1,S}
6   Cdd U0 {3,D}
7   Cdd U0 {4,D}
8   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Sd)(Cds-Cdd-Sd)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {10,D}
3    Cd  U0 {1,S} {6,D}
4    Cd  U0 {1,S} {7,D}
5    Ct  U0 {1,S}
6    Cdd U0 {3,D} {8,D}
7    Cdd U0 {4,D} {9,D}
8    Sd  U0 {6,D}
9    Sd  U0 {7,D}
10   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Sd)(Cds-Cdd-Cd)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {10,D}
3    Cd  U0 {1,S} {6,D}
4    Cd  U0 {1,S} {7,D}
5    Ct  U0 {1,S}
6    Cdd U0 {3,D} {8,D}
7    Cdd U0 {4,D} {9,D}
8    Sd  U0 {6,D}
9    C   U0 {7,D}
10   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {10,D}
3    Cd  U0 {1,S} {6,D}
4    Cd  U0 {1,S} {7,D}
5    Ct  U0 {1,S}
6    Cdd U0 {3,D} {8,D}
7    Cdd U0 {4,D} {9,D}
8    C   U0 {6,D}
9    C   U0 {7,D}
10   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=S(Cds-Cd)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Cd U0 {1,S}
5   Ct U0 {1,S}
6   Sd U0 {2,D}
7   Sd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=S(Cds-Cds)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {7,D}
3   Cd U0 {1,S} {8,D}
4   Cd U0 {1,S} {6,D}
5   Ct U0 {1,S}
6   Cd U0 {4,D}
7   Sd U0 {2,D}
8   Sd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=S(Cds-Cdd)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {7,D}
3   Cd  U0 {1,S} {8,D}
4   Cd  U0 {1,S} {6,D}
5   Ct  U0 {1,S}
6   Cdd U0 {4,D}
7   Sd  U0 {2,D}
8   Sd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=S(Cds-Cdd-Sd)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {9,D}
4   Cd  U0 {1,S} {6,D}
5   Ct  U0 {1,S}
6   Cdd U0 {4,D} {7,D}
7   Sd  U0 {6,D}
8   Sd  U0 {2,D}
9   Sd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=S(Cds-Cdd-Cd)Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {9,D}
4   Cd  U0 {1,S} {6,D}
5   Ct  U0 {1,S}
6   Cdd U0 {4,D} {7,D}
7   C   U0 {6,D}
8   Sd  U0 {2,D}
9   Sd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=SC=SCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Cd U0 {1,S} {8,D}
5   Ct U0 {1,S}
6   Sd U0 {2,D}
7   Sd U0 {3,D}
8   Sd U0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 730,
    label        = "Cs-CbCdsCdsCds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   Cb      U0 {1,S}
3   {Cd,CO} U0 {1,S}
4   {Cd,CO} U0 {1,S}
5   {Cd,CO} U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 731,
    label        = "Cs-(Cds-Od)(Cds-Od)(Cds-Od)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   CO U0 {1,S}
4   CO U0 {1,S}
5   Cb U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Od)(Cds-Od)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 732,
    label        = "Cs-(Cds-Od)(Cds-Od)(Cds-Cd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   CO U0 {1,S}
4   Cd U0 {1,S}
5   Cb U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 733,
    label        = "Cs-(Cds-Od)(Cds-Od)(Cds-Cds)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   CO U0 {1,S}
4   Cd U0 {1,S} {6,D}
5   Cb U0 {1,S}
6   Cd U0 {4,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 734,
    label        = "Cs-(Cds-Od)(Cds-Od)(Cds-Cdd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   CO  U0 {1,S}
4   Cd  U0 {1,S} {6,D}
5   Cb  U0 {1,S}
6   Cdd U0 {4,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Cd)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 735,
    label        = "Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Od)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   CO  U0 {1,S}
4   Cd  U0 {1,S} {6,D}
5   Cb  U0 {1,S}
6   Cdd U0 {4,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 736,
    label        = "Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Cd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   CO  U0 {1,S}
4   Cd  U0 {1,S} {6,D}
5   Cb  U0 {1,S}
6   Cdd U0 {4,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 737,
    label        = "Cs-(Cds-Od)(Cds-Cd)(Cds-Cd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cd U0 {1,S}
4   Cd U0 {1,S}
5   Cb U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 738,
    label        = "Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cd U0 {1,S} {6,D}
4   Cd U0 {1,S} {7,D}
5   Cb U0 {1,S}
6   Cd U0 {3,D}
7   Cd U0 {4,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 739,
    label        = "Cs-(Cds-Od)(Cds-Cdd)(Cds-Cds)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Cb  U0 {1,S}
6   Cdd U0 {3,D}
7   Cd  U0 {4,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 740,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Cb  U0 {1,S}
6   Cdd U0 {3,D} {8,D}
7   Cd  U0 {4,D}
8   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 741,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cds)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Cb  U0 {1,S}
6   Cdd U0 {3,D} {8,D}
7   Cd  U0 {4,D}
8   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 742,
    label        = "Cs-(Cds-Od)(Cds-Cdd)(Cds-Cdd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Cb  U0 {1,S}
6   Cdd U0 {3,D}
7   Cdd U0 {4,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 743,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Cb  U0 {1,S}
6   Cdd U0 {3,D} {8,D}
7   Cdd U0 {4,D} {9,D}
8   Od  U0 {6,D}
9   Od  U0 {7,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 744,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Cb  U0 {1,S}
6   Cdd U0 {3,D} {8,D}
7   Cdd U0 {4,D} {9,D}
8   Od  U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 745,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Cb  U0 {1,S}
6   Cdd U0 {3,D} {8,D}
7   Cdd U0 {4,D} {9,D}
8   C   U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 746,
    label        = "Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cd U0 {1,S}
4   Cd U0 {1,S}
5   Cb U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 747,
    label        = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Cd U0 {1,S} {8,D}
5   Cb U0 {1,S}
6   Cd U0 {2,D}
7   Cd U0 {3,D}
8   Cd U0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 748,
    label        = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cd  U0 {1,S} {8,D}
5   Cb  U0 {1,S}
6   Cd  U0 {2,D}
7   Cd  U0 {3,D}
8   Cdd U0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 749,
    label        = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cd  U0 {1,S} {8,D}
5   Cb  U0 {1,S}
6   Cd  U0 {2,D}
7   Cd  U0 {3,D}
8   Cdd U0 {4,D} {9,D}
9   Od  U0 {8,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Sd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cd  U0 {1,S} {8,D}
5   Cb  U0 {1,S}
6   Cd  U0 {2,D}
7   Cd  U0 {3,D}
8   Cdd U0 {4,D} {9,D}
9   Sd  U0 {8,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 750,
    label        = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cd  U0 {1,S} {8,D}
5   Cb  U0 {1,S}
6   Cd  U0 {2,D}
7   Cd  U0 {3,D}
8   Cdd U0 {4,D} {9,D}
9   C   U0 {8,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 751,
    label        = "Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cd  U0 {1,S} {8,D}
5   Cb  U0 {1,S}
6   Cd  U0 {2,D}
7   Cdd U0 {3,D}
8   Cdd U0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 752,
    label        = "Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cb  U0 {1,S}
6    Cd  U0 {2,D}
7    Cdd U0 {3,D} {9,D}
8    Cdd U0 {4,D} {10,D}
9    Od  U0 {7,D}
10   Od  U0 {8,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 753,
    label        = "Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Cd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cb  U0 {1,S}
6    Cd  U0 {2,D}
7    Cdd U0 {3,D} {9,D}
8    Cdd U0 {4,D} {10,D}
9    Od  U0 {7,D}
10   C   U0 {8,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cds)(Cds-Cdd-Sd)(Cds-Cdd-Sd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cb  U0 {1,S}
6    Cd  U0 {2,D}
7    Cdd U0 {3,D} {9,D}
8    Cdd U0 {4,D} {10,D}
9    Sd  U0 {7,D}
10   Sd  U0 {8,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cds)(Cds-Cdd-Sd)(Cds-Cdd-Cd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cb  U0 {1,S}
6    Cd  U0 {2,D}
7    Cdd U0 {3,D} {9,D}
8    Cdd U0 {4,D} {10,D}
9    Sd  U0 {7,D}
10   C   U0 {8,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 754,
    label        = "Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cb  U0 {1,S}
6    Cd  U0 {2,D}
7    Cdd U0 {3,D} {9,D}
8    Cdd U0 {4,D} {10,D}
9    C   U0 {7,D}
10   C   U0 {8,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 755,
    label        = "Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cd  U0 {1,S} {8,D}
5   Cb  U0 {1,S}
6   Cdd U0 {2,D}
7   Cdd U0 {3,D}
8   Cdd U0 {4,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 756,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cb  U0 {1,S}
6    Cdd U0 {2,D} {9,D}
7    Cdd U0 {3,D} {10,D}
8    Cdd U0 {4,D} {11,D}
9    Od  U0 {6,D}
10   Od  U0 {7,D}
11   Od  U0 {8,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 757,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cb  U0 {1,S}
6    Cdd U0 {2,D} {9,D}
7    Cdd U0 {3,D} {10,D}
8    Cdd U0 {4,D} {11,D}
9    Od  U0 {6,D}
10   Od  U0 {7,D}
11   C   U0 {8,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 758,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cb  U0 {1,S}
6    Cdd U0 {2,D} {9,D}
7    Cdd U0 {3,D} {10,D}
8    Cdd U0 {4,D} {11,D}
9    Od  U0 {6,D}
10   C   U0 {7,D}
11   C   U0 {8,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)(Cds-Cdd-Sd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cb  U0 {1,S}
6    Cdd U0 {2,D} {9,D}
7    Cdd U0 {3,D} {10,D}
8    Cdd U0 {4,D} {11,D}
9    Sd  U0 {6,D}
10   Sd  U0 {7,D}
11   Sd  U0 {8,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)(Cds-Cdd-Cd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cb  U0 {1,S}
6    Cdd U0 {2,D} {9,D}
7    Cdd U0 {3,D} {10,D}
8    Cdd U0 {4,D} {11,D}
9    Sd  U0 {6,D}
10   Sd  U0 {7,D}
11   C   U0 {8,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cb  U0 {1,S}
6    Cdd U0 {2,D} {9,D}
7    Cdd U0 {3,D} {10,D}
8    Cdd U0 {4,D} {11,D}
9    Sd  U0 {6,D}
10   C   U0 {7,D}
11   C   U0 {8,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 759,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Cb  U0 {1,S}
6    Cdd U0 {2,D} {9,D}
7    Cdd U0 {3,D} {10,D}
8    Cdd U0 {4,D} {11,D}
9    C   U0 {6,D}
10   C   U0 {7,D}
11   C   U0 {8,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cd)(Cds-Cd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S}
4   Cd U0 {1,S}
5   Cb U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cds)(Cds-Cds)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {8,D}
3   Cd U0 {1,S} {6,D}
4   Cd U0 {1,S} {7,D}
5   Cb U0 {1,S}
6   Cd U0 {3,D}
7   Cd U0 {4,D}
8   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd)(Cds-Cds)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Cb  U0 {1,S}
6   Cdd U0 {3,D}
7   Cd  U0 {4,D}
8   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Sd)(Cds-Cds)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {9,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Cb  U0 {1,S}
6   Cdd U0 {3,D} {8,D}
7   Cd  U0 {4,D}
8   Sd  U0 {6,D}
9   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Cd)(Cds-Cds)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {9,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Cb  U0 {1,S}
6   Cdd U0 {3,D} {8,D}
7   Cd  U0 {4,D}
8   C   U0 {6,D}
9   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd)(Cds-Cdd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Cb  U0 {1,S}
6   Cdd U0 {3,D}
7   Cdd U0 {4,D}
8   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Sd)(Cds-Cdd-Sd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {10,D}
3    Cd  U0 {1,S} {6,D}
4    Cd  U0 {1,S} {7,D}
5    Cb  U0 {1,S}
6    Cdd U0 {3,D} {8,D}
7    Cdd U0 {4,D} {9,D}
8    Sd  U0 {6,D}
9    Sd  U0 {7,D}
10   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Sd)(Cds-Cdd-Cd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {10,D}
3    Cd  U0 {1,S} {6,D}
4    Cd  U0 {1,S} {7,D}
5    Cb  U0 {1,S}
6    Cdd U0 {3,D} {8,D}
7    Cdd U0 {4,D} {9,D}
8    Sd  U0 {6,D}
9    C   U0 {7,D}
10   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {10,D}
3    Cd  U0 {1,S} {6,D}
4    Cd  U0 {1,S} {7,D}
5    Cb  U0 {1,S}
6    Cdd U0 {3,D} {8,D}
7    Cdd U0 {4,D} {9,D}
8    C   U0 {6,D}
9    C   U0 {7,D}
10   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=S(Cds-Cd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Cd U0 {1,S}
5   Cb U0 {1,S}
6   Sd U0 {2,D}
7   Sd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=S(Cds-Cds)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {7,D}
3   Cd U0 {1,S} {8,D}
4   Cd U0 {1,S} {6,D}
5   Cb U0 {1,S}
6   Cd U0 {4,D}
7   Sd U0 {2,D}
8   Sd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=S(Cds-Cdd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {7,D}
3   Cd  U0 {1,S} {8,D}
4   Cd  U0 {1,S} {6,D}
5   Cb  U0 {1,S}
6   Cdd U0 {4,D}
7   Sd  U0 {2,D}
8   Sd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=S(Cds-Cdd-Sd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {9,D}
4   Cd  U0 {1,S} {6,D}
5   Cb  U0 {1,S}
6   Cdd U0 {4,D} {7,D}
7   Sd  U0 {6,D}
8   Sd  U0 {2,D}
9   Sd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=S(Cds-Cdd-Cd)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {9,D}
4   Cd  U0 {1,S} {6,D}
5   Cb  U0 {1,S}
6   Cdd U0 {4,D} {7,D}
7   C   U0 {6,D}
8   Sd  U0 {2,D}
9   Sd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=SC=SCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Cd U0 {1,S} {8,D}
5   Cb U0 {1,S}
6   Sd U0 {2,D}
7   Sd U0 {3,D}
8   Sd U0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 760,
    label        = "Cs-CtCtCdsCds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   Ct      U0 {1,S}
3   Ct      U0 {1,S}
4   {Cd,CO} U0 {1,S}
5   {Cd,CO} U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 761,
    label        = "Cs-(Cds-Od)(Cds-Od)CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   CO U0 {1,S}
4   Ct U0 {1,S}
5   Ct U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 762,
    label        = "Cs-(Cds-Od)(Cds-Cd)CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cd U0 {1,S}
4   Ct U0 {1,S}
5   Ct U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)CtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 763,
    label        = "Cs-(Cds-Od)(Cds-Cds)CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cd U0 {1,S} {6,D}
4   Ct U0 {1,S}
5   Ct U0 {1,S}
6   Cd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 764,
    label        = "Cs-(Cds-Od)(Cds-Cdd)CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Ct  U0 {1,S}
5   Ct  U0 {1,S}
6   Cdd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cdd-Cd)CtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 765,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Od)CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Ct  U0 {1,S}
5   Ct  U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 766,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Cd)CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Ct  U0 {1,S}
5   Ct  U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)CtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 767,
    label        = "Cs-(Cds-Cd)(Cds-Cd)CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cd U0 {1,S}
4   Ct U0 {1,S}
5   Ct U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 768,
    label        = "Cs-(Cds-Cds)(Cds-Cds)CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Ct U0 {1,S}
5   Ct U0 {1,S}
6   Cd U0 {2,D}
7   Cd U0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.61,7.3,8.97,9.69,9.84,9.42,7.36],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (5.48,'kcal/mol','+|-',0.26),
        S298 = (-34.5,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = u"""Cs-CtCtCdCd BOZZELLI =3D Cs/Cs/Cd/Ct2 + (Cs/Cs3/Cd - Cs/Cs4)""",
    longDesc = 
u"""

""",
)

entry(
    index        = 769,
    label        = "Cs-(Cds-Cdd)(Cds-Cds)CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ct  U0 {1,S}
5   Ct  U0 {1,S}
6   Cdd U0 {2,D}
7   Cd  U0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cds)CtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 770,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cds)CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ct  U0 {1,S}
5   Ct  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cds)CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ct  U0 {1,S}
5   Ct  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 771,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ct  U0 {1,S}
5   Ct  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 772,
    label        = "Cs-(Cds-Cdd)(Cds-Cdd)CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ct  U0 {1,S}
5   Ct  U0 {1,S}
6   Cdd U0 {2,D}
7   Cdd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 773,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ct  U0 {1,S}
5   Ct  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Od  U0 {6,D}
9   Od  U0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 774,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ct  U0 {1,S}
5   Ct  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Od  U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)(Cds-Cds)CtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ct  U0 {1,S}
5   Ct  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Sd  U0 {6,D}
9   Sd  U0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Cd)CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ct  U0 {1,S}
5   Ct  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Sd  U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 775,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ct  U0 {1,S}
5   Ct  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   C   U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cd)CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S}
4   Ct U0 {1,S}
5   Ct U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cds)CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {7,D}
3   Cd U0 {1,S} {6,D}
4   Ct U0 {1,S}
5   Ct U0 {1,S}
6   Cd U0 {3,D}
7   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd)CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {7,D}
3   Cd  U0 {1,S} {6,D}
4   Ct  U0 {1,S}
5   Ct  U0 {1,S}
6   Cdd U0 {3,D}
7   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Sd)CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {6,D}
4   Ct  U0 {1,S}
5   Ct  U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   Sd  U0 {6,D}
8   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Cd)CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {6,D}
4   Ct  U0 {1,S}
5   Ct  U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
8   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=SCtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Ct U0 {1,S}
5   Ct U0 {1,S}
6   Sd U0 {2,D}
7   Sd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 776,
    label        = "Cs-CbCtCdsCds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   Cb      U0 {1,S}
3   Ct      U0 {1,S}
4   {Cd,CO} U0 {1,S}
5   {Cd,CO} U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CbCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 777,
    label        = "Cs-(Cds-Od)(Cds-Od)CbCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   CO U0 {1,S}
4   Cb U0 {1,S}
5   Ct U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 778,
    label        = "Cs-(Cds-Od)(Cds-Cd)CbCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cd U0 {1,S}
4   Cb U0 {1,S}
5   Ct U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)CbCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 779,
    label        = "Cs-(Cds-Od)(Cds-Cds)CbCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cd U0 {1,S} {6,D}
4   Cb U0 {1,S}
5   Ct U0 {1,S}
6   Cd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 780,
    label        = "Cs-(Cds-Od)(Cds-Cdd)CbCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cb  U0 {1,S}
5   Ct  U0 {1,S}
6   Cdd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cdd-Cd)CbCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 781,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Od)CbCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cb  U0 {1,S}
5   Ct  U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 782,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Cd)CbCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cb  U0 {1,S}
5   Ct  U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)CbCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 783,
    label        = "Cs-(Cds-Cd)(Cds-Cd)CbCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cd U0 {1,S}
4   Cb U0 {1,S}
5   Ct U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CbCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 784,
    label        = "Cs-(Cds-Cds)(Cds-Cds)CbCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Cb U0 {1,S}
5   Ct U0 {1,S}
6   Cd U0 {2,D}
7   Cd U0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.61,7.3,8.97,9.69,9.84,9.42,7.36],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (5.48,'kcal/mol','+|-',0.26),
        S298 = (-34.5,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = u"""Cs-CbCtCdCd BOZZELLI =3D Cs/Cs/Cb/Cd2 + (Cs/Cs3/Ct - Cs/Cs4)""",
    longDesc = 
u"""

""",
)

entry(
    index        = 785,
    label        = "Cs-(Cds-Cdd)(Cds-Cds)CbCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   Ct  U0 {1,S}
6   Cdd U0 {2,D}
7   Cd  U0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cds)CbCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 786,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cds)CbCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   Ct  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cds)CbCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   Ct  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 787,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CbCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   Ct  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CbCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 788,
    label        = "Cs-(Cds-Cdd)(Cds-Cdd)CbCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   Ct  U0 {1,S}
6   Cdd U0 {2,D}
7   Cdd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 789,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CbCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   Ct  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Od  U0 {6,D}
9   Od  U0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 790,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)CbCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   Ct  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Od  U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)(Cds-Cds)CbCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)CbCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   Ct  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Sd  U0 {6,D}
9   Sd  U0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Cd)CbCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   Ct  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Sd  U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 791,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   Ct  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   C   U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CbCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cd)CbCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S}
4   Cb U0 {1,S}
5   Ct U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cds)CbCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {7,D}
3   Cd U0 {1,S} {6,D}
4   Cb U0 {1,S}
5   Ct U0 {1,S}
6   Cd U0 {3,D}
7   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd)CbCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {7,D}
3   Cd  U0 {1,S} {6,D}
4   Cb  U0 {1,S}
5   Ct  U0 {1,S}
6   Cdd U0 {3,D}
7   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Sd)CbCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {6,D}
4   Cb  U0 {1,S}
5   Ct  U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   Sd  U0 {6,D}
8   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Cd)CbCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {6,D}
4   Cb  U0 {1,S}
5   Ct  U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
8   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=SCbCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Cb U0 {1,S}
5   Ct U0 {1,S}
6   Sd U0 {2,D}
7   Sd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 792,
    label        = "Cs-CbCbCdsCds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   Cb      U0 {1,S}
3   Cb      U0 {1,S}
4   {Cd,CO} U0 {1,S}
5   {Cd,CO} U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CbCb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 793,
    label        = "Cs-(Cds-Od)(Cds-Od)CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   CO U0 {1,S}
4   Cb U0 {1,S}
5   Cb U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 794,
    label        = "Cs-(Cds-Od)(Cds-Cd)CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cd U0 {1,S}
4   Cb U0 {1,S}
5   Cb U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)CbCb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 795,
    label        = "Cs-(Cds-Od)(Cds-Cds)CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cd U0 {1,S} {6,D}
4   Cb U0 {1,S}
5   Cb U0 {1,S}
6   Cd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 796,
    label        = "Cs-(Cds-Od)(Cds-Cdd)CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cb  U0 {1,S}
5   Cb  U0 {1,S}
6   Cdd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cdd-Cd)CbCb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 797,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Od)CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cb  U0 {1,S}
5   Cb  U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 798,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Cd)CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cb  U0 {1,S}
5   Cb  U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)CbCb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 799,
    label        = "Cs-(Cds-Cd)(Cds-Cd)CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cd U0 {1,S}
4   Cb U0 {1,S}
5   Cb U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CbCb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 800,
    label        = "Cs-(Cds-Cds)(Cds-Cds)CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Cb U0 {1,S}
5   Cb U0 {1,S}
6   Cd U0 {2,D}
7   Cd U0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.61,7.3,8.97,9.69,9.84,9.42,7.36],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]),
        H298 = (5.48,'kcal/mol','+|-',0.26),
        S298 = (-34.5,'cal/(mol*K)','+|-',0.13),
    ),
    shortDesc = u"""Cs-CbCbCdCd BOZZELLI =3D Cs/Cs/Cb2/Cd + (Cs/Cs3/Cd - Cs/Cs4)""",
    longDesc = 
u"""

""",
)

entry(
    index        = 801,
    label        = "Cs-(Cds-Cdd)(Cds-Cds)CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   Cb  U0 {1,S}
6   Cdd U0 {2,D}
7   Cd  U0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cds)CbCb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 802,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cds)CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   Cb  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cds)CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   Cb  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 803,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   Cb  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CbCb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 804,
    label        = "Cs-(Cds-Cdd)(Cds-Cdd)CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   Cb  U0 {1,S}
6   Cdd U0 {2,D}
7   Cdd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbCb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 805,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   Cb  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Od  U0 {6,D}
9   Od  U0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 806,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   Cb  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Od  U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)(Cds-Cds)CbCb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   Cb  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Sd  U0 {6,D}
9   Sd  U0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Cd)CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   Cb  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Sd  U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 807,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   Cb  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   C   U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CbCb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cd)CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S}
4   Cb U0 {1,S}
5   Cb U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cds)CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {7,D}
3   Cd U0 {1,S} {6,D}
4   Cb U0 {1,S}
5   Cb U0 {1,S}
6   Cd U0 {3,D}
7   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd)CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {7,D}
3   Cd  U0 {1,S} {6,D}
4   Cb  U0 {1,S}
5   Cb  U0 {1,S}
6   Cdd U0 {3,D}
7   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Sd)CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {6,D}
4   Cb  U0 {1,S}
5   Cb  U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   Sd  U0 {6,D}
8   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Cd)CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {6,D}
4   Cb  U0 {1,S}
5   Cb  U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
8   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=SCbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Cb U0 {1,S}
5   Cb U0 {1,S}
6   Sd U0 {2,D}
7   Sd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 808,
    label        = "Cs-CtCtCtCds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   Ct      U0 {1,S}
3   Ct      U0 {1,S}
4   Ct      U0 {1,S}
5   {Cd,CO} U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CtCtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 809,
    label        = "Cs-(Cds-Od)CtCtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Ct U0 {1,S}
4   Ct U0 {1,S}
5   Ct U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cd)CtCtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Ct U0 {1,S}
4   Ct U0 {1,S}
5   Ct U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 810,
    label        = "Cs-(Cds-Cds)CtCtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Ct U0 {1,S}
4   Ct U0 {1,S}
5   Ct U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 811,
    label        = "Cs-(Cds-Cdd)CtCtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ct  U0 {1,S}
4   Ct  U0 {1,S}
5   Ct  U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CtCtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 812,
    label        = "Cs-(Cds-Cdd-Od)CtCtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ct  U0 {1,S}
4   Ct  U0 {1,S}
5   Ct  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)CtCtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ct  U0 {1,S}
4   Ct  U0 {1,S}
5   Ct  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 813,
    label        = "Cs-(Cds-Cdd-Cd)CtCtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ct  U0 {1,S}
4   Ct  U0 {1,S}
5   Ct  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)CtCtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SCtCtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Ct U0 {1,S}
4   Ct U0 {1,S}
5   Ct U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 814,
    label        = "Cs-CbCtCtCds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   Cb      U0 {1,S}
3   Ct      U0 {1,S}
4   Ct      U0 {1,S}
5   {Cd,CO} U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CbCtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 815,
    label        = "Cs-(Cds-Od)CbCtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cb U0 {1,S}
4   Ct U0 {1,S}
5   Ct U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)CtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 816,
    label        = "Cs-(Cds-Cd)CbCtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cb U0 {1,S}
4   Ct U0 {1,S}
5   Ct U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CbCtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 817,
    label        = "Cs-(Cds-Cds)CbCtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cb U0 {1,S}
4   Ct U0 {1,S}
5   Ct U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 818,
    label        = "Cs-(Cds-Cdd)CbCtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Ct  U0 {1,S}
5   Ct  U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CbCtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 819,
    label        = "Cs-(Cds-Cdd-Od)CbCtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Ct  U0 {1,S}
5   Ct  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)(Cds-Cds)CtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)CbCtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Ct  U0 {1,S}
5   Ct  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 820,
    label        = "Cs-(Cds-Cdd-Cd)CbCtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Ct  U0 {1,S}
5   Ct  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)CbCtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SCbCtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cb U0 {1,S}
4   Ct U0 {1,S}
5   Ct U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 821,
    label        = "Cs-CbCbCtCds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   Cb      U0 {1,S}
3   Cb      U0 {1,S}
4   Ct      U0 {1,S}
5   {Cd,CO} U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CbCbCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 822,
    label        = "Cs-(Cds-Od)CbCbCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cb U0 {1,S}
4   Cb U0 {1,S}
5   Ct U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 823,
    label        = "Cs-(Cds-Cd)CbCbCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cb U0 {1,S}
4   Cb U0 {1,S}
5   Ct U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CbCbCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 824,
    label        = "Cs-(Cds-Cds)CbCbCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cb U0 {1,S}
4   Cb U0 {1,S}
5   Ct U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 825,
    label        = "Cs-(Cds-Cdd)CbCbCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Cb  U0 {1,S}
5   Ct  U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CbCbCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 826,
    label        = "Cs-(Cds-Cdd-Od)CbCbCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Cb  U0 {1,S}
5   Ct  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)CbCbCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Cb  U0 {1,S}
5   Ct  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 827,
    label        = "Cs-(Cds-Cdd-Cd)CbCbCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Cb  U0 {1,S}
5   Ct  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)CbCbCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SCbCbCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cb U0 {1,S}
4   Cb U0 {1,S}
5   Ct U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 828,
    label        = "Cs-CbCbCbCds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   Cb      U0 {1,S}
3   Cb      U0 {1,S}
4   Cb      U0 {1,S}
5   {Cd,CO} U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CbCbCb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 829,
    label        = "Cs-(Cds-Od)CbCbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cb U0 {1,S}
4   Cb U0 {1,S}
5   Cb U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 830,
    label        = "Cs-(Cds-Cd)CbCbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cb U0 {1,S}
4   Cb U0 {1,S}
5   Cb U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CbCbCb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 831,
    label        = "Cs-(Cds-Cds)CbCbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cb U0 {1,S}
4   Cb U0 {1,S}
5   Cb U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 832,
    label        = "Cs-(Cds-Cdd)CbCbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Cb  U0 {1,S}
5   Cb  U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CbCbCb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 833,
    label        = "Cs-(Cds-Cdd-Od)CbCbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Cb  U0 {1,S}
5   Cb  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)CbCbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Cb  U0 {1,S}
5   Cb  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 834,
    label        = "Cs-(Cds-Cdd-Cd)CbCbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Cb  U0 {1,S}
5   Cb  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)CbCbCb',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SCbCbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cb U0 {1,S}
4   Cb U0 {1,S}
5   Cb U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 835,
    label        = "Cs-CtCtCtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Ct U0 {1,S}
3   Ct U0 {1,S}
4   Ct U0 {1,S}
5   Ct U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 836,
    label        = "Cs-CbCtCtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Ct U0 {1,S}
4   Ct U0 {1,S}
5   Ct U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CtCtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 837,
    label        = "Cs-CbCbCtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Cb U0 {1,S}
4   Ct U0 {1,S}
5   Ct U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CtCt',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 838,
    label        = "Cs-CbCbCbCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Cb U0 {1,S}
4   Cb U0 {1,S}
5   Ct U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Ct',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 839,
    label        = "Cs-CbCbCbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Cb U0 {1,S}
4   Cb U0 {1,S}
5   Cb U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cds)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 840,
    label        = "Cs-CCCOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   C  U0 {1,S}
3   C  U0 {1,S}
4   C  U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-CsCsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 841,
    label        = "Cs-CsCsCsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cs U0 {1,S}
3   Cs U0 {1,S}
4   Cs U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.33,6.19,7.25,7.7,8.2,8.24,8.24],'cal/(mol*K)','+|-',[0.2,0.2,0.2,0.2,0.2,0.2,0.2]),
        H298 = (-6.6,'kcal/mol','+|-',0.4),
        S298 = (-33.56,'cal/(mol*K)','+|-',0.2),
    ),
    shortDesc = u"""Cs-OCsCsCs BENSON !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index        = 842,
    label        = "Cs-CdsCsCsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   {Cd,CO} U0 {1,S}
3   Cs      U0 {1,S}
4   Cs      U0 {1,S}
5   Os      U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 843,
    label        = "Cs-(Cds-Od)CsCsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cs U0 {1,S}
4   Cs U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.99,6.04,7.43,8.26,8.92,8.96,8.23],'cal/(mol*K)','+|-',[0.2,0.2,0.2,0.2,0.2,0.2,0.2]),
        H298 = (-3.6,'kcal/mol','+|-',0.4),
        S298 = (-34.72,'cal/(mol*K)','+|-',0.2),
    ),
    shortDesc = u"""Cs-OCOCsCs Hf BENSON S,Cp =3D C/Cd/C3""",
    longDesc = 
u"""

""",
)

entry(
    index        = 844,
    label        = "Cs-(Cds-Cd)CsCsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cs U0 {1,S}
4   Cs U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 845,
    label        = "Cs-(Cds-Cds)CsCsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cs U0 {1,S}
4   Cs U0 {1,S}
5   Os U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.63,6.79,7.95,8.4,8.8,8.44,8.44],'cal/(mol*K)','+|-',[0.2,0.2,0.2,0.2,0.2,0.2,0.2]),
        H298 = (-6.6,'kcal/mol','+|-',0.4),
        S298 = (-32.56,'cal/(mol*K)','+|-',0.2),
    ),
    shortDesc = u"""Cs-OCdCsCs BOZZELLI C/C3/O - (C/C3/H - C/Cb/C2/H), Hf-1 !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index        = 846,
    label        = "Cs-(Cds-Cdd)CsCsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cs  U0 {1,S}
4   Cs  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 847,
    label        = "Cs-(Cds-Cdd-Od)CsCsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cs  U0 {1,S}
4   Cs  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.39,9.66,10.03,10.07,9.64,9.26,8.74],'cal/(mol*K)','+|-',[0.2,0.2,0.2,0.2,0.2,0.2,0.2]),
        H298 = (-9.725,'kcal/mol','+|-',0.4),
        S298 = (-36.5,'cal/(mol*K)','+|-',0.2),
    ),
    shortDesc = u"""{C/CCO/O/C2} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""

""",
)

entry(
    index        = 848,
    label        = "Cs-(Cds-Cdd-Cd)CsCsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cs  U0 {1,S}
4   Cs  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)CsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 849,
    label        = "Cs-OsCtCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Os U0 {1,S}
3   Ct U0 {1,S}
4   Cs U0 {1,S}
5   Cs U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 850,
    label        = "Cs-CbCsCsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Cs U0 {1,S}
4   Cs U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.63,6.79,7.95,8.4,8.8,8.44,8.44],'cal/(mol*K)','+|-',[0.2,0.2,0.2,0.2,0.2,0.2,0.2]),
        H298 = (-6.6,'kcal/mol','+|-',0.4),
        S298 = (-32.56,'cal/(mol*K)','+|-',0.2),
    ),
    shortDesc = u"""Cs-OCbCsCs BOZZELLI C/C3/O - (C/C3/H - C/Cb/C2/H), Hf-1 !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index        = 851,
    label        = "Cs-CdsCdsCsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   {Cd,CO} U0 {1,S}
3   {Cd,CO} U0 {1,S}
4   Cs      U0 {1,S}
5   Os      U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 852,
    label        = "Cs-(Cds-Od)(Cds-Od)CsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   CO U0 {1,S}
4   Cs U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-CsCsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 853,
    label        = "Cs-(Cds-Od)(Cds-Cd)CsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cd U0 {1,S}
4   Cs U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 854,
    label        = "Cs-(Cds-Od)(Cds-Cds)CsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cd U0 {1,S} {6,D}
4   Cs U0 {1,S}
5   Os U0 {1,S}
6   Cd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Od)CsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 855,
    label        = "Cs-(Cds-Od)(Cds-Cdd)CsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cs  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cdd-Cd)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 856,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Od)CsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cs  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)CsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 857,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Cd)CsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cs  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 858,
    label        = "Cs-(Cds-Cd)(Cds-Cd)CsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cd U0 {1,S}
4   Cs U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 859,
    label        = "Cs-(Cds-Cds)(Cds-Cds)CsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Cs U0 {1,S}
5   Os U0 {1,S}
6   Cd U0 {2,D}
7   Cd U0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.61,5.98,7.51,8.37,9,9.02,8.34],'cal/(mol*K)','+|-',[0.2,0.2,0.2,0.2,0.2,0.2,0.2]),
        H298 = (-8.01,'kcal/mol','+|-',0.4),
        S298 = (-34.34,'cal/(mol*K)','+|-',0.2),
    ),
    shortDesc = u"""Cs-OCdCdCs Hf jwb 697 S,Cp from C/Cd2/C2""",
    longDesc = 
u"""

""",
)

entry(
    index        = 860,
    label        = "Cs-(Cds-Cdd)(Cds-Cds)CsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cs  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D}
7   Cd  U0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 861,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cds)CsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cs  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)CsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 862,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cs  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 863,
    label        = "Cs-(Cds-Cdd)(Cds-Cdd)CsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cs  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D}
7   Cdd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 864,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cs  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Od  U0 {6,D}
9   Od  U0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 865,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)CsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cs  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Od  U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 866,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cs  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   C   U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 867,
    label        = "Cs-CtCdsCsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   Ct      U0 {1,S}
3   {Cd,CO} U0 {1,S}
4   Cs      U0 {1,S}
5   Os      U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CtCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 868,
    label        = "Cs-(Cds-Od)CtCsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Ct U0 {1,S}
4   Cs U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 869,
    label        = "Cs-(Cds-Cd)CtCsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Ct U0 {1,S}
4   Cs U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CtCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 870,
    label        = "Cs-(Cds-Cds)CtCsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Ct U0 {1,S}
4   Cs U0 {1,S}
5   Os U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 871,
    label        = "Cs-(Cds-Cdd)CtCsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ct  U0 {1,S}
4   Cs  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CtCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 872,
    label        = "Cs-(Cds-Cdd-Od)CtCsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ct  U0 {1,S}
4   Cs  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 873,
    label        = "Cs-(Cds-Cdd-Cd)CtCsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ct  U0 {1,S}
4   Cs  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)CtCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 874,
    label        = "Cs-CbCdsCsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   Cb      U0 {1,S}
3   {Cd,CO} U0 {1,S}
4   Cs      U0 {1,S}
5   Os      U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CbCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 875,
    label        = "Cs-(Cds-Od)CbCsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cb U0 {1,S}
4   Cs U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 876,
    label        = "Cs-(Cds-Cd)CbCsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cb U0 {1,S}
4   Cs U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CbCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 877,
    label        = "Cs-(Cds-Cds)CbCsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cb U0 {1,S}
4   Cs U0 {1,S}
5   Os U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 878,
    label        = "Cs-(Cds-Cdd)CbCsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Cs  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CbCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 879,
    label        = "Cs-(Cds-Cdd-Od)CbCsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Cs  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 880,
    label        = "Cs-(Cds-Cdd-Cd)CbCsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Cs  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)CbCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 881,
    label        = "Cs-CtCtCsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Ct U0 {1,S}
3   Ct U0 {1,S}
4   Cs U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 882,
    label        = "Cs-CbCtCsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Ct U0 {1,S}
4   Cs U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CtCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 883,
    label        = "Cs-CbCbCsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Cb U0 {1,S}
4   Cs U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 884,
    label        = "Cs-CdsCdsCdsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   {Cd,CO} U0 {1,S}
3   {Cd,CO} U0 {1,S}
4   {Cd,CO} U0 {1,S}
5   Os      U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 885,
    label        = "Cs-(Cds-Od)(Cds-Od)(Cds-Od)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   CO U0 {1,S}
4   CO U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-CsCsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 886,
    label        = "Cs-(Cds-Od)(Cds-Od)(Cds-Cd)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   CO U0 {1,S}
4   Cd U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 887,
    label        = "Cs-(Cds-Od)(Cds-Od)(Cds-Cds)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   CO U0 {1,S}
4   Cd U0 {1,S} {6,D}
5   Os U0 {1,S}
6   Cd U0 {4,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Od)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 888,
    label        = "Cs-(Cds-Od)(Cds-Od)(Cds-Cdd)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   CO  U0 {1,S}
4   Cd  U0 {1,S} {6,D}
5   Os  U0 {1,S}
6   Cdd U0 {4,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Cd)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 889,
    label        = "Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Od)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   CO  U0 {1,S}
4   Cd  U0 {1,S} {6,D}
5   Os  U0 {1,S}
6   Cdd U0 {4,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)CsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 890,
    label        = "Cs-(Cds-Od)(Cds-Od)(Cds-Cdd-Cd)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   CO  U0 {1,S}
4   Cd  U0 {1,S} {6,D}
5   Os  U0 {1,S}
6   Cdd U0 {4,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 891,
    label        = "Cs-(Cds-Od)(Cds-Cd)(Cds-Cd)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cd U0 {1,S}
4   Cd U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 892,
    label        = "Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cd U0 {1,S} {6,D}
4   Cd U0 {1,S} {7,D}
5   Os U0 {1,S}
6   Cd U0 {3,D}
7   Cd U0 {4,D}
""",
    thermo = u'Cs-(Cds-Od)CsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 893,
    label        = "Cs-(Cds-Od)(Cds-Cdd)(Cds-Cds)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Os  U0 {1,S}
6   Cdd U0 {3,D}
7   Cd  U0 {4,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 894,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Os  U0 {1,S}
6   Cdd U0 {3,D} {8,D}
7   Cd  U0 {4,D}
8   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cdd-Od)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 895,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cds)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Os  U0 {1,S}
6   Cdd U0 {3,D} {8,D}
7   Cd  U0 {4,D}
8   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 896,
    label        = "Cs-(Cds-Od)(Cds-Cdd)(Cds-Cdd)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Os  U0 {1,S}
6   Cdd U0 {3,D}
7   Cdd U0 {4,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 897,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Os  U0 {1,S}
6   Cdd U0 {3,D} {8,D}
7   Cdd U0 {4,D} {9,D}
8   Od  U0 {6,D}
9   Od  U0 {7,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 898,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Os  U0 {1,S}
6   Cdd U0 {3,D} {8,D}
7   Cdd U0 {4,D} {9,D}
8   Od  U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 899,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Os  U0 {1,S}
6   Cdd U0 {3,D} {8,D}
7   Cdd U0 {4,D} {9,D}
8   C   U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 900,
    label        = "Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cd U0 {1,S}
4   Cd U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 901,
    label        = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Cd U0 {1,S} {8,D}
5   Os U0 {1,S}
6   Cd U0 {2,D}
7   Cd U0 {3,D}
8   Cd U0 {4,D}
""",
    thermo = u'Cs-CsCsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 902,
    label        = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cd  U0 {1,S} {8,D}
5   Os  U0 {1,S}
6   Cd  U0 {2,D}
7   Cd  U0 {3,D}
8   Cdd U0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 903,
    label        = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cd  U0 {1,S} {8,D}
5   Os  U0 {1,S}
6   Cd  U0 {2,D}
7   Cd  U0 {3,D}
8   Cdd U0 {4,D} {9,D}
9   Od  U0 {8,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)CsCsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 904,
    label        = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cd  U0 {1,S} {8,D}
5   Os  U0 {1,S}
6   Cd  U0 {2,D}
7   Cd  U0 {3,D}
8   Cdd U0 {4,D} {9,D}
9   C   U0 {8,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 905,
    label        = "Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cd  U0 {1,S} {8,D}
5   Os  U0 {1,S}
6   Cd  U0 {2,D}
7   Cdd U0 {3,D}
8   Cdd U0 {4,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 906,
    label        = "Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Os  U0 {1,S}
6    Cd  U0 {2,D}
7    Cdd U0 {3,D} {9,D}
8    Cdd U0 {4,D} {10,D}
9    Od  U0 {7,D}
10   Od  U0 {8,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 907,
    label        = "Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Cd)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Os  U0 {1,S}
6    Cd  U0 {2,D}
7    Cdd U0 {3,D} {9,D}
8    Cdd U0 {4,D} {10,D}
9    Od  U0 {7,D}
10   C   U0 {8,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 908,
    label        = "Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Os  U0 {1,S}
6    Cd  U0 {2,D}
7    Cdd U0 {3,D} {9,D}
8    Cdd U0 {4,D} {10,D}
9    C   U0 {7,D}
10   C   U0 {8,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 909,
    label        = "Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cd  U0 {1,S} {8,D}
5   Os  U0 {1,S}
6   Cdd U0 {2,D}
7   Cdd U0 {3,D}
8   Cdd U0 {4,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 910,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Os  U0 {1,S}
6    Cdd U0 {2,D} {9,D}
7    Cdd U0 {3,D} {10,D}
8    Cdd U0 {4,D} {11,D}
9    Od  U0 {6,D}
10   Od  U0 {7,D}
11   Od  U0 {8,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 911,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Os  U0 {1,S}
6    Cdd U0 {2,D} {9,D}
7    Cdd U0 {3,D} {10,D}
8    Cdd U0 {4,D} {11,D}
9    Od  U0 {6,D}
10   Od  U0 {7,D}
11   C   U0 {8,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 912,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Os  U0 {1,S}
6    Cdd U0 {2,D} {9,D}
7    Cdd U0 {3,D} {10,D}
8    Cdd U0 {4,D} {11,D}
9    Od  U0 {6,D}
10   C   U0 {7,D}
11   C   U0 {8,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 913,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Os  U0 {1,S}
6    Cdd U0 {2,D} {9,D}
7    Cdd U0 {3,D} {10,D}
8    Cdd U0 {4,D} {11,D}
9    C   U0 {6,D}
10   C   U0 {7,D}
11   C   U0 {8,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 914,
    label        = "Cs-CtCdsCdsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   Ct      U0 {1,S}
3   {Cd,CO} U0 {1,S}
4   {Cd,CO} U0 {1,S}
5   Os      U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 915,
    label        = "Cs-(Cds-Od)(Cds-Od)CtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   CO U0 {1,S}
4   Ct U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 916,
    label        = "Cs-(Cds-Od)(Cds-Cd)CtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cd U0 {1,S}
4   Ct U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)CtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 917,
    label        = "Cs-(Cds-Od)(Cds-Cds)CtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cd U0 {1,S} {6,D}
4   Ct U0 {1,S}
5   Os U0 {1,S}
6   Cd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 918,
    label        = "Cs-(Cds-Od)(Cds-Cdd)CtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Ct  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cdd-Cd)CtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 919,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Od)CtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Ct  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 920,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Cd)CtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Ct  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)CtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 921,
    label        = "Cs-(Cds-Cd)(Cds-Cd)CtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cd U0 {1,S}
4   Ct U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 922,
    label        = "Cs-(Cds-Cds)(Cds-Cds)CtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Ct U0 {1,S}
5   Os U0 {1,S}
6   Cd U0 {2,D}
7   Cd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 923,
    label        = "Cs-(Cds-Cdd)(Cds-Cds)CtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ct  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D}
7   Cd  U0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cds)CtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 924,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cds)CtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ct  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 925,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ct  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 926,
    label        = "Cs-(Cds-Cdd)(Cds-Cdd)CtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ct  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D}
7   Cdd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 927,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ct  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Od  U0 {6,D}
9   Od  U0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 928,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)CtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ct  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Od  U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)(Cds-Cds)CtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 929,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ct  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   C   U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 930,
    label        = "Cs-CbCdsCdsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   Cb      U0 {1,S}
3   {Cd,CO} U0 {1,S}
4   {Cd,CO} U0 {1,S}
5   Os      U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CbOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 931,
    label        = "Cs-(Cds-Od)(Cds-Od)CbOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   CO U0 {1,S}
4   Cb U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Od)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 932,
    label        = "Cs-(Cds-Od)(Cds-Cd)CbOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cd U0 {1,S}
4   Cb U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)CbOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 933,
    label        = "Cs-(Cds-Od)(Cds-Cds)CbOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cd U0 {1,S} {6,D}
4   Cb U0 {1,S}
5   Os U0 {1,S}
6   Cd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 934,
    label        = "Cs-(Cds-Od)(Cds-Cdd)CbOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cb  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cdd-Cd)CbOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 935,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Od)CbOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cb  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cdd-Od)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 936,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Cd)CbOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Cb  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)CbOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 937,
    label        = "Cs-(Cds-Cd)(Cds-Cd)CbOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cd U0 {1,S}
4   Cb U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CbOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 938,
    label        = "Cs-(Cds-Cds)(Cds-Cds)CbOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Cb U0 {1,S}
5   Os U0 {1,S}
6   Cd U0 {2,D}
7   Cd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 939,
    label        = "Cs-(Cds-Cdd)(Cds-Cds)CbOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D}
7   Cd  U0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cds)CbOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 940,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cds)CbOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 941,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CbOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CbOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 942,
    label        = "Cs-(Cds-Cdd)(Cds-Cdd)CbOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D}
7   Cdd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 943,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CbOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Od  U0 {6,D}
9   Od  U0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 944,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)CbOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Od  U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)(Cds-Cds)CbOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 945,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   C   U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CbOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 946,
    label        = "Cs-CtCtCdsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   Ct      U0 {1,S}
3   Ct      U0 {1,S}
4   {Cd,CO} U0 {1,S}
5   Os      U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CtCtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 947,
    label        = "Cs-(Cds-Od)CtCtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Ct U0 {1,S}
4   Ct U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 948,
    label        = "Cs-(Cds-Cd)CtCtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Ct U0 {1,S}
4   Ct U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CtCtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 949,
    label        = "Cs-(Cds-Cds)CtCtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Ct U0 {1,S}
4   Ct U0 {1,S}
5   Os U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 950,
    label        = "Cs-(Cds-Cdd)CtCtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ct  U0 {1,S}
4   Ct  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CtCtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 951,
    label        = "Cs-(Cds-Cdd-Od)CtCtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ct  U0 {1,S}
4   Ct  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 952,
    label        = "Cs-(Cds-Cdd-Cd)CtCtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ct  U0 {1,S}
4   Ct  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)CtCtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 953,
    label        = "Cs-CbCtCdsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   Cb      U0 {1,S}
3   Ct      U0 {1,S}
4   {Cd,CO} U0 {1,S}
5   Os      U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CbCtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 954,
    label        = "Cs-(Cds-Od)CbCtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cb U0 {1,S}
4   Ct U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)CtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 955,
    label        = "Cs-(Cds-Cd)CbCtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cb U0 {1,S}
4   Ct U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CbCtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 956,
    label        = "Cs-(Cds-Cds)CbCtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cb U0 {1,S}
4   Ct U0 {1,S}
5   Os U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 957,
    label        = "Cs-(Cds-Cdd)CbCtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Ct  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CbCtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 958,
    label        = "Cs-(Cds-Cdd-Od)CbCtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Ct  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)(Cds-Cds)CtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 959,
    label        = "Cs-(Cds-Cdd-Cd)CbCtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Ct  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)CbCtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 960,
    label        = "Cs-CbCbCdsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   Cb      U0 {1,S}
3   Cb      U0 {1,S}
4   {Cd,CO} U0 {1,S}
5   Os      U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CbCbOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 961,
    label        = "Cs-(Cds-Od)CbCbOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cb U0 {1,S}
4   Cb U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 962,
    label        = "Cs-(Cds-Cd)CbCbOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cb U0 {1,S}
4   Cb U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CbCbOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 963,
    label        = "Cs-(Cds-Cds)CbCbOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cb U0 {1,S}
4   Cb U0 {1,S}
5   Os U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 964,
    label        = "Cs-(Cds-Cdd)CbCbOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Cb  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CbCbOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 965,
    label        = "Cs-(Cds-Cdd-Od)CbCbOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Cb  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 966,
    label        = "Cs-(Cds-Cdd-Cd)CbCbOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Cb  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)CbCbOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 967,
    label        = "Cs-CtCtCtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Ct U0 {1,S}
3   Ct U0 {1,S}
4   Ct U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 968,
    label        = "Cs-CbCtCtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Ct U0 {1,S}
4   Ct U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CtCtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 969,
    label        = "Cs-CbCbCtOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Cb U0 {1,S}
4   Ct U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)CtOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 970,
    label        = "Cs-CbCbCbOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Cb U0 {1,S}
4   Cb U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Os',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 971,
    label        = "Cs-CCOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   C  U0 {1,S}
3   C  U0 {1,S}
4   Os U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-CsCsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 972,
    label        = "Cs-CsCsOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cs U0 {1,S}
3   Cs U0 {1,S}
4   Os U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.8,6.09,7.3,7.78,8.24,8.24,8.24],'cal/(mol*K)','+|-',[0.2,0.2,0.2,0.2,0.2,0.2,0.2]),
        H298 = (-9.77,'kcal/mol','+|-',0.4),
        S298 = (-33.18,'cal/(mol*K)','+|-',0.2),
    ),
    shortDesc = u"""Cs-OOCsCs BOZZELLI =3D C/C3/O - (C/C2/H2 - C/C/H2/O) !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index        = 973,
    label        = "Cs-CdsCsOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   {Cd,CO} U0 {1,S}
3   Cs      U0 {1,S}
4   Os      U0 {1,S}
5   Os      U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 974,
    label        = "Cs-(Cds-Od)CsOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cs U0 {1,S}
4   Os U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-CsCsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 975,
    label        = "Cs-(Cds-Cd)CsOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cs U0 {1,S}
4   Os U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 976,
    label        = "Cs-(Cds-Cds)CsOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cs U0 {1,S}
4   Os U0 {1,S}
5   Os U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = u'Cs-CsCsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 977,
    label        = "Cs-(Cds-Cdd)CsOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cs  U0 {1,S}
4   Os  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 978,
    label        = "Cs-(Cds-Cdd-Od)CsOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cs  U0 {1,S}
4   Os  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)CsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 979,
    label        = "Cs-(Cds-Cdd-Cd)CsOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cs  U0 {1,S}
4   Os  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)CsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 980,
    label        = "Cs-CdsCdsOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   {Cd,CO} U0 {1,S}
3   {Cd,CO} U0 {1,S}
4   Os      U0 {1,S}
5   Os      U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 981,
    label        = "Cs-(Cds-Od)(Cds-Od)OsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   CO U0 {1,S}
4   Os U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-CsCsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 982,
    label        = "Cs-(Cds-Od)(Cds-Cd)OsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cd U0 {1,S}
4   Os U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 983,
    label        = "Cs-(Cds-Od)(Cds-Cds)OsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cd U0 {1,S} {6,D}
4   Os U0 {1,S}
5   Os U0 {1,S}
6   Cd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Od)CsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 984,
    label        = "Cs-(Cds-Od)(Cds-Cdd)OsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Os  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cdd-Cd)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 985,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Od)OsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Os  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)CsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 986,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Cd)OsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Os  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 987,
    label        = "Cs-(Cds-Cd)(Cds-Cd)OsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cd U0 {1,S}
4   Os U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 988,
    label        = "Cs-(Cds-Cds)(Cds-Cds)OsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Os U0 {1,S}
5   Os U0 {1,S}
6   Cd U0 {2,D}
7   Cd U0 {3,D}
""",
    thermo = u'Cs-CsCsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 989,
    label        = "Cs-(Cds-Cdd)(Cds-Cds)OsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Os  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D}
7   Cd  U0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 990,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cds)OsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Os  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)CsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 991,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cds)OsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Os  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 992,
    label        = "Cs-(Cds-Cdd)(Cds-Cdd)OsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Os  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D}
7   Cdd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 993,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)OsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Os  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Od  U0 {6,D}
9   Od  U0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 994,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)OsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Os  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Od  U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 995,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)OsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Os  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   C   U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 996,
    label        = "Cs-CtCsOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Ct U0 {1,S}
3   Cs U0 {1,S}
4   Os U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 997,
    label        = "Cs-CtCdsOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   Ct      U0 {1,S}
3   {Cd,CO} U0 {1,S}
4   Os      U0 {1,S}
5   Os      U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CtOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 998,
    label        = "Cs-(Cds-Od)CtOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Ct U0 {1,S}
4   Os U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 999,
    label        = "Cs-(Cds-Cd)CtOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Ct U0 {1,S}
4   Os U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CtOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1000,
    label        = "Cs-(Cds-Cds)CtOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Ct U0 {1,S}
4   Os U0 {1,S}
5   Os U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1001,
    label        = "Cs-(Cds-Cdd)CtOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ct  U0 {1,S}
4   Os  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CtOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1002,
    label        = "Cs-(Cds-Cdd-Od)CtOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ct  U0 {1,S}
4   Os  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1003,
    label        = "Cs-(Cds-Cdd-Cd)CtOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ct  U0 {1,S}
4   Os  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)CtOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1004,
    label        = "Cs-CtCtOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Ct U0 {1,S}
3   Ct U0 {1,S}
4   Os U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1005,
    label        = "Cs-CbCsOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Cs U0 {1,S}
4   Os U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1006,
    label        = "Cs-CbCdsOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   Cb      U0 {1,S}
3   {Cd,CO} U0 {1,S}
4   Os      U0 {1,S}
5   Os      U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CbOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1007,
    label        = "Cs-(Cds-Od)CbOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cb U0 {1,S}
4   Os U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1008,
    label        = "Cs-(Cds-Cd)CbOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cb U0 {1,S}
4   Os U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CbOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1009,
    label        = "Cs-(Cds-Cds)CbOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cb U0 {1,S}
4   Os U0 {1,S}
5   Os U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1010,
    label        = "Cs-(Cds-Cdd)CbOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Os  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CbOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1011,
    label        = "Cs-(Cds-Cdd-Od)CbOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Os  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1012,
    label        = "Cs-(Cds-Cdd-Cd)CbOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Os  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)CbOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1013,
    label        = "Cs-CbCtOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Ct U0 {1,S}
4   Os U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CtOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1014,
    label        = "Cs-CbCbOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Cb U0 {1,S}
4   Os U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)OsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1015,
    label        = "Cs-COsOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   C  U0 {1,S}
3   Os U0 {1,S}
4   Os U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-CsOsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1016,
    label        = "Cs-CsOsOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cs U0 {1,S}
3   Os U0 {1,S}
4   Os U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.33,6.19,7.25,7.7,8.2,8.24,8.24],'cal/(mol*K)','+|-',[0.2,0.2,0.2,0.2,0.2,0.2,0.2]),
        H298 = (-19,'kcal/mol','+|-',0.4),
        S298 = (-33.56,'cal/(mol*K)','+|-',0.2),
    ),
    shortDesc = u"""Cs-OOOCs BOZZELLI est !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1017,
    label        = "Cs-CdsOsOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   {Cd,CO} U0 {1,S}
3   Os      U0 {1,S}
4   Os      U0 {1,S}
5   Os      U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)OsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1018,
    label        = "Cs-(Cds-Od)OsOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Os U0 {1,S}
4   Os U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-CsOsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1019,
    label        = "Cs-(Cds-Cd)OsOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Os U0 {1,S}
4   Os U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)OsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1020,
    label        = "Cs-(Cds-Cds)OsOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Os U0 {1,S}
4   Os U0 {1,S}
5   Os U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = u'Cs-CsOsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1021,
    label        = "Cs-(Cds-Cdd)OsOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Os  U0 {1,S}
4   Os  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)OsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1022,
    label        = "Cs-(Cds-Cdd-Od)OsOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Os  U0 {1,S}
4   Os  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)OsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1023,
    label        = "Cs-(Cds-Cdd-Cd)OsOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Os  U0 {1,S}
4   Os  U0 {1,S}
5   Os  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)OsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1024,
    label        = "Cs-CtOsOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Ct U0 {1,S}
3   Os U0 {1,S}
4   Os U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)OsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1025,
    label        = "Cs-CbOsOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Os U0 {1,S}
4   Os U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)OsOsOs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1026,
    label        = "Cs-OsOsOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Os U0 {1,S}
3   Os U0 {1,S}
4   Os U0 {1,S}
5   Os U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.33,6.13,7.25,7.7,8.2,8.24,8.24],'cal/(mol*K)','+|-',[0.2,0.2,0.2,0.2,0.2,0.2,0.2]),
        H298 = (-23,'kcal/mol','+|-',0.4),
        S298 = (-35.56,'cal/(mol*K)','+|-',0.2),
    ),
    shortDesc = u"""Cs-OOOO BOZZELLI est !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1027,
    label        = "Cs-COsOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   C  U0 {1,S}
3   Os U0 {1,S}
4   Os U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-CsOsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1028,
    label        = "Cs-CsOsOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cs U0 {1,S}
3   Os U0 {1,S}
4   Os U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.25,7.1,8.81,9.55,10.31,11.05,11.05],'cal/(mol*K)','+|-',[0.12,0.12,0.12,0.12,0.12,0.12,0.12]),
        H298 = (-16,'kcal/mol','+|-',0.24),
        S298 = (-12.07,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = u"""Cs-OOCsH BENSON Hf, BOZZELLI C/C3/H - C/C2/O/H !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1029,
    label        = "Cs-CdsOsOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   {Cd,CO} U0 {1,S}
3   Os      U0 {1,S}
4   Os      U0 {1,S}
5   H       U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)OsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1030,
    label        = "Cs-(Cds-Od)OsOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Os U0 {1,S}
4   Os U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-CsOsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1031,
    label        = "Cs-(Cds-Cd)OsOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Os U0 {1,S}
4   Os U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)OsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1032,
    label        = "Cs-(Cds-Cds)OsOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Os U0 {1,S}
4   Os U0 {1,S}
5   H  U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = u'Cs-CsOsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1033,
    label        = "Cs-(Cds-Cdd)OsOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Os  U0 {1,S}
4   Os  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)OsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1034,
    label        = "Cs-(Cds-Cdd-Od)OsOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Os  U0 {1,S}
4   Os  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)OsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1035,
    label        = "Cs-(Cds-Cdd-Cd)OsOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Os  U0 {1,S}
4   Os  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)OsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1036,
    label        = "Cs-CtOsOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Ct U0 {1,S}
3   Os U0 {1,S}
4   Os U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)OsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1037,
    label        = "Cs-CbOsOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Os U0 {1,S}
4   Os U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)OsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-COsSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   C  U0 {1,S}
3   Os U0 {1,S}
4   Ss U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1452,
    label        = "Cs-CsOsSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cs U0 {1,S}
3   Os U0 {1,S}
4   Ss U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.9,10.48,11.12,11.27,11.29,11.31,11.7],'cal/(mol*K)'),
        H298 = (-10.28,'kcal/mol'),
        S298 = (-17.78,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 1DHR calc""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CdsOsSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Os U0 {1,S}
4   Ss U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CtOsSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Ct U0 {1,S}
3   Os U0 {1,S}
4   Ss U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CbOsSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Os U0 {1,S}
4   Ss U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1460,
    label        = "Cs-COsOsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   C  U0 {1,S}
3   Os U0 {1,S}
4   Os U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = u'Cs-CsOsOsSs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1461,
    label        = "Cs-CsOsOsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cs U0 {1,S}
3   Os U0 {1,S}
4   Os U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.79,8.59,9.36,9.54,9.39,9.12,8.83],'cal/(mol*K)'),
        H298 = (-19.49,'kcal/mol'),
        S298 = (-37.31,'cal/(mol*K)'),
    ),
    shortDesc = u"""CAC calc 1D-HR""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1038,
    label        = "Cs-CCOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   C  U0 {1,S}
3   C  U0 {1,S}
4   Os U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-CsCsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1039,
    label        = "Cs-CsCsOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cs U0 {1,S}
3   Cs U0 {1,S}
4   Os U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.8,6.64,8.1,8.73,9.81,10.4,11.51],'cal/(mol*K)','+|-',[0.12,0.12,0.12,0.12,0.12,0.12,0.12]),
        H298 = (-7.2,'kcal/mol','+|-',0.24),
        S298 = (-11,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = u"""Cs-OCsCs BENSON: Cp1500 =3D Cp1000*(Cp1500/Cp1000: C/C2Cd/H)""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1040,
    label        = "Cs-CdsCsOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   {Cd,CO} U0 {1,S}
3   Cs      U0 {1,S}
4   Os      U0 {1,S}
5   H       U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1041,
    label        = "Cs-(Cds-Od)CsOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cs U0 {1,S}
4   Os U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.47,6.82,8.45,9.17,10.24,10.8,11.02],'cal/(mol*K)','+|-',[0.12,0.12,0.12,0.12,0.12,0.12,0.12]),
        H298 = (-6,'kcal/mol','+|-',0.24),
        S298 = (-11.1,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = u"""Cs-OCOCsH BOZZELLI""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1042,
    label        = "Cs-(Cds-Cd)CsOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cs U0 {1,S}
4   Os U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1043,
    label        = "Cs-(Cds-Cds)CsOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cs U0 {1,S}
4   Os U0 {1,S}
5   H  U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.47,6.82,8.45,9.17,10.24,10.8,11.02],'cal/(mol*K)','+|-',[0.12,0.12,0.12,0.12,0.12,0.12,0.12]),
        H298 = (-6,'kcal/mol','+|-',0.24),
        S298 = (-11.1,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = u"""Cs-OCdCsH BOZZELLI""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1044,
    label        = "Cs-(Cds-Cdd)CsOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cs  U0 {1,S}
4   Os  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1045,
    label        = "Cs-(Cds-Cdd-Od)CsOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cs  U0 {1,S}
4   Os  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.2,8.49,9.33,9.92,10.5,10.92,11.71],'cal/(mol*K)','+|-',[0.12,0.12,0.12,0.12,0.12,0.12,0.12]),
        H298 = (-8.37,'kcal/mol','+|-',0.24),
        S298 = (-13.04,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = u"""{C/CCO/O/C/H} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1046,
    label        = "Cs-(Cds-Cdd-Cd)CsOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cs  U0 {1,S}
4   Os  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)CsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1047,
    label        = "Cs-CdsCdsOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   {Cd,CO} U0 {1,S}
3   {Cd,CO} U0 {1,S}
4   Os      U0 {1,S}
5   H       U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1048,
    label        = "Cs-(Cds-Od)(Cds-Od)OsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   CO U0 {1,S}
4   Os U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-CsCsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1049,
    label        = "Cs-(Cds-Od)(Cds-Cd)OsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cd U0 {1,S}
4   Os U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1050,
    label        = "Cs-(Cds-Od)(Cds-Cds)OsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cd U0 {1,S} {6,D}
4   Os U0 {1,S}
5   H  U0 {1,S}
6   Cd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Od)CsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1051,
    label        = "Cs-(Cds-Od)(Cds-Cdd)OsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Os  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cdd-Cd)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1052,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Od)OsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Os  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)CsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1053,
    label        = "Cs-(Cds-Od)(Cds-Cdd-Cd)OsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   CO  U0 {1,S}
3   Cd  U0 {1,S} {6,D}
4   Os  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1054,
    label        = "Cs-(Cds-Cd)(Cds-Cd)OsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cd U0 {1,S}
4   Os U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1055,
    label        = "Cs-(Cds-Cds)(Cds-Cds)OsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Os U0 {1,S}
5   H  U0 {1,S}
6   Cd U0 {2,D}
7   Cd U0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.21,6.6,8.26,9.05,10.23,10.86,11.04],'cal/(mol*K)','+|-',[0.12,0.12,0.12,0.12,0.12,0.12,0.12]),
        H298 = (-6.67,'kcal/mol','+|-',0.24),
        S298 = (-10.42,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = u"""Cs-OCdCdH BOZZELLI""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1056,
    label        = "Cs-(Cds-Cdd)(Cds-Cds)OsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Os  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D}
7   Cd  U0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1057,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cds)OsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Os  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)CsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1058,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cds)OsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Os  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1059,
    label        = "Cs-(Cds-Cdd)(Cds-Cdd)OsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Os  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D}
7   Cdd U0 {3,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1060,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)OsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Os  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Od  U0 {6,D}
9   Od  U0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1061,
    label        = "Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)OsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Os  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Od  U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1062,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)OsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Os  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   C   U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1063,
    label        = "Cs-CtCsOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Ct U0 {1,S}
3   Cs U0 {1,S}
4   Os U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CsOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1064,
    label        = "Cs-CtCdsOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   Ct      U0 {1,S}
3   {Cd,CO} U0 {1,S}
4   Os      U0 {1,S}
5   H       U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CtOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1065,
    label        = "Cs-(Cds-Od)CtOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Ct U0 {1,S}
4   Os U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1066,
    label        = "Cs-(Cds-Cd)CtOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Ct U0 {1,S}
4   Os U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CtOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1067,
    label        = "Cs-(Cds-Cds)CtOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Ct U0 {1,S}
4   Os U0 {1,S}
5   H  U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1068,
    label        = "Cs-(Cds-Cdd)CtOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ct  U0 {1,S}
4   Os  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CtOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1069,
    label        = "Cs-(Cds-Cdd-Od)CtOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ct  U0 {1,S}
4   Os  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1070,
    label        = "Cs-(Cds-Cdd-Cd)CtOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ct  U0 {1,S}
4   Os  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)CtOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1071,
    label        = "Cs-CtCtOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Ct U0 {1,S}
3   Ct U0 {1,S}
4   Os U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1072,
    label        = "Cs-CbCsOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Cs U0 {1,S}
4   Os U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.47,6.82,8.45,9.17,10.24,10.8,11.02],'cal/(mol*K)','+|-',[0.12,0.12,0.12,0.12,0.12,0.12,0.12]),
        H298 = (-6,'kcal/mol','+|-',0.24),
        S298 = (-11.1,'cal/(mol*K)','+|-',0.12),
    ),
    shortDesc = u"""Cs-OCbCsH BOZZELLI =3D C/Cd/C/H/O Jul 91""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1073,
    label        = "Cs-CbCdsOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   Cb      U0 {1,S}
3   {Cd,CO} U0 {1,S}
4   Os      U0 {1,S}
5   H       U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CbOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1074,
    label        = "Cs-(Cds-Od)CbOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Cb U0 {1,S}
4   Os U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-(Cds-Od)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1075,
    label        = "Cs-(Cds-Cd)CbOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cb U0 {1,S}
4   Os U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CbOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1076,
    label        = "Cs-(Cds-Cds)CbOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cb U0 {1,S}
4   Os U0 {1,S}
5   H  U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1077,
    label        = "Cs-(Cds-Cdd)CbOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Os  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)CbOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1078,
    label        = "Cs-(Cds-Cdd-Od)CbOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Os  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cdd-Od)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1079,
    label        = "Cs-(Cds-Cdd-Cd)CbOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Os  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)CbOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1080,
    label        = "Cs-CbCtOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Ct U0 {1,S}
4   Os U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)CtOsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1081,
    label        = "Cs-CbCbOsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Cb U0 {1,S}
4   Os U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)(Cds-Cds)OsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1082,
    label        = "Cs-COsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   C  U0 {1,S}
3   Os U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-CsOsHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1083,
    label        = "Cs-CsOsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cs U0 {1,S}
3   Os U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.99,6.85,8.3,9.43,11.11,12.33,12.33],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-8.1,'kcal/mol','+|-',0.2),
        S298 = (9.8,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cs-OCsHH BENSON !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1084,
    label        = "Cs-CdsOsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs      U0 {2,S} {3,S} {4,S} {5,S}
2   {Cd,CO} U0 {1,S}
3   Os      U0 {1,S}
4   H       U0 {1,S}
5   H       U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)OsHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1085,
    label        = "Cs-(Cds-Od)OsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   CO U0 {1,S}
3   Os U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.95,6.74,8.53,9.8,11.61,12.65,14.4],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-5.28,'kcal/mol','+|-',0.2),
        S298 = (10.17,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cs-OCOHH jwl 99 cdsQ cc*ocq""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1086,
    label        = "Cs-(Cds-Cd)OsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Os U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)OsHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1087,
    label        = "Cs-(Cds-Cds)OsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Os U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.12,6.86,8.32,9.49,11.22,12.48,14.4],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-6.76,'kcal/mol','+|-',0.2),
        S298 = (9.8,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cs-OCdHH BOZZELLI Hf PEDLEY c*ccoh C/C/Cd/H2""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1088,
    label        = "Cs-(Cds-Cdd)OsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Os  U0 {1,S}
4   H   U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = u'Cs-(Cds-Cdd-Cd)OsHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1089,
    label        = "Cs-(Cds-Cdd-Od)OsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Os  U0 {1,S}
4   H   U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Od  U0 {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.15,8.67,9.75,10.65,11.93,12.97,14.86],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-8.68,'kcal/mol','+|-',0.2),
        S298 = (8.43,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""{C/CCO/O/H2} RAMAN & GREEN JPCA 2002, 106, 7937-7949""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1090,
    label        = "Cs-(Cds-Cdd-Cd)OsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Os  U0 {1,S}
4   H   U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = u'Cs-(Cds-Cds)OsHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1091,
    label        = "Cs-CtOsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Ct U0 {1,S}
3   Os U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.12,6.86,8.32,9.49,11.22,12.48,14.4],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-6.76,'kcal/mol','+|-',0.2),
        S298 = (9.8,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Cs-OCtHH BOZZELLI assigned C/Cd/H2/O""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1092,
    label        = "Cs-CbOsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Os U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = u'Cs-(Cds-Cds)OsHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CCCSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   C  U0 {1,S}
3   C  U0 {1,S}
4   C  U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1175,
    label        = "Cs-CsCsCsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cs U0 {1,S}
3   Cs U0 {1,S}
4   Cs U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.41,7.05,8.02,8.53,8.87,8.85,8.57],'cal/(mol*K)'),
        H298 = (-0.49,'kcal/mol'),
        S298 = (-34.44,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CdsCsCsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cs U0 {1,S}
4   Cs U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cd)CsCsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cs U0 {1,S}
4   Cs U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cds)CsCsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cs U0 {1,S}
4   Cs U0 {1,S}
5   Ss U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd)CsCsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cs  U0 {1,S}
4   Cs  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)CsCsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cs  U0 {1,S}
4   Cs  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Cd)CsCsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cs  U0 {1,S}
4   Cs  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SCsCsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cs U0 {1,S}
4   Cs U0 {1,S}
5   Ss U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-SsCtCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Ss U0 {1,S}
3   Ct U0 {1,S}
4   Cs U0 {1,S}
5   Cs U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CbCsCsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Cs U0 {1,S}
4   Cs U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CdsCdsCsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cd U0 {1,S}
4   Cs U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cd)(Cds-Cd)CsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cd U0 {1,S}
4   Cs U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cds)(Cds-Cds)CsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Cs U0 {1,S}
5   Ss U0 {1,S}
6   Cd U0 {2,D}
7   Cd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd)(Cds-Cds)CsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cs  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D}
7   Cd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cds)CsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cs  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cs  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   C   U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd)(Cds-Cdd)CsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cs  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D}
7   Cdd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)CsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cs  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Sd  U0 {6,D}
9   Sd  U0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Cd)CsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cs  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Sd  U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cs  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   C   U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cd)CsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S}
4   Cs U0 {1,S}
5   Ss U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cds)CsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {7,D}
3   Cd U0 {1,S} {6,D}
4   Cs U0 {1,S}
5   Ss U0 {1,S}
6   Cd U0 {3,D}
7   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd)CsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {7,D}
3   Cd  U0 {1,S} {6,D}
4   Cs  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {3,D}
7   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Sd)CsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {6,D}
4   Cs  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   Sd  U0 {6,D}
8   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Cd)CsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {6,D}
4   Cs  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
8   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=SCsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Cs U0 {1,S}
5   Ss U0 {1,S}
6   Sd U0 {2,D}
7   Sd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CtCdsCsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Ct U0 {1,S}
3   Cd U0 {1,S}
4   Cs U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cd)CtCsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Ct U0 {1,S}
4   Cs U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cds)CtCsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Ct U0 {1,S}
4   Cs U0 {1,S}
5   Ss U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd)CtCsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ct  U0 {1,S}
4   Cs  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)CtCsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ct  U0 {1,S}
4   Cs  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Cd)CtCsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ct  U0 {1,S}
4   Cs  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SCtCsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Ct U0 {1,S}
4   Cs U0 {1,S}
5   Ss U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CbCdsCsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Cd U0 {1,S}
4   Cs U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cd)CbCsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cb U0 {1,S}
4   Cs U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cds)CbCsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cb U0 {1,S}
4   Cs U0 {1,S}
5   Ss U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd)CbCsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Cs  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)CbCsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Cs  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Cd)CbCsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Cs  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SCbCsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cb U0 {1,S}
4   Cs U0 {1,S}
5   Ss U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CtCtCsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Ct U0 {1,S}
3   Ct U0 {1,S}
4   Cs U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CbCtCsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Ct U0 {1,S}
4   Cs U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CbCbCsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Cb U0 {1,S}
4   Cs U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CdsCdsCdsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cd U0 {1,S}
4   Cd U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cd U0 {1,S}
4   Cd U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Cd U0 {1,S} {8,D}
5   Ss U0 {1,S}
6   Cd U0 {2,D}
7   Cd U0 {3,D}
8   Cd U0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cd  U0 {1,S} {8,D}
5   Ss  U0 {1,S}
6   Cd  U0 {2,D}
7   Cd  U0 {3,D}
8   Cdd U0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Sd)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cd  U0 {1,S} {8,D}
5   Ss  U0 {1,S}
6   Cd  U0 {2,D}
7   Cd  U0 {3,D}
8   Cdd U0 {4,D} {9,D}
9   Sd  U0 {8,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cd  U0 {1,S} {8,D}
5   Ss  U0 {1,S}
6   Cd  U0 {2,D}
7   Cd  U0 {3,D}
8   Cdd U0 {4,D} {9,D}
9   C   U0 {8,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cd  U0 {1,S} {8,D}
5   Ss  U0 {1,S}
6   Cd  U0 {2,D}
7   Cdd U0 {3,D}
8   Cdd U0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cds)(Cds-Cdd-Sd)(Cds-Cdd-Sd)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Ss  U0 {1,S}
6    Cd  U0 {2,D}
7    Cdd U0 {3,D} {9,D}
8    Cdd U0 {4,D} {10,D}
9    Sd  U0 {7,D}
10   Sd  U0 {8,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cds)(Cds-Cdd-Sd)(Cds-Cdd-Cd)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Ss  U0 {1,S}
6    Cd  U0 {2,D}
7    Cdd U0 {3,D} {9,D}
8    Cdd U0 {4,D} {10,D}
9    Sd  U0 {7,D}
10   C   U0 {8,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Ss  U0 {1,S}
6    Cd  U0 {2,D}
7    Cdd U0 {3,D} {9,D}
8    Cdd U0 {4,D} {10,D}
9    C   U0 {7,D}
10   C   U0 {8,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cd  U0 {1,S} {8,D}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D}
7   Cdd U0 {3,D}
8   Cdd U0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)(Cds-Cdd-Sd)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Ss  U0 {1,S}
6    Cdd U0 {2,D} {9,D}
7    Cdd U0 {3,D} {10,D}
8    Cdd U0 {4,D} {11,D}
9    Sd  U0 {6,D}
10   Sd  U0 {7,D}
11   Sd  U0 {8,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)(Cds-Cdd-Cd)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Ss  U0 {1,S}
6    Cdd U0 {2,D} {9,D}
7    Cdd U0 {3,D} {10,D}
8    Cdd U0 {4,D} {11,D}
9    Sd  U0 {6,D}
10   Sd  U0 {7,D}
11   C   U0 {8,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Ss  U0 {1,S}
6    Cdd U0 {2,D} {9,D}
7    Cdd U0 {3,D} {10,D}
8    Cdd U0 {4,D} {11,D}
9    Sd  U0 {6,D}
10   C   U0 {7,D}
11   C   U0 {8,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {6,D}
3    Cd  U0 {1,S} {7,D}
4    Cd  U0 {1,S} {8,D}
5    Ss  U0 {1,S}
6    Cdd U0 {2,D} {9,D}
7    Cdd U0 {3,D} {10,D}
8    Cdd U0 {4,D} {11,D}
9    C   U0 {6,D}
10   C   U0 {7,D}
11   C   U0 {8,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cd)(Cds-Cd)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S}
4   Cd U0 {1,S}
5   Ss U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cds)(Cds-Cds)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {8,D}
3   Cd U0 {1,S} {6,D}
4   Cd U0 {1,S} {7,D}
5   Ss U0 {1,S}
6   Cd U0 {3,D}
7   Cd U0 {4,D}
8   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd)(Cds-Cds)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Ss  U0 {1,S}
6   Cdd U0 {3,D}
7   Cd  U0 {4,D}
8   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Sd)(Cds-Cds)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {9,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Ss  U0 {1,S}
6   Cdd U0 {3,D} {8,D}
7   Cd  U0 {4,D}
8   Sd  U0 {6,D}
9   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Cd)(Cds-Cds)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {9,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Ss  U0 {1,S}
6   Cdd U0 {3,D} {8,D}
7   Cd  U0 {4,D}
8   C   U0 {6,D}
9   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd)(Cds-Cdd)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {6,D}
4   Cd  U0 {1,S} {7,D}
5   Ss  U0 {1,S}
6   Cdd U0 {3,D}
7   Cdd U0 {4,D}
8   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Sd)(Cds-Cdd-Sd)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {10,D}
3    Cd  U0 {1,S} {6,D}
4    Cd  U0 {1,S} {7,D}
5    Ss  U0 {1,S}
6    Cdd U0 {3,D} {8,D}
7    Cdd U0 {4,D} {9,D}
8    Sd  U0 {6,D}
9    Sd  U0 {7,D}
10   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Sd)(Cds-Cdd-Cd)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {10,D}
3    Cd  U0 {1,S} {6,D}
4    Cd  U0 {1,S} {7,D}
5    Ss  U0 {1,S}
6    Cdd U0 {3,D} {8,D}
7    Cdd U0 {4,D} {9,D}
8    Sd  U0 {6,D}
9    C   U0 {7,D}
10   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2    Cd  U0 {1,S} {10,D}
3    Cd  U0 {1,S} {6,D}
4    Cd  U0 {1,S} {7,D}
5    Ss  U0 {1,S}
6    Cdd U0 {3,D} {8,D}
7    Cdd U0 {4,D} {9,D}
8    C   U0 {6,D}
9    C   U0 {7,D}
10   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=S(Cds-Cd)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Cd U0 {1,S}
5   Ss U0 {1,S}
6   Sd U0 {2,D}
7   Sd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=S(Cds-Cds)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {7,D}
3   Cd U0 {1,S} {8,D}
4   Cd U0 {1,S} {6,D}
5   Ss U0 {1,S}
6   Cd U0 {4,D}
7   Sd U0 {2,D}
8   Sd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=S(Cds-Cdd)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {7,D}
3   Cd  U0 {1,S} {8,D}
4   Cd  U0 {1,S} {6,D}
5   Ss  U0 {1,S}
6   Cdd U0 {4,D}
7   Sd  U0 {2,D}
8   Sd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=S(Cds-Cdd-Sd)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {9,D}
4   Cd  U0 {1,S} {6,D}
5   Ss  U0 {1,S}
6   Cdd U0 {4,D} {7,D}
7   Sd  U0 {6,D}
8   Sd  U0 {2,D}
9   Sd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=S(Cds-Cdd-Cd)Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {9,D}
4   Cd  U0 {1,S} {6,D}
5   Ss  U0 {1,S}
6   Cdd U0 {4,D} {7,D}
7   C   U0 {6,D}
8   Sd  U0 {2,D}
9   Sd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=SC=SSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Cd U0 {1,S} {8,D}
5   Ss U0 {1,S}
6   Sd U0 {2,D}
7   Sd U0 {3,D}
8   Sd U0 {4,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CtCdsCdsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Ct U0 {1,S}
3   Cd U0 {1,S}
4   Cd U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cd)(Cds-Cd)CtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cd U0 {1,S}
4   Ct U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cds)(Cds-Cds)CtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Ct U0 {1,S}
5   Ss U0 {1,S}
6   Cd U0 {2,D}
7   Cd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd)(Cds-Cds)CtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ct  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D}
7   Cd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cds)CtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ct  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ct  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   C   U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd)(Cds-Cdd)CtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ct  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D}
7   Cdd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)CtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ct  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Sd  U0 {6,D}
9   Sd  U0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Cd)CtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ct  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Sd  U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ct  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   C   U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cd)CtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S}
4   Ct U0 {1,S}
5   Ss U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cds)CtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {7,D}
3   Cd U0 {1,S} {6,D}
4   Ct U0 {1,S}
5   Ss U0 {1,S}
6   Cd U0 {3,D}
7   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd)CtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {7,D}
3   Cd  U0 {1,S} {6,D}
4   Ct  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {3,D}
7   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Sd)CtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {6,D}
4   Ct  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   Sd  U0 {6,D}
8   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Cd)CtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {6,D}
4   Ct  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
8   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=SCtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Ct U0 {1,S}
5   Ss U0 {1,S}
6   Sd U0 {2,D}
7   Sd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CbCdsCdsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Cd U0 {1,S}
4   Cd U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cd)(Cds-Cd)CbSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cd U0 {1,S}
4   Cb U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cds)(Cds-Cds)CbSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Cb U0 {1,S}
5   Ss U0 {1,S}
6   Cd U0 {2,D}
7   Cd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd)(Cds-Cds)CbSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D}
7   Cd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cds)CbSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cds)CbSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   C   U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd)(Cds-Cdd)CbSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D}
7   Cdd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)CbSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Sd  U0 {6,D}
9   Sd  U0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Cd)CbSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Sd  U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Cb  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   C   U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cd)CbSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S}
4   Cb U0 {1,S}
5   Ss U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cds)CbSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {7,D}
3   Cd U0 {1,S} {6,D}
4   Cb U0 {1,S}
5   Ss U0 {1,S}
6   Cd U0 {3,D}
7   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd)CbSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {7,D}
3   Cd  U0 {1,S} {6,D}
4   Cb  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {3,D}
7   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Sd)CbSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {6,D}
4   Cb  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   Sd  U0 {6,D}
8   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Cd)CbSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {6,D}
4   Cb  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
8   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=SCbSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Cb U0 {1,S}
5   Ss U0 {1,S}
6   Sd U0 {2,D}
7   Sd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CtCtCdsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Ct U0 {1,S}
3   Ct U0 {1,S}
4   Cd U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cd)CtCtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Ct U0 {1,S}
4   Ct U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cds)CtCtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Ct U0 {1,S}
4   Ct U0 {1,S}
5   Ss U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd)CtCtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ct  U0 {1,S}
4   Ct  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)CtCtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ct  U0 {1,S}
4   Ct  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Cd)CtCtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ct  U0 {1,S}
4   Ct  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SCtCtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Ct U0 {1,S}
4   Ct U0 {1,S}
5   Ss U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CbCtCdsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Ct U0 {1,S}
4   Cd U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cd)CbCtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cb U0 {1,S}
4   Ct U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cds)CbCtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cb U0 {1,S}
4   Ct U0 {1,S}
5   Ss U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd)CbCtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Ct  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)CbCtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Ct  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Cd)CbCtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Ct  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SCbCtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cb U0 {1,S}
4   Ct U0 {1,S}
5   Ss U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CbCbCdsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Cb U0 {1,S}
4   Cd U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cd)CbCbSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cb U0 {1,S}
4   Cb U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cds)CbCbSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cb U0 {1,S}
4   Cb U0 {1,S}
5   Ss U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd)CbCbSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Cb  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)CbCbSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Cb  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Cd)CbCbSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Cb  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SCbCbSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cb U0 {1,S}
4   Cb U0 {1,S}
5   Ss U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CtCtCtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Ct U0 {1,S}
3   Ct U0 {1,S}
4   Ct U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CbCtCtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Ct U0 {1,S}
4   Ct U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CbCbCtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Cb U0 {1,S}
4   Ct U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CbCbCbSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Cb U0 {1,S}
4   Cb U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CCSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   C  U0 {1,S}
3   C  U0 {1,S}
4   Ss U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1202,
    label        = "Cs-CsCsSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cs U0 {1,S}
3   Cs U0 {1,S}
4   Ss U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.17,8.72,9.4,9.63,9.55,9.29,8.67],'cal/(mol*K)'),
        H298 = (-1.34,'kcal/mol'),
        S298 = (-36.66,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CdsCsSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cs U0 {1,S}
4   Ss U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cd)CsSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cs U0 {1,S}
4   Ss U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cds)CsSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cs U0 {1,S}
4   Ss U0 {1,S}
5   Ss U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd)CsSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cs  U0 {1,S}
4   Ss  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)CsSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cs  U0 {1,S}
4   Ss  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Cd)CsSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cs  U0 {1,S}
4   Ss  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SCsSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cs U0 {1,S}
4   Ss U0 {1,S}
5   Ss U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CdsCdsSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cd U0 {1,S}
4   Ss U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cd)(Cds-Cd)SsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cd U0 {1,S}
4   Ss U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cds)(Cds-Cds)SsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Ss U0 {1,S}
5   Ss U0 {1,S}
6   Cd U0 {2,D}
7   Cd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd)(Cds-Cds)SsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ss  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D}
7   Cd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cds)SsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ss  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cds)SsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ss  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   C   U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd)(Cds-Cdd)SsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ss  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D}
7   Cdd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)SsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ss  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Sd  U0 {6,D}
9   Sd  U0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Cd)SsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ss  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Sd  U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)SsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ss  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   C   U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cd)SsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S}
4   Ss U0 {1,S}
5   Ss U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cds)SsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {7,D}
3   Cd U0 {1,S} {6,D}
4   Ss U0 {1,S}
5   Ss U0 {1,S}
6   Cd U0 {3,D}
7   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd)SsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {7,D}
3   Cd  U0 {1,S} {6,D}
4   Ss  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {3,D}
7   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Sd)SsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {6,D}
4   Ss  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   Sd  U0 {6,D}
8   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Cd)SsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {6,D}
4   Ss  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
8   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=SSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Ss U0 {1,S}
5   Ss U0 {1,S}
6   Sd U0 {2,D}
7   Sd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CtCsSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Ct U0 {1,S}
3   Cs U0 {1,S}
4   Ss U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CtCdsSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Ct U0 {1,S}
3   Cd U0 {1,S}
4   Ss U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cd)CtSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Ct U0 {1,S}
4   Ss U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cds)CtSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Ct U0 {1,S}
4   Ss U0 {1,S}
5   Ss U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd)CtSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ct  U0 {1,S}
4   Ss  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)CtSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ct  U0 {1,S}
4   Ss  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Cd)CtSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ct  U0 {1,S}
4   Ss  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SCtSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Ct U0 {1,S}
4   Ss U0 {1,S}
5   Ss U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CtCtSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Ct U0 {1,S}
3   Ct U0 {1,S}
4   Ss U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CbCsSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Cs U0 {1,S}
4   Ss U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CbCdsSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Cd U0 {1,S}
4   Ss U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cd)CbSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cb U0 {1,S}
4   Ss U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cds)CbSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cb U0 {1,S}
4   Ss U0 {1,S}
5   Ss U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd)CbSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Ss  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)CbSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Ss  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Cd)CbSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Ss  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SCbSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cb U0 {1,S}
4   Ss U0 {1,S}
5   Ss U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CbCtSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Ct U0 {1,S}
4   Ss U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CbCbSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Cb U0 {1,S}
4   Ss U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CSsSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   C  U0 {1,S}
3   Ss U0 {1,S}
4   Ss U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1203,
    label        = "Cs-CsSsSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cs U0 {1,S}
3   Ss U0 {1,S}
4   Ss U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.45,9.59,10.49,10.71,10.42,9.94,8.92],'cal/(mol*K)'),
        H298 = (-1.8,'kcal/mol'),
        S298 = (-38.19,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CdsSsSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Ss U0 {1,S}
4   Ss U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cd)SsSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Ss U0 {1,S}
4   Ss U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cds)SsSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Ss U0 {1,S}
4   Ss U0 {1,S}
5   Ss U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd)SsSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ss  U0 {1,S}
4   Ss  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)SsSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ss  U0 {1,S}
4   Ss  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Cd)SsSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ss  U0 {1,S}
4   Ss  U0 {1,S}
5   Ss  U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SSsSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Ss U0 {1,S}
4   Ss U0 {1,S}
5   Ss U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CtSsSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Ct U0 {1,S}
3   Ss U0 {1,S}
4   Ss U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CbSsSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Ss U0 {1,S}
4   Ss U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-SsSsSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Ss U0 {1,S}
3   Ss U0 {1,S}
4   Ss U0 {1,S}
5   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CSsSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   C  U0 {1,S}
3   Ss U0 {1,S}
4   Ss U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1173,
    label        = "Cs-CsSsSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cs U0 {1,S}
3   Ss U0 {1,S}
4   Ss U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.82,9.05,9.73,10.14,10.63,10.97,11.44],'cal/(mol*K)'),
        H298 = (-3.3,'kcal/mol'),
        S298 = (-14.59,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CdsSsSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Ss U0 {1,S}
4   Ss U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cd)SsSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Ss U0 {1,S}
4   Ss U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cds)SsSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Ss U0 {1,S}
4   Ss U0 {1,S}
5   H  U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd)SsSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ss  U0 {1,S}
4   Ss  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)SsSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ss  U0 {1,S}
4   Ss  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Cd)SsSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ss  U0 {1,S}
4   Ss  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SSsSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Ss U0 {1,S}
4   Ss U0 {1,S}
5   H  U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CtSsSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Ct U0 {1,S}
3   Ss U0 {1,S}
4   Ss U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CbSsSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Ss U0 {1,S}
4   Ss U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CCSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   C  U0 {1,S}
3   C  U0 {1,S}
4   Ss U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1169,
    label        = "Cs-CsCsSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cs U0 {1,S}
3   Cs U0 {1,S}
4   Ss U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.01,6.7,7.96,8.83,9.89,10.51,11.27],'cal/(mol*K)'),
        H298 = (-1.98,'kcal/mol'),
        S298 = (-11.89,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1170,
    label        = "Cs-CdsCsSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cs U0 {1,S}
4   Ss U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.41,9.85,10.93,11.28,11.37,11.41,11.61],'cal/(mol*K)'),
        H298 = (-2.15,'kcal/mol'),
        S298 = (-15.26,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cd)CsSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cs U0 {1,S}
4   Ss U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cds)CsSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cs U0 {1,S}
4   Ss U0 {1,S}
5   H  U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd)CsSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cs  U0 {1,S}
4   Ss  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)CsSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cs  U0 {1,S}
4   Ss  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Cd)CsSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cs  U0 {1,S}
4   Ss  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1174,
    label        = "Cs-C=SCsSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cs U0 {1,S}
4   Ss U0 {1,S}
5   H  U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.53,10.09,11.25,11.65,11.76,11.74,11.77],'cal/(mol*K)'),
        H298 = (-3.49,'kcal/mol'),
        S298 = (-15.86,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CdsCdsSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cd U0 {1,S}
4   Ss U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cd)(Cds-Cd)SsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cd U0 {1,S}
4   Ss U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cds)(Cds-Cds)SsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Ss U0 {1,S}
5   H  U0 {1,S}
6   Cd U0 {2,D}
7   Cd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd)(Cds-Cds)SsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ss  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D}
7   Cd  U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cds)SsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ss  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cds)SsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ss  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cd  U0 {3,D}
8   C   U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd)(Cds-Cdd)SsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ss  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D}
7   Cdd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)SsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ss  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Sd  U0 {6,D}
9   Sd  U0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)(Cds-Cdd-Cd)SsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ss  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   Sd  U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)SsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cd  U0 {1,S} {7,D}
4   Ss  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {8,D}
7   Cdd U0 {3,D} {9,D}
8   C   U0 {6,D}
9   C   U0 {7,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cd)SsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S}
4   Ss U0 {1,S}
5   H  U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cds)SsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {7,D}
3   Cd U0 {1,S} {6,D}
4   Ss U0 {1,S}
5   H  U0 {1,S}
6   Cd U0 {3,D}
7   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd)SsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {7,D}
3   Cd  U0 {1,S} {6,D}
4   Ss  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {3,D}
7   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Sd)SsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {6,D}
4   Ss  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   Sd  U0 {6,D}
8   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=S(Cds-Cdd-Cd)SsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {8,D}
3   Cd  U0 {1,S} {6,D}
4   Ss  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {3,D} {7,D}
7   C   U0 {6,D}
8   Sd  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SC=SSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cd U0 {1,S} {7,D}
4   Ss U0 {1,S}
5   H  U0 {1,S}
6   Sd U0 {2,D}
7   Sd U0 {3,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1171,
    label        = "Cs-CtCsSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Ct U0 {1,S}
3   Cs U0 {1,S}
4   Ss U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.08,6.78,7.93,8.72,9.73,10.35,11.19],'cal/(mol*K)'),
        H298 = (0.72,'kcal/mol'),
        S298 = (-11.64,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CtCdsSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Ct U0 {1,S}
3   Cd U0 {1,S}
4   Ss U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cd)CtSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Ct U0 {1,S}
4   Ss U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cds)CtSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Ct U0 {1,S}
4   Ss U0 {1,S}
5   H  U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd)CtSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ct  U0 {1,S}
4   Ss  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)CtSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ct  U0 {1,S}
4   Ss  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Cd)CtSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ct  U0 {1,S}
4   Ss  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SCtSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Ct U0 {1,S}
4   Ss U0 {1,S}
5   H  U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CtCtSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Ct U0 {1,S}
3   Ct U0 {1,S}
4   Ss U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1172,
    label        = "Cs-CbCsSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Cs U0 {1,S}
4   Ss U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.38,7.96,9.03,9.69,10.45,10.89,11.47],'cal/(mol*K)'),
        H298 = (-1.66,'kcal/mol'),
        S298 = (-13.65,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CbCdsSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Cd U0 {1,S}
4   Ss U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cd)CbSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Cb U0 {1,S}
4   Ss U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cds)CbSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cb U0 {1,S}
4   Ss U0 {1,S}
5   H  U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd)CbSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Ss  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)CbSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Ss  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Cd)CbSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Cb  U0 {1,S}
4   Ss  U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-C=SCbSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Cb U0 {1,S}
4   Ss U0 {1,S}
5   H  U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CbCtSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Ct U0 {1,S}
4   Ss U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CbCbSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Cb U0 {1,S}
4   Ss U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-CSsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   C  U0 {1,S}
3   Ss U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1163,
    label        = "Cs-CsSsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cs U0 {1,S}
3   Ss U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.11,6.59,7.97,9.15,10.99,12.33,14.32],'cal/(mol*K)'),
        H298 = (-4.94,'kcal/mol'),
        S298 = (9.92,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1164,
    label        = "Cs-CdsSsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Ss U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.17,9.71,10.55,11.14,12.11,12.95,14.43],'cal/(mol*K)'),
        H298 = (-5.07,'kcal/mol'),
        S298 = (6.75,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cd)SsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S}
3   Ss U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cds)SsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Ss U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
6   Cd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd)SsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ss  U0 {1,S}
4   H   U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Sd)SsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ss  U0 {1,S}
4   H   U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   Sd  U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Cs-(Cds-Cdd-Cd)SsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs  U0 {2,S} {3,S} {4,S} {5,S}
2   Cd  U0 {1,S} {6,D}
3   Ss  U0 {1,S}
4   H   U0 {1,S}
5   H   U0 {1,S}
6   Cdd U0 {2,D} {7,D}
7   C   U0 {6,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1168,
    label        = "Cs-C=SSsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cd U0 {1,S} {6,D}
3   Ss U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
6   Sd U0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.23,10.43,11.42,11.97,12.76,13.43,14.63],'cal/(mol*K)'),
        H298 = (-6.13,'kcal/mol'),
        S298 = (5.73,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1165,
    label        = "Cs-CtSsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Ct U0 {1,S}
3   Ss U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.19,7.02,8.42,9.51,11.14,12.34,14.18],'cal/(mol*K)'),
        H298 = (-2.69,'kcal/mol'),
        S298 = (9.75,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1166,
    label        = "Cs-CbSsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cb U0 {1,S}
3   Ss U0 {1,S}
4   H  U0 {1,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.3,7.96,9.19,10.12,11.53,12.59,14.26],'cal/(mol*K)'),
        H298 = (-5.04,'kcal/mol'),
        S298 = (8.26,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1093,
    label        = "O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * O U0
""",
    thermo = u'Os-CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1094,
    label        = "Od",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Od U0
""",
    thermo = u'Od-Cd',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1095,
    label        = "Od-Cd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Od      U0 {2,D}
2   {Cd,CO} U0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""In this case the C is treated as the central atom""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1096,
    label        = "Od-Od",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Od U0 {2,D}
2   Od U0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.5,3.575,3.685,3.8,3.99,4.12,4.29],'cal/(mol*K)'),
        H298 = (14.01,'kcal/mol'),
        S298 = (24.085,'cal/(mol*K)'),
    ),
    shortDesc = u"""A. Vandeputte""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1943,
    label        = "Od-N3d",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Od  U0 {2,D}
2   N3d U0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1944,
    label        = "Od-N5d",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Od  U0 {2,D}
2   N5d U0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1097,
    label        = "Os",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os U0
""",
    thermo = u'Os-(Cds-Cd)(Cds-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1945,
    label        = "Os-N",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os U0 {2,S}
2   N  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1935,
    label        = "Os-CN",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os U0 {2,S} {3,S}
2   C  U0 {1,S}
3   N  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1874,
    label        = "Os-CsN3s",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os  U0 {2,S} {3,S}
2   N3s U0 {1,S}
3   Cs  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.5,3.6,4,4.3,4.7,4.8,4.2],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-9.2,'kcal/mol','+|-',1.3),
        S298 = (7.2,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1875,
    label        = "Os-CsN3d",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os  U0 {2,S} {3,S}
2   Cs  U0 {1,S}
3   N3d U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1847,
    label        = "Os-Cs(N3dOd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os  U0 {2,S} {4,S}
2   N3d U0 {1,S} {3,D}
3   Od  U0 {2,D}
4   Cs  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.6,11.3,11.9,12.6,13.6,14.3,14.8],'cal/(mol*K)','+|-',[0.8,0.8,0.8,0.8,0.8,0.8,0.8]),
        H298 = (-4.8,'kcal/mol','+|-',1.1),
        S298 = (40,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1877,
    label        = "Os-CdN3d",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os  U0 {2,S} {3,S}
2   Cd  U0 {1,S}
3   N3d U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1878,
    label        = "Os-(Cd-Cd)(N3dOd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os  U0 {2,S} {4,S}
2   N3d U0 {1,S} {3,D}
3   Od  U0 {2,D}
4   Cd  U0 {1,S} {5,D} {6,S}
5   Cd  U0 {4,D}
6   R   U0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.1,11.7,12.2,12.7,13.5,14.1,14.9],'cal/(mol*K)','+|-',[0.7,0.7,0.7,0.7,0.7,0.7,0.7]),
        H298 = (-5.3,'kcal/mol','+|-',0.9),
        S298 = (39.5,'cal/(mol*K)','+|-',0.9),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1876,
    label        = "Os-CsN5d",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os  U0 {2,S} {3,S}
2   Cs  U0 {1,S}
3   N5d U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1848,
    label        = "Os-Cs(N5dOdOs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os  U0 {2,S} {5,S}
2   N5d U0 {1,S} {3,D} {4,S}
3   Od  U0 {2,D}
4   Os  U0 {2,S}
5   Cs  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.2,13.9,15.4,16.6,18.4,19.3,19.9],'cal/(mol*K)','+|-',[0.8,0.8,0.8,0.8,0.8,0.8,0.8]),
        H298 = (-19.1,'kcal/mol','+|-',1.1),
        S298 = (45.3,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1879,
    label        = "Os-CdN5d",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os  U0 {2,S} {3,S}
2   Cd  U0 {1,S}
3   N5d U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1880,
    label        = "Os-(Cd-CdHH)(N5dOdOs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os  U0 {2,S} {5,S}
2   N5d U0 {1,S} {3,D} {4,S}
3   Od  U0 {2,D}
4   Os  U0 {2,S}
5   Cd  U0 {1,S} {6,D} {7,S}
6   Cd  U0 {5,D}
7   R   U0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.4,14.2,15.7,16.9,18.5,19.3,20.1],'cal/(mol*K)','+|-',[0.8,0.8,0.8,0.8,0.8,0.8,0.8]),
        H298 = (-18.4,'kcal/mol','+|-',1.1),
        S298 = (45.4,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1936,
    label        = "Os-ON",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os U0 {2,S} {3,S}
2   O  U0 {1,S}
3   N  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1881,
    label        = "Os-OsN3s",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os  U0 {2,S} {3,S}
2   N3s U0 {1,S}
3   Os  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.3,4.9,5.6,6.3,7,7.1,6.5],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (5.3,'kcal/mol','+|-',1.3),
        S298 = (6.9,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1882,
    label        = "Os-OsN3d",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os  U0 {2,S} {3,S}
2   Os  U0 {1,S}
3   N3d U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1883,
    label        = "Os-Os(N3dOd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os  U0 {2,S} {4,S}
2   N3d U0 {1,S} {3,D}
3   Od  U0 {2,D}
4   Os  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.7,12.9,13.6,14.2,15,15.5,16],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (15.2,'kcal/mol','+|-',1.3),
        S298 = (40.7,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1937,
    label        = "Os-NN",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os U0 {2,S} {3,S}
2   N  U0 {1,S}
3   N  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1884,
    label        = "Os-N3sN3s",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os  U0 {2,S} {3,S}
2   N3s U0 {1,S}
3   N3s U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.8,4.6,5.1,5.2,5.2,4.9,4.3],'cal/(mol*K)','+|-',[1.6,1.6,1.6,1.6,1.6,1.6,1.6]),
        H298 = (5.7,'kcal/mol','+|-',2.2),
        S298 = (6.8,'cal/(mol*K)','+|-',2.1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1885,
    label        = "Os-N3sN3d",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os  U0 {2,S} {3,S}
2   N3s U0 {1,S}
3   N3d U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1886,
    label        = "Os-N3s(N3dOd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os  U0 {2,S} {4,S}
2   N3d U0 {1,S} {3,D}
3   Od  U0 {2,D}
4   N3s U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.2,11.5,12.4,13,13.9,14.3,14.8],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (10.8,'kcal/mol','+|-',1.3),
        S298 = (40.8,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1098,
    label        = "Os-HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os U0 {2,S} {3,S}
2   H  U0 {1,S}
3   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.03,8.19,8.42,8.68,9.26,9.86,11.26],'cal/(mol*K)'),
        H298 = (-57.8,'kcal/mol','+|-',0.01),
        S298 = (46.51,'cal/(mol*K)','+|-',0.002),
    ),
    shortDesc = u"""O-HH WATER. !!!Using NIST value for H2O, S(group) = S(H2O) + Rln(2)""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1099,
    label        = "Os-OsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os U0 {2,S} {3,S}
2   Os U0 {1,S}
3   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.21,5.72,6.17,6.66,7.15,7.61,8.43],'cal/(mol*K)','+|-',[0.07,0.07,0.07,0.07,0.07,0.07,0.07]),
        H298 = (-16.3,'kcal/mol','+|-',0.14),
        S298 = (27.83,'cal/(mol*K)','+|-',0.07),
    ),
    shortDesc = u"""O-OH SANDIA 1/2*H2O2""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1100,
    label        = "Os-OsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os U0 {2,S} {3,S}
2   Os U0 {1,S}
3   Os U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.2,3.64,4.2,4.34,4.62,4.9,4.9],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (8.85,'kcal/mol','+|-',0.16),
        S298 = (9.4,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""O-OO LAY 1997=20 !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1101,
    label        = "Os-CH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os U0 {2,S} {3,S}
2   C  U0 {1,S}
3   H  U0 {1,S}
""",
    thermo = u'Os-CsH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1102,
    label        = "Os-CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os U0 {2,S} {3,S}
2   Ct U0 {1,S}
3   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.3,4.5,4.82,5.23,6.02,6.61,7.44],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-37.9,'kcal/mol','+|-',0.16),
        S298 = (29.1,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""O-CtH BENSON (Assigned O-CsH)""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1103,
    label        = "Os-CdsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os      U0 {2,S} {3,S}
2   {Cd,CO} U0 {1,S}
3   H       U0 {1,S}
""",
    thermo = u'Os-(Cds-Cd)H',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1104,
    label        = "Os-(Cds-Od)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os U0 {2,S} {3,S}
2   CO U0 {1,S}
3   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.8,5,5.8,6.3,7.2,7.8,7.8],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-58.1,'kcal/mol','+|-',0.16),
        S298 = (24.5,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""O-COH !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1105,
    label        = "Os-(Cds-Cd)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os U0 {2,S} {3,S}
2   Cd U0 {1,S} {4,D}
3   H  U0 {1,S}
4   Cd U0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.3,4.5,4.82,5.23,6.02,6.61,7.44],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-37.9,'kcal/mol','+|-',0.16),
        S298 = (29.1,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""O-CdH BENSON (Assigned O-CsH)""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1106,
    label        = "Os-CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os U0 {2,S} {3,S}
2   Cs U0 {1,S}
3   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.3,4.5,4.82,5.23,6.02,6.61,7.44],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-37.9,'kcal/mol','+|-',0.2),
        S298 = (29.07,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""O-CsH BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1107,
    label        = "Os-CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os U0 {2,S} {3,S}
2   Cb U0 {1,S}
3   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.3,4.5,4.82,5.23,6.02,6.61,7.44],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-37.9,'kcal/mol','+|-',0.16),
        S298 = (29.1,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""O-CbH BENSON (Assigned O-CsH)""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1457,
    label        = "Os-CSH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * O  U0 {2,S} {3,S}
2   C  U0 {1,S} {4,D}
3   H  U0 {1,S}
4   Sd U0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.17,8.51,9.68,10.66,12.14,13.14,14.38],'cal/(mol*K)'),
        H298 = (-20.04,'kcal/mol'),
        S298 = (33.59,'cal/(mol*K)'),
    ),
    shortDesc = u"""CAC calc 1D-HR""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1108,
    label        = "Os-OsC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os U0 {2,S} {3,S}
2   Os U0 {1,S}
3   C  U0 {1,S}
""",
    thermo = u'Os-OsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1109,
    label        = "Os-OsCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os U0 {2,S} {3,S}
2   Os U0 {1,S}
3   Ct U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.9,4.31,4.6,4.84,5.32,5.8,5.8],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (7,'kcal/mol','+|-',0.3),
        S298 = (10.8,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""O-OCb Hf JWB plot S,Cp assigned O/O/Cd !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1110,
    label        = "Os-OsCds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os      U0 {2,S} {3,S}
2   Os      U0 {1,S}
3   {Cd,CO} U0 {1,S}
""",
    thermo = u'Os-Os(Cds-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1111,
    label        = "Os-Os(Cds-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os U0 {2,S} {3,S}
2   Os U0 {1,S}
3   CO U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.53,5.02,5.79,6.08,6.54,6.49,6.49],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (-23.22,'kcal/mol','+|-',0.3),
        S298 = (9.11,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""O-OCO jwl cbsQ 99 cqcho=20 !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1112,
    label        = "Os-Os(Cds-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os U0 {2,S} {3,S}
2   Os U0 {1,S}
3   Cd U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.5,3.87,3.95,4.15,4.73,4.89,4.89],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (1.64,'kcal/mol','+|-',0.3),
        S298 = (10.12,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""O-OCd WESTMORELAND S,Cp LAY'9405 !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1113,
    label        = "Os-OsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os U0 {2,S} {3,S}
2   Os U0 {1,S}
3   Cs U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.9,4.31,4.6,4.84,5.32,5.8,5.8],'cal/(mol*K)','+|-',[0.15,0.15,0.15,0.15,0.15,0.15,0.15]),
        H298 = (-5.4,'kcal/mol','+|-',0.3),
        S298 = (8.54,'cal/(mol*K)','+|-',0.15),
    ),
    shortDesc = u"""O-OCs LAY 1997 !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1114,
    label        = "Os-OsCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os U0 {2,S} {3,S}
2   Os U0 {1,S}
3   Cb U0 {1,S}
""",
    thermo = u'Os-Os(Cds-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1115,
    label        = "Os-CC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os U0 {2,S} {3,S}
2   C  U0 {1,S}
3   C  U0 {1,S}
""",
    thermo = u'Os-(Cds-Cd)(Cds-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1116,
    label        = "Os-CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os U0 {2,S} {3,S}
2   Ct U0 {1,S}
3   Ct U0 {1,S}
""",
    thermo = u'Os-(Cds-Cd)(Cds-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1117,
    label        = "Os-CtCds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os      U0 {2,S} {3,S}
2   Ct      U0 {1,S}
3   {Cd,CO} U0 {1,S}
""",
    thermo = u'Os-(Cds-Cd)(Cds-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1118,
    label        = "Os-Ct(Cds-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os U0 {2,S} {3,S}
2   Ct U0 {1,S}
3   CO U0 {1,S}
""",
    thermo = u'Os-(Cds-Cd)(Cds-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1119,
    label        = "Os-Ct(Cds-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os U0 {2,S} {3,S}
2   Ct U0 {1,S}
3   Cd U0 {1,S}
""",
    thermo = u'Os-(Cds-Cd)(Cds-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1120,
    label        = "Os-CtCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os U0 {2,S} {3,S}
2   Ct U0 {1,S}
3   Cs U0 {1,S}
""",
    thermo = u'Os-Cs(Cds-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1873,
    label        = "Os-Cs(CtN3t)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os  U0 {2,S} {4,S}
2   Ct  U0 {1,S} {3,T}
3   N3t U0 {2,T}
4   Cs  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.1,9.8,10.6,11.2,12.3,13,13.8],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (10,'kcal/mol','+|-',1.3),
        S298 = (39.1,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1121,
    label        = "Os-CtCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os U0 {2,S} {3,S}
2   Ct U0 {1,S}
3   Cb U0 {1,S}
""",
    thermo = u'Os-(Cds-Cd)(Cds-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1122,
    label        = "Os-CdsCds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os      U0 {2,S} {3,S}
2   {Cd,CO} U0 {1,S}
3   {Cd,CO} U0 {1,S}
""",
    thermo = u'Os-(Cds-Cd)(Cds-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1123,
    label        = "Os-(Cds-Od)(Cds-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os U0 {2,S} {3,S}
2   CO U0 {1,S}
3   CO U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.45,4.74,5.28,5.74,5.89,6.1,6.1],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-46,'kcal/mol','+|-',0.19),
        S298 = (2.5,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""O-COCO Hf BENSON S,Cp Mopac=3D""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1124,
    label        = "Os-(Cds-Od)(Cds-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os U0 {2,S} {3,S}
2   CO U0 {1,S}
3   Cd U0 {1,S}
""",
    thermo = u'Os-(Cds-Cd)(Cds-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1125,
    label        = "Os-(Cds-Cd)(Cds-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os U0 {2,S} {3,S}
2   Cd U0 {1,S}
3   Cd U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.4,3.7,3.7,3.8,4.4,4.6,4.8],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-19.61,'kcal/mol','+|-',0.19),
        S298 = (10,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""O-CdCd BOZZELLI""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1126,
    label        = "Os-CdsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os      U0 {2,S} {3,S}
2   {Cd,CO} U0 {1,S}
3   Cs      U0 {1,S}
""",
    thermo = u'Os-Cs(Cds-Cd)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1127,
    label        = "Os-Cs(Cds-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os U0 {2,S} {3,S}
2   Cs U0 {1,S}
3   CO U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.91,4.31,4.6,4.84,5.32,5.8,5.8],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-42.19,'kcal/mol','+|-',0.19),
        S298 = (8.4,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""O-COCs BOZZELLI Jul91 S,Cp ABaldwin O/Cs/O !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1128,
    label        = "Os-Cs(Cds-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os U0 {2,S} {3,S}
2   Cs U0 {1,S}
3   Cd U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.91,4.31,4.6,4.84,5.32,5.8,5.8],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-23.73,'kcal/mol','+|-',0.19),
        S298 = (9.7,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""O-CdCs Hf RADOM vin-oh S A.Baldwin O/Cs/O !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Os-CdsCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os      U0 {2,S} {3,S}
2   {Cd,CO} U0 {1,S}
3   Cb      U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Os-Cb(Cds-Od)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os U0 {2,S} {3,S}
2   Cb U0 {1,S}
3   CO U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Os-Cb(Cds-Cd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os U0 {2,S} {3,S}
2   Cb U0 {1,S}
3   Cd U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1129,
    label        = "Os-CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os U0 {2,S} {3,S}
2   Cs U0 {1,S}
3   Cs U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.4,3.7,3.7,3.8,4.4,4.6,4.6],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-23.2,'kcal/mol','+|-',0.19),
        S298 = (8.68,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""O-CsCs BENSON !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1130,
    label        = "Os-CsCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os U0 {2,S} {3,S}
2   Cs U0 {1,S}
3   Cb U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.4,3.7,3.7,3.8,4.4,4.6,4.6],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-22.6,'kcal/mol','+|-',0.19),
        S298 = (9.7,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""O-CbCs REID, PRAUSNITZ and SHERWOOD !!!WARNING! Cp1500 value taken as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1131,
    label        = "Os-CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Os U0 {2,S} {3,S}
2   Cb U0 {1,S}
3   Cb U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.19,-0.24,-0.72,-0.51,0.43,1.36,1.75],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]),
        H298 = (-18.77,'kcal/mol','+|-',0.19),
        S298 = (13.59,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""O-CbCb CHERN 1/97 Hf PEDLEY, Mopac""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1600,
    label        = "Si",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Si U0
""",
    thermo = u'Cs-HHHH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1400,
    label        = "S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * S U0
""",
    thermo = u'Ss-CsCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Sd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Sd U0
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1160,
    label        = "Sd-Cd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Sd U0 {2,D}
2   Cd U0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1161,
    label        = "Sd-Sd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Sd U0 {2,D}
2   Sd U0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.9,4.08,4.2,4.27,4.35,4.39,4.43],'cal/(mol*K)'),
        H298 = (22.82,'kcal/mol'),
        S298 = (26.89,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U0
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1132,
    label        = "Ss-HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U0 {2,S} {3,S}
2   H  U0 {1,S}
3   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.15,8.48,8.85,9.26,10.08,10.82,12.1],'cal/(mol*K)'),
        H298 = (-5.37,'kcal/mol'),
        S298 = (50.52,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Ss-CH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U0 {2,S} {3,S}
2   C  U0 {1,S}
3   H  U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1133,
    label        = "Ss-CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U0 {2,S} {3,S}
2   Cs U0 {1,S}
3   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.17,6.22,6.4,6.65,7.18,7.65,8.45],'cal/(mol*K)'),
        H298 = (5.05,'kcal/mol'),
        S298 = (33.68,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1134,
    label        = "Ss-CdH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U0 {2,S} {3,S}
2   Cd U0 {1,S}
3   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.01,6.82,7.28,7.55,7.9,8.18,8.7],'cal/(mol*K)'),
        H298 = (4.19,'kcal/mol'),
        S298 = (32.23,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1153,
    label        = "Ss-C=SH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U0 {2,S} {3,S}
2   Cd U0 {1,S} {4,D}
3   H  U0 {1,S}
4   Sd U0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.01,6.82,7.28,7.55,7.9,8.18,8.7],'cal/(mol*K)'),
        H298 = (4.19,'kcal/mol'),
        S298 = (32.23,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1135,
    label        = "Ss-CtH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U0 {2,S} {3,S}
2   Ct U0 {1,S}
3   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.22,6.87,7.26,7.55,7.94,8.24,8.73],'cal/(mol*K)'),
        H298 = (6.27,'kcal/mol'),
        S298 = (31.59,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1136,
    label        = "Ss-CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U0 {2,S} {3,S}
2   Cb U0 {1,S}
3   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.65,7.07,7.33,7.5,7.79,8.05,8.53],'cal/(mol*K)'),
        H298 = (3.91,'kcal/mol'),
        S298 = (31.98,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1458,
    label        = "Ss-COH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * S  U0 {2,S} {3,S}
2   C  U0 {1,S} {4,D}
3   H  U0 {1,S}
4   Od U0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.72,8.66,9.51,10.25,11.37,12.18,13.21],'cal/(mol*K)'),
        H298 = (-25.85,'kcal/mol'),
        S298 = (29.06,'cal/(mol*K)'),
    ),
    shortDesc = u"""CAC calc 1D-HR""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1147,
    label        = "Ss-SsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U0 {2,S} {3,S}
2   Ss U0 {1,S}
3   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.75,6.48,7.02,7.43,8.03,8.43,9],'cal/(mol*K)'),
        H298 = (1.97,'kcal/mol'),
        S298 = (31.73,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1152,
    label        = "Ss-SsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U0 {2,S} {3,S}
2   Ss U0 {1,S}
3   Ss U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.19,6.32,6.38,6.44,6.47,6.39,5.95],'cal/(mol*K)'),
        H298 = (3.03,'kcal/mol'),
        S298 = (11.18,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Ss-SsC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U0 {2,S} {3,S}
2   Ss U0 {1,S}
3   C  U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1148,
    label        = "Ss-SsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U0 {2,S} {3,S}
2   Ss U0 {1,S}
3   Cs U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.59,5.73,5.79,5.8,5.74,5.65,5.43],'cal/(mol*K)'),
        H298 = (6.99,'kcal/mol'),
        S298 = (12.61,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1149,
    label        = "Ss-SsCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U0 {2,S} {3,S}
2   Ss U0 {1,S}
3   Cd U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.41,5.92,6.11,6.14,5.98,5.74,5.25],'cal/(mol*K)'),
        H298 = (7.62,'kcal/mol'),
        S298 = (12.13,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1159,
    label        = "Ss-C=SSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U0 {2,S} {3,S}
2   Ss U0 {1,S}
3   Cd U0 {1,S} {4,D}
4   Sd U0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.25,5.49,5.65,5.74,5.74,5.65,5.37],'cal/(mol*K)'),
        H298 = (7.9,'kcal/mol'),
        S298 = (13.34,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1150,
    label        = "Ss-SsCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U0 {2,S} {3,S}
2   Ss U0 {1,S}
3   Ct U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.3,5.8,5.94,5.94,5.77,5.57,5.24],'cal/(mol*K)'),
        H298 = (11.93,'kcal/mol'),
        S298 = (12.73,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1151,
    label        = "Ss-SsCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U0 {2,S} {3,S}
2   Ss U0 {1,S}
3   Cb U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.71,5.93,5.98,5.92,5.67,5.38,4.78],'cal/(mol*K)'),
        H298 = (7.09,'kcal/mol'),
        S298 = (11.38,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "Ss-CC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U0 {2,S} {3,S}
2   C  U0 {1,S}
3   C  U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1137,
    label        = "Ss-CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U0 {2,S} {3,S}
2   Cs U0 {1,S}
3   Cs U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.8,5.76,5.63,5.51,5.3,5.18,5.07],'cal/(mol*K)'),
        H298 = (11.41,'kcal/mol'),
        S298 = (13.72,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1138,
    label        = "Ss-CsCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U0 {2,S} {3,S}
2   Cs U0 {1,S}
3   Cd U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.68,6.98,6.89,6.65,6.16,5.79,5.33],'cal/(mol*K)'),
        H298 = (9.83,'kcal/mol'),
        S298 = (11.01,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1154,
    label        = "Ss-C=SCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U0 {2,S} {3,S}
2   Cs U0 {1,S}
3   Cd U0 {1,S} {4,D}
4   Sd U0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.43,5.15,5.65,5.92,6.04,5.97,5.72],'cal/(mol*K)'),
        H298 = (6.87,'kcal/mol'),
        S298 = (11.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1139,
    label        = "Ss-CsCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U0 {2,S} {3,S}
2   Cs U0 {1,S}
3   Ct U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.45,5.71,5.77,5.73,5.57,5.42,5.2],'cal/(mol*K)'),
        H298 = (12.03,'kcal/mol'),
        S298 = (13.23,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1140,
    label        = "Ss-CsCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U0 {2,S} {3,S}
2   Cs U0 {1,S}
3   Cb U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.62,5.74,5.7,5.6,5.38,5.22,5],'cal/(mol*K)'),
        H298 = (10.51,'kcal/mol'),
        S298 = (12.6,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1141,
    label        = "Ss-CdCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U0 {2,S} {3,S}
2   Cd U0 {1,S}
3   Cd U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.82,6.48,6.62,6.51,6.09,5.74,5.25],'cal/(mol*K)'),
        H298 = (10.56,'kcal/mol'),
        S298 = (12.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1155,
    label        = "Ss-C=SCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U0 {2,S} {3,S}
2   Cd U0 {1,S}
3   Cd U0 {1,S} {4,D}
4   Sd U0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.13,6.41,7.01,7.14,6.87,6.48,5.84],'cal/(mol*K)'),
        H298 = (7.78,'kcal/mol'),
        S298 = (10.23,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1158,
    label        = "Ss-C=SC=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U0 {2,S} {3,S}
2   Cd U0 {1,S} {4,D}
3   Cd U0 {1,S} {5,D}
4   Sd U0 {2,D}
5   Sd U0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.98,5.28,5.67,6.04,6.51,6.52,5.77],'cal/(mol*K)'),
        H298 = (12.91,'kcal/mol'),
        S298 = (12.96,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1142,
    label        = "Ss-CdCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U0 {2,S} {3,S}
2   Cd U0 {1,S}
3   Ct U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.34,5.99,6.17,6.13,5.88,5.63,5.27],'cal/(mol*K)'),
        H298 = (12.84,'kcal/mol'),
        S298 = (12.07,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1156,
    label        = "Ss-C=SCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U0 {2,S} {3,S}
2   Cd U0 {1,S} {4,D}
3   Ct U0 {1,S}
4   Sd U0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.39,4.92,5.17,5.28,5.33,5.29,5.19],'cal/(mol*K)'),
        H298 = (15.16,'kcal/mol'),
        S298 = (14.06,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1143,
    label        = "Ss-CdCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U0 {2,S} {3,S}
2   Cd U0 {1,S}
3   Cb U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.91,6.42,6.51,6.38,6,5.65,5.07],'cal/(mol*K)'),
        H298 = (10.23,'kcal/mol'),
        S298 = (11.93,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1157,
    label        = "Ss-C=SCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U0 {2,S} {3,S}
2   Cd U0 {1,S} {4,D}
3   Cb U0 {1,S}
4   Sd U0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.08,5.5,5.68,5.7,5.59,5.42,5.05],'cal/(mol*K)'),
        H298 = (10.76,'kcal/mol'),
        S298 = (13.05,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1144,
    label        = "Ss-CtCt",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U0 {2,S} {3,S}
2   Ct U0 {1,S}
3   Ct U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.61,5.28,5.46,5.47,5.37,5.27,5.11],'cal/(mol*K)'),
        H298 = (19.93,'kcal/mol'),
        S298 = (13.38,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1145,
    label        = "Ss-CtCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U0 {2,S} {3,S}
2   Ct U0 {1,S}
3   Cb U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.6,5.94,5.94,5.82,5.56,5.35,5.06],'cal/(mol*K)'),
        H298 = (13.27,'kcal/mol'),
        S298 = (11.87,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1146,
    label        = "Ss-CbCb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U0 {2,S} {3,S}
2   Cb U0 {1,S}
3   Cb U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.27,5.7,5.8,5.74,5.53,5.35,5.09],'cal/(mol*K)'),
        H298 = (10.52,'kcal/mol'),
        S298 = (12.32,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1887,
    label        = "N",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * {N1d,N3s,N3d,N3t,N5s,N5d,N5dd,N5t} U0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1922,
    label        = "N1d",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N1d U0 L2
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1888,
    label        = "N3s",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3s U0 L1
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1938,
    label        = "N3s-CHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3s U0 {2,S} {3,S} {4,S}
2   C   U0 {1,S}
3   H   U0 {1,S}
4   H   U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1808,
    label        = "N3s-CsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3s U0 {2,S} {3,S} {4,S}
2   Cs  U0 {1,S}
3   H   U0 {1,S}
4   H   U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.72,6.51,7.32,8.07,9.41,10.47,12.28],'cal/(mol*K)'),
        H298 = (4.8,'kcal/mol'),
        S298 = (29.71,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1817,
    label        = "N3s-CbHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3s U0 {2,S} {3,S} {4,S}
2   Cb  U0 {1,S}
3   H   U0 {1,S}
4   H   U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.72,6.51,7.32,8.07,9.41,10.47,12.28],'cal/(mol*K)'),
        H298 = (4.8,'kcal/mol'),
        S298 = (29.71,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1825,
    label        = "N3s-(CO)HH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3s U0 {2,S} {3,S} {4,S}
2   CO  U0 {1,S}
3   H   U0 {1,S}
4   H   U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.07,5.74,7.13,8.29,9.96,11.22,14.37],'cal/(mol*K)'),
        H298 = (-14.9,'kcal/mol'),
        S298 = (-24.69,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1889,
    label        = "N3s-CdHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3s U0 {2,S} {3,S} {4,S}
2   Cd  U0 {1,S}
3   H   U0 {1,S}
4   H   U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.7,6.5,7.3,8.1,9.4,10.5,12.3],'cal/(mol*K)'),
        H298 = (4.8,'kcal/mol'),
        S298 = (29.7,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1938,
    label        = "N3s-CCH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3s U0 {2,S} {3,S} {4,S}
2   C   U0 {1,S}
3   C   U0 {1,S}
4   H   U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1809,
    label        = "N3s-CsCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3s U0 {2,S} {3,S} {4,S}
2   Cs  U0 {1,S}
3   Cs  U0 {1,S}
4   H   U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.2,5.21,6.13,6.83,7.9,8.65,9.55],'cal/(mol*K)'),
        H298 = (15.4,'kcal/mol'),
        S298 = (8.94,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1818,
    label        = "N3s-CbCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3s U0 {2,S} {3,S} {4,S}
2   Cb  U0 {1,S}
3   Cs  U0 {1,S}
4   H   U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (14.9,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1820,
    label        = "N3s-CbCbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3s U0 {2,S} {3,S} {4,S}
2   Cb  U0 {1,S}
3   Cb  U0 {1,S}
4   H   U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (16.3,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1826,
    label        = "N3s-(CO)CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3s U0 {2,S} {3,S} {4,S}
2   CO  U0 {1,S}
3   Cs  U0 {1,S}
4   H   U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (-4.4,'kcal/mol'),
        S298 = (3.9,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1828,
    label        = "N3s-(CO)CbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3s U0 {2,S} {3,S} {4,S}
2   CO  U0 {1,S}
3   Cb  U0 {1,S}
4   H   U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0.4,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1829,
    label        = "N3s-(CO)(CO)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3s U0 {2,S} {3,S} {4,S}
2   CO  U0 {1,S}
3   CO  U0 {1,S}
4   H   U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (-18.5,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1894,
    label        = "N3s-(CtN3t)CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3s U0 {2,S} {4,S} {5,S}
2   Ct  U0 {1,S} {3,T}
3   N3t U0 {2,T}
4   Cs  U0 {1,S}
5   H   U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.3,11.6,12.8,13.9,15.5,16.7,18.3],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (44.1,'kcal/mol','+|-',1.3),
        S298 = (40.7,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1899,
    label        = "N3s-(CdCd)CsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3s U0 {2,S} {5,S} {6,S}
2   Cd  U0 {1,S} {3,D} {4,S}
3   Cd  U0 {2,D}
4   R   U0 {2,S}
5   Cs  U0 {1,S}
6   H   U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.8,6.1,6.4,6.7,7.5,8.1,9.1],'cal/(mol*K)','+|-',[1.3,1.3,1.3,1.3,1.3,1.3,1.3]),
        H298 = (15.3,'kcal/mol','+|-',1.9),
        S298 = (8.7,'cal/(mol*K)','+|-',1.7),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1939,
    label        = "N3s-CCC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3s U0 {2,S} {3,S} {4,S}
2   C   U0 {1,S}
3   C   U0 {1,S}
4   C   U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1810,
    label        = "N3s-CsCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3s U0 {2,S} {3,S} {4,S}
2   Cs  U0 {1,S}
3   Cs  U0 {1,S}
4   Cs  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.48,4.56,5.43,5.97,6.56,6.67,6.5],'cal/(mol*K)'),
        H298 = (24.4,'kcal/mol'),
        S298 = (-13.46,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1819,
    label        = "N3s-CbCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3s U0 {2,S} {3,S} {4,S}
2   Cb  U0 {1,S}
3   Cs  U0 {1,S}
4   Cs  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (26.2,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1827,
    label        = "N3s-(CO)CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3s U0 {2,S} {3,S} {4,S}
2   CO  U0 {1,S}
3   Cs  U0 {1,S}
4   Cs  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1830,
    label        = "N3s-(CO)(CO)Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3s U0 {2,S} {3,S} {4,S}
2   CO  U0 {1,S}
3   CO  U0 {1,S}
4   Cs  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (-5.9,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1831,
    label        = "N3s-(CO)(CO)Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3s U0 {2,S} {3,S} {4,S}
2   CO  U0 {1,S}
3   CO  U0 {1,S}
4   Cb  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (-0.5,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1895,
    label        = "N3s-(CtN3t)CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3s U0 {2,S} {4,S} {5,S}
2   Ct  U0 {1,S} {3,T}
3   N3t U0 {2,T}
4   Cs  U0 {1,S}
5   Cs  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.6,9.6,10.5,11.4,12.9,13.8,14.8],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (53.3,'kcal/mol','+|-',1.3),
        S298 = (21,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1898,
    label        = "N3s-(CdCd)CsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3s U0 {2,S} {5,S} {6,S}
2   Cd  U0 {1,S} {3,D} {4,S}
3   Cd  U0 {2,D}
4   R   U0 {2,S}
5   Cs  U0 {1,S}
6   Cs  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.8,2.9,3.3,3.7,4.6,5,5.5],'cal/(mol*K)','+|-',[1.3,1.3,1.3,1.3,1.3,1.3,1.3]),
        H298 = (25.9,'kcal/mol','+|-',1.9),
        S298 = (-11,'cal/(mol*K)','+|-',1.7),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1811,
    label        = "N3s-N3sHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3s U0 {2,S} {3,S} {4,S}
2   H   U0 {1,S}
3   H   U0 {1,S}
4   N3s U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.1,7.38,8.43,9.27,10.54,11.52,13.19],'cal/(mol*K)'),
        H298 = (11.4,'kcal/mol'),
        S298 = (29.13,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1940,
    label        = "N3s-NCH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3s U0 {2,S} {3,S} {4,S}
2   N   U0 {1,S}
3   C   U0 {1,S}
4   H   U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1812,
    label        = "N3s-N3sCsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3s U0 {2,S} {3,S} {4,S}
2   Cs  U0 {1,S}
3   H   U0 {1,S}
4   N3s U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.82,5.8,6.5,7,7.8,8.3,9],'cal/(mol*K)'),
        H298 = (20.9,'kcal/mol'),
        S298 = (9.61,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1814,
    label        = "N3s-N3sCbH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3s U0 {2,S} {3,S} {4,S}
2   N3s U0 {1,S}
3   Cb  U0 {1,S}
4   H   U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (22.1,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1897,
    label        = "N3s-CsH(N3dOd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3s U0 {2,S} {3,S} {4,S}
2   Cs  U0 {1,S}
3   H   U0 {1,S}
4   N3d U0 {1,S} {5,D}
5   Od  U0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.4,11.9,13.4,14.7,16.6,17.9,19.2],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (25.2,'kcal/mol','+|-',1.3),
        S298 = (41.7,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1902,
    label        = "N3s-CsH(N5dOdOs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3s U0 {2,S} {3,S} {4,S}
2   Cs  U0 {1,S}
3   H   U0 {1,S}
4   N5d U0 {1,S} {5,D} {6,S}
5   Od  U0 {4,D}
6   Os  U0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.1,15.5,17.6,19.2,21.4,22.8,24.4],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (8.4,'kcal/mol','+|-',1.3),
        S298 = (45.3,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1901,
    label        = "N3s-(CdCd)HN3s",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3s U0 {2,S} {5,S} {6,S}
2   Cd  U0 {1,S} {3,D} {4,S}
3   Cd  U0 {2,D}
4   R   U0 {2,S}
5   H   U0 {1,S}
6   N3s U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.5,5.4,6.5,7.3,8.5,9.1,9.9],'cal/(mol*K)','+|-',[1.1,1.1,1.1,1.1,1.1,1.1,1.1]),
        H298 = (20.5,'kcal/mol','+|-',1.5),
        S298 = (6.6,'cal/(mol*K)','+|-',1.4),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1940,
    label        = "N3s-NCC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3s U0 {2,S} {3,S} {4,S}
2   N   U0 {1,S}
3   C   U0 {1,S}
4   C   U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1893,
    label        = "N3s-NCsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3s U0 {2,S} {3,S} {4,S}
2   N   U0 {1,S}
3   Cs  U0 {1,S}
4   Cs  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (29.2,'kcal/mol'),
        S298 = (-13.8,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1813,
    label        = "N3s-CsCsN3s",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3s U0 {2,S} {3,S} {4,S}
2   Cs  U0 {1,S}
3   Cs  U0 {1,S}
4   N3s U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.7,4.9,5.8,6.3,6.8,6.8,6.7],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (26.8,'kcal/mol','+|-',1.3),
        S298 = (-14.5,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1896,
    label        = "N3s-CsCs(N3dOd)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3s U0 {2,S} {3,S} {4,S}
2   Cs  U0 {1,S}
3   Cs  U0 {1,S}
4   N3d U0 {1,S} {5,D}
5   Od  U0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.4,10.5,11.5,12.4,13.8,14.6,15.3],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (32.6,'kcal/mol','+|-',1.3),
        S298 = (19.3,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1903,
    label        = "N3s-CsCs(N5dOdOs)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3s U0 {2,S} {3,S} {4,S}
2   Cs  U0 {1,S}
3   Cs  U0 {1,S}
4   N5d U0 {1,S} {5,D} {6,S}
5   Od  U0 {4,D}
6   Os  U0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.5,13.4,15.2,16.7,18.8,20,21.1],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (16.7,'kcal/mol','+|-',1.3),
        S298 = (25.8,'cal/(mol*K)','+|-',1.2),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1941,
    label        = "N3s-NCdCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3s U0 {2,S} {3,S} {4,S}
2   N   U0 {1,S}
3   Cd  U0 {1,S}
4   Cs  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1900,
    label        = "N3s-(CdCd)CsN3s",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3s U0 {2,S} {5,S} {6,S}
2   Cd  U0 {1,S} {3,D} {4,S}
3   Cd  U0 {2,D}
4   R   U0 {2,S}
5   Cs  U0 {1,S}
6   N3s U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.2,4.2,4.4,4.8,5.4,5.7,6],'cal/(mol*K)','+|-',[1.1,1.1,1.1,1.1,1.1,1.1,1.1]),
        H298 = (30.3,'kcal/mol','+|-',1.5),
        S298 = (-13.2,'cal/(mol*K)','+|-',1.4),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1891,
    label        = "N3s-CsHOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3s U0 {2,S} {3,S} {4,S}
2   Cs  U0 {1,S}
3   H   U0 {1,S}
4   Os  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.2,6.2,7,7.7,8.7,9.4,10.5],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (20.4,'kcal/mol','+|-',1.4),
        S298 = (8.1,'cal/(mol*K)','+|-',1.3),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1892,
    label        = "N3s-CsCsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3s U0 {2,S} {3,S} {4,S}
2   Cs  U0 {1,S}
3   Cs  U0 {1,S}
4   Os  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.3,5.1,5.7,6.2,7,7.3,7.5],'cal/(mol*K)','+|-',[0.8,0.8,0.8,0.8,0.8,0.8,0.8]),
        H298 = (26.6,'kcal/mol','+|-',1.2),
        S298 = (-12.7,'cal/(mol*K)','+|-',1.1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1890,
    label        = "N3s-OsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3s U0 {2,S} {3,S} {4,S}
2   Os  U0 {1,S}
3   H   U0 {1,S}
4   H   U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.1,7.4,8.4,9.3,10.5,11.5,13.2],'cal/(mol*K)'),
        H298 = (11.4,'kcal/mol'),
        S298 = (29.1,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1904,
    label        = "N3d",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3d U0
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1906,
    label        = "N3d-CdH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3d      U0 {2,D} {3,S}
2   {Cd,Cdd} U0 {1,D}
3   H        U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3,3.5,3.9,4.3,5,5.5,6.4],'cal/(mol*K)'),
        H298 = (16.3,'kcal/mol'),
        S298 = (13.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1815,
    label        = "N3d-N3dH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3d U0 {2,S} {3,D}
2   H   U0 {1,S}
3   N3d U0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.38,4.89,5.44,5.94,6.77,7.42,8.44],'cal/(mol*K)'),
        H298 = (25.1,'kcal/mol'),
        S298 = (26.8,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1822,
    label        = "N3d-N3dN3s",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3d U0 {2,D} {3,S}
2   N3d U0 {1,D}
3   N3s U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (23,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1909,
    label        = "N3d-OdOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3d U0 {2,D} {3,S}
2   Od  U0 {1,D}
3   Os  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1910,
    label        = "N3d-OdN3s",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3d U0 {2,D} {3,S}
2   Od  U0 {1,D}
3   N3s U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1911,
    label        = "N3d-CsR",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3d U0 {2,S} {3,D}
2   Cs  U0 {1,S}
3   R!H U0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (21.3,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1908,
    label        = "N3d-OdC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3d U0 {2,D} {3,S}
2   Od  U0 {1,D}
3   C   U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1905,
    label        = "N3d-CdCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3d      U0 {2,D} {3,S}
2   {Cd,Cdd} U0 {1,D}
3   Cs       U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2,2.2,2.2,2.3,2.5,2.7,2.9],'cal/(mol*K)'),
        H298 = (21.3,'kcal/mol'),
        S298 = (-6.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1907,
    label        = "N3d-N3dCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3d U0 {2,D} {3,S}
2   N3d U0 {1,D}
3   Cs  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([3.4,3.6,3.7,3.9,4.3,4.6,4.9],'cal/(mol*K)'),
        H298 = (27,'kcal/mol'),
        S298 = (7.2,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1912,
    label        = "N3d-CbR",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N3d U0 {2,S} {3,D}
2   Cb  U0 {1,S}
3   R!H U0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (16.7,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1913,
    label        = "N5d",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N5d U0
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1914,
    label        = "N5d-OdOsCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N5d U0 {2,D} {3,S} {4,S}
2   Od  U0 {1,D}
3   Os  U0 {1,S}
4   Cs  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1915,
    label        = "N5d-OdOsCd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N5d U0 {2,D} {3,S} {4,S}
2   Od  U0 {1,D}
3   Os  U0 {1,S}
4   Cd  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1916,
    label        = "N5d-OdOsOs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N5d U0 {2,D} {3,S} {4,S}
2   Od  U0 {1,D}
3   Os  U0 {1,S}
4   Os  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1917,
    label        = "N5d-OdOsN3s",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N5d U0 {2,D} {3,S} {4,S}
2   Od  U0 {1,D}
3   Os  U0 {1,S}
4   N3s U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1918,
    label        = "N5dd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * N5dd U0
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
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
            L4: Cb-Ss
            L4: Cb-C
                L5: Cb-Cs
                L5: Cb-Cds
                    L6: Cb-(Cds-Od)
                    L6: Cb-(Cds-Cd)
                        L7: Cb-(Cds-Cds)
                        L7: Cb-(Cds-Cdd)
                            L8: Cb-(Cds-Cdd-Od)
                            L8: Cb-(Cds-Cdd-Sd)
                            L8: Cb-(Cds-Cdd-Cd)
                    L6: Cb-C=S
                L5: Cb-Ct
                    L6: Cb-(CtN3t)
                L5: Cb-Cb
                    L6: Cb-CbCbN3s
        L3: Ct
            L4: Ct-CtN3s
            L4: Ct-N3tN3s
            L4: Ct-CtH
            L4: Ct-CtOs
            L4: Ct-N3tOs
            L4: Ct-CtSs
            L4: Ct-N3tC
                L5: Ct-N3tCs
                L5: Ct-N3tCd
            L4: Ct-CtC
                L5: Ct-CtCs
                L5: Ct-CtCds
                    L6: Ct-Ct(Cds-Od)
                    L6: Ct-Ct(Cds-Cd)
                        L7: Ct-Ct(Cds-Cds)
                        L7: Ct-Ct(Cds-Cdd)
                            L8: Ct-Ct(Cds-Cdd-Od)
                            L8: Ct-Ct(Cds-Cdd-Sd)
                            L8: Ct-Ct(Cds-Cdd-Cd)
                    L6: Ct-CtC=S
                L5: Ct-CtCt
                    L6: Ct-Ct(CtN3t)
                L5: Ct-CtCb
        L3: Cdd
            L4: Cdd-N3dCd
            L4: Cdd-OdOd
            L4: Cdd-SdSd
            L4: Cdd-CdOd
                L5: Cdd-CdsOd
                L5: Cdd-CddOd
                    L6: Cdd-(Cdd-Od)Od
                    L6: Cdd-(Cdd-Cd)Od
            L4: Cdd-CdSd
                L5: Cdd-CdsSd
                L5: Cdd-CddSd
                    L6: Cdd-(Cdd-Sd)Sd
                    L6: Cdd-(Cdd-Cd)Sd
            L4: Cdd-CdCd
                L5: Cdd-CddCdd
                    L6: Cdd-(Cdd-Od)(Cdd-Od)
                    L6: Cdd-(Cdd-Sd)(Cdd-Sd)
                    L6: Cdd-(Cdd-Od)(Cdd-Cd)
                    L6: Cdd-(Cdd-Sd)(Cdd-Cd)
                    L6: Cdd-(Cdd-Cd)(Cdd-Cd)
                L5: Cdd-CddCds
                    L6: Cdd-(Cdd-Od)Cds
                    L6: Cdd-(Cdd-Sd)Cds
                    L6: Cdd-(Cdd-Cd)Cds
                L5: Cdd-CdsCds
        L3: Cds
            L4: Cds-OdN3sH
            L4: Cds-OdN3sCs
            L4: Cd-N3dCsCs
            L4: Cd-N3dCsH
            L4: Cd-N3dHH
            L4: Cds-OdHH
            L4: Cds-OdOsH
            L4: CO-SsH
            L4: Cds-OdOsOs
            L4: CO-CsSs
            L4: C=S-HH
            L4: C=S-SsH
            L4: CS-OsH
            L4: C=S-SsSs
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
            L4: C=S-CH
                L5: C=S-CsH
                L5: C=S-CdsH
                    L6: C=S-(Cds-Cd)H
                        L7: C=S-(Cds-Cds)H
                        L7: C=S-(Cds-Cdd)H
                            L8: C=S-(Cds-Cdd-Sd)H
                            L8: C=S-(Cds-Cdd-Cd)H
                    L6: C=S-C=SH
                L5: C=S-CtH
                L5: C=S-CbH
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
            L4: C=S-CSs
                L5: C=S-CsSs
                L5: C=S-CdsSs
                    L6: C=S-(Cds-Cd)Ss
                        L7: C=S-(Cds-Cds)Ss
                        L7: C=S-(Cds-Cdd)Ss
                            L8: C=S-(Cds-Cdd-Sd)Ss
                            L8: C=S-(Cds-Cdd-Cd)Ss
                    L6: C=S-C=SSs
                L5: C=S-CtSs
                L5: C=S-CbSs
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
            L4: C=S-CC
                L5: C=S-CsCs
                L5: C=S-CdsCs
                    L6: C=S-(Cds-Cd)Cs
                        L7: C=S-(Cds-Cds)Cs
                        L7: C=S-(Cds-Cdd)Cs
                            L8: C=S-(Cds-Cdd-Sd)Cs
                            L8: C=S-(Cds-Cdd-Cd)Cs
                    L6: C=S-C=SCs
                L5: C=S-CdsCds
                    L6: C=S-(Cds-Cd)(Cds-Cd)
                        L7: C=S-(Cds-Cds)(Cds-Cds)
                        L7: C=S-(Cds-Cdd)(Cds-Cds)
                            L8: C=S-(Cds-Cdd-Sd)(Cds-Cds)
                            L8: C=S-(Cds-Cdd-Cd)(Cds-Cds)
                        L7: C=S-(Cds-Cdd)(Cds-Cdd)
                            L8: C=S-(Cds-Cdd-Sd)(Cds-Cdd-Sd)
                            L8: C=S-(Cds-Cdd-Cd)(Cds-Cdd-Sd)
                            L8: C=S-(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                    L6: C=S-(Cds-Cd)C=S
                        L7: C=S-(Cds-Cds)C=S
                        L7: C=S-(Cds-Cdd)C=S
                            L8: C=S-(Cds-Cdd-Sd)C=S
                            L8: C=S-(Cds-Cdd-Cd)C=S
                    L6: C=S-C=SC=S
                L5: C=S-CtCs
                L5: C=S-CtCds
                    L6: C=S-Ct(Cds-Cd)
                        L7: C=S-Ct(Cds-Cds)
                        L7: C=S-Ct(Cds-Cdd)
                            L8: C=S-Ct(Cds-Cdd-Sd)
                            L8: C=S-Ct(Cds-Cdd-Cd)
                    L6: C=S-CtC=S
                L5: C=S-CtCt
                L5: C=S-CbCs
                L5: C=S-CbCds
                    L6: C=S-Cb(Cds-Cd)
                        L7: C=S-Cb(Cds-Cds)
                        L7: C=S-Cb(Cds-Cdd)
                            L8: C=S-Cb(Cds-Cdd-Sd)
                            L8: C=S-Cb(Cds-Cdd-Cd)
                    L6: C=S-CbC=S
                L5: C=S-CbCt
                L5: C=S-CbCb
            L4: CS-CsOs
            L4: Cds-CdHH
                L5: Cds-CdsHH
                L5: Cds-CddHH
                    L6: Cds-(Cdd-Od)HH
                    L6: Cds-(Cdd-Sd)HH
                    L6: Cds-(Cdd-Cd)HH
            L4: Cds-CdOsH
                L5: Cds-CdsOsH
                L5: Cds-CddOsH
                    L6: Cds-(Cdd-Od)OsH
                    L6: Cds-(Cdd-Cd)OsH
            L4: Cds-CdSsH
                L5: Cds-CdsSsH
                L5: Cds-CddSsH
                    L6: Cds-(Cdd-Sd)SsH
                    L6: Cds-(Cdd-Cd)SsH
            L4: Cds-CdOsOs
                L5: Cds-CdsOsOs
                L5: Cds-CddOsOs
                    L6: Cds-(Cdd-Od)OsOs
                    L6: Cds-(Cdd-Cd)OsOs
            L4: Cds-CdSsSs
                L5: Cds-CdsSsSs
                L5: Cds-CddSsSs
                    L6: Cds-(Cdd-Sd)SsSs
                    L6: Cds-(Cdd-Cd)SsSs
            L4: Cds-CdCH
                L5: Cds-CdsCsH
                L5: Cds-CdsCdsH
                    L6: Cds-Cds(Cds-Od)H
                    L6: Cds-Cds(Cds-Cd)H
                        L7: Cds-Cds(Cds-Cds)H
                        L7: Cds-Cds(Cds-Cdd)H
                            L8: Cds-Cds(Cds-Cdd-Od)H
                            L8: Cds-Cds(Cds-Cdd-Sd)H
                            L8: Cds-Cds(Cds-Cdd-Cd)H
                    L6: Cds-CdsC=SH
                L5: Cds-CdsCtH
                    L6: Cds-CdsH(CtN3t)
                L5: Cds-CdsCbH
                L5: Cds-CddCsH
                    L6: Cds-(Cdd-Od)CsH
                    L6: Cds-(Cdd-Sd)CsH
                    L6: Cds-(Cdd-Cd)CsH
                L5: Cds-CddCdsH
                    L6: Cds-(Cdd-Od)(Cds-Od)H
                    L6: Cds-(Cdd-Od)(Cds-Cd)H
                        L7: Cds-(Cdd-Od)(Cds-Cds)H
                        L7: Cds-(Cdd-Od)(Cds-Cdd)H
                            L8: Cds-(Cdd-Od)(Cds-Cdd-Od)H
                            L8: Cds-(Cdd-Od)(Cds-Cdd-Cd)H
                    L6: Cds-(Cdd-Sd)(Cds-Cd)H
                        L7: Cds-(Cdd-Sd)(Cds-Cds)H
                        L7: Cds-(Cdd-Sd)(Cds-Cdd)H
                            L8: Cds-(Cdd-Sd)(Cds-Cdd-Sd)H
                            L8: Cds-(Cdd-Sd)(Cds-Cdd-Cd)H
                    L6: Cds-(Cdd-Cd)(Cds-Od)H
                    L6: Cds-(Cdd-Cd)(Cds-Cd)H
                        L7: Cds-(Cdd-Cd)(Cds-Cds)H
                        L7: Cds-(Cdd-Cd)(Cds-Cdd)H
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Od)H
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Sd)H
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Cd)H
                    L6: Cds-(Cdd-Sd)C=SH
                    L6: Cds-(Cdd-Cd)C=SH
                L5: Cds-CddCtH
                    L6: Cds-(Cdd-Od)CtH
                    L6: Cds-(Cdd-Sd)CtH
                    L6: Cds-(Cdd-Cd)CtH
                L5: Cds-CddCbH
                    L6: Cds-(Cdd-Od)CbH
                    L6: Cds-(Cdd-Sd)CbH
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
            L4: Cds-CdCS
                L5: Cds-CdsCsSs
                L5: Cds-CdsCdsSs
                    L6: Cds-Cds(Cds-Cd)Ss
                        L7: Cds-Cds(Cds-Cds)Ss
                        L7: Cds-Cds(Cds-Cdd)Ss
                            L8: Cds-Cds(Cds-Cdd-Sd)Ss
                            L8: Cds-Cds(Cds-Cdd-Cd)Ss
                    L6: Cds-CdsC=SSs
                L5: Cds-CdsCtSs
                L5: Cds-CdsCbSs
                L5: Cds-CddCsSs
                    L6: Cds-(Cdd-Sd)CsSs
                    L6: Cds-(Cdd-Cd)CsSs
                L5: Cds-CddCdsSs
                    L6: Cds-(Cdd-Sd)(Cds-Cd)Ss
                        L7: Cds-(Cdd-Sd)(Cds-Cds)Ss
                        L7: Cds-(Cdd-Sd)(Cds-Cdd)Ss
                            L8: Cds-(Cdd-Sd)(Cds-Cdd-Sd)Ss
                            L8: Cds-(Cdd-Sd)(Cds-Cdd-Cd)Ss
                    L6: Cds-(Cdd-Cd)(Cds-Cd)Ss
                        L7: Cds-(Cdd-Cd)(Cds-Cds)Ss
                        L7: Cds-(Cdd-Cd)(Cds-Cdd)Ss
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Sd)Ss
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Cd)Ss
                    L6: Cds-(Cdd-Sd)C=SSs
                L5: Cds-CddCtSs
                    L6: Cds-(Cdd-Sd)CtSs
                    L6: Cds-(Cdd-Cd)CtSs
                L5: Cds-CddCbSs
                    L6: Cds-(Cdd-Sd)CbSs
                    L6: Cds-(Cdd-Cd)CbSs
            L4: Cds-CdCC
                L5: Cds-CdsCsCs
                L5: Cds-CdsCdsCs
                    L6: Cds-Cds(Cds-Od)Cs
                    L6: Cds-Cds(Cds-Cd)Cs
                        L7: Cds-Cds(Cds-Cds)Cs
                        L7: Cds-Cds(Cds-Cdd)Cs
                            L8: Cds-Cds(Cds-Cdd-Od)Cs
                            L8: Cds-Cds(Cds-Cdd-Sd)Cs
                            L8: Cds-Cds(Cds-Cdd-Cd)Cs
                    L6: Cds-CdsC=SCs
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
                            L8: Cds-Cds(Cds-Cds)(Cds-Cdd-Sd)
                            L8: Cds-Cds(Cds-Cds)(Cds-Cdd-Cd)
                        L7: Cds-Cds(Cds-Cdd)(Cds-Cdd)
                            L8: Cds-Cds(Cds-Cdd-Od)(Cds-Cdd-Od)
                            L8: Cds-Cds(Cds-Cdd-Od)(Cds-Cdd-Cd)
                            L8: Cds-Cds(Cds-Cdd-Sd)(Cds-Cdd-Sd)
                            L8: Cds-Cds(Cds-Cdd-Sd)(Cds-Cdd-Cd)
                            L8: Cds-Cds(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                    L6: Cds-CdsC=S(Cds-Cd)
                        L7: Cds-CdsC=S(Cds-Cds)
                        L7: Cds-CdsC=S(Cds-Cdd)
                            L8: Cds-CdsC=S(Cds-Cdd-Sd)
                            L8: Cds-CdsC=S(Cds-Cdd-Cd)
                    L6: Cds-CdsC=SC=S
                L5: Cds-CdsCtCs
                    L6: Cd-CdCs(CtN3t)
                L5: Cds-CdsCtCds
                    L6: Cds-CdsCt(Cds-Od)
                    L6: Cds-CdsCt(Cds-Cd)
                        L7: Cds-Cds(Cds-Cds)Ct
                        L7: Cds-Cds(Cds-Cdd)Ct
                            L8: Cds-Cds(Cds-Cdd-Od)Ct
                            L8: Cds-Cds(Cds-Cdd-Sd)Ct
                            L8: Cds-Cds(Cds-Cdd-Cd)Ct
                    L6: Cds-CdsCtC=S
                L5: Cds-CdsCtCt
                    L6: Cds-Cd(CtN3t)(CtN3t)
                L5: Cds-CdsCbCs
                L5: Cds-CdsCbCds
                    L6: Cds-CdsCb(Cds-Od)
                    L6: Cds-Cds(Cds-Cd)Cb
                        L7: Cds-Cds(Cds-Cds)Cb
                        L7: Cds-Cds(Cds-Cdd)Cb
                            L8: Cds-Cds(Cds-Cdd-Od)Cb
                            L8: Cds-Cds(Cds-Cdd-Sd)Cb
                            L8: Cds-Cds(Cds-Cdd-Cd)Cb
                    L6: Cds-CdsCbC=S
                L5: Cds-CdsCbCt
                L5: Cds-CdsCbCb
                L5: Cds-CddCsCs
                    L6: Cds-(Cdd-Od)CsCs
                    L6: Cds-(Cdd-Sd)CsCs
                    L6: Cds-(Cdd-Cd)CsCs
                L5: Cds-CddCdsCs
                    L6: Cds-(Cdd-Od)(Cds-Od)Cs
                    L6: Cds-(Cdd-Od)(Cds-Cd)Cs
                        L7: Cds-(Cdd-Od)(Cds-Cds)Cs
                        L7: Cds-(Cdd-Od)(Cds-Cdd)Cs
                            L8: Cds-(Cdd-Od)(Cds-Cdd-Od)Cs
                            L8: Cds-(Cdd-Od)(Cds-Cdd-Cd)Cs
                    L6: Cds-(Cdd-Sd)(Cds-Cd)Cs
                        L7: Cds-(Cdd-Sd)(Cds-Cds)Cs
                        L7: Cds-(Cdd-Sd)(Cds-Cdd)Cs
                            L8: Cds-(Cdd-Sd)(Cds-Cdd-Sd)Cs
                            L8: Cds-(Cdd-Sd)(Cds-Cdd-Cd)Cs
                    L6: Cds-(Cdd-Cd)(Cds-Cd)Cs
                        L7: Cds-(Cdd-Cd)(Cds-Cds)Cs
                        L7: Cds-(Cdd-Cd)(Cds-Cdd)Cs
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Od)Cs
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Sd)Cs
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Cd)Cs
                    L6: Cds-(Cdd-Sd)C=SCs
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
                    L6: Cds-(Cdd-Sd)(Cds-Cd)(Cds-Cd)
                        L7: Cds-(Cdd-Sd)(Cds-Cds)(Cds-Cds)
                        L7: Cds-(Cdd-Sd)(Cds-Cdd)(Cds-Cds)
                            L8: Cds-(Cdd-Sd)(Cds-Cdd-Sd)(Cds-Cds)
                            L8: Cds-(Cdd-Sd)(Cds-Cdd-Cd)(Cds-Cds)
                        L7: Cds-(Cdd-Sd)(Cds-Cdd)(Cds-Cdd)
                            L8: Cds-(Cdd-Sd)(Cds-Cdd-Sd)(Cds-Cdd-Sd)
                            L8: Cds-(Cdd-Sd)(Cds-Cdd-Sd)(Cds-Cdd-Cd)
                            L8: Cds-(Cdd-Sd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                    L6: Cds-(Cdd-Cd)(Cds-Cd)(Cds-Cd)
                        L7: Cds-(Cdd-Cd)(Cds-Cds)(Cds-Cds)
                        L7: Cds-(Cdd-Cd)(Cds-Cdd)(Cds-Cds)
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Od)(Cds-Cds)
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Sd)(Cds-Cds)
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cds)
                        L7: Cds-(Cdd-Cd)(Cds-Cdd)(Cds-Cdd)
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Od)(Cds-Cdd-Od)
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Od)(Cds-Cdd-Cd)
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Sd)(Cds-Cdd-Sd)
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Sd)(Cds-Cdd-Cd)
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                    L6: Cds-(Cdd-Sd)(Cds-Cd)C=S
                        L7: Cds-(Cdd-Sd)(Cds-Cds)C=S
                        L7: Cds-(Cdd-Sd)(Cds-Cdd)C=S
                            L8: Cds-(Cdd-Sd)(Cds-Cdd-Sd)C=S
                            L8: Cds-(Cdd-Sd)(Cds-Cdd-Cd)C=S
                    L6: Cds-(Cdd-Cd)C=S(Cds-Cd)
                        L7: Cds-(Cdd-Cd)C=S(Cds-Cds)
                        L7: Cds-(Cdd-Cd)C=S(Cds-Cdd)
                            L8: Cds-(Cdd-Cd)C=S(Cds-Cdd-Sd)
                            L8: Cds-(Cdd-Cd)C=S(Cds-Cdd-Cd)
                    L6: Cds-(Cdd-Sd)C=SC=S
                    L6: Cds-(Cdd-Cd)C=SC=S
                L5: Cds-CddCtCs
                    L6: Cds-(Cdd-Od)CtCs
                    L6: Cds-(Cdd-Sd)CtCs
                    L6: Cds-(Cdd-Cd)CtCs
                L5: Cds-CddCtCds
                    L6: Cds-(Cdd-Od)(Cds-Od)Ct
                    L6: Cds-(Cdd-Od)(Cds-Cd)Ct
                        L7: Cds-(Cdd-Od)(Cds-Cds)Ct
                        L7: Cds-(Cdd-Od)(Cds-Cdd)Ct
                            L8: Cds-(Cdd-Od)(Cds-Cdd-Od)Ct
                            L8: Cds-(Cdd-Od)(Cds-Cdd-Cd)Ct
                    L6: Cds-(Cdd-Sd)(Cds-Cd)Ct
                        L7: Cds-(Cdd-Sd)(Cds-Cds)Ct
                        L7: Cds-(Cdd-Sd)(Cds-Cdd)Ct
                            L8: Cds-(Cdd-Sd)(Cds-Cdd-Sd)Ct
                            L8: Cds-(Cdd-Sd)(Cds-Cdd-Cd)Ct
                    L6: Cds-(Cdd-Cd)(Cds-Cd)Ct
                        L7: Cds-(Cdd-Cd)(Cds-Cds)Ct
                        L7: Cds-(Cdd-Cd)(Cds-Cdd)Ct
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Od)Ct
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Sd)Ct
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Cd)Ct
                    L6: Cds-(Cdd-Sd)C=SCt
                L5: Cds-CddCtCt
                    L6: Cds-(Cdd-Od)CtCt
                    L6: Cds-(Cdd-Sd)CtCt
                    L6: Cds-(Cdd-Cd)CtCt
                L5: Cds-CddCbCs
                    L6: Cds-(Cdd-Od)CbCs
                    L6: Cds-(Cdd-Sd)CbCs
                    L6: Cds-(Cdd-Cd)CbCs
                L5: Cds-CddCbCds
                    L6: Cds-(Cdd-Od)(Cds-Od)Cb
                    L6: Cds-(Cdd-Od)(Cds-Cd)Cb
                        L7: Cds-(Cdd-Od)(Cds-Cds)Cb
                        L7: Cds-(Cdd-Od)(Cds-Cdd)Cb
                            L8: Cds-(Cdd-Od)(Cds-Cdd-Od)Cb
                            L8: Cds-(Cdd-Od)(Cds-Cdd-Cd)Cb
                    L6: Cds-(Cdd-Sd)(Cds-Cd)Cb
                        L7: Cds-(Cdd-Sd)(Cds-Cds)Cb
                        L7: Cds-(Cdd-Sd)(Cds-Cdd)Cb
                            L8: Cds-(Cdd-Sd)(Cds-Cdd-Sd)Cb
                            L8: Cds-(Cdd-Sd)(Cds-Cdd-Cd)Cb
                    L6: Cds-(Cdd-Cd)(Cds-Cd)Cb
                        L7: Cds-(Cdd-Cd)(Cds-Cds)Cb
                        L7: Cds-(Cdd-Cd)(Cds-Cdd)Cb
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Od)Cb
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Sd)Cb
                            L8: Cds-(Cdd-Cd)(Cds-Cdd-Cd)Cb
                    L6: Cds-(Cdd-Sd)C=SCb
                L5: Cds-CddCbCt
                    L6: Cds-(Cdd-Od)CbCt
                    L6: Cds-(Cdd-Sd)CbCt
                    L6: Cds-(Cdd-Cd)CbCt
                L5: Cds-CddCbCb
                    L6: Cds-(Cdd-Od)CbCb
                    L6: Cds-(Cdd-Sd)CbCb
                    L6: Cds-(Cdd-Cd)CbCb
            L4: Cds-CNH
                L5: Cd-CdHN3s
                L5: Cd-CdH(N5dOdOs)
            L4: Cds-CCN
                L5: Cd-CdCsN3s
                L5: Cd-CdCs(N5dOdOs)
        L3: Cs
            L4: Cs-NHHH
                L5: Cs-N3sHHH
                L5: Cs-N3dHHH
                    L6: Cs-(N3dCd)HHH
                    L6: Cs-(N3dN3d)HHH
            L4: Cs-NCsHH
                L5: Cs-N3sCsHH
                L5: Cs-N3dCHH
                    L6: Cs-(N3dN3d)CsHH
                    L6: Cs-(N3dOd)CHH
                    L6: Cs-(N3dCd)CsHH
                L5: Cs-N5dCsHH
                    L6: Cs-(N5dOdOs)CsHH
            L4: Cs-NCsCsH
                L5: Cs-N3sCsCsH
                L5: Cs-N3dCsCsH
                    L6: Cs-(N3dN3d)CsCsH
                    L6: Cs-(N3dOd)CsCsH
                L5: Cs-N5dCsCsH
                    L6: Cs-(N5dOdOs)CsCsH
            L4: Cs-NCsCsCs
                L5: Cs-N3sCsCsCs
                L5: Cs-N3dCsCsCs
                    L6: Cs-(N3dN3d)CsCsCs
                    L6: Cs-(N3dOd)CsCsCs
                L5: Cs-N5dCsCsCs
                    L6: Cs-(N5dOdOs)CsCsCs
            L4: Cs-NNCsH
                L5: Cs-N5dN5dCsH
                    L6: Cs-(N5dOdOs)(N5dOdOs)CsH
            L4: Cs-HHHH
            L4: Cs-CHHH
                L5: Cs-CsHHH
                L5: Cs-CdsHHH
                    L6: Cs-(Cds-Od)HHH
                    L6: Cs-(Cds-Cd)HHH
                        L7: Cs-(CdN3d)HHH
                        L7: Cs-(Cds-Cds)HHH
                        L7: Cs-(Cds-Cdd)HHH
                            L8: Cs-(Cds-Cdd-Od)HHH
                            L8: Cs-(Cds-Cdd-Sd)HHH
                            L8: Cs-(Cds-Cdd-Cd)HHH
                    L6: Cs-C=SHHH
                L5: Cs-CtHHH
                    L6: Cs-(CtN3t)HHH
                L5: Cs-CbHHH
            L4: Cs-OsHHH
            L4: Cs-OsOsHH
            L4: Cs-OsOsOsH
            L4: Cs-OsSsHH
            L4: Cs-OsOsSsH
            L4: Cs-SsHHH
            L4: Cs-SsSsHH
            L4: Cs-SsSsSsH
            L4: Cs-CCHH
                L5: Cs-CsCsHH
                L5: Cs-CdsCsHH
                    L6: Cs-(Cds-Od)CsHH
                    L6: Cs-(Cds-Cd)CsHH
                        L7: Cs-(Cds-Cds)CsHH
                        L7: Cs-(Cds-Cdd)CsHH
                            L8: Cs-(Cds-Cdd-Od)CsHH
                            L8: Cs-(Cds-Cdd-Sd)CsHH
                            L8: Cs-(Cds-Cdd-Cd)CsHH
                        L7: Cs-(CdN3d)CsHH
                    L6: Cs-C=SCsHH
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
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cds)HH
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)HH
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)HH
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)HH
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)HH
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)HH
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Cd)HH
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)HH
                    L6: Cs-C=S(Cds-Cd)HH
                        L7: Cs-C=S(Cds-Cds)HH
                        L7: Cs-C=S(Cds-Cdd)HH
                            L8: Cs-C=S(Cds-Cdd-Sd)HH
                            L8: Cs-C=S(Cds-Cdd-Cd)HH
                    L6: Cs-C=SC=SHH
                L5: Cs-CtCsHH
                    L6: Cs-(CtN3t)CsHH
                L5: Cs-CtCdsHH
                    L6: Cs-(Cds-Od)CtHH
                    L6: Cs-(Cds-Cd)CtHH
                        L7: Cs-(Cds-Cds)CtHH
                        L7: Cs-(Cds-Cdd)CtHH
                            L8: Cs-(Cds-Cdd-Od)CtHH
                            L8: Cs-(Cds-Cdd-Sd)CtHH
                            L8: Cs-(Cds-Cdd-Cd)CtHH
                    L6: Cs-C=SCtHH
                L5: Cs-CtCtHH
                L5: Cs-CbCsHH
                L5: Cs-CbCdsHH
                    L6: Cs-(Cds-Od)CbHH
                    L6: Cs-(Cds-Cd)CbHH
                        L7: Cs-(Cds-Cds)CbHH
                        L7: Cs-(Cds-Cdd)CbHH
                            L8: Cs-(Cds-Cdd-Od)CbHH
                            L8: Cs-(Cds-Cdd-Sd)CbHH
                            L8: Cs-(Cds-Cdd-Cd)CbHH
                    L6: Cs-C=SCbHH
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
                            L8: Cs-(Cds-Cdd-Sd)CsCsH
                            L8: Cs-(Cds-Cdd-Cd)CsCsH
                        L7: Cs-(CdN3d)CsCsH
                    L6: Cs-C=SCsCsH
                L5: Cs-CtCsCsH
                    L6: Cs-(CtN3t)CsCsH
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
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cds)CsH
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CsH
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CsH
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CsH
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)CsH
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)CsH
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Cd)CsH
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CsH
                    L6: Cs-C=S(Cds-Cd)CsH
                        L7: Cs-C=S(Cds-Cds)CsH
                        L7: Cs-C=S(Cds-Cdd)CsH
                            L8: Cs-C=S(Cds-Cdd-Sd)CsH
                            L8: Cs-C=S(Cds-Cdd-Cd)CsH
                    L6: Cs-C=SC=SCsH
                L5: Cs-CtCdsCsH
                    L6: Cs-(Cds-Od)CtCsH
                    L6: Cs-(Cds-Cd)CtCsH
                        L7: Cs-(Cds-Cds)CtCsH
                        L7: Cs-(Cds-Cdd)CtCsH
                            L8: Cs-(Cds-Cdd-Od)CtCsH
                            L8: Cs-(Cds-Cdd-Sd)CtCsH
                            L8: Cs-(Cds-Cdd-Cd)CtCsH
                    L6: Cs-C=SCtCsH
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
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Sd)H
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)H
                        L7: Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)H
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)H
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Cd)H
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Sd)(Cds-Cdd-Sd)H
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Sd)(Cds-Cdd-Cd)H
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)H
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)H
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)H
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)(Cds-Cdd-Sd)H
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)(Cds-Cdd-Cd)H
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)H
                    L6: Cs-C=S(Cds-Cd)(Cds-Cd)H
                        L7: Cs-C=S(Cds-Cds)(Cds-Cds)H
                        L7: Cs-C=S(Cds-Cdd)(Cds-Cds)H
                            L8: Cs-C=S(Cds-Cdd-Sd)(Cds-Cds)H
                            L8: Cs-C=S(Cds-Cdd-Cd)(Cds-Cds)H
                        L7: Cs-C=S(Cds-Cdd)(Cds-Cdd)H
                            L8: Cs-C=S(Cds-Cdd-Sd)(Cds-Cdd-Sd)H
                            L8: Cs-C=S(Cds-Cdd-Sd)(Cds-Cdd-Cd)H
                            L8: Cs-C=S(Cds-Cdd-Cd)(Cds-Cdd-Cd)H
                    L6: Cs-C=SC=S(Cds-Cd)H
                        L7: Cs-C=SC=S(Cds-Cds)H
                        L7: Cs-C=SC=S(Cds-Cdd)H
                            L8: Cs-C=SC=S(Cds-Cdd-Sd)H
                            L8: Cs-C=SC=S(Cds-Cdd-Cd)H
                    L6: Cs-C=SC=SC=SH
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
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cds)CtH
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CtH
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CtH
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CtH
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)CtH
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)CtH
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Cd)CtH
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtH
                    L6: Cs-C=S(Cds-Cd)CtH
                        L7: Cs-C=S(Cds-Cds)CtH
                        L7: Cs-C=S(Cds-Cdd)CtH
                            L8: Cs-C=S(Cds-Cdd-Sd)CtH
                            L8: Cs-C=S(Cds-Cdd-Cd)CtH
                    L6: Cs-C=SC=SCtH
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
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cds)CbH
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CbH
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CbH
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CbH
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)CbH
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)CbH
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Cd)CbH
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbH
                    L6: Cs-C=S(Cds-Cd)CbH
                        L7: Cs-C=S(Cds-Cds)CbH
                        L7: Cs-C=S(Cds-Cdd)CbH
                            L8: Cs-C=S(Cds-Cdd-Sd)CbH
                            L8: Cs-C=S(Cds-Cdd-Cd)CbH
                    L6: Cs-C=SC=SCbH
                L5: Cs-CtCtCdsH
                    L6: Cs-CtCt(Cds-Od)H
                    L6: Cs-CtCt(Cds-Cd)H
                        L7: Cs-CtCt(Cds-Cds)H
                        L7: Cs-CtCt(Cds-Cdd)H
                            L8: Cs-CtCt(Cds-Cdd-Od)H
                            L8: Cs-CtCt(Cds-Cdd-Sd)H
                            L8: Cs-CtCt(Cds-Cdd-Cd)H
                    L6: Cs-CtCtC=SH
                L5: Cs-CbCtCdsH
                    L6: Cs-CbCt(Cds-Od)H
                    L6: Cs-CbCt(Cds-Cd)H
                        L7: Cs-CbCt(Cds-Cds)H
                        L7: Cs-CbCt(Cds-Cdd)H
                            L8: Cs-CbCt(Cds-Cdd-Od)H
                            L8: Cs-CbCt(Cds-Cdd-Sd)H
                            L8: Cs-CbCt(Cds-Cdd-Cd)H
                    L6: Cs-CbCtC=SH
                L5: Cs-CbCbCdsH
                    L6: Cs-CbCb(Cds-Od)H
                    L6: Cs-CbCb(Cds-Cd)H
                        L7: Cs-CbCb(Cds-Cds)H
                        L7: Cs-CbCb(Cds-Cdd)H
                            L8: Cs-CbCb(Cds-Cdd-Od)H
                            L8: Cs-CbCb(Cds-Cdd-Sd)H
                            L8: Cs-CbCb(Cds-Cdd-Cd)H
                    L6: Cs-CbCbC=SH
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
                            L8: Cs-(Cds-Cdd-Sd)CsCsCs
                            L8: Cs-(Cds-Cdd-Cd)CsCsCs
                        L7: Cs-(CdN3d)CsCsCs
                    L6: Cs-C=SCsCsCs
                L5: Cs-CtCsCsCs
                    L6: Cs-(CtN3t)CsCsCs
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
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cds)CsCs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CsCs
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CsCs
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CsCs
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)CsCs
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)CsCs
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Cd)CsCs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CsCs
                    L6: Cs-C=S(Cds-Cd)CsCs
                        L7: Cs-C=S(Cds-Cds)CsCs
                        L7: Cs-C=S(Cds-Cdd)CsCs
                            L8: Cs-C=S(Cds-Cdd-Sd)CsCs
                            L8: Cs-C=S(Cds-Cdd-Cd)CsCs
                    L6: Cs-C=SC=SCsCs
                L5: Cs-CtCdsCsCs
                    L6: Cs-(Cds-Od)CtCsCs
                    L6: Cs-(Cds-Cd)CtCsCs
                        L7: Cs-(Cds-Cds)CtCsCs
                        L7: Cs-(Cds-Cdd)CtCsCs
                            L8: Cs-(Cds-Cdd-Od)CtCsCs
                            L8: Cs-(Cds-Cdd-Sd)CtCsCs
                            L8: Cs-(Cds-Cdd-Cd)CtCsCs
                    L6: Cs-C=SCtCsCs
                L5: Cs-CbCdsCsCs
                    L6: Cs-(Cds-Od)CbCsCs
                    L6: Cs-(Cds-Cd)CbCsCs
                        L7: Cs-(Cds-Cds)CbCsCs
                        L7: Cs-(Cds-Cdd)CbCsCs
                            L8: Cs-(Cds-Cdd-Od)CbCsCs
                            L8: Cs-(Cds-Cdd-Sd)CbCsCs
                            L8: Cs-(Cds-Cdd-Cd)CbCsCs
                    L6: Cs-C=SCbCsCs
                L5: Cs-CtCtCsCs
                    L6: Cs-(CtN3t)(CtN3t)CsCs
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
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Sd)Cs
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)Cs
                        L7: Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)Cs
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)Cs
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Cd)Cs
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Sd)(Cds-Cdd-Sd)Cs
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Sd)(Cds-Cdd-Cd)Cs
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)Cs
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)Cs
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)Cs
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)(Cds-Cdd-Sd)Cs
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)(Cds-Cdd-Cd)Cs
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs
                    L6: Cs-C=S(Cds-Cd)(Cds-Cd)Cs
                        L7: Cs-C=S(Cds-Cds)(Cds-Cds)Cs
                        L7: Cs-C=S(Cds-Cdd)(Cds-Cds)Cs
                            L8: Cs-C=S(Cds-Cdd-Sd)(Cds-Cds)Cs
                            L8: Cs-C=S(Cds-Cdd-Cd)(Cds-Cds)Cs
                        L7: Cs-C=S(Cds-Cdd)(Cds-Cdd)Cs
                            L8: Cs-C=S(Cds-Cdd-Sd)(Cds-Cdd-Sd)Cs
                            L8: Cs-C=S(Cds-Cdd-Sd)(Cds-Cdd-Cd)Cs
                            L8: Cs-C=S(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cs
                    L6: Cs-C=SC=S(Cds-Cd)Cs
                        L7: Cs-C=SC=S(Cds-Cds)Cs
                        L7: Cs-C=SC=S(Cds-Cdd)Cs
                            L8: Cs-C=SC=S(Cds-Cdd-Sd)Cs
                            L8: Cs-C=SC=S(Cds-Cdd-Cd)Cs
                    L6: Cs-C=SC=SC=SCs
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
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cds)CtCs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CtCs
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CtCs
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CtCs
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)CtCs
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)CtCs
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Cd)CtCs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtCs
                    L6: Cs-C=S(Cds-Cd)CtCs
                        L7: Cs-C=S(Cds-Cds)CtCs
                        L7: Cs-C=S(Cds-Cdd)CtCs
                            L8: Cs-C=S(Cds-Cdd-Sd)CtCs
                            L8: Cs-C=S(Cds-Cdd-Cd)CtCs
                    L6: Cs-C=SC=SCtCs
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
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cds)CbCs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CbCs
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CbCs
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CbCs
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)CbCs
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)CbCs
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Cd)CbCs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbCs
                    L6: Cs-C=S(Cds-Cd)CbCs
                        L7: Cs-C=S(Cds-Cds)CbCs
                        L7: Cs-C=S(Cds-Cdd)CbCs
                            L8: Cs-C=S(Cds-Cdd-Sd)CbCs
                            L8: Cs-C=S(Cds-Cdd-Cd)CbCs
                    L6: Cs-C=SC=SCbCs
                L5: Cs-CtCtCdsCs
                    L6: Cs-(Cds-Od)CtCtCs
                    L6: Cs-(Cds-Cd)CtCtCs
                        L7: Cs-(Cds-Cds)CtCtCs
                        L7: Cs-(Cds-Cdd)CtCtCs
                            L8: Cs-(Cds-Cdd-Od)CtCtCs
                            L8: Cs-(Cds-Cdd-Sd)CtCtCs
                            L8: Cs-(Cds-Cdd-Cd)CtCtCs
                    L6: Cs-C=SCtCtCs
                L5: Cs-CbCtCdsCs
                    L6: Cs-(Cds-Od)CbCtCs
                    L6: Cs-(Cds-Cd)CbCtCs
                        L7: Cs-(Cds-Cds)CbCtCs
                        L7: Cs-(Cds-Cdd)CbCtCs
                            L8: Cs-(Cds-Cdd-Od)CbCtCs
                            L8: Cs-(Cds-Cdd-Sd)CbCtCs
                            L8: Cs-(Cds-Cdd-Cd)CbCtCs
                    L6: Cs-C=SCbCtCs
                L5: Cs-CbCbCdsCs
                    L6: Cs-(Cds-Od)CbCbCs
                    L6: Cs-(Cds-Cd)CbCbCs
                        L7: Cs-(Cds-Cds)CbCbCs
                        L7: Cs-(Cds-Cdd)CbCbCs
                            L8: Cs-(Cds-Cdd-Od)CbCbCs
                            L8: Cs-(Cds-Cdd-Sd)CbCbCs
                            L8: Cs-(Cds-Cdd-Cd)CbCbCs
                    L6: Cs-C=SCbCbCs
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
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Sd)
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)
                        L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)(Cds-Cdd)
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Sd)(Cds-Cdd-Sd)
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Sd)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                        L7: Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Sd)(Cds-Cdd-Sd)(Cds-Cdd-Sd)
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Sd)(Cds-Cdd-Sd)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Sd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)(Cds-Cdd-Sd)(Cds-Cdd-Sd)
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)(Cds-Cdd-Sd)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                    L6: Cs-C=S(Cds-Cd)(Cds-Cd)(Cds-Cd)
                        L7: Cs-C=S(Cds-Cds)(Cds-Cds)(Cds-Cds)
                        L7: Cs-C=S(Cds-Cds)(Cds-Cds)(Cds-Cdd)
                            L8: Cs-C=S(Cds-Cds)(Cds-Cds)(Cds-Cdd-Sd)
                            L8: Cs-C=S(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)
                        L7: Cs-C=S(Cds-Cds)(Cds-Cdd)(Cds-Cdd)
                            L8: Cs-C=S(Cds-Cds)(Cds-Cdd-Sd)(Cds-Cdd-Sd)
                            L8: Cs-C=S(Cds-Cds)(Cds-Cdd-Sd)(Cds-Cdd-Cd)
                            L8: Cs-C=S(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                        L7: Cs-C=S(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)
                            L8: Cs-C=S(Cds-Cdd-Sd)(Cds-Cdd-Sd)(Cds-Cdd-Sd)
                            L8: Cs-C=S(Cds-Cdd-Sd)(Cds-Cdd-Sd)(Cds-Cdd-Cd)
                            L8: Cs-C=S(Cds-Cdd-Sd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                            L8: Cs-C=S(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                    L6: Cs-C=SC=S(Cds-Cd)(Cds-Cd)
                        L7: Cs-C=SC=S(Cds-Cds)(Cds-Cds)
                        L7: Cs-C=SC=S(Cds-Cdd)(Cds-Cds)
                            L8: Cs-C=SC=S(Cds-Cdd-Sd)(Cds-Cds)
                            L8: Cs-C=SC=S(Cds-Cdd-Cd)(Cds-Cds)
                        L7: Cs-C=SC=S(Cds-Cdd)(Cds-Cdd)
                            L8: Cs-C=SC=S(Cds-Cdd-Sd)(Cds-Cdd-Sd)
                            L8: Cs-C=SC=S(Cds-Cdd-Sd)(Cds-Cdd-Cd)
                            L8: Cs-C=SC=S(Cds-Cdd-Cd)(Cds-Cdd-Cd)
                    L6: Cs-C=SC=SC=S(Cds-Cd)
                        L7: Cs-C=SC=SC=S(Cds-Cds)
                        L7: Cs-C=SC=SC=S(Cds-Cdd)
                            L8: Cs-C=SC=SC=S(Cds-Cdd-Sd)
                            L8: Cs-C=SC=SC=S(Cds-Cdd-Cd)
                    L6: Cs-C=SC=SC=SC=S
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
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Sd)Ct
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)Ct
                        L7: Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)Ct
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)Ct
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Cd)Ct
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Sd)(Cds-Cdd-Sd)Ct
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Sd)(Cds-Cdd-Cd)Ct
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)Ct
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)Ct
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)Ct
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)(Cds-Cdd-Sd)Ct
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)(Cds-Cdd-Cd)Ct
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct
                    L6: Cs-C=S(Cds-Cd)(Cds-Cd)Ct
                        L7: Cs-C=S(Cds-Cds)(Cds-Cds)Ct
                        L7: Cs-C=S(Cds-Cdd)(Cds-Cds)Ct
                            L8: Cs-C=S(Cds-Cdd-Sd)(Cds-Cds)Ct
                            L8: Cs-C=S(Cds-Cdd-Cd)(Cds-Cds)Ct
                        L7: Cs-C=S(Cds-Cdd)(Cds-Cdd)Ct
                            L8: Cs-C=S(Cds-Cdd-Sd)(Cds-Cdd-Sd)Ct
                            L8: Cs-C=S(Cds-Cdd-Sd)(Cds-Cdd-Cd)Ct
                            L8: Cs-C=S(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ct
                    L6: Cs-C=SC=S(Cds-Cd)Ct
                        L7: Cs-C=SC=S(Cds-Cds)Ct
                        L7: Cs-C=SC=S(Cds-Cdd)Ct
                            L8: Cs-C=SC=S(Cds-Cdd-Sd)Ct
                            L8: Cs-C=SC=S(Cds-Cdd-Cd)Ct
                    L6: Cs-C=SC=SC=SCt
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
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Sd)Cb
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)Cb
                        L7: Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)Cb
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Od)Cb
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Od)(Cds-Cdd-Cd)Cb
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Sd)(Cds-Cdd-Sd)Cb
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Sd)(Cds-Cdd-Cd)Cb
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)Cb
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Od)Cb
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)(Cds-Cdd-Cd)Cb
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)(Cds-Cdd-Sd)Cb
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)(Cds-Cdd-Cd)Cb
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb
                    L6: Cs-C=S(Cds-Cd)(Cds-Cd)Cb
                        L7: Cs-C=S(Cds-Cds)(Cds-Cds)Cb
                        L7: Cs-C=S(Cds-Cdd)(Cds-Cds)Cb
                            L8: Cs-C=S(Cds-Cdd-Sd)(Cds-Cds)Cb
                            L8: Cs-C=S(Cds-Cdd-Cd)(Cds-Cds)Cb
                        L7: Cs-C=S(Cds-Cdd)(Cds-Cdd)Cb
                            L8: Cs-C=S(Cds-Cdd-Sd)(Cds-Cdd-Sd)Cb
                            L8: Cs-C=S(Cds-Cdd-Sd)(Cds-Cdd-Cd)Cb
                            L8: Cs-C=S(Cds-Cdd-Cd)(Cds-Cdd-Cd)Cb
                    L6: Cs-C=SC=S(Cds-Cd)Cb
                        L7: Cs-C=SC=S(Cds-Cds)Cb
                        L7: Cs-C=SC=S(Cds-Cdd)Cb
                            L8: Cs-C=SC=S(Cds-Cdd-Sd)Cb
                            L8: Cs-C=SC=S(Cds-Cdd-Cd)Cb
                    L6: Cs-C=SC=SC=SCb
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
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cds)CtCt
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CtCt
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CtCt
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CtCt
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)CtCt
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)CtCt
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Cd)CtCt
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtCt
                    L6: Cs-C=S(Cds-Cd)CtCt
                        L7: Cs-C=S(Cds-Cds)CtCt
                        L7: Cs-C=S(Cds-Cdd)CtCt
                            L8: Cs-C=S(Cds-Cdd-Sd)CtCt
                            L8: Cs-C=S(Cds-Cdd-Cd)CtCt
                    L6: Cs-C=SC=SCtCt
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
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cds)CbCt
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CbCt
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CbCt
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CbCt
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)CbCt
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)CbCt
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Cd)CbCt
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbCt
                    L6: Cs-C=S(Cds-Cd)CbCt
                        L7: Cs-C=S(Cds-Cds)CbCt
                        L7: Cs-C=S(Cds-Cdd)CbCt
                            L8: Cs-C=S(Cds-Cdd-Sd)CbCt
                            L8: Cs-C=S(Cds-Cdd-Cd)CbCt
                    L6: Cs-C=SC=SCbCt
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
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cds)CbCb
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CbCb
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CbCb
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Od)CbCb
                            L8: Cs-(Cds-Cdd-Od)(Cds-Cdd-Cd)CbCb
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)CbCb
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Cd)CbCb
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbCb
                    L6: Cs-C=S(Cds-Cd)CbCb
                        L7: Cs-C=S(Cds-Cds)CbCb
                        L7: Cs-C=S(Cds-Cdd)CbCb
                            L8: Cs-C=S(Cds-Cdd-Sd)CbCb
                            L8: Cs-C=S(Cds-Cdd-Cd)CbCb
                    L6: Cs-C=SC=SCbCb
                L5: Cs-CtCtCtCds
                    L6: Cs-(Cds-Od)CtCtCt
                    L6: Cs-(Cds-Cd)CtCtCt
                        L7: Cs-(Cds-Cds)CtCtCt
                        L7: Cs-(Cds-Cdd)CtCtCt
                            L8: Cs-(Cds-Cdd-Od)CtCtCt
                            L8: Cs-(Cds-Cdd-Sd)CtCtCt
                            L8: Cs-(Cds-Cdd-Cd)CtCtCt
                    L6: Cs-C=SCtCtCt
                L5: Cs-CbCtCtCds
                    L6: Cs-(Cds-Od)CbCtCt
                    L6: Cs-(Cds-Cd)CbCtCt
                        L7: Cs-(Cds-Cds)CbCtCt
                        L7: Cs-(Cds-Cdd)CbCtCt
                            L8: Cs-(Cds-Cdd-Od)CbCtCt
                            L8: Cs-(Cds-Cdd-Sd)CbCtCt
                            L8: Cs-(Cds-Cdd-Cd)CbCtCt
                    L6: Cs-C=SCbCtCt
                L5: Cs-CbCbCtCds
                    L6: Cs-(Cds-Od)CbCbCt
                    L6: Cs-(Cds-Cd)CbCbCt
                        L7: Cs-(Cds-Cds)CbCbCt
                        L7: Cs-(Cds-Cdd)CbCbCt
                            L8: Cs-(Cds-Cdd-Od)CbCbCt
                            L8: Cs-(Cds-Cdd-Sd)CbCbCt
                            L8: Cs-(Cds-Cdd-Cd)CbCbCt
                    L6: Cs-C=SCbCbCt
                L5: Cs-CbCbCbCds
                    L6: Cs-(Cds-Od)CbCbCb
                    L6: Cs-(Cds-Cd)CbCbCb
                        L7: Cs-(Cds-Cds)CbCbCb
                        L7: Cs-(Cds-Cdd)CbCbCb
                            L8: Cs-(Cds-Cdd-Od)CbCbCb
                            L8: Cs-(Cds-Cdd-Sd)CbCbCb
                            L8: Cs-(Cds-Cdd-Cd)CbCbCb
                    L6: Cs-C=SCbCbCb
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
            L4: Cs-COsSsH
                L5: Cs-CsOsSsH
                L5: Cs-CdsOsSsH
                L5: Cs-CtOsSsH
                L5: Cs-CbOsSsH
            L4: Cs-COsOsSs
                L5: Cs-CsOsOsSs
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
            L4: Cs-CCCSs
                L5: Cs-CsCsCsSs
                L5: Cs-CdsCsCsSs
                    L6: Cs-(Cds-Cd)CsCsSs
                        L7: Cs-(Cds-Cds)CsCsSs
                        L7: Cs-(Cds-Cdd)CsCsSs
                            L8: Cs-(Cds-Cdd-Sd)CsCsSs
                            L8: Cs-(Cds-Cdd-Cd)CsCsSs
                    L6: Cs-C=SCsCsSs
                L5: Cs-SsCtCsCs
                L5: Cs-CbCsCsSs
                L5: Cs-CdsCdsCsSs
                    L6: Cs-(Cds-Cd)(Cds-Cd)CsSs
                        L7: Cs-(Cds-Cds)(Cds-Cds)CsSs
                        L7: Cs-(Cds-Cdd)(Cds-Cds)CsSs
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cds)CsSs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CsSs
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CsSs
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)CsSs
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Cd)CsSs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CsSs
                    L6: Cs-C=S(Cds-Cd)CsSs
                        L7: Cs-C=S(Cds-Cds)CsSs
                        L7: Cs-C=S(Cds-Cdd)CsSs
                            L8: Cs-C=S(Cds-Cdd-Sd)CsSs
                            L8: Cs-C=S(Cds-Cdd-Cd)CsSs
                    L6: Cs-C=SC=SCsSs
                L5: Cs-CtCdsCsSs
                    L6: Cs-(Cds-Cd)CtCsSs
                        L7: Cs-(Cds-Cds)CtCsSs
                        L7: Cs-(Cds-Cdd)CtCsSs
                            L8: Cs-(Cds-Cdd-Sd)CtCsSs
                            L8: Cs-(Cds-Cdd-Cd)CtCsSs
                    L6: Cs-C=SCtCsSs
                L5: Cs-CbCdsCsSs
                    L6: Cs-(Cds-Cd)CbCsSs
                        L7: Cs-(Cds-Cds)CbCsSs
                        L7: Cs-(Cds-Cdd)CbCsSs
                            L8: Cs-(Cds-Cdd-Sd)CbCsSs
                            L8: Cs-(Cds-Cdd-Cd)CbCsSs
                    L6: Cs-C=SCbCsSs
                L5: Cs-CtCtCsSs
                L5: Cs-CbCtCsSs
                L5: Cs-CbCbCsSs
                L5: Cs-CdsCdsCdsSs
                    L6: Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)Ss
                        L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Ss
                        L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd)Ss
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Sd)Ss
                            L8: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cdd-Cd)Ss
                        L7: Cs-(Cds-Cds)(Cds-Cdd)(Cds-Cdd)Ss
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Sd)(Cds-Cdd-Sd)Ss
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Sd)(Cds-Cdd-Cd)Ss
                            L8: Cs-(Cds-Cds)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ss
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)(Cds-Cdd)Ss
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)(Cds-Cdd-Sd)Ss
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)(Cds-Cdd-Cd)Ss
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ss
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ss
                    L6: Cs-C=S(Cds-Cd)(Cds-Cd)Ss
                        L7: Cs-C=S(Cds-Cds)(Cds-Cds)Ss
                        L7: Cs-C=S(Cds-Cdd)(Cds-Cds)Ss
                            L8: Cs-C=S(Cds-Cdd-Sd)(Cds-Cds)Ss
                            L8: Cs-C=S(Cds-Cdd-Cd)(Cds-Cds)Ss
                        L7: Cs-C=S(Cds-Cdd)(Cds-Cdd)Ss
                            L8: Cs-C=S(Cds-Cdd-Sd)(Cds-Cdd-Sd)Ss
                            L8: Cs-C=S(Cds-Cdd-Sd)(Cds-Cdd-Cd)Ss
                            L8: Cs-C=S(Cds-Cdd-Cd)(Cds-Cdd-Cd)Ss
                    L6: Cs-C=SC=S(Cds-Cd)Ss
                        L7: Cs-C=SC=S(Cds-Cds)Ss
                        L7: Cs-C=SC=S(Cds-Cdd)Ss
                            L8: Cs-C=SC=S(Cds-Cdd-Sd)Ss
                            L8: Cs-C=SC=S(Cds-Cdd-Cd)Ss
                    L6: Cs-C=SC=SC=SSs
                L5: Cs-CtCdsCdsSs
                    L6: Cs-(Cds-Cd)(Cds-Cd)CtSs
                        L7: Cs-(Cds-Cds)(Cds-Cds)CtSs
                        L7: Cs-(Cds-Cdd)(Cds-Cds)CtSs
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cds)CtSs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CtSs
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CtSs
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)CtSs
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Cd)CtSs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CtSs
                    L6: Cs-C=S(Cds-Cd)CtSs
                        L7: Cs-C=S(Cds-Cds)CtSs
                        L7: Cs-C=S(Cds-Cdd)CtSs
                            L8: Cs-C=S(Cds-Cdd-Sd)CtSs
                            L8: Cs-C=S(Cds-Cdd-Cd)CtSs
                    L6: Cs-C=SC=SCtSs
                L5: Cs-CbCdsCdsSs
                    L6: Cs-(Cds-Cd)(Cds-Cd)CbSs
                        L7: Cs-(Cds-Cds)(Cds-Cds)CbSs
                        L7: Cs-(Cds-Cdd)(Cds-Cds)CbSs
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cds)CbSs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)CbSs
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)CbSs
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)CbSs
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Cd)CbSs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)CbSs
                    L6: Cs-C=S(Cds-Cd)CbSs
                        L7: Cs-C=S(Cds-Cds)CbSs
                        L7: Cs-C=S(Cds-Cdd)CbSs
                            L8: Cs-C=S(Cds-Cdd-Sd)CbSs
                            L8: Cs-C=S(Cds-Cdd-Cd)CbSs
                    L6: Cs-C=SC=SCbSs
                L5: Cs-CtCtCdsSs
                    L6: Cs-(Cds-Cd)CtCtSs
                        L7: Cs-(Cds-Cds)CtCtSs
                        L7: Cs-(Cds-Cdd)CtCtSs
                            L8: Cs-(Cds-Cdd-Sd)CtCtSs
                            L8: Cs-(Cds-Cdd-Cd)CtCtSs
                    L6: Cs-C=SCtCtSs
                L5: Cs-CbCtCdsSs
                    L6: Cs-(Cds-Cd)CbCtSs
                        L7: Cs-(Cds-Cds)CbCtSs
                        L7: Cs-(Cds-Cdd)CbCtSs
                            L8: Cs-(Cds-Cdd-Sd)CbCtSs
                            L8: Cs-(Cds-Cdd-Cd)CbCtSs
                    L6: Cs-C=SCbCtSs
                L5: Cs-CbCbCdsSs
                    L6: Cs-(Cds-Cd)CbCbSs
                        L7: Cs-(Cds-Cds)CbCbSs
                        L7: Cs-(Cds-Cdd)CbCbSs
                            L8: Cs-(Cds-Cdd-Sd)CbCbSs
                            L8: Cs-(Cds-Cdd-Cd)CbCbSs
                    L6: Cs-C=SCbCbSs
                L5: Cs-CtCtCtSs
                L5: Cs-CbCtCtSs
                L5: Cs-CbCbCtSs
                L5: Cs-CbCbCbSs
            L4: Cs-CCSsSs
                L5: Cs-CsCsSsSs
                L5: Cs-CdsCsSsSs
                    L6: Cs-(Cds-Cd)CsSsSs
                        L7: Cs-(Cds-Cds)CsSsSs
                        L7: Cs-(Cds-Cdd)CsSsSs
                            L8: Cs-(Cds-Cdd-Sd)CsSsSs
                            L8: Cs-(Cds-Cdd-Cd)CsSsSs
                    L6: Cs-C=SCsSsSs
                L5: Cs-CdsCdsSsSs
                    L6: Cs-(Cds-Cd)(Cds-Cd)SsSs
                        L7: Cs-(Cds-Cds)(Cds-Cds)SsSs
                        L7: Cs-(Cds-Cdd)(Cds-Cds)SsSs
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cds)SsSs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)SsSs
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)SsSs
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)SsSs
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Cd)SsSs
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)SsSs
                    L6: Cs-C=S(Cds-Cd)SsSs
                        L7: Cs-C=S(Cds-Cds)SsSs
                        L7: Cs-C=S(Cds-Cdd)SsSs
                            L8: Cs-C=S(Cds-Cdd-Sd)SsSs
                            L8: Cs-C=S(Cds-Cdd-Cd)SsSs
                    L6: Cs-C=SC=SSsSs
                L5: Cs-CtCsSsSs
                L5: Cs-CtCdsSsSs
                    L6: Cs-(Cds-Cd)CtSsSs
                        L7: Cs-(Cds-Cds)CtSsSs
                        L7: Cs-(Cds-Cdd)CtSsSs
                            L8: Cs-(Cds-Cdd-Sd)CtSsSs
                            L8: Cs-(Cds-Cdd-Cd)CtSsSs
                    L6: Cs-C=SCtSsSs
                L5: Cs-CtCtSsSs
                L5: Cs-CbCsSsSs
                L5: Cs-CbCdsSsSs
                    L6: Cs-(Cds-Cd)CbSsSs
                        L7: Cs-(Cds-Cds)CbSsSs
                        L7: Cs-(Cds-Cdd)CbSsSs
                            L8: Cs-(Cds-Cdd-Sd)CbSsSs
                            L8: Cs-(Cds-Cdd-Cd)CbSsSs
                    L6: Cs-C=SCbSsSs
                L5: Cs-CbCtSsSs
                L5: Cs-CbCbSsSs
            L4: Cs-CSsSsSs
                L5: Cs-CsSsSsSs
                L5: Cs-CdsSsSsSs
                    L6: Cs-(Cds-Cd)SsSsSs
                        L7: Cs-(Cds-Cds)SsSsSs
                        L7: Cs-(Cds-Cdd)SsSsSs
                            L8: Cs-(Cds-Cdd-Sd)SsSsSs
                            L8: Cs-(Cds-Cdd-Cd)SsSsSs
                    L6: Cs-C=SSsSsSs
                L5: Cs-CtSsSsSs
                L5: Cs-CbSsSsSs
            L4: Cs-SsSsSsSs
            L4: Cs-CSsSsH
                L5: Cs-CsSsSsH
                L5: Cs-CdsSsSsH
                    L6: Cs-(Cds-Cd)SsSsH
                        L7: Cs-(Cds-Cds)SsSsH
                        L7: Cs-(Cds-Cdd)SsSsH
                            L8: Cs-(Cds-Cdd-Sd)SsSsH
                            L8: Cs-(Cds-Cdd-Cd)SsSsH
                    L6: Cs-C=SSsSsH
                L5: Cs-CtSsSsH
                L5: Cs-CbSsSsH
            L4: Cs-CCSsH
                L5: Cs-CsCsSsH
                L5: Cs-CdsCsSsH
                    L6: Cs-(Cds-Cd)CsSsH
                        L7: Cs-(Cds-Cds)CsSsH
                        L7: Cs-(Cds-Cdd)CsSsH
                            L8: Cs-(Cds-Cdd-Sd)CsSsH
                            L8: Cs-(Cds-Cdd-Cd)CsSsH
                    L6: Cs-C=SCsSsH
                L5: Cs-CdsCdsSsH
                    L6: Cs-(Cds-Cd)(Cds-Cd)SsH
                        L7: Cs-(Cds-Cds)(Cds-Cds)SsH
                        L7: Cs-(Cds-Cdd)(Cds-Cds)SsH
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cds)SsH
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cds)SsH
                        L7: Cs-(Cds-Cdd)(Cds-Cdd)SsH
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Sd)SsH
                            L8: Cs-(Cds-Cdd-Sd)(Cds-Cdd-Cd)SsH
                            L8: Cs-(Cds-Cdd-Cd)(Cds-Cdd-Cd)SsH
                    L6: Cs-C=S(Cds-Cd)SsH
                        L7: Cs-C=S(Cds-Cds)SsH
                        L7: Cs-C=S(Cds-Cdd)SsH
                            L8: Cs-C=S(Cds-Cdd-Sd)SsH
                            L8: Cs-C=S(Cds-Cdd-Cd)SsH
                    L6: Cs-C=SC=SSsH
                L5: Cs-CtCsSsH
                L5: Cs-CtCdsSsH
                    L6: Cs-(Cds-Cd)CtSsH
                        L7: Cs-(Cds-Cds)CtSsH
                        L7: Cs-(Cds-Cdd)CtSsH
                            L8: Cs-(Cds-Cdd-Sd)CtSsH
                            L8: Cs-(Cds-Cdd-Cd)CtSsH
                    L6: Cs-C=SCtSsH
                L5: Cs-CtCtSsH
                L5: Cs-CbCsSsH
                L5: Cs-CbCdsSsH
                    L6: Cs-(Cds-Cd)CbSsH
                        L7: Cs-(Cds-Cds)CbSsH
                        L7: Cs-(Cds-Cdd)CbSsH
                            L8: Cs-(Cds-Cdd-Sd)CbSsH
                            L8: Cs-(Cds-Cdd-Cd)CbSsH
                    L6: Cs-C=SCbSsH
                L5: Cs-CbCtSsH
                L5: Cs-CbCbSsH
            L4: Cs-CSsHH
                L5: Cs-CsSsHH
                L5: Cs-CdsSsHH
                    L6: Cs-(Cds-Cd)SsHH
                        L7: Cs-(Cds-Cds)SsHH
                        L7: Cs-(Cds-Cdd)SsHH
                            L8: Cs-(Cds-Cdd-Sd)SsHH
                            L8: Cs-(Cds-Cdd-Cd)SsHH
                    L6: Cs-C=SSsHH
                L5: Cs-CtSsHH
                L5: Cs-CbSsHH
    L2: O
        L3: Od
            L4: Od-Cd
            L4: Od-Od
            L4: Od-N3d
            L4: Od-N5d
        L3: Os
            L4: Os-N
                L5: Os-CN
                    L6: Os-CsN3s
                    L6: Os-CsN3d
                        L7: Os-Cs(N3dOd)
                    L6: Os-CdN3d
                        L7: Os-(Cd-Cd)(N3dOd)
                    L6: Os-CsN5d
                        L7: Os-Cs(N5dOdOs)
                    L6: Os-CdN5d
                        L7: Os-(Cd-CdHH)(N5dOdOs)
                L5: Os-ON
                    L6: Os-OsN3s
                    L6: Os-OsN3d
                        L7: Os-Os(N3dOd)
                L5: Os-NN
                    L6: Os-N3sN3s
                    L6: Os-N3sN3d
                        L7: Os-N3s(N3dOd)
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
                L5: Os-CSH
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
                    L6: Os-Cs(CtN3t)
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
        L3: Sd
            L4: Sd-Cd
            L4: Sd-Sd
        L3: Ss
            L4: Ss-HH
            L4: Ss-CH
                L5: Ss-CsH
                L5: Ss-CdH
                    L6: Ss-C=SH
                L5: Ss-CtH
                L5: Ss-CbH
                L5: Ss-COH
            L4: Ss-SsH
            L4: Ss-SsSs
            L4: Ss-SsC
                L5: Ss-SsCs
                L5: Ss-SsCd
                    L6: Ss-C=SSs
                L5: Ss-SsCt
                L5: Ss-SsCb
            L4: Ss-CC
                L5: Ss-CsCs
                L5: Ss-CsCd
                    L6: Ss-C=SCs
                L5: Ss-CsCt
                L5: Ss-CsCb
                L5: Ss-CdCd
                    L6: Ss-C=SCd
                        L7: Ss-C=SC=S
                L5: Ss-CdCt
                    L6: Ss-C=SCt
                L5: Ss-CdCb
                    L6: Ss-C=SCb
                L5: Ss-CtCt
                L5: Ss-CtCb
                L5: Ss-CbCb
    L2: N
        L3: N1d
        L3: N3s
            L4: N3s-CHH
                L5: N3s-CsHH
                L5: N3s-CbHH
                L5: N3s-(CO)HH
                L5: N3s-CdHH
            L4: N3s-CCH
                L5: N3s-CsCsH
                L5: N3s-CbCsH
                L5: N3s-CbCbH
                L5: N3s-(CO)CsH
                L5: N3s-(CO)CbH
                L5: N3s-(CO)(CO)H
                L5: N3s-(CtN3t)CsH
                L5: N3s-(CdCd)CsH
            L4: N3s-CCC
                L5: N3s-CsCsCs
                L5: N3s-CbCsCs
                L5: N3s-(CO)CsCs
                L5: N3s-(CO)(CO)Cs
                L5: N3s-(CO)(CO)Cb
                L5: N3s-(CtN3t)CsCs
                L5: N3s-(CdCd)CsCs
            L4: N3s-N3sHH
            L4: N3s-NCH
                L5: N3s-N3sCsH
                L5: N3s-N3sCbH
                L5: N3s-CsH(N3dOd)
                L5: N3s-CsH(N5dOdOs)
                L5: N3s-(CdCd)HN3s
            L4: N3s-NCC
                L5: N3s-NCsCs
                    L6: N3s-CsCsN3s
                    L6: N3s-CsCs(N3dOd)
                    L6: N3s-CsCs(N5dOdOs)
                L5: N3s-NCdCs
                    L6: N3s-(CdCd)CsN3s
            L4: N3s-CsHOs
            L4: N3s-CsCsOs
            L4: N3s-OsHH
        L3: N3d
            L4: N3d-CdH
            L4: N3d-N3dH
            L4: N3d-N3dN3s
            L4: N3d-OdOs
            L4: N3d-OdN3s
            L4: N3d-CsR
                L5: N3d-OdC
                L5: N3d-CdCs
                L5: N3d-N3dCs
            L4: N3d-CbR
        L3: N5d
            L4: N5d-OdOsCs
            L4: N5d-OdOsCd
            L4: N5d-OdOsOs
            L4: N5d-OdOsN3s
        L3: N5dd
"""
)

