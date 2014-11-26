#!/usr/bin/env python
# encoding: utf-8

name = "H2_transfer/rules"
shortDesc = u""
longDesc = u"""
General comments go at the top of the file,

or in a section(s) titled 'General'

.. the ID must match those in the rateLibrary AS A STRING (ie. '2' is different from '02')

"""
entry(
	index = 1,
	label = "R-SiH2;SiH2",  
	kinetics = ArrheniusEP(
		A = (2.65E15 , 'cm^3/(mol*s)'),
		n = 0.1,
		alpha = 0,
		E0 = (35.5, 'kJ/mol'),
		Tmin = (700, 'K'),
		Tmax = (1150, 'K'),
	),
	rank = 1,
	shortDesc = u"""Any transfer from a silane to SiH2""",     
	longDesc =
u"""
Rate is from the reaction SiH2 + Si2H6 <-> SiH4 + H3SiSiH, from the LIF measurements in silane CVD in a rotating disk reactor, Ho et al., J. Phys. Chem. 1994.
""",
)

entry(
	index = 2,
	label = "RH2;Si_pair", 
	kinetics = ArrheniusEP(
		A = (1.03E4, 'cm^3/(mol*s)'),
		n = 2.76,
		alpha = 0,
		E0 = (49.3, 'kJ/mol'),
		Tmin = (300, 'K'),
		Tmax = (2000, 'K'),
	),
	rank = 1,
	shortDesc = u"""Any transfer from a silane or SiH2-triplet to a Si_pair""",   
	longDesc =
u"""
Rate is from the reaction SiH4 + Si <-> SiH2 + SiH2, from QRRK calcs of Dollet and de Persis, J. Anal. Appl. Pyrolysis, 2007.
""",
)

entry(
	index = 3,
	label = "R-SiH2;H3SiSiH",  
	kinetics = ArrheniusEP(
		A = (1.73E14 , 'cm^3/(mol*s)'),
		n = 0.4,
		alpha = 0,
		E0 = (37.2, 'kJ/mol'),
		Tmin = (700, 'K'),
		Tmax = (1150, 'K'),
	),
	rank = 1,
	shortDesc = u"""Any transfer from an alkane to H3SiSiH""",     
	longDesc =
u"""
Rate is from the reaction SiH4 + H3SiSiH <-> Si2H6 + SiH2, from the LIF measurements in silane CVD in a rotating disk reactor, Ho et al., J. Phys. Chem. 1994.
""",
)
