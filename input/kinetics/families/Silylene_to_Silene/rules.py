#!/usr/bin/env python
# encoding: utf-8

name = "Silylene_to_Silene/rules"
shortDesc = u""
longDesc = u"""
General comments go at the top of the file,

or in a section(s) titled 'General'

.. the ID must match those in the rateLibrary AS A STRING (ie. '2' is different from '02')

"""
entry(
        index = 1,
        label = "SiRSiH",
        kinetics = ArrheniusEP(
                A = (7.9E12, 'cm^3/(mol*s)'),
                n = 0,
                alpha = 0,
                E0 = (5.3095, 'kJ/mol'),
                Tmin = (300, 'K'),
                Tmax = (1600, 'K'),
        ),
        rank = 0,
        shortDesc = u"""Top level node""",
        longDesc =
u"""
Rate is from the reaction H3Si-SiH <-> H2Si=SiH2, high P limit of QRRK calcs. From Dollet and de Persis, J. Anal. Apply. Pyrolysis, 2007, 460-470.
""",
)

