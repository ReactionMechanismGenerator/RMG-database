#!/usr/bin/env python
# encoding: utf-8

name = "surfaceThermo"
shortDesc = u""
longDesc = u"""
A few surface species.
"""


entry(
    index = 1,
    label = "*",
    molecule = 
"""
1 X u0 p0 c0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""library value for a vacant surface site""",
    longDesc = 
u"""
Zeros, by definition.
""",
)

entry(
    index = 2,
    label = "CH3*",
    molecule = 
"""
1 C u0 p0 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 {1,S}
3 H u0 p0 {1,S}
4 H u0 p0 {1,S}
5 X u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.57,11.53,13.02,14.19,16.03,17.47,19.94],'cal/(mol*K)'),
        H298 = (-7.32,'kcal/mol','+|-',0.1),
        S298 = (8.06,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""Methyl adsorbed on nickle""",
    longDesc = 
u"""

""",
)


