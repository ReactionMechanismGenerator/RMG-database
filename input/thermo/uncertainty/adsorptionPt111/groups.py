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
    label = "RX",
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
    label = "RXbidentate",
    group = 
"""
1 * X   u0 p0 c0 {3,[S,D,T]}
2   X   u0 p0 c0 {4,[S,D,T]}
3   R!H u0 {1,[S,D,T]} {4,[S,D,T]}
4   R!H u0 {2,[S,D,T]} {3,[S,D,T]}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2,
    label = "CXCX",
    group = 
"""
1 * X u0 p0 c0 {3,[S,D,T]}
2   X u0 p0 c0 {4,[S,D,T]}
3   C u0 {1,[S,D,T]} {4,[S,D,T]}
4   C u0 {2,[S,D,T]} {3,[S,D,T]}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 3,
    label = "C#XC-XR",
    group = 
"""
1 * X   u0 p0 c0 {3,T}
2   X   u0 p0 c0 {4,S}
3   C   u0 p0 c0 {1,T} {4,S}
4   C   u0 p0 c0 {2,S} {3,S} {5,D}
5   R!H u0 c0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 4,
    label = "C#XC-XR2",
    group = 
"""
1 * X u0 p0 c0 {3,T}
2   X u0 p0 c0 {4,S}
3   C u0 p0 c0 {1,T} {4,S}
4   C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
5   R u0 c0 {4,S}
6   R u0 c0 {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 5,
    label = "C#XC=XR",
    group = 
"""
1 * X u0 p0 c0 {3,T}
2   X u0 p0 c0 {4,D}
3   C u0 p0 c0 {1,T} {4,S}
4   C u0 p0 c0 {2,D} {3,S} {5,S}
5   R u0 c0 {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 6,
    label = "C-XC-X",
    group = 
"""
1 * X u0 p0 c0 {3,D}
2   X u0 p0 c0 {4,D}
3   C u0 p0 c0 {1,D} {4,D}
4   C u0 p0 c0 {2,D} {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 7,
    label = "C-XR2C-XR",
    group = 
"""
1 * X   u0 p0 c0 {3,S}
2   X   u0 p0 c0 {4,S}
3   C   u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4   C   u0 p0 c0 {2,S} {3,S} {7,D}
5   R   u0 c0 {3,S}
6   R   u0 c0 {3,S}
7   R!H u0 c0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 8,
    label = "C-XR2C-XR2",
    group = 
"""
1 * X u0 p0 c0 {3,S}
2   X u0 p0 c0 {4,S}
3   C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4   C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
5   R u0 c0 {3,S}
6   R u0 c0 {3,S}
7   R u0 c0 {4,S}
8   R u0 c0 {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 9,
    label = "C-XR2C=XR",
    group = 
"""
1 * X u0 p0 c0 {3,S}
2   X u0 p0 c0 {4,D}
3   C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4   C u0 p0 c0 {2,D} {3,S} {7,S}
5   R u0 c0 {3,S}
6   R u0 c0 {3,S}
7   R u0 c0 {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 10,
    label = "C-XRC-XR",
    group = 
"""
1 * X u0 p0 c0 {3,S}
2   X u0 p0 c0 {4,S}
3   C u0 p0 c0 {1,S} {4,D} {5,S}
4   C u0 p0 c0 {2,S} {3,D} {6,S}
5   R u0 c0 {3,S}
6   R u0 c0 {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 11,
    label = "C-XRC=X",
    group = 
"""
1 * X u0 p0 c0 {3,S}
2   X u0 p0 c0 {4,D}
3   C u0 p0 c0 {1,S} {4,D} {5,S}
4   C u0 p0 c0 {2,D} {3,D}
5   R u0 c0 {3,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 12,
    label = "C=XRC-XR",
    group = 
"""
1 * X   u0 p0 c0 {3,D}
2   X   u0 p0 c0 {4,S}
3   C   u0 p0 c0 {1,D} {4,S} {5,S}
4   C   u0 p0 c0 {2,S} {3,S} {6,D}
5   R   u0 c0 {3,S}
6   R!H u0 c0 {4,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 13,
    label = "C=XRC=XR",
    group = 
"""
1 * X u0 p0 c0 {3,D}
2   X u0 p0 c0 {4,D}
3   C u0 p0 c0 {1,D} {4,S} {5,S}
4   C u0 p0 c0 {2,D} {3,S} {6,S}
5   R u0 c0 {3,S}
6   R u0 c0 {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 14,
    label = "CXNX",
    group = 
"""
1   X u0 p0 c0 {3,[S,D,T]}
2 * X u0 p0 c0 {4,[S,D]}
3   C u0 p0 c0 {1,[S,D,T]} {4,[S,D]}
4   N u0 p1 c0 {2,[S,D]} {3,[S,D]}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 15,
    label = "C-XR2N-XR",
    group = 
"""
1   X u0 p0 c0 {3,S}
2 * X u0 p0 c0 {4,S}
3   C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4   N u0 p1 c0 {2,S} {3,S} {7,S}
5   R u0 p0 c0 {3,S}
6   R u0 p0 c0 {3,S}
7   R u0 p0 c0 {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 16,
    label = "C-XR2N=X",
    group = 
"""
1   X u0 p0 c0 {3,S}
2 * X u0 p0 c0 {4,D}
3   C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4   N u0 p1 c0 {2,D} {3,S}
5   R u0 p0 c0 {3,S}
6   R u0 p0 c0 {3,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 17,
    label = "C-XRN-X",
    group = 
"""
1   X u0 p0 c0 {3,S}
2 * X u0 p0 c0 {5,S}
3   C u0 p0 c0 {1,S} {4,S} {5,D}
4   R u0 c0 {3,S}
5   N u0 p1 c0 {2,S} {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 18,
    label = "C-XRN-XR",
    group = 
"""
1   X   u0 p0 c0 {3,S}
2 * X   u0 p0 c0 {4,S}
3   C   u0 p0 c0 {1,S} {4,S} {5,D}
4   N   u0 p1 c0 {2,S} {3,S} {6,S}
5   R!H u0 c0 {3,D}
6   R   u0 c0 {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 19,
    label = "C-XRN=X",
    group = 
"""
1   X   u0 p0 c0 {3,S}
2 * X   u0 p0 c0 {4,D}
3   C   u0 p0 c0 {1,S} {4,S} {5,D}
4   N   u0 p1 c0 {2,D} {3,S}
5   R!H u0 c0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 20,
    label = "C=XRN-XR",
    group = 
"""
1   X u0 p0 c0 {3,D}
2 * X u0 p0 c0 {4,S}
3   C u0 p0 c0 {1,D} {4,S} {5,S}
4   N u0 p1 c0 {2,S} {3,S} {6,S}
5   R u0 p0 c0 {3,S}
6   R u0 p0 c0 {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 21,
    label = "C=XRN=X",
    group = 
"""
1   X u0 p0 c0 {3,D}
2 * X u0 p0 c0 {4,D}
3   C u0 p0 c0 {1,D} {4,S} {5,S}
4   N u0 p1 c0 {2,D} {3,S}
5   R u0 p0 c0 {3,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 22,
    label = "CXOX",
    group = 
"""
1 * X u0 p0 c0 {3,[S,D,T]}
2   X u0 p0 c0 {4,S}
3   C u0 {1,[S,D,T]} {4,S}
4   O u0 p2 {2,S} {3,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 23,
    label = "C-XR2O-X",
    group = 
"""
1 * X u0 p0 c0 {3,S}
2   X u0 p0 c0 {4,S}
3   C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4   O u0 p2 c0 {2,S} {3,S}
5   R u0 c0 {3,S}
6   R u0 c0 {3,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 24,
    label = "C-XRO-X",
    group = 
"""
1 * X   u0 p0 c0 {3,S}
2   X   u0 p0 c0 {4,S}
3   C   u0 p0 c0 {1,S} {4,S} {5,D}
4   O   u0 p2 c0 {2,S} {3,S}
5   R!H u0 c0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 25,
    label = "C=XRO-X",
    group = 
"""
1 * X u0 p0 c0 {3,D}
2   X u0 p0 c0 {4,S}
3   C u0 p0 c0 {1,D} {4,S} {5,S}
4   O u0 p2 c0 {2,S} {3,S}
5   R u0 c0 {3,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 26,
    label = "NXCX",
    group = 
"""
1 * X u0 p0 c0 {3,[S,D,T]}
2   X u0 p0 c0 {4,[S,D]}
3   C u0 p0 c0 {1,[S,D,T]} {4,[S,D]}
4   N u0 p1 c0 {2,[S,D]} {3,[S,D]}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 27,
    label = "inv(C-XR2N-XR)",
    group = 
"""
1 * X u0 p0 c0 {3,S}
2   X u0 p0 c0 {4,S}
3   C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4   N u0 p1 c0 {2,S} {3,S} {7,S}
5   R u0 p0 c0 {3,S}
6   R u0 p0 c0 {3,S}
7   R u0 p0 c0 {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 28,
    label = "inv(C-XR2N=X)",
    group = 
"""
1 * X u0 p0 c0 {3,S}
2   X u0 p0 c0 {4,D}
3   C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4   N u0 p1 c0 {2,D} {3,S}
5   R u0 p0 c0 {3,S}
6   R u0 p0 c0 {3,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 29,
    label = "inv(C-XRN-X)",
    group = 
"""
1 * X u0 p0 c0 {3,S}
2   X u0 p0 c0 {5,S}
3   C u0 p0 c0 {1,S} {4,S} {5,D}
4   R u0 c0 {3,S}
5   N u0 p1 c0 {2,S} {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 30,
    label = "inv(C-XRN-XR)",
    group = 
"""
1 * X   u0 p0 c0 {3,S}
2   X   u0 p0 c0 {4,S}
3   C   u0 p0 c0 {1,S} {4,S} {5,D}
4   N   u0 p1 c0 {2,S} {3,S} {6,S}
5   R!H u0 c0 {3,D}
6   R   u0 c0 {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 31,
    label = "inv(C-XRN=X)",
    group = 
"""
1 * X   u0 p0 c0 {3,S}
2   X   u0 p0 c0 {4,D}
3   C   u0 p0 c0 {1,S} {4,S} {5,D}
4   N   u0 p1 c0 {2,D} {3,S}
5   R!H u0 c0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 32,
    label = "inv(C=XRN-XR)",
    group = 
"""
1 * X u0 p0 c0 {3,D}
2   X u0 p0 c0 {4,S}
3   C u0 p0 c0 {1,D} {4,S} {5,S}
4   N u0 p1 c0 {2,S} {3,S} {6,S}
5   R u0 p0 c0 {3,S}
6   R u0 p0 c0 {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 33,
    label = "inv(C=XRN=X)",
    group = 
"""
1 * X u0 p0 c0 {3,D}
2   X u0 p0 c0 {4,D}
3   C u0 p0 c0 {1,D} {4,S} {5,S}
4   N u0 p1 c0 {2,D} {3,S}
5   R u0 p0 c0 {3,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 34,
    label = "NXNX",
    group = 
"""
1 * X u0 p0 c0 {3,[S,D]}
2   X u0 p0 c0 {4,[S,D]}
3   N u0 {1,[S,D]} {4,[S,D]}
4   N u0 {2,[S,D]} {3,[S,D]}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 35,
    label = "N-XRN-XR",
    group = 
"""
1 * X u0 p0 c0 {3,S}
2   X u0 p0 c0 {4,S}
3   N u0 p1 c0 {1,S} {4,S} {5,S}
4   N u0 p1 c0 {2,S} {3,S} {6,S}
5   R u0 p0 c0 {3,S}
6   R u0 p0 c0 {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 36,
    label = "N-XRN=X",
    group = 
"""
1 * X u0 p0 c0 {3,S}
2   X u0 p0 c0 {4,D}
3   N u0 p1 c0 {1,S} {4,S} {5,S}
4   N u0 p1 c0 {2,D} {3,S}
5   R u0 p0 c0 {3,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 37,
    label = "NXOX",
    group = 
"""
1 * X u0 p0 c0 {3,[S,D]}
2   X u0 p0 c0 {4,S}
3   N u0 {1,[S,D]} {4,[S,D]}
4   O u0 p2 c0 {2,S} {3,[S,D]}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 38,
    label = "N-XRO-X",
    group = 
"""
1 * X u0 p0 c0 {3,S}
2   X u0 p0 c0 {4,S}
3   N u0 p1 c0 {1,S} {4,S} {5,S}
4   O u0 p2 c0 {2,S} {3,S}
5   R u0 c0 {3,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 39,
    label = "N[+]=XR[-]O-X",
    group = 
"""
1 * X   u0 p0 c0 {3,D}
2   X   u0 p0 c0 {4,S}
3   N   u0 p0 c+1 {1,D} {4,S} {5,S}
4   O   u0 p2 c0 {2,S} {3,S}
5   R!H u0 p[1,2,3] c-1 {3,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 40,
    label = "RXbridgedBidentate",
    group = 
"""
1 * X   u0 {3,[S,D,T]}
2   X   u0 {4,[S,D,T]}
3   R!H ux {1,[S,D,T]} {5,[S,D,T]}
4   R!H ux {2,[S,D,T]} {5,[S,D,T]}
5   R!H ux {3,[S,D,T]} {4,[S,D,T]}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 41,
    label = "CXRCX",
    group = 
"""
1 * X   u0 {3,[S,D,T]}
2   X   u0 {4,[S,D,T]}
3   C   u0 {1,[S,D,T]} {5,[S,D,T]}
4   C   u0 {2,[S,D,T]} {5,[S,D,T]}
5   R!H u0 {3,[S,D,T]} {4,[S,D,T]}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 42,
    label = "C#X-R-C#X",
    group = 
"""
1 * X   u0 p0 c0 {3,T}
2   X   u0 p0 c0 {5,T}
3   C   u0 p0 c0 {1,T} {4,S}
4   R!H u0 c0 {3,S} {5,S}
5   C   u0 p0 c0 {2,T} {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 43,
    label = "C#X-R-C-XR2",
    group = 
"""
1 * X   u0 p0 c0 {3,T}
2   X   u0 p0 c0 {5,S}
3   C   u0 p0 c0 {1,T} {4,S}
4   R!H u0 c0 {3,S} {5,S}
5   C   u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
6   R   u0 c0 {5,S}
7   R   u0 c0 {5,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 44,
    label = "C#X-R-C=XR",
    group = 
"""
1 * X   u0 p0 c0 {3,T}
2   X   u0 p0 c0 {5,D}
3   C   u0 p0 c0 {1,T} {4,S}
4   R!H u0 c0 {3,S} {5,S}
5   C   u0 p0 c0 {2,D} {4,S} {6,S}
6   R   u0 p0 c0 {5,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 45,
    label = "C#X-R=C-XR",
    group = 
"""
1 * X   u0 p0 c0 {3,T}
2   X   u0 p0 c0 {5,S}
3   C   u0 p0 c0 {1,T} {4,S}
4   R!H u0 c0 {3,S} {5,D}
5   C   u0 p0 c0 {2,S} {4,D} {6,S}
6   R   u0 c0 {5,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 46,
    label = "C=X=R-C-XR2",
    group = 
"""
1 * X   u0 p0 c0 {3,D}
2   X   u0 p0 c0 {5,S}
3   C   u0 p0 c0 {1,D} {4,D}
4   R!H u0 c0 {3,D} {5,S}
5   C   u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
6   R   u0 c0 {5,S}
7   R   u0 c0 {5,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 47,
    label = "R2C-X-R-C-XR2",
    group = 
"""
1 * X   u0 p0 c0 {3,S}
2   X   u0 p0 c0 {5,S}
3   C   u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
4   R!H u0 c0 {3,S} {5,S}
5   C   u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
6   R   u0 c0 {5,S}
7   R   u0 c0 {5,S}
8   R   u0 c0 {3,S}
9   R   u0 c0 {3,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 48,
    label = "(OROR)X",
    group = 
"""
1 * X u0 p0 c0
2   O u0 p2 c0 {3,S} {4,S}
3   O u0 p2 c0 {2,S} {5,S}
4   R u0 p0 c0 {2,S}
5   R u0 p0 c0 {3,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 49,
    label = "RC-X=R-C-XR2",
    group = 
"""
1 * X   u0 p0 c0 {3,S}
2   X   u0 p0 c0 {5,S}
3   C   u0 p0 c0 {1,S} {4,D} {6,S}
4   R!H u0 c0 {3,D} {5,S}
5   C   u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
6   R   u0 c0 {3,S}
7   R   u0 c0 {5,S}
8   R   u0 c0 {5,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 50,
    label = "RC-X=R=C-XR",
    group = 
"""
1 * X   u0 p0 c0 {3,S}
2   X   u0 p0 c0 {5,S}
3   C   u0 p0 c0 {1,S} {4,D} {6,S}
4   R!H u0 p0 c0 {3,D} {5,D}
5   C   u0 p0 c0 {2,S} {4,D} {7,S}
6   R   u0 c0 {3,S}
7   R   u0 c0 {5,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 51,
    label = "RC-X=R=C=X",
    group = 
"""
1 * X   u0 p0 c0 {3,S}
2   X   u0 p0 c0 {5,D}
3   C   u0 p0 c0 {1,S} {4,D} {6,S}
4   R!H u0 p0 c0 {3,D} {5,D}
5   C   u0 p0 c0 {2,D} {4,D}
6   R   u0 c0 {3,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 52,
    label = "RC=X-R-C-XR2",
    group = 
"""
1 * X   u0 p0 c0 {3,D}
2   X   u0 p0 c0 {5,S}
3   C   u0 p0 c0 {1,D} {4,S} {6,S}
4   R!H u0 c0 {3,S} {5,S}
5   C   u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
6   R   u0 c0 {3,S}
7   R   u0 c0 {5,S}
8   R   u0 c0 {5,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 53,
    label = "RC=X-R-C=XR",
    group = 
"""
1 * X   u0 p0 c0 {3,D}
2   X   u0 p0 c0 {5,D}
3   C   u0 p0 c0 {1,D} {4,S} {6,S}
4   R!H u0 c0 {3,S} {5,S}
5   C   u0 p0 c0 {2,D} {4,S} {7,S}
6   R   u0 c0 {3,S}
7   R   u0 c0 {5,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 54,
    label = "RC=X-R=C-XR",
    group = 
"""
1 * X   u0 p0 c0 {3,D}
2   X   u0 p0 c0 {5,S}
3   C   u0 p0 c0 {1,D} {4,S} {6,S}
4   R!H u0 c0 {3,S} {5,D}
5   C   u0 p0 c0 {2,S} {4,D} {7,S}
6   R   u0 c0 {3,S}
7   R   u0 c0 {5,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 55,
    label = "CXROX",
    group = 
"""
1 * X   u0 {3,[S,D,T]}
2   X   u0 {4,S}
3   C   u0 {1,[S,D,T]} {5,[S,D,T]}
4   O   u0 p2 {2,S} {5,S}
5   R!H u0 {3,[S,D,T]} {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 56,
    label = "RC-X=R-O-X",
    group = 
"""
1 * X   u0 p0 c0 {3,S}
2   X   u0 p0 c0 {5,S}
3   C   u0 p0 c0 {1,S} {4,D} {6,S}
4   R!H u0 c0 {3,D} {5,S}
5   O   u0 p2 c0 {2,S} {4,S}
6   R   u0 c0 {3,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 57,
    label = "OXROX",
    group = 
"""
1 * X   u0 p0 c0 {3,S}
2   X   u0 p0 c0 {4,S}
3   O   u0 p2 c0 {1,S} {5,S}
4   O   u0 p2 c0 {2,S} {5,S}
5   R!H u0 c0 {3,S} {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 58,
    label = "O-X-C-O-X",
    group = 
"""
1 * X u0 p0 c0 {3,S}
2   X u0 p0 c0 {5,S}
3   O u0 p2 c0 {1,S} {4,S}
4   C u0 p0 c0 {3,S} {5,S}
5   O u0 p2 c0 {2,S} {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 59,
    label = "RXsingleChemisorbed",
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
    index = 60,
    label = "CX",
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
    index = 61,
    label = "C#XR",
    group = 
"""
1 * X u0 p0 c0 {2,T}
2   C u0 p0 c0 {1,T} {3,S}
3   R u0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 62,
    label = "C#XCR2",
    group = 
"""
1 * X   u0 p0 c0 {3,T}
2   C   u0 p0 c0 {3,S} {4,S} {5,D}
3   C   u0 p0 c0 {1,T} {2,S}
4   R   u0 c0 {2,S}
5   R!H u0 c0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 63,
    label = "C#XCR3",
    group = 
"""
1 * X u0 p0 c0 {3,T}
2   C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3   C u0 p0 c0 {1,T} {2,S}
4   R u0 c0 {2,S}
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
    index = 64,
    label = "C#XN",
    group = 
"""
1 * X u0 p0 c0 {2,T}
2   C u0 p0 c0 {1,T} {3,S}
3   N u0 p1 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 65,
    label = "C#XOR",
    group = 
"""
1 * X u0 p0 c0 {2,T}
2   C u0 p0 c0 {1,T} {3,S}
3   O u0 p2 c0 {2,S} {4,S}
4   R u0 c0 {3,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 66,
    label = "C-XR2",
    group = 
"""
1 * X   u0 p0 c0 {2,S}
2   C   u0 p0 c0 {1,S} {3,D} {4,S}
3   R!H u0 c0 {2,D}
4   R   u0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 67,
    label = "C-XRCR2",
    group = 
"""
1 * X u0 p0 c0 {2,S}
2   C u0 p0 c0 {1,S} {3,D} {4,S}
3   C u0 p0 c0 {2,D} {5,S} {6,S}
4   R u0 c0 {2,S}
5   R u0 c0 {3,S}
6   R u0 c0 {3,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 68,
    label = "C-XRN",
    group = 
"""
1 * X   u0 p0 c0 {2,S}
2   C   u0 p0 c0 {1,S} {3,S} {4,D}
3   N   u0 p1 c0 {2,S}
4   R!H u0 p[1,2,3] c0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 69,
    label = "C-XRNR",
    group = 
"""
1 * X u0 p0 c0 {2,S}
2   C u0 p0 c0 {1,S} {3,D} {4,S}
3   N u0 p1 c0 {2,D} {5,S}
4   R u0 c0 {2,S}
5   R u0 c0 {3,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 70,
    label = "C-XRO",
    group = 
"""
1 * X u0 p0 c0 {2,S}
2   C u0 p0 c0 {1,S} {3,D} {4,S}
3   O u0 p2 c0 {2,D}
4   R u0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 71,
    label = "C-XR3",
    group = 
"""
1 * X u0 p0 c0 {2,S}
2   C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3   R u0 c0 {2,S}
4   R u0 c0 {2,S}
5   R u0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 72,
    label = "C-XR2CR3",
    group = 
"""
1 * X u0 p0 c0 {2,S}
2   C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3   C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
4   R u0 c0 {2,S}
5   R u0 c0 {2,S}
6   R u0 c0 {3,S}
7   R u0 c0 {3,S}
8   R u0 c0 {3,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 73,
    label = "C-XR2N",
    group = 
"""
1 * X u0 p0 c0 {2,S}
2   C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3   N u0 p1 c0 {2,S}
4   R u0 c0 {2,S}
5   R u0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 74,
    label = "C-XR2OR",
    group = 
"""
1 * X u0 p0 c0 {2,S}
2   C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3   O u0 p2 c0 {2,S} {6,S}
4   R u0 c0 {2,S}
5   R u0 c0 {2,S}
6   R u0 c0 {3,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 75,
    label = "C=X(=R)",
    group = 
"""
1 * X   u0 p0 c0 {2,D}
2   C   u0 p0 c0 {1,D} {3,D}
3   R!H u0 c0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 76,
    label = "C=X(=C)",
    group = 
"""
1 * X u0 p0 c0 {2,D}
2   C u0 p0 c0 {1,D} {3,D}
3   C u0 p0 c0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 77,
    label = "C=X(=NR)",
    group = 
"""
1 * X u0 p0 c0 {2,D}
2   C u0 p0 c0 {1,D} {3,D}
3   N u0 p1 c0 {2,D} {4,S}
4   R u0 c0 {3,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 78,
    label = "C=XR2",
    group = 
"""
1 * X u0 p0 c0 {2,D}
2   C u0 p0 c0 {1,D} {3,S} {4,S}
3   R u0 c0 {2,S}
4   R u0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 79,
    label = "C=XRCR2",
    group = 
"""
1 * X   u0 p0 c0 {3,D}
2   C   u0 p0 c0 {3,S} {4,S} {5,D}
3   C   u0 p0 c0 {1,D} {2,S} {6,S}
4   R   u0 c0 {2,S}
5   R!H u0 c0 {2,D}
6   R   u0 c0 {3,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 80,
    label = "C=XRCR3",
    group = 
"""
1 * X u0 p0 c0 {3,D}
2   C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3   C u0 p0 c0 {1,D} {2,S} {7,S}
4   R u0 c0 {2,S}
5   R u0 c0 {2,S}
6   R u0 c0 {2,S}
7   R u0 c0 {3,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 81,
    label = "C=XRN",
    group = 
"""
1 * X u0 p0 c0 {2,D}
2   C u0 p0 c0 {1,D} {3,S} {4,S}
3   N u0 p1 c0 {2,S}
4   R u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 82,
    label = "C=XROR",
    group = 
"""
1 * X u0 p0 c0 {2,D}
2   C u0 p0 c0 {1,D} {3,S} {4,S}
3   O u0 p2 c0 {2,S} {5,S}
4   R u0 c0 {2,S}
5   R u0 c0 {3,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 83,
    label = "NX",
    group = 
"""
1 * X u0 {2,[S,D,T]}
2   N u0 {1,[S,D,T]}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 84,
    label = "N-XR",
    group = 
"""
1 * X   u0 p0 c0 {2,S}
2   N   u0 p1 c0 {1,S} {3,D}
3   R!H u0 c0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 85,
    label = "N-XCR",
    group = 
"""
1 * X   u0 p0 c0 {2,S}
2   N   u0 p1 c0 {1,S} {3,D}
3   C   u0 p0 c0 {2,D} {4,D}
4   R!H u0 c0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 86,
    label = "N-XCR2",
    group = 
"""
1 * X u0 p0 c0 {3,S}
2   C u0 p0 c0 {3,D} {4,S} {5,S}
3   N u0 p1 c0 {1,S} {2,D}
4   R u0 c0 {2,S}
5   R u0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 87,
    label = "N-XNR",
    group = 
"""
1 * X u0 p0 c0 {2,S}
2   N u0 p1 c0 {1,S} {3,D}
3   N u0 p1 c0 {2,D} {4,S}
4   R u0 c0 {3,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 88,
    label = "N-XR2",
    group = 
"""
1 * X   u0 p0 c0 {2,[S,D]}
2   N   u0 {1,[S,D]} {3,[S,D]} {4,[S,D]}
3   R!H u0 {2,[S,D]}
4   R   u0 c0 {2,[S,D]}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 89,
    label = "N-XRCR",
    group = 
"""
1 * X   u0 p0 c0 {2,S}
2   N   u0 p1 c0 {1,S} {3,S} {4,S}
3   C   u0 p0 c0 {2,S} {5,D}
4   R   u0 c0 {2,S}
5   R!H u0 c0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 90,
    label = "N-XRCR3",
    group = 
"""
1 * X u0 p0 c0 {3,S}
2   C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3   N u0 p1 c0 {1,S} {2,S} {7,S}
4   R u0 c0 {2,S}
5   R u0 c0 {2,S}
6   R u0 c0 {2,S}
7   R u0 c0 {3,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 91,
    label = "N-XRNR",
    group = 
"""
1 * X   u0 p0 c0 {2,S}
2   N   u0 p1 c0 {1,S} {3,S} {4,S}
3   N   u0 p1 c0 {2,S} {5,D}
4   R   u0 c0 {2,S}
5   R!H u0 c0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 92,
    label = "N-XRNR2",
    group = 
"""
1 * X u0 p0 c0 {2,S}
2   N u0 p1 c0 {1,S} {3,S} {4,S}
3   N u0 p1 c0 {2,S} {5,S} {6,S}
4   R u0 c0 {2,S}
5   R u0 c0 {3,S}
6   R u0 c0 {3,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 93,
    label = "N-XROR",
    group = 
"""
1 * X u0 p0 c0 {2,S}
2   N u0 p1 c0 {1,S} {3,S} {4,S}
3   O u0 p2 c0 {2,S} {5,S}
4   R u0 c0 {2,S}
5   R u0 c0 {3,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 94,
    label = "N[+]-XR[-]R",
    group = 
"""
1 * X   u0 p0 c0 {2,S}
2   N   u0 p0 c+1 {1,S} {3,S} {4,D}
3   R!H u0 p[1,2,3] c-1 {2,S}
4   R!H u0 c0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 95,
    label = "N[+]=XR[-]R",
    group = 
"""
1 * X   u0 p0 c0 {2,D}
2   N   u0 p0 c+1 {1,D} {3,S} {4,S}
3   R!H u0 p[1,2,3] c-1 {2,S}
4   R   u0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 96,
    label = "N=XR",
    group = 
"""
1 * X u0 p0 c0 {2,D}
2   N u0 p1 c0 {1,D} {3,S}
3   R u0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 97,
    label = "N=XC#R",
    group = 
"""
1 * X   u0 p0 c0 {2,D}
2   N   u0 p1 c0 {1,D} {3,S}
3   C   u0 p0 c0 {2,S} {4,T}
4   R!H u0 c0 {3,T}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 98,
    label = "N=XC-R",
    group = 
"""
1 * X u0 p0 c0 {3,D}
2   C u0 p0 c0 {3,S} {4,S}
3   N u0 p1 c0 {1,D} {2,S}
4   R u0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 99,
    label = "N=XN",
    group = 
"""
1 * X u0 p0 c0 {2,D}
2   N u0 p1 c0 {1,D} {3,S}
3   N u0 p1 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 100,
    label = "N=XOR",
    group = 
"""
1 * X u0 p0 c0 {2,D}
2   N u0 p1 c0 {1,D} {3,S}
3   O u0 p2 c0 {2,S} {4,S}
4   R u0 c0 {3,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 101,
    label = "OX",
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
    index = 102,
    label = "O-XR",
    group = 
"""
1 * X u0 p0 c0 {2,S}
2   O u0 p2 c0 {1,S} {3,S}
3   R u0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 103,
    label = "O-XCR2",
    group = 
"""
1 * X   u0 p0 c0 {3,S}
2   C   u0 p0 c0 {3,S} {4,S} {5,D}
3   O   u0 p2 c0 {1,S} {2,S}
4   R   u0 c0 {2,S}
5   R!H u0 c0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 104,
    label = "O-XCR3",
    group = 
"""
1 * X u0 p0 c0 {3,S}
2   C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3   O u0 p2 c0 {1,S} {2,S}
4   R u0 c0 {2,S}
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
    index = 105,
    label = "O-XN",
    group = 
"""
1 * X u0 p0 c0 {3,S}
2   N u0 p1 c0 {3,S}
3   O u0 p2 c0 {1,S} {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 106,
    label = "O-XOR",
    group = 
"""
1 * X u0 p0 c0 {2,S}
2   O u0 p2 c0 {1,S} {3,S}
3   O u0 p2 c0 {2,S} {4,S}
4   R u0 p0 c0 {3,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 107,
    label = "RXvdW",
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
    index = 108,
    label = "(CR2)X",
    group = 
"""
1 * X   u0
2   C   u0 {3,T} {4,S}
3   R!H u0 {2,T}
4   R   u0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 109,
    label = "(CRCR)X",
    group = 
"""
1 * X u0 p0 c0
2   C u0 p0 c0 {3,T} {4,S}
3   C u0 p0 c0 {2,T} {5,S}
4   R u0 c0 {2,S}
5   R u0 c0 {3,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 110,
    label = "(CRN)X",
    group = 
"""
1 * X u0 p0 c0
2   C u0 p0 c0 {3,T} {4,S}
3   N u0 p1 c0 {2,T}
4   R u0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 111,
    label = "(CR3)X",
    group = 
"""
1 * X   u0
2   C   u0 {3,D} {4,S} {5,S}
3   R!H u0 {2,D}
4   R   u0 {2,S}
5   R   u0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 112,
    label = "(CR2CR)X",
    group = 
"""
1 * X u0 p0 c0
2   C u0 p0 c0 {3,D} {4,S} {5,S}
3   C u0 p0 c0 {2,D} {6,S}
4   R u0 c0 {2,S}
5   R u0 c0 {2,S}
6   R u0 c0 {3,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 113,
    label = "(CR2N)X",
    group = 
"""
1 * X u0 p0 c0
2   C u0 p0 c0 {3,D} {4,S} {5,S}
3   N u0 p1 c0 {2,D}
4   R u0 c0 {2,S}
5   R u0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 114,
    label = "(CR2O)X",
    group = 
"""
1 * X u0 p0 c0
2   C u0 p0 c0 {3,D} {4,S} {5,S}
3   O u0 p2 c0 {2,D}
4   R u0 c0 {2,S}
5   R u0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 115,
    label = "(CR4)X",
    group = 
"""
1 * X u0 p0 c0
2   C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3   R u0 c0 {2,S}
4   R u0 c0 {2,S}
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
    index = 116,
    label = "(CR3CR3)X",
    group = 
"""
1 * X u0 p0 c0
2   C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3   C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4   R u0 c0 {2,S}
5   R u0 c0 {2,S}
6   R u0 c0 {2,S}
7   R u0 c0 {3,S}
8   R u0 c0 {3,S}
9   R u0 c0 {3,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 117,
    label = "(CR3N)X",
    group = 
"""
1 * X u0 p0 c0
2   C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3   N u0 p1 c0 {2,S}
4   R u0 c0 {2,S}
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
    index = 118,
    label = "(CR3OR)X",
    group = 
"""
1 * X u0 p0 c0
2   C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3   O u0 p2 c0 {2,S} {7,S}
4   R u0 c0 {2,S}
5   R u0 c0 {2,S}
6   R u0 c0 {2,S}
7   R u0 p0 c0 {3,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 119,
    label = "(N=C)X",
    group = 
"""
1 * X   u0 p0 c0
2   N   u0 p1 c0 {3,D} {4,S}
3   C   u0 p0 c0 {2,D} {5,D}
4   R   u0 p0 c0 {2,S}
5   R!H u0 p[1,2] c0 {3,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 120,
    label = "(NR3)X",
    group = 
"""
1 * X u0 p0 c0
2   N u0 p1 c0 {3,S} {4,S} {5,S}
3   R u0 c0 {2,S}
4   R u0 c0 {2,S}
5   R u0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 121,
    label = "(NN)X",
    group = 
"""
1 * X u0 p0 c0
2   N u0 p1 c0 {3,S} {4,S} {5,S}
3   N u0 p1 c0 {2,S}
4   R u0 c0 {2,S}
5   R u0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 122,
    label = "(NO)X",
    group = 
"""
1 * X u0 p0 c0
2   N u0 p1 c0 {3,S} {4,S} {5,S}
3   O u0 p2 c0 {2,S}
4   R u0 c0 {2,S}
5   R u0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 123,
    label = "(OR)X",
    group = 
"""
1 * X   u0 p0 c0
2   O   u0 p2 c0 {3,D}
3   R!H u0 p1 c0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 124,
    label = "(ONR)X",
    group = 
"""
1 * X u0 p0 c0
2   O u0 p2 c0 {3,D}
3   N u0 p1 c0 {2,D} {4,S}
4   R u0 c0 {3,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 125,
    label = "(ONN)X",
    group = 
"""
1 * X u0 p0 c0
2   O u0 p2 c0 {3,D}
3   N u0 p1 c0 {2,D} {4,S}
4   N u0 p2 c0 {3,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 126,
    label = "(ONOR)X",
    group = 
"""
1 * X u0 p0 c0
2   O u0 p2 c0 {3,D}
3   N u0 p1 c0 {2,D} {4,S}
4   O u0 p2 c0 {3,S} {5,S}
5   R u0 c0 {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 127,
    label = "(OR2)X",
    group = 
"""
1 * X u0 p0 c0
2   O u0 p2 c0 {3,S} {4,S}
3   R u0 p[0,1,2] c0 {2,S}
4   R u0 p[0,1,2] c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

