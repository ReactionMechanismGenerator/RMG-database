#!/usr/bin/env python
# encoding: utf-8

name = "Radical Corrections"
shortDesc = u""
longDesc = u"""

"""
entry(
    index        = 0,
    label        = "Radical",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * R U{1,2,3,4}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 1,
    label        = "RJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * R U1
""",
    thermo = u'CJ',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 2,
    label        = "CJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1
""",
    thermo = u'CsJ',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 3,
    label        = "CsJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U1
""",
    thermo = u'Cs_P',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 4,
    label        = "CH3",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   H U0 {1,S}
3   H U0 {1,S}
4   H U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.71,0.34,-0.33,-1.07,-2.43,-3.54,-5.43],'cal/(mol*K)'),
        H298 = (104.81,'kcal/mol','+|-',0.1),
        S298 = (0.52,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated in relation to methane from NIST values""",
    longDesc = 
u"""

""",
)

entry(
    index        = 5,
    label        = "Cs_P",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   C U0 {1,S}
3   H U0 {1,S}
4   H U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.77,-1.36,-1.91,-2.4,-3.16,-3.74,-4.66],'cal/(mol*K)'),
        H298 = (101.1,'kcal/mol'),
        S298 = (2.61,'cal/(mol*K)'),
    ),
    shortDesc = u"""Generic primary radical. (CHEN & BOZZELLI) #""",
    longDesc = 
u"""

""",
)

entry(
    index        = 6,
    label        = "CsCsJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Cs U0 {1,S}
3   H  U0 {1,S}
4   H  U0 {1,S}
""",
    thermo = u'Cs_P',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 11,
    label        = "CJCOOH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Cs U0 {1,S} {5,S}
3   H  U0 {1,S}
4   H  U0 {1,S}
5   O  U0 {2,S} {6,S}
6   Os U0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.25,-0.76,-1.34,-1.91,-2.87,-3.6,-4.69],'cal/(mol*K)'),
        H298 = (103.26,'kcal/mol'),
        S298 = (3.54,'cal/(mol*K)'),
    ),
    shortDesc = u"""WIJAYA et al.""",
    longDesc = 
u"""

""",
)

entry(
    index        = 7,
    label        = "CCJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   C U0 {1,S} {5,S} {6,S} {7,S}
3   H U0 {1,S}
4   H U0 {1,S}
5   H U0 {2,S}
6   H U0 {2,S}
7   H U0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.65,-1.21,-1.75,-2.24,-3.02,-3.63,-3.63],'cal/(mol*K)'),
        H298 = (101.1,'kcal/mol','+|-',0.2),
        S298 = (2.61,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
)

entry(
    index        = 8,
    label        = "RCCJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   C U0 {1,S} {5,S} {6,S} {7,S}
3   H U0 {1,S}
4   H U0 {1,S}
5   C U0 {2,S}
6   H U0 {2,S}
7   H U0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.77,-1.36,-1.91,-2.4,-3.16,-3.74,-4.66],'cal/(mol*K)'),
        H298 = (101.1,'kcal/mol','+|-',0.2),
        S298 = (2.61,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
u"""

""",
)

entry(
    index        = 9,
    label        = "Isobutyl",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   C U0 {1,S} {5,S} {6,S} {7,S}
3   H U0 {1,S}
4   H U0 {1,S}
5   C U0 {2,S}
6   C U0 {2,S}
7   H U0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.54,-1.26,-1.92,-2.46,-3.27,-3.84,-3.84],'cal/(mol*K)'),
        H298 = (101.1,'kcal/mol'),
        S298 = (2.91,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
)

entry(
    index        = 10,
    label        = "Neopentyl",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   C U0 {1,S} {5,S} {6,S} {7,S}
3   H U0 {1,S}
4   H U0 {1,S}
5   C U0 {2,S}
6   C U0 {2,S}
7   C U0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.59,-1.32,-2.05,-2.65,-3.5,-4.06,-4.87],'cal/(mol*K)'),
        H298 = (101.1,'kcal/mol'),
        S298 = (3.03,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
u"""

""",
)

entry(
    index        = 12,
    label        = "Benzyl_P",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Cb U0 {1,S}
3   H  U0 {1,S}
4   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.75,0.6,0.13,-0.42,-1.41,-2.18,-2.18],'cal/(mol*K)'),
        H298 = (88.5,'kcal/mol','+|-',0.1),
        S298 = (-4.74,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
)

entry(
    index        = 13,
    label        = "Allyl_P",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Cd U0 {1,S}
3   H  U0 {1,S}
4   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.62,-0.56,-0.78,-1.12,-1.84,-2.46,-3.49],'cal/(mol*K)'),
        H298 = (88.2,'kcal/mol'),
        S298 = (-2.56,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
u"""

""",
)

entry(
    index        = 14,
    label        = "C=CC=CCJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Cd U0 {1,S} {5,D}
3   H  U0 {1,S}
4   H  U0 {1,S}
5   C  U0 {2,D} {6,S}
6   Cd U0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.83,-1.86,-1.98,-1.99,-2.3,-2.5,-2.5],'cal/(mol*K)'),
        H298 = (80,'kcal/mol'),
        S298 = (-1.55,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
)

entry(
    index        = 15,
    label        = "CTCC=CCJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Cd U0 {1,S} {5,D}
3   H  U0 {1,S}
4   H  U0 {1,S}
5   C  U0 {2,D} {6,S}
6   Ct U0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.09,-1.62,-2.01,-2.63,-3.07,-3.48,-3.48],'cal/(mol*K)'),
        H298 = (81,'kcal/mol'),
        S298 = (-3.55,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
)

entry(
    index        = 17,
    label        = "Propargyl",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Ct U0 {1,S}
3   H  U0 {1,S}
4   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.84,-1.17,-1.56,-1.95,-2.7,-3.31,-5.31],'cal/(mol*K)'),
        H298 = (89.4,'kcal/mol'),
        S298 = (-0.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
u"""

""",
)

entry(
    index        = 16,
    label        = "C2JC=O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   CO U0 {1,S} {5,D} {6,S}
3   H  U0 {1,S}
4   H  U0 {1,S}
5   O  U0 {2,D}
6   C  U0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.32,0.19,-0.15,-0.57,-1.43,-2.22,-3.67],'cal/(mol*K)'),
        H298 = (94.4,'kcal/mol'),
        S298 = (-1.16,'cal/(mol*K)'),
    ),
    shortDesc = u"""CHEN & BOZZELLI""",
    longDesc = 
u"""

""",
)

entry(
    index        = 18,
    label        = "Cs_S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   C U0 {1,S}
3   C U0 {1,S}
4   H U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.5,-2.33,-3.1,-3.39,-3.75,-4.45,-5.2],'cal/(mol*K)'),
        H298 = (98.45,'kcal/mol'),
        S298 = (4.44,'cal/(mol*K)'),
    ),
    shortDesc = u"""Generic secondary radical. (CHEN & BOZZELLI) #""",
    longDesc = 
u"""

""",
)

entry(
    index        = 19,
    label        = "(Cs)2CsJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Cs U0 {1,S}
3   Cs U0 {1,S}
4   H  U0 {1,S}
""",
    thermo = u'Cs_S',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 142,
    label        = "cyclopropane",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U1 {2,S} {3,S} {4,S}
2   Cs U0 {1,S} {3,S}
3   Cs U0 {1,S} {2,S}
4   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (106,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""D.F. McMillen, D.M. Golden, HYDROCARBON BOND-DISSOCIATION ENERGIES, Annual Review of Physical Chemistry, 33 (1982) 493-532.. S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 143,
    label        = "cyclobutane",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U1 {2,S} {4,S} {5,S}
2   Cs U0 {1,S} {3,S}
3   Cs U0 {2,S} {4,S}
4   Cs U0 {1,S} {3,S}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (96.9,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Tian, Z.; Fattahi, A.; Lis, L.; Kass, S. R., "Cycloalkane and Cycloalkene C-H Bond Dissociation Energies," J. Am. Chem. Soc. 2006, 128, 17087-17092, DOI: 10.1021/ja065348u. S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 152,
    label        = "bicyclo[1.1.0]butane-secondary",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   Cs U0 {2,S} {3,S} {4,S}
2   Cs U0 {1,S} {3,S} {4,S}
3 * Cs U1 {1,S} {2,S} {5,S}
4   Cs U0 {1,S} {2,S}
5   H  U0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (101.1,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 23,
    label        = "CCJCOOH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Cs U0 {1,S} {5,S}
3   Cs U0 {1,S}
4   H  U0 {1,S}
5   O  U0 {2,S} {6,S}
6   O  U0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.65,-1.4,-2,-2.5,-3.27,-3.84,-4.73],'cal/(mol*K)'),
        H298 = (99.98,'kcal/mol'),
        S298 = (4.79,'cal/(mol*K)'),
    ),
    shortDesc = u"""WIJAYA et al.""",
    longDesc = 
u"""

""",
)

entry(
    index        = 151,
    label        = "spiro[2.2]pentane-secondary",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   Cs U0 {2,S} {3,S} {4,S} {5,S}
2 * Cs U1 {1,S} {3,S} {6,S}
3   Cs U0 {1,S} {2,S}
4   Cs U0 {1,S} {5,S}
5   Cs U0 {1,S} {4,S}
6   H  U0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (107.3,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 153,
    label        = "bicyclo[2.1.0]pentane-secondary-C4",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   Cs U0 {2,S} {3,S} {5,S}
2   Cs U0 {1,S} {3,S} {4,S}
3   Cs U0 {1,S} {2,S}
4   Cs U0 {2,S} {5,S}
5 * Cs U1 {1,S} {4,S} {6,S}
6   H  U0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (99.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 154,
    label        = "bicyclo[2.1.0]pentane-secondary-C3",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   Cs U0 {2,S} {3,S} {5,S}
2   Cs U0 {1,S} {3,S} {4,S}
3 * Cs U1 {1,S} {2,S} {6,S}
4   Cs U0 {2,S} {5,S}
5   Cs U0 {1,S} {4,S}
6   H  U0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (105.9,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 179,
    label        = "cyclopentene-4",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U1 {2,S} {3,S} {6,S}
2   Cs U0 {1,S} {5,S}
3   Cs U0 {1,S} {4,S}
4   C  U0 {3,S} {5,D}
5   C  U0 {2,S} {4,D}
6   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (96.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Allyl_S""",
    longDesc = 
u"""

""",
)

entry(
    index        = 185,
    label        = "bicyclo[2.1.0]pent-2-ene-C5",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   Cs U0 {2,S} {3,S} {5,S}
2   Cs U0 {1,S} {3,S} {4,S}
3 * C  U1 {1,S} {2,S} {6,S}
4   C  U0 {2,S} {5,D}
5   C  U0 {1,S} {4,D}
6   H  U0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (106.9,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 196,
    label        = "bicyclo[1.1.1]pentane-C2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   Cs U0 {3,S} {4,S} {5,S}
2   Cs U0 {3,S} {4,S} {5,S}
3 * C  U1 {1,S} {2,S} {6,S}
4   C  U0 {1,S} {2,S}
5   C  U0 {1,S} {2,S}
6   H  U0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (106.5,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 197,
    label        = "tricyclo[1.1.1.0(1,3)]pentane-C2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   Cs U0 {2,S} {3,S} {4,S} {5,S}
2   Cs U0 {1,S} {3,S} {4,S} {5,S}
3 * C  U1 {1,S} {2,S} {6,S}
4   C  U0 {1,S} {2,S}
5   C  U0 {1,S} {2,S}
6   H  U0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (111.5,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 155,
    label        = "bicyclo[3.1.0]hexane-C5-2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   Cs U0 {2,S} {3,S} {5,S}
2   Cs U0 {1,S} {3,S} {4,S}
3   Cs U0 {1,S} {2,S}
4 * Cs U1 {2,S} {6,S} {7,S}
5   Cs U0 {1,S} {6,S}
6   Cs U0 {4,S} {5,S}
7   H  U0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (93.6,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 156,
    label        = "bicyclo[3.1.0]hexane-C5-3",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   Cs U0 {2,S} {3,S} {5,S} {7,S}
2   Cs U0 {1,S} {3,S} {4,S}
3   Cs U0 {1,S} {2,S}
4   Cs U0 {2,S} {6,S}
5   Cs U0 {1,S} {6,S}
6 * Cs U1 {4,S} {5,S}
7   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (94.1,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 157,
    label        = "bicyclo[3.1.0]hexane-C3",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   Cs U0 {2,S} {3,S} {5,S}
2   Cs U0 {1,S} {3,S} {4,S}
3 * Cs U1 {1,S} {2,S} {7,S}
4   Cs U0 {2,S} {6,S}
5   Cs U0 {1,S} {6,S}
6   Cs U0 {4,S} {5,S}
7   H  U0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (108.3,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 158,
    label        = "bicyclo[2.2.0]hexane-secondary",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   Cs U0 {2,S} {3,S} {6,S}
2   Cs U0 {1,S} {4,S} {5,S}
3 * Cs U1 {1,S} {4,S} {7,S}
4   Cs U0 {2,S} {3,S}
5   Cs U0 {2,S} {6,S}
6   Cs U0 {1,S} {5,S}
7   H  U0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (98.6,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 188,
    label        = "bicyclo[2.1.1]hex-2-ene-C5",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   Cs U0 {3,S} {4,S} {6,S}
2   Cs U0 {3,S} {4,S} {5,S}
3 * C  U1 {1,S} {2,S} {7,S}
4   C  U0 {1,S} {2,S}
5   C  U0 {2,S} {6,D}
6   C  U0 {1,S} {5,D}
7   H  U0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (104.8,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 190,
    label        = "tricyclo[2.1.1.0(1,4)]hex-2-ene-C5",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   Cs U0 {2,S} {3,S} {4,S} {6,S}
2   Cs U0 {1,S} {3,S} {4,S} {5,S}
3 * C  U1 {1,S} {2,S} {7,S}
4   C  U0 {1,S} {2,S}
5   C  U0 {2,S} {6,D}
6   C  U0 {1,S} {5,D}
7   H  U0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (105.2,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 199,
    label        = "bicyclo[2.1.1]hexane-C2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   C  U0 {3,S} {4,S} {6,S}
2   Cs U0 {3,S} {4,S} {5,S}
3   C  U0 {1,S} {2,S}
4   C  U0 {1,S} {2,S}
5 * C  U1 {2,S} {6,S} {7,S}
6   Cs U0 {1,S} {5,S}
7   H  U0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (100.8,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 200,
    label        = "bicyclo[2.1.1]hexane-C5",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   Cs U0 {3,S} {4,S} {6,S}
2   Cs U0 {3,S} {4,S} {5,S}
3 * C  U1 {1,S} {2,S} {7,S}
4   C  U0 {1,S} {2,S}
5   C  U0 {2,S} {6,S}
6   C  U0 {1,S} {5,S}
7   H  U0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (105.4,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 201,
    label        = "tricyclo[2.1.1.0(1,4)]hexane-C2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   C  U0 {2,S} {3,S} {4,S} {6,S}
2   Cs U0 {1,S} {3,S} {4,S} {5,S}
3   C  U0 {1,S} {2,S}
4   C  U0 {1,S} {2,S}
5 * C  U1 {2,S} {6,S} {7,S}
6   Cs U0 {1,S} {5,S}
7   H  U0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (100.1,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 202,
    label        = "tricyclo[2.1.1.0(1,4)]hexane-C5",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   Cs U0 {2,S} {3,S} {4,S} {6,S}
2   Cs U0 {1,S} {3,S} {4,S} {5,S}
3 * C  U1 {1,S} {2,S} {7,S}
4   C  U0 {1,S} {2,S}
5   C  U0 {2,S} {6,S}
6   C  U0 {1,S} {5,S}
7   H  U0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (103.4,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 140,
    label        = "7-norbornyl",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   Cs U0 {3,S} {4,S} {7,S}
2   Cs U0 {3,S} {5,S} {6,S}
3 * Cs U1 {1,S} {2,S} {8,S}
4   Cs U0 {1,S} {5,S}
5   Cs U0 {2,S} {4,S}
6   Cs U0 {2,S} {7,S}
7   Cs U0 {1,S} {6,S}
8   H  U0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (98.8,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""P.M. Nunes, S.G. Estacio, G.T. Lopes, B.J. Costa Cabral, R.M. Borges dos Santos, J.A. Martinho Simoes, CH Bond Dissociation Enthalpies in Norbornane. An Experimental and Computational Study, Organic Letters, 10 (2008) 1613-1616. S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 141,
    label        = "2-norbornyl",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   Cs U0 {3,S} {4,S} {7,S} {8,S}
2   Cs U0 {3,S} {5,S} {6,S}
3   Cs U0 {1,S} {2,S}
4 * Cs U1 {1,S} {5,S}
5   Cs U0 {2,S} {4,S}
6   Cs U0 {2,S} {7,S}
7   Cs U0 {1,S} {6,S}
8   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (105.02,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""P.M. Nunes, S.G. Estacio, G.T. Lopes, B.J. Costa Cabral, R.M. Borges dos Santos, J.A. Martinho Simoes, CH Bond Dissociation Enthalpies in Norbornane. An Experimental and Computational Study, Organic Letters, 10 (2008) 1613-1616. S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 150,
    label        = "cycloheptane",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U1 {2,S} {7,S} {8,S}
2   Cs U0 {1,S} {3,S}
3   Cs U0 {2,S} {4,S}
4   Cs U0 {3,S} {5,S}
5   Cs U0 {4,S} {6,S}
6   Cs U0 {5,S} {7,S}
7   Cs U0 {1,S} {6,S}
8   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (92.5,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 159,
    label        = "bicyclo[3.2.0]heptane-C5-2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   Cs U0 {2,S} {3,S} {6,S}
2   Cs U0 {1,S} {4,S} {5,S}
3   Cs U0 {1,S} {4,S}
4   Cs U0 {2,S} {3,S}
5 * Cs U1 {2,S} {7,S} {8,S}
6   Cs U0 {1,S} {7,S}
7   Cs U0 {5,S} {6,S}
8   H  U0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.9,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 160,
    label        = "bicyclo[3.2.0]heptane-C5-3",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   Cs U0 {2,S} {3,S} {6,S}
2   Cs U0 {1,S} {4,S} {5,S}
3   Cs U0 {1,S} {4,S}
4   Cs U0 {2,S} {3,S}
5   Cs U0 {2,S} {7,S}
6   Cs U0 {1,S} {7,S}
7 * Cs U1 {5,S} {6,S} {8,S}
8   H  U0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (99.5,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 161,
    label        = "bicyclo[3.2.0]heptane-C5-6",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   Cs U0 {2,S} {3,S} {6,S}
2   Cs U0 {1,S} {4,S} {5,S}
3 * Cs U1 {1,S} {4,S} {8,S}
4   Cs U0 {2,S} {3,S}
5   Cs U0 {2,S} {7,S}
6   Cs U0 {1,S} {7,S}
7   Cs U0 {5,S} {6,S}
8   H  U0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (99,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 170,
    label        = "bicyclo[4.1.0]heptane-C6-2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   C  U0 {2,S} {3,S} {5,S}
2   Cs U0 {1,S} {3,S} {4,S}
3   C  U0 {1,S} {2,S}
4 * C  U1 {2,S} {6,S} {8,S}
5   C  U0 {1,S} {7,S}
6   Cs U0 {4,S} {7,S}
7   C  U0 {5,S} {6,S}
8   H  U0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (94.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 171,
    label        = "bicyclo[4.1.0]heptane-C6-3",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   C  U0 {2,S} {3,S} {5,S}
2   C  U0 {1,S} {3,S} {4,S}
3   C  U0 {1,S} {2,S}
4   Cs U0 {2,S} {6,S}
5   C  U0 {1,S} {7,S}
6 * Cs U1 {4,S} {7,S} {8,S}
7   Cs U0 {5,S} {6,S}
8   H  U0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.6,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 172,
    label        = "bicyclo[4.1.0]heptane-C3-7",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   Cs U0 {2,S} {3,S} {5,S}
2   Cs U0 {1,S} {3,S} {4,S}
3 * C  U1 {1,S} {2,S} {8,S}
4   C  U0 {2,S} {6,S}
5   C  U0 {1,S} {7,S}
6   C  U0 {4,S} {7,S}
7   C  U0 {5,S} {6,S}
8   H  U0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (108.1,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 170,
    label        = "bicyclo[4.1.0]heptane-C6-2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   C  U0 {2,S} {3,S} {5,S}
2   Cs U0 {1,S} {3,S} {4,S}
3   C  U0 {1,S} {2,S}
4 * C  U1 {2,S} {6,S} {8,S}
5   C  U0 {1,S} {7,S}
6   Cs U0 {4,S} {7,S}
7   C  U0 {5,S} {6,S}
8   H  U0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (94.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 171,
    label        = "bicyclo[4.1.0]heptane-C6-3",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   C  U0 {2,S} {3,S} {5,S}
2   C  U0 {1,S} {3,S} {4,S}
3   C  U0 {1,S} {2,S}
4   Cs U0 {2,S} {6,S}
5   C  U0 {1,S} {7,S}
6 * Cs U1 {4,S} {7,S} {8,S}
7   Cs U0 {5,S} {6,S}
8   H  U0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.6,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 172,
    label        = "bicyclo[4.1.0]heptane-C3-7",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   Cs U0 {2,S} {3,S} {5,S}
2   Cs U0 {1,S} {3,S} {4,S}
3 * C  U1 {1,S} {2,S} {8,S}
4   C  U0 {2,S} {6,S}
5   C  U0 {1,S} {7,S}
6   C  U0 {4,S} {7,S}
7   C  U0 {5,S} {6,S}
8   H  U0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (108.1,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 204,
    label        = "bicyclo[3.1.1]heptane-C2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   C  U0 {3,S} {4,S} {6,S}
2   Cs U0 {3,S} {4,S} {5,S}
3   C  U0 {1,S} {2,S}
4   C  U0 {1,S} {2,S}
5 * C  U1 {2,S} {7,S} {8,S}
6   C  U0 {1,S} {7,S}
7   Cs U0 {5,S} {6,S}
8   H  U0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.6,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 205,
    label        = "bicyclo[3.1.1]heptane-C3",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   C  U0 {3,S} {4,S} {6,S}
2   C  U0 {3,S} {4,S} {5,S}
3   C  U0 {1,S} {2,S}
4   C  U0 {1,S} {2,S}
5   Cs U0 {2,S} {7,S}
6   Cs U0 {1,S} {7,S}
7 * C  U1 {5,S} {6,S} {8,S}
8   H  U0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.3,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 206,
    label        = "bicyclo[3.1.1]heptane-C6",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   Cs U0 {3,S} {4,S} {6,S}
2   Cs U0 {3,S} {4,S} {5,S}
3 * C  U1 {1,S} {2,S} {8,S}
4   C  U0 {1,S} {2,S}
5   C  U0 {2,S} {7,S}
6   C  U0 {1,S} {7,S}
7   C  U0 {5,S} {6,S}
8   H  U0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (103,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 207,
    label        = "tricyclo[3.1.1.0(1,5)]heptane-C2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   C  U0 {2,S} {3,S} {4,S} {6,S}
2   Cs U0 {1,S} {3,S} {4,S} {5,S}
3   C  U0 {1,S} {2,S}
4   C  U0 {1,S} {2,S}
5 * C  U1 {2,S} {7,S} {8,S}
6   C  U0 {1,S} {7,S}
7   Cs U0 {5,S} {6,S}
8   H  U0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (98.5,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 208,
    label        = "tricyclo[3.1.1.0(1,5)]heptane-C3",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   C  U0 {2,S} {3,S} {4,S} {6,S}
2   C  U0 {1,S} {3,S} {4,S} {5,S}
3   C  U0 {1,S} {2,S}
4   C  U0 {1,S} {2,S}
5   Cs U0 {2,S} {7,S}
6   Cs U0 {1,S} {7,S}
7 * C  U1 {5,S} {6,S} {8,S}
8   H  U0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 209,
    label        = "tricyclo[3.1.1.0(1,5)]heptane-C6",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   Cs U0 {2,S} {3,S} {4,S} {6,S}
2   Cs U0 {1,S} {3,S} {4,S} {5,S}
3 * C  U1 {1,S} {2,S} {8,S}
4   C  U0 {1,S} {2,S}
5   C  U0 {2,S} {7,S}
6   C  U0 {1,S} {7,S}
7   C  U0 {5,S} {6,S}
8   H  U0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (100,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 210,
    label        = "tricyclo[2.2.1.0(1,4)]heptane-C2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   C  U0 {2,S} {3,S} {5,S} {7,S}
2   Cs U0 {1,S} {3,S} {4,S} {6,S}
3   C  U0 {1,S} {2,S}
4 * C  U1 {2,S} {5,S} {8,S}
5   Cs U0 {1,S} {4,S}
6   C  U0 {2,S} {7,S}
7   C  U0 {1,S} {6,S}
8   H  U0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (96.8,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 211,
    label        = "tricyclo[2.2.1.0(1,4)]heptane-C7",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   Cs U0 {2,S} {3,S} {5,S} {7,S}
2   Cs U0 {1,S} {3,S} {4,S} {6,S}
3 * C  U1 {1,S} {2,S} {8,S}
4   C  U0 {2,S} {5,S}
5   C  U0 {1,S} {4,S}
6   C  U0 {2,S} {7,S}
7   C  U0 {1,S} {6,S}
8   H  U0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (106.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 173,
    label        = "octahydro-pentalene-C5-2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   Cs U0 {2,S} {3,S} {4,S}
2   C  U0 {1,S} {5,S} {6,S}
3 * C  U1 {1,S} {8,S} {9,S}
4   C  U0 {1,S} {7,S}
5   C  U0 {2,S} {7,S}
6   C  U0 {2,S} {8,S}
7   C  U0 {4,S} {5,S}
8   Cs U0 {3,S} {6,S}
9   H  U0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.8,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 174,
    label        = "octahydro-pentalene-C5-3",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   C  U0 {2,S} {3,S} {4,S}
2   C  U0 {1,S} {5,S} {6,S}
3   C  U0 {1,S} {8,S}
4   Cs U0 {1,S} {7,S}
5   Cs U0 {2,S} {7,S}
6   C  U0 {2,S} {8,S}
7 * C  U1 {4,S} {5,S} {9,S}
8   C  U0 {3,S} {6,S}
9   H  U0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (98.1,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 175,
    label        = "bicyclo[4.2.0]octane-C6-2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   C  U0 {2,S} {3,S} {6,S}
2   Cs U0 {1,S} {4,S} {5,S}
3   C  U0 {1,S} {4,S}
4   C  U0 {2,S} {3,S}
5 * C  U1 {2,S} {7,S} {9,S}
6   C  U0 {1,S} {8,S}
7   Cs U0 {5,S} {8,S}
8   C  U0 {6,S} {7,S}
9   H  U0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (96.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 176,
    label        = "bicyclo[4.2.0]octane-C6-3",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   C  U0 {2,S} {3,S} {6,S}
2   C  U0 {1,S} {4,S} {5,S}
3   C  U0 {1,S} {4,S}
4   C  U0 {2,S} {3,S}
5   Cs U0 {2,S} {7,S}
6   C  U0 {1,S} {8,S}
7 * C  U1 {5,S} {8,S} {9,S}
8   Cs U0 {6,S} {7,S}
9   H  U0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (99,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 177,
    label        = "bicyclo[4.2.0]octane-C4-7",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   Cs U0 {2,S} {3,S} {6,S}
2   C  U0 {1,S} {4,S} {5,S}
3 * C  U1 {1,S} {4,S} {9,S}
4   Cs U0 {2,S} {3,S}
5   C  U0 {2,S} {7,S}
6   C  U0 {1,S} {8,S}
7   C  U0 {5,S} {8,S}
8   C  U0 {6,S} {7,S}
9   H  U0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (100.7,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 213,
    label        = "bicyclo[2.2.2]octane-C2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   Cs U0 {3,S} {6,S} {8,S}
2   C  U0 {4,S} {5,S} {7,S}
3 * C  U1 {1,S} {4,S} {9,S}
4   Cs U0 {2,S} {3,S}
5   C  U0 {2,S} {6,S}
6   C  U0 {1,S} {5,S}
7   C  U0 {2,S} {8,S}
8   C  U0 {1,S} {7,S}
9   H  U0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (97.8,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 214,
    label        = "tricyclo[2.2.2.0(1,4)]octane-C2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   C  U0 {2,S} {4,S} {6,S} {8,S}
2   Cs U0 {1,S} {3,S} {5,S} {7,S}
3 * C  U1 {2,S} {4,S} {9,S}
4   Cs U0 {1,S} {3,S}
5   C  U0 {2,S} {6,S}
6   C  U0 {1,S} {5,S}
7   C  U0 {2,S} {8,S}
8   C  U0 {1,S} {7,S}
9   H  U0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (99.3,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from CCJC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 20,
    label        = "CCJC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * C U1 {2,S} {3,S} {4,S}
2    C U0 {1,S} {5,S} {6,S} {7,S}
3    C U0 {1,S} {8,S} {9,S} {10,S}
4    H U0 {1,S}
5    H U0 {2,S}
6    H U0 {2,S}
7    H U0 {2,S}
8    H U0 {3,S}
9    H U0 {3,S}
10   H U0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.3,-2.36,-3.02,-3.44,-3.98,-4.36,-4.99],'cal/(mol*K)'),
        H298 = (98.45,'kcal/mol','+|-',0.2),
        S298 = (4.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
u"""

""",
)

entry(
    index        = 21,
    label        = "RCCJC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * C U1 {2,S} {3,S} {4,S}
2    C U0 {1,S} {5,S} {6,S} {7,S}
3    C U0 {1,S} {8,S} {9,S} {10,S}
4    H U0 {1,S}
5    C U0 {2,S}
6    H U0 {2,S}
7    H U0 {2,S}
8    H U0 {3,S}
9    H U0 {3,S}
10   H U0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.54,-2.77,-3.49,-3.9,-4.35,-4.64,-4.64],'cal/(mol*K)'),
        H298 = (98.45,'kcal/mol'),
        S298 = (5.13,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
)

entry(
    index        = 22,
    label        = "RCCJCC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * C U1 {2,S} {3,S} {4,S}
2    C U0 {1,S} {5,S} {6,S} {7,S}
3    C U0 {1,S} {8,S} {9,S} {10,S}
4    H U0 {1,S}
5    C U0 {2,S}
6    H U0 {2,S}
7    H U0 {2,S}
8    C U0 {3,S}
9    H U0 {3,S}
10   H U0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.71,-3.14,-3.92,-4.33,-4.71,-4.92,-4.92],'cal/(mol*K)'),
        H298 = (98.45,'kcal/mol'),
        S298 = (4.9,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
)

entry(
    index        = 215,
    label        = "cyclopentane",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * C U1 {2,S} {3,S} {4,S}
2    C U0 {1,S} {5,S} {6,S} {7,S}
3    C U0 {1,S} {8,S} {9,S} {10,S}
4    H U0 {1,S}
5    C U0 {2,S} {8,S}
6    H U0 {2,S}
7    H U0 {2,S}
8    C U0 {3,S} {5,S}
9    H U0 {3,S}
10   H U0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.71,-3.14,-3.92,-4.33,-4.71,-4.92,-4.92],'cal/(mol*K)'),
        H298 = (96.4,'kcal/mol'),
        S298 = (4.9,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from RCCJCC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 216,
    label        = "cyclohexane",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  * C U1 {2,S} {3,S} {4,S}
2    C U0 {1,S} {5,S} {6,S} {7,S}
3    C U0 {1,S} {8,S} {9,S} {10,S}
4    H U0 {1,S}
5    C U0 {2,S} {11,S}
6    H U0 {2,S}
7    H U0 {2,S}
8    C U0 {3,S} {11,S}
9    H U0 {3,S}
10   H U0 {3,S}
11   C U0 {5,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.71,-3.14,-3.92,-4.33,-4.71,-4.92,-4.92],'cal/(mol*K)'),
        H298 = (95.5,'kcal/mol'),
        S298 = (4.9,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from RCCJCC entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 24,
    label        = "Benzyl_S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Cb U0 {1,S}
3   C  U0 {1,S}
4   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.87,0.09,-0.63,-1.21,-2.07,-2.69,-2.69],'cal/(mol*K)'),
        H298 = (85.9,'kcal/mol'),
        S298 = (-5.04,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
)

entry(
    index        = 25,
    label        = "Allyl_S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Cd U0 {1,S}
3   Cs U0 {1,S}
4   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.54,-1.82,-2.08,-2.32,-2.75,-3.14,-3.85],'cal/(mol*K)'),
        H298 = (85.6,'kcal/mol'),
        S298 = (-3.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
u"""

""",
)

entry(
    index        = 147,
    label        = "cyclobutene-allyl",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {4,S} {5,S}
2   Cs U0 {1,S} {3,S}
3   C  U0 {2,S} {4,D}
4   Cd U0 {1,S} {3,D}
5   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.54,-1.82,-2.08,-2.32,-2.75,-3.14,-3.85],'cal/(mol*K)'),
        H298 = (91.2,'kcal/mol'),
        S298 = (-3.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""Tian, Z.; Fattahi, A.; Lis, L.; Kass, S. R., "Cycloalkane and Cycloalkene C-H Bond Dissociation Energies," J. Am. Chem. Soc. 2006, 128, 17087-17092, DOI: 10.1021/ja065348u S, Cp copied from Allyl_S""",
    longDesc = 
u"""

""",
)

entry(
    index        = 148,
    label        = "cyclopentene-allyl",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   Cs U0 {2,S} {3,S}
2   C  U0 {1,S} {5,S}
3 * C  U1 {1,S} {4,S} {6,S}
4   Cd U0 {3,S} {5,D}
5   C  U0 {2,S} {4,D}
6   H  U0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.54,-1.82,-2.08,-2.32,-2.75,-3.14,-3.85],'cal/(mol*K)'),
        H298 = (82.3,'kcal/mol'),
        S298 = (-3.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""Furuyama, S.; Golden, D. M.; Benson, S. W., "Kinetic Study of the Gas-Phase Reaction c-C5H8+I2 c-C5H6+2HI. Heat of Formation and the Stabilization Energy of the Cyclopentenyl Radical,"Int. J. Chem. Kinet. 1970, 2, 93-99. S, Cp copied from Allyl_S""",
    longDesc = 
u"""

""",
)

entry(
    index        = 149,
    label        = "cyclohexene-allyl",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   C  U0 {2,S} {3,S}
2   Cs U0 {1,S} {4,S}
3   C  U0 {1,S} {6,S}
4 * C  U1 {2,S} {5,S} {7,S}
5   Cd U0 {4,S} {6,D}
6   C  U0 {3,S} {5,D}
7   H  U0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.54,-1.82,-2.08,-2.32,-2.75,-3.14,-3.85],'cal/(mol*K)'),
        H298 = (85,'kcal/mol'),
        S298 = (-3.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""Alfassi, Z. B.; Feldman, L., "The Kinetics of Radiation-Induced Hydrogen Abstraction by Trichloromethyl Radicals in the Liquid Phase: Cyclohexene," Int. J. Chem. Kinet. 1981, 13, 771-783. S, Cp copied from Allyl_S""",
    longDesc = 
u"""

""",
)

entry(
    index        = 27,
    label        = "C=CCJC=C",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Cd U0 {1,S}
3   Cd U0 {1,S}
4   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.13,-1.96,-1.88,-1.89,-2.2,-2.6,-2.6],'cal/(mol*K)'),
        H298 = (76,'kcal/mol'),
        S298 = (-4.05,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
)

entry(
    index        = 145,
    label        = "cyclopropenyl-allyl",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Cd U0 {1,S} {3,D}
3   Cd U0 {1,S} {2,D}
4   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.13,-1.96,-1.88,-1.89,-2.2,-2.6,-2.6],'cal/(mol*K)'),
        H298 = (90.6,'kcal/mol'),
        S298 = (-4.05,'cal/(mol*K)'),
    ),
    shortDesc = u"""DeFrees, D. J.; McIver, R. T., Jr.; Hehre, W. J., "Heats of Formation of Gaseous Free Radicals via Ion Cyclotron Double Resonance Spectroscopy," J. Am. Chem. Soc. 1980, 102, 3334-3338, DOI: 10.1021/ja00530a005 S, Cp copied from C=CCJC=C""",
    longDesc = 
u"""

""",
)

entry(
    index        = 182,
    label        = "1,3-cyclopentadiene-allyl",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {6,S}
2   Cd U0 {1,S} {4,D}
3   Cd U0 {1,S} {5,D}
4   C  U0 {2,D} {5,S}
5   C  U0 {3,D} {4,S}
6   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.54,-1.82,-2.08,-2.32,-2.75,-3.14,-3.85],'cal/(mol*K)'),
        H298 = (82.6,'kcal/mol'),
        S298 = (-3.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
u"""

""",
)

entry(
    index        = 28,
    label        = "Sec_Propargyl",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Ct U0 {1,S}
3   Cs U0 {1,S}
4   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.59,-1.2,-1.75,-2.19,-2.91,-3.49,-3.49],'cal/(mol*K)'),
        H298 = (87,'kcal/mol'),
        S298 = (-0.45,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
)

entry(
    index        = 26,
    label        = "CCJCHO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   CO U0 {1,S} {5,D} {6,S}
3   Cs U0 {1,S}
4   H  U0 {1,S}
5   O  U0 {2,D}
6   H  U0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.36,-1.57,-1.73,-1.89,-2.66,-3.11,-3.5],'cal/(mol*K)'),
        H298 = (91.9,'kcal/mol'),
        S298 = (-2.37,'cal/(mol*K)'),
    ),
    shortDesc = u"""CHEN & BOZZELLI #""",
    longDesc = 
u"""

""",
)

entry(
    index        = 29,
    label        = "Cs_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   C U0 {1,S}
3   C U0 {1,S}
4   C U0 {1,S}
""",
    thermo = u'Tertalkyl',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 30,
    label        = "Tertalkyl",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Cs U0 {1,S}
3   Cs U0 {1,S}
4   Cs U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (96.5,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
u"""

""",
)

entry(
    index        = 162,
    label        = "bicyclo[1.1.0]butane-tertiary",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   Cs U0 {2,S} {3,S} {4,S}
2 * Cs U1 {1,S} {3,S} {4,S}
3   Cs U0 {1,S} {2,S}
4   Cs U0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (113.8,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 163,
    label        = "bicyclo[2.1.0]pentane-tertiary",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U1 {2,S} {3,S} {5,S}
2   Cs U0 {1,S} {3,S} {4,S}
3   Cs U0 {1,S} {2,S}
4   Cs U0 {2,S} {5,S}
5   Cs U0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (110.2,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 195,
    label        = "bicyclo[1.1.1]pentane-C1",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {3,S} {4,S} {5,S}
2   C  U0 {3,S} {4,S} {5,S}
3   Cs U0 {1,S} {2,S}
4   Cs U0 {1,S} {2,S}
5   Cs U0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (106.2,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 31,
    label        = "C2CJCOOH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Cs U0 {1,S} {5,S}
3   Cs U0 {1,S}
4   Cs U0 {1,S}
5   O  U0 {2,S} {6,S}
6   O  U0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.54,-4.16,-4.44,-4.58,-4.74,-4.88,-5.23],'cal/(mol*K)'),
        H298 = (97.2,'kcal/mol'),
        S298 = (7.31,'cal/(mol*K)'),
    ),
    shortDesc = u"""WIJAYA et al.""",
    longDesc = 
u"""

""",
)

entry(
    index        = 164,
    label        = "bicyclo[3.1.0]hexane-tertiary",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U1 {2,S} {3,S} {5,S}
2   Cs U0 {1,S} {3,S} {4,S}
3   Cs U0 {1,S} {2,S}
4   Cs U0 {2,S} {6,S}
5   Cs U0 {1,S} {6,S}
6   Cs U0 {4,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (108.6,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 165,
    label        = "bicyclo[2.2.0]hexane-tertiary",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U1 {2,S} {3,S} {6,S}
2   Cs U0 {1,S} {4,S} {5,S}
3   Cs U0 {1,S} {4,S}
4   Cs U0 {2,S} {3,S}
5   Cs U0 {2,S} {6,S}
6   Cs U0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (104,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 198,
    label        = "bicyclo[2.1.1]hexane-C1",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {3,S} {4,S} {6,S}
2   C  U0 {3,S} {4,S} {5,S}
3   Cs U0 {1,S} {2,S}
4   Cs U0 {1,S} {2,S}
5   C  U0 {2,S} {6,S}
6   Cs U0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (108.9,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 139,
    label        = "bridgehead_norbornyl",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U1 {3,S} {4,S} {7,S}
2   Cs U0 {3,S} {5,S} {6,S}
3   Cs U0 {1,S} {2,S}
4   Cs U0 {1,S} {5,S}
5   Cs U0 {2,S} {4,S}
6   Cs U0 {2,S} {7,S}
7   Cs U0 {1,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (107.42,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""P.M. Nunes, S.G. Estacio, G.T. Lopes, B.J. Costa Cabral, R.M. Borges dos Santos, J.A. Martinho Simoes, CH Bond Dissociation Enthalpies in Norbornane. An Experimental and Computational Study, Organic Letters, 10 (2008) 1613-1616. S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 166,
    label        = "bicyclo[3.2.0]heptane-tertiary",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U1 {2,S} {3,S} {6,S}
2   Cs U0 {1,S} {4,S} {5,S}
3   Cs U0 {1,S} {4,S}
4   Cs U0 {2,S} {3,S}
5   Cs U0 {2,S} {7,S}
6   Cs U0 {1,S} {7,S}
7   Cs U0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (102.6,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 167,
    label        = "bicyclo[4.1.0]heptane-tertiary",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cs U1 {2,S} {3,S} {5,S}
2   Cs U0 {1,S} {3,S} {4,S}
3   Cs U0 {1,S} {2,S}
4   Cs U0 {2,S} {6,S}
5   Cs U0 {1,S} {7,S}
6   Cs U0 {4,S} {7,S}
7   Cs U0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (105.4,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 203,
    label        = "bicyclo[3.1.1]heptane-C1",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {3,S} {4,S} {6,S}
2   C  U0 {3,S} {4,S} {5,S}
3   Cs U0 {1,S} {2,S}
4   Cs U0 {1,S} {2,S}
5   C  U0 {2,S} {7,S}
6   Cs U0 {1,S} {7,S}
7   C  U0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (103.6,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 168,
    label        = "octahydro-pentalene-tertiary",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Cs U0 {1,S} {5,S} {6,S}
3   Cs U0 {1,S} {8,S}
4   Cs U0 {1,S} {7,S}
5   C  U0 {2,S} {7,S}
6   C  U0 {2,S} {8,S}
7   C  U0 {4,S} {5,S}
8   C  U0 {3,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (95.7,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 169,
    label        = "bicyclo[4.2.0]octane-tertiary",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {6,S}
2   Cs U0 {1,S} {4,S} {5,S}
3   Cs U0 {1,S} {4,S}
4   C  U0 {2,S} {3,S}
5   C  U0 {2,S} {7,S}
6   Cs U0 {1,S} {8,S}
7   C  U0 {5,S} {8,S}
8   C  U0 {6,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (97,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 212,
    label        = "bicyclo[2.2.2]octane-C1",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {3,S} {6,S} {8,S}
2   C  U0 {4,S} {5,S} {7,S}
3   Cs U0 {1,S} {4,S}
4   C  U0 {2,S} {3,S}
5   C  U0 {2,S} {6,S}
6   Cs U0 {1,S} {5,S}
7   C  U0 {2,S} {8,S}
8   Cs U0 {1,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (101.9,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 32,
    label        = "Benzyl_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Cb U0 {1,S}
3   C  U0 {1,S}
4   C  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.27,-0.78,-1.54,-2.06,-2.74,-3.19,-3.19],'cal/(mol*K)'),
        H298 = (83.8,'kcal/mol'),
        S298 = (-5.34,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
)

entry(
    index        = 33,
    label        = "Allyl_T",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Cd U0 {1,S}
3   Cs U0 {1,S}
4   Cs U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.79,-2.38,-2.74,-2.97,-3.28,-3.55,-3.55],'cal/(mol*K)'),
        H298 = (83.4,'kcal/mol'),
        S298 = (-3.69,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
)

entry(
    index        = 183,
    label        = "bicyclo[2.1.0]pent-2-ene-C1",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {5,S}
2   Cs U0 {1,S} {3,S} {4,S}
3   Cs U0 {1,S} {2,S}
4   C  U0 {2,S} {5,D}
5   Cd U0 {1,S} {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (112.1,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 186,
    label        = "bicyclo[2.1.1]hex-2-ene-C1",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {3,S} {4,S} {6,S}
2   C  U0 {3,S} {4,S} {5,S}
3   Cs U0 {1,S} {2,S}
4   Cs U0 {1,S} {2,S}
5   C  U0 {2,S} {6,D}
6   Cd U0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (110.1,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 35,
    label        = "Tert_Propargyl",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Ct U0 {1,S}
3   Cs U0 {1,S}
4   Cs U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.04,-1.01,-1.74,-2.41,-3.19,-3.65,-3.65],'cal/(mol*K)'),
        H298 = (84.5,'kcal/mol'),
        S298 = (1.48,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
)

entry(
    index        = 501,
    label        = "C2CJCO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   CO U0 {1,S} {5,D} {6,S}
3   Cs U0 {1,S}
4   Cs U0 {1,S}
5   O  U0 {2,D}
6   R  U0 {2,S}
""",
    thermo = u'C2CJCHO',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 34,
    label        = "C2CJCHO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   CO U0 {1,S} {5,D} {6,S}
3   Cs U0 {1,S}
4   Cs U0 {1,S}
5   O  U0 {2,D}
6   H  U0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.62,-0.2,-1.23,-1.82,-2.87,-3.47,-3.47],'cal/(mol*K)'),
        H298 = (89.8,'kcal/mol'),
        S298 = (-1.71,'cal/(mol*K)'),
    ),
    shortDesc = u"""CHEN & BOZZELLI #. Value for Cp1500 taken as equal to Cp1000""",
    longDesc = 
u"""

""",
)

entry(
    index        = 191,
    label        = "bicyclo[2.2.0]hexa-2,5-diene-C1",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {6,S}
2   Cs U0 {1,S} {4,S} {5,S}
3   Cd U0 {1,S} {4,D}
4   C  U0 {2,S} {3,D}
5   C  U0 {2,S} {6,D}
6   Cd U0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.48,-3.55,-4.15,-4.75,-5.02,-5.39],'cal/(mol*K)'),
        H298 = (102.8,'kcal/mol'),
        S298 = (5.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from TertAlkyl entry""",
    longDesc = 
u"""

""",
)

entry(
    index        = 36,
    label        = "CsJO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   O U0 {1,S}
3   H U0 {1,S}
4   H U0 {1,S}
""",
    thermo = u'CsJOH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 37,
    label        = "CsJOH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   O U0 {1,S} {5,S}
3   H U0 {1,S}
4   H U0 {1,S}
5   H U0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.25,0.18,-0.26,-0.83,-1.95,-2.85,-4.22],'cal/(mol*K)'),
        H298 = (96.51,'kcal/mol'),
        S298 = (0.09,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index        = 38,
    label        = "CsJOC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   O U0 {1,S} {5,S}
3   H U0 {1,S}
4   H U0 {1,S}
5   C U0 {2,S}
""",
    thermo = u'CsJOCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 39,
    label        = "CsJOCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   O  U0 {1,S} {5,S}
3   H  U0 {1,S}
4   H  U0 {1,S}
5   Cs U0 {2,S}
""",
    thermo = u'CsJOCH3',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 40,
    label        = "CsJOCH3",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   O U0 {1,S} {5,S}
3   H U0 {1,S}
4   H U0 {1,S}
5   C U0 {2,S} {6,S} {7,S} {8,S}
6   H U0 {5,S}
7   H U0 {5,S}
8   H U0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.16,-0.4,-0.82,-1.33,-2.32,-3.13,-4.37],'cal/(mol*K)'),
        H298 = (97,'kcal/mol'),
        S298 = (0.78,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN #""",
    longDesc = 
u"""

""",
)

entry(
    index        = 41,
    label        = "CsJOCC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   O U0 {1,S} {5,S}
3   H U0 {1,S}
4   H U0 {1,S}
5   C U0 {2,S} {6,S} {7,S} {8,S}
6   C U0 {5,S}
7   H U0 {5,S}
8   H U0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.01,-1.22,-1.4,-1.71,-3.5,-3.24,-4.42],'cal/(mol*K)'),
        H298 = (96.83,'kcal/mol'),
        S298 = (1.41,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated from data in SUMATHI & GREEN. Values might have large error bars.""",
    longDesc = 
u"""

""",
)

entry(
    index        = 42,
    label        = "CsJOCC2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   O U0 {1,S} {5,S}
3   H U0 {1,S}
4   H U0 {1,S}
5   C U0 {2,S} {6,S} {7,S} {8,S}
6   C U0 {5,S}
7   C U0 {5,S}
8   H U0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.95,0.75,0.23,-0.43,-1.71,-2.72,-4.19],'cal/(mol*K)'),
        H298 = (96.16,'kcal/mol'),
        S298 = (-0.59,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index        = 43,
    label        = "CsJOCC3",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   O U0 {1,S} {5,S}
3   H U0 {1,S}
4   H U0 {1,S}
5   C U0 {2,S} {6,S} {7,S} {8,S}
6   C U0 {5,S}
7   C U0 {5,S}
8   C U0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.08,-0.09,-0.52,-1.06,-2.11,-2.96,-4.27],'cal/(mol*K)'),
        H298 = (95.75,'kcal/mol'),
        S298 = (0.27,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index        = 44,
    label        = "CsJOCds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C       U1 {2,S} {3,S} {4,S}
2   O       U0 {1,S} {5,S}
3   H       U0 {1,S}
4   H       U0 {1,S}
5   {Cd,CO} U0 {2,S}
""",
    thermo = u'CsJOC(O)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 45,
    label        = "CsJOC(O)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   O U0 {1,S} {5,S}
3   H U0 {1,S}
4   H U0 {1,S}
5   C U0 {2,S} {6,D}
6   O U0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.91,0.89,0.42,-0.21,-1.5,-2.62,-4.43],'cal/(mol*K)'),
        H298 = (100.7,'kcal/mol'),
        S298 = (-0.18,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index        = 46,
    label        = "CsJOC(O)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   O U0 {1,S} {5,S}
3   H U0 {1,S}
4   H U0 {1,S}
5   C U0 {2,S} {6,D} {7,S}
6   O U0 {5,D}
7   H U0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.95,0.97,0.53,-0.12,-1.54,-2.76,-4.53],'cal/(mol*K)'),
        H298 = (100.88,'kcal/mol'),
        S298 = (-0.18,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index        = 47,
    label        = "CsJOC(O)C",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   O U0 {1,S} {5,S}
3   H U0 {1,S}
4   H U0 {1,S}
5   C U0 {2,S} {6,D} {7,S}
6   O U0 {5,D}
7   C U0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.88,0.81,0.31,-0.3,-1.45,-2.47,-4.33],'cal/(mol*K)'),
        H298 = (100.48,'kcal/mol'),
        S298 = (-0.17,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index        = 48,
    label        = "CsJOO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   O U0 {1,S} {5,S}
3   H U0 {1,S}
4   H U0 {1,S}
5   O U0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.18,-0.42,-0.79,-1.2,-1.99,-2.63,-3.65],'cal/(mol*K)'),
        H298 = (98.5,'kcal/mol'),
        S298 = (-1.57,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index        = 49,
    label        = "CsJOOH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   O U0 {1,S} {5,S}
3   H U0 {1,S}
4   H U0 {1,S}
5   O U0 {2,S} {6,S}
6   H U0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.06,-0.35,-0.76,-1.19,-1.99,-2.64,-3.68],'cal/(mol*K)'),
        H298 = (98.91,'kcal/mol'),
        S298 = (-1.52,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index        = 50,
    label        = "CsJOOC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   O U0 {1,S} {5,S}
3   H U0 {1,S}
4   H U0 {1,S}
5   O U0 {2,S} {6,S}
6   C U0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.31,-0.48,-0.82,-1.22,-1.99,-2.62,-3.63],'cal/(mol*K)'),
        H298 = (98.34,'kcal/mol'),
        S298 = (-1.62,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index        = 51,
    label        = "CCsJO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   O U0 {1,S}
3   C U0 {1,S}
4   H U0 {1,S}
""",
    thermo = u'CCsJOC',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 52,
    label        = "CCsJOH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   O U0 {1,S} {5,S}
3   C U0 {1,S}
4   H U0 {1,S}
5   H U0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.65,-0.01,-0.75,-1.43,-2.52,-3.31,-4.47],'cal/(mol*K)'),
        H298 = (95.39,'kcal/mol'),
        S298 = (0.92,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index        = 53,
    label        = "CCsJOC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   O U0 {1,S} {5,S}
3   C U0 {1,S}
4   H U0 {1,S}
5   C U0 {2,S}
""",
    thermo = u'CCsJOCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 54,
    label        = "CCsJOCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   O  U0 {1,S} {5,S}
3   C  U0 {1,S}
4   H  U0 {1,S}
5   Cs U0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.82,0.53,-0.11,-0.86,-2.2,-3.18,-4.51],'cal/(mol*K)'),
        H298 = (95.41,'kcal/mol'),
        S298 = (0.33,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index        = 55,
    label        = "CCsJOCds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C       U1 {2,S} {3,S} {4,S}
2   O       U0 {1,S} {5,S}
3   C       U0 {1,S}
4   H       U0 {1,S}
5   {CO,Cd} U0 {2,S}
""",
    thermo = u'CCsJOC(O)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 56,
    label        = "CCsJOC(O)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   O U0 {1,S} {5,S}
3   C U0 {1,S}
4   H U0 {1,S}
5   C U0 {2,S} {6,D}
6   O U0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.16,0.78,0.05,-0.73,-2.13,-3.24,-4.9],'cal/(mol*K)'),
        H298 = (98.7,'kcal/mol'),
        S298 = (0.98,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index        = 57,
    label        = "CCsJOC(O)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   O U0 {1,S} {5,S}
3   C U0 {1,S}
4   H U0 {1,S}
5   C U0 {2,S} {6,D} {7,S}
6   O U0 {5,D}
7   H U0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.2,0.88,0.16,-0.67,-2.22,-3.43,-5],'cal/(mol*K)'),
        H298 = (98.87,'kcal/mol'),
        S298 = (0.98,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "CCsJOC(O)C",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   O U0 {1,S} {5,S}
3   C U0 {1,S}
4   H U0 {1,S}
5   C U0 {2,S} {6,D} {7,S}
6   O U0 {5,D}
7   C U0 {5,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 58,
    label        = "CCsJOO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   O U0 {1,S} {5,S}
3   C U0 {1,S}
4   H U0 {1,S}
5   O U0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.48,-1.15,-1.68,-2.11,-2.77,-3.26,-4.02],'cal/(mol*K)'),
        H298 = (96.9,'kcal/mol'),
        S298 = (0.76,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index        = 59,
    label        = "CCsJOOH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   O U0 {1,S} {5,S}
3   C U0 {1,S}
4   H U0 {1,S}
5   O U0 {2,S} {6,S}
6   H U0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.39,-1.08,-1.64,-2.08,-2.75,-3.26,-4.03],'cal/(mol*K)'),
        H298 = (97.19,'kcal/mol'),
        S298 = (0.77,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index        = 60,
    label        = "CCsJOOC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   O U0 {1,S} {5,S}
3   C U0 {1,S}
4   H U0 {1,S}
5   O U0 {2,S} {6,S}
6   C U0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.58,-1.21,-1.73,-2.15,-2.8,-3.27,-4.01],'cal/(mol*K)'),
        H298 = (96.64,'kcal/mol'),
        S298 = (0.74,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index        = 61,
    label        = "C2CsJO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   O U0 {1,S}
3   C U0 {1,S}
4   C U0 {1,S}
""",
    thermo = u'C2CsJOC',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 62,
    label        = "C2CsJOH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   O U0 {1,S} {5,S}
3   C U0 {1,S}
4   C U0 {1,S}
5   H U0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.31,-0.66,-1.54,-2.23,-3.17,-3.8,-4.72],'cal/(mol*K)'),
        H298 = (94.5,'kcal/mol'),
        S298 = (2.17,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index        = 63,
    label        = "C2CsJOC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   O U0 {1,S} {5,S}
3   C U0 {1,S}
4   C U0 {1,S}
5   C U0 {2,S}
""",
    thermo = u'C2CsJOCs',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 64,
    label        = "C2CsJOCs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   O  U0 {1,S} {5,S}
3   C  U0 {1,S}
4   C  U0 {1,S}
5   Cs U0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.09,-1.37,-2.49,-3.26,-4.15,-4.63,-5.23],'cal/(mol*K)'),
        H298 = (95.5,'kcal/mol'),
        S298 = (3.71,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index        = 65,
    label        = "C2CsJOCds",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C       U1 {2,S} {3,S} {4,S}
2   O       U0 {1,S} {5,S}
3   C       U0 {1,S}
4   C       U0 {1,S}
5   {Cd,CO} U0 {2,S}
""",
    thermo = u'C2CsJOC(O)',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 66,
    label        = "C2CsJOC(O)",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   O U0 {1,S} {5,S}
3   C U0 {1,S}
4   C U0 {1,S}
5   C U0 {2,S} {6,D}
6   O U0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.04,-1.34,-2.3,-2.99,-3.99,-4.77,-5.98],'cal/(mol*K)'),
        H298 = (100.1,'kcal/mol'),
        S298 = (4.77,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index        = 67,
    label        = "C2CsJOC(O)H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   O U0 {1,S} {5,S}
3   C U0 {1,S}
4   C U0 {1,S}
5   C U0 {2,S} {6,D} {7,S}
6   O U0 {5,D}
7   H U0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.03,-1.28,-2.28,-3.1,-4.35,-5.19,-6.06],'cal/(mol*K)'),
        H298 = (99.97,'kcal/mol'),
        S298 = (4.88,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index        = 68,
    label        = "C2CsJOC(O)C",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   O U0 {1,S} {5,S}
3   C U0 {1,S}
4   C U0 {1,S}
5   C U0 {2,S} {6,D} {7,S}
6   O U0 {5,D}
7   C U0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.04,-1.4,-2.32,-2.89,-3.62,-4.36,-5.9],'cal/(mol*K)'),
        H298 = (100.25,'kcal/mol'),
        S298 = (4.66,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index        = 69,
    label        = "C2CsJOO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   O U0 {1,S} {5,S}
3   C U0 {1,S}
4   C U0 {1,S}
5   O U0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.89,-2.09,-2.81,-3.24,-3.69,-3.97,-4.43],'cal/(mol*K)'),
        H298 = (96.7,'kcal/mol'),
        S298 = (2.22,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index        = 70,
    label        = "C2CsJOOH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   O U0 {1,S} {5,S}
3   C U0 {1,S}
4   C U0 {1,S}
5   O U0 {2,S} {6,S}
6   H U0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.01,-2.17,-2.87,-3.3,-3.77,-4.05,-4.49],'cal/(mol*K)'),
        H298 = (96.74,'kcal/mol'),
        S298 = (2.37,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index        = 71,
    label        = "C2CsJOOC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   O U0 {1,S} {5,S}
3   C U0 {1,S}
4   C U0 {1,S}
5   O U0 {2,S} {6,S}
6   C U0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.78,-2.02,-2.75,-3.18,-3.62,-3.88,-4.37],'cal/(mol*K)'),
        H298 = (96.58,'kcal/mol'),
        S298 = (2.08,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index        = 264,
    label        = "CCsJOS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   C U0 {1,S}
3   O U0 {1,S}
4   S U0 {1,S}
""",
    thermo = u'CCsJOHSH',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 265,
    label        = "CCsJOHSH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   C U0 {1,S}
3   O U0 {1,S} {5,S}
4   S U0 {1,S} {6,S}
5   H U0 {3,S}
6   H U0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.38,-1.32,-1.19,-1.14,-1.39,-1.94,-3.4],'cal/(mol*K)'),
        H298 = (92.1,'kcal/mol'),
        S298 = (1.95,'cal/(mol*K)'),
    ),
    shortDesc = u"""CAC CBS-QB3 1d-hr""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "CsJ-S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Ss U0 {1,S}
3   R  U0 {1,S}
4   R  U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 244,
    label        = "CsJ-SsHH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Ss U0 {1,S}
3   H  U0 {1,S}
4   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.07,-0.32,-0.73,-1.22,-2.18,-2.99,-4.27],'cal/(mol*K)'),
        H298 = (95.34,'kcal/mol'),
        S298 = (1.18,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "CsJ-CSH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   C  U0 {1,S}
3   Ss U0 {1,S}
4   H  U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 245,
    label        = "CsJ-CsSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Cs U0 {1,S}
3   Ss U0 {1,S}
4   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.25,-0.79,-1.36,-1.9,-2.82,-3.53,-4.64],'cal/(mol*K)'),
        H298 = (92.87,'kcal/mol'),
        S298 = (1.91,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 247,
    label        = "CsJ-CtSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Ct U0 {1,S}
3   Ss U0 {1,S}
4   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.26,-0.02,-0.47,-0.97,-1.95,-2.77,-4.12],'cal/(mol*K)'),
        H298 = (83.48,'kcal/mol'),
        S298 = (-0.16,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 248,
    label        = "CsJ-CbSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Cb U0 {1,S}
3   Ss U0 {1,S}
4   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.32,-0.38,-0.65,-1.01,-1.75,-2.4,-3.57],'cal/(mol*K)'),
        H298 = (84.88,'kcal/mol'),
        S298 = (-0.98,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 246,
    label        = "CsJ-CdSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Cd U0 {1,S} {5,D}
3   Ss U0 {1,S}
4   H  U0 {1,S}
5   C  U0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.21,-2.77,-2.39,-2.24,-2.39,-2.74,-3.56],'cal/(mol*K)'),
        H298 = (81.92,'kcal/mol'),
        S298 = (0.66,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 249,
    label        = "CsJ-C=SSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Cd U0 {1,S} {5,D}
3   Ss U0 {1,S}
4   H  U0 {1,S}
5   Sd U0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.75,-2.93,-2.07,-1.54,-1.2,-1.31,-2.01],'cal/(mol*K)'),
        H298 = (71.51,'kcal/mol'),
        S298 = (-3.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "CsJ-CCS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   C  U0 {1,S}
3   C  U0 {1,S}
4   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 251,
    label        = "CsJ-CsCsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Cs U0 {1,S}
3   Cs U0 {1,S}
4   Ss U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.72,-2.04,-2.88,-3.4,-3.99,-4.36,-4.96],'cal/(mol*K)'),
        H298 = (92.32,'kcal/mol'),
        S298 = (3.87,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 253,
    label        = "CsJ-CsCtSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Cs U0 {1,S}
3   Ct U0 {1,S}
4   Ss U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.99,-1.64,-2.18,-2.62,-3.3,-3.82,-4.65],'cal/(mol*K)'),
        H298 = (81.17,'kcal/mol'),
        S298 = (3.05,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 254,
    label        = "CsJ-CsCbSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Cs U0 {1,S}
3   Cb U0 {1,S}
4   Ss U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.99,-2.26,-2.53,-2.75,-3.12,-3.49,-4.43],'cal/(mol*K)'),
        H298 = (84.1,'kcal/mol'),
        S298 = (0.96,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 252,
    label        = "CsJ-CsCdSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Cs U0 {1,S}
3   Cd U0 {1,S} {5,D}
4   Ss U0 {1,S}
5   C  U0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4,-4.74,-4.81,-4.59,-4.17,-3.99,-4.12],'cal/(mol*K)'),
        H298 = (80.07,'kcal/mol'),
        S298 = (2.53,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 255,
    label        = "CsJ-CsC=SSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Cs U0 {1,S}
3   Cd U0 {1,S} {5,D}
4   Ss U0 {1,S}
5   Sd U0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.86,-3.83,-3.41,-2.93,-2.28,-2.07,-2.36],'cal/(mol*K)'),
        H298 = (69.17,'kcal/mol'),
        S298 = (-1.97,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "CsJ-SS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Ss U0 {1,S}
3   Ss U0 {1,S}
4   R  U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 250,
    label        = "CsJ-SsSsH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Ss U0 {1,S}
3   Ss U0 {1,S}
4   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.52,-4,-3.64,-3.53,-3.68,-4,-4.72],'cal/(mol*K)'),
        H298 = (90.16,'kcal/mol'),
        S298 = (1.31,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "CsJ-CSS",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   C  U0 {1,S}
3   Ss U0 {1,S}
4   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 256,
    label        = "CsJ-CsSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Cs U0 {1,S}
3   S  U0 {1,S}
4   Ss U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.36,-4,-4.17,-4.24,-4.37,-4.55,-5],'cal/(mol*K)'),
        H298 = (89.98,'kcal/mol'),
        S298 = (5.5,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "CsJ-CtSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Ct U0 {1,S}
3   Ss U0 {1,S}
4   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "CsJ-CbSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Cb U0 {1,S}
3   Ss U0 {1,S}
4   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "CsJ-CdSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Cd U0 {1,S} {5,D}
3   Ss U0 {1,S}
4   Ss U0 {1,S}
5   C  U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "CsJ-C=SSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Cd U0 {1,S} {5,D}
3   Ss U0 {1,S}
4   Ss U0 {1,S}
5   Sd U0 {2,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "CsJ-SsSsSs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,S} {3,S} {4,S}
2   Ss U0 {1,S}
3   Ss U0 {1,S}
4   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 300,
    label        = "CsJN",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   N U0 {1,S}
3   H U0 {1,S}
4   H U0 {1,S}
""",
    thermo = u'CCsJN',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 301,
    label        = "CCsJN",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   N U0 {1,S}
3   C U0 {1,S}
4   H U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.2,-0.7,-1.4,-1.9,-2.8,-3.4,-4.5],'cal/(mol*K)'),
        H298 = (92.1,'kcal/mol'),
        S298 = (2.5,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 302,
    label        = "C2CsJN",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,S} {3,S} {4,S}
2   N U0 {1,S}
3   C U0 {1,S}
4   C U0 {1,S}
""",
    thermo = u'CCsJN',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 72,
    label        = "CdsJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * {Cd,CO} U1
""",
    thermo = u'Cds_P',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 79,
    label        = "CdsJO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,D}
2   O U0 {1,D}
""",
    thermo = u'CCJ=O',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 80,
    label        = "HCdsJO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,D} {3,S}
2   O U0 {1,D}
3   H U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.19,-0.65,-1.19,-1.73,-2.63,-3.32,-4.42],'cal/(mol*K)'),
        H298 = (88.45,'kcal/mol'),
        S298 = (-0.01,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated in relation to formaldehyde from NIST values""",
    longDesc = 
u"""

""",
)

entry(
    index        = 81,
    label        = "CCJ=O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,D} {3,S}
2   O U0 {1,D}
3   C U0 {1,S}
""",
    thermo = u'CsCJ=O',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 82,
    label        = "CsCJ=O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,D} {3,S}
2   O  U0 {1,D}
3   Cs U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.83,-1.43,-1.96,-2.42,-3.16,-3.73,-4.64],'cal/(mol*K)'),
        H298 = (89,'kcal/mol'),
        S298 = (1.12,'cal/(mol*K)'),
    ),
    shortDesc = u"""CHEN & BOZZELLI #""",
    longDesc = 
u"""

""",
)

entry(
    index        = 83,
    label        = "C=CCJ=O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,D} {3,S}
2   O  U0 {1,D}
3   Cd U0 {1,S} {4,D}
4   Cd U0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.19,-0.85,-1.59,-2.21,-3.21,-3.89,-4.61],'cal/(mol*K)'),
        H298 = (83,'kcal/mol'),
        S298 = (-1.39,'cal/(mol*K)'),
    ),
    shortDesc = u"""CHEN & BOZZELLI #""",
    longDesc = 
u"""

""",
)

entry(
    index        = 84,
    label        = "(O)CJO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,D} {3,S}
2   O U0 {1,D}
3   O U0 {1,S}
""",
    thermo = u'(O)CJOC',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 85,
    label        = "(O)CJOH",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,D} {3,S}
2   O U0 {1,D}
3   O U0 {1,S} {4,S}
4   H U0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.02,-0.66,-1.4,-2.12,-3.41,-4.44,-5.79],'cal/(mol*K)'),
        H298 = (100.75,'kcal/mol'),
        S298 = (0.78,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN #""",
    longDesc = 
u"""

""",
)

entry(
    index        = 86,
    label        = "(O)CJOC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,D} {3,S}
2   O U0 {1,D}
3   O U0 {1,S} {4,S}
4   C U0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.45,-0.27,-1.19,-2.1,-3.63,-4.69,-5.8],'cal/(mol*K)'),
        H298 = (98.99,'kcal/mol'),
        S298 = (0.72,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN (Hf assigned value of (O)CJOCH(CH3)2)""",
    longDesc = 
u"""

""",
)

entry(
    index        = 87,
    label        = "(O)CJOCH3",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,D} {3,S}
2   O U0 {1,D}
3   O U0 {1,S} {4,S}
4   C U0 {3,S} {5,S} {6,S} {7,S}
5   H U0 {4,S}
6   H U0 {4,S}
7   H U0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.51,-0.11,-0.94,-1.8,-3.34,-4.48,-5.79],'cal/(mol*K)'),
        H298 = (100.1,'kcal/mol'),
        S298 = (0.72,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN""",
    longDesc = 
u"""

""",
)

entry(
    index        = 88,
    label        = "(O)CJOCC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,D} {3,S}
2   O U0 {1,D}
3   O U0 {1,S} {4,S}
4   C U0 {3,S} {5,S} {6,S} {7,S}
5   C U0 {4,S}
6   H U0 {4,S}
7   H U0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.45,-0.13,-0.98,-1.86,-3.43,-4.56,-5.79],'cal/(mol*K)'),
        H298 = (99.49,'kcal/mol'),
        S298 = (0.55,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN (values from (O)CJOCH2CH3)""",
    longDesc = 
u"""

""",
)

entry(
    index        = 89,
    label        = "(O)CJOCC2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,D} {3,S}
2   O U0 {1,D}
3   O U0 {1,S} {4,S}
4   C U0 {3,S} {5,S} {6,S} {7,S}
5   C U0 {4,S}
6   C U0 {4,S}
7   H U0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.74,-0.06,-1.04,-2.01,-3.6,-4.66,-5.77],'cal/(mol*K)'),
        H298 = (98.99,'kcal/mol'),
        S298 = (0.82,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN (values from (O)CJOCH(CH3)2)""",
    longDesc = 
u"""

""",
)

entry(
    index        = 90,
    label        = "(O)CJOCC3",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,D} {3,S}
2   O U0 {1,D}
3   O U0 {1,S} {4,S}
4   C U0 {3,S} {5,S} {6,S} {7,S}
5   C U0 {4,S}
6   C U0 {4,S}
7   C U0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.11,-0.79,-1.8,-2.73,-4.17,-5.06,-5.87],'cal/(mol*K)'),
        H298 = (97.98,'kcal/mol'),
        S298 = (0.76,'cal/(mol*K)'),
    ),
    shortDesc = u"""SUMATHI & GREEN (values from (O)CJOC(CH3)3)""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=SJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cd U1 {2,D}
2   Sd U0 {1,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 258,
    label        = "C=SJ-H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cd U1 {2,S} {3,D}
2   H  U0 {1,S}
3   Sd U0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.31,-0.88,-1.47,-1.99,-2.85,-3.49,-4.52],'cal/(mol*K)'),
        H298 = (92.39,'kcal/mol'),
        S298 = (-0.14,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=SJ-C",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cd U1 {2,S} {3,D}
2   C  U0 {1,S}
3   Sd U0 {1,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 259,
    label        = "C=SJ-Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cd U1 {2,S} {3,D}
2   Cs U0 {1,S}
3   Sd U0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.2,-1.8,-2.25,-2.63,-3.24,-3.74,-4.64],'cal/(mol*K)'),
        H298 = (91.94,'kcal/mol'),
        S298 = (0.65,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 260,
    label        = "C=SJ-Cd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cd U1 {2,S} {3,D}
2   Cd U0 {1,S}
3   Sd U0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.21,-1.76,-2.24,-2.65,-3.3,-3.81,-4.67],'cal/(mol*K)'),
        H298 = (77.87,'kcal/mol'),
        S298 = (0.48,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "C=SJ-Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cd U1 {2,S} {3,D}
2   Ss U0 {1,S}
3   Sd U0 {1,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 74,
    label        = "Cds_P",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,D} {3,S}
2   C U0 {1,D}
3   H U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.19,-0.75,-1.36,-1.92,-2.82,-3.49,-4.53],'cal/(mol*K)'),
        H298 = (111.2,'kcal/mol'),
        S298 = (1.39,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
u"""

""",
)

entry(
    index        = 75,
    label        = "C=C=CJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,D} {3,S}
2   C U0 {1,D} {4,D}
3   H U0 {1,S}
4   C U0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.45,-1.05,-1.64,-2.15,-2.98,-3.6,-3.6],'cal/(mol*K)'),
        H298 = (89,'kcal/mol'),
        S298 = (1.29,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
)

entry(
    index        = 77,
    label        = "Cds_S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,D} {3,S}
2   C U0 {1,D}
3   C U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (109,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al. CHEN & BOZZELLI #""",
    longDesc = 
u"""

""",
)

entry(
    index        = 78,
    label        = "C=CJC=C",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C       U1 {2,D} {3,S}
2   Cd      U0 {1,D}
3   {Cd,CO} U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.19,-0.76,-1.51,-2.01,-2.7,-3.17,-3.17],'cal/(mol*K)'),
        H298 = (99.8,'kcal/mol'),
        S298 = (0.71,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
)

entry(
    index        = 194,
    label        = "cyclobutadiene-C1",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C  U1 {2,D} {4,S}
2   Cd U0 {1,D} {3,S}
3   C  U0 {2,S} {4,D}
4   Cd U0 {1,S} {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (104.6,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
u"""

""",
)

entry(
    index        = 181,
    label        = "1,3-cyclopentadiene-vinyl-2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   C U0 {2,S} {3,S}
2   C U0 {1,S} {4,D}
3   C U0 {1,S} {5,D}
4 * C U1 {2,D} {5,S}
5   C U0 {3,D} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (116.2,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
u"""

""",
)

entry(
    index        = 193,
    label        = "bicyclo[2.2.0]hexa-1(4),2,5-triene-C2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   C U0 {2,D} {3,S} {6,S}
2   C U0 {1,D} {4,S} {5,S}
3 * C U1 {1,S} {4,D}
4   C U0 {2,S} {3,D}
5   C U0 {2,S} {6,D}
6   C U0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (102.9,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
u"""

""",
)

entry(
    index        = 144,
    label        = "cyclopropenyl-vinyl",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   C U0 {2,S} {3,S}
2 * C U1 {1,S} {3,D}
3   C U0 {1,S} {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (106.7,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fattahi, A.; McCarthy, R. E.; Ahmad, M. R.; Kass, S. R., "Why Does Cyclopropene Have the Acidity of an Acetylene but the Bond Energy of Methane?," J. Am. Chem. Soc. 2003, 125, 11746-11750, DOI: 10.1021/ja035725s. S, Cp copied from Cds_S""",
    longDesc = 
u"""

""",
)

entry(
    index        = 146,
    label        = "cyclobutene-vinyl",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   C U0 {2,S} {4,S}
2   C U0 {1,S} {3,S}
3 * C U1 {2,S} {4,D}
4   C U0 {1,S} {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (112.5,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""Tian, Z.; Fattahi, A.; Lis, L.; Kass, S. R., "Cycloalkane and Cycloalkene C-H Bond Dissociation Energies," J. Am. Chem. Soc. 2006, 128, 17087-17092, DOI: 10.1021/ja065348u S, Cp copied from Cds_S""",
    longDesc = 
u"""

""",
)

entry(
    index        = 178,
    label        = "cyclopentene-vinyl",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   C U0 {2,S} {3,S}
2   C U0 {1,S} {5,S}
3   C U0 {1,S} {4,S}
4 * C U1 {3,S} {5,D}
5   C U0 {2,S} {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (113.7,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
u"""

""",
)

entry(
    index        = 180,
    label        = "1,3-cyclopentadiene-vinyl-1",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   C U0 {2,S} {3,S}
2 * C U1 {1,S} {4,D}
3   C U0 {1,S} {5,D}
4   C U0 {2,D} {5,S}
5   C U0 {3,D} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (116.9,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
u"""

""",
)

entry(
    index        = 184,
    label        = "bicyclo[2.1.0]pent-2-ene-C2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   C U0 {2,S} {3,S} {5,S}
2   C U0 {1,S} {3,S} {4,S}
3   C U0 {1,S} {2,S}
4 * C U1 {2,S} {5,D}
5   C U0 {1,S} {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (109.8,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
u"""

""",
)

entry(
    index        = 187,
    label        = "bicyclo[2.1.1]hex-2-ene-C2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   C U0 {3,S} {4,S} {6,S}
2   C U0 {3,S} {4,S} {5,S}
3   C U0 {1,S} {2,S}
4   C U0 {1,S} {2,S}
5 * C U1 {2,S} {6,D}
6   C U0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (115.9,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
u"""

""",
)

entry(
    index        = 189,
    label        = "tricyclo[2.1.1.0(1,4)]hex-2-ene-C2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   C U0 {2,S} {3,S} {4,S} {6,S}
2   C U0 {1,S} {3,S} {4,S} {5,S}
3   C U0 {1,S} {2,S}
4   C U0 {1,S} {2,S}
5 * C U1 {2,S} {6,D}
6   C U0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (108.6,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
u"""

""",
)

entry(
    index        = 192,
    label        = "bicyclo[2.2.0]hexa-2,5-diene-C2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1   C U0 {2,S} {3,S} {6,S}
2   C U0 {1,S} {4,S} {5,S}
3 * C U1 {1,S} {4,D}
4   C U0 {2,S} {3,D}
5   C U0 {2,S} {6,D}
6   C U0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.34,-1.21,-1.94,-2.52,-3.34,-3.91,-4.76],'cal/(mol*K)'),
        H298 = (111.6,'kcal/mol'),
        S298 = (1.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""Homolytic C-H and N-H bond dissociation energies of strained organic compounds Feng et al. 2004S, Cp copied from Cds_S""",
    longDesc = 
u"""

""",
)

entry(
    index        = 257,
    label        = "CdsJ-Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Cd U1 {2,S} {3,D}
2   Ss U0 {1,S}
3   C  U0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.16,-0.48,-1.16,-1.76,-2.68,-3.35,-4.45],'cal/(mol*K)'),
        H298 = (104.73,'kcal/mol'),
        S298 = (0.37,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 91,
    label        = "CtJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,T}
2   C U0 {1,T}
""",
    thermo = u'Acetyl',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 92,
    label        = "Acetyl",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,T}
2   C U0 {1,T} {3,S}
3   H U0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.51,-1.56,-2.27,-2.78,-3.47,-3.97,-3.97],'cal/(mol*K)'),
        H298 = (132.7,'kcal/mol'),
        S298 = (2.11,'cal/(mol*K)'),
    ),
    shortDesc = u"""LAY et al.""",
    longDesc = 
u"""

""",
)

entry(
    index        = 93,
    label        = "CbJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * C U1 {2,B} {3,B}
2   C U0 {1,B}
3   C U0 {1,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.41,-1.18,-1.93,-2.69,-3.75,-4.48,-5.24],'cal/(mol*K)'),
        H298 = (113,'kcal/mol'),
        S298 = (1.48,'cal/(mol*K)'),
    ),
    shortDesc = u"""BDE from TSANG, S and Cp from THERM""",
    longDesc = 
u"""

""",
)

entry(
    index        = 94,
    label        = "OJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * O U1
""",
    thermo = u'COJ',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 95,
    label        = "HOJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * O U1 {2,S}
2   H U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.87,-1.1,-1.36,-1.62,-2.11,-2.53,-3.38],'cal/(mol*K)'),
        H298 = (119.22,'kcal/mol'),
        S298 = (-2.6,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated from NIST values for H2O, OH and H""",
    longDesc = 
u"""

""",
)

entry(
    index        = 135,
    label        = "COJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * O U1 {2,S}
2   C U0 {1,S}
""",
    thermo = u'CsOJ',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 96,
    label        = "CsOJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * O  U1 {2,S}
2   Cs U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.98,-1.3,-1.61,-1.89,-2.38,-2.8,-3.59],'cal/(mol*K)'),
        H298 = (104.06,'kcal/mol'),
        S298 = (-1.46,'cal/(mol*K)'),
    ),
    shortDesc = u"""CHEN & BOZZELLI(ROJ)""",
    longDesc = 
u"""

""",
)

entry(
    index        = 97,
    label        = "H3COJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * O U1 {2,S}
2   C U0 {1,S} {3,S} {4,S} {5,S}
3   H U0 {2,S}
4   H U0 {2,S}
5   H U0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.11,-1.29,-1.62,-1.97,-2.59,-3.07,-3.84],'cal/(mol*K)'),
        H298 = (104.27,'kcal/mol'),
        S298 = (0.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Enthalpy HBI calculated from NIST values, entropy and Cp from B3LYP/6-31G* for CH3OH, CH3O and H""",
    longDesc = 
u"""

""",
)

entry(
    index        = 98,
    label        = "CdsOJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * O       U1 {2,S}
2   {Cd,CO} U0 {1,S}
""",
    thermo = u'RC=COJ',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 99,
    label        = "RC=COJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * O  U1 {2,S}
2   Cd U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.34,-1.99,-2.48,-2.79,-3.13,-3.33,-3.79],'cal/(mol*K)'),
        H298 = (88,'kcal/mol'),
        S298 = (-1.11,'cal/(mol*K)'),
    ),
    shortDesc = u"""CHEN & BOZZELLI""",
    longDesc = 
u"""

""",
)

entry(
    index        = 100,
    label        = "OJC=O",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * O  U1 {2,S}
2   CO U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.31,-1.87,-2.32,-2.69,-3.28,-3.74,-4.56],'cal/(mol*K)'),
        H298 = (104,'kcal/mol'),
        S298 = (0.79,'cal/(mol*K)'),
    ),
    shortDesc = u"""CHEN & BOZZELLI""",
    longDesc = 
u"""

""",
)

entry(
    index        = 217,
    label        = "CbOJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * O  U1 {2,S}
2   Cb U0 {1,S}
""",
    thermo = u'RC=COJ',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 101,
    label        = "OOJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * O U1 {2,S}
2   O U0 {1,S}
""",
    thermo = u'ROOJ',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 102,
    label        = "ROOJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * O   U1 {2,S}
2   O   U0 {1,S} {3,S}
3   R!H U0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.05,-2.84,-3.55,-4.09,-4.72,-4.97,-5.08],'cal/(mol*K)'),
        H298 = (88.2,'kcal/mol'),
        S298 = (0.22,'cal/(mol*K)'),
    ),
    shortDesc = u"""CHEN & BOZZELLI""",
    longDesc = 
u"""

""",
)

entry(
    index        = 104,
    label        = "C(=O)OOJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * O U1 {2,S}
2   O U0 {1,S} {3,S}
3   C U0 {2,S} {4,D}
4   O U0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.05,-2.84,-3.55,-4.09,-4.72,-4.97,-5.08],'cal/(mol*K)'),
        H298 = (98.33,'kcal/mol'),
        S298 = (0.22,'cal/(mol*K)'),
    ),
    shortDesc = u"""HBI for enthalpy from CHEN & BOZZELLI. Cp and S values taken from ROOJ""",
    longDesc = 
u"""

""",
)

entry(
    index        = 103,
    label        = "C3COOJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * O U1 {2,S}
2   O U0 {1,S} {3,S}
3   C U0 {2,S} {4,S} {5,S} {6,S}
4   C U0 {3,S}
5   C U0 {3,S}
6   C U0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.05,-2.84,-3.55,-4.09,-4.72,-4.97,-5.08],'cal/(mol*K)'),
        H298 = (85.3,'kcal/mol'),
        S298 = (0.22,'cal/(mol*K)'),
    ),
    shortDesc = u"""CHEN & BOZZELLI""",
    longDesc = 
u"""

""",
)

entry(
    index        = 105,
    label        = "HOOJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * O U1 {2,S}
2   O U0 {1,S} {3,S}
3   H U0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.99,-2.68,-3.07,-3.3,-3.55,-3.66,-3.9],'cal/(mol*K)'),
        H298 = (85.13,'kcal/mol'),
        S298 = (-0.92,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated from NIST values for H2O2, O2H and H""",
    longDesc = 
u"""

""",
)

entry(
    index        = 134,
    label        = "SiJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Si U1
""",
    thermo = u'CJ',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 137,
    label        = "SJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U1
""",
    thermo = u'OJ',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 235,
    label        = "SJ-H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U1 {2,S}
2   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.2,-1.52,-1.84,-2.17,-2.73,-3.2,-3.95],'cal/(mol*K)'),
        H298 = (91.82,'kcal/mol'),
        S298 = (-4.62,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "SJ-C",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U1 {2,S}
2   C  U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 236,
    label        = "SJ-Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U1 {2,S}
2   Cs U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.94,-2.78,-2.72,-2.78,-3.07,-3.41,-4.04],'cal/(mol*K)'),
        H298 = (86.98,'kcal/mol'),
        S298 = (-2.77,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 238,
    label        = "SJ-Ct",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U1 {2,S}
2   Ct U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.18,-2.05,-2.66,-3.12,-3.76,-4.24,-4.99],'cal/(mol*K)'),
        H298 = (77.56,'kcal/mol'),
        S298 = (-4.6,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 239,
    label        = "SJ-Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U1 {2,S}
2   Cb U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.92,-2.1,-2.3,-2.51,-2.93,-3.32,-3.96],'cal/(mol*K)'),
        H298 = (81.36,'kcal/mol'),
        S298 = (-3.66,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 237,
    label        = "SJ-Cd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U1 {2,S}
2   Cd U0 {1,S} {3,D}
3   C  U0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.29,-2.56,-2.72,-2.87,-3.19,-3.52,-4.13],'cal/(mol*K)'),
        H298 = (79.29,'kcal/mol'),
        S298 = (-1.79,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 240,
    label        = "SJ-C=S",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U1 {2,S}
2   Cd U0 {1,S} {3,D}
3   Sd U0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.93,-3.56,-3.88,-4.08,-4.41,-4.74,-5.25],'cal/(mol*K)'),
        H298 = (80.07,'kcal/mol'),
        S298 = (-0.7,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 266,
    label        = "SJ-CO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U1 {2,S}
2   C  U0 {1,S} {3,D}
3   Od U0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.33,-2.82,-3.2,-3.55,-4.16,-4.61,-5.12],'cal/(mol*K)'),
        H298 = (89.86,'kcal/mol'),
        S298 = (-0.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 CAC""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "SJ-Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U1 {2,S}
2   Ss U0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 241,
    label        = "SJ-Ss-H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U1 {2,S}
2   Ss U0 {1,S} {3,S}
3   H  U0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.93,-2.7,-3.26,-3.67,-4.24,-4.59,-5],'cal/(mol*K)'),
        H298 = (73.97,'kcal/mol'),
        S298 = (-2.53,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 242,
    label        = "SJ-Ss-Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U1 {2,S}
2   Ss U0 {1,S} {3,S}
3   C  U0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.95,-3.43,-3.78,-4.06,-4.47,-4.74,-5.03],'cal/(mol*K)'),
        H298 = (71.05,'kcal/mol'),
        S298 = (-1.7,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 243,
    label        = "SJ-Ss-Ss",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 * Ss U1 {2,S}
2   Ss U0 {1,S} {3,S}
3   S  U0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.63,-4.32,-4.84,-5.26,-5.82,-6.07,-5.99],'cal/(mol*K)'),
        H298 = (72.74,'kcal/mol'),
        S298 = (0.6,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2010""",
    longDesc = 
u"""

""",
)

entry(
    index        = 106,
    label        = "RJ2",
    multiplicity = [1, 3],
    group = 
"""
1 * R U2
""",
    thermo = u'CJ2',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 107,
    label        = "CJ2",
    multiplicity = [1, 3],
    group = 
"""
1 * C U2
""",
    thermo = u'CsJ2',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 108,
    label        = "CsJ2",
    multiplicity = [1, 3],
    group = 
"""
1 * Cs U2
""",
    thermo = u'CH2',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 109,
    label        = "CH2",
    multiplicity = [1, 3],
    group = 
"""
1 * C U2 {2,S} {3,S}
2   H U0 {1,S}
3   H U0 {1,S}
""",
    thermo = u'CH2_t',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 110,
    label        = "CH2_t",
    multiplicity = [3],
    group = 
"""
1 * C U2 {2,S} {3,S}
2   H U0 {1,S}
3   H U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.27,-1.08,-2.14,-3.23,-5.18,-6.74,-9.47],'cal/(mol*K)'),
        H298 = (214.44,'kcal/mol'),
        S298 = (-1.73,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated for methylene in relation to methane from NIST values""",
    longDesc = 
u"""

""",
)

entry(
    index        = 111,
    label        = "CH2_s",
    multiplicity = [1],
    group = 
"""
1 * C U2 {2,S} {3,S}
2   H U0 {1,S}
3   H U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.27,-1.08,-2.14,-3.23,-5.18,-6.74,-9.47],'cal/(mol*K)'),
        H298 = (223.7,'kcal/mol'),
        S298 = (-1.73,'cal/(mol*K)'),
    ),
    shortDesc = u"""BDE JANOSCHEK & ROSSI. S and Cp from CH2_t.""",
    longDesc = 
u"""

""",
)

entry(
    index        = 112,
    label        = "CsJ2_P",
    multiplicity = [1, 3],
    group = 
"""
1 * C U2 {2,S} {3,S}
2   C U0 {1,S}
3   H U0 {1,S}
""",
    thermo = u'CsCsJ2',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 113,
    label        = "CsCsJ2",
    multiplicity = [1, 3],
    group = 
"""
1 * C  U2 {2,S} {3,S}
2   Cs U0 {1,S}
3   H  U0 {1,S}
""",
    thermo = u'CCJ2',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 114,
    label        = "CCJ2",
    multiplicity = [1, 3],
    group = 
"""
1 * C  U2 {2,S} {3,S}
2   Cs U0 {1,S} {4,S} {5,S} {6,S}
3   H  U0 {1,S}
4   H  U0 {2,S}
5   H  U0 {2,S}
6   H  U0 {2,S}
""",
    thermo = u'CCJ2_t',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 115,
    label        = "CCJ2_t",
    multiplicity = [3],
    group = 
"""
1 * C  U2 {2,S} {3,S}
2   Cs U0 {1,S} {4,S} {5,S} {6,S}
3   H  U0 {1,S}
4   H  U0 {2,S}
5   H  U0 {2,S}
6   H  U0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.81,-1.74,-2.69,-3.61,-5.18,-6.42,-8.36],'cal/(mol*K)'),
        H298 = (211.3,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""BDE and Cp calculated from data in KIM et al.""",
    longDesc = 
u"""

""",
)

entry(
    index        = 116,
    label        = "CCJ2_s",
    multiplicity = [1],
    group = 
"""
1 * C  U2 {2,S} {3,S}
2   Cs U0 {1,S} {4,S} {5,S} {6,S}
3   H  U0 {1,S}
4   H  U0 {2,S}
5   H  U0 {2,S}
6   H  U0 {2,S}
""",
    thermo = u'CCJ2_t',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 117,
    label        = "PhCH",
    multiplicity = [1, 3],
    group = 
"""
1 * C  U2 {2,S} {3,S}
2   Cb U0 {1,S}
3   H  U0 {1,S}
""",
    thermo = u'PhCH_t',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 118,
    label        = "PhCH_t",
    multiplicity = [3],
    group = 
"""
1 * C  U2 {2,S} {3,S}
2   Cb U0 {1,S}
3   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (195,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""BDE from PUTSMA et al.""",
    longDesc = 
u"""

""",
)

entry(
    index        = 119,
    label        = "PhCH_s",
    multiplicity = [1],
    group = 
"""
1 * C  U2 {2,S} {3,S}
2   Cb U0 {1,S}
3   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (205.8,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""BDE from NGUYEN et al.""",
    longDesc = 
u"""

""",
)

entry(
    index        = 120,
    label        = "AllylJ2",
    multiplicity = [1, 3],
    group = 
"""
1 * C  U2 {2,S} {3,S}
2   Cd U0 {1,S}
3   H  U0 {1,S}
""",
    thermo = u'AllylJ2_t',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 121,
    label        = "AllylJ2_t",
    multiplicity = [3],
    group = 
"""
1 * C  U2 {2,S} {3,S}
2   Cd U0 {1,S}
3   H  U0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (192.8,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""BDE from PUTSMA et al.""",
    longDesc = 
u"""

""",
)

entry(
    index        = 122,
    label        = "AllylJ2_s",
    multiplicity = [1],
    group = 
"""
1 * C  U2 {2,S} {3,S}
2   Cd U0 {1,S}
3   H  U0 {1,S}
""",
    thermo = u'AllylJ2_t',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 123,
    label        = "CsJ2_S",
    multiplicity = [1],
    group = 
"""
1 * C U2 {2,S} {3,S}
2   C U0 {1,S}
3   C U0 {1,S}
""",
    thermo = u'CsJ2_P',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 124,
    label        = "CdJ2",
    multiplicity = [1, 3],
    group = 
"""
1 * {Cd,CO} U2
""",
    thermo = u'CCdJ2',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 125,
    label        = "CCdJ2",
    multiplicity = [1, 3],
    group = 
"""
1 * C U2 {2,D}
2   C U0 {1,D}
""",
    thermo = u'CCdJ2_s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 126,
    label        = "CCdJ2_t",
    multiplicity = [3],
    group = 
"""
1 * C U2 {2,D}
2   C U0 {1,D}
""",
    thermo = u'CCdJ2_s',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 127,
    label        = "CCdJ2_s",
    multiplicity = [1],
    group = 
"""
1 * C U2 {2,D}
2   C U0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (190.7,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""BDE from ERWIN et al.""",
    longDesc = 
u"""

""",
)

entry(
    index        = -1,
    label        = "CdJ2-Sd",
    multiplicity = [1, 3],
    group = 
"""
1 * Cd U2 {2,D}
2   Sd U0 {1,D}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 261,
    label        = "CdJ2-Sd_s",
    multiplicity = [1],
    group = 
"""
1 * Cd U2 {2,D}
2   Sd U0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.97,-2.97,-3.85,-4.6,-5.82,-6.79,-8.44],'cal/(mol*K)'),
        H298 = (143.53,'kcal/mol'),
        S298 = (-6.23,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
u"""

""",
)

entry(
    index        = 262,
    label        = "CdJ2-Sd_t",
    multiplicity = [3],
    group = 
"""
1 * Cd U2 {2,D}
2   Sd U0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.42,-2.3,-3.22,-4.04,-5.42,-6.5,-8.29],'cal/(mol*K)'),
        H298 = (238.75,'kcal/mol'),
        S298 = (-3.31,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
u"""

""",
)

entry(
    index        = 129,
    label        = "Oa",
    multiplicity = [1, 3],
    group = 
"""
1 * O U2
""",
    thermo = u'Oa_t',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 130,
    label        = "Oa_t",
    multiplicity = [3],
    group = 
"""
1 * O U2
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.8,-3.05,-3.33,-3.62,-4.24,-4.86,-6.28],'cal/(mol*K)'),
        H298 = (221.55,'kcal/mol'),
        S298 = (-8.02,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated for atomic oxygen in relation to water from NIST values""",
    longDesc = 
u"""

""",
)

entry(
    index        = 131,
    label        = "Oa_s",
    multiplicity = [1],
    group = 
"""
1 * O U2
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.8,-3.05,-3.33,-3.62,-4.24,-4.86,-6.28],'cal/(mol*K)'),
        H298 = (266.9,'kcal/mol'),
        S298 = (-8.02,'cal/(mol*K)'),
    ),
    shortDesc = u"""BDE from SCHALLEY et al. S and Cp values taken from Oa_t""",
    longDesc = 
u"""

""",
)

entry(
    index        = 135,
    label        = "SiJ2",
    multiplicity = [1, 3],
    group = 
"""
1 * Si U2
""",
    thermo = u'CJ2',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 263,
    label        = "SJ2",
    multiplicity = [1, 3],
    group = 
"""
1 * S U2
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.19,-3.52,-3.89,-4.3,-5.12,-5.86,-7.14],'cal/(mol*K)'),
        H298 = (176.42,'kcal/mol'),
        S298 = (-12.02,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 GA 1D-HR Aaron Vandeputte 2009""",
    longDesc = 
u"""

""",
)

entry(
    index        = 132,
    label        = "RJ3",
    multiplicity = [2, 4],
    group = 
"""
1 * R U3
""",
    thermo = u'CJ3',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 133,
    label        = "CJ3",
    multiplicity = [2, 4],
    group = 
"""
1 * C U3
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.57,-2.73,-4.11,-5.5,-7.92,-9.85,-12.95],'cal/(mol*K)'),
        H298 = (316.19,'kcal/mol'),
        S298 = (-5.7,'cal/(mol*K)'),
    ),
    shortDesc = u"""Calculated for methylidyene in relation to methane from NIST values""",
    longDesc = 
u"""

""",
)

entry(
    index        = 136,
    label        = "SiJ3",
    multiplicity = [2, 4],
    group = 
"""
1 * Si U3
""",
    thermo = u'CJ3',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

tree(
"""
L1: Radical
    L2: RJ
        L3: CJ
            L4: CsJ
                L5: CH3
                L5: Cs_P
                    L6: CsCsJ
                        L7: CJCOOH
                        L7: CCJ
                        L7: RCCJ
                        L7: Isobutyl
                        L7: Neopentyl
                    L6: Benzyl_P
                    L6: Allyl_P
                        L7: C=CC=CCJ
                        L7: CTCC=CCJ
                    L6: Propargyl
                    L6: C2JC=O
                L5: Cs_S
                    L6: (Cs)2CsJ
                        L7: cyclopropane
                        L7: cyclobutane
                        L7: bicyclo[1.1.0]butane-secondary
                        L7: CCJCOOH
                        L7: spiro[2.2]pentane-secondary
                        L7: bicyclo[2.1.0]pentane-secondary-C4
                        L7: bicyclo[2.1.0]pentane-secondary-C3
                        L7: cyclopentene-4
                        L7: bicyclo[2.1.0]pent-2-ene-C5
                        L7: bicyclo[1.1.1]pentane-C2
                        L7: tricyclo[1.1.1.0(1,3)]pentane-C2
                        L7: bicyclo[3.1.0]hexane-C5-2
                        L7: bicyclo[3.1.0]hexane-C5-3
                        L7: bicyclo[3.1.0]hexane-C3
                        L7: bicyclo[2.2.0]hexane-secondary
                        L7: bicyclo[2.1.1]hex-2-ene-C5
                        L7: tricyclo[2.1.1.0(1,4)]hex-2-ene-C5
                        L7: bicyclo[2.1.1]hexane-C2
                        L7: bicyclo[2.1.1]hexane-C5
                        L7: tricyclo[2.1.1.0(1,4)]hexane-C2
                        L7: tricyclo[2.1.1.0(1,4)]hexane-C5
                        L7: 7-norbornyl
                        L7: 2-norbornyl
                        L7: cycloheptane
                        L7: bicyclo[3.2.0]heptane-C5-2
                        L7: bicyclo[3.2.0]heptane-C5-3
                        L7: bicyclo[3.2.0]heptane-C5-6
                        L7: bicyclo[4.1.0]heptane-C6-2
                        L7: bicyclo[4.1.0]heptane-C6-3
                        L7: bicyclo[4.1.0]heptane-C3-7
                        L7: bicyclo[4.1.0]heptane-C6-2
                        L7: bicyclo[4.1.0]heptane-C6-3
                        L7: bicyclo[4.1.0]heptane-C3-7
                        L7: bicyclo[3.1.1]heptane-C2
                        L7: bicyclo[3.1.1]heptane-C3
                        L7: bicyclo[3.1.1]heptane-C6
                        L7: tricyclo[3.1.1.0(1,5)]heptane-C2
                        L7: tricyclo[3.1.1.0(1,5)]heptane-C3
                        L7: tricyclo[3.1.1.0(1,5)]heptane-C6
                        L7: tricyclo[2.2.1.0(1,4)]heptane-C2
                        L7: tricyclo[2.2.1.0(1,4)]heptane-C7
                        L7: octahydro-pentalene-C5-2
                        L7: octahydro-pentalene-C5-3
                        L7: bicyclo[4.2.0]octane-C6-2
                        L7: bicyclo[4.2.0]octane-C6-3
                        L7: bicyclo[4.2.0]octane-C4-7
                        L7: bicyclo[2.2.2]octane-C2
                        L7: tricyclo[2.2.2.0(1,4)]octane-C2
                        L7: CCJC
                        L7: RCCJC
                        L7: RCCJCC
                            L8: cyclopentane
                            L8: cyclohexane
                    L6: Benzyl_S
                    L6: Allyl_S
                        L7: cyclobutene-allyl
                        L7: cyclopentene-allyl
                        L7: cyclohexene-allyl
                    L6: C=CCJC=C
                        L7: cyclopropenyl-allyl
                        L7: 1,3-cyclopentadiene-allyl
                    L6: Sec_Propargyl
                    L6: CCJCHO
                L5: Cs_T
                    L6: Tertalkyl
                        L7: bicyclo[1.1.0]butane-tertiary
                        L7: bicyclo[2.1.0]pentane-tertiary
                        L7: bicyclo[1.1.1]pentane-C1
                        L7: C2CJCOOH
                        L7: bicyclo[3.1.0]hexane-tertiary
                        L7: bicyclo[2.2.0]hexane-tertiary
                        L7: bicyclo[2.1.1]hexane-C1
                        L7: bridgehead_norbornyl
                        L7: bicyclo[3.2.0]heptane-tertiary
                        L7: bicyclo[4.1.0]heptane-tertiary
                        L7: bicyclo[3.1.1]heptane-C1
                        L7: octahydro-pentalene-tertiary
                        L7: bicyclo[4.2.0]octane-tertiary
                        L7: bicyclo[2.2.2]octane-C1
                    L6: Benzyl_T
                    L6: Allyl_T
                        L7: bicyclo[2.1.0]pent-2-ene-C1
                        L7: bicyclo[2.1.1]hex-2-ene-C1
                    L6: Tert_Propargyl
                    L6: C2CJCO
                        L7: C2CJCHO
                    L6: bicyclo[2.2.0]hexa-2,5-diene-C1
                L5: CsJO
                    L6: CsJOH
                    L6: CsJOC
                        L7: CsJOCs
                            L8: CsJOCH3
                            L8: CsJOCC
                            L8: CsJOCC2
                            L8: CsJOCC3
                        L7: CsJOCds
                            L8: CsJOC(O)
                                L9: CsJOC(O)H
                                L9: CsJOC(O)C
                    L6: CsJOO
                        L7: CsJOOH
                        L7: CsJOOC
                L5: CCsJO
                    L6: CCsJOH
                    L6: CCsJOC
                        L7: CCsJOCs
                        L7: CCsJOCds
                            L8: CCsJOC(O)
                                L9: CCsJOC(O)H
                                L9: CCsJOC(O)C
                    L6: CCsJOO
                        L7: CCsJOOH
                        L7: CCsJOOC
                L5: C2CsJO
                    L6: C2CsJOH
                    L6: C2CsJOC
                        L7: C2CsJOCs
                        L7: C2CsJOCds
                            L8: C2CsJOC(O)
                                L9: C2CsJOC(O)H
                                L9: C2CsJOC(O)C
                    L6: C2CsJOO
                        L7: C2CsJOOH
                        L7: C2CsJOOC
                L5: CCsJOS
                    L6: CCsJOHSH
                L5: CsJ-S
                    L6: CsJ-SsHH
                    L6: CsJ-CSH
                        L7: CsJ-CsSsH
                        L7: CsJ-CtSsH
                        L7: CsJ-CbSsH
                        L7: CsJ-CdSsH
                        L7: CsJ-C=SSsH
                    L6: CsJ-CCS
                        L7: CsJ-CsCsSs
                        L7: CsJ-CsCtSs
                        L7: CsJ-CsCbSs
                        L7: CsJ-CsCdSs
                        L7: CsJ-CsC=SSs
                L5: CsJ-SS
                    L6: CsJ-SsSsH
                    L6: CsJ-CSS
                        L7: CsJ-CsSsSs
                        L7: CsJ-CtSsSs
                        L7: CsJ-CbSsSs
                        L7: CsJ-CdSsSs
                        L7: CsJ-C=SSsSs
                L5: CsJ-SsSsSs
                L5: CsJN
                L5: CCsJN
                L5: C2CsJN
            L4: CdsJ
                L5: CdsJO
                    L6: HCdsJO
                    L6: CCJ=O
                        L7: CsCJ=O
                        L7: C=CCJ=O
                    L6: (O)CJO
                        L7: (O)CJOH
                        L7: (O)CJOC
                            L8: (O)CJOCH3
                            L8: (O)CJOCC
                            L8: (O)CJOCC2
                            L8: (O)CJOCC3
                L5: C=SJ
                    L6: C=SJ-H
                    L6: C=SJ-C
                        L7: C=SJ-Cs
                        L7: C=SJ-Cd
                    L6: C=SJ-Ss
                L5: Cds_P
                    L6: C=C=CJ
                L5: Cds_S
                    L6: C=CJC=C
                        L7: cyclobutadiene-C1
                        L7: 1,3-cyclopentadiene-vinyl-2
                        L7: bicyclo[2.2.0]hexa-1(4),2,5-triene-C2
                    L6: cyclopropenyl-vinyl
                    L6: cyclobutene-vinyl
                    L6: cyclopentene-vinyl
                    L6: 1,3-cyclopentadiene-vinyl-1
                    L6: bicyclo[2.1.0]pent-2-ene-C2
                    L6: bicyclo[2.1.1]hex-2-ene-C2
                    L6: tricyclo[2.1.1.0(1,4)]hex-2-ene-C2
                    L6: bicyclo[2.2.0]hexa-2,5-diene-C2
                L5: CdsJ-Ss
            L4: CtJ
                L5: Acetyl
            L4: CbJ
        L3: OJ
            L4: HOJ
            L4: COJ
                L5: CsOJ
                    L6: H3COJ
                L5: CdsOJ
                    L6: RC=COJ
                    L6: OJC=O
                L5: CbOJ
            L4: OOJ
                L5: ROOJ
                    L6: C(=O)OOJ
                    L6: C3COOJ
                L5: HOOJ
        L3: SiJ
        L3: SJ
            L4: SJ-H
            L4: SJ-C
                L5: SJ-Cs
                L5: SJ-Ct
                L5: SJ-Cb
                L5: SJ-Cd
                L5: SJ-C=S
                L5: SJ-CO
            L4: SJ-Ss
                L5: SJ-Ss-H
                L5: SJ-Ss-Cs
                L5: SJ-Ss-Ss
    L2: RJ2
        L3: CJ2
            L4: CsJ2
                L5: CH2
                    L6: CH2_t
                    L6: CH2_s
                L5: CsJ2_P
                    L6: CsCsJ2
                        L7: CCJ2
                            L8: CCJ2_t
                            L8: CCJ2_s
                    L6: PhCH
                        L7: PhCH_t
                        L7: PhCH_s
                    L6: AllylJ2
                        L7: AllylJ2_t
                        L7: AllylJ2_s
                L5: CsJ2_S
            L4: CdJ2
                L5: CCdJ2
                    L6: CCdJ2_t
                    L6: CCdJ2_s
                L5: CdJ2-Sd
                    L6: CdJ2-Sd_s
                    L6: CdJ2-Sd_t
        L3: Oa
            L4: Oa_t
            L4: Oa_s
        L3: SiJ2
        L3: SJ2
    L2: RJ3
        L3: CJ3
        L3: SiJ3
"""
)

