#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_MultipleBond/TS_training"
shortDesc = u"Distances used to train group additivity values for TS geometries"
longDesc = u"""
"""
recommended = True

entry(
    index = 1,
    label = "C2H2O + H <=> C2H3O",
    distances = DistanceData(
        distances = {'d12': 1.32763, 'd13': 1.7757, 'd23': 2.2096},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 2,
    label = "C4H7O + C3H6 <=> C7H13O",
    distances = DistanceData(
        distances = {'d12': 1.35796, 'd13': 2.18876, 'd23': 2.90401},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 3,
    label = "C7H12O + H <=> C7H13O-1",
    distances = DistanceData(
        distances = {'d12': 1.34507, 'd13': 1.892, 'd23': 2.54564},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 4,
    label = "C7H12O3 + H <=> C7H13O3",
    distances = DistanceData(
        distances = {'d12': 1.34908, 'd13': 1.865, 'd23': 2.53897},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 5,
    label = "C3H6O + C4H5O <=> C7H11O2",
    distances = DistanceData(
        distances = {'d12': 1.25663, 'd13': 1.98921, 'd23': 2.58254},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 6,
    label = "C6H11O + CH2O <=> C7H13O2",
    distances = DistanceData(
        distances = {'d12': 1.24008, 'd13': 2.0208, 'd23': 2.56593},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 7,
    label = "C7H12O-1 + H <=> C7H13O-2",
    distances = DistanceData(
        distances = {'d12': 1.23113, 'd13': 1.59687, 'd23': 2.37117},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 8,
    label = "C6H10O + CH3 <=> C7H13O-3",
    distances = DistanceData(
        distances = {'d12': 1.35483, 'd13': 2.26063, 'd23': 2.96305},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 9,
    label = "C4H6O + C3H5 <=> C7H11O",
    distances = DistanceData(
        distances = {'d12': 1.32476, 'd13': 2.18072, 'd23': 2.85259},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

