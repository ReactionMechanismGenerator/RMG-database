#!/usr/bin/env python
# encoding: utf-8

name = "polycyclic"
shortDesc = u""
longDesc = u""" 
All groups are fitted using experimental solute parameter data unless written otherwise.
See Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
"""

entry(
	index = 1,
	label = "PolycyclicRing",
	group = 
"""
1 * R u0
""",
	solute = SoluteData(
		S = 0.00086,
		B = 0.04137,
		E = -0.08617,
		L = 0.16153,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 17,
		B = 17,
		E = 17,
		L = 15,
		A = 17,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 2,
	label = "polycyclic_7fused",
	group =  "OR{Strychnine_general}",
	solute = None,
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 3,
	label = "Strychnine_general",
	group = 
"""
1  * R!H u0 {9,[S,D,B]} {16,[S,D,B]}
2  R!H u0 {7,[S,D,B]} {13,[S,D,B]} {15,[S,D,B]}
3  R!H u0 {6,[S,D,B]} {14,[S,D,B]} {19,[S,D,B]}
4  R!H u0 {6,[S,D,B]} {7,[S,D,B]} {10,[S,D,B]} {18,[S,D,B]}
5  R!H u0 {6,[S,D,B]} {8,[S,D,B]} {9,[S,D,B]}
6  R!H u0 {3,[S,D,B]} {4,[S,D,B]} {5,[S,D,B]}
7  R!H u0 {2,[S,D,B]} {4,[S,D,B]} {11,[S,D,B]}
8  R!H u0 {5,[S,D,B]} {11,[S,D,B]} {17,[S,D,B]}
9  R!H u0 {1,[S,D,B]} {5,[S,D,B]} {12,[S,D,B]}
10 R!H u0 {4,[S,D,B]} {13,[S,D,B]}
11 R!H u0 {7,[S,D,B]} {8,[S,D,B]}
12 R!H u0 {9,[S,D,B]} {14,[S,D,B]}
13 R!H u0 {2,[S,D,B]} {10,[S,D,B]}
14 R!H u0 {3,[S,D,B]} {12,[S,D,B]}
15 R!H u0 {2,[S,D,B]} {17,[S,D,B]}
16 R!H u0 {1,[S,D,B]} {20,[S,D,B]}
17 R!H u0 {8,[S,D,B]} {15,[S,D,B]} {20,[S,D,B]}
18 R!H u0 {4,[S,D,B]} {19,[S,D,B]} {21,[S,D,B]}
19 R!H u0 {3,[S,D,B]} {18,[S,D,B]} {22,[S,D,B]}
20 R!H u0 {16,[S,D,B]} {17,[S,D,B]}
21 R!H u0 {18,[S,D,B]} {23,[S,D,B]}
22 R!H u0 {19,[S,D,B]} {24,[S,D,B]}
23 R!H u0 {21,[S,D,B]} {24,[S,D,B]}
24 R!H u0 {22,[S,D,B]} {23,[S,D,B]}
""",
	solute = u'Strychnine',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 4,
	label = "Strychnine",
	group = 
"""
1  * O u0 {9,S} {16,S}
2  N u0 {7,S} {13,S} {15,S}
3  N u0 {6,S} {14,S} {19,S}
4  C u0 {6,S} {7,S} {10,S} {18,S}
5  C u0 {6,S} {8,S} {9,S}
6  C u0 {3,S} {4,S} {5,S}
7  C u0 {2,S} {4,S} {11,S}
8  C u0 {5,S} {11,S} {17,S}
9  C u0 {1,S} {5,S} {12,S}
10 C u0 {4,S} {13,S}
11 C u0 {7,S} {8,S}
12 C u0 {9,S} {14,S}
13 C u0 {2,S} {10,S}
14 CO u0 {3,S} {12,S}
15 C u0 {2,S} {17,S}
16 C u0 {1,S} {20,S}
17 C u0 {8,S} {15,S} {20,D}
18 C u0 {4,S} {19,B} {21,B}
19 C u0 {3,S} {18,B} {22,B}
20 C u0 {16,S} {17,D}
21 C u0 {18,B} {23,B}
22 C u0 {19,B} {24,B}
23 C u0 {21,B} {24,B}
24 C u0 {22,B} {23,B}
""",
	solute = SoluteData(
		S = -0.03901,
		B = 0.04494,
		E = 0.24179,
		L = 0.19867,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
		E = 2,
		L = 2,
		A = 2,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 5,
	label = "polycyclic_5fused",
	group =  "OR{Porphyrin, Morphine_general, Benzo[e]pyrene_general, Benzo[a]pyrene_general, Fluoran_general, Picene_general,\
1H-Cyclopenta[a]chrysene_general, Benzo[ghi]fluoranthene_general, Cholanthrene_general, \
5fused_r6_r6_r6_r5_r5}",
	solute = None,
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 6,
	label = "Porphyrin",
	group = 
"""
1  * N u0 {7,[S,D]} {8,[S,D]}
2  N u0 {5,[S,D]} {6,[S,D]}
3  N u0 {10,[S,D]} {11,[S,D]}
4  N u0 {9,[S,D]} {12,[S,D]}
5  C u0 {2,[S,D]} {13,[S,D]} {17,[S,D]}
6  C u0 {2,[S,D]} {14,[S,D]} {18,[S,D]}
7  C u0 {1,[S,D]} {15,[S,D]} {19,[S,D]}
8  C u0 {1,[S,D]} {16,[S,D]} {20,[S,D]}
9  C u0 {4,[S,D]} {13,[S,D]} {22,[S,D]}
10 C u0 {3,[S,D]} {14,[S,D]} {24,[S,D]}
11 C u0 {3,[S,D]} {15,[S,D]} {23,[S,D]}
12 C u0 {4,[S,D]} {16,[S,D]} {21,[S,D]}
13 C u0 {5,[S,D]} {9,[S,D]}
14 C u0 {6,[S,D]} {10,[S,D]}
15 C u0 {7,[S,D]} {11,[S,D]}
16 C u0 {8,[S,D]} {12,[S,D]}
17 C u0 {5,[S,D]} {18,[S,D]}
18 C u0 {6,[S,D]} {17,[S,D]}
19 C u0 {7,[S,D]} {20,[S,D]}
20 C u0 {8,[S,D]} {19,[S,D]}
21 C u0 {12,[S,D]} {22,[S,D]}
22 C u0 {9,[S,D]} {21,[S,D]}
23 C u0 {11,[S,D]} {24,[S,D]}
24 C u0 {10,[S,D]} {23,[S,D]}
""",
	solute = SoluteData(
		S = 0.00826,
		B = -0.03271,
		E = -0.10104,
		L = 0.11850,
		A = -0.06272,
	),
	dataCount = DataCountGAV(
		S = 17,
		B = 17,
		E = 26,
		L = 17,
		A = 26,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 7,
	label = "Morphine_general",
	group = 
"""
1  * R!H u0 {6,[S,D,B]} {15,[S,D,B]}
2  R!H u0 {5,[S,D,B]} {12,[S,D,B]}
3  R!H u0 {4,[S,D,B]} {6,[S,D,B]} {7,[S,D,B]} {13,[S,D,B]}
4  R!H u0 {3,[S,D,B]} {5,[S,D,B]} {8,[S,D,B]}
5  R!H u0 {2,[S,D,B]} {4,[S,D,B]} {11,[S,D,B]}
6  R!H u0 {1,[S,D,B]} {3,[S,D,B]} {9,[S,D,B]}
7  R!H u0 {3,[S,D,B]} {12,[S,D,B]}
8  R!H u0 {4,[S,D,B]} {10,[S,D,B]}
9  R!H u0 {6,[S,D,B]} {10,[S,D,B]}
10 R!H u0 {8,[S,D,B]} {9,[S,D,B]}
11 R!H u0 {5,[S,D,B]} {14,[S,D,B]}
12 R!H u0 {2,[S,D,B]} {7,[S,D,B]}
13 R!H u0 {3,[S,D,B]} {14,[S,D,B]} {15,[S,D,B]}
14 R!H u0 {11,[S,D,B]} {13,[S,D,B]} {16,[S,D,B]}
15 R!H u0 {1,[S,D,B]} {13,[S,D,B]} {17,[S,D,B]}
16 R!H u0 {14,[S,D,B]} {18,[S,D,B]}
17 R!H u0 {15,[S,D,B]} {18,[S,D,B]}
18 R!H u0 {16,[S,D,B]} {17,[S,D,B]}
""",
	solute = u'Dihydro-normorphine,3-desoxy-',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 8,
	label = "Dihydro-normorphine,3-desoxy-",
	group = 
"""
1  * O u0 {6,S} {15,S}
2  N u0 {5,S} {12,S}
3  C u0 {4,S} {6,S} {7,S} {13,S}
4  C u0 {3,S} {5,S} {8,S}
5  C u0 {2,S} {4,S} {11,S}
6  C u0 {1,S} {3,S} {9,S}
7  C u0 {3,S} {12,S}
8  C u0 {4,S} {10,S}
9  CO u0 {6,S} {10,S}
10 C u0 {8,S} {9,S}
11 C u0 {5,S} {14,S}
12 C u0 {2,S} {7,S}
13 C u0 {3,S} {14,B} {15,B}
14 C u0 {11,S} {13,B} {16,B}
15 C u0 {1,S} {13,B} {17,B}
16 C u0 {14,B} {18,B}
17 C u0 {15,B} {18,B}
18 C u0 {16,B} {17,B}
""",
	solute = SoluteData(
		S = 0.11119,
		B = -0.08070,
		E = 0.04218,
		L = 0.12585,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 6,
		B = 6,
		E = 6,
		L = 6,
		A = 6,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 9,
	label = "Morphine",
	group = 
"""
1  * O u0 {6,S} {15,S}
2  N u0 {5,S} {12,S}
3  C u0 {4,S} {6,S} {7,S} {13,S}
4  C u0 {3,S} {5,S} {8,S}
5  C u0 {2,S} {4,S} {11,S}
6  C u0 {1,S} {3,S} {9,S}
7  C u0 {3,S} {12,S}
8  C u0 {4,S} {10,D}
9  C u0 {6,S} {10,S}
10 C u0 {8,D} {9,S}
11 C u0 {5,S} {14,S}
12 C u0 {2,S} {7,S}
13 C u0 {3,S} {14,B} {15,B}
14 C u0 {11,S} {13,B} {16,B}
15 C u0 {1,S} {13,B} {17,B}
16 C u0 {14,B} {18,B}
17 C u0 {15,B} {18,B}
18 C u0 {16,B} {17,B}
""",
	solute = SoluteData(
		S = 0.13666,
		B = -0.08163,
		E = -0.03679,
		L = 0.24899,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 3,
		L = 3,
		A = 3,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 10,
	label = "Dihydromorphine",
	group = 
"""
1  * O u0 {6,S} {15,S}
2  N u0 {5,S} {12,S}
3  C u0 {4,S} {6,S} {7,S} {13,S}
4  C u0 {3,S} {5,S} {8,S}
5  C u0 {2,S} {4,S} {11,S}
6  C u0 {1,S} {3,S} {9,S}
7  C u0 {3,S} {12,S}
8  C u0 {4,S} {10,S}
9  C u0 {6,S} {10,S}
10 C u0 {8,S} {9,S}
11 C u0 {5,S} {14,S}
12 C u0 {2,S} {7,S}
13 C u0 {3,S} {14,B} {15,B}
14 C u0 {11,S} {13,B} {16,B}
15 C u0 {1,S} {13,B} {17,B}
16 C u0 {14,B} {18,B}
17 C u0 {15,B} {18,B}
18 C u0 {16,B} {17,B}
""",
	solute = SoluteData(
		S = 0.03415,
		B = 0.13790,
		E = 0.01346,
		L = -0.10507,
		A = -0.04230,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 3,
		L = 3,
		A = 3,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 11,
	label = "Benzo[e]pyrene_general",
	group = 
"""
1  * R!H u0 {2,[S,D,B]} {6,[S,D,B]} {8,[S,D,B]}
2  R!H u0 {1,[S,D,B]} {5,[S,D,B]} {7,[S,D,B]}
3  R!H u0 {4,[S,D,B]} {6,[S,D,B]} {9,[S,D,B]}
4  R!H u0 {3,[S,D,B]} {5,[S,D,B]} {10,[S,D,B]}
5  R!H u0 {2,[S,D,B]} {4,[S,D,B]} {11,[S,D,B]}
6  R!H u0 {1,[S,D,B]} {3,[S,D,B]} {16,[S,D,B]}
7  R!H u0 {2,[S,D,B]} {12,[S,D,B]} {13,[S,D,B]}
8  R!H u0 {1,[S,D,B]} {14,[S,D,B]} {15,[S,D,B]}
9  R!H u0 {3,[S,D,B]} {18,[S,D,B]}
10 R!H u0 {4,[S,D,B]} {17,[S,D,B]}
11 R!H u0 {5,[S,D,B]} {19,[S,D,B]}
12 R!H u0 {7,[S,D,B]} {19,[S,D,B]}
13 R!H u0 {7,[S,D,B]} {14,[S,D,B]}
14 R!H u0 {8,[S,D,B]} {13,[S,D,B]}
15 R!H u0 {8,[S,D,B]} {20,[S,D,B]}
16 R!H u0 {6,[S,D,B]} {20,[S,D,B]}
17 R!H u0 {10,[S,D,B]} {18,[S,D,B]}
18 R!H u0 {9,[S,D,B]} {17,[S,D,B]}
19 R!H u0 {11,[S,D,B]} {12,[S,D,B]}
20 R!H u0 {15,[S,D,B]} {16,[S,D,B]}
""",
	solute = u'Benzo[e]pyrene',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 12,
	label = "Benzo[e]pyrene",
	group = 
"""
1  * C u0 {2,B} {6,B} {8,B}
2  C u0 {1,B} {5,B} {7,B}
3  C u0 {4,B} {6,B} {9,B}
4  C u0 {3,B} {5,B} {10,B}
5  C u0 {2,B} {4,B} {11,B}
6  C u0 {1,B} {3,B} {16,B}
7  C u0 {2,B} {12,B} {13,B}
8  C u0 {1,B} {14,B} {15,B}
9  C u0 {3,B} {18,B}
10 C u0 {4,B} {17,B}
11 C u0 {5,B} {19,B}
12 C u0 {7,B} {19,B}
13 C u0 {7,B} {14,B}
14 C u0 {8,B} {13,B}
15 C u0 {8,B} {20,B}
16 C u0 {6,B} {20,B}
17 C u0 {10,B} {18,B}
18 C u0 {9,B} {17,B}
19 C u0 {11,B} {12,B}
20 C u0 {15,B} {16,B}
""",
	solute = SoluteData(
		S = 0.02831,
		B = -0.04796,
		E = 0.03844,
		L = 0.39002,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 4,
		B = 4,
		E = 4,
		L = 3,
		A = 4,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 13,
	label = "Benzo[a]pyrene_general",
	group = 
"""
1  * R!H u0 {2,[S,D,B]} {4,[S,D,B]} {6,[S,D,B]}
2  R!H u0 {1,[S,D,B]} {7,[S,D,B]} {8,[S,D,B]}
3  R!H u0 {4,[S,D,B]} {5,[S,D,B]} {10,[S,D,B]}
4  R!H u0 {1,[S,D,B]} {3,[S,D,B]} {17,[S,D,B]}
5  R!H u0 {3,[S,D,B]} {9,[S,D,B]} {11,[S,D,B]}
6  R!H u0 {1,[S,D,B]} {9,[S,D,B]} {12,[S,D,B]}
7  R!H u0 {2,[S,D,B]} {13,[S,D,B]} {14,[S,D,B]}
8  R!H u0 {2,[S,D,B]} {15,[S,D,B]} {16,[S,D,B]}
9  R!H u0 {5,[S,D,B]} {6,[S,D,B]}
10 R!H u0 {3,[S,D,B]} {19,[S,D,B]}
11 R!H u0 {5,[S,D,B]} {18,[S,D,B]}
12 R!H u0 {6,[S,D,B]} {13,[S,D,B]}
13 R!H u0 {7,[S,D,B]} {12,[S,D,B]}
14 R!H u0 {7,[S,D,B]} {20,[S,D,B]}
15 R!H u0 {8,[S,D,B]} {20,[S,D,B]}
16 R!H u0 {8,[S,D,B]} {17,[S,D,B]}
17 R!H u0 {4,[S,D,B]} {16,[S,D,B]}
18 R!H u0 {11,[S,D,B]} {19,[S,D,B]}
19 R!H u0 {10,[S,D,B]} {18,[S,D,B]}
20 R!H u0 {14,[S,D,B]} {15,[S,D,B]}
""",
	solute = u'Benzo[a]pyrene',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 14,
	label = "Benzo[a]pyrene",
	group = 
"""
1  * C u0 {2,B} {4,B} {6,B}
2  C u0 {1,B} {7,B} {8,B}
3  C u0 {4,B} {5,B} {10,B}
4  C u0 {1,B} {3,B} {17,B}
5  C u0 {3,B} {9,B} {11,B}
6  C u0 {1,B} {9,B} {12,B}
7  C u0 {2,B} {13,B} {14,B}
8  C u0 {2,B} {15,B} {16,B}
9  C u0 {5,B} {6,B}
10 C u0 {3,B} {19,B}
11 C u0 {5,B} {18,B}
12 C u0 {6,B} {13,B}
13 C u0 {7,B} {12,B}
14 C u0 {7,B} {20,B}
15 C u0 {8,B} {20,B}
16 C u0 {8,B} {17,B}
17 C u0 {4,B} {16,B}
18 C u0 {11,B} {19,B}
19 C u0 {10,B} {18,B}
20 C u0 {14,B} {15,B}
""",
	solute = SoluteData(
		S = 0.01349,
		B = -0.01129,
		E = 0.08825,
		L = 0.18456,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
		E = 2,
		L = 2,
		A = 2,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 15,
	label = "Fluoran_general",
	group = 
"""
1  * R!H u0 {3,[S,D,B]} {4,[S,D,B]}
2  R!H u0 {9,[S,D,B]} {10,[S,D,B]}
3  R!H u0 {1,[S,D,B]} {5,[S,D,B]} {6,[S,D,B]} {7,[S,D,B]}
4  R!H u0 {1,[S,D,B]} {8,[S,D,B]}
5  R!H u0 {3,[S,D,B]} {8,[S,D,B]} {13,[S,D,B]}
6  R!H u0 {3,[S,D,B]} {9,[S,D,B]} {11,[S,D,B]}
7  R!H u0 {3,[S,D,B]} {10,[S,D,B]} {12,[S,D,B]}
8  R!H u0 {4,[S,D,B]} {5,[S,D,B]} {14,[S,D,B]}
9  R!H u0 {2,[S,D,B]} {6,[S,D,B]} {15,[S,D,B]}
10 R!H u0 {2,[S,D,B]} {7,[S,D,B]} {16,[S,D,B]}
11 R!H u0 {6,[S,D,B]} {17,[S,D,B]}
12 R!H u0 {7,[S,D,B]} {20,[S,D,B]}
13 R!H u0 {5,[S,D,B]} {21,[S,D,B]}
14 R!H u0 {8,[S,D,B]} {22,[S,D,B]}
15 R!H u0 {9,[S,D,B]} {18,[S,D,B]}
16 R!H u0 {10,[S,D,B]} {19,[S,D,B]}
17 R!H u0 {11,[S,D,B]} {18,[S,D,B]}
18 R!H u0 {15,[S,D,B]} {17,[S,D,B]}
19 R!H u0 {16,[S,D,B]} {20,[S,D,B]}
20 R!H u0 {12,[S,D,B]} {19,[S,D,B]}
21 R!H u0 {13,[S,D,B]} {22,[S,D,B]}
22 R!H u0 {14,[S,D,B]} {21,[S,D,B]}
""",
	solute = u'Fluoran',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 16,
	label = "Fluoran",
	group = 
"""
1  * O u0 {3,S} {4,S}
2  O u0 {9,S} {10,S}
3  C u0 {1,S} {5,S} {6,S} {7,S}
4  CO u0 {1,S} {8,S}
5  C u0 {3,S} {8,B} {13,B}
6  C u0 {3,S} {9,B} {11,B}
7  C u0 {3,S} {10,B} {12,B}
8  C u0 {4,S} {5,B} {14,B}
9  C u0 {2,S} {6,B} {15,B}
10 C u0 {2,S} {7,B} {16,B}
11 C u0 {6,B} {17,B}
12 C u0 {7,B} {20,B}
13 C u0 {5,B} {21,B}
14 C u0 {8,B} {22,B}
15 C u0 {9,B} {18,B}
16 C u0 {10,B} {19,B}
17 C u0 {11,B} {18,B}
18 C u0 {15,B} {17,B}
19 C u0 {16,B} {20,B}
20 C u0 {12,B} {19,B}
21 C u0 {13,B} {22,B}
22 C u0 {14,B} {21,B}
""",
	solute = SoluteData(
		S = 0.12438,
		B = -0.00941,
		E = -0.02436,
		L = 0.13617,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 3,
		L = 3,
		A = 3,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 17,
	label = "Picene_general",
	group = 
"""
1  * R!H u0 {2,[S,D,B]} {4,[S,D,B]} {9,[S,D,B]}
2  R!H u0 {1,[S,D,B]} {3,[S,D,B]} {20,[S,D,B]}
3  R!H u0 {2,[S,D,B]} {7,[S,D,B]} {12,[S,D,B]}
4  R!H u0 {1,[S,D,B]} {10,[S,D,B]} {11,[S,D,B]}
5  R!H u0 {6,[S,D,B]} {8,[S,D,B]} {13,[S,D,B]}
6  R!H u0 {5,[S,D,B]} {14,[S,D,B]} {21,[S,D,B]}
7  R!H u0 {3,[S,D,B]} {15,[S,D,B]} {21,[S,D,B]}
8  R!H u0 {5,[S,D,B]} {16,[S,D,B]}
9  R!H u0 {1,[S,D,B]} {18,[S,D,B]}
10 R!H u0 {4,[S,D,B]} {19,[S,D,B]}
11 R!H u0 {4,[S,D,B]} {12,[S,D,B]}
12 R!H u0 {3,[S,D,B]} {11,[S,D,B]}
13 R!H u0 {5,[S,D,B]} {15,[S,D,B]}
14 R!H u0 {6,[S,D,B]} {17,[S,D,B]}
15 R!H u0 {7,[S,D,B]} {13,[S,D,B]}
16 R!H u0 {8,[S,D,B]} {17,[S,D,B]}
17 R!H u0 {14,[S,D,B]} {16,[S,D,B]}
18 R!H u0 {9,[S,D,B]} {19,[S,D,B]}
19 R!H u0 {10,[S,D,B]} {18,[S,D,B]}
20 R!H u0 {2,[S,D,B]} {22,[S,D,B]}
21 R!H u0 {6,[S,D,B]} {7,[S,D,B]} {22,[S,D,B]}
22 R!H u0 {20,[S,D,B]} {21,[S,D,B]}
""",
	solute = u'Picene',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 18,
	label = "Picene",
	group = 
"""
1  * C u0 {2,B} {4,B} {9,B}
2  C u0 {1,B} {3,B} {20,B}
3  C u0 {2,B} {7,B} {12,B}
4  C u0 {1,B} {10,B} {11,B}
5  C u0 {6,B} {8,B} {13,B}
6  C u0 {5,B} {14,B} {21,B}
7  C u0 {3,B} {15,B} {21,B}
8  C u0 {5,B} {16,B}
9  C u0 {1,B} {18,B}
10 C u0 {4,B} {19,B}
11 C u0 {4,B} {12,B}
12 C u0 {3,B} {11,B}
13 C u0 {5,B} {15,B}
14 C u0 {6,B} {17,B}
15 C u0 {7,B} {13,B}
16 C u0 {8,B} {17,B}
17 C u0 {14,B} {16,B}
18 C u0 {9,B} {19,B}
19 C u0 {10,B} {18,B}
20 C u0 {2,B} {22,B}
21 C u0 {6,B} {7,B} {22,B}
22 C u0 {20,B} {21,B}
""",
	solute = SoluteData(
		S = -0.00848,
		B = 0.00482,
		E = 0.01055,
		L = 0.07780,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 1,
		B = 1,
		E = 1,
		L = 1,
		A = 1,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 19,
	label = "Icosahydropicene",
	group = 
"""
1  * C u0 {2,S} {4,S} {9,S}
2  C u0 {1,S} {3,S} {20,S}
3  C u0 {2,S} {7,S} {12,S}
4  C u0 {1,S} {10,S} {11,S}
5  C u0 {6,S} {8,S} {13,S}
6  C u0 {5,S} {14,S} {21,S}
7  C u0 {3,S} {15,S} {21,S}
8  C u0 {5,S} {16,S}
9  C u0 {1,S} {18,S}
10 C u0 {4,S} {19,S}
11 C u0 {4,S} {12,S}
12 C u0 {3,S} {11,S}
13 C u0 {5,S} {15,S}
14 C u0 {6,S} {17,S}
15 C u0 {7,S} {13,S}
16 C u0 {8,S} {17,S}
17 C u0 {14,S} {16,S}
18 C u0 {9,S} {19,S}
19 C u0 {10,S} {18,S}
20 C u0 {2,S} {22,S}
21 C u0 {6,S} {7,S} {22,D}
22 C u0 {20,S} {21,D}
""",
	solute = SoluteData(
		S = -0.04109,
		B = 0.20873,
		E = -0.14768,
		L = 0.30673,
		A = 0.59089,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 3,
		L = 3,
		A = 3,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 20,
	label = "1H-Cyclopenta[a]chrysene_general",
	group = 
"""
1  * R!H u0 {3,[S,D,B]} {7,[S,D,B]} {9,[S,D,B]}
2  R!H u0 {3,[S,D,B]} {6,[S,D,B]} {12,[S,D,B]}
3  R!H u0 {1,[S,D,B]} {2,[S,D,B]} {13,[S,D,B]}
4  R!H u0 {5,[S,D,B]} {6,[S,D,B]} {14,[S,D,B]}
5  R!H u0 {4,[S,D,B]} {8,[S,D,B]} {15,[S,D,B]}
6  R!H u0 {2,[S,D,B]} {4,[S,D,B]} {18,[S,D,B]}
7  R!H u0 {1,[S,D,B]} {10,[S,D,B]} {11,[S,D,B]}
8  R!H u0 {5,[S,D,B]} {16,[S,D,B]} {17,[S,D,B]}
9  R!H u0 {1,[S,D,B]} {20,[S,D,B]}
10 R!H u0 {7,[S,D,B]} {19,[S,D,B]}
11 R!H u0 {7,[S,D,B]} {12,[S,D,B]}
12 R!H u0 {2,[S,D,B]} {11,[S,D,B]}
13 R!H u0 {3,[S,D,B]} {14,[S,D,B]}
14 R!H u0 {4,[S,D,B]} {13,[S,D,B]}
15 R!H u0 {5,[S,D,B]} {21,[S,D,B]}
16 R!H u0 {8,[S,D,B]} {21,[S,D,B]}
17 R!H u0 {8,[S,D,B]} {18,[S,D,B]}
18 R!H u0 {6,[S,D,B]} {17,[S,D,B]}
19 R!H u0 {10,[S,D,B]} {20,[S,D,B]}
20 R!H u0 {9,[S,D,B]} {19,[S,D,B]}
21 R!H u0 {15,[S,D,B]} {16,[S,D,B]}
""",
	solute = u'1H-Cyclopenta[a]chrysene',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 21,
	label = "1H-Cyclopenta[a]chrysene",
	group = 
"""
1  * C u0 {3,S} {7,S} {9,S}
2  C u0 {3,S} {6,S} {12,S}
3  C u0 {1,S} {2,S} {13,S}
4  C u0 {5,S} {6,S} {14,S}
5  C u0 {4,S} {8,S} {15,S}
6  C u0 {2,S} {4,S} {18,S}
7  C u0 {1,S} {10,S} {11,S}
8  C u0 {5,S} {16,S} {17,S}
9  C u0 {1,S} {20,S}
10 C u0 {7,S} {19,S}
11 C u0 {7,S} {12,S}
12 C u0 {2,S} {11,S}
13 C u0 {3,S} {14,S}
14 C u0 {4,S} {13,S}
15 C u0 {5,S} {21,S}
16 C u0 {8,S} {21,S}
17 C u0 {8,S} {18,S}
18 C u0 {6,S} {17,S}
19 C u0 {10,S} {20,S}
20 C u0 {9,S} {19,S}
21 C u0 {15,S} {16,S}
""",
	solute = SoluteData(
		S = -0.03500,
		B = 0.14057,
		E = -0.02027,
		L = 0.27100,
		A = 0.04393,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
		E = 2,
		L = 2,
		A = 2,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 22,
	label = "Benzo[ghi]fluoranthene_general",
	group = 
"""
1  * R!H u0 {3,[S,D,B]} {4,[S,D,B]} {6,[S,D,B]}
2  R!H u0 {3,[S,D,B]} {5,[S,D,B]} {8,[S,D,B]}
3  R!H u0 {1,[S,D,B]} {2,[S,D,B]} {7,[S,D,B]}
4  R!H u0 {1,[S,D,B]} {5,[S,D,B]} {9,[S,D,B]}
5  R!H u0 {2,[S,D,B]} {4,[S,D,B]} {16,[S,D,B]}
6  R!H u0 {1,[S,D,B]} {10,[S,D,B]} {11,[S,D,B]}
7  R!H u0 {3,[S,D,B]} {12,[S,D,B]} {13,[S,D,B]}
8  R!H u0 {2,[S,D,B]} {14,[S,D,B]} {15,[S,D,B]}
9  R!H u0 {4,[S,D,B]} {17,[S,D,B]}
10 R!H u0 {6,[S,D,B]} {17,[S,D,B]}
11 R!H u0 {6,[S,D,B]} {12,[S,D,B]}
12 R!H u0 {7,[S,D,B]} {11,[S,D,B]}
13 R!H u0 {7,[S,D,B]} {14,[S,D,B]}
14 R!H u0 {8,[S,D,B]} {13,[S,D,B]}
15 R!H u0 {8,[S,D,B]} {18,[S,D,B]}
16 R!H u0 {5,[S,D,B]} {18,[S,D,B]}
17 R!H u0 {9,[S,D,B]} {10,[S,D,B]}
18 R!H u0 {15,[S,D,B]} {16,[S,D,B]}
""",
	solute = u'Benzo[ghi]fluoranthene',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 23,
	label = "Benzo[ghi]fluoranthene",
	group = 
"""
1  * C u0 {3,B} {4,B} {6,B}
2  C u0 {3,B} {5,B} {8,B}
3  C u0 {1,B} {2,B} {7,B}
4  C u0 {1,B} {5,S} {9,B}
5  C u0 {2,B} {4,S} {16,B}
6  C u0 {1,B} {10,B} {11,B}
7  C u0 {3,B} {12,B} {13,B}
8  C u0 {2,B} {14,B} {15,B}
9  C u0 {4,B} {17,B}
10 C u0 {6,B} {17,B}
11 C u0 {6,B} {12,B}
12 C u0 {7,B} {11,B}
13 C u0 {7,B} {14,B}
14 C u0 {8,B} {13,B}
15 C u0 {8,B} {18,B}
16 C u0 {5,B} {18,B}
17 C u0 {9,B} {10,B}
18 C u0 {15,B} {16,B}
""",
	solute = SoluteData(
		S = 0.01965,
		B = 0.01096,
		E = 0.03205,
		L = -0.08480,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 1,
		B = 1,
		E = 1,
		L = 1,
		A = 1,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 24,
	label = "Cholanthrene_general",
	group = 
"""
1  * R!H u0 {2,[S,D,B]} {3,[S,D,B]}
2  R!H u0 {1,[S,D,B]} {4,[S,D,B]}
3  R!H u0 {1,[S,D,B]} {5,[S,D,B]} {6,[S,D,B]}
4  R!H u0 {2,[S,D,B]} {5,[S,D,B]} {12,[S,D,B]}
5  R!H u0 {3,[S,D,B]} {4,[S,D,B]} {10,[S,D,B]}
6  R!H u0 {3,[S,D,B]} {8,[S,D,B]} {13,[S,D,B]}
7  R!H u0 {8,[S,D,B]} {9,[S,D,B]} {16,[S,D,B]}
8  R!H u0 {6,[S,D,B]} {7,[S,D,B]} {11,[S,D,B]}
9  R!H u0 {7,[S,D,B]} {14,[S,D,B]} {15,[S,D,B]}
10 R!H u0 {5,[S,D,B]} {11,[S,D,B]} {17,[S,D,B]}
11 R!H u0 {8,[S,D,B]} {10,[S,D,B]}
12 R!H u0 {4,[S,D,B]} {18,[S,D,B]}
13 R!H u0 {6,[S,D,B]} {14,[S,D,B]}
14 R!H u0 {9,[S,D,B]} {13,[S,D,B]}
15 R!H u0 {9,[S,D,B]} {19,[S,D,B]}
16 R!H u0 {7,[S,D,B]} {20,[S,D,B]}
17 R!H u0 {10,[S,D,B]} {18,[S,D,B]}
18 R!H u0 {12,[S,D,B]} {17,[S,D,B]}
19 R!H u0 {15,[S,D,B]} {20,[S,D,B]} 
20 R!H u0 {16,[S,D,B]} {19,[S,D,B]}
""",
	solute = u'Cholanthrene',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 25,
	label = "Cholanthrene",
	group = 
"""
1  * C u0 {2,S} {3,S}
2  C u0 {1,S} {4,S}
3  C u0 {1,S} {5,B} {6,B}
4  C u0 {2,S} {5,B} {12,B}
5  C u0 {3,B} {4,B} {10,B}
6  C u0 {3,B} {8,B} {13,B}
7  C u0 {8,B} {9,B} {16,B}
8  C u0 {6,B} {7,B} {11,B}
9  C u0 {7,B} {14,B} {15,B}
10 C u0 {5,B} {11,B} {17,B}
11 C u0 {8,B} {10,B}
12 C u0 {4,B} {18,B}
13 C u0 {6,B} {14,B}
14 C u0 {9,B} {13,B}
15 C u0 {9,B} {19,B}
16 C u0 {7,B} {20,B}
17 C u0 {10,B} {18,B}
18 C u0 {12,B} {17,B}
19 C u0 {15,B} {20,B} 
20 C u0 {16,B} {19,B}
""",
	solute = SoluteData(
		S = -0.03270,
		B = 0.02006,
		E = 0.08714,
		L = 0.10280,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
		E = 2,
		L = 1,
		A = 2,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 26,
	label = "5fused_r6_r6_r6_r5_r5",
	group = 
"""
1  * R!H u0 {9,[S,D,B]} {16,[S,D,B]}
2  R!H u0 {8,[S,D,B]} {16,[S,D,B]}
3  R!H u0 {4,[S,D,B]} {5,[S,D,B]} {13,[S,D,B]}
4  R!H u0 {3,[S,D,B]} {6,[S,D,B]} {10,[S,D,B]}
5  R!H u0 {3,[S,D,B]} {7,[S,D,B]} {11,[S,D,B]}
6  R!H u0 {4,[S,D,B]} {8,[S,D,B]} {12,[S,D,B]}
7  R!H u0 {5,[S,D,B]} {17,[S,D,B]} {18,[S,D,B]}
8  R!H u0 {2,[S,D,B]} {6,[S,D,B]} {9,[S,D,B]}
9  R!H u0 {1,[S,D,B]} {8,[S,D,B]} {10,[S,D,B]}
10 R!H u0 {4,[S,D,B]} {9,[S,D,B]}
11 R!H u0 {5,[S,D,B]} {12,[S,D,B]}
12 R!H u0 {6,[S,D,B]} {11,[S,D,B]}
13 R!H u0 {3,[S,D,B]} {14,[S,D,B]}
14 R!H u0 {13,[S,D,B]} {17,[S,D,B]}
15 R!H u0 {19,[S,D,B]} {20,[S,D,B]}
16 R!H u0 {1,[S,D,B]} {2,[S,D,B]}
17 R!H u0 {7,[S,D,B]} {14,[S,D,B]} {19,[S,D,B]}
18 R!H u0 {7,[S,D,B]} {20,[S,D,B]}
19 R!H u0 {15,[S,D,B]} {17,[S,D,B]}
20 R!H u0 {15,[S,D,B]} {18,[S,D,B]}
""",
	solute = u'5fused_r6_diene_r6_r6_r5_r5_dioxo',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 27,
	label = "5fused_r6_diene_r6_r6_r5_r5_dioxo",
	group = 
"""
1  * O u0 {9,S} {16,S}
2  O u0 {8,S} {16,S}
3  C u0 {4,S} {5,S} {13,S}
4  C u0 {3,S} {6,S} {10,S}
5  C u0 {3,S} {7,S} {11,S}
6  C u0 {4,S} {8,S} {12,S}
7  C u0 {5,S} {17,S} {18,S}
8  C u0 {2,S} {6,S} {9,S}
9  C u0 {1,S} {8,S} {10,S}
10 C u0 {4,S} {9,S}
11 C u0 {5,S} {12,S}
12 C u0 {6,S} {11,S}
13 C u0 {3,S} {14,S}
14 C u0 {13,S} {17,S}
15 CO u0 {19,S} {20,S}
16 C u0 {1,S} {2,S}
17 C u0 {7,S} {14,S} {19,D}
18 C u0 {7,S} {20,D}
19 C u0 {15,S} {17,D}
20 C u0 {15,S} {18,D}
""",
	solute = SoluteData(
		S = -0.04129,
		B = 0.00759,
		E = 0.10643,
		L = 0.08733,
		A = 0.02091,
	),
	dataCount = DataCountGAV(
		S = 8,
		B = 8,
		E = 8,
		L = 3,
		A = 8,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 28,
	label = "polycyclic_4fused",
	group =  "OR{Artemether_general, Fluoranthene_general, s3_6_6_s3_6_6_s3_6_6, s2_5_6_s2_6_6_s2_6_6, s2_6_6_s2_6_6_s2_6_6,\
s2_6_6_s2_6_6_s2_6_6_A, s2_6_6_s2_6_6_s2_6_6_B, s2_6_5_s2_5_9_s3_9_6, s2_6_7_s2_7_6_s2_7_6, Quadricyclane_general}",
	solute = None,
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 29,
	label = "Artemether_general",
	group = 
"""
1  * R!H u0 {14,[S,D,B]} {15,[S,D,B]}
2  R!H u0 {14,[S,D,B]} {16,[S,D,B]}
3  R!H u0 {4,[S,D,B]} {5,[S,D,B]}
4  R!H u0 {3,[S,D,B]} {15,[S,D,B]}
5  R!H u0 {3,[S,D,B]} {6,[S,D,B]} {7,[S,D,B]} {14,[S,D,B]}
6  R!H u0 {5,[S,D,B]} {8,[S,D,B]} {11,[S,D,B]}
7  R!H u0 {5,[S,D,B]} {9,[S,D,B]} {10,[S,D,B]}
8  R!H u0 {6,[S,D,B]} {12,[S,D,B]}
9  R!H u0 {7,[S,D,B]} {13,[S,D,B]}
10 R!H u0 {7,[S,D,B]} {12,[S,D,B]}
11 R!H u0 {6,[S,D,B]} {16,[S,D,B]}
12 R!H u0 {8,[S,D,B]} {10,[S,D,B]}
13 R!H u0 {9,[S,D,B]} {15,[S,D,B]}
14 R!H u0 {1,[S,D,B]} {2,[S,D,B]} {5,[S,D,B]}
15 R!H u0 {1,[S,D,B]} {4,[S,D,B]} {13,[S,D,B]}
16 R!H u0 {2,[S,D,B]} {11,[S,D,B]}
""",
	solute = u'Artemether',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 30,
	label = "Artemether",
	group = 
"""
1  * O u0 {14,S} {15,S}
2  O u0 {14,S} {16,S}
3  O u0 {4,S} {5,S}
4  O u0 {3,S} {15,S}
5  C u0 {3,S} {6,S} {7,S} {14,S}
6  C u0 {5,S} {8,S} {11,S}
7  C u0 {5,S} {9,S} {10,S}
8  C u0 {6,S} {12,S}
9  C u0 {7,S} {13,S}
10 C u0 {7,S} {12,S}
11 C u0 {6,S} {16,S}
12 C u0 {8,S} {10,S}
13 C u0 {9,S} {15,S}
14 C u0 {1,S} {2,S} {5,S}
15 C u0 {1,S} {4,S} {13,S}
16 C u0 {2,S} {11,S}
""",
	solute = SoluteData(
		S = 0.03995,
		B = 0.06911,
		E = 0.08418,
		L = 0.21893,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 7,
		B = 7,
		E = 7,
		L = 7,
		A = 7,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 31,
	label = "Fluoranthene_general",
	group = 
"""
1  * R!H u0 {4,[S,D,B]} {5,[S,D,B]} {6,[S,D,B]}
2  R!H u0 {3,[S,D,B]} {5,[S,D,B]} {7,[S,D,B]}
3  R!H u0 {2,[S,D,B]} {4,[S,D,B]} {8,[S,D,B]}
4  R!H u0 {1,[S,D,B]} {3,[S,D,B]} {9,[S,D,B]}
5  R!H u0 {1,[S,D,B]} {2,[S,D,B]} {12,[S,D,B]}
6  R!H u0 {1,[S,D,B]} {10,[S,D,B]} {11,[S,D,B]}
7  R!H u0 {2,[S,D,B]} {14,[S,D,B]}
8  R!H u0 {3,[S,D,B]} {13,[S,D,B]}
9  R!H u0 {4,[S,D,B]} {15,[S,D,B]}
10 R!H u0 {6,[S,D,B]} {15,[S,D,B]}
11 R!H u0 {6,[S,D,B]} {16,[S,D,B]}
12 R!H u0 {5,[S,D,B]} {16,[S,D,B]}
13 R!H u0 {8,[S,D,B]} {14,[S,D,B]}
14 R!H u0 {7,[S,D,B]} {13,[S,D,B]} 
15 R!H u0 {9,[S,D,B]} {10,[S,D,B]}
16 R!H u0 {11,[S,D,B]} {12,[S,D,B]}
""",
	solute = u'Fluoranthene',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 32,
	label = "Fluoranthene",
	group = 
"""
1  * C u0 {4,B} {5,B} {6,B}
2  C u0 {3,B} {5,S} {7,B}
3  C u0 {2,B} {4,S} {8,B}
4  C u0 {1,B} {3,S} {9,B}
5  C u0 {1,B} {2,S} {12,B}
6  C u0 {1,B} {10,B} {11,B}
7  C u0 {2,B} {14,B}
8  C u0 {3,B} {13,B}
9  C u0 {4,B} {15,B}
10 C u0 {6,B} {15,B}
11 C u0 {6,B} {16,B}
12 C u0 {5,B} {16,B}
13 C u0 {8,B} {14,B}
14 C u0 {7,B} {13,B}
15 C u0 {9,B} {10,B}
16 C u0 {11,B} {12,B}
""",
	solute = SoluteData(
		S = -0.00838,
		B = -0.00639,
		E = 0.00714,
		L = 0.22045,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 3,
		L = 2,
		A = 3,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 33,
	label = "s3_6_6_s3_6_6_s3_6_6",
	group = 
"""
1  * R!H u0 {2,[S,D,B]} {3,[S,D,B]} {6,[S,D,B]}
2  R!H u0 {1,[S,D,B]} {4,[S,D,B]} {5,[S,D,B]}
3  R!H u0 {1,[S,D,B]} {7,[S,D,B]} {8,[S,D,B]}
4  R!H u0 {2,[S,D,B]} {9,[S,D,B]} {10,[S,D,B]}
5  R!H u0 {2,[S,D,B]} {11,[S,D,B]} {12,[S,D,B]}
6  R!H u0 {1,[S,D,B]} {13,[S,D,B]} {14,[S,D,B]}
7  R!H u0 {3,[S,D,B]} {15,[S,D,B]}
8  R!H u0 {3,[S,D,B]} {9,[S,D,B]}
9  R!H u0 {4,[S,D,B]} {8,[S,D,B]}
10 R!H u0 {4,[S,D,B]} {16,[S,D,B]}
11 R!H u0 {5,[S,D,B]} {16,[S,D,B]}
12 R!H u0 {5,[S,D,B]} {13,[S,D,B]}
13 R!H u0 {6,[S,D,B]} {12,[S,D,B]}
14 * R!H u0 {6,[S,D,B]} {15,[S,D,B]}
15 R!H u0 {7,[S,D,B]} {14,[S,D,B]}
16 R!H u0 {10,[S,D,B]} {11,[S,D,B]}
""",
	solute = u's3_6_6_s3_6_6_s3_6_6_pyrene',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 34,
	label = "s3_6_6_s3_6_6_s3_6_6_pyrene",
	group = 
"""
1  * C u0 {2,B} {3,B} {6,B}
2  C u0 {1,B} {4,B} {5,B}
3  C u0 {1,B} {7,B} {8,B}
4  C u0 {2,B} {9,B} {10,B}
5  C u0 {2,B} {11,B} {12,B}
6  C u0 {1,B} {13,B} {14,B}
7  C u0 {3,B} {15,B}
8  C u0 {3,B} {9,B}
9  C u0 {4,B} {8,B}
10 C u0 {4,B} {16,B}
11 C u0 {5,B} {16,B}
12 C u0 {5,B} {13,B}
13 C u0 {6,B} {12,B}
14 * C u0 {6,B} {15,B}
15 C u0 {7,B} {14,B}
16 C u0 {10,B} {11,B}
""",
	solute = SoluteData(
		S = 0.10088,
		B = -0.01296,
		E = 0.17247,
		L = 0.12107,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 12,
		B = 12,
		E = 17,
		L = 16,
		A = 17,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 35,
	label = "s2_5_6_s2_6_6_s2_6_6",
	group = 
"""
1  * R!H u0 {2,[S,D,B]} {17,[S,D,B]}
2    R!H u0 {1,[S,D,B]} {3,[S,D,B]}
3    R!H u0 {2,[S,D,B]} {4,[S,D,B]} {15,[S,D,B]}
4    R!H u0 {3,[S,D,B]} {5,[S,D,B]}
5    R!H u0 {4,[S,D,B]} {6,[S,D,B]}
6    R!H u0 {5,[S,D,B]} {7,[S,D,B]} {14,[S,D,B]}
7    R!H u0 {6,[S,D,B]} {8,[S,D,B]} {11,[S,D,B]}
8    R!H u0 {7,[S,D,B]} {9,[S,D,B]}
9    R!H u0 {8,[S,D,B]} {10,[S,D,B]}
10   R!H u0 {9,[S,D,B]} {11,[S,D,B]}
11   R!H u0 {7,[S,D,B]} {10,[S,D,B]} {12,[S,D,B]}
12   R!H u0 {11,[S,D,B]} {13,[S,D,B]}
13   R!H u0 {12,[S,D,B]} {14,[S,D,B]}
14   R!H u0 {6,[S,D,B]} {13,[S,D,B]} {15,[S,D,B]}
15   R!H u0 {3,[S,D,B]} {14,[S,D,B]} {16,[S,D,B]}
16   R!H u0 {15,[S,D,B]} {17,[S,D,B]}
17   R!H u0 {1,[S,D,B]} {16,[S,D,B]}
""",
	solute = SoluteData(
		S = 0.12106,
		B = -0.00552,
		E = -0.02452,
		L = 0.38087,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 7,
		B = 7,
		E = 7,
		L = 6,
		A = 8,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 36,
	label = "s2_5_6_s2_6_6_s2_6_6_ben",
	group = 
"""
1  * Cb  u0 {2,B} {17,B}
2    Cb  u0 {1,B} {3,B}
3    Cb  u0 {2,B} {4,S} {15,B}
4    R!H u0 {3,S} {5,S}
5    R!H u0 {4,S} {6,S}
6    R!H u0 {5,S} {7,S} {14,S}
7    R!H u0 {6,S} {8,S} {11,S}
8    R!H u0 {7,S} {9,S}
9    R!H u0 {8,S} {10,S}
10   R!H u0 {9,S} {11,S}
11   R!H u0 {7,S} {10,S} {12,S}
12   R!H u0 {11,S} {13,S}
13   R!H u0 {12,S} {14,S}
14   R!H u0 {6,S} {13,S} {15,S}
15   Cb  u0 {3,B} {14,S} {16,B}
16   Cb  u0 {15,B} {17,B}
17   Cb  u0 {1,B} {16,B}
""",
	solute = u's2_5_6_s2_6_6_s2_6_6_ben_onlyC',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 37,
	label = "s2_5_6_s2_6_6_s2_6_6_ben_onlyC",
	group = 
"""
1  * Cb  u0 {2,B} {17,B}
2    Cb  u0 {1,B} {3,B}
3    Cb  u0 {2,B} {4,S} {15,B}
4    C   u0 {3,S} {5,S}
5    C   u0 {4,S} {6,S}
6    C   u0 {5,S} {7,S} {14,S}
7    C   u0 {6,S} {8,S} {11,S}
8    C   u0 {7,S} {9,S}
9    C   u0 {8,S} {10,S}
10   C   u0 {9,S} {11,S}
11   C   u0 {7,S} {10,S} {12,S}
12   C   u0 {11,S} {13,S}
13   C   u0 {12,S} {14,S}
14   C   u0 {6,S} {13,S} {15,S}
15   Cb  u0 {3,B} {14,S} {16,B}
16   Cb  u0 {15,B} {17,B}
17   Cb  u0 {1,B} {16,B}
""",
	solute = SoluteData(
		S = 0.10685,
		B = 0.19609,
		E = 0.16013,
		L = 0.04345,
		A = 0.09970,
	),
	dataCount = DataCountGAV(
		S = 10,
		B = 10,
		E = 10,
		L = 10,
		A = 10,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 38,
	label = "s2_5_6_s2_6_6_s2_6_6_ane",
	group = 
"""
1  * R!H u0 {2,S} {17,S}
2    R!H u0 {1,S} {3,S}
3    R!H u0 {2,S} {4,S} {15,S}
4    R!H u0 {3,S} {5,S}
5    R!H u0 {4,S} {6,S}
6    R!H u0 {5,S} {7,S} {14,S}
7    R!H u0 {6,S} {8,S} {11,S}
8    R!H u0 {7,S} {9,S}
9    R!H u0 {8,S} {10,S}
10   R!H u0 {9,S} {11,S}
11   R!H u0 {7,S} {10,S} {12,S}
12   R!H u0 {11,S} {13,S}
13   R!H u0 {12,S} {14,S}
14   R!H u0 {6,S} {13,S} {15,S}
15   R!H u0 {3,S} {14,S} {16,S}
16   R!H u0 {15,S} {17,S}
17   R!H u0 {1,S} {16,S}
""",
	solute = u's2_5_6_s2_6_6_s2_6_6_ane_onlyC',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 39,
	label = "s2_5_6_s2_6_6_s2_6_6_ane_onlyC",
	group = 
"""
1  * C  u0 {2,S} {17,S}
2    C  u0 {1,S} {3,S}
3    C  u0 {2,S} {4,S} {15,S}
4    C  u0 {3,S} {5,S}
5    C  u0 {4,S} {6,S}
6    C  u0 {5,S} {7,S} {14,S}
7    C  u0 {6,S} {8,S} {11,S}
8    C  u0 {7,S} {9,S}
9    C  u0 {8,S} {10,S}
10   C  u0 {9,S} {11,S}
11   C  u0 {7,S} {10,S} {12,S}
12   C  u0 {11,S} {13,S}
13   C  u0 {12,S} {14,S}
14   C  u0 {6,S} {13,S} {15,S}
15   C  u0 {3,S} {14,S} {16,S}
16   C  u0 {15,S} {17,S}
17   C  u0 {1,S} {16,S}
""",
	solute = SoluteData(
		S = 0.17040,
		B = 0.00000,
		E = -0.05725,
		L = 0.25677,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 8,
		B = 8,
		E = 8,
		L = 6,
		A = 8,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 40,
	label = "s2_5_6_s2_6_6_s2_6_6_ane_onlyC(=O)",
	group = 
"""
1  * CO u0 {2,S} {17,S}
2    C  u0 {1,S} {3,S}
3    C  u0 {2,S} {4,S} {15,S}
4    C  u0 {3,S} {5,S}
5    C  u0 {4,S} {6,S}
6    C  u0 {5,S} {7,S} {14,S}
7    C  u0 {6,S} {8,S} {11,S}
8    C  u0 {7,S} {9,S}
9    C  u0 {8,S} {10,S}
10   C  u0 {9,S} {11,S}
11   C  u0 {7,S} {10,S} {12,S}
12   C  u0 {11,S} {13,S}
13   C  u0 {12,S} {14,S}
14   C  u0 {6,S} {13,S} {15,S}
15   C  u0 {3,S} {14,S} {16,S}
16   C  u0 {15,S} {17,S}
17   C  u0 {1,S} {16,S}
""",
	solute = SoluteData(
		S = 0.16022,
		B = 0.06922,
		E = 0.00919,
		L = 0.29073,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 6,
		B = 6,
		E = 6,
		L = 5,
		A = 6,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 41,
	label = "s2_5_6_s2_6_6_s2_6_6_ene_2",
	group = 
"""
1  * R!H u0 {2,S} {17,S}
2    R!H u0 {1,S} {3,D}
3    R!H u0 {2,D} {4,S} {15,S}
4    R!H u0 {3,S} {5,S}
5    R!H u0 {4,S} {6,S}
6    R!H u0 {5,S} {7,S} {14,S}
7    R!H u0 {6,S} {8,S} {11,S}
8    R!H u0 {7,S} {9,S}
9    R!H u0 {8,S} {10,S}
10   R!H u0 {9,S} {11,S}
11   R!H u0 {7,S} {10,S} {12,S}
12   R!H u0 {11,S} {13,S}
13   R!H u0 {12,S} {14,S}
14   R!H u0 {6,S} {13,S} {15,S}
15   R!H u0 {3,S} {14,S} {16,S}
16   R!H u0 {15,S} {17,S}
17   R!H u0 {1,S} {16,S}
""",
	solute = u's2_5_6_s2_6_6_s2_6_6_ene_2_onlyC',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 42,
	label = "s2_5_6_s2_6_6_s2_6_6_ene_2_onlyC",
	group = 
"""
1  * C  u0 {2,S} {17,S}
2    C  u0 {1,S} {3,D}
3    C  u0 {2,D} {4,S} {15,S}
4    C  u0 {3,S} {5,S}
5    C  u0 {4,S} {6,S}
6    C  u0 {5,S} {7,S} {14,S}
7    C  u0 {6,S} {8,S} {11,S}
8    C  u0 {7,S} {9,S}
9    C  u0 {8,S} {10,S}
10   C  u0 {9,S} {11,S}
11   C  u0 {7,S} {10,S} {12,S}
12   C  u0 {11,S} {13,S}
13   C  u0 {12,S} {14,S}
14   C  u0 {6,S} {13,S} {15,S}
15   C  u0 {3,S} {14,S} {16,S}
16   C  u0 {15,S} {17,S}
17   C  u0 {1,S} {16,S}
""",
	solute = u's2_5_6_s2_6_6_s2_6_6_ene_2_onlyC(=O)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 43,
	label = "s2_5_6_s2_6_6_s2_6_6_ene_2_onlyC(=O)",
	group = 
"""
1  * CO u0 {2,S} {17,S}
2    C  u0 {1,S} {3,D}
3    C  u0 {2,D} {4,S} {15,S}
4    C  u0 {3,S} {5,S}
5    C  u0 {4,S} {6,S}
6    C  u0 {5,S} {7,S} {14,S}
7    C  u0 {6,S} {8,S} {11,S}
8    C  u0 {7,S} {9,S}
9    C  u0 {8,S} {10,S}
10   C  u0 {9,S} {11,S}
11   C  u0 {7,S} {10,S} {12,S}
12   C  u0 {11,S} {13,S}
13   C  u0 {12,S} {14,S}
14   C  u0 {6,S} {13,S} {15,S}
15   C  u0 {3,S} {14,S} {16,S}
16   C  u0 {15,S} {17,S}
17   C  u0 {1,S} {16,S}
""",
	solute = SoluteData(
		S = 0.04818,
		B = 0.03208,
		E = -0.00754,
		L = 0.04223,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 63,
		B = 63,
		E = 63,
		L = 53,
		A = 63,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 44,
	label = "s2_5_6_s2_6_6_s2_6_6_ene_3",
	group = 
"""
1  * R!H u0 {2,S} {17,S}
2    R!H u0 {1,S} {3,S}
3    R!H u0 {2,S} {4,D} {15,S}
4    R!H u0 {3,D} {5,S}
5    R!H u0 {4,S} {6,S}
6    R!H u0 {5,S} {7,S} {14,S}
7    R!H u0 {6,S} {8,S} {11,S}
8    R!H u0 {7,S} {9,S}
9    R!H u0 {8,S} {10,S}
10   R!H u0 {9,S} {11,S}
11   R!H u0 {7,S} {10,S} {12,S}
12   R!H u0 {11,S} {13,S}
13   R!H u0 {12,S} {14,S}
14   R!H u0 {6,S} {13,S} {15,S}
15   R!H u0 {3,S} {14,S} {16,S}
16   R!H u0 {15,S} {17,S}
17   R!H u0 {1,S} {16,S}
""",
	solute = u's2_5_6_s2_6_6_s2_6_6_ene_3_onlyC',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 45,
	label = "s2_5_6_s2_6_6_s2_6_6_ene_3_onlyC",
	group = 
"""
1  * C  u0 {2,S} {17,S}
2    C  u0 {1,S} {3,S}
3    C  u0 {2,S} {4,D} {15,S}
4    C  u0 {3,D} {5,S}
5    C  u0 {4,S} {6,S}
6    C  u0 {5,S} {7,S} {14,S}
7    C  u0 {6,S} {8,S} {11,S}
8    C  u0 {7,S} {9,S}
9    C  u0 {8,S} {10,S}
10   C  u0 {9,S} {11,S}
11   C  u0 {7,S} {10,S} {12,S}
12   C  u0 {11,S} {13,S}
13   C  u0 {12,S} {14,S}
14   C  u0 {6,S} {13,S} {15,S}
15   C  u0 {3,S} {14,S} {16,S}
16   C  u0 {15,S} {17,S}
17   C  u0 {1,S} {16,S}
""",
	solute = SoluteData(
		S = 0.10513,
		B = 0.02489,
		E = -0.02957,
		L = 0.43057,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 6,
		B = 6,
		E = 6,
		L = 4,
		A = 6,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 46,
	label = "s2_5_6_s2_6_6_s2_6_6_diene_2_16",
	group = 
"""
1  * R!H u0 {2,S} {17,S}
2    R!H u0 {1,S} {3,D}
3    R!H u0 {2,D} {4,S} {15,S}
4    R!H u0 {3,S} {5,S}
5    R!H u0 {4,S} {6,S}
6    R!H u0 {5,S} {7,S} {14,S}
7    R!H u0 {6,S} {8,S} {11,S}
8    R!H u0 {7,S} {9,S}
9    R!H u0 {8,S} {10,S}
10   R!H u0 {9,S} {11,S}
11   R!H u0 {7,S} {10,S} {12,S}
12   R!H u0 {11,S} {13,S}
13   R!H u0 {12,S} {14,S}
14   R!H u0 {6,S} {13,S} {15,S}
15   R!H u0 {3,S} {14,S} {16,S}
16   R!H u0 {15,S} {17,D}
17   R!H u0 {1,S} {16,D}
""",
	solute = u's2_5_6_s2_6_6_s2_6_6_diene_2_16_onlyC',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 47,
	label = "s2_5_6_s2_6_6_s2_6_6_diene_2_16_onlyC",
	group = 
"""
1  * C  u0 {2,S} {17,S}
2    C  u0 {1,S} {3,D}
3    C  u0 {2,D} {4,S} {15,S}
4    C  u0 {3,S} {5,S}
5    C  u0 {4,S} {6,S}
6    C  u0 {5,S} {7,S} {14,S}
7    C  u0 {6,S} {8,S} {11,S}
8    C  u0 {7,S} {9,S}
9    C  u0 {8,S} {10,S}
10   C  u0 {9,S} {11,S}
11   C  u0 {7,S} {10,S} {12,S}
12   C  u0 {11,S} {13,S}
13   C  u0 {12,S} {14,S}
14   C  u0 {6,S} {13,S} {15,S}
15   C  u0 {3,S} {14,S} {16,S}
16   C  u0 {15,S} {17,D}
17   C  u0 {1,S} {16,D}
""",
	solute = u's2_5_6_s2_6_6_s2_6_6_diene_2_16_onlyC(=O)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 48,
	label = "s2_5_6_s2_6_6_s2_6_6_diene_2_16_onlyC(=O)",
	group = 
"""
1  * CO u0 {2,S} {17,S}
2    C  u0 {1,S} {3,D}
3    C  u0 {2,D} {4,S} {15,S}
4    C  u0 {3,S} {5,S}
5    C  u0 {4,S} {6,S}
6    C  u0 {5,S} {7,S} {14,S}
7    C  u0 {6,S} {8,S} {11,S}
8    C  u0 {7,S} {9,S}
9    C  u0 {8,S} {10,S}
10   C  u0 {9,S} {11,S}
11   C  u0 {7,S} {10,S} {12,S}
12   C  u0 {11,S} {13,S}
13   C  u0 {12,S} {14,S}
14   C  u0 {6,S} {13,S} {15,S}
15   C  u0 {3,S} {14,S} {16,S}
16   C  u0 {15,S} {17,D}
17   C  u0 {1,S} {16,D}
""",
	solute = SoluteData(
		S = 0.19379,
		B = 0.05248,
		E = 0.05417,
		L = 0.24345,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 12,
		B = 12,
		E = 12,
		L = 8,
		A = 12,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 49,
	label = "s2_5_6_s2_6_6_s2_6_6_diene_2_4",
	group = 
"""
1  * R!H u0 {2,S} {17,S}
2    R!H u0 {1,S} {3,D}
3    R!H u0 {2,D} {4,S} {15,S}
4    R!H u0 {3,S} {5,D}
5    R!H u0 {4,D} {6,S}
6    R!H u0 {5,S} {7,S} {14,S}
7    R!H u0 {6,S} {8,S} {11,S}
8    R!H u0 {7,S} {9,S}
9    R!H u0 {8,S} {10,S}
10   R!H u0 {9,S} {11,S}
11   R!H u0 {7,S} {10,S} {12,S}
12   R!H u0 {11,S} {13,S}
13   R!H u0 {12,S} {14,S}
14   R!H u0 {6,S} {13,S} {15,S}
15   R!H u0 {3,S} {14,S} {16,S}
16   R!H u0 {15,S} {17,S}
17   R!H u0 {1,S} {16,S}
""",
	solute = u's2_5_6_s2_6_6_s2_6_6_diene_2_4_onlyC',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 50,
	label = "s2_5_6_s2_6_6_s2_6_6_diene_2_4_onlyC",
	group = 
"""
1  * C u0 {2,S} {17,S}
2    C u0 {1,S} {3,D}
3    C u0 {2,D} {4,S} {15,S}
4    C u0 {3,S} {5,D}
5    C u0 {4,D} {6,S}
6    C u0 {5,S} {7,S} {14,S}
7    C u0 {6,S} {8,S} {11,S}
8    C u0 {7,S} {9,S}
9    C u0 {8,S} {10,S}
10   C u0 {9,S} {11,S}
11   C u0 {7,S} {10,S} {12,S}
12   C u0 {11,S} {13,S}
13   C u0 {12,S} {14,S}
14   C u0 {6,S} {13,S} {15,S}
15   C u0 {3,S} {14,S} {16,S}
16   C u0 {15,S} {17,S}
17   C u0 {1,S} {16,S}
""",
	solute = u's2_5_6_s2_6_6_s2_6_6_diene_2_4_onlyC(=O)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 51,
	label = "s2_5_6_s2_6_6_s2_6_6_diene_2_4_onlyC(=O)",
	group = 
"""
1  * CO u0 {2,S} {17,S}
2    C u0 {1,S} {3,D}
3    C u0 {2,D} {4,S} {15,S}
4    C u0 {3,S} {5,D}
5    C u0 {4,D} {6,S}
6    C u0 {5,S} {7,S} {14,S}
7    C u0 {6,S} {8,S} {11,S}
8    C u0 {7,S} {9,S}
9    C u0 {8,S} {10,S}
10   C u0 {9,S} {11,S}
11   C u0 {7,S} {10,S} {12,S}
12   C u0 {11,S} {13,S}
13   C u0 {12,S} {14,S}
14   C u0 {6,S} {13,S} {15,S}
15   C u0 {3,S} {14,S} {16,S}
16   C u0 {15,S} {17,S}
17   C u0 {1,S} {16,S}
""",
	solute = SoluteData(
		S = 0.04583,
		B = 0.02142,
		E = 0.04648,
		L = 0.34717,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 3,
		L = 2,
		A = 3,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 52,
	label = "s2_5_6_s2_6_6_s2_6_6_triene_2_12_14",
	group = 
"""
1  * R!H u0 {2,S} {17,S}
2    R!H u0 {1,S} {3,D}
3    R!H u0 {2,D} {4,S} {15,S}
4    R!H u0 {3,S} {5,S}
5    R!H u0 {4,S} {6,S}
6    R!H u0 {5,S} {7,S} {14,S}
7    R!H u0 {6,S} {8,S} {11,S}
8    R!H u0 {7,S} {9,S}
9    R!H u0 {8,S} {10,S}
10   R!H u0 {9,S} {11,S}
11   R!H u0 {7,S} {10,S} {12,S}
12   R!H u0 {11,S} {13,D}
13   R!H u0 {12,D} {14,S}
14   R!H u0 {6,S} {13,S} {15,D}
15   R!H u0 {3,S} {14,D} {16,S}
16   R!H u0 {15,S} {17,S}
17   R!H u0 {1,S} {16,S}
""",
	solute = u's2_5_6_s2_6_6_s2_6_6_triene_2_12_14_onlyC',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 53,
	label = "s2_5_6_s2_6_6_s2_6_6_triene_2_12_14_onlyC",
	group = 
"""
1  * C u0 {2,S} {17,S}
2    C u0 {1,S} {3,D}
3    C u0 {2,D} {4,S} {15,S}
4    C u0 {3,S} {5,S}
5    C u0 {4,S} {6,S}
6    C u0 {5,S} {7,S} {14,S}
7    C u0 {6,S} {8,S} {11,S}
8    C u0 {7,S} {9,S}
9    C u0 {8,S} {10,S}
10   C u0 {9,S} {11,S}
11   C u0 {7,S} {10,S} {12,S}
12   C u0 {11,S} {13,D}
13   C u0 {12,D} {14,S}
14   C u0 {6,S} {13,S} {15,D}
15   C u0 {3,S} {14,D} {16,S}
16   C u0 {15,S} {17,S}
17   C u0 {1,S} {16,S}
""",
	solute = SoluteData(
		S = 0.06874,
		B = 0.03920,
		E = -0.03672,
		L = 0.08413,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
		E = 2,
		L = 2,
		A = 2,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 54,
	label = "s2_6_6_s2_6_6_s2_6_6",
	group = 
"""
1  R!H u0 {2,[S,D,B]} {4,[S,D,B]} {7,[S,D,B]}
2  R!H u0 {1,[S,D,B]} {6,[S,D,B]} {14,[S,D,B]}
3  R!H u0 {5,[S,D,B]} {7,[S,D,B]} {9,[S,D,B]}
4  R!H u0 {1,[S,D,B]} {8,[S,D,B]} {11,[S,D,B]}
5  R!H u0 {3,[S,D,B]} {8,[S,D,B]} {10,[S,D,B]}
6  R!H u0 {2,[S,D,B]} {12,[S,D,B]} {13,[S,D,B]}
7  R!H u0 {1,[S,D,B]} {3,[S,D,B]}
8  R!H u0 {4,[S,D,B]} {5,[S,D,B]}
9  R!H u0 {3,[S,D,B]} {16,[S,D,B]}
10 R!H u0 {5,[S,D,B]} {15,[S,D,B]}
11 R!H u0 {4,[S,D,B]} {12,[S,D,B]}
12 R!H u0 {6,[S,D,B]} {11,[S,D,B]}
13 R!H u0 {6,[S,D,B]} {17,[S,D,B]}
14 R!H u0 {2,[S,D,B]} {18,[S,D,B]}
15 R!H u0 {10,[S,D,B]} {16,[S,D,B]}
16 R!H u0 {9,[S,D,B]} {15,[S,D,B]}
17 R!H u0 {13,[S,D,B]} {18,[S,D,B]}
18 * R!H u0 {14,[S,D,B]} {17,[S,D,B]}
""",
	solute = u's2_6_6_s2_6_6_s2_6_6_aromatic',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 55,
	label = "s2_6_6_s2_6_6_s2_6_6_aromatic",
	group =  "OR{s2_6_6_s2_6_6_s2_6_6_benz[a]anthracene, s2_6_6_s2_6_6_s2_6_6_benzacridine1, \
s2_6_6_s2_6_6_s2_6_6_benzacridine2, s2_6_6_s2_6_6_s2_6_6_benzacridine3, s2_6_6_s2_6_6_s2_6_6_benzacridine4, \
s2_6_6_s2_6_6_s2_6_6_benzacridine5}",
	solute = u's2_6_6_s2_6_6_s2_6_6_benz[a]anthracene',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 56,
	label = "s2_6_6_s2_6_6_s2_6_6_benzacridine1",
	group = 
"""
1  N u0 {6,D} {7,S}
2  C u0 {3,S} {4,B} {9,B}
3  C u0 {2,S} {6,S} {8,D}
4  C u0 {2,B} {10,B} {11,S}
5  C u0 {7,B} {8,S} {12,B}
6  C u0 {1,D} {3,S} {13,S}
7  C u0 {1,S} {5,B} {14,B}
8  C u0 {3,D} {5,S}
9  C u0 {2,B} {16,B}
10 C u0 {4,B} {15,B}
11 C u0 {4,S} {13,D}
12 C u0 {5,B} {18,B}
13 C u0 {6,S} {11,D}
14 C u0 {7,B} {17,B}
15 C u0 {10,B} {16,B}
16 * C u0 {9,B} {15,B}
17 C u0 {14,B} {18,B}
18 C u0 {12,B} {17,B}
""",
	solute = u's2_6_6_s2_6_6_s2_6_6_benzacridine',
	dataCount = None,
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
this is one of the groups that belong to s2_6_6_s2_6_6_s2_6_6_benzacridine
""",
)

entry(
	index = 57,
	label = "s2_6_6_s2_6_6_s2_6_6_benzacridine2",
	group = 
"""
1  N u0 {6,S} {7,D}
2  C u0 {3,B} {4,B} {12,B}
3  C u0 {2,B} {6,B} {8,S}
4  C u0 {2,B} {10,B} {11,B}
5  C u0 {7,S} {8,D} {9,S}
6  C u0 {1,S} {3,B} {13,B}
7  C u0 {1,D} {5,S} {14,S}
8  C u0 {3,S} {5,D}
9  C u0 {5,S} {15,D}
10 C u0 {4,B} {13,B}
11 C u0 {4,B} {16,B}
12 C u0 {2,B} {17,B}
13 C u0 {6,B} {10,B}
14 C u0 {7,S} {18,D}
15 C u0 {9,D} {18,S}
16 C u0 {11,B} {17,B}
17 * C u0 {12,B} {16,B}
18 C u0 {14,D} {15,S}
""",
	solute = u's2_6_6_s2_6_6_s2_6_6_benzacridine',
	dataCount = None,
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
this is one of the groups that belong to s2_6_6_s2_6_6_s2_6_6_benzacridine
""",
)

entry(
	index = 58,
	label = "s2_6_6_s2_6_6_s2_6_6_benzacridine3",
	group = 
"""
1  N u0 {6,D} {7,S}
2  C u0 {3,B} {6,S} {12,B}
3  C u0 {2,B} {11,S} {13,B}
4  C u0 {7,B} {8,S} {9,B}
5  C u0 {6,S} {8,D} {10,S}
6  C u0 {1,D} {2,S} {5,S}
7  C u0 {1,S} {4,B} {14,B}
8  C u0 {4,S} {5,D}
9  C u0 {4,B} {16,B}
10 C u0 {5,S} {11,D}
11 C u0 {3,S} {10,D}
12 C u0 {2,B} {17,B}
13 C u0 {3,B} {18,B}
14 C u0 {7,B} {15,B}
15 C u0 {14,B} {16,B} 
16 C u0 {9,B} {15,B}
17 * C u0 {12,B} {18,B}
18 C u0 {13,B} {17,B}
""",
	solute = u's2_6_6_s2_6_6_s2_6_6_benzacridine',
	dataCount = None,
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
this is one of the groups that belong to s2_6_6_s2_6_6_s2_6_6_benzacridine
""",
)

entry(
	index = 59,
	label = "s2_6_6_s2_6_6_s2_6_6_benzacridine4",
	group = 
"""
1  N u0 {6,D} {7,S}
2  C u0 {3,B} {6,S} {9,B}
3  C u0 {2,B} {10,B} {11,S}
4  C u0 {6,S} {8,D} {12,S}
5  C u0 {7,B} {8,S} {13,B}
6  C u0 {1,D} {2,S} {4,S}
7  C u0 {1,S} {5,B} {14,B}
8  C u0 {4,D} {5,S}
9  C u0 {2,B} {16,B}
10 C u0 {3,B} {15,B}
11 C u0 {3,S} {12,D}
12 C u0 {4,S} {11,D}
13 C u0 {5,B} {17,B}
14 C u0 {7,B} {18,B}
15 C u0 {10,B} {16,B}
16 * C u0 {9,B} {15,B}
17 C u0 {13,B} {18,B}
18 C u0 {14,B} {17,B}
""",
	solute = u's2_6_6_s2_6_6_s2_6_6_benzacridine',
	dataCount = None,
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
this is one of the groups that belong to s2_6_6_s2_6_6_s2_6_6_benzacridine
""",
)

entry(
	index = 60,
	label = "s2_6_6_s2_6_6_s2_6_6_benzacridine5",
	group = 
"""
1  N u0 {6,S} {7,D}
2  C u0 {3,B} {6,B} {12,B}
3  C u0 {2,B} {10,B} {11,B}
4  C u0 {6,B} {8,S} {9,B}
5  C u0 {7,S} {8,D} {13,S}
6  C u0 {1,S} {2,B} {4,B}
7  C u0 {1,D} {5,S} {14,S}
8  C u0 {4,S} {5,D}
9  C u0 {4,B} {10,B}
10 C u0 {3,B} {9,B}
11 C u0 {3,B} {16,B}
12 C u0 {2,B} {17,B}
13 C u0 {5,S} {18,D}
14 C u0 {7,S} {15,D}
15 C u0 {14,D} {18,S}
16 C u0 {11,B} {17,B}
17 * C u0 {12,B} {16,B}
18 C u0 {13,D} {15,S}
""",
	solute = u's2_6_6_s2_6_6_s2_6_6_benzacridine',
	dataCount = None,
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
this is one of the groups that belong to s2_6_6_s2_6_6_s2_6_6_benzacridine
""",
)

entry(
	index = 61,
	label = "s2_6_6_s2_6_6_s2_6_6_benz[a]anthracene",
	group = 
"""
1  C u0 {2,B} {4,B} {7,B}
2  C u0 {1,B} {6,B} {14,B}
3  C u0 {5,B} {7,B} {9,B}
4  C u0 {1,B} {8,B} {11,B}
5  C u0 {3,B} {8,B} {10,B}
6  C u0 {2,B} {12,B} {13,B}
7  C u0 {1,B} {3,B}
8  C u0 {4,B} {5,B}
9  C u0 {3,B} {16,B}
10 C u0 {5,B} {15,B}
11 C u0 {4,B} {12,B}
12 C u0 {6,B} {11,B}
13 C u0 {6,B} {17,B}
14 C u0 {2,B} {18,B}
15 C u0 {10,B} {16,B}
16 C u0 {9,B} {15,B}
17 C u0 {13,B} {18,B}
18 * C u0 {14,B} {17,B}
""",
	solute = SoluteData(
		S = -0.03349,
		B = 0.02413,
		E = -0.02557,
		L = -0.18099,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 9,
		B = 9,
		E = 18,
		L = 16,
		A = 18,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 62,
	label = "s2_6_6_s2_6_6_s2_6_6_benzacridine",
	group = 
"""
1  R!H u0 {2,[S,D,B]} {4,[S,D,B]} {7,[S,D,B]}
2  R!H u0 {1,[S,D,B]} {6,[S,D,B]} {14,[S,D,B]}
3  R!H u0 {5,[S,D,B]} {7,[S,D,B]} {9,[S,D,B]}
4  R!H u0 {1,[S,D,B]} {8,[S,D,B]} {11,[S,D,B]}
5  R!H u0 {3,[S,D,B]} {8,[S,D,B]} {10,[S,D,B]}
6  R!H u0 {2,[S,D,B]} {12,[S,D,B]} {13,[S,D,B]}
7  R!H u0 {1,[S,D,B]} {3,[S,D,B]}
8  R!H u0 {4,[S,D,B]} {5,[S,D,B]}
9  R!H u0 {3,[S,D,B]} {16,[S,D,B]}
10 R!H u0 {5,[S,D,B]} {15,[S,D,B]}
11 R!H u0 {4,[S,D,B]} {12,[S,D,B]}
12 R!H u0 {6,[S,D,B]} {11,[S,D,B]}
13 R!H u0 {6,[S,D,B]} {17,[S,D,B]}
14 R!H u0 {2,[S,D,B]} {18,[S,D,B]}
15 R!H u0 {10,[S,D,B]} {16,[S,D,B]}
16 R!H u0 {9,[S,D,B]} {15,[S,D,B]}
17 R!H u0 {13,[S,D,B]} {18,[S,D,B]}
18 * R!H u0 {14,[S,D,B]} {17,[S,D,B]}
""",
	solute = SoluteData(
		S = 0.02388,
		B = -0.01301,
		E = 0.36148,
		L = 0.20888,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 6,
		B = 1,
		E = 9,
		L = 9,
		A = 3,
	),
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
dummy group to put all s2_6_6_s2_6_6_s2_6_6_benzacridine groups (s2_6_6_s2_6_6_s2_6_6_benzacridine1-5) together
""",
)

entry(
	index = 63,
	label = "s2_6_6_s2_6_6_s2_6_6_A",
	group = 
"""
1  * R!H u0 {4,[S,D,B]} {5,[S,D,B]} {7,[S,D,B]}
2  R!H u0 {3,[S,D,B]} {4,[S,D,B]} {10,[S,D,B]}
3  R!H u0 {2,[S,D,B]} {6,[S,D,B]} {11,[S,D,B]}
4  R!H u0 {1,[S,D,B]} {2,[S,D,B]} {14,[S,D,B]}
5  R!H u0 {1,[S,D,B]} {8,[S,D,B]} {9,[S,D,B]}
6  R!H u0 {3,[S,D,B]} {12,[S,D,B]} {13,[S,D,B]}
7  R!H u0 {1,[S,D,B]} {16,[S,D,B]}
8  R!H u0 {5,[S,D,B]} {15,[S,D,B]}
9  R!H u0 {5,[S,D,B]} {10,[S,D,B]}
10 R!H u0 {2,[S,D,B]} {9,[S,D,B]}
11 R!H u0 {3,[S,D,B]} {17,[S,D,B]}
12 R!H u0 {6,[S,D,B]} {18,[S,D,B]}
13 R!H u0 {6,[S,D,B]} {14,[S,D,B]}
14 R!H u0 {4,[S,D,B]} {13,[S,D,B]}
15 R!H u0 {8,[S,D,B]} {16,[S,D,B]}
16 R!H u0 {7,[S,D,B]} {15,[S,D,B]}
17 R!H u0 {11,[S,D,B]} {18,[S,D,B]}
18 R!H u0 {12,[S,D,B]} {17,[S,D,B]}
""",
	solute = u's2_6_6_s2_6_6_s2_6_6_A_chrysene',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 64,
	label = "s2_6_6_s2_6_6_s2_6_6_A_chrysene",
	group = 
"""
1  * C u0 {4,B} {5,B} {7,B}
2  C u0 {3,B} {4,B} {10,B}
3  C u0 {2,B} {6,B} {11,B}
4  C u0 {1,B} {2,B} {14,B}
5  C u0 {1,B} {8,B} {9,B}
6  C u0 {3,B} {12,B} {13,B}
7  C u0 {1,B} {16,B}
8  C u0 {5,B} {15,B}
9  C u0 {5,B} {10,B}
10 C u0 {2,B} {9,B}
11 C u0 {3,B} {17,B}
12 C u0 {6,B} {18,B}
13 C u0 {6,B} {14,B}
14 C u0 {4,B} {13,B}
15 C u0 {8,B} {16,B}
16 C u0 {7,B} {15,B}
17 C u0 {11,B} {18,B}
18 C u0 {12,B} {17,B}
""",
	solute = SoluteData(
		S = -0.01431,
		B = 0.01003,
		E = -0.08884,
		L = 0.02838,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 9,
		B = 9,
		E = 9,
		L = 8,
		A = 9,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 65,
	label = "s2_6_6_s2_6_6_s2_6_6_B",
	group = 
"""
1  * R!H u0 {2,[S,D,B]} {4,[S,D,B]} {5,[S,D,B]}
2  R!H u0 {1,[S,D,B]} {6,[S,D,B]} {12,[S,D,B]}
3  R!H u0 {4,[S,D,B]} {7,[S,D,B]} {9,[S,D,B]}
4  R!H u0 {1,[S,D,B]} {3,[S,D,B]}
5  R!H u0 {1,[S,D,B]} {8,[S,D,B]}
6  R!H u0 {2,[S,D,B]} {9,[S,D,B]}
7  R!H u0 {3,[S,D,B]} {10,[S,D,B]}
8  R!H u0 {5,[S,D,B]} {13,[S,D,B]}
9  R!H u0 {3,[S,D,B]} {6,[S,D,B]} {14,[S,D,B]}
10 R!H u0 {7,[S,D,B]} {11,[S,D,B]} {15,[S,D,B]}
11 R!H u0 {10,[S,D,B]} {14,[S,D,B]} {16,[S,D,B]}
12 R!H u0 {2,[S,D,B]} {13,[S,D,B]}
13 R!H u0 {8,[S,D,B]} {12,[S,D,B]}
14 R!H u0 {9,[S,D,B]} {11,[S,D,B]}
15 R!H u0 {10,[S,D,B]} {18,[S,D,B]}
16 R!H u0 {11,[S,D,B]} {17,[S,D,B]}
17 R!H u0 {16,[S,D,B]} {18,[S,D,B]}
18 R!H u0 {15,[S,D,B]} {17,[S,D,B]}
""",
	solute = u's2_6_6_s2_6_6_s2_6_6_B_ben_diene',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 66,
	label = "s2_6_6_s2_6_6_s2_6_6_B_tetracene",
	group = 
"""
1  * C u0 {2,B} {4,B} {5,B}
2  C u0 {1,B} {6,B} {12,B}
3  C u0 {4,B} {7,B} {9,B}
4  C u0 {1,B} {3,B}
5  C u0 {1,B} {8,B}
6  C u0 {2,B} {9,B}
7  C u0 {3,B} {10,B}
8  C u0 {5,B} {13,B}
9  C u0 {3,B} {6,B} {14,B}
10 C u0 {7,B} {11,B} {15,B}
11 C u0 {10,B} {14,B} {16,B}
12 C u0 {2,B} {13,B}
13 C u0 {8,B} {12,B}
14 C u0 {9,B} {11,B}
15 C u0 {10,B} {18,B}
16 C u0 {11,B} {17,B}
17 C u0 {16,B} {18,B}
18 C u0 {15,B} {17,B}
""",
	solute = SoluteData(
		S = -0.01103,
		B = 0.01066,
		E = -0.01482,
		L = -0.06004,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 1,
		B = 1,
		E = 1,
		L = 1,
		A = 1,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 67,
	label = "s2_6_6_s2_6_6_s2_6_6_B_1,2,3,4,6,11-hexahydrotetracene",
	group = 
"""
1  C u0 {2,S} {3,S}
2  C u0 {1,S} {4,S}
3  C u0 {1,S} {8,S}
4  C u0 {2,S} {7,S}
5  C u0 {10,S} {11,S}
6  C u0 {9,S} {12,S}
7  C u0 {4,S} {8,B} {13,B}
8  * C u0 {3,S} {7,B} {14,B}
9  C u0 {6,S} {10,B} {16,B}
10 C u0 {5,S} {9,B} {15,B}
11 C u0 {5,S} {12,B} {14,B}
12 C u0 {6,S} {11,B} {13,B}
13 C u0 {7,B} {12,B}
14 C u0 {8,B} {11,B}
15 C u0 {10,B} {17,B}
16 C u0 {9,B} {18,B}
17 C u0 {15,B} {18,B}
18 C u0 {16,B} {17,B}
""",
	solute = SoluteData(
		S = 0.05984,
		B = 0.14753,
		E = -0.00157,
		L = -0.19294,
		A = -0.26192,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 3,
		L = 3,
		A = 3,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 68,
	label = "s2_6_6_s2_6_6_s2_6_6_B_ben_diene",
	group = 
"""
1  * C u0 {2,S} {4,S} {5,S}
2  C u0 {1,S} {6,S} {12,S}
3  C u0 {4,S} {7,S} {9,S}
4  C u0 {1,S} {3,S}
5  C u0 {1,S} {8,S}
6  C u0 {2,S} {9,S}
7  C u0 {3,S} {10,S}
8  C u0 {5,S} {13,S}
9  C u0 {3,S} {6,S} {14,D}
10 C u0 {7,S} {11,B} {15,B}
11 C u0 {10,B} {14,S} {16,B}
12 C u0 {2,S} {13,D}
13 C u0 {8,S} {12,D}
14 C u0 {9,D} {11,S}
15 C u0 {10,B} {18,B}
16 C u0 {11,B} {17,B}
17 C u0 {16,B} {18,B}
18 C u0 {15,B} {17,B}
""",
	solute = SoluteData(
		S = -0.09062,
		B = -0.05727,
		E = -0.01586,
		L = -0.16117,
		A = 0.02541,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 3,
		L = 3,
		A = 3,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 69,
	label = "s2_6_5_s2_5_9_s3_9_6",
	group = 
"""
1  * R!H u0 {7,[S,D,B]} {8,[S,D,B]} {9,[S,D,B]}
2  R!H u0 {13,[S,D,B]} {15,[S,D,B]}
3  R!H u0 {4,[S,D,B]} {5,[S,D,B]} {7,[S,D,B]}
4  R!H u0 {3,[S,D,B]} {6,[S,D,B]}
5  R!H u0 {3,[S,D,B]} {10,[S,D,B]}
6  R!H u0 {4,[S,D,B]} {8,[S,D,B]}
7  R!H u0 {1,[S,D,B]} {3,[S,D,B]}
8  R!H u0 {1,[S,D,B]} {6,[S,D,B]}
9  R!H u0 {1,[S,D,B]} {11,[S,D,B]}
10 R!H u0 {5,[S,D,B]} {13,[S,D,B]}
11 R!H u0 {9,[S,D,B]} {12,[S,D,B]}
12 R!H u0 {11,[S,D,B]} {13,[S,D,B]} {14,[S,D,B]}
13 R!H u0 {2,[S,D,B]} {10,[S,D,B]} {12,[S,D,B]}
14 R!H u0 {12,[S,D,B]} {15,[S,D,B]} {17,[S,D,B]}
15 R!H u0 {2,[S,D,B]} {14,[S,D,B]} {16,[S,D,B]}
16 R!H u0 {15,[S,D,B]} {18,[S,D,B]}
17 R!H u0 {14,[S,D,B]} {19,[S,D,B]}
18 R!H u0 {16,[S,D,B]} {19,[S,D,B]}
19 R!H u0 {17,[S,D,B]} {18,[S,D,B]}
""",
	solute = u's2_6_5_ben_ene_s2_5_9_s3_9_6_hetero',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 70,
	label = "s2_6_5_ben_ene_s2_5_9_s3_9_6_hetero",
	group = 
"""
1  * N u0 {7,S} {8,S} {9,S}
2  N u0 {13,S} {15,S}
3  C u0 {4,S} {5,S} {7,S}
4  C u0 {3,S} {6,S}
5  C u0 {3,S} {10,S}
6  C u0 {4,S} {8,S}
7  C u0 {1,S} {3,S}
8  C u0 {1,S} {6,S}
9  C u0 {1,S} {11,S}
10 C u0 {5,S} {13,S}
11 C u0 {9,S} {12,S}
12 C u0 {11,S} {13,D} {14,S}
13 C u0 {2,S} {10,S} {12,D}
14 C u0 {12,S} {15,B} {17,B}
15 C u0 {2,S} {14,B} {16,B}
16 C u0 {15,B} {18,B}
17 C u0 {14,B} {19,B}
18 C u0 {16,B} {19,B}
19 C u0 {17,B} {18,B}
""",
	solute = SoluteData(
		S = 0.03834,
		B = -0.01704,
		E = -0.00473,
		L = 0.04905,
		A = 0.01444,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
		E = 2,
		L = 2,
		A = 2,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 71,
	label = "s2_6_7_s2_7_6_s2_7_6",
	group = 
"""
1  * R!H u0 {10,[S,D,B]} {11,[S,D,B]}
2  R!H u0 {6,[S,D,B]} {7,[S,D,B]}
3  R!H u0 {4,[S,D,B]} {5,[S,D,B]} {8,[S,D,B]}
4  R!H u0 {3,[S,D,B]} {6,[S,D,B]} {9,[S,D,B]}
5  R!H u0 {3,[S,D,B]} {7,[S,D,B]}
6  R!H u0 {2,[S,D,B]} {4,[S,D,B]}
7  R!H u0 {2,[S,D,B]} {5,[S,D,B]}
8  R!H u0 {3,[S,D,B]} {10,[S,D,B]} {12,[S,D,B]}
9  R!H u0 {4,[S,D,B]} {11,[S,D,B]} {13,[S,D,B]}
10 R!H u0 {1,[S,D,B]} {8,[S,D,B]} {14,[S,D,B]}
11 R!H u0 {1,[S,D,B]} {9,[S,D,B]} {15,[S,D,B]}
12 R!H u0 {8,[S,D,B]} {17,[S,D,B]}
13 R!H u0 {9,[S,D,B]} {19,[S,D,B]}
14 R!H u0 {10,[S,D,B]} {16,[S,D,B]}
15 R!H u0 {11,[S,D,B]} {18,[S,D,B]}
16 R!H u0 {14,[S,D,B]} {17,[S,D,B]}
17 R!H u0 {12,[S,D,B]} {16,[S,D,B]}
18 R!H u0 {15,[S,D,B]} {19,[S,D,B]}
19 R!H u0 {13,[S,D,B]} {18,[S,D,B]}
""",
	solute = SoluteData(
		S = -0.07266,
		B = -0.01224,
		E = 0.04993,
		L = 0.05495,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
		E = 2,
		L = 2,
		A = 2,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 72,
	label = "s2_6_7_ben_s2_7_6_ben_s2_7_6_piperidine",
	group = 
"""
1  * O u0 {10,S} {11,S}
2  N u0 {6,S} {7,S}
3  C u0 {4,S} {5,S} {8,S}
4  C u0 {3,S} {6,S} {9,S}
5  C u0 {3,S} {7,S}
6  C u0 {2,S} {4,S}
7  C u0 {2,S} {5,S}
8  C u0 {3,S} {10,B} {12,B}
9  C u0 {4,S} {11,B} {13,B}
10 C u0 {1,S} {8,B} {14,B}
11 C u0 {1,S} {9,B} {15,B}
12 C u0 {8,B} {17,B}
13 C u0 {9,B} {19,B}
14 C u0 {10,B} {16,B}
15 C u0 {11,B} {18,B}
16 C u0 {14,B} {17,B}
17 C u0 {12,B} {16,B}
18 C u0 {15,B} {19,B}
19 C u0 {13,B} {18,B}
""",
	solute = SoluteData(
		S = -0.01105,
		B = -0.02492,
		E = 0.02815,
		L = 0.01544,
		A = -0.01389,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
		E = 2,
		L = 2,
		A = 2,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 73,
	label = "Quadricyclane_general",
	group = 
"""
1  * R!H u0 {2,[S,D,B]} {4,[S,D,B]} {5,[S,D,B]}
2  R!H u0 {1,[S,D,B]} {3,[S,D,B]} {5,[S,D,B]}
3  R!H u0 {2,[S,D,B]} {4,[S,D,B]} {6,[S,D,B]}
4  R!H u0 {1,[S,D,B]} {3,[S,D,B]} {6,[S,D,B]}
5  R!H u0 {1,[S,D,B]} {2,[S,D,B]} {7,[S,D,B]}
6  R!H u0 {3,[S,D,B]} {4,[S,D,B]} {7,[S,D,B]}
7  R!H u0 {5,[S,D,B]} {6,[S,D,B]}
""",
	solute = u'Quadricyclane',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 74,
	label = "Quadricyclane",
	group = 
"""
1  * C u0 {2,S} {4,S} {5,S}
2  C u0 {1,S} {3,S} {5,S}
3  C u0 {2,S} {4,S} {6,S}
4  C u0 {1,S} {3,S} {6,S}
5  C u0 {1,S} {2,S} {7,S}
6  C u0 {3,S} {4,S} {7,S}
7  C u0 {5,S} {6,S}
""",
	solute = SoluteData(
		S = -0.09580,
		B = 0.00000,
		E = -0.04218,
		L = -0.47881,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 1,
		B = 1,
		E = 1,
		L = 1,
		A = 1,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 75,
	label = "polycyclic_3fused",
	group =  "OR{Adamantane_general, s2_6_7_s2_7_6, s2_6_6_s2_6_5, s2_6_6_s2_6_6, s2_6_6_s2_6_6_A, s2_6_5_s2_5_6, s2_5_6_s2_6_6,\
s2_5_7_s2_7_3, Nortricyclene_general, s3_6_3_s3_3_6, Acenaphthene_general, s2_5_5_s2_5_5_ane}",
	solute = None,
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 76,
	label = "Adamantane_general",
	group = 
"""
1  * R!H u0 {5,[S,D,B]} {6,[S,D,B]} {9,[S,D,B]}
2  R!H u0 {6,[S,D,B]} {7,[S,D,B]} {10,[S,D,B]}
3  R!H u0 {5,[S,D,B]} {7,[S,D,B]} {8,[S,D,B]}
4  R!H u0 {8,[S,D,B]} {9,[S,D,B]} {10,[S,D,B]}
5  R!H u0 {1,[S,D,B]} {3,[S,D,B]}
6  R!H u0 {1,[S,D,B]} {2,[S,D,B]}
7  R!H u0 {2,[S,D,B]} {3,[S,D,B]}
8  R!H u0 {3,[S,D,B]} {4,[S,D,B]}
9  R!H u0 {1,[S,D,B]} {4,[S,D,B]}
10 R!H u0 {2,[S,D,B]} {4,[S,D,B]}
""",
	solute = u'Adamantane',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 77,
	label = "Adamantane",
	group = 
"""
1  * C u0 {5,S} {6,S} {9,S}
2  C u0 {6,S} {7,S} {10,S}
3  C u0 {5,S} {7,S} {8,S}
4  C u0 {8,S} {9,S} {10,S}
5  C u0 {1,S} {3,S}
6  C u0 {1,S} {2,S}
7  C u0 {2,S} {3,S}
8  C u0 {3,S} {4,S}
9  C u0 {1,S} {4,S}
10 C u0 {2,S} {4,S}
""",
	solute = SoluteData(
		S = 0.06655,
		B = 0.08122,
		E = 0.06194,
		L = 0.07941,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 10,
		B = 10,
		E = 10,
		L = 10,
		A = 10,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 78,
	label = "s2_6_7_s2_7_6",
	group = 
"""
1  * R!H u0 {6,[S,D,B]} {7,[S,D,B]}
2  R!H u0 {3,[S,D,B]} {4,[S,D,B]}
3  R!H u0 {2,[S,D,B]} {5,[S,D,B]}
4  R!H u0 {2,[S,D,B]} {6,[S,D,B]} {8,[S,D,B]}
5  R!H u0 {3,[S,D,B]} {7,[S,D,B]} {9,[S,D,B]}
6  R!H u0 {1,[S,D,B]} {4,[S,D,B]} {10,[S,D,B]}
7  R!H u0 {1,[S,D,B]} {5,[S,D,B]} {11,[S,D,B]}
8  R!H u0 {4,[S,D,B]} {12,[S,D,B]}
9  R!H u0 {5,[S,D,B]} {14,[S,D,B]}
10 R!H u0 {6,[S,D,B]} {13,[S,D,B]}
11 R!H u0 {7,[S,D,B]} {15,[S,D,B]}
12 R!H u0 {8,[S,D,B]} {13,[S,D,B]}
13 R!H u0 {10,[S,D,B]} {12,[S,D,B]}
14 R!H u0 {9,[S,D,B]} {15,[S,D,B]}
15 R!H u0 {11,[S,D,B]} {14,[S,D,B]}
""",
	solute = u's2_6_7_ben_s2_7_6_ben_ene',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 79,
	label = "s2_6_7_ben_s2_7_6_ben_general",
	group =  "OR{s2_6_7_ben_s2_7_6_ben, s2_6_7_ben_s2_7_6_ben_iminodibenzyl_general}",
	solute = u's2_6_7_ben_s2_7_6_ben',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 80,
	label = "s2_6_7_ben_s2_7_6_ben_iminodibenzyl_general",
	group =  "OR{s2_6_7_ben_s2_7_6_ben_iminodibenzyl1, s2_6_7_ben_s2_7_6_ben_iminodibenzyl2, s2_6_7_ben_s2_7_6_ben_iminodibenzyl3, \
s2_6_7_ben_s2_7_6_ben_iminodibenzyl4, s2_6_7_ben_s2_7_6_ben_iminodibenzyl5, s2_6_7_ben_s2_7_6_ben_iminodibenzyl6}",
	solute = u's2_6_7_ben_s2_7_6_ben_iminodibenzyl',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 81,
	label = "s2_6_7_ben_s2_7_6_ben_iminodibenzyl1",
	group = 
"""
1  N u0 {6,S} {7,S}
2  C u0 {3,S} {4,S}
3  C u0 {2,S} {5,S}
4  C u0 {2,S} {6,B} {8,B}
5  C u0 {3,S} {7,B} {9,B}
6  C u0 {1,S} {4,B} {10,B}
7  C u0 {1,S} {5,B} {11,B}
8  C u0 {4,B} {12,B}
9  C u0 {5,B} {14,B}
10 C u0 {6,B} {13,B}
11 C u0 {7,B} {15,B}
12 C u0 {8,B} {13,B}
13 C u0 {10,B} {12,B}
14 C u0 {9,B} {15,B}
15 C u0 {11,B} {14,B}
""",
	solute = u's2_6_7_ben_s2_7_6_ben_iminodibenzyl',
	dataCount = None,
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
this is one of the groups that belong to s2_6_7_ben_s2_7_6_ben_iminodibenzyl
""",
)

entry(
	index = 82,
	label = "s2_6_7_ben_s2_7_6_ben_iminodibenzyl2",
	group = 
"""
1  [C,N] u0 {4,S} {7,S}
2  N     u0 {6,S} {8,S}
3  [C,N] u0 {8,S} {15,D}
4  [C,N] u0 {1,S} {5,S}
5  [C,N] u0 {4,S} {6,B} {9,B}
6  [C,N] u0 {2,S} {5,B} {10,B}
7  [C,N] u0 {1,S} {8,D} {11,S}
8  [C,N] u0 {2,S} {3,S} {7,D}
9  [C,N] u0 {5,B} {13,B}
10 [C,N] u0 {6,B} {12,B}
11 [C,N] u0 {7,S} {14,D}
12 [C,N] u0 {10,B} {13,B}
13 [C,N] u0 {9,B} {12,B}
14 [C,N] u0 {11,D} {15,S}
15 [C,N] u0 {3,D} {14,S}
""",
	solute = u's2_6_7_ben_s2_7_6_ben_iminodibenzyl',
	dataCount = None,
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
this is one of the groups that belong to s2_6_7_ben_s2_7_6_ben_iminodibenzyl
""",
)

entry(
	index = 83,
	label = "s2_6_7_ben_s2_7_6_ben_iminodibenzyl3",
	group = 
"""
1  [C,N] u0 {5,S} {7,S}
2  N     u0 {8,S} {9,S}
3  [C,N] u0 {9,D} {14,S}
4  [C,N] u0 {8,S} {15,D}
5  [C,N] u0 {1,S} {6,S}
6  [C,N] u0 {5,S} {8,D} {10,S}
7  [C,N] u0 {1,S} {9,S} {11,D}
8  [C,N] u0 {2,S} {4,S} {6,D}
9  [C,N] u0 {2,S} {3,D} {7,S}
10 [C,N] u0 {6,S} {13,D}
11 [C,N] u0 {7,D} {12,S}
12 [C,N] u0 {11,S} {14,D}
13 [C,N] u0 {10,D} {15,S}
14 [C,N] u0 {3,S} {12,D}
15 [C,N] u0 {4,D} {13,S}
""",
	solute = u's2_6_7_ben_s2_7_6_ben_iminodibenzyl',
	dataCount = None,
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
this is one of the groups that belong to s2_6_7_ben_s2_7_6_ben_iminodibenzyl
""",
)

entry(
	index = 84,
	label = "s2_6_7_ben_s2_7_6_ben_iminodibenzyl4",
	group = 
"""
1  [C,N] u0 {5,S} {7,S}
2  N     u0 {8,S} {9,S}
3  [C,N] u0 {9,S} {14,D}
4  [C,N] u0 {8,S} {15,D}
5  [C,N] u0 {1,S} {6,S}
6  [C,N] u0 {5,S} {8,D} {10,S}
7  [C,N] u0 {1,S} {9,D} {11,S}
8  [C,N] u0 {2,S} {4,S} {6,D}
9  [C,N] u0 {2,S} {3,S} {7,D}
10 [C,N] u0 {6,S} {13,D}
11 [C,N] u0 {7,S} {12,D}
12 [C,N] u0 {11,D} {14,S}
13 [C,N] u0 {10,D} {15,S}
14 [C,N] u0 {3,D} {12,S}
15 [C,N] u0 {4,D} {13,S}
""",
	solute = u's2_6_7_ben_s2_7_6_ben_iminodibenzyl',
	dataCount = None,
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
this is one of the groups that belong to s2_6_7_ben_s2_7_6_ben_iminodibenzyl
""",
)

entry(
	index = 85,
	label = "s2_6_7_ben_s2_7_6_ben_iminodibenzyl5",
	group = 
"""
1  [C,N] u0 {5,S} {7,S}
2  N     u0 {8,S} {9,S}
3  [C,N] u0 {9,D} {14,S}
4  [C,N] u0 {8,D} {15,S}
5  [C,N] u0 {1,S} {6,S}
6  [C,N] u0 {5,S} {8,S} {10,D}
7  [C,N] u0 {1,S} {9,S} {11,D}
8  [C,N] u0 {2,S} {4,D} {6,S}
9  [C,N] u0 {2,S} {3,D} {7,S}
10 [C,N] u0 {6,D} {13,S}
11 [C,N] u0 {7,D} {12,S}
12 [C,N] u0 {11,S} {14,D}
13 [C,N] u0 {10,S} {15,D}
14 [C,N] u0 {3,S} {12,D}
15 [C,N] u0 {4,S} {13,D}
""",
	solute = u's2_6_7_ben_s2_7_6_ben_iminodibenzyl',
	dataCount = None,
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
this is one of the groups that belong to s2_6_7_ben_s2_7_6_ben_iminodibenzyl
""",
)

entry(
	index = 86,
	label = "s2_6_7_ben_s2_7_6_ben_iminodibenzyl6",
	group = 
"""
1  [C,N] u0 {4,S} {7,S}
2  N     u0 {6,S} {8,S}
3  [C,N] u0 {8,D} {15,S}
4  [C,N] u0 {1,S} {5,S}
5  [C,N] u0 {4,S} {6,B} {9,B}
6  [C,N] u0 {2,S} {5,B} {10,B}
7  [C,N] u0 {1,S} {8,S} {11,D}
8  [C,N] u0 {2,S} {3,D} {7,S}
9  [C,N] u0 {5,B} {13,B}
10 [C,N] u0 {6,B} {12,B}
11 [C,N] u0 {7,D} {14,S}
12 [C,N] u0 {10,B} {13,B}
13 [C,N] u0 {9,B} {12,B}
14 [C,N] u0 {11,S} {15,D}
15 [C,N] u0 {3,S} {14,D}
""",
	solute = u's2_6_7_ben_s2_7_6_ben_iminodibenzyl',
	dataCount = None,
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
this is one of the groups that belong to s2_6_7_ben_s2_7_6_ben_iminodibenzyl
""",
)

entry(
	index = 87,
	label = "s2_6_7_ben_s2_7_6_ben_iminodibenzyl",
	group = 
"""
1  R!H u0 {6,[S,D,B]} {7,[S,D,B]}
2  R!H u0 {3,[S,D,B]} {4,[S,D,B]}
3  R!H u0 {2,[S,D,B]} {5,[S,D,B]}
4  R!H u0 {2,[S,D,B]} {6,[S,D,B]} {8,[S,D,B]}
5  R!H u0 {3,[S,D,B]} {7,[S,D,B]} {9,[S,D,B]}
6  R!H u0 {1,[S,D,B]} {4,[S,D,B]} {10,[S,D,B]}
7  R!H u0 {1,[S,D,B]} {5,[S,D,B]} {11,[S,D,B]}
8  R!H u0 {4,[S,D,B]} {12,[S,D,B]}
9  R!H u0 {5,[S,D,B]} {14,[S,D,B]}
10 R!H u0 {6,[S,D,B]} {13,[S,D,B]}
11 R!H u0 {7,[S,D,B]} {15,[S,D,B]}
12 R!H u0 {8,[S,D,B]} {13,[S,D,B]}
13 R!H u0 {10,[S,D,B]} {12,[S,D,B]}
14 R!H u0 {9,[S,D,B]} {15,[S,D,B]}
15 R!H u0 {11,[S,D,B]} {14,[S,D,B]}
""",
	solute = SoluteData(
		S = 0.02338,
		B = -0.05327,
		E = -0.10435,
		L = -0.15494,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 6,
		B = 6,
		E = 7,
		L = 6,
		A = 6,
	),
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
dummy groups to put all s2_6_7_ben_s2_7_6_ben_iminodibenzyl groups (s2_6_7_ben_s2_7_6_ben_iminodibenzyl1-6) together
""",
)

entry(
	index = 88,
	label = "s2_6_7_ben_s2_7_6_ben",
	group = 
"""
1  * R!H u0 {6,S} {7,S}
2  R!H u0 {3,S} {4,S}
3  R!H u0 {2,S} {5,S}
4  R!H u0 {2,S} {6,B} {8,B}
5  R!H u0 {3,S} {7,B} {9,B}
6  R!H u0 {1,S} {4,B} {10,B}
7  R!H u0 {1,S} {5,B} {11,B}
8  R!H u0 {4,B} {12,B}
9  R!H u0 {5,B} {14,B}
10 R!H u0 {6,B} {13,B}
11 R!H u0 {7,B} {15,B}
12 R!H u0 {8,B} {13,B}
13 R!H u0 {10,B} {12,B}
14 R!H u0 {9,B} {15,B}
15 R!H u0 {11,B} {14,B}
""",
	solute = SoluteData(
		S = 0.00696,
		B = 0.00011,
		E = -0.00973,
		L = 0.07011,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 4,
		B = 4,
		E = 4,
		L = 4,
		A = 4,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 89,
	label = "s2_6_7_ben_s2_7_6_ben_ene",
	group = 
"""
1  * R!H u0 {6,S} {7,S}
2  R!H u0 {3,D} {4,S}
3  R!H u0 {2,D} {5,S}
4  R!H u0 {2,S} {6,B} {8,B}
5  R!H u0 {3,S} {7,B} {9,B}
6  R!H u0 {1,S} {4,B} {10,B}
7  R!H u0 {1,S} {5,B} {11,B}
8  R!H u0 {4,B} {12,B}
9  R!H u0 {5,B} {14,B}
10 R!H u0 {6,B} {13,B}
11 R!H u0 {7,B} {15,B}
12 R!H u0 {8,B} {13,B}
13 R!H u0 {10,B} {12,B}
14 R!H u0 {9,B} {15,B}
15 R!H u0 {11,B} {14,B}
""",
	solute = SoluteData(
		S = -0.10938,
		B = 0.09353,
		E = -0.11225,
		L = -0.19892,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 11,
		B = 11,
		E = 11,
		L = 11,
		A = 11,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 90,
	label = "s2_6_6_s2_6_5",
	group = 
"""
1  * R!H u0 {3,[S,D,B]} {6,[S,D,B]}
2  R!H u0 {7,[S,D,B]} {13,[S,D,B]}
3  R!H u0 {1,[S,D,B]} {8,[S,D,B]}
4  R!H u0 {7,[S,D,B]} {9,[S,D,B]} {12,[S,D,B]}
5  R!H u0 {6,[S,D,B]} {9,[S,D,B]} {10,[S,D,B]}
6  R!H u0 {1,[S,D,B]} {5,[S,D,B]} {11,[S,D,B]}
7  R!H u0 {2,[S,D,B]} {4,[S,D,B]} {11,[S,D,B]}
8  R!H u0 {3,[S,D,B]} {10,[S,D,B]}
9  R!H u0 {4,[S,D,B]} {5,[S,D,B]}
10 R!H u0 {5,[S,D,B]} {8,[S,D,B]}
11 R!H u0 {6,[S,D,B]} {7,[S,D,B]}
12 R!H u0 {4,[S,D,B]} {13,[S,D,B]}
13 R!H u0 {2,[S,D,B]} {12,[S,D,B]}
""",
	solute = SoluteData(
		S = 0.04715,
		B = -0.02702,
		E = 0.02078,
		L = 0.14645,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 3,
		L = 3,
		A = 3,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 91,
	label = "s2_6_6_s2_6_5_ben_ene",
	group = 
"""
1  * R!H u0 {3,S} {6,S}
2  R!H u0 {7,S} {13,S}
3  R!H u0 {1,S} {8,D}
4  R!H u0 {7,B} {9,B} {12,S}
5  R!H u0 {6,B} {9,B} {10,S}
6  R!H u0 {1,S} {5,B} {11,B}
7  R!H u0 {2,S} {4,B} {11,B}
8  R!H u0 {3,D} {10,S}
9  R!H u0 {4,B} {5,B}
10 R!H u0 {5,S} {8,S}
11 R!H u0 {6,B} {7,B}
12 R!H u0 {4,S} {13,S}
13 R!H u0 {2,S} {12,S}
""",
	solute = SoluteData(
		S = -0.08473,
		B = 0.01327,
		E = 0.10047,
		L = -0.26149,
		A = 0.00866,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
		E = 3,
		L = 2,
		A = 2,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 92,
	label = "s2_6_6_s2_6_5_ben_diene",
	group = 
"""
1  * R!H u0 {3,S} {6,S}
2  R!H u0 {7,S} {13,S}
3  R!H u0 {1,S} {8,S}
4  R!H u0 {7,B} {9,B} {12,S}
5  R!H u0 {6,B} {9,B} {10,S}
6  R!H u0 {1,S} {5,B} {11,B}
7  R!H u0 {2,S} {4,B} {11,B}
8  R!H u0 {3,S} {10,D}
9  R!H u0 {4,B} {5,B}
10 R!H u0 {5,S} {8,D}
11 R!H u0 {6,B} {7,B}
12 R!H u0 {4,S} {13,D}
13 R!H u0 {2,S} {12,D}
""",
	solute = u's2_6_6_s2_6_5_ben_diene_psoralen',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 93,
	label = "s2_6_6_s2_6_5_ben_diene_psoralen",
	group = 
"""
1  * O u0 {3,S} {6,S}
2  O u0 {7,S} {13,S}
3  CO u0 {1,S} {8,S}
4  C u0 {7,B} {9,B} {12,S}
5  C u0 {6,B} {9,B} {10,S}
6  C u0 {1,S} {5,B} {11,B}
7  C u0 {2,S} {4,B} {11,B}
8  C u0 {3,S} {10,D}
9  C u0 {4,B} {5,B}
10 C u0 {5,S} {8,D}
11 C u0 {6,B} {7,B}
12 C u0 {4,S} {13,D}
13 C u0 {2,S} {12,D}
""",
	solute = SoluteData(
		S = -0.02531,
		B = 0.02067,
		E = 0.01404,
		L = -0.09039,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 4,
		B = 4,
		E = 4,
		L = 3,
		A = 4,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 94,
	label = "s2_6_6_s2_6_6",
	group = 
"""
1  * R!H u0 {2,[S,D,B]} {3,[S,D,B]} {5,[S,D,B]}
2    R!H u0 {1,[S,D,B]} {4,[S,D,B]} {10,[S,D,B]}
3    R!H u0 {1,[S,D,B]} {6,[S,D,B]} {7,[S,D,B]}
4    R!H u0 {2,[S,D,B]} {8,[S,D,B]} {9,[S,D,B]}
5    R!H u0 {1,[S,D,B]} {12,[S,D,B]}
6    R!H u0 {3,[S,D,B]} {11,[S,D,B]}
7    R!H u0 {3,[S,D,B]} {8,[S,D,B]}
8    R!H u0 {4,[S,D,B]} {7,[S,D,B]}
9    R!H u0 {4,[S,D,B]} {13,[S,D,B]}
10   R!H u0 {2,[S,D,B]} {14,[S,D,B]}
11   R!H u0 {6,[S,D,B]} {12,[S,D,B]}
12   R!H u0 {5,[S,D,B]} {11,[S,D,B]}
13   R!H u0 {9,[S,D,B]} {14,[S,D,B]}
14   R!H u0 {10,[S,D,B]} {13,[S,D,B]}
""",
	solute = SoluteData(
		S = 0.10072,
		B = -0.03236,
		E = 0.09049,
		L = -0.55079,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
		E = 3,
		L = 3,
		A = 3,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 95,
	label = "s2_6_6_s2_6_6_aromatic",
	group =  "OR{s2_6_6_s2_6_6_aromatic1, s2_6_6_s2_6_6_aromatic2, s2_6_6_s2_6_6_aromatic3, s2_6_6_s2_6_6_aromatic4}",
	solute = u's2_6_6_s2_6_6_all_ben',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 96,
	label = "s2_6_6_s2_6_6_aromatic1",
	group = 
"""
1  * [C,N]  u0 {2,[S,B]} {3,B} {5,B}
2    [C,N]  u0 {1,[S,B]} {4,B} {10,B}
3    [C,N]  u0 {1,B} {6,B} {7,[S,B]}
4    [C,N]  u0 {2,B} {8,[S,B]} {9,B}
5    [C,N]  u0 {1,B} {12,B}
6    [C,N]  u0 {3,B} {11,B}
7    [C,N]  u0 {3,[S,B]} {8,[D,B]}
8    [C,N]  u0 {4,[S,B]} {7,[D,B]}
9    [C,N]  u0 {4,B} {13,B}
10   [C,N]  u0 {2,B} {14,B}
11   [C,N]  u0 {6,B} {12,B}
12   [C,N]  u0 {5,B} {11,B}
13   [C,N]  u0 {9,B} {14,B}
14   [C,N]  u0 {10,B} {13,B}
""",
	solute = u's2_6_6_s2_6_6_heteroaromatic',
	dataCount = None,
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
the heterocyclic form belongs to s2_6_6_s2_6_6_heteroaromatic
""",
)

entry(
	index = 97,
	label = "s2_6_6_s2_6_6_aromatic2",
	group = 
"""
1  * [C,N]  u0 {2,[S,B]} {3,[D,B]} {5,[S,B]}
2    [C,N]  u0 {1,[S,B]} {4,[D,B]} {10,[S,B]}
3    [C,N]  u0 {1,[D,B]} {6,[S,B]} {7,[S,B]}
4    [C,N]  u0 {2,[D,B]} {8,[S,B]} {9,[S,B]}
5    [C,N]  u0 {1,[S,B]} {12,[D,B]}
6    [C,N]  u0 {3,[S,B]} {11,[D,B]}
7    [C,N]  u0 {3,[S,B]} {8,[D,B]}
8    [C,N]  u0 {4,[S,B]} {7,[D,B]}
9    [C,N]  u0 {4,[S,B]} {13,[D,B]}
10   [C,N]  u0 {2,[S,B]} {14,[D,B]}
11   [C,N]  u0 {6,[D,B]} {12,[S,B]}
12   [C,N]  u0 {5,[D,B]} {11,[S,B]}
13   [C,N]  u0 {9,[D,B]} {14,[S,B]}
14   [C,N]  u0 {10,[D,B]} {13,[S,B]}
""",
	solute = u's2_6_6_s2_6_6_heteroaromatic',
	dataCount = None,
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
the heterocyclic form belongs to s2_6_6_s2_6_6_heteroaromatic
""",
)

entry(
	index = 98,
	label = "s2_6_6_s2_6_6_aromatic3",
	group = 
"""
1  * [C,N]  u0 {2,[S,B]} {3,[D,B]} {5,[S,B]}
2    [C,N]  u0 {1,[S,B]} {4,[S,B]} {10,[D,B]}
3    [C,N]  u0 {1,[D,B]} {6,[S,B]} {7,[S,B]}
4    [C,N]  u0 {2,[S,B]} {8,[S,B]} {9,[D,B]}
5    [C,N]  u0 {1,[S,B]} {12,[D,B]}
6    [C,N]  u0 {3,[S,B]} {11,[D,B]}
7    [C,N]  u0 {3,[S,B]} {8,[D,B]}
8    [C,N]  u0 {4,[S,B]} {7,[D,B]}
9    [C,N]  u0 {4,[D,B]} {13,[S,B]}
10   [C,N]  u0 {2,[D,B]} {14,[S,B]}
11   [C,N]  u0 {6,[D,B]} {12,[S,B]}
12   [C,N]  u0 {5,[D,B]} {11,[S,B]}
13   [C,N]  u0 {9,[S,B]} {14,[D,B]}
14   [C,N]  u0 {10,[S,B]} {13,[D,B]}
""",
	solute = u's2_6_6_s2_6_6_heteroaromatic',
	dataCount = None,
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
the heterocyclic form belongs to s2_6_6_s2_6_6_heteroaromatic
""",
)

entry(
	index = 99,
	label = "s2_6_6_s2_6_6_aromatic4",
	group = 
"""
1  * [C,N]  u0 {2,[S,B]} {3,[S,B]} {5,[D,B]}
2    [C,N]  u0 {1,[S,B]} {4,[S,B]} {10,[D,B]}
3    [C,N]  u0 {1,[S,B]} {6,[D,B]} {7,[S,B]}
4    [C,N]  u0 {2,[S,B]} {8,[S,B]} {9,[D,B]}
5    [C,N]  u0 {1,[D,B]} {12,[S,B]}
6    [C,N]  u0 {3,[D,B]} {11,[S,B]}
7    [C,N]  u0 {3,[S,B]} {8,[D,B]}
8    [C,N]  u0 {4,[S,B]} {7,[D,B]}
9    [C,N]  u0 {4,[D,B]} {13,[S,B]}
10   [C,N]  u0 {2,[D,B]} {14,[S,B]}
11   [C,N]  u0 {6,[S,B]} {12,[D,B]}
12   [C,N]  u0 {5,[S,B]} {11,[D,B]}
13   [C,N]  u0 {9,[S,B]} {14,[D,B]}
14   [C,N]  u0 {10,[S,B]} {13,[D,B]}
""",
	solute = u's2_6_6_s2_6_6_heteroaromatic',
	dataCount = None,
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
the heterocyclic form belongs to s2_6_6_s2_6_6_heteroaromatic
""",
)

entry(
	index = 100,
	label = "s2_6_6_s2_6_6_all_ben",
	group = 
"""
1  * C  u0 {2,B} {3,B} {5,B}
2    C  u0 {1,B} {4,B} {10,B}
3    C  u0 {1,B} {6,B} {7,B}
4    C  u0 {2,B} {8,B} {9,B}
5    C  u0 {1,B} {12,B}
6    C  u0 {3,B} {11,B}
7    C  u0 {3,B} {8,B}
8    C  u0 {4,B} {7,B}
9    C  u0 {4,B} {13,B}
10   C  u0 {2,B} {14,B}
11   C  u0 {6,B} {12,B}
12   C  u0 {5,B} {11,B}
13   C  u0 {9,B} {14,B}
14   C  u0 {10,B} {13,B}
""",
	solute = SoluteData(
		S = -0.07986,
		B = 0.03301,
		E = -0.21229,
		L = -0.06221,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 13,
		B = 13,
		E = 23,
		L = 22,
		A = 25,
	),
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
dummy group to put all aromatic s2_6_6_s2_6_6_aromatic groups (s2_6_6_s2_6_6_aromatic1-4) together
""",
)

entry(
	index = 101,
	label = "s2_6_6_s2_6_6_heteroaromatic",
	group = 
"""
1  * R!H u0 {2,[S,D,B]} {3,[S,D,B]} {5,[S,D,B]}
2    R!H u0 {1,[S,D,B]} {4,[S,D,B]} {10,[S,D,B]}
3    R!H u0 {1,[S,D,B]} {6,[S,D,B]} {7,[S,D,B]}
4    R!H u0 {2,[S,D,B]} {8,[S,D,B]} {9,[S,D,B]}
5    R!H u0 {1,[S,D,B]} {12,[S,D,B]}
6    R!H u0 {3,[S,D,B]} {11,[S,D,B]}
7    R!H u0 {3,[S,D,B]} {8,[S,D,B]}
8    R!H u0 {4,[S,D,B]} {7,[S,D,B]}
9    R!H u0 {4,[S,D,B]} {13,[S,D,B]}
10   R!H u0 {2,[S,D,B]} {14,[S,D,B]}
11   R!H u0 {6,[S,D,B]} {12,[S,D,B]}
12   R!H u0 {5,[S,D,B]} {11,[S,D,B]}
13   R!H u0 {9,[S,D,B]} {14,[S,D,B]}
14   R!H u0 {10,[S,D,B]} {13,[S,D,B]}
""",
	solute = SoluteData(
		S = -0.03696,
		B = -0.01071,
		E = -0.02164,
		L = 0.16883,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 3,
		E = 5,
		L = 5,
		A = 5,
	),
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
dummy group to put all heterocyclic s2_6_6_s2_6_6_aromatic groups (s2_6_6_s2_6_6_aromatic1-4) together
""",
)

entry(
	index = 102,
	label = "s2_6_6_ben_s2_6_6_ben",
	group = 
"""
1  * C   u0 {2,S} {3,B} {5,B}
2    C   u0 {1,S} {4,B} {10,B}
3    C   u0 {1,B} {6,B} {7,S}
4    C   u0 {2,B} {8,S} {9,B}
5    C   u0 {1,B} {12,B}
6    C   u0 {3,B} {11,B}
7    R!H u0 {3,S} {8,S}
8    R!H u0 {4,S} {7,S}
9    C   u0 {4,B} {13,B}
10   C   u0 {2,B} {14,B}
11   C   u0 {6,B} {12,B}
12   C   u0 {5,B} {11,B}
13   C   u0 {9,B} {14,B}
14   C   u0 {10,B} {13,B}
""",
	solute = SoluteData(
		S = 0.00726,
		B = -0.00624,
		E = -0.01118,
		L = 0.34616,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 6,
		B = 6,
		E = 6,
		L = 6,
		A = 6,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 103,
	label = "s2_6_6_ene_s2_6_6_ene",
	group = 
"""
1    R!H u0 {2,S} {14,S}
2    R!H u0 {1,S} {3,S}
3    R!H u0 {2,S} {4,S}
4    R!H u0 {3,S} {5,S}
5    R!H u0 {4,S} {6,S} {14,S}
6  * R!H u0 {5,S} {7,S} {11,S}
7    R!H u0 {6,S} {8,S}
8    R!H u0 {7,S} {9,S}
9    R!H u0 {8,S} {10,D}
10   R!H u0 {9,D} {11,S}
11   R!H u0 {6,S} {10,S} {12,D}
12   R!H u0 {11,D} {13,S}
13   R!H u0 {12,S} {14,S}
14   R!H u0 {1,S} {5,S} {13,S}
""",
	solute = SoluteData(
		S = -0.04326,
		B = 0.03785,
		E = 0.01024,
		L = 0.14346,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 3,
		L = 2,
		A = 3,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 104,
	label = "s2_6_6_ben_s2_6_6_ane",
	group = 
"""
1   R!H u0 {2,B} {6,B}
2   R!H u0 {1,B} {3,B}
3   R!H u0 {2,B} {4,B}
4   R!H u0 {3,B} {5,B}
5 * R!H u0 {4,B} {6,B} {14,S}
6   R!H u0 {1,B} {5,B} {7,S}
7   R!H u0 {6,S} {8,S}
8   R!H u0 {7,S} {9,S}
9   R!H u0 {8,S} {10,S} {14,S}
10  R!H u0 {9,S} {11,S}
11  R!H u0 {10,S} {12,S}
12  R!H u0 {11,S} {13,S}
13  R!H u0 {12,S} {14,S}
14  R!H u0 {5,S} {9,S} {13,S}
""",
	solute = SoluteData(
		S = 0.05601,
		B = 0.01036,
		E = -0.02585,
		L = 0.24897,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 4,
		B = 4,
		E = 4,
		L = 4,
		A = 4,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 105,
	label = "s2_6_6_s2_6_6_A",
	group = 
"""
1  R!H u0 {4,[S,D,B]} {5,[S,D,B]} {7,[S,D,B]}
2  * R!H u0 {3,[S,D,B]} {5,[S,D,B]} {8,[S,D,B]}
3  R!H u0 {2,[S,D,B]} {6,[S,D,B]} {9,[S,D,B]}
4  R!H u0 {1,[S,D,B]} {6,[S,D,B]} {10,[S,D,B]}
5  R!H u0 {1,[S,D,B]} {2,[S,D,B]}
6  R!H u0 {3,[S,D,B]} {4,[S,D,B]}
7  R!H u0 {1,[S,D,B]} {12,[S,D,B]}
8  R!H u0 {2,[S,D,B]} {13,[S,D,B]}
9  R!H u0 {3,[S,D,B]} {14,[S,D,B]}
10 R!H u0 {4,[S,D,B]} {11,[S,D,B]}
11 R!H u0 {10,[S,D,B]} {12,[S,D,B]}
12 R!H u0 {7,[S,D,B]} {11,[S,D,B]}
13 R!H u0 {8,[S,D,B]} {14,[S,D,B]}
14 R!H u0 {9,[S,D,B]} {13,[S,D,B]}
""",
	solute = SoluteData(
		S = 0.20220,
		B = -0.03172,
		E = 0.15349,
		L = 0.33084,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 7,
		B = 7,
		E = 9,
		L = 7,
		A = 9,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 106,
	label = "s2_6_6_s2_6_6_A_aromatic",
	group =  "OR{s2_6_6_s2_6_6_A_anthracene, s2_6_6_s2_6_6_A_acridine}",
	solute = u's2_6_6_s2_6_6_A_anthracene',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 107,
	label = "s2_6_6_s2_6_6_A_anthracene",
	group = 
"""
1 * C u0 {4,B} {5,B} {7,B}
2   C u0 {3,B} {5,B} {8,B}
3   C u0 {2,B} {6,B} {9,B}
4   C u0 {1,B} {6,B} {10,B}
5   C u0 {1,B} {2,B}
6   C u0 {3,B} {4,B}
7   C u0 {1,B} {12,B}
8   C u0 {2,B} {13,B}
9   C u0 {3,B} {14,B}
10  C u0 {4,B} {11,B}
11  C u0 {10,B} {12,B}
12  C u0 {7,B} {11,B}
13  C u0 {8,B} {14,B}
14  C u0 {9,B} {13,B}
""",
	solute = SoluteData(
		S = -0.06710,
		B = 0.07043,
		E = 0.05360,
		L = -0.24912,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 26,
		B = 26,
		E = 26,
		L = 16,
		A = 26,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 108,
	label = "s2_6_6_s2_6_6_A_acridine",
	group = 
"""
1  N u0 {4,S} {5,D}
2  * C u0 {4,B} {6,S} {7,B}
3  C u0 {5,S} {6,D} {8,S}
4  C u0 {1,S} {2,B} {9,B}
5  C u0 {1,D} {3,S} {10,S}
6  C u0 {2,S} {3,D}
7  C u0 {2,B} {12,B}
8  C u0 {3,S} {13,D}
9  C u0 {4,B} {11,B}
10 C u0 {5,S} {14,D}
11 C u0 {9,B} {12,B}
12 C u0 {7,B} {11,B}
13 C u0 {8,D} {14,S}
14 C u0 {10,D} {13,S}
""",
	solute = SoluteData(
		S = -0.07191,
		B = 0.02070,
		E = 0.27246,
		L = -0.05036,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 1,
		E = 4,
		L = 4,
		A = 4,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 109,
	label = "s2_6_6_ben_s2_6_6_ben_A",
	group = 
"""
1    R!H u0 {5,S} {6,S}
2    R!H u0 {3,S} {4,S}
3  * C   u0 {2,S} {5,B} {7,B}
4    C   u0 {2,S} {6,B} {8,B}
5    C   u0 {1,S} {3,B} {9,B}
6    C   u0 {1,S} {4,B} {10,B}
7    C   u0 {3,B} {11,B}
8    C   u0 {4,B} {14,B}
9    C   u0 {5,B} {12,B}
10   C   u0 {6,B} {13,B}
11   C   u0 {7,B} {12,B}
12   C   u0 {9,B} {11,B}
13   C   u0 {10,B} {14,B}
14   C   u0 {8,B} {13,B}
""",
	solute = SoluteData(
		S = -0.02275,
		B = 0.05088,
		E = -0.07847,
		L = 0.05140,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 8,
		B = 9,
		E = 10,
		L = 9,
		A = 10,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 110,
	label = "s2_6_6_ben_s2_6_6_ben_A_anthraquinone",
	group = 
"""
1    CO  u0 {5,S} {6,S}
2    CO  u0 {3,S} {4,S}
3  * C   u0 {2,S} {5,B} {7,B}
4    C   u0 {2,S} {6,B} {8,B}
5    C   u0 {1,S} {3,B} {9,B}
6    C   u0 {1,S} {4,B} {10,B}
7    C   u0 {3,B} {11,B}
8    C   u0 {4,B} {14,B}
9    C   u0 {5,B} {12,B}
10   C   u0 {6,B} {13,B}
11   C   u0 {7,B} {12,B}
12   C   u0 {9,B} {11,B}
13   C   u0 {10,B} {14,B}
14   C   u0 {8,B} {13,B}
""",
	solute = SoluteData(
		S = -0.11753,
		B = -0.22439,
		E = -0.05683,
		L = -0.37362,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 10,
		B = 10,
		E = 11,
		L = 10,
		A = 10,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 111,
	label = "s2_6_6_ben_s2_6_6_ben_A_phenothiazine",
	group = 
"""
1    N   u0 {5,S} {6,S}
2    S   u0 {3,S} {4,S}
3  * C   u0 {2,S} {5,B} {7,B}
4    C   u0 {2,S} {6,B} {8,B}
5    C   u0 {1,S} {3,B} {9,B}
6    C   u0 {1,S} {4,B} {10,B}
7    C   u0 {3,B} {11,B}
8    C   u0 {4,B} {14,B}
9    C   u0 {5,B} {12,B}
10   C   u0 {6,B} {13,B}
11   C   u0 {7,B} {12,B}
12   C   u0 {9,B} {11,B}
13   C   u0 {10,B} {14,B}
14   C   u0 {8,B} {13,B}
""",
	solute = SoluteData(
		S = 0.05546,
		B = -0.03258,
		E = -0.00404,
		L = 0.05519,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 21,
		B = 21,
		E = 21,
		L = 20,
		A = 21,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 112,
	label = "s2_6_6_ben_s2_6_6_ben_A_9H-xanthene",
	group = 
"""
1    O   u0 {5,S} {6,S}
2    C   u0 {3,S} {4,S}
3  * C   u0 {2,S} {5,B} {7,B}
4    C   u0 {2,S} {6,B} {8,B}
5    C   u0 {1,S} {3,B} {9,B}
6    C   u0 {1,S} {4,B} {10,B}
7    C   u0 {3,B} {11,B}
8    C   u0 {4,B} {14,B}
9    C   u0 {5,B} {12,B}
10   C   u0 {6,B} {13,B}
11   C   u0 {7,B} {12,B}
12   C   u0 {9,B} {11,B}
13   C   u0 {10,B} {14,B}
14   C   u0 {8,B} {13,B}
""",
	solute = SoluteData(
		S = -0.08633,
		B = 0.06984,
		E = -0.03276,
		L = -0.17675,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 5,
		E = 5,
		L = 5,
		A = 5,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 113,
	label = "s2_6_5_s2_5_6",
	group = 
"""
1  * R!H u0 {2,[S,D,B]} {6,[S,D,B]}
2    R!H u0 {1,[S,D,B]} {3,[S,D,B]}
3    R!H u0 {2,[S,D,B]} {4,[S,D,B]}
4    R!H u0 {3,[S,D,B]} {5,[S,D,B]} {13,[S,D,B]}
5    R!H u0 {4,[S,D,B]} {6,[S,D,B]} {7,[S,D,B]}
6    R!H u0 {1,[S,D,B]} {5,[S,D,B]}
7    R!H u0 {5,[S,D,B]} {8,[S,D,B]}
8    R!H u0 {7,[S,D,B]} {9,[S,D,B]} {13,[S,D,B]}
9    R!H u0 {8,[S,D,B]} {10,[S,D,B]}
10   R!H u0 {9,[S,D,B]} {11,[S,D,B]}
11   R!H u0 {10,[S,D,B]} {12,[S,D,B]}
12   R!H u0 {11,[S,D,B]} {13,[S,D,B]}
13   R!H u0 {4,[S,D,B]} {8,[S,D,B]} {12,[S,D,B]}
""",
	solute = SoluteData(
		S = 0.02272,
		B = -0.06517,
		E = 0.14311,
		L = 0.25278,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
		E = 6,
		L = 5,
		A = 5,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 114,
	label = "s2_6_5_ben_s2_5_6_ben",
	group = 
"""
1  * Cb  u0 {2,B} {6,B}
2    Cb  u0 {1,B} {3,B}
3    Cb  u0 {2,B} {4,B}
4    Cb  u0 {3,B} {5,B} {13,S}
5    Cb  u0 {4,B} {6,B} {7,S}
6    Cb  u0 {1,B} {5,B}
7    R!H u0 {5,S} {8,S}
8    Cb  u0 {7,S} {9,B} {13,B}
9    Cb  u0 {8,B} {10,B}
10   Cb  u0 {9,B} {11,B}
11   Cb  u0 {10,B} {12,B}
12   Cb  u0 {11,B} {13,B}
13   Cb  u0 {4,S} {8,B} {12,B}
""",
	solute = u's2_6_5_s2_5_6_dibenzothiophene',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 115,
	label = "s2_6_5_s2_5_6_fluorene",
	group = 
"""
1  * Cb  u0 {2,B} {6,B}
2    Cb  u0 {1,B} {3,B}
3    Cb  u0 {2,B} {4,B}
4    Cb  u0 {3,B} {5,B} {13,S}
5    Cb  u0 {4,B} {6,B} {7,S}
6    Cb  u0 {1,B} {5,B}
7    C   u0 {5,S} {8,S}
8    Cb  u0 {7,S} {9,B} {13,B}
9    Cb  u0 {8,B} {10,B}
10   Cb  u0 {9,B} {11,B}
11   Cb  u0 {10,B} {12,B}
12   Cb  u0 {11,B} {13,B}
13   Cb  u0 {4,S} {8,B} {12,B}
""",
	solute = SoluteData(
		S = -0.03670,
		B = 0.00056,
		E = 0.00353,
		L = 0.20194,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 9,
		B = 9,
		E = 13,
		L = 11,
		A = 13,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 116,
	label = "s2_6_5_s2_5_6_carbazole",
	group = 
"""
1  * Cb  u0 {2,B} {6,B}
2    Cb  u0 {1,B} {3,B}
3    Cb  u0 {2,B} {4,B}
4    Cb  u0 {3,B} {5,B} {13,S}
5    Cb  u0 {4,B} {6,B} {7,S}
6    Cb  u0 {1,B} {5,B}
7    N   u0 {5,S} {8,S}
8    Cb  u0 {7,S} {9,B} {13,B}
9    Cb  u0 {8,B} {10,B}
10   Cb  u0 {9,B} {11,B}
11   Cb  u0 {10,B} {12,B}
12   Cb  u0 {11,B} {13,B}
13   Cb  u0 {4,S} {8,B} {12,B}
""",
	solute = SoluteData(
		S = 0.15219,
		B = -0.15318,
		E = 0.05875,
		L = 0.36105,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 11,
		B = 11,
		E = 14,
		L = 14,
		A = 11,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 117,
	label = "s2_6_5_s2_5_6_dibenzofuran",
	group = 
"""
1  * Cb  u0 {2,B} {6,B}
2    Cb  u0 {1,B} {3,B}
3    Cb  u0 {2,B} {4,B}
4    Cb  u0 {3,B} {5,B} {13,S}
5    Cb  u0 {4,B} {6,B} {7,S}
6    Cb  u0 {1,B} {5,B}
7    O   u0 {5,S} {8,S}
8    Cb  u0 {7,S} {9,B} {13,B}
9    Cb  u0 {8,B} {10,B}
10   Cb  u0 {9,B} {11,B}
11   Cb  u0 {10,B} {12,B}
12   Cb  u0 {11,B} {13,B}
13   Cb  u0 {4,S} {8,B} {12,B}
""",
	solute = SoluteData(
		S = -0.08351,
		B = 0.01747,
		E = 0.00764,
		L = 0.13563,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 4,
		B = 4,
		E = 4,
		L = 2,
		A = 4,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 118,
	label = "s2_6_5_s2_5_6_dibenzothiophene",
	group = 
"""
1  * Cb  u0 {2,B} {6,B}
2    Cb  u0 {1,B} {3,B}
3    Cb  u0 {2,B} {4,B}
4    Cb  u0 {3,B} {5,B} {13,S}
5    Cb  u0 {4,B} {6,B} {7,S}
6    Cb  u0 {1,B} {5,B}
7    S   u0 {5,S} {8,S}
8    Cb  u0 {7,S} {9,B} {13,B}
9    Cb  u0 {8,B} {10,B}
10   Cb  u0 {9,B} {11,B}
11   Cb  u0 {10,B} {12,B}
12   Cb  u0 {11,B} {13,B}
13   Cb  u0 {4,S} {8,B} {12,B}
""",
	solute = SoluteData(
		S = -0.00808,
		B = -0.08225,
		E = 0.01591,
		L = 0.25147,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 45,
		B = 45,
		E = 46,
		L = 44,
		A = 46,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 119,
	label = "s2_6_5_ben_s2_5_6",
	group = 
"""
1  * Cb  u0 {2,B} {6,B}
2    Cb  u0 {1,B} {3,B}
3    Cb  u0 {2,B} {4,B}
4    Cb  u0 {3,B} {5,B} {13,S}
5    Cb  u0 {4,B} {6,B} {7,S}
6    Cb  u0 {1,B} {5,B}
7    R!H u0 {5,S} {8,S}
8    R!H u0 {7,S} {9,S} {13,S}
9    R!H u0 {8,S} {10,S}
10   R!H u0 {9,S} {11,S}
11   R!H u0 {10,S} {12,S}
12   R!H u0 {11,S} {13,S}
13   R!H u0 {4,S} {8,S} {12,S}
""",
	solute = u's2_6_5_ben_s2_5_6_hetero',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 120,
	label = "s2_6_5_ben_s2_5_6_hetero",
	group = 
"""
1  * Cb  u0 {2,B} {6,B}
2    Cb  u0 {1,B} {3,B}
3    Cb  u0 {2,B} {4,B}
4    Cb  u0 {3,B} {5,B} {13,S}
5    Cb  u0 {4,B} {6,B} {7,S}
6    Cb  u0 {1,B} {5,B}
7    N   u0 {5,S} {8,S}
8    C   u0 {7,S} {9,S} {13,S}
9    C   u0 {8,S} {10,S}
10   C   u0 {9,S} {11,S}
11   N   u0 {10,S} {12,S}
12   C   u0 {11,S} {13,S}
13   C   u0 {4,S} {8,S} {12,S}
""",
	solute = SoluteData(
		S = -0.05001,
		B = -0.04688,
		E = 0.05438,
		L = 0.10199,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 4,
		B = 4,
		E = 4,
		L = 4,
		A = 4,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 121,
	label = "s2_5_6_s2_6_6",
	group = 
"""
1  * R!H u0 {5,[S,D,B]} {13,[S,D,B]}
2    R!H u0 {3,[S,D,B]} {4,[S,D,B]} {6,[S,D,B]}
3    R!H u0 {2,[S,D,B]} {5,[S,D,B]} {10,[S,D,B]}
4    R!H u0 {2,[S,D,B]} {7,[S,D,B]} {8,[S,D,B]}
5    R!H u0 {1,[S,D,B]} {3,[S,D,B]} {9,[S,D,B]}
6    R!H u0 {2,[S,D,B]} {12,[S,D,B]}
7    R!H u0 {4,[S,D,B]} {11,[S,D,B]}
8    R!H u0 {4,[S,D,B]} {9,[S,D,B]}
9    R!H u0 {5,[S,D,B]} {8,[S,D,B]}
10   R!H u0 {3,[S,D,B]} {13,[S,D,B]}
11   R!H u0 {7,[S,D,B]} {12,[S,D,B]}
12   R!H u0 {6,[S,D,B]} {11,[S,D,B]}
13   R!H u0 {1,[S,D,B]} {10,[S,D,B]}
""",
	solute = u's2_5_6_ben_s2_6_6_ben',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 122,
	label = "s2_5_6_ben_s2_6_6_ben",
	group = 
"""
1  * R!H u0 {5,S} {13,[S,D]}
2    C   u0 {3,B} {4,B} {6,B}
3    C   u0 {2,B} {5,B} {10,S}
4    C   u0 {2,B} {7,B} {8,B}
5    C   u0 {1,S} {3,B} {9,B}
6    C   u0 {2,B} {12,B}
7    C   u0 {4,B} {11,B}
8    C   u0 {4,B} {9,B}
9    C   u0 {5,B} {8,B}
10   R!H u0 {3,S} {13,[S,D]}
11   C   u0 {7,B} {12,B}
12   C   u0 {6,B} {11,B}
13   R!H u0 {1,[S,D]} {10,[S,D]}
""",
	solute = u's2_5_6_s2_6_6_naphtho[2,1-b]thiophene',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 123,
	label = "s2_5_6_s2_6_6_naphtho[2,1-b]thiophene",
	group = 
"""
1  * S   u0 {5,S} {13,S}
2    C   u0 {3,B} {4,B} {6,B}
3    C   u0 {2,B} {5,B} {10,S}
4    C   u0 {2,B} {7,B} {8,B}
5    C   u0 {1,S} {3,B} {9,B}
6    C   u0 {2,B} {12,B}
7    C   u0 {4,B} {11,B}
8    C   u0 {4,B} {9,B}
9    C   u0 {5,B} {8,B}
10   C   u0 {3,S} {13,D}
11   C   u0 {7,B} {12,B}
12   C   u0 {6,B} {11,B}
13   C   u0 {1,S} {10,D}
""",
	solute = SoluteData(
		S = 0.00101,
		B = 0.01675,
		E = 0.01663,
		L = -0.06958,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 10,
		B = 10,
		E = 10,
		L = 10,
		A = 10,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 124,
	label = "s2_5_6_s2_6_6_benzo[g][1]benzothiole",
	group = 
"""
1  * C   u0 {5,S} {13,D}
2    C   u0 {3,B} {4,B} {6,B}
3    C   u0 {2,B} {5,B} {10,S}
4    C   u0 {2,B} {7,B} {8,B}
5    C   u0 {1,S} {3,B} {9,B}
6    C   u0 {2,B} {12,B}
7    C   u0 {4,B} {11,B}
8    C   u0 {4,B} {9,B}
9    C   u0 {5,B} {8,B}
10   S   u0 {3,S} {13,S}
11   C   u0 {7,B} {12,B}
12   C   u0 {6,B} {11,B}
13   C   u0 {1,D} {10,S}
""",
	solute = SoluteData(
		S = 0.00561,
		B = 0.00367,
		E = 0.01878,
		L = -0.14187,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 9,
		B = 9,
		E = 9,
		L = 8,
		A = 9,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 125,
	label = "s2_5_7_s2_7_3",
	group = 
"""
1  * R!H u0 {2,[S,D,B]} {3,[S,D,B]} {5,[S,D,B]} 
2  R!H u0 {1,[S,D,B]} {4,[S,D,B]} {8,[S,D,B]}
3  R!H u0 {1,[S,D,B]} {5,[S,D,B]} {7,[S,D,B]}
4  R!H u0 {2,[S,D,B]} {6,[S,D,B]} {9,[S,D,B]}
5  R!H u0 {1,[S,D,B]} {3,[S,D,B]}
6  R!H u0 {4,[S,D,B]} {10,[S,D,B]}
7  R!H u0 {3,[S,D,B]} {10,[S,D,B]}
8  R!H u0 {2,[S,D,B]} {11,[S,D,B]}
9  R!H u0 {4,[S,D,B]} {11,[S,D,B]}
10 R!H u0 {6,[S,D,B]} {7,[S,D,B]}
11 R!H u0 {8,[S,D,B]} {9,[S,D,B]}
""",
	solute = u's2_5_7_s2_7_3_ane',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 126,
	label = "s2_5_7_s2_7_3_ane",
	group = 
"""
1  * R!H u0 {2,S} {3,S} {5,S} 
2  R!H u0 {1,S} {4,S} {8,S}
3  R!H u0 {1,S} {5,S} {7,S}
4  R!H u0 {2,S} {6,S} {9,S}
5  R!H u0 {1,S} {3,S}
6  R!H u0 {4,S} {10,S}
7  R!H u0 {3,S} {10,S}
8  R!H u0 {2,S} {11,S}
9  R!H u0 {4,S} {11,S}
10 R!H u0 {6,S} {7,S}
11 R!H u0 {8,S} {9,S}
""",
	solute = u's2_5_7_s2_7_3_ane_side_ene',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 127,
	label = "s2_5_7_s2_7_3_ane_side_ene",
	group = 
"""
1  * R!H u0 {2,S} {3,S} {5,S} 
2  R!H u0 {1,S} {4,S} {8,S}
3  R!H u0 {1,S} {5,S} {7,S}
4  R!H u0 {2,S} {6,S} {9,S}
5  R!H u0 {1,S} {3,S}
6  R!H u0 {4,S} {10,S} {12,D}
7  R!H u0 {3,S} {10,S}
8  R!H u0 {2,S} {11,S}
9  R!H u0 {4,S} {11,S}
10 R!H u0 {6,S} {7,S}
11 R!H u0 {8,S} {9,S}
12 R!H u0 {6,D}
""",
	solute = SoluteData(
		S = -0.04971,
		B = 0.05845,
		E = -0.03569,
		L = -0.03516,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
		E = 2,
		L = 2,
		A = 2,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 128,
	label = "s2_5_7_s2_7_3_ene",
	group = 
"""
1  * R!H u0 {2,S} {3,S} {5,S} 
2  R!H u0 {1,S} {4,S} {8,D}
3  R!H u0 {1,S} {5,S} {7,S}
4  R!H u0 {2,S} {6,S} {9,S}
5  R!H u0 {1,S} {3,S}
6  R!H u0 {4,S} {10,S}
7  R!H u0 {3,S} {10,S}
8  R!H u0 {2,D} {11,S}
9  R!H u0 {4,S} {11,S}
10 R!H u0 {6,S} {7,S}
11 R!H u0 {8,S} {9,S}
""",
	solute = SoluteData(
		S = -0.04118,
		B = -0.03465,
		E = -0.00877,
		L = -0.18708,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 1,
		B = 1,
		E = 1,
		L = 1,
		A = 1,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 129,
	label = "Nortricyclene_general",
	group = 
"""
1  * R!H u0 {2,[S,D,B]} {3,[S,D,B]} {6,[S,D,B]}
2  R!H u0 {1,[S,D,B]} {3,[S,D,B]} {5,[S,D,B]}
3  R!H u0 {1,[S,D,B]} {2,[S,D,B]} {7,[S,D,B]}
4  R!H u0 {5,[S,D,B]} {6,[S,D,B]} {7,[S,D,B]}
5  R!H u0 {2,[S,D,B]} {4,[S,D,B]}
6  R!H u0 {1,[S,D,B]} {4,[S,D,B]}
7  R!H u0 {3,[S,D,B]} {4,[S,D,B]}
""",
	solute = u'Nortricyclene',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 130,
	label = "Nortricyclene",
	group = 
"""
1  * C u0 {2,S} {3,S} {6,S}
2  C u0 {1,S} {3,S} {5,S}
3  C u0 {1,S} {2,S} {7,S}
4  C u0 {5,S} {6,S} {7,S}
5  C u0 {2,S} {4,S}
6  C u0 {1,S} {4,S}
7  C u0 {3,S} {4,S}
""",
	solute = SoluteData(
		S = -0.09421,
		B = 0.06698,
		E = 0.00977,
		L = -0.24951,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
		E = 2,
		L = 2,
		A = 2,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 131,
	label = "s3_6_3_s3_3_6",
	group = 
"""
1  * R!H u0 {2,[S,D,B]} {3,[S,D,B]} {5,[S,D,B]}
2  R!H u0 {1,[S,D,B]} {4,[S,D,B]} {6,[S,D,B]}
3  R!H u0 {1,[S,D,B]} {4,[S,D,B]} {7,[S,D,B]}
4  R!H u0 {2,[S,D,B]} {3,[S,D,B]} {8,[S,D,B]}
5  R!H u0 {1,[S,D,B]} {9,[S,D,B]}
6  R!H u0 {2,[S,D,B]} {10,[S,D,B]}
7  R!H u0 {3,[S,D,B]} {10,[S,D,B]}
8  R!H u0 {4,[S,D,B]} {9,[S,D,B]}
9  R!H u0 {5,[S,D,B]} {8,[S,D,B]}
10 R!H u0 {6,[S,D,B]} {7,[S,D,B]}
""",
	solute = u's3_6_3_s3_3_6_ane',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 132,
	label = "s3_6_3_s3_3_6_ane",
	group = 
"""
1  * C u0 {2,S} {3,S} {5,S}
2  C u0 {1,S} {4,S} {6,S}
3  C u0 {1,S} {4,S} {7,S}
4  C u0 {2,S} {3,S} {8,S}
5  C u0 {1,S} {9,S}
6  C u0 {2,S} {10,S}
7  C u0 {3,S} {10,S}
8  C u0 {4,S} {9,S}
9  C u0 {5,S} {8,S}
10 C u0 {6,S} {7,S}
""",
	solute = SoluteData(
		S = -0.09448,
		B = 0.06445,
		E = -0.06016,
		L = -0.23017,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
		E = 2,
		L = 2,
		A = 2,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 133,
	label = "s3_6_3_s3_3_6_ene",
	group = 
"""
1  * C u0 {2,S} {3,S} {5,S}
2  C u0 {1,S} {4,S} {6,S}
3  C u0 {1,S} {4,S} {7,S}
4  C u0 {2,S} {3,S} {8,S}
5  C u0 {1,S} {9,S}
6  C u0 {2,S} {10,S}
7  C u0 {3,S} {10,D}
8  C u0 {4,S} {9,S}
9  C u0 {5,S} {8,S}
10 C u0 {6,S} {7,D}
""",
	solute = SoluteData(
		S = -0.11844,
		B = 0.04445,
		E = -0.05581,
		L = -0.40248,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
		E = 2,
		L = 2,
		A = 2,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 134,
	label = "Acenaphthene_general",
	group = 
"""
1  * R!H u0 {2,[S,D,B]} {4,[S,D,B]}
2  R!H u0 {1,[S,D,B]} {3,[S,D,B]}
3  R!H u0 {2,[S,D,B]} {5,[S,D,B]} {7,[S,D,B]}
4  R!H u0 {1,[S,D,B]} {5,[S,D,B]} {8,[S,D,B]}
5  R!H u0 {3,[S,D,B]} {4,[S,D,B]} {6,[S,D,B]}
6  R!H u0 {5,[S,D,B]} {9,[S,D,B]} {10,[S,D,B]}
7  R!H u0 {3,[S,D,B]} {11,[S,D,B]}
8  R!H u0 {4,[S,D,B]} {12,[S,D,B]}
9  R!H u0 {6,[S,D,B]} {12,[S,D,B]}
10 R!H u0 {6,[S,D,B]} {11,[S,D,B]}
11 R!H u0 {7,[S,D,B]} {10,[S,D,B]}
12 R!H u0 {8,[S,D,B]} {9,[S,D,B]}
""",
	solute = u'Acenaphthene',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 135,
	label = "Acenaphthene",
	group = 
"""
1  * C u0 {2,S} {4,S}
2  C u0 {1,S} {3,S}
3  C u0 {2,S} {5,B} {7,B}
4  C u0 {1,S} {5,B} {8,B}
5  C u0 {3,B} {4,B} {6,B}
6  C u0 {5,B} {9,B} {10,B}
7  C u0 {3,B} {11,B}
8  C u0 {4,B} {12,B}
9  C u0 {6,B} {12,B}
10 C u0 {6,B} {11,B}
11 C u0 {7,B} {10,B}
12 C u0 {8,B} {9,B}
""",
	solute = SoluteData(
		S = 0.01537,
		B = -0.01647,
		E = 0.06220,
		L = -0.06515,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 4,
		B = 4,
		E = 4,
		L = 4,
		A = 4,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 136,
	label = "Acenaphthylene",
	group = 
"""
1  * C u0 {2,D} {4,S}
2  C u0 {1,D} {3,S}
3  C u0 {2,S} {5,B} {7,B}
4  C u0 {1,S} {5,B} {8,B}
5  C u0 {3,B} {4,B} {6,B}
6  C u0 {5,B} {9,B} {10,B}
7  C u0 {3,B} {11,B}
8  C u0 {4,B} {12,B}
9  C u0 {6,B} {12,B}
10 C u0 {6,B} {11,B}
11 C u0 {7,B} {10,B}
12 C u0 {8,B} {9,B}
""",
	solute = SoluteData(
		S = -0.00029,
		B = 0.01016,
		E = -0.03186,
		L = -0.39261,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
		E = 2,
		L = 2,
		A = 2,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 137,
	label = "s2_5_5_s2_5_5_ane",
	group = 
"""
1    R!H u0 {2,S} {4,S} {9,S}
2    R!H u0 {1,S} {3,S} {8,S}
3  * R!H u0 {2,S} {5,S} {6,S}
4    R!H u0 {1,S} {5,S} {7,S}
5    R!H u0 {3,S} {4,S}
6    R!H u0 {3,S} {7,S}
7    R!H u0 {4,S} {6,S}
8    R!H u0 {2,S} {10,S}
9    R!H u0 {1,S} {10,S}
10   R!H u0 {8,S} {9,S}
""",
	solute = SoluteData(
		S = -0.00425,
		B = 0.01500,
		E = -0.02258,
		L = -0.13095,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 1,
		B = 1,
		E = 1,
		L = 1,
		A = 1,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 138,
	label = "s1_3_6",
	group = 
"""
1   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6   R!H u0 {4,[S,D,T,B]} {8,[S,D,T,B]}
7   R!H u0 {5,[S,D,T,B]} {8,[S,D,T,B]}
8 * R!H u0 {6,[S,D,T,B]} {7,[S,D,T,B]}
""",
	solute = u's1_3_6_ane',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 139,
	label = "s1_3_6_ane",
	group = 
"""
1   R!H u0 {2,S} {3,S} {4,S} {5,S}
2   R!H u0 {1,S} {3,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {6,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {4,S} {8,S}
7   R!H u0 {5,S} {8,S}
8 * R!H u0 {6,S} {7,S}
""",
	solute = SoluteData(
		S = -0.00921,
		B = 0.02340,
		E = -0.03777,
		L = -0.03540,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 1,
		B = 1,
		E = 1,
		L = 1,
		A = 1,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 140,
	label = "s1_5_5",
	group = 
"""
1   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2 * R!H u0 {1,[S,D,T,B]} {9,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
4   R!H u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
6   R!H u0 {4,[S,D,T,B]} {7,[S,D,T,B]}
7   R!H u0 {3,[S,D,T,B]} {6,[S,D,T,B]}
8   R!H u0 {5,[S,D,T,B]} {9,[S,D,T,B]}
9   R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
""",
	solute = u's1_5_5_ane',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 141,
	label = "s1_5_5_ane",
	group = 
"""
1   R!H u0 {2,S} {3,S} {4,S} {5,S}
2 * R!H u0 {1,S} {9,S}
3   R!H u0 {1,S} {7,S}
4   R!H u0 {1,S} {6,S}
5   R!H u0 {1,S} {8,S}
6   R!H u0 {4,S} {7,S}
7   R!H u0 {3,S} {6,S}
8   R!H u0 {5,S} {9,S}
9   R!H u0 {2,S} {8,S}
""",
	solute = SoluteData(
		S = 0.12322,
		B = 0.03064,
		E = 0.05470,
		L = 0.04819,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 6,
		B = 6,
		E = 7,
		L = 3,
		A = 6,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 142,
	label = "s1_5_6",
	group = 
"""
1    R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2    R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
3    R!H u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
4    R!H u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
5    R!H u0 {1,[S,D,T,B]} {9,[S,D,T,B]}
6  * R!H u0 {3,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H u0 {2,[S,D,T,B]} {6,[S,D,T,B]}
8    R!H u0 {4,[S,D,T,B]} {10,[S,D,T,B]}
9    R!H u0 {5,[S,D,T,B]} {10,[S,D,T,B]}
10   R!H u0 {8,[S,D,T,B]} {9,[S,D,T,B]}
""",
	solute = u's1_5_6_ane',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 143,
	label = "s1_5_6_ane",
	group = 
"""
1    R!H u0 {2,S} {3,S} {4,S} {5,S}
2    R!H u0 {1,S} {7,S}
3    R!H u0 {1,S} {6,S}
4    R!H u0 {1,S} {8,S}
5    R!H u0 {1,S} {9,S}
6  * R!H u0 {3,S} {7,S}
7    R!H u0 {2,S} {6,S}
8    R!H u0 {4,S} {10,S}
9    R!H u0 {5,S} {10,S}
10   R!H u0 {8,S} {9,S}
""",
	solute = SoluteData(
		S = 0.06245,
		B = 0.12433,
		E = 0.02612,
		L = 0.10273,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 16,
		B = 16,
		E = 16,
		L = 15,
		A = 16,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 144,
	label = "s1_5_6_ene",
	group =  "OR{s1_5_6_ene_1, s1_5_6_ene_2, s1_5_6_ene_7, s1_5_6_ene_8}",
	solute = u's1_5_6_ene_1',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 145,
	label = "s1_5_6_ene_1",
	group = 
"""
1    R!H u0 {2,S} {3,S} {4,S} {5,S}
2    R!H u0 {1,S} {6,S}
3    R!H u0 {1,S} {7,D}
4    R!H u0 {1,S} {8,S}
5    R!H u0 {1,S} {9,S}
6  * R!H u0 {2,S} {9,S}
7    R!H u0 {3,D} {10,S}
8    R!H u0 {4,S} {10,S}
9    R!H u0 {5,S} {6,S}
10   R!H u0 {7,S} {8,S}
""",
	solute = SoluteData(
		S = -0.01266,
		B = 0.04906,
		E = 0.06681,
		L = 0.19447,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 3,
		L = 3,
		A = 3,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 146,
	label = "s1_5_6_ene_2",
	group = 
"""
1    R!H u0 {2,S} {3,S} {4,S} {5,S}
2    R!H u0 {1,S} {6,S}
3    R!H u0 {1,S} {8,S}
4    R!H u0 {1,S} {7,S}
5    R!H u0 {1,S} {9,S}
6    R!H u0 {2,S} {10,S}
7  * R!H u0 {4,S} {9,S}
8    R!H u0 {3,S} {10,D}
9    R!H u0 {5,S} {7,S}
10   R!H u0 {6,S} {8,D}
""",
	solute = SoluteData(
		S = -0.01143,
		B = 0.02849,
		E = -0.01609,
		L = 0.05583,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
		E = 2,
		L = 2,
		A = 2,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 147,
	label = "s1_5_6_ene_7",
	group = 
"""
1    R!H u0 {2,S} {3,S} {4,S} {5,S}
2    R!H u0 {1,S} {7,S}
3    R!H u0 {1,S} {8,D}
4    R!H u0 {1,S} {6,S}
5    R!H u0 {1,S} {9,S}
6    R!H u0 {4,S} {10,S}
7    R!H u0 {2,S} {10,S}
8  * R!H u0 {3,D} {9,S}
9    R!H u0 {5,S} {8,S}
10   R!H u0 {6,S} {7,S}
""",
	solute = SoluteData(
		S = 0.00048,
		B = -0.00723,
		E = 0.03829,
		L = -0.03837,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 1,
		B = 1,
		E = 1,
		L = 1,
		A = 1,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 148,
	label = "s1_5_6_ene_8",
	group = 
"""
1    R!H u0 {2,S} {3,S} {4,S} {5,S}
2    R!H u0 {1,S} {7,S}
3    R!H u0 {1,S} {6,S}
4    R!H u0 {1,S} {9,S}
5    R!H u0 {1,S} {8,S}
6  * R!H u0 {3,S} {8,D}
7    R!H u0 {2,S} {10,S}
8    R!H u0 {5,S} {6,D}
9    R!H u0 {4,S} {10,S}
10   R!H u0 {7,S} {9,S}
""",
	solute = SoluteData(
		S = -0.00962,
		B = 0.02498,
		E = -0.00381,
		L = -0.09931,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 1,
		B = 1,
		E = 1,
		L = 1,
		A = 1,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 149,
	label = "s1_6_6",
	group = 
"""
1    R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2    R!H u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
3    R!H u0 {1,[S,D,T,B]} {9,[S,D,T,B]}
4    R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
5    R!H u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H u0 {5,[S,D,T,B]} {11,[S,D,T,B]}
7    R!H u0 {4,[S,D,T,B]} {10,[S,D,T,B]}
8    R!H u0 {2,[S,D,T,B]} {11,[S,D,T,B]}
9    R!H u0 {3,[S,D,T,B]} {10,[S,D,T,B]}
10 * R!H u0 {7,[S,D,T,B]} {9,[S,D,T,B]}
11   R!H u0 {6,[S,D,T,B]} {8,[S,D,T,B]}
""",
	solute = u's1_6_6_ane',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 150,
	label = "s1_6_6_ane",
	group = 
"""
1    R!H u0 {2,S} {3,S} {4,S} {5,S}
2    R!H u0 {1,S} {8,S}
3    R!H u0 {1,S} {9,S}
4    R!H u0 {1,S} {7,S}
5    R!H u0 {1,S} {6,S}
6    R!H u0 {5,S} {11,S}
7    R!H u0 {4,S} {10,S}
8    R!H u0 {2,S} {11,S}
9    R!H u0 {3,S} {10,S}
10 * R!H u0 {7,S} {9,S}
11   R!H u0 {6,S} {8,S}
""",
	solute = u's1_6_6_ane_2,4,8,10-Tetraoxa-3,9-diphosphaspiro-3,9-dioxide',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 151,
	label = "s1_6_6_ane_2,4,8,10-Tetraoxa-3,9-diphosphaspiro-3,9-dioxide",
	group = 
"""
1    C   u0 {2,S} {3,S} {4,S} {5,S}
2    C   u0 {1,S} {8,S}
3    C   u0 {1,S} {9,S}
4    C   u0 {1,S} {7,S}
5    C   u0 {1,S} {6,S}
6    O2s u0 {5,S} {11,S}
7    O2s u0 {4,S} {10,S}
8    O2s u0 {2,S} {11,S}
9    O2s u0 {3,S} {10,S}
10 * P5d u0 {7,S} {9,S} {12,D}
11   P5d u0 {6,S} {8,S} {13,D}
12   O2d u0 {10,D}
13   O2d u0 {11,D}
""",
	solute = SoluteData(
		S = -0.05123,
		B = -0.11390,
		E = 0.03470,
		L = 0.11015,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 5,
		E = 5,
		L = 4,
		A = 6,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 152,
	label = "s2_3_5",
	group = 
"""
1 * R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {6,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
6   R!H u0 {4,[S,D,T,B]} {5,[S,D,T,B]}
""",
	solute = u's2_3_5_ane',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 153,
	label = "s2_3_5_ene",
	group =  "OR{s2_3_5_ene_1, s2_3_5_ene_side}",
	solute = u's2_3_5_ene_1',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 154,
	label = "s2_3_5_ene_1",
	group = 
"""
1 * R!H u0 {2,S} {3,S} {5,S}
2   R!H u0 {1,S} {3,S} {4,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {2,S} {6,D}
5   R!H u0 {1,S} {6,S}
6   R!H u0 {4,D} {5,S}
""",
	solute = SoluteData(
		S = -0.04519,
		B = -0.00282,
		E = -0.02174,
		L = -0.19696,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 4,
		B = 4,
		E = 4,
		L = 4,
		A = 4,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 155,
	label = "s2_3_5_ene_side",
	group = 
"""
1 * R!H u0 {2,S} {4,S} {6,S}
2   R!H u0 {1,S} {4,S} {5,S}
3   R!H u0 {5,S} {6,S} {7,D}
4   R!H u0 {1,S} {2,S}
5   R!H u0 {2,S} {3,S}
6   R!H u0 {1,S} {3,S}
7   R!H ux {3,D}
""",
	solute = SoluteData(
		S = -0.02003,
		B = 0.01210,
		E = 0.04142,
		L = -0.35397,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 1,
		B = 1,
		E = 1,
		L = 1,
		A = 1,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 156,
	label = "s2_3_5_ane",
	group = 
"""
1 * R!H u0 {2,S} {3,S} {5,S}
2   R!H u0 {1,S} {3,S} {4,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {2,S} {6,S}
5   R!H u0 {1,S} {6,S}
6   R!H u0 {4,S} {5,S}
""",
	solute = SoluteData(
		S = -0.11358,
		B = 0.00000,
		E = 0.01834,
		L = -0.32737,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 12,
		B = 13,
		E = 12,
		L = 12,
		A = 15,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 157,
	label = "s2_3_6",
	group = 
"""
1   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {6,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6 * R!H u0 {4,[S,D,T,B]} {7,[S,D,T,B]}
7   R!H u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
""",
	solute = u's2_3_6_ane',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 158,
	label = "s2_3_6_ane",
	group = 
"""
1   R!H u0 {2,S} {3,S} {5,S}
2   R!H u0 {1,S} {3,S} {4,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {2,S} {6,S}
5   R!H u0 {1,S} {7,S}
6 * R!H u0 {4,S} {7,S}
7   R!H u0 {5,S} {6,S}
""",
	solute = SoluteData(
		S = 0.03346,
		B = 0.00000,
		E = -0.02132,
		L = -0.10768,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 4,
		B = 6,
		E = 4,
		L = 4,
		A = 6,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 159,
	label = "s2_3_6_ene",
	group =  "OR{s2_3_6_ene_1, s2_3_6_ene_2}",
	solute = u's2_3_6_ene_1',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 160,
	label = "s2_3_6_ene_1",
	group = 
"""
1   R!H u0 {2,S} {3,S} {4,S}
2   R!H u0 {1,S} {3,S} {5,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {6,D}
5   R!H u0 {2,S} {7,S}
6 * R!H u0 {4,D} {7,S}
7   R!H u0 {5,S} {6,S}
""",
	solute = SoluteData(
		S = -0.00984,
		B = -0.00092,
		E = -0.02400,
		L = 0.00882,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
		E = 2,
		L = 2,
		A = 2,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 161,
	label = "s2_3_6_ene_2",
	group = 
"""
1   R!H u0 {2,S} {3,S} {4,S}
2   R!H u0 {1,S} {3,S} {5,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {7,S}
5   R!H u0 {2,S} {6,S}
6 * R!H u0 {5,S} {7,D}
7   R!H u0 {4,S} {6,D}
""",
	solute = SoluteData(
		S = 0.13834,
		B = 0.00926,
		E = 0.11867,
		L = 0.40853,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 3,
		L = 3,
		A = 3,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 162,
	label = "s2_3_8",
	group = 
"""
1 * R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {6,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6   R!H u0 {4,[S,D,T,B]} {8,[S,D,T,B]}
7   R!H u0 {5,[S,D,T,B]} {9,[S,D,T,B]}
8   R!H u0 {6,[S,D,T,B]} {9,[S,D,T,B]}
9   R!H u0 {7,[S,D,T,B]} {8,[S,D,T,B]}
""",
	solute = u's2_3_8_ane',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 163,
	label = "s2_3_8_ane",
	group = 
"""
1 * R!H u0 {2,S} {3,S} {5,S}
2   R!H u0 {1,S} {3,S} {4,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {2,S} {6,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {4,S} {8,S}
7   R!H u0 {5,S} {9,S}
8   R!H u0 {6,S} {9,S}
9   R!H u0 {7,S} {8,S}
""",
	solute = u's2_3_6_ane',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 164,
	label = "s2_4_5",
	group = 
"""
1 * R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6   R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
7   R!H u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
""",
	solute = u's2_4_5_ane',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 165,
	label = "s2_4_5_ane",
	group = 
"""
1 * R!H u0 {2,S} {3,S} {5,S}
2   R!H u0 {1,S} {4,S} {6,S}
3   R!H u0 {1,S} {4,S}
4   R!H u0 {2,S} {3,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {2,S} {7,S}
7   R!H u0 {5,S} {6,S}
""",
	solute = SoluteData(
		S = 0.00818,
		B = 0.00000,
		E = -0.02020,
		L = -0.17704,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 4,
		L = 3,
		A = 4,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 166,
	label = "s2_4_5_ane_hetero_N_S",
	group = 
"""
1 * C   u0 {2,S} {3,S} {5,S}
2   N   u0 {1,S} {4,S} {6,S}
3   C   u0 {1,S} {4,S}
4   C   u0 {2,S} {3,S}
5   S   u0 {1,S} {7,S}
6   C   u0 {2,S} {7,S}
7   C   u0 {5,S} {6,S}
""",
	solute = SoluteData(
		S = -0.14051,
		B = -0.00345,
		E = 0.11392,
		L = -0.20032,
		A = -0.17693,
	),
	dataCount = DataCountGAV(
		S = 16,
		B = 16,
		E = 16,
		L = 15,
		A = 16,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 167,
	label = "s2_4_6",
	group = 
"""
1   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {6,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]}
5   R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
6   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
7 * R!H u0 {6,[S,D,T,B]} {8,[S,D,T,B]}
8   R!H u0 {5,[S,D,T,B]} {7,[S,D,T,B]}
""",
	solute = u's2_4_6_ene',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 168,
	label = "s2_4_6_ene",
	group =  "OR{s2_4_6_ene_1}",
	solute = u's2_4_6_ene_1',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 169,
	label = "s2_4_6_ene_1",
	group = 
"""
1   R!H u0 {2,S} {3,S} {5,S}
2   R!H u0 {1,S} {4,S} {6,S}
3   R!H u0 {1,S} {4,S}
4   R!H u0 {2,S} {3,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {2,S} {8,D}
7 * R!H u0 {5,S} {8,S}
8   R!H u0 {6,D} {7,S}
""",
	solute = SoluteData(
		S = 0.00319,
		B = 0.00594,
		E = 0.06447,
		L = -0.04443,
		A = 0.02298,
	),
	dataCount = DataCountGAV(
		S = 11,
		B = 11,
		E = 11,
		L = 11,
		A = 11,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 170,
	label = "s2_5_5",
	group = 
"""
1   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
3 * R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
6   R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
7   R!H u0 {3,[S,D,T,B]} {4,[S,D,T,B]}
8   R!H u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
""",
	solute = u's2_5_5_ane',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 171,
	label = "s2_5_5_ane",
	group = 
"""
1   R!H u0 {2,S} {3,S} {5,S}
2   R!H u0 {1,S} {4,S} {6,S}
3 * R!H u0 {1,S} {7,S}
4   R!H u0 {2,S} {7,S}
5   R!H u0 {1,S} {8,S}
6   R!H u0 {2,S} {8,S}
7   R!H u0 {3,S} {4,S}
8   R!H u0 {5,S} {6,S}
""",
	solute = SoluteData(
		S = -0.01758,
		B = -0.02628,
		E = 0.01724,
		L = -0.11722,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 22,
		B = 22,
		E = 23,
		L = 21,
		A = 23,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 172,
	label = "s2_5_5_ene",
	group =  "OR{s2_5_5_ene_0, s2_5_5_ene_1}",
	solute = u's2_5_5_ene_1',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 173,
	label = "s2_5_5_ene_0",
	group = 
"""
1   R!H u0 {2,S} {3,S} {4,S}
2   R!H u0 {1,S} {5,D} {6,S}
3 * R!H u0 {1,S} {8,S}
4   R!H u0 {1,S} {7,S}
5   R!H u0 {2,D} {7,S}
6   R!H u0 {2,S} {8,S}
7   R!H u0 {4,S} {5,S}
8   R!H u0 {3,S} {6,S}
""",
	solute = SoluteData(
		S = 0.00048,
		B = -0.00723,
		E = 0.03829,
		L = -0.03837,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 1,
		B = 1,
		E = 1,
		L = 1,
		A = 1,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 174,
	label = "s2_5_5_ene_1",
	group = 
"""
1   R!H u0 {2,S} {4,S} {5,S}
2   R!H u0 {1,S} {3,S} {6,S}
3 * R!H u0 {2,S} {7,D}
4   R!H u0 {1,S} {8,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {2,S} {8,S}
7   R!H u0 {3,D} {5,S}
8   R!H u0 {4,S} {6,S}
""",
	solute = SoluteData(
		S = -0.03907,
		B = -0.02500,
		E = -0.04708,
		L = 0.05704,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 2,
		E = 3,
		L = 3,
		A = 3,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 175,
	label = "s2_5_5_diene",
	group =  "OR{s2_5_5_diene_0_2, s2_5_5_diene_0_4}",
	solute = u's2_5_5_diene_0_4',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 176,
	label = "s2_5_5_diene_0_2",
	group = 
"""
1   R!H u0 {2,S} {3,S} {4,S}
2   R!H u0 {1,S} {5,S} {6,D}
3 * R!H u0 {1,S} {8,S}
4   R!H u0 {1,S} {7,D}
5   R!H u0 {2,S} {8,S}
6   R!H u0 {2,D} {7,S}
7   R!H u0 {4,D} {6,S}
8   R!H u0 {3,S} {5,S}
""",
	solute = u's2_5_5_diene_0_4',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 177,
	label = "s2_5_5_diene_0_4",
	group = 
"""
1   R!H u0 {2,S} {3,D} {4,S}
2   R!H u0 {1,S} {5,D} {6,S}
3 * R!H u0 {1,D} {7,S}
4   R!H u0 {1,S} {8,S}
5   R!H u0 {2,D} {8,S}
6   R!H u0 {2,S} {7,S}
7   R!H u0 {3,S} {6,S}
8   R!H u0 {4,S} {5,S}
""",
	solute = SoluteData(
		S = 0.03897,
		B = -0.02929,
		E = 0.00915,
		L = 0.02292,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
		E = 2,
		L = 1,
		A = 2,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 178,
	label = "s2_5_6",
	group = 
"""
1 * R!H u0 {2,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {6,[S,D,T,B]}
3   R!H u0 {2,[S,D,T,B]} {9,[S,D,T,B]}
4   R!H u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6   R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
7   R!H u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
8   R!H u0 {4,[S,D,T,B]} {9,[S,D,T,B]}
9   R!H u0 {3,[S,D,T,B]} {8,[S,D,T,B]}
""",
	solute = u's2_5_6_ane',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 179,
	label = "s2_5_6_ane",
	group = 
"""
1 * R!H u0 {2,S} {4,S} {5,S}
2   R!H u0 {1,S} {3,S} {6,S}
3   R!H u0 {2,S} {9,S}
4   R!H u0 {1,S} {8,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {2,S} {7,S}
7   R!H u0 {5,S} {6,S}
8   R!H u0 {4,S} {9,S}
9   R!H u0 {3,S} {8,S}
""",
	solute = SoluteData(
		S = 0.06297,
		B = 0.00000,
		E = 0.04766,
		L = 0.10993,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 28,
		B = 28,
		E = 29,
		L = 24,
		A = 28,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 180,
	label = "s2_5_6_ene",
	group =  "OR{s2_5_6_ene_0, s2_5_6_ene_1, s2_5_6_ene_m, s2_5_6_ene_2, s2_5_6_ene_5}",
	solute = u's2_5_6_ene_m',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 181,
	label = "s2_5_6_ene_0",
	group = 
"""
1 * R!H u0 {2,S} {3,S} {5,S}
2   R!H u0 {1,S} {4,D} {6,S}
3   R!H u0 {1,S} {7,S}
4   R!H u0 {2,D} {8,S}
5   R!H u0 {1,S} {9,S}
6   R!H u0 {2,S} {7,S}
7   R!H u0 {3,S} {6,S}
8   R!H u0 {4,S} {9,S}
9   R!H u0 {5,S} {8,S}
""",
	solute = SoluteData(
		S = -0.01105,
		B = -0.02032,
		E = -0.07840,
		L = 0.02487,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 4,
		B = 4,
		E = 4,
		L = 3,
		A = 4,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 182,
	label = "s2_5_6_ene_1",
	group = 
"""
1 * R!H u0 {2,S} {4,S} {6,S}
2   R!H u0 {1,S} {3,S} {5,S}
3   R!H u0 {2,S} {8,D}
4   R!H u0 {1,S} {7,S}
5   R!H u0 {2,S} {7,S}
6   R!H u0 {1,S} {9,S}
7   R!H u0 {4,S} {5,S}
8   R!H u0 {3,D} {9,S}
9   R!H u0 {6,S} {8,S}
""",
	solute = SoluteData(
		S = 0.07429,
		B = 0.04486,
		E = 0.14050,
		L = 0.12520,
		A = -0.00999,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
		E = 2,
		L = 2,
		A = 2,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 183,
	label = "s2_5_6_ene_m",
	group = 
"""
1 * R!H u0 {2,D} {5,S} {6,S}
2   R!H u0 {1,D} {3,S} {4,S}
3   R!H u0 {2,S} {8,S}
4   R!H u0 {2,S} {7,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {1,S} {9,S}
7   R!H u0 {4,S} {5,S}
8   R!H u0 {3,S} {9,S}
9   R!H u0 {6,S} {8,S}
""",
	solute = SoluteData(
		S = -0.08669,
		B = 0.00540,
		E = 0.02064,
		L = -0.30851,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 5,
		E = 5,
		L = 5,
		A = 5,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 184,
	label = "s2_5_6_ene_2",
	group = 
"""
1 * R!H u0 {2,S} {5,S} {6,S}
2   R!H u0 {1,S} {3,S} {4,S}
3   R!H u0 {2,S} {7,S}
4   R!H u0 {2,S} {8,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {1,S} {9,S}
7   R!H u0 {3,S} {5,S}
8   R!H u0 {4,S} {9,D}
9   R!H u0 {6,S} {8,D}
""",
	solute = u's2_5_6_ene_0',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 185,
	label = "s2_5_6_ene_5",
	group = 
"""
1 * R!H u0 {2,S} {3,D} {6,S}
2   R!H u0 {1,S} {4,S} {5,S}
3   R!H u0 {1,D} {7,S}
4   R!H u0 {2,S} {9,S}
5   R!H u0 {2,S} {7,S}
6   R!H u0 {1,S} {8,S}
7   R!H u0 {3,S} {5,S}
8   R!H u0 {6,S} {9,S}
9   R!H u0 {4,S} {8,S}
""",
	solute = SoluteData(
		S = 0.01693,
		B = -0.03572,
		E = 0.08585,
		L = 0.09047,
		A = -0.00992,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
		E = 2,
		L = 2,
		A = 2,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 186,
	label = "s2_5_6_diene",
	group =  "OR{s2_5_6_diene_m_2, s2_5_6_diene_m_7}",
	solute = u's2_5_6_diene_m_7',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 187,
	label = "s2_5_6_diene_m_2",
	group = 
"""
1 * R!H u0 {2,D} {3,S} {6,S}
2   R!H u0 {1,D} {4,S} {5,S}
3   R!H u0 {1,S} {9,S}
4   R!H u0 {2,S} {8,S}
5   R!H u0 {2,S} {7,S}
6   R!H u0 {1,S} {7,S}
7   R!H u0 {5,S} {6,S}
8   R!H u0 {4,S} {9,D}
9   R!H u0 {3,S} {8,D}
""",
	solute = u's2_5_6_diene_m_7',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 188,
	label = "s2_5_6_diene_m_7",
	group = 
"""
1 * R!H u0 {2,D} {3,S} {5,S}
2   R!H u0 {1,D} {4,S} {6,S}
3   R!H u0 {1,S} {8,S}
4   R!H u0 {2,S} {7,S}
5   R!H u0 {1,S} {7,D}
6   R!H u0 {2,S} {9,S}
7   R!H u0 {4,S} {5,D}
8   R!H u0 {3,S} {9,S}
9   R!H u0 {6,S} {8,S}
""",
	solute = SoluteData(
		S = -0.00510,
		B = -0.01207,
		E = 0.01266,
		L = 0.06481,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 1,
		E = 2,
		L = 2,
		A = 2,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 189,
	label = "s2_5_6_diene_m_7_hetero",
	group = 
"""
1 * C   u0 {2,D} {3,S} {5,S}
2   C   u0 {1,D} {4,S} {6,S}
3   N   u0 {1,S} {8,S}
4   N   u0 {2,S} {7,S}
5   N   u0 {1,S} {7,D}
6   C   u0 {2,S} {9,S}
7   C   u0 {4,S} {5,D}
8   C   u0 {3,S} {9,S}
9   N   u0 {6,S} {8,S}
""",
	solute = u's2_5_6_diene_xanthine',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 190,
	label = "s2_5_6_diene_xanthine",
	group = 
"""
1 * C   u0 {2,D} {3,S} {5,S}
2   C   u0 {1,D} {4,S} {6,S}
3   N   u0 {1,S} {8,S}
4   N   u0 {2,S} {7,S}
5   N   u0 {1,S} {7,D}
6   CO  u0 {2,S} {9,S}
7   C   u0 {4,S} {5,D}
8   CO  u0 {3,S} {9,S}
9   N   u0 {6,S} {8,S}
""",
	solute = SoluteData(
		S = 0.06485,
		B = 0.04158,
		E = 0.06747,
		L = 0.28290,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 22,
		B = 22,
		E = 23,
		L = 22,
		A = 22,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 191,
	label = "s2_5_6_triene",
	group =  "OR{s2_5_6_triene_m_1_7}",
	solute = u's2_5_6_triene_m_1_7',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 192,
	label = "s2_5_6_triene_m_1_7",
	group = 
"""
1 * R!H u0 {2,D} {3,S} {6,S}
2   R!H u0 {1,D} {4,S} {5,S}
3   R!H u0 {1,S} {9,D}
4   R!H u0 {2,S} {8,S}
5   R!H u0 {2,S} {7,S}
6   R!H u0 {1,S} {7,D}
7   R!H u0 {5,S} {6,D}
8   R!H u0 {4,S} {9,S}
9   R!H u0 {3,D} {8,S}
""",
	solute = SoluteData(
		S = -0.07579,
		B = 0.01305,
		E = -0.06278,
		L = -0.23438,
		A = 0.02605,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
		E = 2,
		L = 2,
		A = 2,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 193,
	label = "s2_5_6_tetraene",
	group =  "OR{s2_5_6_tetraene_1_3_5_7, s2_5_6_tetraene_1_3_5_8}",
	solute = u's2_5_6_tetraene_1_3_5_7',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 194,
	label = "s2_5_6_tetraene_1_3_5_7",
	group = 
"""
1 * R!H u0 {2,S} {4,S} {5,D}
2   R!H u0 {1,S} {3,S} {6,S}
3   R!H u0 {2,S} {8,D}
4   R!H u0 {1,S} {9,D}
5   R!H u0 {1,D} {7,S}
6   R!H u0 {2,S} {7,D}
7   R!H u0 {5,S} {6,D}
8   R!H u0 {3,D} {9,S}
9   R!H u0 {4,D} {8,S}
""",
	solute = SoluteData(
		S = 0.03533,
		B = -0.00632,
		E = -0.00303,
		L = -0.07679,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 5,
		E = 5,
		L = 3,
		A = 5,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 195,
	label = "s2_5_6_tetraene_1_3_5_8",
	group = 
"""
1 * R!H u0 {2,S} {5,S} {6,D}
2   R!H u0 {1,S} {3,S} {4,D}
3   R!H u0 {2,S} {8,D}
4   R!H u0 {2,D} {7,S}
5   R!H u0 {1,S} {9,D}
6   R!H u0 {1,D} {7,S}
7   R!H u0 {4,S} {6,S}
8   R!H u0 {3,D} {9,S}
9   R!H u0 {5,D} {8,S}
""",
	solute = SoluteData(
		S = 0.04788,
		B = 0.02431,
		E = 0.06783,
		L = 0.08692,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 3,
		L = 3,
		A = 3,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 196,
	label = "s2_5_6_ben",
	group = 
"""
1 * R!H u0 {2,B} {3,S} {5,B}
2   R!H u0 {1,B} {4,S} {6,B}
3   R!H u0 {1,S} {7,S}
4   R!H u0 {2,S} {7,S}
5   R!H u0 {1,B} {9,B}
6   R!H u0 {2,B} {8,B}
7   R!H u0 {3,S} {4,S}
8   R!H u0 {6,B} {9,B}
9   R!H u0 {5,B} {8,B}
""",
	solute = SoluteData(
		S = 0.05553,
		B = 0.11066,
		E = 0.01860,
		L = -0.15571,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 9,
		B = 9,
		E = 9,
		L = 8,
		A = 9,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 197,
	label = "s2_5_6_ben_onlyC",
	group = 
"""
1 * C u0 {2,B} {3,S} {5,B}
2   C u0 {1,B} {4,S} {6,B}
3   C u0 {1,S} {7,S}
4   C u0 {2,S} {7,S}
5   C u0 {1,B} {9,B}
6   C u0 {2,B} {8,B}
7   C u0 {3,S} {4,S}
8   C u0 {6,B} {9,B}
9   C u0 {5,B} {8,B}
""",
	solute = SoluteData(
		S = -0.00818,
		B = -0.01021,
		E = 0.00879,
		L = 0.00438,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 26,
		B = 22,
		E = 30,
		L = 29,
		A = 29,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 198,
	label = "s2_5_6_phthalan",
	group = 
"""
1 * C u0 {2,B} {3,S} {5,B}
2   C u0 {1,B} {4,S} {6,B}
3   C u0 {1,S} {7,S}
4   C u0 {2,S} {7,S}
5   C u0 {1,B} {9,B}
6   C u0 {2,B} {8,B}
7   O u0 {3,S} {4,S}
8   C u0 {6,B} {9,B}
9   C u0 {5,B} {8,B}
""",
	solute = SoluteData(
		S = 0.15106,
		B = -0.03653,
		E = 0.07424,
		L = 0.18762,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 5,
		E = 5,
		L = 5,
		A = 5,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 199,
	label = "s2_5_6_2,3-dihydrobenzofuran",
	group = 
"""
1 * C u0 {2,B} {3,S} {5,B}
2   C u0 {1,B} {4,S} {6,B}
3   O u0 {1,S} {7,S}
4   C u0 {2,S} {7,S}
5   C u0 {1,B} {9,B}
6   C u0 {2,B} {8,B}
7   C u0 {3,S} {4,S}
8   C u0 {6,B} {9,B}
9   C u0 {5,B} {8,B}
""",
	solute = SoluteData(
		S = -0.12431,
		B = 0.05867,
		E = -0.07069,
		L = -0.27658,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 9,
		B = 9,
		E = 9,
		L = 8,
		A = 9,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 200,
	label = "s2_5_6_indoline",
	group = 
"""
1 * C u0 {2,B} {3,S} {5,B}
2   C u0 {1,B} {4,S} {6,B}
3   N u0 {1,S} {7,S}
4   C u0 {2,S} {7,S}
5   C u0 {1,B} {9,B}
6   C u0 {2,B} {8,B}
7   C u0 {3,S} {4,S}
8   C u0 {6,B} {9,B}
9   C u0 {5,B} {8,B}
""",
	solute = SoluteData(
		S = 0.02074,
		B = 0.06276,
		E = -0.03188,
		L = 0.20864,
		A = -0.01765,
	),
	dataCount = DataCountGAV(
		S = 6,
		B = 4,
		E = 10,
		L = 10,
		A = 6,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 201,
	label = "s2_5_6_isatin",
	group = 
"""
1 * C u0 {2,B} {3,S} {5,B}
2   C u0 {1,B} {4,S} {6,B}
3   N u0 {1,S} {7,S}
4   CO u0 {2,S} {7,S}
5   C u0 {1,B} {9,B}
6   C u0 {2,B} {8,B}
7   CO u0 {3,S} {4,S}
8   C u0 {6,B} {9,B}
9   C u0 {5,B} {8,B}
""",
	solute = SoluteData(
		S = 0.04765,
		B = -0.04551,
		E = -0.07313,
		L = -0.10695,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
		E = 2,
		L = 2,
		A = 2,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 202,
	label = "s2_5_6_oxindole",
	group = 
"""
1 * C u0 {2,B} {3,S} {5,B}
2   C u0 {1,B} {4,S} {6,B}
3   N u0 {1,S} {7,S}
4   C u0 {2,S} {7,S}
5   C u0 {1,B} {9,B}
6   C u0 {2,B} {8,B}
7   CO u0 {3,S} {4,S}
8   C u0 {6,B} {9,B}
9   C u0 {5,B} {8,B}
""",
	solute = SoluteData(
		S = 0.17678,
		B = 0.01136,
		E = 0.00837,
		L = 0.21558,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 6,
		B = 6,
		E = 6,
		L = 6,
		A = 6,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 203,
	label = "s2_5_6_isoindoline",
	group = 
"""
1 * C u0 {2,B} {3,S} {5,B}
2   C u0 {1,B} {4,S} {6,B}
3   C u0 {1,S} {7,S}
4   C u0 {2,S} {7,S}
5   C u0 {1,B} {9,B}
6   C u0 {2,B} {8,B}
7   N u0 {3,S} {4,S}
8   C u0 {6,B} {9,B}
9   C u0 {5,B} {8,B}
""",
	solute = SoluteData(
		S = 0.13789,
		B = -0.07897,
		E = -0.04305,
		L = -0.07442,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 4,
		L = 4,
		A = 3,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 204,
	label = "s2_5_6_isoindole-1,3-dione",
	group = 
"""
1 * C  u0 {2,B} {3,S} {5,B}
2   C  u0 {1,B} {4,S} {6,B}
3   CO u0 {1,S} {7,S}
4   CO u0 {2,S} {7,S}
5   C  u0 {1,B} {9,B}
6   C  u0 {2,B} {8,B}
7   N  u0 {3,S} {4,S}
8   C  u0 {6,B} {9,B}
9   C  u0 {5,B} {8,B}
""",
	solute = SoluteData(
		S = 0.01774,
		B = -0.30115,
		E = -0.17385,
		L = -0.75088,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 10,
		B = 10,
		E = 10,
		L = 10,
		A = 10,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 205,
	label = "s2_5_6_1,3-benzodioxole",
	group = 
"""
1 * C u0 {2,B} {3,S} {5,B}
2   C u0 {1,B} {4,S} {6,B}
3   O u0 {1,S} {7,S}
4   O u0 {2,S} {7,S}
5   C u0 {1,B} {9,B}
6   C u0 {2,B} {8,B}
7   C u0 {3,S} {4,S}
8   C u0 {6,B} {9,B}
9   C u0 {5,B} {8,B}
""",
	solute = SoluteData(
		S = 0.00001,
		B = -0.04312,
		E = -0.04733,
		L = -0.12137,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 12,
		B = 12,
		E = 12,
		L = 12,
		A = 12,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 206,
	label = "s2_5_6_2,3-dihydrobenzothiophene",
	group = 
"""
1 * C u0 {2,B} {3,S} {5,B}
2   C u0 {1,B} {4,S} {6,B}
3   S u0 {1,S} {7,S}
4   C u0 {2,S} {7,S}
5   C u0 {1,B} {9,B}
6   C u0 {2,B} {8,B}
7   C u0 {3,S} {4,S}
8   C u0 {6,B} {9,B}
9   C u0 {5,B} {8,B}
""",
	solute = SoluteData(
		S = 0.00187,
		B = -0.00339,
		E = -0.02439,
		L = 0.06063,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 4,
		B = 4,
		E = 4,
		L = 4,
		A = 4,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 207,
	label = "s2_5_6_heteroaromatic_general",
	group =  "OR{s2_5_6_purine_general, s2_5_6_heteroaromatic1, s2_5_6_heteroaromatic2, s2_5_6_heteroaromatic3}",
	solute = u's2_5_6_purine_general',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 208,
	label = "s2_5_6_heteroaromatic1",
	group = 
"""
1  [C,N,S] u0 {5,S} {9,S}
2  [C,N,S] u0 {4,S} {7,S}
3  [C,N,S] u0 {7,S} {9,D}
4  [C,N,S] u0 {2,S} {8,D}
5  [C,N,S] u0 {1,S} {6,S}
6  [C,N,S] u0 {5,S} {7,D} {8,S}
7  [C,N,S] u0 {2,S} {3,S} {6,D}
8  [C,N,S] u0 {4,D} {6,S}
9  [C,N,S] u0 {1,S} {3,D}
""",
	solute = u's2_5_6_heteroaromatic',
	dataCount = None,
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
this is one of the groups that belong to s2_5_6_heteroaromatic
""",
)

entry(
	index = 209,
	label = "s2_5_6_heteroaromatic2",
	group = 
"""
1  [C,N,S] u0 {5,S} {9,D}
2  [C,N,S] u0 {4,D} {7,S}
3  [C,N,S] u0 {7,D} {9,S}
4  [C,N,S] u0 {2,D} {8,S}
5  [C,N,S] u0 {1,S} {6,D}
6  [C,N,S] u0 {5,D} {7,S} {8,S}
7  [C,N,S] u0 {2,S} {3,D} {6,S}
8  [C,N,S] u0 {4,S} {6,S}
9  [C,N,S] u0 {1,D} {3,S}
""",
	solute = u's2_5_6_heteroaromatic',
	dataCount = None,
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
this is one of the groups that belong to s2_5_6_heteroaromatic
""",
)

entry(
	index = 210,
	label = "s2_5_6_heteroaromatic3",
	group = 
"""
1  [C,N,S] u0 {4,S} {7,S}
2  [C,N,S] u0 {4,S} {9,D}
3  [C,N,S] u0 {4,D} {5,S} {6,S}
4  * [C,N,S] u0 {1,S} {2,S} {3,D}
5  [C,N,S] u0 {3,S} {8,D}
6  [C,N,S] u0 {3,S} {7,D}
7  [C,N,S] u0 {1,S} {6,D}
8  [C,N,S] u0 {5,D} {9,S}
9  [C,N,S] u0 {2,D} {8,S}
""",
	solute = u's2_5_6_heteroaromatic',
	dataCount = None,
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
this is one of the groups that belong to s2_5_6_heteroaromatic
""",
)

entry(
	index = 211,
	label = "s2_5_6_purine_general",
	group =  "OR{s2_5_6_purine1, s2_5_6_purine2, s2_5_6_purine3, s2_5_6_purine4, s2_5_6_purine5, s2_5_6_purine6, \
s2_5_6_purine7, s2_5_6_purine8, s2_5_6_hypoxanthine_general}",
	solute = u's2_5_6_purine',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 212,
	label = "s2_5_6_purine1",
	group = 
"""
1 * C u0 {2,S} {3,S} {5,D}
2   C u0 {1,S} {4,S} {6,D}
3   N u0 {1,S} {7,D}
4   N u0 {2,S} {7,S}
5   N u0 {1,D} {9,S}
6   C u0 {2,D} {8,S}
7   C u0 {3,D} {4,S}
8   N u0 {6,S} {9,D}
9   C u0 {5,S} {8,D}
""",
	solute = u's2_5_6_purine',
	dataCount = None,
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
this is one of the groups that belong to s2_5_6_purine
""",
)

entry(
	index = 213,
	label = "s2_5_6_purine2",
	group = 
"""
1 * C u0 {2,D} {3,S} {5,S}
2   C u0 {1,D} {4,S} {6,S}
3   N u0 {1,S} {7,D}
4   N u0 {2,S} {7,S}
5   N u0 {1,S} {9,D}
6   C u0 {2,S} {8,D}
7   C u0 {3,D} {4,S}
8   N u0 {6,D} {9,S}
9   C u0 {5,D} {8,S}
""",
	solute = u's2_5_6_purine',
	dataCount = None,
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
this is one of the groups that belong to s2_5_6_purine
""",
)

entry(
	index = 214,
	label = "s2_5_6_purine3",
	group = 
"""
1 * C u0 {2,S} {3,S} {5,D}
2   C u0 {1,S} {4,S} {6,D}
3   N u0 {1,S} {7,S}
4   N u0 {2,S} {7,D}
5   N u0 {1,D} {9,S}
6   C u0 {2,D} {8,S}
7   C u0 {3,S} {4,D}
8   N u0 {6,S} {9,D}
9   C u0 {5,S} {8,D}
""",
	solute = u's2_5_6_purine',
	dataCount = None,
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
this is one of the groups that belong to s2_5_6_purine
""",
)

entry(
	index = 215,
	label = "s2_5_6_purine4",
	group = 
"""
1  N u0 {5,S} {8,S}
2  N u0 {6,S} {8,D}
3  N u0 {6,S} {9,D}
4  N u0 {7,D} {9,S}
5  * C u0 {1,S} {6,D} {7,S}
6  C u0 {2,S} {3,S} {5,D}
7  C u0 {4,D} {5,S}
8  C u0 {1,S} {2,D}
9  C u0 {3,D} {4,S}
""",
	solute = u's2_5_6_purine',
	dataCount = None,
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
this is one of the groups that belong to s2_5_6_purine
""",
)

entry(
	index = 216,
	label = "s2_5_6_purine5",
	group = 
"""
1  N u0 {5,S} {7,S}
2  N u0 {6,S} {7,D}
3  N u0 {5,S} {9,D}
4  N u0 {8,D} {9,S}
5  * C u0 {1,S} {3,S} {6,D}
6  C u0 {2,S} {5,D} {8,S}
7  C u0 {1,S} {2,D}
8  C u0 {4,D} {6,S}
9  C u0 {3,D} {4,S}
""",
	solute = u's2_5_6_purine',
	dataCount = None,
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
this is one of the groups that belong to s2_5_6_purine
""",
)

entry(
	index = 217,
	label = "s2_5_6_purine6",
	group = 
"""
1  N u0 {7,S} {8,S}
2  N u0 {5,S} {9,D}
3  N u0 {6,S} {8,D}
4  N u0 {6,D} {9,S}
5  * C u0 {2,S} {6,S} {7,D}
6  C u0 {3,S} {4,D} {5,S}
7  C u0 {1,S} {5,D}
8  C u0 {1,S} {3,D}
9  C u0 {2,D} {4,S}
""",
	solute = u's2_5_6_purine',
	dataCount = None,
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
this is one of the groups that belong to s2_5_6_purine
""",
)

entry(
	index = 218,
	label = "s2_5_6_purine7",
	group = 
"""
1  N u0 {6,S} {9,S}
2  N u0 {7,S} {8,S}
3  N u0 {5,S} {8,D}
4  N u0 {7,S} {9,D}
5  C u0 {3,S} {6,S}
6  * C u0 {1,S} {5,S} {7,D}
7  C u0 {2,S} {4,S} {6,D}
8  C u0 {2,S} {3,D}
9  C u0 {1,S} {4,D}
""",
	solute = u's2_5_6_purine',
	dataCount = None,
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
this is one of the groups that belong to s2_5_6_purine
""",
)

entry(
	index = 219,
	label = "s2_5_6_purine8",
	group = 
"""
1  N u0 {5,S} {8,S}
2  N u0 {7,S} {9,S}
3  N u0 {6,S} {9,D}
4  N u0 {7,S} {8,D}
5  C u0 {1,S} {6,S}
6  * C u0 {3,S} {5,S} {7,D}
7  C u0 {2,S} {4,S} {6,D}
8  C u0 {1,S} {4,D}
9  C u0 {2,S} {3,D}
""",
	solute = u's2_5_6_purine',
	dataCount = None,
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
this is one of the groups that belong to s2_5_6_purine
""",
)

entry(
	index = 220,
	label = "s2_5_6_purine",
	group = 
"""
1 * R!H u0 {2,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {6,[S,D,T,B]}
3   R!H u0 {2,[S,D,T,B]} {9,[S,D,T,B]}
4   R!H u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6   R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
7   R!H u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
8   R!H u0 {4,[S,D,T,B]} {9,[S,D,T,B]}
9   R!H u0 {3,[S,D,T,B]} {8,[S,D,T,B]}
""",
	solute = SoluteData(
		S = 0.22179,
		B = -0.04470,
		E = 0.19292,
		L = 0.59304,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 27,
		B = 25,
		E = 27,
		L = 25,
		A = 27,
	),
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
dummy group to put all s2_5_6_purine groups (s2_5_6_purine1-8) together
""",
)

entry(
	index = 221,
	label = "s2_5_6_hypoxanthine_general",
	group =  "OR{s2_5_6_hypoxanthine1, s2_5_6_hypoxanthine2}",
	solute = u's2_5_6_hypoxanthine',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 222,
	label = "s2_5_6_hypoxanthine1",
	group = 
"""
1  N  u0 {6,S} {9,S}
2  N  u0 {7,S} {8,S}
3  N  u0 {5,S} {8,D}
4  N  u0 {7,S} {9,D}
5  CO u0 {3,S} {6,S}
6  * C u0 {1,S} {5,S} {7,D}
7  C  u0 {2,S} {4,S} {6,D}
8  C  u0 {2,S} {3,D}
9  C  u0 {1,S} {4,D}
""",
	solute = u's2_5_6_hypoxanthine',
	dataCount = None,
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
this is one of the groups that belong to s2_5_6_hypoxanthine
""",
)

entry(
	index = 223,
	label = "s2_5_6_hypoxanthine2",
	group = 
"""
1  N u0 {5,S} {8,S}
2  N u0 {7,S} {9,S}
3  N u0 {6,S} {9,D}
4  N u0 {7,S} {8,D}
5  CO u0 {1,S} {6,S}
6  * C u0 {3,S} {5,S} {7,D}
7  C u0 {2,S} {4,S} {6,D}
8  C u0 {1,S} {4,D}
9  C u0 {2,S} {3,D}
""",
	solute = u's2_5_6_hypoxanthine',
	dataCount = None,
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
this is one of the groups that belong to s2_5_6_hypoxanthine
""",
)

entry(
	index = 224,
	label = "s2_5_6_hypoxanthine",
	group = 
"""
1 * R!H u0 {2,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {6,[S,D,T,B]}
3   R!H u0 {2,[S,D,T,B]} {9,[S,D,T,B]}
4   R!H u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6   R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
7   R!H u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
8   R!H u0 {4,[S,D,T,B]} {9,[S,D,T,B]}
9   R!H u0 {3,[S,D,T,B]} {8,[S,D,T,B]}
""",
	solute = SoluteData(
		S = -0.05496,
		B = 0.02645,
		E = 0.07175,
		L = 0.02655,
		A = 0.08134,
	),
	dataCount = DataCountGAV(
		S = 7,
		B = 7,
		E = 7,
		L = 7,
		A = 7,
	),
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
dummy group to put all s2_5_6_hypoxanthine groups (s2_5_6_hypoxanthine1-2) together
""",
)

entry(
	index = 225,
	label = "s2_5_6_heteroaromatic",
	group = 
"""
1 * R!H u0 {2,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {6,[S,D,T,B]}
3   R!H u0 {2,[S,D,T,B]} {9,[S,D,T,B]}
4   R!H u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6   R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
7   R!H u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
8   R!H u0 {4,[S,D,T,B]} {9,[S,D,T,B]}
9   R!H u0 {3,[S,D,T,B]} {8,[S,D,T,B]}
""",
	solute = SoluteData(
		S = 0.01345,
		B = -0.00024,
		E = 0.14259,
		L = 0.24269,
		A = 0.06991,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 5,
		E = 6,
		L = 4,
		A = 5,
	),
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
dummy group to put all s2_5_6_heteroaromatic groups (s2_5_6_heteroaromatic1-3) together
""",
)

entry(
	index = 226,
	label = "s2_5_6_indene_general",
	group = 
"""
1 * R!H u0 {2,B} {3,S} {4,B}
2   R!H u0 {1,B} {5,S} {6,B}
3   R!H u0 {1,S} {7,S}
4   R!H u0 {1,B} {8,B}
5   R!H u0 {2,S} {7,D}
6   R!H u0 {2,B} {9,B}
7   R!H u0 {3,S} {5,D}
8   R!H u0 {4,B} {9,B}
9   R!H u0 {6,B} {8,B}
""",
	solute = u's2_5_6_indene',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 227,
	label = "s2_5_6_indene",
	group = 
"""
1 * Cb  u0 {2,B} {3,S} {4,B}
2   Cb  u0 {1,B} {5,S} {6,B}
3   C    u0 {1,S} {7,S}
4   Cb  u0 {1,B} {8,B}
5   C   u0 {2,S} {7,D}
6   Cb  u0 {2,B} {9,B}
7   C   u0 {3,S} {5,D}
8   C   u0 {4,B} {9,B}
9   C   u0 {6,B} {8,B}
""",
	solute = SoluteData(
		S = 0.03757,
		B = -0.01964,
		E = -0.01333,
		L = -0.24232,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 9,
		B = 9,
		E = 10,
		L = 10,
		A = 10,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 228,
	label = "s2_5_6_indole",
	group = 
"""
1 * Cb  u0 {2,B} {3,S} {4,B}
2   Cb  u0 {1,B} {5,S} {6,B}
3   N   u0 {1,S} {7,S}
4   Cb  u0 {1,B} {8,B}
5   C   u0 {2,S} {7,D}
6   Cb  u0 {2,B} {9,B}
7   C   u0 {3,S} {5,D}
8   Cb  u0 {4,B} {9,B}
9   Cb  u0 {6,B} {8,B}
""",
	solute = SoluteData(
		S = -0.05644,
		B = -0.06163,
		E = 0.00162,
		L = -0.05036,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 42,
		B = 34,
		E = 44,
		L = 42,
		A = 42,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 229,
	label = "s2_5_6_benzimidazole",
	group = 
"""
1 * Cb  u0 {2,B} {3,S} {4,B}
2   Cb  u0 {1,B} {5,S} {6,B}
3   N   u0 {1,S} {7,S}
4   Cb  u0 {1,B} {8,B}
5   N   u0 {2,S} {7,D}
6   Cb  u0 {2,B} {9,B}
7   C   u0 {3,S} {5,D}
8   Cb  u0 {4,B} {9,B}
9   Cb  u0 {6,B} {8,B}
""",
	solute = SoluteData(
		S = 0.09078,
		B = 0.07990,
		E = -0.03745,
		L = 0.24075,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 27,
		B = 27,
		E = 27,
		L = 25,
		A = 27,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 230,
	label = "s2_5_6_indazole",
	group = 
"""
1 * Cb  u0 {2,B} {3,S} {4,B}
2   Cb  u0 {1,B} {5,S} {6,B}
3   N   u0 {1,S} {7,S}
4   Cb  u0 {1,B} {8,B}
5   C   u0 {2,S} {7,D}
6   Cb  u0 {2,B} {9,B}
7   N   u0 {3,S} {5,D}
8   Cb  u0 {4,B} {9,B}
9   Cb  u0 {6,B} {8,B}
""",
	solute = SoluteData(
		S = 0.06449,
		B = -0.02986,
		E = 0.10654,
		L = 0.12670,
		A = 0.03879,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
		E = 2,
		L = 2,
		A = 2,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 231,
	label = "s2_5_6_benzofuran",
	group = 
"""
1 * Cb  u0 {2,B} {3,S} {4,B}
2   Cb  u0 {1,B} {5,S} {6,B}
3   O   u0 {1,S} {7,S}
4   Cb  u0 {1,B} {8,B}
5   C   u0 {2,S} {7,D}
6   Cb  u0 {2,B} {9,B}
7   C   u0 {3,S} {5,D}
8   Cb  u0 {4,B} {9,B}
9   Cb  u0 {6,B} {8,B}
""",
	solute = SoluteData(
		S = 0.07506,
		B = -0.04433,
		E = 0.00880,
		L = 0.06866,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 7,
		B = 7,
		E = 7,
		L = 6,
		A = 7,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 232,
	label = "s2_5_6_benzothiophene",
	group = 
"""
1 * Cb  u0 {2,B} {3,S} {4,B}
2   Cb  u0 {1,B} {5,S} {6,B}
3   S   u0 {1,S} {7,S}
4   Cb  u0 {1,B} {8,B}
5   C   u0 {2,S} {7,D}
6   Cb  u0 {2,B} {9,B}
7   C   u0 {3,S} {5,D}
8   Cb  u0 {4,B} {9,B}
9   Cb  u0 {6,B} {8,B}
""",
	solute = SoluteData(
		S = 0.01941,
		B = -0.01943,
		E = 0.03815,
		L = 0.17716,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 26,
		B = 26,
		E = 27,
		L = 27,
		A = 27,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 233,
	label = "s2_5_6_benzoxazole",
	group = 
"""
1 * Cb  u0 {2,B} {3,S} {4,B}
2   Cb  u0 {1,B} {5,S} {6,B}
3   O   u0 {1,S} {7,S}
4   Cb  u0 {1,B} {8,B}
5   N   u0 {2,S} {7,D}
6   Cb  u0 {2,B} {9,B}
7   C   u0 {3,S} {5,D}
8   Cb  u0 {4,B} {9,B}
9   Cb  u0 {6,B} {8,B}
""",
	solute = SoluteData(
		S = 0.07845,
		B = -0.02596,
		E = 0.02581,
		L = 0.12560,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 4,
		B = 4,
		E = 4,
		L = 3,
		A = 4,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 234,
	label = "s2_5_6_benzisoxazole",
	group = 
"""
1 * Cb  u0 {2,B} {3,S} {4,B}
2   Cb  u0 {1,B} {5,S} {6,B}
3   O   u0 {1,S} {7,S}
4   Cb  u0 {1,B} {8,B}
5   C   u0 {2,S} {7,D}
6   Cb  u0 {2,B} {9,B}
7   N   u0 {3,S} {5,D}
8   Cb  u0 {4,B} {9,B}
9   Cb  u0 {6,B} {8,B}
""",
	solute = SoluteData(
		S = 0.09013,
		B = 0.02305,
		E = 0.00484,
		L = 0.23195,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 4,
		B = 4,
		E = 4,
		L = 4,
		A = 4,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 235,
	label = "s2_5_6_benzothiazole",
	group = 
"""
1 * Cb  u0 {2,B} {3,S} {4,B}
2   Cb  u0 {1,B} {5,S} {6,B}
3   S   u0 {1,S} {7,S}
4   Cb  u0 {1,B} {8,B}
5   N   u0 {2,S} {7,D}
6   Cb  u0 {2,B} {9,B}
7   C   u0 {3,S} {5,D}
8   Cb  u0 {4,B} {9,B}
9   Cb  u0 {6,B} {8,B}
""",
	solute = SoluteData(
		S = 0.08575,
		B = -0.01901,
		E = 0.03474,
		L = 0.35652,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 5,
		E = 6,
		L = 5,
		A = 6,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 236,
	label = "s2_5_6_benzotriazole",
	group = 
"""
1 * Cb  u0 {2,B} {3,S} {4,B}
2   Cb  u0 {1,B} {5,S} {6,B}
3   N   u0 {1,S} {7,S}
4   Cb  u0 {1,B} {8,B}
5   N   u0 {2,S} {7,D}
6   Cb  u0 {2,B} {9,B}
7   N   u0 {3,S} {5,D}
8   Cb  u0 {4,B} {9,B}
9   Cb  u0 {6,B} {8,B}
""",
	solute = SoluteData(
		S = 0.12936,
		B = 0.03289,
		E = 0.13340,
		L = 0.28689,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
		E = 2,
		L = 2,
		A = 2,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 237,
	label = "s2_5_7",
	group = 
"""
1  * R!H u0 {2,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2    R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {6,[S,D,T,B]}
3    R!H u0 {2,[S,D,T,B]} {9,[S,D,T,B]}
4    R!H u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
5    R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6    R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
8    R!H u0 {4,[S,D,T,B]} {10,[S,D,T,B]}
9    R!H u0 {3,[S,D,T,B]} {10,[S,D,T,B]}
10   R!H u0 {8,[S,D,T,B]} {9,[S,D,T,B]}
""",
	solute = SoluteData(
		S = 0.01109,
		B = 0.05613,
		E = 0.08479,
		L = 0.08047,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 16,
		B = 16,
		E = 16,
		L = 14,
		A = 16,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 238,
	label = "s2_5_7_azulene",
	group = 
"""
1  * C u0 {2,S} {3,D} {4,S}
2  C u0 {1,S} {5,D} {6,S}
3  C u0 {1,D} {8,S}
4  C u0 {1,S} {9,D}
5  C u0 {2,D} {9,S}
6  C u0 {2,S} {10,D} 
7  C u0 {8,D} {10,S}
8  C u0 {3,S} {7,D}
9  C u0 {4,D} {5,S}
10 C u0 {6,D} {7,S}
""",
	solute = SoluteData(
		S = 0.00554,
		B = -0.06118,
		E = 0.02397,
		L = 0.26676,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 6,
		L = 6,
		A = 6,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 239,
	label = "s2_5_7_ene_1",
	group = 
"""
1  * C u0 {2,D} {4,S} {5,S}
2    C u0 {1,D} {3,S} {6,S}
3    C u0 {2,S} {9,S}
4    C u0 {1,S} {8,S}
5    C u0 {1,S} {7,S}
6    C u0 {2,S} {7,S}
7    C u0 {5,S} {6,S}
8    C u0 {4,S} {10,S}
9    C u0 {3,S} {10,S}
10   C u0 {8,S} {9,S}
""",
	solute = SoluteData(
		S = -0.06294,
		B = -0.09034,
		E = -0.03948,
		L = -0.39742,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 3,
		L = 3,
		A = 3,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 240,
	label = "s2_5_7_ene_2",
	group = 
"""
1  * C u0 {2,S} {4,D} {5,S}
2    C u0 {1,S} {3,S} {6,S}
3    C u0 {2,S} {9,S}
4    C u0 {1,D} {8,S}
5    C u0 {1,S} {7,S}
6    C u0 {2,S} {7,S}
7    C u0 {5,S} {6,S}
8    C u0 {4,S} {10,S}
9    C u0 {3,S} {10,S}
10   C u0 {8,S} {9,S}
""",
	solute = SoluteData(
		S = -0.04974,
		B = -0.04786,
		E = -0.01945,
		L = -0.09382,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
		E = 2,
		L = 2,
		A = 2,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 241,
	label = "s2_6_6",
	group = 
"""
1    R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {6,[S,D,T,B]}
2    R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3    R!H u0 {1,[S,D,T,B]} {9,[S,D,T,B]}
4    R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
5    R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
6    R!H u0 {1,[S,D,T,B]} {10,[S,D,T,B]}
7  * R!H u0 {4,[S,D,T,B]} {9,[S,D,T,B]}
8    R!H u0 {5,[S,D,T,B]} {10,[S,D,T,B]}
9    R!H u0 {3,[S,D,T,B]} {7,[S,D,T,B]}
10   R!H u0 {6,[S,D,T,B]} {8,[S,D,T,B]}
""",
	solute = SoluteData(
		S = -0.16867,
		B = 0.13981,
		E = -0.05694,
		L = -0.42139,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 4,
		B = 4,
		E = 4,
		L = 4,
		A = 4,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 242,
	label = "s2_6_6_ane",
	group = 
"""
1    R!H u0 {2,S} {3,S} {6,S}
2    R!H u0 {1,S} {4,S} {5,S}
3    R!H u0 {1,S} {9,S}
4    R!H u0 {2,S} {7,S}
5    R!H u0 {2,S} {8,S}
6    R!H u0 {1,S} {10,S}
7  * R!H u0 {4,S} {9,S}
8    R!H u0 {5,S} {10,S}
9    R!H u0 {3,S} {7,S}
10   R!H u0 {6,S} {8,S}
""",
	solute = SoluteData(
		S = -0.04038,
		B = 0.00000,
		E = -0.04689,
		L = -0.13896,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 18,
		B = 18,
		E = 22,
		L = 12,
		A = 22,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 243,
	label = "s2_6_6_ene",
	group =  "OR{s2_6_6_ene_0, s2_6_6_ene_1, s2_6_6_ene_2, s2_6_6_ene_m}",
	solute = u's2_6_6_ene_1',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 244,
	label = "s2_6_6_ene_0",
	group = 
"""
1    R!H u0 {2,S} {3,S} {5,S}
2    R!H u0 {1,S} {4,D} {6,S}
3    R!H u0 {1,S} {7,S}
4    R!H u0 {2,D} {8,S}
5    R!H u0 {1,S} {10,S}
6    R!H u0 {2,S} {9,S}
7  * R!H u0 {3,S} {8,S}
8    R!H u0 {4,S} {7,S}
9    R!H u0 {6,S} {10,S}
10   R!H u0 {5,S} {9,S}
""",
	solute = SoluteData(
		S = -0.09435,
		B = -0.00904,
		E = 0.03891,
		L = -0.04303,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 6,
		B = 6,
		E = 7,
		L = 5,
		A = 7,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 245,
	label = "s2_6_6_ene_1",
	group = 
"""
1    R!H u0 {2,S} {3,S} {5,S}
2    R!H u0 {1,S} {4,S} {6,S}
3    R!H u0 {1,S} {9,D}
4    R!H u0 {2,S} {7,S}
5    R!H u0 {1,S} {10,S}
6    R!H u0 {2,S} {8,S}
7  * R!H u0 {4,S} {10,S}
8    R!H u0 {6,S} {9,S}
9    R!H u0 {3,D} {8,S}
10   R!H u0 {5,S} {7,S}
""",
	solute = SoluteData(
		S = -0.00903,
		B = 0.02653,
		E = 0.04275,
		L = 0.10620,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 14,
		B = 14,
		E = 14,
		L = 13,
		A = 14,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 246,
	label = "s2_6_6_ene_2",
	group = 
"""
1    R!H u0 {2,S} {3,S} {4,S}
2    R!H u0 {1,S} {5,S} {6,S}
3    R!H u0 {1,S} {10,S}
4    R!H u0 {1,S} {7,S}
5    R!H u0 {2,S} {8,S}
6    R!H u0 {2,S} {9,S}
7  * R!H u0 {4,S} {8,S}
8    R!H u0 {5,S} {7,S}
9    R!H u0 {6,S} {10,D}
10   R!H u0 {3,S} {9,D}
""",
	solute = SoluteData(
		S = -0.01391,
		B = 0.00500,
		E = 0.25196,
		L = -0.00083,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 3,
		L = 2,
		A = 3,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 247,
	label = "s2_6_6_ene_m",
	group = 
"""
1    R!H u0 {2,D} {5,S} {6,S}
2    R!H u0 {1,D} {3,S} {4,S}
3    R!H u0 {2,S} {7,S}
4    R!H u0 {2,S} {8,S}
5    R!H u0 {1,S} {10,S}
6    R!H u0 {1,S} {9,S}
7  * R!H u0 {3,S} {9,S}
8    R!H u0 {4,S} {10,S}
9    R!H u0 {6,S} {7,S}
10   R!H u0 {5,S} {8,S}
""",
	solute = u's2_6_6_ene_0',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 248,
	label = "s2_6_6_diene",
	group =  "OR{s2_6_6_diene_0_2, s2_6_6_diene_0_3, s2_6_6_diene_0_6, s2_6_6_diene_0_8, s2_6_6_diene_1_6, s2_6_6_diene_1_7}",
	solute = u's2_6_6_diene_0_8',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 249,
	label = "s2_6_6_diene_0_2",
	group = 
"""
1    R!H u0 {2,S} {3,S} {5,S}
2    R!H u0 {1,S} {4,S} {6,D}
3    R!H u0 {1,S} {8,S}
4    R!H u0 {2,S} {10,S}
5    R!H u0 {1,S} {9,S}
6    R!H u0 {2,D} {7,S}
7  * R!H u0 {6,S} {8,D}
8    R!H u0 {3,S} {7,D}
9    R!H u0 {5,S} {10,S}
10   R!H u0 {4,S} {9,S}
""",
	solute = SoluteData(
		S = 0.06559,
		B = 0.08608,
		E = 0.03331,
		L = 0.22695,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 3,
		L = 3,
		A = 3,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 250,
	label = "s2_6_6_diene_0_3",
	group = 
"""
1    R!H u0 {2,S} {4,S} {6,D}
2    R!H u0 {1,S} {3,S} {5,S}
3    R!H u0 {2,S} {10,S}
4    R!H u0 {1,S} {9,S}
5    R!H u0 {2,S} {7,D}
6    R!H u0 {1,D} {8,S}
7  * R!H u0 {5,D} {8,S}
8    R!H u0 {6,S} {7,S}
9    R!H u0 {4,S} {10,S}
10   R!H u0 {3,S} {9,S}
""",
	solute = SoluteData(
		S = -0.01643,
		B = 0.03143,
		E = 0.05837,
		L = 0.10156,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
		E = 2,
		L = 1,
		A = 2,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 251,
	label = "s2_6_6_diene_0_6",
	group = 
"""
1    R!H u0 {2,S} {5,S} {6,D}
2    R!H u0 {1,S} {3,S} {4,S}
3    R!H u0 {2,S} {10,S}
4    R!H u0 {2,S} {9,D}
5    R!H u0 {1,S} {8,S}
6    R!H u0 {1,D} {7,S}
7  * R!H u0 {6,S} {10,S}
8    R!H u0 {5,S} {9,S}
9    R!H u0 {4,D} {8,S}
10   R!H u0 {3,S} {7,S}
""",
	solute = SoluteData(
		S = -0.00420,
		B = 0.01231,
		E = 0.04223,
		L = 0.04220,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 1,
		B = 1,
		E = 1,
		L = 1,
		A = 1,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 252,
	label = "s2_6_6_diene_0_8",
	group = 
"""
1    R!H u0 {2,S} {4,S} {6,D}
2    R!H u0 {1,S} {3,S} {5,S}
3    R!H u0 {2,S} {9,S}
4    R!H u0 {1,S} {10,D}
5    R!H u0 {2,S} {8,S}
6    R!H u0 {1,D} {7,S}
7  * R!H u0 {6,S} {8,S}
8    R!H u0 {5,S} {7,S}
9    R!H u0 {3,S} {10,S}
10   R!H u0 {4,D} {9,S}
""",
	solute = SoluteData(
		S = 0.13668,
		B = 0.02840,
		E = 0.13603,
		L = 0.37567,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 7,
		B = 7,
		E = 7,
		L = 6,
		A = 7,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 253,
	label = "s2_6_6_diene_1_6",
	group = 
"""
1    R!H u0 {2,S} {5,S} {6,S}
2    R!H u0 {1,S} {3,S} {4,S}
3    R!H u0 {2,S} {10,S}
4    R!H u0 {2,S} {8,D}
5    R!H u0 {1,S} {9,S}
6    R!H u0 {1,S} {7,D}
7  * R!H u0 {6,D} {10,S}
8    R!H u0 {4,D} {9,S}
9    R!H u0 {5,S} {8,S}
10   R!H u0 {3,S} {7,S}
""",
	solute = SoluteData(
		S = -0.03418,
		B = -0.03389,
		E = 0.02793,
		L = 0.04067,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 3,
		L = 3,
		A = 3,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 254,
	label = "s2_6_6_diene_1_7",
	group = 
"""
1    R!H u0 {2,S} {4,S} {6,S}
2    R!H u0 {1,S} {3,S} {5,S}
3    R!H u0 {2,S} {10,S}
4    R!H u0 {1,S} {7,S}
5    R!H u0 {2,S} {8,D}
6    R!H u0 {1,S} {9,S}
7  * R!H u0 {4,S} {10,D}
8    R!H u0 {5,D} {9,S}
9    R!H u0 {6,S} {8,S}
10   R!H u0 {3,S} {7,D}
""",
	solute = SoluteData(
		S = 0.00753,
		B = 0.01840,
		E = 0.01157,
		L = 0.00120,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
		E = 2,
		L = 2,
		A = 2,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 255,
	label = "s2_6_6_tetraene",
	group =  "OR{s2_6_6_tetraene_0_2_4_7, s2_6_6_tetraene_0_2_6_8}",
	solute = u's2_6_6_tetraene_0_2_6_8',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 256,
	label = "s2_6_6_tetraene_0_2_4_7",
	group = 
"""
1    R!H u0 {2,S} {3,S} {4,D}
2    R!H u0 {1,S} {5,D} {6,S}
3    R!H u0 {1,S} {8,S}
4    R!H u0 {1,D} {7,S}
5    R!H u0 {2,D} {10,S}
6    R!H u0 {2,S} {9,S}
7  * R!H u0 {4,S} {10,D}
8    R!H u0 {3,S} {9,D}
9    R!H u0 {6,S} {8,D}
10   R!H u0 {5,S} {7,D}
""",
	solute = SoluteData(
		S = -0.05566,
		B = 0.05940,
		E = -0.03677,
		L = -0.16307,
		A = 0.04066,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
		E = 2,
		L = 2,
		A = 2,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 257,
	label = "s2_6_6_tetraene_0_2_6_8",
	group = 
"""
1    R!H u0 {2,S} {3,S} {6,S}
2    R!H u0 {1,S} {4,D} {5,S}
3    R!H u0 {1,S} {8,D}
4    R!H u0 {2,D} {7,S}
5    R!H u0 {2,S} {10,D}
6    R!H u0 {1,S} {9,S}
7  * R!H u0 {4,S} {9,D}
8    R!H u0 {3,D} {10,S}
9    R!H u0 {6,S} {7,D}
10   R!H u0 {5,D} {8,S}
""",
	solute = SoluteData(
		S = -0.03623,
		B = 0.02064,
		E = 0.02425,
		L = -0.09794,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 1,
		B = 1,
		E = 1,
		L = 1,
		A = 1,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 258,
	label = "s2_6_6_ben",
	group = 
"""
1    R!H u0 {2,B} {3,B} {5,S}
2    R!H u0 {1,B} {4,B} {6,S}
3    R!H u0 {1,B} {7,B}
4    R!H u0 {2,B} {9,B}
5    R!H u0 {1,S} {10,S}
6    R!H u0 {2,S} {8,S}
7  * R!H u0 {3,B} {9,B}
8    R!H u0 {6,S} {10,S}
9    R!H u0 {4,B} {7,B}
10   R!H u0 {5,S} {8,S}
""",
	solute = SoluteData(
		S = 0.07905,
		B = -0.01768,
		E = 0.08820,
		L = 0.11933,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 13,
		B = 13,
		E = 14,
		L = 11,
		A = 14,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 259,
	label = "s2_6_6_ben_onlyC",
	group = 
"""
1    C u0 {2,B} {3,B} {5,S}
2    C u0 {1,B} {4,B} {6,S}
3    C u0 {1,B} {7,B}
4    C u0 {2,B} {9,B}
5    C u0 {1,S} {10,S}
6    C u0 {2,S} {8,S}
7  * C u0 {3,B} {9,B}
8    C u0 {6,S} {10,S}
9    C u0 {4,B} {7,B}
10   C u0 {5,S} {8,S}
""",
	solute = SoluteData(
		S = -0.04077,
		B = 0.00568,
		E = -0.02663,
		L = -0.29995,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 24,
		B = 24,
		E = 25,
		L = 23,
		A = 25,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 260,
	label = "s2_6_6_ben_chromane",
	group = 
"""
1    C u0 {2,B} {3,B} {5,S}
2    C u0 {1,B} {4,B} {6,S}
3    C u0 {1,B} {7,B}
4    C u0 {2,B} {9,B}
5    C u0 {1,S} {10,S}
6    O u0 {2,S} {8,S}
7  * C u0 {3,B} {9,B}
8    C u0 {6,S} {10,S}
9    C u0 {4,B} {7,B}
10   C u0 {5,S} {8,S}
""",
	solute = SoluteData(
		S = -0.25794,
		B = 0.03181,
		E = 0.06359,
		L = -0.27370,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 11,
		B = 11,
		E = 11,
		L = 11,
		A = 11,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 261,
	label = "s2_6_6_ben_1,4-dioxane",
	group = 
"""
1    C u0 {2,B} {3,B} {5,S}
2    C u0 {1,B} {4,B} {6,S}
3    C u0 {1,B} {7,B}
4    C u0 {2,B} {9,B}
5    O u0 {1,S} {10,S}
6    O u0 {2,S} {8,S}
7  * C u0 {3,B} {9,B}
8    C u0 {6,S} {10,S}
9    C u0 {4,B} {7,B}
10   C u0 {5,S} {8,S}
""",
	solute = SoluteData(
		S = -0.02661,
		B = 0.03512,
		E = 0.00848,
		L = -0.13700,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
		E = 2,
		L = 2,
		A = 2,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 262,
	label = "s2_6_6_ben_ene",
	group =  "OR{s2_6_6_ben_ene_1, s2_6_6_ben_ene_2}",
	solute = u's2_6_6_ben_ene_1',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 263,
	label = "s2_6_6_ben_ene_1",
	group = 
"""
1    R!H u0 {2,B} {3,S} {4,B}
2    R!H u0 {1,B} {5,B} {6,S}
3    R!H u0 {1,S} {7,D}
4    R!H u0 {1,B} {8,B}
5    R!H u0 {2,B} {9,B}
6    R!H u0 {2,S} {10,S}
7  * R!H u0 {3,D} {10,S}
8    R!H u0 {4,B} {9,B}
9    R!H u0 {5,B} {8,B}
10   R!H u0 {6,S} {7,S}
""",
	solute = SoluteData(
		S = -0.09384,
		B = 0.00273,
		E = -0.12769,
		L = -0.19321,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 10,
		B = 10,
		E = 10,
		L = 8,
		A = 10,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 264,
	label = "s2_6_6_ben_ene_1_2-Benzothiazine-1,1-dioxide",
	group = 
"""
1    C    u0 {2,B} {3,S} {4,B}
2    C    u0 {1,B} {5,B} {6,S}
3    C    u0 {1,S} {7,D}
4    C    u0 {1,B} {8,B}
5    C    u0 {2,B} {9,B}
6    S6dd u0 {2,S} {10,S} {11,D} {12,D}
7  * C    u0 {3,D} {10,S}
8    C    u0 {4,B} {9,B}
9    C    u0 {5,B} {8,B}
10   N    u0 {6,S} {7,S}
11   O    u0 {6,D}
12   O    u0 {6,D}
""",
	solute = SoluteData(
		S = 0.00607,
		B = 0.02677,
		E = 0.01380,
		L = 0.09781,
		A = -0.02712,
	),
	dataCount = DataCountGAV(
		S = 4,
		B = 4,
		E = 4,
		L = 3,
		A = 4,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 265,
	label = "s2_6_6_ben_ene_1_coumarin",
	group = 
"""
1    C  u0 {2,B} {3,S} {4,B}
2    C  u0 {1,B} {5,B} {6,S}
3    C  u0 {1,S} {7,D}
4    C  u0 {1,B} {8,B}
5    C  u0 {2,B} {9,B}
6    O  u0 {2,S} {10,S}
7  * C  u0 {3,D} {10,S}
8    C  u0 {4,B} {9,B}
9    C  u0 {5,B} {8,B}
10   CO u0 {6,S} {7,S}
""",
	solute = SoluteData(
		S = -0.04893,
		B = -0.00137,
		E = -0.08314,
		L = -0.02796,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 5,
		E = 5,
		L = 5,
		A = 5,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 266,
	label = "s2_6_6_ben_ene_2",
	group = 
"""
1    R!H u0 {2,B} {4,B} {5,S}
2    R!H u0 {1,B} {3,S} {6,B}
3    R!H u0 {2,S} {8,S}
4    R!H u0 {1,B} {10,B}
5    R!H u0 {1,S} {7,S}
6    R!H u0 {2,B} {9,B}
7  * R!H u0 {5,S} {8,D}
8    R!H u0 {3,S} {7,D}
9    R!H u0 {6,B} {10,B}
10   R!H u0 {4,B} {9,B}
""",
	solute = SoluteData(
		S = -0.13822,
		B = 0.14838,
		E = 0.00490,
		L = -0.19335,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 20,
		B = 20,
		E = 22,
		L = 21,
		A = 22,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 267,
	label = "s2_6_6_chromen-4-one",
	group = 
"""
1    Cb  u0 {2,B} {4,B} {5,S}
2    Cb  u0 {1,B} {3,S} {6,B}
3    CO  u0 {2,S} {8,S}
4    Cb  u0 {1,B} {10,B}
5    O2s u0 {1,S} {7,S}
6    Cb  u0 {2,B} {9,B}
7  * Cd  u0 {5,S} {8,D}
8    Cd  u0 {3,S} {7,D}
9    Cb  u0 {6,B} {10,B}
10   Cb  u0 {4,B} {9,B}
""",
	solute = SoluteData(
		S = -0.02043,
		B = 0.08406,
		E = 0.10458,
		L = 0.47957,
		A = 0.17123,
	),
	dataCount = DataCountGAV(
		S = 86,
		B = 86,
		E = 87,
		L = 85,
		A = 86,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 268,
	label = "s2_6_6_ben_heteroaromatic_general",
	group =  "OR{s2_6_6_ben_heteroaromatic1, s2_6_6_ben_heteroaromatic2, s2_6_6_ben_heteroaromatic3, s2_6_6_ben_heteroaromatic4,\
s2_6_6_isoquinoline_general, s2_6_6_quinoline_general}",
	solute = u's2_6_6_quinoline_general',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 269,
	label = "s2_6_6_ben_heteroaromatic1",
	group = 
"""
1  * [C,N] u0 {9,D} {10,S}
2  [C,N] u0 {3,B} {5,B} {6,S}
3  [C,N] u0 {2,B} {4,B} {9,S}
4  [C,N] u0 {3,B} {8,B}
5  [C,N] u0 {2,B} {7,B}
6  [C,N] u0 {2,S} {10,D}
7  [C,N] u0 {5,B} {8,B}
8  [C,N] u0 {4,B} {7,B}
9  [C,N] u0 {1,D} {3,S}
10 [C,N] u0 {1,S} {6,D}
""",
	solute = u's2_6_6_ben_heteroaromatic',
	dataCount = None,
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
this is one of the groups that belong to s2_6_6_ben_heteroaromatic
""",
)

entry(
	index = 270,
	label = "s2_6_6_ben_heteroaromatic2",
	group = 
"""
1  [C,N] u0 {3,S} {9,D}
2  [C,N] u0 {4,S} {10,D}
3  [C,N] u0 {1,S} {4,D} {5,S}
4  [C,N] u0 {2,S} {3,D} {6,S}
5  [C,N] u0 {3,S} {7,D}
6  [C,N] u0 {4,S} {8,D}
7  [C,N] u0 {5,D} {10,S}
8  * [C,N] u0 {6,D} {9,S}
9  [C,N] u0 {1,D} {8,S}
10 [C,N] u0 {2,D} {7,S}
""",
	solute = u's2_6_6_ben_heteroaromatic',
	dataCount = None,
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
this is one of the groups that belong to s2_6_6_ben_heteroaromatic
""",
)

entry(
	index = 271,
	label = "s2_6_6_ben_heteroaromatic3",
	group = 
"""
1  [C,N] u0 p1 c0 {9,S} {10,D}
2  [C,N] u0 p0 c0 {3,S} {4,S} {6,D}
3  [C,N] u0 p0 c0 {2,S} {5,S} {9,D}
4  [C,N] u0 p0 c0 {2,S} {7,D}
5  [C,N] u0 p0 c0 {3,S} {8,D}
6  [C,N] u0 p0 c0 {2,D} {10,S}
7  [C,N] u0 p0 c0 {4,D} {8,S}
8  [C,N] u0 p0 c0 {5,D} {7,S}
9  [C,N] u0 p0 c0 {1,S} {3,D}
10 [C,N] u0 p0 c0 {1,D} {6,S}
""",
	solute = u's2_6_6_ben_heteroaromatic',
	dataCount = None,
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
this is one of the groups that belong to s2_6_6_ben_heteroaromatic
""",
)

entry(
	index = 272,
	label = "s2_6_6_ben_heteroaromatic4",
	group = 
"""
1  [C,N] u0 {5,S} {8,S}
2  [C,N] u0 {5,S} {10,D}
3  [C,N] u0 {4,S} {6,S}
4  [C,N] u0 {3,S} {5,D} {7,S}
5  [C,N] u0 {1,S} {2,S} {4,D}
6  [C,N] u0 {3,S} {8,D}
7  [C,N] u0 {4,S} {9,D}
8  [C,N] u0 {1,S} {6,D}
9  [C,N] u0 {7,D} {10,S}
10 [C,N] u0 {2,D} {9,S}
""",
	solute = u's2_6_6_ben_heteroaromatic',
	dataCount = None,
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
this is one of the groups that belong to s2_6_6_ben_heteroaromatic
""",
)

entry(
	index = 273,
	label = "s2_6_6_quinoline_general",
	group =  "OR{s2_6_6_quinoline1, s2_6_6_quinoline2, s2_6_6_8-Hydroxyquinoline_general, s2_6_6_quinoline_nitro_general}",
	solute = u's2_6_6_quinoline',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 274,
	label = "s2_6_6_quinoline1",
	group = 
"""
1    Cb  u0 {2,B} {4,B} {5,S}
2    Cb  u0 {1,B} {3,S} {6,B}
3    N   u0 {2,S} {8,D}
4    Cb  u0 {1,B} {10,B}
5    Cd  u0 {1,S} {7,D}
6    Cb  u0 {2,B} {9,B}
7  * Cd  u0 {5,D} {8,S}
8    Cd  u0 {3,D} {7,S}
9    Cb  u0 {6,B} {10,B}
10   Cb  u0 {4,B} {9,B}
""",
	solute = u's2_6_6_quinoline',
	dataCount = None,
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
this is one of the groups that belong to s2_6_6_quinoline
""",
)

entry(
	index = 275,
	label = "s2_6_6_quinoline2",
	group = 
"""
1  N u0 {3,D} {10,S}
2  C u0 {3,S} {4,D} {5,S}
3  C u0 {1,D} {2,S} {6,S}
4  C u0 {2,D} {9,S}
5  C u0 {2,S} {7,D}
6  C u0 {3,S} {8,D}
7  C u0 {5,D} {8,S}
8  C u0 {6,D} {7,S}
9  * C u0 {4,S} {10,D}
10 C u0 {1,S} {9,D}
""",
	solute = u's2_6_6_quinoline',
	dataCount = None,
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
this is one of the groups that belong to s2_6_6_quinoline
""",
)

entry(
	index = 276,
	label = "s2_6_6_8-Hydroxyquinoline_general",
	group =  "OR{s2_6_6_8-Hydroxyquinoline1, s2_6_6_8-Hydroxyquinoline2}",
	solute = u's2_6_6_8-Hydroxyquinoline',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 277,
	label = "s2_6_6_8-Hydroxyquinoline1",
	group = 
"""
1    Cb  u0 {2,B} {4,B} {5,S}
2    Cb  u0 {1,B} {3,S} {6,B}
3    N3d u0 {2,S} {8,D}
4    Cb  u0 {1,B} {10,B}
5    Cd  u0 {1,S} {7,D}
6    Cb  u0 {2,B} {9,B} {11,S}
7  * Cd  u0 {5,D} {8,S}
8    Cd  u0 {3,D} {7,S}
9    Cb  u0 {6,B} {10,B}
10   Cb  u0 {4,B} {9,B}
11   O   u0 {6,S} {12,S}
12   H   u0 {11,S}
""",
	solute = u's2_6_6_8-Hydroxyquinoline',
	dataCount = None,
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
this is one of the groups that belong to s2_6_6_8-Hydroxyquinoline
""",
)

entry(
	index = 278,
	label = "s2_6_6_8-Hydroxyquinoline2",
	group = 
"""
1  N u0 {3,D} {10,S}
2  C u0 {3,S} {4,D} {5,S}
3  C u0 {1,D} {2,S} {6,S}
4  C u0 {2,D} {9,S}
5  C u0 {2,S} {7,D}
6  C u0 {3,S} {8,D} {11,S}
7  C u0 {5,D} {8,S}
8  C u0 {6,D} {7,S}
9  * C u0 {4,S} {10,D}
10   C u0 {1,S} {9,D}
11   O   u0 {6,S} {12,S}
12   H   u0 {11,S}
""",
	solute = u's2_6_6_8-Hydroxyquinoline',
	dataCount = None,
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
this is one of the groups that belong to s2_6_6_8-Hydroxyquinoline
""",
)

entry(
	index = 279,
	label = "s2_6_6_8-Hydroxyquinoline",
	group = 
"""
1    R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {6,[S,D,T,B]}
2    R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3    R!H u0 {1,[S,D,T,B]} {9,[S,D,T,B]}
4    R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
5    R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
6    R!H u0 {1,[S,D,T,B]} {10,[S,D,T,B]}
7  * R!H u0 {4,[S,D,T,B]} {9,[S,D,T,B]}
8    R!H u0 {5,[S,D,T,B]} {10,[S,D,T,B]}
9    R!H u0 {3,[S,D,T,B]} {7,[S,D,T,B]}
10   R!H u0 {6,[S,D,T,B]} {8,[S,D,T,B]}
""",
	solute = SoluteData(
		S = -0.14265,
		B = -0.03943,
		E = -0.06617,
		L = -0.17238,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 40,
		B = 40,
		E = 40,
		L = 40,
		A = 40,
	),
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
dummy group to put all s2_6_6_8-Hydroxyquinoline groups (s2_6_6_8-Hydroxyquinoline1-2) together
""",
)

entry(
	index = 280,
	label = "s2_6_6_quinoline_nitro_general",
	group =  "OR{s2_6_6_quinoline_nitro1, s2_6_6_quinoline_nitro2}",
	solute = u's2_6_6_quinoline_nitro',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 281,
	label = "s2_6_6_quinoline_nitro1",
	group = 
"""
1    Cb  u0 {2,B} {4,B} {5,S}
2    Cb  u0 {1,B} {3,S} {6,B}
3    N5dc  u0 {2,S} {8,D}
4    Cb  u0 {1,B} {10,B}
5    Cd  u0 {1,S} {7,D}
6    Cb  u0 {2,B} {9,B}
7  * Cd  u0 {5,D} {8,S}
8    Cd  u0 {3,D} {7,S}
9    Cb  u0 {6,B} {10,B}
10   Cb  u0 {4,B} {9,B}
""",
	solute = u's2_6_6_quinoline_nitro',
	dataCount = None,
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
this is one of the groups that belong to s2_6_6_quinoline_nitro
""",
)

entry(
	index = 282,
	label = "s2_6_6_quinoline_nitro2",
	group = 
"""
1  N5dc u0 {3,D} {10,S}
2  C u0 {3,S} {4,D} {5,S}
3  C u0 {1,D} {2,S} {6,S}
4  C u0 {2,D} {9,S}
5  C u0 {2,S} {7,D}
6  C u0 {3,S} {8,D}
7  C u0 {5,D} {8,S}
8  C u0 {6,D} {7,S}
9  * C u0 {4,S} {10,D}
10 C u0 {1,S} {9,D}
""",
	solute = u's2_6_6_quinoline_nitro',
	dataCount = None,
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
this is one of the groups that belong to s2_6_6_quinoline_nitro
""",
)

entry(
	index = 283,
	label = "s2_6_6_quinoline_nitro",
	group = 
"""
1    R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {6,[S,D,T,B]}
2    R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3    R!H u0 {1,[S,D,T,B]} {9,[S,D,T,B]}
4    R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
5    R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
6    R!H u0 {1,[S,D,T,B]} {10,[S,D,T,B]}
7  * R!H u0 {4,[S,D,T,B]} {9,[S,D,T,B]}
8    R!H u0 {5,[S,D,T,B]} {10,[S,D,T,B]}
9    R!H u0 {3,[S,D,T,B]} {7,[S,D,T,B]}
10   R!H u0 {6,[S,D,T,B]} {8,[S,D,T,B]}
""",
	solute = SoluteData(
		S = 0.10305,
		B = 0.02319,
		E = 0.05358,
		L = 0.27670,
		A = -0.00735,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
		E = 3,
		L = 2,
		A = 2,
	),
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
dummy group to put all s2_6_6_quinoline_nitro groups (s2_6_6_quinoline_nitro1-2) together
""",
)

entry(
	index = 284,
	label = "s2_6_6_quinoline",
	group = 
"""
1    R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {6,[S,D,T,B]}
2    R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3    R!H u0 {1,[S,D,T,B]} {9,[S,D,T,B]}
4    R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
5    R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
6    R!H u0 {1,[S,D,T,B]} {10,[S,D,T,B]}
7  * R!H u0 {4,[S,D,T,B]} {9,[S,D,T,B]}
8    R!H u0 {5,[S,D,T,B]} {10,[S,D,T,B]}
9    R!H u0 {3,[S,D,T,B]} {7,[S,D,T,B]}
10   R!H u0 {6,[S,D,T,B]} {8,[S,D,T,B]}
""",
	solute = SoluteData(
		S = -0.09548,
		B = 0.03091,
		E = -0.01508,
		L = 0.08005,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 39,
		B = 39,
		E = 41,
		L = 36,
		A = 41,
	),
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
dummy group to put all s2_6_6_quinoline groups (s2_6_6_quinoline1-2) together
""",
)

entry(
	index = 285,
	label = "s2_6_6_isoquinoline_general",
	group =  "OR{s2_6_6_isoquinoline1, s2_6_6_isoquinoline2}",
	solute = u's2_6_6_isoquinoline',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 286,
	label = "s2_6_6_isoquinoline1",
	group = 
"""
1  * N u0 {9,D} {10,S}
2  C u0 {3,B} {5,B} {6,S}
3  C u0 {2,B} {4,B} {9,S}
4  C u0 {3,B} {8,B}
5  C u0 {2,B} {7,B}
6  C u0 {2,S} {10,D}
7  C u0 {5,B} {8,B}
8  C u0 {4,B} {7,B}
9  C u0 {1,D} {3,S}
10 C u0 {1,S} {6,D}
""",
	solute = u's2_6_6_isoquinoline',
	dataCount = None,
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
this is one of the groups that belong to s2_6_6_isoquinoline
""",
)

entry(
	index = 287,
	label = "s2_6_6_isoquinoline2",
	group = 
"""
1  * N u0 {9,S} {10,D}
2  C u0 {3,S} {4,S} {6,D}
3  C u0 {2,S} {5,S} {9,D}
4  C u0 {2,S} {7,D}
5  C u0 {3,S} {8,D}
6  C u0 {2,D} {10,S}
7  C u0 {4,D} {8,S}
8  C u0 {5,D} {7,S}
9  C u0 {1,S} {3,D}
10 C u0 {1,D} {6,S}
""",
	solute = u's2_6_6_isoquinoline',
	dataCount = None,
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
this is one of the groups that belong to s2_6_6_isoquinoline
""",
)

entry(
	index = 288,
	label = "s2_6_6_isoquinoline",
	group = 
"""
1    R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {6,[S,D,T,B]}
2    R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3    R!H u0 {1,[S,D,T,B]} {9,[S,D,T,B]}
4    R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
5    R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
6    R!H u0 {1,[S,D,T,B]} {10,[S,D,T,B]}
7  * R!H u0 {4,[S,D,T,B]} {9,[S,D,T,B]}
8    R!H u0 {5,[S,D,T,B]} {10,[S,D,T,B]}
9    R!H u0 {3,[S,D,T,B]} {7,[S,D,T,B]}
10   R!H u0 {6,[S,D,T,B]} {8,[S,D,T,B]}
""",
	solute = SoluteData(
		S = 0.03888,
		B = 0.02608,
		E = -0.00598,
		L = 0.16069,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 3,
		E = 5,
		L = 5,
		A = 6,
	),
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
dummy group to put all s2_6_6_isoquinoline groups (s2_6_6_isoquinoline1-2) together
""",
)

entry(
	index = 289,
	label = "s2_6_6_ben_heteroaromatic",
	group = 
"""
1    R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {6,[S,D,T,B]}
2    R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3    R!H u0 {1,[S,D,T,B]} {9,[S,D,T,B]}
4    R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
5    R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
6    R!H u0 {1,[S,D,T,B]} {10,[S,D,T,B]}
7  * R!H u0 {4,[S,D,T,B]} {9,[S,D,T,B]}
8    R!H u0 {5,[S,D,T,B]} {10,[S,D,T,B]}
9    R!H u0 {3,[S,D,T,B]} {7,[S,D,T,B]}
10   R!H u0 {6,[S,D,T,B]} {8,[S,D,T,B]}
""",
	solute = SoluteData(
		S = 0.12359,
		B = -0.01719,
		E = 0.09017,
		L = 0.31087,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 10,
		B = 10,
		E = 10,
		L = 10,
		A = 10,
	),
	shortDesc = u"""special solvation polycyclic group""",
	longDesc = 
u"""
dummy group to put all s2_6_6_ben_heteroaromatic groups (s2_6_6_ben_heteroaromatic1-4) together
""",
)

entry(
	index = 290,
	label = "s2_6_6_naphthalene",
	group = 
"""
1    R!H u0 {2,B} {3,B} {4,B}
2    R!H u0 {1,B} {5,B} {6,B}
3    R!H u0 {1,B} {9,B}
4    R!H u0 {1,B} {8,B}
5    R!H u0 {2,B} {10,B}
6    R!H u0 {2,B} {7,B}
7  * R!H u0 {6,B} {8,B}
8    R!H u0 {4,B} {7,B}
9    R!H u0 {3,B} {10,B}
10   R!H u0 {5,B} {9,B}
""",
	solute = SoluteData(
		S = -0.11108,
		B = 0.03868,
		E = -0.10182,
		L = -0.02138,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 221,
		B = 219,
		E = 236,
		L = 216,
		A = 235,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 291,
	label = "s2_6_7",
	group = 
"""
1    R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {6,[S,D,T,B]}
2    R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3    R!H u0 {1,[S,D,T,B]} {9,[S,D,T,B]}
4    R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
5    R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
6    R!H u0 {1,[S,D,T,B]} {10,[S,D,T,B]}
7  * R!H u0 {4,[S,D,T,B]} {9,[S,D,T,B]}
8    R!H u0 {5,[S,D,T,B]} {11,[S,D,T,B]}
9    R!H u0 {3,[S,D,T,B]} {7,[S,D,T,B]}
10   R!H u0 {6,[S,D,T,B]} {11,[S,D,T,B]}
11   R!H u0 {8,[S,D,T,B]} {10,[S,D,T,B]}
""",
	solute = SoluteData(
		S = 0.04430,
		B = -0.04834,
		E = 0.09810,
		L = 0.02258,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 4,
		B = 4,
		E = 4,
		L = 3,
		A = 4,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 292,
	label = "s2_6_7_ben",
	group = 
"""
1    R!H u0 {2,B} {3,B} {6,[S,D,T,B]}
2    R!H u0 {1,B} {4,B} {5,[S,D,T,B]}
3    R!H u0 {1,B} {9,B}
4    R!H u0 {2,B} {7,B}
5    R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
6    R!H u0 {1,[S,D,T,B]} {10,[S,D,T,B]}
7  * R!H u0 {4,B} {9,B}
8    R!H u0 {5,[S,D,T,B]} {11,[S,D,T,B]}
9    R!H u0 {3,B} {7,B}
10   R!H u0 {6,[S,D,T,B]} {11,[S,D,T,B]}
11   R!H u0 {8,[S,D,T,B]} {10,[S,D,T,B]}
""",
	solute = SoluteData(
		S = 0.02284,
		B = 0.02362,
		E = -0.03239,
		L = 0.03414,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 9,
		B = 9,
		E = 9,
		L = 8,
		A = 9,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 293,
	label = "s2_6_7_ben_ene",
	group =  "OR{s2_6_7_ben_ene_1}",
	solute = u's2_6_7_ben_ene_1',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 294,
	label = "s2_6_7_ben_ene_1",
	group = 
"""
1    R!H u0 {2,B} {3,B} {6,[S,D,T,B]}
2    R!H u0 {1,B} {4,B} {5,[S,D,T,B]}
3    R!H u0 {1,B} {9,B}
4    R!H u0 {2,B} {7,B}
5    R!H u0 {2,[S,D,T,B]} {8,D}
6    R!H u0 {1,[S,D,T,B]} {10,[S,D,T,B]}
7  * R!H u0 {4,B} {9,B}
8    R!H u0 {5,D} {11,[S,D,T,B]}
9    R!H u0 {3,B} {7,B}
10   R!H u0 {6,[S,D,T,B]} {11,[S,D,T,B]}
11   R!H u0 {8,[S,D,T,B]} {10,[S,D,T,B]}
""",
	solute = SoluteData(
		S = -0.19877,
		B = 0.13041,
		E = -0.09436,
		L = -0.16154,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 31,
		B = 31,
		E = 31,
		L = 10,
		A = 31,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 295,
	label = "s2_6_7_ben_diene_1_3",
	group = 
"""
1    R!H u0 {2,B} {3,B} {6,[S,D,T,B]}
2    R!H u0 {1,B} {4,B} {5,[S,D,T,B]}
3    R!H u0 {1,B} {9,B}
4    R!H u0 {2,B} {7,B}
5    R!H u0 {2,[S,D,T,B]} {8,D}
6    R!H u0 {1,[S,D,T,B]} {10,[S,D,T,B]}
7  * R!H u0 {4,B} {9,B}
8    R!H u0 {5,D} {11,[S,D,T,B]}
9    R!H u0 {3,B} {7,B}
10   R!H u0 {6,[S,D,T,B]} {11,D}
11   R!H u0 {8,[S,D,T,B]} {10,D}
""",
	solute = SoluteData(
		S = -0.04432,
		B = 0.04576,
		E = -0.02546,
		L = -0.04960,
		A = -0.01639,
	),
	dataCount = DataCountGAV(
		S = 1,
		B = 1,
		E = 1,
		L = 1,
		A = 1,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 296,
	label = "s2_9_4",
	group = 
"""
1  * R!H u0 {2,[S,D,B]} {4,[S,D,B]} {6,[S,D,B]}
2  R!H u0 {1,[S,D,B]} {3,[S,D,B]} {5,[S,D,B]}
3  R!H u0 {2,[S,D,B]} {7,[S,D,B]}
4  R!H u0 {1,[S,D,B]} {5,[S,D,B]}
5  R!H u0 {2,[S,D,B]} {4,[S,D,B]}
6  R!H u0 {1,[S,D,B]} {9,[S,D,B]}
7  R!H u0 {3,[S,D,B]} {8,[S,D,B]}
8  R!H u0 {7,[S,D,B]} {10,[S,D,B]}
9  R!H u0 {6,[S,D,B]} {11,[S,D,B]}
10 R!H u0 {8,[S,D,B]} {11,[S,D,B]}
11 R!H u0 {9,[S,D,B]} {10,[S,D,B]}
""",
	solute = u's2_9_4_ene',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 297,
	label = "s2_9_4_ene",
	group = 
"""
1  * R!H u0 {2,S} {4,S} {6,S}
2  R!H u0 {1,S} {3,S} {5,S}
3  R!H u0 {2,S} {7,S}
4  R!H u0 {1,S} {5,S}
5  R!H u0 {2,S} {4,S}
6  R!H u0 {1,S} {9,S}
7  R!H u0 {3,S} {8,S}
8  R!H u0 {7,S} {10,S}
9  R!H u0 {6,S} {11,S}
10 R!H u0 {8,S} {11,D}
11 R!H u0 {9,S} {10,D}
""",
	solute = SoluteData(
		S = 0.03321,
		B = 0.00107,
		E = -0.03469,
		L = -0.18576,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 3,
		L = 3,
		A = 3,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 298,
	label = "s3_4_4",
	group = 
"""
1   R!H u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 * R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
""",
	solute = u's3_4_4_ane',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 299,
	label = "s3_4_4_ane",
	group = 
"""
1   R!H u0 {3,S} {4,S} {5,S}
2   R!H u0 {3,S} {4,S} {5,S}
3 * R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {2,S}
5   R!H u0 {1,S} {2,S}
""",
	solute = SoluteData(
		S = 0.03269,
		B = 0.01550,
		E = 0.05130,
		L = -0.03673,
		A = 0.00139,
	),
	dataCount = DataCountGAV(
		S = 1,
		B = 1,
		E = 1,
		L = 1,
		A = 1,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 300,
	label = "s3_4_6",
	group = 
"""
1   R!H u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
2   R!H u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 * R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
5   R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
6   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
7   R!H u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
""",
	solute = u's3_4_6_ane',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 301,
	label = "s3_4_6_ane",
	group = 
"""
1   R!H u0 {3,S} {4,S} {6,S}
2   R!H u0 {3,S} {4,S} {5,S}
3 * R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {2,S}
5   R!H u0 {2,S} {7,S}
6   R!H u0 {1,S} {7,S}
7   R!H u0 {5,S} {6,S}
""",
	solute = SoluteData(
		S = -0.03200,
		B = 0.04435,
		E = 0.02742,
		L = -0.03462,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 3,
		L = 3,
		A = 3,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 302,
	label = "s3_4_6_ene",
	group =  "OR{s3_4_6_ene_1}",
	solute = u's3_4_6_ene_1',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 303,
	label = "s3_4_6_ene_1",
	group = 
"""
1   R!H u0 {3,S} {4,S} {6,S}
2   R!H u0 {3,S} {4,S} {5,S}
3 * R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {2,S}
5   R!H u0 {2,S} {7,S}
6   R!H u0 {1,S} {7,D}
7   R!H u0 {5,S} {6,D}
""",
	solute = SoluteData(
		S = -0.02747,
		B = 0.01408,
		E = -0.01073,
		L = -0.22894,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 8,
		B = 8,
		E = 8,
		L = 8,
		A = 8,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 304,
	label = "s3_5_5",
	group = 
"""
1   R!H u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {3,[S,D,T,B]} {6,[S,D,T,B]} {7,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4 * R!H u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6   R!H u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
7   R!H u0 {2,[S,D,T,B]} {5,[S,D,T,B]}
""",
	solute = u's3_5_5_ane',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 305,
	label = "s3_5_5_ene",
	group =  "OR{s3_5_5_ene_1, s3_5_5_ene_side}",
	solute = u's3_5_5_ene_1',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 306,
	label = "s3_5_5_ene_1",
	group = 
"""
1   R!H u0 {3,S} {5,S} {6,S}
2   R!H u0 {3,S} {4,S} {7,S}
3   R!H u0 {1,S} {2,S}
4 * R!H u0 {2,S} {5,S}
5   R!H u0 {1,S} {4,S}
6   R!H u0 {1,S} {7,D}
7   R!H u0 {2,S} {6,D}
""",
	solute = SoluteData(
		S = -0.05483,
		B = -0.11774,
		E = -0.01759,
		L = -0.30255,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 19,
		B = 17,
		E = 22,
		L = 18,
		A = 22,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 307,
	label = "s3_5_5_ene_side",
	group = 
"""
1   R!H u0 {3,S} {4,S} {6,S}
2   R!H u0 {4,S} {5,S} {7,S}
3 * R!H u0 {1,S} {5,S} {8,D}
4   R!H u0 {1,S} {2,S}
5   R!H u0 {2,S} {3,S}
6   R!H u0 {1,S} {7,S}
7   R!H u0 {2,S} {6,S}
8   R!H ux {3,D}
""",
	solute = SoluteData(
		S = -0.00708,
		B = 0.02176,
		E = -0.00349,
		L = -0.10827,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 4,
		B = 4,
		E = 4,
		L = 4,
		A = 4,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 308,
	label = "s3_5_5_ene_side_norcamphor",
	group = 
"""
1   C  u0 {3,S} {4,S} {6,S}
2   C  u0 {4,S} {5,S} {7,S}
3 * CO u0 {1,S} {5,S} {8,D}
4   C  u0 {1,S} {2,S}
5   C  u0 {2,S} {3,S}
6   C  u0 {1,S} {7,S}
7   C  u0 {2,S} {6,S}
8   O2d u0 {3,D}
""",
	solute = SoluteData(
		S = -0.01799,
		B = 0.04560,
		E = -0.01425,
		L = -0.25746,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 4,
		B = 4,
		E = 4,
		L = 3,
		A = 4,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 309,
	label = "s3_5_5_ane",
	group = 
"""
1   R!H u0 {3,S} {4,S} {5,S}
2   R!H u0 {3,S} {6,S} {7,S}
3   R!H u0 {1,S} {2,S}
4 * R!H u0 {1,S} {6,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {2,S} {4,S}
7   R!H u0 {2,S} {5,S}
""",
	solute = SoluteData(
		S = -0.11270,
		B = 0.00000,
		E = -0.00276,
		L = -0.44472,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 21,
		B = 21,
		E = 22,
		L = 21,
		A = 23,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 310,
	label = "s3_5_5_diene",
	group =  "OR{s3_5_5_diene_1_4}",
	solute = u's3_5_5_diene_1_4',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 311,
	label = "s3_5_5_diene_1_4",
	group = 
"""
1   R!H u0 {3,S} {6,S} {7,S}
2   R!H u0 {3,S} {4,S} {5,S}
3   R!H u0 {1,S} {2,S}
4 * R!H u0 {2,S} {6,D}
5   R!H u0 {2,S} {7,D}
6   R!H u0 {1,S} {4,D}
7   R!H u0 {1,S} {5,D}
""",
	solute = SoluteData(
		S = -0.00176,
		B = 0.00155,
		E = -0.01260,
		L = -0.01478,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 1,
		B = 1,
		E = 1,
		L = 1,
		A = 1,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 312,
	label = "s3_5_6",
	group = 
"""
1   R!H u0 {3,[S,D,T,B]} {5,[S,D,T,B]} {6,[S,D,T,B]}
2   R!H u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {7,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {5,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]}
6   R!H u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
7   R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
8 * R!H u0 {6,[S,D,T,B]} {7,[S,D,T,B]}
""",
	solute = u's3_5_6_ane',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 313,
	label = "s3_5_6_ane",
	group = 
"""
1   R!H u0 {3,S} {5,S} {6,S}
2   R!H u0 {3,S} {4,S} {7,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {2,S} {5,S}
5   R!H u0 {1,S} {4,S}
6   R!H u0 {1,S} {8,S}
7   R!H u0 {2,S} {8,S}
8 * R!H u0 {6,S} {7,S}
""",
	solute = SoluteData(
		S = -0.04708,
		B = 0.06188,
		E = -0.04224,
		L = -0.15630,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 6,
		B = 6,
		E = 7,
		L = 6,
		A = 6,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 314,
	label = "s3_5_6_ane_tropane",
	group = 
"""
1   C u0 {3,S} {5,S} {6,S}
2   C u0 {3,S} {4,S} {7,S}
3   N u0 {1,S} {2,S}
4   C u0 {2,S} {5,S}
5   C u0 {1,S} {4,S}
6   C u0 {1,S} {8,S}
7   C u0 {2,S} {8,S}
8 * C u0 {6,S} {7,S}
""",
	solute = SoluteData(
		S = -0.05339,
		B = 0.06184,
		E = -0.01742,
		L = -0.25923,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 5,
		E = 5,
		L = 5,
		A = 5,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 315,
	label = "s3_5_6_ene",
	group =  "OR{s3_5_6_ene_1}",
	solute = u's3_5_6_ene_1',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 316,
	label = "s3_5_6_ene_1",
	group = 
"""
1   R!H u0 {3,S} {4,S} {7,S}
2   R!H u0 {3,S} {5,S} {6,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {5,S}
5   R!H u0 {2,S} {4,S}
6   R!H u0 {2,S} {8,S}
7   R!H u0 {1,S} {8,D}
8 * R!H u0 {6,S} {7,D}
""",
	solute = SoluteData(
		S = -0.04624,
		B = -0.01231,
		E = -0.00390,
		L = -0.08479,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 3,
		L = 3,
		A = 3,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 317,
	label = "s3_5_7",
	group = 
"""
1 * R!H u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {7,[S,D,T,B]}
2   R!H u0 {3,[S,D,T,B]} {5,[S,D,T,B]} {6,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {1,[S,D,T,B]} {5,[S,D,T,B]}
5   R!H u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
6   R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
7   R!H u0 {1,[S,D,T,B]} {9,[S,D,T,B]}
8   R!H u0 {6,[S,D,T,B]} {9,[S,D,T,B]}
9   R!H u0 {7,[S,D,T,B]} {8,[S,D,T,B]}
""",
	solute = u's3_5_7_ane_0',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 318,
	label = "s3_5_7_ane_0",
	group = 
"""
1 * R!H u0 {3,S} {4,S} {7,S}
2   R!H u0 {3,S} {5,S} {6,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {5,S}
5   R!H u0 {2,S} {4,S}
6   R!H u0 {2,S} {8,S}
7   R!H u0 {1,S} {9,S}
8   R!H u0 {6,S} {9,S}
9   R!H u0 {7,S} {8,S}
""",
	solute = SoluteData(
		S = 0.01611,
		B = -0.07058,
		E = 0.07610,
		L = 0.04672,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
		E = 2,
		L = 1,
		A = 2,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 319,
	label = "s3_6_6",
	group = 
"""
1   R!H u0 {3,[S,D,T,B]} {6,[S,D,T,B]} {7,[S,D,T,B]}
2   R!H u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4 * R!H u0 {2,[S,D,T,B]} {9,[S,D,T,B]}
5   R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
6   R!H u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
7   R!H u0 {1,[S,D,T,B]} {9,[S,D,T,B]}
8   R!H u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
9   R!H u0 {4,[S,D,T,B]} {7,[S,D,T,B]}
""",
	solute = u's3_6_6_ane',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 320,
	label = "s3_6_6_ane",
	group = 
"""
1   R!H u0 {3,S} {6,S} {7,S}
2   R!H u0 {3,S} {4,S} {5,S}
3   R!H u0 {1,S} {2,S}
4 * R!H u0 {2,S} {9,S}
5   R!H u0 {2,S} {8,S}
6   R!H u0 {1,S} {8,S}
7   R!H u0 {1,S} {9,S}
8   R!H u0 {5,S} {6,S}
9   R!H u0 {4,S} {7,S}
""",
	solute = SoluteData(
		S = 0.02842,
		B = 0.09046,
		E = 0.05043,
		L = 0.12760,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 8,
		B = 8,
		E = 8,
		L = 5,
		A = 10,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 321,
	label = "s4_6_6",
	group = 
"""
1 * R!H u0 {3,[S,D,T,B]} {6,[S,D,T,B]} {8,[S,D,T,B]}
2   R!H u0 {4,[S,D,T,B]} {5,[S,D,T,B]} {7,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]}
5   R!H u0 {2,[S,D,T,B]} {6,[S,D,T,B]}
6   R!H u0 {1,[S,D,T,B]} {5,[S,D,T,B]}
7   R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
8   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
""",
	solute = u's4_6_6_ane',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 322,
	label = "s4_6_6_ane",
	group = 
"""
1 * R!H u0 {3,S} {6,S} {8,S}
2   R!H u0 {4,S} {5,S} {7,S}
3   R!H u0 {1,S} {4,S}
4   R!H u0 {2,S} {3,S}
5   R!H u0 {2,S} {6,S}
6   R!H u0 {1,S} {5,S}
7   R!H u0 {2,S} {8,S}
8   R!H u0 {1,S} {7,S}
""",
	solute = SoluteData(
		S = -0.07049,
		B = 0.07524,
		E = 0.03424,
		L = -0.03434,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 9,
		B = 9,
		E = 9,
		L = 8,
		A = 9,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

tree(
"""
L1: PolycyclicRing
	L2: polycyclic_7fused
		L3: Strychnine_general
			L4: Strychnine
	L2: polycyclic_5fused
		L3: Porphyrin
		L3: Morphine_general
			L4: Dihydro-normorphine,3-desoxy-
			L4: Morphine
			L4: Dihydromorphine
		L3: Benzo[e]pyrene_general
			L4: Benzo[e]pyrene
		L3: Benzo[a]pyrene_general
			L4: Benzo[a]pyrene
		L3: Fluoran_general
			L4: Fluoran
		L3: Picene_general
			L4: Picene
			L4: Icosahydropicene
		L3: 1H-Cyclopenta[a]chrysene_general
			L4: 1H-Cyclopenta[a]chrysene
		L3: Benzo[ghi]fluoranthene_general
			L4: Benzo[ghi]fluoranthene
		L3: Cholanthrene_general
			L4: Cholanthrene
		L3: 5fused_r6_r6_r6_r5_r5
			L4: 5fused_r6_diene_r6_r6_r5_r5_dioxo
	L2: polycyclic_4fused
		L3: Artemether_general
			L4: Artemether
		L3: Fluoranthene_general
			L4: Fluoranthene
		L3: s3_6_6_s3_6_6_s3_6_6
			L4: s3_6_6_s3_6_6_s3_6_6_pyrene
		L3: s2_5_6_s2_6_6_s2_6_6
			L4: s2_5_6_s2_6_6_s2_6_6_ben
				L5: s2_5_6_s2_6_6_s2_6_6_ben_onlyC
			L4: s2_5_6_s2_6_6_s2_6_6_ane
				L5: s2_5_6_s2_6_6_s2_6_6_ane_onlyC
					L6: s2_5_6_s2_6_6_s2_6_6_ane_onlyC(=O)
			L4: s2_5_6_s2_6_6_s2_6_6_ene_2
				L5: s2_5_6_s2_6_6_s2_6_6_ene_2_onlyC
					L6: s2_5_6_s2_6_6_s2_6_6_ene_2_onlyC(=O)
			L4: s2_5_6_s2_6_6_s2_6_6_ene_3
				L5: s2_5_6_s2_6_6_s2_6_6_ene_3_onlyC
			L4: s2_5_6_s2_6_6_s2_6_6_diene_2_16
				L5: s2_5_6_s2_6_6_s2_6_6_diene_2_16_onlyC
					L6: s2_5_6_s2_6_6_s2_6_6_diene_2_16_onlyC(=O)
			L4: s2_5_6_s2_6_6_s2_6_6_diene_2_4
				L5: s2_5_6_s2_6_6_s2_6_6_diene_2_4_onlyC
					L6: s2_5_6_s2_6_6_s2_6_6_diene_2_4_onlyC(=O)
			L4: s2_5_6_s2_6_6_s2_6_6_triene_2_12_14
				L5: s2_5_6_s2_6_6_s2_6_6_triene_2_12_14_onlyC
		L3: s2_6_6_s2_6_6_s2_6_6
			L4: s2_6_6_s2_6_6_s2_6_6_aromatic
				L5: s2_6_6_s2_6_6_s2_6_6_benz[a]anthracene
				L5: s2_6_6_s2_6_6_s2_6_6_benzacridine
		L3: s2_6_6_s2_6_6_s2_6_6_A
			L4: s2_6_6_s2_6_6_s2_6_6_A_chrysene
		L3: s2_6_6_s2_6_6_s2_6_6_B
			L4: s2_6_6_s2_6_6_s2_6_6_B_tetracene
			L4: s2_6_6_s2_6_6_s2_6_6_B_1,2,3,4,6,11-hexahydrotetracene
			L4: s2_6_6_s2_6_6_s2_6_6_B_ben_diene
		L3: s2_6_5_s2_5_9_s3_9_6
			L4: s2_6_5_ben_ene_s2_5_9_s3_9_6_hetero
		L3: s2_6_7_s2_7_6_s2_7_6
			L4: s2_6_7_ben_s2_7_6_ben_s2_7_6_piperidine
		L3: Quadricyclane_general
			L4: Quadricyclane
	L2: polycyclic_3fused
		L3: Adamantane_general
			L4: Adamantane
		L3: s2_6_7_s2_7_6
			L4: s2_6_7_ben_s2_7_6_ben_general
				L5: s2_6_7_ben_s2_7_6_ben_iminodibenzyl_general
					L6: s2_6_7_ben_s2_7_6_ben_iminodibenzyl
				L5: s2_6_7_ben_s2_7_6_ben
			L4: s2_6_7_ben_s2_7_6_ben_ene
		L3: s2_6_6_s2_6_5
			L4: s2_6_6_s2_6_5_ben_ene
			L4: s2_6_6_s2_6_5_ben_diene
				L5: s2_6_6_s2_6_5_ben_diene_psoralen
		L3: s2_6_6_s2_6_6
			L4: s2_6_6_s2_6_6_aromatic
				L5: s2_6_6_s2_6_6_all_ben
				L5: s2_6_6_s2_6_6_heteroaromatic
			L4: s2_6_6_ben_s2_6_6_ben
			L4: s2_6_6_ene_s2_6_6_ene
			L4: s2_6_6_ben_s2_6_6_ane
		L3: s2_6_6_s2_6_6_A
			L4: s2_6_6_s2_6_6_A_aromatic
				L5: s2_6_6_s2_6_6_A_anthracene
				L5: s2_6_6_s2_6_6_A_acridine
			L4: s2_6_6_ben_s2_6_6_ben_A
				L5: s2_6_6_ben_s2_6_6_ben_A_anthraquinone
				L5: s2_6_6_ben_s2_6_6_ben_A_phenothiazine
				L5: s2_6_6_ben_s2_6_6_ben_A_9H-xanthene
		L3: s2_6_5_s2_5_6
			L4: s2_6_5_ben_s2_5_6_ben
				L5: s2_6_5_s2_5_6_fluorene
				L5: s2_6_5_s2_5_6_carbazole
				L5: s2_6_5_s2_5_6_dibenzofuran
				L5: s2_6_5_s2_5_6_dibenzothiophene
			L4: s2_6_5_ben_s2_5_6
				L5: s2_6_5_ben_s2_5_6_hetero
		L3: s2_5_6_s2_6_6
			L4: s2_5_6_ben_s2_6_6_ben
				L5: s2_5_6_s2_6_6_naphtho[2,1-b]thiophene
				L5: s2_5_6_s2_6_6_benzo[g][1]benzothiole
		L3: s2_5_7_s2_7_3
			L4: s2_5_7_s2_7_3_ane
				L5: s2_5_7_s2_7_3_ane_side_ene
			L4: s2_5_7_s2_7_3_ene
		L3: Nortricyclene_general
			L4: Nortricyclene
		L3: s3_6_3_s3_3_6
			L4: s3_6_3_s3_3_6_ane
			L4: s3_6_3_s3_3_6_ene
		L3: Acenaphthene_general
			L4: Acenaphthene
			L4: Acenaphthylene
		L3: s2_5_5_s2_5_5_ane
	L2: s1_3_6
		L3: s1_3_6_ane
	L2: s1_5_5
		L3: s1_5_5_ane
	L2: s1_5_6
		L3: s1_5_6_ane
		L3: s1_5_6_ene
			L4: s1_5_6_ene_1
			L4: s1_5_6_ene_2
			L4: s1_5_6_ene_7
			L4: s1_5_6_ene_8
	L2: s1_6_6
		L3: s1_6_6_ane
			L4: s1_6_6_ane_2,4,8,10-Tetraoxa-3,9-diphosphaspiro-3,9-dioxide
	L2: s2_3_5
		L3: s2_3_5_ene
			L4: s2_3_5_ene_1
			L4: s2_3_5_ene_side
		L3: s2_3_5_ane
	L2: s2_3_6
		L3: s2_3_6_ane
		L3: s2_3_6_ene
			L4: s2_3_6_ene_1
			L4: s2_3_6_ene_2
	L2: s2_3_8
		L3: s2_3_8_ane
	L2: s2_4_5
		L3: s2_4_5_ane
			L4: s2_4_5_ane_hetero_N_S
	L2: s2_4_6
		L3: s2_4_6_ene
			L4: s2_4_6_ene_1
	L2: s2_5_5
		L3: s2_5_5_ane
		L3: s2_5_5_ene
			L4: s2_5_5_ene_0
			L4: s2_5_5_ene_1
		L3: s2_5_5_diene
			L4: s2_5_5_diene_0_2
			L4: s2_5_5_diene_0_4
	L2: s2_5_6
		L3: s2_5_6_ane
		L3: s2_5_6_ene
			L4: s2_5_6_ene_0
			L4: s2_5_6_ene_1
			L4: s2_5_6_ene_m
			L4: s2_5_6_ene_2
			L4: s2_5_6_ene_5
		L3: s2_5_6_diene
			L4: s2_5_6_diene_m_2
			L4: s2_5_6_diene_m_7
				L5: s2_5_6_diene_m_7_hetero
					L6: s2_5_6_diene_xanthine
		L3: s2_5_6_triene
			L4: s2_5_6_triene_m_1_7
		L3: s2_5_6_tetraene
			L4: s2_5_6_tetraene_1_3_5_7
			L4: s2_5_6_tetraene_1_3_5_8
		L3: s2_5_6_ben
			L4: s2_5_6_ben_onlyC
			L4: s2_5_6_phthalan
			L4: s2_5_6_2,3-dihydrobenzofuran
			L4: s2_5_6_indoline
				L5: s2_5_6_isatin
				L5: s2_5_6_oxindole
			L4: s2_5_6_isoindoline
				L5: s2_5_6_isoindole-1,3-dione
			L4: s2_5_6_1,3-benzodioxole
			L4: s2_5_6_2,3-dihydrobenzothiophene
		L3: s2_5_6_heteroaromatic_general
			L4: s2_5_6_purine_general
				L5: s2_5_6_purine
					L6: s2_5_6_hypoxanthine_general
						L7: s2_5_6_hypoxanthine
			L4: s2_5_6_heteroaromatic
		L3: s2_5_6_indene_general
			L4: s2_5_6_indene
			L4: s2_5_6_indole
			L4: s2_5_6_benzimidazole
			L4: s2_5_6_indazole
			L4: s2_5_6_benzofuran
			L4: s2_5_6_benzothiophene
			L4: s2_5_6_benzoxazole
			L4: s2_5_6_benzisoxazole
			L4: s2_5_6_benzothiazole
			L4: s2_5_6_benzotriazole
	L2: s2_5_7
		L3: s2_5_7_azulene
		L3: s2_5_7_ene_1
		L3: s2_5_7_ene_2
	L2: s2_6_6
		L3: s2_6_6_ane
		L3: s2_6_6_ene
			L4: s2_6_6_ene_0
			L4: s2_6_6_ene_1
			L4: s2_6_6_ene_2
			L4: s2_6_6_ene_m
		L3: s2_6_6_diene
			L4: s2_6_6_diene_0_2
			L4: s2_6_6_diene_0_3
			L4: s2_6_6_diene_0_6
			L4: s2_6_6_diene_0_8
			L4: s2_6_6_diene_1_6
			L4: s2_6_6_diene_1_7
		L3: s2_6_6_tetraene
			L4: s2_6_6_tetraene_0_2_4_7
			L4: s2_6_6_tetraene_0_2_6_8
		L3: s2_6_6_ben
			L4: s2_6_6_ben_onlyC
			L4: s2_6_6_ben_chromane
			L4: s2_6_6_ben_1,4-dioxane
		L3: s2_6_6_ben_ene
			L4: s2_6_6_ben_ene_1
				L5: s2_6_6_ben_ene_1_2-Benzothiazine-1,1-dioxide
				L5: s2_6_6_ben_ene_1_coumarin
			L4: s2_6_6_ben_ene_2
				L5: s2_6_6_chromen-4-one
		L3: s2_6_6_ben_heteroaromatic_general
			L4: s2_6_6_quinoline_general
				L5: s2_6_6_8-Hydroxyquinoline_general
					L6: s2_6_6_8-Hydroxyquinoline
				L5: s2_6_6_quinoline_nitro_general
					L6: s2_6_6_quinoline_nitro
				L5: s2_6_6_quinoline
			L4: s2_6_6_isoquinoline_general
				L5: s2_6_6_isoquinoline
			L4: s2_6_6_ben_heteroaromatic
		L3: s2_6_6_naphthalene
	L2: s2_6_7
		L3: s2_6_7_ben
			L4: s2_6_7_ben_ene
				L5: s2_6_7_ben_ene_1
					L6: s2_6_7_ben_diene_1_3
	L2: s2_9_4
		L3: s2_9_4_ene
	L2: s3_4_4
		L3: s3_4_4_ane
	L2: s3_4_6
		L3: s3_4_6_ane
		L3: s3_4_6_ene
			L4: s3_4_6_ene_1
	L2: s3_5_5
		L3: s3_5_5_ene
			L4: s3_5_5_ene_1
			L4: s3_5_5_ene_side
				L5: s3_5_5_ene_side_norcamphor
		L3: s3_5_5_ane
		L3: s3_5_5_diene
			L4: s3_5_5_diene_1_4
	L2: s3_5_6
		L3: s3_5_6_ane
			L4: s3_5_6_ane_tropane
		L3: s3_5_6_ene
			L4: s3_5_6_ene_1
	L2: s3_5_7
		L3: s3_5_7_ane_0
	L2: s3_6_6
		L3: s3_6_6_ane
	L2: s4_6_6
		L3: s4_6_6_ane
"""
)
