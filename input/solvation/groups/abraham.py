#!/usr/bin/env python
# encoding: utf-8

name = "Abraham Solute Descriptors"
shortDesc = u""
longDesc = u"""

"""


entry(
    index = -4,
    label = "O",
    group = 
"""
1 * {Os,Od} 0
""",
    solute = None,
    shortDesc = u"""""",
    longDesc = 
u"""

"""
)
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
1 * {Cd,CO} 0
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
1 * Cs  0 {2,S} {3,S} {4,S} {5,S}
2   H   0 {1,S}
3   H   0 {1,S}
4   H   0 {1,S}
5   R   0 {1,S}
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
1 * Cs  0 {2,S} {3,S} {4,S} {5,S}
2   H   0 {1,S}
3   H   0 {1,S}
4   R!H 0 {1,S}
5   R!H 0 {1,S}  
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
1 * Cs  0 {2,S} {3,S} {4,S} {5,S}
2   H   0 {1,S}
3   R!H   0 {1,S}
4   R!H   0 {1,S}
5   R!H   0 {1,S}

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
1 * Cs 0 {2,S} {3,S} {4,S} {5,S}
2   R!H   0 {1,S}
3   R!H   0 {1,S}
4   R!H   0 {1,S}
5	R!H	  0	{1,S}

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
1 * {Cd,CO} 0 {2,S} {3,S} {4,D}
2   H 0 {1,S}
3   H 0 {1,S}
4   R!H 0 {1,D}

""",
	solute = SoluteData(
		 S =  -0.085,
		 B =  0.019,
		 E =  -0.045,
		 L =  0.244,
		 A =  0
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
1 * {Cd,CO} 0 {2,S} {3,S} {4,D}
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
1 * {Cd,CO,Cb} 0 {2,S} {3,S} {4,D}
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
	index = 10,
	label = "Cb",
	group = 
"""
1 * Cb 0

""",
	solute = None,
	shortDesc = u"""""",
	longDesc = 
u"""

"""
)

entry(
	index = 11,
	label = "Cb-noH",
	group = 
"""
1 * Cb 0 (2,B) (3,B) (4,B)
2   R!H 0 (1,B)
3   R!H 0 (1,B)
4   R!H 0 (1,B)

""",
	solute = SoluteData(
		 S =  0.101,
		 B =  0,
		 E =  0.18,
		 L =  0.624,
		 A =  0,
	),
	shortDesc = u"""same as Platts group 7""",
	longDesc = 
u"""

"""
)

entry(
	index = 12,
	label = "Cb-H",
	group = 
"""
1 * Cb 0 (2,B) (3,B) (4,S)
2   R!H 0 (1,B)
3   R!H 0 (1,B)
4   H   0 (1,S)

""",
	solute = SoluteData(
		 S =  0.05,
		 B =  0.011,
		 E =  0.068,
		 L =  0.469,
		 A =  0,
	),
	shortDesc = u"""same as Platts group 6""",
	longDesc = 
u"""

"""
)

entry(
	index = 11,
	label = "Cb-noHnoRing",
	group = 
"""
1 * Cb 0 (2,B) (3,B) (4,S)
2   R!H 0 (1,B)
3   R!H 0 (1,B)
4   R!H 0 (1,S)

""",
	solute = SoluteData(
		 S =  0.101,
		 B =  0,
		 E =  0.18,
		 L =  0.624,
		 A =  0,
	),
	shortDesc = u"""same as Platts group 7""",
	longDesc = 
u"""
Cb is attached to a 3rd R group that isn't in the ring, as in phenol.
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
		 A =  0
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
	index = 75,
	label = "Cdd",
	group = 
"""
1 * Cdd 0

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


tree(
"""
L0: R

L1: C

	L2: Cbf // fused aromatic
	
	L2: Css // sp3
		L3: CssH3
		L3: CssH2
		L3: CssH
		L3: Css-noH
	
	L2: Cds // sp2
		L3: CdsH2
		L3: CdsH
		L3: Cds-noH
		
	L2: Ct // sp

	L2: Cdd // sp2 nonfused aromatic
	
	L2: Cb
		L3: Cb-noH
		L3: Cb-H
		L3: Cb-noHnoRing
	

L1: O

	L2: Oss
		L3: OssH           // Hydroxyl group
		L3: Oss-noncyclic
		
    L2: Od // sp2
"""
)