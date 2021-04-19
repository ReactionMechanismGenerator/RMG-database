#!/usr/bin/env python
# encoding: utf-8

name = "Radical Groups"
shortDesc = u"Radical corrections to A"
longDesc = u"""
H-bonding parameter A should be modified for when we saturate 
radical molecules with hydrogens and look up the saturated
structure.
"""

entry(
	index = 0,
	label = "R_rad",
	group = 
"""
1 * R u1
""",
	solute = None,
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1,
	label = "O_rad",
	group = 
"""
1 * O u1 p2
""",
	solute = None,
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 2,
	label = "ROJ",
	group = 
"""
1 * O u1 p2 c0 {2,S}
2   R u0 {1,S}
""",
	solute = SoluteData(
		S = 0.0,
		B = 0.0,
		E = 0.0,
		L = 0.0,
		A = -0.345,
	),
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 3,
	label = "ROOJ",
	group = 
"""
1 * O u1 p2 c0 {2,S}
2   O u0 p2 {1,S} {3,S}
3   R u0 {2,S}
""",
	solute = SoluteData(
		S = 0.0,
		B = 0.0,
		E = 0.0,
		L = 0.0,
		A = -0.345,
	),
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 4,
	label = "RC(O)OJ",
	group = 
"""
1 * O u1 p2 c0 {2,S}
2   C u0 p0 {1,S} {3,D} {4,S}
3   O u0 p2 {2,D}
4   R u0 {2,S}
""",
	solute = SoluteData(
		S = 0.0,
		B = 0.0,
		E = 0.0,
		L = 0.0,
		A = -0.243,
	),
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 5,
	label = "N3s_rad",
	group = 
"""
1 * N3s u1 p1 
""",
	solute = SoluteData(
		S = 0.0,
		B = 0.0,
		E = 0.0,
		L = 0.0,
		A = -0.087,
	),
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 6,
	label = "N3_pyrrole",
	group = 
"""
1 * N3s u1 p1 {2,S} {3,S}
2   Cb  u0 {1,S} {4,B}
3   Cb  u0 {1,S} {5,B}
4   Cb  u0 {2,B} {5,B}
5   Cb  u0 {3,B} {4,B}
""",
	solute = SoluteData(
		S = 0.0,
		B = 0.0,
		E = 0.0,
		L = 0.0,
		A = -0.371,
	),
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 7,
	label = "phenoxy",
	group = 
"""
1 * O  u1 p2 c0 {2,S}
2   Cb u0 {1,S}
""",
	solute = SoluteData(
		S = 0.0,
		B = 0.0,
		E = 0.0,
		L = 0.0,
		A = -0.543,
	),
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 8,
	label = "N3_aniline",
	group = 
"""
1 * N3s u1 p1 c0 {2,S} {3,S}
2   H   u0 p0 c0 {1,S}
3   Cb  u0 {1,S} {4,B} {5,B}
4   Cb  u0 {3,B} {6,B}
5   Cb  u0 {3,B} {7,B}
6   Cb  u0 {4,B} {8,B}
7   Cb  u0 {5,B} {8,B}
8   Cb  u0 {6,B} {7,B}
""",
	solute = SoluteData(
		S = 0.0,
		B = 0.0,
		E = 0.0,
		L = 0.0,
		A = -0.247,
	),
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 9,
	label = "N3_amide_pri",
	group = 
"""
1 * N3s u1 p1 c0 {2,S} {3,S}
2   H   u0 p0 c0 {1,S}
3   CO  u0 {1,S} {4,D}
4   O   u0 p2 {3,D}
""",
	solute = SoluteData(
		S = 0.0,
		B = 0.0,
		E = 0.0,
		L = 0.0,
		A = -0.275,
	),
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 10,
	label = "N3_amide_sec",
	group = 
"""
1 * N3s u1 p1 c0 {2,S} {3,S}
2   R!H u0 {1,S}
3   CO  u0 {1,S} {4,D}
4   O   u0 p2 {3,D}
""",
	solute = SoluteData(
		S = 0.0,
		B = 0.0,
		E = 0.0,
		L = 0.0,
		A = -0.281,
	),
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 11,
	label = "N3_amide_aromatic",
	group = 
"""
1 * N3s	  u1 p1 c0 {2,S} {3,S}
2   [Cb,N3b] u0 {1,S}
3   CO	   u0 {1,S} {4,D}
4   O		u0 p2 {3,D}
""",
	solute = SoluteData(
		S = 0.0,
		B = 0.0,
		E = 0.0,
		L = 0.0,
		A = 0.091,
	),
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 12,
	label = "N3_urea_pri",
	group = 
"""
1 * N3s u1 p1 c0 {2,S} {3,S}
2   R!H u0 p0 c0 {1,S}
3   CO  u0 {1,S} {4,D} {5,S}
4   O   u0 p2 {3,D}
5   N3s u0 p1 {3,S} {6,S}
6   H   u0 p0 c0 {5,S}
""",
	solute = SoluteData(
		S = 0.0,
		B = 0.0,
		E = 0.0,
		L = 0.0,
		A = 0.0825,
	),
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 13,
	label = "N3_urea_sec",
	group = 
"""
1 * N3s u1 p1 c0 {2,S} {3,S}
2   R!H u0 p0 c0 {1,S}
3   CO  u0 {1,S} {4,D} {5,S}
4   O   u0 p2 {3,D}
5   N3s u0 p1 {3,S} {6,S} {7,S}
6   R!H u0 {5,S}
7   R!H u0 {5,S}
""",
	solute = SoluteData(
		S = 0.0,
		B = 0.0,
		E = 0.0,
		L = 0.0,
		A = 0.119,
	),
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 14,
	label = "N3d_guanidine",
	group = 
"""
1   Cd  u0 {2,D} {3,S} {4,S}
2 * N3d u1 {1,D}
3   N3s u0 {1,S} {5,S} {6,S}
4   N3s u0 {1,S} {7,S} {8,S}
5   H   u0 {3,S}
6   H   u0 {3,S}
7   H   u0 {4,S}
8   H   u0 {4,S}
""",
	solute = SoluteData(
		S = 0.0,
		B = 0.0,
		E = 0.0,
		L = 0.0,
		A = -0.17
	),
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

tree(
"""
L1: R_rad
	L2: O_rad
		L3: ROJ
			L4: RC(O)OJ
			L4: ROOJ
			L4: phenoxy
	L2: N3s_rad
		L3: N3_pyrrole
		L3: N3_aniline
		L3: N3_amide_pri
			L4: N3_urea_pri
		L3: N3_amide_sec
			L4: N3_urea_pri
			L4: N3_urea_sec
			L4: N3_amide_aromatic
	L2: N3d_guanidine
"""
)

