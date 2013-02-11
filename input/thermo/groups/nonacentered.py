#!/usr/bin/env python
# encoding: utf-8

name = "Non Atom Centered Platts Groups"
shortDesc = u""
longDesc = u"""

"""

entry(
	index = 1,
	label = "Oss(CdsOd)R",
	group = 
"""
1 * CO  0 {2,S} {3,S} {4,D}
2   Os  0 {1,S}
3   R   0 {1,S}
4   Od	0 {1,D}
""",
	solute = SoluteData(
		S = -0.225,
		B = -0.206,
		E = -0.113,
		L = -0.39,
		A =  0
	),
	shortDesc = u"""Platts fragment 43 non-cyclic ester""",
	longDesc = 
u"""

"""
)

entry(
	index = 2,
	label = "Oss(CdsOd)Oss",
	group = 
"""
1 * CO  0 {2,S} {3,S} {4,D}
2   Os  0 {1,S}
3   Os  0 {1,S}
4   Od	0 {1,D}
""",
	solute = SoluteData(
		S = -0.19,
		B = -0.267,
		E =  0,
		L =  0,
		A =  0
	),
	shortDesc = u"""Platts fragment 46 carbonate""",
	longDesc = 
u"""

"""
)

entry(
	index = 3,
	label = "OssH(CdsOd)R",
	group = 
"""
1 * CO  0 {2,S} {3,S} {4,D}
2   Os  0 {1,S}, {5,S}
3   R   0 {1,S}
4   Od	0 {1,D}
5   H   0 {2,S}
""",
	solute = SoluteData(
		S = -0.412,
		B = -0.308,
		E = -0.192,
		L = -0.369,
		A =  0.243
	),
	shortDesc = u"""Platts fragment 47 carboxylic acid""",
	longDesc = 
u"""

"""
)

entry(
	index = 4,
	label = "RRCs(OssH)Cs(OssH)RR",
	group = 
"""
1 * Cs 0 {2,S} {3,S} {4,S}, {5,S}
2   R  0 {1,S}
3   R  0 {1,S}
4   Os 0 {1,S} {6,S}
5   Cs 0 {1,S} {7,S} {8,S} (9,S}
6   H  0 {4,S}
7   R  0 {5,S}
8   R  0 {5,S}
9   Os 0 {5,S} {10,S}
10  H  0 {9,S}

""",
	solute = SoluteData(
		S = 0.052,
		B = 0,
		E = -0.043,
		L = 0.1,
		A = 0
	),
	shortDesc = u"""Platts fragment 68 1,2 diol""",
	longDesc = 
u"""

"""
)

tree(
"""
L0: R

	L1: CO
		L1: Oss(CdsOd)R // non-cyclic ester
		L1: Oss(CdsOd)Oss // carbonate
		L1: OssH(CdsOd)R // carboxylic acid
	
	L1: RRCs(OssH)Cs(OssH)RR // 1,2 diol

"""
)