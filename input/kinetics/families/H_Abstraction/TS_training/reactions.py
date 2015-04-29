#!/usr/bin/env python
# encoding: utf-8

name = "H_Abstraction/TS_training"
shortDesc = u"Distances used to train group additivity values for TS geometries"
longDesc = u"""
Put interatomic distances for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 1,
    label = "H + C3H4 <=> H2 + C3H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.29429, 'd13': 2.25818, 'd23': 0.964372},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 2,
    label = "C3H3-1 + HO <=> H2O + C3H2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.16089, 'd13': 2.53998, 'd23': 1.39444},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 3,
    label = "HO + C3H4 <=> H2O + C3H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.16829, 'd13': 2.52734, 'd23': 1.38856},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 4,
    label = "HO2 + C3H3 <=> C3H4 + O2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.11714, 'd13': 2.58514, 'd23': 1.4872},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 5,
    label = "C6H5 + HO2 <=> C6H6 + O2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.02548, 'd13': 2.71755, 'd23': 1.70887},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 6,
    label = "C6H5 + H2 <=> C6H6 + H",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 0.863963, 'd13': 2.30267, 'd23': 1.43871},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 7,
    label = "C6H6 + HO <=> H2O + C6H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.20143, 'd13': 2.48234, 'd23': 1.29764},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 8,
    label = "C6H5 + H2O2 <=> C6H6 + HO2-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.10118, 'd13': 2.51218, 'd23': 1.41939},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 9,
    label = "C6H5 + C3H4-1 <=> C6H6 + C3H3-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.24081, 'd13': 2.69952, 'd23': 1.46367},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 10,
    label = "C6H5 + C3H4 <=> C6H6 + C3H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.23949, 'd13': 2.6721, 'd23': 1.43987},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 11,
    label = "C3H3-1 + C6H5 <=> C6H6 + C3H2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.23879, 'd13': 2.66223, 'd23': 1.43316},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 12,
    label = "H2O2 + C3H5 <=> C3H6 + HO2-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.23782, 'd13': 2.51432, 'd23': 1.29485},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 13,
    label = "C6H5 + C3H6 <=> C6H6 + C3H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.22823, 'd13': 2.71466, 'd23': 1.49307},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 14,
    label = "C6H7 + HO2 <=> C6H8 + O2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.17506, 'd13': 2.57332, 'd23': 1.40599},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 15,
    label = "C6H7-1 + HO2 <=> C6H8-1 + O2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.14303, 'd13': 2.5876, 'd23': 1.44974},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 16,
    label = "C6H8-1 + H <=> H2 + C6H7-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.24169, 'd13': 2.28501, 'd23': 1.04792},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 17,
    label = "C6H8 + HO2-1 <=> H2O2 + C6H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.26321, 'd13': 2.51752, 'd23': 1.2818},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 18,
    label = "C6H8 + C3H3-2 <=> C3H4-1 + C6H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.28937, 'd13': 2.71084, 'd23': 1.42929},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 19,
    label = "C6H8 + C3H3 <=> C3H4 + C6H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.27631, 'd13': 2.6899, 'd23': 1.42317},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 20,
    label = "C6H8-1 + C3H3 <=> C3H4 + C6H7-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.28653, 'd13': 2.67292, 'd23': 1.39168},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 21,
    label = "C6H8 + C3H5 <=> C3H6 + C6H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.31802, 'd13': 2.68772, 'd23': 1.39143},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 22,
    label = "C6H8-2 + H <=> H2 + C6H7-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.21509, 'd13': 2.33131, 'd23': 1.11664},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 23,
    label = "C6H8-2 + HO <=> H2O + C6H7-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.14278, 'd13': 2.6537, 'd23': 1.5609},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 24,
    label = "C6H8-2 + HO2-1 <=> H2O2 + C6H7-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.25253, 'd13': 2.53945, 'd23': 1.30413},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 25,
    label = "C6H8-2 + C3H3-2 <=> C3H4-1 + C6H7-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.27154, 'd13': 2.71853, 'd23': 1.45419},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 26,
    label = "C6H8-2 + C3H3 <=> C3H4 + C6H7-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.26587, 'd13': 2.71157, 'd23': 1.45239},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 27,
    label = "H2 + C2H3 <=> C2H4 + H",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 0.875435, 'd13': 2.28904, 'd23': 1.41583},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 28,
    label = "HO + C2H4 <=> H2O + C2H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.19826, 'd13': 2.48347, 'd23': 1.30794},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 29,
    label = "HO2 + C2H3 <=> C2H4 + O2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.03948, 'd13': 2.65148, 'd23': 1.64481},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 30,
    label = "H2O2 + C2H3 <=> C2H4 + HO2-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.1138, 'd13': 2.50659, 'd23': 1.40308},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 31,
    label = "C6H5 + C2H4 <=> C6H6 + C2H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.31116, 'd13': 2.64253, 'd23': 1.33973},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 32,
    label = "C6H8 + C2H3 <=> C2H4 + C6H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.22123, 'd13': 2.7132, 'd23': 1.51519},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 33,
    label = "C6H8-1 + C2H3 <=> C2H4 + C6H7-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.21775, 'd13': 2.71729, 'd23': 1.50467},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 34,
    label = "C6H8-2 + C2H3 <=> C2H4 + C6H7-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.2049, 'd13': 2.75678, 'd23': 1.56363},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 35,
    label = "C3H3 + C3H6 <=> C3H4 + C3H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.30549, 'd13': 2.68461, 'd23': 1.38273},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 36,
    label = "C3H4 + C2H3 <=> C2H4 + C3H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.25087, 'd13': 2.66446, 'd23': 1.42468},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 37,
    label = "C3H3-2 + C3H6 <=> C3H4-1 + C3H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.31908, 'd13': 2.70098, 'd23': 1.38408},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 38,
    label = "C2H + C6H6 <=> C2H2 + C6H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.13377, 'd13': 2.77186, 'd23': 1.64103},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 39,
    label = "C2H + C6H8-1 <=> C2H2 + C6H7-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.12895, 'd13': 2.80635, 'd23': 1.81579},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 40,
    label = "C2H + C6H8 <=> C2H2 + C6H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.11842, 'd13': 2.92561, 'd23': 1.92436},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 41,
    label = "C2H + C2H4 <=> C2H2 + C2H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.1357, 'd13': 2.74708, 'd23': 1.63784},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 42,
    label = "HO2 + C3H5-1 <=> C3H6-1 + O2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.03032, 'd13': 2.70779, 'd23': 1.69229},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 43,
    label = "H2O2 + C3H5-1 <=> C3H6-1 + HO2-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.11246, 'd13': 2.50817, 'd23': 1.40439},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 44,
    label = "C6H5 + C3H6-1 <=> C6H6 + C3H5-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.31533, 'd13': 2.64119, 'd23': 1.3329},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 45,
    label = "C6H8 + C3H5-1 <=> C3H6-1 + C6H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.21725, 'd13': 2.73396, 'd23': 1.52719},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 46,
    label = "C6H8-2 + C3H5-1 <=> C3H6-1 + C6H7-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.21065, 'd13': 2.75365, 'd23': 1.55054},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 47,
    label = "C3H4 + C3H5-1 <=> C3H6-1 + C3H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.25311, 'd13': 2.68089, 'd23': 1.42807},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 48,
    label = "C2H + C3H6-1 <=> C2H2 + C3H5-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.13352, 'd13': 2.782, 'd23': 1.6608},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 49,
    label = "HO2 + C3H5-2 <=> C3H6-2 + O2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.04109, 'd13': 2.67214, 'd23': 1.64509},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 50,
    label = "H2O2 + C3H5-2 <=> C3H6-2 + HO2-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.14267, 'd13': 2.50461, 'd23': 1.36766},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 51,
    label = "C6H5 + C3H6-2 <=> C6H6 + C3H5-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.28554, 'd13': 2.65879, 'd23': 1.37662},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 52,
    label = "C6H8-1 + C3H5-2 <=> C3H6-2 + C6H7-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.23787, 'd13': 2.70705, 'd23': 1.47766},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 53,
    label = "C6H8-2 + C3H5-2 <=> C3H6-2 + C6H7-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.22146, 'd13': 2.72915, 'd23': 1.52564},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 54,
    label = "C3H4 + C3H5-2 <=> C3H6-2 + C3H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.27301, 'd13': 2.66332, 'd23': 1.39444},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 55,
    label = "H + CH4 <=> H2 + CH3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.39367, 'd13': 2.28754, 'd23': 0.89387},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 56,
    label = "HO + CH4 <=> H2O + CH3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.18721, 'd13': 2.53015, 'd23': 1.34972},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 57,
    label = "HO2 + CH3 <=> CH4 + O2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.06293, 'd13': 2.63067, 'd23': 1.57678},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 58,
    label = "C6H5 + CH4 <=> C6H6 + CH3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.2924, 'd13': 2.66748, 'd23': 1.37511},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 59,
    label = "C6H8-2 + CH3 <=> CH4 + C6H7-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.22886, 'd13': 2.74275, 'd23': 1.51722},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 60,
    label = "H2O2 + C3H7 <=> C3H8 + HO2-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.17376, 'd13': 2.50779, 'd23': 1.33927},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 61,
    label = "C6H8-2 + C3H7 <=> C3H8 + C6H7-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.24581, 'd13': 2.7249, 'd23': 1.49143},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 62,
    label = "C3H4 + C3H7 <=> C3H8 + C3H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.30866, 'd13': 2.66791, 'd23': 1.36677},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 63,
    label = "H2O2 + C3H7-1 <=> C3H8-1 + HO2-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.20167, 'd13': 2.50733, 'd23': 1.31076},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 64,
    label = "C6H8 + C3H7-1 <=> C3H8-1 + C6H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.27756, 'd13': 2.70403, 'd23': 1.43905},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 65,
    label = "C6H8-1 + C3H7-1 <=> C3H8-1 + C6H7-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.28593, 'd13': 2.6921, 'd23': 1.41101},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 66,
    label = "C3H4 + C3H7-1 <=> C3H8-1 + C3H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.33117, 'd13': 2.66142, 'd23': 1.33751},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 67,
    label = "C2H + C3H8-1 <=> C2H2 + C3H7-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.12062, 'd13': 2.84485, 'd23': 1.83964},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 68,
    label = "C3H5-1 + C3H6 <=> C3H6-1 + C3H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.238, 'd13': 2.72057, 'd23': 1.48294},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 69,
    label = "C3H5-2 + C3H6 <=> C3H6-2 + C3H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.25432, 'd13': 2.70702, 'd23': 1.4568},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 70,
    label = "C3H5-1 + C2H4 <=> C3H6-1 + C2H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.32017, 'd13': 2.63625, 'd23': 1.33047},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 71,
    label = "C3H6-2 + C2H3 <=> C2H4 + C3H5-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.3004, 'd13': 2.65083, 'd23': 1.36116},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 72,
    label = "C3H6 + C2H3 <=> C2H4 + C3H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.23665, 'd13': 2.70715, 'd23': 1.47886},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 73,
    label = "C3H6-2 + C3H5-1 <=> C3H6-1 + C3H5-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.29405, 'd13': 2.64922, 'd23': 1.36623},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 74,
    label = "C3H5-1 + C3H8 <=> C3H6-1 + C3H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.27435, 'd13': 2.67949, 'd23': 1.40726},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 75,
    label = "C3H5-2 + C3H8 <=> C3H6-2 + C3H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.30736, 'd13': 2.6748, 'd23': 1.37471},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 76,
    label = "C3H6 + C3H7-1 <=> C3H8-1 + C3H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.2989, 'd13': 2.69039, 'd23': 1.40177},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 77,
    label = "C2H3 + C3H8 <=> C2H4 + C3H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.27912, 'd13': 2.68031, 'd23': 1.40281},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 78,
    label = "C2H3 + C3H8-1 <=> C2H4 + C3H7-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.25852, 'd13': 2.68364, 'd23': 1.4322},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 79,
    label = "C2HO + HO2 <=> C2H2O + O2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.08374, 'd13': 2.58042, 'd23': 1.51572},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 80,
    label = "C2H2O + HO <=> H2O + C2HO",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.20894, 'd13': 2.37828, 'd23': 1.28541},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 81,
    label = "C2HO + H2O2 <=> C2H2O + HO2-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.13828, 'd13': 2.43193, 'd23': 1.36667},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 82,
    label = "C2HO + C3H6 <=> C2H2O + C3H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.21615, 'd13': 2.67111, 'd23': 1.46309},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 83,
    label = "C2HO + C6H8-1 <=> C2H2O + C6H7-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.20339, 'd13': 2.68918, 'd23': 1.5019},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 84,
    label = "C2HO + C6H8-2 <=> C2H2O + C6H7-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.19207, 'd13': 2.72322, 'd23': 1.56813},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 85,
    label = "C2HO + C6H8 <=> C2H2O + C6H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.19879, 'd13': 2.70826, 'd23': 1.54305},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 86,
    label = "C2HO + CH4 <=> C2H2O + CH3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.30622, 'd13': 2.62821, 'd23': 1.32292},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 87,
    label = "C2HO + C3H8 <=> C2H2O + C3H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.26828, 'd13': 2.63862, 'd23': 1.37254},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 88,
    label = "C2HO + C3H8-1 <=> C2H2O + C3H7-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.23012, 'd13': 2.64379, 'd23': 1.4223},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 89,
    label = "CHO + HO2 <=> CH2O + O2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.13702, 'd13': 2.52224, 'd23': 1.46132},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 90,
    label = "CH2O + C7H13O <=> C7H14O + CHO",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.38352, 'd13': 2.70046, 'd23': 1.34343},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 91,
    label = "CH2O + C7H13O-1 <=> C7H14O-1 + CHO",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.28896, 'd13': 2.71347, 'd23': 1.44639},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 92,
    label = "CHO + H2O2 <=> CH2O + HO2-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.27438, 'd13': 2.50503, 'd23': 1.26913},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 93,
    label = "CH2O + C3H3 <=> C3H4 + CHO",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.31001, 'd13': 2.69203, 'd23': 1.39946},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 94,
    label = "CH2O + C6H5 <=> C6H6 + CHO",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.23244, 'd13': 2.7239, 'd23': 1.51853},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 95,
    label = "CHO + C6H8-1 <=> CH2O + C6H7-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.35064, 'd13': 2.69115, 'd23': 1.3732},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 96,
    label = "CHO + C6H8-2 <=> CH2O + C6H7-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.31218, 'd13': 2.70729, 'd23': 1.43643},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 97,
    label = "CHO + C6H8 <=> CH2O + C6H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.32975, 'd13': 2.71528, 'd23': 1.41139},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 98,
    label = "CH2O + C3H5-2 <=> C3H6-2 + CHO",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.26216, 'd13': 2.72997, 'd23': 1.47526},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 99,
    label = "CH2O + CH3 <=> CH4 + CHO",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.2668, 'd13': 2.74286, 'd23': 1.47729},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 100,
    label = "CH2O + C3H7-1 <=> C3H8-1 + CHO",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.31562, 'd13': 2.69363, 'd23': 1.41644},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 101,
    label = "CH3O + HO2 <=> CH4O + O2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.12284, 'd13': 2.54708, 'd23': 1.48263},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 102,
    label = "CH4O + HO <=> H2O + CH3O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.15063, 'd13': 2.57058, 'd23': 1.50472},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 103,
    label = "CH4O + C6H5 <=> C6H6 + CH3O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.25056, 'd13': 2.68233, 'd23': 1.45716},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 104,
    label = "CH3O + C3H6 <=> CH4O + C3H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.32359, 'd13': 2.67219, 'd23': 1.39238},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 105,
    label = "CH3O + C6H8-1 <=> CH4O + C6H7-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.31014, 'd13': 2.68538, 'd23': 1.40064},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 106,
    label = "CH3O + C6H8-2 <=> CH4O + C6H7-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.27727, 'd13': 2.70354, 'd23': 1.46371},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 107,
    label = "CH3O + C6H8 <=> CH4O + C6H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.3068, 'd13': 2.69787, 'd23': 1.43159},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 108,
    label = "CH4O + C2H3 <=> C2H4 + CH3O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.26318, 'd13': 2.67317, 'd23': 1.44012},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 109,
    label = "CH4O + C3H5-2 <=> C3H6-2 + CH3O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.28156, 'd13': 2.67526, 'd23': 1.41572},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 110,
    label = "CH4O + CH3 <=> CH4 + CH3O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.28625, 'd13': 2.70078, 'd23': 1.41933},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 111,
    label = "CH4O + C3H7 <=> C3H8 + CH3O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.3141, 'd13': 2.68879, 'd23': 1.39091},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 112,
    label = "CH4O + C3H7-1 <=> C3H8-1 + CH3O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.34136, 'd13': 2.67914, 'd23': 1.36275},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 113,
    label = "C7H14O-1 + CH2 <=> CH3-1 + C7H13O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.304, 'd13': 2.65247, 'd23': 1.36244},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 114,
    label = "H2 + CH2 <=> CH3-1 + H",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 0.893488, 'd13': 2.2681, 'd23': 1.37462},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 115,
    label = "HO2 + CH2 <=> CH3-1 + O2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.04106, 'd13': 2.65255, 'd23': 1.62095},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 116,
    label = "C6H8-2 + CH2 <=> CH3-1 + C6H7-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.21541, 'd13': 2.72728, 'd23': 1.51602},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 117,
    label = "C3H4-1 + CH2 <=> CH3-1 + C3H3-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.26532, 'd13': 2.6758, 'd23': 1.41049},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 118,
    label = "C2H + C3H3-1 <=> C2H2 + C3H2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.12253, 'd13': 2.83796, 'd23': 1.71577},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 119,
    label = "CH4 + O <=> HO-1 + CH3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.31451, 'd13': 2.5001, 'd23': 1.18564},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 120,
    label = "C2H5O + HO2 <=> C2H6O + O2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.13544, 'd13': 2.54805, 'd23': 1.46401},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 121,
    label = "C2H6O-1 + O <=> HO-1 + C2H5O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.28296, 'd13': 2.4907, 'd23': 1.23278},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 122,
    label = "C2H6O-1 + HO <=> H2O + C2H5O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.17282, 'd13': 2.56055, 'd23': 1.39273},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 123,
    label = "C2H6O-2 + HO <=> H2O + C2H5O-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.05464, 'd13': 2.25495, 'd23': 1.30097},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 124,
    label = "C2H5O-1 + H2O2 <=> C2H6O-1 + HO2-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.18908, 'd13': 2.50813, 'd23': 1.32482},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 125,
    label = "C2H5O-2 + H2O2 <=> C2H6O-2 + HO2-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.0907, 'd13': 2.34208, 'd23': 1.26753},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 126,
    label = "C2H5O + C3H4-1 <=> C2H6O + C3H3-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.37417, 'd13': 2.67587, 'd23': 1.33628},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 127,
    label = "C2H5O-1 + C3H4 <=> C2H6O-1 + C3H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.28916, 'd13': 2.66232, 'd23': 1.38},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 128,
    label = "C2H5O + C3H4 <=> C2H6O + C3H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.37262, 'd13': 2.64429, 'd23': 1.32124},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 129,
    label = "C2H6O + C6H5 <=> C6H6 + C2H5O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.23639, 'd13': 2.68474, 'd23': 1.47985},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 130,
    label = "C2H5O-1 + C3H6 <=> C2H6O-1 + C3H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.28225, 'd13': 2.70662, 'd23': 1.42761},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 131,
    label = "C2H5O + C3H6 <=> C2H6O + C3H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.33156, 'd13': 2.68289, 'd23': 1.37945},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 132,
    label = "C2H5O-2 + C3H6 <=> C2H6O-2 + C3H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.20738, 'd13': 2.54626, 'd23': 1.34423},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 133,
    label = "C2H5O + C6H8-1 <=> C2H6O + C6H7-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.32327, 'd13': 2.69545, 'd23': 1.39458},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 134,
    label = "C2H5O-1 + C6H8-2 <=> C2H6O-1 + C6H7-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.23984, 'd13': 2.73677, 'd23': 1.50198},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 135,
    label = "C2H5O + C6H8-2 <=> C2H6O + C6H7-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.28502, 'd13': 2.69905, 'd23': 1.44872},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 136,
    label = "C2H5O-1 + C6H8 <=> C2H6O-1 + C6H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.25307, 'd13': 2.71417, 'd23': 1.47083},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 137,
    label = "C2H5O + C6H8 <=> C2H6O + C6H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.30437, 'd13': 2.69066, 'd23': 1.42257},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 138,
    label = "C2H6O + C2H3 <=> C2H4 + C2H5O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.24444, 'd13': 2.69949, 'd23': 1.46842},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 139,
    label = "C2H6O-1 + C3H5-1 <=> C3H6-1 + C2H5O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.28245, 'd13': 2.66834, 'd23': 1.38892},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 140,
    label = "C2H6O-2 + C3H5-1 <=> C3H6-1 + C2H5O-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.19204, 'd13': 2.477, 'd23': 1.2896},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 141,
    label = "C2H6O + C3H5-2 <=> C3H6-2 + C2H5O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.26947, 'd13': 2.68027, 'd23': 1.43501},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 142,
    label = "C2H6O-2 + C3H5-2 <=> C3H6-2 + C2H5O-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.23172, 'd13': 2.48996, 'd23': 1.26004},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 143,
    label = "C2H5O-1 + C3H8 <=> C2H6O-1 + C3H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.33091, 'd13': 2.68227, 'd23': 1.35476},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 144,
    label = "C2H6O + C3H7 <=> C3H8 + C2H5O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.30452, 'd13': 2.69633, 'd23': 1.40708},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 145,
    label = "C2H5O-1 + C3H8-1 <=> C2H6O-1 + C3H7-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.3046, 'd13': 2.68341, 'd23': 1.38322},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 146,
    label = "C2H5O-2 + C3H8-1 <=> C2H6O-2 + C3H7-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.21874, 'd13': 2.53143, 'd23': 1.31493},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 147,
    label = "C2H6O-2 + CH2 <=> CH3-1 + C2H5O-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.22278, 'd13': 2.46055, 'd23': 1.25118},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 148,
    label = "C2H5O-1 + C3H3-1 <=> C2H6O-1 + C3H2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.31744, 'd13': 2.65773, 'd23': 1.35141},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 149,
    label = "C2H + C2H6O <=> C2H2 + C2H5O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.12539, 'd13': 2.78624, 'd23': 1.87771},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 150,
    label = "C2HO + C2H6O <=> C2H2O + C2H5O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.19919, 'd13': 2.66425, 'd23': 1.50082},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 151,
    label = "CH2O + C2H5O <=> C2H6O + CHO",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.36, 'd13': 2.63632, 'd23': 1.38457},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 152,
    label = "CH3O + C2H6O <=> CH4O + C2H5O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.34617, 'd13': 2.66976, 'd23': 1.37526},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 153,
    label = "C2H5O-1 + C2H6O <=> C2H6O-1 + C2H5O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.28767, 'd13': 2.70294, 'd23': 1.41971},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 154,
    label = "C2H5O-2 + C2H6O <=> C2H6O-2 + C2H5O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.1862, 'd13': 2.54826, 'd23': 1.38278},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 155,
    label = "C2H + C2H6O-1 <=> C2H2 + C2H5O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.1331, 'd13': 2.81507, 'd23': 1.69997},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 156,
    label = "C2HO + C2H6O-1 <=> C2H2O + C2H5O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.26716, 'd13': 2.63108, 'd23': 1.36612},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 157,
    label = "CH2O + C2H5O-1 <=> C2H6O-1 + CHO",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.28021, 'd13': 2.72254, 'd23': 1.46034},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 158,
    label = "CH4O + C2H5O-1 <=> C2H6O-1 + CH3O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.30263, 'd13': 2.69753, 'd23': 1.39917},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 159,
    label = "C2HO + C2H6O-2 <=> C2H2O + C2H5O-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.19687, 'd13': 2.41073, 'd23': 1.27793},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 160,
    label = "CH2O + C2H5O-2 <=> C2H6O-2 + CHO",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.19469, 'd13': 2.54285, 'd23': 1.38043},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 161,
    label = "C2H4O + H <=> H2 + C2H3O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.2835, 'd13': 2.2699, 'd23': 0.988982},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 162,
    label = "C2H4O + O <=> HO-1 + C2H3O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.26594, 'd13': 2.509, 'd23': 1.24337},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 163,
    label = "C2H3O + C3H4 <=> C2H4O + C3H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.33898, 'd13': 2.67345, 'd23': 1.3371},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 164,
    label = "C2H4O-1 + C3H3 <=> C3H4 + C2H3O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.29899, 'd13': 2.71053, 'd23': 1.41884},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 165,
    label = "C2H3O + C3H6 <=> C2H4O + C3H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.31509, 'd13': 2.69476, 'd23': 1.38198},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 166,
    label = "C2H3O-1 + C3H6 <=> C2H4O-1 + C3H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.38142, 'd13': 2.73419, 'd23': 1.35777},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 167,
    label = "C2H4O-1 + C3H5-1 <=> C3H6-1 + C2H3O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.23815, 'd13': 2.71907, 'd23': 1.51077},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 168,
    label = "C2H4O-1 + C3H5-2 <=> C3H6-2 + C2H3O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.26406, 'd13': 2.72247, 'd23': 1.48187},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 169,
    label = "C2H4O + C3H7-1 <=> C3H8-1 + C2H3O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.31358, 'd13': 2.67539, 'd23': 1.37596},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 170,
    label = "C2H3O + C2H6O <=> C2H4O + C2H5O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.34478, 'd13': 2.67719, 'd23': 1.36561},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 171,
    label = "C2H4O-1 + C2H5O <=> C2H6O + C2H3O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.36326, 'd13': 2.64477, 'd23': 1.39001},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 172,
    label = "C2H4O + C2H5O-1 <=> C2H6O-1 + C2H3O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.28374, 'd13': 2.68723, 'd23': 1.41906},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 173,
    label = "C2H4O-1 + C2H5O-1 <=> C2H6O-1 + C2H3O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.27669, 'd13': 2.73719, 'd23': 1.47522},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 174,
    label = "C2H4O + C2H5O-2 <=> C2H6O-2 + C2H3O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.23891, 'd13': 2.503, 'd23': 1.28001},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 175,
    label = "C2H4O-1 + C2H5O-2 <=> C2H6O-2 + C2H3O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.18584, 'd13': 2.57286, 'd23': 1.41532},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 176,
    label = "C2HO + C2H4O-1 <=> C2H2O + C2H3O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.17982, 'd13': 2.78509, 'd23': 1.62371},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 177,
    label = "C2H3O + C2H4O-1 <=> C2H4O + C2H3O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.3191, 'd13': 2.72768, 'd23': 1.42279},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 178,
    label = "C2H + C2H4O <=> C2H2 + C2H3O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.13807, 'd13': 2.82491, 'd23': 1.69131},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 179,
    label = "CH2O + C2H3O <=> C2H4O + CHO",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.32077, 'd13': 2.72822, 'd23': 1.41002},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 180,
    label = "CH4O + C2H3O <=> C2H4O + CH3O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.36017, 'd13': 2.63431, 'd23': 1.36251},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 181,
    label = "H + C2H6 <=> H2 + C2H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.3556, 'd13': 2.27781, 'd23': 0.923854},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 182,
    label = "HO + C2H6 <=> H2O + C2H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.16128, 'd13': 2.58129, 'd23': 1.42871},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 183,
    label = "H2O2 + C2H5 <=> C2H6 + HO2-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.18051, 'd13': 2.502, 'd23': 1.33003},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 184,
    label = "C6H8-2 + C2H5 <=> C2H6 + C6H7-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.24657, 'd13': 2.72313, 'd23': 1.48928},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 185,
    label = "C3H4 + C2H5 <=> C2H6 + C3H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.30523, 'd13': 2.66293, 'd23': 1.36484},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 186,
    label = "C2H + C2H6 <=> C2H2 + C2H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.12448, 'd13': 2.84901, 'd23': 1.77031},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 187,
    label = "C3H5-1 + C2H6 <=> C3H6-1 + C2H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.27848, 'd13': 2.67973, 'd23': 1.40632},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 188,
    label = "C2H3 + C2H6 <=> C2H4 + C2H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.2791, 'd13': 2.67322, 'd23': 1.40141},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 189,
    label = "CH2O + C2H5 <=> C2H6 + CHO",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.2938, 'd13': 2.71507, 'd23': 1.44276},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 190,
    label = "CH4O + C2H5 <=> C2H6 + CH3O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.31607, 'd13': 2.68893, 'd23': 1.38918},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 191,
    label = "C2H5O-1 + C2H6 <=> C2H6O-1 + C2H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.32896, 'd13': 2.67947, 'd23': 1.35819},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 192,
    label = "C2H6O + C2H5 <=> C2H6 + C2H5O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.30228, 'd13': 2.68903, 'd23': 1.40589},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 193,
    label = "C2H4O-1 + C2H5 <=> C2H6 + C2H3O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.29072, 'd13': 2.74355, 'd23': 1.4566},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 194,
    label = "C2H6 + C3H7 <=> C3H8 + C2H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.34625, 'd13': 2.6847, 'd23': 1.34484},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 195,
    label = "C2H5 + C3H8-1 <=> C2H6 + C3H7-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.31863, 'd13': 2.68547, 'd23': 1.37018},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 196,
    label = "C2HO-1 + C2HO <=> C2H2O + C2O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.23814, 'd13': 2.5461, 'd23': 1.42541},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 197,
    label = "C2HO-1 + C2H3 <=> C2H4 + C2O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.22447, 'd13': 2.65518, 'd23': 1.45282},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 198,
    label = "C2HO-1 + C3H5-1 <=> C3H6-1 + C2O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.22851, 'd13': 2.66445, 'd23': 1.45534},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 199,
    label = "C2HO-1 + CH3 <=> CH4 + C2O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.25782, 'd13': 2.66063, 'd23': 1.41193},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 200,
    label = "C2H + CH4O <=> C2H2 + CH3O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.12964, 'd13': 2.73886, 'd23': 1.80501},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 201,
    label = "CH2O + CH3O <=> CH4O + CHO",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.34446, 'd13': 2.64444, 'd23': 1.40076},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 202,
    label = "C3H8 + CH2 <=> CH3-1 + C3H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.29557, 'd13': 2.65918, 'd23': 1.36887},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 203,
    label = "C3H4O + C3H3-2 <=> C3H4-1 + C3H3O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.32882, 'd13': 2.69912, 'd23': 1.38361},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 204,
    label = "C3H4O + C6H5 <=> C6H6 + C3H3O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.2296, 'd13': 2.71452, 'd23': 1.49058},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 205,
    label = "C3H3O + C3H6 <=> C3H4O + C3H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.34518, 'd13': 2.70794, 'd23': 1.36733},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 206,
    label = "C3H4O + C2H3 <=> C2H4 + C3H3O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.24093, 'd13': 2.70515, 'd23': 1.47374},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 207,
    label = "C3H4O + CH3 <=> CH4 + C3H3O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.26608, 'd13': 2.70924, 'd23': 1.44373},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 208,
    label = "C3H4O + C2H5O <=> C2H6O + C3H3O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.35377, 'd13': 2.67764, 'd23': 1.3583},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 209,
    label = "C3H4O + C2H5O-2 <=> C2H6O-2 + C3H3O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.20098, 'd13': 2.55933, 'd23': 1.36702},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 210,
    label = "C3H3O + C2H4O-1 <=> C3H4O + C2H3O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.34864, 'd13': 2.74343, 'd23': 1.39821},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 211,
    label = "C3H4O + C2H <=> C2H2 + C3H3O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.11369, 'd13': 3.02434, 'd23': 1.92365},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 212,
    label = "C3H3O + CH2O <=> C3H4O + CHO",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.3605, 'd13': 2.71051, 'd23': 1.38045},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 213,
    label = "H2O2 + C3H3O-1 <=> C3H4O-1 + HO2-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.28834, 'd13': 2.55114, 'd23': 1.26977},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 214,
    label = "C6H8-1 + C3H3O-1 <=> C3H4O-1 + C6H7-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.35154, 'd13': 2.72595, 'd23': 1.38621},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 215,
    label = "C6H8-2 + C3H3O-1 <=> C3H4O-1 + C6H7-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.31832, 'd13': 2.73038, 'd23': 1.43828},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 216,
    label = "C3H3 + C3H4O-1 <=> C3H4 + C3H3O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.30526, 'd13': 2.70487, 'd23': 1.40546},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 217,
    label = "C3H5-2 + C3H4O-1 <=> C3H6-2 + C3H3O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.26354, 'd13': 2.73766, 'd23': 1.47802},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 218,
    label = "C2H3 + C3H4O-1 <=> C2H4 + C3H3O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.24541, 'd13': 2.75861, 'd23': 1.51687},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 219,
    label = "CH2O + C3H3O-1 <=> C3H4O-1 + CHO",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.39696, 'd13': 2.78275, 'd23': 1.3858},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 220,
    label = "CH3O + C3H4O-1 <=> CH4O + C3H3O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.32835, 'd13': 2.72713, 'd23': 1.41741},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 221,
    label = "C2H5O-1 + C3H4O-1 <=> C2H6O-1 + C3H3O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.28825, 'd13': 2.74272, 'd23': 1.46084},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 222,
    label = "C2H5 + C3H4O-1 <=> C2H6 + C3H3O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.29948, 'd13': 2.72285, 'd23': 1.43639},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 223,
    label = "C3H7 + C3H4O-1 <=> C3H8 + C3H3O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.30052, 'd13': 2.74595, 'd23': 1.44902},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 224,
    label = "H2 + C4H3 <=> C4H4 + H",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 0.86239, 'd13': 2.2983, 'd23': 1.43782},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 225,
    label = "C6H8-1 + C4H3 <=> C4H4 + C6H7-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.20715, 'd13': 2.72106, 'd23': 1.52486},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 226,
    label = "C3H8 + C4H3 <=> C4H4 + C3H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.26356, 'd13': 2.67127, 'd23': 1.42033},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 227,
    label = "C3H8-1 + C4H3 <=> C4H4 + C3H7-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.24194, 'd13': 2.68962, 'd23': 1.45416},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 228,
    label = "H + C4H4-1 <=> H2 + C4H3-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.32577, 'd13': 2.25494, 'd23': 0.934703},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 229,
    label = "C6H8-1 + C4H3-1 <=> C4H4-1 + C6H7-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.25686, 'd13': 2.6938, 'd23': 1.44101},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 230,
    label = "C3H6 + C4H3-1 <=> C4H4-1 + C3H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.27452, 'd13': 2.68689, 'd23': 1.41709},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 231,
    label = "CH4O + C4H3-1 <=> C4H4-1 + CH3O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.30557, 'd13': 2.66673, 'd23': 1.38363},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 232,
    label = "C2H6O + C4H3-1 <=> C4H4-1 + C2H5O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.28694, 'd13': 2.66635, 'd23': 1.40233},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 233,
    label = "C2H4O-1 + C4H3-1 <=> C4H4-1 + C2H3O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.27972, 'd13': 2.70939, 'd23': 1.44337},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 234,
    label = "C7H14O3 + H <=> H2 + C7H13O3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.36184, 'd13': 2.27416, 'd23': 0.916182},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 235,
    label = "C3H5-2 + C4H8O3 <=> C3H6-2 + C4H7O3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.20349, 'd13': 2.49703, 'd23': 1.30031},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 236,
    label = "CH2O + C4H7O3 <=> C4H8O3 + CHO",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.24357, 'd13': 2.51754, 'd23': 1.31034},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 237,
    label = "C4H5O + HO2 <=> C4H6O + O2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.13391, 'd13': 2.58993, 'd23': 1.47468},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 238,
    label = "C4H6O + H <=> H2 + C4H5O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.27258, 'd13': 2.29683, 'd23': 1.02425},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 239,
    label = "C4H6O + O <=> HO-1 + C4H5O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.19795, 'd13': 2.57366, 'd23': 1.38024},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 240,
    label = "C4H6O + HO <=> H2O + C4H5O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.13826, 'd13': 2.68698, 'd23': 1.56688},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 241,
    label = "C4H6O + C3H3-2 <=> C3H4-1 + C4H5O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.33334, 'd13': 2.71645, 'd23': 1.39021},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 242,
    label = "C4H6O + C3H3 <=> C3H4 + C4H5O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.31592, 'd13': 2.68893, 'd23': 1.38866},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 243,
    label = "C4H6O + C2H3 <=> C2H4 + C4H5O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.24309, 'd13': 2.70749, 'd23': 1.47821},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 244,
    label = "C4H6O + C3H5-2 <=> C3H6-2 + C4H5O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.26427, 'd13': 2.70747, 'd23': 1.45209},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 245,
    label = "C4H6O + C2H3O <=> C2H4O + C4H5O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.32269, 'd13': 2.70085, 'd23': 1.38658},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 246,
    label = "C4H6O + CHO <=> CH2O + C4H5O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.3794, 'd13': 2.71184, 'd23': 1.36693},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 247,
    label = "C4H6O + C4H3 <=> C4H4 + C4H5O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.22756, 'd13': 2.71548, 'd23': 1.50228},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 248,
    label = "H + C4H6O3 <=> H2 + C4H5O3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.17221, 'd13': 2.10708, 'd23': 0.937577},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 249,
    label = "C3H4O-1 + C4H5O3 <=> C4H6O3 + C3H3O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.20258, 'd13': 2.57887, 'd23': 1.39989},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 250,
    label = "C3H6O + H <=> H2 + C3H5O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.29246, 'd13': 2.26945, 'd23': 0.977884},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 251,
    label = "C3H6O + O <=> HO-1 + C3H5O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.26772, 'd13': 2.50718, 'd23': 1.24182},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 252,
    label = "C3H6O + HO <=> H2O + C3H5O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.17334, 'd13': 2.55818, 'd23': 1.3975},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 253,
    label = "C3H5O + C3H4-1 <=> C3H6O + C3H3-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.3314, 'd13': 2.68729, 'd23': 1.35655},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 254,
    label = "C3H5O + C3H4 <=> C3H6O + C3H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.33117, 'd13': 2.67376, 'd23': 1.34695},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 255,
    label = "C3H5O + C3H6 <=> C3H6O + C3H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.31181, 'd13': 2.6992, 'd23': 1.39115},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 256,
    label = "C3H6O + C2H3 <=> C2H4 + C3H5O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.25117, 'd13': 2.6909, 'd23': 1.44434},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 257,
    label = "C3H6O + C3H7 <=> C3H8 + C3H5O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.304, 'd13': 2.69336, 'd23': 1.38996},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 258,
    label = "C3H6O + C3H7-1 <=> C3H8-1 + C3H5O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.32744, 'd13': 2.67448, 'd23': 1.36322},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 259,
    label = "C3H5O + C2H6O <=> C3H6O + C2H5O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.33278, 'd13': 2.68099, 'd23': 1.37871},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 260,
    label = "C3H6O + C2H5O-1 <=> C2H6O-1 + C3H5O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.30451, 'd13': 2.69447, 'd23': 1.39121},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 261,
    label = "C3H5O + C2H4O-1 <=> C3H6O + C2H3O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.3104, 'd13': 2.73412, 'd23': 1.43504},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 262,
    label = "C3H5O + C2H4O <=> C3H6O + C2H3O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.33375, 'd13': 2.6698, 'd23': 1.34492},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 263,
    label = "C3H6O + C2HO <=> C2H2O + C3H5O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.24384, 'd13': 2.6519, 'd23': 1.40806},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 264,
    label = "C3H5O + CH4O <=> C3H6O + CH3O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.34429, 'd13': 2.69505, 'd23': 1.35705},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 265,
    label = "C3H6O + C2H <=> C2H2 + C3H5O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.13451, 'd13': 2.82673, 'd23': 1.7064},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 266,
    label = "C3H5O + C3H4O <=> C3H6O + C3H3O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.31947, 'd13': 2.70389, 'd23': 1.39347},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 267,
    label = "C3H5O + C3H4O-1 <=> C3H6O + C3H3O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.3159, 'd13': 2.7251, 'd23': 1.42272},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 268,
    label = "C4H5 + CH4 <=> C4H6 + CH3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.30083, 'd13': 2.67241, 'd23': 1.37193},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 269,
    label = "C4H5-1 + C3H6 <=> C4H6-1 + C3H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.28525, 'd13': 2.69021, 'd23': 1.41027},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 270,
    label = "C5H8 + C3H5 <=> C3H6 + C5H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.33035, 'd13': 2.69608, 'd23': 1.37277},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 271,
    label = "H + C5H8 <=> H2 + C5H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.25278, 'd13': 2.2939, 'd23': 1.04276},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 272,
    label = "C2H3 + C5H8 <=> C2H4 + C5H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.22446, 'd13': 2.72203, 'd23': 1.50747},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 273,
    label = "C3H5-2 + C5H8 <=> C3H6-2 + C5H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.24194, 'd13': 2.71985, 'd23': 1.48174},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 274,
    label = "C3H3 + C5H8 <=> C3H4 + C5H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.29177, 'd13': 2.69187, 'd23': 1.41098},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 275,
    label = "C4H3-1 + C5H8 <=> C4H4-1 + C5H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.25846, 'd13': 2.69783, 'd23': 1.44527},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 276,
    label = "C4H5 + C5H8 <=> C4H6 + C5H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.23044, 'd13': 2.73213, 'd23': 1.50298},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 277,
    label = "C4H5-1 + C5H8 <=> C4H6-1 + C5H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.23344, 'd13': 2.72066, 'd23': 1.49618},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 278,
    label = "H + C6H8-3 <=> H2 + C6H7-3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.22195, 'd13': 2.31786, 'd23': 1.10827},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 279,
    label = "C2H3 + C6H8-3 <=> C2H4 + C6H7-3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.22334, 'd13': 2.70803, 'd23': 1.49591},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 280,
    label = "C4H6-1 + H <=> H2 + C4H5-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.34474, 'd13': 2.26775, 'd23': 0.925569},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 281,
    label = "C4H6-1 + HO <=> H2O + C4H5-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.17381, 'd13': 2.52182, 'd23': 1.37475},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 282,
    label = "C5H8 + HO <=> H2O + C5H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.15346, 'd13': 2.61123, 'd23': 1.48476},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 283,
    label = "C6H8-3 + HO <=> H2O + C6H7-3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.14956, 'd13': 2.63671, 'd23': 1.55043},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 284,
    label = "C4H5-1 + HO2 <=> C4H6-1 + O2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.09601, 'd13': 2.5987, 'd23': 1.51283},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 285,
    label = "C5H7 + HO2 <=> C5H8 + O2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.17121, 'd13': 2.56276, 'd23': 1.40169},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 286,
    label = "C6H7-3 + HO2 <=> C6H8-3 + O2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.19836, 'd13': 2.58114, 'd23': 1.3926},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 287,
    label = "C4H5-1 + H2O2 <=> C4H6-1 + HO2-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.17101, 'd13': 2.4995, 'd23': 1.33502},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 288,
    label = "C5H8 + HO2-1 <=> H2O2 + C5H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.2625, 'd13': 2.53577, 'd23': 1.27831},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 289,
    label = "C6H8-3 + HO2-1 <=> H2O2 + C6H7-3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.25002, 'd13': 2.55894, 'd23': 1.31685},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 290,
    label = "C4H5 + C3H4-1 <=> C4H6 + C3H3-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.24326, 'd13': 2.69413, 'd23': 1.45773},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 291,
    label = "C4H5-1 + C3H4 <=> C4H6-1 + C3H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.30619, 'd13': 2.65607, 'd23': 1.35764},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 292,
    label = "C4H6 + C6H5 <=> C6H6 + C4H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.31915, 'd13': 2.6379, 'd23': 1.32869},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 293,
    label = "C4H6-1 + C6H5 <=> C6H6 + C4H5-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.26785, 'd13': 2.66171, 'd23': 1.39908},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 294,
    label = "C2H3 + C4H6-1 <=> C2H4 + C4H5-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.28122, 'd13': 2.65101, 'd23': 1.38457},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 295,
    label = "C3H5-1 + C4H6-1 <=> C3H6-1 + C4H5-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.27479, 'd13': 2.65584, 'd23': 1.38786},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 296,
    label = "C3H5-2 + C4H6-1 <=> C3H6-2 + C4H5-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.34806, 'd13': 2.66402, 'd23': 1.31616},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 297,
    label = "C4H3 + C4H6-1 <=> C4H4 + C4H5-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.26407, 'd13': 2.6525, 'd23': 1.40244},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 298,
    label = "C3H4O + C4H5-1 <=> C4H6-1 + C3H3O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.29046, 'd13': 2.69234, 'd23': 1.40769},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 299,
    label = "C4H5 + C2H4 <=> C4H6 + C2H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.31168, 'd13': 2.63523, 'd23': 1.33775},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 300,
    label = "C4H5 + C3H8 <=> C4H6 + C3H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.27788, 'd13': 2.68277, 'd23': 1.41052},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 301,
    label = "C5H8 + C3H7 <=> C3H8 + C5H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.26652, 'd13': 2.7145, 'd23': 1.4522},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 302,
    label = "C6H8-3 + C3H7 <=> C3H8 + C6H7-3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.25108, 'd13': 2.73836, 'd23': 1.49045},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 303,
    label = "C4H5 + C3H8-1 <=> C4H6 + C3H7-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.26709, 'd13': 2.67652, 'd23': 1.43051},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 304,
    label = "C2HO + C6H8-3 <=> C2H2O + C6H7-3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.19956, 'd13': 2.73629, 'd23': 1.56756},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 305,
    label = "CHO + C5H8 <=> CH2O + C5H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.34171, 'd13': 2.71439, 'd23': 1.39501},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 306,
    label = "CHO + C6H8-3 <=> CH2O + C6H7-3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.33317, 'd13': 2.67611, 'd23': 1.40518},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 307,
    label = "CH3O + C6H8-3 <=> CH4O + C6H7-3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.27675, 'd13': 2.71438, 'd23': 1.46478},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 308,
    label = "C2H5O-1 + C5H8 <=> C2H6O-1 + C5H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.26293, 'd13': 2.72099, 'd23': 1.46049},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 309,
    label = "C2H5O-2 + C5H8 <=> C2H6O-2 + C5H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.19996, 'd13': 2.55492, 'd23': 1.36954},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 310,
    label = "C2H5O + C6H8-3 <=> C2H6O + C6H7-3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.2915, 'd13': 2.72027, 'd23': 1.44841},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 311,
    label = "C2H5O-1 + C4H6-1 <=> C2H6O-1 + C4H5-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.3715, 'd13': 2.67317, 'd23': 1.30771},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 312,
    label = "C2H5O-2 + C4H6-1 <=> C2H6O-2 + C4H5-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.26262, 'd13': 2.47315, 'd23': 1.22374},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 313,
    label = "C4H5 + C2H6O-2 <=> C4H6 + C2H5O-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.19167, 'd13': 2.46742, 'd23': 1.29281},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 314,
    label = "C2H3O + C5H8 <=> C2H4O + C5H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.3031, 'd13': 2.69908, 'd23': 1.4035},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 315,
    label = "C2H4O + C4H5-1 <=> C4H6-1 + C2H3O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.30426, 'd13': 2.67549, 'd23': 1.38149},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 316,
    label = "C4H5 + C2H4O <=> C4H6 + C2H3O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.24191, 'd13': 2.69416, 'd23': 1.4648},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 317,
    label = "C6H8-3 + C2H5 <=> C2H6 + C6H7-3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.2516, 'd13': 2.73592, 'd23': 1.48985},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 318,
    label = "C4H5 + CH4O <=> C4H6 + CH3O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.25253, 'd13': 2.67681, 'd23': 1.45256},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 319,
    label = "C4H5 + CH2O <=> C4H6 + CHO",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.23344, 'd13': 2.73543, 'd23': 1.51785},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 320,
    label = "C4H5-1 + C3H4O-1 <=> C4H6-1 + C3H3O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.30563, 'd13': 2.7049, 'd23': 1.42103},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 321,
    label = "C5H8 + C3H3O-1 <=> C3H4O-1 + C5H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.35345, 'd13': 2.73862, 'd23': 1.39477},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 322,
    label = "C6H8-3 + C3H3O-1 <=> C3H4O-1 + C6H7-3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.31698, 'd13': 2.73633, 'd23': 1.44654},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 323,
    label = "C6H12O + CH2 <=> CH3-1 + C6H11O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.24477, 'd13': 2.68253, 'd23': 1.44365},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 324,
    label = "C4H8 + CH3 <=> CH4 + C4H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.25004, 'd13': 2.7138, 'd23': 1.47071},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 325,
    label = "C4H8 + C3H5 <=> C3H6 + C4H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.33069, 'd13': 2.69409, 'd23': 1.36693},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 326,
    label = "C4H8 + H <=> H2 + C4H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.24931, 'd13': 2.28907, 'd23': 1.04556},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 327,
    label = "C4H8 + HO <=> H2O + C4H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.1469, 'd13': 2.63461, 'd23': 1.50989},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 328,
    label = "C4H7 + HO2 <=> C4H8 + O2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.14943, 'd13': 2.58595, 'd23': 1.44047},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 329,
    label = "C4H8 + HO2-1 <=> H2O2 + C4H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.27808, 'd13': 2.5216, 'd23': 1.25759},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 330,
    label = "C4H8 + C3H3-2 <=> C3H4-1 + C4H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.30388, 'd13': 2.69887, 'd23': 1.39822},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 331,
    label = "C4H8 + C4H5-1 <=> C4H6-1 + C4H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.23827, 'd13': 2.7203, 'd23': 1.48659},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 332,
    label = "C4H8 + C2H3 <=> C2H4 + C4H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.22245, 'd13': 2.71956, 'd23': 1.50256},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 333,
    label = "C4H8 + C3H5-1 <=> C3H6-1 + C4H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.22274, 'd13': 2.71493, 'd23': 1.50503},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 334,
    label = "C4H8 + C3H5-2 <=> C3H6-2 + C4H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.24181, 'd13': 2.71435, 'd23': 1.47479},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 335,
    label = "C4H8 + C3H7-1 <=> C3H8-1 + C4H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.28031, 'd13': 2.70008, 'd23': 1.4227},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 336,
    label = "C4H8 + C2H5O <=> C2H6O + C4H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.31124, 'd13': 2.68493, 'd23': 1.40173},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 337,
    label = "C4H8 + C2H3O-1 <=> C2H4O-1 + C4H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.36021, 'd13': 2.71526, 'd23': 1.37804},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 338,
    label = "C4H8 + C2H3O <=> C2H4O + C4H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.30218, 'd13': 2.68806, 'd23': 1.39284},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 339,
    label = "C4H8 + C2H5 <=> C2H6 + C4H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.26907, 'd13': 2.70983, 'd23': 1.44471},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 340,
    label = "C4H8 + C2HO <=> C2H2O + C4H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.1971, 'd13': 2.69609, 'd23': 1.51223},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 341,
    label = "C4H8 + C2H <=> C2H2 + C4H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.12015, 'd13': 2.90963, 'd23': 1.87803},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 342,
    label = "C5H6 + CH3 <=> CH4 + C5H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.23495, 'd13': 2.73802, 'd23': 1.50981},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 343,
    label = "C5H6 + C3H5 <=> C3H6 + C5H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.31543, 'd13': 2.72946, 'd23': 1.41701},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 344,
    label = "C5H6 + H <=> H2 + C5H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.22696, 'd13': 2.31365, 'd23': 1.08669},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 345,
    label = "C5H6 + O <=> HO-1 + C5H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.20524, 'd13': 2.56073, 'd23': 1.35558},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 346,
    label = "C5H6 + HO2-1 <=> H2O2 + C5H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.29463, 'd13': 2.53967, 'd23': 1.26548},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 347,
    label = "C5H6 + C3H3-2 <=> C3H4-1 + C5H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.28483, 'd13': 2.70766, 'd23': 1.42982},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 348,
    label = "C5H6 + C3H7 <=> C3H8 + C5H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.24783, 'd13': 2.73394, 'd23': 1.49281},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 349,
    label = "C5H6 + C3H7-1 <=> C3H8-1 + C5H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.25929, 'd13': 2.72785, 'd23': 1.47588},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 350,
    label = "C5H6 + C2H5O <=> C2H6O + C5H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.28719, 'd13': 2.71445, 'd23': 1.45355},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 351,
    label = "C5H6 + C2H5O-1 <=> C2H6O-1 + C5H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.24675, 'd13': 2.73547, 'd23': 1.49597},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 352,
    label = "C5H6 + C2H5O-2 <=> C2H6O-2 + C5H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.21167, 'd13': 2.55664, 'd23': 1.35029},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 353,
    label = "C5H6 + C2H3O-1 <=> C2H4O-1 + C5H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.33141, 'd13': 2.73482, 'd23': 1.41773},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 354,
    label = "C5H6 + C2H3O <=> C2H4O + C5H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.27473, 'd13': 2.71553, 'd23': 1.44527},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 355,
    label = "C5H6 + C2H5 <=> C2H6 + C5H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.2491, 'd13': 2.73256, 'd23': 1.49166},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 356,
    label = "C5H6 + C2HO <=> C2H2O + C5H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.22726, 'd13': 2.69238, 'd23': 1.48687},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 357,
    label = "C5H6 + CHO <=> CH2O + C5H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.31716, 'd13': 2.70575, 'd23': 1.44528},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 358,
    label = "C5H6 + C4H7 <=> C4H8 + C5H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.32679, 'd13': 2.71818, 'd23': 1.39346},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 359,
    label = "C5H6-1 + CH3 <=> CH4 + C5H5-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.39771, 'd13': 2.67085, 'd23': 1.27339},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 360,
    label = "C5H5-1 + C3H6 <=> C5H6-1 + C3H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.2163, 'd13': 2.71499, 'd23': 1.50984},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 361,
    label = "C5H6-1 + H <=> H2 + C5H5-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.46973, 'd13': 2.31972, 'd23': 0.850002},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 362,
    label = "C5H6-1 + HO <=> H2O + C5H5-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.22001, 'd13': 2.46578, 'd23': 1.26358},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 363,
    label = "C5H5-1 + HO2 <=> C5H6-1 + O2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.02215, 'd13': 2.71885, 'd23': 1.71724},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 364,
    label = "C5H5-1 + H2O2 <=> C5H6-1 + HO2-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.08854, 'd13': 2.51563, 'd23': 1.43772},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 365,
    label = "C5H5-1 + C3H4 <=> C5H6-1 + C3H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.22673, 'd13': 2.6851, 'd23': 1.45942},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 366,
    label = "C5H6-1 + C2H3 <=> C2H4 + C5H5-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.36199, 'd13': 2.64125, 'd23': 1.2893},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 367,
    label = "C5H6-1 + C3H5-1 <=> C3H6-1 + C5H5-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.35669, 'd13': 2.63872, 'd23': 1.292},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 368,
    label = "C5H6-1 + C3H5-2 <=> C3H6-2 + C5H5-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.39863, 'd13': 2.65954, 'd23': 1.26716},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 369,
    label = "C5H5-1 + C3H8 <=> C5H6-1 + C3H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.25243, 'd13': 2.683, 'd23': 1.43377},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 370,
    label = "H2 + C3H3 <=> H + C3H4",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 0.964372, 'd13': 2.25818, 'd23': 1.29429},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 1""",
)

entry(
    index = 371,
    label = "H2O + C3H2 <=> C3H3-1 + HO",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.39444, 'd13': 2.53998, 'd23': 1.16089},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 2""",
)

entry(
    index = 372,
    label = "H2O + C3H3 <=> HO + C3H4",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.38856, 'd13': 2.52734, 'd23': 1.16829},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 3""",
)

entry(
    index = 373,
    label = "C3H4 + O2 <=> HO2 + C3H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.4872, 'd13': 2.58514, 'd23': 1.11714},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 4""",
)

entry(
    index = 374,
    label = "C6H6 + O2 <=> C6H5 + HO2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.70887, 'd13': 2.71755, 'd23': 1.02548},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 5""",
)

entry(
    index = 375,
    label = "C6H6 + H <=> C6H5 + H2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.43871, 'd13': 2.30267, 'd23': 0.863963},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 6""",
)

entry(
    index = 376,
    label = "H2O + C6H5 <=> C6H6 + HO",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.29764, 'd13': 2.48234, 'd23': 1.20143},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 7""",
)

entry(
    index = 377,
    label = "C6H6 + HO2-1 <=> C6H5 + H2O2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.41939, 'd13': 2.51218, 'd23': 1.10118},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 8""",
)

entry(
    index = 378,
    label = "C6H6 + C3H3-2 <=> C6H5 + C3H4-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.46367, 'd13': 2.69952, 'd23': 1.24081},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 9""",
)

entry(
    index = 379,
    label = "C6H6 + C3H3 <=> C6H5 + C3H4",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.43987, 'd13': 2.6721, 'd23': 1.23949},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 10""",
)

entry(
    index = 380,
    label = "C6H6 + C3H2 <=> C3H3-1 + C6H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.43316, 'd13': 2.66223, 'd23': 1.23879},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 11""",
)

entry(
    index = 381,
    label = "C3H6 + HO2-1 <=> H2O2 + C3H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.29485, 'd13': 2.51432, 'd23': 1.23782},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 12""",
)

entry(
    index = 382,
    label = "C6H6 + C3H5 <=> C6H5 + C3H6",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.49307, 'd13': 2.71466, 'd23': 1.22823},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 13""",
)

entry(
    index = 383,
    label = "C6H8 + O2 <=> C6H7 + HO2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.40599, 'd13': 2.57332, 'd23': 1.17506},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 14""",
)

entry(
    index = 384,
    label = "C6H8-1 + O2 <=> C6H7-1 + HO2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.44974, 'd13': 2.5876, 'd23': 1.14303},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 15""",
)

entry(
    index = 385,
    label = "H2 + C6H7-1 <=> C6H8-1 + H",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.04792, 'd13': 2.28501, 'd23': 1.24169},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 16""",
)

entry(
    index = 386,
    label = "H2O2 + C6H7 <=> C6H8 + HO2-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.2818, 'd13': 2.51752, 'd23': 1.26321},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 17""",
)

entry(
    index = 387,
    label = "C3H4-1 + C6H7 <=> C6H8 + C3H3-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.42929, 'd13': 2.71084, 'd23': 1.28937},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 18""",
)

entry(
    index = 388,
    label = "C3H4 + C6H7 <=> C6H8 + C3H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.42317, 'd13': 2.6899, 'd23': 1.27631},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 19""",
)

entry(
    index = 389,
    label = "C3H4 + C6H7-1 <=> C6H8-1 + C3H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.39168, 'd13': 2.67292, 'd23': 1.28653},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 20""",
)

entry(
    index = 390,
    label = "C3H6 + C6H7 <=> C6H8 + C3H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.39143, 'd13': 2.68772, 'd23': 1.31802},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 21""",
)

entry(
    index = 391,
    label = "H2 + C6H7-2 <=> C6H8-2 + H",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.11664, 'd13': 2.33131, 'd23': 1.21509},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 22""",
)

entry(
    index = 392,
    label = "H2O + C6H7-2 <=> C6H8-2 + HO",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.5609, 'd13': 2.6537, 'd23': 1.14278},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 23""",
)

entry(
    index = 393,
    label = "H2O2 + C6H7-2 <=> C6H8-2 + HO2-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.30413, 'd13': 2.53945, 'd23': 1.25253},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 24""",
)

entry(
    index = 394,
    label = "C3H4-1 + C6H7-2 <=> C6H8-2 + C3H3-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.45419, 'd13': 2.71853, 'd23': 1.27154},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 25""",
)

entry(
    index = 395,
    label = "C3H4 + C6H7-2 <=> C6H8-2 + C3H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.45239, 'd13': 2.71157, 'd23': 1.26587},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 26""",
)

entry(
    index = 396,
    label = "C2H4 + H <=> H2 + C2H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.41583, 'd13': 2.28904, 'd23': 0.875435},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 27""",
)

entry(
    index = 397,
    label = "H2O + C2H3 <=> HO + C2H4",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.30794, 'd13': 2.48347, 'd23': 1.19826},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 28""",
)

entry(
    index = 398,
    label = "C2H4 + O2 <=> HO2 + C2H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.64481, 'd13': 2.65148, 'd23': 1.03948},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 29""",
)

entry(
    index = 399,
    label = "C2H4 + HO2-1 <=> H2O2 + C2H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.40308, 'd13': 2.50659, 'd23': 1.1138},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 30""",
)

entry(
    index = 400,
    label = "C6H6 + C2H3 <=> C6H5 + C2H4",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.33973, 'd13': 2.64253, 'd23': 1.31116},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 31""",
)

entry(
    index = 401,
    label = "C2H4 + C6H7 <=> C6H8 + C2H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.51519, 'd13': 2.7132, 'd23': 1.22123},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 32""",
)

entry(
    index = 402,
    label = "C2H4 + C6H7-1 <=> C6H8-1 + C2H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.50467, 'd13': 2.71729, 'd23': 1.21775},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 33""",
)

entry(
    index = 403,
    label = "C2H4 + C6H7-2 <=> C6H8-2 + C2H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.56363, 'd13': 2.75678, 'd23': 1.2049},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 34""",
)

entry(
    index = 404,
    label = "C3H4 + C3H5 <=> C3H3 + C3H6",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.38273, 'd13': 2.68461, 'd23': 1.30549},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 35""",
)

entry(
    index = 405,
    label = "C2H4 + C3H3 <=> C3H4 + C2H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.42468, 'd13': 2.66446, 'd23': 1.25087},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 36""",
)

entry(
    index = 406,
    label = "C3H4-1 + C3H5 <=> C3H3-2 + C3H6",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.38408, 'd13': 2.70098, 'd23': 1.31908},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 37""",
)

entry(
    index = 407,
    label = "C2H2 + C6H5 <=> C2H + C6H6",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.64103, 'd13': 2.77186, 'd23': 1.13377},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 38""",
)

entry(
    index = 408,
    label = "C2H2 + C6H7-1 <=> C2H + C6H8-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.81579, 'd13': 2.80635, 'd23': 1.12895},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 39""",
)

entry(
    index = 409,
    label = "C2H2 + C6H7 <=> C2H + C6H8",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.92436, 'd13': 2.92561, 'd23': 1.11842},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 40""",
)

entry(
    index = 410,
    label = "C2H2 + C2H3 <=> C2H + C2H4",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.63784, 'd13': 2.74708, 'd23': 1.1357},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 41""",
)

entry(
    index = 411,
    label = "C3H6-1 + O2 <=> HO2 + C3H5-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.69229, 'd13': 2.70779, 'd23': 1.03032},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 42""",
)

entry(
    index = 412,
    label = "C3H6-1 + HO2-1 <=> H2O2 + C3H5-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.40439, 'd13': 2.50817, 'd23': 1.11246},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 43""",
)

entry(
    index = 413,
    label = "C6H6 + C3H5-1 <=> C6H5 + C3H6-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.3329, 'd13': 2.64119, 'd23': 1.31533},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 44""",
)

entry(
    index = 414,
    label = "C3H6-1 + C6H7 <=> C6H8 + C3H5-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.52719, 'd13': 2.73396, 'd23': 1.21725},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 45""",
)

entry(
    index = 415,
    label = "C3H6-1 + C6H7-2 <=> C6H8-2 + C3H5-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.55054, 'd13': 2.75365, 'd23': 1.21065},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 46""",
)

entry(
    index = 416,
    label = "C3H6-1 + C3H3 <=> C3H4 + C3H5-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.42807, 'd13': 2.68089, 'd23': 1.25311},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 47""",
)

entry(
    index = 417,
    label = "C2H2 + C3H5-1 <=> C2H + C3H6-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.6608, 'd13': 2.782, 'd23': 1.13352},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 48""",
)

entry(
    index = 418,
    label = "C3H6-2 + O2 <=> HO2 + C3H5-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.64509, 'd13': 2.67214, 'd23': 1.04109},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 49""",
)

entry(
    index = 419,
    label = "C3H6-2 + HO2-1 <=> H2O2 + C3H5-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.36766, 'd13': 2.50461, 'd23': 1.14267},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 50""",
)

entry(
    index = 420,
    label = "C6H6 + C3H5-2 <=> C6H5 + C3H6-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.37662, 'd13': 2.65879, 'd23': 1.28554},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 51""",
)

entry(
    index = 421,
    label = "C3H6-2 + C6H7-1 <=> C6H8-1 + C3H5-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.47766, 'd13': 2.70705, 'd23': 1.23787},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 52""",
)

entry(
    index = 422,
    label = "C3H6-2 + C6H7-2 <=> C6H8-2 + C3H5-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.52564, 'd13': 2.72915, 'd23': 1.22146},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 53""",
)

entry(
    index = 423,
    label = "C3H6-2 + C3H3 <=> C3H4 + C3H5-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.39444, 'd13': 2.66332, 'd23': 1.27301},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 54""",
)

entry(
    index = 424,
    label = "H2 + CH3 <=> H + CH4",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 0.89387, 'd13': 2.28754, 'd23': 1.39367},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 55""",
)

entry(
    index = 425,
    label = "H2O + CH3 <=> HO + CH4",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.34972, 'd13': 2.53015, 'd23': 1.18721},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 56""",
)

entry(
    index = 426,
    label = "CH4 + O2 <=> HO2 + CH3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.57678, 'd13': 2.63067, 'd23': 1.06293},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 57""",
)

entry(
    index = 427,
    label = "C6H6 + CH3 <=> C6H5 + CH4",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.37511, 'd13': 2.66748, 'd23': 1.2924},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 58""",
)

entry(
    index = 428,
    label = "CH4 + C6H7-2 <=> C6H8-2 + CH3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.51722, 'd13': 2.74275, 'd23': 1.22886},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 59""",
)

entry(
    index = 429,
    label = "C3H8 + HO2-1 <=> H2O2 + C3H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.33927, 'd13': 2.50779, 'd23': 1.17376},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 60""",
)

entry(
    index = 430,
    label = "C3H8 + C6H7-2 <=> C6H8-2 + C3H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.49143, 'd13': 2.7249, 'd23': 1.24581},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 61""",
)

entry(
    index = 431,
    label = "C3H8 + C3H3 <=> C3H4 + C3H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.36677, 'd13': 2.66791, 'd23': 1.30866},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 62""",
)

entry(
    index = 432,
    label = "C3H8-1 + HO2-1 <=> H2O2 + C3H7-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.31076, 'd13': 2.50733, 'd23': 1.20167},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 63""",
)

entry(
    index = 433,
    label = "C3H8-1 + C6H7 <=> C6H8 + C3H7-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.43905, 'd13': 2.70403, 'd23': 1.27756},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 64""",
)

entry(
    index = 434,
    label = "C3H8-1 + C6H7-1 <=> C6H8-1 + C3H7-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.41101, 'd13': 2.6921, 'd23': 1.28593},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 65""",
)

entry(
    index = 435,
    label = "C3H8-1 + C3H3 <=> C3H4 + C3H7-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.33751, 'd13': 2.66142, 'd23': 1.33117},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 66""",
)

entry(
    index = 436,
    label = "C2H2 + C3H7-1 <=> C2H + C3H8-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.83964, 'd13': 2.84485, 'd23': 1.12062},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 67""",
)

entry(
    index = 437,
    label = "C3H6-1 + C3H5 <=> C3H5-1 + C3H6",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.48294, 'd13': 2.72057, 'd23': 1.238},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 68""",
)

entry(
    index = 438,
    label = "C3H6-2 + C3H5 <=> C3H5-2 + C3H6",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.4568, 'd13': 2.70702, 'd23': 1.25432},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 69""",
)

entry(
    index = 439,
    label = "C3H6-1 + C2H3 <=> C3H5-1 + C2H4",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.33047, 'd13': 2.63625, 'd23': 1.32017},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 70""",
)

entry(
    index = 440,
    label = "C2H4 + C3H5-2 <=> C3H6-2 + C2H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.36116, 'd13': 2.65083, 'd23': 1.3004},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 71""",
)

entry(
    index = 441,
    label = "C2H4 + C3H5 <=> C3H6 + C2H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.47886, 'd13': 2.70715, 'd23': 1.23665},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 72""",
)

entry(
    index = 442,
    label = "C3H6-1 + C3H5-2 <=> C3H6-2 + C3H5-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.36623, 'd13': 2.64922, 'd23': 1.29405},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 73""",
)

entry(
    index = 443,
    label = "C3H6-1 + C3H7 <=> C3H5-1 + C3H8",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.40726, 'd13': 2.67949, 'd23': 1.27435},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 74""",
)

entry(
    index = 444,
    label = "C3H6-2 + C3H7 <=> C3H5-2 + C3H8",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.37471, 'd13': 2.6748, 'd23': 1.30736},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 75""",
)

entry(
    index = 445,
    label = "C3H8-1 + C3H5 <=> C3H6 + C3H7-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.40177, 'd13': 2.69039, 'd23': 1.2989},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 76""",
)

entry(
    index = 446,
    label = "C2H4 + C3H7 <=> C2H3 + C3H8",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.40281, 'd13': 2.68031, 'd23': 1.27912},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 77""",
)

entry(
    index = 447,
    label = "C2H4 + C3H7-1 <=> C2H3 + C3H8-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.4322, 'd13': 2.68364, 'd23': 1.25852},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 78""",
)

entry(
    index = 448,
    label = "C2H2O + O2 <=> C2HO + HO2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.51572, 'd13': 2.58042, 'd23': 1.08374},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 79""",
)

entry(
    index = 449,
    label = "H2O + C2HO <=> C2H2O + HO",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.28541, 'd13': 2.37828, 'd23': 1.20894},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 80""",
)

entry(
    index = 450,
    label = "C2H2O + HO2-1 <=> C2HO + H2O2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.36667, 'd13': 2.43193, 'd23': 1.13828},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 81""",
)

entry(
    index = 451,
    label = "C2H2O + C3H5 <=> C2HO + C3H6",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.46309, 'd13': 2.67111, 'd23': 1.21615},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 82""",
)

entry(
    index = 452,
    label = "C2H2O + C6H7-1 <=> C2HO + C6H8-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.5019, 'd13': 2.68918, 'd23': 1.20339},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 83""",
)

entry(
    index = 453,
    label = "C2H2O + C6H7-2 <=> C2HO + C6H8-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.56813, 'd13': 2.72322, 'd23': 1.19207},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 84""",
)

entry(
    index = 454,
    label = "C2H2O + C6H7 <=> C2HO + C6H8",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.54305, 'd13': 2.70826, 'd23': 1.19879},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 85""",
)

entry(
    index = 455,
    label = "C2H2O + CH3 <=> C2HO + CH4",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.32292, 'd13': 2.62821, 'd23': 1.30622},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 86""",
)

entry(
    index = 456,
    label = "C2H2O + C3H7 <=> C2HO + C3H8",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.37254, 'd13': 2.63862, 'd23': 1.26828},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 87""",
)

entry(
    index = 457,
    label = "C2H2O + C3H7-1 <=> C2HO + C3H8-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.4223, 'd13': 2.64379, 'd23': 1.23012},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 88""",
)

entry(
    index = 458,
    label = "CH2O + O2 <=> CHO + HO2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.46132, 'd13': 2.52224, 'd23': 1.13702},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 89""",
)

entry(
    index = 459,
    label = "C7H14O + CHO <=> CH2O + C7H13O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.34343, 'd13': 2.70046, 'd23': 1.38352},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 90""",
)

entry(
    index = 460,
    label = "C7H14O-1 + CHO <=> CH2O + C7H13O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.44639, 'd13': 2.71347, 'd23': 1.28896},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 91""",
)

entry(
    index = 461,
    label = "CH2O + HO2-1 <=> CHO + H2O2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.26913, 'd13': 2.50503, 'd23': 1.27438},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 92""",
)

entry(
    index = 462,
    label = "C3H4 + CHO <=> CH2O + C3H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.39946, 'd13': 2.69203, 'd23': 1.31001},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 93""",
)

entry(
    index = 463,
    label = "C6H6 + CHO <=> CH2O + C6H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.51853, 'd13': 2.7239, 'd23': 1.23244},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 94""",
)

entry(
    index = 464,
    label = "CH2O + C6H7-1 <=> CHO + C6H8-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.3732, 'd13': 2.69115, 'd23': 1.35064},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 95""",
)

entry(
    index = 465,
    label = "CH2O + C6H7-2 <=> CHO + C6H8-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.43643, 'd13': 2.70729, 'd23': 1.31218},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 96""",
)

entry(
    index = 466,
    label = "CH2O + C6H7 <=> CHO + C6H8",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.41139, 'd13': 2.71528, 'd23': 1.32975},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 97""",
)

entry(
    index = 467,
    label = "C3H6-2 + CHO <=> CH2O + C3H5-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.47526, 'd13': 2.72997, 'd23': 1.26216},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 98""",
)

entry(
    index = 468,
    label = "CH4 + CHO <=> CH2O + CH3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.47729, 'd13': 2.74286, 'd23': 1.2668},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 99""",
)

entry(
    index = 469,
    label = "C3H8-1 + CHO <=> CH2O + C3H7-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.41644, 'd13': 2.69363, 'd23': 1.31562},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 100""",
)

entry(
    index = 470,
    label = "CH4O + O2 <=> CH3O + HO2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.48263, 'd13': 2.54708, 'd23': 1.12284},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 101""",
)

entry(
    index = 471,
    label = "H2O + CH3O <=> CH4O + HO",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.50472, 'd13': 2.57058, 'd23': 1.15063},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 102""",
)

entry(
    index = 472,
    label = "C6H6 + CH3O <=> CH4O + C6H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.45716, 'd13': 2.68233, 'd23': 1.25056},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 103""",
)

entry(
    index = 473,
    label = "CH4O + C3H5 <=> CH3O + C3H6",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.39238, 'd13': 2.67219, 'd23': 1.32359},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 104""",
)

entry(
    index = 474,
    label = "CH4O + C6H7-1 <=> CH3O + C6H8-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.40064, 'd13': 2.68538, 'd23': 1.31014},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 105""",
)

entry(
    index = 475,
    label = "CH4O + C6H7-2 <=> CH3O + C6H8-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.46371, 'd13': 2.70354, 'd23': 1.27727},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 106""",
)

entry(
    index = 476,
    label = "CH4O + C6H7 <=> CH3O + C6H8",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.43159, 'd13': 2.69787, 'd23': 1.3068},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 107""",
)

entry(
    index = 477,
    label = "C2H4 + CH3O <=> CH4O + C2H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.44012, 'd13': 2.67317, 'd23': 1.26318},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 108""",
)

entry(
    index = 478,
    label = "C3H6-2 + CH3O <=> CH4O + C3H5-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.41572, 'd13': 2.67526, 'd23': 1.28156},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 109""",
)

entry(
    index = 479,
    label = "CH4 + CH3O <=> CH4O + CH3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.41933, 'd13': 2.70078, 'd23': 1.28625},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 110""",
)

entry(
    index = 480,
    label = "C3H8 + CH3O <=> CH4O + C3H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.39091, 'd13': 2.68879, 'd23': 1.3141},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 111""",
)

entry(
    index = 481,
    label = "C3H8-1 + CH3O <=> CH4O + C3H7-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.36275, 'd13': 2.67914, 'd23': 1.34136},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 112""",
)

entry(
    index = 482,
    label = "CH3-1 + C7H13O-1 <=> C7H14O-1 + CH2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.36244, 'd13': 2.65247, 'd23': 1.304},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 113""",
)

entry(
    index = 483,
    label = "CH3-1 + H <=> H2 + CH2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.37462, 'd13': 2.2681, 'd23': 0.893488},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 114""",
)

entry(
    index = 484,
    label = "CH3-1 + O2 <=> HO2 + CH2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.62095, 'd13': 2.65255, 'd23': 1.04106},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 115""",
)

entry(
    index = 485,
    label = "CH3-1 + C6H7-2 <=> C6H8-2 + CH2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.51602, 'd13': 2.72728, 'd23': 1.21541},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 116""",
)

entry(
    index = 486,
    label = "CH3-1 + C3H3-2 <=> C3H4-1 + CH2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.41049, 'd13': 2.6758, 'd23': 1.26532},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 117""",
)

entry(
    index = 487,
    label = "C2H2 + C3H2 <=> C2H + C3H3-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.71577, 'd13': 2.83796, 'd23': 1.12253},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 118""",
)

entry(
    index = 488,
    label = "HO-1 + CH3 <=> CH4 + O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.18564, 'd13': 2.5001, 'd23': 1.31451},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 119""",
)

entry(
    index = 489,
    label = "C2H6O + O2 <=> C2H5O + HO2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.46401, 'd13': 2.54805, 'd23': 1.13544},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 120""",
)

entry(
    index = 490,
    label = "HO-1 + C2H5O-1 <=> C2H6O-1 + O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.23278, 'd13': 2.4907, 'd23': 1.28296},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 121""",
)

entry(
    index = 491,
    label = "H2O + C2H5O-1 <=> C2H6O-1 + HO",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.39273, 'd13': 2.56055, 'd23': 1.17282},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 122""",
)

entry(
    index = 492,
    label = "H2O + C2H5O-2 <=> C2H6O-2 + HO",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.30097, 'd13': 2.25495, 'd23': 1.05464},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 123""",
)

entry(
    index = 493,
    label = "C2H6O-1 + HO2-1 <=> C2H5O-1 + H2O2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.32482, 'd13': 2.50813, 'd23': 1.18908},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 124""",
)

entry(
    index = 494,
    label = "C2H6O-2 + HO2-1 <=> C2H5O-2 + H2O2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.26753, 'd13': 2.34208, 'd23': 1.0907},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 125""",
)

entry(
    index = 495,
    label = "C2H6O + C3H3-2 <=> C2H5O + C3H4-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.33628, 'd13': 2.67587, 'd23': 1.37417},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 126""",
)

entry(
    index = 496,
    label = "C2H6O-1 + C3H3 <=> C2H5O-1 + C3H4",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.38, 'd13': 2.66232, 'd23': 1.28916},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 127""",
)

entry(
    index = 497,
    label = "C2H6O + C3H3 <=> C2H5O + C3H4",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.32124, 'd13': 2.64429, 'd23': 1.37262},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 128""",
)

entry(
    index = 498,
    label = "C6H6 + C2H5O <=> C2H6O + C6H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.47985, 'd13': 2.68474, 'd23': 1.23639},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 129""",
)

entry(
    index = 499,
    label = "C2H6O-1 + C3H5 <=> C2H5O-1 + C3H6",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.42761, 'd13': 2.70662, 'd23': 1.28225},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 130""",
)

entry(
    index = 500,
    label = "C2H6O + C3H5 <=> C2H5O + C3H6",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.37945, 'd13': 2.68289, 'd23': 1.33156},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 131""",
)

entry(
    index = 501,
    label = "C2H6O-2 + C3H5 <=> C2H5O-2 + C3H6",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.34423, 'd13': 2.54626, 'd23': 1.20738},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 132""",
)

entry(
    index = 502,
    label = "C2H6O + C6H7-1 <=> C2H5O + C6H8-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.39458, 'd13': 2.69545, 'd23': 1.32327},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 133""",
)

entry(
    index = 503,
    label = "C2H6O-1 + C6H7-2 <=> C2H5O-1 + C6H8-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.50198, 'd13': 2.73677, 'd23': 1.23984},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 134""",
)

entry(
    index = 504,
    label = "C2H6O + C6H7-2 <=> C2H5O + C6H8-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.44872, 'd13': 2.69905, 'd23': 1.28502},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 135""",
)

entry(
    index = 505,
    label = "C2H6O-1 + C6H7 <=> C2H5O-1 + C6H8",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.47083, 'd13': 2.71417, 'd23': 1.25307},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 136""",
)

entry(
    index = 506,
    label = "C2H6O + C6H7 <=> C2H5O + C6H8",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.42257, 'd13': 2.69066, 'd23': 1.30437},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 137""",
)

entry(
    index = 507,
    label = "C2H4 + C2H5O <=> C2H6O + C2H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.46842, 'd13': 2.69949, 'd23': 1.24444},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 138""",
)

entry(
    index = 508,
    label = "C3H6-1 + C2H5O-1 <=> C2H6O-1 + C3H5-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.38892, 'd13': 2.66834, 'd23': 1.28245},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 139""",
)

entry(
    index = 509,
    label = "C3H6-1 + C2H5O-2 <=> C2H6O-2 + C3H5-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.2896, 'd13': 2.477, 'd23': 1.19204},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 140""",
)

entry(
    index = 510,
    label = "C3H6-2 + C2H5O <=> C2H6O + C3H5-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.43501, 'd13': 2.68027, 'd23': 1.26947},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 141""",
)

entry(
    index = 511,
    label = "C3H6-2 + C2H5O-2 <=> C2H6O-2 + C3H5-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.26004, 'd13': 2.48996, 'd23': 1.23172},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 142""",
)

entry(
    index = 512,
    label = "C2H6O-1 + C3H7 <=> C2H5O-1 + C3H8",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.35476, 'd13': 2.68227, 'd23': 1.33091},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 143""",
)

entry(
    index = 513,
    label = "C3H8 + C2H5O <=> C2H6O + C3H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.40708, 'd13': 2.69633, 'd23': 1.30452},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 144""",
)

entry(
    index = 514,
    label = "C2H6O-1 + C3H7-1 <=> C2H5O-1 + C3H8-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.38322, 'd13': 2.68341, 'd23': 1.3046},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 145""",
)

entry(
    index = 515,
    label = "C2H6O-2 + C3H7-1 <=> C2H5O-2 + C3H8-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.31493, 'd13': 2.53143, 'd23': 1.21874},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 146""",
)

entry(
    index = 516,
    label = "CH3-1 + C2H5O-2 <=> C2H6O-2 + CH2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.25118, 'd13': 2.46055, 'd23': 1.22278},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 147""",
)

entry(
    index = 517,
    label = "C2H6O-1 + C3H2 <=> C2H5O-1 + C3H3-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.35141, 'd13': 2.65773, 'd23': 1.31744},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 148""",
)

entry(
    index = 518,
    label = "C2H2 + C2H5O <=> C2H + C2H6O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.87771, 'd13': 2.78624, 'd23': 1.12539},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 149""",
)

entry(
    index = 519,
    label = "C2H2O + C2H5O <=> C2HO + C2H6O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.50082, 'd13': 2.66425, 'd23': 1.19919},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 150""",
)

entry(
    index = 520,
    label = "C2H6O + CHO <=> CH2O + C2H5O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.38457, 'd13': 2.63632, 'd23': 1.36},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 151""",
)

entry(
    index = 521,
    label = "CH4O + C2H5O <=> CH3O + C2H6O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.37526, 'd13': 2.66976, 'd23': 1.34617},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 152""",
)

entry(
    index = 522,
    label = "C2H6O-1 + C2H5O <=> C2H5O-1 + C2H6O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.41971, 'd13': 2.70294, 'd23': 1.28767},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 153""",
)

entry(
    index = 523,
    label = "C2H6O-2 + C2H5O <=> C2H5O-2 + C2H6O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.38278, 'd13': 2.54826, 'd23': 1.1862},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 154""",
)

entry(
    index = 524,
    label = "C2H2 + C2H5O-1 <=> C2H + C2H6O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.69997, 'd13': 2.81507, 'd23': 1.1331},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 155""",
)

entry(
    index = 525,
    label = "C2H2O + C2H5O-1 <=> C2HO + C2H6O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.36612, 'd13': 2.63108, 'd23': 1.26716},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 156""",
)

entry(
    index = 526,
    label = "C2H6O-1 + CHO <=> CH2O + C2H5O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.46034, 'd13': 2.72254, 'd23': 1.28021},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 157""",
)

entry(
    index = 527,
    label = "C2H6O-1 + CH3O <=> CH4O + C2H5O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.39917, 'd13': 2.69753, 'd23': 1.30263},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 158""",
)

entry(
    index = 528,
    label = "C2H2O + C2H5O-2 <=> C2HO + C2H6O-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.27793, 'd13': 2.41073, 'd23': 1.19687},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 159""",
)

entry(
    index = 529,
    label = "C2H6O-2 + CHO <=> CH2O + C2H5O-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.38043, 'd13': 2.54285, 'd23': 1.19469},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 160""",
)

entry(
    index = 530,
    label = "H2 + C2H3O <=> C2H4O + H",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 0.988982, 'd13': 2.2699, 'd23': 1.2835},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 161""",
)

entry(
    index = 531,
    label = "HO-1 + C2H3O <=> C2H4O + O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.24337, 'd13': 2.509, 'd23': 1.26594},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 162""",
)

entry(
    index = 532,
    label = "C2H4O + C3H3 <=> C2H3O + C3H4",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.3371, 'd13': 2.67345, 'd23': 1.33898},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 163""",
)

entry(
    index = 533,
    label = "C3H4 + C2H3O-1 <=> C2H4O-1 + C3H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.41884, 'd13': 2.71053, 'd23': 1.29899},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 164""",
)

entry(
    index = 534,
    label = "C2H4O + C3H5 <=> C2H3O + C3H6",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.38198, 'd13': 2.69476, 'd23': 1.31509},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 165""",
)

entry(
    index = 535,
    label = "C2H4O-1 + C3H5 <=> C2H3O-1 + C3H6",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.35777, 'd13': 2.73419, 'd23': 1.38142},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 166""",
)

entry(
    index = 536,
    label = "C3H6-1 + C2H3O-1 <=> C2H4O-1 + C3H5-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.51077, 'd13': 2.71907, 'd23': 1.23815},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 167""",
)

entry(
    index = 537,
    label = "C3H6-2 + C2H3O-1 <=> C2H4O-1 + C3H5-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.48187, 'd13': 2.72247, 'd23': 1.26406},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 168""",
)

entry(
    index = 538,
    label = "C3H8-1 + C2H3O <=> C2H4O + C3H7-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.37596, 'd13': 2.67539, 'd23': 1.31358},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 169""",
)

entry(
    index = 539,
    label = "C2H4O + C2H5O <=> C2H3O + C2H6O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.36561, 'd13': 2.67719, 'd23': 1.34478},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 170""",
)

entry(
    index = 540,
    label = "C2H6O + C2H3O-1 <=> C2H4O-1 + C2H5O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.39001, 'd13': 2.64477, 'd23': 1.36326},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 171""",
)

entry(
    index = 541,
    label = "C2H6O-1 + C2H3O <=> C2H4O + C2H5O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.41906, 'd13': 2.68723, 'd23': 1.28374},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 172""",
)

entry(
    index = 542,
    label = "C2H6O-1 + C2H3O-1 <=> C2H4O-1 + C2H5O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.47522, 'd13': 2.73719, 'd23': 1.27669},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 173""",
)

entry(
    index = 543,
    label = "C2H6O-2 + C2H3O <=> C2H4O + C2H5O-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.28001, 'd13': 2.503, 'd23': 1.23891},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 174""",
)

entry(
    index = 544,
    label = "C2H6O-2 + C2H3O-1 <=> C2H4O-1 + C2H5O-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.41532, 'd13': 2.57286, 'd23': 1.18584},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 175""",
)

entry(
    index = 545,
    label = "C2H2O + C2H3O-1 <=> C2HO + C2H4O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.62371, 'd13': 2.78509, 'd23': 1.17982},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 176""",
)

entry(
    index = 546,
    label = "C2H4O + C2H3O-1 <=> C2H3O + C2H4O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.42279, 'd13': 2.72768, 'd23': 1.3191},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 177""",
)

entry(
    index = 547,
    label = "C2H2 + C2H3O <=> C2H + C2H4O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.69131, 'd13': 2.82491, 'd23': 1.13807},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 178""",
)

entry(
    index = 548,
    label = "C2H4O + CHO <=> CH2O + C2H3O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.41002, 'd13': 2.72822, 'd23': 1.32077},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 179""",
)

entry(
    index = 549,
    label = "C2H4O + CH3O <=> CH4O + C2H3O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.36251, 'd13': 2.63431, 'd23': 1.36017},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 180""",
)

entry(
    index = 550,
    label = "H2 + C2H5 <=> H + C2H6",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 0.923854, 'd13': 2.27781, 'd23': 1.3556},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 181""",
)

entry(
    index = 551,
    label = "H2O + C2H5 <=> HO + C2H6",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.42871, 'd13': 2.58129, 'd23': 1.16128},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 182""",
)

entry(
    index = 552,
    label = "C2H6 + HO2-1 <=> H2O2 + C2H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.33003, 'd13': 2.502, 'd23': 1.18051},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 183""",
)

entry(
    index = 553,
    label = "C2H6 + C6H7-2 <=> C6H8-2 + C2H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.48928, 'd13': 2.72313, 'd23': 1.24657},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 184""",
)

entry(
    index = 554,
    label = "C2H6 + C3H3 <=> C3H4 + C2H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.36484, 'd13': 2.66293, 'd23': 1.30523},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 185""",
)

entry(
    index = 555,
    label = "C2H2 + C2H5 <=> C2H + C2H6",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.77031, 'd13': 2.84901, 'd23': 1.12448},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 186""",
)

entry(
    index = 556,
    label = "C3H6-1 + C2H5 <=> C3H5-1 + C2H6",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.40632, 'd13': 2.67973, 'd23': 1.27848},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 187""",
)

entry(
    index = 557,
    label = "C2H4 + C2H5 <=> C2H3 + C2H6",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.40141, 'd13': 2.67322, 'd23': 1.2791},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 188""",
)

entry(
    index = 558,
    label = "C2H6 + CHO <=> CH2O + C2H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.44276, 'd13': 2.71507, 'd23': 1.2938},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 189""",
)

entry(
    index = 559,
    label = "C2H6 + CH3O <=> CH4O + C2H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.38918, 'd13': 2.68893, 'd23': 1.31607},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 190""",
)

entry(
    index = 560,
    label = "C2H6O-1 + C2H5 <=> C2H5O-1 + C2H6",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.35819, 'd13': 2.67947, 'd23': 1.32896},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 191""",
)

entry(
    index = 561,
    label = "C2H6 + C2H5O <=> C2H6O + C2H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.40589, 'd13': 2.68903, 'd23': 1.30228},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 192""",
)

entry(
    index = 562,
    label = "C2H6 + C2H3O-1 <=> C2H4O-1 + C2H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.4566, 'd13': 2.74355, 'd23': 1.29072},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 193""",
)

entry(
    index = 563,
    label = "C3H8 + C2H5 <=> C2H6 + C3H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.34484, 'd13': 2.6847, 'd23': 1.34625},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 194""",
)

entry(
    index = 564,
    label = "C2H6 + C3H7-1 <=> C2H5 + C3H8-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.37018, 'd13': 2.68547, 'd23': 1.31863},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 195""",
)

entry(
    index = 565,
    label = "C2H2O + C2O <=> C2HO-1 + C2HO",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.42541, 'd13': 2.5461, 'd23': 1.23814},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 196""",
)

entry(
    index = 566,
    label = "C2H4 + C2O <=> C2HO-1 + C2H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.45282, 'd13': 2.65518, 'd23': 1.22447},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 197""",
)

entry(
    index = 567,
    label = "C3H6-1 + C2O <=> C2HO-1 + C3H5-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.45534, 'd13': 2.66445, 'd23': 1.22851},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 198""",
)

entry(
    index = 568,
    label = "CH4 + C2O <=> C2HO-1 + CH3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.41193, 'd13': 2.66063, 'd23': 1.25782},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 199""",
)

entry(
    index = 569,
    label = "C2H2 + CH3O <=> C2H + CH4O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.80501, 'd13': 2.73886, 'd23': 1.12964},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 200""",
)

entry(
    index = 570,
    label = "CH4O + CHO <=> CH2O + CH3O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.40076, 'd13': 2.64444, 'd23': 1.34446},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 201""",
)

entry(
    index = 571,
    label = "CH3-1 + C3H7 <=> C3H8 + CH2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.36887, 'd13': 2.65918, 'd23': 1.29557},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 202""",
)

entry(
    index = 572,
    label = "C3H4-1 + C3H3O <=> C3H4O + C3H3-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.38361, 'd13': 2.69912, 'd23': 1.32882},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 203""",
)

entry(
    index = 573,
    label = "C6H6 + C3H3O <=> C3H4O + C6H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.49058, 'd13': 2.71452, 'd23': 1.2296},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 204""",
)

entry(
    index = 574,
    label = "C3H4O + C3H5 <=> C3H3O + C3H6",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.36733, 'd13': 2.70794, 'd23': 1.34518},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 205""",
)

entry(
    index = 575,
    label = "C2H4 + C3H3O <=> C3H4O + C2H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.47374, 'd13': 2.70515, 'd23': 1.24093},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 206""",
)

entry(
    index = 576,
    label = "CH4 + C3H3O <=> C3H4O + CH3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.44373, 'd13': 2.70924, 'd23': 1.26608},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 207""",
)

entry(
    index = 577,
    label = "C2H6O + C3H3O <=> C3H4O + C2H5O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.3583, 'd13': 2.67764, 'd23': 1.35377},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 208""",
)

entry(
    index = 578,
    label = "C2H6O-2 + C3H3O <=> C3H4O + C2H5O-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.36702, 'd13': 2.55933, 'd23': 1.20098},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 209""",
)

entry(
    index = 579,
    label = "C3H4O + C2H3O-1 <=> C3H3O + C2H4O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.39821, 'd13': 2.74343, 'd23': 1.34864},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 210""",
)

entry(
    index = 580,
    label = "C2H2 + C3H3O <=> C3H4O + C2H",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.92365, 'd13': 3.02434, 'd23': 1.11369},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 211""",
)

entry(
    index = 581,
    label = "C3H4O + CHO <=> C3H3O + CH2O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.38045, 'd13': 2.71051, 'd23': 1.3605},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 212""",
)

entry(
    index = 582,
    label = "C3H4O-1 + HO2-1 <=> H2O2 + C3H3O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.26977, 'd13': 2.55114, 'd23': 1.28834},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 213""",
)

entry(
    index = 583,
    label = "C3H4O-1 + C6H7-1 <=> C6H8-1 + C3H3O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.38621, 'd13': 2.72595, 'd23': 1.35154},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 214""",
)

entry(
    index = 584,
    label = "C3H4O-1 + C6H7-2 <=> C6H8-2 + C3H3O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.43828, 'd13': 2.73038, 'd23': 1.31832},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 215""",
)

entry(
    index = 585,
    label = "C3H4 + C3H3O-1 <=> C3H3 + C3H4O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.40546, 'd13': 2.70487, 'd23': 1.30526},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 216""",
)

entry(
    index = 586,
    label = "C3H6-2 + C3H3O-1 <=> C3H5-2 + C3H4O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.47802, 'd13': 2.73766, 'd23': 1.26354},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 217""",
)

entry(
    index = 587,
    label = "C2H4 + C3H3O-1 <=> C2H3 + C3H4O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.51687, 'd13': 2.75861, 'd23': 1.24541},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 218""",
)

entry(
    index = 588,
    label = "C3H4O-1 + CHO <=> CH2O + C3H3O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.3858, 'd13': 2.78275, 'd23': 1.39696},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 219""",
)

entry(
    index = 589,
    label = "CH4O + C3H3O-1 <=> CH3O + C3H4O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.41741, 'd13': 2.72713, 'd23': 1.32835},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 220""",
)

entry(
    index = 590,
    label = "C2H6O-1 + C3H3O-1 <=> C2H5O-1 + C3H4O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.46084, 'd13': 2.74272, 'd23': 1.28825},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 221""",
)

entry(
    index = 591,
    label = "C2H6 + C3H3O-1 <=> C2H5 + C3H4O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.43639, 'd13': 2.72285, 'd23': 1.29948},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 222""",
)

entry(
    index = 592,
    label = "C3H8 + C3H3O-1 <=> C3H7 + C3H4O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.44902, 'd13': 2.74595, 'd23': 1.30052},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 223""",
)

entry(
    index = 593,
    label = "C4H4 + H <=> H2 + C4H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.43782, 'd13': 2.2983, 'd23': 0.86239},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 224""",
)

entry(
    index = 594,
    label = "C4H4 + C6H7-1 <=> C6H8-1 + C4H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.52486, 'd13': 2.72106, 'd23': 1.20715},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 225""",
)

entry(
    index = 595,
    label = "C4H4 + C3H7 <=> C3H8 + C4H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.42033, 'd13': 2.67127, 'd23': 1.26356},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 226""",
)

entry(
    index = 596,
    label = "C4H4 + C3H7-1 <=> C3H8-1 + C4H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.45416, 'd13': 2.68962, 'd23': 1.24194},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 227""",
)

entry(
    index = 597,
    label = "H2 + C4H3-1 <=> H + C4H4-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 0.934703, 'd13': 2.25494, 'd23': 1.32577},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 228""",
)

entry(
    index = 598,
    label = "C4H4-1 + C6H7-1 <=> C6H8-1 + C4H3-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.44101, 'd13': 2.6938, 'd23': 1.25686},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 229""",
)

entry(
    index = 599,
    label = "C4H4-1 + C3H5 <=> C3H6 + C4H3-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.41709, 'd13': 2.68689, 'd23': 1.27452},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 230""",
)

entry(
    index = 600,
    label = "C4H4-1 + CH3O <=> CH4O + C4H3-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.38363, 'd13': 2.66673, 'd23': 1.30557},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 231""",
)

entry(
    index = 601,
    label = "C4H4-1 + C2H5O <=> C2H6O + C4H3-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.40233, 'd13': 2.66635, 'd23': 1.28694},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 232""",
)

entry(
    index = 602,
    label = "C4H4-1 + C2H3O-1 <=> C2H4O-1 + C4H3-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.44337, 'd13': 2.70939, 'd23': 1.27972},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 233""",
)

entry(
    index = 603,
    label = "H2 + C7H13O3 <=> C7H14O3 + H",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 0.916182, 'd13': 2.27416, 'd23': 1.36184},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 234""",
)

entry(
    index = 604,
    label = "C3H6-2 + C4H7O3 <=> C3H5-2 + C4H8O3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.30031, 'd13': 2.49703, 'd23': 1.20349},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 235""",
)

entry(
    index = 605,
    label = "C4H8O3 + CHO <=> CH2O + C4H7O3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.31034, 'd13': 2.51754, 'd23': 1.24357},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 236""",
)

entry(
    index = 606,
    label = "C4H6O + O2 <=> C4H5O + HO2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.47468, 'd13': 2.58993, 'd23': 1.13391},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 237""",
)

entry(
    index = 607,
    label = "H2 + C4H5O <=> C4H6O + H",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.02425, 'd13': 2.29683, 'd23': 1.27258},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 238""",
)

entry(
    index = 608,
    label = "HO-1 + C4H5O <=> C4H6O + O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.38024, 'd13': 2.57366, 'd23': 1.19795},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 239""",
)

entry(
    index = 609,
    label = "H2O + C4H5O <=> C4H6O + HO",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.56688, 'd13': 2.68698, 'd23': 1.13826},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 240""",
)

entry(
    index = 610,
    label = "C3H4-1 + C4H5O <=> C4H6O + C3H3-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.39021, 'd13': 2.71645, 'd23': 1.33334},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 241""",
)

entry(
    index = 611,
    label = "C3H4 + C4H5O <=> C4H6O + C3H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.38866, 'd13': 2.68893, 'd23': 1.31592},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 242""",
)

entry(
    index = 612,
    label = "C2H4 + C4H5O <=> C4H6O + C2H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.47821, 'd13': 2.70749, 'd23': 1.24309},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 243""",
)

entry(
    index = 613,
    label = "C3H6-2 + C4H5O <=> C4H6O + C3H5-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.45209, 'd13': 2.70747, 'd23': 1.26427},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 244""",
)

entry(
    index = 614,
    label = "C2H4O + C4H5O <=> C4H6O + C2H3O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.38658, 'd13': 2.70085, 'd23': 1.32269},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 245""",
)

entry(
    index = 615,
    label = "CH2O + C4H5O <=> C4H6O + CHO",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.36693, 'd13': 2.71184, 'd23': 1.3794},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 246""",
)

entry(
    index = 616,
    label = "C4H4 + C4H5O <=> C4H6O + C4H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.50228, 'd13': 2.71548, 'd23': 1.22756},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 247""",
)

entry(
    index = 617,
    label = "H2 + C4H5O3 <=> H + C4H6O3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 0.937577, 'd13': 2.10708, 'd23': 1.17221},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 248""",
)

entry(
    index = 618,
    label = "C4H6O3 + C3H3O-1 <=> C3H4O-1 + C4H5O3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.39989, 'd13': 2.57887, 'd23': 1.20258},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 249""",
)

entry(
    index = 619,
    label = "H2 + C3H5O <=> C3H6O + H",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 0.977884, 'd13': 2.26945, 'd23': 1.29246},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 250""",
)

entry(
    index = 620,
    label = "HO-1 + C3H5O <=> C3H6O + O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.24182, 'd13': 2.50718, 'd23': 1.26772},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 251""",
)

entry(
    index = 621,
    label = "H2O + C3H5O <=> C3H6O + HO",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.3975, 'd13': 2.55818, 'd23': 1.17334},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 252""",
)

entry(
    index = 622,
    label = "C3H6O + C3H3-2 <=> C3H5O + C3H4-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.35655, 'd13': 2.68729, 'd23': 1.3314},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 253""",
)

entry(
    index = 623,
    label = "C3H6O + C3H3 <=> C3H5O + C3H4",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.34695, 'd13': 2.67376, 'd23': 1.33117},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 254""",
)

entry(
    index = 624,
    label = "C3H6O + C3H5 <=> C3H5O + C3H6",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.39115, 'd13': 2.6992, 'd23': 1.31181},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 255""",
)

entry(
    index = 625,
    label = "C2H4 + C3H5O <=> C3H6O + C2H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.44434, 'd13': 2.6909, 'd23': 1.25117},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 256""",
)

entry(
    index = 626,
    label = "C3H8 + C3H5O <=> C3H6O + C3H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.38996, 'd13': 2.69336, 'd23': 1.304},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 257""",
)

entry(
    index = 627,
    label = "C3H8-1 + C3H5O <=> C3H6O + C3H7-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.36322, 'd13': 2.67448, 'd23': 1.32744},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 258""",
)

entry(
    index = 628,
    label = "C3H6O + C2H5O <=> C3H5O + C2H6O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.37871, 'd13': 2.68099, 'd23': 1.33278},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 259""",
)

entry(
    index = 629,
    label = "C2H6O-1 + C3H5O <=> C3H6O + C2H5O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.39121, 'd13': 2.69447, 'd23': 1.30451},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 260""",
)

entry(
    index = 630,
    label = "C3H6O + C2H3O-1 <=> C3H5O + C2H4O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.43504, 'd13': 2.73412, 'd23': 1.3104},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 261""",
)

entry(
    index = 631,
    label = "C3H6O + C2H3O <=> C3H5O + C2H4O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.34492, 'd13': 2.6698, 'd23': 1.33375},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 262""",
)

entry(
    index = 632,
    label = "C2H2O + C3H5O <=> C3H6O + C2HO",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.40806, 'd13': 2.6519, 'd23': 1.24384},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 263""",
)

entry(
    index = 633,
    label = "C3H6O + CH3O <=> C3H5O + CH4O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.35705, 'd13': 2.69505, 'd23': 1.34429},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 264""",
)

entry(
    index = 634,
    label = "C2H2 + C3H5O <=> C3H6O + C2H",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.7064, 'd13': 2.82673, 'd23': 1.13451},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 265""",
)

entry(
    index = 635,
    label = "C3H6O + C3H3O <=> C3H5O + C3H4O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.39347, 'd13': 2.70389, 'd23': 1.31947},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 266""",
)

entry(
    index = 636,
    label = "C3H6O + C3H3O-1 <=> C3H5O + C3H4O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.42272, 'd13': 2.7251, 'd23': 1.3159},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 267""",
)

entry(
    index = 637,
    label = "C4H6 + CH3 <=> C4H5 + CH4",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.37193, 'd13': 2.67241, 'd23': 1.30083},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 268""",
)

entry(
    index = 638,
    label = "C4H6-1 + C3H5 <=> C4H5-1 + C3H6",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.41027, 'd13': 2.69021, 'd23': 1.28525},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 269""",
)

entry(
    index = 639,
    label = "C3H6 + C5H7 <=> C5H8 + C3H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.37277, 'd13': 2.69608, 'd23': 1.33035},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 270""",
)

entry(
    index = 640,
    label = "H2 + C5H7 <=> H + C5H8",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.04276, 'd13': 2.2939, 'd23': 1.25278},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 271""",
)

entry(
    index = 641,
    label = "C2H4 + C5H7 <=> C2H3 + C5H8",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.50747, 'd13': 2.72203, 'd23': 1.22446},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 272""",
)

entry(
    index = 642,
    label = "C3H6-2 + C5H7 <=> C3H5-2 + C5H8",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.48174, 'd13': 2.71985, 'd23': 1.24194},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 273""",
)

entry(
    index = 643,
    label = "C3H4 + C5H7 <=> C3H3 + C5H8",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.41098, 'd13': 2.69187, 'd23': 1.29177},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 274""",
)

entry(
    index = 644,
    label = "C4H4-1 + C5H7 <=> C4H3-1 + C5H8",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.44527, 'd13': 2.69783, 'd23': 1.25846},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 275""",
)

entry(
    index = 645,
    label = "C4H6 + C5H7 <=> C4H5 + C5H8",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.50298, 'd13': 2.73213, 'd23': 1.23044},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 276""",
)

entry(
    index = 646,
    label = "C4H6-1 + C5H7 <=> C4H5-1 + C5H8",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.49618, 'd13': 2.72066, 'd23': 1.23344},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 277""",
)

entry(
    index = 647,
    label = "H2 + C6H7-3 <=> H + C6H8-3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.10827, 'd13': 2.31786, 'd23': 1.22195},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 278""",
)

entry(
    index = 648,
    label = "C2H4 + C6H7-3 <=> C2H3 + C6H8-3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.49591, 'd13': 2.70803, 'd23': 1.22334},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 279""",
)

entry(
    index = 649,
    label = "H2 + C4H5-1 <=> C4H6-1 + H",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 0.925569, 'd13': 2.26775, 'd23': 1.34474},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 280""",
)

entry(
    index = 650,
    label = "H2O + C4H5-1 <=> C4H6-1 + HO",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.37475, 'd13': 2.52182, 'd23': 1.17381},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 281""",
)

entry(
    index = 651,
    label = "H2O + C5H7 <=> C5H8 + HO",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.48476, 'd13': 2.61123, 'd23': 1.15346},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 282""",
)

entry(
    index = 652,
    label = "H2O + C6H7-3 <=> C6H8-3 + HO",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.55043, 'd13': 2.63671, 'd23': 1.14956},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 283""",
)

entry(
    index = 653,
    label = "C4H6-1 + O2 <=> C4H5-1 + HO2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.51283, 'd13': 2.5987, 'd23': 1.09601},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 284""",
)

entry(
    index = 654,
    label = "C5H8 + O2 <=> C5H7 + HO2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.40169, 'd13': 2.56276, 'd23': 1.17121},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 285""",
)

entry(
    index = 655,
    label = "C6H8-3 + O2 <=> C6H7-3 + HO2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.3926, 'd13': 2.58114, 'd23': 1.19836},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 286""",
)

entry(
    index = 656,
    label = "C4H6-1 + HO2-1 <=> C4H5-1 + H2O2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.33502, 'd13': 2.4995, 'd23': 1.17101},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 287""",
)

entry(
    index = 657,
    label = "H2O2 + C5H7 <=> C5H8 + HO2-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.27831, 'd13': 2.53577, 'd23': 1.2625},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 288""",
)

entry(
    index = 658,
    label = "H2O2 + C6H7-3 <=> C6H8-3 + HO2-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.31685, 'd13': 2.55894, 'd23': 1.25002},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 289""",
)

entry(
    index = 659,
    label = "C4H6 + C3H3-2 <=> C4H5 + C3H4-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.45773, 'd13': 2.69413, 'd23': 1.24326},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 290""",
)

entry(
    index = 660,
    label = "C4H6-1 + C3H3 <=> C4H5-1 + C3H4",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.35764, 'd13': 2.65607, 'd23': 1.30619},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 291""",
)

entry(
    index = 661,
    label = "C6H6 + C4H5 <=> C4H6 + C6H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.32869, 'd13': 2.6379, 'd23': 1.31915},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 292""",
)

entry(
    index = 662,
    label = "C6H6 + C4H5-1 <=> C4H6-1 + C6H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.39908, 'd13': 2.66171, 'd23': 1.26785},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 293""",
)

entry(
    index = 663,
    label = "C2H4 + C4H5-1 <=> C2H3 + C4H6-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.38457, 'd13': 2.65101, 'd23': 1.28122},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 294""",
)

entry(
    index = 664,
    label = "C3H6-1 + C4H5-1 <=> C3H5-1 + C4H6-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.38786, 'd13': 2.65584, 'd23': 1.27479},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 295""",
)

entry(
    index = 665,
    label = "C3H6-2 + C4H5-1 <=> C3H5-2 + C4H6-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.31616, 'd13': 2.66402, 'd23': 1.34806},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 296""",
)

entry(
    index = 666,
    label = "C4H4 + C4H5-1 <=> C4H3 + C4H6-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.40244, 'd13': 2.6525, 'd23': 1.26407},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 297""",
)

entry(
    index = 667,
    label = "C4H6-1 + C3H3O <=> C3H4O + C4H5-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.40769, 'd13': 2.69234, 'd23': 1.29046},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 298""",
)

entry(
    index = 668,
    label = "C4H6 + C2H3 <=> C4H5 + C2H4",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.33775, 'd13': 2.63523, 'd23': 1.31168},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 299""",
)

entry(
    index = 669,
    label = "C4H6 + C3H7 <=> C4H5 + C3H8",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.41052, 'd13': 2.68277, 'd23': 1.27788},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 300""",
)

entry(
    index = 670,
    label = "C3H8 + C5H7 <=> C5H8 + C3H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.4522, 'd13': 2.7145, 'd23': 1.26652},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 301""",
)

entry(
    index = 671,
    label = "C3H8 + C6H7-3 <=> C6H8-3 + C3H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.49045, 'd13': 2.73836, 'd23': 1.25108},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 302""",
)

entry(
    index = 672,
    label = "C4H6 + C3H7-1 <=> C4H5 + C3H8-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.43051, 'd13': 2.67652, 'd23': 1.26709},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 303""",
)

entry(
    index = 673,
    label = "C2H2O + C6H7-3 <=> C2HO + C6H8-3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.56756, 'd13': 2.73629, 'd23': 1.19956},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 304""",
)

entry(
    index = 674,
    label = "CH2O + C5H7 <=> CHO + C5H8",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.39501, 'd13': 2.71439, 'd23': 1.34171},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 305""",
)

entry(
    index = 675,
    label = "CH2O + C6H7-3 <=> CHO + C6H8-3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.40518, 'd13': 2.67611, 'd23': 1.33317},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 306""",
)

entry(
    index = 676,
    label = "CH4O + C6H7-3 <=> CH3O + C6H8-3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.46478, 'd13': 2.71438, 'd23': 1.27675},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 307""",
)

entry(
    index = 677,
    label = "C2H6O-1 + C5H7 <=> C2H5O-1 + C5H8",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.46049, 'd13': 2.72099, 'd23': 1.26293},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 308""",
)

entry(
    index = 678,
    label = "C2H6O-2 + C5H7 <=> C2H5O-2 + C5H8",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.36954, 'd13': 2.55492, 'd23': 1.19996},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 309""",
)

entry(
    index = 679,
    label = "C2H6O + C6H7-3 <=> C2H5O + C6H8-3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.44841, 'd13': 2.72027, 'd23': 1.2915},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 310""",
)

entry(
    index = 680,
    label = "C2H6O-1 + C4H5-1 <=> C2H5O-1 + C4H6-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.30771, 'd13': 2.67317, 'd23': 1.3715},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 311""",
)

entry(
    index = 681,
    label = "C2H6O-2 + C4H5-1 <=> C2H5O-2 + C4H6-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.22374, 'd13': 2.47315, 'd23': 1.26262},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 312""",
)

entry(
    index = 682,
    label = "C4H6 + C2H5O-2 <=> C4H5 + C2H6O-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.29281, 'd13': 2.46742, 'd23': 1.19167},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 313""",
)

entry(
    index = 683,
    label = "C2H4O + C5H7 <=> C2H3O + C5H8",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.4035, 'd13': 2.69908, 'd23': 1.3031},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 314""",
)

entry(
    index = 684,
    label = "C4H6-1 + C2H3O <=> C2H4O + C4H5-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.38149, 'd13': 2.67549, 'd23': 1.30426},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 315""",
)

entry(
    index = 685,
    label = "C4H6 + C2H3O <=> C4H5 + C2H4O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.4648, 'd13': 2.69416, 'd23': 1.24191},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 316""",
)

entry(
    index = 686,
    label = "C2H6 + C6H7-3 <=> C6H8-3 + C2H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.48985, 'd13': 2.73592, 'd23': 1.2516},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 317""",
)

entry(
    index = 687,
    label = "C4H6 + CH3O <=> C4H5 + CH4O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.45256, 'd13': 2.67681, 'd23': 1.25253},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 318""",
)

entry(
    index = 688,
    label = "C4H6 + CHO <=> C4H5 + CH2O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.51785, 'd13': 2.73543, 'd23': 1.23344},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 319""",
)

entry(
    index = 689,
    label = "C4H6-1 + C3H3O-1 <=> C4H5-1 + C3H4O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.42103, 'd13': 2.7049, 'd23': 1.30563},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 320""",
)

entry(
    index = 690,
    label = "C3H4O-1 + C5H7 <=> C5H8 + C3H3O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.39477, 'd13': 2.73862, 'd23': 1.35345},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 321""",
)

entry(
    index = 691,
    label = "C3H4O-1 + C6H7-3 <=> C6H8-3 + C3H3O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.44654, 'd13': 2.73633, 'd23': 1.31698},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 322""",
)

entry(
    index = 692,
    label = "CH3-1 + C6H11O <=> C6H12O + CH2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.44365, 'd13': 2.68253, 'd23': 1.24477},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 323""",
)

entry(
    index = 693,
    label = "CH4 + C4H7 <=> C4H8 + CH3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.47071, 'd13': 2.7138, 'd23': 1.25004},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 324""",
)

entry(
    index = 694,
    label = "C3H6 + C4H7 <=> C4H8 + C3H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.36693, 'd13': 2.69409, 'd23': 1.33069},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 325""",
)

entry(
    index = 695,
    label = "H2 + C4H7 <=> C4H8 + H",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.04556, 'd13': 2.28907, 'd23': 1.24931},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 326""",
)

entry(
    index = 696,
    label = "H2O + C4H7 <=> C4H8 + HO",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.50989, 'd13': 2.63461, 'd23': 1.1469},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 327""",
)

entry(
    index = 697,
    label = "C4H8 + O2 <=> C4H7 + HO2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.44047, 'd13': 2.58595, 'd23': 1.14943},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 328""",
)

entry(
    index = 698,
    label = "H2O2 + C4H7 <=> C4H8 + HO2-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.25759, 'd13': 2.5216, 'd23': 1.27808},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 329""",
)

entry(
    index = 699,
    label = "C3H4-1 + C4H7 <=> C4H8 + C3H3-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.39822, 'd13': 2.69887, 'd23': 1.30388},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 330""",
)

entry(
    index = 700,
    label = "C4H6-1 + C4H7 <=> C4H8 + C4H5-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.48659, 'd13': 2.7203, 'd23': 1.23827},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 331""",
)

entry(
    index = 701,
    label = "C2H4 + C4H7 <=> C4H8 + C2H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.50256, 'd13': 2.71956, 'd23': 1.22245},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 332""",
)

entry(
    index = 702,
    label = "C3H6-1 + C4H7 <=> C4H8 + C3H5-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.50503, 'd13': 2.71493, 'd23': 1.22274},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 333""",
)

entry(
    index = 703,
    label = "C3H6-2 + C4H7 <=> C4H8 + C3H5-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.47479, 'd13': 2.71435, 'd23': 1.24181},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 334""",
)

entry(
    index = 704,
    label = "C3H8-1 + C4H7 <=> C4H8 + C3H7-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.4227, 'd13': 2.70008, 'd23': 1.28031},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 335""",
)

entry(
    index = 705,
    label = "C2H6O + C4H7 <=> C4H8 + C2H5O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.40173, 'd13': 2.68493, 'd23': 1.31124},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 336""",
)

entry(
    index = 706,
    label = "C2H4O-1 + C4H7 <=> C4H8 + C2H3O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.37804, 'd13': 2.71526, 'd23': 1.36021},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 337""",
)

entry(
    index = 707,
    label = "C2H4O + C4H7 <=> C4H8 + C2H3O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.39284, 'd13': 2.68806, 'd23': 1.30218},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 338""",
)

entry(
    index = 708,
    label = "C2H6 + C4H7 <=> C4H8 + C2H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.44471, 'd13': 2.70983, 'd23': 1.26907},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 339""",
)

entry(
    index = 709,
    label = "C2H2O + C4H7 <=> C4H8 + C2HO",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.51223, 'd13': 2.69609, 'd23': 1.1971},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 340""",
)

entry(
    index = 710,
    label = "C2H2 + C4H7 <=> C4H8 + C2H",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.87803, 'd13': 2.90963, 'd23': 1.12015},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 341""",
)

entry(
    index = 711,
    label = "CH4 + C5H5 <=> C5H6 + CH3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.50981, 'd13': 2.73802, 'd23': 1.23495},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 342""",
)

entry(
    index = 712,
    label = "C3H6 + C5H5 <=> C5H6 + C3H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.41701, 'd13': 2.72946, 'd23': 1.31543},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 343""",
)

entry(
    index = 713,
    label = "H2 + C5H5 <=> C5H6 + H",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.08669, 'd13': 2.31365, 'd23': 1.22696},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 344""",
)

entry(
    index = 714,
    label = "HO-1 + C5H5 <=> C5H6 + O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.35558, 'd13': 2.56073, 'd23': 1.20524},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 345""",
)

entry(
    index = 715,
    label = "H2O2 + C5H5 <=> C5H6 + HO2-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.26548, 'd13': 2.53967, 'd23': 1.29463},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 346""",
)

entry(
    index = 716,
    label = "C3H4-1 + C5H5 <=> C5H6 + C3H3-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.42982, 'd13': 2.70766, 'd23': 1.28483},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 347""",
)

entry(
    index = 717,
    label = "C3H8 + C5H5 <=> C5H6 + C3H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.49281, 'd13': 2.73394, 'd23': 1.24783},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 348""",
)

entry(
    index = 718,
    label = "C3H8-1 + C5H5 <=> C5H6 + C3H7-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.47588, 'd13': 2.72785, 'd23': 1.25929},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 349""",
)

entry(
    index = 719,
    label = "C2H6O + C5H5 <=> C5H6 + C2H5O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.45355, 'd13': 2.71445, 'd23': 1.28719},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 350""",
)

entry(
    index = 720,
    label = "C2H6O-1 + C5H5 <=> C5H6 + C2H5O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.49597, 'd13': 2.73547, 'd23': 1.24675},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 351""",
)

entry(
    index = 721,
    label = "C2H6O-2 + C5H5 <=> C5H6 + C2H5O-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.35029, 'd13': 2.55664, 'd23': 1.21167},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 352""",
)

entry(
    index = 722,
    label = "C2H4O-1 + C5H5 <=> C5H6 + C2H3O-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.41773, 'd13': 2.73482, 'd23': 1.33141},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 353""",
)

entry(
    index = 723,
    label = "C2H4O + C5H5 <=> C5H6 + C2H3O",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.44527, 'd13': 2.71553, 'd23': 1.27473},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 354""",
)

entry(
    index = 724,
    label = "C2H6 + C5H5 <=> C5H6 + C2H5",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.49166, 'd13': 2.73256, 'd23': 1.2491},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 355""",
)

entry(
    index = 725,
    label = "C2H2O + C5H5 <=> C5H6 + C2HO",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.48687, 'd13': 2.69238, 'd23': 1.22726},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 356""",
)

entry(
    index = 726,
    label = "CH2O + C5H5 <=> C5H6 + CHO",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.44528, 'd13': 2.70575, 'd23': 1.31716},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 357""",
)

entry(
    index = 727,
    label = "C4H8 + C5H5 <=> C5H6 + C4H7",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.39346, 'd13': 2.71818, 'd23': 1.32679},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 358""",
)

entry(
    index = 728,
    label = "CH4 + C5H5-1 <=> C5H6-1 + CH3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.27339, 'd13': 2.67085, 'd23': 1.39771},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 359""",
)

entry(
    index = 729,
    label = "C5H6-1 + C3H5 <=> C5H5-1 + C3H6",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.50984, 'd13': 2.71499, 'd23': 1.2163},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 360""",
)

entry(
    index = 730,
    label = "H2 + C5H5-1 <=> C5H6-1 + H",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 0.850002, 'd13': 2.31972, 'd23': 1.46973},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 361""",
)

entry(
    index = 731,
    label = "H2O + C5H5-1 <=> C5H6-1 + HO",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.26358, 'd13': 2.46578, 'd23': 1.22001},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 362""",
)

entry(
    index = 732,
    label = "C5H6-1 + O2 <=> C5H5-1 + HO2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.71724, 'd13': 2.71885, 'd23': 1.02215},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 363""",
)

entry(
    index = 733,
    label = "C5H6-1 + HO2-1 <=> C5H5-1 + H2O2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.43772, 'd13': 2.51563, 'd23': 1.08854},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 364""",
)

entry(
    index = 734,
    label = "C5H6-1 + C3H3 <=> C5H5-1 + C3H4",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.45942, 'd13': 2.6851, 'd23': 1.22673},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 365""",
)

entry(
    index = 735,
    label = "C2H4 + C5H5-1 <=> C5H6-1 + C2H3",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.2893, 'd13': 2.64125, 'd23': 1.36199},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 366""",
)

entry(
    index = 736,
    label = "C3H6-1 + C5H5-1 <=> C5H6-1 + C3H5-1",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.292, 'd13': 2.63872, 'd23': 1.35669},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 367""",
)

entry(
    index = 737,
    label = "C3H6-2 + C5H5-1 <=> C5H6-1 + C3H5-2",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.26716, 'd13': 2.65954, 'd23': 1.39863},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 368""",
)

entry(
    index = 738,
    label = "C5H6-1 + C3H7 <=> C5H5-1 + C3H8",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.43377, 'd13': 2.683, 'd23': 1.25243},
        method = 'm062x/6-311+G(2df,2p)',
    ),
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 369""",
)

entry(
    index = 1029,
    label = "CH4 + C4H7-1 <=> C4H8-1 + CH3",
    distances = DistanceData(
        distances = {'d12': 1.31658, 'd13': 2.68174, 'd23': 1.36865},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 768""",
)

entry(
    index = 907,
    label = "C6H8 + C2H5 <=> C2H6 + C6H7",
    distances = DistanceData(
        distances = {'d12': 1.26228, 'd13': 2.7051, 'd23': 1.45857},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1051,
    label = "C4H8-1 + C3H7-1 <=> C4H7-1 + C3H8-1",
    distances = DistanceData(
        distances = {'d12': 1.3144, 'd13': 2.68485, 'd23': 1.3737},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 897""",
)

entry(
    index = 977,
    label = "C3H8 + C4H9 <=> C4H10 + C3H7",
    distances = DistanceData(
        distances = {'d12': 1.34357, 'd13': 2.68932, 'd23': 1.34993},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 815""",
)

entry(
    index = 1154,
    label = "H2 + C4H7O3 <=> H + C4H8O3",
    distances = DistanceData(
        distances = {'d12': 1.17526, 'd13': 2.10644, 'd23': 0.933968},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 945""",
)

entry(
    index = 1045,
    label = "C6H12O + C2H3O <=> C6H11O + C2H4O",
    distances = DistanceData(
        distances = {'d12': 1.37417, 'd13': 2.68214, 'd23': 1.31883},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 791""",
)

entry(
    index = 830,
    label = "C5H6-1 + C2H5O-1 <=> C2H6O-1 + C5H5-1",
    distances = DistanceData(
        distances = {'d12': 1.43422, 'd13': 2.67314, 'd23': 1.25801},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 967,
    label = "C4H9 + C3H4 <=> C4H10 + C3H3",
    distances = DistanceData(
        distances = {'d12': 1.30584, 'd13': 2.66777, 'd23': 1.36856},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1089,
    label = "C2H6 + C7H13O <=> C7H14O + C2H5",
    distances = DistanceData(
        distances = {'d12': 1.26281, 'd13': 2.70619, 'd23': 1.45623},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 924""",
)

entry(
    index = 928,
    label = "C4H10 + H <=> H2 + C4H9",
    distances = DistanceData(
        distances = {'d12': 1.36224, 'd13': 2.2802, 'd23': 0.920142},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1138,
    label = "H2O + C4H9 <=> C4H10 + HO",
    distances = DistanceData(
        distances = {'d12': 1.16316, 'd13': 2.5778, 'd23': 1.42849},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 756""",
)

entry(
    index = 1182,
    label = "C2HO-1 + C7H13O3-1 <=> C2O + C7H14O3-1",
    distances = DistanceData(
        distances = {'d12': 1.20322, 'd13': 2.47449, 'd23': 1.30463},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 911""",
)

entry(
    index = 886,
    label = "C3H3O + HO2 <=> C3H4O + O2",
    distances = DistanceData(
        distances = {'d12': 1.12756, 'd13': 2.58337, 'd23': 1.47776},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 809,
    label = "C2O + C6H8-3 <=> C2HO-1 + C6H7-3",
    distances = DistanceData(
        distances = {'d12': 1.27451, 'd13': 2.69334, 'd23': 1.43806},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 993,
    label = "C2H6 + C4H5O <=> C4H6O + C2H5",
    distances = DistanceData(
        distances = {'d12': 1.29624, 'd13': 2.7028, 'd23': 1.41609},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 761""",
)

entry(
    index = 1185,
    label = "CH4O + C5H7 <=> CH3O + C5H8",
    distances = DistanceData(
        distances = {'d12': 1.30583, 'd13': 2.68, 'd23': 1.41848},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 843""",
)

entry(
    index = 1128,
    label = "C2HO-1 + C3H7 <=> C2O + C3H8",
    distances = DistanceData(
        distances = {'d12': 1.3731, 'd13': 2.6576, 'd23': 1.29024},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 900""",
)

entry(
    index = 890,
    label = "C2H6O-1 + C6H5 <=> C6H6 + C2H5O-1",
    distances = DistanceData(
        distances = {'d12': 1.27191, 'd13': 2.66815, 'd23': 1.41251},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1058,
    label = "CH3-1 + C2H5O-1 <=> C2H6O-1 + CH2",
    distances = DistanceData(
        distances = {'d12': 1.29952, 'd13': 2.65527, 'd23': 1.36789},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 942""",
)

entry(
    index = 751,
    label = "C6H8 + CH2 <=> CH3-1 + C6H7",
    distances = DistanceData(
        distances = {'d12': 1.22945, 'd13': 2.69941, 'd23': 1.48121},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1118,
    label = "C4H8-1 + C3H3 <=> C4H7-1 + C3H4",
    distances = DistanceData(
        distances = {'d12': 1.30055, 'd13': 2.66745, 'd23': 1.3757},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 861""",
)

entry(
    index = 1209,
    label = "C2H6O-2 + C4H9 <=> C4H10 + C2H5O-2",
    distances = DistanceData(
        distances = {'d12': 1.23896, 'd13': 2.51204, 'd23': 1.27424},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 848""",
)

entry(
    index = 1206,
    label = "CH4 + C4H9 <=> C4H10 + CH3",
    distances = DistanceData(
        distances = {'d12': 1.31259, 'd13': 2.68284, 'd23': 1.3725},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 885""",
)

entry(
    index = 1020,
    label = "C4H4 + C6H5 <=> C6H6 + C4H3",
    distances = DistanceData(
        distances = {'d12': 1.31609, 'd13': 2.63793, 'd23': 1.3296},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 870""",
)

entry(
    index = 1198,
    label = "C4H10 + C3H3-2 <=> C4H9 + C3H4-1",
    distances = DistanceData(
        distances = {'d12': 1.30166, 'd13': 2.69315, 'd23': 1.39287},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 899""",
)

entry(
    index = 1019,
    label = "C3H6-2 + C3H2 <=> C3H3-1 + C3H5-2",
    distances = DistanceData(
        distances = {'d12': 1.2802, 'd13': 2.65511, 'd23': 1.37946},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 760""",
)

entry(
    index = 1096,
    label = "C4H10 + C3H3O-1 <=> C4H9 + C3H4O-1",
    distances = DistanceData(
        distances = {'d12': 1.29628, 'd13': 2.72409, 'd23': 1.44175},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 834""",
)

entry(
    index = 1080,
    label = "H2 + C4H9 <=> C4H10 + H",
    distances = DistanceData(
        distances = {'d12': 1.36224, 'd13': 2.2802, 'd23': 0.920142},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 928""",
)

entry(
    index = 1160,
    label = "HO-1 + C7H13O <=> C7H14O + O",
    distances = DistanceData(
        distances = {'d12': 1.25832, 'd13': 2.50711, 'd23': 1.24903},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 965""",
)

entry(
    index = 860,
    label = "C6H11O + CH4O <=> C6H12O + CH3O",
    distances = DistanceData(
        distances = {'d12': 1.39573, 'd13': 2.69101, 'd23': 1.32711},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 823,
    label = "C4H8-1 + C5H5-1 <=> C5H6-1 + C4H7-1",
    distances = DistanceData(
        distances = {'d12': 1.25779, 'd13': 2.68301, 'd23': 1.4303},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1010,
    label = "C2HO-1 + C6H11O <=> C6H12O + C2O",
    distances = DistanceData(
        distances = {'d12': 1.3268, 'd13': 2.65341, 'd23': 1.34368},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 739""",
)

entry(
    index = 1113,
    label = "C5H6-1 + C3H3O-1 <=> C5H5-1 + C3H4O-1",
    distances = DistanceData(
        distances = {'d12': 1.21228, 'd13': 2.77185, 'd23': 1.56487},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 926""",
)

entry(
    index = 763,
    label = "C5H5-1 + C4H6-1 <=> C5H6-1 + C4H5-1",
    distances = DistanceData(
        distances = {'d12': 1.25326, 'd13': 2.67051, 'd23': 1.41772},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1168,
    label = "C4H8O3 + O2 <=> HO2 + C4H7O3",
    distances = DistanceData(
        distances = {'d12': 1.05085, 'd13': 2.45125, 'd23': 1.40891},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 774""",
)

entry(
    index = 1176,
    label = "C4H6 + H <=> C4H5 + H2",
    distances = DistanceData(
        distances = {'d12': 0.868906, 'd13': 2.29421, 'd23': 1.42789},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 955""",
)

entry(
    index = 788,
    label = "C6H8 + C3H3O-1 <=> C3H4O-1 + C6H7",
    distances = DistanceData(
        distances = {'d12': 1.32693, 'd13': 2.72644, 'd23': 1.40764},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 873,
    label = "C3H5-2 + C5H8-1 <=> C3H6-2 + C5H7-1",
    distances = DistanceData(
        distances = {'d12': 1.22668, 'd13': 2.74045, 'd23': 1.5169},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1144,
    label = "C2H2O + C3H3O <=> C3H4O + C2HO",
    distances = DistanceData(
        distances = {'d12': 1.20818, 'd13': 2.70272, 'd23': 1.50799},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 883""",
)

entry(
    index = 1070,
    label = "C5H6-1 + CH3O <=> C5H5-1 + CH4O",
    distances = DistanceData(
        distances = {'d12': 1.23286, 'd13': 2.698, 'd23': 1.48209},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 790""",
)

entry(
    index = 925,
    label = "C2H5O-2 + C6H8-3 <=> C2H6O-2 + C6H7-3",
    distances = DistanceData(
        distances = {'d12': 1.16827, 'd13': 2.60362, 'd23': 1.47037},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 952,
    label = "C2H4O + C3H5-1 <=> C3H6-1 + C2H3O",
    distances = DistanceData(
        distances = {'d12': 1.24294, 'd13': 2.69569, 'd23': 1.46406},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1126,
    label = "C2H6O-1 + C3H3O <=> C3H4O + C2H5O-1",
    distances = DistanceData(
        distances = {'d12': 1.27855, 'd13': 2.69884, 'd23': 1.43642},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 933""",
)

entry(
    index = 1033,
    label = "C5H6-1 + C4H7-1 <=> C4H8-1 + C5H5-1",
    distances = DistanceData(
        distances = {'d12': 1.25779, 'd13': 2.68301, 'd23': 1.4303},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 823""",
)

entry(
    index = 804,
    label = "CH2O + C3H7 <=> C3H8 + CHO",
    distances = DistanceData(
        distances = {'d12': 1.29165, 'd13': 2.71612, 'd23': 1.4446},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 851,
    label = "C4H5 + C3H4O-1 <=> C4H6 + C3H3O-1",
    distances = DistanceData(
        distances = {'d12': 1.23749, 'd13': 2.76161, 'd23': 1.52791},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 915,
    label = "C2H3O + C6H8 <=> C2H4O + C6H7",
    distances = DistanceData(
        distances = {'d12': 1.28222, 'd13': 2.70728, 'd23': 1.43207},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 948,
    label = "C5H5-1 + C2H6 <=> C5H6-1 + C2H5",
    distances = DistanceData(
        distances = {'d12': 1.25029, 'd13': 2.67572, 'd23': 1.4357},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 790,
    label = "C5H5-1 + CH4O <=> C5H6-1 + CH3O",
    distances = DistanceData(
        distances = {'d12': 1.23286, 'd13': 2.698, 'd23': 1.48209},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 812,
    label = "C3H5O + H2O2 <=> C3H6O + HO2-1",
    distances = DistanceData(
        distances = {'d12': 1.18004, 'd13': 2.50468, 'd23': 1.33384},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 869,
    label = "C2H6O + C3H5-1 <=> C3H6-1 + C2H5O",
    distances = DistanceData(
        distances = {'d12': 1.25163, 'd13': 2.69261, 'd23': 1.46878},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 984,
    label = "C2HO-1 + C4H5O3 <=> C2O + C4H6O3",
    distances = DistanceData(
        distances = {'d12': 1.29547, 'd13': 2.44288, 'd23': 1.22556},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 821""",
)

entry(
    index = 828,
    label = "C3H3-2 + C3H4O-1 <=> C3H4-1 + C3H3O-1",
    distances = DistanceData(
        distances = {'d12': 1.33338, 'd13': 2.73703, 'd23': 1.41055},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 786,
    label = "C3H5O + C6H8 <=> C3H6O + C6H7",
    distances = DistanceData(
        distances = {'d12': 1.27728, 'd13': 2.69872, 'd23': 1.43575},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1100,
    label = "C2H6O-1 + C4H7 <=> C4H8 + C2H5O-1",
    distances = DistanceData(
        distances = {'d12': 1.26366, 'd13': 2.71186, 'd23': 1.45239},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 903""",
)

entry(
    index = 770,
    label = "C4H9 + CH2O <=> C4H10 + CHO",
    distances = DistanceData(
        distances = {'d12': 1.29256, 'd13': 2.71979, 'd23': 1.44608},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 955,
    label = "C4H5 + H2 <=> C4H6 + H",
    distances = DistanceData(
        distances = {'d12': 0.868906, 'd13': 2.29421, 'd23': 1.42789},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1063,
    label = "C3H6-1 + C2H3O <=> C2H4O + C3H5-1",
    distances = DistanceData(
        distances = {'d12': 1.24294, 'd13': 2.69569, 'd23': 1.46406},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 952""",
)

entry(
    index = 941,
    label = "C2O + C6H8 <=> C2HO-1 + C6H7",
    distances = DistanceData(
        distances = {'d12': 1.28566, 'd13': 2.66596, 'd23': 1.41018},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1161,
    label = "C3H8-1 + C4H5O <=> C4H6O + C3H7-1",
    distances = DistanceData(
        distances = {'d12': 1.31482, 'd13': 2.70454, 'd23': 1.39366},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 905""",
)

entry(
    index = 1194,
    label = "C3H6-2 + C4H9 <=> C4H10 + C3H5-2",
    distances = DistanceData(
        distances = {'d12': 1.311, 'd13': 2.67475, 'd23': 1.36923},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 855""",
)

entry(
    index = 1003,
    label = "CH3-1 + C6H7 <=> C6H8 + CH2",
    distances = DistanceData(
        distances = {'d12': 1.22945, 'd13': 2.69941, 'd23': 1.48121},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 751""",
)

entry(
    index = 1041,
    label = "H2 + C4H7-1 <=> C4H8-1 + H",
    distances = DistanceData(
        distances = {'d12': 1.35991, 'd13': 2.27964, 'd23': 0.922801},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 832""",
)

entry(
    index = 932,
    label = "C2H5O-2 + C3H3-1 <=> C2H6O-2 + C3H2",
    distances = DistanceData(
        distances = {'d12': 1.23187, 'd13': 2.48503, 'd23': 1.26673},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 834,
    label = "C4H9 + C3H4O-1 <=> C4H10 + C3H3O-1",
    distances = DistanceData(
        distances = {'d12': 1.29628, 'd13': 2.72409, 'd23': 1.44175},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 963,
    label = "C4H7-1 + HO2 <=> C4H8-1 + O2",
    distances = DistanceData(
        distances = {'d12': 1.071, 'd13': 2.63014, 'd23': 1.56838},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1002,
    label = "C3H8-1 + C6H7-3 <=> C6H8-3 + C3H7-1",
    distances = DistanceData(
        distances = {'d12': 1.25999, 'd13': 2.72483, 'd23': 1.46614},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 871""",
)

entry(
    index = 1122,
    label = "CH4 + C3H3O-1 <=> CH3 + C3H4O-1",
    distances = DistanceData(
        distances = {'d12': 1.27053, 'd13': 2.74347, 'd23': 1.47295},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 806""",
)

entry(
    index = 1079,
    label = "H2O2 + C5H7-1 <=> HO2-1 + C5H8-1",
    distances = DistanceData(
        distances = {'d12': 1.2596, 'd13': 2.54094, 'd23': 1.29536},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 841""",
)

entry(
    index = 846,
    label = "CH2O + C3H5 <=> C3H6 + CHO",
    distances = DistanceData(
        distances = {'d12': 1.36139, 'd13': 2.73144, 'd23': 1.37055},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1038,
    label = "H2 + CHO <=> CH2O + H",
    distances = DistanceData(
        distances = {'d12': 1.26516, 'd13': 2.33001, 'd23': 1.06488},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 949""",
)

entry(
    index = 1134,
    label = "C4H8-1 + CHO <=> C4H7-1 + CH2O",
    distances = DistanceData(
        distances = {'d12': 1.28691, 'd13': 2.73049, 'd23': 1.45431},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 974""",
)

entry(
    index = 819,
    label = "C6H11O + HO2 <=> C6H12O + O2",
    distances = DistanceData(
        distances = {'d12': 1.1049, 'd13': 2.59673, 'd23': 1.50072},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 894,
    label = "C3H4 + C4H3-2 <=> C4H4-2 + C3H3",
    distances = DistanceData(
        distances = {'d12': 1.33324, 'd13': 2.66168, 'd23': 1.33955},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 755,
    label = "C6H8-1 + C3H5 <=> C3H6 + C6H7-1",
    distances = DistanceData(
        distances = {'d12': 1.34303, 'd13': 2.69934, 'd23': 1.36251},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 741,
    label = "C4H9 + C2H6 <=> C4H10 + C2H5",
    distances = DistanceData(
        distances = {'d12': 1.34613, 'd13': 2.69062, 'd23': 1.34864},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1190,
    label = "C4H8O3 + CH3O <=> CH4O + C4H7O3",
    distances = DistanceData(
        distances = {'d12': 1.2397, 'd13': 2.54065, 'd23': 1.31272},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 904""",
)

entry(
    index = 1024,
    label = "CH4 + C6H7-1 <=> C6H8-1 + CH3",
    distances = DistanceData(
        distances = {'d12': 1.24498, 'd13': 2.70693, 'd23': 1.46572},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 818""",
)

entry(
    index = 902,
    label = "C3H6 + CH2 <=> CH3-1 + C3H5",
    distances = DistanceData(
        distances = {'d12': 1.25295, 'd13': 2.69011, 'd23': 1.43716},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1056,
    label = "C3H6-2 + C5H7-1 <=> C3H5-2 + C5H8-1",
    distances = DistanceData(
        distances = {'d12': 1.22668, 'd13': 2.74045, 'd23': 1.5169},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 873""",
)

entry(
    index = 974,
    label = "C4H7-1 + CH2O <=> C4H8-1 + CHO",
    distances = DistanceData(
        distances = {'d12': 1.28691, 'd13': 2.73049, 'd23': 1.45431},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1153,
    label = "H2 + C3H3-2 <=> H + C3H4-1",
    distances = DistanceData(
        distances = {'d12': 1.28684, 'd13': 2.27534, 'd23': 0.989057},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 930""",
)

entry(
    index = 1191,
    label = "C6H12O + C3H5 <=> C6H11O + C3H6",
    distances = DistanceData(
        distances = {'d12': 1.34419, 'd13': 2.68744, 'd23': 1.3542},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 782""",
)

entry(
    index = 971,
    label = "C4H6O + C3H7 <=> C3H8 + C4H5O",
    distances = DistanceData(
        distances = {'d12': 1.29249, 'd13': 2.70409, 'd23': 1.41556},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1009,
    label = "C4H10 + C2H3O <=> C4H9 + C2H4O",
    distances = DistanceData(
        distances = {'d12': 1.29263, 'd13': 2.69713, 'd23': 1.40578},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 780""",
)

entry(
    index = 1084,
    label = "C4H4-2 + C2H3O-1 <=> C2H4O-1 + C4H3-2",
    distances = DistanceData(
        distances = {'d12': 1.29821, 'd13': 2.71699, 'd23': 1.43014},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 872""",
)

entry(
    index = 883,
    label = "C3H4O + C2HO <=> C2H2O + C3H3O",
    distances = DistanceData(
        distances = {'d12': 1.20818, 'd13': 2.70272, 'd23': 1.50799},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 994,
    label = "C2HO-1 + CH3O <=> C2O + CH4O",
    distances = DistanceData(
        distances = {'d12': 1.33986, 'd13': 2.66562, 'd23': 1.33683},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 773""",
)

entry(
    index = 1186,
    label = "CH4O + C4H5O <=> C4H6O + CH3O",
    distances = DistanceData(
        distances = {'d12': 1.33432, 'd13': 2.70859, 'd23': 1.38363},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 935""",
)

entry(
    index = 893,
    label = "C7H14O3-2 + H <=> H2 + C7H13O3-2",
    distances = DistanceData(
        distances = {'d12': 1.23924, 'd13': 2.28474, 'd23': 1.05547},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1036,
    label = "C3H4 + C5H5 <=> C5H6 + C3H3",
    distances = DistanceData(
        distances = {'d12': 1.28818, 'd13': 2.71621, 'd23': 1.43215},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 914""",
)

entry(
    index = 767,
    label = "C5H5-1 + C4H8 <=> C5H6-1 + C4H7",
    distances = DistanceData(
        distances = {'d12': 1.20054, 'd13': 2.73647, 'd23': 1.54533},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 774,
    label = "HO2 + C4H7O3 <=> C4H8O3 + O2",
    distances = DistanceData(
        distances = {'d12': 1.05085, 'd13': 2.45125, 'd23': 1.40891},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1205,
    label = "CH4O + C3H3 <=> CH3O + C3H4",
    distances = DistanceData(
        distances = {'d12': 1.35448, 'd13': 2.64694, 'd23': 1.33566},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 837""",
)

entry(
    index = 1140,
    label = "C3H4O + O2 <=> C3H3O + HO2",
    distances = DistanceData(
        distances = {'d12': 1.12756, 'd13': 2.58337, 'd23': 1.47776},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 886""",
)

entry(
    index = 1093,
    label = "C3H6-1 + C2H5O <=> C2H6O + C3H5-1",
    distances = DistanceData(
        distances = {'d12': 1.25163, 'd13': 2.69261, 'd23': 1.46878},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 869""",
)

entry(
    index = 1083,
    label = "C4H6O3 + CH3O <=> CH4O + C4H5O3",
    distances = DistanceData(
        distances = {'d12': 1.23697, 'd13': 2.5442, 'd23': 1.31812},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 754""",
)

entry(
    index = 911,
    label = "C2O + C7H14O3-1 <=> C2HO-1 + C7H13O3-1",
    distances = DistanceData(
        distances = {'d12': 1.20322, 'd13': 2.47449, 'd23': 1.30463},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 944,
    label = "C5H5 + C5H8 <=> C5H6 + C5H7",
    distances = DistanceData(
        distances = {'d12': 1.38704, 'd13': 2.73712, 'd23': 1.35364},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 816,
    label = "C3H4O + C2H5 <=> C2H6 + C3H3O",
    distances = DistanceData(
        distances = {'d12': 1.29343, 'd13': 2.69759, 'd23': 1.41322},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 824,
    label = "C3H6O + C2H5 <=> C2H6 + C3H5O",
    distances = DistanceData(
        distances = {'d12': 1.3031, 'd13': 2.68154, 'd23': 1.38809},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 782,
    label = "C6H11O + C3H6 <=> C6H12O + C3H5",
    distances = DistanceData(
        distances = {'d12': 1.34419, 'd13': 2.68744, 'd23': 1.3542},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 879,
    label = "C4H7-1 + C4H6-1 <=> C4H8-1 + C4H5-1",
    distances = DistanceData(
        distances = {'d12': 1.38408, 'd13': 2.6733, 'd23': 1.29385},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1104,
    label = "C5H6 + O2 <=> C5H5 + HO2",
    distances = DistanceData(
        distances = {'d12': 1.1551, 'd13': 2.61984, 'd23': 1.4756},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 919""",
)

entry(
    index = 1068,
    label = "C2H4O + C6H7 <=> C2H3O + C6H8",
    distances = DistanceData(
        distances = {'d12': 1.28222, 'd13': 2.70728, 'd23': 1.43207},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 915""",
)

entry(
    index = 1116,
    label = "C2HO-1 + C4H7O3 <=> C2O + C4H8O3",
    distances = DistanceData(
        distances = {'d12': 1.29824, 'd13': 2.44224, 'd23': 1.22384},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 798""",
)

entry(
    index = 1165,
    label = "C3H4O + C3H3 <=> C3H3O + C3H4",
    distances = DistanceData(
        distances = {'d12': 1.38164, 'd13': 2.68056, 'd23': 1.31356},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 959""",
)

entry(
    index = 864,
    label = "HO2 + C5H7-1 <=> C5H8-1 + O2",
    distances = DistanceData(
        distances = {'d12': 1.17806, 'd13': 2.5809, 'd23': 1.41009},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1171,
    label = "C4H6 + C3H3O <=> C4H5 + C3H4O",
    distances = DistanceData(
        distances = {'d12': 1.23646, 'd13': 2.70816, 'd23': 1.48483},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 850""",
)

entry(
    index = 1159,
    label = "C2HO-1 + C4H3-2 <=> C2O + C4H4-2",
    distances = DistanceData(
        distances = {'d12': 1.33539, 'd13': 2.65038, 'd23': 1.32523},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 939""",
)

entry(
    index = 876,
    label = "C6H8-2 + C3H5 <=> C3H6 + C6H7-2",
    distances = DistanceData(
        distances = {'d12': 1.30176, 'd13': 2.70556, 'd23': 1.41366},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 936,
    label = "C6H8 + C4H3 <=> C4H4 + C6H7",
    distances = DistanceData(
        distances = {'d12': 1.19794, 'd13': 2.75226, 'd23': 1.55714},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 838,
    label = "C2H5O-2 + C5H8-1 <=> C2H6O-2 + C5H7-1",
    distances = DistanceData(
        distances = {'d12': 1.18827, 'd13': 2.59176, 'd23': 1.41159},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1006,
    label = "C4H8-1 + CH3O <=> C4H7-1 + CH4O",
    distances = DistanceData(
        distances = {'d12': 1.3149, 'd13': 2.69717, 'd23': 1.39395},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 863""",
)

entry(
    index = 842,
    label = "C2H4O-1 + C4H5-1 <=> C4H6-1 + C2H3O-1",
    distances = DistanceData(
        distances = {'d12': 1.29795, 'd13': 2.70193, 'd23': 1.42844},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 920,
    label = "C2H2O + C6H5 <=> C6H6 + C2HO",
    distances = DistanceData(
        distances = {'d12': 1.27346, 'd13': 2.6232, 'd23': 1.35092},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1034,
    label = "C5H8-1 + O2 <=> HO2 + C5H7-1",
    distances = DistanceData(
        distances = {'d12': 1.17806, 'd13': 2.5809, 'd23': 1.41009},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 864""",
)

entry(
    index = 1130,
    label = "CH2O + C4H7 <=> C4H8 + CHO",
    distances = DistanceData(
        distances = {'d12': 1.34691, 'd13': 2.72011, 'd23': 1.38629},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 847""",
)

entry(
    index = 1069,
    label = "C5H6-1 + C2H5 <=> C5H5-1 + C2H6",
    distances = DistanceData(
        distances = {'d12': 1.25029, 'd13': 2.67572, 'd23': 1.4357},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 948""",
)

entry(
    index = 801,
    label = "C4H8 + C3H3 <=> C3H4 + C4H7",
    distances = DistanceData(
        distances = {'d12': 1.28656, 'd13': 2.68616, 'd23': 1.4021},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 916,
    label = "C2H6 + CH2 <=> CH3-1 + C2H5",
    distances = DistanceData(
        distances = {'d12': 1.29393, 'd13': 2.65751, 'd23': 1.36785},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 854,
    label = "C3H2 + C3H4O-1 <=> C3H3-1 + C3H3O-1",
    distances = DistanceData(
        distances = {'d12': 1.29048, 'd13': 2.70823, 'd23': 1.42472},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 795,
    label = "C4H9 + HO2 <=> C4H10 + O2",
    distances = DistanceData(
        distances = {'d12': 1.07128, 'd13': 2.63224, 'd23': 1.56784},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 898,
    label = "C2H5O + C5H8-1 <=> C2H6O + C5H7-1",
    distances = DistanceData(
        distances = {'d12': 1.28329, 'd13': 2.70711, 'd23': 1.45592},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 983,
    label = "C2H6O-1 + C2O <=> C2HO-1 + C2H5O-1",
    distances = DistanceData(
        distances = {'d12': 1.27603, 'd13': 2.65577, 'd23': 1.39236},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 796""",
)

entry(
    index = 759,
    label = "C2H6O + C3H2 <=> C3H3-1 + C2H5O",
    distances = DistanceData(
        distances = {'d12': 1.30123, 'd13': 2.65081, 'd23': 1.38924},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 745,
    label = "C7H14O3-3 + H <=> H2 + C7H13O3-3",
    distances = DistanceData(
        distances = {'d12': 1.37479, 'd13': 2.28497, 'd23': 0.910186},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1048,
    label = "C4H6 + C2H3O-1 <=> C4H5 + C2H4O-1",
    distances = DistanceData(
        distances = {'d12': 1.22264, 'd13': 2.76781, 'd23': 1.55081},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 906""",
)

entry(
    index = 968,
    label = "C2HO-1 + C2H5O-2 <=> C2H6O-2 + C2O",
    distances = DistanceData(
        distances = {'d12': 1.20931, 'd13': 2.42545, 'd23': 1.29442},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1074,
    label = "C3H4-1 + C3H3O-1 <=> C3H3-2 + C3H4O-1",
    distances = DistanceData(
        distances = {'d12': 1.33338, 'd13': 2.73703, 'd23': 1.41055},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 828""",
)

entry(
    index = 775,
    label = "CH3 + C2H6 <=> CH4 + C2H5",
    distances = DistanceData(
        distances = {'d12': 1.3078, 'd13': 2.67929, 'd23': 1.37491},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 849,
    label = "C2H4O + C2H3 <=> C2H4 + C2H3O",
    distances = DistanceData(
        distances = {'d12': 1.24746, 'd13': 2.69391, 'd23': 1.458},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 956,
    label = "C4H7-1 + C4H8 <=> C4H8-1 + C4H7",
    distances = DistanceData(
        distances = {'d12': 1.26395, 'd13': 2.70656, 'd23': 1.4483},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1066,
    label = "C4H4 + C4H7 <=> C4H8 + C4H3",
    distances = DistanceData(
        distances = {'d12': 1.20907, 'd13': 2.7289, 'd23': 1.52599},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 740""",
)

entry(
    index = 1028,
    label = "H2O2 + C6H7-1 <=> C6H8-1 + HO2-1",
    distances = DistanceData(
        distances = {'d12': 1.26672, 'd13': 2.52787, 'd23': 1.2669},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 957""",
)

entry(
    index = 906,
    label = "C4H5 + C2H4O-1 <=> C4H6 + C2H3O-1",
    distances = DistanceData(
        distances = {'d12': 1.22264, 'd13': 2.76781, 'd23': 1.55081},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1052,
    label = "C2H6 + C3H5 <=> C3H6 + C2H5",
    distances = DistanceData(
        distances = {'d12': 1.28114, 'd13': 2.70064, 'd23': 1.4242},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 938""",
)

entry(
    index = 970,
    label = "C2H5O-1 + C4H8O3 <=> C2H6O-1 + C4H7O3",
    distances = DistanceData(
        distances = {'d12': 1.21026, 'd13': 2.49975, 'd23': 1.30339},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1011,
    label = "H2 + C7H13O3-4 <=> C7H14O3-4 + H",
    distances = DistanceData(
        distances = {'d12': 1.12442, 'd13': 2.11848, 'd23': 0.995758},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 802""",
)

entry(
    index = 1157,
    label = "C2H4 + C2H5O-1 <=> C2H6O-1 + C2H3",
    distances = DistanceData(
        distances = {'d12': 1.28725, 'd13': 2.66941, 'd23': 1.38918},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 797""",
)

entry(
    index = 1044,
    label = "C2H6 + C3H3O <=> C3H4O + C2H5",
    distances = DistanceData(
        distances = {'d12': 1.29343, 'd13': 2.69759, 'd23': 1.41322},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 816""",
)

entry(
    index = 833,
    label = "C6H12O + C2H5O-1 <=> C2H6O-1 + C6H11O",
    distances = DistanceData(
        distances = {'d12': 1.28226, 'd13': 2.70645, 'd23': 1.43343},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 966,
    label = "C2H5O-1 + C5H8-1 <=> C2H6O-1 + C5H7-1",
    distances = DistanceData(
        distances = {'d12': 1.24491, 'd13': 2.73182, 'd23': 1.4955},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1088,
    label = "C6H6 + C2H3O-1 <=> C2H4O-1 + C6H5",
    distances = DistanceData(
        distances = {'d12': 1.22745, 'd13': 2.74998, 'd23': 1.53858},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 931""",
)

entry(
    index = 1137,
    label = "C3H8 + C4H5O <=> C4H6O + C3H7",
    distances = DistanceData(
        distances = {'d12': 1.29249, 'd13': 2.70409, 'd23': 1.41556},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 971""",
)

entry(
    index = 887,
    label = "C2H3O-1 + C6H8-1 <=> C2H4O-1 + C6H7-1",
    distances = DistanceData(
        distances = {'d12': 1.35993, 'd13': 2.69198, 'd23': 1.36847},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 990,
    label = "C4H10 + C3H3 <=> C4H9 + C3H4",
    distances = DistanceData(
        distances = {'d12': 1.30584, 'd13': 2.66777, 'd23': 1.36856},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 967""",
)

entry(
    index = 897,
    label = "C4H7-1 + C3H8-1 <=> C4H8-1 + C3H7-1",
    distances = DistanceData(
        distances = {'d12': 1.3144, 'd13': 2.68485, 'd23': 1.3737},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 752,
    label = "C6H12O + C2H3 <=> C2H4 + C6H11O",
    distances = DistanceData(
        distances = {'d12': 1.23336, 'd13': 2.70964, 'd23': 1.48512},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1023,
    label = "C2HO-1 + C5H7-1 <=> C2O + C5H8-1",
    distances = DistanceData(
        distances = {'d12': 1.27178, 'd13': 2.68587, 'd23': 1.43053},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 772""",
)

entry(
    index = 901,
    label = "C6H8 + C4H3-1 <=> C4H4-1 + C6H7",
    distances = DistanceData(
        distances = {'d12': 1.25175, 'd13': 2.69783, 'd23': 1.45755},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1097,
    label = "C4H8-1 + O2 <=> C4H7-1 + HO2",
    distances = DistanceData(
        distances = {'d12': 1.071, 'd13': 2.63014, 'd23': 1.56838},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 963""",
)

entry(
    index = 1075,
    label = "C3H6O + C6H7 <=> C3H5O + C6H8",
    distances = DistanceData(
        distances = {'d12': 1.27728, 'd13': 2.69872, 'd23': 1.43575},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 786""",
)

entry(
    index = 938,
    label = "C3H6 + C2H5 <=> C2H6 + C3H5",
    distances = DistanceData(
        distances = {'d12': 1.28114, 'd13': 2.70064, 'd23': 1.4242},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1087,
    label = "C3H6-2 + C5H5 <=> C5H6 + C3H5-2",
    distances = DistanceData(
        distances = {'d12': 1.2249, 'd13': 2.73975, 'd23': 1.52504},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 742""",
)

entry(
    index = 880,
    label = "C3H5O + C6H8-2 <=> C3H6O + C6H7-2",
    distances = DistanceData(
        distances = {'d12': 1.26035, 'd13': 2.72489, 'd23': 1.46951},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 820,
    label = "C4H7-1 + C3H3-1 <=> C4H8-1 + C3H2",
    distances = DistanceData(
        distances = {'d12': 1.31227, 'd13': 2.65729, 'd23': 1.3528},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 875,
    label = "C2H + C6H8-2 <=> C2H2 + C6H7-2",
    distances = DistanceData(
        distances = {'d12': 1.11789, 'd13': 2.95802, 'd23': 1.92812},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1108,
    label = "C2HO-1 + C7H13O3-4 <=> C2O + C7H14O3-4",
    distances = DistanceData(
        distances = {'d12': 1.1624, 'd13': 2.45359, 'd23': 1.34106},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 845""",
)

entry(
    index = 778,
    label = "C4H8 + CH3O <=> CH4O + C4H7",
    distances = DistanceData(
        distances = {'d12': 1.3051, 'd13': 2.69432, 'd23': 1.40875},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1150,
    label = "H2 + C7H13O3-5 <=> C7H14O3-5 + H",
    distances = DistanceData(
        distances = {'d12': 1.25835, 'd13': 2.26959, 'd23': 1.02105},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 950""",
)

entry(
    index = 1112,
    label = "C3H6-2 + C2O <=> C2HO-1 + C3H5-2",
    distances = DistanceData(
        distances = {'d12': 1.24881, 'd13': 2.65744, 'd23': 1.41691},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 794""",
)

entry(
    index = 762,
    label = "C2H5O-1 + C6H8-1 <=> C2H6O-1 + C6H7-1",
    distances = DistanceData(
        distances = {'d12': 1.26231, 'd13': 2.69766, 'd23': 1.4453},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1169,
    label = "C4H4 + C4H7O3 <=> C4H3 + C4H8O3",
    distances = DistanceData(
        distances = {'d12': 1.14021, 'd13': 2.50003, 'd23': 1.36034},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 878""",
)

entry(
    index = 1175,
    label = "C4H4-1 + C4H5O <=> C4H6O + C4H3-1",
    distances = DistanceData(
        distances = {'d12': 1.28004, 'd13': 2.70043, 'd23': 1.42978},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 884""",
)

entry(
    index = 872,
    label = "C2H4O-1 + C4H3-2 <=> C4H4-2 + C2H3O-1",
    distances = DistanceData(
        distances = {'d12': 1.29821, 'd13': 2.71699, 'd23': 1.43014},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1145,
    label = "C2H2O + C5H7 <=> C2HO + C5H8",
    distances = DistanceData(
        distances = {'d12': 1.20374, 'd13': 2.69602, 'd23': 1.50184},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 799""",
)

entry(
    index = 1090,
    label = "C2HO-1 + C6H7-2 <=> C2O + C6H8-2",
    distances = DistanceData(
        distances = {'d12': 1.26308, 'd13': 2.68515, 'd23': 1.44379},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 874""",
)

entry(
    index = 924,
    label = "C7H14O + C2H5 <=> C2H6 + C7H13O",
    distances = DistanceData(
        distances = {'d12': 1.26281, 'd13': 2.70619, 'd23': 1.45623},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1030,
    label = "C6H12O + CH3O <=> C6H11O + CH4O",
    distances = DistanceData(
        distances = {'d12': 1.39573, 'd13': 2.69101, 'd23': 1.32711},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 860""",
)

entry(
    index = 1065,
    label = "C3H8 + CHO <=> CH2O + C3H7",
    distances = DistanceData(
        distances = {'d12': 1.29165, 'd13': 2.71612, 'd23': 1.4446},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 804""",
)

entry(
    index = 805,
    label = "C2O + C7H14O-1 <=> C2HO-1 + C7H13O-1",
    distances = DistanceData(
        distances = {'d12': 1.39483, 'd13': 2.65039, 'd23': 1.27497},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 912,
    label = "C4H8 + C2O <=> C2HO-1 + C4H7",
    distances = DistanceData(
        distances = {'d12': 1.2934, 'd13': 2.67343, 'd23': 1.38322},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 850,
    label = "C4H5 + C3H4O <=> C4H6 + C3H3O",
    distances = DistanceData(
        distances = {'d12': 1.23646, 'd13': 2.70816, 'd23': 1.48483},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 811,
    label = "C5H6-1 + C4H3 <=> C4H4 + C5H5-1",
    distances = DistanceData(
        distances = {'d12': 1.33942, 'd13': 2.63237, 'd23': 1.3049},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 791,
    label = "C6H11O + C2H4O <=> C6H12O + C2H3O",
    distances = DistanceData(
        distances = {'d12': 1.37417, 'd13': 2.68214, 'd23': 1.31883},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 987,
    label = "C3H3-1 + C3H3O-1 <=> C3H2 + C3H4O-1",
    distances = DistanceData(
        distances = {'d12': 1.29048, 'd13': 2.70823, 'd23': 1.42472},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 854""",
)

entry(
    index = 785,
    label = "C4H7-1 + C5H6 <=> C4H8-1 + C5H5",
    distances = DistanceData(
        distances = {'d12': 1.24707, 'd13': 2.73212, 'd23': 1.49367},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 829,
    label = "C2H + C3H8 <=> C2H2 + C3H7",
    distances = DistanceData(
        distances = {'d12': 1.1247, 'd13': 2.854, 'd23': 1.76717},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 749,
    label = "C2H5O-1 + HO2 <=> C2H6O-1 + O2",
    distances = DistanceData(
        distances = {'d12': 1.08298, 'd13': 2.6123, 'd23': 1.53916},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1014,
    label = "C2H6O-1 + C6H11O <=> C6H12O + C2H5O-1",
    distances = DistanceData(
        distances = {'d12': 1.28226, 'd13': 2.70645, 'd23': 1.43343},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 833""",
)

entry(
    index = 1101,
    label = "CH3-1 + C3H3O-1 <=> C3H4O-1 + CH2",
    distances = DistanceData(
        distances = {'d12': 1.2591, 'd13': 2.73884, 'd23': 1.48009},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 765""",
)

entry(
    index = 771,
    label = "C2HO-1 + H <=> H2 + C2O",
    distances = DistanceData(
        distances = {'d12': 1.25756, 'd13': 2.22931, 'd23': 0.998142},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1115,
    label = "C2H2 + C4H9 <=> C4H10 + C2H",
    distances = DistanceData(
        distances = {'d12': 1.12575, 'd13': 2.85671, 'd23': 1.77057},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 940""",
)

entry(
    index = 1062,
    label = "C4H6 + C4H9 <=> C4H10 + C4H5",
    distances = DistanceData(
        distances = {'d12': 1.27659, 'd13': 2.67701, 'd23': 1.40569},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 908""",
)

entry(
    index = 859,
    label = "C5H6-1 + C2HO <=> C2H2O + C5H5-1",
    distances = DistanceData(
        distances = {'d12': 1.38366, 'd13': 2.63338, 'd23': 1.25087},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 940,
    label = "C4H10 + C2H <=> C2H2 + C4H9",
    distances = DistanceData(
        distances = {'d12': 1.12575, 'd13': 2.85671, 'd23': 1.77057},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 798,
    label = "C2O + C4H8O3 <=> C2HO-1 + C4H7O3",
    distances = DistanceData(
        distances = {'d12': 1.29824, 'd13': 2.44224, 'd23': 1.22384},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 861,
    label = "C4H7-1 + C3H4 <=> C4H8-1 + C3H3",
    distances = DistanceData(
        distances = {'d12': 1.30055, 'd13': 2.66745, 'd23': 1.3757},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1197,
    label = "C2H2O + C2H5 <=> C2HO + C2H6",
    distances = DistanceData(
        distances = {'d12': 1.26738, 'd13': 2.62923, 'd23': 1.36841},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 831""",
)

entry(
    index = 1015,
    label = "C6H6 + C2HO <=> C2H2O + C6H5",
    distances = DistanceData(
        distances = {'d12': 1.27346, 'd13': 2.6232, 'd23': 1.35092},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 920""",
)

entry(
    index = 1040,
    label = "HO-1 + C3H2 <=> C3H3-1 + O",
    distances = DistanceData(
        distances = {'d12': 1.24201, 'd13': 2.49561, 'd23': 1.2536},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 813""",
)

entry(
    index = 837,
    label = "CH3O + C3H4 <=> CH4O + C3H3",
    distances = DistanceData(
        distances = {'d12': 1.35448, 'd13': 2.64694, 'd23': 1.33566},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 933,
    label = "C3H4O + C2H5O-1 <=> C2H6O-1 + C3H3O",
    distances = DistanceData(
        distances = {'d12': 1.27855, 'd13': 2.69884, 'd23': 1.43642},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1001,
    label = "C2H4 + C2H3O <=> C2H4O + C2H3",
    distances = DistanceData(
        distances = {'d12': 1.24746, 'd13': 2.69391, 'd23': 1.458},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 849""",
)

entry(
    index = 1123,
    label = "C4H10 + CH3O <=> C4H9 + CH4O",
    distances = DistanceData(
        distances = {'d12': 1.31649, 'd13': 2.69835, 'd23': 1.39228},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 913""",
)

entry(
    index = 923,
    label = "C4H10 + C2H3 <=> C2H4 + C4H9",
    distances = DistanceData(
        distances = {'d12': 1.28393, 'd13': 2.68344, 'd23': 1.40156},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 847,
    label = "C4H8 + CHO <=> CH2O + C4H7",
    distances = DistanceData(
        distances = {'d12': 1.34691, 'd13': 2.72011, 'd23': 1.38629},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 958,
    label = "C2H3O + C6H8-2 <=> C2H4O + C6H7-2",
    distances = DistanceData(
        distances = {'d12': 1.26746, 'd13': 2.71432, 'd23': 1.46173},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1039,
    label = "H2 + C6H11O <=> C6H12O + H",
    distances = DistanceData(
        distances = {'d12': 1.25894, 'd13': 2.2779, 'd23': 1.02314},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 927""",
)

entry(
    index = 1133,
    label = "C4H8-1 + C4H7 <=> C4H7-1 + C4H8",
    distances = DistanceData(
        distances = {'d12': 1.26395, 'd13': 2.70656, 'd23': 1.4483},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 956""",
)

entry(
    index = 857,
    label = "C5H5-1 + C2H4O <=> C5H6-1 + C2H3O",
    distances = DistanceData(
        distances = {'d12': 1.227, 'd13': 2.70108, 'd23': 1.48813},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 818,
    label = "C6H8-1 + CH3 <=> CH4 + C6H7-1",
    distances = DistanceData(
        distances = {'d12': 1.24498, 'd13': 2.70693, 'd23': 1.46572},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 756,
    label = "C4H10 + HO <=> H2O + C4H9",
    distances = DistanceData(
        distances = {'d12': 1.16316, 'd13': 2.5778, 'd23': 1.42849},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1199,
    label = "CH4 + C4H3-1 <=> CH3 + C4H4-1",
    distances = DistanceData(
        distances = {'d12': 1.3021, 'd13': 2.66512, 'd23': 1.36509},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 758""",
)

entry(
    index = 1049,
    label = "C2H2 + C6H7-2 <=> C2H + C6H8-2",
    distances = DistanceData(
        distances = {'d12': 1.11789, 'd13': 2.95802, 'd23': 1.92812},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 875""",
)

entry(
    index = 740,
    label = "C4H8 + C4H3 <=> C4H4 + C4H7",
    distances = DistanceData(
        distances = {'d12': 1.20907, 'd13': 2.7289, 'd23': 1.52599},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1071,
    label = "CH4O + C4H7 <=> C4H8 + CH3O",
    distances = DistanceData(
        distances = {'d12': 1.3051, 'd13': 2.69432, 'd23': 1.40875},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 778""",
)

entry(
    index = 1027,
    label = "C2H4 + C6H11O <=> C6H12O + C2H3",
    distances = DistanceData(
        distances = {'d12': 1.23336, 'd13': 2.70964, 'd23': 1.48512},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 752""",
)

entry(
    index = 905,
    label = "C4H6O + C3H7-1 <=> C3H8-1 + C4H5O",
    distances = DistanceData(
        distances = {'d12': 1.31482, 'd13': 2.70454, 'd23': 1.39366},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1148,
    label = "H2 + C7H13O3-2 <=> C7H14O3-2 + H",
    distances = DistanceData(
        distances = {'d12': 1.23924, 'd13': 2.28474, 'd23': 1.05547},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 893""",
)

entry(
    index = 1057,
    label = "C2H6O-1 + C4H7-1 <=> C4H8-1 + C2H5O-1",
    distances = DistanceData(
        distances = {'d12': 1.33993, 'd13': 2.68325, 'd23': 1.34623},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 753""",
)

entry(
    index = 975,
    label = "C2O + C7H14O <=> C2HO-1 + C7H13O",
    distances = DistanceData(
        distances = {'d12': 1.29402, 'd13': 2.65919, 'd23': 1.37455},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1152,
    label = "C2H6O + C4H5O <=> C4H6O + C2H5O",
    distances = DistanceData(
        distances = {'d12': 1.35348, 'd13': 2.68208, 'd23': 1.36598},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 910""",
)

entry(
    index = 1047,
    label = "C5H6-1 + C4H5-1 <=> C5H5-1 + C4H6-1",
    distances = DistanceData(
        distances = {'d12': 1.25326, 'd13': 2.67051, 'd23': 1.41772},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 763""",
)

entry(
    index = 1008,
    label = "C2H2 + C6H7-3 <=> C2H + C6H8-3",
    distances = DistanceData(
        distances = {'d12': 1.12015, 'd13': 2.88828, 'd23': 1.81999},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 822""",
)

entry(
    index = 1124,
    label = "C6H6 + C2H5O-1 <=> C2H6O-1 + C6H5",
    distances = DistanceData(
        distances = {'d12': 1.27191, 'd13': 2.66815, 'd23': 1.41251},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 890""",
)

entry(
    index = 884,
    label = "C4H6O + C4H3-1 <=> C4H4-1 + C4H5O",
    distances = DistanceData(
        distances = {'d12': 1.28004, 'd13': 2.70043, 'd23': 1.42978},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 995,
    label = "H2 + C7H13O3-3 <=> C7H14O3-3 + H",
    distances = DistanceData(
        distances = {'d12': 1.37479, 'd13': 2.28497, 'd23': 0.910186},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 745""",
)

entry(
    index = 1187,
    label = "C3H4O-1 + C2H3O-1 <=> C2H4O-1 + C3H3O-1",
    distances = DistanceData(
        distances = {'d12': 1.38531, 'd13': 2.7684, 'd23': 1.39267},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 960""",
)

entry(
    index = 892,
    label = "C6H5 + C3H8-1 <=> C6H6 + C3H7-1",
    distances = DistanceData(
        distances = {'d12': 1.24668, 'd13': 2.68706, 'd23': 1.44809},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 989,
    label = "C4H10 + O2 <=> C4H9 + HO2",
    distances = DistanceData(
        distances = {'d12': 1.07128, 'd13': 2.63224, 'd23': 1.56784},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 795""",
)

entry(
    index = 766,
    label = "C4H6 + C2H <=> C2H2 + C4H5",
    distances = DistanceData(
        distances = {'d12': 1.14543, 'd13': 2.74504, 'd23': 1.60344},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 973,
    label = "H + C5H8-1 <=> H2 + C5H7-1",
    distances = DistanceData(
        distances = {'d12': 1.21574, 'd13': 2.33091, 'd23': 1.11688},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1192,
    label = "C2H2 + C4H5 <=> C4H6 + C2H",
    distances = DistanceData(
        distances = {'d12': 1.14543, 'd13': 2.74504, 'd23': 1.60344},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 766""",
)

entry(
    index = 1179,
    label = "C3H8-1 + C3H3O <=> C3H4O + C3H7-1",
    distances = DistanceData(
        distances = {'d12': 1.3154, 'd13': 2.68928, 'd23': 1.38695},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 867""",
)

entry(
    index = 962,
    label = "C6H5 + C3H8 <=> C6H6 + C3H7",
    distances = DistanceData(
        distances = {'d12': 1.26734, 'd13': 2.68016, 'd23': 1.41706},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1141,
    label = "C2H6O-2 + O2 <=> C2H5O-2 + HO2",
    distances = DistanceData(
        distances = {'d12': 1.01926, 'd13': 2.52174, 'd23': 1.52675},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 858""",
)

entry(
    index = 1201,
    label = "C3H6O + CHO <=> C3H5O + CH2O",
    distances = DistanceData(
        distances = {'d12': 1.31083, 'd13': 2.72403, 'd23': 1.4195},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 929""",
)

entry(
    index = 1094,
    label = "C3H6-1 + C4H7-1 <=> C4H8-1 + C3H5-1",
    distances = DistanceData(
        distances = {'d12': 1.28375, 'd13': 2.67551, 'd23': 1.39697},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 793""",
)

entry(
    index = 1196,
    label = "C6H6 + C4H7-1 <=> C4H8-1 + C6H5",
    distances = DistanceData(
        distances = {'d12': 1.26992, 'd13': 2.67805, 'd23': 1.4125},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 810""",
)

entry(
    index = 1082,
    label = "CH3-1 + C4H7-1 <=> C4H8-1 + CH2",
    distances = DistanceData(
        distances = {'d12': 1.29871, 'd13': 2.65801, 'd23': 1.36436},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 835""",
)

entry(
    index = 947,
    label = "C4H5 + C2H6O <=> C4H6 + C2H5O",
    distances = DistanceData(
        distances = {'d12': 1.24174, 'd13': 2.70502, 'd23': 1.48068},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 815,
    label = "C4H10 + C3H7 <=> C3H8 + C4H9",
    distances = DistanceData(
        distances = {'d12': 1.34357, 'd13': 2.68932, 'd23': 1.34993},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 862,
    label = "C6H12O + HO <=> H2O + C6H11O",
    distances = DistanceData(
        distances = {'d12': 1.18121, 'd13': 2.50415, 'd23': 1.36928},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 781,
    label = "C2H4O-1 + C2H3 <=> C2H4 + C2H3O-1",
    distances = DistanceData(
        distances = {'d12': 1.2334, 'd13': 2.75993, 'd23': 1.53124},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 825,
    label = "C4H4-1 + O <=> HO-1 + C4H3-1",
    distances = DistanceData(
        distances = {'d12': 1.27336, 'd13': 2.48545, 'd23': 1.22055},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 878,
    label = "C4H3 + C4H8O3 <=> C4H4 + C4H7O3",
    distances = DistanceData(
        distances = {'d12': 1.14021, 'd13': 2.50003, 'd23': 1.36034},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1105,
    label = "C6H12O + O2 <=> C6H11O + HO2",
    distances = DistanceData(
        distances = {'d12': 1.1049, 'd13': 2.59673, 'd23': 1.50072},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 819""",
)

entry(
    index = 1111,
    label = "C2H2O + C5H5-1 <=> C5H6-1 + C2HO",
    distances = DistanceData(
        distances = {'d12': 1.38366, 'd13': 2.63338, 'd23': 1.25087},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 859""",
)

entry(
    index = 761,
    label = "C4H6O + C2H5 <=> C2H6 + C4H5O",
    distances = DistanceData(
        distances = {'d12': 1.29624, 'd13': 2.7028, 'd23': 1.41609},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1166,
    label = "C2H4 + C2HO <=> C2H2O + C2H3",
    distances = DistanceData(
        distances = {'d12': 1.2934, 'd13': 2.61734, 'd23': 1.32838},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 918""",
)

entry(
    index = 865,
    label = "C4H9 + H2O2 <=> C4H10 + HO2-1",
    distances = DistanceData(
        distances = {'d12': 1.18443, 'd13': 2.51157, 'd23': 1.32976},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1170,
    label = "C3H6-1 + C3H7-1 <=> C3H5-1 + C3H8-1",
    distances = DistanceData(
        distances = {'d12': 1.25402, 'd13': 2.68374, 'd23': 1.43673},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 746""",
)

entry(
    index = 871,
    label = "C6H8-3 + C3H7-1 <=> C3H8-1 + C6H7-3",
    distances = DistanceData(
        distances = {'d12': 1.25999, 'd13': 2.72483, 'd23': 1.46614},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1146,
    label = "C6H6 + C2H3O <=> C2H4O + C6H5",
    distances = DistanceData(
        distances = {'d12': 1.23714, 'd13': 2.70344, 'd23': 1.47425},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 866""",
)

entry(
    index = 937,
    label = "H2O2 + C3H3-2 <=> C3H4-1 + HO2-1",
    distances = DistanceData(
        distances = {'d12': 1.19369, 'd13': 2.5118, 'd23': 1.33001},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1005,
    label = "CH4O + C3H3O <=> C3H4O + CH3O",
    distances = DistanceData(
        distances = {'d12': 1.3388, 'd13': 2.67854, 'd23': 1.37393},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 814""",
)

entry(
    index = 1072,
    label = "C3H6O + HO2-1 <=> C3H5O + H2O2",
    distances = DistanceData(
        distances = {'d12': 1.18004, 'd13': 2.50468, 'd23': 1.33384},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 812""",
)

entry(
    index = 927,
    label = "C6H12O + H <=> H2 + C6H11O",
    distances = DistanceData(
        distances = {'d12': 1.25894, 'd13': 2.2779, 'd23': 1.02314},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 843,
    label = "CH3O + C5H8 <=> CH4O + C5H7",
    distances = DistanceData(
        distances = {'d12': 1.30583, 'd13': 2.68, 'd23': 1.41848},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1035,
    label = "C2H4 + C5H7-1 <=> C2H3 + C5H8-1",
    distances = DistanceData(
        distances = {'d12': 1.21856, 'd13': 2.739, 'd23': 1.52394},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 803""",
)

entry(
    index = 739,
    label = "C6H12O + C2O <=> C2HO-1 + C6H11O",
    distances = DistanceData(
        distances = {'d12': 1.3268, 'd13': 2.65341, 'd23': 1.34368},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 802,
    label = "C7H14O3-4 + H <=> H2 + C7H13O3-4",
    distances = DistanceData(
        distances = {'d12': 1.12442, 'd13': 2.11848, 'd23': 0.995758},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 853,
    label = "C3H3-1 + H <=> H2 + C3H2",
    distances = DistanceData(
        distances = {'d12': 1.29695, 'd13': 2.25538, 'd23': 0.958432},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 998,
    label = "C4H10 + HO2-1 <=> C4H9 + H2O2",
    distances = DistanceData(
        distances = {'d12': 1.18443, 'd13': 2.51157, 'd23': 1.32976},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 865""",
)

entry(
    index = 917,
    label = "C4H5-1 + C2H6 <=> C4H6-1 + C2H5",
    distances = DistanceData(
        distances = {'d12': 1.33514, 'd13': 2.67222, 'd23': 1.33881},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 796,
    label = "C2HO-1 + C2H5O-1 <=> C2H6O-1 + C2O",
    distances = DistanceData(
        distances = {'d12': 1.27603, 'd13': 2.65577, 'd23': 1.39236},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 982,
    label = "HO-1 + C4H3-1 <=> C4H4-1 + O",
    distances = DistanceData(
        distances = {'d12': 1.27336, 'd13': 2.48545, 'd23': 1.22055},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 825""",
)

entry(
    index = 744,
    label = "C3H7 + C5H8-1 <=> C3H8 + C5H7-1",
    distances = DistanceData(
        distances = {'d12': 1.24145, 'd13': 2.74478, 'd23': 1.50625},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1102,
    label = "C2H2 + C3H7 <=> C2H + C3H8",
    distances = DistanceData(
        distances = {'d12': 1.1247, 'd13': 2.854, 'd23': 1.76717},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 829""",
)

entry(
    index = 772,
    label = "C2O + C5H8-1 <=> C2HO-1 + C5H7-1",
    distances = DistanceData(
        distances = {'d12': 1.27178, 'd13': 2.68587, 'd23': 1.43053},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 957,
    label = "C6H8-1 + HO2-1 <=> H2O2 + C6H7-1",
    distances = DistanceData(
        distances = {'d12': 1.26672, 'd13': 2.52787, 'd23': 1.2669},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1061,
    label = "C2H6O-2 + C6H7-3 <=> C2H5O-2 + C6H8-3",
    distances = DistanceData(
        distances = {'d12': 1.16827, 'd13': 2.60362, 'd23': 1.47037},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 925""",
)

entry(
    index = 768,
    label = "C4H8-1 + CH3 <=> CH4 + C4H7-1",
    distances = DistanceData(
        distances = {'d12': 1.31658, 'd13': 2.68174, 'd23': 1.36865},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1180,
    label = "C6H6 + C3H7-1 <=> C6H5 + C3H8-1",
    distances = DistanceData(
        distances = {'d12': 1.24668, 'd13': 2.68706, 'd23': 1.44809},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 892""",
)

entry(
    index = 909,
    label = "C4H8-1 + C4H5 <=> C4H6 + C4H7-1",
    distances = DistanceData(
        distances = {'d12': 1.28012, 'd13': 2.67229, 'd23': 1.40053},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1053,
    label = "C2H6O-1 + C5H5-1 <=> C5H6-1 + C2H5O-1",
    distances = DistanceData(
        distances = {'d12': 1.43422, 'd13': 2.67314, 'd23': 1.25801},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 830""",
)

entry(
    index = 1012,
    label = "H2 + C3H2 <=> C3H3-1 + H",
    distances = DistanceData(
        distances = {'d12': 1.29695, 'd13': 2.25538, 'd23': 0.958432},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 853""",
)

entry(
    index = 1156,
    label = "C4H4-1 + C5H7-1 <=> C4H3-1 + C5H8-1",
    distances = DistanceData(
        distances = {'d12': 1.24544, 'd13': 2.71399, 'd23': 1.47544},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 934""",
)

entry(
    index = 1043,
    label = "C4H8-1 + C3H2 <=> C4H7-1 + C3H3-1",
    distances = DistanceData(
        distances = {'d12': 1.31227, 'd13': 2.65729, 'd23': 1.3528},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 820""",
)

entry(
    index = 930,
    label = "H + C3H4-1 <=> H2 + C3H3-2",
    distances = DistanceData(
        distances = {'d12': 1.28684, 'd13': 2.27534, 'd23': 0.989057},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 832,
    label = "C4H8-1 + H <=> H2 + C4H7-1",
    distances = DistanceData(
        distances = {'d12': 1.35991, 'd13': 2.27964, 'd23': 0.922801},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 965,
    label = "C7H14O + O <=> HO-1 + C7H13O",
    distances = DistanceData(
        distances = {'d12': 1.25832, 'd13': 2.50711, 'd23': 1.24903},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1120,
    label = "C3H4-1 + HO2-1 <=> H2O2 + C3H3-2",
    distances = DistanceData(
        distances = {'d12': 1.19369, 'd13': 2.5118, 'd23': 1.33001},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 937""",
)

entry(
    index = 844,
    label = "C7H13O + HO2 <=> C7H14O + O2",
    distances = DistanceData(
        distances = {'d12': 1.12823, 'd13': 2.57092, 'd23': 1.46156},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1136,
    label = "C3H6O + C4H5O <=> C3H5O + C4H6O",
    distances = DistanceData(
        distances = {'d12': 1.31514, 'd13': 2.69186, 'd23': 1.40066},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 852""",
)

entry(
    index = 888,
    label = "C3H4O + C4H3-1 <=> C4H4-1 + C3H3O",
    distances = DistanceData(
        distances = {'d12': 1.27723, 'd13': 2.69438, 'd23': 1.42433},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 991,
    label = "C2H6O + C5H7-1 <=> C2H5O + C5H8-1",
    distances = DistanceData(
        distances = {'d12': 1.28329, 'd13': 2.70711, 'd23': 1.45592},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 898""",
)

entry(
    index = 896,
    label = "C4H10 + C4H3-1 <=> C4H4-1 + C4H9",
    distances = DistanceData(
        distances = {'d12': 1.33552, 'd13': 2.66325, 'd23': 1.33444},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1193,
    label = "C6H6 + C4H3-2 <=> C6H5 + C4H4-2",
    distances = DistanceData(
        distances = {'d12': 1.24513, 'd13': 2.67111, 'd23': 1.43661},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 800""",
)

entry(
    index = 753,
    label = "C4H8-1 + C2H5O-1 <=> C2H6O-1 + C4H7-1",
    distances = DistanceData(
        distances = {'d12': 1.33993, 'd13': 2.68325, 'd23': 1.34623},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 978,
    label = "C2H6O-2 + C5H7-1 <=> C2H5O-2 + C5H8-1",
    distances = DistanceData(
        distances = {'d12': 1.18827, 'd13': 2.59176, 'd23': 1.41159},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 838""",
)

entry(
    index = 743,
    label = "C4H5 + H2O2 <=> C4H6 + HO2-1",
    distances = DistanceData(
        distances = {'d12': 1.10753, 'd13': 2.50949, 'd23': 1.41137},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1022,
    label = "H2O + CHO <=> CH2O + HO",
    distances = DistanceData(
        distances = {'d12': 1.14261, 'd13': 2.69644, 'd23': 1.5699},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 777""",
)

entry(
    index = 900,
    label = "C2O + C3H8 <=> C2HO-1 + C3H7",
    distances = DistanceData(
        distances = {'d12': 1.3731, 'd13': 2.6576, 'd23': 1.29024},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1054,
    label = "C4H4-1 + C4H9 <=> C4H10 + C4H3-1",
    distances = DistanceData(
        distances = {'d12': 1.33552, 'd13': 2.66325, 'd23': 1.33444},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 896""",
)

entry(
    index = 1098,
    label = "C2H4 + C4H3-2 <=> C2H3 + C4H4-2",
    distances = DistanceData(
        distances = {'d12': 1.25669, 'd13': 2.6645, 'd23': 1.42124},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 779""",
)

entry(
    index = 939,
    label = "C2O + C4H4-2 <=> C2HO-1 + C4H3-2",
    distances = DistanceData(
        distances = {'d12': 1.33539, 'd13': 2.65038, 'd23': 1.32523},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1086,
    label = "C2HO-1 + C6H7 <=> C2O + C6H8",
    distances = DistanceData(
        distances = {'d12': 1.28566, 'd13': 2.66596, 'd23': 1.41018},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 941""",
)

entry(
    index = 776,
    label = "C5H6 + CH3O <=> CH4O + C5H5",
    distances = DistanceData(
        distances = {'d12': 1.27671, 'd13': 2.7273, 'd23': 1.46189},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 881,
    label = "C4H9 + C2H6O <=> C4H10 + C2H5O",
    distances = DistanceData(
        distances = {'d12': 1.30948, 'd13': 2.71554, 'd23': 1.41318},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 996,
    label = "C2HO-1 + C6H7-3 <=> C2O + C6H8-3",
    distances = DistanceData(
        distances = {'d12': 1.27451, 'd13': 2.69334, 'd23': 1.43806},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 809""",
)

entry(
    index = 1189,
    label = "C2HO-1 + C3H5O <=> C3H6O + C2O",
    distances = DistanceData(
        distances = {'d12': 1.37633, 'd13': 2.64671, 'd23': 1.29438},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 921""",
)

entry(
    index = 821,
    label = "C2O + C4H6O3 <=> C2HO-1 + C4H5O3",
    distances = DistanceData(
        distances = {'d12': 1.29547, 'd13': 2.44288, 'd23': 1.22556},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 874,
    label = "C2O + C6H8-2 <=> C2HO-1 + C6H7-2",
    distances = DistanceData(
        distances = {'d12': 1.26308, 'd13': 2.68515, 'd23': 1.44379},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1109,
    label = "C3H6 + C6H7-1 <=> C6H8-1 + C3H5",
    distances = DistanceData(
        distances = {'d12': 1.34303, 'd13': 2.69934, 'd23': 1.36251},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 755""",
)

entry(
    index = 779,
    label = "C2H3 + C4H4-2 <=> C2H4 + C4H3-2",
    distances = DistanceData(
        distances = {'d12': 1.25669, 'd13': 2.6645, 'd23': 1.42124},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 765,
    label = "C3H4O-1 + CH2 <=> CH3-1 + C3H3O-1",
    distances = DistanceData(
        distances = {'d12': 1.2591, 'd13': 2.73884, 'd23': 1.48009},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1203,
    label = "C2H6O-1 + C4H7O3 <=> C2H5O-1 + C4H8O3",
    distances = DistanceData(
        distances = {'d12': 1.21026, 'd13': 2.49975, 'd23': 1.30339},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 970""",
)

entry(
    index = 1174,
    label = "C2HO-1 + C7H13O <=> C2O + C7H14O",
    distances = DistanceData(
        distances = {'d12': 1.29402, 'd13': 2.65919, 'd23': 1.37455},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 975""",
)

entry(
    index = 1142,
    label = "C3H8 + C3H7-1 <=> C3H8-1 + C3H7",
    distances = DistanceData(
        distances = {'d12': 1.31982, 'd13': 2.69065, 'd23': 1.37102},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 943""",
)

entry(
    index = 1091,
    label = "C2HO-1 + C7H13O-1 <=> C2O + C7H14O-1",
    distances = DistanceData(
        distances = {'d12': 1.39483, 'd13': 2.65039, 'd23': 1.27497},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 805""",
)

entry(
    index = 950,
    label = "C7H14O3-5 + H <=> H2 + C7H13O3-5",
    distances = DistanceData(
        distances = {'d12': 1.25835, 'd13': 2.26959, 'd23': 1.02105},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1031,
    label = "C2H4O-1 + C6H7-1 <=> C2H3O-1 + C6H8-1",
    distances = DistanceData(
        distances = {'d12': 1.35993, 'd13': 2.69198, 'd23': 1.36847},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 887""",
)

entry(
    index = 806,
    label = "CH3 + C3H4O-1 <=> CH4 + C3H3O-1",
    distances = DistanceData(
        distances = {'d12': 1.27053, 'd13': 2.74347, 'd23': 1.47295},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 913,
    label = "C4H9 + CH4O <=> C4H10 + CH3O",
    distances = DistanceData(
        distances = {'d12': 1.31649, 'd13': 2.69835, 'd23': 1.39228},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 792,
    label = "C4H7-1 + C3H4-1 <=> C4H8-1 + C3H3-2",
    distances = DistanceData(
        distances = {'d12': 1.30241, 'd13': 2.6941, 'd23': 1.39855},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 810,
    label = "C4H8-1 + C6H5 <=> C6H6 + C4H7-1",
    distances = DistanceData(
        distances = {'d12': 1.26992, 'd13': 2.67805, 'd23': 1.4125},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 986,
    label = "CH3-1 + C2H5 <=> C2H6 + CH2",
    distances = DistanceData(
        distances = {'d12': 1.29393, 'd13': 2.65751, 'd23': 1.36785},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 916""",
)

entry(
    index = 826,
    label = "C5H8 + C3H7-1 <=> C3H8-1 + C5H7",
    distances = DistanceData(
        distances = {'d12': 1.28345, 'd13': 2.69893, 'd23': 1.4242},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 784,
    label = "CH4O + C4H5-1 <=> C4H6-1 + CH3O",
    distances = DistanceData(
        distances = {'d12': 1.27312, 'd13': 2.70184, 'd23': 1.43129},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 748,
    label = "C4H9 + C3H8-1 <=> C4H10 + C3H7-1",
    distances = DistanceData(
        distances = {'d12': 1.31707, 'd13': 2.68611, 'd23': 1.37457},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1106,
    label = "C4H4-2 + C3H3 <=> C3H4 + C4H3-2",
    distances = DistanceData(
        distances = {'d12': 1.33324, 'd13': 2.66168, 'd23': 1.33955},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 894""",
)

entry(
    index = 1151,
    label = "C4H6 + C4H7 <=> C4H8 + C4H5",
    distances = DistanceData(
        distances = {'d12': 1.22111, 'd13': 2.71297, 'd23': 1.50812},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 807""",
)

entry(
    index = 1114,
    label = "C4H10 + C2H5 <=> C4H9 + C2H6",
    distances = DistanceData(
        distances = {'d12': 1.34613, 'd13': 2.69062, 'd23': 1.34864},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 741""",
)

entry(
    index = 1210,
    label = "C3H6 + C6H7-2 <=> C6H8-2 + C3H5",
    distances = DistanceData(
        distances = {'d12': 1.30176, 'd13': 2.70556, 'd23': 1.41366},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 876""",
)

entry(
    index = 858,
    label = "C2H5O-2 + HO2 <=> C2H6O-2 + O2",
    distances = DistanceData(
        distances = {'d12': 1.01926, 'd13': 2.52174, 'd23': 1.52675},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 943,
    label = "C3H8-1 + C3H7 <=> C3H8 + C3H7-1",
    distances = DistanceData(
        distances = {'d12': 1.31982, 'd13': 2.69065, 'd23': 1.37102},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 769,
    label = "C7H14O3-1 + H <=> H2 + C7H13O3-1",
    distances = DistanceData(
        distances = {'d12': 1.1136, 'd13': 2.12218, 'd23': 1.01225},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1163,
    label = "C5H6-1 + C4H7 <=> C5H5-1 + C4H8",
    distances = DistanceData(
        distances = {'d12': 1.20054, 'd13': 2.73647, 'd23': 1.54533},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 767""",
)

entry(
    index = 799,
    label = "C2HO + C5H8 <=> C2H2O + C5H7",
    distances = DistanceData(
        distances = {'d12': 1.20374, 'd13': 2.69602, 'd23': 1.50184},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 866,
    label = "C2H4O + C6H5 <=> C6H6 + C2H3O",
    distances = DistanceData(
        distances = {'d12': 1.23714, 'd13': 2.70344, 'd23': 1.47425},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1173,
    label = "C7H14O + O2 <=> C7H13O + HO2",
    distances = DistanceData(
        distances = {'d12': 1.12823, 'd13': 2.57092, 'd23': 1.46156},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 844""",
)

entry(
    index = 1016,
    label = "C2H6O-1 + C5H7-1 <=> C2H5O-1 + C5H8-1",
    distances = DistanceData(
        distances = {'d12': 1.24491, 'd13': 2.73182, 'd23': 1.4955},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 966""",
)

entry(
    index = 934,
    label = "C4H3-1 + C5H8-1 <=> C4H4-1 + C5H7-1",
    distances = DistanceData(
        distances = {'d12': 1.24544, 'd13': 2.71399, 'd23': 1.47544},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 836,
    label = "C2O + C6H8-1 <=> C2HO-1 + C6H7-1",
    distances = DistanceData(
        distances = {'d12': 1.30356, 'd13': 2.65764, 'd23': 1.373},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 961,
    label = "C5H5-1 + C3H3-1 <=> C5H6-1 + C3H2",
    distances = DistanceData(
        distances = {'d12': 1.22321, 'd13': 2.67029, 'd23': 1.45619},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1000,
    label = "CH4 + C2H5 <=> CH3 + C2H6",
    distances = DistanceData(
        distances = {'d12': 1.3078, 'd13': 2.67929, 'd23': 1.37491},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 775""",
)

entry(
    index = 840,
    label = "C5H8 + CH3 <=> CH4 + C5H7",
    distances = DistanceData(
        distances = {'d12': 1.24875, 'd13': 2.722, 'd23': 1.47417},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 922,
    label = "C4H7-1 + C2H4O-1 <=> C4H8-1 + C2H3O-1",
    distances = DistanceData(
        distances = {'d12': 1.28931, 'd13': 2.71038, 'd23': 1.45617},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 959,
    label = "C3H3O + C3H4 <=> C3H4O + C3H3",
    distances = DistanceData(
        distances = {'d12': 1.38164, 'd13': 2.68056, 'd23': 1.31356},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1132,
    label = "C3H6-2 + C2H5O-1 <=> C2H6O-1 + C3H5-2",
    distances = DistanceData(
        distances = {'d12': 1.31549, 'd13': 2.67588, 'd23': 1.36225},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 764""",
)

entry(
    index = 1183,
    label = "C5H6 + C5H7 <=> C5H5 + C5H8",
    distances = DistanceData(
        distances = {'d12': 1.38704, 'd13': 2.73712, 'd23': 1.35364},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 944""",
)

entry(
    index = 918,
    label = "C2H2O + C2H3 <=> C2H4 + C2HO",
    distances = DistanceData(
        distances = {'d12': 1.2934, 'd13': 2.61734, 'd23': 1.32838},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 856,
    label = "C7H13O-1 + C2H6 <=> C7H14O-1 + C2H5",
    distances = DistanceData(
        distances = {'d12': 1.33239, 'd13': 2.67842, 'd23': 1.35237},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1129,
    label = "C3H8-1 + C5H7 <=> C5H8 + C3H7-1",
    distances = DistanceData(
        distances = {'d12': 1.28345, 'd13': 2.69893, 'd23': 1.4242},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 826""",
)

entry(
    index = 981,
    label = "C2H4 + C2H3O-1 <=> C2H4O-1 + C2H3",
    distances = DistanceData(
        distances = {'d12': 1.2334, 'd13': 2.75993, 'd23': 1.53124},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 781""",
)

entry(
    index = 757,
    label = "C3H6O + C3H2 <=> C3H3-1 + C3H5O",
    distances = DistanceData(
        distances = {'d12': 1.32513, 'd13': 2.66456, 'd23': 1.34118},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 747,
    label = "C2H5O-2 + C2H6O-1 <=> C2H6O-2 + C2H5O-1",
    distances = DistanceData(
        distances = {'d12': 1.25129, 'd13': 2.49822, 'd23': 1.25191},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1212,
    label = "CH3-1 + C4H9 <=> C4H10 + CH2",
    distances = DistanceData(
        distances = {'d12': 1.30064, 'd13': 2.66707, 'd23': 1.36853},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 951""",
)

entry(
    index = 1076,
    label = "C2H6O-1 + C6H7-1 <=> C2H5O-1 + C6H8-1",
    distances = DistanceData(
        distances = {'d12': 1.26231, 'd13': 2.69766, 'd23': 1.4453},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 762""",
)

entry(
    index = 777,
    label = "CH2O + HO <=> H2O + CHO",
    distances = DistanceData(
        distances = {'d12': 1.14261, 'd13': 2.69644, 'd23': 1.5699},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1026,
    label = "C4H6 + HO2-1 <=> C4H5 + H2O2",
    distances = DistanceData(
        distances = {'d12': 1.10753, 'd13': 2.50949, 'd23': 1.41137},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 743""",
)

entry(
    index = 1162,
    label = "CH4 + C3H2 <=> C3H3-1 + CH3",
    distances = DistanceData(
        distances = {'d12': 1.28156, 'd13': 2.66668, 'd23': 1.38512},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 954""",
)

entry(
    index = 904,
    label = "CH4O + C4H7O3 <=> C4H8O3 + CH3O",
    distances = DistanceData(
        distances = {'d12': 1.2397, 'd13': 2.54065, 'd23': 1.31272},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1149,
    label = "C2H4O + C3H3O <=> C3H4O + C2H3O",
    distances = DistanceData(
        distances = {'d12': 1.32553, 'd13': 2.69973, 'd23': 1.38253},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 827""",
)

entry(
    index = 1050,
    label = "C4H4-1 + C3H3O <=> C3H4O + C4H3-1",
    distances = DistanceData(
        distances = {'d12': 1.27723, 'd13': 2.69438, 'd23': 1.42433},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 888""",
)

entry(
    index = 976,
    label = "C4H6 + C2H5O <=> C4H5 + C2H6O",
    distances = DistanceData(
        distances = {'d12': 1.24174, 'd13': 2.70502, 'd23': 1.48068},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 947""",
)

entry(
    index = 1155,
    label = "H2O + C4H7-1 <=> C4H8-1 + HO",
    distances = DistanceData(
        distances = {'d12': 1.17855, 'd13': 2.53153, 'd23': 1.38018},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 895""",
)

entry(
    index = 1046,
    label = "CH4 + C4H5-1 <=> C4H6-1 + CH3",
    distances = DistanceData(
        distances = {'d12': 1.31088, 'd13': 2.67032, 'd23': 1.36145},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 787""",
)

entry(
    index = 831,
    label = "C2HO + C2H6 <=> C2H2O + C2H5",
    distances = DistanceData(
        distances = {'d12': 1.26738, 'd13': 2.62923, 'd23': 1.36841},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1125,
    label = "C4H8-1 + C3H3-2 <=> C4H7-1 + C3H4-1",
    distances = DistanceData(
        distances = {'d12': 1.30241, 'd13': 2.6941, 'd23': 1.39855},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 792""",
)

entry(
    index = 929,
    label = "C3H5O + CH2O <=> C3H6O + CHO",
    distances = DistanceData(
        distances = {'d12': 1.31083, 'd13': 2.72403, 'd23': 1.4195},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1208,
    label = "C5H6-1 + C2H3O-1 <=> C5H5-1 + C2H4O-1",
    distances = DistanceData(
        distances = {'d12': 1.21204, 'd13': 2.75883, 'd23': 1.56594},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 891""",
)

entry(
    index = 1139,
    label = "CH4 + C5H7 <=> C5H8 + CH3",
    distances = DistanceData(
        distances = {'d12': 1.24875, 'd13': 2.722, 'd23': 1.47417},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 840""",
)

entry(
    index = 808,
    label = "C4H8 + C3H7 <=> C3H8 + C4H7",
    distances = DistanceData(
        distances = {'d12': 1.27256, 'd13': 2.71035, 'd23': 1.44138},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 885,
    label = "C4H10 + CH3 <=> CH4 + C4H9",
    distances = DistanceData(
        distances = {'d12': 1.31259, 'd13': 2.68284, 'd23': 1.3725},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 992,
    label = "C3H3-1 + C2H5O <=> C2H6O + C3H2",
    distances = DistanceData(
        distances = {'d12': 1.30123, 'd13': 2.65081, 'd23': 1.38924},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 759""",
)

entry(
    index = 1184,
    label = "C2HO-1 + C2H5O <=> C2O + C2H6O",
    distances = DistanceData(
        distances = {'d12': 1.31682, 'd13': 2.65929, 'd23': 1.35739},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 839""",
)

entry(
    index = 891,
    label = "C5H5-1 + C2H4O-1 <=> C5H6-1 + C2H3O-1",
    distances = DistanceData(
        distances = {'d12': 1.21204, 'd13': 2.75883, 'd23': 1.56594},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 988,
    label = "C4H4 + C6H7 <=> C6H8 + C4H3",
    distances = DistanceData(
        distances = {'d12': 1.19794, 'd13': 2.75226, 'd23': 1.55714},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 936""",
)

entry(
    index = 750,
    label = "C5H5-1 + C3H4O <=> C5H6-1 + C3H3O",
    distances = DistanceData(
        distances = {'d12': 1.21568, 'd13': 2.72718, 'd23': 1.51387},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1119,
    label = "C4H6 + C5H5 <=> C5H6 + C4H5",
    distances = DistanceData(
        distances = {'d12': 1.21437, 'd13': 2.7376, 'd23': 1.53766},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 877""",
)

entry(
    index = 1207,
    label = "C6H6 + C4H3-1 <=> C6H5 + C4H4-1",
    distances = DistanceData(
        distances = {'d12': 1.25933, 'd13': 2.66027, 'd23': 1.40789},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 969""",
)

entry(
    index = 953,
    label = "CH4O + C2HO <=> C2H2O + CH3O",
    distances = DistanceData(
        distances = {'d12': 1.22102, 'd13': 2.65835, 'd23': 1.45614},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1178,
    label = "C4H4-1 + C6H7 <=> C6H8 + C4H3-1",
    distances = DistanceData(
        distances = {'d12': 1.25175, 'd13': 2.69783, 'd23': 1.45755},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 901""",
)

entry(
    index = 1021,
    label = "C3H8 + C5H7-1 <=> C3H7 + C5H8-1",
    distances = DistanceData(
        distances = {'d12': 1.24145, 'd13': 2.74478, 'd23': 1.50625},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 744""",
)

entry(
    index = 1018,
    label = "C4H4 + C5H5-1 <=> C5H6-1 + C4H3",
    distances = DistanceData(
        distances = {'d12': 1.33942, 'd13': 2.63237, 'd23': 1.3049},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 811""",
)

entry(
    index = 1095,
    label = "C2H6O-2 + C3H2 <=> C2H5O-2 + C3H3-1",
    distances = DistanceData(
        distances = {'d12': 1.23187, 'd13': 2.48503, 'd23': 1.26673},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 932""",
)

entry(
    index = 1164,
    label = "C4H8-1 + C2H3O-1 <=> C4H7-1 + C2H4O-1",
    distances = DistanceData(
        distances = {'d12': 1.28931, 'd13': 2.71038, 'd23': 1.45617},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 922""",
)

entry(
    index = 1127,
    label = "C3H6-2 + C2H3O <=> C2H4O + C3H5-2",
    distances = DistanceData(
        distances = {'d12': 1.26576, 'd13': 2.69421, 'd23': 1.434},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 882""",
)

entry(
    index = 1081,
    label = "C4H10 + CHO <=> C4H9 + CH2O",
    distances = DistanceData(
        distances = {'d12': 1.29256, 'd13': 2.71979, 'd23': 1.44608},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 770""",
)

entry(
    index = 814,
    label = "C3H4O + CH3O <=> CH4O + C3H3O",
    distances = DistanceData(
        distances = {'d12': 1.3388, 'd13': 2.67854, 'd23': 1.37393},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 863,
    label = "C4H7-1 + CH4O <=> C4H8-1 + CH3O",
    distances = DistanceData(
        distances = {'d12': 1.3149, 'd13': 2.69717, 'd23': 1.39395},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 822,
    label = "C2H + C6H8-3 <=> C2H2 + C6H7-3",
    distances = DistanceData(
        distances = {'d12': 1.12015, 'd13': 2.88828, 'd23': 1.81999},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 780,
    label = "C4H9 + C2H4O <=> C4H10 + C2H3O",
    distances = DistanceData(
        distances = {'d12': 1.29263, 'd13': 2.69713, 'd23': 1.40578},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1110,
    label = "C2H6O-2 + C2O <=> C2HO-1 + C2H5O-2",
    distances = DistanceData(
        distances = {'d12': 1.20931, 'd13': 2.42545, 'd23': 1.29442},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 968""",
)

entry(
    index = 760,
    label = "C3H3-1 + C3H5-2 <=> C3H6-2 + C3H2",
    distances = DistanceData(
        distances = {'d12': 1.2802, 'd13': 2.65511, 'd23': 1.37946},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1167,
    label = "C7H14O-1 + C2H5 <=> C7H13O-1 + C2H6",
    distances = DistanceData(
        distances = {'d12': 1.33239, 'd13': 2.67842, 'd23': 1.35237},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 856""",
)

entry(
    index = 1177,
    label = "C2H4 + C4H9 <=> C4H10 + C2H3",
    distances = DistanceData(
        distances = {'d12': 1.28393, 'd13': 2.68344, 'd23': 1.40156},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 923""",
)

entry(
    index = 789,
    label = "C5H5-1 + C2H6O <=> C5H6-1 + C2H5O",
    distances = DistanceData(
        distances = {'d12': 1.21749, 'd13': 2.70768, 'd23': 1.51119},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 870,
    label = "C6H6 + C4H3 <=> C4H4 + C6H5",
    distances = DistanceData(
        distances = {'d12': 1.31609, 'd13': 2.63793, 'd23': 1.3296},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1147,
    label = "C2H6O-2 + C2H5O-1 <=> C2H5O-2 + C2H6O-1",
    distances = DistanceData(
        distances = {'d12': 1.25129, 'd13': 2.49822, 'd23': 1.25191},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 747""",
)

entry(
    index = 1004,
    label = "H2 + C7H13O3-1 <=> C7H14O3-1 + H",
    distances = DistanceData(
        distances = {'d12': 1.1136, 'd13': 2.12218, 'd23': 1.01225},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 769""",
)

entry(
    index = 1073,
    label = "C4H8-1 + C3H7 <=> C4H7-1 + C3H8",
    distances = DistanceData(
        distances = {'d12': 1.34046, 'd13': 2.68402, 'd23': 1.34671},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 964""",
)

entry(
    index = 926,
    label = "C5H5-1 + C3H4O-1 <=> C5H6-1 + C3H3O-1",
    distances = DistanceData(
        distances = {'d12': 1.21228, 'd13': 2.77185, 'd23': 1.56487},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1032,
    label = "C4H6 + C4H7-1 <=> C4H8-1 + C4H5",
    distances = DistanceData(
        distances = {'d12': 1.28012, 'd13': 2.67229, 'd23': 1.40053},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 909""",
)

entry(
    index = 803,
    label = "C2H3 + C5H8-1 <=> C2H4 + C5H7-1",
    distances = DistanceData(
        distances = {'d12': 1.21856, 'd13': 2.739, 'd23': 1.52394},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 914,
    label = "C5H6 + C3H3 <=> C3H4 + C5H5",
    distances = DistanceData(
        distances = {'d12': 1.28818, 'd13': 2.71621, 'd23': 1.43215},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 852,
    label = "C3H5O + C4H6O <=> C3H6O + C4H5O",
    distances = DistanceData(
        distances = {'d12': 1.31514, 'd13': 2.69186, 'd23': 1.40066},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 949,
    label = "CH2O + H <=> H2 + CHO",
    distances = DistanceData(
        distances = {'d12': 1.26516, 'd13': 2.33001, 'd23': 1.06488},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 999,
    label = "C5H6-1 + C2H3O <=> C5H5-1 + C2H4O",
    distances = DistanceData(
        distances = {'d12': 1.227, 'd13': 2.70108, 'd23': 1.48813},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 857""",
)

entry(
    index = 813,
    label = "C3H3-1 + O <=> HO-1 + C3H2",
    distances = DistanceData(
        distances = {'d12': 1.24201, 'd13': 2.49561, 'd23': 1.2536},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 797,
    label = "C2H6O-1 + C2H3 <=> C2H4 + C2H5O-1",
    distances = DistanceData(
        distances = {'d12': 1.28725, 'd13': 2.66941, 'd23': 1.38918},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 868,
    label = "C3H5 + C5H8-1 <=> C3H6 + C5H7-1",
    distances = DistanceData(
        distances = {'d12': 1.3087, 'd13': 2.70951, 'd23': 1.40551},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 985,
    label = "C3H4 + C4H7 <=> C4H8 + C3H3",
    distances = DistanceData(
        distances = {'d12': 1.28656, 'd13': 2.68616, 'd23': 1.4021},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 801""",
)

entry(
    index = 787,
    label = "C4H6-1 + CH3 <=> CH4 + C4H5-1",
    distances = DistanceData(
        distances = {'d12': 1.31088, 'd13': 2.67032, 'd23': 1.36145},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1103,
    label = "C2H6O-1 + O2 <=> C2H5O-1 + HO2",
    distances = DistanceData(
        distances = {'d12': 1.08298, 'd13': 2.6123, 'd23': 1.53916},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 749""",
)

entry(
    index = 773,
    label = "C2O + CH4O <=> C2HO-1 + CH3O",
    distances = DistanceData(
        distances = {'d12': 1.33986, 'd13': 2.66562, 'd23': 1.33683},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 954,
    label = "C3H3-1 + CH3 <=> CH4 + C3H2",
    distances = DistanceData(
        distances = {'d12': 1.28156, 'd13': 2.66668, 'd23': 1.38512},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1060,
    label = "C2H6O-2 + C2H5 <=> C2H5O-2 + C2H6",
    distances = DistanceData(
        distances = {'d12': 1.23808, 'd13': 2.50752, 'd23': 1.27554},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 946""",
)

entry(
    index = 946,
    label = "C2H5O-2 + C2H6 <=> C2H6O-2 + C2H5",
    distances = DistanceData(
        distances = {'d12': 1.23808, 'd13': 2.50752, 'd23': 1.27554},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 960,
    label = "C2H4O-1 + C3H3O-1 <=> C3H4O-1 + C2H3O-1",
    distances = DistanceData(
        distances = {'d12': 1.38531, 'd13': 2.7684, 'd23': 1.39267},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 908,
    label = "C4H10 + C4H5 <=> C4H6 + C4H9",
    distances = DistanceData(
        distances = {'d12': 1.27659, 'd13': 2.67701, 'd23': 1.40569},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1195,
    label = "H2 + C5H7-1 <=> H + C5H8-1",
    distances = DistanceData(
        distances = {'d12': 1.21574, 'd13': 2.33091, 'd23': 1.11688},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 973""",
)

entry(
    index = 972,
    label = "C2H5O-2 + C4H4-2 <=> C2H6O-2 + C4H3-2",
    distances = DistanceData(
        distances = {'d12': 1.22479, 'd13': 2.4977, 'd23': 1.28802},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1013,
    label = "C4H6-1 + C2H5 <=> C4H5-1 + C2H6",
    distances = DistanceData(
        distances = {'d12': 1.33514, 'd13': 2.67222, 'd23': 1.33881},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 917""",
)

entry(
    index = 1042,
    label = "C3H6 + C5H7-1 <=> C3H5 + C5H8-1",
    distances = DistanceData(
        distances = {'d12': 1.3087, 'd13': 2.70951, 'd23': 1.40551},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 868""",
)

entry(
    index = 1059,
    label = "C3H6O + C6H7-2 <=> C3H5O + C6H8-2",
    distances = DistanceData(
        distances = {'d12': 1.26035, 'd13': 2.72489, 'd23': 1.46951},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 880""",
)

entry(
    index = 835,
    label = "C4H8-1 + CH2 <=> CH3-1 + C4H7-1",
    distances = DistanceData(
        distances = {'d12': 1.29871, 'd13': 2.65801, 'd23': 1.36436},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 931,
    label = "C2H4O-1 + C6H5 <=> C6H6 + C2H3O-1",
    distances = DistanceData(
        distances = {'d12': 1.22745, 'd13': 2.74998, 'd23': 1.53858},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 964,
    label = "C4H7-1 + C3H8 <=> C4H8-1 + C3H7",
    distances = DistanceData(
        distances = {'d12': 1.34046, 'd13': 2.68402, 'd23': 1.34671},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1121,
    label = "C2HO-1 + C6H7-1 <=> C2O + C6H8-1",
    distances = DistanceData(
        distances = {'d12': 1.30356, 'd13': 2.65764, 'd23': 1.373},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 836""",
)

entry(
    index = 1078,
    label = "C2H6O-2 + C3H3O-1 <=> C2H5O-2 + C3H4O-1",
    distances = DistanceData(
        distances = {'d12': 1.1924, 'd13': 2.55699, 'd23': 1.38954},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 889""",
)

entry(
    index = 845,
    label = "C2O + C7H14O3-4 <=> C2HO-1 + C7H13O3-4",
    distances = DistanceData(
        distances = {'d12': 1.1624, 'd13': 2.45359, 'd23': 1.34106},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1135,
    label = "C4H10 + C3H7-1 <=> C4H9 + C3H8-1",
    distances = DistanceData(
        distances = {'d12': 1.31707, 'd13': 2.68611, 'd23': 1.37457},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 748""",
)

entry(
    index = 889,
    label = "C2H5O-2 + C3H4O-1 <=> C2H6O-2 + C3H3O-1",
    distances = DistanceData(
        distances = {'d12': 1.1924, 'd13': 2.55699, 'd23': 1.38954},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 895,
    label = "C4H8-1 + HO <=> H2O + C4H7-1",
    distances = DistanceData(
        distances = {'d12': 1.17855, 'd13': 2.53153, 'd23': 1.38018},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 754,
    label = "CH4O + C4H5O3 <=> C4H6O3 + CH3O",
    distances = DistanceData(
        distances = {'d12': 1.23697, 'd13': 2.5442, 'd23': 1.31812},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 979,
    label = "H2O + C6H11O <=> C6H12O + HO",
    distances = DistanceData(
        distances = {'d12': 1.18121, 'd13': 2.50415, 'd23': 1.36928},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 862""",
)

entry(
    index = 742,
    label = "C5H6 + C3H5-2 <=> C3H6-2 + C5H5",
    distances = DistanceData(
        distances = {'d12': 1.2249, 'd13': 2.73975, 'd23': 1.52504},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1204,
    label = "C4H8-1 + C5H5 <=> C4H7-1 + C5H6",
    distances = DistanceData(
        distances = {'d12': 1.24707, 'd13': 2.73212, 'd23': 1.49367},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 785""",
)

entry(
    index = 1025,
    label = "C5H6-1 + C2H5O <=> C5H5-1 + C2H6O",
    distances = DistanceData(
        distances = {'d12': 1.21749, 'd13': 2.70768, 'd23': 1.51119},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 789""",
)

entry(
    index = 903,
    label = "C4H8 + C2H5O-1 <=> C2H6O-1 + C4H7",
    distances = DistanceData(
        distances = {'d12': 1.26366, 'd13': 2.71186, 'd23': 1.45239},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1055,
    label = "C3H4O-1 + C6H7 <=> C6H8 + C3H3O-1",
    distances = DistanceData(
        distances = {'d12': 1.32693, 'd13': 2.72644, 'd23': 1.40764},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 788""",
)

entry(
    index = 1099,
    label = "C3H8 + C4H7 <=> C4H8 + C3H7",
    distances = DistanceData(
        distances = {'d12': 1.27256, 'd13': 2.71035, 'd23': 1.44138},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 808""",
)

entry(
    index = 1085,
    label = "CH4O + C5H5 <=> C5H6 + CH3O",
    distances = DistanceData(
        distances = {'d12': 1.27671, 'd13': 2.7273, 'd23': 1.46189},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 776""",
)

entry(
    index = 882,
    label = "C2H4O + C3H5-2 <=> C3H6-2 + C2H3O",
    distances = DistanceData(
        distances = {'d12': 1.26576, 'd13': 2.69421, 'd23': 1.434},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 997,
    label = "C4H8-1 + C4H5-1 <=> C4H7-1 + C4H6-1",
    distances = DistanceData(
        distances = {'d12': 1.38408, 'd13': 2.6733, 'd23': 1.29385},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 879""",
)

entry(
    index = 1181,
    label = "CH3-1 + C3H5 <=> C3H6 + CH2",
    distances = DistanceData(
        distances = {'d12': 1.25295, 'd13': 2.69011, 'd23': 1.43716},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 902""",
)

entry(
    index = 877,
    label = "C5H6 + C4H5 <=> C4H6 + C5H5",
    distances = DistanceData(
        distances = {'d12': 1.21437, 'd13': 2.7376, 'd23': 1.53766},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 764,
    label = "C2H6O-1 + C3H5-2 <=> C3H6-2 + C2H5O-1",
    distances = DistanceData(
        distances = {'d12': 1.31549, 'd13': 2.67588, 'd23': 1.36225},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1202,
    label = "H2 + C2O <=> C2HO-1 + H",
    distances = DistanceData(
        distances = {'d12': 1.25756, 'd13': 2.22931, 'd23': 0.998142},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 771""",
)

entry(
    index = 1158,
    label = "C5H6-1 + C3H2 <=> C5H5-1 + C3H3-1",
    distances = DistanceData(
        distances = {'d12': 1.22321, 'd13': 2.67029, 'd23': 1.45619},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 961""",
)

entry(
    index = 1143,
    label = "C2H2O + CH3O <=> CH4O + C2HO",
    distances = DistanceData(
        distances = {'d12': 1.22102, 'd13': 2.65835, 'd23': 1.45614},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 953""",
)

entry(
    index = 1092,
    label = "C2HO-1 + C4H7 <=> C4H8 + C2O",
    distances = DistanceData(
        distances = {'d12': 1.2934, 'd13': 2.67343, 'd23': 1.38322},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 912""",
)

entry(
    index = 1067,
    label = "C2H6O-2 + C4H3-2 <=> C2H5O-2 + C4H4-2",
    distances = DistanceData(
        distances = {'d12': 1.22479, 'd13': 2.4977, 'd23': 1.28802},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 972""",
)

entry(
    index = 807,
    label = "C4H8 + C4H5 <=> C4H6 + C4H7",
    distances = DistanceData(
        distances = {'d12': 1.22111, 'd13': 2.71297, 'd23': 1.50812},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 910,
    label = "C4H6O + C2H5O <=> C2H6O + C4H5O",
    distances = DistanceData(
        distances = {'d12': 1.35348, 'd13': 2.68208, 'd23': 1.36598},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 945,
    label = "H + C4H8O3 <=> H2 + C4H7O3",
    distances = DistanceData(
        distances = {'d12': 1.17526, 'd13': 2.10644, 'd23': 0.933968},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 817,
    label = "C3H3O-1 + C5H8-1 <=> C3H4O-1 + C5H7-1",
    distances = DistanceData(
        distances = {'d12': 1.31213, 'd13': 2.75581, 'd23': 1.4517},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 793,
    label = "C4H8-1 + C3H5-1 <=> C3H6-1 + C4H7-1",
    distances = DistanceData(
        distances = {'d12': 1.28375, 'd13': 2.67551, 'd23': 1.39697},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 783,
    label = "C3H5O + HO2 <=> C3H6O + O2",
    distances = DistanceData(
        distances = {'d12': 1.07958, 'd13': 2.60996, 'd23': 1.54151},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 827,
    label = "C3H4O + C2H3O <=> C2H4O + C3H3O",
    distances = DistanceData(
        distances = {'d12': 1.32553, 'd13': 2.69973, 'd23': 1.38253},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1188,
    label = "C4H10 + C2H5O <=> C4H9 + C2H6O",
    distances = DistanceData(
        distances = {'d12': 1.30948, 'd13': 2.71554, 'd23': 1.41318},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 881""",
)

entry(
    index = 1064,
    label = "C4H6 + C3H3O-1 <=> C4H5 + C3H4O-1",
    distances = DistanceData(
        distances = {'d12': 1.23749, 'd13': 2.76161, 'd23': 1.52791},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 851""",
)

entry(
    index = 1107,
    label = "C2H6 + C6H7 <=> C6H8 + C2H5",
    distances = DistanceData(
        distances = {'d12': 1.26228, 'd13': 2.7051, 'd23': 1.45857},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 907""",
)

entry(
    index = 1117,
    label = "C3H4O-1 + C5H7-1 <=> C3H3O-1 + C5H8-1",
    distances = DistanceData(
        distances = {'d12': 1.31213, 'd13': 2.75581, 'd23': 1.4517},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 817""",
)

entry(
    index = 1211,
    label = "C5H6-1 + C3H3O <=> C5H5-1 + C3H4O",
    distances = DistanceData(
        distances = {'d12': 1.21568, 'd13': 2.72718, 'd23': 1.51387},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 750""",
)

entry(
    index = 942,
    label = "C2H6O-1 + CH2 <=> CH3-1 + C2H5O-1",
    distances = DistanceData(
        distances = {'d12': 1.29952, 'd13': 2.65527, 'd23': 1.36789},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 867,
    label = "C3H4O + C3H7-1 <=> C3H8-1 + C3H3O",
    distances = DistanceData(
        distances = {'d12': 1.3154, 'd13': 2.68928, 'd23': 1.38695},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1172,
    label = "C3H3-1 + C3H5O <=> C3H6O + C3H2",
    distances = DistanceData(
        distances = {'d12': 1.32513, 'd13': 2.66456, 'd23': 1.34118},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 757""",
)

entry(
    index = 1017,
    label = "C3H6O + O2 <=> C3H5O + HO2",
    distances = DistanceData(
        distances = {'d12': 1.07958, 'd13': 2.60996, 'd23': 1.54151},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 783""",
)

entry(
    index = 839,
    label = "C2O + C2H6O <=> C2HO-1 + C2H5O",
    distances = DistanceData(
        distances = {'d12': 1.31682, 'd13': 2.65929, 'd23': 1.35739},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1200,
    label = "C6H6 + C3H7 <=> C6H5 + C3H8",
    distances = DistanceData(
        distances = {'d12': 1.26734, 'd13': 2.68016, 'd23': 1.41706},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 962""",
)

entry(
    index = 935,
    label = "C4H6O + CH3O <=> CH4O + C4H5O",
    distances = DistanceData(
        distances = {'d12': 1.33432, 'd13': 2.70859, 'd23': 1.38363},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1007,
    label = "C4H6-1 + C2H3O-1 <=> C2H4O-1 + C4H5-1",
    distances = DistanceData(
        distances = {'d12': 1.29795, 'd13': 2.70193, 'd23': 1.42844},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 842""",
)

entry(
    index = 921,
    label = "C3H6O + C2O <=> C2HO-1 + C3H5O",
    distances = DistanceData(
        distances = {'d12': 1.37633, 'd13': 2.64671, 'd23': 1.29438},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 841,
    label = "HO2-1 + C5H8-1 <=> H2O2 + C5H7-1",
    distances = DistanceData(
        distances = {'d12': 1.2596, 'd13': 2.54094, 'd23': 1.29536},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1037,
    label = "C3H6 + CHO <=> CH2O + C3H5",
    distances = DistanceData(
        distances = {'d12': 1.36139, 'd13': 2.73144, 'd23': 1.37055},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 846""",
)

entry(
    index = 1131,
    label = "C2H4O + C6H7-2 <=> C2H3O + C6H8-2",
    distances = DistanceData(
        distances = {'d12': 1.26746, 'd13': 2.71432, 'd23': 1.46173},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 958""",
)

entry(
    index = 800,
    label = "C6H5 + C4H4-2 <=> C6H6 + C4H3-2",
    distances = DistanceData(
        distances = {'d12': 1.24513, 'd13': 2.67111, 'd23': 1.43661},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 855,
    label = "C4H10 + C3H5-2 <=> C3H6-2 + C4H9",
    distances = DistanceData(
        distances = {'d12': 1.311, 'd13': 2.67475, 'd23': 1.36923},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 919,
    label = "C5H5 + HO2 <=> C5H6 + O2",
    distances = DistanceData(
        distances = {'d12': 1.1551, 'd13': 2.61984, 'd23': 1.4756},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 794,
    label = "C2HO-1 + C3H5-2 <=> C3H6-2 + C2O",
    distances = DistanceData(
        distances = {'d12': 1.24881, 'd13': 2.65744, 'd23': 1.41691},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 899,
    label = "C4H9 + C3H4-1 <=> C4H10 + C3H3-2",
    distances = DistanceData(
        distances = {'d12': 1.30166, 'd13': 2.69315, 'd23': 1.39287},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 980,
    label = "C4H6-1 + CH3O <=> CH4O + C4H5-1",
    distances = DistanceData(
        distances = {'d12': 1.27312, 'd13': 2.70184, 'd23': 1.43129},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 784""",
)

entry(
    index = 758,
    label = "CH3 + C4H4-1 <=> CH4 + C4H3-1",
    distances = DistanceData(
        distances = {'d12': 1.3021, 'd13': 2.66512, 'd23': 1.36509},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 746,
    label = "C3H5-1 + C3H8-1 <=> C3H6-1 + C3H7-1",
    distances = DistanceData(
        distances = {'d12': 1.25402, 'd13': 2.68374, 'd23': 1.43673},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 969,
    label = "C6H5 + C4H4-1 <=> C6H6 + C4H3-1",
    distances = DistanceData(
        distances = {'d12': 1.25933, 'd13': 2.66027, 'd23': 1.40789},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 1077,
    label = "C2H6 + C3H5O <=> C3H6O + C2H5",
    distances = DistanceData(
        distances = {'d12': 1.3031, 'd13': 2.68154, 'd23': 1.38809},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""Reverse reaction for reaction index 824""",
)

entry(
    index = 848,
    label = "C4H10 + C2H5O-2 <=> C2H6O-2 + C4H9",
    distances = DistanceData(
        distances = {'d12': 1.23896, 'd13': 2.51204, 'd23': 1.27424},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

entry(
    index = 951,
    label = "C4H10 + CH2 <=> CH3-1 + C4H9",
    distances = DistanceData(
        distances = {'d12': 1.30064, 'd13': 2.66707, 'd23': 1.36853},
        method = 'm062x/6-311+g(2df,2p)',
    ),
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
)

