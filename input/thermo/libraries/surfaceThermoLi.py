#!/usr/bin/env python
# encoding: utf-8


name = "SurfaceThermoLi"
shortDesc = u"Surface adsorbates on Li"
longDesc = u"""

"""
#

entry(
    index = 1,
    label = "vacant",
    molecule =
"""
1 X  u0 p0 c0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        #H298 = (3*96495/4184,'kcal/mol'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
)
