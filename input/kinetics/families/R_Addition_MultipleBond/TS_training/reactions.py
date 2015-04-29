#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_MultipleBond/TS_training"
shortDesc = u"Distances used to train group additivity values for TS geometries"
longDesc = u"""
Put interatomic distances for reactions to use as a training set for fitting
group additivity values in this file.
"""

entry(
    index = 1,
    label = "C2H2O + H <=> C2H3O",
    degeneracy = 1,
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
    degeneracy = 1,
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
    degeneracy = 1,
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
    degeneracy = 1,
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
    degeneracy = 1,
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
    degeneracy = 1,
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
    degeneracy = 1,
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
    degeneracy = 1,
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
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.32476, 'd13': 2.18072, 'd23': 2.85259},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 22,
    label = "CH2O + CH3 <=> C2H5O",
    distances = DistanceData(
        distances = {'d12': 1.22446, 'd13': 2.14028, 'd23': 2.70332},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 25,
    label = "C2H4 + HO <=> C2H5O-1",
    distances = DistanceData(
        distances = {'d12': 1.34494, 'd13': 2.11279, 'd23': 2.6333},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 30,
    label = "C3H6 + C4H5 <=> C7H11",
    distances = DistanceData(
        distances = {'d12': 1.35997, 'd13': 2.14579, 'd23': 2.85442},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 20,
    label = "C4H7O + C3H6O <=> C7H13O2-1",
    distances = DistanceData(
        distances = {'d12': 1.25469, 'd13': 1.97141, 'd23': 2.56517},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 23,
    label = "C6H10O4 + HO <=> C6H11O5",
    distances = DistanceData(
        distances = {'d12': 1.29196, 'd13': 1.58275, 'd23': 2.35177},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 19,
    label = "C3H6 + C4H5-1 <=> C7H11-1",
    distances = DistanceData(
        distances = {'d12': 1.34525, 'd13': 2.31511, 'd23': 2.97155},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 21,
    label = "CH2O-1 + H <=> CH3O",
    distances = DistanceData(
        distances = {'d12': 1.22215, 'd13': 1.54586, 'd23': 2.41838},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 15,
    label = "C2H2O-1 + C2H3O-1 <=> C4H5O2",
    distances = DistanceData(
        distances = {'d12': 1.35161, 'd13': 2.04525, 'd23': 2.74384},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 14,
    label = "C4H7O + C3H4 <=> C7H11O-1",
    distances = DistanceData(
        distances = {'d12': 1.30803, 'd13': 2.27768, 'd23': 2.74987},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 10,
    label = "C2H4 + C2H3 <=> C4H7",
    distances = DistanceData(
        distances = {'d12': 1.34418, 'd13': 2.30181, 'd23': 3.02179},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 28,
    label = "C3H4O + CH3 <=> C4H7O-1",
    distances = DistanceData(
        distances = {'d12': 1.34, 'd13': 2.22806, 'd23': 2.96732},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 29,
    label = "C2H2 + C2H3 <=> C4H5-2",
    distances = DistanceData(
        distances = {'d12': 1.21024, 'd13': 2.25036, 'd23': 2.90843},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 17,
    label = "C3H6-1 + C4H5 <=> C7H11-2",
    distances = DistanceData(
        distances = {'d12': 1.36491, 'd13': 2.14533, 'd23': 2.77836},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 16,
    label = "C2H2O + CH3 <=> C3H5O",
    distances = DistanceData(
        distances = {'d12': 1.32569, 'd13': 2.06572, 'd23': 2.72168},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 26,
    label = "C4H6 + H <=> C4H7-1",
    distances = DistanceData(
        distances = {'d12': 1.34401, 'd13': 1.89838, 'd23': 2.56425},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 18,
    label = "C3H6O + C4H5O2-1 <=> C7H11O3",
    distances = DistanceData(
        distances = {'d12': 1.25392, 'd13': 1.97075, 'd23': 2.5241},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 13,
    label = "C4H6O-1 + H <=> C4H7O-2",
    distances = DistanceData(
        distances = {'d12': 1.32577, 'd13': 1.85882, 'd23': 2.46716},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 12,
    label = "C3H6-1 + CH3 <=> C4H9",
    distances = DistanceData(
        distances = {'d12': 1.35418, 'd13': 2.24123, 'd23': 2.89667},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 24,
    label = "CH2O + C2HO2 <=> C3H3O3",
    distances = DistanceData(
        distances = {'d12': 1.24363, 'd13': 1.98252, 'd23': 2.43491},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 27,
    label = "C2H2O-1 + H <=> C2H3O-2",
    distances = DistanceData(
        distances = {'d12': 1.32417, 'd13': 1.87573, 'd23': 2.64509},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 11,
    label = "C2H4O + H <=> C2H5O-2",
    distances = DistanceData(
        distances = {'d12': 1.2257, 'd13': 1.52639, 'd23': 2.308},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

