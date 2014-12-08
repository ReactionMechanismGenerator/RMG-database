#!/usr/bin/env python
# encoding: utf-8

name = "Fake_3products3/rules"
shortDesc = u""
longDesc = u"""

"""
recommended = True

entry(
	index = 1,
	label = "OjORROH",
    group1 = """
1 *1 O 1 {2,S} 
2 *2 O 0 {1,S} {3,S}
3 *3 R 0 {2,S} {4,S}
4 *4 R 0 {3,S} {5,S}
5 *5 O 0 {4,S} {6,S}
6 *6 H 0 {5,S}
""",
	kinetics = ArrheniusEP(
		A = (10000000000000.0, 'cm^3/(mol*s)'),
		n = 0,
		alpha = 0,
		E0 = (0.5, 'kcal/mol'),
		Tmin = (300, 'K'),
		Tmax = (1500, 'K'),
	),
	reference = None,
	referenceType = "",
	rank = 0,
	shortDesc = u"""Default""",
	longDesc = 
u"""

""",
	history = [
		("Thu Dec 4 2014","Richard West","action","""Created to use only for importing other groups chemkin filesthis entry from the old RMG database."""),
	],
)
