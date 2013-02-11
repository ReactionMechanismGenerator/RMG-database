#!/usr/bin/env python
# encoding: utf-8

name = "Non Atom Centered Platts Groups"
shortDesc = u""
longDesc = u"""

"""

entry(
	index = 1,
	label = "Oss(CdsOd)",
	group = 
"""
1 * CO  0 {2,S} {3,S} {4,D}
2   Os  0 {1,S} {5,S}
3   {Cs, Cd, Cdd, Ct, Cb, Cbf, CO, H}   0 {1,S}
4   Od	0 {1,D}
5   R!H 0 {2,S}
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
2   Os  0 {1,S} {5,S}
3   Os  0 {1,S}
4   Od	0 {1,D}
5   R!H 0 {2,S}
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
	label = "OssH(CdsOd)",
	group = 
"""
1 * CO  0 {2,S} {3,S} {4,D}
2   Os  0 {1,S}, {5,S}
3   {Cs, Cd, Cdd, Ct, Cb, Cbf, CO, H}   0 {1,S}
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
	label = "Cs(OssH)Cs(OssH)",
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
		S = 0.052/2,
		B = 0,
		E = -0.043/2,
		L = 0.1/2,
		A = 0
	),
	shortDesc = u"""Platts fragment 68 1,2 diol""",
	longDesc = 
u"""

"""
)

entry(
	index = 5,
	label = "Cd(Od)Cd=CdCd(Od)",
	group = 
"""
1 * CO 0 {2,D} {3,S} {4,S}
2   Od 0 {1,D}
3   Cd 0 {1,S} {5,S} {6,D}
4   R  0 {1,S}
5   R  0 {3,S}
6   Cd 0 {3,D} {7,S} {8,S}
7   R  0 {6,S}
8   CO 0 {6,S} {9,S} {10,D}
9   R  0 {8,S}
10  Od 0 {8,D}

""",
	solute = SoluteData(
		S = -0.411/2,
		B = -0.051/2,
		E = 0,
		L = 0,
		A = 0
	),
	shortDesc = u"""Platts fragment 55 quinone""",
	longDesc = 
u"""

"""
)

entry(
	index = 6,
	label = "CbCsOssH",
	group = 
"""
1 * Cb {2,S}
2   Cs {1,S} {3,S}
3   Os {2,S} {4,S}
4   H  {3,S}

""",
	solute = SoluteData(
		S = 0,
		B = 0.131,
		E = 0,
		L = -0.145,
		A = 0
	),
	shortDesc = u"""Platts fragment 79 benzyl alcohol""",
	longDesc = 
u"""

"""
)



tree(
"""
L0: R

	L1: CO
		L2: Oss(CdsOd) // non-cyclic ester
		L2: Oss(CdsOd)Oss // carbonate
		L2: OssH(CdsOd) // carboxylic acid
		L2: Cd(Od)Cd-CdCd(Od) // quinone
	
	L1: Cs
		L2: Cs(OssH)Cs(OssH) // 1,2 diol
		
	L1: Cb
		L2: CbCsOssH // benzyl alcohol

"""
)