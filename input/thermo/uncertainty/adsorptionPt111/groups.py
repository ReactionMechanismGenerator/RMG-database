#!/usr/bin/env python
# encoding: utf-8

name = "adsorptionPt111 uncertainty groups"
shortDesc = "Uncertainty group definitions for adsorbates on Pt(111)"
longDesc = """
This database defines the adsorption-group patterns in the same order as the corresponding covariances.npy.
This is allows the uncertainty analysis to account for correlations when different groups on the same adsorption correction tree
were trained using the same DFT data.
"""
entry(
    index = 0,
    label = "R*",
    group = 
"""
1   R ux
2 * X ux
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1,
    label = "(OR2)*",
    group = 
"""
1   O u0 p2 c0 {2,S} {3,S}
2   R u0 c0 {1,S}
3   R u0 c0 {1,S}
4 * X u0 p0 c0
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2,
    label = "O-*R",
    group = 
"""
1   O u0 p2 c0 {2,S} {3,S}
2 * X u0 p0 c0 {1,S}
3   R u0 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 3,
    label = "(OROR)*",
    group = 
"""
1   O u0 p2 c0 {2,S} {3,S}
2   O u0 p2 c0 {1,S} {4,S}
3   R u0 c0 {1,S}
4   R u0 c0 {2,S}
5 * X u0 p0 c0
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 4,
    label = "O*O*",
    group = 
"""
1   O u0 p2 c0 {2,S} {3,S}
2   O u0 p2 c0 {1,S} {4,S}
3 * X u0 p0 c0 {1,S}
4   X u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 5,
    label = "O-*OR",
    group = 
"""
1   O u0 p2 c0 {2,S} {3,S}
2   O u0 p2 c0 {1,S} {4,S}
3 * X u0 p0 c0 {1,S}
4   R u0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 6,
    label = "O=*",
    group = 
"""
1 * X u0 p0 c0 {2,D}
2   O u0 p2 c0 {1,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 7,
    label = "O-*NR2",
    group = 
"""
1   N u0 p1 c0 {2,S} {3,S} {4,S}
2   O u0 p2 c0 {1,S} {5,S}
3   R u0 p0 c0 {1,S}
4   R u0 p0 c0 {1,S}
5 * X u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 8,
    label = "O-*CR3",
    group = 
"""
1   C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   O u0 p2 c0 {1,S} {6,S}
3   R u0 c0 {1,S}
4   R u0 c0 {1,S}
5   R u0 c0 {1,S}
6 * X u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 9,
    label = "(NR3)*",
    group = 
"""
1   N u0 p1 c0 {2,S} {3,S} {4,S}
2   R u0 c0 {1,S}
3   R u0 c0 {1,S}
4   R u0 c0 {1,S}
5 * X u0 p0 c0
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 10,
    label = "N-*R2",
    group = 
"""
1   N u0 p1 c0 {2,S} {3,[S,D]}
2 * X u0 p0 c0 {1,S}
3   R u0 c0 {1,[S,D]}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 11,
    label = "N=*R",
    group = 
"""
1   N u0 p1 c0 {2,D} {3,S}
2 * X u0 p0 c0 {1,D}
3   R u0 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 12,
    label = "N#*",
    group = 
"""
1 * X u0 p0 {2,T}
2   N u0 p1 {1,T}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 13,
    label = "(NR2OR)*",
    group = 
"""
1   N u0 p1 c0 {2,S} {3,S} {4,S}
2   O u0 p2 c0 {1,S} {5,S}
3   R u0 p0 c0 {1,S}
4   R u0 p0 c0 {1,S}
5   R u0 p0 c0 {2,S}
6 * X u0 p0 c0
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 14,
    label = "(NRO)*",
    group = 
"""
1   N u0 p1 c0 {2,D} {3,S}
2   O u0 p2 c0 {1,D}
3   R u0 p0 c0 {1,S}
4 * X u0 p0 c0
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 15,
    label = "N-*ROR",
    group = 
"""
1   N u0 p1 c0 {2,S} {3,S} {4,S}
2   O u0 p2 c0 {1,S} {5,S}
3 * X u0 p0 c0 {1,S}
4   R u0 p0 c0 {1,S}
5   R u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 16,
    label = "N-*O",
    group = 
"""
1   N u0 p1 c0 {2,S} {3,D}
2 * X u0 p0 c0 {1,S}
3   O u0 p2 c0 {1,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 17,
    label = "N=*O-*",
    group = 
"""
1   N u0 p1 c0 {2,S} {3,D}
2   O u0 p2 c0 {1,S} {4,S}
3 * X u0 p0 c0 {1,D}
4   X u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 18,
    label = "N=*OR",
    group = 
"""
1   N u0 p1 c0 {2,S} {3,D}
2   O u0 p2 c0 {1,S} {4,S}
3 * X u0 p0 c0 {1,D}
4   R u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 19,
    label = "(NR2NR2)*",
    group = 
"""
1   N u0 p1 c0 {2,S} {3,S} {4,S}
2   N u0 p1 c0 {1,S} {5,S} {6,S}
3   R u0 p0 c0 {1,S}
4   R u0 p0 c0 {1,S}
5   R u0 p0 c0 {2,S}
6   R u0 p0 c0 {2,S}
7 * X u0 p0 c0
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 20,
    label = "(NRNR)*",
    group = 
"""
1   N u0 p1 c0 {2,D} {3,S}
2   N u0 p1 c0 {1,D} {4,S}
3   R u0 p0 c0 {1,S}
4   R u0 p0 c0 {2,S}
5 * X u0 p0 c0
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 21,
    label = "N-*RNR2",
    group = 
"""
1   N u0 p1 c0 {2,S} {3,S} {4,S}
2   N u0 p1 c0 {1,S} {5,S} {6,S}
3 * X u0 p0 c0 {1,S}
4   R u0 p0 c0 {1,S}
5   R u0 p0 c0 {2,S}
6   R u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 22,
    label = "N-*NR",
    group = 
"""
1   N u0 p1 c0 {2,D} {3,S}
2   N u0 p1 c0 {1,D} {4,S}
3 * X u0 p0 c0 {1,S}
4   R u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 23,
    label = "N=*NR2",
    group = 
"""
1   N u0 p1 c0 {2,S} {3,S} {4,S}
2   N u0 p1 c0 {1,S} {5,D}
3   R u0 p0 c0 {1,S}
4   R u0 p0 c0 {1,S}
5 * X u0 p0 c0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 24,
    label = "N-*RN-*R",
    group = 
"""
1   N u0 p1 c0 {2,S} {3,S} {5,S}
2   N u0 p1 c0 {1,S} {4,S} {6,S}
3 * X u0 p0 c0 {1,S}
4   X u0 p0 c0 {2,S}
5   R u0 p0 c0 {1,S}
6   R u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 25,
    label = "N-*RCR3",
    group = 
"""
1   C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   N u0 p1 c0 {1,S} {6,S} {7,S}
3   R u0 p0 c0 {1,S}
4   R u0 p0 c0 {1,S}
5   R u0 p0 c0 {1,S}
6 * X u0 p0 c0 {2,S}
7   R u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 26,
    label = "N-*CR2",
    group = 
"""
1   C u0 p0 c0 {2,D} {3,S} {4,S}
2   N u0 p1 c0 {1,D} {5,S}
3   R u0 p0 c0 {1,S}
4   R u0 p0 c0 {1,S}
5 * X u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 27,
    label = "N=*CR3",
    group = 
"""
1   C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   N u0 p1 c0 {1,S} {6,D}
3   R u0 p0 c0 {1,S}
4   R u0 p0 c0 {1,S}
5   R u0 p0 c0 {1,S}
6 * X u0 p0 c0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 28,
    label = "Cq*",
    group = 
"""
1 * X u0 p0 c0 {2,Q}
2   C u0 p0 c0 {1,Q}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 29,
    label = "C-*C-*",
    group = 
"""
1   C u0 p0 c0 {2,D} {3,D}
2   C u0 p0 c0 {1,D} {4,D}
3 * X u0 p0 c0 {1,D}
4   X u0 p0 c0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 30,
    label = "C=*(=R)",
    group = 
"""
1   C   u0 p0 c0 {2,D} {3,D}
2 * X   u0 p0 c0 {1,D}
3   R!H u0 c0 {1,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 31,
    label = "C#*CR3",
    group = 
"""
1   C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   C u0 p0 c0 {1,S} {6,T}
3   R u0 c0 {1,S}
4   R u0 c0 {1,S}
5   R u0 c0 {1,S}
6 * X u0 p0 c0 {2,T}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 32,
    label = "C#*R",
    group = 
"""
1   C u0 p0 c0 {2,T} {3,S}
2 * X u0 p0 c0 {1,T}
3   R u0 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 33,
    label = "C=*RC=*R",
    group = 
"""
1   C u0 p0 c0 {2,S} {3,D} {5,S}
2   C u0 p0 c0 {1,S} {4,D} {6,S}
3 * X u0 p0 c0 {1,D}
4   X u0 p0 c0 {2,D}
5   R u0 c0 {1,S}
6   R u0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 34,
    label = "C=*R2",
    group = 
"""
1   C u0 p0 c0 {2,D} {3,S} {4,S}
2 * X u0 p0 c0 {1,D}
3   R u0 c0 {1,S}
4   R u0 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 35,
    label = "C-*R2C-*R2",
    group = 
"""
1   C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2   C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3 * X u0 p0 c0 {1,S}
4   X u0 p0 c0 {2,S}
5   R u0 c0 {1,S}
6   R u0 c0 {1,S}
7   R u0 c0 {2,S}
8   R u0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 36,
    label = "C-*R3",
    group = 
"""
1   C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * X u0 p0 c0 {1,S}
3   R u0 c0 {1,S}
4   R u0 c0 {1,S}
5   R u0 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 37,
    label = "(CR3CR3)*",
    group = 
"""
1   C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3   R u0 c0 {1,S}
4   R u0 c0 {1,S}
5   R u0 c0 {1,S}
6   R u0 c0 {2,S}
7   R u0 c0 {2,S}
8   R u0 c0 {2,S}
9 * X u0 p0 c0
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 38,
    label = "(CR4)*",
    group = 
"""
1   C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   R u0 c0 {1,S}
3   R u0 c0 {1,S}
4   R u0 c0 {1,S}
5   R u0 c0 {1,S}
6 * X u0 p0 c0
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 39,
    label = "C=*N-*",
    group = 
"""
1   C u0 p0 c0 {2,D} {3,D}
2   N u0 p1 c0 {1,D} {4,S}
3 * X u0 p0 c0 {1,D}
4   X u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 40,
    label = "C=*(=NR)",
    group = 
"""
1   C u0 p0 c0 {2,D} {3,D}
2   N u0 p1 c0 {1,D} {4,S}
3 * X u0 p0 c0 {1,D}
4   R u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 41,
    label = "C#*NR2",
    group = 
"""
1   N u0 p1 c0 {2,S} {3,S} {4,S}
2   C u0 p0 c0 {1,S} {5,T}
3   R u0 p0 c0 {1,S}
4   R u0 p0 c0 {1,S}
5 * X u0 p0 c0 {2,T}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 42,
    label = "C#*OR",
    group = 
"""
1   C u0 p0 c0 {2,S} {3,T}
2   O u0 p2 c0 {1,S} {4,S}
3 * X u0 p0 c0 {1,T}
4   R u0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 43,
    label = "C-*R2C=*R",
    group = 
"""
1   C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   C u0 p0 c0 {1,S} {6,D} {7,S}
3 * X u0 p0 c0 {1,S}
4   R u0 c0 {1,S}
5   R u0 c0 {1,S}
6   X u0 p0 c0 {2,D}
7   R u0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 44,
    label = "C-*R2CR3",
    group = 
"""
1   C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 * X u0 p0 c0 {1,S}
4   R u0 c0 {1,S}
5   R u0 c0 {1,S}
6   R u0 c0 {2,S}
7   R u0 c0 {2,S}
8   R u0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 45,
    label = "(CR2NR)*",
    group = 
"""
1   C u0 p0 c0 {2,D} {3,S} {4,S}
2   N u0 p1 c0 {1,D} {5,S}
3   R u0 p0 c0 {1,S}
4   R u0 p0 c0 {1,S}
5   R u0 p0 c0 {2,S}
6 * X u0 p0 c0
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 46,
    label = "C-*R2NR2",
    group = 
"""
1   C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   N u0 p1 c0 {1,S} {6,S} {7,S}
3 * X u0 p0 c0 {1,S}
4   R u0 p0 c0 {1,S}
5   R u0 p0 c0 {1,S}
6   R u0 p0 c0 {2,S}
7   R u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 47,
    label = "(CR2O)*",
    group = 
"""
1   C u0 p0 c0 {2,D} {3,S} {4,S}
2   O u0 p2 c0 {1,D}
3   R u0 c0 {1,S}
4   R u0 c0 {1,S}
5 * X u0 p0 c0
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 48,
    label = "C-*R2OR",
    group = 
"""
1   C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   O u0 p2 c0 {1,S} {6,S}
3 * X u0 p0 c0 {1,S}
4   R u0 c0 {1,S}
5   R u0 c0 {1,S}
6   R u0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 49,
    label = "(CR3NR2)*",
    group = 
"""
1   C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   N u0 p1 c0 {1,S} {6,S} {7,S}
3   R u0 p0 c0 {1,S}
4   R u0 p0 c0 {1,S}
5   R u0 p0 c0 {1,S}
6   R u0 p0 c0 {2,S}
7   R u0 p0 c0 {2,S}
8 * X u0 p0 c0
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 50,
    label = "(CR3OR)*",
    group = 
"""
1   C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   O u0 p2 c0 {1,S} {6,S}
3   R u0 c0 {1,S}
4   R u0 c0 {1,S}
5   R u0 c0 {1,S}
6   R u0 c0 {2,S}
7 * X u0 p0 c0
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 51,
    label = "C-*RC=*",
    group = 
"""
1   C u0 p0 c0 {2,D} {3,S} {4,S}
2   C u0 p0 c0 {1,D} {5,D}
3 * X u0 p0 c0 {1,S}
4   R u0 c0 {1,S}
5   X u0 p0 c0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 52,
    label = "C-*RCR2",
    group = 
"""
1   C u0 p0 c0 {2,D} {3,S} {4,S}
2   C u0 p0 c0 {1,D} {5,S} {6,S}
3 * X u0 p0 c0 {1,S}
4   R u0 c0 {1,S}
5   R u0 c0 {2,S}
6   R u0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 53,
    label = "C=*RCR3",
    group = 
"""
1   C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   C u0 p0 c0 {1,S} {6,D} {7,S}
3   R u0 c0 {1,S}
4   R u0 c0 {1,S}
5   R u0 c0 {1,S}
6 * X u0 p0 c0 {2,D}
7   R u0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 54,
    label = "(CRN)*",
    group = 
"""
1   C u0 p0 c0 {2,T} {3,S}
2   N u0 p1 c0 {1,T}
3   R u0 p0 c0 {1,S}
4 * X u0 p0 c0
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 55,
    label = "C=*RN=*",
    group = 
"""
1   C u0 p0 c0 {2,S} {3,D} {4,S}
2   N u0 p1 c0 {1,S} {5,D}
3 * X u0 p0 c0 {1,D}
4   R u0 p0 c0 {1,S}
5   X u0 p0 c0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 56,
    label = "C-*RNR",
    group = 
"""
1   C u0 p0 c0 {2,D} {3,S} {4,S}
2   N u0 p1 c0 {1,D} {5,S}
3 * X u0 p0 c0 {1,S}
4   R u0 p0 c0 {1,S}
5   R u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 57,
    label = "C=*RN-*R",
    group = 
"""
1   C u0 p0 c0 {2,S} {3,D} {5,S}
2   N u0 p1 c0 {1,S} {4,S} {6,S}
3 * X u0 p0 c0 {1,D}
4   X u0 p0 c0 {2,S}
5   R u0 p0 c0 {1,S}
6   R u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 58,
    label = "C=*RNR2",
    group = 
"""
1   C u0 p0 c0 {2,S} {3,D} {4,S}
2   N u0 p1 c0 {1,S} {5,S} {6,S}
3 * X u0 p0 c0 {1,D}
4   R u0 p0 c0 {1,S}
5   R u0 p0 c0 {2,S}
6   R u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 59,
    label = "C-*RO",
    group = 
"""
1   C u0 p0 c0 {2,S} {3,D} {4,S}
2 * X u0 p0 c0 {1,S}
3   O u0 p2 c0 {1,D}
4   R u0 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 60,
    label = "C=*RO-*",
    group = 
"""
1   C u0 p0 c0 {2,S} {3,D} {4,S}
2   O u0 p2 c0 {1,S} {5,S}
3 * X u0 p0 c0 {1,D}
4   R u0 c0 {1,S}
5   X u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 61,
    label = "C=*ROR",
    group = 
"""
1   C u0 p0 c0 {2,S} {3,D} {4,S}
2   O u0 p2 c0 {1,S} {5,S}
3 * X u0 p0 c0 {1,D}
4   R u0 c0 {1,S}
5   R u0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 62,
    label = "C*",
    group = 
"""
1 * X u0 {2,[S,D,T,Q]}
2   C ux {1,[S,D,T,Q]}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 63,
    label = "N*",
    group = 
"""
1 * X u0 {2,[S,D,T]}
2   N ux {1,[S,D,T]}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 64,
    label = "O*",
    group = 
"""
1 * X u0 {2,[S,D]}
2   O ux {1,[S,D]}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 65,
    label = "R*single-chemisorbed",
    group = 
"""
1 * X u0 {2,[S,D,T,Q]}
2   R ux {1,[S,D,T,Q]}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 66,
    label = "C*C*",
    group = 
"""
1   C u0 {2,[S,D,T]} {3,[S,D,T]}
2   C u0 {1,[S,D,T]} {4,[S,D,T]}
3 * X u0 {1,[S,D,T]}
4   X u0 {2,[S,D,T]}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 67,
    label = "C*N*",
    group = 
"""
1   C u0 {2,[S,D,T]} {3,[S,D]}
2   N u0 {1,[S,D,T]} {4,[S,D,T]}
3 * X u0 {1,[S,D]}
4   X u0 {2,[S,D,T]}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 68,
    label = "C*O*",
    group = 
"""
1   C u0 {2,S} {3,[S,D,T]}
2   O u0 p2 {1,S} {4,S}
3 * X u0 {1,[S,D,T]}
4   X u0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 69,
    label = "N*N*",
    group = 
"""
1   N u0 {2,[S,D]} {3,[S,D]}
2   N u0 {1,[S,D]} {4,[S,D]}
3 * X u0 {1,[S,D]}
4   X u0 {2,[S,D]}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 70,
    label = "R*bidentate",
    group = 
"""
1   R!H ux {2,[S,D,T]} {3,[S,D,T]}
2   R!H ux {1,[S,D,T]} {4,[S,D,T]}
3 * X   u0 {1,[S,D,T]}
4   X   u0 {2,[S,D,T]}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 71,
    label = "R*vdW",
    group = 
"""
1 * X u0
2   R u0
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 72,
    label = "N*O*",
    group = 
"""
1   N u0 p1 c0 {2,[S,D]} {3,[S,D]}
2   O u0 p2 c0 {1,[S,D]} {4,[S,D]}
3 * X u0 p0 c0 {1,[S,D]}
4   X u0 p0 c0 {2,[S,D]}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 73,
    label = "(CR3)*",
    group = 
"""
1   C   u0 {2,D} {3,S} {4,S}
2   R!H u0 {1,D}
3   R   u0 {1,S}
4   R   u0 {1,S}
5 * X   u0
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 74,
    label = "(CR2)*",
    group = 
"""
1   C   u0 {2,T} {3,S}
2   R!H u0 {1,T}
3   R   u0 {1,S}
4 * X   u0
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 75,
    label = "(N=[O,N]R)*",
    group = 
"""
1   N     u0 {2,D} {3,S}
2   [N,O] u0 {1,D}
3   R     u0 {1,S}
4 * X     u0
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 76,
    label = "N-*RN=*",
    group = 
"""
1   N u0 p1 c0 {2,S} {3,S} {4,S}
2   N u0 p1 c0 {1,S} {5,D}
3 * X u0 p0 c0 {1,S}
4   R u0 p0 c0 {1,S}
5   X u0 p0 c0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 77,
    label = "(CRCR)*",
    group = 
"""
1   C u0 p0 c0 {2,T} {3,S}
2   C u0 p0 c0 {1,T} {4,S}
3   R u0 c0 {1,S}
4   R u0 c0 {2,S}
5 * X u0 p0 c0
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 78,
    label = "C-*R2N=*",
    group = 
"""
1   C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   N u0 p1 c0 {1,S} {6,D}
3 * X u0 p0 c0 {1,S}
4   R u0 p0 c0 {1,S}
5   R u0 p0 c0 {1,S}
6   X u0 p0 c0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 79,
    label = "C-*R2N-*R",
    group = 
"""
1   C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   N u0 p1 c0 {1,S} {6,S} {7,S}
3 * X u0 p0 c0 {1,S}
4   R u0 p0 c0 {1,S}
5   R u0 p0 c0 {1,S}
6   X u0 p0 c0 {2,S}
7   R u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 80,
    label = "C=*(=C)",
    group = 
"""
1   C u0 p0 c0 {2,D} {3,D}
2 * X u0 p0 c0 {1,D}
3   C u0 p0 c0 {1,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 81,
    label = "C-*R2O-*",
    group = 
"""
1   C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   O u0 p2 c0 {1,S} {6,S}
3 * X u0 p0 c0 {1,S}
4   R u0 c0 {1,S}
5   R u0 c0 {1,S}
6   X u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 82,
    label = "(CR2CR)*",
    group = 
"""
1   C u0 p0 c0 {2,D} {3,S} {4,S}
2   C u0 p0 c0 {1,D} {5,S}
3   R u0 c0 {1,S}
4   R u0 c0 {1,S}
5   R u0 c0 {2,S}
6 * X u0 p0 c0
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 83,
    label = "C=*RC-*R",
    group = 
"""
1   C   u0 p0 c0 {2,S} {3,D} {5,S}
2   C   u0 p0 c0 {1,S} {4,S} {6,D}
3 * X   u0 p0 c0 {1,D}
4   X   u0 p0 c0 {2,S}
5   R   u0 c0 {1,S}
6   R!H u0 c0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 84,
    label = "C#*C-*R",
    group = 
"""
1   C   u0 p0 c0 {2,S} {3,S} {4,D}
2   C   u0 p0 c0 {1,S} {5,T}
3   X   u0 p0 c0 {1,S}
4   R!H u0 c0 {1,D}
5 * X   u0 p0 c0 {2,T}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 85,
    label = "C#*C-*R2",
    group = 
"""
1   C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   C u0 p0 c0 {1,S} {6,T}
3   X u0 p0 c0 {1,S}
4   R u0 c0 {1,S}
5   R u0 c0 {1,S}
6 * X u0 p0 c0 {2,T}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 86,
    label = "C-*R2C-*R",
    group = 
"""
1   C   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   C   u0 p0 c0 {1,S} {6,S} {7,D}
3 * X   u0 p0 c0 {1,S}
4   R   u0 c0 {1,S}
5   R   u0 c0 {1,S}
6   X   u0 p0 c0 {2,S}
7   R!H u0 c0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 87,
    label = "C-*RC-*R",
    group = 
"""
1   C u0 p0 c0 {2,D} {3,S} {5,S}
2   C u0 p0 c0 {1,D} {4,S} {6,S}
3 * X u0 p0 c0 {1,S}
4   X u0 p0 c0 {2,S}
5   R u0 c0 {1,S}
6   R u0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 88,
    label = "C#*C=*R",
    group = 
"""
1   C u0 p0 c0 {2,S} {3,D} {4,S}
2   C u0 p0 c0 {1,S} {5,T}
3   X u0 p0 c0 {1,D}
4   R u0 c0 {1,S}
5 * X u0 p0 c0 {2,T}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 89,
    label = "C=*=R-C-*R2",
    group = 
"""
1   C   u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2   R!H u0 c0 {1,S} {3,D}
3   C   u0 p0 c0 {2,D} {7,D}
4   X   u0 p0 c0 {1,S}
5   R   u0 c0 {1,S}
6   R   u0 c0 {1,S}
7 * X   u0 p0 c0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 90,
    label = "R2C-*-R-C-*R2",
    group = 
"""
1   C   u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
2   C   u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
3   R!H u0 c0 {1,S} {2,S}
4 * X   u0 p0 c0 {1,S}
5   X   u0 p0 c0 {2,S}
6   R   u0 c0 {2,S}
7   R   u0 c0 {2,S}
8   R   u0 c0 {1,S}
9   R   u0 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 91,
    label = "RC=*-R=C-*R",
    group = 
"""
1   C   u0 p0 c0 {3,S} {4,D} {6,S}
2   C   u0 p0 c0 {3,D} {5,S} {7,S}
3   R!H u0 c0 {1,S} {2,D}
4 * X   u0 p0 c0 {1,D}
5   X   u0 p0 c0 {2,S}
6   R   u0 c0 {1,S}
7   R   u0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 92,
    label = "RC-*=R-C-*R2",
    group = 
"""
1   C   u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2   C   u0 p0 c0 {3,D} {7,S} {8,S}
3   R!H u0 c0 {1,S} {2,D}
4   X   u0 p0 c0 {1,S}
5   R   u0 c0 {1,S}
6   R   u0 c0 {1,S}
7 * X   u0 p0 c0 {2,S}
8   R   u0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 93,
    label = "RC=*-R-C-*R2",
    group = 
"""
1   C   u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2   C   u0 p0 c0 {3,S} {7,D} {8,S}
3   R!H u0 c0 {1,S} {2,S}
4   X   u0 p0 c0 {1,S}
5   R   u0 c0 {1,S}
6   R   u0 c0 {1,S}
7 * X   u0 p0 c0 {2,D}
8   R   u0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 94,
    label = "RC-*=R=C-*R",
    group = 
"""
1   C   u0 p0 c0 {3,D} {4,S} {6,S}
2   C   u0 p0 c0 {3,D} {5,S} {7,S}
3   R!H u0 p0 c0 {1,D} {2,D}
4 * X   u0 p0 c0 {1,S}
5   X   u0 p0 c0 {2,S}
6   R   u0 c0 {1,S}
7   R   u0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 95,
    label = "RC-*=R=C=*",
    group = 
"""
1   C   u0 p0 c0 {2,D} {4,S} {5,S}
2   R!H u0 p0 c0 {1,D} {3,D}
3   C   u0 p0 c0 {2,D} {6,D}
4 * X   u0 p0 c0 {1,S}
5   R   u0 c0 {1,S}
6   X   u0 p0 c0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 96,
    label = "O-*-C-O-*",
    group = 
"""
1   C u0 p0 c0 {2,S} {3,S}
2   O u0 p2 c0 {1,S} {4,S}
3   O u0 p2 c0 {1,S} {5,S}
4 * X u0 p0 c0 {2,S}
5   X u0 p0 c0 {3,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 97,
    label = "RC-*=R-O-*",
    group = 
"""
1   C   u0 p0 c0 {2,D} {4,S} {5,S}
2   R!H u0 c0 {1,D} {3,S}
3   O   u0 p2 c0 {2,S} {6,S}
4 * X   u0 p0 c0 {1,S}
5   R   u0 c0 {1,S}
6   X   u0 p0 c0 {3,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 98,
    label = "C-*R2",
    group = 
"""
1   C   u0 p0 c0 {2,S} {3,D} {4,S}
2 * X   u0 p0 c0 {1,S}
3   R!H u0 c0 {1,D}
4   R   u0 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 99,
    label = "C=*RCR2",
    group = 
"""
1   C   u0 p0 c0 {2,S} {4,S} {5,D}
2   C   u0 p0 c0 {1,S} {3,D} {6,S}
3 * X   u0 p0 c0 {2,D}
4   R   u0 c0 {1,S}
5   R!H u0 c0 {1,D}
6   R   u0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 100,
    label = "C#*CR2",
    group = 
"""
1   C   u0 p0 c0 {2,S} {3,S} {4,D}
2   C   u0 p0 c0 {1,S} {5,T}
3   R   u0 c0 {1,S}
4   R!H u0 c0 {1,D}
5 * X   u0 p0 c0 {2,T}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 101,
    label = "O-*CR2",
    group = 
"""
1   C   u0 p0 c0 {2,S} {3,S} {4,D}
2   O   u0 p2 c0 {1,S} {5,S}
3   R   u0 c0 {1,S}
4   R!H u0 c0 {1,D}
5 * X   u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 102,
    label = "C*RC*",
    group = 
"""
1   R!H u0 {2,[S,D,T]} {3,[S,D,T]}
2   C   u0 {1,[S,D,T]} {4,[S,D,T]}
3   C   u0 {1,[S,D,T]} {5,[S,D,T]}
4 * X   u0 {2,[S,D,T]}
5   X   u0 {3,[S,D,T]}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 103,
    label = "R*bridged-bidentate",
    group = 
"""
1   R!H ux {2,[S,D,T]} {3,[S,D,T]}
2   R!H ux {1,[S,D,T]} {4,[S,D,T]}
3   R!H ux {1,[S,D,T]} {5,[S,D,T]}
4 * X   u0 {2,[S,D,T]}
5   X   u0 {3,[S,D,T]}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 104,
    label = "C*RO*",
    group = 
"""
1   R!H u0 {2,[S,D,T]} {3,S}
2   C   u0 {1,[S,D,T]} {4,[S,D,T]}
3   O   u0 p2 {1,S} {5,S}
4 * X   u0 {2,[S,D,T]}
5   X   u0 {3,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 105,
    label = "O*RO*",
    group = 
"""
1   R!H u0 c0 {2,S} {3,S}
2   O   u0 p2 c0 {1,S} {4,S}
3   O   u0 p2 c0 {1,S} {5,S}
4 * X   u0 p0 c0 {2,S}
5   X   u0 p0 c0 {3,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 106,
    label = "C#*-R-C-*R2",
    group = 
"""
1   C   u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2   R!H u0 c0 {1,S} {3,S}
3   C   u0 p0 c0 {2,S} {7,T}
4   X   u0 p0 c0 {1,S}
5   R   u0 c0 {1,S}
6   R   u0 c0 {1,S}
7 * X   u0 p0 c0 {3,T}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 107,
    label = "C#*-R=C-*R",
    group = 
"""
1   C   u0 p0 c0 {2,D} {4,S} {5,S}
2   R!H u0 c0 {1,D} {3,S}
3   C   u0 p0 c0 {2,S} {6,T}
4   X   u0 p0 c0 {1,S}
5   R   u0 c0 {1,S}
6 * X   u0 p0 c0 {3,T}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 108,
    label = "C#*-R-C#*",
    group = 
"""
1   R!H u0 c0 {2,S} {3,S}
2   C   u0 p0 c0 {1,S} {4,T}
3   C   u0 p0 c0 {1,S} {5,T}
4 * X   u0 p0 c0 {2,T}
5   X   u0 p0 c0 {3,T}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 109,
    label = "RC=*-R-C=*R",
    group = 
"""
1   C   u0 p0 c0 {3,S} {4,D} {6,S}
2   C   u0 p0 c0 {3,S} {5,D} {7,S}
3   R!H u0 c0 {1,S} {2,S}
4 * X   u0 p0 c0 {1,D}
5   X   u0 p0 c0 {2,D}
6   R   u0 c0 {1,S}
7   R   u0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 110,
    label = "C#*-R-C=*R",
    group = 
"""
1   C   u0 p0 c0 {2,S} {4,D} {5,S}
2   R!H u0 c0 {1,S} {3,S}
3   C   u0 p0 c0 {2,S} {6,T}
4   X   u0 p0 c0 {1,D}
5   R   u0 c0 {1,S}
6 * X   u0 p0 c0 {3,T}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

