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
1 * R 0
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
1 * CO 0
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
1 * CO  						0 {2,S} {3,S} {4,D}
2   Os  						0 {1,S} {5,S}
3   {Cs,Cd,Cdd,Ct,Cb,Cbf,CO,H}  0 {1,S}
4   Od							0 {1,D}
5   R!H 						0 {2,S}
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
3   Os  0 {1,S} {6,S}
4   Od	0 {1,D}
5   R!H 0 {2,S}
6   R!H 0 {3,S}
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
1 * CO  						0 {2,S} {3,S} {4,D}
2   Os  						0 {1,S}, {5,S}
3   {Cs,Cd,Cdd,Ct,Cb,Cbf,CO,H}  0 {1,S}
4   Od							0 {1,D}
5   H   						0 {2,S}
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
1 * Cb 0 {2,S}
2   Cs 0 {1,S} {3,S}
3   Os 0 {2,S} {4,S}
4   H  0 {3,S}

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
1 * Os 0 {2,S} {3,S}
2   H  0 {1,S}
3   {Cb,Cbf} 0 {1,S}

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
1 * Os 0 {2,S} {3,S}
2   H 0 {1,S}
3   {Cs,Cd,Ct,CO,Os,H} 0 {1,S}

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
1 * Os 0 {2,S} {3,S}
2   R  0 {1,S} {3,{S,D,B}}
3   R  0 {1,S} {2,{S,D,B}}
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
1 * Os 0 {2,S} {4,S}
2   R  0 {1,S} {3,{S,D,B}}
3   R  0 {2,{S,D,B}} {4,{S,D,B}}
4   R  0 {1,S} {3,{S,D,B}}

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
1 * Os 0 {2,S} {5,S}
2   R  0 {1,S} {3,{S,D,B}}
3   R  0 {2,{S,D,B}} {4,{S,D,B}}
4   R  0 {3,{S,D,B}} {5,{S,D,B}}
5   R  0 {1,S} {4,{S,D,B}}
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
1 * Os 0 {2,S} {6,S}
2   R  0 {1,S} {3,{S,D,B}}
3   R  0 {2,{S,D,B}} {4,{S,D,B}}
4   R  0 {3,{S,D,B}} {5,{S,D,B}}
5   R  0 {4,{S,D,B}} {6,{S,D,B}}
6   R  0 {1,S} {5,{S,D,B}}

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
1 * Os 0 {2,S} {7,S}
2   R  0 {1,S} {3,{S,D,B}}
3   R  0 {2,{S,D,B}} {4,{S,D,B}}
4   R  0 {3,{S,D,B}} {5,{S,D,B}}
5   R  0 {4,{S,D,B}} {6,{S,D,B}}
6   R  0 {5,{S,D,B}} {7,{S,D,B}}
7   R  0 {1,S} {6,{S,D,B}}

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
1   Od 0 {2,D}
2 * CO 0 {1,D} {3,S} {4,S}
3   Os 0 {2,S} {4,S}
4   R!H 0 {2,S} {3,S}
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
1   Od 0 {2,D}
2 * CO 0 {1,D} {3,S} {5,S}
3   Os 0 {2,S} {4,S}
4   R!H 0 {5,S} {3,S}
5   R!H 0 {2,S} {4,S}
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
1   Od 0 {2,D}
2 * CO 0 {1,D} {3,S} {6,S}
3   Os 0 {2,S} {4,S}
4   R!H 0 {5,S} {3,S}
5   R!H 0 {4,S} {6,S}
6   R!H 0 {5,S} {2,S}
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
1   Od 0 {2,D}
2 * CO 0 {1,D} {3,S} {7,S}
3   Os 0 {2,S} {4,S}
4   R!H 0 {5,S} {3,S}
5   R!H 0 {4,S} {6,S}
6   R!H 0 {5,S} {7,S}
7   R!H 0 {6,S} {2,S}
""",
	solute = None,
	shortDesc = u"""lactone, 6 membered ring""",
	longDesc = 
u"""

"""
)

entry(
	index = 20,
	label = "Cd(Od)N",
	group = 
"""
1 * CO 		  {2,D} {3,S}
2   Od 		  {1,D}
3   {N3s,N3d} {1,S}

""",
	solute = SoluteData(
		S = 0.175,
		B = -0.287,
		E = 0.0,
		L = 0.603,
		A = 0.0
	),
	shortDesc = u"""Platts group 49 noncyclic aliphatic amide""",
	longDesc = 
u"""

"""
)

entry(
	index = 21,
	label = "Lactam",
	group = "OR{Lactam4, Lactam5, Lactam6, Lactam7}",
	solute = SoluteData(
		S = -0.1,
		B = -0.231,
		E = 0.061,
		L = 0.583,
		A = 0
	),
	shortDesc = u"""Platts group 50 lactam""",
	longDesc = 
u"""

"""
)

entry(
	index = 22,
	label = "Lactam4",
	group = 
"""
1   Od 0 {2,D}
2 * CO 0 {1,D} {3,S} {5,S}
3   N  0 {2,S} {4,S}
4   Cs 0 {5,S} {3,S}
5   Cs 0 {4,S} {1,S}
""",
	solute = None,
	shortDesc = u"""lactam, 4 membered ring""",
	longDesc = 
u"""

"""
)

entry(
	index = 23,
	label = "Lactam5",
	group = 
"""
1   Od 0 {2,D}
2 * CO 0 {1,D} {3,S} {6,S}
3   N  0 {2,S} {4,S}
4   Cs 0 {5,S} {3,S}
5   Cs 0 {4,S} {6,S}
6   Cs 0 {5,S} {1,S}
""",
	solute = None,
	shortDesc = u"""lactam, 5 membered ring""",
	longDesc = 
u"""

"""
)

entry(
	index = 24,
	label = "Lactam6",
	group = 
"""
1   Od 0 {2,D}
2 * CO 0 {1,D} {3,S} {7,S}
3   N  0 {2,S} {4,S}
4   Cs 0 {5,S} {3,S}
5   Cs 0 {4,S} {6,S}
6   Cs 0 {5,S} {7,S}
7   Cs 0 {6,S} {1,S}
""",
	solute = None,
	shortDesc = u"""lactam, 6 membered ring""",
	longDesc = 
u"""

"""
)

entry(
	index = 25,
	label = "Lactam7",
	group = 
"""
1   Od 0 {2,D}
2 * CO 0 {1,D} {3,S} {78,S}
3   N  0 {2,S} {4,S}
4   Cs 0 {5,S} {3,S}
5   Cs 0 {4,S} {6,S}
6   Cs 0 {5,S} {7,S}
7   Cs 0 {6,S} {8,S}
8   Cs 0 {7,S} {1,S}
""",
	solute = None,
	shortDesc = u"""lactam, 7 membered ring""",
	longDesc = 
u"""

"""
)

entry(
	index = 26,
	label = "SdOdOdN",
	group = 
"""
1 * Sd 0 {2,D} {3,D} {4,S}
2   Od 0 {1,D}
3   Od 0 {1,D}
4   N  0 {1,S}

""",
	solute = SoluteData(
		S = -0.569,
		B = -0.446,
		E = -0.111,
		L = 0.0,
		A = 0.356
	),
	shortDesc = u"""Platts group 51 sulfonamide -S(O)(O)N- (and fragment 13 for A)""",
	longDesc = 
u"""

"""
)

entry(
	index = 27,
	label = "NCd(Od)N",
	group = 
"""
1 * CO  0 {2,D} {3,S} {4,S}
2   Od  0 {1,D}
3   N3s 0 {1,S}
4   N3s 0 {1,S}

""",
	solute = SoluteData(
		S = -0.553,
		B = -0.076,
		E = -0.11,
		L = 0.0,
		A = 0.0
	),
	shortDesc = u"""Platts group 52 urea""",
	longDesc = 
u"""

"""
)

entry(
	index = 28,
	label = "OsCd(Od)N",
	group = 
"""
1 * CO  0 {2,D} {3,S} {4,S}
2   Od  0 {1,D}
3   Os  0 {1,S}
4   N3s 0 {1,S}

""",
	solute = SoluteData(
		S = -0.588,
		B = -0.252,
		E = 0.0,
		L = 0.0,
		A = -0.105
	),
	shortDesc = u"""Platts group 53 carbamate (fragment 16 for A)""",
	longDesc = 
u"""

"""
)

entry(
	index = 29,
	label = "Cd(Od)NCd(Od)",
	group = 
"""
1 * CO  0 {2,D} {3,S}
2   Od  0 {1,D}
3   N3s 0 {1,S} {4,S}
4   CO  0 {3,S} {5,D}
5   Od  0 {4,D}

""",
	solute = SoluteData(
		S = -0.51/2,
		B = -0.148/2,
		E = 0.0,
		L = 0.0,
		A = 0.0
	),
	shortDesc = u"""Platts group 54 imide""",
	longDesc = 
u"""

"""
)

entry(
	index = 30,
	label = "N3sH2-benz",
	group = 
"""
1 * N3s 0 {2,S} {3,S} {4,S}
2   H   0 [1,S}
3   H   0 {1,S}
4   Cb  0 {1,S} {5,B} {9,B}
5   Cb  0 {4,B} {6,B}
6   Cb  0 {5,B} {7,B}
7   Cb  0 {6,B} {8,B}
8   Cb  0 {7,B} {9,B}
9   Cb  0 {8,B} {4,B}
""",
	solute = SoluteData(
		S = 0.0,
		B = 0.0,
		E = 0.0,
		L = 0.0,
		A = 0.247
	),
	shortDesc = u"""aniline correction for A (fragment 4)""",
	longDesc = 
u"""

"""
)

entry(
	index = 31,
	label = "Cd(Od)NH2",
	group = 
"""
1 * N3s 0 {2,S} {3,S} {4,S}
2   H   0 {1,S}
3   H   0 {1,S}
4   CO  0 {1,S} {5,D}
5   Od  0 {4,D}
""",
	solute = SoluteData(
		S = 0.0,
		B = 0.0,
		E = 0.0,
		L = 0.0,
		A = 0.275
	),
	shortDesc = u"""primary amide correction for A (fragment 10)""",
	longDesc = 
u"""

"""
)

entry(
	index = 32,
	label = "Cd(Od)NHR",
	group = 
"""
1 * N3s 0 {2,S} {3,S} {4,S}
2   H   0 {1,S}
3   R!H 0 {1,S}
4   CO  0 {1,S} {5,D}
5   Od  0 {4,D}
""",
	solute = SoluteData(
		S = 0.0,
		B = 0.0,
		E = 0.0,
		L = 0.0,
		A = 0.281
	),
	shortDesc = u"""secondary amide correction for A (fragment 11)""",
	longDesc = 
u"""

"""
)

entry(
	index = 33,
	label = "Cd(Od)NH-arom",
	group = 
"""
1 * N3s 	0 {2,S} {3,S} {4,S}
2   H   	0 {1,S}
3   {Cb,Nb} 0 {1,S}
4   CO  	0 {1,S} {5,D}
5   Od  	0 {4,D}
""",
	solute = SoluteData(
		S = 0.0,
		B = 0.0,
		E = 0.0,
		L = 0.0,
		A = -0.091
	),
	shortDesc = u"""aromatic amide correction for A (fragment 12)""",
	longDesc = 
u"""

"""
)

entry(
	index = 34,
	label = "N3sHCd(Od)N3sH,
	group = 
"""
1 * N3s 	0 {2,S} {3,S}
2   H   	0 {1,S}
3   CO 		0 {1,S} {4,D} {5,S}
4   Od		0 {3,D}
5   N3s		0 {3,S} {6,S}
6   H       0 {5,S}
""",
	solute = SoluteData(
		S = 0.0,
		B = 0.0,
		E = 0.0,
		L = 0.0,
		A = -0.165
	),
	shortDesc = u"""urea correction for A (fragment 14)""",
	longDesc = 
u"""

"""
)
		
entry(
	index = 34,
	label = "N3sHCd(Od)N3sH",
	group = 
"""
1 * N3s 	0 {2,S} {3,S}
2   H   	0 {1,S}
3   CO 		0 {1,S} {4,D} {5,S}
4   Od		0 {3,D}
5   N3s		0 {3,S} {6,S}
6   H       0 {5,S}
""",
	solute = SoluteData(
		S = 0.0,
		B = 0.0,
		E = 0.0,
		L = 0.0,
		A = -0.165/2
	),
	shortDesc = u"""urea correction for A (fragment 14)""",
	longDesc = 
u"""

"""
)

entry(
	index = 35,
	label = "N3sCd(Od)N3sH",
	group = 
"""
1 * N3s 	0 {2,S} {3,S} {7,S}
2   R!H   	0 {1,S}
3   CO 		0 {1,S} {4,D} {5,S}
4   Od		0 {3,D}
5   N3s		0 {3,S} {6,S}
6   H       0 {5,S}
7   R!H		0 {1,S}
""",
	solute = SoluteData(
		S = 0.0,
		B = 0.0,
		E = 0.0,
		L = 0.0,
		A = -0.119
	),
	shortDesc = u"""urea correction for A (fragment 15)""",
	longDesc = 
u"""

"""
)
		
entry(
	index = 36,
	label = "CdsNdNsNs",
	group = 
"""
1 * Cd 	0 {2,D} {3,S} {4,S}
2   N3d 0 {1,D} {5,S}
3   N3s 0 {1,S} {6,S} {7,S}
4	N3s 0 {1,S} {8,S} {9,S}
5   H   0 {2,S}
6   H   0 {3,S}
7   H   0 {3,S}
8   H   0 {4,S}
9   H   0 {4,S}
""",
	solute = SoluteData(
		S = 0.0,
		B = 0.0,
		E = 0.0,
		L = 0.0,
		A = 0.17
	),
	shortDesc = u"""guanidine correction for A (fragment 17)""",
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
		L2: Cd(Od)N // amide
			L3: Lactam 
				L4: Lactam4
				L4: Lactam5
				L4: Lactam6
				L4: Lactam7
			L3: NCd(Od)N // urea
			L3: OsCd(Od)N // carbamate
			L3: Cd(Od)NCd(Od) // imide
				
	
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
	
	L1: SdOdOdN // sulfonamide
	
	L1: N3sH2-benz // aniline
	
	L1: Cd(Od)NH2 // primary amide
	L1: Cd(Od)NHR // secondary amide
			L2: Cd(Od)NH-arom // aromatic amide
	
	L1: N3sHCd(Od)N3sH // urea (with at least 2 H)
	L1: N3sCd(Od)N3sH // urea (noH on one side)
	
	L1: CdsNdNsNs // guanadine
"""
)