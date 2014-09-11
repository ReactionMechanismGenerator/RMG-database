#!/usr/bin/env python
# encoding: utf-8

name = "Abraham Solute Descriptors"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = -11,
    label = "O",
    group = 
"""
1 * O 0
""",
    solute = None,
    shortDesc = u"""""",
    longDesc = 
u"""

"""
)

entry(
    index = -10,
    label = "Oss",
    group = 
"""
1 * Os 0
""",
    solute = None,
    shortDesc = u"""""",
    longDesc = 
u"""

"""
)

entry(
    index = -9,
    label = "Cb",
    group = 
"""
1 * Cb 0

""",
    solute = None,
    shortDesc = u"""""",
    longDesc = 
u"""

"""
)

entry(
    index = -8,
    label = "N",
    group = 
"""
1 * N 0
""",
    solute = None,
    shortDesc = u"""""",
    longDesc = 
u"""

"""
)

entry(
    index = -7,
    label = "N3s",
    group = 
"""
1 * N3s 0
""",
    solute = None,
    shortDesc = u"""""",
    longDesc = 
u"""

"""
)

entry(
    index = -6,
    label = "N3d",
    group = 
"""
1 * N3d 0
""",
    solute = None,
    shortDesc = u"""""",
    longDesc = 
u"""

"""
)

entry(
    index = -5,
    label = "N3t",
    group = 
"""
1 * N3t 0
""",
    solute = None,
    shortDesc = u"""""",
    longDesc = 
u"""

"""
)

entry(
    index = -4,
    label = "O",
    group = 
"""
1 * {Os,Od} 0
""",
    solute = None,
    shortDesc = u"""""",
    longDesc = 
u"""

"""
)
entry(
	index = -3,
	label = "R",
	group = 
"""
1 * R 0
""",
	solute = None,
	shortDesc = u"""""",
	longDesc = 
u"""

"""
)

entry(
	index = -2,
	label = "C",
	group = 
"""
1 * C 0
""",
	solute = None,
	shortDesc = u"""""",
	longDesc = 
u"""

"""
)

entry(
	index = -1,
	label = "Css",
	group = 
"""
1 * Cs 0
""",
	solute = None,
	shortDesc = u"""""",
	longDesc = 
u"""

"""
)

entry(
	index = 0,
	label = "Cds",
	group = 
"""
1 * {Cd,CO} 0
""",
	solute = None,
	shortDesc = u"""""",
	longDesc = 
u"""

"""
)

entry(
    index = 1,
    label = "CssH3",
    group = 
"""
1 * Cs  0 {2,S} {3,S} {4,S} {5,S}
2   H   0 {1,S}
3   H   0 {1,S}
4   H   0 {1,S}
5   R   0 {1,S}
""",
    solute = SoluteData(
        S = -0.075,
		 B =  0.007,
		 E = -0.104,
		 L =  0.321,
		 A =  0
    ),
    shortDesc = u"""Platts fragment 1 sp3 CH3""",
    longDesc = 
u"""

"""
)

entry(
    index = 2,
    label = "CssH2",
    group = 
"""
1 * Cs  0 {2,S} {3,S} {4,S} {5,S}
2   H   0 {1,S}
3   H   0 {1,S}
4   R!H 0 {1,S}
5   R!H 0 {1,S}  
""",
    solute = SoluteData(
        S =  0,
		 B =  0,
		 E =  0,
		 L =  0.499,
		 A =  0
    ),
    shortDesc = u"""Platts fragment 2 sp3 >CH2""",
    longDesc = 
u"""

"""
)

entry(
    index = 3,
    label = "CssH",
    group = 
"""
1 * Cs  0 {2,S} {3,S} {4,S} {5,S}
2   H   0 {1,S}
3   R!H   0 {1,S}
4   R!H   0 {1,S}
5   R!H   0 {1,S}

""",
    solute = SoluteData(
        S =  0.036,
		 B =  0.011,
		 E =  0.089,
		 L =  0.499,
		 A =  0
    ),
    shortDesc = u"""Platts fragment 3 sp3 >CH-""",
    longDesc = 
u"""

"""
)

entry(
	index = 4,
	label = "Css-noH",
	group = 
"""
1 * Cs 0 {2,S} {3,S} {4,S} {5,S}
2   R!H   0 {1,S}
3   R!H   0 {1,S}
4   R!H   0 {1,S}
5	R!H	  0	{1,S}

""",
	solute = SoluteData(
		 S =  0.071,
		 B =  0.037,
		 E =  0.187,
		 L =  0.443,
		 A =  0
	),
	shortDesc = u"""Platts fragment 4 sp3 >C<""",		longDesc = 
u"""

"""
)

entry(
	index = 5,
	label = "CdsH2",
	group = 
"""
1 * {Cd,CO} 0 {2,S} {3,S} {4,D}
2   H 0 {1,S}
3   H 0 {1,S}
4   R!H 0 {1,D}

""",
	solute = SoluteData(
		 S =  -0.085,
		 B =  0.019,
		 E =  -0.045,
		 L =  0.244,
		 A =  0
	),
	shortDesc = u"""Platts' fragment 5 sp2 =CH2""",
	longDesc = 
u"""

"""
)

entry(
	index = 6,
	label = "CdsH",
	group = 
"""
1 * {Cd,CO} 0 {2,S} {3,S} {4,D}
2   H 0 {1,S}
3   R!H 0 {1,S}
4   R!H 0 {1,D}

""",
	solute = SoluteData(
		 S =  0.05,
		 B =  0.011,
		 E =  0.068,
		 L =  0.469,
		 A =  0,
	),
	shortDesc = u"""Platts' fragment 6 sp2 =CH-""",
	longDesc = 
u"""

"""
)

entry(
	index = 7,
	label = "Cds-noH",
	group = 
"""
1 * {Cd,CO,Cb} 0 {2,S} {3,S} {4,D}
2   R!H 0 {1,S}
3   R!H 0 {1,S}
4   R!H 0 {1,D}

""",
	solute = SoluteData(
		 S =  0.101,
		 B =  0,
		 E =  0.18,
		 L =  0.624,
		 A =  0,
	),
	shortDesc = u"""Platts' fragment 7 sp2 =C<""",
	longDesc = 
u"""

"""
)

entry(
	index = 8,
	label = "Cbf",
	group = 
"""
1 * Cbf 0

""",
	solute = SoluteData(
		 S =  0.121,
		 B =  0.019,
		 E =  0.3,
		 L =  0.744,
		 A =  0,
	),
	shortDesc = u"""Platts' fragment 8 fused aromatic""",
	longDesc = 
u"""

"""
)

entry(
	index = 9,
	label = "Ct",
	group = 
"""
1 * Ct 0

""",
	solute = SoluteData(
		 S =  0.034,
		 B =  0.028,
		 E =  0.04,
		 L =  0.332,
		 A =  0,
	),
	shortDesc = u"""Platts' fragment 9 sp""",
	longDesc = 
u"""

"""
)

entry(
        index = 10,
        label = "N3sH2",
        group =
"""
1 * N3s 0 {2,S} {3,S} 
2   H   0 {1,S}
3   H   0 {1,S}
""",
	solute = None,
	shortDesc = u"""""",
	longDesc = 
u"""

""")

entry(
        index = 11,
        label = "N3sH2-aromatic",
        group = "OR{N3sH2-Cb,N3sH2-N5ring}",
        solute = SoluteData(
         S =  0.383,
         B =  0.275,
         E =  0.163,
         L =  0.949,
         A =  0.0
    ),
    shortDesc = u"""Platts fragment 11""",
    longDesc = 
u"""

""")

entry(
        index = 12,
        label = "N3sH",
        group =
"""
1 * N3s 0 {2,S} {3,S} {4,S}
2   H   0 {1,S}
3   R!H 0 {1,S}
4   R!H   0 {1,S}
""",
solute = SoluteData(
         S =  0.265,
         B =  0.541,
         E =  0.138,
         L =  0.568,
         A =  0.087
    ),
    shortDesc = u"""Platts fragment 12 >NH (fragment 5 for A)""",
    longDesc = 
u"""

""")

entry(
        index = 13,
        label = "N3sH-aromatic",
        group = "OR{N3sH-Cb,N3sH-N5ring}",
        solute = SoluteData(
         S =  0.311,
         B =  0.415,
         E =  0.192,
         L =  0.912,
         A =  0.0
    ),
    shortDesc = u"""Platts fragment 13""",
    longDesc = 
u"""

""")

entry(
    index = 14,
    label = "N3sH-pyrrole",
    group = 
"""
1 * N3s      0 {2,S} {3,S} {4,S}
2   H        0 {1,S}
3   Cb       0 {1,S} {5,B}
4   Cb       0 {1,S} {6,B}
5   Cb       0 {3,B} {6,B}
6   Cb       0 {4,B} {5,B}
""",
    solute = SoluteData(
         S =  0.221,
         B =  0.316,
         E =  -0.03,
         L =  1.25,
         A =  0.371
    ),
    shortDesc = u"""Platts fragment 14 pyrrole (fragment 8 for A)""",
    longDesc = 
u"""

"""
)

entry(
        index = 15,
        label = "N3s-noH",
        group =
"""
1 * N3s 0 {2,S} {3,S} {4,S}
2   R!H 0 {1,S}
3   R!H 0 {1,S}
4   R!H 0 {1,S}
""",
solute = SoluteData(
         S =  0.323,
         B =  0.653,
         E =  0.22,
         L =  0.4,
         A =  0.0
    ),
    shortDesc = u"""Platts fragment 15 >N-""",
    longDesc = 
u"""

""")

entry(
        index = 16,
        label = "N3s-noH-aromatic",
        group = "OR{N3s-noH-Cb,N3s-noH-N5ring}",
        solute = SoluteData(
         S =  0.295,
         B =  0.321,
         E =  0.346,
         L =  0.869,
         A =  0.0
    ),
    shortDesc = u"""Platts fragment 16""",
    longDesc = 
u"""

""")

entry(
    index = 17,
    label = "N3s-noH-pyrrole",
    group = 
"""
1 * N3s      0 {2,S} {3,S} {4,S}
2   R!H      0 {1,S}
3   Cb       0 {1,S} {5,B}
4   Cb       0 {1,S} {6,B}
5   Cb       0 {3,B} {6,B}
6   Cb       0 {4,B} {5,B}
""",
    solute = SoluteData(
         S =  0.265,
         B =  0.392,
         E =  0.083,
         L =  0.794,
         A =  0.0
    ),
    shortDesc = u"""Platts fragment 17 pyrrole""",
    longDesc = 
u"""

"""
)

entry(
        index = 18,
        label = "N3d",
        group =
"""
1 * N3d 0
""",
solute = SoluteData(
         S =  0.125,
         B =  0.2,
         E =  0.117,
         L =  -0.235,
         A =  0.0
    ),
    shortDesc = u"""Platts fragment 18 =N""",
    longDesc = 
u"""

""")



entry(
      index = 19,
      label = "N3b",
      group =
"""
1 * N3b 0
""",
    solute = SoluteData(
         S =  0.254,
         B =  0.596,
         E =  0.121,
         L =  -0.24,
         A =  0,
    ),
    shortDesc = u"""Platts group 19 =N sp2 cyclic""",
    longDesc = 
u"""

"""
)

entry(
      index = 20,
      label = "N3bpyr",
      group =
"""
1 * N3b 0 {2,B} {6,B}
2   Cb 0 {1,B} {3,B}
3   Cb 0 {2,B} {4,B}
4   Cb 0 {3,B} {5,B}
5   Cb 0 {4,B} {6,B}
6   Cb 0 {1,B} {5,B}
""",
    solute = SoluteData(
         S =  0.223,
         B =  0.321,
         E =  0.046,
         L =  0.574,
         A =  0,
    ),
    shortDesc = u"""Platts group 20 pyridine""",
    longDesc = 
u"""

"""
)

entry(
        index = 21,
        label = "N3t",
        group =
"""
1 * N3t 0 {2,T}
2   Ct  0 {1,T}
""",
solute = SoluteData(
         S =  0.694,
         B =  0.242,
         E =  0.0,
         L =  0.757,
         A =  0.0
    ),
    shortDesc = u"""Platts fragment 21 N#C-""",
    longDesc = 
u"""

""")

entry(
        index = 22,
        label = "N3t-aromatic",
        group = "OR{N3t-Cb,N3t-N5ring}",
        solute = SoluteData(
         S =  0.39,
         B =  0.103,
         E =  0.0,
         L =  0.732,
         A =  0.0
    ),
    shortDesc = u"""Platts fragment 22""",
    longDesc = 
u"""

""")

entry(
        index = 23,
        label = "NO2",
        group =
"""
1 * N3s 0 {2,S} {3,S} {4,S}
2   R   0 {1,S}
3   Os  0 {1,S}
4   Os  0 {1,S}
""",
solute = SoluteData(
         S =  0.0,
         B =  -0.476,
         E =  0.2,
         L =  0.278,
         A =  0.0
    ),
    shortDesc = u"""Platts fragment 23 -NO2""",
    longDesc = 
u"""

""")

entry(
    index = 25,
    label = "ONO2",
    group = 
"""
1 * N3s      0 {2,S} {3,S} {4,S}
2   Os       0 {1,S}
3   Os       0 {1,S}
4   Os       0 {1,S}
""",
    solute = SoluteData(
         S =  -0.476,
         B =  -0.204,
         E =  0.0,
         L =  0.0,
         A =  0.0
    ),
    shortDesc = u"""Platts fragment 25 nitrate""",
    longDesc = 
u"""

"""
)

entry(
	index = 26,
	label = "OssH",
	group = 
"""
1 * Os 0 {2,S}
2   H 0 {1,S}

""",
	solute = SoluteData(
		 S =  0.247,
		 B =  0.307,
		 E =  0.061,
		 L =  0.672,
		 A =  0
	),
	shortDesc = u"""Platts fragment 26 -OH""",
	longDesc = 
u"""

"""
)

entry(
	index = 27,
	label = "Oss-noncyclic",
	group = 
"""
1 * Os 0 {2,S} {3,S}
2   R!H 0 {1,S}
3   R!H 0 {1,S}

""",
	solute = SoluteData(
		 S =  0.185,
		 B =  0.211,
		 E =  0.014,
		 L =  0.360,
		 A =  0
	),
	shortDesc = u"""Platts fragment 27 noncyclic -O-""",
	longDesc = 
u"""

"""
)

entry(
	index = 30,
	label = "Od",
	group = 
"""
1 * Od 0

""",
	solute = SoluteData(
		 S =  0.370,
		 B =  0.334,
		 E =  -0.041,
		 L =  0.495,
		 A =  0
	),
	shortDesc = u"""Platts fragment 30 sp2 =O""",
	longDesc = 
u"""

"""
)

entry(
    index = 31,
    label = "Ss",
    group = 
"""
1 * Ss 0

""",
    solute = SoluteData(
         S =  0.189,
         B =  0.168,
         E =  0.33,
         L =  1.258,
         A =  0
    ),
    shortDesc = u"""Platts fragment 31 -S- sp3""",
    longDesc = 
u"""

"""
)

entry(
    index = 32,
    label = "Ss-aromatic",
    group = 
"""
1 * Ss      0 {2,S} {5,S}
2   Cb      0 {1,S} {3,B}
3   {Cb,N3b} 0 {2,B} {4,B}
4   {Cb,N3b} 0 {3,B} {5,B}
5   Cb      0 {1,S} {4,B}

""",
    solute = SoluteData(
         S =  0,
         B =  0.043,
         E =  0.116,
         L =  0.848,
         A =  0
    ),
    shortDesc = u"""Platts fragment 32 -S- aromatic""",
    longDesc = 
u"""

"""
)

entry(
    index = 33,
    label = "Sd",
    group = 
"""
1 * Sd 0

""",
    solute = SoluteData(
         S =  0.618,
         B =  0.071,
         E =  0.364,
         L =  0.954,
         A =  0
    ),
    shortDesc = u"""Platts fragment 33 =S sp2""",
    longDesc = 
u"""

"""
)

entry(
    index = 34,
    label = "Sds",
    group = 
"""
1 * Sd 0 {2,S} {3,S}
2   R  0 {1,S}
3   R  0 {1,S}

""",
    solute = SoluteData(
         S =  1.065,
         B =  0.448,
         E =  0.413,
         L =  2.196,
         A =  0
    ),
    shortDesc = u"""Platts fragment 34 >S=""",
    longDesc = 
u"""

"""
)

entry(
    index = 35,
    label = "SdsOsOdOd",
    group = 
"""
1 * Sd 0 {2,D} {3,D} {4,S}
2   Od 0 {1,D}
3   Od 0 {1,D}
4   Os 0 {1,S}

""",
    solute = SoluteData(
         S =  -0.505,
         B =  -0.188,
         E =  0.0,
         L =  0.0,
         A =  0.0
    ),
    shortDesc = u"""Platts fragment 35 sulfonate""",
    longDesc = 
u"""

"""
)

entry(
    index = 36,
    label = "S",
    group = 
"""
1 * {S,Ss,Sd,Sa} 0

""",
    solute = SoluteData(
         S =  0.643,
         B =  0.0,
         E =  0.465,
         L =  0.554,
         A =  0
    ),
    shortDesc = u"""Platts fragment 36 (any other sulfur)""",
    longDesc = 
u"""

"""
)



entry(
    index = 37,
    label = "Cb-noH",
    group = 
"""
1 * Cb 0 {2,B} {3,B} {4,B}
2   R!H 0 {1,B}
3   R!H 0 {1,B}
4   R!H 0 {1,B}

""",
    solute = SoluteData(
         S =  0.101,
         B =  0,
         E =  0.18,
         L =  0.624,
         A =  0,
    ),
    shortDesc = u"""same as Platts group 7""",
    longDesc = 
u"""

"""
)

entry(
    index = 38,
    label = "Cb-H",
    group = 
"""
1 * Cb 0 {2,B} (3,B} (4,S}
2   R!H 0 {1,B}
3   R!H 0 {1,B}
4   H   0 {1,S}

""",
    solute = SoluteData(
         S =  0.05,
         B =  0.011,
         E =  0.068,
         L =  0.469,
         A =  0,
    ),
    shortDesc = u"""same as Platts group 6""",
    longDesc = 
u"""

"""
)

entry(
    index = 39,
    label = "Cb-noHnoRing",
    group = 
"""
1 * Cb 0 {2,B} {3,B} {4,S}
2   R!H 0 {1,B}
3   R!H 0 {1,B}
4   R!H 0 {1,S}

""",
    solute = SoluteData(
         S =  0.101,
         B =  0,
         E =  0.18,
         L =  0.624,
         A =  0,
    ),
    shortDesc = u"""same as Platts group 7""",
    longDesc = 
u"""
Cb is attached to a 3rd R group that isn't in the ring,as in phenol.
"""
)

entry(
    index = 40,
    label = "N3sH2-Cb",
    group = 
"""
1 * N3s      0 {2,S} {3,S} {4,S}
2   H        0 {1,S}
3   H        0 {1,S}
4   Cb       0 {1,S} {5,B} {6,B}
5   {Cb,N3b} 0 {4,B} {7,B}
6   {Cb,N3b} 0 {4,B} {8,B}
7   {Cb,N3b} 0 {5,B} {9,B}
8   {Cb,N3b} 0 {6,B} {9,B}
9   {Cb,N3b} 0 {7,B} {8,B}
""",
    solute = None,
    shortDesc = u"""""",
    longDesc = 
u"""

"""
)

entry(
    index = 41,
    label = "N3sH2-N5ring",
    group = 
"""
1 * N3s      0 {2,S} {3,S} {4,S}
2   H        0 {1,S}
3   H        0 {1,S}
4   N3s      0 {1,S} {5,S} {6,S}
5   {Cb,N3b} 0 {4,S} {7,B}
6   {Cb,N3b} 0 {4,S} {8,B}
7   {Cb,N3b} 0 {5,B} {8,B}
8   {Cb,N3b} 0 {6,B} {7,B}
""",
    solute = None,
    shortDesc = u"""""",
    longDesc = 
u"""

"""
)

entry(
    index = 42,
    label = "N3sH-Cb",
    group = 
"""
1 * N3s      0 {2,S} {3,S} {4,S}
2   H        0 {1,S}
3   R!H      0 {1,S}
4   Cb       0 {1,S} {5,B} {6,B}
5   {Cb,N3b} 0 {4,B} {7,B}
6   {Cb,N3b} 0 {4,B} {8,B}
7   {Cb,N3b} 0 {5,B} {9,B}
8   {Cb,N3b} 0 {6,B} {9,B}
9   {Cb,N3b} 0 {7,B} {8,B}
""",
    solute = None,
    shortDesc = u"""""",
    longDesc = 
u"""

"""
)

entry(
    index = 43,
    label = "N3sH-N5ring",
    group = 
"""
1 * N3s      0 {2,S} {3,S} {4,S}
2   H        0 {1,S}
3   R!H      0 {1,S}
4   N3s      0 {1,S} {5,S} {6,S}
5   {Cb,N3b} 0 {4,S} {7,B}
6   {Cb,N3b} 0 {4,S} {8,B}
7   {Cb,N3b} 0 {5,B} {8,B}
8   {Cb,N3b} 0 {6,B} {7,B}
""",
    solute = None,
    shortDesc = u"""""",
    longDesc = 
u"""

"""
)

entry(
    index = 44,
    label = "N3s-noH-Cb",
    group = 
"""
1 * N3s      0 {2,S} {3,S} {4,S}
2   R!H        0 {1,S}
3   R!H      0 {1,S}
4   Cb       0 {1,S} {5,B} {6,B}
5   {Cb,N3b} 0 {4,B} {7,B}
6   {Cb,N3b} 0 {4,B} {8,B}
7   {Cb,N3b} 0 {5,B} {9,B}
8   {Cb,N3b} 0 {6,B} {9,B}
9   {Cb,N3b} 0 {7,B} {8,B}
""",
    solute = None,
    shortDesc = u"""""",
    longDesc = 
u"""

"""
)

entry(
    index = 45,
    label = "N3s-noH-N5ring",
    group = 
"""
1 * N3s      0 {2,S} {3,S} {4,S}
2   R!H      0 {1,S}
3   R!H      0 {1,S}
4   N3s      0 {1,S} {5,S} {6,S}
5   {Cb,N3b} 0 {4,S} {7,B}
6   {Cb,N3b} 0 {4,S} {8,B}
7   {Cb,N3b} 0 {5,B} {8,B}
8   {Cb,N3b} 0 {6,B} {7,B}
""",
    solute = None,
    shortDesc = u"""""",
    longDesc = 
u"""

"""
)


entry(
    index = 46,
    label = "NO2-Cb",
    group = 
"""
1 * N3s      0 {2,S} {3,S} {4,S}
2   Os       0 {1,S}
3   Os       0 {1,S}
4   Cb       0 {1,S} {5,B} {6,B}
5   {Cb,N3b} 0 {4,B} {7,B}
6   {Cb,N3b} 0 {4,B} {8,B}
7   {Cb,N3b} 0 {5,B} {9,B}
8   {Cb,N3b} 0 {6,B} {9,B}
9   {Cb,N3b} 0 {7,B} {8,B}
""",
    solute = SoluteData(
         S =  -0.231,
         B =  -0.525,
         E =  0.21,
         L =  0.347,
         A =  0.0
    ),
    shortDesc = u"""Platts fragment 24""",
    longDesc = 
u"""

"""
)

entry(
    index = 47,
    label = "NO2-N5ring",
    group = 
"""
1 * N3s      0 {2,S} {3,S} {4,S}
2   Os       0 {1,S}
3   Os       0 {1,S}
4   N3s      0 {1,S} {5,S} {6,S}
5   {Cb,N3b} 0 {4,S} {7,B}
6   {Cb,N3b} 0 {4,S} {8,B}
7   {Cb,N3b} 0 {5,B} {8,B}
8   {Cb,N3b} 0 {6,B} {7,B}
""",
    solute = SoluteData(
         S =  -0.231,
         B =  -0.525,
         E =  0.21,
         L =  0.347,
         A =  0.0
    ),
    shortDesc = u"""Platts fragment 24""",
    longDesc = 
u"""

"""
)

entry(
    index = 55,
    label = "N3t-Cb",
    group = 
"""
1 * N3t 0 {2,T}
2   Ct  0 {1,T} {3,S}
3   Cb  0 {2,S}
""",
    solute = None,
    shortDesc = u"""""",
    longDesc = 
u"""

"""
)

entry(
    index = 56,
    label = "N3t-N5ring",
    group = 
"""
1 * N3t      0 {2,T}
2   Ct       0 {1,T} {3,S}
3   N3s      0 {2,S} {4,S} {5,S}
4   {Cb,N3b} 0 {3,S} {6,B}
5   {Cb,N3b} 0 {3,S} {7,B}
6   {Cb,N3b} 0 {4,B} {7,B}
7   {Cb,N3b} 0 {5,B} {6,B}
""",
    solute = None,
    shortDesc = u"""""",
    longDesc = 
u"""

"""
)



entry(
	index = 57,
	label = "Cdd",
	group = 
"""
1 * Cdd 0

""",
	solute = SoluteData(
		 S =  0.101,
		 B =  0,
		 E =  0.18,
		 L =  0.624,
		 A =  0,
	),
	shortDesc = u"""Platts' fragment 7 nonfused aromatic =C<""",
	longDesc = 
u"""

"""
)


tree(
"""
L0: R

L1: C

	L2: Cbf // fused aromatic
	
	L2: Css // sp3
		L3: CssH3
		L3: CssH2
		L3: CssH
		L3: Css-noH
	
	L2: Cds // sp2
		L3: CdsH2
		L3: CdsH
		L3: Cds-noH
		
	L2: Ct // sp

	L2: Cdd // sp2 nonfused aromatic
	
	L2: Cb
		L3: Cb-noH
		L3: Cb-H
		L3: Cb-noHnoRing
	

L1: O

	L2: Oss
		L3: OssH           // Hydroxyl group
		L3: Oss-noncyclic
		
    L2: Od // sp2

L1: N

    L2: N3s // sp3
        L3: N3sH2
            L4: N3sH2-aromatic
                L5: N3sH2-Cb
                L5: N3sH2-N5ring
        L3: N3sH
            L4: N3sH-aromatic
                L5: N3sH-Cb
                L5: N3sH-N5ring
                    L6: N3sH-pyrrole
            L4: NO2
        L3: N3s-noH
            L4: N3s-noH-aromatic
                L5: N3s-noH-Cb
                    L6: NO2-Cb
                L5: N3s-noH-N5ring
                    L6: N3s-noH-pyrrole
                    L6: NO2-N5ring
            L4: NO2
                L5: ONO2 // nitrate
        
    
    L2: N3d // sp2
    
    L2: N3t // sp
        L3: N3t-aromatic
            L4: N3t-Cb
            L4: N3t-N5ring
            
    
    L2: N3b
        L3: N3bpyr

L1: S
    
    L2: Ss // sp3
        L3: Ss-aromatic
    
    L2: Sd
        L3: Sds
            L4: SdsOsOdOd // sulfonate
"""
)
