#!/usr/bin/env python
# encoding: utf-8

name = "Abraham Solute Descriptors"
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
	label = "C",
	group = 
"""
1 * C 0
""",
	solute = None,
	shortDesc = u"""""",
	longDesc = 
u"""

"""
)

entry(
	index = -1,
	label = "Css",
	group = 
"""
1 * Cs 0
""",
	solute = None,
	shortDesc = u"""""",
	longDesc = 
u"""

"""
)

entry(
	index = 0,
	label = "Cds",
	group = 
"""
1 * Cd 0
""",
	solute = None,
	shortDesc = u"""""",
	longDesc = 
u"""

"""
)

entry(
    index = 1,
    label = "CssH3",
    group = 
"""
1 * Cs  0 {2,S} {3,S} {4,S}
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

"""
)

entry(
    index = 2,
    label = "CssH2",
    group = 
"""
1 * Cs  0 {2,S} {3,S} {4,S}
2   H   0 {1,S}
3   H   0 {1,S}
4   R!H   0 {1,S}
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

"""
)

entry(
    index = 3,
    label = "CssH",
    group = 
"""
1 * Cs  0 {2,S} {3,S} {4,S}
2   H   0 {1,S}
3   R!H   0 {1,S}
4   R!H   0 {1,S}

""",
    solute = SoluteData(
        S =  0.036,
		 B =  0.011,
		 E =  0.089,
		 L =  0.499,
		 A =  0
    ),
    shortDesc = u"""Platts fragment 3 sp3 >CH-""",
    longDesc = 
u"""

"""
)

entry(
	index = 4,
	label = "Css-noH",
	group = 
"""
1 * Cs 0 {2,S} {3,S} {4,S}
2   R!H   0 {1,S}
3   R!H   0 {1,S}
4   R!H   0 {1,S}

""",
	solute = SoluteData(
		 S =  0.071,
		 B =  0.037,
		 E =  0.187,
		 L =  0.443,
		 A =  0
	),
	shortDesc = u"""Platts fragment 4 sp3 >C<""",		longDesc = 
u"""

"""
)

entry(
	index = 5,
	label = "CdsH2",
	group = 
"""
1 * Cd 0 {2,S} {3,S} {4,D}
2   H 0 {1,S}
3   H 0 {1,S}
4   R!H 0 {1,D}

""",
	solute = SoluteData(
		 S =  -0.085,
		 B =  0.019,
		 E =  -0.045,
		 L =  0.244,
		 A =  0,
	),
	shortDesc = u"""Platts' fragment 5 sp2 =CH2""",
	longDesc = 
u"""

"""
)

entry(
	index = 6,
	label = "CdsH",
	group = 
"""
1 * Cd 0 {2,S} {3,S} {4,D}
2   H 0 {1,S}
3   R!H 0 {1,S}
4   R!H 0 {1,D}

""",
	solute = SoluteData(
		 S =  0.05,
		 B =  0.011,
		 E =  0.068,
		 L =  0.469,
		 A =  0,
	),
	shortDesc = u"""Platts' fragment 6 sp2 =CH-""",
	longDesc = 
u"""

"""
)

entry(
	index = 7,
	label = "Cds-noH",
	group = 
"""
1 * Cd 0 {2,S} {3,S} {4,D}
2   R!H 0 {1,S}
3   R!H 0 {1,S}
4   R!H 0 {1,D}

""",
	solute = SoluteData(
		 S =  0.101,
		 B =  0,
		 E =  0.18,
		 L =  0.624,
		 A =  0,
	),
	shortDesc = u"""Platts' fragment 7 sp2 =C<""",
	longDesc = 
u"""

"""
)

entry(
	index = 8,
	label = "Cbf",
	group = 
"""
1 * Cbf 0

""",
	solute = SoluteData(
		 S =  0.121,
		 B =  0.019,
		 E =  0.3,
		 L =  0.744,
		 A =  0,
	),
	shortDesc = u"""Platts' fragment 8 fused aromatic""",
	longDesc = 
u"""

"""
)

entry(
	index = 9,
	label = "Ct",
	group = 
"""
1 * Ct 0

""",
	solute = SoluteData(
		 S =  0.034,
		 B =  0.028,
		 E =  0.04,
		 L =  0.332,
		 A =  0,
	),
	shortDesc = u"""Platts' fragment 9 sp""",
	longDesc = 
u"""

"""
)

entry(
	index = 24,
	label = "O",
	group = 
"""
1 * O 0
""",
	solute = None,
	shortDesc = u"""""",
	longDesc = 
u"""

"""
)

entry(
	index = 25,
	label = "Oss",
	group = 
"""
1 * Os 0
""",
	solute = None,
	shortDesc = u"""""",
	longDesc = 
u"""

"""
)


entry(
	index = 26,
	label = "OssH",
	group = 
"""
1 * Os 0 {2,S}
2   H 0 {1,S}

""",
	solute = SoluteData(
		 S =  0.247,
		 B =  0.307,
		 E =  0.061,
		 L =  0.672,
		 A =  0.345
	),
	shortDesc = u"""Platts fragment 26 -OH""",
	longDesc = 
u"""

"""
)

entry(
	index = 27,
	label = "Oss-noncyclic",
	group = 
"""
1 * Os 0 {2,S} {3,S}
2   R!H 0 {1,S}
3   R!H 0 {1,S}

""",
	solute = SoluteData(
		 S =  0.185,
		 B =  0.211,
		 E =  0.014,
		 L =  0.360,
		 A =  0
	),
	shortDesc = u"""Platts fragment 27 noncyclic -O-""",
	longDesc = 
u"""

"""
)

entry(
	index = 28,
	label = "Oss-cyclic",
	group = 
"""
1 * Os 0 {2,S} {3,S}
2   R!H 0 {1,S} {3,S}
3   R!H 0 {1,S} {2,S}

""",
	solute = SoluteData(
		 S =  0.185,
		 B =  0.331,
		 E =  0.013,
		 L =  0.359,
		 A =  0
	),
	shortDesc = u"""Platts fragment 28 cyclic -O-""",
	longDesc = 
u"""

"""
)

entry(
	index = 30,
	label = "Od",
	group = 
"""
1 * Od 0

""",
	solute = SoluteData(
		 S =  0.370,
		 B =  0.334,
		 E =  -0.041,
		 L =  0.495,
		 A =  0
	),
	shortDesc = u"""Platts fragment 30 sp2 =O""",
	longDesc = 
u"""

"""
)

entry(
	index = 43,
	label = "Oss(CdsOd)",
	group = 
"""
1 * CO 0 {2,S} {3,D}
2   Os 0 {1,S}
3   Od 0 {1,D}

""",
	solute = SoluteData(
		 S =  -0.225,
		 B =  -0.206,
		 E =  -0.113,
		 L =  -0.39,
		 A =  0
	),
	shortDesc = u"""Platts' fragment 43 non-cyclic ester""",
	longDesc = 
u"""

"""
)

entry(
	index = 46,
	label = "OssCds(Od)Oss",
	group = 
"""
1 * CO 0 {2,S} {3,S} {4,D}
2   Os 0 {1,S}
3   Os 0 {1,S}
4   Od 0 {1,D}

""",
	solute = SoluteData(
		 S =  0.014,
		 B =  -0.025,
		 E =  -0.138,
		 L =  1.08,
		 A =  0.243
	),
	shortDesc = u"""Platts' fragment 46 carbonate""",
	longDesc = 
u"""

"""
)

entry(
	index = 47,
	label = "Cds(Od)OssH",
	group = 
"""
1 * CO 0 {2,S} {4,D}
2   Os 0 {1,S} {3,S}
3   H 0 {2,S}
4   Od 0 {1,D}

""",
	solute = SoluteData(
		 S =  -0.412,
		 B =  -0.308,
		 E =  -0.192,
		 L =  -0.369,
		 A =  0.243
	),
	shortDesc = u"""Platts fragment 47 carboxylic acid -CO2H""",
	longDesc = 
u"""

"""
)



entry(
	index = 55,
	label = "Cds(Od)Cds=CdsCds(Od)",
	group = 
"""
1 * Cd 0 {2,D} {3,S}
2   Cd 0 {1,D} {4,S}
3   CO 0 {1,S} {5,D}
4   CO 0 {2,S} {6,D}
5   Od 0 {3,D}
6   Od 0 {4,D}

""",
	solute = SoluteData(
		 S =  -0.411,
		 B =  -0.051,
		 E =  0,
		 L =  0,
		 A =  0
	),
	shortDesc = u"""Platts fragment 55 quinone""",
	longDesc = 
u"""

"""
)

entry(
	index = 68,
	label = "Css(OssH)-Css(OssH)",
	group = 
"""
1 * Cs 0 {2,S} {4,S}
2   Os 0 {1,S} {3,S}
3   H 0 {2,S}
4   Cs 0 {5,S} {1,S}
5   Os 0 {4,S} {6,S}
6   H 0 {5,S}

""",
	solute = SoluteData(
		 S =  0.052,
		 B =  0,
		 E =  -0.043,
		 L =  0.1,
		 A =  0
	),
	shortDesc = u"""Platts fragment 68 1,2-diol""",
	longDesc = 
u"""

"""
)

entry(
	index = 69,
	label = "Cds*(Od)Cds=CdsCds(Od)",
	group = 
"""
1   Cd 0 {2,D} {3,S}
2   Cd 0 {1,D} {4,S}
3 * CO 0 {1,S} {5,D}
4   CO 0 {2,S} {6,D}
5   Od 0 {3,D}
6   Od 0 {4,D}
""",
	solute = SoluteData(
		 S =  0.0,
		 B =  0.0,
		 E =  0.0,
		 L =  0.0,
		 A =  0.0
	),
	shortDesc = u"""same as 55""",
	longDesc = 
u"""

"""
)

entry(
	index = 70,
	label = "Cds(Od*)Cds=CdsCds(Od)",
	group = 
"""
1   Cd 0 {2,D} {3,S}
2   Cd 0 {1,D} {4,S}
3   CO 0 {1,S} {5,D}
4   CO 0 {2,S} {6,D}
5 * Od 0 {3,D}
6   Od 0 {4,D}
""",
	solute = SoluteData(
		 S =  0.0,
		 B =  0.0,
		 E =  0.0,
		 L =  0.0,
		 A =  0.0
	),
	shortDesc = u"""same as 55""",
	longDesc = 
u"""

"""
)


entry(
	index = 71,
	label = "Oss*Cds(Od)Oss",
	group = 
"""
1   CO 0 {2,S} {3,S} {4,D}
2 * Os 0 {1,S}
3   Os 0 {1,S}
4   Od 0 {1,D}

""",
	solute = SoluteData(
		 S =  0.0,
		 B =  0.0,
		 E =  0.0,
		 L =  0.0,
		 A =  0.0
	),
	shortDesc = u"""same as 46""",
	longDesc = 
u"""

"""
)

entry(
	index = 72,
	label = "OssCds(Od*)Oss",
	group = 
"""
1   CO 0 {2,S} {3,S} {4,D}
2   Os 0 {1,S}
3   Os 0 {1,S}
4 * Od 0 {1,D}

""",
	solute = SoluteData(
		 S =  0.0,
		 B =  0.0,
		 E =  0.0,
		 L =  0.0,
		 A =  0.0
	),
	shortDesc = u"""same as 46""",
	longDesc = 
u"""

"""
)

entry(
	index = 73,
	label = "Css(Oss*H)-Css(OssH)",
	group = 
"""
1   Cs 0 {2,S} {4,S}
2 * Os 0 {1,S} {3,S}
3   H 0 {2,S}
4   Cs 0 {5,S} {1,S}
5   Os 0 {4,S} {6,S}
6   H 0 {5,S}

""",
	solute = SoluteData(
		 S =  0.0,
		 B =  0.0,
		 E =  0.0,
		 L =  0.0,
		 A =  0.0
	),
	shortDesc = u"""same as 68""",
	longDesc = 
u"""

"""
)



entry(
	index = 74,
	label = "Cb",
	group = 
"""
1 * Cb 0

""",
	solute = SoluteData(
		 S =  0.05,
		 B =  0.011,
		 E =  0.068,
		 L =  0.469,
		 A =  0,
	),
	shortDesc = u"""Platts' fragment 6 aromatic =CH-""",
	longDesc = 
u"""

"""
)

entry(
	index = 75,
	label = "Cdd",
	group = 
"""
1 * Cd 0

""",
	solute = SoluteData(
		 S =  0.101,
		 B =  0,
		 E =  0.18,
		 L =  0.624,
		 A =  0,
	),
	shortDesc = u"""Platts' fragment 7 nonfused aromatic =C<""",
	longDesc = 
u"""

"""
)

entry(
	index = 76,
	label = "Oss*(CdsOd)",
	group = 
"""
1   CO 0 {2,S} {3,D}
2 * Os 0 {1,S}
3   Od 0 {1,D}

""",
	solute = SoluteData(
		 S =  0.0,
		 B =  0.0,
		 E =  0.0,
		 L =  0.0,
		 A =  0.0
	),
	shortDesc = u"""same as 43""",
	longDesc = 
u"""

"""
)

entry(
	index = 77,
	label = "Oss(CdsOd*)",
	group = 
"""
1   CO 0 {2,S} {3,D}
2   Os 0 {1,S}
3 * Od 0 {1,D}

""",
	solute = SoluteData(
		 S =  0.0,
		 B =  0.0,
		 E =  0.0,
		 L =  0.0,
		 A =  0.0
	),
	shortDesc = u"""same as 43""",
	longDesc = 
u"""

"""
)



entry(
	index = 79,
	label = "CbCssOssH",
	group = 
"""
1 * Cb 0 {2,S}
2   Cs 0 {1,S} {3,S}
3   Os 0 {2,S} {4,S}
4   H  0 {3,S} 

""",
	solute = SoluteData(
		 S =  0,
		 B =  0.131,
		 E =  0,
		 L =  0,
		 A =  0
	),
	shortDesc = u"""Platts' fragment 79 benzyl alcohol""",
	longDesc = 
u"""

"""
)

entry(
	index = 80,
	label = "CbCss*OssH",
	group = 
"""
1   Cb 0 {2,S}
2 * Cs 0 {1,S} {3,S}
3   Os 0 {2,S} {4,S}
4   H  0 {3,S} 

""",
	solute = SoluteData(
		 S =  0.0,
		 B =  0.0,
		 E =  0.0,
		 L =  0.0,
		 A =  0.0
	),
	shortDesc = u"""same as 79""",
	longDesc = 
u"""

"""
)

entry(
	index = 81,
	label = "CbCssOss*H",
	group = 
"""
1   Cb 0 {2,S}
2   Cs 0 {1,S} {3,S}
3 * Os 0 {2,S} {4,S}
4   H  0 {3,S} 

""",
	solute = SoluteData(
		 S =  0.0,
		 B =  0.0,
		 E =  0.0,
		 L =  0.0,
		 A =  0.0
	),
	shortDesc = u"""same as 79""",
	longDesc = 
u"""

"""
)

entry(
	index = 82,
	label = "Cds(Od*)OssH",
	group = 
"""
1   CO 0 {2,S} {4,D}
2   Os 0 {1,S} {3,S}
3   H 0 {2,S}
4 * Od 0 {1,D}

""",
	solute = SoluteData(
		 S =  0.0,
		 B =  0.0,
		 E =  0.0,
		 L =  0.0,
		 A =  0.0
	),
	shortDesc = u"""same as 47""",
	longDesc = 
u"""

"""
)

entry(
	index = 83,
	label = "Cds(Od)Oss*H",
	group = 
"""
1   CO 0 {2,S} {4,D}
2 * Os 0 {1,S} {3,S}
3   H 0 {2,S}
4   Od 0 {1,D}

""",
	solute = SoluteData(
		 S =  0.0,
		 B =  0.0,
		 E =  0.0,
		 L =  0.0,
		 A =  0.0
	),
	shortDesc = u"""same as 47""",
	longDesc = 
u"""

"""
)


tree(
"""
L0: R

L1: C

	L2: Cbf // fused aromatic
	
	L2: Css // sp3
		L3: CssH3
		L3: CssH2
			L4: Css(OssH)-Css(OssH) // 1,2-diol
			L4: CbCss*OssH // benzyl alcohol
		L3: CssH
			L4: Css(OssH)-Css(OssH) // 1,2-diol
			L4: CbCss*OssH // benzyl alcohol
		L3: Css-noH
			L4: Css(OssH)-Css(OssH) // 1,2-diol
			L4: CbCss*OssH // benzyl alcohol
	
	L2: Cds // sp2
		L3: CdsH2
		L3: CdsH
			L4: Oss(CdsOd) // non-cyclic ester
				L5: Cds(Od)OssH // carboxylic acid
			L4: Cds(Od)Cds=CdsCds(Od) // quinone
			L4: Cds*(Od)Cds=CdsCds(Od) // quinone

		L3: Cds-noH
			L4: Oss(CdsOd) // non-cyclic ester
				L5: Cds(Od)OssH // carboxylic acid
				L5: OssCds(Od)Oss // carbonate
			L4: Cds(Od)Cds=CdsCds(Od) // quinone
			L4: Cds*(Od)Cds=CdsCds(Od) / quinone
		
	L2: Ct // sp
	L2: Cb // sp2 aromatic
		L3: CbCssOssH // benzyl alcohol
	L2: Cdd // sp2 nonfused aromatic

L1: O

	L2: Oss
		L3: OssH           // Hydroxyl group
			L4: Cds(Od)Oss*H // carboxylic acid
			L4: CbCssOss*H // benzyl alcohol
			L4: Css(Oss*H)-Css(OssH) // 1,2-diol
			
		L3: Oss*(CdsOd) // non-cyclic ester
			L4: Oss*Cds(Od)Oss // Carbonate
		 
		L3: Oss-noncyclic
		L3: Oss-cyclic
		
    L2: Od // sp2
    	L3: Oss(CdsOd*) // non-cyclic ester
    		L4: Cds(Od*)OssH // carboxylic acid
    		L4: OssCds(Od*)Oss // Carbonate
    	
    	L3: Cds(Od*)Cds=CdsCds(Od) // Quinone
"""
)