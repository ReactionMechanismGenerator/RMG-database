#!/usr/bin/env python
# encoding: utf-8

name = "SulfurGlarborgNS"
shortDesc = u""
longDesc = u"""
Interactions between nitrogen and sulfur species in combustion

Taken from:
Hidden interactions - Trace species governing combustion and emmision
Peter Glarborg
Proceedings of the Combustion Institute, 31 (2007) 77-98
DOI: 10.1016/j.proci.2006.08.119
"""

entry(
    index = 1,
    label = "NS",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {2,D}
2 S u0 p2 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([31.78,32.45,33.29,33.81,34.08,35.34,36.97],'J/(mol*K)'),
        H298 = (278.0,'J/mol'),
        S298 = (222.2,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "SNO",
    molecule = 
"""
multiplicity 2
1 S u1 p2 c0 {2,S}
2 N u0 p1 c0 {1,S} {3,D}
3 O u0 p2 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([41.43,44.83,47.42,49.44,52.27,54.00,56.12],'J/(mol*K)'),
        H298 = (176.0,'J/mol'),
        S298 = (257.9,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "NSO",
    molecule = 
"""
1 N u1 p1 c0 {2,D}
2 S u0 p1 c0 {1,D} {3,D}
3 O u0 p2 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([42.70,46.11,48.85,50.92,53.56,55.04,56.70],'J/(mol*K)'),
        H298 = (168.0,'J/mol'),
        S298 = (262.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "HSNO",
    molecule = 
"""
1 S u0 p2 c0 {2,S} {4,S}
2 N u0 p1 c0 {1,S} {3,D}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([53.72,58.53,62.04,64.89,69.32,72.55,77.28],'J/(mol*K)'),
        H298 = (94.0,'J/mol'),
        S298 = (267.8,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

