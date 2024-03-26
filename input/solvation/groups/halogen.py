#!/usr/bin/env python
# encoding: utf-8

name = "halogen"
shortDesc = u""
longDesc = u""" 
All groups are fitted using experimental solute parameter data unless written otherwise.
See Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
"""

entry(
	index = 1,
	label = "X",
	group = 
"""
1 * [F1s,Cl1s,Br1s,I1s] ux
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
	label = "F",
	group = 
"""
1 * F1s u0
""",
	solute = u'F-C',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 3,
	label = "F-C",
	group = 
"""
1 * F1s u0 {2,S}
2   C   u0 {1,S}
""",
	solute = u'F-Cs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 4,
	label = "F-Cb",
	group = 
"""
1 * F1s u0 {2,S}
2   Cb  u0 {1,S}
""",
	solute = SoluteData(
		S = -0.02870,
		B = -0.01608,
		E = -0.10588,
		L = -0.12204,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 135,
		B = 131,
		E = 146,
		L = 104,
		A = 150,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 5,
	label = "F-Phenol",
	group =  "OR{F-Phenol(ortho), F-Phenol(meta), F-Phenol(para)}",
	solute = None,
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 6,
	label = "F-Phenol(ortho)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cb  u0 {1,S} {3,B}
3   Cb  u0 {2,B} {4,S}
4   O2s u0 {3,S} {5,S}
5   H   u0 {4,S}
""",
	solute = SoluteData(
		S = -0.01903,
		B = -0.03461,
		E = -0.10427,
		L = -0.12259,
		A = 0.09756,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 5,
		E = 8,
		L = 5,
		A = 7,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 7,
	label = "F-Phenol(meta)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cb  u0 {1,S} {3,B}
3   Cb  u0 {2,B} {4,B}
4   Cb  u0 {3,B} {5,S}
5   O2s u0 {4,S} {6,S}
6   H   u0 {5,S}
""",
	solute = SoluteData(
		S = 0.02174,
		B = -0.03645,
		E = -0.09013,
		L = -0.02170,
		A = 0.07464,
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
	index = 8,
	label = "F-Phenol(para)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cb  u0 {1,S} {3,B}
3   Cb  u0 {2,B} {4,B}
4   Cb  u0 {3,B} {5,B}
5   Cb  u0 {4,B} {6,S}
6   O2s u0 {5,S} {7,S}
7   H   u0 {6,S}
""",
	solute = SoluteData(
		S = -0.00778,
		B = -0.02958,
		E = -0.09518,
		L = -0.13622,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 4,
		B = 4,
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
	index = 9,
	label = "F-BenzoicAcid",
	group =  "OR{F-BenzoicAcid(ortho), F-BenzoicAcid(meta), F-BenzoicAcid(para)}",
	solute = None,
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 10,
	label = "F-BenzoicAcid(ortho)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cb  u0 {1,S} {3,B}
3   Cb  u0 {2,B} {4,S}
4   CO  u0 {3,S} {5,S}
5   O2s u0 {4,S} {6,S}
6   H   u0 {5,S}
""",
	solute = SoluteData(
		S = -0.01126,
		B = 0.00000,
		E = -0.07247,
		L = -0.04312,
		A = 0.07852,
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
	index = 11,
	label = "F-BenzoicAcid(meta)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cb  u0 {1,S} {3,B}
3   Cb  u0 {2,B} {4,B}
4   Cb  u0 {3,B} {5,S}
5   CO  u0 {4,S} {6,S}
6   O2s u0 {5,S} {7,S}
7   H   u0 {6,S}
""",
	solute = SoluteData(
		S = -0.05665,
		B = 0.00000,
		E = -0.07247,
		L = -0.11925,
		A = 0.05052,
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
	index = 12,
	label = "F-BenzoicAcid(para)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cb  u0 {1,S} {3,B}
3   Cb  u0 {2,B} {4,B}
4   Cb  u0 {3,B} {5,B}
5   Cb  u0 {4,B} {6,S}
6   CO  u0 {5,S} {7,S}
7   O2s u0 {6,S} {8,S}
8   H   u0 {7,S}
""",
	solute = SoluteData(
		S = -0.04977,
		B = 0.01219,
		E = -0.04977,
		L = -0.11742,
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
	index = 13,
	label = "F-Aniline",
	group =  "OR{F-Aniline(ortho), F-Aniline(meta), F-Aniline(para)}",
	solute = None,
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 14,
	label = "F-Aniline(ortho)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cb  u0 {1,S} {3,B}
3   Cb  u0 {2,B} {4,S}
4   N3s u0 {3,S} {5,S} {6,S}
5   H   u0 {4,S}
6   H   u0 {4,S}
""",
	solute = SoluteData(
		S = -0.00377,
		B = -0.00166,
		E = -0.18386,
		L = -0.20968,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 4,
		B = 2,
		E = 6,
		L = 4,
		A = 4,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 15,
	label = "F-Aniline(meta)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cb  u0 {1,S} {3,B}
3   Cb  u0 {2,B} {4,B}
4   Cb  u0 {3,B} {5,S}
5   N3s u0 {4,S} {6,S} {7,S}
6   H   u0 {5,S}
7   H   u0 {5,S}
""",
	solute = SoluteData(
		S = 0.03842,
		B = -0.00651,
		E = -0.17201,
		L = -0.14335,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 1,
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
	index = 16,
	label = "F-Aniline(para)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cb  u0 {1,S} {3,B}
3   Cb  u0 {2,B} {4,B}
4   Cb  u0 {3,B} {5,B}
5   Cb  u0 {4,B} {6,S}
6   N3s u0 {5,S} {7,S} {8,S}
7   H   u0 {6,S}
8   H   u0 {6,S}
""",
	solute = SoluteData(
		S = 0.02190,
		B = -0.00166,
		E = -0.14880,
		L = -0.13381,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 4,
		B = 2,
		E = 6,
		L = 4,
		A = 4,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 17,
	label = "F-Cs",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S}
""",
	solute = u'F-(Cs-CZZ)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 18,
	label = "F-(Cs-CZZ)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   C   u0 {2,S}
4   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = u'F-(Cs-CsZZ)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 19,
	label = "F-(Cs-CbZZ)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cb  u0 {2,S}
4   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = u'F-(Cs-CbHH)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 20,
	label = "F-(Cs-CbHH)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cb  u0 {2,S}
4   H   u0 {2,S}
5   H   u0 {2,S}
""",
	solute = SoluteData(
		S = 0.00829,
		B = 0.01872,
		E = -0.01612,
		L = 0.17940,
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
	index = 21,
	label = "F-(Cs-CbXX)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cb  u0 {2,S}
4   [F1s,Cl1s,Br1s,I1s]  u0 {2,S}
5   [F1s,Cl1s,Br1s,I1s]  u0 {2,S}
""",
	solute = u'F-(Cs-CbFF)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 22,
	label = "F-(Cs-CbFF)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cb  u0 {2,S}
4   F1s u0 {2,S}
5   F1s u0 {2,S}
""",
	solute = SoluteData(
		S = -0.04570,
		B = -0.02828,
		E = -0.11707,
		L = -0.13339,
		A = 0.02420,
	),
	dataCount = DataCountGAV(
		S = 49,
		B = 48,
		E = 54,
		L = 41,
		A = 54,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 23,
	label = "F-(Cs-CsZZ)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = u'F-(Cs-CsHH)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 24,
	label = "F-(Cs-CsHH)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   H   u0 {2,S}
5   H   u0 {2,S}
""",
	solute = SoluteData(
		S = 0.24834,
		B = 0.07507,
		E = -0.09938,
		L = 0.13316,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 26,
		B = 26,
		E = 27,
		L = 26,
		A = 27,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 25,
	label = "F-(Cs-(Cs-ZZZ)HH)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S} {7,S} {8,S}
4   H   u0 {2,S}
5   H   u0 {2,S}
6   [H,F1s,Cl1s,Br1s,I1s] u0 {3,S}
7   [H,F1s,Cl1s,Br1s,I1s] u0 {3,S}
8   [H,F1s,Cl1s,Br1s,I1s] u0 {3,S}
""",
	solute = u'F-(Cs-(Cs-HHH)HH)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 26,
	label = "F-(Cs-(Cs-HHH)HH)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S} {7,S} {8,S}
4   H   u0 {2,S}
5   H   u0 {2,S}
6   H   u0 {3,S}
7   H   u0 {3,S}
8   H   u0 {3,S}
""",
	solute = SoluteData(
		S = 0.04250,
		B = 0.01250,
		E = 0.01733,
		L = -0.18090,
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
	index = 27,
	label = "F-(Cs-(Cs-HHX)HH)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S} {7,S} {8,S}
4   H   u0 {2,S}
5   H   u0 {2,S}
6   H   u0 {3,S}
7   H   u0 {3,S}
8   [F1s,Cl1s,Br1s,I1s] u0 {3,S}
""",
	solute = SoluteData(
		S = 0.06504,
		B = 0.02047,
		E = -0.01277,
		L = 0.04968,
		A = 0.01096,
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
	label = "F-(Cs-(Cs-HXX)HH)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S} {7,S} {8,S}
4   H   u0 {2,S}
5   H   u0 {2,S}
6   H   u0 {3,S}
7   [F1s,Cl1s,Br1s,I1s] u0 {3,S}
8   [F1s,Cl1s,Br1s,I1s] u0 {3,S}
""",
	solute = SoluteData(
		S = 0.00253,
		B = 0.01809,
		E = -0.04537,
		L = -0.18993,
		A = 0.01554,
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
	index = 29,
	label = "F-(Cs-(Cs-XXX)HH)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S} {7,S} {8,S}
4   H   u0 {2,S}
5   H   u0 {2,S}
6   [F1s,Cl1s,Br1s,I1s] u0 {3,S}
7   [F1s,Cl1s,Br1s,I1s] u0 {3,S}
8   [F1s,Cl1s,Br1s,I1s] u0 {3,S}
""",
	solute = SoluteData(
		S = 0.00963,
		B = 0.00000,
		E = -0.09316,
		L = -0.29943,
		A = 0.00480,
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
	index = 30,
	label = "F-(Cs-(Cs-(OH))HH)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S}
4   H   u0 {2,S}
5   H   u0 {2,S}
6   O2s u0 {3,S} {7,S}
7   H   u0 {6,S}
""",
	solute = None,
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 31,
	label = "F-(Cs-CsXH)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   [F1s,Cl1s,Br1s,I1s] u0 {2,S}
5   H   u0 {2,S}
""",
	solute = u'F-(Cs-CsFH)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 32,
	label = "F-(Cs-(Cs-ZZZ)XH)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S} {7,S} {8,S}
4   [F1s,Cl1s,Br1s,I1s]   u0 {2,S}
5   H   u0 {2,S}
6   [H,F1s,Cl1s,Br1s,I1s] u0 {3,S}
7   [H,F1s,Cl1s,Br1s,I1s] u0 {3,S}
8   [H,F1s,Cl1s,Br1s,I1s] u0 {3,S}
""",
	solute = u'F-(Cs-(Cs-HHH)XH)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 33,
	label = "F-(Cs-(Cs-HHH)XH)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S} {7,S} {8,S}
4   [F1s,Cl1s,Br1s,I1s]   u0 {2,S}
5   H   u0 {2,S}
6   H   u0 {3,S}
7   H   u0 {3,S}
8   H   u0 {3,S}
""",
	solute = SoluteData(
		S = 0.08364,
		B = 0.02000,
		E = -0.06800,
		L = -0.23276,
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
	index = 34,
	label = "F-(Cs-(Cs-HHX)XH)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S} {7,S} {8,S}
4   [F1s,Cl1s,Br1s,I1s]   u0 {2,S}
5   H   u0 {2,S}
6   H   u0 {3,S}
7   H   u0 {3,S}
8   [F1s,Cl1s,Br1s,I1s] u0 {3,S}
""",
	solute = SoluteData(
		S = 0.13987,
		B = 0.02383,
		E = -0.08194,
		L = -0.10545,
		A = 0.04114,
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
	index = 35,
	label = "F-(Cs-(Cs-HXX)XH)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S} {7,S} {8,S}
4   [F1s,Cl1s,Br1s,I1s]   u0 {2,S}
5   H   u0 {2,S}
6   H   u0 {3,S}
7   [F1s,Cl1s,Br1s,I1s] u0 {3,S}
8   [F1s,Cl1s,Br1s,I1s] u0 {3,S}
""",
	solute = SoluteData(
		S = 0.06123,
		B = 0.02370,
		E = -0.09350,
		L = -0.18447,
		A = 0.02543,
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
	index = 36,
	label = "F-(Cs-(Cs-XXX)XH)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S} {7,S} {8,S}
4   [F1s,Cl1s,Br1s,I1s]   u0 {2,S}
5   H   u0 {2,S}
6   [F1s,Cl1s,Br1s,I1s] u0 {3,S}
7   [F1s,Cl1s,Br1s,I1s] u0 {3,S}
8   [F1s,Cl1s,Br1s,I1s] u0 {3,S}
""",
	solute = SoluteData(
		S = 0.02803,
		B = 0.00000,
		E = -0.08484,
		L = -0.19780,
		A = 0.01288,
	),
	dataCount = DataCountGAV(
		S = 9,
		B = 9,
		E = 9,
		L = 9,
		A = 10,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 37,
	label = "F-(Cs-(Cs-(OH))XH)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S}
4   [F1s,Cl1s,Br1s,I1s] u0 {2,S}
5   H   u0 {2,S}
6   O2s u0 {3,S} {7,S}
7   H   u0 {6,S}
""",
	solute = None,
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 38,
	label = "F-(Cs-CsFH)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S}
4   F1s u0 {2,S}
5   H   u0 {2,S}
6   [C,N,O,S,P] u0 {3,S}
""",
	solute = SoluteData(
		S = 0.00000,
		B = 0.01502,
		E = -0.12026,
		L = -0.07584,
		A = 0.02979,
	),
	dataCount = DataCountGAV(
		S = 25,
		B = 25,
		E = 26,
		L = 25,
		A = 25,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 39,
	label = "F-(Cs-CsClH)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S}
4   Cl1s u0 {2,S}
5   H   u0 {2,S}
6   [C,N,O,S,P] u0 {3,S}
""",
	solute = SoluteData(
		S = 0.15129,
		B = 0.01122,
		E = 0.02979,
		L = 0.31889,
		A = 0.02231,
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
	index = 40,
	label = "F-(Cs-CsBrH)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S}
4   Br1s u0 {2,S}
5   H   u0 {2,S}
6   [C,N,O,S,P] u0 {3,S}
""",
	solute = SoluteData(
		S = 0.07899,
		B = -0.00121,
		E = 0.01275,
		L = 0.29461,
		A = 0.01928,
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
	index = 41,
	label = "F-(Cs-CsIH)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S}
4   I1s u0 {2,S}
5   H   u0 {2,S}
6   [C,N,O,S,P] u0 {3,S}
""",
	solute = u'F-(Cs-CsBrH)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 42,
	label = "F-(Cs-CsXX)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   [F1s,Cl1s,Br1s,I1s] u0 {2,S}
5   [F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = SoluteData(
		S = 0.10378,
		B = 0.02211,
		E = 0.10567,
		L = 0.61635,
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
	index = 43,
	label = "F-(Cs-(Cs-ZZZ)XX)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S} {7,S} {8,S}
4   [F1s,Cl1s,Br1s,I1s]   u0 {2,S}
5   [F1s,Cl1s,Br1s,I1s]   u0 {2,S}
6   [H,F1s,Cl1s,Br1s,I1s] u0 {3,S}
7   [H,F1s,Cl1s,Br1s,I1s] u0 {3,S}
8   [H,F1s,Cl1s,Br1s,I1s] u0 {3,S}
""",
	solute = u'F-(Cs-(Cs-HHH)XX)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 44,
	label = "F-(Cs-(Cs-HHH)XX)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S} {7,S} {8,S}
4   [F1s,Cl1s,Br1s,I1s]   u0 {2,S}
5   [F1s,Cl1s,Br1s,I1s]   u0 {2,S}
6   H   u0 {3,S}
7   H   u0 {3,S}
8   H   u0 {3,S}
""",
	solute = SoluteData(
		S = 0.04332,
		B = 0.02264,
		E = -0.08635,
		L = -0.25699,
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
	index = 45,
	label = "F-(Cs-(Cs-HHX)XX)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S} {7,S} {8,S}
4   [F1s,Cl1s,Br1s,I1s]   u0 {2,S}
5   [F1s,Cl1s,Br1s,I1s]   u0 {2,S}
6   H   u0 {3,S}
7   H   u0 {3,S}
8   [F1s,Cl1s,Br1s,I1s] u0 {3,S}
""",
	solute = SoluteData(
		S = 0.11899,
		B = 0.00000,
		E = -0.06618,
		L = -0.07654,
		A = 0.01824,
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
	index = 46,
	label = "F-(Cs-(Cs-HXX)XX)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S} {7,S} {8,S}
4   [F1s,Cl1s,Br1s,I1s]   u0 {2,S}
5   [F1s,Cl1s,Br1s,I1s]   u0 {2,S}
6   H   u0 {3,S}
7   [F1s,Cl1s,Br1s,I1s] u0 {3,S}
8   [F1s,Cl1s,Br1s,I1s] u0 {3,S}
""",
	solute = SoluteData(
		S = 0.05989,
		B = 0.00000,
		E = -0.05765,
		L = -0.08983,
		A = 0.02412,
	),
	dataCount = DataCountGAV(
		S = 14,
		B = 14,
		E = 14,
		L = 14,
		A = 15,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 47,
	label = "F-(Cs-(Cs-XXX)XX)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S} {7,S} {8,S}
4   [F1s,Cl1s,Br1s,I1s]   u0 {2,S}
5   [F1s,Cl1s,Br1s,I1s]   u0 {2,S}
6   [F1s,Cl1s,Br1s,I1s] u0 {3,S}
7   [F1s,Cl1s,Br1s,I1s] u0 {3,S}
8   [F1s,Cl1s,Br1s,I1s] u0 {3,S}
""",
	solute = SoluteData(
		S = -0.04682,
		B = 0.00000,
		E = -0.08351,
		L = -0.22240,
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
	index = 48,
	label = "F-(Cs-CsFX)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S}
4   F1s u0 {2,S}
5   [F1s,Cl1s,Br1s,I1s] u0 {2,S}
6   [C,N,O,S,P] u0 {3,S}
""",
	solute = u'F-(Cs-CsFH)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 49,
	label = "F-(Cs-CsFF)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S}
4   F1s u0 {2,S}
5   F1s u0 {2,S}
6   [C,N,O,S,P] u0 {3,S}
""",
	solute = SoluteData(
		S = -0.04245,
		B = 0.01028,
		E = -0.09262,
		L = -0.13333,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 57,
		B = 54,
		E = 64,
		L = 53,
		A = 60,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 50,
	label = "F-(Cs-(Cs-(OH))FF)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S}
4   F1s u0 {2,S}
5   F1s u0 {2,S}
6   O2s u0 {3,S} {7,S}
7   H   u0 {6,S}
""",
	solute = SoluteData(
		S = 0.00960,
		B = -0.06363,
		E = -0.06408,
		L = -0.13003,
		A = 0.05192,
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
	index = 51,
	label = "F-(Cs-(Cs-O)FF)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S}
4   F1s u0 {2,S}
5   F1s u0 {2,S}
6   O2s u0 {3,S} {7,S}
7   R!H u0 {6,S}
""",
	solute = SoluteData(
		S = -0.01779,
		B = 0.00000,
		E = -0.08041,
		L = -0.08676,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 35,
		B = 34,
		E = 35,
		L = 33,
		A = 34,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 52,
	label = "F-(Cs-CsFCl)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S}
4   F1s u0 {2,S}
5   Cl1s u0 {2,S}
6   [C,N,O,S,P] u0 {3,S}
""",
	solute = SoluteData(
		S = 0.02719,
		B = 0.00889,
		E = -0.02778,
		L = 0.15932,
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
	index = 53,
	label = "F-(Cs-CsFBr)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S}
4   F1s u0 {2,S}
5   Br1s u0 {2,S}
6   [C,N,O,S,P] u0 {3,S}
""",
	solute = SoluteData(
		S = 0.02893,
		B = 0.00000,
		E = -0.07133,
		L = 0.00397,
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
	index = 54,
	label = "F-(Cs-CsFI)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S}
4   F1s u0 {2,S}
5   I1s u0 {2,S}
6   [C,N,O,S,P] u0 {3,S}
""",
	solute = u'F-(Cs-CsFBr)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 55,
	label = "F-(Cs-CdZZ)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   [Cd,CO,CS]   u0 {2,S}
4   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = u'F-(Cs-(Cd-Cd)ZZ)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 56,
	label = "F-(Cs-(Cd-Cd)ZZ)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cd  u0 {2,S} {6,D}
4   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
6   C   u0 {3,D}
""",
	solute = u'F-(Cs-(Cd-Cd)FX)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 57,
	label = "F-(Cs-(Cd-Cd)FX)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cd  u0 {2,S} {6,D}
4   F1s u0 {2,S}
5   [F1s,Cl1s,Br1s,I1s] u0 {2,S}
6   C   u0 {3,D}
""",
	solute = u'F-(Cs-(Cd-Cd)FF)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 58,
	label = "F-(Cs-(Cd-Cd)FF)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cd  u0 {2,S} {6,D}
4   F1s u0 {2,S}
5   F1s u0 {2,S}
6   C   u0 {3,D}
""",
	solute = SoluteData(
		S = -0.09316,
		B = 0.00562,
		E = -0.11980,
		L = -0.21486,
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
	index = 59,
	label = "F-(Cs-(Cd-Nd)ZZ)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cd  u0 {2,S} {6,D}
4   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
6   N   u0 {3,D}
""",
	solute = u'F-(Cs-(Cd-Nd)XX)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 60,
	label = "F-(Cs-(Cd-Nd)XX)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cd  u0 {2,S} {6,D}
4   [F1s,Cl1s,Br1s,I1s] u0 {2,S}
5   [F1s,Cl1s,Br1s,I1s] u0 {2,S}
6   N   u0 {3,D}
""",
	solute = u'F-(Cs-(Cd-Nd)FF)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 61,
	label = "F-(Cs-(Cd-Nd)FF)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cd  u0 {2,S} {6,D}
4   F1s u0 {2,S}
5   F1s u0 {2,S}
6   N   u0 {3,D}
""",
	solute = SoluteData(
		S = -0.00588,
		B = -0.06859,
		E = -0.13258,
		L = -0.15040,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 11,
		B = 11,
		E = 11,
		L = 9,
		A = 11,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 62,
	label = "F-(Cs-(Cd-O2d)ZZ)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   CO  u0 {2,S} {6,D}
4   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
6   O2d u0 {3,D}
""",
	solute = u'F-(Cs-(Cd-O2d)XX)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 63,
	label = "F-(Cs-(Cd-O2d)HH)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   CO  u0 {2,S} {6,D}
4   H   u0 {2,S}
5   H   u0 {2,S}
6   O2d u0 {3,D}
""",
	solute = SoluteData(
		S = 0.09225,
		B = 0.00000,
		E = 0.00179,
		L = 0.11251,
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
	index = 64,
	label = "F-(Cs-(Cd-O2d(OH))HH)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   CO  u0 {2,S} {6,D} {7,S}
4   H   u0 {2,S}
5   H   u0 {2,S}
6   O2d u0 {3,D}
7   O2s u0 {3,S} {8,S}
8   H   u0 {7,S}
""",
	solute = SoluteData(
		S = 0.05239,
		B = -0.01337,
		E = 0.01277,
		L = 0.12359,
		A = 0.04124,
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
	index = 65,
	label = "F-(Cs-(Cd-O2d)XH)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   CO  u0 {2,S} {6,D}
4   [F1s,Cl1s,Br1s,I1s]  u0 {2,S}
5   H   u0 {2,S}
6   O2d u0 {3,D}
""",
	solute = u'F-(Cs-(Cd-O2d)HH)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 66,
	label = "F-(Cs-(Cd-O2d(OH))XH)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   CO  u0 {2,S} {6,D} {7,S}
4   F1s u0 {2,S}
5   H   u0 {2,S}
6   O2d u0 {3,D}
7   O2s u0 {3,S} {8,S}
8   H   u0 {7,S}
""",
	solute = SoluteData(
		S = 0.03075,
		B = -0.03814,
		E = -0.02290,
		L = 0.05259,
		A = 0.07655,
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
	label = "F-(Cs-(Cd-O2d)XX)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   CO  u0 {2,S} {6,D}
4   [F1s,Cl1s,Br1s,I1s]  u0 {2,S}
5   [F1s,Cl1s,Br1s,I1s]  u0 {2,S}
6   O2d u0 {3,D}
""",
	solute = SoluteData(
		S = -0.12822,
		B = -0.01668,
		E = -0.10019,
		L = -0.22216,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 13,
		B = 12,
		E = 14,
		L = 12,
		A = 15,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 68,
	label = "F-(Cs-(Cd-O2d(OH))XX)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   CO  u0 {2,S} {6,D} {7,S}
4   [F1s,Cl1s,Br1s,I1s] u0 {2,S}
5   [F1s,Cl1s,Br1s,I1s] u0 {2,S}
6   O2d u0 {3,D}
7   O2s u0 {3,S} {8,S}
8   H   u0 {7,S}
""",
	solute = SoluteData(
		S = 0.00733,
		B = -0.04837,
		E = -0.08501,
		L = -0.04070,
		A = 0.08912,
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
	index = 69,
	label = "F-(Cs-(Cd-O2d(NH))XX)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   CO  u0 {2,S} {6,D} {7,S}
4   [F1s,Cl1s,Br1s,I1s] u0 {2,S}
5   [F1s,Cl1s,Br1s,I1s] u0 {2,S}
6   O2d u0 {3,D}
7   N   u0 {3,S} {8,S}
8   H   u0 {7,S}
""",
	solute = SoluteData(
		S = -0.20640,
		B = -0.09379,
		E = -0.18216,
		L = -0.37035,
		A = 0.04150,
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
	index = 70,
	label = "F-(Cs-O2sZZ)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   O2s u0 {2,S}
4   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = u'F-(Cs-O2sHZ)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 71,
	label = "F-(Cs-O2sHZ)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   O2s u0 {2,S}
4   H   u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = u'F-(Cs-O2sHH)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 72,
	label = "F-(Cs-O2sHH)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   O2s u0 {2,S}
4   H   u0 {2,S}
5   H   u0 {2,S}
""",
	solute = SoluteData(
		S = 0.11314,
		B = -0.11150,
		E = -0.02375,
		L = 0.05805,
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
	index = 73,
	label = "F-(Cs-O2sHX)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   O2s u0 {2,S}
4   H   u0 {2,S}
5   [F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = u'F-(Cs-O2sHF)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 74,
	label = "F-(Cs-O2sHF)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   O2s u0 {2,S}
4   H   u0 {2,S}
5   F1s u0 {2,S}
""",
	solute = SoluteData(
		S = 0.04289,
		B = -0.09603,
		E = -0.05573,
		L = -0.03596,
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
	index = 75,
	label = "F-(Cs-O2sXX)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   O2s u0 {2,S}
4   [F1s,Cl1s,Br1s,I1s] u0 {2,S}
5   [F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = SoluteData(
		S = -0.08674,
		B = -0.08006,
		E = -0.03071,
		L = -0.01907,
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
	index = 76,
	label = "F-(Cs-O2sFF)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   O2s u0 {2,S}
4   F1s u0 {2,S}
5   F1s u0 {2,S}
""",
	solute = SoluteData(
		S = -0.10001,
		B = -0.09097,
		E = -0.13457,
		L = -0.28153,
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
	index = 77,
	label = "F-(Cs-CCZ)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   C   u0 {2,S}
4   C   u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = u'F-(Cs-CsCsZ)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 78,
	label = "F-(Cs-CsCsZ)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   Cs  u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = u'F-(Cs-CsCsH)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 79,
	label = "F-(Cs-CsCsH)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   Cs  u0 {2,S}
5   H   u0 {2,S}
""",
	solute = SoluteData(
		S = 0.14690,
		B = 0.02914,
		E = -0.04738,
		L = 0.06577,
		A = 0.05096,
	),
	dataCount = DataCountGAV(
		S = 18,
		B = 18,
		E = 18,
		L = 18,
		A = 18,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 80,
	label = "F-(Cs-CsCsX)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   Cs  u0 {2,S}
5   [F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = u'F-(Cs-CsCsF)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 81,
	label = "F-(Cs-CsCsF)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   Cs  u0 {2,S}
5   F1s u0 {2,S}
""",
	solute = SoluteData(
		S = -0.05069,
		B = 0.01311,
		E = -0.06259,
		L = -0.08756,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 64,
		B = 60,
		E = 71,
		L = 59,
		A = 67,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 82,
	label = "F-(Cs-(Cs-(OH))CsF)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S}
4   Cs  u0 {2,S}
5   F1s u0 {2,S}
6   O2s u0 {3,S} {7,S}
7   H   u0 {6,S}
""",
	solute = SoluteData(
		S = 0.07503,
		B = -0.16093,
		E = -0.07162,
		L = -0.01935,
		A = 0.16197,
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
	index = 83,
	label = "F-(Cs-CsCsCl)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   Cs  u0 {2,S}
5   Cl1s u0 {2,S}
""",
	solute = SoluteData(
		S = -0.00670,
		B = 0.00000,
		E = 0.03334,
		L = 0.29750,
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
	index = 84,
	label = "F-(Cs-CsCsBr)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   Cs  u0 {2,S}
5   Br1s u0 {2,S}
""",
	solute = u'F-(Cs-CsCsCl)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 85,
	label = "F-(Cs-CsCsI)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   Cs  u0 {2,S}
5   I1s u0 {2,S}
""",
	solute = u'F-(Cs-CsCsCl)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 86,
	label = "F-(Cs-CsCdZ)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   [Cd,CO,CS]  u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = u'F-(Cs-CsCsZ)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 87,
	label = "F-(Cs-Cs(Cd-Cd)Z)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   Cd  u0 {2,S} {6,D}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
6   C   u0 {4,D}
""",
	solute = u'F-(Cs-CsCsX)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 88,
	label = "F-(Cs-Cs(Cd-Nd)Z)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   Cd  u0 {2,S} {6,D}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
6   N   u0 {4,D}
""",
	solute = u'F-(Cs-(Cd-Nd)ZZ)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 89,
	label = "F-(Cs-Cs(Cd-O2d)Z)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   CO  u0 {2,S} {6,D}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
6   O2d u0 {4,D}
""",
	solute = u'F-(Cs-(Cd-O2d)ZZ)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 90,
	label = "F-(Cs-CO2sZ)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   C   u0 {2,S}
4   O2s u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = u'F-(Cs-CsO2sZ)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 91,
	label = "F-(Cs-CsO2sZ)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   O2s u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = u'F-(Cs-CsO2sH)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 92,
	label = "F-(Cs-CsO2sH)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   O2s u0 {2,S}
5   H   u0 {2,S}
""",
	solute = SoluteData(
		S = 0.04511,
		B = -0.09196,
		E = -0.08001,
		L = -0.09593,
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
	index = 93,
	label = "F-(Cs-CsO2sX)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   O2s u0 {2,S}
5   [F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = SoluteData(
		S = -0.05247,
		B = -0.02783,
		E = -0.05463,
		L = -0.18948,
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
	index = 94,
	label = "F-(Cs-CsO2sF)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   O2s u0 {2,S}
5   F1s u0 {2,S}
""",
	solute = SoluteData(
		S = -0.13096,
		B = -0.08618,
		E = -0.07782,
		L = -0.18447,
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
	index = 95,
	label = "F-(Cs-CCC)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   C   u0 {2,S}
4   C   u0 {2,S}
5   C   u0 {2,S}
""",
	solute = u'F-(Cs-CsCsCs)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 96,
	label = "F-(Cs-CsCsCs)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   Cs  u0 {2,S}
5   Cs  u0 {2,S}
""",
	solute = SoluteData(
		S = 0.04446,
		B = 0.01940,
		E = -0.09103,
		L = -0.19210,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 15,
		B = 11,
		E = 15,
		L = 7,
		A = 15,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 97,
	label = "F-(Cs-CCO2s)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   C   u0 {2,S}
4   C   u0 {2,S}
5   O2s u0 {2,S}
""",
	solute = u'F-(Cs-CsCsO2s)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 98,
	label = "F-(Cs-CsCsO2s)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   Cs  u0 {2,S}
5   O2s u0 {2,S}
""",
	solute = SoluteData(
		S = -0.12043,
		B = -0.09214,
		E = -0.10666,
		L = -0.32313,
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
	index = 99,
	label = "F-Cd",
	group = 
"""
1 * F1s        u0 {2,S}
2   [Cd,CO,CS] u0 {1,S}
""",
	solute = u'F-(Cd-Cd)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 100,
	label = "F-(Cd-Cd)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cd  u0 {1,S} {3,D}
3   C   u0 {2,D}
""",
	solute = u'F-(Cd-CdR)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 101,
	label = "F-(Cd-CdR)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cd  u0 {1,S} {3,D} {4,S}
3   C   u0 {2,D}
4   [C,N,O,S]  u0 {2,S}
""",
	solute = u'F-(Cd-CdC)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 102,
	label = "F-(Cd-CdC)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cd  u0 {1,S} {3,D} {4,S}
3   C   u0 {2,D}
4   C   u0 {2,S}
""",
	solute = u'F-(Crd-CrdCr)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 103,
	label = "F-(Crd-CrdCr)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cd  u0 r1 {1,S} {3,D} {4,S}
3   C   u0 r1 {2,D}
4   C   u0 r1 {2,S}
""",
	solute = u'F-(Crd-CrdCrd)',
	dataCount = None,
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 104,
	label = "F-(Crd-CrdCrd)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cd  u0 r1 {1,S} {3,D} {4,S}
3   C   u0 r1 {2,D}
4   [Cd,CO,CS] u0 r1 {2,S}
""",
	solute = SoluteData(
		S = 0.01170,
		B = -0.09174,
		E = -0.10720,
		L = -0.08695,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 48,
		B = 48,
		E = 51,
		L = 43,
		A = 52,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 105,
	label = "F-(Cd-CdCs)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cd  u0 {1,S} {3,D} {4,S}
3   C   u0 {2,D}
4   Cs  u0 {2,S}
""",
	solute = SoluteData(
		S = 0.01323,
		B = 0.00079,
		E = 0.01721,
		L = 0.05175,
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
	index = 106,
	label = "F-(Cd-CdN)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cd  u0 {1,S} {3,D} {4,S}
3   C   u0 {2,D}
4   N   u0 {2,S}
""",
	solute = u'F-(Cd-CrdNr)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 107,
	label = "F-(Cd-CrdNr)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cd  u0 r1 {1,S} {3,D} {4,S}
3   C   u0 r1 {2,D}
4   N   u0 r1 {2,S}
""",
	solute = SoluteData(
		S = 0.01749,
		B = -0.08261,
		E = -0.09530,
		L = -0.13030,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 4,
		L = 2,
		A = 3,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 108,
	label = "F-(Cd-CdZ)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cd  u0 {1,S} {3,D} {4,S}
3   C   u0 {2,D}
4   [H,F1s,Cl1s,Br1s,I1s]  u0 {2,S}
""",
	solute = u'F-(Cd-CdH)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 109,
	label = "F-(Cd-CdH)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cd  u0 {1,S} {3,D} {4,S}
3   C   u0 {2,D}
4   H   u0 {2,S}
""",
	solute = SoluteData(
		S = 0.00000,
		B = -0.01129,
		E = -0.06664,
		L = -0.13689,
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
	index = 110,
	label = "F-(Cd-CdX)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cd  u0 {1,S} {3,D} {4,S}
3   C   u0 {2,D}
4   [F1s,Cl1s,Br1s,I1s]  u0 {2,S}
""",
	solute = SoluteData(
		S = 0.00952,
		B = 0.00000,
		E = -0.05465,
		L = -0.00608,
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
	index = 111,
	label = "F-(Cd-CdF)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cd  u0 {1,S} {3,D} {4,S}
3   C   u0 {2,D}
4   F1s u0 {2,S}
""",
	solute = SoluteData(
		S = -0.07028,
		B = 0.00000,
		E = -0.12785,
		L = -0.18943,
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
	index = 112,
	label = "F-(Cd-Nd)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cd  u0 {1,S} {3,D}
3   N   u0 {2,D}
""",
	solute = u'F-(Cd-N3d)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 113,
	label = "F-(Cd-N3d)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cd  u0 {1,S} {3,D}
3   N3d u0 {2,D}
""",
	solute = u'F-(Crd-N3rd)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 114,
	label = "F-(Crd-N3rd)",
	group = 
"""
1 * F1s u0 {2,S}
2   Cd  u0 r1 {1,S} {3,D}
3   N3d u0 r1 {2,D}
""",
	solute = SoluteData(
		S = -0.02033,
		B = -0.03384,
		E = -0.08419,
		L = -0.20990,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 3,
		B = 3,
		E = 4,
		L = 2,
		A = 3,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 115,
	label = "F-N",
	group = 
"""
1 * F1s u0 {2,S}
2   N   u0 {1,S}
""",
	solute = u'F-N3s',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 116,
	label = "F-N3s",
	group = 
"""
1 * F1s u0 {2,S}
2   N3s u0 {1,S}
""",
	solute = SoluteData(
		S = -0.27811,
		B = -0.19612,
		E = -0.18432,
		L = -0.59242,
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
	index = 117,
	label = "F-P",
	group = 
"""
1 * F1s u0 {2,S}
2   P u0 {1,S}
""",
	solute = u'F-P5d',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 118,
	label = "F-P5d",
	group = 
"""
1 * F1s u0 {2,S}
2   P5d u0 {1,S}
""",
	solute = SoluteData(
		S = -0.04700,
		B = 0.04165,
		E = -0.12862,
		L = 0.09741,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 1,
		E = 5,
		L = 1,
		A = 4,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 119,
	label = "Cl",
	group = 
"""
1 * Cl1s u0
""",
	solute = u'Cl-C',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 120,
	label = "Cl-C",
	group = 
"""
1 * Cl1s u0 {2,S}
2   C    u0 {1,S}
""",
	solute = u'Cl-Cs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 121,
	label = "Cl-Cb",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cb   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.09871,
		B = -0.03125,
		E = 0.13565,
		L = 0.61878,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 625,
		B = 609,
		E = 639,
		L = 574,
		A = 642,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 122,
	label = "Cl-Phenol",
	group =  "OR{Cl-Phenol(ortho), Cl-Phenol(meta), Cl-Phenol(para)}",
	solute = None,
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 123,
	label = "Cl-Phenol(ortho)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cb  u0 {1,S} {3,B}
3   Cb  u0 {2,B} {4,S}
4   O2s u0 {3,S} {5,S}
5   H   u0 {4,S}
""",
	solute = SoluteData(
		S = -0.00875,
		B = -0.01197,
		E = 0.06547,
		L = 0.47353,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 28,
		B = 28,
		E = 35,
		L = 35,
		A = 28,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 124,
	label = "Cl-Phenol(meta)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cb  u0 {1,S} {3,B}
3   Cb  u0 {2,B} {4,B}
4   Cb  u0 {3,B} {5,S}
5   O2s u0 {4,S} {6,S}
6   H   u0 {5,S}
""",
	solute = SoluteData(
		S = 0.12972,
		B = -0.07300,
		E = 0.10450,
		L = 0.78011,
		A = 0.14367,
	),
	dataCount = DataCountGAV(
		S = 21,
		B = 21,
		E = 28,
		L = 27,
		A = 21,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 125,
	label = "Cl-Phenol(para)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cb  u0 {1,S} {3,B}
3   Cb  u0 {2,B} {4,B}
4   Cb  u0 {3,B} {5,B}
5   Cb  u0 {4,B} {6,S}
6   O2s u0 {5,S} {7,S}
7   H   u0 {6,S}
""",
	solute = SoluteData(
		S = 0.01371,
		B = -0.07460,
		E = 0.08622,
		L = 0.54024,
		A = -0.01452,
	),
	dataCount = DataCountGAV(
		S = 23,
		B = 23,
		E = 23,
		L = 22,
		A = 23,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 126,
	label = "Cl-BenzoicAcid",
	group =  "OR{Cl-BenzoicAcid(ortho), Cl-BenzoicAcid(meta), Cl-BenzoicAcid(para)}",
	solute = None,
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 127,
	label = "Cl-BenzoicAcid(ortho)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cb  u0 {1,S} {3,B}
3   Cb  u0 {2,B} {4,S}
4   CO  u0 {3,S} {5,S}
5   O2s u0 {4,S} {6,S}
6   H   u0 {5,S}
""",
	solute = SoluteData(
		S = 0.07761,
		B = 0.00000,
		E = 0.06262,
		L = 0.47523,
		A = 0.08274,
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
	index = 128,
	label = "Cl-BenzoicAcid(meta)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cb  u0 {1,S} {3,B}
3   Cb  u0 {2,B} {4,B}
4   Cb  u0 {3,B} {5,S}
5   CO  u0 {4,S} {6,S}
6   O2s u0 {5,S} {7,S}
7   H   u0 {6,S}
""",
	solute = SoluteData(
		S = 0.02261,
		B = -0.02842,
		E = 0.10484,
		L = 0.50277,
		A = 0.03911,
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
	index = 129,
	label = "Cl-BenzoicAcid(para)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cb  u0 {1,S} {3,B}
3   Cb  u0 {2,B} {4,B}
4   Cb  u0 {3,B} {5,B}
5   Cb  u0 {4,B} {6,S}
6   CO  u0 {5,S} {7,S}
7   O2s u0 {6,S} {8,S}
8   H   u0 {7,S}
""",
	solute = SoluteData(
		S = 0.00052,
		B = -0.03521,
		E = 0.08251,
		L = 0.44248,
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
	index = 130,
	label = "Cl-BenzylAlcohol",
	group =  "OR{Cl-BenzylAlcohol(ortho), Cl-BenzylAlcohol(meta), Cl-BenzylAlcohol(para)}",
	solute = None,
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 131,
	label = "Cl-BenzylAlcohol(ortho)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cb  u0 {1,S} {3,B}
3   Cb  u0 {2,B} {4,S}
4   C   u0 {3,S} {5,S}
5   O2s u0 {4,S} {6,S}
6   H   u0 {5,S}
""",
	solute = SoluteData(
		S = 0.03323,
		B = -0.04378,
		E = 0.08578,
		L = 0.39463,
		A = 0.01121,
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
	index = 132,
	label = "Cl-BenzylAlcohol(meta)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cb  u0 {1,S} {3,B}
3   Cb  u0 {2,B} {4,B}
4   Cb  u0 {3,B} {5,S}
5   C   u0 {4,S} {6,S}
6   O2s u0 {5,S} {7,S}
7   H   u0 {6,S}
""",
	solute = SoluteData(
		S = 0.00544,
		B = -0.01836,
		E = 0.07210,
		L = 0.21519,
		A = 0.00688,
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
	index = 133,
	label = "Cl-BenzylAlcohol(para)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cb  u0 {1,S} {3,B}
3   Cb  u0 {2,B} {4,B}
4   Cb  u0 {3,B} {5,B}
5   Cb  u0 {4,B} {6,S}
6   C   u0 {5,S} {7,S}
7   O2s u0 {6,S} {8,S}
8   H   u0 {7,S}
""",
	solute = SoluteData(
		S = -0.06224,
		B = 0.00456,
		E = 0.06827,
		L = 0.34433,
		A = 0.01051,
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
	index = 134,
	label = "Cl-Aniline",
	group =  "OR{Cl-Aniline(ortho), Cl-Aniline(meta), Cl-Aniline(para)}",
	solute = None,
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 135,
	label = "Cl-Aniline(ortho)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cb  u0 {1,S} {3,B}
3   Cb  u0 {2,B} {4,S}
4   N3s u0 {3,S} {5,S} {6,S}
5   H   u0 {4,S}
6   H   u0 {4,S}
""",
	solute = SoluteData(
		S = 0.01752,
		B = -0.08834,
		E = 0.10899,
		L = 0.57089,
		A = 0.02114,
	),
	dataCount = DataCountGAV(
		S = 21,
		B = 21,
		E = 21,
		L = 16,
		A = 21,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 136,
	label = "Cl-Aniline(meta)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cb  u0 {1,S} {3,B}
3   Cb  u0 {2,B} {4,B}
4   Cb  u0 {3,B} {5,S}
5   N3s u0 {4,S} {6,S} {7,S}
6   H   u0 {5,S}
7   H   u0 {5,S}
""",
	solute = SoluteData(
		S = 0.07620,
		B = -0.05871,
		E = 0.10018,
		L = 0.59269,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 16,
		B = 16,
		E = 16,
		L = 11,
		A = 16,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 137,
	label = "Cl-Aniline(para)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cb  u0 {1,S} {3,B}
3   Cb  u0 {2,B} {4,B}
4   Cb  u0 {3,B} {5,B}
5   Cb  u0 {4,B} {6,S}
6   N3s u0 {5,S} {7,S} {8,S}
7   H   u0 {6,S}
8   H   u0 {6,S}
""",
	solute = SoluteData(
		S = 0.05315,
		B = -0.08780,
		E = 0.08998,
		L = 0.47410,
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
	index = 138,
	label = "Cl-Cs",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs   u0 {1,S}
""",
	solute = u'Cl-(Cs-CZZ)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 139,
	label = "Cl-(Cs-CZZ)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   C   u0 {2,S}
4   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = u'Cl-(Cs-CsZZ)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 140,
	label = "Cl-(Cs-CbZZ)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cb  u0 {2,S}
4   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = SoluteData(
		S = 0.14447,
		B = 0.03849,
		E = 0.14000,
		L = 0.73475,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 12,
		B = 10,
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
	index = 141,
	label = "Cl-(Cs-CsZZ)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = u'Cl-(Cs-CsHH)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 142,
	label = "Cl-(Cs-CsHH)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   H   u0 {2,S}
5   H   u0 {2,S}
""",
	solute = SoluteData(
		S = 0.32335,
		B = 0.05705,
		E = 0.17805,
		L = 0.86379,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 62,
		B = 60,
		E = 78,
		L = 67,
		A = 83,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 143,
	label = "Cl-(Cs-(Cs-ZZZ)HH)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S} {7,S} {8,S}
4   H   u0 {2,S}
5   H   u0 {2,S}
6   [H,F1s,Cl1s,Br1s,I1s] u0 {3,S}
7   [H,F1s,Cl1s,Br1s,I1s] u0 {3,S}
8   [H,F1s,Cl1s,Br1s,I1s] u0 {3,S}
""",
	solute = u'Cl-(Cs-(Cs-HHH)HH)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 144,
	label = "Cl-(Cs-(Cs-HHH)HH)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S} {7,S} {8,S}
4   H   u0 {2,S}
5   H   u0 {2,S}
6   H   u0 {3,S}
7   H   u0 {3,S}
8   H   u0 {3,S}
""",
	solute = SoluteData(
		S = 0.05000,
		B = 0.03000,
		E = 0.07567,
		L = 0.12344,
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
	index = 145,
	label = "Cl-(Cs-(Cs-HHX)HH)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S} {7,S} {8,S}
4   H   u0 {2,S}
5   H   u0 {2,S}
6   H   u0 {3,S}
7   H   u0 {3,S}
8   [F1s,Cl1s,Br1s,I1s] u0 {3,S}
""",
	solute = SoluteData(
		S = 0.15919,
		B = 0.02649,
		E = 0.16224,
		L = 0.48838,
		A = 0.02720,
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
	index = 146,
	label = "Cl-(Cs-(Cs-HXX)HH)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S} {7,S} {8,S}
4   H   u0 {2,S}
5   H   u0 {2,S}
6   H   u0 {3,S}
7   [F1s,Cl1s,Br1s,I1s] u0 {3,S}
8   [F1s,Cl1s,Br1s,I1s] u0 {3,S}
""",
	solute = SoluteData(
		S = 0.11845,
		B = 0.01085,
		E = 0.07506,
		L = 0.40279,
		A = 0.02283,
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
	index = 147,
	label = "Cl-(Cs-(Cs-XXX)HH)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S} {7,S} {8,S}
4   H   u0 {2,S}
5   H   u0 {2,S}
6   [F1s,Cl1s,Br1s,I1s] u0 {3,S}
7   [F1s,Cl1s,Br1s,I1s] u0 {3,S}
8   [F1s,Cl1s,Br1s,I1s] u0 {3,S}
""",
	solute = SoluteData(
		S = 0.05733,
		B = 0.02324,
		E = 0.05729,
		L = 0.27932,
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
	label = "Cl-(Cs-(Cs-(OH))HH)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S}
4   H   u0 {2,S}
5   H   u0 {2,S}
6   O2s u0 {3,S} {7,S}
7   H   u0 {6,S}
""",
	solute = SoluteData(
		S = 0.09056,
		B = 0.02542,
		E = 0.10384,
		L = 0.34181,
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
	index = 149,
	label = "Cl-(Cs-CsXH)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   [F1s,Cl1s,Br1s,I1s]  u0 {2,S}
5   H   u0 {2,S}
""",
	solute = u'Cl-(Cs-CsClH)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 150,
	label = "Cl-(Cs-(Cs-ZZZ)XH)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S} {7,S} {8,S}
4   [F1s,Cl1s,Br1s,I1s]   u0 {2,S}
5   H   u0 {2,S}
6   [H,F1s,Cl1s,Br1s,I1s] u0 {3,S}
7   [H,F1s,Cl1s,Br1s,I1s] u0 {3,S}
8   [H,F1s,Cl1s,Br1s,I1s] u0 {3,S}
""",
	solute = u'Cl-(Cs-(Cs-HHH)XH)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 151,
	label = "Cl-(Cs-(Cs-HHH)XH)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S} {7,S} {8,S}
4   [F1s,Cl1s,Br1s,I1s]   u0 {2,S}
5   H   u0 {2,S}
6   H   u0 {3,S}
7   H   u0 {3,S}
8   H   u0 {3,S}
""",
	solute = SoluteData(
		S = 0.09636,
		B = 0.02000,
		E = 0.10733,
		L = 0.27977,
		A = 0.01750,
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
	index = 152,
	label = "Cl-(Cs-(Cs-HHX)XH)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S} {7,S} {8,S}
4   [F1s,Cl1s,Br1s,I1s]   u0 {2,S}
5   H   u0 {2,S}
6   H   u0 {3,S}
7   H   u0 {3,S}
8   [F1s,Cl1s,Br1s,I1s] u0 {3,S}
""",
	solute = SoluteData(
		S = 0.10210,
		B = 0.03404,
		E = 0.14131,
		L = 0.53117,
		A = 0.03560,
	),
	dataCount = DataCountGAV(
		S = 1,
		B = 1,
		E = 1,
		L = 1,
		A = 2,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 153,
	label = "Cl-(Cs-(Cs-HXX)XH)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S} {7,S} {8,S}
4   [F1s,Cl1s,Br1s,I1s]   u0 {2,S}
5   H   u0 {2,S}
6   H   u0 {3,S}
7   [F1s,Cl1s,Br1s,I1s] u0 {3,S}
8   [F1s,Cl1s,Br1s,I1s] u0 {3,S}
""",
	solute = SoluteData(
		S = 0.15167,
		B = 0.02370,
		E = 0.12627,
		L = 0.57308,
		A = 0.03743,
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
	index = 154,
	label = "Cl-(Cs-(Cs-XXX)XH)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S} {7,S} {8,S}
4   [F1s,Cl1s,Br1s,I1s]   u0 {2,S}
5   H   u0 {2,S}
6   [F1s,Cl1s,Br1s,I1s] u0 {3,S}
7   [F1s,Cl1s,Br1s,I1s] u0 {3,S}
8   [F1s,Cl1s,Br1s,I1s] u0 {3,S}
""",
	solute = SoluteData(
		S = 0.07166,
		B = 0.01332,
		E = 0.07136,
		L = 0.38038,
		A = 0.01465,
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
	index = 155,
	label = "Cl-(Cs-(Cs-(OH))XH)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S}
4   [F1s,Cl1s,Br1s,I1s]  u0 {2,S}
5   H   u0 {2,S}
6   O2s u0 {3,S} {7,S}
7   H   u0 {6,S}
""",
	solute = SoluteData(
		S = 0.03118,
		B = -0.01026,
		E = 0.03847,
		L = 0.08907,
		A = 0.00177,
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
	index = 156,
	label = "Cl-(Cs-CsFH)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S}
4   F1s u0 {2,S}
5   H   u0 {2,S}
6   [C,N,O,S,P] u0 {3,S}
""",
	solute = SoluteData(
		S = 0.15129,
		B = 0.01122,
		E = 0.02979,
		L = 0.31889,
		A = 0.02231,
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
	index = 157,
	label = "Cl-(Cs-CsClH)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S}
4   Cl1s u0 {2,S}
5   H   u0 {2,S}
6   [C,N,O,S,P] u0 {3,S}
""",
	solute = SoluteData(
		S = 0.19377,
		B = -0.00037,
		E = 0.14301,
		L = 0.72356,
		A = 0.03763,
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
	index = 158,
	label = "Cl-(Cs-CsBrH)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S}
4   Br1s u0 {2,S}
5   H   u0 {2,S}
6   [C,N,O,S,P] u0 {3,S}
""",
	solute = SoluteData(
		S = 0.11026,
		B = 0.01361,
		E = 0.08308,
		L = 0.48471,
		A = 0.00068,
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
	index = 159,
	label = "Cl-(Cs-CsIH)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S}
4   I1s u0 {2,S}
5   H   u0 {2,S}
6   [C,N,O,S,P] u0 {3,S}
""",
	solute = u'Cl-(Cs-CsBrH)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 160,
	label = "Cl-(Cs-CsXX)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   [F1s,Cl1s,Br1s,I1s]  u0 {2,S}
5   [F1s,Cl1s,Br1s,I1s]  u0 {2,S}
""",
	solute = u'Cl-(Cs-CsFX)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 161,
	label = "Cl-(Cs-(Cs-ZZZ)XX)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S} {7,S} {8,S}
4   [F1s,Cl1s,Br1s,I1s]   u0 {2,S}
5   [F1s,Cl1s,Br1s,I1s]   u0 {2,S}
6   [H,F1s,Cl1s,Br1s,I1s] u0 {3,S}
7   [H,F1s,Cl1s,Br1s,I1s] u0 {3,S}
8   [H,F1s,Cl1s,Br1s,I1s] u0 {3,S}
""",
	solute = u'Cl-(Cs-(Cs-HHH)XX)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 162,
	label = "Cl-(Cs-(Cs-HHH)XX)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S} {7,S} {8,S}
4   [F1s,Cl1s,Br1s,I1s]   u0 {2,S}
5   [F1s,Cl1s,Br1s,I1s]   u0 {2,S}
6   H   u0 {3,S}
7   H   u0 {3,S}
8   H   u0 {3,S}
""",
	solute = SoluteData(
		S = 0.11508,
		B = 0.01879,
		E = 0.10840,
		L = 0.41693,
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
	index = 163,
	label = "Cl-(Cs-(Cs-HHX)XX)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S} {7,S} {8,S}
4   [F1s,Cl1s,Br1s,I1s]   u0 {2,S}
5   [F1s,Cl1s,Br1s,I1s]   u0 {2,S}
6   H   u0 {3,S}
7   H   u0 {3,S}
8   [F1s,Cl1s,Br1s,I1s] u0 {3,S}
""",
	solute = SoluteData(
		S = 0.11838,
		B = 0.02183,
		E = 0.13553,
		L = 0.59623,
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
	index = 164,
	label = "Cl-(Cs-(Cs-HXX)XX)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S} {7,S} {8,S}
4   [F1s,Cl1s,Br1s,I1s]   u0 {2,S}
5   [F1s,Cl1s,Br1s,I1s]   u0 {2,S}
6   H   u0 {3,S}
7   [F1s,Cl1s,Br1s,I1s] u0 {3,S}
8   [F1s,Cl1s,Br1s,I1s] u0 {3,S}
""",
	solute = SoluteData(
		S = 0.10561,
		B = 0.00764,
		E = 0.12782,
		L = 0.61185,
		A = 0.03061,
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
	index = 165,
	label = "Cl-(Cs-(Cs-XXX)XX)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S} {7,S} {8,S}
4   [F1s,Cl1s,Br1s,I1s]   u0 {2,S}
5   [F1s,Cl1s,Br1s,I1s]   u0 {2,S}
6   [F1s,Cl1s,Br1s,I1s] u0 {3,S}
7   [F1s,Cl1s,Br1s,I1s] u0 {3,S}
8   [F1s,Cl1s,Br1s,I1s] u0 {3,S}
""",
	solute = SoluteData(
		S = 0.10394,
		B = 0.00000,
		E = 0.10591,
		L = 0.44403,
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
	index = 166,
	label = "Cl-(Cs-CsFX)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S}
4   F1s u0 {2,S}
5   [F1s,Cl1s,Br1s,I1s]  u0 {2,S}
6   [C,N,O,S,P] u0 {3,S}
""",
	solute = u'Cl-(Cs-CsFF)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 167,
	label = "Cl-(Cs-CsFF)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S}
4   F1s u0 {2,S}
5   F1s u0 {2,S}
6   [C,N,O,S,P] u0 {3,S}
""",
	solute = SoluteData(
		S = 0.01359,
		B = 0.00444,
		E = -0.01389,
		L = 0.07966,
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
	index = 168,
	label = "Cl-(Cs-CsFCl)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S}
4   F1s u0 {2,S}
5   Cl1s u0 {2,S}
6   [C,N,O,S,P] u0 {3,S}
""",
	solute = SoluteData(
		S = 0.04299,
		B = 0.00958,
		E = -0.00240,
		L = 0.18687,
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
	index = 169,
	label = "Cl-(Cs-CsFBr)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S}
4   F1s u0 {2,S}
5   Br1s u0 {2,S}
6   [C,N,O,S,P] u0 {3,S}
""",
	solute = SoluteData(
		S = 0.03522,
		B = 0.00708,
		E = 0.03587,
		L = 0.24588,
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
	index = 170,
	label = "Cl-(Cs-CsFI)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S}
4   F1s u0 {2,S}
5   I1s u0 {2,S}
6   [C,N,O,S,P] u0 {3,S}
""",
	solute = u'Cl-(Cs-CsFBr)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 171,
	label = "Cl-(Cs-CsClX)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S}
4   Cl1s u0 {2,S}
5   [Cl1s,Br1s,I1s]  u0 {2,S}
6   [C,N,O,S,P] u0 {3,S}
""",
	solute = u'Cl-(Cs-CsClCl)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 172,
	label = "Cl-(Cs-CsClCl)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S}
4   Cl1s u0 {2,S}
5   Cl1s u0 {2,S}
6   [C,N,O,S,P] u0 {3,S}
""",
	solute = SoluteData(
		S = 0.10763,
		B = -0.02250,
		E = 0.12668,
		L = 0.53781,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 5,
		E = 8,
		L = 5,
		A = 5,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 173,
	label = "Cl-(Cs-(Cs-(OH))ClCl)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S}
4   Cl1s u0 {2,S}
5   Cl1s u0 {2,S}
6   O2s  u0 {3,S} {7,S}
7   H    u0 {6,S}
""",
	solute = SoluteData(
		S = 0.08101,
		B = -0.04150,
		E = 0.08764,
		L = 0.47079,
		A = 0.03836,
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
	index = 174,
	label = "Cl-(Cs-CsBrX)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S}
4   Br1s u0 {2,S}
5   [Br1s,I1s]  u0 {2,S}
6   [C,N,O,S,P] u0 {3,S}
""",
	solute = u'Cl-(Cs-CsFBr)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 175,
	label = "Cl-(Cs-CsII)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S}
4   I1s u0 {2,S}
5   I1s u0 {2,S}
6   [C,N,O,S,P] u0 {3,S}
""",
	solute = u'Cl-(Cs-CsBrX)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 176,
	label = "Cl-(Cs-CdZZ)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   [Cd,CO,CS]  u0 {2,S}
4   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = u'Cl-(Cs-(Cd-Cd)ZZ)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 177,
	label = "Cl-(Cs-(Cd-Cd)ZZ)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cd  u0 {2,S} {6,D}
4   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
6   Cd  u0 {3,D}
""",
	solute = u'Cl-(Cs-(Cd-Cd)HH)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 178,
	label = "Cl-(Cs-(Cd-Cd)HH)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cd  u0 {2,S} {6,D}
4   H   u0 {2,S}
5   H   u0 {2,S}
6   Cd  u0 {3,D}
""",
	solute = SoluteData(
		S = 0.22974,
		B = 0.02281,
		E = 0.17909,
		L = 0.77362,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 11,
		B = 11,
		E = 11,
		L = 11,
		A = 12,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 179,
	label = "Cl-(Cs-(Cd-O2d)ZZ)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   CO  u0 {2,S} {6,D}
4   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
6   O2d u0 {3,D}
""",
	solute = u'Cl-(Cs-(Cd-O2d)HH)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 180,
	label = "Cl-(Cs-(Cd-O2d)HH)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   CO  u0 {2,S} {6,D}
4   H   u0 {2,S}
5   H   u0 {2,S}
6   O2d u0 {3,D}
""",
	solute = SoluteData(
		S = 0.08398,
		B = -0.03047,
		E = 0.12191,
		L = 0.36586,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 15,
		B = 14,
		E = 15,
		L = 12,
		A = 16,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 181,
	label = "Cl-(Cs-(Cd-O2d(OH))HH)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   CO  u0 {2,S} {6,S} {8,D}
4   H   u0 {2,S}
5   H   u0 {2,S}
6   O2s u0 {3,S} {7,S}
7   H   u0 {6,S}
8   O2d u0 {3,D}
""",
	solute = SoluteData(
		S = 0.03364,
		B = -0.01587,
		E = 0.06510,
		L = 0.26159,
		A = 0.03724,
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
	index = 182,
	label = "Cl-(Cs-(Cd-O2d)XH)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   CO  u0 {2,S} {6,D}
4   [F1s,Cl1s,Br1s,I1s]  u0 {2,S}
5   H   u0 {2,S}
6   O2d u0 {3,D}
""",
	solute = SoluteData(
		S = 0.00522,
		B = -0.09571,
		E = 0.14509,
		L = 0.57205,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 3,
		E = 7,
		L = 4,
		A = 7,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 183,
	label = "Cl-(Cs-(Cd-O2d(OH))XH)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   CO  u0 {2,S} {6,S} {8,D}
4   [F1s,Cl1s,Br1s,I1s]  u0 {2,S}
5   H   u0 {2,S}
6   O2s u0 {3,S} {7,S}
7   H   u0 {6,S}
8   O2d u0 {3,D}
""",
	solute = SoluteData(
		S = 0.10385,
		B = -0.05053,
		E = 0.10045,
		L = 0.59275,
		A = 0.09486,
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
	index = 184,
	label = "Cl-(Cs-(Cd-O2d)XX)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   CO  u0 {2,S} {6,D}
4   [F1s,Cl1s,Br1s,I1s]  u0 {2,S}
5   [F1s,Cl1s,Br1s,I1s]  u0 {2,S}
6   O2d  u0 {3,D}
""",
	solute = u'Cl-(Cs-(Cd-O2d)ClCl)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 185,
	label = "Cl-(Cs-(Cd-O2d(OH))XX)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   CO  u0 {2,S} {6,S} {8,D}
4   [F1s,Cl1s,Br1s,I1s]  u0 {2,S}
5   [F1s,Cl1s,Br1s,I1s]  u0 {2,S}
6   O2s u0 {3,S} {7,S}
7   H   u0 {6,S}
8   O2d u0 {3,D}
""",
	solute = SoluteData(
		S = 0.08421,
		B = -0.03837,
		E = 0.07972,
		L = 0.55221,
		A = 0.09374,
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
	index = 186,
	label = "Cl-(Cs-(Cd-O2d)ClCl)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   CO  u0 {2,S} {6,D}
4   Cl1s u0 {2,S}
5   Cl1s u0 {2,S}
6   O2d  u0 {3,D}
""",
	solute = SoluteData(
		S = 0.01373,
		B = -0.04185,
		E = 0.07079,
		L = 0.52501,
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
	index = 187,
	label = "Cl-(Cs-CtZZ)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Ct  u0 {2,S}
4   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = SoluteData(
		S = -0.11453,
		B = -0.15203,
		E = -0.01524,
		L = 0.03024,
		A = 0.02564,
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
	index = 188,
	label = "Cl-(Cs-O2sZZ)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   O2s u0 {2,S}
4   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = u'Cl-(Cs-O2sHZ)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 189,
	label = "Cl-(Cs-O2sHZ)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   O2s u0 {2,S}
4   H   u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = SoluteData(
		S = 0.03038,
		B = -0.08138,
		E = 0.09897,
		L = 0.07602,
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
	index = 190,
	label = "Cl-(Cs-O2sXX)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   O2s u0 {2,S}
4   [F1s,Cl1s,Br1s,I1s] u0 {2,S}
5   [F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = u'Cl-(Cs-O2sFF)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 191,
	label = "Cl-(Cs-O2sFF)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   O2s u0 {2,S}
4   F1s u0 {2,S}
5   F1s u0 {2,S}
""",
	solute = SoluteData(
		S = -0.05420,
		B = -0.04083,
		E = 0.07111,
		L = 0.27262,
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
	index = 192,
	label = "Cl-(Cs-CCZ)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   C   u0 {2,S}
4   C   u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = u'Cl-(Cs-CsCsZ)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 193,
	label = "Cl-(Cs-CsCsZ)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   Cs  u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = u'Cl-(Cs-CsCsH)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 194,
	label = "Cl-(Crs-CrsCrsZ)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 r1 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 r1 {2,S}
4   Cs  u0 r1 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = u'Cl-(Crs-CrsCrsH)',
	dataCount = None,
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 195,
	label = "Cl-(Crs-CrsCrsH)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 r1 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 r1 {2,S}
4   Cs  u0 r1 {2,S}
5   H   u0 {2,S}
""",
	solute = SoluteData(
		S = 0.10731,
		B = 0.10686,
		E = 0.20234,
		L = 0.74509,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 14,
		B = 13,
		E = 17,
		L = 14,
		A = 17,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 196,
	label = "Cl-(Crs-CrsCrsX)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 r1 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 r1 {2,S}
4   Cs  u0 r1 {2,S}
5   [F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = u'Cl-(Crs-CrsCrsF)',
	dataCount = None,
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 197,
	label = "Cl-(Crs-CrsCrsF)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 r1 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 r1 {2,S}
4   Cs  u0 r1 {2,S}
5   F1s u0 {2,S}
""",
	solute = SoluteData(
		S = -0.04473,
		B = 0.01903,
		E = -0.01751,
		L = -0.00507,
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
	index = 198,
	label = "Cl-(Crs-CrsCrsCl)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 r1 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 r1 {2,S}
4   Cs  u0 r1 {2,S}
5   Cl1s u0 {2,S}
""",
	solute = SoluteData(
		S = 0.08731,
		B = 0.02678,
		E = 0.13683,
		L = 0.65129,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 15,
		B = 15,
		E = 16,
		L = 15,
		A = 16,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 199,
	label = "Cl-(Cs-CsCsH)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   Cs  u0 {2,S}
5   H   u0 {2,S}
""",
	solute = SoluteData(
		S = 0.11424,
		B = 0.04608,
		E = 0.12531,
		L = 0.59153,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 10,
		B = 10,
		E = 14,
		L = 10,
		A = 12,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 200,
	label = "Cl-(Cs-CsCsX)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   Cs  u0 {2,S}
5   [F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = u'Cl-(Cs-CsCsF)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 201,
	label = "Cl-(Cs-CsCsF)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   Cs  u0 {2,S}
5   F1s u0 {2,S}
""",
	solute = SoluteData(
		S = 0.03285,
		B = 0.00000,
		E = -0.00328,
		L = 0.14682,
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
	index = 202,
	label = "Cl-(Cs-CsCsCl)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   Cs  u0 {2,S}
5   Cl1s u0 {2,S}
""",
	solute = SoluteData(
		S = 0.11565,
		B = 0.01803,
		E = 0.10940,
		L = 0.49549,
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
	index = 203,
	label = "Cl-(Cs-CsCdZ)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   [Cd,CO,CS]  u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = u'Cl-(Cs-Cs(Cd-Cd)Z)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 204,
	label = "Cl-(Cs-Cs(Cd-Cd)Z)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   Cd  u0 {2,S} {6,D}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
6   Cd  u0 {4,D}
""",
	solute = u'Cl-(Cs-Cs(Cd-Cd)H)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 205,
	label = "Cl-(Cs-Cs(Cd-Cd)H)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   Cd  u0 {2,S} {6,D}
5   H   u0 {2,S}
6   Cd  u0 {4,D}
""",
	solute = SoluteData(
		S = 0.07865,
		B = 0.02077,
		E = 0.11312,
		L = 0.56330,
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
	index = 206,
	label = "Cl-(Cs-Cs(Cd-O2d)Z)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   CO  u0 {2,S} {6,D}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
6   O2d u0 {4,D}
""",
	solute = u'Cl-(Cs-Cs(Cd-O2d)H)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 207,
	label = "Cl-(Cs-Cs(Cd-O2d)H)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   CO  u0 {2,S} {6,D}
5   H   u0 {2,S}
6   O2d u0 {4,D}
""",
	solute = SoluteData(
		S = 0.06606,
		B = -0.02040,
		E = 0.09521,
		L = 0.50264,
		A = 0.03733,
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
	index = 208,
	label = "Cl-(Cs-CO2sZ)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   C   u0 {2,S}
4   O2s u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = u'Cl-(Cs-CsO2sZ)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 209,
	label = "Cl-(Cs-CsO2sZ)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   O2s u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = u'Cl-(Cs-CsO2sH)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 210,
	label = "Cl-(Cs-CsO2sH)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   O2s u0 {2,S}
5   H   u0 {2,S}
""",
	solute = SoluteData(
		S = 0.03993,
		B = -0.03279,
		E = 0.04192,
		L = 0.27012,
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
	index = 211,
	label = "Cl-(Cs-CsO2sX)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   O2s u0 {2,S}
5   [F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = SoluteData(
		S = -0.07917,
		B = -0.03240,
		E = 0.09510,
		L = 0.36421,
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
	index = 212,
	label = "Cl-(Cs-CCC)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   C   u0 {2,S}
4   C   u0 {2,S}
5   C   u0 {2,S}
""",
	solute = u'Cl-(Cs-CsCsCs)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 213,
	label = "Cl-(Crs-CrCrCr)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 r1 {1,S} {3,S} {4,S} {5,S}
3   C   u0 r1 {2,S}
4   C   u0 r1 {2,S}
5   C   u0 r1 {2,S}
""",
	solute = SoluteData(
		S = 0.09055,
		B = 0.11798,
		E = 0.24303,
		L = 0.77872,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 15,
		B = 15,
		E = 16,
		L = 15,
		A = 16,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 214,
	label = "Cl-(Cs-CsCsCs)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   Cs  u0 {2,S}
5   Cs  u0 {2,S}
""",
	solute = SoluteData(
		S = 0.11021,
		B = 0.04934,
		E = 0.10790,
		L = 0.53701,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 4,
		B = 5,
		E = 4,
		L = 4,
		A = 5,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 215,
	label = "Cl-(Cs-N5dc)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cs   u0 {1,S} {3,S}
3   N5dc u0 {2,S}
""",
	solute = SoluteData(
		S = 0.05314,
		B = 0.00000,
		E = 0.08697,
		L = 0.45931,
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
	index = 216,
	label = "Cl-Cd",
	group = 
"""
1 * Cl1s u0 {2,S}
2   [Cd,CO,CS] u0 {1,S}
""",
	solute = u'Cl-(Cd-Cd)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 217,
	label = "Cl-(Cd-Cd)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cd   u0 {1,S} {3,D}
3   C    u0 {2,D}
""",
	solute = u'Cl-(Cd-CdC)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 218,
	label = "Cl-(Cd-CdC)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cd   u0 {1,S} {3,D} {4,S}
3   C    u0 {2,D}
4   C    u0 {2,S}
""",
	solute = u'Cl-(Cd-CdCs)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 219,
	label = "Cl-(Crd-CrdCr)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cd   u0 r1 {1,S} {3,D} {4,S}
3   C    u0 r1 {2,D}
4   C    u0 r1 {2,S}
""",
	solute = u'Cl-(Crd-CrdCrs)',
	dataCount = None,
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 220,
	label = "Cl-(Crd-CrdCrs)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cd   u0 r1 {1,S} {3,D} {4,S}
3   C    u0 r1 {2,D}
4   Cs   u0 r1 {2,S}
""",
	solute = SoluteData(
		S = -0.01559,
		B = -0.04241,
		E = 0.12255,
		L = 0.30981,
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
	index = 221,
	label = "Cl-(Crd-CrdCrd)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cd   u0 r1 {1,S} {3,D} {4,S}
3   C    u0 r1 {2,D}
4   [Cd,CO,CS]   u0 r1 {2,S}
""",
	solute = u'Cl-(Crd-Crd(Crd-Crd))',
	dataCount = None,
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 222,
	label = "Cl-(Crd-Crd(Crd-Crd))",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cd   u0 r1 {1,S} {3,D} {4,S}
3   C    u0 r1 {2,D}
4   Cd   u0 r1 {2,S} {5,D}
5   C    u0 r1 {4,D}
""",
	solute = SoluteData(
		S = 0.11193,
		B = -0.02295,
		E = 0.12996,
		L = 0.79760,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 15,
		B = 15,
		E = 16,
		L = 15,
		A = 16,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 223,
	label = "Cl-(Crd-Crd(Crd-Nrd))",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cd   u0 r1 {1,S} {3,D} {4,S}
3   C    u0 r1 {2,D}
4   Cd   u0 r1 {2,S} {5,D}
5   N    u0 r1 {4,D}
""",
	solute = SoluteData(
		S = 0.00481,
		B = -0.05095,
		E = 0.07807,
		L = 0.20600,
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
	index = 224,
	label = "Cl-(Crd-Crd(Crd-O2d))",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cd   u0 r1 {1,S} {3,D} {4,S}
3   C    u0 r1 {2,D}
4   CO   u0 r1 {2,S} {5,D}
5   O2d  u0 {4,D}
""",
	solute = SoluteData(
		S = -0.02747,
		B = 0.03784,
		E = 0.18468,
		L = 0.48334,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 5,
		E = 5,
		L = 5,
		A = 6,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 225,
	label = "Cl-(Cd-CdCs)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cd   u0 {1,S} {3,D} {4,S}
3   C    u0 {2,D}
4   Cs   u0 {2,S}
""",
	solute = SoluteData(
		S = 0.06372,
		B = 0.00746,
		E = 0.13515,
		L = 0.62671,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 11,
		B = 11,
		E = 11,
		L = 11,
		A = 12,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 226,
	label = "Cl-(Cd-CdN)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cd   u0 {1,S} {3,D} {4,S}
3   C    u0 {2,D}
4   N    u0 {2,S}
""",
	solute = u'Cl-(Crd-CrdNr)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 227,
	label = "Cl-(Crd-CrdNr)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cd   u0 r1 {1,S} {3,D} {4,S}
3   C    u0 r1 {2,D}
4   N    u0 r1 {2,S}
""",
	solute = SoluteData(
		S = 0.00459,
		B = -0.06724,
		E = 0.10540,
		L = 0.57315,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 8,
		B = 8,
		E = 10,
		L = 9,
		A = 9,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 228,
	label = "Cl-(Cd-CdS)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cd   u0 {1,S} {3,D} {4,S}
3   C    u0 {2,D}
4   S    u0 {2,S}
""",
	solute = u'Cl-(Crd-CrdSr)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 229,
	label = "Cl-(Crd-CrdSr)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cd   u0 r1 {1,S} {3,D} {4,S}
3   C    u0 r1 {2,D}
4   S    u0 r1 {2,S}
""",
	solute = u'Cl-(Crd-CrdNr)',
	dataCount = None,
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 230,
	label = "Cl-(Cd-CdZ)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cd   u0 {1,S} {3,D} {4,S}
3   C    u0 {2,D}
4   [H,F1s,Cl1s,Br1s,I1s]  u0 {2,S}
""",
	solute = u'Cl-(Cd-CdH)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 231,
	label = "Cl-(Cd-CdH)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cd   u0 {1,S} {3,D} {4,S}
3   C    u0 {2,D}
4   H    u0 {2,S}
""",
	solute = SoluteData(
		S = 0.14002,
		B = -0.02380,
		E = 0.11119,
		L = 0.68144,
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
	index = 232,
	label = "Cl-(Cd-CdX)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cd   u0 {1,S} {3,D} {4,S}
3   C    u0 {2,D}
4   [F1s,Cl1s,Br1s,I1s]  u0 {2,S}
""",
	solute = u'Cl-(Cd-CdCl)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 233,
	label = "Cl-(Cd-CdCl)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cd   u0 {1,S} {3,D} {4,S}
3   C    u0 {2,D}
4   Cl1s u0 {2,S}
""",
	solute = SoluteData(
		S = 0.00652,
		B = 0.00000,
		E = 0.08894,
		L = 0.55869,
		A = 0.00000,
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
	index = 234,
	label = "Cl-(Cd-Nd)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cd   u0 {1,S} {3,D}
3   N    u0 {2,D}
""",
	solute = u'Cl-(Cd-NdN)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 235,
	label = "Cl-(Cd-NdC)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cd   u0 {1,S} {3,D} {4,S}
3   N    u0 {2,D}
4   C    u0 {2,S}
""",
	solute = u'Cl-(Crd-NrdCr)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 236,
	label = "Cl-(Crd-NrdCr)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cd   u0 r1 {1,S} {3,D} {4,S}
3   N    u0 r1 {2,D}
4   C    u0 r1 {2,S}
""",
	solute = SoluteData(
		S = 0.06871,
		B = 0.00000,
		E = 0.08195,
		L = 0.38848,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 6,
		E = 6,
		L = 4,
		A = 6,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 237,
	label = "Cl-(Cd-NdN)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cd   u0 {1,S} {3,D} {4,S}
3   N    u0 {2,D}
4   N    u0 {2,S}
""",
	solute = u'Cl-(Crd-NrdNr)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 238,
	label = "Cl-(Crd-NrdNr)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   Cd   u0 r1 {1,S} {3,D} {4,S}
3   N    u0 r1 {2,D}
4   N    u0 r1 {2,S}
""",
	solute = SoluteData(
		S = 0.06360,
		B = 0.00606,
		E = 0.14775,
		L = 0.46397,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 9,
		B = 9,
		E = 10,
		L = 9,
		A = 10,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 239,
	label = "Cl-(Cd-O2d)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   CO   u0 {1,S} {3,D}
3   O2d  u0 {2,D}
""",
	solute = SoluteData(
		S = -0.00734,
		B = -0.10685,
		E = -0.05252,
		L = -0.08603,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 2,
		B = 2,
		E = 5,
		L = 1,
		A = 5,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 240,
	label = "Cl-N",
	group = 
"""
1 * Cl1s u0 {2,S}
2   N    u0 {1,S}
""",
	solute = u'Cl-N3s',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 241,
	label = "Cl-N3s",
	group = 
"""
1 * Cl1s u0 {2,S}
2   N3s  u0 {1,S}
""",
	solute = u'Cl-(N3s-C)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 242,
	label = "Cl-(N3s-C)",
	group = 
"""
1 * Cl1s u0 {2,S}
2   N3s  u0 {1,S} {3,S}
3   C    u0 {2,S}
""",
	solute = u'Cl-(N3s-(Cd-O2d))',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 243,
	label = "Cl-(N3s-(Cd-O2d))",
	group = 
"""
1 * Cl1s u0 {2,S}
2   N3s  u0 {1,S} {3,S}
3   CO   u0 {2,S}
""",
	solute = SoluteData(
		S = 0.15163,
		B = -0.14953,
		E = 0.04020,
		L = 0.65885,
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
	index = 244,
	label = "Cl-P",
	group = 
"""
1 * Cl1s u0 {2,S}
2   P    u0 {1,S}
""",
	solute = u'Cl-P5d',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 245,
	label = "Cl-P5d",
	group = 
"""
1 * Cl1s u0 {2,S}
2   P5d  u0 {1,S}
""",
	solute = SoluteData(
		S = 0.20458,
		B = -0.01805,
		E = 0.07937,
		L = 0.74524,
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
	index = 246,
	label = "Br",
	group = 
"""
1 * Br1s u0
""",
	solute = u'Br-C',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 247,
	label = "Br-C",
	group = 
"""
1 * Br1s u0 {2,S}
2   C    u0 {1,S}
""",
	solute = u'Br-Cs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 248,
	label = "Br-Cb",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cb   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.16175,
		B = -0.03229,
		E = 0.30694,
		L = 1.13072,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 112,
		B = 112,
		E = 119,
		L = 84,
		A = 120,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 249,
	label = "Br-Phenol",
	group =  "OR{Br-Phenol(ortho), Br-Phenol(meta), Br-Phenol(para)}",
	solute = None,
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 250,
	label = "Br-Phenol(ortho)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cb  u0 {1,S} {3,B}
3   Cb  u0 {2,B} {4,S}
4   O2s u0 {3,S} {5,S}
5   H   u0 {4,S}
""",
	solute = SoluteData(
		S = 0.17563,
		B = -0.04015,
		E = 0.27440,
		L = 1.13285,
		A = 0.00355,
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
	index = 251,
	label = "Br-Phenol(meta)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cb  u0 {1,S} {3,B}
3   Cb  u0 {2,B} {4,B}
4   Cb  u0 {3,B} {5,S}
5   O2s u0 {4,S} {6,S}
6   H   u0 {5,S}
""",
	solute = SoluteData(
		S = 0.23572,
		B = -0.06201,
		E = 0.30228,
		L = 1.22823,
		A = 0.15664,
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
	index = 252,
	label = "Br-Phenol(para)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cb  u0 {1,S} {3,B}
3   Cb  u0 {2,B} {4,B}
4   Cb  u0 {3,B} {5,B}
5   Cb  u0 {4,B} {6,S}
6   O2s u0 {5,S} {7,S}
7   H   u0 {6,S}
""",
	solute = SoluteData(
		S = 0.07998,
		B = -0.04863,
		E = 0.23943,
		L = 0.79144,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 9,
		B = 9,
		E = 9,
		L = 9,
		A = 10,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 253,
	label = "Br-BenzoicAcid",
	group =  "OR{Br-BenzoicAcid(ortho), Br-BenzoicAcid(meta), Br-BenzoicAcid(para)}",
	solute = None,
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 254,
	label = "Br-BenzoicAcid(ortho)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cb  u0 {1,S} {3,B}
3   Cb  u0 {2,B} {4,S}
4   CO  u0 {3,S} {5,S}
5   O2s u0 {4,S} {6,S}
6   H   u0 {5,S}
""",
	solute = SoluteData(
		S = 0.11375,
		B = 0.05300,
		E = 0.19576,
		L = 0.83805,
		A = 0.07289,
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
	label = "Br-BenzoicAcid(meta)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cb  u0 {1,S} {3,B}
3   Cb  u0 {2,B} {4,B}
4   Cb  u0 {3,B} {5,S}
5   CO  u0 {4,S} {6,S}
6   O2s u0 {5,S} {7,S}
7   H   u0 {6,S}
""",
	solute = SoluteData(
		S = 0.05818,
		B = -0.04321,
		E = 0.12389,
		L = 0.61285,
		A = 0.03086,
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
	index = 256,
	label = "Br-BenzoicAcid(para)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cb  u0 {1,S} {3,B}
3   Cb  u0 {2,B} {4,B}
4   Cb  u0 {3,B} {5,B}
5   Cb  u0 {4,B} {6,S}
6   CO  u0 {5,S} {7,S}
7   O2s u0 {6,S} {8,S}
8   H   u0 {7,S}
""",
	solute = SoluteData(
		S = 0.01354,
		B = -0.02133,
		E = 0.06559,
		L = 0.28982,
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
	index = 257,
	label = "Br-Aniline",
	group =  "OR{Br-Aniline(ortho), Br-Aniline(meta), Br-Aniline(para)}",
	solute = None,
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 258,
	label = "Br-Aniline(ortho)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cb  u0 {1,S} {3,B}
3   Cb  u0 {2,B} {4,S}
4   N3s u0 {3,S} {5,S} {6,S}
5   H   u0 {4,S}
6   H   u0 {4,S}
""",
	solute = SoluteData(
		S = -0.00259,
		B = -0.01901,
		E = 0.04200,
		L = 0.26830,
		A = 0.01420,
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
	index = 259,
	label = "Br-Aniline(meta)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cb  u0 {1,S} {3,B}
3   Cb  u0 {2,B} {4,B}
4   Cb  u0 {3,B} {5,S}
5   N3s u0 {4,S} {6,S} {7,S}
6   H   u0 {5,S}
7   H   u0 {5,S}
""",
	solute = SoluteData(
		S = 0.02366,
		B = -0.02401,
		E = 0.06133,
		L = 0.31164,
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
	index = 260,
	label = "Br-Aniline(para)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cb  u0 {1,S} {3,B}
3   Cb  u0 {2,B} {4,B}
4   Cb  u0 {3,B} {5,B}
5   Cb  u0 {4,B} {6,S}
6   N3s u0 {5,S} {7,S} {8,S}
7   H   u0 {6,S}
8   H   u0 {6,S}
""",
	solute = SoluteData(
		S = 0.03677,
		B = -0.01786,
		E = 0.12381,
		L = 0.32564,
		A = 0.01366,
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
	index = 261,
	label = "Br-Cs",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs   u0 {1,S}
""",
	solute = u'Br-(Cs-CZZ)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 262,
	label = "Br-(Cs-CZZ)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   C   u0 {2,S}
4   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = u'Br-(Cs-CsZZ)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 263,
	label = "Br-(Cs-CbZZ)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cb  u0 {2,S}
4   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = SoluteData(
		S = 0.14080,
		B = 0.04528,
		E = 0.29736,
		L = 1.07189,
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
	index = 264,
	label = "Br-(Cs-CsZZ)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = u'Br-(Cs-CsHH)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 265,
	label = "Br-(Cs-CsHH)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   H   u0 {2,S}
5   H   u0 {2,S}
""",
	solute = SoluteData(
		S = 0.37495,
		B = 0.10712,
		E = 0.33350,
		L = 1.23423,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 39,
		B = 39,
		E = 41,
		L = 35,
		A = 41,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 266,
	label = "Br-(Cs-(Cs-ZZZ)HH)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S} {7,S} {8,S}
4   H   u0 {2,S}
5   H   u0 {2,S}
6   [H,F1s,Cl1s,Br1s,I1s] u0 {3,S}
7   [H,F1s,Cl1s,Br1s,I1s] u0 {3,S}
8   [H,F1s,Cl1s,Br1s,I1s] u0 {3,S}
""",
	solute = u'Br-(Cs-(Cs-HHH)HH)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 267,
	label = "Br-(Cs-(Cs-HHH)HH)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S} {7,S} {8,S}
4   H   u0 {2,S}
5   H   u0 {2,S}
6   H   u0 {3,S}
7   H   u0 {3,S}
8   H   u0 {3,S}
""",
	solute = SoluteData(
		S = 0.05000,
		B = 0.03000,
		E = 0.12200,
		L = 0.27544,
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
	index = 268,
	label = "Br-(Cs-(Cs-HHX)HH)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S} {7,S} {8,S}
4   H   u0 {2,S}
5   H   u0 {2,S}
6   H   u0 {3,S}
7   H   u0 {3,S}
8   [F1s,Cl1s,Br1s,I1s] u0 {3,S}
""",
	solute = SoluteData(
		S = 0.20967,
		B = 0.05812,
		E = 0.26832,
		L = 0.78227,
		A = 0.03518,
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
	index = 269,
	label = "Br-(Cs-(Cs-HXX)HH)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S} {7,S} {8,S}
4   H   u0 {2,S}
5   H   u0 {2,S}
6   H   u0 {3,S}
7   [F1s,Cl1s,Br1s,I1s] u0 {3,S}
8   [F1s,Cl1s,Br1s,I1s] u0 {3,S}
""",
	solute = u'Br-(Cs-(Cs-HHX)HH)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 270,
	label = "Br-(Cs-(Cs-XXX)HH)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S} {6,S} {7,S} {8,S}
4   H   u0 {2,S}
5   H   u0 {2,S}
6   [F1s,Cl1s,Br1s,I1s] u0 {3,S}
7   [F1s,Cl1s,Br1s,I1s] u0 {3,S}
8   [F1s,Cl1s,Br1s,I1s] u0 {3,S}
""",
	solute = SoluteData(
		S = 0.01796,
		B = 0.00954,
		E = 0.07761,
		L = 0.25105,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 1,
		B = 1,
		E = 1,
		L = 1,
		A = 2,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 271,
	label = "Br-(Cs-CsXH)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   H   u0 {2,S}
5   [F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = u'Br-(Cs-CsFH)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 272,
	label = "Br-(Cs-CsFH)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   H   u0 {2,S}
5   F1s u0 {2,S}
""",
	solute = SoluteData(
		S = 0.10511,
		B = 0.01812,
		E = 0.15848,
		L = 0.63214,
		A = 0.00986,
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
	index = 273,
	label = "Br-(Cs-CsClH)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   H   u0 {2,S}
5   Cl1s u0 {2,S}
""",
	solute = SoluteData(
		S = 0.11927,
		B = 0.01931,
		E = 0.15647,
		L = 0.59840,
		A = 0.00703,
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
	index = 274,
	label = "Br-(Cs-CsBrH)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   H   u0 {2,S}
5   Br1s u0 {2,S}
""",
	solute = SoluteData(
		S = 0.18583,
		B = 0.05037,
		E = 0.29800,
		L = 0.95060,
		A = 0.03483,
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
	index = 275,
	label = "Br-(Cs-CsIH)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   H   u0 {2,S}
5   I1s u0 {2,S}
""",
	solute = u'Br-(Cs-CsClH)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 276,
	label = "Br-(Cs-CsXX)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   [F1s,Cl1s,Br1s,I1s]  u0 {2,S}
5   [F1s,Cl1s,Br1s,I1s]  u0 {2,S}
""",
	solute = u'Br-(Cs-CsFX)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 277,
	label = "Br-(Cs-CsFX)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   F1s  u0 {2,S}
5   [F1s,Cl1s,Br1s,I1s]  u0 {2,S}
""",
	solute = u'Br-(Cs-CsFF)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 278,
	label = "Br-(Cs-CsFF)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   F1s  u0 {2,S}
5   F1s  u0 {2,S}
""",
	solute = SoluteData(
		S = 0.09289,
		B = 0.00000,
		E = 0.19934,
		L = 0.77379,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 11,
		B = 11,
		E = 11,
		L = 11,
		A = 12,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 279,
	label = "Br-(Cs-CsFCl)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   F1s  u0 {2,S}
5   Cl1s  u0 {2,S}
""",
	solute = SoluteData(
		S = 0.06749,
		B = 0.00000,
		E = 0.11328,
		L = 0.51454,
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
	index = 280,
	label = "Br-(Cs-CsFBr)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   F1s  u0 {2,S}
5   Br1s  u0 {2,S}
""",
	solute = SoluteData(
		S = 0.09411,
		B = 0.02047,
		E = 0.14201,
		L = 0.55406,
		A = -0.00917,
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
	index = 281,
	label = "Br-(Cs-CsFI)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   F1s  u0 {2,S}
5   I1s  u0 {2,S}
""",
	solute = u'Br-(Cs-CsClH)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 282,
	label = "Br-(Cs-CsClX)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   Cl1s  u0 {2,S}
5   [Cl1s,Br1s,I1s]  u0 {2,S}
""",
	solute = u'Br-(Cs-CsFCl)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 283,
	label = "Br-(Cs-CsBrX)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   Br1s  u0 {2,S}
5   [Br1s,I1s]  u0 {2,S}
""",
	solute = u'Br-(Cs-CsFBr)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 284,
	label = "Br-(Cs-CsII)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   I1s  u0 {2,S}
5   I1s  u0 {2,S}
""",
	solute = u'Br-(Cs-CsFI)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 285,
	label = "Br-(Cs-CdZZ)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   [Cd,CO,CS]  u0 {2,S}
4   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = u'Br-(Cs-(Cd-Cd)ZZ)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 286,
	label = "Br-(Cs-(Cd-Cd)ZZ)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cd  u0 {2,S} {6,D}
4   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
6   Cd  u0 {3,D}
""",
	solute = SoluteData(
		S = 0.04698,
		B = 0.01251,
		E = 0.12118,
		L = 0.40588,
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
	index = 287,
	label = "Br-(Cs-(Cd-O2d)ZZ)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   CO  u0 {2,S} {6,D}
4   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
6   O2d u0 {3,D}
""",
	solute = SoluteData(
		S = 0.15375,
		B = 0.01091,
		E = 0.21845,
		L = 0.91472,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 5,
		B = 5,
		E = 9,
		L = 5,
		A = 8,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 288,
	label = "Br-(Cs-(Cd-O2d(OH))ZZ)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   CO  u0 {2,S} {6,D} {7,S}
4   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
6   O2d u0 {3,D}
7   O2s u0 {3,S} {8,S}
8   H   u0 {7,S}
""",
	solute = None,
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 289,
	label = "Br-(Cs-(Cd-O2d(OH))HH)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   CO  u0 {2,S} {6,D} {7,S}
4   H   u0 {2,S}
5   H   u0 {2,S}
6   O2d u0 {3,D}
7   O2s u0 {3,S} {8,S}
8   H   u0 {7,S}
""",
	solute = SoluteData(
		S = 0.03739,
		B = -0.00837,
		E = 0.10810,
		L = 0.40126,
		A = 0.03324,
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
	index = 290,
	label = "Br-(Cs-(Cd-O2d(OH))XH)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   CO  u0 {2,S} {6,D} {7,S}
4   [F1s,Cl1s,Br1s,I1s] u0 {2,S}
5   H   u0 {2,S}
6   O2d u0 {3,D}
7   O2s u0 {3,S} {8,S}
8   H   u0 {7,S}
""",
	solute = SoluteData(
		S = 0.11112,
		B = -0.03625,
		E = 0.20578,
		L = 0.87408,
		A = 0.09486,
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
	index = 291,
	label = "Br-(Cs-(Cd-O2d(OH))XX)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   CO  u0 {2,S} {6,D} {7,S}
4   [F1s,Cl1s,Br1s,I1s] u0 {2,S}
5   [F1s,Cl1s,Br1s,I1s] u0 {2,S}
6   O2d u0 {3,D}
7   O2s u0 {3,S} {8,S}
8   H   u0 {7,S}
""",
	solute = SoluteData(
		S = 0.09358,
		B = -0.02587,
		E = 0.23108,
		L = 0.93757,
		A = 0.08681,
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
	index = 292,
	label = "Br-(Cs-CtZZ)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Ct  u0 {2,S}
4   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = SoluteData(
		S = -0.06813,
		B = -0.07590,
		E = 0.13418,
		L = 0.26379,
		A = 0.05856,
	),
	dataCount = DataCountGAV(
		S = 2,
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
	index = 293,
	label = "Br-(Cs-CCZ)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   C   u0 {2,S}
4   C   u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = u'Br-(Cs-CsCsZ)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 294,
	label = "Br-(Cs-CsCsZ)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   Cs  u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = u'Br-(Cs-CsCsH)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 295,
	label = "Br-(Cs-CsCsH)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   Cs  u0 {2,S}
5   H   u0 {2,S}
""",
	solute = SoluteData(
		S = 0.28618,
		B = 0.11702,
		E = 0.30404,
		L = 1.22154,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 25,
		B = 25,
		E = 26,
		L = 21,
		A = 26,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 296,
	label = "Br-(Cs-CsCsX)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   Cs  u0 {2,S}
5   [F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = u'Br-(Cs-CsCsF)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 297,
	label = "Br-(Cs-CsCsF)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   Cs  u0 {2,S}
5   F1s u0 {2,S}
""",
	solute = SoluteData(
		S = 0.00518,
		B = -0.01293,
		E = 0.05413,
		L = 0.15575,
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
	index = 298,
	label = "Br-(Cs-CsCbZ)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   Cb  u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = u'Br-(Cs-CbZZ)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 299,
	label = "Br-(Cs-CsCdZ)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   [Cd,CO,CS]  u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = u'Br-(Cs-Cs(Cd-Cd)Z)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 300,
	label = "Br-(Cs-Cs(Cd-Cd)Z)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   Cd  u0 {2,S} {6,D}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
6   Cd  u0 {4,D}
""",
	solute = u'Br-(Cs-(Cd-Cd)ZZ)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 301,
	label = "Br-(Cs-Cs(Cd-O2d)Z)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   CO  u0 {2,S} {6,D}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
6   O2d u0 {4,D}
""",
	solute = u'Br-(Cs-Cs(Cd-O2d)H)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 302,
	label = "Br-(Cs-Cs(Cd-O2d)H)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   CO  u0 {2,S} {6,D}
5   H   u0 {2,S}
6   O2d u0 {4,D}
""",
	solute = SoluteData(
		S = 0.02293,
		B = -0.00075,
		E = 0.21061,
		L = 0.62351,
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
	index = 303,
	label = "Br-(Cs-Cs(Cd-O2d(OH))H)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   CO  u0 {2,S} {6,D} {7,S}
5   H   u0 {2,S}
6   O2d u0 {4,D}
7   O2s u0 {4,S} {8,S}
8   H   u0 {7,S}
""",
	solute = SoluteData(
		S = 0.13110,
		B = -0.04723,
		E = 0.18070,
		L = 0.76259,
		A = 0.06266,
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
	index = 304,
	label = "Br-(Cs-CO2sZ)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   C   u0 {2,S}
4   O2s u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = SoluteData(
		S = 0.00612,
		B = -0.01410,
		E = 0.14243,
		L = 0.48767,
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
	index = 305,
	label = "Br-(Cs-CCC)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   C   u0 {2,S}
4   C   u0 {2,S}
5   C   u0 {2,S}
""",
	solute = u'Br-(Cs-CsCsCs)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 306,
	label = "Br-(Cs-CsCsCs)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   Cs  u0 {2,S}
5   Cs  u0 {2,S}
""",
	solute = SoluteData(
		S = 0.08195,
		B = 0.05646,
		E = 0.19966,
		L = 0.65970,
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
	index = 307,
	label = "Br-(Cs-CsCsCb)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   Cs  u0 {2,S}
5   Cb  u0 {2,S}
""",
	solute = u'Br-(Cs-CbZZ)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 308,
	label = "Br-(Cs-CsCsCd)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   Cs  u0 {2,S}
5   [Cd,CO,CS]  u0 {2,S}
""",
	solute = u'Br-(Cs-CsCs(Cd-Cd))',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 309,
	label = "Br-(Cs-CsCs(Cd-Cd))",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   Cs  u0 {2,S}
5   Cd  u0 {2,S} {6,D}
6   Cd  u0 {5,D}
""",
	solute = u'Br-(Cs-(Cd-Cd)ZZ)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 310,
	label = "Br-(Cs-CsCs(Cd-O2d))",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   Cs  u0 {2,S}
5   CO  u0 {2,S} {6,D}
6   O2d u0 {5,D}
""",
	solute = u'Br-(Cs-Cs(Cd-O2d)H)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 311,
	label = "Br-Cd",
	group = 
"""
1 * Br1s u0 {2,S}
2   [Cd,CO,CS] u0 {1,S}
""",
	solute = u'Br-(Cd-Cd)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 312,
	label = "Br-(Cd-Cd)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cd   u0 {1,S} {3,D}
3   C    u0 {2,D}
""",
	solute = u'Br-(Cd-CdZ)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 313,
	label = "Br-(Cd-CdZ)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cd   u0 {1,S} {3,D} {4,S}
3   C    u0 {2,D}
4   [H,F1s,Cl1s,Br1s,I1s]  u0 {2,S}
""",
	solute = SoluteData(
		S = 0.15019,
		B = 0.00000,
		E = 0.25124,
		L = 0.95384,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 9,
		B = 6,
		E = 7,
		L = 5,
		A = 10,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 314,
	label = "Br-(Cd-CdC)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cd   u0 {1,S} {3,D} {4,S}
3   C    u0 {2,D}
4   C    u0 {2,S}
""",
	solute = None,
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 315,
	label = "Br-(Cd-CdCd)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cd   u0 {1,S} {3,D} {4,S}
3   C    u0 {2,D}
4   [Cd,CO,CS]   u0 {2,S}
""",
	solute = None,
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 316,
	label = "Br-(Crd-CrdCrd)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cd   u0 r1 {1,S} {3,D} {4,S}
3   C    u0 r1 {2,D}
4   [Cd,CO,CS]   u0 r1 {2,S}
""",
	solute = SoluteData(
		S = 0.13580,
		B = -0.05362,
		E = 0.25784,
		L = 0.85193,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 15,
		B = 15,
		E = 16,
		L = 10,
		A = 16,
	),
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 317,
	label = "Br-(Cd-CdCs)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cd   u0 {1,S} {3,D} {4,S}
3   C    u0 {2,D}
4   Cs   u0 {2,S}
""",
	solute = u'Br-(Cd-CdZ)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 318,
	label = "Br-(Cd-CdN)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cd   u0 {1,S} {3,D} {4,S}
3   C    u0 {2,D}
4   N    u0 {2,S}
""",
	solute = None,
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 319,
	label = "Br-(Cd-CdN3d)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cd   u0 {1,S} {3,D} {4,S}
3   C    u0 {2,D}
4   N3d  u0 {2,S}
""",
	solute = None,
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 320,
	label = "Br-(Crd-CrdN3rd)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cd   u0 r1 {1,S} {3,D} {4,S}
3   C    u0 r1 {2,D}
4   N3d  u0 r1 {2,S}
""",
	solute = u'Br-(Crd-CrdCrd)',
	dataCount = None,
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 321,
	label = "Br-(Cd-CdO2s)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cd   u0 {1,S} {3,D} {4,S}
3   C    u0 {2,D}
4   O2s  u0 {2,S}
""",
	solute = None,
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 322,
	label = "Br-(Crd-CrdO2rs)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cd   u0 r1 {1,S} {3,D} {4,S}
3   C    u0 r1 {2,D}
4   O2s  u0 r1 {2,S}
""",
	solute = u'Br-(Crd-CrdCrd)',
	dataCount = None,
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 323,
	label = "Br-(Cd-Nd)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cd   u0 {1,S} {3,D}
3   N    u0 {2,D}
""",
	solute = None,
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 324,
	label = "Br-(Cd-NdN)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cd   u0 {1,S} {3,D} {4,S}
3   N    u0 {2,D}
4   N    u0 {2,S}
""",
	solute = None,
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 325,
	label = "Br-(Cd-N3dN3d)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cd   u0 {1,S} {3,D} {4,S}
3   N3d  u0 {2,D}
4   N3d  u0 {2,S}
""",
	solute = None,
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 326,
	label = "Br-(Crd-N3rdN3rd)",
	group = 
"""
1 * Br1s u0 {2,S}
2   Cd   u0 r1 {1,S} {3,D} {4,S}
3   N3d  u0 r1 {2,D}
4   N3d  u0 r1 {2,S}
""",
	solute = u'Br-(Crd-CrdN3rd)',
	dataCount = None,
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 327,
	label = "Br-N",
	group = 
"""
1 * Br1s u0 {2,S}
2   N    u0 {1,S}
""",
	solute = None,
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 328,
	label = "Br-N3s",
	group = 
"""
1 * Br1s u0 {2,S}
2   N3s  u0 {1,S}
""",
	solute = None,
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 329,
	label = "Br-(N3s-CH)",
	group = 
"""
1 * Br1s u0 {2,S}
2   N3s  u0 {1,S} {3,S} {4,S}
3   C    u0 {2,S}
4   H    u0 {2,S}
""",
	solute = None,
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 330,
	label = "Br-(N3s-(Cd-O2d)H)",
	group = 
"""
1 * Br1s u0 {2,S}
2   N3s  u0 {1,S} {3,S} {4,S}
3   CO   u0 {2,S}
4   H    u0 {2,S}
""",
	solute = SoluteData(
		S = 0.04429,
		B = -0.06935,
		E = 0.06070,
		L = 0.33856,
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
	index = 331,
	label = "I",
	group = 
"""
1 * I1s u0
""",
	solute = u'I-C',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 332,
	label = "I-C",
	group = 
"""
1 * I1s  u0 {2,S}
2   C    u0 {1,S}
""",
	solute = u'I-Cs',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 333,
	label = "I-Cb",
	group = 
"""
1 * I1s  u0 {2,S}
2   Cb   u0 {1,S}
""",
	solute = SoluteData(
		S = 0.19767,
		B = -0.00107,
		E = 0.57971,
		L = 1.60540,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 47,
		B = 40,
		E = 46,
		L = 28,
		A = 47,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 334,
	label = "I-Phenol",
	group =  "OR{I-Phenol(ortho), I-Phenol(meta), I-Phenol(para)}",
	solute = None,
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 335,
	label = "I-Phenol(ortho)",
	group = 
"""
1 * I1s u0 {2,S}
2   Cb  u0 {1,S} {3,B}
3   Cb  u0 {2,B} {4,S}
4   O2s u0 {3,S} {5,S}
5   H   u0 {4,S}
""",
	solute = SoluteData(
		S = 0.12327,
		B = 0.00000,
		E = 0.56832,
		L = 1.69175,
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
	index = 336,
	label = "I-Phenol(meta)",
	group = 
"""
1 * I1s u0 {2,S}
2   Cb  u0 {1,S} {3,B}
3   Cb  u0 {2,B} {4,B}
4   Cb  u0 {3,B} {5,S}
5   O2s u0 {4,S} {6,S}
6   H   u0 {5,S}
""",
	solute = SoluteData(
		S = 0.04800,
		B = -0.02617,
		E = 0.18810,
		L = 0.52734,
		A = 0.05379,
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
	index = 337,
	label = "I-Phenol(para)",
	group = 
"""
1 * I1s u0 {2,S}
2   Cb  u0 {1,S} {3,B}
3   Cb  u0 {2,B} {4,B}
4   Cb  u0 {3,B} {5,B}
5   Cb  u0 {4,B} {6,S}
6   O2s u0 {5,S} {7,S}
7   H   u0 {6,S}
""",
	solute = SoluteData(
		S = 0.12071,
		B = 0.00000,
		E = 0.45796,
		L = 1.31024,
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
	index = 338,
	label = "I-BenzoicAcid",
	group =  "OR{I-BenzoicAcid(ortho), I-BenzoicAcid(meta), I-BenzoicAcid(para)}",
	solute = None,
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 339,
	label = "I-BenzoicAcid(ortho)",
	group = 
"""
1 * I1s u0 {2,S}
2   Cb  u0 {1,S} {3,B}
3   Cb  u0 {2,B} {4,S}
4   CO  u0 {3,S} {5,S}
5   O2s u0 {4,S} {6,S}
6   H   u0 {5,S}
""",
	solute = SoluteData(
		S = 0.16625,
		B = 0.06425,
		E = 0.41719,
		L = 1.33662,
		A = 0.08400,
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
	index = 340,
	label = "I-BenzoicAcid(meta)",
	group = 
"""
1 * I1s u0 {2,S}
2   Cb  u0 {1,S} {3,B}
3   Cb  u0 {2,B} {4,B}
4   Cb  u0 {3,B} {5,S}
5   CO  u0 {4,S} {6,S}
6   O2s u0 {5,S} {7,S}
7   H   u0 {6,S}
""",
	solute = SoluteData(
		S = 0.04479,
		B = -0.02383,
		E = 0.16893,
		L = 0.60515,
		A = 0.01173,
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
	index = 341,
	label = "I-BenzoicAcid(para)",
	group = 
"""
1 * I1s u0 {2,S}
2   Cb  u0 {1,S} {3,B}
3   Cb  u0 {2,B} {4,B}
4   Cb  u0 {3,B} {5,B}
5   Cb  u0 {4,B} {6,S}
6   CO  u0 {5,S} {7,S}
7   O2s u0 {6,S} {8,S}
8   H   u0 {7,S}
""",
	solute = SoluteData(
		S = 0.04479,
		B = -0.01383,
		E = 0.16893,
		L = 0.62815,
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
	index = 342,
	label = "I-Aniline",
	group =  "OR{I-Aniline(ortho), I-Aniline(meta), I-Aniline(para)}",
	solute = None,
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 343,
	label = "I-Aniline(ortho)",
	group = 
"""
1 * I1s u0 {2,S}
2   Cb  u0 {1,S} {3,B}
3   Cb  u0 {2,B} {4,S}
4   N3s u0 {3,S} {5,S} {6,S}
5   H   u0 {4,S}
6   H   u0 {4,S}
""",
	solute = SoluteData(
		S = 0.08830,
		B = 0.02814,
		E = 0.41748,
		L = 1.60331,
		A = 0.03589,
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
	index = 344,
	label = "I-Aniline(meta)",
	group = 
"""
1 * I1s u0 {2,S}
2   Cb  u0 {1,S} {3,B}
3   Cb  u0 {2,B} {4,B}
4   Cb  u0 {3,B} {5,S}
5   N3s u0 {4,S} {6,S} {7,S}
6   H   u0 {5,S}
7   H   u0 {5,S}
""",
	solute = SoluteData(
		S = 0.03241,
		B = -0.02151,
		E = 0.15667,
		L = 0.47997,
		A = 0.01820,
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
	index = 345,
	label = "I-Aniline(para)",
	group = 
"""
1 * I1s u0 {2,S}
2   Cb  u0 {1,S} {3,B}
3   Cb  u0 {2,B} {4,B}
4   Cb  u0 {3,B} {5,B}
5   Cb  u0 {4,B} {6,S}
6   N3s u0 {5,S} {7,S} {8,S}
7   H   u0 {6,S}
8   H   u0 {6,S}
""",
	solute = SoluteData(
		S = 0.11050,
		B = -0.00582,
		E = 0.35221,
		L = 1.05447,
		A = 0.00440,
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
	index = 346,
	label = "I-Cs",
	group = 
"""
1 * I1s  u0 {2,S}
2   Cs   u0 {1,S}
""",
	solute = u'I-(Cs-CZZ)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 347,
	label = "I-(Cs-CZZ)",
	group = 
"""
1 * I1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   C   u0 {2,S}
4   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = u'I-(Cs-CsZZ)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 348,
	label = "I-(Cs-CbZZ)",
	group = 
"""
1 * I1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cb  u0 {2,S}
4   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = SoluteData(
		S = 0.09157,
		B = 0.03350,
		E = 0.36377,
		L = 1.06863,
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
	index = 349,
	label = "I-(Cs-CsZZ)",
	group = 
"""
1 * I1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = u'I-(Cs-CsHH)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 350,
	label = "I-(Cs-CsHH)",
	group = 
"""
1 * I1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   H   u0 {2,S}
5   H   u0 {2,S}
""",
	solute = SoluteData(
		S = 0.28905,
		B = 0.12991,
		E = 0.57766,
		L = 1.81542,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 19,
		B = 19,
		E = 21,
		L = 19,
		A = 22,
	),
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 351,
	label = "I-(Cs-CdZZ)",
	group = 
"""
1 * I1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   [Cd,CO,CS]   u0 {2,S}
4   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = u'I-(Cs-(Cd-Cd)ZZ)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 352,
	label = "I-(Cs-(Cd-Cd)ZZ)",
	group = 
"""
1 * I1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cd  u0 {2,S} {6,D}
4   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
6   C   u0 {3,D}
""",
	solute = SoluteData(
		S = 0.05073,
		B = 0.03501,
		E = 0.22218,
		L = 0.66254,
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
	index = 353,
	label = "I-(Cs-(Cd-O2d)ZZ)",
	group = 
"""
1 * I1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   CO  u0 {2,S} {6,D}
4   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
6   O2d u0 {3,D}
""",
	solute = SoluteData(
		S = 0.08634,
		B = -0.00706,
		E = 0.35642,
		L = 0.93663,
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
	index = 354,
	label = "I-(Cs-(Cd-O2d(OH))ZZ)",
	group = 
"""
1 * I1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   CO  u0 {2,S} {6,D} {7,S}
4   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
6   O2d u0 {3,D}
7   O2s u0 {3,S} {8,S}
8   H   u0 {7,S}
""",
	solute = None,
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 355,
	label = "I-(Cs-(Cd-O2d(OH))HH)",
	group = 
"""
1 * I1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   CO  u0 {2,S} {6,D} {7,S}
4   H   u0 {2,S}
5   H   u0 {2,S}
6   O2d u0 {3,D}
7   O2s u0 {3,S} {8,S}
8   H   u0 {7,S}
""",
	solute = SoluteData(
		S = 0.04739,
		B = -0.00837,
		E = 0.19244,
		L = 0.59092,
		A = 0.03524,
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
	index = 356,
	label = "I-(Cs-(Cd-O2d(OH))XH)",
	group = 
"""
1 * I1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   CO  u0 {2,S} {6,D} {7,S}
4   [F1s,Cl1s,Br1s,I1s] u0 {2,S}
5   H   u0 {2,S}
6   O2d u0 {3,D}
7   O2s u0 {3,S} {8,S}
8   H   u0 {7,S}
""",
	solute = SoluteData(
		S = 0.09802,
		B = -0.01814,
		E = 0.37377,
		L = 1.25459,
		A = 0.07405,
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
	index = 357,
	label = "I-(Cs-(Cd-O2d(OH))XX)",
	group = 
"""
1 * I1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   CO  u0 {2,S} {6,D} {7,S}
4   [F1s,Cl1s,Br1s,I1s] u0 {2,S}
5   [F1s,Cl1s,Br1s,I1s] u0 {2,S}
6   O2d u0 {3,D}
7   O2s u0 {3,S} {8,S}
8   H   u0 {7,S}
""",
	solute = SoluteData(
		S = 0.10296,
		B = -0.01587,
		E = 0.45417,
		L = 1.46503,
		A = 0.08220,
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
	index = 358,
	label = "I-(Cs-CCZ)",
	group = 
"""
1 * I1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   C   u0 {2,S}
4   C   u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = u'I-(Cs-CsCsZ)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 359,
	label = "I-(Cs-CsCsZ)",
	group = 
"""
1 * I1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   Cs  u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = u'I-(Cs-CsCsH)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 360,
	label = "I-(Cs-CsCsH)",
	group = 
"""
1 * I1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   Cs  u0 {2,S}
5   H   u0 {2,S}
""",
	solute = SoluteData(
		S = 0.10502,
		B = 0.07667,
		E = 0.37866,
		L = 1.00789,
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
	index = 361,
	label = "I-(Cs-CsCbZ)",
	group = 
"""
1 * I1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   Cb  u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = u'I-(Cs-CbZZ)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 362,
	label = "I-(Cs-CsCdZ)",
	group = 
"""
1 * I1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   [Cd,CO,CS]   u0 {2,S}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
""",
	solute = u'I-(Cs-Cs(Cd-Cd)Z)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 363,
	label = "I-(Cs-Cs(Cd-Cd)Z)",
	group = 
"""
1 * I1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   Cd  u0 {2,S} {6,D}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
6   C   u0 {4,D}
""",
	solute = u'I-(Cs-(Cd-Cd)ZZ)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 364,
	label = "I-(Cs-Cs(Cd-O2d)Z)",
	group = 
"""
1 * I1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   Cs  u0 {2,S}
4   CO  u0 {2,S} {6,D}
5   [H,F1s,Cl1s,Br1s,I1s] u0 {2,S}
6   O2d u0 {4,D}
""",
	solute = u'I-(Cs-(Cd-O2d)ZZ)',
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 365,
	label = "I-(Cs-CCC)",
	group = 
"""
1 * I1s u0 {2,S}
2   Cs  u0 {1,S} {3,S} {4,S} {5,S}
3   C   u0 {2,S}
4   C   u0 {2,S}
5   C   u0 {2,S}
""",
	solute = SoluteData(
		S = 0.08359,
		B = 0.05634,
		E = 0.31160,
		L = 1.00887,
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
	index = 366,
	label = "I-Cd",
	group = 
"""
1 * I1s  u0 {2,S}
2   [Cd,CO,CS]   u0 {1,S}
""",
	solute = None,
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 367,
	label = "I-(Cd-Cd)",
	group = 
"""
1 * I1s  u0 {2,S}
2   Cd   u0 {1,S} {3,D}
3   C    u0 {2,D}
""",
	solute = None,
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 368,
	label = "I-(Cd-CdC)",
	group = 
"""
1 * I1s  u0 {2,S}
2   Cd   u0 {1,S} {3,D} {4,S}
3   C    u0 {2,D}
4   C    u0 {2,S}
""",
	solute = None,
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 369,
	label = "I-(Crd-CrdCr)",
	group = 
"""
1 * I1s  u0 {2,S}
2   Cd   u0 r1 {1,S} {3,D} {4,S}
3   C    u0 r1 {2,D}
4   C    u0 r1 {2,S}
""",
	solute = SoluteData(
		S = 0.15654,
		B = -0.05127,
		E = 0.46471,
		L = 1.24992,
		A = 0.00000,
	),
	dataCount = DataCountGAV(
		S = 7,
		B = 5,
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
	index = 370,
	label = "I-(Cd-CdN)",
	group = 
"""
1 * I1s  u0 {2,S}
2   Cd   u0 {1,S} {3,D} {4,S}
3   C    u0 {2,D}
4   N    u0 {2,S}
""",
	solute = None,
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 371,
	label = "I-(Crd-CrdNr)",
	group = 
"""
1 * I1s  u0 {2,S}
2   Cd   u0 r1 {1,S} {3,D} {4,S}
3   C    u0 r1 {2,D}
4   N    u0 r1 {2,S}
""",
	solute = u'I-(Crd-CrdCr)',
	dataCount = None,
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

entry(
	index = 372,
	label = "I-(Cd-Nd)",
	group = 
"""
1 * I1s  u0 {2,S}
2   Cd   u0 {1,S} {3,D}
3   N    u0 {2,D}
""",
	solute = None,
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 373,
	label = "I-(Cd-NdN)",
	group = 
"""
1 * I1s  u0 {2,S}
2   Cd   u0 {1,S} {3,D} {4,S}
3   N    u0 {2,D}
4   N    u0 {2,S}
""",
	solute = None,
	dataCount = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""",
)

entry(
	index = 374,
	label = "I-(Crd-NrdNr)",
	group = 
"""
1 * I1s  u0 {2,S}
2   Cd   u0 r1 {1,S} {3,D} {4,S}
3   N    u0 r1 {2,D}
4   N    u0 r1 {2,S}
""",
	solute = u'I-(Crd-CrdNr)',
	dataCount = None,
	shortDesc = u"""special solvation group with ring""",
	longDesc = 
u"""

""",
)

tree(
"""
L1: X
	L2: F
		L3: F-C
			L4: F-Cb
				L5: F-Phenol
					L6: F-Phenol(ortho)
					L6: F-Phenol(meta)
					L6: F-Phenol(para)
				L5: F-BenzoicAcid
					L6: F-BenzoicAcid(ortho)
					L6: F-BenzoicAcid(meta)
					L6: F-BenzoicAcid(para)
				L5: F-Aniline
					L6: F-Aniline(ortho)
					L6: F-Aniline(meta)
					L6: F-Aniline(para)
			L4: F-Cs
				L5: F-(Cs-CZZ)
					L6: F-(Cs-CbZZ)
						L7: F-(Cs-CbHH)
						L7: F-(Cs-CbXX)
							L8: F-(Cs-CbFF)
					L6: F-(Cs-CsZZ)
						L7: F-(Cs-CsHH)
							L8: F-(Cs-(Cs-ZZZ)HH)
								L9: F-(Cs-(Cs-HHH)HH)
								L9: F-(Cs-(Cs-HHX)HH)
								L9: F-(Cs-(Cs-HXX)HH)
								L9: F-(Cs-(Cs-XXX)HH)
							L8: F-(Cs-(Cs-(OH))HH)
						L7: F-(Cs-CsXH)
							L8: F-(Cs-(Cs-ZZZ)XH)
								L9: F-(Cs-(Cs-HHH)XH)
								L9: F-(Cs-(Cs-HHX)XH)
								L9: F-(Cs-(Cs-HXX)XH)
								L9: F-(Cs-(Cs-XXX)XH)
							L8: F-(Cs-(Cs-(OH))XH)
							L8: F-(Cs-CsFH)
							L8: F-(Cs-CsClH)
							L8: F-(Cs-CsBrH)
							L8: F-(Cs-CsIH)
						L7: F-(Cs-CsXX)
							L8: F-(Cs-(Cs-ZZZ)XX)
								L9: F-(Cs-(Cs-HHH)XX)
								L9: F-(Cs-(Cs-HHX)XX)
								L9: F-(Cs-(Cs-HXX)XX)
								L9: F-(Cs-(Cs-XXX)XX)
							L8: F-(Cs-CsFX)
								L9: F-(Cs-CsFF)
									L10: F-(Cs-(Cs-(OH))FF)
									L10: F-(Cs-(Cs-O)FF)
								L9: F-(Cs-CsFCl)
								L9: F-(Cs-CsFBr)
								L9: F-(Cs-CsFI)
					L6: F-(Cs-CdZZ)
						L7: F-(Cs-(Cd-Cd)ZZ)
							L8: F-(Cs-(Cd-Cd)FX)
								L9: F-(Cs-(Cd-Cd)FF)
						L7: F-(Cs-(Cd-Nd)ZZ)
							L8: F-(Cs-(Cd-Nd)XX)
								L9: F-(Cs-(Cd-Nd)FF)
						L7: F-(Cs-(Cd-O2d)ZZ)
							L8: F-(Cs-(Cd-O2d)HH)
								L9: F-(Cs-(Cd-O2d(OH))HH)
							L8: F-(Cs-(Cd-O2d)XH)
								L9: F-(Cs-(Cd-O2d(OH))XH)
							L8: F-(Cs-(Cd-O2d)XX)
								L9: F-(Cs-(Cd-O2d(OH))XX)
								L9: F-(Cs-(Cd-O2d(NH))XX)
				L5: F-(Cs-O2sZZ)
					L6: F-(Cs-O2sHZ)
						L7: F-(Cs-O2sHH)
						L7: F-(Cs-O2sHX)
							L8: F-(Cs-O2sHF)
					L6: F-(Cs-O2sXX)
						L7: F-(Cs-O2sFF)
				L5: F-(Cs-CCZ)
					L6: F-(Cs-CsCsZ)
						L7: F-(Cs-CsCsH)
						L7: F-(Cs-CsCsX)
							L8: F-(Cs-CsCsF)
								L9: F-(Cs-(Cs-(OH))CsF)
							L8: F-(Cs-CsCsCl)
							L8: F-(Cs-CsCsBr)
							L8: F-(Cs-CsCsI)
					L6: F-(Cs-CsCdZ)
						L7: F-(Cs-Cs(Cd-Cd)Z)
						L7: F-(Cs-Cs(Cd-Nd)Z)
						L7: F-(Cs-Cs(Cd-O2d)Z)
				L5: F-(Cs-CO2sZ)
					L6: F-(Cs-CsO2sZ)
						L7: F-(Cs-CsO2sH)
						L7: F-(Cs-CsO2sX)
							L8: F-(Cs-CsO2sF)
				L5: F-(Cs-CCC)
					L6: F-(Cs-CsCsCs)
				L5: F-(Cs-CCO2s)
					L6: F-(Cs-CsCsO2s)
			L4: F-Cd
				L5: F-(Cd-Cd)
					L6: F-(Cd-CdR)
						L7: F-(Cd-CdC)
							L8: F-(Crd-CrdCr)
								L9: F-(Crd-CrdCrd)
							L8: F-(Cd-CdCs)
						L7: F-(Cd-CdN)
							L8: F-(Cd-CrdNr)
					L6: F-(Cd-CdZ)
						L7: F-(Cd-CdH)
						L7: F-(Cd-CdX)
							L8: F-(Cd-CdF)
				L5: F-(Cd-Nd)
					L6: F-(Cd-N3d)
						L7: F-(Crd-N3rd)
		L3: F-N
			L4: F-N3s
		L3: F-P
			L4: F-P5d
	L2: Cl
		L3: Cl-C
			L4: Cl-Cb
				L5: Cl-Phenol
					L6: Cl-Phenol(ortho)
					L6: Cl-Phenol(meta)
					L6: Cl-Phenol(para)
				L5: Cl-BenzoicAcid
					L6: Cl-BenzoicAcid(ortho)
					L6: Cl-BenzoicAcid(meta)
					L6: Cl-BenzoicAcid(para)
				L5: Cl-BenzylAlcohol
					L6: Cl-BenzylAlcohol(ortho)
					L6: Cl-BenzylAlcohol(meta)
					L6: Cl-BenzylAlcohol(para)
				L5: Cl-Aniline
					L6: Cl-Aniline(ortho)
					L6: Cl-Aniline(meta)
					L6: Cl-Aniline(para)
			L4: Cl-Cs
				L5: Cl-(Cs-CZZ)
					L6: Cl-(Cs-CbZZ)
					L6: Cl-(Cs-CsZZ)
						L7: Cl-(Cs-CsHH)
							L8: Cl-(Cs-(Cs-ZZZ)HH)
								L9: Cl-(Cs-(Cs-HHH)HH)
								L9: Cl-(Cs-(Cs-HHX)HH)
								L9: Cl-(Cs-(Cs-HXX)HH)
								L9: Cl-(Cs-(Cs-XXX)HH)
							L8: Cl-(Cs-(Cs-(OH))HH)
						L7: Cl-(Cs-CsXH)
							L8: Cl-(Cs-(Cs-ZZZ)XH)
								L9: Cl-(Cs-(Cs-HHH)XH)
								L9: Cl-(Cs-(Cs-HHX)XH)
								L9: Cl-(Cs-(Cs-HXX)XH)
								L9: Cl-(Cs-(Cs-XXX)XH)
							L8: Cl-(Cs-(Cs-(OH))XH)
							L8: Cl-(Cs-CsFH)
							L8: Cl-(Cs-CsClH)
							L8: Cl-(Cs-CsBrH)
							L8: Cl-(Cs-CsIH)
						L7: Cl-(Cs-CsXX)
							L8: Cl-(Cs-(Cs-ZZZ)XX)
								L9: Cl-(Cs-(Cs-HHH)XX)
								L9: Cl-(Cs-(Cs-HHX)XX)
								L9: Cl-(Cs-(Cs-HXX)XX)
								L9: Cl-(Cs-(Cs-XXX)XX)
							L8: Cl-(Cs-CsFX)
								L9: Cl-(Cs-CsFF)
								L9: Cl-(Cs-CsFCl)
								L9: Cl-(Cs-CsFBr)
								L9: Cl-(Cs-CsFI)
							L8: Cl-(Cs-CsClX)
								L9: Cl-(Cs-CsClCl)
									L10: Cl-(Cs-(Cs-(OH))ClCl)
							L8: Cl-(Cs-CsBrX)
							L8: Cl-(Cs-CsII)
					L6: Cl-(Cs-CdZZ)
						L7: Cl-(Cs-(Cd-Cd)ZZ)
							L8: Cl-(Cs-(Cd-Cd)HH)
						L7: Cl-(Cs-(Cd-O2d)ZZ)
							L8: Cl-(Cs-(Cd-O2d)HH)
								L9: Cl-(Cs-(Cd-O2d(OH))HH)
							L8: Cl-(Cs-(Cd-O2d)XH)
								L9: Cl-(Cs-(Cd-O2d(OH))XH)
							L8: Cl-(Cs-(Cd-O2d)XX)
								L9: Cl-(Cs-(Cd-O2d(OH))XX)
								L9: Cl-(Cs-(Cd-O2d)ClCl)
					L6: Cl-(Cs-CtZZ)
				L5: Cl-(Cs-O2sZZ)
					L6: Cl-(Cs-O2sHZ)
					L6: Cl-(Cs-O2sXX)
						L7: Cl-(Cs-O2sFF)
				L5: Cl-(Cs-CCZ)
					L6: Cl-(Cs-CsCsZ)
						L7: Cl-(Crs-CrsCrsZ)
							L8: Cl-(Crs-CrsCrsH)
							L8: Cl-(Crs-CrsCrsX)
								L9: Cl-(Crs-CrsCrsF)
								L9: Cl-(Crs-CrsCrsCl)
						L7: Cl-(Cs-CsCsH)
						L7: Cl-(Cs-CsCsX)
							L8: Cl-(Cs-CsCsF)
							L8: Cl-(Cs-CsCsCl)
					L6: Cl-(Cs-CsCdZ)
						L7: Cl-(Cs-Cs(Cd-Cd)Z)
							L8: Cl-(Cs-Cs(Cd-Cd)H)
						L7: Cl-(Cs-Cs(Cd-O2d)Z)
							L8: Cl-(Cs-Cs(Cd-O2d)H)
				L5: Cl-(Cs-CO2sZ)
					L6: Cl-(Cs-CsO2sZ)
						L7: Cl-(Cs-CsO2sH)
						L7: Cl-(Cs-CsO2sX)
				L5: Cl-(Cs-CCC)
					L6: Cl-(Crs-CrCrCr)
					L6: Cl-(Cs-CsCsCs)
				L5: Cl-(Cs-N5dc)
			L4: Cl-Cd
				L5: Cl-(Cd-Cd)
					L6: Cl-(Cd-CdC)
						L7: Cl-(Crd-CrdCr)
							L8: Cl-(Crd-CrdCrs)
							L8: Cl-(Crd-CrdCrd)
								L9: Cl-(Crd-Crd(Crd-Crd))
								L9: Cl-(Crd-Crd(Crd-Nrd))
								L9: Cl-(Crd-Crd(Crd-O2d))
						L7: Cl-(Cd-CdCs)
					L6: Cl-(Cd-CdN)
						L7: Cl-(Crd-CrdNr)
					L6: Cl-(Cd-CdS)
						L7: Cl-(Crd-CrdSr)
					L6: Cl-(Cd-CdZ)
						L7: Cl-(Cd-CdH)
						L7: Cl-(Cd-CdX)
							L8: Cl-(Cd-CdCl)
				L5: Cl-(Cd-Nd)
					L6: Cl-(Cd-NdC)
						L7: Cl-(Crd-NrdCr)
					L6: Cl-(Cd-NdN)
						L7: Cl-(Crd-NrdNr)
				L5: Cl-(Cd-O2d)
		L3: Cl-N
			L4: Cl-N3s
				L5: Cl-(N3s-C)
					L6: Cl-(N3s-(Cd-O2d))
		L3: Cl-P
			L4: Cl-P5d
	L2: Br
		L3: Br-C
			L4: Br-Cb
				L5: Br-Phenol
					L6: Br-Phenol(ortho)
					L6: Br-Phenol(meta)
					L6: Br-Phenol(para)
				L5: Br-BenzoicAcid
					L6: Br-BenzoicAcid(ortho)
					L6: Br-BenzoicAcid(meta)
					L6: Br-BenzoicAcid(para)
				L5: Br-Aniline
					L6: Br-Aniline(ortho)
					L6: Br-Aniline(meta)
					L6: Br-Aniline(para)
			L4: Br-Cs
				L5: Br-(Cs-CZZ)
					L6: Br-(Cs-CbZZ)
					L6: Br-(Cs-CsZZ)
						L7: Br-(Cs-CsHH)
							L8: Br-(Cs-(Cs-ZZZ)HH)
								L9: Br-(Cs-(Cs-HHH)HH)
								L9: Br-(Cs-(Cs-HHX)HH)
								L9: Br-(Cs-(Cs-HXX)HH)
								L9: Br-(Cs-(Cs-XXX)HH)
						L7: Br-(Cs-CsXH)
							L8: Br-(Cs-CsFH)
							L8: Br-(Cs-CsClH)
							L8: Br-(Cs-CsBrH)
							L8: Br-(Cs-CsIH)
						L7: Br-(Cs-CsXX)
							L8: Br-(Cs-CsFX)
								L9: Br-(Cs-CsFF)
								L9: Br-(Cs-CsFCl)
								L9: Br-(Cs-CsFBr)
								L9: Br-(Cs-CsFI)
							L8: Br-(Cs-CsClX)
							L8: Br-(Cs-CsBrX)
							L8: Br-(Cs-CsII)
					L6: Br-(Cs-CdZZ)
						L7: Br-(Cs-(Cd-Cd)ZZ)
						L7: Br-(Cs-(Cd-O2d)ZZ)
							L8: Br-(Cs-(Cd-O2d(OH))ZZ)
								L9: Br-(Cs-(Cd-O2d(OH))HH)
								L9: Br-(Cs-(Cd-O2d(OH))XH)
								L9: Br-(Cs-(Cd-O2d(OH))XX)
					L6: Br-(Cs-CtZZ)
				L5: Br-(Cs-CCZ)
					L6: Br-(Cs-CsCsZ)
						L7: Br-(Cs-CsCsH)
						L7: Br-(Cs-CsCsX)
							L8: Br-(Cs-CsCsF)
					L6: Br-(Cs-CsCbZ)
					L6: Br-(Cs-CsCdZ)
						L7: Br-(Cs-Cs(Cd-Cd)Z)
						L7: Br-(Cs-Cs(Cd-O2d)Z)
							L8: Br-(Cs-Cs(Cd-O2d)H)
								L9: Br-(Cs-Cs(Cd-O2d(OH))H)
				L5: Br-(Cs-CO2sZ)
				L5: Br-(Cs-CCC)
					L6: Br-(Cs-CsCsCs)
					L6: Br-(Cs-CsCsCb)
					L6: Br-(Cs-CsCsCd)
						L7: Br-(Cs-CsCs(Cd-Cd))
						L7: Br-(Cs-CsCs(Cd-O2d))
			L4: Br-Cd
				L5: Br-(Cd-Cd)
					L6: Br-(Cd-CdZ)
					L6: Br-(Cd-CdC)
						L7: Br-(Cd-CdCd)
							L8: Br-(Crd-CrdCrd)
						L7: Br-(Cd-CdCs)
					L6: Br-(Cd-CdN)
						L7: Br-(Cd-CdN3d)
							L8: Br-(Crd-CrdN3rd)
					L6: Br-(Cd-CdO2s)
						L7: Br-(Crd-CrdO2rs)
				L5: Br-(Cd-Nd)
					L6: Br-(Cd-NdN)
						L7: Br-(Cd-N3dN3d)
							L8: Br-(Crd-N3rdN3rd)
		L3: Br-N
			L4: Br-N3s
				L5: Br-(N3s-CH)
					L6: Br-(N3s-(Cd-O2d)H)
	L2: I
		L3: I-C
			L4: I-Cb
				L5: I-Phenol
					L6: I-Phenol(ortho)
					L6: I-Phenol(meta)
					L6: I-Phenol(para)
				L5: I-BenzoicAcid
					L6: I-BenzoicAcid(ortho)
					L6: I-BenzoicAcid(meta)
					L6: I-BenzoicAcid(para)
				L5: I-Aniline
					L6: I-Aniline(ortho)
					L6: I-Aniline(meta)
					L6: I-Aniline(para)
			L4: I-Cs
				L5: I-(Cs-CZZ)
					L6: I-(Cs-CbZZ)
					L6: I-(Cs-CsZZ)
						L7: I-(Cs-CsHH)
					L6: I-(Cs-CdZZ)
						L7: I-(Cs-(Cd-Cd)ZZ)
						L7: I-(Cs-(Cd-O2d)ZZ)
							L8: I-(Cs-(Cd-O2d(OH))ZZ)
								L9: I-(Cs-(Cd-O2d(OH))HH)
								L9: I-(Cs-(Cd-O2d(OH))XH)
								L9: I-(Cs-(Cd-O2d(OH))XX)
				L5: I-(Cs-CCZ)
					L6: I-(Cs-CsCsZ)
						L7: I-(Cs-CsCsH)
					L6: I-(Cs-CsCbZ)
					L6: I-(Cs-CsCdZ)
						L7: I-(Cs-Cs(Cd-Cd)Z)
						L7: I-(Cs-Cs(Cd-O2d)Z)
				L5: I-(Cs-CCC)
			L4: I-Cd
				L5: I-(Cd-Cd)
					L6: I-(Cd-CdC)
						L7: I-(Crd-CrdCr)
					L6: I-(Cd-CdN)
						L7: I-(Crd-CrdNr)
				L5: I-(Cd-Nd)
					L6: I-(Cd-NdN)
						L7: I-(Crd-NrdNr)
"""
)
