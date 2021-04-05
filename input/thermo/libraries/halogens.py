#!/usr/bin/env python
# encoding: utf-8

name = "halogens"
shortDesc = "halogens small molecules"
longDesc = """
This is a WIP library with small halogenated species
The H298 is from ATcT, but the S and Cp are estimated with GAV
This libary should be used for F/Cl/Br-containing systems
"""
entry(
    index = 0,
    label = "CCHF",
    molecule = 
"""
1 C u0 p1 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), 
    Cpdata=([53.9106,58.1472,61.299,63.8388,68.1495,71.6867,76.6116],'J/(mol*K)'), 
    H298=(300.1,'kJ/mol'), S298=(246.826,'J/(mol*K)'), Cp0=(33.2579,'J/(mol*K)'), 
    CpInf=(83.1447,'J/(mol*K)')),
    shortDesc = """GA + ATcT 1.122p 70302-00-0*0 H298""",
    longDesc = 
"""
H298 = 300.1 kJ/mol
""",
)

entry(
    index = 1,
    label = "CCF2",
    molecule = 
"""
1 C u0 p1 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 F u0 p3 c0 {2,S}
""",
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), 
    Cpdata=([62.2121,66.8883,69.8504,71.9626,75.5195,78.4131,80.7894],'J/(mol*K)'), 
    H298=(130.6,'kJ/mol'), S298=(259.54,'J/(mol*K)'), Cp0=(33.2579,'J/(mol*K)'), 
    CpInf=(83.1447,'J/(mol*K)')),
    shortDesc = """GA + ATcT 1.122p 41895-33-4*0 H298""",
    longDesc = 
"""
H298 = 130.6 kJ/mol
""",
)

entry(
    index = 2,
    label = "CCBr2",
    molecule = 
"""
1 C u0 p1 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 Br u0 p3 c0 {2,S}
4 Br u0 p3 c0 {2,S}
""",
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), 
    Cpdata=([72.2886,75.7863,76.9547,77.4615,79.7599,82.7872,82.4281],'J/(mol*K)'), 
    H298=(498.9,'kJ/mol'), S298=(304.88,'J/(mol*K)'), Cp0=(33.2579,'J/(mol*K)'), 
    CpInf=(83.1447,'J/(mol*K)')),
    shortDesc = """GA + ATcT 1.122p 261771-36-2*0 H298""",
    longDesc = 
"""
H298 = 498.9 kJ/mol
""",
)

entry(
    index = 3,
    label = "CCHBr",
    molecule = 
"""
1 C u0 p1 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 Br u0 p3 c0 {2,S}
""",
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), 
    Cpdata=([57.9599,61.9054,64.5072,66.5253,70.3786,73.8408,77.4814],'J/(mol*K)'), 
    H298=(460.1,'kJ/mol'), S298=(269.119,'J/(mol*K)'), Cp0=(33.2579,'J/(mol*K)'), 
    CpInf=(83.1447,'J/(mol*K)')),
    shortDesc = """GA + ATcT 1.122p 161957-27-3*0 H298""",
    longDesc = 
"""
H298 = 460.1 kJ/mol
""",
)

entry(
    index = 4,
    label = "CCHCl",
    molecule = 
"""
1 C u0 p1 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 Cl u0 p3 c0 {2,S}
""",
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'),
    Cpdata=([56.7425,60.9627,63.8772,66.1233,70.0187,73.3222,77.3704],'J/(mol*K)'),
    H298=(429.8,'kJ/mol'), S298=(257.32,'J/(mol*K)'), Cp0=(33.2579,'J/(mol*K)'),
    CpInf=(83.1447,'J/(mol*K)')),
    shortDesc = """GA + ATcT 1.122p 70277-82-6*0 H298""",
    longDesc = 
"""
H298 = 429.8 kJ/mol
""",
)

entry(
    index = 5,
    label = "CCCl2",
    molecule = 
"""
1 C u0 p1 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 Cl u0 p3 c0 {2,S}
4 Cl u0 p3 c0 {2,S}
""",
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'),
    Cpdata=([68.8108,73.1302,75.2712,76.546,79.2441,81.9894,82.7851],'J/(mol*K)'),
    H298=(424.8,'kJ/mol'), S298=(281.351,'J/(mol*K)'), Cp0=(33.2579,'J/(mol*K)'),
    CpInf=(83.1447,'J/(mol*K)')),
    shortDesc = """GA + ATcT 1.122p 70277-82-6*0 H298""",
    longDesc = 
"""
H298 = 424.8 kJ/mol
""",
)

entry(
    index = 6,
    label = "OOBr",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {2,S}
2 O  u0 p2 c0 {1,S} {3,S}
3 O  u1 p2 c0 {2,S}
""",
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), 
    Cpdata=([51.8844,52.5941,51.888,50.7367,49.4281,50.2226,52.5304],'J/(mol*K)'), 
    H298=(109.2,'kJ/mol'), S298=(275.814,'J/(mol*K)'), 
    Cp0=(33.2579,'J/(mol*K)'), CpInf=(58.2013,'J/(mol*K)')),
    shortDesc = """GA + ATcT 1.122p 67177-47-3*0 H298""",
    longDesc = 
"""
H298 = 109.2 kJ/mol
""",
)

entry(
    index = 7,
    label = "OOCl",
    molecule = 
"""
multiplicity 2
1 Cl u0 p3 c0 {2,S}
2 O  u0 p2 c0 {1,S} {3,S}
3 O  u1 p2 c0 {2,S}
""",
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), 
    Cpdata=([50.6312,51.4088,50.9024,49.9987,49.104,50.0514,52.3303],'J/(mol*K)'), 
    H298=(102.82,'kJ/mol'), S298=(267.489,'J/(mol*K)'), Cp0=(33.2579,'J/(mol*K)'), 
    CpInf=(58.2013,'J/(mol*K)')),
    shortDesc = """GA + ATcT 1.122p 17376-09-9*0 H298""",
    longDesc = 
"""
H298 = 102.82 kJ/mol
""",
)

entry(
    index = 8,
    label = "OOF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u1 p2 c0 {2,S}
""",
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), 
    Cpdata=([43.4949,45.0513,46.0077,46.7044,48.1531,50.0169,53.7856],'J/(mol*K)'), 
    H298=(25.10,'kJ/mol'), S298=(255.854,'J/(mol*K)'), Cp0=(33.2579,'J/(mol*K)'), 
    CpInf=(58.2013,'J/(mol*K)')),
    shortDesc = """GA + ATcT 1.122p 15499-23-7*0 H298""",
    longDesc = 
"""
H298 = 25.10 kJ/mol
""",
)