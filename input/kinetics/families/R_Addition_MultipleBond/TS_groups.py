#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_MultipleBond/TS_groups"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 1,
    label = "XZ",
    group = "OR{CZ, SZ, OCO, OCddO, OSi, OSiddO, Od_N, N_R}",
    distances = DistanceData(
        distances = {'d12': 1.357076, 'd13': 2.240507, 'd23': 2.933188},
        uncertainties = {'d12': 0.010297, 'd13': 0.033216, 'd23': 0.049111},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 13 distances.
[<Entry index=28 label="Cd/NonDe2_Cd/H2">, <Entry index=192 label="C_methyl">]
[<Entry index=9 label="Cd/H2_Cd/NonDe2">, <Entry index=192 label="C_methyl">]
[<Entry index=7 label="Cd/H2_Cd/H/NonDe">, <Entry index=192 label="C_methyl">]
[<Entry index=101 label="CS/CsCs_S">, <Entry index=192 label="C_methyl">]
[<Entry index=94 label="CS/H2_S">, <Entry index=192 label="C_methyl">]
[<Entry index=87 label="CO/H2_O">, <Entry index=192 label="C_methyl">]
[<Entry index=90 label="CO/NonDe2_O">, <Entry index=192 label="C_methyl">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=160 label="H_rad">]
[<Entry index=119 label="OCO">, <Entry index=192 label="C_methyl">]
[<Entry index=88 label="CO/H/NonDe_O">, <Entry index=192 label="C_methyl">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=192 label="C_methyl">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 2,
    label = "Y_rad_birad_trirad_quadrad",
    group = "OR{Y_rad, Y_birad, Y_1centertrirad, Y_2centerbirad, Y_1centerbirad, Y_1centerquadrad}",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 3,
    label = "CZ",
    group = 
"""
1 *1 {Cd,Cdd,Ct,CO,CS}                0 {2,{D,T}}
2 *2 {Cd,Cdd,Ct,Od,Sd,Sid,Sidd,Sit,N} 0 {1,{D,T}}
""",
    distances = DistanceData(
        distances = {'d12': 0.02771, 'd13': 0.098786, 'd23': 0.047819},
        uncertainties = {'d12': 0.008175, 'd13': 0.01813, 'd23': 0.050169},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 10 distances.
[<Entry index=28 label="Cd/NonDe2_Cd/H2">, <Entry index=192 label="C_methyl">]
[<Entry index=9 label="Cd/H2_Cd/NonDe2">, <Entry index=192 label="C_methyl">]
[<Entry index=7 label="Cd/H2_Cd/H/NonDe">, <Entry index=192 label="C_methyl">]
[<Entry index=101 label="CS/CsCs_S">, <Entry index=192 label="C_methyl">]
[<Entry index=94 label="CS/H2_S">, <Entry index=192 label="C_methyl">]
[<Entry index=87 label="CO/H2_O">, <Entry index=192 label="C_methyl">]
[<Entry index=90 label="CO/NonDe2_O">, <Entry index=192 label="C_methyl">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=160 label="H_rad">]
[<Entry index=88 label="CO/H/NonDe_O">, <Entry index=192 label="C_methyl">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=192 label="C_methyl">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 4,
    label = "Cd_Cd",
    group = 
"""
1 *1 Cd 0 {2,D}
2 *2 Cd 0 {1,D}
""",
    distances = DistanceData(
        distances = {'d12': 0.00571, 'd13': 0.081955, 'd23': 0.046828},
        uncertainties = {'d12': 0.014532, 'd13': 0.033233, 'd23': 0.09233},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 5 distances.
[<Entry index=28 label="Cd/NonDe2_Cd/H2">, <Entry index=192 label="C_methyl">]
[<Entry index=9 label="Cd/H2_Cd/NonDe2">, <Entry index=192 label="C_methyl">]
[<Entry index=7 label="Cd/H2_Cd/H/NonDe">, <Entry index=192 label="C_methyl">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=160 label="H_rad">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=192 label="C_methyl">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 5,
    label = "Cd/H2",
    group = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D}
3    H  0 {1,S}
4    H  0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.003461, 'd13': 0.085379, 'd23': 0.073709},
        uncertainties = {'d12': 0.019094, 'd13': 0.043947, 'd23': 0.122196},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 4 distances.
[<Entry index=9 label="Cd/H2_Cd/NonDe2">, <Entry index=192 label="C_methyl">]
[<Entry index=7 label="Cd/H2_Cd/H/NonDe">, <Entry index=192 label="C_methyl">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=160 label="H_rad">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=192 label="C_methyl">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 6,
    label = "Cd/H2_Cd/H2",
    group = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.002877, 'd13': 0.084394, 'd23': 0.104414},
        uncertainties = {'d12': 0.130082, 'd13': 0.303377, 'd23': 0.844909},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=160 label="H_rad">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=192 label="C_methyl">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 7,
    label = "Cd/H2_Cd/H/NonDe",
    group = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    H        0 {1,S}
4    H        0 {1,S}
5    H        0 {2,S}
6    {Cs,O,S} 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.003872, 'd13': 0.103372, 'd23': 0.147656},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=7 label="Cd/H2_Cd/H/NonDe">, <Entry index=192 label="C_methyl">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 8,
    label = "Cd/H2_Cd/H/OneDe",
    group = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    H                0 {1,S}
4    H                0 {1,S}
5    H                0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 9,
    label = "Cd/H2_Cd/NonDe2",
    group = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    H        0 {1,S}
4    H        0 {1,S}
5    {Cs,O,S} 0 {2,S}
6    {Cs,O,S} 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.014142, 'd13': 0.069112, 'd23': -0.053974},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=9 label="Cd/H2_Cd/NonDe2">, <Entry index=192 label="C_methyl">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 10,
    label = "Cd/H2_Cd/NonDe/OneDe",
    group = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    H                0 {1,S}
4    H                0 {1,S}
5    {Cs,O,S}         0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 11,
    label = "Cd/H2_Cd/TwoDe",
    group = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    H                0 {1,S}
4    H                0 {1,S}
5    {Cd,Ct,Cb,CO,CS} 0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 12,
    label = "Cd/H/NonDe",
    group = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D}
3    H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 13,
    label = "Cd/H/NonDe_Cd/H2",
    group = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    H        0 {2,S}
6    H        0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 14,
    label = "Cd/H/NonDe_Cd/H/NonDe",
    group = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    H        0 {2,S}
6    {Cs,O,S} 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 15,
    label = "Cd/H/Os_Cd/H/Cs",
    group = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    O  0 {1,S}
5    H  0 {2,S}
6    Cs 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 16,
    label = "Cd/H/NonDe_Cd/H/OneDe",
    group = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    H                0 {1,S}
4    {Cs,O,S}         0 {1,S}
5    H                0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 17,
    label = "Cd/H/NonDe_Cd/NonDe2",
    group = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    {Cs,O,S} 0 {2,S}
6    {Cs,O,S} 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 18,
    label = "Cd/H/NonDe_Cd/NonDe/OneDe",
    group = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    H                0 {1,S}
4    {Cs,O,S}         0 {1,S}
5    {Cs,O,S}         0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 19,
    label = "Cd/H/NonDe_Cd/TwoDe",
    group = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    H                0 {1,S}
4    {Cs,O,S}         0 {1,S}
5    {Cd,Ct,Cb,CO,CS} 0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 20,
    label = "Cd/H/OneDe",
    group = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D}
3    H                0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 21,
    label = "Cd/H/OneDe_Cd/H2",
    group = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    H                0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    H                0 {2,S}
6    H                0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 22,
    label = "Cd/H/OneDe_Cd/H/NonDe",
    group = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    H                0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    H                0 {2,S}
6    {Cs,O,S}         0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 23,
    label = "Cd/H/OneDe_Cd/H/OneDe",
    group = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    H                0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    H                0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 24,
    label = "Cd/H/OneDe_Cd/NonDe2",
    group = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    H                0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    {Cs,O,S}         0 {2,S}
6    {Cs,O,S}         0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 25,
    label = "Cd/H/OneDe_Cd/NonDe/OneDe",
    group = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    H                0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    {Cs,O,S}         0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 26,
    label = "Cd/H/OneDe_Cd/TwoDe",
    group = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    H                0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    {Cd,Ct,Cb,CO,CS} 0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 27,
    label = "Cd/NonDe2",
    group = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D}
3    {Cs,O,S} 0 {1,S}
4    {Cs,O,S} 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.014142, 'd13': 0.069112, 'd23': -0.053974},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=28 label="Cd/NonDe2_Cd/H2">, <Entry index=192 label="C_methyl">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 28,
    label = "Cd/NonDe2_Cd/H2",
    group = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    {Cs,O,S} 0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    H        0 {2,S}
6    H        0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.014142, 'd13': 0.069112, 'd23': -0.053974},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=28 label="Cd/NonDe2_Cd/H2">, <Entry index=192 label="C_methyl">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 29,
    label = "Cd/NonDe2_Cd/H/NonDe",
    group = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    {Cs,O,S} 0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    H        0 {2,S}
6    {Cs,O,S} 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 30,
    label = "Cd/NonDe2_Cd/H/OneDe",
    group = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    {Cs,O,S}         0 {1,S}
4    {Cs,O,S}         0 {1,S}
5    H                0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 31,
    label = "Cd/NonDe2_Cd/NonDe2",
    group = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cd       0 {1,D} {5,S} {6,S}
3    {Cs,O,S} 0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    {Cs,O,S} 0 {2,S}
6    {Cs,O,S} 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 32,
    label = "Cd/NonDe2_Cd/NonDe/OneDe",
    group = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    {Cs,O,S}         0 {1,S}
4    {Cs,O,S}         0 {1,S}
5    {Cs,O,S}         0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 33,
    label = "Cd/NonDe2_Cd/TwoDe",
    group = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    {Cs,O,S}         0 {1,S}
4    {Cs,O,S}         0 {1,S}
5    {Cd,Ct,Cb,CO,CS} 0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 34,
    label = "Cd/NonDe/OneDe",
    group = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D}
3    {Cs,O,S}         0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 35,
    label = "Cd/NonDe/OneDe_Cd/H2",
    group = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    {Cs,O,S}         0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    H                0 {2,S}
6    H                0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 36,
    label = "Cd/NonDe/OneDe_Cd/H/NonDe",
    group = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    {Cs,O,S}         0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    H                0 {2,S}
6    {Cs,O,S}         0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 37,
    label = "Cd/NonDe/OneDe_Cd/H/OneDe",
    group = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    {Cs,O,S}         0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    H                0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 38,
    label = "Cd/NonDe/OneDe_Cd/NonDe2",
    group = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    {Cs,O,S}         0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    {Cs,O,S}         0 {2,S}
6    {Cs,O,S}         0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 39,
    label = "Cd/NonDe/OneDe_Cd/NonDe/OneDe",
    group = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    {Cs,O,S}         0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    {Cs,O,S}         0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 40,
    label = "Cd/NonDe/OneDe_Cd/TwoDe",
    group = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    {Cs,O,S}         0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    {Cd,Ct,Cb,CO,CS} 0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 41,
    label = "Cd/TwoDe",
    group = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 42,
    label = "Cd/TwoDe_Cd/H2",
    group = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    H                0 {2,S}
6    H                0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 43,
    label = "Cd/TwoDe_Cd/H/NonDe",
    group = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    H                0 {2,S}
6    {Cs,O,S}         0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 44,
    label = "Cd/TwoDe_Cd/H/OneDe",
    group = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    H                0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 45,
    label = "Cd/TwoDe_Cd/NonDe2",
    group = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    {Cs,O,S}         0 {2,S}
6    {Cs,O,S}         0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 46,
    label = "Cd/TwoDe_Cd/NonDe/OneDe",
    group = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    {Cs,O,S}         0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 47,
    label = "Cd/TwoDe_Cd/TwoDe",
    group = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cd               0 {1,D} {5,S} {6,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    {Cd,Ct,Cb,CO,CS} 0 {2,S}
6    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 48,
    label = "Cd_Cdd",
    group = 
"""
1 *1 Cd  0 {2,D}
2 *2 Cdd 0 {1,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 49,
    label = "Cd_Ca",
    group = 
"""
1 *1 Cd  0 {2,D}
2 *2 Cdd 0 {1,D} {3,D}
3    C   0 {2,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 50,
    label = "Cd/H2_Ca",
    group = 
"""
1 *1 Cd  0 {2,D} {3,S} {4,S}
2 *2 Cdd 0 {1,D} {5,D}
3    H   0 {1,S}
4    H   0 {1,S}
5    C   0 {2,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 51,
    label = "Cd/H/NonDe_Ca",
    group = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cdd      0 {1,D} {5,D}
3    H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    C        0 {2,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 52,
    label = "Cd/H/OneDe_Ca",
    group = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cdd              0 {1,D} {5,D}
3    H                0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    C                0 {2,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 53,
    label = "Cd/NonDe2_Ca",
    group = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cdd      0 {1,D} {5,D}
3    {Cs,O,S} 0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    C        0 {2,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 54,
    label = "Cd/NonDe/OneDe_Ca",
    group = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cdd              0 {1,D} {5,D}
3    {Cs,O,S}         0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    C                0 {2,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 55,
    label = "Cd/TwoDe_Ca",
    group = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cdd              0 {1,D} {5,D}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    C                0 {2,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 56,
    label = "Cd_Ck",
    group = 
"""
1 *1 Cd  0 {2,D}
2 *2 Cdd 0 {1,D} {3,D}
3    Od  0 {2,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 57,
    label = "Cd/H2_Ck",
    group = 
"""
1 *1 Cd  0 {2,D} {3,S} {4,S}
2 *2 Cdd 0 {1,D} {5,D}
3    H   0 {1,S}
4    H   0 {1,S}
5    Od  0 {2,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 58,
    label = "Cd/H/NonDe_Ck",
    group = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cdd      0 {1,D} {5,D}
3    H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    Od       0 {2,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 59,
    label = "Cd/H/OneDe_Ck",
    group = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cdd              0 {1,D} {5,D}
3    H                0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    Od               0 {2,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 60,
    label = "Cd/NonDe2_Ck",
    group = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Cdd      0 {1,D} {5,D}
3    {Cs,O,S} 0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    Od       0 {2,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 61,
    label = "Cd/NonDe/OneDe_Ck",
    group = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cdd              0 {1,D} {5,D}
3    {Cs,O,S}         0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    Od               0 {2,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 62,
    label = "Cd/TwoDe_Ck",
    group = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Cdd              0 {1,D} {5,D}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
5    Od               0 {2,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 63,
    label = "Cdd_Cd",
    group = 
"""
1 *1 Cdd 0 {2,D}
2 *2 Cd  0 {1,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 64,
    label = "Ca_Cd",
    group = 
"""
1 *1 Cdd 0 {2,D} {3,D}
2 *2 Cd  0 {1,D}
3    C   0 {1,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 65,
    label = "Ca_Cd/H2",
    group = 
"""
1 *1 Cdd 0 {2,D} {3,D}
2 *2 Cd  0 {1,D} {4,S} {5,S}
3    C   0 {1,D}
4    H   0 {2,S}
5    H   0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 66,
    label = "Ca_Cd/H/NonDe",
    group = 
"""
1 *1 Cdd      0 {2,D} {3,D}
2 *2 Cd       0 {1,D} {4,S} {5,S}
3    C        0 {1,D}
4    H        0 {2,S}
5    {Cs,O,S} 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 67,
    label = "Ca_Cd/H/OneDe",
    group = 
"""
1 *1 Cdd              0 {2,D} {3,D}
2 *2 Cd               0 {1,D} {4,S} {5,S}
3    C                0 {1,D}
4    H                0 {2,S}
5    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 68,
    label = "Ca_Cd/NonDe2",
    group = 
"""
1 *1 Cdd      0 {2,D} {3,D}
2 *2 Cd       0 {1,D} {4,S} {5,S}
3    C        0 {1,D}
4    {Cs,O,S} 0 {2,S}
5    {Cs,O,S} 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 69,
    label = "Ca_Cd/NonDe/OneDe",
    group = 
"""
1 *1 Cdd              0 {2,D} {3,D}
2 *2 Cd               0 {1,D} {4,S} {5,S}
3    C                0 {1,D}
4    {Cs,O,S}         0 {2,S}
5    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 70,
    label = "Ca_Cd/TwoDe",
    group = 
"""
1 *1 Cdd              0 {2,D} {3,D}
2 *2 Cd               0 {1,D} {4,S} {5,S}
3    C                0 {1,D}
4    {Cd,Ct,Cb,CO,CS} 0 {2,S}
5    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 71,
    label = "Ck_Cd",
    group = 
"""
1 *1 Cdd 0 {2,D} {3,D}
2 *2 Cd  0 {1,D}
3    Od  0 {1,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 72,
    label = "Ck_Cd/H2",
    group = 
"""
1 *1 Cdd 0 {2,D} {3,D}
2 *2 Cd  0 {1,D} {4,S} {5,S}
3    Od  0 {1,D}
4    H   0 {2,S}
5    H   0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 73,
    label = "Ck_Cd/H/NonDe",
    group = 
"""
1 *1 Cdd      0 {2,D} {3,D}
2 *2 Cd       0 {1,D} {4,S} {5,S}
3    Od       0 {1,D}
4    H        0 {2,S}
5    {Cs,O,S} 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 74,
    label = "Ck_Cd/H/OneDe",
    group = 
"""
1 *1 Cdd              0 {2,D} {3,D}
2 *2 Cd               0 {1,D} {4,S} {5,S}
3    Od               0 {1,D}
4    H                0 {2,S}
5    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 75,
    label = "Ck_Cd/NonDe2",
    group = 
"""
1 *1 Cdd      0 {2,D} {3,D}
2 *2 Cd       0 {1,D} {4,S} {5,S}
3    Od       0 {1,D}
4    {Cs,O,S} 0 {2,S}
5    {Cs,O,S} 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 76,
    label = "Ck_Cd/NonDe/OneDe",
    group = 
"""
1 *1 Cdd              0 {2,D} {3,D}
2 *2 Cd               0 {1,D} {4,S} {5,S}
3    Od               0 {1,D}
4    {Cs,O,S}         0 {2,S}
5    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 77,
    label = "Ck_Cd/TwoDe",
    group = 
"""
1 *1 Cdd              0 {2,D} {3,D}
2 *2 Cd               0 {1,D} {4,S} {5,S}
3    Od               0 {1,D}
4    {Cd,Ct,Cb,CO,CS} 0 {2,S}
5    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 78,
    label = "Cdd_Cdd",
    group = 
"""
1 *1 Cdd 0 {2,D}
2 *2 Cdd 0 {1,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 79,
    label = "Ca_Ca",
    group = 
"""
1 *1 Cdd 0 {2,D} {3,D}
2 *2 Cdd 0 {1,D} {4,D}
3    C   0 {1,D}
4    C   0 {2,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 80,
    label = "Ck_Ck",
    group = 
"""
1 *1 Cdd 0 {2,D} {3,D}
2 *2 Cdd 0 {1,D} {4,D}
3    Od  0 {1,D}
4    Od  0 {2,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 81,
    label = "Ca_Ck",
    group = 
"""
1 *1 Cdd 0 {2,D} {3,D}
2 *2 Cdd 0 {1,D} {4,D}
3    C   0 {1,D}
4    Od  0 {2,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 82,
    label = "Ck_Ca",
    group = 
"""
1 *1 Cdd 0 {2,D} {3,D}
2 *2 Cdd 0 {1,D} {4,D}
3    Od  0 {1,D}
4    C   0 {2,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 83,
    label = "Cdd_Sd",
    group = 
"""
1 *1 Cdd 0 {2,D}
2 *2 Sd  0 {1,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 84,
    label = "CS2",
    group = 
"""
1 *1 Cdd 0 {2,D} {3,D}
2 *2 Sd  0 {1,D}
3    Sd  0 {1,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 85,
    label = "CS_O",
    group = 
"""
1 *1 Cdd 0 {2,D} {3,D}
2 *2 Sd  0 {1,D}
3    Od  0 {1,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 86,
    label = "CO_O",
    group = 
"""
1 *1 CO 0 {2,D}
2 *2 Od 0 {1,D}
""",
    distances = DistanceData(
        distances = {'d12': -0.113808, 'd13': -0.058601, 'd23': -0.236747},
        uncertainties = {'d12': 0.006648, 'd13': 0.005275, 'd23': 0.004141},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 3 distances.
[<Entry index=90 label="CO/NonDe2_O">, <Entry index=192 label="C_methyl">]
[<Entry index=87 label="CO/H2_O">, <Entry index=192 label="C_methyl">]
[<Entry index=88 label="CO/H/NonDe_O">, <Entry index=192 label="C_methyl">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 87,
    label = "CO/H2_O",
    group = 
"""
1 *1 CO 0 {2,D} {3,S} {4,S}
2 *2 Od 0 {1,D}
3    H  0 {1,S}
4    H  0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.123668, 'd13': -0.000378, 'd23': -0.124864},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=87 label="CO/H2_O">, <Entry index=192 label="C_methyl">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 88,
    label = "CO/H/NonDe_O",
    group = 
"""
1 *1 CO       0 {2,D} {3,S} {4,S}
2 *2 Od       0 {1,D}
3    H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.113908, 'd13': -0.071068, 'd23': -0.250414},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=88 label="CO/H/NonDe_O">, <Entry index=192 label="C_methyl">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 89,
    label = "CO/H/OneDe_O",
    group = 
"""
1 *1 CO               0 {2,D} {3,S} {4,S}
2 *2 Od               0 {1,D}
3    H                0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 90,
    label = "CO/NonDe2_O",
    group = 
"""
1 *1 CO       0 {2,D} {3,S} {4,S}
2 *2 Od       0 {1,D}
3    {Cs,O,S} 0 {1,S}
4    {Cs,O,S} 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.103848, 'd13': -0.104358, 'd23': -0.334964},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=90 label="CO/NonDe2_O">, <Entry index=192 label="C_methyl">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 91,
    label = "CO/NonDe/OneDe_O",
    group = 
"""
1 *1 CO               0 {2,D} {3,S} {4,S}
2 *2 Od               0 {1,D}
3    {Cs,O,S}         0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 92,
    label = "CO/TwoDe_O",
    group = 
"""
1 *1 CO               0 {2,D} {3,S} {4,S}
2 *2 Od               0 {1,D}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 93,
    label = "CS_S",
    group = 
"""
1 *1 Cd 0 {2,D}
2 *2 Sd 0 {1,D}
""",
    distances = DistanceData(
        distances = {'d12': 0.292237, 'd13': 0.374842, 'd23': 0.477021},
        uncertainties = {'d12': 0.022669, 'd13': 0.017988, 'd23': 0.01412},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=101 label="CS/CsCs_S">, <Entry index=192 label="C_methyl">]
[<Entry index=94 label="CS/H2_S">, <Entry index=192 label="C_methyl">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 94,
    label = "CS/H2_S",
    group = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Sd 0 {1,D}
3    H  0 {1,S}
4    H  0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.273902, 'd13': 0.497202, 'd23': 0.716126},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=94 label="CS/H2_S">, <Entry index=192 label="C_methyl">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 95,
    label = "CS/H/NonDe_S",
    group = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Sd       0 {1,D}
3    H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 96,
    label = "CS/H/Cs_S",
    group = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Sd 0 {1,D}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 97,
    label = "CS/H/Os_S",
    group = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Sd 0 {1,D}
3    H  0 {1,S}
4    O  0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 98,
    label = "CS/H/Ss_S",
    group = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Sd 0 {1,D}
3    H  0 {1,S}
4    S  0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 99,
    label = "CS/H/OneDe_S",
    group = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Sd               0 {1,D}
3    H                0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 100,
    label = "CS/NonDe2_S",
    group = 
"""
1 *1 Cd       0 {2,D} {3,S} {4,S}
2 *2 Sd       0 {1,D}
3    {Cs,O,S} 0 {1,S}
4    {Cs,O,S} 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.310572, 'd13': 0.252482, 'd23': 0.237916},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=101 label="CS/CsCs_S">, <Entry index=192 label="C_methyl">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 101,
    label = "CS/CsCs_S",
    group = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Sd 0 {1,D}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.310572, 'd13': 0.252482, 'd23': 0.237916},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=101 label="CS/CsCs_S">, <Entry index=192 label="C_methyl">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 102,
    label = "CS/CsOs_S",
    group = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Sd 0 {1,D}
3    Cs 0 {1,S}
4    O  0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 103,
    label = "CS/CsSs_S",
    group = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Sd 0 {1,D}
3    Cs 0 {1,S}
4    S  0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 104,
    label = "CS/NonDe/OneDe_S",
    group = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Sd               0 {1,D}
3    {Cs,O,S}         0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 105,
    label = "CS/TwoDe_S",
    group = 
"""
1 *1 Cd               0 {2,D} {3,S} {4,S}
2 *2 Sd               0 {1,D}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 106,
    label = "Ct_Ct",
    group = 
"""
1 *1 Ct 0 {2,T}
2 *2 Ct 0 {1,T}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 107,
    label = "Ct/H_Ct/H",
    group = 
"""
1 *1 Ct 0 {2,T} {3,S}
2 *2 Ct 0 {1,T} {4,S}
3    H  0 {1,S}
4    H  0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 108,
    label = "Ct/H_Ct/NonDe",
    group = 
"""
1 *1 Ct       0 {2,T} {3,S}
2 *2 Ct       0 {1,T} {4,S}
3    H        0 {1,S}
4    {Cs,O,S} 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 109,
    label = "Ct/H_Ct/OneDe",
    group = 
"""
1 *1 Ct               0 {2,T} {3,S}
2 *2 Ct               0 {1,T} {4,S}
3    H                0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 110,
    label = "Ct/NonDe_Ct/H",
    group = 
"""
1 *1 Ct       0 {2,T} {3,S}
2 *2 Ct       0 {1,T} {4,S}
3    {Cs,O,S} 0 {1,S}
4    H        0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 111,
    label = "Ct/NonDe_Ct/NonDe",
    group = 
"""
1 *1 Ct       0 {2,T} {3,S}
2 *2 Ct       0 {1,T} {4,S}
3    {Cs,O,S} 0 {1,S}
4    {Cs,O,S} 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 112,
    label = "Ct/NonDe_Ct/OneDe",
    group = 
"""
1 *1 Ct               0 {2,T} {3,S}
2 *2 Ct               0 {1,T} {4,S}
3    {Cs,O,S}         0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 113,
    label = "Ct/OneDe_Ct/H",
    group = 
"""
1 *1 Ct               0 {2,T} {3,S}
2 *2 Ct               0 {1,T} {4,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    H                0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 114,
    label = "Ct/OneDe_Ct/NonDe",
    group = 
"""
1 *1 Ct               0 {2,T} {3,S}
2 *2 Ct               0 {1,T} {4,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cs,O,S}         0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 115,
    label = "Ct/OneDe_Ct/OneDe",
    group = 
"""
1 *1 Ct               0 {2,T} {3,S}
2 *2 Ct               0 {1,T} {4,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 300,
    label = "Ct_N",
    group = 
"""
1 *1 Ct        0 {2,T}
2 *2 {N3t,N5t} 0 {1,T}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 301,
    label = "Ct_N3t",
    group = 
"""
1 *1 Ct  0 {2,T}
2 *2 N3t 0 {1,T}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 302,
    label = "Ct_N5t",
    group = 
"""
1 *1 Ct  0 {2,T}
2 *2 N5t 0 {1,T}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 303,
    label = "Ct/H_N3t",
    group = 
"""
1 *1 Ct  0 {2,T} {3,S}
2 *2 N3t 0 {1,T}
3    H   0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 304,
    label = "Ct/NonDe_N3t",
    group = 
"""
1 *1 Ct          0 {2,T} {3,S}
2 *2 N3t         0 {1,T}
3    {Cs,N3s,Os} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 305,
    label = "Ct/OneDe_N3t",
    group = 
"""
1 *1 Ct                    0 {2,T} {3,S}
2 *2 N3t                   0 {1,T}
3    {Cd,Ct,Cb,CO,N3d,N5d} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 306,
    label = "Cds_N",
    group = 
"""
1 *1 Cd 0 {2,D}
2 *2 N  0 {1,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 307,
    label = "Cds_N3d",
    group = 
"""
1 *1 Cd  0 {2,D}
2 *2 N3d 0 {1,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 308,
    label = "Cds/H2_N3d",
    group = 
"""
1 *1 Cd  0 {2,D} {3,S} {4,S}
2 *2 N3d 0 {1,D}
3    H   0 {1,S}
4    H   0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 309,
    label = "Cds_sec_N3d",
    group = 
"""
1 *1 Cd  0 {2,D} {3,S} {4,S}
2 *2 N3d 0 {1,D}
3    H   0 {1,S}
4    R!H 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 310,
    label = "Cds_ter_N3d",
    group = 
"""
1 *1 Cd  0 {2,D} {3,S} {4,S}
2 *2 N3d 0 {1,D}
3    R!H 0 {1,S}
4    R!H 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 116,
    label = "Cdd_Od",
    group = 
"""
1 *1 Cdd    0 {2,D} {3,D}
2 *2 Od     0 {1,D}
3    {C,Od} 0 {1,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 117,
    label = "CO2",
    group = 
"""
1 *1 Cdd 0 {2,D} {3,D}
2 *2 Od  0 {1,D}
3    Od  0 {1,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 118,
    label = "Ck_O",
    group = 
"""
1 *1 Cdd 0 {2,D} {3,D}
2 *2 Od  0 {1,D}
3    C   0 {1,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 119,
    label = "OCO",
    group = 
"""
1 *1 Od 0 {2,D}
2 *2 CO 0 {1,D}
""",
    distances = DistanceData(
        distances = {'d12': -0.090058, 'd13': -0.321055, 'd23': -0.155411},
        uncertainties = {'d12': 0.03732, 'd13': 0.143054, 'd23': 0.12434},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 3 distances.
[<Entry index=119 label="OCO">, <Entry index=192 label="C_methyl">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 120,
    label = "OSi",
    group = 
"""
1 *1 Od 0 {2,D}
2 *2 Si 0 {1,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 121,
    label = "SZ",
    group = 
"""
1 *1 Sd 0 {2,D}
2 *2 R  0 {1,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 122,
    label = "Sd_Cdd",
    group = 
"""
1 *1 Sd  0 {2,D}
2 *2 Cdd 0 {1,D} {3,D}
3    R   0 {2,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 123,
    label = "Sd_Cdd/Sd",
    group = 
"""
1 *1 Sd  0 {2,D}
2 *2 Cdd 0 {1,D} {3,D}
3    Sd  0 {2,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 124,
    label = "Sd_Cdd/Od",
    group = 
"""
1 *1 Sd  0 {2,D}
2 *2 Cdd 0 {1,D} {3,D}
3    Od  0 {2,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 125,
    label = "Sd_Cds",
    group = 
"""
1 *1 Sd 0 {2,D}
2 *2 Cd 0 {1,D} {3,S} {4,S}
3    R  0 {2,S}
4    R  0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 126,
    label = "Sd_Cds/H2",
    group = 
"""
1 *1 Sd 0 {2,D}
2 *2 Cd 0 {1,D} {3,S} {4,S}
3    H  0 {2,S}
4    H  0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 127,
    label = "Sd_Cds/H/NonDe",
    group = 
"""
1 *1 Sd       0 {2,D}
2 *2 Cd       0 {1,D} {3,S} {4,S}
3    {Cs,O,S} 0 {2,S}
4    H        0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 128,
    label = "Sd_Cds/NonDe2",
    group = 
"""
1 *1 Sd       0 {2,D}
2 *2 Cd       0 {1,D} {3,S} {4,S}
3    {Cs,O,S} 0 {2,S}
4    {Cs,O,S} 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 129,
    label = "Sd_Cds/CsO",
    group = 
"""
1 *1 Sd 0 {2,D}
2 *2 Cd 0 {1,D} {3,S} {4,S}
3    Cs 0 {2,S}
4    O  0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 130,
    label = "Sd_Cds/H/OneDe",
    group = 
"""
1 *1 Sd               0 {2,D}
2 *2 Cd               0 {1,D} {3,S} {4,S}
3    {Cd,Ct,Cb,CO,CS} 0 {2,S}
4    H                0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 131,
    label = "Sd_Cds/H/Ct",
    group = 
"""
1 *1 Sd 0 {2,D}
2 *2 Cd 0 {1,D} {3,S} {4,S}
3    Ct 0 {2,S}
4    H  0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 132,
    label = "Sd_Cds/H/Cb",
    group = 
"""
1 *1 Sd 0 {2,D}
2 *2 Cd 0 {1,D} {3,S} {4,S}
3    Cb 0 {2,S}
4    H  0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 133,
    label = "Sd_Cds/H/CO",
    group = 
"""
1 *1 Sd 0 {2,D}
2 *2 Cd 0 {1,D} {3,S} {4,S}
3    CO 0 {2,S}
4    H  0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 134,
    label = "Sd_Cds/H/Cd",
    group = 
"""
1 *1 Sd 0 {2,D}
2 *2 Cd 0 {1,D} {3,S} {4,S}
3    Cd 0 {2,S} {5,D}
4    H  0 {2,S}
5    C  0 {3,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 135,
    label = "Sd_Cds/H/CS",
    group = 
"""
1 *1 Sd 0 {2,D}
2 *2 Cd 0 {1,D} {3,S} {4,S}
3    Cd 0 {2,S} {5,D}
4    H  0 {2,S}
5    Sd 0 {3,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 136,
    label = "Sd_Cds/NonDe/OneDe",
    group = 
"""
1 *1 Sd               0 {2,D}
2 *2 Cd               0 {1,D} {3,S} {4,S}
3    {Cd,Ct,Cb,CO,CS} 0 {2,S}
4    {Cs,O,S}         0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 137,
    label = "Sd_Cds/NonDe/Ct",
    group = 
"""
1 *1 Sd       0 {2,D}
2 *2 Cd       0 {1,D} {3,S} {4,S}
3    Ct       0 {2,S}
4    {Cs,O,S} 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 138,
    label = "Sd_Cds/NonDe/Cb",
    group = 
"""
1 *1 Sd       0 {2,D}
2 *2 Cd       0 {1,D} {3,S} {4,S}
3    Cb       0 {2,S}
4    {Cs,O,S} 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 139,
    label = "Sd_Cds/NonDe/CO",
    group = 
"""
1 *1 Sd       0 {2,D}
2 *2 Cd       0 {1,D} {3,S} {4,S}
3    CO       0 {2,S}
4    {Cs,O,S} 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 140,
    label = "Sd_Cds/NonDe/Cd",
    group = 
"""
1 *1 Sd       0 {2,D}
2 *2 Cd       0 {1,D} {3,S} {4,S}
3    Cd       0 {2,S} {5,D}
4    {Cs,O,S} 0 {2,S}
5    C        0 {3,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 141,
    label = "Sd_Cds/NonDe/CS",
    group = 
"""
1 *1 Sd       0 {2,D}
2 *2 Cd       0 {1,D} {3,S} {4,S}
3    Cd       0 {2,S} {5,D}
4    {Cs,O,S} 0 {2,S}
5    Sd       0 {3,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 142,
    label = "Sd_Cds/TwoDe",
    group = 
"""
1 *1 Sd               0 {2,D}
2 *2 Cd               0 {1,D} {3,S} {4,S}
3    {Cd,Ct,Cb,CO,CS} 0 {2,S}
4    {Cd,Ct,Cb,CO,CS} 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 143,
    label = "Sd_Cds/CtCt",
    group = 
"""
1 *1 Sd 0 {2,D}
2 *2 Cd 0 {1,D} {3,S} {4,S}
3    Ct 0 {2,S}
4    Ct 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 144,
    label = "Sd_Cds/CtCb",
    group = 
"""
1 *1 Sd 0 {2,D}
2 *2 Cd 0 {1,D} {3,S} {4,S}
3    Ct 0 {2,S}
4    Cb 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 145,
    label = "Sd_Cds/CtCO",
    group = 
"""
1 *1 Sd 0 {2,D}
2 *2 Cd 0 {1,D} {3,S} {4,S}
3    Ct 0 {2,S}
4    CO 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 146,
    label = "Sd_Cds/CbCb",
    group = 
"""
1 *1 Sd 0 {2,D}
2 *2 Cd 0 {1,D} {3,S} {4,S}
3    Cb 0 {2,S}
4    Cb 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 147,
    label = "Sd_Cds/CbCO",
    group = 
"""
1 *1 Sd 0 {2,D}
2 *2 Cd 0 {1,D} {3,S} {4,S}
3    Cb 0 {2,S}
4    CO 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 148,
    label = "Sd_Cds/COCO",
    group = 
"""
1 *1 Sd 0 {2,D}
2 *2 Cd 0 {1,D} {3,S} {4,S}
3    CO 0 {2,S}
4    CO 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 149,
    label = "Sd_Cds/CdCt",
    group = 
"""
1 *1 Sd 0 {2,D}
2 *2 Cd 0 {1,D} {3,S} {4,S}
3    Cd 0 {2,S} {5,D}
4    Ct 0 {2,S}
5    C  0 {3,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 150,
    label = "Sd_Cds/CtCS",
    group = 
"""
1 *1 Sd 0 {2,D}
2 *2 Cd 0 {1,D} {3,S} {4,S}
3    Ct 0 {2,S}
4    Cd 0 {2,S} {5,D}
5    Sd 0 {4,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 151,
    label = "Sd_Cds/CdCb",
    group = 
"""
1 *1 Sd 0 {2,D}
2 *2 Cd 0 {1,D} {3,S} {4,S}
3    Cd 0 {2,S} {5,D}
4    Cb 0 {2,S}
5    C  0 {3,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 152,
    label = "Sd_Cds/CbCS",
    group = 
"""
1 *1 Sd 0 {2,D}
2 *2 Cd 0 {1,D} {3,S} {4,S}
3    Cb 0 {2,S}
4    Cd 0 {2,S} {5,D}
5    Sd 0 {4,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 153,
    label = "Sd_Cds/CdCO",
    group = 
"""
1 *1 Sd 0 {2,D}
2 *2 Cd 0 {1,D} {3,S} {4,S}
3    Cd 0 {2,S} {5,D}
4    CO 0 {2,S}
5    C  0 {3,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 154,
    label = "Sd_Cds/COCS",
    group = 
"""
1 *1 Sd 0 {2,D}
2 *2 Cd 0 {1,D} {3,S} {4,S}
3    CO 0 {2,S}
4    Cd 0 {2,S} {5,D}
5    Sd 0 {4,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 155,
    label = "Sd_Cds/CdCd",
    group = 
"""
1 *1 Sd 0 {2,D}
2 *2 Cd 0 {1,D} {3,S} {4,S}
3    Cd 0 {2,S} {5,D}
4    Cd 0 {2,S} {6,D}
5    C  0 {3,D}
6    C  0 {4,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 156,
    label = "Sd_Cds/CdCS",
    group = 
"""
1 *1 Sd 0 {2,D}
2 *2 Cd 0 {1,D} {3,S} {4,S}
3    Cd 0 {2,S} {6,D}
4    Cd 0 {2,S} {5,D}
5    Sd 0 {4,D}
6    C  0 {3,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 157,
    label = "Sd_Cds/CSCS",
    group = 
"""
1 *1 Sd 0 {2,D}
2 *2 Cd 0 {1,D} {3,S} {4,S}
3    Cd 0 {2,S} {5,D}
4    Cd 0 {2,S} {6,D}
5    Sd 0 {3,D}
6    Sd 0 {4,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 158,
    label = "OCddO",
    group = 
"""
1 *1 Od  0 {2,D}
2 *2 Cdd 0 {1,D} {3,D}
3    Od  0 {2,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 159,
    label = "OSiddO",
    group = 
"""
1 *1 Od   0 {2,D}
2 *2 Sidd 0 {1,D} {3,D}
3    Od   0 {2,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 311,
    label = "Od_N",
    group = 
"""
1 *1 Od 0 {2,D}
2 *2 N  0 {1,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 312,
    label = "Od_N3d",
    group = 
"""
1 *1 Od  0 {2,D}
2 *2 N3d 0 {1,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 313,
    label = "Od_N5d",
    group = 
"""
1 *1 Od  0 {2,D}
2 *2 N5d 0 {1,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 314,
    label = "N_R",
    group = "OR{N3_R, N5t_R}",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 315,
    label = "N3_R",
    group = "OR{N3d_R, N3t_R}",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 316,
    label = "N3d_R",
    group = 
"""
1 *1 N3d 0 {2,D}
2 *2 R!H 0 {1,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 317,
    label = "N3d_C",
    group = 
"""
1 *1 N3d      0 {2,D}
2 *2 {Cd,Cdd} 0 {1,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 325,
    label = "N3d_Cdd",
    group = 
"""
1 *1 N3d 0 {2,D}
2 *2 Cdd 0 {1,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 318,
    label = "N3d_Cds",
    group = 
"""
1 *1 N3d 0 {2,D}
2 *2 Cd  0 {1,D} {3,S} {4,S}
3    R   0 {2,S}
4    R   0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 319,
    label = "N3d/H_Cds",
    group = 
"""
1 *1 N3d 0 {2,D} {5,S}
2 *2 Cd  0 {1,D} {3,S} {4,S}
3    R   0 {2,S}
4    R   0 {2,S}
5    H   0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 320,
    label = "N3d/H_Cds/H2",
    group = 
"""
1 *1 N3d 0 {2,D} {5,S}
2 *2 Cd  0 {1,D} {3,S} {4,S}
3    H   0 {2,S}
4    H   0 {2,S}
5    H   0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 321,
    label = "N3d/H_Cds_sec",
    group = 
"""
1 *1 N3d 0 {2,D} {5,S}
2 *2 Cd  0 {1,D} {3,S} {4,S}
3    R!H 0 {2,S}
4    H   0 {2,S}
5    H   0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 322,
    label = "N3d/H_Cds_ter",
    group = 
"""
1 *1 N3d 0 {2,D} {5,S}
2 *2 Cd  0 {1,D} {3,S} {4,S}
3    R!H 0 {2,S}
4    R!H 0 {2,S}
5    H   0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 323,
    label = "N3d/NonDe_Cds",
    group = 
"""
1 *1 N3d         0 {2,D} {5,S}
2 *2 Cd          0 {1,D} {3,S} {4,S}
3    R!H         0 {2,S}
4    R!H         0 {2,S}
5    {Cs,N3s,Os} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 324,
    label = "N3d/OneDe_Cds",
    group = 
"""
1 *1 N3d                   0 {2,D} {5,S}
2 *2 Cd                    0 {1,D} {3,S} {4,S}
3    R!H                   0 {2,S}
4    R!H                   0 {2,S}
5    {Cd,Ct,Cb,CO,N3d,N5d} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 326,
    label = "N3d_Od",
    group = 
"""
1 *1 N3d 0 {2,D}
2 *2 Od  0 {1,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 327,
    label = "N3d/H_Od",
    group = 
"""
1 *1 N3d 0 {2,D} {3,S}
2 *2 Od  0 {1,D}
3    H   0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 328,
    label = "N3d/NonDe_Od",
    group = 
"""
1 *1 N3d         0 {2,D} {3,S}
2 *2 Od          0 {1,D}
3    {Cs,N3s,Os} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 329,
    label = "N3d/OneDe_Od",
    group = 
"""
1 *1 N3d                   0 {2,D} {3,S}
2 *2 Od                    0 {1,D}
3    {Cd,Ct,Cb,CO,N3d,N5d} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 330,
    label = "N3d_N",
    group = 
"""
1 *1 N3d 0 {2,D}
2 *2 N   0 {1,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 330,
    label = "N3d_N3d",
    group = 
"""
1 *1 N3d 0 {2,D}
2 *2 N3d 0 {1,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 331,
    label = "N3d/H_N3d",
    group = 
"""
1 *1 N3d 0 {2,D} {3,S}
2 *2 N3d 0 {1,D}
3    H   0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 332,
    label = "N3d/H_N3d/H",
    group = 
"""
1 *1 N3d 0 {2,D} {3,S}
2 *2 N3d 0 {1,D} {4,S}
3    H   0 {1,S}
4    H   0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 333,
    label = "N3d/H_N3d/NonDe",
    group = 
"""
1 *1 N3d         0 {2,D} {3,S}
2 *2 N3d         0 {1,D} {4,S}
3    H           0 {1,S}
4    {Cs,N3s,Os} 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 334,
    label = "N3d/H_N3d/OneDe",
    group = 
"""
1 *1 N3d                   0 {2,D} {3,S}
2 *2 N3d                   0 {1,D} {4,S}
3    H                     0 {1,S}
4    {Cd,Ct,Cb,CO,N3d,N5d} 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 335,
    label = "N3d/NonDe_N3d",
    group = 
"""
1 *1 N3d         0 {2,D} {3,S}
2 *2 N3d         0 {1,D}
3    {Cs,N3s,Os} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 336,
    label = "N3d/OneDe_N3d",
    group = 
"""
1 *1 N3d                   0 {2,D} {3,S}
2 *2 N3d                   0 {1,D}
3    {Cd,Ct,Cb,CO,N3d,N5d} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 337,
    label = "N3d_N5",
    group = 
"""
1 *1 N3d       0 {2,D}
2 *2 {N5d,N5t} 0 {1,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 338,
    label = "N3t_R",
    group = 
"""
1 *1 N3t 0 {2,T}
2 *2 R!H 0 {1,T}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 339,
    label = "N3t_Ct",
    group = 
"""
1 *1 N3t 0 {2,T}
2 *2 Ct  0 {1,T}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 339,
    label = "N3t_Ct/H",
    group = 
"""
1 *1 N3t 0 {2,T}
2 *2 Ct  0 {1,T} {3,S}
3    H   0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 340,
    label = "N3t_Ct/NonDe",
    group = 
"""
1 *1 N3t         0 {2,T}
2 *2 Ct          0 {1,T} {3,S}
3    {Cs,N3s,Os} 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 341,
    label = "N3t_Ct/OneDe",
    group = 
"""
1 *1 N3t                   0 {2,T}
2 *2 Ct                    0 {1,T} {3,S}
3    {Cd,Ct,Cb,CO,N3d,N5d} 0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 342,
    label = "N3t_N3t",
    group = 
"""
1 *1 N3t 0 {2,T}
2 *2 N3t 0 {1,T}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 343,
    label = "N5t_R",
    group = 
"""
1 *1 N5t 0 {2,T}
2 *2 R   0 {1,T}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 393,
    label = "Y_1centerquadrad",
    group = "OR{C_quintet, C_triplet, C_singlet}",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 383,
    label = "C_quintet",
    group = 
"""
1 *3 C 4V
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 384,
    label = "C_triplet",
    group = 
"""
1 *3 C 4T
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 385,
    label = "C_singlet",
    group = 
"""
1 *3 C 4S
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 344,
    label = "Y_1centertrirad",
    group = "OR{N_atom_quartet, N_atom_doublet, CH_quartet, CH_doublet}",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 386,
    label = "N_atom_quartet",
    group = 
"""
1 *3 N 3Q
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 387,
    label = "N_atom_doublet",
    group = 
"""
1 *3 N 3D
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 388,
    label = "CH_quartet",
    group = 
"""
1 *3 C 3Q {2,S}
2    H 0  {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 389,
    label = "CH_doublet",
    group = 
"""
1 *3 C 3D {2,S}
2    H 0  {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 347,
    label = "Y_2centerbirad",
    group = "OR{O2b, C2b}",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 348,
    label = "O2b",
    group = 
"""
1 *3 Os 1 {2,S}
2    Os 1 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 349,
    label = "C2b",
    group = 
"""
1 *3 Ct 1 {2,S}
2    Ct 1 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 350,
    label = "Y_1centerbirad",
    group = 
"""
1 *3 R!H {2S,2T}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 352,
    label = "O_atom_triplet",
    group = 
"""
1 *3 O 2T
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 351,
    label = "CO_birad",
    group = 
"""
1 *3 C  {2S,2T} {2,D}
2    Od 0       {1,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 354,
    label = "NH_triplet",
    group = 
"""
1 *3 N3s 2T {2,S}
2    H   0  {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 353,
    label = "CH2_triplet",
    group = 
"""
1 *3 C 2T {2,S} {3,S}
2    H 0  {1,S}
3    H 0  {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = -1,
    label = "Y_rad",
    group = 
"""
1 *3 R 1
""",
    distances = DistanceData(
        distances = {'d12': 0.0, 'd13': -0.0, 'd23': 0.0},
        uncertainties = {'d12': 0.010297, 'd13': 0.033216, 'd23': 0.049111},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 13 distances.
[<Entry index=28 label="Cd/NonDe2_Cd/H2">, <Entry index=192 label="C_methyl">]
[<Entry index=9 label="Cd/H2_Cd/NonDe2">, <Entry index=192 label="C_methyl">]
[<Entry index=7 label="Cd/H2_Cd/H/NonDe">, <Entry index=192 label="C_methyl">]
[<Entry index=101 label="CS/CsCs_S">, <Entry index=192 label="C_methyl">]
[<Entry index=94 label="CS/H2_S">, <Entry index=192 label="C_methyl">]
[<Entry index=87 label="CO/H2_O">, <Entry index=192 label="C_methyl">]
[<Entry index=90 label="CO/NonDe2_O">, <Entry index=192 label="C_methyl">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=160 label="H_rad">]
[<Entry index=119 label="OCO">, <Entry index=192 label="C_methyl">]
[<Entry index=88 label="CO/H/NonDe_O">, <Entry index=192 label="C_methyl">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=192 label="C_methyl">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 160,
    label = "H_rad",
    group = 
"""
1 *3 H 1
""",
    distances = DistanceData(
        distances = {'d12': -0.023717, 'd13': -0.01882, 'd23': -0.014772},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=160 label="H_rad">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 364,
    label = "N3_rad",
    group = 
"""
1 *3 {N3s,N3d} 1
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 365,
    label = "N3s_rad",
    group = 
"""
1 *3 N3s 1
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 366,
    label = "NH2_rad",
    group = 
"""
1 *3 N3s 1 {2,S} {3,S}
2    H   0 {1,S}
3    H   0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 367,
    label = "N3s_rad_pri",
    group = 
"""
1 *3 N3s 1 {2,S} {3,S}
2    R!H 0 {1,S}
3    H   0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 368,
    label = "N3s_rad/H/NonDe",
    group = 
"""
1 *3 N3s         1 {2,S} {3,S}
2    {Cs,N3s,Os} 0 {1,S}
3    H           0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 369,
    label = "N3s_rad/H/NonDeC",
    group = 
"""
1 *3 N3s 1 {2,S} {3,S}
2    Cs  0 {1,S}
3    H   0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 370,
    label = "N3s_rad/H/NonDeO",
    group = 
"""
1 *3 N3s 1 {2,S} {3,S}
2    Os  0 {1,S}
3    H   0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 371,
    label = "N3s_rad/H/NonDeN",
    group = 
"""
1 *3 N3s 1 {2,S} {3,S}
2    N3s 0 {1,S}
3    H   0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 372,
    label = "N3s_rad/H/OneDe",
    group = 
"""
1 *3 N3s                      1 {2,S} {3,S}
2    {Cd,Ct,Cb,CO,CS,N3d,N5d} 0 {1,S}
3    H                        0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 373,
    label = "N3s_rad_sec",
    group = 
"""
1 *3 N3s 1 {2,S} {3,S}
2    R!H 0 {1,S}
3    R!H 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 374,
    label = "N3s_rad/NonDe2",
    group = 
"""
1 *3 N3s         1 {2,S} {3,S}
2    {Cs,N3s,Os} 0 {1,S}
3    {Cs,N3s,Os} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 375,
    label = "N3s_rad/OneDe",
    group = 
"""
1 *3 N3s                      1 {2,S} {3,S}
2    {Cd,Ct,Cb,CO,CS,N3d,N5d} 0 {1,S}
3    {Cs,N3s,Os}              0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 376,
    label = "N3s_rad/TwoDe",
    group = 
"""
1 *3 N3s                      1 {2,S} {3,S}
2    {Cd,Ct,Cb,CO,CS,N3d,N5d} 0 {1,S}
3    {Cd,Ct,Cb,CO,CS,N3d,N5d} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 377,
    label = "N3d_rad",
    group = 
"""
1 *3 N3d 1
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 378,
    label = "N3d_rad/C",
    group = 
"""
1 *3 N3d 1 {2,D}
2    C   0 {1,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 379,
    label = "N3d_rad/O",
    group = 
"""
1 *3 N3d 1 {2,D}
2    Od  0 {1,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 380,
    label = "N3d_rad/N",
    group = 
"""
1 *3 N3d 1 {2,D}
2    N   0 {1,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 381,
    label = "N5_rad",
    group = 
"""
1 *3 {N5d,N5dd,N5t} 1
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 382,
    label = "N5d_rad",
    group = 
"""
1 *3 N5d 1
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 161,
    label = "Ct_rad",
    group = 
"""
1 *3 Ct       1 {2,T}
2    {Ct,N3t} 0 {1,T}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 355,
    label = "Ct_rad/Ct",
    group = 
"""
1 *3 Ct 1 {2,T}
2    Ct 0 {1,T}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 356,
    label = "Ct_rad/N3t",
    group = 
"""
1 *3 Ct  1 {2,T}
2    N3t 0 {1,T}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 162,
    label = "O_rad",
    group = 
"""
1 *3 O 1 {2,S}
2    R 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 163,
    label = "O_pri_rad",
    group = 
"""
1 *3 O 1 {2,S}
2    H 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 164,
    label = "O_sec_rad",
    group = 
"""
1 *3 O   1 {2,S}
2    R!H 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 165,
    label = "O_rad/NonDe",
    group = 
"""
1 *3 O        1 {2,S}
2    {Cs,O,S} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 166,
    label = "O_rad/NonDeO",
    group = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 167,
    label = "O_rad/NonDeC",
    group = 
"""
1 *3 O  1 {2,S}
2    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 357,
    label = "O_rad/NonDeN",
    group = 
"""
1 *3 O   1 {2,S}
2    N3s 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 358,
    label = "O_rad/OneDe",
    group = 
"""
1 *3 O                     1 {2,S}
2    {Cd,Ct,Cb,CO,N3d,N5d} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 359,
    label = "O_rad/OneDeN",
    group = 
"""
1 *3 O         1 {2,S}
2    {N3d,N5d} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 360,
    label = "O_rad/NO",
    group = 
"""
1 *3 O         1 {2,S}
2    {N3d,N5d} 0 {1,S} {3,D}
3    Od        0 {2,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 169,
    label = "S_rad",
    group = 
"""
1 *3 Ss 1 {2,S}
2    R  0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 170,
    label = "S_pri_rad",
    group = 
"""
1 *3 Ss 1 {2,S}
2    H  0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 171,
    label = "S_sec_rad",
    group = 
"""
1 *3 Ss  1 {2,S}
2    R!H 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 172,
    label = "S_rad/NonDeC",
    group = 
"""
1 *3 Ss 1 {2,S}
2    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 173,
    label = "S_rad/NonDeS",
    group = 
"""
1 *3 Ss 1 {2,S}
2    Ss 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 174,
    label = "S_rad/OneDe",
    group = 
"""
1 *3 Ss               1 {2,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 175,
    label = "S_rad/Ct",
    group = 
"""
1 *3 Ss 1 {2,S}
2    Ct 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 176,
    label = "S_rad/Cb",
    group = 
"""
1 *3 Ss 1 {2,S}
2    Cb 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 177,
    label = "S_rad/CO",
    group = 
"""
1 *3 Ss 1 {2,S}
2    CO 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 178,
    label = "S_rad/Cd",
    group = 
"""
1 *3 Ss 1 {2,S}
2    Cd 0 {1,S} {3,D}
3    C  0 {2,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 179,
    label = "S_rad/CS",
    group = 
"""
1 *3 Ss 1 {2,S}
2    Cd 0 {1,S} {3,D}
3    S  0 {2,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 180,
    label = "Cd_rad",
    group = 
"""
1 *3 Cd 1 {2,D} {3,S}
2    Cd 0 {1,D}
3    R  0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 181,
    label = "Cd_pri_rad",
    group = 
"""
1 *3 Cd 1 {2,D} {3,S}
2    Cd 0 {1,D}
3    H  0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 182,
    label = "Cd_sec_rad",
    group = 
"""
1 *3 Cd  1 {2,D} {3,S}
2    Cd  0 {1,D}
3    R!H 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 183,
    label = "Cd_rad/NonDe",
    group = 
"""
1 *3 Cd       1 {2,D} {3,S}
2    Cd       0 {1,D}
3    {Cs,O,S} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 184,
    label = "Cd_rad/OneDe",
    group = 
"""
1 *3 Cd               1 {2,D} {3,S}
2    Cd               0 {1,D}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 185,
    label = "Cb_rad",
    group = 
"""
1 *3 Cb       1 {2,B} {3,B}
2    {Cb,Cbf} 0 {1,B}
3    {Cb,Cbf} 0 {1,B}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 186,
    label = "CO_rad",
    group = 
"""
1 *3 C 1 {2,D} {3,S}
2    O 0 {1,D}
3    R 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 187,
    label = "CO_pri_rad",
    group = 
"""
1 *3 C 1 {2,D} {3,S}
2    O 0 {1,D}
3    H 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 188,
    label = "CO_sec_rad",
    group = 
"""
1 *3 C   1 {2,D} {3,S}
2    O   0 {1,D}
3    R!H 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 189,
    label = "CO_rad/NonDe",
    group = 
"""
1 *3 C            1 {2,D} {3,S}
2    O            0 {1,D}
3    {Cs,O,S,N3s} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 190,
    label = "CO_rad/OneDe",
    group = 
"""
1 *3 C                1 {2,D} {3,S}
2    O                0 {1,D}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 191,
    label = "Cs_rad",
    group = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    R 0 {1,S}
3    R 0 {1,S}
4    R 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.002523, 'd13': 0.002002, 'd23': 0.001572},
        uncertainties = {'d12': 0.008762, 'd13': 0.033739, 'd23': 0.039877},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 12 distances.
[<Entry index=28 label="Cd/NonDe2_Cd/H2">, <Entry index=192 label="C_methyl">]
[<Entry index=9 label="Cd/H2_Cd/NonDe2">, <Entry index=192 label="C_methyl">]
[<Entry index=7 label="Cd/H2_Cd/H/NonDe">, <Entry index=192 label="C_methyl">]
[<Entry index=101 label="CS/CsCs_S">, <Entry index=192 label="C_methyl">]
[<Entry index=94 label="CS/H2_S">, <Entry index=192 label="C_methyl">]
[<Entry index=87 label="CO/H2_O">, <Entry index=192 label="C_methyl">]
[<Entry index=90 label="CO/NonDe2_O">, <Entry index=192 label="C_methyl">]
[<Entry index=119 label="OCO">, <Entry index=192 label="C_methyl">]
[<Entry index=88 label="CO/H/NonDe_O">, <Entry index=192 label="C_methyl">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=192 label="C_methyl">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 192,
    label = "C_methyl",
    group = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.002523, 'd13': 0.002002, 'd23': 0.001572},
        uncertainties = {'d12': 0.008762, 'd13': 0.033739, 'd23': 0.039877},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 12 distances.
[<Entry index=28 label="Cd/NonDe2_Cd/H2">, <Entry index=192 label="C_methyl">]
[<Entry index=9 label="Cd/H2_Cd/NonDe2">, <Entry index=192 label="C_methyl">]
[<Entry index=7 label="Cd/H2_Cd/H/NonDe">, <Entry index=192 label="C_methyl">]
[<Entry index=101 label="CS/CsCs_S">, <Entry index=192 label="C_methyl">]
[<Entry index=94 label="CS/H2_S">, <Entry index=192 label="C_methyl">]
[<Entry index=87 label="CO/H2_O">, <Entry index=192 label="C_methyl">]
[<Entry index=90 label="CO/NonDe2_O">, <Entry index=192 label="C_methyl">]
[<Entry index=119 label="OCO">, <Entry index=192 label="C_methyl">]
[<Entry index=88 label="CO/H/NonDe_O">, <Entry index=192 label="C_methyl">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=192 label="C_methyl">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 193,
    label = "C_pri_rad",
    group = 
"""
1 *3 C   1 {2,S} {3,S} {4,S}
2    H   0 {1,S}
3    H   0 {1,S}
4    R!H 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 194,
    label = "C_rad/H2/Cs",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 195,
    label = "C_rad/H2/Cd",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cd 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 196,
    label = "C_rad/H2/Ct",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Ct 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 197,
    label = "C_rad/H2/Cb",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    Cb 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 198,
    label = "C_rad/H2/CO",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    H  0 {1,S}
4    CO 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 199,
    label = "C_rad/H2/O",
    group = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    O 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 361,
    label = "C_rad/H2/N",
    group = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    N 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 200,
    label = "C_sec_rad",
    group = 
"""
1 *3 C   1 {2,S} {3,S} {4,S}
2    H   0 {1,S}
3    R!H 0 {1,S}
4    R!H 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 201,
    label = "C_rad/H/NonDeC",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 202,
    label = "C_rad/H/NonDeO",
    group = 
"""
1 *3 C        1 {2,S} {3,S} {4,S}
2    H        0 {1,S}
3    O        0 {1,S}
4    {Cs,O,S} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 203,
    label = "C_rad/H/CsO",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
4    O  0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 204,
    label = "C_rad/H/O2",
    group = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    O 0 {1,S}
4    O 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 205,
    label = "C_rad/H/NonDeS",
    group = 
"""
1 *3 C      1 {2,S} {3,S} {4,S}
2    H      0 {1,S}
3    S      0 {1,S}
4    {Cs,S} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 206,
    label = "C_rad/H/CsS",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    H  0 {1,S}
3    S  0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 207,
    label = "C_rad/H/S2",
    group = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    S 0 {1,S}
4    S 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 362,
    label = "C_rad/H/NonDeN",
    group = 
"""
1 *3 C   1 {2,S} {3,S} {4,S}
2    H   0 {1,S}
3    N3s 0 {1,S}
4    R   0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 208,
    label = "C_rad/H/OneDe",
    group = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cs,O,S}         0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 209,
    label = "C_rad/H/OneDeC",
    group = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    Cs               0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 210,
    label = "C_rad/H/OneDeO",
    group = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    O                0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 363,
    label = "C_rad/H/OneDeN",
    group = 
"""
1 *3 C                        1 {2,S} {3,S} {4,S}
2    H                        0 {1,S}
3    {Cd,Ct,Cb,CO,CS,N3d,N5d} 0 {1,S}
4    N                        0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 211,
    label = "C_rad/H/TwoDe",
    group = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    H                0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 212,
    label = "C_ter_rad",
    group = 
"""
1 *3 C   1 {2,S} {3,S} {4,S}
2    R!H 0 {1,S}
3    R!H 0 {1,S}
4    R!H 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 213,
    label = "C_rad/NonDeC",
    group = 
"""
1 *3 C        1 {2,S} {3,S} {4,S}
2    {Cs,O,S} 0 {1,S}
3    {Cs,O,S} 0 {1,S}
4    {Cs,O,S} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 214,
    label = "C_rad/Cs3",
    group = 
"""
1 *3 C  1 {2,S} {3,S} {4,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 215,
    label = "C_rad/NDMustO",
    group = 
"""
1 *3 C        1 {2,S} {3,S} {4,S}
2    O        0 {1,S}
3    {Cs,O,S} 0 {1,S}
4    {Cs,O,S} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 216,
    label = "C_rad/OneDe",
    group = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
3    {Cs,O,S}         0 {1,S}
4    {Cs,O,S}         0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 217,
    label = "C_rad/Cs2",
    group = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
3    Cs               0 {1,S}
4    Cs               0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 218,
    label = "C_rad/ODMustO",
    group = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
3    O                0 {1,S}
4    {Cs,O,S}         0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 219,
    label = "C_rad/TwoDe",
    group = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cs,O,S}         0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 220,
    label = "C_rad/Cs",
    group = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    Cs               0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 221,
    label = "C_rad/TDMustO",
    group = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    O                0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 222,
    label = "C_rad/ThreeDe",
    group = 
"""
1 *3 C                1 {2,S} {3,S} {4,S}
2    {Cd,Ct,Cb,CO,CS} 0 {1,S}
3    {Cd,Ct,Cb,CO,CS} 0 {1,S}
4    {Cd,Ct,Cb,CO,CS} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = 223,
    label = "Cd_pri_rad-Cdd/Cd",
    group = 
"""
1 *3 Cd  1 {2,D} {3,S}
2    Cdd 0 {1,D} {4,D}
3    H   0 {1,S}
4    Cd  0 {2,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

entry(
    index = -1,
    label = "Y_birad",
    group = 
"""
1 *3 R {2S,2T}
""",
    kinetics = {},
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from current kinetics groups."""),
    ],
)

tree(
"""
L1: XZ
    L2: CZ
        L3: Cd_Cd
            L4: Cd/H2
                L5: Cd/H2_Cd/H2
                L5: Cd/H2_Cd/H/NonDe
                L5: Cd/H2_Cd/H/OneDe
                L5: Cd/H2_Cd/NonDe2
                L5: Cd/H2_Cd/NonDe/OneDe
                L5: Cd/H2_Cd/TwoDe
            L4: Cd/H/NonDe
                L5: Cd/H/NonDe_Cd/H2
                L5: Cd/H/NonDe_Cd/H/NonDe
                    L6: Cd/H/Os_Cd/H/Cs
                L5: Cd/H/NonDe_Cd/H/OneDe
                L5: Cd/H/NonDe_Cd/NonDe2
                L5: Cd/H/NonDe_Cd/NonDe/OneDe
                L5: Cd/H/NonDe_Cd/TwoDe
            L4: Cd/H/OneDe
                L5: Cd/H/OneDe_Cd/H2
                L5: Cd/H/OneDe_Cd/H/NonDe
                L5: Cd/H/OneDe_Cd/H/OneDe
                L5: Cd/H/OneDe_Cd/NonDe2
                L5: Cd/H/OneDe_Cd/NonDe/OneDe
                L5: Cd/H/OneDe_Cd/TwoDe
            L4: Cd/NonDe2
                L5: Cd/NonDe2_Cd/H2
                L5: Cd/NonDe2_Cd/H/NonDe
                L5: Cd/NonDe2_Cd/H/OneDe
                L5: Cd/NonDe2_Cd/NonDe2
                L5: Cd/NonDe2_Cd/NonDe/OneDe
                L5: Cd/NonDe2_Cd/TwoDe
            L4: Cd/NonDe/OneDe
                L5: Cd/NonDe/OneDe_Cd/H2
                L5: Cd/NonDe/OneDe_Cd/H/NonDe
                L5: Cd/NonDe/OneDe_Cd/H/OneDe
                L5: Cd/NonDe/OneDe_Cd/NonDe2
                L5: Cd/NonDe/OneDe_Cd/NonDe/OneDe
                L5: Cd/NonDe/OneDe_Cd/TwoDe
            L4: Cd/TwoDe
                L5: Cd/TwoDe_Cd/H2
                L5: Cd/TwoDe_Cd/H/NonDe
                L5: Cd/TwoDe_Cd/H/OneDe
                L5: Cd/TwoDe_Cd/NonDe2
                L5: Cd/TwoDe_Cd/NonDe/OneDe
                L5: Cd/TwoDe_Cd/TwoDe
        L3: Cd_Cdd
            L4: Cd_Ca
                L5: Cd/H2_Ca
                L5: Cd/H/NonDe_Ca
                L5: Cd/H/OneDe_Ca
                L5: Cd/NonDe2_Ca
                L5: Cd/NonDe/OneDe_Ca
                L5: Cd/TwoDe_Ca
            L4: Cd_Ck
                L5: Cd/H2_Ck
                L5: Cd/H/NonDe_Ck
                L5: Cd/H/OneDe_Ck
                L5: Cd/NonDe2_Ck
                L5: Cd/NonDe/OneDe_Ck
                L5: Cd/TwoDe_Ck
        L3: Cdd_Cd
            L4: Ca_Cd
                L5: Ca_Cd/H2
                L5: Ca_Cd/H/NonDe
                L5: Ca_Cd/H/OneDe
                L5: Ca_Cd/NonDe2
                L5: Ca_Cd/NonDe/OneDe
                L5: Ca_Cd/TwoDe
            L4: Ck_Cd
                L5: Ck_Cd/H2
                L5: Ck_Cd/H/NonDe
                L5: Ck_Cd/H/OneDe
                L5: Ck_Cd/NonDe2
                L5: Ck_Cd/NonDe/OneDe
                L5: Ck_Cd/TwoDe
        L3: Cdd_Cdd
            L4: Ca_Ca
            L4: Ck_Ck
            L4: Ca_Ck
            L4: Ck_Ca
        L3: Cdd_Sd
            L4: CS2
            L4: CS_O
        L3: CO_O
            L4: CO/H2_O
            L4: CO/H/NonDe_O
            L4: CO/H/OneDe_O
            L4: CO/NonDe2_O
            L4: CO/NonDe/OneDe_O
            L4: CO/TwoDe_O
        L3: CS_S
            L4: CS/H2_S
            L4: CS/H/NonDe_S
                L5: CS/H/Cs_S
                L5: CS/H/Os_S
                L5: CS/H/Ss_S
            L4: CS/H/OneDe_S
            L4: CS/NonDe2_S
                L5: CS/CsCs_S
                L5: CS/CsOs_S
                L5: CS/CsSs_S
            L4: CS/NonDe/OneDe_S
            L4: CS/TwoDe_S
        L3: Ct_Ct
            L4: Ct/H_Ct/H
            L4: Ct/H_Ct/NonDe
            L4: Ct/H_Ct/OneDe
            L4: Ct/NonDe_Ct/H
            L4: Ct/NonDe_Ct/NonDe
            L4: Ct/NonDe_Ct/OneDe
            L4: Ct/OneDe_Ct/H
            L4: Ct/OneDe_Ct/NonDe
            L4: Ct/OneDe_Ct/OneDe
        L3: Ct_N
            L4: Ct_N3t
                L5: Ct_N5t
                L5: Ct/H_N3t
                L5: Ct/NonDe_N3t
                L5: Ct/OneDe_N3t
        L3: Cds_N
            L4: Cds_N3d
                L5: Cds/H2_N3d
                L5: Cds_sec_N3d
                L5: Cds_ter_N3d
        L3: Cdd_Od
            L4: CO2
            L4: Ck_O
    L2: OCO
    L2: OSi
    L2: SZ
        L3: Sd_Cdd
            L4: Sd_Cdd/Sd
            L4: Sd_Cdd/Od
        L3: Sd_Cds
            L4: Sd_Cds/H2
            L4: Sd_Cds/H/NonDe
            L4: Sd_Cds/NonDe2
                L5: Sd_Cds/CsO
            L4: Sd_Cds/H/OneDe
                L5: Sd_Cds/H/Ct
                L5: Sd_Cds/H/Cb
                L5: Sd_Cds/H/CO
                L5: Sd_Cds/H/Cd
                L5: Sd_Cds/H/CS
            L4: Sd_Cds/NonDe/OneDe
                L5: Sd_Cds/NonDe/Ct
                L5: Sd_Cds/NonDe/Cb
                L5: Sd_Cds/NonDe/CO
                L5: Sd_Cds/NonDe/Cd
                L5: Sd_Cds/NonDe/CS
            L4: Sd_Cds/TwoDe
                L5: Sd_Cds/CtCt
                L5: Sd_Cds/CtCb
                L5: Sd_Cds/CtCO
                L5: Sd_Cds/CbCb
                L5: Sd_Cds/CbCO
                L5: Sd_Cds/COCO
                L5: Sd_Cds/CdCt
                L5: Sd_Cds/CtCS
                L5: Sd_Cds/CdCb
                L5: Sd_Cds/CbCS
                L5: Sd_Cds/CdCO
                L5: Sd_Cds/COCS
                L5: Sd_Cds/CdCd
                L5: Sd_Cds/CdCS
                L5: Sd_Cds/CSCS
    L2: OCddO
    L2: OSiddO
    L2: Od_N
        L3: Od_N3d
        L3: Od_N5d
    L2: N_R
        L3: N3_R
            L4: N3d_R
                L5: N3d_C
                    L6: N3d_Cdd
                    L6: N3d_Cds
                        L7: N3d/H_Cds
                            L8: N3d/H_Cds/H2
                            L8: N3d/H_Cds_sec
                            L8: N3d/H_Cds_ter
                        L7: N3d/NonDe_Cds
                        L7: N3d/OneDe_Cds
                L5: N3d_Od
                    L6: N3d/H_Od
                    L6: N3d/NonDe_Od
                    L6: N3d/OneDe_Od
                L5: N3d_N
                    L6: N3d_N3d
                        L7: N3d/H_N3d
                            L8: N3d/H_N3d/H
                            L8: N3d/H_N3d/NonDe
                            L8: N3d/H_N3d/OneDe
                        L7: N3d/NonDe_N3d
                        L7: N3d/OneDe_N3d
                    L6: N3d_N5
            L4: N3t_R
                L5: N3t_Ct
                    L6: N3t_Ct/H
                    L6: N3t_Ct/NonDe
                    L6: N3t_Ct/OneDe
                L5: N3t_N3t
        L3: N5t_R
L1: Y_rad_birad_trirad_quadrad
    L2: Y_1centerquadrad
        L3: C_quintet
        L3: C_triplet
        L3: C_singlet
    L2: Y_1centertrirad
        L3: N_atom_quartet
        L3: N_atom_doublet
        L3: CH_quartet
        L3: CH_doublet
    L2: Y_2centerbirad
        L3: O2b
        L3: C2b
    L2: Y_1centerbirad
        L3: O_atom_triplet
        L3: CO_birad
        L3: NH_triplet
        L3: CH2_triplet
    L2: Y_rad
        L3: H_rad
        L3: N3_rad
            L4: N3s_rad
                L5: NH2_rad
                L5: N3s_rad_pri
                    L6: N3s_rad/H/NonDe
                        L7: N3s_rad/H/NonDeC
                        L7: N3s_rad/H/NonDeO
                        L7: N3s_rad/H/NonDeN
                    L6: N3s_rad/H/OneDe
                L5: N3s_rad_sec
                    L6: N3s_rad/NonDe2
                    L6: N3s_rad/OneDe
                    L6: N3s_rad/TwoDe
            L4: N3d_rad
                L5: N3d_rad/C
                L5: N3d_rad/O
                L5: N3d_rad/N
        L3: N5_rad
            L4: N5d_rad
        L3: Ct_rad
            L4: Ct_rad/Ct
            L4: Ct_rad/N3t
        L3: O_rad
            L4: O_pri_rad
            L4: O_sec_rad
                L5: O_rad/NonDe
                    L6: O_rad/NonDeO
                    L6: O_rad/NonDeC
                    L6: O_rad/NonDeN
                L5: O_rad/OneDe
                    L6: O_rad/OneDeN
                        L7: O_rad/NO
        L3: S_rad
            L4: S_pri_rad
            L4: S_sec_rad
                L5: S_rad/NonDeC
                L5: S_rad/NonDeS
                L5: S_rad/OneDe
                    L6: S_rad/Ct
                    L6: S_rad/Cb
                    L6: S_rad/CO
                    L6: S_rad/Cd
                    L6: S_rad/CS
        L3: Cd_rad
            L4: Cd_pri_rad
            L4: Cd_sec_rad
                L5: Cd_rad/NonDe
                L5: Cd_rad/OneDe
        L3: Cb_rad
        L3: CO_rad
            L4: CO_pri_rad
            L4: CO_sec_rad
                L5: CO_rad/NonDe
                L5: CO_rad/OneDe
        L3: Cs_rad
            L4: C_methyl
            L4: C_pri_rad
                L5: C_rad/H2/Cs
                L5: C_rad/H2/Cd
                L5: C_rad/H2/Ct
                L5: C_rad/H2/Cb
                L5: C_rad/H2/CO
                L5: C_rad/H2/O
                L5: C_rad/H2/N
            L4: C_sec_rad
                L5: C_rad/H/NonDeC
                L5: C_rad/H/NonDeO
                    L6: C_rad/H/CsO
                    L6: C_rad/H/O2
                L5: C_rad/H/NonDeS
                    L6: C_rad/H/CsS
                    L6: C_rad/H/S2
                L5: C_rad/H/NonDeN
                L5: C_rad/H/OneDe
                    L6: C_rad/H/OneDeC
                    L6: C_rad/H/OneDeO
                    L6: C_rad/H/OneDeN
                L5: C_rad/H/TwoDe
            L4: C_ter_rad
                L5: C_rad/NonDeC
                    L6: C_rad/Cs3
                    L6: C_rad/NDMustO
                L5: C_rad/OneDe
                    L6: C_rad/Cs2
                    L6: C_rad/ODMustO
                L5: C_rad/TwoDe
                    L6: C_rad/Cs
                    L6: C_rad/TDMustO
                L5: C_rad/ThreeDe
        L3: Cd_pri_rad-Cdd/Cd
"""
)

