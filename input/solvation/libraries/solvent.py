#!/usr/bin/env python
# encoding: utf-8

name = "Solvent Descriptors"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 1,
    label = "water",
    solvent = SolventData(
        # Abraham solvent descriptors:
        c_g = -1.271,
    	e_g = 0.822,
    	s_g = 2.743,
    	a_g = 3.904,
    	b_g = 4.814,
    	l_g = -0.213,
    	c_h = -13.310,
    	e_h = 9.91,
    	s_h = 2.836,
    	a_h = -32.010,	
    	b_h = -41.816,	
    	l_h = -6.354,
        # Viscosity correlation coefficients:
    	A = -52.843,
    	B = 3703.6,
    	C = 5.866,
    	D = -5.88E-29,
    	E = 10,
        # Abraham SOLUTE descriptors for calculating H-abstraction intrinsic correction
    	alpha = 0.353,
    	beta = 0.38,
        # The dielectric constant
        eps = 80.4
    ),
    shortDesc = u""" """,
    longDesc = 
u"""

"""
)

entry(
    index = 2,
    label = "1-octanol",
    solvent = SolventData(
    	c_g = -0.12,
    	e_g = -0.203,
    	s_g = 0.56,
    	a_g = 3.56,
    	b_g = 0.702,
    	l_g = 0.939,
    	c_h = -6.49,
    	e_h = -1.04,
    	s_h = 5.89,
    	a_h = -53.99,	
    	b_h = -8.99,
    	l_h = -9.18,
    	A = -0.022128,
    	B = 3018.4,
    	C = -2.8054,
    	D = 0.000013141,
    	E = 2,
    	alpha = 0.328, #primary alcohols
    	beta = 0.45, #primary alcohols,
        eps = 10.3
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
alpha = 0.328, #primary alcohols
beta = 0.45, #primary alcohols,
"""
)

entry(
    index = 3,
    label = "benzene",
    solvent = SolventData(
    	c_g = 0.107,
    	e_g = -0.313,
    	s_g = 1.053,
    	a_g = 0.457,
    	b_g = 0.169,
    	l_g = 1.02,
    	c_h = -4.637,
    	e_h = 4.446,
    	s_h = -12.599,
    	a_h = -9.775,	
    	b_h =-4.023,	
    	l_h = -8.488,
    	A = 7.5117,
    	B = 294.68,
    	C = -2.794,
    	D = 0,
    	E = 0,
    	alpha = 0,
    	beta = 0.14,
        eps = 2.3
    ),
    shortDesc = u""" """,
    longDesc = 
u"""

"""
)

entry(
    index = 4,
    label = "cyclohexane",
    solvent = SolventData(
    	c_g = 0.163,
    	e_g = -0.11,
    	s_g = 0,
    	a_g = 0,
    	b_g = 0,
    	l_g = 1.013,
    	c_h = -6.507,
    	e_h = 3.375,
    	s_h = 0.0,
    	a_h = 0.0,
    	b_h = 0.0,	
    	l_h = -9.078,
    	A = -33.763,
    	B = 2497.2,
    	C = 3.2236,
    	D = 0,
    	E = 0,
    	alpha = 0,
    	beta = 0,
        eps = 2.0
    ),
    shortDesc = u""" """,
    longDesc = 
u"""

"""
)

entry(
    index = 5,
    label = "dibutylether",
    solvent = SolventData(
    	c_g = 0.369,
    	e_g = -0.216,
    	s_g = 0.026,
    	a_g = 2.626,
    	b_g = -0.499,
    	l_g = 1.124,
    	c_h = -6.366,
    	e_h = 3.943,
    	s_h = -5.105,
    	a_h = -33.970,	
    	b_h = 0.0,	
    	l_h = -9.325,
    	A = 10.027,
    	B = 206,
    	C = -3.1607,
    	D = 0,
    	E = 0,
    	alpha = 0, 
    	beta = 0.45,
        eps = 3.1
    ),
    shortDesc = u""" """,
    longDesc = 
u"""

"""
)

entry(
    index = 6,
    label = "octane",
    solvent = SolventData(
    	c_g = 0.215,
    	e_g = -0.049,
    	s_g = 0,
    	a_g = 0,
    	b_g = 0,
    	l_g = 0.967,
    	c_h = -6.708,
    	e_h = 2.999,
    	s_h = 0.0,
    	a_h = 0.0,
    	b_h = 0.0,
    	l_h = -9.279,
    	A = -98.805,
    	B = 3905.5,
    	C = 14.103,
    	D = -0.000025112,
    	E = 2,
    	alpha = 0,
    	beta = 0,
        eps = 2.0
    ),
    shortDesc = u""" """,
    longDesc = 
u"""

"""
)

entry(
    index = 7,
    label = "butanol",
    solvent = SolventData(
    	c_g = -0.039,	
    	e_g = -0.276,
    	s_g = 0.539,
    	a_g = 3.781,
    	b_g = 0.995,
    	l_g = 0.934,
    	c_h = -7.629,
    	e_h = 0.0,
    	s_h = 0.0,
    	a_h = -50.806,
    	b_h = -4.261,
    	l_h = -8.507,
    	A = -82.851,
    	B = 4481.8,
    	C = 11.182,
    	D = -0.000020943,
    	E = 2,
    	alpha = 0.37,
    	beta = 0.48,
        eps = 17.8
    ),
    shortDesc = u""" """,
    longDesc = 
u"""

"""
)

entry(
    index = 8,
    label = "carbontet",
    solvent = SolventData(
    	c_g = 0.282,
    	e_g = -0.303,
    	s_g = 0.46,
    	a_g = 0,
    	b_g = 0,
    	l_g = 1.047,
    	c_h = -6.441,
    	e_h = 3.517,
    	s_h = -4.824,
    	a_h = 0.0,
    	b_h = -7.045,
    	l_h = -8.886,
    	A = -8.0738,
    	B = 1121.1,
    	C = -0.4726,
    	D = 0,
    	E = 0,
    	alpha = 0,
    	beta = 0.05, # Note 24 in Snelgrove et al. 2001
        eps = 2.23
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
beta = 0.05, # Note 24 in Snelgrove et al. 2001
"""
)
entry(
    index = 9,
    label = "chloroform",
    solvent = SolventData(
    	c_g = 0.168,
    	e_g = -0.595,
    	s_g = 1.256,
    	a_g = 0.28,
    	b_g = 1.37,
    	l_g = 0.981,
    	c_h = -6.516,
    	e_h = 8.628,
    	s_h = -13.956,
    	a_h = -2.712,
    	b_h = -17.334,
    	l_h = -8.739,
    	A = -14.109,
    	B = 1049.2,
    	C = 0.5377,
    	D = 0,
    	E = 0,
    	alpha = 0.15,
    	beta = 0.02,
        eps = 4.8
    ),
    shortDesc = u""" """,
    longDesc = 
u"""

"""
)
entry(
    index = 10,
    label = "decane",
    solvent = SolventData(
    	c_g = 0.156,
    	e_g = -0.143,
    	s_g = 0,
    	a_g = 0,
    	b_g = 0,
    	l_g = 0.989,
    	c_h = -6.708,
    	e_h = 2.999,
    	s_h = 0.0,
    	a_h = 0.0,
    	b_h = 0.0,
    	l_h = -9.279,
    	A = -97.662,
    	B = 4342.7,
    	C = 13.645,
    	D = -0.000019319,
    	E = 2,
    	alpha = 0,
    	beta = 0,
        eps = 2.0
    ),
    shortDesc = u""" """,
    longDesc = 
u"""

"""
)
entry(
    index = 11,
    label = "dicholorethane",
    solvent = SolventData(
    	c_g = 0.011,
    	e_g = -0.15,
    	s_g = 1.436,
    	a_g = 0.649,
    	b_g = 0.736,
    	l_g = 0.936,
    	c_h = -2.345,
    	e_h = 5.555,
    	s_h = -18.328,
    	a_h = -9.599,
    	b_h = -7.101,
    	l_h = -8.045,
    	A = 15.312,
    	B = -41.12,
    	C = -3.919,
    	D = 0,
    	E = 0,
    	alpha = 0.1,
    	beta = 0.105,
        eps = 10.7
    ),
    shortDesc = u""" """,
    longDesc = 
u"""

"""
)
entry(
    index = 12,
    label = "dimethylformamide",
    solvent = SolventData(
    	c_g = -0.174,
    	e_g = -0.339,
    	s_g = 2.315,
    	a_g = 4.112,
    	b_g = 0,
    	l_g = 0.83,
    	c_h = -4.324,
    	e_h = 0.0,
    	s_h = -15.168,
    	a_h = -42.211,
    	b_h = -8.253,
    	l_h = -7.118,
    	A = -20.425,
    	B = 1515.5,
    	C = 1.4444,
    	D = 0,
    	E = 0,
    	alpha = 0,
    	beta = 0.73,
        eps = 36.7
    ),
    shortDesc = u""" """,
    longDesc = 
u"""

"""
)
entry(
    index = 13,
    label = "dimethylsulfoxide",
    solvent = SolventData(
    	c_g = -0.59,
    	e_g = -0.2,
    	s_g = 2.89,
    	a_g = 5.46,
    	b_g = 0,
    	l_g = 0.732,
    	c_h = -2.546,
    	e_h = -0.329,
    	s_h = -18.448,
    	a_h = -47.419,
    	b_h = -5.861,
    	l_h = -6.38,
    	A = -37.347,
    	B = 2835,
    	C = 3.7937,
    	D = 0,
    	E = 0,
    	alpha = 0,
    	beta = 0.88,
        eps = 46.7
    ),
    shortDesc = u""" """,
    longDesc = 
u"""

"""
)
entry(
    index = 14,
    label = "dodecane",
    solvent = SolventData(
    	c_g = 0.053,
    	e_g = 0,
    	s_g = 0,
    	a_g = 0,
    	b_g = 0,
    	l_g = 0.986,
    	c_h = -6.708,
    	e_h = 2.999,
    	s_h = 0.0,
    	a_h = 0.0,
    	b_h = 0.0,
    	l_h = -9.279,
    	A = -134.91,
    	B = 6054.2,
    	C = 19.337,
    	D = -0.00002443,
    	E = 2,
    	alpha = 0,
    	beta = 0,
        eps = 2.0
    ),
    shortDesc = u""" """,
    longDesc = 
u"""

"""
)
entry(
    index = 15,
    label = "ethanol",
    solvent = SolventData(
    	c_g = 0.012,
    	e_g = -0.206,
    	s_g = 0.789,
    	a_g = 3.635,
    	b_g = 1.311,
    	l_g = 0.853,
    	c_h = -6.558,
    	e_h = 0.0,
    	s_h = 0.0,
    	a_h = -48.600,
    	b_h = -11.899,
    	l_h = -8.298,
    	A = 7.875,
    	B = 781.98,
    	C = -3.0418,
    	D = 0,
    	E = 0,
    	alpha = 0.37,
    	beta = 0.48,
        eps = 24.3
    ),
    shortDesc = u""" """,
    longDesc = 
u"""

"""
)
entry(
    index = 16,
    label = "heptane",
    solvent = SolventData(
    	c_g = 0.275,
    	e_g = -0.162,
    	s_g = 0,
    	a_g = 0,
    	b_g = 0,
    	l_g = 0.983,
    	c_h = -6.708,
    	e_h = 2.999,
    	s_h = 0.0,
    	a_h = 0.0,
    	b_h = 0.0,
    	l_h = -9.279,
    	A = -98.159,
    	B = 3592.6,
    	C = 14.197,
    	D = -0.000029555,
    	E = 2,
    	alpha = 0,
    	beta = 0,
        eps = 1.9
    ),
    shortDesc = u""" """,
    longDesc = 
u"""

"""
)
entry(
    index = 17,
    label = "hexadecane",
    solvent = SolventData(
    	c_g = 0,
    	e_g = 0,
    	s_g = 0,
    	a_g = 0,	
    	b_g = 0,	
    	l_g = 1,
    	c_h = -6.708,
    	e_h = 2.999,
    	s_h = 0.0,
    	a_h = 0.0,
    	b_h = 0.0,
    	l_h = -9.279,
    	A = -20.182,
    	B = 2203.5,
    	C = 1.2289,
    	D = 0,
    	E = 0,
    	alpha = 0,
    	beta = 0,
        eps = 2.08
    ),
    shortDesc = u""" """,
    longDesc = 
u"""

"""
)
entry(
    index = 18,
    label = "hexane",
    solvent = SolventData(
    	c_g = 0.292,
    	e_g = -0.169,
    	s_g = 0,
    	a_g = 0,
    	b_g = 0,
    	l_g = 0.979,
    	c_h = -6.708,
    	e_h = 2.999	,
    	s_h = 0.0	,
    	a_h = 0.0	,
    	b_h = 0.0	,
    	l_h = -9.279,
    	A = -56.569,
    	B = 2140.5,
    	C = 7.5175,
    	D = -0.000017676,
    	E = 2,
    	alpha = 0,
    	beta = 0,
        eps = 2.0
    ),
    shortDesc = u""" """,
    longDesc = 
u"""

"""
)
entry(
    index = 19,
    label = "isooctane",
    solvent = SolventData(
    	c_g = 0.275	,
    	e_g = -0.244,
    	s_g = 0		,
    	a_g = 0		,
    	b_g = 0		,
    	l_g = -6.708,
    	c_h = 2.999	,
    	e_h = 0.0	,
    	s_h = 0.0	,
    	a_h = 0.0	,
    	b_h = 0.0	,
    	l_h = -9.279,
    	A = -12.928,
    	B = 1137.5,
    	C = 0.25725,
    	D = -3.69E-28,
    	E = 10,
    	alpha = 0,
    	beta = 0,
        eps = 1.94
    ),
    shortDesc = u""" """,
    longDesc = 
u"""

"""
)
entry(
    index = 20,
    label = "nonane",
    solvent = SolventData(
    	c_g = 0.2	,
    	e_g = -0.145,
    	s_g = 0		,
    	a_g = 0		,
    	b_g = 0		,
    	l_g = 0.98	,
    	c_h = -6.708,
    	e_h = 2.999	,
    	s_h = 0.0	,
    	a_h = 0.0	,
    	b_h = 0.0	,
    	l_h = -9.279,
    	A = -68.54,
    	B = 3165.3,
    	C = 9.0919,
    	D = -0.000013519,
    	E = 2,
    	alpha = 0,
    	beta = 0,
        eps = 2.0
    ),
    shortDesc = u""" """,
    longDesc = 
u"""

"""
)
entry(
    index = 21,
    label = "pentane",
    solvent = SolventData(
    	c_g = 0.335	,
    	e_g = -0.276,
    	s_g = 0		,
    	a_g = 0		,
    	b_g = 0		,
    	l_g = 0.968	,
    	c_h = -6.708,
    	e_h = 2.999	,
    	s_h = 0.0	,
    	a_h = 0.0	,
    	b_h = 0.0	,
    	l_h = -9.279,
    	A = -53.509,
    	B = 1836.6,
    	C = 7.1409,
    	D = -0.000019627,
    	E = 2,
    	alpha = 0,
    	beta = 0,
        eps = 1.8
    ),
    shortDesc = u""" """,
    longDesc = 
u"""

"""
)
entry(
    index = 22,
    label = "toluene",
    solvent = SolventData(
    	c_g = 0.121	,
    	e_g = -0.222,
    	s_g = 0.938	,
    	a_g = 0.467	,
    	b_g = 0.099	,
    	l_g = 1.012	,
    	c_h = -5.107,
    	e_h = 0.226	,
    	s_h = -11.339,
    	a_h = -2.25	,
    	b_h = -6.984,
    	l_h = -8.272,
    	A = -226.08,
    	B = 6805.7,
    	C = 37.542,
    	D = -0.060853,
    	E = 1,
    	alpha = 0,
    	beta = 0.14,
        eps = 2.2 # aerage of range 2.0-2.4
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
eps = 2.2 # aerage of range 2.0-2.4
"""
)
entry(
    index = 23,
    label = "undecane",
    solvent = SolventData(
    	c_g = 0.113	,
    	e_g = 0		,
    	s_g = 0		,
    	a_g = 0		,
    	b_g = 0		,
    	l_g = 0.971	,
    	c_h = -6.708,
    	e_h = 2.999	,
    	s_h = 0.0	,
    	a_h = 0.0	,
    	b_h = 0.0	,
    	l_h = -9.279,
    	A = 52.176,
    	B = -4951.9,
    	C = -8.5676,
    	D = 570980,
    	E = -2,
    	alpha = 0,
    	beta = 0,
        eps = 2.0
    ),
    shortDesc = u""" """,
    longDesc = 
u"""

"""
)
entry(
    index = 24,
    label = "acetonitrile",
    solvent = SolventData(
    	c_g = -0.007,
    	e_g = -0.595,
    	s_g = 2.461	,
    	a_g = 2.085	,
    	b_g = 0.418	,
    	l_g = 0.738	,
    	c_h = -4.148,
    	e_h = -3.304,
    	s_h = -18.430,
    	a_h = -26.104,
    	b_h = -7.535,
    	l_h = -6.727,
    	A = -10.906,
    	B = 872.02,
    	C = 0,
    	D = 0,
    	E = 0,
    	alpha = 0.04,
    	beta = 0.33,
        eps = 37.5
    ),
    shortDesc = u""" """,
    longDesc = 
u"""

"""
)
entry(
    index = 25,
    label = "ethylacetate",
    solvent = SolventData(
    	c_g = 0.203	,
    	e_g = -0.335,
    	s_g = 1.251	,
    	a_g = 2.949	,
    	b_g = 0		,
    	l_g = 0.917	,
    	c_h = -7.063,
    	e_h = 4.671	,
    	s_h = -15.141,
    	a_h = -28.763,
    	b_h = 0.0	,
    	l_h = -7.691,
    	A = 14.354,
    	B = -154.6,
    	C = -3.7887,
    	D = 0,
    	E = 0,
    	alpha = 0,
    	beta = 0.45,
        eps = 6.0
    ),
    shortDesc = u""" """,
    longDesc = 
u"""

"""
)