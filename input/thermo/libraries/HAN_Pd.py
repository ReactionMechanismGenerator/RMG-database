#!/usr/bin/env python
# encoding: utf-8

name = "HAN"
shortDesc = "Things needed for HAN modeling"
longDesc = """
Collection of things needed for the modeling of Hydroxyl Ammonium Nitrate on Ir
"""

entry(
    index = 1,
    label = 'HAN_Pd',
    molecule = 
"""
metal Ir
1  O u0 p2 c0 {5,S} {8,S}
2  O u0 p3 c-1 {6,S} {7,H}
3  O u0 p3 c-1 {6,S} {8,H}
4  O u0 p2 c0 {6,D}
5  N u0 p0 c+1 {1,S} {7,S} {9,S} {10,S}
6  N u0 p0 c+1 {2,S} {3,S} {4,D}
7  H u0 p0 c0 {2,H} {5,S}
8  H u0 p0 c0 {1,S} {3,H}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 X u0 p0 c0
""",
    thermo = ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'), 
        Cpdata=([111.078, 131.036, 147.758, 161.708, 183.224, 198.423, 219.656], 'J/(mol*K)'), 
        H298=(-326.996, 'kJ/mol'), S298=(203.955, 'J/(mol*K)'),
            
    ),
    shortDesc = """Estimated from gas phase and Banerjee""",
    longDesc = 
"""
"""
)
