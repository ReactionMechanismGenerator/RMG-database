#!/usr/bin/env python
# encoding: utf-8

name = "Ring Corrections"
shortDesc = ""
longDesc = """

"""
entry(
    index = 0,
    label = "Ring",
    group = 
"""
1 * R u0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """Dummy Root""",
    longDesc = 
"""

""",
    rank = 10,
)

entry(
    index = 1,
    label = "Aromatic",
    group = 
"""
1 * Cb u0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """Aromatic""",
    longDesc = 
"""
Ring correction is zero because RMG uses Cb group corrections instead in the case of a ring containing Cb bonds
""",
    rank = 1,
)

entry(
    index = 2,
    label = "Benzene",
    group = 
"""
1 * Cb u0 {2,B} {6,B}
2   Cb u0 {1,B} {3,B}
3   Cb u0 {2,B} {4,B}
4   Cb u0 {3,B} {5,B}
5   Cb u0 {4,B} {6,B}
6   Cb u0 {1,B} {5,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """Aromatic""",
    longDesc = 
"""
Ring correction is zero because RMG uses Cb group corrections instead in the case of a ring containing Cb bonds
""",
    rank = 1,
)

entry(
    index = 3,
    label = "ThreeMember",
    group = 
"""
1 * R!H u0 {2,[S,D,T]} {3,[S,D]}
2   R!H u0 {1,[S,D,T]} {3,[S,D]}
3   R!H u0 {1,[S,D]} {2,[S,D]}
""",
    thermo = 'Cyclopropane',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 4,
    label = "Cyclopropane",
    group = 
"""
1 * Cs u0 {2,S} {3,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.227,-2.849,-2.536,-2.35,-2.191,-2.111,-1.76],'cal/(mol*K)'),
        H298 = (27.53,'kcal/mol'),
        S298 = (32.0088,'cal/(mol*K)'),
    ),
    shortDesc = """Cyclopropane ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 5,
    label = "Cs-Cs-Cs(C-BrBrBr)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2   Cs   u0 p0 c0 {1,S} {3,S} {4,S}
3   Cs   u0 p0 c0 {2,S} {4,S}
4 * Cs   u0 p0 c0 {2,S} {3,S}
5   Br1s u0 p3 c0 {1,S}
6   Br1s u0 p3 c0 {1,S}
7   Br1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 6,
    label = "Cs(Br)-Cs-Cs(O2)",
    group = 
"""
1 * Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {3,S} {4,S}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Br1s u0 p3 c0 {2,S}
5   O2s  u0 p2 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 7,
    label = "Cs(Br)(Br)-Cs-Cs(O2)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cs   u0 p0 c0 {1,S} {3,S} {6,S}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Br1s u0 p3 c0 {1,S}
5   Br1s u0 p3 c0 {1,S}
6   O2s  u0 p2 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 8,
    label = "Cs-Cs-Cs(Br)(C)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {3,S}
3 * Cs   u0 p0 c0 {1,S} {2,S}
4   Br1s u0 p3 c0 {1,S}
5   Cs   u0 p0 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 9,
    label = "Cs-Cs(C)-Cs(Br)",
    group = 
"""
1 * Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {3,S} {4,S}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Br1s u0 p3 c0 {2,S}
5   Cs   u0 p0 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 10,
    label = "Cs(C)-Cs-Cs(Br)(Br)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {3,S} {6,S}
3 * Cs   u0 p0 c0 {1,S} {2,S}
4   Br1s u0 p3 c0 {1,S}
5   Br1s u0 p3 c0 {1,S}
6   Cs   u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 11,
    label = "Cs-Cs-Cs(Br)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2 * Cs   u0 p0 c0 {1,S} {3,S}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Br1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 12,
    label = "Cs-Cs-Cs(Br)(Br)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cs   u0 p0 c0 {1,S} {3,S}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Br1s u0 p3 c0 {1,S}
5   Br1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 13,
    label = "Cs-Cs(Br)(O2)-Cs",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {3,S}
3 * Cs   u0 p0 c0 {1,S} {2,S}
4   O2s  u0 p2 c0 {1,S}
5   Br1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 14,
    label = "Cs-Cs-Cs(C-BrBr)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs   u0 p0 c0 {1,S} {5,S} {6,S}
3   Cs   u0 p0 c0 {1,S} {4,S}
4 * Cs   u0 p0 c0 {1,S} {3,S}
5   Br1s u0 p3 c0 {2,S}
6   Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 15,
    label = "Cs-Cs(C-Br)-Cs",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs   u0 p0 c0 {1,S} {3,S}
3 * Cs   u0 p0 c0 {1,S} {2,S}
4   Cs   u0 p0 c0 {1,S} {5,S}
5   Br1s u0 p3 c0 {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 16,
    label = "Cs-Cs-Cs(C-Cl)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs   u0 p0 c0 {1,S} {3,S}
3 * Cs   u0 p0 c0 {1,S} {2,S}
4   Cs   u0 p0 c0 {1,S} {5,S}
5   Cl1s u0 p3 c0 {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 17,
    label = "Cs-Cs(C-ClClCl)-Cs",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2   Cs   u0 p0 c0 {1,S} {3,S} {4,S}
3 * Cs   u0 p0 c0 {2,S} {4,S}
4   Cs   u0 p0 c0 {2,S} {3,S}
5   Cl1s u0 p3 c0 {1,S}
6   Cl1s u0 p3 c0 {1,S}
7   Cl1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 18,
    label = "Cs(C-ClCl)-Cs-Cs",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs   u0 p0 c0 {1,S} {5,S} {6,S}
3   Cs   u0 p0 c0 {1,S} {4,S}
4 * Cs   u0 p0 c0 {1,S} {3,S}
5   Cl1s u0 p3 c0 {2,S}
6   Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 19,
    label = "Cs(Cl)-Cs-Cs",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2 * Cs   u0 p0 c0 {1,S} {3,S}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 20,
    label = "Cs-Cs-Cs(Cl)(O2)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {3,S}
3 * Cs   u0 p0 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {1,S}
5   O2s  u0 p2 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 21,
    label = "Cs-Cs(C)-Cs(Cl)(Cl)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {3,S} {6,S}
3 * Cs   u0 p0 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {1,S}
5   Cl1s u0 p3 c0 {1,S}
6   Cs   u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 22,
    label = "Cs(Cl)-Cs-Cs(O2)",
    group = 
"""
1 * Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs   u0 p0 c0 {1,S} {3,S} {5,S}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   O2s  u0 p2 c0 {1,S}
5   Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 23,
    label = "Cs(O2)-Cs-Cs(Cl)(Cl)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {3,S} {6,S}
3 * Cs   u0 p0 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {1,S}
5   Cl1s u0 p3 c0 {1,S}
6   O2s  u0 p2 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 24,
    label = "Cs-Cs-Cs(Cl)(C)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {3,S}
3 * Cs   u0 p0 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {1,S}
5   Cs   u0 p0 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 25,
    label = "Cs-Cs(Cl)-Cs(C)",
    group = 
"""
1 * Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {3,S} {4,S}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {2,S}
5   Cs   u0 p0 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 26,
    label = "Cs-Cs(Cl)(Cl)-Cs",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {3,S}
3 * Cs   u0 p0 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {1,S}
5   Cl1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 27,
    label = "Cs-Cs(F)(F)-Cs",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u0 p0 c0 {1,S} {3,S}
3   Cs  u0 p0 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 28,
    label = "Cs-Cs(F)(F)-Cs(O2)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u0 p0 c0 {1,S} {3,S} {6,S}
3   Cs  u0 p0 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
6   O2s u0 p2 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 29,
    label = "Cs(F)(F)-Cs(C)-Cs",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 p0 c0 {1,S} {3,S} {6,S}
3 * Cs  u0 p0 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
6   Cs  u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 30,
    label = "Cs(C)-Cs-Cs(F)",
    group = 
"""
1 * Cs  u0 p0 c0 {2,S} {3,S} {5,S}
2   Cs  u0 p0 c0 {1,S} {3,S} {4,S}
3   Cs  u0 p0 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {2,S}
5   Cs  u0 p0 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 31,
    label = "Cs-Cs(F)(C)-Cs",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u0 p0 c0 {1,S} {3,S}
3   Cs  u0 p0 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {1,S}
5   Cs  u0 p0 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 32,
    label = "Cs(F)-Cs-Cs(O2)",
    group = 
"""
1 * Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S} {3,S} {5,S}
3   Cs  u0 p0 c0 {1,S} {2,S}
4   O2s u0 p2 c0 {1,S}
5   F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 33,
    label = "Cs-Cs(C-FFF)-Cs",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2   Cs  u0 p0 c0 {1,S} {3,S} {4,S}
3   Cs  u0 p0 c0 {2,S} {4,S}
4 * Cs  u0 p0 c0 {2,S} {3,S}
5   F1s u0 p3 c0 {1,S}
6   F1s u0 p3 c0 {1,S}
7   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 34,
    label = "Cs-Cs(F)(O2)-Cs",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cs  u0 p0 c0 {1,S} {3,S}
3   Cs  u0 p0 c0 {1,S} {2,S}
4   O2s u0 p2 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 35,
    label = "Cs(F)-Cs-Cs",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S} {3,S}
3 * Cs  u0 p0 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 36,
    label = "Cs-Cs(C-FF)-Cs",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S} {5,S} {6,S}
3   Cs  u0 p0 c0 {1,S} {4,S}
4 * Cs  u0 p0 c0 {1,S} {3,S}
5   F1s u0 p3 c0 {2,S}
6   F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 37,
    label = "Cs(C-F)-Cs-Cs",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S} {3,S}
3 * Cs  u0 p0 c0 {1,S} {2,S}
4   Cs  u0 p0 c0 {1,S} {5,S}
5   F1s u0 p3 c0 {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 38,
    label = "Cyclopropene",
    group = 
"""
1 * [Cs,N]  u0 {2,S} {3,S}
2   [C,N,S] u0 {1,S} {3,D}
3   [C,N,S] u0 {1,S} {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.469,-0.789,-0.953,-1.107,-1.45,-1.696,-1.716],'cal/(mol*K)'),
        H298 = (55.4702,'kcal/mol'),
        S298 = (33.3257,'cal/(mol*K)'),
    ),
    shortDesc = """Cyclopropene ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 39,
    label = "Cd(O2)-Cs-Cd(Br)",
    group = 
"""
1   Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd   u0 p0 c0 {1,D} {3,S} {5,S}
3 * Cs   u0 p0 c0 {1,S} {2,S}
4   O2s  u0 p2 c0 {1,S}
5   Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 40,
    label = "Cd(C)-Cs-Cd(Br)",
    group = 
"""
1   Cd   u0 p0 c0 {2,D} {3,S} {5,S}
2   Cd   u0 p0 c0 {1,D} {3,S} {4,S}
3 * Cs   u0 p0 c0 {1,S} {2,S}
4   Br1s u0 p3 c0 {2,S}
5   Cs   u0 p0 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 41,
    label = "Cd-Cs-Cd(Br)",
    group = 
"""
1   Cd   u0 p0 c0 {2,S} {3,D} {4,S}
2 * Cs   u0 p0 c0 {1,S} {3,S}
3   Cd   u0 p0 c0 {1,D} {2,S}
4   Br1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 42,
    label = "Cs-Cd-Cd(C-Cl)",
    group = 
"""
1   Cd   u0 p0 c0 {2,S} {3,D} {4,S}
2 * Cs   u0 p0 c0 {1,S} {3,S}
3   Cd   u0 p0 c0 {1,D} {2,S}
4   Cs   u0 p0 c0 {1,S} {5,S}
5   Cl1s u0 p3 c0 {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 43,
    label = "Cs-Cd-Cd(C-ClClCl)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2   Cd   u0 p0 c0 {1,S} {3,S} {4,D}
3 * Cs   u0 p0 c0 {2,S} {4,S}
4   Cd   u0 p0 c0 {2,D} {3,S}
5   Cl1s u0 p3 c0 {1,S}
6   Cl1s u0 p3 c0 {1,S}
7   Cl1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 44,
    label = "Cs-Cd(Cl)-Cd(O2)",
    group = 
"""
1   Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd   u0 p0 c0 {1,D} {3,S} {5,S}
3 * Cs   u0 p0 c0 {1,S} {2,S}
4   O2s  u0 p2 c0 {1,S}
5   Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 45,
    label = "Cs(O2)-Cd-Cd(Cl)",
    group = 
"""
1 * Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2   Cd   u0 p0 c0 {1,S} {3,D} {5,S}
3   Cd   u0 p0 c0 {1,S} {2,D}
4   O2s  u0 p2 c0 {1,S}
5   Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 46,
    label = "Cs-Cd(Cl)-Cd(C)",
    group = 
"""
1   Cd   u0 p0 c0 {2,D} {3,S} {5,S}
2   Cd   u0 p0 c0 {1,D} {3,S} {4,S}
3 * Cs   u0 p0 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {2,S}
5   Cs   u0 p0 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 47,
    label = "Cs-Cd(F)-Cd",
    group = 
"""
1   Cd  u0 p0 c0 {2,S} {3,D} {4,S}
2 * Cs  u0 p0 c0 {1,S} {3,S}
3   Cd  u0 p0 c0 {1,D} {2,S}
4   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 48,
    label = "Cd-Cd(F)-Cs(O2)",
    group = 
"""
1 * Cs  u0 p0 c0 {2,S} {3,S} {5,S}
2   Cd  u0 p0 c0 {1,S} {3,D} {4,S}
3   Cd  u0 p0 c0 {1,S} {2,D}
4   F1s u0 p3 c0 {2,S}
5   O2s u0 p2 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 49,
    label = "Cs-Cd(C)-Cd(F)",
    group = 
"""
1   Cd  u0 p0 c0 {2,D} {3,S} {5,S}
2   Cd  u0 p0 c0 {1,D} {3,S} {4,S}
3 * Cs  u0 p0 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {2,S}
5   Cs  u0 p0 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 50,
    label = "Cd-Cs-Cd(C-FF)",
    group = 
"""
1   Cd  u0 p0 c0 {2,S} {3,S} {4,D}
2   Cs  u0 p0 c0 {1,S} {5,S} {6,S}
3 * Cs  u0 p0 c0 {1,S} {4,S}
4   Cd  u0 p0 c0 {1,D} {3,S}
5   F1s u0 p3 c0 {2,S}
6   F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 51,
    label = "Cd-Cs-Cd(C-F)",
    group = 
"""
1   Cd  u0 p0 c0 {2,S} {3,D} {4,S}
2 * Cs  u0 p0 c0 {1,S} {3,S}
3   Cd  u0 p0 c0 {1,D} {2,S}
4   Cs  u0 p0 c0 {1,S} {5,S}
5   F1s u0 p3 c0 {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 52,
    label = "Cyclopropene2",
    group = 
"""
1   [Cs,N,O2s,S] u0 {2,S} {3,S}
2 * [C,N,O,S]    u0 {1,S} {3,D}
3   [C,N,O,S]    u0 {1,S} {2,D}
""",
    thermo = 'Cyclopropene',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 53,
    label = "Cd(C)-Cd-Cs(Br)(Br)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3   Cd   u0 p0 c0 {1,S} {2,D}
4   Br1s u0 p3 c0 {1,S}
5   Br1s u0 p3 c0 {1,S}
6   Cs   u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 54,
    label = "Cd-Cs(C-BrBr)-Cd",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs   u0 p0 c0 {1,S} {5,S} {6,S}
3 * Cd   u0 p0 c0 {1,S} {4,D}
4   Cd   u0 p0 c0 {1,S} {3,D}
5   Br1s u0 p3 c0 {2,S}
6   Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 55,
    label = "Cs(C-BrBrBr)-Cd-Cd",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2   Cs   u0 p0 c0 {1,S} {3,S} {4,S}
3 * Cd   u0 p0 c0 {2,S} {4,D}
4   Cd   u0 p0 c0 {2,S} {3,D}
5   Br1s u0 p3 c0 {1,S}
6   Br1s u0 p3 c0 {1,S}
7   Br1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 56,
    label = "Cd-Cs(C-Br)-Cd",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2   Cd   u0 p0 c0 {1,S} {3,D}
3 * Cd   u0 p0 c0 {1,S} {2,D}
4   Cs   u0 p0 c0 {1,S} {5,S}
5   Br1s u0 p3 c0 {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 57,
    label = "Cs(C)-Cd(Br)-Cd",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2   Cd   u0 p0 c0 {1,S} {3,D} {4,S}
3 * Cd   u0 p0 c0 {1,S} {2,D}
4   Br1s u0 p3 c0 {2,S}
5   Cs   u0 p0 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 58,
    label = "Cd-Cd-Cs(Br)(O2)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cd   u0 p0 c0 {1,S} {3,D}
3 * Cd   u0 p0 c0 {1,S} {2,D}
4   Br1s u0 p3 c0 {1,S}
5   O2s  u0 p2 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 59,
    label = "Cd-Cd-Cs(Br)(Br)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cd   u0 p0 c0 {1,S} {3,D}
3   Cd   u0 p0 c0 {1,S} {2,D}
4   Br1s u0 p3 c0 {1,S}
5   Br1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 60,
    label = "Cd(O2)-Cs(Br)(Br)-Cd",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3   Cd   u0 p0 c0 {1,S} {2,D}
4   Br1s u0 p3 c0 {1,S}
5   Br1s u0 p3 c0 {1,S}
6   O2s  u0 p2 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 61,
    label = "Cd-Cd-Cs(Br)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2 * Cd   u0 p0 c0 {1,S} {3,D}
3   Cd   u0 p0 c0 {1,S} {2,D}
4   Br1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 62,
    label = "Cs(Br)-Cd(C)-Cd",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2   Cd   u0 p0 c0 {1,S} {3,D} {5,S}
3 * Cd   u0 p0 c0 {1,S} {2,D}
4   Br1s u0 p3 c0 {1,S}
5   Cs   u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 63,
    label = "Cd-Cd(O2)-Cs(Br)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2   Cd   u0 p0 c0 {1,S} {3,D} {4,S}
3 * Cd   u0 p0 c0 {1,S} {2,D}
4   O2s  u0 p2 c0 {2,S}
5   Br1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 64,
    label = "Cd-Cd-Cs(Br)(C)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cd   u0 p0 c0 {1,S} {3,D}
3   Cd   u0 p0 c0 {1,S} {2,D}
4   Cs   u0 p0 c0 {1,S}
5   Br1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 65,
    label = "Cs-Cd-Cd(C-Br)",
    group = 
"""
1   Cd   u0 p0 c0 {2,S} {3,D} {4,S}
2   Cs   u0 p0 c0 {1,S} {3,S}
3 * Cd   u0 p0 c0 {1,D} {2,S}
4   Cs   u0 p0 c0 {1,S} {5,S}
5   Br1s u0 p3 c0 {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 66,
    label = "Cd-Cs-Cd(C-BrBrBr)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2   Cd   u0 p0 c0 {1,S} {3,S} {4,D}
3   Cs   u0 p0 c0 {2,S} {4,S}
4 * Cd   u0 p0 c0 {2,D} {3,S}
5   Br1s u0 p3 c0 {1,S}
6   Br1s u0 p3 c0 {1,S}
7   Br1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 67,
    label = "Cd(C-BrBr)-Cd-Cs",
    group = 
"""
1   Cd   u0 p0 c0 {2,S} {3,S} {4,D}
2   Cs   u0 p0 c0 {1,S} {5,S} {6,S}
3   Cs   u0 p0 c0 {1,S} {4,S}
4 * Cd   u0 p0 c0 {1,D} {3,S}
5   Br1s u0 p3 c0 {2,S}
6   Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 68,
    label = "Cd(C)-Cd(Br)-O2s",
    group = 
"""
1   Cd   u0 p0 c0 {2,D} {3,S} {5,S}
2 * Cd   u0 p0 c0 {1,D} {3,S} {4,S}
3   O2s  u0 p2 c0 {1,S} {2,S}
4   Br1s u0 p3 c0 {2,S}
5   Cs   u0 p0 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 69,
    label = "O2s-Cd(C-Br)-Cd",
    group = 
"""
1 * Cd   u0 p0 c0 {2,S} {3,D} {4,S}
2   O2s  u0 p2 c0 {1,S} {3,S}
3   Cd   u0 p0 c0 {1,D} {2,S}
4   Cs   u0 p0 c0 {1,S} {5,S}
5   Br1s u0 p3 c0 {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 70,
    label = "O2s-Cd-Cd(C-BrBrBr)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 * Cd   u0 p0 c0 {1,S} {3,S} {4,D}
3   O2s  u0 p2 c0 {2,S} {4,S}
4   Cd   u0 p0 c0 {2,D} {3,S}
5   Br1s u0 p3 c0 {1,S}
6   Br1s u0 p3 c0 {1,S}
7   Br1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 71,
    label = "Cd(C-BrBr)-Cd-O2s",
    group = 
"""
1   Cd   u0 p0 c0 {2,S} {3,S} {4,D}
2   Cs   u0 p0 c0 {1,S} {5,S} {6,S}
3   O2s  u0 p2 c0 {1,S} {4,S}
4 * Cd   u0 p0 c0 {1,D} {3,S}
5   Br1s u0 p3 c0 {2,S}
6   Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 72,
    label = "Cs(O2)-Cd-Cd(Br)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2   Cd   u0 p0 c0 {1,S} {3,D} {4,S}
3 * Cd   u0 p0 c0 {1,S} {2,D}
4   Br1s u0 p3 c0 {2,S}
5   O2s  u0 p2 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 73,
    label = "Cd-Cd-Cs(C-ClCl)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs   u0 p0 c0 {1,S} {5,S} {6,S}
3 * Cd   u0 p0 c0 {1,S} {4,D}
4   Cd   u0 p0 c0 {1,S} {3,D}
5   Cl1s u0 p3 c0 {2,S}
6   Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 74,
    label = "Cd-Cd-Cs(C-ClClCl)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2   Cs   u0 p0 c0 {1,S} {3,S} {4,S}
3 * Cd   u0 p0 c0 {2,S} {4,D}
4   Cd   u0 p0 c0 {2,S} {3,D}
5   Cl1s u0 p3 c0 {1,S}
6   Cl1s u0 p3 c0 {1,S}
7   Cl1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 75,
    label = "Cd-Cs-Cd(Cl)",
    group = 
"""
1 * Cd   u0 p0 c0 {2,S} {3,D} {4,S}
2   Cs   u0 p0 c0 {1,S} {3,S}
3   Cd   u0 p0 c0 {1,D} {2,S}
4   Cl1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 76,
    label = "Cd-Cd(Cl)-Cs(C)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2   Cd   u0 p0 c0 {1,S} {3,D} {5,S}
3 * Cd   u0 p0 c0 {1,S} {2,D}
4   Cs   u0 p0 c0 {1,S}
5   Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 77,
    label = "Cd-Cs(Cl)(C)-Cd",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cd   u0 p0 c0 {1,S} {3,D}
3   Cd   u0 p0 c0 {1,S} {2,D}
4   Cs   u0 p0 c0 {1,S}
5   Cl1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 78,
    label = "Cd-Cd-Cs(Cl)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2 * Cd   u0 p0 c0 {1,S} {3,D}
3   Cd   u0 p0 c0 {1,S} {2,D}
4   Cl1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 79,
    label = "Cs(Cl)-Cd-Cd(O2)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2   Cd   u0 p0 c0 {1,S} {3,D} {5,S}
3 * Cd   u0 p0 c0 {1,S} {2,D}
4   Cl1s u0 p3 c0 {1,S}
5   O2s  u0 p2 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 80,
    label = "Cd(O2)-Cs(Cl)(Cl)-Cd",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3 * Cd   u0 p0 c0 {1,S} {2,D}
4   Cl1s u0 p3 c0 {1,S}
5   Cl1s u0 p3 c0 {1,S}
6   O2s  u0 p2 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 81,
    label = "Cs(Cl)(Cl)-Cd-Cd(C)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cd   u0 p0 c0 {1,S} {3,D} {6,S}
3 * Cd   u0 p0 c0 {1,S} {2,D}
4   Cl1s u0 p3 c0 {1,S}
5   Cl1s u0 p3 c0 {1,S}
6   Cs   u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 82,
    label = "Cs(Cl)(Cl)-Cd-Cd",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cd   u0 p0 c0 {1,S} {3,D}
3 * Cd   u0 p0 c0 {1,S} {2,D}
4   Cl1s u0 p3 c0 {1,S}
5   Cl1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 83,
    label = "Cd-Cs(Cl)(O2)-Cd",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cd   u0 p0 c0 {1,S} {3,D}
3 * Cd   u0 p0 c0 {1,S} {2,D}
4   Cl1s u0 p3 c0 {1,S}
5   O2s  u0 p2 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 84,
    label = "Cd-Cd(C)-Cs(Cl)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2   Cd   u0 p0 c0 {1,S} {3,D} {4,S}
3 * Cd   u0 p0 c0 {1,S} {2,D}
4   Cs   u0 p0 c0 {2,S}
5   Cl1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 85,
    label = "Cs-Cd-Cd(C-ClCl)",
    group = 
"""
1   Cd   u0 p0 c0 {2,S} {3,S} {4,D}
2   Cs   u0 p0 c0 {1,S} {5,S} {6,S}
3   Cs   u0 p0 c0 {1,S} {4,S}
4 * Cd   u0 p0 c0 {1,D} {3,S}
5   Cl1s u0 p3 c0 {2,S}
6   Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 86,
    label = "O2s-Cd(Cl)-Cd(C)",
    group = 
"""
1   Cd   u0 p0 c0 {2,D} {3,S} {5,S}
2 * Cd   u0 p0 c0 {1,D} {3,S} {4,S}
3   O2s  u0 p2 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {2,S}
5   Cs   u0 p0 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 87,
    label = "Cd(C-ClCl)-Cd-O2s",
    group = 
"""
1 * Cd   u0 p0 c0 {2,S} {3,S} {4,D}
2   Cs   u0 p0 c0 {1,S} {5,S} {6,S}
3   O2s  u0 p2 c0 {1,S} {4,S}
4   Cd   u0 p0 c0 {1,D} {3,S}
5   Cl1s u0 p3 c0 {2,S}
6   Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 88,
    label = "Cd-O2s-Cd(C-ClClCl)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 * Cd   u0 p0 c0 {1,S} {3,S} {4,D}
3   O2s  u0 p2 c0 {2,S} {4,S}
4   Cd   u0 p0 c0 {2,D} {3,S}
5   Cl1s u0 p3 c0 {1,S}
6   Cl1s u0 p3 c0 {1,S}
7   Cl1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 89,
    label = "Cs(C-Cl)-Cd-Cd",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2 * Cd   u0 p0 c0 {1,S} {3,D}
3   Cd   u0 p0 c0 {1,S} {2,D}
4   Cs   u0 p0 c0 {1,S} {5,S}
5   Cl1s u0 p3 c0 {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 90,
    label = "Cd-O2s-Cd(C-Cl)",
    group = 
"""
1 * Cd   u0 p0 c0 {2,S} {3,D} {4,S}
2   O2s  u0 p2 c0 {1,S} {3,S}
3   Cd   u0 p0 c0 {1,D} {2,S}
4   Cs   u0 p0 c0 {1,S} {5,S}
5   Cl1s u0 p3 c0 {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 91,
    label = "O2s-Cd-Cd(C-FFF)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 * Cd  u0 p0 c0 {1,S} {3,S} {4,D}
3   O2s u0 p2 c0 {2,S} {4,S}
4   Cd  u0 p0 c0 {2,D} {3,S}
5   F1s u0 p3 c0 {1,S}
6   F1s u0 p3 c0 {1,S}
7   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 92,
    label = "Cd-Cs-Cd(C-FFF)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2   Cd  u0 p0 c0 {1,S} {3,S} {4,D}
3   Cs  u0 p0 c0 {2,S} {4,S}
4 * Cd  u0 p0 c0 {2,D} {3,S}
5   F1s u0 p3 c0 {1,S}
6   F1s u0 p3 c0 {1,S}
7   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 93,
    label = "Cd-Cs(F)(C)-Cd",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 p0 c0 {1,S} {3,D}
3 * Cd  u0 p0 c0 {1,S} {2,D}
4   Cs  u0 p0 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 94,
    label = "Cd(C)-Cd-Cs(F)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2 * Cd  u0 p0 c0 {1,S} {3,D} {5,S}
3   Cd  u0 p0 c0 {1,S} {2,D}
4   F1s u0 p3 c0 {1,S}
5   Cs  u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 95,
    label = "Cd-Cd(C)-Cs(F)(F)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cd  u0 p0 c0 {1,S} {3,D} {6,S}
3   Cd  u0 p0 c0 {1,S} {2,D}
4   F1s u0 p3 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
6   Cs  u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 96,
    label = "Cd-Cs(C-FFF)-Cd",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2   Cs  u0 p0 c0 {1,S} {3,S} {4,S}
3   Cd  u0 p0 c0 {2,S} {4,D}
4 * Cd  u0 p0 c0 {2,S} {3,D}
5   F1s u0 p3 c0 {1,S}
6   F1s u0 p3 c0 {1,S}
7   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 97,
    label = "Cd-Cd-Cs(C-FF)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S} {5,S} {6,S}
3   Cd  u0 p0 c0 {1,S} {4,D}
4 * Cd  u0 p0 c0 {1,S} {3,D}
5   F1s u0 p3 c0 {2,S}
6   F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 98,
    label = "Cs(F)(O2)-Cd-Cd",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cd  u0 p0 c0 {1,S} {3,D}
3   Cd  u0 p0 c0 {1,S} {2,D}
4   F1s u0 p3 c0 {1,S}
5   O2s u0 p2 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 99,
    label = "Cd-O2s-Cd(C-F)",
    group = 
"""
1 * Cd  u0 p0 c0 {2,S} {3,D} {4,S}
2   O2s u0 p2 c0 {1,S} {3,S}
3   Cd  u0 p0 c0 {1,D} {2,S}
4   Cs  u0 p0 c0 {1,S} {5,S}
5   F1s u0 p3 c0 {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 100,
    label = "Cd-Cs(F)-Cd",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2 * Cd  u0 p0 c0 {1,S} {3,D}
3   Cd  u0 p0 c0 {1,S} {2,D}
4   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 101,
    label = "Cs(F)(F)-Cd-Cd(O2)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cd  u0 p0 c0 {1,S} {3,D} {6,S}
3   Cd  u0 p0 c0 {1,S} {2,D}
4   F1s u0 p3 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
6   O2s u0 p2 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 102,
    label = "Cs(F)-Cd-Cd(O2)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {5,S}
2 * Cd  u0 p0 c0 {1,S} {3,D} {4,S}
3   Cd  u0 p0 c0 {1,S} {2,D}
4   O2s u0 p2 c0 {2,S}
5   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 103,
    label = "Cd-Cd-Cs(F)(F)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cd  u0 p0 c0 {1,S} {3,D}
3   Cd  u0 p0 c0 {1,S} {2,D}
4   F1s u0 p3 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 104,
    label = "Cd(C-FF)-Cd-O2s",
    group = 
"""
1   Cd  u0 p0 c0 {2,S} {3,S} {4,D}
2   Cs  u0 p0 c0 {1,S} {5,S} {6,S}
3   O2s u0 p2 c0 {1,S} {4,S}
4 * Cd  u0 p0 c0 {1,D} {3,S}
5   F1s u0 p3 c0 {2,S}
6   F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 105,
    label = "Cd-Cd-Cs(C-F)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2 * Cd  u0 p0 c0 {1,S} {3,D}
3   Cd  u0 p0 c0 {1,S} {2,D}
4   Cs  u0 p0 c0 {1,S} {5,S}
5   F1s u0 p3 c0 {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 106,
    label = "Cd-Cd(F)-Cs(C)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {5,S}
2   Cd  u0 p0 c0 {1,S} {3,D} {4,S}
3 * Cd  u0 p0 c0 {1,S} {2,D}
4   F1s u0 p3 c0 {2,S}
5   Cs  u0 p0 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 107,
    label = "Cd(F)-Cd(O2)-Cs",
    group = 
"""
1 * Cd  u0 p0 c0 {2,D} {3,S} {5,S}
2   Cd  u0 p0 c0 {1,D} {3,S} {4,S}
3   Cs  u0 p0 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {2,S}
5   O2s u0 p2 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 108,
    label = "Cd(C)-Cd(F)-O2s",
    group = 
"""
1   Cd  u0 p0 c0 {2,D} {3,S} {5,S}
2 * Cd  u0 p0 c0 {1,D} {3,S} {4,S}
3   O2s u0 p2 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {2,S}
5   Cs  u0 p0 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 109,
    label = "Cyclopropadiene",
    group = 
"""
1 * [C,N,O,S]   u0 {2,S} {3,D}
2   [C,N,O,S]   u0 {1,S} {3,D}
3   [Cdd,N,O,S] u0 {1,D} {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.469,-0.789,-0.953,-1.107,-1.45,-1.696,-1.716],'cal/(mol*K)'),
        H298 = (73.04,'kcal/mol'),
        S298 = (33.3257,'cal/(mol*K)'),
    ),
    shortDesc = """Enthalpy from doi:10.1021/j100005a002 (S and Cp from Cyclopropene row above)""",
    longDesc = 
"""

""",
)

entry(
    index = 110,
    label = "Cyclopropadiene2",
    group = 
"""
1   [C,N,O,S]   u0 {2,S} {3,D}
2   [C,N,O,S]   u0 {1,S} {3,D}
3 * [Cdd,N,O,S] u0 {1,D} {2,D}
""",
    thermo = 'Cyclopropadiene',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 111,
    label = "Cyclopropyne",
    group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   Ct  u0 {1,T} {3,S}
3   R!H u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.22,1.515,0.554,-0.319,-1.215,-1.31,-2.439],'cal/(mol*K)'),
        H298 = (111.641,'kcal/mol'),
        S298 = (37.345,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Fitted to M06 calculations
""",
)

entry(
    index = 112,
    label = "oxirene",
    group = 
"""
1   [C,N,S] u0 {2,S} {3,D}
2 * O2s     u0 {1,S} {3,S}
3   [C,N,S] u0 {1,D} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.283,-1.56,-2.46,-2.83,-3.22,-3.08,-3.04],'cal/(mol*K)'),
        H298 = (80.64,'kcal/mol'),
        S298 = (38.08,'cal/(mol*K)'),
    ),
    shortDesc = """Derived from goldsmith's DFT-QCI library""",
    longDesc = 
"""

""",
)

entry(
    index = 113,
    label = "Cyclopropatriene",
    group = 
"""
1 * [Cdd,N,O,S] u0 {2,D} {3,D}
2   [Cdd,N,O,S] u0 {1,D} {3,D}
3   [Cdd,N,O,S] u0 {1,D} {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.469,-0.789,-0.953,-1.107,-1.45,-1.696,-1.716],'cal/(mol*K)'),
        H298 = (78,'kcal/mol'),
        S298 = (33.3257,'cal/(mol*K)'),
    ),
    shortDesc = """Enthalpy from doi:10.1021/j100005a002 (S and Cp from Cyclopropene row above)""",
    longDesc = 
"""

""",
)

entry(
    index = 114,
    label = "Ethylene_oxide",
    group = 
"""
1 * O2s    u0 {2,S} {3,S}
2   [Cs,N] u0 {1,S} {3,S}
3   [Cs,N] u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.891,-2.459,-2.221,-1.969,-1.965,-1.759,2.564],'cal/(mol*K)'),
        H298 = (26.82,'kcal/mol'),
        S298 = (31.1767,'cal/(mol*K)'),
    ),
    shortDesc = """CY/C2O from THERM (Dorofeeva, 92) Cp1500 est. as Cp1000""",
    longDesc = 
"""

""",
)

entry(
    index = 115,
    label = "O2s-Cs(Br)-Cs(O2)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs   u0 p0 c0 {1,S} {3,S} {5,S}
3 * O2s  u0 p2 c0 {1,S} {2,S}
4   O2s  u0 p2 c0 {1,S}
5   Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 116,
    label = "O2s-Cs(Br)(Br)-Cs(O2)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {3,S} {6,S}
3 * O2s  u0 p2 c0 {1,S} {2,S}
4   Br1s u0 p3 c0 {1,S}
5   Br1s u0 p3 c0 {1,S}
6   O2s  u0 p2 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 117,
    label = "O2s-Cs(C)-Cs(Br)(Br)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {3,S} {6,S}
3 * O2s  u0 p2 c0 {1,S} {2,S}
4   Br1s u0 p3 c0 {1,S}
5   Br1s u0 p3 c0 {1,S}
6   Cs   u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 118,
    label = "O2s-Cs(C-BrBrBr)-Cs",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2   Cs   u0 p0 c0 {1,S} {3,S} {4,S}
3   Cs   u0 p0 c0 {2,S} {4,S}
4 * O2s  u0 p2 c0 {2,S} {3,S}
5   Br1s u0 p3 c0 {1,S}
6   Br1s u0 p3 c0 {1,S}
7   Br1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 119,
    label = "O2s-Cs(Br)(C)-Cs",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * O2s  u0 p2 c0 {1,S} {3,S}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Br1s u0 p3 c0 {1,S}
5   Cs   u0 p0 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 120,
    label = "O2s-Cs-Cs(Br)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs   u0 p0 c0 {1,S} {3,S}
3 * O2s  u0 p2 c0 {1,S} {2,S}
4   Br1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 121,
    label = "O2s-Cs-Cs(Br)(Br)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {3,S}
3 * O2s  u0 p2 c0 {1,S} {2,S}
4   Br1s u0 p3 c0 {1,S}
5   Br1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 122,
    label = "Cs(C)-Cs(Br)-O2s",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {3,S} {4,S}
3 * O2s  u0 p2 c0 {1,S} {2,S}
4   Br1s u0 p3 c0 {2,S}
5   Cs   u0 p0 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 123,
    label = "Cs-Cs(Br)(O2)-O2s",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {3,S}
3 * O2s  u0 p2 c0 {1,S} {2,S}
4   O2s  u0 p2 c0 {1,S}
5   Br1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 124,
    label = "Cs(C-BrBr)-Cs-O2s",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs   u0 p0 c0 {1,S} {5,S} {6,S}
3 * O2s  u0 p2 c0 {1,S} {4,S}
4   Cs   u0 p0 c0 {1,S} {3,S}
5   Br1s u0 p3 c0 {2,S}
6   Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 125,
    label = "Cs(C-Br)-Cs-O2s",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2 * O2s  u0 p2 c0 {1,S} {3,S}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Cs   u0 p0 c0 {1,S} {5,S}
5   Br1s u0 p3 c0 {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 126,
    label = "Cs(C-Cl)-Cs-O2s",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2 * O2s  u0 p2 c0 {1,S} {3,S}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Cs   u0 p0 c0 {1,S} {5,S}
5   Cl1s u0 p3 c0 {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 127,
    label = "O2s-Cs-Cs(C-ClClCl)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2   Cs   u0 p0 c0 {1,S} {3,S} {4,S}
3 * O2s  u0 p2 c0 {2,S} {4,S}
4   Cs   u0 p0 c0 {2,S} {3,S}
5   Cl1s u0 p3 c0 {1,S}
6   Cl1s u0 p3 c0 {1,S}
7   Cl1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 128,
    label = "O2s-Cs(C-ClCl)-Cs",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs   u0 p0 c0 {1,S} {5,S} {6,S}
3 * O2s  u0 p2 c0 {1,S} {4,S}
4   Cs   u0 p0 c0 {1,S} {3,S}
5   Cl1s u0 p3 c0 {2,S}
6   Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 129,
    label = "Cs-O2s-Cs(Cl)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2 * O2s  u0 p2 c0 {1,S} {3,S}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 130,
    label = "Cs(O2)-O2s-Cs(Cl)(Cl)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {3,S} {6,S}
3 * O2s  u0 p2 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {1,S}
5   Cl1s u0 p3 c0 {1,S}
6   O2s  u0 p2 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 131,
    label = "Cs-O2s-Cs(Cl)(O2)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * O2s  u0 p2 c0 {1,S} {3,S}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {1,S}
5   O2s  u0 p2 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 132,
    label = "Cs(Cl)-O2s-Cs(O2)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {3,S} {4,S}
3 * O2s  u0 p2 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {2,S}
5   O2s  u0 p2 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 133,
    label = "Cs(Cl)-O2s-Cs(C)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs   u0 p0 c0 {1,S} {3,S} {5,S}
3 * O2s  u0 p2 c0 {1,S} {2,S}
4   Cs   u0 p0 c0 {1,S}
5   Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 134,
    label = "Cs(Cl)(Cl)-O2s-Cs(C)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {3,S} {6,S}
3 * O2s  u0 p2 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {1,S}
5   Cl1s u0 p3 c0 {1,S}
6   Cs   u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 135,
    label = "Cs-O2s-Cs(Cl)(C)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * O2s  u0 p2 c0 {1,S} {3,S}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {1,S}
5   Cs   u0 p0 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 136,
    label = "Cs(Cl)(Cl)-Cs-O2s",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * O2s  u0 p2 c0 {1,S} {3,S}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {1,S}
5   Cl1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 137,
    label = "O2s-Cs-Cs(C-FFF)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2   Cs  u0 p0 c0 {1,S} {3,S} {4,S}
3   Cs  u0 p0 c0 {2,S} {4,S}
4 * O2s u0 p2 c0 {2,S} {3,S}
5   F1s u0 p3 c0 {1,S}
6   F1s u0 p3 c0 {1,S}
7   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 138,
    label = "Cs(F)(O2)-O2s-Cs",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 p0 c0 {1,S} {3,S}
3 * O2s u0 p2 c0 {1,S} {2,S}
4   O2s u0 p2 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 139,
    label = "Cs(O2)-O2s-Cs(F)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S} {3,S} {5,S}
3 * O2s u0 p2 c0 {1,S} {2,S}
4   O2s u0 p2 c0 {1,S}
5   F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 140,
    label = "Cs(O2)-Cs(F)(F)-O2s",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 p0 c0 {1,S} {3,S} {6,S}
3 * O2s u0 p2 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
6   O2s u0 p2 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 141,
    label = "O2s-Cs-Cs(F)(F)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * O2s u0 p2 c0 {1,S} {3,S}
3   Cs  u0 p0 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 142,
    label = "Cs(C)-Cs(F)(F)-O2s",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 p0 c0 {1,S} {3,S} {6,S}
3 * O2s u0 p2 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
6   Cs  u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 143,
    label = "Cs(F)(C)-Cs-O2s",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * O2s u0 p2 c0 {1,S} {3,S}
3   Cs  u0 p0 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {1,S}
5   Cs  u0 p0 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 144,
    label = "O2s-Cs(F)-Cs(C)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {5,S}
2   Cs  u0 p0 c0 {1,S} {3,S} {4,S}
3 * O2s u0 p2 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {2,S}
5   Cs  u0 p0 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 145,
    label = "Cs-Cs(F)-O2s",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S} {3,S}
3 * O2s u0 p2 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 146,
    label = "Cs(C-F)-Cs-O2s",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2 * O2s u0 p2 c0 {1,S} {3,S}
3   Cs  u0 p0 c0 {1,S} {2,S}
4   Cs  u0 p0 c0 {1,S} {5,S}
5   F1s u0 p3 c0 {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 147,
    label = "Cs(C-FF)-Cs-O2s",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S} {5,S} {6,S}
3 * O2s u0 p2 c0 {1,S} {4,S}
4   Cs  u0 p0 c0 {1,S} {3,S}
5   F1s u0 p3 c0 {2,S}
6   F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 148,
    label = "dioxirane",
    group = 
"""
1 * O2s    u0 {2,S} {3,S}
2   O2s    u0 {1,S} {3,S}
3   [Cs,N] u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.099,-3.194,-3.095,-3.038,-3.281,-3.818,-1.346],'cal/(mol*K)'),
        H298 = (25.1977,'kcal/mol'),
        S298 = (32.3877,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 149,
    label = "O2s-O2s-Cs(Br)(C)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * O2s  u0 p2 c0 {1,S} {3,S}
3   O2s  u0 p2 c0 {1,S} {2,S}
4   Cs   u0 p0 c0 {1,S}
5   Br1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 150,
    label = "Cs(C-BrBr)-O2s-O2s",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs   u0 p0 c0 {1,S} {5,S} {6,S}
3 * O2s  u0 p2 c0 {1,S} {4,S}
4   O2s  u0 p2 c0 {1,S} {3,S}
5   Br1s u0 p3 c0 {2,S}
6   Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 151,
    label = "Cs(C-BrBrBr)-O2s-O2s",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2   Cs   u0 p0 c0 {1,S} {3,S} {4,S}
3 * O2s  u0 p2 c0 {2,S} {4,S}
4   O2s  u0 p2 c0 {2,S} {3,S}
5   Br1s u0 p3 c0 {1,S}
6   Br1s u0 p3 c0 {1,S}
7   Br1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 152,
    label = "O2s-Cs(C-Br)-O2s",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2 * O2s  u0 p2 c0 {1,S} {3,S}
3   O2s  u0 p2 c0 {1,S} {2,S}
4   Cs   u0 p0 c0 {1,S} {5,S}
5   Br1s u0 p3 c0 {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 153,
    label = "O2s-Cs(Br)-O2s",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2   O2s  u0 p2 c0 {1,S} {3,S}
3 * O2s  u0 p2 c0 {1,S} {2,S}
4   Br1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 154,
    label = "O2s-O2s-Cs(Br)(Br)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * O2s  u0 p2 c0 {1,S} {3,S}
3   O2s  u0 p2 c0 {1,S} {2,S}
4   Br1s u0 p3 c0 {1,S}
5   Br1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 155,
    label = "O2s-Cs(C-ClClCl)-O2s",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2   Cs   u0 p0 c0 {1,S} {3,S} {4,S}
3 * O2s  u0 p2 c0 {2,S} {4,S}
4   O2s  u0 p2 c0 {2,S} {3,S}
5   Cl1s u0 p3 c0 {1,S}
6   Cl1s u0 p3 c0 {1,S}
7   Cl1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 156,
    label = "O2s-O2s-Cs(C-ClCl)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs   u0 p0 c0 {1,S} {5,S} {6,S}
3 * O2s  u0 p2 c0 {1,S} {4,S}
4   O2s  u0 p2 c0 {1,S} {3,S}
5   Cl1s u0 p3 c0 {2,S}
6   Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 157,
    label = "O2s-Cs(Cl)(C)-O2s",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * O2s  u0 p2 c0 {1,S} {3,S}
3   O2s  u0 p2 c0 {1,S} {2,S}
4   Cs   u0 p0 c0 {1,S}
5   Cl1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 158,
    label = "Cs(Cl)(Cl)-O2s-O2s",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * O2s  u0 p2 c0 {1,S} {3,S}
3   O2s  u0 p2 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {1,S}
5   Cl1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 159,
    label = "O2s-O2s-Cs(Cl)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2   O2s  u0 p2 c0 {1,S} {3,S}
3 * O2s  u0 p2 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 160,
    label = "Cs(C-Cl)-O2s-O2s",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2 * O2s  u0 p2 c0 {1,S} {3,S}
3   O2s  u0 p2 c0 {1,S} {2,S}
4   Cs   u0 p0 c0 {1,S} {5,S}
5   Cl1s u0 p3 c0 {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 161,
    label = "O2s-O2s-Cs(C-F)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2 * O2s u0 p2 c0 {1,S} {3,S}
3   O2s u0 p2 c0 {1,S} {2,S}
4   Cs  u0 p0 c0 {1,S} {5,S}
5   F1s u0 p3 c0 {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 162,
    label = "O2s-O2s-Cs(C-FF)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2   Cs  u0 p0 c0 {1,S} {5,S} {6,S}
3 * O2s u0 p2 c0 {1,S} {4,S}
4   O2s u0 p2 c0 {1,S} {3,S}
5   F1s u0 p3 c0 {2,S}
6   F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 163,
    label = "Cs(C-FFF)-O2s-O2s",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2   Cs  u0 p0 c0 {1,S} {3,S} {4,S}
3 * O2s u0 p2 c0 {2,S} {4,S}
4   O2s u0 p2 c0 {2,S} {3,S}
5   F1s u0 p3 c0 {1,S}
6   F1s u0 p3 c0 {1,S}
7   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 164,
    label = "O2s-O2s-Cs(F)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2   O2s u0 p2 c0 {1,S} {3,S}
3 * O2s u0 p2 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 165,
    label = "O2s-O2s-Cs(F)(C)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * O2s u0 p2 c0 {1,S} {3,S}
3   O2s u0 p2 c0 {1,S} {2,S}
4   Cs  u0 p0 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 166,
    label = "O2s-Cs(F)(F)-O2s",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * O2s u0 p2 c0 {1,S} {3,S}
3   O2s u0 p2 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 167,
    label = "2(co)oxirane",
    group = 
"""
1   [CO,CS]  u0 {2,S} {3,S}
2 * [O2s,S]  u0 {1,S} {3,S}
3   [Cs,N,S] u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.147,-1.715,-2.067,-2.254,-2.546,-2.592,-1.488],'cal/(mol*K)'),
        H298 = (40.7699,'kcal/mol'),
        S298 = (34.529,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 168,
    label = "O2s-CO(O2d)-Cs(Br)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2   CO   u0 p0 c0 {1,S} {3,S} {5,D}
3 * O2s  u0 p2 c0 {1,S} {2,S}
4   Br1s u0 p3 c0 {1,S}
5   O2d  u0 p2 c0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 169,
    label = "CO(O2d)-O2s-Cs(Br)(Br)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2   CO   u0 p0 c0 {1,S} {3,S} {6,D}
3 * O2s  u0 p2 c0 {1,S} {2,S}
4   Br1s u0 p3 c0 {1,S}
5   Br1s u0 p3 c0 {1,S}
6   O2d  u0 p2 c0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 170,
    label = "cyclopropanedione",
    group = 
"""
1   [CO,CS]      u0 {2,S} {3,S}
2 * [CO,CS]      u0 {1,S} {3,S}
3   [Cs,N,O2s,S] u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.85,1.69,0.674,-0.137,-1.157,-2.068,0.878],'cal/(mol*K)'),
        H298 = (67.2975,'kcal/mol'),
        S298 = (38.9107,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 171,
    label = "cyclopropenone",
    group = 
"""
1   [C,N,O,S] u0 {2,S} {3,D}
2 * [CO,CS]   u0 {1,S} {3,S}
3   [C,N,O,S] u0 {1,D} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.734,-1.275,-1.673,-1.861,-2.134,-2.557,-1.78],'cal/(mol*K)'),
        H298 = (56.774,'kcal/mol'),
        S298 = (35.6157,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 172,
    label = "Cd(Br)-CO(O2d)-Cd",
    group = 
"""
1 * CO   u0 p0 c0 {2,S} {3,S} {5,D}
2   Cd   u0 p0 c0 {1,S} {3,D} {4,S}
3   Cd   u0 p0 c0 {1,S} {2,D}
4   Br1s u0 p3 c0 {2,S}
5   O2d  u0 p2 c0 {1,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 173,
    label = "Cd-Cd(Cl)-CO(O2d)",
    group = 
"""
1 * CO   u0 p0 c0 {2,S} {3,S} {5,D}
2   Cd   u0 p0 c0 {1,S} {3,D} {4,S}
3   Cd   u0 p0 c0 {1,S} {2,D}
4   Cl1s u0 p3 c0 {2,S}
5   O2d  u0 p2 c0 {1,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 174,
    label = "CO(O2d)-Cd-Cd(F)",
    group = 
"""
1 * CO  u0 p0 c0 {2,S} {3,S} {5,D}
2   Cd  u0 p0 c0 {1,S} {3,D} {4,S}
3   Cd  u0 p0 c0 {1,S} {2,D}
4   F1s u0 p3 c0 {2,S}
5   O2d u0 p2 c0 {1,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 175,
    label = "thiirane",
    group = 
"""
1 * S     u0 {2,S} {3,S}
2   [C,N] u0 {1,S} {3,S}
3   [C,N] u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.02,-2.54,-2.13,-1.81,-1.49,-1.26,-0.96],'cal/(mol*K)'),
        H298 = (17.82,'kcal/mol'),
        S298 = (28.57,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
"""

""",
)

entry(
    index = 176,
    label = "dithiirane",
    group = 
"""
1 * S     u0 {2,S} {3,S}
2   S     u0 {1,S} {3,S}
3   [C,N] u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.26,-6.35,-5.37,-4.63,-3.67,-3.08,-2.21],'cal/(mol*K)'),
        H298 = (21.37,'kcal/mol'),
        S298 = (31.73,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
"""

""",
)

entry(
    index = 177,
    label = "trithiirane",
    group = 
"""
1 * S u0 {2,S} {3,S}
2   S u0 {1,S} {3,S}
3   S u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.97,-6.66,-6.4,-6.29,-6.1,-5.72,-4.28],'cal/(mol*K)'),
        H298 = (24.72,'kcal/mol'),
        S298 = (34.89,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009, dH from NIST-JANAF""",
    longDesc = 
"""

""",
)

entry(
    index = 178,
    label = "thiirene",
    group = 
"""
1 * S     u0 {2,S} {3,S}
2   [C,N] u0 {1,S} {3,D}
3   [C,N] u0 {1,S} {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.13,-3.8,-6.26,-8.36,-11.65,-14.12,-18.01],'cal/(mol*K)'),
        H298 = (52.44,'kcal/mol'),
        S298 = (34.28,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
"""

""",
)

entry(
    index = 179,
    label = "Ethyleneimine",
    group = 
"""
1 * N        u0 {2,S} {3,S}
2   [Cs,N,S] u0 {1,S} {3,S}
3   [Cs,N,S] u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (27.7,'kcal/mol'),
        S298 = (31.6,'cal/(mol*K)'),
    ),
    shortDesc = """Ethyleneimine ring BENSON (Aziridine)""",
    longDesc = 
"""

""",
)

entry(
    index = 180,
    label = "Methylene_cyclopropane",
    group = 
"""
1 * [Cd,N] u0 {2,S} {3,S} {4,D}
2   [Cs,N] u0 {1,S} {3,S}
3   [Cs,N] u0 {1,S} {2,S}
4   [Cd,N] u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.1,-2.121,-2.081,-2.005,-1.98,-1.903,-1.541],'cal/(mol*K)'),
        H298 = (40.92,'kcal/mol'),
        S298 = (31.4507,'cal/(mol*K)'),
    ),
    shortDesc = """Methylene cyclopropane ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 181,
    label = "Cs-Cd(Cd)-Cs(Br)(Br)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cd   u0 p0 c0 {1,S} {3,S} {6,D}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Br1s u0 p3 c0 {1,S}
5   Br1s u0 p3 c0 {1,S}
6   Cd   u0 p0 c0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 182,
    label = "Cs-Cd(Cd-BrBr)-Cs",
    group = 
"""
1 * Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd   u0 p0 c0 {1,D} {5,S} {6,S}
3   Cs   u0 p0 c0 {1,S} {4,S}
4   Cs   u0 p0 c0 {1,S} {3,S}
5   Br1s u0 p3 c0 {2,S}
6   Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 183,
    label = "Cd(Cd-Br)-Cs-Cs",
    group = 
"""
1 * Cd   u0 p0 c0 {2,S} {3,S} {4,D}
2   Cs   u0 p0 c0 {1,S} {3,S}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Cd   u0 p0 c0 {1,D} {5,S}
5   Br1s u0 p3 c0 {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 184,
    label = "Cs-Cd(Cd)-Cs(Br)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2 * Cd   u0 p0 c0 {1,S} {3,S} {4,D}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Cd   u0 p0 c0 {2,D}
5   Br1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 185,
    label = "Cs-Cd(Cd)-Cs(Cl)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2 * Cd   u0 p0 c0 {1,S} {3,S} {5,D}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {1,S}
5   Cd   u0 p0 c0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 186,
    label = "Cs-Cs(Cl)(Cl)-Cd(Cd)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cd   u0 p0 c0 {1,S} {3,S} {6,D}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {1,S}
5   Cl1s u0 p3 c0 {1,S}
6   Cd   u0 p0 c0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 187,
    label = "Cs-Cd(Cd-ClCl)-Cs",
    group = 
"""
1 * Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd   u0 p0 c0 {1,D} {5,S} {6,S}
3   Cs   u0 p0 c0 {1,S} {4,S}
4   Cs   u0 p0 c0 {1,S} {3,S}
5   Cl1s u0 p3 c0 {2,S}
6   Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 188,
    label = "Cs-Cs-Cd(Cd-Cl)",
    group = 
"""
1 * Cd   u0 p0 c0 {2,S} {3,S} {4,D}
2   Cs   u0 p0 c0 {1,S} {3,S}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Cd   u0 p0 c0 {1,D} {5,S}
5   Cl1s u0 p3 c0 {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 189,
    label = "Cs-Cs(F)(F)-Cd(Cd)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cd  u0 p0 c0 {1,S} {3,S} {6,D}
3   Cs  u0 p0 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
6   Cd  u0 p0 c0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 190,
    label = "Cd(Cd-F)-Cs-Cs",
    group = 
"""
1 * Cd  u0 p0 c0 {2,S} {3,S} {4,D}
2   Cs  u0 p0 c0 {1,S} {3,S}
3   Cs  u0 p0 c0 {1,S} {2,S}
4   Cd  u0 p0 c0 {1,D} {5,S}
5   F1s u0 p3 c0 {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 191,
    label = "Cs-Cd(Cd-FF)-Cs",
    group = 
"""
1 * Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S} {6,S}
3   Cs  u0 p0 c0 {1,S} {4,S}
4   Cs  u0 p0 c0 {1,S} {3,S}
5   F1s u0 p3 c0 {2,S}
6   F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 192,
    label = "Cd(Cd)-Cs-Cs(F)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2 * Cd  u0 p0 c0 {1,S} {3,S} {5,D}
3   Cs  u0 p0 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {1,S}
5   Cd  u0 p0 c0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 193,
    label = "cyclopropanone",
    group = 
"""
1 * [C,N,S]   u0 {2,S} {3,S} {4,D}
2   [C,N,O,S] u0 {1,S} {3,S}
3   [C,N,O,S] u0 {1,S} {2,S}
4   [O,S]     u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.274,-1.932,-1.307,-0.838,-1.06,-1.032,-0.271],'cal/(mol*K)'),
        H298 = (45.6,'kcal/mol'),
        S298 = (30.7247,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 194,
    label = "Cs-CO(O2d)-Cs(Br)(Br)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * CO   u0 p0 c0 {1,S} {3,S} {6,D}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Br1s u0 p3 c0 {1,S}
5   Br1s u0 p3 c0 {1,S}
6   O2d  u0 p2 c0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 195,
    label = "Cs-Cs(Br)-CO(O2d)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2 * CO   u0 p0 c0 {1,S} {3,S} {5,D}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Br1s u0 p3 c0 {1,S}
5   O2d  u0 p2 c0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 196,
    label = "Cs-CO(O2d)-Cs(Cl)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2 * CO   u0 p0 c0 {1,S} {3,S} {5,D}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {1,S}
5   O2d  u0 p2 c0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 197,
    label = "Cs-CO(O2d)-Cs(Cl)(Cl)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * CO   u0 p0 c0 {1,S} {3,S} {6,D}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {1,S}
5   Cl1s u0 p3 c0 {1,S}
6   O2d  u0 p2 c0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 198,
    label = "O2s-Cs(Cl)-CO(O2d)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2 * CO   u0 p0 c0 {1,S} {3,S} {5,D}
3   O2s  u0 p2 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {1,S}
5   O2d  u0 p2 c0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 199,
    label = "O2s-CO(O2d)-Cs(Cl)(Cl)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * CO   u0 p0 c0 {1,S} {3,S} {6,D}
3   O2s  u0 p2 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {1,S}
5   Cl1s u0 p3 c0 {1,S}
6   O2d  u0 p2 c0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 200,
    label = "CO(O2d)-O2s-Cs(F)(F)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * CO  u0 p0 c0 {1,S} {3,S} {6,D}
3   O2s u0 p2 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
6   O2d u0 p2 c0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 201,
    label = "CO(O2d)-Cs-Cs(F)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2 * CO  u0 p0 c0 {1,S} {3,S} {5,D}
3   Cs  u0 p0 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {1,S}
5   O2d u0 p2 c0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 202,
    label = "Cs(F)(F)-Cs-CO(O2d)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * CO  u0 p0 c0 {1,S} {3,S} {6,D}
3   Cs  u0 p0 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
6   O2d u0 p2 c0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 203,
    label = "O2s-CO(O2d)-Cs(F)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S}
2 * CO  u0 p0 c0 {1,S} {3,S} {5,D}
3   O2s u0 p2 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {1,S}
5   O2d u0 p2 c0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 204,
    label = "methylenecyclopropene",
    group = 
"""
1 * [C,N,S]   u0 {2,S} {3,S} {4,D}
2   [C,N,S]   u0 {1,S} {3,D}
3   [C,N,O,S] u0 {1,S} {2,D}
4   [C,N,O,S] u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.457,-0.093,-0.645,-1.124,-1.936,-2.246,-2.962],'cal/(mol*K)'),
        H298 = (69.316,'kcal/mol'),
        S298 = (39.8857,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 205,
    label = "Cd(Cd)-Cd-Cd(Br)",
    group = 
"""
1 * Cd   u0 p0 c0 {2,S} {3,S} {5,D}
2   Cd   u0 p0 c0 {1,S} {3,D} {4,S}
3   Cd   u0 p0 c0 {1,S} {2,D}
4   Br1s u0 p3 c0 {2,S}
5   Cd   u0 p0 c0 {1,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 206,
    label = "Cd-Cd-Cd(Cd-Br)",
    group = 
"""
1 * Cd   u0 p0 c0 {2,S} {3,S} {4,D}
2   Cd   u0 p0 c0 {1,S} {3,D}
3   Cd   u0 p0 c0 {1,S} {2,D}
4   Cd   u0 p0 c0 {1,D} {5,S}
5   Br1s u0 p3 c0 {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 207,
    label = "Cd-Cd-Cd(Cd-BrBr)",
    group = 
"""
1 * Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd   u0 p0 c0 {1,D} {5,S} {6,S}
3   Cd   u0 p0 c0 {1,S} {4,D}
4   Cd   u0 p0 c0 {1,S} {3,D}
5   Br1s u0 p3 c0 {2,S}
6   Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 208,
    label = "Cd(Cd)-Cd(Cl)-Cd",
    group = 
"""
1 * Cd   u0 p0 c0 {2,S} {3,S} {5,D}
2   Cd   u0 p0 c0 {1,S} {3,D} {4,S}
3   Cd   u0 p0 c0 {1,S} {2,D}
4   Cl1s u0 p3 c0 {2,S}
5   Cd   u0 p0 c0 {1,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 209,
    label = "Cd-Cd-Cd(Cd-ClCl)",
    group = 
"""
1 * Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd   u0 p0 c0 {1,D} {5,S} {6,S}
3   Cd   u0 p0 c0 {1,S} {4,D}
4   Cd   u0 p0 c0 {1,S} {3,D}
5   Cl1s u0 p3 c0 {2,S}
6   Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 210,
    label = "Cd-Cd(Cd-Cl)-Cd",
    group = 
"""
1 * Cd   u0 p0 c0 {2,S} {3,S} {4,D}
2   Cd   u0 p0 c0 {1,S} {3,D}
3   Cd   u0 p0 c0 {1,S} {2,D}
4   Cd   u0 p0 c0 {1,D} {5,S}
5   Cl1s u0 p3 c0 {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 211,
    label = "Cd(F)-Cd-Cd(Cd)",
    group = 
"""
1 * Cd  u0 p0 c0 {2,S} {3,S} {5,D}
2   Cd  u0 p0 c0 {1,S} {3,D} {4,S}
3   Cd  u0 p0 c0 {1,S} {2,D}
4   F1s u0 p3 c0 {2,S}
5   Cd  u0 p0 c0 {1,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 212,
    label = "Cd-Cd-Cd(Cd-F)",
    group = 
"""
1 * Cd  u0 p0 c0 {2,S} {3,S} {4,D}
2   Cd  u0 p0 c0 {1,S} {3,D}
3   Cd  u0 p0 c0 {1,S} {2,D}
4   Cd  u0 p0 c0 {1,D} {5,S}
5   F1s u0 p3 c0 {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 213,
    label = "Cd-Cd(Cd-FF)-Cd",
    group = 
"""
1 * Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S} {6,S}
3   Cd  u0 p0 c0 {1,S} {4,D}
4   Cd  u0 p0 c0 {1,S} {3,D}
5   F1s u0 p3 c0 {2,S}
6   F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 214,
    label = "methylenecyclopropanone",
    group = 
"""
1 * [C,N,S]    u0 {2,S} {3,S} {4,D}
2   [CO,CS]    u0 {1,S} {3,S}
3   [Cs,N,O,S] u0 {1,S} {2,S}
4   [C,N,O,S]  u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.13,-1.101,-1.774,-2.139,-2.509,-2.858,-0.084],'cal/(mol*K)'),
        H298 = (57.7946,'kcal/mol'),
        S298 = (37.18,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 215,
    label = "methyleneoxirane",
    group = 
"""
1 * [C,N,S]   u0 {2,S} {3,S} {4,D}
2   [O2s,S2s] u0 {1,S} {3,S}
3   [Cs,N]    u0 {1,S} {2,S}
4   [C,N,O,S] u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.101,-2.381,-2.338,-2.236,-2.424,-2.639,-2.068],'cal/(mol*K)'),
        H298 = (36.0543,'kcal/mol'),
        S298 = (29.893,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 216,
    label = "Cs-O2s-Cd(Cd-BrBr)",
    group = 
"""
1 * Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd   u0 p0 c0 {1,D} {5,S} {6,S}
3   Cs   u0 p0 c0 {1,S} {4,S}
4   O2s  u0 p2 c0 {1,S} {3,S}
5   Br1s u0 p3 c0 {2,S}
6   Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 217,
    label = "Cs(Br)-O2s-Cd(Cd)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S}
2 * Cd   u0 p0 c0 {1,S} {3,S} {5,D}
3   O2s  u0 p2 c0 {1,S} {2,S}
4   Br1s u0 p3 c0 {1,S}
5   Cd   u0 p0 c0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 218,
    label = "Cs(Br)(Br)-O2s-Cd(Cd)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cd   u0 p0 c0 {1,S} {3,S} {6,D}
3   O2s  u0 p2 c0 {1,S} {2,S}
4   Br1s u0 p3 c0 {1,S}
5   Br1s u0 p3 c0 {1,S}
6   Cd   u0 p0 c0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 219,
    label = "Cd(Cd-Br)-Cs-O2s",
    group = 
"""
1 * Cd   u0 p0 c0 {2,S} {3,S} {4,D}
2   O2s  u0 p2 c0 {1,S} {3,S}
3   Cs   u0 p0 c0 {1,S} {2,S}
4   Cd   u0 p0 c0 {1,D} {5,S}
5   Br1s u0 p3 c0 {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 220,
    label = "Cd(Cd)-O2s-Cs(Cl)(Cl)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cd   u0 p0 c0 {1,S} {3,S} {6,D}
3   O2s  u0 p2 c0 {1,S} {2,S}
4   Cl1s u0 p3 c0 {1,S}
5   Cl1s u0 p3 c0 {1,S}
6   Cd   u0 p0 c0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 221,
    label = "Cs-Cd(Cd-ClCl)-O2s",
    group = 
"""
1 * Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd   u0 p0 c0 {1,D} {5,S} {6,S}
3   Cs   u0 p0 c0 {1,S} {4,S}
4   O2s  u0 p2 c0 {1,S} {3,S}
5   Cl1s u0 p3 c0 {2,S}
6   Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 222,
    label = "Cs-O2s-Cd(Cd-Cl)",
    group = 
"""
1 * Cd   u0 p0 c0 {2,S} {3,S} {4,D}
2   Cs   u0 p0 c0 {1,S} {3,S}
3   O2s  u0 p2 c0 {1,S} {2,S}
4   Cd   u0 p0 c0 {1,D} {5,S}
5   Cl1s u0 p3 c0 {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 223,
    label = "Cs(Cl)-Cd(Cd)-O2s",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2 * Cd   u0 p0 c0 {1,S} {3,S} {4,D}
3   O2s  u0 p2 c0 {1,S} {2,S}
4   Cd   u0 p0 c0 {2,D}
5   Cl1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 224,
    label = "O2s-Cs(F)(F)-Cd(Cd)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 * Cd  u0 p0 c0 {1,S} {3,S} {6,D}
3   O2s u0 p2 c0 {1,S} {2,S}
4   F1s u0 p3 c0 {1,S}
5   F1s u0 p3 c0 {1,S}
6   Cd  u0 p0 c0 {2,D}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 225,
    label = "Cd(Cd-F)-Cs-O2s",
    group = 
"""
1 * Cd  u0 p0 c0 {2,S} {3,S} {4,D}
2   O2s u0 p2 c0 {1,S} {3,S}
3   Cs  u0 p0 c0 {1,S} {2,S}
4   Cd  u0 p0 c0 {1,D} {5,S}
5   F1s u0 p3 c0 {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 226,
    label = "O2s-Cs-Cd(Cd-FF)",
    group = 
"""
1 * Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S} {6,S}
3   Cs  u0 p0 c0 {1,S} {4,S}
4   O2s u0 p2 c0 {1,S} {3,S}
5   F1s u0 p3 c0 {2,S}
6   F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 227,
    label = "Cs(F)-Cd(Cd)-O2s",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {5,S}
2 * Cd  u0 p0 c0 {1,S} {3,S} {4,D}
3   O2s u0 p2 c0 {1,S} {2,S}
4   Cd  u0 p0 c0 {2,D}
5   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 228,
    label = "12Methylenecyclopropane",
    group = 
"""
1   [C,N,S]    u0 {2,S} {3,S} {4,D}
2 * [C,N,S]    u0 {1,S} {3,S} {5,D}
3   [Cs,N,O,S] u0 {1,S} {2,S}
4   [C,N,O,S]  u0 {1,D}
5   [C,N,O,S]  u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.326,-3.139,-3.361,-3.148,-2.736,-2.412,-1.706],'cal/(mol*K)'),
        H298 = (51.4711,'kcal/mol'),
        S298 = (35.3587,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 229,
    label = "O2s-O2s-Cd(Cd-Br)",
    group = 
"""
1 * Cd   u0 p0 c0 {2,S} {3,S} {4,D}
2   O2s  u0 p2 c0 {1,S} {3,S}
3   O2s  u0 p2 c0 {1,S} {2,S}
4   Cd   u0 p0 c0 {1,D} {5,S}
5   Br1s u0 p3 c0 {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 230,
    label = "O2s-O2s-Cd(Cd-BrBr)",
    group = 
"""
1 * Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd   u0 p0 c0 {1,D} {5,S} {6,S}
3   O2s  u0 p2 c0 {1,S} {4,S}
4   O2s  u0 p2 c0 {1,S} {3,S}
5   Br1s u0 p3 c0 {2,S}
6   Br1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 231,
    label = "O2s-O2s-Cd(Cd-Cl)",
    group = 
"""
1 * Cd   u0 p0 c0 {2,S} {3,S} {4,D}
2   O2s  u0 p2 c0 {1,S} {3,S}
3   O2s  u0 p2 c0 {1,S} {2,S}
4   Cd   u0 p0 c0 {1,D} {5,S}
5   Cl1s u0 p3 c0 {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 232,
    label = "O2s-Cd(Cd-ClCl)-O2s",
    group = 
"""
1 * Cd   u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd   u0 p0 c0 {1,D} {5,S} {6,S}
3   O2s  u0 p2 c0 {1,S} {4,S}
4   O2s  u0 p2 c0 {1,S} {3,S}
5   Cl1s u0 p3 c0 {2,S}
6   Cl1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 233,
    label = "O2s-Cd(Cd-FF)-O2s",
    group = 
"""
1 * Cd  u0 p0 c0 {2,D} {3,S} {4,S}
2   Cd  u0 p0 c0 {1,D} {5,S} {6,S}
3   O2s u0 p2 c0 {1,S} {4,S}
4   O2s u0 p2 c0 {1,S} {3,S}
5   F1s u0 p3 c0 {2,S}
6   F1s u0 p3 c0 {2,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 234,
    label = "O2s-O2s-Cd(Cd-F)",
    group = 
"""
1 * Cd  u0 p0 c0 {2,S} {3,S} {4,D}
2   O2s u0 p2 c0 {1,S} {3,S}
3   O2s u0 p2 c0 {1,S} {2,S}
4   Cd  u0 p0 c0 {1,D} {5,S}
5   F1s u0 p3 c0 {4,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 235,
    label = "FourMember",
    group = 
"""
1 * R!H u0 {2,[S,D]} {4,[S,D]}
2   R!H u0 {1,[S,D]} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,[S,D]}
4   R!H u0 {1,[S,D]} {3,[S,D]}
""",
    thermo = 'Cyclobutane',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 236,
    label = "Cyclobutane",
    group = 
"""
1 * Cs u0 {2,S} {4,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.61,-3.89,-3.14,-2.64,-1.88,-1.38,-0.67],'cal/(mol*K)'),
        H298 = (26.2,'kcal/mol'),
        S298 = (29.8,'cal/(mol*K)'),
    ),
    shortDesc = """Cyclobutane ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 237,
    label = "Cs-Cs(Br)(Br)-Cs-Cs",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 * Cs   u0 p0 c0 {1,S} {4,S}
3   Cs   u0 p0 c0 {1,S} {4,S}
4   Cs   u0 p0 c0 {2,S} {3,S}
5   Br1s u0 p3 c0 {1,S}
6   Br1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 238,
    label = "Cs(Br)-Cs-Cs-Cs",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {4,S}
3 * Cs   u0 p0 c0 {1,S} {4,S}
4   Cs   u0 p0 c0 {2,S} {3,S}
5   Br1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 239,
    label = "Cs-Cs(Cl)-Cs-Cs",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {4,S}
3 * Cs   u0 p0 c0 {1,S} {4,S}
4   Cs   u0 p0 c0 {2,S} {3,S}
5   Cl1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 240,
    label = "Cs-Cs(Cl)(Cl)-Cs-Cs",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2   Cs   u0 p0 c0 {1,S} {4,S}
3 * Cs   u0 p0 c0 {1,S} {4,S}
4   Cs   u0 p0 c0 {2,S} {3,S}
5   Cl1s u0 p3 c0 {1,S}
6   Cl1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 241,
    label = "Cs(F)-Cs-Cs-Cs",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {5,S}
2 * Cs  u0 p0 c0 {1,S} {4,S}
3   Cs  u0 p0 c0 {1,S} {4,S}
4   Cs  u0 p0 c0 {2,S} {3,S}
5   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 242,
    label = "Cs-Cs-Cs(F)(F)-Cs",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 * Cs  u0 p0 c0 {1,S} {4,S}
3   Cs  u0 p0 c0 {1,S} {4,S}
4   Cs  u0 p0 c0 {2,S} {3,S}
5   F1s u0 p3 c0 {1,S}
6   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 243,
    label = "34methylenecyclobutene",
    group = 
"""
1 * Cd u0 {2,S} {3,S} {5,D}
2   Cd u0 {1,S} {4,S} {6,D}
3   Cd u0 {1,S} {4,D}
4   Cd u0 {2,S} {3,D}
5   Cd u0 {1,D}
6   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.441,0.307,-0.336,-1.197,-1.921,-1.513,-3.264],'cal/(mol*K)'),
        H298 = (33.076,'kcal/mol'),
        S298 = (38.6947,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3""",
    longDesc = 
"""

""",
)

entry(
    index = 244,
    label = "dioxerene",
    group = 
"""
1   [Cd,N] u0 {2,D} {4,S}
2 * [Cd,N] u0 {1,D} {3,S}
3   O2s    u0 {2,S} {4,S}
4   O2s    u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.375,-4.281,-4.206,-4.037,-3.926,-3.327,-2.473],'cal/(mol*K)'),
        H298 = (24.4413,'kcal/mol'),
        S298 = (29.7827,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 245,
    label = "Oxetene",
    group = 
"""
1 * O2s     u0 {2,S} {4,S}
2   [C,N,S] u0 {1,S} {3,D}
3   [C,N,S] u0 {2,D} {4,S}
4   [C,N,S] u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.88,-4.22,-4.18,-3.97,-3.65,-3.56,-2.93],'cal/(mol*K)'),
        H298 = (32.51,'kcal/mol'),
        S298 = (29.26,'cal/(mol*K)'),
    ),
    shortDesc = """Derived from goldsmith's DFT-QCI library""",
    longDesc = 
"""

""",
)

entry(
    index = 246,
    label = "Cd-Cd-O2s-Cs(F)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {5,S}
2 * O2s u0 p2 c0 {1,S} {4,S}
3   Cd  u0 p0 c0 {1,S} {4,D}
4   Cd  u0 p0 c0 {2,S} {3,D}
5   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 247,
    label = "four-inringonedouble",
    group = 
"""
1   R!H u0 {2,D} {4,S}
2   R!H u0 {1,D} {3,S}
3 * R!H u0 {2,S} {4,S}
4   R!H u0 {1,S} {3,S}
""",
    thermo = 'Cyclobutene',
    shortDesc = """""",
    longDesc = 
"""
Use cyclobutene correction for any four membered ring with one double bond
""",
)

entry(
    index = 248,
    label = "Cyclobutene",
    group = 
"""
1 * [Cs,N,O,S] u0 {2,S} {4,S}
2   [C,N,O,S]  u0 {1,S} {3,D}
3   [C,N,O,S]  u0 {2,D} {4,S}
4   [Cs,N,O,S] u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.038,-2.783,-2.423,-2.153,-1.888,-1.694,-1.258],'cal/(mol*K)'),
        H298 = (29.84,'kcal/mol'),
        S298 = (29.8677,'cal/(mol*K)'),
    ),
    shortDesc = """Cyclobutene ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 249,
    label = "Cs(Br)-Cd-Cd-O2s",
    group = 
"""
1 * Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2   O2s  u0 p2 c0 {1,S} {4,S}
3   Cd   u0 p0 c0 {1,S} {4,D}
4   Cd   u0 p0 c0 {2,S} {3,D}
5   Br1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 250,
    label = "Cd-Cd-Cs(Br)(Br)-O2s",
    group = 
"""
1 * Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2   Cd   u0 p0 c0 {1,S} {4,D}
3   O2s  u0 p2 c0 {1,S} {4,S}
4   Cd   u0 p0 c0 {2,D} {3,S}
5   Br1s u0 p3 c0 {1,S}
6   Br1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 251,
    label = "Cs-Cd-Cd-Cs(Br)",
    group = 
"""
1 * Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {4,S}
3   Cd   u0 p0 c0 {1,S} {4,D}
4   Cd   u0 p0 c0 {2,S} {3,D}
5   Br1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 252,
    label = "Cd(Br)-Cd-Cs-O2s",
    group = 
"""
1   Cd   u0 p0 c0 {2,D} {3,S} {5,S}
2   Cd   u0 p0 c0 {1,D} {4,S}
3   O2s  u0 p2 c0 {1,S} {4,S}
4 * Cs   u0 p0 c0 {2,S} {3,S}
5   Br1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 253,
    label = "Cs-Cs(Br)(Br)-Cd-Cd",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 * Cs   u0 p0 c0 {1,S} {4,S}
3   Cd   u0 p0 c0 {1,S} {4,D}
4   Cd   u0 p0 c0 {2,S} {3,D}
5   Br1s u0 p3 c0 {1,S}
6   Br1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 254,
    label = "Cd(Br)-Cd-O2s-Cs",
    group = 
"""
1   Cd   u0 p0 c0 {2,S} {3,D} {5,S}
2 * Cs   u0 p0 c0 {1,S} {4,S}
3   Cd   u0 p0 c0 {1,D} {4,S}
4   O2s  u0 p2 c0 {2,S} {3,S}
5   Br1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 255,
    label = "Cd(Br)-Cd-Cs-Cs",
    group = 
"""
1   Cd   u0 p0 c0 {2,S} {3,D} {5,S}
2   Cs   u0 p0 c0 {1,S} {4,S}
3   Cd   u0 p0 c0 {1,D} {4,S}
4 * Cs   u0 p0 c0 {2,S} {3,S}
5   Br1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 256,
    label = "O2s-O2s-Cd-Cd(Br)",
    group = 
"""
1   Cd   u0 p0 c0 {2,D} {3,S} {5,S}
2   Cd   u0 p0 c0 {1,D} {4,S}
3 * O2s  u0 p2 c0 {1,S} {4,S}
4   O2s  u0 p2 c0 {2,S} {3,S}
5   Br1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 257,
    label = "Cs-Cd(Cl)-Cd-Cs",
    group = 
"""
1   Cd   u0 p0 c0 {2,S} {3,D} {5,S}
2   Cs   u0 p0 c0 {1,S} {4,S}
3   Cd   u0 p0 c0 {1,D} {4,S}
4 * Cs   u0 p0 c0 {2,S} {3,S}
5   Cl1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 258,
    label = "Cd-Cd-O2s-Cs(Cl)",
    group = 
"""
1 * Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2   Cd   u0 p0 c0 {1,S} {4,D}
3   O2s  u0 p2 c0 {1,S} {4,S}
4   Cd   u0 p0 c0 {2,D} {3,S}
5   Cl1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 259,
    label = "Cd-Cs(Cl)(Cl)-O2s-Cd",
    group = 
"""
1 * Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2   Cd   u0 p0 c0 {1,S} {4,D}
3   O2s  u0 p2 c0 {1,S} {4,S}
4   Cd   u0 p0 c0 {2,D} {3,S}
5   Cl1s u0 p3 c0 {1,S}
6   Cl1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 260,
    label = "Cd(Cl)-O2s-Cs-Cd",
    group = 
"""
1   Cd   u0 p0 c0 {2,S} {3,D} {5,S}
2   O2s  u0 p2 c0 {1,S} {4,S}
3   Cd   u0 p0 c0 {1,D} {4,S}
4 * Cs   u0 p0 c0 {2,S} {3,S}
5   Cl1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 261,
    label = "Cs-Cs(Cl)-Cd-Cd",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2 * Cs   u0 p0 c0 {1,S} {4,S}
3   Cd   u0 p0 c0 {1,S} {4,D}
4   Cd   u0 p0 c0 {2,S} {3,D}
5   Cl1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 262,
    label = "Cd-Cs-Cs(Cl)(Cl)-Cd",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 * Cs   u0 p0 c0 {1,S} {4,S}
3   Cd   u0 p0 c0 {1,S} {4,D}
4   Cd   u0 p0 c0 {2,S} {3,D}
5   Cl1s u0 p3 c0 {1,S}
6   Cl1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 263,
    label = "Cs-O2s-Cd-Cd(Cl)",
    group = 
"""
1   Cd   u0 p0 c0 {2,S} {3,D} {5,S}
2 * Cs   u0 p0 c0 {1,S} {4,S}
3   Cd   u0 p0 c0 {1,D} {4,S}
4   O2s  u0 p2 c0 {2,S} {3,S}
5   Cl1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 264,
    label = "Cd-O2s-O2s-Cd(Cl)",
    group = 
"""
1   Cd   u0 p0 c0 {2,D} {3,S} {5,S}
2   Cd   u0 p0 c0 {1,D} {4,S}
3 * O2s  u0 p2 c0 {1,S} {4,S}
4   O2s  u0 p2 c0 {2,S} {3,S}
5   Cl1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 265,
    label = "O2s-Cd-Cd-Cs(F)(F)",
    group = 
"""
1 * Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2   Cd  u0 p0 c0 {1,S} {4,D}
3   O2s u0 p2 c0 {1,S} {4,S}
4   Cd  u0 p0 c0 {2,D} {3,S}
5   F1s u0 p3 c0 {1,S}
6   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 266,
    label = "Cs(F)-Cs-Cd-Cd",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {5,S}
2 * Cs  u0 p0 c0 {1,S} {4,S}
3   Cd  u0 p0 c0 {1,S} {4,D}
4   Cd  u0 p0 c0 {2,S} {3,D}
5   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 267,
    label = "Cd-Cs-Cs(F)(F)-Cd",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 * Cs  u0 p0 c0 {1,S} {4,S}
3   Cd  u0 p0 c0 {1,S} {4,D}
4   Cd  u0 p0 c0 {2,S} {3,D}
5   F1s u0 p3 c0 {1,S}
6   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 268,
    label = "Cd(F)-Cd-Cs-Cs",
    group = 
"""
1   Cd  u0 p0 c0 {2,S} {3,D} {5,S}
2 * Cs  u0 p0 c0 {1,S} {4,S}
3   Cd  u0 p0 c0 {1,D} {4,S}
4   Cs  u0 p0 c0 {2,S} {3,S}
5   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 269,
    label = "Cd-Cd(F)-Cs-O2s",
    group = 
"""
1   Cd  u0 p0 c0 {2,S} {3,D} {5,S}
2 * Cs  u0 p0 c0 {1,S} {4,S}
3   Cd  u0 p0 c0 {1,D} {4,S}
4   O2s u0 p2 c0 {2,S} {3,S}
5   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 270,
    label = "Cs-Cd-Cd(F)-O2s",
    group = 
"""
1   Cd  u0 p0 c0 {2,D} {3,S} {5,S}
2   Cd  u0 p0 c0 {1,D} {4,S}
3   O2s u0 p2 c0 {1,S} {4,S}
4 * Cs  u0 p0 c0 {2,S} {3,S}
5   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 271,
    label = "Cd-Cd(F)-O2s-O2s",
    group = 
"""
1   Cd  u0 p0 c0 {2,D} {3,S} {5,S}
2   Cd  u0 p0 c0 {1,D} {4,S}
3 * O2s u0 p2 c0 {1,S} {4,S}
4   O2s u0 p2 c0 {2,S} {3,S}
5   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 272,
    label = "Oxetane",
    group = 
"""
1 * O2s      u0 {2,S} {4,S}
2   [Cs,N,S] u0 {1,S} {3,S}
3   [Cs,N,S] u0 {2,S} {4,S}
4   [Cs,N,S] u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.08,-4.28,-3.636,-3.016,-2.451,-1.896,2.84],'cal/(mol*K)'),
        H298 = (25.08,'kcal/mol'),
        S298 = (28.5487,'cal/(mol*K)'),
    ),
    shortDesc = """CY/C3O from THERM (Dorofeeva, 92) Cp1500 est. as Cp1000""",
    longDesc = 
"""

""",
)

entry(
    index = 273,
    label = "Cs-Cs(Br)-Cs-O2s",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {4,S}
3   Cs   u0 p0 c0 {1,S} {4,S}
4 * O2s  u0 p2 c0 {2,S} {3,S}
5   Br1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 274,
    label = "O2s-Cs-Cs(Br)(Br)-Cs",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2   Cs   u0 p0 c0 {1,S} {4,S}
3   Cs   u0 p0 c0 {1,S} {4,S}
4 * O2s  u0 p2 c0 {2,S} {3,S}
5   Br1s u0 p3 c0 {1,S}
6   Br1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 275,
    label = "Cs-Cs-Cs(Br)(Br)-O2s",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2   Cs   u0 p0 c0 {1,S} {4,S}
3 * O2s  u0 p2 c0 {1,S} {4,S}
4   Cs   u0 p0 c0 {2,S} {3,S}
5   Br1s u0 p3 c0 {1,S}
6   Br1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 276,
    label = "O2s-Cs(Br)-Cs-Cs",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2 * O2s  u0 p2 c0 {1,S} {4,S}
3   Cs   u0 p0 c0 {1,S} {4,S}
4   Cs   u0 p0 c0 {2,S} {3,S}
5   Br1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 277,
    label = "O2s-Cs(Cl)-Cs-Cs",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2 * O2s  u0 p2 c0 {1,S} {4,S}
3   Cs   u0 p0 c0 {1,S} {4,S}
4   Cs   u0 p0 c0 {2,S} {3,S}
5   Cl1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 278,
    label = "O2s-Cs-Cs-Cs(Cl)(Cl)",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 * O2s  u0 p2 c0 {1,S} {4,S}
3   Cs   u0 p0 c0 {1,S} {4,S}
4   Cs   u0 p0 c0 {2,S} {3,S}
5   Cl1s u0 p3 c0 {1,S}
6   Cl1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 279,
    label = "O2s-Cs-Cs(Cl)-Cs",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2   Cs   u0 p0 c0 {1,S} {4,S}
3   Cs   u0 p0 c0 {1,S} {4,S}
4 * O2s  u0 p2 c0 {2,S} {3,S}
5   Cl1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 280,
    label = "Cs-Cs(Cl)(Cl)-Cs-O2s",
    group = 
"""
1   Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2   Cs   u0 p0 c0 {1,S} {4,S}
3   Cs   u0 p0 c0 {1,S} {4,S}
4 * O2s  u0 p2 c0 {2,S} {3,S}
5   Cl1s u0 p3 c0 {1,S}
6   Cl1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 281,
    label = "O2s-Cs-Cs-Cs(F)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {5,S}
2   Cs  u0 p0 c0 {1,S} {4,S}
3 * O2s u0 p2 c0 {1,S} {4,S}
4   Cs  u0 p0 c0 {2,S} {3,S}
5   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 282,
    label = "Cs-Cs(F)(F)-O2s-Cs",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2   Cs  u0 p0 c0 {1,S} {4,S}
3 * O2s u0 p2 c0 {1,S} {4,S}
4   Cs  u0 p0 c0 {2,S} {3,S}
5   F1s u0 p3 c0 {1,S}
6   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 283,
    label = "Cs-O2s-Cs-Cs(F)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {5,S}
2   Cs  u0 p0 c0 {1,S} {4,S}
3   Cs  u0 p0 c0 {1,S} {4,S}
4 * O2s u0 p2 c0 {2,S} {3,S}
5   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 284,
    label = "Cs-O2s-Cs-Cs(F)(F)",
    group = 
"""
1   Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2   Cs  u0 p0 c0 {1,S} {4,S}
3   Cs  u0 p0 c0 {1,S} {4,S}
4 * O2s u0 p2 c0 {2,S} {3,S}
5   F1s u0 p3 c0 {1,S}
6   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 285,
    label = "Beta-Propiolactone",
    group = 
"""
1 * O2s      u0 {2,S} {4,S}
2   [Cs,N,S] u0 {1,S} {3,S}
3   [Cs,N,S] u0 {2,S} {4,S}
4   [CO,CS]  u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.434,-4.019,-3.31,-2.703,-2.253,-2.012,1.3],'cal/(mol*K)'),
        H298 = (22.98,'kcal/mol'),
        S298 = (30.392,'cal/(mol*K)'),
    ),
    shortDesc = """Beta-Propiolactone ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 286,
    label = "Cyclobutanone",
    group = 
"""
1 * [CO,CS]  u0 {2,S} {4,S}
2   [Cs,N,S] u0 {1,S} {3,S}
3   [Cs,N,S] u0 {2,S} {4,S}
4   [Cs,N,S] u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.62,-4.96,-3.744,-2.671,-1.962,-1.415,-0.3],'cal/(mol*K)'),
        H298 = (22.53,'kcal/mol'),
        S298 = (29.8337,'cal/(mol*K)'),
    ),
    shortDesc = """Cyclobutanone ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 287,
    label = "12dioxetane",
    group = 
"""
1   [Cs,N] u0 {2,S} {4,S}
2 * [Cs,N] u0 {1,S} {3,S}
3   O2s    u0 {2,S} {4,S}
4   O2s    u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.512,-4.727,-5.01,-4.504,-4.218,-4.242,-2.465],'cal/(mol*K)','+|-',[0.7921,0.7921,0.7921,0.7921,0.7921,0.7921,0.7921]),
        H298 = (26.826,'kcal/mol','+|-',3.3865),
        S298 = (27.858,'cal/(mol*K)','+|-',1.0404),
    ),
    shortDesc = """Calculations from Duminda Ranasinghe""",
    longDesc = 
"""
Based on CBS-QB3 calculation with rotors and BAC for singlet C=CC1COO1 from Duminda Ranasinghe in 05/2019, fitted by Hao-Wei Pang
""",
)

entry(
    index = 288,
    label = "Cs-Cs(Br)-O2s-O2s",
    group = 
"""
1 * Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2   O2s  u0 p2 c0 {1,S} {4,S}
3   Cs   u0 p0 c0 {1,S} {4,S}
4   O2s  u0 p2 c0 {2,S} {3,S}
5   Br1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 289,
    label = "O2s-Cs(Br)(Br)-Cs-O2s",
    group = 
"""
1 * Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2   O2s  u0 p2 c0 {1,S} {4,S}
3   Cs   u0 p0 c0 {1,S} {4,S}
4   O2s  u0 p2 c0 {2,S} {3,S}
5   Br1s u0 p3 c0 {1,S}
6   Br1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 290,
    label = "Cs(Cl)-O2s-O2s-Cs",
    group = 
"""
1 * Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2   O2s  u0 p2 c0 {1,S} {4,S}
3   Cs   u0 p0 c0 {1,S} {4,S}
4   O2s  u0 p2 c0 {2,S} {3,S}
5   Cl1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 291,
    label = "O2s-Cs-Cs(Cl)(Cl)-O2s",
    group = 
"""
1 * Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2   Cs   u0 p0 c0 {1,S} {4,S}
3   O2s  u0 p2 c0 {1,S} {4,S}
4   O2s  u0 p2 c0 {2,S} {3,S}
5   Cl1s u0 p3 c0 {1,S}
6   Cl1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 292,
    label = "Cs-Cs(F)-O2s-O2s",
    group = 
"""
1 * Cs  u0 p0 c0 {2,S} {3,S} {5,S}
2   O2s u0 p2 c0 {1,S} {4,S}
3   Cs  u0 p0 c0 {1,S} {4,S}
4   O2s u0 p2 c0 {2,S} {3,S}
5   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 293,
    label = "O2s-Cs(F)(F)-Cs-O2s",
    group = 
"""
1 * Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2   O2s u0 p2 c0 {1,S} {4,S}
3   Cs  u0 p0 c0 {1,S} {4,S}
4   O2s u0 p2 c0 {2,S} {3,S}
5   F1s u0 p3 c0 {1,S}
6   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 294,
    label = "four-inringtwodouble",
    group = 
"""
1   R!H u0 {2,D} {4,[S,D]}
2 * R!H u0 {1,D} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,D}
4   R!H u0 {1,[S,D]} {3,D}
""",
    thermo = 'cyclobutadiene_13',
    shortDesc = """""",
    longDesc = 
"""
Use cyclobutadiene_13 correction for any four membered ring with at least two double bonds in the 1,3-positions
""",
)

entry(
    index = 295,
    label = "cyclobutadiene_13",
    group = 
"""
1   [Cd,N] u0 {2,D} {4,S}
2 * [Cd,N] u0 {1,D} {3,S}
3   [Cd,N] u0 {2,S} {4,D}
4   [Cd,N] u0 {1,S} {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.336,-3.24,-3.526,-3.419,-3.071,-2.761,-2.346],'cal/(mol*K)'),
        H298 = (77.2135,'kcal/mol'),
        S298 = (36.4303,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 296,
    label = "Cd-Cd-Cd-Cd(Br)",
    group = 
"""
1   Cd   u0 p0 c0 {2,D} {3,S} {5,S}
2   Cd   u0 p0 c0 {1,D} {4,S}
3   Cd   u0 p0 c0 {1,S} {4,D}
4 * Cd   u0 p0 c0 {2,S} {3,D}
5   Br1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 297,
    label = "Cd-Cd-Cd(Cl)-Cd",
    group = 
"""
1   Cd   u0 p0 c0 {2,D} {3,S} {5,S}
2   Cd   u0 p0 c0 {1,D} {4,S}
3   Cd   u0 p0 c0 {1,S} {4,D}
4 * Cd   u0 p0 c0 {2,S} {3,D}
5   Cl1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 298,
    label = "Cd-Cd-Cd-Cd(F)",
    group = 
"""
1   Cd  u0 p0 c0 {2,S} {3,D} {5,S}
2 * Cd  u0 p0 c0 {1,S} {4,D}
3   Cd  u0 p0 c0 {1,D} {4,S}
4   Cd  u0 p0 c0 {2,D} {3,S}
5   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 299,
    label = "cyclobutadiene_12",
    group = 
"""
1   R!H u0 {2,D} {4,S}
2 * R!H u0 {1,D} {3,D}
3   R!H u0 {2,D} {4,S}
4   R!H u0 {1,S} {3,S}
""",
    thermo = 'cyclobutadiene_13',
    shortDesc = """""",
    longDesc = 
"""
Use cyclobutadiene_13 correction for 1,2_CBD
""",
)

entry(
    index = 300,
    label = "thietane",
    group = 
"""
1 * S     u0 {2,S} {4,S}
2   [C,N] u0 {1,S} {3,S}
3   [C,N] u0 {2,S} {4,S}
4   [C,N] u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.42,-3.66,-2.92,-2.3,-1.53,-1.01,-0.3],'cal/(mol*K)'),
        H298 = (19.82,'kcal/mol'),
        S298 = (25.35,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
"""

""",
)

entry(
    index = 301,
    label = "1,2-dithietane",
    group = 
"""
1 * S     u0 {2,S} {4,S}
2   S     u0 {1,S} {3,S}
3   [C,N] u0 {2,S} {4,S}
4   [C,N] u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.24,-3.62,-3.13,-2.69,-2.11,-1.62,-0.79],'cal/(mol*K)'),
        H298 = (23.45,'kcal/mol'),
        S298 = (24.44,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
"""

""",
)

entry(
    index = 302,
    label = "1,3-dithietane",
    group = 
"""
1 * S     u0 {2,S} {4,S}
2   [C,N] u0 {1,S} {3,S}
3   S     u0 {2,S} {4,S}
4   [C,N] u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-11.59,-9.53,-7.27,-5.52,-3.34,-2.19,-0.96],'cal/(mol*K)'),
        H298 = (16.87,'kcal/mol'),
        S298 = (29.55,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
"""

""",
)

entry(
    index = 303,
    label = "trithietane",
    group = 
"""
1 * S     u0 {2,S} {4,S}
2   S     u0 {1,S} {3,S}
3   S     u0 {2,S} {4,S}
4   [C,N] u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.81,-7.66,-6.51,-5.66,-4.53,-3.75,-2.33],'cal/(mol*K)'),
        H298 = (30.77,'kcal/mol'),
        S298 = (29.05,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
"""

""",
)

entry(
    index = 304,
    label = "tetrathietane",
    group = 
"""
1 * S u0 {2,S} {4,S}
2   S u0 {1,S} {3,S}
3   S u0 {2,S} {4,S}
4   S u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.92,-7.46,-7.14,-6.99,-6.77,-6.27,-4.36],'cal/(mol*K)'),
        H298 = (22.72,'kcal/mol'),
        S298 = (32.19,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009, dH from NIST-JANAF""",
    longDesc = 
"""

""",
)

entry(
    index = 305,
    label = "Azetidine",
    group = 
"""
1 * N          u0 {2,S} {4,S}
2   [Cs,N,O,S] u0 {1,S} {3,S}
3   [Cs,N,O,S] u0 {2,S} {4,S}
4   [Cs,N,O,S] u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (26.2,'kcal/mol'),
        S298 = (29.3,'cal/(mol*K)'),
    ),
    shortDesc = """Azetidine ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 306,
    label = "4-Methylene-2-oxetanone",
    group = 
"""
1   [Cd,N]  u0 {2,S} {3,S} {5,D}
2 * O       u0 {1,S} {4,S}
3   [Cs,N]  u0 {1,S} {4,S}
4   [CO,CS] u0 {2,S} {3,S}
5   [Cd,N]  u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.912,-1.903,-1.567,-1.378,-1.566,-1.528,1.547],'cal/(mol*K)'),
        H298 = (16.94,'kcal/mol'),
        S298 = (35.477,'cal/(mol*K)'),
    ),
    shortDesc = """4-Methylene-2-oxetanone ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 307,
    label = "methylenecyclobutane",
    group = 
"""
1 * [Cd,N] u0 {2,S} {3,S} {5,D}
2   [Cs,N] u0 {1,S} {4,S}
3   [Cs,N] u0 {1,S} {4,S}
4   [Cs,N] u0 {2,S} {3,S}
5   [Cd,N] u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.862,-3.896,-3.629,-3.244,-2.48,-1.836,-1.085],'cal/(mol*K)'),
        H298 = (29.371,'kcal/mol'),
        S298 = (30.511,'cal/(mol*K)'),
    ),
    shortDesc = """Fitted from CBS-QB3 calculation""",
    longDesc = 
"""
"
Fitted from CBS-QB3 calculation for C=C1CCC1. Mengjie Liu 9/9/19.
""",
)

entry(
    index = 308,
    label = "2methyleneoxetane",
    group = 
"""
1 * [Cd,N]    u0 {2,S} {3,S} {5,D}
2   [O2s,S2s] u0 {1,S} {4,S}
3   [Cs,N]    u0 {1,S} {4,S}
4   [Cs,N]    u0 {2,S} {3,S}
5   [Cd,N]    u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.33,-3.553,-3.213,-2.78,-2.445,-2.331,0.556],'cal/(mol*K)'),
        H298 = (23.79,'kcal/mol'),
        S298 = (25.597,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 309,
    label = "12methylenecyclobutane",
    group = 
"""
1 * [Cd,N,S]   u0 {2,S} {4,S} {5,D}
2   [Cd,N,S]   u0 {1,S} {3,S} {6,D}
3   [Cs,N,O,S] u0 {2,S} {4,S}
4   [Cs,N,O,S] u0 {1,S} {3,S}
5   [Cd,N,O,S] u0 {1,D}
6   [Cd,N,O,S] u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.313,-4.605,-4.416,-3.887,-3.024,-2.355,-1.276],'cal/(mol*K)'),
        H298 = (28.04,'kcal/mol'),
        S298 = (31.4877,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 310,
    label = "O2s-Cs-O2s-Cs(Br)(Br)",
    group = 
"""
1 * Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2   O2s  u0 p2 c0 {1,S} {4,S}
3   O2s  u0 p2 c0 {1,S} {4,S}
4   Cs   u0 p0 c0 {2,S} {3,S}
5   Br1s u0 p3 c0 {1,S}
6   Br1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 311,
    label = "Cs-O2s-Cs(Br)-O2s",
    group = 
"""
1 * Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2   O2s  u0 p2 c0 {1,S} {4,S}
3   O2s  u0 p2 c0 {1,S} {4,S}
4   Cs   u0 p0 c0 {2,S} {3,S}
5   Br1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 312,
    label = "O2s-Cs-O2s-Cs(Cl)(Cl)",
    group = 
"""
1 * Cs   u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2   O2s  u0 p2 c0 {1,S} {4,S}
3   O2s  u0 p2 c0 {1,S} {4,S}
4   Cs   u0 p0 c0 {2,S} {3,S}
5   Cl1s u0 p3 c0 {1,S}
6   Cl1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 313,
    label = "Cs-O2s-Cs(Cl)-O2s",
    group = 
"""
1 * Cs   u0 p0 c0 {2,S} {3,S} {5,S}
2   O2s  u0 p2 c0 {1,S} {4,S}
3   O2s  u0 p2 c0 {1,S} {4,S}
4   Cs   u0 p0 c0 {2,S} {3,S}
5   Cl1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 314,
    label = "O2s-Cs-O2s-Cs(F)",
    group = 
"""
1 * Cs  u0 p0 c0 {2,S} {3,S} {5,S}
2   O2s u0 p2 c0 {1,S} {4,S}
3   O2s u0 p2 c0 {1,S} {4,S}
4   Cs  u0 p0 c0 {2,S} {3,S}
5   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 315,
    label = "Cs-O2s-Cs(F)(F)-O2s",
    group = 
"""
1 * Cs  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2   O2s u0 p2 c0 {1,S} {4,S}
3   O2s u0 p2 c0 {1,S} {4,S}
4   Cs  u0 p0 c0 {2,S} {3,S}
5   F1s u0 p3 c0 {1,S}
6   F1s u0 p3 c0 {1,S}
""",
    thermo = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 316,
    label = "FiveMember",
    group = 
"""
1 * R!H u0 {2,[S,D,T]} {5,[S,D]}
2   R!H u0 {1,[S,D,T]} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,[S,D]}
4   R!H u0 {3,[S,D]} {5,[S,D,T]}
5   R!H u0 {1,[S,D]} {4,[S,D,T]}
""",
    thermo = 'Cyclopentane',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 317,
    label = "Cyclopentane",
    group = 
"""
1 * Cs u0 {2,S} {5,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.5,-5.5,-4.5,-3.8,-2.8,-1.93,-0.37],'cal/(mol*K)'),
        H298 = (6.3,'kcal/mol'),
        S298 = (27.3,'cal/(mol*K)'),
    ),
    shortDesc = """Cyclopentane ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 318,
    label = "Cyclopentene",
    group = 
"""
1   [Cs,N] u0 {2,S} {5,S}
2   [Cd,N] u0 {1,S} {3,D}
3   [Cd,N] u0 {2,D} {4,S}
4   [Cs,N] u0 {3,S} {5,S}
5 * [Cs,N] u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.5,-3.942,-3.291,-2.759,-2.08,-1.628,-0.898],'cal/(mol*K)'),
        H298 = (5.97,'kcal/mol'),
        S298 = (25.8284,'cal/(mol*K)'),
    ),
    shortDesc = """Cyclopentene ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 319,
    label = "Cyclopentadiene",
    group = 
"""
1 * [Cs,N]     u0 {2,S} {5,S}
2   [Cd,N,O,S] u0 {1,S} {3,D}
3   [Cd,N,O,S] u0 {2,D} {4,S}
4   [Cd,N,O,S] u0 {3,S} {5,D}
5   [Cd,N,O,S] u0 {1,S} {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.7845,-3.72708,-3.2688,-2.74383,-2.05359,-1.65464,-0.98756],'cal/(mol*K)'),
        H298 = (6.05,'kcal/mol'),
        S298 = (27.9821,'cal/(mol*K)'),
    ),
    shortDesc = """Cyclopentadiene ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 320,
    label = "five-inringtwodouble-12",
    group = 
"""
1 * R!H u0 {2,[S,D]} {5,S}
2   R!H u0 {1,[S,D]} {3,D}
3   Cdd u0 {2,D} {4,D}
4   R!H u0 {3,D} {5,[S,D]}
5   R!H u0 {1,S} {4,[S,D]}
""",
    thermo = '1,2-Cyclopentadiene',
    shortDesc = """""",
    longDesc = 
"""
For now, any 5-membered ring that has at least 2 double-bonds in the 1,2 positions will use this general correction.
""",
)

entry(
    index = 321,
    label = "1,2-Cyclopentadiene",
    group = 
"""
1 * C   u0 {2,S} {5,S}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {2,D} {4,D}
4   Cd  u0 {3,D} {5,S}
5   C   u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.61023,-3.22037,-2.91832,-2.86073,-2.50323,-1.66978,-1.31002],'cal/(mol*K)'),
        H298 = (65.8534,'kcal/mol'),
        S298 = (26.7523,'cal/(mol*K)'),
    ),
    shortDesc = """Fitted to M06 calculation""",
    longDesc = 
"""

""",
)

entry(
    index = 322,
    label = "five-inringthreedouble-124",
    group = 
"""
1 * R!H       u0 {2,D} {5,[S,D]}
2   [Cdd,N,S] u0 {1,D} {3,D}
3   R!H       u0 {2,D} {4,[S,D]}
4   R!H       u0 {3,[S,D]} {5,D}
5   R!H       u0 {1,[S,D]} {4,D}
""",
    thermo = 'Cyclopentatriene',
    shortDesc = """""",
    longDesc = 
"""
For now, any 5-membered ring that has at least 3 double-bonds in the 1,2,4 positions will use this general correction.
""",
)

entry(
    index = 323,
    label = "Cyclopentatriene",
    group = 
"""
1 * Cd  u0 {2,D} {5,S}
2   Cdd u0 {1,D} {3,D}
3   Cd  u0 {2,D} {4,S}
4   Cd  u0 {3,S} {5,D}
5   Cd  u0 {1,S} {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.08,-4.69,-4.58,-4.25,-3.54,-3.08,-2.47],'cal/(mol*K)'),
        H298 = (70.16,'kcal/mol'),
        S298 = (36.76,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 isodesmic reaction approach allene + 2-butene = cyclopentatriene + 2 CH4, DHr = 220.8 kJ mol-1, exp data from NIST""",
    longDesc = 
"""

""",
)

entry(
    index = 324,
    label = "five-inringonetriple",
    group = 
"""
1 * R!H u0 {2,T} {5,S}
2   R!H u0 {1,T} {3,S}
3   R!H u0 {2,S} {4,[S,D]}
4   R!H u0 {3,[S,D]} {5,[S,D,T]}
5   R!H u0 {1,S} {4,[S,D,T]}
""",
    thermo = 'Cyclopentyne',
    shortDesc = """""",
    longDesc = 
"""
Use cyclopentyne ring correction for any five-membered ring containing a triple bond.
""",
)

entry(
    index = 325,
    label = "Cyclopentyne",
    group = 
"""
1 * Ct u0 {2,T} {5,S}
2   Ct u0 {1,T} {3,S}
3   C  u0 {2,S} {4,S}
4   C  u0 {3,S} {5,S}
5   C  u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.441,-1.573,-1.731,-1.812,-1.511,-1.194,-3.151],'cal/(mol*K)'),
        H298 = (72.047,'kcal/mol'),
        S298 = (28.96,'cal/(mol*K)'),
    ),
    shortDesc = """Fitted to CBS-QB3 calculation""",
    longDesc = 
"""

""",
)

entry(
    index = 326,
    label = "Tetrahydrofuran",
    group = 
"""
1 * O      u0 {2,S} {5,S}
2   [Cs,N] u0 {1,S} {3,S}
3   [Cs,N] u0 {2,S} {4,S}
4   [Cs,N] u0 {3,S} {5,S}
5   [Cs,N] u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.93,-5.71,-4.67,-3.721,-2.689,-1.856,3.213],'cal/(mol*K)'),
        H298 = (5.96,'kcal/mol'),
        S298 = (21.1624,'cal/(mol*K)'),
    ),
    shortDesc = """CY/C4O from THERM (Dorofeeva, 92) Cp1500 est. as Cp1000""",
    longDesc = 
"""

""",
)

entry(
    index = 327,
    label = "2,3-Dihydrofuran",
    group = 
"""
1 * O      u0 {2,S} {5,S}
2   [Cd,N] u0 {1,S} {3,D}
3   [Cd,N] u0 {2,D} {4,S}
4   [Cs,N] u0 {3,S} {5,S}
5   [Cs,N] u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.56,-5.96,-5.695,-5.144,-4.218,-3.708,-0.284],'cal/(mol*K)'),
        H298 = (4.57,'kcal/mol'),
        S298 = (23.83,'cal/(mol*K)'),
    ),
    shortDesc = """2,3-Dihydrofuran ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 328,
    label = "1,3-Dioxolane",
    group = 
"""
1 * [Cs,N] u0 {2,S} {5,S}
2   O      u0 {1,S} {3,S}
3   [Cs,N] u0 {2,S} {4,S}
4   [Cs,N] u0 {3,S} {5,S}
5   O      u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.655,-6.405,-6.306,-6.405,-7.631,-8.27,-3.21],'cal/(mol*K)'),
        H298 = (5.13,'kcal/mol'),
        S298 = (20.4021,'cal/(mol*K)'),
    ),
    shortDesc = """1,3-Dioxolane ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 329,
    label = "Furan",
    group = 
"""
1   [Cd,N] u0 {2,D} {5,S}
2   [Cd,N] u0 {1,D} {3,S}
3   [Cd,N] u0 {2,S} {4,D}
4   [Cd,N] u0 {3,D} {5,S}
5 * O      u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.09,-7.18,-6.79,-5.86,-4.83,-3.71,-2.9],'cal/(mol*K)'),
        H298 = (-6.3,'kcal/mol'),
        S298 = (31.71,'cal/(mol*K)'),
    ),
    shortDesc = """Furan ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 330,
    label = "Dihydro-2,5-furandione",
    group = 
"""
1 * O       u0 {2,S} {5,S}
2   [CO,CS] u0 {1,S} {3,S}
3   [Cs,N]  u0 {2,S} {4,S}
4   [Cs,N]  u0 {3,S} {5,S}
5   [CO,CS] u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.235,-4.726,-3.615,-1.82,-1.835,-1.084,1.104],'cal/(mol*K)'),
        H298 = (1.4,'kcal/mol'),
        S298 = (37.7647,'cal/(mol*K)'),
    ),
    shortDesc = """Dihydro-2,5-furandione ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 331,
    label = "2,5-Furandione",
    group = 
"""
1 * O       u0 {2,S} {5,S}
2   [CO,CS] u0 {1,S} {3,S}
3   [Cd,N]  u0 {2,S} {4,D}
4   [Cd,N]  u0 {3,D} {5,S}
5   [CO,CS] u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (3.6,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """2,5-Furandione ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 332,
    label = "Cyclopentanone",
    group = 
"""
1 * [CO,CS] u0 {2,S} {5,S}
2   [Cs,N]  u0 {1,S} {3,S}
3   [Cs,N]  u0 {2,S} {4,S}
4   [Cs,N]  u0 {3,S} {5,S}
5   [Cs,N]  u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.06,-4.927,-3.392,-2.097,-1.093,-0.322,1.29],'cal/(mol*K)'),
        H298 = (4.47,'kcal/mol'),
        S298 = (24.6287,'cal/(mol*K)'),
    ),
    shortDesc = """Cyclopentanone ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 333,
    label = "butyrolactone",
    group = 
"""
1 * [CO,CS] u0 {2,S} {5,S}
2   O2s     u0 {1,S} {3,S}
3   [Cs,N]  u0 {2,S} {4,S}
4   [Cs,N]  u0 {3,S} {5,S}
5   [Cs,N]  u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.836,-5.134,-4.114,-3.222,-2.341,-1.822,1.888],'cal/(mol*K)'),
        H298 = (7.92,'kcal/mol'),
        S298 = (27.4547,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 334,
    label = "25dihydrofuran",
    group = 
"""
1 * [Cs,N] u0 {2,S} {5,S}
2   [Cd,N] u0 {1,S} {3,D}
3   [Cd,N] u0 {2,D} {4,S}
4   [Cs,N] u0 {3,S} {5,S}
5   O2s    u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.946,-3.361,-2.438,-1.799,-1.458,-1.056,-0.254],'cal/(mol*K)'),
        H298 = (4.23674,'kcal/mol'),
        S298 = (25.1504,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 335,
    label = "12dioxolane",
    group = 
"""
1 * O2s    u0 {2,S} {5,S}
2   [Cs,N] u0 {1,S} {3,S}
3   [Cs,N] u0 {2,S} {4,S}
4   [Cs,N] u0 {3,S} {5,S}
5   O2s    u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.95,-4.859,-4.265,-3.679,-3.089,-3.091,1.915],'cal/(mol*K)'),
        H298 = (6.05383,'kcal/mol'),
        S298 = (25.0554,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 336,
    label = "12dioxolene",
    group = 
"""
1 * O2s    u0 {2,S} {5,S}
2   [Cd,N] u0 {1,S} {3,D}
3   [Cd,N] u0 {2,D} {4,S}
4   [Cs,N] u0 {3,S} {5,S}
5   O2s    u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.159,-4.213,-3.754,-3.376,-3.14,-2.919,-1.982],'cal/(mol*K)'),
        H298 = (4.56853,'kcal/mol'),
        S298 = (29.97,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 337,
    label = "123trioxolane",
    group = 
"""
1 * O2s    u0 {2,S} {5,S}
2   O2s    u0 {1,S} {3,S}
3   [Cs,N] u0 {2,S} {4,S}
4   [Cs,N] u0 {3,S} {5,S}
5   O2s    u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.566,-3.543,-3.344,-2.829,-2.487,-2.78,2.13],'cal/(mol*K)'),
        H298 = (10.1971,'kcal/mol'),
        S298 = (23.316,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 338,
    label = "124trioxolane",
    group = 
"""
1 * O2s    u0 {2,S} {5,S}
2   [Cs,N] u0 {1,S} {3,S}
3   O2s    u0 {2,S} {4,S}
4   [Cs,N] u0 {3,S} {5,S}
5   O2s    u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.648,-4.764,-3.63,-2.89,-2.711,-2.859,2.25],'cal/(mol*K)'),
        H298 = (9.45319,'kcal/mol'),
        S298 = (25.1104,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 339,
    label = "thiolane",
    group = 
"""
1 * S     u0 {2,S} {5,S}
2   [C,N] u0 {1,S} {3,S}
3   [C,N] u0 {2,S} {4,S}
4   [C,N] u0 {3,S} {5,S}
5   [C,N] u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.61,-4.54,-3.51,-2.63,-1.49,-0.73,0.32],'cal/(mol*K)'),
        H298 = (2.02,'kcal/mol'),
        S298 = (20.68,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
"""

""",
)

entry(
    index = 340,
    label = "2,3-dihydrothiophene",
    group = 
"""
1 * S      u0 {2,S} {5,S}
2   [Cd,N] u0 {1,S} {3,D}
3   [Cd,N] u0 {2,D} {4,S}
4   [C,N]  u0 {3,S} {5,S}
5   [C,N]  u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.58,-4.63,-3.67,-2.89,-1.9,-1.26,-0.41],'cal/(mol*K)'),
        H298 = (3.37,'kcal/mol'),
        S298 = (24.24,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
"""

""",
)

entry(
    index = 341,
    label = "2,5-dihydrothiophene",
    group = 
"""
1 * S      u0 {2,S} {5,S}
2   [C,N]  u0 {1,S} {3,S}
3   [Cd,N] u0 {2,S} {4,D}
4   [Cd,N] u0 {3,D} {5,S}
5   [C,N]  u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10.84,-9.28,-7.17,-5.42,-3.18,-1.97,-0.74],'cal/(mol*K)'),
        H298 = (2.19,'kcal/mol'),
        S298 = (28.23,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
"""

""",
)

entry(
    index = 342,
    label = "thiophene",
    group = 
"""
1 * S      u0 {2,S} {5,S}
2   [Cd,N] u0 {1,S} {3,D}
3   [Cd,N] u0 {2,D} {4,S}
4   [Cd,N] u0 {3,S} {5,D}
5   [Cd,N] u0 {1,S} {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.15,-3.75,-2.7,-2.03,-1.45,-1.14,-0.76],'cal/(mol*K)'),
        H298 = (-17.22,'kcal/mol'),
        S298 = (23.78,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
"""

""",
)

entry(
    index = 343,
    label = "1,2-dithiolane",
    group = 
"""
1 * S     u0 {2,S} {5,S}
2   S     u0 {1,S} {3,S}
3   [C,N] u0 {2,S} {4,S}
4   [C,N] u0 {3,S} {5,S}
5   [C,N] u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.15,-6.27,-7.52,-8.83,-11.39,-13.48,-16.94],'cal/(mol*K)'),
        H298 = (23.29,'kcal/mol'),
        S298 = (23.78,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
"""

""",
)

entry(
    index = 344,
    label = "1,3-dithiolane",
    group = 
"""
1 * S     u0 {2,S} {5,S}
2   [C,N] u0 {1,S} {3,S}
3   S     u0 {2,S} {4,S}
4   [C,N] u0 {3,S} {5,S}
5   [C,N] u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.45,-6.68,-4.91,-3.49,-1.72,-0.7,0.45],'cal/(mol*K)'),
        H298 = (0.48,'kcal/mol'),
        S298 = (22.84,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
"""

""",
)

entry(
    index = 345,
    label = "1,2,3-trithiolane",
    group = 
"""
1 * S     u0 {2,S} {5,S}
2   S     u0 {1,S} {3,S}
3   S     u0 {2,S} {4,S}
4   [C,N] u0 {3,S} {5,S}
5   [C,N] u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.51,-4.63,-3.98,-3.49,-2.82,-2.2,-0.88],'cal/(mol*K)'),
        H298 = (9.12,'kcal/mol'),
        S298 = (22.01,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
"""

""",
)

entry(
    index = 346,
    label = "1,2,4-trithiolane",
    group = 
"""
1 * S     u0 {2,S} {5,S}
2   S     u0 {1,S} {3,S}
3   [C,N] u0 {2,S} {4,S}
4   S     u0 {3,S} {5,S}
5   [C,N] u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-11.78,-9.58,-7.37,-5.67,-3.5,-2.26,-0.71],'cal/(mol*K)'),
        H298 = (4.4,'kcal/mol'),
        S298 = (24.39,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
"""

""",
)

entry(
    index = 347,
    label = "tetrathiolane",
    group = 
"""
1 * S     u0 {2,S} {5,S}
2   S     u0 {1,S} {3,S}
3   S     u0 {2,S} {4,S}
4   S     u0 {3,S} {5,S}
5   [C,N] u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.82,-8.46,-7.22,-6.33,-5.17,-4.28,-2.4],'cal/(mol*K)'),
        H298 = (10.72,'kcal/mol'),
        S298 = (26.56,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
"""

""",
)

entry(
    index = 348,
    label = "pentathiolane",
    group = 
"""
1 * S u0 {2,S} {5,S}
2   S u0 {1,S} {3,S}
3   S u0 {2,S} {4,S}
4   S u0 {3,S} {5,S}
5   S u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.87,-8.3,-7.89,-7.72,-7.45,-6.84,-4.46],'cal/(mol*K)'),
        H298 = (10.99,'kcal/mol'),
        S298 = (30.31,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 GA 1D-HR Aaron Vandeputte 2009, dH from NIST-JANAF""",
    longDesc = 
"""

""",
)

entry(
    index = 349,
    label = "Pyrrolidine",
    group = 
"""
1 * N      u0 {2,S} {5,S}
2   [Cs,N] u0 {1,S} {3,S}
3   [Cs,N] u0 {2,S} {4,S}
4   [Cs,N] u0 {3,S} {5,S}
5   [Cs,N] u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.17,-5.58,-4.8,-4,-2.87,-2.17,0],'cal/(mol*K)'),
        H298 = (6.8,'kcal/mol'),
        S298 = (26.7,'cal/(mol*K)'),
    ),
    shortDesc = """Pyrrolidine ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 350,
    label = "methylenecyclopentane",
    group = 
"""
1 * Cd     u0 {2,S} {5,S} {6,D}
2   [Cs,N] u0 {1,S} {3,S}
3   [Cs,N] u0 {2,S} {4,S}
4   [Cs,N] u0 {3,S} {5,S}
5   [Cs,N] u0 {1,S} {4,S}
6   [Cd,N] u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.861,-4.909,-3.91,-3.01,-1.769,-0.969,0],'cal/(mol*K)'),
        H298 = (5.21,'kcal/mol'),
        S298 = (24.6287,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 351,
    label = "Fulvene",
    group = 
"""
1 * Cd     u0 {2,S} {5,S} {6,D}
2   [Cd,N] u0 {1,S} {3,D}
3   [Cd,N] u0 {2,D} {4,S}
4   [Cd,N] u0 {3,S} {5,D}
5   [Cd,N] u0 {1,S} {4,D}
6   [Cd,N] u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.376,-3.662,-3.634,-3.412,-3.209,-2.823,-2.737],'cal/(mol*K)'),
        H298 = (9.06,'kcal/mol'),
        S298 = (33.947,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3""",
    longDesc = 
"""
Fit to CBS-QB3 calculations of fulvene thermo in vinylCPD_H and Fulvene_H libraries
""",
)

entry(
    index = 352,
    label = "3-Methylenecyclopentene",
    group = 
"""
1 * [Cs,N] u0 {2,S} {3,S}
2   [Cs,N] u0 {1,S} {4,S}
3   Cd     u0 {1,S} {5,S} {6,D}
4   [Cd,N] u0 {2,S} {5,D}
5   [Cd,N] u0 {3,S} {4,D}
6   [Cd,N] u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.9,-4.8,-4.4,-3.7,-2.7,-2,-0.9],'cal/(mol*K)'),
        H298 = (6.2,'kcal/mol'),
        S298 = (28.9,'cal/(mol*K)'),
    ),
    shortDesc = """Copied from 4-methylenecyclopentene""",
    longDesc = 
"""

""",
)

entry(
    index = 353,
    label = "4-Methylenecyclopentene",
    group = 
"""
1 * [Cs,N] u0 {3,S} {4,S}
2   [Cs,N] u0 {3,S} {5,S}
3   Cd     u0 {1,S} {2,S} {6,D}
4   [Cd,N] u0 {1,S} {5,D}
5   [Cd,N] u0 {2,S} {4,D}
6   [Cd,N] u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.9,-4.8,-4.4,-3.7,-2.7,-2,-0.9],'cal/(mol*K)'),
        H298 = (6.2,'kcal/mol'),
        S298 = (28.9,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 354,
    label = "12methylenecyclopentane",
    group = 
"""
1 * Cd     u0 {2,S} {5,S} {6,D}
2   Cd     u0 {1,S} {3,S} {7,D}
3   [Cs,N] u0 {2,S} {4,S}
4   [Cs,N] u0 {3,S} {5,S}
5   [Cs,N] u0 {1,S} {4,S}
6   [Cd,N] u0 {1,D}
7   [Cd,N] u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.844,-5.197,-4.882,-4.175,-2.988,-2.088,-0.655],'cal/(mol*K)'),
        H298 = (6.67,'kcal/mol'),
        S298 = (31.384,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 355,
    label = "SixMember",
    group = 
"""
1 * R!H u0 {2,[S,D,T]} {6,[S,D]}
2   R!H u0 {1,[S,D,T]} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,[S,D,T]}
4   R!H u0 {3,[S,D,T]} {5,[S,D]}
5   R!H u0 {4,[S,D]} {6,[S,D,T]}
6   R!H u0 {1,[S,D]} {5,[S,D,T]}
""",
    thermo = 'Cyclohexane',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 356,
    label = "sixnosidedouble",
    group = 
"""
1 * [Cs,O2s,N,S2s] u0 {2,S} {6,S}
2   [Cs,O2s,N,S2s] u0 {1,S} {3,S}
3   [Cs,O2s,N,S2s] u0 {2,S} {4,S}
4   [Cs,O2s,N,S2s] u0 {3,S} {5,S}
5   [Cs,O2s,N,S2s] u0 {4,S} {6,S}
6   [Cs,O2s,N,S2s] u0 {1,S} {5,S}
""",
    thermo = 'Cyclohexane',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 357,
    label = "Cyclohexane",
    group = 
"""
1 * Cs u0 {2,S} {6,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.8,-4.1,-2.9,-1.3,1.08,2.16,3],'cal/(mol*K)'),
        H298 = (0.08,'kcal/mol'),
        S298 = (18.1277,'cal/(mol*K)'),
    ),
    shortDesc = """Cyclohexane ring BENSON https:""",
    longDesc = 
"""

""",
)

entry(
    index = 358,
    label = "12dioxane",
    group = 
"""
1   Cs  u0 {2,S} {6,S}
2   Cs  u0 {1,S} {3,S}
3   Cs  u0 {2,S} {4,S}
4 * Cs  u0 {3,S} {5,S}
5   O2s u0 {4,S} {6,S}
6   O2s u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.66,-5.11,-4.17,-3.36,-2.52,-2.4,2.76],'cal/(mol*K)'),
        H298 = (3.9,'kcal/mol'),
        S298 = (19.6424,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 359,
    label = "1,3-Dioxane",
    group = 
"""
1   O2s u0 {2,S} {6,S}
2 * Cs  u0 {1,S} {3,S}
3   O2s u0 {2,S} {4,S}
4   Cs  u0 {3,S} {5,S}
5   Cs  u0 {4,S} {6,S}
6   Cs  u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.28,-5.951,-4.458,-3.15,-1.967,-0.83,6.799],'cal/(mol*K)'),
        H298 = (1.88,'kcal/mol'),
        S298 = (16.1924,'cal/(mol*K)'),
    ),
    shortDesc = """1,3-Dioxane ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 360,
    label = "1,4-Dioxane",
    group = 
"""
1   Cs  u0 {2,S} {6,S}
2   Cs  u0 {1,S} {3,S}
3 * O2s u0 {2,S} {4,S}
4   Cs  u0 {3,S} {5,S}
5   Cs  u0 {4,S} {6,S}
6   O2s u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.6,-5,-3.8,-2.6,-1.5,-0.4,8.9],'cal/(mol*K)'),
        H298 = (3.4,'kcal/mol'),
        S298 = (17.8049,'cal/(mol*K)'),
    ),
    shortDesc = """1,4-Dioxane ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 361,
    label = "1,3,5-Trioxane",
    group = 
"""
1   Cs  u0 {2,S} {6,S}
2   O2s u0 {1,S} {3,S}
3   Cs  u0 {2,S} {4,S}
4 * O2s u0 {3,S} {5,S}
5   Cs  u0 {4,S} {6,S}
6   O2s u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.01,-5.719,-3.632,-2.189,-1.525,-0.624,7.031],'cal/(mol*K)'),
        H298 = (4.09,'kcal/mol'),
        S298 = (16.1953,'cal/(mol*K)'),
    ),
    shortDesc = """1,3,5-Trioxane ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 362,
    label = "124trioxane",
    group = 
"""
1   O2s u0 {2,S} {6,S}
2   Cs  u0 {1,S} {3,S}
3   O2s u0 {2,S} {4,S}
4 * Cs  u0 {3,S} {5,S}
5   Cs  u0 {4,S} {6,S}
6   O2s u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.68,-4.07,-2.95,-2.09,-1.73,-1.8,5.2],'cal/(mol*K)'),
        H298 = (3.6,'kcal/mol'),
        S298 = (19.9,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 363,
    label = "123trioxane",
    group = 
"""
1   O2s u0 {2,S} {6,S}
2   O2s u0 {1,S} {3,S}
3   Cs  u0 {2,S} {4,S}
4 * Cs  u0 {3,S} {5,S}
5   Cs  u0 {4,S} {6,S}
6   O2s u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.08,-2.81,-2.55,-1.93,-1.55,-1.9,3.09],'cal/(mol*K)'),
        H298 = (4.87,'kcal/mol'),
        S298 = (17.2,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 364,
    label = "Oxane",
    group = 
"""
1 * Cs  u0 {2,S} {6,S}
2   O2s u0 {1,S} {3,S}
3   Cs  u0 {2,S} {4,S}
4   Cs  u0 {3,S} {5,S}
5   Cs  u0 {4,S} {6,S}
6   Cs  u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6,-5.5,-4.2,-3,-1.6,-0.5,4.9],'cal/(mol*K)'),
        H298 = (0.7,'kcal/mol'),
        S298 = (18.8,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 365,
    label = "hexasulfur",
    group = 
"""
1 * S2s u0 {2,S} {6,S}
2   S2s u0 {1,S} {3,S}
3   S2s u0 {2,S} {4,S}
4   S2s u0 {3,S} {5,S}
5   S2s u0 {4,S} {6,S}
6   S2s u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.61,-0.16,-5.5,-6.91,-8.91,-9.24,-7.14],'cal/(mol*K)'),
        H298 = (6.1,'kcal/mol'),
        S298 = (4.36,'cal/(mol*K)'),
    ),
    shortDesc = """All from NIST-JANAF table""",
    longDesc = 
"""

""",
)

entry(
    index = 366,
    label = "Piperidine",
    group = 
"""
1 * N  u0 {2,S} {6,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.17,-5.58,-4.8,-4,-2.87,-2.17,0],'cal/(mol*K)'),
        H298 = (6.8,'kcal/mol'),
        S298 = (26.7,'cal/(mol*K)'),
    ),
    shortDesc = """Piperidine ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 367,
    label = "six-sidedoubles",
    group = 
"""
1   [C,O]   u0 {2,S} {6,S}
2 * [Cd,CO] u0 {1,S} {3,S}
3   [C,O]   u0 {2,S} {4,S}
4   [C,O]   u0 {3,S} {5,S}
5   [C,O]   u0 {4,S} {6,S}
6   [C,O]   u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10,10,10,10,10,10,0],'cal/(mol*K)'),
        H298 = (10,'kcal/mol'),
        S298 = (10,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 368,
    label = "six-onesidedouble",
    group = 
"""
1   [Cs,O2s] u0 {2,S} {6,S}
2 * [Cd,CO]  u0 {1,S} {3,S}
3   [Cs,O2s] u0 {2,S} {4,S}
4   [Cs,O2s] u0 {3,S} {5,S}
5   [Cs,O2s] u0 {4,S} {6,S}
6   [Cs,O2s] u0 {1,S} {5,S}
""",
    thermo = 'Cyclohexanone',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 369,
    label = "Cyclohexanone",
    group = 
"""
1 * CO u0 {2,S} {6,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.4,-3.9,-2.3,-1,0.1,0.9,0],'cal/(mol*K)'),
        H298 = (1.29,'kcal/mol'),
        S298 = (19.1,'cal/(mol*K)'),
    ),
    shortDesc = """Cyclohexanone ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 370,
    label = "sixmembd-allsingles-twosidedoubles-para",
    group = 
"""
1   [Cs,O2s] u0 {2,S} {6,S}
2 * [Cd,CO]  u0 {1,S} {3,S}
3   [Cs,O2s] u0 {2,S} {4,S}
4   [Cs,O2s] u0 {3,S} {5,S}
5   [Cd,CO]  u0 {4,S} {6,S}
6   [Cs,O2s] u0 {1,S} {5,S}
""",
    thermo = '14methylenecyclohexane',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 371,
    label = "14methylenecyclohexane",
    group = 
"""
1   Cs u0 {2,S} {6,S}
2 * Cd u0 {1,S} {3,S} {7,D}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cd u0 {4,S} {6,S} {8,D}
6   Cs u0 {1,S} {5,S}
7   Cd u0 {2,D}
8   Cd u0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6,-5.349,-4.468,-3.521,-2.203,-1.238,0.384],'cal/(mol*K)'),
        H298 = (1.23,'kcal/mol'),
        S298 = (15.7314,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 372,
    label = "sixmembd-allsingles-twosidedoubles-ortho",
    group = 
"""
1   [Cs,O2s] u0 {2,S} {6,S}
2 * [Cd,CO]  u0 {1,S} {3,S}
3   [Cd,CO]  u0 {2,S} {4,S}
4   [Cs,O2s] u0 {3,S} {5,S}
5   [Cs,O2s] u0 {4,S} {6,S}
6   [Cs,O2s] u0 {1,S} {5,S}
""",
    thermo = 'six-sidedoubles',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 373,
    label = "sixmembd-allsingles-twosidedoubles-meta",
    group = 
"""
1   [Cs,O2s] u0 {2,S} {6,S}
2 * [Cd,CO]  u0 {1,S} {3,S}
3   [Cs,O2s] u0 {2,S} {4,S}
4   [Cd,CO]  u0 {3,S} {5,S}
5   [Cs,O2s] u0 {4,S} {6,S}
6   [Cs,O2s] u0 {1,S} {5,S}
""",
    thermo = 'six-sidedoubles',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 374,
    label = "six-inringonedouble",
    group = 
"""
1   [Cs,O2s] u0 {2,S} {6,S}
2 * Cd       u0 {1,S} {3,D}
3   Cd       u0 {2,D} {4,S}
4   [Cs,O2s] u0 {3,S} {5,S}
5   [Cs,O2s] u0 {4,S} {6,S}
6   [Cs,O2s] u0 {1,S} {5,S}
""",
    thermo = 'Cyclohexene',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 375,
    label = "34dihydro12dioxin",
    group = 
"""
1   O2s u0 {2,S} {6,S}
2   O2s u0 {1,S} {3,S}
3   Cs  u0 {2,S} {4,S}
4   Cs  u0 {3,S} {5,S}
5 * Cd  u0 {4,S} {6,D}
6   Cd  u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.7,-4.9,-4.3,-3.7,-3.11,-2.62,0.62],'cal/(mol*K)'),
        H298 = (1.07,'kcal/mol'),
        S298 = (20.3,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 376,
    label = "36dihydro2hpyran",
    group = 
"""
1 * Cd  u0 {2,S} {6,D}
2   Cs  u0 {1,S} {3,S}
3   Cs  u0 {2,S} {4,S}
4   O2s u0 {3,S} {5,S}
5   Cs  u0 {4,S} {6,S}
6   Cd  u0 {1,D} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.4,-4,-3,-2.2,-1.5,-0.8,2.3],'cal/(mol*K)'),
        H298 = (1.43,'kcal/mol'),
        S298 = (19.2,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 377,
    label = "Cyclohexene",
    group = 
"""
1   Cs u0 {2,S} {6,S}
2   Cs u0 {1,S} {3,S}
3 * Cd u0 {2,S} {4,D}
4   Cd u0 {3,D} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.1,-4.3,-3.3,-2.5,-1.4,-0.7,0.4],'cal/(mol*K)'),
        H298 = (1.17,'kcal/mol'),
        S298 = (21.2114,'cal/(mol*K)'),
    ),
    shortDesc = """Cyclohexene ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 378,
    label = "3,4-Dihydro-2H-pyran",
    group = 
"""
1   O2s u0 {2,S} {6,S}
2   Cs  u0 {1,S} {3,S}
3   Cs  u0 {2,S} {4,S}
4   Cs  u0 {3,S} {5,S}
5 * Cd  u0 {4,S} {6,D}
6   Cd  u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.26,-6.496,-5.96,-5.142,-3.74,-2.915,0.529],'cal/(mol*K)'),
        H298 = (3.94,'kcal/mol'),
        S298 = (22.01,'cal/(mol*K)'),
    ),
    shortDesc = """3,4-Dihydro-2H-pyran ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 379,
    label = "36dihydro12dioxin",
    group = 
"""
1   Cs  u0 {2,S} {6,S}
2 * Cd  u0 {1,S} {3,D}
3   Cd  u0 {2,D} {4,S}
4   Cs  u0 {3,S} {5,S}
5   O2s u0 {4,S} {6,S}
6   O2s u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.45,-4.66,-3.81,-3.16,-2.65,-2.68,-1.53],'cal/(mol*K)'),
        H298 = (3.32,'kcal/mol'),
        S298 = (18.72,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 380,
    label = "24dihydro13dioxin",
    group = 
"""
1   Cd  u0 {2,D} {6,S}
2 * Cd  u0 {1,D} {3,S}
3   Cs  u0 {2,S} {4,S}
4   O2s u0 {3,S} {5,S}
5   Cs  u0 {4,S} {6,S}
6   O2s u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.5,-5.1,-4.2,-3.4,-2.8,-2.3,0.9],'cal/(mol*K)'),
        H298 = (3.1,'kcal/mol'),
        S298 = (20.2,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 381,
    label = "23dihydro14dioxin",
    group = 
"""
1   Cd  u0 {2,D} {6,S}
2 * Cd  u0 {1,D} {3,S}
3   O2s u0 {2,S} {4,S}
4   Cs  u0 {3,S} {5,S}
5   Cs  u0 {4,S} {6,S}
6   O2s u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.3,-7.5,-7.5,-6.9,-5.5,-4.9,0.7],'cal/(mol*K)'),
        H298 = (7.9,'kcal/mol'),
        S298 = (19.3,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 382,
    label = "124trioxene",
    group = 
"""
1   O2s u0 {2,S} {6,S}
2   Cs  u0 {1,S} {3,S}
3   O2s u0 {2,S} {4,S}
4 * Cd  u0 {3,S} {5,D}
5   Cd  u0 {4,D} {6,S}
6   O2s u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.51,-5.86,-5.48,-4.98,-4.44,-4.15,-0.75],'cal/(mol*K)'),
        H298 = (6.98,'kcal/mol'),
        S298 = (24.5,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 383,
    label = "123trioxene",
    group = 
"""
1   O2s u0 {2,S} {6,S}
2   O2s u0 {1,S} {3,S}
3   Cs  u0 {2,S} {4,S}
4 * Cd  u0 {3,S} {5,D}
5   Cd  u0 {4,D} {6,S}
6   O2s u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.73,-2.67,-2.62,-2.27,-2.14,-2.08,-0.97],'cal/(mol*K)'),
        H298 = (4,'kcal/mol'),
        S298 = (21.57,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 384,
    label = "six-inringtwodouble-13",
    group = 
"""
1   [Cs,O2s] u0 {2,S} {6,S}
2 * Cd       u0 {1,S} {3,D}
3   Cd       u0 {2,D} {4,S}
4   Cd       u0 {3,S} {5,D}
5   Cd       u0 {4,D} {6,S}
6   [Cs,O2s] u0 {1,S} {5,S}
""",
    thermo = '1,3-Cyclohexadiene',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 385,
    label = "1,3-Cyclohexadiene",
    group = 
"""
1   Cs u0 {2,S} {6,S}
2   Cs u0 {1,S} {3,S}
3 * Cd u0 {2,S} {4,D}
4   Cd u0 {3,D} {5,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.8,-4.7,-4.2,-3.5,-2.5,-1.8,-0.7],'cal/(mol*K)'),
        H298 = (3.78,'kcal/mol'),
        S298 = (23.9824,'cal/(mol*K)'),
    ),
    shortDesc = """1,3-Cyclohexadiene ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 386,
    label = "six-inringtwodouble-14",
    group = 
"""
1   [Cs,O2s] u0 {2,S} {6,S}
2 * Cd       u0 {1,S} {3,D}
3   Cd       u0 {2,D} {4,S}
4   [Cs,O2s] u0 {3,S} {5,S}
5   Cd       u0 {4,S} {6,D}
6   Cd       u0 {1,S} {5,D}
""",
    thermo = '1,4-Cyclohexadiene',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 387,
    label = "1,4-Cyclohexadiene",
    group = 
"""
1   Cs u0 {2,S} {6,S}
2 * Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.4,-3.2,-2.6,-1.9,-1.2,-0.8,0.2],'cal/(mol*K)'),
        H298 = (0.52,'kcal/mol'),
        S298 = (25.3849,'cal/(mol*K)'),
    ),
    shortDesc = """1,4-Cyclohexadiene ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 388,
    label = "14dioxin",
    group = 
"""
1   Cd  u0 {2,D} {6,S}
2   Cd  u0 {1,D} {3,S}
3   O2s u0 {2,S} {4,S}
4 * Cd  u0 {3,S} {5,D}
5   Cd  u0 {4,D} {6,S}
6   O2s u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.9,-7.5,-7.5,-7.5,-6.8,-5.6,-4.2],'cal/(mol*K)'),
        H298 = (11.71,'kcal/mol','+|-',-2.9),
        S298 = (27.6,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 389,
    label = "six-inringthreedouble_124",
    group = 
"""
1   R!H u0 {2,D} {6,S}
2 * Cdd u0 {1,D} {3,D}
3   R!H u0 {2,D} {4,S}
4   R!H u0 {3,S} {5,[S,D]}
5   R!H u0 {4,[S,D]} {6,D}
6   R!H u0 {1,S} {5,D}
""",
    thermo = '124cyclohexatriene',
    shortDesc = """""",
    longDesc = 
"""
Use 124cyclohexatriene correction for any 6-membered ring that contains at least 3 double bonds in the 1,2 and 4 p
positions.
""",
)

entry(
    index = 390,
    label = "124cyclohexatriene",
    group = 
"""
1   Cd       u0 {2,D} {6,S}
2 * Cdd      u0 {1,D} {3,D}
3   Cd       u0 {2,D} {4,S}
4   [Cs,O2s] u0 {3,S} {5,S}
5   Cd       u0 {4,S} {6,D}
6   Cd       u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.21,-4.32,-3.9,-3.46,-2.71,-2.25,-1.38],'cal/(mol*K)'),
        H298 = (36.04,'kcal/mol'),
        S298 = (26.47,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3 isodesmic reaction approach C1=CC=CCC=1 + 3 ethane + ethene = allene + 2 2-butene + propane""",
    longDesc = 
"""

""",
)

entry(
    index = 391,
    label = "six-inringthreedouble_123",
    group = 
"""
1   Cdd u0 {2,D} {6,D}
2 * Cdd u0 {1,D} {3,D}
3   R!H u0 {2,D} {4,[S,D]}
4   R!H u0 {3,[S,D]} {5,[S,D]}
5   R!H u0 {4,[S,D]} {6,[S,D]}
6   R!H u0 {1,D} {5,[S,D]}
""",
    thermo = '123cyclohexatriene',
    shortDesc = """""",
    longDesc = 
"""
Use 123cyclohexatriene correction for any 6-membered ring that contains at least 3 double bonds in the 1,2 and 3
positions.
""",
)

entry(
    index = 392,
    label = "123cyclohexatriene",
    group = 
"""
1   Cdd u0 {2,D} {6,D}
2 * Cdd u0 {1,D} {3,D}
3   Cd  u0 {2,D} {4,S}
4   Cs  u0 {3,S} {5,S}
5   Cs  u0 {4,S} {6,S}
6   Cd  u0 {1,D} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.033,-4.022,-3.919,-3.755,-3.149,-2.312,-1.645],'cal/(mol*K)'),
        H298 = (50.291,'kcal/mol'),
        S298 = (27.334,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Fitted to M06 calculations
""",
)

entry(
    index = 393,
    label = "six-inringtwodouble-12",
    group = 
"""
1   [Cs,O2s] u0 {2,S} {6,S}
2 * Cd       u0 {1,S} {3,D}
3   C        u0 {2,D} {4,D}
4   Cd       u0 {3,D} {5,S}
5   [Cs,O2s] u0 {4,S} {6,S}
6   [Cs,O2s] u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10,10,10,10,10,10,10],'cal/(mol*K)'),
        H298 = (10,'kcal/mol'),
        S298 = (10,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 394,
    label = "six-oneside-twoindoubles-25",
    group = 
"""
1   [Cs,O2s] u0 {2,S} {6,S}
2   Cd       u0 {1,S} {3,D}
3   Cd       u0 {2,D} {4,S}
4 * [Cd,CO]  u0 {3,S} {5,S}
5   Cd       u0 {4,S} {6,D}
6   Cd       u0 {1,S} {5,D}
""",
    thermo = '14cyclohexadiene3methylene',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 395,
    label = "25cyclohexadienone",
    group = 
"""
1 * CO u0 {2,S} {6,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.4,-3.4,-3.1,-2.6,-2,-1.9,-0.3],'cal/(mol*K)'),
        H298 = (2.9,'kcal/mol'),
        S298 = (25.3,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 396,
    label = "14cyclohexadiene3methylene",
    group = 
"""
1   Cd u0 {2,D} {6,S}
2   Cd u0 {1,D} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6 * Cd u0 {1,S} {5,S} {7,D}
7   Cd u0 {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.71,-2.829,-2.749,-2.625,-2.174,-1.591,-1.484],'cal/(mol*K)','+|-',[0.3481,0.3481,0.3481,0.3481,0.3481,0.3481,0.3481]),
        H298 = (-3.253,'kcal/mol','+|-',2.9353),
        S298 = (26.101,'cal/(mol*K)','+|-',0.5184),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations, 02/2019, Lawrence Lai
Model species is 1,4-cyclohexadiene-3-methylene
""",
)

entry(
    index = 397,
    label = "six-oneside-twoindoubles-24",
    group = 
"""
1   [Cs,O2s] u0 {2,S} {6,S}
2   Cd       u0 {1,S} {3,D}
3   Cd       u0 {2,D} {4,S}
4   Cd       u0 {3,S} {5,D}
5   Cd       u0 {4,D} {6,S}
6 * [Cd,CO]  u0 {1,S} {5,S}
""",
    thermo = '13cyclohexadiene5methylene',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 398,
    label = "24cyclohexadienone",
    group = 
"""
1   Cs u0 {2,S} {6,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6 * CO u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.6,-4.3,-4.4,-4.1,-3.5,-3.3,0.3],'cal/(mol*K)'),
        H298 = (3.3,'kcal/mol'),
        S298 = (29.7,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 399,
    label = "13cyclohexadiene5methylene",
    group = 
"""
1   Cs u0 {2,S} {6,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6 * Cd u0 {1,S} {5,S} {7,D}
7   Cd u0 {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.182,-6.383,-6.343,-5.497,-3.657,-2.381,-1.242],'cal/(mol*K)','+|-',[0.3969,0.3969,0.3969,0.3969,0.3969,0.3969,0.3969]),
        H298 = (5.22,'kcal/mol','+|-',3.016),
        S298 = (27.698,'cal/(mol*K)','+|-',0.5184),
    ),
    shortDesc = """Calculations from Hexylbenzene Library, Lawrence Lai""",
    longDesc = 
"""
"
Based on CBS-QB3 calculations, 02/2019, Lawrence Lai
Model species is 1,3-cyclohexadiene-5-methylene
""",
)

entry(
    index = 400,
    label = "six-twoin13-twoout",
    group = 
"""
1   [CO,Cd] u0 {2,S} {6,S}
2   Cd      u0 {1,S} {3,D}
3   Cd      u0 {2,D} {4,S}
4   Cd      u0 {3,S} {5,D}
5   Cd      u0 {4,D} {6,S}
6 * [Cd,CO] u0 {1,S} {5,S}
""",
    thermo = 'oxylene',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 401,
    label = "fg6",
    group = 
"""
1 * CO u0 {2,S} {6,S}
2   Cd u0 {1,S} {3,S} {7,D}
3   Cd u0 {2,S} {4,D}
4   Cd u0 {3,D} {5,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {1,S} {5,D}
7   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.597,-6.43,-6.331,-5.573,-4.198,-3.361,-1.155],'cal/(mol*K)'),
        H298 = (-4.62,'kcal/mol'),
        S298 = (28.901,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 402,
    label = "oxylene",
    group = 
"""
1 * Cd u0 {5,S} {6,S} {8,D}
2   Cd u0 {3,D} {6,S}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {1,S} {4,D}
6   Cd u0 {1,S} {2,S} {7,D}
7   Cd u0 {6,D}
8   Cd u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.078,-2.192,-2.249,-2.275,-2.541,-2.331,-2.797],'cal/(mol*K)'),
        H298 = (4.16,'kcal/mol'),
        S298 = (32.519,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 403,
    label = "obenzoquinone",
    group = 
"""
1 * CO u0 {5,S} {6,S}
2   Cd u0 {3,D} {6,S}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {1,S} {4,D}
6   CO u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.887,-3.225,-3.233,-2.897,-2.4,-2.365,-0.077],'cal/(mol*K)'),
        H298 = (11,'kcal/mol'),
        S298 = (25.331,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 404,
    label = "six-twoin14-twoout",
    group = 
"""
1   [Cd,CO] u0 {2,S} {6,S}
2   Cd      u0 {1,S} {3,D}
3   Cd      u0 {2,D} {4,S}
4 * [Cd,CO] u0 {3,S} {5,S}
5   Cd      u0 {4,S} {6,D}
6   Cd      u0 {1,S} {5,D}
""",
    thermo = 'pxylene',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 405,
    label = "pbenzoquinone",
    group = 
"""
1 * CO u0 {4,S} {5,S}
2   Cd u0 {5,D} {6,S}
3   Cd u0 {4,D} {6,S}
4   Cd u0 {1,S} {3,D}
5   Cd u0 {1,S} {2,D}
6   CO u0 {2,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.957,-3.282,-3.278,-2.934,-2.427,-2.627,-0.312],'cal/(mol*K)'),
        H298 = (15.52,'kcal/mol'),
        S298 = (24.9239,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 406,
    label = "pxylene",
    group = 
"""
1 * Cd u0 {4,S} {5,S} {6,D}
2   Cd u0 {5,D} {7,S}
3   Cd u0 {4,D} {7,S}
4   Cd u0 {1,S} {3,D}
5   Cd u0 {1,S} {2,D}
6   Cd u0 {1,D}
7   Cd u0 {2,S} {3,S} {8,D}
8   Cd u0 {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.139,-2.309,-2.384,-2.407,-2.643,-2.403,-2.826],'cal/(mol*K)'),
        H298 = (1.16,'kcal/mol'),
        S298 = (31.3499,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 407,
    label = "3,4-dimethylenecyclohexene",
    group = 
"""
1 * C  u0 {2,S} {3,S}
2   C  u0 {1,S} {5,S}
3   Cd u0 {1,S} {4,S} {7,D}
4   Cd u0 {3,S} {6,S} {8,D}
5   Cd u0 {2,S} {6,D}
6   Cd u0 {4,S} {5,D}
7   Cd u0 {3,D}
8   Cd u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.1,-2.2,-2.2,-2.3,-2.5,-2.3,-0.3],'cal/(mol*K)'),
        H298 = (4.2,'kcal/mol'),
        S298 = (32.5,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 408,
    label = "six-inringonetriple",
    group = 
"""
1 * Ct  u0 {2,T} {6,S}
2   Ct  u0 {1,T} {3,S}
3   R!H u0 {2,S} {4,S}
4   R!H u0 {3,S} {5,S}
5   R!H u0 {4,S} {6,S}
6   R!H u0 {1,S} {5,S}
""",
    thermo = 'cyclohexyne',
    shortDesc = """""",
    longDesc = 
"""
Use cyclohexyne correction for any 6-membered ring containing 1 triple bond
""",
)

entry(
    index = 409,
    label = "cyclohexyne",
    group = 
"""
1 * Ct      u0 {2,T} {6,S}
2   Ct      u0 {1,T} {3,S}
3   [C,O2s] u0 {2,S} {4,S}
4   [C,O2s] u0 {3,S} {5,S}
5   [C,O2s] u0 {4,S} {6,S}
6   [C,O2s] u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.306,-2.849,-2.452,-2.229,-1.543,-0.932,-2.535],'cal/(mol*K)'),
        H298 = (39.857,'kcal/mol'),
        S298 = (21.862,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3""",
    longDesc = 
"""
Fitted to CBS-QB3 calculation for cyclohexyne
""",
)

entry(
    index = 410,
    label = "six-inringonetripleonedouble-13",
    group = 
"""
1 * Ct  u0 {2,T} {6,S}
2   Ct  u0 {1,T} {3,S}
3   R!H u0 {2,S} {4,D}
4   R!H u0 {3,D} {5,S}
5   R!H u0 {4,S} {6,[S,D]}
6   R!H u0 {1,S} {5,[S,D]}
""",
    thermo = 'cyclohex_1_yne_3_ene',
    shortDesc = """""",
    longDesc = 
"""
Use cyclohex_1_yne_3_ene correction for any 6-membered ring containing at least one triple bond
and one double bond in the 1,3-positions.
""",
)

entry(
    index = 411,
    label = "cyclohex_1_yne_3_ene",
    group = 
"""
1 * Ct      u0 {2,T} {6,S}
2   Ct      u0 {1,T} {3,S}
3   Cd      u0 {2,S} {4,D}
4   Cd      u0 {3,D} {5,S}
5   [C,O2s] u0 {4,S} {6,S}
6   [C,O2s] u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.292,-2.038,-2.856,-3.187,-2.814,-1.639,-2.564],'cal/(mol*K)'),
        H298 = (48.034,'kcal/mol'),
        S298 = (25.6327,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3""",
    longDesc = 
"""
Fitted to CBS-QB3 calculation for cyclohex_1_yne_3_ene
""",
)

entry(
    index = 412,
    label = "o_benzyne",
    group = 
"""
1 * Ct u0 {2,T} {6,S}
2   Ct u0 {1,T} {3,S}
3   Cd u0 {2,S} {4,D}
4   Cd u0 {3,D} {5,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.003,-4.523,-5.242,-5.892,-5.423,-3.742,-3.198],'cal/(mol*K)'),
        H298 = (26.527,'kcal/mol'),
        S298 = (29.264,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3""",
    longDesc = 
"""
Fitted to CBS-QB3 calculation for o_benzyne
""",
)

entry(
    index = 413,
    label = "six-inringonetripleonedouble-14",
    group = 
"""
1 * Ct  u0 {2,T} {6,S}
2   Ct  u0 {1,T} {3,S}
3   R!H u0 {2,S} {4,S}
4   R!H u0 {3,S} {5,D}
5   R!H u0 {4,D} {6,S}
6   R!H u0 {1,S} {5,S}
""",
    thermo = 'cyclohex_1_yne_4_ene',
    shortDesc = """""",
    longDesc = 
"""
Use cyclohex_1_yne_4_ene correction for any 6-membered ring containing at least one triple bond
and one double bond in the 1,4-positions.
""",
)

entry(
    index = 414,
    label = "cyclohex_1_yne_4_ene",
    group = 
"""
1 * Ct      u0 {2,T} {6,S}
2   Ct      u0 {1,T} {3,S}
3   [C,O2s] u0 {2,S} {4,S}
4   Cd      u0 {3,S} {5,D}
5   Cd      u0 {4,D} {6,S}
6   [C,O2s] u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.431,-0.775,-1.308,-1.515,-1.294,-0.369,-1.036],'cal/(mol*K)'),
        H298 = (38.484,'kcal/mol'),
        S298 = (25.2137,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3""",
    longDesc = 
"""
Fitted to CBS-QB3 calculation for cyclohex_1_yne_4_ene
""",
)

entry(
    index = 415,
    label = "six-inringonetripletwodouble-134",
    group = 
"""
1 * Ct  u0 {2,T} {6,S}
2   Ct  u0 {1,T} {3,S}
3   R!H u0 {2,S} {4,D}
4   R!H u0 {3,D} {5,D}
5   R!H u0 {4,D} {6,S}
6   R!H u0 {1,S} {5,S}
""",
    thermo = 'cyclohex_1_yne_3_ene',
    shortDesc = """""",
    longDesc = 
"""
Use cyclohex_1_yne_3_ene correction for any 6-membered ring containing at least one triple bond
and two double bonds in the 1,3,4-positions.
""",
)

entry(
    index = 416,
    label = "six-inringonetriplethreedouble-1345",
    group = 
"""
1 * Ct  u0 {2,T} {6,S}
2   Ct  u0 {1,T} {3,S}
3   R!H u0 {2,S} {4,D}
4   R!H u0 {3,D} {5,D}
5   R!H u0 {4,D} {6,D}
6   R!H u0 {1,S} {5,D}
""",
    thermo = 'cyclohex_1_yne_3_ene',
    shortDesc = """""",
    longDesc = 
"""
Use cyclohex_1_yne_3_ene correction for any 6-membered ring containing at least one triple bond
and three double bonds in the 1,3,4,5-positions.
""",
)

entry(
    index = 417,
    label = "six-inringtwotriple-13",
    group = 
"""
1 * Ct  u0 {2,T} {6,S}
2   Ct  u0 {1,T} {3,S}
3   Ct  u0 {2,S} {4,T}
4   Ct  u0 {3,T} {5,S}
5   R!H u0 {4,S} {6,[S,D,T]}
6   R!H u0 {1,S} {5,[S,D,T]}
""",
    thermo = '1_3_cyclohexadiyne',
    shortDesc = """CBS-QB3""",
    longDesc = 
"""
Use 1_3_cyclohexadiyne correction for any six-membered  ring with at least two triple bonds
""",
)

entry(
    index = 418,
    label = "1_3_cyclohexadiyne",
    group = 
"""
1 * Ct      u0 {2,T} {6,S}
2   Ct      u0 {1,T} {3,S}
3   Ct      u0 {2,S} {4,T}
4   Ct      u0 {3,T} {5,S}
5   [C,O2s] u0 {4,S} {6,S}
6   [C,O2s] u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.086,-1.458,-1.692,-1.747,-1.465,-1.403,-3.712],'cal/(mol*K)'),
        H298 = (103.484,'kcal/mol'),
        S298 = (31.221,'cal/(mol*K)'),
    ),
    shortDesc = """CBS-QB3""",
    longDesc = 
"""
Fitted to CBS-QB3 calculation for 1_3_cyclohexadiyne
""",
)

entry(
    index = 419,
    label = "SevenMember",
    group = 
"""
1 * R!H u0 {2,[S,D,T]} {7,[S,D]}
2   R!H u0 {1,[S,D,T]} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,[S,D]}
4   R!H u0 {3,[S,D]} {5,[S,D]}
5   R!H u0 {4,[S,D]} {6,[S,D]}
6   R!H u0 {5,[S,D]} {7,[S,D]}
7   R!H u0 {1,[S,D]} {6,[S,D]}
""",
    thermo = 'Cycloheptane',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 420,
    label = "Cycloheptane",
    group = 
"""
1 * Cs u0 {2,S} {7,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cs u0 {1,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.1,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (6.4,'kcal/mol'),
        S298 = (15.9,'cal/(mol*K)'),
    ),
    shortDesc = """Cycloheptane ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 421,
    label = "Cycloheptene",
    group = 
"""
1 * Cs u0 {2,S} {7,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cs u0 {1,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.1,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (5.4,'kcal/mol'),
        S298 = (15.6,'cal/(mol*K)'),
    ),
    shortDesc = """Cycloheptene ring BENSON Cp 300K copied from cycloheptane""",
    longDesc = 
"""

""",
)

entry(
    index = 422,
    label = "1,3-Cycloheptadiene",
    group = 
"""
1 * Cs u0 {2,S} {7,S}
2   Cs u0 {1,S} {3,S}
3   Cd u0 {2,S} {4,D}
4   Cd u0 {3,D} {5,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {5,D} {7,S}
7   Cs u0 {1,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (6.6,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """1,3-Cycloheptadiene ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 423,
    label = "1,3,5-Cycloheptatriene",
    group = 
"""
1 * Cs u0 {2,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cd u0 {5,S} {7,D}
7   Cd u0 {1,S} {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (4.7,'kcal/mol'),
        S298 = (23.7,'cal/(mol*K)'),
    ),
    shortDesc = """1,3,5-Cycloheptatriene ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 424,
    label = "Cycloheptanone",
    group = 
"""
1 * CO u0 {2,S} {7,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cs u0 {1,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (2.3,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """Cycloheptanone ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 425,
    label = "1,4-Cycloheptadiene",
    group = 
"""
1 * C  u0 {2,D} {7,S}
2   Cd u0 {1,D} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cs u0 {1,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.1,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (4.3,'kcal/mol'),
        S298 = (15.9,'cal/(mol*K)'),
    ),
    shortDesc = """Automated Estimation of Ring Strain Energies, Gasteiger, 1978, S, Cp from Cycloheptane""",
    longDesc = 
"""

""",
)

entry(
    index = 426,
    label = "seven-inringtwodouble-12",
    group = 
"""
1 * Cd  u0 {2,D} {7,S}
2   Cdd u0 {1,D} {3,D}
3   Cd  u0 {2,D} {4,S}
4   R!H u0 {3,S} {5,[S,D]}
5   R!H u0 {4,[S,D]} {6,[S,D]}
6   R!H u0 {5,[S,D]} {7,[S,D]}
7   R!H u0 {1,S} {6,[S,D]}
""",
    thermo = '1_2_cycloheptadiene',
    shortDesc = """""",
    longDesc = 
"""
Use 1_2_cycloheptadiene correction for any seven membered ring with at least two double bonds in the 1,2-positions
""",
)

entry(
    index = 427,
    label = "1_2_cycloheptadiene",
    group = 
"""
1 * Cd  u0 {2,D} {7,S}
2   Cdd u0 {1,D} {3,D}
3   Cd  u0 {2,D} {4,S}
4   C   u0 {3,S} {5,S}
5   C   u0 {4,S} {6,S}
6   C   u0 {5,S} {7,S}
7   C   u0 {1,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.058,-4.616,-4.065,-3.549,-2.425,-1.185,-0.012],'cal/(mol*K)'),
        H298 = (19.726,'kcal/mol'),
        S298 = (17.979,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Fitted to CBS-QB3 calculations
""",
)

entry(
    index = 428,
    label = "1,2,4,6-Cycloheptatetraene",
    group = 
"""
1 * Cd  u0 {2,D} {7,S}
2   Cdd u0 {1,D} {3,D}
3   Cd  u0 {2,D} {4,S}
4   Cd  u0 {3,S} {5,D}
5   Cd  u0 {4,D} {6,S}
6   Cd  u0 {5,S} {7,D}
7   Cd  u0 {1,S} {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.6,-7.5,-7.3,-6.5,-4.9,-3.7,-2.2],'cal/(mol*K)'),
        H298 = (23.9,'kcal/mol'),
        S298 = (25.5,'cal/(mol*K)'),
    ),
    shortDesc = """AG Vandeputte""",
    longDesc = 
"""
CBS-QB3 isodesmic reaction approach C7H6 + 4 ethene = allene + 3 butadiene
""",
)

entry(
    index = 429,
    label = "seven-inringthreedouble-123",
    group = 
"""
1 * R!H u0 {2,D} {7,[S,D]}
2   Cdd u0 {1,D} {3,D}
3   Cdd u0 {2,D} {4,D}
4   R!H u0 {3,D} {5,[S,D]}
5   R!H u0 {4,[S,D]} {6,[S,D]}
6   R!H u0 {5,[S,D]} {7,[S,D]}
7   R!H u0 {1,[S,D]} {6,[S,D]}
""",
    thermo = '1_2_3_cycloheptatriene',
    shortDesc = """""",
    longDesc = 
"""
Use 1_2_3_cycloheptatriene correction for any seven membered ring with at least three double bonds in the 1,2 and 3-positions
""",
)

entry(
    index = 430,
    label = "1_2_3_cycloheptatriene",
    group = 
"""
1 * Cd  u0 {2,D} {7,S}
2   Cdd u0 {1,D} {3,D}
3   Cdd u0 {2,D} {4,D}
4   Cd  u0 {3,D} {5,S}
5   C   u0 {4,S} {6,S}
6   C   u0 {5,S} {7,S}
7   C   u0 {1,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.854,-4.544,-4.148,-3.726,-2.801,-1.852,-0.8],'cal/(mol*K)'),
        H298 = (25.76,'kcal/mol'),
        S298 = (22.122,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Fitted to CBS-QB3 calculations
""",
)

entry(
    index = 431,
    label = "seven-inringonetriple",
    group = 
"""
1 * Ct  u0 {2,T} {7,S}
2   Ct  u0 {1,T} {3,S}
3   R!H u0 {2,S} {4,[S,D]}
4   R!H u0 {3,[S,D]} {5,[S,D]}
5   R!H u0 {4,[S,D]} {6,[S,D]}
6   R!H u0 {5,[S,D]} {7,[S,D]}
7   R!H u0 {1,S} {6,[S,D]}
""",
    thermo = 'cycloheptyne',
    shortDesc = """""",
    longDesc = 
"""
Use cycloheptyne correction for any seven membered ring with at least one triple bond
""",
)

entry(
    index = 432,
    label = "cycloheptyne",
    group = 
"""
1 * Ct u0 {2,T} {7,S}
2   Ct u0 {1,T} {3,S}
3   C  u0 {2,S} {4,S}
4   C  u0 {3,S} {5,S}
5   C  u0 {4,S} {6,S}
6   C  u0 {5,S} {7,S}
7   C  u0 {1,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4,-3.568,-3.106,-2.646,-1.582,-0.695,-1.916],'cal/(mol*K)'),
        H298 = (24.448,'kcal/mol'),
        S298 = (17.688,'cal/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Fitted to CBS-QB3 calculations
""",
)

entry(
    index = 433,
    label = "heptasulfur",
    group = 
"""
1 * S2s u0 {2,S} {7,S}
2   S2s u0 {1,S} {3,S}
3   S2s u0 {2,S} {4,S}
4   S2s u0 {3,S} {5,S}
5   S2s u0 {4,S} {6,S}
6   S2s u0 {5,S} {7,S}
7   S2s u0 {1,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.26,-9.91,-9.2,-8.99,-8.5,-7.55,-3.9],'cal/(mol*K)'),
        H298 = (-0.44,'kcal/mol'),
        S298 = (8.52,'cal/(mol*K)'),
    ),
    shortDesc = """All from NIST-JANAF table""",
    longDesc = 
"""

""",
)

entry(
    index = 434,
    label = "oxepane",
    group = 
"""
1 * C   u0 {2,S} {7,S}
2   C   u0 {1,S} {3,S}
3   C   u0 {2,S} {4,S}
4   C   u0 {3,S} {5,S}
5   C   u0 {4,S} {6,S}
6   C   u0 {5,S} {7,S}
7   O2s u0 {1,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.1,-5.33,-3.85,-2.52,-0.92,0.26,5.83],'cal/(mol*K)'),
        H298 = (6.54,'kcal/mol'),
        S298 = (17.14,'cal/(mol*K)'),
    ),
    shortDesc = """Calculation: Mixture of two twist chair formations""",
    longDesc = 
"""

""",
)

entry(
    index = 435,
    label = "EightMember",
    group = 
"""
1 * R!H u0 {2,[S,D]} {8,[S,D]}
2   R!H u0 {1,[S,D]} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,[S,D]}
4   R!H u0 {3,[S,D]} {5,[S,D]}
5   R!H u0 {4,[S,D]} {6,[S,D]}
6   R!H u0 {5,[S,D]} {7,[S,D]}
7   R!H u0 {6,[S,D]} {8,[S,D]}
8   R!H u0 {1,[S,D]} {7,[S,D]}
""",
    thermo = 'Cyclooctane',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 436,
    label = "Cyclooctane",
    group = 
"""
1 * Cs u0 {2,S} {8,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cs u0 {6,S} {8,S}
8   Cs u0 {1,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.8,-7.5,-5.9,-4.5,-2.3,-0.8,1.4],'cal/(mol*K)'),
        H298 = (10.5,'kcal/mol'),
        S298 = (16.63,'cal/(mol*K)'),
    ),
    shortDesc = """Updated AG Vandeputte (good agreement with BENSON correction but explicit for cyclooctane from CBS-QB3 isodesmic reaction and B3LYP/cbsb7 for S and cp, results in perfect agreement with calculations of Dorofeeva et al.)""",
    longDesc = 
"""

""",
)

entry(
    index = 437,
    label = "cis-Cyclooctene",
    group = 
"""
1 * Cd u0 {2,D} {8,S}
2   Cd u0 {1,D} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cs u0 {6,S} {8,S}
8   Cs u0 {1,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.9,-5.8,-4.6,-3.4,-1.8,-0.7,1.2],'cal/(mol*K)'),
        H298 = (6.8,'kcal/mol'),
        S298 = (13.01,'cal/(mol*K)'),
    ),
    shortDesc = """Updated AG Vandeputte (CBS-QB3 isodesmic reaction and B3LYP/cbsb7 for S and cp)""",
    longDesc = 
"""

""",
)

entry(
    index = 438,
    label = "1,3,5-Cyclooctatriene",
    group = 
"""
1 * Cs u0 {2,S} {8,S}
2   Cs u0 {1,S} {3,S}
3   Cd u0 {2,S} {4,D}
4   Cd u0 {3,D} {5,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {5,D} {7,S}
7   Cd u0 {6,S} {8,D}
8   Cd u0 {1,S} {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.9,-4.3,-3.3,-2.5,-1.3,-0.5,1],'cal/(mol*K)'),
        H298 = (8.9,'kcal/mol'),
        S298 = (13.89,'cal/(mol*K)'),
    ),
    shortDesc = """1,3,5-Cyclooctatriene ring BENSON, S and cp from 1,4-cyclooctadiene""",
    longDesc = 
"""

""",
)

entry(
    index = 439,
    label = "Cyclooctatetraene",
    group = 
"""
1 * Cd u0 {2,D} {8,S}
2   Cd u0 {1,D} {3,S}
3   Cd u0 {2,S} {4,D}
4   Cd u0 {3,D} {5,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {5,D} {7,S}
7   Cd u0 {6,S} {8,D}
8   Cd u0 {1,S} {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.9,-4.3,-3.3,-2.5,-1.3,-0.5,1],'cal/(mol*K)'),
        H298 = (17.1,'kcal/mol'),
        S298 = (13.89,'cal/(mol*K)'),
    ),
    shortDesc = """Cyclooctatetraene ring BENSON, S and cp from 1,4-cyclooctadiene""",
    longDesc = 
"""

""",
)

entry(
    index = 440,
    label = "Cyclooctanone",
    group = 
"""
1 * CO u0 {2,S} {8,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cs u0 {6,S} {8,S}
8   Cs u0 {1,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (1.5,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """Cyclooctanone ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 441,
    label = "1,3-cyclooctadiene",
    group = 
"""
1 * Cd u0 {2,D} {8,S}
2   Cd u0 {1,D} {3,S}
3   Cd u0 {2,S} {4,D}
4   Cd u0 {3,D} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cs u0 {6,S} {8,S}
8   Cs u0 {1,S} {7,S}
""",
    thermo = '1,4-cyclooctadiene',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 442,
    label = "1,4-cyclooctadiene",
    group = 
"""
1 * Cd u0 {2,D} {8,S}
2   Cd u0 {1,D} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cs u0 {6,S} {8,S}
8   Cs u0 {1,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.9,-4.3,-3.3,-2.5,-1.3,-0.5,1],'cal/(mol*K)'),
        H298 = (8.2,'kcal/mol'),
        S298 = (13.89,'cal/(mol*K)'),
    ),
    shortDesc = """Updated AG Vandeputte (CBS-QB3 isodesmic reaction and B3LYP/cbsb7 for S and cp)""",
    longDesc = 
"""

""",
)

entry(
    index = 443,
    label = "1,5-cyclooctadiene",
    group = 
"""
1 * Cd u0 {2,D} {8,S}
2   Cd u0 {1,D} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {5,D} {7,S}
7   Cs u0 {6,S} {8,S}
8   Cs u0 {1,S} {7,S}
""",
    thermo = '1,4-cyclooctadiene',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 444,
    label = "octasulfur",
    group = 
"""
1 * S2s u0 {2,S} {8,S}
2   S2s u0 {1,S} {3,S}
3   S2s u0 {2,S} {4,S}
4   S2s u0 {3,S} {5,S}
5   S2s u0 {4,S} {6,S}
6   S2s u0 {5,S} {7,S}
7   S2s u0 {6,S} {8,S}
8   S2s u0 {1,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.56,-10.72,-9.9,-9.63,-9.1,-8.08,-4.19],'cal/(mol*K)'),
        H298 = (-10.14,'kcal/mol'),
        S298 = (2.42,'cal/(mol*K)'),
    ),
    shortDesc = """All from NIST-JANAF table""",
    longDesc = 
"""

""",
)

entry(
    index = 445,
    label = "NineMember",
    group = 
"""
1 * R!H u0 {2,[S,D]} {9,[S,D]}
2   R!H u0 {1,[S,D]} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,[S,D]}
4   R!H u0 {3,[S,D]} {5,[S,D]}
5   R!H u0 {4,[S,D]} {6,[S,D]}
6   R!H u0 {5,[S,D]} {7,[S,D]}
7   R!H u0 {6,[S,D]} {8,[S,D]}
8   R!H u0 {7,[S,D]} {9,[S,D]}
9   R!H u0 {1,[S,D]} {8,[S,D]}
""",
    thermo = 'Cyclononane',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 446,
    label = "Cyclononane",
    group = 
"""
1 * Cs u0 {2,S} {9,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cs u0 {6,S} {8,S}
8   Cs u0 {7,S} {9,S}
9   Cs u0 {1,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (12.8,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """Cyclononane ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 447,
    label = "Cyclononanone",
    group = 
"""
1 * CO u0 {2,S} {9,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cs u0 {6,S} {8,S}
8   Cs u0 {7,S} {9,S}
9   Cs u0 {1,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (4.7,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """Cyclononanone ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 448,
    label = "TenMember",
    group = 
"""
1  * R!H u0 {2,[S,D]} {10,[S,D]}
2    R!H u0 {1,[S,D]} {3,[S,D]}
3    R!H u0 {2,[S,D]} {4,[S,D]}
4    R!H u0 {3,[S,D]} {5,[S,D]}
5    R!H u0 {4,[S,D]} {6,[S,D]}
6    R!H u0 {5,[S,D]} {7,[S,D]}
7    R!H u0 {6,[S,D]} {8,[S,D]}
8    R!H u0 {7,[S,D]} {9,[S,D]}
9    R!H u0 {8,[S,D]} {10,[S,D]}
10   R!H u0 {1,[S,D]} {9,[S,D]}
""",
    thermo = 'Cyclodecane',
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 449,
    label = "Cyclodecane",
    group = 
"""
1  * Cs u0 {2,S} {10,S}
2    Cs u0 {1,S} {3,S}
3    Cs u0 {2,S} {4,S}
4    Cs u0 {3,S} {5,S}
5    Cs u0 {4,S} {6,S}
6    Cs u0 {5,S} {7,S}
7    Cs u0 {6,S} {8,S}
8    Cs u0 {7,S} {9,S}
9    Cs u0 {8,S} {10,S}
10   Cs u0 {1,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (12.6,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """Cyclodecane ring BENSON""",
    longDesc = 
"""

""",
)

entry(
    index = 450,
    label = "Cyclodecanone",
    group = 
"""
1  * CO u0 {2,S} {10,S}
2    Cs u0 {1,S} {3,S}
3    Cs u0 {2,S} {4,S}
4    Cs u0 {3,S} {5,S}
5    Cs u0 {4,S} {6,S}
6    Cs u0 {5,S} {7,S}
7    Cs u0 {6,S} {8,S}
8    Cs u0 {7,S} {9,S}
9    Cs u0 {8,S} {10,S}
10   Cs u0 {1,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (3.6,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = """Cyclodecanone ring BENSON""",
    longDesc = 
"""

""",
)

tree(
"""
L1: Ring
    L2: Aromatic
        L3: Benzene
    L2: ThreeMember
        L3: Cyclopropane
            L4: Cs-Cs-Cs(C-BrBrBr)
            L4: Cs(Br)-Cs-Cs(O2)
                L5: Cs(Br)(Br)-Cs-Cs(O2)
            L4: Cs-Cs-Cs(Br)(C)
            L4: Cs-Cs(C)-Cs(Br)
            L4: Cs(C)-Cs-Cs(Br)(Br)
            L4: Cs-Cs-Cs(Br)
                L5: Cs-Cs-Cs(Br)(Br)
                L5: Cs-Cs(Br)(O2)-Cs
            L4: Cs-Cs-Cs(C-BrBr)
            L4: Cs-Cs(C-Br)-Cs
            L4: Cs-Cs-Cs(C-Cl)
                L5: Cs-Cs(C-ClClCl)-Cs
                L5: Cs(C-ClCl)-Cs-Cs
            L4: Cs(Cl)-Cs-Cs
                L5: Cs-Cs-Cs(Cl)(O2)
                L5: Cs-Cs(C)-Cs(Cl)(Cl)
                L5: Cs(Cl)-Cs-Cs(O2)
                L5: Cs(O2)-Cs-Cs(Cl)(Cl)
                L5: Cs-Cs-Cs(Cl)(C)
                L5: Cs-Cs(Cl)-Cs(C)
                L5: Cs-Cs(Cl)(Cl)-Cs
            L4: Cs-Cs(F)(F)-Cs
                L5: Cs-Cs(F)(F)-Cs(O2)
                L5: Cs(F)(F)-Cs(C)-Cs
            L4: Cs(C)-Cs-Cs(F)
            L4: Cs-Cs(F)(C)-Cs
            L4: Cs(F)-Cs-Cs(O2)
            L4: Cs-Cs(C-FFF)-Cs
            L4: Cs-Cs(F)(O2)-Cs
            L4: Cs(F)-Cs-Cs
            L4: Cs-Cs(C-FF)-Cs
            L4: Cs(C-F)-Cs-Cs
        L3: Cyclopropene
            L4: Cd(O2)-Cs-Cd(Br)
            L4: Cd(C)-Cs-Cd(Br)
            L4: Cd-Cs-Cd(Br)
            L4: Cs-Cd-Cd(C-Cl)
                L5: Cs-Cd-Cd(C-ClClCl)
            L4: Cs-Cd(Cl)-Cd(O2)
            L4: Cs(O2)-Cd-Cd(Cl)
            L4: Cs-Cd(Cl)-Cd(C)
            L4: Cs-Cd(F)-Cd
                L5: Cd-Cd(F)-Cs(O2)
                L5: Cs-Cd(C)-Cd(F)
            L4: Cd-Cs-Cd(C-FF)
            L4: Cd-Cs-Cd(C-F)
        L3: Cyclopropene2
            L4: Cd(C)-Cd-Cs(Br)(Br)
            L4: Cd-Cs(C-BrBr)-Cd
                L5: Cs(C-BrBrBr)-Cd-Cd
            L4: Cd-Cs(C-Br)-Cd
            L4: Cs(C)-Cd(Br)-Cd
            L4: Cd-Cd-Cs(Br)(O2)
            L4: Cd-Cd-Cs(Br)(Br)
                L5: Cd(O2)-Cs(Br)(Br)-Cd
            L4: Cd-Cd-Cs(Br)
                L5: Cs(Br)-Cd(C)-Cd
                L5: Cd-Cd(O2)-Cs(Br)
                L5: Cd-Cd-Cs(Br)(C)
            L4: Cs-Cd-Cd(C-Br)
                L5: Cd-Cs-Cd(C-BrBrBr)
                L5: Cd(C-BrBr)-Cd-Cs
            L4: Cd(C)-Cd(Br)-O2s
            L4: O2s-Cd(C-Br)-Cd
                L5: O2s-Cd-Cd(C-BrBrBr)
            L4: Cd(C-BrBr)-Cd-O2s
            L4: Cs(O2)-Cd-Cd(Br)
            L4: Cd-Cd-Cs(C-ClCl)
                L5: Cd-Cd-Cs(C-ClClCl)
            L4: Cd-Cs-Cd(Cl)
            L4: Cd-Cd(Cl)-Cs(C)
            L4: Cd-Cs(Cl)(C)-Cd
            L4: Cd-Cd-Cs(Cl)
                L5: Cs(Cl)-Cd-Cd(O2)
                    L6: Cd(O2)-Cs(Cl)(Cl)-Cd
                L5: Cs(Cl)(Cl)-Cd-Cd(C)
                L5: Cs(Cl)(Cl)-Cd-Cd
                L5: Cd-Cs(Cl)(O2)-Cd
                L5: Cd-Cd(C)-Cs(Cl)
            L4: Cs-Cd-Cd(C-ClCl)
            L4: O2s-Cd(Cl)-Cd(C)
            L4: Cd(C-ClCl)-Cd-O2s
                L5: Cd-O2s-Cd(C-ClClCl)
            L4: Cs(C-Cl)-Cd-Cd
            L4: Cd-O2s-Cd(C-Cl)
            L4: O2s-Cd-Cd(C-FFF)
            L4: Cd-Cs-Cd(C-FFF)
            L4: Cd-Cs(F)(C)-Cd
            L4: Cd(C)-Cd-Cs(F)
                L5: Cd-Cd(C)-Cs(F)(F)
            L4: Cd-Cs(C-FFF)-Cd
            L4: Cd-Cd-Cs(C-FF)
            L4: Cs(F)(O2)-Cd-Cd
            L4: Cd-O2s-Cd(C-F)
            L4: Cd-Cs(F)-Cd
                L5: Cs(F)(F)-Cd-Cd(O2)
                L5: Cs(F)-Cd-Cd(O2)
                L5: Cd-Cd-Cs(F)(F)
            L4: Cd(C-FF)-Cd-O2s
            L4: Cd-Cd-Cs(C-F)
            L4: Cd-Cd(F)-Cs(C)
            L4: Cd(F)-Cd(O2)-Cs
            L4: Cd(C)-Cd(F)-O2s
        L3: Cyclopropadiene
        L3: Cyclopropadiene2
        L3: Cyclopropyne
        L3: oxirene
        L3: Cyclopropatriene
        L3: Ethylene_oxide
            L4: O2s-Cs(Br)-Cs(O2)
                L5: O2s-Cs(Br)(Br)-Cs(O2)
            L4: O2s-Cs(C)-Cs(Br)(Br)
            L4: O2s-Cs(C-BrBrBr)-Cs
            L4: O2s-Cs(Br)(C)-Cs
            L4: O2s-Cs-Cs(Br)
                L5: O2s-Cs-Cs(Br)(Br)
                L5: Cs(C)-Cs(Br)-O2s
                L5: Cs-Cs(Br)(O2)-O2s
            L4: Cs(C-BrBr)-Cs-O2s
            L4: Cs(C-Br)-Cs-O2s
            L4: Cs(C-Cl)-Cs-O2s
                L5: O2s-Cs-Cs(C-ClClCl)
                L5: O2s-Cs(C-ClCl)-Cs
            L4: Cs-O2s-Cs(Cl)
                L5: Cs(O2)-O2s-Cs(Cl)(Cl)
                L5: Cs-O2s-Cs(Cl)(O2)
                L5: Cs(Cl)-O2s-Cs(O2)
                L5: Cs(Cl)-O2s-Cs(C)
                    L6: Cs(Cl)(Cl)-O2s-Cs(C)
                L5: Cs-O2s-Cs(Cl)(C)
                L5: Cs(Cl)(Cl)-Cs-O2s
            L4: O2s-Cs-Cs(C-FFF)
            L4: Cs(F)(O2)-O2s-Cs
            L4: Cs(O2)-O2s-Cs(F)
                L5: Cs(O2)-Cs(F)(F)-O2s
            L4: O2s-Cs-Cs(F)(F)
                L5: Cs(C)-Cs(F)(F)-O2s
            L4: Cs(F)(C)-Cs-O2s
            L4: O2s-Cs(F)-Cs(C)
            L4: Cs-Cs(F)-O2s
            L4: Cs(C-F)-Cs-O2s
                L5: Cs(C-FF)-Cs-O2s
        L3: dioxirane
            L4: O2s-O2s-Cs(Br)(C)
            L4: Cs(C-BrBr)-O2s-O2s
                L5: Cs(C-BrBrBr)-O2s-O2s
            L4: O2s-Cs(C-Br)-O2s
            L4: O2s-Cs(Br)-O2s
                L5: O2s-O2s-Cs(Br)(Br)
            L4: O2s-Cs(C-ClClCl)-O2s
            L4: O2s-O2s-Cs(C-ClCl)
            L4: O2s-Cs(Cl)(C)-O2s
            L4: Cs(Cl)(Cl)-O2s-O2s
            L4: O2s-O2s-Cs(Cl)
            L4: Cs(C-Cl)-O2s-O2s
            L4: O2s-O2s-Cs(C-F)
                L5: O2s-O2s-Cs(C-FF)
                    L6: Cs(C-FFF)-O2s-O2s
            L4: O2s-O2s-Cs(F)
                L5: O2s-O2s-Cs(F)(C)
                L5: O2s-Cs(F)(F)-O2s
        L3: 2(co)oxirane
            L4: O2s-CO(O2d)-Cs(Br)
                L5: CO(O2d)-O2s-Cs(Br)(Br)
        L3: cyclopropanedione
        L3: cyclopropenone
            L4: Cd(Br)-CO(O2d)-Cd
            L4: Cd-Cd(Cl)-CO(O2d)
            L4: CO(O2d)-Cd-Cd(F)
        L3: thiirane
        L3: dithiirane
        L3: trithiirane
        L3: thiirene
        L3: Ethyleneimine
        L3: Methylene_cyclopropane
            L4: Cs-Cd(Cd)-Cs(Br)(Br)
            L4: Cs-Cd(Cd-BrBr)-Cs
            L4: Cd(Cd-Br)-Cs-Cs
            L4: Cs-Cd(Cd)-Cs(Br)
            L4: Cs-Cd(Cd)-Cs(Cl)
                L5: Cs-Cs(Cl)(Cl)-Cd(Cd)
            L4: Cs-Cd(Cd-ClCl)-Cs
            L4: Cs-Cs-Cd(Cd-Cl)
            L4: Cs-Cs(F)(F)-Cd(Cd)
            L4: Cd(Cd-F)-Cs-Cs
                L5: Cs-Cd(Cd-FF)-Cs
            L4: Cd(Cd)-Cs-Cs(F)
        L3: cyclopropanone
            L4: Cs-CO(O2d)-Cs(Br)(Br)
            L4: Cs-Cs(Br)-CO(O2d)
            L4: Cs-CO(O2d)-Cs(Cl)
                L5: Cs-CO(O2d)-Cs(Cl)(Cl)
            L4: O2s-Cs(Cl)-CO(O2d)
                L5: O2s-CO(O2d)-Cs(Cl)(Cl)
            L4: CO(O2d)-O2s-Cs(F)(F)
            L4: CO(O2d)-Cs-Cs(F)
                L5: Cs(F)(F)-Cs-CO(O2d)
            L4: O2s-CO(O2d)-Cs(F)
        L3: methylenecyclopropene
            L4: Cd(Cd)-Cd-Cd(Br)
            L4: Cd-Cd-Cd(Cd-Br)
                L5: Cd-Cd-Cd(Cd-BrBr)
            L4: Cd(Cd)-Cd(Cl)-Cd
            L4: Cd-Cd-Cd(Cd-ClCl)
            L4: Cd-Cd(Cd-Cl)-Cd
            L4: Cd(F)-Cd-Cd(Cd)
            L4: Cd-Cd-Cd(Cd-F)
                L5: Cd-Cd(Cd-FF)-Cd
        L3: methylenecyclopropanone
        L3: methyleneoxirane
            L4: Cs-O2s-Cd(Cd-BrBr)
            L4: Cs(Br)-O2s-Cd(Cd)
                L5: Cs(Br)(Br)-O2s-Cd(Cd)
            L4: Cd(Cd-Br)-Cs-O2s
            L4: Cd(Cd)-O2s-Cs(Cl)(Cl)
            L4: Cs-Cd(Cd-ClCl)-O2s
            L4: Cs-O2s-Cd(Cd-Cl)
            L4: Cs(Cl)-Cd(Cd)-O2s
            L4: O2s-Cs(F)(F)-Cd(Cd)
            L4: Cd(Cd-F)-Cs-O2s
                L5: O2s-Cs-Cd(Cd-FF)
            L4: Cs(F)-Cd(Cd)-O2s
        L3: 12Methylenecyclopropane
        L3: O2s-O2s-Cd(Cd-Br)
            L4: O2s-O2s-Cd(Cd-BrBr)
        L3: O2s-O2s-Cd(Cd-Cl)
            L4: O2s-Cd(Cd-ClCl)-O2s
        L3: O2s-Cd(Cd-FF)-O2s
        L3: O2s-O2s-Cd(Cd-F)
    L2: FourMember
        L3: Cyclobutane
            L4: Cs-Cs(Br)(Br)-Cs-Cs
            L4: Cs(Br)-Cs-Cs-Cs
            L4: Cs-Cs(Cl)-Cs-Cs
                L5: Cs-Cs(Cl)(Cl)-Cs-Cs
            L4: Cs(F)-Cs-Cs-Cs
                L5: Cs-Cs-Cs(F)(F)-Cs
        L3: 34methylenecyclobutene
        L3: dioxerene
        L3: Oxetene
            L4: Cd-Cd-O2s-Cs(F)
        L3: four-inringonedouble
            L4: Cyclobutene
                L5: Cs(Br)-Cd-Cd-O2s
                    L6: Cd-Cd-Cs(Br)(Br)-O2s
                L5: Cs-Cd-Cd-Cs(Br)
                L5: Cd(Br)-Cd-Cs-O2s
                L5: Cs-Cs(Br)(Br)-Cd-Cd
                L5: Cd(Br)-Cd-O2s-Cs
                L5: Cd(Br)-Cd-Cs-Cs
                L5: O2s-O2s-Cd-Cd(Br)
                L5: Cs-Cd(Cl)-Cd-Cs
                L5: Cd-Cd-O2s-Cs(Cl)
                    L6: Cd-Cs(Cl)(Cl)-O2s-Cd
                L5: Cd(Cl)-O2s-Cs-Cd
                L5: Cs-Cs(Cl)-Cd-Cd
                    L6: Cd-Cs-Cs(Cl)(Cl)-Cd
                L5: Cs-O2s-Cd-Cd(Cl)
                L5: Cd-O2s-O2s-Cd(Cl)
                L5: O2s-Cd-Cd-Cs(F)(F)
                L5: Cs(F)-Cs-Cd-Cd
                    L6: Cd-Cs-Cs(F)(F)-Cd
                L5: Cd(F)-Cd-Cs-Cs
                L5: Cd-Cd(F)-Cs-O2s
                L5: Cs-Cd-Cd(F)-O2s
                L5: Cd-Cd(F)-O2s-O2s
        L3: Oxetane
            L4: Cs-Cs(Br)-Cs-O2s
                L5: O2s-Cs-Cs(Br)(Br)-Cs
            L4: Cs-Cs-Cs(Br)(Br)-O2s
            L4: O2s-Cs(Br)-Cs-Cs
            L4: O2s-Cs(Cl)-Cs-Cs
                L5: O2s-Cs-Cs-Cs(Cl)(Cl)
            L4: O2s-Cs-Cs(Cl)-Cs
                L5: Cs-Cs(Cl)(Cl)-Cs-O2s
            L4: O2s-Cs-Cs-Cs(F)
                L5: Cs-Cs(F)(F)-O2s-Cs
            L4: Cs-O2s-Cs-Cs(F)
                L5: Cs-O2s-Cs-Cs(F)(F)
        L3: Beta-Propiolactone
        L3: Cyclobutanone
        L3: 12dioxetane
            L4: Cs-Cs(Br)-O2s-O2s
                L5: O2s-Cs(Br)(Br)-Cs-O2s
            L4: Cs(Cl)-O2s-O2s-Cs
                L5: O2s-Cs-Cs(Cl)(Cl)-O2s
            L4: Cs-Cs(F)-O2s-O2s
                L5: O2s-Cs(F)(F)-Cs-O2s
        L3: four-inringtwodouble
            L4: cyclobutadiene_13
                L5: Cd-Cd-Cd-Cd(Br)
                L5: Cd-Cd-Cd(Cl)-Cd
                L5: Cd-Cd-Cd-Cd(F)
        L3: cyclobutadiene_12
        L3: thietane
        L3: 1,2-dithietane
        L3: 1,3-dithietane
        L3: trithietane
        L3: tetrathietane
        L3: Azetidine
        L3: 4-Methylene-2-oxetanone
        L3: methylenecyclobutane
        L3: 2methyleneoxetane
        L3: 12methylenecyclobutane
        L3: O2s-Cs-O2s-Cs(Br)(Br)
        L3: Cs-O2s-Cs(Br)-O2s
        L3: O2s-Cs-O2s-Cs(Cl)(Cl)
        L3: Cs-O2s-Cs(Cl)-O2s
        L3: O2s-Cs-O2s-Cs(F)
            L4: Cs-O2s-Cs(F)(F)-O2s
    L2: FiveMember
        L3: Cyclopentane
        L3: Cyclopentene
        L3: Cyclopentadiene
        L3: five-inringtwodouble-12
            L4: 1,2-Cyclopentadiene
        L3: five-inringthreedouble-124
            L4: Cyclopentatriene
        L3: five-inringonetriple
            L4: Cyclopentyne
        L3: Tetrahydrofuran
        L3: 2,3-Dihydrofuran
        L3: 1,3-Dioxolane
        L3: Furan
        L3: Dihydro-2,5-furandione
        L3: 2,5-Furandione
        L3: Cyclopentanone
        L3: butyrolactone
        L3: 25dihydrofuran
        L3: 12dioxolane
        L3: 12dioxolene
        L3: 123trioxolane
        L3: 124trioxolane
        L3: thiolane
        L3: 2,3-dihydrothiophene
        L3: 2,5-dihydrothiophene
        L3: thiophene
        L3: 1,2-dithiolane
        L3: 1,3-dithiolane
        L3: 1,2,3-trithiolane
        L3: 1,2,4-trithiolane
        L3: tetrathiolane
        L3: pentathiolane
        L3: Pyrrolidine
        L3: methylenecyclopentane
        L3: Fulvene
        L3: 3-Methylenecyclopentene
        L3: 4-Methylenecyclopentene
        L3: 12methylenecyclopentane
    L2: SixMember
        L3: sixnosidedouble
            L4: Cyclohexane
            L4: 12dioxane
            L4: 1,3-Dioxane
            L4: 1,4-Dioxane
            L4: 1,3,5-Trioxane
            L4: 124trioxane
            L4: 123trioxane
            L4: Oxane
            L4: hexasulfur
            L4: Piperidine
        L3: six-sidedoubles
            L4: six-onesidedouble
                L5: Cyclohexanone
            L4: sixmembd-allsingles-twosidedoubles-para
                L5: 14methylenecyclohexane
            L4: sixmembd-allsingles-twosidedoubles-ortho
            L4: sixmembd-allsingles-twosidedoubles-meta
        L3: six-inringonedouble
            L4: 34dihydro12dioxin
            L4: 36dihydro2hpyran
            L4: Cyclohexene
            L4: 3,4-Dihydro-2H-pyran
            L4: 36dihydro12dioxin
            L4: 24dihydro13dioxin
            L4: 23dihydro14dioxin
            L4: 124trioxene
            L4: 123trioxene
        L3: six-inringtwodouble-13
            L4: 1,3-Cyclohexadiene
        L3: six-inringtwodouble-14
            L4: 1,4-Cyclohexadiene
            L4: 14dioxin
        L3: six-inringthreedouble_124
            L4: 124cyclohexatriene
        L3: six-inringthreedouble_123
            L4: 123cyclohexatriene
        L3: six-inringtwodouble-12
        L3: six-oneside-twoindoubles-25
            L4: 25cyclohexadienone
            L4: 14cyclohexadiene3methylene
        L3: six-oneside-twoindoubles-24
            L4: 24cyclohexadienone
            L4: 13cyclohexadiene5methylene
        L3: six-twoin13-twoout
            L4: fg6
            L4: oxylene
            L4: obenzoquinone
        L3: six-twoin14-twoout
            L4: pbenzoquinone
            L4: pxylene
        L3: 3,4-dimethylenecyclohexene
        L3: six-inringonetriple
            L4: cyclohexyne
        L3: six-inringonetripleonedouble-13
            L4: cyclohex_1_yne_3_ene
            L4: o_benzyne
        L3: six-inringonetripleonedouble-14
            L4: cyclohex_1_yne_4_ene
        L3: six-inringonetripletwodouble-134
        L3: six-inringonetriplethreedouble-1345
        L3: six-inringtwotriple-13
            L4: 1_3_cyclohexadiyne
    L2: SevenMember
        L3: Cycloheptane
        L3: Cycloheptene
        L3: 1,3-Cycloheptadiene
        L3: 1,3,5-Cycloheptatriene
        L3: Cycloheptanone
        L3: 1,4-Cycloheptadiene
        L3: seven-inringtwodouble-12
            L4: 1_2_cycloheptadiene
            L4: 1,2,4,6-Cycloheptatetraene
        L3: seven-inringthreedouble-123
            L4: 1_2_3_cycloheptatriene
        L3: seven-inringonetriple
            L4: cycloheptyne
        L3: heptasulfur
        L3: oxepane
    L2: EightMember
        L3: Cyclooctane
        L3: cis-Cyclooctene
        L3: 1,3,5-Cyclooctatriene
        L3: Cyclooctatetraene
        L3: Cyclooctanone
        L3: 1,3-cyclooctadiene
        L3: 1,4-cyclooctadiene
        L3: 1,5-cyclooctadiene
        L3: octasulfur
    L2: NineMember
        L3: Cyclononane
        L3: Cyclononanone
    L2: TenMember
        L3: Cyclodecane
        L3: Cyclodecanone
"""
)

