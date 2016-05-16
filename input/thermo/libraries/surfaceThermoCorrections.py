#!/usr/bin/env python
# encoding: utf-8

name = "surfaceThermoCorrection"
shortDesc = u""
longDesc = u"""
A few surface species.
"""

entry(
    index = 1,
    label = "CR*",
    molecule =  
"""
1 C u0 p0 {2,S} {3,T}
2 R u0 p0 {1,S}
3 X u0 p0 {1,T}
""",
    thermo = AdsorptionCorrection(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Delta_Cpdata = ([-2.67,-1.82,-1.11,-0.48,0.49,1.16, 2.05],'cal/(mol*K)'),
        Delta_H298 = (-135.97,'kcal/mol'),
        Delta_S298 = (-39.38,'cal/(mol*K)'),
        ),
    shortDesc = u"""C-R triple-bonded on nickel""",
    longDesc =  u"""Estimated via CFG-TiC
  R-C
   |||
***********
""",
)

entry(
    index = 2,
    label = "CR2*",
    molecule =  
"""
1 C u0 p0 {2,S} {3,S} {4,D}
2 R u0 p0 {1,S}
3 R u0 p0 {1,S}
4 X u0 p0 {1,D}
""",
    thermo = AdsorptionCorrection(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Delta_Cpdata = ([-2.14,-0.93,0.01,0.74,1.76,2.39, 3.18],'cal/(mol*K)'),
        Delta_H298 = (-76.05,'kcal/mol'),
        Delta_S298 = (-41.84,'cal/(mol*K)'),
        ),
    shortDesc = u"""CR2 doubled-bonded on nickel""",
    longDesc =  u"""Estimated via CFG-TiC
  R-C-R
   ||
***********
""",
)

entry(
    index = 3,
    label = "CR3*",
    molecule = 
"""
1 C u0 p0 {2,S} {3,S} {4,S} {5,S}
2 R u0 p0 {1,S}
3 R u0 p0 {1,S}
4 R u0 p0 {1,S}
5 X u0 p0 {1,S}
""",
    thermo = AdsorptionCorrection(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Delta_Cpdata = ([0.97,2.02,2.63,3.00,3.40,3.60, 3.80],'cal/(mol*K)'),
        Delta_H298 = (-29.96,'kcal/mol'),
        Delta_S298 = (-36.94,'cal/(mol*K)'),
    ),
    shortDesc = u"""CR3 single-bonded on nickle""",
    longDesc = u"""Estimated via CFG-TiC
   R
   |
 R-C-R
   |
***********
""",
)

entry(
    index = 4,
    label = "CR4*",
    molecule =  
"""
1 C u0 p0 {2,S} {3,S} {4,S} {5,S} {6,vdW}
2 R u0 p0 {1,S}
3 R u0 p0 {1,S}
4 R u0 p0 {1,S}
5 R u0 p0 {1,S}
6 X u0 p0 {1,vdW}
""",
    thermo = AdsorptionCorrection(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Delta_Cpdata = ([-1.17,-1.10,-1.06,-1.04,-1.02,-1.01, -1.00],'cal/(mol*K)'),
        Delta_H298 = (-0.46,'kcal/mol'),
        Delta_S298 = (-19.25,'cal/(mol*K)'),
    ),
    shortDesc = u"""CR4 physisorbed on nickel""",
    longDesc =  u"""Estimated via CFG-TiC
 R2-C-R2
    :
***********
""",
)

entry(
    index = 5,
    label = "R2O*",
    molecule =  
"""
1 O u0 p2 {2,S} {3,S} {4,vdW}
2 R u0 p0 {1,S}
3 R u0 p0 {1,S}
4 X u0 p0 {1,vdW}
""",
    thermo = AdsorptionCorrection(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Delta_Cpdata = ([-0.99,-0.99,-0.99,-0.99,-0.99,-0.99, -0.99],'cal/(mol*K)'),
        Delta_H298 = (-0.46,'kcal/mol'),
        Delta_S298 = (-14.96,'cal/(mol*K)'),
    ),
    shortDesc = u"""R2O physisorbed on nickel""",
    longDesc =  u"""Estimated via CFG-TiC
  R-O-R
    :
***********
""",
)

entry(
    index = 7,
    label = "RCR*",
    molecule =  
"""
1 C u0 p0 {2,S} {3,S} {4,D}
2 R u0 p2 {1,S} {4,S}
3 R u0 p0 {1,S}
4 X u0 p0 {1,D} {2,S}
""",
    thermo = AdsorptionCorrection(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Delta_Cpdata = ([-3.85,-2.46,-1.42,-0.65,0.42,1.14, 2.25],'cal/(mol*K)'),
        Delta_H298 = (-41.48,'kcal/mol'),
        Delta_S298 = (-51.44,'cal/(mol*K)'),
    ),
    shortDesc = u"""RCR di-sigma adsorbed on nickel""",
    longDesc =  u"""Estimated via CFG-TiC
R--C--R
   || |
***********
""",
)

entry(
    index = 8,
    label = "COR*",
    molecule =  
"""
1 C u0 p0 {2,S} {4,T}
2 O u0 p2 {1,S} {3,S}
3 R u0 p0 {2,S}
4 X u0 p0 {1,T}
""",
    thermo = AdsorptionCorrection(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Delta_Cpdata = ([1.24,2.09,2.62,2.96,3.36,3.56, 3.78],'cal/(mol*K)'),
        Delta_H298 = (-48.39,'kcal/mol'),
        Delta_S298 = (-43.58,'cal/(mol*K)'),
    ),
    shortDesc = u"""COR adsorbed on nickel: SUBSET OF CR*!""",
    longDesc =  u"""Estimated via CFG-TiC
 RO-C
   |||
***********
""",

)

entry(
    index = 9,
    label = "CR2R*",
    molecule =  
"""
1 C u0 p0 {2,S} {3,S} {4,S} {5,S}
2 R u0 p2 {1,S} {5,S}
3 R u0 p0 {1,S}
4 R u0 p0 {1,S}
5 X u0 p0 {1,S} {2,S}
""",
    thermo = AdsorptionCorrection(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Delta_Cpdata = ([2.27,2.92,3.26,3.47,3.68,3.78, 3.88],'cal/(mol*K)'),
        Delta_H298 = (-4.61,'kcal/mol'),
        Delta_S298 = (-39.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""CR2-R di-sigma adsorbed on nickel""",
    longDesc =  u"""Estimated via CFG-TiC
R2--C--R
    |  |
***********
""",
)

entry(
    index = 10,
    label = "CROR*",
    molecule =  
"""
1 C u0 p0 {2,S} {3,S} {5,D}
2 O u0 p2 {1,S} {4,S}
3 R u0 p0 {1,S}
4 R u0 p0 {2,S}
5 X u0 p0 {1,D}
""",
    thermo = AdsorptionCorrection(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Delta_Cpdata = ([1.68,2.50,2.96,3.24,3.54,3.69, 3.84],'cal/(mol*K)'),
        Delta_H298 = (-55.31,'kcal/mol'),
        Delta_S298 = (-45.59,'cal/(mol*K)'),
    ),
    shortDesc = u"""CROR double-bonded on nickel: SUBSET OF CR2*""",
    longDesc =  u"""Estimated via CFG-TiC
  R-C-OR
   ||
***********
""",

)

entry(
    index = 11,
    label = "CR3O*",
    molecule =  
"""
1 O u0 p2 {2,S} {6,S}
2 C u0 p0 {1,S} {3,S} {4,S} {5,S}
3 R u0 p0 {2,S}
4 R u0 p0 {2,S}
5 R u0 p0 {2,S}
6 X u0 p0 {1,S}
""",
    thermo = AdsorptionCorrection(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Delta_Cpdata = ([2.76,3.26,3.50,3.64,3.78,3.85, 3.92],'cal/(mol*K)'),
        Delta_H298 = (-43.79,'kcal/mol'),
        Delta_S298 = (-40.59,'cal/(mol*K)'),
    ),
    shortDesc = u"""CR3O adsorbed on nickel""",
    longDesc =  u"""Estimated via CFG-TiC
   CR3
   |
   O
   |
***********
""",

)

entry(
    index = 12,
    label = "CR2OR*",
    molecule =  
"""
1 C u0 p0 {2,S} {3,S} {4,S} {6,S}
2 R u0 p0 {1,S}
3 R u0 p0 {1,S}
4 O u0 p2 {1,S} {5,S}
5 R u0 p0 {4,S}
6 X u0 p0 {1,S}
""",
    thermo = AdsorptionCorrection(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Delta_Cpdata = ([3.07,3.45,3.63,3.73,3.83,3.88, 3.93],'cal/(mol*K)'),
        Delta_H298 = (-23.05,'kcal/mol'),
        Delta_S298 = (-40.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""CR2OR adsorbed on nickel: SUBSET OF CR3""",
    longDesc =  u"""Estimated via CFG-TiC
   R
   |
 R-C-OR
   |
***********
""",
)

entry(
    index = 13,
    label = "CR3OR*",
    molecule =  
"""
1 O u0 p2 {2,S} {3,S} {7,vdW}
2 C u0 p0 {1,S} {4,S} {5,S} {6,S}
3 R u0 p0 {1,S}
4 R u0 p0 {2,S}
5 R u0 p0 {2,S}
6 R u0 p0 {2,S}
7 X u0 p0 {1,vdW}
""",
    thermo = AdsorptionCorrection(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Delta_Cpdata = ([0.98,0.99,0.99,0.99,0.99,0.99, 0.99],'cal/(mol*K)'),
        Delta_H298 = (-0.69,'kcal/mol'),
        Delta_S298 = (-17.57,'cal/(mol*K)'),
    ),
    shortDesc = u"""CR3OR physisorbed on nickel: SUBSET OF R2O""",
    longDesc =  u"""Estimated via CFG-TiC
   CR3
   |
   O-R
   :
***********
""",
)

entry(
    index = 14,
    label = "ROCR*",
    molecule =  
"""
1 C u0 p0 {2,S} {3,S} {5,D}
2 R u0 p2 {1,S} {5,S}
3 O u0 p2 {1,S} {4,S}
4 R u0 p0 {3,S}
5 X u0 p0 {1,D} {2,S}
""",
    thermo = AdsorptionCorrection(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Delta_Cpdata = ([-4.42,-2.87,-1.69,-0.80,0.45,1.28, 2.47],'cal/(mol*K)'),
        Delta_H298 = (-55.31,'kcal/mol'),
        Delta_S298 = (-54.21,'cal/(mol*K)'),
    ),
    shortDesc = u"""HOCO adsorbed on nickel: SUBSET OF RCR*""",
    longDesc =  u"""Estimated via CFG-TiC
RO--C--R
    || |
***********
""",
)


