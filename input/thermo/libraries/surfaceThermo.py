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
    longDesc = u"""Zeros, by definition.""",
)

entry(
    index = 2,
    label = "H*",
    molecule =  
"""
1 H u0 p0 {2,S}
2 X u0 p0 {1,S}
""",
#    thermo = ThermoData(
#        Tdata = ([300,400,500,600,800,1000,1500],'K'),
#        Cpdata = ([1.50, 2.58, 3.40, 4.00, 4.73, 5.13, 5.57],'cal/(mol*K)'),
#        H298 = (-11.26,'kcal/mol','+|-',0.1),
#        S298 = (0.44,'cal/(mol*K)','+|-',0.1),
#    ),
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.01510910E+00, 1.27747196E-02,-1.36892852E-05, 6.67076880E-09,-1.15946694E-12,-5.53052906E+03, 8.44686890E+00], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[-1.84968995E-01, 6.05229805E-03,-4.83715532E-06, 1.81340221E-09,-2.61948776E-13,-5.91533033E+03,-5.04191778E-01], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = u"""H atom adsorbed on nickel""",
    longDesc =  u"""Estimated via CFG-TOC""",
)

entry(
    index = 3,
    label = "C*",
    molecule =  
"""
1 C u0 p0 {2,Q}
2 X u0 p0 {1,Q}
""", 
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.04, 4.73, 5.12, 5.35, 5.60, 5.73, 5.85],'cal/(mol*K)'),
        H298 = (29.89,'kcal/mol','+|-',0.1),
        S298 = (2.62,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""C atom adsorbed on nickel""",
    longDesc =  u"""Estimated via CFG-TOC.
    Unsure of adjacency list: Do we want a lone pair and triple bond?!""",
)

entry(
    index = 4,
    label = "O*",
    molecule =  
"""
1 O u0 p2 {2,D}
2 X u0 p0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.52, 5.06, 5.35, 5.52, 5.70, 5.79, 5.88],'cal/(mol*K)'),
        H298 = (-52.58,'kcal/mol','+|-',0.1),
        S298 = (3.61,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""O atom adsorbed on nickel""",
    longDesc =  u"""Estimated via CFG-TOC""",
)

entry(
    index = 5,
    label = "H2*",
    molecule =  
"""
1 H u0 p0 {2,S} {3,vdW}
2 H u0 p0 {1,S}
3 X u0 p0 {1,vdW}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.83, 7.88, 7.90, 7.92, 7.97, 8.08, 8.48],'cal/(mol*K)'),
        H298 = (-2.0,'kcal/mol','+|-',0.1),
        S298 = (19.42,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""H2 physisorbed on nickel""",
    longDesc =  u"""Estimated via CFG-TOC""",
)

entry(
    index = 6,
    label = "CH*",
    molecule =  
"""
1 C u0 p0 {2,S} {3,T}
2 H u0 p0 {1,S}
3 X u0 p0 {1,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.27, 5.13, 5.88, 6.57, 7.77,  8.71, 10.12],'cal/(mol*K)'),
        H298 = (5.73,'kcal/mol','+|-',0.1),
        S298 = (2.88,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""CH adsorbed on nickel""",
    longDesc =  u"""Estimated via CFG-TOC""",
)

entry(
    index = 7,
    label = "CH2*",
    molecule =  
"""
1 C u0 p0 {2,S} {3,S} {4,D}
2 H u0 p0 {1,S}
3 H u0 p0 {1,S}
4 X u0 p0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.82, 7.37, 8.64, 9.69, 11.35, 12.64, 14.74],'cal/(mol*K)'),
        H298 = (4.11,'kcal/mol','+|-',0.1),
        S298 = (4.28,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""CH2 adsorbed on nickel""",
    longDesc =  u"""Estimated via CFG-TOC""",
)

entry(
    index = 8,
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
    longDesc = u"""Estimated via CFG-TOC""",
)

entry(
    index = 9,
    label = "CH4*",
    molecule =  
"""
1 C u0 p0 {2,S} {3,S} {4,S} {5,S} {6,vdW}
2 H u0 p0 {1,S}
3 H u0 p0 {1,S}
4 H u0 p0 {1,S}
5 H u0 p0 {1,S}
6 X u0 p0 {1,vdW}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.82, 7.37, 8.64, 9.69, 11.35, 12.64, 14.74],'cal/(mol*K)'),
        H298 = (4.11,'kcal/mol','+|-',0.1),
        S298 = (4.28,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""CH4 physisorbed on nickel""",
    longDesc =  u"""Estimated via CFG-TOC""",
)


entry(
    index = 10,
    label = "OH*",
    molecule =  
"""
1 O u0 p2 {2,S} {3,S}
2 H u0 p0 {1,S}
3 X u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.51, 6.23, 6.90, 7.47, 8.37, 9.04, 10.12],'cal/(mol*K)'),
        H298 = (-56.47,'kcal/mol','+|-',0.1),
        S298 = (5.53,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""OH adsorbed on nickel""",
    longDesc =  u"""Estimated via CFG-TOC""",
)

entry(
    index = 11,
    label = "H2O*",
    molecule =  
"""
1 O u0 p2 {2,S} {3,S} {4,vdW}
2 H u0 p0 {1,S}
3 H u0 p0 {1,S}
4 X u0 p0 {1,vdW}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.26, 11.71, 12.08, 12.41, 13.03, 13.63, 14.95],'cal/(mol*K)'),
        H298 = (-63.46,'kcal/mol','+|-',0.1),
        S298 = (20.46,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""H2O physisorbed on nickel""",
    longDesc =  u"""Estimated via CFG-TOC""",
)

entry(
    index = 12,
    label = "CO*",
    molecule =  
"""
1 C u0 p0 {2,D} {3,D}
2 O u0 p2 {1,D} 
3 X u0 p0 {1,D} 
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.96, 9.40, 9.70, 9.96, 10.40, 10.75, 11.28],'cal/(mol*K)'),
        H298 = (-57.42,'kcal/mol','+|-',0.1),
        S298 = (11.03,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""CO adsorbed on nickel (?)""",
    longDesc =  u"""Estimated via CFG-TOC
    Unsure of adjacency list.""",
)

entry(
    index = 13,
    label = "HCO*",
    molecule =  
"""
1 C u0 p0 {2,S} {3,S} {4,D}
2 O u0 p2 {1,S} {4,S}
3 H u0 p0 {1,S}
4 X u0 p0 {1,D} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.41, 10.70, 11.74, 12.60, 13.93, 14.88, 16.24],'cal/(mol*K)'),
        H298 = (-40.89,'kcal/mol','+|-',0.1),
        S298 = (9.72,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""HCO di-sigma adsorbed on nickel""",
    longDesc =  u"""Estimated via CFG-TOC
H--C--O
   || |
***********
""",
)

entry(
    index = 14,
    label = "COH*",
    molecule =  
"""
1 C u0 p0 {2,S} {4,T}
2 O u0 p2 {1,S} {3,S}
3 H u0 p0 {2,S}
4 X u0 p0 {1,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.41, 10.70, 11.74, 12.60, 13.93, 14.88, 16.24],'cal/(mol*K)'),
        H298 = (-40.89,'kcal/mol','+|-',0.1),
        S298 = (9.72,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""COH adsorbed on nickel""",
    longDesc =  u"""Estimated via CFG-TOC""",
)

entry(
    index = 15,
    label = "CH2O*",
    molecule =  
"""
1 C u0 p0 {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 {1,S} {5,S}
3 H u0 p0 {1,S}
4 H u0 p0 {1,S}
5 X u0 p0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.66, 9.82, 11.75, 13.39, 15.96, 17.80, 20.47],'cal/(mol*K)'),
        H298 = (-41.61,'kcal/mol','+|-',0.1),
        S298 = (5.62,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""CH2O di-sigma adsorbed on nickel""",
    longDesc =  u"""Estimated via CFG-TOC""",
)

entry(
    index = 16,
    label = "CHOH*",
    molecule =  
"""
1 C u0 p0 {2,S} {3,S} {5,D}
2 O u0 p2 {1,S} {4,S}
3 H u0 p0 {1,S}
4 H u0 p0 {2,S}
5 X u0 p0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.75, 12.91, 14.10, 15.22, 17.13, 18.59, 20.84],'cal/(mol*K)'),
        H298 = (-38.31,'kcal/mol','+|-',0.1),
        S298 = (17.74,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""CHOH adsorbed on nickel""",
    longDesc =  u"""Estimated via CFG-TOC""",
)

entry(
    index = 17,
    label = "CH3O*",
    molecule =  
"""
1 O u0 p2 {2,S} {6,S}
2 C u0 p0 {1,S} {3,S} {4,S} {5,S}
3 H u0 p0 {2,S}
4 H u0 p0 {2,S}
5 H u0 p0 {2,S}
6 X u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.88, 12.21, 14.63, 16.64, 18.31, 20.92, 22.84, 25.78],'cal/(mol*K)'),
        H298 = (-55.49,'kcal/mol','+|-',0.1),
        S298 = (11.88,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""CH3O adsorbed on nickel""",
    longDesc =  u"""Estimated via CFG-TOC""",
)

entry(
    index = 18,
    label = "CH2OH*",
    molecule =  
"""
1 C u0 p0 {2,S} {3,S} {4,S} {6,S}
2 H u0 p0 {1,S}
3 H u0 p0 {1,S}
4 O u0 p2 {1,S} {5,S}
5 H u0 p0 {4,S}
6 X u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.94, 16.04, 17.71, 19.02, 20.96, 22.41, 24.83],'cal/(mol*K)'),
        H298 = (-46.52,'kcal/mol','+|-',0.1),
        S298 = (14.28,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""CH2OH adsorbed on nickel""",
    longDesc =  u"""Estimated via CFG-TOC""",
)

entry(
    index = 19,
    label = "CH3OH*",
    molecule =  
"""
1 O u0 p2 {2,S} {3,S} {7,vdW}
2 C u0 p0 {1,S} {4,S} {5,S} {6,S}
3 H u0 p0 {1,S}
4 H u0 p0 {2,S}
5 H u0 p0 {2,S}
6 H u0 p0 {2,S}
7 X u0 p0 {1,vdW}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.27, 16.16, 18.12, 19.91, 22.88, 25.19, 28.98],'cal/(mol*K)'),
        H298 = (-61.06,'kcal/mol','+|-',0.1),
        S298 = (23.89,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""CH3OH physisorbed on nickel""",
    longDesc =  u"""Estimated via CFG-TOC""",
)


entry(
    index = 20,
    label = "CO2*",
    molecule =  
"""
1 C u0 p0 {2,D} {3,D} {4,vdW}
2 O u0 p2 {1,D}
3 O u0 p2 {1,D}
4 X u0 p0 {1,vdW}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.68, 10.73, 11.55, 12.21, 13.19, 13.87, 14.81],'cal/(mol*K)'),
        H298 = (-96.36,'kcal/mol','+|-',0.1),
        S298 = (35.02,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""CO2 physisorbed on nickel""",
    longDesc =  u"""Estimated via CFG-TOC""",
)

entry(
    index = 21,
    label = "HOCO*",
    molecule =  
"""
1 C u0 p0 {2,D} {3,S} {5,S}
2 O u0 p2 {1,D}
3 O u0 p2 {1,S} {4,S}
4 H u0 p0 {3,S}
5 X u0 p0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.89, 15.96, 17.39, 18.43, 19.83, 20.71, 21.81],'cal/(mol*K)'),
        H298 = (-100.37,'kcal/mol','+|-',0.1),
        S298 = (14.45,'cal/(mol*K)','+|-',0.1),
    ),
    shortDesc = u"""HOCO adsorbed on nickel""",
    longDesc =  u"""Estimated via CFG-TOC""",
)


