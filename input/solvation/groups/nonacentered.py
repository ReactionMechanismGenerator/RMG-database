#!/usr/bin/env python
# encoding: utf-8

name = "Non Atom Centered Platts Groups"
shortDesc = u""
longDesc = u"""

"""

entry(
	index = -3,
	label = "R",
	group = 
"""
1 * R U0
""",
	solute = None,
	shortDesc = u"""""",
	longDesc = 
u"""

"""
)

entry(
	index = -2,
	label = "CO",
	group = 
"""
1 * CO U0
""",
	solute = None,
	shortDesc = u"""""",
	longDesc = 
u"""

"""
)

entry(
	index = 1,
	label = "Oss(CdsOd)",
	group = 
"""
1 * CO  						U0 {2,S} {3,S} {4,D}
2   Os  						U0 {1,S} {5,S}
3   {Cs,Cd,Cdd,Ct,Cb,Cbf,CO,H}  U0 {1,S}
4   Od							U0 {1,D}
5   R!H 						U0 {2,S}
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
1 * CO  U0 {2,S} {3,S} {4,D}
2   Os  U0 {1,S} {5,S}
3   Os  U0 {1,S} {6,S}
4   Od	U0 {1,D}
5   R!H U0 {2,S}
6   R!H U0 {3,S}
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
1 * CO  						U0 {2,S} {3,S} {4,D}
2   Os  						U0 {1,S}, {5,S}
3   {Cs,Cd,Cdd,Ct,Cb,Cbf,CO,H}  U0 {1,S}
4   Od							U0 {1,D}
5   H   						U0 {2,S}
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
1 * Cs U0 {2,S} {3,S} {4,S}, {5,S}
2   R  U0 {1,S}
3   R  U0 {1,S}
4   Os U0 {1,S} {6,S}
5   Cs U0 {1,S} {7,S} {8,S} (9,S}
6   H  U0 {4,S}
7   R  U0 {5,S}
8   R  U0 {5,S}
9   Os U0 {5,S} {10,S}
10  H  U0 {9,S}

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
1 * CO U0 {2,D} {3,S} {4,S}
2   Od U0 {1,D}
3   Cd U0 {1,S} {5,S} {6,D}
4   R  U0 {1,S}
5   R  U0 {3,S}
6   Cd U0 {3,D} {7,S} {8,S}
7   R  U0 {6,S}
8   CO U0 {6,S} {9,S} {10,D}
9   R  U0 {8,S}
10  Od U0 {8,D}

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
1 * Cb U0 {2,S}
2   Cs U0 {1,S} {3,S}
3   Os U0 {2,S} {4,S}
4   H  U0 {3,S}

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

entry(
	index = 7,
	label = "phenol",
	group = 
"""
1 * Os       U0 {2,S} {3,S}
2   H        U0 {1,S}
3   {Cb,Cbf} U0 {1,S}

""",
	solute = SoluteData(
		S = 0,
		B = 0,
		E = 0,
		L = 0,
		A = 0.543
	),
	shortDesc = u"""phenol correction for A""",
	longDesc = 
u"""

"""
)

entry(
	index = 8,
	label = "OssH",
	group = 
"""
1 * Os                 U0 {2,S} {3,S}
2   H                  U0 {1,S}
3   {Cs,Cd,Ct,CO,Os,H} U0 {1,S}

""",
	solute = SoluteData(
		S = 0,
		B = 0,
		E = 0,
		L = 0,
		A = 0.345
	),
	shortDesc = u"""-OH (connected to aliphatic) correction for A""",
	longDesc = 
u"""

"""
)

entry(
	index = 9,
	label = "OxRing",
	group = "OR{OxR3,OxR4,OxR5,OxR6,OxR7}",
	solute = SoluteData(
		S = 0,
		B = 0.12,
		E = -0.001,
		L = -0.001,
		A = 0
	),
	shortDesc = u"""Correction for an Oss group in a ring""",
	longDesc = 
u"""

"""
)

entry(
	index = 10,
	label = "OxR3",
	group = 
"""
1 * Os U0 {2,S} {3,S}
2   R  U0 {1,S} {3,{S,D,B}}
3   R  U0 {1,S} {2,{S,D,B}}
""",
	solute = None,
	shortDesc = u"""O in a 3 membered ring""",
	longDesc = 
u"""

"""
)

entry(
	index = 11,
	label = "OxR4",
	group = 
"""
1 * Os U0 {2,S} {4,S}
2   R  U0 {1,S} {3,{S,D,B}}
3   R  U0 {2,{S,D,B}} {4,{S,D,B}}
4   R  U0 {1,S} {3,{S,D,B}}

""",
	solute = None,
	shortDesc = u"""O in a 4 membered ring""",
	longDesc = 
u"""

"""
)

entry(
	index = 12,
	label = "OxR5",
	group = 
"""
1 * Os U0 {2,S} {5,S}
2   R  U0 {1,S} {3,{S,D,B}}
3   R  U0 {2,{S,D,B}} {4,{S,D,B}}
4   R  U0 {3,{S,D,B}} {5,{S,D,B}}
5   R  U0 {1,S} {4,{S,D,B}}
""",
	solute = None,
	shortDesc = u"""O in a 5 membered ring""",
	longDesc = 
u"""

"""
)

entry(
	index = 13,
	label = "OxR6",
	group = 
"""
1 * Os U0 {2,S} {6,S}
2   R  U0 {1,S} {3,{S,D,B}}
3   R  U0 {2,{S,D,B}} {4,{S,D,B}}
4   R  U0 {3,{S,D,B}} {5,{S,D,B}}
5   R  U0 {4,{S,D,B}} {6,{S,D,B}}
6   R  U0 {1,S} {5,{S,D,B}}

""",
	solute = None,
	shortDesc = u"""O in a 6 membered ring""",
	longDesc = 
u"""

"""
)

entry(
	index = 14,
	label = "OxR7",
	group = 
"""
1 * Os U0 {2,S} {7,S}
2   R  U0 {1,S} {3,{S,D,B}}
3   R  U0 {2,{S,D,B}} {4,{S,D,B}}
4   R  U0 {3,{S,D,B}} {5,{S,D,B}}
5   R  U0 {4,{S,D,B}} {6,{S,D,B}}
6   R  U0 {5,{S,D,B}} {7,{S,D,B}}
7   R  U0 {1,S} {6,{S,D,B}}

""",
	solute = None,
	shortDesc = u"""O in a 7 membered ring""",
	longDesc = 
u"""

"""
)

entry(
	index = 15,
	label = "Lac",
	group = "OR{Lac3, Lac4, Lac5, Lac6}",
	solute = SoluteData(
		S = 0.36,
		B = -0.214,
		E = 0,
		L = 0.406,
		A = 0
	),
	shortDesc = u"""Platts group 44 lactone""",
	longDesc = 
u"""

"""
)

entry(
	index = 16,
	label = "Lac3",
	group = 
"""
1   Od  U0 {2,D}
2 * CO  U0 {1,D} {3,S} {4,S}
3   Os  U0 {2,S} {4,S}
4   R!H U0 {2,S} {3,S}
""",
	solute = None,
	shortDesc = u"""lactone, 3 membered ring""",
	longDesc = 
u"""

"""
)

entry(
	index = 17,
	label = "Lac4",
	group = 
"""
1   Od  U0 {2,D}
2 * CO  U0 {1,D} {3,S} {5,S}
3   Os  U0 {2,S} {4,S}
4   R!H U0 {5,S} {3,S}
5   R!H U0 {2,S} {4,S}
""",
	solute = None,
	shortDesc = u"""lactone, 4 membered ring""",
	longDesc = 
u"""

"""
)

entry(
	index = 18,
	label = "Lac5",
	group = 
"""
1   Od  U0 {2,D}
2 * CO  U0 {1,D} {3,S} {6,S}
3   Os  U0 {2,S} {4,S}
4   R!H U0 {5,S} {3,S}
5   R!H U0 {4,S} {6,S}
6   R!H U0 {5,S} {2,S}
""",
	solute = None,
	shortDesc = u"""lactone, 5 membered ring""",
	longDesc = 
u"""

"""
)

entry(
	index = 19,
	label = "Lac6",
	group = 
"""
1   Od  U0 {2,D}
2 * CO  U0 {1,D} {3,S} {7,S}
3   Os  U0 {2,S} {4,S}
4   R!H U0 {5,S} {3,S}
5   R!H U0 {4,S} {6,S}
6   R!H U0 {5,S} {7,S}
7   R!H U0 {6,S} {2,S}
""",
	solute = None,
	shortDesc = u"""lactone, 6 membered ring""",
	longDesc = 
u"""

"""
)




tree(
"""
L0: R

	L1: CO
		L2: Oss(CdsOd) // ester
		    L3: Lac // lactone
		        L4: Lac3
		        L4: Lac4
		        L4: Lac5
		        L4: Lac6
		L2: Oss(CdsOd)Oss // carbonate
		L2: OssH(CdsOd) // carboxylic acid
		L2: Cd(Od)Cd=CdCd(Od) // quinone
	
	L1: Cs(OssH)Cs(OssH) // 1,2 diol
		
	L1: CbCsOssH // benzyl alcohol
	
	L1: OssH
	
	L1: phenol
	
	L1: OxRing
	    L2: OxR3
	    L2: OxR4
	    L2: OxR5
	    L2: OxR6
	    L2: OxR7
	    
"""
)