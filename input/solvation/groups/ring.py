#!/usr/bin/env python
# encoding: utf-8

name = "ring"
shortDesc = u""
longDesc = u""" 
All groups are fitted using experimental solute parameter data unless written otherwise.
See Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
"""

entry(
	index = 1,
	label = "Ring",
	group = 
"""
1 * R u0
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
	label = "Aromatic",
	group = 
"""
1 * Cb u0
""",
	solute = u'Benzene',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 3,
	label = "Benzene",
	group = 
"""
1 * Cb u0 {2,B} {6,B}
2   Cb u0 {1,B} {3,B}
3   Cb u0 {2,B} {4,B}
4   Cb u0 {3,B} {5,B}
5   Cb u0 {4,B} {6,B}
6   Cb u0 {1,B} {5,B}
""",
	solute = SoluteData(
		S = -0.08211,
		B = 0.03455,
		E = -0.09106,
		L = -0.06839,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 3037,
		B = 2925,
		E = 3195,
		L = 2736,
		A = 3192,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 4,
	label = "ThreeMember",
	group = 
"""
1 * R!H u0 {2,[S,D,T]} {3,[S,D]}
2   R!H u0 {1,[S,D,T]} {3,[S,D]}
3   R!H u0 {1,[S,D]} {2,[S,D]}
""",
	solute = u'Cyclopropane',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 5,
	label = "Cyclopropane",
	group = 
"""
1 * Cs u0 {2,S} {3,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {1,S} {2,S}
""",
	solute = SoluteData(
		S = 0.08944,
		B = 0.00000,
		E = 0.12286,
		L = -0.02938,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 46,
		B = 45,
		E = 45,
		L = 36,
		A = 46,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 6,
	label = "Ethylene_oxide",
	group = 
"""
1 * O2s    u0 {2,S} {3,S}
2   [Cs,N] u0 {1,S} {3,S}
3   [Cs,N] u0 {1,S} {2,S}
""",
	solute = SoluteData(
		S = 0.26498,
		B = -0.00442,
		E = 0.07866,
		L = 0.07046,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 20,
		B = 20,
		E = 22,
		L = 20,
		A = 21,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 7,
	label = "Ethyleneimine",
	group = 
"""
1 * N       u0 {2,S} {3,S}
2   [Cs,N,S]  u0 {1,S} {3,S}
3   [Cs,N,S]  u0 {1,S} {2,S}
""",
	solute = SoluteData(
		S = 0.07140,
		B = -0.02734,
		E = 0.04383,
		L = 0.07610,
		A = 0.00704,
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
	index = 8,
	label = "FourMember",
	group = 
"""
1 * R!H u0 {2,[S,D]} {4,[S,D]}
2   R!H u0 {1,[S,D]} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,[S,D]}
4   R!H u0 {1,[S,D]} {3,[S,D]}
""",
	solute = u'Cyclobutane',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 9,
	label = "Cyclobutane",
	group = 
"""
1 * C  u0 {2,S} {4,S}
2   C  u0 {1,S} {3,S}
3   C  u0 {2,S} {4,S}
4   C  u0 {1,S} {3,S}
""",
	solute = SoluteData(
		S = 0.05047,
		B = 0.00000,
		E = 0.03551,
		L = -0.04096,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 19,
		B = 19,
		E = 20,
		L = 17,
		A = 21,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 10,
	label = "Oxetane",
	group = 
"""
1 * O2s  u0 {2,S} {4,S}
2   C    u0 {1,S} {3,S}
3   C    u0 {2,S} {4,S}
4   C    u0 {1,S} {3,S}
""",
	solute = SoluteData(
		S = 0.07828,
		B = -0.08516,
		E = 0.08708,
		L = 0.21831,
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
	index = 11,
	label = "Beta-Propiolactone",
	group = 
"""
1 * O2s      u0 {2,S} {4,S}
2   C        u0 {1,S} {3,S}
3   C        u0 {2,S} {4,S}
4   [CO,CS]  u0 {1,S} {3,S}
""",
	solute = SoluteData(
		S = 0.03077,
		B = -0.01204,
		E = 0.05842,
		L = 0.00337,
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
	index = 12,
	label = "Azetidine",
	group = 
"""
1 * N       u0 {4,S} {2,S}
2   [Cs,N,O,S]  u0 {1,S} {3,S}
3   [Cs,N,O,S]  u0 {2,S} {4,S}
4   [Cs,N,O,S]  u0 {3,S} {1,S}
""",
	solute = SoluteData(
		S = 0.05099,
		B = -0.02619,
		E = 0.04282,
		L = 0.06247,
		A = 0.02704,
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
	index = 13,
	label = "FiveMember",
	group = 
"""
1 * R!H u0 {2,[S,D,T]} {5,[S,D]}
2   R!H u0 {1,[S,D,T]} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,[S,D]}
4   R!H u0 {3,[S,D]} {5,[S,D,T]}
5   R!H u0 {1,[S,D]} {4,[S,D,T]}
""",
	solute = u'Cyclopentane',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 14,
	label = "five-0double",
	group = 
"""
1 * R!H u0 {2,S} {5,S}
2   R!H u0 {1,S} {3,S}
3   R!H u0 {2,S} {4,S}
4   R!H u0 {3,S} {5,S}
5   R!H u0 {1,S} {4,S}
""",
	solute = SoluteData(
		S = -0.04857,
		B = 0.02233,
		E = 0.10263,
		L = 0.12483,
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
	index = 15,
	label = "Cyclopentane",
	group = 
"""
1 * C  u0 {2,S} {5,S}
2   C  u0 {1,S} {3,S}
3   C  u0 {2,S} {4,S}
4   C  u0 {3,S} {5,S}
5   C  u0 {1,S} {4,S}
""",
	solute = SoluteData(
		S = 0.02389,
		B = 0.00000,
		E = 0.01582,
		L = -0.07917,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 70,
		B = 70,
		E = 75,
		L = 69,
		A = 74,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 16,
	label = "Cyclopentanone",
	group = 
"""
1 * CO  u0 {2,S} {5,S}
2   Cs  u0 {1,S} {3,S}
3   Cs  u0 {2,S} {4,S}
4   Cs  u0 {3,S} {5,S}
5   Cs  u0 {1,S} {4,S}
""",
	solute = SoluteData(
		S = 0.04966,
		B = 0.02069,
		E = 0.00933,
		L = -0.25376,
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
	index = 17,
	label = "Cyclopentanol",
	group = 
"""
1 * Cs       u0 {2,S} {5,S} {6,S}
2   [Cs,Cb]  u0 {1,S} {3,S}
3   [Cs,Cb]  u0 {2,S} {4,S}
4   [Cs,Cb]  u0 {3,S} {5,S}
5   [Cs,Cb]  u0 {1,S} {4,S}
6   O2s		 u0 {1,S} {7,S}
7   H		 u0 {6,S}
""",
	solute = SoluteData(
		S = 0.09449,
		B = 0.11164,
		E = 0.03198,
		L = 0.08964,
		A = -0.00191,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 5,
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
	index = 18,
	label = "methylenecyclopentane",
	group = 
"""
1 * Cd     u0 {2,S} {5,S} {6,D}
2   Cs     u0 {1,S} {3,S}
3   Cs     u0 {2,S} {4,S}
4   Cs     u0 {3,S} {5,S}
5   Cs     u0 {1,S} {4,S}
6   [Cd,N] u0 {1,D}
""",
	solute = SoluteData(
		S = 0.02089,
		B = 0.01448,
		E = 0.02130,
		L = -0.05434,
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
	index = 19,
	label = "Tetrahydrofuran",
	group = 
"""
1 * O  u0 {2,S} {5,S}
2   C  u0 {1,S} {3,S}
3   C  u0 {2,S} {4,S}
4   C  u0 {3,S} {5,S}
5   C  u0 {1,S} {4,S}
""",
	solute = SoluteData(
		S = 0.00107,
		B = 0.02952,
		E = 0.02196,
		L = -0.15476,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 37,
		B = 37,
		E = 39,
		L = 34,
		A = 38,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 20,
	label = "butyrolactone",
	group = 
"""
1   CO   u0 {2,S} {5,S}
2 * O2s  u0 {1,S} {3,S}
3   Cs   u0 {2,S} {4,S}
4   Cs   u0 {3,S} {5,S}
5   Cs   u0 {1,S} {4,S}
""",
	solute = SoluteData(
		S = 0.09798,
		B = 0.13193,
		E = 0.03445,
		L = -0.07526,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 15,
		B = 15,
		E = 16,
		L = 15,
		A = 15,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 21,
	label = "Pyrrolidine",
	group = 
"""
1 * N  u0 {2,S} {5,S}
2   C  u0 {1,S} {3,S}
3   C  u0 {2,S} {4,S}
4   C  u0 {3,S} {5,S}
5   C  u0 {1,S} {4,S}
""",
	solute = u'Pyrrolidine(N-R)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 22,
	label = "Pyrrolidine(N-H)",
	group = 
"""
1 * N  u0 {2,S} {5,S} {6,S}
2   C  u0 {1,S} {3,S}
3   C  u0 {2,S} {4,S}
4   C  u0 {3,S} {5,S}
5   C  u0 {1,S} {4,S}
6   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.11593,
		B = -0.10524,
		E = -0.00262,
		L = 0.06511,
		A = 0.07453,
	),
	dataCount = DataCountGAV(
		S = 9,
		B = 9,
		E = 13,
		L = 13,
		A = 9,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 23,
	label = "Pyrrolidine(N-R)",
	group = 
"""
1 * N    u0 {2,S} {5,S} {6,S}
2   C    u0 {1,S} {3,S}
3   C    u0 {2,S} {4,S}
4   C    u0 {3,S} {5,S}
5   C    u0 {1,S} {4,S}
6   R!H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.02640,
		B = 0.03290,
		E = 0.07170,
		L = -0.06756,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 32,
		B = 32,
		E = 33,
		L = 32,
		A = 32,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 24,
	label = "1,3-Dioxolane",
	group = 
"""
1 * C      u0 {2,S} {5,S}
2   O      u0 {1,S} {3,S}
3   C      u0 {2,S} {4,S}
4   C      u0 {3,S} {5,S}
5   O      u0 {1,S} {4,S}
""",
	solute = SoluteData(
		S = 0.10708,
		B = 0.05187,
		E = 0.03192,
		L = 0.04193,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 12,
		B = 12,
		E = 12,
		L = 11,
		A = 12,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 25,
	label = "thiolane",
	group = 
"""
1 * S u0 {2,S} {5,S}
2   C u0 {1,S} {3,S}
3   C u0 {2,S} {4,S}
4   C u0 {3,S} {5,S}
5   C u0 {1,S} {4,S}
""",
	solute = SoluteData(
		S = 0.00514,
		B = 0.05321,
		E = 0.07800,
		L = 0.04336,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 6,
		B = 6,
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
	index = 26,
	label = "Imidazolidine",
	group = 
"""
1 * N u0 {2,S} {5,S}
2   C u0 {1,S} {3,S}
3   N u0 {2,S} {4,S}
4   C u0 {3,S} {5,S}
5   C u0 {1,S} {4,S}
""",
	solute = u'imidazolidine-2,4-dione',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 27,
	label = "imidazolidine-2,4-dione",
	group = 
"""
1 * N  u0 {2,S} {5,S}
2   CO u0 {1,S} {3,S}
3   N  u0 {2,S} {4,S}
4   C  u0 {3,S} {5,S}
5   CO u0 {1,S} {4,S}
""",
	solute = SoluteData(
		S = 0.11276,
		B = 0.02014,
		E = -0.02176,
		L = 0.13047,
		A = 0.08853,
	),
	dataCount = DataCountGAV(
		S = 17,
		B = 17,
		E = 17,
		L = 10,
		A = 17,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 28,
	label = "five-1double",
	group = 
"""
1 * R!H u0 {2,S} {5,S}
2   R!H u0 {1,S} {3,D}
3   R!H u0 {2,D} {4,S}
4   R!H u0 {3,S} {5,S}
5   R!H u0 {1,S} {4,S}
""",
	solute = SoluteData(
		S = -0.01665,
		B = 0.03634,
		E = 0.05573,
		L = 0.12296,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 6,
		B = 6,
		E = 8,
		L = 5,
		A = 8,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 29,
	label = "Cyclopentene",
	group = 
"""
1 * C  u0 {2,S} {5,S}
2   C  u0 {1,S} {3,D}
3   C  u0 {2,D} {4,S}
4   C  u0 {3,S} {5,S}
5   C  u0 {1,S} {4,S}
""",
	solute = SoluteData(
		S = 0.06054,
		B = 0.00866,
		E = -0.00089,
		L = 0.08210,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 14,
		B = 14,
		E = 15,
		L = 14,
		A = 15,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 30,
	label = "2-pyrroline",
	group = 
"""
1 * N  u0 {2,S} {5,S}
2   C  u0 {1,S} {3,D}
3   C  u0 {2,D} {4,S}
4   C  u0 {3,S} {5,S}
5   C  u0 {1,S} {4,S}
""",
	solute = SoluteData(
		S = 0.02913,
		B = -0.04147,
		E = -0.10757,
		L = 0.04343,
		A = 0.04506,
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
	index = 31,
	label = "3-pyrroline",
	group = 
"""
1 * C  u0 {2,S} {5,S}
2   C  u0 {1,S} {3,D}
3   C  u0 {2,D} {4,S}
4   C  u0 {3,S} {5,S}
5   N  u0 {1,S} {4,S}
""",
	solute = SoluteData(
		S = 0.05384,
		B = -0.10975,
		E = -0.00421,
		L = -0.10537,
		A = 0.03208,
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
	index = 32,
	label = "2-pyrazoline",
	group = 
"""
1 * N  u0 {2,S} {5,S}
2   N  u0 {1,S} {3,D}
3   C  u0 {2,D} {4,S}
4   C  u0 {3,S} {5,S}
5   C  u0 {1,S} {4,S}
""",
	solute = SoluteData(
		S = -0.14489,
		B = -0.03317,
		E = 0.01938,
		L = -0.18258,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 11,
		B = 11,
		E = 12,
		L = 11,
		A = 11,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 33,
	label = "2-imidazoline",
	group = 
"""
1 * N  u0 {2,S} {5,S}
2   C  u0 {1,S} {3,D}
3   N  u0 {2,D} {4,S}
4   C  u0 {3,S} {5,S}
5   C  u0 {1,S} {4,S}
""",
	solute = SoluteData(
		S = 0.15325,
		B = -0.00728,
		E = -0.07526,
		L = 0.24613,
		A = 0.05429,
	),
	dataCount = DataCountGAV(
		S = 6,
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
	index = 34,
	label = "five-N1NC=CC1",
	group = 
"""
1 * N  u0 {2,S} {5,S}
2   C  u0 {1,S} {3,D}
3   C  u0 {2,D} {4,S}
4   C  u0 {3,S} {5,S}
5   N  u0 {1,S} {4,S}
""",
	solute = SoluteData(
		S = 0.02465,
		B = 0.19015,
		E = -0.01792,
		L = 0.29907,
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
	index = 35,
	label = "2,5-Dihydrofuran",
	group = 
"""
1 * C  u0 {2,S} {5,S}
2   C  u0 {1,S} {3,D}
3   C  u0 {2,D} {4,S}
4   C  u0 {3,S} {5,S}
5   O  u0 {1,S} {4,S}
""",
	solute = u'5H-furan-2-one',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 36,
	label = "5H-furan-2-one",
	group = 
"""
1 * C  u0 {2,S} {5,S}
2   C  u0 {1,S} {3,D}
3   C  u0 {2,D} {4,S}
4   CO u0 {3,S} {5,S}
5   O  u0 {1,S} {4,S}
""",
	solute = SoluteData(
		S = 0.14770,
		B = 0.07187,
		E = 0.00883,
		L = 0.27225,
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
	index = 37,
	label = "five-2double",
	group = 
"""
1 * R!H u0 {2,S} {5,S}
2   R!H u0 {1,S} {3,D}
3   R!H u0 {2,D} {4,S}
4   R!H u0 {3,S} {5,D}
5   R!H u0 {1,S} {4,D}
""",
	solute = u'Furan',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 38,
	label = "Cyclopentadiene",
	group = 
"""
1 * C     u0 {2,S} {5,S}
2   Cd    u0 {1,S} {3,D}
3   Cd    u0 {2,D} {4,S}
4   Cd    u0 {3,S} {5,D}
5   Cd    u0 {1,S} {4,D}
""",
	solute = SoluteData(
		S = -0.03717,
		B = -0.01300,
		E = -0.03319,
		L = -0.03893,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 4,
		B = 3,
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
	index = 39,
	label = "Furan",
	group = 
"""
1 * O      u0 {2,S} {5,S}
2   Cd     u0 {1,S} {3,D}
3   Cd     u0 {2,D} {4,S}
4   Cd     u0 {3,S} {5,D}
5   Cd     u0 {1,S} {4,D}
""",
	solute = SoluteData(
		S = 0.02936,
		B = -0.00815,
		E = 0.03637,
		L = 0.26485,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 51,
		B = 50,
		E = 56,
		L = 32,
		A = 61,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 40,
	label = "1H-Pyrrole",
	group = 
"""
1 * N      u0 {2,S} {5,S}
2   Cd     u0 {1,S} {3,D}
3   Cd     u0 {2,D} {4,S}
4   Cd     u0 {3,S} {5,D}
5   Cd     u0 {1,S} {4,D}
""",
	solute = SoluteData(
		S = 0.09574,
		B = -0.05707,
		E = 0.02275,
		L = 0.18058,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 16,
		B = 16,
		E = 17,
		L = 12,
		A = 16,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 41,
	label = "Thiophene",
	group = 
"""
1 * S    u0 {2,S} {5,S}
2   Cd   u0 {1,S} {3,D}
3   Cd   u0 {2,D} {4,S}
4   Cd   u0 {3,S} {5,D}
5   Cd   u0 {1,S} {4,D}
""",
	solute = SoluteData(
		S = -0.00182,
		B = -0.00298,
		E = 0.07126,
		L = 0.14607,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 18,
		B = 18,
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
	index = 42,
	label = "Pyrazole",
	group = 
"""
1 * N      u0 {2,S} {5,S}
2   N      u0 {1,S} {3,D}
3   Cd     u0 {2,D} {4,S}
4   Cd     u0 {3,S} {5,D}
5   Cd     u0 {1,S} {4,D}
""",
	solute = SoluteData(
		S = 0.05857,
		B = -0.04645,
		E = 0.05620,
		L = 0.25672,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 12,
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
	index = 43,
	label = "Imidazole",
	group = 
"""
1 * N      u0 {2,S} {5,S}
2   Cd     u0 {1,S} {3,D}
3   N      u0 {2,D} {4,S}
4   Cd     u0 {3,S} {5,D}
5   Cd     u0 {1,S} {4,D}
""",
	solute = SoluteData(
		S = 0.00875,
		B = 0.01088,
		E = -0.03837,
		L = 0.13736,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 22,
		B = 16,
		E = 22,
		L = 14,
		A = 22,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 44,
	label = "2-Nitroimidazole",
	group = 
"""
1 * N      u0 {2,S} {5,S}
2   Cd     u0 {1,S} {3,D} {6,S}
3   N      u0 {2,D} {4,S}
4   Cd     u0 {3,S} {5,D}
5   Cd     u0 {1,S} {4,D}
6   N5dc   u0 {2,S} {7,D} {8,S}
7   O2d    u0 {6,D}
8   O0sc   u0 {6,S}
""",
	solute = SoluteData(
		S = 0.05294,
		B = -0.00271,
		E = -0.08480,
		L = 0.06636,
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
	index = 45,
	label = "1,2,4-Triazole",
	group = 
"""
1 * N      u0 {2,S} {5,S}
2   N      u0 {1,S} {3,D}
3   Cd     u0 {2,D} {4,S}
4   N      u0 {3,S} {5,D}
5   Cd     u0 {1,S} {4,D}
""",
	solute = SoluteData(
		S = 0.11808,
		B = 0.00069,
		E = 0.01312,
		L = 0.28014,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 22,
		B = 22,
		E = 22,
		L = 20,
		A = 22,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 46,
	label = "Tetrazole",
	group = 
"""
1 * N      u0 {2,S} {5,S}
2   N      u0 {1,S} {3,D}
3   N      u0 {2,D} {4,S}
4   N      u0 {3,S} {5,D}
5   Cd     u0 {1,S} {4,D}
""",
	solute = SoluteData(
		S = -0.02691,
		B = 0.03029,
		E = 0.02081,
		L = 0.14437,
		A = 0.03053,
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
	index = 47,
	label = "2H-Tetrazole",
	group = 
"""
1 * N      u0 {2,S} {5,S}
2   N      u0 {1,S} {3,D}
3   Cd     u0 {2,D} {4,S}
4   N      u0 {3,S} {5,D}
5   N      u0 {1,S} {4,D}
""",
	solute = SoluteData(
		S = 0.18461,
		B = -0.03115,
		E = 0.16165,
		L = 0.61297,
		A = 0.02963,
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
	index = 48,
	label = "Oxazole",
	group = 
"""
1 * O      u0 {2,S} {5,S}
2   Cd     u0 {1,S} {3,D}
3   N      u0 {2,D} {4,S}
4   Cd     u0 {3,S} {5,D}
5   Cd     u0 {1,S} {4,D}
""",
	solute = SoluteData(
		S = 0.03086,
		B = 0.04483,
		E = -0.05703,
		L = 0.06932,
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
	index = 49,
	label = "Isoxazole",
	group = 
"""
1 * O      u0 {2,S} {5,S}
2   N      u0 {1,S} {3,D}
3   Cd     u0 {2,D} {4,S}
4   Cd     u0 {3,S} {5,D}
5   Cd     u0 {1,S} {4,D}
""",
	solute = SoluteData(
		S = 0.09827,
		B = 0.04350,
		E = 0.09967,
		L = 0.45513,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 11,
		B = 11,
		E = 11,
		L = 10,
		A = 11,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 50,
	label = "Thiazole",
	group = 
"""
1 * S      u0 {2,S} {5,S}
2   Cd     u0 {1,S} {3,D}
3   N      u0 {2,D} {4,S}
4   Cd     u0 {3,S} {5,D}
5   Cd     u0 {1,S} {4,D}
""",
	solute = SoluteData(
		S = 0.21117,
		B = 0.01353,
		E = 0.06885,
		L = 0.35218,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 26,
		B = 25,
		E = 31,
		L = 18,
		A = 29,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 51,
	label = "1,2,4-Thiadiazole",
	group = 
"""
1 * S      u0 {2,S} {5,S}
2   N      u0 {1,S} {3,D}
3   Cd     u0 {2,D} {4,S}
4   N      u0 {3,S} {5,D}
5   Cd     u0 {1,S} {4,D}
""",
	solute = SoluteData(
		S = -0.01544,
		B = 0.02840,
		E = 0.10558,
		L = 0.17477,
		A = 0.02649,
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
	index = 52,
	label = "1,3,4-Thiadiazole",
	group = 
"""
1 * S      u0 {2,S} {5,S}
2   Cd     u0 {1,S} {3,D}
3   N      u0 {2,D} {4,S}
4   N      u0 {3,S} {5,D}
5   Cd     u0 {1,S} {4,D}
""",
	solute = SoluteData(
		S = -0.05576,
		B = 0.00184,
		E = 0.01926,
		L = -0.00711,
		A = -0.02186,
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
	index = 53,
	label = "SixMember",
	group = 
"""
1 * R!H u0 {2,[S,D,T]} {6,[S,D]}
2   R!H u0 {1,[S,D,T]} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,[S,D,T]}
4   R!H u0 {3,[S,D,T]} {5,[S,D]}
5   R!H u0 {4,[S,D]} {6,[S,D,T]}
6   R!H u0 {1,[S,D]} {5,[S,D,T]}
""",
	solute = u'Cyclohexane',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 54,
	label = "six-0double",
	group = 
"""
1 * R!H  u0 {2,S} {6,S}
2   R!H  u0 {1,S} {3,S}
3   R!H  u0 {2,S} {4,S}
4   R!H  u0 {3,S} {5,S}
5   R!H  u0 {4,S} {6,S}
6   R!H  u0 {1,S} {5,S}
""",
	solute = SoluteData(
		S = 0.00862,
		B = -0.02503,
		E = 0.00687,
		L = -0.11632,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 5,
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
	index = 55,
	label = "Cyclohexane",
	group = 
"""
1 * C  u0 {2,S} {6,S}
2   C  u0 {1,S} {3,S}
3   C  u0 {2,S} {4,S}
4   C  u0 {3,S} {5,S}
5   C  u0 {4,S} {6,S}
6   C  u0 {1,S} {5,S}
""",
	solute = SoluteData(
		S = 0.02883,
		B = 0.00000,
		E = 0.00866,
		L = -0.03759,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 140,
		B = 128,
		E = 150,
		L = 133,
		A = 150,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 56,
	label = "Cyclohexanone",
	group = 
"""
1 * CO u0 {2,S} {6,S}
2   C  u0 {1,S} {3,S}
3   C  u0 {2,S} {4,S}
4   C  u0 {3,S} {5,S}
5   C  u0 {4,S} {6,S}
6   C  u0 {1,S} {5,S}
""",
	solute = SoluteData(
		S = -0.00752,
		B = -0.01727,
		E = -0.01754,
		L = -0.32084,
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
	index = 57,
	label = "Cyclohexanol",
	group = 
"""
1 * Cs  u0 {2,S} {6,S} {7,S}
2   Cs  u0 {1,S} {3,S}
3   Cs  u0 {2,S} {4,S}
4   Cs  u0 {3,S} {5,S}
5   Cs  u0 {4,S} {6,S}
6   Cs  u0 {1,S} {5,S}
7   O2s u0 {1,S} {8,S}
8   H   u0 {7,S}
""",
	solute = SoluteData(
		S = 0.07636,
		B = 0.04768,
		E = -0.01796,
		L = -0.25025,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 20,
		B = 21,
		E = 27,
		L = 20,
		A = 21,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 58,
	label = "N-Cyclohexylacetamide",
	group = 
"""
1 * Cs  u0 {2,S} {6,S} {7,S}
2   Cs  u0 {1,S} {3,S}
3   Cs  u0 {2,S} {4,S}
4   Cs  u0 {3,S} {5,S}
5   Cs  u0 {4,S} {6,S}
6   Cs  u0 {1,S} {5,S}
7   N3s u0 {1,S} {8,S} {10,S}
8   CO  u0 {7,S} {9,S}
9   Cs  u0 {8,S} {11,S} {12,S} {13,S}
10  H   u0 {7,S}
11  H   u0 {9,S}
12  H   u0 {9,S}
13  H   u0 {9,S}
""",
	solute = SoluteData(
		S = 0.10298,
		B = 0.06161,
		E = -0.06255,
		L = -0.00249,
		A = 0.05654,
	),
	dataCount = DataCountGAV(
		S = 12,
		B = 12,
		E = 14,
		L = 13,
		A = 12,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 59,
	label = "1,3-Dioxane",
	group = 
"""
1   O2s u0 {2,S} {6,S}
2 * Cs u0 {1,S} {3,S}
3   O2s u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {1,S} {5,S}
""",
	solute = SoluteData(
		S = 0.15619,
		B = 0.02040,
		E = 0.03079,
		L = 0.34104,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 6,
		L = 4,
		A = 8,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 60,
	label = "1,4-Dioxane",
	group = 
"""
1   Cs u0 {2,S} {6,S}
2   Cs u0 {1,S} {3,S}
3 * O2s u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   O2s u0 {1,S} {5,S}
""",
	solute = SoluteData(
		S = 0.02654,
		B = -0.00711,
		E = 0.05594,
		L = 0.06724,
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
	index = 61,
	label = "1,3,5-Trioxane",
	group = 
"""
1   Cs u0 {2,S} {6,S}
2   O2s u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4 * O2s u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   O2s u0 {1,S} {5,S}
""",
	solute = SoluteData(
		S = 0.07825,
		B = 0.00203,
		E = -0.03849,
		L = 0.09794,
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
	index = 62,
	label = "Oxane",
	group = 
"""
1 * C   u0 {2,S} {6,S}
2   O2s u0 {1,S} {3,S}
3   C   u0 {2,S} {4,S}
4   C   u0 {3,S} {5,S}
5   C   u0 {4,S} {6,S}
6   C   u0 {1,S} {5,S}
""",
	solute = SoluteData(
		S = -0.05249,
		B = -0.04367,
		E = 0.03659,
		L = -0.08531,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 43,
		B = 43,
		E = 44,
		L = 39,
		A = 44,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 63,
	label = "4-Hydroxyoxan-2-one",
	group = 
"""
1 * CO  u0 {2,S} {6,S}
2   O2s u0 {1,S} {3,S}
3   C   u0 {2,S} {4,S}
4   C   u0 {3,S} {5,S}
5   C   u0 {4,S} {6,S} {7,S}
6   C   u0 {1,S} {5,S}
7   O   u0 {5,S} {8,S}
8   H   u0 {7,S}
""",
	solute = SoluteData(
		S = 0.03292,
		B = 0.02288,
		E = -0.06405,
		L = 0.01672,
		A = 0.02481,
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
	index = 64,
	label = "Piperidine",
	group = 
"""
1 * N  u0 {2,S} {6,S}
2   C  u0 {1,S} {3,S}
3   C  u0 {2,S} {4,S}
4   C  u0 {3,S} {5,S}
5   C  u0 {4,S} {6,S}
6   C  u0 {1,S} {5,S}
""",
	solute = u'Piperidine(N-R)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 65,
	label = "Piperidine(N-H)",
	group = 
"""
1 * N  u0 {2,S} {6,S} {7,S}
2   C  u0 {1,S} {3,S}
3   C  u0 {2,S} {4,S}
4   C  u0 {3,S} {5,S}
5   C  u0 {4,S} {6,S}
6   C  u0 {1,S} {5,S}
7   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.06484,
		B = -0.03563,
		E = 0.03502,
		L = -0.06851,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 21,
		B = 21,
		E = 23,
		L = 18,
		A = 21,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 66,
	label = "Piperidine(N-R)",
	group = 
"""
1 * N   u0 {2,S} {6,S} {7,S}
2   C   u0 {1,S} {3,S}
3   C   u0 {2,S} {4,S}
4   C   u0 {3,S} {5,S}
5   C   u0 {4,S} {6,S}
6   C   u0 {1,S} {5,S}
7   R!H u0 {1,S}
""",
	solute = SoluteData(
		S = 0.00587,
		B = 0.04542,
		E = 0.03765,
		L = 0.07983,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 53,
		B = 53,
		E = 54,
		L = 47,
		A = 53,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 67,
	label = "1-Piperidinecarboxaldehyde",
	group = 
"""
1 * N   u0 {2,S} {6,S} {7,S}
2   C   u0 {1,S} {3,S}
3   C   u0 {2,S} {4,S}
4   C   u0 {3,S} {5,S}
5   C   u0 {4,S} {6,S}
6   C   u0 {1,S} {5,S}
7   CO  u0 {1,S}
""",
	solute = SoluteData(
		S = -0.06312,
		B = 0.15569,
		E = -0.01468,
		L = -0.07140,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 6,
		B = 6,
		E = 8,
		L = 4,
		A = 10,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 68,
	label = "Piperidine-2,6-dione",
	group = 
"""
1 * N   u0 {2,S} {6,S} {7,S}
2   CO  u0 {1,S} {3,S}
3   C   u0 {2,S} {4,S}
4   C   u0 {3,S} {5,S}
5   C   u0 {4,S} {6,S}
6   CO  u0 {1,S} {5,S}
7   R!H u0 {1,S}
""",
	solute = SoluteData(
		S = -0.06255,
		B = -0.11688,
		E = -0.04693,
		L = -0.34557,
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
	index = 69,
	label = "Piperazine",
	group = 
"""
1 * N   u0 {2,S} {6,S}
2   C   u0 {1,S} {3,S}
3   C   u0 {2,S} {4,S}
4   N   u0 {3,S} {5,S}
5   C   u0 {4,S} {6,S}
6   C   u0 {1,S} {5,S}
""",
	solute = u'Piperazine(N-R,N-R)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 70,
	label = "Piperazine(N-H,N-H)",
	group = 
"""
1 * N   u0 {2,S} {6,S} {7,S}
2   C   u0 {1,S} {3,S}
3   C   u0 {2,S} {4,S}
4   N   u0 {3,S} {5,S} {8,S}
5   C   u0 {4,S} {6,S}
6   C   u0 {1,S} {5,S}
7   H   u0 {1,S}
8   H   u0 {4,S}
""",
	solute = SoluteData(
		S = 0.06403,
		B = 0.01781,
		E = 0.02413,
		L = 0.10650,
		A = 0.04340,
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
	index = 71,
	label = "Piperazine(N-H,N-R)",
	group = 
"""
1 * N   u0 {2,S} {6,S} {7,S}
2   C   u0 {1,S} {3,S}
3   C   u0 {2,S} {4,S}
4   N   u0 {3,S} {5,S} {8,S}
5   C   u0 {4,S} {6,S}
6   C   u0 {1,S} {5,S}
7   H   u0 {1,S}
8   R!H u0 {4,S}
""",
	solute = SoluteData(
		S = -0.04453,
		B = 0.07822,
		E = -0.00584,
		L = -0.01954,
		A = 0.02095,
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
	index = 72,
	label = "Piperazine(N-R,N-R)",
	group = 
"""
1 * N   u0 {2,S} {6,S} {7,S}
2   C   u0 {1,S} {3,S}
3   C   u0 {2,S} {4,S}
4   N   u0 {3,S} {5,S} {8,S}
5   C   u0 {4,S} {6,S}
6   C   u0 {1,S} {5,S}
7   R!H u0 {1,S}
8   R!H u0 {4,S}
""",
	solute = SoluteData(
		S = -0.16121,
		B = -0.01928,
		E = 0.01774,
		L = -0.01659,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 44,
		B = 44,
		E = 46,
		L = 42,
		A = 45,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 73,
	label = "Morpholine",
	group = 
"""
1 * N   u0 {2,S} {6,S}
2   C   u0 {1,S} {3,S}
3   C   u0 {2,S} {4,S}
4   O   u0 {3,S} {5,S}
5   C   u0 {4,S} {6,S}
6   C   u0 {1,S} {5,S}
""",
	solute = u'Morpholine(N-R)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 74,
	label = "Morpholine(N-H)",
	group = 
"""
1 * N   u0 {2,S} {6,S} {7,S}
2   C   u0 {1,S} {3,S}
3   C   u0 {2,S} {4,S}
4   O   u0 {3,S} {5,S}
5   C   u0 {4,S} {6,S}
6   C   u0 {1,S} {5,S}
7   H   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.01327,
		B = -0.06638,
		E = -0.07542,
		L = -0.03160,
		A = 0.04649,
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
	index = 75,
	label = "Morpholine(N-R)",
	group = 
"""
1 * N   u0 {2,S} {6,S} {7,S}
2   C   u0 {1,S} {3,S}
3   C   u0 {2,S} {4,S}
4   O   u0 {3,S} {5,S}
5   C   u0 {4,S} {6,S}
6   C   u0 {1,S} {5,S}
7   R!H u0 {1,S}
""",
	solute = SoluteData(
		S = 0.05837,
		B = -0.04950,
		E = 0.05420,
		L = -0.09903,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 9,
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
	index = 76,
	label = "1,3-Diazinane",
	group = 
"""
1 * N   u0 {2,S} {6,S}
2   C   u0 {1,S} {3,S}
3   N   u0 {2,S} {4,S}
4   C   u0 {3,S} {5,S}
5   C   u0 {4,S} {6,S}
6   C   u0 {1,S} {5,S}
""",
	solute = u'1,3-Diazinane-2,4,6-trione',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 77,
	label = "1,3-Diazinane-2,4,6-trione",
	group = 
"""
1 * N   u0 {2,S} {6,S}
2   CO  u0 {1,S} {3,S}
3   N   u0 {2,S} {4,S}
4   CO  u0 {3,S} {5,S}
5   C   u0 {4,S} {6,S}
6   CO  u0 {1,S} {5,S}
""",
	solute = SoluteData(
		S = -0.09205,
		B = 0.15211,
		E = 0.10004,
		L = -0.02775,
		A = 0.04082,
	),
	dataCount = DataCountGAV(
		S = 56,
		B = 56,
		E = 57,
		L = 15,
		A = 56,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 78,
	label = "2-Sulfanylidene-1,3-diazinane-4,6-dione",
	group = 
"""
1 * N   u0 {2,S} {6,S}
2   CS  u0 {1,S} {3,S}
3   N   u0 {2,S} {4,S}
4   CO  u0 {3,S} {5,S}
5   C   u0 {4,S} {6,S}
6   CO  u0 {1,S} {5,S}
""",
	solute = SoluteData(
		S = -0.03277,
		B = 0.00993,
		E = 0.03043,
		L = 0.09017,
		A = 0.03900,
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
	index = 79,
	label = "1,3,5-Triazinane",
	group = 
"""
1 * N   u0 {2,S} {6,S}
2   C   u0 {1,S} {3,S}
3   N   u0 {2,S} {4,S}
4   C   u0 {3,S} {5,S}
5   N   u0 {4,S} {6,S}
6   C   u0 {1,S} {5,S}
""",
	solute = SoluteData(
		S = 0.04044,
		B = -0.09095,
		E = 0.00405,
		L = 0.13839,
		A = 0.16025,
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
	index = 80,
	label = "1,3,2-Dioxaphosphorinane",
	group = 
"""
1 * P   u0 {2,S} {6,S}
2   O   u0 {1,S} {3,S}
3   C   u0 {2,S} {4,S}
4   C   u0 {3,S} {5,S}
5   C   u0 {4,S} {6,S}
6   O   u0 {1,S} {5,S}
""",
	solute = u'1,3,2-Dioxaphosphorinane-2-oxide',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 81,
	label = "1,3,2-Dioxaphosphorinane-2-oxide",
	group = 
"""
1 * P5d u0 {2,S} {6,S} {7,D}
2   O   u0 {1,S} {3,S}
3   C   u0 {2,S} {4,S}
4   C   u0 {3,S} {5,S}
5   C   u0 {4,S} {6,S}
6   O   u0 {1,S} {5,S}
7   O2d u0 {1,D}
""",
	solute = SoluteData(
		S = 0.28243,
		B = -0.10632,
		E = 0.11941,
		L = 0.68994,
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
	index = 82,
	label = "six-1double",
	group = 
"""
1   R!H  u0 {2,S} {6,S}
2 * R!H  u0 {1,S} {3,D}
3   R!H  u0 {2,D} {4,S}
4   R!H  u0 {3,S} {5,S}
5   R!H  u0 {4,S} {6,S}
6   R!H  u0 {1,S} {5,S}
""",
	solute = SoluteData(
		S = -0.06432,
		B = 0.05672,
		E = 0.07427,
		L = 0.23213,
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
	index = 83,
	label = "Cyclohexene",
	group = 
"""
1   C  u0 {2,S} {6,S}
2   C  u0 {1,S} {3,S}
3 * Cd u0 {2,S} {4,D}
4   Cd u0 {3,D} {5,S}
5   C  u0 {4,S} {6,S}
6   C  u0 {1,S} {5,S}
""",
	solute = SoluteData(
		S = 0.02591,
		B = 0.00923,
		E = 0.00877,
		L = 0.06028,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 66,
		B = 54,
		E = 67,
		L = 58,
		A = 67,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 84,
	label = "Tetrahydropyrimidine",
	group = 
"""
1   N  u0 {2,S} {6,S}
2   C  u0 {1,S} {3,S}
3 * Cd u0 {2,S} {4,D}
4   Cd u0 {3,D} {5,S}
5   N  u0 {4,S} {6,S}
6   C  u0 {1,S} {5,S}
""",
	solute = u'Uracil',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 85,
	label = "Uracil",
	group = 
"""
1   N  u0 {2,S} {6,S}
2   CO u0 {1,S} {3,S}
3 * Cd u0 {2,S} {4,D}
4   Cd u0 {3,D} {5,S}
5   N  u0 {4,S} {6,S}
6   CO u0 {1,S} {5,S}
""",
	solute = SoluteData(
		S = 0.06262,
		B = 0.00158,
		E = -0.00151,
		L = 0.04941,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 60,
		B = 60,
		E = 63,
		L = 55,
		A = 61,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 86,
	label = "1,2,3,6-Tetrahydropyridine",
	group = 
"""
1   N   u0 {2,S} {6,S}
2   C   u0 {1,S} {3,S}
3 * Cd  u0 {2,S} {4,D}
4   Cd  u0 {3,D} {5,S}
5   C   u0 {4,S} {6,S}
6   C   u0 {1,S} {5,S}
""",
	solute = SoluteData(
		S = -0.00389,
		B = -0.03247,
		E = 0.07600,
		L = 0.10213,
		A = 0.00315,
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
	index = 87,
	label = "1,4,5,6-Tetrahydropyridazine",
	group = 
"""
1   C   u0 {2,S} {6,S}
2   N3s u0 {1,S} {3,S}
3 * N3d u0 {2,S} {4,D}
4   Cd  u0 {3,D} {5,S}
5   C   u0 {4,S} {6,S}
6   C   u0 {1,S} {5,S}
""",
	solute = u'4,5-Dihydro-2H-pyridazin-3-one',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 88,
	label = "4,5-Dihydro-2H-pyridazin-3-one",
	group = 
"""
1   CO  u0 {2,S} {6,S}
2   N3s u0 {1,S} {3,S}
3 * N3d u0 {2,S} {4,D}
4   Cd  u0 {3,D} {5,S}
5   C   u0 {4,S} {6,S}
6   C   u0 {1,S} {5,S}
""",
	solute = SoluteData(
		S = -0.02390,
		B = 0.00677,
		E = 0.01159,
		L = -0.10729,
		A = 0.06687,
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
	index = 89,
	label = "six-2double-1,3",
	group = 
"""
1 * R!H  u0 {2,S} {6,S}
2   R!H  u0 {1,S} {3,D}
3   R!H  u0 {2,D} {4,S}
4   R!H  u0 {3,S} {5,D}
5   R!H  u0 {4,D} {6,S}
6   R!H  u0 {1,S} {5,S}
""",
	solute = u'1,3-Cyclohexadiene',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 90,
	label = "1,3-Cyclohexadiene",
	group = 
"""
1 * C   u0 {2,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cd  u0 {2,D} {4,S}
4   Cd  u0 {3,S} {5,D}
5   Cd  u0 {4,D} {6,S}
6   C   u0 {1,S} {5,S}
""",
	solute = SoluteData(
		S = -0.03540,
		B = 0.00316,
		E = 0.04465,
		L = 0.10760,
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
	index = 91,
	label = "1,2-Dihydropyridine",
	group = 
"""
1 * N   u0 {2,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cd  u0 {2,D} {4,S}
4   Cd  u0 {3,S} {5,D}
5   Cd  u0 {4,D} {6,S}
6   C   u0 {1,S} {5,S}
""",
	solute = SoluteData(
		S = 0.02281,
		B = 0.07135,
		E = -0.05827,
		L = -0.03410,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 6,
		B = 5,
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
	index = 92,
	label = "2,3-Dihydropyridine",
	group = 
"""
1 * C   u0 {2,S} {6,S}
2   N   u0 {1,S} {3,D}
3   Cd  u0 {2,D} {4,S}
4   Cd  u0 {3,S} {5,D}
5   Cd  u0 {4,D} {6,S}
6   C   u0 {1,S} {5,S}
""",
	solute = u'1,2-Dihydropyridine',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 93,
	label = "1,2-Dihydropyrimidine",
	group = 
"""
1 * N   u0 {2,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cd  u0 {2,D} {4,S}
4   Cd  u0 {3,S} {5,D}
5   N   u0 {4,D} {6,S}
6   C   u0 {1,S} {5,S}
""",
	solute = u'1H-Pyrimidin-2-one',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 94,
	label = "1H-Pyrimidin-2-one",
	group = 
"""
1 * N   u0 {2,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cd  u0 {2,D} {4,S}
4   Cd  u0 {3,S} {5,D}
5   N   u0 {4,D} {6,S}
6   CO  u0 {1,S} {5,S}
""",
	solute = SoluteData(
		S = 0.00569,
		B = 0.08118,
		E = 0.03568,
		L = -0.16033,
		A = -0.03955,
	),
	dataCount = DataCountGAV(
		S = 7,
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
	index = 95,
	label = "N1C=NC=CC1",
	group = 
"""
1 * N   u0 {2,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   N   u0 {2,D} {4,S}
4   Cd  u0 {3,S} {5,D}
5   Cd  u0 {4,D} {6,S}
6   C   u0 {1,S} {5,S}
""",
	solute = u'3H-Pyrimidin-4-one',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 96,
	label = "3H-Pyrimidin-4-one",
	group = 
"""
1 * N   u0 {2,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   N   u0 {2,D} {4,S}
4   Cd  u0 {3,S} {5,D}
5   Cd  u0 {4,D} {6,S}
6   CO  u0 {1,S} {5,S}
""",
	solute = SoluteData(
		S = 0.06823,
		B = -0.01484,
		E = 0.05632,
		L = 0.10899,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 7,
		B = 5,
		E = 7,
		L = 2,
		A = 7,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 97,
	label = "six-2double-1,4",
	group = 
"""
1 * R!H  u0 {2,S} {6,S}
2   R!H  u0 {1,S} {3,D}
3   R!H  u0 {2,D} {4,S}
4   R!H  u0 {3,S} {5,S}
5   R!H  u0 {4,S} {6,D}
6   R!H  u0 {1,S} {5,D}
""",
	solute = u'1,4-Dihydropyridine',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 98,
	label = "1,4-Cyclohexadiene",
	group = 
"""
1 * C  u0 {2,S} {6,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   C  u0 {3,S} {5,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
	solute = SoluteData(
		S = 0.01625,
		B = 0.01045,
		E = 0.04315,
		L = 0.22985,
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
	index = 99,
	label = "p-Benzoquinone",
	group = 
"""
1 * CO  u0 {2,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cd  u0 {2,D} {4,S}
4   CO  u0 {3,S} {5,S}
5   Cd  u0 {4,S} {6,D}
6   Cd  u0 {1,S} {5,D}
""",
	solute = SoluteData(
		S = -0.26091,
		B = -0.05845,
		E = 0.02068,
		L = -0.29764,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 8,
		B = 8,
		E = 8,
		L = 8,
		A = 11,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 100,
	label = "1,4-Dihydropyridine",
	group = 
"""
1 * N  u0 {2,S} {6,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   C  u0 {3,S} {5,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
	solute = SoluteData(
		S = -0.02787,
		B = -0.01409,
		E = 0.01803,
		L = 0.30997,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 15,
		B = 15,
		E = 15,
		L = 14,
		A = 15,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 101,
	label = "3,4-Dihydroxypyridine",
	group = 
"""
1 * N   u0 {2,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cd  u0 {2,D} {4,S} {7,S}
4   CO  u0 {3,S} {5,S}
5   Cd  u0 {4,S} {6,D}
6   Cd  u0 {1,S} {5,D}
7   O2s u0 {3,S} {8,S}
8   H   u0 {7,S}
""",
	solute = SoluteData(
		S = 0.07515,
		B = 0.11103,
		E = 0.01227,
		L = 0.01058,
		A = 0.11713,
	),
	dataCount = DataCountGAV(
		S = 18,
		B = 18,
		E = 18,
		L = 1,
		A = 18,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 102,
	label = "4H-Pyran",
	group = 
"""
1 * O  u0 {2,S} {6,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   C  u0 {3,S} {5,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
	solute = SoluteData(
		S = 0.03439,
		B = 0.00080,
		E = 0.08281,
		L = 0.23859,
		A = 0.10000,
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
	index = 103,
	label = "3-Hydroxypyran-4-one",
	group = 
"""
1 * O  u0 {2,S} {6,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   CO u0 {3,S} {5,S}
5   Cd u0 {4,S} {6,D} {7,S}
6   Cd u0 {1,S} {5,D}
7   O  u0 {5,S} {8,S}
8   H  u0 {7,S}
""",
	solute = SoluteData(
		S = 0.04191,
		B = 0.02863,
		E = 0.08525,
		L = 0.30922,
		A = 0.09491,
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
	index = 104,
	label = "six-3double",
	group = 
"""
1 * R!H  u0 {2,D} {6,S}
2   R!H  u0 {1,D} {3,S}
3   R!H  u0 {2,S} {4,D}
4   R!H  u0 {3,D} {5,S}
5   R!H  u0 {4,S} {6,D}
6   R!H  u0 {1,S} {5,D}
""",
	solute = u'Pyridine',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 105,
	label = "Pyridine",
	group = 
"""
1 * N   u0 {2,D} {6,S}
2   C   u0 {1,D} {3,S}
3   C   u0 {2,S} {4,D}
4   C   u0 {3,D} {5,S}
5   C   u0 {4,S} {6,D}
6   C   u0 {1,S} {5,D}
""",
	solute = SoluteData(
		S = -0.04652,
		B = 0.06745,
		E = -0.04982,
		L = -0.00812,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 202,
		B = 151,
		E = 232,
		L = 184,
		A = 226,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 106,
	label = "Pyridine-N-oxide",
	group = 
"""
1 * N5dc  u0 {2,D} {6,S} {7,S}
2   C     u0 {1,D} {3,S}
3   C     u0 {2,S} {4,D}
4   C     u0 {3,D} {5,S}
5   C     u0 {4,S} {6,D}
6   C     u0 {1,S} {5,D}
7   O0sc  u0 {1,S}
""",
	solute = SoluteData(
		S = -0.01816,
		B = 0.10560,
		E = 0.06933,
		L = 0.08089,
		A = 0.07458,
	),
	dataCount = DataCountGAV(
		S = 13,
		B = 13,
		E = 13,
		L = 13,
		A = 13,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 107,
	label = "Isonicotinamide",
	group = 
"""
1 * N   u0 {2,D} {6,S}
2   C   u0 {1,D} {3,S}
3   C   u0 {2,S} {4,D}
4   C   u0 {3,D} {5,S} {7,S}
5   C   u0 {4,S} {6,D}
6   C   u0 {1,S} {5,D}
7   CO  u0 {4,S} {8,S}
8   N3s u0 {7,S}
""",
	solute = SoluteData(
		S = 0.00166,
		B = 0.04407,
		E = -0.03798,
		L = 0.06717,
		A = 0.18332,
	),
	dataCount = DataCountGAV(
		S = 35,
		B = 35,
		E = 35,
		L = 35,
		A = 35,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 108,
	label = "NicotinicAcidEster",
	group = 
"""
1 * N   u0 {2,D} {6,S}
2   C   u0 {1,D} {3,S}
3   C   u0 {2,S} {4,D}
4   C   u0 {3,D} {5,S}
5   C   u0 {4,S} {6,D} {7,S}
6   C   u0 {1,S} {5,D}
7   CO  u0 {5,S} {8,S}
8   O2s u0 {7,S}
""",
	solute = SoluteData(
		S = -0.07264,
		B = 0.00023,
		E = -0.04917,
		L = -0.08813,
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
	index = 109,
	label = "Pyridazine",
	group = 
"""
1 * N   u0 {2,D} {6,S}
2   C   u0 {1,D} {3,S}
3   C   u0 {2,S} {4,D}
4   C   u0 {3,D} {5,S}
5   C   u0 {4,S} {6,D}
6   N   u0 {1,S} {5,D}
""",
	solute = SoluteData(
		S = 0.11794,
		B = -0.01258,
		E = 0.03256,
		L = 0.23892,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 5,
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
	index = 110,
	label = "Pyrimidine",
	group = 
"""
1 * N   u0 {2,D} {6,S}
2   C   u0 {1,D} {3,S}
3   C   u0 {2,S} {4,D}
4   C   u0 {3,D} {5,S}
5   N   u0 {4,S} {6,D}
6   C   u0 {1,S} {5,D}
""",
	solute = SoluteData(
		S = 0.06005,
		B = 0.01742,
		E = -0.01599,
		L = 0.02219,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 44,
		B = 45,
		E = 47,
		L = 42,
		A = 49,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 111,
	label = "Pyrazine",
	group = 
"""
1 * N   u0 {2,D} {6,S}
2   C   u0 {1,D} {3,S}
3   C   u0 {2,S} {4,D}
4   N   u0 {3,D} {5,S}
5   C   u0 {4,S} {6,D}
6   C   u0 {1,S} {5,D}
""",
	solute = SoluteData(
		S = 0.04189,
		B = -0.02262,
		E = -0.10548,
		L = -0.00391,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 45,
		B = 45,
		E = 52,
		L = 31,
		A = 53,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 112,
	label = "1,3,5-Triazine",
	group = 
"""
1 * N   u0 {2,D} {6,S}
2   C   u0 {1,D} {3,S}
3   N   u0 {2,S} {4,D}
4   C   u0 {3,D} {5,S}
5   N   u0 {4,S} {6,D}
6   C   u0 {1,S} {5,D}
""",
	solute = u'2-Methylsulfanyl-1,3,5-triazine',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 113,
	label = "2-Methylsulfanyl-1,3,5-triazine",
	group = 
"""
1 * N   u0 {2,D} {6,S}
2   C   u0 {1,D} {3,S} {7,S}
3   N   u0 {2,S} {4,D}
4   C   u0 {3,D} {5,S}
5   N   u0 {4,S} {6,D}
6   C   u0 {1,S} {5,D}
7   S2s u0 {2,S} {8,S}
8   Cs  u0 {7,S}
""",
	solute = SoluteData(
		S = 0.02772,
		B = 0.00427,
		E = -0.04375,
		L = -0.04546,
		A = -0.06201,
	),
	dataCount = DataCountGAV(
		S = 15,
		B = 15,
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
	index = 114,
	label = "2-Methoxy-1,3,5-triazine",
	group = 
"""
1 * N   u0 {2,D} {6,S}
2   C   u0 {1,D} {3,S} {7,S}
3   N   u0 {2,S} {4,D}
4   C   u0 {3,D} {5,S}
5   N   u0 {4,S} {6,D}
6   C   u0 {1,S} {5,D}
7   O2s u0 {2,S} {8,S}
8   Cs  u0 {7,S}
""",
	solute = SoluteData(
		S = -0.04153,
		B = 0.06045,
		E = -0.05898,
		L = -0.00615,
		A = -0.02708,
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
	index = 115,
	label = "SevenMember",
	group = 
"""
1 * R!H u0 {2,[S,D,T]} {7,[S,D]}
2   R!H u0 {1,[S,D,T]} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,[S,D]}
4   R!H u0 {3,[S,D]} {5,[S,D]}
5   R!H u0 {4,[S,D]} {6,[S,D]}
6   R!H u0 {5,[S,D]} {7,[S,D]}
7   R!H u0 {1,[S,D]} {6,[S,D]}
""",
	solute = u'Cycloheptane',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 116,
	label = "seven-0double",
	group = 
"""
1 * R!H u0 {2,S} {7,S}
2   R!H u0 {1,S} {3,S}
3   R!H u0 {2,S} {4,S}
4   R!H u0 {3,S} {5,S}
5   R!H u0 {4,S} {6,S}
6   R!H u0 {5,S} {7,S}
7   R!H u0 {1,S} {6,S}
""",
	solute = SoluteData(
		S = 0.03666,
		B = 0.06054,
		E = -0.01122,
		L = 0.17728,
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
	index = 117,
	label = "Cycloheptane",
	group = 
"""
1 * C  u0 {2,S} {7,S}
2   C  u0 {1,S} {3,S}
3   C  u0 {2,S} {4,S}
4   C  u0 {3,S} {5,S}
5   C  u0 {4,S} {6,S}
6   C  u0 {5,S} {7,S}
7   C  u0 {1,S} {6,S}
""",
	solute = SoluteData(
		S = 0.03156,
		B = 0.00000,
		E = 0.03666,
		L = -0.02859,
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
	index = 118,
	label = "Oxepane",
	group = 
"""
1 * O2s u0 {2,S} {7,S}
2   C   u0 {1,S} {3,S}
3   C   u0 {2,S} {4,S}
4   C   u0 {3,S} {5,S}
5   C   u0 {4,S} {6,S}
6   C   u0 {5,S} {7,S}
7   C   u0 {1,S} {6,S}
""",
	solute = SoluteData(
		S = 0.00354,
		B = 0.14608,
		E = -0.06788,
		L = 0.10552,
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
	index = 119,
	label = "seven-0double_N",
	group = 
"""
1 * N  u0 {2,S} {7,S}
2   C  u0 {1,S} {3,S}
3   C  u0 {2,S} {4,S}
4   C  u0 {3,S} {5,S}
5   C  u0 {4,S} {6,S}
6   C  u0 {5,S} {7,S}
7   C  u0 {1,S} {6,S}
""",
	solute = SoluteData(
		S = -0.05043,
		B = 0.06559,
		E = 0.02447,
		L = -0.02088,
		A = 0.00598,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 5,
		E = 6,
		L = 4,
		A = 5,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 120,
	label = "seven-1double",
	group = 
"""
1 * R!H u0 {2,S} {7,S}
2   R!H u0 {1,S} {3,S}
3   R!H u0 {2,S} {4,S}
4   R!H u0 {3,S} {5,D}
5   R!H u0 {4,D} {6,S}
6   R!H u0 {5,S} {7,S}
7   R!H u0 {1,S} {6,S}
""",
	solute = SoluteData(
		S = -0.13718,
		B = -0.04473,
		E = -0.08816,
		L = -0.29254,
		A = -0.00069,
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
	index = 121,
	label = "Cycloheptene",
	group = 
"""
1 * C  u0 {2,S} {7,S}
2   C  u0 {1,S} {3,S}
3   C  u0 {2,S} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   C  u0 {5,S} {7,S}
7   C  u0 {1,S} {6,S}
""",
	solute = SoluteData(
		S = -0.01654,
		B = 0.01326,
		E = -0.00236,
		L = 0.05312,
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
	index = 122,
	label = "seven-2double-1,3",
	group = 
"""
1 * R!H u0 {2,S} {7,S}
2   R!H u0 {1,S} {3,S}
3   R!H u0 {2,S} {4,D}
4   R!H u0 {3,D} {5,S}
5   R!H u0 {4,S} {6,D}
6   R!H u0 {5,D} {7,S}
7   R!H u0 {1,S} {6,S}
""",
	solute = SoluteData(
		S = 0.03404,
		B = -0.03575,
		E = 0.03007,
		L = 0.05843,
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
	index = 123,
	label = "seven-3double-1,3,5",
	group = 
"""
1 * R!H u0 {2,S} {7,S}
2   R!H u0 {1,S} {3,D}
3   R!H u0 {2,D} {4,S}
4   R!H u0 {3,S} {5,D}
5   R!H u0 {4,D} {6,S}
6   R!H u0 {5,S} {7,D}
7   R!H u0 {1,S} {6,D}
""",
	solute = u'1,3,5-Cycloheptatriene',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 124,
	label = "1,3,5-Cycloheptatriene",
	group = 
"""
1 * C  u0 {2,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cd u0 {5,S} {7,D}
7   Cd u0 {1,S} {6,D}
""",
	solute = SoluteData(
		S = 0.05462,
		B = 0.00045,
		E = 0.00191,
		L = 0.11308,
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
	index = 125,
	label = "EightMember",
	group = 
"""
1 * R!H u0 {2,[S,D]} {8,[S,D]}
2   R!H u0 {1,[S,D]} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,[S,D]}
4   R!H u0 {3,[S,D]} {5,[S,D]}
5   R!H u0 {4,[S,D]} {6,[S,D]}
6   R!H u0 {5,[S,D]} {7,[S,D]}
7   R!H u0 {6,[S,D]} {8,[S,D]}
8   R!H u0 {1,[S,D]} {7,[S,D]}
""",
	solute = u'Cyclooctane',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 126,
	label = "eight-0double",
	group = 
"""
1 * R!H u0 {2,S} {8,S}
2   R!H u0 {1,S} {3,S}
3   R!H u0 {2,S} {4,S}
4   R!H u0 {3,S} {5,S}
5   R!H u0 {4,S} {6,S}
6   R!H u0 {5,S} {7,S}
7   R!H u0 {6,S} {8,S}
8   R!H u0 {1,S} {7,S}
""",
	solute = u'Cyclooctane',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 127,
	label = "Cyclooctane",
	group = 
"""
1 * C  u0 {2,S} {8,S}
2   C  u0 {1,S} {3,S}
3   C  u0 {2,S} {4,S}
4   C  u0 {3,S} {5,S}
5   C  u0 {4,S} {6,S}
6   C  u0 {5,S} {7,S}
7   C  u0 {6,S} {8,S}
8   C  u0 {1,S} {7,S}
""",
	solute = SoluteData(
		S = -0.08204,
		B = 0.00000,
		E = -0.03351,
		L = -0.04409,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 15,
		B = 15,
		E = 15,
		L = 14,
		A = 15,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 128,
	label = "Azocane",
	group = 
"""
1 * N  u0 {2,S} {8,S}
2   C  u0 {1,S} {3,S}
3   C  u0 {2,S} {4,S}
4   C  u0 {3,S} {5,S}
5   C  u0 {4,S} {6,S}
6   C  u0 {5,S} {7,S}
7   C  u0 {6,S} {8,S}
8   C  u0 {1,S} {7,S}
""",
	solute = SoluteData(
		S = 0.04326,
		B = 0.01385,
		E = -0.00953,
		L = 0.00592,
		A = -0.00529,
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
	index = 129,
	label = "Octasulfur",
	group = 
"""
1 * S2s u0 {2,S} {8,S}
2   S2s u0 {1,S} {3,S}
3   S2s u0 {2,S} {4,S}
4   S2s u0 {3,S} {5,S}
5   S2s u0 {4,S} {6,S}
6   S2s u0 {5,S} {7,S}
7   S2s u0 {6,S} {8,S}
8   S2s u0 {1,S} {7,S}
""",
	solute = SoluteData(
		S = 0.01041,
		B = 0.00000,
		E = 0.01201,
		L = 0.07767,
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
	index = 130,
	label = "eight-1double",
	group = 
"""
1 * R!H  u0 {2,D} {8,S}
2   R!H  u0 {1,D} {3,S}
3   R!H  u0 {2,S} {4,S}
4   R!H  u0 {3,S} {5,S}
5   R!H  u0 {4,S} {6,S}
6   R!H  u0 {5,S} {7,S}
7   R!H  u0 {6,S} {8,S}
8   R!H  u0 {1,S} {7,S}
""",
	solute = u'Cyclooctene',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 131,
	label = "Cyclooctene",
	group = 
"""
1 * Cd u0 {2,D} {8,S}
2   Cd u0 {1,D} {3,S}
3   C  u0 {2,S} {4,S}
4   C  u0 {3,S} {5,S}
5   C  u0 {4,S} {6,S}
6   C  u0 {5,S} {7,S}
7   C  u0 {6,S} {8,S}
8   C  u0 {1,S} {7,S}
""",
	solute = SoluteData(
		S = -0.00706,
		B = 0.00243,
		E = 0.01477,
		L = 0.05954,
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
	index = 132,
	label = "eight-2double-1,3",
	group = 
"""
1 * R!H u0 {2,D} {8,S}
2   R!H u0 {1,D} {3,S}
3   R!H u0 {2,S} {4,D}
4   R!H u0 {3,D} {5,S}
5   R!H u0 {4,S} {6,S}
6   R!H u0 {5,S} {7,S}
7   R!H u0 {6,S} {8,S}
8   R!H u0 {1,S} {7,S}
""",
	solute = u'1,3-cyclooctadiene',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 133,
	label = "1,3-cyclooctadiene",
	group = 
"""
1 * Cd u0 {2,D} {8,S}
2   Cd u0 {1,D} {3,S}
3   Cd u0 {2,S} {4,D}
4   Cd u0 {3,D} {5,S}
5   C  u0 {4,S} {6,S}
6   C  u0 {5,S} {7,S}
7   C  u0 {6,S} {8,S}
8   C  u0 {1,S} {7,S}
""",
	solute = u'1,5-cyclooctadiene',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 134,
	label = "eight-2double-1,5",
	group = 
"""
1 * R!H u0 {2,D} {8,S}
2   R!H u0 {1,D} {3,S}
3   R!H u0 {2,S} {4,S}
4   R!H u0 {3,S} {5,S}
5   R!H u0 {4,S} {6,D}
6   R!H u0 {5,D} {7,S}
7   R!H u0 {6,S} {8,S}
8   R!H u0 {1,S} {7,S}
""",
	solute = u'1,5-cyclooctadiene',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 135,
	label = "1,5-cyclooctadiene",
	group = 
"""
1 * Cd u0 {2,D} {8,S}
2   Cd u0 {1,D} {3,S}
3   C  u0 {2,S} {4,S}
4   C  u0 {3,S} {5,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {5,D} {7,S}
7   C  u0 {6,S} {8,S}
8   C  u0 {1,S} {7,S}
""",
	solute = SoluteData(
		S = 0.00474,
		B = -0.00024,
		E = 0.01211,
		L = 0.01926,
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
	index = 136,
	label = "eight-4double",
	group = 
"""
1 * R!H u0 {2,D} {8,S}
2   R!H u0 {1,D} {3,S}
3   R!H u0 {2,S} {4,D}
4   R!H u0 {3,D} {5,S}
5   R!H u0 {4,S} {6,D}
6   R!H u0 {5,D} {7,S}
7   R!H u0 {6,S} {8,D}
8   R!H u0 {1,S} {7,D}
""",
	solute = u'Cyclooctatetraene',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 137,
	label = "Cyclooctatetraene",
	group = 
"""
1 * Cd u0 {2,D} {8,S}
2   Cd u0 {1,D} {3,S}
3   Cd u0 {2,S} {4,D}
4   Cd u0 {3,D} {5,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {5,D} {7,S}
7   Cd u0 {6,S} {8,D}
8   Cd u0 {1,S} {7,D}
""",
	solute = SoluteData(
		S = -0.04873,
		B = -0.02685,
		E = -0.06156,
		L = -0.10408,
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
	label = "NineMember",
	group = 
"""
1 * R!H u0 {2,[S,D]} {9,[S,D]}
2   R!H u0 {1,[S,D]} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,[S,D]}
4   R!H u0 {3,[S,D]} {5,[S,D]}
5   R!H u0 {4,[S,D]} {6,[S,D]}
6   R!H u0 {5,[S,D]} {7,[S,D]}
7   R!H u0 {6,[S,D]} {8,[S,D]}
8   R!H u0 {7,[S,D]} {9,[S,D]}
9   R!H u0 {1,[S,D]} {8,[S,D]}
""",
	solute = u'Cyclononane',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 139,
	label = "Cyclononane",
	group = 
"""
1 * C  u0 {2,S} {9,S}
2   C  u0 {1,S} {3,S}
3   C  u0 {2,S} {4,S}
4   C  u0 {3,S} {5,S}
5   C  u0 {4,S} {6,S}
6   C  u0 {5,S} {7,S}
7   C  u0 {6,S} {8,S}
8   C  u0 {7,S} {9,S}
9   C  u0 {1,S} {8,S}
""",
	solute = SoluteData(
		S = 0.01787,
		B = 0.00000,
		E = 0.00507,
		L = 0.06278,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 6,
		B = 6,
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
	index = 140,
	label = "TenMember",
	group = 
"""
1  * R!H u0 {2,[S,D]} {10,[S,D]}
2    R!H u0 {1,[S,D]} {3,[S,D]}
3    R!H u0 {2,[S,D]} {4,[S,D]}
4    R!H u0 {3,[S,D]} {5,[S,D]}
5    R!H u0 {4,[S,D]} {6,[S,D]}
6    R!H u0 {5,[S,D]} {7,[S,D]}
7    R!H u0 {6,[S,D]} {8,[S,D]}
8    R!H u0 {7,[S,D]} {9,[S,D]}
9    R!H u0 {8,[S,D]} {10,[S,D]}
10   R!H u0 {1,[S,D]} {9,[S,D]}
""",
	solute = SoluteData(
		S = 0.03628,
		B = -0.01901,
		E = -0.00872,
		L = 0.04759,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 4,
		B = 3,
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
	index = 141,
	label = "Cyclodecane",
	group = 
"""
1  * C  u0 {2,S} {10,S}
2    C  u0 {1,S} {3,S}
3    C  u0 {2,S} {4,S}
4    C  u0 {3,S} {5,S}
5    C  u0 {4,S} {6,S}
6    C  u0 {5,S} {7,S}
7    C  u0 {6,S} {8,S}
8    C  u0 {7,S} {9,S}
9    C  u0 {8,S} {10,S}
10   C  u0 {1,S} {9,S}
""",
	solute = SoluteData(
		S = -0.04460,
		B = 0.00000,
		E = 0.00203,
		L = 0.05150,
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
	index = 142,
	label = "ElevenMember",
	group = 
"""
1  * R!H u0 {2,[S,D]} {11,[S,D]}
2    R!H u0 {1,[S,D]} {3,[S,D]}
3    R!H u0 {2,[S,D]} {4,[S,D]}
4    R!H u0 {3,[S,D]} {5,[S,D]}
5    R!H u0 {4,[S,D]} {6,[S,D]}
6    R!H u0 {5,[S,D]} {7,[S,D]}
7    R!H u0 {6,[S,D]} {8,[S,D]}
8    R!H u0 {7,[S,D]} {9,[S,D]}
9    R!H u0 {8,[S,D]} {10,[S,D]}
10   R!H u0 {9,[S,D]} {11,[S,D]}
11   R!H u0 {1,[S,D]} {10,[S,D]}
""",
	solute = SoluteData(
		S = -0.07953,
		B = 0.00000,
		E = -0.00309,
		L = 0.03128,
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
	index = 143,
	label = "TwelveMember",
	group = 
"""
1  * R!H u0 {2,[S,D]} {12,[S,D]}
2    R!H u0 {1,[S,D]} {3,[S,D]}
3    R!H u0 {2,[S,D]} {4,[S,D]}
4    R!H u0 {3,[S,D]} {5,[S,D]}
5    R!H u0 {4,[S,D]} {6,[S,D]}
6    R!H u0 {5,[S,D]} {7,[S,D]}
7    R!H u0 {6,[S,D]} {8,[S,D]}
8    R!H u0 {7,[S,D]} {9,[S,D]}
9    R!H u0 {8,[S,D]} {10,[S,D]}
10   R!H u0 {9,[S,D]} {11,[S,D]}
11   R!H u0 {10,[S,D]} {12,[S,D]}
12   R!H u0 {1,[S,D]} {11,[S,D]}
""",
	solute = SoluteData(
		S = -0.07121,
		B = 0.00000,
		E = -0.01820,
		L = 0.07672,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 7,
		B = 7,
		E = 8,
		L = 5,
		A = 8,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 144,
	label = "ThirteenMember",
	group = 
"""
1  * R!H u0 {2,[S,D]} {13,[S,D]}
2    R!H u0 {1,[S,D]} {3,[S,D]}
3    R!H u0 {2,[S,D]} {4,[S,D]}
4    R!H u0 {3,[S,D]} {5,[S,D]}
5    R!H u0 {4,[S,D]} {6,[S,D]}
6    R!H u0 {5,[S,D]} {7,[S,D]}
7    R!H u0 {6,[S,D]} {8,[S,D]}
8    R!H u0 {7,[S,D]} {9,[S,D]}
9    R!H u0 {8,[S,D]} {10,[S,D]}
10   R!H u0 {9,[S,D]} {11,[S,D]}
11   R!H u0 {10,[S,D]} {12,[S,D]}
12   R!H u0 {11,[S,D]} {13,[S,D]}
13   R!H u0 {1,[S,D]} {12,[S,D]}
""",
	solute = SoluteData(
		S = -0.08200,
		B = 0.00000,
		E = -0.02425,
		L = 0.15033,
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
	index = 145,
	label = "FourteenMember",
	group = 
"""
1  * R!H u0 {2,[S,D]} {14,[S,D]}
2    R!H u0 {1,[S,D]} {3,[S,D]}
3    R!H u0 {2,[S,D]} {4,[S,D]}
4    R!H u0 {3,[S,D]} {5,[S,D]}
5    R!H u0 {4,[S,D]} {6,[S,D]}
6    R!H u0 {5,[S,D]} {7,[S,D]}
7    R!H u0 {6,[S,D]} {8,[S,D]}
8    R!H u0 {7,[S,D]} {9,[S,D]}
9    R!H u0 {8,[S,D]} {10,[S,D]}
10   R!H u0 {9,[S,D]} {11,[S,D]}
11   R!H u0 {10,[S,D]} {12,[S,D]}
12   R!H u0 {11,[S,D]} {13,[S,D]}
13   R!H u0 {12,[S,D]} {14,[S,D]}
14   R!H u0 {1,[S,D]} {13,[S,D]}
""",
	solute = SoluteData(
		S = -0.07302,
		B = 0.00000,
		E = 0.02093,
		L = 0.79366,
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
	index = 146,
	label = "FifteenMember",
	group = 
"""
1  * R!H u0 {2,[S,D]} {15,[S,D]}
2    R!H u0 {1,[S,D]} {3,[S,D]}
3    R!H u0 {2,[S,D]} {4,[S,D]}
4    R!H u0 {3,[S,D]} {5,[S,D]}
5    R!H u0 {4,[S,D]} {6,[S,D]}
6    R!H u0 {5,[S,D]} {7,[S,D]}
7    R!H u0 {6,[S,D]} {8,[S,D]}
8    R!H u0 {7,[S,D]} {9,[S,D]}
9    R!H u0 {8,[S,D]} {10,[S,D]}
10   R!H u0 {9,[S,D]} {11,[S,D]}
11   R!H u0 {10,[S,D]} {12,[S,D]}
12   R!H u0 {11,[S,D]} {13,[S,D]}
13   R!H u0 {12,[S,D]} {14,[S,D]}
14   R!H u0 {13,[S,D]} {15,[S,D]}
15   R!H u0 {1,[S,D]} {14,[S,D]}
""",
	solute = SoluteData(
		S = -0.13937,
		B = 0.01533,
		E = -0.10564,
		L = 0.06886,
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
	index = 147,
	label = "SixteenMember",
	group = 
"""
1  * R!H u0 {2,[S,D]} {16,[S,D]}
2    R!H u0 {1,[S,D]} {3,[S,D]}
3    R!H u0 {2,[S,D]} {4,[S,D]}
4    R!H u0 {3,[S,D]} {5,[S,D]}
5    R!H u0 {4,[S,D]} {6,[S,D]}
6    R!H u0 {5,[S,D]} {7,[S,D]}
7    R!H u0 {6,[S,D]} {8,[S,D]}
8    R!H u0 {7,[S,D]} {9,[S,D]}
9    R!H u0 {8,[S,D]} {10,[S,D]}
10   R!H u0 {9,[S,D]} {11,[S,D]}
11   R!H u0 {10,[S,D]} {12,[S,D]}
12   R!H u0 {11,[S,D]} {13,[S,D]}
13   R!H u0 {12,[S,D]} {14,[S,D]}
14   R!H u0 {13,[S,D]} {15,[S,D]}
15   R!H u0 {14,[S,D]} {16,[S,D]}
16   R!H u0 {1,[S,D]} {15,[S,D]}
""",
	solute = SoluteData(
		S = -0.18716,
		B = 0.08901,
		E = 0.00251,
		L = -0.05472,
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
	index = 148,
	label = "EighteenMember",
	group = 
"""
1  * R!H u0 {2,[S,D]} {18,[S,D]}
2    R!H u0 {1,[S,D]} {3,[S,D]}
3    R!H u0 {2,[S,D]} {4,[S,D]}
4    R!H u0 {3,[S,D]} {5,[S,D]}
5    R!H u0 {4,[S,D]} {6,[S,D]}
6    R!H u0 {5,[S,D]} {7,[S,D]}
7    R!H u0 {6,[S,D]} {8,[S,D]}
8    R!H u0 {7,[S,D]} {9,[S,D]}
9    R!H u0 {8,[S,D]} {10,[S,D]}
10   R!H u0 {9,[S,D]} {11,[S,D]}
11   R!H u0 {10,[S,D]} {12,[S,D]}
12   R!H u0 {11,[S,D]} {13,[S,D]}
13   R!H u0 {12,[S,D]} {14,[S,D]}
14   R!H u0 {13,[S,D]} {15,[S,D]}
15   R!H u0 {14,[S,D]} {16,[S,D]}
16   R!H u0 {15,[S,D]} {17,[S,D]}
17   R!H u0 {16,[S,D]} {18,[S,D]}
18   R!H u0 {1,[S,D]} {17,[S,D]}
""",
	solute = SoluteData(
		S = 0.03458,
		B = -0.06708,
		E = 0.00255,
		L = 0.11260,
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
	index = 149,
	label = "TwentyfourMember",
	group = 
"""
1  * R!H u0 {2,[S,D]} {24,[S,D]}
2    R!H u0 {1,[S,D]} {3,[S,D]}
3    R!H u0 {2,[S,D]} {4,[S,D]}
4    R!H u0 {3,[S,D]} {5,[S,D]}
5    R!H u0 {4,[S,D]} {6,[S,D]}
6    R!H u0 {5,[S,D]} {7,[S,D]}
7    R!H u0 {6,[S,D]} {8,[S,D]}
8    R!H u0 {7,[S,D]} {9,[S,D]}
9    R!H u0 {8,[S,D]} {10,[S,D]}
10   R!H u0 {9,[S,D]} {11,[S,D]}
11   R!H u0 {10,[S,D]} {12,[S,D]}
12   R!H u0 {11,[S,D]} {13,[S,D]}
13   R!H u0 {12,[S,D]} {14,[S,D]}
14   R!H u0 {13,[S,D]} {15,[S,D]}
15   R!H u0 {14,[S,D]} {16,[S,D]}
16   R!H u0 {15,[S,D]} {17,[S,D]}
17   R!H u0 {16,[S,D]} {18,[S,D]}
18   R!H u0 {17,[S,D]} {19,[S,D]}
19   R!H u0 {18,[S,D]} {20,[S,D]}
20   R!H u0 {19,[S,D]} {21,[S,D]}
21   R!H u0 {20,[S,D]} {22,[S,D]}
22   R!H u0 {21,[S,D]} {23,[S,D]}
23   R!H u0 {22,[S,D]} {24,[S,D]}
24   R!H u0 {1,[S,D]} {23,[S,D]}
""",
	solute = SoluteData(
		S = 0.09300,
		B = -0.13005,
		E = 0.15788,
		L = -0.01905,
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
	index = 150,
	label = "ThirtythreeMember",
	group = 
"""
1  * R!H u0 {13,[S,D]} {14,[S,D]}
2  R!H u0 {15,[S,D]} {16,[S,D]}
3  R!H u0 {17,[S,D]} {18,[S,D]}
4  R!H u0 {19,[S,D]} {20,[S,D]}
5  R!H u0 {21,[S,D]} {22,[S,D]}
6  R!H u0 {23,[S,D]} {24,[S,D]}
7  R!H u0 {25,[S,D]} {26,[S,D]}
8  R!H u0 {27,[S,D]} {28,[S,D]}
9  R!H u0 {29,[S,D]} {30,[S,D]}
10 R!H u0 {31,[S,D]} {32,[S,D]}
11 R!H u0 {12,[S,D]} {33,[S,D]}
12 R!H u0 {11,[S,D]} {13,[S,D]}
13 R!H u0 {1,[S,D]} {12,[S,D]}
14 R!H u0 {1,[S,D]} {15,[S,D]}
15 R!H u0 {2,[S,D]} {14,[S,D]}
16 R!H u0 {2,[S,D]} {17,[S,D]}
17 R!H u0 {3,[S,D]} {16,[S,D]}
18 R!H u0 {3,[S,D]} {19,[S,D]}
19 R!H u0 {4,[S,D]} {18,[S,D]}
20 R!H u0 {4,[S,D]} {21,[S,D]}
21 R!H u0 {5,[S,D]} {20,[S,D]}
22 R!H u0 {5,[S,D]} {23,[S,D]}
23 R!H u0 {6,[S,D]} {22,[S,D]}
24 R!H u0 {6,[S,D]} {25,[S,D]}
25 R!H u0 {7,[S,D]} {24,[S,D]}
26 R!H u0 {7,[S,D]} {27,[S,D]}
27 R!H u0 {8,[S,D]} {26,[S,D]}
28 R!H u0 {8,[S,D]} {29,[S,D]}
29 R!H u0 {9,[S,D]} {28,[S,D]}
30 R!H u0 {9,[S,D]} {31,[S,D]}
31 R!H u0 {10,[S,D]} {30,[S,D]}
32 R!H u0 {10,[S,D]} {33,[S,D]}
33 R!H u0 {11,[S,D]} {32,[S,D]}
""",
	solute = u'Cyclosporin',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 151,
	label = "Cyclosporin",
	group = 
"""
1  O u0 {34,D}
2  O u0 {35,D}
3  O u0 {36,D}
4  O u0 {37,D}
5  O u0 {38,D}
6  O u0 {39,D}
7  O u0 {40,D}
8  O u0 {41,D}
9  O u0 {42,D}
10 O u0 {43,D}
11 O u0 {44,D}
12 N u0 {24,S} {34,S}
13 N u0 {25,S} {35,S}
14 N u0 {26,S} {36,S}
15 N u0 {27,S} {37,S}
16 N u0 {28,S} {38,S}
17 N u0 {29,S} {39,S}
18 N u0 {30,S} {40,S}
19 N u0 {31,S} {41,S}
20 N u0 {32,S} {42,S}
21 N u0 {33,S} {43,S}
22 N u0 {23,S} {44,S}
23 * C u0 {22,S} {34,S}
24 C u0 {12,S} {35,S}
25 C u0 {13,S} {36,S}
26 C u0 {14,S} {37,S}
27 C u0 {15,S} {38,S}
28 C u0 {16,S} {39,S}
29 C u0 {17,S} {40,S}
30 C u0 {18,S} {41,S}
31 C u0 {19,S} {42,S}
32 C u0 {20,S} {43,S}
33 C u0 {21,S} {44,S}
34 CO u0 {1,D} {12,S} {23,S}
35 CO u0 {2,D} {13,S} {24,S}
36 CO u0 {3,D} {14,S} {25,S}
37 CO u0 {4,D} {15,S} {26,S}
38 CO u0 {5,D} {16,S} {27,S}
39 CO u0 {6,D} {17,S} {28,S}
40 CO u0 {7,D} {18,S} {29,S}
41 CO u0 {8,D} {19,S} {30,S}
42 CO u0 {9,D} {20,S} {31,S}
43 CO u0 {10,D} {21,S} {32,S}
44 CO u0 {11,D} {22,S} {33,S}
""",
	solute = SoluteData(
		S = 0.05579,
		B = -0.01893,
		E = -0.12556,
		L = 0.20437,
		A = -0.02278,
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

tree(
"""
L1: Ring
	L2: Aromatic
		L3: Benzene
	L2: ThreeMember
		L3: Cyclopropane
		L3: Ethylene_oxide
		L3: Ethyleneimine
	L2: FourMember
		L3: Cyclobutane
		L3: Oxetane
			L4: Beta-Propiolactone
		L3: Azetidine
	L2: FiveMember
		L3: five-0double
			L4: Cyclopentane
				L5: Cyclopentanone
				L5: Cyclopentanol
				L5: methylenecyclopentane
			L4: Tetrahydrofuran
				L5: butyrolactone
			L4: Pyrrolidine
				L5: Pyrrolidine(N-H)
				L5: Pyrrolidine(N-R)
			L4: 1,3-Dioxolane
			L4: thiolane
			L4: Imidazolidine
				L5: imidazolidine-2,4-dione
		L3: five-1double
			L4: Cyclopentene
			L4: 2-pyrroline
			L4: 3-pyrroline
			L4: 2-pyrazoline
			L4: 2-imidazoline
			L4: five-N1NC=CC1
			L4: 2,5-Dihydrofuran
				L5: 5H-furan-2-one
		L3: five-2double
			L4: Cyclopentadiene
			L4: Furan
			L4: 1H-Pyrrole
			L4: Thiophene
			L4: Pyrazole
			L4: Imidazole
				L5: 2-Nitroimidazole
			L4: 1,2,4-Triazole
			L4: Tetrazole
			L4: 2H-Tetrazole
			L4: Oxazole
			L4: Isoxazole
			L4: Thiazole
			L4: 1,2,4-Thiadiazole
			L4: 1,3,4-Thiadiazole
	L2: SixMember
		L3: six-0double
			L4: Cyclohexane
				L5: Cyclohexanone
				L5: Cyclohexanol
				L5: N-Cyclohexylacetamide
			L4: 1,3-Dioxane
			L4: 1,4-Dioxane
			L4: 1,3,5-Trioxane
			L4: Oxane
				L5: 4-Hydroxyoxan-2-one
			L4: Piperidine
				L5: Piperidine(N-H)
				L5: Piperidine(N-R)
					L6: 1-Piperidinecarboxaldehyde
					L6: Piperidine-2,6-dione
			L4: Piperazine
				L5: Piperazine(N-H,N-H)
				L5: Piperazine(N-H,N-R)
				L5: Piperazine(N-R,N-R)
			L4: Morpholine
				L5: Morpholine(N-H)
				L5: Morpholine(N-R)
			L4: 1,3-Diazinane
				L5: 1,3-Diazinane-2,4,6-trione
				L5: 2-Sulfanylidene-1,3-diazinane-4,6-dione
			L4: 1,3,5-Triazinane
			L4: 1,3,2-Dioxaphosphorinane
				L5: 1,3,2-Dioxaphosphorinane-2-oxide
		L3: six-1double
			L4: Cyclohexene
			L4: Tetrahydropyrimidine
				L5: Uracil
			L4: 1,2,3,6-Tetrahydropyridine
			L4: 1,4,5,6-Tetrahydropyridazine
				L5: 4,5-Dihydro-2H-pyridazin-3-one
		L3: six-2double-1,3
			L4: 1,3-Cyclohexadiene
			L4: 1,2-Dihydropyridine
			L4: 2,3-Dihydropyridine
			L4: 1,2-Dihydropyrimidine
				L5: 1H-Pyrimidin-2-one
			L4: N1C=NC=CC1
				L5: 3H-Pyrimidin-4-one
		L3: six-2double-1,4
			L4: 1,4-Cyclohexadiene
				L5: p-Benzoquinone
			L4: 1,4-Dihydropyridine
				L5: 3,4-Dihydroxypyridine
			L4: 4H-Pyran
				L5: 3-Hydroxypyran-4-one
		L3: six-3double
			L4: Pyridine
				L5: Pyridine-N-oxide
				L5: Isonicotinamide
				L5: NicotinicAcidEster
			L4: Pyridazine
			L4: Pyrimidine
			L4: Pyrazine
			L4: 1,3,5-Triazine
				L5: 2-Methylsulfanyl-1,3,5-triazine
				L5: 2-Methoxy-1,3,5-triazine
	L2: SevenMember
		L3: seven-0double
			L4: Cycloheptane
			L4: Oxepane
			L4: seven-0double_N
		L3: seven-1double
			L4: Cycloheptene
		L3: seven-2double-1,3
		L3: seven-3double-1,3,5
			L4: 1,3,5-Cycloheptatriene
	L2: EightMember
		L3: eight-0double
			L4: Cyclooctane
			L4: Azocane
			L4: Octasulfur
		L3: eight-1double
			L4: Cyclooctene
		L3: eight-2double-1,3
			L4: 1,3-cyclooctadiene
		L3: eight-2double-1,5
			L4: 1,5-cyclooctadiene
		L3: eight-4double
			L4: Cyclooctatetraene
	L2: NineMember
		L3: Cyclononane
	L2: TenMember
		L3: Cyclodecane
	L2: ElevenMember
	L2: TwelveMember
	L2: ThirteenMember
	L2: FourteenMember
	L2: FifteenMember
	L2: SixteenMember
	L2: EighteenMember
	L2: TwentyfourMember
	L2: ThirtythreeMember
		L3: Cyclosporin
"""
)
