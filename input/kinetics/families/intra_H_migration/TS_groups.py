#!/usr/bin/env python
# encoding: utf-8

name = "intra_H_migration/groups"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 1,
    label = "RnH",
    group = "OR{R2H, R3H, R4H, R5H, R6H, R7H}",
    distances = DistanceData(
        distances = {'d12': 2.27248, 'd13': 1.339657, 'd23': 1.292727},
        uncertainties = {'d12': 0.147038, 'd13': 0.066512, 'd23': 0.060703},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 12 distances.
[<Entry index=26 label="Others-R3H_SS">, <Entry index=181 label="C_rad_out_H/NonDeC">, <Entry index=199 label="O_H_out">]
[<Entry index=125 label="R6H_SSSSS">, <Entry index=181 label="C_rad_out_H/NonDeC">, <Entry index=211 label="Cs_H_out_2H">]
[<Entry index=73 label="R5H_CCCC_O">, <Entry index=167 label="O_rad_out">, <Entry index=210 label="Cs_H_out">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=179 label="C_rad_out_2H">, <Entry index=210 label="Cs_H_out">]
[<Entry index=72 label="R5H_SSSS">, <Entry index=181 label="C_rad_out_H/NonDeC">, <Entry index=211 label="Cs_H_out_2H">]
[<Entry index=125 label="R6H_SSSSS">, <Entry index=191 label="Others-C_rad_out_Cs2">, <Entry index=199 label="O_H_out">]
[<Entry index=38 label="R4H_SSS">, <Entry index=167 label="O_rad_out">, <Entry index=213 label="Cs_H_out_H/NonDeC">]
[<Entry index=164 label="R7H">, <Entry index=179 label="C_rad_out_2H">, <Entry index=199 label="O_H_out">]
[<Entry index=26 label="Others-R3H_SS">, <Entry index=179 label="C_rad_out_2H">, <Entry index=214 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=179 label="C_rad_out_2H">, <Entry index=214 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=38 label="R4H_SSS">, <Entry index=179 label="C_rad_out_2H">, <Entry index=214 label="Cs_H_out_H/(NonDeC/Cs)">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 2,
    label = "Y_rad_out",
    group = 
"""
1 *1 R!H 1
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 3,
    label = "XH_out",
    group = 
"""
1 *2 R!H 0 {2,S}
2 *3 H   0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 4,
    label = "R2H",
    group = 
"""
1 *1 R!H 1 {2,{S,D,B}}
2 *2 R!H 0 {1,{S,D,B}} {3,S}
3 *3 H   0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.780342, 'd13': -0.053695, 'd23': -0.029122},
        uncertainties = {'d12': 0.334568, 'd13': 0.325737, 'd23': 0.404825},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=9 label="Others-R2H_S">, <Entry index=179 label="C_rad_out_2H">, <Entry index=214 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=179 label="C_rad_out_2H">, <Entry index=210 label="Cs_H_out">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 5,
    label = "R2H_S",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *2 R!H 0 {1,S} {3,S}
3 *3 H   0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.780342, 'd13': -0.053695, 'd23': -0.029122},
        uncertainties = {'d12': 0.334568, 'd13': 0.325737, 'd23': 0.404825},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=9 label="Others-R2H_S">, <Entry index=179 label="C_rad_out_2H">, <Entry index=214 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=179 label="C_rad_out_2H">, <Entry index=210 label="Cs_H_out">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 6,
    label = "R2H_S_cy3",
    group = 
"""
1 *1 R!H 1 {2,S} {4,{S,D,B}}
2 *2 R!H 0 {1,S} {3,S} {4,{S,D,B}}
3 *3 H   0 {2,S}
4    R!H 0 {1,{S,D,B}} {2,{S,D,B}}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 7,
    label = "R2H_S_cy4",
    group = 
"""
1 *1 R!H 1 {2,S} {5,{S,D,B}}
2 *2 R!H 0 {1,S} {3,S} {4,{S,D,B}}
3 *3 H   0 {2,S}
4    R!H 0 {2,{S,D,B}} {5,{S,D,B}}
5    R!H 0 {1,{S,D,B}} {4,{S,D,B}}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 8,
    label = "R2H_S_cy5",
    group = 
"""
1 *1 R!H 1 {2,S} {6,{S,D,B}}
2 *2 R!H 0 {1,S} {3,S} {4,{S,D,B}}
3 *3 H   0 {2,S}
4    R!H 0 {2,{S,D,B}} {5,{S,D,B}}
5    R!H 0 {4,{S,D,B}} {6,{S,D,B}}
6    R!H 0 {1,{S,D,B}} {5,{S,D,B}}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 9,
    label = "Others-R2H_S",
    group = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    distances = DistanceData(
        distances = {'d12': -0.780342, 'd13': -0.053695, 'd23': -0.029122},
        uncertainties = {'d12': 0.334568, 'd13': 0.325737, 'd23': 0.404825},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=9 label="Others-R2H_S">, <Entry index=179 label="C_rad_out_2H">, <Entry index=214 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=179 label="C_rad_out_2H">, <Entry index=210 label="Cs_H_out">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 10,
    label = "R2H_D",
    group = 
"""
1 *1 Cd 1 {2,D}
2 *2 Cd 0 {1,D} {3,S}
3 *3 H  0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 11,
    label = "R2H_B",
    group = 
"""
1 *1 Cb 1 {2,B}
2 *2 Cb 0 {1,B} {3,S}
3 *3 H  0 {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 12,
    label = "R3H",
    group = "OR{R3H_SR, R3H_MS, R3H_BB}",
    distances = DistanceData(
        distances = {'d12': -0.114367, 'd13': 0.032614, 'd23': 0.047761},
        uncertainties = {'d12': 2.04679, 'd13': 0.290832, 'd23': 0.213783},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=26 label="Others-R3H_SS">, <Entry index=181 label="C_rad_out_H/NonDeC">, <Entry index=199 label="O_H_out">]
[<Entry index=26 label="Others-R3H_SS">, <Entry index=179 label="C_rad_out_2H">, <Entry index=214 label="Cs_H_out_H/(NonDeC/Cs)">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 13,
    label = "R3H_SR",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,{S,D,T,B}}
3 *2 R!H 0 {2,{S,D,T,B}} {4,S}
4 *3 H   0 {3,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.114367, 'd13': 0.032614, 'd23': 0.047761},
        uncertainties = {'d12': 2.04679, 'd13': 0.290832, 'd23': 0.213783},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=26 label="Others-R3H_SS">, <Entry index=181 label="C_rad_out_H/NonDeC">, <Entry index=199 label="O_H_out">]
[<Entry index=26 label="Others-R3H_SS">, <Entry index=179 label="C_rad_out_2H">, <Entry index=214 label="Cs_H_out_H/(NonDeC/Cs)">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 14,
    label = "R3H_SS",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3 *2 R!H 0 {2,S} {4,S}
4 *3 H   0 {3,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.114367, 'd13': 0.032614, 'd23': 0.047761},
        uncertainties = {'d12': 2.04679, 'd13': 0.290832, 'd23': 0.213783},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=26 label="Others-R3H_SS">, <Entry index=181 label="C_rad_out_H/NonDeC">, <Entry index=199 label="O_H_out">]
[<Entry index=26 label="Others-R3H_SS">, <Entry index=179 label="C_rad_out_2H">, <Entry index=214 label="Cs_H_out_H/(NonDeC/Cs)">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 15,
    label = "R3H_SS_12cy3",
    group = 
"""
1 *1 R!H 1 {2,S} {5,{S,D,B}}
2 *4 R!H 0 {1,S} {3,S} {5,{S,D,B}}
3 *2 R!H 0 {2,S} {4,S}
4 *3 H   0 {3,S}
5    R!H 0 {1,{S,D,B}} {2,{S,D,B}}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 16,
    label = "R3H_SS_23cy3",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S} {5,{S,D,B}}
3 *2 R!H 0 {2,S} {4,S} {5,{S,D,B}}
4 *3 H   0 {3,S}
5    R!H 0 {2,{S,D,B}} {3,{S,D,B}}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 17,
    label = "R3H_SS_12cy4",
    group = 
"""
1 *1 R!H 1 {2,S} {6,{S,D,B}}
2 *4 R!H 0 {1,S} {3,S} {5,{S,D,B}}
3 *2 R!H 0 {2,S} {4,S}
4 *3 H   0 {3,S}
5    R!H 0 {2,{S,D,B}} {6,{S,D,B}}
6    R!H 0 {1,{S,D,B}} {5,{S,D,B}}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 18,
    label = "R3H_SS_23cy4",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S} {6,{S,D,B}}
3 *2 R!H 0 {2,S} {4,S} {5,{S,D,B}}
4 *3 H   0 {3,S}
5    R!H 0 {3,{S,D,B}} {6,{S,D,B}}
6    R!H 0 {2,{S,D,B}} {5,{S,D,B}}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 19,
    label = "R3H_SS_13cy4",
    group = 
"""
1 *1 R!H 1 {2,S} {5,{S,D,B}}
2 *4 R!H 0 {1,S} {3,S}
3 *2 R!H 0 {2,S} {4,S} {5,{S,D,B}}
4 *3 H   0 {3,S}
5    R!H 0 {1,{S,D,B}} {3,{S,D,B}}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 20,
    label = "R3H_SS_12cy5",
    group = 
"""
1 *1 R!H 1 {2,S} {7,{S,D,B}}
2 *4 R!H 0 {1,S} {3,S} {5,{S,D,B}}
3 *2 R!H 0 {2,S} {4,S}
4 *3 H   0 {3,S}
5    R!H 0 {2,{S,D,B}} {6,{S,D,B}}
6    R!H 0 {5,{S,D,B}} {7,{S,D,B}}
7    R!H 0 {1,{S,D,B}} {6,{S,D,B}}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 21,
    label = "R3H_SS_23cy5",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S} {7,{S,D,B}}
3 *2 R!H 0 {2,S} {4,S} {5,{S,D,B}}
4 *3 H   0 {3,S}
5    R!H 0 {3,{S,D,B}} {6,{S,D,B}}
6    R!H 0 {5,{S,D,B}} {7,{S,D,B}}
7    R!H 0 {2,{S,D,B}} {6,{S,D,B}}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 22,
    label = "R3H_SS_13cy5",
    group = 
"""
1 *1 R!H 1 {2,S} {6,{S,D,B}}
2 *4 R!H 0 {1,S} {3,S}
3 *2 R!H 0 {2,S} {4,S} {5,{S,D,B}}
4 *3 H   0 {3,S}
5    R!H 0 {3,{S,D,B}} {6,{S,D,B}}
6    R!H 0 {1,{S,D,B}} {5,{S,D,B}}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 23,
    label = "R3H_SS_2Cd",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 Cd  0 {1,S} {3,S}
3 *2 R!H 0 {2,S} {4,S}
4 *3 H   0 {3,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 24,
    label = "R3H_SS_OC",
    group = 
"""
1 *1 Os 1 {2,S}
2 *4 Os 0 {1,S} {3,S}
3 *2 Cs 0 {2,S} {4,S}
4 *3 H  0 {3,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 25,
    label = "R3H_SS_S",
    group = 
"""
1 *1 R  1 {2,S}
2 *4 Ss 0 {1,S} {3,S}
3 *2 R  0 {2,S} {4,S}
4 *3 H  0 {3,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 26,
    label = "Others-R3H_SS",
    group = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    distances = DistanceData(
        distances = {'d12': -0.114367, 'd13': 0.032614, 'd23': 0.047761},
        uncertainties = {'d12': 2.04679, 'd13': 0.290832, 'd23': 0.213783},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=26 label="Others-R3H_SS">, <Entry index=181 label="C_rad_out_H/NonDeC">, <Entry index=199 label="O_H_out">]
[<Entry index=26 label="Others-R3H_SS">, <Entry index=179 label="C_rad_out_2H">, <Entry index=214 label="Cs_H_out_H/(NonDeC/Cs)">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 27,
    label = "R3H_SD",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 Cd  0 {1,S} {3,D}
3 *2 Cd  0 {2,D} {4,S}
4 *3 H   0 {3,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 28,
    label = "R3H_ST",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 Ct  0 {1,S} {3,T}
3 *2 Ct  0 {2,T} {4,S}
4 *3 H   0 {3,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 29,
    label = "R3H_SB",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 Cb  0 {1,S} {3,B}
3 *2 Cb  0 {2,B} {4,S}
4 *3 H   0 {3,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 30,
    label = "R3H_MS",
    group = 
"""
1 *1 R!H 1 {2,{D,T,B}}
2 *4 R!H 0 {1,{D,T,B}} {3,S}
3 *2 R!H 0 {2,S} {4,S}
4 *3 H   0 {3,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 31,
    label = "R3H_DS",
    group = 
"""
1 *1 Cd  1 {2,D}
2 *4 Cd  0 {1,D} {3,S}
3 *2 R!H 0 {2,S} {4,S}
4 *3 H   0 {3,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 32,
    label = "R3H_TS",
    group = 
"""
1 *1 Ct  1 {2,T}
2 *4 Ct  0 {1,T} {3,S}
3 *2 R!H 0 {2,S} {4,S}
4 *3 H   0 {3,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 33,
    label = "R3H_BS",
    group = 
"""
1 *1 Cb  1 {2,B}
2 *4 Cb  0 {1,B} {3,S}
3 *2 R!H 0 {2,S} {4,S}
4 *3 H   0 {3,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 34,
    label = "R3H_BB",
    group = 
"""
1 *1 Cb  1 {2,B}
2 *4 Cbf 0 {1,B} {3,B}
3 *2 Cb  0 {2,B} {4,S}
4 *3 H   0 {3,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 35,
    label = "R4H",
    group = "OR{R4H_RSR, R4H_SMS, R4H_SBB, R4H_BBS, R4H_BBB}",
    distances = DistanceData(
        distances = {'d12': 0.214392, 'd13': 0.011624, 'd23': 0.01349},
        uncertainties = {'d12': 1.03899, 'd13': 0.150634, 'd23': 0.193248},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=38 label="R4H_SSS">, <Entry index=167 label="O_rad_out">, <Entry index=213 label="Cs_H_out_H/NonDeC">]
[<Entry index=38 label="R4H_SSS">, <Entry index=179 label="C_rad_out_2H">, <Entry index=214 label="Cs_H_out_H/(NonDeC/Cs)">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 36,
    label = "R4H_RSR",
    group = 
"""
1 *1 R!H 1 {2,{S,D,T,B}}
2 *4 R!H 0 {1,{S,D,T,B}} {3,S}
3 *5 R!H 0 {2,S} {4,{S,D,T,B}}
4 *2 R!H 0 {3,{S,D,T,B}} {5,S}
5 *3 H   0 {4,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.214392, 'd13': 0.011624, 'd23': 0.01349},
        uncertainties = {'d12': 1.03899, 'd13': 0.150634, 'd23': 0.193248},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=38 label="R4H_SSS">, <Entry index=167 label="O_rad_out">, <Entry index=213 label="Cs_H_out_H/NonDeC">]
[<Entry index=38 label="R4H_SSS">, <Entry index=179 label="C_rad_out_2H">, <Entry index=214 label="Cs_H_out_H/(NonDeC/Cs)">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 37,
    label = "R4H_RSS",
    group = 
"""
1 *1 R!H 1 {2,{S,D,T,B}}
2 *4 R!H 0 {1,{S,D,T,B}} {3,S}
3 *5 R!H 0 {2,S} {4,S}
4 *2 R!H 0 {3,S} {5,S}
5 *3 H   0 {4,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.214392, 'd13': 0.011624, 'd23': 0.01349},
        uncertainties = {'d12': 1.03899, 'd13': 0.150634, 'd23': 0.193248},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=38 label="R4H_SSS">, <Entry index=167 label="O_rad_out">, <Entry index=213 label="Cs_H_out_H/NonDeC">]
[<Entry index=38 label="R4H_SSS">, <Entry index=179 label="C_rad_out_2H">, <Entry index=214 label="Cs_H_out_H/(NonDeC/Cs)">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 38,
    label = "R4H_SSS",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3 *5 R!H 0 {2,S} {4,S}
4 *2 R!H 0 {3,S} {5,S}
5 *3 H   0 {4,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.214392, 'd13': 0.011624, 'd23': 0.01349},
        uncertainties = {'d12': 1.03899, 'd13': 0.150634, 'd23': 0.193248},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=38 label="R4H_SSS">, <Entry index=167 label="O_rad_out">, <Entry index=213 label="Cs_H_out_H/NonDeC">]
[<Entry index=38 label="R4H_SSS">, <Entry index=179 label="C_rad_out_2H">, <Entry index=214 label="Cs_H_out_H/(NonDeC/Cs)">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 39,
    label = "R4H_SSS_CsSCsCs",
    group = 
"""
1 *1 Cs 1 {2,S}
2 *4 Ss 0 {1,S} {3,S}
3 *5 Cs 0 {2,S} {4,S}
4 *2 Cs 0 {3,S} {5,S}
5 *3 H  0 {4,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 40,
    label = "R4H_SSS_CsCsSCs",
    group = 
"""
1 *1 Cs 1 {2,S}
2 *4 Cs 0 {1,S} {3,S}
3 *5 Ss 0 {2,S} {4,S}
4 *2 Cs 0 {3,S} {5,S}
5 *3 H  0 {4,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 41,
    label = "R4H_SSS_OOCsCs",
    group = 
"""
1 *1 Os 1 {2,S}
2 *4 Os 0 {1,S} {3,S}
3 *5 Cs 0 {2,S} {4,S}
4 *2 Cs 0 {3,S} {5,S}
5 *3 H  0 {4,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 42,
    label = "R4H_SSS_OO(Cs/Cs)Cs",
    group = 
"""
1 *1 Os 1 {2,S}
2 *4 Os 0 {1,S} {3,S}
3 *5 Cs 0 {2,S} {4,S} {6,S}
4 *2 Cs 0 {3,S} {5,S}
5 *3 H  0 {4,S}
6    Cs 0 {3,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 43,
    label = "R4H_SSS_OO(Cs/Cs/Cs)Cs",
    group = 
"""
1 *1 Os 1 {2,S}
2 *4 Os 0 {1,S} {3,S}
3 *5 Cs 0 {2,S} {4,S} {6,S} {7,S}
4 *2 Cs 0 {3,S} {5,S}
5 *3 H  0 {4,S}
6    Cs 0 {3,S}
7    Cs 0 {3,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 44,
    label = "R4H_DSS",
    group = 
"""
1 *1 Cd  1 {2,D}
2 *4 Cd  0 {1,D} {3,S}
3 *5 R!H 0 {2,S} {4,S}
4 *2 R!H 0 {3,S} {5,S}
5 *3 H   0 {4,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 45,
    label = "R4H_TSS",
    group = 
"""
1 *1 Ct  1 {2,T}
2 *4 Ct  0 {1,T} {3,S}
3 *5 R!H 0 {2,S} {4,S}
4 *2 R!H 0 {3,S} {5,S}
5 *3 H   0 {4,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 46,
    label = "R4H_BSS",
    group = 
"""
1 *1 Cb  1 {2,B}
2 *4 Cb  0 {1,B} {3,S}
3 *5 R!H 0 {2,S} {4,S}
4 *2 R!H 0 {3,S} {5,S}
5 *3 H   0 {4,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 47,
    label = "R4H_RSD",
    group = 
"""
1 *1 R!H 1 {2,{S,D,T,B}}
2 *4 R!H 0 {1,{S,D,T,B}} {3,S}
3 *5 Cd  0 {2,S} {4,D}
4 *2 Cd  0 {3,D} {5,S}
5 *3 H   0 {4,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 48,
    label = "R4H_SSD",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3 *5 Cd  0 {2,S} {4,D}
4 *2 Cd  0 {3,D} {5,S}
5 *3 H   0 {4,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 49,
    label = "R4H_DSD",
    group = 
"""
1 *1 Cd 1 {2,D}
2 *4 Cd 0 {1,D} {3,S}
3 *5 Cd 0 {2,S} {4,D}
4 *2 Cd 0 {3,D} {5,S}
5 *3 H  0 {4,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 50,
    label = "R4H_TSD",
    group = 
"""
1 *1 Ct 1 {2,T}
2 *4 Ct 0 {1,T} {3,S}
3 *5 Cd 0 {2,S} {4,D}
4 *2 Cd 0 {3,D} {5,S}
5 *3 H  0 {4,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 51,
    label = "R4H_BSD",
    group = 
"""
1 *1 Cb 1 {2,B}
2 *4 Cb 0 {1,B} {3,S}
3 *5 Cd 0 {2,S} {4,D}
4 *2 Cd 0 {3,D} {5,S}
5 *3 H  0 {4,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 52,
    label = "R4H_RST",
    group = 
"""
1 *1 R!H 1 {2,{S,D,T,B}}
2 *4 R!H 0 {1,{S,D,T,B}} {3,S}
3 *5 Ct  0 {2,S} {4,T}
4 *2 Ct  0 {3,T} {5,S}
5 *3 H   0 {4,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 53,
    label = "R4H_SST",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3 *5 Ct  0 {2,S} {4,T}
4 *2 Ct  0 {3,T} {5,S}
5 *3 H   0 {4,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 54,
    label = "R4H_DST",
    group = 
"""
1 *1 Cd 1 {2,D}
2 *4 Cd 0 {1,D} {3,S}
3 *5 Ct 0 {2,S} {4,T}
4 *2 Ct 0 {3,T} {5,S}
5 *3 H  0 {4,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 55,
    label = "R4H_TST",
    group = 
"""
1 *1 Ct 1 {2,T}
2 *4 Ct 0 {1,T} {3,S}
3 *5 Ct 0 {2,S} {4,T}
4 *2 Ct 0 {3,T} {5,S}
5 *3 H  0 {4,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 56,
    label = "R4H_BST",
    group = 
"""
1 *1 Cb 1 {2,B}
2 *4 Cb 0 {1,B} {3,S}
3 *5 Ct 0 {2,S} {4,T}
4 *2 Ct 0 {3,T} {5,S}
5 *3 H  0 {4,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 57,
    label = "R4H_RSB",
    group = 
"""
1 *1 R!H 1 {2,{S,D,T,B}}
2 *4 R!H 0 {1,{S,D,T,B}} {3,S}
3 *5 Cb  0 {2,S} {4,B}
4 *2 Cb  0 {3,B} {5,S}
5 *3 H   0 {4,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 58,
    label = "R4H_SSB",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3 *5 Cb  0 {2,S} {4,B}
4 *2 Cb  0 {3,B} {5,S}
5 *3 H   0 {4,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 59,
    label = "R4H_DSB",
    group = 
"""
1 *1 Cd 1 {2,D}
2 *4 Cd 0 {1,D} {3,S}
3 *5 Cb 0 {2,S} {4,B}
4 *2 Cb 0 {3,B} {5,S}
5 *3 H  0 {4,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 60,
    label = "R4H_TSB",
    group = 
"""
1 *1 Ct 1 {2,T}
2 *4 Ct 0 {1,T} {3,S}
3 *5 Cb 0 {2,S} {4,B}
4 *2 Cb 0 {3,B} {5,S}
5 *3 H  0 {4,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 61,
    label = "R4H_BSB",
    group = 
"""
1 *1 Cb 1 {2,B}
2 *4 Cb 0 {1,B} {3,S}
3 *5 Cb 0 {2,S} {4,B}
4 *2 Cb 0 {3,B} {5,S}
5 *3 H  0 {4,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 62,
    label = "R4H_SMS",
    group = 
"""
1 *1 R!H        1 {2,S}
2 *4 {Cd,Ct,Cb} 0 {1,S} {3,{D,T,B}}
3 *5 {Cd,Ct,Cb} 0 {2,{D,T,B}} {4,S}
4 *2 R!H        0 {3,S} {5,S}
5 *3 H          0 {4,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 63,
    label = "R4H_SDS",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 Cd  0 {1,S} {3,D}
3 *5 Cd  0 {2,D} {4,S}
4 *2 R!H 0 {3,S} {5,S}
5 *3 H   0 {4,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 64,
    label = "R4H_STS",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 Ct  0 {1,S} {3,T}
3 *5 Ct  0 {2,T} {4,S}
4 *2 R!H 0 {3,S} {5,S}
5 *3 H   0 {4,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 65,
    label = "R4H_SBS",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 Cb  0 {1,S} {3,B}
3 *5 Cb  0 {2,B} {4,S}
4 *2 R!H 0 {3,S} {5,S}
5 *3 H   0 {4,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 66,
    label = "R4H_SBB",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 Cb  0 {1,S} {3,B}
3 *5 Cbf 0 {2,B} {4,B}
4 *2 Cb  0 {3,B} {5,S}
5 *3 H   0 {4,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 67,
    label = "R4H_BBS",
    group = 
"""
1 *1 Cb  1 {2,B}
2 *4 Cbf 0 {1,B} {3,B}
3 *5 Cb  0 {2,B} {4,S}
4 *2 R!H 0 {3,S} {5,S}
5 *3 H   0 {4,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 68,
    label = "R4H_BBB",
    group = 
"""
1  *1 Cb       1 {2,B} {15,B}
2  *4 Cbf      0 {1,B} {3,B} {12,B}
3  *5 Cbf      0 {2,B} {4,B} {9,B}
4  *2 Cb       0 {3,B} {5,S} {6,B}
5  *3 H        0 {4,S}
6     {Cb,Cbf} 0 {4,B} {7,B}
7     {Cb,Cbf} 0 {6,B} {8,B}
8     {Cb,Cbf} 0 {7,B} {9,B}
9     Cbf      0 {3,B} {8,B} {10,B}
10    {Cb,Cbf} 0 {9,B} {11,B}
11    {Cb,Cbf} 0 {10,B} {12,B}
12    Cbf      0 {2,B} {11,B} {13,B}
13    {Cb,Cbf} 0 {12,B} {14,B}
14    {Cb,Cbf} 0 {13,B} {15,B}
15    {Cb,Cbf} 0 {1,B} {14,B}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 69,
    label = "R5H",
    group = "OR{R5H_RSSR, R5H_RSMS, R5H_SMSR, R5H_BBSR, R5H_RSBB, R5H_SBBS, R5H_SBBB, R5H_BBBS, R5H_BBBB}",
    distances = DistanceData(
        distances = {'d12': 0.284917, 'd13': 0.031417, 'd23': -0.009447},
        uncertainties = {'d12': 1.151051, 'd13': 0.346579, 'd23': 0.248831},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=72 label="R5H_SSSS">, <Entry index=181 label="C_rad_out_H/NonDeC">, <Entry index=211 label="Cs_H_out_2H">]
[<Entry index=73 label="R5H_CCCC_O">, <Entry index=167 label="O_rad_out">, <Entry index=210 label="Cs_H_out">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 70,
    label = "R5H_RSSR",
    group = 
"""
1 *1 R!H 1 {2,{S,D,T,B}}
2 *4 R!H 0 {1,{S,D,T,B}} {3,S}
3    R!H 0 {2,S} {4,S}
4 *5 R!H 0 {3,S} {5,{S,D,T,B}}
5 *2 R!H 0 {4,{S,D,T,B}} {6,S}
6 *3 H   0 {5,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.284917, 'd13': 0.031417, 'd23': -0.009447},
        uncertainties = {'d12': 1.151051, 'd13': 0.346579, 'd23': 0.248831},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=72 label="R5H_SSSS">, <Entry index=181 label="C_rad_out_H/NonDeC">, <Entry index=211 label="Cs_H_out_2H">]
[<Entry index=73 label="R5H_CCCC_O">, <Entry index=167 label="O_rad_out">, <Entry index=210 label="Cs_H_out">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 71,
    label = "R5H_SSSR",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3    R!H 0 {2,S} {4,S}
4 *5 R!H 0 {3,S} {5,{S,D,T,B}}
5 *2 R!H 0 {4,{S,D,T,B}} {6,S}
6 *3 H   0 {5,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.284917, 'd13': 0.031417, 'd23': -0.009447},
        uncertainties = {'d12': 1.151051, 'd13': 0.346579, 'd23': 0.248831},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=72 label="R5H_SSSS">, <Entry index=181 label="C_rad_out_H/NonDeC">, <Entry index=211 label="Cs_H_out_2H">]
[<Entry index=73 label="R5H_CCCC_O">, <Entry index=167 label="O_rad_out">, <Entry index=210 label="Cs_H_out">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 72,
    label = "R5H_SSSS",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3    R!H 0 {2,S} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 R!H 0 {4,S} {6,S}
6 *3 H   0 {5,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.284917, 'd13': 0.031417, 'd23': -0.009447},
        uncertainties = {'d12': 1.151051, 'd13': 0.346579, 'd23': 0.248831},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=72 label="R5H_SSSS">, <Entry index=181 label="C_rad_out_H/NonDeC">, <Entry index=211 label="Cs_H_out_2H">]
[<Entry index=73 label="R5H_CCCC_O">, <Entry index=167 label="O_rad_out">, <Entry index=210 label="Cs_H_out">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 73,
    label = "R5H_CCCC_O",
    group = 
"""
1 *1 O 1 {2,S}
2 *4 C 0 {1,S} {3,S}
3    C 0 {2,S} {4,S}
4 *5 C 0 {3,S} {5,S}
5 *2 C 0 {4,S} {6,S}
6 *3 H 0 {5,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.244595, 'd13': 0.000377, 'd23': -0.037537},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=73 label="R5H_CCCC_O">, <Entry index=167 label="O_rad_out">, <Entry index=210 label="Cs_H_out">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 74,
    label = "R5H_SSSS_CsCsCsSCs",
    group = 
"""
1 *1 Cs 1 {2,S}
2 *4 Cs 0 {1,S} {3,S}
3    Cs 0 {2,S} {4,S}
4 *5 Ss 0 {3,S} {5,S}
5 *2 Cs 0 {4,S} {6,S}
6 *3 H  0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 75,
    label = "R5H_SSSS_OOCCC",
    group = 
"""
1 *1 Os 1 {2,S}
2 *4 Os 0 {1,S} {3,S}
3    Cs 0 {2,S} {4,S}
4 *5 Cs 0 {3,S} {5,S}
5 *2 Cs 0 {4,S} {6,S}
6 *3 H  0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 76,
    label = "R5H_SSSS_OO(Cs/Cs)Cs",
    group = 
"""
1 *1 Os 1 {2,S}
2 *4 Os 0 {1,S} {3,S}
3    Cs 0 {2,S} {4,S} {7,S}
4 *5 Cs 0 {3,S} {5,S}
5 *2 Cs 0 {4,S} {6,S}
6 *3 H  0 {5,S}
7    Cs 0 {3,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 77,
    label = "R5H_SSSS_OO(Cs/Cs/Cs)Cs",
    group = 
"""
1 *1 Os 1 {2,S}
2 *4 Os 0 {1,S} {3,S}
3    Cs 0 {2,S} {4,S} {7,S} {8,S}
4 *5 Cs 0 {3,S} {5,S}
5 *2 Cs 0 {4,S} {6,S}
6 *3 H  0 {5,S}
7    Cs 0 {3,S}
8    Cs 0 {3,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 78,
    label = "R5H_SSSS_OOCs(Cs/Cs)",
    group = 
"""
1 *1 Os 1 {2,S}
2 *4 Os 0 {1,S} {3,S}
3    Cs 0 {2,S} {4,S}
4 *5 Cs 0 {3,S} {5,S} {7,S}
5 *2 Cs 0 {4,S} {6,S}
6 *3 H  0 {5,S}
7    Cs 0 {4,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 79,
    label = "R5H_SSSS_OOCs(Cs/Cs/Cs)",
    group = 
"""
1 *1 Os 1 {2,S}
2 *4 Os 0 {1,S} {3,S}
3    Cs 0 {2,S} {4,S}
4 *5 Cs 0 {3,S} {5,S} {7,S} {8,S}
5 *2 Cs 0 {4,S} {6,S}
6 *3 H  0 {5,S}
7    Cs 0 {4,S}
8    Cs 0 {4,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 80,
    label = "R5H_SSSD",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3    R!H 0 {2,S} {4,S}
4 *5 Cd  0 {3,S} {5,D}
5 *2 Cd  0 {4,D} {6,S}
6 *3 H   0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 81,
    label = "R5H_SSST",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3    R!H 0 {2,S} {4,S}
4 *5 Ct  0 {3,S} {5,T}
5 *2 Ct  0 {4,T} {6,S}
6 *3 H   0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 82,
    label = "R5H_SSSB",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3    R!H 0 {2,S} {4,S}
4 *5 Cb  0 {3,S} {5,B}
5 *2 Cb  0 {4,B} {6,S}
6 *3 H   0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 83,
    label = "R5H_DSSR",
    group = 
"""
1 *1 Cd  1 {2,D}
2 *4 Cd  0 {1,D} {3,S}
3    R!H 0 {2,S} {4,S}
4 *5 R!H 0 {3,S} {5,{S,D,T,B}}
5 *2 R!H 0 {4,{S,D,T,B}} {6,S}
6 *3 H   0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 84,
    label = "R5H_DSSS",
    group = 
"""
1 *1 Cd  1 {2,D}
2 *4 Cd  0 {1,D} {3,S}
3    R!H 0 {2,S} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 R!H 0 {4,S} {6,S}
6 *3 H   0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 85,
    label = "R5H_DSSD",
    group = 
"""
1 *1 Cd  1 {2,D}
2 *4 Cd  0 {1,D} {3,S}
3    R!H 0 {2,S} {4,S}
4 *5 Cd  0 {3,S} {5,D}
5 *2 Cd  0 {4,D} {6,S}
6 *3 H   0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 86,
    label = "R5H_DSST",
    group = 
"""
1 *1 Cd  1 {2,D}
2 *4 Cd  0 {1,D} {3,S}
3    R!H 0 {2,S} {4,S}
4 *5 Ct  0 {3,S} {5,T}
5 *2 Ct  0 {4,T} {6,S}
6 *3 H   0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 87,
    label = "R5H_DSSB",
    group = 
"""
1 *1 Cd  1 {2,D}
2 *4 Cd  0 {1,D} {3,S}
3    R!H 0 {2,S} {4,S}
4 *5 Cb  0 {3,S} {5,B}
5 *2 Cb  0 {4,B} {6,S}
6 *3 H   0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 88,
    label = "R5H_TSSR",
    group = 
"""
1 *1 Ct  1 {2,T}
2 *4 Ct  0 {1,T} {3,S}
3    R!H 0 {2,S} {4,S}
4 *5 R!H 0 {3,S} {5,{S,D,T,B}}
5 *2 R!H 0 {4,{S,D,T,B}} {6,S}
6 *3 H   0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 89,
    label = "R5H_TSSS",
    group = 
"""
1 *1 Ct  1 {2,T}
2 *4 Ct  0 {1,T} {3,S}
3    R!H 0 {2,S} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 R!H 0 {4,S} {6,S}
6 *3 H   0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 90,
    label = "R5H_TSSD",
    group = 
"""
1 *1 Ct  1 {2,T}
2 *4 Ct  0 {1,T} {3,S}
3    R!H 0 {2,S} {4,S}
4 *5 Cd  0 {3,S} {5,D}
5 *2 Cd  0 {4,D} {6,S}
6 *3 H   0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 91,
    label = "R5H_TSST",
    group = 
"""
1 *1 Ct  1 {2,T}
2 *4 Ct  0 {1,T} {3,S}
3    R!H 0 {2,S} {4,S}
4 *5 Ct  0 {3,S} {5,T}
5 *2 Ct  0 {4,T} {6,S}
6 *3 H   0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 92,
    label = "R5H_TSSB",
    group = 
"""
1 *1 Ct  1 {2,T}
2 *4 Ct  0 {1,T} {3,S}
3    R!H 0 {2,S} {4,S}
4 *5 Cb  0 {3,S} {5,B}
5 *2 Cb  0 {4,B} {6,S}
6 *3 H   0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 93,
    label = "R5H_BSSR",
    group = 
"""
1 *1 Cb  1 {2,B}
2 *4 Cb  0 {1,B} {3,S}
3    R!H 0 {2,S} {4,S}
4 *5 R!H 0 {3,S} {5,{S,D,T,B}}
5 *2 R!H 0 {4,{S,D,T,B}} {6,S}
6 *3 H   0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 94,
    label = "R5H_BSSS",
    group = 
"""
1 *1 Cb  1 {2,B}
2 *4 Cb  0 {1,B} {3,S}
3    R!H 0 {2,S} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 R!H 0 {4,S} {6,S}
6 *3 H   0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 95,
    label = "R5H_BSSD",
    group = 
"""
1 *1 Cb  1 {2,B}
2 *4 Cb  0 {1,B} {3,S}
3    R!H 0 {2,S} {4,S}
4 *5 Cd  0 {3,S} {5,D}
5 *2 Cd  0 {4,D} {6,S}
6 *3 H   0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 96,
    label = "R5H_BSST",
    group = 
"""
1 *1 Cb  1 {2,B}
2 *4 Cb  0 {1,B} {3,S}
3    R!H 0 {2,S} {4,S}
4 *5 Ct  0 {3,S} {5,T}
5 *2 Ct  0 {4,T} {6,S}
6 *3 H   0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 97,
    label = "R5H_BSSB",
    group = 
"""
1 *1 Cb  1 {2,B}
2 *4 Cb  0 {1,B} {3,S}
3    R!H 0 {2,S} {4,S}
4 *5 Cb  0 {3,S} {5,B}
5 *2 Cb  0 {4,B} {6,S}
6 *3 H   0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 98,
    label = "R5H_RSMS",
    group = 
"""
1 *1 R!H 1 {2,{S,D,T,B}}
2 *4 R!H 0 {1,{S,D,T,B}} {3,S}
3    R!H 0 {2,S} {4,{D,T,B}}
4 *5 R!H 0 {3,{D,T,B}} {5,S}
5 *2 R!H 0 {4,S} {6,S}
6 *3 H   0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 99,
    label = "R5H_SSMS",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3    R!H 0 {2,S} {4,{D,T,B}}
4 *5 R!H 0 {3,{D,T,B}} {5,S}
5 *2 R!H 0 {4,S} {6,S}
6 *3 H   0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 100,
    label = "R5H_DSMS",
    group = 
"""
1 *1 Cd  1 {2,D}
2 *4 Cd  0 {1,D} {3,S}
3    R!H 0 {2,S} {4,{D,T,B}}
4 *5 R!H 0 {3,{D,T,B}} {5,S}
5 *2 R!H 0 {4,S} {6,S}
6 *3 H   0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 101,
    label = "R5H_TSMS",
    group = 
"""
1 *1 Ct  1 {2,T}
2 *4 Ct  0 {1,T} {3,S}
3    R!H 0 {2,S} {4,{D,T,B}}
4 *5 R!H 0 {3,{D,T,B}} {5,S}
5 *2 R!H 0 {4,S} {6,S}
6 *3 H   0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 102,
    label = "R5H_BSMS",
    group = 
"""
1 *1 Cb  1 {2,B}
2 *4 Cb  0 {1,B} {3,S}
3    R!H 0 {2,S} {4,{D,T,B}}
4 *5 R!H 0 {3,{D,T,B}} {5,S}
5 *2 R!H 0 {4,S} {6,S}
6 *3 H   0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 103,
    label = "R5H_SMSR",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,{D,T,B}}
3    R!H 0 {2,{D,T,B}} {4,S}
4 *5 R!H 0 {3,S} {5,{S,D,T,B}}
5 *2 R!H 0 {4,{S,D,T,B}} {6,S}
6 *3 H   0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 104,
    label = "R5H_SMSS",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,{D,T,B}}
3    R!H 0 {2,{D,T,B}} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 R!H 0 {4,S} {6,S}
6 *3 H   0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 105,
    label = "R5H_SMSD",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,{D,T,B}}
3    R!H 0 {2,{D,T,B}} {4,S}
4 *5 Cd  0 {3,S} {5,D}
5 *2 Cd  0 {4,D} {6,S}
6 *3 H   0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 106,
    label = "R5H_SMST",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,{D,T,B}}
3    R!H 0 {2,{D,T,B}} {4,S}
4 *5 Ct  0 {3,S} {5,T}
5 *2 Ct  0 {4,T} {6,S}
6 *3 H   0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 107,
    label = "R5H_SMSB",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,{D,T,B}}
3    R!H 0 {2,{D,T,B}} {4,S}
4 *5 Cb  0 {3,S} {5,B}
5 *2 Cb  0 {4,B} {6,S}
6 *3 H   0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 108,
    label = "R5H_BBSR",
    group = 
"""
1 *1 Cb  1 {2,B}
2 *4 Cbf 0 {1,B} {3,B}
3    Cb  0 {2,B} {4,S}
4 *5 R!H 0 {3,S} {5,{S,D,T,B}}
5 *2 R!H 0 {4,{S,D,T,B}} {6,S}
6 *3 H   0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 109,
    label = "R5H_BBSS",
    group = 
"""
1 *1 Cb  1 {2,B}
2 *4 Cbf 0 {1,B} {3,B}
3    Cb  0 {2,B} {4,S}
4 *5 R!H 0 {3,S} {5,S}
5 *2 R!H 0 {4,S} {6,S}
6 *3 H   0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 110,
    label = "R5H_BBSD",
    group = 
"""
1 *1 Cb  1 {2,B}
2 *4 Cbf 0 {1,B} {3,B}
3    Cb  0 {2,B} {4,S}
4 *5 Cd  0 {3,S} {5,D}
5 *2 Cd  0 {4,D} {6,S}
6 *3 H   0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 111,
    label = "R5H_BBST",
    group = 
"""
1 *1 Cb  1 {2,B}
2 *4 Cbf 0 {1,B} {3,B}
3    Cb  0 {2,B} {4,S}
4 *5 Ct  0 {3,S} {5,T}
5 *2 Ct  0 {4,T} {6,S}
6 *3 H   0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 112,
    label = "R5H_BBSB",
    group = 
"""
1 *1 Cb  1 {2,B}
2 *4 Cbf 0 {1,B} {3,B}
3    Cb  0 {2,B} {4,S}
4 *5 Cb  0 {3,S} {5,B}
5 *2 Cb  0 {4,B} {6,S}
6 *3 H   0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 113,
    label = "R5H_RSBB",
    group = 
"""
1 *1 R!H 1 {2,{S,D,T,B}}
2 *4 R!H 0 {1,{S,D,T,B}} {3,S}
3    Cb  0 {2,S} {4,B}
4 *5 Cbf 0 {3,B} {5,B}
5 *2 Cb  0 {4,B} {6,S}
6 *3 H   0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 114,
    label = "R5H_SSBB",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3    Cb  0 {2,S} {4,B}
4 *5 Cbf 0 {3,B} {5,B}
5 *2 Cb  0 {4,B} {6,S}
6 *3 H   0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 115,
    label = "R5H_DSBB",
    group = 
"""
1 *1 Cd  1 {2,D}
2 *4 Cd  0 {1,D} {3,S}
3    Cb  0 {2,S} {4,B}
4 *5 Cbf 0 {3,B} {5,B}
5 *2 Cb  0 {4,B} {6,S}
6 *3 H   0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 116,
    label = "R5H_TSBB",
    group = 
"""
1 *1 Ct  1 {2,T}
2 *4 Ct  0 {1,T} {3,S}
3    Cb  0 {2,S} {4,B}
4 *5 Cbf 0 {3,B} {5,B}
5 *2 Cb  0 {4,B} {6,S}
6 *3 H   0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 117,
    label = "R5H_BSBB",
    group = 
"""
1 *1 Cb  1 {2,B}
2 *4 Cb  0 {1,B} {3,S}
3    Cb  0 {2,S} {4,B}
4 *5 Cbf 0 {3,B} {5,B}
5 *2 Cb  0 {4,B} {6,S}
6 *3 H   0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 118,
    label = "R5H_SBBS",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 Cb  0 {1,S} {3,B}
3    Cbf 0 {2,B} {4,B}
4 *5 Cb  0 {3,B} {5,S}
5 *2 R!H 0 {4,S} {6,S}
6 *3 H   0 {5,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 119,
    label = "R5H_SBBB",
    group = 
"""
1  *1 R!H      1 {2,S}
2  *4 Cb       0 {1,S} {3,B} {16,B}
3     Cbf      0 {2,B} {4,B} {13,B}
4  *5 Cbf      0 {3,B} {5,B} {10,B}
5  *2 Cb       0 {4,B} {6,S} {7,B}
6  *3 H        0 {5,S}
7     {Cb,Cbf} 0 {5,B} {8,B}
8     {Cb,Cbf} 0 {7,B} {9,B}
9     {Cb,Cbf} 0 {8,B} {10,B}
10    Cbf      0 {4,B} {9,B} {11,B}
11    {Cb,Cbf} 0 {10,B} {12,B}
12    {Cb,Cbf} 0 {11,B} {13,B}
13    Cbf      0 {3,B} {12,B} {14,B}
14    {Cb,Cbf} 0 {13,B} {15,B}
15    {Cb,Cbf} 0 {14,B} {16,B}
16    {Cb,Cbf} 0 {2,B} {15,B}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 120,
    label = "R5H_BBBS",
    group = 
"""
1  *1 Cb       1 {2,B} {16,B}
2  *4 Cbf      0 {1,B} {3,B} {13,B}
3     Cbf      0 {2,B} {4,B} {10,B}
4  *5 Cb       0 {3,B} {5,S} {7,B}
5  *2 R!H      0 {4,S} {6,S}
6  *3 H        0 {5,S}
7     {Cb,Cbf} 0 {4,B} {8,B}
8     {Cb,Cbf} 0 {7,B} {9,B}
9     {Cb,Cbf} 0 {8,B} {10,B}
10    Cbf      0 {3,B} {9,B} {11,B}
11    {Cb,Cbf} 0 {10,B} {12,B}
12    {Cb,Cbf} 0 {11,B} {13,B}
13    Cbf      0 {2,B} {12,B} {14,B}
14    {Cb,Cbf} 0 {13,B} {15,B}
15    {Cb,Cbf} 0 {14,B} {16,B}
16    {Cb,Cbf} 0 {1,B} {15,B}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 121,
    label = "R5H_BBBB",
    group = 
"""
1  *1 Cb       1 {2,B} {19,B}
2  *4 Cbf      0 {1,B} {3,B} {16,B}
3     Cbf      0 {2,B} {4,B} {13,B}
4  *5 Cbf      0 {3,B} {5,B} {10,B}
5  *2 Cb       0 {4,B} {6,S} {7,B}
6  *3 H        0 {5,S}
7     {Cb,Cbf} 0 {5,B} {8,B}
8     {Cb,Cbf} 0 {7,B} {9,B}
9     {Cb,Cbf} 0 {8,B} {10,B}
10    Cbf      0 {4,B} {9,B} {11,B}
11    {Cb,Cbf} 0 {10,B} {12,B}
12    {Cb,Cbf} 0 {11,B} {13,B}
13    Cbf      0 {3,B} {12,B} {14,B}
14    {Cb,Cbf} 0 {13,B} {15,B}
15    {Cb,Cbf} 0 {14,B} {16,B}
16    Cbf      0 {2,B} {15,B} {17,B}
17    {Cb,Cbf} 0 {16,B} {18,B}
18    {Cb,Cbf} 0 {17,B} {19,B}
19    {Cb,Cbf} 0 {1,B} {18,B}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 122,
    label = "R6H",
    group = "OR{R6H_RSSSR, R6H_RSSMS, R6H_RSMSR, R6H_SMSSR, R6H_SMSMS, R6H_BBSRS, R6H_BBSSM, R6H_BBSBB, R6H_SBBSR, R6H_RSBBS, R6H_BBBSR, R6H_SBBBS, R6H_RSBBB, R6H_SBBBB, R6H_BBBBS, R6H_BBBBB}",
    distances = DistanceData(
        distances = {'d12': 0.264228, 'd13': -0.013414, 'd23': 0.010889},
        uncertainties = {'d12': 0.940541, 'd13': 0.148253, 'd23': 0.359681},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=125 label="R6H_SSSSS">, <Entry index=191 label="Others-C_rad_out_Cs2">, <Entry index=199 label="O_H_out">]
[<Entry index=125 label="R6H_SSSSS">, <Entry index=181 label="C_rad_out_H/NonDeC">, <Entry index=211 label="Cs_H_out_2H">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 123,
    label = "R6H_RSSSR",
    group = 
"""
1 *1 R!H 1 {2,{S,D,T,B}}
2 *4 R!H 0 {1,{S,D,T,B}} {3,S}
3    R!H 0 {2,S} {4,S}
4    R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,{S,D,T,B}}
6 *2 R!H 0 {5,{S,D,T,B}} {7,S}
7 *3 H   0 {6,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.264228, 'd13': -0.013414, 'd23': 0.010889},
        uncertainties = {'d12': 0.940541, 'd13': 0.148253, 'd23': 0.359681},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=125 label="R6H_SSSSS">, <Entry index=191 label="Others-C_rad_out_Cs2">, <Entry index=199 label="O_H_out">]
[<Entry index=125 label="R6H_SSSSS">, <Entry index=181 label="C_rad_out_H/NonDeC">, <Entry index=211 label="Cs_H_out_2H">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 124,
    label = "R6H_SSSSR",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3    R!H 0 {2,S} {4,S}
4    R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,{S,D,T,B}}
6 *2 R!H 0 {5,{S,D,T,B}} {7,S}
7 *3 H   0 {6,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.264228, 'd13': -0.013414, 'd23': 0.010889},
        uncertainties = {'d12': 0.940541, 'd13': 0.148253, 'd23': 0.359681},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=125 label="R6H_SSSSS">, <Entry index=191 label="Others-C_rad_out_Cs2">, <Entry index=199 label="O_H_out">]
[<Entry index=125 label="R6H_SSSSS">, <Entry index=181 label="C_rad_out_H/NonDeC">, <Entry index=211 label="Cs_H_out_2H">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 125,
    label = "R6H_SSSSS",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3    R!H 0 {2,S} {4,S}
4    R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,S}
6 *2 R!H 0 {5,S} {7,S}
7 *3 H   0 {6,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.264228, 'd13': -0.013414, 'd23': 0.010889},
        uncertainties = {'d12': 0.940541, 'd13': 0.148253, 'd23': 0.359681},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=125 label="R6H_SSSSS">, <Entry index=191 label="Others-C_rad_out_Cs2">, <Entry index=199 label="O_H_out">]
[<Entry index=125 label="R6H_SSSSS">, <Entry index=181 label="C_rad_out_H/NonDeC">, <Entry index=211 label="Cs_H_out_2H">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 126,
    label = "R6H_SSSSS_OO",
    group = 
"""
1 *1 Os 1 {2,S}
2 *4 Os 0 {1,S} {3,S}
3    Cs 0 {2,S} {4,S}
4    Cs 0 {3,S} {5,S}
5 *5 Cs 0 {4,S} {6,S}
6 *2 Cs 0 {5,S} {7,S}
7 *3 H  0 {6,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 127,
    label = "R6H_SSSSS_OO(Cs/Cs)Cs",
    group = 
"""
1 *1 Os 1 {2,S}
2 *4 Os 0 {1,S} {3,S}
3    Cs 0 {2,S} {4,S} {8,S}
4    Cs 0 {3,S} {5,S}
5 *5 Cs 0 {4,S} {6,S}
6 *2 Cs 0 {5,S} {7,S}
7 *3 H  0 {6,S}
8    Cs 0 {3,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 130,
    label = "R6H_SSSSS_OO(Cs/Cs)C(Cs/Cs)",
    group = 
"""
1 *1 Os 1 {2,S}
2 *4 Os 0 {1,S} {3,S}
3    Cs 0 {2,S} {4,S} {8,S}
4    Cs 0 {3,S} {5,S}
5 *5 Cs 0 {4,S} {6,S}
6 *2 Cs 0 {5,S} {7,S} {9,S}
7 *3 H  0 {6,S}
8    Cs 0 {3,S}
9    Cs 0 {6,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 129,
    label = "R6H_SSSSS_OOCCC(Cs/Cs)",
    group = 
"""
1 *1 Os 1 {2,S}
2 *4 Os 0 {1,S} {3,S}
3    Cs 0 {2,S} {4,S}
4    Cs 0 {3,S} {5,S}
5 *5 Cs 0 {4,S} {6,S}
6 *2 Cs 0 {5,S} {7,S} {8,S}
7 *3 H  0 {6,S}
8    Cs 0 {6,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 130,
    label = "R6H_SSSSS_OO(Cs/Cs)C(Cs/Cs)",
    group = 
"""
1 *1 Os 1 {2,S}
2 *4 Os 0 {1,S} {3,S}
3    Cs 0 {2,S} {4,S} {8,S}
4    Cs 0 {3,S} {5,S}
5 *5 Cs 0 {4,S} {6,S}
6 *2 Cs 0 {5,S} {7,S} {9,S}
7 *3 H  0 {6,S}
8    Cs 0 {3,S}
9    Cs 0 {6,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 131,
    label = "R6H_SSSSD",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3    R!H 0 {2,S} {4,S}
4    R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,D}
6 *2 R!H 0 {5,D} {7,S}
7 *3 H   0 {6,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 132,
    label = "R6H_SSSST",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3    R!H 0 {2,S} {4,S}
4    R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,T}
6 *2 R!H 0 {5,T} {7,S}
7 *3 H   0 {6,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 133,
    label = "R6H_SSSSB",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,S}
3    R!H 0 {2,S} {4,S}
4    R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,B}
6 *2 R!H 0 {5,B} {7,S}
7 *3 H   0 {6,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 134,
    label = "R6H_DSSSR",
    group = 
"""
1 *1 R!H 1 {2,D}
2 *4 R!H 0 {1,D} {3,S}
3    R!H 0 {2,S} {4,S}
4    R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,{S,D,T,B}}
6 *2 R!H 0 {5,{S,D,T,B}} {7,S}
7 *3 H   0 {6,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 135,
    label = "R6H_DSSSS",
    group = 
"""
1 *1 R!H 1 {2,D}
2 *4 R!H 0 {1,D} {3,S}
3    R!H 0 {2,S} {4,S}
4    R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,S}
6 *2 R!H 0 {5,S} {7,S}
7 *3 H   0 {6,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 136,
    label = "R6H_DSSSD",
    group = 
"""
1 *1 R!H 1 {2,D}
2 *4 R!H 0 {1,D} {3,S}
3    R!H 0 {2,S} {4,S}
4    R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,D}
6 *2 R!H 0 {5,D} {7,S}
7 *3 H   0 {6,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 137,
    label = "R6H_DSSST",
    group = 
"""
1 *1 R!H 1 {2,D}
2 *4 R!H 0 {1,D} {3,S}
3    R!H 0 {2,S} {4,S}
4    R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,T}
6 *2 R!H 0 {5,T} {7,S}
7 *3 H   0 {6,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 138,
    label = "R6H_DSSSB",
    group = 
"""
1 *1 R!H 1 {2,D}
2 *4 R!H 0 {1,D} {3,S}
3    R!H 0 {2,S} {4,S}
4    R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,B}
6 *2 R!H 0 {5,B} {7,S}
7 *3 H   0 {6,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 139,
    label = "R6H_TSSSR",
    group = 
"""
1 *1 R!H 1 {2,T}
2 *4 R!H 0 {1,T} {3,S}
3    R!H 0 {2,S} {4,S}
4    R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,{S,D,T,B}}
6 *2 R!H 0 {5,{S,D,T,B}} {7,S}
7 *3 H   0 {6,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 140,
    label = "R6H_TSSSS",
    group = 
"""
1 *1 R!H 1 {2,T}
2 *4 R!H 0 {1,T} {3,S}
3    R!H 0 {2,S} {4,S}
4    R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,S}
6 *2 R!H 0 {5,S} {7,S}
7 *3 H   0 {6,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 141,
    label = "R6H_TSSSD",
    group = 
"""
1 *1 R!H 1 {2,T}
2 *4 R!H 0 {1,T} {3,S}
3    R!H 0 {2,S} {4,S}
4    R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,D}
6 *2 R!H 0 {5,D} {7,S}
7 *3 H   0 {6,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 142,
    label = "R6H_TSSST",
    group = 
"""
1 *1 R!H 1 {2,T}
2 *4 R!H 0 {1,T} {3,S}
3    R!H 0 {2,S} {4,S}
4    R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,T}
6 *2 R!H 0 {5,T} {7,S}
7 *3 H   0 {6,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 143,
    label = "R6H_TSSSB",
    group = 
"""
1 *1 R!H 1 {2,T}
2 *4 R!H 0 {1,T} {3,S}
3    R!H 0 {2,S} {4,S}
4    R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,B}
6 *2 R!H 0 {5,B} {7,S}
7 *3 H   0 {6,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 144,
    label = "R6H_BSSSR",
    group = 
"""
1 *1 R!H 1 {2,B}
2 *4 R!H 0 {1,B} {3,S}
3    R!H 0 {2,S} {4,S}
4    R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,{S,D,T,B}}
6 *2 R!H 0 {5,{S,D,T,B}} {7,S}
7 *3 H   0 {6,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 145,
    label = "R6H_BSSSS",
    group = 
"""
1 *1 R!H 1 {2,B}
2 *4 R!H 0 {1,B} {3,S}
3    R!H 0 {2,S} {4,S}
4    R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,S}
6 *2 R!H 0 {5,S} {7,S}
7 *3 H   0 {6,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 146,
    label = "R6H_BSSSD",
    group = 
"""
1 *1 R!H 1 {2,B}
2 *4 R!H 0 {1,B} {3,S}
3    R!H 0 {2,S} {4,S}
4    R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,D}
6 *2 R!H 0 {5,D} {7,S}
7 *3 H   0 {6,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 147,
    label = "R6H_BSSST",
    group = 
"""
1 *1 R!H 1 {2,B}
2 *4 R!H 0 {1,B} {3,S}
3    R!H 0 {2,S} {4,S}
4    R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,T}
6 *2 R!H 0 {5,T} {7,S}
7 *3 H   0 {6,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 148,
    label = "R6H_BSSSB",
    group = 
"""
1 *1 R!H 1 {2,B}
2 *4 R!H 0 {1,B} {3,S}
3    R!H 0 {2,S} {4,S}
4    R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,B}
6 *2 R!H 0 {5,B} {7,S}
7 *3 H   0 {6,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 149,
    label = "R6H_RSSMS",
    group = 
"""
1 *1 R!H 1 {2,{S,D,T,B}}
2 *4 R!H 0 {1,{S,D,T,B}} {3,S}
3    R!H 0 {2,S} {4,S}
4    R!H 0 {3,S} {5,{D,T,B}}
5 *5 R!H 0 {4,{D,T,B}} {6,S}
6 *2 R!H 0 {5,S} {7,S}
7 *3 H   0 {6,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 150,
    label = "R6H_RSMSR",
    group = 
"""
1 *1 R!H 1 {2,{S,D,T,B}}
2 *4 R!H 0 {1,{S,D,T,B}} {3,S}
3    R!H 0 {2,S} {4,{D,T,B}}
4    R!H 0 {3,{D,T,B}} {5,S}
5 *5 R!H 0 {4,S} {6,{S,D,T,B}}
6 *2 R!H 0 {5,{S,D,T,B}} {7,S}
7 *3 H   0 {6,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 151,
    label = "R6H_SMSSR",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,{D,T,B}}
3    R!H 0 {2,{D,T,B}} {4,S}
4    R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,{S,D,T,B}}
6 *2 R!H 0 {5,{S,D,T,B}} {7,S}
7 *3 H   0 {6,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 152,
    label = "R6H_SMSMS",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 R!H 0 {1,S} {3,{D,T,B}}
3    R!H 0 {2,{D,T,B}} {4,S}
4    R!H 0 {3,S} {5,{D,T,B}}
5 *5 R!H 0 {4,{D,T,B}} {6,S}
6 *2 R!H 0 {5,S} {7,S}
7 *3 H   0 {6,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 153,
    label = "R6H_BBSRS",
    group = 
"""
1 *1 Cb  1 {2,B}
2 *4 Cbf 0 {1,B} {3,B}
3    Cb  0 {2,B} {4,S}
4    R!H 0 {3,S} {5,{S,D,T,B}}
5 *5 R!H 0 {4,{S,D,T,B}} {6,S}
6 *2 R!H 0 {5,S} {7,S}
7 *3 H   0 {6,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 154,
    label = "R6H_BBSSM",
    group = 
"""
1 *1 Cb  1 {2,B}
2 *4 Cbf 0 {1,B} {3,B}
3    Cb  0 {2,B} {4,S}
4    R!H 0 {3,S} {5,S}
5 *5 R!H 0 {4,S} {6,{D,T,B}}
6 *2 R!H 0 {5,{D,T,B}} {7,S}
7 *3 H   0 {6,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 155,
    label = "R6H_BBSBB",
    group = 
"""
1 *1 Cb  1 {2,B}
2 *4 Cbf 0 {1,B} {3,B}
3    Cb  0 {2,B} {4,S}
4    Cb  0 {3,S} {5,B}
5 *5 Cbf 0 {4,B} {6,B}
6 *2 Cb  0 {5,B} {7,S}
7 *3 H   0 {6,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 156,
    label = "R6H_SBBSR",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 Cb  0 {1,S} {3,B}
3    Cbf 0 {2,B} {4,B}
4    Cb  0 {3,B} {5,S}
5 *5 R!H 0 {4,S} {6,{S,D,T,B}}
6 *2 R!H 0 {5,{S,D,T,B}} {7,S}
7 *3 H   0 {6,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 157,
    label = "R6H_RSBBS",
    group = 
"""
1 *1 R!H 1 {2,{S,D,T,B}}
2 *4 R!H 0 {1,{S,D,T,B}} {3,S}
3    Cb  0 {2,S} {4,B}
4    Cbf 0 {3,B} {5,B}
5 *5 Cb  0 {4,B} {6,S}
6 *2 R!H 0 {5,S} {7,S}
7 *3 H   0 {6,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 158,
    label = "R6H_BBBSR",
    group = 
"""
1 *1 Cb  1 {2,B}
2 *4 Cbf 0 {1,B} {3,B}
3    Cbf 0 {2,B} {4,B}
4    Cb  0 {3,B} {5,S}
5 *5 R!H 0 {4,S} {6,{S,D,T,B}}
6 *2 R!H 0 {5,{S,D,T,B}} {7,S}
7 *3 H   0 {6,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 159,
    label = "R6H_SBBBS",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 Cb  0 {1,S} {3,B}
3    Cbf 0 {2,B} {4,B}
4    Cbf 0 {3,B} {5,B}
5 *5 Cb  0 {4,B} {6,S}
6 *2 R!H 0 {5,S} {7,S}
7 *3 H   0 {6,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 160,
    label = "R6H_RSBBB",
    group = 
"""
1 *1 R!H 1 {2,{S,D,T,B}}
2 *4 R!H 0 {1,{S,D,T,B}} {3,S}
3    Cb  0 {2,S} {4,B}
4    Cbf 0 {3,B} {5,B}
5 *5 Cbf 0 {4,B} {6,B}
6 *2 Cb  0 {5,B} {7,S}
7 *3 H   0 {6,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 161,
    label = "R6H_SBBBB",
    group = 
"""
1 *1 R!H 1 {2,S}
2 *4 Cb  0 {1,S} {3,B}
3    Cbf 0 {2,B} {4,B}
4    Cbf 0 {3,B} {5,B}
5 *5 Cbf 0 {4,B} {6,B}
6 *2 Cb  0 {5,B} {7,S}
7 *3 H   0 {6,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 162,
    label = "R6H_BBBBS",
    group = 
"""
1 *1 Cb  1 {2,B}
2 *4 Cbf 0 {1,B} {3,B}
3    Cbf 0 {2,B} {4,B}
4    Cbf 0 {3,B} {5,B}
5 *5 Cb  0 {4,B} {6,S}
6 *2 R!H 0 {5,S} {7,S}
7 *3 H   0 {6,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 163,
    label = "R6H_BBBBB",
    group = 
"""
1 *1 Cb  1 {2,B}
2 *4 Cbf 0 {1,B} {3,B}
3    Cbf 0 {2,B} {4,B}
4    Cbf 0 {3,B} {5,B}
5 *5 Cbf 0 {4,B} {6,B}
6 *2 Cb  0 {5,B} {7,S}
7 *3 H   0 {6,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 164,
    label = "R7H",
    group = 
"""
1 *1 R!H 1 {2,{S,D,T,B}}
2 *4 R!H 0 {1,{S,D,T,B}} {3,{S,D,T,B}}
3    R!H 0 {2,{S,D,T,B}} {4,{S,D,T,B}}
4    R!H 0 {3,{S,D,T,B}} {5,{S,D,T,B}}
5    R!H 0 {4,{S,D,T,B}} {6,{S,D,T,B}}
6 *5 R!H 0 {5,{S,D,T,B}} {7,{S,D,T,B}}
7 *2 R!H 0 {6,{S,D,T,B}} {8,S}
8 *3 H   0 {7,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.265539, 'd13': -0.005884, 'd23': -0.075617},
        uncertainties = {'d12': 0.579275, 'd13': 1.125309, 'd23': 0.955315},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=164 label="R7H">, <Entry index=179 label="C_rad_out_2H">, <Entry index=199 label="O_H_out">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 165,
    label = "R7H_OOCs4",
    group = 
"""
1 *1 Os  1 {2,S}
2 *4 Os  0 {1,S} {3,S}
3    R!H 0 {2,S} {4,{S,D,T,B}}
4    R!H 0 {3,{S,D,T,B}} {5,{S,D,T,B}}
5    R!H 0 {4,{S,D,T,B}} {6,{S,D,T,B}}
6 *5 R!H 0 {5,{S,D,T,B}} {7,{S,D,T,B}}
7 *2 R!H 0 {6,{S,D,T,B}} {8,S}
8 *3 H   0 {7,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 166,
    label = "R7H_OOCCCC(Cs/Cs)",
    group = 
"""
1 *1 Os  1 {2,S}
2 *4 Os  0 {1,S} {3,S}
3    R!H 0 {2,S} {4,{S,D,T,B}}
4    R!H 0 {3,{S,D,T,B}} {5,{S,D,T,B}}
5    R!H 0 {4,{S,D,T,B}} {6,{S,D,T,B}}
6 *5 R!H 0 {5,{S,D,T,B}} {7,{S,D,T,B}}
7 *2 R!H 0 {6,{S,D,T,B}} {8,S} {9,S}
8 *3 H   0 {7,S}
9    Cs  0 {7,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 167,
    label = "O_rad_out",
    group = 
"""
1 *1 O 1
""",
    distances = DistanceData(
        distances = {'d12': -0.046796, 'd13': -0.056767, 'd23': -0.051092},
        uncertainties = {'d12': 0.678492, 'd13': 0.345512, 'd23': 0.203413},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=38 label="R4H_SSS">, <Entry index=167 label="O_rad_out">, <Entry index=213 label="Cs_H_out_H/NonDeC">]
[<Entry index=73 label="R5H_CCCC_O">, <Entry index=167 label="O_rad_out">, <Entry index=210 label="Cs_H_out">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 168,
    label = "S_rad_out",
    group = 
"""
1 *1 S 1
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 169,
    label = "Cd_rad_out_double",
    group = 
"""
1 *1 Cd 1 {2,D}
2    Cd 0 {1,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 170,
    label = "Cd_rad_out_single",
    group = 
"""
1 *1 Cd 1 {2,S}
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
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 171,
    label = "Cd_rad_out_singleH",
    group = 
"""
1 *1 Cd 1 {2,S}
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
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 172,
    label = "Cd_rad_out_singleNd",
    group = 
"""
1 *1 Cd       1 {2,S}
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
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 173,
    label = "Cd_rad_out_singleDe",
    group = 
"""
1 *1 Cd            1 {2,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 174,
    label = "Ct_rad_out",
    group = 
"""
1 *1 Ct 1 {2,T}
2 *4 Ct 0 {1,T}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 175,
    label = "Cb_rad_out",
    group = 
"""
1 *1 Cb       1 {2,B}
2 *4 {Cb,Cbf} 0 {1,B}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 176,
    label = "CO_rad_out",
    group = 
"""
1 *1 C 1 {2,D}
2    O 0 {1,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 177,
    label = "C=S_rad_out",
    group = 
"""
1 *1 Cd 1 {2,D}
2    Sd 0 {1,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 178,
    label = "C_rad_out_single",
    group = 
"""
1 *1 C 1 {2,S} {3,S}
2    R 0 {1,S}
3    R 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.011011, 'd13': 0.013357, 'd23': 0.012022},
        uncertainties = {'d12': 0.16215, 'd13': 0.072741, 'd23': 0.06791},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 10 distances.
[<Entry index=26 label="Others-R3H_SS">, <Entry index=181 label="C_rad_out_H/NonDeC">, <Entry index=199 label="O_H_out">]
[<Entry index=125 label="R6H_SSSSS">, <Entry index=181 label="C_rad_out_H/NonDeC">, <Entry index=211 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=179 label="C_rad_out_2H">, <Entry index=210 label="Cs_H_out">]
[<Entry index=72 label="R5H_SSSS">, <Entry index=181 label="C_rad_out_H/NonDeC">, <Entry index=211 label="Cs_H_out_2H">]
[<Entry index=125 label="R6H_SSSSS">, <Entry index=191 label="Others-C_rad_out_Cs2">, <Entry index=199 label="O_H_out">]
[<Entry index=164 label="R7H">, <Entry index=179 label="C_rad_out_2H">, <Entry index=199 label="O_H_out">]
[<Entry index=26 label="Others-R3H_SS">, <Entry index=179 label="C_rad_out_2H">, <Entry index=214 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=179 label="C_rad_out_2H">, <Entry index=214 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=38 label="R4H_SSS">, <Entry index=179 label="C_rad_out_2H">, <Entry index=214 label="Cs_H_out_H/(NonDeC/Cs)">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 179,
    label = "C_rad_out_2H",
    group = 
"""
1 *1 C 1 {2,S} {3,S}
2    H 0 {1,S}
3    H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.011478, 'd13': 0.019908, 'd23': 0.018479},
        uncertainties = {'d12': 0.13711, 'd13': 0.10601, 'd23': 0.094331},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 6 distances.
[<Entry index=9 label="Others-R2H_S">, <Entry index=179 label="C_rad_out_2H">, <Entry index=210 label="Cs_H_out">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=179 label="C_rad_out_2H">, <Entry index=214 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=164 label="R7H">, <Entry index=179 label="C_rad_out_2H">, <Entry index=199 label="O_H_out">]
[<Entry index=38 label="R4H_SSS">, <Entry index=179 label="C_rad_out_2H">, <Entry index=214 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=26 label="Others-R3H_SS">, <Entry index=179 label="C_rad_out_2H">, <Entry index=214 label="Cs_H_out_H/(NonDeC/Cs)">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 180,
    label = "C_rad_out_1H",
    group = 
"""
1 *1 C   1 {2,S} {3,S}
2    H   0 {1,S}
3    R!H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.049769, 'd13': -0.002845, 'd23': 0.020086},
        uncertainties = {'d12': 0.533232, 'd13': 0.08068, 'd23': 0.073561},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 3 distances.
[<Entry index=26 label="Others-R3H_SS">, <Entry index=181 label="C_rad_out_H/NonDeC">, <Entry index=199 label="O_H_out">]
[<Entry index=72 label="R5H_SSSS">, <Entry index=181 label="C_rad_out_H/NonDeC">, <Entry index=211 label="Cs_H_out_2H">]
[<Entry index=125 label="R6H_SSSSS">, <Entry index=181 label="C_rad_out_H/NonDeC">, <Entry index=211 label="Cs_H_out_2H">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 181,
    label = "C_rad_out_H/NonDeC",
    group = 
"""
1 *1 C  1 {2,S} {3,S}
2    H  0 {1,S}
3    Cs 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.049769, 'd13': -0.002845, 'd23': 0.020086},
        uncertainties = {'d12': 0.533232, 'd13': 0.08068, 'd23': 0.073561},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 3 distances.
[<Entry index=26 label="Others-R3H_SS">, <Entry index=181 label="C_rad_out_H/NonDeC">, <Entry index=199 label="O_H_out">]
[<Entry index=72 label="R5H_SSSS">, <Entry index=181 label="C_rad_out_H/NonDeC">, <Entry index=211 label="Cs_H_out_2H">]
[<Entry index=125 label="R6H_SSSSS">, <Entry index=181 label="C_rad_out_H/NonDeC">, <Entry index=211 label="Cs_H_out_2H">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 182,
    label = "C_rad_out_H/NonDeO",
    group = 
"""
1 *1 C 1 {2,S} {3,S}
2    H 0 {1,S}
3    O 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 183,
    label = "C_rad_out_H/NonDeS",
    group = 
"""
1 *1 C 1 {2,S} {3,S}
2    H 0 {1,S}
3    S 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 184,
    label = "C_rad_out_H/OneDe",
    group = 
"""
1 *1 C             1 {2,S} {3,S}
2    H             0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 185,
    label = "C_rad_out_noH",
    group = 
"""
1 *1 C   1 {2,S} {3,S}
2    R!H 0 {1,S}
3    R!H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.049385, 'd13': 0.02183, 'd23': -0.075767},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=125 label="R6H_SSSSS">, <Entry index=191 label="Others-C_rad_out_Cs2">, <Entry index=199 label="O_H_out">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 186,
    label = "C_rad_out_NonDe",
    group = 
"""
1 *1 C        1 {2,S} {3,S}
2    {Cs,O,S} 0 {1,S}
3    {Cs,O,S} 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.049385, 'd13': 0.02183, 'd23': -0.075767},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=125 label="R6H_SSSSS">, <Entry index=191 label="Others-C_rad_out_Cs2">, <Entry index=199 label="O_H_out">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 187,
    label = "C_rad_out_Cs2",
    group = 
"""
1 *1 C  1 {2,S} {3,S}
2    Cs 0 {1,S}
3    Cs 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.049385, 'd13': 0.02183, 'd23': -0.075767},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=125 label="R6H_SSSSS">, <Entry index=191 label="Others-C_rad_out_Cs2">, <Entry index=199 label="O_H_out">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 188,
    label = "C_rad_out_Cs2_cy3",
    group = 
"""
1 *1 C  1 {2,S} {3,S}
2    Cs 0 {1,S} {3,S}
3    Cs 0 {1,S} {2,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 189,
    label = "C_rad_out_Cs2_cy4",
    group = 
"""
1 *1 C       1 {2,S} {3,S}
2    Cs      0 {1,S} {4,S}
3    Cs      0 {1,S} {4,S}
4    {Cs,Cd} 0 {2,S} {3,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 190,
    label = "C_rad_out_Cs2_cy5",
    group = 
"""
1 *1 C             1 {2,S} {3,S}
2    Cs            0 {1,S} {4,S}
3    Cs            0 {1,S} {5,S}
4    {Cs,Cd,Cb,Ct} 0 {2,S} {5,{S,D,T,B}}
5    {Cs,Cd,Cb,Ct} 0 {3,S} {4,{S,D,T,B}}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 191,
    label = "Others-C_rad_out_Cs2",
    group = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    distances = DistanceData(
        distances = {'d12': 0.049385, 'd13': 0.02183, 'd23': -0.075767},
        uncertainties = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=125 label="R6H_SSSSS">, <Entry index=191 label="Others-C_rad_out_Cs2">, <Entry index=199 label="O_H_out">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 192,
    label = "C_rad_out_NDMustO",
    group = 
"""
1 *1 C        1 {2,S} {3,S}
2    O        0 {1,S}
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
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 193,
    label = "C_rad_out_OneDe",
    group = 
"""
1 *1 C             1 {2,S} {3,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    {Cs,O,S}      0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 194,
    label = "C_rad_out_OneDe/Cs",
    group = 
"""
1 *1 C             1 {2,S} {3,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    Cs            0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 195,
    label = "C_rad_out_OneDe/O",
    group = 
"""
1 *1 C             1 {2,S} {3,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    O             0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 196,
    label = "C_rad_out_OneDe/S",
    group = 
"""
1 *1 C             1 {2,S} {3,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    S             0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 197,
    label = "C_rad_out_TwoDe",
    group = 
"""
1 *1 C             1 {2,S} {3,S}
2    {Cd,Ct,Cb,CO} 0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 198,
    label = "CO_H_out",
    group = 
"""
1 *2 CO 0 {2,S}
2 *3 H  0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 199,
    label = "O_H_out",
    group = 
"""
1 *2 O 0 {2,S}
2 *3 H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.033615, 'd13': -0.014553, 'd23': -0.060682},
        uncertainties = {'d12': 0.272006, 'd13': 0.169049, 'd23': 0.150687},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 4 distances.
[<Entry index=26 label="Others-R3H_SS">, <Entry index=181 label="C_rad_out_H/NonDeC">, <Entry index=199 label="O_H_out">]
[<Entry index=125 label="R6H_SSSSS">, <Entry index=191 label="Others-C_rad_out_Cs2">, <Entry index=199 label="O_H_out">]
[<Entry index=164 label="R7H">, <Entry index=179 label="C_rad_out_2H">, <Entry index=199 label="O_H_out">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 200,
    label = "Ct_H_out",
    group = 
"""
1 *2 Ct 0 {2,S}
2 *3 H  0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 201,
    label = "Cb_H_out",
    group = 
"""
1 *2 Cb 0 {2,S}
2 *3 H  0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 202,
    label = "S_H_out",
    group = 
"""
1 *2 S 0 {2,S}
2 *3 H 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 203,
    label = "Cd_H_out_double",
    group = 
"""
1 *2 Cd     0 {2,S} {3,D}
2 *3 H      0 {1,S}
3    {Cd,O} 0 {1,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 204,
    label = "Cd_H_out_doubleC",
    group = 
"""
1 *2 Cd 0 {2,S} {3,D}
2 *3 H  0 {1,S}
3    Cd 0 {1,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 205,
    label = "Cd_H_out_doubleO",
    group = 
"""
1 *2 Cd 0 {2,S} {3,D}
2 *3 H  0 {1,S}
3    O  0 {1,D}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 206,
    label = "Cd_H_out_single",
    group = 
"""
1 *2 Cd 0 {2,S} {3,S}
2 *3 H  0 {1,S}
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
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 207,
    label = "Cd_H_out_singleH",
    group = 
"""
1 *2 Cd 0 {2,S} {3,S}
2 *3 H  0 {1,S}
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
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 208,
    label = "Cd_H_out_singleNd",
    group = 
"""
1 *2 Cd     0 {2,S} {3,S}
2 *3 H      0 {1,S}
3    {Cs,O} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 209,
    label = "Cd_H_out_singleDe",
    group = 
"""
1 *2 Cd            0 {2,S} {3,S}
2 *3 H             0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 210,
    label = "Cs_H_out",
    group = 
"""
1 *2 Cs 0 {2,S} {3,S} {4,S}
2 *3 H  0 {1,S}
3    R  0 {1,S}
4    R  0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.017967, 'd13': 0.007779, 'd23': 0.032433},
        uncertainties = {'d12': 0.147337, 'd13': 0.03553, 'd23': 0.036207},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 8 distances.
[<Entry index=125 label="R6H_SSSSS">, <Entry index=181 label="C_rad_out_H/NonDeC">, <Entry index=211 label="Cs_H_out_2H">]
[<Entry index=73 label="R5H_CCCC_O">, <Entry index=167 label="O_rad_out">, <Entry index=210 label="Cs_H_out">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=179 label="C_rad_out_2H">, <Entry index=210 label="Cs_H_out">]
[<Entry index=72 label="R5H_SSSS">, <Entry index=181 label="C_rad_out_H/NonDeC">, <Entry index=211 label="Cs_H_out_2H">]
[<Entry index=38 label="R4H_SSS">, <Entry index=167 label="O_rad_out">, <Entry index=213 label="Cs_H_out_H/NonDeC">]
[<Entry index=26 label="Others-R3H_SS">, <Entry index=179 label="C_rad_out_2H">, <Entry index=214 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=179 label="C_rad_out_2H">, <Entry index=214 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=38 label="R4H_SSS">, <Entry index=179 label="C_rad_out_2H">, <Entry index=214 label="Cs_H_out_H/(NonDeC/Cs)">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 211,
    label = "Cs_H_out_2H",
    group = 
"""
1 *2 Cs 0 {2,S} {3,S} {4,S}
2 *3 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.1301, 'd13': 0.00855, 'd23': 0.045533},
        uncertainties = {'d12': 1.402253, 'd13': 0.170936, 'd23': 0.22177},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=72 label="R5H_SSSS">, <Entry index=181 label="C_rad_out_H/NonDeC">, <Entry index=211 label="Cs_H_out_2H">]
[<Entry index=125 label="R6H_SSSSS">, <Entry index=181 label="C_rad_out_H/NonDeC">, <Entry index=211 label="Cs_H_out_2H">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 212,
    label = "Cs_H_out_1H",
    group = 
"""
1 *2 Cs  0 {2,S} {3,S} {4,S}
2 *3 H   0 {1,S}
3    R!H 0 {1,S}
4    H   0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.01868, 'd13': 0.013555, 'd23': 0.036165},
        uncertainties = {'d12': 0.222077, 'd13': 0.051875, 'd23': 0.053968},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 4 distances.
[<Entry index=38 label="R4H_SSS">, <Entry index=167 label="O_rad_out">, <Entry index=213 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=179 label="C_rad_out_2H">, <Entry index=214 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=38 label="R4H_SSS">, <Entry index=179 label="C_rad_out_2H">, <Entry index=214 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=26 label="Others-R3H_SS">, <Entry index=179 label="C_rad_out_2H">, <Entry index=214 label="Cs_H_out_H/(NonDeC/Cs)">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 213,
    label = "Cs_H_out_H/NonDeC",
    group = 
"""
1 *2 Cs 0 {2,S} {3,S} {4,S}
2 *3 H  0 {1,S}
3    Cs 0 {1,S}
4    H  0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.01868, 'd13': 0.013555, 'd23': 0.036165},
        uncertainties = {'d12': 0.222077, 'd13': 0.051875, 'd23': 0.053968},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 4 distances.
[<Entry index=38 label="R4H_SSS">, <Entry index=167 label="O_rad_out">, <Entry index=213 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=179 label="C_rad_out_2H">, <Entry index=214 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=38 label="R4H_SSS">, <Entry index=179 label="C_rad_out_2H">, <Entry index=214 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=26 label="Others-R3H_SS">, <Entry index=179 label="C_rad_out_2H">, <Entry index=214 label="Cs_H_out_H/(NonDeC/Cs)">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 214,
    label = "Cs_H_out_H/(NonDeC/Cs)",
    group = 
"""
1 *2 Cs 0 {2,S} {3,S} {4,S}
2 *3 H  0 {1,S}
3    Cs 0 {1,S} {5,S}
4    H  0 {1,S}
5    Cs 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.011076, 'd13': 0.022571, 'd23': 0.044702},
        uncertainties = {'d12': 0.332794, 'd13': 0.078022, 'd23': 0.08012},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 3 distances.
[<Entry index=9 label="Others-R2H_S">, <Entry index=179 label="C_rad_out_2H">, <Entry index=214 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=38 label="R4H_SSS">, <Entry index=179 label="C_rad_out_2H">, <Entry index=214 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=26 label="Others-R3H_SS">, <Entry index=179 label="C_rad_out_2H">, <Entry index=214 label="Cs_H_out_H/(NonDeC/Cs)">]
""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 215,
    label = "Cs_H_out_H/(NonDeC/Cs/Cs)",
    group = 
"""
1 *2 Cs 0 {2,S} {3,S} {4,S}
2 *3 H  0 {1,S}
3    Cs 0 {1,S} {5,S} {6,S}
4    H  0 {1,S}
5    Cs 0 {3,S}
6    Cs 0 {3,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 216,
    label = "Cs_H_out_H/(NonDeC/Cs/Cs/Cs)",
    group = 
"""
1 *2 Cs 0 {2,S} {3,S} {4,S}
2 *3 H  0 {1,S}
3    Cs 0 {1,S} {5,S} {6,S} {7,S}
4    H  0 {1,S}
5    Cs 0 {3,S}
6    Cs 0 {3,S}
7    Cs 0 {3,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 217,
    label = "Cs_H_out_H/NonDeO",
    group = 
"""
1 *2 Cs 0 {2,S} {3,S} {4,S}
2 *3 H  0 {1,S}
3    O  0 {1,S}
4    H  0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 218,
    label = "Cs_H_out_OOH/H",
    group = 
"""
1 *2 Cs 0 {2,S} {3,S} {4,S}
2 *3 H  0 {1,S}
3    H  0 {1,S}
4    O  0 {1,S} {5,S}
5    O  0 {4,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 219,
    label = "Cs_H_out_H/NonDeS",
    group = 
"""
1 *2 Cs 0 {2,S} {3,S} {4,S}
2 *3 H  0 {1,S}
3    S  0 {1,S}
4    H  0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 220,
    label = "Cs_H_out_H/OneDe",
    group = 
"""
1 *2 Cs            0 {2,S} {3,S} {4,S}
2 *3 H             0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    H             0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 221,
    label = "Cs_H_out_OOH",
    group = 
"""
1 *2 Cs 0 {2,S} {3,S} {4,S}
2 *3 H  0 {1,S}
3    R  0 {1,S}
4    O  0 {1,S} {5,S}
5    O  0 {4,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 222,
    label = "Cs_H_out_OOH/Cs",
    group = 
"""
1 *2 Cs 0 {2,S} {3,S} {4,S}
2 *3 H  0 {1,S}
3    Cs 0 {1,S}
4    O  0 {1,S} {5,S}
5    O  0 {4,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 223,
    label = "Cs_H_out_noH",
    group = 
"""
1 *2 Cs  0 {2,S} {3,S} {4,S} {5,S}
2 *3 H   0 {1,S}
3    R!H 0 {1,S}
4    R!H 0 {1,S}
5    R!H 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 224,
    label = "Cs_H_out_NonDe",
    group = 
"""
1 *2 Cs     0 {2,S} {3,S} {4,S} {5,S}
2 *3 H      0 {1,S}
3    {Cs,O} 0 {1,S}
4    {Cs,O} 0 {1,S}
5    R!H    0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 225,
    label = "Cs_H_out_Cs2",
    group = 
"""
1 *2 Cs  0 {2,S} {3,S} {4,S} {5,S}
2 *3 H   0 {1,S}
3    Cs  0 {1,S}
4    Cs  0 {1,S}
5    R!H 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 226,
    label = "Cs_H_out_Cs2_cy3",
    group = 
"""
1 *2 Cs  0 {2,S} {3,S} {4,S} {5,S}
2 *3 H   0 {1,S}
3    Cs  0 {1,S} {4,S}
4    Cs  0 {1,S} {3,S}
5    R!H 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 227,
    label = "Cs_H_out_Cs2_cy4",
    group = 
"""
1 *2 Cs  0 {2,S} {3,S} {4,S} {6,S}
2 *3 H   0 {1,S}
3    Cs  0 {1,S} {5,S}
4    Cs  0 {1,S} {5,S}
5    Cs  0 {3,S} {4,S}
6    R!H 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 228,
    label = "Cs_H_out_Cs2_cy5",
    group = 
"""
1 *2 Cs  0 {2,S} {3,S} {4,S} {7,S}
2 *3 H   0 {1,S}
3    Cs  0 {1,S} {5,S}
4    Cs  0 {1,S} {6,S}
5    Cs  0 {3,S} {6,S}
6    Cs  0 {4,S} {5,S}
7    R!H 0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 229,
    label = "Others-Cs_H_out_Cs2",
    group = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 230,
    label = "Cs_H_out_NDMustO",
    group = 
"""
1 *2 Cs     0 {2,S} {3,S} {4,S} {5,S}
2 *3 H      0 {1,S}
3    O      0 {1,S}
4    {Cs,O} 0 {1,S}
5    R!H    0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 231,
    label = "Cs_H_out_OneDe",
    group = 
"""
1 *2 Cs            0 {2,S} {3,S} {4,S} {5,S}
2 *3 H             0 {1,S}
3    {Cs,O}        0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    R!H           0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

entry(
    index = 232,
    label = "Cs_H_out_TwoDe",
    group = 
"""
1 *2 Cs            0 {2,S} {3,S} {4,S} {5,S}
2 *3 H             0 {1,S}
3    {Cd,Ct,Cb,CO} 0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
5    R!H           0 {1,S}
""",
    distances = DistanceData(distances={}),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jan 14 10:45:30 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Created from kinetics groups."""),
    ],
)

tree(
"""
L1: RnH
    L2: R2H
        L3: R2H_S
            L4: R2H_S_cy3
            L4: R2H_S_cy4
            L4: R2H_S_cy5
            L4: Others-R2H_S
        L3: R2H_D
        L3: R2H_B
    L2: R3H
        L3: R3H_SR
            L4: R3H_SS
                L5: R3H_SS_12cy3
                L5: R3H_SS_23cy3
                L5: R3H_SS_12cy4
                L5: R3H_SS_23cy4
                L5: R3H_SS_13cy4
                L5: R3H_SS_12cy5
                L5: R3H_SS_23cy5
                L5: R3H_SS_13cy5
                L5: R3H_SS_2Cd
                L5: R3H_SS_OC
                L5: R3H_SS_S
                L5: Others-R3H_SS
            L4: R3H_SD
            L4: R3H_ST
            L4: R3H_SB
        L3: R3H_MS
            L4: R3H_DS
            L4: R3H_TS
            L4: R3H_BS
        L3: R3H_BB
    L2: R4H
        L3: R4H_RSR
            L4: R4H_RSS
                L5: R4H_SSS
                    L6: R4H_SSS_CsSCsCs
                    L6: R4H_SSS_CsCsSCs
                    L6: R4H_SSS_OOCsCs
                        L7: R4H_SSS_OO(Cs/Cs)Cs
                            L8: R4H_SSS_OO(Cs/Cs/Cs)Cs
                L5: R4H_DSS
                L5: R4H_TSS
                L5: R4H_BSS
            L4: R4H_RSD
                L5: R4H_SSD
                L5: R4H_DSD
                L5: R4H_TSD
                L5: R4H_BSD
            L4: R4H_RST
                L5: R4H_SST
                L5: R4H_DST
                L5: R4H_TST
                L5: R4H_BST
            L4: R4H_RSB
                L5: R4H_SSB
                L5: R4H_DSB
                L5: R4H_TSB
                L5: R4H_BSB
        L3: R4H_SMS
            L4: R4H_SDS
            L4: R4H_STS
            L4: R4H_SBS
        L3: R4H_SBB
        L3: R4H_BBS
        L3: R4H_BBB
    L2: R5H
        L3: R5H_RSSR
            L4: R5H_SSSR
                L5: R5H_SSSS
                    L6: R5H_CCCC_O
                    L6: R5H_SSSS_CsCsCsSCs
                    L6: R5H_SSSS_OOCCC
                        L7: R5H_SSSS_OO(Cs/Cs)Cs
                            L8: R5H_SSSS_OO(Cs/Cs/Cs)Cs
                        L7: R5H_SSSS_OOCs(Cs/Cs)
                            L8: R5H_SSSS_OOCs(Cs/Cs/Cs)
                L5: R5H_SSSD
                L5: R5H_SSST
                L5: R5H_SSSB
            L4: R5H_DSSR
                L5: R5H_DSSS
                L5: R5H_DSSD
                L5: R5H_DSST
                L5: R5H_DSSB
            L4: R5H_TSSR
                L5: R5H_TSSS
                L5: R5H_TSSD
                L5: R5H_TSST
                L5: R5H_TSSB
            L4: R5H_BSSR
                L5: R5H_BSSS
                L5: R5H_BSSD
                L5: R5H_BSST
                L5: R5H_BSSB
        L3: R5H_RSMS
            L4: R5H_SSMS
            L4: R5H_DSMS
            L4: R5H_TSMS
            L4: R5H_BSMS
        L3: R5H_SMSR
            L4: R5H_SMSS
            L4: R5H_SMSD
            L4: R5H_SMST
            L4: R5H_SMSB
        L3: R5H_BBSR
            L4: R5H_BBSS
            L4: R5H_BBSD
            L4: R5H_BBST
            L4: R5H_BBSB
        L3: R5H_RSBB
            L4: R5H_SSBB
            L4: R5H_DSBB
            L4: R5H_TSBB
            L4: R5H_BSBB
        L3: R5H_SBBS
        L3: R5H_SBBB
        L3: R5H_BBBS
        L3: R5H_BBBB
    L2: R6H
        L3: R6H_RSSSR
            L4: R6H_SSSSR
                L5: R6H_SSSSS
                    L6: R6H_SSSSS_OO
                        L7: R6H_SSSSS_OO(Cs/Cs)Cs
                            L8: R6H_SSSSS_OO(Cs/Cs)C(Cs/Cs)
                        L7: R6H_SSSSS_OOCCC(Cs/Cs)
                            L8: R6H_SSSSS_OO(Cs/Cs)C(Cs/Cs)
                L5: R6H_SSSSD
                L5: R6H_SSSST
                L5: R6H_SSSSB
            L4: R6H_DSSSR
                L5: R6H_DSSSS
                L5: R6H_DSSSD
                L5: R6H_DSSST
                L5: R6H_DSSSB
            L4: R6H_TSSSR
                L5: R6H_TSSSS
                L5: R6H_TSSSD
                L5: R6H_TSSST
                L5: R6H_TSSSB
            L4: R6H_BSSSR
                L5: R6H_BSSSS
                L5: R6H_BSSSD
                L5: R6H_BSSST
                L5: R6H_BSSSB
        L3: R6H_RSSMS
        L3: R6H_RSMSR
        L3: R6H_SMSSR
        L3: R6H_SMSMS
        L3: R6H_BBSRS
        L3: R6H_BBSSM
        L3: R6H_BBSBB
        L3: R6H_SBBSR
        L3: R6H_RSBBS
        L3: R6H_BBBSR
        L3: R6H_SBBBS
        L3: R6H_RSBBB
        L3: R6H_SBBBB
        L3: R6H_BBBBS
        L3: R6H_BBBBB
    L2: R7H
        L3: R7H_OOCs4
            L4: R7H_OOCCCC(Cs/Cs)
L1: Y_rad_out
    L2: O_rad_out
    L2: S_rad_out
    L2: Cd_rad_out_double
    L2: Cd_rad_out_single
        L3: Cd_rad_out_singleH
        L3: Cd_rad_out_singleNd
        L3: Cd_rad_out_singleDe
    L2: Ct_rad_out
    L2: Cb_rad_out
    L2: CO_rad_out
    L2: C=S_rad_out
    L2: C_rad_out_single
        L3: C_rad_out_2H
        L3: C_rad_out_1H
            L4: C_rad_out_H/NonDeC
            L4: C_rad_out_H/NonDeO
            L4: C_rad_out_H/NonDeS
            L4: C_rad_out_H/OneDe
        L3: C_rad_out_noH
            L4: C_rad_out_NonDe
                L5: C_rad_out_Cs2
                    L6: C_rad_out_Cs2_cy3
                    L6: C_rad_out_Cs2_cy4
                    L6: C_rad_out_Cs2_cy5
                    L6: Others-C_rad_out_Cs2
                L5: C_rad_out_NDMustO
            L4: C_rad_out_OneDe
                L5: C_rad_out_OneDe/Cs
                L5: C_rad_out_OneDe/O
                L5: C_rad_out_OneDe/S
            L4: C_rad_out_TwoDe
L1: XH_out
    L2: CO_H_out
    L2: O_H_out
    L2: Ct_H_out
    L2: Cb_H_out
    L2: S_H_out
    L2: Cd_H_out_double
        L3: Cd_H_out_doubleC
        L3: Cd_H_out_doubleO
    L2: Cd_H_out_single
        L3: Cd_H_out_singleH
        L3: Cd_H_out_singleNd
        L3: Cd_H_out_singleDe
    L2: Cs_H_out
        L3: Cs_H_out_2H
        L3: Cs_H_out_1H
            L4: Cs_H_out_H/NonDeC
                L5: Cs_H_out_H/(NonDeC/Cs)
                    L6: Cs_H_out_H/(NonDeC/Cs/Cs)
                        L7: Cs_H_out_H/(NonDeC/Cs/Cs/Cs)
            L4: Cs_H_out_H/NonDeO
                L5: Cs_H_out_OOH/H
            L4: Cs_H_out_H/NonDeS
            L4: Cs_H_out_H/OneDe
        L3: Cs_H_out_OOH
            L4: Cs_H_out_OOH/Cs
        L3: Cs_H_out_noH
            L4: Cs_H_out_NonDe
                L5: Cs_H_out_Cs2
                    L6: Cs_H_out_Cs2_cy3
                    L6: Cs_H_out_Cs2_cy4
                    L6: Cs_H_out_Cs2_cy5
                    L6: Others-Cs_H_out_Cs2
                L5: Cs_H_out_NDMustO
            L4: Cs_H_out_OneDe
            L4: Cs_H_out_TwoDe
"""
)

