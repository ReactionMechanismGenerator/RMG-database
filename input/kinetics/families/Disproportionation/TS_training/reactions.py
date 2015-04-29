#!/usr/bin/env python
# encoding: utf-8

name = "Disproportionation/TS_training"
shortDesc = u"Distances used to train group additivity values for TS geometries"
longDesc = u"""
Put interatomic distances for reactions to use as a training set for fitting
group additivity values in this file.
d12 is the distance *2 and *4. d23 is the distance between *1 and *4. d13 is the distance between *1 and *2.
"""
entry(
    index = 1,
    label = "CH3 + C2H5O <=> CH4 + C2H4O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.24380, 'd13': 2.49217, 'd23': 1.25473},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation by Pierre Bhoorasingh.""",
)

entry(
    index = 2,
    label = "CH3 + C2H5 <=> CH4 + C2H4",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.31012, 'd13': 2.67387, 'd23': 1.36730},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation by Pierre Bhoorasingh.""",
)

entry(
    index = 3,
    label = "O2 + C2H5 <=> HO2 + C2H4",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.58633, 'd13': 2.64511, 'd23': 1.06371},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation by Pierre Bhoorasingh.""",
)

entry(
    index = 4,
    label = "O2 + C3H7 <=> HO2 + C3H6",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.52740, 'd13': 2.59357, 'd23': 1.08489},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation by Pierre Bhoorasingh.""",
)

entry(
    index = 5,
    label = "H + CH3O <=> H2 + CH2O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.28821, 'd13': 2.30134, 'd23': 1.01313},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation by Pierre Bhoorasingh.""",
)
