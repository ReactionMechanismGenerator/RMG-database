#!/usr/bin/env python
# encoding: utf-8

name = "Ring Corrections"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 96,
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
    shortDesc = u"""Dummy Root""",
    longDesc = 
u"""

""",
    rank = 10,
)


entry(
    index = 96,
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
    shortDesc = u"""Aromatic""",
    longDesc = 
u"""
Ring correction is zero because RMG uses Cb group corrections instead in the case of a ring containing Cb bonds
""",
    rank = 1,
)


entry(
    index = 96,
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
    shortDesc = u"""Aromatic""",
    longDesc = 
u"""
Ring correction is zero because RMG uses Cb group corrections instead in the case of a ring containing Cb bonds
""",
    rank = 1,
)

entry(
    index = 97,
    label = "ThreeMember",
    group = 
"""
1 * R!H u0 {2,[S,D,T]} {3,[S,D]}
2   R!H u0 {1,[S,D,T]} {3,[S,D]}
3   R!H u0 {1,[S,D]} {2,[S,D]}
""",
    thermo = u'Cyclopropane',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1,
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
    shortDesc = u"""Cyclopropane ring BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "Cyclopropene",
    group = 
"""
1 * Cs u0 {2,S} {3,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {1,S} {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.469,-0.789,-0.953,-1.107,-1.45,-1.696,-1.716],'cal/(mol*K)'),
        H298 = (55.4702,'kcal/mol'),
        S298 = (33.3257,'cal/(mol*K)'),
    ),
    shortDesc = u"""Cyclopropene ring BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 125,
    label = "Cyclopropadiene",
    group = 
"""
1 * Cd  u0 {2,S} {3,D}
2   Cd  u0 {1,S} {3,D}
3   Cdd u0 {1,D} {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.469,-0.789,-0.953,-1.107,-1.45,-1.696,-1.716],'cal/(mol*K)'),
        H298 = (73.04,'kcal/mol'),
        S298 = (33.3257,'cal/(mol*K)'),
    ),
    shortDesc = u"""Enthalpy from doi:10.1021/j100005a002 (S and Cp from Cyclopropene row above)""",
    longDesc = 
u"""

""",
)

entry(
    index = 126,
    label = "Cyclopropatriene",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   Cdd u0 {1,D} {3,D}
3   Cdd u0 {1,D} {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.469,-0.789,-0.953,-1.107,-1.45,-1.696,-1.716],'cal/(mol*K)'),
        H298 = (78,'kcal/mol'),
        S298 = (33.3257,'cal/(mol*K)'),
    ),
    shortDesc = u"""Enthalpy from doi:10.1021/j100005a002 (S and Cp from Cyclopropene row above)""",
    longDesc = 
u"""

""",
)

entry(
    index = 69,
    label = "Ethylene_oxide",
    group = 
"""
1 * O  u0 {2,S} {3,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.891,-2.459,-2.221,-1.969,-1.965,-1.759,2.564],'cal/(mol*K)'),
        H298 = (26.82,'kcal/mol'),
        S298 = (31.1767,'cal/(mol*K)'),
    ),
    shortDesc = u"""CY/C2O from THERM (Dorofeeva, 92) Cp1500 est. as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "dioxirane",
    group = 
"""
1 * Os u0 {2,S} {3,S}
2   Os u0 {1,S} {3,S}
3   Cs u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.099,-3.194,-3.095,-3.038,-3.281,-3.818,-1.346],'cal/(mol*K)'),
        H298 = (25.1977,'kcal/mol'),
        S298 = (32.3877,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "2(co)oxirane",
    group = 
"""
1   CO u0 {2,S} {3,S}
2 * Os u0 {1,S} {3,S}
3   Cs u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.147,-1.715,-2.067,-2.254,-2.546,-2.592,-1.488],'cal/(mol*K)'),
        H298 = (40.7699,'kcal/mol'),
        S298 = (34.529,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 158,
    label = "oxirene",
    group = 
"""
1   Cd u0 {2,S} {3,D}
2 * Os u0 {1,S} {3,S}
3   Cd u0 {1,D} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.283,-1.56,-2.46,-2.83,-3.22,-3.08,-3.04],'cal/(mol*K)'),
        H298 = (80.64,'kcal/mol'),
        S298 = (38.08,'cal/(mol*K)'),
    ),
    shortDesc = u"""Derived from goldsmith's DFT-QCI library""",
    longDesc = 
u"""

""",
)




entry(
    index = 8,
    label = "cyclopropanedione",
    group = 
"""
1   CO u0 {2,S} {3,S}
2 * CO u0 {1,S} {3,S}
3   Cs u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.85,1.69,0.674,-0.137,-1.157,-2.068,0.878],'cal/(mol*K)'),
        H298 = (67.2975,'kcal/mol'),
        S298 = (38.9107,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "cyclopropenone",
    group = 
"""
1   Cd u0 {2,S} {3,D}
2 * CO u0 {1,S} {3,S}
3   Cd u0 {1,D} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.734,-1.275,-1.673,-1.861,-2.134,-2.557,-1.78],'cal/(mol*K)'),
        H298 = (56.774,'kcal/mol'),
        S298 = (35.6157,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 133,
    label = "thiirane",
    group = 
"""
1 * S u0 {2,S} {3,S}
2   C u0 {1,S} {3,S}
3   C u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.02,-2.54,-2.13,-1.81,-1.49,-1.26,-0.96],'cal/(mol*K)'),
        H298 = (17.82,'kcal/mol'),
        S298 = (28.57,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
u"""

""",
)

entry(
    index = 134,
    label = "dithiirane",
    group = 
"""
1 * S u0 {2,S} {3,S}
2   S u0 {1,S} {3,S}
3   C u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.26,-6.35,-5.37,-4.63,-3.67,-3.08,-2.21],'cal/(mol*K)'),
        H298 = (21.37,'kcal/mol'),
        S298 = (31.73,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
u"""

""",
)

entry(
    index = 135,
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
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2009, dH from NIST-JANAF""",
    longDesc = 
u"""

""",
)

entry(
    index = 151,
    label = "thiirene",
    group = 
"""
1 * S u0 {2,S} {3,S}
2   C u0 {1,S} {3,D}
3   C u0 {1,S} {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.13,-3.8,-6.26,-8.36,-11.65,-14.12,-18.01],'cal/(mol*K)'),
        H298 = (52.44,'kcal/mol'),
        S298 = (34.28,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
u"""

""",
)

entry(
    index = 92,
    label = "Ethyleneimine",
    group = 
"""
1 * N3s u0 {2,S} {3,S}
2   Cs  u0 {1,S} {3,S}
3   Cs  u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (27.7,'kcal/mol'),
        S298 = (31.6,'cal/(mol*K)'),
    ),
    shortDesc = u"""Ethyleneimine ring BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "Methylene_cyclopropane",
    group = 
"""
1 * Cd u0 {2,S} {3,S} {4,D}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {1,S} {2,S}
4   Cd u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.1,-2.121,-2.081,-2.005,-1.98,-1.903,-1.541],'cal/(mol*K)'),
        H298 = (40.92,'kcal/mol'),
        S298 = (31.4507,'cal/(mol*K)'),
    ),
    shortDesc = u"""Methylene cyclopropane ring BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "cyclopropanone",
    group = 
"""
1 * C u0 {2,S} {3,S} {4,D}
2   C u0 {1,S} {3,S}
3   C u0 {1,S} {2,S}
4   O u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.274,-1.932,-1.307,-0.838,-1.06,-1.032,-0.271],'cal/(mol*K)'),
        H298 = (45.6,'kcal/mol'),
        S298 = (30.7247,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "methylenecyclopropene",
    group = 
"""
1   Cd u0 {2,S} {3,D}
2 * Cd u0 {1,S} {3,S} {4,D}
3   Cd u0 {1,D} {2,S}
4   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.457,-0.093,-0.645,-1.124,-1.936,-2.246,-2.962],'cal/(mol*K)'),
        H298 = (69.316,'kcal/mol'),
        S298 = (39.8857,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "methylenecyclopropanone",
    group = 
"""
1   CO u0 {2,S} {3,S}
2 * Cd u0 {1,S} {3,S} {4,D}
3   Cs u0 {1,S} {2,S}
4   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.13,-1.101,-1.774,-2.139,-2.509,-2.858,-0.084],'cal/(mol*K)'),
        H298 = (57.7946,'kcal/mol'),
        S298 = (37.18,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "methyleneoxirane",
    group = 
"""
1   Os u0 {2,S} {3,S}
2 * Cd u0 {1,S} {3,S} {4,D}
3   Cs u0 {1,S} {2,S}
4   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.101,-2.381,-2.338,-2.236,-2.424,-2.639,-2.068],'cal/(mol*K)'),
        H298 = (36.0543,'kcal/mol'),
        S298 = (29.893,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "12Methylenecyclopropane",
    group = 
"""
1   Cd u0 {2,S} {3,S} {4,D}
2 * Cd u0 {1,S} {3,S} {5,D}
3   Cs u0 {1,S} {2,S}
4   Cd u0 {1,D}
5   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.326,-3.139,-3.361,-3.148,-2.736,-2.412,-1.706],'cal/(mol*K)'),
        H298 = (51.4711,'kcal/mol'),
        S298 = (35.3587,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 98,
    label = "FourMember",
    group = 
"""
1 * R!H u0 {2,[S,D]} {4,[S,D]}
2   R!H u0 {1,[S,D]} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,[S,D]}
4   R!H u0 {1,[S,D]} {3,[S,D]}
""",
    thermo = u'Cyclobutane',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
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
    shortDesc = u"""Cyclobutane ring BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "Cyclobutene",
    group = 
"""
1 * Cs u0 {2,S} {4,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cs u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.038,-2.783,-2.423,-2.153,-1.888,-1.694,-1.258],'cal/(mol*K)'),
        H298 = (29.84,'kcal/mol'),
        S298 = (29.8677,'cal/(mol*K)'),
    ),
    shortDesc = u"""Cyclobutene ring BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 70,
    label = "Oxetane",
    group = 
"""
1 * O  u0 {2,S} {4,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.08,-4.28,-3.636,-3.016,-2.451,-1.896,2.84],'cal/(mol*K)'),
        H298 = (25.08,'kcal/mol'),
        S298 = (28.5487,'cal/(mol*K)'),
    ),
    shortDesc = u"""CY/C3O from THERM (Dorofeeva, 92) Cp1500 est. as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index = 159,
    label = "Oxetene",
    group = 
"""
1 * Os u0 {2,S} {4,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   C  u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.88,-4.22,-4.18,-3.97,-3.65,-3.56,-2.93],'cal/(mol*K)'),
        H298 = (32.51,'kcal/mol'),
        S298 = (29.26,'cal/(mol*K)'),
    ),
    shortDesc = u"""Derived from goldsmith's DFT-QCI library""",
    longDesc = 
u"""

""",
)

entry(
    index = 83,
    label = "Beta-Propiolactone",
    group = 
"""
1 * O  u0 {2,S} {4,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   CO u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.434,-4.019,-3.31,-2.703,-2.253,-2.012,1.3],'cal/(mol*K)'),
        H298 = (22.98,'kcal/mol'),
        S298 = (30.392,'cal/(mol*K)'),
    ),
    shortDesc = u"""Beta-Propiolactone ring BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 85,
    label = "Cyclobutanone",
    group = 
"""
1 * CO u0 {2,S} {4,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.62,-4.96,-3.744,-2.671,-1.962,-1.415,-0.3],'cal/(mol*K)'),
        H298 = (22.53,'kcal/mol'),
        S298 = (29.8337,'cal/(mol*K)'),
    ),
    shortDesc = u"""Cyclobutanone ring BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "12dioxetane",
    group = 
"""
1   Cs u0 {2,S} {4,S}
2 * Cs u0 {1,S} {3,S}
3   Os u0 {2,S} {4,S}
4   Os u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.586,-4.031,-3.818,-3.503,-3.252,-3.45,1.262],'cal/(mol*K)'),
        H298 = (28.0736,'kcal/mol'),
        S298 = (29.0217,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "dioxerene",
    group = 
"""
1   Cd u0 {2,D} {4,S}
2 * Cd u0 {1,D} {3,S}
3   Os u0 {2,S} {4,S}
4   Os u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.375,-4.281,-4.206,-4.037,-3.926,-3.327,-2.473],'cal/(mol*K)'),
        H298 = (24.4413,'kcal/mol'),
        S298 = (29.7827,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "cyclobutadiene_13",
    group = 
"""
1   Cd u0 {2,D} {4,S}
2 * Cd u0 {1,D} {3,S}
3   Cd u0 {2,S} {4,D}
4   Cd u0 {1,S} {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.336,-3.24,-3.526,-3.419,-3.071,-2.761,-2.346],'cal/(mol*K)'),
        H298 = (77.2135,'kcal/mol'),
        S298 = (36.4303,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 136,
    label = "thietane",
    group = 
"""
1 * S u0 {2,S} {4,S}
2   C u0 {1,S} {3,S}
3   C u0 {2,S} {4,S}
4   C u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.42,-3.66,-2.92,-2.3,-1.53,-1.01,-0.3],'cal/(mol*K)'),
        H298 = (19.82,'kcal/mol'),
        S298 = (25.35,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
u"""

""",
)

entry(
    index = 137,
    label = "1,2-dithietane",
    group = 
"""
1 * S u0 {2,S} {4,S}
2   S u0 {1,S} {3,S}
3   C u0 {2,S} {4,S}
4   C u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.24,-3.62,-3.13,-2.69,-2.11,-1.62,-0.79],'cal/(mol*K)'),
        H298 = (23.45,'kcal/mol'),
        S298 = (24.44,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
u"""

""",
)

entry(
    index = 138,
    label = "1,3-dithietane",
    group = 
"""
1 * S u0 {2,S} {4,S}
2   C u0 {1,S} {3,S}
3   S u0 {2,S} {4,S}
4   C u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-11.59,-9.53,-7.27,-5.52,-3.34,-2.19,-0.96],'cal/(mol*K)'),
        H298 = (16.87,'kcal/mol'),
        S298 = (29.55,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
u"""

""",
)

entry(
    index = 139,
    label = "trithietane",
    group = 
"""
1 * S u0 {2,S} {4,S}
2   S u0 {1,S} {3,S}
3   S u0 {2,S} {4,S}
4   C u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.81,-7.66,-6.51,-5.66,-4.53,-3.75,-2.33],'cal/(mol*K)'),
        H298 = (30.77,'kcal/mol'),
        S298 = (29.05,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
u"""

""",
)

entry(
    index = 140,
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
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2009, dH from NIST-JANAF""",
    longDesc = 
u"""

""",
)

entry(
    index = 93,
    label = "Azetidine",
    group = 
"""
1 * N3s u0 {2,S} {4,S}
2   Cs  u0 {1,S} {3,S}
3   Cs  u0 {2,S} {4,S}
4   Cs  u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (26.2,'kcal/mol'),
        S298 = (29.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""Azetidine ring BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 84,
    label = "4-Methylene-2-oxetanone",
    group = 
"""
1 * O  u0 {2,S} {4,S}
2   Cd u0 {1,S} {3,S} {5,D}
3   Cs u0 {2,S} {4,S}
4   CO u0 {1,S} {3,S}
5   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.912,-1.903,-1.567,-1.378,-1.566,-1.528,1.547],'cal/(mol*K)'),
        H298 = (16.94,'kcal/mol'),
        S298 = (35.477,'cal/(mol*K)'),
    ),
    shortDesc = u"""4-Methylene-2-oxetanone ring BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "methylenecyclobutane",
    group = 
"""
1   Cs u0 {2,S} {4,S}
2 * Cd u0 {1,S} {3,S} {5,D}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {1,S} {3,S}
5   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.91,-3.339,-2.739,-2.2,-1.51,-1.051,-62.52],'cal/(mol*K)'),
        H298 = (26.9,'kcal/mol'),
        S298 = (28.8887,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "2methyleneoxetane",
    group = 
"""
1   Os u0 {2,S} {4,S}
2 * Cd u0 {1,S} {3,S} {5,D}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {1,S} {3,S}
5   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.33,-3.553,-3.213,-2.78,-2.445,-2.331,0.556],'cal/(mol*K)'),
        H298 = (23.79,'kcal/mol'),
        S298 = (25.597,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "12methylenecyclobutane",
    group = 
"""
1 * Cd u0 {2,S} {4,S} {5,D}
2   Cd u0 {1,S} {3,S} {6,D}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {1,S} {3,S}
5   Cd u0 {1,D}
6   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.313,-4.605,-4.416,-3.887,-3.024,-2.355,-1.276],'cal/(mol*K)'),
        H298 = (28.04,'kcal/mol'),
        S298 = (31.4877,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 99,
    label = "FiveMember",
    group = 
"""
1 * R!H u0 {2,[S,D,T]} {5,[S,D]}
2   R!H u0 {1,[S,D,T]} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,[S,D]}
4   R!H u0 {3,[S,D]} {5,[S,D,T]}
5   R!H u0 {1,[S,D]} {4,[S,D,T]}
""",
    thermo = u'Cyclopentane',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
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
    shortDesc = u"""Cyclopentane ring BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "Cyclopentene",
    group = 
"""
1   Cs u0 {2,S} {5,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cs u0 {3,S} {5,S}
5 * Cs u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.5,-3.942,-3.291,-2.759,-2.08,-1.628,-0.898],'cal/(mol*K)'),
        H298 = (5.97,'kcal/mol'),
        S298 = (25.8284,'cal/(mol*K)'),
    ),
    shortDesc = u"""Cyclopentene ring BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "Cyclopentadiene",
    group = 
"""
1 * Cs u0 {2,S} {5,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {1,S} {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.7845,-3.72708,-3.2688,-2.74383,-2.05359,-1.65464,-0.98756],'cal/(mol*K)'),
        H298 = (6.05,'kcal/mol'),
        S298 = (27.9821,'cal/(mol*K)'),
    ),
    shortDesc = u"""Cyclopentadiene ring BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 152,
    label = "five-inringthreedouble-124",
    group = 
"""
1 * R!H  u0 {2,D} {5,[S,D]}
2   Cdd u0 {1,D} {3,D}
3   R!H  u0 {2,D} {4,[S,D]}
4   R!H  u0 {3,[S,D]} {5,D}
5   R!H  u0 {1,[S,D]} {4,D}
""",
    thermo = u'Cyclopentatriene',
    shortDesc = u"""""",
    longDesc = 
u"""
For now, any 5-membered ring that has at least 3 double-bonds in the 1,2,4 positions will use this general correction.
""",
)

entry(
    index = 71,
    label = "Tetrahydrofuran",
    group = 
"""
1 * O  u0 {2,S} {5,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.93,-5.71,-4.67,-3.721,-2.689,-1.856,3.213],'cal/(mol*K)'),
        H298 = (5.96,'kcal/mol'),
        S298 = (21.1624,'cal/(mol*K)'),
    ),
    shortDesc = u"""CY/C4O from THERM (Dorofeeva, 92) Cp1500 est. as Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index = 76,
    label = "2,3-Dihydrofuran",
    group = 
"""
1 * O  u0 {2,S} {5,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.56,-5.96,-5.695,-5.144,-4.218,-3.708,-0.284],'cal/(mol*K)'),
        H298 = (4.57,'kcal/mol'),
        S298 = (23.83,'cal/(mol*K)'),
    ),
    shortDesc = u"""2,3-Dihydrofuran ring BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 77,
    label = "1,3-Dioxolane",
    group = 
"""
1 * Cs u0 {2,S} {5,S}
2   O  u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   O  u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.655,-6.405,-6.306,-6.405,-7.631,-8.27,-3.21],'cal/(mol*K)'),
        H298 = (5.13,'kcal/mol'),
        S298 = (20.4021,'cal/(mol*K)'),
    ),
    shortDesc = u"""1,3-Dioxolane ring BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 78,
    label = "Furan",
    group = 
"""
1   Cd u0 {2,D} {5,S}
2   Cd u0 {1,D} {3,S}
3   Cd u0 {2,S} {4,D}
4   Cd u0 {3,D} {5,S}
5 * O  u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.09,-7.18,-6.79,-5.86,-4.83,-3.71,-2.9],'cal/(mol*K)'),
        H298 = (-6.3,'kcal/mol'),
        S298 = (31.71,'cal/(mol*K)'),
    ),
    shortDesc = u"""Furan ring BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 80,
    label = "Dihydro-2,5-furandione",
    group = 
"""
1 * O  u0 {2,S} {5,S}
2   CO u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   CO u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.235,-4.726,-3.615,-1.82,-1.835,-1.084,1.104],'cal/(mol*K)'),
        H298 = (1.4,'kcal/mol'),
        S298 = (37.7647,'cal/(mol*K)'),
    ),
    shortDesc = u"""Dihydro-2,5-furandione ring BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 82,
    label = "2,5-Furandione",
    group = 
"""
1 * O  u0 {2,S} {5,S}
2   CO u0 {1,S} {3,S}
3   Cd u0 {2,S} {4,D}
4   Cd u0 {3,D} {5,S}
5   CO u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (3.6,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""2,5-Furandione ring BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 86,
    label = "Cyclopentanone",
    group = 
"""
1 * CO u0 {2,S} {5,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.06,-4.927,-3.392,-2.097,-1.093,-0.322,1.29],'cal/(mol*K)'),
        H298 = (4.47,'kcal/mol'),
        S298 = (24.6287,'cal/(mol*K)'),
    ),
    shortDesc = u"""Cyclopentanone ring BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "butyrolactone",
    group = 
"""
1 * CO u0 {2,S} {5,S}
2   Os u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.836,-5.134,-4.114,-3.222,-2.341,-1.822,1.888],'cal/(mol*K)'),
        H298 = (7.92,'kcal/mol'),
        S298 = (27.4547,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "25dihydrofuran",
    group = 
"""
1 * Cs u0 {2,S} {5,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cs u0 {3,S} {5,S}
5   Os u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.946,-3.361,-2.438,-1.799,-1.458,-1.056,-0.254],'cal/(mol*K)'),
        H298 = (4.23674,'kcal/mol'),
        S298 = (25.1504,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "12dioxolane",
    group = 
"""
1 * Os u0 {2,S} {5,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Os u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.95,-4.859,-4.265,-3.679,-3.089,-3.091,1.915],'cal/(mol*K)'),
        H298 = (6.05383,'kcal/mol'),
        S298 = (25.0554,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "12dioxolene",
    group = 
"""
1 * Os u0 {2,S} {5,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cs u0 {3,S} {5,S}
5   Os u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.159,-4.213,-3.754,-3.376,-3.14,-2.919,-1.982],'cal/(mol*K)'),
        H298 = (4.56853,'kcal/mol'),
        S298 = (29.97,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "123trioxolane",
    group = 
"""
1 * Os u0 {2,S} {5,S}
2   Os u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Os u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.566,-3.543,-3.344,-2.829,-2.487,-2.78,2.13],'cal/(mol*K)'),
        H298 = (10.1971,'kcal/mol'),
        S298 = (23.316,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "124trioxolane",
    group = 
"""
1 * Os u0 {2,S} {5,S}
2   Cs u0 {1,S} {3,S}
3   Os u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Os u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.648,-4.764,-3.63,-2.89,-2.711,-2.859,2.25],'cal/(mol*K)'),
        H298 = (9.45319,'kcal/mol'),
        S298 = (25.1104,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 141,
    label = "thiolane",
    group = 
"""
1 * S u0 {2,S} {5,S}
2   C u0 {1,S} {3,S}
3   C u0 {2,S} {4,S}
4   C u0 {3,S} {5,S}
5   C u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.61,-4.54,-3.51,-2.63,-1.49,-0.73,0.32],'cal/(mol*K)'),
        H298 = (2.02,'kcal/mol'),
        S298 = (20.68,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
u"""

""",
)

entry(
    index = 142,
    label = "2,3-dihydrothiophene",
    group = 
"""
1 * S  u0 {2,S} {5,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   C  u0 {3,S} {5,S}
5   C  u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.58,-4.63,-3.67,-2.89,-1.9,-1.26,-0.41],'cal/(mol*K)'),
        H298 = (3.37,'kcal/mol'),
        S298 = (24.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
u"""

""",
)

entry(
    index = 143,
    label = "2,5-dihydrothiophene",
    group = 
"""
1 * S  u0 {2,S} {5,S}
2   C  u0 {1,S} {3,S}
3   Cd u0 {2,S} {4,D}
4   Cd u0 {3,D} {5,S}
5   C  u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10.84,-9.28,-7.17,-5.42,-3.18,-1.97,-0.74],'cal/(mol*K)'),
        H298 = (2.19,'kcal/mol'),
        S298 = (28.23,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
u"""

""",
)

entry(
    index = 144,
    label = "thiophene",
    group = 
"""
1 * S  u0 {2,S} {5,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {1,S} {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.15,-3.75,-2.7,-2.03,-1.45,-1.14,-0.76],'cal/(mol*K)'),
        H298 = (-17.22,'kcal/mol'),
        S298 = (23.78,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
u"""

""",
)

entry(
    index = 145,
    label = "1,2-dithiolane",
    group = 
"""
1 * S u0 {2,S} {5,S}
2   S u0 {1,S} {3,S}
3   C u0 {2,S} {4,S}
4   C u0 {3,S} {5,S}
5   C u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.15,-6.27,-7.52,-8.83,-11.39,-13.48,-16.94],'cal/(mol*K)'),
        H298 = (23.29,'kcal/mol'),
        S298 = (23.78,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
u"""

""",
)

entry(
    index = 146,
    label = "1,3-dithiolane",
    group = 
"""
1 * S u0 {2,S} {5,S}
2   C u0 {1,S} {3,S}
3   S u0 {2,S} {4,S}
4   C u0 {3,S} {5,S}
5   C u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.45,-6.68,-4.91,-3.49,-1.72,-0.7,0.45],'cal/(mol*K)'),
        H298 = (0.48,'kcal/mol'),
        S298 = (22.84,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
u"""

""",
)

entry(
    index = 147,
    label = "1,2,3-trithiolane",
    group = 
"""
1 * S u0 {2,S} {5,S}
2   S u0 {1,S} {3,S}
3   S u0 {2,S} {4,S}
4   C u0 {3,S} {5,S}
5   C u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.51,-4.63,-3.98,-3.49,-2.82,-2.2,-0.88],'cal/(mol*K)'),
        H298 = (9.12,'kcal/mol'),
        S298 = (22.01,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
u"""

""",
)

entry(
    index = 148,
    label = "1,2,4-trithiolane",
    group = 
"""
1 * S u0 {2,S} {5,S}
2   S u0 {1,S} {3,S}
3   C u0 {2,S} {4,S}
4   S u0 {3,S} {5,S}
5   C u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-11.78,-9.58,-7.37,-5.67,-3.5,-2.26,-0.71],'cal/(mol*K)'),
        H298 = (4.4,'kcal/mol'),
        S298 = (24.39,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
u"""

""",
)

entry(
    index = 149,
    label = "tetrathiolane",
    group = 
"""
1 * S u0 {2,S} {5,S}
2   S u0 {1,S} {3,S}
3   S u0 {2,S} {4,S}
4   S u0 {3,S} {5,S}
5   C u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.82,-8.46,-7.22,-6.33,-5.17,-4.28,-2.4],'cal/(mol*K)'),
        H298 = (10.72,'kcal/mol'),
        S298 = (26.56,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
u"""

""",
)

entry(
    index = 150,
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
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2009, dH from NIST-JANAF""",
    longDesc = 
u"""

""",
)

entry(
    index = 94,
    label = "Pyrrolidine",
    group = 
"""
1 * N3s u0 {2,S} {5,S}
2   Cs  u0 {1,S} {3,S}
3   Cs  u0 {2,S} {4,S}
4   Cs  u0 {3,S} {5,S}
5   Cs  u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.17,-5.58,-4.8,-4,-2.87,-2.17,0],'cal/(mol*K)'),
        H298 = (6.8,'kcal/mol'),
        S298 = (26.7,'cal/(mol*K)'),
    ),
    shortDesc = u"""Pyrrolidine ring BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    label = "methylenecyclopentane",
    group = 
"""
1 * Cd u0 {2,S} {5,S} {6,D}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {1,S} {4,S}
6   Cd u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.861,-4.909,-3.91,-3.01,-1.769,-0.969,0],'cal/(mol*K)'),
        H298 = (5.21,'kcal/mol'),
        S298 = (24.6287,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 122,
    label = "Fulvene",
    group = 
"""
1 * Cd u0 {2,S} {5,S} {6,D}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {1,S} {4,D}
6   Cd u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.1,-3.4,-3.4,-3.2,-3,-2.6,-2.6],'cal/(mol*K)'),
        H298 = (14.73,'kcal/mol'),
        S298 = (34.1,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 123,
    label = "3-Methylenecyclopentene",
    group = 
"""
1 * Cs u0 {2,S} {3,S}
2   Cs u0 {1,S} {4,S}
3   Cd u0 {1,S} {5,S} {6,D}
4   Cd u0 {2,S} {5,D}
5   Cd u0 {3,S} {4,D}
6   Cd u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.9,-4.8,-4.4,-3.7,-2.7,-2,-0.9],'cal/(mol*K)'),
        H298 = (6.2,'kcal/mol'),
        S298 = (28.9,'cal/(mol*K)'),
    ),
    shortDesc = u"""Copied from 4-methylenecyclopentene""",
    longDesc = 
u"""

""",
)

entry(
    index = 124,
    label = "4-Methylenecyclopentene",
    group = 
"""
1 * Cs u0 {3,S} {4,S}
2   Cs u0 {3,S} {5,S}
3   Cd u0 {1,S} {2,S} {6,D}
4   Cd u0 {1,S} {5,D}
5   Cd u0 {2,S} {4,D}
6   Cd u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.9,-4.8,-4.4,-3.7,-2.7,-2,-0.9],'cal/(mol*K)'),
        H298 = (6.2,'kcal/mol'),
        S298 = (28.9,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "12methylenecyclopentane",
    group = 
"""
1 * Cd u0 {2,S} {5,S} {6,D}
2   Cd u0 {1,S} {3,S} {7,D}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {1,S} {4,S}
6   Cd u0 {1,D}
7   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.844,-5.197,-4.882,-4.175,-2.988,-2.088,-0.655],'cal/(mol*K)'),
        H298 = (6.67,'kcal/mol'),
        S298 = (31.384,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 100,
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
    thermo = u'Cyclohexane',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 105,
    label = "sixnosidedouble",
    group = 
"""
1 * [Cs,Os,N3s,Ss] u0 {2,S} {6,S}
2   [Cs,Os,N3s,Ss] u0 {1,S} {3,S}
3   [Cs,Os,N3s,Ss] u0 {2,S} {4,S}
4   [Cs,Os,N3s,Ss] u0 {3,S} {5,S}
5   [Cs,Os,N3s,Ss] u0 {4,S} {6,S}
6   [Cs,Os,N3s,Ss] u0 {1,S} {5,S}
""",
    thermo = u'Cyclohexane',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
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
    shortDesc = u"""Cyclohexane ring BENSON https:""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    label = "12dioxane",
    group = 
"""
1   Cs u0 {2,S} {6,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4 * Cs u0 {3,S} {5,S}
5   Os u0 {4,S} {6,S}
6   Os u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.66,-5.11,-4.17,-3.36,-2.52,-2.4,2.76],'cal/(mol*K)'),
        H298 = (3.9,'kcal/mol'),
        S298 = (19.6424,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 73,
    label = "1,3-Dioxane",
    group = 
"""
1   Os u0 {2,S} {6,S}
2 * Cs u0 {1,S} {3,S}
3   Os u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.28,-5.951,-4.458,-3.15,-1.967,-0.83,6.799],'cal/(mol*K)'),
        H298 = (1.88,'kcal/mol'),
        S298 = (16.1924,'cal/(mol*K)'),
    ),
    shortDesc = u"""1,3-Dioxane ring BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 74,
    label = "1,4-Dioxane",
    group = 
"""
1   Cs u0 {2,S} {6,S}
2   Cs u0 {1,S} {3,S}
3 * Os u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Os u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.6,-5,-3.8,-2.6,-1.5,-0.4,8.9],'cal/(mol*K)'),
        H298 = (3.4,'kcal/mol'),
        S298 = (17.8049,'cal/(mol*K)'),
    ),
    shortDesc = u"""1,4-Dioxane ring BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 75,
    label = "1,3,5-Trioxane",
    group = 
"""
1   Cs u0 {2,S} {6,S}
2   Os u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4 * Os u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Os u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.01,-5.719,-3.632,-2.189,-1.525,-0.624,7.031],'cal/(mol*K)'),
        H298 = (4.09,'kcal/mol'),
        S298 = (16.1953,'cal/(mol*K)'),
    ),
    shortDesc = u"""1,3,5-Trioxane ring BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
    label = "124trioxane",
    group = 
"""
1   Os u0 {2,S} {6,S}
2   Cs u0 {1,S} {3,S}
3   Os u0 {2,S} {4,S}
4 * Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Os u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.68,-4.07,-2.95,-2.09,-1.73,-1.8,5.2],'cal/(mol*K)'),
        H298 = (3.6,'kcal/mol'),
        S298 = (19.9,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 43,
    label = "123trioxane",
    group = 
"""
1   Os u0 {2,S} {6,S}
2   Os u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4 * Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Os u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.08,-2.81,-2.55,-1.93,-1.55,-1.9,3.09],'cal/(mol*K)'),
        H298 = (4.87,'kcal/mol'),
        S298 = (17.2,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 111,
    label = "Oxane",
    group = 
"""
1 * Cs u0 {2,S} {6,S}
2   Os u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6,-5.5,-4.2,-3,-1.6,-0.5,4.9],'cal/(mol*K)'),
        H298 = (0.7,'kcal/mol'),
        S298 = (18.8,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 155,
    label = "hexasulfur",
    group = 
"""
1 * Ss u0 {2,S} {6,S}
2   Ss u0 {1,S} {3,S}
3   Ss u0 {2,S} {4,S}
4   Ss u0 {3,S} {5,S}
5   Ss u0 {4,S} {6,S}
6   Ss u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.61,-0.16,-5.5,-6.91,-8.91,-9.24,-7.14],'cal/(mol*K)'),
        H298 = (6.1,'kcal/mol'),
        S298 = (4.36,'cal/(mol*K)'),
    ),
    shortDesc = u"""All from NIST-JANAF table""",
    longDesc = 
u"""

""",
)

entry(
    index = 95,
    label = "Piperidine",
    group = 
"""
1 * N3s u0 {2,S} {6,S}
2   Cs  u0 {1,S} {3,S}
3   Cs  u0 {2,S} {4,S}
4   Cs  u0 {3,S} {5,S}
5   Cs  u0 {4,S} {6,S}
6   Cs  u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.17,-5.58,-4.8,-4,-2.87,-2.17,0],'cal/(mol*K)'),
        H298 = (6.8,'kcal/mol'),
        S298 = (26.7,'cal/(mol*K)'),
    ),
    shortDesc = u"""Piperidine ring BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 106,
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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 107,
    label = "six-onesidedouble",
    group = 
"""
1   [Cs,Os] u0 {2,S} {6,S}
2 * [Cd,CO] u0 {1,S} {3,S}
3   [Cs,Os] u0 {2,S} {4,S}
4   [Cs,Os] u0 {3,S} {5,S}
5   [Cs,Os] u0 {4,S} {6,S}
6   [Cs,Os] u0 {1,S} {5,S}
""",
    thermo = u'Cyclohexanone',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 87,
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
    shortDesc = u"""Cyclohexanone ring BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 108,
    label = "sixmembd-allsingles-twosidedoubles-para",
    group = 
"""
1   [Cs,Os] u0 {2,S} {6,S}
2 * [Cd,CO] u0 {1,S} {3,S}
3   [Cs,Os] u0 {2,S} {4,S}
4   [Cs,Os] u0 {3,S} {5,S}
5   [Cd,CO] u0 {4,S} {6,S}
6   [Cs,Os] u0 {1,S} {5,S}
""",
    thermo = u'14methylenecyclohexane',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 36,
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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 109,
    label = "sixmembd-allsingles-twosidedoubles-ortho",
    group = 
"""
1   [Cs,Os] u0 {2,S} {6,S}
2 * [Cd,CO] u0 {1,S} {3,S}
3   [Cd,CO] u0 {2,S} {4,S}
4   [Cs,Os] u0 {3,S} {5,S}
5   [Cs,Os] u0 {4,S} {6,S}
6   [Cs,Os] u0 {1,S} {5,S}
""",
    thermo = u'six-sidedoubles',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 110,
    label = "sixmembd-allsingles-twosidedoubles-meta",
    group = 
"""
1   [Cs,Os] u0 {2,S} {6,S}
2 * [Cd,CO] u0 {1,S} {3,S}
3   [Cs,Os] u0 {2,S} {4,S}
4   [Cd,CO] u0 {3,S} {5,S}
5   [Cs,Os] u0 {4,S} {6,S}
6   [Cs,Os] u0 {1,S} {5,S}
""",
    thermo = u'six-sidedoubles',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 114,
    label = "six-inringonedouble",
    group = 
"""
1   [Cs,Os] u0 {2,S} {6,S}
2 * Cd      u0 {1,S} {3,D}
3   Cd      u0 {2,D} {4,S}
4   [Cs,Os] u0 {3,S} {5,S}
5   [Cs,Os] u0 {4,S} {6,S}
6   [Cs,Os] u0 {1,S} {5,S}
""",
    thermo = u'Cyclohexene',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
    label = "34dihydro12dioxin",
    group = 
"""
1   Os u0 {2,S} {6,S}
2   Os u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5 * Cd u0 {4,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.7,-4.9,-4.3,-3.7,-3.11,-2.62,0.62],'cal/(mol*K)'),
        H298 = (1.07,'kcal/mol'),
        S298 = (20.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 37,
    label = "36dihydro2hpyran",
    group = 
"""
1 * Cd u0 {2,S} {6,D}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Os u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cd u0 {1,D} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.4,-4,-3,-2.2,-1.5,-0.8,2.3],'cal/(mol*K)'),
        H298 = (1.43,'kcal/mol'),
        S298 = (19.2,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
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
    shortDesc = u"""Cyclohexene ring BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 79,
    label = "3,4-Dihydro-2H-pyran",
    group = 
"""
1   Os u0 {2,S} {6,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5 * Cd u0 {4,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.26,-6.496,-5.96,-5.142,-3.74,-2.915,0.529],'cal/(mol*K)'),
        H298 = (3.94,'kcal/mol'),
        S298 = (22.01,'cal/(mol*K)'),
    ),
    shortDesc = u"""3,4-Dihydro-2H-pyran ring BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    label = "36dihydro12dioxin",
    group = 
"""
1   Cs u0 {2,S} {6,S}
2 * Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cs u0 {3,S} {5,S}
5   Os u0 {4,S} {6,S}
6   Os u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.45,-4.66,-3.81,-3.16,-2.65,-2.68,-1.53],'cal/(mol*K)'),
        H298 = (3.32,'kcal/mol'),
        S298 = (18.72,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 112,
    label = "24dihydro13dioxin",
    group = 
"""
1   Cd u0 {2,D} {6,S}
2 * Cd u0 {1,D} {3,S}
3   Cs u0 {2,S} {4,S}
4   Os u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Os u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.5,-5.1,-4.2,-3.4,-2.8,-2.3,0.9],'cal/(mol*K)'),
        H298 = (3.1,'kcal/mol'),
        S298 = (20.2,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 113,
    label = "23dihydro14dioxin",
    group = 
"""
1   Cd u0 {2,D} {6,S}
2 * Cd u0 {1,D} {3,S}
3   Os u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Os u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.3,-7.5,-7.5,-6.9,-5.5,-4.9,0.7],'cal/(mol*K)'),
        H298 = (7.9,'kcal/mol'),
        S298 = (19.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "124trioxene",
    group = 
"""
1   Os u0 {2,S} {6,S}
2   Cs u0 {1,S} {3,S}
3   Os u0 {2,S} {4,S}
4 * Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Os u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.51,-5.86,-5.48,-4.98,-4.44,-4.15,-0.75],'cal/(mol*K)'),
        H298 = (6.98,'kcal/mol'),
        S298 = (24.5,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 45,
    label = "123trioxene",
    group = 
"""
1   Os u0 {2,S} {6,S}
2   Os u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4 * Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Os u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.73,-2.67,-2.62,-2.27,-2.14,-2.08,-0.97],'cal/(mol*K)'),
        H298 = (4,'kcal/mol'),
        S298 = (21.57,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 115,
    label = "six-inringtwodouble-13",
    group = 
"""
1   [Cs,Os] u0 {2,S} {6,S}
2 * Cd      u0 {1,S} {3,D}
3   Cd      u0 {2,D} {4,S}
4   Cd      u0 {3,S} {5,D}
5   Cd      u0 {4,D} {6,S}
6   [Cs,Os] u0 {1,S} {5,S}
""",
    thermo = u'1,3-Cyclohexadiene',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 34,
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
    shortDesc = u"""1,3-Cyclohexadiene ring BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 116,
    label = "six-inringtwodouble-14",
    group = 
"""
1   [Cs,Os] u0 {2,S} {6,S}
2 * Cd      u0 {1,S} {3,D}
3   Cd      u0 {2,D} {4,S}
4   [Cs,Os] u0 {3,S} {5,S}
5   Cd      u0 {4,S} {6,D}
6   Cd      u0 {1,S} {5,D}
""",
    thermo = u'1,4-Cyclohexadiene',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
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
    shortDesc = u"""1,4-Cyclohexadiene ring BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 41,
    label = "14dioxin",
    group = 
"""
1   Cd u0 {2,D} {6,S}
2   Cd u0 {1,D} {3,S}
3   Os u0 {2,S} {4,S}
4 * Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Os u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.9,-7.5,-7.5,-7.5,-6.8,-5.6,-4.2],'cal/(mol*K)'),
        H298 = (11.71,'kcal/mol','+|-',-2.9),
        S298 = (27.6,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 153,
    label = "six-inringthreedouble_124",
    group = 
"""
1   R!H     u0 {2,D} {6,S}
2 * Cdd     u0 {1,D} {3,D}
3   R!H      u0 {2,D} {4,S}
4   R!H u0 {3,S} {5,[S,D]}
5   R!H      u0 {4,[S,D]} {6,D}
6   R!H      u0 {1,S} {5,D}
""",
    thermo = u'124cyclohexatriene',
    shortDesc = u"""""",
    longDesc = 
u"""
Use 124cyclohexatriene correction for any 6-membered ring that contains at least 3 double bonds in the 1,2 and 4 p
positions.
""",
)

entry(
    index = 117,
    label = "six-inringtwodouble-12",
    group = 
"""
1   [Cs,Os] u0 {2,S} {6,S}
2 * Cd      u0 {1,S} {3,D}
3   C       u0 {2,D} {4,D}
4   Cd      u0 {3,D} {5,S}
5   [Cs,Os] u0 {4,S} {6,S}
6   [Cs,Os] u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10,10,10,10,10,10,10],'cal/(mol*K)'),
        H298 = (10,'kcal/mol'),
        S298 = (10,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 118,
    label = "six-oneside-twoindoubles-25",
    group = 
"""
1   [Cs,Os] u0 {2,S} {6,S}
2   Cd      u0 {1,S} {3,D}
3   Cd      u0 {2,D} {4,S}
4 * [Cd,CO] u0 {3,S} {5,S}
5   Cd      u0 {4,S} {6,D}
6   Cd      u0 {1,S} {5,D}
""",
    thermo = u'14cyclohexadiene3methylene',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 49,
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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 47,
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
        Cpdata = ([-2.818,-2.82,-2.578,-2.314,-2.091,-1.771,-1.49],'cal/(mol*K)'),
        H298 = (-2.31,'kcal/mol'),
        S298 = (27.775,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 119,
    label = "six-oneside-twoindoubles-24",
    group = 
"""
1   [Cs,Os] u0 {2,S} {6,S}
2   Cd      u0 {1,S} {3,D}
3   Cd      u0 {2,D} {4,S}
4   Cd      u0 {3,S} {5,D}
5   Cd      u0 {4,D} {6,S}
6 * [Cd,CO] u0 {1,S} {5,S}
""",
    thermo = u'13cyclohexadiene5methylene',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 48,
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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 46,
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
        Cpdata = ([-5.437,-6.088,-5.788,-4.994,-3.626,-2.664,-1.187],'cal/(mol*K)'),
        H298 = (-4.78,'kcal/mol'),
        S298 = (28.295,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 120,
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
    thermo = u'oxylene',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 50,
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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 51,
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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 54,
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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 121,
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
    thermo = u'pxylene',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 53,
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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 52,
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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 125,
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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 101,
    label = "SevenMember",
    group = 
"""
1 * R!H u0 {2,[S,D]} {7,[S,D]}
2   R!H u0 {1,[S,D]} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,[S,D]}
4   R!H u0 {3,[S,D]} {5,[S,D]}
5   R!H u0 {4,[S,D]} {6,[S,D]}
6   R!H u0 {5,[S,D]} {7,[S,D]}
7   R!H u0 {1,[S,D]} {6,[S,D]}
""",
    thermo = u'Cycloheptane',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 55,
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
    shortDesc = u"""Cycloheptane ring BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 56,
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
    shortDesc = u"""Cycloheptene ring BENSON Cp 300K copied from cycloheptane""",
    longDesc = 
u"""

""",
)

entry(
    index = 57,
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
    shortDesc = u"""1,3-Cycloheptadiene ring BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 58,
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
    shortDesc = u"""1,3,5-Cycloheptatriene ring BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 88,
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
    shortDesc = u"""Cycloheptanone ring BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 129,
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
    shortDesc = u"""Automated Estimation of Ring Strain Energies, Gasteiger, 1978, S, Cp from Cycloheptane""",
    longDesc = 
u"""

""",
)

entry(
    index = 102,
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
    thermo = u'Cyclooctane',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 103,
    label = "1,2,4,6-Cycloheptatetraene",
    group = 
"""
1  * Cd u0 {2,D} {7,S}
2    Cdd u0 {1,D} {3,D}
3    Cd u0 {4,S} {2,D}
4    Cd u0 {3,S} {5,D}
5    Cd u0 {6,S} {4,D}
6    Cd u0 {5,S} {7,D}
7    Cd u0 {1,S} {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.6,-7.5,-7.3,-6.5,-4.9,-3.7,-2.2],'cal/(mol*K)'),
        H298 = (23.9,'kcal/mol'),
        S298 = (25.5,'cal/(mol*K)'),
    ),
    shortDesc = u"""AG Vandeputte""",
    longDesc = 
u"""
CBS-QB3 isodesmic reaction approach C7H6 + 4 ethene = allene + 3 butadiene
""",
)

entry(
    index = 156,
    label = "heptasulfur",
    group = 
"""
1 * Ss u0 {2,S} {7,S}
2   Ss u0 {1,S} {3,S}
3   Ss u0 {2,S} {4,S}
4   Ss u0 {3,S} {5,S}
5   Ss u0 {4,S} {6,S}
6   Ss u0 {5,S} {7,S}
7   Ss u0 {1,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.26,-9.91,-9.2,-8.99,-8.5,-7.55,-3.9],'cal/(mol*K)'),
        H298 = (-0.44,'kcal/mol'),
        S298 = (8.52,'cal/(mol*K)'),
    ),
    shortDesc = u"""All from NIST-JANAF table""",
    longDesc = 
u"""

""",
)

entry(
    index = 160,
    label = "oxepane",
    group =
"""
1 * C u0 {2,S} {7,S}
2   C u0 {1,S} {3,S}
3   C u0 {2,S} {4,S}
4   C u0 {3,S} {5,S}
5   C u0 {4,S} {6,S}
6   C u0 {5,S} {7,S}
7   Os u0 {1,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.10,-5.33,-3.85,-2.52,-0.92,0.26,5.83],'cal/(mol*K)'),
        H298 = (6.54,'kcal/mol'),
        S298 = (17.14,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculation: Mixture of two twist chair formations""",
    longDesc =
u"""

""",
)

entry(
    index = 59,
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
    shortDesc = u"""Updated AG Vandeputte (good agreement with BENSON correction but explicit for cyclooctane from CBS-QB3 isodesmic reaction and B3LYP/cbsb7 for S and cp, results in perfect agreement with calculations of Dorofeeva et al.)""",
    longDesc = 
u"""

""",
)

entry(
    index = 60,
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
    shortDesc = u"""Updated AG Vandeputte (CBS-QB3 isodesmic reaction and B3LYP/cbsb7 for S and cp)""",
    longDesc = 
u"""

""",
)

entry(
    index = 62,
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
    shortDesc = u"""1,3,5-Cyclooctatriene ring BENSON, S and cp from 1,4-cyclooctadiene""",
    longDesc = 
u"""

""",
)

entry(
    index = 63,
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
    shortDesc = u"""Cyclooctatetraene ring BENSON, S and cp from 1,4-cyclooctadiene""",
    longDesc = 
u"""

""",
)

entry(
    index = 89,
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
    shortDesc = u"""Cyclooctanone ring BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 126,
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
    thermo = u'1,4-cyclooctadiene',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 127,
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
    shortDesc = u"""Updated AG Vandeputte (CBS-QB3 isodesmic reaction and B3LYP/cbsb7 for S and cp)""",
    longDesc = 
u"""

""",
)

entry(
    index = 128,
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
    thermo = u'1,4-cyclooctadiene',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 157,
    label = "octasulfur",
    group = 
"""
1 * Ss u0 {2,S} {8,S}
2   Ss u0 {1,S} {3,S}
3   Ss u0 {2,S} {4,S}
4   Ss u0 {3,S} {5,S}
5   Ss u0 {4,S} {6,S}
6   Ss u0 {5,S} {7,S}
7   Ss u0 {6,S} {8,S}
8   Ss u0 {1,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.56,-10.72,-9.9,-9.63,-9.1,-8.08,-4.19],'cal/(mol*K)'),
        H298 = (-10.14,'kcal/mol'),
        S298 = (2.42,'cal/(mol*K)'),
    ),
    shortDesc = u"""All from NIST-JANAF table""",
    longDesc = 
u"""

""",
)

entry(
    index = 103,
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
    thermo = u'Cyclononane',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 64,
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
    shortDesc = u"""Cyclononane ring BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 90,
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
    shortDesc = u"""Cyclononanone ring BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 104,
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
    thermo = u'Cyclodecane',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 67,
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
    shortDesc = u"""Cyclodecane ring BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 91,
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
    shortDesc = u"""Cyclodecanone ring BENSON""",
    longDesc = 
u"""

""",
)

entry(
    index = 92,
    label = "five-inringtwodouble-12",
    group =
"""
1 * R!H u0 {2,[S,D]} {5,S}
2   R!H u0 {1,[S,D]} {3,D}
3   Cdd u0 {2,D} {4,D}
4   R!H u0 {3,D} {5,[S,D]}
5   R!H u0 {1,S} {4,[S,D]}
""",
    thermo = u'1,2-Cyclopentadiene',
    shortDesc = u"""""",
    longDesc =
u"""
For now, any 5-membered ring that has at least 2 double-bonds in the 1,2 positions will use this general correction.
""",
)

entry(
    index = 93,
    label = "Cyclopentyne",
    group =
"""
1 * Ct u0 {2,T} {5,S}
2   Ct u0 {1,T} {3,S}
3   C u0 {2,S} {4,S}
4   C u0 {3,S} {5,S}
5   C u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.441, -1.573, -1.731, -1.812, -1.511, -1.194, -3.151],'cal/(mol*K)'),
        H298 = (72.047,'kcal/mol'),
        S298 = (28.96,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted to CBS-QB3 calculation""",
    longDesc =
u"""

""",
)

entry(
    index = 94,
    label = "five-inringonetriple",
    group =
"""
1 * R!H u0 {2,T} {5,S}
2   R!H u0 {1,T} {3,S}
3   R!H u0 {2,S} {4,[S,D]}
4   R!H u0 {3,[S,D]} {5,[S,D,T]}
5   R!H u0 {1,S} {4,[S,D,T]}
""",
    thermo = u'Cyclopentyne',
    shortDesc = u"""""",
    longDesc =
u"""
Use cyclopentyne ring correction for any five-membered ring containing a triple bond.
""",
)

entry(
    index = 95,
    label = "six-inringonetriple",
    group =
"""
1 * Ct u0 {2,T} {6,S}
2   Ct u0 {1,T} {3,S}
3   R!H u0 {2,S} {4,S}
4   R!H u0 {3,S} {5,S}
5   R!H u0 {4,S} {6,S}
6   R!H u0 {1,S} {5,S}
""",
    thermo = u'cyclohexyne',
    shortDesc = u"""""",
    longDesc =
u"""
Use cyclohexyne correction for any 6-membered ring containing 1 triple bond
""",
)

entry(
    index = 96,
    label = "six-inringonetripleonedouble",
    group =
"""
1 * Ct u0 {2,T} {6,S}
2   Ct u0 {1,T} {3,S}
3   R!H u0 {2,S} {4,[S,D]}
4   R!H u0 {3,[S,D]} {5,[S,D]}
5   R!H u0 {4,[S,D]} {6,[S,D]}
6   R!H u0 {1,S} {5,[S,D]}
""",
    thermo = u'cyclohex_1_yne_3_ene',
    shortDesc = u"""""",
    longDesc =
u"""
Use cyclohex_1_yne_3_ene correction for any 6-membered ring containing at least one triple bond
and one double bond.
""",
)

entry(
    index = 97,
    label = "cyclohex_1_yne_3_ene",
    group =
"""
1 * Ct u0 {2,T} {6,S}
2   Ct u0 {1,T} {3,S}
3   Cd u0 {2,S} {4,D}
4   Cd u0 {3,D} {5,S}
5   [C,Os] u0 {4,S} {6,S}
6   [C,Os] u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.292 ,-2.038, -2.856, -3.187, -2.814, -1.639,-2.564],'cal/(mol*K)'),
        H298 = (48.034,'kcal/mol'),
        S298 = (25.6327,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3""",
    longDesc =
u"""
Fitted to CBS-QB3 calculation for cyclohex_1_yne_3_ene
""",
)

entry(
    index = 98,
    label = "six-inringtwotriple-13",
    group =
"""
1 * Ct u0 {2,T} {6,S}
2   Ct u0 {1,T} {3,S}
3   Ct u0 {2,S} {4,T}
4   Ct u0 {3,T} {5,S}
5   R!H u0 {4,S} {6,[S,D,T]}
6   R!H u0 {1,S} {5,[S,D,T]}
""",
    thermo = u'1_3_cyclohexadiyne',
    shortDesc = u"""CBS-QB3""",
    longDesc =
u"""
Use 1_3_cyclohexadiyne correction for any six-membered  ring with at least two triple bonds
""",
)

entry(
    index = 99,
    label = "1,2-Cyclopentadiene",
    group =
"""
1 * C u0 {2,S} {5,S}
2   Cd u0 {1,S} {3,D}
3   Cdd u0 {2,D} {4,D}
4   Cd u0 {3,D} {5,S}
5   C u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.610227533, -3.220365201, -2.9183174, -2.860732314, -2.503231358, -1.669783939, -1.310015296],'cal/(mol*K)'),
        H298 = (65.85343212,'kcal/mol'),
        S298 = (26.75230402,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted to M06 calculation""",
    longDesc =
u"""

""",
)

entry(
    index = 153,
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
    shortDesc = u"""CBS-QB3 isodesmic reaction approach allene + 2-butene = cyclopentatriene + 2 CH4, DHr = 220.8 kJ mol-1, exp data from NIST""",
    longDesc =
u"""

""",
)

entry(
    index = 154,
    label = "cyclohexyne",
    group =
"""
1 * Ct u0 {2,T} {6,S}
2   Ct u0 {1,T} {3,S}
3   [C,Os] u0 {2,S} {4,S}
4   [C,Os] u0 {3,S} {5,S}
5   [C,Os] u0 {4,S} {6,S}
6   [C,Os] u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.306, -2.849, -2.452, -2.229, -1.543, -0.932, -2.535],'cal/(mol*K)'),
        H298 = (39.857,'kcal/mol'),
        S298 = (21.862,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3""",
    longDesc =
u"""
Fitted to CBS-QB3 calculation for cyclohexyne
""",
)

entry(
    index = 155,
    label = "cyclohex_1_yne_4_ene",
    group =
"""
1 * Ct u0 {2,T} {6,S}
2   Ct u0 {1,T} {3,S}
3   [C,Os] u0 {2,S} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   [C,Os] u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.431, -0.775, -1.308, -1.515, -1.294, -0.369, -1.036],'cal/(mol*K)'),
        H298 = (38.484,'kcal/mol'),
        S298 = (25.2137,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3""",
    longDesc =
u"""
Fitted to CBS-QB3 calculation for cyclohex_1_yne_4_ene
""",
)

entry(
    index = 156,
    label = "1_3_cyclohexadiyne",
    group =
"""
1 * Ct u0 {2,T} {6,S}
2   Ct u0 {1,T} {3,S}
3   Ct u0 {2,S} {4,T}
4   Ct u0 {3,T} {5,S}
5   [C,Os] u0 {4,S} {6,S}
6   [C,Os] u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.086,-1.458,-1.692,-1.747,-1.465,-1.403,-3.712],'cal/(mol*K)'),
        H298 = (103.484,'kcal/mol'),
        S298 = (31.221,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3""",
    longDesc =
u"""
Fitted to CBS-QB3 calculation for 1_3_cyclohexadiyne
""",
)

entry(
    index = 157,
    label = "124cyclohexatriene",
    group =
"""
1   Cd      u0 {2,D} {6,S}
2 * Cdd     u0 {1,D} {3,D}
3   Cd      u0 {2,D} {4,S}
4   [Cs,Os] u0 {3,S} {5,S}
5   Cd      u0 {4,S} {6,D}
6   Cd      u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.21,-4.32,-3.9,-3.46,-2.71,-2.25,-1.38],'cal/(mol*K)'),
        H298 = (36.04,'kcal/mol'),
        S298 = (26.47,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 isodesmic reaction approach C1=CC=CCC=1 + 3 ethane + ethene = allene + 2 2-butene + propane""",
    longDesc =
u"""

""",
)

entry(
    index = 158,
    label = "Cyclopropyne",
    group =
"""
1 * Ct u0 {2,T} {3,S}
2   Ct u0 {1,T} {3,S}
3   R!H u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([2.22, 1.515, 0.554, -0.319, -1.215, -1.31, -2.439],'cal/(mol*K)'),
        H298 = (111.641,'kcal/mol'),
        S298 = (37.345,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
Fitted to M06 calculations
""",
)


entry(
    index = 159,
    label = "six-inringthreedouble_123",
    group =
"""
1   Cdd     u0 {2,D} {6,D}
2 * Cdd     u0 {1,D} {3,D}
3   R!H      u0 {2,D} {4,[S,D]}
4   R!H u0 {3,[S,D]} {5,[S,D]}
5   R!H      u0 {4,[S,D]} {6,[S,D]}
6   R!H      u0 {1,D} {5,[S,D]}
""",
    thermo = u'123cyclohexatriene',
    shortDesc = u"""""",
    longDesc =
u"""
Use 123cyclohexatriene correction for any 6-membered ring that contains at least 3 double bonds in the 1,2 and 3
positions.
""",
)

entry(
    index = 160,
    label = "123cyclohexatriene",
    group =
"""
1   Cdd      u0 {2,D} {6,D}
2 * Cdd     u0 {1,D} {3,D}
3   Cd      u0 {2,D} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs      u0 {4,S} {6,S}
6   Cd      u0 {1,D} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.033, -4.022, -3.919, -3.755, -3.149 ,-2.312, -1.645],'cal/(mol*K)'),
        H298 = (50.291,'kcal/mol'),
        S298 = (27.334,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
Fitted to M06 calculations
""",
)

entry(
    index = 161,
    label = "four-inringonedouble",
    group =
"""
1 * R!H u0 {2,D} {4,S}
2   R!H u0 {1,D} {3,S}
3   R!H u0 {2,S} {4,S}
4   R!H u0 {1,S} {3,S}
""",
    thermo = u'Cyclobutene',
    shortDesc = u"""""",
    longDesc =
u"""
Use cyclobutene correction for any four membered ring with one double bond
""",
)

entry(
    index = 162,
    label = "four-inringtwodouble",
    group =
"""
1   R!H u0 {2,D} {4,[S,D]}
2 * R!H u0 {1,D} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,D}
4   R!H u0 {1,[S,D]} {3,D}
""",
    thermo = u'cyclobutadiene_13',
    shortDesc = u"""""",
    longDesc =
u"""
Use cyclobutadiene_13 correction for any four membered ring with at least two double bonds in the 1,3-positions
""",
)

entry(
    index = 163,
    label = "cyclobutadiene_12",
    group =
"""
1   R!H u0 {2,D} {4,S}
2 * R!H u0 {1,D} {3,D}
3   R!H u0 {2,D} {4,S}
4   R!H u0 {1,S} {3,S}
""",
    thermo = u'cyclobutadiene_13',
    shortDesc = u"""""",
    longDesc =
u"""
Use cyclobutadiene_13 correction for 1,2_CBD
""",
)

tree(
"""
L1: Ring
    L2: Aromatic
        L3: Benzene
    L2: ThreeMember
        L3: Cyclopropane
        L3: Cyclopropene
        L3: Cyclopropadiene
        L3: Cyclopropyne
		L3: oxirene
        L3: Cyclopropatriene
        L3: Ethylene_oxide
        L3: dioxirane
        L3: 2(co)oxirane
        L3: cyclopropanedione
        L3: cyclopropenone
        L3: thiirane
        L3: dithiirane
        L3: trithiirane
        L3: thiirene
        L3: Ethyleneimine
        L3: Methylene_cyclopropane
        L3: cyclopropanone
        L3: methylenecyclopropene
        L3: methylenecyclopropanone
        L3: methyleneoxirane
        L3: 12Methylenecyclopropane
    L2: FourMember
        L3: Cyclobutane
        L3: four-inringonedouble
            L4: Cyclobutene
        L3: Oxetane
		L3: Oxetene
        L3: Beta-Propiolactone
        L3: Cyclobutanone
        L3: 12dioxetane
        L3: dioxerene
        L3: four-inringtwodouble
            L4: cyclobutadiene_13
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
        L3: six-inringonetripleonedouble
            L4: cyclohex_1_yne_4_ene
            L4: cyclohex_1_yne_3_ene
        L3: six-inringtwotriple-13
            L4: 1_3_cyclohexadiyne
    L2: SevenMember
        L3: Cycloheptane
        L3: Cycloheptene
        L3: 1,3-Cycloheptadiene
        L3: 1,3,5-Cycloheptatriene
        L3: Cycloheptanone
        L3: 1,4-Cycloheptadiene
        L3: 1,2,4,6-Cycloheptatetraene
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

