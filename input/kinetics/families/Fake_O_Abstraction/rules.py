#!/usr/bin/env python
# encoding: utf-8

name = "Fake_O_Abstraction/rules"
shortDesc = u""
longDesc = u"""

"""
recommended = True

entry(
	index = 1,
	label = "X_O;Y_rad",
	kinetics = ArrheniusEP(
		A = (1e13, 'cm^3/(mol*s)'),
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
)
