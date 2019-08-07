#!/usr/bin/env python
# encoding: utf-8

name = "iglesia_surface"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 0,
    label = "NO",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {2,D}
2 O u0 p2 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.97,7.06,7.2,7.37,7.72,8,8.46],'cal/(mol*K)'),
        # H298 = (21.85,'kcal/mol'),
        H298 = (-25.0,'kcal/mol'),
        S298 = (49.02,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
From thermo_DFT_CCSDTF12_BAC:
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.97,7.06,7.2,7.37,7.72,8,8.46],'cal/(mol*K)'),
        H298 = (21.85,'kcal/mol'),
        S298 = (49.02,'cal/(mol*K)'),
    ),

H298 (NO)      =  21.85 kcal/mol
H298 (H)       =  52.10 kcal/mol

H298 (HNO)     =  25.34 kcal/mol

H298 (NO + H)  =  73.95 kcal/mol

H298 (HNO - H) = -26.76 kcal/mol
""",
)


