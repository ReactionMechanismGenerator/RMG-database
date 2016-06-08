#!/usr/bin/env python
# encoding: utf-8

name = "Solvent Descriptors"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "water",
    molecule = "O",
    solvent = SolventData(
        s_g = 2.743,
        b_g = 4.814,
        e_g = 0.822,
        l_g = -0.213,
        a_g = 3.904,
        c_g = -1.271,
        s_h = 2.836,
        b_h = -41.816,
        e_h = 9.91,
        l_h = -6.354,
        a_h = -32.01,
        c_h = -13.31,
        A = -52.843,
        B = 3703.6,
        C = 5.866,
        D = -5.88e-29,
        E = 10,
        alpha = 0.353,
        beta = 0.38,
        eps = 80.4,
    ),
    shortDesc = u""" """,
    longDesc =
u"""

""",
)

entry(
    index = 2,
    label = "1-octanol",
    molecule = "CCCCCCCCO",
    solvent = SolventData(
        s_g = 0.56,
        b_g = 0.702,
        e_g = -0.203,
        l_g = 0.939,
        a_g = 3.56,
        c_g = -0.12,
        s_h = 5.89,
        b_h = -8.99,
        e_h = -1.04,
        l_h = -9.18,
        a_h = -53.99,
        c_h = -6.49,
        A = -0.022128,
        B = 3018.4,
        C = -2.8054,
        D = 1.3141e-05,
        E = 2,
        alpha = 0.328,
        beta = 0.45,
        eps = 10.3,
    ),
    shortDesc = u""" """,
    longDesc =
u"""
alpha = 0.328, #primary alcohols
beta = 0.45, #primary alcohols,
""",
)

entry(
    index = 3,
    label = "benzene",
    molecule = "C1=CC=CC=C1",
    solvent = SolventData(
        s_g = 1.053,
        b_g = 0.169,
        e_g = -0.313,
        l_g = 1.02,
        a_g = 0.457,
        c_g = 0.107,
        s_h = -12.599,
        b_h = -4.023,
        e_h = 4.446,
        l_h = -8.488,
        a_h = -9.775,
        c_h = -4.637,
        A = 7.5117,
        B = 294.68,
        C = -2.794,
        D = 0,
        E = 0,
        alpha = 0,
        beta = 0.14,
        eps = 2.3,
    ),
    shortDesc = u""" """,
    longDesc =
u"""

""",
)

entry(
    index = 4,
    label = "cyclohexane",
    molecule = "C1CCCCC1",
    solvent = SolventData(
        s_g = 0,
        b_g = 0,
        e_g = -0.11,
        l_g = 1.013,
        a_g = 0,
        c_g = 0.163,
        s_h = 0.0,
        b_h = 0.0,
        e_h = 3.375,
        l_h = -9.078,
        a_h = 0.0,
        c_h = -6.507,
        A = -33.763,
        B = 2497.2,
        C = 3.2236,
        D = 0,
        E = 0,
        alpha = 0,
        beta = 0,
        eps = 2.0,
    ),
    shortDesc = u""" """,
    longDesc =
u"""

""",
)

entry(
    index = 5,
    label = "dibutylether",
    molecule = "CCCCOCCCC",
    solvent = SolventData(
        s_g = 0.026,
        b_g = -0.499,
        e_g = -0.216,
        l_g = 1.124,
        a_g = 2.626,
        c_g = 0.369,
        s_h = -5.105,
        b_h = 0.0,
        e_h = 3.943,
        l_h = -9.325,
        a_h = -33.97,
        c_h = -6.366,
        A = 10.027,
        B = 206,
        C = -3.1607,
        D = 0,
        E = 0,
        alpha = 0,
        beta = 0.45,
        eps = 3.1,
    ),
    shortDesc = u""" """,
    longDesc =
u"""

""",
)

entry(
    index = 6,
    label = "octane",
    molecule = "CCCCCCCC",
    solvent = SolventData(
        s_g = 0,
        b_g = 0,
        e_g = -0.049,
        l_g = 0.967,
        a_g = 0,
        c_g = 0.215,
        s_h = 0.0,
        b_h = 0.0,
        e_h = 2.999,
        l_h = -9.279,
        a_h = 0.0,
        c_h = -6.708,
        A = -98.805,
        B = 3905.5,
        C = 14.103,
        D = -2.5112e-05,
        E = 2,
        alpha = 0,
        beta = 0,
        eps = 2.0,
    ),
    shortDesc = u""" """,
    longDesc =
u"""

""",
)

entry(
    index = 7,
    label = "butanol",
    molecule = "CCCCO",
    solvent = SolventData(
        s_g = 0.539,
        b_g = 0.995,
        e_g = -0.276,
        l_g = 0.934,
        a_g = 3.781,
        c_g = -0.039,
        s_h = 0.0,
        b_h = -4.261,
        e_h = 0.0,
        l_h = -8.507,
        a_h = -50.806,
        c_h = -7.629,
        A = -82.851,
        B = 4481.8,
        C = 11.182,
        D = -2.0943e-05,
        E = 2,
        alpha = 0.37,
        beta = 0.48,
        eps = 17.8,
    ),
    shortDesc = u""" """,
    longDesc =
u"""

""",
)

entry(
    index = 8,
    label = "carbontet",
    molecule = "ClC(Cl)(Cl)Cl",
    solvent = SolventData(
        s_g = 0.46,
        b_g = 0,
        e_g = -0.303,
        l_g = 1.047,
        a_g = 0,
        c_g = 0.282,
        s_h = -4.824,
        b_h = -7.045,
        e_h = 3.517,
        l_h = -8.886,
        a_h = 0.0,
        c_h = -6.441,
        A = -8.0738,
        B = 1121.1,
        C = -0.4726,
        D = 0,
        E = 0,
        alpha = 0,
        beta = 0.05,
        eps = 2.23,
    ),
    shortDesc = u""" """,
    longDesc =
u"""
beta = 0.05, # Note 24 in Snelgrove et al. 2001
""",
)

entry(
    index = 9,
    label = "chloroform",
    molecule = "ClC(Cl)Cl",
    solvent = SolventData(
        s_g = 1.256,
        b_g = 1.37,
        e_g = -0.595,
        l_g = 0.981,
        a_g = 0.28,
        c_g = 0.168,
        s_h = -13.956,
        b_h = -17.334,
        e_h = 8.628,
        l_h = -8.739,
        a_h = -2.712,
        c_h = -6.516,
        A = -14.109,
        B = 1049.2,
        C = 0.5377,
        D = 0,
        E = 0,
        alpha = 0.15,
        beta = 0.02,
        eps = 4.8,
    ),
    shortDesc = u""" """,
    longDesc =
u"""

""",
)

entry(
    index = 10,
    label = "decane",
    molecule = "CCCCCCCCCC",
    solvent = SolventData(
        s_g = 0,
        b_g = 0,
        e_g = -0.143,
        l_g = 0.989,
        a_g = 0,
        c_g = 0.156,
        s_h = 0.0,
        b_h = 0.0,
        e_h = 2.999,
        l_h = -9.279,
        a_h = 0.0,
        c_h = -6.708,
        A = -97.662,
        B = 4342.7,
        C = 13.645,
        D = -1.9319e-05,
        E = 2,
        alpha = 0,
        beta = 0,
        eps = 2.0,
    ),
    shortDesc = u""" """,
    longDesc =
u"""

""",
)

entry(
    index = 11,
    label = "dichloroethane",
    molecule = "CC(Cl)Cl",
    solvent = SolventData(
        s_g = 1.436,
        b_g = 0.736,
        e_g = -0.15,
        l_g = 0.936,
        a_g = 0.649,
        c_g = 0.011,
        s_h = -18.328,
        b_h = -7.101,
        e_h = 5.555,
        l_h = -8.045,
        a_h = -9.599,
        c_h = -2.345,
        A = 15.312,
        B = -41.12,
        C = -3.919,
        D = 0,
        E = 0,
        alpha = 0.1,
        beta = 0.105,
        eps = 10.7,
    ),
    shortDesc = u""" """,
    longDesc =
u"""

""",
)

entry(
    index = 12,
    label = "dimethylformamide",
    molecule = "N(C)(C)C=O",
    solvent = SolventData(
        s_g = 2.315,
        b_g = 0,
        e_g = -0.339,
        l_g = 0.83,
        a_g = 4.112,
        c_g = -0.174,
        s_h = -15.168,
        b_h = -8.253,
        e_h = 0.0,
        l_h = -7.118,
        a_h = -42.211,
        c_h = -4.324,
        A = -20.425,
        B = 1515.5,
        C = 1.4444,
        D = 0,
        E = 0,
        alpha = 0,
        beta = 0.73,
        eps = 36.7,
    ),
    shortDesc = u""" """,
    longDesc =
u"""

""",
)

entry(
    index = 13,
    label = "dimethylsulfoxide",
    molecule = "CS(C)=O",
    solvent = SolventData(
        s_g = 2.89,
        b_g = 0,
        e_g = -0.2,
        l_g = 0.732,
        a_g = 5.46,
        c_g = -0.59,
        s_h = -18.448,
        b_h = -5.861,
        e_h = -0.329,
        l_h = -6.38,
        a_h = -47.419,
        c_h = -2.546,
        A = -37.347,
        B = 2835,
        C = 3.7937,
        D = 0,
        E = 0,
        alpha = 0,
        beta = 0.88,
        eps = 46.7,
    ),
    shortDesc = u""" """,
    longDesc =
u"""
Molecule Search on RMG website cannot draw molecule and says "Invalid adjacency list" although it can give the
adjacency list with the solvent name or its correct SMILES representation
""",
)

entry(
    index = 14,
    label = "dodecane",
    molecule = "CCCCCCCCCCCC",
    solvent = SolventData(
        s_g = 0,
        b_g = 0,
        e_g = 0,
        l_g = 0.986,
        a_g = 0,
        c_g = 0.053,
        s_h = 0.0,
        b_h = 0.0,
        e_h = 2.999,
        l_h = -9.279,
        a_h = 0.0,
        c_h = -6.708,
        A = -134.91,
        B = 6054.2,
        C = 19.337,
        D = -2.443e-05,
        E = 2,
        alpha = 0,
        beta = 0,
        eps = 2.0,
    ),
    shortDesc = u""" """,
    longDesc =
u"""

""",
)

entry(
    index = 15,
    label = "ethanol",
    molecule = "CCO",
    solvent = SolventData(
        s_g = 0.789,
        b_g = 1.311,
        e_g = -0.206,
        l_g = 0.853,
        a_g = 3.635,
        c_g = 0.012,
        s_h = 0.0,
        b_h = -11.899,
        e_h = 0.0,
        l_h = -8.298,
        a_h = -48.6,
        c_h = -6.558,
        A = 7.875,
        B = 781.98,
        C = -3.0418,
        D = 0,
        E = 0,
        alpha = 0.37,
        beta = 0.48,
        eps = 24.3,
    ),
    shortDesc = u""" """,
    longDesc =
u"""

""",
)

entry(
    index = 16,
    label = "heptane",
    molecule = "CCCCCCC",
    solvent = SolventData(
        s_g = 0,
        b_g = 0,
        e_g = -0.162,
        l_g = 0.983,
        a_g = 0,
        c_g = 0.275,
        s_h = 0.0,
        b_h = 0.0,
        e_h = 2.999,
        l_h = -9.279,
        a_h = 0.0,
        c_h = -6.708,
        A = -98.159,
        B = 3592.6,
        C = 14.197,
        D = -2.9555e-05,
        E = 2,
        alpha = 0,
        beta = 0,
        eps = 1.9,
    ),
    shortDesc = u""" """,
    longDesc =
u"""

""",
)

entry(
    index = 17,
    label = "hexadecane",
    molecule = "CCCCCCCCCCCCCCCC",
    solvent = SolventData(
        s_g = 0,
        b_g = 0,
        e_g = 0,
        l_g = 1,
        a_g = 0,
        c_g = 0,
        s_h = 0.0,
        b_h = 0.0,
        e_h = 2.999,
        l_h = -9.279,
        a_h = 0.0,
        c_h = -6.708,
        A = -20.182,
        B = 2203.5,
        C = 1.2289,
        D = 0,
        E = 0,
        alpha = 0,
        beta = 0,
        eps = 2.08,
    ),
    shortDesc = u""" """,
    longDesc =
u"""

""",
)

entry(
    index = 18,
    label = "hexane",
    molecule = "CCCCCC",
    solvent = SolventData(
        s_g = 0,
        b_g = 0,
        e_g = -0.169,
        l_g = 0.979,
        a_g = 0,
        c_g = 0.292,
        s_h = 0.0,
        b_h = 0.0,
        e_h = 2.999,
        l_h = -9.279,
        a_h = 0.0,
        c_h = -6.708,
        A = -56.569,
        B = 2140.5,
        C = 7.5175,
        D = -1.7676e-05,
        E = 2,
        alpha = 0,
        beta = 0,
        eps = 2.0,
    ),
    shortDesc = u""" """,
    longDesc =
u"""

""",
)

entry(
    index = 19,
    label = "isooctane",
    molecule = "CC(C)CC(C)(C)C",
    solvent = SolventData(
        s_g = 0,
        b_g = 0,
        e_g = -0.244,
        l_g = -6.708,
        a_g = 0,
        c_g = 0.275,
        s_h = 0.0,
        b_h = 0.0,
        e_h = 0.0,
        l_h = -9.279,
        a_h = 0.0,
        c_h = 2.999,
        A = -12.928,
        B = 1137.5,
        C = 0.25725,
        D = -3.69e-28,
        E = 10,
        alpha = 0,
        beta = 0,
        eps = 1.94,
    ),
    shortDesc = u""" """,
    longDesc =
u"""

""",
)

entry(
    index = 20,
    label = "nonane",
    molecule = "CCCCCCCCC",
    solvent = SolventData(
        s_g = 0,
        b_g = 0,
        e_g = -0.145,
        l_g = 0.98,
        a_g = 0,
        c_g = 0.2,
        s_h = 0.0,
        b_h = 0.0,
        e_h = 2.999,
        l_h = -9.279,
        a_h = 0.0,
        c_h = -6.708,
        A = -68.54,
        B = 3165.3,
        C = 9.0919,
        D = -1.3519e-05,
        E = 2,
        alpha = 0,
        beta = 0,
        eps = 2.0,
    ),
    shortDesc = u""" """,
    longDesc =
u"""

""",
)

entry(
    index = 21,
    label = "pentane",
    molecule = "CCCCC",
    solvent = SolventData(
        s_g = 0,
        b_g = 0,
        e_g = -0.276,
        l_g = 0.968,
        a_g = 0,
        c_g = 0.335,
        s_h = 0.0,
        b_h = 0.0,
        e_h = 2.999,
        l_h = -9.279,
        a_h = 0.0,
        c_h = -6.708,
        A = -53.509,
        B = 1836.6,
        C = 7.1409,
        D = -1.9627e-05,
        E = 2,
        alpha = 0,
        beta = 0,
        eps = 1.8,
    ),
    shortDesc = u""" """,
    longDesc =
u"""

""",
)

entry(
    index = 22,
    label = "toluene",
    molecule = "CC1C=CC=CC=1",
    solvent = SolventData(
        s_g = 0.938,
        b_g = 0.099,
        e_g = -0.222,
        l_g = 1.012,
        a_g = 0.467,
        c_g = 0.121,
        s_h = -11.339,
        b_h = -6.984,
        e_h = 0.226,
        l_h = -8.272,
        a_h = -2.25,
        c_h = -5.107,
        A = -226.08,
        B = 6805.7,
        C = 37.542,
        D = -0.060853,
        E = 1,
        alpha = 0,
        beta = 0.14,
        eps = 2.2,
    ),
    shortDesc = u""" """,
    longDesc =
u"""
eps = 2.2 # aerage of range 2.0-2.4
""",
)

entry(
    index = 23,
    label = "undecane",
    molecule = "CCCCCCCCCCC",
    solvent = SolventData(
        s_g = 0,
        b_g = 0,
        e_g = 0,
        l_g = 0.971,
        a_g = 0,
        c_g = 0.113,
        s_h = 0.0,
        b_h = 0.0,
        e_h = 2.999,
        l_h = -9.279,
        a_h = 0.0,
        c_h = -6.708,
        A = 52.176,
        B = -4951.9,
        C = -8.5676,
        D = 570980,
        E = -2,
        alpha = 0,
        beta = 0,
        eps = 2.0,
    ),
    shortDesc = u""" """,
    longDesc =
u"""

""",
)

entry(
    index = 24,
    label = "acetonitrile",
    molecule = "CC#N",
    solvent = SolventData(
        s_g = 2.461,
        b_g = 0.418,
        e_g = -0.595,
        l_g = 0.738,
        a_g = 2.085,
        c_g = -0.007,
        s_h = -18.43,
        b_h = -7.535,
        e_h = -3.304,
        l_h = -6.727,
        a_h = -26.104,
        c_h = -4.148,
        A = -10.906,
        B = 872.02,
        C = 0,
        D = 0,
        E = 0,
        alpha = 0.04,
        beta = 0.33,
        eps = 37.5,
    ),
    shortDesc = u""" """,
    longDesc =
u"""

""",
)

entry(
    index = 25,
    label = "ethylacetate",
    molecule = "CCOC(C)=O",
    solvent = SolventData(
        s_g = 1.251,
        b_g = 0,
        e_g = -0.335,
        l_g = 0.917,
        a_g = 2.949,
        c_g = 0.203,
        s_h = -15.141,
        b_h = 0.0,
        e_h = 4.671,
        l_h = -7.691,
        a_h = -28.763,
        c_h = -7.063,
        A = 14.354,
        B = -154.6,
        C = -3.7887,
        D = 0,
        E = 0,
        alpha = 0,
        beta = 0.45,
        eps = 6.0,
    ),
    shortDesc = u""" """,
    longDesc =
u"""

""",
)

