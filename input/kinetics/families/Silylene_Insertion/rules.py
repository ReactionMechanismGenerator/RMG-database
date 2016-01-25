#!/usr/bin/env python
# encoding: utf-8

name = "Silylene_Insertion/rules"
shortDesc = u""
longDesc = u"""
General comments go at the top of the file,

or in a section(s) titled 'General'

.. the ID must match those in the rateLibrary AS A STRING (ie. '2' is different from '02')

"""
entry(
	index = 1,
	label = "Si2S;Si_H",
	kinetics = ArrheniusEP(
		A = (1.86E14, 'cm^3/(mol*s)'),
		n = 0,
		alpha = 0,
		E0 = (-1.9, 'kJ/mol'),
		Tmin = (295, 'K'),
		Tmax = (595, 'K'),
	),
	rank = 5,
	shortDesc = u"""Any silylene insertion into an Si-H bond""",
	longDesc =
u"""
Rate is from the reaction SiH2 + Si2H6 <-> Si3H8, from laser flash photolysis studies of Becerra et al., J. Organometal. Chem., 333-349, 1996.
""",
)

entry(
	index = 2,
	label = "Si2S;H_H",
	kinetics = ArrheniusEP(
		A = (1.05E6, 'cm^3/(mol*s)'),
		n = 1.97,
		alpha = 0,
		E0 = (-1.9, 'kJ/mol'),
		Tmin = (400, 'K'),
		Tmax = (2000, 'K'),
	),
	rank = 5,
	shortDesc = u"""Any silylene insertion into an H-H bond""",
	longDesc =
u"""
Rate is from the reaction SiH2 + H2 <-> SiH4, from high level calculations (see training reactions), from Walch and Dateo, J. Phys. Chem. A, 2001, 2015-2022.
""",
)
