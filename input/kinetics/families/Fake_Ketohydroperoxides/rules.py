#!/usr/bin/env python
# encoding: utf-8

name = "Fake_Ketohydroperoxides/rules"
shortDesc = u""
longDesc = u"""

"""
recommended = True

entry(
	index = 1,
	label = "jOOQOOH",
	kinetics = ArrheniusEP(
		A = (10000000000000.0, '1/s'),
		n = 0,
		alpha = 0,
		E0 = (0.5, 'kcal/mol'),
		Tmin = (300, 'K'),
		Tmax = (1500, 'K'),
	),
	reference = None,
	referenceType = "",
	rank = 0,
	shortDesc = u"""Irrevelant as shouldn't be used for making kinetics""",
	longDesc =
u"""

""",
)
