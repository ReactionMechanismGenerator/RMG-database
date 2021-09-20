#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Adsorption_Dissociation_Double/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 1,
    label = "C2H4 + X_1 + X_4 <=> CH2X_2 + CH2X_3",
    kinetics = StickingCoefficient(
        A = 0.1,
        n = 0,
        Ea = (2.5, 'eV/molecule'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Made up by Emily""",
    longDesc = u"""
    A made up by Emily,

    Ea taken from
    Publication: "High-throughput Calculations Of Catalytic Properties Of
    Bimetallic Alloy Surfaces". Mamun, Osman; Winther, Kirsten T.; Boes,
    Jacob R.; Bligaard, Thomas. Scientific Data. , 1, 76 (2019)
    Source DOI: 10.1038/s41597-019-0080-z
    from AlNi
    """,
	metal = "Ni",
)
