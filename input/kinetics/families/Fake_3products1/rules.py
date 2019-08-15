#!/usr/bin/env python
# encoding: utf-8

name = "Fake_3products1/rules"
shortDesc = u""
longDesc = u"""

"""
recommended = True

entry(
	index = 1,
	label = "HOORRR",
	kinetics = ArrheniusEP(
		A = (1e13, '1/s'),
		n = 0,
		alpha = 0,
		E0 = (0.5, 'kcal/mol'),
		Tmin = (300, 'K'),
		Tmax = (1500, 'K'),
	),
	reference = None,
	referenceType = "",
	rank = 0,
	shortDesc = u"""Irrelevant, because not used to make kinetics""",
	longDesc =
u"""

""",
)
