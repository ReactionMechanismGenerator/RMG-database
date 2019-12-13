#!/usr/bin/env python
# encoding: utf-8

name = "Surface Adsorption Corrections"
shortDesc = u""
longDesc = u"""
Changes due to adsorbing on a surface.
Initially, Nickel
"""

entry(
    index = 1,
    label = "R*",
    group=
"""
1 R u0
2 X u0
""",
    thermo=None,
    shortDesc=u"""Anything adsorbed anyhow.""",
    longDesc=u"""
   R
   x
***********
This node should be empty, ensuring that one of the nodes below is used.
""",
    metal = "Ni",
    facet = "111",
)

entry(
    index=1,
    label="R*chemisorbed",
    group=
"""
1 R u0 px {2,[S,D,T,Q]}
2 X u0 p0 {1,[S,D,T,Q]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-2.67, -1.82, -1.11, -0.48, 0.49, 1.16, 2.05], 'cal/(mol*K)'),
        H298=(-100, 'kcal/mol'),
        S298=(-30., 'cal/(mol*K)'),
        ),
    shortDesc=u"""Anything adsorbed by any chemical bond. BAD DATA! REMOVE!""",
    longDesc=u"""
   R
   x  <--(single, double, triple, or quadruple bond)
********
Data made up. Do not use!
""",
    metal = "Ni",
    facet = "111",
)

entry(
    index=1,
    label="R*vdW",
    group=
"""
1 R u0 px
2 X u0 p0
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'cal/(mol*K)'),
        H298=(-2.0, 'kcal/mol'),
        S298=(-15.0, 'cal/(mol*K)'),
        ),
    shortDesc=u"""Anything physisorbed by a van der Waals bond""",
    longDesc =  u"""
   R
   :  <---(van der Waals bond)
********
Consider the Deutschmann mechanism rate constants for CH4, CO2, and H2O.
The average binding enthalpy is 41.3 kJ/mol, so call it 10 kcal/mol.
The average loss in entropy is -16.7 J/mol-K, so call it -4. cal/mol-K

This binds too strongly and won't desorb until ~2500K, so we're trying
-2 kcal/mol and -15 cal/mol/K
""",
    metal = "Ni",
    facet = "111",
)



entry(
    index = 1,
    label = "C*",
    group=
"""
1 C u0 px {2,[S,D,T,Q]}
2 X u0 p0 {1,[S,D,T,Q]}
""",
    thermo=None,
    shortDesc=u"""Carbon chemisorbed by any bond""",
    longDesc =  u"""
   C
   x
***********
""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 1,
    label = "O*",
    group=
"""
1 O u0 px {2,[S,D,T,Q]}
2 X u0 p0 {1,[S,D,T,Q]}
""",
    thermo=None,
    shortDesc=u"""Oxygen chemisorbed by any bond""",
    longDesc =  u"""
   O
   x
***********
""",
    metal = "Ni",
    facet = "111",
)


entry(
    index = 1,
    label="C#*R",
    group=
"""
1 C u0 p0 {2,S} {3,T}
2 R u0 p0 {1,S}
3 X u0 p0 {1,T}
""",
    thermo=ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata=([-2.67, -1.82, -1.11, -0.48, 0.49, 1.16, 2.05], 'cal/(mol*K)'),
        H298=(-135.97, 'kcal/mol'),
        S298=(-39.38, 'cal/(mol*K)'),
        ),
    shortDesc = u"""C-R triple-bonded on nickel""",
    longDesc =  u"""Estimated via CFG-TiC
  R-C
   |||
***********
""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 2,
    label="C=*R2",
    group=
"""
1 C u0 p0 {2,S} {3,S} {4,D}
2 R u0 p0 {1,S}
3 R u0 p0 {1,S}
4 X u0 p0 {1,D}
""",
    thermo=ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata=([-2.14, -0.93, 0.01, 0.74, 1.76, 2.39, 3.18], 'cal/(mol*K)'),
        H298=(-76.05, 'kcal/mol'),
        S298=(-41.84, 'cal/(mol*K)'),
        ),
    shortDesc = u"""CR2 doubled-bonded on nickel""",
    longDesc =  u"""Estimated via CFG-TiC
  R-C-R
   ||
***********
""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 3,
    label = "C*R3",
    group=
"""
1 C u0 p0 {2,S} {3,S} {4,S} {5,S}
2 R u0 p0 {1,S}
3 R u0 p0 {1,S}
4 R u0 p0 {1,S}
5 X u0 p0 {1,S}
""",
    thermo=ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata=([0.97, 2.02, 2.63, 3.00, 3.40, 3.60, 3.80], 'cal/(mol*K)'),
        H298=(-29.96, 'kcal/mol'),
        S298=(-36.94, 'cal/(mol*K)'),
    ),
    shortDesc = u"""CR3 single-bonded on nickle""",
    longDesc = u"""Estimated via CFG-TiC
   R
   |
 R-C-R
   |
***********
""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 4,
    label="(CR4)*",
    group=
"""
1 C u0 p0 {2,S} {3,S} {4,S} {5,S}
2 R u0 p0 {1,S}
3 R u0 p0 {1,S}
4 R u0 p0 {1,S}
5 R u0 p0 {1,S}
6 X u0 p0
""",
    thermo=None,
    shortDesc = u"""CR4 physisorbed on nickel""",
    longDesc =  u"""
 R2-C-R2
    :
***********
""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 5,
    label="(OR2)*",
    group=
"""
1 O u0 p2 {2,S} {3,S}
2 R u0 p0 {1,S}
3 R u0 p0 {1,S}
4 X u0 p0
""",
    thermo=None,
    shortDesc = u"""R2O physisorbed on nickel""",
    longDesc =  u"""
  R-O-R
    :
***********
""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 6,
    label="C=*RR*",
    group=
"""
1 C u0 p0 {2,S} {3,S} {4,D}
2 R u0 p2 {1,S} {4,S}
3 R u0 p0 {1,S}
4 X u0 p0 {1,D} {2,S}
""",
    thermo=ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata=([-3.85, -2.46, -1.42, -0.65, 0.42, 1.14, 2.25], 'cal/(mol*K)'),
        H298=(-41.48, 'kcal/mol'),
        S298=(-51.44, 'cal/(mol*K)'),
    ),
    shortDesc = u"""RCR di-sigma adsorbed on nickel""",
    longDesc =  u"""Estimated via CFG-TiC
R--C--R
   || |
***********
""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 7,
    label="C#*OR",
    group=
"""
1 C u0 p0 {2,S} {4,T}
2 O u0 p2 {1,S} {3,S}
3 R u0 p0 {2,S}
4 X u0 p0 {1,T}
""",
    thermo=ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata=([1.24, 2.09, 2.62, 2.96, 3.36, 3.56, 3.78], 'cal/(mol*K)'),
        H298=(-48.39, 'kcal/mol'),
        S298=(-43.58, 'cal/(mol*K)'),
    ),
    shortDesc=u"""COR adsorbed on nickel by a triple bond: SUBSET OF C*R!""",
    longDesc =  u"""Estimated via CFG-TiC
 RO-C
   |||
***********
""",

)

entry(
    index = 8,
    label = "C*R2R*",
    group=
"""
1 C u0 p0 {2,S} {3,S} {4,S} {5,S}
2 R u0 p2 {1,S} {6,S}
3 R u0 p0 {1,S}
4 R u0 p0 {1,S}
5 X u0 p0 {1,S}
6 X u0 p0 {2,S}
""",
    thermo=ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata=([2.27, 2.92, 3.26, 3.47, 3.68, 3.78, 3.88], 'cal/(mol*K)'),
        H298=(-4.61, 'kcal/mol'),
        S298=(-39.81, 'cal/(mol*K)'),
    ),
    shortDesc = u"""CR2-R di-sigma adsorbed on nickel""",
    longDesc =  u"""Estimated via CFG-TiC
R2--C--R
    |  |
***********
""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 9,
    label="C=*ROR",
    group=
"""
1 C u0 p0 {2,S} {3,S} {5,D}
2 O u0 p2 {1,S} {4,S}
3 R u0 p0 {1,S}
4 R u0 p0 {2,S}
5 X u0 p0 {1,D}
""",
    thermo=ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata=([1.68, 2.50, 2.96, 3.24, 3.54, 3.69, 3.84], 'cal/(mol*K)'),
        H298=(-55.31, 'kcal/mol'),
        S298=(-45.59, 'cal/(mol*K)'),
    ),
    shortDesc=u"""CROR double-bonded on nickel: SUBSET OF C=*R2""",
    longDesc =  u"""Estimated via CFG-TiC
  R-C-OR
   ||
***********
""",

)

entry(
    index = 10,
    label = "O*CR3",
    group=
"""
1 O u0 p2 {2,S} {6,S}
2 C u0 p0 {1,S} {3,S} {4,S} {5,S}
3 R u0 p0 {2,S}
4 R u0 p0 {2,S}
5 R u0 p0 {2,S}
6 X u0 p0 {1,S}
""",
    thermo=ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata=([2.76, 3.26, 3.50, 3.64, 3.78, 3.85, 3.92], 'cal/(mol*K)'),
        H298=(-43.79, 'kcal/mol'),
        S298=(-40.59, 'cal/(mol*K)'),
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
    index = 11,
    label = "C*R2OR",
    group=
"""
1 C u0 p0 {2,S} {3,S} {4,S} {6,S}
2 R u0 p0 {1,S}
3 R u0 p0 {1,S}
4 O u0 p2 {1,S} {5,S}
5 R u0 p0 {4,S}
6 X u0 p0 {1,S}
""",
    thermo=ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata=([3.07, 3.45, 3.63, 3.73, 3.83, 3.88, 3.93], 'cal/(mol*K)'),
        H298=(-23.05, 'kcal/mol'),
        S298=(-40.81, 'cal/(mol*K)'),
    ),
    shortDesc = u"""CR2OR adsorbed on nickel: SUBSET OF C*R3""",
    longDesc =  u"""Estimated via CFG-TiC
   R
   |
 R-C-OR
   |
***********
""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 12,
    label="(CR3OR)*",
    group=
"""
1 O u0 p2 {2,S} {3,S}
2 C u0 p0 {1,S} {4,S} {5,S} {6,S}
3 R u0 p0 {1,S}
4 R u0 p0 {2,S}
5 R u0 p0 {2,S}
6 R u0 p0 {2,S}
7 X u0 p0
""",
    thermo=None,
    shortDesc = u"""CR3OR physisorbed on nickel: SUBSET OF O*R2""",
    longDesc =  u"""
   CR3
   |
   O-R
   :
***********
""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 13,
    label = "C*ORR*",
    group=
"""
1 C u0 p0 {2,S} {3,S} {5,D}
2 R u0 p2 {1,S} {6,S}
3 O u0 p2 {1,S} {4,S}
4 R u0 p0 {3,S}
5 X u0 p0 {1,D}
6 X u0 p0 {2,S}
""",
    thermo=ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata=([-4.42, -2.87, -1.69, -0.80, 0.45, 1.28, 2.47], 'cal/(mol*K)'),
        H298=(-55.31, 'kcal/mol'),
        S298=(-54.21, 'cal/(mol*K)'),
    ),
    shortDesc = u"""HOCO adsorbed on nickel: SUBSET OF RCR*""",
    longDesc =  u"""Estimated via CFG-TiC
RO--C--R
    || |
***********
""",
    metal = "Ni",
    facet = "111",
)

tree(
"""
L1: R*
    L2: R*chemisorbed
        L3: C*
            L4: C#*R
                L5: C#*OR
            L4: C=*R2
                L5: C=*ROR
            L4: C*R3
                L5: C*R2OR
        L3: O*
            L4: O*CR3
    L2: R*vdW
        L3: (CR4)*
        L3: (OR2)*
           L4: (CR3OR)*

"""
)
