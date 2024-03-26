#!/usr/bin/env python
# encoding: utf-8

name = "group"
shortDesc = u""
longDesc = u""" 
All groups are fitted using experimental solute parameter data unless written otherwise.
See Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
"""

entry(
	index = -1,
	label = "R",
	group = 
"""
1 * R ux
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
	label = "C",
	group = 
"""
1 * C u0
""",
	solute = u'Cs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 2,
	label = "C2tc",
	group = 
"""
1 * C2tc u0 p1 c-1
""",
	solute = u'C2tc-N5tc',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 3,
	label = "C2tc-N5tc",
	group = 
"""
1 * C2tc u0 p1 c-1 {2,T}
2   N5tc u0 c+1 {1,T}
""",
	solute = SoluteData(
		S = 0.08110,
		B = 0.01778,
		E = 0.08002,
		L = 0.37429,
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
	index = 4,
	label = "Cbf",
	group = 
"""
1 * Cbf u0
""",
	solute = u'Cbf-CbCbCbf',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 5,
	label = "Cbf-CbCbCbf",
	group = 
"""
1 * Cbf u0 {2,B} {3,B} {4,B}
2   Cb  u0 {1,B}
3   Cb  u0 {1,B}
4   Cbf u0 {1,B}
""",
	solute = SoluteData(
		S = 0.07856,
		B = 0.01187,
		E = 0.24563,
		L = 0.75301,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 335,
		B = 330,
		E = 373,
		L = 333,
		A = 373,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 6,
	label = "Cbf-CbCbfCbf",
	group = 
"""
1 * Cbf u0 {2,B} {3,B} {4,B}
2   Cb  u0 {1,B}
3   Cbf u0 {1,B}
4   Cbf u0 {1,B}
""",
	solute = SoluteData(
		S = 0.06907,
		B = 0.03191,
		E = 0.30385,
		L = 0.64169,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 51,
		B = 50,
		E = 73,
		L = 67,
		A = 74,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 7,
	label = "Cbf-CbfCbfCbf",
	group = 
"""
1 * Cbf u0 {2,B} {3,B} {4,B}
2   Cbf u0 {1,B}
3   Cbf u0 {1,B}
4   Cbf u0 {1,B}
""",
	solute = SoluteData(
		S = 0.06184,
		B = 0.05644,
		E = 0.22728,
		L = 0.45812,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 25,
		B = 25,
		E = 30,
		L = 28,
		A = 30,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 8,
	label = "Cb",
	group = 
"""
1 * Cb u0
""",
	solute = u'Cb-C',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 9,
	label = "Cb-H",
	group = 
"""
1 * Cb u0 {2,S}
2   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.10974,
		B = 0.01468,
		E = 0.11814,
		L = 0.53417,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 3841,
		B = 3704,
		E = 4058,
		L = 3525,
		A = 4039,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 10,
	label = "Cb-P",
	group = 
"""
1 * Cb u0 {2,S}
2   P  u0 {1,S}
""",
	solute = u'Cb-P5d',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 11,
	label = "Cb-P3s",
	group = 
"""
1 * Cb  u0 {2,S}
2   P3s u0 {1,S}
""",
	solute = SoluteData(
		S = 0.05477,
		B = 0.07566,
		E = 0.13338,
		L = 0.85899,
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
	label = "Cb-P5d",
	group = 
"""
1 * Cb  u0 {2,S}
2   P5d u0 {1,S}
""",
	solute = SoluteData(
		S = 0.06238,
		B = 0.20534,
		E = 0.12145,
		L = 0.72083,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 9,
		B = 9,
		E = 10,
		L = 9,
		A = 15,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 13,
	label = "Cb-O",
	group = 
"""
1 * Cb u0 {2,S}
2   O  u0 {1,S}
""",
	solute = u'Cb-O2s',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 14,
	label = "Cb-O2s",
	group = 
"""
1 * Cb u0 {2,S}
2   O2s u0 {1,S}
""",
	solute = SoluteData(
		S = 0.08806,
		B = 0.08873,
		E = 0.11740,
		L = 0.77137,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 1100,
		B = 1055,
		E = 1145,
		L = 1053,
		A = 1127,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 15,
	label = "Cb-O2rs",
	group = 
"""
1 * Cb u0 {2,S}
2   O2s u0 r1 {1,S}
""",
	solute = SoluteData(
		S = 0.14959,
		B = 0.01886,
		E = 0.14037,
		L = 0.78052,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 193,
		B = 193,
		E = 196,
		L = 185,
		A = 193,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 16,
	label = "Cb-S",
	group = 
"""
1 * Cb u0 {2,S}
2   S u0 {1,S}
""",
	solute = u'Cb-S6dd',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 17,
	label = "Cb-S2s",
	group = 
"""
1 * Cb  u0 {2,S}
2   S2s u0 {1,S}
""",
	solute = SoluteData(
		S = 0.17680,
		B = 0.03402,
		E = 0.25607,
		L = 0.94701,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 20,
		B = 20,
		E = 24,
		L = 19,
		A = 22,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 18,
	label = "Cb-S2rs",
	group = 
"""
1 * Cb  u0 {2,S}
2   S2s u0 r1 {1,S}
""",
	solute = SoluteData(
		S = 0.07275,
		B = 0.03881,
		E = 0.30204,
		L = 0.98441,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 129,
		B = 129,
		E = 132,
		L = 128,
		A = 132,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 19,
	label = "Cb-S4d",
	group = 
"""
1 * Cb  u0 {2,S}
2   S4d u0 p1 {1,S}
""",
	solute = SoluteData(
		S = 0.10827,
		B = 0.13776,
		E = 0.10492,
		L = 0.53771,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 11,
		B = 11,
		E = 12,
		L = 11,
		A = 17,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 20,
	label = "Cb-S6dd",
	group = 
"""
1 * Cb   u0 {2,S}
2   S6dd u0 {1,S}
""",
	solute = SoluteData(
		S = 0.11593,
		B = 0.01448,
		E = 0.11357,
		L = 0.53224,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 153,
		B = 152,
		E = 161,
		L = 141,
		A = 157,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 21,
	label = "Cb-N",
	group = 
"""
1 * Cb  u0 {2,S}
2   N   u0 {1,S}
""",
	solute = u'Cb-N3s',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 22,
	label = "Cb-N3s",
	group = 
"""
1 * Cb  u0 {2,S}
2   N3s u0 {1,S}
""",
	solute = SoluteData(
		S = 0.12621,
		B = 0.11692,
		E = 0.21711,
		L = 1.02731,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 540,
		B = 504,
		E = 567,
		L = 421,
		A = 561,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 23,
	label = "Cb-N3rs",
	group = 
"""
1 * Cb  u0 {2,S}
2   N3s u0 r1 {1,S}
""",
	solute = SoluteData(
		S = 0.11872,
		B = 0.11746,
		E = 0.22711,
		L = 0.98327,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 252,
		B = 242,
		E = 267,
		L = 233,
		A = 254,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 24,
	label = "Cb-N3d",
	group = 
"""
1 * Cb  u0 {2,S}
2   N3d u0 {1,S}
""",
	solute = SoluteData(
		S = -0.04532,
		B = 0.03414,
		E = 0.10585,
		L = 0.37962,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 32,
		B = 32,
		E = 34,
		L = 29,
		A = 33,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 25,
	label = "Cb-N3rd",
	group = 
"""
1 * Cb  u0 {2,S}
2   N3d u0 r1 {1,S}
""",
	solute = SoluteData(
		S = 0.18304,
		B = 0.14874,
		E = 0.25906,
		L = 0.88577,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 127,
		B = 119,
		E = 134,
		L = 126,
		A = 128,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 26,
	label = "Cb-N5dc",
	group = 
"""
1 * Cb   u0 {2,S}
2   N5dc u0 {1,S}
""",
	solute = SoluteData(
		S = 0.09953,
		B = -0.03875,
		E = 0.13249,
		L = 0.42484,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 302,
		B = 300,
		E = 305,
		L = 259,
		A = 308,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 27,
	label = "Cb-N5tc",
	group = 
"""
1 * Cb   u0 {2,S}
2   N5tc u0 {1,S}
""",
	solute = SoluteData(
		S = 0.03915,
		B = 0.02085,
		E = 0.04258,
		L = 0.24081,
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
	index = 28,
	label = "Cb-C",
	group = 
"""
1 * Cb u0 {2,S}
2   C  u0 {1,S}
""",
	solute = u'Cb-Cs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 29,
	label = "Cb-Cb",
	group = 
"""
1 * Cb u0 {2,S}
2   Cb u0 {1,S}
""",
	solute = SoluteData(
		S = 0.06988,
		B = 0.02674,
		E = 0.17229,
		L = 0.40857,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 379,
		B = 367,
		E = 401,
		L = 385,
		A = 398,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 30,
	label = "Cb-Cr",
	group = 
"""
1 * Cb u0 {2,S}
2   C  u0 r1 {1,S}
""",
	solute = SoluteData(
		S = 0.07086,
		B = 0.06486,
		E = 0.13979,
		L = 0.71759,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 686,
		B = 662,
		E = 731,
		L = 656,
		A = 715,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 31,
	label = "Cb-Cs",
	group = 
"""
1 * Cb u0 {2,S}
2   Cs u0 {1,S}
""",
	solute = SoluteData(
		S = 0.08305,
		B = 0.09566,
		E = 0.11012,
		L = 0.84210,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 1440,
		B = 1362,
		E = 1529,
		L = 1301,
		A = 1507,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 32,
	label = "Cb-(Cs-Cb)",
	group = 
"""
1 * Cb u0 {2,S}
2   Cs u0 {1,S} {3,S}
3   Cb u0 {2,S}
""",
	solute = SoluteData(
		S = 0.01163,
		B = 0.07540,
		E = 0.09593,
		L = 0.57243,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 48,
		B = 47,
		E = 52,
		L = 46,
		A = 49,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 33,
	label = "Cb-(Cs-Cr)",
	group = 
"""
1 * Cb u0 {2,S}
2   Cs u0 {1,S} {3,S}
3   C  u0 r1 {2,S}
""",
	solute = SoluteData(
		S = -0.02437,
		B = 0.13040,
		E = 0.09298,
		L = 0.90955,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 25,
		B = 23,
		E = 26,
		L = 24,
		A = 26,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 34,
	label = "Cb-Cds",
	group = 
"""
1 * Cb      u0 {2,S}
2   [Cd,CO,CS] u0 {1,S}
""",
	solute = u'Cb-(Cds-O2d)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 35,
	label = "Cb-(Cds-O2d)",
	group = 
"""
1 * Cb u0 {2,S}
2   CO u0 {1,S} {3,D}
3   O2d u0 {2,D}
""",
	solute = SoluteData(
		S = 0.04055,
		B = 0.01613,
		E = 0.12083,
		L = 0.54122,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 317,
		B = 314,
		E = 333,
		L = 262,
		A = 334,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 36,
	label = "Cb-(Cds-O2dOs)",
	group = 
"""
1   CO  u0 {2,S} {3,D} {4,S}
2 * Cb  u0 {1,S}
3   O2d u0 {1,D}
4   O2s u0 {1,S}
""",
	solute = SoluteData(
		S = -0.12480,
		B = 0.00772,
		E = 0.11354,
		L = 0.34015,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 365,
		B = 358,
		E = 376,
		L = 345,
		A = 379,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 37,
	label = "Cb-(Cds-Cd)",
	group = 
"""
1 * Cb u0 {2,S}
2   Cd u0 {1,S} {3,D}
3   C  u0 {2,D}
""",
	solute = SoluteData(
		S = 0.07357,
		B = 0.06763,
		E = 0.12021,
		L = 0.75313,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 84,
		B = 80,
		E = 108,
		L = 97,
		A = 95,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 38,
	label = "Cb-(Cds-N3d)",
	group = 
"""
1 * Cb   u0 {2,S}
2   Cd   u0 {1,S} {3,D}
3   N3d  u0 {2,D}
""",
	solute = SoluteData(
		S = -0.07287,
		B = 0.14192,
		E = 0.10959,
		L = 0.47070,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 26,
		B = 26,
		E = 29,
		L = 26,
		A = 28,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 39,
	label = "Cb-(Cds-S2d)",
	group = 
"""
1 * Cb   u0 {2,S}
2   CS   u0 {1,S} {3,D}
3   S2d  u0 {2,D}
""",
	solute = SoluteData(
		S = 0.19617,
		B = 0.00422,
		E = 0.07767,
		L = 0.70680,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 8,
		B = 8,
		E = 8,
		L = 8,
		A = 10,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 40,
	label = "Cb-Ct",
	group = 
"""
1 * Cb u0 {2,S}
2   Ct u0 {1,S}
""",
	solute = u'Cb-(CtN3t)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 41,
	label = "Cb-(CtCt)",
	group = 
"""
1 * Cb u0 {2,S}
2   Ct u0 {1,S} {3,T}
3   Ct u0 {2,T}
""",
	solute = SoluteData(
		S = 0.00563,
		B = 0.01953,
		E = 0.07725,
		L = 0.26644,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
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
	index = 42,
	label = "Cb-(CtN3t)",
	group = 
"""
1 * Cb  u0 {2,S}
2   Ct  u0 {1,S} {3,T}
3   N3t u0 {2,T}
""",
	solute = SoluteData(
		S = 0.11598,
		B = 0.00278,
		E = 0.04079,
		L = 0.23385,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 46,
		B = 41,
		E = 46,
		L = 35,
		A = 54,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 43,
	label = "Ct",
	group = 
"""
1 * Ct u0
""",
	solute = u'Ct-CtC',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 44,
	label = "Ct-N3tN",
	group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   N3t u0 {1,T}
3   N   u0 {1,S}
""",
	solute = SoluteData(
		S = -0.02836,
		B = 0.05170,
		E = 0.00114,
		L = 0.24359,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 10,
		B = 10,
		E = 12,
		L = 2,
		A = 11,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 45,
	label = "Ct-N3tS",
	group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   N3t u0 {1,T}
3   S   u0 {1,S}
""",
	solute = u'Ct-N3tS2s',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 46,
	label = "Ct-N3tS2s",
	group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   N3t u0 {1,T}
3   S2s u0 {1,S}
""",
	solute = SoluteData(
		S = 0.06822,
		B = 0.03635,
		E = 0.11788,
		L = 0.46689,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 4,
		B = 8,
		E = 8,
		L = 4,
		A = 11,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 47,
	label = "Ct-CtH",
	group = 
"""
1 * Ct u0 {2,T} {3,S}
2   Ct u0 {1,T}
3   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.16979,
		B = 0.05857,
		E = 0.09432,
		L = 0.51536,
		A = 0.08872,
	),
	dataCount = DataCountGAV(
		S = 43,
		B = 46,
		E = 47,
		L = 36,
		A = 48,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 48,
	label = "Ct-N3tO",
	group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   N3t u0 {1,T}
3   O   u0 {1,S}
""",
	solute = u'Ct-N3tOs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 49,
	label = "Ct-N3tOs",
	group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   N3t u0 {1,T}
3   O2s  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.02528,
		B = 0.01601,
		E = -0.00086,
		L = -0.00928,
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
	index = 50,
	label = "Ct-N3tC",
	group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   N3t u0 {1,T}
3   C   u0 {1,S}
""",
	solute = u'Ct-N3tCs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 51,
	label = "Ct-N3tCb",
	group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   N3t u0 {1,T}
3   Cb  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.11598,
		B = 0.00278,
		E = 0.04079,
		L = 0.23385,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 46,
		B = 41,
		E = 46,
		L = 35,
		A = 54,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 52,
	label = "Ct-N3tCs",
	group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   N3t u0 {1,T}
3   Cs  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.20222,
		B = 0.09272,
		E = -0.00212,
		L = 0.26366,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 56,
		B = 55,
		E = 55,
		L = 52,
		A = 56,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 53,
	label = "Ct-N3tCd",
	group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   N3t u0 {1,T}
3   Cd  u0 {1,S}
""",
	solute = SoluteData(
		S = -0.01538,
		B = 0.02984,
		E = 0.03048,
		L = 0.05675,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 23,
		B = 23,
		E = 39,
		L = 36,
		A = 19,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 54,
	label = "Ct-N3tCt",
	group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   N3t u0 {1,T}
3   Ct  u0 {1,S}
""",
	solute = u'Ct-N3t(CtN3t)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 55,
	label = "Ct-N3t(CtN3t)",
	group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   N3t u0 {1,T}
3   Ct  u0 {1,S} {4,T}
4   N3t u0 {3,T}
""",
	solute = SoluteData(
		S = 0.06988,
		B = -0.05615,
		E = -0.00092,
		L = -0.04818,
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
	index = 56,
	label = "Ct-CtC",
	group = 
"""
1 * Ct u0 {2,T} {3,S}
2   Ct u0 {1,T}
3   C  u0 {1,S}
""",
	solute = u'Ct-CtCs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 57,
	label = "Ct-CtCs",
	group = 
"""
1 * Ct u0 {2,T} {3,S}
2   Ct u0 {1,T}
3   Cs u0 {1,S}
""",
	solute = SoluteData(
		S = 0.15051,
		B = 0.12324,
		E = 0.11750,
		L = 0.95445,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 81,
		B = 84,
		E = 89,
		L = 53,
		A = 86,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 58,
	label = "Ct-CtCds",
	group = 
"""
1 * Ct      u0 {2,T} {3,S}
2   Ct      u0 {1,T}
3   [Cd,CO,CS] u0 {1,S}
""",
	solute = u'Ct-Ct(Cds-Cd)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 59,
	label = "Ct-Ct(Cds-O2d)",
	group = 
"""
1 * Ct u0 {2,T} {3,S}
2   Ct u0 {1,T}
3   CO u0 {1,S} {4,D}
4   O2d u0 {3,D}
""",
	solute = SoluteData(
		S = 0.03378,
		B = 0.03713,
		E = 0.04079,
		L = 0.18477,
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
	index = 60,
	label = "Ct-Ct(Cds-Cd)",
	group = 
"""
1 * Ct u0 {2,T} {3,S}
2   Ct u0 {1,T}
3   Cd u0 {1,S} {4,D}
4   C  u0 {3,D}
""",
	solute = u'Ct-Ct(Cds-Cds)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 61,
	label = "Ct-Ct(Cds-Cds)",
	group = 
"""
1 * Ct u0 {2,T} {3,S}
2   Ct u0 {1,T}
3   Cd u0 {1,S} {4,D}
4   Cd u0 {3,D}
""",
	solute = SoluteData(
		S = 0.05273,
		B = 0.01072,
		E = 0.09964,
		L = 0.45881,
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
	index = 62,
	label = "Ct-CtCt",
	group = 
"""
1 * Ct u0 {2,T} {3,S}
2   Ct u0 {1,T}
3   Ct u0 {1,S}
""",
	solute = u'Ct-Ct(CtCt)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 63,
	label = "Ct-Ct(CtCt)",
	group = 
"""
1 * Ct u0 {2,T} {3,S}
2   Ct u0 {1,T}
3   Ct u0 {1,S} {4,T}
4   Ct u0 {3,T}
""",
	solute = SoluteData(
		S = 0.02917,
		B = 0.01510,
		E = 0.07612,
		L = 0.29643,
		A = -0.00186,
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
	index = 64,
	label = "Ct-CtCb",
	group = 
"""
1 * Ct u0 {2,T} {3,S}
2   Ct u0 {1,T}
3   Cb u0 {1,S}
""",
	solute = SoluteData(
		S = 0.00563,
		B = 0.01953,
		E = 0.07725,
		L = 0.26644,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
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
	index = 65,
	label = "Cdd",
	group = 
"""
1 * Cdd u0
""",
	solute = u'Cdd-CdCd',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 66,
	label = "Cdd-CdCd",
	group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   C   u0 {1,D}
3   C   u0 {1,D}
""",
	solute = u'Cdd-CdsCds',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 67,
	label = "Cdd-CdsCds",
	group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   Cd  u0 {1,D}
3   Cd  u0 {1,D}
""",
	solute = SoluteData(
		S = 0.05704,
		B = 0.02777,
		E = 0.08002,
		L = 0.54157,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 11,
		B = 11,
		E = 10,
		L = 6,
		A = 14,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 68,
	label = "Cdd-N3dO2d",
	group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   N3d u0 {1,D}
3   O2d  u0 {1,D}
""",
	solute = SoluteData(
		S = 0.16925,
		B = 0.04807,
		E = 0.06879,
		L = 0.50992,
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
	index = 69,
	label = "Cdd-N3dS",
	group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   N3d u0 {1,D}
3   S   u0 {1,D}
""",
	solute = u'Cdd-N3dS2d',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 70,
	label = "Cdd-N3dS2d",
	group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   N3d u0 {1,D}
3   S2d u0 {1,D}
""",
	solute = SoluteData(
		S = 0.03743,
		B = -0.02447,
		E = 0.08017,
		L = 0.23881,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 7,
		B = 10,
		E = 9,
		L = 7,
		A = 12,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 71,
	label = "Cds",
	group = 
"""
1 * [Cd,CO,CS] u0
""",
	solute = u'Cds-Cd',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 72,
	label = "Cds-Od",
	group = 
"""
1 * CO u0 {2,D}
2   O  u0 {1,D}
""",
	solute = u'Cds-OdCC',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 73,
	label = "Cds-OdNC",
	group = 
"""
1 * CO  u0 {2,S} {3,S} {4,D}
2   N   u0 {1,S}
3   C   u0 {1,S}
4   O2d u0 {1,D}
""",
	solute = u'Cds-OdN3sC',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 74,
	label = "Cds-OdN3sC",
	group = 
"""
1 * CO  u0 {2,S} {3,S} {4,D}
2   N3s u0 {1,S}
3   C   u0 {1,S}
4   O2d u0 {1,D}
""",
	solute = u'Cds-OdN3sCs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 75,
	label = "Crds-OdN3rsCr",
	group = 
"""
1 * CO  u0 r1 {2,S} {3,S} {4,D}
2   N3s u0 r1 {1,S}
3   C   u0 r1 {1,S}
4   O2d u0 {1,D}
""",
	solute = SoluteData(
		S = 0.06281,
		B = 0.10749,
		E = 0.07240,
		L = 0.44045,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 339,
		B = 337,
		E = 347,
		L = 254,
		A = 340,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 76,
	label = "Cds-OdN3sCb",
	group = 
"""
1 * CO  u0 {2,S} {3,S} {4,D}
2   N3s u0 {1,S}
3   Cb  u0 {1,S}
4   O2d  u0 {1,D}
""",
	solute = u'Cds-Od(N3s-RH)Cb',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 77,
	label = "Cds-Od(N3s-HH)Cb",
	group = 
"""
1 * CO  u0 {2,S} {3,S} {4,D}
2   N3s u0 {1,S} {5,S} {6,S}
3   Cb  u0 {1,S}
4   O2d  u0 {1,D}
5   H   u0 {2,S}
6   H   u0 {2,S}
""",
	solute = SoluteData(
		S = 0.07519,
		B = 0.02264,
		E = 0.03618,
		L = 0.02914,
		A = 0.01906,
	),
	dataCount = DataCountGAV(
		S = 33,
		B = 33,
		E = 35,
		L = 24,
		A = 34,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 78,
	label = "Cds-Od(N3s-RH)Cb",
	group = 
"""
1 * CO  u0 {2,S} {3,S} {4,D}
2   N3s u0 {1,S} {5,S} {6,S}
3   Cb  u0 {1,S}
4   O2d  u0 {1,D}
5   R!H  u0 {2,S}
6   H   u0 {2,S}
""",
	solute = SoluteData(
		S = 0.00408,
		B = 0.04293,
		E = 0.02920,
		L = 0.13768,
		A = 0.01839,
	),
	dataCount = DataCountGAV(
		S = 47,
		B = 47,
		E = 47,
		L = 43,
		A = 47,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 79,
	label = "Cds-Od(N3s-RR)Cb",
	group = 
"""
1 * CO  u0 {2,S} {3,S} {4,D}
2   N3s u0 {1,S} {5,S} {6,S}
3   Cb  u0 {1,S}
4   O2d  u0 {1,D}
5   R!H  u0 {2,S}
6   R!H  u0 {2,S}
""",
	solute = SoluteData(
		S = -0.06084,
		B = 0.12192,
		E = 0.01750,
		L = -0.00533,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 31,
		B = 31,
		E = 31,
		L = 26,
		A = 37,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 80,
	label = "Cds-OdN3sCs",
	group = 
"""
1 * CO  u0 {2,S} {3,S} {4,D}
2   N3s u0 {1,S}
3   Cs  u0 {1,S}
4   O2d  u0 {1,D}
""",
	solute = u'Cds-Od(N3s-RH)Cs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 81,
	label = "Cds-OdN3rsCs",
	group = 
"""
1 * CO  u0 {2,S} {3,S} {4,D}
2   N3s u0 r1 {1,S}
3   Cs  u0 {1,S}
4   O2d  u0 {1,D}
""",
	solute = SoluteData(
		S = -0.03050,
		B = -0.02876,
		E = -0.03080,
		L = -0.13201,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 41,
		B = 41,
		E = 45,
		L = 35,
		A = 46,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 82,
	label = "Cds-Od(N3s-HH)Cs",
	group = 
"""
1 * CO  u0 {2,S} {3,S} {4,D}
2   N3s u0 {1,S} {5,S} {6,S}
3   Cs  u0 {1,S}
4   O2d  u0 {1,D}
5   H  u0 {2,S}
6   H  u0 {2,S}
""",
	solute = SoluteData(
		S = 0.12285,
		B = 0.08867,
		E = 0.08413,
		L = 0.40012,
		A = 0.09053,
	),
	dataCount = DataCountGAV(
		S = 36,
		B = 36,
		E = 38,
		L = 32,
		A = 36,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 83,
	label = "Cds-Od(N3s-RH)Cs",
	group = 
"""
1 * CO  u0 {2,S} {3,S} {4,D}
2   N3s u0 {1,S} {5,S} {6,S}
3   Cs  u0 {1,S}
4   O2d  u0 {1,D}
5   R!H u0 {2,S}
6   H  u0 {2,S}
""",
	solute = SoluteData(
		S = 0.19227,
		B = 0.08960,
		E = 0.00140,
		L = 0.33521,
		A = 0.05293,
	),
	dataCount = DataCountGAV(
		S = 157,
		B = 156,
		E = 160,
		L = 139,
		A = 156,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 84,
	label = "Cds-Od(N3s-RR)Cs",
	group = 
"""
1 * CO  u0 {2,S} {3,S} {4,D}
2   N3s u0 {1,S} {5,S} {6,S}
3   Cs  u0 {1,S}
4   O2d  u0 {1,D}
5   R!H u0 {2,S}
6   R!H u0 {2,S}
""",
	solute = SoluteData(
		S = 0.13994,
		B = 0.04639,
		E = 0.00550,
		L = 0.38090,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 39,
		B = 43,
		E = 45,
		L = 39,
		A = 57,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 85,
	label = "Cds-OdN3sCd",
	group = 
"""
1 * CO            u0 {2,S} {3,S} {4,D}
2   N3s           u0 {1,S}
3   [Cd,CO,CS]  u0 {1,S}
4   O2d           u0 {1,D}
""",
	solute = SoluteData(
		S = -0.09423,
		B = 0.04519,
		E = 0.05442,
		L = 0.13761,
		A = 0.05485,
	),
	dataCount = DataCountGAV(
		S = 9,
		B = 9,
		E = 9,
		L = 9,
		A = 9,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 86,
	label = "Cds-OdN3rsCd",
	group = 
"""
1 * CO            u0 {2,S} {3,S} {4,D}
2   N3s           u0 r1 {1,S}
3   [Cd,CO,CS]  u0 {1,S}
4   O2d           u0 {1,D}
""",
	solute = SoluteData(
		S = -0.08133,
		B = 0.09407,
		E = 0.00996,
		L = 0.03761,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 3,
		L = 3,
		A = 3,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 87,
	label = "Cds-OdN3sCrd",
	group = 
"""
1 * CO            u0 {2,S} {3,S} {4,D}
2   N3s           u0 {1,S}
3   [Cd,CO,CS]  u0 r1 {1,S}
4   O2d           u0 {1,D}
""",
	solute = SoluteData(
		S = -0.02549,
		B = 0.03455,
		E = 0.07157,
		L = 0.23470,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 66,
		B = 66,
		E = 69,
		L = 59,
		A = 70,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 88,
	label = "Cds-OdN3dC",
	group = 
"""
1 * CO  u0 {2,S} {3,S} {4,D}
2   N3d u0 {1,S}
3   C   u0 {1,S}
4   O2d u0 {1,D}
""",
	solute = u'Crds-OdN3rdCr',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 89,
	label = "Crds-OdN3rdCr",
	group = 
"""
1 * CO  u0 r1 {2,S} {3,S} {4,D}
2   N3d u0 r1 {1,S}
3   C   u0 r1 {1,S}
4   O2d u0 {1,D}
""",
	solute = SoluteData(
		S = 0.02795,
		B = 0.05094,
		E = 0.03857,
		L = 0.13208,
		A = 0.00452,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 5,
		E = 5,
		L = 4,
		A = 5,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 90,
	label = "Cds-OdNH",
	group = 
"""
1 * CO  u0 {2,S} {3,S} {4,D}
2   N   u0 {1,S}
3   H   u0 {1,S}
4   O2d  u0 {1,D}
""",
	solute = SoluteData(
		S = 0.32063,
		B = 0.00340,
		E = 0.05844,
		L = 0.24039,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 15,
		B = 15,
		E = 17,
		L = 13,
		A = 16,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 91,
	label = "Cds-OdNN",
	group = 
"""
1 * CO  u0 {2,S} {3,S} {4,D}
2   N   u0 {1,S}
3   N   u0 {1,S}
4   O2d u0 {1,D}
""",
	solute = u'Cds-OdN3sN',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 92,
	label = "Cds-OdN3sN",
	group = 
"""
1 * CO  u0 {2,S} {3,S} {4,D}
2   N3s u0 {1,S}
3   N   u0 {1,S}
4   O2d u0 {1,D}
""",
	solute = u'Cds-OdN3sN3s',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 93,
	label = "Cds-OdN3sN3s",
	group = 
"""
1 * CO  u0 {2,S} {3,S} {4,D}
2   N3s u0 {1,S}
3   N3s u0 {1,S}
4   O2d u0 {1,D}
""",
	solute = SoluteData(
		S = -0.05725,
		B = 0.01418,
		E = 0.02108,
		L = 0.11667,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 109,
		B = 103,
		E = 111,
		L = 60,
		A = 110,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 94,
	label = "Crds-OdN3rsN3rs",
	group = 
"""
1 * CO  u0 r1 {2,S} {3,S} {4,D}
2   N3s u0 r1 {1,S}
3   N3s u0 r1 {1,S}
4   O2d u0 {1,D}
""",
	solute = SoluteData(
		S = 0.00217,
		B = -0.03735,
		E = -0.03977,
		L = 0.22237,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 165,
		B = 165,
		E = 170,
		L = 110,
		A = 166,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 95,
	label = "Cds-OdN3rsN3s",
	group = 
"""
1 * CO  u0 {2,S} {3,S} {4,D}
2   N3s u0 r1 {1,S}
3   N3s u0 {1,S}
4   O2d u0 {1,D}
""",
	solute = SoluteData(
		S = -0.14401,
		B = -0.13850,
		E = 0.03368,
		L = -0.14794,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 17,
		B = 17,
		E = 17,
		L = 16,
		A = 17,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 96,
	label = "Cds-OdN3sN3d",
	group = 
"""
1 * CO  u0 {2,S} {3,S} {4,D}
2   N3s u0 {1,S}
3   N3d u0 {1,S}
4   O2d u0 {1,D}
""",
	solute = u'Crds-OdN3rsN3rd',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 97,
	label = "Crds-OdN3rsN3rd",
	group = 
"""
1 * CO  u0 r1 {2,S} {3,S} {4,D}
2   N3s u0 r1 {1,S}
3   N3d u0 r1 {1,S}
4   O2d u0 {1,D}
""",
	solute = SoluteData(
		S = 0.06347,
		B = 0.03769,
		E = 0.11461,
		L = 0.37581,
		A = 0.01779,
	),
	dataCount = DataCountGAV(
		S = 7,
		B = 6,
		E = 7,
		L = 6,
		A = 7,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 98,
	label = "Cds-OdNOs",
	group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   N   u0 {1,S}
4   O2s u0 {1,S}
""",
	solute = u'Cds-Od(N3sCH)Os',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 99,
	label = "Cds-OdN3rsOs",
	group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   N3s u0 r1 {1,S}
3   O2d u0 {1,D}
4   O2s u0 {1,S}
""",
	solute = SoluteData(
		S = -0.08418,
		B = -0.00225,
		E = 0.01188,
		L = -0.05354,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 15,
		B = 15,
		E = 15,
		L = 14,
		A = 15,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 100,
	label = "Cds-Od(N3sHH)Os",
	group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   N3s u0 {1,S} {5,S} {6,S}
3   O2d u0 {1,D}
4   O2s u0 {1,S}
5   H   u0 {2,S}
6   H   u0 {2,S}
""",
	solute = SoluteData(
		S = 0.10967,
		B = -0.04988,
		E = 0.05205,
		L = 0.28493,
		A = 0.05565,
	),
	dataCount = DataCountGAV(
		S = 16,
		B = 16,
		E = 16,
		L = 16,
		A = 16,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 101,
	label = "Cds-Od(N3sCH)Os",
	group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   N3s u0 {1,S} {5,S} {6,S}
3   O2d u0 {1,D}
4   O2s u0 {1,S}
5   C   u0 {2,S}
6   H   u0 {2,S}
""",
	solute = SoluteData(
		S = -0.03357,
		B = 0.01532,
		E = -0.03313,
		L = -0.07412,
		A = -0.01274,
	),
	dataCount = DataCountGAV(
		S = 28,
		B = 28,
		E = 28,
		L = 26,
		A = 28,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 102,
	label = "Cds-Od(N3sCC)Os",
	group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   N3s u0 {1,S} {5,S} {6,S}
3   O2d u0 {1,D}
4   O2s u0 {1,S}
5   C   u0 {2,S}
6   C   u0 {2,S}
""",
	solute = SoluteData(
		S = -0.03350,
		B = -0.08006,
		E = -0.00704,
		L = -0.07948,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 7,
		B = 7,
		E = 7,
		L = 5,
		A = 8,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 103,
	label = "Cds-OdNS",
	group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   N   u0 {1,S}
4   S   u0 {1,S}
""",
	solute = SoluteData(
		S = -0.02841,
		B = 0.02223,
		E = 0.08891,
		L = 0.22034,
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
	index = 104,
	label = "Cds-OdOsH",
	group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   O2s u0 {1,S}
4   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.02503,
		B = 0.02072,
		E = -0.01810,
		L = -0.29483,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 26,
		B = 25,
		E = 26,
		L = 25,
		A = 27,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 105,
	label = "Cds-OdOsOs",
	group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
""",
	solute = SoluteData(
		S = 0.01559,
		B = 0.03222,
		E = -0.01775,
		L = -0.13747,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 15,
		B = 15,
		E = 15,
		L = 15,
		A = 15,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 106,
	label = "Cds-OdCS",
	group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   S  u0 {1,S}
4   C  u0 {1,S}
""",
	solute = u'Cds-OdCsSs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 107,
	label = "Cds-OdCsSs",
	group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   S2s u0 {1,S}
4   Cs u0 {1,S}
""",
	solute = SoluteData(
		S = 0.02704,
		B = 0.03807,
		E = 0.04191,
		L = 0.11996,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 4,
		B = 3,
		E = 7,
		L = 2,
		A = 6,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 108,
	label = "Cds-OdCH",
	group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   C  u0 {1,S}
4   H  u0 {1,S}
""",
	solute = u'Cds-OdCsH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 109,
	label = "Cds-OdCsH",
	group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cs u0 {1,S}
4   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.04357,
		B = 0.04890,
		E = 0.00355,
		L = -0.18553,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 57,
		B = 57,
		E = 62,
		L = 58,
		A = 64,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 110,
	label = "Cds-OdCdsH",
	group = 
"""
1 * CO      u0 {2,D} {3,S} {4,S}
2   O2d      u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   H       u0 {1,S}
""",
	solute = u'Cds-O2d(Cds-Cd)H',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 111,
	label = "Cds-O2d(Cds-O2d)H",
	group = 
"""
1 * CO u0 {2,S} {3,D} {4,S}
2   CO u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   H  u0 {1,S}
5   O2d u0 {2,D}
""",
	solute = SoluteData(
		S = -0.01962,
		B = -0.00898,
		E = 0.00618,
		L = -0.32615,
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
	index = 112,
	label = "Cds-O2d(Cds-Cd)H",
	group = 
"""
1 * CO u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   H  u0 {1,S}
5   C  u0 {2,D}
""",
	solute = u'Cds-O2d(Cds-Cds)H',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 113,
	label = "Cds-O2d(Cds-Cds)H",
	group = 
"""
1 * CO u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   H  u0 {1,S}
5   Cd u0 {2,D}
""",
	solute = SoluteData(
		S = 0.22078,
		B = 0.01338,
		E = 0.06920,
		L = 0.08112,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 43,
		B = 43,
		E = 44,
		L = 43,
		A = 44,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 114,
	label = "Cds-OdCtH",
	group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Ct u0 {1,S}
4   H  u0 {1,S}
""",
	solute = u'Cds-Od(Ct-(Ct-H))H',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 115,
	label = "Cds-Od(Ct-(Ct-H))H",
	group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Ct u0 {1,S} {5,T}
4   H  u0 {1,S}
5   Ct u0 {3,T} {6,S}
6   H  u0 {5,S}
""",
	solute = SoluteData(
		S = 0.02798,
		B = 0.00501,
		E = 0.01823,
		L = -0.01933,
		A = 0.00026,
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
	index = 116,
	label = "Cds-OdCbH",
	group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cb u0 {1,S}
4   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.07491,
		B = -0.03993,
		E = 0.05398,
		L = -0.21798,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 74,
		B = 71,
		E = 85,
		L = 70,
		A = 79,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 117,
	label = "Cds-OdPOs",
	group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   P   u0 {1,S}
4   O2s u0 {1,S}
""",
	solute = None,
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 118,
	label = "Cds-OdP5dOs",
	group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   P5d u0 {1,S}
4   O2s u0 {1,S}
""",
	solute = None,
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 119,
	label = "Cds-OdP5d(OsH)",
	group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   P5d u0 {1,S}
4   O2s u0 {1,S} {5,S}
5   H   u0 {4,S}
""",
	solute = SoluteData(
		S = -0.00496,
		B = 0.04553,
		E = 0.00847,
		L = -0.06074,
		A = 0.03725,
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
	index = 120,
	label = "Cds-OdCOs",
	group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   C  u0 {1,S}
4   O2s u0 {1,S}
""",
	solute = u'Cds-OdCsOs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 121,
	label = "Cds-OdCtOs",
	group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Ct u0 {1,S}
4   O2s u0 {1,S}
""",
	solute = SoluteData(
		S = 0.00581,
		B = 0.03213,
		E = 0.02256,
		L = 0.20410,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
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
	label = "Cds-OdC(OsH)",
	group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   C   u0 {1,S}
3   O2d u0 {1,D}
4   O2s u0 {1,S} {5,S}
5   H   u0 {4,S}
""",
	solute = u'Cds-OdCs(OsH)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 123,
	label = "Cds-OdCs(OsH)",
	group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   Cs  u0 {1,S}
3   O2d u0 {1,D}
4   O2s u0 {1,S} {5,S}
5   H   u0 {4,S}
""",
	solute = SoluteData(
		S = 0.01149,
		B = 0.03832,
		E = -0.02591,
		L = 0.01317,
		A = 0.11724,
	),
	dataCount = DataCountGAV(
		S = 280,
		B = 280,
		E = 286,
		L = 252,
		A = 280,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 124,
	label = "Cds-OdCds(OsH)",
	group = 
"""
1 * CO      u0 {2,S} {3,D} {4,S}
2   [Cd,CO] u0 {1,S}
3   O2d     u0 {1,D}
4   O2s     u0 {1,S} {5,S}
5   H       u0 {4,S}
""",
	solute = u'Cds-Od(Cds-Cd)(OsH)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 125,
	label = "Cds-Od(Cds-O2d)(OsH)",
	group = 
"""
1 * CO   u0 {2,S} {3,D} {4,S}
2   CO   u0 {1,S} {6,D}
3   O2d  u0 {1,D}
4   O2s  u0 {1,S} {5,S}
5   H    u0 {4,S}
6   O2d  u0 {2,D}
""",
	solute = SoluteData(
		S = 0.07834,
		B = -0.06728,
		E = 0.01477,
		L = -0.04321,
		A = 0.03969,
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
	index = 126,
	label = "Cds-Od(Cds-Cd)(OsH)",
	group = 
"""
1 * CO   u0 {2,S} {3,D} {4,S}
2   Cd   u0 {1,S} {6,D}
3   O2d  u0 {1,D}
4   O2s  u0 {1,S} {5,S}
5   H    u0 {4,S}
6   C    u0 {2,D}
""",
	solute = SoluteData(
		S = -0.08075,
		B = -0.02867,
		E = -0.00374,
		L = -0.06622,
		A = 0.03418,
	),
	dataCount = DataCountGAV(
		S = 28,
		B = 28,
		E = 28,
		L = 26,
		A = 28,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 127,
	label = "Cds-Od(Crds-Crd)(OsH)",
	group = 
"""
1 * CO   u0 {2,S} {3,D} {4,S}
2   Cd   u0 r1 {1,S} {6,D}
3   O2d  u0 {1,D}
4   O2s  u0 {1,S} {5,S}
5   H    u0 {4,S}
6   C    u0 r1 {2,D}
""",
	solute = SoluteData(
		S = 0.00400,
		B = 0.00940,
		E = 0.05806,
		L = 0.06004,
		A = 0.00477,
	),
	dataCount = DataCountGAV(
		S = 30,
		B = 30,
		E = 32,
		L = 30,
		A = 30,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 128,
	label = "Cds-Od(Cds-N3d)(OsH)",
	group = 
"""
1 * CO   u0 {2,S} {3,D} {4,S}
2   Cd   u0 {1,S} {6,D}
3   O2d  u0 {1,D}
4   O2s  u0 {1,S} {5,S}
5   H    u0 {4,S}
6   N3d  u0 {2,D}
""",
	solute = SoluteData(
		S = 0.09564,
		B = 0.06623,
		E = 0.01328,
		L = 0.08165,
		A = 0.02479,
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
	index = 129,
	label = "Cds-OdCb(OsH)",
	group = 
"""
1 * CO   u0 {2,S} {3,D} {4,S}
2   Cb   u0 {1,S}
3   O2d  u0 {1,D}
4   O2s  u0 {1,S} {5,S}
5   H    u0 {4,S}
""",
	solute = SoluteData(
		S = -0.00562,
		B = -0.07988,
		E = -0.03377,
		L = -0.09524,
		A = 0.09476,
	),
	dataCount = DataCountGAV(
		S = 194,
		B = 194,
		E = 197,
		L = 182,
		A = 194,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 130,
	label = "Cds-OdCsOs",
	group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cs u0 {1,S}
4   O2s u0 {1,S} {5,S}
5   R!H u0 {4,S}
""",
	solute = SoluteData(
		S = -0.12167,
		B = 0.02031,
		E = -0.08476,
		L = -0.16654,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 585,
		B = 569,
		E = 605,
		L = 540,
		A = 610,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 131,
	label = "Crds-OdCrsOrs",
	group = 
"""
1 * CO  u0 r1 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cs  u0 r1 {1,S}
4   O2s u0 r1 {1,S} {5,S}
5   R!H u0 {4,S}
""",
	solute = SoluteData(
		S = 0.36542,
		B = 0.05361,
		E = -0.01988,
		L = 0.81639,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 32,
		B = 32,
		E = 33,
		L = 29,
		A = 32,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 132,
	label = "Cds-OdCrsOs",
	group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cs u0 r1 {1,S}
4   O2s u0 {1,S} {5,S}
5   R!H u0 {4,S}
""",
	solute = SoluteData(
		S = 0.03325,
		B = -0.03120,
		E = -0.06544,
		L = 0.17235,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 23,
		B = 23,
		E = 23,
		L = 23,
		A = 23,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 133,
	label = "Cds-OdCdsOs",
	group = 
"""
1 * CO      u0 {2,D} {3,S} {4,S}
2   O2d      u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   O2s      u0 {1,S} {5,S}
5   R!H     u0 {4,S}
""",
	solute = u'Cds-O2d(Cds-Cd)O2s',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 134,
	label = "Crds-OdCrdsOrs",
	group = 
"""
1 * CO      u0 r1 {2,D} {3,S} {4,S}
2   O2d      u0 {1,D}
3   [Cd,CO] u0 r1 {1,S}
4   O2s      u0 r1 {1,S} {5,S}
5   R!H     u0 {4,S}
""",
	solute = SoluteData(
		S = 0.05757,
		B = 0.07131,
		E = 0.04521,
		L = 0.09985,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 16,
		B = 16,
		E = 16,
		L = 14,
		A = 16,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 135,
	label = "Cds-OdCrdsOs",
	group = 
"""
1 * CO      u0 {2,D} {3,S} {4,S}
2   O2d      u0 {1,D}
3   [Cd,CO] u0 r1 {1,S}
4   O2s      u0 {1,S} {5,S}
5   R!H     u0 {4,S}
""",
	solute = SoluteData(
		S = -0.05927,
		B = -0.05930,
		E = -0.02584,
		L = 0.00516,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 50,
		B = 50,
		E = 51,
		L = 32,
		A = 51,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 136,
	label = "Cds-O2d(Cds-O2d)O2s",
	group = 
"""
1 * CO u0 {2,S} {3,D} {4,S}
2   CO u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   O2s u0 {1,S} {6,S}
5   O2d u0 {2,D}
6   R!H u0 {4,S}
""",
	solute = SoluteData(
		S = -0.05886,
		B = 0.00323,
		E = -0.04972,
		L = -0.30062,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
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
	index = 137,
	label = "Cds-O2d(Cds-Cd)O2s",
	group = 
"""
1 * CO u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   O2s u0 {1,S} {6,S}
5   C  u0 {2,D}
6   R!H u0 {4,S}
""",
	solute = u'Cds-O2d(Cds-Cds)O2s',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 138,
	label = "Cds-O2d(Cds-Cds)O2s",
	group = 
"""
1 * CO u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   O2s u0 {1,S} {6,S}
5   Cd u0 {2,D}
6   R!H u0 {4,S}
""",
	solute = SoluteData(
		S = -0.09615,
		B = -0.04351,
		E = -0.08829,
		L = -0.22780,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 78,
		B = 77,
		E = 81,
		L = 70,
		A = 77,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 139,
	label = "Cds-OdCbOs",
	group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cb u0 {1,S}
4   O2s u0 {1,S} {5,S}
5   R!H u0 {4,S}
""",
	solute = SoluteData(
		S = -0.00034,
		B = -0.00910,
		E = -0.06551,
		L = -0.06894,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 182,
		B = 175,
		E = 190,
		L = 174,
		A = 197,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 140,
	label = "Cds-OdCC",
	group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   C  u0 {1,S}
4   C  u0 {1,S}
""",
	solute = u'Cds-OdCsCs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 141,
	label = "Cds-OdCsCs",
	group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
""",
	solute = SoluteData(
		S = -0.03370,
		B = 0.07988,
		E = -0.03325,
		L = 0.02304,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 122,
		B = 119,
		E = 127,
		L = 116,
		A = 128,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 142,
	label = "Crds-OdCrsCrs",
	group = 
"""
1 * CO u0 r1 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cs u0 r1 {1,S}
4   Cs u0 r1 {1,S}
""",
	solute = SoluteData(
		S = 0.02604,
		B = 0.06312,
		E = 0.05659,
		L = 0.73746,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 63,
		B = 65,
		E = 66,
		L = 57,
		A = 67,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 143,
	label = "Cds-OdCrsCrs",
	group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cs u0 r1 {1,S}
4   Cs u0 r1 {1,S}
""",
	solute = SoluteData(
		S = 0.07717,
		B = 0.00755,
		E = -0.01202,
		L = 0.16951,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
		E = 2,
		L = 2,
		A = 2,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 144,
	label = "Cds-OdCrsCs",
	group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cs u0 r1 {1,S}
4   Cs u0 {1,S}
""",
	solute = SoluteData(
		S = 0.15060,
		B = -0.00263,
		E = -0.00005,
		L = 0.68732,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 73,
		B = 73,
		E = 73,
		L = 54,
		A = 73,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 145,
	label = "Cds-OdCdsCs",
	group = 
"""
1 * CO      u0 {2,D} {3,S} {4,S}
2   O2d      u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
""",
	solute = u'Cds-O2d(Cds-Cd)Cs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 146,
	label = "Cds-O2d(Cds-O2d)Cs",
	group = 
"""
1 * CO u0 {2,S} {3,D} {4,S}
2   CO u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   Cs u0 {1,S}
5   O2d u0 {2,D}
""",
	solute = SoluteData(
		S = -0.05409,
		B = 0.00062,
		E = -0.05738,
		L = -0.38313,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 5,
		E = 5,
		L = 4,
		A = 5,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 147,
	label = "Cds-O2d(Cds-Cd)Cs",
	group = 
"""
1 * CO u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   Cs u0 {1,S}
5   C  u0 {2,D}
""",
	solute = SoluteData(
		S = 0.06456,
		B = 0.07691,
		E = -0.01848,
		L = 0.16970,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 16,
		B = 15,
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
	index = 148,
	label = "Crds-O2d(Crds-Crd)Crs",
	group = 
"""
1 * CO u0 r1 {2,S} {3,D} {4,S}
2   Cd u0 r1 {1,S} {5,D}
3   O2d u0 {1,D}
4   Cs u0 r1 {1,S}
5   C  u0 r1 {2,D}
""",
	solute = SoluteData(
		S = 0.15652,
		B = 0.04417,
		E = 0.15310,
		L = 0.48548,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 93,
		B = 93,
		E = 93,
		L = 79,
		A = 93,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 149,
	label = "Cds-O2d(Crds-Crd)Cs",
	group = 
"""
1 * CO u0 {2,S} {3,D} {4,S}
2   Cd u0 r1 {1,S} {5,D}
3   O2d u0 {1,D}
4   Cs u0 {1,S}
5   C  u0 r1 {2,D}
""",
	solute = SoluteData(
		S = -0.05204,
		B = 0.02571,
		E = -0.00388,
		L = 0.06904,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 8,
		B = 8,
		E = 10,
		L = 8,
		A = 12,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 150,
	label = "Cds-O2d(Cds-N3d)Cs",
	group = 
"""
1 * CO u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   Cs u0 {1,S}
5   N3d u0 {2,D}
""",
	solute = SoluteData(
		S = -0.06320,
		B = -0.02449,
		E = 0.01077,
		L = -0.18425,
		A = 0.00000,
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
	index = 151,
	label = "Cds-OdCdsCds",
	group = 
"""
1 * CO      u0 {2,D} {3,S} {4,S}
2   O2d      u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   [Cd,CO] u0 {1,S}
""",
	solute = u'Cds-O2d(Cds-Cd)(Cds-O2d)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 152,
	label = "Cds-O2d(Cds-Cd)(Cds-O2d)",
	group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cd u0 {1,S} {5,D}
4   CO u0 {1,S} {6,D}
5   C  u0 {3,D}
6   O2d u0 {4,D}
""",
	solute = u'Crds-O2d(Crds-Cd)(Crds-O2d)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 153,
	label = "Crds-O2d(Crds-Cd)(Crds-O2d)",
	group = 
"""
1 * CO u0 r1 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cd u0 r1 {1,S} {5,D}
4   CO u0 r1 {1,S} {6,D}
5   C  u0 {3,D}
6   O2d u0 {4,D}
""",
	solute = SoluteData(
		S = -0.07348,
		B = 0.02029,
		E = -0.03701,
		L = -0.78239,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 4,
		L = 3,
		A = 4,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 154,
	label = "Cds-O2d(Cds-Cd)(Cds-Cd)",
	group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cd u0 {1,S} {5,D}
4   Cd u0 {1,S} {6,D}
5   C  u0 {3,D}
6   C  u0 {4,D}
""",
	solute = u'Crds-O2d(Crds-Cd)(Crds-Cd)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 155,
	label = "Crds-O2d(Crds-Cd)(Crds-Cd)",
	group = 
"""
1 * CO u0 r1 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cd u0 r1 {1,S} {5,D}
4   Cd u0 r1 {1,S} {6,D}
5   C  u0 {3,D}
6   C  u0 {4,D}
""",
	solute = SoluteData(
		S = -0.04584,
		B = 0.04096,
		E = 0.07457,
		L = 0.35646,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 63,
		B = 63,
		E = 63,
		L = 36,
		A = 66,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 156,
	label = "Cds-O2d(Cds-Cd)(Cds-N3d)",
	group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cd u0 {1,S} {5,D}
4   Cd u0 {1,S} {6,D}
5   C  u0 {3,D}
6   N3d u0 {4,D}
""",
	solute = SoluteData(
		S = -0.04970,
		B = -0.08156,
		E = -0.04558,
		L = -0.08790,
		A = -0.09185,
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
	index = 157,
	label = "Cds-OdCbCs",
	group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
""",
	solute = SoluteData(
		S = -0.03897,
		B = -0.00319,
		E = -0.00714,
		L = -0.06151,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 104,
		B = 104,
		E = 106,
		L = 79,
		A = 105,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 158,
	label = "Crds-OdCbCrs",
	group = 
"""
1 * CO u0 r1 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cb u0 {1,S}
4   Cs u0 r1 {1,S}
""",
	solute = SoluteData(
		S = -0.03648,
		B = 0.01518,
		E = -0.04339,
		L = -0.21825,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 12,
		B = 12,
		E = 12,
		L = 11,
		A = 12,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 159,
	label = "Cds-OdCbCds",
	group = 
"""
1 * CO      u0 {2,D} {3,S} {4,S}
2   O2d      u0 {1,D}
3   Cb      u0 {1,S}
4   [Cd,CO] u0 {1,S}
""",
	solute = u'Cds-OdCb(Cds-O2d)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 160,
	label = "Cds-OdCb(Cds-O2d)",
	group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cb u0 {1,S}
4   CO u0 {1,S} {5,D}
5   O2d u0 {4,D}
""",
	solute = SoluteData(
		S = -0.02007,
		B = -0.04944,
		E = -0.02980,
		L = -0.51710,
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
	index = 161,
	label = "Cds-OdCb(Cds-Cd)",
	group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cb u0 {1,S}
4   Cd u0 {1,S} {5,D}
5   C  u0 {4,D}
""",
	solute = u'Crds-OdCb(Crds-Cd)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 162,
	label = "Crds-OdCb(Crds-Cd)",
	group = 
"""
1 * CO u0 r1 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cb u0 {1,S}
4   Cd u0 r1 {1,S} {5,D}
5   C  u0 {4,D}
""",
	solute = SoluteData(
		S = -0.08793,
		B = -0.10178,
		E = -0.07680,
		L = -0.14387,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 107,
		B = 107,
		E = 110,
		L = 106,
		A = 108,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 163,
	label = "Cds-OdCb(Crds-Cd)",
	group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cb u0 {1,S}
4   Cd u0 r1 {1,S} {5,D}
5   C  u0 {4,D}
""",
	solute = SoluteData(
		S = -0.01450,
		B = -0.05778,
		E = 0.05717,
		L = 0.27953,
		A = 0.01107,
	),
	dataCount = DataCountGAV(
		S = 4,
		B = 4,
		E = 4,
		L = 3,
		A = 4,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 164,
	label = "Cds-OdCb(Cds-N3d)",
	group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cb u0 {1,S}
4   Cd u0 {1,S} {5,D}
5   N3d u0 {4,D}
""",
	solute = u'Crds-OdCb(Crds-N3rd)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 165,
	label = "Crds-OdCb(Crds-N3rd)",
	group = 
"""
1 * CO u0 r1 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cb u0 {1,S}
4   Cd u0 r1 {1,S} {5,D}
5   N3d u0 r1 {4,D}
""",
	solute = SoluteData(
		S = -0.05307,
		B = -0.01848,
		E = -0.02205,
		L = -0.28226,
		A = -0.00122,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
		E = 2,
		L = 2,
		A = 2,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 166,
	label = "Cds-OdCbCb",
	group = 
"""
1 * CO u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
""",
	solute = SoluteData(
		S = 0.00554,
		B = -0.02378,
		E = -0.00392,
		L = -0.07243,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 22,
		B = 22,
		E = 23,
		L = 15,
		A = 26,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 167,
	label = "Crds-OdCbCb",
	group = 
"""
1 * CO u0 r1 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
""",
	solute = SoluteData(
		S = -0.13304,
		B = -0.12511,
		E = -0.09555,
		L = -0.41324,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 21,
		B = 22,
		E = 23,
		L = 21,
		A = 22,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 168,
	label = "Cds-Nd",
	group = 
"""
1 * Cd u0 {2,D}
2   N  u0 {1,D}
""",
	solute = u'Cds-N3dCC',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 169,
	label = "Cds-N3dCC",
	group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   N3d u0 {1,D}
3   C   u0 {1,S}
4   C   u0 {1,S}
""",
	solute = u'Cds-N3dCdCs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 170,
	label = "Cds-N3dCbCb",
	group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   N3d u0 {1,D}
3   Cb  u0 {1,S}
4   Cb  u0 {1,S}
""",
	solute = SoluteData(
		S = -0.03681,
		B = 0.06652,
		E = 0.00411,
		L = -0.20092,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 28,
		B = 28,
		E = 29,
		L = 11,
		A = 28,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 171,
	label = "Cds-N3dCbCs",
	group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   N3d u0 {1,D}
3   Cb  u0 {1,S}
4   Cs  u0 {1,S}
""",
	solute = SoluteData(
		S = -0.09288,
		B = -0.06035,
		E = 0.04350,
		L = 0.12467,
		A = 0.04837,
	),
	dataCount = DataCountGAV(
		S = 16,
		B = 16,
		E = 16,
		L = 16,
		A = 16,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 172,
	label = "Crds-N3rdCbCrs",
	group = 
"""
1 * Cd  u0 r1 {2,D} {3,S} {4,S}
2   N3d u0 r1 {1,D}
3   Cb  u0 {1,S}
4   Cs  u0 r1 {1,S}
""",
	solute = SoluteData(
		S = 0.02797,
		B = 0.06693,
		E = 0.10481,
		L = 0.28635,
		A = 0.04930,
	),
	dataCount = DataCountGAV(
		S = 4,
		B = 4,
		E = 5,
		L = 4,
		A = 4,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 173,
	label = "Crds-N3rdCbCs",
	group = 
"""
1 * Cd  u0 r1 {2,D} {3,S} {4,S}
2   N3d u0 r1 {1,D}
3   Cb  u0 {1,S}
4   Cs  u0 {1,S}
""",
	solute = SoluteData(
		S = -0.07304,
		B = 0.13635,
		E = 0.01905,
		L = -0.14087,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 2,
		E = 3,
		L = 3,
		A = 3,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 174,
	label = "Cds-N3dCbCd",
	group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   N3d u0 {1,D}
3   Cb  u0 {1,S}
4   [Cd,CO,CS] u0 {1,S}
""",
	solute = SoluteData(
		S = -0.18202,
		B = 0.12100,
		E = 0.08612,
		L = 0.23370,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 16,
		B = 14,
		E = 17,
		L = 13,
		A = 14,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 175,
	label = "Cds-N3dCb(Cd-O2d)",
	group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   N3d u0 {1,D}
3   Cb  u0 {1,S}
4   CO  u0 {1,S}
""",
	solute = SoluteData(
		S = -0.05465,
		B = -0.02885,
		E = -0.09320,
		L = -0.10844,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 5,
		E = 5,
		L = 4,
		A = 5,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 176,
	label = "Cds-N3dCsCs",
	group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   N3d u0 {1,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.11478,
		B = 0.04618,
		E = 0.06091,
		L = 0.40369,
		A = 0.00454,
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
	index = 177,
	label = "Crds-N3rdCrsCs",
	group = 
"""
1 * Cd  u0 r1 {2,D} {3,S} {4,S}
2   N3d u0 r1 {1,D}
3   Cs  u0 r1 {1,S}
4   Cs  u0 {1,S}
""",
	solute = SoluteData(
		S = -0.11569,
		B = -0.01990,
		E = -0.01764,
		L = -0.14520,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 12,
		B = 12,
		E = 12,
		L = 12,
		A = 12,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 178,
	label = "Crds-N3dCrsCrs",
	group = 
"""
1 * Cd  u0 r1 {2,D} {3,S} {4,S}
2   N3d u0 {1,D}
3   Cs  u0 r1 {1,S}
4   Cs  u0 r1 {1,S}
""",
	solute = SoluteData(
		S = 0.05706,
		B = 0.03230,
		E = 0.02313,
		L = 0.23506,
		A = 0.00129,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 5,
		E = 5,
		L = 5,
		A = 5,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 179,
	label = "Cds-N3dCdCs",
	group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   N3d u0 {1,D}
3   [Cd,CO,CS] u0 {1,S}
4   Cs  u0 {1,S}
""",
	solute = u'Cds-N3d(Cd-N3d)Cs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 180,
	label = "Cds-N3d(Cd-N3d)Cs",
	group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   N3d u0 {1,D}
3   Cd  u0 {1,S}, {5,D}
4   Cs  u0 {1,S}
5   N3d u0 {3,D}
""",
	solute = u'Crds-N3rd(Crd-N3rd)Cs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 181,
	label = "Crds-N3rd(Crd-N3rd)Cs",
	group = 
"""
1 * Cd  u0 r1 {2,D} {3,S} {4,S}
2   N3d u0 r1 {1,D}
3   Cd  u0 r1 {1,S}, {5,D}
4   Cs  u0 {1,S}
5   N3d u0 r1 {3,D}
""",
	solute = SoluteData(
		S = 0.00809,
		B = 0.06584,
		E = 0.02751,
		L = 0.16423,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 21,
		B = 21,
		E = 29,
		L = 13,
		A = 29,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 182,
	label = "Cds-N3d(Cd-Cd)Cs",
	group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   N3d u0 {1,D}
3   Cd  u0 {1,S}, {5,D}
4   Cs  u0 {1,S}
5   Cd  u0 {3,D}
""",
	solute = u'Crds-N3rd(Crd-Crd)Cs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 183,
	label = "Crds-N3rd(Crd-Crd)Cs",
	group = 
"""
1 * Cd  u0 r1 {2,D} {3,S} {4,S}
2   N3d u0 r1 {1,D}
3   Cd  u0 r1 {1,S}, {5,D}
4   Cs  u0 {1,S}
5   Cd  u0 r1 {3,D}
""",
	solute = SoluteData(
		S = 0.00520,
		B = 0.02661,
		E = 0.04547,
		L = 0.06160,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 84,
		B = 48,
		E = 90,
		L = 78,
		A = 89,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 184,
	label = "Cds-N3dCdCd",
	group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   N3d u0 {1,D}
3   [Cd,CO,CS] u0 {1,S}
4   [Cd,CO,CS] u0 {1,S}
""",
	solute = SoluteData(
		S = 0.00568,
		B = 0.04318,
		E = 0.03287,
		L = 0.33367,
		A = 0.05831,
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
	index = 185,
	label = "Crds-N3rdCrdCrd",
	group = 
"""
1 * Cd  u0 r1 {2,D} {3,S} {4,S}
2   N3d u0 r1 {1,D}
3   [Cd,CO,CS] u0 r1 {1,S}
4   [Cd,CO,CS] u0 r1 {1,S}
""",
	solute = SoluteData(
		S = -0.01981,
		B = -0.03783,
		E = 0.10647,
		L = 0.39653,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 44,
		B = 38,
		E = 49,
		L = 46,
		A = 46,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 186,
	label = "Crds-N3rdCrdCd",
	group = 
"""
1 * Cd  u0 r1 {2,D} {3,S} {4,S}
2   N3d u0 r1 {1,D}
3   [Cd,CO,CS] u0 r1 {1,S}
4   [Cd,CO,CS] u0 {1,S}
""",
	solute = SoluteData(
		S = 0.04783,
		B = 0.02773,
		E = 0.02226,
		L = 0.13322,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 9,
		B = 9,
		E = 9,
		L = 9,
		A = 9,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 187,
	label = "Cds-N3dCtC",
	group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   N3d u0 {1,D}
3   Ct  u0 {1,S}
4   C   u0 {1,S}
""",
	solute = SoluteData(
		S = -0.11547,
		B = -0.03873,
		E = -0.08101,
		L = -0.20247,
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
	index = 188,
	label = "Cds-N3dCO",
	group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   N3d u0 {1,D}
3   C   u0 {1,S}
4   O   u0 {1,S}
""",
	solute = u'Crds-N3rdCrO',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 189,
	label = "Crds-N3rdCrO",
	group = 
"""
1 * Cd  u0 r1 {2,D} {3,S} {4,S}
2   N3d u0 r1 {1,D}
3   C   u0 r1 {1,S}
4   O   u0 {1,S}
""",
	solute = SoluteData(
		S = -0.01188,
		B = -0.02839,
		E = 0.01501,
		L = 0.28115,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 22,
		B = 22,
		E = 25,
		L = 18,
		A = 25,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 190,
	label = "Crds-N3rdCOr",
	group = 
"""
1 * Cd  u0 r1 {2,D} {3,S} {4,S}
2   N3d u0 r1 {1,D}
3   C   u0 {1,S}
4   O   u0 r1 {1,S}
""",
	solute = SoluteData(
		S = 0.07892,
		B = 0.01192,
		E = 0.02933,
		L = 0.36501,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 3,
		L = 3,
		A = 3,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 191,
	label = "Cds-N3dCS",
	group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   N3d u0 {1,D}
3   C   u0 {1,S}
4   S   u0 {1,S}
""",
	solute = u'Crds-N3rdCrS',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 192,
	label = "Crds-N3rdCrS",
	group = 
"""
1 * Cd  u0 r1 {2,D} {3,S} {4,S}
2   N3d u0 r1 {1,D}
3   C   u0 r1 {1,S}
4   S   u0 {1,S}
""",
	solute = SoluteData(
		S = -0.01918,
		B = 0.03892,
		E = 0.08096,
		L = 0.26538,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 18,
		B = 18,
		E = 18,
		L = 18,
		A = 18,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 193,
	label = "Crds-N3rdCSr",
	group = 
"""
1 * Cd  u0 r1 {2,D} {3,S} {4,S}
2   N3d u0 r1 {1,D}
3   C   u0 {1,S}
4   S   u0 r1 {1,S}
""",
	solute = SoluteData(
		S = -0.01139,
		B = 0.00870,
		E = -0.01161,
		L = 0.06755,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 10,
		B = 10,
		E = 12,
		L = 7,
		A = 12,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 194,
	label = "Cds-N3dCH",
	group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   N3d u0 {1,D}
3   C   u0 {1,S}
4   H   u0 {1,S}
""",
	solute = u'Cds-N3dCdH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 195,
	label = "Cds-N3dCbH",
	group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   N3d u0 {1,D}
3   Cb  u0 {1,S}
4   H   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.00363,
		B = 0.02291,
		E = 0.02329,
		L = 0.04069,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 8,
		B = 8,
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
	index = 196,
	label = "Crds-N3rdCbH",
	group = 
"""
1 * Cd  u0 r1 {2,D} {3,S} {4,S}
2   N3d u0 r1 {1,D}
3   Cb  u0 {1,S}
4   H   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.14776,
		B = 0.07104,
		E = 0.00797,
		L = 0.11432,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 8,
		B = 7,
		E = 8,
		L = 7,
		A = 9,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 197,
	label = "Cds-N3dCdH",
	group = 
"""
1 * Cd          u0 {2,D} {3,S} {4,S}
2   N3d         u0 {1,D}
3   [Cd,CO,CS]  u0 {1,S}
4   H           u0 {1,S}
""",
	solute = u'Crds-N3rdCrdH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 198,
	label = "Crds-N3rdCrdH",
	group = 
"""
1 * Cd          u0 r1 {2,D} {3,S} {4,S}
2   N3d         u0 r1 {1,D}
3   [Cd,CO,CS]  u0 r1 {1,S}
4   H           u0 {1,S}
""",
	solute = SoluteData(
		S = 0.09529,
		B = 0.08537,
		E = 0.01173,
		L = 0.15595,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 305,
		B = 285,
		E = 337,
		L = 275,
		A = 334,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 199,
	label = "Cds-N3dCrdH",
	group = 
"""
1 * Cd          u0 {2,D} {3,S} {4,S}
2   N3d         u0 {1,D}
3   [Cd,CO,CS]  u0 r1 {1,S}
4   H           u0 {1,S}
""",
	solute = SoluteData(
		S = 0.02339,
		B = 0.04516,
		E = 0.06866,
		L = 0.07688,
		A = -0.01875,
	),
	dataCount = DataCountGAV(
		S = 4,
		B = 4,
		E = 4,
		L = 4,
		A = 4,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 200,
	label = "Cds-N3dCsH",
	group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   N3d u0 {1,D}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
""",
	solute = u'Cds-(N3d-(O-H))CsH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 201,
	label = "Crds-N3rdCrsH",
	group = 
"""
1 * Cd  u0 r1 {2,D} {3,S} {4,S}
2   N3d u0 r1 {1,D}
3   Cs  u0 r1 {1,S}
4   H   u0 {1,S}
""",
	solute = u'Crds-N3rdCrdH',
	dataCount = None,
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 202,
	label = "Cds-(N3d-(O-H))CsH",
	group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   N3d u0 {1,D} {5,S}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   O   u0 {2,S} {6,S}
6   H   u0 {5,S}
""",
	solute = SoluteData(
		S = 0.06672,
		B = 0.07557,
		E = 0.05253,
		L = 0.22243,
		A = 0.00459,
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
	index = 203,
	label = "Cds-N3dNN",
	group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   N3d u0 {1,D}
3   N   u0 {1,S}
4   N   u0 {1,S}
""",
	solute = u'Cds-N3dN3sN3s',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 204,
	label = "Cds-N3dN3sN3s",
	group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   N3d u0 {1,D}
3   N3s u0 {1,S}
4   N3s u0 {1,S}
""",
	solute = SoluteData(
		S = -0.05762,
		B = 0.11105,
		E = 0.09599,
		L = 0.24135,
		A = 0.11162,
	),
	dataCount = DataCountGAV(
		S = 28,
		B = 28,
		E = 30,
		L = 19,
		A = 28,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 205,
	label = "Crds-N3rdN3rsN3s",
	group = 
"""
1 * Cd  u0 r1 {2,D} {3,S} {4,S}
2   N3d u0 r1 {1,D}
3   N3s u0 r1 {1,S}
4   N3s u0 {1,S}
""",
	solute = SoluteData(
		S = 0.13118,
		B = 0.04032,
		E = 0.27899,
		L = 0.61708,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 27,
		B = 25,
		E = 28,
		L = 21,
		A = 28,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 206,
	label = "Cds-N3dN3dN3s",
	group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   N3d u0 {1,D}
3   N3d u0 {1,S}
4   N3s u0 {1,S}
""",
	solute = SoluteData(
		S = 0.02803,
		B = 0.15814,
		E = 0.12515,
		L = 0.26599,
		A = 0.01928,
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
	index = 207,
	label = "Crds-N3rdN3rdN3s",
	group = 
"""
1 * Cd  u0 r1 {2,D} {3,S} {4,S}
2   N3d u0 r1 {1,D}
3   N3d u0 r1 {1,S}
4   N3s u0 {1,S}
""",
	solute = SoluteData(
		S = 0.07647,
		B = -0.08450,
		E = 0.13324,
		L = 0.63295,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 53,
		B = 52,
		E = 53,
		L = 49,
		A = 53,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 208,
	label = "Cds-N3dN3sN5dc",
	group = 
"""
1 * Cd   u0 {2,D} {3,S} {4,S}
2   N3d  u0 {1,D}
3   N3s  u0 {1,S}
4   N5dc u0 {1,S}
""",
	solute = u'Crds-N3rdN3rsN5dc',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 209,
	label = "Crds-N3rdN3rsN5dc",
	group = 
"""
1 * Cd   u0 r1 {2,D} {3,S} {4,S}
2   N3d  u0 r1 {1,D}
3   N3s  u0 r1 {1,S}
4   N5dc u0 {1,S}
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
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 210,
	label = "Cds-N3dN3dN5dc",
	group = 
"""
1 * Cd   u0 {2,D} {3,S} {4,S}
2   N3d  u0 {1,D}
3   N3d  u0 {1,S}
4   N5dc u0 {1,S}
""",
	solute = u'Crds-N3rdN3rdN5dc',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 211,
	label = "Crds-N3rdN3rdN5dc",
	group = 
"""
1 * Cd   u0 r1 {2,D} {3,S} {4,S}
2   N3d  u0 r1 {1,D}
3   N3d  u0 r1 {1,S}
4   N5dc u0 {1,S}
""",
	solute = SoluteData(
		S = 0.10822,
		B = 0.00460,
		E = 0.03565,
		L = 0.12163,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 4,
		B = 4,
		E = 4,
		L = 4,
		A = 4,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 212,
	label = "Cds-N3dNC",
	group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   N3d u0 {1,D}
3   N   u0 {1,S}
4   C   u0 {1,S}
""",
	solute = u'Cds-N3dN3sC',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 213,
	label = "Cds-N3dN3sC",
	group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   N3d u0 {1,D}
3   N3s u0 {1,S}
4   C   u0 {1,S}
""",
	solute = SoluteData(
		S = -0.12638,
		B = 0.16950,
		E = 0.09143,
		L = 0.24028,
		A = 0.03016,
	),
	dataCount = DataCountGAV(
		S = 9,
		B = 9,
		E = 9,
		L = 9,
		A = 9,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 214,
	label = "Crds-N3rdN3rsCr",
	group = 
"""
1 * Cd  u0 r1 {2,D} {3,S} {4,S}
2   N3d u0 r1 {1,D}
3   N3s u0 r1 {1,S}
4   C   u0 r1 {1,S}
""",
	solute = SoluteData(
		S = 0.06492,
		B = 0.05554,
		E = 0.19152,
		L = 0.51827,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 49,
		B = 48,
		E = 49,
		L = 44,
		A = 49,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 215,
	label = "Crds-N3rdN3rsC",
	group = 
"""
1 * Cd  u0 r1 {2,D} {3,S} {4,S}
2   N3d u0 r1 {1,D}
3   N3s u0 r1 {1,S}
4   C   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.13198,
		B = 0.06486,
		E = 0.11619,
		L = 0.39926,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 27,
		B = 24,
		E = 27,
		L = 22,
		A = 27,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 216,
	label = "Crds-N3rdN3sCr",
	group = 
"""
1 * Cd  u0 r1 {2,D} {3,S} {4,S}
2   N3d u0 r1 {1,D}
3   N3s u0 {1,S}
4   C   u0 r1 {1,S}
""",
	solute = SoluteData(
		S = 0.04740,
		B = 0.00784,
		E = 0.07931,
		L = 0.37109,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 23,
		B = 23,
		E = 23,
		L = 21,
		A = 23,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 217,
	label = "Cds-N3dN3dC",
	group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   N3d u0 {1,D}
3   N3d u0 {1,S}
4   C   u0 {1,S}
""",
	solute = u'Crds-N3rdN3rdCr',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 218,
	label = "Crds-N3rdN3rdCr",
	group = 
"""
1 * Cd  u0 r1 {2,D} {3,S} {4,S}
2   N3d u0 r1 {1,D}
3   N3d u0 r1 {1,S}
4   C   u0 r1 {1,S}
""",
	solute = SoluteData(
		S = 0.10377,
		B = 0.11958,
		E = 0.17103,
		L = 0.41730,
		A = 0.07499,
	),
	dataCount = DataCountGAV(
		S = 14,
		B = 12,
		E = 14,
		L = 10,
		A = 14,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 219,
	label = "Crds-N3rdN3rdC",
	group = 
"""
1 * Cd  u0 r1 {2,D} {3,S} {4,S}
2   N3d u0 r1 {1,D}
3   N3d u0 r1 {1,S}
4   C   u0 {1,S}
""",
	solute = SoluteData(
		S = -0.01283,
		B = 0.08480,
		E = 0.04368,
		L = 0.29691,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 14,
		B = 15,
		E = 15,
		L = 14,
		A = 15,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 220,
	label = "Cds-N3dNO",
	group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   N3d u0 {1,D}
3   N   u0 {1,S}
4   O   u0 {1,S}
""",
	solute = u'Crds-N3rdNrO',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 221,
	label = "Crds-N3rdNrO",
	group = 
"""
1 * Cd  u0 r1 {2,D} {3,S} {4,S}
2   N3d u0 r1 {1,D}
3   N   u0 r1 {1,S}
4   O   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.01097,
		B = 0.02374,
		E = 0.01046,
		L = 0.20396,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 12,
		B = 12,
		E = 12,
		L = 11,
		A = 12,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 222,
	label = "Crds-N3rdNOr",
	group = 
"""
1 * Cd  u0 r1 {2,D} {3,S} {4,S}
2   N3d u0 r1 {1,D}
3   N   u0 {1,S}
4   O   u0 r1 {1,S}
""",
	solute = SoluteData(
		S = -0.01777,
		B = 0.08029,
		E = 0.07612,
		L = 0.03641,
		A = -0.03456,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 3,
		L = 3,
		A = 3,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 223,
	label = "Cds-N3dNS",
	group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   N3d u0 {1,D}
3   N   u0 {1,S}
4   S   u0 {1,S}
""",
	solute = u'Crds-N3rdNSr',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 224,
	label = "Crds-N3rdNrS",
	group = 
"""
1 * Cd  u0 r1 {2,D} {3,S} {4,S}
2   N3d u0 r1 {1,D}
3   N   u0 r1 {1,S}
4   S   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.09759,
		B = 0.00037,
		E = 0.17123,
		L = 0.62525,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 23,
		B = 23,
		E = 23,
		L = 23,
		A = 23,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 225,
	label = "Crds-N3rdNSr",
	group = 
"""
1 * Cd  u0 r1 {2,D} {3,S} {4,S}
2   N3d u0 r1 {1,D}
3   N   u0 {1,S}
4   S   u0 r1 {1,S}
""",
	solute = SoluteData(
		S = 0.13138,
		B = 0.01960,
		E = 0.16156,
		L = 0.55053,
		A = 0.07631,
	),
	dataCount = DataCountGAV(
		S = 27,
		B = 26,
		E = 28,
		L = 23,
		A = 27,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 226,
	label = "Cds-N3dNH",
	group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   N3d u0 {1,D}
3   N   u0 {1,S}
4   H   u0 {1,S}
""",
	solute = u'Cds-N3dN3sH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 227,
	label = "Cds-N3dN3sH",
	group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   N3d u0 {1,D}
3   N3s u0 {1,S}
4   H   u0 {1,S}
""",
	solute = u'Crds-N3rdN3rsH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 228,
	label = "Crds-N3rdN3rsH",
	group = 
"""
1 * Cd  u0 r1 {2,D} {3,S} {4,S}
2   N3d u0 r1 {1,D}
3   N3s u0 r1 {1,S}
4   H   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.26414,
		B = 0.16023,
		E = 0.06966,
		L = 0.43991,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 100,
		B = 97,
		E = 101,
		L = 92,
		A = 100,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 229,
	label = "Cds-N3dN3dH",
	group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   N3d u0 {1,D}
3   N3d u0 {1,S}
4   H   u0 {1,S}
""",
	solute = u'Crds-N3rdN3rdH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 230,
	label = "Crds-N3rdN3rdH",
	group = 
"""
1 * Cd  u0 r1 {2,D} {3,S} {4,S}
2   N3d u0 r1 {1,D}
3   N3d u0 r1 {1,S}
4   H   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.13060,
		B = 0.03256,
		E = 0.02325,
		L = 0.32982,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 62,
		B = 61,
		E = 65,
		L = 58,
		A = 67,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 231,
	label = "Cds-N3dOH",
	group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   N3d u0 {1,D}
3   O   u0 {1,S}
4   H   u0 {1,S}
""",
	solute = u'Crds-N3rdOrH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 232,
	label = "Crds-N3rdOrH",
	group = 
"""
1 * Cd  u0 r1 {2,D} {3,S} {4,S}
2   N3d u0 r1 {1,D}
3   O   u0 r1 {1,S}
4   H   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.05264,
		B = 0.04581,
		E = -0.06632,
		L = -0.09899,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 3,
		L = 2,
		A = 3,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 233,
	label = "Cds-N3dSS",
	group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   N3d u0 {1,D}
3   S   u0 {1,S}
4   S   u0 {1,S}
""",
	solute = u'Crds-N3rdSrS',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 234,
	label = "Crds-N3rdSrS",
	group = 
"""
1 * Cd  u0 r1 {2,D} {3,S} {4,S}
2   N3d u0 r1 {1,D}
3   S   u0 r1 {1,S}
4   S   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.02333,
		B = 0.01858,
		E = 0.08286,
		L = 0.25509,
		A = -0.01500,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 3,
		L = 3,
		A = 3,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 235,
	label = "Cds-N3dSH",
	group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   N3d u0 {1,D}
3   S   u0 {1,S}
4   H   u0 {1,S}
""",
	solute = u'Crds-N3rdSrH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 236,
	label = "Crds-N3rdSrH",
	group = 
"""
1 * Cd  u0 r1 {2,D} {3,S} {4,S}
2   N3d u0 r1 {1,D}
3   S   u0 r1 {1,S}
4   H   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.07801,
		B = 0.03393,
		E = 0.02476,
		L = 0.04437,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 5,
		E = 8,
		L = 4,
		A = 7,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 237,
	label = "Cds-N5dc",
	group = 
"""
1 * Cd   u0 {2,D}
2   N5dc u0 {1,D}
""",
	solute = u'Crds-N5rdc',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 238,
	label = "Crds-N5rdc",
	group = 
"""
1 * Cd   u0 r1 {2,D}
2   N5dc u0 r1 {1,D}
""",
	solute = SoluteData(
		S = 0.19908,
		B = 0.14855,
		E = 0.06814,
		L = 0.48605,
		A = 0.11753,
	),
	dataCount = DataCountGAV(
		S = 18,
		B = 18,
		E = 19,
		L = 18,
		A = 18,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 239,
	label = "Cds-Cd",
	group = 
"""
1 * Cd u0 {2,D}
2   C  u0 {1,D}
""",
	solute = u'Cds-CdCC',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 240,
	label = "Cds-CdHH",
	group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
	solute = u'Cds-CdsHH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 241,
	label = "Cds-CdsHH",
	group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.07968,
		B = 0.01758,
		E = 0.06146,
		L = 0.33013,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 361,
		B = 347,
		E = 379,
		L = 340,
		A = 380,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 242,
	label = "Cds-CrdsHH",
	group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 r1 {1,D}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.03399,
		B = 0.04100,
		E = 0.07796,
		L = 0.43327,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 40,
		B = 37,
		E = 40,
		L = 39,
		A = 42,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 243,
	label = "Cds-CddHH",
	group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
	solute = u'Cds-(Cdd-Cd)HH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 244,
	label = "Cds-(Cdd-Cd)HH",
	group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   C   u0 {2,D}
""",
	solute = SoluteData(
		S = 0.05813,
		B = 0.01946,
		E = 0.07261,
		L = 0.41198,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 6,
		B = 6,
		E = 6,
		L = 5,
		A = 9,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 245,
	label = "Cds-CdOsH",
	group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   O2s u0 {1,S}
4   H  u0 {1,S}
""",
	solute = u'Cds-CdsOsH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 246,
	label = "Cds-CdsOsH",
	group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   O2s u0 {1,S}
4   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.04765,
		B = 0.08459,
		E = 0.04788,
		L = 0.43043,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 14,
		B = 13,
		E = 13,
		L = 13,
		A = 14,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 247,
	label = "Crds-CrdsOrsH",
	group = 
"""
1 * Cd u0 r1 {2,D} {3,S} {4,S}
2   Cd u0 r1 {1,D}
3   O2s u0 r1 {1,S}
4   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.08597,
		B = 0.03952,
		E = 0.02714,
		L = 0.08372,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 83,
		B = 83,
		E = 87,
		L = 64,
		A = 93,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 248,
	label = "Cds-CdOsOs",
	group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
""",
	solute = u'Cds-CdsOsOs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 249,
	label = "Cds-CdsOsOs",
	group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
""",
	solute = u'Crds-CrdsOrsOs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 250,
	label = "Crds-CrdsOrsOs",
	group = 
"""
1 * Cd u0 r1 {2,D} {3,S} {4,S}
2   Cd u0 r1 {1,D}
3   O2s u0 r1 {1,S}
4   O2s u0 {1,S}
""",
	solute = SoluteData(
		S = 0.13378,
		B = 0.08774,
		E = 0.01198,
		L = 0.23277,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 10,
		B = 10,
		E = 11,
		L = 9,
		A = 11,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 251,
	label = "Cds-CdPH",
	group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   P  u0 {1,S}
4   H  u0 {1,S}
""",
	solute = None,
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 252,
	label = "Cds-CdP5dH",
	group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   P5d u0 {1,S}
4   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.03841,
		B = -0.00750,
		E = 0.03615,
		L = 0.22459,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 1,
		B = 1,
		E = 2,
		L = 1,
		A = 1,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 253,
	label = "Cds-CdNH",
	group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   N  u0 {1,S}
4   H  u0 {1,S}
""",
	solute = u'Cds-CdN3dH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 254,
	label = "Cds-CdN3sH",
	group = 
"""
1 * Cd  u0 {2,D} {5,S} {6,S}
2   Cd  u0 {1,D} {3,S} {4,S}
3   R   u0 {2,S}
4   R   u0 {2,S}
5   H   u0 {1,S}
6   N3s u0 {1,S}
""",
	solute = SoluteData(
		S = -0.06523,
		B = 0.10680,
		E = 0.24047,
		L = 0.42503,
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
	index = 255,
	label = "Crds-CrdN3rsH",
	group = 
"""
1 * Cd  u0 r1 {2,D} {5,S} {6,S}
2   Cd  u0 r1 {1,D} {3,S} {4,S}
3   R   u0 {2,S}
4   R   u0 {2,S}
5   H   u0 {1,S}
6   N3s u0 r1 {1,S}
""",
	solute = SoluteData(
		S = 0.25006,
		B = 0.14664,
		E = 0.12921,
		L = 0.65557,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 178,
		B = 164,
		E = 186,
		L = 141,
		A = 182,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 256,
	label = "Cds-CdN3dH",
	group = 
"""
1 * Cd  u0 {2,D} {5,S} {6,S}
2   Cd  u0 {1,D} {3,S} {4,S}
3   R   u0 {2,S}
4   R   u0 {2,S}
5   H   u0 {1,S}
6   N3d u0 {1,S}
""",
	solute = u'Crds-CrdN3rdH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 257,
	label = "Crds-CrdN3rdH",
	group = 
"""
1 * Cd  u0 r1 {2,D} {5,S} {6,S}
2   Cd  u0 r1 {1,D} {3,S} {4,S}
3   R   u0 {2,S}
4   R   u0 {2,S}
5   H   u0 {1,S}
6   N3d u0 r1 {1,S}
""",
	solute = SoluteData(
		S = 0.12495,
		B = 0.06331,
		E = 0.00670,
		L = 0.11994,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 297,
		B = 259,
		E = 322,
		L = 248,
		A = 321,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 258,
	label = "Cds-CdN5dcH",
	group = 
"""
1 * Cd   u0 {2,D} {5,S} {6,S}
2   Cd   u0 {1,D} {3,S} {4,S}
3   R    u0 {2,S}
4   R    u0 {2,S}
5   H    u0 {1,S}
6   N5dc u0 {1,S}
""",
	solute = SoluteData(
		S = 0.05238,
		B = 0.05110,
		E = -0.02091,
		L = 0.21000,
		A = 0.00197,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 5,
		E = 5,
		L = 4,
		A = 5,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 259,
	label = "Crds-CrdN5rdcH",
	group = 
"""
1 * Cd   u0 r1 {2,D} {5,S} {6,S}
2   Cd   u0 r1 {1,D} {3,S} {4,S}
3   R    u0 {2,S}
4   R    u0 {2,S}
5   H    u0 {1,S}
6   N5dc u0 r1 {1,S}
""",
	solute = SoluteData(
		S = 0.08058,
		B = 0.11574,
		E = 0.01135,
		L = 0.25513,
		A = 0.10422,
	),
	dataCount = DataCountGAV(
		S = 15,
		B = 15,
		E = 15,
		L = 15,
		A = 15,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 260,
	label = "Cds-CdNN",
	group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   N  u0 {1,S}
4   N  u0 {1,S}
""",
	solute = u'Cds-CdN3sN3d',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 261,
	label = "Cds-CdN3sN3s",
	group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   C   u0 {1,D}
3   N3s u0 {1,S}
4   N3s u0 {1,S}
""",
	solute = SoluteData(
		S = 0.09430,
		B = 0.15315,
		E = 0.12938,
		L = 0.65504,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 12,
		B = 12,
		E = 13,
		L = 6,
		A = 12,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 262,
	label = "Cds-CdN3sN3d",
	group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   C   u0 {1,D}
3   N3s u0 {1,S}
4   N3d u0 {1,S}
""",
	solute = u'Crds-CrdN3rsN3rd',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 263,
	label = "Crds-CrdN3rsN3rd",
	group = 
"""
1 * Cd  u0 r1 {2,D} {3,S} {4,S}
2   C   u0 r1 {1,D}
3   N3s u0 r1 {1,S}
4   N3d u0 r1 {1,S}
""",
	solute = SoluteData(
		S = 0.06871,
		B = 0.00064,
		E = 0.14722,
		L = 0.30053,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 47,
		B = 47,
		E = 48,
		L = 46,
		A = 47,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 264,
	label = "Crds-CrdN3sN3rd",
	group = 
"""
1 * Cd  u0 r1 {2,D} {3,S} {4,S}
2   C   u0 r1 {1,D}
3   N3s u0 {1,S}
4   N3d u0 r1 {1,S}
""",
	solute = SoluteData(
		S = 0.03200,
		B = -0.06231,
		E = 0.10723,
		L = 0.39227,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 22,
		B = 22,
		E = 24,
		L = 21,
		A = 23,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 265,
	label = "Cds-CdN3dN3d",
	group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   C   u0 {1,D}
3   N3d u0 {1,S}
4   N3d u0 {1,S}
""",
	solute = SoluteData(
		S = 0.01504,
		B = 0.07196,
		E = 0.09643,
		L = 0.17970,
		A = 0.06621,
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
	index = 266,
	label = "Cds-CdN3sN5dc",
	group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   C   u0 {1,D}
3   N3s u0 {1,S}
4   N5dc u0 {1,S}
""",
	solute = SoluteData(
		S = 0.00369,
		B = 0.00874,
		E = 0.05214,
		L = 0.12815,
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
	index = 267,
	label = "Cds-CdN3dN5dc",
	group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   C   u0 {1,D}
3   N3d u0 {1,S}
4   N5dc u0 {1,S}
""",
	solute = SoluteData(
		S = 0.02306,
		B = -0.03132,
		E = -0.07222,
		L = -0.14316,
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
	index = 268,
	label = "Cds-CdNO",
	group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   C   u0 {1,D}
3   N   u0 {1,S}
4   O   u0 {1,S}
""",
	solute = u'Cds-CdN3dO',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 269,
	label = "Cds-CdN3sO",
	group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   C   u0 {1,D}
3   N3s u0 {1,S}
4   O   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.05150,
		B = 0.10284,
		E = -0.01548,
		L = 0.42766,
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
	index = 270,
	label = "Cds-CdN3dO",
	group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   C   u0 {1,D}
3   N3d u0 {1,S}
4   O   u0 {1,S}
""",
	solute = SoluteData(
		S = -0.03404,
		B = -0.04538,
		E = -0.00417,
		L = 0.16282,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 9,
		B = 10,
		E = 11,
		L = 9,
		A = 10,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 271,
	label = "Cds-CdN5dcO",
	group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   C   u0 {1,D}
3   N5dc u0 {1,S}
4   O   u0 {1,S}
""",
	solute = SoluteData(
		S = -0.00581,
		B = 0.03189,
		E = 0.10957,
		L = 0.03950,
		A = -0.02945,
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
	index = 272,
	label = "Cds-CdNS",
	group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   C   u0 {1,D}
3   N   u0 {1,S}
4   S   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.02226,
		B = -0.01506,
		E = 0.07272,
		L = 0.08631,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 5,
		E = 5,
		L = 4,
		A = 5,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 273,
	label = "Cds-CdSH",
	group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   S  u0 {1,S}
4   H  u0 {1,S}
""",
	solute = u'Cds-CdsSH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 274,
	label = "Cds-CdsSH",
	group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   S  u0 {1,S}
4   H  u0 {1,S}
""",
	solute = u'Cds-CdsS2H',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 275,
	label = "Cds-CdsS2H",
	group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   S2s  u0 {1,S}
4   H  u0 {1,S}
""",
	solute = u'Crds-CrdsS2rH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 276,
	label = "Crds-CrdsS2rH",
	group = 
"""
1 * Cd u0 r1 {2,D} {3,S} {4,S}
2   Cd u0 r1 {1,D}
3   S2s  u0 r1 {1,S}
4   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.09462,
		B = 0.00309,
		E = 0.10521,
		L = 0.44391,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 77,
		B = 76,
		E = 81,
		L = 69,
		A = 79,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 277,
	label = "Cds-CdCH",
	group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   C  u0 {1,S}
4   H  u0 {1,S}
""",
	solute = u'Cds-CdsCsH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 278,
	label = "Cds-CdsCsH",
	group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cs u0 {1,S}
4   H  u0 {1,S}
""",
	solute = SoluteData(
		S = -0.02507,
		B = 0.00376,
		E = 0.03644,
		L = 0.24129,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 443,
		B = 437,
		E = 457,
		L = 410,
		A = 458,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 279,
	label = "Crds-CrdsCrsH",
	group = 
"""
1 * Cd u0 r1 {2,D} {3,S} {4,S}
2   Cd u0 r1 {1,D}
3   Cs u0 r1 {1,S}
4   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.08511,
		B = 0.03005,
		E = 0.09702,
		L = 0.54967,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 220,
		B = 201,
		E = 231,
		L = 194,
		A = 231,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 280,
	label = "Cds-CrdsCsH",
	group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 r1 {1,D}
3   Cs u0 {1,S}
4   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.00706,
		B = 0.03660,
		E = 0.06762,
		L = 0.45070,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 10,
		B = 10,
		E = 10,
		L = 10,
		A = 10,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 281,
	label = "Cds-CdsCrsH",
	group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cs u0 r1 {1,S}
4   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.00600,
		B = 0.02316,
		E = 0.12287,
		L = 0.69995,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 24,
		B = 23,
		E = 24,
		L = 23,
		A = 24,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 282,
	label = "Cds-CdsCdsH",
	group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cd      u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   H       u0 {1,S}
""",
	solute = u'Cds-Cd(Cd-O2d)H',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 283,
	label = "Cds-Cd(Cd-O2d)H",
	group = 
"""
1 * Cd u0 {2,S} {3,S} {4,D}
2   CO u0 {1,S} {5,D}
3   H  u0 {1,S}
4   Cd u0 {1,D}
5   O2d u0 {2,D}
""",
	solute = SoluteData(
		S = 0.03600,
		B = 0.07147,
		E = 0.09085,
		L = 0.30190,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 123,
		B = 122,
		E = 126,
		L = 114,
		A = 126,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 284,
	label = "Crds-Crd(Crd-O2d)H",
	group = 
"""
1 * Cd u0 r1 {2,S} {3,S} {4,D}
2   CO u0 r1 {1,S} {5,D}
3   H  u0 {1,S}
4   Cd u0 r1 {1,D}
5   O2d u0 {2,D}
""",
	solute = SoluteData(
		S = 0.12557,
		B = 0.05233,
		E = 0.03925,
		L = 0.31276,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 270,
		B = 268,
		E = 276,
		L = 218,
		A = 275,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 285,
	label = "Cds-Cd(Cd-N3d)H",
	group = 
"""
1 * Cd u0 {2,S} {3,S} {4,D}
2   Cd u0 {1,S} {5,D}
3   H  u0 {1,S}
4   Cd u0 {1,D}
5   N3d u0 {2,D}
""",
	solute = u'Crds-Crd(Crd-N3rd)H',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 286,
	label = "Crds-Crd(Crd-N3rd)H",
	group = 
"""
1 * Cd u0 r1 {2,S} {3,S} {4,D}
2   Cd u0 r1 {1,S} {5,D}
3   H  u0 {1,S}
4   Cd u0 r1 {1,D}
5   N3d u0 r1 {2,D}
""",
	solute = SoluteData(
		S = 0.18917,
		B = 0.05309,
		E = 0.07234,
		L = 0.56724,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 344,
		B = 303,
		E = 374,
		L = 320,
		A = 367,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 287,
	label = "Cds-Cd(Crd-N3rd)H",
	group = 
"""
1 * Cd u0 {2,S} {3,S} {4,D}
2   Cd u0 r1 {1,S} {5,D}
3   H  u0 {1,S}
4   Cd u0 {1,D}
5   N3d u0 r1 {2,D}
""",
	solute = SoluteData(
		S = -0.00344,
		B = 0.04936,
		E = 0.02238,
		L = 0.17804,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 1,
		B = 1,
		E = 1,
		L = 1,
		A = 1,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 288,
	label = "Cds-Cd(Cd-N5dc)H",
	group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   Cd  u0 {1,S} {5,D}
3   H   u0 {1,S}
4   Cd  u0 {1,D}
5   N5dc u0 {2,D}
""",
	solute = SoluteData(
		S = 0.18364,
		B = 0.13893,
		E = 0.06493,
		L = 0.53183,
		A = 0.09687,
	),
	dataCount = DataCountGAV(
		S = 17,
		B = 17,
		E = 18,
		L = 17,
		A = 17,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 289,
	label = "Cds-Cds(Cds-Cd)H",
	group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   H  u0 {1,S}
5   C  u0 {2,D}
""",
	solute = u'Cds-Cds(Cds-Cds)H',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 290,
	label = "Cds-Cds(Cds-Cds)H",
	group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   H  u0 {1,S}
5   Cd u0 {2,D}
""",
	solute = SoluteData(
		S = 0.04783,
		B = 0.03620,
		E = 0.11287,
		L = 0.56372,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 38,
		B = 38,
		E = 43,
		L = 36,
		A = 44,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 291,
	label = "Crds-Crds(Crds-Crds)H",
	group = 
"""
1 * Cd u0 r1 {2,S} {3,D} {4,S}
2   Cd u0 r1 {1,S} {5,D}
3   Cd u0 r1 {1,D}
4   H  u0 {1,S}
5   Cd u0 r1 {2,D}
""",
	solute = SoluteData(
		S = 0.10498,
		B = 0.03593,
		E = 0.12358,
		L = 0.52628,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 424,
		B = 374,
		E = 477,
		L = 387,
		A = 472,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 292,
	label = "Crds-Crds(Crds-Cds)H",
	group = 
"""
1 * Cd u0 r1 {2,S} {3,D} {4,S}
2   Cd u0 r1 {1,S} {5,D}
3   Cd u0 r1 {1,D}
4   H  u0 {1,S}
5   Cd u0 {2,D}
""",
	solute = SoluteData(
		S = 0.01586,
		B = -0.00161,
		E = 0.09037,
		L = 0.38978,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 5,
		E = 7,
		L = 5,
		A = 7,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 293,
	label = "Cds-Cds(Crds-Crds)H",
	group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 r1 {1,S} {5,D}
3   Cd u0 {1,D}
4   H  u0 {1,S}
5   Cd u0 r1 {2,D}
""",
	solute = SoluteData(
		S = 0.02247,
		B = 0.07088,
		E = 0.10137,
		L = 0.65942,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 9,
		B = 9,
		E = 10,
		L = 8,
		A = 10,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 294,
	label = "Cds-CdsCtH",
	group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Ct u0 {1,S}
4   H  u0 {1,S}
""",
	solute = u'Cds-CdsH(Ct-N3t)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 295,
	label = "Cds-CdsH(Ct-N3t)",
	group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Ct  u0 {1,S} {5,T}
3   Cd  u0 {1,D}
4   H   u0 {1,S}
5   N3t u0 {2,T}
""",
	solute = SoluteData(
		S = 0.11286,
		B = 0.03471,
		E = 0.12848,
		L = 0.44452,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 19,
		L = 19,
		A = 3,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 296,
	label = "Cds-CdsH(Ct-Ct)",
	group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Ct  u0 {1,S} {5,T}
3   Cd  u0 {1,D}
4   H   u0 {1,S}
5   Ct  u0 {2,T}
""",
	solute = SoluteData(
		S = 0.03008,
		B = 0.03313,
		E = 0.04987,
		L = 0.41557,
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
	index = 297,
	label = "Cds-CdsCbH",
	group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cb u0 {1,S}
4   H  u0 {1,S}
""",
	solute = SoluteData(
		S = -0.00296,
		B = -0.00815,
		E = 0.15448,
		L = 0.41715,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 72,
		B = 68,
		E = 96,
		L = 86,
		A = 80,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 298,
	label = "Crds-CrdsCbH",
	group = 
"""
1 * Cd u0 r1 {2,D} {3,S} {4,S}
2   Cd u0 r1 {1,D}
3   Cb u0 {1,S}
4   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.09331,
		B = -0.01751,
		E = 0.16906,
		L = 0.43575,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 155,
		B = 138,
		E = 162,
		L = 155,
		A = 155,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 299,
	label = "Cds-CddCH",
	group = 
"""
1 * Cd u0  {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   C  u0  {1,S}
4   H  u0  {1,S}
""",
	solute = SoluteData(
		S = 0.04061,
		B = 0.02717,
		E = 0.06992,
		L = 0.49604,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 7,
		B = 7,
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
	index = 300,
	label = "Cds-CdCO",
	group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   C  u0 {1,S}
4   O2s u0 {1,S}
""",
	solute = u'Cds-CdsCdsOs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 301,
	label = "Cds-CdsCdsOs",
	group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cd      u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   O2s      u0 {1,S}
""",
	solute = u'Cds-Cds(Cds-O2d)O2s',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 302,
	label = "Cds-Cds(Cds-O2d)O2s",
	group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   CO u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   O2s u0 {1,S}
5   O2d u0 {2,D}
""",
	solute = u'Crds-Crds(Crds-O2d)O2s',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 303,
	label = "Crds-Crds(Crds-O2d)O2s",
	group = 
"""
1 * Cd u0 r1 {2,S} {3,D} {4,S}
2   CO u0 r1 {1,S} {5,D}
3   Cd u0 r1 {1,D}
4   O2s u0 {1,S}
5   O2d u0 {2,D}
""",
	solute = u'Crds-Crds(Crds-O2d)(O2s-H)',
	dataCount = None,
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 304,
	label = "Crds-Crds(Crds-O2d)(O2s-H)",
	group = 
"""
1 * Cd u0 r1 {2,S} {3,D} {4,S}
2   CO u0 r1 {1,S} {5,D}
3   Cd u0 r1 {1,D}
4   O2s u0 {1,S} {6,S}
5   O2d u0 {2,D}
6   H   u0 {4,S}
""",
	solute = SoluteData(
		S = 0.14557,
		B = 0.04025,
		E = 0.05041,
		L = 0.36191,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 36,
		B = 36,
		E = 36,
		L = 19,
		A = 36,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 305,
	label = "Crds-Crds(Crds-O2d)(O2s-R)",
	group = 
"""
1 * Cd u0 r1 {2,S} {3,D} {4,S}
2   CO u0 r1 {1,S} {5,D}
3   Cd u0 r1 {1,D}
4   O2s u0 {1,S} {6,S}
5   O2d u0 {2,D}
6   R!H u0 {4,S}
""",
	solute = SoluteData(
		S = -0.22671,
		B = -0.00166,
		E = 0.02106,
		L = -0.28263,
		A = -0.36787,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
		E = 2,
		L = 2,
		A = 2,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 306,
	label = "Crds-Crds(Cds-O2d)O2rs",
	group = 
"""
1 * Cd u0 r1 {2,S} {3,D} {4,S}
2   CO u0 {1,S} {5,D}
3   Cd u0 r1 {1,D}
4   O2s u0 r1 {1,S}
5   O2d u0 {2,D}
""",
	solute = SoluteData(
		S = -0.00849,
		B = 0.05521,
		E = 0.07059,
		L = -0.02969,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 13,
		B = 13,
		E = 15,
		L = 8,
		A = 17,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 307,
	label = "Cds-Cds(Cds-N3d)O2s",
	group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   O2s u0 {1,S}
5   N3d u0 {2,D}
""",
	solute = u'Cds-Cds(Cds-N3d)(O2s-R)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 308,
	label = "Cds-Cds(Cds-N3d)(O2s-H)",
	group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   O2s u0 {1,S} {6,S}
5   N3d u0 {2,D}
6   H  u0 {4,S}
""",
	solute = u'Crds-Crds(Crds-Nr3d)(O2s-H)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 309,
	label = "Crds-Crds(Crds-Nr3d)(O2s-H)",
	group = 
"""
1 * Cd u0 r1 {2,S} {3,D} {4,S}
2   Cd u0 r1 {1,S} {5,D}
3   Cd u0 r1 {1,D}
4   O2s u0 {1,S} {6,S}
5   N3d u0 r1 {2,D}
6   H  u0 {4,S}
""",
	solute = SoluteData(
		S = 0.09273,
		B = 0.03153,
		E = 0.01827,
		L = 0.23382,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 15,
		B = 15,
		E = 15,
		L = 15,
		A = 15,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 310,
	label = "Cds-Cds(Cds-N3d)(O2s-R)",
	group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   O2s u0 {1,S} {6,S}
5   N3d u0 {2,D}
6   R!H u0 {4,S}
""",
	solute = SoluteData(
		S = 0.00526,
		B = 0.00965,
		E = 0.07260,
		L = 0.20994,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 9,
		B = 9,
		E = 10,
		L = 7,
		A = 10,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 311,
	label = "Cds-Cds(Cds-Cd)O2s",
	group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   O2s u0 {1,S}
5   C  u0 {2,D}
""",
	solute = u'Cds-Cds(Cds-Cds)O2s',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 312,
	label = "Cds-Cds(Cds-Cds)O2s",
	group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   O2s u0 {1,S}
5   Cd u0 {2,D}
""",
	solute = SoluteData(
		S = -0.01017,
		B = 0.00698,
		E = 0.10567,
		L = 0.68971,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 14,
		B = 14,
		E = 15,
		L = 13,
		A = 16,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 313,
	label = "Cds-CdsCbOs",
	group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cb u0 {1,S}
4   O2s u0 {1,S}
""",
	solute = u'Crds-CrdsCbOrs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 314,
	label = "Crds-CrdsCbOrs",
	group = 
"""
1 * Cd u0 r1 {2,D} {3,S} {4,S}
2   Cd u0 r1 {1,D}
3   Cb u0 {1,S}
4   O2s u0 r1 {1,S}
""",
	solute = SoluteData(
		S = -0.07990,
		B = -0.03418,
		E = 0.01291,
		L = -0.39831,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 54,
		B = 54,
		E = 56,
		L = 54,
		A = 55,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 315,
	label = "Crds-CrdsCbOs",
	group = 
"""
1 * Cd u0 r1 {2,D} {3,S} {4,S}
2   Cd u0 r1 {1,D}
3   Cb u0 {1,S}
4   O2s u0 {1,S}
""",
	solute = SoluteData(
		S = -0.11464,
		B = -0.01740,
		E = 0.00828,
		L = 0.01425,
		A = 0.04540,
	),
	dataCount = DataCountGAV(
		S = 9,
		B = 9,
		E = 9,
		L = 8,
		A = 9,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 316,
	label = "Cds-CdCsOs",
	group = 
"""
1 * Cd u0 {2,S} {3,S} {4,D}
2   Cs u0 {1,S}
3   O2s u0 {1,S}
4   C  u0 {1,D}
""",
	solute = u'Cds-CdsCsOs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 317,
	label = "Cds-CdsCsOs",
	group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cs u0 {1,S}
4   O2s u0 {1,S}
""",
	solute = SoluteData(
		S = 0.06818,
		B = -0.08846,
		E = 0.01118,
		L = 0.39983,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 9,
		B = 9,
		E = 9,
		L = 9,
		A = 9,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 318,
	label = "Crds-CrdsCsOrs",
	group = 
"""
1 * Cd u0 r1 {2,D} {3,S} {4,S}
2   Cd u0 r1 {1,D}
3   Cs u0 {1,S}
4   O2s u0 r1 {1,S}
""",
	solute = SoluteData(
		S = 0.10630,
		B = 0.01507,
		E = 0.04087,
		L = 0.29935,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 38,
		B = 38,
		E = 41,
		L = 34,
		A = 40,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 319,
	label = "Cds-CdCtOs",
	group = 
"""
1 * Cd u0 {2,S} {3,S} {4,D}
2   Ct u0 {1,S}
3   O2s u0 {1,S}
4   C  u0 {1,D}
""",
	solute = u'Crds-CrdCtOrs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 320,
	label = "Crds-CrdCtOrs",
	group = 
"""
1 * Cd u0 r1 {2,S} {3,S} {4,D}
2   Ct u0 {1,S}
3   O2s u0 r1 {1,S}
4   C  u0 r1 {1,D}
""",
	solute = u'Crds-CrdsCsOrs',
	dataCount = None,
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 321,
	label = "Cds-CdCS",
	group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   C  u0 {1,S}
4   S  u0 {1,S}
""",
	solute = u'Cds-CdsCsSs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 322,
	label = "Cds-CdsCsSs",
	group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cs u0 {1,S}
4   S  u0 {1,S}
""",
	solute = u'Cds-CdsCsS2',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 323,
	label = "Cds-CdsCsS2",
	group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cs u0 {1,S}
4   S2s  u0 {1,S}
""",
	solute = u'Crds-CrdsCsS2r',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 324,
	label = "Crds-CrdsCsS2r",
	group = 
"""
1 * Cd u0 r1 {2,D} {3,S} {4,S}
2   Cd u0 r1 {1,D}
3   Cs u0 {1,S}
4   S2s  u0 r1 {1,S}
""",
	solute = SoluteData(
		S = -0.00736,
		B = 0.02501,
		E = 0.05474,
		L = 0.40231,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 21,
		B = 21,
		E = 28,
		L = 25,
		A = 27,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 325,
	label = "Cds-CdsCdsSs",
	group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   [Cd,CO,CS] u0 {1,S}
4   S2s u0 {1,S}
""",
	solute = u'Cds-Cds(Cds-O2d)S2s',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 326,
	label = "Cds-Cds(Cds-Cd)S2s",
	group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   S2s u0 {1,S}
5   C  u0 {2,D}
""",
	solute = SoluteData(
		S = 0.12369,
		B = -0.04542,
		E = 0.11429,
		L = 0.60731,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 4,
		B = 4,
		E = 5,
		L = 3,
		A = 4,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 327,
	label = "Cds-Cds(Cds-O2d)S2s",
	group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   CO u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   S2s u0 {1,S}
5   O2d u0 {2,D}
""",
	solute = SoluteData(
		S = -0.00880,
		B = 0.01827,
		E = 0.04427,
		L = 0.07171,
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
	index = 328,
	label = "Cds-CdsCS6dd",
	group = 
"""
1 * Cd   u0 {2,D} {3,S} {4,S}
2   Cd   u0 {1,D}
3   C    u0 {1,S}
4   S6dd u0 {1,S}
""",
	solute = SoluteData(
		S = -0.03646,
		B = -0.04074,
		E = 0.03417,
		L = 0.07442,
		A = 0.03443,
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
	index = 329,
	label = "Cds-CdCC",
	group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   C  u0 {1,S}
4   C  u0 {1,S}
""",
	solute = u'Cds-CdsCsCs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 330,
	label = "Cds-CdsCsCs",
	group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
""",
	solute = SoluteData(
		S = 0.00326,
		B = 0.04603,
		E = -0.01615,
		L = 0.04799,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 115,
		B = 114,
		E = 117,
		L = 108,
		A = 116,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 331,
	label = "Crds-CrdsCrsCrs",
	group = 
"""
1 * Cd u0 r1 {2,D} {3,S} {4,S}
2   Cd u0 r1 {1,D}
3   Cs u0 r1 {1,S}
4   Cs u0 r1 {1,S}
""",
	solute = SoluteData(
		S = 0.20933,
		B = 0.12797,
		E = 0.14719,
		L = 0.79422,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 126,
		B = 125,
		E = 129,
		L = 102,
		A = 129,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 332,
	label = "Crds-CrdsCrsCs",
	group = 
"""
1 * Cd u0 r1 {2,D} {3,S} {4,S}
2   Cd u0 r1 {1,D}
3   Cs u0 r1 {1,S}
4   Cs u0 {1,S}
""",
	solute = SoluteData(
		S = -0.09114,
		B = 0.06344,
		E = 0.06020,
		L = 0.50316,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 102,
		B = 98,
		E = 106,
		L = 101,
		A = 106,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 333,
	label = "Cds-CrdsCsCs",
	group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 r1 {1,D}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
""",
	solute = SoluteData(
		S = 0.03246,
		B = -0.00645,
		E = 0.02374,
		L = 0.14733,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 11,
		B = 9,
		E = 13,
		L = 11,
		A = 13,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 334,
	label = "Cds-CdsCrsCs",
	group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cs u0 r1 {1,S}
4   Cs u0 {1,S}
""",
	solute = SoluteData(
		S = -0.12058,
		B = -0.00433,
		E = 0.04365,
		L = 0.40576,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 82,
		B = 74,
		E = 82,
		L = 79,
		A = 85,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 335,
	label = "Cds-CdsCdsCs",
	group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cd      u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
""",
	solute = u'Cds-Cd(Cds-O2d)Cs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 336,
	label = "Cds-Cd(Cds-O2d)Cs",
	group = 
"""
1 * Cd u0 {2,S} {3,S} {4,D}
2   CO u0 {1,S} {5,D}
3   Cs u0 {1,S}
4   Cd u0 {1,D}
5   O2d u0 {2,D}
""",
	solute = SoluteData(
		S = -0.13838,
		B = 0.08384,
		E = 0.03805,
		L = 0.12893,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 46,
		B = 45,
		E = 48,
		L = 45,
		A = 47,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 337,
	label = "Crds-Crd(Crds-O2d)Cs",
	group = 
"""
1 * Cd u0 r1 {2,S} {3,S} {4,D}
2   CO u0 r1 {1,S} {5,D}
3   Cs u0 {1,S}
4   Cd u0 r1 {1,D}
5   O2d u0 {2,D}
""",
	solute = SoluteData(
		S = -0.05898,
		B = 0.13315,
		E = 0.00357,
		L = 0.11483,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 31,
		B = 31,
		E = 31,
		L = 27,
		A = 33,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 338,
	label = "Cds-Cd(Cds-N3d)Cs",
	group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   Cd  u0 {1,S} {5,D}
3   Cs  u0 {1,S}
4   Cd  u0 {1,D}
5   N3d u0 {2,D}
""",
	solute = u'Crds-Crd(Crds-N3rd)Cs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 339,
	label = "Crds-Crd(Crds-N3rd)Cs",
	group = 
"""
1 * Cd  u0 r1 {2,S} {3,S} {4,D}
2   Cd  u0 r1 {1,S} {5,D}
3   Cs  u0 {1,S}
4   Cd  u0 r1 {1,D}
5   N3d u0 r1 {2,D}
""",
	solute = SoluteData(
		S = 0.10779,
		B = 0.06981,
		E = 0.05726,
		L = 0.58502,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 55,
		B = 34,
		E = 63,
		L = 50,
		A = 65,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 340,
	label = "Cds-Cds(Cds-Cd)Cs",
	group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   Cs u0 {1,S}
5   C  u0 {2,D}
""",
	solute = u'Cds-Cds(Cds-Cds)Cs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 341,
	label = "Cds-Cds(Cds-Cds)Cs",
	group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   Cs u0 {1,S}
5   Cd u0 {2,D}
""",
	solute = SoluteData(
		S = -0.00718,
		B = 0.02570,
		E = 0.04958,
		L = 0.36551,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 20,
		B = 20,
		E = 24,
		L = 19,
		A = 25,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 342,
	label = "Crds-Crds(Crds-Crds)Cs",
	group = 
"""
1 * Cd u0 r1 {2,S} {3,D} {4,S}
2   Cd u0 r1 {1,S} {5,D}
3   Cd u0 r1 {1,D}
4   Cs u0 {1,S}
5   Cd u0 r1 {2,D}
""",
	solute = SoluteData(
		S = 0.09342,
		B = 0.03768,
		E = 0.09907,
		L = 0.64588,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 145,
		B = 98,
		E = 171,
		L = 138,
		A = 172,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 343,
	label = "Crds-Cds(Crds-Crds)Crs",
	group = 
"""
1 * Cd u0 r1 {2,S} {3,D} {4,S}
2   Cd u0 r1 {1,S} {5,D}
3   Cd u0 {1,D}
4   Cs u0 r1 {1,S}
5   Cd u0 r1 {2,D}
""",
	solute = SoluteData(
		S = 0.01586,
		B = -0.00161,
		E = 0.09037,
		L = 0.38978,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 5,
		E = 7,
		L = 5,
		A = 7,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 344,
	label = "Cds-CdsCdsCds",
	group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cd      u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   [Cd,CO] u0 {1,S}
""",
	solute = u'Cds-Cds(Cds-Cd)(Cds-Cd)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 345,
	label = "Cds-Cds(Cds-O2d)(Cds-O2d)",
	group = 
"""
1 * Cd u0 {2,S} {3,S} {4,D}
2   CO u0 {1,S} {5,D}
3   CO u0 {1,S} {6,D}
4   Cd u0 {1,D}
5   O2d u0 {2,D}
6   O2d u0 {3,D}
""",
	solute = u'Crds-Crds(Crds-O2d)(Cds-O2d)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 346,
	label = "Crds-Crds(Crds-O2d)(Cds-O2d)",
	group = 
"""
1 * Cd u0 r1 {2,S} {3,S} {4,D}
2   CO u0 r1 {1,S} {5,D}
3   CO u0 {1,S} {6,D}
4   Cd u0 r1 {1,D}
5   O2d u0 {2,D}
6   O2d u0 {3,D}
""",
	solute = SoluteData(
		S = 0.02894,
		B = -0.00926,
		E = -0.01341,
		L = 0.24078,
		A = -0.14627,
	),
	dataCount = DataCountGAV(
		S = 21,
		B = 21,
		E = 22,
		L = 21,
		A = 21,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 347,
	label = "Cds-Cds(Cds-O2d)(Cds-Cd)",
	group = 
"""
1 * Cd u0 {2,S} {3,S} {4,D}
2   CO u0 {1,S} {6,D}
3   Cd u0 {1,S} {5,D}
4   Cd u0 {1,D}
5   C  u0 {3,D}
6   O2d u0 {2,D}
""",
	solute = u'Cds-Cds(Cds-O2d)(Cds-Cds)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 348,
	label = "Cds-Cds(Cds-O2d)(Cds-Cds)",
	group = 
"""
1 * Cd u0 {2,S} {3,S} {4,D}
2   CO u0 {1,S} {6,D}
3   Cd u0 {1,S} {5,D}
4   Cd u0 {1,D}
5   Cd u0 {3,D}
6   O2d u0 {2,D}
""",
	solute = u'Crds-Crds(Cds-O2d)(Crds-Crds)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 349,
	label = "Crds-Crds(Cds-O2d)(Crds-Crds)",
	group = 
"""
1 * Cd u0 r1 {2,S} {3,S} {4,D}
2   CO u0 {1,S} {6,D}
3   Cd u0 r1 {1,S} {5,D}
4   Cd u0 r1 {1,D}
5   Cd u0 r1 {3,D}
6   O2d u0 {2,D}
""",
	solute = SoluteData(
		S = -0.03800,
		B = 0.01238,
		E = 0.08541,
		L = 0.29580,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 69,
		B = 69,
		E = 71,
		L = 61,
		A = 73,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 350,
	label = "Cds-Cds(Cds-O2d)(Cds-N3d)",
	group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   CO  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {5,D}
4   Cd  u0 {1,D}
5   N3d u0 {3,D}
6   O2d u0 {2,D}
""",
	solute = u'Crds-Crds(Cds-O2d)(Crds-N3rd)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 351,
	label = "Crds-Crds(Crds-O2d)(Crds-N3rd)",
	group = 
"""
1 * Cd  u0 r1 {2,S} {3,S} {4,D}
2   CO  u0 r1 {1,S} {6,D}
3   Cd  u0 r1 {1,S} {5,D}
4   Cd  u0 r1 {1,D}
5   N3d u0 r1 {3,D}
6   O2d u0 {2,D}
""",
	solute = SoluteData(
		S = -0.02130,
		B = 0.05204,
		E = -0.00717,
		L = 0.02242,
		A = 0.06217,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 3,
		L = 3,
		A = 3,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 352,
	label = "Crds-Crds(Cds-O2d)(Crds-N3rd)",
	group = 
"""
1 * Cd  u0 r1 {2,S} {3,S} {4,D}
2   CO  u0 {1,S} {6,D}
3   Cd  u0 r1 {1,S} {5,D}
4   Cd  u0 r1 {1,D}
5   N3d u0 r1 {3,D}
6   O2d u0 {2,D}
""",
	solute = SoluteData(
		S = -0.06487,
		B = 0.01081,
		E = 0.04249,
		L = 0.18443,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 12,
		B = 12,
		E = 12,
		L = 7,
		A = 12,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 353,
	label = "Cds-Cds(Cds-N3d)(Cds-N3d)",
	group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {5,D}
4   Cd  u0 {1,D}
5   N3d u0 {3,D}
6   N3d u0 {2,D}
""",
	solute = SoluteData(
		S = 0.06092,
		B = -0.04807,
		E = 0.24820,
		L = 0.06570,
		A = -0.02368,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 3,
		L = 1,
		A = 3,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 354,
	label = "Cds-Cds(Cds-Cd)(Cds-N3d)",
	group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {5,D}
4   Cd  u0 {1,D}
5   N3d u0 {3,D}
6   C   u0 {2,D}
""",
	solute = u'Crds-Crds(Crds-Crd)(Crds-N3rd)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 355,
	label = "Crds-Crds(Crds-Crd)(Crds-N3rd)",
	group = 
"""
1 * Cd  u0 r1 {2,S} {3,S} {4,D}
2   Cd  u0 r1 {1,S} {6,D}
3   Cd  u0 r1 {1,S} {5,D}
4   Cd  u0 r1 {1,D}
5   N3d u0 r1 {3,D}
6   C   u0 r1 {2,D}
""",
	solute = SoluteData(
		S = 0.02899,
		B = 0.07090,
		E = 0.17860,
		L = 0.59976,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 36,
		B = 30,
		E = 38,
		L = 37,
		A = 34,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 356,
	label = "Cds-Cds(Cds-Cd)(Cds-Cd)",
	group = 
"""
1 * Cd u0 {2,S} {3,S} {4,D}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,S} {6,D}
4   Cd u0 {1,D}
5   C  u0 {2,D}
6   C  u0 {3,D}
""",
	solute = u'Cds-Cds(Cds-Cds)(Cds-Cds)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 357,
	label = "Cds-Cds(Cds-Cds)(Cds-Cds)",
	group = 
"""
1 * Cd u0 {2,S} {3,S} {4,D}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,S} {6,D}
4   Cd u0 {1,D}
5   Cd u0 {2,D}
6   Cd u0 {3,D}
""",
	solute = SoluteData(
		S = 0.09611,
		B = -0.00828,
		E = 0.15894,
		L = 0.61078,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 10,
		B = 10,
		E = 15,
		L = 13,
		A = 15,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 358,
	label = "Cds-CdsCtCs",
	group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
""",
	solute = u'Cds-CdCs(CtN3t)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 359,
	label = "Cds-CdCs(CtN3t)",
	group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cd  u0 {1,D} {5,S} {6,S}
3   Ct  u0 {1,S} {7,T}
4   Cs  u0 {1,S}
5   R   u0 {2,S}
6   R   u0 {2,S}
7   N3t u0 {3,T}
""",
	solute = SoluteData(
		S = 0.00353,
		B = 0.02517,
		E = -0.01696,
		L = 0.00197,
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
	index = 360,
	label = "Cds-CdsCtCds",
	group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cd      u0 {1,D}
3   Ct      u0 {1,S}
4   [Cd,CO] u0 {1,S}
""",
	solute = SoluteData(
		S = -0.00074,
		B = -0.00408,
		E = 0.04319,
		L = 0.16589,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 9,
		B = 9,
		E = 9,
		L = 9,
		A = 5,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 361,
	label = "Cds-CdsCtCt",
	group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
""",
	solute = u'Cds-Cd(CtN3t)(CtN3t)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 362,
	label = "Cds-Cd(CtN3t)(CtN3t)",
	group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   Ct  u0 {1,S} {5,T}
3   Ct  u0 {1,S} {6,T}
4   Cd  u0 {1,D}
5   N3t u0 {2,T}
6   N3t u0 {3,T}
""",
	solute = SoluteData(
		S = 0.06003,
		B = 0.05931,
		E = -0.02248,
		L = 0.09131,
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
	index = 363,
	label = "Cds-CdsCbCs",
	group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
""",
	solute = SoluteData(
		S = -0.01883,
		B = 0.00344,
		E = 0.01876,
		L = 0.31010,
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
	index = 364,
	label = "Crds-CrdsCbCrs",
	group = 
"""
1 * Cd u0 r1 {2,D} {3,S} {4,S}
2   Cd u0 r1 {1,D}
3   Cb u0 {1,S}
4   Cs u0 r1 {1,S}
""",
	solute = SoluteData(
		S = 0.05957,
		B = -0.03906,
		E = 0.10209,
		L = 0.50230,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 10,
		B = 10,
		E = 12,
		L = 11,
		A = 11,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 365,
	label = "Crds-CrdsCbCs",
	group = 
"""
1 * Cd u0 r1 {2,D} {3,S} {4,S}
2   Cd u0 r1 {1,D}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
""",
	solute = SoluteData(
		S = 0.00513,
		B = 0.03195,
		E = 0.13433,
		L = 0.49814,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 33,
		B = 31,
		E = 37,
		L = 34,
		A = 35,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 366,
	label = "Cds-CdsCbCds",
	group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cd      u0 {1,D}
3   Cb      u0 {1,S}
4   [Cd,CO] u0 {1,S}
""",
	solute = u'Cds-CdsCb(Cds-O2d)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 367,
	label = "Cds-CdsCb(Cds-O2d)",
	group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   CO u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   Cb u0 {1,S}
5   O2d u0 {2,D}
""",
	solute = SoluteData(
		S = -0.01724,
		B = -0.00834,
		E = 0.10738,
		L = 0.24795,
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
	index = 368,
	label = "Crds-CrdsCb(Crds-O2d)",
	group = 
"""
1 * Cd u0 r1 {2,S} {3,D} {4,S}
2   CO u0 r1 {1,S} {5,D}
3   Cd u0 r1 {1,D}
4   Cb u0 {1,S}
5   O2d u0 {2,D}
""",
	solute = SoluteData(
		S = -0.03975,
		B = 0.05229,
		E = 0.03889,
		L = -0.13396,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 39,
		B = 39,
		E = 39,
		L = 39,
		A = 39,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 369,
	label = "Cds-CdsCb(Cds-N3d)",
	group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,D}
4   Cb  u0 {1,S}
5   N3d u0 {2,D}
""",
	solute = SoluteData(
		S = -0.08646,
		B = -0.10783,
		E = 0.08029,
		L = 0.36628,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 3,
		E = 10,
		L = 8,
		A = 8,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 370,
	label = "Cds-Cds(Cds-Cd)Cb",
	group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   Cb u0 {1,S}
5   C  u0 {2,D}
""",
	solute = u'Cds-Cds(Cds-Cds)Cb',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 371,
	label = "Cds-Cds(Cds-Cds)Cb",
	group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   Cb u0 {1,S}
5   Cd u0 {2,D}
""",
	solute = SoluteData(
		S = -0.03073,
		B = 0.03633,
		E = 0.06458,
		L = 0.63031,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 18,
		B = 18,
		E = 23,
		L = 19,
		A = 23,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 372,
	label = "Cds-CdsCbCb",
	group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
""",
	solute = SoluteData(
		S = -0.06718,
		B = -0.04433,
		E = 0.08250,
		L = 0.14928,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 12,
		B = 12,
		E = 13,
		L = 12,
		A = 13,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 373,
	label = "Cds-CddCC",
	group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   C   u0 {1,S}
4   C   u0 {1,S}
""",
	solute = u'Cds-(Cdd-Cd)CC',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 374,
	label = "Cds-(Cdd-Cd)CC",
	group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   C   u0 {2,D}
""",
	solute = SoluteData(
		S = 0.01534,
		B = 0.00892,
		E = 0.01752,
		L = 0.17511,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 4,
		B = 4,
		E = 4,
		L = 1,
		A = 6,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 375,
	label = "Cds-CdCN",
	group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   C  u0 {1,S}
4   N  u0 {1,S}
""",
	solute = u'Cds-CdCsN3d',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 376,
	label = "Cds-CdCbN3s",
	group = 
"""
1 * Cd  u0 {2,D} {5,S} {6,S}
2   Cd  u0 {1,D} {3,S} {4,S}
3   R   u0 {2,S}
4   R   u0 {2,S}
5   Cb  u0 {1,S}
6   N3s u0 {1,S}
""",
	solute = SoluteData(
		S = 0.12008,
		B = 0.07004,
		E = 0.06553,
		L = 0.62998,
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
	index = 377,
	label = "Cds-CdCsN3s",
	group = 
"""
1 * Cd  u0 {2,D} {5,S} {6,S}
2   Cd  u0 {1,D} {3,S} {4,S}
3   R   u0 {2,S}
4   R   u0 {2,S}
5   Cs  u0 {1,S}
6   N3s u0 {1,S}
""",
	solute = SoluteData(
		S = 0.06071,
		B = 0.21262,
		E = 0.12735,
		L = 0.70798,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 66,
		B = 61,
		E = 69,
		L = 46,
		A = 65,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 378,
	label = "Cds-CdCdsN3s",
	group = 
"""
1 * Cd         u0 {2,D} {5,S} {6,S}
2   Cd         u0 {1,D} {3,S} {4,S}
3   R          u0 {2,S}
4   R          u0 {2,S}
5   [Cd,CO,Cs] u0 {1,S}
6   N3s        u0 {1,S}
""",
	solute = u'Cds-Cd(Cds-O2d)N3s',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 379,
	label = "Cds-Cd(Cds-O2d)N3s",
	group = 
"""
1 * Cd  u0 {2,D} {5,S} {6,S}
2   Cd  u0 {1,D} {3,S} {4,S}
3   R   u0 {2,S}
4   R   u0 {2,S}
5   CO  u0 {1,S} {7,D}
6   N3s u0 {1,S}
7   O2d u0 {5,D}
""",
	solute = SoluteData(
		S = -0.01501,
		B = 0.02492,
		E = 0.08663,
		L = 0.31055,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 53,
		B = 53,
		E = 55,
		L = 50,
		A = 53,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 380,
	label = "Cds-Cd(Cds-N3d)N3s",
	group = 
"""
1 * Cd  u0 {2,D} {5,S} {6,S}
2   Cd  u0 {1,D} {3,S} {4,S}
3   R   u0 {2,S}
4   R   u0 {2,S}
5   Cd  u0 {1,S} {7,D}
6   N3s u0 {1,S}
7   N3d u0 {5,D}
""",
	solute = SoluteData(
		S = 0.11330,
		B = 0.04604,
		E = 0.02887,
		L = 0.58012,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 20,
		B = 18,
		E = 21,
		L = 18,
		A = 22,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 381,
	label = "Cds-Cd(Cds-Cds)N3s",
	group = 
"""
1 * Cd  u0 {2,D} {5,S} {6,S}
2   Cd  u0 {1,D} {3,S} {4,S}
3   R   u0 {2,S}
4   R   u0 {2,S}
5   Cd  u0 {1,S} {7,D}
6   N3s u0 {1,S}
7   Cd  u0 {5,D}
""",
	solute = SoluteData(
		S = 0.00753,
		B = 0.08562,
		E = 0.12813,
		L = 0.57197,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 26,
		B = 26,
		E = 35,
		L = 25,
		A = 35,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 382,
	label = "Cds-CdCbN3d",
	group = 
"""
1 * Cd  u0 {2,D} {5,S} {6,S}
2   Cd  u0 {1,D} {3,S} {4,S}
3   R   u0 {2,S}
4   R   u0 {2,S}
5   Cb  u0 {1,S}
6   N3d u0 {1,S}
""",
	solute = SoluteData(
		S = 0.01947,
		B = 0.02515,
		E = 0.09000,
		L = 0.20944,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 11,
		B = 11,
		E = 12,
		L = 8,
		A = 11,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 383,
	label = "Cds-CdCsN3d",
	group = 
"""
1 * Cd  u0 {2,D} {5,S} {6,S}
2   Cd  u0 {1,D} {3,S} {4,S}
3   R   u0 {2,S}
4   R   u0 {2,S}
5   Cs  u0 {1,S}
6   N3d u0 {1,S}
""",
	solute = SoluteData(
		S = -0.03247,
		B = 0.15030,
		E = -0.00959,
		L = 0.05341,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 105,
		B = 77,
		E = 125,
		L = 96,
		A = 124,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 384,
	label = "Cds-CdCdsN3d",
	group = 
"""
1 * Cd         u0 {2,D} {5,S} {6,S}
2   Cd         u0 {1,D} {3,S} {4,S}
3   R          u0 {2,S}
4   R          u0 {2,S}
5   [Cd,CO,Cs] u0 {1,S}
6   N3d        u0 {1,S}
""",
	solute = SoluteData(
		S = 0.05925,
		B = -0.00538,
		E = 0.01742,
		L = 0.17340,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 46,
		B = 46,
		E = 51,
		L = 40,
		A = 51,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 385,
	label = "Cds-CdCtN3d",
	group = 
"""
1 * Cd   u0 {2,D} {5,S} {6,S}
2   Cd   u0 {1,D} {3,S} {4,S}
3   R    u0 {2,S}
4   R    u0 {2,S}
5   Ct   u0 {1,S}
6   N3d  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.00287,
		B = -0.03744,
		E = -0.04962,
		L = -0.10150,
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
	index = 386,
	label = "Cds-CdCN5dc",
	group = 
"""
1 * Cd   u0 {2,D} {5,S} {6,S}
2   Cd   u0 {1,D} {3,S} {4,S}
3   R    u0 {2,S}
4   R    u0 {2,S}
5   C    u0 {1,S}
6   N5dc u0 {1,S}
""",
	solute = SoluteData(
		S = 0.08474,
		B = -0.01509,
		E = 0.04048,
		L = 0.40020,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 14,
		B = 14,
		E = 19,
		L = 14,
		A = 15,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 387,
	label = "Cds-Sd",
	group = 
"""
1 * CS u0 {2,D}
2   S  u0 {1,D}
""",
	solute = u'Cds-S2dNN',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 388,
	label = "Cds-S2dNN",
	group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   N   u0 {1,S}
4   N   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.08127,
		B = 0.13686,
		E = 0.17091,
		L = 0.52156,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 18,
		B = 18,
		E = 19,
		L = 14,
		A = 19,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 389,
	label = "Cds-S2dNC",
	group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   N   u0 {1,S}
4   C   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.25290,
		B = 0.03884,
		E = 0.12637,
		L = 0.67317,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 10,
		B = 10,
		E = 10,
		L = 9,
		A = 12,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 390,
	label = "Cds-S2dNS",
	group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   N   u0 {1,S}
4   S   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.06140,
		B = -0.00583,
		E = 0.14690,
		L = 0.31565,
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
	index = 391,
	label = "Cds-S2dOC",
	group = 
"""
1 * CS u0 {2,D} {3,S} {4,S}
2   S2d u0 {1,D}
3   O  u0 {1,S}
4   C  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.00785,
		B = 0.00141,
		E = -0.04527,
		L = 0.11173,
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
	index = 392,
	label = "Cs",
	group = 
"""
1 * Cs u0
""",
	solute = u'Cs-CCCC',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 393,
	label = "Cs-P3s",
	group = 
"""
1 * Cs u0 {2,S}
2   P3s u0 {1,S}
""",
	solute = u'Cs-P3sHHH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 394,
	label = "Cs-P3sHHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   P3s u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = -0.06356,
		B = 0.12722,
		E = 0.09695,
		L = 0.60735,
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
	index = 395,
	label = "Cs-P3sRHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   P3s u0 {1,S}
3   R!H u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = u'Cs-P3sCsHH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 396,
	label = "Cs-P3sCsHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   P3s u0 {1,S}
3   Cs u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = u'Cs-P3sHHH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 397,
	label = "Cs-P5d",
	group = 
"""
1 * Cs u0 {2,S}
2   P5d u0 {1,S}
""",
	solute = u'Cs-P5dRHH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 398,
	label = "Cs-P5dHHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   P5d u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = u'Cs-(P5d-O2d)HHH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 399,
	label = "Cs-(P5d-O2d)HHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   P5d u0 {1,S} {6,D}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   O2d u0 {2,D}
""",
	solute = SoluteData(
		S = 0.12367,
		B = 0.08738,
		E = -0.02010,
		L = 0.20421,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 5,
		E = 12,
		L = 5,
		A = 14,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 400,
	label = "Cs-P5dRHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   P5d u0 {1,S}
3   R!H u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = u'Cs-P5dCHH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 401,
	label = "Cs-P5dNHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   P5d u0 {1,S}
3   N  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = u'Cs-P5dN3sHH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 402,
	label = "Cs-P5dN3sHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   P5d u0 {1,S}
3   N3s u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = u'Cs-P5dCsHH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 403,
	label = "Cs-P5dCHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   P5d u0 {1,S}
3   C  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = u'Cs-P5dCsHH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 404,
	label = "Cs-P5dCsHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   P5d u0 {1,S}
3   Cs u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.09328,
		B = 0.29014,
		E = 0.00630,
		L = 0.57279,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 9,
		B = 9,
		E = 21,
		L = 9,
		A = 25,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 405,
	label = "Cs-P5dOsHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 {1,S}
3   P5d u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = -0.05564,
		B = 0.06896,
		E = 0.06334,
		L = 0.07604,
		A = 0.05232,
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
	index = 407,
	label = "Cs-P5dOCH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   P5d u0 {1,S}
3   O  u0 {1,S}
4   C  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.00845,
		B = 0.07668,
		E = 0.08441,
		L = 0.19730,
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
	index = 408,
	label = "Cs-P5d(O-H)CH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   P5d u0 {1,S}
3   O  u0 {1,S} {6,S}
4   C  u0 {1,S}
5   H  u0 {1,S}
6   H  u0 {3,S}
""",
	solute = SoluteData(
		S = 0.06329,
		B = -0.00847,
		E = 0.04766,
		L = 0.23122,
		A = 0.03096,
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
	index = 409,
	label = "Cs-P5dOCC",
	group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   P5d  u0 {1,S}
3   O   u0 {1,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
""",
	solute = u'Cs-P5dOCC',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 410,
	label = "Cs-P5dOCC",
	group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   P5d u0 {1,S}
3   O2s u0 {1,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
""",
	solute = u'Cs-P5dOCH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 411,
	label = "Cs-P5d(O-H)CC",
	group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   P5d u0 {1,S}
3   O2s u0 {1,S} {6,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
6   H   u0 {3,S}
""",
	solute = u'Cs-P5d(O-H)CH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 413,
	label = "Cs-P5dCCC",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   P5d u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
5   C  u0 {1,S}
""",
	solute = u'Cs-P5dCsCsCs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 414,
	label = "Cs-P5dCsCsCs",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   P5d u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
""",
	solute = u'Cs-P5dCsHH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 415,
	label = "Cs-NHHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   N  u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = u'Cs-N3sHHH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 416,
	label = "Cs-N3sHHH",
	group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3s u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
	solute = u'Cs-(N3s-RR)HHH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 417,
	label = "Cs-N3rsHHH",
	group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3s u0 r1 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.21254,
		B = 0.14235,
		E = 0.03871,
		L = 0.49095,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 165,
		B = 165,
		E = 169,
		L = 142,
		A = 165,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 418,
	label = "Cs-(N3s-RH)HHH",
	group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3s u0 {1,S} {6,S} {7,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {2,S}
7   R!H u0 {2,S}
""",
	solute = SoluteData(
		S = 0.13514,
		B = 0.17889,
		E = 0.04890,
		L = 0.53868,
		A = 0.03602,
	),
	dataCount = DataCountGAV(
		S = 92,
		B = 88,
		E = 99,
		L = 71,
		A = 95,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 419,
	label = "Cs-(N3s-RR)HHH",
	group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3s u0 {1,S} {6,S} {7,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   R!H u0 {2,S}
7   R!H u0 {2,S}
""",
	solute = SoluteData(
		S = 0.13036,
		B = 0.14475,
		E = 0.07419,
		L = 0.64399,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 228,
		B = 229,
		E = 248,
		L = 190,
		A = 257,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 420,
	label = "Cs-N3dHHH",
	group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3d u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
	solute = u'Cs-(N3dCd)HHH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 421,
	label = "Cs-(N3dCd)HHH",
	group = 
"""
1 * Cs       u0 {2,S} {3,S} {4,S} {5,S}
2   N3d      u0 {1,S} {6,D}
3   H        u0 {1,S}
4   H        u0 {1,S}
5   H        u0 {1,S}
6   [Cd,Cdd] u0 {2,D}
""",
	solute = SoluteData(
		S = 0.12541,
		B = 0.05892,
		E = 0.05968,
		L = 0.34286,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 5,
		E = 6,
		L = 3,
		A = 6,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 422,
	label = "Cs-N5cHHH",
	group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   N    u0 c+1  {1,S}
3   H    u0 {1,S}
4   H    u0 {1,S}
5   H    u0 {1,S}
""",
	solute = SoluteData(
		S = 0.08297,
		B = -0.00887,
		E = -0.04654,
		L = 0.32829,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
		E = 6,
		L = 2,
		A = 2,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 423,
	label = "Cs-NNHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   N  u0 {1,S}
3   N  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.16930,
		B = 0.04448,
		E = 0.15883,
		L = 0.81401,
		A = 0.00000,
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
	index = 424,
	label = "Cs-NOHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   N  u0 {1,S}
3   O  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = u'Cs-N3sOHH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 425,
	label = "Cs-N3sOHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   N3s u0 {1,S}
3   O  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = u'Cs-N3rsOHH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 426,
	label = "Cs-N3rsOHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   N3s u0 r1 {1,S}
3   O  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.01595,
		B = 0.08998,
		E = 0.15129,
		L = 0.57385,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 45,
		B = 45,
		E = 46,
		L = 38,
		A = 45,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 427,
	label = "Cs-NSHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   N  u0 {1,S}
3   S  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = -0.06086,
		B = 0.03327,
		E = 0.12442,
		L = 0.10093,
		A = -0.00272,
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
	index = 428,
	label = "Cs-NCHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   N  u0 {1,S}
3   C  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = u'Cs-NCsHH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 429,
	label = "Cs-NCbHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   N  u0 {1,S}
3   Cb u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.07724,
		B = 0.06578,
		E = 0.03677,
		L = 0.41610,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 52,
		B = 52,
		E = 53,
		L = 31,
		A = 55,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 430,
	label = "Crs-NrCbHH",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   N  u0 r1 {1,S}
3   Cb u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.12096,
		B = 0.04510,
		E = 0.09099,
		L = 0.33701,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 5,
		E = 5,
		L = 5,
		A = 5,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 431,
	label = "Cs-NrCbHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   N  u0 r1 {1,S}
3   Cb u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.11405,
		B = -0.01551,
		E = 0.04266,
		L = 0.37098,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 34,
		B = 34,
		E = 34,
		L = 29,
		A = 34,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 432,
	label = "Cs-NCsHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   N  u0 {1,S}
3   Cs u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = u'Cs-N3sCsHH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 433,
	label = "Cs-N3sCsHH",
	group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3s u0 {1,S}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.09432,
		B = 0.17831,
		E = 0.05618,
		L = 0.64379,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 401,
		B = 396,
		E = 420,
		L = 349,
		A = 421,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 434,
	label = "Crs-N3rsCrsHH",
	group = 
"""
1 * Cs  u0 r1 {2,S} {3,S} {4,S} {5,S}
2   N3s u0 r1 {1,S}
3   Cs  u0 r1 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.13555,
		B = 0.17421,
		E = 0.08666,
		L = 0.70570,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 257,
		B = 258,
		E = 269,
		L = 237,
		A = 264,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 435,
	label = "Cs-N3rsCsHH",
	group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3s u0 r1 {1,S}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.06269,
		B = 0.12307,
		E = 0.04171,
		L = 0.57835,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 144,
		B = 144,
		E = 151,
		L = 121,
		A = 146,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 436,
	label = "Cs-N3dCHH",
	group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3d u0 {1,S}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
	solute = u'Cs-(N3d-Cd)CsHH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 437,
	label = "Cs-(N3d-Nd)CsHH",
	group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3d u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   N   u0 {2,D}
""",
	solute = SoluteData(
		S = 0.16105,
		B = 0.04298,
		E = 0.06468,
		L = 0.39388,
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
	index = 438,
	label = "Cs-(N3d-Cd)CsHH",
	group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3d u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   Cd  u0 {2,D}
""",
	solute = SoluteData(
		S = 0.08232,
		B = 0.21370,
		E = 0.01305,
		L = 0.49914,
		A = 0.11280,
	),
	dataCount = DataCountGAV(
		S = 15,
		B = 16,
		E = 16,
		L = 13,
		A = 16,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 439,
	label = "Cs-(N3d-Cdd)CsHH",
	group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3d u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
""",
	solute = SoluteData(
		S = 0.07643,
		B = 0.08052,
		E = 0.03855,
		L = 0.37266,
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
	index = 440,
	label = "Cs-N5cCsHH",
	group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N   u0 c+1 {1,S}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.29454,
		B = 0.05443,
		E = 0.01156,
		L = 0.61309,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 12,
		B = 12,
		E = 16,
		L = 8,
		A = 13,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 441,
	label = "Cs-NCdsHH",
	group = 
"""
1 * Cs         u0 {2,S} {3,S} {4,S} {5,S}
2   N          u0 {1,S}
3   [Cd,CO,CS] u0 {1,S}
4   H          u0 {1,S}
5   H          u0 {1,S}
""",
	solute = u'Cs-N(Cds-Cd)HH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 442,
	label = "Cs-N(Cds-O2d)HH",
	group = 
"""
1 * Cs         u0 {2,S} {3,S} {4,S} {5,S}
2   N          u0 {1,S}
3   CO         u0 {1,S}
4   H          u0 {1,S}
5   H          u0 {1,S}
""",
	solute = SoluteData(
		S = 0.21646,
		B = 0.02862,
		E = 0.09309,
		L = 0.76065,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 39,
		B = 39,
		E = 40,
		L = 24,
		A = 39,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 443,
	label = "Cs-N(Cds-O2d(OsH))HH",
	group = 
"""
1 * Cs         u0 {2,S} {3,S} {4,S} {5,S}
2   N          u0 {1,S}
3   CO         u0 {1,S} {6,S}
4   H          u0 {1,S}
5   H          u0 {1,S}
6   O2s        u0 {3,S} {7,S}
7   H          u0 {6,S}
""",
	solute = SoluteData(
		S = 0.24685,
		B = -0.02241,
		E = 0.12665,
		L = 0.58548,
		A = -0.08198,
	),
	dataCount = DataCountGAV(
		S = 30,
		B = 30,
		E = 30,
		L = 29,
		A = 30,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 444,
	label = "Cs-N(Cds-Cd)HH",
	group = 
"""
1 * Cs         u0 {2,S} {3,S} {4,S} {5,S}
2   N          u0 {1,S}
3   Cd         u0 {1,S} {6,D}
4   H          u0 {1,S}
5   H          u0 {1,S}
6   C          u0 {3,D}
""",
	solute = SoluteData(
		S = 0.03449,
		B = 0.13209,
		E = 0.05279,
		L = 0.61179,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 36,
		B = 36,
		E = 40,
		L = 31,
		A = 39,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 445,
	label = "Cs-N(Cds-N3d)HH",
	group = 
"""
1 * Cs         u0 {2,S} {3,S} {4,S} {5,S}
2   N          u0 {1,S}
3   Cd         u0 {1,S} {6,D}
4   H          u0 {1,S}
5   H          u0 {1,S}
6   N3d        u0 {3,D}
""",
	solute = SoluteData(
		S = 0.21086,
		B = 0.11833,
		E = -0.03720,
		L = 0.70966,
		A = -0.00185,
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
	index = 446,
	label = "Cs-NCtHH",
	group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N   u0 {1,S}
3   Ct  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.03381,
		B = 0.04164,
		E = 0.02801,
		L = 0.18082,
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
	index = 447,
	label = "Cs-NNCH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   N  u0 {1,S}
3   N  u0 {1,S}
4   C  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = -0.01005,
		B = 0.10779,
		E = 0.13837,
		L = 0.61712,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 7,
		B = 7,
		E = 7,
		L = 7,
		A = 8,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 448,
	label = "Cs-NOCH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   N  u0 {1,S}
3   O  u0 {1,S}
4   C  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = -0.24017,
		B = 0.08511,
		E = 0.12095,
		L = 0.28252,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 30,
		B = 30,
		E = 30,
		L = 26,
		A = 30,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 449,
	label = "Cs-NSCH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   N  u0 {1,S}
3   S  u0 {1,S}
4   C  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = -0.11441,
		B = -0.03339,
		E = 0.14626,
		L = 0.13370,
		A = -0.13097,
	),
	dataCount = DataCountGAV(
		S = 26,
		B = 26,
		E = 26,
		L = 25,
		A = 26,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 450,
	label = "Cs-NCCH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   N  u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.09180,
		B = 0.08140,
		E = -0.00598,
		L = 0.48297,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 21,
		B = 21,
		E = 22,
		L = 19,
		A = 22,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 451,
	label = "Cs-NCsCsH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   N  u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
""",
	solute = u'Cs-N3sCsCsH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 452,
	label = "Cs-N3sCsCsH",
	group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3s u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.03117,
		B = 0.18969,
		E = 0.05167,
		L = 0.62509,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 90,
		B = 88,
		E = 93,
		L = 85,
		A = 94,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 453,
	label = "Crs-N3rsCrsCrsH",
	group = 
"""
1 * Cs  u0 r1 {2,S} {3,S} {4,S} {5,S}
2   N3s u0 r1 {1,S}
3   Cs  u0 r1 {1,S}
4   Cs  u0 r1 {1,S}
5   H   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.06273,
		B = 0.18852,
		E = 0.15623,
		L = 0.62870,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 45,
		B = 45,
		E = 46,
		L = 42,
		A = 45,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 454,
	label = "Crs-N3sCrsCrsH",
	group = 
"""
1 * Cs  u0 r1 {2,S} {3,S} {4,S} {5,S}
2   N3s u0 {1,S}
3   Cs  u0 r1 {1,S}
4   Cs  u0 r1 {1,S}
5   H   u0 {1,S}
""",
	solute = SoluteData(
		S = -0.00333,
		B = 0.17505,
		E = 0.05637,
		L = 0.53423,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 56,
		B = 55,
		E = 61,
		L = 50,
		A = 57,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 455,
	label = "Crs-N3rsCrsCsH",
	group = 
"""
1 * Cs  u0 r1 {2,S} {3,S} {4,S} {5,S}
2   N3s u0 r1 {1,S}
3   Cs  u0 r1 {1,S}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.07907,
		B = 0.15884,
		E = 0.08263,
		L = 0.72863,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 25,
		B = 23,
		E = 26,
		L = 23,
		A = 25,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 456,
	label = "Cs-N3dCsCsH",
	group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3d u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
""",
	solute = SoluteData(
		S = -0.19109,
		B = 0.14875,
		E = 0.25485,
		L = 0.49593,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 10,
		B = 11,
		E = 11,
		L = 10,
		A = 13,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 457,
	label = "Cs-N5dcCsCsH",
	group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N5dc u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.09035,
		B = 0.03713,
		E = 0.01712,
		L = 0.42741,
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
	index = 458,
	label = "Cs-NCsCdsH",
	group = 
"""
1 * Cs         u0 {2,S} {3,S} {4,S} {5,S}
2   N          u0 {1,S}
3   Cs         u0 {1,S}
4   [Cd,CO,CS] u0 {1,S}
5   H          u0 {1,S}
""",
	solute = u'Cs-NCs(Cds-O2d)H',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 459,
	label = "Cs-NCs(Cds-O2d)H",
	group = 
"""
1 * Cs         u0 {2,S} {3,S} {4,S} {5,S}
2   N          u0 {1,S}
3   Cs         u0 {1,S}
4   CO         u0 {1,S}
5   H          u0 {1,S}
""",
	solute = SoluteData(
		S = 0.05416,
		B = 0.20770,
		E = 0.10886,
		L = 0.74604,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 73,
		B = 73,
		E = 73,
		L = 69,
		A = 73,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 460,
	label = "Cs-NCs(Cds-Cd)H",
	group = 
"""
1 * Cs         u0 {2,S} {3,S} {4,S} {5,S}
2   N          u0 {1,S}
3   Cs         u0 {1,S}
4   Cd         u0 {1,S} {6,D}
5   H          u0 {1,S}
6   C          u0 {4,D}
""",
	solute = SoluteData(
		S = -0.02779,
		B = 0.03849,
		E = 0.04723,
		L = 0.17215,
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
	index = 461,
	label = "Cs-NOCR",
	group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N   u0 {1,S}
3   O   u0 {1,S}
4   C   u0 {1,S}
5   R!H u0 {1,S}
""",
	solute = SoluteData(
		S = -0.00518,
		B = -0.03614,
		E = 0.14251,
		L = 0.34035,
		A = -0.00235,
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
	index = 462,
	label = "Cs-NCCC",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   N  u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
5   C  u0 {1,S}
""",
	solute = u'Cs-NCsCsCs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 463,
	label = "Cs-NCsCsCs",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   N  u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
""",
	solute = u'Cs-N3CsCsCs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 464,
	label = "Cs-N3CsCsCs",
	group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   [N3s,N3d] u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.09535,
		B = 0.20273,
		E = 0.02178,
		L = 0.61692,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 41,
		B = 41,
		E = 41,
		L = 37,
		A = 44,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 465,
	label = "Cs-N5dcCsCsCs",
	group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N5dc u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.16390,
		B = 0.03806,
		E = 0.02741,
		L = 0.53216,
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
	index = 466,
	label = "Cs-NCdCbCb",
	group = 
"""
1 * Cs          u0 {2,S} {3,S} {4,S} {5,S}
2   N           u0 {1,S}
3   [Cd,CO,CS]  u0 {1,S}
4   Cb          u0 {1,S}
5   Cb          u0 {1,S}
""",
	solute = u'Cs-N3s(Cd-O2d)CbCb',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 467,
	label = "Cs-N3s(Cd-O2d)CbCb",
	group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3s u0 {1,S}
3   CO  u0 {1,S}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.01426,
		B = 0.02508,
		E = -0.21400,
		L = -0.07816,
		A = 0.05944,
	),
	dataCount = DataCountGAV(
		S = 15,
		B = 15,
		E = 15,
		L = 8,
		A = 15,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 468,
	label = "Cs-NNNN",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   N  u0 {1,S}
3   N  u0 {1,S}
4   N  u0 {1,S}
5   N  u0 {1,S}
""",
	solute = u'Cs-N5dcN5dcN5dcN5dc',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 469,
	label = "Cs-N5dcN5dcN5dcN5dc",
	group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   N5dc u0 {1,S}
3   N5dc u0 {1,S}
4   N5dc u0 {1,S}
5   N5dc u0 {1,S}
""",
	solute = SoluteData(
		S = -0.18222,
		B = -0.02717,
		E = -0.10655,
		L = -0.53262,
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
	index = 470,
	label = "Cs-OsHHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.10606,
		B = 0.06237,
		E = 0.04228,
		L = 0.42904,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 663,
		B = 626,
		E = 691,
		L = 619,
		A = 692,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 471,
	label = "Cs-OsOsHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 {1,S}
3   O2s u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.03318,
		B = -0.02621,
		E = 0.00000,
		L = 0.11764,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 17,
		B = 6,
		E = 31,
		L = 17,
		A = 36,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 472,
	label = "Crs-OrsOrsHH",
	group = 
"""
1 * Cs  u0 r1 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 r1 {1,S}
3   O2s u0 r1 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.13088,
		B = 0.01101,
		E = 0.08958,
		L = -0.02162,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 20,
		B = 20,
		E = 23,
		L = 21,
		A = 22,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 473,
	label = "Cs-OsSHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 {1,S}
3   S u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = u'Cs-OsS2HH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 474,
	label = "Cs-OsS2HH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 {1,S}
3   S2s u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.02108,
		B = 0.12338,
		E = 0.09977,
		L = 0.47438,
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
	index = 475,
	label = "Cs-OsOsOsH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 {1,S}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   H  u0 {1,S}
""",
	solute = u'Cs-OsOsHH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 476,
	label = "Cs-OsOsOsCs",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 {1,S}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   Cs u0 {1,S}
""",
	solute = u'Cs-CsCsOsOs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 477,
	label = "Cs-CHHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = u'Cs-CsHHH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 478,
	label = "Cs-CsHHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.00000,
		B = 0.00000,
		E = 0.00000,
		L = 0.40084,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 3619,
		B = 3489,
		E = 3855,
		L = 3315,
		A = 3882,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 479,
	label = "Cs-CdsHHH",
	group = 
"""
1 * Cs         u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO,CS] u0 {1,S}
3   H          u0 {1,S}
4   H          u0 {1,S}
5   H          u0 {1,S}
""",
	solute = u'Cs-(Cds-Cd)HHH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 480,
	label = "Cs-(Cds-O2d)HHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   O2d u0 {2,D}
""",
	solute = SoluteData(
		S = 0.17391,
		B = 0.05563,
		E = 0.03381,
		L = 0.30890,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 462,
		B = 445,
		E = 490,
		L = 407,
		A = 502,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 481,
	label = "Cs-(Cds-Cd)HHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
	solute = u'Cs-(Cds-Cds)HHH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 482,
	label = "Cs-(Cds-Cds)HHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
	solute = SoluteData(
		S = 0.08299,
		B = 0.00670,
		E = 0.02660,
		L = 0.46561,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 577,
		B = 518,
		E = 620,
		L = 552,
		A = 615,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 483,
	label = "Cs-(Cds-Cdd)HHH",
	group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
""",
	solute = u'Cs-(Cds-Cdd-Cd)HHH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 484,
	label = "Cs-(Cds-Cdd-Cd)HHH",
	group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   C   u0 {3,D}
""",
	solute = SoluteData(
		S = 0.03345,
		B = 0.01592,
		E = 0.05347,
		L = 0.37636,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 7,
		B = 7,
		E = 7,
		L = 3,
		A = 8,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 485,
	label = "Cs-(Cd-Nd)HHH",
	group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   N   u0 {2,D}
""",
	solute = SoluteData(
		S = 0.07608,
		B = 0.09777,
		E = -0.00141,
		L = 0.44489,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 126,
		B = 102,
		E = 136,
		L = 110,
		A = 134,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 486,
	label = "Cs-(Cd-S2d)SHHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   S2d u0 {2,D}
""",
	solute = SoluteData(
		S = 0.07306,
		B = 0.07796,
		E = 0.04554,
		L = 0.10310,
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
	index = 487,
	label = "Cs-CtHHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = u'Cs-(Ct-Ct)HHH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 488,
	label = "Cs-(Ct-Ct)HHH",
	group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S} {6,T}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   Ct  u0 {2,T}
""",
	solute = SoluteData(
		S = -0.03605,
		B = -0.04365,
		E = 0.04106,
		L = -0.02686,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 20,
		B = 21,
		E = 23,
		L = 15,
		A = 22,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 489,
	label = "Cs-CbHHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.03408,
		B = -0.05849,
		E = 0.01760,
		L = 0.11622,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 774,
		B = 720,
		E = 824,
		L = 736,
		A = 808,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 490,
	label = "Cs-CCHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = u'Cs-CsCsHH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 491,
	label = "Crs-CrCrHH",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   C  u0 r1 {1,S}
3   C  u0 r1 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = u'Crs-CrsCrsHH',
	dataCount = None,
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 492,
	label = "Crs-CrsCrsHH",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 r1 {1,S}
3   Cs u0 r1 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.03683,
		B = 0.00000,
		E = 0.03901,
		L = 0.49867,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 901,
		B = 872,
		E = 952,
		L = 827,
		A = 949,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 493,
	label = "Crs-CrdsCrsHH",
	group = 
"""
1 * Cs         u0 r1 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO,CS] u0 r1 {1,S}
3   Cs         u0 r1 {1,S}
4   H          u0 {1,S}
5   H          u0 {1,S}
""",
	solute = u'Crs-(Crds-O2d)CrsHH',
	dataCount = None,
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 494,
	label = "Crs-(Crds-Cd)CrsHH",
	group = 
"""
1 * Cs         u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cd         u0 r1 {1,S} {6,D}
3   Cs         u0 r1 {1,S}
4   H          u0 {1,S}
5   H          u0 {1,S}
6   C          u0 {2,D}
""",
	solute = SoluteData(
		S = 0.07413,
		B = 0.04837,
		E = 0.06595,
		L = 0.54998,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 50,
		B = 45,
		E = 51,
		L = 49,
		A = 51,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 495,
	label = "Crs-(Crds-Crd)CrsHH",
	group = 
"""
1 * Cs         u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cd         u0 r1 {1,S} {6,D}
3   Cs         u0 r1 {1,S}
4   H          u0 {1,S}
5   H          u0 {1,S}
6   C          u0 r1 {2,D}
""",
	solute = SoluteData(
		S = 0.00045,
		B = 0.00690,
		E = 0.04775,
		L = 0.44018,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 253,
		B = 242,
		E = 260,
		L = 222,
		A = 260,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 496,
	label = "Crs-(Crds-O2d)CrsHH",
	group = 
"""
1 * Cs         u0 r1 {2,S} {3,S} {4,S} {5,S}
2   CO         u0 r1 {1,S} {6,D}
3   Cs         u0 r1 {1,S}
4   H          u0 {1,S}
5   H          u0 {1,S}
6   O2d        u0 {2,D}
""",
	solute = SoluteData(
		S = 0.22154,
		B = 0.08339,
		E = -0.03379,
		L = 0.24870,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 190,
		B = 192,
		E = 195,
		L = 170,
		A = 193,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 497,
	label = "Crs-(Crds-Nd)CrsHH",
	group = 
"""
1 * Cs         u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cd         u0 r1 {1,S} {6,D}
3   Cs         u0 r1 {1,S}
4   H          u0 {1,S}
5   H          u0 {1,S}
6   N          u0 {2,D}
""",
	solute = u'Crs-(Crds-N3d)CrsHH',
	dataCount = None,
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 498,
	label = "Crs-(Crds-Nrd)CrsHH",
	group = 
"""
1 * Cs         u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cd         u0 r1 {1,S} {6,D}
3   Cs         u0 r1 {1,S}
4   H          u0 {1,S}
5   H          u0 {1,S}
6   N          u0 r1 {2,D}
""",
	solute = u'Crs-(Crds-N3rd)CrsHH',
	dataCount = None,
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 499,
	label = "Crs-(Crds-N3rd)CrsHH",
	group = 
"""
1 * Cs         u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cd         u0 r1 {1,S} {6,D}
3   Cs         u0 r1 {1,S}
4   H          u0 {1,S}
5   H          u0 {1,S}
6   N3d        u0 r1 {2,D}
""",
	solute = SoluteData(
		S = 0.04761,
		B = 0.04624,
		E = 0.03455,
		L = 0.30997,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 4,
		L = 3,
		A = 3,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 500,
	label = "Crs-(Crds-N3d)CrsHH",
	group = 
"""
1 * Cs         u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cd         u0 r1 {1,S} {6,D}
3   Cs         u0 r1 {1,S}
4   H          u0 {1,S}
5   H          u0 {1,S}
6   N3d        u0 {2,D}
""",
	solute = SoluteData(
		S = 0.11411,
		B = 0.06461,
		E = 0.04627,
		L = 0.47012,
		A = 0.00258,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 5,
		E = 5,
		L = 5,
		A = 5,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 501,
	label = "Crs-CrdsCrdsHH",
	group = 
"""
1 * Cs         u0 r1 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO,CS] u0 r1 {1,S}
3   [Cd,CO,CS] u0 r1 {1,S}
4   H          u0 {1,S}
5   H          u0 {1,S}
""",
	solute = SoluteData(
		S = 0.04471,
		B = -0.00313,
		E = 0.02770,
		L = 0.24533,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 25,
		B = 23,
		E = 26,
		L = 24,
		A = 26,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 502,
	label = "Crs-CbCrsHH",
	group = 
"""
1 * Cs         u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cb         u0 r1 {1,S}
3   Cs         u0 r1 {1,S}
4   H          u0 {1,S}
5   H          u0 {1,S}
""",
	solute = SoluteData(
		S = 0.01848,
		B = 0.02290,
		E = 0.01687,
		L = 0.33855,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 93,
		B = 88,
		E = 101,
		L = 93,
		A = 99,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 503,
	label = "Crs-CbCrdsHH",
	group = 
"""
1 * Cs         u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cb         u0 r1 {1,S}
3   [Cd,CO,CS] u0 r1 {1,S}
4   H          u0 {1,S}
5   H          u0 {1,S}
""",
	solute = SoluteData(
		S = 0.12606,
		B = -0.00293,
		E = 0.05426,
		L = 0.18254,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 12,
		B = 12,
		E = 13,
		L = 13,
		A = 13,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 504,
	label = "Crs-CbCbHH",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 r1 {1,S}
3   Cb u0 r1 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = -0.00861,
		B = -0.05467,
		E = 0.05842,
		L = 0.14990,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 15,
		B = 16,
		E = 18,
		L = 16,
		A = 18,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 505,
	label = "Cs-CsCsHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.00000,
		B = 0.00000,
		E = 0.00000,
		L = 0.49258,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 2202,
		B = 2168,
		E = 2317,
		L = 2014,
		A = 2319,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 506,
	label = "Cs-CdsCsHH",
	group = 
"""
1 * Cs         u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO,CS] u0 {1,S}
3   Cs         u0 {1,S}
4   H          u0 {1,S}
5   H          u0 {1,S}
""",
	solute = u'Cs-(Cds-Cd)CsHH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 507,
	label = "Cs-(Cds-O2d)CsHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   O2d u0 {2,D}
""",
	solute = SoluteData(
		S = 0.08767,
		B = 0.07422,
		E = -0.00602,
		L = 0.30058,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 591,
		B = 587,
		E = 610,
		L = 537,
		A = 614,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 508,
	label = "Cs-(Cds-Cd)CsHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
	solute = u'Cs-(Cds-Cds)CsHH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 509,
	label = "Cs-(Cds-Cds)CsHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
	solute = SoluteData(
		S = 0.03558,
		B = 0.01742,
		E = 0.01675,
		L = 0.45596,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 421,
		B = 389,
		E = 446,
		L = 376,
		A = 446,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 510,
	label = "Cs-(Cds-Cdd)CsHH",
	group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   Cdd u0 {2,D}
""",
	solute = u'Cs-(Cds-Cdd-Cd)CsHH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 511,
	label = "Cs-(Cds-Cdd-Cd)CsHH",
	group = 
"""
1 * Cs  u0 {2,S} {4,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {7,D}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   H   u0 {1,S}
7   C   u0 {3,D}
""",
	solute = SoluteData(
		S = 0.02480,
		B = 0.01302,
		E = 0.05149,
		L = 0.46989,
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
	index = 512,
	label = "Cs-(Cd-N3d)CsHH",
	group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D} {7,S}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   N3d u0 {2,D}
7   R   u0 {2,S}
""",
	solute = SoluteData(
		S = 0.02925,
		B = 0.11261,
		E = -0.01126,
		L = 0.44492,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 49,
		B = 35,
		E = 58,
		L = 42,
		A = 57,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 513,
	label = "Cs-(Cds-S2d)CsHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CS u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   S2d u0 {2,D}
""",
	solute = u'Cs-(Cds-O2d)CsHH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 514,
	label = "Cs-CdsCdsHH",
	group = 
"""
1 * Cs         u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO,CS] u0 {1,S}
3   [Cd,CO,CS] u0 {1,S}
4   H          u0 {1,S}
5   H          u0 {1,S}
""",
	solute = u'Cs-(Cds-O2d)(Cds-Cd)HH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 515,
	label = "Cs-(Cds-O2d)(Cds-O2d)HH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   CO u0 {1,S} {7,D}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
""",
	solute = SoluteData(
		S = -0.13243,
		B = -0.08551,
		E = 0.05491,
		L = 0.14352,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 29,
		B = 29,
		E = 32,
		L = 28,
		A = 30,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 516,
	label = "Cs-(Cds-O2d)(Cds-Cd)HH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {3,D}
7   O2d u0 {2,D}
""",
	solute = u'Cs-(Cds-O2d)(Cds-Cds)HH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 517,
	label = "Cs-(Cds-O2d)(Cds-Cds)HH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {3,D}
7   O2d u0 {2,D}
""",
	solute = SoluteData(
		S = -0.00162,
		B = 0.00705,
		E = 0.01856,
		L = 0.21083,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 26,
		B = 26,
		E = 26,
		L = 25,
		A = 26,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 518,
	label = "Cs-(Cds-Cd)(Cds-Cd)HH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
""",
	solute = u'Cs-(Cds-Cds)(Cds-Cds)HH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 519,
	label = "Cs-(Cds-Cds)(Cds-Cds)HH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
""",
	solute = SoluteData(
		S = 0.03289,
		B = 0.04253,
		E = 0.06497,
		L = 0.49390,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 19,
		B = 19,
		E = 20,
		L = 16,
		A = 20,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 520,
	label = "Cs-CtCsHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Cs u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = u'Cs-(Ct-Ct)CsHH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 521,
	label = "Cs-(Ct-N3t)CsHH",
	group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S} {6,T}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   N3t u0 {2,T}
""",
	solute = SoluteData(
		S = 0.19063,
		B = 0.05558,
		E = -0.01313,
		L = 0.29211,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 28,
		B = 28,
		E = 27,
		L = 26,
		A = 28,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 522,
	label = "Cs-(Ct-Ct)CsHH",
	group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S} {6,T}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   Ct  u0 {2,T}
""",
	solute = SoluteData(
		S = -0.01485,
		B = -0.04339,
		E = -0.02705,
		L = -0.11775,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 49,
		B = 49,
		E = 52,
		L = 27,
		A = 49,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 523,
	label = "Cs-CtCdsHH",
	group = 
"""
1 * Cs         u0 {2,S} {3,S} {4,S} {5,S}
2   Ct         u0 {1,S}
3   [Cd,CO,CS] u0 {1,S}
4   H          u0 {1,S}
5   H          u0 {1,S}
""",
	solute = SoluteData(
		S = 0.04720,
		B = -0.00097,
		E = 0.00927,
		L = 0.06229,
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
	index = 524,
	label = "Cs-CtCtHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Ct u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = u'Cs-(Ct-N3t)(Ct-N3t)HH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 525,
	label = "Cs-(Ct-N3t)(Ct-N3t)HH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S} {6,T}
3   Ct u0 {1,S} {7,T}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   N3t u0 {2,T}
7   N3t u0 {3,T}
""",
	solute = SoluteData(
		S = 0.03748,
		B = 0.00701,
		E = -0.00951,
		L = 0.01205,
		A = 0.04000,
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
	index = 526,
	label = "Cs-CbCsHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cs u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = -0.00741,
		B = -0.03620,
		E = 0.01176,
		L = 0.10327,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 392,
		B = 372,
		E = 407,
		L = 348,
		A = 409,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 527,
	label = "Cs-CbCdsHH",
	group = 
"""
1 * Cs         u0 {2,S} {3,S} {4,S} {5,S}
2   Cb         u0 {1,S}
3   [Cd,CO,CS] u0 {1,S}
4   H          u0 {1,S}
5   H          u0 {1,S}
""",
	solute = u'Cs-(Cds-O2d)CbHH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 528,
	label = "Cs-(Cds-O2d)CbHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   O2d u0 {2,D}
""",
	solute = SoluteData(
		S = -0.09416,
		B = 0.04178,
		E = -0.03802,
		L = -0.07294,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 60,
		B = 60,
		E = 60,
		L = 48,
		A = 61,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 529,
	label = "Cs-(Cds-Cd)CbHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
	solute = u'Cs-(Cds-Cds)CbHH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 530,
	label = "Cs-(Cds-Cds)CbHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
	solute = SoluteData(
		S = -0.04585,
		B = 0.00289,
		E = 0.00802,
		L = 0.13872,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 15,
		B = 13,
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
	index = 531,
	label = "Cs-(Cds-N3d)CbHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   N3d u0 {2,D}
""",
	solute = SoluteData(
		S = 0.05755,
		B = -0.00094,
		E = -0.01700,
		L = 0.11419,
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
	index = 532,
	label = "Cs-CbCtHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Ct u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = -0.00531,
		B = 0.00702,
		E = -0.02654,
		L = -0.06262,
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
	index = 533,
	label = "Cs-CbCbHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.17743,
		B = -0.04295,
		E = 0.02634,
		L = 0.52945,
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
	index = 534,
	label = "Cs-CCCH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = u'Cs-CsCsCsH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 535,
	label = "Crs-CrCrCrH",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   C  u0 r1 {1,S}
3   C  u0 r1 {1,S}
4   C  u0 r1 {1,S}
5   H  u0 {1,S}
""",
	solute = u'Crs-CrsCrsCrsH',
	dataCount = None,
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 536,
	label = "Crs-CrsCrsCrsH",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 r1 {1,S}
3   Cs u0 r1 {1,S}
4   Cs u0 r1 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.12326,
		B = 0.00000,
		E = 0.10592,
		L = 0.51296,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 277,
		B = 279,
		E = 283,
		L = 244,
		A = 287,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 537,
	label = "Crs-CrdCrsCrsH",
	group = 
"""
1 * Cs         u0 r1 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO,CS] u0 r1 {1,S}
3   Cs         u0 r1 {1,S}
4   Cs         u0 r1 {1,S}
5   H          u0 {1,S}
""",
	solute = u'Crs-(Crd-Cd)CrsCrsH',
	dataCount = None,
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 538,
	label = "Crs-(Crd-Cd)CrsCrsH",
	group = 
"""
1 * Cs         u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cd         u0 r1 {1,S} {6,D}
3   Cs         u0 r1 {1,S}
4   Cs         u0 r1 {1,S}
5   H          u0 {1,S}
6   C          u0 {2,D}
""",
	solute = SoluteData(
		S = 0.03860,
		B = 0.05885,
		E = 0.12599,
		L = 0.46837,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 32,
		B = 32,
		E = 32,
		L = 31,
		A = 34,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 539,
	label = "Crs-(Crd-Crd)CrsCrsH",
	group = 
"""
1 * Cs         u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cd         u0 r1 {1,S} {6,D}
3   Cs         u0 r1 {1,S}
4   Cs         u0 r1 {1,S}
5   H          u0 {1,S}
6   C          u0 r1 {2,D}
""",
	solute = SoluteData(
		S = 0.07837,
		B = 0.10681,
		E = 0.11230,
		L = 0.46203,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 92,
		B = 89,
		E = 96,
		L = 85,
		A = 96,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 540,
	label = "Crs-(Crd-O2d)CrsCrsH",
	group = 
"""
1 * Cs         u0 r1 {2,S} {3,S} {4,S} {5,S}
2   CO         u0 r1 {1,S} {6,D}
3   Cs         u0 r1 {1,S}
4   Cs         u0 r1 {1,S}
5   H          u0 {1,S}
6   O2d        u0 {2,D}
""",
	solute = SoluteData(
		S = 0.11668,
		B = 0.02766,
		E = 0.04771,
		L = 0.24275,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 20,
		B = 21,
		E = 22,
		L = 17,
		A = 22,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 541,
	label = "Crs-CbCrsCrsH",
	group = 
"""
1 * Cs         u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cb         u0 r1 {1,S}
3   Cs         u0 r1 {1,S}
4   Cs         u0 r1 {1,S}
5   H          u0 {1,S}
""",
	solute = SoluteData(
		S = -0.00432,
		B = 0.10323,
		E = 0.00755,
		L = 0.53551,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 35,
		B = 35,
		E = 37,
		L = 35,
		A = 36,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 542,
	label = "Crs-CrdCrdCrsH",
	group = 
"""
1 * Cs         u0 r1 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO,CS] u0 r1 {1,S}
3   [Cd,CO,CS] u0 r1 {1,S}
4   Cs         u0 r1 {1,S}
5   H          u0 {1,S}
""",
	solute = SoluteData(
		S = -0.02159,
		B = -0.00820,
		E = 0.05286,
		L = 0.22751,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 4,
		E = 5,
		L = 5,
		A = 5,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 543,
	label = "Crs-CbCrdCrsH",
	group = 
"""
1 * Cs         u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cb         u0 r1 {1,S}
3   [Cd,CO,CS] u0 r1 {1,S}
4   Cs         u0 r1 {1,S}
5   H          u0 {1,S}
""",
	solute = SoluteData(
		S = 0.05479,
		B = -0.02349,
		E = 0.00616,
		L = 0.19062,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 4,
		B = 4,
		E = 4,
		L = 4,
		A = 4,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 544,
	label = "Crs-CbCrdCrdH",
	group = 
"""
1 * Cs         u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cb         u0 r1 {1,S}
3   [Cd,CO,CS] u0 r1 {1,S}
4   [Cd,CO,CS] u0 r1 {1,S}
5   H          u0 {1,S}
""",
	solute = SoluteData(
		S = -0.12161,
		B = 0.07275,
		E = -0.00011,
		L = 0.03151,
		A = 0.09793,
	),
	dataCount = DataCountGAV(
		S = 9,
		B = 9,
		E = 9,
		L = 9,
		A = 9,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 545,
	label = "Crs-CbCbCrsH",
	group = 
"""
1 * Cs         u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cb         u0 r1 {1,S}
3   Cb         u0 r1 {1,S}
4   Cs         u0 r1 {1,S}
5   H          u0 {1,S}
""",
	solute = SoluteData(
		S = -0.02089,
		B = -0.00129,
		E = -0.08184,
		L = 0.12228,
		A = -0.00464,
	),
	dataCount = DataCountGAV(
		S = 4,
		B = 4,
		E = 4,
		L = 4,
		A = 4,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 546,
	label = "Crs-CrCrCH",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   C  u0 r1 {1,S}
3   C  u0 r1 {1,S}
4   C  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = u'Crs-CrsCrsCsH',
	dataCount = None,
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 547,
	label = "Crs-CrsCrsCsH",
	group = 
"""
1 * Cs         u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cs         u0 r1 {1,S}
3   Cs         u0 r1 {1,S}
4   Cs         u0 {1,S}
5   H          u0 {1,S}
""",
	solute = SoluteData(
		S = 0.02889,
		B = 0.00000,
		E = 0.03737,
		L = 0.55376,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 226,
		B = 215,
		E = 235,
		L = 209,
		A = 227,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 548,
	label = "Crs-CrsCrsCdH",
	group = 
"""
1 * Cs         u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cs         u0 r1 {1,S}
3   Cs         u0 r1 {1,S}
4   [Cd,CO,CS] u0 {1,S}
5   H          u0 {1,S}
""",
	solute = SoluteData(
		S = 0.09954,
		B = 0.09593,
		E = 0.00762,
		L = 0.29495,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 81,
		B = 77,
		E = 81,
		L = 77,
		A = 82,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 549,
	label = "Crs-CrsCrsCtH",
	group = 
"""
1 * Cs         u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cs         u0 r1 {1,S}
3   Cs         u0 r1 {1,S}
4   Ct         u0 {1,S}
5   H          u0 {1,S}
""",
	solute = u'Crs-CrsCrs(Ct-Ct)H',
	dataCount = None,
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 550,
	label = "Crs-CrsCrs(Ct-N3t)H",
	group = 
"""
1 * Cs         u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cs         u0 r1 {1,S}
3   Cs         u0 r1 {1,S}
4   Ct         u0 {1,S} {6,T}
5   H          u0 {1,S}
6   N3t        u0 {4,T}
""",
	solute = u'Cs-(Ct-N3t)CsCsH',
	dataCount = None,
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 551,
	label = "Crs-CrsCrs(Ct-Ct)H",
	group = 
"""
1 * Cs         u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cs         u0 r1 {1,S}
3   Cs         u0 r1 {1,S}
4   Ct         u0 {1,S} {6,T}
5   H          u0 {1,S}
6   Ct         u0 {4,T}
""",
	solute = u'Cs-(Ct-Ct)CsCsH',
	dataCount = None,
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 552,
	label = "Crs-CrdCrsCsH",
	group = 
"""
1 * Cs         u0 r1 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO,CS] u0 r1 {1,S}
3   Cs         u0 r1 {1,S}
4   Cs         u0 {1,S}
5   H          u0 {1,S}
""",
	solute = SoluteData(
		S = -0.02918,
		B = 0.07227,
		E = 0.03340,
		L = 0.55472,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 46,
		B = 41,
		E = 48,
		L = 41,
		A = 47,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 553,
	label = "Crs-CrdCrsCdH",
	group = 
"""
1 * Cs         u0 r1 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO,CS] u0 r1 {1,S}
3   Cs         u0 r1 {1,S}
4   [Cd,CO,CS] u0 {1,S}
5   H          u0 {1,S}
""",
	solute = SoluteData(
		S = 0.04280,
		B = -0.01491,
		E = 0.02947,
		L = 0.07906,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 6,
		B = 6,
		E = 6,
		L = 5,
		A = 6,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 554,
	label = "Crs-CrdCrdCsH",
	group = 
"""
1 * Cs         u0 r1 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO,CS] u0 r1 {1,S}
3   [Cd,CO,CS] u0 r1 {1,S}
4   Cs         u0 {1,S}
5   H          u0 {1,S}
""",
	solute = SoluteData(
		S = 0.02322,
		B = 0.02008,
		E = 0.04747,
		L = 0.09280,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 5,
		E = 5,
		L = 1,
		A = 5,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 555,
	label = "Crs-CrdCrdCdH",
	group = 
"""
1 * Cs         u0 r1 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO,CS] u0 r1 {1,S}
3   [Cd,CO,CS] u0 r1 {1,S}
4   [Cd,CO,CS] u0 {1,S}
5   H          u0 {1,S}
""",
	solute = SoluteData(
		S = -0.21649,
		B = -0.06013,
		E = 0.00017,
		L = -0.43697,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 11,
		B = 11,
		E = 11,
		L = 11,
		A = 11,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 556,
	label = "Crs-CbCrsCsH",
	group = 
"""
1 * Cs         u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cb         u0 r1 {1,S}
3   Cs         u0 r1 {1,S}
4   Cs         u0 {1,S}
5   H          u0 {1,S}
""",
	solute = SoluteData(
		S = 0.01107,
		B = -0.01279,
		E = 0.01278,
		L = 0.23578,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 8,
		B = 7,
		E = 8,
		L = 8,
		A = 8,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 557,
	label = "Crs-CbCbCsH",
	group = 
"""
1 * Cs         u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cb         u0 r1 {1,S}
3   Cb         u0 r1 {1,S}
4   Cs         u0 {1,S}
5   H          u0 {1,S}
""",
	solute = SoluteData(
		S = 0.03259,
		B = -0.03075,
		E = -0.00979,
		L = 0.07824,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
		E = 6,
		L = 6,
		A = 6,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 558,
	label = "Cs-CsCsCsH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.00000,
		B = 0.00000,
		E = 0.00000,
		L = 0.40981,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 409,
		B = 399,
		E = 420,
		L = 385,
		A = 432,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 559,
	label = "Cs-CdsCsCsH",
	group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   Cs      u0 {1,S}
4   Cs      u0 {1,S}
5   H       u0 {1,S}
""",
	solute = u'Cs-(Cds-Cd)CsCsH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 560,
	label = "Cs-(Cds-O2d)CsCsH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
6   O2d u0 {2,D}
""",
	solute = SoluteData(
		S = 0.05454,
		B = 0.07812,
		E = -0.00341,
		L = 0.22936,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 96,
		B = 95,
		E = 97,
		L = 89,
		A = 98,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 561,
	label = "Cs-(Cds-Cd)CsCsH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
	solute = u'Cs-(Cds-Cds)CsCsH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 562,
	label = "Cs-(Cds-Cds)CsCsH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
	solute = SoluteData(
		S = 0.01356,
		B = 0.02637,
		E = 0.01047,
		L = 0.40066,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 35,
		B = 31,
		E = 36,
		L = 33,
		A = 36,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 563,
	label = "Cs-(CdN3d)CsCsH",
	group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D} {7,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   N3d u0 {2,D}
7   R   u0 {2,S}
""",
	solute = SoluteData(
		S = 0.08975,
		B = 0.09000,
		E = 0.02314,
		L = 0.57919,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 4,
		E = 5,
		L = 5,
		A = 6,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 564,
	label = "Cs-CtCsCsH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
""",
	solute = u'Cs-(Ct-N3t)CsCsH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 565,
	label = "Cs-(Ct-N3t)CsCsH",
	group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S} {6,T}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   N3t u0 {2,T}
""",
	solute = SoluteData(
		S = 0.09873,
		B = 0.03342,
		E = -0.01514,
		L = 0.24266,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 4,
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
	index = 566,
	label = "Cs-(Ct-Ct)CsCsH",
	group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S} {6,T}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   Ct  u0 {2,T}
""",
	solute = SoluteData(
		S = -0.04622,
		B = -0.03485,
		E = -0.02959,
		L = 0.10041,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 4,
		B = 6,
		E = 5,
		L = 2,
		A = 6,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 567,
	label = "Cs-CbCsCsH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = -0.00189,
		B = -0.02530,
		E = 0.01285,
		L = 0.03492,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 93,
		B = 84,
		E = 99,
		L = 80,
		A = 95,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 568,
	label = "Cs-CdsCdsCsH",
	group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
5   H       u0 {1,S}
""",
	solute = SoluteData(
		S = -0.01719,
		B = -0.03372,
		E = -0.00478,
		L = 0.14775,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 6,
		B = 6,
		E = 10,
		L = 6,
		A = 7,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 569,
	label = "Cs-CbCdsCsH",
	group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
5   H       u0 {1,S}
""",
	solute = u'Cs-(Cds-O2d)CbCsH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 570,
	label = "Cs-(Cds-O2d)CbCsH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
6   O2d u0 {2,D}
""",
	solute = SoluteData(
		S = 0.04058,
		B = 0.03020,
		E = -0.02145,
		L = 0.14258,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 28,
		B = 28,
		E = 28,
		L = 26,
		A = 28,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 571,
	label = "Cs-(Cds-Cd)CbCsH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
	solute = u'Cs-(Cds-Cds)CbCsH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 572,
	label = "Cs-(Cds-Cds)CbCsH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
	solute = SoluteData(
		S = -0.00314,
		B = 0.00286,
		E = 0.01699,
		L = 0.32322,
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
	index = 573,
	label = "Cs-CbCbCsH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.09615,
		B = 0.00664,
		E = 0.00891,
		L = 0.31177,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 13,
		B = 13,
		E = 14,
		L = 13,
		A = 13,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 574,
	label = "Cs-CbCdsCdsH",
	group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   H       u0 {1,S}
""",
	solute = SoluteData(
		S = 0.00657,
		B = -0.08838,
		E = 0.09805,
		L = 0.33279,
		A = -0.00081,
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
	index = 575,
	label = "Cs-CbCbCdsH",
	group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   Cb      u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   H       u0 {1,S}
""",
	solute = u'Cs-CbCb(Cds-O2d)H',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 576,
	label = "Cs-CbCb(Cds-O2d)H",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   H  u0 {1,S}
6   O2d u0 {2,D}
""",
	solute = SoluteData(
		S = -0.05200,
		B = 0.06384,
		E = -0.02226,
		L = -0.07640,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 1,
		B = 1,
		E = 2,
		L = 1,
		A = 1,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 577,
	label = "Cs-CbCbCbH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = -0.01432,
		B = -0.00751,
		E = 0.00442,
		L = -0.46157,
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
	index = 578,
	label = "Cs-CCCC",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
5   C  u0 {1,S}
""",
	solute = u'Cs-CsCsCsCs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 579,
	label = "Crs-CrCrCrCr",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   C  u0 r1 {1,S}
3   C  u0 r1 {1,S}
4   C  u0 r1 {1,S}
5   C  u0 r1 {1,S}
""",
	solute = u'Crs-CbCrsCrsCrs',
	dataCount = None,
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 580,
	label = "Crs-CrsCrsCrsCrs",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 r1 {1,S}
3   Cs u0 r1 {1,S}
4   Cs u0 r1 {1,S}
5   Cs u0 r1 {1,S}
""",
	solute = SoluteData(
		S = 0.02699,
		B = -0.01232,
		E = 0.19857,
		L = 0.28691,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 14,
		B = 14,
		E = 14,
		L = 14,
		A = 15,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 581,
	label = "Crs-CbCrsCrsCrs",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 r1 {1,S}
3   Cs u0 r1 {1,S}
4   Cs u0 r1 {1,S}
5   Cs u0 r1 {1,S}
""",
	solute = SoluteData(
		S = 0.03756,
		B = 0.06899,
		E = 0.13755,
		L = 0.24554,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 20,
		B = 20,
		E = 20,
		L = 19,
		A = 20,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 582,
	label = "Crs-CrdCrsCrsCrs",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO,CS] u0 r1 {1,S}
3   Cs u0 r1 {1,S}
4   Cs u0 r1 {1,S}
5   Cs u0 r1 {1,S}
""",
	solute = SoluteData(
		S = -0.04708,
		B = 0.01104,
		E = 0.04619,
		L = 0.17574,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 5,
		E = 5,
		L = 4,
		A = 5,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 583,
	label = "Crs-CbCrdCrsCrs",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 r1 {1,S}
3   [Cd,CO,CS] u0 r1 {1,S}
4   Cs u0 r1 {1,S}
5   Cs u0 r1 {1,S}
""",
	solute = SoluteData(
		S = 0.30776,
		B = -0.01410,
		E = -0.01172,
		L = 0.67499,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
		E = 2,
		L = 2,
		A = 2,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 584,
	label = "Crs-CrCrCrC",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   C  u0 r1 {1,S}
3   C  u0 r1 {1,S}
4   C  u0 r1 {1,S}
5   C  u0 {1,S}
""",
	solute = u'Crs-CrsCrsCrsCs',
	dataCount = None,
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 585,
	label = "Crs-CrsCrsCrsCs",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 r1 {1,S}
3   Cs u0 r1 {1,S}
4   Cs u0 r1 {1,S}
5   Cs u0 {1,S}
""",
	solute = SoluteData(
		S = 0.16315,
		B = 0.00000,
		E = 0.07252,
		L = 0.75695,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 165,
		B = 165,
		E = 166,
		L = 135,
		A = 168,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 586,
	label = "Crs-CbCrsCrsCs",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 r1 {1,S}
3   Cs u0 r1 {1,S}
4   Cs u0 r1 {1,S}
5   Cs u0 {1,S}
""",
	solute = SoluteData(
		S = -0.02584,
		B = 0.04822,
		E = -0.00520,
		L = 0.27127,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 7,
		B = 7,
		E = 7,
		L = 7,
		A = 7,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 587,
	label = "Crs-CbCrsCrsCd",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 r1 {1,S}
3   Cs u0 r1 {1,S}
4   Cs u0 r1 {1,S}
5   [Cd,CO,CS] u0 {1,S}
""",
	solute = SoluteData(
		S = -0.11161,
		B = 0.07181,
		E = 0.00343,
		L = -0.01939,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 3,
		L = 3,
		A = 3,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 588,
	label = "Crs-CbCrdCrsCd",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 r1 {1,S}
3   [Cd,CO,CS] u0 r1 {1,S}
4   Cs u0 r1 {1,S}
5   [Cd,CO,CS] u0 {1,S}
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
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 589,
	label = "Crs-CbCbCrsCs",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 r1 {1,S}
3   Cb u0 r1 {1,S}
4   Cs u0 r1 {1,S}
5   Cs u0 {1,S}
""",
	solute = SoluteData(
		S = 0.02627,
		B = -0.00734,
		E = 0.09727,
		L = 0.24891,
		A = -0.00496,
	),
	dataCount = DataCountGAV(
		S = 1,
		B = 1,
		E = 1,
		L = 1,
		A = 1,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 590,
	label = "Crs-CrsCrsCrsCd",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 r1 {1,S}
3   Cs u0 r1 {1,S}
4   Cs u0 r1 {1,S}
5   [Cd,CO,CS] u0 {1,S}
""",
	solute = u'Crs-CrsCrsCrs(Cd-O2d)',
	dataCount = None,
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 591,
	label = "Crs-CrsCrsCrs(Cd-O2d)",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 r1 {1,S}
3   Cs u0 r1 {1,S}
4   Cs u0 r1 {1,S}
5   CO u0 {1,S}
""",
	solute = SoluteData(
		S = 0.09607,
		B = 0.12605,
		E = -0.00837,
		L = 0.35399,
		A = -0.11074,
	),
	dataCount = DataCountGAV(
		S = 6,
		B = 6,
		E = 6,
		L = 6,
		A = 6,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 592,
	label = "Crs-CrdCrsCrsCs",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO,CS] u0 r1 {1,S}
3   Cs u0 r1 {1,S}
4   Cs u0 r1 {1,S}
5   Cs u0 {1,S}
""",
	solute = u'Crs-(Crd-O2d)CrsCrsCs',
	dataCount = None,
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 593,
	label = "Crs-(Crd-O2d)CrsCrsCs",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   CO u0 r1 {1,S}
3   Cs u0 r1 {1,S}
4   Cs u0 r1 {1,S}
5   Cs u0 {1,S}
""",
	solute = SoluteData(
		S = 0.14531,
		B = 0.08905,
		E = 0.06193,
		L = 0.11160,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 9,
		B = 9,
		E = 9,
		L = 5,
		A = 9,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 594,
	label = "Crs-(Crd-Cd)CrsCrsCs",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 r1 {1,S} {6,D}
3   Cs u0 r1 {1,S}
4   Cs u0 r1 {1,S}
5   Cs u0 {1,S}
6   C u0 {2,D}
""",
	solute = u'Crs-(Crd-Crd)CrsCrsCs',
	dataCount = None,
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 595,
	label = "Crs-(Crd-Crd)CrsCrsCs",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 r1 {1,S} {6,D}
3   Cs u0 r1 {1,S}
4   Cs u0 r1 {1,S}
5   Cs u0 {1,S}
6   C u0 r1 {2,D}
""",
	solute = SoluteData(
		S = 0.08072,
		B = 0.12947,
		E = 0.07131,
		L = 0.35719,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 84,
		B = 84,
		E = 85,
		L = 68,
		A = 86,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 596,
	label = "Crs-CrdCrdCrsCs",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO,CS] u0 r1 {1,S}
3   [Cd,CO,CS] u0 r1 {1,S}
4   Cs u0 r1 {1,S}
5   Cs u0 {1,S}
""",
	solute = SoluteData(
		S = 0.06956,
		B = 0.10121,
		E = 0.04074,
		L = 0.27232,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 22,
		B = 22,
		E = 22,
		L = 12,
		A = 22,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 597,
	label = "Crs-CrdCrdCbCs",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO,CS] u0 r1 {1,S}
3   [Cd,CO,CS] u0 r1 {1,S}
4   Cb u0 r1 {1,S}
5   Cs u0 {1,S}
""",
	solute = SoluteData(
		S = 0.01873,
		B = -0.04416,
		E = -0.02351,
		L = 0.03967,
		A = 0.09159,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
		E = 2,
		L = 1,
		A = 2,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 598,
	label = "Crs-CrdCrdCrdCs",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO,CS] u0 r1 {1,S}
3   [Cd,CO,CS] u0 r1 {1,S}
4   [Cd,CO,CS] u0 r1 {1,S}
5   Cs u0 {1,S}
""",
	solute = SoluteData(
		S = -0.04025,
		B = 0.05351,
		E = -0.00463,
		L = 0.08487,
		A = -0.00656,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 3,
		L = 1,
		A = 3,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 599,
	label = "Crs-CrCrCC",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   C  u0 r1 {1,S}
3   C  u0 r1 {1,S}
4   C  u0 {1,S}
5   C  u0 {1,S}
""",
	solute = u'Crs-CrsCrsCsCs',
	dataCount = None,
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 600,
	label = "Crs-CrsCrsCsCs",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 r1 {1,S}
3   Cs u0 r1 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
""",
	solute = SoluteData(
		S = -0.08160,
		B = 0.00000,
		E = -0.00335,
		L = 0.32778,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 81,
		B = 81,
		E = 84,
		L = 79,
		A = 84,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 601,
	label = "Crs-CbCrsCsCs",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 r1 {1,S}
3   Cs u0 r1 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
""",
	solute = SoluteData(
		S = 0.04577,
		B = 0.00936,
		E = 0.05732,
		L = 0.30959,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
		E = 3,
		L = 2,
		A = 3,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 602,
	label = "Crs-CrdCrsCsCs",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO,CS] u0 r1 {1,S}
3   Cs u0 r1 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
""",
	solute = SoluteData(
		S = 0.09783,
		B = 0.02688,
		E = 0.02528,
		L = 0.42410,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 14,
		B = 13,
		E = 14,
		L = 14,
		A = 14,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 603,
	label = "Crs-CrdCrdCsCs",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO,CS] u0 r1 {1,S}
3   [Cd,CO,CS] u0 r1 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
""",
	solute = u'Crs-(Crd-O2d)(Crd-O2d)CsCs',
	dataCount = None,
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 604,
	label = "Crs-(Crd-O2d)(Crd-O2d)CsCs",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   CO u0 r1 {1,S}
3   CO u0 r1 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
""",
	solute = SoluteData(
		S = -0.01938,
		B = 0.09211,
		E = -0.00349,
		L = 0.16422,
		A = 0.02342,
	),
	dataCount = DataCountGAV(
		S = 46,
		B = 46,
		E = 47,
		L = 13,
		A = 46,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 605,
	label = "Crs-CrdCrdCdCs",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO,CS] u0 r1 {1,S}
3   [Cd,CO,CS] u0 r1 {1,S}
4   [Cd,CO,CS] u0 {1,S}
5   Cs u0 {1,S}
""",
	solute = u'Crs-(Crd-O2d)(Crd-O2d)CdCs',
	dataCount = None,
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 606,
	label = "Crs-(Crd-O2d)(Crd-O2d)CdCs",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   CO u0 r1 {1,S}
3   CO u0 r1 {1,S}
4   [Cd,CO,CS] u0 {1,S}
5   Cs u0 {1,S}
""",
	solute = u'Crs-(Crd-O2d)(Crd-O2d)CsCs',
	dataCount = None,
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 607,
	label = "Crs-CrsCrsCdCs",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 r1 {1,S}
3   Cs u0 r1 {1,S}
4   [Cd,CO,CS] u0 {1,S}
5   Cs u0 {1,S}
""",
	solute = SoluteData(
		S = -0.10701,
		B = 0.10766,
		E = 0.00385,
		L = 0.03898,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 9,
		B = 9,
		E = 9,
		L = 7,
		A = 9,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 608,
	label = "Cs-CsCsCsCs",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
""",
	solute = SoluteData(
		S = 0.00000,
		B = 0.00000,
		E = 0.00000,
		L = 0.38226,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 80,
		B = 80,
		E = 78,
		L = 69,
		A = 80,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 609,
	label = "Cs-CdsCsCsCs",
	group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   Cs      u0 {1,S}
4   Cs      u0 {1,S}
5   Cs      u0 {1,S}
""",
	solute = u'Cs-(Cds-Cd)CsCsCs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 610,
	label = "Cs-(Cds-O2d)CsCsCs",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
6   O2d u0 {2,D}
""",
	solute = SoluteData(
		S = 0.04973,
		B = 0.12163,
		E = 0.00915,
		L = 0.32713,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 18,
		B = 18,
		E = 19,
		L = 19,
		A = 20,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 611,
	label = "Cs-(Cds-Cd)CsCsCs",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
6   C  u0 {2,D}
""",
	solute = u'Cs-(Cds-Cds)CsCsCs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 612,
	label = "Cs-(Cds-Cds)CsCsCs",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
6   Cd u0 {2,D}
""",
	solute = SoluteData(
		S = 0.04109,
		B = 0.03573,
		E = -0.02479,
		L = 0.40494,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 9,
		B = 9,
		E = 11,
		L = 9,
		A = 13,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 613,
	label = "Cs-CtCsCsCs",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
""",
	solute = SoluteData(
		S = 0.02249,
		B = 0.02547,
		E = 0.03254,
		L = 0.18485,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 2,
		L = 2,
		A = 3,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 614,
	label = "Cs-CbCsCsCs",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
""",
	solute = SoluteData(
		S = 0.04410,
		B = 0.01241,
		E = 0.01341,
		L = 0.25132,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 61,
		B = 60,
		E = 70,
		L = 60,
		A = 67,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 615,
	label = "Cs-CdsCdsCsCs",
	group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
5   Cs      u0 {1,S}
""",
	solute = SoluteData(
		S = 0.04578,
		B = -0.03230,
		E = -0.03788,
		L = 0.07553,
		A = -0.07754,
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
	index = 616,
	label = "Cs-CbCtCsCs",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
""",
	solute = SoluteData(
		S = 0.01011,
		B = 0.12546,
		E = -0.02589,
		L = 0.18917,
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
	index = 617,
	label = "Cs-CbCbCsCs",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
""",
	solute = SoluteData(
		S = -0.00378,
		B = 0.05379,
		E = -0.00364,
		L = 0.21433,
		A = 0.00860,
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
	index = 618,
	label = "Cs-CbCdsCdsCs",
	group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   Cs      u0 {1,S}
""",
	solute = u'Cs-(Cds-O2d)(Cds-Cd)CbCs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 619,
	label = "Cs-(Cds-O2d)(Cds-Cd)CbCs",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Cb u0 {1,S}
5   Cs u0 {1,S}
6   C  u0 {3,D}
7   O2d u0 {2,D}
""",
	solute = u'Cs-(Cds-O2d)(Cds-Cds)CbCs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 620,
	label = "Cs-(Cds-O2d)(Cds-Cds)CbCs",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Cb u0 {1,S}
5   Cs u0 {1,S}
6   Cd u0 {3,D}
7   O2d u0 {2,D}
""",
	solute = u'Cs-(Cds-O2d)(Crds-Crds)CbCs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 621,
	label = "Cs-(Cds-O2d)(Crds-Crds)CbCs",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   Cd u0 r1 {1,S} {6,D}
4   Cb u0 {1,S}
5   Cs u0 {1,S}
6   Cd u0 r1 {3,D}
7   O2d u0 {2,D}
""",
	solute = u'Cs-(Cds-O2d)CbCbCs',
	dataCount = None,
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 622,
	label = "Cs-CbCbCdsCs",
	group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   Cb      u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   Cs      u0 {1,S}
""",
	solute = u'Cs-(Cds-O2d)CbCbCs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 623,
	label = "Cs-(Cds-O2d)CbCbCs",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   Cs u0 {1,S}
6   O2d u0 {2,D}
""",
	solute = SoluteData(
		S = -0.01303,
		B = 0.09437,
		E = -0.02483,
		L = 0.25873,
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
	index = 624,
	label = "Cs-CbCbCbCb",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   Cb u0 {1,S}
""",
	solute = SoluteData(
		S = -0.08035,
		B = -0.02584,
		E = -0.01078,
		L = -0.55987,
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
	index = 625,
	label = "Cs-CCCOs",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
5   O2s u0 {1,S}
""",
	solute = u'Cs-CsCsCsOs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 626,
	label = "Cs-CsCsCsOs",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   O2s u0 {1,S}
""",
	solute = u'Cs-CsCsCs(Os-R)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 627,
	label = "Cs-CsCsCs(Os-H)",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   O2s u0 {1,S} {6,S}
6   H  u0 {5,S}
""",
	solute = SoluteData(
		S = 0.02326,
		B = 0.21460,
		E = -0.03469,
		L = 0.14805,
		A = 0.03541,
	),
	dataCount = DataCountGAV(
		S = 31,
		B = 30,
		E = 31,
		L = 27,
		A = 31,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 628,
	label = "Crs-CrsCrsCrs(Os-H)",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 r1 {1,S}
3   Cs u0 r1 {1,S}
4   Cs u0 r1 {1,S}
5   O2s u0 {1,S} {6,S}
6   H  u0 {5,S}
""",
	solute = SoluteData(
		S = 0.20452,
		B = 0.05943,
		E = 0.14762,
		L = 0.21668,
		A = -0.06699,
	),
	dataCount = DataCountGAV(
		S = 14,
		B = 14,
		E = 15,
		L = 12,
		A = 14,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 629,
	label = "Crs-CrsCrsCs(Os-H)",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 r1 {1,S}
3   Cs u0 r1 {1,S}
4   Cs u0 {1,S}
5   O2s u0 {1,S} {6,S}
6   H  u0 {5,S}
""",
	solute = SoluteData(
		S = 0.05891,
		B = 0.13191,
		E = 0.02670,
		L = 0.53451,
		A = 0.05930,
	),
	dataCount = DataCountGAV(
		S = 19,
		B = 19,
		E = 20,
		L = 16,
		A = 19,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 630,
	label = "Cs-CsCsCs(Os-R)",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   O2s u0 {1,S} {6,S}
6   R!H u0 {5,S}
""",
	solute = SoluteData(
		S = 0.00873,
		B = 0.09966,
		E = 0.00000,
		L = 0.16083,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 30,
		B = 30,
		E = 37,
		L = 26,
		A = 39,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 631,
	label = "Crs-CrsCrsCrs(Ors-R)",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 r1 {1,S}
3   Cs u0 r1 {1,S}
4   Cs u0 r1 {1,S}
5   O2s u0 r1 {1,S} {6,S}
6   R!H u0 {5,S}
""",
	solute = SoluteData(
		S = 0.11248,
		B = 0.08850,
		E = 0.13885,
		L = 0.21807,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 10,
		B = 10,
		E = 11,
		L = 8,
		A = 10,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 632,
	label = "Crs-CrsCrsCs(Ors-R)",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 r1 {1,S}
3   Cs u0 r1 {1,S}
4   Cs u0 {1,S}
5   O2s u0 r1 {1,S} {6,S}
6   R!H u0 {5,S}
""",
	solute = SoluteData(
		S = 0.01116,
		B = 0.08272,
		E = 0.08100,
		L = 0.22238,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 3,
		L = 2,
		A = 3,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 633,
	label = "Crs-CrsCrsCs(Os-R)",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 r1 {1,S}
3   Cs u0 r1 {1,S}
4   Cs u0 {1,S}
5   O2s u0 {1,S} {6,S}
6   R!H u0 {5,S}
""",
	solute = SoluteData(
		S = 0.04282,
		B = 0.08296,
		E = 0.02043,
		L = -2.45597,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 6,
		B = 6,
		E = 6,
		L = 5,
		A = 6,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 634,
	label = "Crs-CrsCsCs(Ors-R)",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 r1 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   O2s u0 r1 {1,S} {6,S}
6   R!H u0 {5,S}
""",
	solute = SoluteData(
		S = 0.08079,
		B = 0.07647,
		E = 0.02620,
		L = -0.25668,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 14,
		B = 14,
		E = 14,
		L = 13,
		A = 14,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 635,
	label = "Cs-CdsCsCsOs",
	group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   Cs      u0 {1,S}
4   Cs      u0 {1,S}
5   O2s      u0 {1,S}
""",
	solute = u'Cs-CdsCsCs(Os-R)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 636,
	label = "Cs-CdsCsCs(Os-H)",
	group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   Cs      u0 {1,S}
4   Cs      u0 {1,S}
5   O2s     u0 {1,S} {6,S}
6   H       u0 {5,S}
""",
	solute = u'Cs-(Cds-O2d)CsCs(Os-H)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 637,
	label = "Cs-(Cds-O2d)CsCs(Os-H)",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   O2s u0 {1,S} {7,S}
6   O2d u0 {2,D}
7   H  u0 {5,S}
""",
	solute = SoluteData(
		S = 0.06470,
		B = -0.09491,
		E = -0.02128,
		L = 0.14711,
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
	index = 638,
	label = "Crs-(Cds-O2d)CrsCrs(Os-H)",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   Cs u0 r1 {1,S}
4   Cs u0 r1 {1,S}
5   O2s u0 {1,S} {7,S}
6   O2d u0 {2,D}
7   H  u0 {5,S}
""",
	solute = SoluteData(
		S = -0.06496,
		B = -0.06032,
		E = -0.05199,
		L = -0.16933,
		A = -0.04858,
	),
	dataCount = DataCountGAV(
		S = 45,
		B = 45,
		E = 46,
		L = 35,
		A = 45,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 639,
	label = "Cs-(Cds-Cd)CsCs(Os-H)",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   O2s u0 {1,S} {7,S}
6   C  u0 {2,D}
7   H  u0 {5,S}
""",
	solute = SoluteData(
		S = 0.07313,
		B = 0.04923,
		E = -0.02442,
		L = -0.04615,
		A = 0.01282,
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
	index = 640,
	label = "Cs-CdsCsCs(Os-R)",
	group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   Cs      u0 {1,S}
4   Cs      u0 {1,S}
5   O2s     u0 {1,S} {6,S}
6   R!H     u0 {5,S}
""",
	solute = u'Cs-(Cds-Cd)CsCs(Os-R)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 641,
	label = "Cs-(Cds-O2d)CsCs(Os-R)",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   O2s u0 {1,S} {7,S}
6   O2d u0 {2,D}
7   R!H  u0 {5,S}
""",
	solute = SoluteData(
		S = -0.01248,
		B = 0.12481,
		E = 0.02917,
		L = 0.41046,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 17,
		B = 17,
		E = 17,
		L = 9,
		A = 17,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 642,
	label = "Cs-(Cds-Cd)CsCs(Os-R)",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   O2s u0 {1,S} {7,S}
6   C  u0 {2,D}
7   R!H  u0 {5,S}
""",
	solute = SoluteData(
		S = 0.02338,
		B = 0.06858,
		E = -0.01962,
		L = 0.26749,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 7,
		B = 7,
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
	index = 643,
	label = "Cs-OsCtCsCs",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 {1,S}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
""",
	solute = SoluteData(
		S = 0.14808,
		B = 0.06781,
		E = 0.03621,
		L = 0.52765,
		A = 0.07466,
	),
	dataCount = DataCountGAV(
		S = 13,
		B = 13,
		E = 15,
		L = 11,
		A = 13,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 644,
	label = "Cs-CbCsCsOs",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   O2s u0 {1,S}
""",
	solute = SoluteData(
		S = -0.12786,
		B = 0.08883,
		E = 0.03865,
		L = -0.09199,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 20,
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
	index = 645,
	label = "Cs-CdsCdsCsOs",
	group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
5   O2s      u0 {1,S}
""",
	solute = u'Cs-(Cds-O2d)(Cds-Cd)CsOs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 646,
	label = "Cs-(Cds-O2d)(Cds-Cd)CsOs",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Cs u0 {1,S}
5   O2s u0 {1,S}
6   C  u0 {3,D}
7   O2d u0 {2,D}
""",
	solute = u'Cs-(Cds-O2d)(Cds-Cds)CsOs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 647,
	label = "Cs-(Cds-O2d)(Cds-Cds)CsOs",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {7,D}
3   Cd u0 {1,S} {6,D}
4   Cs u0 {1,S}
5   O2s u0 {1,S}
6   Cd u0 {3,D}
7   O2d u0 {2,D}
""",
	solute = SoluteData(
		S = -0.11603,
		B = -0.00499,
		E = -0.00195,
		L = 0.03671,
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
	index = 648,
	label = "Cs-CtCdsCsOs",
	group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Ct      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
5   O2s      u0 {1,S}
""",
	solute = u'Cs-(Cds-Cd)CtCsOs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 649,
	label = "Cs-(Cds-Cd)CtCsOs",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
5   O2s u0 {1,S}
6   C  u0 {2,D}
""",
	solute = u'Cs-(Cds-Cds)CtCsOs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 650,
	label = "Cs-(Cds-Cds)CtCsOs",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
5   O2s u0 {1,S}
6   Cd u0 {2,D}
""",
	solute = SoluteData(
		S = 0.08360,
		B = -0.02115,
		E = 0.03874,
		L = 0.24741,
		A = 0.03067,
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
	index = 651,
	label = "Cs-CbCdsCsOs",
	group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
5   O2s      u0 {1,S}
""",
	solute = SoluteData(
		S = -0.01618,
		B = 0.00349,
		E = 0.08979,
		L = 0.13263,
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
	index = 652,
	label = "Cs-CbCbCsOs",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
5   O2s u0 {1,S}
""",
	solute = SoluteData(
		S = -0.09011,
		B = 0.15785,
		E = 0.01180,
		L = 0.19184,
		A = 0.00278,
	),
	dataCount = DataCountGAV(
		S = 4,
		B = 4,
		E = 5,
		L = 4,
		A = 4,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 653,
	label = "Cs-CbCbCdsOs",
	group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   Cb      u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   O2s      u0 {1,S}
""",
	solute = u'Cs-(Cds-O2d)CbCbOs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 654,
	label = "Cs-(Cds-O2d)CbCbOs",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   O2s u0 {1,S}
6   O2d u0 {2,D}
""",
	solute = SoluteData(
		S = -0.03810,
		B = -0.04808,
		E = -0.01699,
		L = -0.03847,
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
	index = 655,
	label = "Cs-CbCbCbOs",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   O2s u0 {1,S}
""",
	solute = SoluteData(
		S = 0.12927,
		B = 0.01084,
		E = -0.02009,
		L = 0.21807,
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
	index = 656,
	label = "Cs-CCOsOs",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
""",
	solute = u'Cs-CsCsOsOs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 657,
	label = "Crs-CCOsOs",
	group = 
"""
1 * Cs  u0 r1 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 {1,S}
3   O2s u0 {1,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
""",
	solute = u'Crs-OrsOrsCC',
	dataCount = None,
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 658,
	label = "Crs-OrsOrsCC",
	group = 
"""
1 * Cs  u0 r1 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 r1 {1,S}
3   O2s u0 r1 {1,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.05514,
		B = 0.09381,
		E = 0.13941,
		L = 0.19930,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 24,
		B = 24,
		E = 24,
		L = 17,
		A = 24,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 659,
	label = "Crs-CrOrsOsC",
	group = 
"""
1 * Cs  u0 r1 {2,S} {3,S} {4,S} {5,S}
2   C   u0 r1 {1,S}
3   O2s u0 r1 {1,S}
4   O2s u0 {1,S}
5   C   u0 {1,S}
""",
	solute = SoluteData(
		S = -0.10670,
		B = -0.19367,
		E = 0.06361,
		L = -0.06337,
		A = 0.21730,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 4,
		L = 3,
		A = 3,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 660,
	label = "Cs-CsCsOsOs",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
""",
	solute = SoluteData(
		S = 0.00185,
		B = 0.04791,
		E = -0.03075,
		L = 0.14849,
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
	index = 661,
	label = "Cs-COsOsH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   H  u0 {1,S}
""",
	solute = u'Cs-CsOsOsH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 662,
	label = "Crs-COsOsH",
	group = 
"""
1 * Cs  u0 r1 {2,S} {3,S} {4,S} {5,S}
2   C   u0 {1,S}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
""",
	solute = u'Crs-CrOrsOsH',
	dataCount = None,
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 663,
	label = "Crs-OrsOrsCH",
	group = 
"""
1 * Cs  u0 r1 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 r1 {1,S}
3   O2s u0 r1 {1,S}
4   C   u0 {1,S}
5   H   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.11251,
		B = -0.00061,
		E = 0.08195,
		L = 0.13344,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 14,
		B = 14,
		E = 15,
		L = 14,
		A = 17,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 664,
	label = "Crs-CrOrsOsH",
	group = 
"""
1 * Cs  u0 r1 {2,S} {3,S} {4,S} {5,S}
2   C   u0 r1 {1,S}
3   O2s u0 r1 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.05199,
		B = -0.11038,
		E = 0.03597,
		L = -0.03215,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 41,
		B = 41,
		E = 43,
		L = 38,
		A = 42,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 665,
	label = "Cs-CsOsOsH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.04896,
		B = 0.08880,
		E = -0.01032,
		L = 0.22679,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 14,
		B = 9,
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
	index = 666,
	label = "Cs-COsSH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   O2s u0 {1,S}
4   S  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = u'Cs-CsOsSH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 667,
	label = "Cs-CsOsSH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   O2s u0 {1,S}
4   S  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = u'Cs-CsOsS2H',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 668,
	label = "Cs-CsOsS2H",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   O2s u0 {1,S}
4   S2s  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = -0.04584,
		B = -0.08341,
		E = 0.04626,
		L = 0.04549,
		A = 0.01124,
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
	index = 669,
	label = "Cs-CCOsH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   O2s u0 {1,S}
5   H  u0 {1,S}
""",
	solute = u'Cs-CsCsOsH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 670,
	label = "Cs-CsCsOsH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   O2s u0 {1,S}
5   H  u0 {1,S}
""",
	solute = u'Cs-CsCs(Os-H)H',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 671,
	label = "Cs-CsCs(Os-H)H",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   O2s u0 {1,S} {6,S}
5   H  u0 {1,S}
6   H  u0 {4,S}
""",
	solute = SoluteData(
		S = 0.02639,
		B = 0.04048,
		E = 0.00331,
		L = 0.27872,
		A = -0.03207,
	),
	dataCount = DataCountGAV(
		S = 140,
		B = 138,
		E = 141,
		L = 129,
		A = 141,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 672,
	label = "Crs-CrsCrs(Os-H)H",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 r1 {1,S}
3   Cs u0 r1 {1,S}
4   O2s u0 {1,S} {6,S}
5   H  u0 {1,S}
6   H  u0 {4,S}
""",
	solute = SoluteData(
		S = -0.06134,
		B = 0.01098,
		E = 0.05978,
		L = 0.35925,
		A = -0.01867,
	),
	dataCount = DataCountGAV(
		S = 153,
		B = 153,
		E = 162,
		L = 131,
		A = 153,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 673,
	label = "Cs-CsCs(Os-R)H",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   O2s u0 {1,S} {6,S}
5   H  u0 {1,S}
6   R!H u0 {4,S}
""",
	solute = SoluteData(
		S = 0.03766,
		B = 0.08419,
		E = 0.00000,
		L = 0.33244,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 96,
		B = 83,
		E = 112,
		L = 91,
		A = 110,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 674,
	label = "Crs-CrsCrs(Ors-R)H",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 r1 {1,S}
3   Cs u0 r1 {1,S}
4   O2s u0 r1 {1,S} {6,S}
5   H  u0 {1,S}
6   R!H u0 {4,S}
""",
	solute = SoluteData(
		S = 0.12656,
		B = 0.03721,
		E = 0.13974,
		L = 0.37174,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 34,
		B = 34,
		E = 34,
		L = 26,
		A = 35,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 675,
	label = "Crs-CrsCs(Ors-R)H",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 r1 {1,S}
3   Cs u0 {1,S}
4   O2s u0 r1 {1,S} {6,S}
5   H  u0 {1,S}
6   R!H u0 {4,S}
""",
	solute = SoluteData(
		S = 0.22051,
		B = -0.00409,
		E = 0.08250,
		L = 0.46345,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 96,
		B = 96,
		E = 99,
		L = 93,
		A = 98,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 676,
	label = "Crs-CrsCrs(Os-R)H",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 r1 {1,S}
3   Cs u0 r1 {1,S}
4   O2s u0 {1,S} {6,S}
5   H  u0 {1,S}
6   R!H u0 {4,S}
""",
	solute = SoluteData(
		S = -0.05071,
		B = 0.14573,
		E = 0.06871,
		L = 0.63723,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 75,
		B = 75,
		E = 76,
		L = 70,
		A = 76,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 677,
	label = "Cs-CdsCsOsH",
	group = 
"""
1 * Cs         u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO,CS] u0 {1,S}
3   Cs         u0 {1,S}
4   O2s        u0 {1,S}
5   H          u0 {1,S}
""",
	solute = u'Cs-(Cds-Cd)CsOsH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 678,
	label = "Cs-(Cds-O2d)CsOsH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   O2s u0 {1,S}
5   H  u0 {1,S}
6   O2d u0 {2,D}
""",
	solute = u'Cs-(Cds-O2d)Cs(Os-H)H',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 679,
	label = "Cs-(Cds-O2d)Cs(Os-H)H",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   O2s u0 {1,S} {7,S}
5   H  u0 {1,S}
6   O2d u0 {2,D}
7   H  u0 {4,S}
""",
	solute = SoluteData(
		S = -0.06555,
		B = -0.07916,
		E = -0.01119,
		L = -0.20619,
		A = -0.05781,
	),
	dataCount = DataCountGAV(
		S = 17,
		B = 17,
		E = 20,
		L = 16,
		A = 17,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 680,
	label = "Cs-(Cds-O2d)Cs(Os-R)H",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   O2s u0 {1,S} {7,S}
5   H  u0 {1,S}
6   O2d u0 {2,D}
7   R!H u0 {4,S}
""",
	solute = SoluteData(
		S = -0.28451,
		B = 0.18035,
		E = 0.09668,
		L = -0.28628,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 15,
		B = 15,
		E = 16,
		L = 13,
		A = 15,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 681,
	label = "Cs-(Cds-Cd)CsOsH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   O2s u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
	solute = u'Cs-(Cds-Cds)CsOsH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 682,
	label = "Cs-(Cds-Cds)CsOsH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   O2s u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
	solute = u'Cs-(Cds-Cds)Cs(Os-H)H',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 683,
	label = "Cs-(Cds-Cds)Cs(Os-H)H",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   O2s u0 {1,S} {7,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
7   H  u0 {4,S}
""",
	solute = SoluteData(
		S = -0.03875,
		B = 0.15167,
		E = 0.04011,
		L = 0.12938,
		A = 0.03244,
	),
	dataCount = DataCountGAV(
		S = 26,
		B = 27,
		E = 28,
		L = 24,
		A = 27,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 684,
	label = "Cs-(Cds-Cds)Cs(Os-R)H",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   O2s u0 {1,S} {7,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
7   R!H u0 {4,S}
""",
	solute = SoluteData(
		S = 0.12285,
		B = 0.02076,
		E = -0.01405,
		L = 0.34251,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 18,
		B = 18,
		E = 18,
		L = 17,
		A = 21,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 685,
	label = "Cs-CtCsOsH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Cs u0 {1,S}
4   O2s u0 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.01351,
		B = 0.02384,
		E = -0.05187,
		L = -0.07799,
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
	index = 686,
	label = "Cs-CbCsOsH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cs u0 {1,S}
4   O2s u0 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = -0.11575,
		B = 0.07941,
		E = 0.03257,
		L = 0.14228,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 38,
		B = 37,
		E = 41,
		L = 37,
		A = 39,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 687,
	label = "Cs-CbCdsOsH",
	group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   O2s      u0 {1,S}
5   H       u0 {1,S}
""",
	solute = u'Cs-(Cds-O2d)CbOsH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 688,
	label = "Cs-(Cds-O2d)CbOsH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   O2s u0 {1,S}
5   H  u0 {1,S}
6   O2d u0 {2,D}
""",
	solute = SoluteData(
		S = 0.00947,
		B = 0.02578,
		E = 0.00534,
		L = 0.01230,
		A = -0.02657,
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
	index = 689,
	label = "Cs-CbCbOsH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
4   O2s u0 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = -0.01550,
		B = 0.01210,
		E = 0.00780,
		L = 0.10645,
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
	index = 690,
	label = "Cs-COsHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   O2s u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = u'Cs-CsOsHH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 691,
	label = "Cs-CsOsHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   O2s u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = u'Cs-Cs(Os-R)HH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 692,
	label = "Cs-Cs(Os-H)HH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   O2s u0 {1,S} {6,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   H  u0 {3,S}
""",
	solute = SoluteData(
		S = 0.12262,
		B = 0.02183,
		E = -0.01428,
		L = 0.24975,
		A = 0.03295,
	),
	dataCount = DataCountGAV(
		S = 281,
		B = 271,
		E = 292,
		L = 254,
		A = 283,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 693,
	label = "Cs-Cs(Os-R)HH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   O2s u0 {1,S} {6,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   R!H u0 {3,S}
""",
	solute = SoluteData(
		S = 0.06941,
		B = 0.08610,
		E = 0.00000,
		L = 0.43827,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 844,
		B = 825,
		E = 907,
		L = 790,
		A = 910,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 694,
	label = "Crs-Crs(Ors-R)HH",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 r1 {1,S}
3   O2s u0 r1 {1,S} {6,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   R!H u0 {3,S}
""",
	solute = SoluteData(
		S = 0.11646,
		B = 0.07056,
		E = 0.03960,
		L = 0.36313,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 106,
		B = 106,
		E = 115,
		L = 105,
		A = 115,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 695,
	label = "Cs-CdsOsHH",
	group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   O2s      u0 {1,S}
4   H       u0 {1,S}
5   H       u0 {1,S}
""",
	solute = u'Cs-(Cds-Cd)OsHH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 696,
	label = "Cs-(Cds-O2d)OsHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   O2s u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   O2d u0 {2,D}
""",
	solute = u'Cs-(Cds-O2d)(Os-R)HH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 697,
	label = "Cs-(Cds-O2d)(Os-H)HH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   O2s u0 {1,S} {7,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   O2d u0 {2,D}
7   H  u0 {3,S}
""",
	solute = SoluteData(
		S = 0.01335,
		B = -0.07053,
		E = 0.00707,
		L = -0.10246,
		A = -0.02235,
	),
	dataCount = DataCountGAV(
		S = 26,
		B = 26,
		E = 27,
		L = 16,
		A = 26,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 698,
	label = "Cs-(Cds-O2d)(Os-R)HH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   CO u0 {1,S} {6,D}
3   O2s u0 {1,S} {7,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   O2d u0 {2,D}
7   R!H u0 {3,S}
""",
	solute = SoluteData(
		S = -0.28532,
		B = 0.10197,
		E = 0.01050,
		L = 0.05128,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 66,
		B = 66,
		E = 67,
		L = 62,
		A = 66,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 699,
	label = "Cs-(Cds-Cd)OsHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   O2s u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
	solute = u'Cs-(Cds-Cds)OsHH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 700,
	label = "Cs-(Cds-Cds)OsHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   O2s u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
	solute = u'Cs-(Cds-Cds)(Os-R)HH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 701,
	label = "Cs-(Cds-Cds)(Os-H)HH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   O2s u0 {1,S} {7,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
7   H  u0 {3,S}
""",
	solute = SoluteData(
		S = 0.10814,
		B = 0.04961,
		E = 0.01276,
		L = 0.23619,
		A = 0.08638,
	),
	dataCount = DataCountGAV(
		S = 24,
		B = 23,
		E = 25,
		L = 23,
		A = 24,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 702,
	label = "Cs-(Cds-Cds)(Os-R)HH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   O2s u0 {1,S} {7,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
7   R!H u0 {3,S}
""",
	solute = SoluteData(
		S = 0.03348,
		B = 0.05687,
		E = 0.01458,
		L = 0.42585,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 67,
		B = 63,
		E = 67,
		L = 66,
		A = 67,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 703,
	label = "Cs-(Cds-Nd)OsHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   O2s u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   N  u0 {2,D}
""",
	solute = u'Cs-(Cds-N3d)OsHH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 704,
	label = "Cs-(Cds-N3d)OsHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   O2s u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   N3d u0 {2,D}
""",
	solute = SoluteData(
		S = -0.01504,
		B = 0.05106,
		E = -0.07988,
		L = 0.00797,
		A = 0.05917,
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
	index = 705,
	label = "Cs-CtOsHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   O2s u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = u'Cs-Ct(Os-H)HH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 706,
	label = "Cs-Ct(Os-H)HH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   O2s u0 {1,S} {6,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   H  u0 {3,S}
""",
	solute = SoluteData(
		S = 0.02191,
		B = 0.02064,
		E = -0.02182,
		L = -0.19580,
		A = 0.05311,
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
	index = 707,
	label = "Cs-Ct(Os-R)HH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   O2s u0 {1,S} {6,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   R!H u0 {3,S}
""",
	solute = SoluteData(
		S = -0.05880,
		B = 0.01227,
		E = 0.00731,
		L = -0.08402,
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
	index = 708,
	label = "Cs-CbOsHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   O2s u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = u'Cs-Cb(Os-R)HH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 709,
	label = "Cs-Cb(Os-H)HH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   O2s u0 {1,S} {6,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   H  u0 {3,S}
""",
	solute = SoluteData(
		S = 0.06494,
		B = 0.02146,
		E = 0.00119,
		L = -0.04258,
		A = 0.14012,
	),
	dataCount = DataCountGAV(
		S = 41,
		B = 40,
		E = 51,
		L = 25,
		A = 45,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 710,
	label = "Cs-Cb(Os-R)HH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   O2s u0 {1,S} {6,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   R!H u0 {3,S}
""",
	solute = SoluteData(
		S = -0.03773,
		B = 0.02312,
		E = 0.00095,
		L = 0.02842,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 45,
		B = 40,
		E = 45,
		L = 43,
		A = 46,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 711,
	label = "Cs-CCCS",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
5   S u0 {1,S}
""",
	solute = SoluteData(
		S = 0.02898,
		B = 0.16094,
		E = 0.08614,
		L = 0.39673,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 29,
		B = 29,
		E = 29,
		L = 28,
		A = 33,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 712,
	label = "Cs-CCC(S-H)",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
5   S u0 {1,S} {6,S}
6   H  u0 {5,S}
""",
	solute = SoluteData(
		S = 0.02770,
		B = 0.07080,
		E = 0.04513,
		L = 0.32328,
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
	index = 713,
	label = "Cs-CCSS",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   S  u0 {1,S}
5   S  u0 {1,S}
""",
	solute = u'Cs-CsCsSS',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 714,
	label = "Cs-CsCsSS",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   S  u0 {1,S}
5   S  u0 {1,S}
""",
	solute = SoluteData(
		S = -0.26901,
		B = -0.00438,
		E = -0.22663,
		L = -0.23993,
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
	index = 715,
	label = "Cs-CCSH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   S  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = -0.01002,
		B = -0.01272,
		E = 0.02622,
		L = 0.33580,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
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
	index = 716,
	label = "Cs-CsCsSH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   S  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.17437,
		B = 0.11405,
		E = 0.08230,
		L = 0.47917,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 18,
		B = 17,
		E = 20,
		L = 16,
		A = 25,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 717,
	label = "Cs-CsCs(S-H)H",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   S  u0 {1,S} {6,S}
5   H  u0 {1,S}
6   H  u0 {4,S}
""",
	solute = SoluteData(
		S = 0.07289,
		B = 0.05923,
		E = 0.09058,
		L = 0.49396,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 4,
		B = 4,
		E = 5,
		L = 4,
		A = 5,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 718,
	label = "Cs-CSHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   S  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = -0.02061,
		B = 0.10080,
		E = -0.00039,
		L = 0.17217,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
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
	index = 719,
	label = "Crs-CrSrHH",
	group = 
"""
1 * Cs u0 r1 {2,S} {3,S} {4,S} {5,S}
2   C  u0 r1 {1,S}
3   S  u0 r1 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.21372,
		B = 0.09377,
		E = 0.11274,
		L = 0.62238,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 22,
		B = 21,
		E = 23,
		L = 20,
		A = 24,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 720,
	label = "Cs-CsSHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   S  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = u'Cs-CsS2HH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 721,
	label = "Cs-CsS2HH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   S2s u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.12784,
		B = 0.07985,
		E = 0.10616,
		L = 0.64136,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 106,
		B = 108,
		E = 128,
		L = 104,
		A = 130,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 722,
	label = "Cs-Cs(S2-H)HH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   S2s u0 {1,S} {6,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   H  u0 {3,S}
""",
	solute = SoluteData(
		S = 0.15263,
		B = 0.05553,
		E = 0.15386,
		L = 0.84696,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 23,
		B = 23,
		E = 23,
		L = 23,
		A = 23,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 723,
	label = "Cs-CsS4HH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   [S4s,S4d,S4b,S4t] u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.36935,
		B = 0.20182,
		E = 0.05648,
		L = 0.62285,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 9,
		B = 7,
		E = 10,
		L = 7,
		A = 13,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 724,
	label = "Cs-CsS6HH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   [S6s,S6d,S6dd,S6t,S6td] u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.17886,
		B = 0.14814,
		E = 0.09700,
		L = 0.20515,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 12,
		B = 12,
		E = 13,
		L = 5,
		A = 12,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 725,
	label = "Cs-CdsSsHH",
	group = 
"""
1 * Cs         u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO,CS] u0 {1,S}
3   S2s        u0 {1,S}
4   H          u0 {1,S}
5   H          u0 {1,S}
""",
	solute = SoluteData(
		S = -0.02496,
		B = 0.09717,
		E = 0.12336,
		L = 0.37926,
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
	index = 726,
	label = "Cs-(Cds-Cd)SsHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   S2s u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
	solute = u'Cs-(Cds-Cds)SsHH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 727,
	label = "Cs-(Cds-Cds)SsHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   S2s u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
	solute = SoluteData(
		S = 0.13330,
		B = 0.02846,
		E = 0.14249,
		L = 0.79871,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 26,
		B = 26,
		E = 27,
		L = 19,
		A = 26,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 728,
	label = "Cs-(Cds-Od)SsHH",
	group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   S2s u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
""",
	solute = SoluteData(
		S = 0.16918,
		B = 0.01527,
		E = 0.10263,
		L = 0.57606,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 9,
		B = 9,
		E = 9,
		L = 9,
		A = 9,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 729,
	label = "Cs-CbSsHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   S2s u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = -0.01133,
		B = -0.00966,
		E = 0.11321,
		L = 0.33966,
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
	index = 730,
	label = "Cs-CS4dHH",
	group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   C   u0 {1,S}
3   S4d u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.08311,
		B = 0.06174,
		E = 0.07144,
		L = 0.53261,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 3,
		L = 3,
		A = 4,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 731,
	label = "Cs-SsHHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   S  u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = u'Cs-S2sHHH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 732,
	label = "Cs-S2sHHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   S2s  u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.14259,
		B = 0.03954,
		E = 0.12254,
		L = 0.60167,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 54,
		B = 53,
		E = 55,
		L = 53,
		A = 55,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 733,
	label = "Cs-S4HHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   [S4s,S4d,S4b,S4t]  u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.30364,
		B = 0.15869,
		E = 0.11391,
		L = 0.69181,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 11,
		B = 11,
		E = 11,
		L = 11,
		A = 13,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 734,
	label = "Cs-S6HHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   [S6s,S6d,S6dd,S6t,S6td]  u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.23884,
		B = 0.06128,
		E = 0.04970,
		L = 0.41058,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 26,
		B = 25,
		E = 28,
		L = 21,
		A = 29,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 735,
	label = "Cs-SsSsHH",
	group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   S  u0 {1,S}
3   S  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.12853,
		B = 0.04914,
		E = 0.10862,
		L = 0.25645,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 4,
		L = 1,
		A = 4,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 736,
	label = "O",
	group = 
"""
1 * O u0
""",
	solute = u'O2s',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 737,
	label = "O2d",
	group = 
"""
1 * O2d u0
""",
	solute = u'O2d-Cd',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 738,
	label = "O2d-Cd",
	group = 
"""
1 * O2d u0 {2,D}
2   CO u0 {1,D}
""",
	solute = SoluteData(
		S = 0.42260,
		B = 0.26426,
		E = 0.16122,
		L = 1.33788,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 2468,
		B = 2432,
		E = 2569,
		L = 2186,
		A = 2577,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 739,
	label = "O2d-Crd",
	group = 
"""
1 * O2d u0    {2,D}
2   CO  u0 r1 {1,D}
""",
	solute = SoluteData(
		S = 0.38858,
		B = 0.25281,
		E = 0.25209,
		L = 1.17012,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 768,
		B = 768,
		E = 786,
		L = 629,
		A = 780,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 740,
	label = "O2d-Cdd",
	group = 
"""
1 * O2d u0 {2,D}
2   Cdd u0 {1,D}
""",
	solute = SoluteData(
		S = 0.16925,
		B = 0.04807,
		E = 0.06879,
		L = 0.50992,
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
	index = 741,
	label = "O2d-N3d",
	group = 
"""
1 * O2d  u0 {2,D}
2   N3d u0 {1,D}
""",
	solute = SoluteData(
		S = 0.30062,
		B = 0.11165,
		E = 0.09620,
		L = 0.66859,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 54,
		B = 54,
		E = 62,
		L = 54,
		A = 64,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 742,
	label = "O2d-N5dc",
	group = 
"""
1 * O2d  u0 {2,D}
2   N5dc u0 {1,D}
""",
	solute = SoluteData(
		S = 0.15169,
		B = 0.01884,
		E = 0.15896,
		L = 0.50229,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 370,
		B = 369,
		E = 384,
		L = 322,
		A = 384,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 743,
	label = "O2d-Sd",
	group = 
"""
1 * O2d   u0 {2,D}
2   S     ux {1,D}
""",
	solute = u'O2d-S6dd',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 744,
	label = "O2d-S4d",
	group = 
"""
1 * O2d   u0 {2,D}
2   S4d   u0 {1,D}
""",
	solute = SoluteData(
		S = 0.43270,
		B = 0.32003,
		E = 0.25408,
		L = 1.50388,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 26,
		B = 23,
		E = 30,
		L = 23,
		A = 43,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 745,
	label = "O2d-S6dd",
	group = 
"""
1 * O2d   u0 {2,D}
2   S6dd  u0 {1,D}
""",
	solute = SoluteData(
		S = 0.42033,
		B = 0.23748,
		E = 0.13369,
		L = 1.18320,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 185,
		B = 183,
		E = 199,
		L = 164,
		A = 194,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 746,
	label = "O2d-P5d",
	group = 
"""
1 * O2d  u0 {2,D}
2   P5d  u0 {1,D}
""",
	solute = SoluteData(
		S = 0.31224,
		B = 0.33431,
		E = 0.01768,
		L = 1.02636,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 63,
		B = 62,
		E = 87,
		L = 62,
		A = 88,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 747,
	label = "O2s",
	group = 
"""
1 * O2s u0
""",
	solute = u'O2s-CC',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 748,
	label = "O2s-PH",
	group = 
"""
1 * O2s u0 {2,S} {3,S}
2   P  u0 {1,S}
3   H  u0 {1,S}
""",
	solute = u'O2s-P5dH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 749,
	label = "O2s-P5dH",
	group = 
"""
1 * O2s u0 {2,S} {3,S}
2   P5d u0 {1,S}
3   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.08424,
		B = 0.23799,
		E = 0.20451,
		L = 0.75843,
		A = 0.76359,
	),
	dataCount = DataCountGAV(
		S = 30,
		B = 30,
		E = 33,
		L = 30,
		A = 33,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 750,
	label = "O2s-PC",
	group = 
"""
1 * O2s u0 {2,S} {3,S}
2   P  u0 {1,S}
3   C  u0 {1,S}
""",
	solute = u'O2s-P5dC',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 751,
	label = "O2s-P3sC",
	group = 
"""
1 * O2s u0 {2,S} {3,S}
2   P3s u0 {1,S}
3   C  u0 {1,S}
""",
	solute = u'O2s-P3sCs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 752,
	label = "O2s-P3sCs",
	group = 
"""
1 * O2s u0 {2,S} {3,S}
2   P3s u0 {1,S}
3   Cs u0 {1,S}
""",
	solute = SoluteData(
		S = 0.11817,
		B = 0.20538,
		E = 0.01933,
		L = 0.53571,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
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
	index = 753,
	label = "O2s-P5dC",
	group = 
"""
1 * O2s u0 {2,S} {3,S}
2   P5d u0 {1,S}
3   C  u0 {1,S}
""",
	solute = u'O2s-P5dCs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 754,
	label = "O2s-P5dCs",
	group = 
"""
1 * O2s u0 {2,S} {3,S}
2   P5d u0 {1,S}
3   Cs  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.08609,
		B = 0.16265,
		E = 0.04349,
		L = 0.58522,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 43,
		B = 42,
		E = 55,
		L = 42,
		A = 54,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 755,
	label = "O2s-P5dCd",
	group = 
"""
1 * O2s u0 {2,S} {3,S}
2   P5d u0 {1,S}
3   [Cd,CO,CS] u0 {1,S}
""",
	solute = None,
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 756,
	label = "O2s-P5d(Cd-Nd)",
	group = 
"""
1 * O2s u0 {2,S} {3,S}
2   P5d u0 {1,S}
3   Cd  u0 {1,S} {4,D}
4   N   u0 {3,D}
""",
	solute = SoluteData(
		S = 0.07004,
		B = 0.02526,
		E = 0.10284,
		L = 0.56260,
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
	index = 757,
	label = "O2s-P5dCb",
	group = 
"""
1 * O2s u0 {2,S} {3,S}
2   P5d u0 {1,S}
3   Cb  u0 {1,S}
""",
	solute = SoluteData(
		S = -0.01893,
		B = 0.04914,
		E = 0.03414,
		L = 0.33853,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 20,
		B = 20,
		E = 20,
		L = 20,
		A = 20,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 758,
	label = "O2s-NH",
	group = 
"""
1 * O2s u0 {2,S} {3,S}
2   N  u0 {1,S}
3   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.12364,
		B = 0.18761,
		E = 0.16199,
		L = 0.56775,
		A = 0.30096,
	),
	dataCount = DataCountGAV(
		S = 29,
		B = 29,
		E = 30,
		L = 28,
		A = 30,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 759,
	label = "O2s-NR",
	group = 
"""
1 * O2s u0 {2,S} {3,S}
2   N  u0 {1,S}
3   R!H u0 {1,S}
""",
	solute = u'O2s-CN',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 760,
	label = "O2s-CN",
	group = 
"""
1 * O2s u0 {2,S} {3,S}
2   C  u0 {1,S}
3   N  u0 {1,S}
""",
	solute = u'O2s-CdN3d',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 761,
	label = "O2s-CbN3d",
	group = 
"""
1 * O2s  u0 {2,S} {3,S}
2   N3d u0 {1,S}
3   Cb  u0 {1,S}
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
	index = 762,
	label = "O2s-CsN3s",
	group = 
"""
1 * O2s  u0 {2,S} {3,S}
2   N3s u0 {1,S}
3   Cs  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.02377,
		B = 0.09308,
		E = 0.06653,
		L = 0.33936,
		A = -0.00146,
	),
	dataCount = DataCountGAV(
		S = 6,
		B = 6,
		E = 6,
		L = 6,
		A = 7,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 763,
	label = "O2s-CsN3d",
	group = 
"""
1 * O2s  u0 {2,S} {3,S}
2   Cs  u0 {1,S}
3   N3d u0 {1,S}
""",
	solute = u'O2s-Cs(N3d-Od)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 764,
	label = "O2s-Cs(N3d-Od)",
	group = 
"""
1 * O2s  u0 {2,S} {4,S}
2   N3d u0 {1,S} {3,D}
3   O2d  u0 {2,D}
4   Cs  u0 {1,S}
""",
	solute = SoluteData(
		S = -0.01340,
		B = 0.04305,
		E = -0.01741,
		L = 0.03588,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 5,
		E = 13,
		L = 5,
		A = 15,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 765,
	label = "O2s-Cs(N3d-Cd)",
	group = 
"""
1 * O2s  u0 {2,S} {4,S}
2   N3d u0 {1,S} {3,D}
3   Cd  u0 {2,D}
4   Cs  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.04544,
		B = 0.07594,
		E = 0.08985,
		L = 0.59921,
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
	index = 766,
	label = "O2s-CdN3d",
	group = 
"""
1 * O2s        u0 {2,S} {3,S}
2   [Cd,CO,CS] u0 {1,S}
3   N3d        u0 {1,S}
""",
	solute = SoluteData(
		S = 0.05602,
		B = 0.08093,
		E = 0.06540,
		L = 0.30162,
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
	index = 767,
	label = "O2s-CsN5dc",
	group = 
"""
1 * O2s  u0 {2,S} {3,S}
2   Cs  u0 {1,S}
3   N5dc u0 {1,S}
""",
	solute = SoluteData(
		S = 0.09525,
		B = -0.07354,
		E = -0.06071,
		L = 0.07396,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 7,
		B = 8,
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
	index = 768,
	label = "O2s-OsH",
	group = 
"""
1 * O2s u0 {2,S} {3,S}
2   O2s u0 {1,S}
3   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.15824,
		B = 0.05902,
		E = 0.12734,
		L = 0.46756,
		A = 0.23700,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 4,
		L = 3,
		A = 6,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 769,
	label = "O2s-CH",
	group = 
"""
1 * O2s u0 {2,S} {3,S}
2   C  u0 {1,S}
3   H  u0 {1,S}
""",
	solute = u'O2s-CsH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 770,
	label = "O2s-CdsH",
	group = 
"""
1 * O2s      u0 {2,S} {3,S}
2   [Cd,CO] u0 {1,S}
3   H       u0 {1,S}
""",
	solute = u'O2s-(Cds-O2d)H',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 771,
	label = "O2s-(Cds-O2d)H",
	group = 
"""
1 * O2s u0 {2,S} {3,S}
2   CO u0 {1,S} {4,D}
3   H  u0 {1,S}
4   O2d u0 {2,D}
""",
	solute = SoluteData(
		S = 0.15290,
		B = 0.05529,
		E = 0.06258,
		L = 0.41728,
		A = 0.48657,
	),
	dataCount = DataCountGAV(
		S = 538,
		B = 538,
		E = 549,
		L = 496,
		A = 538,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 772,
	label = "O2s-(Cds-Cd)H",
	group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cd u0 {1,S} {4,D}
3   H  u0 {1,S}
4   C  u0 {2,D}
""",
	solute = SoluteData(
		S = 0.09007,
		B = 0.18326,
		E = 0.21389,
		L = 0.64439,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 72,
		B = 72,
		E = 73,
		L = 54,
		A = 72,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 773,
	label = "O2s-CsH",
	group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cs u0 {1,S}
3   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.28190,
		B = 0.34836,
		E = 0.21079,
		L = 0.99143,
		A = 0.25925,
	),
	dataCount = DataCountGAV(
		S = 759,
		B = 747,
		E = 798,
		L = 669,
		A = 768,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 774,
	label = "O2s-CbH",
	group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cb u0 {1,S}
3   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.26135,
		B = 0.08802,
		E = 0.18865,
		L = 0.57213,
		A = 0.43104,
	),
	dataCount = DataCountGAV(
		S = 634,
		B = 617,
		E = 669,
		L = 625,
		A = 644,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 775,
	label = "O2s-OsC",
	group = 
"""
1 * O2s u0 {2,S} {3,S}
2   O2s u0 {1,S}
3   C  u0 {1,S}
""",
	solute = u'O2s-OsCs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 776,
	label = "O2s-OsCds",
	group = 
"""
1 * O2s      u0 {2,S} {3,S}
2   O2s      u0 {1,S}
3   [Cd,CO] u0 {1,S}
""",
	solute = u'O2s-O2s(Cds-O2d)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 777,
	label = "O2s-O2s(Cds-O2d)",
	group = 
"""
1 * O2s u0 {2,S} {3,S}
2   CO u0 {1,S} {4,D}
3   O2s u0 {1,S}
4   O2d u0 {2,D}
""",
	solute = SoluteData(
		S = 0.14030,
		B = 0.01441,
		E = 0.00425,
		L = 0.24733,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 3,
		L = 3,
		A = 6,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 778,
	label = "O2s-OsCs",
	group = 
"""
1 * O2s u0 {2,S} {3,S}
2   O2s u0 {1,S}
3   Cs u0 {1,S}
""",
	solute = SoluteData(
		S = 0.06478,
		B = 0.23841,
		E = 0.03638,
		L = 0.50419,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 9,
		B = 9,
		E = 10,
		L = 9,
		A = 9,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 779,
	label = "O2s-CC",
	group = 
"""
1 * O2s u0 {2,S} {3,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
""",
	solute = u'O2s-CsCs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 780,
	label = "O2s-CtCb",
	group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Ct u0 {1,S}
3   Cb u0 {1,S}
""",
	solute = u'O2s-(Ct-N3t)Cb',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 781,
	label = "O2s-(Ct-N3t)Cb",
	group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Ct u0 {1,S} {4,T}
3   Cb u0 {1,S}
4   N3t u0 {2,T}
""",
	solute = SoluteData(
		S = 0.02528,
		B = 0.01601,
		E = -0.00086,
		L = -0.00928,
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
	index = 782,
	label = "O2s-CdsCds",
	group = 
"""
1 * O2s      u0 {2,S} {3,S}
2   [Cd,CO] u0 {1,S}
3   [Cd,CO] u0 {1,S}
""",
	solute = u'O2s-(Cds-Cd)(Cds-Cd)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 783,
	label = "O2s-(Cds-O2d)(Cds-O2d)",
	group = 
"""
1 * O2s u0 {2,S} {3,S}
2   CO u0 {1,S} {4,D}
3   CO u0 {1,S} {5,D}
4   O2d u0 {2,D}
5   O2d u0 {3,D}
""",
	solute = SoluteData(
		S = -0.04290,
		B = -0.07575,
		E = -0.03043,
		L = -0.20861,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 7,
		L = 3,
		A = 8,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 784,
	label = "O2s-(Cds-O2d)(Cds-Cd)",
	group = 
"""
1 * O2s u0 {2,S} {3,S}
2   CO u0 {1,S} {5,D}
3   Cd u0 {1,S} {4,D}
4   C  u0 {3,D}
5   O2d u0 {2,D}
""",
	solute = SoluteData(
		S = -0.01328,
		B = 0.01879,
		E = 0.00060,
		L = -0.00504,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 6,
		B = 5,
		E = 5,
		L = 6,
		A = 6,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 785,
	label = "O2s-(Cds-Cd)(Cds-Cd)",
	group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cd u0 {1,S}
3   Cd u0 {1,S}
""",
	solute = SoluteData(
		S = 0.04121,
		B = 0.03783,
		E = 0.05339,
		L = 0.46124,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 61,
		B = 61,
		E = 67,
		L = 43,
		A = 72,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 786,
	label = "O2s-CdsCs",
	group = 
"""
1 * O2s        u0 {2,S} {3,S}
2   [Cd,CO,CS] u0 {1,S}
3   Cs         u0 {1,S}
""",
	solute = u'O2s-Cs(Cds-O2d)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 787,
	label = "O2s-Cs(Cds-N3d)",
	group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cd u0 {1,S} {4,D}
3   Cs u0 {1,S}
4   N3d u0 {2,D}
""",
	solute = SoluteData(
		S = 0.06125,
		B = 0.03441,
		E = 0.03006,
		L = 0.31039,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 27,
		B = 27,
		E = 29,
		L = 22,
		A = 29,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 788,
	label = "O2s-Cs(Cds-O2d)",
	group = 
"""
1 * O2s u0 {2,S} {3,S}
2   CO u0 {1,S} {4,D}
3   Cs u0 {1,S}
4   O2d u0 {2,D}
""",
	solute = SoluteData(
		S = 0.07252,
		B = 0.03205,
		E = -0.04931,
		L = 0.14232,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 996,
		B = 975,
		E = 1028,
		L = 916,
		A = 1025,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 789,
	label = "O2s-Cs(Cds-Cd)",
	group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cd u0 {1,S} {4,D}
3   Cs u0 {1,S}
4   C  u0 {2,D}
""",
	solute = SoluteData(
		S = 0.09456,
		B = 0.13261,
		E = 0.05365,
		L = 0.26657,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 37,
		B = 38,
		E = 43,
		L = 34,
		A = 44,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 790,
	label = "O2s-Cs(Cds-Sd)",
	group = 
"""
1 * O2s u0 {2,S} {3,S}
2   CS u0 {1,S} {4,D}
3   Cs u0 {1,S}
4   S  u0 {2,D}
""",
	solute = SoluteData(
		S = 0.00785,
		B = 0.00141,
		E = -0.04527,
		L = 0.11173,
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
	index = 791,
	label = "O2s-CdsCb",
	group = 
"""
1 * O2s        u0 {2,S} {3,S}
2   [Cd,CO,CS] u0 {1,S}
3   Cb         u0 {1,S}
""",
	solute = u'O2s-Cb(Cds-Cd)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 792,
	label = "O2s-Cb(Cds-N3d)",
	group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cd  u0 {1,S} {4,D}
3   Cb  u0 {1,S}
4   N3d u0 {2,D}
""",
	solute = SoluteData(
		S = 0.03802,
		B = 0.02363,
		E = 0.00980,
		L = 0.17607,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 5,
		E = 5,
		L = 4,
		A = 5,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 793,
	label = "O2s-Cb(Cds-O2d)",
	group = 
"""
1 * O2s u0 {2,S} {3,S}
2   CO u0 {1,S} {4,D}
3   Cb u0 {1,S}
4   O2d u0 {2,D}
""",
	solute = SoluteData(
		S = 0.06482,
		B = -0.03227,
		E = -0.04910,
		L = -0.00387,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 66,
		B = 63,
		E = 66,
		L = 55,
		A = 73,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 794,
	label = "O2s-Cb(Cds-Cd)",
	group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cd u0 {1,S} {4,D}
3   Cb u0 {1,S}
4   C  u0 {2,D}
""",
	solute = SoluteData(
		S = -0.05921,
		B = 0.07025,
		E = 0.03402,
		L = 0.27689,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 101,
		B = 101,
		E = 102,
		L = 98,
		A = 101,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 795,
	label = "O2s-Cb(Cds-Sd)",
	group = 
"""
1 * O2s u0 {2,S} {3,S}
2   CS u0 {1,S} {4,D}
3   Cb u0 {1,S}
4   S  u0 {2,D}
""",
	solute = u'O2s-Cb(Cds-O2d)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 796,
	label = "O2s-CsCs",
	group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
""",
	solute = SoluteData(
		S = 0.03540,
		B = 0.29928,
		E = 0.00000,
		L = 0.92651,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 307,
		B = 284,
		E = 329,
		L = 293,
		A = 335,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 797,
	label = "O2rs-CrsCrs",
	group = 
"""
1 * O2s u0 r1 {2,S} {3,S}
2   Cs u0 r1 {1,S}
3   Cs u0 r1 {1,S}
""",
	solute = SoluteData(
		S = 0.03592,
		B = 0.19310,
		E = 0.00139,
		L = 0.61888,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 173,
		B = 173,
		E = 182,
		L = 161,
		A = 182,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 798,
	label = "O2s-CsCb",
	group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cs u0 {1,S}
3   Cb u0 {1,S}
""",
	solute = SoluteData(
		S = 0.13149,
		B = 0.04434,
		E = 0.03978,
		L = 0.32573,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 451,
		B = 425,
		E = 467,
		L = 425,
		A = 461,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 799,
	label = "O2rs-CrsCb",
	group = 
"""
1 * O2s u0 r1 {2,S} {3,S}
2   Cs u0 r1 {1,S}
3   Cb u0 r1 {1,S}
""",
	solute = SoluteData(
		S = 0.06190,
		B = 0.10797,
		E = 0.02966,
		L = 0.42495,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 56,
		B = 56,
		E = 58,
		L = 55,
		A = 56,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 800,
	label = "O2s-CbCb",
	group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
""",
	solute = SoluteData(
		S = -0.04687,
		B = -0.08139,
		E = -0.01455,
		L = -0.11860,
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
	index = 801,
	label = "O2rs-CbCb",
	group = 
"""
1 * O2s u0 r1 {2,S} {3,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
""",
	solute = SoluteData(
		S = -0.10408,
		B = -0.03940,
		E = 0.00652,
		L = -0.14347,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 21,
		B = 21,
		E = 21,
		L = 18,
		A = 21,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 802,
	label = "O2s-CS",
	group = 
"""
1 * O2s   u0 {2,S} {3,S}
2   S     ux {1,S}
3   C     ux {1,S}
""",
	solute = SoluteData(
		S = -0.22144,
		B = 0.00791,
		E = -0.00817,
		L = 0.04782,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 8,
		B = 8,
		E = 15,
		L = 8,
		A = 17,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 803,
	label = "O2s-SH",
	group = 
"""
1 * O2s   u0 {2,S} {3,S}
2   S     ux {1,S}
3   H     ux {1,S}
""",
	solute = u'O2s-S_DeH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 804,
	label = "O2s-S_DeH",
	group = 
"""
1 * O2s   u0 {2,S} {3,S}
2   [S4d,S6d,S6dd]   ux {1,S}
3   H     ux {1,S}
""",
	solute = SoluteData(
		S = 0.24344,
		B = 0.24590,
		E = 0.02099,
		L = 0.29051,
		A = 0.16623,
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
	index = 805,
	label = "Oc",
	group = 
"""
1 * O0sc u0 c-1
""",
	solute = u'Oc-N5c',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 806,
	label = "Oc-N5c",
	group = 
"""
1 * O0sc u0 c-1 {2,S}
2   [N5sc,N5dc] u0 c+1 {1,S}
""",
	solute = SoluteData(
		S = 0.35077,
		B = 0.16739,
		E = 0.14849,
		L = 0.98834,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 386,
		B = 385,
		E = 405,
		L = 338,
		A = 400,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 807,
	label = "S",
	group = 
"""
1 * S ux
""",
	solute = u'S2s',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 808,
	label = "S2d",
	group = 
"""
1 * S2d u0
""",
	solute = u'S2d-C',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 809,
	label = "S2d-C",
	group = 
"""
1 * S2d u0 {2,D}
2   C u0 {1,D}
""",
	solute = SoluteData(
		S = 0.44085,
		B = 0.14681,
		E = 0.47907,
		L = 1.86092,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 40,
		B = 42,
		E = 43,
		L = 35,
		A = 48,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 810,
	label = "S2d-P",
	group = 
"""
1 * S2d u0 {2,D}
2   P u0 {1,D}
""",
	solute = u'S2d-P5d',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 811,
	label = "S2d-P5d",
	group = 
"""
1 * S2d u0 {2,D}
2   P5d u0 {1,D}
""",
	solute = SoluteData(
		S = 0.00892,
		B = 0.11892,
		E = 0.28230,
		L = 0.97685,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 12,
		B = 12,
		E = 12,
		L = 12,
		A = 18,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 812,
	label = "S2s",
	group = 
"""
1 * S2s u0
""",
	solute = u'S2s-CC',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 813,
	label = "S2s-CH",
	group = 
"""
1 * S2s u0 {2,S} {3,S}
2   C  u0 {1,S}
3   H  u0 {1,S}
""",
	solute = u'S2s-CsH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 814,
	label = "S2s-CsH",
	group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cs u0 {1,S}
3   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.20433,
		B = 0.14840,
		E = 0.22845,
		L = 0.91094,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 37,
		B = 37,
		E = 38,
		L = 37,
		A = 38,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 815,
	label = "S2s-CdH",
	group = 
"""
1 * S2s u0 {2,S} {3,S}
2   [Cd,CO,CS] u0 {1,S}
3   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.07884,
		B = 0.04018,
		E = 0.20570,
		L = 0.63132,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 4,
		L = 3,
		A = 3,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 816,
	label = "S2s-CbH",
	group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cb u0 {1,S}
3   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.15673,
		B = -0.01553,
		E = 0.21099,
		L = 0.65357,
		A = 0.05171,
	),
	dataCount = DataCountGAV(
		S = 12,
		B = 12,
		E = 14,
		L = 11,
		A = 12,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 817,
	label = "S2s-PH",
	group = 
"""
1 * S2s u0 {2,S} {3,S}
2   P   u0 {1,S}
3   H   u0 {1,S}
""",
	solute = u'S2s-P5dH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 818,
	label = "S2s-P5dH",
	group = 
"""
1 * S2s u0 {2,S} {3,S}
2   P5d u0 {1,S}
3   H  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.06826,
		B = 0.11157,
		E = 0.15133,
		L = 0.50523,
		A = 0.00400,
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
	index = 819,
	label = "S2s-PC",
	group = 
"""
1 * S2s u0 {2,S} {3,S}
2   P   u0 {1,S}
3   C  u0 {1,S}
""",
	solute = u'S2s-P5dC',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 820,
	label = "S2s-P5dC",
	group = 
"""
1 * S2s u0 {2,S} {3,S}
2   P5d u0 {1,S}
3   C  u0 {1,S}
""",
	solute = SoluteData(
		S = -0.08248,
		B = 0.04760,
		E = 0.11772,
		L = 0.46096,
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
	index = 821,
	label = "S2s-SS",
	group = 
"""
1 * S2s u0 {2,S} {3,S}
2   S ux {1,S}
3   S ux {1,S}
""",
	solute = u'S2s-SsSs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 822,
	label = "S2s-SsSs",
	group = 
"""
1 * S2s u0 {2,S} {3,S}
2   S2s u0 {1,S}
3   S2s u0 {1,S}
""",
	solute = SoluteData(
		S = 0.09209,
		B = 0.00000,
		E = 0.23549,
		L = 0.86175,
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
	index = 823,
	label = "S2s-SC",
	group = 
"""
1 * S2s u0 {2,S} {3,S}
2   S ux {1,S}
3   C ux {1,S}
""",
	solute = u'S2s-S2sC',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 824,
	label = "S2s-S2sC",
	group = 
"""
1 * S2s u0 {2,S} {3,S}
2   S2s u0 {1,S}
3   C  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.13828,
		B = 0.07058,
		E = 0.22146,
		L = 0.96626,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 22,
		B = 22,
		E = 26,
		L = 22,
		A = 26,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 825,
	label = "S2s-S46C",
	group = 
"""
1 * S2s u0 {2,S} {3,S}
2   [S4s,S4d,S4b,S4t,S6d,S6dd,S6t,S6td] u0 {1,S}
3   C  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.07094,
		B = 0.04064,
		E = 0.09107,
		L = 0.42457,
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
	index = 826,
	label = "S2s-NN",
	group = 
"""
1 * S2s u0 {2,S} {3,S}
2   N  u0 {1,S}
3   N  u0 {1,S}
""",
	solute = u'S2s-N3dN3d',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 827,
	label = "S2s-N3dN3d",
	group = 
"""
1 * S2s u0 {2,S} {3,S}
2   N3d u0 {1,S}
3   N3d u0 {1,S}
""",
	solute = SoluteData(
		S = 0.13479,
		B = 0.00827,
		E = 0.12936,
		L = 0.55934,
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
	index = 828,
	label = "S2s-NC",
	group = 
"""
1 * S2s u0 {2,S} {3,S}
2   N   u0 {1,S}
3   C   u0 {1,S}
""",
	solute = u'S2s-N3dCd',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 829,
	label = "S2s-N3dCd",
	group = 
"""
1 * S2s u0 {2,S} {3,S}
2   N3d u0 {1,S}
3   Cd  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.01319,
		B = 0.04536,
		E = 0.16479,
		L = 0.43630,
		A = 0.04705,
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
	index = 830,
	label = "S2s-CC",
	group = 
"""
1 * S2s u0 {2,S} {3,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
""",
	solute = u'S2s-CsCs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 831,
	label = "S2s-CsCs",
	group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
""",
	solute = SoluteData(
		S = 0.10492,
		B = 0.20161,
		E = 0.13510,
		L = 0.98477,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 103,
		B = 103,
		E = 115,
		L = 102,
		A = 117,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 832,
	label = "S2rs-CrsCrs",
	group = 
"""
1 * S2s u0 r1 {2,S} {3,S}
2   Cs u0 r1 {1,S}
3   Cs u0 r1 {1,S}
""",
	solute = SoluteData(
		S = 0.03907,
		B = 0.11774,
		E = 0.28209,
		L = 0.73745,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 34,
		B = 33,
		E = 37,
		L = 33,
		A = 38,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 833,
	label = "S2s-CsCd",
	group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cs u0 {1,S}
3   Cd u0 {1,S}
""",
	solute = SoluteData(
		S = 0.12528,
		B = 0.00405,
		E = 0.17226,
		L = 0.75873,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 37,
		B = 37,
		E = 37,
		L = 37,
		A = 37,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 834,
	label = "S2s-Cs(C=O)",
	group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cs u0 {1,S}
3   CO u0 {1,S} {4,D}
4   O2d u0 {3,D}
""",
	solute = SoluteData(
		S = -0.00137,
		B = 0.06030,
		E = 0.10865,
		L = 0.34031,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 8,
		B = 7,
		E = 10,
		L = 6,
		A = 10,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 835,
	label = "S2s-CsCt",
	group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cs u0 {1,S}
3   Ct u0 {1,S}
""",
	solute = SoluteData(
		S = 0.03527,
		B = 0.05057,
		E = 0.03588,
		L = 0.11695,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 6,
		E = 6,
		L = 2,
		A = 9,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 836,
	label = "S2s-CsCb",
	group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cs u0 {1,S}
3   Cb u0 {1,S}
""",
	solute = SoluteData(
		S = 0.03852,
		B = 0.06047,
		E = 0.14117,
		L = 0.62914,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 6,
		B = 6,
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
	index = 837,
	label = "S2s-CdCd",
	group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cd u0 {1,S}
3   Cd u0 {1,S}
""",
	solute = u'S2rs-CrdCrd',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 838,
	label = "S2rs-CrdCrd",
	group = 
"""
1 * S2s u0 r1 {2,S} {3,S}
2   Cd u0 r1 {1,S}
3   Cd u0 r1 {1,S}
""",
	solute = SoluteData(
		S = 0.10206,
		B = 0.09010,
		E = 0.14351,
		L = 0.76630,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 53,
		B = 52,
		E = 62,
		L = 47,
		A = 59,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 839,
	label = "S2s-CdCb",
	group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cd u0 {1,S}
3   Cb u0 {1,S}
""",
	solute = u'S2rs-CrdCb',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 840,
	label = "S2rs-CrdCb",
	group = 
"""
1 * S2s u0 r1 {2,S} {3,S}
2   Cd u0 r1 {1,S}
3   Cb u0 {1,S}
""",
	solute = SoluteData(
		S = 0.06070,
		B = 0.02407,
		E = 0.08802,
		L = 0.42914,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 52,
		B = 52,
		E = 55,
		L = 53,
		A = 55,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 841,
	label = "S2s-CtCb",
	group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Ct u0 {1,S}
3   Cb u0 {1,S}
""",
	solute = u'S2s-(Ct-N3t)Cb',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 842,
	label = "S2s-(Ct-N3t)Cb",
	group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Ct u0 {1,S} {4,T}
3   Cb u0 {1,S}
4   N3t u0 {2,T}
""",
	solute = SoluteData(
		S = 0.00882,
		B = -0.02539,
		E = 0.03334,
		L = 0.04878,
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
	index = 843,
	label = "S2s-CbCb",
	group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
""",
	solute = SoluteData(
		S = -0.01084,
		B = 0.00402,
		E = 0.03885,
		L = 0.14034,
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
	index = 844,
	label = "S2rs-CbCb",
	group = 
"""
1 * S2s u0 r1 {2,S} {3,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
""",
	solute = SoluteData(
		S = 0.01785,
		B = -0.00037,
		E = 0.02261,
		L = 0.07159,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 74,
		B = 74,
		E = 74,
		L = 72,
		A = 74,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 845,
	label = "S2s-(Cd-S2d)C",
	group = 
"""
1 * S2s u0 {2,S} {3,S}
2   C  u0 {1,S}
3   CS u0 {1,S} {4,D}
4   S2d u0 {3,D}
""",
	solute = SoluteData(
		S = 0.10426,
		B = -0.03720,
		E = 0.12059,
		L = 0.60369,
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
	index = 846,
	label = "S4dd",
	group = 
"""
1 * S4dd  u0
""",
	solute = u'S4dd-N3dN3d',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 847,
	label = "S4dd-N3dN3d",
	group = 
"""
1 * S4dd  u0 {2,D} {3,D}
2   N3d   u0 {1,D}
3   N3d   u0 {1,D}
""",
	solute = SoluteData(
		S = 0.09129,
		B = 0.01073,
		E = 0.11589,
		L = 0.42640,
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
	index = 848,
	label = "S4d",
	group = 
"""
1 * S4d  u0
""",
	solute = u'S4d-Od',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 849,
	label = "S4d-Od",
	group = 
"""
1 * S4d u0 p1 {2,D}
2   O2d ux    {1,D}
""",
	solute = u'S4d-OdCC',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 850,
	label = "S4d-OdCC",
	group = 
"""
1 * S4d  u0 p1 {2,D} {3,S} {4,S}
2   O2d  u0 {1,D}
3   C    ux (1,S)
4   C    ux (1,S)
""",
	solute = u'S4d-OdCsCs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 851,
	label = "S4d-OdCsCs",
	group = 
"""
1 * S4d  u0 p1 {2,D} {3,S} {4,S}
2   O2d  u0 {1,D}
3   Cs    ux (1,S)
4   Cs    ux (1,S)
""",
	solute = SoluteData(
		S = 0.26069,
		B = 0.17376,
		E = 0.07036,
		L = 0.60651,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 14,
		B = 11,
		E = 17,
		L = 11,
		A = 27,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 852,
	label = "S4d-OdCsCb",
	group = 
"""
1 * S4d  u0 p1 {2,D} {3,S} {4,S}
2   O2d  u0 {1,D}
3   Cs    ux (1,S)
4   Cb    ux (1,S)
""",
	solute = SoluteData(
		S = 0.09387,
		B = 0.07349,
		E = 0.08040,
		L = 0.40789,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 10,
		B = 10,
		E = 11,
		L = 10,
		A = 12,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 853,
	label = "S4d-OdCbCb",
	group = 
"""
1 * S4d  u0 p1 {2,D} {3,S} {4,S}
2   O2d  u0 {1,D}
3   Cb    ux (1,S)
4   Cb    ux (1,S)
""",
	solute = SoluteData(
		S = 0.00720,
		B = 0.03214,
		E = 0.01226,
		L = 0.06491,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 1,
		B = 1,
		E = 1,
		L = 1,
		A = 3,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 854,
	label = "S4d-OdCS",
	group = 
"""
1 * S4d  u0 p1 {2,D} {3,S} {4,S}
2   O2d  ux {1,D}
3   C    ux (1,S)
4   S    ux (1,S)
""",
	solute = SoluteData(
		S = 0.07094,
		B = 0.04064,
		E = 0.09107,
		L = 0.42457,
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
	index = 855,
	label = "S6dd",
	group = 
"""
1 * S6dd   u0
""",
	solute = u'S6dd-OdOd',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 856,
	label = "S6dd-OdOd",
	group = 
"""
1 * S6dd u0 p0 {2,D} {3,D}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
""",
	solute = u'S6dd-OdOdCC',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 857,
	label = "S6dd-OdOdCC",
	group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
4   C    ux {1,S}
5   C    ux {1,S}
""",
	solute = u'S6dd-OdOdCbCb',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 858,
	label = "S6dd-OdOdCbCb",
	group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
4   Cb   ux {1,S}
5   Cb   ux {1,S}
""",
	solute = SoluteData(
		S = -0.02950,
		B = -0.05186,
		E = 0.03957,
		L = 0.11171,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 20,
		B = 20,
		E = 23,
		L = 20,
		A = 21,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 859,
	label = "S6dd-OdOdCrCr",
	group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
4   C    ux r1 {1,S}
5   C    ux r1 {1,S}
""",
	solute = SoluteData(
		S = 0.01709,
		B = -0.05985,
		E = -0.06581,
		L = -0.15529,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 3,
		L = 3,
		A = 3,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 860,
	label = "S6dd-OdOdCsCs",
	group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
4   Cs   ux {1,S}
5   Cs   ux {1,S}
""",
	solute = SoluteData(
		S = 0.00384,
		B = 0.00127,
		E = -0.01552,
		L = 0.13681,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 11,
		B = 10,
		E = 11,
		L = 3,
		A = 12,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 861,
	label = "S6dd-OdOdCsCb",
	group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
4   Cs   ux {1,S}
5   Cb   ux {1,S}
""",
	solute = SoluteData(
		S = 0.01274,
		B = 0.01130,
		E = -0.00722,
		L = -0.01918,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 19,
		B = 18,
		E = 19,
		L = 13,
		A = 19,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 862,
	label = "S6dd-OdOdCO",
	group = 
"""
1 * S6dd    u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d     ux {1,D}
3   O2d     ux {1,D}
4   C       ux {1,S}
5   O       ux {1,S}
""",
	solute = u'S6dd-OdOdCbOs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 863,
	label = "S6dd-OdOdCsOs",
	group = 
"""
1 * S6dd    u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d     ux {1,D}
3   O2d     ux {1,D}
4   Cs      ux {1,S}
5   O       ux {1,S}
""",
	solute = SoluteData(
		S = -0.00703,
		B = 0.17261,
		E = -0.04891,
		L = -0.07132,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
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
	index = 864,
	label = "S6dd-OdOdCbOs",
	group = 
"""
1 * S6dd    u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d     ux {1,D}
3   O2d     ux {1,D}
4   Cb      ux {1,S}
5   O       ux {1,S}
""",
	solute = SoluteData(
		S = 0.19517,
		B = 0.03231,
		E = -0.05921,
		L = 0.10478,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 4,
		B = 4,
		E = 7,
		L = 4,
		A = 6,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 865,
	label = "S6dd-OdOdNC",
	group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
4   N    ux {1,S}
5   C    ux {1,S}
""",
	solute = SoluteData(
		S = 0.01653,
		B = -0.06708,
		E = 0.13698,
		L = 0.13786,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 12,
		B = 12,
		E = 15,
		L = 11,
		A = 13,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 866,
	label = "S6dd-OdOdNCb",
	group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
4   N    ux {1,S}
5   Cb   ux {1,S}
""",
	solute = SoluteData(
		S = -0.03298,
		B = 0.07459,
		E = 0.10086,
		L = 0.22322,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 110,
		B = 110,
		E = 112,
		L = 104,
		A = 111,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 867,
	label = "S6dd-OdOdNN",
	group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
4   N    ux {1,S}
5   N    ux {1,S}
""",
	solute = u'S6dd-OdOdNC',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 868,
	label = "S6dd-OdOdOO",
	group = 
"""
1 * S6dd    u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d     ux {1,D}
3   O2d     ux {1,D}
4   O       ux {1,S}
5   O       ux {1,S}
""",
	solute = SoluteData(
		S = 0.05247,
		B = 0.02515,
		E = -0.05111,
		L = 0.09171,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
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
	index = 869,
	label = "S6dd-OdOdON",
	group = 
"""
1 * S6dd    u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d     ux {1,D}
3   O2d     ux {1,D}
4   O       ux {1,S}
5   N       ux {1,S}
""",
	solute = SoluteData(
		S = -0.01816,
		B = -0.01970,
		E = 0.03722,
		L = 0.03131,
		A = 0.00413,
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
	index = 870,
	label = "N",
	group = 
"""
1 * N u0
""",
	solute = u'N3s',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 871,
	label = "N1dc",
	group = 
"""
1 * N1dc u0 p2 {2,D}
2   R!H ux px {1,D}
""",
	solute = u'N1dc-N5ddc',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 872,
	label = "N1dc-N5ddc",
	group = 
"""
1 * N1dc u0 p2 {2,D}
2   N5ddc u0 px {1,D}
""",
	solute = SoluteData(
		S = 0.04468,
		B = 0.00000,
		E = 0.09588,
		L = 0.39946,
		A = 0.01261,
	),
	dataCount = DataCountGAV(
		S = 9,
		B = 9,
		E = 9,
		L = 9,
		A = 9,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 873,
	label = "N3s",
	group = 
"""
1 * N3s u0
""",
	solute = u'N3s-CCH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 874,
	label = "N3s-CHH",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   C   u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
	solute = u'N3s-CsHH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 875,
	label = "N3s-CsHH",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.27024,
		B = 0.38829,
		E = 0.16260,
		L = 0.62432,
		A = 0.17304,
	),
	dataCount = DataCountGAV(
		S = 91,
		B = 91,
		E = 96,
		L = 80,
		A = 92,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 876,
	label = "N3s-CrsHH",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cs  u0 r1 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.24468,
		B = 0.12098,
		E = 0.17885,
		L = 0.57256,
		A = 0.12840,
	),
	dataCount = DataCountGAV(
		S = 15,
		B = 15,
		E = 17,
		L = 15,
		A = 15,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 877,
	label = "N3s-CbHH",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cb  u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.40793,
		B = 0.16116,
		E = 0.22723,
		L = 0.66930,
		A = 0.23902,
	),
	dataCount = DataCountGAV(
		S = 247,
		B = 229,
		E = 257,
		L = 204,
		A = 248,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 878,
	label = "N3s-CdHH",
	group = 
"""
1 * N3s         u0 {2,S} {3,S} {4,S}
2   [Cd,CO,CS]  u0 {1,S}
3   H           u0 {1,S}
4   H           u0 {1,S}
""",
	solute = u'N3s-(Cd-O2d)HH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 879,
	label = "N3s-(Cd-Cd)HH",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   C   u0 {2,D}
""",
	solute = u'N3s-(Crd-Crd)HH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 880,
	label = "N3s-(Crd-Crd)HH",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cd  u0 r1 {1,S} {5,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   C   u0 r1 {2,D}
""",
	solute = SoluteData(
		S = 0.18972,
		B = 0.14751,
		E = 0.22157,
		L = 0.66050,
		A = 0.25898,
	),
	dataCount = DataCountGAV(
		S = 16,
		B = 16,
		E = 16,
		L = 14,
		A = 18,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 881,
	label = "N3s-(Cd-N3d)HH",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   N3d u0 {2,D}
""",
	solute = SoluteData(
		S = 0.19084,
		B = 0.22975,
		E = 0.23095,
		L = 0.95739,
		A = 0.13806,
	),
	dataCount = DataCountGAV(
		S = 26,
		B = 26,
		E = 27,
		L = 23,
		A = 26,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 882,
	label = "N3s-(Crd-N3rd)HH",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cd  u0 r1 {1,S} {5,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   N3d u0 r1 {2,D}
""",
	solute = SoluteData(
		S = 0.23348,
		B = 0.21851,
		E = 0.27122,
		L = 0.79503,
		A = 0.20872,
	),
	dataCount = DataCountGAV(
		S = 36,
		B = 31,
		E = 36,
		L = 29,
		A = 36,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 883,
	label = "N3s-(Cd-O2d)HH",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   O2d u0 {2,D}
""",
	solute = SoluteData(
		S = 0.41631,
		B = 0.18885,
		E = 0.15875,
		L = 0.77742,
		A = 0.39827,
	),
	dataCount = DataCountGAV(
		S = 136,
		B = 130,
		E = 142,
		L = 101,
		A = 138,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 884,
	label = "N3s-(Cd-Sd)HH",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   CS  u0 {1,S} {5,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   S   u0 {2,D}
""",
	solute = SoluteData(
		S = 0.12045,
		B = 0.20854,
		E = 0.09545,
		L = 0.34140,
		A = 0.23923,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 5,
		E = 5,
		L = 4,
		A = 5,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 885,
	label = "N3s-NHH",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   N   u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
	solute = u'N3s-N3sHH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 886,
	label = "N3s-N3sHH",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   H   u0 {1,S}
3   H   u0 {1,S}
4   N3s u0 {1,S}
""",
	solute = SoluteData(
		S = 0.11956,
		B = 0.11078,
		E = 0.18172,
		L = 0.60495,
		A = 0.08925,
	),
	dataCount = DataCountGAV(
		S = 6,
		B = 6,
		E = 8,
		L = 6,
		A = 6,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 887,
	label = "N3s-SHH",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   S   u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
	solute = u'N3s-S6ddHH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 888,
	label = "N3s-S6ddHH",
	group = 
"""
1 * N3s  u0 {2,S} {3,S} {4,S}
2   S6dd u0 {1,S}
3   H    u0 {1,S}
4   H    u0 {1,S}
""",
	solute = SoluteData(
		S = 0.07498,
		B = 0.14653,
		E = 0.14577,
		L = 0.33390,
		A = 0.48818,
	),
	dataCount = DataCountGAV(
		S = 61,
		B = 61,
		E = 63,
		L = 60,
		A = 61,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 889,
	label = "N3s-NNH",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   N   u0 {1,S}
3   N   u0 {1,S}
4   H   u0 {1,S}
""",
	solute = u'N3rs-N3rd(Crd-Nd)H',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 890,
	label = "N3s-PCH",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   P   u0 {1,S}
3   C   u0 {1,S}
4   H   u0 {1,S}
""",
	solute = u'N3s-P5dCH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 891,
	label = "N3s-P5dCH",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   P5d u0 {1,S}
3   C   u0 {1,S}
4   H   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.15712,
		B = 0.07240,
		E = -0.00694,
		L = 0.43741,
		A = 0.13478,
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
	index = 892,
	label = "N3s-NCH",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   N   u0 {1,S}
3   C   u0 {1,S}
4   H   u0 {1,S}
""",
	solute = u'N3s-N3dCdH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 893,
	label = "N3s-N3sCsH",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   H   u0 {1,S}
4   N3s u0 {1,S}
""",
	solute = SoluteData(
		S = 0.01408,
		B = 0.09226,
		E = 0.08007,
		L = 0.19320,
		A = 0.03846,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
		E = 4,
		L = 2,
		A = 2,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 894,
	label = "N3s-N3sCbH",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   N3s u0 {1,S}
3   Cb  u0 {1,S}
4   H   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.04221,
		B = 0.10686,
		E = 0.11535,
		L = 0.29088,
		A = 0.08564,
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
	index = 895,
	label = "N3s-N3sCdH",
	group = 
"""
1 * N3s         u0 {2,S} {3,S} {4,S}
2   N3s         u0 {1,S}
3   [Cd,CO,CS]  u0 {1,S}
4   H           u0 {1,S}
""",
	solute = SoluteData(
		S = 0.27252,
		B = 0.07462,
		E = 0.11966,
		L = 0.68556,
		A = 0.17297,
	),
	dataCount = DataCountGAV(
		S = 9,
		B = 9,
		E = 10,
		L = 9,
		A = 9,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 896,
	label = "N3s-N3dCsH",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   N3d u0 {1,S}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
""",
	solute = u'N3rs-N3rd(Crd-Cd)H',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 897,
	label = "N3s-N3dCbH",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   N3d u0 {1,S}
3   Cb  u0 {1,S}
4   H   u0 {1,S}
""",
	solute = SoluteData(
		S = -0.03080,
		B = -0.09369,
		E = 0.00180,
		L = 0.01489,
		A = 0.29556,
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
	index = 898,
	label = "N3s-N3dCdH",
	group = 
"""
1 * N3s         u0 {2,S} {3,S} {4,S}
2   N3d         u0 {1,S}
3   [Cd,CO,CS]  u0 {1,S}
4   H           u0 {1,S}
""",
	solute = u'N3s-N3d(Cd-O2d)H',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 899,
	label = "N3rs-N3rdCrdH",
	group = 
"""
1 * N3s         u0 r1 {2,S} {3,S} {4,S}
2   N3d         u0 r1 {1,S}
3   [Cd,CO,CS]  u0 r1 {1,S}
4   H           u0 {1,S}
""",
	solute = u'N3rs-N3rd(Crd-O2d)H',
	dataCount = None,
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 900,
	label = "N3rs-N3rd(Crd-O2d)H",
	group = 
"""
1 * N3s         u0 r1 {2,S} {3,S} {4,S}
2   N3d         u0 r1 {1,S}
3   CO          u0 r1 {1,S}
4   H           u0 {1,S}
""",
	solute = SoluteData(
		S = 0.00530,
		B = 0.02004,
		E = -0.02931,
		L = -0.06992,
		A = 0.07756,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 4,
		L = 3,
		A = 3,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 901,
	label = "N3rs-N3rd(Crd-Cd)H",
	group = 
"""
1 * N3s         u0 r1 {2,S} {3,S} {4,S}
2   N3d         u0 r1 {1,S}
3   Cd          u0 r1 {1,S} {5,D}
4   H           u0 {1,S}
5   C           u0 {3,D}
""",
	solute = SoluteData(
		S = 0.14290,
		B = -0.00247,
		E = 0.05898,
		L = 0.32090,
		A = 0.33960,
	),
	dataCount = DataCountGAV(
		S = 7,
		B = 3,
		E = 8,
		L = 6,
		A = 7,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 902,
	label = "N3rs-N3rd(Crd-Nd)H",
	group = 
"""
1 * N3s         u0 r1 {2,S} {3,S} {4,S}
2   N3d         u0 r1 {1,S}
3   Cd          u0 r1 {1,S} {5,D}
4   H           u0 {1,S}
5   N           u0 {3,D}
""",
	solute = SoluteData(
		S = 0.13665,
		B = 0.09966,
		E = 0.01480,
		L = 0.30183,
		A = 0.35445,
	),
	dataCount = DataCountGAV(
		S = 8,
		B = 8,
		E = 8,
		L = 8,
		A = 8,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 903,
	label = "N3s-N3d(Cd-O2d)H",
	group = 
"""
1 * N3s         u0 {2,S} {3,S} {4,S}
2   N3d         u0 {1,S}
3   CO          u0 {1,S}
4   H           u0 {1,S}
""",
	solute = SoluteData(
		S = 0.03639,
		B = 0.03215,
		E = -0.04736,
		L = 0.34880,
		A = 0.09983,
	),
	dataCount = DataCountGAV(
		S = 32,
		B = 32,
		E = 32,
		L = 32,
		A = 32,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 904,
	label = "N3s-PCC",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   P   u0 {1,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
""",
	solute = SoluteData(
		S = -0.03784,
		B = 0.05012,
		E = -0.01946,
		L = 0.11493,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 1,
		B = 1,
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
	index = 905,
	label = "N3s-NCC",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   N   u0 {1,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
""",
	solute = u'N3s-N3dCC',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 906,
	label = "N3rs-NrCrCr",
	group = 
"""
1 * N3s u0 r1 {2,S} {3,S} {4,S}
2   N   u0 r1 {1,S}
3   C   u0 r1 {1,S}
4   C   u0 r1 {1,S}
""",
	solute = SoluteData(
		S = -0.03717,
		B = 0.08658,
		E = 0.09925,
		L = 0.23346,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 5,
		E = 5,
		L = 4,
		A = 5,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 907,
	label = "N3rs-NrCrCb",
	group = 
"""
1 * N3s u0 r1 {2,S} {3,S} {4,S}
2   N   u0 r1 {1,S}
3   C   u0 r1 {1,S}
4   Cb  u0 r1 {1,S}
""",
	solute = SoluteData(
		S = -0.08888,
		B = 0.07249,
		E = 0.07750,
		L = 0.02129,
		A = 0.04929,
	),
	dataCount = DataCountGAV(
		S = 4,
		B = 4,
		E = 4,
		L = 4,
		A = 4,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 908,
	label = "N3rs-Nr(Crd-O2d)Cb",
	group = 
"""
1 * N3s u0 r1 {2,S} {3,S} {4,S}
2   N   u0 r1 {1,S}
3   CO  u0 r1 {1,S}
4   Cb  u0 r1 {1,S}
""",
	solute = SoluteData(
		S = -0.08027,
		B = 0.09826,
		E = -0.00320,
		L = 0.06777,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 20,
		B = 20,
		E = 20,
		L = 19,
		A = 20,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 909,
	label = "N3rs-NrCrC",
	group = 
"""
1 * N3s u0 r1 {2,S} {3,S} {4,S}
2   N   u0 r1 {1,S}
3   C   u0 r1 {1,S}
4   C   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.08102,
		B = -0.03932,
		E = 0.10687,
		L = 0.25252,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 44,
		B = 44,
		E = 45,
		L = 37,
		A = 45,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 910,
	label = "N3rs-NCrCr",
	group = 
"""
1 * N3s u0 r1 {2,S} {3,S} {4,S}
2   N   u0 {1,S}
3   C   u0 r1 {1,S}
4   C   u0 r1 {1,S}
""",
	solute = u'N3rs-N3dCrCr',
	dataCount = None,
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 911,
	label = "N3rs-N3dCrCr",
	group = 
"""
1 * N3s u0 r1 {2,S} {3,S} {4,S}
2   N3d u0 {1,S}
3   C   u0 r1 {1,S}
4   C   u0 r1 {1,S}
""",
	solute = SoluteData(
		S = 0.07205,
		B = 0.15034,
		E = 0.10428,
		L = 0.33714,
		A = 0.06027,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 5,
		E = 5,
		L = 5,
		A = 5,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 912,
	label = "N3rs-(N3d-O2d)CrCr",
	group = 
"""
1 * N3s u0 r1 {2,S} {3,S} {4,S}
2   N3d u0 {1,S} {5,D}
3   C   u0 r1 {1,S}
4   C   u0 r1 {1,S}
5   O2d u0 {2,D}
""",
	solute = SoluteData(
		S = 0.04914,
		B = 0.01674,
		E = 0.00120,
		L = 0.03106,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 8,
		B = 8,
		E = 8,
		L = 8,
		A = 8,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 913,
	label = "N3rs-N5dcCrCr",
	group = 
"""
1 * N3s u0 r1 {2,S} {3,S} {4,S}
2   N5dc u0 {1,S}
3   C   u0 r1 {1,S}
4   C   u0 r1 {1,S}
""",
	solute = SoluteData(
		S = 0.02675,
		B = -0.01251,
		E = -0.04143,
		L = 0.21473,
		A = 0.07466,
	),
	dataCount = DataCountGAV(
		S = 4,
		B = 4,
		E = 4,
		L = 4,
		A = 4,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 914,
	label = "N3s-N3dCC",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   N3d u0 {1,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
""",
	solute = u'N3s-(N3d-O2d)CC',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 915,
	label = "N3s-(N3d-O2d)CC",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   N3d u0 {1,S} {5,D}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   O2d u0 {2,D}
""",
	solute = SoluteData(
		S = -0.00575,
		B = -0.05818,
		E = -0.01779,
		L = 0.12028,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 4,
		B = 4,
		E = 7,
		L = 4,
		A = 4,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 916,
	label = "N3s-(N3d-O2d)CsCs",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   N3d u0 {1,S} {5,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   O2d u0 {2,D}
""",
	solute = SoluteData(
		S = 0.16578,
		B = 0.12560,
		E = -0.02665,
		L = 0.18833,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 26,
		B = 26,
		E = 26,
		L = 26,
		A = 26,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 917,
	label = "N3s-(N3d-O2d)CbCs",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   N3d u0 {1,S} {5,D}
3   Cb  u0 {1,S}
4   Cs  u0 {1,S}
5   O2d u0 {2,D}
""",
	solute = SoluteData(
		S = 0.01769,
		B = -0.00720,
		E = 0.03744,
		L = 0.06381,
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
	index = 918,
	label = "N3s-(N3d-O2d)CbCb",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   N3d u0 {1,S} {5,D}
3   Cb  u0 {1,S}
4   Cb  u0 {1,S}
5   O2d u0 {2,D}
""",
	solute = SoluteData(
		S = -0.00886,
		B = -0.00973,
		E = 0.03658,
		L = -0.05446,
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
	index = 919,
	label = "N3s-NNC",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   N   u0 {1,S}
3   N   u0 {1,S}
4   C   u0 {1,S}
""",
	solute = u'N3rs-NrNrC',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 920,
	label = "N3rs-NrNrC",
	group = 
"""
1 * N3s u0 r1 {2,S} {3,S} {4,S}
2   N   u0 r1 {1,S}
3   N   u0 r1 {1,S}
4   C   u0 {1,S}
""",
	solute = u'N3rs-NrCrC',
	dataCount = None,
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 921,
	label = "N3s-NNO",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   N   u0 {1,S}
3   N   u0 {1,S}
4   O   u0 {1,S}
""",
	solute = u'N3rs-NrNrO',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 922,
	label = "N3rs-NrNrO",
	group = 
"""
1 * N3s u0 r1 {2,S} {3,S} {4,S}
2   N   u0 r1 {1,S}
3   N   u0 r1 {1,S}
4   O   u0 {1,S}
""",
	solute = u'N3rs-N3rdN3rdO',
	dataCount = None,
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 923,
	label = "N3rs-N3rdN3rdO",
	group = 
"""
1 * N3s u0 r1 {2,S} {3,S} {4,S}
2   N3d  u0 r1 {1,S}
3   N3d u0 r1 {1,S}
4   O   u0 {1,S}
""",
	solute = u'N3rs-N3rdN3rd(O2s-H)',
	dataCount = None,
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 924,
	label = "N3rs-N3rdN3rd(O2s-H)",
	group = 
"""
1 * N3s u0 r1 {2,S} {3,S} {4,S}
2   N3d  u0 r1 {1,S}
3   N3d u0 r1 {1,S}
4   O2s  u0 {1,S} {5,S}
5   H    u0 {4,S}
""",
	solute = SoluteData(
		S = 0.04824,
		B = 0.02361,
		E = 0.04882,
		L = 0.06663,
		A = 0.10381,
	),
	dataCount = DataCountGAV(
		S = 1,
		B = 1,
		E = 1,
		L = 1,
		A = 1,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 925,
	label = "N3s-CCH",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
4   H   u0 {1,S}
""",
	solute = u'N3s-CsCsH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 926,
	label = "N3s-CsCsH",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
""",
	solute = SoluteData(
		S = -0.01402,
		B = 0.25997,
		E = 0.03900,
		L = 0.38134,
		A = 0.07343,
	),
	dataCount = DataCountGAV(
		S = 107,
		B = 106,
		E = 110,
		L = 99,
		A = 108,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 927,
	label = "N3rs-CrsCrsH",
	group = 
"""
1 * N3s u0 r1 {2,S} {3,S} {4,S}
2   Cs  u0 r1 {1,S}
3   Cs  u0 r1 {1,S}
4   H   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.10419,
		B = 0.22632,
		E = 0.06021,
		L = 0.17752,
		A = 0.11482,
	),
	dataCount = DataCountGAV(
		S = 38,
		B = 38,
		E = 39,
		L = 36,
		A = 38,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 928,
	label = "N3s-CbCsH",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cb  u0 {1,S}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.10569,
		B = -0.01570,
		E = 0.12734,
		L = 0.29768,
		A = 0.08713,
	),
	dataCount = DataCountGAV(
		S = 24,
		B = 15,
		E = 29,
		L = 24,
		A = 30,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 929,
	label = "N3rs-CbCrsH",
	group = 
"""
1 * N3s u0 r1 {2,S} {3,S} {4,S}
2   Cb  u0 {1,S}
3   Cs  u0 r1 {1,S}
4   H   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.10132,
		B = 0.03747,
		E = 0.11831,
		L = 0.09311,
		A = 0.16283,
	),
	dataCount = DataCountGAV(
		S = 9,
		B = 7,
		E = 9,
		L = 9,
		A = 9,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 930,
	label = "N3s-CbCbH",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cb  u0 {1,S}
3   Cb  u0 {1,S}
4   H   u0 {1,S}
""",
	solute = SoluteData(
		S = -0.04530,
		B = -0.09186,
		E = 0.01997,
		L = -0.02473,
		A = 0.05885,
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
	index = 931,
	label = "N3rs-CbCbH",
	group = 
"""
1 * N3s u0 r1 {2,S} {3,S} {4,S}
2   Cb  u0 {1,S}
3   Cb  u0 {1,S}
4   H   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.11689,
		B = -0.04208,
		E = -0.01174,
		L = 0.38988,
		A = 0.18917,
	),
	dataCount = DataCountGAV(
		S = 13,
		B = 13,
		E = 21,
		L = 20,
		A = 14,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 932,
	label = "N3s-CdCsH",
	group = 
"""
1 * N3s         u0 {2,S} {3,S} {4,S}
2   [Cd,CO,CS]  u0 {1,S}
3   Cs          u0 {1,S}
4   H           u0 {1,S}
""",
	solute = u'N3s-(Cd-O2d)CsH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 933,
	label = "N3s-(Cd-Cd)CsH",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   C   u0 {2,D}
""",
	solute = SoluteData(
		S = 0.09907,
		B = 0.11900,
		E = 0.09033,
		L = 0.63360,
		A = 0.15854,
	),
	dataCount = DataCountGAV(
		S = 10,
		B = 10,
		E = 11,
		L = 6,
		A = 10,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 934,
	label = "N3s-(Cd-N3d)CsH",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   N3d u0 {2,D}
""",
	solute = SoluteData(
		S = 0.10242,
		B = 0.09640,
		E = 0.10359,
		L = 0.45079,
		A = 0.12706,
	),
	dataCount = DataCountGAV(
		S = 39,
		B = 39,
		E = 40,
		L = 28,
		A = 39,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 935,
	label = "N3rs-(Crd-N3rd)CrsH",
	group = 
"""
1 * N3s u0 r1 {2,S} {3,S} {4,S}
2   Cd  u0 r1 {1,S} {5,D}
3   Cs  u0 r1 {1,S}
4   H   u0 {1,S}
5   N3d u0 r1 {2,D}
""",
	solute = SoluteData(
		S = 0.01547,
		B = 0.08380,
		E = 0.22463,
		L = 0.44209,
		A = 0.13765,
	),
	dataCount = DataCountGAV(
		S = 6,
		B = 7,
		E = 7,
		L = 7,
		A = 7,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 936,
	label = "N3s-(Cd-O2d)CsH",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   O2d u0 {2,D}
""",
	solute = SoluteData(
		S = 0.27531,
		B = 0.07844,
		E = 0.09529,
		L = 0.62625,
		A = 0.27168,
	),
	dataCount = DataCountGAV(
		S = 236,
		B = 235,
		E = 240,
		L = 196,
		A = 236,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 937,
	label = "N3s-(Cd-Sd)CsH",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   CS  u0 {1,S} {5,D}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   S   u0 {2,D}
""",
	solute = SoluteData(
		S = 0.07694,
		B = 0.09424,
		E = 0.05702,
		L = 0.25350,
		A = 0.13490,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 5,
		E = 5,
		L = 4,
		A = 5,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 938,
	label = "N3s-CdCtH",
	group = 
"""
1 * N3s         u0 {2,S} {3,S} {4,S}
2   [Cd,CO,CS]  u0 {1,S}
3   Ct          u0 {1,S}
4   H           u0 {1,S}
""",
	solute = u'N3s-(Cd-N3d)CtH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 939,
	label = "N3s-(Cd-N3d)CtH",
	group = 
"""
1 * N3s         u0 {2,S} {3,S} {4,S}
2   Cd          u0 {1,S} {5,D}
3   Ct          u0 {1,S}
4   H           u0 {1,S}
5   N3d         u0 {2,D}
""",
	solute = u'N3s-(Cd-N3d)(Ct-N3t)H',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 940,
	label = "N3s-(Cd-N3d)(Ct-N3t)H",
	group = 
"""
1 * N3s         u0 {2,S} {3,S} {4,S}
2   Cd          u0 {1,S} {5,D}
3   Ct          u0 {1,S} {6,T}
4   H           u0 {1,S}
5   N3d         u0 {2,D}
6   N3t         u0 {3,T}
""",
	solute = u'N3s-(Cd-N3d)CsH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 941,
	label = "N3s-CdCbH",
	group = 
"""
1 * N3s         u0 {2,S} {3,S} {4,S}
2   [Cd,CO,CS]  u0 {1,S}
3   Cb          u0 {1,S}
4   H           u0 {1,S}
""",
	solute = u'N3s-(Cd-O2d)CbH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 942,
	label = "N3s-(Cd-Cd)CbH",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cb  u0 {1,S}
4   H   u0 {1,S}
5   C   u0 {2,D}
""",
	solute = u'N3rs-(Crd-Crd)CbH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 943,
	label = "N3rs-(Crd-Crd)CbH",
	group = 
"""
1 * N3s u0 r1 {2,S} {3,S} {4,S}
2   Cd  u0 r1 {1,S} {5,D}
3   Cb  u0 {1,S}
4   H   u0 {1,S}
5   C   u0 r1 {2,D}
""",
	solute = SoluteData(
		S = 0.20364,
		B = -0.00534,
		E = 0.10404,
		L = 0.60136,
		A = 0.31193,
	),
	dataCount = DataCountGAV(
		S = 41,
		B = 33,
		E = 43,
		L = 41,
		A = 40,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 944,
	label = "N3s-(Crd-Crd)CbH",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cd  u0 r1 {1,S} {5,D}
3   Cb  u0 {1,S}
4   H   u0 {1,S}
5   C   u0 r1 {2,D}
""",
	solute = SoluteData(
		S = -0.05871,
		B = 0.11981,
		E = 0.04934,
		L = 0.39603,
		A = 0.15331,
	),
	dataCount = DataCountGAV(
		S = 6,
		B = 6,
		E = 6,
		L = 5,
		A = 6,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 945,
	label = "N3s-(Cd-N3d)CbH",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cb  u0 {1,S}
4   H   u0 {1,S}
5   N3d u0 {2,D}
""",
	solute = u'N3s-(Crd-N3rd)CbH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 946,
	label = "N3rs-(Crd-N3rd)CbH",
	group = 
"""
1 * N3s u0 r1 {2,S} {3,S} {4,S}
2   Cd  u0 r1 {1,S} {5,D}
3   Cb  u0 {1,S}
4   H   u0 {1,S}
5   N3d u0 r1 {2,D}
""",
	solute = SoluteData(
		S = 0.09927,
		B = -0.00303,
		E = 0.17548,
		L = 0.49401,
		A = 0.34952,
	),
	dataCount = DataCountGAV(
		S = 24,
		B = 24,
		E = 24,
		L = 22,
		A = 24,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 947,
	label = "N3s-(Crd-N3rd)CbH",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cd  u0 r1 {1,S} {5,D}
3   Cb  u0 {1,S}
4   H   u0 {1,S}
5   N3d u0 r1 {2,D}
""",
	solute = SoluteData(
		S = 0.00029,
		B = 0.09407,
		E = 0.09852,
		L = 0.21290,
		A = 0.08747,
	),
	dataCount = DataCountGAV(
		S = 13,
		B = 13,
		E = 14,
		L = 12,
		A = 13,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 948,
	label = "N3s-(Cd-O2d)CbH",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   Cb  u0 {1,S}
4   H   u0 {1,S}
5   O2d u0 {2,D}
""",
	solute = SoluteData(
		S = 0.02187,
		B = -0.00688,
		E = 0.00555,
		L = 0.07867,
		A = 0.35985,
	),
	dataCount = DataCountGAV(
		S = 165,
		B = 159,
		E = 168,
		L = 95,
		A = 164,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 949,
	label = "N3s-(Cd-Sd)CbH",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   CS  u0 {1,S} {5,D}
3   Cb  u0 {1,S}
4   H   u0 {1,S}
5   S   u0 {2,D}
""",
	solute = SoluteData(
		S = 0.15610,
		B = 0.09548,
		E = 0.00942,
		L = 0.31130,
		A = 0.20437,
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
	index = 950,
	label = "N3s-CdCdH",
	group = 
"""
1 * N3s         u0 {2,S} {3,S} {4,S}
2   [Cd,CO,CS]  u0 {1,S}
3   [Cd,CO,CS]  u0 {1,S}
4   H           u0 {1,S}
""",
	solute = u'N3s-(Cd-Cd)(Cd-Cd)H',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 951,
	label = "N3s-(Cd-Cd)(Cd-Cd)H",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   C   u0 {2,D}
6   C   u0 {3,D}
""",
	solute = u'N3rs-(Crd-Crd)(Crd-Crd)H',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 952,
	label = "N3rs-(Crd-Crd)(Crd-Crd)H",
	group = 
"""
1 * N3s u0 r1 {2,S} {3,S} {4,S}
2   Cd  u0 r1 {1,S} {5,D}
3   Cd  u0 r1 {1,S} {6,D}
4   H   u0 {1,S}
5   C   u0 r1 {2,D}
6   C   u0 r1 {3,D}
""",
	solute = SoluteData(
		S = 0.04822,
		B = -0.04175,
		E = 0.08125,
		L = 0.42451,
		A = 0.10480,
	),
	dataCount = DataCountGAV(
		S = 43,
		B = 43,
		E = 53,
		L = 39,
		A = 52,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 953,
	label = "N3s-(Cd-N3d)(Cd-Cd)H",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   N3d u0 {2,D}
6   C   u0 {3,D}
""",
	solute = u'N3rs-(Crd-N3rd)(Crd-Crd)H',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 954,
	label = "N3rs-(Crd-N3rd)(Crd-Crd)H",
	group = 
"""
1 * N3s u0 r1 {2,S} {3,S} {4,S}
2   Cd  u0 r1 {1,S} {5,D}
3   Cd  u0 r1 {1,S} {6,D}
4   H   u0 {1,S}
5   N3d u0 r1 {2,D}
6   C   u0 r1 {3,D}
""",
	solute = SoluteData(
		S = 0.11659,
		B = 0.05591,
		E = 0.09783,
		L = 0.30336,
		A = 0.36901,
	),
	dataCount = DataCountGAV(
		S = 30,
		B = 24,
		E = 32,
		L = 22,
		A = 31,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 955,
	label = "N3s-(Cd-O2d)(Cd-Cd)H",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   O2d u0 {2,D}
6   C   u0 {3,D}
""",
	solute = u'N3rs-(Crd-O2d)(Crd-Crd)H',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 956,
	label = "N3rs-(Crd-O2d)(Crd-Crd)H",
	group = 
"""
1 * N3s u0 r1 {2,S} {3,S} {4,S}
2   CO  u0 r1 {1,S} {5,D}
3   Cd  u0 r1 {1,S} {6,D}
4   H   u0 {1,S}
5   O2d u0 {2,D}
6   C   u0 r1 {3,D}
""",
	solute = SoluteData(
		S = 0.02212,
		B = 0.11893,
		E = 0.13108,
		L = 0.35857,
		A = 0.21888,
	),
	dataCount = DataCountGAV(
		S = 25,
		B = 24,
		E = 28,
		L = 23,
		A = 25,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 957,
	label = "N3s-(Cd-O2d)(Crd-Crd)H",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   Cd  u0 r1 {1,S} {6,D}
4   H   u0 {1,S}
5   O2d u0 {2,D}
6   C   u0 r1 {3,D}
""",
	solute = SoluteData(
		S = 0.03658,
		B = -0.01540,
		E = 0.05058,
		L = 0.31102,
		A = 0.06093,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 5,
		L = 3,
		A = 3,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 958,
	label = "N3s-(Cd-Sd)(Cd-Cd)H",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   CS  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   S   u0 {2,D}
6   C   u0 {3,D}
""",
	solute = u'N3rs-(Crd-Sd)(Crd-Crd)H',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 959,
	label = "N3rs-(Crd-Sd)(Crd-Crd)H",
	group = 
"""
1 * N3s u0 r1 {2,S} {3,S} {4,S}
2   CS  u0 r1 {1,S} {5,D}
3   Cd  u0 r1 {1,S} {6,D}
4   H   u0 {1,S}
5   S   u0 {2,D}
6   C   u0 r1 {3,D}
""",
	solute = SoluteData(
		S = 0.05724,
		B = 0.07594,
		E = 0.06116,
		L = 0.15459,
		A = 0.08231,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
		E = 2,
		L = 2,
		A = 2,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 960,
	label = "N3s-(Cd-O2d)(Cd-O2d)H",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   CO  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   O2d u0 {2,D}
6   O2d u0 {3,D}
""",
	solute = u'N3rs-(Crd-O2d)(Crd-O2d)H',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 961,
	label = "N3rs-(Crd-O2d)(Crd-O2d)H",
	group = 
"""
1 * N3s u0 r1 {2,S} {3,S} {4,S}
2   CO  u0 r1 {1,S} {5,D}
3   CO  u0 r1 {1,S} {6,D}
4   H   u0 {1,S}
5   O2d u0 {2,D}
6   O2d u0 {3,D}
""",
	solute = SoluteData(
		S = -0.04081,
		B = 0.00953,
		E = 0.03972,
		L = 0.01880,
		A = 0.21470,
	),
	dataCount = DataCountGAV(
		S = 125,
		B = 125,
		E = 126,
		L = 78,
		A = 125,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 962,
	label = "N3s-(Cd-O2d)(Cd-N3d)H",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   O2d u0 {2,D}
6   N3d u0 {3,D}
""",
	solute = u'N3rs-(Crd-O2d)(Crd-N3rd)H',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 963,
	label = "N3rs-(Crd-O2d)(Crd-N3rd)H",
	group = 
"""
1 * N3s u0 r1 {2,S} {3,S} {4,S}
2   CO  u0 r1 {1,S} {5,D}
3   Cd  u0 r1 {1,S} {6,D}
4   H   u0 {1,S}
5   O2d u0 {2,D}
6   N3d u0 r1 {3,D}
""",
	solute = SoluteData(
		S = 0.05652,
		B = 0.02663,
		E = -0.01893,
		L = -0.00494,
		A = 0.19227,
	),
	dataCount = DataCountGAV(
		S = 18,
		B = 16,
		E = 18,
		L = 14,
		A = 18,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 964,
	label = "N3s-(Cd-O2d)(Crd-N3rd)H",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   Cd  u0 r1 {1,S} {6,D}
4   H   u0 {1,S}
5   O2d u0 {2,D}
6   N3d u0 r1 {3,D}
""",
	solute = SoluteData(
		S = -0.08759,
		B = 0.01986,
		E = 0.11096,
		L = 0.19544,
		A = 0.19228,
	),
	dataCount = DataCountGAV(
		S = 16,
		B = 16,
		E = 16,
		L = 13,
		A = 16,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 965,
	label = "N3s-(Cd-O2d)(Cd-Sd)H",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   CS  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   O2d u0 {2,D}
6   S   u0 {3,D}
""",
	solute = u'N3rs-(Crd-O2d)(Crd-Sd)H',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 966,
	label = "N3rs-(Crd-O2d)(Crd-Sd)H",
	group = 
"""
1 * N3s u0 r1 {2,S} {3,S} {4,S}
2   CO  u0 r1 {1,S} {5,D}
3   CS  u0 r1 {1,S} {6,D}
4   H   u0 {1,S}
5   O2d u0 {2,D}
6   S   u0 {3,D}
""",
	solute = SoluteData(
		S = -0.03928,
		B = -0.00824,
		E = 0.05579,
		L = 0.08980,
		A = 0.19612,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 5,
		E = 5,
		L = 4,
		A = 5,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 967,
	label = "N3s-COH",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   C   u0 {1,S}
3   O   u0 {1,S}
4   H   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.08721,
		B = 0.02674,
		E = 0.01591,
		L = 0.14396,
		A = 0.13152,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
		E = 2,
		L = 2,
		A = 3,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 968,
	label = "N3s-CSH",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   C   u0 {1,S}
3   S   u0 {1,S}
4   H   u0 {1,S}
""",
	solute = u'N3s-CS6ddH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 969,
	label = "N3s-CS6ddH",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   C   u0 {1,S}
3   S6dd u0 {1,S}
4   H   u0 {1,S}
""",
	solute = u'N3s-CrS6ddH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 970,
	label = "N3s-CbS6ddH",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cb  u0 {1,S}
3   S6dd u0 {1,S}
4   H   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.05051,
		B = 0.04229,
		E = -0.02881,
		L = 0.09517,
		A = 0.21541,
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
	index = 971,
	label = "N3s-CrS6ddH",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   C   u0 r1 {1,S}
3   S6dd u0 {1,S}
4   H   u0 {1,S}
""",
	solute = u'N3s-CrdS6ddH',
	dataCount = None,
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 972,
	label = "N3s-CrdS6ddH",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cd  u0 r1 {1,S}
3   S6dd u0 {1,S}
4   H   u0 {1,S}
""",
	solute = SoluteData(
		S = -0.07906,
		B = 0.06637,
		E = 0.05224,
		L = 0.13183,
		A = 0.26684,
	),
	dataCount = DataCountGAV(
		S = 25,
		B = 25,
		E = 25,
		L = 23,
		A = 25,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 973,
	label = "N3s-CdS6ddH",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   [Cd,CO,CS]  u0 {1,S}
3   S6dd u0 {1,S}
4   H   u0 {1,S}
""",
	solute = u'N3s-(Cd-O2d)S6ddH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 974,
	label = "N3s-(Cd-O2d)S6ddH",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   CO  u0 {1,S}
3   S6dd u0 {1,S}
4   H   u0 {1,S}
""",
	solute = SoluteData(
		S = -0.09830,
		B = -0.05440,
		E = 0.03221,
		L = -0.07423,
		A = 0.13635,
	),
	dataCount = DataCountGAV(
		S = 9,
		B = 9,
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
	index = 975,
	label = "N3s-CsS6ddH",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   S6dd u0 {1,S}
4   H   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.07195,
		B = -0.01825,
		E = 0.03641,
		L = 0.07666,
		A = 0.18086,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 4,
		L = 2,
		A = 3,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 976,
	label = "N3s-CCC",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
""",
	solute = u'N3s-CsCsCs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 977,
	label = "N3s-CsCsCs",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
""",
	solute = SoluteData(
		S = -0.11941,
		B = 0.14315,
		E = -0.08614,
		L = 0.12131,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 141,
		B = 141,
		E = 150,
		L = 114,
		A = 151,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 978,
	label = "N3rs-CrsCrsCrs",
	group = 
"""
1 * N3s u0 r1 {2,S} {3,S} {4,S}
2   Cs  u0 r1 {1,S}
3   Cs  u0 r1 {1,S}
4   Cs  u0 r1 {1,S}
""",
	solute = SoluteData(
		S = -0.07446,
		B = -0.03097,
		E = 0.07594,
		L = 0.00705,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 14,
		B = 14,
		E = 15,
		L = 13,
		A = 14,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 979,
	label = "N3rs-CrsCrsCs",
	group = 
"""
1 * N3s u0 r1 {2,S} {3,S} {4,S}
2   Cs  u0 r1 {1,S}
3   Cs  u0 r1 {1,S}
4   Cs  u0 {1,S}
""",
	solute = SoluteData(
		S = -0.07680,
		B = 0.09229,
		E = 0.01676,
		L = 0.18912,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 141,
		B = 141,
		E = 144,
		L = 132,
		A = 142,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 980,
	label = "N3s-CbCsCs",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cb  u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.01650,
		B = -0.09642,
		E = 0.06505,
		L = -0.09044,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 64,
		B = 61,
		E = 69,
		L = 56,
		A = 71,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 981,
	label = "N3s-CbCdCd",
	group = 
"""
1 * N3s         u0 {2,S} {3,S} {4,S}
2   [Cd,CO,CS]  u0 {1,S}
3   [Cd,CO,CS]  u0 {1,S}
4   Cb          u0 {1,S}
""",
	solute = u'N3s-Cb(Cd-O2d)(Cd-Cd)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 982,
	label = "N3s-Cb(Cd-O2d)(Cd-Cd)",
	group = 
"""
1 * N3s  u0 {2,S} {3,S} {4,S}
2   CO   u0 {1,S}
3   Cd   u0 {1,S} {5,D}
4   Cb   u0 {1,S}
5   C    u0 {3,D}
""",
	solute = u'N3rs-Cb(Cd-O2d)(Crd-Crd)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 983,
	label = "N3rs-Cb(Cd-O2d)(Crd-Crd)",
	group = 
"""
1 * N3s  u0 r1 {2,S} {3,S} {4,S}
2   CO   u0 {1,S}
3   Cd   u0 r1 {1,S} {5,D}
4   Cb   u0 {1,S}
5   C    u0 r1 {3,D}
""",
	solute = u'N3rs-(Cd-O2d)CbCrs',
	dataCount = None,
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 984,
	label = "N3s-CbCbCs",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cb  u0 {1,S}
3   Cb  u0 {1,S}
4   Cs  u0 {1,S}
""",
	solute = u'N3rs-CbCbCs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 985,
	label = "N3rs-CbCbCs",
	group = 
"""
1 * N3s u0 r1 {2,S} {3,S} {4,S}
2   Cb  u0 {1,S}
3   Cb  u0 {1,S}
4   Cs  u0 {1,S}
""",
	solute = SoluteData(
		S = -0.03392,
		B = -0.09198,
		E = -0.13215,
		L = -0.10413,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 26,
		B = 26,
		E = 27,
		L = 25,
		A = 26,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 986,
	label = "N3s-CbCbCd",
	group = 
"""
1 * N3s         u0 {2,S} {3,S} {4,S}
2   Cb          u0 {1,S}
3   Cb          u0 {1,S}
4   [Cd,CO,CS]  u0 {1,S}
""",
	solute = u'N3s-CbCb(Cd-O2d)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 987,
	label = "N3s-CbCb(Cd-O2d)",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cb  u0 {1,S}
3   Cb  u0 {1,S}
4   CO  u0 {1,S} {5,D}
5   O2d u0 {4,D}
""",
	solute = SoluteData(
		S = -0.05187,
		B = 0.05829,
		E = -0.17407,
		L = -0.26976,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 7,
		B = 7,
		E = 7,
		L = 7,
		A = 13,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 988,
	label = "N3s-CbCbCb",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cb  u0 {1,S}
3   Cb  u0 {1,S}
4   Cb  u0 {1,S}
""",
	solute = SoluteData(
		S = -0.04475,
		B = -0.02670,
		E = -0.05483,
		L = -0.00790,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
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
	index = 989,
	label = "N3s-CdCsCs",
	group = 
"""
1 * N3s         u0 {2,S} {3,S} {4,S}
2   [Cd,CO,CS]  u0 {1,S}
3   Cs          u0 {1,S}
4   Cs          u0 {1,S}
""",
	solute = u'N3s-(Cd-O2d)CsCs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 990,
	label = "N3s-(Cd-N3d)CsCs",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   N3d  u0 {2,D}
""",
	solute = SoluteData(
		S = -0.03844,
		B = 0.10897,
		E = -0.04845,
		L = 0.09584,
		A = -0.01157,
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
	index = 991,
	label = "N3rs-(Crd-N3rd)CrsCrs",
	group = 
"""
1 * N3s u0 r1 {2,S} {3,S} {4,S}
2   Cd  u0 r1 {1,S} {5,D}
3   Cs  u0 r1 {1,S}
4   Cs  u0 r1 {1,S}
5   N3d  u0 r1 {2,D}
""",
	solute = SoluteData(
		S = -0.08500,
		B = -0.09428,
		E = 0.01809,
		L = 0.09527,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 19,
		B = 19,
		E = 19,
		L = 17,
		A = 19,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 992,
	label = "N3s-(Crd-N3rd)CsCs",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cd  u0 r1 {1,S} {5,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   N3d  u0 r1 {2,D}
""",
	solute = SoluteData(
		S = -0.18622,
		B = -0.00426,
		E = 0.05385,
		L = -0.03400,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 8,
		B = 8,
		E = 8,
		L = 8,
		A = 8,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 993,
	label = "N3s-(Cd-O2d)CsCs",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   O2d  u0 {2,D}
""",
	solute = SoluteData(
		S = 0.21632,
		B = 0.07780,
		E = -0.01746,
		L = 0.32263,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 80,
		B = 84,
		E = 85,
		L = 65,
		A = 101,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 994,
	label = "N3rs-(Crd-O2d)CrsCrs",
	group = 
"""
1 * N3s u0 r1 {2,S} {3,S} {4,S}
2   CO  u0 r1 {1,S} {5,D}
3   Cs  u0 r1 {1,S}
4   Cs  u0 r1 {1,S}
5   O2d  u0 {2,D}
""",
	solute = SoluteData(
		S = -0.12288,
		B = -0.00880,
		E = 0.20355,
		L = 0.07046,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 20,
		B = 20,
		E = 20,
		L = 19,
		A = 20,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 995,
	label = "N3rs-(Cd-O2d)CrsCrs",
	group = 
"""
1 * N3s u0 r1 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   Cs  u0 r1 {1,S}
4   Cs  u0 r1 {1,S}
5   O2d  u0 {2,D}
""",
	solute = SoluteData(
		S = 0.09173,
		B = 0.00490,
		E = 0.03635,
		L = 0.27497,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 29,
		B = 29,
		E = 32,
		L = 25,
		A = 34,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 996,
	label = "N3rs-(Crd-O2d)CrsCs",
	group = 
"""
1 * N3s u0 r1 {2,S} {3,S} {4,S}
2   CO  u0 r1 {1,S} {5,D}
3   Cs  u0 r1 {1,S}
4   Cs  u0 {1,S}
5   O2d  u0 {2,D}
""",
	solute = SoluteData(
		S = 0.25162,
		B = -0.02681,
		E = -0.16355,
		L = 0.36541,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 17,
		B = 17,
		E = 19,
		L = 17,
		A = 17,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 997,
	label = "N3s-(Cd-Cd)CsCs",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   C   u0 {2,D}
""",
	solute = u'N3s-(Crd-Crd)CsCs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 998,
	label = "N3rs-(Crd-Crd)CrsCs",
	group = 
"""
1 * N3s u0 r1 {2,S} {3,S} {4,S}
2   Cd  u0 r1 {1,S} {5,D}
3   Cs  u0 r1 {1,S}
4   Cs  u0 {1,S}
5   C   u0 r1 {2,D}
""",
	solute = SoluteData(
		S = 0.11364,
		B = 0.01832,
		E = 0.01620,
		L = 0.40492,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 6,
		B = 6,
		E = 6,
		L = 6,
		A = 6,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 999,
	label = "N3s-(Crd-Crd)CsCs",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cd  u0 r1 {1,S} {5,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   C   u0 r1 {2,D}
""",
	solute = SoluteData(
		S = -0.02560,
		B = 0.01183,
		E = 0.13265,
		L = 0.24870,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 8,
		B = 7,
		E = 8,
		L = 7,
		A = 8,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 1000,
	label = "N3s-(Cd-Sd)CsCs",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   CS  u0 {1,S} {5,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   S   u0 {2,D}
""",
	solute = SoluteData(
		S = 0.01374,
		B = 0.02245,
		E = 0.03518,
		L = 0.40353,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 6,
		B = 6,
		E = 6,
		L = 4,
		A = 9,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1001,
	label = "N3s-CdCbCs",
	group = 
"""
1 * N3s         u0 {2,S} {3,S} {4,S}
2   [Cd,CO,CS]  u0 {1,S}
3   Cb          u0 {1,S}
4   Cs          u0 {1,S}
""",
	solute = u'N3s-(Cd-O2d)CbCs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1002,
	label = "N3s-(Cd-O2d)CbCs",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   Cb  u0 {1,S}
4   Cs  u0 {1,S}
5   O2d  u0 {2,D}
""",
	solute = SoluteData(
		S = -0.02816,
		B = 0.07418,
		E = -0.02420,
		L = -0.01764,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 24,
		B = 24,
		E = 26,
		L = 22,
		A = 25,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1003,
	label = "N3rs-(Crd-O2d)CbCrs",
	group = 
"""
1 * N3s u0 r1 {2,S} {3,S} {4,S}
2   CO  u0 r1 {1,S} {5,D}
3   Cb  u0 {1,S}
4   Cs  u0 r1 {1,S}
5   O2d  u0 {2,D}
""",
	solute = SoluteData(
		S = -0.06341,
		B = 0.00351,
		E = -0.00129,
		L = -0.01278,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 8,
		B = 8,
		E = 8,
		L = 8,
		A = 8,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 1004,
	label = "N3rs-(Crd-O2d)CbCs",
	group = 
"""
1 * N3s u0 r1 {2,S} {3,S} {4,S}
2   CO  u0 r1 {1,S} {5,D}
3   Cb  u0 {1,S}
4   Cs  u0 {1,S}
5   O2d  u0 {2,D}
""",
	solute = SoluteData(
		S = 0.01992,
		B = -0.09733,
		E = -0.02426,
		L = 0.19885,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 27,
		B = 27,
		E = 27,
		L = 13,
		A = 27,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 1005,
	label = "N3rs-(Cd-O2d)CbCrs",
	group = 
"""
1 * N3s u0 r1 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   Cb  u0 {1,S}
4   Cs  u0 r1 {1,S}
5   O2d  u0 {2,D}
""",
	solute = SoluteData(
		S = 0.01709,
		B = -0.08440,
		E = 0.04331,
		L = -0.05840,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 16,
		B = 16,
		E = 17,
		L = 15,
		A = 17,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 1006,
	label = "N3s-(Cd-Cd)CbCs",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cb  u0 {1,S}
4   Cs  u0 {1,S}
5   C  u0 {2,D}
""",
	solute = u'N3rs-(Crd-Crd)CbCs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1007,
	label = "N3rs-(Crd-Crd)CbCs",
	group = 
"""
1 * N3s u0 r1 {2,S} {3,S} {4,S}
2   Cd  u0 r1 {1,S} {5,D}
3   Cb  u0 {1,S}
4   Cs  u0 {1,S}
5   C  u0 r1 {2,D}
""",
	solute = SoluteData(
		S = 0.07305,
		B = 0.10823,
		E = 0.04875,
		L = 0.37072,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 13,
		B = 13,
		E = 15,
		L = 13,
		A = 14,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 1008,
	label = "N3s-(Cd-Nd)CbCs",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cb  u0 {1,S}
4   Cs  u0 {1,S}
5   N  u0 {2,D}
""",
	solute = u'N3rs-(Crd-Nrd)CbCs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1009,
	label = "N3rs-(Crd-Nrd)CbCs",
	group = 
"""
1 * N3s u0 r1 {2,S} {3,S} {4,S}
2   Cd  u0 r1 {1,S} {5,D}
3   Cb  u0 {1,S}
4   Cs  u0 {1,S}
5   N  u0 r1 {2,D}
""",
	solute = SoluteData(
		S = 0.00752,
		B = -0.00118,
		E = -0.00735,
		L = 0.21412,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 6,
		B = 6,
		E = 6,
		L = 6,
		A = 6,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 1010,
	label = "N3s-(Cd-S2d)CbCs",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   CS  u0 {1,S} {5,D}
3   Cb  u0 {1,S}
4   Cs  u0 {1,S}
5   S2d u0 {2,D}
""",
	solute = u'N3s-(Cd-O2d)CbCs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1011,
	label = "N3s-CdCdCs",
	group = 
"""
1 * N3s         u0 {2,S} {3,S} {4,S}
2   [Cd,CO,CS]  u0 {1,S}
3   [Cd,CO,CS]  u0 {1,S}
4   Cs          u0 {1,S}
""",
	solute = u'N3s-(Cd-O2d)(Cd-Cd)Cs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1012,
	label = "N3s-(Cd-O2d)(Cd-O2d)Cs",
	group = 
"""
1 * N3s  u0 {2,S} {3,S} {4,S}
2   CO   u0 {1,S}
3   CO   u0 {1,S}
4   Cs   u0 {1,S}
""",
	solute = u'N3rs-(Crd-O2d)(Crd-O2d)Cs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1013,
	label = "N3rs-(Crd-O2d)(Crd-O2d)Cs",
	group = 
"""
1 * N3s  u0 r1 {2,S} {3,S} {4,S}
2   CO   u0 r1 {1,S}
3   CO   u0 r1 {1,S}
4   Cs   u0 {1,S}
""",
	solute = SoluteData(
		S = -0.10952,
		B = -0.14275,
		E = -0.02558,
		L = -0.06096,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 56,
		B = 56,
		E = 59,
		L = 44,
		A = 56,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 1014,
	label = "N3rs-(Crd-O2d)(Cd-O2d)Crs",
	group = 
"""
1 * N3s  u0 r1 {2,S} {3,S} {4,S}
2   CO   u0 r1 {1,S}
3   CO   u0 {1,S}
4   Cs   u0 r1 {1,S}
""",
	solute = SoluteData(
		S = -0.06671,
		B = -0.01783,
		E = 0.05477,
		L = -0.33967,
		A = 0.00601,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
		E = 2,
		L = 2,
		A = 2,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 1015,
	label = "N3s-(Cd-O2d)(Cd-Cd)Cs",
	group = 
"""
1 * N3s  u0 {2,S} {3,S} {4,S}
2   CO   u0 {1,S}
3   Cd   u0 {1,S} {5,D}
4   Cs   u0 {1,S}
5   C    u0 {3,D}
""",
	solute = u'N3rs-(Crd-O2d)(Crd-Crd)Cs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1016,
	label = "N3rs-(Crd-O2d)(Crd-Crd)Cs",
	group = 
"""
1 * N3s  u0 r1 {2,S} {3,S} {4,S}
2   CO   u0 r1 {1,S}
3   Cd   u0 r1 {1,S} {5,D}
4   Cs   u0 {1,S}
5   C    u0 r1 {3,D}
""",
	solute = SoluteData(
		S = 0.09800,
		B = 0.04498,
		E = 0.13039,
		L = 0.53174,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 62,
		B = 62,
		E = 62,
		L = 61,
		A = 62,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 1017,
	label = "N3s-(Cd-O2d)(Cd-Nd)Cs",
	group = 
"""
1 * N3s  u0 {2,S} {3,S} {4,S}
2   CO   u0 {1,S}
3   Cd   u0 {1,S} {5,D}
4   Cs   u0 {1,S}
5   N    u0 {3,D}
""",
	solute = u'N3rs-(Crd-O2d)(Crd-Nrd)Cs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1018,
	label = "N3rs-(Crd-O2d)(Crd-Nrd)Cs",
	group = 
"""
1 * N3s  u0 r1 {2,S} {3,S} {4,S}
2   CO   u0 r1 {1,S}
3   Cd   u0 r1 {1,S} {5,D}
4   Cs   u0 {1,S}
5   N    u0 r1 {3,D}
""",
	solute = SoluteData(
		S = 0.00819,
		B = 0.02527,
		E = 0.04558,
		L = 0.04612,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 8,
		B = 8,
		E = 8,
		L = 8,
		A = 8,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 1019,
	label = "N3s-(Cd-Cd)(Cd-Cd)Cs",
	group = 
"""
1 * N3s  u0 {2,S} {3,S} {4,S}
2   Cd   u0 {1,S} {6,D}
3   Cd   u0 {1,S} {5,D}
4   Cs   u0 {1,S}
5   C    u0 {3,D}
6   C    u0 {2,D}
""",
	solute = u'N3rs-(Crd-Crd)(Crd-Crd)Cs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1020,
	label = "N3rs-(Crd-Crd)(Crd-Crd)Cs",
	group = 
"""
1 * N3s  u0 r1 {2,S} {3,S} {4,S}
2   Cd   u0 r1 {1,S} {6,D}
3   Cd   u0 r1 {1,S} {5,D}
4   Cs   u0 {1,S}
5   C    u0 r1 {3,D}
6   C    u0 r1 {2,D}
""",
	solute = SoluteData(
		S = -0.03892,
		B = 0.02468,
		E = -0.04150,
		L = 0.00851,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 24,
		B = 24,
		E = 24,
		L = 6,
		A = 24,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 1021,
	label = "N3s-(Cd-Cd)(Cd-Nd)Cs",
	group = 
"""
1 * N3s  u0 {2,S} {3,S} {4,S}
2   Cd   u0 {1,S} {6,D}
3   Cd   u0 {1,S} {5,D}
4   Cs   u0 {1,S}
5   C    u0 {3,D}
6   N    u0 {2,D}
""",
	solute = u'N3rs-(Crd-Crd)(Crd-Nrd)Cs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1022,
	label = "N3rs-(Crd-Crd)(Crd-Nrd)Cs",
	group = 
"""
1 * N3s  u0 r1 {2,S} {3,S} {4,S}
2   Cd   u0 r1 {1,S} {6,D}
3   Cd   u0 r1 {1,S} {5,D}
4   Cs   u0 {1,S}
5   C    u0 r1 {3,D}
6   N    u0 r1 {2,D}
""",
	solute = SoluteData(
		S = -0.06297,
		B = 0.00249,
		E = 0.07425,
		L = 0.34422,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 46,
		B = 45,
		E = 47,
		L = 45,
		A = 46,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 1023,
	label = "N3s-(Cd-Cd)(Cd-S2d)Cs",
	group = 
"""
1 * N3s  u0 {2,S} {3,S} {4,S}
2   CS   u0 {1,S} {6,D}
3   Cd   u0 {1,S} {5,D}
4   Cs   u0 {1,S}
5   C    u0 {3,D}
6   S2d  u0 {2,D}
""",
	solute = u'N3rs-(Crd-Crd)(Crd-S2d)Cs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1024,
	label = "N3rs-(Crd-Crd)(Crd-S2d)Cs",
	group = 
"""
1 * N3s  u0 r1 {2,S} {3,S} {4,S}
2   CS   u0 r1 {1,S} {6,D}
3   Cd   u0 r1 {1,S} {5,D}
4   Cs   u0 {1,S}
5   C    u0 r1 {3,D}
6   S2d  u0 {2,D}
""",
	solute = u'N3rs-(Crd-O2d)(Crd-Crd)Cs',
	dataCount = None,
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 1025,
	label = "N3s-(Cd-Nd)(Cd-Nd)Cs",
	group = 
"""
1 * N3s  u0 {2,S} {3,S} {4,S}
2   Cd   u0 {1,S} {6,D}
3   Cd   u0 {1,S} {5,D}
4   Cs   u0 {1,S}
5   N    u0 {3,D}
6   N    u0 {2,D}
""",
	solute = u'N3rs-(Crd-Nrd)(Crd-Nrd)Cs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1026,
	label = "N3rs-(Crd-Nrd)(Crd-Nrd)Cs",
	group = 
"""
1 * N3s  u0 r1 {2,S} {3,S} {4,S}
2   Cd   u0 r1 {1,S} {6,D}
3   Cd   u0 r1 {1,S} {5,D}
4   Cs   u0 {1,S}
5   N    u0 r1 {3,D}
6   N    u0 r1 {2,D}
""",
	solute = SoluteData(
		S = 0.11807,
		B = -0.01637,
		E = 0.04096,
		L = 0.17913,
		A = 0.04984,
	),
	dataCount = DataCountGAV(
		S = 7,
		B = 7,
		E = 7,
		L = 7,
		A = 7,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 1027,
	label = "N3s-CdCdCd",
	group = 
"""
1 * N3s         u0 {2,S} {3,S} {4,S}
2   [Cd,CO,CS]  u0 {1,S}
3   [Cd,CO,CS]  u0 {1,S}
4   [Cd,CO,CS]  u0 {1,S}
""",
	solute = SoluteData(
		S = -0.09449,
		B = -0.07978,
		E = 0.07824,
		L = -0.10496,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 28,
		B = 28,
		E = 29,
		L = 24,
		A = 29,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1028,
	label = "N3s-(Cd-O2d)(Cd-Cd)(Cd-Nd)",
	group = 
"""
1 * N3s  u0 {2,S} {3,S} {4,S}
2   CO   u0 {1,S}
3   Cd   u0 {1,S} {5,D}
4   Cd   u0 {1,S} {6,D}
5   C    u0 {3,D}
6   N    u0 {4,D}
""",
	solute = SoluteData(
		S = 0.02732,
		B = -0.07457,
		E = -0.04320,
		L = 0.05112,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 13,
		B = 13,
		E = 13,
		L = 12,
		A = 13,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1029,
	label = "N3s-CCO",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
4   O   u0 {1,S}
""",
	solute = u'N3s-Cb(Cd-O2d)(O-H)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1030,
	label = "N3s-CbCd(O-H)",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cb  u0 {1,S}
3   [Cd,CO,CS] u0 {1,S}
4   O2s u0 {1,S} {5,S}
5   H   u0 {4,S}
""",
	solute = u'N3s-Cb(Cd-O2d)(O-H)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1031,
	label = "N3s-Cb(Cd-O2d)(O-H)",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cb  u0 {1,S}
3   CO  u0 {1,S}
4   O2s u0 {1,S} {5,S}
5   H   u0 {4,S}
""",
	solute = SoluteData(
		S = -0.17235,
		B = 0.10594,
		E = 0.03362,
		L = -0.04211,
		A = 0.02431,
	),
	dataCount = DataCountGAV(
		S = 22,
		B = 22,
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
	index = 1032,
	label = "N3s-CCS",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
4   S   u0 {1,S}
""",
	solute = u'N3s-CCS6dd',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1033,
	label = "N3s-CCS4d",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
4   S4d u0 {1,S}
""",
	solute = u'N3s-CC(S4d-O2d)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1034,
	label = "N3s-CC(S4d-O2d)",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
4   S4d u0 {1,S} {5,D}
5   O2d u0 {4,D}
""",
	solute = u'N3s-CsCs(S4d-O2d)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1035,
	label = "N3s-CsCs(S4d-O2d)",
	group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
4   S4d u0 {1,S} {5,D}
5   O2d u0 {4,D}
""",
	solute = u'N3s-CsCs(S6dd-O2dO2d)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1036,
	label = "N3s-CCS6dd",
	group = 
"""
1 * N3s  u0 {2,S} {3,S} {4,S}
2   C    u0 {1,S}
3   C    u0 {1,S}
4   S6dd u0 {1,S}
""",
	solute = u'N3s-CC(S6dd-O2dO2d)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1037,
	label = "N3s-CC(S6dd-O2dO2d)",
	group = 
"""
1 * N3s  u0 {2,S} {3,S} {4,S}
2   C    u0 {1,S}
3   C    u0 {1,S}
4   S6dd u0 {1,S} {5,D} {6,D}
5   O2d  u0 {4,D}
6   O2d  u0 {4,D}
""",
	solute = u'N3s-CsCs(S6dd-O2dO2d)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1038,
	label = "N3s-CsCs(S6dd-O2dO2d)",
	group = 
"""
1 * N3s  u0 {2,S} {3,S} {4,S}
2   Cs   u0 {1,S}
3   Cs   u0 {1,S}
4   S6dd u0 {1,S} {5,D} {6,D}
5   O2d  u0 {4,D}
6   O2d  u0 {4,D}
""",
	solute = SoluteData(
		S = 0.00396,
		B = -0.12692,
		E = -0.01189,
		L = -0.07670,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 17,
		B = 17,
		E = 18,
		L = 17,
		A = 22,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1039,
	label = "N3s-CsCd(S6dd-O2dO2d)",
	group = 
"""
1 * N3s  u0 {2,S} {3,S} {4,S}
2   Cs   u0 {1,S}
3   [Cd,CO,CS]  u0 {1,S}
4   S6dd u0 {1,S} {5,D} {6,D}
5   O2d  u0 {4,D}
6   O2d  u0 {4,D}
""",
	solute = u'N3s-Cs(Cd-Cd)(S6dd-O2dO2d)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1040,
	label = "N3s-Cs(Cd-Cd)(S6dd-O2dO2d)",
	group = 
"""
1 * N3s  u0 {2,S} {3,S} {4,S}
2   Cs   u0 {1,S}
3   Cd  u0 {1,S} {7,D}
4   S6dd u0 {1,S} {5,D} {6,D}
5   O2d  u0 {4,D}
6   O2d  u0 {4,D}
7   C    u0 {3,D}
""",
	solute = SoluteData(
		S = 0.00510,
		B = 0.02041,
		E = 0.03085,
		L = 0.09413,
		A = -0.01875,
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
	index = 1041,
	label = "N3s-CbCb(S6dd-O2dO2d)",
	group = 
"""
1 * N3s  u0 {2,S} {3,S} {4,S}
2   Cb   u0 {1,S}
3   Cb   u0 {1,S}
4   S6dd u0 {1,S} {5,D} {6,D}
5   O2d  u0 {4,D}
6   O2d  u0 {4,D}
""",
	solute = SoluteData(
		S = -0.06415,
		B = -0.05212,
		E = -0.07815,
		L = -0.31958,
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
	index = 1042,
	label = "N3d",
	group = 
"""
1 * N3d u0
""",
	solute = u'N3d-CdC',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1043,
	label = "N3d-N5ddc",
	group = 
"""
1 * N3d   u0 {2,D}
2   N5ddc u0 c+1 {1,D}
""",
	solute = SoluteData(
		S = 0.04468,
		B = 0.00000,
		E = 0.09588,
		L = 0.39946,
		A = 0.01261,
	),
	dataCount = DataCountGAV(
		S = 9,
		B = 9,
		E = 9,
		L = 9,
		A = 9,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1044,
	label = "N3d-CdH",
	group = 
"""
1 * N3d  u0 {2,D} {3,S}
2   Cd   u0 {1,D}
3   H    u0 {1,S}
""",
	solute = SoluteData(
		S = 0.08189,
		B = 0.20816,
		E = 0.18543,
		L = 0.43644,
		A = 0.04616,
	),
	dataCount = DataCountGAV(
		S = 6,
		B = 6,
		E = 8,
		L = 3,
		A = 6,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1045,
	label = "N3d-CdN",
	group = 
"""
1 * N3d  u0 {2,D} {3,S}
2   Cd   u0 {1,D}
3   N    u0 {1,S}
""",
	solute = u'N3d-CdN3s',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1046,
	label = "N3d-CdN3s",
	group = 
"""
1 * N3d  u0 {2,D} {3,S}
2   Cd   u0 {1,D}
3   N3s  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.18191,
		B = 0.15063,
		E = 0.32247,
		L = 1.14517,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 102,
		B = 99,
		E = 105,
		L = 96,
		A = 103,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1047,
	label = "N3d-CdN3d",
	group = 
"""
1 * N3d  u0 {2,D} {3,S}
2   Cd   u0 {1,D}
3   N3d  u0 {1,S}
""",
	solute = u'N3rd-CrdN3rd',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1048,
	label = "N3rd-CrdN3rd",
	group = 
"""
1 * N3d  u0 r1 {2,D} {3,S}
2   Cd   u0 r1 {1,D}
3   N3d  u0 r1 {1,S}
""",
	solute = SoluteData(
		S = 0.24565,
		B = 0.12774,
		E = 0.22520,
		L = 0.88458,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 21,
		B = 21,
		E = 22,
		L = 20,
		A = 22,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 1049,
	label = "N3d-CdO",
	group = 
"""
1 * N3d  u0 {2,D} {3,S}
2   Cd   u0 {1,D}
3   O    u0 {1,S}
""",
	solute = u'N3d-Cd(O-H)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1050,
	label = "N3d-Cd(O-H)",
	group = 
"""
1 * N3d  u0 {2,D} {3,S}
2   Cd   u0 {1,D}
3   O    u0 {1,S} {4,S}
4   H    u0 {3,S}
""",
	solute = SoluteData(
		S = 0.18430,
		B = 0.12440,
		E = 0.13017,
		L = 0.73864,
		A = 0.03986,
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
	index = 1051,
	label = "N3d-Cd(O-R)",
	group = 
"""
1 * N3d  u0 {2,D} {3,S}
2   Cd   u0 {1,D}
3   O    u0 {1,S} {4,S}
4   R!H  u0 {3,S}
""",
	solute = SoluteData(
		S = 0.00356,
		B = 0.11268,
		E = 0.03656,
		L = 0.42541,
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
	index = 1052,
	label = "N3rd-Crd(Or-R)",
	group = 
"""
1 * N3d  u0 r1 {2,D} {3,S}
2   Cd   u0 r1 {1,D}
3   O    u0 r1 {1,S} {4,S}
4   R!H  u0 {3,S}
""",
	solute = SoluteData(
		S = 0.13615,
		B = 0.09126,
		E = 0.20262,
		L = 0.62299,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 17,
		B = 17,
		E = 17,
		L = 16,
		A = 17,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 1053,
	label = "N3d-CdS",
	group = 
"""
1 * N3d  u0 {2,D} {3,S}
2   Cd   u0 {1,D}
3   S    u0 {1,S}
""",
	solute = u'N3d-CdS2s',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1054,
	label = "N3d-CdS2s",
	group = 
"""
1 * N3d  u0 {2,D} {3,S}
2   Cd   u0 {1,D}
3   S2s  u0 {1,S}
""",
	solute = u'N3rd-CrdS2rs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1055,
	label = "N3rd-CrdS2rs",
	group = 
"""
1 * N3d  u0 r1 {2,D} {3,S}
2   Cd   u0 r1 {1,D}
3   S2s  u0 r1 {1,S}
""",
	solute = SoluteData(
		S = 0.10020,
		B = 0.04043,
		E = 0.19174,
		L = 0.70217,
		A = -0.00913,
	),
	dataCount = DataCountGAV(
		S = 8,
		B = 8,
		E = 8,
		L = 8,
		A = 8,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 1056,
	label = "N3d-CdS6dd",
	group = 
"""
1 * N3d  u0 {2,D} {3,S}
2   Cd   u0 {1,D}
3   S6dd u0 {1,S}
""",
	solute = SoluteData(
		S = -0.03518,
		B = 0.00807,
		E = 0.07348,
		L = 0.13719,
		A = -0.01722,
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
	index = 1057,
	label = "N3d-CdC",
	group = 
"""
1 * N3d  u0 {2,D} {3,S}
2   Cd   u0 {1,D}
3   C    u0 {1,S}
""",
	solute = u'N3d-CdCd',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1058,
	label = "N3d-CdCs",
	group = 
"""
1 * N3d  u0 {2,D} {3,S}
2   Cd   u0 {1,D}
3   Cs   u0 {1,S}
""",
	solute = SoluteData(
		S = -0.16065,
		B = 0.14780,
		E = 0.01262,
		L = 0.02561,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 12,
		B = 12,
		E = 13,
		L = 8,
		A = 13,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1059,
	label = "N3rd-CrdCrs",
	group = 
"""
1 * N3d  u0 r1 {2,D} {3,S}
2   Cd   u0 r1 {1,D}
3   Cs   u0 r1 {1,S}
""",
	solute = SoluteData(
		S = -0.06109,
		B = 0.22653,
		E = 0.18571,
		L = 0.64033,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 41,
		B = 41,
		E = 42,
		L = 21,
		A = 42,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 1060,
	label = "N3d-CdCb",
	group = 
"""
1 * N3d  u0 {2,D} {3,S}
2   Cd   u0 {1,D}
3   Cb   u0 {1,S}
""",
	solute = u'N3rd-CrdCb',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1061,
	label = "N3rd-CrdCb",
	group = 
"""
1 * N3d  u0 r1 {2,D} {3,S}
2   Cd   u0 r1 {1,D}
3   Cb   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.00262,
		B = 0.06847,
		E = 0.17967,
		L = 0.49325,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 124,
		B = 116,
		E = 132,
		L = 123,
		A = 126,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 1062,
	label = "N3d-CdCd",
	group = 
"""
1 * N3d         u0 {2,D} {3,S}
2   Cd          u0 {1,D}
3   [Cd,CO,CS]  u0 {1,S}
""",
	solute = u'N3d-Cd(Cd-Cd)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1063,
	label = "N3d-Cd(Cd-O2d)",
	group = 
"""
1 * N3d  u0 {2,D} {3,S}
2   Cd   u0 {1,D}
3   CO   u0 {1,S} {4,D}
4   O2d  u0 {3,D}
""",
	solute = u'N3rd-Crd(Crd-O2d)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1064,
	label = "N3rd-Crd(Crd-O2d)",
	group = 
"""
1 * N3d   u0 r1 {2,D} {3,S}
2   Cd    u0 r1 {1,D}
3   CO    u0 r1 {1,S} {4,D}
4   O2d   u0 {3,D}
""",
	solute = SoluteData(
		S = 0.09142,
		B = 0.08863,
		E = 0.15317,
		L = 0.50789,
		A = 0.02231,
	),
	dataCount = DataCountGAV(
		S = 12,
		B = 11,
		E = 12,
		L = 10,
		A = 12,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 1065,
	label = "N3d-Cd(Cd-N3d)",
	group = 
"""
1 * N3d  u0 {2,D} {3,S}
2   Cd   u0 {1,D}
3   Cd   u0 {1,S} {4,D}
4   N3d  u0 {3,D}
""",
	solute = SoluteData(
		S = 0.09106,
		B = 0.18768,
		E = 0.04579,
		L = 0.59277,
		A = -0.00225,
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
	index = 1066,
	label = "N3rd-Crd(Crd-N3rd)",
	group = 
"""
1 * N3d  u0 r1 {2,D} {3,S}
2   Cd   u0 r1 {1,D}
3   Cd   u0 r1 {1,S} {4,D}
4   N3d  u0 r1 {3,D}
""",
	solute = SoluteData(
		S = 0.12462,
		B = 0.18226,
		E = 0.16491,
		L = 0.69020,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 132,
		B = 131,
		E = 136,
		L = 124,
		A = 138,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 1067,
	label = "N3d-Cd(Crd-N3rd)",
	group = 
"""
1 * N3d  u0 {2,D} {3,S}
2   Cd   u0 {1,D}
3   Cd   u0 r1 {1,S} {4,D}
4   N3d  u0 r1 {3,D}
""",
	solute = SoluteData(
		S = -0.00508,
		B = -0.00293,
		E = 0.04022,
		L = 0.20700,
		A = 0.16512,
	),
	dataCount = DataCountGAV(
		S = 6,
		B = 6,
		E = 7,
		L = 4,
		A = 6,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 1068,
	label = "N3d-Cd(Cd-Cd)",
	group = 
"""
1 * N3d  u0 {2,D} {3,S}
2   Cd   u0 {1,D}
3   Cd   u0 {1,S} {4,D}
4   C    u0 {3,D}
""",
	solute = u'N3rd-Crd(Crd-Crd)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1069,
	label = "N3rd-Crd(Crd-Crd)",
	group = 
"""
1 * N3d  u0 r1 {2,D} {3,S}
2   Cd   u0 r1 {1,D}
3   Cd   u0 r1 {1,S} {4,D}
4   C    u0 r1 {3,D}
""",
	solute = SoluteData(
		S = 0.20649,
		B = 0.13895,
		E = 0.34976,
		L = 1.24580,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 506,
		B = 442,
		E = 556,
		L = 446,
		A = 550,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 1070,
	label = "N3d-CdCt",
	group = 
"""
1 * N3d  u0 {2,D} {3,S}
2   Cd   u0 {1,D}
3   Ct   u0 {1,S}
""",
	solute = u'N3d-Cd(Ct-N3t)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1071,
	label = "N3d-Cd(Ct-N3t)",
	group = 
"""
1 * N3d  u0 {2,D} {3,S}
2   Cd   u0 {1,D}
3   Ct   u0 {1,S} {4,T}
4   N3t  u0 {3,T}
""",
	solute = SoluteData(
		S = 0.08061,
		B = 0.02152,
		E = -0.00632,
		L = 0.24359,
		A = 0.12173,
	),
	dataCount = DataCountGAV(
		S = 4,
		B = 4,
		E = 5,
		L = 2,
		A = 4,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1072,
	label = "N3d-CddC",
	group = 
"""
1 * N3d  u0 {2,D} {3,S}
2   Cdd  u0 {1,D}
3   C    u0 {1,S}
""",
	solute = u'N3d-(Cdd-O2d)C',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1073,
	label = "N3d-(Cdd-O2d)C",
	group = 
"""
1 * N3d  u0 {2,D} {3,S}
2   Cdd  u0 {1,D} {4,D}
3   C    u0 {1,S}
4   O2d  u0 {2,D}
""",
	solute = u'N3d-(Cdd-O2d)Cs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1074,
	label = "N3d-(Cdd-O2d)Cs",
	group = 
"""
1 * N3d  u0 {2,D} {3,S}
2   Cdd  u0 {1,D} {4,D}
3   Cs   u0 {1,S}
4   O2d  u0 {2,D}
""",
	solute = SoluteData(
		S = 0.07104,
		B = 0.01930,
		E = 0.01070,
		L = 0.20647,
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
	index = 1075,
	label = "N3d-(Cdd-O2d)Cb",
	group = 
"""
1 * N3d  u0 {2,D} {3,S}
2   Cdd  u0 {1,D} {4,D}
3   Cb   u0 {1,S}
4   O2d  u0 {2,D}
""",
	solute = SoluteData(
		S = 0.09820,
		B = 0.02877,
		E = 0.05808,
		L = 0.30346,
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
	index = 1076,
	label = "N3d-(Cdd-Sd)C",
	group = 
"""
1 * N3d  u0 {2,D} {3,S}
2   Cdd  u0 {1,D} {4,D}
3   C    u0 {1,S}
4   S    u0 {2,D}
""",
	solute = u'N3d-(Cdd-S2d)C',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1077,
	label = "N3d-(Cdd-S2d)C",
	group = 
"""
1 * N3d  u0 {2,D} {3,S}
2   Cdd  u0 {1,D} {4,D}
3   C    u0 {1,S}
4   S2d  u0 {2,D}
""",
	solute = u'N3d-(Cdd-S2d)Cs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1078,
	label = "N3d-(Cdd-S2d)Cs",
	group = 
"""
1 * N3d  u0 {2,D} {3,S}
2   Cdd  u0 {1,D} {4,D}
3   Cs   u0 {1,S}
4   S2d  u0 {2,D}
""",
	solute = SoluteData(
		S = 0.03612,
		B = 0.00163,
		E = 0.01842,
		L = 0.15609,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 6,
		B = 9,
		E = 8,
		L = 6,
		A = 11,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1079,
	label = "N3d-(Cdd-S2d)Cb",
	group = 
"""
1 * N3d  u0 {2,D} {3,S}
2   Cdd  u0 {1,D} {4,D}
3   Cb   u0 {1,S}
4   S2d  u0 {2,D}
""",
	solute = SoluteData(
		S = 0.00131,
		B = -0.02611,
		E = 0.06175,
		L = 0.08273,
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
	index = 1080,
	label = "N3d-N3dN",
	group = 
"""
1 * N3d  u0 {2,D} {3,S}
2   N3d  u0 {1,D}
3   N    u0 {1,S}
""",
	solute = u'N3d-N3dN3s',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1081,
	label = "N3d-N3dN3s",
	group = 
"""
1 * N3d  u0 {2,D} {3,S}
2   N3d  u0 {1,D}
3   N3s  u0 {1,S}
""",
	solute = u'N3rd-N3rdN3rs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1082,
	label = "N3rd-N3rdN3rs",
	group = 
"""
1 * N3d  u0 r1 {2,D} {3,S}
2   N3d  u0 r1 {1,D}
3   N3s  u0 r1 {1,S}
""",
	solute = SoluteData(
		S = 0.12876,
		B = 0.10683,
		E = 0.20440,
		L = 0.57559,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 16,
		B = 15,
		E = 16,
		L = 13,
		A = 16,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 1083,
	label = "N3d-N3dN3d",
	group = 
"""
1 * N3d  u0 {2,D} {3,S}
2   N3d  u0 {1,D}
3   N3d  u0 {1,S}
""",
	solute = u'N3d-N3d(N3d-Cd)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1084,
	label = "N3d-N3d(N3d-Cd)",
	group = 
"""
1 * N3d  u0 {2,D} {3,S}
2   N3d  u0 {1,D}
3   N3d  u0 {1,S} {4,D}
4   Cd   u0 {3,D}
""",
	solute = u'N3rd-N3rd(N3rd-Crd)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1085,
	label = "N3rd-N3rd(N3rd-Crd)",
	group = 
"""
1 * N3d  u0 r1 {2,D} {3,S}
2   N3d  u0 r1 {1,D}
3   N3d  u0 r1 {1,S} {4,D}
4   Cd   u0 r1 {3,D}
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
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 1086,
	label = "N3d-N3dC",
	group = 
"""
1 * N3d  u0 {2,D} {3,S}
2   N3d  u0 {1,D}
3   C    u0 {1,S}
""",
	solute = u'N3d-N3dCb',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1087,
	label = "N3d-N3dCb",
	group = 
"""
1 * N3d  u0 {2,D} {3,S}
2   N3d  u0 {1,D}
3   Cb   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.00703,
		B = 0.02136,
		E = 0.06188,
		L = 0.44470,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 19,
		B = 19,
		E = 20,
		L = 16,
		A = 19,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1088,
	label = "N3d-N3dCs",
	group = 
"""
1 * N3d  u0 {2,D} {3,S}
2   N3d  u0 {1,D}
3   Cs   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.13053,
		B = 0.04972,
		E = 0.05888,
		L = 0.58952,
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
	index = 1089,
	label = "N3d-N3dCd",
	group = 
"""
1 * N3d  u0 {2,D} {3,S}
2   N3d  u0 {1,D}
3   Cd   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.25089,
		B = 0.12557,
		E = 0.12649,
		L = 0.65242,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 9,
		B = 8,
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
	index = 1090,
	label = "N3d-O2dO",
	group = 
"""
1 * N3d  u0 {2,D} {3,S}
2   O2d  u0 {1,D}
3   O    u0 {1,S}
""",
	solute = SoluteData(
		S = -0.01340,
		B = 0.04305,
		E = -0.01741,
		L = 0.03588,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 5,
		E = 13,
		L = 5,
		A = 15,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1091,
	label = "N3d-O2dN",
	group = 
"""
1 * N3d  u0 {2,D} {3,S}
2   O2d  u0 {1,D}
3   N    u0 {1,S}
""",
	solute = u'N3d-O2dN3s',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1092,
	label = "N3d-O2dN3s",
	group = 
"""
1 * N3d  u0 {2,D} {3,S}
2   O2d  u0 {1,D}
3   N3s  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.29469,
		B = 0.01752,
		E = 0.14053,
		L = 0.65622,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 39,
		B = 39,
		E = 39,
		L = 39,
		A = 39,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1093,
	label = "N3d-O2dC",
	group = 
"""
1 * N3d  u0 {2,D} {3,S}
2   O2d  u0 {1,D}
3   C    u0 {1,S}
""",
	solute = u'N3d-O2dCb',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1094,
	label = "N3d-O2dCb",
	group = 
"""
1 * N3d  u0 {2,D} {3,S}
2   O2d  u0 {1,D}
3   Cb   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.01932,
		B = 0.05108,
		E = -0.02692,
		L = -0.02351,
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
	index = 1095,
	label = "N3d-SdS",
	group = 
"""
1 * N3d  u0 {2,D} {3,S}
2   S    u0 {1,D}
3   S    u0 {1,S}
""",
	solute = u'N3d-S4ddS2s',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1096,
	label = "N3d-S4ddS2s",
	group = 
"""
1 * N3d  u0 {2,D} {3,S}
2   S4dd u0 {1,D}
3   S2s   u0 {1,S}
""",
	solute = u'N3d-(S4dd-N3d)S2s',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1097,
	label = "N3d-(S4dd-N3d)S2s",
	group = 
"""
1 * N3d  u0 {2,D} {3,S}
2   S4dd u0 {1,D} {4,D}
3   S2s  u0 {1,S}
4   N3d  u0 {2,D}
""",
	solute = SoluteData(
		S = 0.18259,
		B = 0.02147,
		E = 0.23178,
		L = 0.85280,
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
	index = 1098,
	label = "N3d-PdP",
	group = 
"""
1 * N3d  u0 {2,D} {3,S}
2   P    u0 {1,D}
3   P    u0 {1,S}
""",
	solute = u'N3d-P5dP5d',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1099,
	label = "N3d-P5dP5d",
	group = 
"""
1 * N3d  u0 {2,D} {3,S}
2   P5d  u0 {1,D}
3   P5d  u0 {1,S}
""",
	solute = SoluteData(
		S = -0.03994,
		B = 0.09164,
		E = 0.06619,
		L = 0.40872,
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
	index = 1100,
	label = "N3t",
	group = 
"""
1 * N3t  u0 p1 {2,T}
2   R!H  u0 {1,T}
""",
	solute = u'N3t-Ct',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1101,
	label = "N3t-Ct",
	group = 
"""
1 * N3t  u0 p1 {2,T}
2   Ct   u0 {1,T}
""",
	solute = SoluteData(
		S = 0.43784,
		B = 0.17326,
		E = 0.18638,
		L = 1.20727,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 141,
		B = 139,
		E = 162,
		L = 131,
		A = 153,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1102,
	label = "N5sc",
	group = 
"""
1 * N5sc u0 p0 c+1
""",
	solute = u'N5sc-O0sc',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1103,
	label = "N5sc-O0sc",
	group = 
"""
1 * N5sc u0 p0 c+1 {2,S}
2   O0sc u0 c-1 {1,S} 
""",
	solute = u'N5dc-CdO0sc(Crd-Crd)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1104,
	label = "N5dc",
	group = 
"""
1 * N5dc u0 c+1
""",
	solute = u'N5dc-OdO0scC',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1105,
	label = "N5dc-OdO0scC",
	group = 
"""
1 * N5dc u0 c+1 {2,D} {3,S} {4,S}
2   O2d  u0 {1,D}
3   O0sc u0 c-1 {1,S}
4   C    u0 {1,S}
""",
	solute = u'N5dc-OdO0scCb',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1106,
	label = "N5dc-OdO0scCb",
	group = 
"""
1 * N5dc u0 c+1 {2,D} {3,S} {4,S}
2   O2d  u0 {1,D}
3   O0sc u0 c-1 {1,S}
4   Cb   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.01052,
		B = -0.02704,
		E = -0.06471,
		L = -0.00701,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 301,
		B = 299,
		E = 303,
		L = 258,
		A = 307,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1107,
	label = "N5dc-OdO0scCs",
	group = 
"""
1 * N5dc u0 c+1 {2,D} {3,S} {4,S}
2   O2d  u0 {1,D}
3   O0sc u0 c-1 {1,S}
4   Cs   u0 {1,S}
""",
	solute = SoluteData(
		S = -0.07052,
		B = 0.04093,
		E = -0.11504,
		L = -0.28616,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 20,
		B = 20,
		E = 20,
		L = 15,
		A = 22,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1108,
	label = "N5dc-OdO0scCd",
	group = 
"""
1 * N5dc        u0 c+1 {2,D} {3,S} {4,S}
2   O2d         u0 {1,D}
3   O0sc        u0 c-1 {1,S}
4   [Cd,CO,CS]  u0 {1,S}
""",
	solute = u'N5dc-OdO0sc(Cd-Cd)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1109,
	label = "N5dc-OdO0sc(Cd-Cd)",
	group = 
"""
1 * N5dc        u0 c+1 {2,D} {3,S} {4,S}
2   O2d         u0 {1,D}
3   O0sc        u0 c-1 {1,S}
4   Cd          u0 {1,S} {5,D}
5   C           u0 {4,D}
""",
	solute = SoluteData(
		S = 0.05238,
		B = 0.05110,
		E = 0.02977,
		L = 0.39693,
		A = 0.03358,
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
	index = 1110,
	label = "N5dc-OdO0sc(Crd-Crd)",
	group = 
"""
1 * N5dc        u0 c+1 {2,D} {3,S} {4,S}
2   O2d         u0 {1,D}
3   O0sc        u0 c-1 {1,S}
4   Cd          u0 r1 {1,S} {5,D}
5   C           u0 r1 {4,D}
""",
	solute = SoluteData(
		S = 0.09024,
		B = -0.01540,
		E = 0.07609,
		L = 0.28353,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 22,
		B = 22,
		E = 26,
		L = 21,
		A = 22,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 1111,
	label = "N5dc-OdO0sc(Cd-Nd)",
	group = 
"""
1 * N5dc        u0 c+1 {2,D} {3,S} {4,S}
2   O2d         u0 {1,D}
3   O0sc        u0 c-1 {1,S}
4   Cd          u0 {1,S} {5,D}
5   N           u0 {4,D}
""",
	solute = u'N5dc-OdO0sc(Crd-N3rd)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1112,
	label = "N5dc-OdO0sc(Crd-N3rd)",
	group = 
"""
1 * N5dc        u0 c+1 {2,D} {3,S} {4,S}
2   O2d         u0 {1,D}
3   O0sc        u0 c-1 {1,S}
4   Cd          u0 r1 {1,S} {5,D}
5   N3d         u0 r1 {4,D}
""",
	solute = SoluteData(
		S = 0.03927,
		B = -0.00815,
		E = 0.11728,
		L = 0.01902,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 11,
		B = 11,
		E = 12,
		L = 11,
		A = 11,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 1113,
	label = "N5dc-OdO0scO2s",
	group = 
"""
1 * N5dc u0 c+1 {2,D} {3,S} {4,S}
2   O2d  u0 {1,D}
3   O0sc u0 c-1 {1,S}
4   O2s  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.09525,
		B = -0.07354,
		E = -0.06071,
		L = 0.07396,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 7,
		B = 8,
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
	index = 1114,
	label = "N5dc-OdO0scN",
	group = 
"""
1 * N5dc u0 c+1 {2,D} {3,S} {4,S}
2   O2d  u0 {1,D}
3   O0sc u0 c-1 {1,S}
4   N    u0 {1,S}
""",
	solute = SoluteData(
		S = -0.05141,
		B = 0.08585,
		E = 0.03266,
		L = -0.13313,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 7,
		B = 7,
		E = 8,
		L = 7,
		A = 7,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1115,
	label = "N5dc-CdO0scC",
	group = 
"""
1 * N5dc u0 c+1 {2,D} {3,S} {4,S}
2   Cd   u0 {1,D}
3   O0sc u0 c-1 {1,S}
4   C    u0 {1,S}
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
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1116,
	label = "N5dc-CdO0scCd",
	group = 
"""
1 * N5dc u0 c+1 {2,D} {3,S} {4,S}
2   Cd   u0 {1,D}
3   O0sc u0 c-1 {1,S}
4   Cd   u0 {1,S}
""",
	solute = u'N5dc-CdO0sc(Cd-Cd)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1117,
	label = "N5dc-CdO0sc(Cd-Cd)",
	group = 
"""
1 * N5dc u0 c+1 {2,D} {3,S} {4,S}
2   Cd   u0 {1,D}
3   O0sc u0 c-1 {1,S}
4   Cd   u0 {1,S} {5,D}
5   C    u0 {4,D}
""",
	solute = u'N5dc-CdO0sc(Crd-Crd)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1118,
	label = "N5dc-CdO0sc(Crd-Crd)",
	group = 
"""
1 * N5dc u0 c+1 {2,D} {3,S} {4,S}
2   Cd   u0 {1,D}
3   O0sc u0 c-1 {1,S}
4   Cd   u0 r1 {1,S} {5,D}
5   C    u0 r1 {4,D}
""",
	solute = SoluteData(
		S = 0.08199,
		B = 0.09045,
		E = 0.07957,
		L = 0.36450,
		A = 0.06846,
	),
	dataCount = DataCountGAV(
		S = 15,
		B = 15,
		E = 19,
		L = 15,
		A = 15,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 1119,
	label = "N5ddc",
	group = 
"""
1 * N5ddc u0 p0 c+1
""",
	solute = u'N5ddc-N1dcN3d',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1120,
	label = "N5ddc-N1dcN3d",
	group = 
"""
1 * N5ddc u0 p0 c+1 {2,D} {3,D}
2   N1dc  u0 c-1 {1,D}
3   N3d   u0 {1,D}
""",
	solute = SoluteData(
		S = 0.04468,
		B = 0.00000,
		E = 0.09588,
		L = 0.39946,
		A = 0.01261,
	),
	dataCount = DataCountGAV(
		S = 9,
		B = 9,
		E = 9,
		L = 9,
		A = 9,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1121,
	label = "N5tc",
	group = 
"""
1 * N5tc u0 p0 c+1
""",
	solute = u'N5tc-C2tcC',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1122,
	label = "N5tc-C2tcC",
	group = 
"""
1 * N5tc u0 p0 c+1 {2,T} {3,S}
2   C2tc u0 c-1 {1,T}
3   C    u0 {1,S}
""",
	solute = u'N5tc-C2tcCs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1123,
	label = "N5tc-C2tcCs",
	group = 
"""
1 * N5tc u0 p0 c+1 {2,T} {3,S}
2   C2tc u0 c-1 {1,T}
3   Cs   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.04195,
		B = -0.00307,
		E = 0.03744,
		L = 0.13348,
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
	index = 1124,
	label = "N5tc-C2tcCb",
	group = 
"""
1 * N5tc u0 p0 c+1 {2,T} {3,S}
2   C2tc u0 c-1 {1,T}
3   Cb   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.03915,
		B = 0.02085,
		E = 0.04258,
		L = 0.24081,
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
	index = 1125,
	label = "P",
	group = 
"""
1 * P u0
""",
	solute = u'P3s',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1126,
	label = "P3s",
	group = 
"""
1 * P3s u0
""",
	solute = u'P3s-CCC',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1127,
	label = "P3s-O2sO2sO2s",
	group = 
"""
1 * P3s u0 {2,S} {3,S} {4,S}
2   O2s u0 {1,S}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
""",
	solute = SoluteData(
		S = 0.03939,
		B = 0.06846,
		E = 0.00644,
		L = 0.17857,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
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
	index = 1128,
	label = "P3s-CCC",
	group = 
"""
1 * P3s u0 {2,S} {3,S} {4,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
""",
	solute = u'P3s-CsCsCs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1129,
	label = "P3s-CsCsCs",
	group = 
"""
1 * P3s u0 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
""",
	solute = SoluteData(
		S = -0.02119,
		B = 0.04241,
		E = 0.03763,
		L = 0.20245,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
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
	index = 1130,
	label = "P3s-CbCbCb",
	group = 
"""
1 * P3s u0 {2,S} {3,S} {4,S}
2   Cb  u0 {1,S}
3   Cb  u0 {1,S}
4   Cb  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.01826,
		B = 0.02522,
		E = 0.04446,
		L = 0.28633,
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
	index = 1131,
	label = "P5d",
	group = 
"""
1 * P5d u0
""",
	solute = u'P5d-O2d',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1132,
	label = "P5d-O2d",
	group = 
"""
1 * P5d u0 {2,D}
2   O2d u0 {1,D}
""",
	solute = u'P5d-O2dO2sO2sO2s',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1133,
	label = "P5d-O2dO2sCH",
	group = 
"""
1 * P5d u0 {2,D} {3,S} {4,S} {5,S}
2   O2d u0 {1,D}
3   O2s u0 {1,S}
4   C   u0 {1,S}
5   H   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.05910,
		B = 0.02484,
		E = 0.00977,
		L = 0.20991,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
		E = 5,
		L = 2,
		A = 4,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1134,
	label = "P5d-O2dO2sO2sH",
	group = 
"""
1 * P5d u0 {2,D} {3,S} {4,S} {5,S}
2   O2d u0 {1,D}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
""",
	solute = SoluteData(
		S = -0.03548,
		B = 0.02141,
		E = -0.01617,
		L = -0.05763,
		A = 0.01667,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 1,
		E = 5,
		L = 1,
		A = 2,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1135,
	label = "P5d-O2dNNN",
	group = 
"""
1 * P5d u0 {2,D} {3,S} {4,S} {5,S}
2   O2d u0 {1,D}
3   N   u0 {1,S}
4   N   u0 {1,S}
5   N   u0 {1,S}
""",
	solute = u'P5d-O2dN3sN3sN3s',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1136,
	label = "P5d-O2dN3sN3sN3s",
	group = 
"""
1 * P5d u0 {2,D} {3,S} {4,S} {5,S}
2   O2d u0 {1,D}
3   N3s u0 {1,S}
4   N3s u0 {1,S}
5   N3s u0 {1,S}
""",
	solute = SoluteData(
		S = -0.01261,
		B = 0.01671,
		E = -0.01180,
		L = 0.03831,
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
	index = 1137,
	label = "P5d-O2dCCC",
	group = 
"""
1 * P5d u0 {2,D} {3,S} {4,S} {5,S}
2   O2d u0 {1,D}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
""",
	solute = u'P5d-O2dCsCsCs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1138,
	label = "P5d-O2dCbCbCb",
	group = 
"""
1 * P5d u0 {2,D} {3,S} {4,S} {5,S}
2   O2d u0 {1,D}
3   Cb  u0 {1,S}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.03711,
		B = 0.10339,
		E = -0.05135,
		L = 0.12497,
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
	index = 1139,
	label = "P5d-O2dCsCsCs",
	group = 
"""
1 * P5d u0 {2,D} {3,S} {4,S} {5,S}
2   O2d u0 {1,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.06224,
		B = 0.11382,
		E = 0.06389,
		L = 0.23542,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 1,
		B = 1,
		E = 9,
		L = 1,
		A = 11,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1140,
	label = "P5d-O2dO2sCC",
	group = 
"""
1 * P5d u0 {2,D} {3,S} {4,S} {5,S}
2   O2d u0 {1,D}
3   O2s u0 {1,S}
4   C   u0 {1,S}
5   C   u0 {1,S}
""",
	solute = u'P5d-O2dO2sCsCs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1141,
	label = "P5d-O2dO2sCbCb",
	group = 
"""
1 * P5d u0 {2,D} {3,S} {4,S} {5,S}
2   O2d u0 {1,D}
3   O2s u0 {1,S}
4   Cb  u0 {1,S}
5   Cb  u0 {1,S}
""",
	solute = SoluteData(
		S = -0.04972,
		B = -0.01787,
		E = 0.07423,
		L = 0.05448,
		A = -0.02595,
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
	index = 1142,
	label = "P5d-O2dO2sCbCs",
	group = 
"""
1 * P5d u0 {2,D} {3,S} {4,S} {5,S}
2   O2d u0 {1,D}
3   O2s u0 {1,S}
4   Cb  u0 {1,S}
5   Cs  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.01258,
		B = -0.05228,
		E = 0.03358,
		L = 0.12447,
		A = -0.04373,
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
	index = 1143,
	label = "P5d-O2dO2sCsCs",
	group = 
"""
1 * P5d u0 {2,D} {3,S} {4,S} {5,S}
2   O2d u0 {1,D}
3   O2s u0 {1,S}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
""",
	solute = SoluteData(
		S = -0.04377,
		B = 0.04838,
		E = 0.00145,
		L = -0.03121,
		A = -0.04156,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 5,
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
	index = 1144,
	label = "P5d-O2dO2sO2sN",
	group = 
"""
1 * P5d u0 {2,D} {3,S} {4,S} {5,S}
2   O2d u0 {1,D}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   N   u0 {1,S}
""",
	solute = u'P5d-O2dO2sO2sN3s',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1145,
	label = "P5d-O2dO2sO2sN3s",
	group = 
"""
1 * P5d u0 {2,D} {3,S} {4,S} {5,S}
2   O2d u0 {1,D}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   N3s u0 {1,S}
""",
	solute = SoluteData(
		S = 0.14510,
		B = -0.06299,
		E = -0.05811,
		L = 0.06398,
		A = 0.10290,
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
	index = 1146,
	label = "P5d-O2dO2sO2sC",
	group = 
"""
1 * P5d u0 {2,D} {3,S} {4,S} {5,S}
2   O2d u0 {1,D}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   C   u0 {1,S}
""",
	solute = u'P5d-O2dO2sO2sCs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1147,
	label = "P5d-O2dO2sO2sCs",
	group = 
"""
1 * P5d u0 {2,D} {3,S} {4,S} {5,S}
2   O2d u0 {1,D}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   Cs  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.10011,
		B = 0.08711,
		E = 0.02767,
		L = 0.41582,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 11,
		B = 11,
		E = 16,
		L = 11,
		A = 17,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1148,
	label = "P5d-O2dO2sO2sCd",
	group = 
"""
1 * P5d u0 {2,D} {3,S} {4,S} {5,S}
2   O2d u0 {1,D}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   [Cd,CO,CS]  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.03345,
		B = 0.03803,
		E = 0.05408,
		L = 0.16385,
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
	index = 1149,
	label = "P5d-O2dO2sO2sO2s",
	group = 
"""
1 * P5d u0 {2,D} {3,S} {4,S} {5,S}
2   O2d u0 {1,D}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
""",
	solute = SoluteData(
		S = 0.00413,
		B = 0.01377,
		E = -0.10957,
		L = -0.31601,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 30,
		B = 30,
		E = 31,
		L = 30,
		A = 33,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1150,
	label = "P5d-N3d",
	group = 
"""
1 * P5d u0 {2,D}
2   N3d u0 {1,D}
""",
	solute = u'P5d-N3dNOO',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1151,
	label = "P5d-N3dNHH",
	group = 
"""
1 * P5d u0 {2,D} {3,S} {4,S} {5,S}
2   N3d u0 {1,D}
3   N   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
	solute = u'P5d-N3dN3dHH',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1152,
	label = "P5d-N3dN3dHH",
	group = 
"""
1 * P5d u0 {2,D} {3,S} {4,S} {5,S}
2   N3d u0 {1,D}
3   N3d u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
	solute = u'P5d-N3dN3dO2sO2s',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1153,
	label = "P5d-N3dNOO",
	group = 
"""
1 * P5d u0 {2,D} {3,S} {4,S} {5,S}
2   N3d u0 {1,D}
3   N   u0 {1,S}
4   O   u0 {1,S}
5   O   u0 {1,S}
""",
	solute = u'P5d-N3dNOO',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1154,
	label = "P5d-N3dN3dO2sO2s",
	group = 
"""
1 * P5d u0 {2,D} {3,S} {4,S} {5,S}
2   N3d u0 {1,D}
3   N3d u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
""",
	solute = SoluteData(
		S = -0.03994,
		B = 0.09164,
		E = 0.06619,
		L = 0.40872,
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
	index = 1155,
	label = "P5d-S2d",
	group = 
"""
1 * P5d u0 {2,D}
2   S2d u0 {1,D}
""",
	solute = u'P5d-S2dO2sO2sO2s',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1156,
	label = "P5d-S2dO2sO2sS",
	group = 
"""
1 * P5d u0 {2,D} {3,S} {4,S} {5,S}
2   S2d u0 {1,D}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   S   u0 {1,S}
""",
	solute = u'P5d-S2dO2sO2sS2s',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 1157,
	label = "P5d-S2dO2sO2sS2s",
	group = 
"""
1 * P5d u0 {2,D} {3,S} {4,S} {5,S}
2   S2d u0 {1,D}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   S2s u0 {1,S}
""",
	solute = SoluteData(
		S = 0.04395,
		B = 0.07729,
		E = 0.18675,
		L = 0.74347,
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
	index = 1158,
	label = "P5d-S2dO2sO2sO2s",
	group = 
"""
1 * P5d u0 {2,D} {3,S} {4,S} {5,S}
2   S2d u0 {1,D}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
""",
	solute = SoluteData(
		S = -0.03503,
		B = 0.04163,
		E = 0.09555,
		L = 0.23338,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 8,
		B = 8,
		E = 8,
		L = 8,
		A = 14,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

tree(
"""
L1: R
	L2: C
		L3: C2tc
			L4: C2tc-N5tc
		L3: Cbf
			L4: Cbf-CbCbCbf
			L4: Cbf-CbCbfCbf
			L4: Cbf-CbfCbfCbf
		L3: Cb
			L4: Cb-H
			L4: Cb-P
				L5: Cb-P3s
				L5: Cb-P5d
			L4: Cb-O
				L5: Cb-O2s
					L6: Cb-O2rs
			L4: Cb-S
				L5: Cb-S2s
					L6: Cb-S2rs
				L5: Cb-S4d
				L5: Cb-S6dd
			L4: Cb-N
				L5: Cb-N3s
					L6: Cb-N3rs
				L5: Cb-N3d
					L6: Cb-N3rd
				L5: Cb-N5dc
				L5: Cb-N5tc
			L4: Cb-C
				L5: Cb-Cb
				L5: Cb-Cr
				L5: Cb-Cs
					L6: Cb-(Cs-Cb)
					L6: Cb-(Cs-Cr)
				L5: Cb-Cds
					L6: Cb-(Cds-O2d)
						L7: Cb-(Cds-O2dOs)
					L6: Cb-(Cds-Cd)
					L6: Cb-(Cds-N3d)
					L6: Cb-(Cds-S2d)
				L5: Cb-Ct
					L6: Cb-(CtCt)
					L6: Cb-(CtN3t)
		L3: Ct
			L4: Ct-N3tN
			L4: Ct-N3tS
				L5: Ct-N3tS2s
			L4: Ct-CtH
			L4: Ct-N3tO
				L5: Ct-N3tOs
			L4: Ct-N3tC
				L5: Ct-N3tCb
				L5: Ct-N3tCs
				L5: Ct-N3tCd
				L5: Ct-N3tCt
					L6: Ct-N3t(CtN3t)
			L4: Ct-CtC
				L5: Ct-CtCs
				L5: Ct-CtCds
					L6: Ct-Ct(Cds-O2d)
					L6: Ct-Ct(Cds-Cd)
						L7: Ct-Ct(Cds-Cds)
				L5: Ct-CtCt
					L6: Ct-Ct(CtCt)
				L5: Ct-CtCb
		L3: Cdd
			L4: Cdd-CdCd
				L5: Cdd-CdsCds
			L4: Cdd-N3dO2d
			L4: Cdd-N3dS
				L5: Cdd-N3dS2d
		L3: Cds
			L4: Cds-Od
				L5: Cds-OdNC
					L6: Cds-OdN3sC
						L7: Crds-OdN3rsCr
						L7: Cds-OdN3sCb
							L8: Cds-Od(N3s-HH)Cb
							L8: Cds-Od(N3s-RH)Cb
							L8: Cds-Od(N3s-RR)Cb
						L7: Cds-OdN3sCs
							L8: Cds-OdN3rsCs
							L8: Cds-Od(N3s-HH)Cs
							L8: Cds-Od(N3s-RH)Cs
							L8: Cds-Od(N3s-RR)Cs
						L7: Cds-OdN3sCd
							L8: Cds-OdN3rsCd
							L8: Cds-OdN3sCrd
					L6: Cds-OdN3dC
						L7: Crds-OdN3rdCr
				L5: Cds-OdNH
				L5: Cds-OdNN
					L6: Cds-OdN3sN
						L7: Cds-OdN3sN3s
							L8: Crds-OdN3rsN3rs
							L8: Cds-OdN3rsN3s
						L7: Cds-OdN3sN3d
							L8: Crds-OdN3rsN3rd
				L5: Cds-OdNOs
					L6: Cds-OdN3rsOs
					L6: Cds-Od(N3sHH)Os
					L6: Cds-Od(N3sCH)Os
					L6: Cds-Od(N3sCC)Os
				L5: Cds-OdNS
				L5: Cds-OdOsH
				L5: Cds-OdOsOs
				L5: Cds-OdCS
					L6: Cds-OdCsSs
				L5: Cds-OdCH
					L6: Cds-OdCsH
					L6: Cds-OdCdsH
						L7: Cds-O2d(Cds-O2d)H
						L7: Cds-O2d(Cds-Cd)H
							L8: Cds-O2d(Cds-Cds)H
					L6: Cds-OdCtH
						L7: Cds-Od(Ct-(Ct-H))H
					L6: Cds-OdCbH
				L5: Cds-OdPOs
					L6: Cds-OdP5dOs
						L7: Cds-OdP5d(OsH)
				L5: Cds-OdCOs
					L6: Cds-OdCtOs
					L6: Cds-OdC(OsH)
						L7: Cds-OdCs(OsH)
						L7: Cds-OdCds(OsH)
							L8: Cds-Od(Cds-O2d)(OsH)
							L8: Cds-Od(Cds-Cd)(OsH)
								L9: Cds-Od(Crds-Crd)(OsH)
							L8: Cds-Od(Cds-N3d)(OsH)
						L7: Cds-OdCb(OsH)
					L6: Cds-OdCsOs
						L7: Crds-OdCrsOrs
						L7: Cds-OdCrsOs
					L6: Cds-OdCdsOs
						L7: Crds-OdCrdsOrs
						L7: Cds-OdCrdsOs
						L7: Cds-O2d(Cds-O2d)O2s
						L7: Cds-O2d(Cds-Cd)O2s
							L8: Cds-O2d(Cds-Cds)O2s
					L6: Cds-OdCbOs
				L5: Cds-OdCC
					L6: Cds-OdCsCs
						L7: Crds-OdCrsCrs
						L7: Cds-OdCrsCrs
						L7: Cds-OdCrsCs
					L6: Cds-OdCdsCs
						L7: Cds-O2d(Cds-O2d)Cs
						L7: Cds-O2d(Cds-Cd)Cs
							L8: Crds-O2d(Crds-Crd)Crs
							L8: Cds-O2d(Crds-Crd)Cs
						L7: Cds-O2d(Cds-N3d)Cs
					L6: Cds-OdCdsCds
						L7: Cds-O2d(Cds-Cd)(Cds-O2d)
							L8: Crds-O2d(Crds-Cd)(Crds-O2d)
						L7: Cds-O2d(Cds-Cd)(Cds-Cd)
							L8: Crds-O2d(Crds-Cd)(Crds-Cd)
						L7: Cds-O2d(Cds-Cd)(Cds-N3d)
					L6: Cds-OdCbCs
						L7: Crds-OdCbCrs
					L6: Cds-OdCbCds
						L7: Cds-OdCb(Cds-O2d)
						L7: Cds-OdCb(Cds-Cd)
							L8: Crds-OdCb(Crds-Cd)
							L8: Cds-OdCb(Crds-Cd)
						L7: Cds-OdCb(Cds-N3d)
							L8: Crds-OdCb(Crds-N3rd)
					L6: Cds-OdCbCb
						L7: Crds-OdCbCb
			L4: Cds-Nd
				L5: Cds-N3dCC
					L6: Cds-N3dCbCb
					L6: Cds-N3dCbCs
						L7: Crds-N3rdCbCrs
						L7: Crds-N3rdCbCs
					L6: Cds-N3dCbCd
						L7: Cds-N3dCb(Cd-O2d)
					L6: Cds-N3dCsCs
						L7: Crds-N3rdCrsCs
						L7: Crds-N3dCrsCrs
					L6: Cds-N3dCdCs
						L7: Cds-N3d(Cd-N3d)Cs
							L8: Crds-N3rd(Crd-N3rd)Cs
						L7: Cds-N3d(Cd-Cd)Cs
							L8: Crds-N3rd(Crd-Crd)Cs
					L6: Cds-N3dCdCd
						L7: Crds-N3rdCrdCrd
						L7: Crds-N3rdCrdCd
					L6: Cds-N3dCtC
				L5: Cds-N3dCO
					L6: Crds-N3rdCrO
					L6: Crds-N3rdCOr
				L5: Cds-N3dCS
					L6: Crds-N3rdCrS
					L6: Crds-N3rdCSr
				L5: Cds-N3dCH
					L6: Cds-N3dCbH
						L7: Crds-N3rdCbH
					L6: Cds-N3dCdH
						L7: Crds-N3rdCrdH
						L7: Cds-N3dCrdH
					L6: Cds-N3dCsH
						L7: Crds-N3rdCrsH
						L7: Cds-(N3d-(O-H))CsH
				L5: Cds-N3dNN
					L6: Cds-N3dN3sN3s
						L7: Crds-N3rdN3rsN3s
					L6: Cds-N3dN3dN3s
						L7: Crds-N3rdN3rdN3s
					L6: Cds-N3dN3sN5dc
						L7: Crds-N3rdN3rsN5dc
					L6: Cds-N3dN3dN5dc
						L7: Crds-N3rdN3rdN5dc
				L5: Cds-N3dNC
					L6: Cds-N3dN3sC
						L7: Crds-N3rdN3rsCr
						L7: Crds-N3rdN3rsC
						L7: Crds-N3rdN3sCr
					L6: Cds-N3dN3dC
						L7: Crds-N3rdN3rdCr
						L7: Crds-N3rdN3rdC
				L5: Cds-N3dNO
					L6: Crds-N3rdNrO
					L6: Crds-N3rdNOr
				L5: Cds-N3dNS
					L6: Crds-N3rdNrS
					L6: Crds-N3rdNSr
				L5: Cds-N3dNH
					L6: Cds-N3dN3sH
						L7: Crds-N3rdN3rsH
					L6: Cds-N3dN3dH
						L7: Crds-N3rdN3rdH
				L5: Cds-N3dOH
					L6: Crds-N3rdOrH
				L5: Cds-N3dSS
					L6: Crds-N3rdSrS
				L5: Cds-N3dSH
					L6: Crds-N3rdSrH
				L5: Cds-N5dc
					L6: Crds-N5rdc
			L4: Cds-Cd
				L5: Cds-CdHH
					L6: Cds-CdsHH
						L7: Cds-CrdsHH
					L6: Cds-CddHH
						L7: Cds-(Cdd-Cd)HH
				L5: Cds-CdOsH
					L6: Cds-CdsOsH
						L7: Crds-CrdsOrsH
				L5: Cds-CdOsOs
					L6: Cds-CdsOsOs
						L7: Crds-CrdsOrsOs
				L5: Cds-CdPH
					L6: Cds-CdP5dH
				L5: Cds-CdNH
					L6: Cds-CdN3sH
						L7: Crds-CrdN3rsH
					L6: Cds-CdN3dH
						L7: Crds-CrdN3rdH
					L6: Cds-CdN5dcH
						L7: Crds-CrdN5rdcH
				L5: Cds-CdNN
					L6: Cds-CdN3sN3s
					L6: Cds-CdN3sN3d
						L7: Crds-CrdN3rsN3rd
						L7: Crds-CrdN3sN3rd
					L6: Cds-CdN3dN3d
					L6: Cds-CdN3sN5dc
					L6: Cds-CdN3dN5dc
				L5: Cds-CdNO
					L6: Cds-CdN3sO
					L6: Cds-CdN3dO
					L6: Cds-CdN5dcO
				L5: Cds-CdNS
				L5: Cds-CdSH
					L6: Cds-CdsSH
						L7: Cds-CdsS2H
							L8: Crds-CrdsS2rH
				L5: Cds-CdCH
					L6: Cds-CdsCsH
						L7: Crds-CrdsCrsH
						L7: Cds-CrdsCsH
						L7: Cds-CdsCrsH
					L6: Cds-CdsCdsH
						L7: Cds-Cd(Cd-O2d)H
							L8: Crds-Crd(Crd-O2d)H
						L7: Cds-Cd(Cd-N3d)H
							L8: Crds-Crd(Crd-N3rd)H
							L8: Cds-Cd(Crd-N3rd)H
						L7: Cds-Cd(Cd-N5dc)H
						L7: Cds-Cds(Cds-Cd)H
							L8: Cds-Cds(Cds-Cds)H
								L9: Crds-Crds(Crds-Crds)H
								L9: Crds-Crds(Crds-Cds)H
								L9: Cds-Cds(Crds-Crds)H
					L6: Cds-CdsCtH
						L7: Cds-CdsH(Ct-N3t)
						L7: Cds-CdsH(Ct-Ct)
					L6: Cds-CdsCbH
						L7: Crds-CrdsCbH
					L6: Cds-CddCH
				L5: Cds-CdCO
					L6: Cds-CdsCdsOs
						L7: Cds-Cds(Cds-O2d)O2s
							L8: Crds-Crds(Crds-O2d)O2s
								L9: Crds-Crds(Crds-O2d)(O2s-H)
								L9: Crds-Crds(Crds-O2d)(O2s-R)
							L8: Crds-Crds(Cds-O2d)O2rs
						L7: Cds-Cds(Cds-N3d)O2s
							L8: Cds-Cds(Cds-N3d)(O2s-H)
								L9: Crds-Crds(Crds-Nr3d)(O2s-H)
							L8: Cds-Cds(Cds-N3d)(O2s-R)
						L7: Cds-Cds(Cds-Cd)O2s
							L8: Cds-Cds(Cds-Cds)O2s
					L6: Cds-CdsCbOs
						L7: Crds-CrdsCbOrs
						L7: Crds-CrdsCbOs
					L6: Cds-CdCsOs
						L7: Cds-CdsCsOs
							L8: Crds-CrdsCsOrs
					L6: Cds-CdCtOs
						L7: Crds-CrdCtOrs
				L5: Cds-CdCS
					L6: Cds-CdsCsSs
						L7: Cds-CdsCsS2
							L8: Crds-CrdsCsS2r
					L6: Cds-CdsCdsSs
						L7: Cds-Cds(Cds-Cd)S2s
						L7: Cds-Cds(Cds-O2d)S2s
					L6: Cds-CdsCS6dd
				L5: Cds-CdCC
					L6: Cds-CdsCsCs
						L7: Crds-CrdsCrsCrs
						L7: Crds-CrdsCrsCs
						L7: Cds-CrdsCsCs
						L7: Cds-CdsCrsCs
					L6: Cds-CdsCdsCs
						L7: Cds-Cd(Cds-O2d)Cs
							L8: Crds-Crd(Crds-O2d)Cs
						L7: Cds-Cd(Cds-N3d)Cs
							L8: Crds-Crd(Crds-N3rd)Cs
						L7: Cds-Cds(Cds-Cd)Cs
							L8: Cds-Cds(Cds-Cds)Cs
								L9: Crds-Crds(Crds-Crds)Cs
								L9: Crds-Cds(Crds-Crds)Crs
					L6: Cds-CdsCdsCds
						L7: Cds-Cds(Cds-O2d)(Cds-O2d)
							L8: Crds-Crds(Crds-O2d)(Cds-O2d)
						L7: Cds-Cds(Cds-O2d)(Cds-Cd)
							L8: Cds-Cds(Cds-O2d)(Cds-Cds)
								L9: Crds-Crds(Cds-O2d)(Crds-Crds)
						L7: Cds-Cds(Cds-O2d)(Cds-N3d)
							L8: Crds-Crds(Crds-O2d)(Crds-N3rd)
							L8: Crds-Crds(Cds-O2d)(Crds-N3rd)
						L7: Cds-Cds(Cds-N3d)(Cds-N3d)
						L7: Cds-Cds(Cds-Cd)(Cds-N3d)
							L8: Crds-Crds(Crds-Crd)(Crds-N3rd)
						L7: Cds-Cds(Cds-Cd)(Cds-Cd)
							L8: Cds-Cds(Cds-Cds)(Cds-Cds)
					L6: Cds-CdsCtCs
						L7: Cds-CdCs(CtN3t)
					L6: Cds-CdsCtCds
					L6: Cds-CdsCtCt
						L7: Cds-Cd(CtN3t)(CtN3t)
					L6: Cds-CdsCbCs
						L7: Crds-CrdsCbCrs
						L7: Crds-CrdsCbCs
					L6: Cds-CdsCbCds
						L7: Cds-CdsCb(Cds-O2d)
							L8: Crds-CrdsCb(Crds-O2d)
						L7: Cds-CdsCb(Cds-N3d)
						L7: Cds-Cds(Cds-Cd)Cb
							L8: Cds-Cds(Cds-Cds)Cb
					L6: Cds-CdsCbCb
					L6: Cds-CddCC
						L7: Cds-(Cdd-Cd)CC
				L5: Cds-CdCN
					L6: Cds-CdCbN3s
					L6: Cds-CdCsN3s
					L6: Cds-CdCdsN3s
						L7: Cds-Cd(Cds-O2d)N3s
						L7: Cds-Cd(Cds-N3d)N3s
						L7: Cds-Cd(Cds-Cds)N3s
					L6: Cds-CdCbN3d
					L6: Cds-CdCsN3d
					L6: Cds-CdCdsN3d
					L6: Cds-CdCtN3d
					L6: Cds-CdCN5dc
			L4: Cds-Sd
				L5: Cds-S2dNN
				L5: Cds-S2dNC
				L5: Cds-S2dNS
				L5: Cds-S2dOC
		L3: Cs
			L4: Cs-P3s
				L5: Cs-P3sHHH
				L5: Cs-P3sRHH
					L6: Cs-P3sCsHH
			L4: Cs-P5d
				L5: Cs-P5dHHH
					L6: Cs-(P5d-O2d)HHH
				L5: Cs-P5dRHH
					L6: Cs-P5dNHH
						L7: Cs-P5dN3sHH
					L6: Cs-P5dCHH
						L7: Cs-P5dCsHH
					L6: Cs-P5dOsHH
				L5: Cs-P5dOCH
					L6: Cs-P5d(O-H)CH
				L5: Cs-P5dOCC
					L6: Cs-P5d(O-H)CC
				L5: Cs-P5dCCC
					L6: Cs-P5dCsCsCs
			L4: Cs-NHHH
				L5: Cs-N3sHHH
					L6: Cs-N3rsHHH
					L6: Cs-(N3s-RH)HHH
					L6: Cs-(N3s-RR)HHH
				L5: Cs-N3dHHH
					L6: Cs-(N3dCd)HHH
				L5: Cs-N5cHHH
			L4: Cs-NNHH
			L4: Cs-NOHH
				L5: Cs-N3sOHH
					L6: Cs-N3rsOHH
			L4: Cs-NSHH
			L4: Cs-NCHH
				L5: Cs-NCbHH
					L6: Crs-NrCbHH
					L6: Cs-NrCbHH
				L5: Cs-NCsHH
					L6: Cs-N3sCsHH
						L7: Crs-N3rsCrsHH
						L7: Cs-N3rsCsHH
					L6: Cs-N3dCHH
						L7: Cs-(N3d-Nd)CsHH
						L7: Cs-(N3d-Cd)CsHH
						L7: Cs-(N3d-Cdd)CsHH
					L6: Cs-N5cCsHH
				L5: Cs-NCdsHH
					L6: Cs-N(Cds-O2d)HH
						L7: Cs-N(Cds-O2d(OsH))HH
					L6: Cs-N(Cds-Cd)HH
					L6: Cs-N(Cds-N3d)HH
				L5: Cs-NCtHH
			L4: Cs-NNCH
			L4: Cs-NOCH
			L4: Cs-NSCH
			L4: Cs-NCCH
				L5: Cs-NCsCsH
					L6: Cs-N3sCsCsH
						L7: Crs-N3rsCrsCrsH
						L7: Crs-N3sCrsCrsH
						L7: Crs-N3rsCrsCsH
					L6: Cs-N3dCsCsH
					L6: Cs-N5dcCsCsH
				L5: Cs-NCsCdsH
					L6: Cs-NCs(Cds-O2d)H
					L6: Cs-NCs(Cds-Cd)H
			L4: Cs-NOCR
			L4: Cs-NCCC
				L5: Cs-NCsCsCs
					L6: Cs-N3CsCsCs
					L6: Cs-N5dcCsCsCs
				L5: Cs-NCdCbCb
					L6: Cs-N3s(Cd-O2d)CbCb
			L4: Cs-NNNN
				L5: Cs-N5dcN5dcN5dcN5dc
			L4: Cs-OsHHH
			L4: Cs-OsOsHH
				L5: Crs-OrsOrsHH
			L4: Cs-OsSHH
				L5: Cs-OsS2HH
			L4: Cs-OsOsOsH
			L4: Cs-OsOsOsCs
			L4: Cs-CHHH
				L5: Cs-CsHHH
				L5: Cs-CdsHHH
					L6: Cs-(Cds-O2d)HHH
					L6: Cs-(Cds-Cd)HHH
						L7: Cs-(Cds-Cds)HHH
						L7: Cs-(Cds-Cdd)HHH
							L8: Cs-(Cds-Cdd-Cd)HHH
					L6: Cs-(Cd-Nd)HHH
					L6: Cs-(Cd-S2d)SHHH
				L5: Cs-CtHHH
					L6: Cs-(Ct-Ct)HHH
				L5: Cs-CbHHH
			L4: Cs-CCHH
				L5: Crs-CrCrHH
					L6: Crs-CrsCrsHH
					L6: Crs-CrdsCrsHH
						L7: Crs-(Crds-Cd)CrsHH
							L8: Crs-(Crds-Crd)CrsHH
						L7: Crs-(Crds-O2d)CrsHH
						L7: Crs-(Crds-Nd)CrsHH
							L8: Crs-(Crds-Nrd)CrsHH
								L9: Crs-(Crds-N3rd)CrsHH
							L8: Crs-(Crds-N3d)CrsHH
					L6: Crs-CrdsCrdsHH
					L6: Crs-CbCrsHH
					L6: Crs-CbCrdsHH
					L6: Crs-CbCbHH
				L5: Cs-CsCsHH
				L5: Cs-CdsCsHH
					L6: Cs-(Cds-O2d)CsHH
					L6: Cs-(Cds-Cd)CsHH
						L7: Cs-(Cds-Cds)CsHH
						L7: Cs-(Cds-Cdd)CsHH
							L8: Cs-(Cds-Cdd-Cd)CsHH
					L6: Cs-(Cd-N3d)CsHH
					L6: Cs-(Cds-S2d)CsHH
				L5: Cs-CdsCdsHH
					L6: Cs-(Cds-O2d)(Cds-O2d)HH
					L6: Cs-(Cds-O2d)(Cds-Cd)HH
						L7: Cs-(Cds-O2d)(Cds-Cds)HH
					L6: Cs-(Cds-Cd)(Cds-Cd)HH
						L7: Cs-(Cds-Cds)(Cds-Cds)HH
				L5: Cs-CtCsHH
					L6: Cs-(Ct-N3t)CsHH
					L6: Cs-(Ct-Ct)CsHH
				L5: Cs-CtCdsHH
				L5: Cs-CtCtHH
					L6: Cs-(Ct-N3t)(Ct-N3t)HH
				L5: Cs-CbCsHH
				L5: Cs-CbCdsHH
					L6: Cs-(Cds-O2d)CbHH
					L6: Cs-(Cds-Cd)CbHH
						L7: Cs-(Cds-Cds)CbHH
					L6: Cs-(Cds-N3d)CbHH
				L5: Cs-CbCtHH
				L5: Cs-CbCbHH
			L4: Cs-CCCH
				L5: Crs-CrCrCrH
					L6: Crs-CrsCrsCrsH
					L6: Crs-CrdCrsCrsH
						L7: Crs-(Crd-Cd)CrsCrsH
							L8: Crs-(Crd-Crd)CrsCrsH
						L7: Crs-(Crd-O2d)CrsCrsH
					L6: Crs-CbCrsCrsH
					L6: Crs-CrdCrdCrsH
					L6: Crs-CbCrdCrsH
					L6: Crs-CbCrdCrdH
					L6: Crs-CbCbCrsH
				L5: Crs-CrCrCH
					L6: Crs-CrsCrsCsH
					L6: Crs-CrsCrsCdH
					L6: Crs-CrsCrsCtH
						L7: Crs-CrsCrs(Ct-N3t)H
						L7: Crs-CrsCrs(Ct-Ct)H
					L6: Crs-CrdCrsCsH
					L6: Crs-CrdCrsCdH
					L6: Crs-CrdCrdCsH
					L6: Crs-CrdCrdCdH
					L6: Crs-CbCrsCsH
					L6: Crs-CbCbCsH
				L5: Cs-CsCsCsH
				L5: Cs-CdsCsCsH
					L6: Cs-(Cds-O2d)CsCsH
					L6: Cs-(Cds-Cd)CsCsH
						L7: Cs-(Cds-Cds)CsCsH
					L6: Cs-(CdN3d)CsCsH
				L5: Cs-CtCsCsH
					L6: Cs-(Ct-N3t)CsCsH
					L6: Cs-(Ct-Ct)CsCsH
				L5: Cs-CbCsCsH
				L5: Cs-CdsCdsCsH
				L5: Cs-CbCdsCsH
					L6: Cs-(Cds-O2d)CbCsH
					L6: Cs-(Cds-Cd)CbCsH
						L7: Cs-(Cds-Cds)CbCsH
				L5: Cs-CbCbCsH
				L5: Cs-CbCdsCdsH
				L5: Cs-CbCbCdsH
					L6: Cs-CbCb(Cds-O2d)H
				L5: Cs-CbCbCbH
			L4: Cs-CCCC
				L5: Crs-CrCrCrCr
					L6: Crs-CrsCrsCrsCrs
					L6: Crs-CbCrsCrsCrs
					L6: Crs-CrdCrsCrsCrs
					L6: Crs-CbCrdCrsCrs
				L5: Crs-CrCrCrC
					L6: Crs-CrsCrsCrsCs
					L6: Crs-CbCrsCrsCs
					L6: Crs-CbCrsCrsCd
					L6: Crs-CbCrdCrsCd
					L6: Crs-CbCbCrsCs
					L6: Crs-CrsCrsCrsCd
						L7: Crs-CrsCrsCrs(Cd-O2d)
					L6: Crs-CrdCrsCrsCs
						L7: Crs-(Crd-O2d)CrsCrsCs
						L7: Crs-(Crd-Cd)CrsCrsCs
							L8: Crs-(Crd-Crd)CrsCrsCs
					L6: Crs-CrdCrdCrsCs
					L6: Crs-CrdCrdCbCs
					L6: Crs-CrdCrdCrdCs
				L5: Crs-CrCrCC
					L6: Crs-CrsCrsCsCs
					L6: Crs-CbCrsCsCs
					L6: Crs-CrdCrsCsCs
					L6: Crs-CrdCrdCsCs
						L7: Crs-(Crd-O2d)(Crd-O2d)CsCs
					L6: Crs-CrdCrdCdCs
						L7: Crs-(Crd-O2d)(Crd-O2d)CdCs
					L6: Crs-CrsCrsCdCs
				L5: Cs-CsCsCsCs
				L5: Cs-CdsCsCsCs
					L6: Cs-(Cds-O2d)CsCsCs
					L6: Cs-(Cds-Cd)CsCsCs
						L7: Cs-(Cds-Cds)CsCsCs
				L5: Cs-CtCsCsCs
				L5: Cs-CbCsCsCs
				L5: Cs-CdsCdsCsCs
				L5: Cs-CbCtCsCs
				L5: Cs-CbCbCsCs
				L5: Cs-CbCdsCdsCs
					L6: Cs-(Cds-O2d)(Cds-Cd)CbCs
						L7: Cs-(Cds-O2d)(Cds-Cds)CbCs
							L8: Cs-(Cds-O2d)(Crds-Crds)CbCs
				L5: Cs-CbCbCdsCs
					L6: Cs-(Cds-O2d)CbCbCs
				L5: Cs-CbCbCbCb
			L4: Cs-CCCOs
				L5: Cs-CsCsCsOs
					L6: Cs-CsCsCs(Os-H)
						L7: Crs-CrsCrsCrs(Os-H)
						L7: Crs-CrsCrsCs(Os-H)
					L6: Cs-CsCsCs(Os-R)
						L7: Crs-CrsCrsCrs(Ors-R)
						L7: Crs-CrsCrsCs(Ors-R)
						L7: Crs-CrsCrsCs(Os-R)
						L7: Crs-CrsCsCs(Ors-R)
				L5: Cs-CdsCsCsOs
					L6: Cs-CdsCsCs(Os-H)
						L7: Cs-(Cds-O2d)CsCs(Os-H)
							L8: Crs-(Cds-O2d)CrsCrs(Os-H)
						L7: Cs-(Cds-Cd)CsCs(Os-H)
					L6: Cs-CdsCsCs(Os-R)
						L7: Cs-(Cds-O2d)CsCs(Os-R)
						L7: Cs-(Cds-Cd)CsCs(Os-R)
				L5: Cs-OsCtCsCs
				L5: Cs-CbCsCsOs
				L5: Cs-CdsCdsCsOs
					L6: Cs-(Cds-O2d)(Cds-Cd)CsOs
						L7: Cs-(Cds-O2d)(Cds-Cds)CsOs
				L5: Cs-CtCdsCsOs
					L6: Cs-(Cds-Cd)CtCsOs
						L7: Cs-(Cds-Cds)CtCsOs
				L5: Cs-CbCdsCsOs
				L5: Cs-CbCbCsOs
				L5: Cs-CbCbCdsOs
					L6: Cs-(Cds-O2d)CbCbOs
				L5: Cs-CbCbCbOs
			L4: Cs-CCOsOs
				L5: Crs-CCOsOs
					L6: Crs-OrsOrsCC
					L6: Crs-CrOrsOsC
				L5: Cs-CsCsOsOs
			L4: Cs-COsOsH
				L5: Crs-COsOsH
					L6: Crs-OrsOrsCH
					L6: Crs-CrOrsOsH
				L5: Cs-CsOsOsH
			L4: Cs-COsSH
				L5: Cs-CsOsSH
					L6: Cs-CsOsS2H
			L4: Cs-CCOsH
				L5: Cs-CsCsOsH
					L6: Cs-CsCs(Os-H)H
						L7: Crs-CrsCrs(Os-H)H
					L6: Cs-CsCs(Os-R)H
						L7: Crs-CrsCrs(Ors-R)H
						L7: Crs-CrsCs(Ors-R)H
						L7: Crs-CrsCrs(Os-R)H
				L5: Cs-CdsCsOsH
					L6: Cs-(Cds-O2d)CsOsH
						L7: Cs-(Cds-O2d)Cs(Os-H)H
						L7: Cs-(Cds-O2d)Cs(Os-R)H
					L6: Cs-(Cds-Cd)CsOsH
						L7: Cs-(Cds-Cds)CsOsH
							L8: Cs-(Cds-Cds)Cs(Os-H)H
							L8: Cs-(Cds-Cds)Cs(Os-R)H
				L5: Cs-CtCsOsH
				L5: Cs-CbCsOsH
				L5: Cs-CbCdsOsH
					L6: Cs-(Cds-O2d)CbOsH
				L5: Cs-CbCbOsH
			L4: Cs-COsHH
				L5: Cs-CsOsHH
					L6: Cs-Cs(Os-H)HH
					L6: Cs-Cs(Os-R)HH
						L7: Crs-Crs(Ors-R)HH
				L5: Cs-CdsOsHH
					L6: Cs-(Cds-O2d)OsHH
						L7: Cs-(Cds-O2d)(Os-H)HH
						L7: Cs-(Cds-O2d)(Os-R)HH
					L6: Cs-(Cds-Cd)OsHH
						L7: Cs-(Cds-Cds)OsHH
							L8: Cs-(Cds-Cds)(Os-H)HH
							L8: Cs-(Cds-Cds)(Os-R)HH
					L6: Cs-(Cds-Nd)OsHH
						L7: Cs-(Cds-N3d)OsHH
				L5: Cs-CtOsHH
					L6: Cs-Ct(Os-H)HH
					L6: Cs-Ct(Os-R)HH
				L5: Cs-CbOsHH
					L6: Cs-Cb(Os-H)HH
					L6: Cs-Cb(Os-R)HH
			L4: Cs-CCCS
				L5: Cs-CCC(S-H)
			L4: Cs-CCSS
				L5: Cs-CsCsSS
			L4: Cs-CCSH
				L5: Cs-CsCsSH
					L6: Cs-CsCs(S-H)H
			L4: Cs-CSHH
				L5: Crs-CrSrHH
				L5: Cs-CsSHH
					L6: Cs-CsS2HH
						L7: Cs-Cs(S2-H)HH
					L6: Cs-CsS4HH
					L6: Cs-CsS6HH
				L5: Cs-CdsSsHH
					L6: Cs-(Cds-Cd)SsHH
						L7: Cs-(Cds-Cds)SsHH
					L6: Cs-(Cds-Od)SsHH
				L5: Cs-CbSsHH
				L5: Cs-CS4dHH
			L4: Cs-SsHHH
				L5: Cs-S2sHHH
				L5: Cs-S4HHH
				L5: Cs-S6HHH
			L4: Cs-SsSsHH
	L2: O
		L3: O2d
			L4: O2d-Cd
				L5: O2d-Crd
			L4: O2d-Cdd
			L4: O2d-N3d
			L4: O2d-N5dc
			L4: O2d-Sd
				L5: O2d-S4d
				L5: O2d-S6dd
			L4: O2d-P5d
		L3: O2s
			L4: O2s-PH
				L5: O2s-P5dH
			L4: O2s-PC
				L5: O2s-P3sC
					L6: O2s-P3sCs
				L5: O2s-P5dC
					L6: O2s-P5dCs
					L6: O2s-P5dCd
						L7: O2s-P5d(Cd-Nd)
					L6: O2s-P5dCb
			L4: O2s-NH
			L4: O2s-NR
				L5: O2s-CN
					L6: O2s-CbN3d
					L6: O2s-CsN3s
					L6: O2s-CsN3d
						L7: O2s-Cs(N3d-Od)
						L7: O2s-Cs(N3d-Cd)
					L6: O2s-CdN3d
					L6: O2s-CsN5dc
			L4: O2s-OsH
			L4: O2s-CH
				L5: O2s-CdsH
					L6: O2s-(Cds-O2d)H
					L6: O2s-(Cds-Cd)H
				L5: O2s-CsH
				L5: O2s-CbH
			L4: O2s-OsC
				L5: O2s-OsCds
					L6: O2s-O2s(Cds-O2d)
				L5: O2s-OsCs
			L4: O2s-CC
				L5: O2s-CtCb
					L6: O2s-(Ct-N3t)Cb
				L5: O2s-CdsCds
					L6: O2s-(Cds-O2d)(Cds-O2d)
					L6: O2s-(Cds-O2d)(Cds-Cd)
					L6: O2s-(Cds-Cd)(Cds-Cd)
				L5: O2s-CdsCs
					L6: O2s-Cs(Cds-N3d)
					L6: O2s-Cs(Cds-O2d)
					L6: O2s-Cs(Cds-Cd)
					L6: O2s-Cs(Cds-Sd)
				L5: O2s-CdsCb
					L6: O2s-Cb(Cds-N3d)
					L6: O2s-Cb(Cds-O2d)
					L6: O2s-Cb(Cds-Cd)
					L6: O2s-Cb(Cds-Sd)
				L5: O2s-CsCs
					L6: O2rs-CrsCrs
				L5: O2s-CsCb
					L6: O2rs-CrsCb
				L5: O2s-CbCb
					L6: O2rs-CbCb
			L4: O2s-CS
			L4: O2s-SH
				L5: O2s-S_DeH
		L3: Oc
			L4: Oc-N5c
	L2: S
		L3: S2d
			L4: S2d-C
			L4: S2d-P
				L5: S2d-P5d
		L3: S2s
			L4: S2s-CH
				L5: S2s-CsH
				L5: S2s-CdH
				L5: S2s-CbH
			L4: S2s-PH
				L5: S2s-P5dH
			L4: S2s-PC
				L5: S2s-P5dC
			L4: S2s-SS
				L5: S2s-SsSs
			L4: S2s-SC
				L5: S2s-S2sC
				L5: S2s-S46C
			L4: S2s-NN
				L5: S2s-N3dN3d
			L4: S2s-NC
				L5: S2s-N3dCd
			L4: S2s-CC
				L5: S2s-CsCs
					L6: S2rs-CrsCrs
				L5: S2s-CsCd
				L5: S2s-Cs(C=O)
				L5: S2s-CsCt
				L5: S2s-CsCb
				L5: S2s-CdCd
					L6: S2rs-CrdCrd
				L5: S2s-CdCb
					L6: S2rs-CrdCb
				L5: S2s-CtCb
					L6: S2s-(Ct-N3t)Cb
				L5: S2s-CbCb
					L6: S2rs-CbCb
				L5: S2s-(Cd-S2d)C
		L3: S4dd
			L4: S4dd-N3dN3d
		L3: S4d
			L4: S4d-Od
				L5: S4d-OdCC
					L6: S4d-OdCsCs
					L6: S4d-OdCsCb
					L6: S4d-OdCbCb
				L5: S4d-OdCS
		L3: S6dd
			L4: S6dd-OdOd
				L5: S6dd-OdOdCC
					L6: S6dd-OdOdCbCb
					L6: S6dd-OdOdCrCr
					L6: S6dd-OdOdCsCs
					L6: S6dd-OdOdCsCb
				L5: S6dd-OdOdCO
					L6: S6dd-OdOdCsOs
					L6: S6dd-OdOdCbOs
				L5: S6dd-OdOdNC
					L6: S6dd-OdOdNCb
				L5: S6dd-OdOdNN
				L5: S6dd-OdOdOO
				L5: S6dd-OdOdON
	L2: N
		L3: N1dc
			L4: N1dc-N5ddc
		L3: N3s
			L4: N3s-CHH
				L5: N3s-CsHH
					L6: N3s-CrsHH
				L5: N3s-CbHH
				L5: N3s-CdHH
					L6: N3s-(Cd-Cd)HH
						L7: N3s-(Crd-Crd)HH
					L6: N3s-(Cd-N3d)HH
						L7: N3s-(Crd-N3rd)HH
					L6: N3s-(Cd-O2d)HH
					L6: N3s-(Cd-Sd)HH
			L4: N3s-NHH
				L5: N3s-N3sHH
			L4: N3s-SHH
				L5: N3s-S6ddHH
			L4: N3s-NNH
			L4: N3s-PCH
				L5: N3s-P5dCH
			L4: N3s-NCH
				L5: N3s-N3sCsH
				L5: N3s-N3sCbH
				L5: N3s-N3sCdH
				L5: N3s-N3dCsH
				L5: N3s-N3dCbH
				L5: N3s-N3dCdH
					L6: N3rs-N3rdCrdH
						L7: N3rs-N3rd(Crd-O2d)H
						L7: N3rs-N3rd(Crd-Cd)H
						L7: N3rs-N3rd(Crd-Nd)H
					L6: N3s-N3d(Cd-O2d)H
			L4: N3s-PCC
			L4: N3s-NCC
				L5: N3rs-NrCrCr
					L6: N3rs-NrCrCb
						L7: N3rs-Nr(Crd-O2d)Cb
				L5: N3rs-NrCrC
				L5: N3rs-NCrCr
					L6: N3rs-N3dCrCr
						L7: N3rs-(N3d-O2d)CrCr
					L6: N3rs-N5dcCrCr
				L5: N3s-N3dCC
					L6: N3s-(N3d-O2d)CC
						L7: N3s-(N3d-O2d)CsCs
						L7: N3s-(N3d-O2d)CbCs
						L7: N3s-(N3d-O2d)CbCb
			L4: N3s-NNC
				L5: N3rs-NrNrC
			L4: N3s-NNO
				L5: N3rs-NrNrO
					L6: N3rs-N3rdN3rdO
						L7: N3rs-N3rdN3rd(O2s-H)
			L4: N3s-CCH
				L5: N3s-CsCsH
					L6: N3rs-CrsCrsH
				L5: N3s-CbCsH
					L6: N3rs-CbCrsH
				L5: N3s-CbCbH
					L6: N3rs-CbCbH
				L5: N3s-CdCsH
					L6: N3s-(Cd-Cd)CsH
					L6: N3s-(Cd-N3d)CsH
						L7: N3rs-(Crd-N3rd)CrsH
					L6: N3s-(Cd-O2d)CsH
					L6: N3s-(Cd-Sd)CsH
				L5: N3s-CdCtH
					L6: N3s-(Cd-N3d)CtH
						L7: N3s-(Cd-N3d)(Ct-N3t)H
				L5: N3s-CdCbH
					L6: N3s-(Cd-Cd)CbH
						L7: N3rs-(Crd-Crd)CbH
						L7: N3s-(Crd-Crd)CbH
					L6: N3s-(Cd-N3d)CbH
						L7: N3rs-(Crd-N3rd)CbH
						L7: N3s-(Crd-N3rd)CbH
					L6: N3s-(Cd-O2d)CbH
					L6: N3s-(Cd-Sd)CbH
				L5: N3s-CdCdH
					L6: N3s-(Cd-Cd)(Cd-Cd)H
						L7: N3rs-(Crd-Crd)(Crd-Crd)H
					L6: N3s-(Cd-N3d)(Cd-Cd)H
						L7: N3rs-(Crd-N3rd)(Crd-Crd)H
					L6: N3s-(Cd-O2d)(Cd-Cd)H
						L7: N3rs-(Crd-O2d)(Crd-Crd)H
						L7: N3s-(Cd-O2d)(Crd-Crd)H
					L6: N3s-(Cd-Sd)(Cd-Cd)H
						L7: N3rs-(Crd-Sd)(Crd-Crd)H
					L6: N3s-(Cd-O2d)(Cd-O2d)H
						L7: N3rs-(Crd-O2d)(Crd-O2d)H
					L6: N3s-(Cd-O2d)(Cd-N3d)H
						L7: N3rs-(Crd-O2d)(Crd-N3rd)H
						L7: N3s-(Cd-O2d)(Crd-N3rd)H
					L6: N3s-(Cd-O2d)(Cd-Sd)H
						L7: N3rs-(Crd-O2d)(Crd-Sd)H
			L4: N3s-COH
			L4: N3s-CSH
				L5: N3s-CS6ddH
					L6: N3s-CbS6ddH
					L6: N3s-CrS6ddH
						L7: N3s-CrdS6ddH
					L6: N3s-CdS6ddH
						L7: N3s-(Cd-O2d)S6ddH
					L6: N3s-CsS6ddH
			L4: N3s-CCC
				L5: N3s-CsCsCs
					L6: N3rs-CrsCrsCrs
					L6: N3rs-CrsCrsCs
				L5: N3s-CbCsCs
				L5: N3s-CbCdCd
					L6: N3s-Cb(Cd-O2d)(Cd-Cd)
						L7: N3rs-Cb(Cd-O2d)(Crd-Crd)
				L5: N3s-CbCbCs
					L6: N3rs-CbCbCs
				L5: N3s-CbCbCd
					L6: N3s-CbCb(Cd-O2d)
				L5: N3s-CbCbCb
				L5: N3s-CdCsCs
					L6: N3s-(Cd-N3d)CsCs
						L7: N3rs-(Crd-N3rd)CrsCrs
						L7: N3s-(Crd-N3rd)CsCs
					L6: N3s-(Cd-O2d)CsCs
						L7: N3rs-(Crd-O2d)CrsCrs
						L7: N3rs-(Cd-O2d)CrsCrs
						L7: N3rs-(Crd-O2d)CrsCs
					L6: N3s-(Cd-Cd)CsCs
						L7: N3rs-(Crd-Crd)CrsCs
						L7: N3s-(Crd-Crd)CsCs
					L6: N3s-(Cd-Sd)CsCs
				L5: N3s-CdCbCs
					L6: N3s-(Cd-O2d)CbCs
						L7: N3rs-(Crd-O2d)CbCrs
						L7: N3rs-(Crd-O2d)CbCs
						L7: N3rs-(Cd-O2d)CbCrs
					L6: N3s-(Cd-Cd)CbCs
						L7: N3rs-(Crd-Crd)CbCs
					L6: N3s-(Cd-Nd)CbCs
						L7: N3rs-(Crd-Nrd)CbCs
					L6: N3s-(Cd-S2d)CbCs
				L5: N3s-CdCdCs
					L6: N3s-(Cd-O2d)(Cd-O2d)Cs
						L7: N3rs-(Crd-O2d)(Crd-O2d)Cs
						L7: N3rs-(Crd-O2d)(Cd-O2d)Crs
					L6: N3s-(Cd-O2d)(Cd-Cd)Cs
						L7: N3rs-(Crd-O2d)(Crd-Crd)Cs
					L6: N3s-(Cd-O2d)(Cd-Nd)Cs
						L7: N3rs-(Crd-O2d)(Crd-Nrd)Cs
					L6: N3s-(Cd-Cd)(Cd-Cd)Cs
						L7: N3rs-(Crd-Crd)(Crd-Crd)Cs
					L6: N3s-(Cd-Cd)(Cd-Nd)Cs
						L7: N3rs-(Crd-Crd)(Crd-Nrd)Cs
					L6: N3s-(Cd-Cd)(Cd-S2d)Cs
						L7: N3rs-(Crd-Crd)(Crd-S2d)Cs
					L6: N3s-(Cd-Nd)(Cd-Nd)Cs
						L7: N3rs-(Crd-Nrd)(Crd-Nrd)Cs
				L5: N3s-CdCdCd
					L6: N3s-(Cd-O2d)(Cd-Cd)(Cd-Nd)
			L4: N3s-CCO
				L5: N3s-CbCd(O-H)
					L6: N3s-Cb(Cd-O2d)(O-H)
			L4: N3s-CCS
				L5: N3s-CCS4d
					L6: N3s-CC(S4d-O2d)
						L7: N3s-CsCs(S4d-O2d)
				L5: N3s-CCS6dd
					L6: N3s-CC(S6dd-O2dO2d)
						L7: N3s-CsCs(S6dd-O2dO2d)
						L7: N3s-CsCd(S6dd-O2dO2d)
							L8: N3s-Cs(Cd-Cd)(S6dd-O2dO2d)
						L7: N3s-CbCb(S6dd-O2dO2d)
		L3: N3d
			L4: N3d-N5ddc
			L4: N3d-CdH
			L4: N3d-CdN
				L5: N3d-CdN3s
				L5: N3d-CdN3d
					L6: N3rd-CrdN3rd
			L4: N3d-CdO
				L5: N3d-Cd(O-H)
				L5: N3d-Cd(O-R)
					L6: N3rd-Crd(Or-R)
			L4: N3d-CdS
				L5: N3d-CdS2s
					L6: N3rd-CrdS2rs
				L5: N3d-CdS6dd
			L4: N3d-CdC
				L5: N3d-CdCs
					L6: N3rd-CrdCrs
				L5: N3d-CdCb
					L6: N3rd-CrdCb
				L5: N3d-CdCd
					L6: N3d-Cd(Cd-O2d)
						L7: N3rd-Crd(Crd-O2d)
					L6: N3d-Cd(Cd-N3d)
						L7: N3rd-Crd(Crd-N3rd)
						L7: N3d-Cd(Crd-N3rd)
					L6: N3d-Cd(Cd-Cd)
						L7: N3rd-Crd(Crd-Crd)
				L5: N3d-CdCt
					L6: N3d-Cd(Ct-N3t)
			L4: N3d-CddC
				L5: N3d-(Cdd-O2d)C
					L6: N3d-(Cdd-O2d)Cs
					L6: N3d-(Cdd-O2d)Cb
				L5: N3d-(Cdd-Sd)C
					L6: N3d-(Cdd-S2d)C
						L7: N3d-(Cdd-S2d)Cs
						L7: N3d-(Cdd-S2d)Cb
			L4: N3d-N3dN
				L5: N3d-N3dN3s
					L6: N3rd-N3rdN3rs
				L5: N3d-N3dN3d
					L6: N3d-N3d(N3d-Cd)
						L7: N3rd-N3rd(N3rd-Crd)
			L4: N3d-N3dC
				L5: N3d-N3dCb
				L5: N3d-N3dCs
				L5: N3d-N3dCd
			L4: N3d-O2dO
			L4: N3d-O2dN
				L5: N3d-O2dN3s
			L4: N3d-O2dC
				L5: N3d-O2dCb
			L4: N3d-SdS
				L5: N3d-S4ddS2s
					L6: N3d-(S4dd-N3d)S2s
			L4: N3d-PdP
				L5: N3d-P5dP5d
		L3: N3t
			L4: N3t-Ct
		L3: N5sc
			L4: N5sc-O0sc
		L3: N5dc
			L4: N5dc-OdO0scC
				L5: N5dc-OdO0scCb
				L5: N5dc-OdO0scCs
				L5: N5dc-OdO0scCd
					L6: N5dc-OdO0sc(Cd-Cd)
						L7: N5dc-OdO0sc(Crd-Crd)
					L6: N5dc-OdO0sc(Cd-Nd)
						L7: N5dc-OdO0sc(Crd-N3rd)
			L4: N5dc-OdO0scO2s
			L4: N5dc-OdO0scN
			L4: N5dc-CdO0scC
				L5: N5dc-CdO0scCd
					L6: N5dc-CdO0sc(Cd-Cd)
						L7: N5dc-CdO0sc(Crd-Crd)
		L3: N5ddc
			L4: N5ddc-N1dcN3d
		L3: N5tc
			L4: N5tc-C2tcC
				L5: N5tc-C2tcCs
				L5: N5tc-C2tcCb
	L2: P
		L3: P3s
			L4: P3s-O2sO2sO2s
			L4: P3s-CCC
				L5: P3s-CsCsCs
				L5: P3s-CbCbCb
		L3: P5d
			L4: P5d-O2d
				L5: P5d-O2dO2sCH
				L5: P5d-O2dO2sO2sH
				L5: P5d-O2dNNN
					L6: P5d-O2dN3sN3sN3s
				L5: P5d-O2dCCC
					L6: P5d-O2dCbCbCb
					L6: P5d-O2dCsCsCs
				L5: P5d-O2dO2sCC
					L6: P5d-O2dO2sCbCb
					L6: P5d-O2dO2sCbCs
					L6: P5d-O2dO2sCsCs
				L5: P5d-O2dO2sO2sN
					L6: P5d-O2dO2sO2sN3s
				L5: P5d-O2dO2sO2sC
					L6: P5d-O2dO2sO2sCs
					L6: P5d-O2dO2sO2sCd
				L5: P5d-O2dO2sO2sO2s
			L4: P5d-N3d
				L5: P5d-N3dNHH
					L6: P5d-N3dN3dHH
				L5: P5d-N3dNOO
					L6: P5d-N3dN3dO2sO2s
			L4: P5d-S2d
				L5: P5d-S2dO2sO2sS
					L6: P5d-S2dO2sO2sS2s
				L5: P5d-S2dO2sO2sO2s
"""
)
