#!/usr/bin/env python
# encoding: utf-8

name = "Abraham Solute Descriptors"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "CssH3",
    group = 
"""
1 * Css 0 {2,S} {3,S} {4,S}
2   H   0 {1,S}
3   H   0 {1,S}
4   H   0 {1,S}
""",
    solute = SoluteData(
        S = -0.075,
		 B =  0.007,
		 E = -0.104,
		 L =  0.321,
		 A =  0
    ),
    shortDesc = u"""Platts fragment 1 sp3 CH3""",
    longDesc = 
u"""

""",
    history = [
        ("Imported Sat Jan 5 2013"),
    ],
)

entry(
    index = 2,
    label = "CssH2",
    group = 
"""
1 * Css 0 {2,S} {3,S}
2   H   0 {1,S}
3   H   0 {1,S}
""",
    solute = SoluteData(
        S =  0,
		 B =  0,
		 E =  0,
		 L =  0.499,
		 A =  0
    ),
    shortDesc = u"""Platts fragment 2 sp3 >CH2""",
    longDesc = 
u"""

""",
    history = [
        ("Imported Sat Jan 5 2013"),
    ],
)

entry(
    index = 3,
    label = "CssH",
    group = 
"""
1 * Css 0 {2,S}
2   H   0 {1,S}

""",
    solute = SoluteData(
        S =  0.036,
		 B =  0.011,
		 E =  0.089,
		 L =  0.499,
		 A =  0
    ),
    shortDesc = u"""  """,
    longDesc = 
u"""

""",
    history = [
        ("Imported Sat Jan 5 2013"),
    ],
)



tree(
"""
L0: R

L1: C

	L2: Cbf
	
	L2: Css
		L3: CssH3
		L3: CssH2
			L4: Css(OssH)-Css(OssH)
		L3: CssH
			L4: Css(OssH)-Css(OssH)
		L3: Css-noH
			L4: Css(OssH)-Css(OssH)
	
	L2: Cds
		L3: CdsH2
		L3: CdsH
			L4: Oss(CdsOd)
				L5: Cds(Od)OssH
			L4: Cds(Od)Cds=CdsCds(Od)
			L4: Cds*(Od)Cds=CdsCds(Od)

		L3: Cds-noH
			L4: Oss(CdsOd)
				L5: OssCds(Od)Oss
			L4: Cds(Od)OssH
			L4: Cds(Od)Cds=CdsCds(Od)
			L4: Cds*(Od)Cds=CdsCds(Od)
		
	L2: Ct
	L2: Cb
	L2: Cdd

L1: O

	L2: Oss
		L3: OssH           // Hydroxyl group
			
		L3: Oss*Cds(Od)Oss // Carbonate
		L3: OssCds(Od)Oss* // Carbonate
		
		L3: Css(Oss*H)-Css(OssH) // 1,2-diol
		L3: Oss-noncyclic
		
    L2: Od
    	
    	L3: OssCds(Od*)Oss // Carbonate
    	
    	L3: Cds(Od*)Cds=CdsCds(Od) // Quinone
"""
)